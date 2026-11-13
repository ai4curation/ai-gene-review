---
provider: claude_code
cached: false
start_time: '2026-11-13T00:08:52.726863'
end_time: '2026-11-13T00:10:26.412262'
duration_seconds: 93.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SNAP25
  gene_symbol: SNAP25
  uniprot_accession: P60880
  protein_description: 'RecName: Full=Synaptosomal-associated protein 25; Short=SNAP-25;
    AltName: Full=Super protein; Short=SUP; AltName: Full=Synaptosomal-associated
    25 kDa protein;'
  gene_info: Name=SNAP25; Synonyms=SNAP;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the SNAP-25 family. .
  protein_domains: SNAP-25_dom. (IPR000928); SNAP-25_N_SNARE_chord. (IPR039077); T_SNARE_dom.
    (IPR000727); SNAP-25 (PF00835); SNARE (PF05739)
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
  web_search_requests: 9
  num_turns: 12
  total_cost_usd: 1.3916800999999999
  session_id: feca520e-6778-4384-84fd-f9a268293c6b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P60880
- **Protein Description:** RecName: Full=Synaptosomal-associated protein 25; Short=SNAP-25; AltName: Full=Super protein; Short=SUP; AltName: Full=Synaptosomal-associated 25 kDa protein;
- **Gene Information:** Name=SNAP25; Synonyms=SNAP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the SNAP-25 family. .
- **Key Domains:** SNAP-25_dom. (IPR000928); SNAP-25_N_SNARE_chord. (IPR039077); T_SNARE_dom. (IPR000727); SNAP-25 (PF00835); SNARE (PF05739)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SNAP25" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SNAP25' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SNAP25** (gene ID: SNAP25, UniProt: P60880) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SNAP25 (human, UniProt P60880): research report for functional annotation

## Identity check

The target is unambiguous. *SNAP25* encodes Synaptosomal-associated protein 25 (SNAP-25), a 206-residue member of the SNAP-25 family with two t-SNARE coiled-coil homology domains (residues 19–81 and 140–202), matching the UniProt domain set (IPR000928, IPR000727, PF00835, PF05739). The literature found is on this protein; no conflicting gene with the same symbol turned up.

Sourcing: claims come from this session's web searches (abstracts and snippets, not full texts) and the local UniProt record. Statements marked "(background)" are from my own knowledge of the classic literature and were not re-verified here. PMIDs appear only where the local UniProt record or a search result gave them.

## 1. Primary molecular function: Qbc-SNARE of the neuronal fusion machine

SNAP-25 is not an enzyme or transporter. It is a structural component of the membrane fusion machinery: it contributes two of the four helices of the neuronal SNARE complex.

- **Core complex.** UniProt describes the SNARE core complex of SNAP25, VAMP2 and STX1A as "the basic catalytic machinery of the complex neurotransmitter release apparatus" (PMID:11832227). That paper also shows the complex binding complexin-1 (CPLX1); the structure is PDB 1KIL, with human SNAP-25 residues 11–81 and 139–203.
- **Structure.** The 2.4 Å crystal structure (Sutton et al., Nature 1998; PDB 1SFC, rat proteins) shows a twisted, parallel four-helix bundle. It has leucine-zipper-like layers and a central ionic layer of one arginine and three glutamines.
- **Q/R classification.** Fasshauer et al. 1998 (PMID:9861047) reclassified SNAREs on this basis: fusion-competent complexes have three Q-SNARE helices and one R-SNARE helix. SNAP-25 supplies two Q helices (Qb and Qc), syntaxin-1 supplies Qa, and VAMP2 supplies R.
- **Mechanism (background).** N-to-C zippering of the trans-SNARE complex pulls vesicle and plasma membranes together and supplies the energy for fusion. NSF and α-SNAP then disassemble the cis complex.

The best-fitting GO molecular function is SNAP receptor activity (with syntaxin binding), not generic protein binding.

## 2. Biological process: Ca²⁺-triggered regulated exocytosis

