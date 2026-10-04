#!/usr/bin/env python3
"""Add a beta build to the SideStore/AltStore source (docs/apps.json).

Reads the version, build, and minimum iOS straight from the IPA's Info.plist, so the source can
never disagree with the binary. Prints the `gh release create` command for the matching tag.

    scripts/add_release.py path/to/ReversePanels.ipa --beta 2 --notes "Fixes ..."
"""
import argparse, datetime as dt, json, plistlib, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/apps.json"
REPO = "josh-eg112/reverse-panels"
BUNDLE_ID = "com.comicreader.app"


def ipa_info(ipa: Path) -> dict:
    with zipfile.ZipFile(ipa) as z:
        name = next(n for n in z.namelist() if re.fullmatch(r"Payload/[^/]+\.app/Info\.plist", n))
        plist = plistlib.loads(z.read(name))
    return {"version": plist["CFBundleShortVersionString"], "build": plist["CFBundleVersion"],
            "min_os": plist.get("MinimumOSVersion", "17.0"), "bundle": plist["CFBundleIdentifier"]}


def asset_name(info: dict) -> str:
    return f"ReversePanels-{info['version']}-{info['build']}.ipa"


def add_version(source: dict, info: dict, *, beta: int, notes: str, size: int, date: str) -> dict:
    app = next(a for a in source["apps"] if a["bundleIdentifier"] == BUNDLE_ID)
    if info["bundle"] != BUNDLE_ID:
        raise SystemExit(f"IPA bundle {info['bundle']} is not {BUNDLE_ID}")
    tag = f"v{info['version']}-beta.{beta}"
    for existing in app["versions"]:
        if (existing["version"], existing["buildVersion"]) == (info["version"], info["build"]):
            raise SystemExit(f"{info['version']} ({info['build']}) is already in the source; bump the build number")
    entry = {"version": info["version"], "buildVersion": info["build"], "date": date,
             "localizedDescription": f"Beta {beta}: {notes}",
             "downloadURL": f"https://github.com/{REPO}/releases/download/{tag}/{asset_name(info)}",
             "size": size, "minOSVersion": info["min_os"]}
    app["versions"].insert(0, entry)
    # Legacy top-level fields for older SideStore/AltStore clients.
    app.update({"version": entry["version"], "versionDate": date, "versionDescription": entry["localizedDescription"],
                "downloadURL": entry["downloadURL"], "size": size})
    return entry | {"tag": tag}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("ipa", type=Path)
    parser.add_argument("--beta", type=int, required=True, help="beta number for the tag and notes")
    parser.add_argument("--notes", required=True, help="one-line release notes")
    args = parser.parse_args()
    info = ipa_info(args.ipa)
    source = json.loads(SOURCE.read_text())
    entry = add_version(source, info, beta=args.beta, notes=args.notes, size=args.ipa.stat().st_size,
                        date=dt.date.today().isoformat())
    SOURCE.write_text(json.dumps(source, indent=2) + "\n")
    print(f"added {entry['version']} ({entry['buildVersion']}) as {entry['tag']}")
    print(f"cp {args.ipa} {asset_name(info)}")
    print(f"gh release create {entry['tag']} {asset_name(info)} --repo {REPO} --prerelease "
          f"--title 'Reverse Panels {entry['version']} Beta {args.beta}' --notes-file CHANGELOG.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
