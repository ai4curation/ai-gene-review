---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:21:44.856473'
end_time: '2026-11-18T15:24:33.252802'
duration_seconds: 168.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: NTO1
  gene_symbol: NTO1
  uniprot_accession: Q12311
  protein_description: 'RecName: Full=NuA3 HAT complex component NTO1;'
  gene_info: Name=NTO1; OrderedLocusNames=YPR031W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Not specified in UniProt
  protein_domains: Enhancer_polycomb-like_N. (IPR019542); EPHD. (IPR034732); Histone_Mod_Regulator.
    (IPR050701); Zinc_finger_PHD-type_CS. (IPR019786); Znf_FYVE_PHD. (IPR011011)
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
  num_turns: 24
  total_cost_usd: 1.871425
  session_id: 7acc2ab2-b588-42f3-a7f4-0f54aa51b678
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q12311
- **Protein Description:** RecName: Full=NuA3 HAT complex component NTO1;
- **Gene Information:** Name=NTO1; OrderedLocusNames=YPR031W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Enhancer_polycomb-like_N. (IPR019542); EPHD. (IPR034732); Histone_Mod_Regulator. (IPR050701); Zinc_finger_PHD-type_CS. (IPR019786); Znf_FYVE_PHD. (IPR011011)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NTO1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NTO1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NTO1** (gene ID: NTO1, UniProt: Q12311) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Web fetches of the papers were blocked, so I'm pulling Nto1 details from the locally cached publications and Europe PMC instead.

# NTO1 (YPR031W; UniProt Q12311) in *Saccharomyces cerevisiae*: research report for functional annotation

## Scope and source access

Target identity is confirmed: NTO1/YPR031W encodes the "NuA3 HAT complex component NTO1" of *S. cerevisiae* S288c, and the literature found (NuA3, Sas3, PHD fingers, Epc-N domain) matches the UniProt domains. No conflicting gene with this symbol was encountered.

Full-text access was limited in this session. PubMed, PMC, Nature and Springer pages were blocked, and the locally cached copies of the key papers are abstract-only. Claims below therefore rest on abstracts, the UniProt record, the SGD description, PDB entries and search-result excerpts of full text. Items I could not verify are marked as such.

## 1. Summary

Nto1 is a non-catalytic scaffold subunit of NuA3, the Sas3-dependent histone H3 acetyltransferase complex of budding yeast. It has no enzymatic activity of its own. Its established roles are:

- **Complex core:** it forms the structural core of NuA3 together with the catalytic subunit Sas3.
- **Substrate-binding cleft:** its PHD-finger region forms one wall of the histone H3 tail-binding cleft that positions H3K14 for acetylation.
- **Subunit bridge:** a C-terminal helix anchors Yng1 and Eaf6 in a helical bundle.
- **Histone reader (weak):** one PHD finger binds H3K36me3 in vitro, though weakly.

It acts in the nucleus on chromatin of actively transcribed RNA polymerase II genes.

## 2. Key concepts and definitions

### The NuA3 complex

- NuA3 is a MYST-family histone acetyltransferase complex whose catalytic subunit is Sas3, the yeast counterpart of human MOZ/MORF (John et al., Genes Dev 2000, PMID:10817755).
- UniProt lists the NuA3a form as "composed of at least NTO1, SAS3, TAF14, YNG1 and EAF6", citing Taverna et al. 2006 (PMID:17157260).
- One full-text excerpt gives the stable complex as five proteins: Sas3 (98 kDa), Nto1 (86 kDa), Taf30/Taf14 (27 kDa), Yng1 (25 kDa) and Eaf6 (13 kDa). I could not confirm which paper this excerpt comes from.
- A second form, NuA3b, contains the additional PWWP-domain subunit Pdp3 (Gilbert et al., Mol Cell Proteomics 2014, PMID:25104842).

### Two functional forms (per UniProt, citing PMID:17157260 and PMID:25104842)

| Form | Extra subunit | Mark read | Reader | Where it acts | Proposed role |
|---|---|---|---|---|---|
| NuA3a | none | H3K4me3 | Yng1 PHD finger | Promoters / 5′ regions of active genes | H3K14 acetylation, transcription initiation |
| NuA3b | Pdp3 | H3K36me3 | Pdp3 PWWP domain | Coding regions of active genes | Transcription elongation |

Nto1 is present in both forms; SGD annotates it by direct assay to NuA3, NuA3a and NuA3b.

### Domain architecture of Nto1