- **Genetic requirement.** In the mouse knockout (Washbourne et al., Nat Neurosci 2002), loss of SNAP-25 eliminates evoked release but not spontaneous release. Embryos develop to term with superficially normal brain development. Later culture work reported that about 10–12% of Ca²⁺-independent release persists.
- **Assembly and priming.** Munc18-1 and Munc13-1 act as a template for SNARE assembly (Wang et al., Nat Commun 2019, PMC6325239). SNAP-25 entry produces a half-zippered intermediate that releases syntaxin-1 from Munc18-1. A separate report has Munc13-1 binding SNAP-25 directly to recruit it; the order of these steps is still debated.
- **Ca²⁺ sensor coupling.** The synaptotagmin-1 C2B domain binds the partially assembled SNARE complex through the "primary interface", which is formed largely by SNAP-25 with syntaxin-1 (2023 review, PMC9623538).
- **Presynaptic inhibition by G proteins.** Gβγ binds the SNAP-25 C-terminus and the assembled complex, competing with synaptotagmin in a Ca²⁺-sensitive manner. This inhibits exocytosis downstream of Ca²⁺ entry. The SNAP-25 C-terminus is needed for presynaptic long-term depression but not long-term potentiation (PMC3102109), and SNAP25Δ3 mice lose this form of inhibition.
- **Neuroendocrine secretion.** UniProt records (by similarity to rodent orthologs) that SNAP-25 modulates gating of the KCNB1 (Kv2.1) potassium channel in pancreatic beta cells. A 2023 Frontiers in Endocrinology review covers SNAREs in hormone secretion.
- **Postsynaptic roles.** A review (Antonucci et al. 2016, PMC4805587) describes emerging postsynaptic functions. These are less established than the presynaptic role and are best treated as non-core.

## 3. Localization and membrane anchoring

- **No transmembrane domain.** SNAP-25 is a peripheral membrane protein on the cytoplasmic face of the plasma membrane. It is anchored by S-palmitoylation of a four-cysteine cluster (Cys85, Cys88, Cys90, Cys92; sequence 85-CGLCVCPC-92) in the linker between the two SNARE motifs.
- **Targeting.** Residues 85–120 are sufficient to target GFP to the plasma membrane. UniProt states that membrane association requires palmitoylation, with Cys85 as the main site.
- **Palmitoyltransferases.** The ankyrin-repeat domain of ZDHHC17 binds a linker motif (112-VVASQP-117); mutating Pro117 blocks binding, S-acylation and membrane targeting (PMID:28757145, PMID:28882895). Golgi-localized DHHC3, DHHC7 and DHHC17 all enhance membrane association.
- **Compartments.** UniProt lists cell membrane (lipid anchor), synaptosome, perinuclear cytoplasm and photoreceptor inner segment, all by similarity to rodent orthologs. One study proposes that dynamic palmitoylation lets SNAP-25 act at both the plasma membrane and endosomes.
- **Tissue.** Expression is neuronal: neocortex, hippocampus, piriform cortex, anterior thalamic nuclei, pontine nuclei and cerebellar granule cells (UniProt).

The site of action for the core function is the presynaptic plasma membrane at the active zone (background for the active-zone detail).

## 4. Isoforms

Two splice isoforms use alternative homologous exons 5a and 5b, encoding residues 56–94 and differing at 9 of 39 positions (UniProt). Isoform 1 is SNAP-25b (P60880-1, displayed); isoform 2 is SNAP-25a (P60880-2). Three of the nine differences lie in the cysteine-rich domain, and DHHC15 selectively increased membrane association of SNAP-25b in HEK293 cells. SNAP-25a predominates in development and SNAP-25b in mature brain (background).

## 5. Toxin substrate: direct evidence of function in humans

SNAP-25 is the substrate of three botulinum neurotoxin proteases, each of which blocks neurotransmitter release (UniProt):

