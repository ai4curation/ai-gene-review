# TDO (ANOGA) - Research Notes

## Gene Identity

- UniProt: O77457 (T23O_ANOGA)
- Gene: AGAP002721
- Organism: Anopheles gambiae (African malaria mosquito)
- Enzyme: Tryptophan 2,3-dioxygenase (EC 1.13.11.11)
- Chromosome location: 2R (subdivision 12E)
- Homolog of Drosophila melanogaster *vermilion* gene

## Key Literature

### Mukabayire et al. 1996 (PMID:8969464) - Gene cloning and characterization
The foundational paper. Cloned and characterized the A. gambiae tryptophan oxygenase gene (homolog of Drosophila vermilion).
- Maps to chromosome 2R, subdivision 12E (unlike Drosophila where it is X-linked)
- Six introns: four positioned identically to Drosophila, one similarly positioned, one novel
- 1955 nt cDNA encoding 392 amino acid protein (~45 kDa)
- 74% identity to Drosophila, 53% identity to nematode/mammalian TDOs
- Developmentally regulated transcript ~2 kb
- "Since this gene is known to control adult eye color in other flies, its cloning from A. gambiae provides the basis for a dominant phenotypic marker for germline transformation" [PMID:8969464]

### Besansky et al. 1997 (PMID:9443379) - Functional complementation
- A. gambiae TDO cDNA expressed under baculovirus ie-1 promoter partially rescued Drosophila vermilion eye color
- "The successful genetic complementation by this construct demonstrated both the proper function of the tryptophan oxygenase product and the effectiveness of the ie-1 promoter" [PMID:9443379]
- Confirms functional conservation across millions of years of independent evolution

### Mukabayire et al. 2001 (PMID:11240635) - Population genetics
- Used the tryptophan oxygenase locus for population genetic studies of A. gambiae chromosomal forms
- The TDO locus lies inside inversion 2Rb
- "At the tryptophan oxygenase locus inside inversion 2Rb, variation was structured only by inversion orientation and not by taxonomic designation even between An. gambiae and An. arabiensis, providing the first molecular evidence that the 2Rb inversion was transferred between species by introgressive hybridization" [PMID:11240635]

### Paglino et al. 2008 (PMID:18687401) - Biochemical characterization
The key biochemical paper on recombinant A. gambiae TDO.
- "In the malaria vector Anopheles gambiae, tryptophan 2,3-dioxygenase (TDO) is the only enzyme able to initiate l-tryptophan degradation through the kynurenine pathway" [PMID:18687401]
- TDO mRNA is ubiquitously expressed across tissues
- Purified recombinant enzyme in heme-ferric form
- Determined Michaelis-Menten kinetics with reducing agents
- Several kynurenines and tryptophan-derived molecules modulate TDO activity in vitro
- "Our study could contribute to understanding TDO regulation in vivo and to the identification of inhibitors to be used to alter Tryptophan homeostasis in the malaria vector" [PMID:18687401]

### Holt et al. 2002 (PMID:12364791) - Genome sequence
- The A. gambiae genome paper; provides the genomic context for AGAP002721 on chromosome 2R

### Bottino-Rojas et al. 2022 (PMID:34999199) - Kynurenine pathway and midgut homeostasis
- Studies on kynurenine hydroxylase mutants in Aedes aegypti, Anopheles stephensi, Culex quinquefasciatus
- "Insect ommochrome biosynthesis pathways metabolize tryptophan to generate eye-color pigments"
- "Female mosquitoes with spontaneous and induced mutations in the orthologs of the genes encoding kynurenine hydroxylase... exhibited impaired survival and reproductive phenotypes"
- "A compromised midgut permeability barrier function was also observed in An. stephensi"
- KP is implicated in midgut homeostasis and host/microbiota interface regulation
- Xanthurenic acid (KP end-product) rescued lethality and limited microbiota proliferation

### Feng et al. 2022 (PMID:35437328) - Microbiota and tryptophan catabolism
- Gut microbiota in Anopheles stephensi involved in tryptophan metabolism
- 3-hydroxykynurenine (3-HK) impaired peritrophic matrix and promoted Plasmodium berghei infection
- Pseudomonas alcaligenes catabolizes 3-HK via kynureninase (KynU)
- Identifies "an unexpected function of mosquito gut microbiota in controlling mosquito tryptophan metabolism, with important implications for vector competence" [PMID:35437328]

