# /// script
# requires-python = ">=3.11"
# dependencies = ["requests"]
# ///
"""Download every input used by the GNRHR variant-structure analysis.

Nothing is hardcoded except identifiers (UniProt accession, gene symbol). Each
source is written to data/ with a retrieval manifest (data/manifest.json) so
the downstream scripts are reproducible offline. A source that cannot be
reached is recorded as failed in the manifest; downstream scripts report it as
missing rather than substituting anything.
"""
import datetime
import json
import pathlib
import re
import sys
import time

import requests

ACC = "P30968"
GENE = "GNRHR"
DATA = pathlib.Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)
S = requests.Session()
S.headers["User-Agent"] = "gnrhr-variant-analysis/1.0 (python-requests)"
manifest = {"retrieved": datetime.date.today().isoformat(), "sources": {}}


def get(name, url, fname, **kw):
    for attempt in range(4):
        try:
            r = S.request(kw.pop("method", "GET"), url, timeout=120, **kw)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            r.raise_for_status()
            (DATA / fname).write_bytes(r.content)
            manifest["sources"][name] = {"url": url, "file": fname, "bytes": len(r.content), "ok": True}
            print(f"ok   {name}: {len(r.content)} bytes")
            return r
        except Exception as e:  # noqa: BLE001
            err = str(e)
            time.sleep(3)
    manifest["sources"][name] = {"url": url, "file": fname, "ok": False, "error": err}
    print(f"FAIL {name}: {err}", file=sys.stderr)
    return None


# 1. Canonical sequence and features
get("uniprot_fasta", f"https://rest.uniprot.org/uniprotkb/{ACC}.fasta", "P30968.fasta")
get("uniprot_json", f"https://rest.uniprot.org/uniprotkb/{ACC}.json", "P30968.json")
# 2. GPCRdb generic (Ballesteros-Weinstein) residue numbers
get("gpcrdb_residues", "https://gpcrdb.org/services/residues/gnrhr_human/", "gpcrdb_residues.json")
# 3. Structures: which PDB entries contain a GnRH receptor chain?
orth = {"human": "P30968", "pig": "P49922", "mouse": "Q01776", "rat": "P30969"}
q = {
    "query": {"type": "terminal", "service": "text", "parameters": {
        "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession",
        "operator": "in", "value": list(orth.values())}},
    "return_type": "entry", "request_options": {"paginate": {"start": 0, "rows": 100}},
}
r = get("rcsb_search", "https://search.rcsb.org/rcsbsearch/v2/query", "rcsb_search.json", method="POST", json=q)
pdb_ids = sorted({x["identifier"] for x in r.json().get("result_set", [])}) if r is not None else []
# the 2025 cryo-EM paper (PMID:40523184) deposited GnRH-GnRHR-Gq complexes; pick them up by title search too
q2 = {"query": {"type": "terminal", "service": "full_text", "parameters": {"value": "gonadotropin-releasing hormone receptor"}},
      "return_type": "entry", "request_options": {"paginate": {"start": 0, "rows": 150}}}
r2 = get("rcsb_search_text", "https://search.rcsb.org/rcsbsearch/v2/query", "rcsb_search_text.json", method="POST", json=q2)
cand = sorted({x["identifier"] for x in r2.json().get("result_set", [])}) if (r2 is not None and r2.content) else []
titles = {}
for pid in sorted(set(pdb_ids) | set(cand)):
    rr = S.get(f"https://data.rcsb.org/rest/v1/core/entry/{pid}", timeout=60)
    if rr.ok and "struct" in rr.json():
        j = rr.json()
        titles[pid] = {"title": j["struct"]["title"], "method": (j.get("exptl") or [{}])[0].get("method"),
                       "resolution": (j.get("rcsb_entry_info", {}).get("resolution_combined") or [None])[0],
                       "pmid": j.get("rcsb_primary_citation", {}).get("pdbx_database_id_pub_med")}
    time.sleep(0.2)
# keep receptor structures only (the text search also returns free GnRH peptides, antibodies, etc.)
keep = {p: t for p, t in titles.items()
        if p in pdb_ids or re.search(r"gnrh ?1?r|gonadotropin-releasing hormone receptor", t["title"], re.I)}
(DATA / "structures.json").write_text(json.dumps(keep, indent=1))
print("GnRH receptor structures:", json.dumps(keep, indent=1))
for pid in keep:
    get(f"pdb_{pid}", f"https://files.rcsb.org/download/{pid}.cif", f"{pid}.cif")
    get(f"sifts_{pid}", f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pid.lower()}", f"sifts_{pid}.json")
# 4. AlphaFold model
r = get("alphafold_meta", f"https://alphafold.ebi.ac.uk/api/prediction/{ACC}", "alphafold_meta.json")
if r is not None:
    m = r.json()[0]
    get("alphafold_model", m["cifUrl"], "AF-P30968.cif")
# 5. Orthologue sequences for conservation (reviewed GnRH receptors, UniProt)
get("orthologs", "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
    "(protein_name:%22gonadotropin-releasing%20hormone%20receptor%22)%20AND%20(reviewed:true)", "gnrhr_reviewed.fasta")
# 6. ClinVar: all GNRHR records
r = get("clinvar_search", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar"
        f"&term={GENE}[gene]&retmode=json&retmax=2000", "clinvar_ids.json")
if r is not None:
    ids = r.json()["esearchresult"]["idlist"]
    out = {}
    for i in range(0, len(ids), 150):
        for attempt in range(6):
            time.sleep(3 * (attempt + 1))
            rr = S.post("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
                        data={"db": "clinvar", "retmode": "json", "id": ",".join(ids[i:i + 150])}, timeout=120)
            if rr.status_code != 429:
                break
        rr.raise_for_status()
        res = rr.json()["result"]
        for u in res["uids"]:
            out[u] = res[u]
    (DATA / "clinvar_summaries.json").write_text(json.dumps(out))
    manifest["sources"]["clinvar_summaries"] = {"file": "clinvar_summaries.json", "n": len(out), "ok": True}
    print("ok   clinvar summaries:", len(out))
# 7. gnomAD v4: variants and constraint
gq = """query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){
 gene_id canonical_transcript_id
 gnomad_constraint{pLI oe_lof oe_lof_lower oe_lof_upper oe_mis oe_mis_lower oe_mis_upper mis_z lof_z exp_lof obs_lof exp_mis obs_mis}
 variants(dataset:gnomad_r4){variant_id hgvsp hgvsc consequence transcript_id lof rsids
   exome{ac an homozygote_count} genome{ac an homozygote_count}}}}"""
get("gnomad", "https://gnomad.broadinstitute.org/api", "gnomad.json", method="POST",
    json={"query": gq, "variables": {"g": GENE}})
# 8. EBI Proteins API variation (UniProt + large-scale sources, protein coordinates)
get("ebi_variation", f"https://www.ebi.ac.uk/proteins/api/variation/{ACC}", "ebi_variation.json",
    headers={"Accept": "application/json"})
(DATA / "manifest.json").write_text(json.dumps(manifest, indent=1))
