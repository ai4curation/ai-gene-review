---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:31:37.329527'
end_time: '2026-09-10T14:40:59.140559'
duration_seconds: 561.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: amon
  gene_symbol: amon
  uniprot_accession: Q9VBC7
  protein_description: 'RecName: Full=Neuroendocrine convertase 2 {ECO:0000305}; Short=NEC
    2 {ECO:0000305}; EC=3.4.21.94 {ECO:0000269|PubMed:10749852}; AltName: Full=DMH
    #5 {ECO:0000303|PubMed:10436051}; AltName: Full=Prohormone convertase 2 {ECO:0000303|PubMed:10749852};
    Short=dPC2 {ECO:0000303|PubMed:10749852}; AltName: Full=Protein amontillado {ECO:0000303|PubMed:10436051};
    Flags: Precursor;'
  gene_info: Name=amon {ECO:0000303|PubMed:10436051, ECO:0000312|FlyBase:FBgn0023179};
    ORFNames=CG6438 {ECO:0000312|FlyBase:FBgn0023179};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the peptidase S8 family. Furin subfamily.
  protein_domains: Galactose-bd-like_sf. (IPR008979); Kexin/furin. (IPR034182); P_dom.
    (IPR002884); Peptidase_S8/S53_dom. (IPR000209); Peptidase_S8/S53_dom_sf. (IPR036852)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: amon-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VBC7
- **Protein Description:** RecName: Full=Neuroendocrine convertase 2 {ECO:0000305}; Short=NEC 2 {ECO:0000305}; EC=3.4.21.94 {ECO:0000269|PubMed:10749852}; AltName: Full=DMH #5 {ECO:0000303|PubMed:10436051}; AltName: Full=Prohormone convertase 2 {ECO:0000303|PubMed:10749852}; Short=dPC2 {ECO:0000303|PubMed:10749852}; AltName: Full=Protein amontillado {ECO:0000303|PubMed:10436051}; Flags: Precursor;
- **Gene Information:** Name=amon {ECO:0000303|PubMed:10436051, ECO:0000312|FlyBase:FBgn0023179}; ORFNames=CG6438 {ECO:0000312|FlyBase:FBgn0023179};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase S8 family. Furin subfamily.
- **Key Domains:** Galactose-bd-like_sf. (IPR008979); Kexin/furin. (IPR034182); P_dom. (IPR002884); Peptidase_S8/S53_dom. (IPR000209); Peptidase_S8/S53_dom_sf. (IPR036852)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "amon" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'amon' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **amon** (gene ID: amon, UniProt: Q9VBC7) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VBC7
- **Protein Description:** RecName: Full=Neuroendocrine convertase 2 {ECO:0000305}; Short=NEC 2 {ECO:0000305}; EC=3.4.21.94 {ECO:0000269|PubMed:10749852}; AltName: Full=DMH #5 {ECO:0000303|PubMed:10436051}; AltName: Full=Prohormone convertase 2 {ECO:0000303|PubMed:10749852}; Short=dPC2 {ECO:0000303|PubMed:10749852}; AltName: Full=Protein amontillado {ECO:0000303|PubMed:10436051}; Flags: Precursor;
- **Gene Information:** Name=amon {ECO:0000303|PubMed:10436051, ECO:0000312|FlyBase:FBgn0023179}; ORFNames=CG6438 {ECO:0000312|FlyBase:FBgn0023179};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase S8 family. Furin subfamily.
- **Key Domains:** Galactose-bd-like_sf. (IPR008979); Kexin/furin. (IPR034182); P_dom. (IPR002884); Peptidase_S8/S53_dom. (IPR000209); Peptidase_S8/S53_dom_sf. (IPR036852)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "amon" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'amon' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **amon** (gene ID: amon, UniProt: Q9VBC7) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster amontillado* (*amon*; Q9VBC7)

## Executive conclusion

The requested identity is verified. *amon* (amontillado; CG6438; UniProt Q9VBC7) in *Drosophila melanogaster* encodes AMON/dPC2, the fly ortholog of neuroendocrine prohormone convertase 2—not an unrelated similarly named gene. AMON is a soluble, subtilisin-like serine endoprotease of the peptidase-S8/kexin-furin group. It functions in the regulated secretory pathway of peptidergic neurons and endocrine cells, where it cleaves inactive peptide precursors after basic residues so that downstream trimming and modification enzymes can generate bioactive neuropeptides and peptide hormones. The best-established endogenous target is the adipokinetic-hormone (AKH) precursor; AMON-dependent AKH maturation is required for normal circulating carbohydrate levels. Broader peptidomics demonstrates that AMON is required for efficient production of numerous neural, corpora-cardiaca, perisympathetic-organ, and enteroendocrine peptides. (pauls2014peptidomicsandprocessing pages 5-6, wegener2011deficiencyofprohormone pages 1-2, rhea2010theproproteinconvertase pages 4-6)

