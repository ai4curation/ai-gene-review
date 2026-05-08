---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:09:13.544740'
end_time: '2026-04-05T13:09:40.273869'
duration_seconds: 26.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: Q93XQ5
  gene_symbol: NaPMT1.1
  uniprot_accession: Q93XQ5
  protein_description: Putrescine N-methyltransferase 1 ;
  gene_info: Name=PMT1 ;
  organism_full: Nicotiana attenuata (Coyote tobacco).
  protein_family: Belongs to the class I-like SAM-binding methyltransferase
  protein_domains: PABS. (IPR030374);  PABS_CS. (IPR030373);  Putrescine_N-MeTfrase.
    (IPR025803);  SAM-dependent_MTases_sf. (IPR029063);  Spermi_synthase. (IPR001045)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    top_p: 1.0
citation_count: 4
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q93XQ5
- **Protein Description:** Putrescine N-methyltransferase 1 ;
- **Gene Information:** Name=PMT1 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** PABS. (IPR030374);  PABS_CS. (IPR030373);  Putrescine_N-MeTfrase. (IPR025803);  SAM-dependent_MTases_sf. (IPR029063);  Spermi_synthase. (IPR001045)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaPMT1.1" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaPMT1.1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaPMT1.1** (gene ID: Q93XQ5, UniProt: Q93XQ5) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Putrescine N-methyltransferase 1 (PMT1), encoded by the gene **NaPMT1.1** in *Nicotiana attenuata* (coyote tobacco), is a pivotal enzyme in the biosynthesis of nicotine and related alkaloids. This enzyme catalyzes the methylation of putrescine, a polyamine, to form N-methylputrescine, marking the first committed step in the nicotine biosynthetic pathway.

**Enzymatic Function and Substrate Specificity**

PMT1 functions as a methyltransferase, transferring a methyl group from S-adenosyl-L-methionine (SAM) to putrescine, resulting in the production of N-methylputrescine and S-adenosyl-L-homocysteine. This reaction is crucial as it diverts putrescine from polyamine metabolism towards alkaloid biosynthesis. The enzyme's specificity for putrescine over other polyamines underscores its specialized role in this pathway.

**Biological Processes and Localization**

The expression of NaPMT1.1 is predominantly localized in the roots of *N. attenuata*, aligning with the root-specific synthesis of nicotine in this species. Transcriptome analyses have demonstrated that NaPMT1.1, along with other nicotine biosynthetic genes, is highly expressed in root tissues, while its expression in leaves is minimal. This root-specific expression pattern is consistent with findings in other Nicotiana species, where PMT genes are similarly upregulated in roots in response to jasmonate signaling, a plant hormone associated with stress responses and secondary metabolite production. ([frontiersin.org](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1647622/full?utm_source=openai))

**Regulation and Pathway Involvement**

The activity of NaPMT1.1 is tightly regulated within the nicotine biosynthetic pathway. In *N. attenuata*, a DNA methylation valley—a region of reduced DNA methylation—has been identified in the promoter regions of nicotine-related genes, including NaPMT1.1. This hypomethylation is associated with the root-specific expression of these genes, suggesting an epigenetic mechanism controlling their transcription. ([frontiersin.org](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1647622/full?utm_source=openai))

Furthermore, the expression of PMT genes in Nicotiana species is inducible by jasmonate treatment, indicating that NaPMT1.1 is part of a jasmonate-responsive regulatory network that modulates nicotine biosynthesis in response to environmental cues. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/10965939/?utm_source=openai))

**Structural Insights and Evolutionary Context**

Structurally, PMT1 belongs to the class I-like S-adenosylmethionine-dependent methyltransferase family, characterized by specific domains such as the PABS domain (IPR030374) and the SAM-dependent methyltransferase superfamily domain (IPR029063). These domains are integral to the enzyme's function in methyl group transfer. Evolutionary analyses suggest that PMT1 evolved from spermidine synthase, reflecting a functional divergence that enabled the specialized role of PMT1 in alkaloid biosynthesis. ([en.wikipedia.org](https://en.wikipedia.org/wiki/Putrescine_N-methyltransferase?utm_source=openai))

**Conclusion**

NaPMT1.1 encodes putrescine N-methyltransferase 1, a root-localized enzyme essential for the initiation of nicotine biosynthesis in *Nicotiana attenuata*. Its activity is regulated by both epigenetic modifications and jasmonate signaling, highlighting its role in the plant's adaptive responses. Understanding the function and regulation of NaPMT1.1 provides valuable insights into the metabolic pathways that contribute to the production of bioactive alkaloids in Nicotiana species. 