- UniProt annotates three zinc-finger features at residues 263–313, 317–350 and 374–439. Pfam assigns these as PHD_2 (PF13831) and zf-HC5HC2H_2 (PF13832), with InterPro "EPHD" (extended PHD, IPR034732).
- This PHD–zinc knuckle–extended PHD arrangement is the "PZP" module found in BRPF and JADE proteins; the 2025 cryo-EM work reportedly uses this name for the Nto1 region that contacts the H3 tail, though I saw this only in a secondary summary.
- An Epc-N (Enhancer of Polycomb N-terminal-like) domain (Pfam PF10513 EPL1; IPR019542) surrounds the PHD fingers. UniProt notes that residues 156–543 "compose a region conserved in chromatin associated proteins" (Perry, BMC Genomics 2006, PMID:16412250).
- An excerpt, apparently from that analysis, describes Nto1 as having "two PHD fingers surrounded by an interrupted Epc-N domain" predicted to fold into a bromodomain-like helical structure with potential acetyl-lysine binding. That binding is a prediction, not an experimental result.
- PANTHER places Nto1 in PTHR13793 (PHD finger proteins), subfamily SF107.

### Orthology

The mammalian homologs of Nto1 are the JADE1/2/3 and BRPF1/2/3 scaffold proteins. These assemble HBO1 and MOZ/MORF acetyltransferase complexes with ING4/5 and hEaf6 (Doyon et al., Mol Cell 2006, cited in secondary excerpts; not directly accessed). NuA3 is thus the yeast version of a conserved four-part MYST module: catalytic subunit, Epc-N/PZP scaffold, ING-family reader and Eaf6.

## 3. Molecular function

### 3.1 Scaffold and co-former of the substrate-binding cleft (strongest evidence)

Shi et al. (Nat Commun 2025, DOI:10.1038/s41467-025-67049-0, PMID:41318527, PMC12789522) solved cryo-EM structures of NuA3 in three states:

| State | PDB | Resolution |
|---|---|---|
| Apo | 9UUO | 3.68 Å |
| Acetyl-CoA bound | 9VKW | 3.13 Å |
| Acetyl-CoA plus H3 tail | 9UUS | 3.20 Å |

Findings relevant to Nto1, from the abstract and full-text excerpts:

- **Core formation:** "Sas3, the catalytic subunit, interacts with Nto1, a non-catalytic subunit, mainly through its N-terminal domain, together forming the core of the NuA3 complex."
- **Shared cleft:** "The histone tail-binding cleft of NuA3 is formed cooperatively by the catalytic subunit Sas3 and the non-catalytic subunit Nto1."
- **Tail contacts:** Nto1 residues Ile298, Phe299 and Tyr357, together with a Met585 (apparently of Sas3), engage H3 residues 9–12 through hydrophobic contacts.
- **Site specificity:** polar contacts with the backbone of H3 residues 12–15, especially Gly13, help select K14.
- **Helical bundle:** two N-terminal helices of Yng1, a long C-terminal helix of Nto1 (residues 550–603) and Eaf6 assemble into a helical bundle.
- **Catalysis stays with Sas3:** the catalytic residues are Sas3 Cys418 and Glu452.

The paper also tested NuA3 mutants for H3K14 acetylation in BY4741 cells. I could not retrieve the results for individual Nto1 mutants.

The best-fitting description of Nto1's molecular function is therefore a structural adaptor/scaffold within an acetyltransferase complex that contributes to histone H3 substrate binding. It contributes to, but does not itself enable, histone H3K14 acetyltransferase activity.

### 3.2 Histone methyl-lysine reading (weaker evidence)

- Shi et al. (J Biol Chem 2007, PMID:17142463) surveyed all yeast PHD fingers and concluded that PHD fingers are effector modules for H3K4me3 and H3K36me3. This is the source of the Nto1 PHD–H3K36me3 interaction and of the SGD IDA annotation to histone H3K36me3 reader activity (GO:0140003).
- Later authors describe this binding as weak: "a PHD finger of Nto1 is known to weakly bind to H3K36me3 in vitro" (Kim et al., NAR 2020).
- In vivo, H3K36me3-dependent recruitment of NuA3 is attributed to the Pdp3 PWWP domain. Martin et al. (Genetics 2017) concluded that the Yng1 PHD finger and Pdp3 PWWP domain independently target NuA3 to H3K4- and H3K36-methylated chromatin.
- Functional support for the Nto1 PHD finger comes from Kim et al. (NAR 2020, 48:10753–10767, DOI:10.1093/nar/gkaa781). Mutation of the Yng1 N-terminal region, the Nto1 PHD finger or Pdp3 reduced or delayed induction of mRNAs and lncRNAs repressed by the Set2–Rpd3S pathway during carbon-source shifts, without changing basal levels.
- The 2025 structure adds a caveat: the same PHD-finger region contacts unmodified H3 residues 9–12 in the catalytic cleft. A PHD-finger mutant phenotype may therefore reflect loss of substrate engagement and not only loss of H3K36me3 reading. This is my inference from the two papers; neither states it in the excerpts I saw.

