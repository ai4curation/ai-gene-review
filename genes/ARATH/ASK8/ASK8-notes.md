# ASK8 review notes

## Session 1 (2026-10-28)

- fetch-gene resolved Q96287 (KSG8_ARATH, At4g00720, GeneID 828023); 15 GOA rows.
- Key paper PMID:20128883 (Rozhon et al. 2010) cached with full text and read in full.
  PMID:21477822 (HDA autophosphorylation screen) and PMID:17427040 (Claisse 2007, AtSK3-2)
  are abstract-only.
- Literature summary with provenance: ASK8-deep-research-manual.md.

### Decisions

- Core MF: protein serine/threonine kinase activity (GO:0004674). Direct evidence: MBP, BES1,
  BZR1, BEH2 phosphorylation and autophosphorylation, K167R kinase-dead control
  [PMID:20128883 "GST-ASKθ phosphorylated GST-BZR1, GST-BES1 and GST-BEH2, but not GST alone (Figure 5)."].
  The IDA "kinase activity" and IEA "protein kinase activity" rows are MODIFIED to GO:0004674.
- Core BP: brassinosteroid mediated signaling pathway (GO:0009742; is_a descendant of
  GO:0009741 response to brassinosteroid and of GO:0007165 signal transduction, checked with OAK).
  ASK-theta acts downstream of BRI1 and phosphorylates the BES1/BZR1 family TFs, which is a step
  of the pathway performed by the kinase itself. The IBA signal transduction and IMP response to
  brassinosteroid rows are MODIFIED to it.
- Negative regulation of BR signalling (GO:1900458) is the authors' interpretation, but it rests
  mainly on overexpression; knockouts are normal. Not added as NEW; raised as a question.
- cell differentiation IBA: no ASK8-specific support; animal/Dictyostelium-derived. MARK_AS_OVER_ANNOTATED.
- cytoplasm IBA: low cytoplasmic YFP signal observed; KEEP_AS_NON_CORE.
- Nomenclature: Dong 2015 (PMID:25997736) calls At3g61160 "AtSK32"; not this gene; not used.
- Note for others: the BIN2 review description calls ASK-theta "BIL2"; Rozhon 2010 places
  ASK-theta in group III, not with BIN2/ASK-iota/ASK-zeta (group II). Not edited here (out of scope).