| Annotation question | Best-supported conclusion | Key experimental evidence or quantitative result | Confidence and caveat |
|---|---|---|---|
| Identity and orthology | *Drosophila melanogaster amontillado* (*amon*; CG6438; Q9VBC7) encodes dPC2, the fly ortholog of neuroendocrine prohormone convertase 2. | AMON is 66% identical overall and 75% identical in its catalytic domain to human PC2. Independent genetic and biochemical studies identify the same locus as PC2-like (Siekhaus and Fuller 1999; Rayburn et al. 2003; Pauls et al. 2014). (pauls2014peptidomicsandprocessing pages 5-6, rayburn2003amontilladothedrosophila pages 1-2, siekhaus1999arolefor pages 7-9) | **High.** Organism, symbol, locus, protein description, and architecture agree; no conflicting same-symbol protein was used. |
| Domains and catalytic mechanism | AMON is a soluble secretory-pathway subtilisin/kexin-family serine endoprotease with a signal peptide, prodomain, peptidase-S8 catalytic domain, P-domain, and short C-terminal extension. It lacks a transmembrane domain and uses an Asp–His–Ser catalytic triad plus an oxyanion-hole Asp. | Sequence analysis shows canonical PC2 architecture and conserved catalytic residues. Wild-type AMON rescues hatching and developmental defects, whereas the catalytic-His H237A variant and other catalytic-residue substitutions fail or rescue poorly (Siekhaus and Fuller 1999; Rayburn et al. 2003). (pauls2014peptidomicsandprocessing pages 5-6, rayburn2003amontilladothedrosophila pages 9-10, siekhaus1999arolefor pages 2-3, siekhaus1999arolefor pages 7-9) | **High** for architecture and the requirement for proteolytic activity. Purified-enzyme kinetics were not identified. |
| Cleavage specificity | AMON cleaves peptide-hormone precursors on the C-terminal side of basic sites. Likely sites include monobasic Arg and dibasic RR, KR, RK, and KK. | AMON displayed activity against a KR-containing synthetic substrate in S2 cells when coexpressed with d7B2. Mutant peptidomics supports processing at multiple mono- and dibasic precursor sites (Rayburn et al. 2003; Pauls et al. 2014). (pauls2014peptidomicsandprocessing pages 5-6, rayburn2003amontilladothedrosophila pages 1-2) | **Moderate.** Basic-site endoprotease activity is well supported, but AMON-specific preferences and kinetic constants for the complete site panel have not been measured comprehensively. |
| Maturation and 7B2 | AMON is synthesized as a zymogen, undergoes autocatalytic maturation, and depends on neuroendocrine chaperone d7B2 for efficient production or release of fully active enzyme. | In cultured Drosophila S2 cells, AMON activity toward a KR substrate required d7B2 coexpression. Its conserved prodomain and PC2 architecture support autocatalytic activation (Rayburn et al. 2003; Pauls et al. 2014). (pauls2014peptidomicsandprocessing pages 5-6, rayburn2003amontilladothedrosophila pages 1-2) | **Moderate–high.** Cellular evidence directly supports 7B2 dependence; the exact compartmental timing and complete endogenous maturation sequence are less fully mapped. |
| Subcellular and tissue localization | AMON operates in the regulated secretory pathway associated with peptide-containing dense-core vesicles or granules in peptidergic neurons and endocrine cells. Expression occurs in subsets of brain and ventral-nerve-cord neurons, corpora cardiaca AKH cells, and gut enteroendocrine cells. | In situ analysis identified about 168 late-embryonic brain and ventral-cord cells plus anterior sensory structures. Later studies demonstrated expression in the CNS, gut, corpora cardiaca, and multiple identified peptidergic cell classes (Siekhaus and Fuller 1999; Wegener et al. 2011; Pauls et al. 2014). (pauls2014peptidomicsandprocessing pages 5-6, siekhaus1999arolefor pages 1-2, wegener2011deficiencyofprohormone pages 1-2) | **High** for tissue and cell distribution and for assignment to the regulated secretory pathway. Dense-core-vesicle localization rests more on pathway evidence and PC2 biology than on high-resolution endogenous AMON imaging. |
| Strongest substrate and pathway: AKH | The adipokinetic hormone precursor is the best-established endogenous AMON target. In corpora cardiaca cells, AMON acts upstream of mature AKH production and thereby supports glucose and trehalose homeostasis. | AKH-cell-specific *amon* RNAi caused hypoglycemia; AKH-cell-specific AMON restored sugar levels, and induced AKH bypassed AMON knockdown. Larval AKH or AKHGK was detected in 0 of 18 mutants versus 89% of controls. Adult AKH relative to internal standard fell from 2.14 to 0.13, AKHGK fell from 1.974 to 0.15, and five-day male AKH content fell from 174 ± 9 to 20 ± 8 fmol per corpus cardiacum (Rhea et al. 2010). (rhea2010theproproteinconvertase pages 4-6, rhea2010theproproteinconvertase pages 1-2, rhea2010theproproteinconvertase pages 6-8, rhea2010theproproteinconvertase pages 8-9) | **High.** Cell-specific genetics, rescue and epistasis, and mass spectrometry converge. Direct cleavage kinetics with purified AMON were not reported. |
| Broader peptide processing | AMON is the principal canonical PC2-like convertase for maturation of many Drosophila neuropeptides and gut peptide hormones, although dependence varies with peptide, tissue, and life stage. | AMON deficiency strongly reduced or eliminated peptide signals from larval ring glands and perisympathetic organs. AKH was about 16-fold lower after AMON depletion. Most enteroendocrine peptides were absent or reduced, although 3 of 24 adult gut peptides retained control-frequency detection; CNS detection frequencies were often preserved despite likely lower abundance (Wegener et al. 2011; Pauls et al. 2014). (wegener2011deficiencyofprohormone pages 1-2, pauls2014peptidomicsandprocessing pages 6-7) | **High** for a broad processing role; **moderate** for classifying each affected peptide as a direct substrate because abundance changes can include indirect effects or residual processing. |
| Developmental phenotypes | AMON-dependent peptide maturation is required for embryonic hatching behavior, larval growth and ecdysis, later molts, and pupal development. | Deficient embryos retained touch responses and gross anatomy but showed markedly reduced head-swinging and hatching. Mutants displayed partial embryonic lethality, growth delay, duplicated mouthparts, and arrest at the first-to-second-instar molt. Repeated wild-type *amon* expression rescued hatching, growth, and molting, whereas catalytic-mutant AMON did not (Siekhaus and Fuller 1999; Rayburn et al. 2003; Wegener et al. 2011). (rayburn2003amontilladothedrosophila pages 9-10, siekhaus1999arolefor pages 1-2, siekhaus1999arolefor pages 7-9) | **High** for developmental requirement and catalytic dependence. EH, ETH, and CCAP precursors remain candidate mediators of hatching or ecdysis defects rather than confirmed direct substrates. |
| 2023–2024 evidence status | No major 2023–2024 study was identified that directly revised AMON enzymology, substrate specificity, or primary functional annotation. | The most detailed direct AMON evidence remains the genetic, cellular, biochemical, and peptidomic work published from 1999 through 2014 and summarized above. (pauls2014peptidomicsandprocessing pages 5-6, wegener2011deficiencyofprohormone pages 1-2, rhea2010theproproteinconvertase pages 4-6) | **Evidence gap.** Recent Drosophila neuroendocrine research supplies systems-level context but should not be treated as new AMON-specific biochemical validation or as a clinical application. |


