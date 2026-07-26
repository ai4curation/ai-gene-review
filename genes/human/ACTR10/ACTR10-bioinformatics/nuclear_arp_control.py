"""Does the human actin-fold family split into nuclear and cytoplasmic clades?

ACTR10 carries `GO:0005634 nucleus` with the strong `is_active_in` qualifier, by
PAINT phylogenetic propagation (IBA). Resolving the WITH/FROM sources (see
`paint_sources.py`) shows every one of them is a *nuclear* actin-related protein
from a different subfamily - yeast and Candida Arp9 (SWI/SNF and RSC chromatin
remodellers) and mouse Actl7a - not an ACTR10/Arp11 ortholog.

That makes a prediction that can be tested independently of GO: within one species
and one antibody-based dataset, the nuclear ARPs should localise to the nucleoplasm
and the dynactin ARPs should not. This module asks the Human Protein Atlas, using
the human members of each clade as reciprocal controls:

* dynactin clade (expected non-nuclear): ACTR10 itself, plus ACTR1A/ACTR1B, the
  Arp1 centractins that build dynactin's filament;
* nuclear-ARP clade (expected nuclear): ACTL6A, ACTL6B, ACTR5, ACTR6, ACTR8, the
  human subunits of the BAF/PBAF, INO80 and SRCAP chromatin remodellers;
* conventional actin (ACTB) as a reference for the ancestral, mostly cytoplasmic
  state.

Gene membership of each clade is not asserted from memory: each accession is
resolved against UniProt and its recommended name printed, and clade assignment is
reported alongside so a reader can check it. HPA immunofluorescence is
antibody-based and is reported as one line of evidence, not a proof.
"""

from __future__ import annotations

import csv
import io
import json
import sys
import time
import urllib.parse
import urllib.request

# UniProt accessions, one per gene. Clade labels are the hypothesis under test.
PANEL = [
    ("ACTR10", "Q9NZ32", "dynactin pointed end (Arp11)"),
    ("ACTR1A", "P61163", "dynactin filament (Arp1)"),
    ("ACTR1B", "P42025", "dynactin filament (Arp1)"),
    ("ACTB", "P60709", "conventional actin"),
    ("ACTL6A", "O96019", "nuclear ARP (BAF/PBAF)"),
    ("ACTL6B", "O94805", "nuclear ARP (nBAF)"),
    ("ACTR5", "Q9H9F9", "nuclear ARP (INO80)"),
    ("ACTR6", "Q9GZN1", "nuclear ARP (SRCAP)"),
    ("ACTR8", "Q9H981", "nuclear ARP (INO80)"),
]

# HPA uses a controlled vocabulary of subcellular locations. Nuclear compartments are
# matched by exact name, NOT by substring: "Perinuclear theca" is a sperm-head
# cytoplasmic structure and contains the string "nuclear", so substring matching would
# score ACTR10 as nuclear and invert the result of this test.
HPA_NUCLEAR_LOCATIONS = {
    "nucleoplasm",
    "nucleus",
    "nuclear membrane",
    "nuclear speckles",
    "nuclear bodies",
    "nucleoli",
    "nucleoli fibrillar center",
    "nucleoli rim",
    "kinetochore",
    "mitotic chromosome",
}

HPA_URL = "https://www.proteinatlas.org/api/search_download.php"


def http_text(url: str, tries: int = 4) -> str:
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/ACTR10"})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return fh.read().decode()
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url}") from last


def uniprot_name(acc: str) -> tuple[str, str]:
    d = json.loads(
        http_text(f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=protein_name,gene_names")
    )
    name = (
        d.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "?")
    )
    genes = [g["geneName"]["value"] for g in d.get("genes", []) if g.get("geneName")]
    return ("/".join(genes) or "?", name)


def hpa_locations(symbol: str) -> list[str] | None:
    """HPA subcellular locations for `symbol`, or None if HPA has no IF record."""
    url = HPA_URL + "?" + urllib.parse.urlencode(
        {
            "search": symbol,
            "format": "json",
            "columns": "g,scl",
            "compress": "no",
        }
    )
    rows = json.loads(http_text(url))
    for row in rows:
        if row.get("Gene") == symbol:
            locs = row.get("Subcellular location")
            return locs if locs else []
    return None


def main() -> str:
    lines: list[str] = []
    out = lines.append
    out("## D. Nuclear versus dynactin actin-related proteins in one human dataset")
    out("")
    out(
        "The `GO:0005634 nucleus` IBA on ACTR10 is propagated from nuclear ARPs of "
        "another subfamily (Arp9, Actl7a). If that subfamily split is real, then in "
        "human the nuclear ARPs and the dynactin ARPs should localise differently. "
        "Human Protein Atlas immunofluorescence is queried for both clades plus "
        "conventional actin. Antibody-based localisation is one line of evidence, not "
        "proof; it is used here only as a reciprocal control."
    )
    out("")
    out("| gene | UniProt | clade (hypothesis) | recommended name | HPA subcellular locations | nuclear compartment? |")
    out("|---|---|---|---|---|---|")
    summary = {"dynactin": [], "nuclear": []}
    for symbol, acc, clade in PANEL:
        genes, name = uniprot_name(acc)
        locs = hpa_locations(symbol)
        if locs is None:
            cell = "_no HPA immunofluorescence record_"
            nuclear = "n/a"
        elif not locs:
            cell = "_HPA record present but no location reported_"
            nuclear = "n/a"
        else:
            cell = ", ".join(locs)
            matched = [loc for loc in locs if loc.lower() in HPA_NUCLEAR_LOCATIONS]
            # Any location whose name merely contains "nuclear" without being a nuclear
            # compartment is surfaced rather than silently scored either way.
            near_miss = [
                loc
                for loc in locs
                if "nuclear" in loc.lower() and loc.lower() not in HPA_NUCLEAR_LOCATIONS
            ]
            hit = bool(matched)
            nuclear = ("yes (" + ", ".join(matched) + ")") if hit else "no"
            if near_miss:
                nuclear += " [not counted as nuclear: " + ", ".join(near_miss) + "]"
            key = "nuclear" if clade.startswith("nuclear") else "dynactin"
            if clade != "conventional actin":
                summary[key].append((symbol, hit))
        if genes != symbol:
            cell += f" _(UniProt gene name: {genes})_"
        out(f"| {symbol} | {acc} | {clade} | {name} | {cell} | {nuclear} |")
    out("")
    for key, label in (("nuclear", "nuclear-ARP clade"), ("dynactin", "dynactin clade")):
        rows = summary[key]
        if not rows:
            continue
        hits = sum(1 for _, h in rows if h)
        out(
            f"- {label}: {hits}/{len(rows)} genes with a nuclear compartment in their HPA "
            "location list (" + ", ".join(f"{s}:{'nuclear' if h else 'non-nuclear'}" for s, h in rows) + ")"
        )
    out("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.stdout.write(main())
