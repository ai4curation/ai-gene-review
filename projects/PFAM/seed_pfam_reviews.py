#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Seed + self-validate entry-centric Pfam reviews under interpro/pfam/<PFAM>/.

Curating a Pfam family "as its own entry" (next to the machine-fetched
``<PFAM>-metadata.yaml``) captures far more than a flat SSSOM row can: the parent
InterPro entry, the *sibling* member families lumped under it, why an
InterPro-level GO mapping is not viable, and per-term relation/aspect/evidence/
confidence/status. This script writes those review files from a hand-authored
proposal table and verifies every structural claim, refusing to emit anything that
does not check out:

  1. proposed GO id exists in go-basic.obo and is not obsolete (+ aspect);
  2. the Pfam family exists in Pfam-A.clans;
  3. it is a member of the stated parent InterPro entry (member_list);
  4. that parent entry has >=2 Pfam members (heterogeneity proxy);
  5. that parent entry has NO interpro2go term equivalent to the proposal
     (the "InterPro not viable" premise) -- not the id nor an ancestor/descendant.

Output: interpro/pfam/<PFAM>/<PFAM>-review.yaml (one PfamEntryReview per family).
These are SEED files; once written they may be hand-edited (re-running overwrites,
so edit the PROPOSALS table here or the review files, not both). The biological
assignment is a reviewer claim flagged with confidence + status PROPOSED; each
needs curator / experimental validation.

Inputs: the ./data cache (interpro.xml.gz, interpro2go.txt, go-basic.obo,
Pfam-A.clans.tsv.gz) created by analyze_pfam_go_gaps.py --download + the Pfam FTP.