*Table: Compact evidence matrix for the identity, enzymology, localization, substrates, and biological functions of Drosophila AMON. It distinguishes experimentally strong conclusions from inference and identifies the lack of major direct AMON-specific advances in 2023–2024.*

## 1. Identity verification

### Required checks

1. **Symbol and description:** The literature consistently identifies *amontillado* (*amon*) as encoding Drosophila prohormone convertase 2, also called dPC2 or AMON. This agrees with UniProt Q9VBC7’s description “neuroendocrine convertase 2/prohormone convertase 2.” (rayburn2003amontilladothedrosophila pages 1-2, siekhaus1999arolefor pages 1-2)
2. **Organism:** The experimental studies concern *Drosophila melanogaster*. The locus was mapped to chromosome region 97D1–2 and analyzed through deletion, EMS alleles, transgenes, and cell-specific RNAi. (rayburn2003amontilladothedrosophila pages 9-10, siekhaus1999arolefor pages 7-9)
3. **Family and domains:** AMON has a signal sequence, prodomain, subtilisin-family catalytic domain, PC2/Kex2-type P-domain, and short C-terminal extension, but no transmembrane domain. It is 66% identical overall and approximately 75% identical in the catalytic domain to human PC2. This architecture agrees with the supplied peptidase-S8/S53, kexin/furin, P-domain, and galactose-binding-like-superfamily annotations. (pauls2014peptidomicsandprocessing pages 5-6, siekhaus1999arolefor pages 2-3, siekhaus1999arolefor pages 7-9)
4. **Ambiguity check:** No evidence was used from a different organism’s similarly named gene. Comparative insect PC2 literature was considered only as evolutionary context, not as evidence about the identity of Q9VBC7.

