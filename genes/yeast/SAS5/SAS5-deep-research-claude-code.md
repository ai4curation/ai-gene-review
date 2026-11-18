---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:25:25.683329'
end_time: '2026-11-18T15:28:27.741492'
duration_seconds: 182.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SAS5
  gene_symbol: SAS5
  uniprot_accession: Q99314
  protein_description: 'RecName: Full=Something about silencing protein 5;'
  gene_info: Name=SAS5; OrderedLocusNames=YOR213C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Not specified in UniProt
  protein_domains: Sas5/TAF14. (IPR016665); YEAST_sf. (IPR038704); YEATS. (IPR005033);
    YEATS_dom. (IPR055129); YEATS (PF03366)
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
  - claude-fable-5-2
  - claude-haiku-5-5
  web_search_requests: 11
  num_turns: 27
  total_cost_usd: 1.87534286
  session_id: fb8d9ddd-a85b-4665-908b-67fce276eecc
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q99314
- **Protein Description:** RecName: Full=Something about silencing protein 5;
- **Gene Information:** Name=SAS5; OrderedLocusNames=YOR213C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Sas5/TAF14. (IPR016665); YEAST_sf. (IPR038704); YEATS. (IPR005033); YEATS_dom. (IPR055129); YEATS (PF03366)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SAS5" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SAS5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SAS5** (gene ID: SAS5, UniProt: Q99314) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still gathering sources: I've read the cached SAS-complex papers and am now pulling the full text of the 2022 benzoylation paper to check what it actually reports for the Sas5 YEATS domain.

# SAS5 (YOR213C; UniProt Q99314) in *Saccharomyces cerevisiae*: research report for functional annotation

## 1. Identity verification

The target is unambiguous. SAS5 ("Something About Silencing 5", YOR213C) is a 248-residue budding-yeast protein with an N-terminal YEATS domain (residues 1–139; Pfam PF03366, InterPro IPR005033/IPR016665 "Sas5/TAF14"), a phosphoserine at S144 and a disordered C-terminal tail (UniProt Q99314). The literature found matches this protein, organism and domain architecture.

Two same-symbol hits were excluded: *C. elegans* SAS-5 and Sas-4/Sas-6 are centriole-assembly proteins unrelated to yeast Sas5.

Evidence levels in this report:
- **Read directly:** abstracts of the cached papers (PMID 11731479, 11731480, 12626510, 15788653) and the UniProt record.
- **Secondary:** search-result snippets and a partial machine summary of one full text (Wang et al. 2022); these are flagged where used.
- **Unverified recall:** a few background statements, marked as such.

## 2. Summary

Sas5 is a non-catalytic subunit of the nuclear SAS (SAS-I) histone acetyltransferase complex, a heterotrimer of Sas2 (MYST-family catalytic subunit), Sas4 (bridging subunit) and Sas5. The complex acetylates histone H4 lysine 16 (H4K16ac). This mark opposes Sir2-mediated deacetylation and limits spreading of Sir2/3/4 heterochromatin from telomeres and silent mating-type loci into euchromatin.

Sas5 has no demonstrated catalytic activity of its own. It stimulates Sas2 activity, whereas Sas4 is absolutely required. Its YEATS domain is an acyl-lysine reader fold, shown in vitro to bind benzoylated histone H3 peptides weakly. The in vivo ligand and its contribution to SAS-I targeting are unknown.

## 3. Discovery and genetics

- **Identification.** SAS4 and SAS5 were found in 1999 in two companion *Genetics* papers (Xu, Kim, Replogle, Rine & Rivier, PMID 10471696; Xu, Kim & Rivier, PMID 10471697). I did not read these; the findings below come from abstract snippets.
- **Locus-specific effects.** Null alleles of SAS4 and SAS5 restore silencing at a defective HMR locus, but are needed for silencing at HML and telomeres. They are therefore negative regulators at HMR and positive regulators at HML and telomeres.
- **Single pathway.** Combinations of *sas2*, *sas4* and *sas5* nulls are reportedly no more defective for HML silencing than single mutants, consistent with one complex.
- **Interpretation.** The opposite effects are now explained by boundary function rather than a direct silencing role: loss of H4K16ac lets Sir proteins spread and be titrated away from telomeres, weakening silencing there while strengthening it at weakened HMR.

