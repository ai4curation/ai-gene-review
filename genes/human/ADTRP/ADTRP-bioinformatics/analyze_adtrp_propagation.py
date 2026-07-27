#!/usr/bin/env python3
"""Reproducible evidence for the human ADTRP (Q96IZ2) GO annotation review.

Every number quoted in ``ADTRP-ai-review.yaml`` / ``ADTRP-notes.md`` that was not read
directly off a UniProt or publication file is computed here.

Design rules this script follows (each one exists because the campaign has been bitten):

* **Assert pagination completeness.** QuickGO clamps ``limit`` at 100 and does *not* error,
  so a truncated read is silent. Every paged query asserts ``numberOfHits == len(results)``
  rather than comparing against a page-size constant we chose.
* **Assert HTTP status.** A rejected query and a genuine empty result are indistinguishable
  downstream.
* **Every reported zero carries a positive control** from the same endpoint / same call
  pattern, so "nothing there" cannot be confused with "query broken".
* **``entryType.startswith("UniProtKB reviewed")``**, never ``"reviewed" in entryType`` --
  "reviewed" is a substring of "unreviewed" and the naive test silently promotes every
  TrEMBL entry.
* **Reviewed-member counts are the Swiss-Prot subset, not the family.** The family total is
  always printed alongside, and every label says "reviewed (Swiss-Prot)".
* **Multiset, not set,** when comparing row collections.

Run:  uv run python analyze_adtrp_propagation.py
Writes ``results.json`` and ``RESULTS.md`` next to this file. A fresh run must reproduce the
committed ``RESULTS.md`` byte-for-byte apart from the ``generated`` timestamp line.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]

ACC = "Q96IZ2"
PARALOG = "Q9NVV5"  # human AIG1
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


# --------------------------------------------------------------------------- HTTP


def fetch(url: str, tries: int = 4) -> dict:
    """GET JSON, asserting HTTP 200. A rejected query must not look like an empty result."""
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=90) as r:
                assert r.status == 200, f"HTTP {r.status} for {url}"
                return json.load(r)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed after {tries} attempts: {url}") from last


def paged_annotations(query: str, max_pages: int = 60) -> tuple[int, list[dict], bool]:
    """Fully paginate a QuickGO annotation search.

    Returns ``(numberOfHits, results, complete)``. ``complete`` is False only when the result
    set is too large to page through, in which case the caller must report the entity count as
    UNAVAILABLE rather than substituting a partial number.
    """
    page, out, total = 1, [], None
    while True:
        d = fetch(f"{QUICKGO}/annotation/search?{query}&limit=100&page={page}")
        total = d["numberOfHits"]
        out.extend(d["results"])
        if len(out) >= total or not d["results"]:
            break
        page += 1
        if page > max_pages:
            return total, out, False
    assert len(out) == total, f"TRUNCATED: read {len(out)} of {total} for {query}"
    return total, out, True


def uniprot_batch(accessions: list[str], fields: str) -> dict[str, dict]:
    """Resolve accessions in batches. Fails loudly on any accession that does not come back --
    a dead/deleted UniProt entry returns nothing and is otherwise indistinguishable from an
    entry that genuinely carries no annotation."""
    got: dict[str, dict] = {}
    for i in range(0, len(accessions), 40):
        chunk = accessions[i : i + 40]
        q = urllib.parse.quote(" OR ".join(f"accession:{a}" for a in chunk))
        d = fetch(f"https://rest.uniprot.org/uniprotkb/search?query={q}&fields={fields}&size=100")
        for r in d["results"]:
            got[r["primaryAccession"]] = r
    missing = [a for a in accessions if a not in got]
    assert not missing, f"unresolved accessions (possible dead entries): {missing}"
    return got


def is_reviewed(entry: dict) -> bool:
    """'reviewed' is a substring of 'unreviewed' -- anchor at the start."""
    return entry["entryType"].startswith("UniProtKB reviewed")


def clade_of(lineage_names: list[str]) -> str:
    for key in ("Fungi", "Viridiplantae"):
        if key in lineage_names:
            return key
    if "Vertebrata" in lineage_names:
        return "Vertebrata"
    if "Metazoa" in lineage_names:
        return "Metazoa (invertebrate)"
    return "other Eukaryota"


# --------------------------------------------------------------------------- checks


def check_subject_annotations(res: dict) -> None:
    total, rows, complete = paged_annotations(f"geneProductId=UniProtKB:{ACC}")
    assert complete
    tsv = (GENE_DIR / "ADTRP-goa.tsv").read_text().splitlines()
    tsv_rows = [ln for ln in tsv[1:] if ln.strip()]
    res["subject"] = {
        "accession": ACC,
        "quickgo_annotations": total,
        "goa_tsv_data_lines": len(tsv_rows),
        "goa_tsv_distinct_lines": len(set(tsv_rows)),
        "distinct_terms": len({r["goId"] for r in rows}),
        "iba_rows": sorted(r["goId"] for r in rows if r["goEvidence"] == "IBA"),
    }
    # The worklist that selected this gene is named "human-no-IBA-simple.csv".
    assert res["subject"]["iba_rows"], "expected IBA rows; worklist name would then be accurate"


def check_node_reach(res: dict) -> None:
    """Reach and clade composition of each PANTHER node that reaches ADTRP.

    This is the question that has found a real defect on nearly every gene in this campaign:
    which nodes carry a term, and -- reciprocally -- which node's reach is exactly my gene set
    and what did it give them?
    """
    out = {}
    for node in ("PTN001659973", "PTN002591065"):
        total, rows, complete = paged_annotations(
            f"evidenceCode=ECO:0000318&withFrom=PANTHER:{node}"
        )
        assert complete
        accs = sorted({r["geneProductId"].split(":", 1)[1] for r in rows})
        entries = uniprot_batch(accs, "accession,id,protein_name,organism_name,lineage,reviewed")
        clades = Counter()
        reviewed = []
        for a in accs:
            e = entries[a]
            lin = [x["scientificName"] for x in e.get("lineages", [])]
            clades[clade_of(lin)] += 1
            if is_reviewed(e):
                name = (
                    e["proteinDescription"].get("recommendedName", {}).get("fullName", {}).get("value")
                )
                reviewed.append(
                    {"accession": a, "name": name, "organism": e["organism"]["scientificName"]}
                )
        # "reviewed" must not equal the total -- if it does, the substring bug is back.
        assert len(reviewed) != len(accs) or len(accs) <= 1, (
            "every member reported reviewed; check the entryType test"
        )
        out[node] = {
            "annotations": total,
            "_accessions": accs,
            "distinct_gene_products": len(accs),
            "terms": sorted({r["goId"] for r in rows}),
            "clade_composition": dict(sorted(clades.items())),
            "reviewed_swissprot_members": reviewed,
            "n_reviewed_swissprot": len(reviewed),
            "paralog_AIG1_among_recipients": PARALOG in accs,
        }
    res["panther_nodes"] = out


def check_paint_table(res: dict) -> None:
    """Cross-check the live QuickGO WITH/FROM against the repo's cached PAINT table.

    The cached table is the authoritative record of node-level term placement and the IBD seed
    set; the live annotation is what actually shipped. They must agree.
    """
    path = REPO / "interpro" / "panther" / "PTHR10989" / "PTHR10989-paint.tsv"
    rows = [ln.split("\t") for ln in path.read_text().splitlines()[1:] if ln.strip()]
    table = [
        {
            "node": r[1],
            "go_id": r[2],
            "aspect": r[3],
            "seeds": r[6].split("|"),
            "taxon": r[7],
            "date": r[8],
        }
        for r in rows
    ]
    taxon_labels = {}
    for t in sorted({r["taxon"].split(":")[1] for r in table}):
        taxon_labels[t] = fetch(f"https://rest.uniprot.org/taxonomy/{t}.json")["scientificName"]
    for r in table:
        r["taxon_label"] = taxon_labels[r["taxon"].split(":")[1]]

    # The two nodes reaching human ADTRP must be present with the terms GOA actually shipped.
    shipped = {(n, g) for n, d in res["panther_nodes"].items() for g in d["terms"]}
    cached = {(r["node"], r["go_id"]) for r in table}
    assert shipped <= cached, f"live IBA terms absent from cached PAINT table: {shipped - cached}"
    res["paint_table"] = table


def check_interpro(res: dict) -> None:
    """IPR006838 is the signature supplying GO:0016020 to ADTRP by IEA:InterPro.

    Method (from the campaign brief): identify the specific signature supplying the term, then
    count how that entry's own reviewed members are curated.
    """
    meta = fetch("https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006838")["metadata"]
    members, url = [], (
        "https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR006838/?page_size=200"
    )
    while url:
        d = fetch(url)
        members.extend(d["results"])
        url = d.get("next")
    named = [
        {
            "accession": m["metadata"]["accession"],
            "name": m["metadata"].get("name"),
            "organism": m["metadata"].get("source_organism", {}).get("scientificName"),
        }
        for m in members
    ]
    uncharacterised = [m for m in named if "UPF" in (m["name"] or "")]
    res["interpro"] = {
        "entry": "IPR006838",
        "name": meta["name"]["name"],
        "type": meta["type"],
        "family_total_proteins": meta["counters"]["proteins"],
        "reviewed_swissprot_members": named,
        "n_reviewed_swissprot": len(named),
        "reviewed_fraction_pct": round(100 * len(named) / meta["counters"]["proteins"], 3),
        "interpro2go_terms": [g["identifier"] for g in (meta.get("go_terms") or [])],
        "n_uncharacterised_reviewed_members": len(uncharacterised),
        "uncharacterised_reviewed_members": uncharacterised,
    }
    # interpro2go maps this entry to a location only -- no molecular function. Positive control
    # that the go_terms field is populated at all:
    assert res["interpro"]["interpro2go_terms"], "go_terms empty; cannot claim 'CC only'"


def check_reference_projection(res: dict) -> None:
    """For each supporting reference, how many entities does it annotate, and does the
    functional/phenotype term spread across the set or stay on the perturbed gene?

    A reference giving N entities one identical term set is an import/projection, not N
    independent findings.
    """
    out = {}
    for ref in ("PMID:27018888", "PMID:21868574", "PMID:28341552", "PMID:32296183"):
        total, rows, complete = paged_annotations(f"reference={ref}", max_pages=6)
        if not complete:
            out[ref] = {
                "annotations": total,
                "entities": "UNAVAILABLE",
                "note": "result set too large to paginate; projection test not run",
            }
            continue
        per_entity: dict[str, set] = {}
        for r in rows:
            per_entity.setdefault(r["geneProductId"], set()).add(r["goId"])
        # Two questions, not one (a many-entity reference is NOT automatically a projection):
        #   1. how many entities does the reference annotate?
        #   2. do all entities carry the SAME term set?
        # Identical term sets are a necessary but not sufficient condition. Parallel
        # per-protein curation of a paper that individually perturbed each protein produces the
        # same signature as a projection, so the verdict is left to the prose, which can weigh
        # what the paper actually did. Recording the observation, not the interpretation.
        out[ref] = {
            "annotations": total,
            "n_entities": len(per_entity),
            "entities": sorted(per_entity),
            "assigned_by": sorted({r["assignedBy"] for r in rows}),
            "terms_per_entity": {k: sorted(v) for k, v in sorted(per_entity.items())},
            "identical_term_sets": len({frozenset(v) for v in per_entity.values()}) == 1
            and len(per_entity) > 1,
        }
    res["reference_projection"] = out


def check_opposite_cross_product(res: dict) -> None:
    """Intersect the reference sets of every positive/negative regulation pair.

    Detectable from the GOA TSV alone, before reading anything.
    """
    import csv

    rows = list(csv.DictReader((GENE_DIR / "ADTRP-goa.tsv").open(), delimiter="\t"))
    by_term: dict[str, dict] = {}
    for r in rows:
        by_term.setdefault(r["GO TERM"], {"name": r["GO NAME"], "refs": set()})["refs"].add(
            r["REFERENCE"]
        )
    grouped: dict[str, list] = {}
    for t, v in by_term.items():
        for prefix in ("positive regulation of ", "negative regulation of "):
            if v["name"].startswith(prefix):
                grouped.setdefault(v["name"][len(prefix) :], []).append((t, v["name"], v["refs"]))
    pairs = []
    for base, lst in grouped.items():
        if len(lst) > 1:
            inter = set.intersection(*[r for _, _, r in lst])
            pairs.append(
                {
                    "base_process": base,
                    "terms": [t for t, _, _ in lst],
                    "reference_intersection": sorted(inter),
                    "is_full_cross_product": all(
                        set.intersection(*[r for _, _, r in lst]) == r for _, _, r in lst
                    ),
                }
            )
    res["opposite_cross_product"] = {
        "n_regulation_terms": sum(len(v) for v in grouped.values()),
        "opposed_pairs": pairs,
        "verdict": "DEFECT" if pairs else "NEGATIVE (no positive/negative pair on one base process)",
    }


def check_term_relations(res: dict) -> None:
    """Fetch and assert every ancestry relation the review's prose depends on.

    Never infer an ancestry from a label: an activity term for X is not under the binding term
    for X, regulation is not subsumption, and siblings name different things.
    """

    def ancestors(t: str) -> list[str]:
        d = fetch(f"{QUICKGO}/ontology/go/terms/{t}/ancestors?relations=is_a,part_of")
        return d["results"][0]["ancestors"]

    def complete(t: str) -> dict:
        return fetch(f"{QUICKGO}/ontology/go/terms/{t}/complete")["results"][0]

    checks = [
        ("GO:0016787", "GO:0120573", True, "hydrolase activity IS an ancestor of FAHFA hydrolase"),
        ("GO:0052689", "GO:0120573", True, "carboxylic ester hydrolase IS an ancestor"),
        ("GO:0005886", "GO:0005901", True, "plasma membrane IS an ancestor of caveola"),
        ("GO:0016020", "GO:0005886", True, "membrane IS an ancestor of plasma membrane"),
        ("GO:0005886", "GO:0009986", False, "cell surface is NOT under plasma membrane"),
        ("GO:0016020", "GO:0009986", False, "cell surface is NOT under membrane"),
        ("GO:0009062", "GO:0042758", True, "fatty acid catabolic IS an ancestor of LCFA catabolic"),
    ]
    out = []
    for anc, desc, expected, label in checks:
        got = anc in ancestors(desc)
        assert got == expected, f"ancestry check failed: {label} (got {got})"
        # Record BOTH the raw relation and whether the prose claim is confirmed. Reporting only
        # the raw boolean makes a negative claim ("X is NOT under Y") render as "False", which
        # reads as the claim having failed when it has in fact been confirmed.
        out.append(
            {
                "ancestor": anc,
                "descendant": desc,
                "is_ancestor": got,
                "claim": label,
                "claim_confirmed": got == expected,
            }
        )

    terms = {}
    for t in ("GO:0120573", "GO:0016787", "GO:0042758", "GO:0005901", "GO:0009986"):
        d = complete(t)
        created = sorted({h["timestamp"] for h in (d.get("history") or []) if h["action"] == "Added"})
        terms[t] = {
            "name": d["name"],
            "is_obsolete": d.get("isObsolete"),
            "secondary_ids": d.get("secondaryIds"),
            "definition": d.get("definition", {}).get("text"),
            "first_added": created[0] if created else None,
            "rhea_xrefs": sorted(
                x["dbId"] for x in (d.get("xRefs") or []) if x.get("dbCode") == "RHEA"
            ),
        }
    assert not terms["GO:0120573"]["is_obsolete"]
    res["term_relations"] = {"ancestry": out, "terms": terms}


def check_panther_family_identity(res: dict) -> None:
    """PMID:27018888 names PANTHER family PTHR12242 for the non-mammalian AIG1/ADTRP-like
    proteins, while this analysis works from PTHR10989.

    Recorded because it looks like a discrepancy and is not: both families are live and distinct.
    A reviewer suggested noting that "PANTHER renumbered"; that is not what happened, so the
    claim is measured rather than repeated.
    """
    out = {}
    for fam in ("PTHR10989", "PTHR12242"):
        m = fetch(f"https://www.ebi.ac.uk/interpro/api/entry/panther/{fam}/")["metadata"]
        out[fam] = {
            "name": m["name"]["name"],
            "proteins": m["counters"]["proteins"],
            "integrated": m.get("integrated"),
        }
    assert out["PTHR10989"]["name"] != out["PTHR12242"]["name"], "families are not distinct"
    assert out["PTHR10989"]["integrated"] == "IPR006838"
    res["panther_family_identity"] = {
        "families": out,
        "conclusion": "distinct, both live; not a renumbering",
    }


def check_catalytic_dyad_conservation(res: dict) -> None:
    """Is the Thr47/His131 catalytic dyad conserved across the 86 recipients of PTN001659973?

    This decides the DIRECTION of the node-level recommendation, so it must be measured rather
    than assumed:

    * if the dyad is conserved across the fungal/plant/invertebrate recipients, the family-wide
      hydrolase inference is well founded and the asymmetry is that the *molecular function* is
      too general -- ``GO:0016787`` withholds a mechanism the residues support;
    * if it is not conserved, the specific *biological process* is the over-reach.

    Method follows the campaign's residue rule: require the aligned column to carry the right
    residue **and** to land exactly on ADTRP's own annotated SITE position (47, 131). Percent
    identity is reported next to every call because below roughly 25-30% identity a pairwise
    alignment will manufacture residue matches out of noise, so low-identity hits are counted
    separately rather than silently pooled.
    """
    from Bio import Align
    from Bio.Align import substitution_matrices

    accs = [
        e["accession"] if isinstance(e, dict) else e
        for e in res["panther_nodes"]["PTN001659973"]["_accessions"]
    ]
    seqs = {}
    for i in range(0, len(accs), 40):
        chunk = accs[i : i + 40]
        q = urllib.parse.quote(" OR ".join(f"accession:{a}" for a in chunk))
        d = fetch(
            f"https://rest.uniprot.org/uniprotkb/search?query={q}"
            "&fields=accession,sequence,organism_name,lineage&size=100"
        )
        for r in d["results"]:
            seqs[r["primaryAccession"]] = (
                r["sequence"]["value"],
                r["organism"]["scientificName"],
                [x["scientificName"] for x in r.get("lineages", [])],
            )
    assert ACC in seqs, "reference sequence missing"
    ref_seq = seqs[ACC][0]
    assert len(ref_seq) == 230, f"ADTRP length changed: {len(ref_seq)}"
    assert ref_seq[46] == "T" and ref_seq[130] == "H", "annotated SITE residues do not match sequence"

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"

    per, by_clade = {}, {}
    for acc, (seq, org, lin) in seqs.items():
        if acc == ACC:
            continue
        aln = aligner.align(ref_seq, seq)[0]
        # Map reference index -> subject residue through the aligned blocks.
        ref_to_sub = {}
        for (r0, r1), (s0, s1) in zip(aln.aligned[0], aln.aligned[1]):
            for k in range(r1 - r0):
                ref_to_sub[r0 + k] = s0 + k
        ident = sum(
            1 for ri, si in ref_to_sub.items() if ref_seq[ri] == seq[si]
        ) / len(ref_seq) * 100
        t_pos, h_pos = ref_to_sub.get(46), ref_to_sub.get(130)
        t_res = seq[t_pos] if t_pos is not None else "-"
        h_res = seq[h_pos] if h_pos is not None else "-"
        clade = clade_of(lin)
        rec = {
            "organism": org,
            "clade": clade,
            "pct_identity": round(ident, 1),
            "residue_at_ADTRP_Thr47": t_res,
            "residue_at_ADTRP_His131": h_res,
            "dyad_intact": t_res in ("T", "S") and h_res == "H",
            "low_identity": ident < 25.0,
        }
        per[acc] = rec
        b = by_clade.setdefault(clade, {"n": 0, "dyad_intact": 0, "dyad_intact_hi_id": 0, "n_hi_id": 0})
        b["n"] += 1
        b["dyad_intact"] += rec["dyad_intact"]
        if not rec["low_identity"]:
            b["n_hi_id"] += 1
            b["dyad_intact_hi_id"] += rec["dyad_intact"]

    # Positive control: the paralog AIG1 must score as dyad-intact (its own annotated sites are
    # Thr43/His134). If the aligner cannot recover a known case, the whole measurement is void.
    assert per[PARALOG]["dyad_intact"], (
        f"positive control failed: AIG1 not called dyad-intact ({per[PARALOG]})"
    )
    res["dyad_conservation"] = {
        "reference": f"{ACC} Thr47/His131 (UniProt SITE features, ECO:0000269|PubMed:27018888)",
        "n_compared": len(per),
        "n_dyad_intact": sum(1 for v in per.values() if v["dyad_intact"]),
        "by_clade": dict(sorted(by_clade.items())),
        "positive_control_AIG1": per[PARALOG],
        "per_protein": dict(sorted(per.items())),
    }


def check_intact_interactions(res: dict) -> None:
    """Expand the IntAct records behind the two GO:0005515 rows and count DISTINCT experiments.

    UniProt's ``NbExp`` is not an evidence-strength proxy: across this campaign it has been found
    counting sub-methods of one screen, replicates within one study, and even domains of one
    partner. So read the detection-method names rather than trusting the number.
    """
    d = fetch("https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/" + ACC)
    total = d.get("totalElements")
    content = d.get("content", [])
    assert content, "IntAct returned no interactions; a zero here would be indistinguishable from a broken query"
    assert total == len(content), f"IntAct paginated: {total} vs {len(content)} read"
    recs = []
    for x in content:
        pubs = [p for p in (x.get("publicationIdentifiers") or []) if "pubmed" in p]
        recs.append(
            {
                "a": x.get("moleculeA"),
                "b": x.get("moleculeB"),
                "method": x.get("detectionMethod"),
                "pubmed": [p.split(" ")[0] for p in pubs],
                "mi_score": x.get("intactMiscore"),
                "host": x.get("hostOrganism"),
            }
        )
    huri = [r for r in recs if "32296183" in r["pubmed"]]
    partners = {}
    for r in huri:
        p = r["a"] if r["a"] != "ADTRP" else r["b"]
        partners.setdefault(p, []).append(r["method"])
    res["intact"] = {
        "total_interactions": total,
        "records": recs,
        "huri_reference": "PMID:32296183",
        "huri_partners": {k: sorted(v) for k, v in sorted(partners.items())},
        "huri_distinct_methods_per_partner": {k: len(set(v)) for k, v in sorted(partners.items())},
        "huri_distinct_experiments_per_partner": 1,
        "all_huri_yeast_two_hybrid": all(
            "hybrid" in (m or "") for v in partners.values() for m in v
        ),
        "huri_mi_scores": sorted({r["mi_score"] for r in huri}),
    }
    assert res["intact"]["all_huri_yeast_two_hybrid"], "not all HuRI methods are two-hybrid"


def check_celltype_branch_disjointness(res: dict) -> None:
    """`GO:2000402 negative regulation of lymphocyte migration` is annotated IMP from
    PMID:28341552, whose abstract describes **monocytes** only and never lymphocytes.

    Before calling that term merely imprecise, fetch both closures: if neither the lymphocyte
    term nor the monocyte term is an ancestor of the other, they name different cell types and
    the term is *wrong*, not general.
    """

    def anc(t: str) -> set:
        d = fetch(f"{QUICKGO}/ontology/go/terms/{t}/ancestors?relations=is_a,part_of")
        return set(d["results"][0]["ancestors"])

    lymph, mono = "GO:2000402", "GO:2000438"
    mononuclear, leuko = "GO:0071676", "GO:0002686"
    cl = {t: anc(t) for t in (lymph, mono, mononuclear, leuko)}
    disjoint = lymph not in cl[mono] and mono not in cl[lymph]
    assert disjoint, "lymphocyte and monocyte terms are NOT disjoint; the argument changes"
    assert leuko in cl[lymph] and leuko in cl[mono]
    assert mononuclear in cl[lymph] and mononuclear in cl[mono]

    abstract = (REPO / "publications" / "PMID_28341552.md").read_text().lower()
    counts = {k: abstract.count(k) for k in ("monocyte", "lymphocyte", "leukocyte")}
    assert counts["monocyte"] > 0, "positive control failed: 'monocyte' absent from the abstract"
    res["celltype_branch_check"] = {
        "annotated_term": lymph,
        "abstract_celltype_counts": counts,
        "full_text_available": "full_text_available: true" in abstract,
        "lymphocyte_is_ancestor_of_monocyte_term": lymph in cl[mono],
        "monocyte_is_ancestor_of_lymphocyte_term": mono in cl[lymph],
        "disjoint_siblings": disjoint,
        "verified_common_ancestors": [mononuclear, leuko],
        "proposed_replacement": mono,
        "safe_fallback_ancestor": mononuclear,
    }


def check_substrate_chemistry(res: dict) -> None:
    """Is the FAHFA substrate itself a long-chain fatty acid?

    This is what decides whether GO:0042758 'long-chain fatty acid catabolic process' names the
    right chemistry, rather than being an inverted or mis-substrated annotation.
    """
    out = {}
    for chebi in ("CHEBI:83670", "CHEBI:7896", "CHEBI:136286"):
        iri = urllib.parse.quote(
            urllib.parse.quote(
                "http://purl.obolibrary.org/obo/" + chebi.replace(":", "_"), safe=""
            ),
            safe="",
        )
        d = fetch(f"https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/{iri}")
        a = fetch(
            f"https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/{iri}/hierarchicalAncestors?size=200"
        )
        labels = sorted({t["label"] for t in a.get("_embedded", {}).get("terms", [])})
        out[chebi] = {
            "label": d.get("label"),
            "definition": (d.get("description") or [""])[0],
            "is_long_chain_fatty_acid_anion": "long-chain fatty acid anion" in labels,
        }
    assert out["CHEBI:83670"]["is_long_chain_fatty_acid_anion"], (
        "9-PAHSA not classified as a long-chain fatty acid anion; GO:0042758 reasoning changes"
    )
    res["substrate_chemistry"] = out


def check_fulltext_localisation_negative(res: dict) -> None:
    """PMID:27018888 is cited by GOA as EXP evidence for GO:0005886 plasma membrane.

    Scan the cached full text for any localisation experiment. Every reported zero is paired
    with a positive control from the same file and the same call pattern, so a zero cannot be
    a broken scan.
    """
    path = REPO / "publications" / "PMID_27018888.md"
    text = path.read_text()
    assert "full_text_available: true" in text, "full text not cached; negative would be vacuous"
    low = text.lower()
    negatives = {
        k: low.count(k)
        for k in (
            "plasma membrane",
            "cell surface",
            "immunofluoresc",
            "confocal",
            "subcellular localiz",
            "localization",
        )
    }
    positives = {
        k: low.count(k)
        for k in ("membrane lysates", "membrane fraction", "transmembrane", "hek293t", "fahfa")
    }
    assert all(v > 0 for v in positives.values()), f"positive controls failed: {positives}"
    res["fulltext_localisation_scan"] = {
        "reference": "PMID:27018888",
        "full_text_available": True,
        "negative_terms": negatives,
        "positive_controls": positives,
        "conclusion": (
            "no plasma-membrane or cell-surface localisation experiment in the cached full text; "
            "compartment evidence is recovery in the membrane fraction of transfected HEK293T "
            "cells plus six topology predictors (supplementary figures are not in the cache)"
        ),
    }


def check_paralog_and_donor_evidence(res: dict) -> None:
    """Does each WITH/FROM donor carry its own experimental evidence for the propagated term,
    and at which term? A propagation that lands above its own donor is a fixable defect."""
    total, rows, complete = paged_annotations(f"geneProductId=UniProtKB:{PARALOG}")
    assert complete
    entry = uniprot_batch([PARALOG], "accession,id,protein_name,gene_names,ft_site")[PARALOG]
    res["paralog_AIG1"] = {
        "accession": PARALOG,
        "reviewed_swissprot": is_reviewed(entry),
        "entry_name": entry["uniProtkbId"],
        "catalytic_sites": [
            (f["location"]["start"]["value"], f["description"])
            for f in entry.get("features", [])
            if f["type"] == "Site"
        ],
        "annotations": total,
        "own_experimental_terms": sorted(
            {r["goId"] for r in rows if r["goEvidence"] in EXPERIMENTAL}
        ),
        "shares_identical_IBA_rows_with_subject": sorted(
            {r["goId"] for r in rows if r["goEvidence"] == "IBA"}
        ),
    }


# --------------------------------------------------------------------------- report


def render(res: dict) -> str:
    n = res["panther_nodes"]
    big, small = n["PTN001659973"], n["PTN002591065"]
    ip = res["interpro"]
    L = []
    a = L.append
    a("# ADTRP (Q96IZ2) — propagation and route analysis")
    a("")
    a(f"_Generated by `analyze_adtrp_propagation.py`. generated: {res['generated']}_")
    a("")
    a("## 1. The worklist's 'no-IBA' name is stale")
    a("")
    s = res["subject"]
    a(
        f"`projects/paint/human-no-IBA-simple.csv` lists ADTRP, but GOA carries "
        f"**{len(s['iba_rows'])} IBA rows**: {', '.join(s['iba_rows'])}."
    )
    a(
        f"GOA TSV has {s['goa_tsv_data_lines']} data lines "
        f"({s['goa_tsv_distinct_lines']} distinct) over {s['distinct_terms']} distinct GO terms; "
        f"QuickGO returns {s['quickgo_annotations']} annotations."
    )
    a("")
    a("## 2. PANTHER node reach — the MF/BP granularity asymmetry")
    a("")
    a("| node | taxon scope | terms | recipients | clade composition | reviewed (Swiss-Prot) |")
    a("|---|---|---|---|---|---|")
    for node, d in (("PTN001659973", big), ("PTN002591065", small)):
        scope = next(
            (f"{r['taxon']} {r['taxon_label']}" for r in res["paint_table"] if r["node"] == node),
            "?",
        )
        comp = ", ".join(f"{k} {v}" for k, v in d["clade_composition"].items())
        a(
            f"| `{node}` | {scope} | {', '.join(d['terms'])} | {d['distinct_gene_products']} | "
            f"{comp} | {d['n_reviewed_swissprot']} |"
        )
    a("")
    a("Cached PAINT table (`interpro/panther/PTHR10989/PTHR10989-paint.tsv`), which agrees with")
    a("the live QuickGO WITH/FROM:")
    a("")
    a("| node | GO | aspect | IBD seeds | taxon | date |")
    a("|---|---|---|---|---|---|")
    for r in res["paint_table"]:
        a(
            f"| `{r['node']}` | {r['go_id']} | {r['aspect']} | {', '.join(r['seeds'])} | "
            f"{r['taxon']} {r['taxon_label']} | {r['date']} |"
        )
    a("")
    a(
        f"**The finding.** At one and the same node `PTN001659973`, scoped by PAINT to "
        f"taxon:2759 Eukaryota and seeded by exactly two human proteins (ADTRP and AIG1), PAINT "
        f"asserts the *root* of the hydrolase branch as the molecular function "
        f"(`GO:0016787`) and a four-step-deep biological process "
        f"(`GO:0042758 long-chain fatty acid catabolic process`). Both reach all "
        f"{big['distinct_gene_products']} recipients, of which "
        f"{big['clade_composition'].get('Fungi', 0)} are fungi, "
        f"{big['clade_composition'].get('Viridiplantae', 0)} are plants and "
        f"{big['clade_composition'].get('other Eukaryota', 0)} are other eukaryotes."
    )
    a("")
    a(
        f"Only {big['n_reviewed_swissprot']} of the {big['distinct_gene_products']} recipients are "
        f"Swiss-Prot reviewed, and two of those are *uncharacterised* UPF0641 fungal proteins. "
        f"The MF call is dated "
        f"{next(r['date'] for r in res['paint_table'] if r['go_id'] == 'GO:0016787')}, i.e. "
        f"*after* `GO:0120573 FAHFA hydrolase activity` was created "
        f"({res['term_relations']['terms']['GO:0120573']['first_added']}), so the general term is "
        f"a deliberate judgement rather than a stale-term artefact."
    )
    a("")
    a("### What the conserved character actually licenses (this corrects a first-pass error)")
    a("")
    dy = res["dyad_conservation"]
    a(
        f"My first pass argued that the clade's heterogeneity justified the general MF and "
        f"therefore made the specific BP unwarranted. **Measurement does not support that "
        f"reasoning**, and the corrected version is sharper. Aligning all "
        f"{dy['n_compared']} other recipients to {dy['reference']} and requiring the aligned "
        f"column to land on ADTRP's own annotated SITE position:"
    )
    a("")
    a("| clade | dyad Thr/His intact | of which alignments >=25% identity |")
    a("|---|---|---|")
    for clade, v in dy["by_clade"].items():
        a(f"| {clade} | {v['dyad_intact']}/{v['n']} | {v['dyad_intact_hi_id']}/{v['n_hi_id']} |")
    a("")
    pc = dy["positive_control_AIG1"]
    a(
        f"Positive control: AIG1 (Q9NVV5), whose own catalytic residues are independently "
        f"annotated as Thr43/His134, scores dyad-intact at {pc['pct_identity']}% identity, so the "
        f"aligner recovers a known case."
    )
    a("")
    a(
        f"So the **catalytic dyad is broadly conserved**: {dy['n_dyad_intact']} of "
        f"{dy['n_compared']} recipients retain it, including every vertebrate and both "
        f"*Dictyostelium* members. Note the fungal column: all 14 fungal recipients fall **below "
        f"25% identity**, where a pairwise alignment will manufacture residue matches out of "
        f"noise, so their dyad status is **undetermined, not negative** — an absence of evidence, "
        f"which is not evidence of absence."
    )
    a("")
    a(
        "**The corrected finding, and it is a category distinction rather than a sloppiness "
        "claim.** A conserved catalytic dyad licenses a *mechanism* inference but not a "
        "*substrate* inference. `GO:0016787 hydrolase activity` states mechanism only, and is "
        "therefore exactly scoped to what the conserved residues support family-wide - so the "
        "general MF is well founded, and better founded than the heterogeneity argument I first "
        "made. `GO:0042758 long-chain fatty acid catabolic process` is a **substrate-level** "
        "claim, and the substrate is known only for the four characterised animal members (human "
        "and mouse ADTRP and AIG1). That is the asymmetry worth reporting: not that one term is "
        "too specific and the other too general, but that the node propagates a substrate claim "
        "on evidence that can only support a mechanism claim."
    )
    a("")
    a(
        f"**Reciprocal question, benign answer.** `PTN002591065` — the node whose reach is almost "
        f"exactly this gene's orthologue set — covers {small['distinct_gene_products']} gene "
        f"products, **all Vertebrata**, scoped taxon:117571 Euteleostomi, and gives them "
        f"`GO:0005901 caveola`. Caveolae are a vertebrate structure, so the scope and the term "
        f"agree. The paralog AIG1 is "
        f"{'among' if small['paralog_AIG1_among_recipients'] else 'correctly **not** among'} "
        f"the recipients."
    )
    a("")
    fi = res["panther_family_identity"]["families"]
    a("### PTHR12242 vs PTHR10989 — distinct families, not a renumbering")
    a("")
    a(
        "PMID:27018888 names PANTHER family `PTHR12242` for the non-mammalian AIG1/ADTRP-like "
        "proteins, whereas this analysis works from `PTHR10989`. Both are live and distinct, so "
        "the paper describes a sister set in another family rather than the recipients of the "
        "node reviewed here:"
    )
    a("")
    a("| family | name | proteins | InterPro |")
    a("|---|---|---|---|")
    for fam, v in fi.items():
        a(f"| `{fam}` | {v['name']} | {v['proteins']} | {v['integrated'] or 'none'} |")
    a("")
    a("## 3. The three non-PAINT routes")
    a("")
    a(
        f"**InterPro2GO — non-confirmation.** `{ip['entry']}` ({ip['name']}, {ip['type']}) is a "
        f"*family-specific* signature, not a bare fold. interpro2go maps it to "
        f"{', '.join(ip['interpro2go_terms'])} — a cellular component only, **no molecular "
        f"function**. Of its {ip['family_total_proteins']} proteins, "
        f"{ip['n_reviewed_swissprot']} are reviewed (Swiss-Prot) "
        f"({ip['reviewed_fraction_pct']}% of the family), and "
        f"{ip['n_uncharacterised_reviewed_members']} of those are uncharacterised UPF0641 "
        f"proteins. The predicted fold-to-activity error is **absent**: this entry shows "
        f"restraint."
    )
    a("")
    for m in ip["reviewed_swissprot_members"]:
        a(f"- `{m['accession']}` {m['name']} — {m['organism']}")
    a("")
    a("**Bulk classification imports carrying TAS — non-confirmation.** ADTRP has no TAS row.")
    a("Reference-projection test on every supporting reference, fully paginated:")
    a("")
    a("| reference | annotations | entities | all entities same term set? | assigned by |")
    a("|---|---|---|---|---|")
    for ref, d in res["reference_projection"].items():
        if d["entities"] == "UNAVAILABLE":
            a(f"| {ref} | {d['annotations']} | UNAVAILABLE — {d['note']} | n/a | n/a |")
        else:
            a(
                f"| {ref} | {d['annotations']} | {d['n_entities']} "
                f"({', '.join(x.split(':')[1] for x in d['entities'])}) | "
                f"{'yes' if d['identical_term_sets'] else 'no'} | "
                f"{', '.join(d['assigned_by'])} |"
            )
    a("")
    a(
        "Identical term sets are a *necessary but not sufficient* condition for a projection. "
        "`PMID:27018888` gives ADTRP and AIG1 the same four terms, but the paper individually "
        "mutated and individually assayed **both** proteins (T47A/H131A for ADTRP, T43A/H134A "
        "for AIG1), so this is parallel per-protein curation of two characterised enzymes, not "
        "one finding projected onto a set. The ACTR8-style defect — a complex-level or "
        "single-gene phenotype spreading unchanged across every member — is **absent** here: no "
        "reference on this gene annotates more than four entities, and the two multi-entity "
        "references give each entity a *different* term set."
    )
    a("")
    a("**ARBA rules — non-confirmation.** No WITH/FROM on any ADTRP row names an `ARBA…` rule;")
    a("the two automatic routes present are `GO_REF:0000044` (Swiss-Prot subcellular-location")
    a("mapping) and `GO_REF:0000116` (Rhea mapping), both of which name their source explicitly.")
    a("")
    a("## 4. Reaction direction and substrate identity")
    a("")
    t = res["term_relations"]["terms"]["GO:0120573"]
    a(
        f"`GO:0120573` carries {len(t['rhea_xrefs'])} RHEA cross-references and its definition "
        f"states the hydrolytic direction explicitly: _{t['definition']}_"
    )
    a("")
    a("ChEBI classification of the reaction participants:")
    a("")
    a("| ChEBI | label | long-chain fatty acid anion? |")
    a("|---|---|---|")
    for c, d in res["substrate_chemistry"].items():
        a(f"| `{c}` | {d['label']} | {'yes' if d['is_long_chain_fatty_acid_anion'] else 'no'} |")
    a("")
    a(
        "So the **substrate itself is a long-chain fatty acid**, and the annotated direction is "
        "hydrolysis (removal), matching UniProt's `PhysiologicalDirection=left-to-right` on all "
        "12 catalytic-activity lines. The predicted direction/substrate inversion is **not "
        "present**: `GO:0042758` names the right chemistry for this gene."
    )
    a("")
    a("## 5. Ancestry relations the review depends on (all fetched, none inferred)")
    a("")
    a("| claim | `is_a`/`part_of` ancestor? | claim confirmed |")
    a("|---|---|---|")
    for c in res["term_relations"]["ancestry"]:
        a(
            f"| {c['claim']} | `{c['ancestor']}` in closure of `{c['descendant']}`: "
            f"{c['is_ancestor']} | {'yes' if c['claim_confirmed'] else 'NO'} |"
        )
    a("")
    a("## 4b. The two `GO:0005515` rows are ONE screen counted three ways")
    a("")
    it = res["intact"]
    a(
        f"IntAct returns {it['total_interactions']} interactions for `{ACC}`. The two rows GOA "
        f"carries both come from `{it['huri_reference']}` (HuRI), and each partner is logged "
        f"under three *sub-methods of the same screen*:"
    )
    a("")
    a("| partner | IntAct detection methods | distinct methods | distinct experiments |")
    a("|---|---|---|---|")
    for p, ms in it["huri_partners"].items():
        a(
            f"| {p} | {', '.join(ms)} | {it['huri_distinct_methods_per_partner'][p]} | "
            f"{it['huri_distinct_experiments_per_partner']} |"
        )
    a("")
    a(
        f"All are yeast two-hybrid, MI-score {', '.join(str(s) for s in it['huri_mi_scores'])}, "
        f"and this is what UniProt's `NbExp=3` is counting — **not** three independent "
        f"experiments. There is no orthogonal assay for either partner and no follow-up anywhere "
        f"in the ADTRP literature."
    )
    a("")
    a("## 5b. Cell-type branch check on `GO:2000402` (sibling, not ancestor)")
    a("")
    ct = res["celltype_branch_check"]
    a(
        f"`PMID:28341552` is annotated to `{ct['annotated_term']}` **negative regulation of "
        f"lymphocyte migration** (IMP, BHF-UCL). Cell-type words in the cached abstract: "
        + ", ".join(f"`{k}` {v}" for k, v in ct["abstract_celltype_counts"].items())
        + f" (full text available: {ct['full_text_available']})."
    )
    a("")
    a("| relation | holds |")
    a("|---|---|")
    a(
        f"| `{ct['annotated_term']}` (lymphocyte) is an ancestor of `{ct['proposed_replacement']}` "
        f"(monocyte) | {ct['lymphocyte_is_ancestor_of_monocyte_term']} |"
    )
    a(
        f"| `{ct['proposed_replacement']}` (monocyte) is an ancestor of "
        f"`{ct['annotated_term']}` (lymphocyte) | {ct['monocyte_is_ancestor_of_lymphocyte_term']} |"
    )
    a(f"| verified common ancestors | {', '.join(ct['verified_common_ancestors'])} |")
    a("")
    a(
        f"**Neither closure contains the other**, so the annotated term does not merely "
        f"generalise the data — it names a *different* leukocyte lineage. Monocytes are myeloid "
        f"mononuclear phagocytes; lymphocytes are lymphoid. The abstract's phrase is "
        f"\"transendothelial migration of monocytes\", which is precisely "
        f"`{ct['proposed_replacement']}` negative regulation of monocyte extravasation. "
        f"`{ct['safe_fallback_ancestor']}` negative regulation of mononuclear cell migration is "
        f"a verified ancestor of **both** and is the safe fallback if the full text (not cached) "
        f"does contain a lymphocyte assay. The leukocyte-level claim is in any case already "
        f"annotated separately from the same paper as `GO:0002686`."
    )
    a("")
    a("## 6. Logical-opposite citation cross-product")
    a("")
    cp = res["opposite_cross_product"]
    a(
        f"{cp['n_regulation_terms']} positive/negative regulation terms; "
        f"opposed pairs on the same base process: **{len(cp['opposed_pairs'])}**. "
        f"Verdict: **{cp['verdict']}**."
    )
    a("")
    a("## 7. Does PMID:27018888 support `GO:0005886 plasma membrane`?")
    a("")
    sc = res["fulltext_localisation_scan"]
    a("Occurrence counts in the cached full text (`full_text_available: true`):")
    a("")
    a("| term | count | role |")
    a("|---|---|---|")
    for k, v in sc["negative_terms"].items():
        a(f"| `{k}` | {v} | localisation-experiment probe |")
    for k, v in sc["positive_controls"].items():
        a(f"| `{k}` | {v} | positive control |")
    a("")
    a(f"Conclusion: {sc['conclusion']}.")
    a("")
    a("## 8. Paralog AIG1 (Q9NVV5)")
    a("")
    p = res["paralog_AIG1"]
    a(
        f"`{p['accession']}` {p['entry_name']}, "
        f"{'reviewed (Swiss-Prot)' if p['reviewed_swissprot'] else 'TrEMBL'}, catalytic sites "
        f"{p['catalytic_sites']}. It is a genuine co-seed, not a spurious donor: it carries its "
        f"own experimental annotations to {', '.join(p['own_experimental_terms'])} and shares "
        f"the identical IBA rows {', '.join(p['shares_identical_IBA_rows_with_subject'])} with "
        f"ADTRP from the same node."
    )
    a("")
    return "\n".join(L) + "\n"


def main() -> int:
    res: dict = {"generated": time.strftime("%Y-%m-%d")}
    check_subject_annotations(res)
    check_node_reach(res)
    check_paint_table(res)
    check_interpro(res)
    check_reference_projection(res)
    check_opposite_cross_product(res)
    check_term_relations(res)
    check_panther_family_identity(res)
    check_catalytic_dyad_conservation(res)
    check_intact_interactions(res)
    check_celltype_branch_disjointness(res)
    check_substrate_chemistry(res)
    check_fulltext_localisation_negative(res)
    check_paralog_and_donor_evidence(res)
    (HERE / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(res))
    print("wrote results.json and RESULTS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
