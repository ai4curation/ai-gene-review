"""Map UniProt-annotated active-site and SAM-binding residues of E. coli RlmE (P0C0R7)
and human MRM2 (Q9UI43) onto Drosophila Mrm2 (Q9VDT6) by global pairwise alignment.

Run: uv run python compare_catalytic_sites.py > RESULTS-catalytic.txt
Residues and positions are read from UniProt at run time; nothing is hardcoded.
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q9VDT6"
REFERENCES = ["P0C0R7", "Q9UI43"]
FEATURE_TYPES = {"Active site", "Binding site"}


def fetch_entry(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def site_features(entry: dict) -> list[tuple[str, int, int, str]]:
    out = []
    for f in entry.get("features", []):
        if f["type"] in FEATURE_TYPES:
            start = f["location"]["start"]["value"]
            end = f["location"]["end"]["value"]
            evid = ",".join(
                f"{e.get('evidenceCode')}:{e.get('source', '')}:{e.get('id', '')}"
                for e in f.get("evidences", [])
            )
            out.append((f["type"], start, end, evid))
    return out


def position_map(alignment) -> dict[int, int]:
    """Map 1-based reference positions (seqB) to 1-based target positions (seqA)."""
    mapping = {}
    for (a_start, a_end), (b_start, b_end) in zip(*alignment.aligned):
        for offset in range(a_end - a_start):
            mapping[b_start + offset + 1] = a_start + offset + 1
    return mapping


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"

    target = fetch_entry(TARGET)
    tseq = target["sequence"]["value"]
    print(f"# Target {TARGET} length {len(tseq)}")
    for ref_acc in REFERENCES:
        ref = fetch_entry(ref_acc)
        rseq = ref["sequence"]["value"]
        aln = aligner.align(tseq, rseq)[0]
        mapping = position_map(aln)
        ident = sum(
            1 for rpos, tpos in mapping.items() if rseq[rpos - 1] == tseq[tpos - 1]
        )
        print(f"\n## Reference {ref_acc} length {len(rseq)}")
        print(f"aligned_pairs={len(mapping)} identical={ident} "
              f"identity_over_aligned={ident / len(mapping):.3f}")
        print("feature\tref_range\tref_residues\ttarget_range\ttarget_residues\tconserved\tevidence")
        for ftype, start, end, evid in site_features(ref):
            rres = rseq[start - 1:end]
            tpos = [mapping.get(p) for p in range(start, end + 1)]
            tres = "".join(tseq[p - 1] if p else "-" for p in tpos)
            trange = (
                f"{tpos[0]}..{tpos[-1]}" if all(tpos) else ",".join(str(p) for p in tpos)
            )
            print(f"{ftype}\t{start}..{end}\t{rres}\t{trange}\t{tres}\t{rres == tres}\t{evid}")


if __name__ == "__main__":
    main()
