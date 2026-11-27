# /// script
# requires-python = ">=3.11"
# dependencies = ["requests==2.32.5"]
# ///
"""Fetch every raw input for the KRT9 analysis.

Small inputs go to data/ (committed); structure coordinate files go to cache/ (git-ignored).
Existing files are reused unless --refresh is given, so a rerun analyses the same snapshot.
Every request is recorded in data/manifest.json (URL, retrieval time, release headers).

Usage: uv run 00_fetch.py [--refresh] [--accession P35527] [--gene KRT9]
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import time

import requests

from common import CACHE, DATA, dump_json, gene_name, http_json, load_json, protein_name

UNIPROT = "https://rest.uniprot.org/uniprotkb"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
GNOMAD = "https://gnomad.broadinstitute.org/api"
GNOMAD_DATASET = "gnomad_r4"
GNOMAD_REFERENCE = "GRCh38"
KEEP_FEATURES = {"Region", "Domain", "Natural variant", "Mutagenesis", "Sequence conflict",
                 "Compositional bias", "Modified residue", "Site", "Motif"}

MANIFEST: dict = {}
S = requests.Session()
S.headers["User-Agent"] = "krt9-bioinformatics-analysis/0.1 (python-requests)"


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def note(key: str, url: str, resp=None, **extra) -> None:
    rec = {"url": url, "retrieved_utc": now(), **extra}
    if resp is not None:
        for h in ("X-UniProt-Release", "X-UniProt-Release-Date", "Last-Modified"):
            if h in resp.headers:
                rec[h] = resp.headers[h]
        rec["http_status"] = resp.status_code
    MANIFEST[key] = rec


def slim(entry: dict) -> dict:
    """Keep only the UniProt fields the analysis reads (keeps data/ small)."""
    return {
        "primaryAccession": entry["primaryAccession"],
        "uniProtkbId": entry.get("uniProtkbId"),
        "entryType": entry.get("entryType"),
        "organism": {k: entry["organism"].get(k) for k in ("scientificName", "commonName", "taxonId")},
        "genes": entry.get("genes", [])[:1],
        "proteinDescription": {k: v for k, v in entry["proteinDescription"].items()
                               if k in ("recommendedName", "submissionNames")},
        "sequence": {k: entry["sequence"][k] for k in ("value", "length", "crc64")},
        "entryAudit": entry.get("entryAudit"),
        "features": [f for f in entry.get("features", []) if f["type"] in KEEP_FEATURES],
        "pdb_xrefs": [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "PDB"],
        "xref_databases": sorted({x["database"] for x in entry.get("uniProtKBCrossReferences", [])}),
    }


def fetch_uniprot_entry(acc: str) -> None:
    url = f"{UNIPROT}/{acc}.json"
    data, r = http_json(S, url)
    dump_json(slim(data), DATA / f"uniprot_{acc}.json")
    note(f"uniprot_{acc}", url, r, sequence_version=data["entryAudit"]["sequenceVersion"],
         entry_version=data["entryAudit"]["entryVersion"])


def fetch_human_keratins() -> None:
    q = ('(organism_id:9606) AND (reviewed:true) AND (family:"intermediate filament family") '
         'AND (protein_name:keratin)')
    params = {"query": q, "format": "json", "size": 500}
    data, r = http_json(S, f"{UNIPROT}/search", params=params)
    out = []
    for e in data["results"]:
        name = protein_name(e)
        m = re.match(r"Keratin, type (I|II) ", name)
        if not m:
            continue
        s = slim(e)
        s["keratin_type"] = m.group(1)
        out.append(s)
    out.sort(key=lambda e: e["primaryAccession"])
    dump_json(out, DATA / "human_keratins.json")
    note("human_keratins", r.url, r, n_returned=len(data["results"]), n_kept=len(out), query=q,
         filter="recommended name matches '^Keratin, type (I|II) '")


def fetch_human_if_family() -> None:
    """All reviewed human intermediate filament family proteins (used only to find structures)."""
    q = '(organism_id:9606) AND (reviewed:true) AND (family:"intermediate filament family")'
    data, r = http_json(S, f"{UNIPROT}/search", params={"query": q, "format": "json", "size": 500})
    out = []
    for e in data["results"]:
        s = slim(e)
        s["features"] = [f for f in s["features"] if f["type"] == "Region"]
        out.append(s)
    out.sort(key=lambda e: e["primaryAccession"])
    dump_json(out, DATA / "human_if_family.json")
    note("human_if_family", r.url, r, n_returned=len(out), query=q)


def fetch_orthologs(acc: str) -> None:
    url = "https://pantherdb.org/services/oai/pantherdb/ortholog/matchortho"
    params = {"geneInputList": acc, "organism": 9606, "orthologType": "LDO"}
    data, r = http_json(S, url, params=params)
    mapped = data["search"]["mapping"]["mapped"]
    if isinstance(mapped, dict):
        mapped = [mapped]
    rows = []
    for m in mapped:
        tg = m["target_gene"]
        macc = re.search(r"UniProtKB=([A-Z0-9]+)", tg)
        rows.append({"target_gene": tg, "species": tg.split("|")[0], "ortholog_type": m["ortholog"],
                     "target_symbol": m.get("target_gene_symbol", ""),
                     "target_ptn": m.get("target_persistent_id", ""),
                     "accession": macc.group(1) if macc else ""})
    accs = sorted({x["accession"] for x in rows if x["accession"]})
    seqs = {}
    for i in range(0, len(accs), 50):
        chunk = accs[i:i + 50]
        q = " OR ".join(f"accession:{a}" for a in chunk)
        d, _ = http_json(S, f"{UNIPROT}/search", params={"query": q, "format": "json", "size": 100})
        for e in d["results"]:
            if "sequence" not in e or "organism" not in e:  # inactive/obsolete accession
                continue
            seqs[e["primaryAccession"]] = slim(e)
            for sec in e.get("secondaryAccessions", []):
                seqs.setdefault(sec, slim(e))
        time.sleep(0.5)
    dump_json({"panther_version": data["search"]["product"].get("version"),
               "orthologs": rows, "entries": {a: seqs[a] for a in accs if a in seqs},
               "unresolved_accessions": [a for a in accs if a not in seqs]},
              DATA / "panther_orthologs.json")
    note("panther_orthologs", r.url, r, panther_version=data["search"]["product"].get("version"),
         n_orthologs=len(rows))


def fetch_clinvar(gene: str) -> None:
    term = f"{gene}[gene]"
    d, r = http_json(S, f"{EUTILS}/esearch.fcgi",
                     params={"db": "clinvar", "term": term, "retmax": 10000, "retmode": "json"}, pause=2)
    ids = d["esearchresult"]["idlist"]
    count = int(d["esearchresult"]["count"])
    recs = []
    for i in range(0, len(ids), 100):
        time.sleep(1.5)
        chunk = ids[i:i + 100]
        s, _ = http_json(S, f"{EUTILS}/esummary.fcgi",
                         params={"db": "clinvar", "id": ",".join(chunk), "retmode": "json"}, pause=3)
        for uid in s["result"]["uids"]:
            x = s["result"][uid]
            g = x.get("germline_classification", {})
            vs = x.get("variation_set", [])
            loc38 = [l for v in vs for l in v.get("variation_loc", []) if l.get("assembly_name") == "GRCh38"]
            recs.append({
                "uid": uid, "accession": x.get("accession_version"), "title": x.get("title"),
                "obj_type": x.get("obj_type"),
                "protein_change": x.get("protein_change"),
                "molecular_consequences": x.get("molecular_consequence_list", []),
                "genes": [gg["symbol"] for gg in x.get("genes", [])],
                "germline_classification": g.get("description"),
                "review_status": g.get("review_status"),
                "last_evaluated": g.get("last_evaluated"),
                "conditions": [t.get("trait_name") for t in g.get("trait_set", [])],
                "cdna_change": [v.get("cdna_change") for v in vs],
                "canonical_spdi": [v.get("canonical_spdi") for v in vs],
                "aliases": [a for v in vs for a in v.get("aliases", [])],
                "grch38": [{"chr": l["chr"], "start": l["start"], "stop": l["stop"]} for l in loc38],
                "dbsnp": [xr["db_id"] for v in vs for xr in v.get("variation_xrefs", [])
                          if xr.get("db_source") == "dbSNP"],
            })
    dump_json({"term": term, "esearch_count": count, "records": recs}, DATA / f"clinvar_{gene}.json")
    note(f"clinvar_{gene}", r.url, r, esearch_count=count, n_records=len(recs))


def fetch_gnomad(gene: str) -> None:
    q = """query($g:String!){ meta{ clinvar_release_date }
      gene(gene_symbol:$g, reference_genome:%s){
        gene_id symbol chrom start stop strand canonical_transcript_id
        mane_select_transcript{ ensembl_id ensembl_version refseq_id refseq_version }
        gnomad_constraint{ pLI oe_lof oe_lof_lower oe_lof_upper oe_mis oe_mis_lower oe_mis_upper
          oe_syn oe_syn_lower oe_syn_upper mis_z lof_z syn_z exp_lof obs_lof exp_mis obs_mis exp_syn obs_syn flags }
        variants(dataset:%s){ variant_id pos rsids transcript_id hgvsc hgvsp consequence
          lof lof_filter lof_flags flags
          exome{ ac an af homozygote_count hemizygote_count filters }
          genome{ ac an af homozygote_count hemizygote_count filters } } } }""" % (GNOMAD_REFERENCE, GNOMAD_DATASET)
    d, r = http_json(S, GNOMAD, json_body={"query": q, "variables": {"g": gene}}, pause=5)
    if d.get("errors"):
        raise RuntimeError(f"gnomAD errors: {d['errors']}")
    g = d["data"]["gene"]
    allv = g.pop("variants")
    coding = [v for v in allv if v.get("hgvsp") or v.get("lof") or
              v["consequence"] in ("splice_donor_variant", "splice_acceptor_variant", "start_lost", "stop_lost")]
    counts: dict = {}
    for v in allv:
        counts[v["consequence"]] = counts.get(v["consequence"], 0) + 1
    dump_json({"dataset": GNOMAD_DATASET, "reference_genome": GNOMAD_REFERENCE, "meta": d["data"].get("meta"),
               "gene": g, "n_variants_all_consequences": len(allv), "consequence_counts": counts,
               "variants": coding}, DATA / f"gnomad_{gene}.json")
    note(f"gnomad_{gene}", GNOMAD, r, dataset=GNOMAD_DATASET, n_variants=len(allv), n_kept=len(coding),
         kept="variants with a protein HGVS, a LOFTEE call, or an essential-splice/start/stop-lost consequence")


def fetch_interpro(acc: str) -> None:
    url = f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}"
    d, r = http_json(S, url, params={"page_size": 100})
    rows = []
    for x in d["results"]:
        m = x["metadata"]
        for p in x["proteins"]:
            for loc in p["entry_protein_locations"]:
                for f in loc["fragments"]:
                    rows.append({"accession": m["accession"], "database": m["source_database"],
                                 "name": m["name"], "start": f["start"], "end": f["end"]})
    rows.sort(key=lambda x: (x["database"], x["accession"], x["start"]))
    dump_json(rows, DATA / f"interpro_{acc}.json")
    note(f"interpro_{acc}", r.url, r, n_matches=len(rows))


def fetch_alphafold(acc: str) -> None:
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{acc}"
    d, r = http_json(S, url)
    keep = [{k: m.get(k) for k in ("modelEntityId", "toolUsed", "latestVersion", "modelCreatedDate",
                                   "sequenceVersionDate", "globalMetricValue", "uniprotStart", "uniprotEnd",
                                   "sequence", "cifUrl", "pdbUrl", "isReferenceProteome", "isReviewed")}
            for m in d]
    dump_json(keep, DATA / f"alphafold_{acc}.json")
    note(f"alphafold_{acc}", url, r, n_models=len(keep))
    CACHE.mkdir(exist_ok=True)
    for m in keep:
        rr = S.get(m["cifUrl"], timeout=120)
        rr.raise_for_status()
        (CACHE / f"{m['modelEntityId']}.cif").write_bytes(rr.content)
        note(f"alphafold_model_{m['modelEntityId']}", m["cifUrl"], rr, bytes=len(rr.content))


def rcsb_search_by_uniprot(accs: list[str]) -> list[str]:
    body = {"query": {"type": "group", "logical_operator": "and", "nodes": [
        {"type": "terminal", "service": "text", "parameters": {
            "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession",
            "operator": "in", "value": accs}},
        {"type": "terminal", "service": "text", "parameters": {
            "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name",
            "operator": "exact_match", "value": "UniProt"}}]},
        "return_type": "entry", "request_options": {"paginate": {"start": 0, "rows": 1000}}}
    r = S.post("https://search.rcsb.org/rcsbsearch/v2/query", json=body, timeout=120)
    if r.status_code == 204:  # RCSB: no hits
        return []
    r.raise_for_status()
    return sorted(x["identifier"] for x in r.json()["result_set"])


def fetch_structures(acc: str) -> None:
    kers = load_json(DATA / "human_if_family.json")
    all_accs = [k["primaryAccession"] for k in kers]
    own = rcsb_search_by_uniprot([acc])
    pdbe, rp = http_json(S, f"https://www.ebi.ac.uk/pdbe/api/mappings/best_structures/{acc}", ok404=True)
    target = load_json(DATA / f"uniprot_{acc}.json")
    dump_json({"accession": acc, "rcsb_entries_for_accession": own,
               "pdbe_best_structures_http_status": rp.status_code,
               "pdbe_best_structures": (pdbe or {}).get(acc, []),
               "uniprot_pdb_xrefs": target["pdb_xrefs"],
               "uniprot_has_alphafolddb_xref": "AlphaFoldDB" in target["xref_databases"]},
              DATA / f"experimental_structure_check_{acc}.json")
    note("experimental_structure_check", "search.rcsb.org + www.ebi.ac.uk/pdbe/api/mappings/best_structures", rp)

    ids = rcsb_search_by_uniprot(all_accs)
    q = """query($ids:[String!]!){ entries(entry_ids:$ids){ rcsb_id struct{title} exptl{method}
      rcsb_entry_info{resolution_combined deposited_polymer_monomer_count}
      rcsb_accession_info{initial_release_date}
      rcsb_primary_citation{pdbx_database_id_PubMed title year}
      polymer_entities{ rcsb_id entity_poly{pdbx_seq_one_letter_code_can}
        rcsb_polymer_entity{pdbx_description}
        rcsb_polymer_entity_container_identifiers{auth_asym_ids asym_ids uniprot_ids}
        rcsb_polymer_entity_align{reference_database_name reference_database_accession
          aligned_regions{entity_beg_seq_id ref_beg_seq_id length}}
        rcsb_entity_source_organism{ncbi_scientific_name} } } }"""
    d, r = http_json(S, "https://data.rcsb.org/graphql", json_body={"query": q, "variables": {"ids": ids}})
    entries = d["data"]["entries"]
    dump_json({"searched_uniprot_accessions": all_accs, "entry_ids": ids, "entries": entries},
              DATA / "rcsb_if_entries.json")
    note("rcsb_if_entries", "https://search.rcsb.org/rcsbsearch/v2/query + https://data.rcsb.org/graphql", r,
         n_entries=len(ids))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accession", default="P35527")
    ap.add_argument("--gene", default="KRT9")
    ap.add_argument("--refresh", action="store_true", help="refetch even if data/ already has the file")
    a = ap.parse_args()
    DATA.mkdir(exist_ok=True)
    mpath = DATA / "manifest.json"
    if mpath.exists():
        MANIFEST.update(load_json(mpath))
    steps = [
        (DATA / f"uniprot_{a.accession}.json", lambda: fetch_uniprot_entry(a.accession)),
        (DATA / "human_keratins.json", fetch_human_keratins),
        (DATA / "human_if_family.json", fetch_human_if_family),
        (DATA / "panther_orthologs.json", lambda: fetch_orthologs(a.accession)),
        (DATA / f"clinvar_{a.gene}.json", lambda: fetch_clinvar(a.gene)),
        (DATA / f"gnomad_{a.gene}.json", lambda: fetch_gnomad(a.gene)),
        (DATA / f"interpro_{a.accession}.json", lambda: fetch_interpro(a.accession)),
        (DATA / f"alphafold_{a.accession}.json", lambda: fetch_alphafold(a.accession)),
        (DATA / "rcsb_if_entries.json", lambda: fetch_structures(a.accession)),
    ]
    for path, fn in steps:
        if path.exists() and not a.refresh:
            print(f"reuse  {path.name}")
            continue
        print(f"fetch  {path.name}")
        fn()
        dump_json(MANIFEST, mpath)
    # coordinate files are never committed: make sure the cache is populated even when data/ is reused
    CACHE.mkdir(exist_ok=True)
    for m in load_json(DATA / f"alphafold_{a.accession}.json"):
        dest = CACHE / f"{m['modelEntityId']}.cif"
        if not dest.exists():
            rr = S.get(m["cifUrl"], timeout=120)
            rr.raise_for_status()
            dest.write_bytes(rr.content)
    for ent in load_json(DATA / "rcsb_if_entries.json")["entries"]:
        if not ent.get("exptl") or ent["exptl"][0]["method"] != "X-RAY DIFFRACTION":
            continue  # only crystal structures are analysed
        pid = ent["rcsb_id"]
        dest = CACHE / f"{pid}.cif"
        if not dest.exists():
            rr = S.get(f"https://files.rcsb.org/download/{pid}.cif", timeout=300)
            rr.raise_for_status()
            dest.write_bytes(rr.content)
    dump_json(MANIFEST, mpath)
    print("done")


if __name__ == "__main__":
    main()
