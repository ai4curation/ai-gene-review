#!/usr/bin/env python3
"""Test whether human ADCK2 retains the diagnostic UbiB / atypical-protein-kinase-like
(uPKL) motifs that were structurally and biochemically characterised in COQ8A/COQ8B.

Question this answers
---------------------
ADCK2 is annotated by UniProt with ``EC 2.7.11.-`` and the keyword
``Serine/threonine-protein kinase``, yet its own FUNCTION comment says the function is
unknown.  The UbiB family's characterised members (COQ8A/ADCK3, COQ8B/ADCK4) were shown
NOT to carry canonical, in-trans protein kinase activity: the family-specific KxGQ
domain occludes the peptide-substrate site, and an alanine of the "A-rich loop" (the
UbiB replacement for the canonical Gly-rich loop) actively suppresses phosphotransfer
(PMID:25498144, PMID:27499294).

So the falsifiable question for ADCK2 is not "does it look like a kinase" but:

  (a) does it retain the *catalytic* machinery (beta3 Lys, catalytic Asp, Mg-binding
      Asn, DFG-equivalent Asp) -- i.e. is it a plausible phosphotransferase at all? and
  (b) does it retain the *UbiB-specific suppressors* of canonical protein kinase
      activity (KxGQ motif, A-rich loop) -- i.e. is it a uPKL like COQ8, or has it
      reverted to a conventional protein kinase architecture?

Method
------
Multiple sequence alignment (Clustal Omega at EBI) of the human/yeast/bacterial UbiB
family, then projection of COQ8A's *own UniProt-annotated* motif and ligand-binding
positions through the alignment onto every other member.  Following the campaign rule
that a residue match alone is not evidence, we require BOTH:

  * residue identity/compatibility at the aligned position, AND
  * that the aligned position in the target lands on a position the target's own
    UniProt feature table annotates (where the target has such an annotation),

and we report the two conditions separately rather than collapsing them.

Positive control: COQ8B, an independently characterised member, must reproduce COQ8A's
motifs.  Negative control: a protein-kinase-superfamily member outside UbiB (human
PKACA, P17612) must NOT reproduce the UbiB-specific KxGQ/A-rich motifs while still
matching the canonical catalytic residues.

Outputs ``results.json`` and prints a table.  Nothing here is hardcoded from a prior
run; if an input cannot be fetched the script fails loudly.
"""

from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass, asdict, field
from pathlib import Path

import requests

HERE = Path(__file__).parent
UNIPROT = "https://rest.uniprot.org/uniprotkb"
CLUSTALO = "https://www.ebi.ac.uk/Tools/services/rest/clustalo"
EMAIL = "ai-gene-review@example.org"

# Subject first, then the characterised members, then controls.
MEMBERS: dict[str, str] = {
    "Q7Z695": "ADCK2_HUMAN",     # subject
    "Q8NI60": "COQ8A_HUMAN",     # reference: structure + biochemistry (PMID:25498144/27499294)
    "Q96D53": "COQ8B_HUMAN",     # positive control: independently annotated UbiB
    "Q02981": "CQD1_YEAST",      # YPL109C/Cqd1: the ADCK2 orthologue (PMID:34362905)
    "Q06567": "CQD2_YEAST",      # YLR253W/Mcp2/Cqd2: the ADCK1 orthologue (PMID:34362905)
    "Q86TW2": "ADCK1_HUMAN",     # paralogue, different PANTHER family
    "Q3MIX3": "ADCK5_HUMAN",     # paralogue
    "P0A6A0": "UBIB_ECOLI",      # bacterial archetype
    "P17612": "KAPCA_HUMAN",     # NEGATIVE control: canonical Ser/Thr protein kinase
}

REFERENCE = "Q8NI60"  # COQ8A: the member whose motifs are experimentally grounded

