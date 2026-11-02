"""Two checks over every PAINT IRD row: seeds inside the clade, and fully re-annotated blocks.

1. **Seed in clade.** An IRD stops an ancestral IBD. That IBD was placed on the
   experimental annotations of its seeds (the with/from column). If one of those seeds
   sits inside the IRD clade, the IRD denies the function to a protein whose own
   experiment was used to infer it -- the pattern behind most contested IRDs here
   (SSA1 under the fungal refolding IRD, human GK and mouse Gk under the cytosol IRD).
   MOD seed ids are mapped to UniProt with the UniProt ID-mapping service; the mapping
   is cached in ``.cache/paint/seed_uniprot_map.json``.
2. **Fully re-annotated.** PAINT can annotate the blocked term (or a GO descendant)
   again on a node below the IRD. When every protein in the clade gets the term back as
   a positive IBA, the IRD blocks nothing. For each such row this lists the IBD nodes
   inside the clade that re-add the term.

Inputs:  ird_nodes.tsv, ird_clade_members.tsv.gz (from fetch_paint_ird.py and
         fetch_ird_clades.py), PAINT IBD.gaf and leaf GAF under .cache/paint/,
         and the compact PANTHER trees under .cache/panther_trees/.
Outputs: ird_seed_check.md (committed summary), ird_seed_in_clade.tsv and
         ird_fully_reannotated.tsv (git-ignored detail).

Usage:
    uv run python projects/IRD_EVIDENCE/ird_seed_check.py
"""

from __future__ import annotations

import csv
import gzip
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests
from oaklib import get_adapter

from ai_gene_review.etl.panther_paint import open_text
from ai_gene_review.etl.panther_trees import leaves_below, load_family

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
CACHE = ROOT / ".cache" / "paint"
IBD_GAF = CACHE / "IBD.gaf"
LEAF_GAF = CACHE / "gene_association.paint_uniprot.gaf.gz"
SEED_MAP = CACHE / "seed_uniprot_map.json"
NODES = HERE / "ird_nodes.tsv"
MEMBERS = HERE / "ird_clade_members.tsv.gz"
OUT_MD = HERE / "ird_seed_check.md"
OUT_SEEDS = HERE / "ird_seed_in_clade.tsv"
OUT_FULL = HERE / "ird_fully_reannotated.tsv"
PREDS = ["rdfs:subClassOf", "BFO:0000050"]
# GAF with/from prefix -> (UniProt ID-mapping source database, id transform)
MOD_SOURCES = {
    "MGI": ("MGI", lambda i: i if i.startswith("MGI:") else f"MGI:{i}"),
    "FB": ("FlyBase", str), "SGD": ("SGD", str), "AGI_LocusCode": ("Araport", str),
    "WB": ("WormBase", str), "PomBase": ("PomBase", str), "RGD": ("RGD", str),
    "ZFIN": ("ZFIN", str), "CGD": ("CGD", str), "dictyBase": ("dictyBase", str),
    "Xenbase": ("Xenbase", str), "JaponicusDB": ("JaponicusDB", str),
}


UNMAPPABLE: dict[str, tuple[int, str]] = {}  # prefix -> (seed count, reason), reported in the summary


def split_curie(seed: str) -> tuple[str, str]:
    """``MGI:MGI:88314`` -> (``MGI``, ``MGI:88314``); ``UniProtKB:P1`` -> (``UniProtKB``, ``P1``).

    >>> split_curie("MGI:MGI:88314"), split_curie("UniProtKB:P10591")
    (('MGI', 'MGI:88314'), ('UniProtKB', 'P10591'))
    """
    prefix, _, local = seed.partition(":")
    return prefix, local


def idmap(source: str, ids: list[str]) -> dict[str, set[str]]:
    """Map ids from one database to UniProtKB accessions with the UniProt ID-mapping API."""
    out: dict[str, set[str]] = defaultdict(set)
    for start in range(0, len(ids), 5000):
        chunk = ids[start:start + 5000]
        submitted = requests.post("https://rest.uniprot.org/idmapping/run",
                                  data={"from": source, "to": "UniProtKB", "ids": ",".join(chunk)}, timeout=120).json()
        if "jobId" not in submitted:
            raise ValueError(f"UniProt ID mapping rejected source {source}: {submitted}")
        job = submitted["jobId"]
        for _ in range(120):
            status = requests.get(f"https://rest.uniprot.org/idmapping/status/{job}", timeout=60, allow_redirects=False)
            body = status.json() if status.headers.get("content-type", "").startswith("application/json") else {}
            if status.status_code == 303 or body.get("jobStatus") == "FINISHED" or "results" in body:
                break
            if body.get("jobStatus") in ("ERROR", "FAILURE"):
                raise RuntimeError(f"{source}: id mapping failed: {body}")
            time.sleep(3)
        text = requests.get(f"https://rest.uniprot.org/idmapping/stream/{job}", params={"format": "tsv"}, timeout=300).text
        for line in text.splitlines()[1:]:
            frm, _, to = line.partition("\t")
            if to:
                out[frm].add(to)
    return out


