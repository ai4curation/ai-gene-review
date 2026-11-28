"""Ask a model to predict structure, then function, from sequence alone. Usage: ask.py MODEL EFFORT"""
import json, pathlib, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = pathlib.Path(__file__).parent; model, eff = sys.argv[1], sys.argv[2]; out = HERE / "results" / f"{model}.jsonl"
T = json.loads((HERE / "truth.json").read_text())
def fasta(s, w=60): return "\n".join(s[i:i+w] for i in range(0, len(s), w))
P = ('Below is a protein sequence in one-letter amino acid codes (it may be a recombinant construct). Using only the sequence, predict its '
     'three-dimensional structure and then its function. Reply with a single JSON object and nothing else, with these keys: '
     '"helices": list of [start, end] residue ranges predicted to be helix (1-based positions in this sequence); '
     '"strands": list of [start, end] ranges predicted to be beta strand; '
     '"fold": short name of the predicted fold or structural superfamily; '
     '"contacts": list of exactly 20 [i, j] residue pairs with j - i >= 24 that you predict are in contact in the folded structure '
     '(C-alpha atoms within 8 angstroms), most confident first; '
     '"protein_name": string; "function": one sentence on the molecular function; '
     '"functional_residues": list of {"position": int, "residue": one-letter code, "role": string}; '
     '"recognised": true if you recognise this as a specific known protein, else false.\n\n>sequence\n')
done = set()
if out.exists():
    for l in out.open(): done.add(json.loads(l)["pdb"])
def ask(t):
    j = None
    for _ in range(3):
        p = subprocess.run(["claude", "-p", "--model", model, "--system-prompt", "", "--tools", "", "--effort", eff, "--output-format", "json"],
                           input=P + fasta(t["sequence"]), capture_output=True, text=True, cwd="/tmp")
        try: j = json.loads(p.stdout); break
        except Exception: pass
    if j is None: return dict(pdb=t["pdb"], error=True)
    text = j.get("result") or ""; m = re.search(r"\{.*\}", text, re.S); ans = None
    try: ans = json.loads(m.group(0)) if m else None
    except Exception: pass
    return dict(pdb=t["pdb"], effort=eff, text=text, ans=ans, cost=j.get("total_cost_usd"),
                thinking_tokens=j.get("usage", {}).get("output_tokens_details", {}).get("thinking_tokens"), served=list(j.get("modelUsage", {})))
todo = [t for t in T if t["pdb"] not in done]
with ThreadPoolExecutor(8) as ex, out.open("a") as fh:
    for r in ex.map(ask, todo): fh.write(json.dumps(r) + "\n"); fh.flush()
print(model, "done", len(todo))
