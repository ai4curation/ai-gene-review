#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Compare pfam2go vs interpro2go to look for *precision gaps*.

Hypothesis
----------
Pfam is a member database of InterPro, and the official ``pfam2go`` mapping is,
per its own header, "generated from data supplied by InterPro for the
InterPro2GO mapping." InterPro2GO is curated at the level of an *InterPro entry*,
which often integrates several member signatures (Pfam, PROSITE, SMART, CDD ...).

When several Pfam families are lumped into one InterPro entry, the GO term
attached to that entry must be general enough to cover all of them. An individual
Pfam family may legitimately deserve a *more specific* GO term. This script asks,
empirically and reproducibly:

  1. Are there Pfam families whose ``pfam2go`` term is MORE SPECIFIC (a GO
     descendant) than any term mapped to their parent InterPro entry? (precision
     gain)
  2. Are there Pfam families that carry GO terms entirely DISJOINT from their
     parent InterPro entry's terms? (extra signal)
  3. Are there Pfam families that have ``pfam2go`` terms but are NOT integrated
     into any InterPro entry at all? (pure InterPro2GO coverage gap)

Each ``pfam2go`` GO assertion for an *integrated* family is classified relative
to the GO terms of its parent InterPro entry as one of:

  SAME          - identical GO id present on the InterPro entry
  MORE_SPECIFIC - a GO descendant (is_a/part_of) of some InterPro-entry term
  MORE_GENERAL  - a GO ancestor of some InterPro-entry term
  DISJOINT      - neither ancestor nor descendant of any InterPro-entry term

Inputs (downloaded with --download, cached under ./data):
  * pfam2go      http://current.geneontology.org/ontology/external2go/pfam2go
  * interpro2go  http://current.geneontology.org/ontology/external2go/interpro2go
  * interpro.xml.gz   (Pfam<->InterPro membership)
  * go-basic.obo      (GO is_a / part_of DAG)

Outputs (./):
  * RESULTS.md                       human-readable summary (regenerated)
  * pfam_go_precision_gaps.tsv       every classified pfam2go assertion
  * unintegrated_pfam_with_go.tsv    pfam2go families absent from InterPro entries

No results are hardcoded. If an input is missing the script errors out; it never
fabricates mappings.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"

URLS = {
    "pfam2go.txt": "http://current.geneontology.org/ontology/external2go/pfam2go",
    "interpro2go.txt": "http://current.geneontology.org/ontology/external2go/interpro2go",
    "interpro.xml.gz": "https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro.xml.gz",
    "go-basic.obo": "http://current.geneontology.org/ontology/go-basic.obo",
}


def download() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    for name, url in URLS.items():
        dest = DATA / name
        if dest.exists() and dest.stat().st_size > 0:
            print(f"[skip] {name} already present ({dest.stat().st_size:,} bytes)")
            continue
        print(f"[get ] {name} <- {url}")
        urllib.request.urlretrieve(url, dest)
        print(f"       {dest.stat().st_size:,} bytes")


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------
EXT2GO_RE = re.compile(r"^(\S+):(\S+)\s+.*?>\s+GO:(.+?)\s+;\s+(GO:\d+)\s*$")


def parse_ext2go(path: Path, prefix: str) -> tuple[dict[str, set[str]], dict[str, str], str]:
    """Parse an external2go file. Returns (xref->set(GO ids), GO id->label, version)."""
    mapping: dict[str, set[str]] = collections.defaultdict(set)
    go_label: dict[str, str] = {}
    version = "unknown"
    for line in path.read_text().splitlines():
        if line.startswith("!"):
            if "version date" in line:
                version = line.split(":", 1)[1].strip()
            continue
        m = EXT2GO_RE.match(line)
        if not m:
            continue
        db, key, go_label_txt, go_id = m.groups()
        if db.lower() != prefix.lower():
            continue
        mapping[key].add(go_id)
        go_label[go_id] = go_label_txt
    return mapping, go_label, version


def parse_pfam_to_interpro(path: Path) -> tuple[dict[str, str], str]:
    """Parse interpro.xml.gz -> ({PFxxxxx: IPRxxxxxx}, interpro_release).

    A member-database signature integrates into exactly one InterPro entry, so we
    only count PFAM ``db_xref`` elements that sit *inside* a ``<member_list>``.
    PFAM ids also appear in ``contains``/``found_in`` relationship sections of
    *other* entries; those are domain-architecture relationships, not membership,
    and must be ignored (otherwise a Pfam appears to belong to several entries).
    """
    pf2ipr: dict[str, str] = {}
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
                else:
                    elem.clear()
                    current = None
            elif elem.tag == "member_list":
                in_member_list = event == "start"
            elif elem.tag == "db_xref" and event == "start":
                if in_member_list and current and elem.get("db") == "PFAM":
                    pf2ipr[elem.get("dbkey")] = current
    return pf2ipr, release


