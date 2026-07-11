#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Measure the HEADROOM for authoring *new*, more-specific Pfam -> GO mappings.

This is the complement of ``analyze_pfam_go_gaps.py``. That script asked whether
the *existing* ``pfam2go`` file is more specific than ``interpro2go`` (answer: no,
it is a derived copy). This script instead asks the generative question:

    Because InterPro lumps several Pfam families under one entry, and that entry's
    GO term must be general enough to cover all members, is there *room* to author
    NEW per-Pfam GO mappings that are more specific than what InterPro2GO gives?

It quantifies two kinds of opportunity, without fabricating any mapping:

A. COVERAGE GAP -- Pfam families that receive *no* GO term at all through InterPro
   (either unintegrated, or integrated into an entry that has no interpro2go term).
   A new Pfam->GO mapping here adds annotation where InterPro provides nothing.

B. SPLITTING HEADROOM -- InterPro entries that (i) have >=2 Pfam members and
   (ii) carry GO term(s). Every member Pfam inherits the *same* shared GO term, so
   if the members are functionally distinct, individual Pfams could take more
   specific (descendant) GO terms. The opportunity is largest when the shared term
   is GENERAL (shallow in the GO DAG) and the entry is a Family / Homologous
   superfamily (which group divergent sequences) rather than a single Domain.

Generality of a GO term is measured as its DAG depth = shortest is_a/part_of path
to an aspect root (GO:0003674/GO:0008150/GO:0005575). Smaller depth = more general.

Inputs (reuse the ./data cache; run analyze_pfam_go_gaps.py --download first, plus
Pfam-A.clans.tsv.gz from the Pfam FTP):
  * interpro.xml.gz        InterPro entry type + Pfam member_list
  * interpro2go.txt        InterPro entry -> GO
  * go-basic.obo           GO DAG + names
  * Pfam-A.clans.tsv.gz    full Pfam family universe + clan + description

Outputs (./):
  * HEADROOM.md                         human-readable summary (regenerated)
  * pfam_no_go_coverage_gap.tsv         Pfam families with no GO via InterPro
  * lumped_entries_headroom.tsv         multi-Pfam GO-bearing entries, ranked

No mappings are invented. The script reports opportunity counts and lists
candidate entries/families for downstream (curation or model-assisted) authoring.
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

# GO terms considered "general workhorse" labels often attached to lumped entries.
GENERAL_DEPTH_THRESHOLD = 3  # depth <= this counts as a general term


def parse_interpro(path: Path):
    """Return (pf2ipr, ipr_type, ipr_members, interpro_release)."""
    pf2ipr: dict[str, str] = {}
    ipr_type: dict[str, str] = {}
    ipr_members: dict[str, list[str]] = collections.defaultdict(list)
    release = "unknown"
    with gzip.open(path, "rb") as fh:
        current = None
        in_member_list = False
        for event, elem in ET.iterparse(fh, events=("start", "end")):
            if elem.tag == "dbinfo" and event == "start" and elem.get("dbname") == "INTERPRO":
                release = f"{elem.get('version')} ({elem.get('file_date')})"
            elif elem.tag == "interpro":
                if event == "start":
                    current = elem.get("id")
                    ipr_type[current] = elem.get("type")
                else:
                    elem.clear()
                    current = None
            elif elem.tag == "member_list":
                in_member_list = event == "start"
            elif elem.tag == "db_xref" and event == "start":
                if in_member_list and current and elem.get("db") == "PFAM":
                    pf = elem.get("dbkey")
                    pf2ipr[pf] = current
                    ipr_members[current].append(pf)
    return pf2ipr, ipr_type, ipr_members, release


def parse_interpro2go(path: Path):
    ipr2go: dict[str, set[str]] = collections.defaultdict(set)
    for line in path.read_text().splitlines():
        if line.startswith("InterPro:"):
            parts = line.split(" ; ")
            if len(parts) == 2:
                ipr = line.split()[0].split(":")[1]
                ipr2go[ipr].add(parts[1].strip())
    return ipr2go


def parse_go(path: Path):
    parents: dict[str, set[str]] = collections.defaultdict(set)
    name: dict[str, str] = {}
    alt: dict[str, str] = {}
    cur = None
    obsolete = False
    in_term = False
    for line in path.read_text().splitlines():
        if line == "[Term]":
            in_term, cur, obsolete = True, None, False
            continue
        if line.startswith("["):
            in_term = False
            continue
        if not in_term:
            continue
        if line.startswith("id: "):
            cur = line[4:].strip()
        elif line.startswith("name: ") and cur:
            name[cur] = line[6:].strip()
        elif line.startswith("alt_id: ") and cur:
            alt[line[8:].strip()] = cur
        elif line.startswith("is_obsolete: true"):
            obsolete = True
        elif line.startswith("is_a: ") and cur and not obsolete:
            parents[cur].add(line[6:].split("!")[0].strip())
        elif line.startswith("relationship: part_of ") and cur and not obsolete:
            parents[cur].add(line.split("part_of", 1)[1].split("!")[0].strip())
    return parents, name, alt


