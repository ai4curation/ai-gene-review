---
provider: openai
model: gpt-4.1
cached: false
start_time: '2026-04-05T13:06:37.045940'
end_time: '2026-04-05T13:06:47.909171'
duration_seconds: 10.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NICAT
  gene_id: A0A1J6KBX2
  gene_symbol: NaAO2_candidate_AO_0
  uniprot_accession: A0A1J6KBX2
  protein_description: 'RecName: Full=L-aspartate oxidase; EC=1.4.3.16;'
  gene_info: Name=AO_0; ORFNames=A4A49_29386;
  organism_full: Nicotiana attenuata (Coyote tobacco).
  protein_family: Belongs to the FAD-dependent oxidoreductase 2 family. NadB subfamily.
  protein_domains: FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188);
    Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939);
    NadB. (IPR005288)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    top_p: 1.0
citation_count: 5
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A1J6KBX2
- **Protein Description:** RecName: Full=L-aspartate oxidase; EC=1.4.3.16;
- **Gene Information:** Name=AO_0; ORFNames=A4A49_29386;
- **Organism (full):** Nicotiana attenuata (Coyote tobacco).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase 2 family. NadB subfamily.
- **Key Domains:** FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188); Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939); NadB. (IPR005288)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NaAO2_candidate_AO_0" matches the protein description above**
2. **Verify the organism is correct:** Nicotiana attenuata (Coyote tobacco).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NaAO2_candidate_AO_0' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NaAO2_candidate_AO_0** (gene ID: A0A1J6KBX2, UniProt: A0A1J6KBX2) in NICAT.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

The gene **NaAO2_candidate_AO_0** in *Nicotiana attenuata* encodes the enzyme L-aspartate oxidase (LASPO), a pivotal component in the de novo biosynthesis of nicotinamide adenine dinucleotide (NAD⁺). This enzyme catalyzes the oxidation of L-aspartate to iminoaspartate, marking the initial step in the NAD⁺ biosynthetic pathway.

**Enzymatic Function and Reaction Mechanism**

L-aspartate oxidase is a flavoprotein that utilizes flavin adenine dinucleotide (FAD) as a cofactor. The enzyme's primary function involves the oxidation of L-aspartate to iminoaspartate, a reaction that can proceed using molecular oxygen or fumarate as electron acceptors. This reaction is crucial for the subsequent steps in NAD⁺ biosynthesis, as iminoaspartate serves as a precursor for quinolinate, a key intermediate in the pathway. In *Arabidopsis thaliana*, a model plant species, the LASPO enzyme has been characterized with a Km of 0.79 mM for L-aspartate and a kcat of 0.25 s⁻¹, indicating its affinity and catalytic efficiency for the substrate ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29650151/?utm_source=openai)).

**Biological Role and Pathway Involvement**

The de novo NAD⁺ biosynthetic pathway in plants initiates with the LASPO-catalyzed oxidation of L-aspartate. This pathway is essential for maintaining NAD⁺ homeostasis, which is vital for various metabolic processes, including redox reactions, DNA repair, and signaling mechanisms. In *Arabidopsis thaliana*, LASPO activity has been linked to stomatal immunity, highlighting its role beyond primary metabolism ([ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/gene/831328?utm_source=openai)).

**Substrate Specificity**

LASPO specifically acts on L-aspartate, converting it into iminoaspartate. This specificity ensures the proper flow of metabolites through the NAD⁺ biosynthetic pathway, preventing the accumulation of intermediates and maintaining metabolic balance.

**Cellular Localization**

In *Arabidopsis thaliana*, LASPO is localized within the chloroplasts, indicating that the initial steps of NAD⁺ biosynthesis occur in this organelle ([ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/gene/831328?utm_source=openai)). While direct evidence for the subcellular localization of LASPO in *Nicotiana attenuata* is lacking, it is reasonable to infer a similar chloroplastic localization, given the conserved nature of this pathway among plant species.

**Regulation and Inhibition**

The activity of LASPO is subject to regulation by various metabolites. In *Arabidopsis thaliana*, NADP⁺ and NADH have been shown to inhibit LASPO activity by competing with the flavin cofactor for binding to the enzyme. This feedback inhibition mechanism helps maintain NAD⁺ homeostasis within the cell ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29650151/?utm_source=openai)).

**Evolutionary Conservation and Structural Insights**

LASPO belongs to the FAD-dependent oxidoreductase 2 family, specifically the NadB subfamily. This family is characterized by a conserved FAD-binding domain, which is essential for the enzyme's oxidoreductase activity. Structural analyses suggest that LASPO adopts a fold similar to that of succinate dehydrogenase, indicating a conserved mechanism of action among these enzymes ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0168945218302048?utm_source=openai)).

**Conclusion**

The L-aspartate oxidase encoded by the **NaAO2_candidate_AO_0** gene in *Nicotiana attenuata* plays a fundamental role in the de novo biosynthesis of NAD⁺, initiating the pathway by oxidizing L-aspartate to iminoaspartate. While specific studies on this enzyme in *Nicotiana attenuata* are limited, insights from model organisms like *Arabidopsis thaliana* provide a framework for understanding its function, regulation, and structural characteristics. Further research is needed to elucidate the specific roles and regulatory mechanisms of LASPO in *Nicotiana attenuata*, particularly concerning its involvement in secondary metabolite biosynthesis and stress responses. 