import json, pathlib, random, subprocess, sys, zlib, re
from concurrent.futures import ThreadPoolExecutor
HERE = pathlib.Path(__file__).parent; model, eff = sys.argv[1], sys.argv[2]; out = str(HERE / "results" / f"{model}.jsonl")
T = json.load(open(HERE / "truth.json"))
def fasta(s, w=60): return "\n".join(s[i:i+w] for i in range(0, len(s), w))
def shuffled(seq, acc):
    r = list(seq); random.Random(zlib.crc32(acc.encode())).shuffle(r); return "".join(r)
P = ('Below is a protein sequence in one-letter amino acid codes. Annotate it using only the sequence. '
     'Reply with a single JSON object and nothing else, with these keys: '
     '"pfam_domains": list of {"accession": "PFxxxxx", "name": Pfam short name, "start": int, "end": int} (1-based residue positions; empty list if none recognised); '
     '"transmembrane_helices": list of [start, end]; "signal_peptide": true or false; '
     '"protein_name": string; "ec_number": string or null; "function": one sentence. '
     'Do not guess identifiers you are not confident of: leave a field empty or null instead.\n\n>sequence\n')
qs = [(t, c) for t in T for c in ("real", "shuffled")]
done = set()
try:
    for l in open(out): d = json.loads(l); done.add((d["accession"], d["condition"]))
except FileNotFoundError: pass
def ask(tc):
    t, c = tc; seq = t["sequence"] if c == "real" else shuffled(t["sequence"], t["accession"])
    j = None
    for _ in range(3):
        p = subprocess.run(["claude", "-p", "--model", model, "--system-prompt", "", "--tools", "", "--effort", eff, "--output-format", "json"],
                           input=P + fasta(seq), capture_output=True, text=True, cwd="/tmp")
        try: j = json.loads(p.stdout); break
        except Exception: pass
    if j is None: return dict(accession=t["accession"], condition=c, error=True)
    text = j.get("result") or ""; m = re.search(r"\{.*\}", text, re.S); ans = None
    try: ans = json.loads(m.group(0)) if m else None
    except Exception: pass
    return dict(accession=t["accession"], condition=c, text=text, ans=ans, cost=j.get("total_cost_usd"),
                thinking=j.get("usage", {}).get("output_tokens_details", {}).get("thinking_tokens"), served=list(j.get("modelUsage", {})))
todo = [q for q in qs if (q[0]["accession"], q[1]) not in done]
with ThreadPoolExecutor(8) as ex, open(out, "a") as fh:
    for r in ex.map(ask, todo): fh.write(json.dumps(r) + "\n"); fh.flush()
print(model, "done", len(todo))
