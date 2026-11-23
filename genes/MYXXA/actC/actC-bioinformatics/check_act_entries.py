"""Check the duplicate UniProtKB representation of the Myxococcus xanthus act operon.

Two questions, both answered from live public APIs:

1. Are the taxon-34 (*Myxococcus xanthus*) act entries, submitted with
   GenBank AF350253 by the authors of PMID:11359579, the same proteins as the
   taxon-246197 (*M. xanthus* strain DK1622) reference-proteome entries? This
   decides whether the two NCBI taxon ids on the CACAO annotations of
   PMID:11359579 denote two organisms (a cross-isolate transfer) or one.
2. How widely is GO:0004029 propagated from the PANTHER ancestral node
   PTN005180820 that supplies Q93P57's TreeGrafter aldehyde-dehydrogenase row?

Nothing is hardcoded: every number printed comes from a response in this run.
Run with:  uv run --no-project python check_act_entries.py
(or plain `python3 check_act_entries.py`; only the standard library is used,
and `curl` must be on PATH so the container's HTTPS proxy settings apply).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass

UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"

ACT_GENES = ("actA", "actB", "actC", "actD", "actE")
SPECIES_TAXON = "34"
DK1622_TAXON = "246197"
GRAFT_NODE = "PANTHER:PTN005180820"


def fetch(url: str) -> str:
    """GET a URL with curl, so the environment's proxy configuration is honoured."""
    result = subprocess.run(
        ["curl", "-sS", "--fail", "-m", "90", url],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


ACT_LOCI = {"actA": "MXAN_3213", "actB": "MXAN_3214", "actC": "MXAN_3215",
            "actD": "MXAN_3216", "actE": "MXAN_3217"}


@dataclass(frozen=True)
class Entry:
    """One UniProtKB entry, reduced to the fields this check compares."""

    accession: str
    taxon: str
    gene_names: tuple[str, ...]
    length: int
    sequence_md5: str
    sequence: str
    refseq: tuple[str, ...]
    proteomes: tuple[str, ...]
    go_lines: tuple[str, ...]


def parse_flatfile(text: str) -> Entry:
    """Parse the handful of flat-file lines needed to compare two entries."""
    accession = taxon = ""
    gene_names: list[str] = []
    refseq: list[str] = []
    proteomes: list[str] = []
    go_lines: list[str] = []
    sequence: list[str] = []
    in_sequence = False
    for line in text.splitlines():
        if line.startswith("SQ   "):
            in_sequence = True
            continue
        if line.startswith("//"):
            in_sequence = False
            continue
        if in_sequence:
            sequence.append(line.replace(" ", ""))
            continue
        if line.startswith("AC   ") and not accession:
            accession = line[5:].split(";")[0].strip()
        elif line.startswith("OX   NCBI_TaxID="):
            taxon = line[len("OX   NCBI_TaxID="):].split()[0].rstrip(";")
        elif line.startswith("GN   "):
            for field in line[5:].split(";"):
                field = field.strip()
                if field.startswith("Name=") or field.startswith("OrderedLocusNames="):
                    value = field.split("=", 1)[1].split("{")[0].strip()
                    gene_names.append(value)
        elif line.startswith("DR   RefSeq; "):
            refseq.append(line[len("DR   RefSeq; "):].split(";")[0].strip())
        elif line.startswith("DR   Proteomes; "):
            proteomes.append(line[len("DR   Proteomes; "):].split(";")[0].strip())
        elif line.startswith("DR   GO; "):
            go_lines.append(line[len("DR   GO; "):].strip())
    joined = "".join(sequence)
    return Entry(
        accession=accession,
        taxon=taxon,
        gene_names=tuple(gene_names),
        length=len(joined),
        sequence_md5=hashlib.md5(joined.encode()).hexdigest(),
        sequence=joined,
        refseq=tuple(refseq),
        proteomes=tuple(proteomes),
        go_lines=tuple(go_lines),
    )


def search_accessions(query: str) -> list[str]:
    """Return the accessions matching a UniProtKB query, in the order served."""
    url = f"{UNIPROT}/search?query={query}&fields=accession&format=list&size=50"
    return [line.strip() for line in fetch(url).splitlines() if line.strip()]


def act_entries(taxon: str) -> dict[str, Entry]:
    """Fetch every act-operon entry in one taxon, keyed by the act gene symbol."""
    gene_clause = "+OR+".join(f"gene:{gene}" for gene in ACT_GENES)
    accessions = search_accessions(f"({gene_clause})+AND+taxonomy_id:{taxon}")
    found: dict[str, Entry] = {}
    for accession in accessions:
        entry = parse_flatfile(fetch(f"{UNIPROT}/{accession}.txt"))
        if entry.taxon != taxon:
            continue
        for gene in ACT_GENES:
            if any(name.lower() == gene.lower() for name in entry.gene_names):
                found[gene] = entry
    return found


def locus_entry(locus: str) -> Entry | None:
    """Fetch a DK1622 entry by its MXAN ordered locus name."""
    for accession in search_accessions(locus):
        entry = parse_flatfile(fetch(f"{UNIPROT}/{accession}.txt"))
        if locus in entry.gene_names:
            return entry
    return None


def node_annotation_tally(node: str) -> tuple[int, dict[str, int]]:
    """Count the GO annotations QuickGO serves for one PANTHER ancestral node."""
    payload = json.loads(fetch(f"{QUICKGO}/annotation/search?withFrom={node}&limit=200"))
    tally: dict[str, int] = {}
    for row in payload["results"]:
        tally[row["goId"]] = tally.get(row["goId"], 0) + 1
    return payload["numberOfHits"], tally


def main() -> int:
    print("# act operon: UniProtKB entry duplication across two taxon ids\n")
    species = act_entries(SPECIES_TAXON)
    dk1622 = act_entries(DK1622_TAXON)
    # actC, actD and actE have no GN Name on the DK1622 side, so reach them by
    # their ordered locus names instead.
    for gene, locus in ACT_LOCI.items():
        if gene not in dk1622:
            by_locus = locus_entry(locus)
            if by_locus is not None:
                dk1622[gene] = by_locus

    header = f"{'gene':5} {'taxon34':9} {'DK1622':9} {'len34':>6} {'lenDK':>6} {'same seq':9} {'aa diffs':>9} {'same RefSeq':12}"
    print(header)
    print("-" * len(header))
    for gene in ACT_GENES:
        a = species.get(gene)
        b = dk1622.get(gene)
        if a is None or b is None:
            print(f"{gene:5} {a.accession if a else '-':9} {b.accession if b else '-':9} "
                  f"{'-':>6} {'-':>6} {'n/a':9} {'n/a':>9} {'n/a':12}")
            continue
        same_seq = "YES" if a.sequence_md5 == b.sequence_md5 else "no"
        same_ref = "YES" if set(a.refseq) & set(b.refseq) else "no"
        if a.length == b.length:
            diffs = str(sum(1 for x, y in zip(a.sequence, b.sequence) if x != y))
        else:
            diffs = "len"
        print(f"{gene:5} {a.accession:9} {b.accession:9} {a.length:>6} {b.length:>6} "
              f"{same_seq:9} {diffs:>9} {same_ref:12}")

    print("\n## actC pair in detail\n")
    for label, entry in (("taxon 34", species.get("actC")), ("DK1622", dk1622.get("actC"))):
        if entry is None:
            print(f"{label}: not found")
            continue
        print(f"{label}: {entry.accession}")
        print(f"  gene names : {', '.join(entry.gene_names) or '(none)'}")
        print(f"  length     : {entry.length}")
        print(f"  sequence   : md5 {entry.sequence_md5}")
        print(f"  RefSeq     : {', '.join(entry.refseq) or '(none)'}")
        print(f"  proteomes  : {', '.join(entry.proteomes) or '(none)'}")
        print(f"  GO lines   : {len(entry.go_lines)}")
        for go_line in entry.go_lines:
            print(f"    - {go_line}")

    print(f"\n## GO propagation from {GRAFT_NODE}\n")
    total, tally = node_annotation_tally(GRAFT_NODE)
    print(f"QuickGO numberOfHits for withFrom={GRAFT_NODE}: {total}")
    print("terms seen in the first page of results:")
    for term, count in sorted(tally.items()):
        print(f"  {term}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
