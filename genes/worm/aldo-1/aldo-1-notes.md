# aldo-1 (C. elegans) Research Notes

Gene: aldo-1 (T05D4.1, WBGene00011474)
UniProt: P54216
Protein: Fructose-bisphosphate aldolase 1, also known as Aldolase CE-1

## Summary of Gene Biology

aldo-1 encodes one of two fructose-1,6-bisphosphate aldolase isozymes in C. elegans (the other being aldo-2/CE-2). It is a class I aldolase that catalyzes the reversible cleavage of fructose-1,6-bisphosphate (FBP) into glyceraldehyde-3-phosphate (G3P) and dihydroxyacetone phosphate (DHAP), a key step in glycolysis (step 4/4 in the conversion of glucose to triose phosphates) and gluconeogenesis.

## Key Literature Findings

### PMID:9056253 - Inoue et al. 1997 (Arch Biochem Biophys)
Title: "Caenorhabditis elegans has two isozymic forms, CE-1 and CE-2, of fructose-1,6-bisphosphate aldolase which are encoded by different genes."

- Two distinct cDNAs (Ce-1 and Ce-2) isolated; both encode 366 amino acid proteins
- CE-1 (aldo-1) and CE-2 (aldo-2) are encoded by different genes (Southern blot confirmed)
- CE-1 has unique kinetic properties: KM = 16.7 uM for FBP, KM = 0.56 mM for fructose-1-phosphate
- CE-1 exhibits broader substrate specificity than CE-2
- CE-2 is more similar to vertebrate aldolase C, while CE-1 has unique characteristics
- Highest sequence diversity between CE-1 and CE-2 is in the C-terminal region (isozyme-specific)
- EC assigned: 4.1.2.13 (IDA evidence)
[PMID:9056253 "CE-1 evolved to act as an intrinsic enzyme that exhibits a much broader substrate specificity than does CE-2"]

### PMID:21611156 - Meissner et al. 2011 (PLoS One)
Title: "Determining the sub-cellular localization of proteins within Caenorhabditis elegans body wall muscle."

- T05D4.1 (aldo-1) was GFP-tagged and localized in body wall muscle cells
- Classified in Category 6: "Dense bodies, Thick filaments and/or M-lines, ER/SR"
- T05D4.1::GFP was one of 3 proteins used to validate the Gateway approach vs. genomic clones (Figure 3A,B) -- localization was confirmed with both methods
- The study identified 227 GFP-tagged proteins with localized expression in body wall muscle
- This is high-quality HDA evidence for sarcomere, dense body, and ER localization
[PMID:21611156 "The sub-cellular localization for the T05D4.1::GFP (A, B)... proteins expressed from gateway clones using a muscle-specific promoter (A, B and C) or from genomic clones using endogenous promoters (B, D and F)"]

### PMID:14704431 - Li et al. 2004 (Science)
Title: "A map of the interactome network of the metazoan C. elegans."

- High-throughput Y2H screen identified >4000 interactions in C. elegans
- aldo-1 (P54216) self-interaction detected (identical protein binding)
- Part of the Worm Interactome WI5 map
[PMID:14704431 "more than 4000 interactions were identified from high-throughput, yeast two-hybrid (HT=Y2H) screens"]

### PMID:19123269 - Simonis et al. 2009 (Nat Methods)
Title: "Empirically controlled mapping of the Caenorhabditis elegans protein-protein interactome network."

- Expanded C. elegans interactome (WI-2007/WI8)
- aldo-1 self-interaction replicated/confirmed
- Quality-controlled dataset comparable to low-throughput literature data
[PMID:19123269 "the resulting dataset (Worm Interactome 2007 or WI-2007) is similar in quality to low-throughput data curated from the literature"]

## Expression and Tissue Distribution

- UniProt states: ubiquitous expression, all developmental stages
- Bgee: expressed in larva and 3 other cell types/tissues
- The Meissner et al. study used a muscle-specific promoter for GFP localization, so the muscle localization findings are for ectopically driven expression, but were confirmed with endogenous promoter constructs

## Quaternary Structure

- Class I aldolases are typically homotetrameric
- IntAct records 3 experiments showing aldo-1 self-interaction (P54216-P54216)
- The homotetrameric quaternary structure is important for enzyme stability but not strictly required for catalysis (monomers retain ~72% activity in other aldolases)
- The "identical protein binding" GO annotation reflects the self-interaction seen in Y2H

## Relationship to aldo-2 (CE-2)

- aldo-2 (P46563, F01F1.12) is the other C. elegans FBP aldolase
- aldo-2 is more similar to vertebrate aldolase C
- aldo-2 RNAi causes embryonic lethality (~75% of embryos die) [PMID:38947245]
- aldo-2 has been implicated as a potential epigenetic regulator during embryogenesis via histone lactylation

## C. elegans Metabolic Context

- C. elegans has functional glycolysis and gluconeogenesis pathways
- The daf-2/insulin signaling pathway regulates metabolic flux; daf-2 mutants show upregulated glycolytic enzymes
- Glucose toxicity in C. elegans is mediated partly through glycolytic intermediates including DHAP
- Genetic inhibition of aldolase (aldo-1/aldo-2) suppresses glucose toxicity and restores lifespan on high-glucose diets, suggesting DHAP accumulation from aldolase activity mediates glucose-induced aging

## BioReason Claims Assessment

The BioReason deep-research file claims:
1. GO:0042593 (glucose homeostasis) - NOT in existing GOA annotations. While aldo-1 participates in glycolysis which affects glucose levels, C. elegans lacks a blood glucose system. This term is more appropriate for vertebrates. The claim of "systemic sugar balance" is an overreach for a nematode.
2. Dense body/sarcomere/ER localization - CORRECT, supported by PMID:21611156
3. "Glycolytic metabolon" at sarcomeres - Plausible but speculative for C. elegans specifically. There is evidence from vertebrate muscle that glycolytic enzymes form metabolons at sarcomeres, and the dense body/ER localization of aldo-1 is consistent with this, but no direct evidence of a metabolon exists in C. elegans.
4. Homotetrameric assembly - CORRECT for class I aldolases generally

## Reference Verification

All PMIDs cited in the GOA annotations are REAL and verified:
- PMID:9056253 - Verified (Inoue et al. 1997, Arch Biochem Biophys)
- PMID:14704431 - Verified (Li et al. 2004, Science) 
- PMID:19123269 - Verified (Simonis et al. 2009, Nat Methods)
- PMID:21611156 - Verified (Meissner et al. 2011, PLoS One)
- GO_REF:0000033 - Standard phylogenetic annotation reference
- GO_REF:0000024 - Standard manual ISS transfer reference
- GO_REF:0000120 - Standard combined IEA method reference
