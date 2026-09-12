"""Which AGGF1 papers produced GO annotations, and which produced none?

Affinage's trust gates certify precision, not recall, so the interesting
question is not "did it cite real papers" but "how much of what is published
about AGGF1 reached GOA at all". Query QuickGO **by reference** for every paper
this review relies on and count the entities each one annotates.

Two things fall out of the same query:

* A paper with 0 annotations anywhere is a coverage gap.
* A reference that annotates a whole complex or a large panel with identical
  evidence is a projection, not N independent findings (so count distinct
  entity ids, not annotations, and refuse to answer from a truncated page).

The second half asks the reference-class question that decides whether a
G-patch-derived molecular function is defensible: **what molecular function does
GO actually give the characterised human G-patch proteins?** AGGF1's only MF in
GOA outside `protein binding` is `GO:0003676 nucleic acid binding`, an
InterPro2GO mapping off `IPR000467 G-patch domain`. If GO's own treatment of the
proteins whose G-patch has been characterised is *not* nucleic-acid binding, the
mapping is a domain-name inference rather than a measurement.

Run: uv run python gap_by_reference.py
"""

from __future__ import annotations

import json

from uniprot import _cached_get

BASE = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
SUBJECT = "UniProtKB:Q8N302"

# Every PMID cited by the GOA file or by the affinage record, with what it shows.
PAPERS = {
    # --- referenced by GOA ---
    "PMID:14961121": "Tian 2004 Nature -- VG5Q/AGGF1 discovery (source of 6 IDA/IPI rows)",
    "PMID:15905966": "Timur 2005 review -- source of the GO:0001570 TAS row",
    "PMID:16189514": "Rual 2005 CCSB-HI1 Y2H (BLOC1S6)",
    "PMID:22365833": "Hegele 2012 spliceosome Y2H matrix (AGGF1 self-interaction)",
    "PMID:25416956": "Rolland 2014 HI-II-14 Y2H (self)",
    "PMID:31515488": "Fragoza 2019 variant interactome (MAB21L3)",
    "PMID:32296183": "Luck 2020 HuRI (DHX15, MCRS1, FBXO28, MAB21L3)",
    "PMID:33961781": "Huttlin 2021 BioPlex AP-MS (BLOC1S6)",
    "PMID:39251607": "Khoroshkin 2024 post-transcriptional regulatory modules (self)",
    "PMID:40205054": "Schaffer 2025 multimodal cell maps (MAB21L3)",
    # --- affinage citations, none of them referenced by GOA ---
    "PMID:17884784": "Y2H Id1 interaction",
    "PMID:19556247": "GATA1 activates the AGGF1 promoter",
    "PMID:23197652": "zebrafish aggf1 specifies venous identity (donor of the GO:0001525 IBA)",
    "PMID:23628701": "AGGF1 suppresses TNF-alpha endothelial activation; FHA domain required",
    "PMID:24277077": "zebrafish aggf1 upstream of scl/fli1/etsrp in hemangioblast specification",
    "PMID:24462738": "miR-27a represses AGGF1 under hypoxia",
    "PMID:26850475": "Aggf1-SMAD7 complex in liver fibrosis",
    "PMID:27513923": "AGGF1 activates JNK-dependent autophagy in endothelial cells",
    "PMID:27522498": "AGGF1 activates PI3K p110alpha/p85alpha-AKT; VE-cadherin",
    "PMID:28649088": "AGGF1 and VSMC phenotypic switching (neointima)",
    "PMID:28958996": "Aggf1 blocks NF-kB binding at the Ccl2 promoter",
    "PMID:29641288": "AngII/NF-kB p65 induces AGGF1",
    "PMID:29885663": "AGGF1 and BBB after subarachnoid haemorrhage",
    "PMID:31092480": "AGGF1, Fyn/Nrf2 and EPC dysfunction",
    "PMID:32061268": "Aggf1 3'UTR as a competing endogenous RNA with Mcl1",
    "PMID:33069768": "AGGF1 FHA domain binds p53; antagonises MDM2 (tumour suppressor)",
    "PMID:33168501": "AGGF1 and DNA damage repair markers in colon cancer",
    "PMID:34551592": "integrin alpha5beta1 is the AGGF1 receptor; FQRDDAPAS motif",
    "PMID:35202649": "integrin alpha7 on VSMCs via the RDDAPAS motif",
    "PMID:35608889": "AGGF1-coated paraspeckles; binds NONO/PSF/HNRNPK and NEAT1 RNA",
    "PMID:36696895": "AGGF1 binds TWEAK and blocks TWEAK-Fn14 in muscle atrophy",
    "PMID:37081014": "AGGF1 enhances ITGA7-LAP-TGF-beta1 binding; thoracic aortic aneurysm",
    "PMID:37881938": "aggf1 upstream of npas4l and mTOR-S6K-Emp2",
    "PMID:39905000": "HIF-1alpha drives AGGF1; AGGF1 increases TNFSF12-FN14 binding",
    "PMID:40035560": "AGGF1 is a general splicing factor; SRSF6 exon 3 skipping",
}

