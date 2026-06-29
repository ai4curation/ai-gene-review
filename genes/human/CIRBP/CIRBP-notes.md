# CIRBP (Cold-Inducible RNA-Binding Protein) — Review Notes

UniProt: Q14011 (CIRBP_HUMAN). 172 aa. Also known as A18 hnRNP, CIRP, glycine-rich
RNA-binding protein. Chromosome 19.

## Domain architecture
- N-terminal RRM (RNA recognition motif), residues ~6–84 (PROSITE PRU00176; CDD
  cd12449 RRM_CIRBP_RBM3). Structures: 1X5S (NMR), 5TBX (X-ray 1.77 Å), 8CMK.
- C-terminal intrinsically disordered, glycine-rich / arginine-glycine-glycine
  (RGG/RG) repeat domain (residues ~69–172; DisProt DP03917). Contains an
  RSY-rich subregion.
- Both the RRM and the RGG domain are required for high-affinity binding to target
  3'-UTRs (TXN) and for stress-granule recruitment.
  [UniProt DOMAIN; PMID:16513844]

## Core established functions (from primary literature)
1. **Cold-inducible RNA-binding protein / cold stress response, growth suppression.**
   Founding paper (mouse cirp) shows CIRP is induced when temperature drops from 37→32 °C,
   localizes to nucleoplasm, and overexpression impairs cell growth by prolonging G1 phase;
   antisense knockdown alleviates cold-induced growth impairment. "CIRP plays an essential
   role in cold-induced growth suppression of mouse fibroblasts."
   [PMID:9151692 "CIRP plays an essential role in cold-induced growth suppression of mouse fibroblasts"]
   Human CIRP cloned/characterized in [PMID:9434172] and as UV-inducible A18 in [PMID:9334257].

2. **mRNA 3'-UTR binding and stabilization of stress-responsive transcripts (RPA2, TXN).**
   A18 hnRNP (CIRP) is induced by UV, translocates nucleus→cytoplasm, binds specifically the
   3'-UTR of RPA2 and thioredoxin (TXN) transcripts; overexpression increases mRNA stability
   and enhances translation dose-dependently; knockdown sensitizes cells to UV. Protective role
   in genotoxic stress.
   [PMID:11574538 "Overexpression of A18 hnRNP increases the mRNAs stability and consequently enhances translation in a dose-dependent manner"]

3. **Post-transcriptional/translational regulation of thioredoxin (TXN); interaction with
   eIF4G1; ribosome association; GSK3B phosphorylation.** RRM and RGG bind TXN 3'-UTR
   independently, both required for maximal binding; CIRP co-localizes with TXN transcripts on
   ribosomal fractions; increases TXN translation; interacts with eIF4G; GSK3β phosphorylation
   increases RNA-binding activity in response to UV.
   [PMID:16513844 "hnRNP A18 increases TRX translation and interacts with the eukaryotic Initiation Factor 4G (eIF4G)"]
   [PMID:16513844 "hnRNP A18 phosphorylation by the hypoxia inducible GSK3beta increases hnRNP A18 RNA binding activity"]

4. **General mRNA-binding protein (RBP).** Identified in unbiased mRNA-interactome capture atlases
   (HeLa; HEK293) by UV-crosslinking + oligo(dT) capture.
   [PMID:22658674 atlas of mammalian mRNA-binding proteins]
   [PMID:22681889 mRNA-bound proteome]

5. **Subcellular localization / nucleocytoplasmic shuttling / stress granules.**
   Predominantly nucleoplasmic at steady state; translocates to cytoplasm and into stress granules
   upon UV, osmotic, heat, and other cytoplasmic stresses. Nuclear import mediated by Transportin-1
   (TNPO1) recognizing the RG/RGG region and Transportin-3 (TNPO3) recognizing an RSY-rich region;
   importin binding also prevents aberrant phase separation / SG recruitment.
   [PMID:32234784 "both TNPO1 and Transportin-3 (TNPO3) recognize two nonclassical NLSs within the cold-inducible RNA-binding protein (CIRBP)"]
   RGG arginine methylation is a prerequisite for SG recruitment (By similarity, UniProt PTM).

6. **Induction by hypoxia (HIF-1-independent).** [PMID:15075239]

## Protein–protein interactions (IntAct/IPI; mostly large-scale)
HNRNPK (P61978) — recurrent; ATXN1 (P54253); RBMX/RBMY paralogs; SNRPA; SRSF3; TNPO1; TNPO3;
KHDRBS2; LNX1. Many are large-scale Y2H / interactome-map derived (PMID:25416956, 32296183,
33961781, 35271311 OpenCell, 31515488, 29892012, 21516116, 16189514, 16713569, 22365833 spliceosome).
These support GO:0005515 protein binding (uninformative) but individually are not strong evidence
for a specific MF.

## GO annotation assessment summary (working)
- **mRNA binding / RNA binding / mRNA 3'-UTR binding**: well supported (IDA PMID:11574538, 16513844;
  HDA atlases). mRNA 3'-UTR binding is the most specific/informative MF — CORE.