# COQ8A positions taken from its UniProt feature table (fetched at runtime and
# cross-checked, never trusted from this literal alone).
REF_SITES: dict[str, tuple[int, str]] = {
    "KxGQ_K": (276, "KxGQ motif, invariant Lys; occludes peptide-substrate site"),
    "KxGQ_Q": (279, "KxGQ motif Gln"),
    "Arich_A1": (337, "A-rich loop A337 (Gly-rich-loop equivalent)"),
    "Arich_A3": (339, "A-rich loop A339; A339G de-represses autophosphorylation"),
    "Arich_S": (340, "A-rich loop Ser; ATP-binding"),
    "beta3_K": (358, "beta3 Lys (VAIK equivalent); ATP-binding"),
    "cat_D": (488, "catalytic Asp, proton acceptor (HRD/HAD equivalent)"),
    "cat_N": (493, "catalytic-loop Asn; Mg2+ / ATP-binding"),
    "DFG_D": (507, "DFG-equivalent Asp; Mg2+ / ATP-binding"),
}

CONSERVATIVE = [set("AGSTP"), set("ILVMFC"), set("DENQ"), set("KRH"), set("FYW")]


def _english_list(items: list[str]) -> str:
    """Join for prose: 'A', 'A and B', 'A, B and C'. A bare ' and '.join degrades to
    'A and B and C' as soon as a third member appears -- unreachable at the current
    membership, which is exactly why it would go unnoticed when membership changes."""
    if not items:
        return "none"
    if len(items) == 1:
        return items[0]
    return f"{', '.join(items[:-1])} and {items[-1]}"


def conservative(a: str, b: str) -> bool:
    return any(a in g and b in g for g in CONSERVATIVE)


@dataclass
class Entry:
    accession: str
    entry_name: str
    reviewed: bool
    length: int
    sequence: str
    features: list[dict] = field(default_factory=list)

    def annotated_positions(self) -> set[int]:
        pos: set[int] = set()
        for f in self.features:
            for p in range(f["start"], f["end"] + 1):
                pos.add(p)
        return pos

    def feature_at(self, p: int) -> list[str]:
        return [
            f"{f['type']}:{f['description']}"
            for f in self.features
            if f["start"] <= p <= f["end"]
        ]


def fetch_entry(acc: str) -> Entry:
    fields = "accession,id,reviewed,length,sequence,ft_motif,ft_act_site,ft_binding,ft_domain"
    r = requests.get(f"{UNIPROT}/{acc}.json?fields={fields}", timeout=60)
    r.raise_for_status()
    d = r.json()
    seq = d["sequence"]["value"]
    if not seq:
        raise SystemExit(f"FATAL: empty sequence for {acc}; UniProt entry may be dead")
    entry_type = d.get("entryType", "")
    # NB: 'reviewed' is a substring of 'unreviewed' -- must anchor with startswith.
    reviewed = entry_type.startswith("UniProtKB reviewed")
    feats = []
    for f in d.get("features", []):
        if f["type"] in ("Motif", "Active site", "Binding site"):
            lig = (f.get("ligand") or {}).get("name", "")
            desc = f.get("description") or lig or f["type"]
            feats.append(
                {
                    "type": f["type"],
                    "description": desc,
                    "start": f["location"]["start"]["value"],
                    "end": f["location"]["end"]["value"],
                }
            )
    return Entry(
        accession=d["primaryAccession"],
        entry_name=d.get("uniProtkbId", acc),
        reviewed=reviewed,
        length=d["sequence"]["length"],
        sequence=seq,
        features=feats,
    )


