---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T19:05:48.719156'
end_time: '2026-09-08T19:14:59.489359'
duration_seconds: 550.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: cem1
  gene_symbol: cem1
  uniprot_accession: O94297
  protein_description: 'RecName: Full=Putative 3-oxoacyl-[acyl-carrier-protein] synthase,
    mitochondrial {ECO:0000305}; EC=2.3.1.41 {ECO:0000250|UniProtKB:Q9NWU1}; AltName:
    Full=Beta-ketoacyl-ACP synthase; AltName: Full=mtKAS; Flags: Precursor;'
  gene_info: ORFNames=SPBC887.13c;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
  protein_domains: 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794);
    KAS_C. (IPR014031); KAS_N. (IPR014030); PKS_Beta-ketoAc_synthase_dom. (IPR020841)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: cem1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** O94297
- **Protein Description:** RecName: Full=Putative 3-oxoacyl-[acyl-carrier-protein] synthase, mitochondrial {ECO:0000305}; EC=2.3.1.41 {ECO:0000250|UniProtKB:Q9NWU1}; AltName: Full=Beta-ketoacyl-ACP synthase; AltName: Full=mtKAS; Flags: Precursor;
- **Gene Information:** ORFNames=SPBC887.13c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
- **Key Domains:** 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794); KAS_C. (IPR014031); KAS_N. (IPR014030); PKS_Beta-ketoAc_synthase_dom. (IPR020841)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cem1" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cem1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cem1** (gene ID: cem1, UniProt: O94297) in SCHPO.

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
- **UniProt Accession:** O94297
- **Protein Description:** RecName: Full=Putative 3-oxoacyl-[acyl-carrier-protein] synthase, mitochondrial {ECO:0000305}; EC=2.3.1.41 {ECO:0000250|UniProtKB:Q9NWU1}; AltName: Full=Beta-ketoacyl-ACP synthase; AltName: Full=mtKAS; Flags: Precursor;
- **Gene Information:** ORFNames=SPBC887.13c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
- **Key Domains:** 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794); KAS_C. (IPR014031); KAS_N. (IPR014030); PKS_Beta-ketoAc_synthase_dom. (IPR020841)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cem1" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cem1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cem1** (gene ID: cem1, UniProt: O94297) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Schizosaccharomyces pombe cem1* (O94297)

## Executive conclusion

The gene symbol **“cem1” is ambiguous and the literature is limited for this specific protein**. The target specified here is **UniProt O94297**, ORF **SPBC887.13c**, from ***Schizosaccharomyces pombe* strain 972 / ATCC 24843**—not the better-studied **CEM1** gene of budding yeast, *Saccharomyces cerevisiae*. Searches using the accession, ORF name, gene name, organism, and enzyme description found no publication directly demonstrating the localization, catalytic activity, substrate specificity, or mutant phenotype of O94297.

Accordingly, the strongest defensible annotation is that O94297 is a **predicted mitochondrial 3-oxoacyl–acyl-carrier-protein synthase**—also called beta-ketoacyl-ACP synthase or mtKAS—of the mitochondrial type-II fatty-acid-synthesis pathway (mtFAS). This interpretation rests on the supplied UniProt record, its predicted mitochondrial precursor status, and its KAS_N/KAS_C/beta-ketoacyl-synthase domains. It is strongly consistent with conserved yeast and mammalian mtFAS biology, but remains **orthology- and domain-based rather than experimentally established in *S. pombe***.