**Confidence:** very high.

## 2. Primary molecular function

AMON is an endoprotease that converts larger, inactive prohormones or proneuropeptides into intermediates from which active signaling peptides are produced. Its general reaction can be represented as:

**propeptide–basic cleavage site–propeptide + H₂O → two peptide products with new termini.**

The enzyme uses the conserved subtilisin-like Asp–His–Ser catalytic triad and an oxyanion-hole Asp characteristic of PC2. The P-domain contributes to folding, stability, calcium dependence, and pH-dependent activity. The requirement for proteolysis is demonstrated genetically: wild-type AMON rescues hatching and developmental defects, whereas H237A substitution of the catalytic histidine does not; other catalytic-residue substitutions also substantially impair rescue. (rayburn2003amontilladothedrosophila pages 1-2, rayburn2003amontilladothedrosophila pages 9-10, siekhaus1999arolefor pages 7-9)

### Cleavage specificity

Available evidence supports cleavage on the C-terminal side of basic residues, including monobasic Arg and dibasic RR, KR, RK, and KK sites. AMON showed activity against a KR-containing synthetic substrate in Drosophila S2 cells when d7B2 was coexpressed. Nevertheless, a systematic purified-enzyme specificity map or kinetic comparison of all candidate sites has not been reported. The full site list is therefore a PC2-informed and peptidomics-supported annotation rather than a complete direct biochemical determination for AMON. (pauls2014peptidomicsandprocessing pages 5-6, rayburn2003amontilladothedrosophila pages 1-2)

This distinction is important: decreases in mature peptides in an *amon* mutant strongly establish a requirement for AMON but do not prove that every affected precursor is bound and cleaved directly by AMON.

## 3. Biosynthesis, activation, and localization

AMON is synthesized as a secretory precursor. Its N-terminal signal peptide directs entry into the endoplasmic-reticulum/Golgi secretory pathway; the prodomain initially supports folding and inhibits premature catalysis. AMON undergoes autocatalytic maturation, while efficient production or release of fully active enzyme depends on the neuroendocrine chaperone 7B2. The S2-cell assay showing d7B2-dependent activity against a KR substrate provides direct cellular support for this relationship. (pauls2014peptidomicsandprocessing pages 5-6, rayburn2003amontilladothedrosophila pages 1-2)

Because AMON lacks a transmembrane domain, it is not a cell-surface receptor or membrane-tethered convertase. It acts as a soluble luminal enzyme in the regulated secretory pathway, associated with peptide-containing dense-core granules/vesicles. Precursor cleavage is followed by enzymes such as carboxypeptidases, which remove residual basic residues, and amidating enzymes where required. (pauls2014peptidomicsandprocessing pages 5-6, wegener2011deficiencyofprohormone pages 1-2)

### Cellular and anatomical distribution

Embryonic in-situ hybridization detected *amon* in anterior sensory structures and approximately 168 cells of the brain and ventral nerve cord. Expression is strongly developmentally regulated: it is prominent late in embryogenesis, falls after hatching in many cells, persists in subsets of larval neurons, rises during late pupal development, and peaks again in adults. (rayburn2003amontilladothedrosophila pages 9-10, siekhaus1999arolefor pages 1-2, siekhaus1999arolefor pages 7-9)

Subsequent work found expression in:

- peptidergic neurons of the brain and ventral nervous system;
- corpora cardiaca endocrine cells producing AKH;
- enteroendocrine cells of the gut;
- identified neuronal populations expressing CAPA peptides, HUGIN-pyrokinin, FMRFamide-like peptides, myosuppressin, short neuropeptide F, and corazonin. (pauls2014peptidomicsandprocessing pages 5-6, wegener2011deficiencyofprohormone pages 1-2)

The regulated-secretory-pathway assignment is strong. However, the available primary evidence is stronger for expression and pathway localization than for nanometer-scale imaging of endogenous AMON within individual dense-core vesicles.

