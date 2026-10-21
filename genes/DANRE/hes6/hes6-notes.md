# hes6 (Q6P0J1): evidence and exact-input prediction review

The three emitted GO predictions are biologically supported but broad. Direct zebrafish biochemistry establishes DNA binding by the Her7:Hes6 heterodimer, so a blanket claim that Hes6 cannot contribute to DNA binding would be wrong.

## Input identity and functional boundary

Q6P0J1 is zebrafish hes6/her13.2, a 226-residue product with bHLH and Orange domains. It is not her6 or her8a. The 2012 paper directly studies Hes6 alongside Her1 and Her7. The three generic protein-binding GOA rows have donors Her1/Q90463, Myod1/Q90477 and Her7/Q9I9K1 respectively; the separate identical-protein-binding row records Hes6 self-association. The primary paper includes MyoD as a promiscuous bHLH interaction comparison.

## Biological evidence

- [PMID:15905406 — Zebrafish hairy/enhancer of split protein links FGF signaling to cyclic gene expression in the periodic segmentation of somites.](https://pubmed.ncbi.nlm.nih.gov/15905406/): The primary reporter and interaction experiments establish transcriptional repression and Her1 association for Her13.2/Hes6.

> Her13.2 augments autorepression of her1 in association with Her1 protein.


> her13.2 is required for periodic repression of the
> Notch-regulated genes her1 and her7, and for proper somite segmentation.

- [PMID:16545363 — her1 and her13.2 are jointly required for somitic border specification along the entire axis of the fish embryo.](https://pubmed.ncbi.nlm.nih.gov/16545363/): The primary abstract explicitly reports combined Her1/Her13.2 loss-of-function effects on somitic borders.

> joint inactivation of her1 and her13.2 leads to a complete loss of all somitic
> borders

- [PMID:20637625 — Segment number and axial identity in a segmentation clock period mutant.](https://pubmed.ncbi.nlm.nih.gov/20637625/): The period-mutant study supports clock-dependent segment number; target identity is independently corroborated by the full 2018 report.

> precise control of segmentation
> clock period in relation to axial growth ensures a species-specific segment
> number


> arguing
> against an instructive role of the segmentation clock in determining axial
> identities.

- [PMID:22911291 — Topology and dynamics of the zebrafish segmentation clock core circuit.](https://pubmed.ncbi.nlm.nih.gov/22911291/): Direct zebrafish biochemistry establishes partner-dependent DNA binding by Hes6 in the Her7:Hes6 heterodimer.

> only Her1 homodimers and Her7:Hes6 heterodimers have strong DNA binding activity and target similar DNA sites.


> all of the possible dimers between Her1, Her7 and Hes6 form


> even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent

- [PMID:29624170 — Segmentation of the zebrafish axial skeleton relies on notochord sheath cells and not on the segmentation clock.](https://pubmed.ncbi.nlm.nih.gov/29624170/): The full primary report directly generates and analyzes a hes6 mutant; its focus on notochord-derived centra does not make the Hes6 annotation a wrong-gene citation.

> The novel hes6 mutation was created by injection of a TALEN targeted against hes6 in wild type.


> her1;hes6 mutants (n=15)

## Exact non-GO claims

The complete emitted record is preserved in [hes6-protnlm-source.json](hes6-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

UNSCORED: “Uncharacterized protein” has no ProtNLM evidence tag in the returned name field. It is an API default rather than a scored biological hypothesis.

## Emitted GO claims

All 3 emitted GO claims are individually assessed in [hes6-protnlm-predictions-review.yaml](hes6-protnlm-predictions-review.yaml).

## Family integration

Hairy/HES-family domains support dimer formation, but individual homo- and heterodimers differ strongly in DNA binding and regulatory effect. In zebrafish, Her7:Hes6 is directly DNA-binding while Hes6 homodimers are not in the tested assays. Neither a universal DNA-binding grant to every dimer nor a blanket non-DNA-binding label for Hes6 is appropriate. Somitogenesis and neurogenesis also require lineage- and tissue-specific evidence.

## Evidence limits

Full text was read for the 2005, 2012 and 2018 target studies, including the interaction controls and hes6-mutant figure captions. The 2006 and 2010 cache entries are abstract-only, with target relevance corroborated by the full later reports. The genuine Falcon research synthesis identifies useful clock studies; the conclusions here are anchored to the experiments themselves. Neural function remains unresolved rather than rejected because mesoderm is the best-studied context.

## Re-review 2026-09-29
- Audit of the earlier careful review: actions on the segmentation-clock rows stand. Filled the empty `reason` field on all 26 rows with row-specific arguments (the summaries already carried the evidence).
- Protein-binding policy applied to the three GO:0005515 IPI rows from [PMID:22911291 "all of the possible dimers between Her1, Her7 and Hes6 form"]: the Her1 (Q90463) and Her7 (Q9I9K1) rows remain MODIFY -> GO:0046982 protein heterodimerization activity; the Myod1 (Q90477) row changed KEEP_AS_NON_CORE -> REMOVE, because the paper uses MyoD only as a demonstration of promiscuous bHLH association [PMID:22911291 "even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent"] and no informative MF is supported for that pair; removal does not deny the observed interaction.
- Added the missing propagation_review to the UNDECIDED IBA GO:0050767 regulation of neurogenesis (node PTN000105428; fly and mouse donors support the source but zebrafish hes6 is studied only in the presomitic mesoderm [PMID:15905406 "her13.2 is required for periodic repression of the Notch-regulated genes her1 and her7, and for proper somite segmentation."]).
- Added reference_review for the two local support files and the deep-research file (one corroborating quote, "Hes6 alone showed no detectable binding to the tested E-box probes.", on the DNA binding IEA row), plus one suggested experiment on a possible neural role. Validation: 0 errors, 0 warnings.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 26 GOA rows, the description and the core functions against the cached primary papers (full text for PMID:15905406, PMID:22911291, PMID:29624170; abstract only for PMID:16545363, PMID:20637625, PMID:10976052) and against PANTHER/PAINT placement. No ProtNLM file or prediction-evidence folder was opened or used.

### Identity
- Q6P0J1 is the full-length zebrafish hes6/her13.2 product (226 aa; bHLH 19-71, Orange 90-123, C-terminal WRPW). It is not a fragment, isoform or alternative model; its length matches the 224-aa mammalian HES6.
- PANTHER 19.0 places it in PTHR10985:SF11 "TRANSCRIPTION COFACTOR HES-6" with human HES6 (Q96HZ4), mouse Hes6 (Q9JHE6), Xenopus hes6.1 and a second zebrafish gene, her13 (Q568A5). Kawamura et al. call mouse Hes6 "the only structural counterpart of her13.2" [PMID:15905406 "In mouse, in contrast to zebrafish, the only structural counterpart of her13.2, Hes6 , is not expressed in the PSM"].
- New analysis `hes6-bioinformatics/compare_sf11_rereview.py` (results in `RESULTS-rereview.md`): zebrafish hes6 and her13 are each about 0.58 identical to human HES6 and 0.61 to each other. They are co-orthologs, and pairwise identity cannot assign mammalian HES6 roles to one paralog over the other.

### Corrections made
- Nucleus (IBA and IEA): the earlier reason said no zebrafish Hes6 imaging was cached. That was wrong. PMID:22911291 used a Hes6 monoclonal antibody [PMID:22911291 "Antibodies show immunoreactivity with a nuclear antigen in wildtype, but not in hes6 mutant embryos."]. Both rows stay ACCEPT, now with that direct evidence.
- GO:0009952 a/p pattern specification (IBA): KEEP_AS_NON_CORE -> MODIFY to GO:0001756 somitogenesis. OLS parents show somitogenesis is_a GO:0009952, and hes6 is itself a seed of the PTN000105428 IBD. The term is true but general, and the gene already carries the specific child.
- GO:0046983 protein dimerization activity (IEA): ACCEPT -> MODIFY to GO:0046982 + GO:0042803. Both specific descendants are experimentally supported, and the old reason argued that the term was broad.
- GO:0045892 negative regulation of DNA-templated transcription (IDA, IGI): ACCEPT -> MODIFY to GO:0000122. The repressed targets are the RNA Pol II promoters of her1/her7 (8.6-kb her1 promoter reporter; nascent her1 intron transcripts), and the gene already carries GO:0000122 by IBA.
- GO:0050767 regulation of neurogenesis (IBA): still UNDECIDED, with new reasoning. HES6-subfamily orthologs promote neurogenesis [PMID:10976052 "When ectopically expressed in Xenopus embryos, Hes6 promotes neurogenesis."], so the propagation is phylogenetically plausible. However, no SF11 gene seeds the node, the Hes6 lineage acts with the opposite sign to E(spl), zebrafish retains two SF11 paralogs (so subfunctionalization is possible), and zebrafish hes6 has been tested only in the PSM.
- Description rewritten. It now covers FGF-dependent non-oscillating transcription, post-transcriptional protein oscillation, the short HLH loop, Her7:Hes6 DNA binding versus non-DNA-binding Her1:Hes6 dimers, and the period/segment-number phenotype.
- Core function 2 (heterodimerization) now records somitogenesis and nucleus.

### Unchanged after re-examination
- Somitogenesis (7 rows, IMP/IGI), all ACCEPT. Hes6 is a dimerization component of the clock's negative-feedback circuit. It directly binds the her1/her7/dlc promoters as Her7:Hes6 and sets the period [PMID:22911291 "Heterozgygous hes6 mutants have fewer segments than their wt siblings."]. This is participation, not a downstream phenotype.
- GO:0000978 and GO:0000981 IBA: ACCEPT. The function is real only in the Her7:Hes6 heterodimer, which is why core function 1 uses contributes_to.
- GO:0003677 -> GO:0000978 MODIFY. The GO:0005515 rows: Her1 and Her7 -> MODIFY to heterodimerization; MyoD -> REMOVE (a promiscuity control). GO:0042802 -> homodimerization. GO:0006351 and GO:0006355 -> GO:0000122. GO:0017053 ACCEPT. All kept.

### Family / modules / relative
- `interpro/panther/PTHR10985/PTHR10985-review.yaml` lists zebrafish Hes6 under a subfamily entry that says "No unverified PANTHER subfamily identifier is assigned". The PANTHER 19.0 classification files do assign it: PTHR10985:SF11. This is a disagreement of omission to raise with the family reviewer; the family file was not edited.
- Modules: `modules/notch_signaling.yaml` covers HES/E(spl) repressors as Notch outputs. Its framing does not fit hes6, which is FGF-induced and not Notch-regulated [PMID:15905406 "These results indicate that her13.2 functions downstream of FGF signaling in the PSM, but is not under direct regulation by Notch signaling"]. No segmentation-clock module exists.
- Relative to review next: mouse Hes6 (Q9JHE6), the same-subfamily (SF11) ortholog with the developmental experimental literature. No repo review exists for mouse Hes6 or human HES6 (Q96HZ4).
