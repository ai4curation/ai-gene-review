# ARG1 (Arginase-1, human, UniProtKB:P05089) — review notes

## Summary of function
ARG1 is the cytosolic, liver-type (type I) arginase, a binuclear manganese
metalloenzyme that catalyzes the terminal (fifth) step of the urea cycle:
L-arginine + H2O -> L-ornithine + urea (EC 3.5.3.1). It regenerates ornithine to
close the cycle and produces the urea that is excreted. It is a homotrimer, each
subunit binding two Mn(2+) ions. Beyond hepatic ureagenesis, ARG1 is
constitutively expressed in neutrophil granules and released during inflammation,
where local arginine depletion suppresses T-cell (and NK-cell) proliferation /
cytokine production — a myeloid immunoregulatory role. Loss-of-function variants
cause argininemia / arginase deficiency, a urea cycle disorder distinguished by
progressive spastic diplegia/paraparesis rather than the neonatal hyperammonemic
crises typical of proximal UCDs.

## Key verbatim citations

- Terminal urea-cycle step + disease:
  [PMID:3540966 "Arginase (EC 3.5.3.1) catalyzes the last step of the urea cycle in the liver of ureotelic animals. Inherited deficiency of the enzyme results in argininemia, an autosomal recessive disorder characterized by hyperammonemia."]

- Catalytic activity / Mn metalloenzyme:
  [PMID:17562323 "Arginase is a manganese metalloenzyme that catalyzes the hydrolysis of l-arginine to yield l-ornithine and urea."]
  [PMID:21728378 "Arginase is a binuclear manganese metalloenzyme that hydrolyzes L-arginine to form L-ornithine and urea"]
  [PMID:21728378 "Arginase I is a cytosolic enzyme found predominantly in the liver, and arginase II is a mitochondrial enzyme found at highest concentrations in the kidney."]

- Binuclear Mn cluster / structure:
  [PMID:16141327 "The ultrahigh-resolution structure of the human arginase I-ABH complex yields an unprecedented view of the binuclear manganese cluster"]

- Homotrimer / quaternary structure:
  [PMID:22959135 "Our study reinforced the role of Arg308 residue for assembly of the ARG1 homotrimer."]

- Neutrophil/granulocyte expression + azurophil granule + antimicrobial:
  [PMID:15546957 "in human leukocytes arginase I is constitutively expressed only in granulocytes"]
  [PMID:15546957 "arginase I is localized in azurophil granules of neutrophils and constitutes a novel antimicrobial effector pathway, likely through arginine depletion in the phagolysosome"]

- T-cell suppression via extracellular arginase / arginine depletion:
  [PMID:16709924 "arginase I is liberated from human granulocytes, and very high activities accumulate extracellularly during purulent inflammatory reactions. Human granulocyte arginase induces a profound suppression of T-cell proliferation and cytokine synthesis. This T-cell phenotype is due to arginase-mediated depletion of arginine in the T-cell environment, which leads to CD3zeta chain down-regulation"]

