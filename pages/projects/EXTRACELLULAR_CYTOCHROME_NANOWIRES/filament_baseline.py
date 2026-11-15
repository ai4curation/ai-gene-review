#!/usr/bin/env python3
"""How badly does the cheap sequence filter for cytochrome filaments over-select?

The project page proposes a pure-sequence candidate generator for extracellular
cytochrome nanowires -- at least N covalent heme motifs, a signal peptide, and no
transmembrane segment -- and notes that it must be run before any structural work,
because if it is specific enough on its own the structural half is unnecessary, and
if it is hopeless the structural half has to carry everything.

This script runs it over a whole proteome and reports the funnel, so the
over-selection is a number rather than a guess. It needs no structures.

Heme motifs counted:
  CXXCH    the canonical c-type attachment motif
  CXXXCH   a common variant (ImcH carries one)
  CX(4-20)CH  rare long-linker variants (OmcZ's heme II uses CX14CH)

Known positives and negatives for this organism are labelled in the output so the
recall and the character of the false positives can both be read off directly.

Usage::

    uv run python filament_baseline.py                   # G. sulfurreducens PCA
    uv run python filament_baseline.py UP000008707       # another proteome
    uv run python filament_baseline.py --min-hemes 4 --max-hemes 8

The proteome TSV is cached under a git-ignored .cache/ beside this script.
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_PROTEOME = "UP000000577"  # Geobacter sulfurreducens PCA

FIELDS = (
    "accession,id,protein_name,gene_names,length,reviewed,"
    "ft_signal,ft_transmem,ft_lipid,keyword,xref_interpro,sequence"
)
STREAM = "https://rest.uniprot.org/uniprotkb/stream"
INTERPRO_ENTRY = "https://www.ebi.ac.uk/interpro/api/entry/interpro/{acc}/"

#: InterPro family-level entries the characterised subunits themselves carry, so
#: they cannot be used to exclude. IPR051174 is only the mirror of PANTHER
#: PTHR30333, the family this project's own review records as heterogeneous.
GENERIC_FAMILIES = {"IPR051174"}

CXXCH = re.compile(r"C..CH")
CXXXCH = re.compile(r"C...CH")
LONG_LINKER = re.compile(r"C.{4,20}CH")

#: Characterised filament subunits of G. sulfurreducens, plus OmcS's tandem paralog.
POSITIVES = {
    "Q74A86": "OmcS, filament",
    "Q74FJ0": "OmcE, filament",
    "Q74BG5": "OmcZ, filament",
    "Q74A87": "OmcT, OmcS paralog",
}
#: The G. sulfurreducens members of CDD cd21555, the hand-curated OmcS-like model.
#: A hit that is also a cd21555 member is a plausible candidate, not a clear error.
CD21555 = {"Q74A86", "Q74A87", "Q74A89", "Q74FA8"}

#: Multiheme cytochromes that are emphatically not filament subunits.
NEGATIVES = {
    "Q747K6": "ImcH, inner membrane",
    "Q74FN7": "CbcL, inner membrane",
    "Q74EV9": "GSU2359",
}


def fetch(proteome: str, cache: Path) -> Path:
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"{proteome}.tsv"
    if not path.exists():
        query = urllib.parse.urlencode(
            {"query": f"proteome:{proteome}", "fields": FIELDS, "format": "tsv"}
        )
        req = urllib.request.Request(
            f"{STREAM}?{query}", headers={"User-Agent": "filament-baseline/1.0"}
        )
        with urllib.request.urlopen(req, timeout=300) as resp:  # noqa: S310 (UniProt)
            path.write_bytes(resp.read())
    return path


_IPR_TYPE: dict[str, tuple[str, str]] = {}


def interpro_type(acc: str) -> tuple[str, str]:
    """(entry type, name) for an InterPro accession; ('?', '?') if unreachable."""
    if acc not in _IPR_TYPE:
        try:
            req = urllib.request.Request(
                INTERPRO_ENTRY.format(acc=acc),
                headers={"User-Agent": "filament-baseline/1.0"},
            )
            with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310 (EBI)
                m = json.load(resp)["metadata"]
            _IPR_TYPE[acc] = (m.get("type") or "?", m["name"]["name"])
        except Exception:  # pragma: no cover - network dependent
            _IPR_TYPE[acc] = ("?", "?")
    return _IPR_TYPE[acc]


def named_families(interpro_field: str) -> list[tuple[str, str]]:
    """InterPro family-level entries that name a specific functional class.

    The characterised subunits carry only homologous superfamilies and structural
    domains, so a family-level entry such as Cytochrome c552 or Octaheme c-type
    cytochrome marks a protein whose function is already classified as something
    else. See BASELINE.md for why this rule is the weaker of the two.
    """
    out = []
    for acc in (x.strip() for x in interpro_field.split(";")):
        if not acc or acc in GENERIC_FAMILIES:
            continue
        kind, name = interpro_type(acc)
        if kind == "family":
            out.append((acc, name))
    return out


def is_lipoprotein(lipid_field: str, keyword_field: str) -> bool:
    """A lipid-anchored protein is tethered to a membrane, not a free polymer subunit."""
    return bool(lipid_field.strip()) or "Lipoprotein" in keyword_field


def heme_motifs(seq: str) -> int:
    """Non-overlapping count of covalent heme-attachment motifs."""
    spans: list[tuple[int, int]] = []
    for pattern in (CXXCH, CXXXCH, LONG_LINKER):
        for m in pattern.finditer(seq):
            if not any(s <= m.start() < e for s, e in spans):
                spans.append((m.start(), m.end()))
    return len(spans)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("proteome", nargs="?", default=DEFAULT_PROTEOME)
    p.add_argument("--min-hemes", type=int, default=4)
    p.add_argument(
        "--max-hemes",
        type=int,
        default=None,
        help="upper bound on heme motifs; the known subunits carry 4-8",
    )
    p.add_argument(
        "--refine",
        action="store_true",
        help="also drop lipoproteins and proteins carrying a named InterPro family",
    )
    p.add_argument(
        "--no-require-signal",
        dest="require_signal",
        action="store_false",
        help=(
            "do not require an annotated signal peptide. Measured to recover a genuine "
            "member whose UniProt entry lacks the annotation, at ~25%% more candidates, "
            "while excluding no known negative; see BASELINE.md"
        ),
    )
    args = p.parse_args(argv)

    cache = Path(__file__).resolve().parent / ".cache"
    rows = fetch(args.proteome, cache).read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t")
    idx = {name: i for i, name in enumerate(header)}

    total = multiheme = with_signal = passing = 0
    dropped_lipo = dropped_family = refined = 0
    hits = []
    for line in rows[1:]:
        f = line.split("\t")
        if len(f) < len(header):
            continue
        total += 1
        seq = f[idx["Sequence"]]
        n = heme_motifs(seq)
        if n < args.min_hemes or (args.max_hemes is not None and n > args.max_hemes):
            continue
        multiheme += 1
        has_signal = bool(f[idx["Signal peptide"]].strip())
        has_tm = bool(f[idx["Transmembrane"]].strip())
        if args.require_signal and not has_signal:
            continue
        with_signal += 1
        if has_tm:
            continue
        passing += 1
        if args.refine:
            if is_lipoprotein(f[idx["Lipidation"]], f[idx["Keywords"]]):
                dropped_lipo += 1
                continue
            if named_families(f[idx["InterPro"]]):
                dropped_family += 1
                continue
            refined += 1
        hits.append(
            (
                f[idx["Entry"]],
                f[idx["Gene Names"]].split(" ")[0],
                f[idx["Protein names"]][:46],
                n,
                f[idx["Length"]],
            )
        )

    print(f"proteome {args.proteome}: {total} proteins\n")
    window = (
        f">= {args.min_hemes}"
        if args.max_hemes is None
        else f"{args.min_hemes}-{args.max_hemes}"
    )
    print(f"  {window} heme motifs{'':<16}{multiheme:>5}")
    sig_label = (
        "  ... and a signal peptide     "
        if args.require_signal
        else "  ... (signal not required)   "
    )
    print(f"{sig_label}{with_signal:>5}")
    if args.refine:
        print(f"  ... and no TM segment         {passing:>5}")
        print(
            f"  ... and not a lipoprotein     {passing - dropped_lipo:>5}  (-{dropped_lipo})"
        )
        print(
            f"  ... and no named IPR family   {refined:>5}  (-{dropped_family})   <- candidate set"
        )
        final = refined
    else:
        print(f"  ... and no TM segment         {passing:>5}   <- candidate set")
        final = passing
    print(
        f"\n  over-selection vs the 3 characterised filament subunits: {final / 3:.0f}x"
    )
    also_cd = sum(1 for h in hits if h[0] in CD21555)
    print(
        f"  of the {final} candidates, {also_cd} are also CDD cd21555 members"
        f" (plausible, not clear errors)\n"
    )

    found = {h[0] for h in hits}
    print("  recall on known filament subunits:")
    for acc, label in POSITIVES.items():
        print(f"    {'PASS' if acc in found else 'MISS'}  {acc}  {label}")
    print("\n  known non-filament multiheme cytochromes:")
    for acc, label in NEGATIVES.items():
        print(
            f"    {'passed (false positive)' if acc in found else 'excluded'}  {acc}  {label}"
        )

    print(f"\n  all {len(hits)} candidates:")
    for acc, gene, name, n, length in sorted(hits, key=lambda h: -h[3]):
        tag = (
            "  <-- known filament"
            if acc in POSITIVES
            else "  (cd21555 member)"
            if acc in CD21555
            else ""
        )
        print(f"    {acc:<10} {gene:<10} {n:>3} motifs  {length:>5} aa  {name}{tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
