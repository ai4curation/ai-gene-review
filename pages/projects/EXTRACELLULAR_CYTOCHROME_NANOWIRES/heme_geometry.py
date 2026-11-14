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
different numbers of hemes.

Fe-Fe is a proxy for the edge-to-edge porphyrin distances the papers quote, which
are smaller; it is used here because it is unambiguous and needs no ring geometry.
Structures that contain several chains include inter-subunit neighbours, which is
the physiologically relevant case for a polymer.

Usage::

    uv run python heme_geometry.py                    # the four filament structures
    uv run python heme_geometry.py 6NEF 7TFS          # named PDB entries

Entries are cached under .cache/ beside this script. Network required on first run.
"""

from __future__ import annotations

import math
import statistics
import sys
import urllib.request
from pathlib import Path

#: OmcS, OmcE and the two independent OmcZ depositions.
DEFAULT_ENTRIES = ("6NEF", "7TFS", "7LQ5", "8D9M")

LABELS = {
    "6NEF": "OmcS   (Q74A86)",
    "6EF8": "OmcS   (Q74A86)",
    "7TFS": "OmcE   (Q74FJ0)",
    "7LQ5": "OmcZ   (Q74BG5)",
    "8D9M": "OmcZ   (Q74BG5), independent deposition",
}

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


def nearest_neighbour_distances(sites) -> list[float]:
    """For each heme iron, the distance to the closest other heme iron, in Angstrom."""
    out = []
    for i, a in enumerate(sites):
        others = [math.dist(a[2:5], b[2:5]) for j, b in enumerate(sites) if j != i]
        if others:
            out.append(min(others))
    return out


def report(entry: str, cache: Path) -> None:
    sites = iron_sites(fetch(entry, cache))
    label = LABELS.get(entry, entry)
    if not sites:
        print(f"{entry}  {label}: no heme iron found")
        return
    chains = {chain for chain, *_ in sites}
    nn = nearest_neighbour_distances(sites)
    quartiles = statistics.quantiles(nn, n=4) if len(nn) > 3 else None
    iqr = f"  IQR {quartiles[0]:.1f}-{quartiles[2]:.1f}" if quartiles else ""
    print(
        f"{entry}  {label}\n"
        f"    {len(sites)} hemes over {len(chains)} chain(s)"
        f" = {len(sites) / len(chains):.0f} per protomer\n"
        f"    nearest-neighbour Fe-Fe: median {statistics.median(nn):.1f} A"
        f"  (min {min(nn):.1f}, max {max(nn):.1f}){iqr}"
    )


def main(argv: list[str] | None = None) -> int:
    args = (argv if argv is not None else sys.argv[1:]) or list(DEFAULT_ENTRIES)
    cache = Path(__file__).resolve().parent / ".cache"
    for entry in args:
        report(entry.upper(), cache)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