| Toxin | Scissile bond | Reference |
|---|---|---|
| BoNT/A | Gln197–Arg198 | PMID:9886085, PMID:15592454 (structure 1XTG) |
| BoNT/C | Arg198–Ala199 | PMID:9886085, PMID:17718519 |
| BoNT/E | Arg180–Ile181 | PMID:9886085 |

Removing as few as nine C-terminal residues (BoNT/A) blocks release, which shows the importance of the C-terminal end of the SNARE motif. This is the basis of clinical botulinum toxin therapy.

## 6. Other interactions (mostly non-core)

- **PRRT2** binds SNAP-25 and may impair SNARE complex formation (PMID:22832103, PMID:25915028).
- **Alpha-synuclein (SNCA)** interacts with SNAP-25 (PMID:20798282).
- **BLOC-1** associates with SNAP-25 through BLOC1S6, for both isoforms (PMID:19546860).
- **By similarity only:** SYT1/SV2B, HSC70/DNAJC5, SNAPIN, RIMS1, OTOF, TRIM9, HGS, and CENPF (the basis of the "plasma membrane recycling" statement).
- **Artefact:** in E. coli, where palmitoylation is absent, the four cysteines form an iron-sulfur cluster (PMID:18375205). UniProt lists this under miscellaneous; it is not a physiological function.

## 7. Disease and recent developments (2020–2025)

- **Developmental and epileptic encephalopathy 117 (DEE117, MIM:616330).** Autosomal dominant, caused by de novo variants (UniProt, PMID:25381298).
- **Cohort.** Klöckner et al. (Genet Med 2021) described 23 individuals with intellectual disability and early-onset epilepsy as core features, plus movement disorders, cerebral visual impairment and brain atrophy. They proposed the term "SNAREopathies" for the overlap with STX1B, STXBP1 and VAMP2 disorders. Functional evidence in that paper was structural modelling only.
- **Spontaneous release as a mechanism.** Alten et al. (Neuron 2021, PMC7790958) found that structurally clustered SNARE-motif mutations cause similar defects. One mutation raised spontaneous release without changing evoked release.
- **Energy landscape.** Kádková et al. (eLife 2024, article 88619) studied V48F, D166Y and I67N. The variants change the energy landscape for priming and fusion, some with combined loss- and gain-of-function features.
- **Review.** Uzay and Kavalali (Front Synaptic Neurosci 2023) summarize how N-terminal, C-terminal and synaptotagmin-interface variants affect different release modes.
- **Biomarker use.** CSF SNAP-25 is elevated in Alzheimer's disease from early stages; the original study gave an area under the curve of 0.901 versus controls (Brinkmalm et al. 2014, PMC4253625). In 958 BioFINDER-2 participants, SNAP-25 was among the four best of 17 synaptic proteins for separating Alzheimer's dementia from controls, and the SNAP-25/NPTX2 ratio predicted cognitive decline and atrophy (Nilsson et al., Brain 2024, PMID:38325331). A 2025 study cautions that its correlation with p-tau limits diagnostic specificity.

## 8. Annotation-relevant summary

| Aspect | Best-supported assignment | Evidence |
|---|---|---|
| Molecular function | SNAP receptor (Qbc-SNARE) activity; syntaxin-1 binding | Structures 1SFC and 1KIL; toxin cleavage |
| Biological process | Synaptic vesicle priming and Ca²⁺-triggered exocytosis; regulated exocytosis in neuroendocrine cells | Mouse knockout; BoNT cleavage; human DEE variants |
| Location | Cytoplasmic face of presynaptic plasma membrane, palmitoyl-anchored; SNARE complex | Palmitoylation and targeting studies |
| Non-core or weaker | Postsynaptic roles, KCNB1 modulation, CENPF-linked recycling, BLOC-1, endosomal function | Mostly rodent or by similarity |

Most function and location statements in the human UniProt record are by similarity to mouse and rat. Direct human evidence is the complexin/SNARE structure, palmitoylation and ZDHHC17 binding, toxin cleavage sites, and disease variants.

## Sources