## 4. Best-established substrate pathway: AKH maturation and carbohydrate homeostasis

AKH is the most rigorously established endogenous AMON-dependent product. In corpora cardiaca cells, the AKH precursor enters the secretory pathway, is cleaved by signal peptidase and AMON, trimmed by a carboxypeptidase to an AKH-GK intermediate, and subsequently modified to mature AKH. AMON loss reduces both mature AKH and AKH-GK, indicating failure early in this processing sequence. (rhea2010theproproteinconvertase pages 6-8)

Multiple forms of evidence establish causal ordering:

- AKH-cell-specific *amon* RNAi lowers combined glucose and trehalose and phenocopies AKH-cell ablation.
- Restoring AMON specifically in AKH cells of an *amon* mutant restores normal sugar levels.
- Induced AKH expression bypasses the hypoglycemia caused by *amon* knockdown, placing AMON upstream of the hormone.
- Mass spectrometry directly detects severe loss of mature AKH and AKH-GK. (rhea2010theproproteinconvertase pages 4-6, rhea2010theproproteinconvertase pages 1-2)

Quantitatively, larval AKH/AKH-GK was absent from all 18 mutant ring glands examined, compared with detection in 89% of controls. In adults five days after the last AMON induction, the AKH/internal-standard ratio fell from 2.14 in controls to 0.13 in mutants, while AKH-GK/internal-standard fell from 1.974 to 0.15. Five-day male AKH content declined from 174 ± 9 to 20 ± 8 fmol per corpus cardiacum; corresponding female values were 178 ± 54 versus 22 ± 10 fmol. At 10–14 days, male values were 167 ± 83 versus 11 ± 7 and female values were 205 ± 114 versus 6 ± 3 fmol. (rhea2010theproproteinconvertase pages 6-8, rhea2010theproproteinconvertase pages 8-9)

These experiments provide the strongest annotation-quality conclusion: **AMON proteolytically enables AKH maturation in corpora cardiaca endocrine cells, thereby supporting normal carbohydrate mobilization and hemolymph sugar homeostasis.**

## 5. Broader neuropeptide-processing role

Mass-spectrometric profiling of *amon* deficiency shows that AMON is not AKH-specific. Peptide-hormone signals were strongly reduced or lost from larval ring glands and perisympathetic organs, and most assayed enteroendocrine peptides were absent or greatly reduced in mutant larvae and adults. After AMON depletion, AKH was approximately 16-fold lower than in controls. Only 3 of 24 adult enteroendocrine peptides retained control-frequency detection. (pauls2014peptidomicsandprocessing pages 6-7, wegener2011deficiencyofprohormone pages 1-2)

Dependence is not uniform. CNS peptide detection frequencies were often not significantly changed, although concentrations could still be reduced, and some adult corpora-cardiaca peptide signals persisted after transient heat-shock rescue. Adult AKH/AKH-GK was detected in 88% of mutants versus 94% of controls despite markedly reduced abundance. These observations imply residual enzyme, slower peptide turnover, alternative cleavage enzymes, or tissue- and stage-specific redundancy—not that AMON is dispensable. (rhea2010theproproteinconvertase pages 4-6, pauls2014peptidomicsandprocessing pages 6-7)

Accordingly, AMON is best described as the fly’s **principal canonical PC2-like convertase for regulated peptide maturation**, rather than as an absolutely exclusive processor of every neuropeptide. (pauls2014peptidomicsandprocessing pages 6-7)

## 6. Developmental and physiological processes

### Hatching

Embryos lacking the *amon* region retain gross anatomy and touch responsiveness but show greatly reduced head-swinging behavior required for hatching. Ubiquitous wild-type *amon* expression substantially restores this behavior, whereas catalytically inactive H237A AMON does not. The result links AMON-dependent proteolysis—not merely protein presence—to production of one or more hatching signals. (siekhaus1999arolefor pages 1-2, siekhaus1999arolefor pages 7-9)

### Larval growth and ecdysis

Defined *amon* alleles cause partial embryonic lethality, delayed or reduced larval growth, duplicated mouthparts, and arrest during the first-to-second-instar molt. Mutants undergo aspects of molting such as apolysis and production of new mouthparts but fail to complete ecdysis. Repeated heat-shock expression of wild-type AMON rescues growth and molting; rescued larvae can arrest at the next molt if AMON is no longer supplied, demonstrating recurrent stage requirements. (rayburn2003amontilladothedrosophila pages 9-10)

