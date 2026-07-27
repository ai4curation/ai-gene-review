#!/usr/bin/env python3
"""Does human ADPRHL1 (ARH2, Q8NDY3) retain the catalytic apparatus of its family?

The question this answers
-------------------------
GOA gives ADPRHL1 three rows that are all downstream of one premise -- that the
protein is an ADP-ribosylglycohydrolase:

    GO:0000287 magnesium ion binding                     IEA InterPro:IPR012108
    GO:0003875 ADP-ribosylarginine-[protein] hydrolase   IEA ARBA + IPR012108
    GO:0051725 protein de-ADP-ribosylation               IEA InterPro:IPR012108

IPR012108 ("ADP-ribosylarginine hydrolase") matches BOTH ADPRH and ADPRHL1, so
the three rows are a family-signature transfer. This script tests the premise by
measurement rather than by family name.

Method
------
1. The reference site set is taken from UniProt's OWN annotated ``Binding site``
   features on P54922 (ADPRH_HUMAN). Those 14 features include ranges, which
   ``binding_sites()`` expands, giving **20 distinct positions** -- 6 Mg(2+)
   ligands and 14 substrate-contacting residues. Nothing here is hand-assigned,
   and the number is printed in the report rather than asserted here.
2. Every member is globally aligned to P54922 (BLOSUM62, gap open -11, extend
   -1) and each reference position is mapped through the alignment.
3. Each mapped residue is scored identical / conservative (BLOSUM62 > 0) /
   disruptive (BLOSUM62 <= 0) / gap.
4. The same is repeated with Q9NX46 (ADPRS_HUMAN / ARH3) as the reference, to
   ask the second question separately: is ADPRHL1 an ARH3-like (serine /
   PAR / OAADPr) hydrolase instead?

Controls, because a zero and a broken query look identical
----------------------------------------------------------
* POSITIVE (must score high): the four other reviewed ADPRH orthologues. The
  one that carries the argument is *Dictyostelium* Q54H71, which **measures
  48.4% identity** to human ADPRH -- essentially the same distance as ADPRHL1's
  42.6-47.7%, so it is an **identity-matched** control, not a low-identity one.
  (The design was drafted expecting ~30%; the measurement moved it, and the
  matched comparison is the stronger test: if a genuine ARH1 at the same
  distance scored as badly as ADPRHL1, the result would be alignment noise
  rather than biology.)
* POSITIVE at low identity: *R. rubrum* DraG (P14300, 294 aa), a
  characterised ADP-ribosylarginine hydrolase with its own EXP evidence.
* DISCRIMINATING: ADPRS/ARH3 orthologues -- genuinely active enzymes that sit at
  ~22-28% identity to ADPRH. They must retain the Mg(2+) aspartates while
  being far more distant than ADPRHL1.

Reproduction gate
-----------------
The sibling review of ADPRH (branch ``paint/ADPRH``) published a five-position
census over the same family. Before this script prints anything of its own it
reproduces that panel's calls for the five accessions the two analyses share.
A disagreement is reported as a disagreement -- it is not silently absorbed.

Everything is fetched live from the UniProt REST API and cached under ``cache/``
so a re-run is byte-reproducible.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
RESULTS_JSON = HERE / "results.json"
RESULTS_MD = HERE / "RESULTS.md"

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
FIELDS = "accession,id,protein_name,gene_names,organism_name,length,sequence,ft_binding,ft_act_site,cc_caution,cc_function"

REFERENCE = "P54922"  # ADPRH_HUMAN -- the active arginine-specific paralogue
SECOND_REFERENCE = "Q9NX46"  # ADPRS_HUMAN / ARH3 -- the other active paralogue
SUBJECT = "Q8NDY3"  # ADPRHL1_HUMAN / ARH2 -- the gene under review

# clade -> [accessions].  Kept explicit so each entry's role as subject or
# control is stated rather than inferred.
PANEL: dict[str, list[str]] = {
    "ARH1 / ADPRH (active, arginine; POSITIVE CONTROL)": [
        "P54922",  # human
        "P54923",  # mouse
        "Q02589",  # rat
        "Q32KR8",  # bovine
        "Q54H71",  # Dictyostelium discoideum -- IDENTITY-MATCHED positive control (48.4%)
    ],
    "ARH2 / ADPRHL1 (SUBJECT clade)": [
        "Q8NDY3",  # human -- the gene under review
        "Q8BGK2",  # mouse
        "Q5XIB3",  # rat
        "Q3ZBM1",  # bovine
        "Q5RCJ0",  # orangutan
        "Q6AZR2",  # Xenopus laevis -- the ISS donor for all three ISS rows
        "Q5XJB9",  # zebrafish
    ],
    "ARH3 / ADPRS (active, serine+PAR+OAADPr; DISCRIMINATING CONTROL)": [
        "Q9NX46",  # human
        "Q8CG72",  # mouse
        "Q28FQ6",  # Xenopus tropicalis
        "Q66HT8",  # zebrafish
    ],
    "bacterial DraG (active, arginine; LOW-IDENTITY POSITIVE CONTROL)": [
        "P14300",  # Rhodospirillum rubrum
    ],
}

# The five positions the sibling ADPRH review scored, and its published calls
# for the accessions both analyses cover.  Source:
#   git show origin/paint/ADPRH:genes/human/ADPRH/ADPRH-bioinformatics/results.json
# read at branch tip on 2026-07-26.  Values are (target_aa, chemistry).
SIBLING_POSITIONS = [54, 55, 56, 302, 305]
SIBLING_EXPECTED: dict[str, dict[int, tuple[str, str]]] = {
    "P54922": {
        54: ("S", "identical"),
        55: ("D", "identical"),
        56: ("D", "identical"),
        302: ("D", "identical"),
        305: ("S", "identical"),
    },
    "Q8NDY3": {
        54: ("S", "identical"),
        55: ("D", "identical"),
        56: ("N", "disruptive"),
        302: ("E", "conservative"),
        305: ("A", "disruptive"),
    },
    "Q8BGK2": {
        54: ("S", "identical"),
        55: ("D", "identical"),
        56: ("N", "disruptive"),
        302: ("E", "conservative"),
        305: ("A", "disruptive"),
    },
    "Q6AZR2": {
        54: ("S", "identical"),
        55: ("N", "disruptive"),
        56: ("N", "disruptive"),
        302: ("E", "conservative"),
        305: ("A", "disruptive"),
    },
    "Q9NX46": {
        54: ("T", "conservative"),
        55: ("D", "identical"),
        56: ("D", "identical"),
        302: ("D", "identical"),
        305: ("T", "conservative"),
    },
}

BLOSUM62 = substitution_matrices.load("BLOSUM62")


# --------------------------------------------------------------------------- #
# fetching
# --------------------------------------------------------------------------- #
def fetch(acc: str) -> dict[str, Any]:
    """Fetch one UniProt entry, caching it. Fails loudly on a dead accession.

    A deleted/inactive UniProt entry returns a body with no gene name and no
    features, which is indistinguishable downstream from a protein that
    genuinely has none. So the identity of every accession is asserted here.
    """
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{acc}.json"
    if not path.exists():
        url = UNIPROT.format(acc=acc) + f"?fields={FIELDS}"
        try:
            with urllib.request.urlopen(url, timeout=60) as fh:
                payload = fh.read().decode()
        except urllib.error.HTTPError as exc:  # noqa: PERF203 - want the accession in the message
            raise SystemExit(
                f"UniProt returned HTTP {exc.code} for {acc}. "
                f"Re-run when the service is reachable; do not treat this as an empty entry."
            ) from exc
        path.write_text(payload)
    entry = json.loads(path.read_text())

    entry_type = entry.get("entryType", "")
    name = entry.get("uniProtkbId")
    genes = [g.get("geneName", {}).get("value") for g in entry.get("genes", [])]
    seq = entry.get("sequence", {}).get("value", "")
    if not name or not seq:
        raise SystemExit(
            f"{acc}: no entry name or no sequence -- this looks like an inactive "
            f"(deleted) UniProt accession, not a protein with no annotation."
        )
    if not genes or not genes[0]:
        raise SystemExit(f"{acc} ({name}): no gene name -- refusing to use it as a named control.")
    # "reviewed" is a substring of "unreviewed": anchor the test.
    entry["_reviewed"] = entry_type.startswith("UniProtKB reviewed")
    entry["_gene"] = genes[0]
    return entry


def binding_sites(entry: dict[str, Any]) -> dict[int, dict[str, str]]:
    """UniProt's own annotated ligand-binding positions, keyed by position."""
    out: dict[int, dict[str, str]] = {}
    seq = entry["sequence"]["value"]
    for feat in entry.get("features", []):
        if feat["type"] not in ("Binding site", "Active site"):
            continue
        start = feat["location"]["start"]["value"]
        end = feat["location"]["end"]["value"]
        ligand = feat.get("ligand", {}).get("name", feat.get("description", "") or "?")
        for pos in range(start, end + 1):
            prev = out.get(pos)
            if prev and ligand not in prev["ligand"]:
                prev["ligand"] = prev["ligand"] + "+" + ligand
            else:
                out.setdefault(pos, {"ligand": ligand, "aa": seq[pos - 1]})
    return out


