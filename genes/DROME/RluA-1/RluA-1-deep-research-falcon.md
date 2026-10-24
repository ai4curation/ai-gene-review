---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:05:01.848702'
end_time: '2026-09-08T18:12:47.511010'
duration_seconds: 465.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: RluA-1
  gene_symbol: RluA-1
  uniprot_accession: Q9VKV0
  protein_description: 'RecName: Full=Pseudouridylate synthase RPUSD2 {ECO:0000256|ARBA:ARBA00072682};
    EC=5.4.99.28 {ECO:0000256|ARBA:ARBA00038944}; EC=5.4.99.42 {ECO:0000256|ARBA:ARBA00096568};
    AltName: Full=RNA pseudouridylate synthase domain-containing protein 2 {ECO:0000256|ARBA:ARBA00080257};'
  gene_info: Name=RluA-1 {ECO:0000313|EMBL:AAF52959.2, ECO:0000313|FlyBase:FBgn0051719};
    Synonyms=CG13143 {ECO:0000313|EMBL:AAF52959.2}, CG7475 {ECO:0000313|EMBL:AAF52959.2},
    Dmel\CG31719 {ECO:0000313|EMBL:AAF52959.2}, RluA1 {ECO:0000313|EMBL:AAF52959.2};
    ORFNames=CG31719 {ECO:0000313|EMBL:AAF52959.2, ECO:0000313|FlyBase:FBgn0051719},
    Dmel_CG31719 {ECO:0000313|EMBL:AAF52959.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the pseudouridine synthase RluA family.
  protein_domains: PsdUridine_synth_cat_dom_sf. (IPR020103); PsdUridine_synth_RluA-like_CS.
    (IPR006224); PsdUridine_synth_RluC/D. (IPR006225); PsdUridine_synth_RsuA/RluA.
    (IPR006145); RluA_PseudoU_synthase. (IPR050188)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: RluA-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VKV0
- **Protein Description:** RecName: Full=Pseudouridylate synthase RPUSD2 {ECO:0000256|ARBA:ARBA00072682}; EC=5.4.99.28 {ECO:0000256|ARBA:ARBA00038944}; EC=5.4.99.42 {ECO:0000256|ARBA:ARBA00096568}; AltName: Full=RNA pseudouridylate synthase domain-containing protein 2 {ECO:0000256|ARBA:ARBA00080257};
- **Gene Information:** Name=RluA-1 {ECO:0000313|EMBL:AAF52959.2, ECO:0000313|FlyBase:FBgn0051719}; Synonyms=CG13143 {ECO:0000313|EMBL:AAF52959.2}, CG7475 {ECO:0000313|EMBL:AAF52959.2}, Dmel\CG31719 {ECO:0000313|EMBL:AAF52959.2}, RluA1 {ECO:0000313|EMBL:AAF52959.2}; ORFNames=CG31719 {ECO:0000313|EMBL:AAF52959.2, ECO:0000313|FlyBase:FBgn0051719}, Dmel_CG31719 {ECO:0000313|EMBL:AAF52959.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the pseudouridine synthase RluA family.
- **Key Domains:** PsdUridine_synth_cat_dom_sf. (IPR020103); PsdUridine_synth_RluA-like_CS. (IPR006224); PsdUridine_synth_RluC/D. (IPR006225); PsdUridine_synth_RsuA/RluA. (IPR006145); RluA_PseudoU_synthase. (IPR050188)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RluA-1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RluA-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RluA-1** (gene ID: RluA-1, UniProt: Q9VKV0) in DROME.

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
- **UniProt Accession:** Q9VKV0
- **Protein Description:** RecName: Full=Pseudouridylate synthase RPUSD2 {ECO:0000256|ARBA:ARBA00072682}; EC=5.4.99.28 {ECO:0000256|ARBA:ARBA00038944}; EC=5.4.99.42 {ECO:0000256|ARBA:ARBA00096568}; AltName: Full=RNA pseudouridylate synthase domain-containing protein 2 {ECO:0000256|ARBA:ARBA00080257};
- **Gene Information:** Name=RluA-1 {ECO:0000313|EMBL:AAF52959.2, ECO:0000313|FlyBase:FBgn0051719}; Synonyms=CG13143 {ECO:0000313|EMBL:AAF52959.2}, CG7475 {ECO:0000313|EMBL:AAF52959.2}, Dmel\CG31719 {ECO:0000313|EMBL:AAF52959.2}, RluA1 {ECO:0000313|EMBL:AAF52959.2}; ORFNames=CG31719 {ECO:0000313|EMBL:AAF52959.2, ECO:0000313|FlyBase:FBgn0051719}, Dmel_CG31719 {ECO:0000313|EMBL:AAF52959.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the pseudouridine synthase RluA family.
- **Key Domains:** PsdUridine_synth_cat_dom_sf. (IPR020103); PsdUridine_synth_RluA-like_CS. (IPR006224); PsdUridine_synth_RluC/D. (IPR006225); PsdUridine_synth_RsuA/RluA. (IPR006145); RluA_PseudoU_synthase. (IPR050188)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RluA-1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RluA-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RluA-1** (gene ID: RluA-1, UniProt: Q9VKV0) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* RluA-1 (UniProt Q9VKV0)

## Executive conclusion

The gene symbol **RluA-1 is literature-limited for this specific protein**. Searches using **RluA-1, RluA1, Q9VKV0, CG31719, CG7475, and FBgn0051719** did not identify a primary study that biochemically characterizes the encoded *Drosophila melanogaster* protein. The available evidence therefore supports a careful annotation rather than a definitive substrate assignment.

The supplied UniProt record identifies Q9VKV0 as *D. melanogaster* RluA-1, an **RluA-family RNA pseudouridine synthase**. Its most defensible primary function is consequently the ATP-independent isomerization of one or more uridines in RNA to pseudouridine (Ψ). However, the endogenous fly RNA substrate, modified nucleotide position, subcellular compartment, physiological pathway, and phenotype have not been established in the retrieved literature. Published experiments on bacterial RluA demonstrate dual rRNA/tRNA specificity, but those results must not be presented as direct evidence for Q9VKV0.

## 1. Identity verification

**Target verified:**

- **Protein:** Q9VKV0
- **Organism:** *Drosophila melanogaster* (fruit fly; DROME)
- **Gene:** RluA-1
- **Aliases supplied by UniProt:** RluA1, CG13143, CG7475, CG31719, Dmel\CG31719
- **FlyBase identifier supplied:** FBgn0051719
- **Annotated family:** RluA pseudouridine-synthase family
- **Annotated domains/signatures:** RluA/RsuA-like and RluC/D-related pseudouridine-synthase catalytic domains/signatures

These identifiers and domain calls are internally consistent with an RNA pseudouridine synthase. Comparative analyses establish RluA and RsuA as related pseudouridine-synthase families and associate members of this wider group with structured-RNA recognition. Some family proteins carry accessory S4-like RNA-binding modules, although such modules are not universal and their presence or absence cannot alone determine a native substrate (aravind1999novelpredictedrnabinding pages 3-6, aravind1999novelpredictedrnabinding pages 2-3).

No retrieved paper established that a similarly named non-fly protein was Q9VKV0. Conversely, most experimentally characterized “RluA” literature concerns bacterial enzymes, especially *Escherichia coli* RluA. That literature is used below only for evolutionary and mechanistic inference.

## 2. Primary biochemical function

### 2.1 Reaction

Pseudouridine synthases catalyze the post-transcriptional isomerization

**RNA–uridine → RNA–pseudouridine (Ψ).**

The reaction replaces uridine’s N1–C1′ N-glycosidic linkage with a C5–C1′ carbon–carbon linkage while preserving nucleotide composition. It requires neither ATP nor an external energy source (koonin1996pseudouridinesynthasesfour pages 1-2). The two EC assignments in the supplied record—**EC 5.4.99.28** and **EC 5.4.99.42**—are consistent with RNA uridine isomerase annotations, but they do not by themselves prove which RNA or nucleotide Q9VKV0 modifies.

### 2.2 Catalytic mechanism

RluA-family proteins share the conserved catalytic architecture of stand-alone pseudouridine synthases. Sequence comparisons identified invariant acidic residues, particularly a conserved aspartate, in a loop implicated in uridine recognition and catalysis (koonin1996pseudouridinesynthasesfour pages 3-5). Mechanistic-probe experiments with bacterial RluA and other pseudouridine synthases support covalent participation of the catalytic machinery during pyrimidine rearrangement. Experiments with 5-fluorouridine-containing RNA also ruled out particular simple ester-hydrolysis interpretations and showed hydration of rearranged probe products (mcdonald2011thehandlingof pages 8-10, mcdonald2011thehandlingof pages 10-11, mcdonald2011thehandlingof pages 14-20).

This is strong evidence for the **family mechanism**, not direct evidence that purified Q9VKV0 has been assayed. A definitive fly-protein test would require catalytic-Asp mutagenesis and activity measurements with candidate RNAs.

## 3. Substrate specificity

### What is established

The exact physiological substrate of *Drosophila* RluA-1 is **unknown**. No retrieved study reported:

- a Q9VKV0-dependent Ψ site;
- loss of a specific modification in an RluA-1 knockout;
- activity of purified Q9VKV0 on a fly RNA;
- or rescue by wild-type but not catalytic-dead RluA-1.

### What can be inferred cautiously

The founding bacterial example, *E. coli* RluA, forms **Ψ746 in 23S rRNA** and can form **Ψ32 in tRNA^Phe**, at least in vitro. Thus, one experimentally characterized RluA homolog recognizes both rRNA and tRNA, probably by recognizing related local RNA structures rather than RNA class alone (koonin1996pseudouridinesynthasesfour pages 2-3, aravind1999novelpredictedrnabinding pages 2-3, koonin1996pseudouridinesynthasesfour pages 3-5).

This dual specificity makes structured rRNA and anticodon-loop tRNA plausible candidate classes for fly RluA-1, but it does **not** establish that Q9VKV0 modifies the homologous positions—or even the same RNA classes. Eukaryotic paralogs frequently partition ancestral activities through altered targeting domains, expression, or localization.

## 4. Biological process and pathway assignment

The best-supported broad assignment is **post-transcriptional RNA modification**, with possible downstream effects on RNA maturation, structure, and translation. Pseudouridine can alter RNA conformational behavior and RNA–protein interactions; tRNA modification can affect decoding and fragmentation, whereas rRNA modification may influence ribosome assembly or function. These are general consequences of RNA modification, not demonstrated RluA-1 phenotypes (wu2024trnamodificationsand pages 6-7, atoi2023massspectrometricstudies pages 37-40).

A 2024 review emphasizes that Ψ can affect multiple stages of the tRNA life cycle and translation, but also notes that physiological functions remain unresolved for many endogenous sites. For comparison, yeast Pus3 modifies U38/U39 in at least 19 tRNAs and is needed for growth at elevated temperature, illustrating how an enzyme’s exact targets and phenotype require direct mapping rather than inference from family membership (wu2024trnamodificationsand pages 6-7).

Accordingly, Q9VKV0 should currently be annotated as participating in an **RNA-pseudouridylation biochemical pathway**, not assigned to a specific signaling cascade. No defensible evidence links it specifically to a developmental, stress-response, neuronal, immune, or disease pathway in the fly.

## 5. Cellular localization

The cellular compartment in which endogenous RluA-1 operates is **not established by the retrieved literature**. Nuclear/nucleolar localization would be compatible with nuclear rRNA processing; cytosolic localization would be compatible with cytoplasmic tRNA or mRNA modification; mitochondrial localization would imply mitochondrial RNA substrates. None of these alternatives should be asserted without validated targeting-sequence analysis, fractionation, or microscopy.

The bacterial name “RluA” provides no localization information for a eukaryotic protein. Likewise, catalytic-domain classification predicts chemistry, not cellular compartment.

## 6. Evidence assessment

The following table separates direct annotation from family-level inference.

| Topic | Conclusion | Evidence type / organism | Confidence | Key limitation |
|---|---|---|---|---|
| Identity | Q9VKV0 corresponds to *Drosophila melanogaster* RluA-1, with aliases CG31719, CG7475 and FBgn0051719, as specified by the supplied UniProt record. Exact-identifier literature searches found no contradictory identity. | Database annotation / *D. melanogaster* | High for identity | No retrieved primary paper independently characterized Q9VKV0; the identity conclusion depends principally on the supplied UniProt annotation. |
| Enzyme reaction | The predicted reaction is ATP-independent isomerization of an RNA uridine to pseudouridine (Ψ), replacing the N1–C1′ N-glycosidic bond with a C5–C1′ carbon–carbon bond without changing nucleotide composition. | Conserved pseudouridine-synthase biochemistry; family-level evidence (koonin1996pseudouridinesynthasesfour pages 1-2) | High for the enzyme family; moderate for Q9VKV0 | The reaction has not been demonstrated directly with purified fly RluA-1 or an RluA-1-deficient fly sample. |
| Catalytic mechanism | RluA-family enzymes use a conserved active-site aspartate in covalent catalysis; mechanistic-probe studies support a conserved rearrangement pathway and exclude some proposed ester-hydrolysis models. | Comparative sequence analysis and biochemical experiments on bacterial pseudouridine synthases, including RluA (koonin1996pseudouridinesynthasesfour pages 3-5, mcdonald2011thehandlingof pages 8-10, mcdonald2011thehandlingof pages 10-11, mcdonald2011thehandlingof pages 14-20) | High at family level; moderate-to-low for Q9VKV0 | Catalytic residues and reaction intermediates have not been tested experimentally in Q9VKV0; bacterial mechanism evidence must not be presented as direct fly-protein evidence. |
| Substrate specificity | The exact RNA class, transcript and uridine position modified by fly RluA-1 are unknown. Bacterial *E. coli* RluA modifies 23S-rRNA U746 and, at least in vitro, tRNA-Phe U32, showing that an RluA homolog can recognize both rRNA and tRNA. | Direct bacterial RluA evidence plus homology-based inference (aravind1999novelpredictedrnabinding pages 3-6, koonin1996pseudouridinesynthasesfour pages 2-3, aravind1999novelpredictedrnabinding pages 2-3) | High for bacterial RluA; low for Q9VKV0 substrate assignment | Dual rRNA/tRNA specificity cannot be transferred automatically to Q9VKV0. No fly knockout-dependent Ψ map or purified-enzyme substrate assay was found. |
| Domains and family | The supplied annotation places Q9VKV0 in the RluA pseudouridine-synthase family and identifies RluA/RsuA-like catalytic signatures, consistent with a structured-RNA-modifying enzyme. Some RluA-family proteins also possess accessory RNA-binding modules that may influence target recognition. | UniProt/InterPro annotation for Q9VKV0; comparative family/domain analysis (aravind1999novelpredictedrnabinding pages 3-6, aravind1999novelpredictedrnabinding pages 2-3) | High for family assignment; moderate for functional implications | Domain presence supports catalytic capability but does not establish the native RNA target, reaction rate or intracellular site of action. |
| Cellular localization | The compartment in which endogenous RluA-1 acts is not established by the retrieved literature. Nuclear, nucleolar, cytosolic or mitochondrial localization should therefore remain unassigned pending direct evidence. | Absence of Q9VKV0-specific microscopy, fractionation or validated targeting data | Unknown | Localization cannot be inferred reliably from the bacterial RluA name, RNA-substrate possibilities or broad family membership. |
| Pathway and biological role | The most defensible role is participation in post-transcriptional RNA modification and, indirectly, RNA maturation and translation. A specific fly signaling pathway, ribosome-biogenesis step or tRNA-maturation pathway has not been demonstrated. | Functional inference from pseudouridine-synthase family biology (koonin1996pseudouridinesynthasesfour pages 1-2, aravind1999novelpredictedrnabinding pages 2-3) | Moderate for RNA modification; low for any specific pathway | No Q9VKV0-specific genetic, biochemical or epistasis evidence links the protein to a defined pathway or phenotype. |
| Recent 2023–2024 developments | Recent work emphasizes transcriptome-scale modification mapping, chemoproteomic capture of RNA-modifying enzymes and cell-type-specific functions of tRNA pseudouridylation. A 2024 review notes 12 human PUS-related proteins and illustrates enzyme-specific tRNA effects, while 2023 chemoproteomic approaches enable native-substrate discovery; none directly studies fly RluA-1 (wu2024trnamodificationsand pages 6-7). | Recent field-level reviews and methods; primarily mammalian/human systems | High as general field context; not evidence for Q9VKV0 | These developments motivate fly knockout/rescue and substrate-mapping experiments but provide no direct Q9VKV0 substrate, localization or phenotype. |
| Quantitative context | General RNA-modification surveys report that modified residues can constitute up to approximately 17% of tRNA residues and about 2% of rRNA residues; these values concern all modifications, not Ψ or RluA-1 specifically (atoi2023massspectrometricstudies pages 37-40). | 2023 mammalian RNA-modification synthesis | Moderate as broad context; none for Q9VKV0 | The figures cannot be used to estimate RluA-1 activity, substrate number or pseudouridine stoichiometry in flies. |


*Table: Evidence-tier assessment for *Drosophila melanogaster* RluA-1/Q9VKV0, distinguishing database annotation and family-level inference from direct protein-specific evidence. It highlights that the fly enzyme’s native substrates and cellular localization remain unknown.*

## 7. Recent developments, 2023–2024

No 2023–2024 publication directly characterizing Q9VKV0 was identified. The important recent developments are therefore methodological opportunities for resolving its function:

1. **Enzyme-resolved Ψ mapping.** Modern transcriptome-wide and quantitative approaches can compare wild-type, knockout, rescue, and catalytic-dead rescue samples to assign individual Ψ sites to an enzyme. Recent literature emphasizes dynamically regulated Ψ in ncRNA and mRNA but also warns that overlapping synthase specificities can mask single-enzyme loss (malviya2026trub1mediatedpseudouridylationis pages 9-9).

2. **Chemoproteomic substrate discovery.** A 2023 review describes mechanism-based metabolic probes and RNA-mediated activity-based protein profiling for capturing RNA-modifying enzymes with native substrates, followed by quantitative proteomics and nucleotide-resolution sequencing. Such methods could be adapted to RluA-1, although the cited applications were not performed on Q9VKV0. Publication: Dai, Yu & Kleiner, September 2023, *Accounts of Chemical Research*, DOI/URL: https://doi.org/10.1021/acs.accounts.3c00450.

3. **Structure-guided specificity analysis.** Recent work in other PUS families has shown that RNA selectivity can depend on features outside the catalytic core. For RluA-1, structural prediction followed by biochemical testing of candidate fly tRNAs and rRNAs would be more informative than transferring bacterial site assignments.

4. **Cell-type-specific interpretation.** The 2024 tRNA-modification literature increasingly treats Ψ as potentially conditional and cell-type-specific rather than uniformly constitutive. The same review lists 12 human PUS-related proteins, illustrating the extensive paralog complexity in metazoans; this human count is comparative context, not a statistic about flies (wu2024trnamodificationsand pages 6-7). Publication: Wu et al., September 2024, *Cell Biology and Toxicology*, DOI/URL: https://doi.org/10.1007/s10565-024-09919-9.

## 8. Current applications and real-world relevance

There is no documented clinical, industrial, diagnostic, or biotechnology application specific to fly RluA-1. Its immediate practical value is as a **functional-genomics target** for understanding enzyme-specific RNA modification in a genetically tractable metazoan.

Broader applications of pseudouridylation research include mapping RNA maturation pathways, engineering RNA stability or translation, identifying modification-associated disease mechanisms, and designing substrate-discovery tools. These are field-level applications and should not be interpreted as validated uses of Q9VKV0. The most relevant near-term implementation would be a *Drosophila* RluA-1 knockout/rescue system combined with quantitative Ψ mapping and subcellular localization.

## 9. Relevant quantitative context

Recent RNA-modification synthesis reports that modified nucleotides collectively can account for **up to approximately 17% of tRNA residues** and approximately **2% of rRNA residues**. These percentages encompass all modification types, not only Ψ, and cannot estimate RluA-1 activity or target number (atoi2023massspectrometricstudies pages 37-40).

The most precise RluA-specific site data remain bacterial: *E. coli* RluA modifies 23S-rRNA position 746 and can modify tRNA^Phe position 32 (koonin1996pseudouridinesynthasesfour pages 2-3). No corresponding quantitative estimate—site count, occupancy, catalytic rate, expression level, or phenotype magnitude—was found for Q9VKV0.

## 10. Expert interpretation and recommended annotation

**Recommended primary annotation:**

> *Drosophila melanogaster* RluA-1/Q9VKV0 is a predicted RluA-family RNA pseudouridine synthase that likely catalyzes ATP-independent isomerization of uridine to pseudouridine in a structured RNA substrate.

**Do not yet annotate as established:**

- a specific tRNA, rRNA, mRNA, or snRNA substrate;
- modification of sites homologous to bacterial 23S-rRNA U746 or tRNA^Phe U32;
- nuclear, nucleolar, cytosolic, or mitochondrial localization;
- a specific developmental or signaling pathway;
- or an organismal phenotype.

The highest-priority experiments are: (1) CRISPR null and catalytic-Asp knock-in alleles; (2) wild-type and catalytic-dead rescue; (3) quantitative Ψ mapping of fractionated tRNA, rRNA, and poly(A) RNA; (4) purified-protein assays against mapped candidate substrates; and (5) endogenous-tag imaging with biochemical fractionation. Together, these would distinguish catalytic activity from structural or indirect effects and provide the first defensible substrate and localization assignment.

## References

- Koonin EV. “Pseudouridine synthases: four families of enzymes containing a putative uridine-binding motif…” *Nucleic Acids Research*. June 1996. https://doi.org/10.1093/nar/24.12.2411 (koonin1996pseudouridinesynthasesfour pages 2-3, koonin1996pseudouridinesynthasesfour pages 1-2, koonin1996pseudouridinesynthasesfour pages 3-5)
- Aravind L, Koonin EV. “Novel Predicted RNA-Binding Domains Associated with the Translation Machinery.” *Journal of Molecular Evolution*. March 1999. https://doi.org/10.1007/pl00006472 (aravind1999novelpredictedrnabinding pages 3-6, aravind1999novelpredictedrnabinding pages 2-3)
- McDonald MK et al. “The Handling of the Mechanistic Probe 5-Fluorouridine by… TruA… TruB and RluA.” *Biochemistry*. December 2011. https://doi.org/10.1021/bi101737z (mcdonald2011thehandlingof pages 8-10, mcdonald2011thehandlingof pages 10-11, mcdonald2011thehandlingof pages 14-20)
- Dai W, Yu NJ, Kleiner RE. “Chemoproteomic Approaches to Studying RNA Modification-Associated Proteins.” *Accounts of Chemical Research*. September 2023. https://doi.org/10.1021/acs.accounts.3c00450
- Wu D et al. “tRNA modifications and tRNA-derived small RNAs: new insights of tRNA in human disease.” *Cell Biology and Toxicology*. September 2024. https://doi.org/10.1007/s10565-024-09919-9 (wu2024trnamodificationsand pages 6-7)
- Atoi PA. “Mass spectrometric studies of RNA modification patterns in mammals.” 2023. https://doi.org/10.21248/gups.74238 (atoi2023massspectrometricstudies pages 37-40)

References

1. (aravind1999novelpredictedrnabinding pages 3-6): L. Aravind and Eugene V. Koonin. Novel predicted rna-binding domains associated with the translation machinery. Journal of Molecular Evolution, 48:291-302, Mar 1999. URL: https://doi.org/10.1007/pl00006472, doi:10.1007/pl00006472. This article has 264 citations and is from a peer-reviewed journal.

2. (aravind1999novelpredictedrnabinding pages 2-3): L. Aravind and Eugene V. Koonin. Novel predicted rna-binding domains associated with the translation machinery. Journal of Molecular Evolution, 48:291-302, Mar 1999. URL: https://doi.org/10.1007/pl00006472, doi:10.1007/pl00006472. This article has 264 citations and is from a peer-reviewed journal.

3. (koonin1996pseudouridinesynthasesfour pages 1-2): E. V. Koonin. Pseudouridine synthases: four families of enzymes containing a putative uridine-binding motif also conserved in dutpases and dctp deaminases. Nucleic acids research, 24 12:2411-5, Jun 1996. URL: https://doi.org/10.1093/nar/24.12.2411, doi:10.1093/nar/24.12.2411. This article has 290 citations and is from a highest quality peer-reviewed journal.

4. (koonin1996pseudouridinesynthasesfour pages 3-5): E. V. Koonin. Pseudouridine synthases: four families of enzymes containing a putative uridine-binding motif also conserved in dutpases and dctp deaminases. Nucleic acids research, 24 12:2411-5, Jun 1996. URL: https://doi.org/10.1093/nar/24.12.2411, doi:10.1093/nar/24.12.2411. This article has 290 citations and is from a highest quality peer-reviewed journal.

5. (mcdonald2011thehandlingof pages 8-10): Marguerite K. McDonald, Edward J. Miracco, Junjun Chen, Yizhou Xie, and Eugene G. Mueller. The handling of the mechanistic probe 5-fluorouridine by the pseudouridine synthase trua and its consistency with the handling of the same probe by the pseudouridine synthases trub and rlua. Biochemistry, 50(3):426-436, Dec 2011. URL: https://doi.org/10.1021/bi101737z, doi:10.1021/bi101737z. This article has 29 citations and is from a peer-reviewed journal.

6. (mcdonald2011thehandlingof pages 10-11): Marguerite K. McDonald, Edward J. Miracco, Junjun Chen, Yizhou Xie, and Eugene G. Mueller. The handling of the mechanistic probe 5-fluorouridine by the pseudouridine synthase trua and its consistency with the handling of the same probe by the pseudouridine synthases trub and rlua. Biochemistry, 50(3):426-436, Dec 2011. URL: https://doi.org/10.1021/bi101737z, doi:10.1021/bi101737z. This article has 29 citations and is from a peer-reviewed journal.

7. (mcdonald2011thehandlingof pages 14-20): Marguerite K. McDonald, Edward J. Miracco, Junjun Chen, Yizhou Xie, and Eugene G. Mueller. The handling of the mechanistic probe 5-fluorouridine by the pseudouridine synthase trua and its consistency with the handling of the same probe by the pseudouridine synthases trub and rlua. Biochemistry, 50(3):426-436, Dec 2011. URL: https://doi.org/10.1021/bi101737z, doi:10.1021/bi101737z. This article has 29 citations and is from a peer-reviewed journal.

8. (koonin1996pseudouridinesynthasesfour pages 2-3): E. V. Koonin. Pseudouridine synthases: four families of enzymes containing a putative uridine-binding motif also conserved in dutpases and dctp deaminases. Nucleic acids research, 24 12:2411-5, Jun 1996. URL: https://doi.org/10.1093/nar/24.12.2411, doi:10.1093/nar/24.12.2411. This article has 290 citations and is from a highest quality peer-reviewed journal.

9. (wu2024trnamodificationsand pages 6-7): Di Wu, Xiuling Li, Faheem Ahmed Khan, Chenyang Yuan, Nuruliarizki Shinta Pandupuspitasari, Chunjie Huang, Fei Sun, and Kaifeng Guan. Trna modifications and trna-derived small rnas: new insights of trna in human disease. Cell Biology and Toxicology, Sep 2024. URL: https://doi.org/10.1007/s10565-024-09919-9, doi:10.1007/s10565-024-09919-9. This article has 23 citations and is from a peer-reviewed journal.

10. (atoi2023massspectrometricstudies pages 37-40): Paria Asadi Atoi. Mass spectrometric studies of rna modification patterns in mammals. ArXiv, 2023. URL: https://doi.org/10.21248/gups.74238, doi:10.21248/gups.74238. This article has 0 citations.

11. (malviya2026trub1mediatedpseudouridylationis pages 9-9): Vanshika Malviya, Cuong Thi Pham, Lauren Michiels, Laura Seldeslachts, Virginie Marchand, Gerlanda Vella, Laurie Rangan, Yuri Motorin, Greetje Vande Velde, Pierre Lemaitre, and Susan M. Schlenner. Trub1-mediated pseudouridylation is dispensable for immune cell development and homeostasis. Genes &amp; Immunity, 27(3):363-373, Mar 2026. URL: https://doi.org/10.1038/s41435-026-00393-3, doi:10.1038/s41435-026-00393-3. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](RluA-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. koonin1996pseudouridinesynthasesfour pages 1-2
2. koonin1996pseudouridinesynthasesfour pages 3-5
3. wu2024trnamodificationsand pages 6-7
4. atoi2023massspectrometricstudies pages 37-40
5. koonin1996pseudouridinesynthasesfour pages 2-3
6. aravind1999novelpredictedrnabinding pages 3-6
7. aravind1999novelpredictedrnabinding pages 2-3
8. mcdonald2011thehandlingof pages 8-10
9. mcdonald2011thehandlingof pages 10-11
10. mcdonald2011thehandlingof pages 14-20
11. https://doi.org/10.1021/acs.accounts.3c00450.
12. https://doi.org/10.1007/s10565-024-09919-9.
13. https://doi.org/10.1093/nar/24.12.2411
14. https://doi.org/10.1007/pl00006472
15. https://doi.org/10.1021/bi101737z
16. https://doi.org/10.1021/acs.accounts.3c00450
17. https://doi.org/10.1007/s10565-024-09919-9
18. https://doi.org/10.21248/gups.74238
19. https://doi.org/10.1007/pl00006472,
20. https://doi.org/10.1093/nar/24.12.2411,
21. https://doi.org/10.1021/bi101737z,
22. https://doi.org/10.1007/s10565-024-09919-9,
23. https://doi.org/10.21248/gups.74238,
24. https://doi.org/10.1038/s41435-026-00393-3,