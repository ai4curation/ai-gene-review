---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:30:04.075473'
end_time: '2026-10-24T04:30:44.445401'
duration_seconds: 40.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TSFM
  gene_symbol: TSFM
  uniprot_accession: P43897
  protein_description: 'RecName: Full=Elongation factor Ts, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03135};
    Short=EF-Ts {ECO:0000255|HAMAP-Rule:MF_03135}; Short=EF-TsMt {ECO:0000255|HAMAP-Rule:MF_03135};
    Flags: Precursor;'
  gene_info: Name=TSFM {ECO:0000255|HAMAP-Rule:MF_03135};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the EF-Ts family. {ECO:0000255|HAMAP-
  protein_domains: EF-Ts_dimer_sf. (IPR036402); Transl_elong_EFTs/EF1B. (IPR001816);
    Transl_elong_EFTs/EF1B_dimer. (IPR014039); Transl_elong_Ts_CS. (IPR018101); UBA-like_sf.
    (IPR009060)
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
  num_turns: 5
  total_cost_usd: 0.21452730000000003
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 4
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P43897
- **Protein Description:** RecName: Full=Elongation factor Ts, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03135}; Short=EF-Ts {ECO:0000255|HAMAP-Rule:MF_03135}; Short=EF-TsMt {ECO:0000255|HAMAP-Rule:MF_03135}; Flags: Precursor;
- **Gene Information:** Name=TSFM {ECO:0000255|HAMAP-Rule:MF_03135};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the EF-Ts family. {ECO:0000255|HAMAP-
- **Key Domains:** EF-Ts_dimer_sf. (IPR036402); Transl_elong_EFTs/EF1B. (IPR001816); Transl_elong_EFTs/EF1B_dimer. (IPR014039); Transl_elong_Ts_CS. (IPR018101); UBA-like_sf. (IPR009060)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TSFM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TSFM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TSFM** (gene ID: TSFM, UniProt: P43897) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TSFM (human mitochondrial elongation factor Ts, UniProt P43897): research report

## Scope and caveats

- **Identity check passed.** The symbol TSFM, the UniProt record P43897 (EF-Ts, mitochondrial, EF-TsMt, precursor), the organism (*Homo sapiens*), and the EF-Ts family domains (IPR001816, IPR014039, IPR018101, IPR036402, UBA-like IPR009060) all agree. TSFM is the human mitochondrial translation elongation factor Ts, not another gene.
- **Sources.** The web search tool returned thin results in this session. The report rests mainly on the local UniProt record (`TSFM-uniprot.txt`), whose evidence codes cite the PMIDs below, and on the general literature on EF-Ts.
- **Citation status.** PMIDs are listed only where the UniProt record cites them. I have not read these papers, so I did not verify them against full text. Statements marked *(background)* come from my recall of the EF-Tu/EF-Ts literature and have no verified citation.
- **Not found.** I did not find a published structure of human TSFM in complex with mtEF-Tu (TUFM) or on the mitoribosome. The one TSFM structure in UniProt is an NMR structure of a short fragment.

## 1. Primary molecular function

**Reaction: guanine nucleotide exchange factor for mtEF-Tu.**
- TSFM binds the mitochondrial EF-Tu·GDP complex and induces exchange of GDP for GTP. UniProt (HAMAP MF_03135) states: "Associates with the EF-Tu.GDP complex and induces the exchange of GDP to GTP. It remains bound to the aminoacyl-tRNA.EF-Tu.GTP complex up to the GTP hydrolysis stage on the ribosome. Participates in mitochondrial translation (PubMed:27677415)." Local file: `TSFM-uniprot.txt`.
- The guanine nucleotide exchange factor (GEF) activity is annotated by sequence similarity (ISS from the mouse ortholog, P43896). It is not annotated from direct human biochemistry.
- The corresponding GO molecular function is GO:0005085 (guanyl-nucleotide exchange factor activity).
- GO:0003746 (translation elongation factor activity) is an IBA annotation. It is broad but acceptable. The more specific description is a GEF for EF-Tu.

**Mechanism (background).**
- In bacteria, EF-Tu has high affinity for GDP, so spontaneous release is slow. EF-Ts binds EF-Tu·GDP, destabilizes nucleotide binding, and releases GDP. GTP, which is more abundant in the cell, then rebinds. EF-Tu·GTP can then bind aminoacyl-tRNA and deliver it to the ribosomal A-site.
- Whether this conserved mechanism holds in human mitochondria is inferred from the UniProt/HAMAP family annotation, not from structures of the human proteins.
- Human mitochondrial EF-Ts is, as I recall, homologous to bacterial EF-Ts with a UBA-like domain and a dimerization domain. The domain assignments (IPR036402 EF-Ts dimerization superfamily, IPR009060 UBA-like superfamily) support this.

**Substrate specificity.**
- The substrate is mitochondrial EF-Tu (TUFM), not cytosolic eEF1A. The cytosolic counterpart is the eEF1B/eEF1Bα GEF family.
- The pathway is "Protein biosynthesis; polypeptide chain elongation" (UniProt, by similarity to mouse).

## 2. Cellular localization

- UniProt gives the **mitochondrial matrix**, by similarity to mouse (ISS). This is consistent with the N-terminal presequence (the entry is flagged "Precursor") and with the location of mitochondrial translation.
- A separate GO annotation, "mitochondrion", rests on Human Protein Atlas immunofluorescence (IDA:HPA).
- The mitoribosome sits on the matrix face of the inner membrane. The 13 mtDNA-encoded OXPHOS subunits are translated there, so matrix localization fits the function.

## 3. Biological process and pathway

- **Mitochondrial translational elongation** (GO:0070125) is annotated IDA:UniProtKB. The UniProt record cites PMID:27677415, which I did not read.
- TSFM acts within the mitochondrial translation elongation cycle, as the nucleotide exchange partner of TUFM, which delivers aminoacyl-tRNAs to the A-site. The cycle then proceeds through GTP hydrolysis, EF-Tu·GDP release, and re-activation by TSFM.
- The products of this cycle are the 13 mtDNA-encoded subunits of OXPHOS complexes I, III, IV and V. Complex II is entirely nuclear-encoded.
- UniProt also annotates RNA binding (GO:0003723) as HDA (high-throughput). This is a weak, non-specific annotation. It likely reflects interactome-capture or similar data and is not evidence of a specific RNA-binding function.

## 4. Disease: COXPD3 as functional evidence

The UniProt record links TSFM variants to **combined oxidative phosphorylation deficiency 3 (COXPD3, MIM:610505)**. UniProt describes it as "a mitochondrial disease resulting in severe metabolic acidosis with encephalomyopathy or with hypertrophic cardiomyopathy. Patients show a severe defect in mitochondrial translation leading to a failure to assemble adequate amounts of three of the oxidative phosphorylation complexes."

The disease evidence is cited as PMIDs 17033963, 21741925, 22499341, 25037205, 27677415 and 30911037.

- **Phenotypic range.** From UniProt's description plus the case report in the search results, the range runs from infantile encephalomyopathy to hypertrophic cardiomyopathy. A 2019 case report describes a 33-year-old woman with compound heterozygous variants and severe cardiomyopathy. I could not verify that report's PMID.
- **Case-report findings (from the search snippet, unverified).**
  - The authors predicted that the variants destabilize the EF-Ts–EF-Tu complex.
  - Both proteins were markedly reduced in affected heart muscle, which showed combined respiratory chain deficiency.
  - In patient fibroblasts, EF-Ts was reduced, EF-Tu was elevated, and oxygen consumption was normal. This points to tissue-specific compensation, which is consistent with the tissue-variable phenotype.
- **Interpretation.** Loss-of-function variants reduce mitochondrial translation and impair OXPHOS assembly. This is genetic evidence that TSFM is necessary for mitochondrial translation. It does not by itself separate TSFM's catalytic role from stabilizing TUFM.

## 5. Other features

- **Expression** (UniProt): all tissues, highest in skeletal muscle, liver and kidney. This matches tissues with high oxidative demand.
- **Isoforms:** four alternatively spliced isoforms (P43897-1 to -4).
- **Structure:** PDB 2CP9, an NMR structure of residues 45–95 (a small N-terminal region). It is not informative about the GEF interface.
- **Interactions** (IntAct, as listed in UniProt): CCDC89, CEP70, CPLX2, GAS8, GOLGA6L9, KRTAP1-1, MDFI and RALBP1, each with NbExp of 3–4. These look like high-throughput two-hybrid-type hits and are probably not physiologically relevant. The expected functional partner, TUFM, is not listed there.

## 6. Annotation recommendations

| Term | Basis | Suggested action |
|---|---|---|
| GO:0070125 mitochondrial translational elongation | IDA | Accept as core process |
| GO:0005085 guanyl-nucleotide exchange factor activity | ISS from mouse | Accept as core function (more specific than elongation factor activity) |
| GO:0003746 translation elongation factor activity | IBA | Accept; keep as a broader parent |
| GO:0005759 mitochondrial matrix | ISS | Accept as the core location |
| GO:0005739 mitochondrion | IDA (HPA) | Accept; less specific than the matrix term |
| GO:0003723 RNA binding | HDA | Candidate for mark-as-over-annotated or non-core; not supported as a specific function |

An optional new annotation would be a more specific term for the EF-Tu-directed activity, if one exists. I did not check ontology term definitions in this session.

## 7. Open questions and suggested experiments

1. Is there a structure of the human TSFM–TUFM complex? The search found none. Cryo-EM or crystallography of the human complex, with and without a disease variant, would close this.
2. Do the COXPD3 variants impair nucleotide exchange or complex stability? An in vitro GDP/GTP exchange assay with recombinant TUFM would separate the two.
3. What explains the tissue specificity (cardiomyopathy versus encephalopathy)? Compare TUFM/TSFM ratios across tissues, since fibroblasts appear to compensate by raising EF-Tu.
4. Does TSFM remain bound to the ternary complex on the mitoribosome, as UniProt describes? Mitoribosome structures with elongation factors could test this.

## Sources

- Local UniProt record: `genes/human/TSFM/TSFM-uniprot.txt` (P43897). Cited there: PMID:17033963, PMID:21741925, PMID:22499341, PMID:25037205, PMID:27677415, PMID:30911037 (not independently read).
- Web search results, snippet-level only and unverified:
  - [GeneCards TSFM](https://www.genecards.org/card/TSFM)
  - [QIAGEN GeneGlobe TSFM](https://geneglobe.qiagen.com/be/knowledge/gene/ENSG00000123297)
  - [CNR record on a TSFM case report](https://iris.cnr.it/handle/20.500.14243/424800)
  - [Karolinska mitoribosome project page](https://nim.nsc.liu.se/projects/6937)

## Citations

1. https://www.genecards.org/card/TSFM
2. https://geneglobe.qiagen.com/be/knowledge/gene/ENSG00000123297
3. https://iris.cnr.it/handle/20.500.14243/424800
4. https://nim.nsc.liu.se/projects/6937