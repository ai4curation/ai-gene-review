# AASS (human) — gene review notes

UniProt: Q9UDR5 (AASS_HUMAN); HGNC:17366; gene ID 10157; chromosome 7q31.3.
926 aa precursor; mitochondrial transit peptide (1..27); mature chain 28..926.

## Core biology (bifunctional enzyme)

AASS = alpha-aminoadipic semialdehyde synthase, mitochondrial. It is a **bifunctional**
enzyme (alias LKR/SDH) that catalyzes the **first two steps of the main (saccharopine)
pathway of L-lysine degradation** in the mitochondrial matrix:

1. **Lysine-ketoglutarate reductase (LKR, EC 1.5.1.8)** — N-terminal domain
   (region 28..476). Condenses L-lysine + 2-oxoglutarate to L-saccharopine using NADPH.
   UniProt CATALYTIC ACTIVITY: "L-saccharopine + NADP(+) + H2O = L-lysine + 2-oxoglutarate
   + NADPH + H(+)"; PhysiologicalDirection=right-to-left (i.e. lysine-forming direction
   is left, so physiological flux is lysine + 2-OG → saccharopine). RHEA:19373; EC 1.5.1.8.
   GO term: GO:0047130 saccharopine dehydrogenase (NADP+, L-lysine-forming) activity.

2. **Saccharopine dehydrogenase (SDH, EC 1.5.1.9)** — C-terminal domain
   (region 477..926). Oxidizes L-saccharopine to (S)-2-amino-6-oxohexanoate
   (= L-2-aminoadipate-6-semialdehyde / alpha-aminoadipic semialdehyde) + L-glutamate,
   reducing NAD+. UniProt: "L-saccharopine + NAD(+) + H2O = (S)-2-amino-6-oxohexanoate +
   L-glutamate + NADH + H(+)"; PhysiologicalDirection=left-to-right. RHEA:24520; EC 1.5.1.9.
   GO term: GO:0047131 saccharopine dehydrogenase (NAD+, L-glutamate-forming) activity.

Net: L-lysine + 2-OG + NADPH → saccharopine → alpha-aminoadipate-6-semialdehyde +
L-glutamate. This is the committed entry into lysine catabolism (steps 1/6 and 2/6 of
glutaryl-CoA from L-lysine; UniPathway UPA00868 UER00835/UER00836).

Structure: homotetramer (by similarity to mouse Q99K67). NAD-binding residues in SDH
domain resolved by crystallography (PDB 5L76/5L78/5O1N/5O1O/5O1P for SDH domain 455-926;
8DDA/8E8T/8E8U/8E8V for LKR domain). L-saccharopine-binding residues 577-578, 604, 703,
724-726 (by similarity to Q9P4R4).

Tissue: expressed broadly, highest in liver. Induced by starvation (by similarity).

## Disease

- **Hyperlysinemia type 1 / HYPLYS1 (MIM 238700)**: autosomal recessive; both AASS
  enzyme activities defective; increased serum lysine (+/- saccharopine); ~half of probands
  asymptomatic; generally considered a benign metabolic variant. [PMID:10775527]
- **Saccharopinuria**: patients retaining significant LKR but low SDH → saccharopine
  accumulation; few/no clinical manifestations. [PMID:463877]
- **DECRD (MIM 616034)**: AASS is one of the NADP(H)-dependent mitochondrial enzymes
  secondarily impaired when NADK2 is mutated (mitochondrial NADP(H) deficiency), producing
  hyperlysinemia alongside 2,4-dienoyl-CoA reductase deficiency. [PMID:24847004] (AASS is
  affected but the primary defect is in NADK2.)

## Annotation assessment

- **GO:0047130 / GO:0047131** (both MF activities): core. Supported by EXP (PMID:463877,
  enzyme assays in human fibroblasts/liver) and IMP (PMID:10775527, loss-of-function
  patient variant). ACCEPT. GO:0004753 (parent "saccharopine dehydrogenase activity", IBA):
  ACCEPT as a valid broader grouping.
- **GO:0004754** (saccharopine dehydrogenase (NAD+, L-lysine-forming) activity, ISS from
  Drosophila Q9VLX0): this is the *biosynthetic* direction SDH (yeast Lys1-type, lysine
  biosynthesis), NOT the human catabolic activity. Human AASS runs the catabolic SDH
  (GO:0047131, glutamate-forming) and the LKR/NADP+ reductase (GO:0047130). The
  L-lysine-forming SDH is the reverse (anabolic) reaction found in fungi. MARK_AS_OVER_ANNOTATED
  / MODIFY toward GO:0047131. (Kept conservative — ISS transfer picked the wrong catalytic
  direction for a catabolic mammalian enzyme.)