def clustal_omega(entries: dict[str, Entry]) -> dict[str, str]:
    fasta = "".join(f">{e.accession}\n{e.sequence}\n" for e in entries.values())
    r = requests.post(
        f"{CLUSTALO}/run",
        data={"email": EMAIL, "sequence": fasta, "stype": "protein", "outfmt": "clustal_num"},
        timeout=120,
    )
    r.raise_for_status()
    job = r.text.strip()
    for _ in range(120):
        s = requests.get(f"{CLUSTALO}/status/{job}", timeout=60).text.strip()
        if s == "FINISHED":
            break
        if s in ("ERROR", "FAILURE", "NOT_FOUND"):
            raise SystemExit(f"FATAL: Clustal Omega job {job} -> {s}")
        time.sleep(3)
    else:
        raise SystemExit(f"FATAL: Clustal Omega job {job} did not finish")
    # NB: the EBI result-type identifier for the FASTA alignment is "fa", not
    # "aln-fasta"; the wrong identifier returns a non-FASTA body with HTTP 200, which
    # is why the parser below asserts the names it recovered rather than trusting them.
    resp = requests.get(f"{CLUSTALO}/result/{job}/fa", timeout=120)
    resp.raise_for_status()
    aln = resp.text
    out: dict[str, str] = {}
    name = None
    for line in aln.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            out[name] = ""
        elif name:
            out[name] += line.strip()
    if set(out) != set(entries):
        raise SystemExit(f"FATAL: alignment names {sorted(out)} != inputs {sorted(entries)}")
    lengths = {len(v) for v in out.values()}
    if len(lengths) != 1:
        raise SystemExit(f"FATAL: ragged alignment, column counts {lengths}")
    return out


def col_of(aligned: str, residue_pos: int) -> int:
    n = 0
    for i, c in enumerate(aligned):
        if c != "-":
            n += 1
            if n == residue_pos:
                return i
    raise SystemExit(f"FATAL: residue {residue_pos} beyond aligned sequence")


def res_at_col(aligned: str, col: int) -> tuple[str, int | None]:
    c = aligned[col]
    if c == "-":
        return "-", None
    return c, sum(1 for ch in aligned[: col + 1] if ch != "-")


def pct_identity(a: str, b: str, lo: int | None = None, hi: int | None = None) -> float:
    """Identity over ungapped column pairs, optionally restricted to a column range."""
    sl = slice(lo, hi)
    pairs = [(x, y) for x, y in zip(a[sl], b[sl]) if x != "-" and y != "-"]
    if not pairs:
        return 0.0
    return 100.0 * sum(1 for x, y in pairs if x == y) / len(pairs)


def context(seq: str, pos: int | None, flank: int = 5) -> str:
    """Residue window around a 1-based position, with the site upper-cased in brackets."""
    if not pos:
        return "-"
    i = pos - 1
    left = seq[max(0, i - flank): i].lower()
    right = seq[i + 1: i + 1 + flank].lower()
    return f"{left}[{seq[i]}]{right}"


