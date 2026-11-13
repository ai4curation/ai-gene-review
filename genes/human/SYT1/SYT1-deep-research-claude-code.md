---
provider: claude_code
cached: false
start_time: '2026-11-13T00:08:54.997435'
end_time: '2026-11-13T00:10:51.616910'
duration_seconds: 116.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SYT1
  gene_symbol: SYT1
  uniprot_accession: P21579
  protein_description: 'RecName: Full=Synaptotagmin-1 {ECO:0000303|PubMed:25705886};
    AltName: Full=Synaptotagmin I {ECO:0000250|UniProtKB:P21707}; Short=SytI; AltName:
    Full=p65 {ECO:0000250|UniProtKB:P21707};'
  gene_info: Name=SYT1 {ECO:0000312|HGNC:HGNC:11509}; Synonyms=SVP65, SYT;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the synaptotagmin family. .
  protein_domains: C2_dom. (IPR000008); C2_domain_sf. (IPR035892); Synaptotagmin.
    (IPR001565); Syt1_N. (IPR064679); C2 (PF00168)
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
  web_search_requests: 7
  num_turns: 10
  total_cost_usd: 1.3756562999999997
  session_id: 11bb7211-d7de-4d9e-a002-49b3a13d9069
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P21579
- **Protein Description:** RecName: Full=Synaptotagmin-1 {ECO:0000303|PubMed:25705886}; AltName: Full=Synaptotagmin I {ECO:0000250|UniProtKB:P21707}; Short=SytI; AltName: Full=p65 {ECO:0000250|UniProtKB:P21707};
- **Gene Information:** Name=SYT1 {ECO:0000312|HGNC:HGNC:11509}; Synonyms=SVP65, SYT;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the synaptotagmin family. .
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); Synaptotagmin. (IPR001565); Syt1_N. (IPR064679); C2 (PF00168)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SYT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SYT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SYT1** (gene ID: SYT1, UniProt: P21579) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Synaptotagmin-1 (SYT1, UniProt P21579, *Homo sapiens*): Research Report for Functional Annotation

## Identity check and scope of evidence

The symbol, organism, family and domains all match the target: the literature found is on synaptotagmin-1 (Syt1, p65), the synaptic-vesicle C2-domain protein of the synaptotagmin family. No conflicting gene with the same symbol was mixed in.

Two caveats on the evidence base:

- **Most mechanistic evidence is from orthologs.** Rat (P21707), mouse (P46096) and *Drosophila* Syt1 carry nearly all the biochemistry, structure and physiology. Direct human-protein evidence is mainly the original cloning, a few interaction studies and the disease genetics.
- **Rat and human residue numbers differ by one in the C2 domains.** Rat Syt1 has 421 residues and human 422, so rat I367 is human I368. Residue numbers below are rat unless marked human.

Citations with a PMID and no link are from my recall of the literature and were not re-fetched in this session; verify them against PubMed before reuse. Linked sources were retrieved in this session, mostly as abstracts or summaries, not full text.

## 1. Key concepts: what the protein is

**Architecture.** SYT1 is a 422-residue single-pass membrane protein. It has a short N-terminal intravesicular (lumenal) segment that is glycosylated, one transmembrane helix, a charged juxtamembrane linker, and two cytoplasmic C2 domains in tandem (C2A and C2B). The cloning papers established this architecture and its conservation from *Drosophila* to human (Perin et al. 1990, PMID:2333096; Perin et al. 1991, PMID:1840599). UniProt records the same topology and notes palmitoylation near the membrane-proximal cysteines by similarity.

**Not an enzyme or transporter.** SYT1 has no catalytic activity. Its molecular function is as a Ca²⁺ sensor: Ca²⁺-dependent binding to anionic phospholipids, coupled to binding of the SNARE fusion machinery.

**Ca²⁺ binding.** Each C2 domain is a β-sandwich with Ca²⁺-binding loops at one tip.
- C2A binds three Ca²⁺ ions and C2B binds two, through conserved aspartates (C2A: D172, D178, D230, D232, D238; C2B: D303, D309, D363, D365, D371) (Sutton et al. 1995, PMID:7697723; Fernandez et al. 2001, PMID:11754837).
- UniProt's "3 Ca²⁺ per subunit" is a by-similarity simplification; the structural literature supports five in total.
- Intrinsic Ca²⁺ affinity is low (high micromolar to millimolar) because the coordination spheres are incomplete. Anionic lipid headgroups complete them, raising apparent affinity into the low-micromolar range seen at release sites.

**Lipid binding.** With Ca²⁺ bound, the loops insert into membranes containing phosphatidylserine (Brose et al. 1992, PMID:1589771). Independently of Ca²⁺, a polybasic strand on the side of C2B (K326, K327 and neighbours) binds PI(4,5)P₂, pre-positioning the protein at the plasma membrane and increasing its Ca²⁺ sensitivity.

