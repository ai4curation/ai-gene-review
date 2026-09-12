# DNAJC3 (p58IPK / PRKRI / ERdj6) research notes

UniProt: Q13217. 504 aa, precursor (signal 1-31). Domain architecture: 9 TPR repeats (37-373) +
C-terminal J domain (394-462). ER-resident HSP40/J-protein (ERdj6). Crystal structure 2Y4T/2Y4U.

## Dual function: BiP/HSP70 co-chaperone AND eIF2-alpha kinase (PKR/PERK/GCN2) inhibitor
- [UniProt FUNCTION "Involved in the unfolded protein response (UPR) during endoplasmic reticulum (ER)
  stress. Acts as a negative regulator of the EIF2AK4/GCN2 kinase activity by preventing the
  phosphorylation of eIF-2-alpha at 'Ser-52'... Co-chaperone of HSPA8/HSC70, it stimulates its ATPase
  activity. May inhibit both the autophosphorylation of EIF2AK2/PKR and the ability of EIF2AK2 to
  catalyze phosphorylation of the EIF2A. May inhibit EIF2AK3/PERK activity."]
- PKR inhibition (the original p58IPK function): [PMID:8576172 "protein inhibits both the
  autophosphorylation of PKR and the phosphorylation of the PKR natural substrate, the alpha subunit
  of eukaryotic initiation factor eIF-2"]; [PMID:8576172 "P58 is a member of the tetratricopeptide"
  family]. => GO:0004860 protein kinase inhibitor activity; GO:0019901 protein kinase binding.
- ER-stress inducible negative regulator of eIF2alpha: [PMID:12601012 "P58IPK, a novel endoplasmic
  reticulum stress-inducible protein and potential negative regulator of eIF2alpha signaling"].
- HSC70 co-chaperone: forms trimeric complex with DNAJB1 + HSPA8 (PMID:9920933); J domain mediates
  HSPA8 interaction. => GO:0051087 protein-folding chaperone binding.

## Disease
- [PMID:25466870 "Absence of BiP co-chaperone DNAJC3 causes diabetes mellitus and multisystemic
  neurodegeneration"] — ACPHD (MIM:616192): juvenile diabetes + ataxia + neuropathy + hearing loss.

## Localization
- ER / ER lumen — CORE (UniProt ISS; Reactome TAS; Ensembl IEA). Note J-domain topology and the
  classic cytosolic PKR-inhibition role mean DNAJC3 is reported in BOTH ER and cytosol.
- Cytosol / cytoplasm (ISS GO_REF:0000024 from mouse Q91YW3; IEA Ensembl; TAS PMID:8666242 cytoplasm;
  TAS Reactome cytosol). The original p58IPK literature is cytoplasmic (PKR is cytosolic). KEEP_AS_NON_CORE
  (genuine dual localization but ER is primary per current UniProt).
- Extracellular region / exosome / extracellular vesicle / azurophil granule lumen / membrane —
  secretome/HT proteomics (HDA, TAS Reactome neutrophil degranulation). KEEP_AS_NON_CORE.

## Caveats on IMP annotations (PMID:22064321)
- GO:1902010 neg reg translation in response to ER stress IMP and GO:0043066 neg reg apoptotic process
  IMP both cite PMID:22064321, which is about ERp29 inducing growth arrest with UPREGULATION of p58IPK
  — this is correlative (p58IPK is a downstream marker), not a direct DNAJC3 loss/gain perturbation
  defining these processes. The neg-reg-translation role IS well supported mechanistically (eIF2alpha
  kinase inhibition) so I ACCEPT/KEEP that term but note the apoptosis one is weakly grounded =>
  KEEP_AS_NON_CORE for apoptosis.

## MF/BP assignment
- Core MF: GO:0004860 protein kinase inhibitor activity (inhibits PKR/PERK/GCN2 eIF2alpha kinases).
- Core MF: GO:0051087 protein-folding chaperone binding / GO:0051787 misfolded protein binding +
  HSPA8 ATPase stimulation (co-chaperone).
- Core BP: negative regulation of translation / eIF2alpha phosphorylation in response to ER stress;
  protein folding in ER; UPR.