- **GO:0019477 L-lysine catabolic process** (IBA + IMP PMID:10775527): core BP. ACCEPT.
- Localization: **mitochondrial matrix (GO:0005759)** is the correct, well-supported
  compartment (Reactome TAS, Ensembl IEA from mouse, UniProt SUBCELL). GO:0005739
  mitochondrion (EXP PMID:463877, HTP PMID:34800366, TAS PMID:10567240, IEA) ACCEPT.
- **GO:0005737 cytoplasm** (IBA): broad but not wrong (matrix is within cytoplasm-ish
  parent); the phylogenetic call is conservative. Keep but non-core given the precise
  matrix annotation exists.
- **Drosophila-derived moonlighting ISS annotations** (all ISS, GO_REF:0000024, WITH
  UniProtKB:Q9VLX0 = D. melanogaster dLKR/SDH): GO:0000122 negative regulation of
  transcription by RNA Pol II, GO:0003714 transcription corepressor activity, GO:0042393
  histone binding, GO:0005634 nucleus, GO:0005829 cytosol. These transfer a fly-specific
  nuclear/transcriptional moonlighting role to human by sequence similarity. No experimental
  support in human; conflicts with the established mitochondrial-matrix metabolic role.
  MARK_AS_OVER_ANNOTATED (per policy, not REMOVE — ISS is an electronic-style transfer but
  the underlying fly biology is real; it is simply unvalidated/non-core for the human enzyme,
  and cytosol/nucleus contradict the matrix localization).

## Verbatim quote sources (for supporting_text)

- PMID:10775527 abstract: "The first two steps in the mammalian lysine-degradation pathway
  are catalyzed by lysine-ketoglutarate reductase and saccharopine dehydrogenase,
  respectively, resulting in the conversion of lysine to alpha-aminoadipic semialdehyde."
  and "we propose that AASS catalyzes the first two steps of the major lysine-degradation
  pathway in human cells and that inactivating mutations in the AASS gene are a cause of
  hyperlysinemia." and "an apparently bifunctional protein, with the N-terminal half similar
  to that of yeast LYS1 and with the C-terminal half similar to that of yeast LYS9."
- PMID:463877 abstract: "In all instances there was a deficiency in lysine-ketoglutarate
  reductase, saccharopine dehydrogenase, and saccharopine oxidoreductase activities."
  and "saccharopine oxidoreductase was partially purified from human liver ... The activity
  did not separate from that of lysine-ketoglutarate reductase or saccharopine dehydrogenase."
- PMID:10567240 abstract: "the bifunctional enzyme is likely to be a mitochondrial protein."
  and "both a bifunctional lysine-oxoglutarate reductase/saccharopine dehydrogenase and a
  monofunctional saccharopine dehydrogenase are likely to be present in this organ."
- PMID:34800366 abstract: "mitochondrial high-confidence proteome of >1,100 proteins
  (MitoCoP)".
- file: UniProt CATALYTIC ACTIVITY / FUNCTION / SUBCELLULAR LOCATION / DOMAIN sections.

## 2026-09-25 evidence-based re-review

This section supersedes the older annotation judgments above where they differ.
The 23 seeded annotation term/evidence/reference/qualifier tuples were preserved.
All annotations were reassessed; none was added. The two enzymatic reactions in
lysine degradation remain the two core functions. The human gene review is now
complete, with explicit unresolved evidence rather than unreviewed rows.

### Correct the cofactor, not the physiological direction

The old GO:0004754 rationale and proposed GO:0047131 replacement were incorrect.
QuickGO definitions were retrieved on 2026-09-25:

| Term | Cofactor pair | Products of saccharopine cleavage |
|---|---|---|
| GO:0004754 | NAD+/NADH | L-lysine + 2-oxoglutarate |
| GO:0047130 | NADP+/NADPH | L-lysine + 2-oxoglutarate |
| GO:0047131 | NAD+/NADH | L-glutamate + allysine |

