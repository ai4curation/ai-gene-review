# /// script
# requires-python = ">=3.11"
# dependencies = ["requests"]
# ///
"""Compare the ACAD9 alternative gene model A0A7P0T7Z1 (ENST00000680636) with canonical Q9H845.

Fetches both UniProt sequences and both Ensembl transcript structures (and CDS sequences),
locates the divergence point, maps it onto the exon structure, and reports which canonical
structural/functional regions (from PMID:33320993 and the UniProt Q9H845 record) are
retained or lost in the alternative model. Nothing is hard-coded except region coordinates
quoted from the literature / UniProt and the accessions themselves.

Run: uv run --script compare_gene_model.py > results.txt
"""
import json
import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.fasta"
ENSEMBL = "https://rest.ensembl.org"
ALT_ACC, CAN_ACC = "A0A7P0T7Z1", "Q9H845"
ALT_TX, CAN_TX = "ENST00000680636", "ENST00000308982"

# Canonical regions (Q9H845 numbering)
REGIONS = {
    "transit peptide (UniProt, PMID:16020546)": (1, 37),
    "Pfam PF02771 ACAD N-terminal (UniProt Q9H845 DR/feature coordinates on alt model 68-173)": (68, 173),
    "Pfam PF02770 ACAD middle": (177, 277),
    "Pfam PF00441 ACAD C-terminal": (290, 437),
    "catalytic proton acceptor Glu426 (UniProt, PMID:24158852)": (426, 426),
    "solvent-exposed linker 445-482 (PMID:33320993)": (445, 482),
    "ECSIT-contact loop 488-496 (PMID:33320993)": (488, 496),
    "vestigial dehydrogenase domain 493-587 (PMID:33320993)": (493, 587),
    "ECSIT-contact helix-turn-helix 554-560 (PMID:33320993)": (554, 560),
    "dimer-stabilising C-terminal helix 588-621 (PMID:33320993)": (588, 621),
}


def fasta(acc: str) -> str:
    r = requests.get(UNIPROT.format(acc), timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def ens(path: str) -> dict | str:
    sep = "&" if "?" in path else "?"
    r = requests.get(ENSEMBL + path + sep + "content-type=application/json", timeout=60)
    r.raise_for_status()
    return r.json()


def main() -> None:
    alt, can = fasta(ALT_ACC), fasta(CAN_ACC)
    print(f"{ALT_ACC} length {len(alt)}; {CAN_ACC} length {len(can)}")
    n = 0
    while n < min(len(alt), len(can)) and alt[n] == can[n]:
        n += 1
    print(f"identical prefix: residues 1-{n} ({n} aa); divergence starts at residue {n + 1}")
    print(f"canonical tail {n + 1}-{len(can)}: {can[n:]}")
    print(f"alternative tail {n + 1}-{len(alt)}: {alt[n:]}")
    tail = alt[n:]
    comp = {aa: tail.count(aa) for aa in "GPHAQRSL"}
    print(f"alternative tail composition (selected): {comp}; G+P+H fraction = "
          f"{(comp['G'] + comp['P'] + comp['H']) / len(tail):.2f}")
    # suffix identity check (does the alt tail re-join canonical anywhere?)
    shared_kmers = {can[i:i + 6] for i in range(n, len(can) - 5)} & {tail[i:i + 6] for i in range(len(tail) - 5)}
    print(f"shared 6-mers between the two tails: {len(shared_kmers)}")

    print("\nRegion retention (canonical numbering):")
    for name, (s, e) in REGIONS.items():
        if e <= n:
            status = "RETAINED (identical)"
        elif s > n:
            status = "LOST (replaced by unrelated sequence)"
        else:
            status = f"PARTIAL: {s}-{n} retained, {n + 1}-{e} lost"
        print(f"  {name}: {status}")

    print("\nEnsembl transcript structures:")
    exons = {}
    for tx in (CAN_TX, ALT_TX):
        d = ens(f"/lookup/id/{tx}?expand=1")
        exons[tx] = [(e["start"], e["end"]) for e in d["Exon"]]
        print(f"  {tx} {d['display_name']} canonical={d['is_canonical']} exons={len(exons[tx])} "
              f"translation_length={d['Translation']['length']}")
    for i, (a, b) in enumerate(zip(exons[CAN_TX], exons[ALT_TX]), 1):
        if a != b:
            print(f"  exon {i} differs: canonical {a} vs alternative {b}; "
                  f"start shift {a[0] - b[0]} nt, end shift {b[1] - a[1]} nt")
            delta = (a[0] - b[0]) + (b[1] - a[1])
            print(f"    net extra exonic nt (frame effect applies only if within the CDS) = {delta}; delta mod 3 = {delta % 3} "
                  f"({'frameshift' if delta % 3 else 'in-frame'})")
    # locate the stop codon exon of the alternative model
    d = ens(f"/lookup/id/{ALT_TX}?expand=1")
    tl = d["Translation"]
    stop = tl["end"]
    last = exons[ALT_TX][-1]
    print(f"  alternative translation genomic end {stop}; last exon {last}; "
          f"stop in last exon: {last[0] <= stop <= last[1]}")
    tl_can = ens(f"/lookup/id/{CAN_TX}?expand=1")["Translation"]
    print(f"  canonical translation genomic end {tl_can['end']}")


if __name__ == "__main__":
    main()
