# ASL (argininosuccinate lyase, P04424) — review notes

## Core enzyme function
ASL catalyzes the reversible cleavage of L-argininosuccinate to L-arginine + fumarate (EC 4.3.2.1;
RHEA:24020). It is the third/final step of the L-arginine biosynthesis branch and the second-to-last
step of the urea cycle (cytosolic).

- UniProt P04424 FUNCTION: "Catalyzes the reversible cleavage of L-argininosuccinate to fumarate and
  L-arginine, an intermediate step reaction in the urea cycle mostly providing for hepatic nitrogen
  detoxification into excretable urea as well as de novo L-arginine synthesis in nonhepatic tissues"
  (ECO:0000269 from PubMed:11747432, 11747433, 22081021, 2263616, 9045711).
- EC 4.3.2.1 established by direct enzyme assay in humans, e.g. [PMID:282632 "associated with a
  deficiency of argininosuccinate lyase (ASL; L-argininosuccinate arginine-lyase, EC 4.3.2.1)"].
- Homotetramer: [PMID:11747433 "Argininosuccinate lyase (ASL) is a homotetrameric enzyme that
  catalyzes the reversible cleavage of argininosuccinate to arginine and fumarate."]; first
  high-resolution human structure is the Q286R allele [PMID:11747432 "This is the first
  high-resolution structure of human ASL."]. Active sites are shared between tetramer subunits,
  the basis of the well-documented intragenic complementation in ASA patients.
- Lyase 1 family, argininosuccinate lyase subfamily; fumarase/aspartase (L-aspartase-like) superfamily
  (UniProt SIMILARITY + InterPro IPR008948 L-Aspartase-like, IPR000362 Fumarate_lyase_fam).

## Second, non-catalytic (structural) role: nitric oxide production
ASL has a well-documented structural role in assembling a NOS-containing multiprotein complex that
channels arginine to nitric oxide synthase; this is independent of catalytic activity.

- [PMID:22081021 "Mechanistic studies showed that ASL has a structural function in addition to its
  catalytic activity, by which it contributes to the formation of a multiprotein complex required for
  NO production."]
- Human catalytic-dead mutants retain the structural function: R236W "abolishes the enzymatic
  activity ... but does not abolish its tertiary structure"; overexpressing R113Q (catalytically dead)
  in ASA fibroblasts restored arginine-stimulated nitrite (NO) production. Loss of ASL, not loss of
  its catalysis, disrupts the NOS complex.
- Human ASA subjects show loss of NOS-dependent (flow-mediated) vascular relaxation but normal
  response to a NOS-independent NO donor (nitroglycerin), and reduced plasma RSNO/nitrite despite
  high plasma arginine — a systemic NO deficiency phenotype distinct from hyperammonemia.
- UniProt SUBUNIT: "Forms tissue-specific complexes with ASS1, SLC7A1, HSP90AA1 and nitric oxide
  synthase NOS1, NOS2 or NOS3; the complex maintenance is independent of ASL catalytic function"
  (partly By similarity to mouse Q91YI0).
- GOA term used is GO:0045429 "positive regulation of nitric oxide biosynthetic process" (IMP,
  PMID:22081021, human ASL) and an Ensembl-Compara ortholog-transfer IEA (GO_REF:0000107) of the
  same term from mouse Asl (Q91YI0). Both point to the same real biology.

## Disease
Argininosuccinic aciduria (ASA / ASLD; MIM 207900; MONDO:0008815), autosomal recessive, second most
common urea cycle disorder (~1 in 70,000; dismech kb/disorders/Argininosuccinic_Aciduria.yaml). Beyond
hyperammonemia, chronic ammonia-independent complications (neurocognitive, hepatic fibrosis, systemic
hypertension) are attributed in part to cell-autonomous NO deficiency (PMID:22081021).

## Localization
Cytosolic enzyme (GO:0005829). UniProt DR: cytosol IBA (GO_Central), cytoplasm TAS (ProtInc,
PMID:282632). Also detected in urinary exosomes by large-scale proteomics [PMID:19056867] — a
mass-spec location catalog finding, not a curated site of action.

## Annotation decisions summary
- Core: GO:0004056 (MF, EXP/IDA/IBA), GO:0000050 urea cycle (BP), GO:0006526 L-arginine biosynthetic
  process (BP), GO:0005829 cytosol (CC), GO:0042802 identical protein binding (homotetramer).
- Second core / non-core: GO:0045429 positive regulation of NO biosynthetic process (structural NOS
  role, PMID:22081021).
- MARK_AS_OVER_ANNOTATED: GO:0003824 catalytic activity (root MF, InterPro IEA) — too general; a
  specific EC 4.3.2.1 term (GO:0004056) is annotated.
- Bare GO:0005515 protein binding IPI (from high-throughput interactome/Y2H/AP-MS screens): not
  informative MF; the biologically meaningful self-association is captured by GO:0042802. Keep as
  non-core (evidence exists) but not core.
- GO:0070062 extracellular exosome (HDA, urinary exosome proteomics) — mass-spec catalog location,
  keep as non-core.
- GO:0006525 arginine metabolic process (IDA) — correct but general parent of the more specific
  GO:0006526; keep as non-core.
</content>


---

## Reassessment on 2026-09-28

The preceding notes are a historical record; the reassessment below supersedes conflicting scope or evidence claims.

# ASL reassessment notes — 2026-09-28

This is a working assessment, not a completed review. The existing human P04424 review has 31 authored rows, including a proposed scaffold annotation, and three alternative products. A separate deterministic seed restores 17 WITH/FROM lists and two distinct HuRI interaction assertions. All 31 prior row objects and decisions remain preserved in that preparatory file; the canonical review is unchanged. The existing falcon report is reused as background. Its selected functional sections were inspected; its mechanistic and evolutionary claims are not accepted without their primary evidence.

The complete abstract bodies of all 13 cited PMID caches were read. Full-text availability is distinct from complete reading of a paper. In particular, the cached structure papers 11747432 and 11747433 are abstract-only, while 22081021 contains body text. No source cache was edited. The ordinary PMID caching command succeeded using existing records. One normal fetch attempt for each missing Reactome record failed on DNS resolution and produced no file; those two normal records still need recovery.

ASL catalyzes argininosuccinate cleavage into arginine and fumarate. The human complementation experiments distinguish active-site restoration in mixed Q286R/D87G tetramers from stabilization involving M360T or A398D. Human COS-cell assays in 9045711 and 2263616 independently support the enzyme assignment. The abstract of 11747432 describes the Q286R structure and comparison with duck crystallins, but does not give the quoted 0.12 mM kinetic value. That value is recorded in UniProt and should not be represented as independently read from this paper's body. The existing two catalytic core entries can be combined into one function connected to both urea-cycle and arginine-biosynthesis processes. [PMID:11747432](https://pubmed.ncbi.nlm.nih.gov/11747432/), [PMID:11747433](https://pubmed.ncbi.nlm.nih.gov/11747433/), [PMID:9045711](https://pubmed.ncbi.nlm.nih.gov/9045711/), [PMID:2263616](https://pubmed.ncbi.nlm.nih.gov/2263616/).

The selected original Results section on NOS-complex maintenance in 22081021 was read in the normal cache. The species and experimental boundaries matter: mouse lung and brain immunoprecipitations address Nos3- and Nos1-containing assemblies, respectively. Human R236W ASL was tested in COS7 assembly assays. Human R113Q ASL was expressed in patient fibroblasts and restored arginine-stimulated nitrite production. These are distinct experiments, not two mutant proteins both tested for every outcome in human tissues. The paper supports a structural contribution beyond arginine-generating catalysis. It does not establish direct pairwise binding to every component or simultaneous inclusion of all three NOS paralogs in one universal complex. The selected Results and complete abstract were read, not all supplementary tables, figure pixels or methods. [PMID:22081021](https://pubmed.ncbi.nlm.nih.gov/22081021/).

The current GO definition of protein complex scaffold activity requires a structural component that holds a protein complex together. Its parent is structural molecule activity. The preexisting proposed MF can be assessed against the actual assembly/rescue experiments; this is not an inference merely from knockout necessity or from another protein having an annotation. If retained as a core scaffold function, the human NO-regulation annotation should have a consistent core decision rather than calling the same function both core and non-core. No new process term is being proposed. The local GO-CAM index has no exact UniProtKB:P04424 entry. [GO:0140378](https://amigo.geneontology.org/amigo/term/GO:0140378).

The current official Reactome pages were independently read. R-HSA-70573 describes the reversible reaction with a cytosolic human ASL tetramer catalyst. R-HSA-9956524 models loss of function of cytosolic ASL variant tetramers and links the normal reaction. These pages support the source identities and cytosolic context; normal cache recovery is still separate. No inference that all variant proteins preserve catalytic activity follows from the reaction's catalyst label. [Reactome:R-HSA-70573](https://reactome.org/content/detail/R-HSA-70573), [Reactome:R-HSA-9956524](https://reactome.org/content/detail/R-HSA-9956524).

The generic interaction rows need source-specific assessment. The restored supporting entities distinguish NTAQ1, MCMBP isoform 2 and TRIM3; a partner's isoform suffix is not an ASL isoform assignment. No target-specific high-throughput table was read at this stage. The homotetramer is independently supported, so self-association can be corroborated without claiming to have rechecked each screen. General binding should not be called false merely because it is nonspecific. The urinary-exosome target entry was not inspected; the existing claims of nonfunctional extracellular localization and bystander detection exceed the accessible evidence. Source-specific uncertainty should be retained without asserting contamination. [PMID:19056867](https://pubmed.ncbi.nlm.nih.gov/19056867/).

PAINT source nodes and descendant evidence must remain intact. Agreement with human experimental evidence supports the transferred functions but does not reconstruct the ancestral tree, and a human self-donor is not circular. The mouse NO-regulation transfer must retain its original donor chain even when the independent human study corroborates the function.

The working revision consolidates the two catalytic cores, retains the preexisting scaffold proposal with primary Results support, and makes nitric-oxide action decisions consistent with that second core. All 33 source objects and three alternative products are preserved. Publication awaits independent consultation and normal Reactome cache recovery.

Independent annotation consultation prompted two precision corrections: broad arginine metabolism is MODIFY to arginine biosynthesis, and the bioautography attachment was removed from the cytosol row because it does not demonstrate localization. The original all-33 prospective map records the earlier decisions.

The original Results label the fibroblast rescue mutant R113Q, while the indexed official Fig. 6c caption labels it R113W. The residue identity is reported here as stated in the Results; the within-paper discrepancy is unresolved and does not change the demonstrated catalytic-site-mutant rescue. Root and the independent reviewer read the indexed official PMC Fig. 6 caption; no figure pixels or supplementary Methods were inspected. The caption also identifies NOS3 and ASS antibodies in the COS7 experiment. [PMID:22081021, Fig. 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC3348956/).


### Final source closure

Both missing normal Reactome records are now recovered and were read in full. The earlier pending statements describe preparation and are resolved. The normal reaction summary explicitly places the ASL homotetramer in the cytosol. The variant summary distinguishes candidate from characterized mutant members; its compartment comes from the independently inspected official event/catalyst pages. The source files remain unmodified. The independent all-33 annotation consultation passed, including preservation of every source assertion and all three alternative products. The prospective consultation found 23 ACCEPT, 2 MODIFY, 7 UNDECIDED and one retained preexisting NEW scaffold molecular function; subsequent direct exosome evidence resolves one UNDECIDED as KEEP_AS_NON_CORE. No additional NEW assertion was introduced.

The [study-authored NHLBI Urinary Exosome Protein Database](https://esbl.nhlbi.nih.gov/UrinaryExosomes/) lists ASL NP_001020117 with one peptide and reference 2, explicitly linked to PMID:19056867. The root read this exact row and the reference mapping. The final exosome action is KEEP_AS_NON_CORE on direct target evidence. No claim of exosomal catalysis, contamination, peptide uniqueness or modern isoform assignment follows. Final totals are 23 ACCEPT, 2 MODIFY, 6 UNDECIDED, 1 KEEP_AS_NON_CORE and the retained NEW scaffold function.
