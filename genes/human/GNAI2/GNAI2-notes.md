# GNAI2 (Gαi2) review notes

## Provenance / process

- 2026-10-23: `just fetch-gene human GNAI2` had already been run. `just fetch-gene-pmids human GNAI2`
  cached all 24 GOA-cited PMIDs.
- Deep research (`just deep-research-falcon human GNAI2 --fallback perplexity-lite`) FAILED twice:
  falcon/Edison returned "Failed to authenticate" and the fallback provider `perplexity` was "not
  available" in this environment. No deep-research file exists; these notes and the review are built
  from the UniProt record, the cached publications, and a small number of additional primary papers
  fetched with `just fetch-pmid` (PMIDs 7663509, 8119955, 8327893, 20508603, 22459149, 22966200,
  25617475, 26976957, 27787898, 27912212, 39249692).
- Background paper PMID:42870023 (Deutsch et al. 2026, smFRET of Gαi α-helical domain opening in
  μOR–Gi complexes) was checked: the construct is human **Gαi1**, not Gαi2
  ("a previously published minimal cysteine background ... of human Gαi1"), and the WT heterotrimer
  is Gαi1β1γ2. GNAI2 is not assayed, so it is NOT cited in the GNAI2 review.

## Identity

- UniProt P04899, GNAI2_HUMAN, 355 aa, G-alpha family, G(i/o/t/z) subfamily; PANTHER PTHR10218:SF73.
- N-terminal myristoylation (Gly2) + palmitoylation anchor it to the cytoplasmic leaflet of the plasma
  membrane. Myristoylation is required for function: "Thus, myristoylation is required both for the
  function of constitutively active Q205L Gi alpha-2 and for receptor-mediated activation of wild type
  Gi alpha-2." [PMID:7961880]
- Isoform sGi2 (P04899-4) is an intracellular short form reported to sequester DRD2 (UniProt).

## Core biochemistry

- GTPase switch: "The transduction of signal depends on the ability of the alpha subunit to cycle
  between a GDP bound and an active GTP bound state capable of interacting with intracellular enzymes."
  [PMID:12359238]
- UniProt: "The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby
  terminating the signal." [file:human/GNAI2/GNAI2-uniprot.txt]
