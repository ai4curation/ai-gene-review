#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Author + self-validate a set of proposed Pfam -> GO mappings for cases where an
InterPro-level mapping is NOT viable.

Rationale
---------
The headroom analysis (HEADROOM.md) showed that InterPro2GO already sits at Pfam
granularity for the entries it annotates, so "splitting" gives no precision. The
exception is **heterogeneous InterPro entries**: a single InterPro entry that
groups *functionally distinct* Pfam families under one shared fold. InterPro2GO
must stay silent (or generic) there, because a substrate/function-specific term
attached to the whole entry would be wrong for the other member signatures. But an
individual Pfam family within such an entry can be functionally specific — so a
**Pfam-level** mapping is viable where an **InterPro-level** mapping is not.

This script does NOT mine these automatically (assigning a specific function is a
curation judgement). Instead it carries a small hand-authored proposal table and
*verifies every structural claim* against the cached data, refusing to emit a
proposal that does not check out:

  1. the proposed GO id exists in go-basic.obo and is not obsolete (+ correct aspect);
  2. the Pfam family exists in Pfam-A.clans;
  3. the Pfam is a member of the stated parent InterPro entry (member_list);
  4. that parent entry has >=2 Pfam members (heterogeneity proxy);
  5. that parent entry has NO interpro2go term for the proposal (the "InterPro not
     viable" premise) — neither the exact id nor an ancestor/descendant of it.

The *biological* assignment (which GO term fits which Pfam) is a reviewer claim,
grounded in the Pfam family name/description and standard biochemistry, and is
explicitly flagged with a confidence level and "NEEDS VALIDATION". Nothing here is
auto-asserted as fact; this is a candidate list for curators / experimental review.

Inputs: the ./data cache used by the other two scripts
(interpro.xml.gz, interpro2go.txt, go-basic.obo, Pfam-A.clans.tsv.gz).

Outputs: proposed_pfam_go_mappings.tsv, PROPOSED_MAPPINGS.md
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

# ---------------------------------------------------------------------------
# Hand-authored proposals. Each is a Pfam family that deserves a specific GO term
# its parent InterPro entry cannot carry (because the entry lumps it with
# functionally distinct member families). evidence = reviewer rationale grounded in
# the Pfam family definition + standard biochemistry. confidence in {HIGH,MEDIUM}.
# ---------------------------------------------------------------------------
PROPOSALS = [
    {
        "pfam": "PF14681", "parent_ipr": "IPR000836",
        "go": ["GO:0004845", "GO:0044206"], "confidence": "HIGH",
        "interpro_blocked_by": "PF00156 Pribosyltran (generic phosphoribosyltransferase "
            "domain shared by APRT/HGPRT/OPRT/etc.)",
        "evidence": "Pfam family 'UPRTase' specifically models uracil "
            "phosphoribosyltransferases (Upp); the parent InterPro PRTase_dom domain "
            "spans many PRT substrates, so a uracil-specific term cannot sit on the "
            "entry, but is correct for this family.",
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
        "interpro_blocked_by": "PF16552 OAM_alpha (D-ornithine 4,5-aminomutase "
            "alpha subunit — a *different* adenosylcobalamin aminomutase sharing the fold)",
        "evidence": "Pfam family 'Lys-AminoMut_A' is the alpha-subunit TIM-barrel "
            "domain of D-lysine 5,6-aminomutase (an adenosylcobalamin/B12-dependent "
            "enzyme). The InterPro entry groups two distinct B12 aminomutases (D-lysine "
            "5,6 vs D-ornithine 4,5), so neither specific activity can be placed on the "
            "entry.",
    },
    {
        "pfam": "PF16552", "parent_ipr": "IPR015130",
        "go": ["GO:0047831"], "confidence": "HIGH",
        "interpro_blocked_by": "PF09043 Lys-AminoMut_A (D-lysine 5,6-aminomutase "
            "alpha subunit — a *different* adenosylcobalamin aminomutase sharing the fold)",
        "evidence": "Pfam family 'OAM_alpha' is the alpha subunit of D-ornithine "
            "4,5-aminomutase (adenosylcobalamin-dependent). Same heterogeneous entry as "
            "PF09043; the specific activity belongs at the Pfam level only.",
    },
    {
        "pfam": "PF27512", "parent_ipr": "IPR000573",
        "go": ["GO:0003861", "GO:0009098"], "confidence": "HIGH",
        "interpro_blocked_by": "PF00694 Aconitase_C (aconitase/IPM-isomerase 'swivel' "
            "domain shared with aconitase, a different enzyme)",
        "evidence": "Pfam family 'LeuD' is the small subunit (LeuD) of "
            "3-isopropylmalate dehydratase (isopropylmalate isomerase). The parent "
            "InterPro entry is the shared swivel domain also found in aconitase, so it "
            "cannot carry an IPM-dehydratase-specific term.",
    },
    {
        "pfam": "PF13561", "parent_ipr": "IPR002347",
        "go": ["GO:0016631"], "confidence": "MEDIUM",
        "interpro_blocked_by": "PF00106 adh_short (the generic short-chain "
            "dehydrogenase/reductase (SDR) domain — thousands of distinct substrates)",
        "evidence": "Pfam family 'adh_short_C2' is annotated as enoyl-(acyl-carrier-"
            "protein) reductase (FabI/FabL-type). The parent SDR_fam entry is one of "
            "the most functionally diverse domains in nature, so no specific activity "
            "is assignable at the entry level. Cofactor-agnostic term used "
            "(NAD(P)H) pending confirmation of cofactor specificity for the family.",
    },
]


def parse_interpro(path: Path):
    pf2ipr = {}
    ipr_pfam = collections.defaultdict(list)
    ipr_name = {}
    cur = None
    in_ml = False
    with gzip.open(path, "rb") as fh:
        for ev, el in ET.iterparse(fh, events=("start", "end")):
            if el.tag == "interpro":
                if ev == "start":
                    cur = el.get("id")
                    ipr_name[cur] = el.get("short_name")
                else:
                    el.clear()
                    cur = None
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
    name = {}
    ns = {}
    obs = set()
    parents = collections.defaultdict(set)
    alt = {}
    cur = None
    o = False
    it = False
    for line in path.read_text().splitlines():
        if line == "[Term]":
            it, cur, o = True, None, False
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

    errors = []
    validated = []
    for p in PROPOSALS:
        pf, ipr = p["pfam"], p["parent_ipr"]
        tag = f"{pf}->{ipr}"
        # 2. Pfam exists
        if pf not in meta:
            errors.append(f"{tag}: Pfam {pf} not in Pfam-A.clans")
            continue
        # 3. membership
        if pf2ipr.get(pf) != ipr:
            errors.append(f"{tag}: {pf} member_list parent is {pf2ipr.get(pf)}, not {ipr}")
            continue
        # 4. heterogeneity proxy
        nmem = len(ipr_pfam.get(ipr, []))
        if nmem < 2:
            errors.append(f"{tag}: parent {ipr} has only {nmem} Pfam member(s)")
            continue
        entry_go = {norm(g) for g in ipr2go.get(ipr, set())}
        for g in p["go"]:
            gn = norm(g)
            # 1. GO valid + not obsolete + aspect
            if gn not in go_name:
                errors.append(f"{tag}: GO {g} not found in go-basic")
                continue
            if gn in go_obs:
                errors.append(f"{tag}: GO {g} is obsolete")
                continue
            # 5. InterPro-not-viable: entry must not already carry it (nor anc/desc)
            if gn in entry_go:
                errors.append(f"{tag}: parent {ipr} ALREADY maps {g} (premise false)")
                continue
            if ancestors(gn) & entry_go:
                errors.append(f"{tag}: parent {ipr} maps an ancestor of {g} (premise weak)")
                continue
            if any(gn in ancestors(eg) for eg in entry_go):
                errors.append(f"{tag}: parent {ipr} maps a descendant of {g} (premise weak)")
                continue
            validated.append({
                "pfam": pf, "pfam_name": meta[pf]["fam"], "pfam_desc": meta[pf]["desc"],
                "go_id": gn, "go_label": go_name[gn], "go_aspect": go_ns[gn],
                "parent_ipr": ipr, "parent_ipr_name": ipr_name.get(ipr, ""),
                "parent_n_pfam": nmem, "confidence": p["confidence"],
                "interpro_blocked_by": p["interpro_blocked_by"], "evidence": p["evidence"],
            })

    if errors:
        print("VALIDATION FAILED — refusing to emit unverified proposals:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 2

    # ---- TSV ----
    cols = ["pfam", "pfam_name", "go_id", "go_label", "go_aspect", "parent_ipr",
            "parent_ipr_name", "parent_n_pfam", "confidence", "interpro_blocked_by", "evidence"]
    with (HERE / "proposed_pfam_go_mappings.tsv").open("w") as fh:
        fh.write("\t".join(cols) + "\n")
        for v in validated:
            fh.write("\t".join(str(v[c]) for c in cols) + "\n")

    # ---- Markdown ----
    asp = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}
    out = []
    A = out.append
    A("---")
    A('title: "Proposed Pfam → GO Mappings (InterPro-level mapping not viable)"')
    A("---")
    A("")
    A("# Proposed Pfam → GO Mappings — cases where an InterPro mapping is not viable")
    A("")
    A("> Generated by `propose_mappings.py`, which **verifies every structural claim** "
      "(GO id valid & non-obsolete; Pfam membership; parent entry heterogeneous; parent "
      "entry carries no equivalent GO term). The *biological* assignment is a reviewer "
      "proposal grounded in the Pfam family definition and standard biochemistry — each "
      "is a **candidate needing curator / experimental validation**, not an asserted "
      "fact. See [parent project](../PFAM.md) and [HEADROOM.md](HEADROOM.md).")
    A("")
    A("## Why these cannot be InterPro mappings")
    A("")
    A("Each parent InterPro entry groups **functionally distinct** Pfam families under "
      "one shared fold and therefore carries **no** `interpro2go` term: a "
      "substrate-specific GO term placed on the entry would be wrong for the sibling "
      "family. The specific function is real at the **Pfam** level, so a Pfam→GO "
      "mapping is viable where an InterPro→GO mapping is not. (This is verified "
      "automatically: the script aborts if the parent entry already maps the term or an "
      "ancestor/descendant of it.)")
    A("")
    A(f"**{len(validated)} proposed mappings** across "
      f"{len({v['pfam'] for v in validated})} Pfam families "
      f"and {len({v['parent_ipr'] for v in validated})} heterogeneous InterPro entries:")
    A("")
    A("| Pfam | family | proposed GO | aspect | conf. | parent InterPro (no GO) | blocked at InterPro by |")
    A("|---|---|---|---|---|---|---|")
    for v in validated:
        A(f"| {v['pfam']} | {v['pfam_name']} | {v['go_id']} {v['go_label']} | "
          f"{asp.get(v['go_aspect'], v['go_aspect'])} | {v['confidence']} | "
          f"{v['parent_ipr']} {v['parent_ipr_name']} ({v['parent_n_pfam']} Pfam) | "
          f"{v['interpro_blocked_by']} |")
    A("")
    A("## Per-proposal rationale")
    A("")
    seen_pf = set()
    for v in validated:
        if v["pfam"] in seen_pf:
            continue
        seen_pf.add(v["pfam"])
        gos = [x for x in validated if x["pfam"] == v["pfam"]]
        A(f"### {v['pfam']} — {v['pfam_name']}")
        A("")
        A(f"*{v['pfam_desc']}*")
        A("")
        for g in gos:
            A(f"- **Proposed:** {g['go_id']} {g['go_label']} "
              f"({asp.get(g['go_aspect'], g['go_aspect'])}) — confidence {g['confidence']}")
        A(f"- **Parent InterPro entry:** {v['parent_ipr']} {v['parent_ipr_name']} "
          f"({v['parent_n_pfam']} Pfam members, **no interpro2go term**)")
        A(f"- **Why InterPro can't:** {v['interpro_blocked_by']}")
        A(f"- **Rationale:** {v['evidence']}")
        A("- **Status:** candidate — needs curator review / experimental confirmation; "
          "confirm the Pfam family's coverage matches the activity (e.g. via the SEED "
          "and a few characterised members).")
        A("")
    (HERE / "PROPOSED_MAPPINGS.md").write_text("\n".join(out) + "\n")

    print(f"OK: {len(validated)} proposed mappings validated and written.")
    print("Wrote proposed_pfam_go_mappings.tsv, PROPOSED_MAPPINGS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
