"""Download every input the analysis uses. Nothing is hardcoded about results.

Usage: fetch_data.py --accession O94903 --gene PLPBP --family-csv <entries.csv>
                     --templates 1CT5 1W8G --outdir data
"""
import argparse
import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path


def get(url: str, data: bytes | None = None, headers: dict | None = None, tries: int = 4) -> bytes:
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=headers or {})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception as e:  # network retry only
            if i == tries - 1:
                raise
            print(f"retry {url}: {e}")
            time.sleep(3 * (i + 1))
    raise RuntimeError(url)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accession", required=True)
    ap.add_argument("--gene", required=True)
    ap.add_argument("--family-csv", required=True)
    ap.add_argument("--extra-accessions", nargs="*", default=[])
    ap.add_argument("--templates", nargs="*", default=[])
    ap.add_argument("--refseq-mrna", help="RefSeq transcript whose CDS is used to check c. numbering")
    ap.add_argument("--outdir", default="data")
    a = ap.parse_args()
    out = Path(a.outdir)
    out.mkdir(exist_ok=True)

    accs = [r["id"] for r in csv.DictReader(open(a.family_csv))]
    for x in [a.accession, *a.extra_accessions]:
        if x not in accs:
            accs.append(x)
    fa = []
    for i in range(0, len(accs), 25):
        q = "+OR+".join(f"accession:{x}" for x in accs[i:i + 25])
        fa.append(get(f"https://rest.uniprot.org/uniprotkb/search?query={q}&format=fasta&size=500").decode())
    (out / "family.fasta").write_text("".join(fa))
    (out / f"{a.accession}.fasta").write_bytes(get(f"https://rest.uniprot.org/uniprotkb/{a.accession}.fasta"))

    meta = json.loads(get(f"https://alphafold.ebi.ac.uk/api/prediction/{a.accession}"))[0]
    (out / "alphafold_meta.json").write_text(json.dumps(meta, indent=1))
    (out / f"AF-{a.accession}.pdb").write_bytes(get(meta["pdbUrl"]))

    (out / "pdbe_best_structures.json").write_bytes(
        get_or_empty(f"https://www.ebi.ac.uk/pdbe/api/mappings/best_structures/{a.accession}"))
    for t in a.templates:
        (out / f"{t}.pdb").write_bytes(get(f"https://files.rcsb.org/download/{t}.pdb"))

    # ClinVar
    term = urllib.parse.quote(f"{a.gene}[gene]")
    ids = json.loads(get(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term={term}&retmax=2000&retmode=json"
    ))["esearchresult"]["idlist"]
    recs = {}
    for i in range(0, len(ids), 100):
        time.sleep(0.5)
        r = json.loads(get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&retmode=json&id="
            + ",".join(ids[i:i + 100])))["result"]
        for k in r.get("uids", []):
            recs[k] = r[k]
    slim = {}
    for k, r in recs.items():
        vs = (r.get("variation_set") or [{}])[0]
        g = r.get("germline_classification", {})
        slim[k] = {"accession": r.get("accession"), "title": r.get("title"), "obj_type": r.get("obj_type"),
                   "cdna_change": vs.get("cdna_change"), "protein_change": r.get("protein_change"),
                   "canonical_spdi": vs.get("canonical_spdi"),
                   "molecular_consequence": r.get("molecular_consequence_list"),
                   "classification": g.get("description"), "review_status": g.get("review_status"),
                   "last_evaluated": g.get("last_evaluated"),
                   "traits": sorted({t.get("trait_name", "") for t in g.get("trait_set", [])}),
                   "genes": [x.get("symbol") for x in r.get("genes", [])]}
    (out / "clinvar.json").write_text(json.dumps(slim, indent=1))
    if a.refseq_mrna:
        time.sleep(1)
        (out / "cds.fasta").write_bytes(get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta_cds_na&retmode=text&id="
            + a.refseq_mrna))

    # gnomAD v4 variants + constraint
    q = """{gene(gene_symbol:"%s",reference_genome:GRCh38){gene_id canonical_transcript_id
      gnomad_constraint{pLI oe_lof oe_lof_lower oe_lof_upper oe_mis oe_mis_lower oe_mis_upper mis_z exp_lof obs_lof exp_mis obs_mis}
      variants(dataset:gnomad_r4){variant_id rsids hgvsc hgvsp consequence transcript_id lof
        exome{ac an homozygote_count} genome{ac an homozygote_count}}}}""" % a.gene
    g = get("https://gnomad.broadinstitute.org/api", data=json.dumps({"query": q}).encode(),
            headers={"content-type": "application/json"})
    (out / "gnomad.json").write_bytes(g)
    print("fetched", len(accs), "family sequences;", len(recs), "ClinVar records")


def get_or_empty(url: str) -> bytes:
    try:
        return get(url, tries=2)
    except Exception as e:
        return json.dumps({"error": str(e)}).encode()


if __name__ == "__main__":
    main()
