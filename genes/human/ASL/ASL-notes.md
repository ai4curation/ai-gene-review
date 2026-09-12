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
