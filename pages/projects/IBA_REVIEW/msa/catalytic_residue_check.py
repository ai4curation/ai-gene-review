#!/usr/bin/env python3
"""
Generalized catalytic-residue check for pseudo-enzyme claims in IBA review.

Given a catalytic REFERENCE protein whose active-site / metal-ligand residues are
annotated in UniProt, align it with a set of family members and report what residue
each member carries at those positions -- in the member's own numbering.

This is the residue-level check IBA_REVIEW.md Pattern 7 calls the strongest single
signal that an enzymatic IBA is wrong. It is deliberately *reference-driven*: the
positions come from the live UniProt feature table, never from memory.

Usage:
    uv run python catalytic_residue_check.py CASE

where CASE is one of the cases registered in CASES below. Each case names catalytic
positive controls and known non-catalytic negative controls alongside the target, so
the readout can be interpreted: a target that patterns with the negative controls and
against the positive controls has lost the site.

    uv run python catalytic_residue_check.py rhomboid
    uv run python catalytic_residue_check.py pgrp
"""
import json
import sys
import urllib.request

from pyfamsa import Aligner, Sequence

# Each case: reference accession (positions come from its UniProt features),
# ordered members as (label, accession, role), and a feature-description filter.
CASES = {
    "rhomboid": {
        "title": "Rhomboid Ser-His catalytic dyad: active rhomboids vs UBAC2",
        "reference": ("GlpG_ecoli", "P09391"),
        "members": [
            ("GlpG_ecoli", "P09391", "catalytic (+)"),
            ("RHBDL2_hs", "Q9NX52", "catalytic (+)"),
            ("PARL_hs", "Q9H300", "catalytic (+)"),
            ("RHBDF1_hs", "Q6PJF5", "pseudoprotease (-)"),
            ("DERL1_hs", "Q9BUN8", "pseudoprotease (-)"),
            ("UBAC2_hs", "Q8NBM4", "TARGET"),
        ],
        "want_types": ("Active site",),
        "keywords": (),  # keep all active-site features
    },
    "pgrp": {
        "title": "PGRP amidase-2 Zn site: catalytic amidases vs recognition receptors",
        "reference": ("PGLYRP2_hs", "Q96PD5"),
        "members": [
            ("PGLYRP2_hs", "Q96PD5", "catalytic (+)"),
            ("PGRP-LB_dm", "Q8INK6", "catalytic (+)"),
            ("PGRP-SC1a_dm", "C0HK98", "catalytic (+)"),
            ("PGRP-LC_dm", "Q9GNK5", "receptor (-)"),
            ("PGRP-LE_dm", "Q9VXN9", "receptor (-)"),
            ("PGRPLC_ag", "A7UTA1", "TARGET"),
        ],
        "want_types": ("Binding site", "Active site"),
        "keywords": ("zn", "zinc", "metal", "active"),
    },
    "caspase": {
        "title": "Caspase His-Cys catalytic dyad: active caspases vs CASP12",
        "reference": ("CASP1_hs", "P29466"),
        "members": [
            ("CASP1_hs", "P29466", "catalytic (+)"),
            ("CASP3_hs", "P42574", "catalytic (+)"),
            ("CASP4_hs", "P49662", "catalytic (+)"),
            ("CASP12_hs", "Q6UXS9", "TARGET"),
        ],
        "want_types": ("Active site",),
        "keywords": (),
    },
    "calpain": {
        "title": "Calpain Cys-His-Asn catalytic triad: active calpains vs androglobin",
        "reference": ("CAPN1_hs", "P07384"),
        "members": [
            ("CAPN1_hs", "P07384", "catalytic (+)"),
            ("CAPN2_hs", "P17655", "catalytic (+)"),
            ("CAPN6_hs", "Q9Y6Q1", "pseudoprotease (-)"),
            ("ADGB_hs", "Q8N7X0", "TARGET"),
        ],
        "want_types": ("Active site",),
        "keywords": (),
    },
    "plasminogen": {
        "title": "Chymotrypsin charge-relay triad: plasminogen vs apolipoprotein(a)",
        "reference": ("PLG_hs", "P00747"),
        "members": [
            ("PLG_hs", "P00747", "catalytic (+)"),
            ("PLAT_hs", "P00750", "catalytic (+)"),
            ("LPA_hs", "P08519", "TARGET"),
        ],
        "want_types": ("Active site",),
        "keywords": (),
    },
    "adprh": {
        "title": "ADP-ribosylarginine hydrolase Mg site: ADPRH/ADPRS vs ADPRHL1",
        "reference": ("ADPRH_hs", "P54922"),
        "members": [
            ("ADPRH_hs", "P54922", "catalytic (+)"),
            ("ADPRS_hs", "Q9NX46", "catalytic (+)"),
            ("ADPRHL1_hs", "Q8NDY3", "TARGET"),
        ],
        "want_types": ("Binding site",),
        "keywords": ("mg", "magnesium", "metal"),
    },
    "e2": {
        "title": "E2 ubiquitin-conjugating catalytic Cys: active E2s vs AKTIP",
        "reference": ("UBE2N_hs", "P61088"),
        "members": [
            ("UBE2N_hs", "P61088", "catalytic (+)"),
            ("UBE2D1_hs", "P51668", "catalytic (+)"),
            ("UBE2V1_hs", "Q13404", "UEV, non-catalytic (-)"),
            ("AKTIP_hs", "Q9H8T0", "TARGET"),
        ],
        "want_types": ("Active site",),
        "keywords": (),
    },
    "odc": {
        "title": "Ornithine decarboxylase site: ODC1 vs the antizyme inhibitors",
        "reference": ("ODC1_hs", "P11926"),
        "members": [
            ("ODC1_hs", "P11926", "catalytic (+)"),
            ("AZIN2_hs", "Q96A70", "antizyme inhibitor (-)"),
            ("AZIN1_hs", "O14977", "TARGET"),
        ],
        "want_types": ("Active site", "Binding site"),
        "keywords": (),
    },
    "sephs": {
        "title": "Selenophosphate synthetase site: SelD/SEPHS2 vs SEPHS1",
        "reference": ("SelD_ecoli", "P16456"),
        "members": [
            ("SelD_ecoli", "P16456", "catalytic (+)"),
            ("SEPHS2_hs", "Q99611", "catalytic (+)"),
            ("SEPHS1_hs", "P49903", "TARGET"),
        ],
        "want_types": ("Active site", "Binding site"),
        "keywords": (),
    },
    "gatase": {
        "title": "Class-I glutamine amidotransferase triad: CarA/CAD vs CPS1",
        "reference": ("CarA_ecoli", "P0A6F1"),
        "members": [
            ("CarA_ecoli", "P0A6F1", "catalytic (+)"),
            ("CAD_hs", "P27708", "catalytic (+)"),
            ("CPS1_hs", "P31327", "TARGET"),
        ],
        "want_types": ("Active site",),
        "keywords": (),
    },
    "mapk": {
        "title": "MAP-kinase catalytic machinery: Fus3/Slt2 vs the pseudokinase Kdx1",
        "reference": ("FUS3_sc", "P16892"),
        "members": [
            ("FUS3_sc", "P16892", "catalytic (+)"),
            ("SLT2_sc", "Q00772", "catalytic (+)"),
            ("KDX1_sc", "P36005", "TARGET"),
        ],
        "want_types": ("Active site", "Binding site"),
        "keywords": (),
    },
    "hsp70": {
        "title": "Hsp70 nucleotide-binding site: HSPA8/Ssa1 vs Ssz1 and HSPA13",
        "reference": ("HSPA8_hs", "P11142"),
        "members": [
            ("HSPA8_hs", "P11142", "catalytic (+)"),
            ("SSA1_sc", "P10591", "catalytic (+)"),
            ("SSZ1_sc", "P38788", "TARGET"),
            ("HSPA13_hs", "P48723", "TARGET"),
        ],
        "want_types": ("Binding site",),
        "keywords": (),
    },
    "argonaute_worm": {
        "title": "Argonaute slicer tetrad: AGO2 vs AGO4 and C. elegans wago-4",
        "reference": ("AGO2_hs", "Q9UKV8"),
        "members": [
            ("AGO2_hs", "Q9UKV8", "slicer (+)"),
            ("AGO4_hs", "Q9HCK5", "non-slicer (-)"),
            ("WAGO4_ce", "O62275", "TARGET"),
        ],
        "want_types": ("Binding site",),
        "keywords": ("metal", "mg", "mn", "cation"),
    },
    "jmjc": {
        "title": "JmjC Fe(II)/2-OG site: KDM2A/KDM2B (the actual IBA donors) vs Epe1",
        "reference": ("KDM2A_hs", "Q9Y2K7"),
        "members": [
            ("KDM2A_hs", "Q9Y2K7", "catalytic (+)"),
            ("KDM2B_hs", "Q8NHM5", "catalytic (+)"),
            ("Epe1_sp", "O94603", "TARGET"),
        ],
        "want_types": ("Binding site",),
        "keywords": ("fe", "2-oxoglutarate", "substrate"),
    },
    "chitinase": {
        "title": "GH18 chitinase catalytic Glu: CHIT1/CHIA vs chi-lectin and pombe cts2",
        "reference": ("CHIT1_hs", "Q13231"),
        "members": [
            ("CHIT1_hs", "Q13231", "catalytic (+)"),
            ("CHIA_hs", "Q9BZP6", "catalytic (+)"),
            ("CHI3L1_hs", "P36222", "chi-lectin, inactive (-)"),
            ("cts2_sp", "Q9C105", "TARGET"),
        ],
        "want_types": ("Active site", "Binding site"),
        "keywords": (),
    },
    "photolyase": {
        "title": "Photolyase FAD/DNA-lesion site: E. coli PhrB vs the cryptochromes",
        "reference": ("PhrB_ecoli", "P00914"),
        "members": [
            ("PhrB_ecoli", "P00914", "photolyase (+)"),
            ("CRY1_hs", "Q16526", "cryptochrome (-)"),
            ("CRY1_at", "Q43125", "TARGET"),
        ],
        "want_types": ("Binding site",),
        "keywords": (),
    },
}


