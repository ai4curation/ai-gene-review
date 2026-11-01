# rab-5 (C. elegans, UniProt P91857) - manual literature synthesis

No deep-research provider was run for this gene (no API keys were available in the
review environment). This file is a manual synthesis written by the reviewer from the
cached publications in `publications/` and the UniProt record
(`rab-5-uniprot.txt`, an unreviewed TrEMBL entry). Every claim carries inline provenance.

## Identity and family

- RAB-5 (F26H9.6, WBGene00004268) is a 208-aa small GTPase of the Rab family; CDD places it
  in the Rab5-related subfamily [file:worm/rab-5/rab-5-uniprot.txt "Belongs to the small GTPase superfamily. Rab family."];
  [file:worm/rab-5/rab-5-uniprot.txt "cd01860; Rab5_related"].
- The entry is unreviewed; its protein name, EC number, catalytic-activity and
  subcellular-location lines are ARBA predictions and are not used as evidence here.
- Sequence features: P-loop (G1) GESAVGKS near the N-terminus, the conserved Ser33 whose
  S33N substitution gives the GDP-locked form, the DTAGQE switch-II motif containing Gln78
  (Q78L gives the GTP-locked form), and a C-terminal dicysteine prenylation motif
  [PMID:15895077 "RME-6 specifically interacted with RAB-5(S33N), which is a mutant form of RAB-5 expected to be locked in the GDP-bound conformation"].

## Nucleotide cycle and regulators

- GEFs: RME-6 (Vps9-domain protein, GAPVD1 homolog) binds GDP-bound RAB-5 and activates it at
  clathrin-coated pits; RABX-5 (Rabex-5) acts mainly on early endosomes
  [PMID:15895077 "RME-6 specifically interacted with RAB-5(S33N), which is a mutant form of RAB-5 expected to be locked in the GDP-bound conformation"];
  [PMID:15895077 "suggests that the primary function of RME-6 is to activate RAB-5 on the plasma membrane and in coated pits"];
  [PMID:15895077 "worm RABX-5 can interact with the putative worm Rab-5 effector RABN-5 as well as GDP-bound RAB-5 in yeast two-hybrid assays"].
- In rme-6; rabx-5 double loss, GFP::RAB-5 becomes cytosolic, i.e. GEF activity is needed for
  membrane association [PMID:15895077 "Strikingly, the punctate pattern of GFP::RAB-5 completely disappeared in rme-6(b1014) mutants depleted of rabx-5 by RNAi"].
- GAP: TBC-2 shows its strongest in vitro GAP activity on RAB-5, which measures RAB-5 GTP
  hydrolysis [PMID:20462958 "the strongest GAP activity on RAB-5 in vitro"].
- Rab conversion: SAND-1/Mon1 displaces RABX-5 to end the RAB-5 positive-feedback loop and
  recruits RAB-7 [PMID:20434987 "SAND-1/Mon1 as the critical switch for Rab conversion in metazoa"].
- Active RAB-5 recruits the PI3K complex that makes endosomal PtdIns3P
  [PMID:26783301 "GTP-RAB-5 is responsible for recruitment of the PI3K complex to early endosomes"].

## Localization

- Early endosomes (oocyte cortex, coelomocytes, intestine)
  [PMID:15895077 "In wild-type oocytes, GFP::RAB-5 is mainly localized to endosomes with a punctate appearance in the cortex"];
  [PMID:26783301 "early endosomes labeled by GFP-tagged RAB-5 (GFP::RAB-5) or RME-8 (RME-8::GFP) were significantly larger than in wild type"];
  [PMID:23840591 "In wild-type animals, RAB-5::GFP was enriched underneath the apical surface lining the gut lumen"].
- Phagosomes containing apoptotic cell corpses
  [PMID:22451698 "GFP::RAB-5 recruitment was prolonged from 67 ± 9 min in WT"].
- Periciliary membrane compartment at the base of sensory cilia
  [PMID:22342749 "RAB-5 endocytic proteins overlaps with a morphologically discrete periciliary membrane compartment"].

## Biological roles

- Receptor-mediated yolk endocytosis by oocytes; RNAi abolishes YP170::GFP uptake and is
  embryonic lethal [PMID:10588660 "YP170::GFP uptake by oocytes was completely abolished"];
  [PMID:10588660 "All progeny embryos of Ce-rab5 (RNAi) hermaphrodites died."].
- Endosome maturation: activated RAB-5(Q78L) phenocopies tbc-2 enlarged late endosomes
  [PMID:20462958 "Our data suggest that TBC-2 functions on late endosomes to"].
- Phagosome maturation during apoptotic cell clearance: RAB-5 acts upstream of RAB-7
  [PMID:22451698 "RAB-5 acts upstream of RAB-7 by tethering early endosomes and nascent phagosomes"].
- Dense core vesicle (DCV) release from motor neurons: rab-5 mutants are defective in DCV
  secretion but not synaptic vesicle exocytosis; RAB-5 acts with RAB-10 at the
  Golgi-endosomal interface during DCV sorting [PMID:23100538 "rab-5 and rab-10 mutants show severe defects in DCV"];
  [PMID:23100538 "the formation of release-competent DCVs requires a reciprocal exclusion cascade coupling RAB-5"].
- Early embryonic polarity: RAB-5 depletion perturbs cortical PAR-6 dynamics and actin
  organization [PMID:22545101 "depleting the early endosome regulator RAB-5 results in polarity-related phenotypes in the early embryo"].
- Partial requirement for EGL-17/FGF secretion from vulval precursors, interpreted by the
  authors as possibly indirect [PMID:16497226 "partially inhibited by RNAi of ce-rab-5"].
