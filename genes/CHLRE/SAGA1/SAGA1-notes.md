# SAGA1 (Chlamydomonas reinhardtii) curation notes

UniProt A0A2K3D7T6 (TrEMBL, "CBM20 domain-containing protein"); locus Cre11.g467712
(CHLRE_11g467712v5); 1,626 aa, ~168 kDa predicted (~180 kDa on gels).

## Deep research

Deep research was not run. The falcon provider currently returns HTTP 402 and
perplexity is unavailable in this environment, so the wrapper was skipped on
instruction. The review rests on the cached primary literature listed below.
No `-deep-research-*.md` file exists for this gene.

## Sequence features (UniProt record)

- CBM20 starch-binding domain at residues 178-308 (PROSITE PS51166; Pfam PF00686; InterPro IPR002044).
- Long coiled-coil region (431-486, 519-599, 687-789 predicted) and an extended alpha-helical middle.
- Disordered N-terminal (91-180) and C-terminal (1512-1626) regions. Itakura 2019 places the CBM20 at aa 214-280.
- Two Rubisco-binding motifs (RBMs), one at the very C terminus. Meyer 2020 found the motif while working out what the anti-SAGA1 C-terminal peptide antibody was recognising.

## Literature summary

### Itakura et al. 2019 (PMID:31455733): discovery, phenotype, Rubisco binding
- Named for the abnormal starch sheath plates in the mutant [PMID:31455733 "SAGA1 contains a starch binding motif, suggesting that it may directly regulate starch sheath morphology"].
- CBM20 conserved residues are present, but starch binding was only predicted in 2019 [PMID:31455733 "All 5 highly conserved residues necessary for starch binding are present in SAGA1, suggesting that SAGA1 can bind starch"].
- Rubisco binding by yeast two-hybrid, with no binding to EPYC1 [PMID:31455733 "We conclude that SAGA1 binds to Rubisco large and small subunits."].
- saga1 has about 10 pyrenoids per cell, most of them without tubules. It is CCM-defective and grows poorly at low CO2 [PMID:31455733 "We conclude from these observations that SAGA1 is required for a functional CCM and for maximal CO2 uptake in cells acclimated to both low and high CO2."].
- SAGA1-Venus localizes to puncta and streaks in the pyrenoid [PMID:31455733 "We conclude that SAGA1-Venus localizes to the pyrenoid."].

### Meyer et al. 2020 (PMID:33177094): the Rubisco-binding motif
- SAGA1 carries the shared Rubisco-binding motif, and motif peptides bind Rubisco in vitro (SPR and peptide arrays).
- In the authors' model, SAGA1 and SAGA2 tie the matrix to the starch sheath [PMID:33177094 "At the periphery of the matrix, the motif on starch-binding proteins SAGA1 and SAGA2 mediates interactions between the matrix and surrounding starch sheath."].

### Photosynth Res 2023 (PMID:36656499; abstract only)
- In saga1 mutants, CAS-dependent Ci-transporter genes (HLA3, LCIA) are not expressed and CAS is mislocalized. This is an indirect (retrograde signalling) consequence of a disrupted pyrenoid, not a SAGA1 activity. No GO term is proposed from it.

### Hennacy et al. 2024 (Nat Plants PMID:39548241; preprint PMID:39211136): tubule biogenesis
- SAGA1 and MITH1 (homologues) together are necessary and sufficient for membranes to traverse the matrix. Neither protein alone does this in Arabidopsis, but the two together do [PMID:39548241 "These results demonstrate that SAGA1 and MITH1 together are sufficient to generate matrix-traversing thylakoid membranes in a heterologous system."].
- SAGA1 localizes to the matrix-traversing membranes and is enriched at their periphery, where sheet-like thylakoids become tubules. It localizes normally in a starchless sta6 background, so its localization does not depend on the starch sheath [PMID:39548241 "indicating that SAGA1 does not require starch for its normal localization"].
- SAGA1 co-pellets with membranes and binds MITH1 (IP-MS) and Rubisco [PMID:39548241 "SAGA1 was MITH1’s most-abundant specific interactor, and MITH1 was one of SAGA1’s most-specific interactors, indicating that the two proteins physically interact"].
- Mechanistic model: SAGA1 makes the first adhesive contact between the thylakoid and the matrix, and MITH1 extends it [PMID:39548241 "SAGA1 is necessary for the initiation of matrix-traversing membranes as recognized by CYN7 (Fig. 3m–o) and CAH3 (Extended Data Fig. 8)."].