- CMTM6 interaction (ARG1 identified as MS interactor in a PD-L1/CMTM6 study; ARG1 itself not the paper's focus):
  UniProt: "INTERACTION WITH CMTM6, AND IDENTIFICATION BY MASS SPECTROMETRY" (RN[15], PMID:28813417).
  Paper abstract is about CMTM6 regulating PD-L1; ARG1 is one MS-detected CMTM6 co-precipitant.

- Sperm nucleus proteomics (HDA nucleus): PMID:21630459 is a bulk sperm-nuclear
  proteome catalog (403 proteins); ARG1 detection is a large-scale MS hit, not a
  dedicated study of nuclear ARG1 function.

## Disease (dismech Arginase_Deficiency.yaml)
"progressive spastic diplegia or paraparesis, seizures, intellectual disability,
and growth retardation... relatively infrequent hyperammonemia compared to other
urea cycle disorders." Neurotoxicity from arginine + guanidino compounds.

## GO term-definition checks (OLS)
- GO:0004053 arginase activity = "L-arginine + H2O = L-ornithine + urea" (exact MF). CORE.
- GO:0000050 urea cycle = full cycle; ARG1 does terminal step. CORE BP.
- GO:0016813 hydrolase acting on C-N linear amidines = PARENT of arginase activity
  (InterPro Mn-binding-site IEA); redundant/over-general vs GO:0004053 -> MODIFY.
- GO:0046872 metal ion binding = PARENT of GO:0030145 manganese ion binding;
  general -> MODIFY to GO:0030145 (which is verified, binuclear Mn cluster).
- GO:0006527 L-arginine catabolic process = verified BP (breakdown of L-arginine). ACCEPT.
- GO:0006525 arginine metabolic process = broader parent; keep (IBA/IEA).
- GO:0030145 manganese ion binding = binds 2 Mn2+/subunit. CORE MF (contributes_to).
- GO:0005829 cytosol = verified subcellular localization (arginase I cytosolic). CORE CC.
- GO:0005737 cytoplasm = parent of cytosol; keep.
- GO:0005576 extracellular region (IDA PMID:16709924) = neutrophil arginase released
  extracellularly; real but non-core (secondary immune role).
- GO:0035578 azurophil granule lumen / GO:0035580 specific granule lumen (Reactome
  neutrophil degranulation) = real neutrophil granule localization; non-core.
- GO:0005634 nucleus (HDA PMID:21630459) = bulk sperm-nucleus proteomics; likely
  not a functional nuclear localization -> non-core / over-annotated.
- GO:0070947 neutrophil-mediated killing of fungus (IMP PMID:15546957) = supported
  by fungicidal-activity paper; non-core immune role.
- GO:0042130 neg reg T cell proliferation (IDA/IBA PMID:16709924) = supported; non-core.
- GO:0060336 neg reg type II IFN signaling (IMP PMID:16709924) = downstream immune
  effect; keep as non-core.
- GO:0042832 defense response to protozoan / GO:0046007 neg reg activated T cell
  proliferation / GO:2000552 neg reg Th2 cytokine production (Ensembl GO_REF:0000107
  IEA from mouse Q61176) = orthology-transferred mouse immune roles; keep non-core.
- GO:0042127 regulation of cell population proliferation (ARBA IEA) = very general;
  over-annotated relative to the specific T-cell terms -> MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI CMTM6, PMID:28813417) = uninformative; MS
  interactor from a PD-L1 study -> non-informative binding, mark over-annotated.

## Deep research
falcon deep-research launched (`just deep-research-falcon human P05089 --alias ARG1`);
FAILED after 600s ("All providers failed" — falcon endpoint timeout). No
-deep-research-falcon.md file produced. Review grounded in the UniProt record, all 9
cached publications, and dismech Arginase_Deficiency.yaml. No DR file fabricated.


## 2026-09-28 source-scope correction and followup

This section supersedes the earlier nuclear carryover, generic-binding removal,
NK-cell specificity, IFN-signaling interpretation and manganese `contributes_to`
comments. All 38 original annotation source objects and three product records
are retained. The six cytoplasm/arginine-metabolism umbrellas remain core
annotations because they describe the same cytosolic catabolic activity at
broader resolution. One arginase activity core now connects that reaction to
the urea cycle and L-arginine catabolism; its binuclear manganese requirement is
part of the catalytic description, not a partial contribution to another
molecular function.

The nine canonical PMID abstracts were read in full. Local full-text availability
is true only for 21728378 and 28813417; these records were read in targeted
sections, not treated as proof of complete experimental inspection. Raw UniProt,
GOA and all existing publication/Reactome cache bytes are unchanged. The prior
failed Falcon attempt remains the actual provider history; no provider file was
authored. Three normal Reactome caches remain pending, so this draft is not a
completed source-closure claim.

### Human IFN-gamma production rather than response signaling