Later depletion experiments likewise showed failure of third-instar larvae to enter the wandering phase and complete ecdysis. Candidate mediators include eclosion hormone, ecdysis-triggering hormone, and crustacean cardioactive peptide, but the retrieved studies do not establish these precursors as direct AMON substrates. They should remain mechanistic hypotheses rather than definitive annotations. (wegener2011deficiencyofprohormone pages 1-2, rayburn2003amontilladothedrosophila pages 9-10)

### Later development

Expression rises in late pupae and adults, and genetic work supports additional pupal requirements. Overall lethality and pleiotropy are most parsimoniously explained by simultaneous failure to mature multiple peptide hormones rather than by a direct structural role for AMON. (rayburn2003amontilladothedrosophila pages 9-10, wegener2011deficiencyofprohormone pages 1-2)

## 7. Current applications and expert interpretation

AMON is used experimentally as:

- a genetic lever for suppressing regulated peptide maturation in selected neuroendocrine cells;
- a pathway-level test of whether a phenotype depends on processed peptide hormones rather than precursor transcription alone;
- a comparator for mammalian PC2 and for evolutionary studies of insect prohormone-convertase systems;
- a component of Drosophila models investigating endocrine control of metabolism, development, behavior, and gut–brain signaling.

Its clearest real-world implementation is therefore as a research tool and model-system enzyme, not as an approved diagnostic or therapeutic target. Tissue-specific RNAi, GAL4/UAS restoration, catalytic-mutant complementation, MALDI-TOF/LC–MS peptidomics, and hormone-bypass experiments together provide an unusually strong framework for functional annotation. (siekhaus1999arolefor pages 7-9, rhea2010theproproteinconvertase pages 4-6, rhea2010theproproteinconvertase pages 10-11)

The expert interpretation in the peptidomics literature is that AMON is the major canonical convertase responsible for Drosophila regulatory-peptide processing. This is well supported at the systems level, but substrate-by-substrate direct cleavage assays remain incomplete. (pauls2014peptidomicsandprocessing pages 5-6, pauls2014peptidomicsandprocessing pages 6-7)

## 8. Recent research status, 2023–2024

Targeted searches identified substantial 2023–2024 progress in Drosophila neuroendocrine connectomics, single-cell transcriptomics, dense-core-vesicle release, and individual peptide maturation. However, no major 2023–2024 study was found that directly revised AMON’s catalytic mechanism, provided a purified-enzyme specificity atlas, or superseded the foundational AMON experiments. Consequently, the most authoritative direct evidence remains the primary genetic and biochemical literature from 1999–2011 and the 2014 peptidomics synthesis. This is a genuine recency gap and should not be obscured by citing newer but only tangential systems-level studies.

## 9. Evidence-weighted annotation

**Recommended primary annotation:**

> AMON/Q9VBC7 is the soluble Drosophila PC2-like serine endoprotease of neuroendocrine dense-core secretory vesicles. Assisted by 7B2 and activated from a proenzyme, it cleaves proneuropeptide and prohormone precursors after basic residues, enabling downstream trimming and modification into bioactive peptides. Its best-validated substrate pathway is AKH maturation in corpora cardiaca cells, required for carbohydrate homeostasis; broader activity is required for efficient production of numerous neural and gut peptide hormones and for peptide-dependent hatching, growth, molting, and ecdysis.

**Confidence by component:** identity and catalytic class, very high; secretory-pathway localization, high; AKH pathway, very high; broad peptide-processing role, high; exact residue-level substrate preferences, moderate; assignment of individual ecdysis peptides as direct substrates, currently insufficient.

## Key publications

- Siekhaus DE, Fuller RS. “A Role for *amontillado*, the Drosophila Homolog of the Neuropeptide Precursor Processing Protease PC2, in Triggering Hatching Behavior.” *Journal of Neuroscience*. **15 August 1999**. https://doi.org/10.1523/JNEUROSCI.19-16-06942.1999 (siekhaus1999arolefor pages 1-2)
- Rayburn LYM et al. “*amontillado*, the Drosophila Homolog of the Prohormone Processing Protease PC2, Is Required During Embryogenesis and Early Larval Development.” *Genetics*. **January 2003**. https://doi.org/10.1093/genetics/163.1.227 (rayburn2003amontilladothedrosophila pages 1-2)
- Rhea JM, Wegener C, Bender M. “The Proprotein Convertase Encoded by *amontillado* (*amon*) Is Required in Drosophila Corpora Cardiaca Endocrine Cells Producing the Glucose Regulatory Hormone AKH.” *PLoS Genetics*. **27 May 2010**. https://doi.org/10.1371/journal.pgen.1000967 (rhea2010theproproteinconvertase pages 1-2)
- Wegener C et al. “Deficiency of Prohormone Convertase dPC2 (AMONTILLADO) Results in Impaired Production of Bioactive Neuropeptide Hormones in Drosophila.” *Journal of Neurochemistry*. **August 2011**. https://doi.org/10.1111/j.1471-4159.2010.07130.x (wegener2011deficiencyofprohormone pages 1-2)
- Pauls D et al. “Peptidomics and Processing of Regulatory Peptides in the Fruit Fly Drosophila.” *EuPA Open Proteomics*. **June 2014**. https://doi.org/10.1016/j.euprot.2014.02.007 (pauls2014peptidomicsandprocessing pages 5-6)

