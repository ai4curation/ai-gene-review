# CDK2 (P24941) — Research Notes

Human cyclin-dependent kinase 2 (CDK2 / CDKN2 / p33). 298 aa Ser/Thr protein kinase,
CMGC group, CDC2/CDKX subfamily. EC 2.7.11.22. Gene on chromosome 12.

## Core molecular function (kinase + cyclin partners)

- CDK2 is a proline-directed Ser/Thr protein kinase that is catalytically inactive as a
  monomer and is activated by binding a cyclin partner. The crystal structure of the
  cyclin A–CDK2–ATP complex showed: "CyclinA binds to one side of CDK2's catalytic cleft,
  inducing large conformational changes in its PSTAIRE helix and T-loop. These changes
  activate the kinase by realigning active site residues and relieving the steric blockade
  at the entrance of the catalytic cleft" [PMID:7630397].
- Full activation additionally requires CAK (CDK7/cyclin H/MAT1)-mediated phosphorylation
  of the activation (T-) loop at Thr160. Phosphorylation at Thr-14 or Tyr-15 inactivates;
  phosphorylation at Thr-160 activates: "the two major phosphorylation sites are Tyr15 (Y15)
  and Thr160 (T160)" and activity is governed by these [PMID:1396589]. UniProt ACTIVITY
  REGULATION: "Phosphorylation at Thr-14 or Tyr-15 inactivates the enzyme, while
  phosphorylation at Thr-160 activates it."
- Catalytic activity (UniProt): L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] +
  ADP + H+ (RHEA:17989); and the threonyl reaction; EC=2.7.11.22. Requires Mg2+ cofactor —
  binds 2 Mg2+ ions [PMID:21565702].
