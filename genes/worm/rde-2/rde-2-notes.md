# rde-2 (RNAi-deficient-2 / MUT-8) — research notes

Gene: **rde-2** = **mut-8** ; ORF **F21C3.4** ; UniProt **Q19672** ; WormBase **WBGene00004324**
Organism: *Caenorhabditis elegans* (NCBITaxon:6239). Chromosome I.

## Identity (verified from UniProt record + literature)

- UniProt Q19672 names the protein "SH2 domain-containing protein" — this is an **automated
  (ECO:0000313, TrEMBL) name only**, and is almost certainly **spurious**. The primary structural
  paper explicitly states MUT-8 "has no previously annotated domains"
  [PMID:39188014 "MUT-8 has no previously annotated domains, and the mechanism by which it recruits MUT-7 to Mutator foci remains unclear"]
  and that it is largely intrinsically disordered
  [PMID:39188014 "MUT-8 is predicted to be mostly unstructured, except for a partially structured NTD that is connected to a structured CTD by a long, flexible linker"].
  There is NO evidence RDE-2 is an SH2-domain signaling protein. Do NOT propagate the "SH2 domain"
  name into functional claims.
- rde-2 and mut-8 were shown to be the same gene (F21C3.4) by allele sequencing/mapping
  [PMID:15653635 "F21C3.4 corresponds to rde-2/mut-8"; "the alleles of rde-2 and mut-8 contained lesions within this gene"].
- PDB **8Q66** (2.03 Å) covers the MUT-8 CTD (residues 322–567) in complex with the MUT-7 CTD
  (from the Busetto 2024 structure).
- Interacts (IntAct, NbExp=8) with **mut-7 / P34607**.

## KNOWN (well supported)

### Molecular function: bridging adaptor in the Mutator complex (structural, not enzymatic)
- RDE-2/MUT-8 is a **bridging adaptor**: its C-terminal domain binds the MUT-7 exoribonuclease CTD,
  and its N-terminal domain contacts the MUT-16 scaffold, thereby recruiting MUT-7 to Mutator foci
  [PMID:39188014 "MUT-7 carries a worm-specific insertion in MUT7-C, which acts as a binding platform for the nematode-specific factor MUT-8. MUT-8, in turn, directly contacts the Mutator scaffold MUT-16, recruiting MUT-7 to Mutator foci"].
- The MUT-7CTD/MUT-8CTD heterodimer was crystallized (PDB 8Q66); the interaction is direct and both
  full-length proteins co-migrate on SEC (Busetto 2024). MUT-8 CTD is insoluble without MUT-7
  ("MUT-8FL and MUT-8CTD are insoluble without MUT-7"), consistent with an obligate partner/adaptor.
- The direct MUT-7 <-> RDE-2 interaction was first shown by yeast two-hybrid + co-IP + relocalization
  [PMID:15653635 "we identified RDE-2 as another component of this complex"; the C-terminal part of MUT-7
  (aa 787-910) and most of F21C3.4 (aa 144-585) are required for the interaction; co-IP of MUT-7 with
  RDE-2 antibodies from wild-type but not rde-2(pk1657) cytosol]. NOTE: 2005 work localized the
  cytosolic MUT-7/RDE-2 complex to the cytosol; the 2012 germline work (below) localizes RDE-2 to
  perinuclear Mutator foci. Both are used — the informative, current CC is the Mutator focus.
