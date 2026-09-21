# PP_0313 (Q88R21) curation notes — PSEPK second ETF beta subunit

## Identity

- UniProt Q88R21, locus PP_0313, 256 aa, *Pseudomonas putida* KT2440
  (NCBITaxon:160488).
- SubName only: "Electron transfer flavoprotein beta subunit"
  [file:PSEPK/PP_0313/PP_0313-uniprot.txt] — no RecName, no FUNCTION line, no
  COFACTOR line (note this differs from etfB/PP_4202, whose record does assert
  an AMP cofactor).
- Family: ["Belongs to the ETF beta-subunit/FixA family."] Domain support:
  Pfam PF01012 (ETF), InterPro IPR012255 (ETF_b), IPR014730 (ETF_a/b_N).
- PANTHER PTHR21294 / PTHR21294:SF8, the same family as etfB/PP_4202
  [file:projects/P_PUTIDA/data/psepk_gene_list.tsv:308].
- GOA carries exactly one annotation for this protein (GO:0009055), so the
  review is short by necessity.

## The donor is not unknown — genomic context

As for its partner PP_0312. The pair lies immediately downstream of
`dgcA` (PP_0310) and `dgcB` (PP_0311), both annotated "Dimethylglycine
dehydrogenase subunit (EC 1.5.8.-)"
[file:projects/P_PUTIDA/data/psepk_gene_list.tsv:305-306]; EC 1.5.8.- enzymes
use a flavin as acceptor and are ETF-dependent by definition. KEGG groups all
four genes in ppu00260 with the glycine-betaine and sarcosine oxidation genes
gbcAB and soxABDG [file:projects/P_PUTIDA/data/psepk_pathway_buckets.tsv:6].
Methylated-glycine oxidation is therefore the likely donor pathway. Not
asserted as established — the pairing has never been assayed. Full detail in
`genes/PSEPK/PP_0312/PP_0312-notes.md`.

## Curation decisions and why

### GO:0009055 electron transfer activity, `enables` — ACCEPT (was MARK_AS_OVER_ANNOTATED)

This was the single annotation on the gene, so marking it over-annotated would
have left PP_0313 with no molecular-function term whatsoever — while the
annotation is not wrong about what the protein is for. GO's convention for an
obligate subunit of a multi-protein electron carrier is to ACCEPT `enables` and
record the subunit-level dependency as `contributes_to_molecular_function`,
which this review does. The repo's completed ortholog review
`genes/human/ETFB/ETFB-ai-review.yaml` ACCEPTs the same term on the
corresponding beta subunit and calls it the core molecular function.

## Open questions

- Does PP_0313 bind AMP, as etfB/PP_4202 and human ETFB do? The record is
  silent; the family architecture suggests yes.
- Is the PP_0312/PP_0313 pair functionally redundant with EtfAB, or is it
  dedicated to the adjacent dgcAB dehydrogenase? Deletion of each pair with
  growth tests on betaine/dimethylglycine versus fatty acids would distinguish
  these.