### 3.3 Zinc binding

The PHD fingers are zinc-coordinating by definition; the GOA zinc ion binding row is a computational (RCA) annotation with no direct assay behind it.

## 4. Biological process and pathway role

- **Histone H3 acetylation at transcribed genes.** Structural and biochemical work is consistent in assigning H3K14 as the principal NuA3 target (Taverna 2006; Shi 2025). H3K23 is also cited as a target in the Martin 2017 introduction.
- **Coupling methylation to acetylation.** NuA3 is recruited by H3K4 and H3K36 methylation, linking Set1- and Set2-dependent marks to H3 acetylation. Loss of both marks abolishes NuA3 recruitment to transcribed genes; loss of either gives partial loss (Martin 2017).
- **Occupancy is not sufficient.** "NuA3 occupancy does not dictate histone acetylation", so targeting is not the only level of control (Martin 2017).
- **Antagonism of Rpd3 deacetylases.** NuA3 opposes the Rpd3S and Rpd3L HDACs to tune the kinetics of gene induction (Kim 2020). This is the clearest process-level phenotype tied specifically to an Nto1 mutation.
- **Taf14 integration.** Taf14 binds motifs in both Sas3 and Yng1, and these contacts are needed for NuA3 function in transcription and DNA repair (Nat Commun 2024, DOI:10.1038/s41467-024-49730-y). No Nto1-specific result was retrieved from this paper.
- **Taf14 YEATS domain.** It binds H3K9ac/H3K9cr in vitro, but Martin 2017 found no evidence that it recruits NuA3.

The current GOA "chromatin remodeling" rows (IPI and IBA) reflect GO's broad use of that term for histone modification; NuA3 is not an ATP-dependent remodeler. The precise process is histone H3 acetylation in support of RNA polymerase II transcription.

## 5. Localization

- A genome-wide GFP-fusion study localised Nto1 to both nucleus and cytoplasm (Huh et al., Nature 2003, PMID:14562095); this is high-throughput evidence.
- All functional data place the protein on nuclear chromatin: promoters/5′ ends (NuA3a) and gene bodies (NuA3b) of active genes. The nucleus is where the function is carried out; the cytoplasmic signal has no known functional meaning.
- Abundance is low, about 172 molecules per cell in log phase (Ghaemmaghami et al., Nature 2003, PMID:14562106).
- Nto1 is listed among Cdk1 substrates in a phosphoproteomic screen (Holt et al., Science 2009, PMID:19779198). No functional consequence is known.

## 6. Recent developments (2023–2025)

| Year | Study | Advance |
|---|---|---|
| 2024 | Nat Commun, DOI:10.1038/s41467-024-49730-y | Structural basis of Taf14 binding to Sas3 and Yng1; both contacts needed in vivo |
| 2025 | Shi et al., Nat Commun, PMID:41318527 | First cryo-EM structures of NuA3; Nto1 shown to co-form the H3 tail cleft with Sas3 |

The 2025 structure moves Nto1 from "PHD-finger subunit of uncertain role" to a defined architectural and substrate-positioning component. One citation detail is unresolved: PDBj lists the DOI above, while RCSB cites the paper as Nat Commun 17:342. Check the volume before citing.

## 7. Evidence assessment and open questions

| Claim | Evidence type | Strength |
|---|---|---|
| Stable NuA3a/NuA3b subunit | Affinity purification/MS; cryo-EM | Strong |
| Forms complex core with Sas3 | Cryo-EM | Strong |
| Co-forms H3 tail cleft (I298, F299, Y357) | Cryo-EM with H3 tail | Strong structurally; mutant data not retrieved |
| Bridges Yng1 and Eaf6 via C-terminal helix | Cryo-EM | Strong |
| H3K36me3 reader | In vitro peptide binding, described as weak | Moderate to weak |
| PHD finger needed for timely gene induction | Point mutant, expression kinetics | Moderate |
| Acetyl-lysine binding by Epc-N region | Sequence/fold prediction only | Speculative |
| Nuclear site of action | HT localisation plus function | Strong |

Open questions I could not resolve from accessible sources:

- Whether *nto1Δ* disrupts NuA3 integrity, Sas3 stability or bulk H3K14ac. The cryo-EM architecture predicts it would, but I found no direct test.
- Whether *nto1Δ* reproduces the synthetic lethality of *sas3Δ* with *gcn5Δ*.
- Which of the two PHD fingers binds H3K36me3, and with what affinity.
- Whether Nto1 influences Sas3 site specificity (K14 versus K23), as BRPF/JADE scaffolds do for HBO1.
- The origin of the name NTO1 and which paper first assigned it. UniProt's subunit attribution points to Taverna 2006, but I could not confirm the naming.

