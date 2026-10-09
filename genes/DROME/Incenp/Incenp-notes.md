# Incenp (Drosophila melanogaster) curation notes

Accession used: A0A0B4LFQ2 (Incenp isoform C, TrEMBL; FBgn0260991).

Deep research: `just deep-research-falcon DROME Incenp --fallback perplexity-lite` failed
(falcon timed out after 600 s; perplexity provider not available). Literature below is from
the cached publications.

## Literature journal

- Incenp is the CPC scaffold thought to regulate and target Aurora B
  [PMID:16507586 "The inner centromere protein (Incenp; a subunit of this complex) is thought to regulate the Aurora B kinase and target it to its substrates"].
- Null allele: no H3S10 phosphorylation, cytokinesis failure, polyploidy
  [PMID:16507586 "Homozygous incenp(EC3747) embryos show absence of phosphorylation of histone H3 in mitosis, failure of cytokinesis and polyploidy"];
  Prospero mis-segregation in neuroblasts [PMID:16507586 "the segregation of the cell-fate determinant Prospero in asymmetric neuroblast division is abnormal"].
- Male meiosis: INCENP colocalizes with and binds MEI-S332; mutants separate sisters prematurely
  [PMID:16824953 "INCENP and MEI-S332 colocalized at centromeres during wild-type male meiosis"]
  [PMID:16824953 "INCENP binds to the cohesion protector protein MEI-S332"]
  [PMID:16824953 "premature sister chromatid separation in meiosis I"].
- Female meiosis (acentrosomal): spindle assembly delayed; equator destabilized
  [PMID:18755775 "the initial assembly of spindle microtubules is drastically delayed in an incenp mutant"]
  [PMID:18755775 "Incenp is necessary to stabilise the equatorial region of the metaphase I spindle"];
  oocyte central spindle contains AurB and Incenp [PMID:16055508 "The meiotic central spindle appears during prometaphase and includes passenger complex proteins such as AurB and Incenp"].
- Localization in spermatocytes/neuroblasts: kinetochores at metaphase, midzone in anaphase
  [PMID:21865602 "INCENP and Aurora B localized correctly to kinetochores at metaphase"]
  [PMID:21865602 "both CPC proteins failed to accumulate to the central spindle midzone during ana/telophase in scpo spermatocytes"].
- CPC membership by affinity purification [PMID:22724069 "A reciprocal affinity purification using cells expressing PtA::Shrb also identified all the CPC components"].

## Decisions

- All IDA localizations (centromere, kinetochore, mitotic/meiotic midzone) accepted; general chromosome and IEA cytoplasm kept as non-core.
- Asymmetric cell division and meiotic chromosome condensation kept as non-core (downstream / secondary to the main findings).
- Core MF given as protein serine/threonine kinase activator activity (IN-box activation of Aurora B); no GOA MF row exists for Incenp.
