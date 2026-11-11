#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Find Pfam families whose GO mapping would be HIGH VALUE and UNIQUE.

``headroom_analysis.py`` showed that most Pfam families get no GO term through
InterPro2GO. That count says nothing about whether a new Pfam -> GO mapping would
be worth writing. Two things decide that, and this script measures both on the
reviewed (Swiss-Prot) members of each family:

HIGH VALUE
    The term is a specific, non-binding molecular function (a catalytic,
    transporter, receptor ... activity) that the family's members share. A term
    only in the GO:0005488 binding branch is skipped: it says little about what
    the protein does.

UNIQUE
    No InterPro entry that the same proteins match already supplies the term.
    The check is per protein and uses every InterPro entry the protein matches,
    not only the entry the Pfam family is integrated into. A function that
    arrives through a separate, unlinked InterPro entry (a PANTHER, NCBIfam or
    CDD based family entry, say) is therefore counted as already supplied.

The result is then tested where the gain would land: for each shortlisted
(family, term) pair the script asks UniProt how many unreviewed proteins match
the family and how many of those already carry the term or a descendant from any
pipeline (InterPro2GO, UniRule, ARBA, EC2GO, RHEA2GO).

Method, for each Pfam family with at least ``--min-members`` reviewed members:

1. Function set of a member = its GO molecular-function terms plus the GO terms
   that ec2go gives for its complete EC numbers, closed over is_a/part_of.
2. Candidate terms = the most specific terms carried by at least ``--purity`` of
   the members (the frontier: no descendant also reaches the threshold),
   excluding binding-only terms and terms carried by more than ``--max-freq`` of
   Swiss-Prot.
3. InterPro-supplied = the member matches an InterPro entry whose interpro2go
   terms include the candidate or a descendant. ``general_only`` means only a
   proper ancestor is supplied.
4. A pair is shortlisted when at most ``--max-supplied`` of members are supplied.
5. Route: whether the mapping needs Pfam at all. ``UNINTEGRATED`` families are in
   no InterPro entry, so only a Pfam-level mapping or rule can reach them.
   ``SOLE_SIGNATURE`` families are the only signature of their entry, so adding
   the term to interpro2go on that entry is equivalent. ``SHARED_ENTRY`` families
   share the entry with other signatures; ``entry_purity`` then says whether the
   term still holds at entry level.

The script also takes a census of the project's "negative" records (InterPro2GO
removals and narrowings in ``projects/INTERPRO/interpro2go.sssom.yaml`` and the
curated rules in ``rules/curated``) and reports whether any of them uses a Pfam
condition, and which Pfam families split the reviewed members of each entry.

Inputs (``./data``, git-ignored; see ``--download``):
  interpro.xml.gz, interpro2go.txt, go-basic.obo, ec2go.txt,
  sprot_pfam_ipr_go.json.gz, sprot_organism.tsv.gz (UniProt REST streams of
  reviewed entries)

Outputs (``./``):
  HIGH_VALUE_UNIQUE.md                 summary page (regenerated)
  high_value_unique_candidates.yaml    the shortlist, ranked
  data/high_value_unique_all.yaml      every candidate pair, before the
                                       uniqueness filter (git-ignored)
  data/uniprot_counts.json             cache of UniProt count queries

No mapping is asserted. Nothing is hardcoded: a missing input is an error, and a
UniProt count that cannot be fetched is reported as missing.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import re
import subprocess
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

HERE = Path(__file__).parent
DATA = HERE / "data"
REPO = HERE.parent.parent

MF_ROOT = "GO:0003674"
BINDING = "GO:0005488"
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
COMPLETE_EC = re.compile(r"^\d+\.\d+\.\d+\.\d+$")
EXT2GO_RE = re.compile(r"^(\S+?):(\S+)\s+.*?>\s+GO:(.+?)\s+;\s+(GO:\d+)\s*$")

URLS = {
    "interpro2go.txt": "https://current.geneontology.org/ontology/external2go/interpro2go",
    "ec2go.txt": "https://current.geneontology.org/ontology/external2go/ec2go",
    "go-basic.obo": "https://current.geneontology.org/ontology/go-basic.obo",
    "interpro.xml.gz": "https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro.xml.gz",
    "sprot_pfam_ipr_go.json.gz": (
        "https://rest.uniprot.org/uniprotkb/stream?query=reviewed:true"
        "&fields=accession,ec,xref_pfam,xref_interpro,go_f&format=json&compressed=true"
    ),
    "sprot_organism.tsv.gz": (
        "https://rest.uniprot.org/uniprotkb/stream?query=reviewed:true"
        "&fields=accession,organism_id&format=tsv&compressed=true"
    ),
}
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"


# ---------------------------------------------------------------------------
# download (curl: current.geneontology.org rejects Python's default client)
# ---------------------------------------------------------------------------
def download() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    for name, url in URLS.items():
        dest = DATA / name
        if dest.exists() and dest.stat().st_size > 0:
            print(f"[skip] {name} ({dest.stat().st_size:,} bytes)")
            continue
        print(f"[get ] {name} <- {url}")
        subprocess.run(["curl", "-sS", "--fail", "--retry", "3", "-o", str(dest), url], check=True)


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------
def parse_ext2go(path: Path, prefix: str) -> tuple[dict[str, set[str]], str]:
    mapping: dict[str, set[str]] = collections.defaultdict(set)
    version = "unknown"
    for line in path.read_text().splitlines():
        if line.startswith("!"):
            low = line.lower()
            if "version date" in low or "generated on" in low:
                version = line.lstrip("! ").strip()
            continue
        m = EXT2GO_RE.match(line)
        if m and m.group(1).lower() == prefix.lower():
            mapping[m.group(2)].add(m.group(4))
    return mapping, version


