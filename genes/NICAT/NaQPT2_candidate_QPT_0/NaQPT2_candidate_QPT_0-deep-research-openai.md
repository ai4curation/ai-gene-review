---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:08:08.675801'
end_time: '2026-04-05T13:08:19.949467'
duration_seconds: 11.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: A0A1J6KEF3
  gene_symbol: NaQPT2_candidate_QPT_0
  uniprot_accession: A0A1J6KEF3
  protein_description: nicotinate-nucleotide diphosphorylase (carboxylating) ;
  gene_info: Name=QPT_0 ; ORFNames=A4A49_25254 ;
  organism_full: Nicotiana attenuata (Coyote tobacco).
  protein_family: Belongs to the NadC/ModD family.
  protein_domains: Aldolase_TIM. (IPR013785);  NadC. (IPR004393);  NadC/ModD. (IPR027277);  Nicotinate_pribotase-like_C.
    (IPR036068);  Quinolinate_PRibosylTase_N_sf. (IPR037128)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    top_p: 1.0
citation_count: 2
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A1J6KEF3
- **Protein Description:** nicotinate-nucleotide diphosphorylase (carboxylating) ;
- **Gene Information:** Name=QPT_0 ; ORFNames=A4A49_25254 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the NadC/ModD family.
- **Key Domains:** Aldolase_TIM. (IPR013785);  NadC. (IPR004393);  NadC/ModD. (IPR027277);  Nicotinate_pribotase-like_C. (IPR036068);  Quinolinate_PRibosylTase_N_sf. (IPR037128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaQPT2_candidate_QPT_0" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaQPT2_candidate_QPT_0' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaQPT2_candidate_QPT_0** (gene ID: A0A1J6KEF3, UniProt: A0A1J6KEF3) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

The gene **NaQPT2_candidate_QPT_0** in *Nicotiana attenuata* encodes the enzyme nicotinate-nucleotide diphosphorylase (carboxylating), also known as quinolinate phosphoribosyltransferase (QAPRTase). This enzyme plays a pivotal role in the biosynthesis of nicotinamide adenine dinucleotide (NAD⁺), a crucial coenzyme in cellular metabolism.

**Enzymatic Function and Reaction Mechanism**

Nicotinate-nucleotide diphosphorylase (carboxylating) catalyzes the conversion of quinolinic acid (QA) into nicotinate mononucleotide (NaMN), a key intermediate in the NAD⁺ biosynthetic pathway. The reaction proceeds as follows:

\[ \text{Quinolinic acid} + \text{5-phosphoribosyl-1-pyrophosphate (PRPP)} \rightarrow \text{NaMN} + \text{pyrophosphate} + \text{CO}_2 \]

This decarboxylation reaction is essential for the de novo synthesis of NAD⁺, facilitating the transfer of a phosphoribosyl group to quinolinic acid, resulting in the formation of NaMN. The enzyme's activity is classified under EC 2.4.2.19. ([ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/mesh/2108126?utm_source=openai))

**Biological Significance**

NAD⁺ is indispensable for various metabolic processes, including redox reactions, DNA repair, and signaling pathways. In plants, NAD⁺ biosynthesis is crucial for energy metabolism and stress responses. The activity of nicotinate-nucleotide diphosphorylase (carboxylating) ensures a steady supply of NAD⁺, thereby supporting these vital functions.

**Protein Family and Structural Domains**

The enzyme belongs to the NadC/ModD family, characterized by specific structural domains:

- **Aldolase_TIM (IPR013785):** A domain associated with the TIM barrel fold, common in enzymes facilitating various catalytic activities.

- **NadC (IPR004393):** A domain specific to nicotinate-nucleotide diphosphorylases, indicating its role in NAD⁺ biosynthesis.

- **Nicotinate_pribotase-like_C (IPR036068):** A domain suggesting structural similarity to other phosphoribosyltransferases.

These domains collectively contribute to the enzyme's function in catalyzing the conversion of quinolinic acid to NaMN.

**Subcellular Localization**

While specific localization studies for *Nicotiana attenuata* are limited, nicotinate-nucleotide diphosphorylase (carboxylating) is generally localized in the cytoplasm, where NAD⁺ biosynthesis predominantly occurs. This cytoplasmic presence aligns with the enzyme's role in central metabolic pathways.

**Pathway Integration**

The enzyme is integral to the de novo NAD⁺ biosynthesis pathway. In plants, this pathway involves the conversion of aspartate to quinolinic acid, which is then transformed into NaMN by nicotinate-nucleotide diphosphorylase (carboxylating). Subsequent enzymatic steps lead to the formation of NAD⁺. This pathway is essential for maintaining cellular NAD⁺ levels, especially under conditions where salvage pathways are insufficient.

**Inference from Homologous Proteins**

Although direct studies on *Nicotiana attenuata*'s nicotinate-nucleotide diphosphorylase (carboxylating) are scarce, research on homologous enzymes in other organisms provides valuable insights. For instance, in *Pyrococcus horikoshii*, the nadC gene encodes a similar enzyme involved in NAD⁺ biosynthesis, highlighting the conserved nature of this pathway across species. ([ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/gene/1443913?utm_source=openai))

**Conclusion**

The nicotinate-nucleotide diphosphorylase (carboxylating) encoded by the **NaQPT2_candidate_QPT_0** gene in *Nicotiana attenuata* is a crucial enzyme in the de novo NAD⁺ biosynthesis pathway. Its activity ensures the production of NAD⁺, supporting essential metabolic processes and stress responses in the plant. While specific studies in *Nicotiana attenuata* are limited, the enzyme's function can be inferred from its conserved role and structural domains shared with homologous proteins in other species. 