## 4. The SAS complex: composition and architecture

- **Complex identification.** Osada et al. (2001, *Genes Dev*, PMID 11731479) identified an approximately 450 kDa SAS complex containing Sas2p, Sas4p and "the tf2f-related Sas5 protein". Mutating the Sas2 acetyl-CoA binding motif disrupted silencing at HML and telomeres.
- **Independent confirmation.** Meijsing & Ehrenhofer-Murray (2001, *Genes Dev*, PMID 11731480) found Sas2 "in a nuclear protein complex that included Sas4 and Sas5, a homolog of TAF(II)30", named it SAS-I, and showed it contributes to rDNA silencing.
- **Stoichiometry.** Shia et al. (2005, *J Biol Chem*, PMID 15659401) re-characterised the native complex as a small trimer with one copy of each subunit. Snippets give about 125–150 kDa, which conflicts with the earlier 450 kDa gel-filtration estimate. I could not retrieve this abstract.
- **Subunit topology.** Schaper et al. (2005, *J Cell Sci*, PMID 15788653): "Sas4p was the central subunit of the SAS-I complex, bridging Sas2p and Sas5p." Sas5 therefore contacts Sas4 rather than Sas2 directly.
- **Proteomics.** UniProt/IntAct records a Sas5–Sas4 binary interaction (4 experiments). The Sas5–Sas4 association is also the basis of a GOA annotation from the 2023 affinity-enrichment interactome (Michaelis et al., *Nature*, PMID 37968396).

No experimental structure of the assembled complex was found. The only Sas5 structure in the PDB is the isolated YEATS domain (7F5M).

## 5. Molecular function

### 5.1 Stimulation of Sas2 acetyltransferase activity

Sutton et al. (2003, *J Biol Chem*, PMID 12626510) is the key biochemical paper:

- "recombinant Sas2 has HAT activity that absolutely requires Sas4 and is stimulated by Sas5."
- "The recombinant SAS complex acetylates H4 lysine 16 and H3 lysine 14," and the native complex shows similar specificity.
- "neither the recombinant nor the native SAS complex acetylated nucleosomal histones under conditions that were optimum for acetylating free histones."
- Asf1-bound H3/H4 is not acetylated, suggesting SAS may act on free histones before deposition.

The catalysed reaction is acetyl-CoA + histone H4 lysine 16 → CoA + N6-acetyl-lysine, performed by Sas2. Sas5 is best described as a stimulatory or stabilising accessory subunit. UniProt states it "may be required to stabilize the complex or help in substrate recognition".

Two points are unsettled:
- **Nucleosomal substrates.** SGD's description says the complex "acetylates free histones and nucleosomes", which contradicts the Sutton 2003 abstract. The SGD wording may derive from Shia 2005, which I could not read.
- **H3K14.** A snippet for Shia 2005 says the complex "exclusively acetylates lysine 16 of histone H4 in vitro", in tension with the H3K14 activity reported by Sutton 2003. H4K16 is the in vivo relevant site: H4K16R phenocopies *sas2Δ* (PMID 11731480).

### 5.2 YEATS domain: acyl-lysine reader

- YEATS domains are immunoglobulin-like β-sandwich readers of acetyl- and other acyl-lysines. Yeast has three: Sas5, Taf14 and Yaf9. Taf14 YEATS reads H3K9ac and H3K9cr (Shanle et al. 2012; Andrews et al. 2016); Yaf9 binds H3K27ac.
- Wang et al. (2022, *Nat Commun*, PMID 35296687) report that "a subset of YEATS domains and bromodomains serve as Kbz readers" and solved the Sas5 YEATS domain bound to an H3K27 benzoyl-lysine peptide (PDB 7F5M, 2.40 Å).
- The following details come from a partial machine summary of that paper, not verbatim text, and need checking before being quoted:
  - Sas5 YEATS preferred H3K14bz and H3K27bz among five benzoylated H3 peptides, and preferred benzoyl- over acetyl-lysine.
  - Affinities were weak, in the hundreds-of-micromolar range.
  - Recognition uses an aromatic sandwich (W82 and F63), and W82A abolished binding.
  - Yaf9 showed no detectable benzoyl-lysine binding.
