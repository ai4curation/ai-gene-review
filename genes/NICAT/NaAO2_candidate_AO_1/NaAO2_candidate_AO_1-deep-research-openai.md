---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:07:48.605372'
end_time: '2026-04-05T13:08:05.795282'
duration_seconds: 17.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: A0A314LIN0
  gene_symbol: NaAO2_candidate_AO_1
  uniprot_accession: A0A314LIN0
  protein_description: L-aspartate oxidase ;
  gene_info: Name=AO_1 ; ORFNames=A4A49_12091 ;
  organism_full: Nicotiana attenuata (Coyote tobacco).
  protein_family: Belongs to the FAD-dependent oxidoreductase 2 family. NadB
  protein_domains: FAD-dep_OxRdtase_2_FAD-bd. (IPR003953);  FAD/NAD-bd_sf. (IPR036188);  Fum_R/Succ_DH_flav-like_C_sf.
    (IPR037099);  Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939);  NadB. (IPR005288)
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
- **UniProt Accession:** A0A314LIN0
- **Protein Description:** L-aspartate oxidase ;
- **Gene Information:** Name=AO_1 ; ORFNames=A4A49_12091 ;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase 2 family. NadB
- **Key Domains:** FAD-dep_OxRdtase_2_FAD-bd. (IPR003953);  FAD/NAD-bd_sf. (IPR036188);  Fum_R/Succ_DH_flav-like_C_sf. (IPR037099);  Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939);  NadB. (IPR005288)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaAO2_candidate_AO_1" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaAO2_candidate_AO_1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaAO2_candidate_AO_1** (gene ID: A0A314LIN0, UniProt: A0A314LIN0) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

The gene **NaAO2_candidate_AO_1** in *Nicotiana attenuata* encodes the enzyme L-aspartate oxidase (LASPO), a pivotal component in the biosynthesis of nicotinamide adenine dinucleotide (NAD⁺) and nicotine alkaloids. This enzyme catalyzes the oxidation of L-aspartate to iminosuccinate, a reaction integral to both NAD⁺ biosynthesis and the production of nicotine, a key secondary metabolite in *N. attenuata*.

**Enzymatic Function and Catalytic Activity**

L-aspartate oxidase (EC 1.4.3.16) facilitates the conversion of L-aspartate and molecular oxygen into iminosuccinate and hydrogen peroxide:

\[ \text{L-aspartate} + O_2 \rightarrow \text{iminosuccinate} + H_2O_2 \]

This reaction represents the initial step in the de novo NAD⁺ biosynthetic pathway. In *Escherichia coli*, iminosuccinate is further processed by quinolinate synthase to produce quinolinic acid, a precursor for NAD⁺ synthesis ([en.wikipedia.org](https://en.wikipedia.org/wiki/L-aspartate_oxidase?utm_source=openai)). While the specific downstream enzymes in *N. attenuata* remain to be fully elucidated, it is likely that a similar pathway exists, given the conservation of NAD⁺ biosynthesis across species.

**Structural Characteristics and Cofactor Requirements**

LASPO belongs to the FAD-dependent oxidoreductase 2 family, characterized by the presence of several conserved domains:

- **FAD-binding domain (IPR003953):** Essential for the binding of flavin adenine dinucleotide (FAD), a cofactor necessary for the enzyme's oxidoreductase activity.

- **FAD/NAD-binding domain superfamily (IPR036188):** Facilitates interactions with nucleotide cofactors, crucial for electron transfer during the catalytic process.

- **Fumarate reductase/succinate dehydrogenase flavoprotein-like C-terminal domain (IPR015939):** Shares structural similarities with other flavoproteins involved in redox reactions.

These domains collectively contribute to the enzyme's ability to catalyze the oxidation of L-aspartate, underscoring its role in redox biology.

**Biological Role in NAD⁺ Biosynthesis**

In plants, LASPO initiates the de novo synthesis of NAD⁺ by converting L-aspartate into iminosuccinate. Subsequent enzymatic steps lead to the formation of quinolinic acid and ultimately NAD⁺. This pathway is vital for maintaining cellular redox balance and energy metabolism. Studies in *Arabidopsis thaliana* have demonstrated that LASPO activity is crucial for NAD⁺ homeostasis, with the enzyme localized in chloroplasts, indicating its integration into photosynthetic metabolism ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29650151/?utm_source=openai)).

**Involvement in Nicotine Biosynthesis**

*N. attenuata* is renowned for its production of nicotine, a secondary metabolite that serves as a defense mechanism against herbivores. The biosynthesis of nicotine involves two primary pathways:

1. **Pyridine Nucleotide Cycle:** Generates nicotinic acid from L-aspartate via the action of LASPO, quinolinate synthase, and quinolinic acid phosphoribosyltransferase.

2. **Methylpyrrole Pathway:** Produces putrescine, which is methylated to form N-methylputrescine, a precursor for the pyrrolidine ring of nicotine.

The integration of these pathways leads to the synthesis of nicotine, with LASPO playing a foundational role by providing nicotinic acid ([frontiersin.org](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1647622/full?utm_source=openai)).

**Subcellular Localization**

While direct experimental evidence for LASPO localization in *N. attenuata* is limited, studies in related species suggest a chloroplastic localization. In *A. thaliana*, LASPO is localized in chloroplasts, aligning with its role in NAD⁺ biosynthesis and linking it to photosynthetic processes ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29650151/?utm_source=openai)). Given the conservation of metabolic pathways, it is plausible that LASPO in *N. attenuata* shares a similar subcellular distribution.

**Pathway Integration and Functional Implications**

The activity of LASPO in *N. attenuata* is integral to both primary and secondary metabolism:

- **NAD⁺ Biosynthesis:** Essential for numerous metabolic processes, including glycolysis, the tricarboxylic acid cycle, and oxidative phosphorylation.

- **Nicotine Production:** Provides nicotinic acid, a precursor for nicotine biosynthesis, contributing to the plant's defense mechanisms.

The dual role of LASPO underscores its importance in the metabolic network of *N. attenuata*, influencing both energy metabolism and ecological interactions through secondary metabolite production.

**Conclusion**

The gene **NaAO2_candidate_AO_1** encodes L-aspartate oxidase, a key enzyme in *N. attenuata* that catalyzes the oxidation of L-aspartate to iminosuccinate. This reaction is crucial for the biosynthesis of NAD⁺ and serves as a foundational step in nicotine production. While direct studies on LASPO in *N. attenuata* are limited, insights from related species provide a framework for understanding its function, localization, and role in metabolic pathways. Further research is needed to elucidate the specific regulatory mechanisms and interactions of LASPO within the unique metabolic context of *N. attenuata*. 