- **translation repressor activity (ISS GO:0030371) & negative regulation of translation
  (IEA from 0030371)**: ISS from mouse P60824. Note primary human data (PMID:11574538) shows CIRP
  is a translational *activator/enhancer* of its targets (RPA2, TXN); UniProt lists "translational
  repressor (By similarity)" and the RGG C-terminus mediates repression by similarity. Mixed —
  CIRP can act as both an activator (of specific stabilized transcripts) and a general translational
  repressor in stress granules. Keep repressor terms but flag; positive regulation of translation
  (IDA) is directly supported.
- **positive regulation of translation (IDA GO:0045727, PMID:11574538)**: supported (enhances
  translation of stabilized targets). CORE-ish.
- **mRNA stabilization (IDA GO:0048255, PMID:11574538)**: supported. CORE.
- **response to UV (IDA GO:0009411, PMID:11574538)**: supported.
- **response to cold (TAS PMID:9151692; IEA ARBA)**: supported — defining property.
- **stress granule assembly / cytoplasmic stress granule (ISS GO:0034063 / GO:0010494)**:
  supported by literature (SG recruitment; promotes SG assembly when overexpressed). Keep.
- **small ribosomal subunit rRNA binding (IDA GO:0070181, PMID:11574538)**: This is unusual.
  PMID:11574538 is about mRNA 3'-UTR (RPA2/TXN) binding, not rRNA. Need to verify — possible
  over-interpretation / mis-mapping. CIRP associates with ribosomes (PMID:16513844) but that is
  not the same as small-subunit rRNA binding. FLAG for scrutiny (likely MODIFY/REMOVE or UNDECIDED).
- **mRNA splicing via spliceosome (IBA GO:0000398) / spliceosomal complex (IBA GO:0005681)**:
  IBA from PANTHER tree including hnRNP/RBM paralogs. CIRP is not a core splicing factor; these are
  phylogenetic propagations from spliceosome-associated relatives. CIRP copurifies with spliceosome
  in one Y2H map (PMID:22365833) but no direct evidence it functions in splicing. Likely
  over-annotation → MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
- **nucleus / nucleoplasm / cytoplasm / stress granule**: all supported (IDA PMID:11574538; HPA;
  HDA). CORE localizations.
- **nucleic acid binding (IEA GO:0003676)**: generic parent of RNA binding; redundant but not wrong.
- **protein binding (GO:0005515, many IPI)**: uninformative; keep as-is per convention (cannot
  propose better term from generic binding).

## Key recent reviews (from deep research, falcon)
- Corre & Lebreton 2024, Biochimie 217:3-9 (doi:10.1016/j.biochi.2023.04.003) — regulation of CIRBP by cellular stresses.
- Rana et al. 2024 (doi:10.1016/j.cstres.2024.07.001) — comprehensive CIRBP review.
- Aziz, Chaudry & Wang 2025, IJMS 26:3524 — extracellular CIRP (eCIRP) DAMP biology.
- Han et al. 2023, Front Immunol — exosome-derived CIRP as inflammation amplifier.
- Zhou et al. 2025, Nat Commun (doi:10.1038/s41467-025-59802-2) — TNPO3 structural basis of phosphorylation-independent nuclear import (PDB 8CMK).

## Final review decisions (CIRBP-ai-review.yaml)
- ACCEPT (core MF): mRNA 3'-UTR binding (GO:0003730, IDA x2), mRNA binding (IBA), RNA binding (IEA/HDA), translation repressor activity (ISS).
- ACCEPT (core BP/CC): mRNA stabilization, positive regulation of translation, response to UV, response to cold (TAS+IEA), stress granule assembly, negative regulation of translation, nucleus/nucleoplasm/cytoplasm/cytoplasmic stress granule.
- ACCEPT (valid but generic): nucleic acid binding (IEA); all protein binding (IPI) — noted partner per study; TNPO1/TNPO3 (32234784) and eIF4G1 (16513844) flagged as functionally meaningful.
- MARK_AS_OVER_ANNOTATED: mRNA splicing via spliceosome (IBA) and spliceosomal complex (IBA) — family-level propagation, no CIRBP-specific splicing evidence; co-purification only (22365833).
- UNDECIDED: small ribosomal subunit rRNA binding (GO:0070181, IDA PMID:11574538) — abstract describes mRNA 3'-UTR binding not rRNA; full text unavailable, so not removed per guidance.
- NEW (non-core, extracellular moonlighting): extracellular space (GO:0005615) and positive regulation of inflammatory response (GO:0050729) for eCIRP/DAMP biology — absent from current GOA.

## Open questions / to verify
- GO:0070181 small ribosomal subunit rRNA binding from PMID:11574538 — does full text support rRNA
  binding, or is this a curation slip from "ribosome association"? (full text not in cache; abstract
  is about mRNA 3'-UTR). Use caution: do not REMOVE an IDA without reading full text — UNDECIDED or
  MODIFY at most.
- Extracellular CIRP (eCIRP) as a DAMP/inflammatory mediator (sepsis, shock) is a major part of the
  CIRBP literature but is NOT in current GOA; consider for proposed new terms / suggested experiments.