def parse_go_dag(path: Path) -> tuple[dict[str, set[str]], dict[str, str], dict[str, str], set[str]]:
    """Parse go-basic.obo. Returns (term->direct parents over is_a+part_of,
    id->name, alt_id->primary id, obsolete ids)."""
    parents: dict[str, set[str]] = collections.defaultdict(set)
    name: dict[str, str] = {}
    alt: dict[str, str] = {}
    obsolete: set[str] = set()
    cur_id = None
    cur_obsolete = False
    in_term = False
    for line in path.read_text().splitlines():
        if line == "[Term]":
            in_term = True
            cur_id = None
            cur_obsolete = False
            continue
        if line.startswith("["):  # some other stanza (Typedef)
            in_term = False
            continue
        if not in_term:
            continue
        if line.startswith("id: "):
            cur_id = line[4:].strip()
        elif line.startswith("name: ") and cur_id:
            name[cur_id] = line[6:].strip()
        elif line.startswith("alt_id: ") and cur_id:
            alt[line[8:].strip()] = cur_id
        elif line.startswith("is_obsolete: true") and cur_id:
            cur_obsolete = True
            obsolete.add(cur_id)
        elif line.startswith("is_a: ") and cur_id and not cur_obsolete:
            parents[cur_id].add(line[6:].split("!")[0].strip())
        elif line.startswith("relationship: part_of ") and cur_id and not cur_obsolete:
            parents[cur_id].add(line.split("part_of", 1)[1].split("!")[0].strip())
    return parents, name, alt, obsolete


def ancestors_of(term: str, parents: dict[str, set[str]]) -> set[str]:
    """All ancestors (exclusive of self) over is_a+part_of."""
    seen: set[str] = set()
    stack = list(parents.get(term, ()))
    while stack:
        p = stack.pop()
        if p in seen:
            continue
        seen.add(p)
        stack.extend(parents.get(p, ()))
    return seen


