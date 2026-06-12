#!/usr/bin/env python3
"""uniprot2aro2go: chain UniProt -> ARO -> GO for AMR genes.

This applies the curated ARO->GO SSSOM mapping (``aro2go.sssom.yaml``) to UniProt
records, producing candidate GO annotations for antimicrobial-resistance genes.

Two routes from UniProt to ARO are supported:

1. ``DR CARD`` cross-reference lines in the cached ``*-uniprot.txt`` records. These are
   deterministic and need no external tools, but are sparse: UniProt only populates a
   CARD cross-reference for a minority of entries (in this repo, currently only MphB).
   The line carries BOTH the determinant ARO id and the resistance-mechanism ARO id, e.g.::

       DR   CARD; ARO:3000318; mphB; ARO:0001004; antibiotic inactivation.

2. Sequence-based assignment with CARD's Resistance Gene Identifier (RGI). RGI is the
   scalable route for entries lacking a DR CARD line (e.g. MphA / Q47396). We do NOT call
   RGI here (it requires installing RGI + the local CARD database); instead, if you run
   RGI yourself, point ``--rgi-output`` at its tab-delimited results and we parse the
   ``Best_Hit_ARO`` / ``ARO`` column. See the README for the exact RGI command.

The ARO->GO step loads the SSSOM mapping set and indexes it by subject (ARO) id. Only ARO
ids present in the mapping produce output, so the result is bounded by curation coverage.

Example::

    uv run python projects/mappings/uniprot2aro2go.py \
        --sssom projects/mappings/aro2go.sssom.yaml \
        genes/ECO8N/A0A0H3EUF3_ECO8N/A0A0H3EUF3_ECO8N-uniprot.txt
"""
from __future__ import annotations

import argparse
import csv
import glob
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

# ARO ids look like ARO:0000000 (7 digits).
ARO_RE = re.compile(r"ARO:\d{7}")


@dataclass
class AroHit:
    """An ARO id assigned to a UniProt accession, with provenance."""

    uniprot_acc: str
    aro_id: str
    aro_label: str
    route: str  # "DR_CARD" or "RGI"


def parse_uniprot_card(uniprot_text: str) -> tuple[str, list[AroHit]]:
    """Parse the primary accession and any ``DR CARD`` hits from a UniProt flat-file.

    The CARD DR line encodes the determinant ARO id, the gene symbol, the resistance
    mechanism ARO id, and the mechanism label, e.g.::

        DR   CARD; ARO:3000318; mphB; ARO:0001004; antibiotic inactivation.

    Both ARO ids (determinant and mechanism) are returned as separate hits so that
    downstream ARO->GO mapping can fire on either.

    >>> acc, hits = parse_uniprot_card(
    ...     "AC   A0A0H3EUF3;\\n"
    ...     "DR   CARD; ARO:3000318; mphB; ARO:0001004; antibiotic inactivation.\\n"
    ... )
    >>> acc
    'A0A0H3EUF3'
    >>> sorted(h.aro_id for h in hits)
    ['ARO:0001004', 'ARO:3000318']
    """
    acc = ""
    hits: list[AroHit] = []
    for line in uniprot_text.splitlines():
        if line.startswith("AC ") and not acc:
            acc = line[5:].split(";")[0].strip()
        if line.startswith("DR   CARD;"):
            payload = line[len("DR   CARD;"):].rstrip(". ").strip()
            fields = [f.strip() for f in payload.split(";")]
            # fields = [determinant_aro, gene_symbol, mechanism_aro, mechanism_label]
            gene_symbol = fields[1] if len(fields) > 1 else ""
            mech_label = fields[3] if len(fields) > 3 else ""
            for field, label in ((fields[0], gene_symbol), (fields[2] if len(fields) > 2 else "", mech_label)):
                if ARO_RE.fullmatch(field):
                    hits.append(AroHit(uniprot_acc=acc, aro_id=field, aro_label=label, route="DR_CARD"))
    return acc, hits


