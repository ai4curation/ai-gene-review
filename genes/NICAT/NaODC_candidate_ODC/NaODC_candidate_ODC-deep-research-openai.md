---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:08:39.863699'
end_time: '2026-04-05T13:08:51.672203'
duration_seconds: 11.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: A0A314KUM9
  gene_symbol: NaODC_candidate_ODC
  uniprot_accession: A0A314KUM9
  protein_description: ornithine decarboxylase ;
  gene_info: Name=ODC ; ORFNames=A4A49_34686 ;
  organism_full: Nicotiana attenuata (Coyote tobacco).
  protein_family: Belongs to the Orn/Lys/Arg decarboxylase class-II family.
  protein_domains: Ala_racemase/Decarboxylase_C. (IPR009006);  De-COase2_N. (IPR022644);  De-COase2_pyr-phos_BS.
    (IPR022653);  Orn/DAP/Arg_de-COase. (IPR000183);  Orn_de-COase. (IPR002433)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    top_p: 1.0
citation_count: 3
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A314KUM9
- **Protein Description:** ornithine decarboxylase ;
- **Gene Information:** Name=ODC ; ORFNames=A4A49_34686 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the Orn/Lys/Arg decarboxylase class-II family.
- **Key Domains:** Ala_racemase/Decarboxylase_C. (IPR009006);  De-COase2_N. (IPR022644);  De-COase2_pyr-phos_BS. (IPR022653);  Orn/DAP/Arg_de-COase. (IPR000183);  Orn_de-COase. (IPR002433)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaODC_candidate_ODC" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaODC_candidate_ODC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaODC_candidate_ODC** (gene ID: A0A314KUM9, UniProt: A0A314KUM9) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Ornithine decarboxylase (ODC) is a pivotal enzyme in the biosynthesis of polyamines, catalyzing the decarboxylation of L-ornithine to produce putrescine. This reaction represents the initial and rate-limiting step in the synthesis of polyamines such as spermidine and spermine, which are essential for various cellular processes, including DNA stabilization, cell growth, and differentiation.

**Function and Enzymatic Activity**

In Nicotiana attenuata (coyote tobacco), ODC plays a crucial role in the production of putrescine, a precursor not only for polyamines but also for alkaloids like nicotine. The enzyme's activity is dependent on the cofactor pyridoxal-5'-phosphate (PLP), which facilitates the decarboxylation process. The reaction can be summarized as follows:

\[ \text{L-ornithine} \xrightarrow{\text{ODC}} \text{Putrescine} + \text{CO}_2 \]

This enzymatic function is critical for the plant's secondary metabolism, particularly in the synthesis of defensive compounds such as nicotine.

**Biological Processes and Localization**

ODC is predominantly expressed in the roots of Nicotiana attenuata, aligning with the root-specific biosynthesis of nicotine. Transcriptome analyses have revealed that genes involved in nicotine biosynthesis, including ODC, exhibit high expression levels in root tissues compared to leaves. This root-specific expression pattern underscores the enzyme's role in the localized production of alkaloids, which are then transported to aerial parts of the plant to deter herbivory. ([frontiersin.org](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1647622/full?utm_source=openai))

**Pathways and Metabolic Integration**

ODC's activity integrates into the broader polyamine biosynthetic pathway, influencing both primary and secondary metabolism. The putrescine produced by ODC serves as a substrate for the synthesis of spermidine and spermine, polyamines that are vital for cellular functions. Additionally, putrescine is a precursor for nicotine biosynthesis in Nicotiana species. Studies in Nicotiana tabacum have demonstrated that down-regulation of ODC leads to decreased levels of nicotine and nornicotine, accompanied by increased levels of anatabine. This alteration suggests that ODC activity directly affects the flux through the nicotine biosynthetic pathway. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/27126795/?utm_source=openai))

**Structural Insights and Evolutionary Considerations**

ODC belongs to the Orn/Lys/Arg decarboxylase class-II family, characterized by specific structural domains:

- **Ala_racemase/Decarboxylase_C (IPR009006):** This domain is involved in the catalytic activity of the enzyme.

- **De-COase2_N (IPR022644):** This N-terminal domain contributes to the enzyme's structural stability.

- **De-COase2_pyr-phos_BS (IPR022653):** This domain is associated with the binding of the pyridoxal-5'-phosphate cofactor.

- **Orn/DAP/Arg_de-COase (IPR000183):** This domain is common among decarboxylases acting on ornithine, diaminopimelate, and arginine.

- **Orn_de-COase (IPR002433):** This domain is specific to ornithine decarboxylases.

These domains collectively facilitate the enzyme's function and stability. Comparative studies have shown that plant ODCs, such as those from Nicotiana glutinosa, share significant sequence identity with ODCs from other plant species, indicating a conserved evolutionary role in polyamine and alkaloid biosynthesis. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/11736657/?utm_source=openai))

**Conclusion**

In Nicotiana attenuata, ornithine decarboxylase is integral to the biosynthesis of polyamines and alkaloids, particularly nicotine. Its root-specific expression aligns with the localized production of these compounds, which are essential for the plant's defense mechanisms. The enzyme's activity, structural domains, and evolutionary conservation underscore its critical role in plant metabolism and adaptation. 