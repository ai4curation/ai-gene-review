# GALK1 (human) review notes

UniProtKB: P51570 · HGNC:4118 · Gene ID 2584 · Chromosome 17q25.1

## Core biology (verified)

GALK1 is the cytosolic ATP-dependent galactokinase that catalyses the **second step**
of the Leloir pathway (first *committed* / phosphorylation step of galactose catabolism):

- Reaction: alpha-D-galactose + ATP -> alpha-D-galactose 1-phosphate + ADP + H+ (RHEA:13553, EC 2.7.1.6)
- UniProt FUNCTION: "Catalyzes the transfer of a phosphate from ATP to alpha-D-galactose and
  participates in the first committed step in the catabolism of galactose."
  [ECO:0000269|PubMed:12694189, ECO:0000269|PubMed:7542884]
- Kinetic mechanism: ordered ternary complex, ATP binds first [PMID:12694189, PMID:14596685].
- KM ~970 uM galactose, ~34 uM ATP [PMID:12694189].
- Member of the GHMP kinase family, GalK subfamily [UniProt SIMILARITY].
- Homodimer [ECO:0000305|PubMed:15590630].
- Substrate specificity: strict at C4/C6 of the sugar ring; D-galactose and 2-deoxy-D-galactose
  are substrates, but D-glucose, D-fucose, L-arabinose, N-acetyl-D-galactosamine are NOT
  phosphorylated [PMID:14596685].

## Localization
- Cytosolic. In vitro translation shows the protein is cytosolic and NOT associated with the
  ER membrane [PMID:8908517] -> this is the basis of both the cytoplasm IDA and the NOT|membrane IDA.
- Reactome & IBA also place activity in cytosol (GO:0005829).
- HDA "membrane" (PMID:19946888, NK-cell membrane proteome) and "extracellular exosome"
  (PMID:19056867, urinary exosome proteomics) are high-throughput proteomic co-purifications;
  not the site of catalytic function. Note NOT|located_in membrane (IDA, PMID:8908517)
  directly contradicts the membrane HDA.

## Disease
- Deficiency -> Galactosemia type II (GALAC2, MIM:230200; MONDO:0009255 galactokinase deficiency),
  autosomal recessive. Hallmark = early-onset **cataracts** from galactitol accumulation in the
  lens via aldose reductase. Milder than classic (GALT) galactosemia; lacks the systemic
  hepatic/neuro toxicity. [dismech Galactosemia.yaml; PMID:3043741; PMID:12694189; PMID:14596685]
- Many disease variants characterized biochemically: P28T (Romani founder), V32M, G36R, H44Y,
  R68C, A198V (Osaka, mild), R239Q, G346S, G349S, T288M, A384P [PMID:12694189, PMID:15024738].

## Annotation review decisions (summary)
- Core MF: GO:0004335 galactokinase activity (EXP/IDA PMID:7542884, PMID:12694189; IBA; IEA) -> ACCEPT.
- ATP binding GO:0005524 (IDA PMID:12694189; IEA) -> ACCEPT (real cofactor/substrate, ordered mechanism ATP first).
- galactose binding GO:0005534 (IDA PMID:14596685) -> ACCEPT (substrate binding directly demonstrated).
- BP galactose metabolic process GO:0006012 (IBA, IEA, IMP) -> ACCEPT; GO:0033499 Leloir pathway (IEA, TAS) -> ACCEPT (more specific, correct).
- cytosol GO:0005829 (IBA, TAS x2) -> ACCEPT. cytoplasm GO:0005737 (IDA PMID:8908517, IEA) -> ACCEPT.
- NOT|membrane GO:0016020 (IDA PMID:8908517) -> ACCEPT (informative negation).
- membrane GO:0016020 (HDA PMID:19946888) -> MARK_AS_OVER_ANNOTATED (HT proteomics; contradicted by NOT IDA).
- extracellular exosome GO:0070062 (HDA PMID:19056867) -> KEEP_AS_NON_CORE (HT proteomics; not functional site).
- kinase activity GO:0016301, phosphotransferase alcohol acceptor GO:0016773 (IEA InterPro) -> MODIFY -> GO:0004335 (too generic parents).
- carbohydrate phosphorylation GO:0046835 (IEA) -> KEEP_AS_NON_CORE (correct but generic BP subsumed by galactose catabolism).
- protein binding GO:0005515 (IPI PMID:32296183, HuRI Y2H, PNRC2/Q9NPJ4) -> REMOVE (uninformative bare term; single HT Y2H interactor, no functional meaning for a soluble metabolic enzyme).
</content>


## 2026-11-02: current-context and primary-source reassessment

The current official record retains human P51570/GALK1, 392 residues and no declared alternative products. All 26 current contexts are preserved; the old 27th object was an authored NEW ancestor of the already present Leloir-pathway term and is now retired as redundant, with its entire object and all 23 old quotation associations archived. The original membrane IDA is NOT|located_in and remains negated; a preliminary private shorthand calling it positive was corrected before manual decisions.

