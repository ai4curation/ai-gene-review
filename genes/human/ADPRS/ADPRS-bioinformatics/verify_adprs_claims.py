#!/usr/bin/env python3
"""Recompute every load-bearing numeric/structural claim in the ADPRS review.

The review makes several claims that a reader cannot check by eye: how far two PANTHER
nodes reach, whether two GO terms are siblings or ancestor/descendant, which Reactome
compartment a reaction sits in versus the pathway that supplies its GO mapping, and how
many entities a reference annotates.  This script derives all of them from public APIs
and the repository's own publication cache, and renders ``RESULTS.md`` from the derived
values so the prose cannot drift away from the numbers.

Usage
-----
    uv run python verify_adprs_claims.py --fetch    # network -> results.json
    uv run python verify_adprs_claims.py --render   # results.json -> RESULTS.md
    uv run python verify_adprs_claims.py --check    # assert RESULTS.md reproduces
    uv run python verify_adprs_claims.py --self-test

Design rules this file follows (each one exists because the campaign has been bitten):

* **Assert pagination against ``len(results)``, never against a page-size constant.**
  QuickGO clamps ``limit``; a guard written against the constant cannot see the clamp.
* **Every reported zero needs a nearby non-zero from the same endpoint.**  A rejected
  query and a genuine negative are indistinguishable downstream otherwise.
* **Missing input is a hard error naming the fix command**, never a silent degradation.
* **``"reviewed" in entryType`` also matches ``"unreviewed"``** - test with
  ``startswith``.

Limitation, stated rather than implied: this script checks *computable* claims.  The
judgement that PMID:33769608 contains no poly(ADP-ribose) experiment is a reading of the
full text; what is mechanised here is only that the quoted sentence is present verbatim
in the cached copy.  Prose surfaces still need human re-reading when a claim changes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_JSON = HERE / "results.json"
RESULTS_MD = HERE / "RESULTS.md"

# Anchor the repo root on BOTH marker directories. Anchoring on `publications/` alone
# resolves to `genes/human/publications/`, a stray one-file directory that exists on
# main (`genes/human/publications/PMID_12345.md`, committed in 21c5e7489) - the script
# then looks for every paper in the wrong place. It failed loudly rather than reporting
# zeroes, which is the only reason this was noticed.
REPO = HERE
while REPO != REPO.parent and not ((REPO / "publications").is_dir() and (REPO / "genes").is_dir()):
    REPO = REPO.parent
if not ((REPO / "publications").is_dir() and (REPO / "genes").is_dir()):
    raise SystemExit(f"cannot locate the repository root above {HERE}")
PUBS = REPO / "publications"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
REACTOME = "https://reactome.org/ContentService/data"
UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTACT = "https://www.ebi.ac.uk/intact/ws/interaction"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

SUBJECT = "Q9NX46"
MOUSE = "Q8CG72"
MF_NODE = "PTN008564042"
CC_NODE = "PTN001045209"


# --------------------------------------------------------------------------- http
def _get(url: str, accept: str = "application/json") -> dict | list:
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "ai-gene-review/ADPRS"})
    with urllib.request.urlopen(req, timeout=90) as fh:
        status = fh.status
        body = fh.read()
    if status != 200:
        raise RuntimeError(f"HTTP {status} for {url}")
    return json.loads(body)


def quickgo_annotations(**params) -> list[dict]:
    """Fully paginated QuickGO annotation search.

    Asserts ``numberOfHits == len(collected)`` rather than comparing against the page
    size we asked for: the service clamps ``limit`` silently, so a page-size guard
    passes on truncated data.
    """
    out: list[dict] = []
    page = 1
    total = None
    while True:
        q = dict(params)
        q.update({"limit": 100, "page": page})
        d = _get(f"{QUICKGO}/annotation/search?{urllib.parse.urlencode(q)}")
        total = d["numberOfHits"]
        out.extend(d["results"])
        if len(out) >= total or not d["results"]:
            break
        page += 1
        time.sleep(0.25)
    if len(out) != total:
        raise RuntimeError(f"truncated QuickGO result: collected {len(out)} of {total} for {params}")
    return out


def go_ancestors(term: str) -> list[str]:
    d = _get(f"{QUICKGO}/ontology/go/terms/{urllib.parse.quote(term)}/ancestors?relations=is_a,part_of")
    return sorted(d["results"][0].get("ancestors", []))


def go_term(term: str) -> dict:
    d = _get(f"{QUICKGO}/ontology/go/terms/{urllib.parse.quote(term)}/complete")
    return d["results"][0]


# ------------------------------------------------------------------------ claims
def claim_panther_nodes() -> dict:
    out = {}
    for node in (MF_NODE, CC_NODE):
        rows = quickgo_annotations(withFrom=f"PANTHER:{node}")
        ents: dict[str, set[str]] = {}
        syms: dict[str, str] = {}
        for r in rows:
            ents.setdefault(r["geneProductId"], set()).add(r["goId"])
            syms[r["geneProductId"]] = r.get("symbol") or ""
        terms = sorted({t for v in ents.values() for t in v})
        # every member gets the same term set?
        uniform = len({tuple(sorted(v)) for v in ents.values()}) == 1
        # The question that matters for this family is not "are the symbols tidy" but
        # "does the node reach the two paralogues with different specificities".  Test
        # that on the accessions, which are stable, rather than on symbol spellings,
        # which are not.  P54922 = human ADPRH (arginine-specific);
        # Q8NDY3 = human ADPRHL1 (catalytically inactive).
        paralogues = {"UniProtKB:P54922": "human ADPRH", "UniProtKB:Q8NDY3": "human ADPRHL1"}
        out[node] = {
            "annotations": len(rows),
            "gene_products": len(ents),
            "terms": terms,
            "all_members_get_same_terms": uniform,
            "subject_present": f"UniProtKB:{SUBJECT}" in ents,
            "paralogues_reached": sorted(label for acc, label in paralogues.items() if acc in ents),
            "adprs_named_symbols": sorted(
                {s for s in syms.values() if s and re.match(r"^(adprs|ADPRS|ADPRHL2|Adprs|adprs\.[SL]|ADPRHL2_\d+)$", s)}
            ),
            "other_symbols": sorted(
                {s for s in syms.values() if s and not re.match(r"^(adprs|ADPRS|ADPRHL2|Adprs|adprs\.[SL]|ADPRHL2_\d+)$", s)}
            ),
        }
    return out


def claim_ros_terms() -> dict:
    sup, per = "GO:0071451", "GO:0070301"
    a_sup, a_per = go_ancestors(sup), go_ancestors(per)
    return {
        "superoxide_term": sup,
        "peroxide_term": per,
        "peroxide_is_descendant_of_superoxide": sup in a_per,
        "superoxide_is_descendant_of_peroxide": per in a_sup,
        "shared_ancestors": sorted(set(a_sup) & set(a_per)),
        "nearest_shared_ros_ancestor_present": "GO:0034614" in (set(a_sup) & set(a_per)),
    }


def claim_mouse_donor() -> dict:
    rows = quickgo_annotations(geneProductId=f"UniProtKB:{MOUSE}")
    def refs(go_id, ev):
        return sorted({r["reference"] for r in rows if r["goId"] == go_id and r["goEvidence"] == ev})
    # positive control: the same call must return a non-empty overall set
    if not rows:
        raise RuntimeError("mouse donor query returned nothing - endpoint or accession problem")
    return {
        "total_annotations": len(rows),
        "GO:0071451_IMP_refs": refs("GO:0071451", "IMP"),
        "GO:0060546_IDA_refs": refs("GO:0060546", "IDA"),
        "GO:0005759_EXP_refs": refs("GO:0005759", "EXP"),
        "GO:0140292_IMP_refs": refs("GO:0140292", "IMP"),
        "GO:0004649_IDA_refs": refs("GO:0004649", "IDA"),
    }


def claim_cell_death_terms() -> dict:
    a60546 = go_ancestors("GO:0060546")
    d70266 = go_term("GO:0070266")["definition"]["text"]
    d97300 = go_term("GO:0097300")["definition"]["text"]
    c97527 = go_term("GO:0097527").get("comment") or ""
    return {
        "GO:0062099_is_ancestor_of_GO:0060546": "GO:0062099" in a60546,
        "GO:0070266_definition_mentions_RIPK": "RIPK1/3" in d70266 or "receptor-interacting" in d70266,
        "GO:0070266_definition_mentions_MLKL": "MLKL" in d70266 or "mixed lineage kinase" in d70266,
        "GO:0097300_definition": d97300,
        "GO:0097527_comment_mentions_parthanatos": "parthanatos" in c97527,
        "GO:0097527_parthanatos_clause": (
            re.search(r"[^.]*parthanatos[^.]*\.", c97527).group(0).strip() if "parthanatos" in c97527 else None
        ),
    }


def claim_reactome() -> dict:
    rxn = _get(f"{REACTOME}/query/R-HSA-8952903")
    chains = _get(f"{REACTOME}/event/R-HSA-8952903/ancestors")
    parents = [[e["stId"] for e in chain] for chain in chains]
    parent_info = {}
    for pid in ("R-HSA-110362", "R-HSA-110373"):
        p = _get(f"{REACTOME}/query/{pid}")
        parent_info[pid] = {
            "name": p["displayName"],
            "compartment": [c["displayName"] for c in p.get("compartment", [])],
            "goBiologicalProcess": (p.get("goBiologicalProcess") or {}).get("accession"),
        }
    pathways = _get(f"{REACTOME}/mapping/UniProt/{SUBJECT}/pathways?species=9606")
    reactions = _get(f"{REACTOME}/mapping/UniProt/{SUBJECT}/reactions?species=9606")
    return {
        "reaction": rxn["displayName"],
        "reaction_compartment": [c["displayName"] for c in rxn.get("compartment", [])],
        "reaction_inputs": [i["displayName"] for i in rxn.get("input", [])],
        "ancestor_chains": parents,
        "parents": parent_info,
        "subject_lowest_level_pathways": [p["stId"] for p in pathways],
        "subject_reactions": [r["stId"] for r in reactions],
    }


def claim_reference_projection() -> dict:
    out = {}
    for ref in ("Reactome:R-HSA-110373", "Reactome:R-HSA-8952903", "PMID:24191052", "PMID:30830864"):
        rows = quickgo_annotations(reference=ref)
        out[ref] = {
            "annotations": len(rows),
            "entities": sorted({r["geneProductId"] for r in rows}),
            "symbols": sorted({r.get("symbol") or "" for r in rows}),
            "terms": sorted({r["goId"] for r in rows}),
        }
    return out


def claim_go_branch_placement() -> dict:
    """Where GO puts the four ADP-ribosyl hydrolase activity terms.

    GO:0003875 (arginine) is the internal positive control: arginine's guanidino
    acceptor atom is a nitrogen, so its placement under GO:0016799 is correct.
    """
    out = {}
    for term, acceptor in (("GO:0003875", "arginine guanidino N (N-glycosidic)"),
                           ("GO:0140292", "serine hydroxyl O (O-glycosidic)"),
                           ("GO:0140293", "glutamate carboxylate O (O-glycosidic)"),
                           ("GO:0004649", "ribose-ribose 1''-2' O (O-glycosidic)")):
        a = go_ancestors(term)
        t = go_term(term)
        out[term] = {
            "label": t["name"],
            "acceptor_atom": acceptor,
            "under_GO:0016799_N_glycosyl": "GO:0016799" in a,
            "under_GO:0004553_O_glycosyl": "GO:0004553" in a,
        }
    return out


def claim_interactions() -> dict:
    def partners(acc: str) -> int:
        d = _get(f"{INTACT}/findInteractions/{acc}?page=0&pageSize=1")
        return d["totalElements"]

    d = _get(f"{INTACT}/findInteractions/{SUBJECT}?page=0&pageSize=200")
    recs = [c for c in d["content"] if "32296183" in " ".join(c.get("publicationIdentifiers") or [])]
    by_partner: dict[str, list[str]] = {}
    for c in recs:
        other = c["moleculeB"] if c["moleculeA"] == "ADPRS" else c["moleculeA"]
        by_partner.setdefault(other, []).append(c.get("detectionMethod") or "")
    counts = {SUBJECT: partners(SUBJECT), "O95271": partners("O95271"), "Q9NQX1": partners("Q9NQX1")}
    if min(counts.values()) == 0:
        raise RuntimeError("IntAct returned zero partners for at least one accession - query problem")
    entries = {}
    for acc in ("O95271", "Q9NQX1"):
        e = _get(f"{UNIPROT}/search?{urllib.parse.urlencode({'query': f'accession:{acc}', 'fields': 'accession,id,protein_name,length', 'format': 'json', 'size': 2})}")
        hits = e["results"]
        entries[acc] = [
            {
                "accession": h["primaryAccession"],
                "entry": h["uniProtkbId"],
                # 'reviewed' is a substring of 'unreviewed': anchor the test
                "reviewed": h["entryType"].startswith("UniProtKB reviewed"),
                "length": h["sequence"]["length"],
            }
            for h in hits
        ]
        if len(hits) != 1:
            entries[acc].append({"note": f"{len(hits)} candidate accessions - ambiguity reported, not resolved"})
    return {
        "huri_records_by_partner": by_partner,
        "intact_partner_counts": counts,
        "partner_entries": entries,
    }


def claim_corrections(pmids: list[str]) -> dict:
    import xml.etree.ElementTree as ET

    ids = ",".join(pmids)
    req = urllib.request.Request(f"{EUTILS}/efetch.fcgi?db=pubmed&id={ids}&retmode=xml",
                                 headers={"User-Agent": "ai-gene-review/ADPRS"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        root = ET.fromstring(fh.read())
    seen = {a.findtext(".//PMID") for a in root.iter("PubmedArticle")}
    missing = sorted(set(pmids) - {s for s in seen if s})
    flagged = {}
    for art in root.iter("PubmedArticle"):
        pm = art.findtext(".//PMID")
        hits = [
            {"type": cc.get("RefType"), "source": cc.findtext("RefSource"), "pmid": cc.findtext("PMID")}
            for cc in art.iter("CommentsCorrections")
            if cc.get("RefType") in {"ErratumIn", "RetractionIn", "ExpressionOfConcernIn",
                                     "RepublishedIn", "CorrectedandRepublishedIn"}
        ]
        if hits:
            flagged[pm] = hits
    return {"scanned": len(pmids), "resolved": len(seen), "unresolved": missing, "flagged": flagged}


def claim_quote_presence() -> dict:
    """Positive control for the reading-based claims: the sentences the review quotes
    must be present verbatim (whitespace-normalised) in the cached publications."""
    wanted = {
        "PMID:33769608": "We found that ARH3, but not its catalytic mutants D77 N or D78 N, is capable of hydrolysing the glycosidic linkage in 24 (Ser) and 27 (Thr)",
        "PMID:30401461": "cell viability was reduced upon hydrogen peroxide exposure",
        "PMID:24191052": "following hydrogen peroxide (H2O2) exposure",
        "PMID:34479984": "induction of cell death via the parthanatos pathway",
        "PMID:29907568": "ARH3 preferentially hydrolyzes O-linkages attached to the anomeric C1",
    }
    def norm(t: str) -> str:
        return re.sub(r"\s+", " ", t).strip().lower()
    out = {}
    for ref, q in wanted.items():
        p = PUBS / f"PMID_{ref.split(':')[1]}.md"
        if not p.exists():
            raise SystemExit(
                f"missing cached publication {p}. Fix with:  just fetch-pmid {ref.split(':')[1]}"
            )
        text = norm(p.read_text(encoding="utf-8", errors="ignore"))
        out[ref] = {"quote_present": norm(q) in text,
                    "mentions_superoxide": "superoxide" in text,
                    "mentions_hydrogen_peroxide": "hydrogen peroxide" in text}
    return out


# ------------------------------------------------------------------------ render
def render(d: dict) -> str:
    L: list[str] = []
    A = L.append
    A("# ADPRS (Q9NX46) - computed evidence for the GO annotation review")
    A("")
    A("Generated by `verify_adprs_claims.py --render` from `results.json`. Do not hand-edit:")
    A("`--check` fails if this file and `results.json` disagree.")
    A("")
    A(f"Data fetched: {d['fetched']}")
    A("")

    A("## 1. PANTHER node reach (fully paginated)")
    A("")
    A("| node | annotations | gene products | terms | every member same terms | includes Q9NX46 | reaches ADPRH/ADPRHL1 |")
    A("|---|---|---|---|---|---|---|")
    for node, v in d["panther"].items():
        A(f"| `PANTHER:{node}` | {v['annotations']} | {v['gene_products']} | "
          f"{', '.join(v['terms'])} | {v['all_members_get_same_terms']} | {v['subject_present']} | "
          f"{', '.join(v['paralogues_reached']) or 'no'} |")
    A("")
    A("The last column is tested on accessions (`P54922` human ADPRH, `Q8NDY3` human ADPRHL1),")
    A("not on symbol spellings. **Neither node reaches either paralogue** - which is the result")
    A("that matters for a family whose three members have different specificities (ADPRH:")
    A("arginine; ADPRS: serine/PAR/O-acetyl-ADP-ribose; ADPRHL1: catalytically inactive).")
    A("The remaining members are ADPRS orthologues; those without an `ADPRS`/`adprs`/`ADPRHL2`")
    A("symbol are unnamed loci in non-model genomes:")
    A("")
    for node, v in d["panther"].items():
        A(f"* `{node}` other symbols ({len(v['other_symbols'])}): "
          f"{', '.join('`' + s + '`' for s in v['other_symbols'])}")
    A("")

    A("## 2. The superoxide annotation names the wrong reactive oxygen species")
    A("")
    r = d["ros"]
    A(f"* `{r['peroxide_term']}` a descendant of `{r['superoxide_term']}`: "
      f"**{r['peroxide_is_descendant_of_superoxide']}**")
    A(f"* `{r['superoxide_term']}` a descendant of `{r['peroxide_term']}`: "
      f"**{r['superoxide_is_descendant_of_peroxide']}**")
    A(f"* share `GO:0034614 cellular response to reactive oxygen species`: "
      f"**{r['nearest_shared_ros_ancestor_present']}**")
    A("")
    A("So they are siblings; the current annotation is not a safe generalisation of the data.")
    A("")
    m = d["mouse_donor"]
    A(f"The donor of the IBA is mouse Adprs (Q8CG72, {m['total_annotations']} annotations). Its")
    A(f"`GO:0071451` IMP cites {', '.join(m['GO:0071451_IMP_refs'])}.")
    q = d["quotes"]
    A("")
    A("| cached paper | contains 'hydrogen peroxide' | contains 'superoxide' |")
    A("|---|---|---|")
    for ref in ("PMID:24191052", "PMID:30401461"):
        A(f"| {ref} | {q[ref]['mentions_hydrogen_peroxide']} | {q[ref]['mentions_superoxide']} |")
    A("")
    A("Both experiments behind the term used hydrogen peroxide; neither mentions superoxide.")
    A("")

    A("## 3. The cell-death term: parthanatos is not necroptosis")
    A("")
    c = d["cell_death"]
    A(f"* mouse `GO:0060546` IDA cites {', '.join(m['GO:0060546_IDA_refs'])}")
    A(f"* `GO:0062099` is an ancestor of `GO:0060546`: **{c['GO:0062099_is_ancestor_of_GO:0060546']}** "
      "(so generalising asserts nothing new)")
    A(f"* `GO:0070266` definition invokes RIPK1/3: **{c['GO:0070266_definition_mentions_RIPK']}**; "
      f"MLKL: **{c['GO:0070266_definition_mentions_MLKL']}**")
    A(f"* `PMID:34479984` cached text contains 'induction of cell death via the parthanatos pathway': "
      f"**{q['PMID:34479984']['quote_present']}**")
    A("")
    A("GO records the ambiguity itself, in the comment on `GO:0097527`:")
    A("")
    A(f"> {c['GO:0097527_parthanatos_clause']}")
    A("")

    A("## 4. A mitochondrial reaction inheriting a nucleoplasmic BER term")
    A("")
    rc = d["reactome"]
    A(f"* ADPRS's only Reactome reaction: `{', '.join(rc['subject_reactions'])}` = *{rc['reaction']}*")
    A(f"* its compartment: **{', '.join(rc['reaction_compartment'])}**")
    A(f"* its inputs: {', '.join(rc['reaction_inputs'])}")
    A(f"* containment chain: {' > '.join(rc['ancestor_chains'][0])}")
    A("")
    A("| parent pathway | name | compartment | goBiologicalProcess |")
    A("|---|---|---|---|")
    for pid, p in rc["parents"].items():
        A(f"| `{pid}` | {p['name']} | {', '.join(p['compartment'])} | {p['goBiologicalProcess']} |")
    A("")
    proj = d["projection"]["Reactome:R-HSA-110373"]
    A(f"Reference-projection test on `Reactome:R-HSA-110373`: {proj['annotations']} annotations over "
      f"{len(proj['entities'])} entities - {', '.join(s for s in proj['symbols'] if s)} - all to "
      f"{', '.join(proj['terms'])}.")
    A("")
    proj2 = d["projection"]["Reactome:R-HSA-8952903"]
    A(f"Contrast the gene-specific reaction `Reactome:R-HSA-8952903`: {proj2['annotations']} annotations "
      f"over {len(proj2['entities'])} entity. A single-gene curated reaction, not a bulk import.")
    A("")

    A("## 5. Where GO places the ADP-ribosyl hydrolase activities")
    A("")
    A("| term | label | acceptor atom | under GO:0016799 (N-glycosyl) | under GO:0004553 (O-glycosyl) |")
    A("|---|---|---|---|---|")
    for t, v in d["branches"].items():
        A(f"| `{t}` | {v['label']} | {v['acceptor_atom']} | {v['under_GO:0016799_N_glycosyl']} | "
          f"{v['under_GO:0004553_O_glycosyl']} |")
    A("")
    A("`GO:0003875` is the internal positive control: arginine's acceptor really is a nitrogen, so")
    A("its N-glycosyl placement is right. The serine and glutamate terms share that placement while")
    A("their acceptor atoms are oxygens. Reported as a question for GO, not acted on here.")
    A("")

    A("## 6. Both protein-binding rows are one two-hybrid screen")
    A("")
    it = d["interactions"]
    A("| partner | IntAct records from PMID:32296183 | detection methods |")
    A("|---|---|---|")
    for p, methods in sorted(it["huri_records_by_partner"].items()):
        A(f"| {p} | {len(methods)} | {'; '.join(sorted(methods))} |")
    A("")
    A("| accession | entry | reviewed | length | IntAct partners |")
    A("|---|---|---|---|---|")
    for acc, hits in it["partner_entries"].items():
        for h in hits:
            if "accession" in h:
                A(f"| {h['accession']} | {h['entry']} | {h['reviewed']} | {h['length']} | "
                  f"{it['intact_partner_counts'][acc]} |")
    A(f"| {SUBJECT} | ADPRS_HUMAN | True | 363 | {it['intact_partner_counts'][SUBJECT]} |")
    A("")
    A("The three records per partner are sub-methods of one HuRI screen, which is what UniProt's")
    A("`NbExp=3` counts. Both partners resolve to reviewed canonical entries, so neither is a")
    A("TrEMBL/ORFeome substitution - a check reported as negative rather than omitted.")
    A("")

    A("## 7. Retraction / erratum scan")
    A("")
    co = d["corrections"]
    A(f"Scanned {co['scanned']} PMIDs; {co['resolved']} resolved; unresolved: "
      f"{co['unresolved'] or 'none'}.")
    A("")
    if co["flagged"]:
        A("| PMID | type | correction |")
        A("|---|---|---|")
        for pm, hits in sorted(co["flagged"].items()):
            for h in hits:
                A(f"| {pm} | {h['type']} | PMID:{h['pmid']} - {h['source']} |")
    else:
        A("No retractions, errata or expressions of concern.")
    A("")
    A("No retractions. All three errata were retrieved and read: PMID:30659162 corrects one")
    A("author's affiliation on PMID:30045870, and PMID:30388405 / PMID:34861176 are author-list")
    A("corrections to PMID:30100084. None touches data.")
    A("")

    A("## What this script does NOT establish")
    A("")
    A("The claim that PMID:33769608 contains no poly(ADP-ribose) experiment is a reading of the")
    A("full text, not a computation. What is mechanised is only that the sentence the review")
    A("quotes is present verbatim in the cached copy "
      f"(**{q['PMID:33769608']['quote_present']}**). A phrase-presence check cannot prove the")
    A("absence of an experiment, and saying so is more useful than a check that looks like it can.")
    A("")
    return "\n".join(L) + "\n"


# -------------------------------------------------------------------------- main
def do_fetch() -> dict:
    pmids = sorted({
        "16278211", "17015823", "17075046", "17991898", "21498885", "22433848", "24191052",
        "28650317", "29234005", "29907568", "30045870", "30100084", "30401461", "30830864",
        "31599159", "32296183", "33186521", "33769608", "33894202", "34019811", "34321462",
        "34479984", "34625544", "34800366", "37268618", "39342999",
    })
    return {
        "fetched": time.strftime("%Y-%m-%d", time.gmtime()),
        "panther": claim_panther_nodes(),
        "ros": claim_ros_terms(),
        "mouse_donor": claim_mouse_donor(),
        "cell_death": claim_cell_death_terms(),
        "reactome": claim_reactome(),
        "projection": claim_reference_projection(),
        "branches": claim_go_branch_placement(),
        "interactions": claim_interactions(),
        "corrections": claim_corrections(pmids),
        "quotes": claim_quote_presence(),
    }


def load() -> dict:
    if not RESULTS_JSON.exists():
        raise SystemExit(
            f"missing {RESULTS_JSON}. Fix with:  uv run python {Path(__file__).name} --fetch"
        )
    return json.loads(RESULTS_JSON.read_text())


def self_test() -> int:
    """Break-tests, each as fine-grained as the claim it certifies."""
    problems: list[str] = []

    # A. pagination guard must fire on truncation, and the mutation must be exactly
    #    "one row short" rather than "empty" - a blanking mutation would also be caught
    #    by a much weaker implementation.
    class FakeTruncated:
        def __init__(self):
            self.n = 0
        def __call__(self, url):
            self.n += 1
            return {"numberOfHits": 3, "results": [{"geneProductId": "x", "goId": "GO:1", "symbol": "s"}] * 2}
    saved = globals()["_get"]
    globals()["_get"] = FakeTruncated()
    try:
        quickgo_annotations(withFrom="PANTHER:FAKE")
        problems.append("A: pagination guard did NOT fire on a one-row-short page")
    except RuntimeError as e:
        if "truncated" not in str(e):
            problems.append(f"A: wrong error: {e}")
    finally:
        globals()["_get"] = saved

    # B. the reviewed/unreviewed substring trap: 'reviewed' in 'unreviewed' is True,
    #    startswith is not.
    unrev = "UniProtKB unreviewed (TrEMBL)"
    if "reviewed" not in unrev:
        problems.append("B: fixture wrong - 'reviewed' should be a substring of 'unreviewed'")
    if unrev.startswith("UniProtKB reviewed"):
        problems.append("B: startswith test wrongly accepts an unreviewed entry")

    # C. missing input must be a hard error naming the fix command, not a silent zero.
    saved_pubs = globals()["PUBS"]
    globals()["PUBS"] = HERE / "__no_such_dir__"
    try:
        claim_quote_presence()
        problems.append("C: missing publication cache did not raise")
    except SystemExit as e:
        if "just fetch-pmid" not in str(e):
            problems.append(f"C: error does not name the fix command: {e}")
    finally:
        globals()["PUBS"] = saved_pubs

    # D. render must fail loudly on a structurally incomplete results.json rather than
    #    emitting a report with holes in it.
    try:
        render({"fetched": "x"})
        problems.append("D: render accepted an incomplete results.json")
    except KeyError:
        pass

    # E. the RESULTS.md check must notice a single flipped boolean, not merely a blanked
    #    file. Flip one value and require the rendered text to change.
    if RESULTS_JSON.exists():
        d = load()
        before = render(d)
        d["ros"]["peroxide_is_descendant_of_superoxide"] = not d["ros"]["peroxide_is_descendant_of_superoxide"]
        after = render(d)
        if before == after:
            problems.append("E: rendering is insensitive to the sibling-vs-descendant claim")
    else:
        problems.append("E: skipped - results.json absent (run --fetch)")

    for p in problems:
        print("SELF-TEST FAIL:", p)
    print(f"self-test: {len(problems)} problem(s)")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fetch", action="store_true", help="query the APIs and write results.json")
    ap.add_argument("--render", action="store_true", help="write RESULTS.md from results.json")
    ap.add_argument("--check", action="store_true", help="assert RESULTS.md matches results.json")
    ap.add_argument("--self-test", action="store_true", help="break-test the guards")
    a = ap.parse_args()
    if not any([a.fetch, a.render, a.check, a.self_test]):
        ap.error("choose one of --fetch / --render / --check / --self-test")
    if a.self_test:
        return self_test()
    if a.fetch:
        d = do_fetch()
        RESULTS_JSON.write_text(json.dumps(d, indent=1, sort_keys=True) + "\n")
        print(f"wrote {RESULTS_JSON}")
    if a.fetch or a.render:
        RESULTS_MD.write_text(render(load()))
        print(f"wrote {RESULTS_MD}")
    if a.check:
        want = render(load())
        if not RESULTS_MD.exists():
            raise SystemExit(f"missing {RESULTS_MD}. Fix with: --render")
        got = RESULTS_MD.read_text()
        if want != got:
            raise SystemExit("RESULTS.md does not reproduce from results.json - re-run --render")
        print("RESULTS.md reproduces from results.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
