---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:58:33.138094'
end_time: '2026-09-08T18:04:16.627627'
duration_seconds: 343.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CG33453
  gene_symbol: Dmel\CG33453
  uniprot_accession: A0A0B4LFV5
  protein_description: 'SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AHN56405.1};'
  gene_info: Name=Dmel\CG33453 {ECO:0000313|EMBL:AHN56405.1}; ORFNames=CG33453 {ECO:0000313|EMBL:AHN56405.1,
    ECO:0000313|FlyBase:FBgn0053453}, Dmel_CG33453 {ECO:0000313|EMBL:AHN56405.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: DUF1091. (IPR010512); DUF1091 (PF06477)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 10
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CG33453-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** A0A0B4LFV5
- **Protein Description:** SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AHN56405.1};
- **Gene Information:** Name=Dmel\CG33453 {ECO:0000313|EMBL:AHN56405.1}; ORFNames=CG33453 {ECO:0000313|EMBL:AHN56405.1, ECO:0000313|FlyBase:FBgn0053453}, Dmel_CG33453 {ECO:0000313|EMBL:AHN56405.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF1091. (IPR010512); DUF1091 (PF06477)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG33453" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG33453' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG33453** (gene ID: CG33453, UniProt: A0A0B4LFV5) in DROME.

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
- **UniProt Accession:** A0A0B4LFV5
- **Protein Description:** SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AHN56405.1};
- **Gene Information:** Name=Dmel\CG33453 {ECO:0000313|EMBL:AHN56405.1}; ORFNames=CG33453 {ECO:0000313|EMBL:AHN56405.1, ECO:0000313|FlyBase:FBgn0053453}, Dmel_CG33453 {ECO:0000313|EMBL:AHN56405.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF1091. (IPR010512); DUF1091 (PF06477)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG33453" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG33453' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG33453** (gene ID: CG33453, UniProt: A0A0B4LFV5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional-annotation report: *Drosophila melanogaster* CG33453

## Executive conclusion

The requested target is **CG33453 (FlyBase FBgn0053453), UniProt A0A0B4LFV5, EMBL AHN56405.1**, annotated in the supplied UniProt record as an **uncharacterized *D. melanogaster* protein containing DUF1091** (InterPro IPR010512; Pfam PF06477). The literature search found **no publication directly establishing CG33453’s molecular function, biochemical substrate, cellular localization, interaction partners, pathway, or phenotype**, and no gene-specific 2023–2024 study was retrieved.

Accordingly, the defensible primary annotation remains **“uncharacterized DUF1091-containing protein.”** Family-level evidence makes a secreted/extracellular chemosensory-support or ligand-binding role plausible, but this is a hypothesis—not an experimentally demonstrated function of CG33453.

## 1. Mandatory identity verification

The supplied identifiers consistently specify *Drosophila melanogaster* CG33453/A0A0B4LFV5 rather than a homolog from another organism. However, the exact searches did not retrieve a paper independently connecting all of A0A0B4LFV5, AHN56405.1, CG33453, and FBgn0053453. Therefore, the identity is supported primarily by the supplied UniProt/EMBL/FlyBase cross-references rather than by a gene-specific experimental publication.

A critical ambiguity was resolved: the experimentally studied DUF1091 gene **daedalus (dls) is CG33690, not CG33453**. The 2020 study also identifies **decima (dcma) as CG34351**, making dls, dcma, and CG33453 three distinct genes (wilson2020gwasforlifespan pages 5-6, wilson2020gwasforlifespan pages 6-7). Thus, published diet-dependent climbing and activity phenotypes of dls and insulin-like-peptide findings for dcma must not be assigned to CG33453.

The gene symbol **“Dmel\\CG33453” is therefore not intrinsically ambiguous when accompanied by FBgn0053453 and A0A0B4LFV5**, but the surrounding DUF1091 literature creates a serious risk of mistaken identity.

## 2. Protein family and domain

CG33453 is reported in the supplied record to contain **DUF1091**, literally a “domain of unknown function.” Comparative-genomic analysis associates DUF1091 with the insect **CheA protein family**. Profile-HMM searches also recovered DUF1091/CheA proteins while searching for remote CheB homologues, leading the authors to suggest that CheA and CheB might be distantly related; the DUF1091 proteins nevertheless lacked the characteristic CheB DM11 domain and were excluded from the CheB analysis (torresoliva2016comparativegenomicsuncovers pages 3-4).

This establishes a possible evolutionary relationship, not biochemical equivalence. No catalytic motif, enzymatic reaction, transporter substrate, receptor activity, or specific ligand has been established for CG33453. It is consequently inappropriate to annotate the protein as an enzyme, transporter, or pheromone receptor on current evidence.

## 3. Most plausible molecular function

The most cautious working hypothesis is that CG33453 could be a **small secreted or extracellular protein participating in chemical-signal handling**, potentially by binding, presenting, transporting, or modulating access to a hydrophobic ligand. This inference rests on the broader CheA/DUF1091 family context, not on an assay of CG33453.

All eight *D. melanogaster* CheA proteins considered in a 2016 comparative study reportedly carried predicted amino-terminal signal peptides. At least two were preferentially expressed in chemosensory sensilla of male appendages, prompting a proposed role in male-specific pheromone responses (torresoliva2016comparativegenomicsuncovers pages 1-2). CheA proteins were also described as having relatively low sequence conservation and dispersed chromosomal locations, consistent with a divergent family whose individual members may not share identical ligands or tissue distributions (torresoliva2016comparativegenomicsuncovers pages 1-2).

CheB proteins provide only a remote functional analogy. They are small secreted/extracellular proteins produced by secretory cells surrounding gustatory neurons and have been proposed to assist recognition or processing of cuticular hydrocarbon pheromones (torresoliva2016comparativegenomicsuncovers pages 1-2, torresoliva2016comparativegenomicsuncovers pages 2-3). Because detectable primary-sequence homology between CheA and CheB is weak or absent, these CheB properties cannot be directly transferred to CG33453.

**Functional verdict:** no primary molecular function is established. A secreted ligand-interaction role in chemosensation is a testable family-level hypothesis of low confidence.

## 4. Localization

No CG33453-specific immunolocalization, tagged-protein imaging, fractionation, or secretion experiment was found. The family-wide prediction of signal peptides makes entry into the classical secretory pathway—and ultimately extracellular or lumenal localization—plausible (torresoliva2016comparativegenomicsuncovers pages 1-2). Whether CG33453 itself has a functional signal peptide should be verified directly from its sequence with current predictors and experimentally with secretion assays.

The evidence does **not** establish localization to neurons, synapses, nucleus, cytosol, membranes, or any particular chemosensory organ. Expression of at least two other CheA proteins in male chemosensory sensilla supports candidate tissues for investigation but does not localize CG33453 (torresoliva2016comparativegenomicsuncovers pages 1-2).

## 5. Biological processes and pathways

No signaling or biochemical pathway has been demonstrated for CG33453. The only defensible candidate process is **peripheral chemosensation, possibly pheromone/contact-cue detection**, inferred from selected CheA-family expression patterns (torresoliva2016comparativegenomicsuncovers pages 1-2).

A remote relationship to CheB is compatible with this hypothesis: CheB proteins are associated with gustatory organs, including male front legs and wings, and are implicated in responses to cuticular hydrocarbons and courtship pheromones (torresoliva2016comparativegenomicsuncovers pages 2-3). Nevertheless, CG33453 has not been shown to bind a hydrocarbon, influence sensory-neuron activation, alter courtship, or participate in odorant/pheromone degradation.

CG33453 should not be placed in dietary-restriction, locomotor-aging, or insulin-like-signaling pathways based on similarly discussed genes. Specifically, dls/CG33690 affects diet-dependent climbing and spontaneous activity, whereas dcma/CG34351 regulates neuronal insulin-like peptide expression; neither result concerns CG33453 (wilson2020gwasforlifespan pages 5-6, wilson2020gwasforlifespan pages 6-7, wilson2020gwasforlifespan pages 9-10).

## 6. Experimental evidence and relevant quantitative data

There is no retrieved target-specific knockout, RNAi, rescue, biochemical, proteomic, interaction, or localization result for CG33453. Consequently, no quantitative effect size can responsibly be reported for this gene.

The closest experimental DUF1091 example is dls/CG33690, but it must remain explicitly separate. Seven downstream polymorphisms were associated with diet-dependent climbing decline; a Minos insertion reduced dls transcript by approximately 90%, and climbing and spontaneous activity increased under dietary restriction. Lifespan effects changed with genetic background: median lifespan rose by 19% under dietary restriction and 8% under ad-libitum feeding in a *w*1118 background, but fell by 7% and 19%, respectively, after outcrossing to Canton-S (wilson2020gwasforlifespan pages 5-6). dls expression was reported to increase nine-fold in heads under dietary restriction (wilson2017genomewideanalysisreveals pages 6-7). These data demonstrate that at least one **different** DUF1091 gene can influence physiology, but they provide no phenotype or mechanism for CG33453.

## 7. Recent developments, applications, and expert assessment

Exact searches for CG33453, FBgn0053453, A0A0B4LFV5, and AHN56405.1 found no directly relevant 2023–2024 publication. Therefore, there is no supported recent development, real-world implementation, therapeutic application, or biotechnology use specific to CG33453.

The authoritative interpretation from the available comparative literature remains deliberately tentative: CheA proteins share predicted secretion and, for some members, chemosensory-sensillum expression, while DUF1091 profile similarity suggests a remote CheA–CheB relationship (torresoliva2016comparativegenomicsuncovers pages 1-2, torresoliva2016comparativegenomicsuncovers pages 3-4). This is sufficient to formulate experiments but not to assign a definitive Gene Ontology molecular function or pathway.

| Claim/category | Conclusion | Evidence level | Key limitation |
|---|---|---|---|
| Identity | Target is *Drosophila melanogaster* CG33453 (FlyBase FBgn0053453), represented by UniProt A0A0B4LFV5 and EMBL AHN56405.1. | Database-level annotation supplied for this review | No retrieved publication independently linked all identifiers or experimentally validated the protein product. |
| Domain | The target is annotated with DUF1091 (InterPro IPR010512; Pfam PF06477). DUF1091 is associated with the insect CheA family; profile searches suggest that CheA may be remotely related to CheB proteins. (torresoliva2016comparativegenomicsuncovers pages 3-4) | Moderate for domain assignment; low for functional inference | DUF means “domain of unknown function”; remote family similarity does not establish a shared ligand or mechanism. |
| Molecular function | No catalytic reaction, substrate specificity, transported substrate, receptor activity, or binding ligand has been established for CG33453. A ligand-binding or chemosensory-support role is only a family-level hypothesis. (torresoliva2016comparativegenomicsuncovers pages 1-2, torresoliva2016comparativegenomicsuncovers pages 3-4) | Unknown for CG33453; speculative inference | The comparative evidence concerns CheA/DUF1091 proteins collectively, not CG33453 specifically. |
| Localization | No CG33453-specific localization has been demonstrated. All eight surveyed *D. melanogaster* CheA proteins were reported to have predicted signal peptides, making secretion/extracellular localization plausible at family level. (torresoliva2016comparativegenomicsuncovers pages 1-2) | Low; computational and family-level | The retrieved source did not identify CG33453 individually or experimentally verify secretion. |
| Biological process/pathway | No pathway assignment is established. At least two CheA proteins are preferentially expressed in male chemosensory sensilla, supporting a possible family-level role in pheromone or contact-chemosensory responses. (torresoliva2016comparativegenomicsuncovers pages 1-2) | Low; indirect | Expression of other family members cannot establish that CG33453 participates in the same cells or pathway. |
| Experimental phenotype | No target-specific knockout, RNAi, rescue, biochemical, interaction, or behavioral phenotype was found. | No direct evidence | Absence from the retrieved literature is not proof that relevant unpublished or database-only screening data do not exist. |
| Recent 2023–2024 literature | Exact searches for CG33453, FBgn0053453, A0A0B4LFV5, and AHN56405.1 found no directly relevant 2023–2024 study. | Search result rather than biological evidence | Consequently, no recent gene-specific development, application, implementation, or quantitative statistic can be responsibly reported. |
| Major confounders | **daedalus/dls is CG33690, not CG33453**, and **decima/dcma is CG34351**; they are distinct genes. The diet-dependent climbing, activity, lifespan, expression, and insulin-like-peptide findings for these genes must not be assigned to CG33453. (wilson2020gwasforlifespan pages 5-6, wilson2020gwasforlifespan pages 6-7) | High; explicit identifiers in primary literature | daedalus also contains DUF1091, making erroneous transfer of its phenotypes to CG33453 especially likely. (wilsonaUnknownyeargenomewideanalysisreveals pages 9-11) |


*Table: This table separates verified identity and domain annotations from indirect DUF1091/CheA-family hypotheses and documents the absence of direct functional evidence. It also highlights the critical risk of confusing CG33453 with the distinct genes daedalus/CG33690 or decima/CG34351.*

## 8. Recommended experiments for resolving function

1. **Confirm the protein model:** validate CG33453 transcripts by long-read RNA sequencing or RACE and confirm A0A0B4LFV5 expression by targeted mass spectrometry.
2. **Test secretion:** express epitope-tagged CG33453 in *Drosophila* cells, assay culture medium versus lysate, and mutate the predicted signal peptide if present.
3. **Map expression:** use endogenous knock-in reporters and tissue-resolved RNA methods, emphasizing antennae, maxillary palps, proboscis, legs, wings, and associated support cells.
4. **Establish phenotype:** generate a clean CRISPR null allele and genomic rescue. Test olfactory and gustatory responses, courtship, contact-pheromone discrimination, locomotion, fertility, and viability.
5. **Identify ligands:** purify the mature secreted protein and screen cuticular hydrocarbons, fatty acids, odorants, and microbial molecules using thermal-shift, native mass-spectrometry, or fluorescence-binding assays.
6. **Identify partners:** conduct affinity purification–mass spectrometry or proximity labeling in the endogenous expression domain.
7. **Use evolutionary evidence carefully:** compare ortholog conservation, signal peptides, cysteines, and structure across drosophilids, but require biochemical or genetic validation before assigning ligand specificity.

## Final annotation

**CG33453/A0A0B4LFV5 is an uncharacterized *D. melanogaster* DUF1091 protein.** Its precise molecular activity, ligand or substrate, cellular site of action, biological pathway, and phenotype remain unknown. The best current hypothesis is a secreted/extracellular CheA-family protein with a possible role in peripheral chemosensory or pheromone-signal handling, but this remains indirect. The gene-specific literature is limited, and evidence from **daedalus/CG33690** or **decima/CG34351** must not be transferred to this target.

References

1. (wilson2020gwasforlifespan pages 5-6): Kenneth A. Wilson, Jennifer N. Beck, Christopher S. Nelson, Tyler A. Hilsabeck, Daniel Promislow, Rachel B. Brem, and Pankaj Kapahi. Gwas for lifespan and decline in climbing ability in flies upon dietary restriction reveal decima as a mediator of insulin-like peptide production. Jul 2020. URL: https://doi.org/10.1016/j.cub.2020.05.020, doi:10.1016/j.cub.2020.05.020. This article has 69 citations and is from a highest quality peer-reviewed journal.

2. (wilson2020gwasforlifespan pages 6-7): Kenneth A. Wilson, Jennifer N. Beck, Christopher S. Nelson, Tyler A. Hilsabeck, Daniel Promislow, Rachel B. Brem, and Pankaj Kapahi. Gwas for lifespan and decline in climbing ability in flies upon dietary restriction reveal decima as a mediator of insulin-like peptide production. Jul 2020. URL: https://doi.org/10.1016/j.cub.2020.05.020, doi:10.1016/j.cub.2020.05.020. This article has 69 citations and is from a highest quality peer-reviewed journal.

3. (torresoliva2016comparativegenomicsuncovers pages 3-4): Montserrat Torres-Oliva, Francisca C. Almeida, Alejandro Sánchez-Gracia, and Julio Rozas. Comparative genomics uncovers unique gene turnover and evolutionary rates in a gene family involved in the detection of insect cuticular pheromones. Genome Biology and Evolution, 8:1734-1747, Jun 2016. URL: https://doi.org/10.1093/gbe/evw108, doi:10.1093/gbe/evw108. This article has 15 citations and is from a domain leading peer-reviewed journal.

4. (torresoliva2016comparativegenomicsuncovers pages 1-2): Montserrat Torres-Oliva, Francisca C. Almeida, Alejandro Sánchez-Gracia, and Julio Rozas. Comparative genomics uncovers unique gene turnover and evolutionary rates in a gene family involved in the detection of insect cuticular pheromones. Genome Biology and Evolution, 8:1734-1747, Jun 2016. URL: https://doi.org/10.1093/gbe/evw108, doi:10.1093/gbe/evw108. This article has 15 citations and is from a domain leading peer-reviewed journal.

5. (torresoliva2016comparativegenomicsuncovers pages 2-3): Montserrat Torres-Oliva, Francisca C. Almeida, Alejandro Sánchez-Gracia, and Julio Rozas. Comparative genomics uncovers unique gene turnover and evolutionary rates in a gene family involved in the detection of insect cuticular pheromones. Genome Biology and Evolution, 8:1734-1747, Jun 2016. URL: https://doi.org/10.1093/gbe/evw108, doi:10.1093/gbe/evw108. This article has 15 citations and is from a domain leading peer-reviewed journal.

6. (wilson2020gwasforlifespan pages 9-10): Kenneth A. Wilson, Jennifer N. Beck, Christopher S. Nelson, Tyler A. Hilsabeck, Daniel Promislow, Rachel B. Brem, and Pankaj Kapahi. Gwas for lifespan and decline in climbing ability in flies upon dietary restriction reveal decima as a mediator of insulin-like peptide production. Jul 2020. URL: https://doi.org/10.1016/j.cub.2020.05.020, doi:10.1016/j.cub.2020.05.020. This article has 69 citations and is from a highest quality peer-reviewed journal.

7. (wilson2017genomewideanalysisreveals pages 6-7): Kenneth A. Wilson, Christopher S. Nelson, Jennifer N. Beck, Rachel B. Brem, and Pankaj Kapahi. Genome-wide analysis reveals distinct genetic mechanisms of diet-dependent lifespan and healthspan in d. melanogaster. bioRxiv, Jun 2017. URL: https://doi.org/10.1101/153791, doi:10.1101/153791. This article has 8 citations.

8. (wilsonaUnknownyeargenomewideanalysisreveals pages 9-11): KA Wilsona, CS Nelsona, and JN Becka. Genome-wide analysis reveals distinct genetic mechanisms of diet-dependent lifespan 1 and healthspan in d. melanogaster 2. Unknown journal, Unknown year.

## Artifacts

- [Edison artifact artifact-00](CG33453-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. torresoliva2016comparativegenomicsuncovers pages 3-4
2. torresoliva2016comparativegenomicsuncovers pages 1-2
3. torresoliva2016comparativegenomicsuncovers pages 2-3
4. wilson2020gwasforlifespan pages 5-6
5. wilson2017genomewideanalysisreveals pages 6-7
6. wilson2020gwasforlifespan pages 6-7
7. wilson2020gwasforlifespan pages 9-10
8. https://doi.org/10.1016/j.cub.2020.05.020,
9. https://doi.org/10.1093/gbe/evw108,
10. https://doi.org/10.1101/153791,