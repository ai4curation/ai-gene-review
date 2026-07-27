#!/usr/bin/env python3
"""Is AGFG2's ArfGAP catalytic machinery intact, and is AGFG1 really its paralogue?

Two questions the gene's *name* ("Arf-GAP domain and FG repeat-containing protein 2")
asserts but does not establish.

TWO residues are tested, not one, and they answer oppositely
------------------------------------------------------------
* the **catalytic arginine** (``C-x2-C-x16-C-x2-C-x4-R``), and
* the **Arf-contacting aspartate** that PMID:23433073 (Schlacht et al. 2013)
  identifies as the residue "*that Ismail, et. al (2010) show contacting the
  glutamine in the Arf (Arf6-Q67) that is essential to hydrolysis*", and reports
  as absent from 38 of 40 AGFG sequences.

Testing only the arginine would have produced the *opposite* conclusion from
testing both, which is why the second residue is not an optional refinement.

Method, and why each step is there
----------------------------------
The two residues are located by **two different methods**, because only one of them
can be derived:

1. **The arginine is derived.**  It sits five residues past the fourth
   zinc-coordinating cysteine, so the script locates the motif
   ``C-x2-C-x16-C-x2-C-x4-R`` by regex inside each protein's own UniProt
   ``Zinc finger`` window and reads off the position.  Validated against an external
   literature anchor: PMID:34369554 names ``AGFG2[R75Q]`` as its GAP-dead mutant, so
   the derivation applied to O95081 must return **75** or the script raises.
2. **The aspartate is transferred by alignment, not derived.**  Its position is an
   *input constant* — ``ASP_CONTROL = ("Q8TDY4", 484)``, the ``D484`` that
   PMID:23433073 names in the ASAP3 structure.  What the script verifies is that
   residue 484 of Q8TDY4 really is an Asp, that it falls inside the annotated
   Arf-GAP domain, and that the MAFFT alignment column holding it holds ``D`` for
   ASAP3; every other protein's residue is then read from that same column.  So this
   is *assert-and-transfer*, and it is labelled as such rather than as a second
   derivation.

   **Tried and refused:** an earlier version treated the aspartate as derivable at a
   fixed offset from the zinc finger — the second of the four residues between the
   fourth cysteine and the arginine.  Its own control refused that: ASAP3 came out at
   466, not 484 (see ``probe_asap3.py``).  The aspartate is 15 residues C-terminal of
   the arginine *in ASAP3*, and indels move it between subfamilies, so no fixed offset
   can be right across the family.  The refutation is kept here because this docstring
   is the first thing a re-runner reads.
3. **Reciprocal check:** a MAFFT alignment of the UniProt ``Arf-GAP`` domains must
   place every derived arginine in the *same alignment column*, and the script raises
   if ASAP3's arginine does not co-align with AGFG2's.  Residue identity alone
   manufactures matches out of alignment noise; requiring co-alignment with a
   literature-anchored position is the load-bearing condition, not a refinement.
4. Identity is computed both full-length and domain-only, because a 481-aa protein
   whose similarity is confined to a 127-aa domain is a different claim from one
   that is similar throughout.

Nothing here measures GAP *activity* — no such measurement exists for any AGFG
protein (see litsearch.py).  An intact site licenses "untested", not "active"; a
missing one licenses "predicted to have lost", not "measured inactive".
"""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import is_reviewed, uniprot_entry, uniprot_search  # noqa: E402

HERE = pathlib.Path(__file__).parent

# ArfGAP consensus as stated for human AGFG2 in PMID:34369554: CX2CX16CX2CX4R
MOTIF = re.compile(r"C.{2}C.{16}C.{2}C.{4}R")
# Relaxed form: the zinc finger alone, so a protein that has the four cysteines
# but NOT the arginine is still located and reported as arginine-less.
MOTIF_RELAXED = re.compile(r"C.{2}C.{16}C.{2}C.{5}")

SUBJECTS = {
    # accession: role
    "O95081": "subject (human AGFG2)",
    "P52594": "human AGFG1 (candidate paralogue; PANTHER PTHR46134:SF1)",
    "Q80WC7": "mouse Agfg2 (candidate orthologue; PANTHER PTHR46134:SF4)",
    "Q8K2K6": "mouse Agfg1 (the IBD seed behind every AGFG2 IBA row)",
    "Q8N6T3": "ARFGAP1 — founding ArfGAP, GAP activity measured",
    "Q9ULH1": "ASAP1 — second characterised ArfGAP",
    "Q8TDY4": "ASAP3 — Asp control: PMID:23433073 names D484 as the Arf-contacting Asp",
    "Q8IYB5": "SMAP1 — the co-hit in PMID:34369554",
}

