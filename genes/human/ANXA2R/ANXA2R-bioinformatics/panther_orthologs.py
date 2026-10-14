"""List UniProt entries classified in PANTHER PTHR38820 (ANNEXIN-2 RECEPTOR) and test their taxonomy.

Tests the claim (PMID:23640736) that the ANXA2R gene is peculiar to human. Each entry's NCBI
taxonomic lineage (UniProt `lineage` field) is checked for "Mammalia"; every organism is printed
with its class so the mammal/non-mammal split can be read directly from the output:
    uv run python panther_orthologs.py
"""
import urllib.request

URL = ("https://rest.uniprot.org/uniprotkb/search?query=xref:panther-PTHR38820"
       "&fields=accession,organism_name,gene_names,lineage&format=tsv&size=500")


def taxon_class(lineage: str) -> str:
    """Return the rank-'class' name from a UniProt lineage string.

    >>> taxon_class("Chordata (phylum), Mammalia (class), Primates (order)")
    'Mammalia'
    """
    for part in lineage.split(", "):
        if part.endswith("(class)"):
            return part[: -len(" (class)")]
    return "no class rank"


def main() -> None:
    with urllib.request.urlopen(URL) as r:
        rows = [line.split("\t") for line in r.read().decode().strip().split("\n")[1:]]
    assert len(rows) < 500, "query capped at size=500; paginate if the family grows"
    organisms = {row[1]: taxon_class(row[3]) for row in rows}
    print(f"UniProt entries in PTHR38820: {len(rows)}")
    print(f"distinct organisms: {len(organisms)}")
    print(f"organisms whose lineage includes Mammalia: {sum('Mammalia (class)' in row[3] for row in {r[1]: r for r in rows}.values())}")
    print(f"organisms outside Mammalia: {sorted(o for o, c in organisms.items() if c != 'Mammalia')}")
    for org, cls in sorted(organisms.items()):
        print(f"  {cls}\t{org}")


if __name__ == "__main__":
    main()