def uniprot_json(acc):
    return json.load(urllib.request.urlopen(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=30))


# FAMSA accepts only the 20 standard residues. Selenocysteine and pyrrolysine are
# mapped to their closest standard counterpart purely so the column can be aligned;
# the substitution is reported so it is never mistaken for the real residue.
NONSTANDARD = {"U": "C", "O": "K"}


def uniprot_seq_and_name(acc):
    d = uniprot_json(acc)
    name = (d.get("proteinDescription", {}).get("recommendedName", {})
             .get("fullName", {}).get("value", ""))
    return d["sequence"]["value"], name


def sanitize(seq):
    """Return (aligner-safe sequence, [(1-based pos, original aa)])."""
    swaps = [(i + 1, c) for i, c in enumerate(seq) if c in NONSTANDARD]
    for orig, repl in NONSTANDARD.items():
        seq = seq.replace(orig, repl)
    return seq, swaps


def feature_positions(acc, want_types, keywords):
    """{1-based position: description} for single-residue features of the wanted types.

    Several features can sit on the same residue (e.g. ODC1 Cys360 is both the
    catalytic Active site and a putrescine Binding site); their descriptions are
    merged rather than one silently overwriting the other.
    """
    out = {}
    for f in uniprot_json(acc).get("features", []):
        if f["type"] not in want_types:
            continue
        loc = f["location"]
        if loc["start"]["value"] != loc["end"]["value"]:
            continue
        desc = f.get("description", "") or f["type"]
        lig = (f.get("ligand") or {}).get("name", "")
        full = (desc + (f" [{lig}]" if lig else "")).strip()
        if keywords and not any(k in full.lower() for k in keywords):
            continue
        pos = loc["start"]["value"]
        tag = "ACT" if f["type"] == "Active site" else "bind"
        entry = f"{tag}:{full}"
        out[pos] = f"{out[pos]} + {entry}" if pos in out else entry
    return out


