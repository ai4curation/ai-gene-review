#!/usr/bin/env python3
"""Fe-Fe geometry of the heme chains in cytochrome filament structures.

The literature claim this tests is that extracellular cytochrome nanowires form a
class defined by heme packing rather than by sequence or fold: Wang et al. report
that OmcE and OmcS have "no overall sequence or structural similarities" yet share
a heme arrangement (PMID:35798889), and Baquero et al. say the same across domains,
that "the ECN protein subunits lack similarities in their folds; however, they share
a common heme arrangement" (PMID:37290436).

That is checkable from coordinates. For each deposited structure this reads the
heme-c iron positions and reports the nearest-neighbour Fe-Fe distance distribution.
If the claim holds, the medians should cluster despite the proteins carrying
different numbers of hemes. They do: 9.1-10.4 A across five proteins and two domains.

The claim that matters for classification is a different one, and it fails. A band
that every member shares is only useful as a filter if non-members fall outside it,
so this also measures non-filament multiheme cytochromes. The cytochrome c3 entries
the literature offers as look-alikes separate cleanly (11.4-11.7 A), but the
pentaheme nitrite reductases do not: NrfA sits at 9.7 A in three independent
structures, inside the filament band, and NrfA is exactly what the sequence screen
in BASELINE.md yields as a false positive. Spacing therefore cannot be the precision
stage.

What does separate them is whether the heme chain is continuous *through* the subunit
interface -- see chain_continuity() -- which is a property of the polymer and not of
the subunit. The filaments measure 1.00x; the hardest control, the NrfHA complex in
which electrons genuinely cross a subunit interface, measures 1.10x.

Fe-Fe is a proxy for the edge-to-edge porphyrin distances the papers quote, which
are smaller; it is used here because it is unambiguous and needs no ring geometry.
Multi-chain structures report both the pooled nearest neighbour (right for a polymer,
where the inter-subunit contact is part of the wire) and the within-chain one (right
for a soluble protein crystallised in several copies).

Usage::

    uv run python heme_geometry.py                    # in-class and out-of-class sets
    uv run python heme_geometry.py 6NEF 7TFS          # named PDB entries

Entries are cached under .cache/ beside this script. Network required on first run.
"""

from __future__ import annotations

import math
import statistics
import sys
import urllib.request
from pathlib import Path

#: In class: the three G. sulfurreducens filaments (with a second OmcZ deposition as
#: an internal control and a 7-subunit OmcS segment), plus the two archaeal ECNs.
IN_CLASS = ("7TFS", "6NEF", "6EF8", "7LQ5", "8D9M", "8E5F", "8E5G", "9YUQ")

#: Out of class. The c3/Hmc entries are the ones PMID:36732469 names as having
#: "similar haem-haem distances"; the Nrf entries are the sequence screen's own
#: hardest false positives, and they are the ones that actually fall in the
#: filament band. See RESULTS.md.
OUT_OF_CLASS = ("1GYO", "2BQ4", "2E84", "1OAH", "2J7A", "3L1T")

DEFAULT_ENTRIES = IN_CLASS + OUT_OF_CLASS

LABELS = {
    # In class: the characterised filaments.
    "6NEF": "OmcS   (Q74A86), one subunit",
    "6EF8": "OmcS   (Q74A86), 7-subunit filament segment",
    "7TFS": "OmcE   (Q74FJ0), one subunit",
    "7LQ5": "OmcZ   (Q74BG5), 3-subunit filament segment",
    "8D9M": "OmcZ   (Q74BG5), independent deposition",
    "8E5F": "PcECN  (A3MW92), Pyrobaculum calidifontis",
    "8E5G": "AvECN  (F2KMU8), Archaeoglobus veneficus",
    "9YUQ": "DsECN  (A0A0M4DKA8), Desulfuromonas soudanensis, 16-chain bundle",
    # Out of class, named by PMID:36732469 as having "similar haem-haem distances".
    "1GYO": "c3     di-tetraheme cytochrome c3, D. gigas  [OUT OF CLASS]",
    "2BQ4": "c3     type I cytochrome c3, D. africanus  [OUT OF CLASS]",
    "2E84": "Hmc    16-heme high-molecular-weight cytochrome c, D. vulgaris  [OUT OF CLASS]",
    # Out of class, and the screen's own false positives: pentaheme nitrite
    # reductases. 2J7A is the NrfHA complex, where electrons really do cross a
    # subunit interface, so it is the hardest control for a continuity criterion.
    "1OAH": "NrfA   nitrite reductase, D. desulfuricans  [OUT OF CLASS]",
    "2J7A": "NrfHA  nitrite reductase complex, D. vulgaris  [OUT OF CLASS]",
    "3L1T": "NrfA   nitrite reductase, E. coli  [OUT OF CLASS]",
}

