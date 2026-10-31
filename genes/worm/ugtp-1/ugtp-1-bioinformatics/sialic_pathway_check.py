"""Count UniProtKB entries carrying sialic-acid pathway EC numbers per organism.

Tests whether C. elegans encodes the enzymes needed to make CMP-sialic acid
(the substrate of SLC35A1-type transporters) or to use it (sialyltransferases).
Human and Drosophila are positive controls. Results are printed, not hardcoded.
"""
import urllib.parse
import urllib.request

ECS = {
    "2.5.1.57": "N-acetylneuraminate-9-phosphate synthase (NANS)",
    "2.5.1.56": "N-acetylneuraminate synthase (bacterial NeuB)",
    "2.7.7.43": "N-acylneuraminate cytidylyltransferase (CMAS)",
    "2.4.3.1": "beta-galactoside alpha-2,6-sialyltransferase",
    "2.4.3.4": "beta-galactoside alpha-2,3-sialyltransferase",
}
TAXA = {"6239": "Caenorhabditis elegans", "9606": "Homo sapiens", "7227": "Drosophila melanogaster"}


def count(ec: str, taxon: str) -> tuple[int, list[str]]:
    q = f"(ec:{ec}) AND (organism_id:{taxon})"
    url = ("https://rest.uniprot.org/uniprotkb/search?"
           + urllib.parse.urlencode({"query": q, "fields": "accession,gene_names", "format": "tsv", "size": 500}))
    with urllib.request.urlopen(url, timeout=120) as r:
        lines = r.read().decode().strip().splitlines()[1:]
    return len(lines), lines[:3]


if __name__ == "__main__":
    print("EC\tenzyme\ttaxon\tn_entries\texamples")
    for ec, name in ECS.items():
        for tx, tname in TAXA.items():
            n, ex = count(ec, tx)
            print(f"{ec}\t{name}\t{tname}\t{n}\t{'; '.join(e.replace(chr(9), ' ') for e in ex)}")
