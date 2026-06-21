# ATP6AP1 notes

## 2026-06-03 Proteostasis PN review

Deep research status: Falcon deep research has now completed successfully (`ATP6AP1-deep-research-falcon.md`, 19 citations); see the synthesis section at the end of this file. The original PN-batch attempt timed out before the `deep_research_unified` tool bugs were fixed. This review uses that report together with the fetched UniProt and GOA records, cached publications, local Reactome entries, and the PN projection report.

Core function synthesis: ATP6AP1/Ac45 is best reviewed as an accessory/regulatory V0-sector subunit of the V-ATPase that supports complex assembly, targeting, stability, and activity rather than as a catalytic proton pump subunit. Human V-ATPase structure work defines ATP6AP1 as a V0 assembly hub [PMID:33065002 "We define ATP6AP1 as a structural hub for Vo complex assembly because it connects to multiple Vo subunits and phospholipids in the c-ring."]. The human deficiency study supports an Ac45/Voa1-like assembly-factor role and shows disease mutants fail to restore V-ATPase-dependent growth in yeast [PMID:27231034 "Processed wild-type Ac45, but not its disease mutants, restored V-ATPase-dependent growth in Voa1 mutant yeast."].

Localization/function context: Ac45 localizes mainly to the ER and ERGIC in hepatocytes, not predominantly to the TGN or endosomal system in that experiment [PMID:27231034 "Ac45 was found to be mainly localized to the ER, and ER-to-Golgi Intermediate Compartment (ERGIC), but not to the trans-Golgi network (TGN) or components of the endosomal system"]. Mature V-ATPase activity is nevertheless central to endolysosomal and secretory-compartment acidification, and Reactome represents ATP6AP1 as an accessory V0 subunit facilitating acidification [Reactome:R-HSA-5252133 "V-type proton ATPase subunit S1 (ATP6AP1) is thought to function as an accessory subunit of the V0 subcomplex of V-ATPase, facilitating acidification"].

PN projection decision: the PN projection reports `GO:0007042 lysosomal lumen acidification` as already present in GOA and projects ATP6AP1 to `GO:0060590 ATPase regulator activity` [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv "ATPase regulator activity is the narrowest GO target that preserves the source mechanism without requiring a speculative complex-specific term."]. I accepted the lysosomal acidification projection as already supported and added `GO:0060590` conservatively as a new reviewed MF term, using the same evidence to modify the broad `GO:0140677 molecular function activator activity` row.

Conservative exclusions: generic `GO:0005515 protein binding` rows were marked over-annotated because they do not describe the ATP6AP1 molecular function. Direct `GO:0031267 small GTPase binding` rows were removed because the key mTORC1 paper supports V-ATPase-dependent Rag nucleotide loading but did not detect direct Rag interactions with purified V-ATPase subunits [PMID:22053050 "The v-ATPase is required for amino acid signaling to mTORC1 and functions between amino acids and the nucleotide loading of the Rag GTPases."]. HIF/iron and broad trafficking terms were kept as non-core secondary consequences where supported [PMID:28296633 "disrupting the V-ATPase results in intracellular iron depletion, thereby impairing PHD activity and leading to HIF activation."].

## Falcon deep research synthesis (2026-06-21)

The Falcon report (`file:human/ATP6AP1/ATP6AP1-deep-research-falcon.md`) is fully
consistent with the assembly-factor / structural-hub framing above and adds
structural and pathway detail. Citations use the report's DOIs except where a
PMID is already established in this file.

**Structural confirmation of the V0 hub role (Wang et al. 2020, Mol Cell 80:501,
doi:10.1016/j.molcel.2020.09.029; the "structural hub" finding already cited here
as PMID:33065002).** The cryo-EM structure shows ATP6AP1's luminal domain adopts a
**β-prism fold homologous to LAMP-family domains** (despite no sequence homology),
sits **centrally inside the c-ring**, and is the **most connected V0 subunit**
(>7,000 Å² buried surface), contacting ATP6AP2, c'', c(1/2/8/9) and subunit d.
This directly supports the assembly/stability MF over any catalytic role and
explains, at residue level, why disease mutations are loss-of-function: Y313C
destabilizes the luminal hydrophobic core, E346K disrupts a luminal salt bridge,
M428I perturbs TM contacts with the c-ring.

**Cooperative V0 assembly with ATP6AP2 (Guida et al. 2018,
doi:10.1091/mbc.e18-04-0234).** ATP6AP1 and ATP6AP2/(pro)renin receptor together
act as ER V0 assembly factors replacing the single yeast Voa1 function;
co-expression rescues V-ATPase-defective yeast and restores vacuolar quinacrine
accumulation. Relevant context for the neighboring ATP6AP2 review.

**Autophagy linkage (non-core, recent/translational).** Fei et al. 2024
(doi:10.1016/... breast-cancer lysosomal-gene study) and Yan et al. 2025 report
that ATP6AP1 supports autophagic flux via lysosomal acidification and, newly,
promotes **autophagosome-lysosome fusion by enhancing Rab7-HOPS interaction**;
overexpression drives chemoresistance. These are downstream/disease-context roles
and should remain **non-core** relative to the V0 assembly MF, but the Rab7-HOPS
fusion link is worth flagging as a candidate ALP-branch secondary function if it
is independently corroborated.

**Other corroborated points (no change to calls):** ER assembly then trafficking
to endolysosomes, Golgi (glycosylation), neuroendocrine secretory vesicles, and
osteoclast ruffled border; tissue-specific proteolytic processing (~40 kDa brain,
62 kDa liver, ~50 kDa B cells); V-ATPase-dependent (structural, not pump-direct)
role in mTORC1 amino-acid sensing. Net: no change to the core call (accessory V0
assembly/structural-hub subunit; `GO:0060590 ATPase regulator activity` + lysosomal
acidification), with strengthened structural justification.
