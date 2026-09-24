# STE5 (YDR103W, UniProt P32917) curation notes

Identity confirmed from `STE5-uniprot.txt`: `AC P32917; D6VS89`, `GN Name=STE5; Synonyms=NUL3; OrderedLocusNames=YDR103W`, 917 aa, S. cerevisiae S288c. Domains (InterPro): RING_Ste5 (IPR063871), PH_STE5 (IPR063666), Ste5_Fus-binding (IPR021651), Ste5_Fus3-bd_dom (IPR021106), Ste5_vWA-ext (IPR062768), Ste5_C_sf (IPR038382). PDB 2KGN/2L4U (PM helix, aa 44-67), 3FZE/4F2H (VWA "Ste5-ms" domain, aa 583-787). No GO-CAM model in `gocams/index.tsv` contains Ste5. Context module: `modules/scer_mating_fus3_cascade.yaml`.

## Core function: pheromone-pathway MAPK scaffold

- Two-hybrid: Ste5 binds all three cascade kinases [PMID:7851759 "Ste5p, a protein of unknown biochemical function, interacted with protein kinases that operate at each step of the MAP kinase cascade, specifically with Ste11p (an MEKK), Ste7p (an MEK), and Fus3p (a MAP kinase)."]
- Tethering / copurification [PMID:8062390 "Ste5 copurifies with Ste11, Fus3, and a hypophosphorylated form of Ste7, and all four proteins cosediment in a glycerol gradient as if in a large complex."; "Ste5 also increases the amount of Ste11 complexed to Ste7 and Fus3 and is required for Ste11 to function."]
- RING-H2 domain binds Ste4 (Gbeta); required for oligomerization and function [PMID:9311911 "Thus, the RING-H2 domain mediates Ste4-Ste5 interaction, which is a prerequisite for Ste5-Ste5 self-association and signaling."]
- Gbeta binding first shown [PMID:7667635 "A haploid-specific interaction between the amino terminus of Ste5p and the G protein beta subunit Ste4p was also detected in a two-hybrid assay"].

## Membrane recruitment

- Pheromone/Gbetagamma recruits Ste5 to the cell surface at projection tips; artificial PM targeting activates pathway [PMID:9732267 "Furthermore, this event has functional significance, as artificial targeting of Ste5 to the plasma membrane, but not intracellular membranes, activates the pathway in the absence of pheromone or Gbetagamma."]; localization [PMID:9732267 "Pheromone caused some of the GFP–Ste5 to accumulate at the cell surface, at the tips of pheromone-induced projections"].
- Nuclear pool: [PMID:9732267 "In untreated cells, GFP–Ste5 was present diffusely throughout the cytoplasm, and was enriched in the nuclei"]; nuclear localization probably not required for signaling [PMID:9732267 "suggesting that nuclear localization of Ste5 may not be required for signaling"].
- PH domain (aa 388-518) binds PI(4,5)P2 and is essential for PM recruitment [PMID:16847350 "In vitro the Ste5 PH domain binds preferentially to PtdIns(4,5)P 2 ."; "the PH domain is essential for stable membrane recruitment of Ste5"]. PM recruitment lets Ste5-bound Ste11 be activated by Ste20.
- Cln/CDK phosphorylation flanking the PM motif blocks membrane binding, restricting signaling to G1 [PMID:17289571 "Cln/CDK disrupts Ste5 membrane localization by phosphorylating a cluster of sites that flank a small, basic, membrane-binding motif in Ste5."].
- Cytoplasm/nucleus + projection tips [PMID:11781566 "Ste5p and Fus3p were found in the nucleus and the cytoplasm"; "Ste5p, Ste7p and Fus3p also localized to tips of mating projections in pheromone-treated cells."].

## Active (allosteric) roles beyond tethering

- VWA/"Ste5-ms" domain binds Ste7 tightly (KD 75 nM) and raises kcat of Ste7->Fus3 ~5000-fold, not Ste7->Kss1 [PMID:19303851 "This domain specifically increases the kcat for the Ste7➔ Fus3 reaction by ~5000-fold, while it has no effect on the kcat or KM of the Ste7➔ Kss1 reaction."; "Thus, the Ste5-ms domain is essentially serving as a substrate specific co-catalyst for Ste7➔Fus3 phosphorylation"]. Analogy drawn to cyclin as Cdk co-catalyst. This is the basis for proposing GO:0043539 protein serine/threonine kinase activator activity (NEW, IDA).
- Fus3-binding domain (FBD, aa 288-316) allosterically activates Fus3 autophosphorylation; the resulting partially active Fus3 phosphorylates Ste5 and dampens output [PMID:16424299 "A fragment of Ste5 allosterically activated autophosphorylation of the mitogen-activated protein kinase Fus3."; "autoactivated Fus3 appears to have a negative regulatory role, promoting Ste5 phosphorylation and a decrease in pathway transcriptional output."]. FBD not required for signaling [PMID:19303851 "the previously identified Fus3 binding site in Ste5 (residues 288–316 in Ste5) is not required to promote the Ste7➔Fus3 reaction."].
- Evolution: VWA activator is ancient (Fus3/Kss1 split); FBD recent; Ste5-FBD also binds heterologous MAPKs in vitro [PMID:23953117 "even though these kinases readily bound to S. cer. Ste5-FBD"]. These xeno IPI rows are evolutionary probes, not physiological partners.

## Kss1 / invasive growth

- In S288c, Ste4 and Ste5 are needed for Kss1 activation and invasive growth; not in Sigma1278b [PMID:15192700 "Thus, Ste4 and Ste5 are required for Kss1 to be activated by multiple stimuli that induce IG."; "The requirement for Ste4 and Ste5 in activation of Kss1 during IG in S288c contrasted Σ1278b, which does not require Ste4 or Ste5 for IG or SVG"]. Treat as non-core, strain-dependent.

## Fus1 SH3 interaction

- Ste5 contains an R(S/T)(S/T)SL motif bound by the non-canonical Fus1 SH3 domain in vitro [PMID:18280496 "this domain binds to R(S/T)(S/T)SL-containing peptides derived from two putative in vivo binding partners from yeast proteins, Bnr1p and Ste5p, with K(d) values in the low micromolar range."]. Physiological role unknown.

## Curation decisions summary

- GO:0005078 MAP kinase scaffold activity: core MF (ACCEPT, 4 rows).
- 20 bare protein-binding rows: MODIFY to MAPKKK binding (Ste11), MAPKK binding (Ste7), MAPK binding (Fus3), G-protein beta-subunit binding (Ste4), SH3 domain binding (Fus1, 18280496 only); REMOVE xeno MAPK rows (23953117) and the Fus1 two-hybrid row from 15020407 (abstract-only, no domain mapping visible).
- NEW: GO:0043539 protein serine/threonine kinase activator activity (Ste5-ms co-catalyst for Ste7->Fus3; FBD activation of Fus3 autophosphorylation).
- Nucleus, invasive growth, negative regulation of MAPK cascade: KEEP_AS_NON_CORE.
