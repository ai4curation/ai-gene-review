# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython", "requests"]
# ///
"""Identity check for horse A0A5F5PNJ9 (UniProt gene name SAT1).

Fetches live: UniProt sequences, the Ensembl gene/transcript the entry maps to,
Ensembl Compara orthology to human, and PANTHER (v19) subfamily assignments.
Prints raw results; nothing is hardcoded.
"""
import io
import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

TARGET = "A0A5F5PNJ9"
COMPARATORS = {
    "Q9BUR5": "human APOO/MIC26",
    "Q6UXV4": "human APOOL/MIC27",
    "Q9DCZ4": "mouse Apoo/Mic26",
    "P21673": "human SAT1 (spermidine/spermine N1-acetyltransferase)",
    "F7AGU3": "horse APOO (UniProt gene name APOO)",
}
ENS = "https://rest.ensembl.org"


def uniprot_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return str(next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq)


def identity(a: str, b: str) -> tuple[int, int]:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score, al.mode = -10, -0.5, "global"
    aln = al.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    paired = sum(1 for x, y in zip(s1, s2) if x != "-" and y != "-")
    return ident, paired


def ensembl(path: str) -> object:
    r = requests.get(f"{ENS}{path}", headers={"Content-Type": "application/json"}, timeout=60)
    r.raise_for_status()
    return r.json()


def panther_sf(acc: str, taxon: int) -> str:
    r = requests.get(
        "https://www.pantherdb.org/services/oai/pantherdb/geneinfo",
        params={"geneInputList": acc, "organism": taxon},
        timeout=60,
    )
    r.raise_for_status()
    g = r.json()["search"]["mapped_genes"]["gene"]
    return f"{g.get('family_id')} {g.get('sf_id')} {g.get('sf_name')}"


def main() -> None:
    q = uniprot_seq(TARGET)
    print(f"## Sequence identity of {TARGET} ({len(q)} aa) to comparators")
    for acc, label in COMPARATORS.items():
        s = uniprot_seq(acc)
        ident, paired = identity(q, s)
        print(f"{acc}\t{label}\tlen={len(s)}\tidentical={ident}\taligned_pairs={paired}\t"
              f"pct_of_target={100*ident/len(q):.1f}")

    print("\n## Ensembl mapping of the target")
    xr = ensembl("/xrefs/id/ENSECAP00000049988?all_levels=0")
    for x in xr:
        print("xref", x["dbname"], x["primary_id"])
    tr = ensembl("/lookup/id/ENSECAT00000077118")
    print("transcript", tr["id"], tr["display_name"], "canonical=", tr.get("is_canonical"))
    gene = ensembl(f"/lookup/id/{tr['Parent']}?expand=1")
    print("gene", gene["id"], gene["display_name"], gene["description"],
          f"chr{gene['seq_region_name']}")
    for t in gene["Transcript"]:
        tl = t.get("Translation") or {}
        print("  ", t["id"], t["display_name"], "canonical=", t.get("is_canonical"),
              tl.get("id"), tl.get("length"))
    hom = ensembl(f"/homology/id/equus_caballus/{gene['id']}?target_species=homo_sapiens;format=condensed")
    for h in hom["data"][0]["homologies"]:
        print("compara", h["type"], h["id"], h["species"], h["taxonomy_level"])

    print("\n## PANTHER v19 subfamily")
    print(TARGET, panther_sf(TARGET, 9796))
    print("Q9BUR5", panther_sf("Q9BUR5", 9606))
    print("Q6UXV4", panther_sf("Q6UXV4", 9606))


if __name__ == "__main__":
    main()
