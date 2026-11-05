---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:17:29.681670'
end_time: '2026-10-14T23:18:04.364566'
duration_seconds: 34.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GTPBP3
  gene_symbol: GTPBP3
  uniprot_accession: Q969Y2
  protein_description: 'RecName: Full=5-taurinomethyluridine-[tRNA] synthase subunit
    GTPB3, mitochondrial {ECO:0000303|PubMed:29390138}; EC=3.6.1.- {ECO:0000269|PubMed:29390138,
    ECO:0000269|PubMed:33619562}; AltName: Full=GTP-binding protein 3 {ECO:0000303|PubMed:12370316};
    AltName: Full=Mitochondrial GTP-binding protein 1; AltName: Full=tRNA modification
    GTPase GTPBP3, mitochondrial; Flags: Precursor;'
  gene_info: Name=GTPBP3 {ECO:0000312|HGNC:HGNC:14880}; Synonyms=MTGP1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class TrmE-Era-EngA-EngB-Septin-like
  protein_domains: G_TrmE. (IPR031168); GTP-bd. (IPR006073); GTP-bd_TrmE_N. (IPR018948);
    GTPase_MnmE. (IPR004520); MnmE_dom2. (IPR027368)
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
  total_cost_usd: 0.19680450000000002
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
- **UniProt Accession:** Q969Y2
- **Protein Description:** RecName: Full=5-taurinomethyluridine-[tRNA] synthase subunit GTPB3, mitochondrial {ECO:0000303|PubMed:29390138}; EC=3.6.1.- {ECO:0000269|PubMed:29390138, ECO:0000269|PubMed:33619562}; AltName: Full=GTP-binding protein 3 {ECO:0000303|PubMed:12370316}; AltName: Full=Mitochondrial GTP-binding protein 1; AltName: Full=tRNA modification GTPase GTPBP3, mitochondrial; Flags: Precursor;
- **Gene Information:** Name=GTPBP3 {ECO:0000312|HGNC:HGNC:14880}; Synonyms=MTGP1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class TrmE-Era-EngA-EngB-Septin-like
- **Key Domains:** G_TrmE. (IPR031168); GTP-bd. (IPR006073); GTP-bd_TrmE_N. (IPR018948); GTPase_MnmE. (IPR004520); MnmE_dom2. (IPR027368)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GTPBP3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GTPBP3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GTPBP3** (gene ID: GTPBP3, UniProt: Q969Y2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GTPBP3 (Q969Y2), human: research report

## Identity check

The symbol, organism and protein description all match. UniProt Q969Y2 is human GTPBP3, the "5-taurinomethyluridine-[tRNA] synthase subunit GTPB3, mitochondrial" (also called tRNA modification GTPase GTPBP3 or MTGP1). It belongs to the TrmE-Era-EngA-EngB-Septin-like TRAFAC GTPase class. Its domains are G_TrmE, GTPase_MnmE and the MnmE N-terminal and domain-2 regions. The literature below concerns this same protein, so there is no ambiguity.

Some details come only from search-result summaries, not from full-text reading of every paper. I flag these below. Quoted passages should be checked against the cached `publications/PMID_*.md` files before they are used as `supporting_text`.

## Primary function

GTPBP3 is the human ortholog of bacterial MnmE (also called TrmE). It works with MTO1, the ortholog of MnmG/GidA, to modify the wobble uridine (U34) of mitochondrial tRNAs. In human mitochondria the product is 5-taurinomethyluridine (τm5U), made by attaching a methylene-taurine group to C5 of the uracil. Yeast and *E. coli* make the glycine-containing analog (cmnm5U) instead.

- **Reaction.** GTPBP3 and MTO1 transform U34 into τm5U34 in tRNA. Reactome annotates this as a single event, [R-HSA-6787403](https://reactome.org/content/detail/R-HSA-6787403). The bacterial paradigm is that the MnmE/MnmG complex uses GTP hydrolysis, a one-carbon donor (methylene-tetrahydrofolate) and the amino-acid substrate, here taurine. The mechanism is still not fully understood.
- **Substrates.** The five human mitochondrial tRNAs carrying τm5U34 are tRNALys, tRNAGlu, tRNAGln, tRNALeu(UUR) and tRNATrp. This follows from the Kopajtich et al. description summarized below and is consistent with the literature. Check the exact list against the cached paper.
- **Enzyme activity.** The UniProt entry annotates EC 3.6.1.- (GTPase activity), citing [PMID:29390138](https://pmc.ncbi.nlm.nih.gov/articles/PMC5829720) and [PMID:33619562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7969015).
  - Earlier work found that two abundant GTPBP3 isoforms bind guanine nucleotides with moderate affinity but hydrolyze GTP about 100 times more slowly than MnmE. The N-terminal domain mediates potassium-independent dimerization.
  - Peng and colleagues (Nucleic Acids Research, 2021, PMID:33619562) identified the mature form of the protein. They showed it is an active GTPase in vitro and is needed for tRNA modification in vivo. The isolated G domain and an N-terminal-truncated mutant hydrolyzed GTP poorly, with high Km values.
- **Cooperation with MTO1.** The two proteins act together in the same pathway, and GTPBP3 is not a stand-alone methyltransferase. The mechanistic details in this section come mainly from MnmE/MnmG homology and the summaries of the 2021 paper.

## Evidence from patients and cells

- **Kopajtich et al., AJHG 2015.** Eleven individuals from nine families carried GTPBP3 mutations. All had lactic acidosis, and nine developed hypertrophic cardiomyopathy. Most also had neurological symptoms, with MRI involvement of the thalamus, putamen and brainstem resembling Leigh syndrome. This differs from MTO1 mutation carriers. Cells showed a severe mitochondrial translation defect, consistent with loss of τm5U in the five tRNAs. I did not retrieve the PMID, so look it up before citing.
- **PMID:29390138 (2018).** Patient cells with GTPBP3 mutations had very little τm5U34. Taurine starvation lowered τm5U levels in cultured cells and animal tissues, which supports taurine as the physiological substrate. This is the source of UniProt's catalytic annotation. Zebrafish *gtpbp3* knockout models were also used in this work.
- **Interpretation.** The cardiomyopathy and lactic acidosis phenotype matches that of MTO1 deficiency, which is also linked to hypertrophic cardiomyopathy. The more neurological, Leigh-like presentation in GTPBP3 patients suggests GTPBP3 has some non-redundant role. This is an inference from the clinical comparison and has not been tested directly.

## Localization and pathway

- **Where it acts.** GTPBP3 is a mitochondrial matrix protein, as the UniProt name "mitochondrial" and the precursor flag indicate. The mature form lacks the N-terminal presequence (PMID:33619562). It modifies tRNAs there, so the modification step is part of mitochondrial tRNA processing and wobble-uridine modification.
- **Pathway.** Its pathway is mitochondrial tRNA wobble modification: tRNA thio-modification and the U34 → τm5U34 step, followed in some tRNAs by 2-thiolation through the separate MTU1/TRMU enzyme. The τm5U modification supports accurate decoding of NNA/NNG codons in mitochondrial translation. Loss of it reduces translation of the mtDNA-encoded OXPHOS subunits and impairs oxidative phosphorylation.

## Suggested GO-level summary

- **Molecular function:** tRNA wobble uridine modification enzyme activity, forming τm5U34. For the GTP-hydrolysing part, annotate GTPase activity and GTP binding. Avoid a generic "protein binding" term.
- **Biological process:** mitochondrial tRNA modification and wobble uridine modification, with mitochondrial translation as a downstream context. The MTO1 partnership could be captured as a complex annotation.
- **Cellular component:** mitochondrion (matrix).

## Caveats and open questions

- This report rests on two web searches and the summaries they returned, not on full-text review of the primary papers. The 2015 AJHG details, the exact tRNA list, and any quantitative kinetics need checking against the primary papers.
- The bacterial MnmE/MnmG mechanism is the model for the reaction scheme. It was not demonstrated for the human enzymes in the sources I retrieved.
- The contribution of GTP hydrolysis cycling to catalysis is still unresolved.
- Whether GTPBP3 has substrate-recognition roles distinct from MTO1 could be tested experimentally.

## Sources

- [Peng et al. 2021, The human tRNA taurine modification enzyme GTPBP3 is an active GTPase linked to mitochondrial diseases (PMC7969015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7969015)
- [PMC5829720, 2018 study of τm5U34, taurine dependence and the zebrafish model (PMID:29390138)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5829720)
- [Reactome R-HSA-6787403, GTPBP3 and MTO1 transform uridine-34 yielding 5-taurinomethyluridine-34 in tRNA](https://reactome.org/content/detail/R-HSA-6787403)
- [Kopajtich et al. 2015 and related records (Cardiff ORCA)](https://orca.cardiff.ac.uk/id/eprint/118889/)
- [PMC2593442, earlier characterization of GTPBP3 isoforms](https://pmc.ncbi.nlm.nih.gov/articles/PMC2593442)
- [PMC10415153](https://pmc.ncbi.nlm.nih.gov/articles/PMC10415153)

## Citations

1. https://reactome.org/content/detail/R-HSA-6787403
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC5829720
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC7969015
4. https://orca.cardiff.ac.uk/id/eprint/118889/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC2593442
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC10415153