def parse_go(path: Path):
    """go-basic.obo -> (parents over is_a+part_of, name, alt_id map, obsolete, namespace)."""
    parents: dict[str, set[str]] = collections.defaultdict(set)
    name: dict[str, str] = {}
    alt: dict[str, str] = {}
    obsolete: set[str] = set()
    namespace: dict[str, str] = {}
    cur = None
    cur_obs = False
    in_term = False
    version = "unknown"
    with path.open() as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("data-version:"):
                version = line.split(":", 1)[1].strip()
            if line == "[Term]":
                in_term, cur, cur_obs = True, None, False
                continue
            if line.startswith("["):
                in_term = False
                continue
            if not in_term:
                continue
            if line.startswith("id: "):
                cur = line[4:].strip()
            elif cur is None:
                continue
            elif line.startswith("name: "):
                name[cur] = line[6:].strip()
            elif line.startswith("namespace: "):
                namespace[cur] = line[11:].strip()
            elif line.startswith("alt_id: "):
                alt[line[8:].strip()] = cur
            elif line.startswith("is_obsolete: true"):
                cur_obs = True
                obsolete.add(cur)
                parents.pop(cur, None)
            elif line.startswith("is_a: ") and not cur_obs:
                parents[cur].add(line[6:].split("!")[0].strip())
            elif line.startswith("relationship: part_of ") and not cur_obs:
                parents[cur].add(line.split("part_of", 1)[1].split("!")[0].strip())
    return parents, name, alt, obsolete, namespace, version


def parse_interpro(path: Path):
    """interpro.xml.gz -> (pfam->entry, entry type, entry name, entry->members by db, release).

    Only signatures inside ``<member_list>`` count as members. Pfam ids in the
    ``contains``/``found_in`` sections of other entries are architecture links.
    """
    pf2ipr: dict[str, str] = {}
    ipr_type: dict[str, str] = {}
    ipr_name: dict[str, str] = {}
    members: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    release = "unknown"
    with gzip.open(path, "rb") as fh:
        current = None
        in_members = False
        for event, elem in ET.iterparse(fh, events=("start", "end")):
            tag = elem.tag
            if tag == "dbinfo" and event == "start" and elem.get("dbname") == "INTERPRO":
                release = f"{elem.get('version')} ({elem.get('file_date')})"
            elif tag == "interpro":
                if event == "start":
                    current = elem.get("id")
                    ipr_type[current] = elem.get("type")
                else:
                    elem.clear()
                    current = None
            elif tag == "name" and event == "end" and current and current not in ipr_name:
                ipr_name[current] = (elem.text or "").strip()
            elif tag == "member_list":
                in_members = event == "start"
            elif tag == "db_xref" and event == "start" and in_members and current:
                members[current].append((elem.get("db"), elem.get("dbkey")))
                if elem.get("db") == "PFAM":
                    pf2ipr[elem.get("dbkey")] = current
    return pf2ipr, ipr_type, ipr_name, members, release


def iter_uniprot_results(path: Path):
    """Yield entries from a gzipped UniProt ``{"results":[...]}`` stream without loading it whole."""
    decoder = json.JSONDecoder()
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        buf = fh.read(1 << 20)
        start = buf.find("[", buf.find('"results"'))
        if start < 0:
            raise ValueError(f"{path}: not a UniProt results stream")
        pos = start + 1
        while True:
            while pos < len(buf) and buf[pos] in " \n\r\t,":
                pos += 1
            if pos < len(buf) and buf[pos] == "]":
                return
            try:
                if pos >= len(buf):
                    raise json.JSONDecodeError("need more", buf, pos)
                obj, end = decoder.raw_decode(buf, pos)
            except json.JSONDecodeError:
                chunk = fh.read(1 << 22)
                if not chunk:
                    raise ValueError(f"{path}: truncated stream (re-download it)") from None
                buf = buf[pos:] + chunk
                pos = 0
                continue
            yield obj
            pos = end


def ec_numbers(node) -> set[str]:
    """All complete EC numbers anywhere in a proteinDescription block."""
    out: set[str] = set()
    stack = [node]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            for key, val in cur.items():
                if key == "ecNumbers":
                    out.update(e["value"] for e in val if COMPLETE_EC.match(e.get("value", "")))
                else:
                    stack.append(val)
        elif isinstance(cur, list):
            stack.extend(cur)
    return out


