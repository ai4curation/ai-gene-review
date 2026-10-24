"""Are AGGF1's FHA and G-patch domains intact at the positions that matter?

The gene symbol "Angiogenic factor with G-patch and FHA domains 1" makes three
independent claims. This script tests the two domain claims at residue level,
because a domain's NAME is not an activity and an InterPro hit is not a
measurement.

Both domains are tested the same way, twice over:

1. **Computed conservation.** Every reviewed human protein whose UniProt entry
   carries an annotated domain of the same type is pulled live, its domain
   sequence aligned to AGGF1's, and a column called conserved when at least a
   stated fraction of the panel agrees. The threshold is reported next to the
   observed distribution rather than asserted, and the panel is derived from an
   InterPro cross-reference query, never hand-listed.
2. **Literature anchors** (FHA only). Phosphothreonine recognition by an FHA
   domain requires an Arg in the beta3-beta4 loop preceded by a Gly, a Ser in
   beta4-beta5, and an Asn in beta6-beta7 (Durocher et al. 2000, PMID:11106755).
   Positions are taken from two structurally characterised FHA domains
   (S. cerevisiae Rad53 FHA1, human CHEK2) and **verified against the live
   UniProt sequence before use**: if the residue at a stated position is not the
   expected one, the anchor is wrong and the script aborts.

Two rules govern the transfer, and dropping either one manufactures results:

* Alignment is **domain-local**, never global over full-length sequences. An
  earlier version of this script globally aligned 714-aa AGGF1 to 543-aa CHEK2
  and mapped every CHEK2 anchor into AGGF1's residues 112-169 -- nowhere near
  AGGF1's FHA domain at 434-487. That produced a clean-looking 0/8 "the FHA is
  degenerate" result which was pure alignment noise.
* A transfer counts only if the aligned residue is **identical** AND the aligned
  position **lands inside AGGF1's own annotated domain** (plus the same flank
  used for every panel member, since UniProt's PROSITE-profile boundary is a
  core rather than the structural domain). Amino-acid identity alone
  manufactures conserved sites out of noise.

A retained residue is NOT evidence of activity. This script answers "is the site
present", which bounds what the literature could still show; it never licenses a
molecular function on its own.

Run: uv run python domain_residues.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

from uniprot import _cached_get, uniprot_entry

SUBJECT = "Q8N302"
FLANK = 30  # residues added on each side of every annotated domain, panel-wide
CONSERVED_MIN = 0.80

# Literature-sourced FHA phosphothreonine-recognition residues. Every one is
# re-tested against the live sequence below; a mismatch is a hard error.
FHA_ANCHORS = {
    "P22216": ("Rad53 FHA1 (S. cerevisiae)", {69: "G", 70: "R", 85: "S", 107: "N"}),
    "O96017": ("CHEK2 (human)", {116: "G", 117: "R", 140: "S", 166: "N"}),
}

PANELS = {
    "FHA": {"interpro": "IPR000253", "match": "fha"},
    "G-patch": {"interpro": "IPR000467", "match": "patch"},
}


def aligner(mode: str) -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = mode
    return a


def domain_spans(acc: str, match: str) -> list[tuple[int, int]]:
    entry = uniprot_entry(acc)
    return [
        (f["location"]["start"]["value"], f["location"]["end"]["value"])
        for f in entry["features"]
        if f["type"] == "Domain" and match in (f.get("description") or "").lower()
    ]


def sequence(acc: str) -> str:
    return uniprot_entry(acc)["sequence"]["value"]


def window(seq: str, start: int, end: int) -> tuple[str, int]:
    """Domain sequence with FLANK on each side, plus its 1-based offset."""
    lo = max(1, start - FLANK)
    hi = min(len(seq), end + FLANK)
    return seq[lo - 1 : hi], lo


def transfer_local(src: str, dst: str, src_pos0: int) -> int | None:
    """0-based index in `dst` locally aligned to 0-based `src_pos0`, or None."""
    alns = aligner("local").align(src, dst)
    if len(alns) == 0:
        return None
    aln = alns[0]
    for (s0, s1), (d0, d1) in zip(aln.aligned[0], aln.aligned[1]):
        if s0 <= src_pos0 < s1:
            return d0 + (src_pos0 - s0)
    return None


def panel(interpro: str, match: str) -> list[tuple[str, str, str, int]]:
    """(accession, gene, domain+flank sequence, 1-based offset) for reviewed human hits."""
    q = f"(xref:interpro-{interpro}) AND (organism_id:9606) AND (reviewed:true)"
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query={q.replace(' ', '%20').replace(':', '%3A')}"
        "&fields=accession,gene_primary&size=200&format=json"
    )
    hits = json.loads(_cached_get(url, f"panel_{interpro}"))["results"]
    out = []
    for h in hits:
        acc = h["primaryAccession"]
        if acc == SUBJECT:
            continue
        gene = (h.get("genes") or [{}])[0].get("geneName", {}).get("value", acc)
        spans = domain_spans(acc, match)
        if not spans:
            continue
        seq = sequence(acc)
        for s, e in spans:
            w, off = window(seq, s, e)
            out.append((acc, gene, w, off))
    return out


def conservation(kind: str, cfg: dict) -> dict:
    subj_seq = sequence(SUBJECT)
    spans = domain_spans(SUBJECT, cfg["match"])
    if len(spans) != 1:
        raise SystemExit(f"AGGF1 has {len(spans)} {kind} domains; expected exactly 1")
    dstart, dend = spans[0]
    subj_win, subj_off = window(subj_seq, dstart, dend)
    print(f"=== {kind}: AGGF1 {SUBJECT} annotated domain {dstart}-{dend} "
          f"({dend - dstart + 1} aa); aligned window {subj_off}-{subj_off + len(subj_win) - 1} "
          f"(+/-{FLANK} flank) ===")
    print(f"    domain: {subj_seq[dstart - 1 : dend]}")
    print()

    members = panel(cfg["interpro"], cfg["match"])
    if len(members) < 5:
        raise SystemExit(f"{kind} panel has only {len(members)} members -- query broken?")
    genes = sorted({g for _, g, _, _ in members})
    print(f"panel: {len(members)} annotated {kind} domain(s) across {len(genes)} reviewed "
          f"human proteins (AGGF1 excluded): {', '.join(genes)}")
    print()

    census: dict[int, Counter[str]] = {}
    al = aligner("local")
    for _acc, _gene, seq, _off in members:
        alns = al.align(subj_win, seq)
        if len(alns) == 0:
            continue
        aln = alns[0]
        for (s0, s1), (d0, d1) in zip(aln.aligned[0], aln.aligned[1]):
            for k in range(s1 - s0):
                census.setdefault(subj_off + s0 + k, Counter())[seq[d0 + k]] += 1

    n = len(members)
    fracs = sorted((max(c.values()) / n for c in census.values() if c), reverse=True)
    print(f"observed per-column agreement, top 12: {', '.join(f'{f:.2f}' for f in fracs[:12])}")
    conserved, matched = [], 0
    for pos in sorted(census):
        c = census[pos]
        res, cnt = c.most_common(1)[0]
        if cnt / n < CONSERVED_MIN:
            continue
        own = subj_seq[pos - 1]
        in_dom = dstart <= pos <= dend
        conserved.append({"pos": pos, "consensus": res, "frac": cnt / n,
                          "aggf1": own, "match": own == res, "in_annotated_domain": in_dom})
        matched += own == res
    print(f"threshold {CONSERVED_MIN:.2f} -> {len(conserved)} conserved column(s)")
    for c in conserved:
        print(f"    position {c['pos']:<4d} panel consensus {c['consensus']} "
              f"({c['frac']:.0%} of {n})  AGGF1 has {c['aggf1']}  "
              f"{'MATCH' if c['match'] else 'MISMATCH'}  "
              f"inside_annotated_domain={c['in_annotated_domain']}")
    print()
    print(f"{kind} CONSERVATION VERDICT: AGGF1 matches {matched}/{len(conserved)} of the "
          f"columns this panel conserves at >={CONSERVED_MIN:.0%}.")
    print()
    return {"domain": [dstart, dend], "panel_members": n, "panel_genes": len(genes),
            "conserved": len(conserved), "matched": matched, "columns": conserved}


def fha_anchors() -> dict:
    subj_seq = sequence(SUBJECT)
    dstart, dend = domain_spans(SUBJECT, "fha")[0]
    subj_win, subj_off = window(subj_seq, dstart, dend)
    lo, hi = dstart - FLANK, dend + FLANK

    print("=== FHA: literature anchor transfer (domain-local alignment) ===")
    results = []
    for acc, (label, anchors) in FHA_ANCHORS.items():
        seq = sequence(acc)
        a_start, a_end = domain_spans(acc, "fha")[0]
        for pos, expect in anchors.items():
            if seq[pos - 1] != expect:
                raise SystemExit(
                    f"{acc} ({label}): position {pos} is {seq[pos - 1]!r}, expected "
                    f"{expect!r}. The literature anchor is wrong or the sequence "
                    "changed -- refusing to transfer it."
                )
        src_win, src_off = window(seq, a_start, a_end)
        print(f"--- {label} {acc}, FHA {a_start}-{a_end}; all {len(anchors)} stated "
              f"residues verified against the live sequence")
        for pos, expect in sorted(anchors.items()):
            if not (src_off <= pos < src_off + len(src_win)):
                raise SystemExit(f"{acc}: anchor {pos} falls outside its own aligned window")
            t0 = transfer_local(src_win, subj_win, pos - src_off)
            if t0 is None:
                print(f"    {expect}{pos:<4d} -> aligns to a GAP in AGGF1")
                results.append({"anchor": f"{label} {expect}{pos}", "target_pos": None,
                                "target_res": "", "identical": False,
                                "in_window": False, "in_annotated_domain": False})
                continue
            t = subj_off + t0
            res = subj_seq[t - 1]
            in_dom = dstart <= t <= dend
            in_win = lo <= t <= hi
            print(f"    {expect}{pos:<4d} -> AGGF1 {res}{t:<4d}  identical={res == expect}  "
                  f"inside_annotated_FHA({dstart}-{dend})={in_dom}  "
                  f"inside_window({lo}-{hi})={in_win}")
            results.append({"anchor": f"{label} {expect}{pos}", "target_pos": t,
                            "target_res": res, "identical": res == expect,
                            "in_window": in_win, "in_annotated_domain": in_dom})
        print()

    strict = [r for r in results if r["identical"] and r["in_annotated_domain"]]
    loose = [r for r in results if r["identical"] and r["in_window"]]
    print(f"FHA ANCHOR VERDICT: {len(strict)}/{len(results)} transfers retained under the "
          f"strict rule (identical residue inside the annotated {dstart}-{dend} core); "
          f"{len(loose)}/{len(results)} inside the +/-{FLANK} window.")
    print("                    A retained site bounds what is possible. It does NOT show")
    print("                    that AGGF1 binds a phosphopeptide.")
    print()
    return {"anchors": results, "retained_strict": len(strict),
            "retained_window": len(loose), "total": len(results)}


def gpatch_claims_vs_nkrf(columns: list[dict]) -> list[dict]:
    """Residue-claim rows for the conserved G-patch columns, anchored on NKRF.

    NKRF is the anchor because its G-patch is the one resolved in complex with
    DHX15 (PMID:32179686), so "AGGF1 has the residue NKRF has here" is a claim
    about a position whose role is structurally known rather than merely
    conserved. Both positions are emitted in each protein's own numbering, which
    is what makes the claim checkable without re-running this alignment.
    """
    subj_seq = sequence(SUBJECT)
    gs, ge = domain_spans(SUBJECT, "patch")[0]
    subj_win, subj_off = window(subj_seq, gs, ge)
    nkrf = "O15226"
    nseq = sequence(nkrf)
    ns, ne = domain_spans(nkrf, "patch")[0]
    nwin, noff = window(nseq, ns, ne)

    print(f"=== G-patch conserved columns mapped onto NKRF {nkrf} (G-patch {ns}-{ne}) ===")
    rows = []
    for c in columns:
        if not c["match"]:
            continue
        t0 = transfer_local(subj_win, nwin, c["pos"] - subj_off)
        if t0 is None:
            print(f"    AGGF1 {c['aggf1']}{c['pos']} -> GAP in NKRF")
            continue
        npos = noff + t0
        nres = nseq[npos - 1]
        print(f"    AGGF1 {c['aggf1']}{c['pos']:<4d} <- NKRF {nres}{npos:<4d}  "
              f"identical={nres == c['aggf1']}  "
              f"inside_NKRF_G-patch={ns <= npos <= ne}")
        rows.append({"aggf1_pos": c["pos"], "aggf1_res": c["aggf1"],
                     "nkrf_pos": npos, "nkrf_res": nres,
                     "identical": nres == c["aggf1"],
                     "inside_nkrf_domain": ns <= npos <= ne})
    n_ok = sum(1 for r in rows if r["identical"] and r["inside_nkrf_domain"])
    print(f"    {n_ok}/{len(columns)} conserved columns retained against the NKRF anchor.")
    print()
    return rows


def main() -> None:
    out = {"flank": FLANK, "conserved_min": CONSERVED_MIN}
    for kind, cfg in PANELS.items():
        out[kind] = conservation(kind, cfg)
    out["gpatch_vs_nkrf"] = gpatch_claims_vs_nkrf(out["G-patch"]["columns"])
    out["fha_anchors"] = fha_anchors()

    def jsonable(o):
        """Biopython alignment indices are numpy int64. Coerce positions to int
        rather than letting a `default=float` fallback turn residue positions
        into 631.0 -- a downstream audit matching on 'G631' then fails, and the
        failure looks like a missing claim rather than a serialisation bug."""
        if isinstance(o, dict):
            return {k: jsonable(v) for k, v in o.items()}
        if isinstance(o, list):
            return [jsonable(v) for v in o]
        if isinstance(o, bool):
            return o
        if hasattr(o, "item"):  # numpy scalar
            o = o.item()
        if isinstance(o, float) and o.is_integer():
            return int(o)
        return o

    Path(__file__).with_name("domain_residues.json").write_text(
        json.dumps(jsonable(out), indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
