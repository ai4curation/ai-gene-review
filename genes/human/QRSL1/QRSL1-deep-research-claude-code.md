---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:28:44.696069'
end_time: '2026-10-24T04:29:16.952595'
duration_seconds: 32.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: QRSL1
  gene_symbol: QRSL1
  uniprot_accession: Q9H0R6
  protein_description: 'RecName: Full=Glutamyl-tRNA(Gln) amidotransferase subunit
    A, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03150}; Short=Glu-AdT subunit A {ECO:0000255|HAMAP-Rule:MF_03150};
    Short=hGatA {ECO:0000303|PubMed:19805282}; EC=3.5.1.2 {ECO:0000255|HAMAP-Rule:MF_03150};
    AltName: Full=Glutaminyl-tRNA synthase-like protein 1 {ECO:0000255|HAMAP-Rule:MF_03150};'
  gene_info: Name=QRSL1 {ECO:0000255|HAMAP-Rule:MF_03150};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the amidase family. GatA subfamily.
  protein_domains: Amidase. (IPR000120); Amidase_dom. (IPR023631); AS_sf. (IPR036928);
    GatA. (IPR004412); Amidase (PF01425)
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
  total_cost_usd: 0.19544460000000002
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 5
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9H0R6
- **Protein Description:** RecName: Full=Glutamyl-tRNA(Gln) amidotransferase subunit A, mitochondrial {ECO:0000255|HAMAP-Rule:MF_03150}; Short=Glu-AdT subunit A {ECO:0000255|HAMAP-Rule:MF_03150}; Short=hGatA {ECO:0000303|PubMed:19805282}; EC=3.5.1.2 {ECO:0000255|HAMAP-Rule:MF_03150}; AltName: Full=Glutaminyl-tRNA synthase-like protein 1 {ECO:0000255|HAMAP-Rule:MF_03150};
- **Gene Information:** Name=QRSL1 {ECO:0000255|HAMAP-Rule:MF_03150};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the amidase family. GatA subfamily.
- **Key Domains:** Amidase. (IPR000120); Amidase_dom. (IPR023631); AS_sf. (IPR036928); GatA. (IPR004412); Amidase (PF01425)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "QRSL1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'QRSL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **QRSL1** (gene ID: QRSL1, UniProt: Q9H0R6) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# QRSL1 (Q9H0R6): mitochondrial GatA subunit of the Glu-tRNA(Gln) amidotransferase (human)

## 0. Identity check
The symbol, UniProt record and literature agree. QRSL1 is human GatA, the catalytic amidase subunit of the mitochondrial GatCAB complex. It belongs to the amidase family, GatA subfamily, and carries the Amidase domain (PF01425, IPR000120) and the GatA signature (IPR004412). The 2009 paper that defined the human complex calls the protein hGatA, which is the name used in the UniProt record (PMID:19805282). I found no conflicting literature for a different gene under this symbol. I did not read the full text of the papers cited below, so the points taken from them rest on abstracts and search summaries, not on checked quotations.

## 1. Primary function
**Reaction (EC 3.5.1.2 per UniProt/HAMAP):** the enzyme performs the second step of an indirect route to Gln-tRNA(Gln) in mitochondria.
- Mitochondria have no glutaminyl-tRNA synthetase. Mitochondrial GluRS (EARS2) misacylates mt-tRNA(Gln) with glutamate, giving Glu-tRNA(Gln).
- GatCAB then converts Glu-tRNA(Gln) to Gln-tRNA(Gln) by ATP-dependent transamidation: Glu-tRNA(Gln) + ATP + glutamine → Gln-tRNA(Gln) + glutamate + ADP + Pi.
- GatA hydrolyses glutamine to ammonia. The ammonia is channelled to GatB, which activates the misacylated glutamate with ATP and then amidates it.
- Nagao et al. (2009) identified hGatCAB, showed that GluRS misacylates mt-tRNA(Gln), and reconstituted Gln-tRNA(Gln) formation in vitro with recombinant enzymes (PMID:19805282; [PMC2752530](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530)). The same paper reported:
  - Knockdown of hGatCAB subunits caused accumulation of Glu-charged tRNA and respiration defects.
  - The misacylated tRNA binds weakly to mtEF-Tu, which the authors interpret as a quality-control step for translational accuracy.
