# HSPB3 (Q12988) research notes

## Identity
- Heat shock protein beta-3 (HspB3 / HSP17 / HSPL27), small heat shock protein (HSP20/alpha-crystallin) family, 150 aa, ~17 kDa.
- "Most deviating of the six known human small heat shock proteins" with a unique N-terminal domain and essentially lacking a C-terminal extension [PMID:9858786 "Among the six known human sHsps it is evident that HspB3 is the most deviating one, having a unique N-terminal domain and essentially lacking a C-terminal extension."].
- Originally described as HSPL27 from a human heart cDNA [PMID:8972725 "Isolation and characterization of a human heart cDNA encoding a new member of the small heat shock protein family--HSPL27."]; HspB3 cDNA is the corrected version of HSPL27 [PMID:9858786 "We argue that the HspB3 cDNA sequence is a corrected version of the HspL27 cDNA."].

## Domain / structure
- Contains the conserved alpha-crystallin domain (sHSP domain, residues 47-150 per UniProt FT). PDB 6F2R (X-ray). InterPro/Pfam HSP20.
- Like other sHSPs, expected ATP-independent holdase activity (no ATPase; sHSPs hold unfolding clients in folding-competent state for downstream HSP70 refolding).

## Expression / tissue
- HPA: group enriched in heart muscle, skeletal muscle, tongue [file:human/HSPB3/HSPB3-uniprot.txt "HPA; ENSG00000169271; Group enriched (heart muscle, skeletal muscle, tongue)."]. Originally cloned from heart; smooth muscle mRNA detected by Northern [PMID:9858786 "Northern blot analysis shows that in smooth muscle tissue the cDNA hybridizes with mRNA of about 0.9 kb."].

## Function
- UniProt FUNCTION: "Inhibitor of actin polymerization." [file:human/HSPB3/HSPB3-uniprot.txt "FUNCTION: Inhibitor of actin polymerization."]
- Partners HSPB2 (MKBP); HSPB2/HSPB3 form a hetero-oligomeric complex in muscle (classic den Engelsman / Sugiyama work, PMID:10625651). Well established in field though primary text not cached here.
- Member of small HSP (HSP20) family [file:human/HSPB3/HSPB3-uniprot.txt "Belongs to the small heat shock protein (HSP20) family."].

## Localization
- UniProt: Cytoplasm and Nucleus; "Translocates to nuclear foci during heat shock." [file:human/HSPB3/HSPB3-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm ... Nucleus ... Note=Translocates to nuclear foci during heat shock."] — from PMID:19464326 (HSPB family localization survey).
- GOA: nuclear speck (IBA, IDA-HPA), nucleus, cytoplasm. The IBA "nuclear speck" is family-transferred (driven by HSPB7-type behavior in PMID:19464326 which actually studied HSPB7 SC35 speckle residence). For HSPB3 the experimentally documented compartments are cytoplasm + nucleus; nuclear speck has IDA (HPA) support.

## Disease
- Distal hereditary motor neuronopathy, autosomal dominant 4 (HMND4; MIM 613376); R7S variant [PMID:20142617 "Mutant small heat shock protein B3 causes motor neuropathy"; file:human/HSPB3/HSPB3-uniprot.txt VARIANT 7 "R -> S (in HMND4...)"].

## GO review reasoning
- Core MF: small-HSP ATP-independent holdase / unfolded-protein binding (chaperone). UniProt's specific molecular action listed is actin-polymerization inhibition; but the GO annotations present concern localization + "response to unfolded protein" (BP, TAS). Core function captured as chaperone (heat shock protein binding / holdase) supported by family membership + response-to-unfolded-protein TAS.
- "response to unfolded protein" (BP, TAS x2) — accept as core stress-response process for this sHSP.
- Localization terms: cytoplasm (accept), nucleus (accept), nuclear speck (keep-as-non-core; IBA transfer + HPA IDA, but the speckle residence is a hallmark of HSPB7 not robustly shown for HSPB3 as constitutive).
</content>
