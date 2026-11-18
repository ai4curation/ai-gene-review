---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:22:30.544497'
end_time: '2026-11-18T15:25:24.538849'
duration_seconds: 173.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: YNG1
  gene_symbol: YNG1
  uniprot_accession: Q08465
  protein_description: 'RecName: Full=Protein YNG1; AltName: Full=ING1 homolog 1;'
  gene_info: Name=YNG1; OrderedLocusNames=YOR064C; ORFNames=YOR29-15;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the ING family. .
  protein_domains: ING_fam. (IPR028651); Znf_FYVE_PHD. (IPR011011); Znf_PHD. (IPR001965);
    Znf_RING/FYVE/PHD. (IPR013083)
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
  web_search_requests: 8
  num_turns: 26
  total_cost_usd: 1.9324768050000003
  session_id: b2b417e8-eac7-4abd-90b3-23602bb12bb8
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q08465
- **Protein Description:** RecName: Full=Protein YNG1; AltName: Full=ING1 homolog 1;
- **Gene Information:** Name=YNG1; OrderedLocusNames=YOR064C; ORFNames=YOR29-15;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the ING family. .
- **Key Domains:** ING_fam. (IPR028651); Znf_FYVE_PHD. (IPR011011); Znf_PHD. (IPR001965); Znf_RING/FYVE/PHD. (IPR013083)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "YNG1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'YNG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **YNG1** (gene ID: YNG1, UniProt: Q08465) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

PMC and Springer block direct page fetches, so I'm switching to the repo's cached publications and the Europe PMC API for the primary-paper details.

# YNG1 (YOR064C; UniProt Q08465) in *Saccharomyces cerevisiae*: research report for functional annotation

## Identity check and evidence base

The target is unambiguous. "YNG1" (Yeast iNhibitor of Growth 1, YOR064C) is a 219-residue ING-family protein with a single C-terminal PHD finger (residues 155–204), matching the UniProt description, organism and domain set given. All literature below concerns this protein.

How far the evidence was verified:

