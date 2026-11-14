"""List KT2440 proteins carrying chorismate-binding or class-I glutamine amidotransferase signatures.

Queries the UniProt REST API (live) for Pseudomonas putida KT2440 (taxon 160488)
proteins with Pfam PF00425 (chorismate binding, TrpE/PabB synthase components),
Pfam PF00117 (class-I GATase) or NCBIfam TIGR00566 (TrpG/PabA amidotransferase),
and prints accession, gene names, Pfam and NCBIfam cross-references and length.

Usage: python amidotransferase_inventory.py > inventory.tsv
"""

import sys
import urllib.parse
import urllib.request

QUERY = (
    "organism_id:160488 AND (xref:pfam-PF00425 OR xref:pfam-PF00117 "
    "OR xref:ncbifam-TIGR00566)"
)
FIELDS = "accession,gene_names,protein_name,length,xref_pfam,xref_ncbifam,xref_panther"


def main() -> None:
    """Fetch the inventory and write it to stdout as TSV."""
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(
        {"query": QUERY, "fields": FIELDS, "format": "tsv", "size": 500}
    )
    with urllib.request.urlopen(url, timeout=60) as resp:
        sys.stdout.write(resp.read().decode("utf-8"))


if __name__ == "__main__":
    main()