# ---------------------------------------------------------------------------
# UniProt counts (cached)
# ---------------------------------------------------------------------------
class UniProtCounter:
    def __init__(self, cache_path: Path, offline: bool):
        self.cache_path = cache_path
        self.offline = offline
        self.cache: dict[str, int] = {}
        self.release = None
        if cache_path.exists():
            blob = json.loads(cache_path.read_text())
            self.cache = blob.get("counts", {})
            self.release = blob.get("release")

    def _fetch(self, query: str) -> int | None:
        url = f"{UNIPROT_SEARCH}?{urllib.parse.urlencode({'query': query, 'size': 0})}"
        for attempt in range(4):
            proc = subprocess.run(
                ["curl", "-sS", "--max-time", "60", "-D", "-", "-o", "/dev/null", url],
                capture_output=True, text=True,
            )
            total = release = None
            for line in proc.stdout.splitlines():
                low = line.lower()
                if low.startswith("x-total-results:"):
                    total = int(line.split(":", 1)[1].strip())
                elif low.startswith("x-uniprot-release:"):
                    release = line.split(":", 1)[1].strip()
            if total is not None:
                self.release = release or self.release
                return total
            time.sleep(2 ** attempt)
        return None

    def count_many(self, queries: list[str]) -> dict[str, int | None]:
        todo = [q for q in dict.fromkeys(queries) if q not in self.cache]
        if todo and not self.offline:
            print(f"UniProt: {len(todo):,} count queries ({len(queries) - len(todo):,} cached)")
            with ThreadPoolExecutor(max_workers=4) as pool:
                for i, (q, n) in enumerate(zip(todo, pool.map(self._fetch, todo)), 1):
                    if n is not None:
                        self.cache[q] = n
                    if i % 200 == 0:
                        print(f"  {i:,}/{len(todo):,}")
                        self.save()
            self.save()
        return {q: self.cache.get(q) for q in queries}

    def save(self) -> None:
        self.cache_path.write_text(json.dumps({"release": self.release, "counts": self.cache}, indent=0))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--download", action="store_true", help="fetch missing inputs into ./data")
    ap.add_argument("--offline", action="store_true", help="do not query UniProt; use cached counts only")
    ap.add_argument("--min-members", type=int, default=5, help="minimum reviewed members per family")
    ap.add_argument("--purity", type=float, default=0.9, help="minimum share of members carrying the term")
    ap.add_argument("--max-freq", type=float, default=0.002,
                    help="maximum share of Swiss-Prot carrying the term (specificity)")
    ap.add_argument("--max-supplied", type=float, default=0.1,
                    help="maximum share of members already supplied by InterPro2GO")
    ap.add_argument("--max-covered", type=float, default=0.5,
                    help="open candidate: at most this share of unreviewed members already carry the term")
    ap.add_argument("--illustrate", action="append", default=["PF00017=GO:0001784"],
                    help="PFxxxxx=GO:nnnnnnn pair to trace regardless of filters (repeatable)")
    args = ap.parse_args()

    if args.download:
        download()
    missing = [n for n in URLS if not (DATA / n).exists()]
    if missing:
        print(f"ERROR: missing inputs {missing}. Re-run with --download.", file=sys.stderr)
        return 2

    parents, go_name, alt, obsolete, namespace, go_version = parse_go(DATA / "go-basic.obo")
    interpro2go_raw, i2g_version = parse_ext2go(DATA / "interpro2go.txt", "InterPro")
    ec2go_raw, ec2go_version = parse_ext2go(DATA / "ec2go.txt", "EC")
    pf2ipr, ipr_type, ipr_name, ipr_sigs, interpro_release = parse_interpro(DATA / "interpro.xml.gz")

    def norm(go_id: str) -> str | None:
        go_id = alt.get(go_id, go_id)
        return None if go_id in obsolete or go_id not in go_name else go_id

    def is_mf(go_id: str) -> bool:
        return namespace.get(go_id) == "molecular_function"

    closure_cache: dict[str, frozenset[str]] = {}

    def closure(go_id: str) -> frozenset[str]:
        """The term and all its ancestors."""
        hit = closure_cache.get(go_id)
        if hit is None:
            seen = {go_id}
            stack = [go_id]
            while stack:
                for p in parents.get(stack.pop(), ()):
                    if p not in seen:
                        seen.add(p)
                        stack.append(p)
            hit = closure_cache[go_id] = frozenset(seen)
        return hit

    def close(terms) -> set[str]:
        out: set[str] = set()
        for t in terms:
            out |= closure(t)
        return out

    depth_cache: dict[str, int] = {MF_ROOT: 0}

    def depth(go_id: str) -> int:
        """Longest is_a/part_of path to the root."""
        if go_id not in depth_cache:
            depth_cache[go_id] = 1 + max((depth(p) for p in parents.get(go_id, ())), default=-1)
        return depth_cache[go_id]

    top_branches = {t for t, ps in parents.items() if MF_ROOT in ps and is_mf(t)}

    def branches(go_id: str) -> list[str]:
        return sorted(go_name[b] for b in closure(go_id) & top_branches)

    def binding_only(go_id: str) -> bool:
        return (closure(go_id) & top_branches) <= {BINDING}

    functional_tops = top_branches - {BINDING}

    def other_function(acc: str, term: str) -> str | None:
        """Most specific non-binding function of a member that is neither the term nor an ancestor of it."""
        rest = [t for t in prot_truth[acc] - closure(term)
                if t != MF_ROOT and closure(t) & functional_tops]
        return max(rest, key=depth) if rest else None

    ipr2mf = {
        ipr: {g for g in (norm(t) for t in terms) if g and is_mf(g)}
        for ipr, terms in interpro2go_raw.items()
    }
    ipr2mf_closed = {ipr: close(terms) for ipr, terms in ipr2mf.items() if terms}
    ec2mf = {ec: {g for g in (norm(t) for t in terms) if g and is_mf(g)} for ec, terms in ec2go_raw.items()}

    # ---- read Swiss-Prot ---------------------------------------------------
    pfam_name: dict[str, str] = {}
    prot_pfams: dict[str, tuple[str, ...]] = {}
    prot_iprs: dict[str, tuple[str, ...]] = {}
    prot_truth: dict[str, frozenset[str]] = {}
    prot_exp: dict[str, frozenset[str]] = {}
    for entry in iter_uniprot_results(DATA / "sprot_pfam_ipr_go.json.gz"):
        acc = entry["primaryAccession"]
        pfams, iprs, truth, exp = [], [], set(), set()
        for xref in entry.get("uniProtKBCrossReferences", ()):
            db = xref["database"]
            props = {p["key"]: p["value"] for p in xref.get("properties", ())}
            if db == "Pfam":
                pfams.append(xref["id"])
                pfam_name.setdefault(xref["id"], props.get("EntryName", ""))
            elif db == "InterPro":
                iprs.append(xref["id"])
                ipr_name.setdefault(xref["id"], props.get("EntryName", ""))
            elif db == "GO" and props.get("GoTerm", "").startswith("F:"):
                go_id = norm(xref["id"])
                if go_id:
                    truth.add(go_id)
                    if props.get("GoEvidenceType", "").split(":")[0] in EXPERIMENTAL:
                        exp.add(go_id)
        for ec in ec_numbers(entry.get("proteinDescription", {})):
            truth |= ec2mf.get(ec, set())
        prot_pfams[acc] = tuple(pfams)
        prot_iprs[acc] = tuple(iprs)
        prot_truth[acc] = frozenset(close(truth))
        prot_exp[acc] = frozenset(close(exp))
    n_sprot = len(prot_truth)
    if n_sprot < 500_000:
        print(f"ERROR: only {n_sprot:,} reviewed entries read; the download is incomplete.", file=sys.stderr)
        return 2
    print(f"Swiss-Prot entries: {n_sprot:,}")

    prot_species: dict[str, str] = {}
    with gzip.open(DATA / "sprot_organism.tsv.gz", "rt") as fh:
        next(fh)
        for line in fh:
            acc, _, taxon = line.rstrip("\n").partition("\t")
            prot_species[acc] = taxon

    term_count: collections.Counter[str] = collections.Counter()
    for truth in prot_truth.values():
        term_count.update(truth)

    prot_supplied: dict[str, set[str]] = {}

    def supplied(acc: str) -> set[str]:
        """Closed set of MF terms that interpro2go gives this protein through any matched entry."""
        hit = prot_supplied.get(acc)
        if hit is None:
            hit = set()
            for ipr in prot_iprs[acc]:
                hit |= ipr2mf_closed.get(ipr, set())
            prot_supplied[acc] = hit
        return hit

    pfam_members: dict[str, list[str]] = collections.defaultdict(list)
    ipr_members: dict[str, list[str]] = collections.defaultdict(list)
    for acc, pfams in prot_pfams.items():
        for pf in pfams:
            pfam_members[pf].append(acc)
        for ipr in prot_iprs[acc]:
            ipr_members[ipr].append(acc)

    # ---- candidates --------------------------------------------------------
    def describe(pf: str, term: str, members: list[str]) -> dict:
        n = len(members)
        support = sum(1 for a in members if term in prot_truth[a])
        n_supplied = n_general = 0
        suppliers: collections.Counter[str] = collections.Counter()
        general_terms: collections.Counter[str] = collections.Counter()
        ancestors = closure(term) - {term, MF_ROOT}
        for acc in members:
            sup = supplied(acc)
            if term in sup:
                n_supplied += 1
                for ipr in prot_iprs[acc]:
                    if term in ipr2mf_closed.get(ipr, ()):
                        suppliers[ipr] += 1
            else:
                shared = sup & ancestors
                if shared:
                    n_general += 1
                    general_terms[max(shared, key=depth)] += 1
        counter_examples = []
        for acc in members:
            if term not in prot_truth[acc]:
                other = other_function(acc, term)
                if other:
                    counter_examples.append({"accession": acc, "function": f"{other} {go_name[other]}"})
        partner_counts: collections.Counter[str] = collections.Counter()
        for acc in members:
            partner_counts.update(set(prot_pfams[acc]) - {pf})
        partners = [
            {"pfam": p, "name": pfam_name.get(p, ""), "reviewed_members": len(pfam_members[p])}
            for p, c in partner_counts.most_common(6) if c >= 0.9 * n
        ]
        own = pf2ipr.get(pf)
        if own is None:
            route = "UNINTEGRATED"
        elif len(ipr_sigs[own]) == 1:
            route = "SOLE_SIGNATURE"
        else:
            route = "SHARED_ENTRY"
        row = {
            "pfam": pf,
            "pfam_name": pfam_name.get(pf, ""),
            "go_id": term,
            "go_label": go_name[term],
            "branches": branches(term),
            "go_depth": depth(term),
            "swissprot_with_term": term_count[term],
            "reviewed_members": n,
            "members_with_term": support,
            "purity": round(support / n, 3),
            "species_with_term": len({prot_species.get(a, a) for a in members if term in prot_truth[a]}),
            "members_with_experimental_evidence": sum(1 for a in members if term in prot_exp[a]),
            "members_with_other_function": len(counter_examples),
            "share_of_term_in_family": round(support / term_count[term], 3),
            "interpro_supplied": round(n_supplied / n, 3),
            "interpro_general_only": round(n_general / n, 3),
            "route": route,
        }
        if counter_examples:
            row["counter_examples"] = counter_examples[:5]
        if partners:
            row["always_with"] = partners
        if general_terms:
            g, _ = general_terms.most_common(1)[0]
            row["most_common_general_term"] = f"{g} {go_name[g]}"
        if suppliers:
            row["supplying_entries"] = [
                {"entry": ipr, "name": ipr_name.get(ipr, ""), "members": c,
                 "is_own_entry": ipr == own}
                for ipr, c in suppliers.most_common(3)
            ]
        if own:
            entry_accs = ipr_members.get(own, [])
            row["own_entry"] = own
            row["own_entry_name"] = ipr_name.get(own, "")
            row["own_entry_type"] = ipr_type.get(own)
            row["own_entry_signatures"] = len(ipr_sigs[own])
            row["own_entry_mf_terms"] = sorted(f"{g} {go_name[g]}" for g in ipr2mf.get(own, ()))
            if entry_accs:
                row["own_entry_reviewed_members"] = len(entry_accs)
                row["own_entry_purity"] = round(
                    sum(1 for a in entry_accs if term in prot_truth[a]) / len(entry_accs), 3)
        return row

    all_rows: list[dict] = []
    n_families = 0
    for pf, members in pfam_members.items():
        if len(members) < args.min_members:
            continue
        n_families += 1
        counts: collections.Counter[str] = collections.Counter()
        for acc in members:
            counts.update(prot_truth[acc])
        need = args.purity * len(members)
        passing = {
            t for t, c in counts.items()
            if c >= need and t != MF_ROOT and not binding_only(t)
        }
        covered_by_descendant: set[str] = set()
        for t in passing:
            covered_by_descendant |= closure(t) - {t}
        for t in passing - covered_by_descendant:
            if term_count[t] / n_sprot <= args.max_freq:
                all_rows.append(describe(pf, t, members))

    shortlist = [r for r in all_rows if r["interpro_supplied"] <= args.max_supplied]

    # ---- UniProt: where would the gain land? -------------------------------
    counter = UniProtCounter(DATA / "uniprot_counts.json", args.offline)

    def queries(row: dict) -> tuple[str, str]:
        base = f"(reviewed:false) AND (xref:pfam-{row['pfam']})"
        return base, f"{base} AND (go:{row['go_id'][3:]})"

    wanted = [q for r in shortlist for q in queries(r)]
    counts = counter.count_many(wanted)
    for r in shortlist:
        q_all, q_term = queries(r)
        n_all, n_term = counts.get(q_all), counts.get(q_term)
        r["unreviewed_members"] = n_all
        r["unreviewed_with_term"] = n_term
        if n_all is not None and n_term is not None:
            r["unreviewed_lacking_term"] = n_all - n_term
            r["unreviewed_already_covered"] = round(n_term / n_all, 3) if n_all else None
    shortlist.sort(key=lambda r: (-(r.get("unreviewed_lacking_term") or -1), r["pfam"]))
    # Families that hit the same proteins (several domains of one enzyme) are one candidate, not many.
    by_term: dict[str, list[dict]] = collections.defaultdict(list)
    for r in shortlist:
        by_term[r["go_id"]].append(r)
    for rows in by_term.values():
        reps: list[tuple[dict, set[str]]] = []
        for r in sorted(rows, key=lambda r: (-r["reviewed_members"], -r["purity"], r["pfam"])):
            accs = set(pfam_members[r["pfam"]])
            for rep_row, rep_accs in reps:
                if len(accs & rep_accs) / len(accs | rep_accs) >= 0.8:
                    r["representative"] = False
                    r["same_proteins_as"] = rep_row["pfam"]
                    rep_row.setdefault("same_protein_families", []).append(r["pfam"])
                    break
            else:
                r["representative"] = True
                reps.append((r, accs))
    for r in shortlist:
        covered = r.get("unreviewed_already_covered")
        r["open"] = covered is not None and covered <= args.max_covered
        r["headline"] = bool(
            r["open"] and r["representative"] and r["members_with_experimental_evidence"] >= 1)

    # ---- illustrations -----------------------------------------------------
    illustrations = []
    specs = [(s, "requested") for s in args.illustrate]
    for path in sorted((REPO / "interpro" / "pfam").glob("PF*/PF*-review.yaml")):
        review = yaml.safe_load(path.read_text())
        for ann in review.get("proposed_annotations") or ():
            if ann.get("aspect") == "molecular_function":
                specs.append((f"{review['pfam_id']}={ann['term']['id']}",
                              f"curated entry, {ann.get('status', 'no status')}"))
    for spec, origin in dict(specs).items():
        pf, _, term = spec.partition("=")
        term = norm(term) if term else None
        if pf not in pfam_members or not term:
            print(f"WARNING: cannot illustrate {spec}", file=sys.stderr)
            continue
        row = describe(pf, term, pfam_members[pf])
        q_all, q_term = queries(row)
        got = counter.count_many([q_all, q_term])
        row["unreviewed_members"], row["unreviewed_with_term"] = got[q_all], got[q_term]
        row["binding_only"] = binding_only(term)
        row["origin"] = origin
        illustrations.append(row)

    # ---- census of negative records ---------------------------------------
    census = negative_census(pf2ipr, ipr_sigs, ipr_name, ipr_type, ipr_members, prot_pfams, pfam_name)

    # ---- write -------------------------------------------------------------
    provenance = {
        "interpro_release": interpro_release,
        "interpro2go": i2g_version,
        "ec2go": ec2go_version,
        "go": go_version,
        "uniprot_release": counter.release,
        "swissprot_entries": n_sprot,
        "parameters": {
            "min_members": args.min_members, "purity": args.purity,
            "max_freq": args.max_freq, "max_supplied": args.max_supplied,
            "max_covered": args.max_covered,
        },
    }
    (DATA / "high_value_unique_all.yaml").write_text(
        yaml.safe_dump({"provenance": provenance, "candidates": all_rows}, sort_keys=False, width=120))
    (DATA / "high_value_unique_shortlist.yaml").write_text(
        yaml.safe_dump({"provenance": provenance, "candidates": shortlist}, sort_keys=False, width=120))
    (HERE / "high_value_unique_candidates.yaml").write_text(
        "# Generated by high_value_unique.py. Do not edit by hand; re-run the script.\n"
        "# Candidates for curation, not asserted mappings. See HIGH_VALUE_UNIQUE.md.\n"
        + yaml.safe_dump({"provenance": provenance, "candidates": [r for r in shortlist if r["open"]]},
                         sort_keys=False, width=120))
    write_report(provenance, n_families, all_rows, shortlist, illustrations, census, args)
    print(f"families tested: {n_families:,}; candidate pairs: {len(all_rows):,}; "
          f"unique (shortlist): {len(shortlist):,}")
    return 0


