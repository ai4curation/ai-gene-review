"""Refresh the cached donor-side facts used by the homology-propagation browser.

For every ISO/ISS/ISA/Compara row in the cached GOA files this resolves the
WITH/FROM donors (UniProt REST) and asks QuickGO which evidence codes the donor
currently carries for the transferred term. It also caches GO ancestor
closures (is_a + part_of) restricted to the terms that occur in propagated or
IBA rows, so builders can test IBA/ISO entailment offline.

Outputs (under ``projects/HOMOLOGY_PROPAGATION/data/`` by default):

* ``donor-entities.tsv``   donor xref -> accession, symbol, taxon
* ``donor-annotations.tsv`` (accession, GO term) -> current evidence codes
* ``term-ancestors.tsv``    term -> ancestors (restricted to corpus terms)
* ``refresh-metadata.json`` date and sources of the refresh

Existing cache rows are reused; pass ``--force`` to refetch everything. Only
facts returned by the services are written; an unresolved donor is simply
absent, and the builders report it as "not checked".
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import time
from typing import Any, Iterable, Optional
import urllib.error
import urllib.parse
import urllib.request

from ai_gene_review.export.propagation_rows import (
    DONOR_EVIDENCE,
    EXPERIMENTAL,
    iter_propagated_rows,
    iter_target_evidence,
    uniprot_base,
)

UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO_SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
RGD_GENE = "https://rest.rgd.mcw.edu/rgdws/genes/"
RGD_SPECIES = "https://rest.rgd.mcw.edu/rgdws/lookup/speciesTypeKeys"

#: Scientific names for RGD's common species names (RGD hosts several mammals,
#: so an RGD id is not necessarily rat).
RGD_SCIENTIFIC = {
    "Human": "Homo sapiens", "Mouse": "Mus musculus", "Rat": "Rattus norvegicus",
    "Chinchilla": "Chinchilla lanigera", "Bonobo": "Pan paniscus",
    "Dog": "Canis lupus familiaris", "Squirrel": "Ictidomys tridecemlineatus",
    "Pig": "Sus scrofa", "Green Monkey": "Chlorocebus sabaeus",
    "Naked Mole-Rat": "Heterocephalus glaber", "Black Rat": "Rattus rattus",
}
GO_JSON = "http://purl.obolibrary.org/obo/go/go-basic.json"
DEFAULT_DATA_DIR = Path("projects/HOMOLOGY_PROPAGATION/data")

#: UniProt cross-reference database names for MOD-prefixed donors.
XREF_DB = {"MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "FB": "flybase",
           "PomBase": "pombase", "WB": "wormbase", "ZFIN": "zfin",
           "TAIR": "araport", "dictyBase": "dictybase", "HGNC": "hgnc"}

ENTITY_FIELDS = ["xref", "accession", "symbol", "taxon_id", "organism", "reviewed"]
ANNOT_FIELDS = ["accession", "term_id", "evidence_codes", "assigned_by", "references"]


def _get(url: str, params: dict[str, Any], accept: str = "application/json",
         retries: int = 4) -> str:
    query = urllib.parse.urlencode(params, safe=":,")
    full = f"{url}?{query}" if query else url
    request = urllib.request.Request(full, headers={
        "Accept": accept, "User-Agent": "ai-gene-review (github.com/ai4curation/ai-gene-review)"})
    delay = 2.0
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            if exc.code < 500 or attempt == retries:
                raise
            time.sleep(delay)
            delay *= 2
        except OSError:
            if attempt == retries:
                raise
            time.sleep(delay)
            delay *= 2
    raise RuntimeError("unreachable")


def _read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t",
                                lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _uniprot_tsv(query: str) -> list[dict[str, str]]:
    text = _get(UNIPROT_SEARCH, {
        "query": query,
        "fields": "accession,gene_primary,organism_id,organism_name,reviewed,"
                  "xref_mgi,xref_rgd,xref_sgd,xref_flybase,xref_pombase,"
                  "xref_wormbase,xref_zfin,xref_hgnc",
        "format": "tsv", "size": 500,
    }, accept="text/plain")
    return list(csv.DictReader(text.splitlines(), delimiter="\t"))


def resolve_uniprot(accessions: list[str]) -> dict[str, dict[str, str]]:
    """Resolve UniProt accessions (batched) to symbol and taxon."""
    out: dict[str, dict[str, str]] = {}
    for i in range(0, len(accessions), 100):
        chunk = accessions[i:i + 100]
        query = " OR ".join(f"accession:{acc}" for acc in chunk)
        for rec in _uniprot_tsv(query):
            out[rec["Entry"]] = {
                "accession": rec["Entry"],
                "symbol": rec.get("Gene Names (primary)", ""),
                "taxon_id": rec.get("Organism (ID)", ""),
                "organism": rec.get("Organism", ""),
                "reviewed": "true" if rec.get("Reviewed") == "reviewed" else "false",
            }
    return out


def resolve_mod(xref: str) -> Optional[dict[str, str]]:
    """Resolve a MOD donor id to its UniProt entry, preferring Swiss-Prot."""
    prefix, local = xref.split(":", 1)
    db = XREF_DB.get(prefix)
    if not db:
        return None
    records = _uniprot_tsv(f'xref:"{db}-{local}"')
    column = {"mgi": "MGI", "rgd": "RGD", "sgd": "SGD", "flybase": "FlyBase",
              "pombase": "PomBase", "wormbase": "WormBase", "zfin": "ZFIN",
              "hgnc": "HGNC"}.get(db, "")
    exact = []
    for rec in records:
        values = [v.strip() for v in (rec.get(column) or "").split(";") if v.strip()]
        # A UniProt entry shared by several loci (e.g. identical calmodulins)
        # lists all of them; only an entry naming this locus alone is exact.
        if local in values or xref in values:
            exact.append((len(values), rec))
    if not exact:
        return None
    exact.sort(key=lambda pair: (pair[1].get("Reviewed") != "reviewed", pair[0]))
    rec = exact[0][1]
    return {
        "accession": rec["Entry"],
        "symbol": rec.get("Gene Names (primary)", ""),
        "taxon_id": rec.get("Organism (ID)", ""),
        "organism": rec.get("Organism", ""),
        "reviewed": "true" if rec.get("Reviewed") == "reviewed" else "false",
    }


def resolve_rgd(xrefs: list[str]) -> dict[str, dict[str, str]]:
    """Resolve RGD gene ids (any RGD species) with RGD's own REST API.

    Used for donors UniProt does not cross-reference, typically non-rat
    mammals behind GO_REF:0000121. No UniProt accession is recorded, so the
    donor's current annotations are not checked.
    """
    if not xrefs:
        return {}
    keys = json.loads(_get(RGD_SPECIES, {}))
    species = {v: RGD_SCIENTIFIC.get(k, k) for k, v in keys.items()}
    out = {}
    for xref in xrefs:
        gene = json.loads(_get(RGD_GENE + xref.split(":", 1)[1], {}))
        out[xref] = {"accession": "", "symbol": gene.get("symbol", ""),
                     "taxon_id": "", "reviewed": "",
                     "organism": species.get(gene.get("speciesTypeKey"), "")}
    return out


def donor_annotations(accession: str, terms: list[str]) -> list[dict[str, str]]:
    """Return the donor's current exact annotations to the given terms."""
    rows: dict[str, dict[str, set[str]]] = {}
    for i in range(0, len(terms), 50):
        page = 1
        while True:
            data = json.loads(_get(QUICKGO_SEARCH, {
                "geneProductId": f"UniProtKB:{accession}",
                "goId": ",".join(terms[i:i + 50]),
                "goUsage": "exact", "limit": 200, "page": page,
            }))
            for rec in data.get("results", []):
                if (rec.get("qualifier") or "").startswith("NOT"):
                    continue
                slot = rows.setdefault(rec["goId"], {"ev": set(), "by": set(), "ref": set()})
                slot["ev"].add(rec.get("goEvidence") or "")
                slot["by"].add(rec.get("assignedBy") or "")
                slot["ref"].add(rec.get("reference") or "")
            pages = (data.get("pageInfo") or {}).get("total", 1)
            if page >= pages:
                break
            page += 1
    return [{
        "accession": accession, "term_id": term,
        "evidence_codes": ",".join(sorted(v["ev"] - {""})),
        "assigned_by": ",".join(sorted(v["by"] - {""})),
        "references": ",".join(sorted(v["ref"] - {""})[:10]),
    } for term, v in sorted(rows.items())]


