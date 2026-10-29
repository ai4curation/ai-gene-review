"""Stream a remote .gz over HTTP (resuming with Range requests after drops) and
write the decompressed bytes as independently zstd-compressed fixed-size chunks:
<out>.zc (data) and <out>.zci (header: chunk size, total; then uint64 offsets)."""
import sys, struct, time, zlib, urllib.request, zstandard as zstd
from concurrent.futures import ThreadPoolExecutor
url, out = sys.argv[1], sys.argv[2]
CHUNK = 256 * 1024
dec = zlib.decompressobj(16 + zlib.MAX_WBITS)
pos = 0          # compressed bytes consumed
buf = bytearray()
offs = [0]; total = 0
ex = ThreadPoolExecutor(4)
f = open(out + '.zc', 'wb')
def comp(b): return zstd.ZstdCompressor(level=3).compress(b)
def flush(final=False):
    global buf, total
    n = len(buf) // CHUNK
    if final and len(buf) % CHUNK: n += 1
    if not n: return
    pieces = [bytes(buf[i*CHUNK:(i+1)*CHUNK]) for i in range(n)]
    del buf[:n*CHUNK]
    for c in ex.map(comp, pieces):
        f.write(c); offs.append(offs[-1] + len(c))
    total += sum(len(p) for p in pieces)
last = 0; fails = 0
while not dec.eof:
    try:
        req = urllib.request.Request(url, headers={'Range': f'bytes={pos}-'})
        with urllib.request.urlopen(req, timeout=120) as r:
            while True:
                data = r.read(4 << 20)
                if not data: break
                pos += len(data)
                buf += dec.decompress(data)
                if len(buf) >= 256 * CHUNK: flush()
                if total - last > 2e9:
                    last = total; print(f'{pos/1e9:.2f} GB gz, {total/1e9:.1f} GB raw, {offs[-1]/1e9:.2f} GB zc', file=sys.stderr, flush=True)
        if not dec.eof:
            raise IOError('stream ended early')
    except Exception as e:
        fails += 1
        print(f'retry {fails} at gz offset {pos}: {e}', file=sys.stderr, flush=True)
        if fails > 200: sys.exit(1)
        time.sleep(min(30, 2 * fails))
flush(final=True)
f.close()
with open(out + '.zci', 'wb') as g:
    g.write(struct.pack('<QQ', CHUNK, total)); g.write(struct.pack(f'<{len(offs)}Q', *offs))
print('done', total, offs[-1], file=sys.stderr)