- The paper's conclusions for Sas5 are in vitro only. No study was found testing whether YEATS–histone binding is needed for SAS-I function, H4K16ac deposition or silencing.

### 5.3 Relationship to Taf14

Sas5 and Taf14 are paralogs sharing the "Sas5/TAF14" signature (IPR016665); early papers called Sas5 "TFIIF-related" or a TAF(II)30 homolog. From memory, SGD lists them as a whole-genome-duplication pair, but my search did not confirm this.

The paralogs have diverged in complex membership. Taf14 is the YEATS subunit of TFIID, TFIIF, SWI/SNF, INO80, RSC and NuA3 (background knowledge, not re-verified here). Every experimental study of Sas5 found places it only in SAS-I.

This matters for the current GO annotations. The IBA rows for TFIID complex, TFIIF complex, SWI/SNF complex, Ino80 complex, chromatin remodeling and regulation of RNA polymerase II transcription describe Taf14-lineage functions. No Sas5-specific evidence supporting them was found.

## 6. Biological process: heterochromatin boundaries

- **Opposition to Sir2.** Sas2-dependent H4K16 acetylation and Sir2 deacetylation form opposing gradients that set the telomeric euchromatin–heterochromatin boundary (Kimura et al. 2002; Suka et al. 2002, *Nat Genet*, doi:10.1038/ng993). An acetyl-mimic H4K16Q mutant greatly reduces Sir3 spreading.
- **All three subunits are required.** Deletion of *sas2*, *sas4* or *sas5* is each synthetically lethal with *rpd3Δ*. The lethality stems from excessive SIR spreading and is suppressed by removing telomeric SIR components (Ehrentraut et al. 2010, PMC2851772; from snippet).
- **HMR boundary.** *sas5Δ* allows heterochromatin to spread past the HMR-tRNA boundary (Jambunathan et al. 2005, *Genetics*, PMID 16079223; cited by UniProt as the disruption phenotype).
- **Chromatin assembly link.** Sas2 interacts with Cac1 (CAF-I) and Asf1, leading to a model in which SAS-I is recruited to newly replicated DNA to acetylate H4K16 (PMID 11731480, 11731479).
- **Genome-wide role.** Sas2-dependent H4K16ac is strongest within open reading frames with low histone exchange, is coupled to S phase, and *sas2Δ* confers 6-azauracil resistance (Heise et al. 2012, *Nucleic Acids Res*, PMID 21908408; from snippet). This work was done on Sas2; Sas5's contribution is inferred from complex membership.
- **rDNA.** SAS-I contributes to rDNA silencing (PMID 11731480).

The process term best supported for Sas5 is its contribution to subtelomeric and silent-locus heterochromatin boundary formation through H4K16 acetylation. General transcription regulation is not directly evidenced for Sas5.

## 7. Localization

- **Nuclear.** Sas5 is in a nuclear complex (PMID 11731480).
- **Import route.** Schaper et al. 2005: "the nuclear import of Sas2p and Sas5p was mediated by two karyopherins/importins, Kap123p and Pse1p, and both were associated in vivo with these importins." Sas4 is not a cargo of either, so subunits are imported independently and presumably assemble in the nucleus.
- **Import signal.** "An unknown signal region was located in the N-terminal domain of Sas5p", which overlaps the YEATS domain.
- **Chromatin.** GOA carries a chromatin IDA and a telomeric-region IEA; the site of action is chromatin at subtelomeric and silent-locus boundaries.
- **Abundance.** About 1,800 molecules per cell in log phase (Ghaemmaghami et al. 2003, PMID 14562106, via UniProt).

## 8. Implications for annotation

| Aspect | Best-supported statement | Evidence |
|---|---|---|
| Molecular function | Stimulates Sas2 H4K16 acetyltransferase activity as a SAS-complex subunit; not itself catalytic | PMID 12626510 |
| Molecular function | Acyl-lysine (benzoyl-lysine) histone binding by YEATS domain, weak and in vitro only | PMID 35296687; PDB 7F5M |
| Complex | SAS acetyltransferase complex, bound through Sas4 | PMID 11731479, 11731480, 15788653, 15659401 |
| Process | Limits Sir heterochromatin spreading at telomeres, HML and HMR; rDNA silencing | PMID 10471696, 10471697, 16079223, 11731480 |
| Location | Nucleus, chromatin | PMID 11731480, 15788653 |

