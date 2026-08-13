# LPGAT1 literature notes

## Research provenance

- On 2026-08-12, the required project deep-research attempt was made with `just deep-research human LPGAT1 --provider perplexity`. It failed immediately because this checkout's Justfile has no `deep-research` recipe (`error: Justfile does not contain recipe deep-research`). No provider-named deep-research file was created or fabricated.
- An independent PubMed title/abstract search for `LPGAT1` was then audited. Decisive primary sources not already cached were fetched through the project command `just fetch-pmid`: PMID:20018982, PMID:30831319, PMID:35131264, PMID:37917582, and PMID:42173283.
- All seeded GO_REF, PMID, and Reactome records were inspected. Abstract-only boundaries are recorded explicitly in the review YAML for PMID:10942595, PMID:15485873, PMID:19946888, and PMID:20018982.

## Identity, location, and nomenclature

LPGAT1 (UniProt Q92604) is also called LPLAT7 in the modern biochemical literature. It is an endoplasmic-reticulum membrane acyltransferase. The original human cloning study localized it directly: [PMID:15485873, "LPGAT1 was localized to the endoplasmic reticulum by subcellular fractionation and immunohistochemical analyses."] The cached UniProt record predicts two transmembrane helices, consistent with an integral/multipass ER-membrane enzyme, but topology prediction and experimental ER localization are distinct evidence types.

The LPLAT7 name better reflects the broad, position-defined lysophospholipid activity found in newer work. [PMID:36049524, "We also propose to use the new nomenclature, LPLAT7, for LPGAT1 since the newly assigned enzymatic activities are quite different from the LPGAT1s previously reported."]

## Best-supported current biochemical function

The strongest current model is sn-1 reacylation of unsaturated 1-lysophospholipids in the ER, with preference for stearoyl-CoA. Human-cell and mouse evidence converge on PC, PE, and PS remodeling:

- Human LPLAT7 assays established position and head-group scope: [PMID:36049524, "In vitro, we found LPLAT7 mainly incorporated several fatty acids into the sn-1 position of lysophosphatidylcholine (LPC) and lysophosphatidylethanolamine (LPE), with weak activities toward other lyso-PLs."]
- The same study found selective loss of stearate-containing products: [PMID:36049524, "only C18:0-containing phosphatidylcholine (PC) and phosphatidylethanolamine (PE) were specifically reduced in the LPLAT7-mutant cells and tissues from knockout mice, with a concomitant increase in the level of C16:0- and C18:1-containing PC and PE."]
- Murine recombinant enzyme and knockout data independently support sn-1 LPE/stearoyl chemistry: [PMID:35131264, "Bacterially expressed murine LPGAT1 transferred saturated acyl-CoAs specifically into the sn-1 position of lysophosphatidylethanolamine (LPE) rather than lysophosphatidylglycerol and preferred stearoyl-CoA over palmitoyl-CoA as the substrate."]
- The latest study gives the most specific native formulation: [PMID:42173283, "The enzymatic activity of LPLAT7 was specific for stearoyl-CoA and 1-lyso-2-acyl positional isomers of unsaturated lysophospholipids."]
- Its human Huh7 and mouse knockout lipidomics support products across three major head groups: [PMID:42173283, "In mice, Lplat7 knockout increased the concentration of unsaturated lysophospholipids, reduced the abundance of 1-stearoyl-2-unsaturated species of phosphatidylcholine, phosphatidylethanolamine, and phosphatidylserine, and inhibited the regeneration of cellular membranes."]

Thus, substrate position is essential: the free hydroxyl is at sn-1 and an unsaturated acyl chain remains at sn-2. A generic statement that LPGAT1 acylates LPC or LPE without positional qualification loses the most informative part of the evidence.

## Lysosomal salvage and membrane biogenesis

PMID:42173283 connects ER LPLAT7 to lysosome-derived substrates rather than locating the enzyme in lysosomes. Its tracer experiments used human Huh7 cells and concluded: [PMID:42173283, "Our data suggest that lysosomal phospholipid degradation is the principal source of LPLAT7 substrates."] This supports a PLA1/SPNS1-to-ER salvage model in which unsaturated 1-lysophospholipids are exported from lysosomes and reacylated by ER LPLAT7. It should not be converted into a lysosomal localization claim.

The same work frames the physiological output as membrane regeneration and lipid-flux partitioning: [PMID:42173283, "Thus, by re-acylating unsaturated 1-lysophospholipids, LPLAT7 shifts lipid metabolism from the biogenesis of lipid droplets to the biogenesis of membranes."] This is supported in Huh7 cells and Lplat7-knockout mice; direct demonstration in intact human tissues remains absent.

## Historical LPG activity and the PG-remodeling dispute

The 2004 study identified recombinant human LPGAT1 by increased LPG acyltransferase activity in Sf9 and COS-7 cells: [PMID:15485873, "Expression of the LPGAT1 cDNA in Sf9 insect and COS-7 cells led to a significant increase in LPG acyltransferase activity."] It also reported no detectable LPC, LPE, LPI, or LPS activity in those assay conditions. This is genuine direct human-enzyme evidence, but the abstract does not resolve the LPG positional isomer, and later studies using position-defined acceptors produce a different specificity model.

PMID:35131264 found that bacterially expressed murine LPGAT1 used sn-1 LPE rather than LPG. PMID:36049524 found broad human sn-1 LPC/LPE activity and explains that acceptor structure and assay selection affect detection. Most decisively, PMID:42173283 reports: [PMID:42173283, "We speculate that LPLAT7 was misidentified as LPGAT1 (6) because LPG, having 3 unesterified hydroxyl groups, is prone to intramolecular acyl migration. As a result, 1-lyso-PG may become available when 2-lyso-PG is used as substrate. However, our lipidomics data do not demonstrate any involvement of LPLAT7 with PG in vivo."]