# Literature-anchored controls, each external to the derivation being validated.
ARG_CONTROL = ("O95081", 75)     # AGFG2[R75Q], PMID:34369554
ASP_CONTROL = ("Q8TDY4", 484)    # ASAP3 D484, PMID:23433073


def fetch(acc: str) -> dict:
    e = uniprot_entry(
        acc,
        "accession,id,protein_name,gene_names,organism_name,length,sequence,"
        "ft_domain,ft_zn_fing,reviewed",
    )
    seq = e["sequence"]["value"]
    dom = zf = None
    for f in e.get("features", []):
        s, t = f["location"]["start"]["value"], f["location"]["end"]["value"]
        if f["type"] == "Domain" and "Arf-GAP" in (f.get("description") or ""):
            dom = (s, t)
        if f["type"] == "Zinc finger":
            zf = (s, t)
    return {
        "accession": acc,
        "entry_name": e["uniProtkbId"],
        "reviewed": is_reviewed(e),
        "organism": e["organism"]["scientificName"],
        "gene": [g.get("geneName", {}).get("value") for g in e.get("genes", [])],
        "length": e["sequence"]["length"],
        "sequence": seq,
        "arfgap_domain": dom,
        "zinc_finger": zf,
    }


def derive_sites(rec: dict) -> dict:
    """Locate C-x2-C-x16-C-x2-C-x4-R and return 1-based residue numbers.

    Falls back to a relaxed motif (any residue where the Arg would be) when the
    strict motif does not match, so that a protein *lacking* the catalytic Arg is
    reported as lacking it rather than as unmatched — the distinction the whole
    analysis turns on.
    """
    seq = rec["sequence"]
    # search only inside the annotated ArfGAP domain, widened by 10 to tolerate
    # a domain boundary that clips the motif
    if rec["arfgap_domain"]:
        lo = max(0, rec["arfgap_domain"][0] - 1 - 10)
        hi = min(len(seq), rec["arfgap_domain"][1] + 10)
    else:
        lo, hi = 0, len(seq)
    window = seq[lo:hi]
    m = MOTIF.search(window)
    strict = m is not None
    if m is None:
        m = MOTIF_RELAXED.search(window)
    if m is None:
        return {"motif_found": False, "strict_motif": False}
    off = lo + m.start()
    cys = [off + i + 1 for i in (0, 3, 20, 23)]
    arg = off + 28 + 1
    # the four residues between the 4th Cys and the Arg; the 2nd of them is the
    # position PMID:23433073 calls D47 in the non-AGFG subfamilies
    x4 = [off + i + 1 for i in (24, 25, 26, 27)]
    for c in cys:
        assert seq[c - 1] == "C", (rec["accession"], c, seq[c - 1])
    return {
        "motif_found": True,
        "strict_motif": strict,
        "motif": m.group(0),
        "cys4": cys,
        "catalytic_arg": arg,
        "catalytic_arg_residue": seq[arg - 1],
        "has_catalytic_arg": seq[arg - 1] == "R",
        "x4_positions": x4,
        "x4_residues": "".join(seq[p - 1] for p in x4),
        # The zinc-finger feature spans the four cysteines, so its end residue
        # should BE the fourth cysteine.  Cross-check the two independent sources.
        "zf_end_equals_cys4": (rec["zinc_finger"] or (None, None))[1] == cys[3],
    }


def mafft(records: list[tuple[str, str]]) -> dict[str, str]:
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for name, seq in records:
            fh.write(f">{name}\n{seq}\n")
        path = fh.name
    proc = subprocess.run(
        ["mafft", "--quiet", "--localpair", "--maxiterate", "1000", path],
        capture_output=True, text=True, check=True,
    )
    out: dict[str, str] = {}
    name = None
    for line in proc.stdout.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            out[name] = ""
        elif name:
            out[name] += line.strip()
    pathlib.Path(path).unlink()
    return out


def ungapped_to_column(aln: str) -> list[int]:
    """Map 1-based ungapped position -> 0-based alignment column."""
    cols = []
    for i, ch in enumerate(aln):
        if ch != "-":
            cols.append(i)
    return cols


def pct_identity(a: str, b: str) -> float:
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    if not pairs:
        return 0.0
    return 100.0 * sum(1 for x, y in pairs if x == y) / len(pairs)


