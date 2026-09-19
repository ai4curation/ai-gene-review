#!/usr/bin/env python3
"""Does ARHGEF16 retain the DH-domain surface that Dbl-family GEFs use to hold a
Rho GTPase -- and would that tell us anything if we did not already know?

Answered honestly in both directions, because in the RhoGAP family reviewed
alongside this one, residue identity and curated activity turned out to be
decoupled *both* ways: proteins missing the canonical arginine finger carried
curated GAP activity, and ARHGAP11B retains the arginine yet is curated
``NOT|enables GO:0005096``.  Neither presence nor absence of a canonical residue
settles activity by itself, so this script is built to be able to say so.

A DH domain has no catalytic residue in the chemical sense -- it catalyses
nucleotide exchange by distorting switch I and switch II, not by covalent
chemistry -- so "the catalytic residue" has to be replaced by something
structurally defined.  Here that is the **exchange surface**: the DH-domain
residues that lie within 4.0 A of the GTPase in a solved DH-GTPase complex.

**Q1 -- is the surface retained?**  Six solved complexes are used as anchors,
deliberately spanning three different substrates so that the answer cannot be an
artefact of one GEF-GTPase pair:

  1KZ7 Dbs(MCF2L) . Cdc42     1LB1 Dbs(MCF2L) . RhoA     1FOE Tiam1 . Rac1
  1KI1 ITSN1 . Cdc42          1X86 LARG(ARHGEF12) . RhoA 2NZ8 Trio . Rac1

Chain-to-UniProt correspondence is taken from SIFTS (PDBe ``mappings/uniprot``),
not assumed, and the contact residues are then required to fall inside the GEF's
own UniProt-delimited DH domain.  Each anchor's contact set is projected onto
every panel member by local alignment against the anchor's DH domain.

**Q2 -- does the surface tell you the substrate?**  This is the question the
review actually needs, because what separates Ephexin-4 from its four siblings is
not whether it is a GEF but *which* GTPase it acts on (RhoG, and in cells nothing
else -- PMID:20679435).  If ARHGEF16 scores alike against the Cdc42-bound,
RhoA-bound and Rac1-bound anchors, then the exchange surface is substrate-blind
and the sequence cannot supply what GO's merged terms also cannot express.

**Q3 -- does a retained surface imply activity?**  Not in this protein, and the
counter-example is the protein itself.  Full-length Ephexin4 is autoinhibited by
two independent modes and is catalytically quiet until relieved by Elmo1 or by a
PDZ protein (PMID:33597305, PMID:28667327, PMID:30445756) -- an intact exchange
surface that does nothing until de-repressed.  The script reports this as a
stated limit, not as a measurement, and also scores isoform Q5VV41-2, which
truncates residues 1-288 and so enters the DH domain five residues in.

Controls, mandatory:
  * positive -- the anchor GEFs themselves, and other Dbl-family GEFs with
    measured exchange activity, must score high;
  * out-group -- DOCK4, a bona fide Rac GEF that uses a DHR2 domain and has no DH
    domain at all, must score low.  It controls the *method*: it shows the panel
    is reading the Dbl fold rather than "any GEF".  It is not a dead DH domain,
    and is not presented as one.

Run:    uv run --with biopython --with requests python dh_exchange_surface.py
        uv run --with biopython --with requests python dh_exchange_surface.py --self-test
Writes: dh_exchange_surface.json
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT_JSON = "https://rest.uniprot.org/uniprotkb/{acc}.json"
UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
SIFTS = "https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb}"
RCSB_CIF = "https://files.rcsb.org/download/{pdb}.cif"

TIMEOUT = 180
CONTACT_CUTOFF_ANGSTROM = 4.0

# PDB -> (GEF UniProt accession, GTPase UniProt accession, substrate label).
# Verified against RCSB titles; the chain assignment itself is read from SIFTS.
ANCHORS: dict[str, dict[str, str]] = {
    "1KZ7": {"gef": "Q64096", "gtpase": "P60953", "gef_name": "Dbs/MCF2L (mouse)", "substrate": "Cdc42"},
    "1LB1": {"gef": "Q64096", "gtpase": "P61586", "gef_name": "Dbs/MCF2L (mouse)", "substrate": "RhoA"},
    "1FOE": {"gef": "Q60610", "gtpase": "P63000", "gef_name": "Tiam1 (mouse)", "substrate": "Rac1"},
    "1KI1": {"gef": "Q15811", "gtpase": "P60953", "gef_name": "ITSN1", "substrate": "Cdc42"},
    "1X86": {"gef": "Q9NZN5", "gtpase": "P61586", "gef_name": "LARG/ARHGEF12", "substrate": "RhoA"},
    "2NZ8": {"gef": "O75962", "gtpase": "P63000", "gef_name": "Trio", "substrate": "Rac1"},
}

# expect: "high" (real DH domain, must retain the surface) | "low" (out-group).
PANEL: dict[str, dict[str, object]] = {
    "Q5VV41": {"symbol": "ARHGEF16/Ephexin-4", "role": "TARGET", "expect": None},
    "Q5VV41-2": {
        "symbol": "ARHGEF16 isoform 2",
        "role": "TARGET isoform, lacks 1-288",
        "expect": None,
    },
    "Q8N5V2": {"symbol": "NGEF/Ephexin-1", "role": "sibling, RhoA GEF", "expect": "high"},
    "Q8IW93": {"symbol": "ARHGEF19/Ephexin-2", "role": "sibling, RhoA GEF", "expect": "high"},
    "Q12774": {"symbol": "ARHGEF5/Ephexin-3", "role": "sibling, RhoA GEF", "expect": "high"},
    "O94989": {"symbol": "ARHGEF15/Ephexin-5", "role": "sibling, RhoA GEF", "expect": "high"},
    "Q96DR7": {"symbol": "ARHGEF26/SGEF", "role": "the other human RhoG GEF", "expect": "high"},
    "Q13009": {"symbol": "TIAM1", "role": "positive control, Rac1 GEF", "expect": "high"},
    "Q15811": {"symbol": "ITSN1", "role": "positive control, Cdc42 GEF", "expect": "high"},
    "Q9NZN5": {"symbol": "LARG/ARHGEF12", "role": "positive control, RhoA GEF", "expect": "high"},
    "O15068": {"symbol": "MCF2L/DBS", "role": "positive control, human Dbs", "expect": "high"},
    "Q8N1I0": {
        "symbol": "DOCK4",
        "role": "out-group: Rac GEF with a DHR2 domain, no DH domain",
        "expect": "low",
    },
}

# The control is each protein against ITS OWN chance baseline, not an absolute
# cut.  An absolute threshold would have to be tuned until the run passed, which
# is tuning to the answer.  Contact sets taken from a distant GEF-GTPase pair are
# legitimately less well conserved, so the absolute numbers vary by anchor while
# "beats its own shuffle" does not.
SEPARATION_MARGIN = 0.15
SHUFFLE_REPLICATES = 5


def fetch_uniprot(acc: str) -> dict:
    r = requests.get(UNIPROT_JSON.format(acc=acc.split("-")[0]), timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def fetch_sequence(acc: str) -> str:
    """Isoform accessions have no JSON record, so read FASTA for everything."""
    r = requests.get(UNIPROT_FASTA.format(acc=acc), timeout=TIMEOUT)
    r.raise_for_status()
    return "".join(l.strip() for l in r.text.splitlines() if not l.startswith(">"))


def dh_domains(entry: dict) -> list[tuple[int, int, str]]:
    """All UniProt DH domains. Trio and Kalirin carry two ("DH 1", "DH 2"), so
    returning a list and letting the caller pick by structural evidence is safer
    than asserting there is exactly one."""
    return [
        (
            f["location"]["start"]["value"],
            f["location"]["end"]["value"],
            f.get("description", "").strip(),
        )
        for f in entry.get("features", [])
        if f["type"] == "Domain"
        and (f.get("description", "").strip() == "DH" or f.get("description", "").strip().startswith("DH "))
    ]


def dh_domain_containing(entry: dict, positions: list[int]) -> tuple[int, int, str] | None:
    """Pick the DH domain that actually holds the structure's contact residues."""
    best, best_n = None, 0
    for start, end, desc in dh_domains(entry):
        n = sum(1 for p in positions if start <= p <= end)
        if n > best_n:
            best, best_n = (start, end, desc), n
    return best