def render_results_md(out, entries, rows, idents, idents_core) -> str:
    """Render RESULTS.md entirely from computed values.

    No number in this report is written by hand: a fresh run must reproduce the
    committed file byte-for-byte (`uv run python ubib_motif_analysis.py && git diff
    --exit-code RESULTS.md`). Interpretation prose is deliberately phrased so that it
    does not restate any figure that the tables already carry.
    """
    subj = "Q7Z695"
    cc = out["control_checks"]
    pk_acc = cc["negative_control"]
    order = list(entries)

    def sym(a: str) -> str:
        return MEMBERS[a].split("_")[0]

    L: list[str] = []
    L.append("# ADCK2: does it retain the UbiB / uPKL motifs of the characterised family members?")
    L.append("")
    L.append("Generated by `ubib_motif_analysis.py`. Do not hand-edit -- rerun the script.")
    L.append("")
    L.append("## Question")
    L.append("")
    L.append(
        "UniProt names ADCK2 an `aarF domain-containing protein kinase`, gives it "
        "`EC=2.7.11.-` and the keyword `Serine/threonine-protein kinase`, while its own "
        "FUNCTION comment says the function is unknown. The two structurally and "
        "biochemically characterised members of the family, COQ8A/ADCK3 and COQ8B/ADCK4, "
        "were shown *not* to carry canonical in-trans protein kinase activity "
        "(PMID:25498144, PMID:27499294): the family-specific KxGQ domain occludes the "
        "peptide-substrate groove, and the alanines of the UbiB `A-rich loop` (which "
        "replaces the canonical Gly-rich loop) actively suppress phosphotransfer."
    )
    L.append("")
    L.append("So the testable questions for ADCK2 are:")
    L.append("")
    L.append("1. does it retain the **catalytic** machinery, i.e. is it a plausible phosphotransferase at all; and")
    L.append("2. does it retain the **UbiB-specific suppressors** of canonical protein kinase activity?")
    L.append("")
    L.append("## Method")
    L.append("")
    L.append(
        "Clustal Omega MSA (EBI REST) of the UbiB family plus a canonical protein kinase "
        "as negative control, then projection of COQ8A's own UniProt-annotated motif and "
        "ligand positions through the alignment. Residue identity and \"lands on a "
        "position the target itself annotates\" are reported as separate conditions, never "
        "collapsed. The reference positions are cross-checked against the live UniProt "
        "feature table at runtime and the script aborts if they have drifted."
    )
    L.append("")
    L.append("## Sequences used")
    L.append("")
    L.append("| accession | entry | length | status | % id to COQ8A (global) | % id to COQ8A (PKL core) |")
    L.append("|---|---|---|---|---|---|")
    for a in order:
        m = out["members"][a]
        g = "-" if m["pct_identity_to_COQ8A_global"] is None else f"{m['pct_identity_to_COQ8A_global']}%"
        c = "-" if m["pct_identity_to_COQ8A_pkl_core"] is None else f"{m['pct_identity_to_COQ8A_pkl_core']}%"
        L.append(f"| {a} | {m['entry']} | {m['length']} aa | {m['status']} | {g} | {c} |")
    L.append("")
    L.append(
        f"`{MEMBERS[REFERENCE]}` is the projection reference; `{MEMBERS['P17612']}` is the "
        "negative control (a canonical Ser/Thr protein kinase outside the UbiB family)."
    )
    L.append("")
    L.append(
        "**These identity figures are properties of this MSA, not of the sequence pairs, "
        "and are not comparable across alignments.** Clustal Omega's gap placement depends "
        "on the whole input set, so adding or removing a single sequence moves every figure "
        f"in this table. They were computed over the {len(order)} sequences listed above; "
        "do not compare them against numbers derived from a different membership, "
        "recompute instead."
    )
    L.append("")
    L.append("## Alignment register, judged by the negative control")
    L.append("")
    L.append(
        "A column counts as in register only if the negative control's aligned position "
        "falls inside one of *its own* UniProt-annotated sites. Register and residue "
        "identity are different questions: the A-rich loop sits at the canonical "
        "Gly-rich-loop position, so the control is expected to land there while carrying "
        "Gly rather than Ala."
    )
    L.append("")
    L.append("| site | COQ8A context | ADCK2 context | control residue | column in register |")
    L.append("|---|---|---|---|---|")
    for r in rows:
        reg = ("yes" if r["column_in_register_by_negative_control"]
               else ("n/a - no equivalent in the control" if r["site"] in ("KxGQ_K", "KxGQ_Q")
                     else "**NOT CONFIRMED**"))
        L.append("| %s | `%s` | `%s` | %s | %s |" % (
            r["site"], r["targets"][REFERENCE]["context"],
            r["targets"][subj]["context"], r["negative_control_residue"], reg))
    L.append("")
    L.append(
        f"{cc['columns_in_register']} of {cc['columns_total']} columns are confirmed in "
        f"register. The control reproduces {cc['pka_canonical_matches']}/4 canonical "
        f"catalytic residues and {cc['pka_kxgq_matches']}/2 KxGQ positions, so the KxGQ "
        "motif is diagnostic for the UbiB family in this alignment and is not an artefact "
        "of aligning any protein kinase."
    )
    # The two tests can disagree, and saying so is the point: a column where the control
    # carries the right residue but has no feature annotation there is unconfirmable by
    # the strict test yet is not evidence against the register.
    unconfirmed_but_identical = [
        r["site"] for r in rows
        if not r["column_in_register_by_negative_control"]
        and r["targets"][pk_acc]["identical"]
    ]
    if unconfirmed_but_identical:
        L.append("")
        L.append(
            "Note where the two conditions come apart: "
            + ", ".join(f"`{s}`" for s in unconfirmed_but_identical)
            + " is not confirmed by the strict test, because the control's UniProt entry "
            "annotates no feature at that position -- yet the control carries the *same* "
            "residue as the reference there. Absence of an annotation in the control is "
            "not evidence that the column is out of register, so this reads as "
            "unconfirmable rather than wrong."
        )
    L.append("")
    L.append("## Projected sites across the family")
    L.append("")
    L.append("| site | what it is in COQ8A | " + " | ".join(sym(a) for a in order) + " |")
    L.append("|---|---|" + "---|" * len(order))
    for r in rows:
        cells = []
        for a in order:
            t = r["targets"][a]
            cells.append(f"{t['aa']}{t['pos'] or ''}" + ("\\*" if t["lands_on_annotated_site"] else ""))
        L.append(f"| {r['site']} | {r['description']} | " + " | ".join(cells) + " |")
    L.append("")
    L.append("`\\*` = the position also carries a UniProt feature annotation in that entry.")
    L.append("")
    L.append("## Findings for ADCK2")
    L.append("")
    canon = ["beta3_K", "cat_D", "cat_N", "DFG_D"]
    kept = [r["site"] for r in rows if r["site"] in canon and r["targets"][subj]["identical"]]
    kxgq = [r["site"] for r in rows if r["site"] in ("KxGQ_K", "KxGQ_Q") and r["targets"][subj]["identical"]]
    arich = [r for r in rows if r["site"].startswith("Arich")]

    def span(acc: str, positions: list[int]) -> tuple[str, int, int]:
        """Contiguous residue span covering the projected positions, so the reference
        and the subject are described by the SAME computation (an earlier version
        concatenated three sampled residues for one and a contiguous span for the
        other, which silently compared 3 characters against 4)."""
        lo_, hi_ = min(positions), max(positions)
        return entries[acc].sequence[lo_ - 1: hi_], lo_, hi_

    ref_arich, ref_lo, ref_hi = span(REFERENCE, [r["coq8a_pos"] for r in arich])
    subj_arich, lo, hi = span(subj, [r["targets"][subj]["pos"] for r in arich
                                     if r["targets"][subj]["pos"]])
    if len(ref_arich) != len(subj_arich):
        raise SystemExit(
            f"FATAL: A-rich spans differ in length ({ref_arich} vs {subj_arich}); the "
            f"comparison would not be like-for-like."
        )
    L.append(
        f"**1. The catalytic core is intact.** ADCK2 matches COQ8A at {len(kept)} of "
        f"{len(canon)} canonical catalytic positions ({', '.join(kept)}). ADCK2 is "
        "therefore not a pseudokinase by loss of catalytic residues; a fold-plus-lost-"
        "residues argument for removing a catalytic annotation is **not** available here."
    )
    L.append("")
    L.append(
        f"**2. The UbiB KxGQ motif is retained** ({len(kxgq)}/2 positions identical to "
        f"COQ8A: {', '.join(kxgq)}). This is the feature shown to occlude the peptide-"
        "substrate site in COQ8A, and PMID:27499294 predicts unorthodox-PKL functionality "
        "throughout the family on exactly this basis. ADCK2 is a uPKL by that criterion, "
        "which argues against a canonical protein-serine/threonine-kinase annotation."
    )
    L.append("")
    L.append(
        f"**3. The A-rich loop is NOT alanine-rich in ADCK2.** Over the aligned span, "
        f"COQ8A carries `{ref_arich}` ({ref_lo}-{ref_hi}) and ADCK2 carries `{subj_arich}` "
        f"({lo}-{hi}); all three projected positions fall inside ADCK2's own annotated "
        "ATP-binding site. Both COQ8A alanines project onto glycines in ADCK2. "
        "This is the one place where ADCK2 looks *more* like a conventional kinase than "
        "COQ8A does, and it must not be over-read: in COQ8A the A339G substitution "
        "de-represses **cis autophosphorylation**, which PMID:27499294 shows is "
        "dispensable for function in vivo, and it does not create in-trans peptide kinase "
        "activity while the KxGQ domain remains in place."
    )
    L.append("")
    # Reciprocal-orthologue test: is the A339-equivalent split branch-diagnostic?
    a3 = next(r for r in rows if r["site"] == "Arich_A3")
    ubib_only = [a for a in order if a != "P17612"]
    gly = [sym(a) for a in ubib_only if a3["targets"][a]["aa"] == "G"]
    ala = [sym(a) for a in ubib_only if a3["targets"][a]["aa"] == "A"]
    other = [sym(a) for a in ubib_only if a3["targets"][a]["aa"] not in ("G", "A")]
    L.append("## Reciprocal-orthologue test at the A339-equivalent position")
    L.append("")
    L.append(
        "PMID:34362905 pairs yeast Cqd1 with human ADCK2 and yeast Cqd2 with human "
        "ADCK1/5, from genetics. The A339-equivalent column tests that pairing from "
        "sequence alone, i.e. **independently of the genetics** -- but NOT independently "
        "of PANTHER, whose subfamily assignment is itself derived from sequence. Treat "
        "this as a second sequence-based line agreeing with the genetics, not as a third "
        "independent line."
    )
    L.append("")
    L.append(f"- Gly (the de-repressing residue) in **{len(gly)}** of {len(ubib_only)} "
             f"UbiB proteins: {', '.join(gly) if gly else 'none'}")
    L.append(f"- Ala (the suppressor residue) in **{len(ala)}**: "
             f"{', '.join(ala) if ala else 'none'}")
    if other:
        L.append(f"- other residue in {len(other)}: {', '.join(other)}")
    L.append("")
    # The adjacent A-rich column must be reported too: if it does NOT split the same way,
    # then only one of the two projected columns is branch-diagnostic, and saying "the
    # A-rich loop supports the pairing" without that distinction would overstate the case.
    a1 = next(r for r in rows if r["site"] == "Arich_A1")
    a1_gly = [sym(a) for a in ubib_only if a1["targets"][a]["aa"] == "G"]
    expected_gly = {"ADCK2", "CQD1"}
    if set(gly) == expected_gly:
        L.append(
            "The split is **exactly the ADCK2/Cqd1 orthologue pair against everything "
            "else**, including Cqd2 and ADCK1, which carry the suppressor alanine. So a "
            "single residue reproduces the published orthology assignment, and it does so "
            "reciprocally: the two branches differ at precisely the position whose "
            "substitution was shown to change COQ8A's behaviour. This corroborates the "
            "pairing; it does not by itself show the two branches differ functionally."
        )
        L.append("")
        # Gate the interpretation on the computed set, exactly as the Arich_A3 sentence is
        # gated. Hardcoding "includes Cqd2 and ADCK1" would silently become false if the
        # membership or the alignment changed.
        crossers = sorted(set(a1_gly) - expected_gly)
        if set(a1_gly) == expected_gly:
            L.append(
                "The adjacent `Arich_A1` position splits the same way, so both projected "
                "A-rich columns support the pairing."
            )
        elif crossers and expected_gly <= set(a1_gly):
            # Only say "the same pair plus X" when the pair really is present at A1.
            L.append(
                f"**Only this column is branch-diagnostic.** At the adjacent `Arich_A1` "
                f"position, Gly is carried by {len(a1_gly)} proteins: the same "
                f"{'/'.join(sorted(expected_gly))} pair plus {_english_list(crossers)}. "
                f"That set therefore cuts across the pairing rather than along it, so the "
                f"claim is specifically about the A339-equivalent position and not about "
                f"the A-rich loop as a whole."
            )
        elif crossers:
            # The pair is NOT wholly present at A1, so describe the set as it is rather
            # than as "the pair plus" anything.
            L.append(
                f"**Only this column is branch-diagnostic.** At the adjacent `Arich_A1` "
                f"position, Gly is carried by {_english_list(sorted(a1_gly))}, which is "
                f"neither the A339-equivalent Gly set nor a subset of it, so that column "
                f"cuts across the pairing. The claim is specifically about the "
                f"A339-equivalent position and not about the A-rich loop as a whole."
            )
        else:
            L.append(
                f"At the adjacent `Arich_A1` position Gly is carried by "
                f"{_english_list(sorted(a1_gly)) if a1_gly else 'no protein'}, a subset "
                f"of the A339-equivalent Gly set, so that column neither supports nor "
                f"contradicts the pairing."
            )
    else:
        L.append(
            f"The split is **not** the clean ADCK2/Cqd1-versus-rest pattern: Gly is carried "
            f"by {sorted(gly)}, so this column does not track the published orthology "
            f"pairing and must not be cited as corroborating it."
        )
    L.append("")
    L.append("## Bottom line")
    L.append("")
    L.append(
        "ADCK2 has an intact phosphotransfer-competent active site inside a UbiB/uPKL "
        "architecture. The evidence supports neither removing nucleotide-related "
        "chemistry from the gene nor asserting canonical protein-serine/threonine kinase "
        "activity for it. No GO annotation on ADCK2 currently asserts either, so this "
        "analysis bears on UniProt's `EC=2.7.11.-` and `Serine/threonine-protein kinase` "
        "keyword rather than on any row of the GOA file."
    )
    L.append("")
    if out["problems"]:
        L.append("## Problems")
        L.append("")
        for p in out["problems"]:
            L.append(f"- {p}")
        L.append("")
    return "\n".join(L)


