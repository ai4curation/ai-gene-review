# acr-16 (P48180) manual literature research

No deep-research API was available; this summary was assembled by hand from cached
publications in `publications/` and PubMed searches (`acr-16[Title] elegans`).

## Identity
- C. elegans acr-16 (F25G6.3, WBGene00000055, GeneID 179235), UniProt P48180 (ACH1_CAEEL),
  498 aa, Cys-loop ligand-gated ion channel, nicotinic AChR alpha-type subunit
  (vicinal Cys211-Cys212). Closest vertebrate relative is CHRNA7.
- Originally cloned as Ce21: [PMID:8627624 "the Ce21 protein most resembles the vertebrate alpha7 subunit"].

## Channel activity
- Homomeric channel in oocytes: [PMID:8627624 "Upon expression in the Xenopus oocyte system, the Ce21 subunit assembled into a functional homomeric nAChR"];
  rapid desensitization, nicotine more potent than ACh, blocked by DHbetaE; levamisole antagonist, not agonist.
- RIC-3 required for robust expression: [PMID:19020092 "we coinjected acr-16 and ric-3 cRNAs. After only 1 day of expression, we recorded large acetylcholine-induced currents"];
  [PMID:19020092 "These recombinant receptors had the expected properties of N-AChRs because they were activated by nicotine and insensitive to levamisole."];
  ACh EC50 ~31 uM, Hill 2.4, profound desensitization [PMID:19020092 "ACR-16 homopentamers desensitize rapidly and profoundly"].
- Calcium permeability not measured: [PMID:19020092 "The calcium permeability of N-AChRs has not been measured."]
- Pharmacology with anthelmintics: PMID:11113327 (abstract only); Xenopus RIC-3 enhancement PMID:22970690.
- Hookworm ACR-16 orthologs are also homopentameric AChRs (PMID:33324163).

## In vivo role
- Muscle levamisole-insensitive (nicotine-sensitive) AChR: [PMID:15917232 "Electrophysiological analysis of the acr-16 deletion mutant showed that the levamisole-insensitive muscle acetylcholine current was eliminated"].
- [PMID:15944127 "acr-16 mutants lack fast cholinergic current at the NMJ and exhibit synthetic behavioral deficits with other known AChR mutants"].
- Localization requires the Ror RTK CAM-1: [PMID:15944127 "In cam-1 mutants, ACR-16 is mislocalized and ACR-16-dependent currents are disrupted"].
- SCA-1 (SERCA) regulates ACR-16 levels/function at the NMJ (PMID:29748129, abstract only).
- Neuronal role: expressed in AVA; with UNC-29 and ACR-18 partially redundant receptors in AVA mediate
  mating reversal: [PMID:23577128 "PVY+PVX-induced reversal depends on cholinergic transmission in AVA that is mediated by partially redundant AChRs that contain acr-18-, unc-29- and acr-16-encoded subunits."]
- Pharmacology/stress papers (nicotine immunomodulation PMID:40846258; hesperidin/autophagy PMID:37913913)
  are indirect, abstract-only and not used for annotation.

## Localization
- UniProt: postsynaptic cell membrane, cell membrane (PMID:15944127). The cell projection IDA rows
  (PMID:15944127, PMID:17719547) are abstract-only in the cache; muscle arms are the likely structure.
