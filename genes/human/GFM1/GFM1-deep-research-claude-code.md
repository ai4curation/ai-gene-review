---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:27:52.790185'
end_time: '2026-10-24T04:28:30.016820'
duration_seconds: 37.23
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GFM1
  gene_symbol: GFM1
  uniprot_accession: Q96RP9
  protein_description: 'RecName: Full=Elongation factor G, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03061};
    Short=EF-Gmt {ECO:0000255|HAMAP-Rule:MF_03061}; EC=3.6.5.- {ECO:0000305|PubMed:19716793};
    AltName: Full=Elongation factor G 1, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03061};
    Short=mEF-G 1 {ECO:0000255|HAMAP-Rule:MF_03061}; AltName: Full=Elongation factor
    G1 {ECO:0000255|HAMAP-Rule:MF_03061}; Short=hEFG1; Flags: Precursor;'
  gene_info: Name=GFM1 {ECO:0000255|HAMAP-Rule:MF_03061}; Synonyms=EFG, EFG1 {ECO:0000255|HAMAP-Rule:MF_03061},
    GFM;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class translation factor GTPase
  protein_domains: EFG_II. (IPR041095); EFG_III. (IPR009022); EFG_III/V. (IPR035647);
    EFG_IV. (IPR047872); EFG_V. (IPR035649)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 2
  num_turns: 4
  total_cost_usd: 0.3031392
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 6
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96RP9
- **Protein Description:** RecName: Full=Elongation factor G, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03061}; Short=EF-Gmt {ECO:0000255|HAMAP-Rule:MF_03061}; EC=3.6.5.- {ECO:0000305|PubMed:19716793}; AltName: Full=Elongation factor G 1, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03061}; Short=mEF-G 1 {ECO:0000255|HAMAP-Rule:MF_03061}; AltName: Full=Elongation factor G1 {ECO:0000255|HAMAP-Rule:MF_03061}; Short=hEFG1; Flags: Precursor;
- **Gene Information:** Name=GFM1 {ECO:0000255|HAMAP-Rule:MF_03061}; Synonyms=EFG, EFG1 {ECO:0000255|HAMAP-Rule:MF_03061}, GFM;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class translation factor GTPase
- **Key Domains:** EFG_II. (IPR041095); EFG_III. (IPR009022); EFG_III/V. (IPR035647); EFG_IV. (IPR047872); EFG_V. (IPR035649)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GFM1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GFM1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GFM1** (gene ID: GFM1, UniProt: Q96RP9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GFM1 (EF-Gmt / mEF-G1, Q96RP9), human: research report

**Identity check.** The symbol GFM1 matches the UniProt record: "Elongation factor G, mitochondrial" (EF-Gmt, mEF-G1/hEFG1), a precursor protein of the TRAFAC class translation factor GTPases, with EF-G domains II–V (InterPro IPR041095, IPR009022, IPR035647, IPR047872, IPR035649). The organism is *Homo sapiens*. The literature found is about this protein, so there is no ambiguity.

**Method note.** This report rests on two web searches, covering the disease and the Tsuboi 2009 paper. Most of it comes from those results and from the UniProt record in the prompt. I did not read the full texts. Claims without a link below come from background knowledge and are marked "to verify". The PMIDs I cite for the enzyme and structural work are not confirmed here, so I left them out.

## 1. Primary function

GFM1 is the nuclear-encoded mitochondrial homolog of bacterial EF-G. It catalyses GTP-dependent translocation during mitochondrial translation elongation. In this step the ribosome moves along the mRNA by one codon and the tRNAs shift from the A and P sites to the P and E sites. The GTP hydrolysis it drives is annotated as EC 3.6.5.-, assigned in UniProt on the basis of PubMed 19716793.

The key evidence is Tsuboi et al. 2009, "EF-G2mt Is an Exclusive Recycling Factor in Mammalian Mitochondrial Protein Synthesis" (Mol Cell 35:502–510). PubMed 19716793 is the ID cited in UniProt, and I did not independently confirm it for this paper. According to the abstract as surfaced in search, bacterial EF-G has two jobs, translocation and ribosome recycling. In mitochondria these are split between two paralogs. EF-G1mt (GFM1) specifically catalyses translocation. EF-G2mt (GFM2) works with mitochondrial RRF to split ribosomes and has no translocation activity. Domain-swap experiments placed the functional specificity of EF-G2mt in domains III and IV. Sources: [Tsuboi 2009 via search result](https://pmc.ncbi.nlm.nih.gov/articles/PMC2673078), [SGD reference page](https://www.yeastgenome.org/reference/19716793).

Within the family, GFM1 is the translocase, and GFM2 (RRF2mt) is the recycling factor. Both are distinct from TUFM (EF-Tu), which delivers aminoacyl-tRNA. The 2020 bioRxiv cryo-EM preprint, which has not been peer reviewed, reports structural differences between the two isoforms, including in how they relate to antibiotic resistance. Source: [bioRxiv 2020](https://www.biorxiv.org/content/biorxiv/early/2020/12/21/2020.12.20.423689.full.pdf).

## 2. Localisation

GFM1 is synthesised with an N-terminal mitochondrial targeting sequence, which is the "Precursor" flag in UniProt. It acts in the mitochondrial matrix on mitoribosomes, which translate the 13 mtDNA-encoded OXPHOS subunits. It is expected to be associated with the inner membrane-tethered mitoribosome. Full-text confirmation of the localisation experiments is pending, and I did not locate the primary papers.

## 3. Pathway

GFM1 acts in mitochondrial translation, specifically the elongation cycle: EF-Tu•GTP•aa-tRNA decoding, peptidyl transfer, EF-G1mt translocation, then termination and recycling by mtRF1a, RRF and EF-G2mt. Through its products it supports assembly of OXPHOS complexes I, III, IV and V.

## 4. Disease

Biallelic GFM1 mutations cause combined oxidative phosphorylation deficiency 1 (COXPD1).

- Loss of function reduces or eliminates EF-G1mt, so fewer mtDNA-encoded OXPHOS proteins are made. More than one OXPHOS complex is therefore affected, which is why the disorder is called "combined". Source: [MedlinePlus](https://medlineplus.gov/genetics/condition/combined-oxidative-phosphorylation-deficiency-1).
- Brain and liver are most affected. Features include hepatoencephalopathy, corpus callosum hypoplasia and basal ganglia leukodystrophy. Individuals usually do not survive past early childhood, though some live longer. MedlinePlus counts at least 12 reported cases. A Leigh disease association is also listed on [GeneCards](https://www.genecards.org/card/GFM1).
- The first report of a patient is described in a 2010 Eur J Hum Genet study (reported via search). It screened 27 patients with combined OXPHOS defects and found a GFM1 mutation in one with severe, rapidly progressive encephalopathy. Enzyme defects appeared in fibroblasts but not in muscle. Both the OXPHOS defects and the translation impairment in fibroblasts were rescued by overexpressing wild-type GFM1. This rescue shows that GFM1 is the causal gene. A 2012 JIMD Reports paper on infantile progressive hepatoencephalomyopathy adds further cases (author lists not retrieved). Reviews of EF-G1mt note that its mutation causes fatal hepatoencephalopathy, indicating the protein is essential in humans. See also [PMC3062000](https://pmc.ncbi.nlm.nih.gov/articles/PMC3062000), which the search returned without enough detail for me to cite specifically.

## 5. Suggested GO framing for the review

The calls below are my inferences, to be checked against the existing GOA annotations.

- **Molecular function.** The best fit is GTPase activity combined with translation elongation factor activity. Ribosome-binding and mitoribosome terms are plausible. Avoid generic "protein binding".
- **Process.** Mitochondrial translational elongation (GO:0070125) is the core process. Per Tsuboi 2009, mitochondrial translational termination and ribosome recycling belong to GFM2, so annotating GFM1 there would be an over-annotation.
- **Component.** Mitochondrial matrix, possibly mitochondrion. A mitoribosome association is not established here.
- **Evidence.** The IEA and IBA annotations are probably sound given the conserved EF-G family. The experimental ones, especially IDA or IMP from the Tsuboi study, should be checked against full text before any change, per the project rule not to overrule curators from incomplete evidence.

## 6. Gaps and verification still needed

- Primary papers for localisation, GTPase kinetics and the mitoribosome structures with EF-G1mt were not retrieved. Verify their PMIDs before citing them.
- It is unclear whether the genotype–phenotype spectrum, such as the Leigh and milder cases, maps to specific domains. The tissue-specific sparing of muscle in the first patient is also unexplained.
- A suggested experiment is cryo-EM of translocation intermediates with disease variants.

## Sources

- [MedlinePlus: COXPD1](https://medlineplus.gov/genetics/condition/combined-oxidative-phosphorylation-deficiency-1)
- [GeneCards GFM1](https://www.genecards.org/card/GFM1)
- [Tsuboi et al. 2009 (PMC2673078)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2673078)
- [SGD reference 19716793](https://www.yeastgenome.org/reference/19716793)
- [bioRxiv 2020 cryo-EM preprint](https://www.biorxiv.org/content/biorxiv/early/2020/12/21/2020.12.20.423689.full.pdf)
- [PMC3062000](https://pmc.ncbi.nlm.nih.gov/articles/PMC3062000)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC2673078
2. https://www.yeastgenome.org/reference/19716793
3. https://www.biorxiv.org/content/biorxiv/early/2020/12/21/2020.12.20.423689.full.pdf
4. https://medlineplus.gov/genetics/condition/combined-oxidative-phosphorylation-deficiency-1
5. https://www.genecards.org/card/GFM1
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3062000