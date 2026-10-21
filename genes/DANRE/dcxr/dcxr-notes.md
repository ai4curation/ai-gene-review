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

## Full re-review 2026-10-20 (independent of ProtNLM output)

This pass was done without consulting any ProtNLM prediction file. The two prediction-related
references (`dcxr-protnlm-source.json`, `dcxr-fabg-prediction-donor.json`) were dropped from the
review's reference list. The bioinformatics script now reads the Q567K5 sequence from
`dcxr-uniprot.txt` instead of the frozen ProtNLM source.

### Identity
Q567K5 is the canonical full-length zebrafish dcxr product (244 aa; ZFIN ZDB-GENE-030131-7002).
It is not an isoform, fragment or alternative gene model. It aligns end to end with human DCXR
Q7Z4W1 (244 aa; 169 identical residues). The Ser136/Tyr149/Lys153 triad and 12 of 14 NADP-contact
positions are identical; the other two are conservative (S38T) or surface (S185E) changes
(dcxr-bioinformatics/RESULTS.md).

### Evolutionary placement
- PANTHER: PTHR44252:SF3 "D-ERYTHRULOSE REDUCTASE-RELATED". Its Swiss-Prot members in the family
  entries list are chicken DER Q8JIS3 and C. elegans dhs-21 Q21929. SF2 "L-XYLULOSE REDUCTASE" holds the
  mammalian DCXRs; SF1 holds mammalian CBR2.
- Pairwise identity to Q567K5: chicken DER 0.701, human DCXR 0.693, mouse Dcxr 0.689, pig/mouse CBR2
  0.635/0.615, worm DHS-21 0.510. A neighbour-joining tree (rooted on SF1) groups Q567K5 with DER and
  DHS-21, consistent with PANTHER. SF3 therefore looks like the non-mammalian DCXR branch, not a
  functionally distinct paralog group.
- The IBA node PTN001211870 has donors from SF1 (MGI:107200 Cbr2), SF2 (human/mouse/rat DCXR) and SF3
  (WB dhs-21), so the propagated terms are ancestral to the clade containing Q567K5.
- SF3 has its own experimental anchor for the core activity: recombinant DHS-21 converts L-xylulose to xylitol
  with NADPH [PMID:21477590 "Recombinant DHS-21 was shown to convert L-xylulose to xylitol using NADPH as a cofactor."],
  and its carbonyl-reductase profile matches human DCXR [PMID:21300042 "revealed that SDR20C18 is the DCXR-orthologue enzyme to the human enzyme"].
- Chicken DER (closest characterized relative by placement and identity) reduces D-erythrulose and,
  per UniProt, may also reduce L-xylulose [PMID:12200544; PMID:7358641]. PAINT did not propagate a tetrose
  reductase term, and that omission is treated as deliberate; no NEW term is proposed.

### Annotation decisions (unchanged actions, re-argued)
- GO:0050038 L-xylulose reductase (NADPH) activity IBA: ACCEPT (core).
- GO:0004090 carbonyl reductase (NADPH) activity IBA: ACCEPT (core).
- GO:0005997 xylulose metabolic process IBA: ACCEPT. The enzyme catalyses the step itself.
- GO:0006006 glucose metabolic process IBA: KEEP_AS_NON_CORE. This is a uronate-cycle association. No valid
  more-specific descendant exists (GO:0019640 is obsolete; GO:0042840 is in another branch).
- GO:0016616 IEA (ARBA): MODIFY -> GO:0050038.
- GO:0005575 ND: ACCEPT. Relatives' compartments disagree (renal membranes and liver fractions in
  mammals, cytoplasm in chicken, spermatid plasma membrane in worm [PMID:21477590 "on the plasma membrane of spermatids"]).
  Second core function (GO:0004090) added.
- Worm dhs-21 longevity/reproduction phenotypes are organismal and were not transferred.

### Modules
No module in modules/ covers the uronate (glucuronate-xylulose) cycle. modules/xylose_oxidoreductase_pathway.yaml
is the fungal D-xylose route and does not include DCXR.