def seed_accessions(seeds: set[str]) -> dict[str, set[str]]:
    """Seed CURIE -> UniProt accessions, from the cache, mapping what is missing."""
    cache: dict[str, list[str]] = json.loads(SEED_MAP.read_text()) if SEED_MAP.exists() else {}
    todo: dict[str, list[str]] = defaultdict(list)
    for seed in seeds:
        prefix, local = split_curie(seed)
        if seed in cache or prefix == "UniProtKB" or prefix not in MOD_SOURCES:
            continue
        todo[prefix].append(local)
    for prefix, locals_ in todo.items():
        source, transform = MOD_SOURCES[prefix]
        try:
            mapped = idmap(source, sorted({transform(x) for x in locals_}))
        except ValueError as e:  # an external service refusing a source database
            UNMAPPABLE[prefix] = (len(locals_), str(e))
            print(f"{prefix}: {e}", file=sys.stderr)
            continue
        for local in locals_:
            cache[f"{prefix}:{local}"] = sorted(mapped.get(transform(local), set()))
        SEED_MAP.write_text(json.dumps(cache, sort_keys=True))
        print(f"mapped {len(locals_)} {prefix} seeds", file=sys.stderr)
    result: dict[str, set[str]] = {}
    for seed in seeds:
        prefix, local = split_curie(seed)
        result[seed] = {local.split("-")[0]} if prefix == "UniProtKB" else set(cache.get(seed, []))
    return result


def read_tsv(path: Path) -> list[dict[str, str]]:
    """Rows of a (possibly gzipped) TSV."""
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def md_table(header: list[str], rows: list[list]) -> list[str]:
    """A markdown table."""
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + [
        "| " + " | ".join(str(c) for c in r) + " |" for r in rows]


