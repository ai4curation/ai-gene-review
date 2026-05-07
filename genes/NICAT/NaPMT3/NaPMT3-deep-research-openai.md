---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:09:56.052013'
end_time: '2026-04-05T13:10:12.615259'
duration_seconds: 16.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: A0A314LG79
  gene_symbol: NaPMT3
  uniprot_accession: A0A314LG79
  protein_description: Putrescine N-methyltransferase 3 ;
  gene_info: Name=PMT3 ; ORFNames=A4A49_61142 ;
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
- **UniProt Accession:** A0A314LG79
- **Protein Description:** Putrescine N-methyltransferase 3 ;
- **Gene Information:** Name=PMT3 ; ORFNames=A4A49_61142 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the class I-like SAM-binding methyltransferase
- **Key Domains:** PABS. (IPR030374);  PABS_CS. (IPR030373);  Putrescine_N-MeTfrase. (IPR025803);  SAM-dependent_MTases_sf. (IPR029063);  Spermi_synthase. (IPR001045)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaPMT3" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaPMT3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaPMT3** (gene ID: A0A314LG79, UniProt: A0A314LG79) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

The gene **NaPMT3** in *Nicotiana attenuata* encodes putrescine N-methyltransferase 3 (PMT3), an enzyme integral to the biosynthesis of nicotine, a predominant alkaloid in tobacco species. PMT3 catalyzes the methylation of putrescine to N-methylputrescine, marking the first committed step in nicotine synthesis.

**Function and Catalytic Activity**

PMT3 facilitates the transfer of a methyl group from S-adenosyl-L-methionine (SAM) to putrescine, producing N-methylputrescine and S-adenosyl-L-homocysteine. This reaction is pivotal in directing putrescine towards alkaloid biosynthesis rather than polyamine synthesis. The enzyme's activity is characterized by the following reaction:

\[ \text{S-adenosyl-L-methionine} + \text{putrescine} \rightarrow \text{S-adenosyl-L-homocysteine} + \text{N-methylputrescine} \]

This enzymatic function is essential for the production of nicotine, as N-methylputrescine serves as a precursor in the subsequent steps of the nicotine biosynthetic pathway.

**Biological Processes and Pathways**

PMT3 operates within the nicotine biosynthesis pathway, primarily localized in the roots of *Nicotiana attenuata*. The pathway involves:

1. **Putrescine Formation**: Derived from ornithine via ornithine decarboxylase or from arginine via arginine decarboxylase.

2. **Methylation by PMT3**: Converts putrescine to N-methylputrescine.

3. **Oxidation to N-methyl-Δ¹-pyrrolinium Cation**: N-methylputrescine is oxidized by N-methylputrescine oxidase (MPO).

4. **Condensation with Nicotinic Acid**: Forms nicotine through a series of enzymatic reactions.

The expression of PMT genes, including PMT3, is upregulated by jasmonate signaling, particularly in response to herbivore attack or mechanical wounding. This regulation underscores the role of PMT3 in plant defense mechanisms. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/10965939/?utm_source=openai))

**Localization**

PMT3 is predominantly expressed in the root tissues of *Nicotiana attenuata*. Within the roots, its expression is localized to the cortex, endodermis, and xylem. This spatial distribution aligns with the site of nicotine biosynthesis, as nicotine is synthesized in the roots and subsequently transported to aerial parts of the plant. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/10965939/?utm_source=openai))

**Regulation and Expression**

The expression of PMT3 is inducible by methyl jasmonate, a plant hormone associated with stress responses. Studies in related species, such as *Nicotiana sylvestris*, have demonstrated that the 5'-flanking regions of PMT genes contain elements responsive to jasmonate, facilitating the upregulation of these genes upon exposure to the hormone. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/10965939/?utm_source=openai))

**Structural and Evolutionary Considerations**

PMT3 belongs to the class I-like S-adenosylmethionine-dependent methyltransferase family. It contains key domains characteristic of this family, including the PABS domain (IPR030374), which is involved in binding S-adenosylmethionine, and the Putrescine N-methyltransferase domain (IPR025803), essential for its catalytic activity. Evolutionarily, PMT enzymes are believed to have diverged from spermidine synthases, adapting to fulfill specialized roles in alkaloid biosynthesis. ([en.wikipedia.org](https://en.wikipedia.org/wiki/Putrescine_N-methyltransferase?utm_source=openai))

**Conclusion**

NaPMT3 in *Nicotiana attenuata* encodes an enzyme crucial for the initial step in nicotine biosynthesis, catalyzing the methylation of putrescine to N-methylputrescine. Its expression is root-specific and regulated by jasmonate signaling, highlighting its role in the plant's defense response. The enzyme's activity and regulation are integral to understanding nicotine production in tobacco species. 