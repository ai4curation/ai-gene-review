---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:21:42.746194'
end_time: '2026-11-18T15:25:38.720735'
duration_seconds: 235.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SGF29
  gene_symbol: SGF29
  uniprot_accession: P25554
  protein_description: 'RecName: Full=SAGA complex subunit SGF29; AltName: Full=29
    kDa SAGA-associated factor; AltName: Full=SAGA histone acetyltransferase complex
    29 kDa subunit; AltName: Full=SAGA-associated factor 29;'
  gene_info: Name=SGF29; OrderedLocusNames=YCL010C; ORFNames=YCL10C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the SGF29 family. {ECO:0000255|PROSITE-
  protein_domains: SGF29. (IPR037802); SGF29_tudor-like_dom. (IPR010750); Tudor_SGF29_rpt1.
    (IPR047288); Tudor_SGF29_rpt2. (IPR047287); SGF29_Tudor (PF07039)
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
  num_turns: 21
  total_cost_usd: 1.8463243000000003
  session_id: 9f5947d4-0f56-487f-a1a7-a67c1d66f299
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P25554
- **Protein Description:** RecName: Full=SAGA complex subunit SGF29; AltName: Full=29 kDa SAGA-associated factor; AltName: Full=SAGA histone acetyltransferase complex 29 kDa subunit; AltName: Full=SAGA-associated factor 29;
- **Gene Information:** Name=SGF29; OrderedLocusNames=YCL010C; ORFNames=YCL10C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the SGF29 family. {ECO:0000255|PROSITE-
- **Key Domains:** SGF29. (IPR037802); SGF29_tudor-like_dom. (IPR010750); Tudor_SGF29_rpt1. (IPR047288); Tudor_SGF29_rpt2. (IPR047287); SGF29_Tudor (PF07039)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SGF29" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SGF29' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SGF29** (gene ID: SGF29, UniProt: P25554) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking the local UniProt record for SGF29 and searching the literature now.

# SGF29 (YCL010C; UniProt P25554) in *Saccharomyces cerevisiae*: research report

## Identity check

The target is unambiguous. The symbol SGF29 ("SAGA-associated factor, 29 kDa"), ORF YCL010C and the SGF29-family tandem Tudor architecture (IPR010750, PF07039) all match the yeast literature. A human orthologue (SGF29/CCDC101) exists, and I flag below wherever a finding comes from it rather than from yeast.

Sourcing: I read the full text of Bian 2011, Lee 2011 and Nuño-Cabanes 2023 and the abstract of Shukla 2012 in the repository cache. Ringel 2015, Kamata 2013 and Schram 2013 come from search summaries of their abstracts, not the papers themselves. Statements cited to UniProt are the record's summaries of the papers it cites.

## 1. Summary

Sgf29 is a non-catalytic chromatin reader, not an enzyme. Its C-terminal tandem Tudor domain binds the N-terminal tail of histone H3 when Lys4 is di- or trimethylated (H3K4me2/3). It is a subunit of the histone acetyltransferase (HAT) module (Gcn5, Ada2, Ada3/Ngg1, Sgf29) shared by the SAGA, SLIK/SALSA and ADA complexes. Its role is to couple the Set1-dependent H3K4me3 mark at active promoters to Gcn5-dependent H3 acetylation, supporting RNA polymerase II transcription. It acts in the nucleus, on chromatin.

## 2. Molecular function: H3K4me2/3 reader

**Structure and specificity** (Bian et al. 2011, EMBO J 30:2829, [PMID:21685874](https://pubmed.ncbi.nlm.nih.gov/21685874/); PDB [3MEA](https://www.rcsb.org/structure/3MEA) and related entries):
- Crystal structures of the yeast and human tandem Tudor domains were solved with H3K4me2/3 peptides.
- The two Tudor domains pack face to face. One negatively charged pocket holds the free N-terminal Ala1 of H3 and the other holds methylated Lys4.
- The fixed spacing between the pockets explains the selectivity for K4 over other methyl-lysines.
- In yeast Sgf29, Asp163 anchors the H3A1 amine. The K4me3 cage is formed by Tyr205 and Tyr212, buttressed by Phe229.
- Peptide binding (ITC, SPR, fluorescence polarisation) was tested across H3K4, K9, K27, K36, K79 and H4K20 methyl states. Yeast Sgf29 did not bind unmodified H3K4 peptide or H3K9me3.
- UniProt summarises the preference as H3K4me3 over H3K4me2.

**Domain layout.** The protein has an N-terminal coiled-coil region and the C-terminal tandem Tudor (SGF29 C-terminal domain, residues 121–255 in UniProt). UniProt also lists a modified residue at position 139 from phosphoproteomic screens; I did not check which modification or whether it has a known function.

**What Sgf29 is not.** It has no catalytic activity; Gcn5 is the acetyltransferase. Sgf29 is not required for HAT-module acetylation in vitro and sits at the periphery of the module (Nuño-Cabanes et al. 2023, [PMC10226619](https://pmc.ncbi.nlm.nih.gov/articles/PMC10226619/)).

## 3. Complex membership and architecture

- **Discovery.** Sgf29 was identified as a SAGA-associated protein by MudPIT proteomics of TFIID/SAGA components (Sanders et al. 2002, PMID:12052880, per UniProt).
- **HAT module of all Gcn5 complexes.** Quantitative proteomics on 10 TAP-tagged baits and 10 deletion strains placed Sgf29 in the "HAT/Core" module (Lee et al. 2011, Mol Syst Biol 7:503, [PMID:21734642](https://pubmed.ncbi.nlm.nih.gov/21734642/)). It co-purifies with Ahc1 and Ahc2, so it is also in the ADA complex. The authors conclude it is "part of all Gcn5 HAT complexes and not just SAGA".
- **ADA phenotype.** *sgf29Δ* suppresses Gal4-VP16 toxicity like *ada3Δ*, the classic ADA phenotype (Lee et al. 2011).
- **Peripheral position.** Deleting *ADA2* releases the other three HAT-module subunits from SAGA, while deleting *SGF29* or *GCN5* does not (Lee et al. 2011). Ada3 is placed next to Sgf29 on the basis of two-hybrid data. UniProt lists IntAct interactions with Ngg1/Ada3 and Hfi1/Ada1.
- **Structure in the complex.** In structure prediction of the HAT module, Sgf29 and its Tudor domain associate with the periphery of an intertwined Gcn5–Ada2–Ada3 core. The module is tethered to SAGA by the Ada2 SWIRM domain (Nuño-Cabanes et al. 2023). The yeast SAGA cryo-EM paper (Wang et al. 2020, Nature, [PMID:31969703](https://pubmed.ncbi.nlm.nih.gov/31969703/)) cites Sgf29 Tudor–H3K4me3 binding as required for chromatin targeting and H3 acetylation by SAGA.
- **SLIK.** SAGA and SLIK are structurally and biochemically equivalent (PMID:33864814, per UniProt), so Sgf29's role is presumably the same in both.

## 4. Biological process: coupling H3K4 methylation to H3 acetylation

**In vivo acetylation** (Bian et al. 2011):
- *sgf29Δ* lowers global H3K9ac and H3K18ac, and H3K14ac to a lesser extent, resembling *gcn5Δ* and *ada3Δ*.
- H3K23ac and H4 acetylation are not significantly affected.
- Wild-type Sgf29 restores acetylation; Tudor-domain mutants do not, although they are expressed.
- At *GAL1*, deleting *SGF29* or its Tudor domains causes H3K9 hypoacetylation across the locus, loss of SAGA occupancy and severely reduced transcription.

**Mechanism in vitro** (Ringel et al. 2015, PNAS 112:E5461, [PMID:26401015](https://pubmed.ncbi.nlm.nih.gov/26401015/)):
- In a nucleosome competition assay, the HAT module preferentially acetylates H3K4me3 nucleosomes even with excess unmodified nucleosomes present.
- This preference requires the Sgf29 Tudor domain.
- H3K4me3 promotes processive, multisite acetylation of the H3 tail by Gcn5. The authors propose this explains the different acetylation patterns at promoters versus coding regions.

**Transcription initiation** (Shukla et al. 2012, Biochemistry 51:706, [PMID:22224423](https://pubmed.ncbi.nlm.nih.gov/22224423/)):
- Sgf29 is recruited with SAGA to the *GAL1* UAS in an activation-domain-dependent manner.
- In *sgf29Δ*, recruitment of Spt20, TAF10, TAF12 and Ubp8 to the UAS is unchanged.
- TBP recruitment to the core promoter of *GAL1* and other SAGA-regulated genes is weakened, and transcription falls.

**Conflict between the two GAL1 studies.** Bian et al. report loss of SAGA at *GAL1* in *sgf29Δ*; Shukla et al. report that SAGA occupancy at the UAS is unchanged. A reasonable reconciliation, which is my interpretation, is that activators (via Tra1) provide the primary recruitment of SAGA. On that reading, Sgf29–H3K4me3 binding stabilises or orients the HAT module on promoter nucleosomes and raises local acetylation output; it is not the main recruitment route. Under that reading, the GO term "SAGA complex localization to transcription regulatory region" for Sgf29 rests on contested evidence.

**Secondary roles:**
- **Heterochromatin boundary.** Sgf29 has barrier activity against the spread of silencing at *HMR*. Two minimal regions, residues 1–12 and the Tudor-containing 110–255, each suffice, reportedly independently of Gcn5 (Kamata et al. 2013, J Biochem, [PMID:24307402](https://pubmed.ncbi.nlm.nih.gov/24307402/)). This was shown in a tethering-type assay and is best treated as non-core.
- **Not yeast.** A role in ER-stress gene induction (GRP78, CHOP) was shown for human SGF29 (Schram et al. 2013, PLoS ONE, [PMC3720948](https://pmc.ncbi.nlm.nih.gov/articles/PMC3720948/)). It should not be transferred to P25554.
- **Not *S. cerevisiae*.** A 2024 fission-yeast genetic screen found the Sgf29 phenotypic profile correlating with DUB-module components (PMID:39565189). This is suggestive only.

## 5. Localization

Sgf29 is nuclear and acts on chromatin, at UAS and promoter regions and, with SAGA, across transcribed regions of genes such as *GAL1* (Bian 2011; Shukla 2012). UniProt's "Nucleus" is by inference (ECO:0000305), but ChIP and stable SAGA/ADA membership support it directly. Abundance is about 1,750 molecules per cell (PMID:14562106, per UniProt).

## 6. Assessment against current GO annotations

| Annotation | Assessment |
|---|---|
| Histone H3K4me3 reader activity (GO:0140002, IDA) | Core molecular function; strongly supported by structures, binding assays and mutants. |
| SAGA complex, SLIK complex, ADA complex | Well supported by proteomics. |
| Positive regulation of transcription by RNA polymerase II | Supported (*GAL1*, TBP recruitment), acting through H3 acetylation. |
| SAGA complex localization to transcription regulatory region (IMP) | Contested between Bian 2011 and Shukla 2012. |
| Intracellular protein localization | Vague; probably reflects TBP or SAGA recruitment. |
| Protein binding (IPI) | Uninformative. |
| Chromatin organization (IEA) | Correct but general. |

**Database inconsistency.** The UniProt function text lists H3K23ac among SAGA products, whereas Bian et al. found H3K23ac unaffected in *sgf29Δ*.

## 7. Open questions

- How much does Sgf29–H3K4me3 binding contribute to SAGA occupancy genome-wide, relative to activator–Tra1 recruitment?
- Does Sgf29 contribute differently in ADA than in SAGA?
- What is the mechanism of the Gcn5-independent boundary activity of the N-terminal 12 residues?
- How is the Tudor domain positioned on a nucleosome in the intact complex? I found no nucleosome-bound structure of the yeast HAT module.

## Sources

- Bian C et al. 2011, EMBO J 30:2829–42. [PMID:21685874](https://pubmed.ncbi.nlm.nih.gov/21685874/) / [PMC3160252](https://pmc.ncbi.nlm.nih.gov/articles/PMC3160252)
- Lee KK et al. 2011, Mol Syst Biol 7:503. [PMID:21734642](https://pubmed.ncbi.nlm.nih.gov/21734642/) / [doi:10.1038/msb.2011.40](https://doi.org/10.1038/msb.2011.40)
- Shukla A et al. 2012, Biochemistry 51:706–14. [PMID:22224423](https://pubmed.ncbi.nlm.nih.gov/22224423/) / [PMC3264703](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264703)
- Ringel AE et al. 2015, PNAS 112:E5461–70. [PMID:26401015](https://pubmed.ncbi.nlm.nih.gov/26401015/) / [PMC4603478](https://pmc.ncbi.nlm.nih.gov/articles/PMC4603478)
- Kamata K et al. 2013/2014, J Biochem. [PMID:24307402](https://pubmed.ncbi.nlm.nih.gov/24307402/)
- Nuño-Cabanes C et al. 2023, "The SAGA HAT module is tethered by its SWIRM domain and modulates activity of the SAGA DUB module". [PMC10226619](https://pmc.ncbi.nlm.nih.gov/articles/PMC10226619/)
- Wang H et al. 2020, Nature, "Structure of the transcription coactivator SAGA". [PMID:31969703](https://pubmed.ncbi.nlm.nih.gov/31969703/)
- Schram AW et al. 2013, PLoS ONE (human SGF29). [PMC3720948](https://pmc.ncbi.nlm.nih.gov/articles/PMC3720948/)
- UniProt [P25554](https://www.uniprot.org/uniprotkb/P25554) and SGD [SGF29](https://www.yeastgenome.org/locus/SGF29)
- PDB [3MEA](https://www.rcsb.org/structure/3MEA) (yeast Sgf29 with H3K4me2/3 peptides) and [3ME9](https://rcsb.org/structure/3ME9) (human)

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/21685874/
2. https://www.rcsb.org/structure/3MEA
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC10226619/
4. https://pubmed.ncbi.nlm.nih.gov/21734642/
5. https://pubmed.ncbi.nlm.nih.gov/31969703/
6. https://pubmed.ncbi.nlm.nih.gov/26401015/
7. https://pubmed.ncbi.nlm.nih.gov/22224423/
8. https://pubmed.ncbi.nlm.nih.gov/24307402/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3720948/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3160252
11. https://doi.org/10.1038/msb.2011.40
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC3264703
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC4603478
14. https://www.uniprot.org/uniprotkb/P25554
15. https://www.yeastgenome.org/locus/SGF29
16. https://rcsb.org/structure/3ME9