The core remains ATP-dependent galactose phosphorylation in cytosol (PMID:7542884, PMID:12694189). Original human kinetics support ATP-first binding. NADH belongs to the coupled reporter assay. Selected original PMID:14596685 Results and Methods show robust 2-deoxygalactose activity in vitro; no physiological role is inferred. The human structure contains a nonhydrolysable ATP analogue and an engineered affinity-tag insertion (PMID:15590630). Crystal Cys391 dimers do not settle physiological assembly, and the earlier human study reports monomeric gel filtration with data not shown. The prior journal's categorical homodimer and absolute-specificity language is not carried forward.

Original PMID:8908517 Results/Figure 3 caption and Methods support soluble, non-microsomal GALK1 in the tested translation system. This does not refute every peripheral association in other cells. The independent YTS positive membrane context remains unresolved because its target table is unrecovered (PMID:19946888). Original urinary-exosome Table 1 and the authentic expanded table positively name GALK1; the association is retained as non-core, with the urine atom and explicit one-peptide/fractionation limits (PMID:19056867). The HuRI pair with Q9NPJ4 is verified from three original assay records; removing generic protein binding does not deny that observation (PMID:32296183).

Actual PAINT origins at AN0/PTN000048421 descend to the exact human AN489/PTN002470832 sequence, with no target-lineage activity loss. Typed ontology paths support the kinase, metabolic-process and cytoplasm refinements. Carbohydrate phosphorylation remains a true original process because no hierarchical path supports replacing it by the separately represented Leloir pathway. Official Reactome normal and mutant models are kept distinct, especially the FailedReaction 5610026 versus normalReaction 70355.

All 21 PMID assessments distinguish authentic abstract scope, selected full original reading and bibliography-only sequence/proteomics provenance. The compact source guide and archive expose exact original contexts, target rows and source locators. Private four-excerpt checks match retained caches; genuine native acquisition, source partition/title/access reconciliation, urine-atom restoration and target validation remain pending. No canonical GALK1 or normal source file has been written at this stage.

## 2026-11-02: genuine native reconciliation

The actual no-seed refresh preserves the inherited review while reconciling all 26 raw contexts, all 16 export columns and the genuine private 26-row seed. Canonical P51570 remains 392 residues, with no declared alternative products. The NOT-membrane context remains negated; the original urine atom is restored at native row 25 with the schema-correct flat BFO part_of projection. Only the separately archived redundant NEW is retired.

All 28 sources are present: 17 unchanged main sources, the exact published GALE R-HSA-70370 source and ten missing-only acquisitions. All 25 normal reference titles and four excerpts match their actual caches. New native PMID:10521295 full text was inspected selectively for mapping, variant and patient-activity context; no purified-mutant assay is inferred. Full-cache availability for the chromosome/proteome bibliography does not imply that target-specific tables were inspected. Existing external-original reading remains identified separately from normal abstract caches. Native EDIT history and targeted checks follow.

## 2026-11-02: targeted checks and finalization

Target validation passed with four advisories; strict GOA matching passed for all 26 original contexts, and the computed status is DRAFT. No NEW annotation was added. The advisories concern the current Leloir label versus an older cache label, optional propagation metadata, the differently signed membrane contexts, and one accepted row without a direct excerpt. They do not change the retained source-specific decisions. The initial INITIALIZED-versus-DRAFT status diagnostic is preserved and resolved by recording the computed status. All 28 scientific source files and the generated term cache remain unchanged after acquisition. Native EDIT history, private rendering/link checks and scoped whitespace checks accompany this candidate.


## 2026-11-04 — Primary evidence anchors and source-specific membrane uncertainty

The original experimental contexts remain distinct. PMID:8908517 tests translated human GALK1 with canine microsomes and supports the negative membrane context under those conditions. PMID:19946888 attempts to remove peripheral/nonintegral proteins from YTS membranes, but its abstract does not demonstrate complete removal and explicitly includes integral and stably associated proteins. Neither lack of a transmembrane segment nor the different negative assay identifies GALK1’s YTS fraction. The target-specific table, peptide and full assay context remain unadjudicated; the positive HDA row stays UNDECIDED.

Short primary findings are now quoted once and explicitly referenced by the relevant rows. They cover human activity, ATP-first mechanism, sugar recognition, structure, variant effects and the tested cytosolic/negative-membrane context. The full 22-word localization sentence replaces its clipped fragment without duplicating it in the core. The original urinary table remains the positive EV evidence; a cytosol quote is not evidence of EV membership. The core description now states only the biological reaction and compartment.

The categorical UniProt homodimer statement is recorded as a probable overstatement for upstream checking: the structure paper leaves physiological assembly unresolved and the earlier kinetic paper reports monomeric gel filtration with data not shown. No definitive monomer correction is asserted. Reference notes now emphasize biological judgments and inspected scope.

The compact evidence preserves all original raw fields, actual joins, NOT and urine extension, product sequence, PAINT/ontology/model and target-table evidence. The full older review/journal, all 23 historical quote associations and detailed access records remain available at the exact published 9fc2999 Git locator. All 26 actions, 28 source bytes and prior history remain unchanged. Ontology-loaded target validation passed without errors and retained three advisories: a cached GO label, optional IBA propagation metadata and the differently signed membrane contexts. Strict GOA matching passed for all 26 original contexts, and computed status remains DRAFT. Native EDIT history, private render/link checks and scoped whitespace checks passed. All 28 scientific source bytes and the derived term caches remain unchanged.