References

1. (pauls2014peptidomicsandprocessing pages 5-6): Dennis Pauls, Jiangtian Chen, Wencke Reiher, Jens T. Vanselow, Andreas Schlosser, Jörg Kahnt, and Christian Wegener. Peptidomics and processing of regulatory peptides in the fruit fly drosophila. Eupa Open Proteomics, 3:114-127, Jun 2014. URL: https://doi.org/10.1016/j.euprot.2014.02.007, doi:10.1016/j.euprot.2014.02.007. This article has 42 citations and is from a peer-reviewed journal.

2. (wegener2011deficiencyofprohormone pages 1-2): Christian Wegener, Henrik Herbert, Jörg Kahnt, Michael Bender, and Jeanne M. Rhea. Deficiency of prohormone convertase dpc2 (amontillado) results in impaired production of bioactive neuropeptide hormones in drosophila. Journal of Neurochemistry, 118:581-595, Aug 2011. URL: https://doi.org/10.1111/j.1471-4159.2010.07130.x, doi:10.1111/j.1471-4159.2010.07130.x. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (rhea2010theproproteinconvertase pages 4-6): Jeanne M. Rhea, Christian Wegener, and Michael Bender. The proprotein convertase encoded by amontillado (amon) is required in drosophila corpora cardiaca endocrine cells producing the glucose regulatory hormone akh. PLoS Genetics, 6(5):e1000967, May 2010. URL: https://doi.org/10.1371/journal.pgen.1000967, doi:10.1371/journal.pgen.1000967. This article has 67 citations and is from a domain leading peer-reviewed journal.

4. (rayburn2003amontilladothedrosophila pages 1-2): Lowell Y M Rayburn, Holly C Gooding, Semil P Choksi, Dhea Maloney, Ambrose R Kidd, Daria E Siekhaus, and Michael Bender. <i>amontillado</i> , the drosophila homolog of the prohormone processing protease pc2, is required during embryogenesis and early larval development. Genetics, 163(1):227-237, Jan 2003. URL: https://doi.org/10.1093/genetics/163.1.227, doi:10.1093/genetics/163.1.227. This article has 52 citations and is from a domain leading peer-reviewed journal.

5. (siekhaus1999arolefor pages 7-9): Daria E. Siekhaus and Robert S. Fuller. A role for amontillado, the drosophilahomolog of the neuropeptide precursor processing protease pc2, in triggering hatching behavior. The Journal of Neuroscience, 19:6942-6954, Aug 1999. URL: https://doi.org/10.1523/jneurosci.19-16-06942.1999, doi:10.1523/jneurosci.19-16-06942.1999. This article has 87 citations.

6. (rayburn2003amontilladothedrosophila pages 9-10): Lowell Y M Rayburn, Holly C Gooding, Semil P Choksi, Dhea Maloney, Ambrose R Kidd, Daria E Siekhaus, and Michael Bender. <i>amontillado</i> , the drosophila homolog of the prohormone processing protease pc2, is required during embryogenesis and early larval development. Genetics, 163(1):227-237, Jan 2003. URL: https://doi.org/10.1093/genetics/163.1.227, doi:10.1093/genetics/163.1.227. This article has 52 citations and is from a domain leading peer-reviewed journal.

7. (siekhaus1999arolefor pages 2-3): Daria E. Siekhaus and Robert S. Fuller. A role for amontillado, the drosophilahomolog of the neuropeptide precursor processing protease pc2, in triggering hatching behavior. The Journal of Neuroscience, 19:6942-6954, Aug 1999. URL: https://doi.org/10.1523/jneurosci.19-16-06942.1999, doi:10.1523/jneurosci.19-16-06942.1999. This article has 87 citations.

