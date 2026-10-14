# Incenp (Drosophila melanogaster) curation notes

Accession used: A0A0B4LFQ2 (Incenp isoform C, TrEMBL; FBgn0260991).

Deep research: `Incenp-deep-research-falcon.md` (falcon; the wrapper logged a 600 s timeout but the run completed and wrote the file). It agrees that Incenp is the non-enzymatic CPC scaffold/Aurora B activator (IN-box) and targeting subunit, adds that purified DmINCENP binds microtubules directly and recruits/activates Polo (Aurora B phosphorylates Polo T182) at centromeres, and notes that in oocytes INCENP sits on a ring around the karyosome and the central spindle rather than at CID/MEI-S332 centromeres. These points were checked against the cached primary papers where available; they do not change the annotation decisions.

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

- All IDA localizations (centromere, kinetochore, mitotic/meiotic midzone) accepted; general chromosome IDA modified to chromosome, centromeric region; IEA cytoplasm kept as non-core.
- Asymmetric cell division and meiotic chromosome condensation kept as non-core (downstream / secondary to the main findings).
- No core MF asserted (see revision below).
- Revision after PR review: GO:0043539 (kinase activator activity) and GO:0000070 removed from core_functions because neither is a reviewed annotation for Incenp and the cached fly evidence for Aurora B activation is only a hedged statement; the activation claim stays in the description and suggested_questions.
