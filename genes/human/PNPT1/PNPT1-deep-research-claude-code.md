---
provider: claude_code
model: claude-sonnet-5-5
cached: true
start_time: '2026-10-14T23:21:32.119278'
end_time: '2026-10-14T23:21:32.121943'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PNPT1
  gene_symbol: PNPT1
  uniprot_accession: Q8TCS8
  protein_description: 'RecName: Full=Polyribonucleotide nucleotidyltransferase 1,
    mitochondrial {ECO:0000305}; EC=2.7.7.8 {ECO:0000269|PubMed:18083836}; AltName:
    Full=3''-5'' RNA exonuclease OLD35; AltName: Full=PNPase old-35; AltName: Full=Polynucleotide
    phosphorylase 1; Short=PNPase 1; AltName: Full=Polynucleotide phosphorylase-like
    protein; Flags: Precursor;'
  gene_info: Name=PNPT1 {ECO:0000312|HGNC:HGNC:23166}; Synonyms=PNPASE;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the polyribonucleotide nucleotidyltransferase
  protein_domains: ExoRNase_PH_dom1. (IPR001247); ExoRNase_PH_dom2. (IPR015847); ExoRNase_PH_dom2_sf.
    (IPR036345); KH_dom. (IPR004087); KH_dom_type_1. (IPR004088)
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
  - claude-sonnet-5-5
  num_turns: 1
  total_cost_usd: 0.1605322
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8TCS8
- **Protein Description:** RecName: Full=Polyribonucleotide nucleotidyltransferase 1, mitochondrial {ECO:0000305}; EC=2.7.7.8 {ECO:0000269|PubMed:18083836}; AltName: Full=3'-5' RNA exonuclease OLD35; AltName: Full=PNPase old-35; AltName: Full=Polynucleotide phosphorylase 1; Short=PNPase 1; AltName: Full=Polynucleotide phosphorylase-like protein; Flags: Precursor;
- **Gene Information:** Name=PNPT1 {ECO:0000312|HGNC:HGNC:23166}; Synonyms=PNPASE;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the polyribonucleotide nucleotidyltransferase
- **Key Domains:** ExoRNase_PH_dom1. (IPR001247); ExoRNase_PH_dom2. (IPR015847); ExoRNase_PH_dom2_sf. (IPR036345); KH_dom. (IPR004087); KH_dom_type_1. (IPR004088)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PNPT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PNPT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PNPT1** (gene ID: PNPT1, UniProt: Q8TCS8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PNPT1 (human PNPase; UniProt Q8TCS8): research report

**Provenance note.** I wrote this from background knowledge and the UniProt header you supplied. I ran no live searches and did not check any PMID against PubMed or the local `publications/` cache. Citations are given as author, year and topic. Only PMID:18083836 comes from the UniProt record. Verify every other reference with `just fetch-gene` or PubMed before using it in a review YAML. No verbatim `supporting_text` quotes are supplied, so none can pass the quote validator yet.

## 1. Identity check

- The gene symbol PNPT1 (HGNC:23166) matches the supplied record: polyribonucleotide nucleotidyltransferase 1, mitochondrial (PNPase, old-35), EC 2.7.7.8.
- The organism is *Homo sapiens*.
- The domains match the family: two RNase PH-like core domains (IPR001247, IPR015847), then a KH domain (IPR004088) and an S1 domain at the C-terminus. This is the canonical bacterial/organellar PNPase architecture, which is also found in *E. coli* PNPase and plant chloroplast PNPase.
- Nothing suggests ambiguity with another gene. The old-35 name derives from the original senescence/interferon-induced cDNA (Leszczyniecka et al., ~2002, *PNPT1* as "old-35"; verify the reference).

## 2. Primary molecular function

**Reaction.** PNPase is a 3'→5' phosphorolytic exoribonuclease. It uses inorganic phosphate to remove ribonucleotides from the 3' end of RNA, releasing nucleoside 5'-diphosphates: RNA(n) + Pi → RNA(n−1) + NDP.

**Reverse activity.** The reaction is reversible. In vitro, and in the presence of NDPs, the enzyme can add (poly)nucleotide tails, which is the basis of the EC 2.7.7.8 "nucleotidyltransferase" name. The UniProt header cites PMID:18083836 for the EC assignment.

**Substrates.**
- It is a processive degrader of single-stranded RNA.
- It stalls on stable secondary structure unless partnered with a helicase, as described in section 4.

**Structure.**
- The enzyme is a homotrimer. The RNase PH domains form a central ring, with a channel through which the 3' end of the RNA is threaded.
- The KH and S1 domains sit above the channel and bind and feed RNA into it.
- This is inferred from bacterial PNPase structures and supported by human structural work (Golzarroshan et al., 2018, Nat Commun, human PNPase structure with RNA; verify).

## 3. Localisation

- **Intermembrane space (IMS).** PNPase is a precursor protein with an N-terminal mitochondrial targeting sequence, and it localises to the IMS and the matrix side of the inner membrane. Chen et al. (2006, Mol Cell Biol) established IMS localisation and an inner-membrane-anchored topology.
- **Matrix and mitochondrial RNA foci.** Borowski et al. (2013, NAR) showed matrix/RNA-granule localisation, where it partners with SUPV3L1 (verify).
- **Not primarily cytosolic.** The older literature on old-35 as a cytosolic or interferon-response factor is largely superseded by the mitochondrial localisation.

## 4. Biological processes and pathways

### 4.1 Mitochondrial RNA degradation and the degradosome

- PNPase forms the mitochondrial RNA degradosome with the helicase SUPV3L1 (SUV3). The helicase unwinds structured RNA and feeds single-stranded 3' ends to the PNPase exonuclease (Borowski 2013; Wang et al. 2010; verify).
- A related reference is Szczesny et al. (2010, NAR) on SUV3 and PNPase and the degradation of mitochondrial transcripts and antisense RNAs (verify).
- Dhir et al. (2018, Nature, "Mitochondrial double-stranded RNA triggers antiviral signalling in humans") showed that PNPT1 and SUV3 degrade mitochondrial dsRNA. When PNPT1 is lost, mt-dsRNA escapes to the cytosol and triggers MDA5-mediated type I interferon signalling.
- PNPase also contributes to turnover of mt-mRNAs, antisense transcripts and processing by-products, and it affects mt-RNA polyadenylation and poly(A) length (Nagaike et al. 2005; Slomovic and Schuster 2008).
  - Slomovic and Schuster 2008 is PMID:18083836. I believe this is the "stable 3' tails and PNPase" paper behind the UniProt EC assignment, but confirm before citing.

### 4.2 RNA import into mitochondria (debated)

- Wang et al. (2010, Cell) reported that PNPase regulates import of small nuclear-encoded RNAs (RNase P RNA, MRP RNA and 5S rRNA) into the mitochondrial matrix. They proposed this occurs through an RNA-binding, structure-dependent mechanism distinct from its exonuclease activity.
- Vedrenne et al. (2012, AJHG) showed the p.Gln510Glu variant impaired RNA import.
- This role is contested. Subsequent work argues the human mitochondrial import of nuclear RNAs, especially 5S rRNA and RNase P RNA, remains unresolved. Treat it as a reported, non-consensus function.
- If annotated, "RNA import into mitochondrion" is better held as lower-confidence or non-core.

### 4.3 Other reported processes

- **mtRNA processing and mitochondrial translation.** Loss of PNPT1 alters mt-RNA levels and processing and causes combined OXPHOS deficiency, which suggests an indirect effect on translation.
- **Homeostasis and mtDNA.** Chen et al. (2006) reported that PNPase knockdown disrupts cristae architecture, mitochondrial morphology and membrane potential, and that it controls mitochondrial homeostasis. The Cell/Chen-era model has PNPase affecting mt-RNA stability. Evidence on direct versus indirect effects is mixed.
- **Interferon and senescence.** The cDNA was originally cloned as an interferon- and senescence-induced gene (old-35). Chronic PNPT1 loss leads to inflammation through the mt-dsRNA route described in 4.1.
- **Cytosolic and miRNA effects.** There are reports that PNPT1 degrades specific miRNAs (e.g. miR-221, in melanoma and fibroblast contexts) and affects c-myc mRNA. These are likely context-dependent and need verification before annotation. Because the protein is largely mitochondrial, they may be indirect.

## 5. Disease associations (human genetics)

- **COXPD13** (combined oxidative phosphorylation deficiency 13): biallelic hypomorphic variants, including p.Gln510Glu, cause early-onset encephalopathy with respiratory-chain deficiency (Vedrenne et al. 2012, AJHG; later case series).
- **DFNB70**: non-syndromic autosomal recessive deafness (von Ameln et al. 2012, AJHG).
- **Other phenotypes.** Later work links biallelic variants to Leigh-like disease, optic atrophy, and a spectrum from mild to severe; there is also an autosomal dominant phenotype. Quote clinical details only after checking sources.
- Disease variants impair either import, degradation, or both. They also increase mt-dsRNA-driven interferon signalling, as inferred from Dhir 2018 and follow-ups (verify).

## 6. Evidence tiers

| Claim | Evidence type | Confidence |
|---|---|---|
| 3'→5' phosphorolytic exoribonuclease (EC 2.7.7.8) | Biochemical assays, structural homology, UniProt (PMID:18083836) | High |
| Forms degradosome with SUPV3L1 and degrades mt-RNA/dsRNA | IDA/IPI, cell biology, Dhir 2018 | High |
| IMS/matrix localisation | Fractionation and protease protection (Chen 2006) | High |
| Trimeric structure and RNA channel | Bacterial and human structures | High |
| RNA import into mitochondria | Wang 2010, Vedrenne 2012 | Contested |
| miRNA/c-myc cytosolic effects | Cell-line studies | Low/context-dependent |
| Interferon/senescence (old-35) | Original cloning | Low as direct function |

## 7. Implications for GO curation

- **Core molecular function**, in descending priority:
  - 3'-5'-RNA exonuclease activity (GO:0000175), or its phosphorolytic child where available.
  - Polyribonucleotide nucleotidyltransferase activity (GO:0004654).
  - RNA binding (GO:0003723), as a more informative alternative to generic "protein binding".
- **Core process:** mitochondrial RNA catabolic process / mitochondrial mRNA catabolism, and mitochondrial dsRNA degradation or regulation of the innate immune response triggered by mt-dsRNA (check exact GO ids with the OLS MCP before use).
- **Core location:** mitochondrial intermembrane space, and mitochondrial matrix / RNA degradosome (the degradosome complex term exists as "mitochondrial degradosome"; verify).
- **Non-core or contested:** RNA import into mitochondrion, miRNA turnover, and interferon or senescence roles. Handle with KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED, as appropriate.
- **Avoid:** "protein binding" annotations, and `REMOVE` actions on experimental annotations without full-text verification, per project guidance.

## 8. Suggested open questions

- What is the true in vivo contribution of PNPase to import of nuclear-encoded RNAs, independent of its catalytic activity?
- How does the PNPase/SUV3 balance control which mitochondrial transcripts are protected or degraded?
- Which disease variants act via degradation defects and which via structural or import defects?
- Is there a physiological cytosolic or extramitochondrial pool of PNPT1?

## 9. Verification checklist before using this report

1. Confirm that PMID:18083836 matches the claimed title and the EC 2.7.7.8 evidence.
2. Look up the PMIDs for Chen 2006, Wang 2010, Vedrenne 2012, von Ameln 2012, Borowski 2013, Dhir 2018, Szczesny 2010 and Golzarroshan 2018. Fetch each into `publications/`.
3. Take verbatim quotes from the cached text.
4. Resolve GO ids through the OLS MCP rather than from memory.