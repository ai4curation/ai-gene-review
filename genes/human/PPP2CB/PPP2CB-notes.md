# PPP2CB Review Notes

## Gene Identity

PPP2CB (UniProt P62714) encodes the catalytic subunit beta isoform of protein phosphatase 2A (PP2A-beta, PP2Acbeta). It is the minor catalytic isoform of PP2A, with PPP2CA being the major isoform (~10x more abundant in most tissues). The two share ~97% sequence identity [deep-research-falcon, goguetrubio2020, "~97% sequence similarity/identity reported in multiple authoritative reviews"].

## Core Function

PPP2CB is a metal-dependent serine/threonine phosphoprotein phosphatase (EC 3.1.3.16). It uses a bimetallic Mn2+ active site to hydrolyze phospho-serine and phospho-threonine bonds on protein substrates [PMID:10318862, deep-research-falcon].

The protein functions as the catalytic subunit of the heterotrimeric PP2A holoenzyme complex, consisting of:
- A (scaffold) subunit (PPP2R1A or PPP2R1B)
- C (catalytic) subunit (PPP2CA or PPP2CB)
- B (regulatory) subunit (multiple families: B/B55, B'/B56, B'', B''')

Regulatory B subunits determine substrate specificity and subcellular localization. Combinatorial assembly yields >70-90 distinct PP2A holoenzymes [deep-research-falcon, nasa2020].

## Regulation

- C-terminal Leu-309 methylation by LCMT1 (reversed by PME-1/PPME1) controls B subunit selection [PMID:8206937, "carboxyl-methylated in vivo...Methylation of PP2Ac subunit, in vitro, increases its activity toward both phosphorylase a and a phosphopeptide"]
- PTPA activates latent phosphatase; alpha4 (IGBP1) protects monomeric C subunit [PMID:9647778, "alpha 4 associates constitutively with the catalytic subunits of PP4, PP6, and both isoforms of PP2A"]

## Subcellular Localization

PPP2CB is predominantly cytoplasmic and nuclear [deep-research-falcon, baskaran2018, "Cbeta (PPP2CB) is predominantly cytoplasmic and nuclear"]. During prometaphase, localizes to centromeres; during mitosis, found at spindle poles [UniProt subcellular location, PMID:16541025].

## STRIPAK Complex

PPP2CB is part of the STRIPAK complex [PMID:18782753, "STRIPAK contains the PP2A catalytic (PP2Ac) and scaffolding (PP2A A) subunits, the striatins (PP2A regulatory B''' subunits), the striatin-associated protein Mob3, the novel proteins STRIP1 and STRIP2...PDCD10...and members of the germinal center kinase III family of Ste20 kinases"].

## Key Protein Interactions (from GOA IPI annotations)

- AXIN2 (Q9Y2T1) - via PMID:10698523 - PP2A complexed with Axin dephosphorylates APC in Wnt signaling
- TIPRL (O75663) - via PMID:16085932 and PMID:27880917 - PP complex regulator
- IGBP1/alpha4 (P78318) - via PMID:9647778, PMID:18782753, PMID:19156129, PMID:26496610, PMID:27880917, PMID:33961781, PMID:35271311 - protects monomeric PP2A C subunit
- STRIP1 (Q5VSL9) - via PMID:18782753, PMID:25531779, PMID:26496610, PMID:28514442, PMID:33961781, PMID:35271311 - STRIPAK component
- FHL1B (Q13642-2) - via PMID:20969868 - LIM domain protein, cell cycle
- TTP/ZFP36 (P26651) - via PMID:21784977 - mRNA stability regulator
- FMR1 (Q06787-7) - via PMID:32814053 - FMRP, neurodegenerative interactome

## NF-kappaB and Inflammatory Signaling

PMID:28159925 shows PPP2CB knockdown in MSCs increases RELA/p65 levels and, in combination with TNFalpha, enhances IL-6, CCL2, and CCL5 transcription. PPP2CB is a direct target of miR-1246. This supports roles in negative regulation of NF-kappaB and TNF-mediated signaling, but the effects are context-dependent (require TNFalpha co-stimulation for pro-inflammatory cytokine changes).

## Tau and Neurodegeneration

PP2A is the major tau phosphatase in human brain, accounting for ~71% of tau phosphatase activity [PMID:16262633]. PP2A activity negatively correlates with tau phosphorylation. This supports annotations related to tau binding and neurofibrillary tangle regulation, though these studies used PP2A broadly (not PPP2CB-specific).

## Key Considerations for Annotation Review

1. Many "protein binding" IPI annotations are from HTP interactome studies - these are uninformative per se, but reflect real PP2A subunit interactions and complex membership
2. IEA annotations transferred from rat PPP2CB (P62716) are generally appropriate given near-100% sequence identity
3. Response to lead ion annotation is based on ISS from rat - indirect evidence
4. Several Reactome cytosol annotations all relate to SPRY2 regulation of FGF signaling pathway
