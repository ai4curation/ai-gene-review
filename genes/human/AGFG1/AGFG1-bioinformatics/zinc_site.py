"""Which residues coordinate the zinc in AGFG1's ArfGAP-domain structures?

Both AGFG1 ArfGAP-domain entries (2OLM, 1.48 A X-ray; 2D9L, NMR) contain one
bound ZINC ION. This computes the Zn coordination shell from the deposited
coordinates so that the claim can be "the zinc is held by Cys29/32/49/52", not
merely "there is a zinc and there is a motif".

Positive control: the same computation on 2QNM/1E0X-style ArfGAP1 is not
available offline, so the control used here is internal and stronger for the
purpose - the coordinating cysteines must be exactly the four the CX2CX16CX2CX4R
scan (arfgap_motif.py) predicts, and the script fails if they are not.

Usage: uv run python zinc_site.py
"""

from __future__ import annotations

import gzip
import json
import math
import pathlib
import urllib.request

OUT = pathlib.Path(__file__).parent / "zinc_site.json"
# From arfgap_motif.py, computed not remembered.
PREDICTED_CYS = [29, 32, 49, 52]
CUTOFF = 3.0  # A; Zn-S bonds are ~2.3 A, so 3.0 is generous but discriminating
SUBJECT = "P52594"


def uniprot_sequence(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=accession,sequence"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        d = json.load(fh)
    assert d["primaryAccession"] == acc, f"{acc} -> {d['primaryAccession']}"
    return d["sequence"]["value"]


def sifts_offset(pdb: str, chain: str, acc: str) -> int:
    """auth-numbering -> UniProt-numbering offset, from SIFTS.

    Deposited author numbering is NOT UniProt numbering: 2D9L is offset by 6.
    Assuming identity silently renumbers a functional site, so the offset is
    read from SIFTS and then checked against the UniProt sequence.
    """
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb}"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        d = json.load(fh)
    maps = d[pdb]["UniProt"][acc]["mappings"]
    hits = [m for m in maps if m["chain_id"] == chain]
    assert len(hits) == 1, f"{pdb} chain {chain}: {len(hits)} SIFTS segments"
    m = hits[0]
    off = m["unp_start"] - m["start"]["author_residue_number"]
    end_auth = m["end"]["author_residue_number"]
    if end_auth is None:
        # 2OLM's SIFTS record has a null end author number; the offset is then
        # only checked at the start, so the caller's per-residue identity check
        # against the UniProt sequence is what validates it.
        print(f"    note: {pdb} SIFTS end.author_residue_number is null; "
              "offset taken from the segment start only")
    else:
        assert m["unp_end"] - end_auth == off, (
            f"{pdb}: non-constant offset across the segment"
        )
    return off


def fetch_cif(pdb: str) -> str:
    url = f"https://www.ebi.ac.uk/pdbe/entry-files/download/{pdb}.cif"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        raw = fh.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", "replace")


def atoms(cif: str) -> list[dict]:
    """Minimal ATOM/HETATM parser for the mmCIF atom_site loop."""
    lines = cif.splitlines()
    cols: list[str] = []
    out: list[dict] = []
    in_loop = False
    for ln in lines:
        if ln.startswith("_atom_site."):
            cols.append(ln.strip().split(".", 1)[1])
            in_loop = True
            continue
        if in_loop and (ln.startswith("ATOM") or ln.startswith("HETATM")):
            f = ln.split()
            if len(f) < len(cols):
                continue
            out.append(dict(zip(cols, f)))
        elif in_loop and ln.startswith("#"):
            break
    assert out, "no atoms parsed - the mmCIF layout changed"
    assert {"Cartn_x", "label_comp_id", "label_atom_id"} <= set(cols), cols
    return out


