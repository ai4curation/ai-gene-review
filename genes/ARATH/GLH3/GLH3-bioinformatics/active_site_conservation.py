"""Check whether GLH3 (Q9FM66) retains the Ca2+-binding and catalytic residues
of experimentally characterized PL1 pectate lyases.

Reference proteins are the two Aspergillus nidulans pectate lyases that seed the
PAINT node behind GLH3's IBA (PTN001271105): plyB (Q00645) and plyA (Q5AVN4).
Their ACT_SITE and Ca2+ BINDING positions are read live from UniProt; each is
globally aligned to GLH3 and the aligned GLH3 residue is reported.

Usage: uv run python active_site_conservation.py
"""

import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q9FM66"
REFERENCES = ["Q00645", "Q5AVN4"]


def fetch_entry(accession):
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    with urllib.request.urlopen(url) as handle:
        return json.load(handle)


def site_features(entry):
    sites = []
    for feature in entry.get("features", []):
        if feature["type"] not in ("Active site", "Binding site"):
            continue
        position = feature["location"]["start"]["value"]
        ligand = feature.get("ligand", {}).get("name", "")
        sites.append((feature["type"], position, ligand))
    return sites


def residue_map(alignment):
    """Map 1-based reference positions to 1-based target positions."""
    mapping = {}
    target_blocks, ref_blocks = alignment.aligned
    for (t_start, t_end), (r_start, r_end) in zip(target_blocks, ref_blocks):
        for offset in range(r_end - r_start):
            mapping[r_start + offset + 1] = t_start + offset + 1
    return mapping


def percent_identity(alignment):
    target_blocks, ref_blocks = alignment.aligned
    target, ref = alignment.sequences
    identical = aligned = 0
    for (t_start, t_end), (r_start, _) in zip(target_blocks, ref_blocks):
        for offset in range(t_end - t_start):
            aligned += 1
            identical += target[t_start + offset] == ref[r_start + offset]
    return 100.0 * identical / aligned, aligned


def main():
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5

    target_seq = fetch_entry(TARGET)["sequence"]["value"]
    print(f"Target {TARGET} length {len(target_seq)}")
    for accession in REFERENCES:
        entry = fetch_entry(accession)
        ref_seq = entry["sequence"]["value"]
        alignment = aligner.align(target_seq, ref_seq)[0]
        identity, aligned = percent_identity(alignment)
        mapping = residue_map(alignment)
        print(f"\nReference {accession} length {len(ref_seq)}: "
              f"{identity:.1f}% identity over {aligned} aligned residues")
        print("feature\tligand\tref_pos\tref_aa\tGLH3_pos\tGLH3_aa\tmatch")
        for kind, position, ligand in site_features(entry):
            ref_aa = ref_seq[position - 1]
            target_pos = mapping.get(position)
            target_aa = target_seq[target_pos - 1] if target_pos else "-"
            print(f"{kind}\t{ligand}\t{position}\t{ref_aa}\t"
                  f"{target_pos or '-'}\t{target_aa}\t{ref_aa == target_aa}")


if __name__ == "__main__":
    main()