Reactome reactions R-HSA-1482539 (1-acyl LPG to PG), R-HSA-1482635 (2-acyl LPG to PG), and pathway R-HSA-1482925 correctly preserve the older LPGAT model and its provenance. They are scientifically disputed rather than mechanically miscited. Neither the 1-acyl nor 2-acyl Reactome reaction should be treated as stronger than the newer position-resolved biochemical and lipidomic evidence.

## Competing mitochondrial/MEGDEL interpretation

Mouse studies report severe mitochondrial and hepatic consequences of Lpgat1 loss. Whole-body knockout caused hepatopathy and mitochondrial dysfunction [PMID:30831319, "LPGAT1 deficiency protected mice from diet-induced obesity, but led to hepatopathy, insulin resistance, and NAFLD as a consequence of oxidative stress, mitochondrial DNA depletion, and mitochondrial dysfunction."] PMID:37917582 proposed that ER PG remodeling is coupled to mitochondrial transport through prohibitin/TIMM14: [PMID:37917582, "We show that PG remodeling by LPGAT1 at the ER is closely coordinated with mitochondrial transport through interaction with the prohibitin/TIMM14 mitochondrial import motor."]

Those phenotypes and reported interactions remain observations, but their PG-specific causal interpretation is contested. The 2026 study found that knockout altered PC, PE, and PS rather than PG and concluded: [PMID:42173283, "Our data do not support any significant involvement of LPLAT7 in the remodeling of PG, a mitochondrial lipid, but instead suggest that mitochondrial dysfunction may result from a defect in phospholipid regeneration in Lplat7 knockouts."] Therefore MEGDEL-like phenotypes should be kept as mouse/context evidence, not stated as proof that human LPGAT1 is a physiological PG remodeler or a confirmed human MEGDEL gene.

## Monoacylglycerol acyltransferase claim

PMID:20018982 reported mouse hepatic MGAT activity and an shRNA phenotype in diabetic db/db mice: [PMID:20018982, "In this study, we identified a novel MGAT gene, which is identical with lysophosphatidylglycerol acyltransferase1 (LPGAT1)."] This is not direct evidence of a core human activity. It combines mouse disease context, liver-directed knockdown, and bulk MGAT activity, while modern studies establish robust lysophospholipid reacylation and the reviewed UniProt record describes MGAT activity as weak with a direct role in triglyceride synthesis unlikely. The MGAT assignment is therefore disputed/secondary, not transferable to a core human molecular function without direct human enzyme evidence.

## Regulation and lipid-synthesis context

PMID:23749231 used mouse liver and human Huh-7 cells to place LPGAT1 downstream of miR-30c. [PMID:23749231, "Analysis of hepatic mRNA showed that miR-30c reduced Lpgat1, Elovl5, Stard3 and Mboat1 mRNA levels"] and [PMID:23749231, "siELOVL5 and siLPGAT1 reduced de novo lipogenesis"]. Importantly, [PMID:23749231, "siLPGAT1 had no effect on media apoB"]. LPGAT1 therefore contributed to the lipid-synthesis arm in this context, whereas MTP mediated the apoB-secretion effect. This paper does not support assigning LPGAT1 a direct lipoprotein-assembly or apoB-secretion function.

## Species, assay, and isoform boundaries

- PMID:15485873 expressed human LPGAT1 cDNA in Sf9 insect and COS-7 cells; its biochemical results are human-protein/heterologous-system evidence, and the available cache is abstract-only.
- PMID:36049524 assayed human LPLAT7 isoform 1 in HEK293A membrane fractions and also used mutant cells and knockout-mouse tissues. The exact construct statement is [PMID:36049524, "cDNA for human LPLAT7 (hLPGAT1 isoform1; NCBI accession number NM_014873) was amplified by PCR using PrimeStar HS Polymerase (TAKARA BIO Inc) and HEK293A cell cDNA as a template."]. This records what was tested; it does not establish that the function is unique to isoform 1. The reviewed UniProt cache does not provide evidence for functionally distinct endogenous protein isoforms.
- PMID:35131264 used bacterially expressed murine LPGAT1 and Lpgat1-knockout mice. Its position-specific chemistry corroborates the human study but must retain its species boundary.
- PMID:42173283 combines recombinant assays, human Huh7 knockout/tracing, and mouse knockout tissues. Huh7 is a transformed hepatic cell line, not intact normal human liver.
- PMID:30831319, PMID:35131264, and much of PMID:37917582 establish mouse phenotypes. They do not establish corresponding human developmental or disease phenotypes.
- PMID:10942595 and PMID:19946888 are broad screen/dataset papers whose abstracts do not expose LPGAT1-specific experimental details; they should not carry mechanistic weight beyond curator/dataset provenance.

## Evidence conclusion

The defensible core is an ER-membrane sn-1 lysophospholipid acyltransferase that preferentially uses stearoyl-CoA and unsaturated 1-lyso-2-acyl LPC/LPE, with LPS also supported in vivo, to regenerate 1-stearoyl-2-unsaturated PC/PE/PS. Lysosomal degradation supplies substrates in human Huh7 experiments, but the enzyme remains ER-localized. Physiological LPG/PG remodeling, the PG-specific mitochondrial transport model, and MGAT/triglyceride-synthesis activity are disputed or context-limited and should not displace the position-resolved core chemistry.
