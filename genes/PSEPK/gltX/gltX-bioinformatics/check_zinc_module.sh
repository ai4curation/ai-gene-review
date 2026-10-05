#!/usr/bin/env bash
set -euo pipefail

record="$(dirname "$0")/../gltX-uniprot.txt"
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT

curl -fsSL 'https://rest.uniprot.org/uniprotkb/P04805.fasta' -o "$tmpdir/p04805.fasta"
awk '
  /^SQ   SEQUENCE/ { in_sequence=1; print ">sp|Q88LF6|SYG_PSEPK"; next }
  in_sequence && /^\/\// { exit }
  in_sequence { gsub(/[^A-Z]/, ""); printf "%s", $0 }
  END { if (in_sequence) printf "\n" }
' "$record" > "$tmpdir/q88lf6.fasta"

cat "$tmpdir/p04805.fasta" "$tmpdir/q88lf6.fasta" > "$tmpdir/input.fasta"
mafft --quiet "$tmpdir/input.fasta"