- **Abstract-level only.** PMC and Springer blocked full-text retrieval, so the primary papers were read as abstracts (the repository's cached PubMed records), supplemented by the UniProt record and search-result summaries.
- **One partial full text.** Loewith et al. 2000 was read through the start of its Results section.
- **Not verified, so not reported.** Dissociation constants, the identities of specific point mutants, and the exact residues of the Taf14-binding motif beyond what UniProt records.

## 1. Summary of function

Yng1 is a non-catalytic, histone-reading subunit of the NuA3 histone H3 acetyltransferase complex. Its primary molecular function is **histone H3K4me3 reader activity** (GO:0140002), carried by the PHD finger. A second, N-terminal region binds the unmodified H3 tail.

Together these tether the catalytic MYST-family subunit Sas3 to nucleosomes carrying Set1-dependent H3K4 methylation, at the 5′ ends of transcribed genes. This promotes Sas3-catalysed acetylation of H3K14 and transcription of a subset of genes. Yng1 has no enzymatic activity of its own: it is an adaptor between a histone mark and a histone-modifying enzyme, acting in the nucleus on chromatin.

## 2. Protein family and architecture

- **ING family.** Yng1 is one of three ING proteins in budding yeast, with Yng2 and Pho23. All three share a conserved C-terminal PHD finger with human p33ING1; the C-terminal regions are "very similar (50 to 60% identity)" (Loewith et al. 2000, *Mol Cell Biol* 20:3807–3816, PMID 10805724, https://pmc.ncbi.nlm.nih.gov/articles/PMC85704).
- **One ING per complex.** Each yeast ING protein belongs to a different histone-modifying complex: Pho23 in Rpd3/Sin3 deacetylase, Yng1 in NuA3 and Yng2 in NuA4 (Nourani et al. 2003, *J Biol Chem* 278:19171–19175, PMID 12672825).
- **Domain layout from structures** (UniProt Q08465 features):

| Region | Residues | Role | Structure |
|---|---|---|---|
| N-terminal helices | 23–41 and 47–97 | Only ordered part of Yng1 in the cryo-EM maps; UniProt does not annotate what it contacts | 9UUO, 9UUS, 9VKW (cryo-EM) |
| ET-binding motif | 113–124 | β-strand bound by the Taf14 extra-terminal domain | 8U77 (X-ray, 1.93 Å) |
| PHD finger | 155–204 (solved as 141–219) | Binds two Zn²⁺ and the H3K4me3 tail | 2JMI (free), 2JMJ (with H3(1–9)K4me3), NMR |

- **PHD finger residues.** Zn²⁺ is coordinated by residues 158, 160, 182, 185 (site 1) and 171, 176, 198, 202 (site 2). H3K4me3-contacting sites are 157, 168, 172 and 180. All are assigned from Taverna et al. 2006.
- **PANTHER.** Family PTHR10333 (Inhibitor of growth protein), subfamily SF103.

## 3. Molecular function: evidence

### 3.1 Bridging Sas3 to nucleosomes

Howe et al. 2002 (*Mol Cell Biol* 22:5047–5053, PMID 12077334, https://pmc.ncbi.nlm.nih.gov/articles/PMC139787) found Yng1 by mass spectrometry of purified NuA3. The abstract states:

- Yng1 "is a stable component of the NuA3 histone acetyltransferase complex", with Sas3 as the catalytic subunit.
- It "is required for NuA3 function in vivo but surprisingly is not required for the integrity of the complex."
- It "mediates the interaction of Sas3p with nucleosomes and is thus required for the ability of NuA3 to modify histone tails."

This is the basis of the GOA "histone acetyltransferase activity" row (IMP). It should be read as Yng1 *contributing to* the complex's activity through substrate engagement, not as Yng1 being a catalyst.

### 3.2 The PHD finger reads H3K4 methylation

Four independent 2006–2007 studies converge:

- **Shi et al. 2006** (*Nature* 442:96–99, PMID 16728974): ING-family PHD domains are "specific and highly robust binding modules for H3K4me3 and H3K4me2". The paper's focus is human ING2; UniProt cites it for Yng1 binding H3K4me3 and, more weakly, H3K4me2.
- **Martin et al. 2006** (*Mol Cell Biol* 26:7871–7879, PMID 16923967): a genetic screen using the toxicity of YNG1 overexpression. Yng1 interacts with the H3 N-terminal tail, and loss of K4 methylation disrupts this. Toxicity maps to the PHD finger, which binds K4-methylated H3 in vitro; PHD mutations that abolish binding are no longer toxic. The authors conclude the finger promotes "stabilization of the NuA3 complex at chromatin through recognition of histone H3 lysine 4 methylation."
- **Taverna et al. 2006** (*Mol Cell* 24:785–796, PMID 17157260, DOI 10.1016/j.molcel.2006.10.026): mass spectrometry, biochemistry and NMR define the PHD–H3K4me3 interaction. Genome-wide ChIP-chip shows "colocalization of Yng1 and H3K4me3 in vivo". Disrupting K4me3 binding "altered K14ac and transcription at certain genes", which the authors present as direct in vivo evidence of sequential methyl-reading, acetylation and gene regulation.
- **Shi et al. 2007** (*J Biol Chem* 282:2450–2455, PMID 17142463): a proteome-wide survey of yeast PHD fingers establishing them as a general class of H3K4me3 and H3K36me3 effectors.

### 3.3 A second, methylation-independent histone contact

Chruscicki et al. 2010 (*Genetics*, "Critical determinants for chromatin binding by *Saccharomyces cerevisiae* Yng1 exist outside of the plant homeodomain finger", https://pmc.ncbi.nlm.nih.gov/articles/PMC2881130) refined the simple "PHD targets NuA3" model:

- Deleting the PHD finger does not release NuA3 from chromatin.
- Full-length Yng1 has two independent histone-binding motifs: an N-terminal one for unmodified H3 tails and the C-terminal PHD finger for H3K4me3.
- The two act together to increase apparent affinity for the H3 tail.

So the PHD finger adds methyl-mark selectivity on top of a basal tail interaction.

### 3.4 Structural placement in NuA3 (2024–2025)

- **Nguyen et al. 2024** (*Nat Commun* 15:5335, PMID 38914563, DOI 10.1038/s41467-024-49730-y): Taf14 binds both Yng1 and Sas3 through its extra-terminal domain, recognising a conserved motif in each. Mutating the motifs reduces binding, and both interactions "are required for proper NuA3 function in gene transcription and DNA repair" in yeast.
- **Shi et al. 2025** (*Nat Commun* 17:342, DOI 10.1038/s41467-025-67049-0, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12789522/): cryo-EM structures of NuA3 in apo, acetyl-CoA-bound and acetyl-CoA plus H3-tail-bound states (3.1–3.7 Å).
  - The H3 tail-binding cleft that confers K14 specificity is formed by Sas3 and Nto1, not Yng1.
  - The Yng1 PHD finger and Taf14 YEATS domain were not resolved, consistent with flexibly tethered reader modules.
  - The paper restates the two-motif model: the N-terminal region binds unmodified H3 and the PHD finger reads H3K4 methylation.

These structures confirm the division of labour: Sas3 and Nto1 provide catalysis and site selection, while Yng1 is a mobile reader arm.

## 4. Complex membership

UniProt and ComplexPortal (CPX-1810) describe two forms of NuA3:

- **NuA3a:** Sas3, Nto1, Yng1, Taf14 and Eaf6. It uses the Yng1 PHD finger to bind H3K4me3 at the 5′ ends of open reading frames.
- **NuA3b:** the same subunits plus Pdp3, whose PWWP domain binds H3K36me3 across transcribed regions.

The distinction comes from Gilbert et al. 2014 (*Mol Cell Proteomics* 13:2883–2895, PMID 25104842). Direct physical partners of Yng1 recorded in IntAct are Sas3, Taf14 and histone H3 (Hht2).

## 5. Biological process and site of action

- **Localisation.** Nuclear, by genome-wide GFP tagging (Huh et al. 2003, PMID 14562095), and on chromatin at the 5′ ends of active genes by ChIP-chip (Taverna et al. 2006). Abundance is about 861 molecules per cell in log phase (Ghaemmaghami et al. 2003, PMID 14562106).
- **Pathway.** Set1/COMPASS deposits H3K4me3, the Yng1 PHD finger reads it, NuA3 is retained, Sas3 acetylates H3K14, and transcription initiation is promoted at a subset of genes (Taverna et al. 2006; Gilbert et al. 2014).
- **Recruitment in vivo is broader than the promoter model.** Martin et al. 2017 (*Genetics*, PMID 28108585, https://pmc.ncbi.nlm.nih.gov/articles/PMC5340327) found:
  - NuA3 is mainly targeted to mid-gene regions through H3K36me3 and H3K4me1/2/3.
  - Losing either methylation pathway causes partial loss of NuA3; losing both abolishes recruitment to transcribed genes.
  - The Taf14 YEATS domain showed no role in recruitment.
  - NuA3 presence alone does not guarantee acetylation of the bound nucleosomes.
- **Elongation.** The GOA row for positive regulation of RNA polymerase II elongation (IGI) derives from Gilbert et al. 2014. The elongation role there is assigned to Pdp3-containing NuA3b; Yng1 is a shared subunit, so this is a complex-level rather than a Yng1-specific function.
- **Redundancy with Gcn5.** NuA3a, but not NuA3b, is synthetically lethal with deletion of GCN5 (Gilbert et al. 2014), consistent with overlapping H3K14 acetylation by SAGA and NuA3.

## 6. Mutant phenotypes

- **Deletion.** *yng1Δ* has "little effect on growth or morphology", but the cells cannot use nonfermentable carbon sources and are heat-shock sensitive (Loewith et al. 2000).
- **Overexpression.** Toxic, dependent on a functional PHD finger and on H3K4 methylation (Martin et al. 2006).
- **Heterologous reporter.** Deleting YNG1 or SAS3 increased p53-dependent transcriptional activation in yeast, suggesting NuA3 can act in gene-specific repression (Nourani et al. 2003). This is an artificial p53 system and of limited weight for native function.

## 7. Implications for GO annotation

- **Core molecular function:** histone H3K4me3 reader activity (GO:0140002), with multiple IDA and IMP lines plus an NMR structure. This is the best-supported term.
- **Histone acetyltransferase activity (GO:0004402, IMP):** Yng1 is not catalytic. Sas3 carries the HAT domain, and the cryo-EM active site and tail cleft are built by Sas3 and Nto1. A "contributes to" reading fits the evidence better than a direct activity.
- **Protein binding (IPI) rows:** the informative content is the Sas3, Taf14 and histone H3 interactions, better expressed as reader or adaptor function and complex membership.
- **Zinc ion binding (RCA):** structurally supported by the two Zn²⁺ sites of the PHD finger, though it is a structural cofactor rather than a function.
- **Cellular component:** NuA3 and NuA3a complex, nucleus and chromatin are all well supported.
- **Biological process:** the most direct support is for promoting H3K14 acetylation and transcription at a subset of genes. "Chromatin remodeling" (IEA) is a loose fit for a reader subunit of an acetyltransferase.

## 8. Open questions

- How much each of the two Yng1 histone contacts contributes to H3K14 acetylation in vivo, as opposed to NuA3 occupancy, given that occupancy does not ensure acetylation (Martin et al. 2017).
- Whether Yng1 is present in NuA3b at the same stoichiometry and whether its PHD finger is engaged there.
- The nature of the DNA-repair role implied by the Taf14–Yng1 interaction mutants (Nguyen et al. 2024).

## Sources

- [Loewith et al. 2000, Mol Cell Biol (PMC85704)](https://pmc.ncbi.nlm.nih.gov/articles/PMC85704)
- [Howe et al. 2002, Mol Cell Biol (PMC139787)](https://pmc.ncbi.nlm.nih.gov/articles/PMC139787)
- [Nourani et al. 2003, J Biol Chem (DOI 10.1074/jbc.C300036200)](https://doi.org/10.1074/jbc.C300036200)
- [Shi et al. 2006, Nature (DOI 10.1038/nature04835)](https://doi.org/10.1038/nature04835)
- [Martin et al. 2006, Mol Cell Biol (DOI 10.1128/MCB.00573-06)](https://doi.org/10.1128/MCB.00573-06)
- [Taverna et al. 2006, Mol Cell (DOI 10.1016/j.molcel.2006.10.026)](https://doi.org/10.1016/j.molcel.2006.10.026)
- [Shi et al. 2007, J Biol Chem (DOI 10.1074/jbc.C600286200)](https://doi.org/10.1074/jbc.C600286200)
- [Chruscicki et al. 2010, Genetics (PMC2881130)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2881130)
- [Gilbert et al. 2014, Mol Cell Proteomics (PMC4223479)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4223479)
- [Martin et al. 2017, Genetics (PMC5340327)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340327)
- [Nguyen et al. 2024, Nat Commun 15:5335](https://link.springer.com/article/10.1038/s41467-024-49730-y) ([PubMed 38914563](https://pubmed.ncbi.nlm.nih.gov/38914563/))
- [Shi et al. 2025, Nat Commun (PMC12789522)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12789522/)
- PDB entries: [2JMI](https://proteopedia.org/w/2jmi), [2JMJ](https://proteopedia.org/w/2jmj), [8U77](https://pdbj.org/mine/summary/8u77), [9UUO](https://www.rcsb.org/structure/9UUO), [9UUS](https://www.rcsb.org/structure/9UUS), [9VKW](https://rcsb.org/structure/9VKW)
- [SGD locus page for YNG1](https://www.yeastgenome.org/locus/YNG1) and UniProt Q08465 (local record `genes/yeast/YNG1/YNG1-uniprot.txt`)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC85704
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC139787
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC2881130
4. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12789522/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC5340327
6. https://doi.org/10.1074/jbc.C300036200
7. https://doi.org/10.1038/nature04835
8. https://doi.org/10.1128/MCB.00573-06
9. https://doi.org/10.1016/j.molcel.2006.10.026
10. https://doi.org/10.1074/jbc.C600286200
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC4223479
12. https://link.springer.com/article/10.1038/s41467-024-49730-y
13. https://pubmed.ncbi.nlm.nih.gov/38914563/
14. https://proteopedia.org/w/2jmi
15. https://proteopedia.org/w/2jmj
16. https://pdbj.org/mine/summary/8u77
17. https://www.rcsb.org/structure/9UUO
18. https://www.rcsb.org/structure/9UUS
19. https://rcsb.org/structure/9VKW
20. https://www.yeastgenome.org/locus/YNG1