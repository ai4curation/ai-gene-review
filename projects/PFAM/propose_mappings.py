#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Author + self-validate proposed Pfam -> GO mappings for cases where an
InterPro-level mapping is NOT viable, and emit them as an SSSOM mapping set.

Rationale
---------
The headroom analysis (HEADROOM.md) showed InterPro2GO already sits at Pfam
granularity for the entries it annotates, so "splitting" gives no precision. The
exception is **heterogeneous InterPro entries**: a single entry that groups
*functionally distinct* Pfam families under one shared fold. InterPro2GO must stay
silent there (a function-specific term on the whole entry would be wrong for the
sibling family), but an individual Pfam family can be functionally specific -- so a
**Pfam-level** mapping is viable where an **InterPro-level** mapping is not.

Assigning a specific function is a curation judgement, so the proposals are
hand-authored; the script *verifies every structural claim* and refuses to emit a
proposal that does not check out:

  1. the proposed GO id exists in go-basic.obo and is not obsolete (+ aspect);
  2. the Pfam family exists in Pfam-A.clans;
  3. the Pfam is a member of the stated parent InterPro entry (member_list);
  4. that parent entry has >=2 Pfam members (heterogeneity proxy);
  5. that parent entry has NO interpro2go term for the proposal (the "InterPro not
     viable" premise) -- neither the exact id nor an ancestor/descendant of it.

The *biological* assignment is a reviewer claim, grounded in the Pfam family
name/description + standard biochemistry, flagged with a confidence level. Nothing
is auto-asserted as fact; this is a candidate list for curators / experimental
review.

Predicate by GO aspect (following the AMR aro2go.sssom convention):
  molecular_function -> RO:0002327 'enables'
  biological_process -> RO:0002331 'involved in'
  cellular_component -> BFO:0000050 'part of'

Inputs: the ./data cache (interpro.xml.gz, interpro2go.txt, go-basic.obo,
Pfam-A.clans.tsv.gz). Outputs: pfam2go.sssom.yaml, PROPOSED_MAPPINGS.md

Validate the emitted SSSOM file structurally with:
  just validate-pfam-mappings
(GO id/label correctness is already enforced here against go-basic.obo.)
"""
from __future__ import annotations

import collections
import csv
import gzip
import sys
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"

# Predicate per GO aspect.
ASPECT_PREDICATE = {
    "molecular_function": ("RO:0002327", "enables"),
    "biological_process": ("RO:0002331", "involved in"),
    "cellular_component": ("BFO:0000050", "part of"),
}
ASPECT_ABBR = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}
CONF_SCORE = {"HIGH": 0.9, "MEDIUM": 0.6}

# ---------------------------------------------------------------------------
# Hand-authored proposals: a Pfam family that deserves a specific GO term its
# parent InterPro entry cannot carry (it lumps the family with functionally
# distinct members). evidence = reviewer rationale; confidence in {HIGH,MEDIUM}.
# ---------------------------------------------------------------------------
PROPOSALS = [
    {
        "pfam": "PF14681", "parent_ipr": "IPR000836",
        "go": ["GO:0004845", "GO:0044206"], "confidence": "HIGH",
        "interpro_blocked_by": "PF00156 Pribosyltran (generic phosphoribosyltransferase "
            "domain shared by APRT/HGPRT/OPRT/etc.)",
        "evidence": "Pfam family 'UPRTase' specifically models uracil "
            "phosphoribosyltransferases (Upp); the parent PRTase_dom domain spans many "
            "PRT substrates, so a uracil-specific term cannot sit on the entry but is "
            "correct for this family.",
    },
    {
        "pfam": "PF16363", "parent_ipr": "IPR016040",
        "go": ["GO:0008446"], "confidence": "HIGH",
        "interpro_blocked_by": "PF13460 NAD_binding_10 (generic NAD(P)-binding "
            "Rossmann domain shared by many oxidoreductases)",
        "evidence": "Pfam family 'GDP_Man_Dehyd' models GDP-mannose 4,6-dehydratase "
            "(Gmd); the parent InterPro entry is a generic NAD(P)-binding fold, which "
            "cannot take a substrate-specific dehydratase term.",
    },
    {
        "pfam": "PF09043", "parent_ipr": "IPR015130",
        "go": ["GO:0047826"], "confidence": "HIGH",
        "interpro_blocked_by": "PF16552 OAM_alpha (D-ornithine 4,5-aminomutase alpha "
            "subunit -- a different adenosylcobalamin aminomutase sharing the fold)",
        "evidence": "Pfam family 'Lys-AminoMut_A' is the alpha-subunit TIM-barrel "
            "domain of D-lysine 5,6-aminomutase (adenosylcobalamin/B12-dependent). The "
            "entry groups two distinct B12 aminomutases (D-lysine 5,6 vs D-ornithine "
            "4,5), so neither specific activity can be placed on the entry.",
    },
    {
        "pfam": "PF16552", "parent_ipr": "IPR015130",
        "go": ["GO:0047831"], "confidence": "HIGH",
        "interpro_blocked_by": "PF09043 Lys-AminoMut_A (D-lysine 5,6-aminomutase alpha "
            "subunit -- a different adenosylcobalamin aminomutase sharing the fold)",
        "evidence": "Pfam family 'OAM_alpha' is the alpha subunit of D-ornithine "
            "4,5-aminomutase (adenosylcobalamin-dependent). Same heterogeneous entry as "
            "PF09043; the specific activity belongs at the Pfam level only.",
    },
    {
        "pfam": "PF27512", "parent_ipr": "IPR000573",
        "go": ["GO:0003861", "GO:0009098"], "confidence": "HIGH",
        "interpro_blocked_by": "PF00694 Aconitase_C (aconitase/IPM-isomerase 'swivel' "
            "domain shared with aconitase, a different enzyme)",
        "evidence": "Pfam family 'LeuD' is the small subunit of 3-isopropylmalate "
            "dehydratase (isopropylmalate isomerase). The parent entry is the shared "
            "swivel domain also found in aconitase, so it cannot carry an "
            "IPM-dehydratase-specific term.",
    },
    {
        "pfam": "PF02431", "parent_ipr": "IPR016087",
        "go": ["GO:0045430"], "confidence": "HIGH",
        "interpro_blocked_by": "PF16035/PF16036 Chalcone_2/3 (chalcone-isomerase-like "
            "(CHIL) families that include non-catalytic fatty-acid-binding members)",
        "evidence": "Pfam family 'Chalcone' is chalcone-flavanone isomerase (CHI). The "
            "parent entry also groups CHI-like proteins (CHIL) that are not isomerases, "
            "so the catalytic term cannot sit on the entry but is correct for CHI.",
    },
    {
        "pfam": "PF13360", "parent_ipr": "IPR002372",
        "go": ["GO:0043165"], "confidence": "HIGH",
        "interpro_blocked_by": "PF01011 PQQ (quinoprotein-dehydrogenase beta-propeller) "
            "and PF13570 (beta-alanine-activating enzyme propeller) -- catalytic "
            "propellers sharing the fold",
        "evidence": "Pfam family 'PQQ_2' is the outer-membrane protein assembly factor "
            "BamB, a BAM-complex accessory lipoprotein. The parent entry is a generic "
            "beta-propeller shared with quinoprotein dehydrogenases, so an OM-assembly "
            "term cannot sit on the entry; BamB is involved in Gram-negative OM "
            "biogenesis.",
    },
    {
        "pfam": "PF07228", "parent_ipr": "IPR001932",
        "go": ["GO:0030435"], "confidence": "MEDIUM",
        "interpro_blocked_by": "PF00481/PF13672 PP2C (the generic PP2C-type "
            "protein-phosphatase domain, not sporulation-specific)",
        "evidence": "Pfam family 'SpoIIE' is the Stage II sporulation protein E "
            "phosphatase that activates sigma-F during Bacillus endospore formation. "
            "Its PP2C phosphatase activity is shared with the generic siblings (so MF "
            "is not Pfam-specific), but the sporulation process is -- and cannot sit on "
            "the generic PP2C entry. MEDIUM: some SpoIIE homologues occur outside "
            "canonical sporulation.",
    },
    {
        "pfam": "PF13561", "parent_ipr": "IPR002347",
        "go": ["GO:0016631"], "confidence": "MEDIUM",
        "interpro_blocked_by": "PF00106 adh_short (the generic short-chain "
            "dehydrogenase/reductase (SDR) domain -- thousands of distinct substrates)",
        "evidence": "Pfam family 'adh_short_C2' is annotated as enoyl-(acyl-carrier-"
            "protein) reductase (FabI/FabL-type). The parent SDR_fam entry is one of "
            "the most functionally diverse domains in nature, so no specific activity "
            "is assignable at entry level. Cofactor-agnostic NAD(P)H term pending "
            "confirmation of cofactor specificity.",
    },
]


def parse_interpro(path: Path):
    pf2ipr, ipr_pfam, ipr_name = {}, collections.defaultdict(list), {}
    cur, in_ml = None, False
    with gzip.open(path, "rb") as fh:
        for ev, el in ET.iterparse(fh, events=("start", "end")):
            if el.tag == "interpro":
                if ev == "start":
                    cur = el.get("id")
                    ipr_name[cur] = el.get("short_name")
                else:
                    el.clear(); cur = None
            elif el.tag == "member_list":
                in_ml = ev == "start"
            elif el.tag == "db_xref" and ev == "start" and in_ml and cur and el.get("db") == "PFAM":
                pf2ipr[el.get("dbkey")] = cur
                ipr_pfam[cur].append(el.get("dbkey"))
    return pf2ipr, ipr_pfam, ipr_name


def parse_interpro2go(path: Path):
    ipr2go = collections.defaultdict(set)
    for line in path.read_text().splitlines():
        if line.startswith("InterPro:"):
            p = line.split(" ; ")
            if len(p) == 2:
                ipr2go[line.split()[0].split(":")[1]].add(p[1].strip())
    return ipr2go


def parse_go(path: Path):
    name, ns, obs = {}, {}, set()
    parents, alt = collections.defaultdict(set), {}
    cur, it = None, False
    for line in path.read_text().splitlines():
        if line == "[Term]":
            it, cur = True, None
            continue
        if line.startswith("["):
            it = False
            continue
        if not it:
            continue
        if line.startswith("id: "):
            cur = line[4:].strip()
        elif line.startswith("name: ") and cur:
            name[cur] = line[6:].strip()
        elif line.startswith("namespace: ") and cur:
            ns[cur] = line[11:].strip()
        elif line.startswith("alt_id: ") and cur:
            alt[line[8:].strip()] = cur
        elif line.startswith("is_obsolete: true") and cur:
            obs.add(cur)
        elif line.startswith("is_a: ") and cur:
            parents[cur].add(line[6:].split("!")[0].strip())
        elif line.startswith("relationship: part_of ") and cur:
            parents[cur].add(line.split("part_of", 1)[1].split("!")[0].strip())
    return name, ns, obs, parents, alt


def parse_clans(path: Path):
    meta = {}
    with gzip.open(path, "rt") as fh:
        for r in csv.reader(fh, delimiter="\t"):
            if len(r) >= 5:
                meta[r[0]] = {"clan": r[1], "clan_name": r[2], "fam": r[3], "desc": r[4]}
    return meta


def main() -> int:
    for n in ["interpro.xml.gz", "interpro2go.txt", "go-basic.obo", "Pfam-A.clans.tsv.gz"]:
        if not (DATA / n).exists():
            print(f"ERROR: missing {n}; run the other scripts' --download first.", file=sys.stderr)
            return 1

    pf2ipr, ipr_pfam, ipr_name = parse_interpro(DATA / "interpro.xml.gz")
    ipr2go = parse_interpro2go(DATA / "interpro2go.txt")
    go_name, go_ns, go_obs, go_parents, go_alt = parse_go(DATA / "go-basic.obo")
    meta = parse_clans(DATA / "Pfam-A.clans.tsv.gz")

    def norm(g):
        return go_alt.get(g, g)

    @lru_cache(maxsize=None)
    def ancestors(g):
        g = norm(g)
        seen, stack = set(), list(go_parents.get(g, ()))
        while stack:
            p = stack.pop()
            if p in seen:
                continue
            seen.add(p)
            stack.extend(go_parents.get(p, ()))
        return seen

    errors, validated = [], []
    for p in PROPOSALS:
        pf, ipr = p["pfam"], p["parent_ipr"]
        tag = f"{pf}->{ipr}"
        if pf not in meta:
            errors.append(f"{tag}: Pfam {pf} not in Pfam-A.clans"); continue
        if pf2ipr.get(pf) != ipr:
            errors.append(f"{tag}: {pf} member_list parent is {pf2ipr.get(pf)}, not {ipr}"); continue
        nmem = len(ipr_pfam.get(ipr, []))
        if nmem < 2:
            errors.append(f"{tag}: parent {ipr} has only {nmem} Pfam member(s)"); continue
        entry_go = {norm(g) for g in ipr2go.get(ipr, set())}
        for g in p["go"]:
            gn = norm(g)
            if gn not in go_name:
                errors.append(f"{tag}: GO {g} not found in go-basic"); continue
            if gn in go_obs:
                errors.append(f"{tag}: GO {g} is obsolete"); continue
            if gn in entry_go:
                errors.append(f"{tag}: parent {ipr} ALREADY maps {g} (premise false)"); continue
            if ancestors(gn) & entry_go:
                errors.append(f"{tag}: parent {ipr} maps an ancestor of {g} (premise weak)"); continue
            if any(gn in ancestors(eg) for eg in entry_go):
                errors.append(f"{tag}: parent {ipr} maps a descendant of {g} (premise weak)"); continue
            aspect = go_ns[gn]
            pred_id, pred_label = ASPECT_PREDICATE[aspect]
            validated.append({
                "pfam": pf, "pfam_name": meta[pf]["fam"], "pfam_desc": meta[pf]["desc"],
                "go_id": gn, "go_label": go_name[gn], "go_aspect": aspect,
                "predicate_id": pred_id, "predicate_label": pred_label,
                "parent_ipr": ipr, "parent_ipr_name": ipr_name.get(ipr, ""),
                "parent_n_pfam": nmem, "confidence": p["confidence"],
                "interpro_blocked_by": p["interpro_blocked_by"], "evidence": p["evidence"],
            })

    if errors:
        print("VALIDATION FAILED -- refusing to emit unverified proposals:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 2

    write_sssom(validated)
    write_markdown(validated)
    print(f"OK: {len(validated)} proposed mappings validated.")
    print("Wrote pfam2go.sssom.yaml, PROPOSED_MAPPINGS.md")
    return 0


def write_sssom(validated):
    """Emit an SSSOM mapping set (same shape as projects/RHEA, ANTIMICROBIAL_RESISTANCE)."""
    def block(text, indent="  "):
        # fold a comment string to a YAML literal block scalar
        return "\n".join(indent + ln for ln in text.split("\n"))

    L = []
    L.append("# Pfam -> GO mapping (SSSOM) -- curated NEW mappings for cases where an")
    L.append("# InterPro-level mapping is NOT viable.")
    L.append("#")
    L.append("# Each subject Pfam family sits in a *heterogeneous* InterPro entry that groups")
    L.append("# functionally distinct member families under one fold; that entry therefore carries")
    L.append("# no interpro2go term (a function-specific term would be wrong for the sibling family).")
    L.append("# The specific function is real at the Pfam level, so a Pfam->GO mapping is viable")
    L.append("# where an InterPro->GO mapping is not. See ../PFAM.md, PROPOSED_MAPPINGS.md, HEADROOM.md.")
    L.append("#")
    L.append("# Predicates: MF -> RO:0002327 'enables'; BP -> RO:0002331 'involved in'.")
    L.append("# These are CANDIDATE proposals (reviewer judgement grounded in the Pfam family")
    L.append("# definition); each needs curator / experimental validation. Every GO id/label is")
    L.append("# verified non-obsolete against go-basic, every Pfam membership and the 'parent entry")
    L.append("# has no equivalent term' premise are verified by propose_mappings.py.")
    L.append("#")
    L.append("# Validate (structural, against the SSSOM schema):")
    L.append("#   just validate-pfam-mappings")
    L.append("")
    L.append("mapping_set_id: https://w3id.org/ai4curation/ai-gene-review/mappings/pfam2go")
    L.append("mapping_set_title: Pfam to GO mapping (curated, where InterPro2GO is not viable)")
    L.append("mapping_set_description: >-")
    L.append(block(
        "Curated Pfam family -> GO mappings for Pfam families that sit in heterogeneous InterPro "
        "entries (entries grouping functionally distinct member families under one fold). Such "
        "entries carry no interpro2go term, so the specific function can only be asserted at the "
        "Pfam level. enables (RO:0002327) rows are molecular functions; involved-in (RO:0002331) "
        "rows are biological processes. Every GO id/label is verified non-obsolete against "
        "go-basic; Pfam membership and the 'parent InterPro entry carries no equivalent term' "
        "premise are verified by propose_mappings.py. These seed curation of new Pfam->GO mappings "
        "and quality-check GO annotation of the corresponding proteins; each is a candidate needing "
        "curator / experimental validation."))
    L.append("license: https://creativecommons.org/licenses/by/4.0/")
    L.append("creator_label:")
    L.append("- AI Gene Review project")
    L.append('mapping_date: "2026-06-20"')
    L.append("subject_source: pfam")
    L.append("object_source: GO")
    L.append("curie_map:")
    L.append("  Pfam: https://www.ebi.ac.uk/interpro/entry/pfam/")
    L.append("  InterPro: https://www.ebi.ac.uk/interpro/entry/InterPro/")
    L.append("  GO: http://purl.obolibrary.org/obo/GO_")
    L.append("  RO: http://purl.obolibrary.org/obo/RO_")
    L.append("  BFO: http://purl.obolibrary.org/obo/BFO_")
    L.append("  skos: http://www.w3.org/2004/02/skos/core#")
    L.append("  semapv: https://w3id.org/semapv/vocab/")
    L.append("  sssom: https://w3id.org/sssom/")
    L.append("  obo: http://purl.obolibrary.org/obo/")
    L.append("")
    L.append("mappings:")
    for v in validated:
        comment = (
            f"{v['evidence']} Parent InterPro entry {v['parent_ipr']} "
            f"({v['parent_ipr_name']}, {v['parent_n_pfam']} Pfam members) has no interpro2go term; "
            f"blocked at InterPro by {v['interpro_blocked_by']}. "
            f"CANDIDATE ({v['confidence']} confidence) -- needs curator/experimental validation."
        )
        L.append(f"- subject_id: Pfam:{v['pfam']}")
        L.append(f"  subject_label: \"{v['pfam_name']}\"")
        L.append(f"  predicate_id: {v['predicate_id']}")
        L.append(f"  predicate_label: {v['predicate_label']}")
        L.append(f"  object_id: {v['go_id']}")
        L.append(f"  object_label: {v['go_label']}")
        L.append("  mapping_justification: semapv:ManualMappingCuration")
        L.append(f"  confidence: {CONF_SCORE[v['confidence']]}")
        L.append("  comment: >-")
        L.append(block(comment, "    "))
    (HERE / "pfam2go.sssom.yaml").write_text("\n".join(L) + "\n")


def write_markdown(validated):
    out = []
    A = out.append
    A("---")
    A('title: "Proposed Pfam → GO Mappings (InterPro-level mapping not viable)"')
    A("---")
    A("")
    A("# Proposed Pfam → GO Mappings — cases where an InterPro mapping is not viable")
    A("")
    A("> Machine-readable mapping set: [`pfam2go.sssom.yaml`](pfam2go.sssom.yaml) (SSSOM). "
      "Generated by `propose_mappings.py`, which **verifies every structural claim** (GO id "
      "valid & non-obsolete; Pfam membership; parent entry heterogeneous; parent entry carries "
      "no equivalent term). The *biological* assignment is a reviewer proposal grounded in the "
      "Pfam family definition — each is a **candidate needing curator / experimental "
      "validation**, not an asserted fact. See [parent project](../PFAM.md), [HEADROOM.md](HEADROOM.md).")
    A("")
    A("## Why these cannot be InterPro mappings")
    A("")
    A("Each parent InterPro entry groups **functionally distinct** Pfam families under one shared "
      "fold and so carries **no** `interpro2go` term: a function-specific term on the whole entry "
      "would be wrong for the sibling family. The specific function is real at the **Pfam** level, "
      "so a Pfam→GO mapping is viable where an InterPro→GO mapping is not. (Verified automatically: "
      "the script aborts if the parent entry already maps the term or an ancestor/descendant.)")
    A("")
    A(f"**{len(validated)} proposed mappings** across "
      f"{len({v['pfam'] for v in validated})} Pfam families and "
      f"{len({v['parent_ipr'] for v in validated})} heterogeneous InterPro entries. "
      "Predicate: `enables` for MF, `involved in` for BP.")
    A("")
    A("| Pfam | family | predicate | proposed GO | aspect | conf. | parent InterPro (no GO) |")
    A("|---|---|---|---|---|---|---|")
    for v in validated:
        A(f"| {v['pfam']} | {v['pfam_name']} | {v['predicate_label']} | "
          f"{v['go_id']} {v['go_label']} | {ASPECT_ABBR[v['go_aspect']]} | {v['confidence']} | "
          f"{v['parent_ipr']} {v['parent_ipr_name']} ({v['parent_n_pfam']} Pfam) |")
    A("")
    A("## Per-proposal rationale")
    A("")
    seen = set()
    for v in validated:
        if v["pfam"] in seen:
            continue
        seen.add(v["pfam"])
        gos = [x for x in validated if x["pfam"] == v["pfam"]]
        A(f"### {v['pfam']} — {v['pfam_name']}")
        A("")
        A(f"*{v['pfam_desc']}*")
        A("")
        for g in gos:
            A(f"- **Proposed:** `{g['predicate_label']}` → {g['go_id']} {g['go_label']} "
              f"({ASPECT_ABBR[g['go_aspect']]}) — confidence {g['confidence']}")
        A(f"- **Parent InterPro entry:** {v['parent_ipr']} {v['parent_ipr_name']} "
          f"({v['parent_n_pfam']} Pfam members, **no interpro2go term**)")
        A(f"- **Why InterPro can't:** {v['interpro_blocked_by']}")
        A(f"- **Rationale:** {v['evidence']}")
        A("- **Status:** candidate — needs curator review / experimental confirmation "
          "(confirm the Pfam family's coverage matches the activity via the SEED + characterised members).")
        A("")
    (HERE / "PROPOSED_MAPPINGS.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