def main() -> None:
    recs = {acc: fetch(acc) for acc in SUBJECTS}

    # Drosophila drongo: FB:FBgn0020304 has NO reviewed entry.  Report that
    # explicitly and use the longest unreviewed isoform, flagged as TrEMBL.
    drongo = uniprot_search(
        "xref:flybase-FBgn0020304",
        "accession,id,gene_names,organism_name,length,sequence,ft_domain,ft_zn_fing,reviewed",
        size=25,
    )
    drongo_reviewed = [h for h in drongo if is_reviewed(h)]
    longest = max(drongo, key=lambda h: h["sequence"]["length"])
    drongo_rec = fetch(longest["primaryAccession"])
    drongo_rec["note"] = (
        f"FB:FBgn0020304 has {len(drongo)} UniProt entries, "
        f"{len(drongo_reviewed)} of them reviewed (Swiss-Prot); the longest "
        f"unreviewed entry is used here and its status is TrEMBL"
    )
    recs[drongo_rec["accession"]] = drongo_rec
    SUBJECTS[drongo_rec["accession"]] = "Drosophila drongo (unreviewed/TrEMBL)"

    for r in recs.values():
        r["site"] = derive_sites(r)

    # --- step 2: the derivation must reproduce BOTH literature-anchored controls ---
    a_acc, a_pos = ARG_CONTROL
    got = recs[a_acc]["site"].get("catalytic_arg")
    if got != a_pos:
        raise AssertionError(
            f"Arg derivation failed its control: {a_acc} derived Arg-{got}, but "
            f"PMID:34369554 names AGFG2[R{a_pos}Q] as its GAP-dead mutant"
        )
    # The Arf-contacting Asp is NOT at a fixed offset from the zinc finger — an
    # earlier version of this script assumed it was the second of the four x4
    # residues and its own control refused the claim (ASAP3 gave 466, not 484).
    # It is 15 residues C-terminal of the catalytic Arg *in ASAP3*, and indels
    # move it between subfamilies, so the only sound way to transfer it is by
    # alignment from the one residue the literature pins in a real sequence.
    d_acc, d_pos = ASP_CONTROL
    d_seq = recs[d_acc]["sequence"]
    if d_seq[d_pos - 1] != "D":
        raise AssertionError(
            f"{d_acc} residue {d_pos} is {d_seq[d_pos - 1]}, not D — PMID:23433073's "
            f"D484 does not resolve in this sequence version"
        )

    # --- step 3: reciprocal alignment of the annotated ArfGAP domains ---
    dom_seqs = []
    for acc, r in recs.items():
        if not r["arfgap_domain"]:
            continue
        s, t = r["arfgap_domain"]
        dom_seqs.append((acc, r["sequence"][s - 1: t]))
    aln = mafft(dom_seqs)

    def columns_for(key: str) -> dict:
        out_cols = {}
        for acc, a in aln.items():
            r = recs[acc]
            s = r["arfgap_domain"][0]
            pos = r["site"].get(key)
            if pos is None:
                out_cols[acc] = None
                continue
            pos_in_domain = pos - s + 1
            cols = ungapped_to_column(a)
            if not 1 <= pos_in_domain <= len(cols):
                out_cols[acc] = None
                continue
            col = cols[pos_in_domain - 1]
            out_cols[acc] = {"column": col, "residue": a[col], "position": pos,
                             "pos_in_domain": pos_in_domain}
        return out_cols

    arg_columns = columns_for("catalytic_arg")
    arg_ref_col = arg_columns[a_acc]["column"]
    co_aligned = {a: (v is not None and v["column"] == arg_ref_col)
                  for a, v in arg_columns.items()}
    # If ASAP3's own arginine does not co-align with AGFG2's R75, the whole
    # cross-subfamily comparison is invalid; say so loudly rather than proceeding.
    if arg_columns[d_acc]["column"] != arg_ref_col:
        raise AssertionError(
            "the two reference proteins do not co-align at the catalytic arginine, "
            "so no cross-subfamily residue transfer is valid"
        )

    # --- step 3b: transfer ASAP3 D484 to every other protein BY ALIGNMENT ---
    d_dom_start = recs[d_acc]["arfgap_domain"][0]
    d_pos_in_domain = d_pos - d_dom_start + 1
    d_cols = ungapped_to_column(aln[d_acc])
    if not 1 <= d_pos_in_domain <= len(d_cols):
        raise AssertionError(
            f"ASAP3 D{d_pos} lies outside the extracted Arf-GAP domain "
            f"{recs[d_acc]['arfgap_domain']} — cannot transfer by alignment"
        )
    asp_ref_col = d_cols[d_pos_in_domain - 1]
    if aln[d_acc][asp_ref_col] != "D":
        raise AssertionError(
            f"alignment column {asp_ref_col} holds "
            f"{aln[d_acc][asp_ref_col]!r} for ASAP3, not D"
        )

    asp_columns: dict[str, dict | None] = {}
    for acc, a in aln.items():
        residue = a[asp_ref_col]
        pos = None
        if residue != "-":
            # count non-gap characters up to and including this column
            pos = (recs[acc]["arfgap_domain"][0] - 1) + sum(
                1 for ch in a[: asp_ref_col + 1] if ch != "-"
            )
            assert recs[acc]["sequence"][pos - 1] == residue, (acc, pos, residue)
        asp_columns[acc] = {"column": asp_ref_col, "residue": residue,
                            "position": pos, "is_asp": residue == "D"}
    asp_co_aligned = {a: True for a in asp_columns}  # transferred by construction

    # --- step 4: identity, full-length and domain-only ---
    full_aln = mafft([(a, r["sequence"]) for a, r in recs.items()])
    subj = "O95081"
    identity = {}
    for acc in recs:
        if acc == subj:
            continue
        identity[acc] = {
            "full_length_pct": round(pct_identity(full_aln[subj], full_aln[acc]), 1),
            "arfgap_domain_pct": (
                round(pct_identity(aln[subj], aln[acc]), 1) if acc in aln else None
            ),
        }

    out = {
        "motif": "C-x2-C-x16-C-x2-C-x4-R (stated for human AGFG2 in PMID:34369554)",
        "controls": {
            "catalytic_arg": {
                "method": "derived from the motif, then matched against the literature",
                "accession": a_acc, "literature_position": a_pos,
                "source": "PMID:34369554 names AGFG2[R75Q] as its GAP-dead mutant",
                "derived": recs[a_acc]["site"]["catalytic_arg"], "agrees": True,
            },
            "arf_contacting_asp": {
                "method": (
                    "NOT derived: the position is an input constant, asserted to be an "
                    "Asp inside the annotated domain and then transferred to the other "
                    "proteins by alignment column"
                ),
                "accession": d_acc, "asserted_position": d_pos,
                "residue_verified": d_seq[d_pos - 1],
                "source": "PMID:23433073 names D484 in the ASAP3 structure",
                "transferred_by": "MAFFT alignment column of ASAP3 D484",
                "alignment_column": asp_ref_col,
            },
        },
        "proteins": {
            a: {k: v for k, v in r.items() if k != "sequence"} | {"role": SUBJECTS[a]}
            for a, r in recs.items()
        },
        "catalytic_arg_alignment": arg_columns,
        "arf_contacting_asp_alignment": asp_columns,
        "arg_co_aligned": co_aligned,
        "asp_co_aligned": asp_co_aligned,
        "identity_vs_AGFG2": identity,
        "domain_alignment": aln,
    }
    (HERE / "arfgap_domain.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    print(f"ArfGAP consensus used: {out['motif']}")
    print(f"control 1 (Arg): {a_acc} derived {recs[a_acc]['site']['catalytic_arg']} "
          f"== literature {a_pos} -> OK")
    print(f"control 2 (Asp, NOT derived): ASAP3 D{d_pos} asserted from PMID:23433073, "
          f"residue verified as {d_seq[d_pos - 1]}, alignment column {asp_ref_col}; "
          f"transferred to every protein by alignment -> OK\n")
    hdr = (f"{'acc':10s} {'entry':16s} {'rev':7s} {'len':>5s} {'x4':>5s} "
           f"{'Arg':>7s} {'aln':>4s} {'Asp-site':>9s}  role")
    print(hdr)
    for a, r in recs.items():
        st = r["site"]
        ac = asp_columns.get(a) or {}
        asp_txt = f"{ac.get('residue','?')}{ac.get('position') or '-'}"
        print(f"{a:10s} {r['entry_name']:16s} {'SP' if r['reviewed'] else 'TrEMBL':7s} "
              f"{r['length']:5d} {st.get('x4_residues',''):>5s} "
              f"{str(st.get('catalytic_arg'))+st.get('catalytic_arg_residue',''):>7s} "
              f"{('Y' if co_aligned.get(a) else 'n'):>4s} "
              f"{asp_txt:>9s}  {SUBJECTS[a]}")
    print("\nidentity vs human AGFG2 (O95081):")
    for a, v in sorted(identity.items(), key=lambda kv: -(kv[1]['full_length_pct'])):
        print(f"  {a} {recs[a]['entry_name']:16s} full={v['full_length_pct']:5.1f}%  "
              f"ArfGAP-domain={v['arfgap_domain_pct']}%")
    print(f"\ndrongo note: {drongo_rec['note']}")


if __name__ == "__main__":
    main()
