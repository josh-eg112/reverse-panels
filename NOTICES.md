# Notices

Reverse Panels includes the following third-party components.

## Panel detector model

- Architecture: SSDLite320 with a MobileNetV3-Large backbone from torchvision (BSD-3-Clause).
- The bundled Core ML model was trained from a random initialization (no ImageNet weights). It runs
  only on your device.

## libarchive (via libarchive-swift)

- Project: libarchive — general-purpose archive-reading library
- Home: <https://www.libarchive.org/> (source: <https://github.com/libarchive/libarchive>)
- Copyright (c) 2003-2024 Tim Kientzle and contributors
- License: 2-Clause BSD

> These terms are distributed with libarchive as its LICENSE (the library is a
> collection of code contributed under permissive licenses; the aggregate
> library is released under the terms below, and individual files retain their
> own copyright headers).

```
Copyright (c) Tim Kientzle and contributors.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
```

Some libarchive compression/decompression back ends used by ComicReader (for
example DEFLATE/raw deflate support) may be derived from or bundled alongside
other permissively licensed implementations; per-file copyright and license
notices are retained in the libarchive source and are incorporated by this
notice.

## libarchive-swift

- Project: libarchive-swift (kmworks / originally everpcpc) — Swift bindings over libarchive
- Home: <https://github.com/kmworks/libarchive-swift>
- Copyright (c) everpcpc and contributors
- License: BSD 2-Clause

> Distributed under the `LibArchive` package product, minimum version 0.1.6.

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```