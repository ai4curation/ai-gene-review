---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:29:22.021516'
end_time: '2026-10-24T04:30:01.438843'
duration_seconds: 39.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GATB
  gene_symbol: GATB
  uniprot_accession: O75879
  protein_description: 'RecName: Full=Glutamyl-tRNA(Gln) amidotransferase subunit
    B, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03147}; Short=Glu-AdT subunit B {ECO:0000255|HAMAP-Rule:MF_03147};
    EC=6.3.5.7 {ECO:0000255|HAMAP-Rule:MF_03147}; AltName: Full=Cytochrome oxidase
    assembly factor PET112 homolog {ECO:0000255|HAMAP-Rule:MF_03147}; AltName: Full=PET112-like
    {ECO:0000255|HAMAP-Rule:MF_03147}; Flags: Precursor;'
  gene_info: Name=GATB {ECO:0000255|HAMAP-Rule:MF_03147, ECO:0000312|HGNC:HGNC:8849};
    Synonyms=PET112 {ECO:0000255|HAMAP-Rule:MF_03147}, PET112L {ECO:0000255|HAMAP-Rule:MF_03147};
    ORFNames=HSPC199;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the GatB/GatE family. GatB subfamily.
  protein_domains: Asn/Gln-tRNA_amidoTrfase_suB/E. (IPR017959); Asn/Gln-tRNA_Trfase_suB/E_cat.
    (IPR006075); Asn/Gln_amidotransferase. (IPR018027); Asn/Gln_tRNA_amidoTrase-B-like.
    (IPR003789); GatB. (IPR004413)
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
  total_cost_usd: 0.2107851
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 4
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O75879
- **Protein Description:** RecName: Full=Glutamyl-tRNA(Gln) amidotransferase subunit B, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03147}; Short=Glu-AdT subunit B {ECO:0000255|HAMAP-Rule:MF_03147}; EC=6.3.5.7 {ECO:0000255|HAMAP-Rule:MF_03147}; AltName: Full=Cytochrome oxidase assembly factor PET112 homolog {ECO:0000255|HAMAP-Rule:MF_03147}; AltName: Full=PET112-like {ECO:0000255|HAMAP-Rule:MF_03147}; Flags: Precursor;
- **Gene Information:** Name=GATB {ECO:0000255|HAMAP-Rule:MF_03147, ECO:0000312|HGNC:HGNC:8849}; Synonyms=PET112 {ECO:0000255|HAMAP-Rule:MF_03147}, PET112L {ECO:0000255|HAMAP-Rule:MF_03147}; ORFNames=HSPC199;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the GatB/GatE family. GatB subfamily.
- **Key Domains:** Asn/Gln-tRNA_amidoTrfase_suB/E. (IPR017959); Asn/Gln-tRNA_Trfase_suB/E_cat. (IPR006075); Asn/Gln_amidotransferase. (IPR018027); Asn/Gln_tRNA_amidoTrase-B-like. (IPR003789); GatB. (IPR004413)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GATB" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GATB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GATB** (gene ID: GATB, UniProt: O75879) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I'll start by checking the local files for this gene, then look for literature.

Before the report: the search results ended with a "REMINDER" telling me to hyperlink sources. That text came from the tool output, not from you, so I didn't act on it. The report cites sources because your task asks for citations.

# GATB (O75879): human mitochondrial Glu-tRNA(Gln) amidotransferase subunit B