| Claim | Best-supported interpretation | Evidence tier | Confidence and caveat |
|---|---|---|---|
| Target identity | **cem1 / SPBC887.13c / UniProt O94297** denotes a putative mitochondrial 3-oxoacyl-ACP synthase (mtKAS; EC 2.3.1.41) in *Schizosaccharomyces pombe* strain 972. Its KAS_N, KAS_C, and beta-ketoacyl-synthase domains agree with that assignment. | Exact-target supplied UniProt annotation | **High for record identity; moderate for function.** The functional name is explicitly “putative,” and no publication directly indexed to O94297/SPBC887.13c was identified. |
| Mitochondrial-matrix localization | O94297 is predicted to be a mitochondrial precursor; mature Cem1 most likely acts in the matrix, where eukaryotic type-II mtFAS operates on soluble mitochondrial ACP. | Exact-target supplied UniProt annotation plus conserved pathway | **Moderate.** Compartment is biologically coherent, but no direct GFP, fractionation, import, or protease-protection experiment for the *S. pombe* protein was found (wedan2024mitochondrialfattyacid pages 1-2). |
| Primary KAS reaction | Cem1 is predicted to catalyze decarboxylative condensation of malonyl-ACP with an even-chain acyl-ACP: **acyl-ACP + malonyl-ACP → 3-oxoacyl-ACP extended by two carbons + CO₂ + ACP**. | Conserved pathway and yeast-ortholog assignment | **High for orthologous enzyme chemistry; moderate for O94297 specifically.** Cem1/OXSM occupies the KAS step in yeast/human mtFAS diagrams, but O94297 has not been biochemically assayed (wedan2024mitochondrialfattyacid pages 1-2, wedan2024mitochondrialfattyacid pages 16-21, rahman2023anengineeredvariant pages 2-3). |
| Substrate and chain-length preference | The physiological donor is malonyl-ACP, while the acceptor is a growing even-chain acyl-ACP. Yeast OXSM-ortholog studies indicate biphasic preference near C6 and C12 acceptors, favoring formation of C8 and C14 acyl-ACP; mtFAS can extend products toward C16. | Yeast ortholog and conserved pathway | **Moderate-to-low for *S. pombe*.** These chain-length preferences must not be treated as measured O94297 kinetics (wedan2024mitochondrialfattyacid pages 11-12, wedan2024mitochondrialfattyacid pages 16-21). |
| C8 lipoate branch | Cem1 is likely required upstream of octanoyl-ACP production. Octanoyl groups can leave mtFAS for conversion into lipoic acid and covalent lipoylation of mitochondrial dehydrogenase systems. | Conserved yeast-to-mammal pathway | **Moderate for pathway participation; untested for O94297.** mtFAS-derived C8 is established broadly, but no *S. pombe cem1* mutant lipoylation measurements were found (wedan2024mitochondrialfattyacid pages 1-2, wedan2024mitochondrialfattyacid pages 2-4). |
| C14–C16 respiratory branch | Continued mtFAS elongation yields longer acyl-ACPs implicated in ACP–LYRM interactions, respiratory-chain assembly, Fe–S-cluster biology, and respiratory competence. A 2023 engineered-enzyme study showed that restoring lipoylation without restoring long-chain acyl-ACP synthesis did not rescue yeast respiration. | Yeast ortholog experiment plus conserved pathway | **Moderate for a conserved mtFAS role; low-to-moderate for O94297 specifically.** The decisive 2023 experiment manipulated Etr1/MECR in *Saccharomyces cerevisiae*, not Cem1 in *S. pombe* (wedan2024mitochondrialfattyacid pages 6-7, rahman2023anengineeredvariant pages 2-3). |
| Direct *S. pombe* experimental support | No exact-target study located in the searched literature directly demonstrated O94297 localization, catalytic activity, substrate specificity, knockout phenotype, complementation, or pathway output. | Evidence-gap finding | **High confidence in the search limitation, not proof that no study exists.** Literature on **CEM1** chiefly concerns the distinct *S. cerevisiae* ortholog and must not be presented as direct *S. pombe* evidence (wedan2024mitochondrialfattyacid pages 16-21). |


*Table: Evidence-tier summary separating exact-target annotation for *S. pombe* O94297 from yeast-ortholog experiments and conserved mtFAS pathway inference. It highlights both the strongest functional interpretation and the major absence of direct biochemical or localization studies for this protein.*

## 1. Identity verification and domain consistency

The required identity checks support the following restricted interpretation:

- **Target:** O94297 / SPBC887.13c / cem1.
- **Organism:** ***Schizosaccharomyces pombe* strain 972**, fission yeast.
- **Supplied annotation:** putative mitochondrial 3-oxoacyl-[ACP] synthase, EC 2.3.1.41; precursor.
- **Family/domain match:** membership in the thiolase-like/beta-ketoacyl-ACP-synthase group and the presence of **KAS_N, KAS_C, beta-ketoacyl-synthase, and 3-oxoacyl-ACP-synthase-2** signatures are structurally consistent with an mtKAS enzyme.