- Local UniProt flat file for P60880: `genes/human/SNAP25/SNAP25-uniprot.txt`
- [Sutton et al. 1998, SNARE complex structure (PDB 1SFC)](https://www.rcsb.org/structure/1SFC)
- [Fasshauer et al. 1998, Q- and R-SNAREs (PMID:9861047)](https://pubmed.ncbi.nlm.nih.gov/9861047/)
- [Washbourne et al. 2002, SNAP-25 knockout (Nat Neurosci)](https://www.nature.com/articles/nn783)
- [Differential effects of SNAP-25 deletion on Ca²⁺-dependent and -independent neurotransmission](https://pmc.ncbi.nlm.nih.gov/articles/PMC2739239)
- [Wang et al. 2019, Munc18 and Munc13 as a template for SNARE assembly](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6325239/)
- [Kalyanasundaram et al., Munc13-1 recruits SNAP25 (accepted manuscript)](https://discovery.ucl.ac.uk/10126208/1/Kalyanasundaram%20et%20al_Manuscript_Accepted.pdf)
- [Review of synaptotagmin–SNARE interactions, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9623538)
- [Zhang et al. 2011, Gβγ and the SNAP-25 C terminus in LTD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3102109/)
- [Gβγ–SNARE review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3432151)
- [Greaves et al., SNAP25 cysteine-rich domain and palmitoylation](https://pmc.ncbi.nlm.nih.gov/articles/PMC3065388)
- [Differential palmitoylation regulates intracellular patterning of SNAP25](https://pureportal.coventry.ac.uk/en/publications/differential-palmitoylation-regulates-intracellular-patterning-of/)
- [zDHHC17–SNAP25 zDABM study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7247313)
- [Antonucci et al. 2016, postsynaptic functions of SNAP-25](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4805587/)
- [Uzay and Kavalali 2023, genetic disorders of neurotransmitter release machinery](https://www.frontiersin.org/journals/synaptic-neuroscience/articles/10.3389/fnsyn.2023.1148957/full)
- [SNAREs in hormone secretion, Front Endocrinol 2023](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2023.1096365/full)
- [Kádková et al. 2024, eLife 88619](https://elifesciences.org/articles/88619.pdf)
- [Alten et al. 2021, aberrant spontaneous neurotransmission in SNAP25 encephalopathies](https://pmc.ncbi.nlm.nih.gov/articles/PMC7790958)
- [Klöckner et al. 2021, de novo SNAP25 variants (preprint full text)](https://medrxiv.org/content/10.1101/2020.05.11.20095141v1.full)
- [Brinkmalm et al. 2014, CSF SNAP-25 in Alzheimer's disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4253625/)
- [Nilsson et al. 2024, CSF synaptic biomarker panel (PMID:38325331)](https://pubmed.ncbi.nlm.nih.gov/38325331/)
- [CSF SNAP-25 Simoa study, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11800177/)
- [SNAP25 in human neurological syndromes, 2023 review](https://www.eurekaselect.com/article/141444)

## Citations

1. https://www.rcsb.org/structure/1SFC
2. https://pubmed.ncbi.nlm.nih.gov/9861047/
3. https://www.nature.com/articles/nn783
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC2739239
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6325239/
6. https://discovery.ucl.ac.uk/10126208/1/Kalyanasundaram%20et%20al_Manuscript_Accepted.pdf
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC9623538
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3102109/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3432151
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3065388
11. https://pureportal.coventry.ac.uk/en/publications/differential-palmitoylation-regulates-intracellular-patterning-of/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC7247313
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4805587/
14. https://www.frontiersin.org/journals/synaptic-neuroscience/articles/10.3389/fnsyn.2023.1148957/full
15. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2023.1096365/full
16. https://elifesciences.org/articles/88619.pdf
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7790958
18. https://medrxiv.org/content/10.1101/2020.05.11.20095141v1.full
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4253625/
20. https://pubmed.ncbi.nlm.nih.gov/38325331/
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11800177/
22. https://www.eurekaselect.com/article/141444