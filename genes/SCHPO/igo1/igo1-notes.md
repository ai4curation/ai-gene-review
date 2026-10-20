# igo1 curation notes

## 2026-09-27 Initial review (P79058, SPAC10F6.16, igo1 / mug134)

### Inputs

- `igo1-uniprot.txt` (entry version 116), `igo1-goa.tsv` (11 rows, 6 references),
  `igo1-deep-research-falcon.md` (Edison/Falcon synthesis, 18 citations, plus
  `artifact-00.md` table).
- Cached publications: PMID:26776736 Chica et al. 2016 (abstract only),
  PMID:29079657 Laboucarie et al. 2017 (abstract only), PMID:31553675 Schutt &
  Moseley 2019 (full text), PMID:16823372 Matsuyama et al. 2006 ORFeome screen
  (abstract only), PMID:16303567 Martin-Castellanos et al. 2005 meiotic screen
  (abstract only; cited by UniProt for induction).
- Open-access full texts consulted online via Europe PMC (not cached, so not
  quoted in `supported_by`): Laboucarie 2017 (PMC5709762, PMC HTML), Martin et
  al. 2017 Curr Biol 27:175 (PMC5266790), Perez-Hidalgo & Moreno 2017
  Biomolecules 7:59 (PMC5618240), del Dedo et al. 2024 Nat Commun (PMC11621810).
  Chica 2016 is not open access.
- Comparators: yeast IGO1 (complete), human ENSA / ARPP19 (complete), S. pombe
  ppk18 (complete, same session batch), S. pombe pab1 (queued);
  `modules/g2_m_transition.yaml` cites igo1 (P79058) as the fission-yeast
  endosulfine exemplar. igo1 is not in `gocams/index.tsv`.

### Gene identity

- 139 aa endosulfine (Pfam PF04667, PANTHER PTHR10358:SF6), Ser64 in the
  conserved YFDSGDY motif (sequence ...GRKYFDSGDYALNK...; residue 64 = S of
  FDSGDY). Disordered C-terminal region 83-139 (MobiDB-lite).
