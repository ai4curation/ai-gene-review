#!/usr/bin/env bash
# Reproduce the eggNOG-mapper runs for this project.
#
#   scripts/run_all.sh WORK_DIR
#
# WORK_DIR receives the environment and databases (~17 GB: DIAMOND DB 9.3 GB,
# zstd-chunked eggnog.db ~6 GB). Steps:
#   1. venv with eggnog-mapper 2.1.13 (--no-deps; its biopython pin does not
#      build on current Python), apsw, zstandard; DIAMOND 2.1.10 binary
#   2. emapper DB 5.0.2: DIAMOND DB + taxa DB, and eggnog.db converted on the fly
#      to a seekable zstd-chunk store (zchunk_build_http.py)
#   3. DIAMOND seed-ortholog search for cohort.fasta (emapper defaults)
#   4. annotation, run "default": all orthologs
#   5. annotation, run "species_excluded": per species, --excluded_taxa <species>
set -euo pipefail
W=$(realpath "$1"); P=$(cd "$(dirname "$0")/.." && pwd)
mkdir -p "$W"/{env,bin,db,search} "$P/runs/default" "$P/runs/species_excluded"
if [ ! -x "$W/env/.venv/bin/python" ]; then
  (cd "$W/env" && uv venv -q --python 3.13 && uv pip install -q apsw zstandard biopython psutil xlsxwriter setuptools pyyaml \
     && uv pip install -q --no-deps eggnog-mapper==2.1.13)
fi
PY="$W/env/.venv/bin/python"; EM="$W/env/.venv/bin/emapper.py"
[ -x "$W/bin/diamond" ] || curl -sSL https://github.com/bbuchfink/diamond/releases/download/v2.1.10/diamond-linux64.tar.gz | tar xz -C "$W/bin"
export PATH="$W/bin:$PATH"
U=http://eggnog5.embl.de/download/emapperdb-5.0.2
[ -s "$W/db/eggnog_proteins.dmnd" ] || curl -sS --retry 5 "$U/eggnog_proteins.dmnd.gz" | gzip -dc > "$W/db/eggnog_proteins.dmnd"
[ -s "$W/db/eggnog.taxa.db" ] || curl -sS --retry 5 "$U/eggnog.taxa.tar.gz" | tar xz -C "$W/db"
[ -s "$W/db/eggnog.db.zci" ] || "$PY" -I "$P/scripts/zchunk_build_http.py" "$U/eggnog.db.gz" "$W/db/eggnog.db"
touch "$W/db/eggnog.db"   # placeholder for emapper's existence check; bytes come from the zchunk store

SEEDS="$W/search/cohort.emapper.seed_orthologs"
[ -s "$SEEDS" ] || "$EM" -m diamond --no_annot -i "$P/cohort.fasta" --data_dir "$W/db" \
    -o cohort --output_dir "$W/search" --temp_dir "$W/search" --cpu 4 --override

RUN="$PY $P/scripts/run_emapper.py --zchunk $W/db/eggnog.db --"
$RUN -m no_search --annotate_hits_table "$SEEDS" --data_dir "$W/db" -o default \
    --output_dir "$P/runs/default" --cpu 1 --mp_start_method fork --override

# species-excluded: one annotation run per species
"$PY" "$P/scripts/species_taxa.py" "$W/db/eggnog.taxa.db"
"$PY" "$P/scripts/split_seeds.py" "$SEEDS" "$W/search/by_species"
for f in "$W"/search/by_species/*.seed_orthologs; do
  sp=$(basename "$f" .seed_orthologs)
  $RUN -m no_search --annotate_hits_table "$f" --data_dir "$W/db" -o "sp$sp" \
      --output_dir "$W/search/by_species" --cpu 1 --mp_start_method fork --override --excluded_taxa "$sp" >/dev/null
done
"$PY" "$P/scripts/merge_annotations.py" "$W/search/by_species" "$P/runs/species_excluded/species_excluded.emapper.annotations"

# species-excluded, experimental GO evidence only (no ISS/ISO/IBA/TAS/IC transfers)
mkdir -p "$W/search/by_species_exp" "$P/runs/species_excluded_experimental"
cp "$W"/search/by_species/*.seed_orthologs "$W/search/by_species_exp/"
for f in "$W"/search/by_species_exp/*.seed_orthologs; do
  sp=$(basename "$f" .seed_orthologs)
  $RUN -m no_search --annotate_hits_table "$f" --data_dir "$W/db" -o "sp$sp" \
      --output_dir "$W/search/by_species_exp" --cpu 1 --mp_start_method fork --override \
      --excluded_taxa "$sp" --go_evidence experimental >/dev/null
done
"$PY" "$P/scripts/merge_annotations.py" "$W/search/by_species_exp" \
    "$P/runs/species_excluded_experimental/species_excluded_experimental.emapper.annotations"

# species-excluded with the narrowest pre-configured taxonomic scope
mkdir -p "$W/search/by_species_narrow" "$P/runs/species_excluded_narrow"
cp "$W"/search/by_species/*.seed_orthologs "$W/search/by_species_narrow/"
for f in "$W"/search/by_species_narrow/*.seed_orthologs; do
  sp=$(basename "$f" .seed_orthologs)
  $RUN -m no_search --annotate_hits_table "$f" --data_dir "$W/db" -o "sp$sp" \
      --output_dir "$W/search/by_species_narrow" --cpu 1 --mp_start_method fork --override \
      --excluded_taxa "$sp" --tax_scope all_narrow >/dev/null
done
"$PY" "$P/scripts/merge_annotations.py" "$W/search/by_species_narrow" \
    "$P/runs/species_excluded_narrow/species_excluded_narrow.emapper.annotations"

# deep dive: non-model genomes (default, species-excluded, narrow scope)
D="$P/deep_dive"; mkdir -p "$W/deep/by_species" "$D/runs/default" "$D/runs/species_excluded" "$D/runs/narrow_scope"
DSEEDS="$W/deep/deep.emapper.seed_orthologs"
[ -s "$DSEEDS" ] || "$EM" -m diamond --no_annot -i "$D/cohort.fasta" --data_dir "$W/db" \
    -o deep --output_dir "$W/deep" --temp_dir "$W/deep" --cpu 4 --override
$RUN -m no_search --annotate_hits_table "$DSEEDS" --data_dir "$W/db" -o default \
    --output_dir "$D/runs/default" --cpu 1 --mp_start_method fork --override
$RUN -m no_search --annotate_hits_table "$DSEEDS" --data_dir "$W/db" -o narrow_scope \
    --output_dir "$D/runs/narrow_scope" --cpu 1 --mp_start_method fork --override --tax_scope all_narrow
"$PY" "$P/scripts/species_taxa.py" "$W/db/eggnog.taxa.db" "$D"
"$PY" "$P/scripts/split_seeds.py" "$DSEEDS" "$W/deep/by_species" "$D"
for f in "$W"/deep/by_species/*.seed_orthologs; do
  sp=$(basename "$f" .seed_orthologs)
  $RUN -m no_search --annotate_hits_table "$f" --data_dir "$W/db" -o "sp$sp" \
      --output_dir "$W/deep/by_species" --cpu 1 --mp_start_method fork --override --excluded_taxa "$sp" >/dev/null
done
"$PY" "$P/scripts/merge_annotations.py" "$W/deep/by_species" "$D/runs/species_excluded/species_excluded.emapper.annotations"
# then: score_emapper.py [--runs ...] and score_emapper.py --base deep_dive --runs default,species_excluded,narrow_scope