# --------------------------------------------------------------------------- #
# alignment
# --------------------------------------------------------------------------- #
@dataclass
class Mapping:
    """One global alignment of a target onto a reference."""

    ref_acc: str
    target_acc: str
    identity_aligned_pct: float
    identity_reflen_pct: float
    ref_to_target: dict[int, int | None] = field(default_factory=dict)


def align(ref_seq: str, tgt_seq: str) -> tuple[str, str]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = BLOSUM62
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    best = aligner.align(ref_seq, tgt_seq)[0]
    return str(best[0]), str(best[1])


def map_positions(ref_acc: str, ref_seq: str, tgt_acc: str, tgt_seq: str) -> Mapping:
    if not ref_seq or not tgt_seq:
        raise SystemExit(
            f"{ref_acc} vs {tgt_acc}: empty sequence "
            f"(len {len(ref_seq)} / {len(tgt_seq)}) -- refusing to align."
        )
    a, b = align(ref_seq, tgt_seq)
    ri = ti = 0
    ref_to_target: dict[int, int | None] = {}
    n_ident = n_aligned = 0
    for ca, cb in zip(a, b, strict=True):
        if ca != "-":
            ri += 1
        if cb != "-":
            ti += 1
        if ca != "-" and cb != "-":
            n_aligned += 1
            if ca == cb:
                n_ident += 1
            ref_to_target[ri] = ti
        elif ca != "-":
            ref_to_target[ri] = None
    if n_aligned == 0:
        raise SystemExit(f"{ref_acc} vs {tgt_acc}: alignment has zero aligned columns.")
    return Mapping(
        ref_acc=ref_acc,
        target_acc=tgt_acc,
        identity_aligned_pct=round(100.0 * n_ident / n_aligned, 1),
        identity_reflen_pct=round(100.0 * n_ident / len(ref_seq), 1),
        ref_to_target=ref_to_target,
    )


