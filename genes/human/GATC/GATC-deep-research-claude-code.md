---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:16:45.727894'
end_time: '2026-10-14T23:17:25.418307'
duration_seconds: 39.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GATC
  gene_symbol: GATC
  uniprot_accession: O43716
  protein_description: 'RecName: Full=Glutamyl-tRNA(Gln) amidotransferase subunit
    C, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03149}; Short=Glu-AdT subunit C {ECO:0000255|HAMAP-Rule:MF_03149};
    Short=hGatC {ECO:0000303|PubMed:19805282}; AltName: Full=Protein 15E1.2; Flags:
    Precursor;'
  gene_info: Name=GATC {ECO:0000255|HAMAP-Rule:MF_03149}; Synonyms=15E1.2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the GatC family. {ECO:0000255|HAMAP-
  protein_domains: Asp/Glu-ADT_sf_sub_c. (IPR036113); GatC. (IPR003837); GatC (PF02686)
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
  total_cost_usd: 0.20444800000000002
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 5
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O43716
- **Protein Description:** RecName: Full=Glutamyl-tRNA(Gln) amidotransferase subunit C, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03149}; Short=Glu-AdT subunit C {ECO:0000255|HAMAP-Rule:MF_03149}; Short=hGatC {ECO:0000303|PubMed:19805282}; AltName: Full=Protein 15E1.2; Flags: Precursor;
- **Gene Information:** Name=GATC {ECO:0000255|HAMAP-Rule:MF_03149}; Synonyms=15E1.2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the GatC family. {ECO:0000255|HAMAP-
- **Key Domains:** Asp/Glu-ADT_sf_sub_c. (IPR036113); GatC. (IPR003837); GatC (PF02686)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GATC" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GATC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GATC** (gene ID: GATC, UniProt: O43716) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GATC (UniProt O43716), human mitochondrial glutamyl-tRNA(Gln) amidotransferase subunit C

## 0. Identity check
- The symbol GATC is the HGNC symbol for the human glutamyl-tRNA(Gln) amidotransferase subunit C (Glu-AdT subunit C, hGatC, formerly 15E1.2). It is not the "GATC" DNA motif used in Dam methylation or restriction-site literature, and it is not a different gene.
- The UniProt record (O43716) gives the family as GatC and the domains as GatC (PF02686, IPR003837) and Asp/Glu-ADT_sf_sub_c (IPR036113). The record is a mitochondrial precursor.
- The symbol is ambiguous with the DNA tetranucleotide. The literature below is for the protein.
- Evidence limits: I had no access to the cached `publications/` files or to the full texts. Statements below come from the UniProt header text supplied in the prompt and from web search summaries. I did not check the quotes verbatim, so they should not be used as `supporting_text` without checking.

## 1. Primary function
GATC is the smallest, non-catalytic subunit of the heterotrimeric mitochondrial GatCAB complex. The other two subunits are QRSL1 (GatA) and GATB.

- **Why the complex is needed.** Mitochondria have no glutaminyl-tRNA synthetase. Mitochondrial tRNA(Gln) is first mischarged with glutamate by the mitochondrial glutamyl-tRNA synthetase (EARS2). GatCAB then converts the Glu-tRNA(Gln) to Gln-tRNA(Gln) by transamidation.
  - Reaction: Glu-tRNA(Gln) + L-glutamine + ATP → Gln-tRNA(Gln) + L-glutamate + ADP + Pi.
  - GatA (QRSL1) supplies the glutamine amidase activity. GatB (GATB) activates the Glu-tRNA with ATP and carries the transamidase function. GatC stabilises the complex and acts as a scaffold between them.
- **Evidence for the pathway.** Nagao et al. 2009, "Biogenesis of glutaminyl-mt tRNAGln in human mitochondria", PNAS (PMID:19805282). The UniProt record cites this paper for the "hGatC" name, and it is the source for the human indirect Gln-mt-tRNA pathway.
  - From memory, which I could not check here, it showed that human GatA, GatB and GatC form the complex and are all needed to make Gln-mt-tRNA(Gln).
  - Web search could not retrieve this paper, so the details are unconfirmed.
- **Evidence from patients.** Friederich et al. 2018, Nat Commun, "Pathogenic variants in glutamyl-tRNAGln amidotransferase subunits cause a lethal mitochondrial cardiomyopathy disorder" (PMID:30283131, doi:10.1038/s41467-018-06250-w; [abstract and mirrors](https://doaj.org/article/5e2c03b6081043e5add48aba3812d059)).
  - The paper describes nine patients from five families with defects in QRSL1, GATB or GATC and a lethal metabolic cardiomyopathy.
  - Patient fibroblasts had combined respiratory chain deficiencies. Charging of mt-tRNAGln and mitochondrial translation were impaired without glutamine and recovered with high glutamine.
  - Lentiviral rescue and yeast homolog models supported pathogenicity.
  - I did not retrieve the specific GATC variants or how many patients carried them.
- **Disease link.** Biallelic GATC variants are listed as combined oxidative phosphorylation deficiency 42 (COXPD42, MIM:617210; see the [dismech entry](https://dismech.monarchinitiative.org/pages/disorders/Combined_oxidative_phosphorylation_deficiency_42.html)). It is a lethal infantile mitochondrial cardiomyopathy. I did not confirm the MIM number independently.

## 2. Localization
The protein has a mitochondrial targeting presequence, which is why UniProt lists it as a precursor. It acts in the mitochondrial matrix, where the mt-tRNA and mitochondrial translation machinery are. The matrix location is inferred from the presequence, the function and the Nagao 2009 mitochondrial biogenesis context. I did not verify direct localization experiments.

## 3. Pathway
GATC acts in mitochondrial tRNA aminoacylation, which feeds mitochondrial translation of the 13 mtDNA-encoded OXPHOS subunits. It has no independent signalling role.

## 4. Suggested GO-level interpretation
These are my inferences, not verified against the existing GOA rows.
- **Molecular function.** The best fit is a contribution to glutamyl-tRNA(Gln) amidotransferase activity (GO:0050567) rather than direct catalysis, because GatC is a non-catalytic scaffold subunit. The `contributes_to` qualifier or a structural-subunit framing is more accurate.
- **Complex.** The glutamyl-tRNA(Gln) amidotransferase complex, mitochondrial.
- **Process.** Mitochondrial glutaminyl-tRNA aminoacylation via transamidation (GO:0070681, "glutaminyl-tRNAGln biosynthesis via transamidation"). Mitochondrial translation is downstream and should be treated as indirect.
- **Cellular component.** Mitochondrion or mitochondrial matrix.
- **Terms to avoid.** Do not use `protein binding`. Avoid broad terms such as "mitochondrial respiratory chain complex assembly" or cardiac development. These are downstream consequences of the translation defect.

## 5. Evidence summary and gaps
| Claim | Evidence | Confidence |
|---|---|---|
| GatC is a GatCAB subunit | Nagao 2009 (PMID:19805282); UniProt GatC family and HAMAP rule MF_03149 | High |
| GatCAB makes Gln-mt-tRNA(Gln) by transamidation | Nagao 2009; Friederich 2018 (PMID:30283131) | High |
| GATC loss of function causes human disease (COXPD42) | Friederich 2018; OMIM/dismech listing | Medium-high |
| Matrix localization | Presequence and inference | Medium |

Open questions, which would need experiments:
- The structural basis of human GatCAB assembly (no human complex structure was found).
- Whether GATC has any role outside tRNA transamidation.
- The biochemical effect of the specific GATC variants. These could be tested by in vitro Gln-tRNA formation assays with recombinant complexes.

## 6. Sources
- Nagao A, Suzuki T, Katoh T, Sakaguchi Y, Suzuki T. PNAS 2009, PMID:19805282. Cited via UniProt and not retrieved.
- Friederich MW et al. Nat Commun 2018, PMID:30283131: [DOAJ record](https://doaj.org/article/5e2c03b6081043e5add48aba3812d059), [DOI link](https://dx.doi.org/10.1038/s41467-018-06250-w), [Cambridge repository](https://www.repository.cam.ac.uk/handle/1810/286571?show=full).
- [NCBI Gene 283459](https://www.ncbi.nlm.nih.gov/gene/283459), listed in the search results and not opened.
- [dismech COXPD42 page](https://dismech.monarchinitiative.org/pages/disorders/Combined_oxidative_phosphorylation_deficiency_42.html).
- UniProt O43716 header, as given in the task.

Before curation, fetch the full texts for both papers and re-quote them verbatim, since the quotes above are paraphrased from search summaries.

## Citations

1. https://doaj.org/article/5e2c03b6081043e5add48aba3812d059
2. https://dismech.monarchinitiative.org/pages/disorders/Combined_oxidative_phosphorylation_deficiency_42.html
3. https://dx.doi.org/10.1038/s41467-018-06250-w
4. https://www.repository.cam.ac.uk/handle/1810/286571?show=full
5. https://www.ncbi.nlm.nih.gov/gene/283459