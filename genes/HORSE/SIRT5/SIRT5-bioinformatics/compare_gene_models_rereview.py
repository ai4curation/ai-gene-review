"""Re-review analysis: is F6S899 a defective gene model of horse SIRT5?

Fetches (live) the UniProt sequences of F6S899 and the alternative horse SIRT5
products A0A9L0T9B1 and A0A9L0T6A9 (Ensembl canonical), the Ensembl exon structures of their transcripts, aligns both
to human SIRT5 (Q9NXA8, from the cached repo flat file) and maps the human
catalytic / zinc / NAD-binding features onto each horse model.

Run: uv run python genes/HORSE/SIRT5/SIRT5-bioinformatics/compare_gene_models_rereview.py
Writes results-rereview.json and RESULTS-rereview.md next to this script.
"""
from pathlib import Path
import io
import json
import hashlib
import urllib.request
from Bio import SeqIO, Align

here = Path(__file__).resolve().parent
root = next(p for p in here.parents if (p / "pyproject.toml").exists())
# A0A9L0T6A9 / ENSECAT00000079525 is the Ensembl canonical transcript of ENSECAG00000026898.
MODELS = {"F6S899": "ENSECAT00000028843", "A0A9L0T9B1": "ENSECAT00000146678",
          "A0A9L0T6A9": "ENSECAT00000079525"}


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def quickgo(acc: str) -> list:
    url = f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId={acc}&limit=100"
    d = json.loads(get(url))
    rows = []
    for r in d["results"]:
        w = [x["connectedXrefs"][0]["db"] + ":" + x["connectedXrefs"][0]["id"] for x in (r["withFrom"] or [])]
        rows.append({"go": r["goId"], "evidence": r["goEvidence"], "reference": r["reference"], "with": w})
    return rows


