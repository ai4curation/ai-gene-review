# Hif1a (rat, UniProt O35800) - manual literature synthesis

No deep-research API was available for this review; this file was compiled by hand from
the cached publications in `publications/` and the UniProt record
(`Hif1a-uniprot.txt`). Each statement carries its provenance.

## Identity and domain architecture

- Rat Hif1a encodes the 825-residue hypoxia-inducible factor 1-alpha (UniProt O35800,
  RGD:61928, GeneID 29560). The rat cDNA was cloned from primary hepatocytes and shown
  to be functional: [PMID:11237857 "All three cDNAs encoded functionally active proteins,
  of 825, 874 and 662 amino acids. After transfection they were able to activate
  luciferase activity of a luciferase gene construct containing three HIF-responsive
  elements."]
- Domains (UniProt FT lines): bHLH (17-70), PAS 1 (85-158), PAS 2 (228-298), PAC
  (302-345), oxygen-dependent degradation domain ODD (401-602), N-terminal
  transactivation domain NTAD (530-574), inhibitory domain (575-784) and C-terminal
  transactivation domain CTAD (785-825). Belongs to the bHLH-PAS family
  (PANTHER PTHR23043:SF7, InterPro IPR001321 HIF-1_alpha).

## Molecular function

- HIF-1 is an alpha/beta heterodimer. UniProt (by similarity to human Q16665):
  "Heterodimerizes with ARNT; heterodimer binds to core DNA sequence 5'-TACGTG-3' within
  the hypoxia response element (HRE) of target gene promoters".
- Rat brain experiments show heterodimerisation with ARNT1 and the neuronal ARNT2:
  [PMID:11029639 "We also identify two splice variants of HIF-1alpha in brain, one of
  which dimerizes with ARNT2 even more avidly than with ARNT1."]
- HRE binding and activation of rat target promoters: tyrosine hydroxylase
  [PMID:12675925 "induction of TH gene expression involves activation of the
  hypoxia-inducible transcription factors (HIFs) that interact with a specific
  hypoxia-responsive element (HRE) in the proximal region of the TH promoter"];
  frataxin in H9C2 cardiomyocytes [PMID:26071548 "Our promoter activity and chromatin
  immunoprecipitation assays confirmed the presence of a functional hypoxia response
  element in the frataxin promoter."]; enolase-1 in nucleus pulposus cells
  [PMID:20496369 "When HIF-1α is silenced, in both normoxia and hypoxia, there is
  significant suppression of enolase-1 promoter activity, a known HIF-1α target gene in
  nucleus pulposus cells (not shown)."].
- HIF-1 can also repress through HREs: [PMID:20496369 "We found that HIF-1 can bind to
  either of the HREs and can suppress promoter activity"].
- DNA-binding activity in rat cells: [PMID:18614764 "Near anoxic, but not hypoxic,
  conditions stabilized HIF-1alpha protein and provoked DNA binding activity"];
  supershift of the HRE complex by HIF-1alpha and HIF-1beta antibodies in neuronal
  cultures (PMID:10559391).
- Coactivator recruitment: Ref-1/APE1 and p300 co-immunoprecipitate with HIF-1 on the
  rat pulmonary artery endothelial VEGF HRE [PMID:15084519 "Co-immunoprecipitation
  experiments indicated that Ref-1/Ape present in nuclear extract interacted with HIF-1
  and p300 but not ATF/CREB."]. Recruitment of p300/CBP by the CTAD is blocked by FIH
  asparaginyl hydroxylation [PMID:21335549 "Asparaginyl hydroxylation blocks the
  recruitment of p300/CBP co-activators to a C-terminal activation domain in HIF-α."].

## Oxygen-dependent regulation (HIF-1alpha as a substrate)

- [PMID:21335549 "Prolyl hydroxylation at two sites within a central degradation domain
  promotes association of HIF-α with the von Hippel-Lindau ubiquitin E3 ligase and
  destruction by the ubiquitin-proteasome pathways."] The same study examined HIF-1alpha
  in rat kidney [PMID:21335549 "we studied HIF-1α from kidneys of rats that had been
  exposed to 0.1% carbon monoxide to create functional anemia"], showing that
  asparaginyl hydroxylation persists in vivo while the protein accumulates.
- p53-driven ubiquitination and degradation of HIF1A in rat H9c2 cardiac cells is
  reversed by Akt (PMID:19950214). These are regulatory inputs on HIF-1alpha, not
  activities of HIF-1alpha.

## Cellular location

- Nuclear in rat cells exposed to hypoxia or other inducers (PMID:18614764,
  PMID:18248612, PMID:22129453). UniProt: "Cytoplasmic in normoxia, nuclear
  translocation in response to hypoxia (By similarity)" and speckle localisation with
  HIF3A (by similarity to mouse).

## Biological roles in rat (mostly target-gene consequences)

- Cellular response to hypoxia: siRNA against HIF-1alpha abolishes purine-nucleoside
  protection of hypoxic PC12 cells and neurons (PMID:18248612); HIF-1alpha mediates
  hypoxic activation of the PNMT promoter, largely via Egr-1 and Sp1 (PMID:19220706).
- Angiogenesis/VEGF: knockdown impairs post-ischemic bmEPC homing and sprouting in rat
  brain [PMID:30052311 "the loss of HIF-1α resulted in deficient expression levels of
  VEGF-A, Flk-1, NRP1, and Dll4 in the ischemic brains, bmEPCs, and astrocytes"]; VEGF
  induction in astrocytes is only partly HIF-1alpha-dependent (PMID:18614764).
- Proliferation and apoptosis: HIF-1alpha knockdown suppresses hypoxic PASMC
  proliferation (PMID:16489407); HIF-1 inhibition promotes VSMC apoptosis via hexokinase
  2 (PMID:20498255); pharmacological HIF-1alpha suppression blocks hypoxia-induced
  myocyte apoptosis with Bnip3 (PMID:20224844).
- Many rat studies report only that HIF-1alpha mRNA or protein changes under a stimulus
  (cobalt, CO, cyanide, insulin, IL-1beta, estrogen, stretch, glucose, exercise, noise
  stress, etc.); they establish induction of Hif1a, not a step performed by it.
- One annotated study (PMID:30404558) concludes that suppression of stress granules in
  Hif1a shRNA cells is an RNAi artefact: [PMID:30404558 "SG formation was suppressed in
  heat shock transcription factor 1 (Hsf1) or hypoxia-inducible factor-1α (Hif1α)
  shRNA-transfected cells but not in Hsf1 or Hif1α-knockout cells, suggesting that RNAi
  per se (rather than gene deficiency) may account for the suppressive effect on SG."]

## Open questions

- Rat brain HIF-1alpha splice variants and the HIF-1alpha/ARNT2 dimer did not recognise
  the Epo HRE (PMID:11029639); the DNA sites and target genes of this neuronal dimer are
  unknown.
