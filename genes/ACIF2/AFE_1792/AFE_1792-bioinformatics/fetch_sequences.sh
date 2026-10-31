#!/usr/bin/env bash
# Download the SQR family target and reference sequences from UniProt REST.
set -euo pipefail
cd "$(dirname "$0")"
ACCS="B7JBP8 F9ZQD6 A0A060UVE9 A0A543Q349 A0A059XTE6 O67931 Q7ZAG8 B7J411 Q9Y6N5 A8MAC9 A8MCW1 Q8KE17 Q8KDG3 Q8KG51 Q8KAS4"
: > sequences.fasta
for a in $ACCS; do
  curl -sS "https://rest.uniprot.org/uniprotkb/${a}.fasta" >> sequences.fasta
done
grep -c '>' sequences.fasta
