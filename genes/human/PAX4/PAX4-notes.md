# PAX4 (human, O43316) review notes

Journal for the de novo review of human PAX4 (HGNC:8618), done for the
BGEEDB_EXPRESSION project (projects/BGEEDB_EXPRESSION.md). The mouse ortholog
review (genes/mouse/Pax4/) is the reference for consistency; this file records
where the human evidence is the same and where it differs.

## 2026-11-10: sources read

- UniProt O43316 (Swiss-Prot). Paired domain 5-131, homeodomain 170-229,
  transcription-repression region 278-350 (ECO:0000250 from mouse P32115).
  FUNCTION text on enteroendocrine differentiation is ECO:0000269 to
  PMID:37883554; the pancreatic FUNCTION text and the nucleus/chromosome
  locations are by similarity to mouse. Isoform 2 (Pax4V) is a dominant
  negative form from human insulinoma (PMID:11263967).
- Residue numbering: the clinical literature numbers residues on isoform 3
  (O43316-4, Ensembl ENST00000341640, which lacks residues 1-8 of the displayed
  sequence). So R192H (rs2233580) is Arg200His of the displayed O43316
  sequence (UniProt VAR_054885), and the MODY9 R164W of PMID:17426099 is
  UniProt VAR_054883 (Trp-172 of the displayed sequence). PMID:41475885 uses a
  third numbering (NP_001353039.1, 351 aa); I did not map its residues.
- Deep research (claude_code provider) read as leads only; checked claims are
  in its reference_review. One claim, that ChIP-qPCR found no direct PAX4-ARX
  interaction in enteroendocrine cells, could not be verified: the authors'
  commentary (PMID:38279896, cached in full) does not say it.
- Cached publications: full text for 28473536, 40614820, 42210309, 41475885,
  36595822, 36208030, 37175989, 26503027, 24951566, 19012751, and (fetched
  today) 37777536, 35108381, 15596543, 38279896. Abstract only: 37883554,
  9480859, 10967107, 33009794, 25483960, 10364449, 10567552, 10891400,
  11263967, 17426099 (fetched today).
- PubMed search used: `PAX4[ti] AND human` (91 hits) and `ZNF800
  enteroendocrine` (1 hit, PMID:37883554).

## Molecular function (with provenance)

