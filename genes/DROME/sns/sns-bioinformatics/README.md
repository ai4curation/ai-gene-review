# Sns isoform comparison

Run `just analyze`. Pinned Biopython/numpy dependencies are in pyproject.toml.
The generic script globally aligns arbitrary UniProt JSON and FASTA inputs with
BLOSUM62, gap open−10/extension−0.5, computing exact identities and all indels.
It hardcodes no target-specific residue or verdict.

Target: frozen project Q0E9F2 record, retained as ../sns-uniprot-source.json.
RefSeq A was fetched2026-09-09 UTC using
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_176106.2&rettype=gb&retmode=text .
The original GenBank record is retained. `sns-A.fasta` contains its CDS translation
for NP_788286.1, extracted using Biopython SeqIO without sequence editing.
The independent control uses CG4793 Q8IP30 and RefSeq NP_723941.2, copied from the
CG4793 catalytic analysis (see that folder's provenance). Expected identity is
checked by actually running the same script, not hardcoded into it.