- The GOA symbol column and the UniProt recommended name still say "mRNA
  stability protein mug134"; the PomBase primary name is igo1. UniProt's FUNCTION
  line ("initiation of the G0 program by preventing the degradation of specific
  nutrient-regulated mRNAs") is a transfer from S. cerevisiae Igo1 (Talarek 2010)
  and has no fission-yeast experimental support. The Falcon report flags this
  [file:igo1-deep-research-falcon.md "The historical description “mRNA
  stability protein” is incomplete relative to current evidence."]. Recorded as
  `correctness: LOW_QUALITY` on the UniProt reference.
- mug134 = meiotically upregulated gene 134 from the Martin-Castellanos 2005
  deletion screen [PMID:16303567 "we have deleted 175 meiotically upregulated
  genes and found seven genes not previously reported to be critical for
  meiotic events"]; igo1 was not one of the seven.

### Holistic picture

1. **Core function: Ppk18-phosphorylated PP2A-B55 (Pab1) inhibitor that couples
   nitrogen status to G2/M size control.** [PMID:26776736 "Here we show that the
   greatwall-endosulfine (Ppk18-Igo1 in fission yeast) pathway couples the
   nutritional environment to the cell-cycle machinery by regulating the
   activity of PP2A·B55."; "When nutrients are limiting, TORC1 activity falls
   off, and the activation of greatwall (Ppk18) leads to the phosphorylation of
   endosulfine (Igo1) and inhibition of PP2A·B55, which in turn allows full
   activation of Cdk1·CyclinB and entry into mitosis with a smaller cell size."].
   Falcon adds the Ser64 site, the elevated PP2A-B55 activity in igo1Δ and the
   pab1 epistasis [file:igo1-deep-research-falcon.md "Loss of *igo1* causes
   abnormally high PP2A-B55 activity under nitrogen-poor or nitrogen-free
   conditions, while genetically reducing PP2A-B55 can rescue multiple *igo1Δ*
   phenotypes."]. Ser64 phosphorylation is detected in vivo with a P-ENSA
   antibody on nitrogen starvation or tor2-51 inactivation (Martin 2017, Fig S4;
   online full text). GO:0004865 IDA, GO:1905287 IMP and GO:0035556 IMP all
   ACCEPT; GO:0004864 IBA ACCEPT (igo1 in its own WITH/FROM is expected).
2. **Nutrient relay to differentiation (Laboucarie 2017, online full text).**
   "Therefore, starvation induces the phosphorylation of Igo1‐Ser64, most likely
   through the Ppk18 kinase, and this pathway is required to promote
   differentiation"; ste11+/mei2+ induction and differentiated-cell counts are
   reduced in ppk18Δ, igo1Δ and igo1-S64A; "gcn5 Δ and pab1 Δ mutants suppress the
   sterility of ppk18 Δ and igo1‐S64A mutants (Appendix Fig S8)"; "Taf12
   phosphorylation is reduced in starved ppk18 Δ, igo1 Δ, and igo1‐S64A mutants";
   "the absence of PP2A‐Pab1 rescues the inability of igo1‐S64A mutants to
   induce Taf12 phosphorylation". Cached abstract only gives the framework
   [PMID:29079657 "Taf12 phosphorylation increases early upon starvation and is
   controlled by the opposing activities of the PP2A phosphatase, which is
   activated by TORC1, and the TORC2-activated Gad8AKT kinase."]. Martin 2017
   (online): igo1Δ blocks Gad8 Ser546 phosphorylation and mei2 induction on
   tor2-51 TORC1 inactivation; constitutively active ryh1QL (TORC2 activator)
   rescues mei2 expression in tor2-51 igo1Δ. GO:0031139 IGI (with pab1,
   SPAC227.07c) ACCEPT and made the second core function, as for ppk18.
3. **Quiescence entry / translation (del Dedo 2024, online full text; Falcon).**
   "elevated PP2A/B55 phosphatase activity, resulting from the deletion of
   Endosulfine (igo1∆), impairs the translation efficiency of mRNAs enriched in
   AAA codons during entry into quiescence"; igo1Δ loses Rap1, Sgo2, Clr2/Clr3,
   telomere attachment and subtelomeric silencing after nitrogen removal, all
   rescued by repressing pab1; reduced mcm5s2U34 and t6A37 tRNA modification;
   paromomycin sensitivity; partial rescue by gsk3Δ [file:igo1-deep-research-
   falcon.md "In *igo1Δ* cells, polysome-to-monosome ratios were **78% of wild
   type in nitrogen-rich medium** and only **27% after four hours of
   starvation**."]. Autophagy: [file:igo1-deep-research-falcon.md "Igo1 loss
   also reduces autophagic flux, and deletion of the PP2A catalytic subunit gene
   *ppa2* rescues this defect."]. None of this is in GOA. Not proposed as NEW:
   the work of translation/tRNA modification is done by Elongator, Ctu1, Trm112
   and TORC2-Gad8 downstream; Igo1's contribution is entirely through PP2A-B55
   inhibition, which is already captured. Folded into the narrative of core
   function 2.
4. **Sds23 genetic interaction (full text cached).** [PMID:31553675 "Both igo1∆
   and ppk18∆ mutants alone did not display defects in cell shape, cell length
   at division, or division symmetry under normal growing conditions"]; double
   mutants more bent and larger at division, but for division symmetry "the
   double mutants were not significantly different from sds23∆ alone despite
   this trend (Figure 5E)". GO:1902472 IGI -> MARK_AS_OVER_ANNOTATED, same
   grading as the ppk18 review.
5. **Localisation.** Only direct datum: ORFeome YFP screen (rich medium),
   cytosol + nucleus [PMID:16823372 "we determined the localization of 4,431
   proteins ... by tagging each ORF with the yellow fluorescent protein"];
   UniProt "SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:16823372}.
   Cytoplasm". Falcon says it found no direct localisation
   [file:igo1-deep-research-falcon.md "not direct Igo1 microscopy or
   fractionation"] - a retrieval gap, not a contradiction. Laboucarie 2017 used
   Igo1-MYC only for Phos-tag westerns. All four CC rows ACCEPT.
6. **Other phosphosites (Falcon, from the Garcia Blanco 2021 thesis).** Cdk1
   sites Ser31/Ser89/Ser102 in vitro and by MS; PKA-consensus Ser76/Ser115;
   Igo1-4A has nutrient-dependent size phenotypes [file:igo1-deep-research-
   falcon.md "Cdk1–Cyclin B phosphorylates Igo1 in vitro."]. Raised as a
   suggested question, not annotated.

### NEW-term consideration

- GO:0010923 negative regulation of phosphatase activity (the BP counterpart of
  the inhibitor MF) was added as NEW in the human ENSA review with ARPP19 as
  comparator. Comparator check here (QuickGO, 2026-09-27): S. pombe sds23
  (Q09826), the other PP2A-family inhibitor, carries GO:0004865 (IDA, IBA) but
  no GO:0010923; PomBase appears to capture the inhibitor role with the MF term
  alone. Treated as a convention, not a gap; raised as a suggested question.
- GO:0006995 cellular response to nitrogen starvation is an ancestor (part_of)
  of the accepted GO:1905287 and was not added.

### Decisions summary

- ACCEPT (10): GO:0004864 IBA; GO:0004865 IDA; GO:0005634 HDA + IEA; GO:0005737
  IBA + IEA; GO:0005829 HDA; GO:0031139 IGI; GO:0035556 IMP; GO:1905287 IMP.
- MARK_AS_OVER_ANNOTATED (1): GO:1902472 IGI (sds23).
- No REMOVE, MODIFY, NEW. Considered MODIFY of GO:0035556 to TORC1 signaling
  (GO:0038202) and rejected: Igo1 is not a direct TORC1 target (TORC1 acts on
  Ppk18 upstream), matching the decision in the ppk18 review.
- core_functions: (1) PP2A-B55 inhibitor -> GO:1905287 + GO:0035556, cytosol +
  nucleus; (2) same MF -> GO:0031139 (differentiation/quiescence relay via
  Gad8/Taf12), cytosol + nucleus. No in_complex: Igo1 is a substrate-like
  inhibitor bound to PP2A-Pab1, not a holoenzyme subunit.

### Open items

- Direct biochemical demonstration of phospho-Igo1 binding/inhibition of
  purified S. pombe PP2A-Pab1 (affinity, B55 specificity versus Par1/Par2).
- Role of the Cdk1/PKA phosphosites; nutrient-dependent redistribution of Igo1.
- Whether all igo1Δ quiescence phenotypes collapse onto the Gad8-S546 branch.
