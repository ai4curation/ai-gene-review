# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Compare the benchmark donkey BICDL1 product with the other donkey BICDL1
gene-model products and with the human and mouse Swiss-Prot entries.

Fetches sequences live from UniProt REST and reports, for each entry, its length
and whether it carries three diagnostic segments:

* CC1 box (AARLG), the dynein light-intermediate-chain binding motif;
* SEG_CORE: a central coiled-coil segment present in canonical human Q6ZP65
  (human residues ~255-303, which the benchmark donkey product lacks);
* SEG_ALT: the extra exon of human isoform 2 (VAR_SEQ at human 436).

Also fetches the Ensembl gene record for the benchmark product and reports
which transcript Ensembl marks as canonical.

Run: uv run --script compare_isoforms_rereview.py > RESULTS-rereview.txt
"""

import json
import urllib.request

ENTRIES = [
    ("A0A9L0JLY3", "donkey, benchmark"),
    ("A0A9L0K8K5", "donkey"),
    ("A0A9L0JCR9", "donkey"),
    ("A0A8C4LG90", "donkey"),
    ("A0A9L0I4K1", "donkey"),
    ("Q6ZP65", "human Swiss-Prot canonical"),
    ("A0JNT9", "mouse Swiss-Prot canonical"),
]
MOTIFS = {
    "CC1": "AARLG",
    "SEG_CORE": "KMLSDRKRELEHRL",
    "SEG_ALT": "DDDSLEEQIRQTSEDSRALREL",
}
ENSEMBL_GENE = "ENSEASG00005007623"


def fetch(url: str) -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def seq(acc: str) -> str:
    fasta = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(fasta.splitlines()[1:])


def main() -> None:
    print("accession\tnote\tlength\t" + "\t".join(MOTIFS))
    for acc, note in ENTRIES:
        s = seq(acc)
        hits = []
        for m in MOTIFS.values():
            i = s.find(m)
            hits.append(str(i + 1) if i >= 0 else "absent")
        print(f"{acc}\t{note}\t{len(s)}\t" + "\t".join(hits))
    gene = json.loads(
        fetch(
            f"https://rest.ensembl.org/lookup/id/{ENSEMBL_GENE}"
            "?expand=1;content-type=application/json"
        )
    )
    print()
    print(f"Ensembl gene {ENSEMBL_GENE} canonical transcript: {gene.get('canonical_transcript')}")
    for t in gene.get("Transcript", []):
        tr = t.get("Translation") or {}
        print(f"{t['id']}\tcanonical={t.get('is_canonical')}\t{tr.get('id')}\tlength={tr.get('length')}")


if __name__ == "__main__":
    main()
