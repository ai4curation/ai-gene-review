"""Per-residue conservation of AK1 among orthologues and across the adenylate kinase family.

Orthologues: every reviewed, non-fragment vertebrate UniProtKB entry whose gene
name is exactly AK1 (query run live; "AK1" entries of insects and Plasmodium are
not one-to-one orthologues and are excluded by the taxon filter). Family panel: reviewed NMP kinases chosen to span the family (human
AK2-AK5 and CMPK1, yeast ADK1, E. coli and B. subtilis Adk). Each sequence is
aligned to human AK1 pairwise (BLOSUM62, local) and the aligned residue at every
human position is recorded; no multiple-alignment program is needed for a
194-residue single-domain protein, and the pairwise identities are reported so the
reader can judge alignment quality.
"""
from __future__ import annotations

from collections import Counter

from Bio.Align import PairwiseAligner, substitution_matrices

from ak1_common import dump, fetch, uniprot_sequence

FAMILY = {  # accession: label; all reviewed entries, checked by the fetch below
    "P54819": "human AK2", "Q9UIJ7": "human AK3", "P27144": "human AK4", "Q9Y6K8": "human AK5",
    "P30085": "human CMPK1", "P07170": "yeast ADK1", "P69441": "E. coli Adk", "P16304": "B. subtilis Adk",
}


def fasta_records(text: str) -> dict[str, tuple[str, str]]:
    out = {}
    for block in text.split(">")[1:]:
        head, *lines = block.splitlines()
        acc = head.split("|")[1]
        out[acc] = (head, "".join(lines))
    return out


def main() -> None:
    human = uniprot_sequence()
    orth = fasta_records(fetch(
        "https://rest.uniprot.org/uniprotkb/search?query=gene_exact:AK1+AND+reviewed:true"
        "+AND+taxonomy_id:7742+AND+fragment:false&format=fasta&size=500", "ak1_vertebrate_orthologs.fasta").read_text())
    fam = fasta_records(fetch(
        "https://rest.uniprot.org/uniprotkb/accessions?accessions=" + ",".join(FAMILY) + "&format=fasta",
        "family_panel.fasta").read_text())
    aligner = PairwiseAligner(); aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10; aligner.extend_gap_score = -0.5

    def column_map(seq: str) -> tuple[dict[int, str], float]:
        aln = aligner.align(human, seq)[0]
        m = {}
        for (h0, h1), (s0, s1) in zip(*aln.aligned):
            for k in range(h1 - h0):
                m[h0 + k + 1] = seq[s0 + k]
        ident = sum(1 for i, a in m.items() if a == human[i - 1]) / len(human)
        return m, ident

    panels = {}
    for name, recs in (("orthologs", orth), ("family", fam)):
        entries = {}
        for acc, (head, seq) in recs.items():
            if acc == "P00568":
                continue
            m, ident = column_map(seq)
            org = head.split("OS=")[1].split(" OX=")[0] if "OS=" in head else ""
            entries[acc] = {"label": FAMILY.get(acc, head.split("|")[2].split()[0]), "organism": org,
                            "identity_to_human_AK1": round(ident, 3), "map": m}
        panels[name] = entries

    per_pos = {}
    for i, aa in enumerate(human, start=1):
        row = {"aa": aa}
        for name, entries in panels.items():
            col = [e["map"].get(i, "-") for e in entries.values()]
            row[f"{name}_identical"] = sum(c == aa for c in col)
            row[f"{name}_n"] = len(col)
            row[f"{name}_residues"] = dict(Counter(col).most_common())
        per_pos[i] = row
    out = {
        "panels": {n: {a: {k: v for k, v in e.items() if k != "map"} for a, e in es.items()}
                   for n, es in panels.items()},
        "positions": per_pos,
        "invariant_in_orthologs_and_family": [i for i, r in per_pos.items()
                                              if r["orthologs_identical"] == r["orthologs_n"]
                                              and r["family_identical"] == r["family_n"]],
    }
    dump(out, "conservation.json")
    print("orthologs:", len(panels["orthologs"]), "family:", len(panels["family"]))
    for n, es in panels.items():
        for a, e in es.items():
            print(f"  {n:9s} {a} {e['label']:22.22s} {e['organism'][:38]:38s} id={e['identity_to_human_AK1']}")
    print("invariant in both panels:", out["invariant_in_orthologs_and_family"])


if __name__ == "__main__":
    main()