def parse_rgi_output(path: Path) -> list[AroHit]:
    """Parse ARO ids from an RGI tab-delimited results file (``rgi main`` output).

    RGI output has a header row; the relevant columns are typically ``ORF_ID`` (or the
    contig/sequence name) and ``Best_Hit_ARO`` / ``ARO`` (the ARO *accession number*,
    without the ``ARO:`` prefix). We accept either ``ARO`` or ``Best_Hit_ARO`` and
    normalise to the ``ARO:NNNNNNN`` CURIE. The sequence/ORF name is stored as the
    ``uniprot_acc`` so the caller can join it back to a UniProt accession.

    This function only *parses* RGI output; it does not run RGI.
    """
    hits: list[AroHit] = []
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        cols = reader.fieldnames or []
        aro_col = next((c for c in ("ARO", "Best_Hit_ARO_accession", "ARO_accession") if c in cols), None)
        name_col = next((c for c in ("ORF_ID", "Contig", "Best_Hit_ARO") if c in cols), None)
        if aro_col is None:
            raise ValueError(f"No ARO accession column found in {path} (columns: {cols})")
        for row in reader:
            raw = (row.get(aro_col) or "").strip()
            if not raw:
                continue
            aro_id = raw if raw.startswith("ARO:") else f"ARO:{raw}"
            if not ARO_RE.fullmatch(aro_id):
                continue
            hits.append(
                AroHit(
                    uniprot_acc=(row.get(name_col) or "").strip() if name_col else "",
                    aro_id=aro_id,
                    aro_label=(row.get("Best_Hit_ARO") or "").strip(),
                    route="RGI",
                )
            )
    return hits


def load_aro2go(sssom_path: Path) -> dict[str, list[dict]]:
    """Index an SSSOM mapping set by subject (ARO) id -> list of mapping rows."""
    doc = yaml.safe_load(sssom_path.read_text())
    index: dict[str, list[dict]] = {}
    for m in doc.get("mappings", []):
        index.setdefault(m["subject_id"], []).append(m)
    return index


def chain(hits: list[AroHit], aro2go: dict[str, list[dict]]) -> list[dict]:
    """Join ARO hits to GO terms via the ARO->GO index. Returns annotation rows."""
    rows: list[dict] = []
    for hit in hits:
        for m in aro2go.get(hit.aro_id, []):
            rows.append(
                {
                    "uniprot_acc": hit.uniprot_acc,
                    "aro_id": hit.aro_id,
                    "aro_label": hit.aro_label or m.get("subject_label", ""),
                    "predicate_id": m["predicate_id"],
                    "predicate_label": m.get("predicate_label", ""),
                    "go_id": m["object_id"],
                    "go_label": m.get("object_label", ""),
                    "mapping_justification": m.get("mapping_justification", ""),
                    "route": hit.route,
                }
            )
    return rows


def collect_hits(uniprot_paths: list[Path], rgi_output: Path | None) -> list[AroHit]:
    hits: list[AroHit] = []
    for p in uniprot_paths:
        _, file_hits = parse_uniprot_card(p.read_text())
        hits.extend(file_hits)
    if rgi_output is not None:
        hits.extend(parse_rgi_output(rgi_output))
    return hits


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("uniprot", nargs="*", help="UniProt flat-file(s) (*-uniprot.txt) or globs")
    ap.add_argument("--sssom", required=True, type=Path, help="ARO->GO SSSOM mapping file")
    ap.add_argument("--rgi-output", type=Path, default=None, help="Optional RGI tab-delimited results to parse for ARO ids")
    ap.add_argument("-o", "--output", type=Path, default=None, help="Output TSV (default: stdout)")
    args = ap.parse_args(argv)

    uniprot_paths: list[Path] = []
    for pat in args.uniprot:
        matched = [Path(p) for p in glob.glob(pat, recursive=True)]
        uniprot_paths.extend(matched if matched else [Path(pat)])

    aro2go = load_aro2go(args.sssom)
    hits = collect_hits(uniprot_paths, args.rgi_output)
    rows = chain(hits, aro2go)

    cols = [
        "uniprot_acc", "aro_id", "aro_label", "predicate_id", "predicate_label",
        "go_id", "go_label", "mapping_justification", "route",
    ]
    out = args.output.open("w", newline="") if args.output else sys.stdout
    try:
        w = csv.DictWriter(out, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    finally:
        if args.output:
            out.close()

    n_aro = len({h.aro_id for h in hits})
    print(
        f"# {len(uniprot_paths)} UniProt file(s); {len(hits)} ARO hit(s) ({n_aro} distinct); "
        f"{len(rows)} GO candidate(s).",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