## 8. Implications for GO annotation

- **Molecular function:** a scaffold/adaptor term within the acetyltransferase complex is better supported than a pure reader term. The H3K36me3 reader activity is experimentally reported but weak and secondary.
- **Contributes-to:** histone H3K14 acetyltransferase activity, as a cleft-forming subunit of the complex.
- **Complex membership:** NuA3, NuA3a and NuA3b are all well supported.
- **Process:** regulation of RNA polymerase II transcription through histone H3 acetylation; "chromatin remodeling" is true only in GO's broad sense.
- **Location:** nucleus/chromatin; the cytoplasm row rests on a single high-throughput observation.

## Sources

- [Shi et al. 2025, Nat Commun — NuA3 cryo-EM (PMC12789522)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12789522/)
- [Shi et al. 2025 — Nature article page](https://www.nature.com/articles/s41467-025-67049-0)
- [Shi et al. 2025 — PubMed 41318527](https://pubmed.ncbi.nlm.nih.gov/41318527/)
- [PDB 9UUO — apo NuA3](https://www.rcsb.org/structure/9UUO)
- [PDB 9UUS — NuA3 with acetyl-CoA and H3 tail](https://www.rcsb.org/structure/9UUS)
- [PDB 9VKW — NuA3 with acetyl-CoA](https://rcsb.org/structure/9VKW)
- [Nat Commun 2024 — Taf14 interactions with Sas3 and Yng1](https://link.springer.com/article/10.1038/s41467-024-49730-y)
- [Kim et al. 2020, NAR — NuA3 antagonises Rpd3S/Rpd3L (PMC7641726)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7641726)
- [Martin et al. 2017, Genetics — H3K4/H3K36 methylation recruit NuA3 (PMC5340327)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340327)
- [Martin et al. — bioRxiv preprint](https://www.biorxiv.org/content/early/2016/12/23/096511)
- [Gilbert et al. 2014, Mol Cell Proteomics — Pdp3/NuA3b (BioGRID record)](https://thebiogrid.org/196834/publication/a-pwwp-domain-containing-protein-targets-the-nua3-acetyltransferase-complex-via-histone-h3-lysine-36-trimethylation-to-coordinate-transcriptional-elongation-at-coding-regions.html)
- [Shi et al. 2007, J Biol Chem — yeast PHD finger survey (PMC2735445)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2735445)
- [Shi et al. 2007 — SGD reference page](https://www.yeastgenome.org/reference/17142463)
- [Taverna et al. 2006, Mol Cell — Yng1 PHD/H3K4me3 and NuA3](https://www.researchgate.net/publication/6642820_Yng1_PHD_finger_binding_to_H3_trimethylated_at_K4_promotes_NuA3_HAT_activity_at_K14_of_H3_and_transcription_at_a_subset_of_targeted_ORFs)
- [John et al. 2000, Genes Dev — Sas3 is the catalytic subunit of NuA3 (PMC316621)](https://pmc.ncbi.nlm.nih.gov/articles/PMC316621/)
- [SGD — NuA3a complex GO term page](https://www.yeastgenome.org/go/GO:1990467)
- [SGD locus page for NTO1](https://www.yeastgenome.org/locus/NTO1)
- [BioGRID — NTO1–HHT1 interaction](https://thebiogrid.org/interaction/346148)
- UniProt Q12311 record and SGD gene description (local copies in `genes/yeast/NTO1/`)

## Citations

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12789522/
2. https://www.nature.com/articles/s41467-025-67049-0
3. https://pubmed.ncbi.nlm.nih.gov/41318527/
4. https://www.rcsb.org/structure/9UUO
5. https://www.rcsb.org/structure/9UUS
6. https://rcsb.org/structure/9VKW
7. https://link.springer.com/article/10.1038/s41467-024-49730-y
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC7641726
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC5340327
10. https://www.biorxiv.org/content/early/2016/12/23/096511
11. https://thebiogrid.org/196834/publication/a-pwwp-domain-containing-protein-targets-the-nua3-acetyltransferase-complex-via-histone-h3-lysine-36-trimethylation-to-coordinate-transcriptional-elongation-at-coding-regions.html
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC2735445
13. https://www.yeastgenome.org/reference/17142463
14. https://www.researchgate.net/publication/6642820_Yng1_PHD_finger_binding_to_H3_trimethylated_at_K4_promotes_NuA3_HAT_activity_at_K14_of_H3_and_transcription_at_a_subset_of_targeted_ORFs
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC316621/
16. https://www.yeastgenome.org/go/GO:1990467
17. https://www.yeastgenome.org/locus/NTO1
18. https://thebiogrid.org/interaction/346148