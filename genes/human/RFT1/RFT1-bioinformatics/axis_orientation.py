"""Independent check of side-chain orientation for selected RFT1 residues.

Two OpenScientist runs disagreed about whether E298 points into the central
cavity or out toward the lipid/solvent. Both used AF-Q96AA3-F1 but estimated the
membrane normal differently, so this recomputes the geometry from scratch and
reports how sensitive each call is to the axis estimate.

Deliberately minimal: no cavity detection, no conservation. The single question
is whether a side chain points toward or away from the membrane-normal axis, and
how stable that answer is when the axis is perturbed.

Run: uv run python axis_orientation.py
"""

import math
import pathlib

import numpy as np

CIF = pathlib.Path(__file__).parent / "AF-Q96AA3-F1-model_v6.cif"
CIF_URL = "https://alphafold.ebi.ac.uk/files/AF-Q96AA3-F1-model_v6.cif"
TARGETS = [64, 67, 152, 186, 283, 290, 298, 378, 435]
BACKBONE = {"N", "CA", "C", "O", "OXT"}


def parse_atoms(path):
    """Yield (resnum, resname, atom, xyz, plddt) from an mmCIF atom_site loop."""
    lines = path.read_text().splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip() == "loop_":
            j, cols = i + 1, []
            while j < len(lines) and lines[j].lstrip().startswith("_"):
                cols.append(lines[j].strip())
                j += 1
            if any(c.startswith("_atom_site.") for c in cols):
                idx = {c.split(".", 1)[1]: k for k, c in enumerate(cols)}
                while j < len(lines) and not lines[j].startswith(("#", "loop_")):
                    f = lines[j].split()
                    if len(f) >= len(cols):
                        yield (
                            int(f[idx["label_seq_id"]]),
                            f[idx["label_comp_id"]],
                            f[idx["label_atom_id"]],
                            np.array([float(f[idx["Cartn_x"]]),
                                      float(f[idx["Cartn_y"]]),
                                      float(f[idx["Cartn_z"]])]),
                            float(f[idx["B_iso_or_equiv"]]),
                        )
                    j += 1
                return
            i = j
        else:
            i += 1


def membrane_normal(ca):
    """Principal direction of local helix axes.

    Helices alternate up/down through the membrane, so summing v*v^T (which is
    sign-invariant) recovers the shared direction rather than cancelling it.
    """
    nums = sorted(ca)
    m = np.zeros((3, 3))
    for n in nums:
        if all(n + k in ca for k in (1, 2, 3, 4)):
            span = ca[n + 4] - ca[n]
            # i->i+4 spans ~6.2 A in an alpha helix; reject extended/loop segments
            if 5.0 < np.linalg.norm(span) < 7.0:
                v = span / np.linalg.norm(span)
                m += np.outer(v, v)
    w, vec = np.linalg.eigh(m)
    return vec[:, np.argmax(w)]


def rotate(axis, tilt_deg, phi):
    """Tilt `axis` by tilt_deg about an arbitrary perpendicular chosen by phi."""
    a = axis / np.linalg.norm(axis)
    tmp = np.array([1.0, 0, 0]) if abs(a[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(a, tmp); e1 /= np.linalg.norm(e1)
    e2 = np.cross(a, e1)
    perp = math.cos(phi) * e1 + math.sin(phi) * e2
    t = math.radians(tilt_deg)
    return a * math.cos(t) + perp * math.sin(t)


def radial(point, centre, axis):
    d = point - centre
    return np.linalg.norm(d - np.dot(d, axis) * axis)


def fetch_model():
    """Download the AlphaFold model if it is not already present."""
    if CIF.exists():
        return
    import urllib.request
    print(f"downloading {CIF_URL}")
    urllib.request.urlretrieve(CIF_URL, CIF)


def main():
    fetch_model()
    ca, sc, plddt, name = {}, {}, {}, {}
    for num, res, atom, xyz, b in parse_atoms(CIF):
        name[num] = res
        if atom == "CA":
            ca[num], plddt[num] = xyz, b
        if atom not in BACKBONE:
            sc.setdefault(num, []).append(xyz)

    axis = membrane_normal(ca)
    coords = np.array([ca[n] for n in sorted(ca)])
    centre = coords.mean(axis=0)

    # TM slab: residues within 15 A of the membrane centre along the normal
    z = {n: float(np.dot(ca[n] - centre, axis)) for n in ca}
    tm = [n for n in ca if abs(z[n]) <= 15.0]

    delta = {n: radial(np.mean(sc[n], axis=0), centre, axis) - radial(ca[n], centre, axis)
             for n in tm if n in sc}
    vals = np.array(list(delta.values()))
    print(f"model            : {CIF.name}")
    print(f"residues         : {len(ca)}   TM slab (|z|<=15 A): {len(tm)}")
    print(f"delta_radial over TM: median {np.median(vals):+.2f} A  "
          f"(negative = side chain points toward the axis)\n")

    print(f"{'res':>8} {'pLDDT':>6} {'z':>7} {'r_CA':>6} {'dRad':>7} {'call':>9}  axis-perturbation")
    for t in TARGETS:
        if t not in delta:
            print(f"{name.get(t,'?')+str(t):>8}   not in TM slab (z={z.get(t, float('nan')):+.1f} A)")
            continue
        # stability: fraction of perturbed axes (+-20 deg, 12 azimuths) keeping the sign
        inward = 0
        trials = 0
        for tilt in (10, 20):
            for k in range(12):
                a2 = rotate(axis, tilt, 2 * math.pi * k / 12)
                c2 = coords.mean(axis=0)
                d2 = radial(np.mean(sc[t], axis=0), c2, a2) - radial(ca[t], c2, a2)
                inward += d2 < 0
                trials += 1
        call = "inward" if delta[t] < 0 else "outward"
        print(f"{name[t]+str(t):>8} {plddt[t]:6.1f} {z[t]:+7.1f} "
              f"{radial(ca[t], centre, axis):6.1f} {delta[t]:+7.2f} {call:>9}  "
              f"{inward}/{trials} perturbed axes inward")


if __name__ == "__main__":
    main()