### Crans et al. 2026 (PNAS PMID:42090253; preprint PMID:41659582): direct starch binding
- **Direct starch binding was measured.** A purified 10xHis-mVenus-2xSAGA1-CBM20 construct (a tandem copy of the SAGA1 CBM20) bound waxy maize starch granules, and the mVenus control did not. β-cyclodextrin and maltoheptaose competed with this binding [PMID:42090253 "We observed that both the 10×His-mVenus-2×SAGA1-CBM20 and the 10×His-mVenus-SAGA2-2×CBM20 proteins, but not a 10×His-mVenus control protein, bound to starch"].
- Caveat: the assay used an isolated, duplicated CBM20, not full-length SAGA1. This is ordinary domain-level IDA evidence for GO:2001070.
- SAGA1 is enriched at starch-tubule-matrix junctions, and SAGA2 covers the rest of the interface. SAGA1 and SAGA2 redundantly localize the starch sheath to the pyrenoid. The saga1;saga2 double mutant has no pyrenoid starch sheath, although starch still forms in the stroma [PMID:42090253 "suggesting that SAGA1 and SAGA2 function redundantly to localize starch sheaths to the pyrenoid"].
- The authors suggest that SAGA1 and SAGA2 prime starch granule initiation at the pyrenoid surface. This is a hypothesis built on binding to maltoheptaose. It is not a demonstrated initiation activity, so GO:0062052 starch granule initiation is not proposed.

### Atkinson/Chan et al. 2024 (PNAS PMID:38241434): Arabidopsis proto-pyrenoid
- SAGA1-mCherry rings the EPYC1-Rubisco condensate and recruits starch to it [PMID:38241434 "We found that SAGA1 did indeed recruit starch to the proto-pyrenoid condensate in Arabidopsis, including extended plate-like starch granules at the edge of the condensate."].

### Expansion microscopy preprint 2026 (PMID:42465278)
- SAGA1 forms narrow rings around the cylindrical tubules at their matrix entry sites, more peripheral than MITH1. This supports a pyrenoid tubule location.

## Decisions on the questions raised

1. **Was SAGA1 starch binding measured directly?** Yes. Crans et al. 2026 (PMID:42090253) did an in vitro pull-down of purified SAGA1 CBM20 (tandem construct) with starch granules and competition with β-cyclodextrin and maltoheptaose. GO:2001070 is therefore justified by experiment and no longer only by the InterPro mapping. I added a NEW IDA row and accepted the IEA. The module annoton text "direct starch binding by SAGA1 has not been measured" is now out of date.
2. **Pyrenoid tubule location (GO:0160223).** Supported. SAGA1 localizes along the matrix-traversing membranes, enriched at their periphery and entry sites (PMID:39548241, PMID:42465278), and co-fractionates with membranes. Added as NEW (IDA). I did not add a separate NEW for GO:1990732 pyrenoid, because pyrenoid tubule is part_of pyrenoid (a redundant ancestor). The matrix-starch interface role is captured at the pyrenoid level in core_functions.
3. **Process term for tubule/thylakoid biogenesis.** GO has no "pyrenoid tubule assembly" term. The closest is GO:0010027 thylakoid membrane organization.
   - Participation test. SAGA1 is not a substrate or a mere requirement. It physically binds both partners: Rubisco through its RBMs (Y2H; in vitro motif binding) and the membranes (co-pelleting, membrane localization in Arabidopsis). Its proposed role is to supply the adhesive membrane-matrix bond that pulls thylakoid membranes into the matrix. Together with MITH1 it is sufficient for this in a heterologous system. That is a structural contribution to the reorganisation step, comparable to the scaffold case, so the term passes.
   - Comparator check. Arabidopsis proteins that physically shape thylakoids, VIPP1 and FZL, carry GO:0010027 (IMP/IBA in QuickGO). The term is used for structural organisers.
   - Added as NEW (IMP + IDA from the reconstitution).
   - The remaining uncertainty is how SAGA1 binds membranes. It has no predicted transmembrane segment, so it may bind via a membrane protein or lipid.
4. **Molecular function for the tubule-initiation role.** The module asserts none. In core_functions I used GO:0043495 protein-membrane adaptor activity, because the published mechanism is a protein (Rubisco)-membrane adhesive bridge. This rests on direct Rubisco binding plus membrane association. Its weakest link is that the mode of membrane binding is uncharacterised, and this is flagged in the report.

## Not annotated
- Rubisco binding: no specific GO MF term exists, and GO:0005515 protein binding is uninformative.
- Retrograde regulation of CAS-dependent genes (PMID:36656499): an indirect effect.
- Starch granule initiation: a hypothesis only.
