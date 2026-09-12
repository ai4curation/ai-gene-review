---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:40:58.304130'
end_time: '2026-09-10T14:48:18.555534'
duration_seconds: 440.25
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CG34117
  gene_symbol: Dmel\CG34117
  uniprot_accession: Q0KI97
  protein_description: 'RecName: Full=Protein FMC1 homolog {ECO:0000256|ARBA:ARBA00013846};'
  gene_info: Name=Dmel\CG34117 {ECO:0000313|EMBL:ABI31150.1}; ORFNames=CG34117 {ECO:0000313|EMBL:ABI31150.1,
    ECO:0000313|FlyBase:FBgn0083953}, Dmel_CG34117 {ECO:0000313|EMBL:ABI31150.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the FMC1 family.
  protein_domains: FMC1_homologue. (IPR037667); Complex1_LYR_2 (PF13233)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CG34117-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q0KI97
- **Protein Description:** RecName: Full=Protein FMC1 homolog {ECO:0000256|ARBA:ARBA00013846};
- **Gene Information:** Name=Dmel\CG34117 {ECO:0000313|EMBL:ABI31150.1}; ORFNames=CG34117 {ECO:0000313|EMBL:ABI31150.1, ECO:0000313|FlyBase:FBgn0083953}, Dmel_CG34117 {ECO:0000313|EMBL:ABI31150.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the FMC1 family.
- **Key Domains:** FMC1_homologue. (IPR037667); Complex1_LYR_2 (PF13233)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG34117" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG34117' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG34117** (gene ID: CG34117, UniProt: Q0KI97) in DROME.

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
- **UniProt Accession:** Q0KI97
- **Protein Description:** RecName: Full=Protein FMC1 homolog {ECO:0000256|ARBA:ARBA00013846};
- **Gene Information:** Name=Dmel\CG34117 {ECO:0000313|EMBL:ABI31150.1}; ORFNames=CG34117 {ECO:0000313|EMBL:ABI31150.1, ECO:0000313|FlyBase:FBgn0083953}, Dmel_CG34117 {ECO:0000313|EMBL:ABI31150.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the FMC1 family.
- **Key Domains:** FMC1_homologue. (IPR037667); Complex1_LYR_2 (PF13233)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dmel\CG34117" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dmel\CG34117' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dmel\CG34117** (gene ID: CG34117, UniProt: Q0KI97) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* CG34117 / Q0KI97

## Executive conclusion

The gene symbol **Dmel\\CG34117** is consistent with the requested *Drosophila melanogaster* locus **CG34117** (FlyBase **FBgn0083953**) and UniProt accession **Q0KI97**. The supplied protein-family assignments—**FMC1 family**, InterPro **FMC1_homologue (IPR037667)**, and Pfam **Complex1_LYR_2 (PF13233)**—are mutually compatible with annotation as a small mitochondrial LYRM-related protein. Searches using the exact accession and gene symbol identified **no peer-reviewed study directly characterizing CG34117/Q0KI97**, including no gene-specific 2023–2024 report. Consequently, the gene symbol is not being conflated here with human FMC1/C7orf55 or yeast Fmc1p; those proteins are used only as comparative evidence.

The best-supported functional hypothesis is that CG34117 encodes a **non-catalytic mitochondrial assembly or stability factor for F₁F₀-ATP synthase (oxidative-phosphorylation complex V)**. More specifically, it probably assists biogenesis of the matrix-facing F₁ catalytic sector, potentially by supporting an ATP12/ATPAF2-like chaperone. This is a **moderate-confidence homology-based annotation**, not a demonstrated function in flies. No reaction, substrate, product, transporter cargo, or substrate specificity is known or expected for CG34117.

| Annotation question | Best-supported conclusion | Evidence type/species | Confidence | Key caveat |
|---|---|---|---|---|
| Identity | Q0KI97 corresponds to *Drosophila melanogaster* CG34117/FBgn0083953 and is database-annotated as an FMC1-family protein containing FMC1_homologue and Complex1_LYR_2 features. | Fly identifier and computational domain annotation; comparative LYRM-family literature (tang2020mitochondrialoxphosbiogenesis pages 16-18) | High for identity; moderate for functional family assignment | No CG34117-specific publication independently validates the functional annotation. |
| Molecular function | Most plausibly a small mitochondrial accessory factor that promotes assembly or stability of F₁F₀-ATP synthase, also called OXPHOS complex V. | Homology-based inference from yeast FMC1 and broader eukaryotic LYRM biology (tang2020mitochondrialoxphosbiogenesis pages 18-20, potocka2007assemblyfactorsin pages 41-45) | Moderate | This function has not been demonstrated by fly knockout, rescue, interaction, or complex-assembly assays. |
| Enzyme status and substrate | Not an established enzyme; no catalytic reaction, substrate, product, or substrate specificity is known. Its expected role is protein-complex biogenesis rather than catalysis. | FMC1 and LYRM family-level mechanistic interpretation (tang2020mitochondrialoxphosbiogenesis pages 18-20, tang2020mitochondrialoxphosbiogenesis pages 16-18) | Moderate to high | Absence of an identified reaction does not prove that the fly protein lacks every biochemical activity. |
| Localization | Predicted to act in mitochondria, probably in the matrix or matrix-facing inner-membrane environment where the F₁ sector is assembled. | Cross-species LYRM and mitochondrial ACP evidence (dibley2020themitochondrialacylcarrier pages 2-3) | Moderate for mitochondria; low for the exact subcompartment | No CG34117-specific microscopy, fractionation, import, or protease-protection experiment was identified. |
| Pathway | Likely participates in mitochondrial oxidative phosphorylation through complex V biogenesis, thereby indirectly supporting proton-gradient-driven ATP production. | Yeast FMC1 and general OXPHOS-assembly literature (tang2020mitochondrialoxphosbiogenesis pages 18-20, tang2020mitochondrialoxphosbiogenesis pages 30-32) | Moderate | CG34117 has not been shown to be a stable ATP-synthase subunit or to affect ATP production in flies. |
| Atp12 and ATPAF2 relationship | Yeast Fmc1 stabilizes or functionally supports Atp12, the homolog of mammalian ATPAF2, during F₁-sector assembly; an analogous relationship in flies is plausible. | Functional evidence from yeast transferred by family homology (tang2020mitochondrialoxphosbiogenesis pages 18-20, potocka2007assemblyfactorsin pages 41-45) | Moderate for yeast; low for fly | Atp12 overexpression rescue supports functional linkage but does not by itself establish direct binding; no fly interaction has been demonstrated. |
| Mitochondrial ACP relationship | FMC1 can interact with mitochondrial acyl-carrier protein in yeast and humans, consistent with ACP–LYRM biology; this association may not be essential for FMC1-mediated complex V assembly. | Cross-species interaction evidence and human LYRM-network studies (tang2020mitochondrialoxphosbiogenesis pages 18-20, dibley2020themitochondrialacylcarrier pages 2-3, dibley2020themitochondrialacylcarrier pages 1-2) | Moderate for the family; low for CG34117 | Disrupting the yeast FMC1 LYR motif can abolish ACP association without impairing growth or complex V assembly; fly ACP binding has not been tested. |
| Direct fly evidence | No CG34117/Q0KI97-specific peer-reviewed functional study, catalytic assay, phenotype, localization result, interaction test, or quantitative complex V measurement was identified. | Literature assessment; available sources provide family-level rather than CG34117-specific evidence (tang2020mitochondrialoxphosbiogenesis pages 18-20, tang2020mitochondrialoxphosbiogenesis pages 16-18, dibley2020themitochondrialacylcarrier pages 2-3) | High confidence in the documented evidence gap | An unsuccessful literature search cannot exclude unpublished or unindexed data; most proposed functions remain homology-based hypotheses. |


*Table: Evidence-tier summary separating verified identity from homology-based functional inference for Drosophila CG34117/Q0KI97. It highlights the absence of direct fly-specific functional evidence.*

## 1. Identity verification and evidence boundary

The supplied record identifies Q0KI97 as a protein encoded by *D. melanogaster* **CG34117**, with the alternative names Dmel_CG34117 and Dmel\\CG34117. Its FMC1-family and Complex1_LYR_2 assignments agree with the broader classification of FMC1 among small mitochondrial LYRM-related proteins. LYRM proteins are generally basic proteins of approximately **10–22 kDa**, often bearing an N-terminal LYR-like motif and conserved downstream residues; they commonly participate in mitochondrial respiratory-complex or mitoribosome biogenesis rather than catalysis (tang2020mitochondrialoxphosbiogenesis pages 16-18).

No conflicting publication for a similarly named fly protein was found. However, the literature contains human **FMC1/C7orf55** and fungal **Fmc1p**; neither should be described as CG34117. The absence of a CG34117-specific paper means that the supplied database identity is secure, but biological function remains primarily computationally inferred.

Authoritative identifier URLs are:

- UniProt Q0KI97: https://www.uniprot.org/uniprotkb/Q0KI97/entry
- FlyBase FBgn0083953: https://flybase.org/reports/FBgn0083953
- InterPro IPR037667: https://www.ebi.ac.uk/interpro/entry/InterPro/IPR037667/
- Pfam PF13233: https://www.ebi.ac.uk/interpro/entry/pfam/PF13233/

These database links identify the target and domain calls; they should not be interpreted as equivalent to experimental validation.

## 2. Predicted primary molecular function

### Assembly factor, not enzyme

FMC1-family proteins are best understood as **accessory biogenesis factors**. In yeast, Fmc1 supports assembly or stability of mitochondrial ATP synthase, particularly its catalytic F₁ portion and particularly under heat stress. Loss-of-function effects can be suppressed by increased Atp12, linking Fmc1 functionally to the F₁-assembly chaperone Atp12 (potocka2007assemblyfactorsin pages 41-45). A major OXPHOS-biogenesis review similarly describes FMC1 as a complex-V assembly factor that stabilizes Atp12, the yeast counterpart of mammalian ATPAF2 (tang2020mitochondrialoxphosbiogenesis pages 18-20).

Accordingly, CG34117 is unlikely to catalyze a conventional chemical reaction. There is **no established substrate specificity**, Michaelis constant, turnover number, cofactor requirement, or transported molecule. Its probable “substrates” in a loose chaperone sense are ATP-synthase assembly intermediates and/or an ATP12-like assembly factor, but these should not be represented as enzymatic substrates.

### Proposed mechanistic role

The most defensible model is:

1. CG34117 is synthesized in the cytosol and imported into mitochondria.
2. In the mitochondrial matrix or at the matrix-facing surface of the inner membrane, it supports formation or stability of an F₁-ATPase assembly intermediate.
3. It may stabilize or cooperate with the fly ATP12/ATPAF2 counterpart, promoting productive incorporation of catalytic F₁ subunits.
4. Mature F₁ then associates with the membrane-embedded F₀ sector to form functional complex V.

Steps 1–4 are a cross-species model, not a pathway demonstrated experimentally for CG34117. Yeast evidence supports the Atp12 relationship, but overexpression rescue alone does not necessarily establish direct physical binding (tang2020mitochondrialoxphosbiogenesis pages 18-20, potocka2007assemblyfactorsin pages 41-45).

## 3. Cellular localization

The protein is most likely **mitochondrial**. LYRM proteins and mitochondrial ACP operate primarily in the mitochondrial matrix, and ATP-synthase F₁ assembly occurs in a matrix-facing environment. Therefore, the likely site of CG34117 action is the **matrix or matrix side of the inner mitochondrial membrane**, near complex-V assembly intermediates (dibley2020themitochondrialacylcarrier pages 2-3).

This localization has not been demonstrated for CG34117 by fluorescent tagging, mitochondrial fractionation, protease protection, import assays, or immuno-electron microscopy. “Mitochondrial” is consequently a moderate-confidence prediction; the precise subcompartment is lower confidence. CG34117 should not presently be annotated as an integral inner-membrane protein or stable mature ATP-synthase subunit without additional evidence.

## 4. Biochemical pathway

CG34117 most plausibly acts in **mitochondrial oxidative phosphorylation**, specifically **complex-V biogenesis**. Mature F₁F₀-ATP synthase uses the proton-motive force generated by respiratory complexes to synthesize ATP from ADP and inorganic phosphate. CG34117 would support this process indirectly by promoting enzyme assembly rather than participating in proton translocation or ATP synthesis itself. Reviews classify LYRM proteins as late-stage accessory factors that regulate incorporation or activation of OXPHOS subunits and cofactors (tang2020mitochondrialoxphosbiogenesis pages 16-18).

Thus, the expected pathway placement is:

**nuclear expression → mitochondrial import → F₁/complex-V assembly → mature ATP synthase → oxidative phosphorylation and ATP production.**

There is no direct evidence that fly CG34117 regulates a signaling cascade. Any effects on AMPK, stress signaling, development, lifespan, locomotion, or fertility would currently be downstream predictions of altered bioenergetics, not established primary functions.

## 5. Relationship to mitochondrial ACP and the LYRM family

Mitochondrial acyl-carrier protein—NDUFAB1 in humans—is a soluble matrix protein whose 4′-phosphopantetheine-linked acyl chain promotes binding to multiple LYRM proteins. Human interaction-network work found associations with **nine known LYRM proteins** and more than **20 other proteins** involved in respiratory-chain or mitoribosome assembly, illustrating the breadth of ACP-linked mitochondrial complex biogenesis (dibley2020themitochondrialacylcarrier pages 1-2). Broader studies connect ACP–LYRM modules to complexes I, II, III, and V (dibley2020themitochondrialacylcarrier pages 2-3).

FMC1 can interact with mitochondrial ACP in yeast and humans. Importantly, yeast mutation of the FMC1 LYR motif can disrupt the ACP interaction without measurably impairing growth or complex-V assembly. The ATP-synthase assembly function therefore may be at least partly **ACP-independent** (tang2020mitochondrialoxphosbiogenesis pages 18-20). For CG34117, ACP binding is plausible from the Complex1_LYR_2/LYRM-like domain but remains untested; it should be annotated as a predicted interaction, not a confirmed partner.

## 6. Direct versus inferred evidence

### Direct evidence for CG34117

No indexed peer-reviewed study was identified that reports any of the following for CG34117/Q0KI97:

- knockout, knockdown, or mutant phenotype;
- rescue by a wild-type transgene;
- complex-V abundance or blue-native PAGE analysis;
- ATP-synthesis, oxygen-consumption, or membrane-potential measurements;
- catalytic or substrate-binding assay;
- physical interaction with ATP12/ATPAF2, ATP-synthase subunits, or mitochondrial ACP;
- microscopy or biochemical localization;
- tissue-specific protein abundance or a quantitative expression effect.

The available literature therefore supplies no fly-specific effect size, penetrance, binding constant, assembly percentage, or activity measurement. Family-level reviews likewise explicitly do not provide direct CG34117 evidence (tang2020mitochondrialoxphosbiogenesis pages 18-20, tang2020mitochondrialoxphosbiogenesis pages 16-18, dibley2020themitochondrialacylcarrier pages 2-3).

### Strength of inference

- **High confidence:** correct accession–gene–organism identity, given the supplied UniProt/FlyBase-linked information.
- **Moderate confidence:** mitochondrial FMC1/LYRM-family accessory protein; non-enzymatic role in complex-V assembly.
- **Low-to-moderate confidence:** action on F₁ assembly through stabilization or support of a fly ATP12/ATPAF2 homolog.
- **Low confidence:** direct mitochondrial-ACP binding and exact matrix/inner-membrane topology.
- **Unsupported:** a catalytic reaction, defined substrate specificity, stable membership in mature ATP synthase, or a specific fly phenotype.

## 7. Recent developments and current understanding

No 2023–2024 publication specific to CG34117 was retrieved. Recent mitochondrial research continues to support a general view in which OXPHOS biogenesis depends on numerous transient ancillary factors rather than spontaneous assembly of structural subunits. The most directly relevant comprehensive source recovered was Tang et al., published **29 May 2020**, which places FMC1 among LYRM-associated OXPHOS assembly factors and discusses its Atp12 and ACP relationships: https://doi.org/10.3390/ijms21113820 (tang2020mitochondrialoxphosbiogenesis pages 18-20, tang2020mitochondrialoxphosbiogenesis pages 16-18).

Dibley et al., published **January 2020**, experimentally mapped the human mitochondrial ACP interaction network and demonstrated that different LYRM proteins specialize in assembling complex I or the mitoribosome. This supports the expert interpretation that a shared LYRM-like fold does not by itself prove the exact client complex of every family member: https://doi.org/10.1074/mcp.RA119.001784 (dibley2020themitochondrialacylcarrier pages 2-3, dibley2020themitochondrialacylcarrier pages 1-2).

A relevant 2023 review of plant OXPHOS biogenesis also recognizes FMC1 among complex-V assembly factors, indicating that FMC1-like involvement in ATP-synthase biogenesis is considered across diverse eukaryotic literature. Nevertheless, plant and fungal results cannot replace direct validation in *Drosophila*.

## 8. Current applications and real-world implementation

CG34117 itself has no established clinical or industrial application. Its immediate value is as an **experimental target for functional genomics and mitochondrial biology**. A fly model could test whether metazoan FMC1-family proteins preserve the heat-sensitive F₁-assembly role first defined in yeast. Because *Drosophila* permits tissue-specific RNA interference, CRISPR editing, and physiological assays, CG34117 perturbation could connect molecular complex-V assembly to organismal energy demand without assuming a human disease association.

The most informative validation program would combine:

1. endogenous fluorescent or epitope tagging with mitochondrial markers;
2. mitochondrial fractionation and protease-protection analysis;
3. CG34117 knockout or inducible RNAi, including heat-stress conditions;
4. blue-native PAGE and complex-V in-gel activity assays;
5. oxygen-consumption, ATP-production, and membrane-potential measurements;
6. co-immunoprecipitation or proximity labeling for ATP12/ATPAF2-like proteins, ATP-synthase intermediates, and mitochondrial ACP;
7. rescue with wild-type CG34117 and an LYR-motif mutant.

A result in which CG34117 loss selectively reduces assembled complex V while sparing other respiratory complexes, followed by rescue with wild-type protein, would strongly validate the proposed primary function. Comparing wild-type and LYR-mutant rescue would determine whether any ACP interaction is mechanistically necessary.

## Final annotation recommendation

**Recommended description:** “Probable mitochondrial ATP synthase assembly factor FMC1 homolog.”

**Recommended molecular-function statement:** “Predicted non-catalytic accessory factor involved in assembly or stability of the mitochondrial F₁F₀-ATP synthase, probably acting during F₁-sector biogenesis.”

**Recommended localization:** “Mitochondrion; matrix or matrix-facing inner-membrane assembly environment, predicted.”

**Recommended pathway:** “Mitochondrial oxidative-phosphorylation complex-V biogenesis.”

**Critical qualifier:** The gene symbol **Dmel\\CG34117** is not being treated as another organism’s FMC1. Literature is limited for this specific protein, and its function should currently be regarded as an inference from the supplied UniProt family/domain annotation and cross-species FMC1/LYRM evidence, not as experimentally established in *Drosophila melanogaster*.

References

1. (tang2020mitochondrialoxphosbiogenesis pages 16-18): Jia Xin Tang, Kyle Thompson, Robert W. Taylor, and Monika Oláhová. Mitochondrial oxphos biogenesis: co-regulation of protein synthesis, import, and assembly pathways. International Journal of Molecular Sciences, 21:3820, May 2020. URL: https://doi.org/10.3390/ijms21113820, doi:10.3390/ijms21113820. This article has 259 citations.

2. (tang2020mitochondrialoxphosbiogenesis pages 18-20): Jia Xin Tang, Kyle Thompson, Robert W. Taylor, and Monika Oláhová. Mitochondrial oxphos biogenesis: co-regulation of protein synthesis, import, and assembly pathways. International Journal of Molecular Sciences, 21:3820, May 2020. URL: https://doi.org/10.3390/ijms21113820, doi:10.3390/ijms21113820. This article has 259 citations.

3. (potocka2007assemblyfactorsin pages 41-45): A Potocká. Assembly factors in the biogenesis of mitochondrial atp synthase. Unknown journal, 2007.

4. (dibley2020themitochondrialacylcarrier pages 2-3): Marris G. Dibley, Luke E. Formosa, Baobei Lyu, Boris Reljic, Dylan McGann, Linden Muellner-Wong, Felix Kraus, Alice J. Sharpe, David A. Stroud, and Michael T. Ryan. The mitochondrial acyl-carrier protein interaction network highlights important roles for lyrm family members in complex i and mitoribosome assembly. Jan 2020. URL: https://doi.org/10.1074/mcp.ra119.001784, doi:10.1074/mcp.ra119.001784. This article has 74 citations and is from a domain leading peer-reviewed journal.

5. (tang2020mitochondrialoxphosbiogenesis pages 30-32): Jia Xin Tang, Kyle Thompson, Robert W. Taylor, and Monika Oláhová. Mitochondrial oxphos biogenesis: co-regulation of protein synthesis, import, and assembly pathways. International Journal of Molecular Sciences, 21:3820, May 2020. URL: https://doi.org/10.3390/ijms21113820, doi:10.3390/ijms21113820. This article has 259 citations.

6. (dibley2020themitochondrialacylcarrier pages 1-2): Marris G. Dibley, Luke E. Formosa, Baobei Lyu, Boris Reljic, Dylan McGann, Linden Muellner-Wong, Felix Kraus, Alice J. Sharpe, David A. Stroud, and Michael T. Ryan. The mitochondrial acyl-carrier protein interaction network highlights important roles for lyrm family members in complex i and mitoribosome assembly. Jan 2020. URL: https://doi.org/10.1074/mcp.ra119.001784, doi:10.1074/mcp.ra119.001784. This article has 74 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CG34117-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. tang2020mitochondrialoxphosbiogenesis pages 16-18
2. dibley2020themitochondrialacylcarrier pages 2-3
3. potocka2007assemblyfactorsin pages 41-45
4. tang2020mitochondrialoxphosbiogenesis pages 18-20
5. dibley2020themitochondrialacylcarrier pages 1-2
6. tang2020mitochondrialoxphosbiogenesis pages 30-32
7. https://www.uniprot.org/uniprotkb/Q0KI97/entry
8. https://flybase.org/reports/FBgn0083953
9. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR037667/
10. https://www.ebi.ac.uk/interpro/entry/pfam/PF13233/
11. https://doi.org/10.3390/ijms21113820
12. https://doi.org/10.1074/mcp.RA119.001784
13. https://doi.org/10.3390/ijms21113820,
14. https://doi.org/10.1074/mcp.ra119.001784,