def negative_census(pf2ipr, ipr_sigs, ipr_name, ipr_type, ipr_members, prot_pfams, pfam_name) -> dict:
    """Which condition types the project's restricting records use, and whether Pfam could split them."""
    out: dict = {"curated_rules": [], "interpro2go_rows": [], "condition_types": collections.Counter()}
    for path in sorted((REPO / "rules" / "curated").glob("CR-*.yaml")):
        rule = yaml.safe_load(path.read_text())
        types: collections.Counter[str] = collections.Counter()
        negated = 0
        for cs in rule.get("condition_sets", ()):
            for cond in cs.get("conditions", ()):
                types[cond["condition_type"]] += 1
                negated += bool(cond.get("negated"))
        out["condition_types"].update(types)
        out["curated_rules"].append({
            "id": rule["id"], "types": dict(types), "negated_conditions": negated,
            "replaces": [r["source_id"] for r in rule.get("replaces", ())],
        })
    sssom = REPO / "projects" / "INTERPRO" / "interpro2go.sssom.yaml"
    if sssom.exists():
        verdicts: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
        for m in yaml.safe_load(sssom.read_text()).get("mappings", ()):
            if m.get("predicate_modifier") == "Not":
                verdict = "REMOVE"
            elif m["predicate_id"] == "skos:broadMatch":
                verdict = "NARROW"
            else:
                verdict = "ENDORSE"
            verdicts[m["subject_id"].split(":")[1]][verdict] += 1
        for ipr, v in sorted(verdicts.items()):
            if not (v["REMOVE"] or v["NARROW"]):
                continue
            sigs = collections.Counter(db for db, _ in ipr_sigs.get(ipr, ()))
            accs = ipr_members.get(ipr, [])
            pf_counts: collections.Counter[str] = collections.Counter()
            for acc in accs:
                pf_counts.update(set(prot_pfams[acc]))
            splitters = [
                {"pfam": pf, "name": pfam_name.get(pf, ""), "share": round(c / len(accs), 3)}
                for pf, c in pf_counts.most_common()
                if accs and 0.05 <= c / len(accs) <= 0.95
            ]
            out["interpro2go_rows"].append({
                "entry": ipr, "name": ipr_name.get(ipr, ""), "type": ipr_type.get(ipr),
                "remove": v["REMOVE"], "narrow": v["NARROW"],
                "signatures": dict(sigs), "pfam_signatures": sigs.get("PFAM", 0),
                "reviewed_members": len(accs), "splitting_pfams": splitters[:6],
                "n_splitting_pfams": len(splitters),
            })
    return out


