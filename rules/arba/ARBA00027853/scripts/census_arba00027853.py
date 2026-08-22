#!/usr/bin/env python3
"""Reproducible census of the annotations ARBA00027853 actually emits.

ARBA00027853 assigns a single GO term, GO:0006720 "isoprenoid metabolic process",
via 94 OR-ed condition sets. The rule's own `statistics` block in the UniProt API
reports ``reviewedProteinCount: 0`` and ``unreviewedProteinCount: 0``, which is
what the commissioned deep research was told. That is wrong: QuickGO reports
thousands of live GO:0006720 / ECO:0000256 / GO_REF:0000117 annotations whose
WITH/FROM is ARBA:ARBA00027853.

This script re-derives, from primary sources only:

1. how many such annotations exist right now;
2. what the annotated proteins actually are (protein-name census);
3. which InterPro signatures they carry, and whether the taxon constraints
   written into the published condition sets are visible in the emitted set.

Nothing is hard-coded. Run it and the numbers in ``ARBA00027853-analysis.md``
should reproduce, modulo UniProt/QuickGO release drift.

Usage::

    uv run python rules/arba/ARBA00027853/scripts/census_arba00027853.py \
        --outdir /tmp/arba27853

Numbers quoted in the review were produced on 2026-08-22.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

RULE_ID = "ARBA00027853"
GO_ID = "GO:0006720"
GO_REF = "GO_REF:0000117"

QUICKGO_DOWNLOAD = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
    "?goId={go}&reference={ref}&withFrom={rule}&downloadLimit=200000"
    "&selectedFields=geneProductId,symbol,taxonId,taxonName,withFrom"
)
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"

# Protein-name buckets, applied in order (first match wins). These are coarse and
# deliberately transparent: the point is to separate "this is plainly an
# isoprenoid-pathway enzyme" from "this plainly is not", not to be a classifier.
BUCKETS: list[tuple[str, str]] = [
    (
        "carotenoid/retinoid cleavage + isomerase (BCO1/BCO2/RPE65/NinaB)",
        r"carotene|carotenoid|carotinoid|BCDO|BCMO|BCO1|BCO2|retino|retinal|RPE65"
        r"|isomerooxygenase|isomerohydrolase|apocarotenoid|NINAB",
    ),
    (
        "carotenoid backbone (phytoene/lycopene/desaturase/cyclase)",
        r"phytoene|lycopene|zeta-carotene|neoxanthin|violaxanthin|capsanthin|zeaxanthin",
    ),
    (
        "prenyl/polyprenyl diphosphate synthase (PDSS/FPPS/GGPPS)",
        r"prenyl|farnesyl|geranylgeranyl|decaprenyl|solanesyl|polyprenyl|octaprenyl"
        r"|nonaprenyl|heptaprenyl|dimethylallyl|DLP1|DPS1",
    ),
    (
        "terpene synthase/cyclase",
        r"terpene|terpenoid|cyclase|copalyl|kaurene|linalool|carene|humulene"
        r"|caryophyllene|germacrene|santalene|bisabolene|cadinene|selinene|pinene"
        r"|myrcene|ocimene|limonene|abienol|isoprene synthase|geranyllinalool"
        r"|amyrin|lupeol|cycloartenol",
    ),
    ("iridoid synthase / PRISE (monoterpenoid side)", r"iridoid|oxocitronellyl"),
    (
        "PRISE steroid side (progesterone / 3-oxo-steroid 5-beta-reductase)",
        r"progesterone 5|5-beta-reductase|5-beta-steroid|oxosteroid|Delta\(4\)-3-oxo|Delta-4",
    ),
    (
        "MVA/MEP precursor enzymes",
        r"HMG-CoA|hydroxymethylglutaryl|mevalonate|xylulose|methylbut-2-enyl|isopentenyl",
    ),
    ("gibberellin/ABA", r"gibberellin|abscisic|kaurenoic"),
    ("cytochrome P450", r"[Cc]ytochrome [Pp]-?450|^CYP"),
    ("glycosyltransferase", r"glycosyltransferase|glucosyltransferase|glucuronosyl"),
    ("squalene/sterol/triterpene", r"squalene|sterol|lanosterol"),
    ("juvenile hormone", r"juvenile hormone"),
    (
        "generic SDR/dehydrogenase/oxidoreductase (non-diagnostic fold)",
        r"SDR |short-chain dehydrogenase|Short-subunit dehydrogenase"
        r"|NAD-dependent epimerase|oxidoreductase|dehydrogenase|reductase|FabG",
    ),
    (
        "uncharacterized / hypothetical / bare domain-containing",
        r"^Uncharacterized|hypothetical|domain-containing protein"
        r"|^Putative uncharacterized|^Dioxygenase$|^Protein ",
    ),
]


def fetch(
    url: str, accept: str = "text/tsv", tries: int = 3, timeout: int = 180
) -> str:
    """GET with a couple of retries; both EBI and UniProt occasionally 503."""
    last: Exception | None = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept})
            return urllib.request.urlopen(req, timeout=timeout).read().decode()
        except Exception as exc:  # noqa: BLE001 - report and retry
            last = exc
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url[:120]}...: {last}")


def download_annotations(outdir: Path) -> list[dict[str, str]]:
    """Every GO:0006720 IEA annotation whose WITH/FROM cites this rule."""
    url = QUICKGO_DOWNLOAD.format(go=GO_ID, ref=GO_REF, rule=RULE_ID)
    path = outdir / f"{RULE_ID}-annotations.tsv"
    path.write_text(fetch(url))
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def uniprot_fields(
    accessions: list[str], fields: str, chunk: int = 100
) -> list[list[str]]:
    """Batch UniProt lookups. Rows are returned as raw split TSV fields."""
    rows: list[list[str]] = []
    for start in range(0, len(accessions), chunk):
        batch = accessions[start : start + chunk]
        query = " OR ".join(f"accession:{acc}" for acc in batch)
        url = (
            f"{UNIPROT_SEARCH}?query={urllib.parse.quote(query)}"
            f"&fields={fields}&format=tsv&size=150"
        )
        body = fetch(url)
        rows.extend(line.split("\t") for line in body.strip().split("\n")[1:] if line)
    return rows


def bucket_names(names: list[str]) -> tuple[collections.Counter, collections.Counter]:
    assigned: collections.Counter = collections.Counter()
    other: collections.Counter = collections.Counter()
    for name in names:
        for label, pattern in BUCKETS:
            if re.search(pattern, name, re.I):
                assigned[label] += 1
                break
        else:
            other[name[:75]] += 1
    return assigned, other


def signature_audit(
    accessions: list[str], sample_size: int, seed: int
) -> dict[str, object]:
    """Do the emitted proteins carry the signatures/taxa the rule text implies?

    The only IPR004294 (carotenoid oxygenase) branch in the published rule is
    condition set 7, which additionally requires taxon Mammalia. The only
    IPR000092 (polyprenyl synthetase-like) branch is condition set 16, which
    additionally requires IPR039702 and taxon Ecdysozoa. If the emitted set is
    full of non-mammalian IPR004294 proteins, the published condition sets do
    not explain the annotations they are credited with.
    """
    random.seed(seed)
    sample = random.sample(accessions, min(sample_size, len(accessions)))
    rows = uniprot_fields(
        sample, "accession,protein_name,organism_name,lineage,xref_interpro"
    )
    n_ipr4294 = n_ipr4294_nonmammal = 0
    n_ipr92 = n_ipr92_with_39702 = 0
    for row in rows:
        lineage = row[3] if len(row) > 3 else ""
        interpro = row[4] if len(row) > 4 else ""
        if "IPR004294" in interpro:
            n_ipr4294 += 1
            if "Mammalia" not in lineage:
                n_ipr4294_nonmammal += 1
        if "IPR000092" in interpro:
            n_ipr92 += 1
            if "IPR039702" in interpro:
                n_ipr92_with_39702 += 1
    return {
        "sampled": len(rows),
        "IPR004294_carotenoid_oxygenase": n_ipr4294,
        "IPR004294_but_not_Mammalia": n_ipr4294_nonmammal,
        "IPR000092_polyprenyl_synthetase_like": n_ipr92,
        "IPR000092_also_with_IPR039702": n_ipr92_with_39702,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outdir", type=Path, default=Path("/tmp/arba27853"))
    parser.add_argument("--sample-size", type=int, default=300)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    annotations = download_annotations(args.outdir)
    accessions = sorted({row["GENE PRODUCT ID"] for row in annotations})
    taxa = {row["TAXON ID"] for row in annotations}
    print(f"annotations: {len(annotations)}")
    print(f"distinct proteins: {len(accessions)}")
    print(f"distinct taxa: {len(taxa)}")

    name_rows = uniprot_fields(accessions, "accession,protein_name,organism_name")
    (args.outdir / f"{RULE_ID}-names.tsv").write_text(
        "\n".join("\t".join(row) for row in name_rows)
    )
    names = [row[1] for row in name_rows if len(row) > 1]
    assigned, other = bucket_names(names)

    print("\n== protein-name census ==")
    total = len(names) or 1
    for label, _ in BUCKETS:
        count = assigned[label]
        if count:
            print(f"{count:6d} ({100 * count / total:5.1f}%)  {label}")
    n_other = sum(other.values())
    print(f"{n_other:6d} ({100 * n_other / total:5.1f}%)  OTHER/unclassified")
    print("\n-- unclassified names (top 40) --")
    for name, count in other.most_common(40):
        print(f"  {count:5d}  {name}")

    print("\n== signature/taxon audit ==")
    audit = signature_audit(accessions, args.sample_size, args.seed)
    print(json.dumps(audit, indent=2))

    summary = {
        "rule": RULE_ID,
        "go_term": GO_ID,
        "annotations": len(annotations),
        "proteins": len(accessions),
        "taxa": len(taxa),
        "name_census": dict(assigned),
        "unclassified": n_other,
        "signature_audit": audit,
    }
    (args.outdir / f"{RULE_ID}-census.json").write_text(json.dumps(summary, indent=2))
    print(f"\nwrote {args.outdir / f'{RULE_ID}-census.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
