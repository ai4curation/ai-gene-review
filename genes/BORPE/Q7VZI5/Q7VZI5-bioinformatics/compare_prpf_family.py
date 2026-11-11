# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare Q7VZI5 (BP0922) with characterised PTHR43709 members and the
B. pertussis prp-operon PrpF paralog (BP2370, Q7VW94).

Fetches sequences and PANTHER/InterPro cross-references from UniProt REST,
computes global (Needleman-Wunsch, BLOSUM62) percent identity of Q7VZI5 to
each comparator, and an all-vs-all identity matrix. Results are printed and
written to results.json. Nothing is hardcoded except the accession list.
"""

import json
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCESSIONS = {
    "Q7VZI5": "B. pertussis BP0922 (target)",
    "Q7VW94": "B. pertussis BP2370 prp-operon PrpF paralog",
    "Q8EJW4": "Shewanella oneidensis PrpF (characterised 2-methylaconitate isomerase)",
    "Q937N7": "Cupriavidus necator PrpF",
    "Q0QLE6": "Eubacterium barkeri Mii (characterised 3-methylitaconate isomerase)",
    "A0A0U2X0E4": "Ustilago maydis Adi1 (characterised aconitate delta-isomerase)",
    "O07931": "Bacillus subtilis YraM",
    "P0AAV8": "E. coli YbhH (SF3)",
    "Q0KJL4": "Novosphingobium LigU (SF3)",
    "Q88JY0": "P. putida GalD (SF3)",
}


def fetch(acc: str) -> dict:
    r = requests.get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60
    )
    r.raise_for_status()
    d = r.json()
    xrefs = d.get("uniProtKBCrossReferences", [])
    return {
        "sequence": d["sequence"]["value"],
        "length": d["sequence"]["length"],
        "panther": sorted(x["id"] for x in xrefs if x["database"] == "PANTHER"),
        "interpro": sorted(x["id"] for x in xrefs if x["database"] == "InterPro"),
        "ncbifam": sorted(x["id"] for x in xrefs if x["database"] == "NCBIfam"),
    }


def identity(aligner: Align.PairwiseAligner, a: str, b: str) -> float:
    aln = aligner.align(a, b)[0]
    matches = 0
    aligned_cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned_cols += 1
            if a[i] == b[j]:
                matches += 1
    # identity over the shorter sequence length
    return 100.0 * matches / min(len(a), len(b))


# Shewanella PrpF (Q8EJW4) residues contacting trans-aconitate / catalytic
# (PMID:17567742: Lys73, Cys107, Lys281, His317)
PRPF_SITES = {73: "K", 107: "C", 281: "K", 317: "H"}


def map_sites(aligner: Align.PairwiseAligner, ref: str, tgt: str) -> dict:
    aln = aligner.align(ref, tgt)[0]
    mapping = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            mapping[i + 1] = j + 1
    out = {}
    for pos, aa in PRPF_SITES.items():
        assert ref[pos - 1] == aa, f"reference residue mismatch at {pos}"
        tpos = mapping.get(pos)
        out[f"{aa}{pos}"] = None if tpos is None else f"{tgt[tpos - 1]}{tpos}"
    return out


KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
      "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
      "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def max_hydropathy(seq: str, window: int = 19, start: int = 0, end: int | None = None) -> float:
    """Maximum Kyte-Doolittle mean over windows (19 aa ~ TM helix scale)."""
    sub = seq[start:end]
    return max(
        sum(KD[c] for c in sub[i:i + window]) / window
        for i in range(len(sub) - window + 1)
    )


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"

    data = {acc: fetch(acc) for acc in ACCESSIONS}
    accs = list(ACCESSIONS)
    matrix = {
        a: {b: round(identity(aligner, data[a]["sequence"], data[b]["sequence"]), 1)
            for b in accs}
        for a in accs
    }
    print("Accession\tLength\tPANTHER\tNCBIfam\t%id_to_Q7VZI5\tdescription")
    for acc in accs:
        d = data[acc]
        print(
            f"{acc}\t{d['length']}\t{','.join(d['panther'])}\t{','.join(d['ncbifam'])}"
            f"\t{matrix['Q7VZI5'][acc]}\t{ACCESSIONS[acc]}"
        )
    print("\nAll-vs-all % identity (over shorter sequence)")
    print("\t" + "\t".join(accs))
    for a in accs:
        print(a + "\t" + "\t".join(str(matrix[a][b]) for b in accs))
    print("\nShewanella PrpF (Q8EJW4) active-site residues mapped by pairwise alignment")
    sites = {}
    for acc in accs:
        sites[acc] = map_sites(aligner, data["Q8EJW4"]["sequence"], data[acc]["sequence"])
        print(acc + "\t" + "\t".join(f"{k}->{v}" for k, v in sites[acc].items()))
    target = data["Q7VZI5"]["sequence"]
    hyd = {
        "max_kd_19aa_whole": round(max_hydropathy(target), 2),
        "max_kd_19aa_first_40": round(max_hydropathy(target, end=40), 2),
    }
    print("\nQ7VZI5 Kyte-Doolittle (19-aa window; >1.6 suggests a TM segment):", hyd)
    out = {
        "q7vzi5_hydropathy": hyd,
        "prpf_site_mapping": sites,
        "accessions": {
            acc: {k: v for k, v in data[acc].items() if k != "sequence"} | {"description": ACCESSIONS[acc]}
            for acc in accs
        },
        "identity_matrix": matrix,
    }
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