def term_ancestors(go_json: Path, terms: set[str]) -> dict[str, list[str]]:
    """Ancestor closure over is_a/part_of, restricted to ``terms``."""
    graph = json.loads(go_json.read_text())["graphs"][0]
    parents: dict[str, set[str]] = {}
    for edge in graph.get("edges", []):
        if edge["pred"] not in {"is_a", "http://purl.obolibrary.org/obo/BFO_0000050"}:
            continue
        sub = edge["sub"].rsplit("/", 1)[-1].replace("_", ":")
        obj = edge["obj"].rsplit("/", 1)[-1].replace("_", ":")
        if sub.startswith("GO:") and obj.startswith("GO:"):
            parents.setdefault(sub, set()).add(obj)
    out: dict[str, list[str]] = {}
    for term in sorted(terms):
        seen: set[str] = set()
        stack = list(parents.get(term, ()))
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(parents.get(node, ()))
        kept = sorted((seen & terms) - {term})
        if kept:
            out[term] = kept
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--genes-dir", type=Path, default=Path("genes"))
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--go-json", type=Path,
                        help="Local go-basic.json (downloaded if omitted)")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-annotations", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    rows = list(iter_propagated_rows(args.genes_dir))
    donor_rows = [r for r in rows if r.evidence in DONOR_EVIDENCE
                  or r.method_class == "ELECTRONIC_ORTHOLOGY"]

    # --- donor entities ---------------------------------------------------
    entity_path = args.data_dir / "donor-entities.tsv"
    entities = {} if args.force else {r["xref"]: r for r in _read_tsv(entity_path)}
    xrefs = sorted({d for r in donor_rows for d in r.donors} - set(entities))
    accs = sorted({a for x in xrefs if (a := uniprot_base(x))})
    resolved = resolve_uniprot(accs)
    def mod(xref: str) -> tuple[str, Optional[dict[str, str]]]:
        try:
            return xref, resolve_mod(xref)
        except Exception as exc:  # network failure: leave unresolved
            print(f"warn: {xref}: {exc}")
            return xref, None

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        mods = dict(pool.map(mod, [x for x in xrefs if not uniprot_base(x)]))
    mods.update(resolve_rgd([x for x in xrefs if x.startswith("RGD:") and not mods.get(x)]))
    for xref in xrefs:
        acc = uniprot_base(xref)
        info = resolved.get(acc) if acc else mods.get(xref)
        if info:
            entities[xref] = {"xref": xref, **info}
    _write_tsv(entity_path, ENTITY_FIELDS, sorted(entities.values(), key=lambda r: r["xref"]))
    print(f"donor entities: {len(entities)} resolved of "
          f"{len({d for r in donor_rows for d in r.donors})}")

    # --- donor annotations ------------------------------------------------
    annot_path = args.data_dir / "donor-annotations.tsv"
    if not args.skip_annotations:
        wanted: dict[str, set[str]] = {}
        for r in donor_rows:
            for d in r.donors:
                if entities.get(d, {}).get("accession"):
                    wanted.setdefault(entities[d]["accession"], set()).add(r.term_id)
        existing = [] if args.force else _read_tsv(annot_path)
        checked_path = args.data_dir / "donor-annotations-checked.tsv"
        checked = set() if args.force else {
            (r["accession"], r["term_id"]) for r in _read_tsv(checked_path)}
        todo = {acc: sorted(t for t in terms if (acc, t) not in checked)
                for acc, terms in wanted.items()}
        todo = {acc: terms for acc, terms in todo.items() if terms}
        print(f"querying QuickGO for {len(todo)} donors")

        def fetch(item: tuple[str, list[str]]) -> tuple[str, list[str], list[dict[str, str]]]:
            acc, terms = item
            try:
                return acc, terms, donor_annotations(acc, terms)
            except Exception as exc:
                print(f"warn: QuickGO {acc}: {exc}")
                return acc, [], []

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            results = list(pool.map(fetch, sorted(todo.items())))
        found = {(r["accession"], r["term_id"]): r for r in existing}
        for acc, terms, annots in results:
            for annot in annots:
                found[(annot["accession"], annot["term_id"])] = annot
            checked.update((acc, t) for t in terms)
        _write_tsv(annot_path, ANNOT_FIELDS, [found[k] for k in sorted(found)])
        _write_tsv(checked_path, ["accession", "term_id"],
                   [{"accession": a, "term_id": t} for a, t in sorted(checked)])

    # --- GO ancestors -----------------------------------------------------
    go_json = args.go_json
    if go_json is None:
        go_json = args.data_dir / ".go-basic.json"
        if not go_json.exists() or args.force:
            urllib.request.urlretrieve(GO_JSON, go_json)
    corpus_terms = {r.term_id for r in rows}
    corpus_terms |= {t for _, _, t, ev in iter_target_evidence(args.genes_dir)
                     if ev in {"IBA", "ISO"} | EXPERIMENTAL}
    ancestors = term_ancestors(go_json, corpus_terms)
    _write_tsv(args.data_dir / "term-ancestors.tsv", ["term_id", "ancestors"],
               [{"term_id": t, "ancestors": " ".join(a)} for t, a in sorted(ancestors.items())])
    go_version = json.loads(go_json.read_text())["graphs"][0].get("meta", {}).get("version", "")

    (args.data_dir / "refresh-metadata.json").write_text(json.dumps({
        "refreshed": datetime.date.today().isoformat(),
        "uniprot": UNIPROT_SEARCH,
        "quickgo": QUICKGO_SEARCH,
        "go_version": go_version,
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