def write_report(prov, n_families, all_rows, shortlist, illustrations, census, args) -> None:
    def pct(x) -> str:
        return "n/a" if x is None else f"{100 * x:.0f}%"

    def num(x) -> str:
        return "n/a" if x is None else f"{x:,}"

    L: list[str] = []
    A = L.append
    A("---")
    A('title: "High-Value, Unique Pfam → GO Candidates"')
    A("---")
    A("")
    A("# High-Value, Unique Pfam → GO Candidates")
    A("")
    A("> Auto-generated by `high_value_unique.py`. Re-run to refresh. See [parent project](../PFAM.md). "
      "Every row is a **candidate for curation**, not an asserted mapping.")
    A("")
    A("## Question")
    A("")
    A("The [headroom analysis](HEADROOM.md) counted Pfam families that get no GO term through "
      "InterPro2GO. That count overstates the opportunity in two ways. Many of the obvious mappings "
      "are binding terms, which say little about what a protein does. And a family whose own InterPro "
      "entry has no GO term may still get the function through a different InterPro entry that the "
      "same proteins match. This page keeps only the candidates that survive both objections.")
    A("")
    A("## Provenance")
    A("")
    A(f"- InterPro release (entry membership): **{prov['interpro_release']}**")
    A(f"- interpro2go: {prov['interpro2go']}")
    A(f"- ec2go: {prov['ec2go']}")
    A(f"- GO: {prov['go']}")
    A(f"- UniProtKB release: **{prov['uniprot_release'] or 'not recorded'}**; "
      f"{prov['swissprot_entries']:,} reviewed entries")
    A(f"- Parameters: at least {args.min_members} reviewed members; purity at least {args.purity}; "
      f"term on at most {100 * args.max_freq:g}% of Swiss-Prot; at most {100 * args.max_supplied:g}% "
      "of members already supplied by InterPro2GO")
    A("")
    A("## Method")
    A("")
    A("1. **Function of a member.** Its GO molecular-function terms plus the GO terms that ec2go gives "
      "for its complete EC numbers, with all ancestors.")
    A("2. **High value.** The most specific terms carried by the required share of a family's reviewed "
      "members. Terms that sit only in the binding branch are dropped, and so are terms common enough "
      "to be uninformative.")
    A("3. **Unique.** For each member, the union of interpro2go terms over *every* InterPro entry the "
      "protein matches. A member is supplied when that union holds the term or a descendant. This is "
      "where a function arriving through a separate, unlinked entry is caught.")
    A("4. **Where the gain lands.** For shortlisted pairs, UniProt is asked how many unreviewed proteins "
      "match the family and how many already carry the term or a descendant from any pipeline.")
    A("5. **Route.** `UNINTEGRATED`: in no InterPro entry, so only a Pfam-level mapping reaches it. "
      "`SOLE_SIGNATURE`: the only signature of its entry, so adding the term to interpro2go on that "
      "entry is equivalent. `SHARED_ENTRY`: the entry has other signatures; the entry-level purity "
      "says whether the term still holds there.")
    A("")
    A("Limits: purity is measured on reviewed members only, and an unreviewed protein may carry the "
      "domain in a different architecture. A Swiss-Prot GO term may itself be electronic, so the count "
      "of members with experimental evidence is given beside each pair. Only molecular function is "
      "tested.")
    A("")

    # funnel
    by_route = collections.Counter(r["route"] for r in shortlist)
    supplied_rows = [r for r in all_rows if r["interpro_supplied"] > args.max_supplied]
    by_other = sum(
        1 for r in supplied_rows
        if any(not s["is_own_entry"] for s in r.get("supplying_entries", ()))
        and not any(s["is_own_entry"] for s in r.get("supplying_entries", ()))
    )
    A("## Funnel")
    A("")
    A("| Step | Count |")
    A("|---|---:|")
    A(f"| Pfam families with at least {args.min_members} reviewed members | {n_families:,} |")
    A(f"| (family, term) pairs that are specific, non-binding and shared by the family | {len(all_rows):,} |")
    A(f"| …already supplied by InterPro2GO on the members | {len(supplied_rows):,} |")
    A(f"| ……supplied only by an entry other than the family's own | {by_other:,} |")
    A(f"| **…not supplied: the shortlist** | **{len(shortlist):,}** |")
    A(f"| ……distinct Pfam families | {len({r['pfam'] for r in shortlist}):,} |")
    for route in ("UNINTEGRATED", "SOLE_SIGNATURE", "SHARED_ENTRY"):
        A(f"| ……route {route} | {by_route.get(route, 0):,} |")
    open_rows = [r for r in shortlist if r["open"]]
    with_exp = [r for r in open_rows if r["members_with_experimental_evidence"]]
    headline = [r for r in shortlist if r["headline"]]
    clean = [r for r in headline if not r["members_with_other_function"]]
    mixed = [r for r in headline if r["members_with_other_function"]]
    A(f"| …at most {pct(args.max_covered)} of unreviewed members already carry the term "
      f"(no other pipeline supplies it): open candidates | {len(open_rows):,} |")
    A(f"| ……with experimental evidence on at least one reviewed member | {len(with_exp):,} |")
    A(f"| **………one per set of proteins: headline candidates** | **{len(headline):,}** |")
    A(f"| …………no reviewed member contradicts the term | {len(clean):,} |")
    A(f"| …………some reviewed members do something else | {len(mixed):,} |")
    A("")
    branch_counts: collections.Counter[str] = collections.Counter()
    for r in headline:
        branch_counts.update(r["branches"])
    A("Headline candidates by top-level molecular-function branch (a term can sit in more than one):")
    A("")
    A("| Branch | Pairs |")
    A("|---|---:|")
    for b, c in branch_counts.most_common():
        A(f"| {b} | {c:,} |")
    A("")

    def table(rows: list[dict]) -> None:
        A("| Pfam | family | proposed term | reviewed | species | purity | exp | InterPro gives | "
          "unreviewed | already have term | would gain | route |")
        A("|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---|")
        for r in rows:
            fam = r["pfam_name"]
            if r.get("same_protein_families"):
                fam += f" (+{len(r['same_protein_families'])})"
            if r["interpro_general_only"] >= 0.5 and r.get("most_common_general_term"):
                gives = r["most_common_general_term"].split(" ", 1)[1]
            else:
                gives = "nothing"
            A(f"| {r['pfam']} | {fam} | {r['go_label']} ({r['go_id']}) | "
              f"{r['reviewed_members']:,} | {r['species_with_term']:,} | {pct(r['purity'])} | "
              f"{r['members_with_experimental_evidence']} | {gives} | "
              f"{num(r.get('unreviewed_members'))} | {pct(r.get('unreviewed_already_covered'))} | "
              f"{num(r.get('unreviewed_lacking_term'))} | {r['route']} |")
        A("")

    def is_enzyme_or_transporter(r: dict) -> bool:
        return bool({"catalytic activity", "transporter activity"} & set(r["branches"]))

    A("## Headline candidates")
    A("")
    A(f"A pair that InterPro2GO does not supply may still reach unreviewed proteins through UniRule, "
      f"ARBA or EC2GO. An open candidate is one where at most {pct(args.max_covered)} of the family's "
      f"unreviewed members already carry the term. A headline candidate is an open candidate with "
      f"experimental evidence on at least one reviewed member, counted once when several families hit "
      f"the same proteins. **{len(headline):,}** pairs qualify.")
    A("")
    if headline:
        nothing = sum(1 for r in headline if r["interpro_general_only"] < 0.5)
        A(f"- InterPro2GO gives these proteins no molecular-function ancestor of the term at all: "
          f"{nothing:,}. It gives a more general ancestor: {len(headline) - nothing:,}.")
        hroute = collections.Counter(r["route"] for r in headline)
        A("- Route: " + ", ".join(f"{k} {v:,}" for k, v in hroute.most_common()) + ".")
        A(f"- Enzymes and transporters: {sum(1 for r in headline if is_enzyme_or_transporter(r)):,}. "
          f"Other branches (adaptors, regulators, receptors, structural): "
          f"{sum(1 for r in headline if not is_enzyme_or_transporter(r)):,}.")
        robust = [r for r in clean if is_enzyme_or_transporter(r)
                  and r["species_with_term"] >= 5 and r["reviewed_members"] >= 10]
        A(f"- Best supported: enzymes and transporters with no contradicting member, at least ten "
          f"reviewed members and at least five species: **{len(robust):,}** "
          f"({sum(r['unreviewed_lacking_term'] for r in robust):,} unreviewed proteins lacking the "
          f"term; route " + ", ".join(
              f"{k} {v}" for k, v in collections.Counter(r["route"] for r in robust).most_common()) + ").")
        few = sum(1 for r in headline if r["species_with_term"] < 5)
        A(f"- Resting on fewer than five species among reviewed members: {few:,}. Purity on a handful "
          "of orthologs says little about the family at large; treat these as leads.")
        A("")
        A("Columns: `species` is the number of species among reviewed members that carry the term. "
          "`exp` is the number of reviewed members with experimental evidence. `InterPro gives` is the "
          "most specific ancestor that interpro2go supplies to most members. `already have term` is the "
          "share of unreviewed members that carry the term or a descendant from any pipeline. "
          "`(+N)` counts further families that hit the same proteins and are folded into the row. "
          "Ranked by `would gain`, the unreviewed members that lack the term. All open candidates: "
          "[`high_value_unique_candidates.yaml`](high_value_unique_candidates.yaml).")
        A("")
        clean_enz = [r for r in clean if is_enzyme_or_transporter(r)]
        clean_other = [r for r in clean if not is_enzyme_or_transporter(r)]
        A(f"### Enzymes and transporters, no contradicting member ({len(clean_enz):,})")
        A("")
        A("Every reviewed member either carries the term or has no other non-binding function "
          "recorded. These can be written as a plain family-to-term mapping.")
        A("")
        table(clean_enz[:45])
        A(f"### Other functions, no contradicting member ({len(clean_other):,})")
        A("")
        A("Adaptor, regulator, receptor and structural terms. Many of these families are regions of one "
          "eukaryotic protein with few reviewed members.")
        A("")
        table(clean_other[:25])
        A(f"### Some reviewed members do something else ({len(mixed):,})")
        A("")
        A("At least one reviewed member lacks the term and carries a different non-binding function. "
          "A plain mapping would mis-annotate those members, so each of these needs a restricting "
          "condition (a second signature, a taxon) and belongs in a curated rule, not a mapping file. "
          "`other` is the number of such members; the YAML lists up to five with their function.")
        A("")
        A("| Pfam | family | proposed term | reviewed | purity | other | example of another function | "
          "unreviewed | would gain | route |")
        A("|---|---|---|---:|---:|---:|---|---:|---:|---|")
        for r in mixed[:34]:
            ex = r["counter_examples"][0]
            A(f"| {r['pfam']} | {r['pfam_name']} | {r['go_label']} ({r['go_id']}) | "
              f"{r['reviewed_members']:,} | {pct(r['purity'])} | {r['members_with_other_function']} | "
              f"{ex['accession']}: {ex['function'].split(' ', 1)[1]} | "
              f"{num(r.get('unreviewed_members'))} | {num(r.get('unreviewed_lacking_term'))} | "
              f"{r['route']} |")
        A("")
    A("## Only a Pfam-level mapping can reach these")
    A("")
    A("Headline candidates whose family is in no InterPro entry, or shares its entry with other "
      "signatures and holds the term better than the entry does. For every other headline candidate, "
      "adding the term to interpro2go on the family's own entry would do the same job.")
    A("")
    pfam_only = [
        r for r in headline
        if r["route"] == "UNINTEGRATED"
        or (r["route"] == "SHARED_ENTRY" and r.get("own_entry_purity", 1) < args.purity)
    ]
    if pfam_only:
        table(pfam_only[:40])
    else:
        A("None.")
        A("")

    A("## Does the function arrive through another InterPro entry?")
    A("")
    A("Traced pairs, reported whatever the filters say: the SH2 example from the project page, and the "
      "molecular-function terms of the Pfam entries already curated under `interpro/pfam/`. `supplied` "
      "is the share of reviewed members that get the term through any matched InterPro entry.")
    A("")
    A("| Pfam | term | origin | binding only | reviewed | carry term | supplied | supplying entries | "
      "unreviewed | already have term |")
    A("|---|---|---|---|---:|---:|---:|---|---:|---:|")
    for r in illustrations:
        sup = "; ".join(
            f"{s['entry']} {s['name']} ({s['members']}{', own entry' if s['is_own_entry'] else ''})"
            for s in r.get("supplying_entries", ())) or "none"
        n_all, n_term = r.get("unreviewed_members"), r.get("unreviewed_with_term")
        share = None if not n_all or n_term is None else n_term / n_all
        A(f"| {r['pfam']} {r['pfam_name']} | {r['go_label']} ({r['go_id']}) | {r['origin']} | "
          f"{'yes' if r['binding_only'] else 'no'} | {r['reviewed_members']:,} | {pct(r['purity'])} | "
          f"{pct(r['interpro_supplied'])} | {sup} | {num(n_all)} | {pct(share)} |")
    A("")

    A("## Is Pfam used in the restricting rules we have?")
    A("")
    types = census["condition_types"]
    A(f"Curated rules (`rules/curated`): {len(census['curated_rules'])}. Condition types used: "
      + ", ".join(f"{k} ×{v}" for k, v in types.most_common()) + ". "
      f"Rules with a Pfam condition: **{sum(1 for r in census['curated_rules'] if 'PFAM' in r['types'])}**. "
      f"Rules with a negated condition: {sum(1 for r in census['curated_rules'] if r['negated_conditions'])}.")
    A("")
    rows = census["interpro2go_rows"]
    if rows:
        A(f"InterPro2GO removals and narrowings (`projects/INTERPRO/interpro2go.sssom.yaml`): "
          f"{len(rows)} entries. For each, whether a Pfam family is a member signature, and which Pfam "
          "families are found on between 5% and 95% of the entry's reviewed members. Such a family "
          "could serve as a splitting condition; whether it separates right from wrong members is a "
          "curation question this table does not answer.")
        A("")
        A("| InterPro | name | type | remove | narrow | Pfam member signatures | reviewed | "
          "Pfam families that split the members |")
        A("|---|---|---|---:|---:|---:|---:|---|")
        for r in rows:
            split = "; ".join(f"{s['pfam']} {s['name']} ({pct(s['share'])})" for s in r["splitting_pfams"])
            if r["n_splitting_pfams"] > len(r["splitting_pfams"]):
                split += f"; +{r['n_splitting_pfams'] - len(r['splitting_pfams'])} more"
            A(f"| {r['entry']} | {r['name']} | {r['type']} | {r['remove']} | {r['narrow']} | "
              f"{r['pfam_signatures']} | {r['reviewed_members']:,} | {split or 'none'} |")
        A("")
    (HERE / "HIGH_VALUE_UNIQUE.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
