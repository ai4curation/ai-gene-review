---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:19:53.952396'
end_time: '2026-11-18T15:21:41.590138'
duration_seconds: 107.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: YNG2
  gene_symbol: YNG2
  uniprot_accession: P38806
  protein_description: 'RecName: Full=Chromatin modification-related protein YNG2;
    AltName: Full=ESA1-associated factor 4; AltName: Full=ING1 homolog 2;'
  gene_info: Name=YNG2; Synonyms=EAF4, NBN1; OrderedLocusNames=YHR090C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the ING family. .
  protein_domains: ING_fam. (IPR028651); ING_N_histone-binding. (IPR024610); Zinc_finger_PHD-type_CS.
    (IPR019786); Znf_FYVE_PHD. (IPR011011); Znf_PHD. (IPR001965)
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
  web_search_requests: 10
  num_turns: 15
  total_cost_usd: 1.9671011
  session_id: ec732f0c-91d6-43e3-950c-6278e73957a6
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P38806
- **Protein Description:** RecName: Full=Chromatin modification-related protein YNG2; AltName: Full=ESA1-associated factor 4; AltName: Full=ING1 homolog 2;
- **Gene Information:** Name=YNG2; Synonyms=EAF4, NBN1; OrderedLocusNames=YHR090C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the ING family. .
- **Key Domains:** ING_fam. (IPR028651); ING_N_histone-binding. (IPR024610); Zinc_finger_PHD-type_CS. (IPR019786); Znf_FYVE_PHD. (IPR011011); Znf_PHD. (IPR001965)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "YNG2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'YNG2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **YNG2** (gene ID: YNG2, UniProt: P38806) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# YNG2 (P38806, YHR090C) in *Saccharomyces cerevisiae*: research report for functional annotation

## Identity check

The symbol YNG2 (synonyms EAF4, NBN1; ORF YHR090C) is unambiguous and matches UniProt P38806, "Chromatin modification-related protein YNG2". The literature found is all about the *S. cerevisiae* NuA4 subunit, an ING-family protein with an N-terminal ING histone-binding region and a C-terminal PHD finger. This agrees with the UniProt family and domain assignments, and no conflicting gene of the same symbol was found.

**Evidence basis.** This report rests on the local UniProt record, the SGD gene description, the GOA file, and web-search abstracts and database summaries. I did not read full texts. The local publication cache has abstracts only for PMID:10805724 and PMID:16728974, and no cached file for PMID:11544250, PMID:11604499 or PMID:12417725. Statements I could only recall from memory are marked as such, and I give PMIDs only where a source confirmed them.

## 1. Summary

Yng2 is a non-catalytic, stoichiometric subunit of the NuA4 histone acetyltransferase complex. It sits in the catalytic "piccolo" HAT module with Esa1 (the catalytic subunit), Epl1 and Eaf6. Its primary function is twofold:

- **Structural and activating cofactor.** It is needed for normal levels and activity of NuA4 on nucleosomal H4 and H2A (and H2A.Z).
- **Histone reader.** Its PHD finger binds H3K4me3 (more weakly H3K4me2) and directs H4 acetylation to nucleosomes near transcription start sites.

It acts in the nucleus on chromatin. Its downstream roles are in transcriptional activation, the response to DNA damage during S phase, DNA double-strand break repair, and mitotic and meiotic progression.

## 2. Molecular function

### 2.1 Subunit of NuA4 and piccolo NuA4

