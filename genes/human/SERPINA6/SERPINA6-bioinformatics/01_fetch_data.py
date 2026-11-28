# /// script
# requires-python = ">=3.11"
# dependencies = ["requests"]
# ///
"""Download every external input used by the SERPINA6 (CBG, P08185) analysis into cache/.

Nothing is computed here. Re-running refreshes the cache; each file is written with the
URL it came from in cache/MANIFEST.tsv so the analysis can be traced to its sources.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE = HERE / "cache"
ACC = "P08185"
GENE = "SERPINA6"
ENSG = "ENSG00000170099"
PDB_IDS = ["2VDX", "2VDY", "4BB2", "4C41", "4C49", "2V95"]  # human CBG structures listed by UniProt P08185 + native rat CBG:cortisol (2V95, P31211)
# Comparator serpins for alignment (reactive-centre loop register, pocket conservation)
COMPARATORS = {
    "P01009": "A1AT_HUMAN",   # archetypal inhibitory clade-A serpin
    "P05543": "THBG_HUMAN",   # thyroxine-binding globulin, the other hormone-carrier serpin
    "P01011": "AACT_HUMAN",
    "P31211": "CBG_RAT",
    "Q06770": "CBG_MOUSE",
}
session = requests.Session()
session.headers["User-Agent"] = "serpina6-bioinformatics/1.0 (python-requests)"
manifest: list[tuple[str, str]] = []


def get(url: str, name: str, *, post: dict | None = None, binary: bool = False, tries: int = 4) -> Path:
    out = CACHE / name
    out.parent.mkdir(parents=True, exist_ok=True)
    last = None
    for i in range(tries):
        try:
            r = session.post(url, json=post, timeout=120) if post else session.get(url, timeout=120)
            if r.status_code == 200:
                out.write_bytes(r.content) if binary else out.write_text(r.text)
                manifest.append((name, url))
                return out
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:  # noqa: PERF203
            last = repr(e)
        time.sleep(2 * (i + 1))
    print(f"FAILED {name}: {last} ({url})", file=sys.stderr)
    manifest.append((name, f"FAILED {last} {url}"))
    return out


def main() -> None:
    CACHE.mkdir(exist_ok=True)
    get(f"https://rest.uniprot.org/uniprotkb/{ACC}.json", "uniprot_P08185.json")
    get(f"https://rest.uniprot.org/uniprotkb/{ACC}.fasta", "uniprot_P08185.fasta")
    for acc in COMPARATORS:
        get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", f"comparators/{acc}.fasta")
    # Orthologues: every UniProtKB entry whose gene name is exactly SERPINA6 (any taxon)
    get(
        "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
        "%28gene_exact%3ASERPINA6%29+AND+%28length%3A%5B350+TO+450%5D%29+AND+%28fragment%3Afalse%29",
        "orthologs_gene_exact_SERPINA6.fasta",
    )
    get(f"https://www.ebi.ac.uk/proteins/api/variation/{ACC}?format=json", "ebi_variation_P08185.json")
    for pdb in PDB_IDS:
        get(f"https://files.rcsb.org/download/{pdb}.cif", f"pdb/{pdb}.cif")
        get(f"https://data.rcsb.org/rest/v1/core/entry/{pdb}", f"pdb/{pdb}_entry.json")
        get(f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot_segments/{pdb.lower()}", f"pdb/{pdb}_sifts_segments.json")
    af = get(f"https://alphafold.ebi.ac.uk/api/prediction/{ACC}", "alphafold_api.json")
    try:
        entry = json.loads(af.read_text())[0]
        get(entry["cifUrl"], "alphafold_model.cif")
        if entry.get("amAnnotationsUrl"):
            get(entry["amAnnotationsUrl"], "alphamissense_substitutions.csv")
    except Exception as e:  # noqa: BLE001
        print(f"AlphaFold metadata not parsed: {e!r}", file=sys.stderr)
    gql = """
    query($g: String!) { gene(gene_symbol: $g, reference_genome: GRCh38) {
      gene_id symbol chrom start stop canonical_transcript_id
      gnomad_constraint { exp_lof obs_lof oe_lof oe_lof_lower oe_lof_upper pLI exp_mis obs_mis oe_mis oe_mis_lower oe_mis_upper mis_z lof_z exp_syn obs_syn oe_syn syn_z }
      variants(dataset: gnomad_r4) { variant_id pos ref alt rsids consequence hgvsc hgvsp lof lof_filter transcript_id
        exome { ac an homozygote_count filters } genome { ac an homozygote_count filters }
        joint { ac an homozygote_count } }
      clinvar_variants { variant_id clinvar_variation_id clinical_significance gold_stars major_consequence hgvsc hgvsp review_status in_gnomad }
    } }"""
    get("https://gnomad.broadinstitute.org/api", "gnomad_gene.json", post={"query": gql, "variables": {"g": GENE}})
    es = get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&retmode=json&retmax=2000&term="
        f"{GENE}%5Bgene%5D",
        "clinvar_esearch.json",
    )
    try:
        ids = json.loads(es.read_text())["esearchresult"]["idlist"]
        chunks = [ids[i : i + 150] for i in range(0, len(ids), 150)]
        for n, ch in enumerate(chunks):
            get(
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&retmode=json&id=" + ",".join(ch),
                f"clinvar_esummary_{n}.json",
            )
            time.sleep(0.5)
    except Exception as e:  # noqa: BLE001
        print(f"ClinVar esearch not parsed: {e!r}", file=sys.stderr)
    (CACHE / "MANIFEST.tsv").write_text(
        "file\tsource_url\n" + "\n".join(f"{n}\t{u}" for n, u in manifest) + f"\n# fetched {time.strftime('%Y-%m-%d')}\n"
    )
    print(f"wrote {len(manifest)} files to {CACHE}")


if __name__ == "__main__":
    main()