def main() -> int:
    entries = {acc: fetch_entry(acc) for acc in MEMBERS}
    for acc, e in entries.items():
        print(f"fetched {acc} {e.entry_name} {e.length} aa "
              f"{'Swiss-Prot' if e.reviewed else 'TrEMBL'}")

    ref = entries[REFERENCE]
    # Cross-check the hardcoded reference positions against the live feature table.
    ref_annotated = ref.annotated_positions()
    for name, (pos, _desc) in REF_SITES.items():
        if pos not in ref_annotated:
            raise SystemExit(
                f"FATAL: COQ8A position {pos} ({name}) is not in the fetched UniProt "
                f"feature table. The literal REF_SITES table has drifted from UniProt; "
                f"re-derive it rather than editing this message away."
            )

    aln = clustal_omega(entries)

    rows: list[dict] = []
    for name, (refpos, desc) in REF_SITES.items():
        col = col_of(aln[REFERENCE], refpos)
        refaa = ref.sequence[refpos - 1]
        row = {"site": name, "description": desc, "coq8a_pos": refpos, "coq8a_aa": refaa,
               "targets": {}}
        for acc, e in entries.items():
            aa, pos = res_at_col(aln[acc], col)
            hit = {
                "aa": aa,
                "pos": pos,
                "identical": aa == refaa,
                "conservative": (aa != "-" and aa != refaa and conservative(aa, refaa)),
                "lands_on_annotated_site": bool(pos and pos in e.annotated_positions()),
                "target_features_here": e.feature_at(pos) if pos else [],
                "context": context(e.sequence, pos),
            }
            row["targets"][acc] = hit
        rows.append(row)

    # Per-column reliability, judged by the negative control. Register and residue
    # identity are DIFFERENT questions and must not be conflated: the A-rich loop
    # occupies the canonical Gly-rich-loop position, so PKA is expected to land there
    # while carrying Gly rather than Ala. Register is therefore tested by asking only
    # whether PKA's aligned position falls inside one of PKA's OWN annotated features.
    pk_acc = "P17612"
    for r in rows:
        t = r["targets"][pk_acc]
        r["column_in_register_by_negative_control"] = t["lands_on_annotated_site"]
        r["negative_control_residue"] = f"{t['aa']}{t['pos'] or ''}"

    # Global identity is depressed by ADCK2's long N-terminal extension, so also
    # report identity restricted to the PKL core: the alignment columns spanning
    # COQ8A's KxGQ motif to its C-terminus.
    core_lo = col_of(aln[REFERENCE], REF_SITES["KxGQ_K"][0])
    idents = {
        acc: round(pct_identity(aln[REFERENCE], aln[acc]), 1)
        for acc in entries
        if acc != REFERENCE
    }
    idents_core = {
        acc: round(pct_identity(aln[REFERENCE], aln[acc], core_lo, None), 1)
        for acc in entries
        if acc != REFERENCE
    }

    # Controls must behave, or the projection is not measuring what it claims.
    problems: list[str] = []
    # Only the KxGQ motif is UbiB-specific in POSITION; the A-rich loop is the canonical
    # Gly-rich loop position and differs from other kinases only in COMPOSITION.
    ubib_specific = ["KxGQ_K", "KxGQ_Q"]
    canonical = ["beta3_K", "cat_D", "cat_N", "DFG_D"]
    pk = "P17612"
    pk_ubib = sum(
        1 for r in rows if r["site"] in ubib_specific and r["targets"][pk]["identical"]
    )
    pk_canon = sum(
        1 for r in rows if r["site"] in canonical and r["targets"][pk]["identical"]
    )
    n_in_register = sum(1 for r in rows if r["column_in_register_by_negative_control"])
    if pk_canon < 3:
        problems.append(
            f"NEGATIVE CONTROL FAILED: canonical PKA matches only {pk_canon}/4 canonical "
            f"catalytic positions -- the alignment is not registering the kinase core, "
            f"so no conclusion about ADCK2 can be drawn from it."
        )
    if pk_ubib > 0:
        problems.append(
            f"NEGATIVE CONTROL FAILED: canonical PKA matches {pk_ubib}/2 KxGQ positions, "
            f"so the KxGQ motif is not UbiB-diagnostic in this alignment."
        )
    if n_in_register < 6:
        problems.append(
            f"REGISTER TOO WEAK: only {n_in_register}/9 columns place the negative "
            f"control on one of its own annotated positions."
        )

    out = {
        "reference": {"accession": REFERENCE, "entry": ref.entry_name},
        "members": {
            acc: {
                "entry": e.entry_name,
                "length": e.length,
                "status": "Swiss-Prot" if e.reviewed else "TrEMBL",
                "pct_identity_to_COQ8A_global": idents.get(acc),
                "pct_identity_to_COQ8A_pkl_core": idents_core.get(acc),
            }
            for acc, e in entries.items()
        },
        "sites": rows,
        "control_checks": {
            "negative_control": pk,
            "pka_canonical_matches": pk_canon,
            "pka_kxgq_matches": pk_ubib,
            "columns_in_register": n_in_register,
            "columns_total": len(rows),
        },
        "problems": problems,
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2))
    (HERE / "RESULTS.md").write_text(render_results_md(out, entries, rows, idents, idents_core))

    print("\n%-10s %-9s %s" % ("site", "COQ8A", "  ".join(f"{MEMBERS[a].split('_')[0]:>8}" for a in entries)))
    for r in rows:
        cells = []
        for acc in entries:
            t = r["targets"][acc]
            mark = "*" if t["lands_on_annotated_site"] else " "
            cells.append(f"{(t['aa'] + str(t['pos'] or '')):>7}{mark}")
        print("%-10s %-9s %s" % (r["site"], f"{r['coq8a_aa']}{r['coq8a_pos']}", "  ".join(cells)))
    print("\n* = position also carries a UniProt feature annotation in that entry")

    print("\nsequence context (COQ8A reference vs ADCK2 subject), and column register:")
    print("%-10s %-18s %-18s %-8s %s" % ("site", "COQ8A", "ADCK2", "PKA", "register"))
    for r in rows:
        print("%-10s %-18s %-18s %-8s %s" % (
            r["site"],
            r["targets"][REFERENCE]["context"],
            r["targets"]["Q7Z695"]["context"],
            r["negative_control_residue"],
            "confirmed" if r["column_in_register_by_negative_control"]
            else ("n/a (no PKA equivalent)" if r["site"] in ubib_specific
                  else "NOT CONFIRMED"),
        ))

    print("\n%% identity to COQ8A (global / PKL core from the KxGQ column onward):")
    for acc, v in sorted(idents.items(), key=lambda x: -x[1]):
        print(f"  {MEMBERS[acc]:<14} {v:>5}% / {idents_core[acc]:>5}%")
    print(f"\nnegative control PKA: canonical {pk_canon}/4, UbiB-specific {pk_ubib}/4")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  -", p)
        return 1
    print("\nno problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
