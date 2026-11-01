---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:30:04.408709'
end_time: '2026-10-24T04:30:50.709666'
duration_seconds: 46.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TUFM
  gene_symbol: TUFM
  uniprot_accession: P49411
  protein_description: 'RecName: Full=Elongation factor Tu, mitochondrial; Short=EF-Tu;
    EC=3.6.5.3 {ECO:0000250|UniProtKB:P49410}; AltName: Full=P43; Flags: Precursor;'
  gene_info: Name=TUFM;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class translation factor GTPase
  protein_domains: EF-Tu_GTP-bd. (IPR041709); EF-Tu_GTPase. (IPR050055); EFTu-like_2.
    (IPR004161); EFTU_2. (IPR033720); G_TR_CS. (IPR031157)
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
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.23375320000000002
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
- **UniProt Accession:** P49411
- **Protein Description:** RecName: Full=Elongation factor Tu, mitochondrial; Short=EF-Tu; EC=3.6.5.3 {ECO:0000250|UniProtKB:P49410}; AltName: Full=P43; Flags: Precursor;
- **Gene Information:** Name=TUFM;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class translation factor GTPase
- **Key Domains:** EF-Tu_GTP-bd. (IPR041709); EF-Tu_GTPase. (IPR050055); EFTu-like_2. (IPR004161); EFTU_2. (IPR033720); G_TR_CS. (IPR031157)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TUFM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TUFM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TUFM** (gene ID: TUFM, UniProt: P49411) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TUFM (P49411): human mitochondrial elongation factor Tu

**Method note.** I did only a few targeted searches. Most mechanistic statements come from the UniProt record and the general literature on EF-Tu, not from papers I read this session. They are marked as such.

## 1. Identity check
- The symbol TUFM matches the UniProt record: P49411, "Elongation factor Tu, mitochondrial", EC 3.6.5.3, human (UniProt header supplied with the task).
- The family and domains fit. It belongs to the TRAFAC translation-factor GTPase class and has a GTP-binding domain (EF-Tu_GTP-bd) and the EF-Tu domain 2 and domain 3 modules (EFTU_2, EFTu-like_2). These are the same domains as bacterial EF-Tu.
- I found no ambiguity with another gene. TUFM is the nuclear-encoded mitochondrial EF-Tu. It is separate from the cytosolic eEF1A and from bacterial tufA/tufB.

## 2. Primary molecular function
**Reaction (EC 3.6.5.3, protein-synthesis GTPase):** GTP + H2O → GDP + phosphate, coupled to delivering aminoacyl-tRNA to the A-site of the mitoribosome.

- **Ternary complex.** In the GTP-bound state, EF-Tu binds aminoacyl-tRNA (aa-tRNA) and forms the EF-Tu·GTP·aa-tRNA complex.
- **Decoding.** The complex enters the A-site of the mitoribosome, where codon–anticodon pairing triggers GTP hydrolysis.
- **Release.** EF-Tu·GDP is released, and the aa-tRNA is accommodated in the peptidyl-transferase center.
- **Recycling.** The mitochondrial nucleotide-exchange factor TSFM (EF-Ts) regenerates EF-Tu·GTP.
- **Source.** This is inferred from the canonical bacterial and mitochondrial elongation cycle. See Kummer & Ban 2021, *Nat Rev Mol Cell Biol* 22:307–325, PMID:33594280 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/33594280/)). That review covers the architecture and mechanism of the mammalian mitochondrial translation apparatus. The search returned no passage on EF-Tu itself, so the specifics above are not quoted from it.
- **Substrate specificity.** Mitochondrial EF-Tu works with the 22 mt-tRNAs, which are unusual in structure. It handles mitochondrial Met-tRNA only in the elongation role, since initiation uses a formylated Met-tRNA and the separate factor MTIF2. I recall these properties from the biochemical literature but did not re-verify them.

**Suggested GO terms**
- MF: translation elongation factor activity (GO:0003746), GTPase activity (GO:0003924), GTP binding (GO:0005525), and aminoacyl-tRNA binding (also mitochondrial tRNA binding).
- BP: mitochondrial translational elongation (GO:0070125).
- Avoid: "protein binding".