**SNARE binding.** Three contact modes with the neuronal SNARE complex (syntaxin-1, SNAP-25, synaptobrevin-2) have been described:
- **Primary interface.** A Ca²⁺-independent contact between C2B and SNAP-25/syntaxin-1, involving region I (E295, Y338) and region II (R398, R399). Mutations here strongly impair evoked release in neurons (Zhou et al. 2015, PMID:26280336; residues as summarised in [Voleti et al. 2020](https://elifesciences.org/articles/57154)).
- **Tripartite interface.** A second C2B molecule contacts both the SNARE complex and complexin in crystal structures of the primed complex ([Zhou et al. 2017](https://zendy.io/pdf-viewer/10.1038/nature23484)).
- **Polybasic interface.** A dynamic contact through the C2B polybasic region (Brewer et al. 2015, PMID:26030874).

Solution NMR and fluorescence work detected the polybasic and primary modes but not the tripartite mode. It also found that Ca²⁺ drives tight binding to PIP₂ membranes at the expense of SNARE contacts ([Voleti et al. 2020](https://elifesciences.org/articles/57154)). Other work reports that C2B can engage acidic membranes and SNAREs at the same time, including during loop insertion ([Wang et al. 2016](https://elifesciences.org/articles/14211)).

## 2. Primary function: Ca²⁺ sensor for fast synchronous exocytosis

**Genetic evidence.**
- Mouse knockout abolishes the fast, synchronous component of evoked release in hippocampal neurons, while slower asynchronous release persists and may increase (Geppert et al. 1994, PMID:7954835; summarised in [this review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6729667)).
- The R233Q knock-in, a C2A mutation, roughly halves the apparent Ca²⁺ affinity of lipid binding and produces a matching drop in release probability. This is the strongest single piece of evidence that Syt1 is the sensor itself, not just a required cofactor (Fernández-Chacón et al. 2001, PMID:11242035).
- Ca²⁺ binding to C2B is essential for synchronous release, while C2A Ca²⁺ binding is partly dispensable and modulatory (Mackler et al. 2002, PMID:12110842).

**Division of labour with paralogs.** Syt1, Syt2 and Syt9 are the fast sensors, with different kinetics and regional expression; Syt1 dominates in forebrain (Xu et al. 2007, PMID:17521570). Syt7 mediates the slower asynchronous phase ([Bacaj et al. 2013](https://pubmed.ncbi.nlm.nih.gov/24267651/)). Syt1 is also the sensor for fast striatal dopamine release ([Banerjee et al. 2020](https://elifesciences.org/articles/58359)).

**Second role: clamping.** Loss of Syt1 increases spontaneous (miniature) release in many preparations and unmasks asynchronous release. Syt1 therefore also restrains fusion before Ca²⁺ arrives. Two lines of work address how:
- Syt1 clamps fusion in mammalian neurons independently of complexin (Courtney et al. 2019, PMID:31501440).
- In reconstitution, Syt1 oligomers hold a limited number of "central" SNARE complexes through the primary interface, and Ca²⁺ releases them to drive synchronised fusion; complexin acts synergistically ([Ramakrishnan et al. 2020](https://elifesciences.org/articles/54506)).

**How Ca²⁺ binding triggers fusion is unresolved.** Proposed models include:
- loop insertion that bends or perturbs the plasma membrane (Martens et al. 2007, PMID:17478680; Hui et al. 2009, PMID:19703397);
- bridging of vesicle and plasma membranes by C2B;
- displacement of complexin, or release of a clamp on SNARE zippering;
- cooperative action with SNAREs on PIP₂ membranes.

A review lays out six competing models and concludes the question is open ([Park and Ryu](https://pmc.ncbi.nlm.nih.gov/articles/PMC6056330)).

## 3. Recent developments (2020–2025)

- **Lever hypothesis (2024 preprints).** Ca²⁺ does not dissociate Syt1 from membrane-anchored SNARE complexes but reorients C2B. The proposal is that C2B acts as a lever pulling on the SNARE complex to complete zippering ([lever hypothesis preprint](https://bohrium.dp.tech/paper/arxiv/2024.06.17.599417); [companion experimental preprint](https://bohrium.dp.tech/paper/arxiv/2024.06.17.599435)).
- **Domain orientation on membranes (Structure, 2024).** Both C2 domains insert on Ca²⁺ binding, with C2A more perpendicular and C2B staying parallel to the bilayer ([Bender et al. 2024](https://durham-repository.worktribe.com/OutputFile/3349630)).
- **All-atom simulations.** Insertion of the Ca²⁺-binding loops did not produce substantial curvature or bilayer disruption. The authors argue against the curvature, perturbation and bridging models ([MD study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12051017/)).
- **Disease mechanism.** Disorder-associated C2B variants reduce Ca²⁺ responsiveness and have graded dominant-negative effects on transmission; the K⁺ channel blocker 4-aminopyridine rescued the heterozygous phenotype in neurons (Bradberry et al. 2020, PMID:32362337; [summary](https://www.sciencedaily.com/releases/2020/05/200501120105.htm)). A structure of the I368T C2B mutant is deposited as [PDB 6U4U](https://www.rcsb.org/structure/6u4u).

## 4. Secondary roles

**Synaptic vesicle endocytosis.** Syt1 promotes the rate of vesicle retrieval after exocytosis. Acute inactivation in *Drosophila* and knockout neurons slow endocytosis (Poskanzer et al. 2003, PMID:14634669). C2B binds the AP-2 adaptor (Zhang et al. 1994, PMID:7918104), and UniProt records a dynamin-1 interaction by similarity.

**Syt1 as endocytic cargo.** Its own sorting back to vesicles uses two overlapping routes:
- Stonin 2, a dedicated adaptor. The human interaction is direct evidence (Walther et al. 2001, PMID:11381094). Loss of stonin 2 missorts Syt1 to the neuronal surface ([Kononenko et al. 2013](https://www.pubmed.gov/23345427/)).
- SV2A/B. Loss of both SV2A/B and stonin 2 greatly worsens Syt1 loss and missorting, and impairs transmission ([Kaempf et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4466747)).
- SGIP1α has also been described as a selective adaptor for Syt1 internalisation ([2019 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6499997)).

For annotation, note the distinction: in the sorting pathway Syt1 is the thing being sorted, whereas its effect on endocytic rate is a separate, active contribution.

**Dense-core vesicle exocytosis.** In adrenal chromaffin cells Syt1 drives the fast burst of catecholamine release, with Syt7 covering the slower component (Voets et al. 2001, PMID:11553786; Schonn et al. 2008, PMID:18308933).

**Other human-specific reports.** These are single studies and peripheral to the core role: an interaction with SCAMP5 in Ca²⁺-triggered cytokine secretion (PMID:19234194) and a role in melanocyte dendrite formation (PMID:23999003), both cited by UniProt.

## 5. Localisation

- **Synaptic vesicle membrane** is the principal site. Syt1 is among the most abundant vesicle proteins, at roughly 15 copies per vesicle (Takamori et al. 2006, PMID:17110340). The C2 domains face the cytoplasm and the N-terminus faces the lumen.
- **Dense-core granule and chromaffin granule membrane** in neuroendocrine cells.
- **Presynaptic plasma membrane, transiently.** After fusion Syt1 is exposed on the surface and retrieved by endocytosis. A stranded surface pool grows when stonin 2 or SV2 is missing.
- **Site of action.** The function is carried out at the presynaptic active zone, in the gap between a docked vesicle and the plasma membrane. The C2 domains act in *trans* on the PI(4,5)P₂- and phosphatidylserine-rich inner leaflet and on assembled SNARE complexes.

UniProt also lists "cytoplasm" by similarity; I found no primary evidence for a functional soluble pool.

## 6. Pathway context

SYT1 acts at the last step of the synaptic vesicle cycle:

1. An action potential opens presynaptic Ca²⁺ channels (Cav2.1/2.2).
2. Ca²⁺ rises in a nanodomain around docked, primed vesicles.
3. Syt1 binds Ca²⁺ and engages membrane and SNAREs.
4. The partly zippered SNARE complex, held with complexin and organised by Munc18-1 and Munc13, completes assembly.
5. The fusion pore opens and transmitter is released in under a millisecond.

Syt1 does not perform fusion; the SNAREs do. It supplies Ca²⁺ dependence, speed and synchrony, and a restraint on Ca²⁺-independent fusion. Standard reviews: Chapman 2008 (Annu Rev Biochem), Südhof 2013 (PMID:24183019), Rizo 2022 (PMID:35167762).

## 7. Human disease

Heterozygous de novo missense variants cause SYT1-associated neurodevelopmental disorder (Baker-Gordon syndrome, MIM 618218).

- **Features.** Infantile hypotonia, ophthalmic abnormalities, hyperkinetic movement disorder, motor stereotypies, developmental delay from moderate to profound, sleep disturbance and EEG abnormalities, typically without frank epilepsy (Baker et al. 2015, PMID:25705886; Baker et al. 2018, PMID:30107533).
- **First variant.** Human I368T in C2B slowed evoked vesicle fusion kinetics and perturbed vesicle cycling when expressed in neurons (Baker et al. 2015).
- **Cohort data.** A 2022 series described 15 de novo variants in 22 individuals: 6 pathogenic, 4 likely pathogenic, 5 of uncertain significance. Four variants were in C2A and the rest in C2B, and the severity range was broader than first reported ([Melland et al. 2022](https://pubmed.ncbi.nlm.nih.gov/35101335/)).
- **Mechanism.** C2B variants act as dominant negatives on evoked release (Bradberry et al. 2020). A later functional study found no simple severity split between C2A and C2B variants and proposed impaired evoked release as the common driver ([PMC11564929](https://pmc.ncbi.nlm.nih.gov/articles/PMC11564929)).

## 8. Summary for annotation

| Aspect | Best-supported statement | Evidence strength |
|---|---|---|
| Molecular function | Ca²⁺ sensor: Ca²⁺-dependent anionic phospholipid binding (phosphatidylserine, PI(4,5)P₂), Ca²⁺ ion binding, SNARE/syntaxin-1/SNAP-25 binding | Strong; mostly rodent protein, structures and knock-ins |
| Core process | Ca²⁺-triggered fast synchronous synaptic vesicle exocytosis; restraint of spontaneous and asynchronous release | Strong (knockout, knock-in, human variants) |
| Secondary processes | Promotes synaptic vesicle endocytosis; Ca²⁺-triggered dense-core vesicle exocytosis | Moderate to strong |
| Location | Synaptic vesicle membrane; dense-core/chromaffin granule membrane; transient presynaptic plasma membrane; acts at the active zone | Strong |
| Peripheral | Cytokine secretion with SCAMP5; melanocyte dendrite formation | Single studies |
| Unresolved | The physical step by which Ca²⁺-bound Syt1 triggers SNARE-mediated fusion | Actively contested, 2024–2025 |

## Sources

- [Models of synaptotagmin-1 to trigger Ca2+-dependent vesicle fusion (Park and Ryu)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6056330)
- [Review citing Geppert 1994 knockout findings](https://pmc.ncbi.nlm.nih.gov/articles/PMC6729667)
- [Zhou et al. 2017, Nature: primed SNARE–complexin–synaptotagmin-1 complex](https://zendy.io/pdf-viewer/10.1038/nature23484)
- [Voleti, Jaczynska and Rizo 2020, eLife 57154](https://elifesciences.org/articles/57154)
- [Ramakrishnan et al. 2020, eLife 54506](https://elifesciences.org/articles/54506)
- [Wang, Li and Ma 2016, eLife 14211](https://elifesciences.org/articles/14211)
- [Bacaj et al. 2013, synaptotagmin-1 and -7 in synchronous and asynchronous release](https://pubmed.ncbi.nlm.nih.gov/24267651/)
- [Banerjee et al. 2020, eLife 58359: Syt1 and striatal dopamine release](https://elifesciences.org/articles/58359)
- [Lever hypothesis preprint, 2024](https://bohrium.dp.tech/paper/arxiv/2024.06.17.599417)
- [Companion preprint on C2B reorientation, 2024](https://bohrium.dp.tech/paper/arxiv/2024.06.17.599435)
- [Bender et al. 2024, Structure (repository copy)](https://durham-repository.worktribe.com/OutputFile/3349630)
- [All-atom MD evaluation of synaptotagmin-1 action models](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12051017/)
- [Kononenko et al. 2013, PNAS: stonin 2 and Syt1 sorting](https://www.pubmed.gov/23345427/)
- [Kaempf et al. 2015, PNAS: SV2A/B and stonin 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC4466747)
- [SGIP1α as an endocytic adaptor for Syt1, 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6499997)
- [Melland et al. 2022, Genetics in Medicine](https://pubmed.ncbi.nlm.nih.gov/35101335/)
- [Functional study of C2A and C2B disorder variants (PMC11564929)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11564929)
- [Bradberry et al. 2020 press summary (ScienceDaily, 1 May 2020)](https://www.sciencedaily.com/releases/2020/05/200501120105.htm)
- [PDB 6U4U: Syt1 C2B I368T](https://www.rcsb.org/structure/6u4u)
- UniProt P21579 flat file, local copy at `genes/human/SYT1/SYT1-uniprot.txt`

## Citations

1. https://elifesciences.org/articles/57154
2. https://zendy.io/pdf-viewer/10.1038/nature23484
3. https://elifesciences.org/articles/14211
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC6729667
5. https://pubmed.ncbi.nlm.nih.gov/24267651/
6. https://elifesciences.org/articles/58359
7. https://elifesciences.org/articles/54506
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC6056330
9. https://bohrium.dp.tech/paper/arxiv/2024.06.17.599417
10. https://bohrium.dp.tech/paper/arxiv/2024.06.17.599435
11. https://durham-repository.worktribe.com/OutputFile/3349630
12. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12051017/
13. https://www.sciencedaily.com/releases/2020/05/200501120105.htm
14. https://www.rcsb.org/structure/6u4u
15. https://www.pubmed.gov/23345427/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC4466747
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC6499997
18. https://pubmed.ncbi.nlm.nih.gov/35101335/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC11564929