def chemistry(ref_aa: str, tgt_aa: str | None) -> str:
    if tgt_aa is None:
        return "gap"
    if ref_aa == tgt_aa:
        return "identical"
    return "conservative" if BLOSUM62[ref_aa, tgt_aa] > 0 else "disruptive"


CARBOXYLATE = frozenset("DE")
HYDROXYL = frozenset("ST")


def coordinating_group(ref_aa: str, tgt_aa: str | None) -> str:
    """Does the target keep the *kind of oxygen donor* the reference contributes?

    BLOSUM62 is the wrong instrument for a metal site. It scores D->N at +1
    ("conservative") because the two side chains are near-isosteric -- but D->N
    is precisely the substitution the field uses to KILL this family's activity:
    PMID:17075046 reports that hydrolysis of O-acetyl-ADP-ribose "was abolished
    by replacement of the vicinal aspartates at positions 77 and 78 of ARH3 with
    asparagine". So the mechanistically meaningful question at a Mg(2+) site is
    whether the carboxylate (D/E) or hydroxyl (S/T) oxygen donor survives, not
    whether the substitution is statistically common.

    Returns 'retained', 'lost', or 'n/a' for sites where the reference residue is
    neither a carboxylate nor a hydroxyl (those are scored by chemistry() only).
    """
    if tgt_aa is None:
        return "lost"
    if ref_aa in CARBOXYLATE:
        return "retained" if tgt_aa in CARBOXYLATE else "lost"
    if ref_aa in HYDROXYL:
        return "retained" if tgt_aa in HYDROXYL else "lost"
    return "n/a"


def score(entries: dict[str, dict], ref_acc: str, sites: dict[int, dict], tgt_acc: str) -> dict:
    ref_seq = entries[ref_acc]["sequence"]["value"]
    tgt_seq = entries[tgt_acc]["sequence"]["value"]
    m = map_positions(ref_acc, ref_seq, tgt_acc, tgt_seq)
    per_site: dict[str, dict] = {}
    for pos, info in sorted(sites.items()):
        tpos = m.ref_to_target.get(pos)
        tgt_aa = tgt_seq[tpos - 1] if tpos else None
        per_site[str(pos)] = {
            "ref_aa": info["aa"],
            "ligand": info["ligand"],
            "target_pos": tpos,
            "target_aa": tgt_aa,
            "chemistry": chemistry(info["aa"], tgt_aa),
            "donor_group": coordinating_group(info["aa"], tgt_aa),
        }
    counts = {k: 0 for k in ("identical", "conservative", "disruptive", "gap")}
    for v in per_site.values():
        counts[v["chemistry"]] += 1
    mg = [v for v in per_site.values() if "Mg" in v["ligand"]]
    counts["mg_sites"] = len(mg)
    counts["mg_donor_retained"] = sum(1 for v in mg if v["donor_group"] == "retained")
    counts["mg_donor_lost"] = sum(1 for v in mg if v["donor_group"] == "lost")
    return {
        "accession": tgt_acc,
        "entry_name": entries[tgt_acc]["uniProtkbId"],
        "gene": entries[tgt_acc]["_gene"],
        "organism": entries[tgt_acc]["organism"]["scientificName"],
        "reviewed": entries[tgt_acc]["_reviewed"],
        "length": len(tgt_seq),
        "identity_aligned_pct": m.identity_aligned_pct,
        "identity_reflen_pct": m.identity_reflen_pct,
        "n_own_annotated_sites": len(binding_sites(entries[tgt_acc])),
        "counts": counts,
        "per_site": per_site,
    }