- Heterotrimer with Gβγ (GNB1/GNG2 in structures); Gα-GDP reassociates with Gβγ (Reactome
  R-HSA-751001: "The inactive G alpha (i):GDP complex has much higher affinity for the G beta:gamma
  complex and consequently reassociates.").
- Activated by liganded Gi-coupled GPCRs acting as GEFs (Reactome R-HSA-380073). Deactivated by RGS
  GAPs (Reactome R-HSA-8982020) and by effector GAP activity of adenylate cyclase (R-HSA-170686).

## Effector: direct adenylyl cyclase inhibition

- Purified Gi alpha subunits inhibit AC directly: "Concentration-dependent inhibition of adenylyl
  cyclases by purified Gi alpha subunits is described." [PMID:8327893]
- Isoform-specific: "Types V and VI adenylyl cyclase are most sensitive to inhibition by Gi alpha 1,
  Gi alpha 2, and Gi alpha 3" [PMID:8119955]. Human GNAI1 carries GO:0010855 adenylate cyclase
  inhibitor activity IDA from this paper, GNAI2 does not -> NEW proposal (comparator: GNAI1 IDA, GNAZ
  mouse IMP both carry it).
- Cellular: "Expression in JEG-3 cells of a mutationally activated Gi alpha-2 in which glutamine 205
  is replaced with leucine (Q205L) decreased forskolin-stimulated expression from the CRE-luciferase
  gene by up to 75%." [PMID:7961880]
- Human somatic F200L mutation in RVOT tachycardia: "This mutation was shown to increase intracellular
  cAMP concentration and inhibit suppression of cAMP by adenosine." [PMID:9637720]
- UNC5H2 (UNC5B) sequesters GTP-Gαi2: "The interaction of G(ialpha(2)) and UNC5H2 liberated adenylyl
  cyclase from G(ialpha(2)) inhibition." [PMID:12359238]
- Rat in vivo antisense: "antisense oligodeoxynucleotide treatment with Giα-2 but not Giα-3 restored
  enhanced inhibition of adenylyl cyclase by oxotremorine to WKY levels" [PMID:27912212] -- note this
  paper is the rat source of the GO:0007189 (adenylate cyclase-ACTIVATING pathway) IMP that is
  projected to human; the abstract describes AC inhibition, so the human IEA is a sign error.

## Receptor coupling (GPCR binding)

- μ-opioid receptor: "The etorphine-induced MOR translocation required the dissociation of the
  receptor from Galphai2 first and then the binding of beta-arrestin." [PMID:18599439]
- CXCR5: "Gαq/11/Gβ3/Gγ9 in LNCaP and Gαi2/Gβ3/Gγ9 in C4-2B and PC3 cell lines, were coupled to CXCR5
  and disassociated following CXCL13 stimulation." [PMID:23773523]
- UniProt also lists ADORA1, CNR1, FPR2, CXCR1/2 (cryo-EM structures for ADORA1–Gi2, CNR1–Gi2,
  FPR2–Gi2).

## Physiology (mostly mouse/rat; non-core, downstream of the switch)

- Immune: Gnai2-/- mice: "G alpha i2-deficient mice display growth retardation and develop a lethal
  diffuse colitis with clinical and histopathological features closely resembling ulcerative colitis
  in humans" [PMID:7663509]. B-cell chemokine responses: "Loss of a single allele of either Gnai2 or
  Rgs1 affected CCL19 triggered chemotaxis" [PMID:20508603]; RGS-insensitive G184S: "B cells carrying a
  Gαi2 (G184S/G184S) mutation that disables all RGS protein/Gαi2 interactions exhibit an unexpectedly
  severe reduction in chemokine receptor signaling" [PMID:25617475]; neutrophils: "We conclude that Gαi2
  controls arrest and Gαi3 controls transmigration and chemotaxis in response to chemokine stimulation
  of neutrophils." [PMID:26976957]; [PMID:22966200].
- Phagocyte NADPH oxidase: "The interaction between Gαi2 and p67 phox is direct and depends on the Gα
  activation state." [PMID:16782902] (preference for inactive Gαi).
- Endothelium/angiogenesis: "In various endothelial cell types, shRNA-induced silencing and
  CRISPR/Cas9-mediated knockout (KO) of Gαi2 resulted in substantial reductions in cell proliferation,
  migration, invasion, and capillary tube formation." [PMID:38505600]; NFAT activation.
- Metabolism: "G ialpha2 deficiency in adipose tissue and liver produces hyperinsulinaemia, impaired
  glucose tolerance and resistance to insulin in vivo." [PMID:8587610]
- Brain: cortical radial migration "Acute knockdown of the α-subunit (Gαi2) with in utero
  electroporation caused delayed radial migration of excitatory neurons during corticogenesis"
  [PMID:27787898]; human variants reported in periventricular nodular heterotopia [PMID:39249692,
  abstract not available in cache].
- Rat PVN: "brain Gαi(2)-subunit protein pathways mediate the natriuretic response to
  α(2)-adrenoreceptor activation in vivo" [PMID:22459149] (source of urine volume IEA).
- Cell proliferation (TSCC, miR-138 target): "we knocked-down GNAI2 in UM1 cells using specific
  siRNA, and demonstrated that the reduced GNAI2 level is associated with reduced cell proliferation"
  [PMID:21079996].

## Non-plasma-membrane pools

- Centrosome/midbody: "We show expression of G(ialpha1), G(ialpha2), and G(ialpha3) in the centrosomes
  and at the midbody." and "Giα1 and Giα2 localized in the centrosomes of interphase and mitotic cells,
  but Giα3 did not" [PMID:17635935]. Knockdown phenotype only with triple Gi1-3 siRNA: "Cells with
  reduced expression of all three Giα isoforms exhibited mainly cytokinesis defects." Overexpressed
  Gαi2 (WT or QL) had little effect.
- Exosome/EV proteomics (HDA) and NK membrane proteome: abundance-driven detections.

## Decisions summary

- Core: G protein activity / GTPase activity; adenylate cyclase inhibitor activity (NEW);
  adenylate cyclase-inhibiting GPCR signaling pathway; heterotrimeric G-protein complex at the
  cytoplasmic side of the plasma membrane; GPCR binding and Gβγ binding.
- Protein binding IPI rows: GPCR partners (OPRM1, CXCR5) -> MODIFY to GPCR binding; Gβ partners
  (GNB1, GNB2) -> MODIFY to G-protein beta/gamma-subunit complex binding; Y2H/other -> REMOVE
  (uninformative; not a statement that the interaction is false).
- Signal transduction / GPCR signaling / AC-modulating -> MODIFY to GO:0007193.
- GO:0007189 (AC-activating) -> MODIFY to GO:0007193 (sign correction).
- response to nutrient (TAS, insulin-action paper) -> REMOVE.
