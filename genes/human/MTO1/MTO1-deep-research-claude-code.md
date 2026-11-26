---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:27:52.773812'
end_time: '2026-10-24T04:28:39.649860'
duration_seconds: 46.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MTO1
  gene_symbol: MTO1
  uniprot_accession: Q9Y2Z2
  protein_description: 'RecName: Full=5-taurinomethyluridine-[tRNA] synthase subunit
    MTO1, mitochondrial {ECO:0000303|PubMed:29390138}; AltName: Full=Mitochondrial
    tRNA translation optimization 1 {ECO:0000303|PubMed:33619562}; AltName: Full=Protein
    MTO1 homolog, mitochondrial {ECO:0000303|PubMed:12011058}; Flags: Precursor;'
  gene_info: Name=MTO1 {ECO:0000312|HGNC:HGNC:19261}; ORFNames=CGI-02;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the MnmG family. .
  protein_domains: FAD/NAD-bd_sf. (IPR036188); GIDA_C_N. (IPR049312); MnmG-rel. (IPR002218);
    MnmG-rel_CS. (IPR020595); MnmG_C. (IPR026904)
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
  total_cost_usd: 0.3112657
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
- **UniProt Accession:** Q9Y2Z2
- **Protein Description:** RecName: Full=5-taurinomethyluridine-[tRNA] synthase subunit MTO1, mitochondrial {ECO:0000303|PubMed:29390138}; AltName: Full=Mitochondrial tRNA translation optimization 1 {ECO:0000303|PubMed:33619562}; AltName: Full=Protein MTO1 homolog, mitochondrial {ECO:0000303|PubMed:12011058}; Flags: Precursor;
- **Gene Information:** Name=MTO1 {ECO:0000312|HGNC:HGNC:19261}; ORFNames=CGI-02;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the MnmG family. .
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); GIDA_C_N. (IPR049312); MnmG-rel. (IPR002218); MnmG-rel_CS. (IPR020595); MnmG_C. (IPR026904)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MTO1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MTO1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MTO1** (gene ID: MTO1, UniProt: Q9Y2Z2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MTO1 (human, UniProt Q9Y2Z2): research report

**Method and limits.** I ran two web searches, and the text of most papers was not available to me. Statements marked [UniProt] come from the record you supplied. Citations are given by author, year and journal, with a PMID only where UniProt's own record supplies it. A few older primary papers are cited from memory and flagged "verify". Check those before quoting them in a review file.

## 1. Identity check

The symbol, organism and domain data all agree.

- MTO1 (alias CGI-02) is the human mitochondrial MnmG-family protein.
- The UniProt recommended name is "5-taurinomethyluridine-[tRNA] synthase subunit MTO1, mitochondrial".
- The domains are FAD/NAD-binding superfamily, GidA C-terminal and N-terminal, and MnmG-related. These are the hallmarks of bacterial MnmG/GidA [UniProt].
- No ambiguity with another gene was found.

## 2. Primary function

MTO1 is a subunit of the mitochondrial tRNA wobble-uridine modification enzyme. It forms a heterocomplex with GTPBP3, the MnmE homolog. Together they install 5-taurinomethyl (τm5) on U34.

- **Reaction.** The complex converts U34 to τm5U34 in mitochondrial tRNAs. 5,10-methylene-tetrahydrofolate (CH2-THF) supplies the one-carbon unit, and taurine is the amino-containing substituent. FAD and NADH are expected to be used, by analogy with bacterial MnmG [Asano et al. 2018, NAR, PMID:29390138; Peng et al. 2021, NAR, PMID:33619562].
  - The 2018 study reported that 5,10-methylene-THF and taurine are the metabolic substrates for τm5U formation catalysed by MTO1 and GTPBP3. GTPBP3-knockout cells showed respiratory defects and reduced mitochondrial translation. Taurine starvation lowered τm5U levels and produced cmnm5U (glycine in place of taurine). This shows the pathway responds to metabolite supply. Source: [Asano 2018 NAR](https://academic.oup.com/nar/article/46/4/1565/4829701) and [PMC5829720](https://pmc.ncbi.nlm.nih.gov/articles/PMC5829720).
  - Peng et al. 2021 reported that GTPBP3 and MTO1 cooperate in τm5U biosynthesis and that human GTPBP3 is an active GTPase in vitro. See [PMC7969015](https://pmc.ncbi.nlm.nih.gov/articles/PMC7969015). The PMC link is from the search result, and I did not confirm that it is this paper.
- **Substrates.** The modification occurs at the wobble position of the five mt-tRNAs that carry a 2-thio-capable U34 and read two-codon NNR boxes: mt-tRNA^Lys, ^Glu, ^Gln, ^Leu(UUR) and ^Trp. This is reported in the GTPBP3 patient paper [Kopajtich et al., AJHG 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4259976).
  - For τm5U34 in Leu(UUR) and Trp, the earlier work is Suzuki and colleagues' mass-spectrometry studies of bovine mt-tRNAs (verify citation).
  - For Lys, Glu and Gln, U34 also carries a 2-thio group (τm5s2U), added by the separate TRMU enzyme. This is also from memory (verify).
- **Biological role.** The τm5 group stabilizes codon–anticodon pairing at the wobble position, and for UUG and UGA/UGG it supports decoding. It is needed for efficient translation of the 13 mtDNA-encoded OXPHOS subunits.
  - Loss of the modification reduces mitochondrial translation and respiratory-chain activity.

## 3. Localization

MTO1 has an N-terminal mitochondrial targeting presequence, so the UniProt entry is a "Precursor" [UniProt]. It acts in the mitochondrial matrix on mt-tRNAs after transcription and processing.

- The 2002 identification of human MTO1 as a homolog of the yeast nuclear modifier gene (Li, Li, Lin & Guan, JBC; PMID 12011058 per UniProt's AltName citation) described it as mitochondrial.
- No nuclear or cytosolic function is established.

## 4. Pathway context

- **Upstream inputs.** Taurine comes from cellular metabolism and import. CH2-THF comes from mitochondrial one-carbon metabolism (the SHMT2/MTHFD2 axis). The GTPBP3 partner provides the GTPase module.
- **Downstream output.** The modified tRNAs support mitochondrial translation and so OXPHOS complexes I, III, IV and V.
- **Interaction with other modifications.** The Lys, Glu and Gln tRNAs also need TRMU for 2-thiolation. The modifications are therefore related but catalysed by separate enzymes.

## 5. Evolution and structure

- MTO1 is the orthologue of bacterial MnmG/GidA, and GTPBP3 is the orthologue of MnmE/TrmE. In bacteria the MnmE–MnmG complex forms cmnm5U or, using ammonium, nm5U at U34.
- The mitochondrial enzyme uses taurine instead of glycine. This is the key functional difference from bacteria, shown experimentally by Asano et al. 2018.
- The proteins carry an FAD-binding Rossmann-like domain (the flavin-dependent oxidoreductase fold) and the MnmG C-terminal helical domains [UniProt InterPro entries].

## 6. Disease

- **MTO1 deficiency (COXPD10).** The autosomal-recessive disorder is combined oxidative phosphorylation deficiency 10. Its typical features are hypertrophic cardiomyopathy and lactic acidosis, with variable neurological involvement.
  - Ghezzi et al., AJHG 2012, reported the first cases with hypertrophic cardiomyopathy and lactic acidosis (verify).
  - Baruffini et al. 2013 added a yeast model and further cases (verify).
- **Cell biology of patients.** Patient cells show reduced τm5U, reduced mitochondrial translation and decreased respiratory-chain activities (complex I and IV most affected).
  - The GTPBP3 paper notes that MTO1 patients present with hypertrophic cardiomyopathy and lactic acidosis, with impaired mitochondrial translation and reduced respiratory chain activities. GTPBP3 patients are more often neurological, with Leigh-like MRI changes. Source: [Kopajtich 2014 AJHG](https://pmc.ncbi.nlm.nih.gov/articles/PMC4259976).
- **Mitochondrial deafness link.** The yeast MTO1 gene was originally identified as a nuclear modifier of the m.1555A>G 12S rRNA deafness mutation (Li et al. 2002, as above). Human MTO1 variants have also been proposed as modifiers of this phenotype. This association is weaker than the COXPD10 evidence.

## 7. Suggested GO-relevant summary

- **Molecular function.** tRNA wobble uridine modification enzyme activity, specifically 5-taurinomethyluridine-[tRNA] synthase activity.
  - Term IDs need checking in OLS or QuickGO before use. A tRNA binding term and FAD binding are plausible as secondary functions.
  - The activity is performed as a complex with GTPBP3, so the "subunit" wording in the UniProt name matters.
- **Biological process.** Mitochondrial tRNA wobble uridine modification (tRNA modification in mitochondria), and by extension the support of mitochondrial translation. Treat the translation term as downstream and non-core.
- **Cellular component.** Mitochondrial matrix, mitochondrion. Whether to add a tRNA-modification-complex term for the MTO1–GTPBP3 heterocomplex needs checking against the GO ontology.
- **Cautions for curation.**
  - Do not annotate "protein binding" for the GTPBP3 interaction.
  - Do not annotate cardiac phenotypes as processes. They are consequences of the translation defect.
  - Following your project's `NEW`-term rules, mitochondrial translation is something MTO1 supports through its tRNA product. It does not perform ribosomal translation steps itself.

## 8. Gaps and suggested experiments

- Direct structural data for the human MTO1–GTPBP3 complex, and how GTP hydrolysis and FAD/NADH are coupled to catalysis.
- The tissue-specific basis for the cardiomyopathy versus neurological split between MTO1 and GTPBP3 patients. Taurine and CH2-THF supply in heart and brain could be tested.
- Whether MTO1 has activity on any nonmitochondrial RNA. There is no current evidence.

## Sources

- [Asano et al. 2018, NAR 46:1565 (PMID:29390138)](https://academic.oup.com/nar/article/46/4/1565/4829701), also [PMC5829720](https://pmc.ncbi.nlm.nih.gov/articles/PMC5829720)
- Peng et al. 2021, NAR (PMID:33619562; link found, not confirmed to be this paper): [PMC7969015](https://pmc.ncbi.nlm.nih.gov/articles/PMC7969015)
- [Kopajtich et al. 2014, AJHG, GTPBP3 mutations (PMC4259976)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4259976)
- UniProt Q9Y2Z2 record (as supplied in the task)
- From memory, not retrieved here (verify): Li et al. 2002 JBC (PMID:12011058, from UniProt's AltName citation), Ghezzi et al. 2012 AJHG, Baruffini et al. 2013, and the Suzuki-lab mt-tRNA modification papers.

## Citations

1. https://academic.oup.com/nar/article/46/4/1565/4829701
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC5829720
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC7969015
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC4259976