[PMID:16709924 original Blood article](https://ashpublications.org/blood/article/108/5/1627/132630/Suppression-of-T-cell-functions-by-human),
Results and Figure 6C–D, directly tests human T-cell cytokine output following
arginine depletion by granulocyte material or recombinant human ARG1.
The Figure 6C legend states: “Human PMN arginase suppresses T-cell IFN-γ synthesis by a posttranscriptional mechanism.”
The targeted original Methods/Results read distinguishes secreted protein
measured after 48 hours from transcript measurements. The existing IMP row is
refined to GO:0032689, negative regulation of type II interferon production;
GO:0060336 concerns regulation of the response pathway. These are distinct
endpoints. The original source/evidence/relationship are preserved. The short
quotation is from the publisher body, not the abstract-only normal cache.

### Target-specific uncertainties

The antiprotozoal and Th2 Ensembl transfers remain unresolved at the exact donor
experiment/transfer level. General human fungicidal or T-cell evidence does not
close those specific assertions. The independently read [mouse macrophage study,
PMID:19360123](https://pubmed.ncbi.nlm.nih.gov/19360123/) provides contextual Th2
corroboration, not a reconstructed Ensembl chain or a direct human assay. Its
official abstract was consulted; no normal cache was requested for that context.

For [PMID:28813417](https://pmc.ncbi.nlm.nih.gov/articles/PMC5706633/), the inspected
CMTM6 co-IP/MS Methods and Extended Data 6c point to a specific interaction
inventory. The ARG1 row of that inventory and Supplementary Table 1 have not
been adjudicated. The original ARG1–CMTM6 interaction stays UNDECIDED; neither
generic wording nor a missing body-text match makes it wrong. The prior MISCITED
judgment is withdrawn. For [PMID:21630459](https://pubmed.ncbi.nlm.nih.gov/21630459/),
the abstract reports microscopy-based nuclear purity above 99.9%. The ARG1
protein-table/peptide entry remains uninspected, so nuclear localization stays
UNDECIDED without speculation about cytoplasmic carryover or a requirement for
a known nuclear function.

### Catalysis and compartment boundaries

[PMID:21728378](https://pmc.ncbi.nlm.nih.gov/articles/PMC3150614/) contains human
arginase I inhibitor-binding and structural work, while its inspected enzyme
inhibition Methods use Plasmodium falciparum arginase. The human activity row is
retained using its established biochemical context; the parasite kinetic assay
is not relabeled as human. The title is reconciled to the normal cached Greek
alpha spelling. [PMID:17562323](https://pubmed.ncbi.nlm.nih.gov/17562323/) explicitly
reports assayed recombinant human enzyme, and
[PMID:3540966](https://pubmed.ncbi.nlm.nih.gov/3540966/) reports activity conferred
by the cloned human cDNA.

The neutrophil fungicidal and T-cell regulatory roles remain secondary to the
core hepatic catabolic role. Phagolysosomal arginine depletion is the proposed
antimicrobial mechanism in PMID:15546957. Its azurophil-granule localization does
not independently establish the separate Reactome specific-granule assertion.
That existing curated compartment is retained with the limited event-summary
scope explicit, rather than supported by an off-target granule quotation.

Official indexed records distinguish [normal ARG1 catalysis](https://reactome.org/content/detail/R-HSA-70569),
[failed ARG1 variant catalysis](https://reactome.org/content/detail/R-HSA-9956512),
and [ARG1 gene expression](https://reactome.org/content/schema/instance/browser/R-HSA-9959871).
For the last event, cytosol describes the protein output, not a transcriptional
activity of the ARG1 protein. Exact normal-cache recovery and its source check
remain pending. No NEW annotation is introduced by this followup.


## 2026-09-28 normal-source closure

The three pending normal Reactome records are now present after Source39 recovery.
Their canonical bytes were checked against the exact independently validated archive;
all three complete event summaries and human identity fields were read. This closes
the recovery hold recorded above. R-HSA-70569 explicitly names the cytosolic ARG1
trimer and its arginine-to-ornithine/urea reaction. R-HSA-9956512 describes deficient
variants and distinguishes candidate versus characterized members; R-HSA-9959871
describes TP53 repression of ARG1 expression. Those latter two short summaries do
not reproduce all participant/compartment fields of the earlier inspected official
graphs. Their location reasons retain that distinction and independent human
cytosolic evidence, without assigning normal activity to deficient variants or
transcriptional activity to the expression product.

All 38 decisions are now made, including four explicit unresolved claims whose
source-specific evidence remains uncertain. The three newly read records do not
change any action, product, core or original source assertion. The review status
is COMPLETE; this records completion of the audit, not resolution of every
biological uncertainty. Raw gene records and every prior cache remain unchanged.