#: A heme chain counts as continuous through the subunit interface when the closest
#: inter-chain Fe-Fe is within this factor of the intra-chain spacing. The filaments
#: measure 1.00 -- the spacing simply does not change at the interface -- and the
#: closest non-filament measured is 1.10 (the NrfHA complex). Provisional: it rests
#: on two multi-subunit filament depositions. See RESULTS.md.
CONTINUITY_FACTOR = 1.05

CIF_URL = "https://files.rcsb.org/download/{entry}.cif"
HEME_COMPS = {"HEC", "HEM"}


def fetch(entry: str, cache: Path) -> Path:
    """Return a local path to the mmCIF for *entry*, downloading it once."""
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"{entry}.cif"
    if not path.exists():
        req = urllib.request.Request(
            CIF_URL.format(entry=entry), headers={"User-Agent": "heme-geometry/1.0"}
        )
        with urllib.request.urlopen(req, timeout=90) as resp:  # noqa: S310 (RCSB)
            path.write_bytes(resp.read())
    return path


def iron_sites(path: Path) -> list[tuple[str, str, float, float, float]]:
    """(chain, residue, x, y, z) for every heme iron in an mmCIF file."""
    sites: list[tuple[str, str, float, float, float]] = []
    order: list[str] = []
    cols: dict[str, int] = {}
    in_loop = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("_atom_site."):
            order.append(line.strip().split(".", 1)[1])
            in_loop = True
            continue
        if in_loop and (line.startswith("#") or line.startswith("loop_")):
            if sites or cols:
                break
            in_loop = False
            order = []
            continue
        if in_loop and line.strip() and not line.startswith("_"):
            if not cols:
                cols = {name: i for i, name in enumerate(order)}
            fields = line.split()
            if len(fields) < len(order):
                continue
            if (
                fields[cols["label_comp_id"]] in HEME_COMPS
                and fields[cols["label_atom_id"]] == "FE"
            ):
                chain_key = (
                    "auth_asym_id" if "auth_asym_id" in cols else "label_asym_id"
                )
                resid_key = "auth_seq_id" if "auth_seq_id" in cols else "label_seq_id"
                sites.append(
                    (
                        fields[cols[chain_key]],
                        fields[cols[resid_key]],
                        float(fields[cols["Cartn_x"]]),
                        float(fields[cols["Cartn_y"]]),
                        float(fields[cols["Cartn_z"]]),
                    )
                )
    return sites


def nearest_neighbour_distances(sites, within_chain: bool = False) -> list[float]:
    """For each heme iron, the distance to the closest other heme iron, in Angstrom.

    By default every heme in the deposition is a candidate neighbour, which is the
    physiologically relevant case for a polymer: in a filament the inter-subunit
    contact is part of the wire.

    With *within_chain*, only hemes in the same chain are candidates. That is the
    honest measure for a soluble protein whose deposition holds several
    crystallographic copies, where a cross-chain contact is a packing artefact and
    not a conduction path. The two numbers differ only where chains touch, so
    reporting both shows whether a comparison turns on that choice.
    """
    out = []
    for i, a in enumerate(sites):
        others = [
            math.dist(a[2:5], b[2:5])
            for j, b in enumerate(sites)
            if j != i and (not within_chain or b[0] == a[0])
        ]
        if others:
            out.append(min(others))
    return out