[PMID:36128717](https://pubmed.ncbi.nlm.nih.gov/36128717/) directly assays human
full-length AASS expressed in HEK293 cells and isolated LOR domains. Both forward
and reverse reactions were measured, with the forward reaction faster. The
paper explicitly distinguishes human NADPH usage from yeast NADH usage. The
physiological catabolic direction does not invalidate a reversible reaction
whose GO name is written in the opposite direction. GO:0004754 therefore becomes
MODIFY to GO:0047130, the NADP-dependent LOR activity, rather than to the different
C-terminal SDH activity GO:0047131.

The fly source was independently traced in QuickGO: Q9VLX0 has GO:0004754 IDA
from [PMID:18695041](https://pubmed.ncbi.nlm.nih.gov/18695041/). Its full text
explicitly describes NADH oxidation by recombinant fly protein with lysine.
That source is not declared erroneous; its cofactor-specific transfer to human
is the problem. The donor paper's background statement that mammalian LKR cannot
run in reverse is superseded by the later direct human measurements. It is not
used as evidence against the human reverse reaction.

### Fly moonlighting: a supported donor with unresolved transfer

The full PMID:18695041 paper demonstrates fly dLKR/SDH histone H3/H4 binding,
EcR-B1 recruitment, inhibition of CARMER-mediated H3R17 methylation, promoter
occupancy, transcriptional repression and dynamic cytosolic/nuclear localization.
The donor genetic and cell assays are genuine. Its LKR domain supplies the histone
interaction; its SDH region supplies receptor interaction. Repression is
separable from metabolic catalysis. This is not histone demethylase activity.

The paper reports 51% sequence identity and 71% similarity to mouse and human
LKR/SDH. Human AASS retains both domains, so conservation is plausible. However,
the interaction surfaces were not mapped onto human AASS, the tested recruitment
context is EcR/Usp, and the donor's targeting mechanism is incompletely defined
(no nuclear localization signal was identified; partner-dependent shuttling was
suggested). These are specific unresolved transfer questions, not proof of a
lineage-specific loss. Human mitochondrial targeting does not exclude a conditional
nuclear or cytosolic pool. The old claims that these activities are necessarily
fly-specific or incompatible with mitochondria are withdrawn.

Accordingly, the five ISS annotations for transcriptional repression,
corepressor activity, histone binding, cytosol and nucleus are UNDECIDED with
UNRESOLVED propagation/source status. They are not removed or labeled proven
functional divergence. Their source Q9VLX0 and primary evidence are documented
separately from the human uncertainty.

### Localization and source tracing

- Cytoplasm GO:0005737 is ACCEPT. QuickGO defines it to include other subcellular
  structures, so a mitochondrial enzyme has this broader location. Broadness
  alone does not justify over-annotation. The three IBA rows trace to ancestral
  nodes PTN000123605 (cytoplasm, saccharopine dehydrogenase parent) and PTN000875308
  (lysine catabolism), not a count of donor proteins. Human AASS being an
  experimental descendant of the node is expected and is not circular evidence.
- The Ensembl matrix transfer traces to mouse Q99K67 and ENSMUSP00000031707.
  QuickGO gives mouse GO:0005759 IDA from PMID:18936211. Its abstract verifies
  murine hepatic Aass knockdown and lysine catabolism, but not the detailed
  localization assay. The curator-supported transfer is accepted in the context
  of convergent mitochondrial-pathway evidence; the inaccessible assay is stated.
- UniProt SL-0173 and EC/Rhea mapping sources agree with the accepted location and
  chemistry. ARBA predicates and the separate Ensembl accession chain were not
  independently reconstructed and their source statuses explicitly remain
  UNRESOLVED. All 13 propagation blocks contain actual traced source entities.
- Reactome R-HSA-70938 and R-HSA-70940 were retrieved with the repository's
  `cache_reactome_pathway` function. Both human reaction summaries explicitly
  place the AASS homotetramer in the mitochondrial matrix. The summaries are
  curated pathway evidence, not new direct human localization experiments.
- PMID:10567240 is a mouse study; its abstract says the bifunctional protein is
  *likely* mitochondrial. It also reports mouse starvation induction. The old
  description's unqualified human starvation-induction claim was removed.
- Supported full-text fetches for PMID:463877, PMID:10775527 and PMID:10567240
  were retried. XML access was restricted and HTML/PDF fallbacks did not recover
  full papers. The 1979 abstract supports human fibroblast enzyme deficiency and
  partial liver purification but says nothing about mitochondrial localization.
  Its EXP mitochondrial row is UNDECIDED, without rejecting the established
  mitochondrial role. Enzymatic rows supported directly in the abstract and by
  later human biochemistry remain ACCEPT. The validator's differing-action
  warning for mitochondrion is an intentional evidence-access distinction.

### Independent MitoCoP supplementary verification

The full PMID:34800366 manuscript and its publisher supplement were inspected.
The workbook was retrieved from:

https://ars.els-cdn.com/content/image/1-s2.0-S1550413121005295-mmc2.xlsx

This is Supplementary Table S1 (linked as mmc2.xlsx by the PMC article XML).
Downloaded workbook SHA-256:
`10690847c50567e11055d474fbe265fe5d699384f38437acd95734f0a87a9183`.
It was opened with `openpyxl.load_workbook(..., read_only=True, data_only=True)`;
row numbers below are one-based Excel rows, with headings in row 2.

| Sheet | Row | Protein Group ID(s) | Simplified protein IDs | Gene name | MitoCoP |
|---|---|---|---|---|---|
| (A) All protein groups | 5 | 11286 | Q9UDR5 | AASS | 1 |
| (B) MitoCoP (1,134 genes) | 5 | 11286 | Q9UDR5 | AASS | 1 |

Sheet (A) additionally has `Identified in this dataset = 1`, Ensembl gene
ENSG00000008311 and NCBI gene 10157. Sheet (B) classifies AASS under amino acid
metabolism. This verifies the specific human HTP target assignment, rather than
using the abstract's description of the overall dataset as if it named AASS.
The dataset establishes mitochondrial association; it does not by itself prove
matrix subcompartment or absence of any other pool. The unmodified 13.9 MB
workbook was inspected locally and is reproducibly accessible from its primary
source; it is not duplicated into the repository.

### Disease mechanisms and evidence limits

- Human gene identification (PMID:10775527), the patient series
  [PMID:23570448](https://pubmed.ncbi.nlm.nih.gov/23570448/) and the screened case
  [PMID:37927488](https://pubmed.ncbi.nlm.nih.gov/37927488/) establish biochemical
  hyperlysinemia from biallelic AASS defects. The 2013 series separates a possible
  PTPRZ1 contribution in a contiguous deletion from AASS biochemical deficiency.
  The 2023 child was doing well at 11 months: that limited follow-up does not
  establish lifelong penetrance or make all neurological findings causal.
- [PMID:30573525](https://pubmed.ncbi.nlm.nih.gov/30573525/) provides full primary
  worm/mouse evidence distinguishing selective LKR impairment from SDH impairment.
  Mouse R65Q elevates lysine without the severe phenotype; SDH G489E elevates
  saccharopine and causes mitochondrial damage, growth impairment and early death.
  The paper's human-AASS worm rescue used an engineered mitochondrial targeting
  sequence and is not an endogenous human localization experiment.
- [PMID:35135854](https://pubmed.ncbi.nlm.nih.gov/35135854/) is available here as an
  abstract. It reports mouse cerebral saccharopine/GPI-associated toxicity. The
  model findings contextualize the biochemical block; they do not support new
  direct human neuronal-development or mitochondrial-dynamics GO functions.
- [PMID:6434529](https://pubmed.ncbi.nlm.nih.gov/6434529/) is abstract-only. Its
  purification and tetramer inference concern baboon and bovine liver, not a
  full-length human structure. The 2022 human LOR structures provide published
  domain evidence. [PMID:42147163](https://pubmed.ncbi.nlm.nih.gov/42147163/) is
  explicitly a 2026 Research Square PREPRINT reporting full-length human
  structures and allostery; its primary text was inspected, but provisional
  allosteric regulation is not promoted into core physiology or a new GO term.
- The description now separates often mild biochemical hyperlysinemia from
  experimentally demonstrated saccharopine toxicity in animal models. It does
  not label every human saccharopinuria presentation either benign or severe.

### Workflow and verification

The annotation-reviewer and core-function-synthesizer procedures were applied.
Deep research and original-publication caching were launched concurrently. A fresh
virtual-environment installation race stopped the first research wrapper before
provider startup; once installation completed, Falcon was started with a
1200-second timeout. Perplexity was not retried because the project had already
observed HTTP 401 `insufficient_quota`. Provider output, if returned, is preserved
as generated and assessed separately from primary-source verification.

The repository-wide baseline had passed 4,975 gene reviews in the coordinator's
checkout. Targeted validation and a semantic comparison of the 23 original
annotation tuples are performed in this gene branch; shared project artifacts are
owned by the coordinator and are not changed here.

Falcon completed successfully in 546.14 seconds (provider metadata), produced its genuine report and artifact, and did not require fallback. Both files are retained unchanged. The report was read in full; its principal chemistry and animal-versus-human disease distinctions corroborate the independently checked studies. It is marked UNVERIFIED as an evidence source: its unnamed-journal Kopec 2017 report was not resolved to a primary publication; its additional 2000 full-text numerical claims and clinical-trial absence were not independently adopted. It also calls AASA the potentially channeled intermediate between the two AASS active sites, whereas that intermediate is saccharopine. Engineered targeting in worm rescue is not used to prove endogenous human localization. The report is not inserted into annotation supported_by fields merely to suppress the validator advisory.