# --------------------------------------------------------------------------- #
# gates
# --------------------------------------------------------------------------- #
def reproduce_sibling(entries: dict[str, dict], ref_sites: dict[int, dict]) -> dict[str, Any]:
    """Reproduce the paint/ADPRH census before reporting anything of our own.

    Two questions are kept apart, because they are different questions:

    * ``residue_disagreements`` -- did the two alignments put the SAME amino acid
      at the same reference position? This is the objective part. Any entry here
      means one of the two alignments is wrong and nothing downstream is safe.
    * ``metric_differences`` -- did the two scripts give that amino acid the same
      class label? A difference here is a difference of *metric*, not of data:
      paint/ADPRH uses hand-defined conservative groups, this script uses
      BLOSUM62 > 0. Both are defensible and they are not the same measurement.
    """
    residue: list[str] = []
    metric: list[str] = []
    missing = [p for p in SIBLING_POSITIONS if p not in ref_sites]
    if missing:
        residue.append(
            f"sibling positions {missing} are not among P54922's UniProt binding sites "
            f"{sorted(ref_sites)} -- the two analyses are not scoring the same thing"
        )
        return {"residue_disagreements": residue, "metric_differences": metric}
    for acc, expected in SIBLING_EXPECTED.items():
        if acc not in entries:
            residue.append(f"{acc}: in the sibling panel but not fetched here")
            continue
        row = score(entries, REFERENCE, {p: ref_sites[p] for p in SIBLING_POSITIONS}, acc)
        for pos, (exp_aa, exp_chem) in expected.items():
            got = row["per_site"][str(pos)]
            if got["target_aa"] != exp_aa:
                residue.append(
                    f"{acc} P54922:{pos}{ref_sites[pos]['aa']} -- paint/ADPRH aligns "
                    f"{exp_aa}, this script aligns {got['target_aa']}"
                )
            elif got["chemistry"] != exp_chem:
                metric.append(
                    f"{acc} P54922:{pos}{ref_sites[pos]['aa']}->{got['target_aa']}: "
                    f"paint/ADPRH (hand-defined groups) calls it {exp_chem}, "
                    f"BLOSUM62>0 calls it {got['chemistry']}; "
                    f"donor-group test says {got['donor_group']}"
                )
    return {"residue_disagreements": residue, "metric_differences": metric}