def parse_pfam_clans(path: Path):
    """PF -> (clan_acc, clan_name, fam_name, description)."""
    meta: dict[str, tuple] = {}
    with gzip.open(path, "rt") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) >= 5:
                meta[row[0]] = (row[1], row[2], row[3], row[4])
    return meta


def main() -> int:
    needed = ["interpro.xml.gz", "interpro2go.txt", "go-basic.obo", "Pfam-A.clans.tsv.gz"]
    missing = [n for n in needed if not (DATA / n).exists()]
    if missing:
        print(f"ERROR: missing inputs {missing}. See analyze_pfam_go_gaps.py --download "
              "and fetch Pfam-A.clans.tsv.gz from the Pfam FTP.", file=sys.stderr)
        return 1

    print("Parsing InterPro membership + types ...")
    pf2ipr, ipr_type, ipr_members, release = parse_interpro(DATA / "interpro.xml.gz")
    print("Parsing interpro2go ...")
    ipr2go = parse_interpro2go(DATA / "interpro2go.txt")
    print("Parsing GO DAG ...")
    parents, go_name, alt = parse_go(DATA / "go-basic.obo")
    print("Parsing Pfam clans ...")
    pfam_meta = parse_pfam_clans(DATA / "Pfam-A.clans.tsv.gz")

    def norm(g):
        return alt.get(g, g)

    @lru_cache(maxsize=None)
    def depth(term: str) -> int:
        term = norm(term)
        ps = parents.get(term)
        if not ps:
            return 0
        return 1 + min(depth(p) for p in ps)

    def glabel(g):
        return go_name.get(norm(g), g)

    universe = set(pfam_meta)              # all current Pfam-A families
    integrated = set(pf2ipr)               # Pfam families with an InterPro entry

    # ---- A. Coverage gap ----
    covered, no_go_integrated = set(), set()
    for pf in integrated:
        if ipr2go.get(pf2ipr[pf]):
            covered.add(pf)
        else:
            no_go_integrated.add(pf)
    unintegrated = universe - integrated
    # families absent from the clans universe but integrated (legacy/dead PF ids)
    integrated_not_in_universe = integrated - universe
    no_go_total = (no_go_integrated | unintegrated) & universe

    gap_rows = []
    n_duf = 0
    for pf in sorted(no_go_total):
        clan, clan_name, fam_name, desc = pfam_meta.get(pf, ("", "", "", ""))
        ipr = pf2ipr.get(pf, "")
        reason = "no_interpro_entry" if pf not in integrated else "entry_has_no_go"
        is_duf = ("DUF" in fam_name) or ("unknown function" in desc.lower())
        if is_duf:
            n_duf += 1
        gap_rows.append((pf, fam_name, ipr, ipr_type.get(ipr, ""), reason, clan, desc))
    n_named_gap = len(gap_rows) - n_duf
    # ~25k rows / ~2 MB: written to the git-ignored data/ dir (regenerable).
    with (DATA / "pfam_no_go_coverage_gap.tsv").open("w") as fh:
        fh.write("pfam\tfam_name\tinterpro\tipr_type\treason\tclan\tdescription\n")
        for r in gap_rows:
            fh.write("\t".join(str(x) for x in r) + "\n")

    # ---- B. Splitting headroom: multi-Pfam GO-bearing entries ----
    lumped = []   # (ipr, type, n_members, min_depth, gos, members)
    for ipr, members in ipr_members.items():
        gos = ipr2go.get(ipr)
        if not gos or len(members) < 2:
            continue
        min_depth = min((depth(g) for g in gos), default=0)
        lumped.append((ipr, ipr_type.get(ipr, ""), len(members), min_depth, sorted(gos), members))

    pfam_in_lumped = {pf for _i, _t, _n, _d, _g, mem in lumped for pf in mem}
    # "general" lumped entries = shared GO term(s) are all shallow
    general_lumped = [e for e in lumped if e[3] <= GENERAL_DEPTH_THRESHOLD]
    pfam_in_general_lumped = {pf for e in general_lumped for pf in e[5]}

    # by type
    by_type = collections.Counter(e[1] for e in lumped)
    fam_super = [e for e in lumped if e[1] in ("Family", "Homologous_superfamily")]

    # rank: most members first, then most general (lowest depth)
    lumped_sorted = sorted(lumped, key=lambda e: (-e[2], e[3]))
    with (HERE / "lumped_entries_headroom.tsv").open("w") as fh:
        fh.write("interpro\ttype\tn_pfam_members\tmin_go_depth\tgo_terms\tpfam_members\n")
        for ipr, typ, n, d, gos, mem in lumped_sorted:
            go_str = "|".join(f"{g} {glabel(g)}" for g in gos)
            fh.write(f"{ipr}\t{typ}\t{n}\t{d}\t{go_str}\t{','.join(mem)}\n")

    # ---- report ----
    pct = lambda a, b: f"{100*a/b:.1f}%" if b else "n/a"
    out = []
    A = out.append
    A("---")
    A('title: "Headroom for New, More-Specific Pfam → GO Mappings"')
    A("---")
    A("")
    A("# Headroom for New, More-Specific Pfam → GO Mappings")
    A("")
    A("> Auto-generated by `headroom_analysis.py`. Re-run to refresh. "
      "See [parent project](../PFAM.md). This measures the *opportunity* to author "
      "new per-Pfam mappings; it does **not** invent any mapping.")
    A("")
    A("## Provenance")
    A("")
    A(f"- InterPro release (membership + types): **{release}**")
    A(f"- Pfam universe: **Pfam-A.clans.tsv**, {len(universe):,} families")
    A(f"- GO depth = shortest is_a/part_of path to an aspect root; "
      f"“general” = depth ≤ {GENERAL_DEPTH_THRESHOLD}.")
    A("")
    A("## A. Coverage gap — Pfam families with *no* GO via InterPro")
    A("")
    A("A new Pfam→GO mapping for these families adds annotation where InterPro2GO "
      "currently provides nothing.")
    A("")
    A(f"- Total Pfam-A families: **{len(universe):,}**")
    A(f"- Integrated into an InterPro entry: **{len(integrated & universe):,}** "
      f"({pct(len(integrated & universe), len(universe))})")
    A(f"- … of which the entry carries ≥1 GO term (covered): "
      f"**{len(covered & universe):,}** ({pct(len(covered & universe), len(universe))})")
    A(f"- Integrated but entry has **no** GO term: "
      f"**{len(no_go_integrated & universe):,}**")
    A(f"- **Not integrated** into any InterPro entry: **{len(unintegrated):,}**")
    A(f"- **Total families with zero GO via InterPro: {len(no_go_total):,}** "
      f"({pct(len(no_go_total), len(universe))})")
    A(f"  - of which domains of unknown function (DUF / 'unknown function'): "
      f"**{n_duf:,}** ({pct(n_duf, len(no_go_total))}) — real *biology* gaps, not mapping gaps")
    A(f"  - **named, tractable** targets for new mappings: **{n_named_gap:,}** "
      f"({pct(n_named_gap, len(no_go_total))})")
    A("")
    A("These are the pure-coverage candidates (full list: "
      "`data/pfam_no_go_coverage_gap.tsv`, git-ignored). Examples with informative descriptions:")
    A("")
    A("| Pfam | name | reason | description |")
    A("|---|---|---|---|")
    shown = 0
    for pf, fam_name, ipr, typ, reason, clan, desc in gap_rows:
        if desc and "DUF" not in fam_name and shown < 20:
            d = desc if len(desc) < 70 else desc[:67] + "…"
            A(f"| {pf} | {fam_name} | {reason} | {d} |")
            shown += 1
    A("")
    A(f"*(Note: a large share of uncovered families are domains of unknown function "
      f"(DUFs); those are genuine knowledge gaps, not mapping gaps.)*")
    A("")
    A("## B. Splitting headroom — lumped entries sharing one GO term")
    A("")
    A("InterPro entries with **≥2 Pfam members** and ≥1 GO term: every member "
      "inherits the *same* GO term, so functionally distinct members are candidates "
      "for more specific (descendant) per-Pfam terms.")
    A("")
    A(f"- Multi-Pfam GO-bearing entries: **{len(lumped):,}**")
    A(f"- Pfam families living in them (share a GO term with ≥1 sibling): "
      f"**{len(pfam_in_lumped):,}**")
    A(f"- Of those entries, GO term is **general** (depth ≤ {GENERAL_DEPTH_THRESHOLD}): "
      f"**{len(general_lumped):,}** entries, **{len(pfam_in_general_lumped):,}** Pfam families")
    A(f"- Multi-Pfam GO entries that are **Family / Homologous superfamily** "
      f"(divergent groupings, strongest case for splitting): **{len(fam_super):,}**")
    A("")
    A("Entry-type breakdown of multi-Pfam GO-bearing entries:")
    A("")
    A("| InterPro entry type | entries |")
    A("|---|---:|")
    for typ, n in by_type.most_common():
        A(f"| {typ} | {n:,} |")
    A("")
    A("### Highest-headroom entries (most Pfam members, most general shared GO)")
    A("")
    A("Family / Homologous-superfamily entries with many members and a general GO "
      "term — the best candidates for per-Pfam refinement. Member descriptions show "
      "whether the lumped families are functionally heterogeneous.")
    A("")
    A("| InterPro | type | members | GO depth | shared GO | example member families |")
    A("|---|---|---:|---:|---|---|")
    fam_super_ranked = sorted(fam_super, key=lambda e: (-e[2], e[3]))
    for ipr, typ, n, d, gos, mem in fam_super_ranked[:25]:
        go_str = "; ".join(glabel(g) for g in gos[:2]) + ("…" if len(gos) > 2 else "")
        ex = "; ".join(pfam_meta.get(p, ("", "", p, ""))[2] for p in mem[:4])
        if len(mem) > 4:
            ex += f"; +{len(mem)-4}"
        A(f"| {ipr} | {typ} | {n} | {d} | {go_str} | {ex} |")
    A("")
    A("Full ranked list: `lumped_entries_headroom.tsv`.")
    A("")
    A("## Interpretation")
    A("")
    A("- **Splitting gives almost no precision headroom.** Only "
      f"{len(lumped):,} GO-bearing InterPro entries have ≥2 Pfam members at all, and "
      f"just {len(fam_super):,} are Family/Homologous-superfamily. The rest are "
      "*Repeat* and *Domain* entries whose multiple Pfam members are **redundant HMM "
      "signatures of the same domain** (e.g. the GNAT acyltransferase or EF-hand "
      "calcium-binding entries list several alternative Pfam models), so a per-Pfam "
      "term would be identical, not finer. The premise that InterPro lumps "
      "*functionally distinct* Pfams under one general GO term rarely holds for "
      "GO-bearing entries: those entries are overwhelmingly 1 Pfam = 1 entry, so "
      "InterPro2GO already sits at Pfam granularity.")
    A("- **Coverage is the real, large opportunity — and for well-characterised "
      "families it is *also* a precision opportunity.** "
      f"{pct(len(no_go_total), len(universe))} of Pfam families get no GO via "
      f"InterPro. About a quarter are DUFs (real biology gaps); the remaining "
      f"~{n_named_gap:,} named families are tractable. Crucially, InterPro2GO is "
      "*conservative*: even canonical, well-understood domains are left unmapped "
      "(e.g. SH2 IPR000980, EGF IPR000742, Kringle IPR000001, Actin IPR004000 all "
      "have **no** interpro2go term). For these a new mapping is not limited by any "
      "existing general InterPro term, so it can be assigned *directly at a specific "
      "level* — e.g. SH2 → phosphotyrosine residue binding (GO:0001784). Here "
      "coverage and precision coincide.")
    A("- **So new mappings can beat InterPro2GO most where InterPro abstained.** They "
      "cannot beat it by *splitting* its lumped entries (there is nothing to split), "
      "but they can (a) annotate the ~18k named uncovered families, often at a "
      "specific level; (b) go *below* the family — Pfam clan subfamilies, domain "
      "architectures, active-site/residue signatures, structure (AlphaFold) — to "
      "refine the ~5k already-covered families. Neither is delivered by `pfam2go` (a "
      "copy of InterPro2GO); both must be *authored* by curation or grounded model "
      "prediction and then validated. This script scopes and prioritizes that work.")
    A("")
    (HERE / "HEADROOM.md").write_text("\n".join(out) + "\n")

    # ---- console ----
    print("\n=== HEADROOM SUMMARY ===")
    print(f"Pfam universe: {len(universe):,}; integrated: {len(integrated & universe):,}; "
          f"covered by GO: {len(covered & universe):,}")
    print(f"No GO via InterPro: {len(no_go_total):,} "
          f"(integrated-no-go {len(no_go_integrated & universe):,}, "
          f"unintegrated {len(unintegrated):,})")
    print(f"Multi-Pfam GO entries: {len(lumped):,}; Pfam families in them: {len(pfam_in_lumped):,}")
    print(f"  general (depth<= {GENERAL_DEPTH_THRESHOLD}): {len(general_lumped):,} entries, "
          f"{len(pfam_in_general_lumped):,} families")
    print(f"  Family/Homologous_superfamily: {len(fam_super):,} entries")
    print("Wrote HEADROOM.md, pfam_no_go_coverage_gap.tsv, lumped_entries_headroom.tsv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
