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

    uv run python projects/ANTIMICROBIAL_RESISTANCE/uniprot2aro2go.py \
        --sssom projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml \
        genes/ECO8N/mphB/mphB-uniprot.txt
"""
from __future__ import annotations

import csv
import glob
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import typer
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aro_release import DEFAULT_CACHE, MINI_OBO, AroOntology, Release, applicable_subjects  # noqa: E402,F401

# ARO ids look like ARO:0000000. Match one-or-more digits for consistency with the report script
# (annotation_gain_report.py) and robustness to any non-7-digit accessions.
ARO_RE = re.compile(r"ARO:\d+")


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
    """Index an SSSOM mapping set by subject (ARO) id -> list of mapping rows.

    Gap rows (object_id ``sssom:NoTermFound``) are excluded; they record an ARO family with no
    GO term and are not GO candidates.
    """
    doc = yaml.safe_load(sssom_path.read_text())
    index: dict[str, list[dict]] = {}
    for m in doc.get("mappings", []):
        if not str(m.get("object_id", "")).startswith("GO:"):
            continue
        index.setdefault(m["subject_id"], []).append(m)
    return index


def chain(hits: list[AroHit], aro2go: dict[str, list[dict]], onto: AroOntology | None = None) -> list[dict]:
    """Join ARO hits to GO terms via the ARO->GO index.

    With ``onto``, a mapping applies when its subject is the hit's ARO term (``exact``), an
    ``is_a`` ancestor of it (``narrower``), or a mechanism the hit reaches through
    ``participates_in`` (``participates_in``); see :func:`aro_release.applicable_subjects`.
    Without ``onto`` only exact matches fire.

    >>> aro = AroOntology.from_obo_text(MINI_OBO)
    >>> index = {"ARO:2": [{"subject_id": "ARO:2", "predicate_id": "RO:0002327", "object_id": "GO:0008800"}],
    ...          "ARO:10": [{"subject_id": "ARO:10", "predicate_id": "skos:relatedMatch", "object_id": "GO:0046677"}]}
    >>> hit = AroHit(uniprot_acc="P1", aro_id="ARO:4", aro_label="TEM-1", route="RGI")
    >>> sorted((r["go_id"], r["aro_relation"]) for r in chain([hit], index, aro))
    [('GO:0008800', 'narrower'), ('GO:0046677', 'participates_in')]
    >>> chain([hit], index)
    []
    """
    rows: list[dict] = []
    seen: set[tuple] = set()
    for hit in hits:
        applicable = applicable_subjects(onto, hit.aro_id) if onto else {hit.aro_id: "exact"}
        for subj, relation in sorted(applicable.items()):
            for m in aro2go.get(subj, []):
                key = (hit.uniprot_acc, m["object_id"], m["predicate_id"], subj, hit.route)
                if key in seen:
                    continue
                seen.add(key)
                rows.append(
                    {
                        "uniprot_acc": hit.uniprot_acc,
                        "gene_aro_id": hit.aro_id,
                        "gene_aro_label": hit.aro_label,
                        "mapped_aro_id": subj,
                        "mapped_aro_label": m.get("subject_label", ""),
                        "aro_relation": relation,
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


def main(
    uniprot: list[str] = typer.Argument(None, help="UniProt flat-file(s) (*-uniprot.txt) or globs"),
    sssom: Path = typer.Option(..., help="ARO->GO SSSOM mapping file"),
    rgi_output: Path | None = typer.Option(None, help="Optional RGI tab-delimited results to parse for ARO ids"),
    output: Path | None = typer.Option(None, "-o", "--output", help="Output TSV (default: stdout)"),
    propagate: bool = typer.Option(True, help="Propagate along ARO is_a and participates_in (see aro_release.py)"),
    aro_cache: Path = typer.Option(DEFAULT_CACHE, help="Fetched CARD release (just fetch-aro)"),
) -> None:
    """Chain UniProt -> ARO -> GO for AMR genes."""
    uniprot_paths: list[Path] = []
    for pat in uniprot or []:
        matched = [Path(p) for p in glob.glob(pat, recursive=True)]
        uniprot_paths.extend(matched if matched else [Path(pat)])

    aro2go = load_aro2go(sssom)
    hits = collect_hits(uniprot_paths, rgi_output)
    onto = None
    if propagate:
        release = Release(aro_cache)
        release.require()
        onto = AroOntology.from_obo(release.obo)
    rows = chain(hits, aro2go, onto)

    cols = [
        "uniprot_acc", "gene_aro_id", "gene_aro_label", "mapped_aro_id", "mapped_aro_label",
        "aro_relation", "predicate_id", "predicate_label", "go_id", "go_label",
        "mapping_justification", "route",
    ]
    out = output.open("w", newline="") if output else sys.stdout
    w = csv.DictWriter(out, fieldnames=cols, delimiter="\t")
    w.writeheader()
    w.writerows(rows)
    if output:
        out.close()

    n_aro = len({h.aro_id for h in hits})
    print(
        f"# {len(uniprot_paths)} UniProt file(s); {len(hits)} ARO hit(s) ({n_aro} distinct); "
        f"{len(rows)} GO candidate(s).",
        file=sys.stderr,
    )


if __name__ == "__main__":
    typer.run(main)