- Cyclin partners: cyclin E1/E2 (CCNE1/CCNE2) at G1/S; cyclin A2 (CCNA2; cyclin A1/CCNA1 in
  germ cells) at S/G2. Identified originally as the cyclin A- and adenovirus E1A-associated
  p33 kinase [PMID:1653904]. Cyclin A is required at two points in the human cell cycle
  (S-phase entry and mitosis) [PMID:1312467]. Cyclin E2 is a G1 cyclin and activating partner
  of CDK2 and CDK3 [PMID:9840943]. Atypical activator Speedy/RINGO (SPDYA) can activate CDK2
  independent of T-loop phosphorylation [PMID:28666995, "Interaction with SPDYA promotes
  kinase activation via a conformation change that alleviates obstruction of the
  substrate-binding cleft by the T-loop"].

## Inhibitors

- CIP/KIP family CDK inhibitors CDKN1A (p21) and CDKN1B (p27) bind and inhibit cyclin–CDK2.
  Crystal structure of p27Kip1 bound to cyclin A–CDK2: "p27Kip1 binds the complex as an
  extended structure interacting with both cyclin A and Cdk2" [PMID:8684460]. p21 cyclin-binding
  (Cy/RXL) motifs essential for function [PMID:8756624]; p21 structural disorder mediates
  binding [PMID:8876165]; p27 binds via sequential folding mechanism [PMID:15024385].
- KAP/CDKN3 (Cdi1) is a phosphatase that dephosphorylates pThr160 [PMID:8242750, PMID:11463386].

## Cell-cycle substrates / biological roles

- RB1: cyclin E/CDK2 phosphorylates RB1, releasing E2F (Reactome R-HSA-188390); part of the
  G1/S transition that drives the E2F transcriptional program and initiation of DNA synthesis.
- NPAT (p220): cyclin E/CDK2 phosphorylates NPAT in Cajal bodies to promote replication-dependent
  histone gene transcription at G1/S [PMID:10995387, "Cyclin E/Cdk2 acts at the G1/S-phase
  transition to promote the E2F transcriptional program and the initiation of DNA synthesis"].
- DNA replication: phosphorylates CDC6, ORC1, NPM1; promotes origin firing and centrosome
  duplication. Centrosome duplication & NPM1 (Cell 2000). Centriole duplication: CDK2 recruited
  by centriolar satellite microcephaly proteins [PMID:26297806].
- USP37: CDK2 phosphorylates and activates USP37 to antagonize APC/C-CDH1 and promote S-phase
  entry [PMID:21596315].
- EZH2: CDK1/CDK2 phosphorylate EZH2 at Thr350 to maintain H3K27me3 and epigenetic gene
  silencing [PMID:20935635].
- SUV39H1: CDK2 phosphorylates Suv39H1 at Ser391, causing dissociation from chromatin and
  regulating heterochromatin replication [PMID:24728993, "CDK2 phosphorylates Suv39H1 at Ser391
  ... results in preferential dissociation from chromatin"].
- NBN/NBS1: cyclin A/CDK2 phosphorylation status dictates telomere repair choice; telomere
  maintenance in response to DNA damage [PMID:28216226].
- ERCC6/CSB: cyclin A-CDK2 phosphorylates CSB at S158, required for its chromatin remodeling
  in DSB repair pathway choice [PMID:29203878, "cell cycle-dependent phosphorylation on S158
  by cyclin A-CDK2"].
- eEF2 (Thr57) by cyclin A-CDK2, regulating eEF2K inhibition [PMID:23184662].
- BRCA2 phosphorylation regulating homologous recombination [PMID:15800615 (UniProt)].
- AKT1/2 C-terminal phosphorylation promoting activation [PMID:24670654].
- MYC phosphorylation to suppress Ras-induced senescence [PMID:19966300 (UniProt)].
- DNA-damage checkpoint roles: G1/S checkpoint and DNA damage response in human ESCs
  [PMID:21319273]; p53-independent G2/M checkpoint (UniProt).

## Localization

- Nucleus and cytoplasm; centrosome (late G2, cyclin A/CDK2); Cajal body (NPAT phosphorylation);
  endosome (compartmentalized CDK2 with SHP-1/beta-catenin, insulin internalization
  [PMID:21262353]). UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome;
  Nucleus, Cajal body; Cytoplasm; Endosome.

## Knockout / redundancy notes

- Cdk2-null mice are viable; CDK2 is dispensable for mitotic cell cycle but essential for meiosis
  (UniProt FUNCTION: "essential for meiosis, but dispensable for mitosis"). CDK1 can compensate
  for CDK2 in the mitotic cycle (Malumbres & Barbacid review [PMID:19238148]). This argues the
  most defensible CORE function is the MF (kinase activity, cyclin binding) plus the canonical
  G1/S and DNA replication roles; many downstream BP annotations are real but non-core/context.

## Annotation strategy

- MF kinase terms (GO:0004693 cyclin-dependent protein Ser/Thr kinase activity; GO:0004674;
  GO:0106310 protein serine kinase; GO:0097472) — ACCEPT as core; well supported.
- GO:0030332 cyclin binding — ACCEPT core; defining feature.
- GO:0005515 protein binding — bare term; KEEP_AS_NON_CORE (uninformative but valid IPI;
  guidance says avoid endorsing as core; do not REMOVE valid experimental IPI).
- GO:0005524 ATP binding, GO:0000287 magnesium ion binding — ACCEPT (required for catalysis).
- Cyclin–CDK2 complex CC terms (GO:0000307; GO:0097123/4 A1/A2; GO:0097134/5 E1/E2) — ACCEPT.
- G1/S, DNA replication, positive regulation of DNA replication — ACCEPT/core.
- G2/M, regulation of mitotic cell cycle, APC/C regulation, senescence, centrosome/centriole
  duplication, telomere maintenance, heterochromatin/chromatin remodeling, NO response, Ras
  signaling (IEP), insulin/endosome — KEEP_AS_NON_CORE (real but peripheral/context-specific).
- IEA chromosome location terms transferred from mouse ortholog (telomeric region, condensed
  chromosome, X/Y chromosome) — KEEP_AS_NON_CORE; over-broad CC transfers, low specificity.
- protein binding (bare) GO:0005515 — avoid as core.
- protein domain specific binding GO:0019904 (p21/p27 docking) — KEEP_AS_NON_CORE.
- histone kinase activity GO:0035173 contributes_to (PMID:8692841, CAK/TFIIH context) —
  this is about CAK complex H1 kinase activity; MARK_AS_OVER_ANNOTATED (CDK2 is not a bona fide
  histone H1 kinase as a primary function; weak).
- Ras protein signal transduction GO:0007265 IEP (PMID:9054499) — IEP/senescence context;
  KEEP_AS_NON_CORE (correlative).
