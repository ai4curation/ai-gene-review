# YGR117C Research Notes

## Basic Information

- **Systematic name**: YGR117C
- **SGD ID**: S000003349
- **UniProt**: P53270
- **Feature type**: ORF, Verified (previously listed as Uncharacterized)
- **Length**: 476 aa, 53.4 kDa
- **Protein expression**: ~1280 molecules/cell in log phase SD medium [PMID:14562106]; median abundance 2,276 +/- 681 molecules/cell per SGD
- **Half-life**: 8.3 hours

## Domain Architecture

From UniProt and InterPro:
- **LisH motif** (IPR006594, PROSITE PS50896): residues 7-39. The LIS1 homology motif is a short alpha-helical domain involved in protein dimerization. Originally identified in the LIS1 (lissencephaly-1) protein.
- **WD40-repeat-containing domain superfamily** (IPR036322, SUPFAM SSF50978): residues 125-472. A beta-propeller fold commonly serving as a protein-protein interaction platform.
- **Uncharacterised conserved protein UCP007778** (IPR016520, PIRSF007778): residues 4-471. A broad family-level signature. Also IPR060045 (UCP007778-like, residues 10-469).

The combination of an N-terminal LisH motif plus a C-terminal WD40 propeller is found in several yeast proteins, notably GID7/YCL039W, a subunit of the GID E3 ubiquitin ligase complex. However, YGR117C is NOT Gid7 -- they are distinct proteins with distinct systematic names.

## SGD Description

"Protein of unknown function; green fluorescent protein (GFP)-fusion protein localizes to the cytoplasm" [PMID:14562095, Huh et al. 2003]

## GO Annotations (from GOA)

Only 3 annotations:
1. GO:0005737 cytoplasm (HDA, PMID:14562095) -- GFP-fusion localization
2. GO:0003674 molecular_function (ND, GO_REF:0000015) -- No Data
3. GO:0008150 biological_process (ND, GO_REF:0000015) -- No Data

This is an extremely poorly annotated gene. The ND annotations explicitly indicate that no molecular function or biological process is known.

## Phenotype Data (from SGD, large-scale surveys)

The ygr117c-delta null mutant is viable and shows:
- Decreased competitive fitness
- Decreased endocytosis
- Decreased hyperosmotic stress resistance
- Increased innate thermotolerance
- Increased oxidative stress resistance
- Increased mitotic recombination
- Abnormal vacuolar morphology
- Decreased utilization of nitrogen source (decreased rate)
- Variable chemical resistance (both increased and decreased reported)
- Haploinsufficient

These are all from large-scale surveys and are not gene-specific studies. The phenotype profile is broad and does not point to a single pathway.

## Physical Interactions (from SGD/BioGRID)

9 physical interactors detected via:
- Affinity Capture-MS: 3 experiments
- Affinity Capture-RNA: 2 experiments
- Co-localization: 1 experiment
- Co-purification: 1 experiment
- Two-hybrid: 2 experiments

Specific interactors not individually available from web scraping, but the total is 9 physical and 29 genetic interactors.

## STRING Interactions

Low-confidence interactions only:
- ISW1 (YBR245C): score 0.412 -- chromatin remodeling ATPase
- PHO81 (YGR233C): score 0.410 -- CDK inhibitor in phosphate signaling
- GDE1 (YPL110C): score 0.403 -- glycerophosphocholine phosphodiesterase

All scores are near the 0.4 threshold, indicating weak/low-confidence associations. These likely reflect genomic context or text-mining co-mentions rather than functional interactions.

## Literature

Only 1 primary reference and 3 additional references per SGD. No gene-specific functional study has been published. All annotations derive from large-scale genomic/proteomic surveys:
- PMID:8905931 -- sequencing of chr VII region (Hansen et al. 1996)
- PMID:9169869 -- chr VII complete sequence (Tettelin et al. 1997)
- PMID:24374639 -- genome reannotation (Engel et al. 2014)
- PMID:14562106 -- protein expression (Ghaemmaghami et al. 2003)
- PMID:14562095 -- protein localization (Huh et al. 2003)

## Key Finding: No gene-specific functional study exists

There is NO published paper that specifically investigates YGR117C function. All information comes from genome-wide surveys. The protein is genuinely uncharacterized.

## Assessment of BioReason Predictions

The BioReason deep research file makes several specific claims that need verification:

### Claim 1: "myosin V binding" (GO:0032033)
**FABRICATED.** 
- The correct GO term for myosin V binding is GO:0031489, not GO:0032033. GO:0032033 does not exist as a myosin V binding term.
- There is NO evidence linking YGR117C to myosin V or any myosin. No published study reports this interaction.
- BioReason appears to reason: LisH domain -> "classically associated with microtubule- and dynein-linked regulation" -> nuclear positioning -> myosin V binding. This chain of reasoning is speculative and unsupported.
- While LisH domains ARE found in some cytoskeletal-associated proteins (LIS1 itself), having a LisH domain does not imply myosin V binding. LisH domains are found in diverse contexts including the GID/CTLH E3 ligase complex.

### Claim 2: "nuclear migration"
**FABRICATED.**
- No evidence links YGR117C to nuclear migration. No published study reports this.
- The BioReason UniProt Summary section states "Involved in nuclear migration. Also involved in transcriptional silencing at the HMR locus." -- this text does NOT appear in the actual UniProt entry for P53270. The UniProt entry says "Uncharacterized protein YGR117C" with NO functional description.
- This is a clear fabrication in the "UniProt Summary" section of the BioReason output.

### Claim 3: "silent mating-type cassette heterochromatin formation" (GO:0030466)
**FABRICATED.**
- No evidence links YGR117C to heterochromatin formation or mating-type silencing.
- The BioReason reasoning: WD40 propeller -> "commonly serve as hubs for chromatin-modifying complexes" -> "recruiting or positioning silencing factors" -> HMR heterochromatin. This is pure speculation.
- While WD40 proteins DO participate in chromatin complexes (e.g., WDR5 in COMPASS), having WD40 repeats does not imply a role in chromatin silencing.

### Claim 4: Domain architecture description
**PARTIALLY CORRECT.**
- The InterPro domain assignments (IPR016520, IPR006594, IPR060045, IPR036322) are accurate.
- The description of LisH as an alpha-helical motif and WD40 as a beta-propeller is correct.
- However, the functional extrapolation from domains to specific biological roles is unfounded.

### Claim 5: "UniProt Summary" section
**FABRICATED.**
- BioReason's "UniProt Summary" states: "Involved in nuclear migration. Also involved in transcriptional silencing at the HMR locus."
- The actual UniProt record for P53270 contains NO functional description. The protein is listed as "Uncharacterized protein YGR117C".
- This is the most concerning fabrication because it masquerades as an authoritative source.

## Conclusion

YGR117C encodes a cytoplasmic protein of unknown function containing LisH and WD40 domains. Its function is genuinely unknown. The BioReason predictions are almost entirely fabricated from domain architecture extrapolation, with a fabricated "UniProt Summary" that does not match the actual UniProt record.