## 3. Localization and pathway
- **Compartment.** The mitochondrial matrix, where it acts on mitoribosomes (inner-membrane-associated).
- **Targeting.** The protein is a precursor with an N-terminal mitochondrial targeting sequence (UniProt "Flags: Precursor").
- **Pathway.** Mitochondrial translation elongation, which makes the 13 mtDNA-encoded OXPHOS subunits. Loss of TUFM therefore affects complexes I, III, IV and V, but not complex II, whose subunits are all nuclear-encoded.
- **Upstream/downstream.** Aminoacylated mt-tRNAs are supplied by the mitochondrial aminoacyl-tRNA synthetases. After peptide-bond formation, EF-G1 (GFM1) catalyzes translocation, and TSFM recycles EF-Tu.

## 4. Disease evidence
- **COXPD4.** Biallelic TUFM mutations cause combined oxidative phosphorylation deficiency 4 (OMIM #610678) ([OMIM mirror](https://https.ncbi.nlm.nih.gov/omim/610678); [LOVD](https://databases.lovd.nl/shared/diseases/02969)).
- **Valente et al. 2007** (*Am J Hum Genet*). This is the founding report. An infant had homozygous c.1016G>A, p.Arg339Gln, with neonatal lactic acidosis, rapidly progressive encephalopathy, severely decreased mitochondrial protein synthesis, and combined deficiency of the mtDNA-dependent respiratory complexes. The same paper described a GFM1 (EF-G1) case ([Helmholtz PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/3067)). I recall the PMID as 17160894, but one search source gave 17160893. **Verify this PMID before citing it.**
- **Further cases.** R339Q has been seen in other families. A 2024 case report states that only six patients with biallelic pathogenic TUFM variants had been reported at that time ([De Gruyter, *J Pediatr Endocrinol Metab*](https://www.degruyterbrill.com/document/doi/10.1515/jpem-2023-0569)).
- **Interpretation.** The defect is in mtDNA-encoded protein synthesis, which is consistent with TUFM being required for mitochondrial translation elongation. This is human genetic evidence of necessity, not a mechanistic assay of its GTPase activity.

## 5. Non-canonical roles (secondary)
- **NLRX1 complex.** Lei et al. 2012, *Immunity* 36:933–946, PMID:22749352 ([PMC3397828](https://pmc.ncbi.nlm.nih.gov/articles/PMC3397828)). TUFM was identified by mass spectrometry as an NLRX1 partner. It also binds the Atg5–Atg12 complex and Atg16L1. Like NLRX1, it dampens RLR-driven type I interferon signaling and promotes autophagy during viral infection (the search summary describes it in these terms; I did not read the full text).
- **Caveat.** These findings were made largely in mouse and cell-line systems. I treat them as non-core, moonlighting roles. The core function remains mitochondrial translation elongation.

## 6. Evidence quality summary
| Claim | Evidence | Strength |
|---|---|---|
| Elongation factor GTPase in mitochondria | Family/domain homology, UniProt, human disease phenotype | Strong inference, plus genetics |
| Matrix localization | Mitochondrial targeting sequence, function | Strong inference |
| COXPD4 | Valente 2007 and later case reports | Strong |
| Autophagy/IFN modulation | Lei 2012 | Moderate, non-core |

## 7. Suggested follow-ups
- Confirm the Valente 2007 PMID against PubMed.
- Pull primary biochemistry on bovine and human mt-EF-Tu: GTP/GDP affinity, TSFM exchange, and tRNA binding (Spremulli lab).
- Look at recent mitoribosome cryo-EM structures with EF-Tu·GTP·aa-tRNA in the A-site, to cite structural support.

## Sources
- [Kummer & Ban 2021, PubMed 33594280](https://pubmed.ncbi.nlm.nih.gov/33594280/)
- [Lei et al. 2012, PMC3397828](https://pmc.ncbi.nlm.nih.gov/articles/PMC3397828)
- [OMIM #610678 mirror](https://https.ncbi.nlm.nih.gov/omim/610678)
- [LOVD COXPD4](https://databases.lovd.nl/shared/diseases/02969)
- [Helmholtz PhenoDis COXPD4](https://iegext02.helmholtz-munich.de/phenodis/disease/show/3067)
- [J Pediatr Endocrinol Metab 2024 case report](https://www.degruyterbrill.com/document/doi/10.1515/jpem-2023-0569)

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/33594280/
2. https://https.ncbi.nlm.nih.gov/omim/610678
3. https://databases.lovd.nl/shared/diseases/02969
4. https://iegext02.helmholtz-munich.de/phenodis/disease/show/3067
5. https://www.degruyterbrill.com/document/doi/10.1515/jpem-2023-0569
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3397828