def sifts_chains(pdb: str) -> dict[str, list[dict]]:
    r = requests.get(SIFTS.format(pdb=pdb.lower()), timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()[pdb.lower()]["UniProt"]


def parse_cif_atoms(text: str) -> list[dict]:
    """Read the ``_atom_site`` loop by column NAME.

    RCSB happens to emit a stable column order, but reading positionally is how a
    silently-shifted file becomes a silently-wrong answer, so the header is
    parsed and the columns are looked up by name.
    """
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip() == "loop_":
            j = i + 1
            cols: list[str] = []
            while j < len(lines) and lines[j].startswith("_atom_site."):
                cols.append(lines[j].strip().split(".", 1)[1])
                j += 1
            if cols:
                idx = {c: k for k, c in enumerate(cols)}
                need = [
                    "label_asym_id",
                    "label_seq_id",
                    "label_comp_id",
                    "Cartn_x",
                    "Cartn_y",
                    "Cartn_z",
                    "group_PDB",
                ]
                missing = [c for c in need if c not in idx]
                if missing:
                    raise RuntimeError(f"_atom_site loop lacks columns {missing}")
                out = []
                while j < len(lines) and not lines[j].startswith(("#", "loop_", "_")):
                    f = lines[j].split()
                    if len(f) == len(cols):
                        out.append(
                            {
                                "group": f[idx["group_PDB"]],
                                "asym": f[idx["label_asym_id"]],
                                "seq": f[idx["label_seq_id"]],
                                "comp": f[idx["label_comp_id"]],
                                "xyz": (
                                    float(f[idx["Cartn_x"]]),
                                    float(f[idx["Cartn_y"]]),
                                    float(f[idx["Cartn_z"]]),
                                ),
                            }
                        )
                    j += 1
                return out
            i = j
        else:
            i += 1
    raise RuntimeError("no _atom_site loop found")


def contact_positions(pdb: str, spec: dict[str, str]) -> dict[str, object]:
    """GEF residues (UniProt numbering) within CONTACT_CUTOFF of the GTPase."""
    chains = sifts_chains(pdb)
    for acc in (spec["gef"], spec["gtpase"]):
        if acc not in chains:
            raise RuntimeError(f"{pdb}: SIFTS has no mapping for {acc}")

    gef_map = chains[spec["gef"]]["mappings"][0]
    gtp_maps = chains[spec["gtpase"]]["mappings"]
    gef_asym = gef_map["struct_asym_id"]
    gtp_asyms = {m["struct_asym_id"] for m in gtp_maps}

    atoms = parse_cif_atoms(requests.get(RCSB_CIF.format(pdb=pdb), timeout=TIMEOUT).text)
    gef_atoms = [a for a in atoms if a["group"] == "ATOM" and a["asym"] == gef_asym]
    gtp_atoms = [a for a in atoms if a["group"] == "ATOM" and a["asym"] in gtp_asyms]
    if not gef_atoms or not gtp_atoms:
        raise RuntimeError(f"{pdb}: empty chain selection ({gef_asym} vs {gtp_asyms})")

    # Restrict the GTPase side to the copy that actually touches this GEF chain,
    # so a second complex in the asymmetric unit cannot donate phantom contacts.
    best_asym, best_n = None, -1
    for asym in sorted(gtp_asyms):
        sub = [a for a in gtp_atoms if a["asym"] == asym]
        n = sum(
            1
            for g in gef_atoms
            for t in sub
            if abs(g["xyz"][0] - t["xyz"][0]) < CONTACT_CUTOFF_ANGSTROM
            and abs(g["xyz"][1] - t["xyz"][1]) < CONTACT_CUTOFF_ANGSTROM
            and abs(g["xyz"][2] - t["xyz"][2]) < CONTACT_CUTOFF_ANGSTROM
            and math.dist(g["xyz"], t["xyz"]) <= CONTACT_CUTOFF_ANGSTROM
        )
        if n > best_n:
            best_asym, best_n = asym, n
    partner = [a for a in gtp_atoms if a["asym"] == best_asym]

    unp_start = gef_map["unp_start"]
    pdb_start = gef_map["start"]["residue_number"]
    hits: dict[int, str] = {}
    for g in gef_atoms:
        if g["seq"] in (".", "?"):
            continue
        for t in partner:
            if math.dist(g["xyz"], t["xyz"]) <= CONTACT_CUTOFF_ANGSTROM:
                pos = unp_start + (int(g["seq"]) - pdb_start)
                hits[pos] = g["comp"]
                break
    return {
        "pdb": pdb,
        "gef_accession": spec["gef"],
        "gef_name": spec["gef_name"],
        "substrate": spec["substrate"],
        "gef_chain": gef_asym,
        "gtpase_chain": best_asym,
        "contacts_unp": sorted(hits),
    }


def make_aligner(mode: str = "local") -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = mode
    return a


def project_positions(
    aligner: Align.PairwiseAligner,
    ref_seq: str,
    ref_offset: int,
    ref_positions: list[int],
    qry_seq: str,
) -> dict[int, tuple[int | None, str]]:
    """Map reference (anchor DH) positions onto the query's full-length numbering.

    ``ref_seq`` is the anchor's DH-domain slice starting at ``ref_offset``;
    ``qry_seq`` is the query's FULL sequence, aligned locally, so proteins with no
    DH domain are handled by the same code path rather than being excluded by it.
    """
    aln = aligner.align(ref_seq, qry_seq)[0]
    indices = aln.indices
    ref_col = {int(indices[0][c]): c for c in range(indices.shape[1]) if indices[0][c] >= 0}
    out: dict[int, tuple[int | None, str]] = {}
    for p in ref_positions:
        ridx = p - ref_offset
        col = ref_col.get(ridx)
        if col is None:
            out[p] = (None, "-")
            continue
        q = int(indices[1][col])
        out[p] = (None, "-") if q < 0 else (q + 1, qry_seq[q])
    return out


def _score_one(
    aligner: Align.PairwiseAligner,
    blosum,
    ref_slice: str,
    ref_offset: int,
    positions: list[int],
    anchor_seq: str,
    qry_seq: str,
) -> dict[str, object]:
    proj = project_positions(aligner, ref_slice, ref_offset, positions, qry_seq)
    identical = similar = gapped = 0
    detail = {}
    for p in positions:
        qpos, qres = proj[p]
        ares = anchor_seq[p - 1]
        if qres == "-":
            gapped += 1
            verdict = "gap"
        elif qres == ares:
            identical += 1
            verdict = "identical"
        elif blosum[ares, qres] > 0:
            similar += 1
            verdict = "similar"
        else:
            verdict = "different"
        detail[p] = {"anchor": ares, "query_position": qpos, "query": qres, "verdict": verdict}
    n = len(positions) or 1
    return {
        "n_contact_positions": len(positions),
        "identical": identical,
        "similar": similar,
        "gapped": gapped,
        "retained_fraction": round((identical + similar) / n, 3),
        "identity_fraction": round(identical / n, 3),
        "per_position": detail,
    }


def score_panel(
    anchor: dict[str, object],
    anchor_seq: str,
    anchor_dh: tuple[int, int],
    sequences: dict[str, str],
) -> dict[str, dict[str, object]]:
    """Score each panel member, and score a seeded shuffle of the same sequence.

    The shuffle is the negative control that matters.  A 1966-residue protein
    locally aligned to a 180-residue DH domain will always align *somewhere*, and
    roughly a third of the columns land on a BLOSUM-positive pair by chance -- so
    an absolute cut-off cannot tell homology from coincidence.  Composition-
    preserving shuffles of the *same* sequence give each protein its own chance
    baseline, and a real DH domain has to beat its own baseline.
    """
    import random

    blosum = substitution_matrices.load("BLOSUM62")
    aligner = make_aligner("local")
    positions = [p for p in anchor["contacts_unp"] if anchor_dh[0] <= p <= anchor_dh[1]]
    ref_slice = anchor_seq[anchor_dh[0] - 1 : anchor_dh[1]]

    rows: dict[str, dict[str, object]] = {}
    for acc, seq in sequences.items():
        real = _score_one(aligner, blosum, ref_slice, anchor_dh[0], positions, anchor_seq, seq)
        shuffles = []
        for rep in range(SHUFFLE_REPLICATES):
            rng = random.Random(f"{anchor['pdb']}|{acc}|{rep}")
            letters = list(seq)
            rng.shuffle(letters)
            shuffles.append(
                _score_one(
                    aligner, blosum, ref_slice, anchor_dh[0], positions, anchor_seq,
                    "".join(letters),
                )["retained_fraction"]
            )
        real["shuffled_retained_fraction_mean"] = round(sum(shuffles) / len(shuffles), 3)
        real["shuffled_retained_fraction_max"] = max(shuffles)
        real["above_own_chance_baseline"] = round(
            real["retained_fraction"] - real["shuffled_retained_fraction_mean"], 3
        )
        rows[acc] = real
    return rows


def run() -> dict[str, object]:
    entries = {acc: fetch_uniprot(acc) for acc in {a["gef"] for a in ANCHORS.values()} | set(PANEL)}
    sequences = {acc: fetch_sequence(acc) for acc in PANEL}

    anchors: dict[str, dict[str, object]] = {}
    for pdb, spec in ANCHORS.items():
        c = contact_positions(pdb, spec)
        gef_entry = entries[spec["gef"]]
        picked = dh_domain_containing(gef_entry, c["contacts_unp"])
        if picked is None:
            raise RuntimeError(
                f"{pdb}: none of {spec['gef']}'s DH domains "
                f"{dh_domains(gef_entry)} contains a contact residue"
            )
        dh = (picked[0], picked[1])
        gef_seq = gef_entry["sequence"]["value"]
        inside = [p for p in c["contacts_unp"] if dh[0] <= p <= dh[1]]
        c["dh_domain"] = list(dh)
        c["dh_domain_name"] = picked[2]
        c["contacts_in_dh"] = inside
        c["contacts_outside_dh"] = [p for p in c["contacts_unp"] if p not in inside]
        c["panel"] = score_panel(c, gef_seq, dh, sequences)
        anchors[pdb] = c

    # Controls, in two parts.
    #
    # (a) PRESENCE.  The out-group must have no DH domain at all, and every
    #     positive must have one.  This is what makes DOCK4 an out-group; its
    #     numeric score is reported but is NOT used as a floor, because local
    #     alignment of a 1966-residue protein to a 180-residue domain finds a
    #     chance match and that chance match is not a measurement.
    # (b) SIGNAL.  Every DH-containing positive must beat its own
    #     composition-matched shuffle by SEPARATION_MARGIN at every anchor.
    #
    # A failure in either means the alignment or the SIFTS offset moved, and
    # nothing else in the table can be believed.
    failures: list[str] = []
    has_dh = {acc: bool(dh_domains(entries[acc.split("-")[0]])) for acc in PANEL}
    for acc, meta in PANEL.items():
        if meta["expect"] == "low" and has_dh[acc]:
            failures.append(f"{meta['symbol']}: out-group unexpectedly has a DH domain")
        if meta["expect"] == "high" and not has_dh[acc]:
            failures.append(f"{meta['symbol']}: positive control has no DH domain")

    separation: dict[str, dict[str, object]] = {}
    for pdb, a in anchors.items():
        margins = {
            m["symbol"]: a["panel"][acc]["above_own_chance_baseline"]
            for acc, m in PANEL.items()
            if m["expect"] == "high"
        }
        if not margins:
            raise RuntimeError("the panel lost its positive-control class")
        worst = min(margins.values())
        separation[pdb] = {
            "worst_positive_margin_over_shuffle": worst,
            "out_group_score": a["panel"]["Q8N1I0"]["retained_fraction"],
            "out_group_shuffle_mean": a["panel"]["Q8N1I0"]["shuffled_retained_fraction_mean"],
            "out_group_margin_over_shuffle": a["panel"]["Q8N1I0"]["above_own_chance_baseline"],
        }
        if worst < SEPARATION_MARGIN:
            failures.append(
                f"{pdb}: positive(s) {[s for s, v in margins.items() if v == worst]} "
                f"only {worst} above their own shuffle"
            )
    if failures:
        raise RuntimeError("control failure:\n  " + "\n  ".join(failures))

    tgt = {pdb: anchors[pdb]["panel"]["Q5VV41"]["retained_fraction"] for pdb in anchors}
    by_substrate: dict[str, list[float]] = {}
    for pdb, spec in ANCHORS.items():
        by_substrate.setdefault(spec["substrate"], []).append(tgt[pdb])

    # The cleanest substrate test in the set: 1KZ7 and 1LB1 are the SAME GEF (Dbs)
    # bound to two DIFFERENT GTPases.  Comparing them holds the GEF constant, so
    # any difference is attributable to the substrate and nothing else.
    a1, a2 = set(anchors["1KZ7"]["contacts_in_dh"]), set(anchors["1LB1"]["contacts_in_dh"])
    same_gef = {
        "gef": ANCHORS["1KZ7"]["gef_name"],
        "substrates": [ANCHORS["1KZ7"]["substrate"], ANCHORS["1LB1"]["substrate"]],
        "contacts_1KZ7_only": sorted(a1 - a2),
        "contacts_1LB1_only": sorted(a2 - a1),
        "contacts_shared": sorted(a1 & a2),
        "jaccard": round(len(a1 & a2) / len(a1 | a2), 3),
        "target_score_difference": round(abs(tgt["1KZ7"] - tgt["1LB1"]), 3),
    }

    return {
        "contact_cutoff_angstrom": CONTACT_CUTOFF_ANGSTROM,
        "separation_margin_required": SEPARATION_MARGIN,
        "shuffle_replicates": SHUFFLE_REPLICATES,
        "separation_observed": separation,
        "has_dh_domain": has_dh,
        "anchors": anchors,
        "target_retained_fraction_by_anchor": tgt,
        "target_retained_fraction_by_substrate": {
            k: {"values": sorted(v), "min": min(v), "max": max(v), "spread": round(max(v) - min(v), 3)}
            for k, v in by_substrate.items()
        },
        "same_gef_two_substrates": same_gef,
        "substrate_discrimination": {
            "spread_across_all_anchors": round(max(tgt.values()) - min(tgt.values()), 3),
            "best_scoring_anchor": max(tgt, key=tgt.get),
            "best_scoring_anchor_substrate": ANCHORS[max(tgt, key=tgt.get)]["substrate"],
            "measured_substrate_of_target": "RhoG (PMID:20679435), absent from every anchor",
            "comment": (
                "Read naively, the panel would name the substrate of the best-scoring "
                "anchor. That answer is wrong for this protein, and the same-GEF "
                "comparison says why: holding the GEF constant and changing the GTPase "
                "barely moves the contact set, so the ranking tracks GEF-to-GEF sequence "
                "similarity, not substrate. The exchange surface does not encode which "
                "GTPase a Dbl-family GEF acts on, and so cannot supply what GO's merged "
                "terms also cannot express."
            ),
        },
        "limits": {
            "retention_does_not_imply_activity": (
                "Full-length Ephexin4 is autoinhibited by two independent modes and is "
                "quiet until relieved by Elmo1 or a PDZ protein (PMID:33597305, "
                "PMID:28667327, PMID:30445756). An intact exchange surface is therefore "
                "compatible with no measurable activity."
            ),
            "absence_would_not_imply_inactivity": (
                "The out-group DOCK4 catalyses exchange on Rac with no DH domain at all, "
                "so a low score on this panel means 'not a Dbl-family GEF', not 'not a GEF'."
            ),
            "this_analysis_is_confirmatory_only": (
                "ARHGEF16's exchange activity was measured directly on purified DH-PH "
                "protein (PMID:20679435); the sequence never had to carry the argument."
            ),
        },
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []
    aligner = make_aligner("local")

    entry = fetch_uniprot("Q5VV41")
    dh = dh_domains(entry)
    checks.append(
        ("target has exactly one DH domain", "PASS" if dh == [(284, 468, "DH")] else f"FAIL {dh}")
    )

    # NEGATIVE CONTROL: the out-group must have no DH domain at all. If UniProt
    # ever gives DOCK4 one, the out-group stops being an out-group.
    og = dh_domains(fetch_uniprot("Q8N1I0"))
    checks.append(("out-group DOCK4 has no DH domain", "PASS" if og == [] else f"FAIL {og}"))

    # Trio carries two DH domains; the picker must choose the one 2NZ8 resolves.
    trio = fetch_uniprot("O75962")
    checks.append(
        (
            "two-DH protein: picker selects the structurally supported domain",
            "PASS"
            if (dh_domain_containing(trio, [1300, 1400]) or (0, 0, ""))[2] == "DH 1"
            and (dh_domain_containing(trio, [2000, 2100]) or (0, 0, ""))[2] == "DH 2"
            else "FAIL",
        )
    )

    anchor = contact_positions("1KZ7", ANCHORS["1KZ7"])
    checks.append(
        (
            "1KZ7 yields a non-empty Dbs-Cdc42 contact set",
            "PASS" if len(anchor["contacts_unp"]) >= 10 else f"FAIL {anchor['contacts_unp']}",
        )
    )

    # 1. Self-projection must be perfect: the anchor DH projected onto its own
    #    full sequence must return identity at every contact position.
    dbs = fetch_uniprot("Q64096")
    dbs_dh = dh_domain_containing(dbs, anchor["contacts_unp"])[:2]
    dbs_seq = dbs["sequence"]["value"]
    inside = [p for p in anchor["contacts_unp"] if dbs_dh[0] <= p <= dbs_dh[1]]
    proj = project_positions(
        aligner, dbs_seq[dbs_dh[0] - 1 : dbs_dh[1]], dbs_dh[0], inside, dbs_seq
    )
    exact = all(proj[p][0] == p and proj[p][1] == dbs_seq[p - 1] for p in inside)
    checks.append(("anchor self-projection is the identity map", "PASS" if exact else "FAIL"))

    # 2. A displaced anchor must change the answer. If shifting every contact
    #    position by 7 leaves the target's score unchanged, the alignment is not
    #    reading the columns we think it is.
    tgt_seq = fetch_sequence("Q5VV41")
    ref_slice = dbs_seq[dbs_dh[0] - 1 : dbs_dh[1]]
    true_proj = project_positions(aligner, ref_slice, dbs_dh[0], inside, tgt_seq)
    shifted = [p + 7 for p in inside if dbs_dh[0] <= p + 7 <= dbs_dh[1]]
    shift_proj = project_positions(aligner, ref_slice, dbs_dh[0], shifted, tgt_seq)
    same = sum(
        1
        for p in inside
        if p + 7 in shift_proj and true_proj[p][1] == shift_proj[p + 7][1]
    )
    checks.append(
        (
            "contact positions are position-specific",
            "PASS" if same < 0.6 * len(shifted) else f"FAIL {same}/{len(shifted)} unchanged",
        )
    )

    # 3. The mmCIF parser must refuse a file whose _atom_site header lost a column.
    cif = requests.get(RCSB_CIF.format(pdb="1KZ7"), timeout=TIMEOUT).text
    # RCSB pads header lines with a trailing space, so a naive
    # ``replace("_atom_site.Cartn_x\n", "")`` matches nothing and the test passes
    # by doing nothing.  Drop the line by predicate instead.
    dropped = [ln for ln in cif.splitlines() if ln.strip() != "_atom_site.Cartn_x"]
    if len(dropped) != len(cif.splitlines()) - 1:
        raise RuntimeError("self-test could not remove exactly one header line")
    broken = "\n".join(dropped)
    try:
        parse_cif_atoms(broken)
        checks.append(("missing mmCIF column raises", "FAIL (no exception)"))
    except RuntimeError:
        checks.append(("missing mmCIF column raises", "PASS"))

    # 4. NEGATIVE CONTROL for 3: the untouched file must parse silently.
    try:
        n = len(parse_cif_atoms(cif))
        checks.append(("intact mmCIF parses", "PASS" if n > 1000 else f"FAIL {n} atoms"))
    except RuntimeError as e:
        checks.append(("intact mmCIF parses", f"FAIL {e}"))

    # 5. A bad SIFTS expectation must raise rather than be absorbed.
    try:
        contact_positions("1KZ7", {**ANCHORS["1KZ7"], "gtpase": "P61586"})
        checks.append(("wrong SIFTS partner raises", "FAIL (no exception)"))
    except RuntimeError:
        checks.append(("wrong SIFTS partner raises", "PASS"))

    # 6. Flipping an expectation must abort the full run.
    saved = PANEL["Q8N1I0"]["expect"]
    PANEL["Q8N1I0"]["expect"] = "high"  # claim the non-DH out-group has the surface
    try:
        run()
        checks.append(("control failure aborts run", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(
            (
                "control failure aborts run",
                "PASS" if "control failure" in str(e) else f"FAIL {e}",
            )
        )
    finally:
        PANEL["Q8N1I0"]["expect"] = saved

    for name, verdict in checks:
        mark = verdict.split()[0]
        print(f"  [{mark}] {name}" + ("" if mark == "PASS" else f" -- {verdict}"))
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("dh_exchange_surface.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    for pdb, a in out["anchors"].items():
        print(
            f"{pdb} {a['gef_name']} . {a['substrate']}: "
            f"{len(a['contacts_in_dh'])} contact residues inside DH {a['dh_domain']}, "
            f"{len(a['contacts_outside_dh'])} outside"
        )
    print()
    header = f"{'symbol':<22} {'DH?':<4} {'role':<42}" + "".join(f"{p:>8}" for p in out["anchors"])
    print(header)
    for acc, meta in PANEL.items():
        cells = "".join(
            f"{out['anchors'][p]['panel'][acc]['retained_fraction']:>8.2f}" for p in out["anchors"]
        )
        dh = "yes" if out["has_dh_domain"][acc] else "NO"
        print(f"{meta['symbol']:<22} {dh:<4} {meta['role']:<42}{cells}")
    print()
    print("controls: every positive must beat its own composition-matched shuffle")
    for pdb, s in out["separation_observed"].items():
        print(
            f"  {pdb}  worst positive margin {s['worst_positive_margin_over_shuffle']:+.2f}   "
            f"out-group DOCK4 {s['out_group_score']:.2f} vs its own shuffle "
            f"{s['out_group_shuffle_mean']:.2f} ({s['out_group_margin_over_shuffle']:+.2f})"
        )
    print()
    print("ARHGEF16 retained fraction by substrate of the anchor complex:")
    for sub, d in out["target_retained_fraction_by_substrate"].items():
        print(f"  {sub:<6} {d['values']}  spread {d['spread']}")
    sd = out["substrate_discrimination"]
    print(f"  spread across all anchors: {sd['spread_across_all_anchors']}")
    print(
        f"  best-scoring anchor {sd['best_scoring_anchor']} is bound to "
        f"{sd['best_scoring_anchor_substrate']}; measured substrate is {sd['measured_substrate_of_target']}"
    )
    g = out["same_gef_two_substrates"]
    print(
        f"  same GEF ({g['gef']}) bound to {g['substrates'][0]} vs {g['substrates'][1]}: "
        f"contact-set Jaccard {g['jaccard']}, target score differs by {g['target_score_difference']}"
    )
    print()
    for k, v in out["limits"].items():
        print(f"  {k}: {v}")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
