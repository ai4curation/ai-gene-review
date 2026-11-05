#!/usr/bin/env bash
# Download the pinned external inputs for the SURFACEOME project into projects/SURFACEOME/data/.
# Zenodo record 23445521 = "The accessible human surfaceome" v1.3.0 (concept record 20805383).
set -euo pipefail
D="$(cd "$(dirname "$0")/.." && pwd)/data"
mkdir -p "$D"
Z=https://zenodo.org/api/records/23445521/files
curl -sSL -o "$D/triage-benchmark-with-reasoning.tsv" "$Z/triage-benchmark-with-reasoning.tsv/content"
curl -sSL -o "$D/deep-dive-preset-membership.tsv"   "$Z/deep-dive-preset-membership.tsv/content"
curl -sSL -o "$D/zenodo-README.md"                  "$Z/README.md/content"
# Current public human GO annotations (GO Consortium release).
curl -sSL -o "$D/goa_human.gaf.gz" http://current.geneontology.org/annotations/goa_human.gaf.gz
zcat "$D/goa_human.gaf.gz" | grep -m1 '^!date-generated' || true
ls -la "$D"
