#!/usr/bin/env bash
# Download the BC4GO corpus (Van Auken et al. 2014, PMID:25070993) from NCBI.
# Not committed: the corpus is for non-commercial use and contains full-text articles.
set -euo pipefail
dest="$(dirname "$0")/raw/bc4go"
mkdir -p "$dest"
for f in BC4GO_Corpus_Training_Set_.zip bc4go_dev_v081213.zip bc4go_test_v090313_.zip bc4go_eval_v091613.zip; do
  curl -sS --fail -o "$dest/$f" "https://ftp.ncbi.nlm.nih.gov/pub/lu/BC4GO/$f"
  unzip -o -q "$dest/$f" -d "$dest" -x "__MACOSX/*" "*.DS_Store"
done