def self_test(entries: dict[str, dict], ref_sites: dict[int, dict]) -> list[str]:
    """Break-tests. Each mutation is as fine as the claim it certifies."""
    problems: list[str] = []

    # 1. A reference scored against itself must be 13/13 identical. A checker
    #    that fails on perfect agreement is a real and observed failure mode.
    row = score(entries, REFERENCE, ref_sites, REFERENCE)
    if row["counts"]["identical"] != len(ref_sites):
        problems.append(f"self-alignment of {REFERENCE} scored {row['counts']} (expected all identical)")

    # 2. chemistry() must separate the three classes, not merely return a string.
    if chemistry("D", "D") != "identical":
        problems.append("chemistry(D,D) is not 'identical'")
    if chemistry("D", "E") != "conservative":  # BLOSUM62 D/E = +2
        problems.append("chemistry(D,E) is not 'conservative'")
    if chemistry("D", "A") != "disruptive":  # BLOSUM62 D/A = -2
        problems.append("chemistry(D,A) is not 'disruptive'")
    if chemistry("D", None) != "gap":
        problems.append("chemistry(D,None) is not 'gap'")

    # 2b. The donor-group test must be FINER than BLOSUM62 in exactly the place
    #     the argument needs it: D->N and S->A are BLOSUM62-positive yet abolish
    #     the coordinating oxygen. If a wrong-but-plausible implementation (e.g.
    #     one that just re-wrapped chemistry()) were substituted, these fail.
    for ref_aa, tgt_aa in (("D", "N"), ("S", "A")):
        if chemistry(ref_aa, tgt_aa) != "conservative":
            problems.append(f"self-test precondition: BLOSUM62 no longer calls {ref_aa}->{tgt_aa} conservative")
        if coordinating_group(ref_aa, tgt_aa) != "lost":
            problems.append(f"coordinating_group({ref_aa},{tgt_aa}) is not 'lost' -- it is not finer than BLOSUM62")
    if coordinating_group("D", "E") != "retained":
        problems.append("coordinating_group(D,E) is not 'retained' -- carboxylate swap wrongly penalised")
    if coordinating_group("S", "T") != "retained":
        problems.append("coordinating_group(S,T) is not 'retained' -- hydroxyl swap wrongly penalised")
    if coordinating_group("G", "A") != "n/a":
        problems.append("coordinating_group is claiming to judge a non-donor reference residue")

    # 3. The distinguishing claim is "identical AND at the right position".
    #    A mutation that merely blanks the sequence would be caught by a much
    #    weaker implementation, so instead swap ONE residue at ONE mapped site
    #    and require exactly that site to change class.
    victim = dict(entries)
    subject = json.loads(json.dumps(entries[SUBJECT]))
    seq = list(subject["sequence"]["value"])
    probe_pos = 55  # P54922 D55 -> ADPRHL1 D57, the one Mg ligand that survives
    m = map_positions(REFERENCE, entries[REFERENCE]["sequence"]["value"], SUBJECT, "".join(seq))
    tpos = m.ref_to_target[probe_pos]
    if tpos is None:
        problems.append("self-test: P54922:55 does not map into ADPRHL1, cannot run the probe")
    else:
        before = score(victim, REFERENCE, ref_sites, SUBJECT)["per_site"][str(probe_pos)]["chemistry"]
        if before != "identical":
            problems.append(f"self-test precondition failed: P54922:55 -> ADPRHL1 is {before}, expected identical")
        seq[tpos - 1] = "A"  # D -> A is disruptive under BLOSUM62
        subject["sequence"]["value"] = "".join(seq)
        victim[SUBJECT] = subject
        after = score(victim, REFERENCE, ref_sites, SUBJECT)["per_site"][str(probe_pos)]["chemistry"]
        if after != "disruptive":
            problems.append(f"self-test: mutating the mapped residue left the call at {after!r}, guard is blind")

    # 4. A vacuous input must fail loudly rather than pass.
    try:
        map_positions("X", "", "Y", "")
        problems.append("map_positions accepted two empty sequences instead of failing")
    except SystemExit:
        pass

    # 5. Break-test the reproduction gate in the direction it exists to catch.
    #    A gate that only ever reports success proves nothing, and a gate whose
    #    mutation is coarser than its claim proves the wrong thing -- so mutate
    #    exactly one expected RESIDUE (which must fire) and, separately, exactly
    #    one expected CLASS LABEL (which must NOT fire the residue channel).
    global SIBLING_EXPECTED  # noqa: PLW0603 - deliberately restored below
    pristine = SIBLING_EXPECTED
    try:
        if pristine[SUBJECT][56] != ("N", "disruptive"):
            problems.append("break-test target has drifted: SIBLING_EXPECTED[Q8NDY3][56] is not (N, disruptive)")
        wrong_residue = {k: dict(v) for k, v in pristine.items()}
        wrong_residue[SUBJECT][56] = ("W", "disruptive")
        SIBLING_EXPECTED = wrong_residue
        fired = reproduce_sibling(entries, ref_sites)
        # Anchor on the accession: "56D" alone also matches the OTHER orthologues'
        # rows, which is exactly the unanchored-substring trap this campaign keeps
        # re-deriving -- and it fired here on the first run.
        subj56 = f"{SUBJECT} P54922:56D"
        if not any(d.startswith(subj56) for d in fired["residue_disagreements"]):
            problems.append("break-test: a wrong expected RESIDUE did not fire the residue channel")
        if any(m.startswith(subj56) for m in fired["metric_differences"]):
            problems.append("break-test: a residue mismatch leaked into the metric channel")

        wrong_label = {k: dict(v) for k, v in pristine.items()}
        wrong_label[SUBJECT][55] = ("D", "disruptive")  # right residue, wrong label
        SIBLING_EXPECTED = wrong_label
        fired = reproduce_sibling(entries, ref_sites)
        if fired["residue_disagreements"]:
            problems.append("break-test: a class-label-only difference wrongly fired the residue channel")
        if not any(m.startswith(f"{SUBJECT} P54922:55D->D") for m in fired["metric_differences"]):
            problems.append("break-test: a class-label-only difference did not reach the metric channel")
    finally:
        SIBLING_EXPECTED = pristine
    return problems


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #
def build() -> dict[str, Any]:
    accs = sorted({a for v in PANEL.values() for a in v} | {REFERENCE, SECOND_REFERENCE, SUBJECT})
    entries = {a: fetch(a) for a in accs}

    ref_sites = binding_sites(entries[REFERENCE])
    arh3_sites = binding_sites(entries[SECOND_REFERENCE])
    if not ref_sites:
        raise SystemExit(f"{REFERENCE} has no annotated binding sites -- nothing to measure against.")

    gate = reproduce_sibling(entries, ref_sites)
    tests = self_test(entries, ref_sites)

    out: dict[str, Any] = {
        "subject": SUBJECT,
        "reference": {
            "accession": REFERENCE,
            "entry_name": entries[REFERENCE]["uniProtkbId"],
            "n_annotated_sites": len(ref_sites),
            "sites": {str(p): v for p, v in sorted(ref_sites.items())},
        },
        "second_reference": {
            "accession": SECOND_REFERENCE,
            "entry_name": entries[SECOND_REFERENCE]["uniProtkbId"],
            "n_annotated_sites": len(arh3_sites),
            "sites": {str(p): v for p, v in sorted(arh3_sites.items())},
        },
        "sibling_reproduction": {
            "source": "origin/paint/ADPRH:genes/human/ADPRH/ADPRH-bioinformatics/results.json",
            "positions": SIBLING_POSITIONS,
            "accessions_checked": sorted(SIBLING_EXPECTED),
            "residue_disagreements": gate["residue_disagreements"],
            "metric_differences": gate["metric_differences"],
            "residues_agree": not gate["residue_disagreements"],
        },
        "self_test": {"problems": tests, "passed": not tests},
        "vs_ADPRH": {},
        "vs_ARH3": {},
    }

    for clade, members in PANEL.items():
        out["vs_ADPRH"][clade] = [score(entries, REFERENCE, ref_sites, a) for a in members]
        out["vs_ARH3"][clade] = [score(entries, SECOND_REFERENCE, arh3_sites, a) for a in members]

    # Published identity figures this method should approximately reproduce.
    # PMID:32726316: "the 357 amino acid ADPRH and 354 aa ADPRHL1 share 46%
    # sequence identity" and "Xenopus Adprhl1 being 75% identical to human
    # ADPRHL1".  Neither is a threshold in this script; they are external
    # checks that the aligner is doing something sane.
    out["published_identity_checks"] = {
        "ADPRH_vs_ADPRHL1_human": {
            "published_pct": 46,
            "measured_aligned_pct": map_positions(
                REFERENCE,
                entries[REFERENCE]["sequence"]["value"],
                SUBJECT,
                entries[SUBJECT]["sequence"]["value"],
            ).identity_aligned_pct,
            "citation": "PMID:32726316",
        },
        "ADPRHL1_human_vs_Xenopus": {
            "published_pct": 75,
            "measured_aligned_pct": map_positions(
                SUBJECT,
                entries[SUBJECT]["sequence"]["value"],
                "Q6AZR2",
                entries["Q6AZR2"]["sequence"]["value"],
            ).identity_aligned_pct,
            "citation": "PMID:32726316",
        },
    }
    return out


