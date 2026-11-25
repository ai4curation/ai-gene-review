# cym1 notes

## GO-CAM context

Model 69729a3800007453 represents Cym1 as a mitochondrial matrix
metalloendopeptidase involved in peptide catabolic process downstream of MPP and
Oct1-mediated presequence cleavage. That agrees with this gene review.

The only upstream curation granularity issue is in the current PTHR43016 PAINT
process IBD: PTN000220482 still transfers the broad GO:0030163 protein
catabolic process, whereas the GO-CAM and the PomBase ISS row use
GO:0043171 peptide catabolic process for the core Cym1/PreP degradation of
released mitochondrial targeting peptides.

No change was made to the shared GO-CAM review file in this gene PR; the final
GO-CAM consistency-notes PR should mention that the model's Cym1 activity uses
the more precise peptide-catabolism term.

## Live donor checks

On 2026-11-25, QuickGO's `GO:0043171` ancestor query showed
`GO:0043171 peptide catabolic process` under peptide metabolism and
organonitrogen compound catabolism, not under `GO:0006508 proteolysis`.

On 2026-11-25, QuickGO `annotation/search` for `UniProtKB:P32898` returned zero
current `GO:0005758` rows and current `GO:0005759` matrix rows from PAINT, SGD,
and UniProt, including SGD and UniProt IDA rows to PMID:21621546. The same API
returned the 2026-05-30 GO Central IBA and a 2013 SGD IMP from PMID:15772085 for
`GO:0030163` on S. cerevisiae `CYM1`; its query for the second PAINT donor,
`UniProtKB:Q76NL8`, returned the same 2026-05-30 PAINT IBA and a direct GeneDB
IDA row to `GO:0042540 hemoglobin catabolic process`.