8. (siekhaus1999arolefor pages 1-2): Daria E. Siekhaus and Robert S. Fuller. A role for amontillado, the drosophilahomolog of the neuropeptide precursor processing protease pc2, in triggering hatching behavior. The Journal of Neuroscience, 19:6942-6954, Aug 1999. URL: https://doi.org/10.1523/jneurosci.19-16-06942.1999, doi:10.1523/jneurosci.19-16-06942.1999. This article has 87 citations.

9. (rhea2010theproproteinconvertase pages 1-2): Jeanne M. Rhea, Christian Wegener, and Michael Bender. The proprotein convertase encoded by amontillado (amon) is required in drosophila corpora cardiaca endocrine cells producing the glucose regulatory hormone akh. PLoS Genetics, 6(5):e1000967, May 2010. URL: https://doi.org/10.1371/journal.pgen.1000967, doi:10.1371/journal.pgen.1000967. This article has 67 citations and is from a domain leading peer-reviewed journal.

10. (rhea2010theproproteinconvertase pages 6-8): Jeanne M. Rhea, Christian Wegener, and Michael Bender. The proprotein convertase encoded by amontillado (amon) is required in drosophila corpora cardiaca endocrine cells producing the glucose regulatory hormone akh. PLoS Genetics, 6(5):e1000967, May 2010. URL: https://doi.org/10.1371/journal.pgen.1000967, doi:10.1371/journal.pgen.1000967. This article has 67 citations and is from a domain leading peer-reviewed journal.

11. (rhea2010theproproteinconvertase pages 8-9): Jeanne M. Rhea, Christian Wegener, and Michael Bender. The proprotein convertase encoded by amontillado (amon) is required in drosophila corpora cardiaca endocrine cells producing the glucose regulatory hormone akh. PLoS Genetics, 6(5):e1000967, May 2010. URL: https://doi.org/10.1371/journal.pgen.1000967, doi:10.1371/journal.pgen.1000967. This article has 67 citations and is from a domain leading peer-reviewed journal.

12. (pauls2014peptidomicsandprocessing pages 6-7): Dennis Pauls, Jiangtian Chen, Wencke Reiher, Jens T. Vanselow, Andreas Schlosser, Jörg Kahnt, and Christian Wegener. Peptidomics and processing of regulatory peptides in the fruit fly drosophila. Eupa Open Proteomics, 3:114-127, Jun 2014. URL: https://doi.org/10.1016/j.euprot.2014.02.007, doi:10.1016/j.euprot.2014.02.007. This article has 42 citations and is from a peer-reviewed journal.

13. (rhea2010theproproteinconvertase pages 10-11): Jeanne M. Rhea, Christian Wegener, and Michael Bender. The proprotein convertase encoded by amontillado (amon) is required in drosophila corpora cardiaca endocrine cells producing the glucose regulatory hormone akh. PLoS Genetics, 6(5):e1000967, May 2010. URL: https://doi.org/10.1371/journal.pgen.1000967, doi:10.1371/journal.pgen.1000967. This article has 67 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](amon-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. rhea2010theproproteinconvertase pages 6-8
2. pauls2014peptidomicsandprocessing pages 6-7
3. rayburn2003amontilladothedrosophila pages 9-10
4. siekhaus1999arolefor pages 1-2
5. rayburn2003amontilladothedrosophila pages 1-2
6. rhea2010theproproteinconvertase pages 1-2
7. wegener2011deficiencyofprohormone pages 1-2
8. pauls2014peptidomicsandprocessing pages 5-6
9. rhea2010theproproteinconvertase pages 4-6
10. siekhaus1999arolefor pages 7-9
11. siekhaus1999arolefor pages 2-3
12. rhea2010theproproteinconvertase pages 8-9
13. rhea2010theproproteinconvertase pages 10-11
14. https://doi.org/10.1523/JNEUROSCI.19-16-06942.1999
15. https://doi.org/10.1093/genetics/163.1.227
16. https://doi.org/10.1371/journal.pgen.1000967
17. https://doi.org/10.1111/j.1471-4159.2010.07130.x
18. https://doi.org/10.1016/j.euprot.2014.02.007
19. https://doi.org/10.1016/j.euprot.2014.02.007,
20. https://doi.org/10.1111/j.1471-4159.2010.07130.x,
21. https://doi.org/10.1371/journal.pgen.1000967,
22. https://doi.org/10.1093/genetics/163.1.227,
23. https://doi.org/10.1523/jneurosci.19-16-06942.1999,