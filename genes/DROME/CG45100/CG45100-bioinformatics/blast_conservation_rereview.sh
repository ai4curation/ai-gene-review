#!/usr/bin/env bash
# Reproducible conservation check for the 38-aa CG45100 (A0A0B4LGP2) uORF peptide.
# Submits blastp (PAM30, short-query matrix) against UniProtKB via the EBI Job Dispatcher REST API
# and saves the raw report. Interpretation is in RESULTS-rereview.md.
set -euo pipefail
EMAIL="${EMAIL:?set EMAIL for the EBI REST API}"
SEQ=">A0A0B4LGP2
MLLGEYDTTRRLLFIVAVLLIVLYAKTYLLPGEDLVHN"
JOB=$(curl -s -X POST https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/run \
  -d email="$EMAIL" -d program=blastp -d stype=protein -d database=uniprotkb \
  -d matrix=PAM30 -d exp=10 -d alignments=50 -d scores=50 --data-urlencode "sequence=$SEQ")
echo "job: $JOB"
until [ "$(curl -s https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/status/$JOB)" = FINISHED ]; do sleep 10; done
curl -s "https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/result/$JOB/out" > blast_uniprotkb_rereview.out
echo "saved blast_uniprotkb_rereview.out"