def chain_continuity(sites) -> tuple[float, float, float, int, int] | None:
    """Does the heme chain continue across the subunit interface?

    Returns (closest inter-chain Fe-Fe, median intra-chain nearest neighbour,
    fraction of hemes whose nearest neighbour lies in another chain, number of
    chains whose own closest other-chain heme is within CONTINUITY_FACTOR of the
    intra-chain spacing, total chains), or None for a single-chain deposition.

    The last two matter because the first number is an *existence* claim: one close
    pair anywhere in the deposition sets it. The per-chain count says how pervasive
    the continuity is, and the two can disagree. In 6EF8 every one of seven OmcS
    subunits has a neighbour at exactly 1.00x, a wire throughout; 7LQ5 is 3/3. In
    9YUQ, the bundled antiparallel Desulfuromonas filament, two chains sit at 1.00x,
    two at 1.05x, two at 1.05x just over the cutoff and the remaining ten at
    1.29-1.40x. So its minimum is filament-like while most modelled chains are not in
    axial contact, which is a property of what the bundle model contains rather than
    evidence against the filament.

    Treat the per-chain count as indicative only: for 9YUQ it is threshold-sensitive,
    reading 2/16 at a factor of 1.03, 4/16 at 1.05 and 6/16 at 1.07. The minimum
    ratio is the robust statistic -- all three filaments reach 1.00x and no
    non-filament measured here gets below 1.10x, nor has a single chain at or below
    the factor.

    This is the measure that distinguishes a wire from a globular multiheme enzyme,
    and it is not a distance threshold. A filament's hemes form one chain that runs
    *through* the subunit interface, so some hemes -- the ones at each subunit's end
    -- have their nearest neighbour in the neighbouring subunit, at roughly the same
    spacing as inside a subunit. A globular enzyme keeps its hemes inside one
    protomer: even in an obligate dimer no heme's nearest neighbour is across the
    interface. Nearest-neighbour spacing alone does not separate the two, because
    NrfA's spacing sits inside the filament band; continuity does.
    """
    chains = {chain for chain, *_ in sites}
    if len(chains) < 2:
        return None
    inter = [
        math.dist(a[2:5], b[2:5])
        for i, a in enumerate(sites)
        for b in sites[i + 1 :]
        if a[0] != b[0]
    ]
    intra = nearest_neighbour_distances(sites, within_chain=True)
    pooled_is_cross = 0
    for i, a in enumerate(sites):
        best_any = min(
            (math.dist(a[2:5], b[2:5]) for j, b in enumerate(sites) if j != i),
            default=None,
        )
        best_own = min(
            (
                math.dist(a[2:5], b[2:5])
                for j, b in enumerate(sites)
                if j != i and b[0] == a[0]
            ),
            default=None,
        )
        if best_any is not None and (best_own is None or best_any < best_own - 1e-6):
            pooled_is_cross += 1
    median_intra = statistics.median(intra)
    continuous_chains = 0
    for c in chains:
        own = [a for a in sites if a[0] == c]
        other = [b for b in sites if b[0] != c]
        closest = min(math.dist(a[2:5], b[2:5]) for a in own for b in other)
        if closest <= median_intra * CONTINUITY_FACTOR:
            continuous_chains += 1
    return (
        min(inter),
        median_intra,
        pooled_is_cross / len(sites),
        continuous_chains,
        len(chains),
    )


def _summary(nn: list[float]) -> str:
    quartiles = statistics.quantiles(nn, n=4) if len(nn) > 3 else None
    iqr = f"  IQR {quartiles[0]:.1f}-{quartiles[2]:.1f}" if quartiles else ""
    return (
        f"median {statistics.median(nn):.1f} A"
        f"  (min {min(nn):.1f}, max {max(nn):.1f}){iqr}"
    )


def report(entry: str, cache: Path) -> None:
    sites = iron_sites(fetch(entry, cache))
    label = LABELS.get(entry, entry)
    if not sites:
        print(f"{entry}  {label}: no heme iron found")
        return
    chains = {chain for chain, *_ in sites}
    print(
        f"{entry}  {label}\n"
        f"    {len(sites)} hemes over {len(chains)} chain(s)"
        f" = {len(sites) / len(chains):.0f} per protomer\n"
        f"    all chains pooled : {_summary(nearest_neighbour_distances(sites))}"
    )
    if len(chains) > 1:
        print(
            "    within one chain  : "
            f"{_summary(nearest_neighbour_distances(sites, within_chain=True))}"
        )
        cont = chain_continuity(sites)
        if cont is not None:
            closest_inter, median_intra, frac, cont_chains, n_chains = cont
            ratio = closest_inter / median_intra
            verdict = (
                "CONTINUOUS through the interface -> wire-like"
                if ratio <= CONTINUITY_FACTOR
                else "confined within subunits -> not a wire"
            )
            print(
                f"    continuity        : closest inter-chain Fe-Fe {closest_inter:.1f} A"
                f" vs {median_intra:.1f} A intra-chain spacing"
                f" = {ratio:.2f}x;"
                f" {cont_chains}/{n_chains} chains continuous,"
                f" {frac:.0%} of hemes with a cross-chain nearest neighbour"
                f"\n                        -> {verdict}"
            )


def main(argv: list[str] | None = None) -> int:
    args = (argv if argv is not None else sys.argv[1:]) or list(DEFAULT_ENTRIES)
    cache = Path(__file__).resolve().parent / ".cache"
    for entry in args:
        report(entry.upper(), cache)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
