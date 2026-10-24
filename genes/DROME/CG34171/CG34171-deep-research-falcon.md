---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T16:53:30.930316'
end_time: '2026-09-08T16:59:19.579161'
duration_seconds: 348.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CG34171
  gene_symbol: Dmel\CG34171
  uniprot_accession: X2JEK1
  protein_description: 'RecName: Full=Peptidase S1 domain-containing protein {ECO:0000259|PROSITE:PS50240};'
  gene_info: Name=Dmel\CG34171 {ECO:0000313|EMBL:AHN54555.1}; Synonyms=SPH244 {ECO:0000313|EMBL:AHN54555.1};
    ORFNames=CG34171 {ECO:0000313|EMBL:AHN54555.1, ECO:0000313|FlyBase:FBgn0085200},
    Dmel_CG34171 {ECO:0000313|EMBL:AHN54555.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the peptidase S1 family. CLIP subfamily.
  protein_domains: Peptidase_S1_PA. (IPR009003); Ser/Thr_Proteases_Immune/Dev. (IPR051487);
    Trypsin_dom. (IPR001254); Trypsin (PF00089)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CG34171-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** X2JEK1
- **Protein Description:** RecName: Full=Peptidase S1 domain-containing protein {ECO:0000259|PROSITE:PS50240};
- **Gene Information:** Name=Dmel\CG34171 {ECO:0000313|EMBL:AHN54555.1}; Synonyms=SPH244 {ECO:0000313|EMBL:AHN54555.1}; ORFNames=CG34171 {ECO:0000313|EMBL:AHN54555.1, ECO:0000313|FlyBase:FBgn0085200}, Dmel_CG34171 {ECO:0000313|EMBL:AHN54555.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase S1 family. CLIP subfamily.
- **Key Domains:** Peptidase_S1_PA. (IPR009003); Ser/Thr_Proteases_Immune/Dev. (IPR051487); Trypsin_dom. (IPR001254); Trypsin (PF00089)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG34171" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG34171' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG34171** (gene ID: CG34171, UniProt: X2JEK1) in DROME.

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
- **UniProt Accession:** X2JEK1
- **Protein Description:** RecName: Full=Peptidase S1 domain-containing protein {ECO:0000259|PROSITE:PS50240};
- **Gene Information:** Name=Dmel\CG34171 {ECO:0000313|EMBL:AHN54555.1}; Synonyms=SPH244 {ECO:0000313|EMBL:AHN54555.1}; ORFNames=CG34171 {ECO:0000313|EMBL:AHN54555.1, ECO:0000313|FlyBase:FBgn0085200}, Dmel_CG34171 {ECO:0000313|EMBL:AHN54555.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase S1 family. CLIP subfamily.
- **Key Domains:** Peptidase_S1_PA. (IPR009003); Ser/Thr_Proteases_Immune/Dev. (IPR051487); Trypsin_dom. (IPR001254); Trypsin (PF00089)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG34171" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG34171' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG34171** (gene ID: CG34171, UniProt: X2JEK1) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: *Drosophila melanogaster* CG34171 / SPH244 (UniProt X2JEK1)

## Executive conclusion

The gene symbol **Dmel\\CG34171 is consistent with the supplied UniProt entry X2JEK1**, organism *Drosophila melanogaster*, aliases **CG34171/SPH244**, and FlyBase identifier **FBgn0085200**. Its defensible annotation is an **uncharacterized CLIP-family protein containing a peptidase-S1/trypsin-like domain**. However, exact-identifier searches found **no primary publication that experimentally establishes CG34171’s catalytic activity, substrate, localization, pathway, expression pattern, or phenotype**. The gene symbol is therefore not ambiguous within the supplied identifier set, but the literature is extremely limited for this specific protein.

Crucially, the similarly named protein **cSPH242**, characterized in 2023, is encoded by **CG40160**, not CG34171/SPH244. Its experimentally demonstrated role in prophenoloxidase-1 activation must not be assigned to CG34171. (jin2023twoclipdomainserine pages 2-3)

| Question | Best-supported conclusion | Evidence tier | Confidence |
|---|---|---|---|
| Identity | **CG34171**, also annotated as **Dmel\\CG34171**, **SPH244**, and **FBgn0085200**, corresponds to **UniProt X2JEK1**. No publication retrieved by exact-identifier searches independently validated these aliases. | Supplied UniProt computational annotation | Moderate |
| Organism | The annotated organism is **Drosophila melanogaster** (fruit fly; DROME). | Supplied UniProt computational annotation | High |
| Protein family and domains | X2JEK1 is annotated as a **peptidase S1 domain-containing protein** in the **peptidase S1, CLIP subfamily**, with Peptidase_S1_PA/trypsin-like domains. CLIP proteins generally contain N-terminal CLIP domain(s) and a C-terminal S1A serine-protease or protease-like domain (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 12-17). | Supplied UniProt computational annotation, supported only at family level | Moderate |
| Catalytic activity | **No catalytic activity has been demonstrated for CG34171.** An S1/trypsin-like domain alone does not establish an active enzyme: CLIP proteins may retain the His–Asp–Ser catalytic triad or be noncatalytic serine-protease homologs (kanost2015clipdomainserineproteases pages 12-17, kanost2015clipdomainserineproteases pages 2-4). | Family-level inference; no direct CG34171 experiment | Low |
| Reaction and substrate specificity | **Unknown.** No cleavage reaction, physiological substrate, kinetic constant, or specificity profile has been reported for CG34171. Family members can process prophenoloxidase, pro-Spätzle, or upstream protease zymogens, but these substrates cannot be assigned to CG34171 (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 2-4). | Family-level inference; no direct CG34171 experiment | Very low |
| Localization | **Unknown for CG34171.** Many immune CLIP proteins function as secreted zymogens in insect hemolymph, but secretion or hemolymph localization has not been demonstrated for this protein (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 10-12). | Family-level inference; no direct CG34171 experiment | Low |
| Biological pathway | **No pathway assignment is established.** Plausible family-level hypotheses include extracellular protease cascades controlling melanization/prophenoloxidase activation or Toll signaling through pro-Spätzle processing; developmental CLIP cascades also exist in Drosophila (kanost2015clipdomainserineproteases pages 1-2, ponting2001novelproteindomains pages 6-8). | Family-level inference; no direct CG34171 experiment | Very low |
| Phenotype and biological process | **No CG34171-specific loss-of-function, gain-of-function, RNAi, infection, developmental, or biochemical phenotype was found.** Phenotypes of other CLIP proteins must not be transferred to CG34171. | No direct CG34171 experiment | High confidence that evidence is currently absent from the retrieved literature |
| Key 2023 disambiguation | The similarly named **cSPH242** studied in 2023 is **CG40160**, whereas **CG34171 is annotated as SPH244**. Therefore, cSPH242’s PPO1-cofactor function and quantitative RNAi phenotypes do **not** constitute evidence about CG34171 (jin2023twoclipdomainserine pages 2-3). | Direct nomenclature evidence for cSPH242 plus supplied UniProt annotation for CG34171 | High |
| Overall functional annotation | The defensible annotation is **an uncharacterized D. melanogaster CLIP-family S1 protease-domain protein**. Whether it is an active protease or a regulatory pseudoprotease—and its substrate, compartment, and pathway—requires direct experimental testing. | Integrated annotation and family-level inference | Moderate for classification; very low for precise function |


*Table: This table separates database-derived identity and domain annotations from direct experimental evidence and broader CLIP-family inference. It highlights that cSPH242/CG40160 findings cannot be assigned to CG34171/SPH244.*

## 1. Identity verification

The supplied identifiers form a coherent target record: X2JEK1; CG34171/Dmel\\CG34171; SPH244; FBgn0085200; *D. melanogaster*; and a peptidase-S1-domain, CLIP-subfamily annotation. Literature searches using each exact identifier did not retrieve an independently characterized protein. Accordingly, this report retains the supplied UniProt identity but treats its functional description as **computational annotation rather than experimentally reviewed function**.

The most important false-match risk is cSPH242. Jin and colleagues explicitly map **cSPH35 to CG5390** and **cSPH242 to CG40160**. Neither is CG34171, and “242” must not be conflated with the SPH244 alias in the target record. (jin2023twoclipdomainserine pages 2-3)

## 2. Key concepts and domain-based interpretation

CLIP-domain proteins generally possess one or more small, cysteine-rich N-terminal clip domains, a linker, and a C-terminal S1A/chymotrypsin-fold serine-protease or protease-like domain. Clip domains are approximately 35–55 residues and usually contain three disulfide bonds; they are thought to mediate regulated protein interactions within extracellular proteolytic cascades. (kanost2015clipdomainserineproteases pages 1-2, ponting2001novelproteindomains pages 6-8, kanost2015clipdomainserineproteases pages 2-4)

The S1A fold normally positions **His, Asp, and Ser** as a catalytic triad. Nevertheless, domain detection alone cannot establish enzymatic activity: some CLIP proteins are active proteases, whereas serine-protease homologs are pseudoproteases in which an essential catalytic residue—often Ser—is substituted. CLIPA proteins commonly have Ser replaced by Gly and function as regulatory proteins or cofactors rather than enzymes. (kanost2015clipdomainserineproteases pages 12-17, kanost2015clipdomainserineproteases pages 2-4)

For **CG34171 specifically**, the supplied annotation confirms Peptidase_S1_PA/trypsin-family sequence similarity but does not report whether the catalytic His–Asp–Ser triad is intact. The alias “SPH244” may suggest a serine-protease homolog, but nomenclature is not biochemical proof. The protein should therefore be described as an **S1 protease-domain protein of unknown catalytic status**, not as a confirmed active serine protease.

## 3. Primary molecular function, reaction, and substrate specificity

No biochemical reaction has been demonstrated for CG34171. If it is catalytically active, the broad family expectation would be hydrolysis of a peptide bond in a protein zymogen or signaling substrate. However, there is no evidence identifying its cleavage-site preference, physiological substrate, catalytic rate, inhibitor sensitivity, or activation mechanism.

Known CLIP-family substrates include prophenoloxidases, pro-Spätzle, and upstream protease zymogens. Terminal CLIPB proteases can activate prophenoloxidase or pro-Spätzle, while CLIPC enzymes often act upstream of CLIPB proteins. These relationships define plausible experimental hypotheses but **do not establish CG34171 as a component of either pathway**. (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 7-8, kanost2015clipdomainserineproteases pages 2-4)

If CG34171 is instead a pseudoprotease, its likely molecular role would be noncatalytic—such as complex assembly, substrate presentation, spatial organization, or regulation of another protease. That possibility remains equally untested.

## 4. Localization

There is no CG34171-specific evidence for a cellular or extracellular location. Immune CLIP proteases are commonly secreted as inactive zymogens into insect hemolymph and activated by restricted proteolysis; after activation, the clip and catalytic domains can remain linked by an interchain disulfide bond. (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 10-12, kanost2015clipdomainserineproteases pages 12-17)

Thus, an extracellular or hemolymph-associated role is biologically plausible, but it should not be asserted without verifying an N-terminal signal peptide and obtaining localization evidence. No retrieved study demonstrated secretion, hemolymph detection, tissue enrichment, membrane association, or subcellular localization for CG34171.

## 5. Candidate biological pathways

Two major family-level hypotheses merit testing:

1. **Melanization/prophenoloxidase activation.** Extracellular CLIP cascades cleave prophenoloxidase to phenoloxidase, generating reactive intermediates and melanin around wounds or pathogens. In *Drosophila*, MP2/Sp7 is a characterized prophenoloxidase-activating CLIP protease. (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 7-8)
2. **Toll signaling.** Other extracellular serine-protease cascades generate active Spätzle, the Toll ligand that induces antimicrobial-peptide expression. Characterized components include Grass, Persephone, Spirit, and the Spätzle-processing enzyme. (kanost2015clipdomainserineproteases pages 10-12, mwangi2011evolutionarygenomicsof pages 1-2, kanost2015clipdomainserineproteases pages 12-17)

CLIP proteases also have developmental precedents: Snake and Easter participate in the extracellular cascade establishing embryonic dorsal–ventral polarity. Therefore, immune function cannot be inferred solely from family membership. (ponting2001novelproteindomains pages 6-8)

At present, **CG34171 has no established placement in melanization, Toll signaling, development, coagulation, or another biochemical pathway**.

## 6. Recent research and quantitative context

No 2023–2024 study directly concerning CG34171 was found. The most relevant recent *Drosophila* work is the September 2023 study of cSPH35/CG5390 and cSPH242/CG40160. These proteins are noncatalytic homologs in which Gly replaces catalytic Ser. Proteolytic processing promotes high-molecular-weight complex formation, and the complexes serve as cofactors for MP2/Sp7-mediated PPO1 activation. Again, neither protein is CG34171. (jin2023twoclipdomainserine pages 1-2, jin2023twoclipdomainserine pages 6-7, jin2023twoclipdomainserine pages 2-3)

That study provides useful evidence of what a CLIP pseudoprotease can do mechanistically. Processed cSPH complexes produced **38.9 U phenoloxidase activity, equivalent to 260 U/mg**, compared with 10.5 U using untreated precursors. Removing cSPH242 or cSPH35 reduced activity from 33.1 U to 14.7 or 4.7 U, respectively. RNAi lowered their transcripts to approximately 60% and 40% of control. (jin2023twoclipdomainserine pages 6-7)

In vivo hemolymph phenoloxidase activity was **26.0 U/ml in controls**, 4.7 U/ml after cSPH242 knockdown, and 1.2 U/ml after cSPH35 knockdown. Septic-prick melanization occurred in 82% of wild-type adults, versus 53% and 30% in the respective knockdowns; ten-day survival was 45% in controls, 15% after cSPH242 RNAi, and 30% after cSPH35 RNAi. (jin2023twoclipdomainserine pages 7-8)

These results demonstrate that noncatalytic CLIP homologs can be indispensable cofactors rather than enzymes. They provide a strong experimental template for studying CG34171, but **none of these numerical findings describes CG34171/SPH244**.

## 7. Current applications and real-world relevance

There is no reported real-world implementation specific to CG34171—no diagnostic, therapeutic, biotechnology reagent, or pest-control application was found. Its present value is primarily as a candidate for functional genomics of extracellular protease networks.

At the family level, CLIP cascades are relevant to insect immunity, host–pathogen interactions, melanization, and development. Mechanistic knowledge can inform comparative immunology and, eventually, species-selective pest or vector-control strategies. However, the large, duplicated, and partly redundant CLIP repertoire makes orthology-based functional transfer unreliable. Authoritative reviews emphasize that the functions of most insect CLIP proteins remain unknown. (kanost2015clipdomainserineproteases pages 10-12)

## 8. Expert assessment and recommended annotation

A suitably conservative annotation is:

> **CG34171/SPH244 encodes an uncharacterized *Drosophila melanogaster* CLIP-family peptidase-S1/trypsin-like-domain protein. Its catalytic status, substrate, extracellular localization, biological pathway, and organismal function have not been experimentally established.**

It would be premature to annotate the protein as a prophenoloxidase-activating enzyme, Spätzle-processing enzyme, immune cofactor, or developmental protease. Those are testable possibilities derived from family biology, not target-specific conclusions.

## 9. Highest-priority experiments

1. **Sequence validation:** confirm the complete coding sequence, signal peptide, clip-domain boundaries, zymogen activation site, disulfide pattern, and catalytic His–Asp–Ser residues.
2. **Catalytic classification:** express the protein and test active-site labeling and hydrolysis of peptide libraries; mutate the putative catalytic Ser if present.
3. **Substrate discovery:** combine N-terminomics/degradomics with candidate assays for PPO1–3, pro-Spätzle, and upstream CLIP zymogens.
4. **Localization:** use an endogenous epitope knock-in plus hemolymph proteomics and tissue-resolved imaging.
5. **Genetics:** generate a clean null allele and rescue line; assay development, wound melanization, phenoloxidase activity, Toll-responsive antimicrobial peptides, and survival after defined bacterial or fungal challenges.
6. **Interaction mapping:** test complex formation with known CLIP proteases, pseudoproteases, serpins, PPOs, and Spätzle-pathway components.

## References

- Jin Q, Wang Y, Yin H, Jiang H. “Two clip-domain serine protease homologs, cSPH35 and cSPH242, act as a cofactor for prophenoloxidase-1 activation in *Drosophila melanogaster*.” *Frontiers in Immunology*. Published September 2023. https://doi.org/10.3389/fimmu.2023.1244792 (jin2023twoclipdomainserine pages 1-2, jin2023twoclipdomainserine pages 2-3)
- Kanost MR, Jiang H. “Clip-domain serine proteases as immune factors in insect hemolymph.” *Current Opinion in Insect Science*. Published October 2015. https://doi.org/10.1016/j.cois.2015.09.003 (kanost2015clipdomainserineproteases pages 1-2, kanost2015clipdomainserineproteases pages 12-17)
- Ponting CP, Mott R, Bork P, Copley RR. “Novel protein domains and repeats in *Drosophila melanogaster*: insights into structure, function, and evolution.” *Genome Research*. Published December 2001. https://doi.org/10.1101/gr.198701 (ponting2001novelproteindomains pages 6-8)
- Mwangi S, Murungi E, Jonas M, Christoffels A. “Evolutionary genomics of *Glossina morsitans* immune-related CLIP domain serine proteases and serine protease inhibitors.” *Infection, Genetics and Evolution*. Published June 2011. https://doi.org/10.1016/j.meegid.2010.10.006 (mwangi2011evolutionarygenomicsof pages 1-2)

References

1. (jin2023twoclipdomainserine pages 2-3): Qiao Jin, Yang Wang, Haodong Yin, and Haobo Jiang. Two clip-domain serine protease homologs, csph35 and csph242, act as a cofactor for prophenoloxidase-1 activation in drosophila melanogaster. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1244792, doi:10.3389/fimmu.2023.1244792. This article has 14 citations and is from a peer-reviewed journal.

2. (kanost2015clipdomainserineproteases pages 1-2): Michael R Kanost and Haobo Jiang. Clip-domain serine proteases as immune factors in insect hemolymph. Current opinion in insect science, 11:47-55, Oct 2015. URL: https://doi.org/10.1016/j.cois.2015.09.003, doi:10.1016/j.cois.2015.09.003. This article has 304 citations and is from a peer-reviewed journal.

3. (kanost2015clipdomainserineproteases pages 12-17): Michael R Kanost and Haobo Jiang. Clip-domain serine proteases as immune factors in insect hemolymph. Current opinion in insect science, 11:47-55, Oct 2015. URL: https://doi.org/10.1016/j.cois.2015.09.003, doi:10.1016/j.cois.2015.09.003. This article has 304 citations and is from a peer-reviewed journal.

4. (kanost2015clipdomainserineproteases pages 2-4): Michael R Kanost and Haobo Jiang. Clip-domain serine proteases as immune factors in insect hemolymph. Current opinion in insect science, 11:47-55, Oct 2015. URL: https://doi.org/10.1016/j.cois.2015.09.003, doi:10.1016/j.cois.2015.09.003. This article has 304 citations and is from a peer-reviewed journal.

5. (kanost2015clipdomainserineproteases pages 10-12): Michael R Kanost and Haobo Jiang. Clip-domain serine proteases as immune factors in insect hemolymph. Current opinion in insect science, 11:47-55, Oct 2015. URL: https://doi.org/10.1016/j.cois.2015.09.003, doi:10.1016/j.cois.2015.09.003. This article has 304 citations and is from a peer-reviewed journal.

6. (ponting2001novelproteindomains pages 6-8): Chris P. Ponting, Richard Mott, Peer Bork, and Richard R. Copley. Novel protein domains and repeats in drosophila melanogaster: insights into structure, function, and evolution. Genome research, 11 12:1996-2008, Dec 2001. URL: https://doi.org/10.1101/gr.198701, doi:10.1101/gr.198701. This article has 162 citations and is from a highest quality peer-reviewed journal.

7. (kanost2015clipdomainserineproteases pages 7-8): Michael R Kanost and Haobo Jiang. Clip-domain serine proteases as immune factors in insect hemolymph. Current opinion in insect science, 11:47-55, Oct 2015. URL: https://doi.org/10.1016/j.cois.2015.09.003, doi:10.1016/j.cois.2015.09.003. This article has 304 citations and is from a peer-reviewed journal.

8. (mwangi2011evolutionarygenomicsof pages 1-2): Sarah Mwangi, Edwin Murungi, Mario Jonas, and Alan Christoffels. Evolutionary genomics of glossina morsitans immune-related clip domain serine proteases and serine protease inhibitors. Infection, genetics and evolution : journal of molecular epidemiology and evolutionary genetics in infectious diseases, 11 4:740-5, Jun 2011. URL: https://doi.org/10.1016/j.meegid.2010.10.006, doi:10.1016/j.meegid.2010.10.006. This article has 14 citations.

9. (jin2023twoclipdomainserine pages 1-2): Qiao Jin, Yang Wang, Haodong Yin, and Haobo Jiang. Two clip-domain serine protease homologs, csph35 and csph242, act as a cofactor for prophenoloxidase-1 activation in drosophila melanogaster. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1244792, doi:10.3389/fimmu.2023.1244792. This article has 14 citations and is from a peer-reviewed journal.

10. (jin2023twoclipdomainserine pages 6-7): Qiao Jin, Yang Wang, Haodong Yin, and Haobo Jiang. Two clip-domain serine protease homologs, csph35 and csph242, act as a cofactor for prophenoloxidase-1 activation in drosophila melanogaster. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1244792, doi:10.3389/fimmu.2023.1244792. This article has 14 citations and is from a peer-reviewed journal.

11. (jin2023twoclipdomainserine pages 7-8): Qiao Jin, Yang Wang, Haodong Yin, and Haobo Jiang. Two clip-domain serine protease homologs, csph35 and csph242, act as a cofactor for prophenoloxidase-1 activation in drosophila melanogaster. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1244792, doi:10.3389/fimmu.2023.1244792. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CG34171-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. jin2023twoclipdomainserine pages 2-3
2. ponting2001novelproteindomains pages 6-8
3. jin2023twoclipdomainserine pages 6-7
4. jin2023twoclipdomainserine pages 7-8
5. kanost2015clipdomainserineproteases pages 10-12
6. mwangi2011evolutionarygenomicsof pages 1-2
7. kanost2015clipdomainserineproteases pages 1-2
8. kanost2015clipdomainserineproteases pages 12-17
9. kanost2015clipdomainserineproteases pages 2-4
10. kanost2015clipdomainserineproteases pages 7-8
11. jin2023twoclipdomainserine pages 1-2
12. https://doi.org/10.3389/fimmu.2023.1244792
13. https://doi.org/10.1016/j.cois.2015.09.003
14. https://doi.org/10.1101/gr.198701
15. https://doi.org/10.1016/j.meegid.2010.10.006
16. https://doi.org/10.3389/fimmu.2023.1244792,
17. https://doi.org/10.1016/j.cois.2015.09.003,
18. https://doi.org/10.1101/gr.198701,
19. https://doi.org/10.1016/j.meegid.2010.10.006,