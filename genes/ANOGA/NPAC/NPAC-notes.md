# NPAC (ANOGA) - Research Notes

## Gene identity

- UniProt: Q7Q161 (GLYR1_ANOGA), Reviewed (Swiss-Prot)
- Gene: AGAP009949
- Organism: Anopheles gambiae (African malaria mosquito), NCBITaxon:7165
- Names: Cytokine-like nuclear factor N-PAC; Glyoxylate reductase 1 homolog; Nuclear protein NP60 homolog; Putative oxidoreductase GLYR1 homolog
- 566 amino acids
- Belongs to the HIBADH-related family, NP60 subfamily

## Orthologs

- Human: Q49A26 (GLYR1/NP60/NPAC/NDF/HIBDL)
- Drosophila melanogaster: Q8T079 (CG4747)
- The UniProt Q7Q161 entry is annotated entirely by homology transfer (ISS/IBA), with no direct experimental evidence in Anopheles gambiae itself.

## Domain architecture

- N-terminal PWWP domain (residues 9-70): chromatin reader that recognizes H3K36me3 and binds DNA
- Linker region (disordered, ~residues 127-274): includes the LSD2-interacting dodecapeptide in human ortholog
- C-terminal dehydrogenase domain (residues 274-566): Rossmann-fold NAD(P)-binding domain, structurally related to 6-phosphogluconate dehydrogenase/3-hydroxyisobutyrate dehydrogenase

## Key functional insights from ortholog studies

### 1. Nucleosome-destabilizing factor (NDF)
Fei et al. (2018) [PMID:29759984] identified the Drosophila ortholog CG4747 and human GLYR1 as NDF, "a nucleosome-destabilizing factor that facilitates transcription through nucleosomes." Key findings:
- NDF interacts with nucleosomes near the dyad
- Destabilizes nucleosomes in an ATP-independent manner
- Facilitates Pol II transcription through nucleosomes
- Stimulates H3K56 acetylation by p300 on nucleosomal substrates
- Recruited to transcribed regions of thousands of genes upon transcriptional induction
- Colocalizes with H3K36me3-enriched regions
- The PWWP domain recognizes H3K36me3, but H3K36me3 is "necessary but not sufficient" for localization
- Essential in human stem cells
- Overexpressed in ~21% of breast cancers

### 2. Cofactor of LSD2/KDM1B histone demethylase
Fang et al. (2013) [PMID:23260659] showed NPAC/GLYR1 is a cofactor of LSD2/KDM1B:
- Stimulates H3K4me1 and H3K4me2 demethylation
- The minimal functional segment is a dodecapeptide (residues 214-225)
- Residue F217 stabilizes enzyme-substrate interaction
- Crystal structures of LSD2 alone and LSD2-NPAC complex were determined

### 3. Co-factor of H3K36me3 in transcriptional elongation
Yu et al. (2021) [PMID:33676077] showed in mouse ESCs:
- Npac co-localizes with H3K36me3 in gene bodies of actively transcribed genes
- Interacts with p-TEFb (positive transcription elongation factor b)
- Interacts with Ser2-phosphorylated and Ser5-phosphorylated RNA Pol II
- Depletion disrupts transcriptional elongation of pluripotency genes (Nanog, Rif1)
- Required for mESC pluripotency maintenance

### 4. Interaction with MSL complex (from Drosophila ortholog, transferred to Anopheles)
UniProt CC for Q7Q161 states (by similarity to Q8T079):
- "Binds to mononucleosomes"
- "Interacts with male-specific lethal (MSL) histone acetyltransferase complex at least composed of mof, msl-1, msl-2 and msl-3"
The MSL complex in Drosophila acetylates H4K16 for dosage compensation on the male X chromosome.

### 5. Dehydrogenase domain is catalytically inert
Fang et al. (2013) [PMID:23260659]: "attempts to identify the intrinsic enzymatic activity of NPAC as a potential dehydrogenase...were unsuccessful." The dehydrogenase domain instead serves as "a catalytically inert oligomerization module" that forms a stable tetramer.

UniProt CC for Q7Q161: "the active site is not conserved, the dehydrogenase domain seems to serve as a catalytically inert oligomerization module"

### 6. Chromatin localization depends on H3K36me3
UniProt CC (by similarity to Drosophila Q8T079): "Localization to open chromatin depends on H3K36 trimethylation by Set2."

## GO annotations in GOA (8 annotations)

| GO ID | Term | Qualifier | Evidence | Reference |
|-------|------|-----------|----------|-----------|
| GO:0003677 | DNA binding | enables | IBA | GO_REF:0000033 |
| GO:0003682 | chromatin binding | enables | IEA | GO_REF:0000117 (ARBA) |
| GO:0031491 | nucleosome binding | enables | IBA | GO_REF:0000033 |
| GO:0050661 | NADP binding | enables | IEA | GO_REF:0000002 (InterPro:IPR006115) |
| GO:0051287 | NAD binding | enables | IEA | GO_REF:0000002 (InterPro:IPR029154) |
| GO:0140673 | transcription elongation-coupled chromatin remodeling | involved_in | IBA | GO_REF:0000033 |
| GO:0000785 | chromatin | is_active_in | IBA | GO_REF:0000033 |
| GO:0005694 | chromosome | located_in | IEA | GO_REF:0000044 |

## InterPro2GO annotations (GO_REF:0000002)

Two InterPro2GO annotations:
- IPR006115 -> GO:0050661 (NADP binding): Based on the 6-phosphogluconate dehydrogenase NADP-binding domain
- IPR029154 -> GO:0051287 (NAD binding): Based on the 3-hydroxyisobutyrate dehydrogenase-like NAD-binding domain

These are technically correct structurally (the Rossmann fold does bind NAD(P)), but the dehydrogenase domain is catalytically inert. The NAD(P) binding may be structural/regulatory rather than enzymatic.

## Key references

1. PMID:12364791 - Holt et al. (2002) "The genome sequence of the malaria mosquito Anopheles gambiae." Science 298:129-149. [Genome sequencing, source of the gene model]
2. PMID:29759984 - Fei et al. (2018) "NDF, a nucleosome-destabilizing factor that facilitates transcription through nucleosomes." Genes Dev 32:682-694. [Key functional characterization in Drosophila and human]
3. PMID:23260659 - Fang et al. (2013) "LSD2/KDM1B and its cofactor NPAC/GLYR1 endow a structural and molecular model for regulation of H3K4 demethylation." Mol Cell 49:558-70. [LSD2 cofactor function, crystal structures]
4. PMID:33676077 - Yu et al. (2021) "Npac Is A Co-factor of Histone H3K36me3 and Regulates Transcriptional Elongation in Mouse Embryonic Stem Cells." Genomics Proteomics Bioinformatics 20:110-128. [H3K36me3 reader, p-TEFb interaction, elongation function]

## Summary assessment

NPAC/GLYR1/NDF is a multifunctional chromatin-associated protein whose core biology is well-characterized in human and Drosophila but entirely inferred by homology for the Anopheles ortholog. The protein reads H3K36me3 marks via its PWWP domain, destabilizes nucleosomes to facilitate RNA Pol II transcription elongation, cofactors LSD2-mediated H3K4 demethylation, and stimulates H3K56 acetylation by p300. The dehydrogenase-like C-terminal domain is catalytically inert but serves as an oligomerization platform. In Drosophila, it also interacts with the MSL dosage compensation complex.