The nomenclature nevertheless creates a serious species-confusion risk. The classic 1993 CEM1 study identified a nuclear gene encoding a beta-ketoacyl-synthase homolog required for mitochondrial respiration in ***S. cerevisiae***, not *S. pombe*. That result supports conserved ortholog function but is not direct evidence about O94297 (Harington et al., 1993, *Molecular Microbiology* 9:545–555; PubMed: https://pubmed.ncbi.nlm.nih.gov/8412701/) (wedan2024mitochondrialfattyacid pages 16-21).

## 2. Predicted primary biochemical function

### Catalyzed reaction

Cem1 is predicted to perform the carbon–carbon bond-forming step of mtFAS:

**even-chain acyl-ACP + malonyl-ACP → 3-oxoacyl-ACP extended by two carbons + ACP + CO₂**.

Malonyl-ACP is therefore the extender substrate, while the second substrate is a growing, even-numbered acyl chain attached by a thioester to mitochondrial ACP. Decarboxylation of malonyl-ACP drives condensation and increases the acyl chain by **two carbon atoms per cycle**. Downstream keto-reduction, dehydration, and enoyl reduction restore a saturated acyl-ACP for another elongation round (wedan2024mitochondrialfattyacid pages 1-2, wedan2024mitochondrialfattyacid pages 16-21).

This reaction is attributable to O94297 with **moderate confidence**, because it is the defining chemistry of proteins assigned to EC 2.3.1.41 and fits the supplied domains. No purified-O94297 kinetic assay, active-site mutagenesis, or metabolite-tracing experiment was found.

### Substrate specificity

The most conservative substrate annotation is **malonyl-ACP plus an even-chain acyl-ACP**, rather than free fatty acid, acyl-CoA, or bulk membrane lipid. mtFAS products generally remain covalently attached to ACP; no dedicated mtFAS thioesterase has been established (wedan2024mitochondrialfattyacid pages 6-7, wedan2024mitochondrialfattyacid pages 11-12).

A recent authoritative review reports that in-vitro work on a **yeast OXSM ortholog** showed biphasic preference around **C6 and C12 acceptor chains**, most readily generating **octanoyl-ACP (C8)** and **myristoyl-ACP (C14)**. Conserved mtFAS can also generate palmitoyl-ACP (C16) (wedan2024mitochondrialfattyacid pages 11-12, wedan2024mitochondrialfattyacid pages 16-21). These chain-length preferences must be treated as an experimentally testable hypothesis for *S. pombe* Cem1, not as measured O94297 kinetics.

## 3. Cellular localization

The supplied UniProt designation “mitochondrial” and “precursor” implies nuclear synthesis followed by mitochondrial import and removal of an N-terminal targeting peptide. The mature enzyme is most likely located in the **mitochondrial matrix**, because eukaryotic mtFAS is a soluble matrix pathway that elongates acyl chains on mitochondrial ACP (wedan2024mitochondrialfattyacid pages 1-2).

Confidence is moderate rather than high: no O94297-specific fluorescence microscopy, biochemical fractionation, mitochondrial import, or protease-protection experiment was identified. Localization should therefore be recorded as **predicted mitochondrial matrix**, not experimentally verified.

## 4. Pathway and biological-process roles

### Mitochondrial type-II fatty-acid synthesis

mtFAS is evolutionarily related to bacterial type-II FAS: its reactions are performed by separate proteins rather than domains of one large cytosolic fatty-acid synthase. ACP is first phosphopantetheinylated, receives malonate from malonyl-CoA, and then undergoes Cem1/OXSM-catalyzed condensation. A complete elongation cycle uses **two NADPH molecules** in the downstream reduction steps, although Cem1 itself is not an NADPH-dependent enzyme (wedan2024mitochondrialfattyacid pages 1-2).

O94297 is therefore predicted to be a core biosynthetic enzyme rather than a transporter, receptor, structural adapter, or conventional signaling protein.

### Octanoyl-ACP, lipoic acid, and central metabolism

One major mtFAS output is **C8 octanoyl-ACP**, the precursor used by the mitochondrial lipoic-acid pathway. In the conserved pathway, octanoate is transferred from ACP to a carrier protein and converted to lipoate, which is subsequently attached covalently to mitochondrial enzyme complexes. Lipoylation supports pyruvate dehydrogenase, 2-oxoglutarate dehydrogenase and, depending on the organism, additional oxidative decarboxylation or glycine-cleavage systems. This links mtFAS to acetyl-CoA production, TCA-cycle flux, amino-acid catabolism, and respiration (wedan2024mitochondrialfattyacid pages 1-2, wedan2024mitochondrialfattyacid pages 2-4).

Thus, *S. pombe* Cem1 is likely required upstream of mitochondrial protein lipoylation. However, no *S. pombe cem1* deletion study measuring lipoate, lipoylated proteins, or enzyme activity was found.

### Longer acyl-ACP products and respiration

Current understanding no longer treats lipoate as the sole biologically important mtFAS product. Longer **C14–C16 acyl-ACPs** promote interactions between mitochondrial ACP and LYRM-family proteins involved in electron-transport-chain assembly and iron–sulfur-cluster biology. Acyl-ACP-dependent effects on mitochondrial translation have also been reported, although some mechanisms remain unresolved (wedan2024mitochondrialfattyacid pages 6-7, wedan2024mitochondrialfattyacid pages 7-9, wedan2024mitochondrialfattyacid pages 16-21).

This provides a mechanistic explanation for the older observation that *S. cerevisiae* CEM1 is required for mitochondrial respiration: loss of mtKAS would be expected to compromise both the C8/lipoate branch and longer-chain acyl-ACP functions. The precise balance between these outputs, however, remains unknown even in well-studied systems (wedan2024mitochondrialfattyacid pages 16-21, wedan2024mitochondrialfattyacid pages 11-12).

## 5. Recent developments, 2023–2024

### Long-chain products are independently required for respiratory competence

Rahman et al. engineered human MECR—the terminal reductase of mtFAS—to support short-chain/octanoyl production while restricting long-chain synthesis, and tested it in an ***S. cerevisiae* Δetr1** model. The engineered variant restored protein lipoylation but did **not** restore respiratory competence, whereas wild-type MECR did. This experimentally separates the C8/lipoylation output from a second requirement for long-chain acyl-ACP products in respiration (published February 2023, *Nature Communications* 14:619; https://doi.org/10.1038/s41467-023-36358-7) (rahman2023anengineeredvariant pages 2-3).

Although this study did not manipulate Cem1 or *S. pombe*, it materially changes interpretation of a predicted mtKAS: Cem1 likely supports mitochondrial function not merely by supplying lipoate precursor but also by enabling synthesis of longer ACP-bound chains.

### mtFAS as an organizer of oxidative metabolism

A January 2, 2024 *Cell Metabolism* review characterizes mtFAS as an evolutionarily conserved regulator connecting carbon availability to protein lipoylation, respiratory-chain assembly, Fe–S-cluster formation, and possibly mitochondrial translation. It emphasizes that the molecular identities, proportions, regulation, and ultimate destinations of several long-chain products remain open questions (Wedan, Longenecker & Nowinski, 2024, 36:36–47; https://doi.org/10.1016/j.cmet.2023.11.017) (wedan2024mitochondrialfattyacid pages 11-12, wedan2024mitochondrialfattyacid pages 1-2, wedan2024mitochondrialfattyacid pages 16-21).

The review also notes that mtFAS does **not appear to provide a quantitatively important source for bulk phospholipid or triglyceride stores**. Proposed effects on specialized lipids, including cardiolipin or sphingolipid species, remain unresolved and may be secondary to altered oxidative metabolism (wedan2024mitochondrialfattyacid pages 11-12).

## 6. Applications and real-world implementation

There is no identified industrial, clinical, or established biotechnological application specifically involving ***S. pombe cem1/O94297***. Its immediate applications are research-oriented:

1. **Functional complementation:** yeast respiratory mutants can test whether heterologous mtFAS enzymes restore pathway function. Human OXSM was previously characterized partly through complementation of a yeast CEM1 knockout, illustrating the utility of yeast as a cross-species functional assay (Zhang et al., 2005, *Journal of Biological Chemistry* 280:12422–12429; https://doi.org/10.1074/jbc.M413686200) (wedan2024mitochondrialfattyacid pages 11-12).
2. **Dissecting mtFAS outputs:** engineered chain-length restrictions can distinguish requirements for octanoyl/lipoyl synthesis from long-chain acyl-ACP-dependent respiration (rahman2023anengineeredvariant pages 2-3).
3. **Mitochondrial-disease modeling and target discovery:** pathogenic human mtFAS variants have renewed interest in the pathway, but extrapolation to O94297 should remain pathway-level. Lipoate supplementation is not expected to substitute straightforwardly for endogenous protein lipoylation because cells lack an effective route to attach supplied free lipoate to the relevant proteins (wedan2024mitochondrialfattyacid pages 2-4).

A targeted *S. pombe* program could exploit the organism’s genetics to examine respiratory growth, protein lipoylation, ACP acyl-chain profiles, mitochondrial translation, and Fe–S-dependent phenotypes after cem1 deletion or catalytic-site mutation.

## 7. Quantitative findings relevant to annotation

- Cem1/OXSM chemistry adds **2 carbons** and releases **1 CO₂** per condensation (wedan2024mitochondrialfattyacid pages 1-2, wedan2024mitochondrialfattyacid pages 16-21).
- A full mtFAS elongation cycle consumes **2 NADPH** in downstream reductive reactions, not in the Cem1 condensation itself (wedan2024mitochondrialfattyacid pages 1-2).
- Major proposed output classes are **C8 octanoyl-ACP** and longer **C14–C16 acyl-ACPs** (wedan2024mitochondrialfattyacid pages 11-12, wedan2024mitochondrialfattyacid pages 16-21).
- Yeast-ortholog biochemical evidence suggests favored acceptor-chain regions near **C6 and C12**, leading most readily to C8 and C14 products; this has not been measured for O94297 (wedan2024mitochondrialfattyacid pages 11-12).
- In the 2023 engineered-enzyme study, restoration of lipoylation without long-chain-product synthesis was insufficient to rescue respiratory growth, demonstrating qualitatively distinct mtFAS outputs rather than one interchangeable product pool (rahman2023anengineeredvariant pages 2-3).

No O94297-specific kinetic constants, protein abundance, expression fold changes, growth rates, or deletion-effect sizes were located.

## 8. Evidence assessment and recommended annotation

### Recommended concise functional annotation

**Cem1 (O94297/SPBC887.13c) is a predicted mitochondrial-matrix beta-ketoacyl-ACP synthase of type-II mitochondrial fatty-acid synthesis. It likely catalyzes decarboxylative condensation of malonyl-ACP with a growing even-chain acyl-ACP, extending the chain by two carbons. Its products are expected to support both octanoyl-ACP/lipoic-acid synthesis and formation of longer acyl-ACPs required for respiratory mitochondrial organization.**

### Confidence by claim

- **Identity and organism:** high, based on the supplied UniProt accession and ORF.
- **KAS family and reaction class:** moderate-to-high, based on domain/family conservation and ortholog chemistry.
- **Mitochondrial-matrix localization:** moderate, predicted but not directly demonstrated for O94297.
- **Specific C6/C12 preference:** low-to-moderate, inferred from a yeast ortholog rather than measured in *S. pombe*.
- **Roles in lipoylation and respiration:** moderate as conserved-pathway inference; direct *S. pombe cem1* evidence is absent.
- **Any exact mutant phenotype:** undetermined.

## Final interpretation

The protein family and domains align well with the supplied mtKAS description, and the best current model places Cem1 at the central condensation step of mitochondrial type-II fatty-acid synthesis. Nevertheless, the exact-target literature gap is decisive: findings for ***S. cerevisiae* CEM1**, human **OXSM**, or other mtFAS enzymes must not be reported as experiments on ***S. pombe* O94297**. Direct validation would require mitochondrial localization, recombinant-enzyme assays against defined acyl-ACP chain lengths, and genetic measurements of lipoylation and respiratory competence in *S. pombe*.

References

1. (wedan2024mitochondrialfattyacid pages 1-2): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 99 citations and is from a highest quality peer-reviewed journal.

2. (wedan2024mitochondrialfattyacid pages 16-21): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 99 citations and is from a highest quality peer-reviewed journal.

3. (rahman2023anengineeredvariant pages 2-3): M. Tanvir Rahman, M. Kristian Koski, Joanna Panecka-Hofman, Werner Schmitz, Alexander J. Kastaniotis, Rebecca C. Wade, Rik K. Wierenga, J. Kalervo Hiltunen, and Kaija J. Autio. An engineered variant of mecr reductase reveals indispensability of long-chain acyl-acps for mitochondrial respiration. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36358-7, doi:10.1038/s41467-023-36358-7. This article has 17 citations and is from a highest quality peer-reviewed journal.

4. (wedan2024mitochondrialfattyacid pages 11-12): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 99 citations and is from a highest quality peer-reviewed journal.

5. (wedan2024mitochondrialfattyacid pages 2-4): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 99 citations and is from a highest quality peer-reviewed journal.

6. (wedan2024mitochondrialfattyacid pages 6-7): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 99 citations and is from a highest quality peer-reviewed journal.

7. (wedan2024mitochondrialfattyacid pages 7-9): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 99 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](cem1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. wedan2024mitochondrialfattyacid pages 1-2
2. wedan2024mitochondrialfattyacid pages 16-21
3. rahman2023anengineeredvariant pages 2-3
4. wedan2024mitochondrialfattyacid pages 11-12
5. wedan2024mitochondrialfattyacid pages 2-4
6. wedan2024mitochondrialfattyacid pages 6-7
7. wedan2024mitochondrialfattyacid pages 7-9
8. acyl-carrier-protein
9. ACP
10. https://pubmed.ncbi.nlm.nih.gov/8412701/
11. https://doi.org/10.1038/s41467-023-36358-7
12. https://doi.org/10.1016/j.cmet.2023.11.017
13. https://doi.org/10.1074/jbc.M413686200
14. https://doi.org/10.1016/j.cmet.2023.11.017,
15. https://doi.org/10.1038/s41467-023-36358-7,