The "histone acetyltransferase activity" and "acetyltransferase activity" IDA rows on Sas5 reflect activity of the complex, with Sas2 as the catalytic subunit. A "contributes to" reading fits the evidence better than intrinsic activity.

## 9. Open questions

- What does the Sas5 YEATS domain bind in vivo, and does that binding affect SAS-I recruitment or activity?
- How does Sas5 stimulate Sas2: by stabilising the complex, presenting substrate, or allostery? No structure of the trimer exists.
- Does SAS-I acetylate nucleosomes under physiological conditions?
- What is the role of S144 phosphorylation?

## Sources

- [UniProt Q99314 (SAS5_YEAST)](https://www.uniprot.org/uniprotkb/Q99314)
- [SGD SAS5 locus page](https://www.yeastgenome.org/locus/SAS5)
- [Xu et al. 1999, Identification of SAS4 and SAS5, Genetics 153:13 (PMC1460750)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1460750)
- [Xu, Kim & Rivier 1999, SAS4 and SAS5 are locus-specific regulators of silencing, Genetics 153:25 (PMC1460757)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1460757)
- [Osada et al. 2001, Genes Dev 15:3155 (PMC312835)](https://pmc.ncbi.nlm.nih.gov/articles/PMC312835)
- [Meijsing & Ehrenhofer-Murray 2001, Genes Dev 15:3169 (PMC312838)](https://pmc.ncbi.nlm.nih.gov/articles/PMC312838)
- [Sutton et al. 2003, J Biol Chem 278:16887 (doi:10.1074/jbc.M210709200)](https://doi.org/10.1074/jbc.M210709200)
- [Shia et al. 2005, Characterization of the yeast trimeric-SAS acetyltransferase complex, J Biol Chem 280:11987](https://www.jbc.org/article/S0021-9258(20)80910-7/fulltext)
- [Schaper et al. 2005, Nuclear import of SAS-I, J Cell Sci 118:1473 (doi:10.1242/jcs.01739)](https://doi.org/10.1242/jcs.01739)
- [Suka et al. 2002, Nat Genet (doi:10.1038/ng993)](https://www.doi.org/10.1038/NG993)
- [Ehrentraut et al. 2010, Rpd3-dependent boundary formation at telomeres (PMC2851772)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2851772)
- [Heise et al. 2012, Genome-wide H4 K16 acetylation by SAS-I, Nucleic Acids Res (BioGRID record)](https://thebiogrid.org/123548/publication/genome-wide-h4-k16-acetylation-by-sas-i-is-deposited-independently-of-transcription-and-histone-exchange.html)
- [Wang et al. 2022, Global profiling of regulatory elements in the histone benzoylation pathway, Nat Commun (PMC8927147)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8927147)
- [PDB 7F5M, Sas5 YEATS domain with H3K27bz peptide](https://www.rcsb.org/structure/7F5M)
- [Andrews et al. 2016, Taf14 YEATS domain is a reader of histone crotonylation (PMC4871749)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4871749)
- [Klein et al. 2018, Yaf9 YEATS and H3K27ac (PMC5758897)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758897)
- [Michaelis et al. 2023, yeast protein interactome, Nature (PMC10700138)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700138/)

## Citations

1. https://www.uniprot.org/uniprotkb/Q99314
2. https://www.yeastgenome.org/locus/SAS5
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC1460750
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC1460757
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC312835
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC312838
7. https://doi.org/10.1074/jbc.M210709200
8. https://www.jbc.org/article/S0021-9258(20
9. https://doi.org/10.1242/jcs.01739
10. https://www.doi.org/10.1038/NG993
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC2851772
12. https://thebiogrid.org/123548/publication/genome-wide-h4-k16-acetylation-by-sas-i-is-deposited-independently-of-transcription-and-histone-exchange.html
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC8927147
14. https://www.rcsb.org/structure/7F5M
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC4871749
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC5758897
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700138/