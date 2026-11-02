# A0A5F5PNJ9 (horse, UniProt gene name SAT1) - identity check

Script: `identity_check.py` (PEP 723; run with `uv run --script identity_check.py`).
Raw output: `identity_check.out`. All data fetched live from UniProt REST, Ensembl REST
(EquCab3.0) and the PANTHER v19 geneinfo service on 2026-10-21; nothing is hardcoded.

## Findings

- A0A5F5PNJ9 is a 198-residue protein that is 91.4% identical (181/198) over its full length to
  human APOO/MIC26 (Q9BUR5, 198 aa), 82.8% identical to mouse Mic26 (Q9DCZ4), 36.4% identical to
  the paralogue human APOOL/MIC27 (Q6UXV4), and only 21.7% identical (43 identities, ungapped
  pairs 141) to human SAT1, the spermidine/spermine N1-acetyltransferase (P21673), which is the
  background expected for unrelated proteins.
- Ensembl maps A0A5F5PNJ9 to translation ENSECAP00000049988, transcript ENSECAT00000077118
  (APOO-201), of gene ENSECAG00000013441, whose display name is APOO, "apolipoprotein O
  [Source:VGNC Symbol;Acc:VGNC:15425]", on chromosome X. Ensembl Compara calls this gene a
  one-to-one orthologue (ortholog_one2one) of human ENSG00000184831 (APOO).
- PANTHER v19 places A0A5F5PNJ9 in PTHR14564:SF2 "MICOS COMPLEX SUBUNIT MIC26", the same
  subfamily as human APOO (Q9BUR5); human APOOL is in PTHR14564:SF3 "MICOS COMPLEX SUBUNIT MIC27".
- The horse APOO gene has nine Ensembl protein-coding transcripts. A0A5F5PNJ9 (APOO-201, 198 aa)
  is not the Ensembl canonical transcript (APOO-209, 241 aa), but its length and end-to-end
  alignment match the reviewed human and mouse MIC26 proteins exactly. The other horse UniProt
  entry for this gene, F7AGU3 (200 aa, gene name APOO), differs from it only at the N-terminus
  (197/198 identical).

## Interpretation

The gene name SAT1 on A0A5F5PNJ9 is a nomenclature error. The protein is the horse
orthologue of MIC26/APOO and is not related to SAT1. It is a full-length product, not
a fragment, and its single predicted transmembrane helix (UniProt 110..128) is at
the position of the human helix (108..128).

## Limits

These are pairwise global alignments and database assignments. No phylogeny was built. The
orthology call rests on the PANTHER subfamily and on Ensembl Compara, not on percent identity.
