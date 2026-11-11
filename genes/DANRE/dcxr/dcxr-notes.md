# dcxr (Q567K5): evidence and exact-input prediction review

The generic oxidoreductase prediction is correct but less precise than the established DCXR-like assignment. The function paragraph instead transfers a bacterial FabG fatty-acid-synthesis reaction across the SDR family, assigning a different substrate class and carrier-protein context.

## Input identity and functional boundary

Q567K5 is a 244-residue zebrafish dcxr product. It aligns without gaps to the 244-residue human DCXR Q7Z4W1, with 169 identical residues. All three reference catalytic positions 136, 149 and 153 are conserved, as are most annotated NADP-contact residues. The selected PANTHER assignment is PTHR44252:SF3, while human DCXR is SF2; the official SF3 label is D-ERYTHRULOSE REDUCTASE-RELATED. That label alone cannot overturn the conserved sequence and PAINT inference or establish an alternative substrate. The emitted donor Q9X248 is Thermotoga FabG.

## Biological evidence

- [PMID:11882650 — Molecular characterization of mammalian dicarbonyl/L-xylulose reductase and its localization in kidney.](https://pubmed.ncbi.nlm.nih.gov/11882650/): Purified mammalian DCXR proteins reduce alpha-dicarbonyls and interconvert xylitol and L-xylulose; this supports ortholog-based chemistry rather than a zebrafish assay.

> homotetramers with NADPH-linked reductase activity for alpha-dicarbonyl
> compounds, catalyzed the oxidoreduction between xylitol and l-xylulose


> which is involved in the uronate cycle
> of glucose metabolism

## Exact non-GO claims

The complete emitted record is preserved in [dcxr-protnlm-source.json](dcxr-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

UNSCORED: “Uncharacterized protein” has no ProtNLM evidence tag in the returned name field and provides no specific functional hypothesis. It is retained in the raw source rather than treated as a model-origin claim.

### Function

> Catalyzes the NADPH-dependent reduction of beta-ketoacyl-ACP substrates to beta-hydroxyacyl-ACP products, the first reductive step in the elongation cycle of fatty acid biosynthesis

PLI (CS 0; PARALOG_OVERANNOTATION). The donor is a bacterial FabG beta-ketoacyl-ACP reductase. Q567K5 instead has the full-length DCXR-like sequence and conserved catalytic architecture supporting soluble L-xylulose/carbonyl reduction. Related NADPH-dependent SDR chemistry does not establish ACP recognition or membership in fatty-acid-chain elongation. This is not a claim that animals lack all ACP-dependent fatty-acid synthesis; it is a distinction between the two enzyme branches. [PMID:11882650](https://pubmed.ncbi.nlm.nih.gov/11882650/); [sequence comparison](dcxr-bioinformatics/RESULTS.md); [donor](dcxr-fabg-prediction-donor.json).

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [dcxr-protnlm-predictions-review.yaml](dcxr-protnlm-predictions-review.yaml).

## Family integration

PTHR44252 includes related small-carbonyl reductases whose substrate boundaries need primary enzymology. Human and fish occupy different PANTHER subfamilies despite a gap-free alignment and conserved catalytic residues. The biological inference rests on the sequence plus experimentally characterized DCXR chemistry and the existing phylogenetic judgment, not on renaming the official family or assuming every SDR is FabG.

## Evidence limits

No purified Q567K5 assay or target-specific compartment study was found. The 2002 mammalian biochemical report is abstract-only in the cache but explicitly states the assayed substrates. The genuine Falcon synthesis is useful for ortholog enzymology, with cofactor preference, tetramerization and tissue distribution kept distinct from direct zebrafish measurements. No kinetic constants or exclusive physiological substrate are assigned.

Exact sequence mapping: [dcxr-bioinformatics/RESULTS.md](dcxr-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Re-review 2026-09-28

Audit of the existing review rather than a rewrite: the six GOA rows, their actions and their
supporting quotes were re-checked against the refreshed goa.tsv and uniprot.txt and all were
sustained (GO:0004090 ACCEPT, GO:0050038 ACCEPT, GO:0005997 ACCEPT, GO:0006006
KEEP_AS_NON_CORE, GO:0016616 MODIFY -> GO:0050038, GO:0005575 ND ACCEPT). No action changed
and no new GOA rows had appeared. What was missing was the argument, so each review block now
carries an explicit `reason` alongside its summary.

- The four IBA rows are argued on node placement rather than donor count, per the IBA policy.
  The node is PANTHER:PTN001211870; the activity behind it was measured on purified ortholog
  enzymes [PMID:11882650 "homotetramers with NADPH-linked reductase activity for alpha-dicarbonyl
  compounds, catalyzed the oxidoreduction between xylitol and l-xylulose"], and the zebrafish
  protein sits inside the clade that inherited it - gap-free alignment to human DCXR over 244
  residues with 169 identities and the catalytic positions retained (dcxr-bioinformatics/RESULTS.md).
  Absence of a zebrafish assay is not evidence of divergence.
- GO:0006006 glucose metabolic process stays non-core with the indirection spelled out: the
  enzyme acts on L-xylulose, not on glucose, and reaches glucose metabolism only through the
  uronate cycle [PMID:11882650 "which is involved in the uronate cycle of glucose metabolism"].
- GO:0005997 xylulose metabolic process is justified on the participation test: the gene product
  performs the L-xylulose-to-xylitol step itself, so it does work in the process rather than
  merely being required for it.
- The ND row for GO:0005575 is accepted with the reason stated: no zebrafish localization
  evidence exists [file:DANRE/dcxr/dcxr-deep-research-falcon.md "No direct zebrafish
  immunolocalization, cell fractionation, proximity-labeling, or fluorescent-tag study was
  found."], and the mammalian renal-tubule and liver-fraction observations are ortholog data
  that should not be transferred as a compartment annotation.
- reference_review on PMID:11882650 was already present and the HIGH/VERIFIED judgment is
  correct, but the note claimed the paper had been checked against "the cached abstract/full
  text" while the cache is abstract-only (full_text_available: false). The note now states the
  limit explicitly and records what the abstract does and does not support.
- Deep-research citations added where they carry information not already in UniProt (the
  absence of zebrafish localization data, the uronate-cycle pathway placement, the
  monocarbonyl-versus-dicarbonyl substrate preference, the unresolved cofactor preference).
- suggested_experiments added (the file had none): recombinant kinetics to fix the zebrafish
  substrate ranking and cofactor preference, given that reported diacetyl specific activities
  differ more than fiftyfold among mammalian orthologs; and a loss-of-function metabolomic test
  for L-xylulose accumulation.
- Validation: zero errors, zero warnings. Status already COMPLETE and unchanged.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not open or use any ProtNLM file or prediction-evidence folder. Sequences were
fetched directly from UniProt (`dcxr-bioinformatics/compare_sequences_rereview.py`, results in
`dcxr-bioinformatics/RESULTS-rereview.md`). The earlier `RESULTS.md` is left unchanged and its numbers
agree (169/244 identities to human DCXR).

### Identity of the benchmark accession

Q567K5 is the full-length 244-aa zebrafish dcxr product (TrEMBL, PE 2), the same length as human
DCXR Q7Z4W1 (244 aa). It is not a fragment, isoform or alternative gene model. It has the TGAGKGIG
Rossmann motif (residues 14-21) and the S136/Y149/K153 catalytic triad. Zebrafish has only one
PTHR44252 gene in PANTHER 19.0, and so does human.

### Evolutionary placement (the SF2/SF3 question)

- PANTHER 19.0 puts Q567K5 in PTHR44252:SF3 ("D-erythrulose reductase-related"). Human, mouse, rat
  and bovine DCXR are in SF2 ("L-xylulose reductase"). Mouse Cbr2 (lung tetrameric carbonyl
  reductase) is in SF1.
- The other SF3 members are Xenopus tropicalis dcxr (Q6P630), X. laevis dcxr.L, chicken DCXR
  (A0A8V1AB26) and chicken DER D-erythrulose reductase (Q8JIS3), C. elegans dhs-21 (Q21929) and
  Drosophila CG7322. SF3 is therefore the non-mammalian DCXR group (vertebrate and invertebrate),
  and SF2 is the mammalian lineage. It is not a clade with a different function.
- Pairwise identities of Q567K5: 69-70% to mammalian SF2 DCXR, 70-72% to the SF3 vertebrates, 61.5%
  to SF1 Cbr2, and 48-51% to the SF3 invertebrates (RESULTS-rereview.md). This is pairwise only, not a tree.
- The PAINT node PTN001211870 lists donors from all three subfamilies: MGI:107200 Cbr2 (SF1), the
  mammalian Dcxr/DCXR (SF2) and WB dhs-21 (SF3). The node is above the subfamily split.
- A same-subfamily characterised ortholog exists. Recombinant DHS-21 reduces L-xylulose with NADPH
  [PMID:21477590 "Recombinant DHS-21 was shown to convert L-xylulose to xylitol using NADPH as a cofactor."],
  and it was identified as the DCXR ortholog by substrate comparison [PMID:21300042 "revealed that SDR20C18
  is the DCXR-orthologue enzyme to the human enzyme"]. L-xylulose reductase activity is therefore
  established on both sides of the SF2/SF3 boundary and is not a subfamily-specific transfer.
- Chicken DER (SF3) is a purified NADPH-preferring D-erythrulose reductase [PMID:7358641 "was highly
  specific to D-erythrulose with an apparent Km of 0.38 mM"]. I did not propose erythrulose reductase
  activity (GO:0047880) as NEW. PAINT did not propagate it and chicken DER is not a donor. It is recorded
  as a suggested question.

### Changes to annotations

- GO:0050038 L-xylulose reductase (NADPH): ACCEPT (core). The reason now argues the SF2/SF3 placement
  explicitly.
- GO:0004090 carbonyl reductase (NADPH): ACCEPT. The donors span SF1 and SF3, and the activity is
  established in SF2 and SF3.
- GO:0005997 xylulose metabolic process: ACCEPT. The enzyme performs the step itself.
- GO:0006006 glucose metabolic process: changed from KEEP_AS_NON_CORE to MODIFY -> GO:0042840 D-glucuronate
  catabolic process. DCXR has no glucose substrate. It works in the pentose branch of glucuronate
  catabolism [PMID:40737316 "L-xylulose is then converted into D-xylulose-5P by the subsequent action of
  L-xylulose reductase (DCXR), sorbitol dehydrogenase (SORD), and xylulokinase (XYLB)."], and the mouse
  GO-CAM 6246724f00000078 models Dcxr L-xylulose reductase as part of GO:0042840. This is a lateral
  correction. The previous KEEP_AS_NON_CORE argued that the term tells a reader nothing about what the
  enzyme does, which is inconsistent with keeping it.
- GO:0016616 (ARBA IEA): MODIFY -> GO:0050038, unchanged.
- GO:0005575 ND: ACCEPT. The reason now notes that ortholog localizations conflict (mammalian renal
  brush-border membrane and cytosol in the mouse GO-CAM; spermatid plasma membrane for DHS-21).
- core_functions: a second core function was added for carbonyl reductase (NADPH). D-glucuronate
  catabolic process was added to directly_involved_in for the L-xylulose reductase function.
- Description rewritten to make the orthology and the evidence base explicit.
- References added: PMID:21477590, PMID:21300042, PMID:40737316, PMID:12200544, PMID:7358641, and
  file RESULTS-rereview.md. The two ProtNLM/FabG file references and RESULTS.md are kept, with
  review_notes saying they are no longer used as support.

### Relative, family review, modules

- Relative: human DCXR (Q7Z4W1), the 1:1 ortholog (a single PTHR44252 gene in each genome) and an
  experimental donor to PTN001211870. It is in SF2, not SF3. The closest same-subfamily characterised
  ortholog is C. elegans dhs-21 (Q21929). The repo has no review of DCXR, Dcxr or dhs-21.
- Family review interpro/panther/PTHR44252/PTHR44252-review.yaml agrees on the SF3 placement. It lists
  only Q567K5 as the SF3 representative. It could add dhs-21 and chicken DER as characterised SF3
  members, which would show that SF3 is the non-mammalian DCXR group rather than a functionally
  distinct one. I did not edit it.
- Modules: no animal glucuronate/pentose-pathway module exists. modules/xylose_oxidoreductase_pathway.yaml
  covers fungal and bacterial D-xylose catabolism; it is related chemistry but does not include DCXR.
  Mouse GO-CAM 6246724f00000078 (glucuronate catabolism to xylulose 5-phosphate) contains Dcxr.