def analyse(pdb: str) -> dict:
    ats = atoms(fetch_cif(pdb))
    # An NMR entry is a multi-model ensemble; without restricting to one model
    # every atom appears N times and the ZN count silently multiplies.
    models = {a.get("pdbx_PDB_model_num") for a in ats}
    if len(models) > 1:
        ats = [a for a in ats if a.get("pdbx_PDB_model_num") == "1"]
        assert ats, "model 1 not found"
    n_models = len(models)
    zn = [a for a in ats if a["label_comp_id"] == "ZN"]
    assert len(zn) == 1, f"{pdb}: expected 1 ZN, found {len(zn)}"
    z = zn[0]
    zx, zy, zz = (float(z[f"Cartn_{c}"]) for c in "xyz")
    shell = []
    for a in ats:
        if a["label_comp_id"] in ("ZN", "HOH"):
            continue
        x, y, w = (float(a[f"Cartn_{c}"]) for c in "xyz")
        d = math.dist((zx, zy, zz), (x, y, w))
        if d <= CUTOFF:
            shell.append(
                {
                    "residue": a["label_comp_id"],
                    "auth_seq_id": a.get("auth_seq_id"),
                    "chain": a.get("auth_asym_id"),
                    "atom": a["label_atom_id"],
                    "distance_A": round(d, 2),
                }
            )
    shell.sort(key=lambda s: s["distance_A"])
    return {
        "pdb": pdb,
        "n_models_in_entry": n_models,
        "model_analysed": 1,
        "cutoff_A": CUTOFF,
        "coordination_shell": shell,
    }


def main() -> None:
    seq = uniprot_sequence(SUBJECT)
    results = {}
    for pdb in ("2olm", "2d9l"):
        r = analyse(pdb)
        results[pdb] = r
        chains = {s["chain"] for s in r["coordination_shell"]}
        assert len(chains) == 1, f"{pdb}: shell spans chains {chains}"
        off = sifts_offset(pdb, chains.pop(), SUBJECT)
        r["auth_to_uniprot_offset"] = off
        auth_cys = sorted(
            {int(s["auth_seq_id"]) for s in r["coordination_shell"] if s["residue"] == "CYS"}
        )
        cys = [c + off for c in auth_cys]
        r["coordinating_cysteines_auth"] = auth_cys
        r["coordinating_cysteines_uniprot"] = cys
        print(f"\n{pdb.upper()}: zinc coordination shell within {CUTOFF} A "
              f"(auth->UniProt offset {off:+d}, {r['n_models_in_entry']} model(s))")
        for s in r["coordination_shell"]:
            print(
                f"   {s['residue']}{s['auth_seq_id']} (UniProt "
                f"{int(s['auth_seq_id']) + off}) {s['atom']} {s['distance_A']} A"
            )
        print(f"   coordinating cysteines, UniProt numbering: {cys}")
        for c in cys:
            assert seq[c - 1] == "C", (
                f"{pdb}: UniProt position {c} is {seq[c - 1]}, not C - the "
                "offset conversion is wrong"
            )
        assert cys == PREDICTED_CYS, (
            f"{pdb}: zinc is held by Cys{cys}, but the CX2CX16CX2CX4R scan "
            f"predicted Cys{PREDICTED_CYS} - one of the two is wrong"
        )
        print(f"   matches the motif prediction Cys{PREDICTED_CYS}: True")

    # The first committed version of this script wrote `{}` because the loop never
    # assigned `results[pdb]`, while every real number went only to stdout - a
    # silent degradation that no gate could see, since the RESULTS.md table it
    # feeds still validated as a byte-exact quote. Assert the payload before AND
    # after writing.
    assert set(results) == {"2olm", "2d9l"}, f"results has keys {sorted(results)}"
    for pdb, r in results.items():
        assert r["coordination_shell"], f"{pdb}: empty coordination shell"
        assert r["coordinating_cysteines_uniprot"] == PREDICTED_CYS, pdb
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    reread = json.loads(OUT.read_text())
    assert reread == results, "what was written back does not match what was computed"
    assert reread, "wrote an empty artifact"
    print(f"\nwrote {OUT} ({len(reread)} entries)")


if __name__ == "__main__":
    main()
