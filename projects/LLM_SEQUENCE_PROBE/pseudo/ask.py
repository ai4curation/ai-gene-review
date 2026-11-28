"""Ask a model, from sequence alone, whether each protein is catalytically active. Usage: ask.py MODEL EFFORT

Calls the local `claude` CLI with no tools and an empty system prompt; the same prompt is used for wild-type
and mutant sequences. Appends to results/MODEL.jsonl and resumes if interrupted.
"""
import json, pathlib, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = pathlib.Path(__file__).parent; model, eff = sys.argv[1], sys.argv[2]; out = HERE / "results" / f"{model}.jsonl"
T = json.loads((HERE / "truth.json").read_text())
def fasta(s, w=60): return "\n".join(s[i:i+w] for i in range(0, len(s), w))
P = ('Below is a protein sequence in one-letter amino acid codes. Using only the sequence, decide whether the protein is '
     'likely to be catalytically active. Reply with a single JSON object and nothing else, with these keys: '
     '"protein_name": string; "enzyme_family": string; '
     '"catalytic_residues": list of {"role": string, "residue": one-letter code actually present in this sequence, "position": int (1-based)}; '
     '"substituted_or_missing": list of {"role": string, "expected": string, "found": string, "position": int or null} for any canonical catalytic or '
     'cofactor-binding residue that this sequence lacks (empty list if none); '
     '"catalytically_active": "yes", "no" or "uncertain"; "ec_number": string or null; "reason": one or two sentences.\n\n>sequence\n')
qs = [(t, v) for t in T for v in t["variants"]]
done = set()
if out.exists():
    for l in out.open(): d = json.loads(l); done.add((d["accession"], d["variant"]))
def ask(tv):
    t, v = tv; j = None
    for _ in range(3):
        p = subprocess.run(["claude", "-p", "--model", model, "--system-prompt", "", "--tools", "", "--effort", eff, "--output-format", "json"],
                           input=P + fasta(t["variants"][v]), capture_output=True, text=True, cwd="/tmp")
        try: j = json.loads(p.stdout); break
        except Exception: pass
    if j is None: return dict(accession=t["accession"], variant=v, error=True)
    text = j.get("result") or ""; m = re.search(r"\{.*\}", text, re.S); ans = None
    try: ans = json.loads(m.group(0)) if m else None
    except Exception: pass
    return dict(accession=t["accession"], group=t["group"], variant=v, effort=eff, text=text, ans=ans, cost=j.get("total_cost_usd"),
                thinking_tokens=j.get("usage", {}).get("output_tokens_details", {}).get("thinking_tokens"), served=list(j.get("modelUsage", {})))
todo = [q for q in qs if (q[0]["accession"], q[1]) not in done]
with ThreadPoolExecutor(8) as ex, out.open("a") as fh:
    for r in ex.map(ask, todo): fh.write(json.dumps(r) + "\n"); fh.flush()
print(model, "done", len(todo))
