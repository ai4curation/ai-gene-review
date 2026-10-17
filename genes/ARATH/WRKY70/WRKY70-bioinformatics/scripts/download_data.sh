#!/usr/bin/env bash
# Download all raw inputs for the WRKY70 DAP-seq target analysis into data/.
# Raw files are git-ignored; this script is the record of exactly where they come from.
#
# Usage: scripts/download_data.sh [DATA_DIR]   (default: data)
set -euo pipefail

DATA_DIR="${1:-data}"
mkdir -p "$DATA_DIR/dap_wrky"

DAP=http://neomorph.salk.edu/dap_web/pages/dap_data_v4
ENS=https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/release-63
GO=https://current.geneontology.org

fetch() {  # url dest
  if [[ -s "$2" ]]; then echo "exists: $2"; return; fi
  echo "fetch: $1"
  curl -sS --fail -m 600 -o "$2" "$1"
}

# 1. O'Malley et al. 2016 (PMID:27203113) Plant Cistrome DAP-seq, WRKY70 (AT3G56400), Col-0 gDNA library
fetch "$DAP/peaks/WRKY_tnt/WRKY70_col/chr1-5/chr1-5_GEM_events.narrowPeak" "$DATA_DIR/WRKY70_col.narrowPeak"
fetch "$DAP/genes/WRKY_tnt/WRKY70_col/chr1-5/chr1-5_GEM_events.nS_targets.txt" "$DATA_DIR/WRKY70_col.nS_targets.txt"
fetch "$DAP/motifs/WRKY_tnt/WRKY70_col/meme_out/meme_m1.txt" "$DATA_DIR/WRKY70_col.meme_m1.txt"
# gene-target list of a second TF, used only by the `test-other-tf` sanity run
fetch "$DAP/genes/WRKY_tnt/WRKY33_col_a/chr1-5/chr1-5_GEM_events.nS_targets.txt" "$DATA_DIR/WRKY33_col_a.nS_targets.txt"

# 1b. All other WRKY DAP-seq peak sets (for specificity comparison at the queried promoters)
for ds in $(curl -sS --fail -m 120 "$DAP/peaks/WRKY_tnt/" | grep -oE 'href="WRKY[0-9]+_[a-z_]+/"' | sed -E 's/href="(.*)\/"/\1/'); do
  fetch "$DAP/peaks/WRKY_tnt/$ds/chr1-5/chr1-5_GEM_events.narrowPeak" "$DATA_DIR/dap_wrky/$ds.narrowPeak" || echo "FAILED: $ds"
done

# 2. TAIR10 genome annotation and sequence (Ensembl Plants release 63; Araport11-based gene models)
fetch "$ENS/gtf/arabidopsis_thaliana/Arabidopsis_thaliana.TAIR10.63.gtf.gz" "$DATA_DIR/Arabidopsis_thaliana.TAIR10.63.gtf.gz"
fetch "$ENS/fasta/arabidopsis_thaliana/dna/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz" "$DATA_DIR/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz"

# 3. GO ontology + TAIR GO annotations (for curated gene sets used in the enrichment test)
fetch "$GO/ontology/go-basic.obo" "$DATA_DIR/go-basic.obo"
fetch "$GO/annotations/tair.gaf.gz" "$DATA_DIR/tair.gaf.gz"

# Record versions / checksums
{
  echo "# downloaded $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  grep -m1 '^data-version' "$DATA_DIR/go-basic.obo" || true
  zcat "$DATA_DIR/tair.gaf.gz" | grep -m5 -E '^!(gaf-version|date-generated|generated-by)' || true
  (cd "$DATA_DIR" && sha256sum WRKY70_col.* Arabidopsis_thaliana.TAIR10.63.gtf.gz tair.gaf.gz go-basic.obo)
} > "$DATA_DIR/VERSIONS.txt"
echo "done"