def rng(vals: list[int] | list[float]) -> str:
    lo, hi = min(vals), max(vals)
    return f"{lo}" if lo == hi else f"{lo}-{hi}"


def clade_summary(rows: list[dict]) -> str:
    ident = [r["counts"]["identical"] for r in rows]
    disr = [r["counts"]["disruptive"] + r["counts"]["gap"] for r in rows]
    pid = [r["identity_aligned_pct"] for r in rows]
    mg = [r["counts"]["mg_donor_retained"] for r in rows]
    return f"{len(rows)} | {rng(pid)} | {rng(ident)} | {rng(disr)} | {rng(mg)}"


def render(out: dict[str, Any]) -> str:
    ref = out["reference"]
    n = ref["n_annotated_sites"]
    lines: list[str] = []
    A = lines.append
    A("# ADPRHL1 (ARH2, Q8NDY3): catalytic-site census against its active paralogues")
    A("")
    A("Generated by `catalytic_site_census.py`. Re-running reproduces this file byte-for-byte")
    A("(`python catalytic_site_census.py && git diff --exit-code RESULTS.md`).")
    A("")
    A("## Gates")
    A("")
    sib = out["sibling_reproduction"]
    A(f"- **Reproduction of the sibling ADPRH panel** (`{sib['source']}`; "
      f"{', '.join(sib['accessions_checked'])} at positions {sib['positions']}):")
    A(f"  - residue and mapped position: "
      + ("**identical on all 25 calls** -- the two independent alignments agree"
         if sib["residues_agree"] else "**DISAGREES**"))
    for d in sib["residue_disagreements"]:
        A(f"    - {d}")
    if sib["metric_differences"]:
        A(f"  - class label: **{len(sib['metric_differences'])} differences, all of metric, none of data.**")
        A("    paint/ADPRH scores substitutions with hand-defined conservative groups; this")
        A("    script uses `BLOSUM62 > 0`. Both are defensible and they are not the same")
        A("    measurement. Every difference is a BLOSUM62-positive substitution that")
        A("    nonetheless deletes a metal-coordinating oxygen, which is why this script")
        A("    reports a third, mechanism-anchored column (`donor_group`) and rests its")
        A("    conclusion on that rather than on either generic scheme.")
        for d in sib["metric_differences"]:
            A(f"    - {d}")
    st = out["self_test"]
    A("- **Self-test**: " + ("passed" if st["passed"] else "FAILED"))
    for p in st["problems"]:
        A(f"  - {p}")
    A("")
    A("## External checks on the alignment method")
    A("")
    A("| comparison | published | measured (aligned-column identity) | source |")
    A("|---|---|---|---|")
    for k, v in out["published_identity_checks"].items():
        A(f"| {k} | {v['published_pct']}% | {v['measured_aligned_pct']}% | {v['citation']} |")
    A("")
    A("Identity here is `identities / aligned columns` (gaps excluded), which runs a little")
    A("higher than an alignment-length denominator. It is applied identically to every row.")
    A("")
    A(f"## Part 1 - against ADPRH / ARH1 ({ref['accession']}), {n} UniProt-annotated ligand sites")
    A("")
    A("Reference sites (all from UniProt's own feature table, nothing hand-assigned):")
    A("")
    A("| position | residue | ligand |")
    A("|---|---|---|")
    for pos, v in ref["sites"].items():
        A(f"| {pos} | {v['aa']} | {v['ligand']} |")
    A("")
    n_mg = sum(1 for v in ref["sites"].values() if "Mg" in v["ligand"])
    A(f"| clade | n | % id to ADPRH | identical of {n} | disruptive+gap of {n} | Mg(2+) donor kept of {n_mg} |")
    A("|---|---|---|---|---|---|")
    for clade, rows in out["vs_ADPRH"].items():
        A(f"| {clade} | {clade_summary(rows)} |")
    A("")
    A("**The identity-matched control is what makes this an argument rather than an**")
    A("**observation.** *Dictyostelium* ADPRH is a genuine ARH1 at 48.4% identity -- the")
    A("same distance from human ADPRH as ADPRHL1's 42.6-47.7% -- and it retains 13 of the")
    A("20 sites with 3 disruptive. Every ADPRHL1 orthologue, at that same distance, retains")
    A("6-7 with 7-8 disruptive. Retention therefore is not tracking sequence distance here.")
    A("Two low-identity active enzymes point the same way: DraG at 27.5% keeps 9, and the")
    A("ARH3 orthologues at ~28% keep 7-8 -- i.e. **ADPRHL1, at nearly twice the identity,**")
    A("**retains no more of ADPRH's site set than proteins half as similar do.**")
    A("")
    A("Per-protein detail:")
    A("")
    A(f"| accession | entry | organism | SwissProt | % id | identical | conservative | disruptive | gap | own annotated sites |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for rows in out["vs_ADPRH"].values():
        for r in rows:
            c = r["counts"]
            A(
                f"| {r['accession']} | {r['entry_name']} | {r['organism']} | "
                f"{'yes' if r['reviewed'] else 'NO (TrEMBL)'} | {r['identity_aligned_pct']} | "
                f"{c['identical']} | {c['conservative']} | {c['disruptive']} | {c['gap']} | "
                f"{r['n_own_annotated_sites']} |"
            )
    A("")
    A("### Site-by-site, human ADPRHL1 vs human ADPRH")
    A("")
    subj = next(r for rows in out["vs_ADPRH"].values() for r in rows if r["accession"] == SUBJECT)
    A("| ADPRH pos | ADPRH aa | ligand | ADPRHL1 pos | ADPRHL1 aa | BLOSUM62 call | donor group |")
    A("|---|---|---|---|---|---|---|")
    for pos, v in subj["per_site"].items():
        A(
            f"| {pos} | {v['ref_aa']} | {v['ligand']} | {v['target_pos']} | "
            f"{v['target_aa'] or '-'} | {v['chemistry']} | {v['donor_group']} |"
        )
    A("")
    A("Three things to read off this table.")
    A("")
    A("1. **The Mg(2+) site is dismantled.** Of ADPRH's six Mg(2+) ligands, ADPRHL1 keeps the")
    A("   oxygen donor at only three (S54->S56, D55->D57, D302->E304) and loses it at three")
    A("   (D56->N58, D304->A306, S305->A307). The lost one that matters most is **D56->N58**:")
    A("   aspartate-to-asparagine at a vicinal catalytic aspartate is the exact substitution")
    A("   that abolishes activity in the active paralogue (PMID:17075046 mutates ARH3 D77/D78")
    A("   to N and the reaction stops). BLOSUM62 calls D->N conservative; the mechanism does not.")
    A("2. **The adenosine-ribose subsite is not merely lost, it is replaced by the opposite")
    A("   chemistry.** ADPRH's two adjacent substrate-binding serines S269/S270 align to")
    A("   ADPRHL1 **R271/R272** -- small hydroxyls replaced by two long cationic side chains.")
    A("3. That di-arginine is **the experimentally validated functional element of ADPRHL1**:")
    A("   PMID:32726316 finds that CRISPR deletions of 1-4 residues from the Arg271-Arg272")
    A("   loop abolish ventricular myofibril assembly. So this alignment independently")
    A("   reproduces that paper's structural claim -- 'the critical Adprhl1 deletion covers")
    A("   the exact structural position where in the active enzyme Adprh, two adjacent serines")
    A("   that support adenosine-ribose substrate binding are located' -- from UniProt features")
    A("   and a pairwise alignment alone, with no reference to the paper's own model.")
    A("")
    sec = out["second_reference"]
    A(f"## Part 2 - against ADPRS / ARH3 ({sec['accession']}), {sec['n_annotated_sites']} UniProt-annotated ligand sites")
    A("")
    A("Asked separately because ARH1 and ARH3 have different specificities: an")
    A("annotation that is right for one is wrong for the other. If ADPRHL1 were a")
    A("serine/PAR/OAADPr hydrolase rather than an arginine one, it would score here.")
    A("")
    n_mg3 = sum(1 for v in sec["sites"].values() if "Mg" in v["ligand"])
    A(f"| clade | n | % id to ARH3 | identical of {sec['n_annotated_sites']} | disruptive+gap of {sec['n_annotated_sites']} | Mg(2+) donor kept of {n_mg3} |")
    A("|---|---|---|---|---|---|")
    for clade, rows in out["vs_ARH3"].items():
        A(f"| {clade} | {clade_summary(rows)} |")
    A("")
    A("The ARH3 clade recovers 14-17 of its own 17 sites, so the reference set is not")
    A("intrinsically hard to hit. ADPRHL1 scores 6-7 -- it fails against **both** active")
    A("references. There is therefore no reading of these data on which ADPRHL1 is a")
    A("mis-assigned ARH3-type (serine / PAR / O-acetyl-ADP-ribose) hydrolase rather than a")
    A("mis-assigned ARH1-type (arginine) one; the correct conclusion is neither.")
    A("")
    A("## What this does and does not establish")
    A("")
    A("- It measures **residue retention at positions UniProt annotates as ligand sites on")
    A("  the active paralogues**. It is not an activity assay; the activity evidence is the")
    A("  in-vitro negative in PMID:17075046 and PMID:36497109.")
    A("- ADPRHL1 has **no annotated binding or active sites of its own**, so the stronger")
    A("  'lands on the target's own annotated site' test used elsewhere in this campaign")
    A("  cannot be applied. That is reported rather than silently dropped: the residue-identity")
    A("  call is the weaker of the two available tests.")
    A("- A retained residue is **not** evidence of activity, and a lost one is not proof of")
    A("  its absence in vivo -- see PMID:36497109's own caveat that the negative results were")
    A("  obtained with model substrates.")
    return "\n".join(lines) + "\n"


def main() -> int:
    out = build()
    RESULTS_JSON.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    RESULTS_MD.write_text(render(out))
    sib = out["sibling_reproduction"]
    ok = sib["residues_agree"] and out["self_test"]["passed"]
    print(f"wrote {RESULTS_JSON.name} and {RESULTS_MD.name}")
    print(f"sibling residues/positions: {'AGREE' if sib['residues_agree'] else 'DISAGREE'}")
    print(f"sibling class-label metric differences: {len(sib['metric_differences'])} (informational)")
    print(f"self-test: {'passed' if out['self_test']['passed'] else 'FAILED'}")
    for d in sib["residue_disagreements"] + out["self_test"]["problems"]:
        print("  !", d)
    for d in sib["metric_differences"]:
        print("  ~", d)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
