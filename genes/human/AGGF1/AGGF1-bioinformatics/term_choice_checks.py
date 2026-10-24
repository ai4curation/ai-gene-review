"""Defend two term choices by GO's own usage, not by reading the definition alone.

This review makes two MODIFY calls that a reviewer could reasonably challenge on
scope. Both are checked against how GO actually uses the term, because a
definition that permits something and a community that never does it are
different situations.

**1. `GO:0019955 cytokine binding` for AGGF1-TNFSF12.** The obvious objection is
that "cytokine binding" is a receptor's term, and AGGF1 is a secreted
non-receptor. Check whether non-receptors hold it.

**2. `GO:0017151 DEAD/H-box RNA helicase binding` for AGGF1-DHX15.** DHX15 is a
DEA**H**-box helicase. Check whether GO has a DEAH-specific term that would be
more correct, and how loosely GO:0017151 is used in practice.

Run: uv run python term_choice_checks.py
"""

from __future__ import annotations

import json
from collections import Counter

from uniprot import _cached_get

QG = "https://www.ebi.ac.uk/QuickGO/services"
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}
# "Is it a receptor?" is decided from each holder's own GO record - does it carry
# GO:0038023 signaling receptor activity or a descendant - not from its symbol.
# A suffix heuristic put ACVRL1, BMPR1A and IFNAR1 in the "non-receptor" column,
# which is exactly the kind of guessed classification this review argues against.
RECEPTOR_ACTIVITY = "GO:0038023"


def qg(path: str, key: str) -> dict:
    d = json.loads(_cached_get(f"{QG}/{path}", key))
    if "results" in d and d.get("numberOfHits", 0) > len(d["results"]):
        d["_truncated"] = True
    return d


def uniprot_name(acc: str) -> tuple[str, str]:
    body = _cached_get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=protein_name,gene_primary",
        f"tcname_{acc}",
    )
    e = json.loads(body)
    gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value", "")
    name = (e.get("proteinDescription", {}).get("recommendedName", {})
            .get("fullName", {}).get("value", ""))
    return gene, name


def check_cytokine_binding() -> None:
    print("=== 1. GO:0019955 cytokine binding: is it receptor-only in practice? ===")
    d = qg("annotation/search?goId=GO:0019955&goUsage=exact&taxonId=9606&limit=100",
           "tc_0019955_human")
    accs = sorted({r["geneProductId"].split(":")[-1] for r in d["results"]})
    note = " (page of a larger set, so these are a floor)" if d.get("_truncated") else ""
    print(f"  {d['numberOfHits']} human annotations, {len(accs)} distinct products read{note}")

    # For each holder, ask its OWN GO record whether it is a signaling receptor.
    receptors, non_receptors, unknown = [], [], []
    for acc in accs:
        r = qg(
            f"annotation/search?geneProductId=UniProtKB:{acc}&goId={RECEPTOR_ACTIVITY}"
            "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=1",
            f"tc_recept_{acc}",
        )
        try:
            gene, name = uniprot_name(acc)
        except Exception:  # noqa: BLE001 - an unresolvable accession is data, not a crash
            unknown.append((acc, "", "lookup failed"))
            continue
        (receptors if r["numberOfHits"] else non_receptors).append((acc, gene, name))

    print(f"  holders carrying signaling receptor activity : {len(receptors)}")
    print(f"  holders NOT carrying it                      : {len(non_receptors)}")
    for acc, gene, name in non_receptors:
        print(f"    {acc}  {gene:10s} {name[:72]}")
    if unknown:
        print(f"  unresolvable: {unknown}")
    if not non_receptors:
        print("  => the term IS receptor-only in practice; reconsider the choice.")
    else:
        print("  => GO:0019955 is not receptor-restricted in use. BGN (biglycan), a")
        print("     secreted extracellular proteoglycan that binds secreted cytokines,")
        print("     is the directly analogous precedent for AGGF1 binding TNFSF12.")
    print()


def check_helicase_binding() -> None:
    print("=== 2. GO:0017151 DEAD/H-box RNA helicase binding: is DHX15 in scope? ===")
    t = json.loads(_cached_get(f"{QG}/ontology/go/terms/GO:0017151/complete",
                               "tc_0017151_term"))["results"][0]
    print(f"  name     : {t['name']}")
    print(f"  def      : {(t.get('definition') or {}).get('text')}")
    print(f"  comment  : {t.get('comment')}")
    print(f"  synonyms : {[s.get('name') for s in (t.get('synonyms') or [])]}")
    print(f"  children : {t.get('children')}")

    s = json.loads(_cached_get(f"{QG}/ontology/go/search?query=DEAH&limit=25", "tc_deah"))
    hits = s.get("results") or []
    print(f"  GO terms whose text mentions DEAH: {len(hits)} {[h['id'] for h in hits]}")
    if hits:
        print("  NOTE: a DEAH-specific term exists -- re-examine the choice.")
    else:
        print("  => GO has NO DEAH-specific binding term, so GO:0017151 is the only")
        print("     available term for binding a helicase of this superfamily.")

    d = qg("annotation/search?goId=GO:0017151&goUsage=exact&taxonId=9606&limit=100",
           "tc_0017151_human")
    print(f"  human annotations: {d['numberOfHits']}; "
          f"evidence {dict(Counter(r['goEvidence'] for r in d['results']))}")
    partners: set[str] = set()
    for r in d["results"]:
        if r["goEvidence"] == "IEA":
            continue
        wf = [x["id"] for c in (r.get("withFrom") or []) for x in c.get("connectedXrefs", [])]
        partners.update(w for w in wf if w[0].isalpha() and len(w) in (6, 10))
        print(f"    {r.get('symbol'):8s} [{r['goEvidence']:4s}] {r.get('reference')} -> {wf}")
    print("  partners named in those rows:")
    dead = deah = other = 0
    for a in sorted(partners):
        gene, name = uniprot_name(a)
        if gene.startswith("DHX") or "DEAH" in name:
            fam, deah = "DEAH/DExH", deah + 1
        elif gene.startswith("DDX") or "DEAD" in name:
            fam, dead = "DEAD-box", dead + 1
        else:
            fam, other = "NOT a DEAD/H-box helicase", other + 1
        print(f"    {a}  {gene:8s} [{fam}] {name}")
    print(f"  => {dead} DEAD-box, {deah} DEAH/DExH, {other} neither.")
    if other:
        print("     GO already applies this term to partners outside a strict DEAD-box")
        print("     reading (POT1 holds it for the RecQ DNA helicases BLM and WRN), so")
        print("     using it for the DEAH-box helicase DHX15 is well inside existing")
        print("     usage -- and considerably more precise than those rows.")
    print()


def main() -> None:
    check_cytokine_binding()
    check_helicase_binding()


if __name__ == "__main__":
    main()