Validate the emitted reviews with:  just validate-pfam-reviews
"""
from __future__ import annotations

import collections
import csv
import gzip
import sys
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

import yaml

HERE = Path(__file__).parent
DATA = HERE / "data"
REPO = HERE.parent.parent              # repo root (…/ai-gene-review)
PFAM_DIR = REPO / "interpro" / "pfam"

ASPECT_RELATION = {
    "molecular_function": ("RO:0002327", "enables"),
    "biological_process": ("RO:0002331", "involved in"),
    "cellular_component": ("BFO:0000050", "part of"),
}

# ---------------------------------------------------------------------------
# Hand-authored proposals (same content as the retired SSSOM emitter). Each is a
# Pfam family whose specific GO term cannot sit on its heterogeneous parent
# InterPro entry. siblings + status are derived/added automatically.
# ---------------------------------------------------------------------------
PROPOSALS = [
    {"pfam": "PF14681", "parent_ipr": "IPR000836",
     "go": ["GO:0004845", "GO:0044206"], "confidence": "HIGH",
     "viability_reason": "PF00156 Pribosyltran is the generic phosphoribosyltransferase "
        "domain shared by APRT/HGPRT/OPRT/etc.; a uracil-specific term would be wrong for it.",
     "evidence": "Pfam family 'UPRTase' specifically models uracil phosphoribosyltransferases "
        "(Upp). The parent PRTase_dom domain spans many PRT substrates, so the uracil-specific "
        "term belongs at the Pfam level only."},
    {"pfam": "PF16363", "parent_ipr": "IPR016040",
     "go": ["GO:0008446"], "confidence": "HIGH",
     "viability_reason": "PF13460 NAD_binding_10 is a generic NAD(P)-binding Rossmann domain "
        "shared by many oxidoreductases; a dehydratase-specific term would be wrong for it.",
     "evidence": "Pfam family 'GDP_Man_Dehyd' models GDP-mannose 4,6-dehydratase (Gmd). The "
        "parent entry is a generic NAD(P)-binding fold, which cannot take a substrate-specific term."},
    {"pfam": "PF09043", "parent_ipr": "IPR015130",
     "go": ["GO:0047826"], "confidence": "HIGH",
     "viability_reason": "The entry groups two distinct adenosylcobalamin aminomutases "
        "(D-lysine 5,6 vs D-ornithine 4,5), so neither specific activity fits the whole entry.",
     "evidence": "Pfam family 'Lys-AminoMut_A' is the alpha-subunit TIM-barrel domain of "
        "D-lysine 5,6-aminomutase (adenosylcobalamin/B12-dependent)."},
    {"pfam": "PF16552", "parent_ipr": "IPR015130",
     "go": ["GO:0047831"], "confidence": "HIGH",
     "viability_reason": "Same heterogeneous entry as PF09043 (D-lysine 5,6 vs D-ornithine 4,5 "
        "aminomutase); the specific activity fits only the Pfam.",
     "evidence": "Pfam family 'OAM_alpha' is the alpha subunit of D-ornithine 4,5-aminomutase "
        "(adenosylcobalamin-dependent)."},
    {"pfam": "PF27512", "parent_ipr": "IPR000573",
     "go": ["GO:0003861", "GO:0009098"], "confidence": "HIGH",
     "viability_reason": "PF00694 Aconitase_C shares the aconitase/IPM-isomerase 'swivel' "
        "domain; aconitase is a different enzyme, so an IPM-dehydratase term cannot sit on the entry.",
     "evidence": "Pfam family 'LeuD' is the small subunit of 3-isopropylmalate dehydratase "
        "(isopropylmalate isomerase)."},
    {"pfam": "PF02431", "parent_ipr": "IPR016087",
     "go": ["GO:0045430"], "confidence": "HIGH",
     "viability_reason": "PF16035/PF16036 Chalcone_2/3 are chalcone-isomerase-like (CHIL) "
        "families including non-catalytic fatty-acid-binding members, so the catalytic term "
        "cannot sit on the entry.",
     "evidence": "Pfam family 'Chalcone' is chalcone-flavanone isomerase (CHI)."},
    {"pfam": "PF13360", "parent_ipr": "IPR002372",
     "go": ["GO:0043165"], "confidence": "HIGH",
     "viability_reason": "PF01011 PQQ and PF13570 are catalytic beta-propellers "
        "(quinoprotein dehydrogenase; beta-alanine-activating enzyme) sharing the fold; an "
        "OM-assembly term cannot sit on the entry.",
     "evidence": "Pfam family 'PQQ_2' is the outer-membrane protein assembly factor BamB, a "
        "BAM-complex accessory lipoprotein involved in Gram-negative OM biogenesis."},
    {"pfam": "PF07228", "parent_ipr": "IPR001932",
     "go": ["GO:0030435"], "confidence": "MEDIUM",
     "viability_reason": "PF00481/PF13672 PP2C are the generic PP2C-type protein-phosphatase "
        "domain (not sporulation-specific); the phosphatase MF is shared, but the sporulation "
        "process is SpoIIE-specific and cannot sit on the generic entry.",
     "evidence": "Pfam family 'SpoIIE' is the Stage II sporulation protein E phosphatase that "
        "activates sigma-F during Bacillus endospore formation. MEDIUM: some SpoIIE homologues "
        "occur outside canonical sporulation."},
    {"pfam": "PF13561", "parent_ipr": "IPR002347",
     "go": ["GO:0016631"], "confidence": "MEDIUM",
     "viability_reason": "PF00106 adh_short is the generic short-chain dehydrogenase/reductase "
        "(SDR) domain spanning thousands of substrates; no specific activity fits the entry.",
     "evidence": "Pfam family 'adh_short_C2' is annotated as enoyl-(acyl-carrier-protein) "
        "reductase (FabI/FabL-type). Cofactor-agnostic NAD(P)H term used pending confirmation "
        "of cofactor specificity."},
]


def parse_interpro(path: Path):
    pf2ipr, ipr_pfam, ipr_name, ipr_type = {}, collections.defaultdict(list), {}, {}
    cur, in_ml = None, False
    with gzip.open(path, "rb") as fh:
        for ev, el in ET.iterparse(fh, events=("start", "end")):
            if el.tag == "interpro":
                if ev == "start":
                    cur = el.get("id"); ipr_name[cur] = el.get("short_name"); ipr_type[cur] = el.get("type")
                else:
                    el.clear(); cur = None
            elif el.tag == "member_list":
                in_ml = ev == "start"
            elif el.tag == "db_xref" and ev == "start" and in_ml and cur and el.get("db") == "PFAM":
                pf2ipr[el.get("dbkey")] = cur
                ipr_pfam[cur].append(el.get("dbkey"))
    return pf2ipr, ipr_pfam, ipr_name, ipr_type


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
            print(f"ERROR: missing {n}; run analyze_pfam_go_gaps.py --download + fetch Pfam-A.clans.", file=sys.stderr)
            return 1

    pf2ipr, ipr_pfam, ipr_name, ipr_type = parse_interpro(DATA / "interpro.xml.gz")
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

    errors, reviews = [], {}
    for p in PROPOSALS:
        pf, ipr = p["pfam"], p["parent_ipr"]
        tag = f"{pf}->{ipr}"
        if pf not in meta:
            errors.append(f"{tag}: Pfam {pf} not in Pfam-A.clans"); continue
        if pf2ipr.get(pf) != ipr:
            errors.append(f"{tag}: {pf} member parent is {pf2ipr.get(pf)}, not {ipr}"); continue
        members = ipr_pfam.get(ipr, [])
        if len(members) < 2:
            errors.append(f"{tag}: parent {ipr} has only {len(members)} Pfam member(s)"); continue
        entry_go = {norm(g) for g in ipr2go.get(ipr, set())}
        ann = []
        for g in p["go"]:
            gn = norm(g)
            if gn not in go_name:
                errors.append(f"{tag}: GO {g} not in go-basic"); continue
            if gn in go_obs:
                errors.append(f"{tag}: GO {g} obsolete"); continue
            if gn in entry_go or ancestors(gn) & entry_go or any(gn in ancestors(eg) for eg in entry_go):
                errors.append(f"{tag}: parent {ipr} already maps {g} or a relative (premise false)"); continue
            aspect = go_ns[gn]
            rel_id, rel_label = ASPECT_RELATION[aspect]
            ann.append({
                "term": {"id": gn, "label": go_name[gn]},
                "relation": {"id": rel_id, "label": rel_label},
                "aspect": aspect,
                "confidence": p["confidence"],
                "evidence": p["evidence"],
                "status": "PROPOSED",
            })
        if not ann:
            continue
        siblings = [
            {"id": f"Pfam:{m}", "label": meta.get(m, {}).get("fam", m),
             "note": "member of the same InterPro entry"}
            for m in members if m != pf
        ]
        reviews[pf] = {
            "pfam_id": pf,
            "pfam_name": meta[pf]["fam"],
            "pfam_description": meta[pf]["desc"],
            "parent_interpro": {
                "id": f"InterPro:{ipr}",
                "label": ipr_name.get(ipr, ""),
                "type": ipr_type.get(ipr, ""),
                "n_pfam_members": len(members),
            },
            "interpro_go_status": "ABSENT" if not entry_go else "PRESENT_GENERAL",
            "interpro_mapping_viability": "NOT_VIABLE",
            "viability_reason": p["viability_reason"],
            "sibling_members": siblings,
            "proposed_annotations": ann,
            "notes": "Candidate review; needs curator / experimental validation "
                     "(confirm the Pfam family's coverage matches the activity via the SEED + "
                     "characterised members).",
            "curator": "AI Gene Review project",
            "review_date": "2026-06-20",
        }

    if errors:
        print("VALIDATION FAILED -- refusing to seed:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 2

    header = ("# Curated Pfam entry review (entry-centric; see "
              "src/ai_gene_review/schema/pfam_entry_review.yaml).\n"
              "# Sidecar to the machine-fetched {pf}-metadata.yaml (do not hand-edit metadata).\n"
              "# Seeded by projects/PFAM/seed_pfam_reviews.py; hand-editable thereafter.\n")
    for pf, review in reviews.items():
        d = PFAM_DIR / pf
        d.mkdir(parents=True, exist_ok=True)
        body = yaml.safe_dump(review, sort_keys=False, default_flow_style=False, width=100, allow_unicode=True)
        (d / f"{pf}-review.yaml").write_text(header.format(pf=pf) + body)

    print(f"OK: wrote {len(reviews)} Pfam entry reviews under {PFAM_DIR.relative_to(REPO)}/:")
    for pf in reviews:
        print(f"  interpro/pfam/{pf}/{pf}-review.yaml")
    write_index(reviews)
    return 0


def write_index(reviews: dict) -> None:
    """Emit a human-readable index of the entry reviews into projects/PFAM/PROPOSED_MAPPINGS.md."""
    asp = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}
    n_ann = sum(len(r["proposed_annotations"]) for r in reviews.values())
    out = []
    A = out.append
    A("---")
    A('title: "Proposed Pfam → GO Annotations (entry-centric reviews)"')
    A("---")
    A("")
    A("# Proposed Pfam → GO Annotations — where an InterPro mapping is not viable")
    A("")
    A("> Index of the curated **per-Pfam entry reviews** under "
      "`interpro/pfam/<PFAM>/<PFAM>-review.yaml` (schema: "
      "`src/ai_gene_review/schema/pfam_entry_review.yaml`). Seeded + structurally verified by "
      "`seed_pfam_reviews.py` (GO id non-obsolete; Pfam membership; parent entry heterogeneous; "
      "parent entry carries no equivalent term). Each proposed annotation is a **candidate "
      "needing curator / experimental validation**. See [parent project](../PFAM.md).")
    A("")
    A(f"**{n_ann} proposed annotations** across **{len(reviews)} Pfam families**. Each Pfam is "
      "curated as its own entry (with parent-entry + sibling context, per-term relation/aspect/"
      "evidence/confidence/status) rather than as a flat mapping row.")
    A("")
    A("| Pfam | family | review file | relation | proposed GO | aspect | conf. |")
    A("|---|---|---|---|---|---|---|")
    for pf, r in reviews.items():
        link = f"../../interpro/pfam/{pf}/{pf}-review.yaml"
        for i, a in enumerate(r["proposed_annotations"]):
            fam = r["pfam_name"] if i == 0 else ""
            fileref = f"[`{pf}-review.yaml`]({link})" if i == 0 else ""
            A(f"| {pf if i==0 else ''} | {fam} | {fileref} | {a['relation']['label']} | "
              f"{a['term']['id']} {a['term']['label']} | {asp.get(a['aspect'], a['aspect'])} | "
              f"{a['confidence']} |")
    A("")
    A("Each review records: parent InterPro entry (id/type/#members), `interpro_go_status`, "
      "`interpro_mapping_viability` + reason, the lumped sibling families, and the proposed "
      "annotations. Validate all with `just validate-pfam-reviews`.")
    A("")
    (HERE / "PROPOSED_MAPPINGS.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
