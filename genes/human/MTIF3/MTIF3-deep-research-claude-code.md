---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:27:52.865330'
end_time: '2026-10-24T04:28:31.500533'
duration_seconds: 38.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MTIF3
  gene_symbol: MTIF3
  uniprot_accession: Q9H2K0
  protein_description: 'RecName: Full=Translation initiation factor IF-3, mitochondrial;
    Short=IF-3(Mt); Short=IF-3Mt; Short=IF3(mt); Short=IF3mt; Flags: Precursor;'
  gene_info: Name=MTIF3; ORFNames=DC38;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the IF-3 family. .
  protein_domains: T_IF-3_C_sf. (IPR036788); T_IF-3_N_sf. (IPR036787); Translation_initiation_fac_3.
    (IPR001288); Translation_initiation_fac_3_N. (IPR019814); IF3_N (PF05198)
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
  total_cost_usd: 0.3164884
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
- **UniProt Accession:** Q9H2K0
- **Protein Description:** RecName: Full=Translation initiation factor IF-3, mitochondrial; Short=IF-3(Mt); Short=IF-3Mt; Short=IF3(mt); Short=IF3mt; Flags: Precursor;
- **Gene Information:** Name=MTIF3; ORFNames=DC38;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the IF-3 family. .
- **Key Domains:** T_IF-3_C_sf. (IPR036788); T_IF-3_N_sf. (IPR036787); Translation_initiation_fac_3. (IPR001288); Translation_initiation_fac_3_N. (IPR019814); IF3_N (PF05198)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MTIF3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MTIF3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MTIF3** (gene ID: MTIF3, UniProt: Q9H2K0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MTIF3 (Q9H2K0), human mitochondrial translation initiation factor 3 (IF3mt)

## Identity check
The symbol, UniProt record and domains all agree. UniProt Q9H2K0 is "Translation initiation factor IF-3, mitochondrial" (gene MTIF3, ORF name DC38), a member of the IF-3 family. Its InterPro domains are the bacterial-type IF3 N-terminal and C-terminal domains (IPR019814, IPR036787, IPR036788, IPR001288). The literature below concerns this same protein, so I found no ambiguity. Sources are in the list at the end.

I ran only two web searches. I did not read the primary papers' full text. Details that come only from search summaries are flagged as secondary.

## Primary function
**MTIF3 is a ribosome-binding translation initiation factor that acts on the mitochondrial small (28S) subunit.** It is the mitochondrial counterpart of bacterial IF3.

- **UniProt function statement.** IF-3 binds the 28S subunit and shifts the equilibrium between 55S ribosomes and their 39S and 28S subunits toward the free subunits. This raises the availability of 28S subunits on which initiation begins. The statement cites the original identification paper, PMID:12095986, "Identification of mammalian mitochondrial translational initiation factor 3 and examination of its role in initiation complex formation with natural mRNAs." That paper is in the UniProt flat file for this protein. I did not retrieve its text, and the web search did not surface it.
- **Not an enzyme.** There is no catalytic activity. MTIF3 acts as a ribosome-associated factor that does the following:
  - It acts as an anti-association factor that dissociates 55S monosomes into 28S and 39S subunits.
  - It destabilises initiator tRNA in the absence of mRNA, which supports fidelity in initiation-complex formation.
  - It may help recruit leaderless mRNAs, a feature of mammalian mitochondrial transcripts.

### Structural evidence
- **Cryo-EM of 28S–IF3mt (2019).** Koripella et al. solved cryo-EM structures of the mammalian 28S subunit bound to human IF3mt at 3.3–3.5 Å ([PMID:30677741](https://pubmed.ncbi.nlm.nih.gov/30677741/), iScience 2019). The reported findings were:
  - Unique contacts between the 28S subunit and the IF3mt N-terminal domain explain its unusually high affinity for 28S.
  - The mitochondria-specific C-terminal extension offers a mechanism for destabilising initiator tRNA when no mRNA is present.
  - The C-terminal domain may help recruit leaderless mRNAs.
  - These points come from the search summary of the abstract. I did not read the full text.
- **Assembly of the initiation complex (2020).** A later study reported two findings ([Nat Commun, s41467-020-16503-2](https://link.springer.com/10.1038/s41467-020-16503-2)):
  - Interactions between the mitochondria-specific protein mS37 and mtIF3 keep the small subunit in a conformation that favours later accommodation of mtIF2.
  - Association of the large subunit is required for initiator tRNA and leaderless mRNA recruitment, which gives a stable initiation complex.
- **Family domain architecture.** The bacterial-like N- and C-terminal domains are connected by a linker. The mitochondrial protein has terminal extensions around this core. A secondary aggregator says it was identified from ESTs as a 278-aa protein ([affinage.wi.mit.edu](https://affinage.wi.mit.edu/gene/MTIF3)). I could not confirm this against the original paper.

## Localization
- MTIF3 is a nuclear-encoded protein that is imported into the mitochondrial matrix, where it works on mitoribosomes. UniProt marks the sequence as a precursor, so it carries a cleavable N-terminal mitochondrial targeting presequence.
- UniProt cites an N-terminome study of the human mitochondrial proteome (PMID:25944712) for presequence processing.
- Its site of action is the mitochondrial matrix, specifically the mitochondrial small ribosomal subunit and the initiation complex.

## Pathway
MTIF3 works in mitochondrial translation initiation. In outline:

1. IF3mt binds free 28S subunits and prevents premature association with 39S.
2. mtIF2 (MTIF2), mRNA and fMet-tRNA join the 28S subunit.
3. IF3mt is released, and the 39S subunit joins to form the 55S initiation complex.

The mitochondrial-DNA-encoded OXPHOS subunits (13 proteins in human) are the products. Loss of MTIF3 therefore mainly affects respiratory chain and ATP synthase biogenesis.

## Phenotypic and disease evidence
These findings concern the consequences of MTIF3 perturbation. They are secondary to the core function.

- **Adipocyte function and obesity genetics.** MTIF3 is a well-replicated obesity-associated locus. Huang et al. reported that rs67785913 is a causal cis-eQTL for MTIF3 expression. The rs67785913 CTCT allele increased MTIF3 expression in CRISPR-edited cells and enhanced transcription in a luciferase assay ([eLife 2023](https://elifesciences.org/articles/84168); [PMC10023155](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10023155/)). MTIF3 deficiency in human white adipocytes had these effects:
  - It reduced mitochondrial respiration and endogenous fatty acid oxidation.
  - It altered expression of mtDNA-encoded genes and proteins.
  - It disturbed OXPHOS complex assembly.
  - After glucose restriction, knockout cells retained more triglycerides than controls.
- **Other models** (from the same search summary, not primary reads):
  - In HepG2 cells, MTIF3 loss decreased translation of the mtDNA-encoded ATP6 mRNA without affecting proliferation.
  - In mice, heart- and skeletal-muscle-specific loss of MTIF3 caused cardiomyopathy. It also produced increased but uncoordinated mitochondrial protein synthesis and loss of specific respiratory complexes.
  - I did not retrieve the primary citations for these, so verify them before using them in a review.
- **No total-deficiency human disease.** The eLife authors note that no human genomic mutations causing total MTIF3 deficiency have been reported.

## Notes for curation
- **Interaction list.** The UniProt INTERACTION list (APOD, BCL2L1, CD47, LDLR and others, all NbExp=3) comes from a single high-throughput IntAct dataset. These are mostly membrane or secreted proteins that do not share a compartment with MTIF3, so they should not support any functional annotation.
- **Core GO-relevant statements.** I would phrase them as follows. The first two are well supported by the structural and UniProt evidence. The third depends on a mechanism that is plausible but not firmly established.
  - Molecular function: mitochondrial small ribosomal subunit (28S) binding, with an anti-association role and a role in positioning initiator tRNA. Avoid "protein binding".
  - Process: mitochondrial translational initiation.
  - Location: mitochondrial matrix, on the 28S subunit and mitoribosome. The core function is hypothesised to be translation initiation factor activity, which is inferred from the bacterial IF3 family and the structures.
- **Verification still needed.** Obtain the full text of PMID:12095986 and PMID:30677741 to check the specific experimental claims before quoting them.

## Sources
- [Koripella et al. 2019, structure of human IF3mt bound to the 28S subunit, PMID:30677741](https://pubmed.ncbi.nlm.nih.gov/30677741/)
- [Nature Communications 2020, mS37–mtIF3 and mtIF2 accommodation](https://link.springer.com/10.1038/s41467-020-16503-2)
- [Huang et al., eLife 2023, MTIF3 eQTL and adipocyte function](https://elifesciences.org/articles/84168)
- [Same study, PMC10023155](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10023155/)
- [Same study, bioRxiv preprint 2022](https://www.biorxiv.org/content/10.1101/2022.10.16.512435.full.pdf)
- [MTIF3 gene summary, affinage.wi.mit.edu (secondary)](https://affinage.wi.mit.edu/gene/MTIF3)
- UniProt Q9H2K0 flat file, local copy in `genes/human/MTIF3/MTIF3-uniprot.txt`. It cites PMID:12095986 and PMID:25944712.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/30677741/
2. https://link.springer.com/10.1038/s41467-020-16503-2
3. https://affinage.wi.mit.edu/gene/MTIF3
4. https://elifesciences.org/articles/84168
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10023155/
6. https://www.biorxiv.org/content/10.1101/2022.10.16.512435.full.pdf