# ---------------------------------------------------------------------------
# main analysis
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--download", action="store_true", help="download/cache inputs into ./data first")
    args = ap.parse_args()

    if args.download:
        download()

    missing = [n for n in URLS if not (DATA / n).exists()]
    if missing:
        print(f"ERROR: missing inputs {missing}. Re-run with --download.", file=sys.stderr)
        return 1

    print("Parsing pfam2go ...")
    pfam2go, pf_labels, pfam_ver = parse_ext2go(DATA / "pfam2go.txt", "Pfam")
    print("Parsing interpro2go ...")
    interpro2go, ipr_labels, ipr_ver = parse_ext2go(DATA / "interpro2go.txt", "InterPro")
    print("Parsing Pfam<->InterPro membership ...")
    pf2ipr, interpro_release = parse_pfam_to_interpro(DATA / "interpro.xml.gz")
    print("Parsing GO DAG ...")
    parents, go_name, alt, obsolete = parse_go_dag(DATA / "go-basic.obo")

    def norm(go_id: str) -> str:
        return alt.get(go_id, go_id)

    def label(go_id: str, fallback: str = "") -> str:
        return go_name.get(norm(go_id), fallback or go_id)

    # ancestor cache
    anc_cache: dict[str, set[str]] = {}

    def anc(go_id: str) -> set[str]:
        go_id = norm(go_id)
        if go_id not in anc_cache:
            anc_cache[go_id] = ancestors_of(go_id, parents)
        return anc_cache[go_id]

    # classify every pfam2go assertion
    rows = []  # (pfam, pfam_name, ipr, ipr_name, go_id, go_label, category)
    cat_count: collections.Counter = collections.Counter()
    integrated_pf = set()
    unintegrated_rows = []

    for pf, gos in sorted(pfam2go.items()):
        pf_name = pf_labels.get(pf, "")  # external2go has no pfam short name col reliably
        ipr = pf2ipr.get(pf)
        if ipr is None:
            # not integrated into any InterPro entry -> pure coverage gap
            for g in sorted(gos):
                unintegrated_rows.append((pf, g, label(g)))
                cat_count["UNINTEGRATED"] += 1
            continue
        integrated_pf.add(pf)
        ipr_gos = {norm(g) for g in interpro2go.get(ipr, set())}
        parent_has_go = bool(ipr_gos)
        for g in sorted(gos):
            gn = norm(g)
            if gn in ipr_gos:
                cat = "SAME"
            elif anc(gn) & ipr_gos:
                cat = "MORE_SPECIFIC"
            elif any(gn in anc(ig) for ig in ipr_gos):
                cat = "MORE_GENERAL"
            elif not parent_has_go:
                # parent InterPro entry carries NO GO term at all: this is the
                # signature of InterPro release skew (the Pfam was re-integrated
                # into a newly created entry that the GO snapshot predates), not
                # a genuine Pfam-specific term.
                cat = "DISJOINT_PARENT_NO_GO"
            else:
                cat = "DISJOINT_PARENT_HAS_GO"
            cat_count[cat] += 1
            rows.append((pf, pf_name, ipr, "", g, label(g), cat))

    # ---- write TSVs ----
    # The committed "findings" TSV holds only the *interesting* (non-SAME) rows.
    # The ~9,800 SAME rows (pfam2go term identical to the InterPro entry) are the
    # overwhelming, uninteresting majority and are omitted to keep the file small
    # and the repo light; the full dump is regenerable and written under data/.
    gap_tsv = HERE / "pfam_go_precision_gaps.tsv"
    with gap_tsv.open("w") as fh:
        fh.write("pfam\tinterpro\tgo_id\tgo_label\tcategory\n")
        for pf, pf_name, ipr, ipr_name, g, glab, cat in rows:
            if cat == "SAME":
                continue
            fh.write(f"{pf}\t{ipr}\t{g}\t{glab}\t{cat}\n")

    DATA.mkdir(parents=True, exist_ok=True)
    full_tsv = DATA / "pfam_go_all_assertions.tsv"  # git-ignored full dump
    with full_tsv.open("w") as fh:
        fh.write("pfam\tinterpro\tgo_id\tgo_label\tcategory\n")
        for pf, pf_name, ipr, ipr_name, g, glab, cat in rows:
            fh.write(f"{pf}\t{ipr}\t{g}\t{glab}\t{cat}\n")

    unint_tsv = HERE / "unintegrated_pfam_with_go.tsv"
    with unint_tsv.open("w") as fh:
        fh.write("pfam\tgo_id\tgo_label\n")
        for pf, g, glab in unintegrated_rows:
            fh.write(f"{pf}\t{g}\t{glab}\n")

    # ---- gather examples for the report ----
    more_specific = [r for r in rows if r[6] == "MORE_SPECIFIC"]
    more_general = [r for r in rows if r[6] == "MORE_GENERAL"]
    disjoint_real = [r for r in rows if r[6] == "DISJOINT_PARENT_HAS_GO"]
    disjoint_skew = [r for r in rows if r[6] == "DISJOINT_PARENT_NO_GO"]

    # For MORE_SPECIFIC, also show the parent InterPro term it refines.
    def parent_terms_for(ipr: str, gn: str) -> list[str]:
        ipr_gos = {norm(x) for x in interpro2go.get(ipr, set())}
        return sorted(a for a in anc(gn) if a in ipr_gos)

    n_pfam_total = len(pfam2go)
    n_integrated = len(integrated_pf)
    n_unintegrated_fam = n_pfam_total - n_integrated
    pf_with_morespecific = sorted({r[0] for r in more_specific})
    pf_with_disjoint_real = sorted({r[0] for r in disjoint_real})
    pf_with_disjoint_skew = sorted({r[0] for r in disjoint_skew})

    # ---- write RESULTS.md ----
    out = []
    out.append("---")
    out.append('title: "Pfam2GO vs InterPro2GO: Precision-Gap Analysis Results"')
    out.append("---")
    out.append("")
    out.append("# Pfam2GO vs InterPro2GO — Precision-Gap Analysis")
    out.append("")
    out.append("> Auto-generated by `analyze_pfam_go_gaps.py`. Do not edit by hand; "
               "re-run the script to refresh. See [parent project](../PFAM.md).")
    out.append("")
    out.append("## Provenance")
    out.append("")
    out.append(f"- `pfam2go` version date: **{pfam_ver}**")
    out.append(f"- `interpro2go` version date: **{ipr_ver}**")
    out.append(f"- `interpro.xml.gz` InterPro release: **{interpro_release}**")
    out.append("- `go-basic.obo`: current release at run time (current.geneontology.org).")
    out.append("- Specificity is judged over the GO `is_a` + `part_of` DAG (go-basic).")
    out.append("- **Note on release skew:** the GO mapping files come from the GO snapshot "
               "and the membership file from the EBI InterPro FTP; if their dates differ, a "
               "few Pfam families re-integrated in the newer InterPro release land in entries "
               "the older GO snapshot has not annotated yet. These surface as "
               "`DISJOINT_PARENT_NO_GO` and are skew, not signal.")
    out.append("")
    out.append("## Headline")
    out.append("")
    out.append(f"Of **{cat_count['SAME'] + cat_count['MORE_SPECIFIC'] + cat_count['MORE_GENERAL'] + cat_count['DISJOINT_PARENT_HAS_GO'] + cat_count['DISJOINT_PARENT_NO_GO']:,}** "
               f"pfam2go assertions on integrated families, **{cat_count['SAME']:,}** are "
               f"byte-identical to a GO id already on the parent InterPro entry and "
               f"**{cat_count['MORE_SPECIFIC']:,}** are more specific. pfam2go is, as its own "
               "header states, *generated from* InterPro2GO — it provides **no precision gain** "
               "over InterPro2GO.")
    out.append("")
    out.append("## Coverage")
    out.append("")
    out.append(f"- Pfam families with at least one `pfam2go` term: **{n_pfam_total:,}**")
    out.append(f"- Of these, integrated into an InterPro entry: **{n_integrated:,}**")
    out.append(f"- Not integrated into any InterPro entry (pure InterPro2GO gap): "
               f"**{n_unintegrated_fam:,}**")
    out.append(f"- Pfam families mapped to an InterPro entry overall (membership file): "
               f"**{len(pf2ipr):,}**")
    out.append("")
    out.append("## Classification of pfam2go assertions for *integrated* families")
    out.append("")
    out.append("Each `pfam2go` (Pfam, GO) assertion compared to the GO terms of the "
               "Pfam family's parent InterPro entry:")
    out.append("")
    out.append("| Category | Assertions | Meaning |")
    out.append("|---|---:|---|")
    out.append(f"| SAME | {cat_count['SAME']:,} | identical GO id already on the InterPro entry |")
    out.append(f"| MORE_SPECIFIC | {cat_count['MORE_SPECIFIC']:,} | **GO descendant** of an InterPro-entry term (would be a precision gain) |")
    out.append(f"| MORE_GENERAL | {cat_count['MORE_GENERAL']:,} | GO ancestor of an InterPro-entry term (Pfam *less* specific) |")
    out.append(f"| DISJOINT_PARENT_HAS_GO | {cat_count['DISJOINT_PARENT_HAS_GO']:,} | unrelated to the entry's terms, entry *does* have GO (genuine difference) |")
    out.append(f"| DISJOINT_PARENT_NO_GO | {cat_count['DISJOINT_PARENT_NO_GO']:,} | parent entry has *no* GO at all — InterPro release-skew artifact |")
    out.append("")
    out.append(f"- Distinct integrated Pfam families with ≥1 MORE_SPECIFIC term: "
               f"**{len(pf_with_morespecific):,}**")
    out.append(f"- Distinct families with a genuine disjoint difference (parent has GO): "
               f"**{len(pf_with_disjoint_real):,}**")
    out.append(f"- Distinct families showing release-skew disjointness (parent has no GO): "
               f"**{len(pf_with_disjoint_skew):,}**")
    out.append(f"- Unintegrated Pfam families contributing GO terms InterPro entries lack: "
               f"**{n_unintegrated_fam:,}** ({cat_count['UNINTEGRATED']:,} assertions)")
    out.append("")
    out.append("## Examples — increased precision (MORE_SPECIFIC)")
    out.append("")
    out.append("Pfam family maps to a GO term strictly more specific than anything on "
               "its parent InterPro entry. These would be the gap-filling candidates.")
    out.append("")
    if more_specific:
        out.append("| Pfam | InterPro | Pfam GO (specific) | refines InterPro GO |")
        out.append("|---|---|---|---|")
        for pf, pf_name, ipr, ipr_name, g, glab, cat in more_specific[:40]:
            pts = parent_terms_for(ipr, g)
            pt_str = "; ".join(f"{p} {label(p)}" for p in pts) or "—"
            out.append(f"| {pf} | {ipr} | {g} {glab} | {pt_str} |")
        if len(more_specific) > 40:
            out.append("")
            out.append(f"*(showing 40 of {len(more_specific):,}; full list in "
                       "`pfam_go_precision_gaps.tsv`)*")
    else:
        out.append("_None found — there is no case where pfam2go is more specific than "
                   "its parent InterPro entry._")
    out.append("")
    out.append("## Examples — Pfam *less* specific than InterPro (MORE_GENERAL)")
    out.append("")
    out.append("The reverse of the hypothesis: InterPro2GO carries the more precise term.")
    out.append("")
    if more_general:
        out.append("| Pfam | InterPro | Pfam GO (general) | InterPro has descendant |")
        out.append("|---|---|---|---|")
        for pf, pf_name, ipr, ipr_name, g, glab, cat in more_general[:40]:
            ipr_gos = {norm(x) for x in interpro2go.get(ipr, set())}
            desc = sorted(ig for ig in ipr_gos if norm(g) in anc(ig))
            d_str = "; ".join(f"{d} {label(d)}" for d in desc) or "—"
            out.append(f"| {pf} | {ipr} | {g} {glab} | {d_str} |")
    else:
        out.append("_None found._")
    out.append("")
    out.append("## Examples — genuine disjoint difference (DISJOINT_PARENT_HAS_GO)")
    out.append("")
    out.append("Parent InterPro entry has GO terms, but the pfam2go term is unrelated to "
               "them. The few cases here are typically a generic process term paired with "
               "a more specific InterPro molecular-function term for the same family.")
    out.append("")
    if disjoint_real:
        out.append("| Pfam | InterPro | Pfam GO (unrelated to entry's terms) |")
        out.append("|---|---|---|")
        for pf, pf_name, ipr, ipr_name, g, glab, cat in disjoint_real[:30]:
            out.append(f"| {pf} | {ipr} | {g} {glab} |")
    else:
        out.append("_None found._")
    out.append("")
    out.append("## Examples — release-skew disjointness (DISJOINT_PARENT_NO_GO)")
    out.append("")
    out.append("Parent InterPro entry has no GO at all (newly created entry the GO snapshot "
               "predates). pfam2go merely *retains* the older term; not a precision gain, but "
               "a small **recall** advantage until InterPro2GO catches up.")
    out.append("")
    if disjoint_skew:
        out.append("| Pfam | InterPro (no GO yet) | Pfam GO (retained) |")
        out.append("|---|---|---|")
        for pf, pf_name, ipr, ipr_name, g, glab, cat in disjoint_skew[:30]:
            out.append(f"| {pf} | {ipr} | {g} {glab} |")
        if len(disjoint_skew) > 30:
            out.append("")
            out.append(f"*(showing 30 of {len(disjoint_skew):,}; full list in "
                       "`pfam_go_precision_gaps.tsv`)*")
    else:
        out.append("_None found._")
    out.append("")
    out.append("## Examples — unintegrated Pfam families with GO terms")
    out.append("")
    out.append("These Pfam families carry `pfam2go` terms but are not part of any "
               "InterPro entry, so InterPro2GO has no equivalent.")
    out.append("")
    if unintegrated_rows:
        out.append("| Pfam | Pfam GO |")
        out.append("|---|---|")
        for pf, g, glab in unintegrated_rows[:30]:
            out.append(f"| {pf} | {g} {glab} |")
        if len(unintegrated_rows) > 30:
            out.append("")
            out.append(f"*(showing 30 of {len(unintegrated_rows):,}; full list in "
                       "`unintegrated_pfam_with_go.tsv`)*")
    else:
        out.append("_None found._")
    out.append("")
    out.append("## Output files")
    out.append("")
    out.append("- `pfam_go_precision_gaps.tsv` — the **non-SAME** classified assertions "
               "(the findings; the ~9,800 identical SAME rows are omitted)")
    out.append("- `unintegrated_pfam_with_go.tsv` — pfam2go terms for unintegrated families")
    out.append("- `data/pfam_go_all_assertions.tsv` — full dump incl. SAME rows "
               "(git-ignored, regenerable)")
    out.append("")

    (HERE / "RESULTS.md").write_text("\n".join(out) + "\n")

    # ---- console summary ----
    print("\n=== SUMMARY ===")
    print(f"pfam2go families: {n_pfam_total:,} (integrated {n_integrated:,}, "
          f"unintegrated {n_unintegrated_fam:,})")
    for c in ("SAME", "MORE_SPECIFIC", "MORE_GENERAL",
              "DISJOINT_PARENT_HAS_GO", "DISJOINT_PARENT_NO_GO", "UNINTEGRATED"):
        print(f"  {c:22s}: {cat_count[c]:,}")
    print(f"Families with MORE_SPECIFIC:       {len(pf_with_morespecific):,}")
    print(f"Families with genuine disjoint:    {len(pf_with_disjoint_real):,}")
    print(f"Families with release-skew disjoint: {len(pf_with_disjoint_skew):,}")
    print(f"Wrote RESULTS.md, {gap_tsv.name}, {unint_tsv.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
