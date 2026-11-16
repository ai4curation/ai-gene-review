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

Known positives, negatives and structural near-misses are registered per proteome in
KNOWN, so recall and the character of the false positives can both be read off directly.

Two of the opening conditions were later measured to be wrong:

  * a floor of four heme motifs loses the P. calidifontis filament entirely, which binds
    four hemes through only three motifs. The default floor is therefore now 3.
  * the signal-peptide requirement cost a real positive and excluded no known negative.
    It is still ON by default, so that the funnel documented in BASELINE.md reproduces
    exactly; --no-require-signal turns it off and is the recommended setting.

So the recommended invocation is not the default. Use:

    uv run python filament_baseline.py <PROTEOME> --max-hemes 8 --refine --no-require-signal

which is what the five-proteome table in BASELINE.md was made with.

Usage::

    uv run python filament_baseline.py                   # G. sulfurreducens PCA
    uv run python filament_baseline.py UP000001431       # Pyrobaculum calidifontis
    uv run python filament_baseline.py --min-hemes 4 --max-hemes 8

The proteome TSV is cached under a git-ignored .cache/ beside this script.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
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

#: Per-proteome ground truth. Three categories, deliberately kept apart:
#:
#:   positives   subunits of a structurally characterised filament
#:   negatives   multiheme cytochromes that are emphatically not filament subunits
#:   near_misses proteins a structural study considered and excluded *on structural
#:               grounds alone*. These are not biological negatives: nothing in their
#:               sequence marks them, so a sequence filter cannot be faulted for
#:               keeping them, and counting them as errors would understate what the
#:               structural second stage is for.
KNOWN: dict[str, dict] = {
    "UP000000577": {
        "organism": "Geobacter sulfurreducens PCA",
        "positives": {
            "Q74A86": "OmcS, filament",
            "Q74FJ0": "OmcE, filament",
            "Q74BG5": "OmcZ, filament",
            "Q74A87": "OmcT, OmcS paralog",
        },
        "negatives": {
            "Q747K6": "ImcH, inner membrane",
            "Q74FN7": "CbcL, inner membrane",
            "Q74EV9": "GSU2359",
        },
        #: Members of CDD cd21555, the hand-curated OmcS-like model. A hit that is
        #: also a cd21555 member is a plausible candidate, not a clear error.
        "cd21555": {"Q74A86", "Q74A87", "Q74A89", "Q74FA8"},
    },
    # Two held-out Geobacteraceae. Their "known members" are homologs in CDD
    # cd21555, the hand-curated OmcS-like model -- membership in a curated model,
    # not a solved filament, so recall here is a weaker claim than for the four
    # G. sulfurreducens subunits or the two archaeal cryo-EM structures.
    "UP000008825": {
        "organism": "Citrifermentans bemidjiense Bem",
        "positives": {
            "B5EH34": "omcS-1, cd21555 homolog",
            "B5EH35": "Gbem_1117, cd21555 homolog",
            "B5EH49": "Gbem_1131, cd21555 homolog",
            "B5EHE9": "omcS-2, cd21555 homolog",
            "B5EHF0": "omcS-3, cd21555 homolog",
        },
        "negatives": {},
    },
    "UP000007721": {
        "organism": "Geotalea daltonii FRC-32",
        "positives": {
            "B9M443": "Geob_3155, cd21555 homolog",
            "B9M454": "Geob_3166, cd21555 homolog",
        },
        "negatives": {},
    },
    # Baquero et al. 2023 (PMID:37290436) solved two archaeal ECNs by cryo-EM and
    # named, for each proteome, every protein they considered and why they rejected it.
    # That makes these two the only proteomes with published negative reasoning.
    "UP000001431": {
        "organism": "Pyrobaculum calidifontis VA1",
        "positives": {"A3MW92": "PcECN, filament (cryo-EM, PMID:37290436)"},
        "negatives": {
            "A3MW94": "8 motifs, too many hemes per subunit; TM segment",
            "A3MW99": "8 motifs, too many hemes per subunit; TM segment",
        },
        "near_misses": {"A3MW89": "AlphaFold fold does not match the cryo-EM map"},
    },
    "UP000008136": {
        "organism": "Archaeoglobus veneficus SNP6",
        "positives": {"F2KMU8": "AvECN, filament (cryo-EM, PMID:37290436)"},
        "negatives": {},
        "near_misses": {
            "F2KMU7": "helix-rich region 120-150 unexplained by the cryo-EM map",
            "F2KPF5": "loop 131-151 too short to fit the map",
        },
    },
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
_IPR_CACHE: Path | None = None


def load_interpro_cache(cache: Path) -> None:
    """Back the InterPro type lookups with a file, so a run is reproducible.

    Without this the numbers in BASELINE.md are not reproducible: an unresolved
    lookup used to be swallowed and reported as ('?', '?'), which is not a family,
    so a transient EBI failure silently made the filter *more permissive* and the
    candidate count larger. One such run put G. daltonii at 31 instead of 24.
    """
    global _IPR_CACHE
    _IPR_CACHE = cache / "interpro_types.json"
    if _IPR_CACHE.exists():
        _IPR_TYPE.update(
            {k: (v[0], v[1]) for k, v in json.loads(_IPR_CACHE.read_text()).items()}
        )


def _save_interpro_cache() -> None:
    if _IPR_CACHE is not None:
        _IPR_CACHE.write_text(
            json.dumps({k: list(v) for k, v in sorted(_IPR_TYPE.items())}, indent=0)
        )


def interpro_type(acc: str) -> tuple[str, str]:
    """(entry type, name) for an InterPro accession.

    Raises after three failed attempts rather than returning a value that would
    quietly pass the filter. A measurement that cannot resolve its inputs must
    stop, not report a larger number.
    """
    if acc not in _IPR_TYPE:
        last: Exception | None = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    INTERPRO_ENTRY.format(acc=acc),
                    headers={"User-Agent": "filament-baseline/1.0"},
                )
                with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310 (EBI)
                    m = json.load(resp)["metadata"]
                _IPR_TYPE[acc] = (m.get("type") or "?", m["name"]["name"])
                _save_interpro_cache()
                break
            except urllib.error.HTTPError as exc:  # pragma: no cover - network
                if exc.code == 404:  # a real answer: InterPro has no such entry
                    _IPR_TYPE[acc] = ("absent", "absent")
                    _save_interpro_cache()
                    break
                last = exc
                time.sleep(2**attempt)
            except Exception as exc:  # pragma: no cover - network dependent
                last = exc
                time.sleep(2**attempt)
        else:
            raise RuntimeError(
                f"could not resolve InterPro entry {acc} after 3 attempts ({last}). "
                "Refusing to continue: an unresolved lookup would silently pass the "
                "named-family filter and inflate the candidate count."
            )
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
    """Non-overlapping count of covalent heme-attachment motifs.

    Patterns are tried canonical-first, so a CXXCH is claimed before any
    long-linker match that would consume the same residues. A candidate is
    rejected if its span overlaps an accepted one *anywhere* -- testing only
    whether the start is inside an accepted span double-counts a long-linker
    match that ends on a His already used by a shorter motif, which inflated
    *P. calidifontis* A3MW92 from 3 to 4. See BASELINE.md.
    """
    spans: list[tuple[int, int]] = []
    for pattern in (CXXCH, CXXXCH, LONG_LINKER):
        for m in pattern.finditer(seq):
            if not any(m.start() < e and s < m.end() for s, e in spans):
                spans.append((m.start(), m.end()))
    return len(spans)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("proteome", nargs="?", default=DEFAULT_PROTEOME)
    p.add_argument(
        "--min-hemes",
        type=int,
        default=3,
        help=(
            "lower bound on heme motifs. 3, not 4: the P. calidifontis filament "
            "carries four hemes per subunit but only three CXXCH motifs, so a floor "
            "of 4 loses it entirely. See BASELINE.md"
        ),
    )
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
    cache.mkdir(parents=True, exist_ok=True)
    load_interpro_cache(cache)
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
    known = KNOWN.get(args.proteome, {})
    positives = known.get("positives", {})
    negatives = known.get("negatives", {})
    near_misses = known.get("near_misses", {})
    cd21555 = known.get("cd21555", set())

    if positives:
        print(
            f"\n  over-selection vs the {len(positives)} known filament"
            f" subunit(s): {final / len(positives):.0f}x"
        )
    if cd21555:
        also_cd = sum(1 for h in hits if h[0] in cd21555)
        print(
            f"  of the {final} candidates, {also_cd} are also CDD cd21555 members"
            f" (plausible, not clear errors)"
        )
    if not known:
        print(f"\n  no ground truth registered for {args.proteome}")

    found = {h[0] for h in hits}
    if positives:
        print("\n  recall on known filament subunits:")
        for acc, label in positives.items():
            print(f"    {'PASS' if acc in found else 'MISS'}  {acc}  {label}")
    if negatives:
        print("\n  known non-filament multiheme cytochromes:")
        for acc, label in negatives.items():
            verdict = "passed (false positive)" if acc in found else "excluded"
            print(f"    {verdict}  {acc}  {label}")
    if near_misses:
        print("\n  excluded by structure alone (not sequence-separable):")
        for acc, label in near_misses.items():
            verdict = "passed (expected)" if acc in found else "excluded by sequence"
            print(f"    {verdict}  {acc}  {label}")

    print(f"\n  all {len(hits)} candidates:")
    for acc, gene, name, n, length in sorted(hits, key=lambda h: -h[3]):
        tag = (
            "  <-- known filament"
            if acc in positives
            else "  (cd21555 member)"
            if acc in cd21555
            else "  (structural near-miss)"
            if acc in near_misses
            else ""
        )
        print(f"    {acc:<10} {gene:<10} {n:>3} motifs  {length:>5} aa  {name}{tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