- Active repressor on Pol II promoters, human data:
  - MODY9 variant study [PMID:17426099 "R164W segregated with diabetes in the
    family of the proband and in vitro studies showed that it impairs the
    repressor activity of PAX4 on the insulin and glucagon promoters"].
  - Autorepression through its own human promoter [PMID:10967107 "PAX4 itself
    has at least two high affinity binding sites within the promoter through
    which it exerts a strong negative autoregulatory effect"].
  - Isoform 2 antagonises it [PMID:11263967 "PAX4v reversed the wild-type
    PAX4 mediated repression of the insulin promoter in cotransfection
    assays"].
  - Knockdown in EndoC-betaH1 derepresses GCG [PMID:37777536 "loss of PAX4
    increased GCG transcript by 2.7-fold in shPAX4 EndoC-βH1 cells (Fig. 2h),
    consistent with PAX4 being a repressor of GCG expression"].
- Weak or context-dependent activation [PMID:15596543 "Pax4 transactivated the
  Bcl-xL and c-myc promoters, whereas its diabetes-linked mutant was less
  efficient"]. So GO:0000981 and GO:0006357 stay as sign-neutral umbrellas, as
  in mouse, and GO:0001227 is the core activity.
- Genome-wide binding: CUT&RUN of overexpressed tagged PAX4 in EndoC-betaH1
  [PMID:40614820 "Analysis using SEACR [30] identified 1,673 binding peaks"],
  including the insulin promoter [PMID:40614820 "The binding of PAX4 to the
  INS gene promoter is direct evidence for the importance of the gene in
  insulin secretion"]. This is the human evidence for GO:0000978 and chromatin.
- HT-SELEX (PMID:28473536) gives the GO:1990837 IDA. PAX4 is not named in the
  main text; the motif is in the supplementary data the curator read.

## Localization

- Nuclear in every human overexpression system tested:
  [PMID:40614820 "Western blotting and fluorescent microscope images confirmed
  nuclear localization and the overexpression of PAX4 in the EndoC-βH1
  cells"]; [PMID:41475885 "The results showed that WT PAX4 was uniformly
  distributed in the nucleus"]; [PMID:37777536 "Overexpression of the PAX4
  variants in AD293 cells confirmed that the p.His192 allele does not prevent
  nuclear localization"]; [PMID:33009794 "The aberrant PAX4 variants were shown
  to retain stability and nuclear localization."]. No endogenous-protein
  localization exists; ChIP-grade antibodies are lacking (PMID:40614820).
- Chromosome (UniProt SL-0468 mapping) is better captured as chromatin, as in
  mouse.

## Pancreatic beta-cell differentiation: human differs from mouse in degree

- Mouse: Pax4 is essential (nulls lack beta and delta cells and die).
- Human: contributes but is not essential.
  - Complete loss in two children gives transient neonatal diabetes
    [PMID:40614820 "demonstrating that in contrast to mouse models, PAX4 is not
    essential for the development of human pancreatic beta-cells"].
  - hiPSC knockout still makes SC-islets [PMID:37777536 "unlike in mouse,
    PAX4 is not essential for human beta cell differentiation in vitro"], but
    they are defective [PMID:37777536 "we found that PAX4 deficiency and/or
    loss-of-function to result in derepression of alpha cell genes, leading to
    the formation of polyhormonal endocrine cells in vitro, with reduced total
    insulin content"].
  - Re-analysis of the knockout endocrine progenitors [PMID:40614820 "human
    PAX4 expression is important for endocrine cell development and has a key
    role in directing progenitor cells toward a beta cell fate"], with ARX up
    [PMID:40614820 "large upregulation of ARX, one of the primary drivers of
    alpha cell fate specification"].
  - Gain of function in hESC-derived progenitors [PMID:25483960 "it did reduce
    the number of glucagon-positive cells and increased the number of
    unihormonal insulin-positive cells"].
- The ARX relationship is not uniform in human cells: ARX rises in PAX4-null
  endocrine progenitors (PMID:40614820) and falls with PAX4 overexpression
  (PMID:25483960), but falls with PAX4 knockdown in the EndoC-betaH1 beta-cell
  line [PMID:37777536 "loss of PAX4 led to a decrease in ARX expression in
  EndoC-βH1 cells"]. Whether PAX4 binds ARX regulatory DNA in human cells is
  not shown. Recorded as a knowledge gap.
- Decision: GO:0003309 IBA and ISS ACCEPT, as in mouse. The human data are
  direct (not only orthology), but they support a contributing role, so the
  core-function text says "biases progenitors toward" rather than "required
  for".
- R192H (rs2233580) knock-in mice are normal at birth and fail under high-fat
  diet [PMID:42210309 "Homozygote knock-in mice (Pax4 R192H) exhibited normal
  pancreatic endocrine development but developed glucose intolerance and
  impaired insulin secretion when fed a high-fat diet"]. This is mouse data plus
  a human cohort association; it supports adult beta-cell maintenance, which
  is not annotated in human GOA. I did not propose a NEW row (no human
  experimental data beyond association; the mouse review treated adult
  survival roles as non-core).

## Intestinal enteroendocrine fate (the human IDA rows)

- PMID:37883554 (Lin et al. 2023, Science): CRISPR knockout screen of all TFs
  in adult human small-intestinal organoids. Abstract only in cache. ZNF800
  restrains EEC commitment and directly targets a TF network centred on PAX4.
- The authors' commentary (full text) gives the PAX4 epistasis result
  [PMID:38279896 "only the knockout of PAX4 resulted in the reversal of EEC
  differentiation, shifting from ECs to other rare EEC subtypes"] and
  [PMID:38279896 "Furthermore, we unveiled a unilateral inhibition of PAX4
  towards ARX"] and [PMID:38279896 "indicating PAX4 is responsible for EC
  lineage specification by suppressing other lineages"].
- GO:7770019 and GO:7770020 were created from this very paper (their GO
  definitions cite PMID:37883554). The three IDA rows (repressor activity,
  negative regulation of EEC differentiation, EC differentiation) are ACCEPT.
  The repressor-activity row is accepted on deference to the curator's full-text
  reading plus independent human promoter-repression data (above); the cached
  abstract does not show direct ARX binding.
- Mouse agrees (PMID:22570716: serotonin cells are exclusively Pax4-dependent).
- Bgee: PAX4 is present in rectum (61.8), transverse-colon mucosa (61.4) and
  duodenum (51.9), its top non-testis tissues; this is the ENRICHED tier for
  GO:7770020, mentioned as corroboration only (project rule 2).

## Eye and brain IBA rows: arguing with the node

- `just paint-losses human PAX4`: no IRD or IKR on the lineage. No
  FamilyReview for PTHR45636 (entries, metadata and paint.tsv only).
- Same nodes as mouse. PAINT IBDs (interpro/panther/PTHR45636/PTHR45636-paint.tsv):
  - PTN002900580 (Euteleostomi): GO:0003309 (seeds MGI:97488 mouse Pax4,
    MGI:97490, RGD:3258, ZFIN pax6b); GO:0030900 (Pax6 seeds only); GO:0060041
    (Pax6 seeds, zebrafish pax10, and RGD:620433 rat Pax4, an IEP from
    PMID:19012751).
  - PTN008693041 (Bilateria): GO:0007420 (fly ey and toy, vertebrate Pax6);
    GO:0007423 (adds RGD:620433 and pax10).
- Human PAX4 sits on the same path as mouse in PANTHER 19: PTN002900580 >
  PTN009179984 (Tetrapoda DUP) > ... > PTN000676674 (Mammalia DUP) >
  PTN000676639 (mammalian PAX4 clade), per
  genes/mouse/Pax4/Pax4-bioinformatics/panther_tree_paths.md (row HGNC:8618).
  The PAX4/PAX6 split is drawn twice below PTN002900580 (Mammalia and
  Neopterygii), against the single 2R origin [PMID:24951566 "Our synteny
  analysis showed that Pax4, -6, and -10 originated in the 2R genome
  duplications early in vertebrate evolution."].
- Human-specific evidence added to the mouse argument:
  - Two children with complete PAX4 loss survive into childhood, and
    [PMID:40614820 "No extra pancreatic features were reported in either
    patient."]. In mouse this was borrowed human evidence; here it is the
    target species. It is a clinical report, not an ophthalmological or
    neurological examination, so it strengthens but does not settle the eye
    rows.
  - Bgee human: PAX4 has low fetal present calls in ganglionic eminence
    (RNA-Seq, 4th-5th LMP month, scores 42.5-48.0) and ventricular zone (50.6),
    which give the CONSISTENT tier for brain and forebrain development. This
    differs from mouse (adult Affymetrix plus one Theiler stage 21 in situ
    call). In the stage-merged calls all 39 forebrain entities with a PAX4
    call are absent (38 gold, hypothalamus silver), including the fetal cortical
    plate, while PAX6 is present in all but the olfactory bulb. These merge
    stages, so they do not exclude a fetal role. Low fetal presence is expression, not function
    (project rules 1 and 2), so it does not change the decision.
  - Bgee human eye: PAX4 absent from pigmented layer of retina (gold, 39) and
    palpebral conjunctiva (gold, 44), where PAX6 is present (89, 100). No
    neural-retina or pineal sample has a PAX4 call. Stage-merged, so
    consistency only for a developmental term.
- Decisions (same as mouse):
  - Brain development, forebrain development: REMOVE.
  - Retina development, sensory organ development: MARK_AS_OVER_ANNOTATED.
    Late photoreceptor maturation was untestable in null mice; in humans the
    survivors had no reported extra-pancreatic features, but no eye
    examination is described, so I kept the mouse action rather than
    escalating to REMOVE.

## Broad ARBA/TAS process rows

- GO:0048513 animal organ development and GO:0048731 system development
  (ARBA): both are ancestors of GO:0003309 (via part_of endocrine pancreas
  development; checked with OAK sqlite:obo:go), which this review accepts. So
  TOO_GENERAL, not MODIFY or MARK.
- GO:0009887 animal organ morphogenesis (TAS, PMID:9480859, a cloning paper):
  not an ancestor of GO:0003309. PAX4 allocates endocrine cell fates; it is
  not known to shape an organ. MARK_AS_OVER_ANNOTATED, as for the mouse TAS row.
  The cloning abstract itself frames PAX4 as a fate regulator [PMID:9480859
  "PAX4, a member of the paired box (PAX) gene family, is involved in the
  mechanism regulating the fate of pancreatic islet endocrine progenitor
  cells"].

## MODY9: contested, not used as functional evidence

- MODY9 (MIM:612225) rests on PMID:17426099 (Thai families; R164W segregated).
- Later evidence is against PAX4 as a MODY gene:
  [PMID:35108381 "Variant and gene-level genetic evidence does not support BLK,
  KLF11, or PAX4 as a cause of MODY."] and, in UK Biobank,
  [PMID:36208030 "the remaining 4 (CEL, BLK, APPL1 and PAX4) failed both
  criteria"]. The complete-loss paper agrees that heterozygous variants are
  unlikely to cause MODY but may raise type 2 diabetes risk (PMID:40614820).
- Case reports and new variants (PMID:36595822, PMID:41475885) report
  heterozygous variants in early-onset diabetes; PMID:41475885 adds that two
  missense variants destabilise the protein in MIN6 cells.
- None of the disease associations is used to support a GO term. The functional
  data used are the reporter, knockdown, knockout and CUT&RUN experiments.

## Terms checked with OAK (sqlite:obo:go)

- GO:0003309 ancestors include GO:0035883, GO:0031018, GO:0031016,
  GO:0048513 and GO:0048731.
- GO:7770019 regulates GO:0035883; GO:7770020 is_a GO:0035883; both defined
  from PMID:37883554.
- GO:1990837 is_a GO:0003690; GO:0000978 is a descendant of both (as recorded
  in the mouse notes).
- GO:2000227 negative regulation of pancreatic A cell differentiation is_a
  GO:7770019. Not proposed as NEW (descendant of a carried, accepted term;
  same decision as mouse).

## 2026-11-10: blinded OpenScientist check on retina development (GO:0060041)

Run in free-text function-assignment mode so that no review-chosen papers were passed: the prompt
held only "PAX4 has retina development in camera-type eye (GO:0060041).", the term, the fact that
the row is an IBA from a PANTHER/PAINT node, and GO_REF:0000033. It did not hold the review's
MARK_AS_OVER_ANNOTATED decision, its rationale, the Bgee report, or PMID:19012751 / PMID:24951566.
Report: `PAX4-hypotheses/function-hypothesis-go-0060041/openscientist.md` (3 iterations).

- Verdict agrees: [file:human/PAX4/PAX4-hypotheses/function-hypothesis-go-0060041/openscientist.md
  "Over-annotated / weakly supported — the term should NOT be retained as a confident PAX4
  function."] It recommends a PAINT-level fix or keeping the row as non-core and low-confidence.
- It found the decisive literature itself: the rat photoreceptor paper (PMID:19012751), the human
  complete-loss patients (PMID:40614820) and the Pax4-null ghrelin-cell phenotype (PMID:14970313).
  Spot-checked: the rat paper reports Pax4 "not detectable" in the embryonic or neonatal retina.
- It did not identify the zebrafish pax10 seed or that the rat IEP is itself a PAINT seed, both found
  by the mouse review.