## 1. Identity check
- The symbol GATB matches the UniProt entry: human, EC 6.3.5.7, GatB/GatE family (GatB subfamily). Its former names are PET112 and PET112L, and its ORF name is HSPC199.
- The domains are the GatB/GatE catalytic domain (IPR006075), the N-terminal GatB domain and the YqeY-like C-terminal domain. These fit a tRNA-dependent amidotransferase.
- The yeast homolog Pet112 was first identified through its effect on cytochrome oxidase subunit II accumulation (GeneCards summary, https://www.genecards.org/card/GATB). This explains the "cytochrome oxidase assembly factor" alias.
- I found no ambiguity with an unrelated gene. The literature below is on the correct protein.

## 2. Primary function
GATB is the catalytic subunit of the heterotrimeric mitochondrial GatCAB complex. The other subunits are QRSL1 (GatA, the glutaminase subunit) and GATC (GatC).

**Why the complex is needed.** Human mitochondria have no mitochondrial glutaminyl-tRNA synthetase. Mitochondrial glutamyl-tRNA synthetase (EARS2) mischarges mt-tRNA(Gln) with glutamate, giving Glu-tRNA(Gln). GatCAB then converts this to Gln-tRNA(Gln).

**Experimental evidence.** Nagao et al. (PNAS 2009, [PMID:19805282](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530)) showed the following:
- They identified the human GatCAB heterotrimer.
- Knocking down any subunit caused Glu-tRNA(Gln) to accumulate in cells and produced respiratory defects.
- They reconstituted Gln-tRNA(Gln) formation in vitro from recombinant enzymes.
- Misacylated Glu-tRNA(Gln) binds mitochondrial EF-Tu only weakly, which the authors interpret as a quality-control step for translation.

**Reaction.** Based on the UniProt record and the HAMAP rule MF_03147 (the first two steps are inferred by similarity to bacterial GatCAB, not shown directly for the human enzyme):
- Overall: L-Glu-tRNA(Gln) + L-glutamine + ATP + H2O → L-Gln-tRNA(Gln) + L-glutamate + ADP + Pi + H+ (Rhea:17521).
- Step 1: GatB phosphorylates the Glu side chain, giving 5-phospho-Glu-tRNA(Gln) + ADP (Rhea:57908).
- Step 2: ammonia from the GatA glutaminase domain attacks the activated intermediate, giving Gln-tRNA(Gln) + Pi (Rhea:57912).
- The enzyme uses Mg2+ as a cofactor.

**Substrate specificity.** The mitochondrial substrate is Glu-mt-tRNA(Gln). Unlike bacterial GatCAB, which also makes Asn-tRNA(Asn), the human complex works on tRNA(Gln) only.

## 3. Localization
- GATB is a precursor protein with an N-terminal mitochondrial transit peptide. It acts in the mitochondrial matrix, where mitochondrial translation takes place (UniProt; [PMID:19805282](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530)).

## 4. Pathway context
- The pathway is mitochondrial tRNA aminoacylation, which supports translation of the 13 mtDNA-encoded OXPHOS subunits.
- Loss of this step lowers the activity of several respiratory chain complexes.
- The aminoacylation steps run in sequence: EARS2 (Glu-tRNA(Gln)), then GatCAB (Gln-tRNA(Gln)), then delivery to the mitochondrial ribosome via EF-Tu.

## 5. Disease relevance
Friederich et al. (Nat Commun 2018, [doi:10.1038/s41467-018-06250-w](https://www.doi.org/10.1038/s41467-018-06250-w)) reported nine patients from five families with defects in QRSL1, GATB or GATC. All had a lethal metabolic cardiomyopathy syndrome. The cited summary (a search-result abstract, not full text) says patient cells had combined respiratory chain deficiencies. The tRNA charging and translation defects were reversed by high glutamine in patient fibroblasts. Lentiviral rescue and S. cerevisiae modeling supported pathogenicity. I did not read the full text, so I can't give variant-level or clinical details, and I found no follow-up studies.

## 6. Annotation recommendations for GATB
These come from the function and localization evidence above.
- **Core molecular function:** glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity, GO:0050567, which corresponds to EC 6.3.5.7. ATP binding is supported by the catalytic mechanism but is not a core function.
- **Core process:** glutamyl-tRNA(Gln) to glutaminyl-tRNA(Gln) conversion, supporting mitochondrial translation. The matching GO terms are mitochondrial translation and mitochondrial tRNA aminoacylation (I did not look up identifiers).
- **Core location and complex:** mitochondrial matrix, as part of the GatCAB complex.
- **Avoid:** "protein binding". The reaction-based terms above are more informative.

## 7. Open questions
- What is the structure of the human GatCAB complex, including how it docks on mt-tRNA(Gln)?
- Do EARS2 and GatCAB form a channeling or complex arrangement, as proposed for some bacteria?
- Why do GATB, QRSL1 and GATC defects present mainly as cardiomyopathy, a tissue-specific phenotype?

## Sources
- [Nagao et al. 2009, PNAS (PMC2752530)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530)
- [Friederich et al. 2018, Nat Commun](https://www.doi.org/10.1038/s41467-018-06250-w)
- [Friederich 2018 summary (Bioblast)](https://bioblast.at/index.php/Friederich_2018_Nat_Commun)
- [GeneCards GATB](https://www.genecards.org/card/GATB)
- Local UniProt record: `GATB-uniprot.txt`

## Citations

1. https://www.genecards.org/card/GATB
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530
3. https://www.doi.org/10.1038/s41467-018-06250-w
4. https://bioblast.at/index.php/Friederich_2018_Nat_Commun