#!/usr/bin/env python3
"""Run eggNOG-mapper 2.1.13 with ``eggnog.db`` read from a seekable zstd-chunk store.

The emapper 5.0.2 annotation database (``eggnog.db``) is a 41 GB SQLite file,
larger than the disk available where this evaluation was run. It is therefore
stored as independently zstd-compressed 256 KiB chunks (``eggnog.db.zc`` plus an
offset index ``eggnog.db.zci``; see ``zchunk_build_http.py``) and served
read-only to SQLite through an apsw VFS. Bytes returned to SQLite are identical
to the original file, so emapper's queries and results are unchanged; only
``AnnotDB.__init__`` is replaced, to open the connection through that VFS.

Usage (all ordinary emapper arguments are passed through):
  run_emapper.py --zchunk DATA_DIR/eggnog.db -- <emapper.py arguments>
``DATA_DIR`` must also hold ``eggnog_proteins.dmnd`` and ``eggnog.taxa.db``,
plus an (empty) placeholder file named ``eggnog.db`` for emapper's existence check.
"""
from __future__ import annotations

import functools
import os
import struct
import sys

import apsw
import zstandard as zstd


class ZChunkFile:
    def __init__(self, base: str, cache_chunks: int = 4096):
        with open(base + ".zci", "rb") as fh:
            self.chunk, self.size = struct.unpack("<QQ", fh.read(16))
            raw = fh.read()
        self.offs = struct.unpack(f"<{len(raw) // 8}Q", raw)
        self.fh = open(base + ".zc", "rb")
        self.dctx = zstd.ZstdDecompressor()
        self.get = functools.lru_cache(maxsize=cache_chunks)(self._load)

    def _load(self, i: int) -> bytes:
        self.fh.seek(self.offs[i])
        return self.dctx.decompress(self.fh.read(self.offs[i + 1] - self.offs[i]))

    def read(self, amount: int, offset: int) -> bytes:
        out = bytearray()
        while amount > 0 and offset < self.size:
            i, o = divmod(offset, self.chunk)
            piece = self.get(i)[o:o + amount]
            out += piece
            amount -= len(piece)
            offset += len(piece)
        return bytes(out) + b"\0" * amount  # short read past EOF is zero-filled


class _File:
    def __init__(self, store: ZChunkFile):
        self.store = store

    def xRead(self, amount, offset):
        return self.store.read(amount, offset)

    def xFileSize(self):
        return self.store.size

    def xClose(self): pass
    def xLock(self, level): pass
    def xUnlock(self, level): pass
    def xCheckReservedLock(self): return False
    def xFileControl(self, op, ptr): return False
    def xSectorSize(self): return 4096
    def xDeviceCharacteristics(self): return 0
    def xSync(self, flags): pass

    def xWrite(self, data, offset):
        raise apsw.ReadOnlyError("zchunk store is read-only")

    def xTruncate(self, size):
        raise apsw.ReadOnlyError("zchunk store is read-only")


class ZChunkVFS(apsw.VFS):
    def __init__(self, base: str):
        self.base = base
        self.store = None
        super().__init__("zchunk", "")

    def xOpen(self, name, flags):
        if self.store is None:  # opened lazily so each forked worker has its own handle
            self.store = ZChunkFile(self.base)
        return _File(self.store)

    def xAccess(self, pathname, flags):
        return False  # no journals / WAL files exist


def install(base: str) -> None:
    vfs = ZChunkVFS(base)
    from eggnogmapper.annotation import db_sqlite

    def __init__(self, usemem=False):
        self._vfs = vfs
        self.conn = apsw.Connection("eggnog.db", flags=apsw.SQLITE_OPEN_READONLY, vfs="zchunk")
        self.conn.execute("PRAGMA cache_size=2000;")

    db_sqlite.AnnotDB.__init__ = __init__


def main() -> None:
    argv = sys.argv[1:]
    if not argv or argv[0] != "--zchunk" or "--" not in argv:
        sys.exit(__doc__)
    base = argv[1]
    emapper_args = argv[argv.index("--") + 1:]
    install(os.path.abspath(base))
    from eggnogmapper.emapper import Emapper  # noqa: F401  (import check)
    import runpy
    sys.argv = ["emapper.py"] + emapper_args
    script = os.path.join(os.path.dirname(sys.executable), "emapper.py")
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    main()