- Genetically, mut-7 and rde-2 interact (dominant enhancement of mut-7(ne311) by rde-2(pk716))
  [PMID:15653635 "showing that mut-7 and rde-2 interact genetically and suggests that interaction
  between the two wild-type proteins is required for RNAi"].

### Biological process: secondary siRNA (22G-RNA) amplification / RNAi / transposon silencing
- rde-2 was defined as one of four RNAi-deficient complementation groups in the original Fire/Mello
  screen [PMID:10535731 — the rde-1 paper; the abstract foregrounds rde-1 and rde-4, but the full
  screen defined the rde-1..rde-4 groups including rde-2; the IMP annotations to
  post-transcriptional gene silencing / regulatory ncRNA-mediated silencing / meiotic chromosome
  segregation are attributed to this paper with WormBase variant WB:WBVar00090964].
- The MUT-7/RDE-2 complex acts **downstream of primary siRNA production and upstream of target RNA
  recognition** — i.e. in the amplification step [PMID:15653635 "Together these data hint at a role
  for the MUT-7/RDE-2 complex in the amplification step of the RNAi pathway in C.elegans"; "rde-2
  mutant animals do not produce detectable levels of siRNAs in vivo"].
- rde-2 is one of the six "mutator" genes whose products form perinuclear Mutator foci; loss of any
  mutator gene (including rde-2) causes substantial loss of RdRP-dependent secondary siRNAs
  [PMID:30036386 "mutations in any of the Mutator complex proteins (mut-2, mut-7, mut-14 smut-1,
  mut-15, rde-2, rde-8, or rrf-1) result in a substantial loss of the RdRP-dependent secondary siRNAs"].
- The Mutator focus is a platform for 22G-RNA amplification by the RdRP RRF-1
  [PMID:22713602 "We propose that the mutator proteins and RRF-1 constitute an RNA processing
  compartment required for siRNA amplification and RNA silencing"].

### Cellular component: perinuclear Mutator foci (germline)
- Each of the six mutator proteins localizes to perinuclear Mutator foci, adjacent to but distinct
  from P granules [PMID:22713602 "each of the six mutator proteins localizes to punctate foci at the
  periphery of germline nuclei. The Mutator foci are adjacent to P granules"].
- RDE-2 localization to Mutator foci depends on MUT-16 [PMID:30036386 "MUT-16 is required for
  localization of MUT-2, MUT-7, RDE-2, MUT-14, and MUT-15, all of which localize independently of
  one another except for MUT-7, which requires RDE-2 for localization"].
- Earlier biochemistry placed the MUT-7/RDE-2 complex in the cytosol (S100), not nucleus
  [PMID:15653635 "the MUT-7 and RDE-2 proteins are associated with each other in the cytosol, but
  not in the nucleus"] — this is the basis of the GO:0005829 cytosol IDA.

### Meiotic chromosome segregation / Him phenotype
- rde-2 (and mut-7) mutants show a high-incidence-of-males (Him) phenotype from X non-disjunction
  [PMID:15653635 "both mut-7 and rde-2 mutants show a high incidence of males (him) phenotype ...
  caused by non-disjunction of the X-chromosome"]. This is the basis of the meiotic chromosome
  segregation IMP; it is a downstream/pleiotropic consequence of losing germline small-RNA silencing,
  not evidence that RDE-2 acts directly in the meiotic segregation machinery.

## NOT known (genuine gaps)

1. **Molecular activity beyond adaptor bridging.** RDE-2/MUT-8 has no catalytic activity and no
   canonical folded domain family; whether the intrinsically disordered N-terminal/linker regions do
   anything beyond MUT-16 binding (e.g. RNA binding, condensate nucleation, regulation of MUT-7
   nuclease activity) is undetermined [PMID:39188014 "MUT-8 has no previously annotated domains, and
   the mechanism by which it recruits MUT-7 to Mutator foci remains unclear"].
2. **Full partner set within the Mutator complex.** Direct binary partners are established for MUT-7
   (CTD-CTD) and MUT-16 (via MUT-8 NTD). Whether RDE-2 directly contacts other mutator components
   (MUT-2/RDE-3, MUT-14, MUT-15, NYN-1/2, RDE-8, RRF-1) or only co-resides in the focus is not
   resolved; the deep-research/Uebel data place MUT-2/MUT-14/MUT-15 in a separate MUT-16 recruitment
   branch, implying no direct RDE-2 contact, but this has not been tested biochemically.
3. **Mechanistic role in amplification.** It is established that rde-2 loss abolishes secondary siRNA
   accumulation, but whether RDE-2's only contribution is to recruit/position MUT-7 (i.e. it is a pure
   structural bridge) or whether it also actively contributes to target-mRNA capture / RdRP templating
   is unknown.
4. **The "SH2 domain" annotation.** The UniProt protein name is an unverified automated assignment
   contradicted by the structural literature; there is no experimental support for SH2/phosphotyrosine
   signaling function.

## Reference correctness flags
- PMID:10535731 (rde-1 paper) is **abstract-only** in cache and the abstract does not name rde-2, but
  it is the paper WormBase cites for the rde-2 IMP silencing/segregation annotations (the screen that
  isolated all rde complementation groups). Per repo guidelines, do NOT REMOVE experimental IMP on the
  basis that the abstract foregrounds rde-1. Relevance MEDIUM (foundational screen), correctness
  VERIFIED for its role as the defining rde screen; supporting text for rde-2 specifics comes from the
  2005 paper.
- PMID:19123269 (interactome) is a high-throughput Y2H network paper; the rde-2 protein-binding IPI
  (with MUT-7 / P34607) is corroborated by the dedicated 2005 and 2024 studies.
- PMID:39188014 (Busetto 2024) is the key molecular-function reference (structure of MUT-8 CTD /
  MUT-7 CTD; PDB 8Q66). Full text cached. Relevance HIGH.
- Deep research: falcon report (rde-2-deep-research-falcon.md) completed (~19 min, 18 citations); its
  central claims (bridging adaptor; Mutator-foci localization; 22G-RNA amplification) are corroborated
  by the primary papers fetched here. perplexity-lite fallback failed (401 quota) — not used.
