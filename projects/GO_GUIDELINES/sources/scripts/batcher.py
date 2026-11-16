import pathlib
def write_batches(items, outdir, prefix, size, limit):
    """items: list of (id, text). Writes outdir/prefix-NN.md batches; returns names."""
    outdir = pathlib.Path(outdir); outdir.mkdir(parents=True, exist_ok=True); names = []
    for k in range(0, len(items), size):
        buf = []
        for id, txt in items[k:k + size]:
            if len(txt) > limit: txt = txt[:limit] + f"\n[... truncated, {len(txt)} chars total]"
            buf.append(f"=== ITEM {id}\n{txt}\n")
        n = f"{prefix}-{k // size:02d}.md"; (outdir / n).write_text("".join(buf)); names.append(n)
    return names