- **Discovery.** Three yeast proteins related to human p33(ING1), namely Yng1, Yng2 and Pho23, were shown to associate with distinct HAT activities; Yng2 associates with the Esa1/NuA4 activity (Loewith et al. 2000, PMID:10805724).
- **Stoichiometric subunit.** Mass spectrometry, immunoblotting and immunoprecipitation showed stable, stoichiometric association of Yng2 with purified NuA4 (Nourani et al. 2001, PMID:11604499, [PMC99934](https://pmc.ncbi.nlm.nih.gov/articles/PMC99934)).
- **Complex composition.** UniProt lists NuA4 as at least Act1, Arp4, Yaf9, Vid21/Eaf1, Swc4, Eaf3, Eaf5, Eaf6, Eaf7, Epl1, Esa1, Tra1 and Yng2 (PMID:15045029, PMID:15353583, PMID:15485911).
- **Piccolo NuA4.** Epl1 is found in NuA4 and in a smaller, highly active complex, picNuA4, containing Esa1, Epl1 and Yng2. picNuA4 strongly prefers chromatin over free histones. Epl1 bridges Esa1 and Yng2, and the trimer is sufficient for the essential function of Esa1 (Boudreault et al. 2003, *Genes Dev*, [PMC196073](https://pmc.ncbi.nlm.nih.gov/articles/PMC196073)).
- **Division of labour.** The same study proposed that picNuA4 carries out global, non-targeted H4/H2A acetylation, while holo-NuA4 is recruited to specific loci.
- **Direct partner.** IntAct records Epl1 as Yng2's binary partner (11 experiments), consistent with the Epl1 N-terminal EPcA domain organising the module ([Searle & Pillus review, PMC5340328](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328)).

### 2.2 Yng2 is a cofactor, not the enzyme

The reaction is acetyl-CoA + histone lysine → CoA + N6-acetyl-lysine, catalysed by the MYST acetyltransferase Esa1. Yng2 has no acetyltransferase domain.

- **Loss-of-function biochemistry.** NuA4 purified from *yng2Δ* cells is low in abundance and has weak HAT activity (PMID:11604499). Choy et al. found the complex still present without Yng2 and concluded Yng2 maintains or activates NuA4 HAT activity (PMID:11544250).
- **Global acetylation.** *yng2* mutants are viable but specifically compromised in global nucleosomal H4 acetylation (Choy & Kron 2002, PMID:12417725, [PMC134065](https://pmc.ncbi.nlm.nih.gov/articles/PMC134065)).
- **SGD wording.** SGD describes Yng2 as the subunit that "positions Piccolo NuA4 for efficient acetylation of histone H4 or histone H2A".
- **Annotation implication.** The GOA row `GO:0004402 histone acetyltransferase activity` (IDA) is best read as an activity of the complex to which Yng2 contributes. The cofactor/adaptor and reader activities are Yng2's own.

### 2.3 Structural evidence

- **Crystal and cryo-EM, 2016.** Xu et al. solved crystal structures of the NuA4 core (Esa1, Epl1, Yng2, Eaf6) and a cryo-EM structure with the nucleosome (*Mol Cell* 63:965–975, doi:10.1016/j.molcel.2016.07.024; PDB [5J9Q](https://www.rcsb.org/structure/5J9Q), 5J9T, 5J9U, 5J9W). Esa1 is activated through interactions with Epl1. The authors describe a "space-sequence double recognition" of the H4 tail.
- **Holo-complex, 2022.** Qu et al. (*Nature*, doi:10.1038/s41586-022-05303-x; PDB 7VVU/7VVY/7VVZ) show the HAT module contacting the nucleosome disk face through the H2A–H2B acidic patch and nucleosomal DNA, positioning the Esa1 pocket toward the H4 tail.
- **Flexibility.** Zukin et al. ([eLife 2022, 81400](https://elifesciences.org/articles/81400)) describe a rigid Tra1-containing hub with flexibly attached HAT and TINTIN modules. They propose Tra1 recruits NuA4 before the HAT module engages.
- **Piccolo on H2A.Z nucleosomes, 2025.** Wang et al. (*PNAS*, doi:10.1073/pnas.2414490122; PDB [8X2X](https://www.rcsb.org/structure/8X2X)–8X32) report seven cryo-EM structures with and without acetyl-CoA. The constructs include a 120-residue Yng2 chain, presumably the N-terminal region (the PDB summaries do not say).
- **From memory, not checked here.** I recall the Yng2 N-terminal region forming a helical bundle with Eaf6 and Epl1, and the PHD finger being absent or unresolved in these structures.

### 2.4 H3K4me3 reader activity of the PHD finger

- **Binding.** The Yng2 PHD finger binds H3K4me3 and, more weakly, H3K4me2. This was shown in the study that defined ING-family PHD fingers as H3K4me3 readers (Shi et al. 2006, PMID:16728974), and is the basis of the IDA rows for `GO:0140002 histone H3K4me3 reader activity`.
- **Not a recruitment signal at promoters.** Genome-wide ChIP-seq found that Yng2–H3K4me3 binding does not significantly affect NuA4 occupancy at promoters. It is important for H4 acetylation near the TSS of highly expressed genes. The authors propose the reader modules orient the catalytic site toward methylated nucleosomes ([Steunou et al. 2016, PMC5086519](https://pmc.ncbi.nlm.nih.gov/articles/PMC5086519); GEO GSE77945).
- **Different result at DSBs.** Combined loss of the Yng2 PHD and the Eaf3 chromodomain impairs NuA4 recruitment and reduces H4K12 acetylation at a double-strand break ([PMC4701104](https://pmc.ncbi.nlm.nih.gov/articles/PMC4701104)). The two contexts differ, so the findings need not conflict.
- **Earlier PHD data.** The PHD finger is dispensable for p53 interaction but needed for full expression of a p53-responsive reporter and other NuA4 targets (PMID:11604499).
- **Zinc binding.** The `GO:0008270` row is a structural inference (RCA); PHD fingers coordinate two Zn²⁺ ions.

## 3. Biological processes

| Process | Key evidence | Source |
|---|---|---|
| Transcriptional activation | *yng2Δ* has gene-specific transcription defects; p53-driven activation in yeast is linked to targeted NuA4-dependent H4 hyperacetylation with H3 unchanged | PMID:11604499 |
| Global H4/H2A acetylation | *yng2* mutants lose global nucleosomal H4 acetylation; picNuA4 proposed as the global activity | PMID:12417725; PMC196073 |
| Intra-S-phase DNA damage response | Mutants are sensitive to hydroxyurea, camptothecin, MMS and *cdc8*/*cdc9* mutations; MMS causes a persistent Mec1-dependent intra-S checkpoint delay with slow repair | PMID:12417725 |
| DSB repair | Yng2 PHD plus Eaf3 chromodomain support NuA4 recruitment and H4K12ac at a DSB | PMC4701104 |
| Mitotic progression | Synchronised *yng2* cells show a mitotic delay, relieved by nocodazole arrest and release | PMID:11544250 |
| Meiosis | Diploid *yng2* mutants show a defect in meiotic progression during sporulation | PMID:11544250 |

Notes on interpretation:

- **Acetylation is the mechanism.** Trichostatin A restores global H4 acetylation and suppresses both the mitotic delay (PMID:11544250) and the checkpoint-recovery defect (PMID:12417725). This ties the phenotypes to reduced H4 acetylation rather than to an acetylation-independent role.
- **Transcription versus genome integrity.** Choy et al. reported little genome-wide expression change in *yng2* mutants (PMID:11544250), while Nourani et al. reported gene-specific defects (PMID:11604499). The *yng2* G2/M delay is DNA-damage-checkpoint dependent (PMID:12417725), so the cell-cycle phenotypes likely reflect replication-associated damage.
- **H2A.Z link.** NuA4 acetylates Htz1 and cooperates with SWR1 in chromosome stability (PMID:15353583, PMID:15485911). These papers establish Yng2's NuA4 membership rather than a Yng2-specific role.
- **Broad GO terms.** `chromatin remodeling` (IEA) and `chromatin organization` (IBA) are generic. Histone H4/H2A acetylation and transcriptional regulation are the specific supported processes.

## 4. Regulation of Yng2

A systematic genetic-interaction study of yeast HATs and HDACs reported acetylation-dependent stabilisation of Yng2, a potential non-histone substrate of NuA4 and the Rpd3 complex (Lin et al. 2008, PMID:18676811, [PMC2492751](https://pmc.ncbi.nlm.nih.gov/articles/PMC2492751)). A review summarises this as Esa1 acetylating and stabilising Yng2. The search snippets did not name the degradation pathway.

Yng2 is also a phosphoprotein in proteomic datasets, including a Cdk1 substrate screen (PMID:18407956, PMID:19779198). No functional consequence was found.

## 5. Localisation

- **Nucleus.** Supported by directed studies and the genome-wide GFP collection (PMID:10805724, PMID:11544250, PMID:14562095). The functional site is chromatin, on nucleosomes at promoters and TSS-proximal regions and at DNA lesions.
- **Nucleosome.** The `GO:0000786` IDA row from ComplexPortal reflects direct engagement of the HAT module with the nucleosome, consistent with the structures above.
- **Cytosol.** SGD states that Yng2 "relocalizes to the cytosol in response to hypoxia", which is the likely basis of the `GO:0005829` IDA row. A study reporting that hypoxia redistributes 203 yeast proteins exists ([PMC3191569](https://pmc.ncbi.nlm.nih.gov/articles/PMC3191569)), but I could not confirm that Yng2 is in it. This is a stress-conditional, high-throughput observation and not a site of function.

## 6. Evolution and family context

Yng2 belongs to the ING family (IPR028651), with the N-terminal ING histone-binding domain (IPR024610) and a C-terminal PHD finger (IPR001965, IPR019786). Yeast has three ING proteins, each dedicated to a different complex: Yng1 (NuA3), Yng2 (NuA4) and Pho23 (Rpd3L) (PMID:10805724). SGD notes similarity to human ING1, ING4 and ING5. From memory, the functional counterpart in the human NuA4/TIP60 complex is ING3; this was not checked in this session.

The IBA rows (nucleus, NuA4 complex, H3K4me3 reader activity, regulation of transcription) are all consistent with direct experimental evidence on Yng2 itself.

## 7. Suggested annotation picture

- **Core molecular function:** histone H3K4me3 reader activity (`GO:0140002`), plus a contributing, non-catalytic role in the H4/H2A acetyltransferase activity of NuA4.
- **Core complexes:** NuA4 histone acetyltransferase complex (`GO:0035267`) and piccolo NuA4 (`GO:0032777`).
- **Core location:** nucleus, on chromatin.
- **Core processes:** histone H4/H2A acetylation in transcriptional activation; DNA damage response and repair.
- **Peripheral or secondary:** mitotic and meiotic progression (downstream of acetylation loss); cytosol under hypoxia.
- **Uninformative:** the six bare `protein binding` IPI rows.

## 8. Open questions

- Which Yng2 residues are acetylated by Esa1 and deacetylated by Rpd3, and what degrades the unacetylated protein?
- How does the PHD finger, which appears flexible in the structures, orient the Esa1 active site on H3K4me3 nucleosomes?
- Does Yng2 have a distinct role in picNuA4 versus holo-NuA4?
- Is the meiotic defect a direct chromatin requirement or secondary to replication stress?

## Sources

- [UniProt P38806 (YNG2_YEAST)](https://uniprot.org/uniprotkb/P38806/entry)
- [SGD YNG2 locus page](https://www.yeastgenome.org/locus/YNG2)
- Loewith et al. 2000, *Mol Cell Biol* 20:3807–3816, PMID:10805724, [PMC85704](https://pmc.ncbi.nlm.nih.gov/articles/PMC85704)
- Choy et al. 2001, *J Biol Chem* 276:43653–43662, PMID:11544250, [SGD reference](https://www.yeastgenome.org/reference/S000068990)
- Nourani et al. 2001, *Mol Cell Biol* 21:7629–7640, PMID:11604499, [PMC99934](https://pmc.ncbi.nlm.nih.gov/articles/PMC99934)
- Choy & Kron 2002, *Mol Cell Biol* 22:8215–8225, PMID:12417725, [PMC134065](https://pmc.ncbi.nlm.nih.gov/articles/PMC134065)
- Boudreault et al. 2003, *Genes Dev*, doi:10.1101/gad.1056603, [PMC196073](https://pmc.ncbi.nlm.nih.gov/articles/PMC196073)
- Shi et al. 2006, *Nature*, PMID:16728974, doi:10.1038/nature04835
- Lin et al. 2008, *Genes Dev* 22:2062, PMID:18676811, [PMC2492751](https://pmc.ncbi.nlm.nih.gov/articles/PMC2492751)
- Xu et al. 2016, *Mol Cell* 63:965–975, doi:10.1016/j.molcel.2016.07.024, [PDB 5J9Q](https://www.rcsb.org/structure/5J9Q)
- Steunou et al. 2016, *Mol Cell Biol*, [PMC5086519](https://pmc.ncbi.nlm.nih.gov/articles/PMC5086519); [GEO GSE77945](https://omicsdi.org/dataset/geo/GSE77945)
- NuA4 reader modules at DSBs, [PMC4701104](https://pmc.ncbi.nlm.nih.gov/articles/PMC4701104)
- Qu et al. 2022, *Nature* 610, [doi:10.1038/s41586-022-05303-x](https://www.nature.com/articles/s41586-022-05303-x.pdf); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2022.07.12.499507.full.pdf)
- Zukin et al. 2022, *eLife* 11:e81400, [article](https://elifesciences.org/articles/81400); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2022.06.24.497536v1.full.pdf)
- Wang et al. 2025, *PNAS*, doi:10.1073/pnas.2414490122, [PDB 8X2X](https://www.rcsb.org/structure/8X2X), [8X30](https://www.rcsb.org/structure/8X30)
- Searle & Pillus reviews, [PMC5340328](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328), [PMC6287951](https://pmc.ncbi.nlm.nih.gov/articles/PMC6287951)
- Hypoxia protein relocalisation study, [PMC3191569](https://pmc.ncbi.nlm.nih.gov/articles/PMC3191569) (Yng2 inclusion not confirmed)
- NuA4 membership references cited by UniProt: PMID:15045029, PMID:15353583, PMID:15485911; localisation PMID:14562095

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC99934
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC196073
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC134065
5. https://www.rcsb.org/structure/5J9Q
6. https://elifesciences.org/articles/81400
7. https://www.rcsb.org/structure/8X2X
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC5086519
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC4701104
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2492751
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3191569
12. https://uniprot.org/uniprotkb/P38806/entry
13. https://www.yeastgenome.org/locus/YNG2
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC85704
15. https://www.yeastgenome.org/reference/S000068990
16. https://omicsdi.org/dataset/geo/GSE77945
17. https://www.nature.com/articles/s41586-022-05303-x.pdf
18. https://www.biorxiv.org/content/10.1101/2022.07.12.499507.full.pdf
19. https://www.biorxiv.org/content/10.1101/2022.06.24.497536v1.full.pdf
20. https://www.rcsb.org/structure/8X30
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC6287951