def align(named_seqs):
    msa = Aligner(guide_tree="upgma").align(
        [Sequence(n.encode(), s.encode()) for n, s in named_seqs])
    return {s.id.decode(): s.sequence.decode() for s in msa}


def col_for_refpos(aln, refname, refpos):
    idx = 0
    for col, ch in enumerate(aln[refname]):
        if ch != "-":
            idx += 1
            if idx == refpos:
                return col
    return None


def run(case_name):
    case = CASES[case_name]
    refname, refacc = case["reference"]
    print(f"# {case['title']}\n")

    named, roles, raw = [], {}, {}
    for label, acc, role in case["members"]:
        seq, name = uniprot_seq_and_name(acc)
        raw[label] = seq
        safe, swaps = sanitize(seq)
        named.append((label, safe))
        roles[label] = role
        note = ""
        if swaps:
            note = ("  [non-standard residues mapped for alignment: "
                    + ", ".join(f"{aa}{p}->{NONSTANDARD[aa]}" for p, aa in swaps) + "]")
        print(f"  {label:<14} {acc:<8} {role:<22} {name[:46]}{note}")

    aln = align(named)
    positions = feature_positions(refacc, case["want_types"], case["keywords"])
    if not positions:
        print(f"\nNo matching single-residue features on reference {refacc}; "
              "cannot run this check. Not falling back to guessed positions.")
        return

    labels = [m[0] for m in case["members"]]
    print(f"\nReference: {refname} ({refacc}); positions from the live UniProt "
          "feature table.")
    print("Cells give residue@position in each protein's own numbering. "
          "'gap' = the protein has no residue aligned to that column, which means the "
          "site is absent or the local region is unalignable -- weaker evidence than a "
          "substitution, so flanking context is printed below for any gapped row.\n")
    header = f"{'reference residue / role':<42} " + " ".join(f"{l:<15}" for l in labels)
    print(header)
    print("-" * len(header))
    gapped = []
    for pos in sorted(positions):
        col = col_for_refpos(aln, refname, pos)
        if col is None:
            continue
        cells = []
        for l in labels:
            aa = aln[l][col]
            if aa == "-":
                cells.append("gap")
                gapped.append((pos, l, col))
            else:
                native = len(aln[l][:col + 1].replace("-", ""))
                # report the TRUE residue, not the alignment-safe substitution
                cells.append(f"{raw[l][native - 1]}{native}")
        label = f"{aln[refname][col]}{pos} {positions[pos][:32]}"
        print(f"{label:<42} " + " ".join(f"{c:<15}" for c in cells))

    if gapped:
        print("\nFlanking context for gapped positions "
              "(alignment columns +/-12 around the site):")
        for pos, l, col in gapped:
            lo, hi = max(0, col - 12), col + 13
            print(f"  {refname} {pos}: {aln[refname][lo:hi]}")
            print(f"  {l:<{len(refname)}} {'':>{len(str(pos))}}  {aln[l][lo:hi]}")

    print("\nRead it as a contrast, not a single row: a TARGET that matches the "
          "catalytic (+) controls retains the site; one that patterns with the (-) "
          "controls has lost it.")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CASES:
        print(f"Usage: catalytic_residue_check.py [{'|'.join(CASES)}]")
        sys.exit(1)
    run(sys.argv[1])