- The other two subunits are GATB (PET112) and GATC. Together with QRSL1 they form a heterotrimer.
- The amidase fold, the catalytic Ser-Ser-Lys triad typical of the family, and the bacterial GatCAB mechanism are my own inference from the family assignment. I did not check them against a structure or publication here.

**Substrate specificity:** the substrate is mt-tRNA(Gln) misacylated with Glu. Human mitochondria use this route for the single mt-tRNA(Gln) species. Glutamine is the nitrogen donor.

## 2. Localization
The enzyme is a mitochondrial matrix protein. The "mitochondrial" and "GatCAB complex" annotations come from the 2009 characterisation in human cells (PMID:19805282). It acts in the matrix, next to the mitochondrial translation machinery.

## 3. Pathway context
It sits in mitochondrial translation. EARS2 misacylates tRNA(Gln), GatCAB corrects it, and mtEF-Tu delivers the correct Gln-tRNA(Gln) to the ribosome. This makes GatCAB necessary for translating the mtDNA-encoded OXPHOS subunits, and loss of it reduces respiratory-chain function.

## 4. Disease and in vivo evidence
Friederich et al. 2018, *Nat Commun* (doi:10.1038/s41467-018-06250-w; I could not confirm the PMID), reported:
- Nine patients from five families with defects in a GatCAB subunit (QRSL1, GATB or GATC).
- A lethal metabolic cardiomyopathy syndrome in these patients.
- Combined respiratory chain enzyme deficiencies.
- Deficient mt-tRNA(Gln) charging and mitochondrial translation in patient fibroblasts without glutamine.
- Confirmation of pathogenicity by lentiviral rescue and by yeast modelling.
- Sources: [Bioblast summary](https://bioblast.at/index.php/Friederich_2018_Nat_Commun); [related title](https://bohrium.dp.tech/paper/arxiv/23929671).

NCBI links QRSL1 to combined oxidative phosphorylation deficiency 40 ([NCBI Gene 76563](https://https.ncbi.nlm.nih.gov/gene/76563)).

## 5. Evidence summary
| Claim | Evidence |
|---|---|
| Part of the mitochondrial GatCAB complex that makes Gln-tRNA(Gln) | Experimental: reconstitution and knockdown (PMID:19805282) |
| Amidase and glutamine-hydrolysing activity | Inferred from family and domain assignment (UniProt/HAMAP) |
| Required for mitochondrial translation in humans | Patient and rescue data (Friederich 2018) |

## 6. Annotation guidance
- Likely to be well supported: tRNA aminoacylation for mitochondrial translation (or glutaminyl-tRNA(Gln) biosynthesis via transamidation); the glutamyl-tRNA(Gln) amidotransferase complex; mitochondrial matrix localization.
- Avoid "protein binding" annotations. The function is a specific enzyme activity (glutaminyl-tRNA(Gln) amidotransferase activity).

## Sources
- [Nagao et al. 2009 PNAS, PMID:19805282](https://ncbi.nlm.nih.gov/pubmed/19805282/), [PMC2752530](https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530)
- [Friederich et al. 2018 Nat Commun](https://bioblast.at/index.php/Friederich_2018_Nat_Commun)
- [NCBI Gene 76563](https://https.ncbi.nlm.nih.gov/gene/76563)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC2752530
2. https://bioblast.at/index.php/Friederich_2018_Nat_Commun
3. https://bohrium.dp.tech/paper/arxiv/23929671
4. https://https.ncbi.nlm.nih.gov/gene/76563
5. https://ncbi.nlm.nih.gov/pubmed/19805282/