# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare every donkey SLC16A11 UniProt entry with human MCT11 (Q8NCK7).

Usage: uv run --script compare_gene_models_rereview.py [OUT_DIR]

Fetches from the UniProt REST API all Equus asinus entries with gene name
SLC16A11, records their Ensembl transcript/gene cross-references, and makes a
global alignment (BLOSUM62, gap open -10, extend -0.5) of each to human Q8NCK7.
For each entry it reports length, the human span covered, identity over the
aligned pairs, the first human position from which a 20-residue window
is >=70% identical, and which human reference helices (UniProt-predicted
TM1-TM3 at human 12-32, 54-74, 82-102) have an aligned (and an identical) counterpart. It also reports the identical\nC-terminal suffix each entry shares with the longest donkey model.
Sequences are written to OUT_DIR (default: alignment_rereview/).
"""
import json
import sys
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

REST = "https://rest.uniprot.org/uniprotkb"
HUMAN = "Q8NCK7"
TM_HUMAN = {"TM1": (12, 32), "TM2": (54, 74), "TM3": (82, 102)}


def fetch_fasta(acc: str) -> str:
    r = requests.get(f"{REST}/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return r.text


def seq_of(fasta: str) -> str:
    return "".join(line.strip() for line in fasta.splitlines() if not line.startswith(">"))


def donkey_entries() -> list[dict]:
    r = requests.get(
        f"{REST}/search",
        params={
            "query": "gene:SLC16A11 AND taxonomy_id:9793",
            "fields": "accession,length,xref_ensembl",
            "format": "json",
        },
        timeout=60,
    )
    r.raise_for_status()
    out = []
    for e in r.json()["results"]:
        ens = [x for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "Ensembl"]
        props = {p["key"]: p["value"] for p in ens[0]["properties"]} if ens else {}
        out.append(
            {
                "accession": e["primaryAccession"],
                "length": e["sequence"]["length"],
                "ensembl_transcript": ens[0]["id"] if ens else None,
                "ensembl_gene": props.get("GeneId"),
            }
        )
    return out


def align(a: str, b: str):
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.end_insertion_score = 0
    al.end_deletion_score = 0
    return al.align(a, b)[0]


def main() -> None:
    out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "alignment_rereview")
    out_dir.mkdir(exist_ok=True)
    hfa = fetch_fasta(HUMAN)
    (out_dir / f"{HUMAN}.fasta").write_text(hfa)
    hs = seq_of(hfa)
    results = []
    for ent in sorted(donkey_entries(), key=lambda x: -x["length"]):
        fa = fetch_fasta(ent["accession"])
        (out_dir / f"{ent['accession']}.fasta").write_text(fa)
        ds = seq_of(fa)
        aln = align(ds, hs)
        pairs = ident = 0
        h2d = {}
        for (d0, d1), (h0, h1) in zip(*aln.aligned):
            for i, j in zip(range(d0, d1), range(h0, h1)):
                pairs += 1
                ident += ds[i] == hs[j]
                h2d[j + 1] = i + 1
        hcov = sorted(h2d)
        # first human position from which a 20-residue window of aligned
        # pairs is >=70% identical (start of confidently homologous sequence)
        hid = {j: ds[h2d[j] - 1] == hs[j - 1] for j in h2d}
        conf_start = None
        for j in hcov:
            win = [hid[k] for k in range(j, j + 20) if k in hid]
            if len(win) == 20 and sum(win) >= 14:
                conf_start = j
                break
        tm = {
            k: sum(1 for p in range(s, e + 1) if p in h2d) / (e - s + 1)
            for k, (s, e) in TM_HUMAN.items()
        }
        tm_ident = {
            k: sum(1 for p in range(s, e + 1) if hid.get(p)) / (e - s + 1)
            for k, (s, e) in TM_HUMAN.items()
        }
        ent.update(
            {
                "starts_with_met": ds.startswith("M"),
                "aligned_pairs": pairs,
                "identity_over_pairs": round(100 * ident / pairs, 1) if pairs else 0,
                "human_span": [hcov[0], hcov[-1]] if hcov else None,
                "human_residues_covered": len(hcov),
                "human_length": len(hs),
                "donkey_pos_of_human_M1": h2d.get(1),
                "first_confident_human_pos": conf_start,
                "donkey_pos_at_first_confident": h2d.get(conf_start),
                "tm1_3_fraction_aligned": {k: round(v, 2) for k, v in tm.items()},
                "tm1_3_fraction_identical": {k: round(v, 2) for k, v in tm_ident.items()},
            }
        )
        results.append(ent)
    # identical C-terminal suffix shared with the longest (most complete) model
    seqs = {e["accession"]: seq_of((out_dir / f"{e['accession']}.fasta").read_text()) for e in results}
    ref = results[0]["accession"]
    c = seqs[ref]
    for e in results:
        q = seqs[e["accession"]]
        k = 0
        while k < min(len(q), len(c)) and q[-1 - k] == c[-1 - k]:
            k += 1
        e["identical_c_terminal_suffix_with_longest"] = {
            "longest_model": ref,
            "length": k,
            "query_range": [len(q) - k + 1, len(q)] if k else None,
            "longest_range": [len(c) - k + 1, len(c)] if k else None,
        }
    print(json.dumps(results, indent=2))
    (out_dir / "results_rereview.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
