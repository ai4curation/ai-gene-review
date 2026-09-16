# TAS2R16 curation notes

## Identity
UniProt Q9NYV7 / T2R16_HUMAN, HGNC:14921, gene TAS2R16, single-exon TAS2R-family
GPCR on chromosome 7. 291 aa, 7TM class-A-like receptor. Now has cryo-EM
structures (PDB 9K6L, 9KPD, 9KPE, 9KPF; see genes/human/TAS2R16/TAS2R16-uniprot.txt).

## Core function
Bitter chemoreceptor for beta-D-glycopyranosides (salicin-type). Founding paper:
[PMID:12379855 "Here we report that a human member of this family, TAS2R16, is
present in taste receptor cells on the tongue and is activated by bitter
beta-glucopyranosides."] and [PMID:12379855 "Bitter compounds consisting of a
hydrophobic residue attached to glucose by a beta-glycosidic bond activate
TAS2R16."]. Broader receptive-range profiling: [PMID:20022913 "we have
challenged 25 human taste 2 receptors (hTAS2Rs) with 104 natural or synthetic
bitter chemicals in a heterologous expression system."]

Deep research (falcon/Edison, `TAS2R16-deep-research-falcon.md`) adds detail
on the structure-function work (Thomas et al. 2017, Sci Rep, 573 receptor
mutants, TM3/TM7 "two-faced" binding pocket) that is not itself cached as a
publications/PMID file here, so I did not cite it as a formal `references`
entry with `supporting_text` (no verbatim-checkable cache) — I only used it as
background context for the `description` field and did not assert unverifiable
direct quotes from it.

## Trafficking / accessory proteins
[PMID:16720576] (Behrens et al. 2006) — cached record is abstract-only
(`full_text_available: false`). Abstract text used for supporting_text:
- "By immunocytochemistry we show accumulation of the bitter beta-glucopyranoside
  receptor hTAS2R16 in the Golgi compartment."
- "The coimmunoprecipitation of hTAS2R16 and RTP3 or RTP4 suggests that the
  mechanism by which these cofactors influence hTAS2R16 function might involve
  direct protein-protein interaction."
- "Coexpression of RTP and REEP proteins changed the responses of some hTAS2Rs
  upon agonist stimulation, which is likely due to efficient cell surface
  localization as demonstrated by cell surface biotinylation experiments."

Confirmed via UniProt REST lookups (not from memory) that the two IPI
`protein binding` partners in the GOA file are:
- UniProtKB:Q96DX8 = RTP4 (Receptor-transporting protein 4)
- UniProtKB:Q9BQQ7 = RTP3 (Receptor-transporting protein 3)

Both match the paper's title ("Members of RTP and REEP gene families...").
Per the curation guideline against annotating bare "protein binding", I
proposed MODIFY -> GO:0051087 "protein-folding chaperone binding" for both
rows (verified as a real, non-obsolete GO term via QuickGO REST lookup:
name "protein-folding chaperone binding", definition "Binding to a chaperone
protein, a class of proteins that bind to nascent or unfolded polypeptides
and ensure correct folding or transport."). RTP3/RTP4 are documented
GPCR-export chaperones for TAS2Rs, so TAS2R16 "enables chaperone binding" is
a materially more informative statement than generic protein binding.

## IBA rows
Both bitter-taste-receptor-activity and detection-of-bitter-chemical-stimulus
IBA rows are propagated from PANTHER node PTN000149628, seeded in part by
TAS2R16's own experimental (IDA) annotations for the same terms. Per
CLAUDE.md's "What an IBA asserts" guidance, this self-inclusion in WITH/FROM
is expected and was not treated as circular; both accepted as core.

## Generic 'membrane' rows
Three GO:0016020 "membrane" rows (IBA, IC, IEA) were marked
MARK_AS_OVER_ANNOTATED (not wrong, but subsumed by the much more specific,
independently well-evidenced GO:0005886 plasma membrane annotations already
present) — this matches standard practice elsewhere in this repository (e.g.
ABCB10, ABCD4) for generic membrane calls alongside specific compartment
calls.

## Polymorphism / disease association caveats
UniProt VARIANT records cite PMID:16051168 (Soranzo et al. 2005, Curr Biol,
K172N sensitivity) and PMID:16385453 (Hinrichs et al. 2006, Am J Hum Genet,
alcohol-dependence association) for the Lys172/Asn172 polymorphism. Neither
PMID is cached under `publications/` in this repo, so I did not cite them as
formal `references` with `supporting_text` (would fail the verbatim-substring
check) and instead only summarized this cautiously in `description` and
`suggested_questions`, consistent with the task brief to "treat cautiously —
verify against the cached literature, don't overstate."

## Validation
`just validate human TAS2R16` — clean pass, 0 warnings, 0 errors, after:
1. filling all 26 `existing_annotations[].review` blocks,
2. adding `propagation_review` to the IBA `MARK_AS_OVER_ANNOTATED` membrane row,
3. citing the deep-research file once in `supported_by` (validator otherwise
   warns that no annotation references the available deep-research file).
