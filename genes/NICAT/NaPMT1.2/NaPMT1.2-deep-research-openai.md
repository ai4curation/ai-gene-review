---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:09:42.699256'
end_time: '2026-04-05T13:09:53.918150'
duration_seconds: 11.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: Q93XQ4
  gene_symbol: NaPMT1.2
  uniprot_accession: Q93XQ4
  protein_description: Putrescine N-methyltransferase 2 ;
  gene_info: Name=PMT2 ; ORFNames=A4A49_05615 ;
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
citation_count: 3
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q93XQ4
- **Protein Description:** Putrescine N-methyltransferase 2 ;
- **Gene Information:** Name=PMT2 ; ORFNames=A4A49_05615 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** PABS. (IPR030374);  PABS_CS. (IPR030373);  Putrescine_N-MeTfrase. (IPR025803);  SAM-dependent_MTases_sf. (IPR029063);  Spermi_synthase. (IPR001045)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaPMT1.2" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaPMT1.2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaPMT1.2** (gene ID: Q93XQ4, UniProt: Q93XQ4) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

The gene **NaPMT1.2** in *Nicotiana attenuata* encodes the enzyme putrescine N-methyltransferase 2 (PMT2), a pivotal catalyst in the biosynthesis of nicotine alkaloids. This enzyme facilitates the methylation of putrescine, a polyamine, to produce N-methylputrescine, marking the initial committed step in nicotine synthesis.

**Enzymatic Function and Substrate Specificity**

PMT2 operates by transferring a methyl group from S-adenosyl-L-methionine (SAM) to putrescine, yielding N-methylputrescine and S-adenosyl-L-homocysteine. This reaction is crucial as it channels putrescine into the alkaloid biosynthetic pathway, leading to the formation of nicotine and related compounds. The enzyme's specificity for putrescine underscores its role in directing polyamine metabolism toward alkaloid production.

**Biological Processes and Localization**

The expression of NaPMT1.2 is predominantly localized in the roots of *N. attenuata*, aligning with the root-specific synthesis of nicotine. Transcriptomic analyses have demonstrated that NaPMT1.2, along with other nicotine biosynthetic genes, exhibits high expression levels in root tissues, while being minimally expressed in leaves, flowers, and stems. This root-specific expression pattern is consistent with the localization of nicotine biosynthesis in the plant. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12361153/?utm_source=openai))

**Regulation and Induction**

The expression of NaPMT1.2 is inducible by jasmonate signaling, a plant hormone pathway activated in response to herbivory and other stressors. Studies in related Nicotiana species have shown that jasmonate treatment upregulates PMT gene expression in roots, suggesting a conserved regulatory mechanism. This induction aligns with the plant's defense strategy, as increased nicotine production can deter herbivores. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/10965939/?utm_source=openai))

**Evolutionary Context**

PMT enzymes, including PMT2, are believed to have evolved from spermidine synthases, enzymes involved in polyamine biosynthesis. This evolutionary transition reflects a functional shift from general polyamine metabolism to specialized secondary metabolism, enabling the production of defensive alkaloids like nicotine. The structural and functional similarities between PMTs and spermidine synthases support this evolutionary relationship. ([frontiersin.org](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2013.00260/full?utm_source=openai))

**Pathway Integration**

Within the nicotine biosynthetic pathway, PMT2's activity is a critical control point. Following the formation of N-methylputrescine by PMT2, subsequent enzymatic steps lead to the production of nicotine. The regulation of PMT2, therefore, directly influences the flux through the pathway and the overall production of nicotine, highlighting its importance in the plant's chemical defense arsenal.

In summary, NaPMT1.2 encodes the enzyme PMT2, which catalyzes the methylation of putrescine to N-methylputrescine, initiating the nicotine biosynthetic pathway in *Nicotiana attenuata*. Its root-specific expression and inducibility by jasmonate signaling underscore its role in the plant's adaptive response to herbivory. The evolutionary derivation from spermidine synthases illustrates a functional adaptation toward specialized metabolism, emphasizing the enzyme's significance in plant defense mechanisms. 