# Human G-patch proteins whose G-patch has been characterised as a DEAH/DExH
# helicase-activation module, plus the helicases themselves as controls.
GPATCH_REFERENCE_CLASS = {
    "NKRF": "O15226",
    "TFIP11": "Q9UBB9",
    "GPKOW": "Q92917",
    "RBM17": "Q96I25",
    "SUGP1": "Q8IWZ8",
    "CMTR1": "Q8N1G2",
    "GPATCH1": "Q9BRR8",
    "GPATCH4": "Q5T3I0",
    "RBM5": "P52756",
    "PINX1": "Q96BK5",
    "ZGPAT": "Q8N5A5",
    "AGGF1": "Q8N302",
    # helicase controls
    "DHX15": "O43143",
    "DHX16": "O60231",
}
MF_ROOT = "GO:0003674"


def qg(url: str, key: str) -> dict:
    d = json.loads(_cached_get(url, key))
    n, got = d.get("numberOfHits", 0), len(d.get("results", []))
    if n > got:
        # Do not read a page total as the whole. Say so instead of guessing.
        d["_truncated"] = True
    return d


def main() -> None:
    print("=== GO annotations produced by each AGGF1-relevant paper ===")
    n_zero = 0
    n_nothing_on_subject = 0
    for pmid, what in PAPERS.items():
        d = qg(f"{BASE}?reference={pmid}&limit=100", f"qgref_{pmid.replace(':', '_')}")
        n = d.get("numberOfHits", 0)
        if d.get("_truncated"):
            print(
                f"{pmid}  {n} annotations -- entity count UNAVAILABLE (paginated); "
                f"projection test unreliable.  [{what}]"
            )
            continue
        ents = sorted({r["geneProductId"] for r in d["results"]})
        subj = [r for r in d["results"] if r["geneProductId"] == SUBJECT]
        print(
            f"{pmid}  {n} annotation(s) over {len(ents)} entit(y/ies); "
            f"{len(subj)} on AGGF1.  [{what}]"
        )
        for r in subj:
            print(f"      AGGF1 <- {r['goId']} {r.get('goName','')} [{r['goEvidence']}]")
        if n == 0:
            n_zero += 1
        elif not subj:
            n_nothing_on_subject += 1
    print()
    print(
        f"SUMMARY: {len(PAPERS)} papers; {n_zero} produced NO GO annotation anywhere; "
        f"{n_nothing_on_subject} annotate other genes but nothing on AGGF1."
    )
    print()

    print("=== molecular functions GO gives the characterised human G-patch proteins ===")
    print("(the reference class for judging the IPR000467 -> GO:0003676 mapping)")
    EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                    "HTP", "HDA", "HMP", "HGI", "HEP"}
    tally = {"queried": 0, "reported": 0, "has_0003676": 0,
             "0003676_iea_only": 0, "0003676_experimental": 0,
             "rna_binding_experimental": 0}
    for name, acc in GPATCH_REFERENCE_CLASS.items():
        u = (
            f"{BASE}?geneProductId=UniProtKB:{acc}&goId={MF_ROOT}"
            "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
        )
        res = qg(u, f"qgmf_{acc}")
        is_control = name in {"DHX15", "DHX16"}
        if not is_control:
            tally["queried"] += 1
        if res.get("_truncated"):
            print(f"{name:9s} MF annotations truncated ({res['numberOfHits']}), not reported")
            continue
        if not is_control:
            tally["reported"] += 1
        terms: dict[str, set[str]] = {}
        for r in res["results"]:
            terms.setdefault(f"{r['goId']} {r.get('goName','')}", set()).add(r["goEvidence"])
        interesting = {
            t: sorted(e)
            for t, e in terms.items()
            if not t.startswith("GO:0005515")
        }
        print(f"{name:9s} ({acc}) {len(terms)} distinct MF terms:")
        for t, e in sorted(interesting.items()):
            print(f"            {t}  {e}")
        if is_control:
            continue
        # Evidence held for GO:0003676 itself, and for anything under RNA binding.
        ev_0003676 = {e for r in res["results"] if r["goId"] == "GO:0003676"
                      for e in [r["goEvidence"]]}
        rna = {r["goEvidence"] for r in res["results"]
               if r["goId"] in {"GO:0003723", "GO:0003729", "GO:0070034", "GO:0003725"}}
        if ev_0003676:
            tally["has_0003676"] += 1
            if ev_0003676 == {"IEA"}:
                tally["0003676_iea_only"] += 1
            if ev_0003676 & EXPERIMENTAL:
                tally["0003676_experimental"] += 1
        if rna & EXPERIMENTAL:
            tally["rna_binding_experimental"] += 1
    print()
    print(
        f"G-PATCH REFERENCE CLASS SUMMARY (controls DHX15/DHX16 excluded): "
        f"{tally['queried']} queried, {tally['reported']} reported;\n"
        f"  {tally['has_0003676']} carry GO:0003676 nucleic acid binding;\n"
        f"  {tally['0003676_iea_only']} carry it by IEA and NOTHING ELSE;\n"
        f"  {tally['0003676_experimental']} carry it with any experimental code;\n"
        f"  {tally['rna_binding_experimental']} carry GO:0003723 RNA binding (or a child)\n"
        f"    with an experimental code."
    )
    print()


if __name__ == "__main__":
    main()
