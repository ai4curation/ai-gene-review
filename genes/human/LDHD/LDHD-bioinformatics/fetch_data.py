"""Download every external input used by the LDHD analysis into data/ (git-ignored).

Sources: UniProt REST (sequences, isoforms, orthologs), RCSB PDB (mouse LDHD crystal
structures, PDB 8JD*), AlphaFold DB (human model), NCBI ClinVar (E-utilities) and
gnomAD v4 (GraphQL API). Nothing is hard-coded except identifiers; re-running
refreshes the snapshot and records retrieval metadata in data/manifest.json.
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys
import time

import requests

HERE = pathlib.Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)

HUMAN = "Q86WU2"
MOUSE = "Q7TNG8"
# Orthologs / family members used for conservation. Accessions are looked up in
# UniProt at run time (sequence and description come from the service).
ORTHOLOGS = {
    "human": "Q86WU2",
    "mouse": "Q7TNG8",
    "zebrafish": "F1QXM5",
    "yeast_DLD1": "P32891",
    "arabidopsis_DLD": "Q94AX4",
}
ORTHOLOG_QUERIES = {
    # reviewed or unreviewed LDHD orthologs found by gene name + taxon
    "rat": "gene_exact:Ldhd AND organism_id:10116",
    "bovine": "gene_exact:LDHD AND organism_id:9913",
    "chicken": "gene_exact:LDHD AND organism_id:9031",
    "xenopus_tropicalis": "gene_exact:ldhd AND organism_id:8364",
}
S = requests.Session()
S.headers["User-Agent"] = "ldhd-analysis-script"


def get(url, tries=5, **kw):
    for i in range(tries):
        r = S.get(url, timeout=60, **kw)
        if r.status_code == 200:
            return r
        time.sleep(2 + 2 * i)
    r.raise_for_status()
    return r


def main() -> None:
    manifest = {"retrieved": dt.datetime.now(dt.timezone.utc).isoformat(), "files": {}}

    # --- UniProt sequences -------------------------------------------------
    r = get(f"https://rest.uniprot.org/uniprotkb/search?query=accession:{HUMAN}&format=fasta&includeIsoform=true")
    (DATA / "human_isoforms.fasta").write_text(r.text)
    r = get(f"https://rest.uniprot.org/uniprotkb/{HUMAN}.json")
    (DATA / "Q86WU2.json").write_text(r.text)
    r = get(f"https://rest.uniprot.org/uniprotkb/{MOUSE}.json")
    (DATA / "Q7TNG8.json").write_text(r.text)
    seqs = []
    resolved = dict(ORTHOLOGS)
    for name, q in ORTHOLOG_QUERIES.items():
        r = get("https://rest.uniprot.org/uniprotkb/search", params={"query": q, "fields": "accession,reviewed,length,protein_name", "format": "json", "size": 10})
        hits = r.json().get("results", [])
        if not hits:
            print(f"no UniProt hit for {name}: {q}", file=sys.stderr)
            continue
        # prefer reviewed, then longest
        hits.sort(key=lambda h: (h["entryType"].startswith("UniProtKB reviewed"), h["sequence"]["length"]), reverse=True)
        resolved[name] = hits[0]["primaryAccession"]
    for name, acc in resolved.items():
        r = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
        seqs.append(r.text.replace(">", f">{name}|", 1))
    (DATA / "orthologs.fasta").write_text("".join(seqs))
    manifest["orthologs"] = resolved

    # --- RefSeq transcripts (both coding transcripts; NM_194436 is MANE Select) ---
    for nm in ("NM_153486", "NM_194436"):
        time.sleep(1)
        r = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", params={"db": "nuccore", "id": nm, "rettype": "gb", "retmode": "text"})
        (DATA / f"{nm}.gb").write_text(r.text)

    # --- PDB: all entries cross-referenced from mouse LDHD -----------------
    mouse = json.loads((DATA / "Q7TNG8.json").read_text())
    pdb_ids = sorted(x["id"] for x in mouse["uniProtKBCrossReferences"] if x["database"] == "PDB")
    entries = []
    for pid in pdb_ids:
        e = get(f"https://data.rcsb.org/rest/v1/core/entry/{pid}").json()
        entries.append({
            "pdb_id": pid,
            "title": e["struct"]["title"],
            "resolution": (e["rcsb_entry_info"].get("resolution_combined") or [None])[0],
            "ligands": e["rcsb_entry_info"].get("nonpolymer_bound_components"),
            "method": e["exptl"][0]["method"],
            "assemblies": e["rcsb_entry_container_identifiers"].get("assembly_ids"),
        })
        cif = DATA / f"{pid}.cif"
        if not cif.exists():
            cif.write_bytes(get(f"https://files.rcsb.org/download/{pid}.cif").content)
    (DATA / "pdb_entries.json").write_text(json.dumps(entries, indent=1))

    # --- AlphaFold human model ---------------------------------------------
    af = get(f"https://alphafold.ebi.ac.uk/api/prediction/{HUMAN}").json()[0]
    (DATA / "alphafold_meta.json").write_text(json.dumps(af, indent=1))
    (DATA / "AF-Q86WU2.cif").write_bytes(get(af["cifUrl"]).content)
    if af.get("amAnnotationsUrl"):
        (DATA / "alphamissense.csv").write_bytes(get(af["amAnnotationsUrl"]).content)

    # --- MitoCarta3.0 (Broad Institute) ---
    mc = DATA / "Human.MitoCarta3.0.xls"
    if not mc.exists():
        mc.write_bytes(get("https://personal.broadinstitute.org/scalvo/MitoCarta3.0/Human.MitoCarta3.0.xls").content)

    # --- ClinVar -----------------------------------------------------------
    eut = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    ids = get(f"{eut}/esearch.fcgi", params={"db": "clinvar", "term": "LDHD[gene]", "retmax": 2000, "retmode": "json"}).json()["esearchresult"]["idlist"]
    recs = {}
    for i in range(0, len(ids), 100):
        time.sleep(1.5)
        j = get(f"{eut}/esummary.fcgi", params={"db": "clinvar", "id": ",".join(ids[i:i + 100]), "retmode": "json"}).json()["result"]
        for u in j["uids"]:
            recs[u] = j[u]
    (DATA / "clinvar_esummary.json").write_text(json.dumps(recs, indent=1))

    # --- gnomAD v4 ----------------------------------------------------------
    q = """{gene(gene_symbol:"LDHD",reference_genome:GRCh38){gene_id chrom start stop
      canonical_transcript_id mane_select_transcript{ensembl_id refseq_id}
      gnomad_constraint{pLI oe_lof oe_lof_lower oe_lof_upper oe_mis oe_mis_lower oe_mis_upper mis_z exp_lof obs_lof exp_mis obs_mis}
      variants(dataset:gnomad_r4){variant_id rsids consequence hgvsc hgvsp lof lof_filter lof_flags transcript_id flags
        exome{ac an homozygote_count filters} genome{ac an homozygote_count filters}}}}"""
    r = S.post("https://gnomad.broadinstitute.org/api", json={"query": q}, timeout=120)
    r.raise_for_status()
    (DATA / "gnomad_r4.json").write_text(json.dumps(r.json(), indent=1))

    manifest["pdb_ids"] = pdb_ids
    manifest["clinvar_records"] = len(recs)
    manifest["alphafold_version"] = af.get("latestVersion")
    (DATA / "manifest.json").write_text(json.dumps(manifest, indent=1))
    print(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