### Rossi et al. 2006 (PMID:16585514) - 3-HKT crystal structure
- Crystal structure of A. gambiae 3-hydroxykynurenine transaminase (downstream enzyme)
- "In Anopheles gambiae, xanthurenic acid (XA) plays a key role in parasite gametogenesis"
- XA produced by transamination of 3-HK, the main detoxification route
- Structure-based design of specific enzyme inhibitors as potential antimalarial agents

### Arai et al. 2001 (PMID:11463462) - XA and Plasmodium gametogenesis
- Both mosquito-derived XA and host blood-derived factors regulate Plasmodium gametogenesis
- XA is a gametocyte-activating factor (GAF)
- "Removal of both host and vector sources of GAF totally inhibited both exflagellation and ookinete production"

## Pathway Context

### Kynurenine Pathway in Mosquitoes
TDO catalyzes step 1: L-tryptophan + O2 --> N-formylkynurenine
N-formylkynurenine is then hydrolyzed to kynurenine by kynurenine formamidase.
Kynurenine --> 3-hydroxykynurenine (via kynurenine 3-monooxygenase)
3-HK --> xanthurenic acid (via 3-HKT) OR --> ommochrome pigments

### Biological Roles
1. **Eye pigmentation**: TDO is the first enzyme in the ommochrome biosynthetic pathway. Loss-of-function = vermilion (bright red/white) eye phenotype in Drosophila and other insects.
2. **Tryptophan homeostasis**: TDO is the only enzyme initiating Trp degradation via the kynurenine pathway in A. gambiae (no IDO identified). Ubiquitous expression underscores metabolic importance.
3. **Blood meal processing**: Blood-feeding generates a massive tryptophan load from hemoglobin digestion. The KP processes this potentially toxic excess.
4. **Malaria transmission**: Downstream product xanthurenic acid triggers Plasmodium gametogenesis in the mosquito midgut.
5. **Midgut homeostasis**: KP disruption impairs midgut permeability barrier and affects host-microbiota interface.
6. **Transformation marker**: The gene provides a visible phenotypic marker (eye color) for germline transformation in mosquito transgenesis.

## Notes on Existing Annotations

The GOA annotations are all computational:
- IBA (phylogenetic inference): TDO activity, heme binding -- supported by Drosophila vermilion orthology
- IEA (electronic annotation): TDO activity, heme binding, ommochrome biosynthesis, metal ion binding
- ISS (sequence similarity): TDO activity, heme binding, L-tryptophan catabolism (based on Q17P71)

The UniProt record also lists GO:0019441 (L-tryptophan catabolic process to kynurenine, ISS) and GO:0019442 (L-tryptophan catabolic process to acetyl-CoA, IBA) but these were not present in the GOA download.

Note: GO:0019442 (L-tryptophan catabolic process to acetyl-CoA) is an over-annotation for this enzyme. TDO only catalyzes the first step to N-formylkynurenine. The full pathway to acetyl-CoA requires many additional enzymes. GO:0019441 (to kynurenine) is more appropriate but still covers two enzymatic steps (TDO + formamidase).

## BioReason SFT Assessment Notes

The BioReason deep-research file correctly identifies:
- Heme-dependent dioxygenase activity
- Kynurenine pathway first step
- Heme binding
- Homotetramer assembly

Issues identified:
1. No literature citations in the trace -- all from InterPro/UniProt
2. Speculative interaction partners: "Hormone-sensitive lipase could modulate local lipid-derived NADPH production" -- no evidence
3. Claims about "GO:1902494 catalytic complex" -- no experimental evidence for TDO complex annotation
4. Mentions of AGAP006020-PA, AGAP009091-PA etc. as "regulatory or scaffolding factors" -- speculative STRING neighbors
5. The thinking trace is reasonable but generic; misses the organism-specific biology (eye pigmentation, blood meal processing, malaria transmission link)
6. No GO predictions listed in the MF/BP/CC sections despite discussing functions in the thinking trace
