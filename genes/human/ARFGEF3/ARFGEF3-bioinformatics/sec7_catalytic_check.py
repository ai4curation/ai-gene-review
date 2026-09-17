"""Does human ARFGEF3 (BIG3) retain the Sec7 catalytic glutamate?

Why this matters
----------------
ARFGEF3's GO record asserts `GO:0005085 guanyl-nucleotide exchange factor
activity` twice: once by IBA from a PANTHER node, once by IEA from InterPro
`IPR000904` (the Sec7 domain signature). Both are *name/domain-implied* catalytic
calls. Sec7-domain ARF-GEFs activate ARF through a single invariant glutamate --
the "glutamic finger" -- which inserts into the ARF nucleotide pocket and
destabilises bound GDP. If ARFGEF3 has lost that residue, the activity terms are
riding on a fold, not on chemistry.

What the script does
--------------------
1. Builds the comparison panel **from the GOA WITH/FROM field** of the
   `GO:0005085` IBA row, not by hand. Those donors are, by construction, the
   family members PAINT judged to carry the activity; `resolve_withfrom.py`
   reports how many hold their own experimental evidence for it. Adds ARFGEF3
   orthologues to ask whether any loss is ARFGEF3-specific or clade-wide.
2. Extracts each entry's SEC7 domain using UniProt's own domain feature, and
   aligns the domains with MAFFT.
3. **Derives** the glutamic-finger column instead of asserting one: the column
   is chosen as the alignment column where the known-active donors are most
   conserved for Glu. A hardcoded column, or a position inferred from prose,
   would be a latent bug.
4. Cross-checks that derived column against an independent, alignment-free
   signal: the `[FY]-x-[LIVM]-P-G-E` motif reported for Sec7 domains. The two
   methods must agree on the known-active donors, or the run fails.
5. Runs controls in both directions (`--self-test`):
   - leave-one-out: the column must still be recovered with any single donor
     removed, so no one sequence is driving it;
   - a known-active member must score "Glu present";
   - that same member with its catalytic Glu mutated to Ala must score
     "Glu absent" -- a detector that cannot report a negative proves nothing;
   - the mutation target must be verified present *before* mutating, so a
     drifted target cannot silently no-op into a passing test.
6. Reproduces the published panel of Chen et al. 2014 (PMID:24997568) as a
   precondition before reporting any conclusion of its own.

Run: uv run python sec7_catalytic_check.py
     uv run python sec7_catalytic_check.py --self-test
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from uniprot import sec7_domain, summarise, uniprot_entry, uniprot_search

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ARFGEF3-goa.tsv"

SUBJECT = "Q5TH69"  # human ARFGEF3 / BIG3
GEF_TERM = "GO:0005085"

# The eight Sec7 domains aligned in Figure 2 of PMID:24997568, taken verbatim
# from that paper's Methods. Reproducing its result is a precondition, not a
# finding of our own.
#
# One published accession is wrong and the script must not paper over it:
# the Methods give GEP100 as Swiss-Prot:Q6ND90, which is a *Rhodopseudomonas
# palustris* succinate dehydrogenase subunit (TrEMBL, no Sec7 domain). Human
# GEP100/BRAG2/IQSEC1 is Q6DN90 -- two transposed characters. The correction is
# declared here, applied explicitly, and reported in the output.
CHEN2014_PANEL_AS_PUBLISHED = {
    "Q9Y6D6": "BIG1", "Q9Y6D5": "BIG2", "Q99418": "ARNO", "Q92538": "GBF1",
    "O43739": "GRP1", "Q42510": "GNOM", "Q6ND90": "GEP100", "Q5TH69": "BIG3",
}
CHEN2014_ACCESSION_CORRECTIONS = {"Q6ND90": "Q6DN90"}

# Sec7-domain motif carrying the catalytic glutamate (PMID:24997568 quotes the
# consensus as FRLPGE). Encoded as a degenerate pattern so the check is not
# tuned to one family branch; used ONLY to cross-check the derived column.
MOTIF_CLASSES = ["FY", "*", "LIVMF", "P", "G", "E"]

# Preference order for the sequence used to build the known-dead comparator:
# the subject's closest catalytically-verified paralogues first (BIG1, BIG2),
# then GBF1. Any of these is a Sec7 GEF with its own IDA for GO:0005085.
DEAD_CONTROL_PREFERENCE = ["Q9Y6D6", "Q9Y6D5", "Q92538"]


def matches_motif(seq: str) -> list[int]:
    """0-based offsets of the catalytic Glu for every motif match in `seq`."""
    hits = []
    w = len(MOTIF_CLASSES)
    for i in range(len(seq) - w + 1):
        if all(c == "*" or seq[i + j] in c for j, c in enumerate(MOTIF_CLASSES)):
            hits.append(i + w - 1)
    return hits


def goa_gef_donors() -> list[str]:
    """UniProt accessions of the GO:0005085 IBA row's WITH/FROM, via the
    resolution table. Derived from GOA so the panel cannot drift from it."""
    tsv = HERE / "withfrom_resolved.tsv"
    if not tsv.exists():
        raise FileNotFoundError(
            f"{tsv} is missing. Run `uv run python resolve_withfrom.py` first."
        )
    ents = json.loads((HERE / "supporting_entities.json").read_text())
    rows = [r for r in ents if r["go_id"] == GEF_TERM and r["evidence"] == "IBA"]
    if len(rows) != 1:
        raise RuntimeError(f"expected exactly one {GEF_TERM} IBA row, got {len(rows)}")
    tokens = set(rows[0]["supporting_entities"])
    resolved = {r["token"]: r for r in csv.DictReader(tsv.open(), delimiter="\t")}
    accs = []
    for tok in sorted(tokens):
        r = resolved.get(tok)
        if r is None:
            raise RuntimeError(f"token {tok} missing from {tsv}")
        if r["accession"]:
            accs.append(r["accession"])
    if not accs:
        raise RuntimeError("no protein donors resolved for the GEF row")
    return accs


def arfgef3_orthologues() -> list[str]:
    """Reviewed ARFGEF3 orthologues, to test whether a loss is clade-wide."""
    hits = uniprot_search("gene:arfgef3 AND reviewed:true", size=25)
    return [h["primaryAccession"] for h in hits
            if h["primaryAccession"] != SUBJECT]


SKIPPED_NO_SEC7: dict[str, str] = {}


def sec7_records(accessions: list[str]) -> dict[str, dict]:
    """{accession: {label, organism, reviewed, domain, seq}} for each entry that
    UniProt annotates with a SEC7 domain.

    Entries without one are recorded in `SKIPPED_NO_SEC7` and reported, never
    dropped silently: "this GEF donor has no annotated Sec7 domain" is itself a
    finding about the propagation, not a gap in the input."""
    out: dict[str, dict] = {}
    skipped: list[str] = []
    for acc in accessions:
        entry = uniprot_entry(acc)
        s = summarise(entry)
        if not s["organism"]:
            raise RuntimeError(f"{acc} resolved to an entry with no organism "
                               "(deleted accession?) -- refusing to score it")
        bounds = sec7_domain(entry)
        if bounds is None:
            label = s["gene"] or s["id"]
            skipped.append(f"{acc}({label})")
            SKIPPED_NO_SEC7[acc] = label
            continue
        start, end = bounds
        out[acc] = {
            "label": s["gene"] or s["id"],
            "organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "start": start, "end": end,
            "seq": s["sequence"][start - 1:end],
        }
    if skipped:
        print(f"note: no UniProt SEC7 domain feature on {len(skipped)} entries: "
              f"{', '.join(skipped)}", file=sys.stderr)
    return out


def mafft(records: dict[str, str]) -> dict[str, str]:
    """MAFFT L-INS-i alignment of {id: sequence}. Raises if MAFFT is absent."""
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for k, v in records.items():
            fh.write(f">{k}\n{v}\n")
        path = fh.name
    try:
        proc = subprocess.run(
            ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", path],
            capture_output=True, text=True, check=True,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("mafft is not installed; `brew install mafft`") from exc
    finally:
        Path(path).unlink()
    aln: dict[str, list[str]] = {}
    key = None
    for line in proc.stdout.splitlines():
        if line.startswith(">"):
            key = line[1:].strip()
            aln[key] = []
        elif key:
            aln[key].append(line.strip())
    return {k: "".join(v).upper() for k, v in aln.items()}


def derive_glu_column(aln: dict[str, str], active: list[str]) -> tuple[int, float]:
    """Alignment column where the known-active members are most Glu-conserved.

    Returns (column, fraction of active members with E there). Raises if no
    column reaches a clear majority -- better a loud failure than a column
    picked out of noise.
    """
    width = len(next(iter(aln.values())))
    best, best_frac = -1, 0.0
    for col in range(width):
        n = sum(1 for a in active if aln[a][col] == "E")
        frac = n / len(active)
        if frac > best_frac:
            best, best_frac = col, frac
    if best_frac < 0.8:
        raise RuntimeError(
            f"no alignment column is Glu in >=80% of the {len(active)} known-active "
            f"Sec7 domains (best {best_frac:.0%} at column {best}); the alignment "
            "is not good enough to locate the glutamic finger."
        )
    return best, best_frac


def ungapped_index(aligned: str, col: int) -> int | None:
    """0-based index into the ungapped sequence for alignment column `col`."""
    if aligned[col] == "-":
        return None
    return col - aligned[:col].count("-")


def analyse(panel: dict[str, dict], active: list[str]) -> dict:
    aln = mafft({k: v["seq"] for k, v in panel.items()})
    col, frac = derive_glu_column(aln, active)

    # Cross-check: the derived column must coincide with the motif-derived Glu
    # in the known-active members. Two independent signals or the run fails.
    motif_agree, motif_absent, motif_disagree = [], [], []
    for acc in active:
        hits = matches_motif(panel[acc]["seq"])
        idx = ungapped_index(aln[acc], col)
        if not hits:
            motif_absent.append(acc)
        elif idx in hits:
            motif_agree.append(acc)
        else:
            motif_disagree.append(acc)
    if motif_disagree:
        raise RuntimeError(
            "derived glutamic-finger column disagrees with the motif for "
            f"{motif_disagree}; do not trust either signal until reconciled."
        )

    rows = []
    for acc, rec in panel.items():
        a = aln[acc]
        idx = ungapped_index(a, col)
        res = a[col]
        rows.append({
            "accession": acc,
            "label": rec["label"],
            "organism": rec["organism"],
            "reviewed": rec["reviewed"],
            "sec7_domain": f"{rec['start']}-{rec['end']}",
            "aligned_residue": res,
            "protein_position": "" if idx is None else str(rec["start"] + idx),
            "glutamic_finger": "yes" if res == "E" else "no",
            "motif_hits": len(matches_motif(rec["seq"])),
            "context": a[max(0, col - 5):col + 6],
            "known_active_donor": "yes" if acc in active else "no",
        })
    rows.sort(key=lambda r: (r["glutamic_finger"] == "yes", r["label"]))
    return {
        "column": col,
        "active_glu_fraction": frac,
        "n_active": len(active),
        "motif_agree": len(motif_agree),
        "motif_absent": motif_absent,
        "rows": rows,
        "alignment": aln,
    }


def check_published_accessions() -> list[dict[str, str]]:
    """Resolve the accessions PMID:24997568 printed, and say what each really is.

    A published identifier that resolves to the wrong protein is data, not a
    missing input: report it rather than aborting or silently substituting.
    """
    report = []
    for acc, name in CHEN2014_PANEL_AS_PUBLISHED.items():
        s = summarise(uniprot_entry(acc))
        report.append({
            "published_as": name,
            "published_accession": acc,
            "resolves_to_gene": s["gene"],
            "resolves_to_organism": s["organism"],
            "reviewed": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "matches_published_name": "yes" if name.lower() in (
                (s["gene"] or "") + " " + (s["protein"] or "")).lower() else "no",
            "correction_used": CHEN2014_ACCESSION_CORRECTIONS.get(acc, ""),
        })
    return report


def reproduce_chen2014() -> dict:
    """Precondition: reproduce PMID:24997568 Figure 2 on its own eight domains."""
    accession_report = check_published_accessions()
    wanted = [CHEN2014_ACCESSION_CORRECTIONS.get(a, a)
              for a in CHEN2014_PANEL_AS_PUBLISHED]
    panel = sec7_records(wanted)
    missing = set(wanted) - set(panel)
    if missing:
        raise RuntimeError(f"Chen 2014 panel members lack a SEC7 feature: {missing}")
    active = [a for a in panel if a != SUBJECT]
    res = analyse(panel, active)
    subj = next(r for r in res["rows"] if r["accession"] == SUBJECT)
    others = [r for r in res["rows"] if r["accession"] != SUBJECT]
    verdict = {
        "published_accessions": accession_report,
        "subject_has_glutamic_finger": subj["glutamic_finger"],
        "subject_residue": subj["aligned_residue"],
        "others_with_glutamic_finger": sum(1 for r in others
                                           if r["glutamic_finger"] == "yes"),
        "others_total": len(others),
    }
    # The paper's claim: BIG3 lacks it, the other seven have it.
    if verdict["subject_has_glutamic_finger"] != "no":
        raise RuntimeError("failed to reproduce PMID:24997568: BIG3 scored as "
                           "retaining the glutamic finger")
    if verdict["others_with_glutamic_finger"] != verdict["others_total"]:
        raise RuntimeError(
            "failed to reproduce PMID:24997568: only "
            f"{verdict['others_with_glutamic_finger']}/{verdict['others_total']} "
            "of its other Sec7 domains scored as retaining the glutamic finger"
        )
    return verdict


def self_test(panel: dict[str, dict], active: list[str]) -> list[str]:
    """Break the detector on purpose. A self-test proves the guards you thought
    of fire; it cannot tell you which guard you failed to write."""
    problems: list[str] = []

    base = analyse(panel, active)
    col = base["column"]

    # 1. Leave-one-out: no single donor may be driving the column.
    for drop in active:
        sub_panel = {k: v for k, v in panel.items() if k != drop}
        sub_active = [a for a in active if a != drop]
        try:
            r = analyse(sub_panel, sub_active)
        except RuntimeError as exc:
            problems.append(f"leave-one-out({drop}) failed: {exc}")
            continue
        subj = next(x for x in r["rows"] if x["accession"] == SUBJECT)
        if subj["glutamic_finger"] != "no":
            problems.append(f"leave-one-out({drop}) flipped the subject verdict")

    # 2/3. Positive control and its mutant. Assert the mutation target is
    # present BEFORE mutating, or the "mutant" is a silent no-op.
    control = active[0]
    ctrl_row = next(r for r in base["rows"] if r["accession"] == control)
    if ctrl_row["glutamic_finger"] != "yes":
        problems.append(f"positive control {control} did not score Glu present")
    else:
        idx = ungapped_index(base["alignment"][control], col)
        seq = panel[control]["seq"]
        if seq[idx] != "E":
            problems.append(f"mutation target for {control} is {seq[idx]!r}, not 'E'"
                            " -- the self-test would have been a no-op")
        else:
            mutant = dict(panel)
            mutant[control] = dict(panel[control])
            mutant[control]["seq"] = seq[:idx] + "A" + seq[idx + 1:]
            r = analyse(mutant, active)
            row = next(x for x in r["rows"] if x["accession"] == control)
            if row["glutamic_finger"] != "no":
                problems.append(f"E->A mutant of {control} still scored Glu present"
                                " -- the detector cannot report a negative")

    # 4. A sequence with no motif at all must not be silently credited.
    if matches_motif(panel[SUBJECT]["seq"]):
        problems.append("subject unexpectedly matches the Sec7 catalytic motif;"
                        " re-examine before relying on the motif cross-check")
    return problems


def main() -> None:
    donors = goa_gef_donors()
    orthologues = arfgef3_orthologues()
    panel = sec7_records(sorted(set(donors + orthologues + [SUBJECT])))
    if SUBJECT not in panel:
        raise RuntimeError("UniProt annotates no SEC7 domain on the subject")
    # "Known active" = the GOA donors, which carry their own experimental GEF
    # evidence (see donor_evidence.tsv). ARFGEF3 and its orthologues are the
    # query set and are deliberately excluded from column derivation.
    active = [a for a in donors if a in panel]

    if "--self-test" in sys.argv:
        problems = self_test(panel, active)
        for p in problems:
            print("SELF-TEST FAIL:", p)
        print(f"self-test: {len(problems)} problem(s)")
        sys.exit(1 if problems else 0)

    chen = reproduce_chen2014()

    # A known-dead comparator goes in the PUBLISHED table, not only in the
    # self-test. Without one, a residue-level check cannot distinguish "the
    # pipeline finds Glu wherever it looks" from "this protein has lost it".
    #
    # The comparator is the closest catalytically-verified paralogue with its
    # glutamic finger substituted to Ala. Glu->Ala/Lys at this position is the
    # literature-standard inactivating mutation for Sec7 domains, so this is a
    # sequence whose GEF activity is known to be abolished. The mutation target
    # is asserted present before it is made, so a drifted target cannot no-op.
    #
    # Note the asymmetry this panel can and cannot support: losing the catalytic
    # residue is strong evidence AGAINST activity, while retaining it would NOT
    # have been evidence FOR activity. Only the negative direction is claimed.
    probe = analyse(panel, active)
    dead_acc = next(a for a in DEAD_CONTROL_PREFERENCE if a in active)
    dead_idx = ungapped_index(probe["alignment"][dead_acc], probe["column"])
    dead_seq = panel[dead_acc]["seq"]
    if dead_idx is None or dead_seq[dead_idx] != "E":
        raise RuntimeError(
            f"cannot build the known-dead comparator: {dead_acc} has "
            f"{dead_seq[dead_idx] if dead_idx is not None else 'a gap'!r} at the "
            "glutamic-finger column, not 'E'"
        )
    dead_id = f"{dead_acc}_E{panel[dead_acc]['start'] + dead_idx}A"
    panel[dead_id] = dict(panel[dead_acc])
    panel[dead_id]["label"] = f"{panel[dead_acc]['label']} E{panel[dead_acc]['start'] + dead_idx}A"
    panel[dead_id]["organism"] = "synthetic catalytic-dead control"
    panel[dead_id]["reviewed"] = "control"
    panel[dead_id]["seq"] = dead_seq[:dead_idx] + "A" + dead_seq[dead_idx + 1:]

    # The column is derived from the unmutated active donors only, so injecting
    # the comparator cannot move the column it is scored against.
    res = analyse(panel, active)
    dead_row = next(r for r in res["rows"] if r["accession"] == dead_id)
    if dead_row["glutamic_finger"] != "no":
        raise RuntimeError(
            "the known-dead comparator scored as retaining the glutamic finger; "
            "the check cannot report a negative and its result is meaningless."
        )

    with (HERE / "sec7_glutamic_finger.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(res["rows"][0].keys()))
        w.writeheader()
        w.writerows(res["rows"])

    subject = next(r for r in res["rows"] if r["accession"] == SUBJECT)
    ortho_rows = [r for r in res["rows"]
                  if r["accession"] in set(orthologues) and r["accession"] in panel]
    donor_rows = [r for r in res["rows"] if r["known_active_donor"] == "yes"]
    summary = {
        "chen2014_reproduction": chen,
        "known_dead_comparator": {
            "id": dead_id,
            "built_from": dead_acc,
            "label": panel[dead_id]["label"],
            "aligned_residue": dead_row["aligned_residue"],
            "glutamic_finger": dead_row["glutamic_finger"],
            "rationale": "Glu->Ala at the glutamic finger is the standard "
                         "inactivating substitution for Sec7 domains; a check "
                         "that cannot score this sequence negative proves nothing.",
        },
        "alignment_column": res["column"],
        "active_donors_with_glutamic_finger": sum(
            1 for r in donor_rows if r["glutamic_finger"] == "yes"),
        "active_donors_total": len(donor_rows),
        "subject": {k: subject[k] for k in
                    ("accession", "label", "organism", "sec7_domain",
                     "aligned_residue", "protein_position", "glutamic_finger",
                     "motif_hits", "context")},
        "orthologues_with_glutamic_finger": sum(
            1 for r in ortho_rows if r["glutamic_finger"] == "yes"),
        "orthologues_total": len(ortho_rows),
        "orthologues": [{k: r[k] for k in ("accession", "label", "organism",
                                           "aligned_residue", "context")}
                        for r in ortho_rows],
        "residue_distribution_at_column": dict(
            Counter(r["aligned_residue"] for r in res["rows"])),
        "gef_donors_without_an_annotated_sec7_domain": {
            a: l for a, l in SKIPPED_NO_SEC7.items() if a in set(donors)},
    }
    (HERE / "sec7_glutamic_finger.json").write_text(json.dumps(summary, indent=2))

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
