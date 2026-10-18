#!/usr/bin/env python3
"""Verify that a zstd-chunk store reproduces the original file byte for byte.

Streams the original .gz from URL (resuming with Range requests after drops) and
the store's chunks, computes SHA-256 of both decompressed streams, and prints
both digests and the byte counts.

Usage: verify_zchunk.py URL STORE_BASE   (STORE_BASE without .zc/.zci)"""
import hashlib
import struct
import sys
import time
import urllib.request
import zlib

import zstandard as zstd

url, base = sys.argv[1], sys.argv[2]

h_store, n_store = hashlib.sha256(), 0
with open(base + ".zci", "rb") as fh:
    chunk, size = struct.unpack("<QQ", fh.read(16))
    raw = fh.read()
offs = struct.unpack(f"<{len(raw) // 8}Q", raw)
dctx = zstd.ZstdDecompressor()
with open(base + ".zc", "rb") as zc:
    for i in range(len(offs) - 1):
        b = dctx.decompress(zc.read(offs[i + 1] - offs[i]))
        h_store.update(b)
        n_store += len(b)

h_orig, n_orig, pos = hashlib.sha256(), 0, 0
dec = zlib.decompressobj(16 + zlib.MAX_WBITS)
fails = 0
while not dec.eof:
    try:
        req = urllib.request.Request(url, headers={"Range": f"bytes={pos}-"})
        with urllib.request.urlopen(req, timeout=120) as r:
            while True:
                data = r.read(4 << 20)
                if not data:
                    break
                pos += len(data)
                b = dec.decompress(data)
                h_orig.update(b)
                n_orig += len(b)
        if not dec.eof:
            raise IOError("stream ended early")
    except Exception as e:  # noqa: BLE001 - resume on any transfer error
        fails += 1
        if fails > 200:
            sys.exit(f"giving up: {e}")
        time.sleep(min(30, 2 * fails))

print(f"original  sha256={h_orig.hexdigest()} bytes={n_orig}")
print(f"zchunk    sha256={h_store.hexdigest()} bytes={n_store} (index says {size})")
print("IDENTICAL" if (h_orig.hexdigest(), n_orig) == (h_store.hexdigest(), n_store) else "DIFFERENT")
