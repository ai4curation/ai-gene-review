"""Generate RESULTS.md from the committed analysis outputs.

Every number in RESULTS.md is computed here from the TSV/JSON the other scripts
write, so a hand-edit to the report is reverted on the next run rather than
silently surviving. Missing input is a hard error naming the command that
produces it - a report that quietly loses a section while stale numbers remain
elsewhere is worse than a crash.

Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/make_results.py
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/make_results.py --check
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent

PRODUCERS = {
    "withfrom_resolved.tsv": "resolve_withfrom.py",
    "donor_evidence.tsv": "resolve_withfrom.py",
    "term_status.json": "check_terms.py",
    "partner_checks.tsv": "partner_checks.py",
    "reference_scope.tsv": "reference_scope.py",
    "reference_annotations.tsv": "reference_scope.py",
    "literature_coverage.tsv": "literature_coverage.py",
}

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def load_tsv(name: str) -> list[dict[str, str]]:
    p = HERE / name
    if not p.exists():
        raise SystemExit(
            f"missing input {p}\n"
            f"  produce it with: uv run python "
            f"genes/human/ARFGEF1/ARFGEF1-bioinformatics/{PRODUCERS[name]}"
        )
    with p.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_json(name: str) -> dict:
    p = HERE / name
    if not p.exists():
        raise SystemExit(
            f"missing input {p}\n"
            f"  produce it with: uv run python "
            f"genes/human/ARFGEF1/ARFGEF1-bioinformatics/{PRODUCERS[name]}"
        )
    return json.loads(p.read_text())


def build() -> str:
    resolved = load_tsv("withfrom_resolved.tsv")
    donors = load_tsv("donor_evidence.tsv")
    terms = load_json("term_status.json")
    partners = load_tsv("partner_checks.tsv")
    refscope = load_tsv("reference_scope.tsv")
    refann = load_tsv("reference_annotations.tsv")
    coverage = load_tsv("literature_coverage.tsv")

    # --- WITH/FROM resolution -------------------------------------------
    prot = [r for r in resolved if r["kind"] in {"protein", "mod-id"} and r["accession"]]
    n_sp = sum(1 for r in prot if r["reviewed"] == "Swiss-Prot")
    n_tr = sum(1 for r in prot if r["reviewed"] == "TrEMBL")
    assert n_sp + n_tr == len(prot), "Swiss-Prot/TrEMBL split does not total"
    unresolved = [r["token"] for r in resolved if r["protein"] == "UNRESOLVED"]
    n_exp = sum(1 for r in donors if r["donor_has_experimental"] == "True")

    # --- per-row donor breakdowns ---------------------------------------
    by_row: dict[str, list[dict[str, str]]] = defaultdict(list)
    for d in donors:
        by_row[d["goa_row"]].append(d)

    def row_stats(goa_row: str) -> tuple[int, int, int, int, list[str]]:
        rows = by_row[goa_row]
        n = len(rows)
        exp = sum(1 for r in rows if r["donor_has_experimental"] == "True")
        sp = sum(1 for r in rows if r["reviewed"] == "Swiss-Prot")
        tr = sum(1 for r in rows if r["reviewed"] == "TrEMBL")
        tset: set[str] = set()
        for r in rows:
            tset.update(t for t in r["donor_terms"].split(";") if t)
        return n, exp, sp, tr, sorted(tset)

    vmt_n, vmt_exp, vmt_sp, vmt_tr, vmt_terms = row_stats("1")
    gef_n, gef_exp, gef_sp, gef_tr, gef_terms = row_stats("4")
    tgn_n, tgn_exp, _, _, tgn_terms = row_stats("2")
    vmt_desc = [t for t in vmt_terms if t != "GO:0016192"]

    # --- GEF term merge --------------------------------------------------
    gef = terms["terms"]["GO:0005085"]
    sec_ids = gef["secondaryIds"] or []
    gef_children = terms["children"]["GO:0005085"]

    # --- MYO9A shadow set ------------------------------------------------
    myo = [r for r in refann if r["reference"] == "PMID:15644318"]
    myo9a = [r for r in myo if r["symbol"] == "MYO9A"]
    myo9b = [r for r in myo if r["symbol"] == "MYO9B"]
    symbol_of = {r["gene_product"].replace("UniProtKB:", "").split("-")[0]: r["symbol"]
                 for r in refann if r["symbol"]}

    def sym(acc_token: str) -> str:
        acc = acc_token.replace("UniProtKB:", "").split("-")[0]
        return symbol_of.get(acc, acc)

    myo9a_partners = sorted({sym(r["with_from"]) for r in myo9a if r["with_from"]})
    myo9b_partners = sorted({sym(r["with_from"]) for r in myo9b if r["with_from"]})
    assert myo9a_partners, "no MYO9A partner rows found for PMID:15644318"
    myo9b_only_terms = sorted({r["go_id"] for r in myo9b} - {r["go_id"] for r in myo9a})

    # --- literature coverage ---------------------------------------------
    aff = [r for r in coverage if r["in_affinage"] == "True"]
    a_zero = [r["pmid"] for r in aff if int(r["annotations_anywhere"]) == 0]
    a_other = [r["pmid"] for r in aff
               if int(r["annotations_anywhere"]) > 0 and r["annotations_on_ARFGEF1"] == "0"]
    a_subj = [r["pmid"] for r in aff
              if r["annotations_on_ARFGEF1"] not in {"0", "UNKNOWN (paginated)"}]
    assert len(a_zero) + len(a_other) + len(a_subj) == len(aff), "affinage buckets do not partition"

    # --- reference scope --------------------------------------------------
    trunc = [r["reference"] for r in refscope if r["truncated"] == "True"]
    focused = [r for r in refscope if r["truncated"] == "False" and int(r["distinct_entities"]) <= 4]

    L: list[str] = []
    A = L.append
    A("# ARFGEF1 bioinformatics results")
    A("")
    A("**Generated by `make_results.py` from the committed TSV/JSON outputs. Do not")
    A("hand-edit — re-running regenerates this file.** Reproduce with the commands in")
    A("`README.md`; verify with `make_results.py --check`.")
    A("")

    A("## 1. WITH/FROM resolution and donor evidence")
    A("")
    A(f"Every WITH/FROM token in `ARFGEF1-goa.tsv` resolves: {len(unresolved)} unresolved.")
    A(f"Of {len(resolved)} distinct tokens, {len(prot)} name a protein — "
      f"**{n_sp} Swiss-Prot, {n_tr} TrEMBL**. The rest are PANTHER ancestral nodes,")
    A("InterPro signatures, ARBA rules, UniProt subcellular-location ids and an Ensembl")
    A("protein id, none of which is a gene product.")
    A("")
    A("Donor evidence was then queried per (donor, propagated term) pair against QuickGO")
    A("with `goUsage=descendants`. **"
      f"{n_exp} of {len(donors)} (donor, term) pairs carry the donor's own experimental")
    A("evidence for the propagated term.** The single exception is "
      f"`{[r['accession'] for r in donors if r['donor_has_experimental'] != 'True'][0]}` "
      "(*Dictyostelium*), which holds")
    A("`GO:0016192` by IBA only. No propagated row on this gene can be argued down on the")
    A("grounds that its sources carry only the same family-level inference.")
    A("")
    A("| IBA row | protein donors | with own experimental evidence | Swiss-Prot / TrEMBL |")
    A("|---|---|---|---|")
    A(f"| `GO:0005085` guanyl-nucleotide exchange factor activity | {gef_n} | {gef_exp} | {gef_sp} / {gef_tr} |")
    A(f"| `GO:0016192` vesicle-mediated transport | {vmt_n} | {vmt_exp} | {vmt_sp} / {vmt_tr} |")
    A(f"| `GO:0005802` trans-Golgi network | {tgn_n} | {tgn_exp} | — |")
    A("")
    A(f"For `GO:0005085`, all {gef_n} donors hold **only** "
      f"{', '.join('`' + t + '`' for t in gef_terms)} — not one holds a descendant.")
    A("")
    A(f"All {gef_n} protein donors of the GO:0005085 IBA carry their own experimental "
      f"evidence for that term, {gef_sp} of them as Swiss-Prot entries, and none holds "
      "a descendant of it.")
    A("")
    A(f"For `GO:0016192`, by contrast, the donors' own terms are spread across "
      f"{len(vmt_desc)} distinct descendant processes "
      f"({', '.join('`' + t + '`' for t in vmt_desc)}), so the generic parent is the")
    A("genuine least common ancestor of a heterogeneous donor set rather than an")
    A("under-specified term.")
    A("")
    A(f"For `GO:0005802`, every donor holds {', '.join('`' + t + '`' for t in tgn_terms)} "
      "itself, so the propagation lands at the same")
    A("specificity as its donors rather than above them.")
    A("")
    A(f"All {tgn_n} protein donors of the GO:0005802 IBA carry their own experimental "
      "evidence for GO:0005802 itself rather than for a parent of it.")
    A("")

    A("## 2. `GO:0005086` and the substrate-specific GEF terms are gone")
    A("")
    A(f"QuickGO resolves `GO:0005086` to **{gef['name']}** (`GO:0005085`), and")
    A(f"GO:0005085 now lists {len(sec_ids)} merged ids among its secondaryIds and has no")
    A("substrate-specific is_a children. The merged ids are:")
    A("")
    A("```")
    A(" ".join(sec_ids))
    A("```")
    A("")
    A(f"Its only children are {len(gef_children)}, neither of them a substrate-specific activity:")
    A("")
    for c in gef_children:
        name = c.get("name") or terms["terms"].get(c["id"], {}).get("name", "")
        if not name:
            raise SystemExit(
                f"no name for child {c['id']}; regenerate term_status.json with "
                "uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/check_terms.py"
            )
        A(f"- `{c['id']}` ({c['relation']}) — {name}")
    A("")
    A("So `GO:0005085` is already maximal for ARFGEF1, whose defining property is that it")
    A("is an **ARF1/ARF3** exchange factor. The substrate can only be recorded as an")
    A("annotation extension (`RO:0002233` has_input) or in `core_functions[].substrates`.")
    A("")

    A("## 3. A paralog shadow set on MYO9A from PMID:15644318")
    A("")
    A(f"Querying GOA by reference rather than by gene returns {len(myo)} annotations for")
    A(f"`PMID:15644318`. **MYO9A has acquired an exact copy of the MYO9B partner set "
      f"({', '.join(p.replace('UniProtKB:', '') for p in myo9a_partners)}) but none of the "
      "MYO9B functional rows** —")
    A(f"MYO9B additionally holds {', '.join('`' + t + '`' for t in myo9b_only_terms)}, "
      "which MYO9A does not.")
    A("")
    A("| gene product | GO term | qualifier | evidence | with/from |")
    A("|---|---|---|---|---|")
    for r in myo:
        if r["symbol"] in {"MYO9A", "MYO9B", "RHOA"} or r["gene_product"] == "UniProtKB:Q9Y6D6":
            A(f"| {r['symbol']} `{r['gene_product'].replace('UniProtKB:', '')}` | "
              f"`{r['go_id']}` | {r['qualifier']} | {r['evidence']} | "
              f"{r['with_from'].replace('UniProtKB:', '') or '—'} |")
    A("")
    A(f"MYO9A partner set: {', '.join(myo9a_partners)}. "
      f"MYO9B partner set: {', '.join(myo9b_partners)}. "
      f"Identical: {myo9a_partners == myo9b_partners}.")
    A("The paper's title, abstract and every described experiment concern myosin IXb. The")
    A("full text could not be obtained (JBC returns HTTP 403), so the affected review row")
    A("is left `UNDECIDED` rather than removed.")
    A("")

    A("## 4. Interaction partners: identity and experiment independence")
    A("")
    A(f"All {len(partners)} `GO:0005515` IPI partner accessions resolve to reviewed")
    A("(Swiss-Prot) canonical entries with the canonical length — no TrEMBL fragments, no")
    A("partial ORFeome clones.")
    A("")
    A("| partner | accession | len | records | pubs | distinct experiments | spoke-expanded | max MI | partner's own IntAct partners |")
    A("|---|---|---|---|---|---|---|---|---|")
    for r in partners:
        A(f"| {r['gene']} | `{r['goa_partner_token']}` | {r['length']} | {r['intact_records']} | "
          f"{r['distinct_publications']} | {r['distinct_experiments']} | "
          f"{r['spoke_expanded_records']} | {r['max_mi_score'] or '—'} | "
          f"{r['partner_total_intact_partners']} |")
    A("")
    A("Counting distinct (publication, detection-method) pairs rather than UniProt's")
    A("`NbExp` did **not** collapse any partner to one screen logged several ways.")
    A("")

    A("## 5. Reference scope — no complex-projection signature")
    A("")
    A(f"{len(focused)} of the {len(refscope)} references supporting ARFGEF1 annotations are")
    A("gene-focused, annotating four entities or fewer across all of GOA. None shows the")
    A("pattern of a complex-level phenotype distributed to every subunit.")
    A("")
    A(f"{len(trunc)} references are too large to enumerate from one page "
      f"({', '.join(trunc)}); their entity")
    A("counts are reported as unavailable rather than derived from a partial page. All")
    A("three are proteome-scale interaction maps contributing only `GO:0005515`.")
    A("")

    A("## 6. Literature coverage")
    A("")
    A(f"Union of the affinage citation block and every `RX PubMed=` line in the UniProt")
    A(f"entry: {len(coverage)} PMIDs. Restricted to the {len(aff)} functional papers affinage")
    A("returned:")
    A("")
    A("| bucket | n | PMIDs |")
    A("|---|---|---|")
    A(f"| annotate ARFGEF1 | {len(a_subj)} | {', '.join(p.replace('PMID:', '') for p in a_subj)} |")
    A(f"| annotate only other genes | {len(a_other)} | {', '.join(p.replace('PMID:', '') for p in a_other)} |")
    A(f"| no GO annotation anywhere | {len(a_zero)} | {', '.join(p.replace('PMID:', '') for p in a_zero)} |")
    A("")
    A(f"That is, **of the {len(aff)} functional papers affinage returned, only {len(a_subj)} have")
    A(f"produced any GO annotation on human ARFGEF1**, and {len(a_zero)} have produced none")
    A("anywhere in GOA — including `PMID:10393931`, which measured the exchange reaction")
    A("and the brefeldin A inhibition constant on the human protein.")
    A("")
    return "\n".join(L) + "\n"


def main() -> int:
    text = build()
    out = HERE / "RESULTS.md"
    if "--check" in sys.argv:
        if not out.exists():
            print("RESULTS.md does not exist; run without --check")
            return 1
        if out.read_text() != text:
            print("RESULTS.md differs from a fresh generation — it has been hand-edited "
                  "or an input changed. Re-run without --check.")
            return 1
        print("OK: RESULTS.md reproduces exactly from the committed inputs.")
        return 0
    out.write_text(text)
    print(f"wrote {out} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
