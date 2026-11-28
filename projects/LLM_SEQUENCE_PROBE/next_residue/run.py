"""Subsample replication of the next-amino-acid probe. Usage: run.py CLONE MODEL EFFORT [CONDITIONS]

CLONE is a checkout of github.com/XinmingTu/LLM-bioseq-probe (results here used commit 0d8d086); only its
data/confirm_sequences.tsv is read. CONDITIONS is 2 (real, shuffled) or 3 (adds reversed). Calls the local
`claude` CLI with no tools and an empty system prompt. Appends to results/EFFORT/MODEL.jsonl and resumes.
"""
import csv, json, pathlib, random, subprocess, sys, zlib, re, collections
from concurrent.futures import ThreadPoolExecutor
S = sys.argv[1]; model = sys.argv[2]; EFF = sys.argv[3]; NCOND = int(sys.argv[4]) if len(sys.argv) > 4 else 2
HERE = pathlib.Path(__file__).parent; (HERE / "results" / EFF).mkdir(parents=True, exist_ok=True); out = str(HERE / "results" / EFF / f"{model}.jsonl")
AA = "ACDEFGHIKLMNPQRSTVWY"
def fasta(s, w=60): return "\n".join(s[i:i+w] for i in range(0, len(s), w))
def prompt(prefix):
    return ("Below is the beginning of a protein sequence in one-letter amino acid codes. "
            "Predict how it continues. Reply with exactly the next 10 amino acids as one-letter "
            "codes on one line, and nothing else.\n\n>sequence\n" + fasta(prefix))
def shuffled(seq, acc):
    r = list(seq); random.Random(zlib.crc32(acc.encode())).shuffle(r); return "".join(r)
rows = list(csv.DictReader(open(f"{S}/data/confirm_sequences.tsv"), delimiter="\t"))
byfam = collections.defaultdict(list)
for r in rows: byfam[(r["size_bin"], r["pfam"])].append(r)
rng = random.Random(20261118)
bins = collections.defaultdict(list)
for (b, f) in sorted(byfam): bins[b].append(f)
qs = []
for b in sorted(bins):
    for f in rng.sample(bins[b], 17):
        r = rng.choice(byfam[(b, f)]); seq = r["sequence"]; acc = r["accession"]
        for cut in rng.sample([int(c) for c in r["cuts"].split(",")], 2):
            # reversed control: mirror the cut so the same prefix length is shown
            variants = {"real": seq, "shuffled": shuffled(seq, acc), "reversed": seq[::-1]}
            for cond, s in list(variants.items())[:NCOND]:
                qs.append(dict(model=model, accession=acc, pfam=f, size_bin=b, fam_n=int(r["family_proteins"]),
                               condition=cond, cut=cut, prefix=s[:cut], target=s[cut:cut+10]))
done = set()
try:
    for l in open(out):
        d = json.loads(l); done.add((d["accession"], d["condition"], d["cut"]))
except FileNotFoundError: pass
todo = [q for q in qs if (q["accession"], q["condition"], q["cut"]) not in done]
print(len(qs), "questions,", len(todo), "to run", flush=True)
def ask(q):
    for attempt in range(3):
        p = subprocess.run(["claude", "-p", "--model", model, "--system-prompt", "", "--tools", "",
                            "--effort", EFF, "--output-format", "json"],
                           input=prompt(q["prefix"]), capture_output=True, text=True, cwd="/tmp")
        try:
            j = json.loads(p.stdout); break
        except Exception: j = None
    if j is None: return dict(q, error=p.stdout[-300:] + p.stderr[-300:])
    text = j.get("result", "") or ""
    cands = re.findall(r"[ACDEFGHIKLMNPQRSTVWY]{5,}", text.replace(" ", ""))
    pred = cands[-1] if cands else ""
    served = list(j.get("modelUsage", {}).keys())
    q = dict(q); del q["prefix"]
    return dict(q, text=text, pred=pred, valid=bool(pred), first_correct=bool(pred) and pred[0] == q["target"][0],
                exact10=pred[:10] == q["target"], served=served,
                thinking=j.get("usage", {}).get("output_tokens_details", {}).get("thinking_tokens"),
                cost=j.get("total_cost_usd"), is_error=j.get("is_error"))
with ThreadPoolExecutor(8) as ex, open(out, "a") as fh:
    for i, r in enumerate(ex.map(ask, todo)):
        fh.write(json.dumps(r) + "\n"); fh.flush()
        if i % 50 == 0: print(i, flush=True)