def main() -> int:
    """Run both checks and write the summary."""
    ird = read_tsv(NODES)
    clade: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for m in read_tsv(MEMBERS):
        clade[(m["ird_node"], m["go_id"])].append(m)

    want = {(r["ancestral_node"], r["go_id"]) for r in ird}
    ibd_seeds: dict[tuple[str, str], set[str]] = defaultdict(set)
    with open_text(IBD_GAF) as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            if len(c) < 14 or "NOT" in c[3] or c[6] != "IBD":
                continue
            if (c[1], c[4]) in want:
                ibd_seeds[(c[1], c[4])] |= {t for t in c[7].split("|") if t and not t.startswith("PANTHER:")}
    seed_map = seed_accessions(set().union(*ibd_seeds.values()) if ibd_seeds else set())

    # 1. seeds inside the IRD clade
    seed_rows = []
    for r in ird:
        members = {m["uniprot"]: m for m in clade.get((r["ird_node"], r["go_id"]), []) if m["uniprot"]}
        hits = [(s, acc) for s in sorted(ibd_seeds.get((r["ancestral_node"], r["go_id"]), set()))
                for acc in sorted(seed_map.get(s, set())) if acc in members]
        if hits:
            seed_rows.append({
                "family": r["family"], "ird_node": r["ird_node"], "go_id": r["go_id"], "go_label": r["go_label"],
                "ancestral_node": r["ancestral_node"], "clade_size": len(members),
                "seeds_in_clade": "|".join(f"{s}={acc} {members[acc]['symbol']} ({members[acc]['organism']})" for s, acc in hits),
            })
    with OUT_SEEDS.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(seed_rows[0]) if seed_rows else ["family"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(seed_rows)

    # 2. fully re-annotated IRD rows
    go = get_adapter("sqlite:obo:go")
    desc_cache: dict[str, set[str]] = {}

    def desc(t: str) -> set[str]:
        if t not in desc_cache:
            desc_cache[t] = set(go.descendants(t, predicates=PREDS, reflexive=True))
        return desc_cache[t]

    accs = {m["uniprot"] for ms in clade.values() for m in ms if m["uniprot"]}
    leaf_pos: dict[str, set[str]] = defaultdict(set)
    leaf_src: dict[str, list[tuple[str, str]]] = defaultdict(list)  # acc -> [(go_id, source PTN)]
    with open_text(LEAF_GAF) as fh:
        for line in fh:
            c = line.split("\t")
            if len(c) > 8 and c[1] in accs and "NOT" not in c[3]:
                leaf_pos[c[1]].add(c[4])
                leaf_src[c[1]] += [(c[4], t.split(":")[-1]) for t in c[7].split("|") if "PTN" in t]
    full_rows = []
    trees: dict[str, dict | None] = {}
    for r in ird:
        all_members = clade.get((r["ird_node"], r["go_id"]), [])
        members = [m for m in all_members if m["uniprot"]]
        if not members or not all(leaf_pos.get(m["uniprot"], set()) & desc(r["go_id"]) for m in members):
            continue
        tree = trees.setdefault(r["family"], load_family(r["family"], ROOT / ".cache" / "panther_trees"))
        inside = set(leaves_below(tree, r["ird_node"])) if tree else set()
        sources = {(src, gid) for m in members for gid, src in leaf_src.get(m["uniprot"], []) if gid in desc(r["go_id"])}

        def where(src: str) -> str:
            if src == r["ird_node"]:
                return "same node"
            if not tree:
                return "no tree"
            below = set(leaves_below(tree, src)) if tree else set()
            return "below" if below and below <= inside else "above"

        readders = sorted(f"{src} {gid} ({where(src)}{', same term' if gid == r['go_id'] else ''})" for src, gid in sources)
        full_rows.append({
            "family": r["family"], "ird_node": r["ird_node"], "go_id": r["go_id"], "go_label": r["go_label"],
            "ird_date": r["date"], "clade_size": len(members), "clade_leaves": len(all_members),
            "reannotated_by": "|".join(readders),
            "kind": next((k for k in ("below", "same node", "no tree") if any(where(s) == k for s, _ in sources)), "above"),
        })
    with OUT_FULL.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(full_rows[0]) if full_rows else ["family"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(full_rows)

    n_seeds = sum(len(v) for v in ibd_seeds.values())
    mapped = sum(1 for s in set().union(*ibd_seeds.values()) if seed_map.get(s)) if ibd_seeds else 0
    by_family = Counter(r["family"] for r in seed_rows)
    md = [
        "# IRD-wide checks: seeds inside the clade, and fully re-annotated blocks",
        "",
        "Generated by `ird_seed_check.py` from PAINT IBD.gaf, the PAINT leaf GAF and the PANTHER",
        "trees. Detail rows are in the git-ignored `ird_seed_in_clade.tsv` and",
        "`ird_fully_reannotated.tsv`.",
        "",
        "## 1. The IRD clade contains a seed of the IBD it blocks",
        "",
        f"- IRD rows: {len(ird)}. Seed slots on their ancestral IBDs: {n_seeds} "
        f"({len(set().union(*ibd_seeds.values())) if ibd_seeds else 0} distinct seeds, {mapped} mapped to UniProt).",
        f"- Clade members checked: {sum(1 for ms in clade.values() for m in ms if m['uniprot'])} of "
        f"{sum(len(ms) for ms in clade.values())} (only leaves with a UniProt accession can match a seed).",
        *[f"- Not mapped: {n} {prefix} seeds ({reason[:120]})." for prefix, (n, reason) in UNMAPPABLE.items()],
        f"- **{len(seed_rows)} IRD rows ({100 * len(seed_rows) / len(ird):.1f}%) have at least one seed of the "
        f"blocked IBD inside their own clade**, in {len(by_family)} families.",
        "",
        "Such an IRD denies the function to a protein whose own experiment was used to infer",
        "it. That is not always an error (the seed's annotation may be weak, or PAINT may judge",
        "it a lineage-specific gain), but each one should be checked first.",
        "",
        "Families with the most such rows:",
        "",
        *md_table(["Family", "IRD rows with a seed in the clade"], [[f, n] for f, n in by_family.most_common(15)]),
        "",
        f"## 2. Fully re-annotated IRD rows ({len(full_rows)})",
        "",
        "Every protein in the clade still gets the blocked term, or a term below it in GO (by",
        "is_a or part_of, the relations `analyze_ird.py` uses), as a positive IBA. The IRD",
        "therefore removes nothing a user can see. The source of each IBA is the PTN node in",
        "the leaf GAF's with/from (every PTN listed there). The kinds are:",
        "",
        f"- **Below** ({sum(r['kind'] == 'below' for r in full_rows)}): PAINT annotates the term again on a",
        "  node inside the IRD clade, overriding the IRD.",
        f"- **Same node** ({sum(r['kind'] == 'same node' for r in full_rows)}): the IRD node itself carries an",
        "  IBD for a more specific term, for example a mitochondrion IBD beside a NOT cytoplasm.",
        f"- **Above** ({sum(r['kind'] == 'above' for r in full_rows)}): an ancestral IBD carries a more specific",
        "  term that the IRD does not block.",
        *([f"- **No tree** ({sum(r['kind'] == 'no tree' for r in full_rows)}): the family's PANTHER tree is not",
           "  cached, so below and above cannot be told apart."] if any(r["kind"] == "no tree" for r in full_rows) else []),
        "",
        "Only clade members with a UniProt accession can be checked; the Clade column gives",
        "checked/all leaves. A clade where few leaves are checked is weaker evidence.",
        "",
        "In each case the IRD contradicts annotations PAINT itself propagates: a gene cannot lack",
        "a process or location while having one of its subtypes or parts. Either the IRD should",
        "also block the more specific term, or it should be retracted. Some pairs cross GO",
        "aspects through part_of (a transporter activity that is part of transmembrane",
        "transport); those are listed but are weaker evidence of inconsistency.",
        "",
        *md_table(["Family", "IRD node", "Blocked term", "IRD date", "Clade", "Kind", "IBA sources (node, term, where)"],
                  [[r["family"], r["ird_node"], f"{r['go_id']} {r['go_label']}", r["ird_date"], f"{r['clade_size']}/{r['clade_leaves']}",
                    r["kind"], r["reannotated_by"].replace("|", "; ")] for r in full_rows]),
        "",
    ]
    OUT_MD.write_text("\n".join(md))
    print(f"{len(seed_rows)} IRD rows with a seed in the clade; {len(full_rows)} fully re-annotated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
