---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:08:22.461754'
end_time: '2026-04-05T13:08:37.130985'
duration_seconds: 14.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: A0A1J6IKI8
  gene_symbol: NaQPT2_candidate_QPT_1
  uniprot_accession: A0A1J6IKI8
  protein_description: nicotinate-nucleotide diphosphorylase (carboxylating) ;
  gene_info: Name=QPT_1 ; ORFNames=A4A49_58606 ;
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
citation_count: 1
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A1J6IKI8
- **Protein Description:** nicotinate-nucleotide diphosphorylase (carboxylating) ;
- **Gene Information:** Name=QPT_1 ; ORFNames=A4A49_58606 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the NadC/ModD family.
- **Key Domains:** Aldolase_TIM. (IPR013785);  NadC. (IPR004393);  NadC/ModD. (IPR027277);  Nicotinate_pribotase-like_C. (IPR036068);  Quinolinate_PRibosylTase_N_sf. (IPR037128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaQPT2_candidate_QPT_1" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaQPT2_candidate_QPT_1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaQPT2_candidate_QPT_1** (gene ID: A0A1J6IKI8, UniProt: A0A1J6IKI8) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

**Gene Research Report: NaQPT2_candidate_QPT_1 (UniProt Accession: A0A1J6IKI8) in *Nicotiana attenuata* (Coyote Tobacco)**

**1. Gene and Protein Identification**

- **UniProt Accession:** A0A1J6IKI8
- **Protein Description:** Nicotinate-nucleotide diphosphorylase (carboxylating)
- **Gene Information:** Name=QPT_1; ORFNames=A4A49_58606
- **Organism:** *Nicotiana attenuata* (Coyote tobacco)
- **Protein Family:** Belongs to the NadC/ModD family
- **Key Domains:** Aldolase_TIM (IPR013785); NadC (IPR004393); NadC/ModD (IPR027277); Nicotinate_pribotase-like_C (IPR036068); Quinolinate_PRibosylTase_N_sf (IPR037128)

**2. Functional Annotation**

The protein encoded by the gene *NaQPT2_candidate_QPT_1* in *Nicotiana attenuata* is identified as nicotinate-nucleotide diphosphorylase (carboxylating), also known as quinolinate phosphoribosyltransferase (QAPRTase). This enzyme plays a pivotal role in the biosynthesis of nicotinamide adenine dinucleotide (NAD⁺), a crucial coenzyme in cellular metabolism.

**Catalytic Activity:**

The enzyme catalyzes the conversion of quinolinate (pyridine-2,3-dicarboxylate) to nicotinate D-ribonucleotide (NaMN), a key intermediate in the NAD⁺ biosynthetic pathway. The reaction proceeds as follows:

\[ \text{Quinolinate} + 5\text{-phospho-}\alpha\text{-D-ribose 1-diphosphate} \rightarrow \text{Nicotinate D-ribonucleotide} + \text{CO}_2 + \text{Diphosphate} \]

This reaction is essential for the de novo synthesis of NAD⁺, facilitating the conversion of quinolinate, derived from tryptophan metabolism, into NaMN. The enzyme's activity is classified under EC 2.4.2.19. ([enzyme.expasy.org](https://enzyme.expasy.org/EC/2.4.2.19?utm_source=openai))

**Biological Process:**

In plants, NAD⁺ is vital for various metabolic processes, including glycolysis, the tricarboxylic acid cycle, and oxidative phosphorylation. The biosynthesis of NAD⁺ through the de novo pathway, involving QAPRTase, is crucial for maintaining cellular redox balance and energy metabolism.

**3. Structural and Domain Information**

The protein belongs to the NadC/ModD family and contains several conserved domains:

- **Aldolase_TIM (IPR013785):** A domain associated with the TIM barrel fold, common in enzymes with diverse catalytic functions.
- **NadC (IPR004393):** A domain specific to nicotinate-nucleotide diphosphorylases, indicating its role in NAD⁺ biosynthesis.
- **NadC/ModD (IPR027277):** A superfamily domain encompassing enzymes involved in NAD⁺ biosynthesis.
- **Nicotinate_pribotase-like_C (IPR036068):** A C-terminal domain found in nicotinate phosphoribosyltransferases.
- **Quinolinate_PRibosylTase_N_sf (IPR037128):** An N-terminal domain associated with quinolinate phosphoribosyltransferase activity.

These domains collectively contribute to the enzyme's function in catalyzing the conversion of quinolinate to NaMN.

**4. Localization**

While specific subcellular localization data for the *Nicotiana attenuata* QAPRTase is not available, similar enzymes in other organisms are typically localized in the cytoplasm, where NAD⁺ biosynthesis occurs. Therefore, it is reasonable to infer a cytoplasmic localization for this enzyme in *Nicotiana attenuata*.

**5. Pathway Involvement**

The enzyme is a key component of the de novo NAD⁺ biosynthesis pathway. In plants, this pathway is essential for producing NAD⁺ from quinolinate, derived from tryptophan metabolism. NAD⁺ serves as a coenzyme in redox reactions, playing a central role in energy metabolism and various biosynthetic processes.

**6. Evolutionary Conservation**

Nicotinate-nucleotide diphosphorylases are conserved across various species, including bacteria, archaea, and eukaryotes, indicating their fundamental role in cellular metabolism. The conservation of key domains and catalytic mechanisms underscores the enzyme's essential function in NAD⁺ biosynthesis.

**7. Experimental Evidence and Inference**

Direct experimental studies on the *Nicotiana attenuata* QAPRTase are limited. However, the presence of conserved domains and its classification within the NadC/ModD family strongly suggest that this enzyme performs a similar function to its homologs in other organisms. Bioinformatic analyses and comparative studies support this inference, highlighting the enzyme's role in NAD⁺ biosynthesis.

**8. Conclusion**

The *NaQPT2_candidate_QPT_1* gene in *Nicotiana attenuata* encodes a nicotinate-nucleotide diphosphorylase (carboxylating) enzyme, integral to the de novo NAD⁺ biosynthesis pathway. Through the conversion of quinolinate to nicotinate D-ribonucleotide, this enzyme contributes to the production of NAD⁺, a coenzyme essential for numerous metabolic processes. While direct experimental data in *Nicotiana attenuata* is scarce, the conserved nature of this enzyme across species provides a strong basis for its functional annotation. 