def uniprot_seq(acc: str) -> str:
    rec = SeqIO.read(io.StringIO(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")), "fasta")
    return str(rec.seq)


def ensembl_transcript(tid: str) -> dict:
    d = json.loads(get(f"https://rest.ensembl.org/lookup/id/{tid}?expand=1;content-type=application/json"))
    exons = sorted((e["start"], e["end"]) for e in d["Exon"])
    return {"id": tid, "gene": d["Parent"], "strand": d["strand"], "exons": exons}


human = SeqIO.read(root / "genes/human/SIRT5/SIRT5-uniprot.txt", "swiss")
hseq = str(human.seq)
aligner = Align.PairwiseAligner(mode="global", match_score=2, mismatch_score=-1,
                                open_gap_score=-10, extend_gap_score=-0.5)
features = []
for f in human.features:
    if f.type in ("ACT_SITE", "BINDING"):
        pos = list(range(int(f.location.start), int(f.location.end)))
        features.append({"type": f.type, "pos": pos,
                         "ligand": str(f.qualifiers.get("ligand", ""))})

results = {"human": {"id": human.id, "length": len(hseq)}, "models": {}}
for acc, tid in MODELS.items():
    s = uniprot_seq(acc)
    al = aligner.align(hseq, s)[0]
    m = {}
    for (a0, a1), (b0, b1) in zip(*al.aligned):
        for i, j in zip(range(a0, a1), range(b0, b1)):
            m[i] = j
    # identity in human windows of 50 residues
    windows = []
    for w in range(0, len(hseq), 50):
        idx = [i for i in range(w, min(w + 50, len(hseq)))]
        paired = [i for i in idx if i in m]
        ident = sum(hseq[i] == s[m[i]] for i in paired)
        windows.append({"human_window_1based": f"{w + 1}-{idx[-1] + 1}", "paired": len(paired),
                        "identical": ident})
    fmap = []
    for f in features:
        fmap.append({"type": f["type"], "ligand": f["ligand"],
                     "human": "".join(hseq[i] for i in f["pos"]),
                     "human_pos_1based": f"{f['pos'][0] + 1}-{f['pos'][-1] + 1}",
                     "horse": "".join(s[m[i]] if i in m else "-" for i in f["pos"])})
    ident = sum(hseq[i] == s[j] for i, j in m.items())
    tr = ensembl_transcript(tid)
    results.setdefault("goa", {})[acc] = quickgo(acc)
    results["models"][acc] = {"length": len(s), "sha256": hashlib.sha256(s.encode()).hexdigest(),
                              "paired": len(m), "identical": ident,
                              "identity_percent": round(100 * ident / len(m), 1),
                              "windows": windows, "features": fmap, "transcript": tr}

ex_a = set(results["models"]["F6S899"]["transcript"]["exons"])
ex_b = set(results["models"]["A0A9L0T9B1"]["transcript"]["exons"])
only_b = sorted(ex_b - ex_a)
only_a = sorted(ex_a - ex_b)
results["exons_only_in_A0A9L0T9B1"] = [{"exon": e, "length": e[1] - e[0] + 1,
                                         "length_mod3": (e[1] - e[0] + 1) % 3} for e in only_b]
results["exons_only_in_F6S899"] = [{"exon": e, "length": e[1] - e[0] + 1,
                                     "length_mod3": (e[1] - e[0] + 1) % 3} for e in only_a]
ex_c = set(results["models"]["A0A9L0T6A9"]["transcript"]["exons"])
results["exons_only_in_A0A9L0T6A9_vs_F6S899"] = [{"exon": e, "length": e[1] - e[0] + 1,
                                                  "length_mod3": (e[1] - e[0] + 1) % 3} for e in sorted(ex_c - ex_a)]
(here / "results-rereview.json").write_text(json.dumps(results, indent=2) + "\n")

L = ["# SIRT5 (horse): F6S899 versus alternative horse SIRT5 models A0A9L0T9B1 and A0A9L0T6A9", "",
     "Generated by `compare_gene_models_rereview.py` (live UniProt and Ensembl REST; human Q9NXA8 from the "
     "cached flat file). Global alignment: Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, "
     "gap extend -0.5. Raw values in `results-rereview.json`.", "", "## Whole-length identity to human SIRT5 (Q9NXA8)", ""]
for acc, r in results["models"].items():
    L.append(f"- {acc}: {r['length']} residues; {r['identical']}/{r['paired']} paired residues identical "
             f"({r['identity_percent']}%); Ensembl transcript {r['transcript']['id']} of gene {r['transcript']['gene']}, "
             f"{len(r['transcript']['exons'])} exons.")
L += ["", "## Identity by 50-residue window of human SIRT5", "",
      "| human window | " + " | ".join(results["models"]) + " |", "|---|" + "---|" * len(results["models"])]
for k in range(len(results["models"]["F6S899"]["windows"])):
    row = [results["models"]["F6S899"]["windows"][k]["human_window_1based"]]
    for acc in results["models"]:
        w = results["models"][acc]["windows"][k]
        row.append(f"{w['identical']}/{w['paired']}")
    L.append("| " + " | ".join(row) + " |")
L += ["", "## Human catalytic, zinc and NAD-binding features mapped onto each horse model", "",
      "| feature | human pos | ligand | human | " + " | ".join(results["models"]) + " |", "|---|---|---|---|" + "---|" * len(results["models"])]
for k, f in enumerate(results["models"]["F6S899"]["features"]):
    row = [f["type"], f["human_pos_1based"], f["ligand"], f["human"]]
    row += [results["models"][acc]["features"][k]["horse"] for acc in results["models"]]
    L.append("| " + " | ".join(row) + " |")
L += ["", "## Exon-structure differences between the Ensembl transcripts (terminal exons include UTR, so only internal-exon mod 3 values bear on reading frame)", ""]
for e in results["exons_only_in_A0A9L0T9B1"]:
    L.append(f"- Exon only in the A0A9L0T9B1 transcript: {e['exon'][0]}-{e['exon'][1]}, {e['length']} nt (length mod 3 = {e['length_mod3']}).")
for e in results["exons_only_in_F6S899"]:
    L.append(f"- Exon only in the F6S899 transcript: {e['exon'][0]}-{e['exon'][1]}, {e['length']} nt (length mod 3 = {e['length_mod3']}).")
for e in results["exons_only_in_A0A9L0T6A9_vs_F6S899"]:
    L.append(f"- Exon in the canonical A0A9L0T6A9 transcript but not in F6S899: {e['exon'][0]}-{e['exon'][1]}, {e['length']} nt (length mod 3 = {e['length_mod3']}).")
for acc, r in results["models"].items():
    L.append(f"- {acc} transcript exons: " + ", ".join(f"{a}-{b}" for a, b in r["transcript"]["exons"]) + ".")
L += ["", "## Current GOA annotations (QuickGO) for each horse SIRT5 model", ""]
for acc, rows in results["goa"].items():
    L.append(f"- {acc}: " + ("; ".join(f"{r['go']} {r['evidence']} {r['reference']} [{', '.join(r['with'][:3])}]" for r in rows) or "none") + ".")
(here / "RESULTS-rereview.md").write_text("\n".join(L) + "\n")
print("\n".join(L))
