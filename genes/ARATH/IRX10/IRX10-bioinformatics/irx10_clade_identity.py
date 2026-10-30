"""Pairwise identity of GT47 (Pfam PF03016) proteins to the Arabidopsis IRX10 clade.

Purpose: find which protein in a species is the IRX10/XYS1 ortholog, for species
whose UniProt entries carry no gene name (poplar, Klebsormidium), and check
whether a chlorophyte (Chlamydomonas) has any IRX10-like protein at all.

Method:
  * Query proteins: Arabidopsis IRX10 (Q9FZJ1) and IRX10L (Q940Q8).
  * Targets: every UniProt protein with a Pfam PF03016 (Exostosin_GT47) match in
    each target taxon, listed by the InterPro API, plus fixed reference proteins.
  * Sequences and PANTHER subfamilies from the EBI Proteins API (used because
    rest.uniprot.org was failing when this was written; same UniProt data).
  * Global alignment (Biopython PairwiseAligner, BLOSUM62, open -10, extend -0.5).
    Identity = identical aligned positions / length of the shorter sequence.

Run from the repository root:
    uv run python genes/ARATH/IRX10/IRX10-bioinformatics/irx10_clade_identity.py
Writes identity.tsv and kfxys1_primer_check.txt next to this script. Nothing is hardcoded except accessions.
"""

import csv
import sys
import time
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

OUT = Path(__file__).parent / "identity.tsv"
QUERIES = {"AtIRX10": "Q9FZJ1", "AtIRX10L": "Q940Q8"}
REFERENCES = {
    "Q8S1X7": "rice IRX10 (LOC_Os01g70200)",
    "Q8S1X8": "rice Os01g0926600",
    "Q8S1X9": "rice Os01g0926400",
    "Q33AH8": "rice GUT1",
    "A0A2K2BTI7": "poplar POPTR_001G068100",
    "A0A2K2B808": "poplar POPTR_003G162000",
    "A9RGD8": "Physcomitrium GT47A",
    "Q9ZUV3": "Arabidopsis IRX7/FRA8 (GT47, other clade)",
    "Q16394": "human EXT1 (GT47 outgroup)",
}
TAXA = {"105231": "Klebsormidium nitens", "3055": "Chlamydomonas reinhardtii"}


def get(url, **kw):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=120, **kw)
            if r.status_code == 200:
                return r
        except requests.RequestException:
            pass
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"failed: {url}")


def pfam_members(taxid):
    url = (f"https://www.ebi.ac.uk/interpro/api/protein/uniprot/entry/pfam/PF03016/"
           f"taxonomy/uniprot/{taxid}/?page_size=200")
    out = []
    while url:
        d = get(url).json()
        out += [r["metadata"]["accession"] for r in d["results"]]
        url = d.get("next")
    return out


def protein(acc):
    r = get(f"https://www.ebi.ac.uk/proteins/api/proteins/{acc}",
            headers={"Accept": "application/json"}).json()
    panther = [x["id"] for x in r.get("dbReferences", []) if x["type"] == "PANTHER"]
    genes = [g.get("orfNames", g.get("olnNames", [{}]))[0].get("value", "")
             for g in r.get("gene", [])]
    return r["sequence"]["sequence"], ";".join(panther), ";".join(g for g in genes if g)


def identity(aligner, a, b):
    aln = aligner.align(a, b)[0]
    same = sum(1 for (s1, e1), (s2, e2) in zip(*aln.aligned)
               for i, j in zip(range(s1, e1), range(s2, e2)) if a[i] == b[j])
    return same / min(len(a), len(b))


# Gene-specific parts of the KfXYS1 cloning primers in Jensen et al. 2018
# (PMID:29460505, Methods): KfXYS1_27F after the TEV-site adapter, and
# KfXYS1_445F after the attB2 adapter (reverse strand).
KFXYS1_FWD = "AGATCCTCTTTGTTCGT"
KFXYS1_REV = "CTAATTTTCATCATCACCACG"
KLEB_CANDIDATE = "A0A1Y1IIS5"


def primer_check():
    from Bio.Seq import Seq
    seq = protein(KLEB_CANDIDATE)[0]
    fwd = str(Seq(KFXYS1_FWD[:15]).translate())
    rev = str(Seq(KFXYS1_REV).reverse_complement().translate()).rstrip("*")
    lines = [
        f"candidate {KLEB_CANDIDATE} length {len(seq)}",
        f"forward primer peptide {fwd}: position {seq.find(fwd) + 1 if fwd in seq else 'not found'}",
        f"reverse primer peptide {rev}: protein C-terminus {seq[-len(rev):]} "
        f"({'match' if seq.endswith(rev) else 'no match'})",
    ]
    (OUT.parent / "kfxys1_primer_check.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aligner.mode = "global"

    qseq = {k: protein(v)[0] for k, v in QUERIES.items()}
    targets = [(acc, "reference", desc) for acc, desc in REFERENCES.items()]
    targets += [(acc, TAXA[tx], "") for tx in TAXA for acc in pfam_members(tx)]

    rows = []
    for acc, group, desc in targets:
        seq, panther, gene = protein(acc)
        row = {"accession": acc, "group": group, "description": desc or gene,
               "length": len(seq), "panther": panther}
        for q, s in qseq.items():
            row[f"identity_vs_{q}"] = round(identity(aligner, s, seq), 3)
        rows.append(row)
        print(acc, group, row["identity_vs_AtIRX10L"], file=sys.stderr)

    rows.sort(key=lambda r: (r["group"], -r["identity_vs_AtIRX10L"]))
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {OUT} ({len(rows)} proteins)")
    primer_check()


if __name__ == "__main__":
    main()
