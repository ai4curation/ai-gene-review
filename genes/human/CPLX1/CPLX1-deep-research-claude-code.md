---
provider: claude_code
cached: false
start_time: '2026-11-12T23:59:32.802269'
end_time: '2026-11-13T00:00:58.382693'
duration_seconds: 85.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CPLX1
  gene_symbol: CPLX1
  uniprot_accession: O14810
  protein_description: 'RecName: Full=Complexin-1; AltName: Full=Complexin I; Short=CPX
    I; AltName: Full=Synaphin-2;'
  gene_info: Name=CPLX1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the complexin/synaphin family. .
  protein_domains: Synaphin. (IPR008849); Synaphin (PF05835)
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
  web_search_requests: 4
  num_turns: 7
  total_cost_usd: 1.6098432
  session_id: d5d4a6fe-c108-48ee-8397-f17dde03325b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O14810
- **Protein Description:** RecName: Full=Complexin-1; AltName: Full=Complexin I; Short=CPX I; AltName: Full=Synaphin-2;
- **Gene Information:** Name=CPLX1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the complexin/synaphin family. .
- **Key Domains:** Synaphin. (IPR008849); Synaphin (PF05835)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CPLX1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CPLX1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CPLX1** (gene ID: CPLX1, UniProt: O14810) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CPLX1 (Complexin-1, human, UniProt O14810): Functional Research Report

## Identity check and provenance

The symbol, organism and family all match the target. CPLX1 encodes complexin-1 (complexin I, synaphin-2), a 134-residue cytosolic protein of the complexin/synaphin family (Pfam PF05835, InterPro IPR008849). No conflicting gene with this symbol was found.

- **Verified this session:** the local UniProt record (`genes/human/CPLX1/CPLX1-uniprot.txt`) and the web sources linked below.
- **Cited from memory:** primary papers without a link or PMID were not re-fetched; confirm their identifiers before using them in the review YAML.
- **Species caveat:** most mechanistic evidence comes from rat and mouse complexin-1 and from Drosophila and C. elegans complexin. Direct human evidence is limited to the structural work, expression studies and disease genetics.
- **Recency:** the searches surfaced no 2023–2024 papers specific to human CPLX1; the most recent sources found are a 2023–2024 eLife study and a 2025 review.

## 1. Key concepts

**Primary function.** Complexin-1 is not an enzyme or transporter. It is a small soluble SNARE-binding regulator of Ca²⁺-triggered exocytosis. It binds the assembled neuronal SNARE complex (syntaxin-1, SNAP-25, VAMP2/synaptobrevin-2) and acts at the last step before membrane fusion. UniProt describes it as positively regulating "a late step in exocytosis of various cytoplasmic vesicles, such as synaptic vesicles and other secretory vesicles."

**Discovery.** Complexins were identified as cytosolic proteins that bind the SNARE complex and compete with α-SNAP (McMahon et al., 1995, Cell 83:111; PMID:7553862). They were independently described as "synaphins" by Ishizuka et al. (1995).

**Domain architecture.** The protein is largely disordered in solution (UniProt predicts disorder for residues 1–60 and 74–113). Four functional regions are usually distinguished:

| Region (approx. residues) | Role |
|---|---|
| N-terminal domain (1–26) | Activating; needed for fast synchronous release (Xue et al., 2007; Maximov et al., 2009) |
| Accessory helix (about 27–47) | Inhibitory; its mechanism is debated |
| Central helix (48–70) | SNARE binding; essential for all complexin functions |
| C-terminal domain (71–134) | Binds membranes and senses curvature; targets complexin to synaptic vesicles and supports clamping (Snead et al., 2014) |

**SNARE binding.** The central helix binds antiparallel in the groove between the VAMP2 and syntaxin-1 helices of the four-helix bundle (Chen et al., 2002, Neuron). Binding is fast, high affinity (roughly 10 nM range) and selective for the assembled complex over individual SNAREs (Pabst et al., 2000 and 2002, J Biol Chem).

## 2. Mechanism: facilitator and clamp

**Facilitation is the best-supported role in mammals.** Neurons from complexin-1/2 double-knockout mice show "a dramatically reduced transmitter release efficiency due to decreased Ca2+ sensitivity of the synaptic secretion process" ([Reim et al., 2001, Cell; PMID:11163241](https://pubmed.ncbi.nlm.nih.gov/11163241/)). The step affected immediately precedes fusion. Double knockouts die at birth, while single Cplx1 knockouts survive. Facilitation holds at both excitatory and inhibitory synapses (Xue et al., 2008, PNAS).

**The clamp model.** In reconstituted and cell-fusion assays, complexin arrests SNARE-driven fusion until Ca²⁺ and synaptotagmin release it (Giraudo et al., 2006, Science; Tang et al., 2006, Cell). Drosophila and C. elegans complexin nulls show greatly increased spontaneous release (Huntwork & Littleton, 2007, Nat Neurosci).

**Human structural evidence.** Kümmel et al. (2011, Nat Struct Mol Biol; PMID:21785414; PDB 3RK3) crystallised human complexin-1 with a truncated prefusion SNARE complex. The central helix sits on one SNARE complex while the accessory helix bridges to a second. This gives a cross-linked "zigzag" array that would be incompatible with fusion. It is the basis of UniProt's functional statement and the only direct experimental citation on the human protein's mechanism.

**The primed tripartite complex.** Crystal structures of the SNARE–complexin–synaptotagmin-1 complex showed "an unexpected tripartite interface between synaptotagmin-1 and both the SNARE complex and complexin" ([Zhou et al., 2017, Nature 548:420](https://www.osti.gov/pages/biblio/1394066-primed-snarecomplexinsynaptotagmin-complex-neuronal-exocytosis); [PDB 5W5C](https://rcsb.org/structure/5w5c), [5W5D](https://rcsb.org/structure/5W5D)). Mutations disrupting the interface severely impaired evoked synchronous release in neurons. The model is that Ca²⁺ binding to synaptotagmin-1 unlocks the complex and allows full SNARE zippering.

**Ongoing debate.** Whether complexin is a true fusion clamp at mammalian synapses remains contested.

- Knockdown studies reported increased spontaneous release (Maximov et al., 2009; Yang et al., 2013, Neuron).
- Constitutive and acute knockouts reduced both spontaneous and evoked release, arguing against a clamp (López-Murcia et al., 2019, Cell Rep).
- Alternative accessory-helix mechanisms include stabilising the central helix (Radoff et al., 2014, eLife) and electrostatic or steric hindrance (Trimbuch et al., 2014, eLife).
- Malsam et al. (2020, Cell Rep) proposed that it captures the membrane-proximal regions of VAMP2 and SNAP25.
- A recent chromaffin-cell study describes the dual clamp/activator function; its reviewers note there is little evidence for a clamp at mammalian synapses ([Makke et al., eLife reviewed preprint 92438](https://elifesciences.org/reviewed-preprints/92438v3/reviews)).
- A 2025 simulation review frames complexin as clamping spontaneous fusion while facilitating evoked release through its central and accessory helices ([Quarterly Reviews of Biophysics](https://www.cambridge.org/core/product/D638EB410F562E86535798DF96106B26)).

The authoritative synthesis remains Trimbuch & Rosenmund (2016, Nat Rev Neurosci, "Should I stop or should I go?"). The consensus is that complexin stabilises a primed, partially zippered SNARE state, which prevents premature fusion and enables fast synchronous release.

## 3. Localisation

- **Cytosol and presynapse.** Complexin-1 is soluble and enriched at release sites in mature neurons. UniProt lists cytosol, perikaryon and presynapse, all by similarity to rat complexin-1 (P63040).
- **Vesicle association.** The C-terminal amphipathic region binds highly curved membranes, which concentrates complexin on synaptic vesicles (Snead et al., 2014, Nat Struct Mol Biol).
- **Site of action.** The functional location is the interface between a docked, primed vesicle and the presynaptic active-zone membrane, where the trans-SNARE complex forms.
- **Postsynaptic role.** Complexins have been reported to control AMPA-receptor exocytosis during long-term potentiation (Ahmad et al., 2012, Neuron). The existing dendrite annotation is an electronic Ensembl transfer.
- **Tissue distribution.** Expression is restricted to the nervous system. In human hippocampus and cerebellum it is "expressed mainly by inhibitory neurons" (UniProt, citing PMID:9853440 and PMID:11483314), whereas complexin-2 predominates in excitatory neurons. Complexin-1 is not the ribbon-synapse isoform; complexins 3 and 4 fill that role in retina (Reim et al., 2005, J Cell Biol).

## 4. Pathways and physiological roles

- **Synaptic vesicle exocytosis.** Reactome places CPLX1 in the glutamate, GABA, acetylcholine, dopamine, serotonin and norepinephrine release cycles (R-HSA-210500, 888590, 264642, 212676, 181429, 181430).
- **Auditory and brainstem synapses.** Complexin-1 is needed for high-fidelity transmission at the endbulb of Held (Strenzke et al., 2009, J Neurosci). At the calyx of Held it stabilises newly primed vesicles and prevents premature fusion (Chang et al., 2015, J Neurosci).
- **Insulin secretion.** Complexin-1 regulates glucose-induced secretion in pancreatic β-cells (Abderrahmani et al., 2004, J Cell Sci). The human GO annotation is an electronic transfer, and UniProt states it by similarity.
- **Motor behaviour.** Cplx1 knockout mice develop strong ataxia without cerebellar degeneration, with abnormal gait and impaired rotarod performance (Glynn et al., 2005, Hum Mol Genet).

## 5. Human disease

**DEE63.** Biallelic loss-of-function variants cause developmental and epileptic encephalopathy 63 (MIM 617976), an autosomal recessive infantile-onset disorder.

- Karaca et al. (2015, Neuron; PMID:26539891) reported two sisters with a homozygous nonsense variant (Glu108Ter; UniProt VAR_080796).
- [Redler et al. (2017, Eur J Hum Genet; PMID:28422131)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5520065) reported three patients from two families with severe infantile myoclonic epilepsy and intellectual disability. Variants included a truncation removing residues 105–134 and Leu128Met, which is of uncertain significance.
- Both truncations remove the C-terminal region, consistent with loss of function.
- [Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/402/gene/CPLX1/) rates the gene green (diagnostic grade). [ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-gene/CPLX1) lists 8 submissions for DEE63.
- The mouse knockout shows ataxia rather than severe epilepsy; this species mismatch is unexplained ([Monarch dismech entry](https://dismech.monarchinitiative.org/pages/disorders/CPLX1-Related_Developmental_and_Epileptic_Encephalopathy.html)).

**Expression changes.** Altered complexin-1 levels are reported in schizophrenia (PMID:9853440, PMID:11483314) and in Parkinson disease substantia nigra (PMID:15526345). These are correlative and do not establish function.

## 6. Implications for annotation

- **Molecular function.** SNARE binding (GO:0000149) is well supported, more precisely binding to the assembled SNARE complex.
- **Core process.** Regulation of synaptic vesicle fusion with the presynaptic active-zone membrane (GO:0031630) and synaptic vesicle exocytosis (GO:0016079) capture the core role.
- **Location.** Presynapse, terminal bouton and cytosol are supported. Human rows rest on orthologs.
- **Complex membership.** Complexin is a stoichiometric, regulatory binder of the SNARE complex, not a SNARE.
- **Peripheral.** Insulin secretion and dendrite are ortholog-derived or electronic; the generic "exocytosis" and "chemical synaptic transmission" terms are true but broad.
- **Open questions.** These are whether a true clamp operates at mammalian synapses, the accessory-helix mechanism, and why human loss causes epilepsy while mouse loss causes ataxia.

## Sources

- [Reim et al. 2001, Cell (PubMed 11163241)](https://pubmed.ncbi.nlm.nih.gov/11163241/)
- [Zhou et al. 2017, Nature (OSTI record)](https://www.osti.gov/pages/biblio/1394066-primed-snarecomplexinsynaptotagmin-complex-neuronal-exocytosis)
- [PDB 5W5C](https://rcsb.org/structure/5w5c) and [PDB 5W5D](https://rcsb.org/structure/5W5D)
- [Makke et al., eLife reviewed preprint 92438](https://elifesciences.org/reviewed-preprints/92438v3/reviews)
- [Quarterly Reviews of Biophysics 2025 simulation review](https://www.cambridge.org/core/product/D638EB410F562E86535798DF96106B26)
- [Redler et al. 2017 (PMC5520065)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5520065)
- [Genomics England PanelApp: CPLX1](https://panelapp.genomicsengland.co.uk/panels/402/gene/CPLX1/)
- [ClinVar Miner: CPLX1](https://clinvarminer.genetics.utah.edu/variants-by-gene/CPLX1)
- [Monarch dismech: CPLX1-related DEE](https://dismech.monarchinitiative.org/pages/disorders/CPLX1-Related_Developmental_and_Epileptic_Encephalopathy.html)
- [GeneCards: CPLX1](https://www.genecards.org/card/CPLX1)
- UniProt O14810 (local copy: `genes/human/CPLX1/CPLX1-uniprot.txt`), including PMIDs 7553862, 21785414, 26539891, 28422131, 9853440, 11483314 and 15526345

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/11163241/
2. https://www.osti.gov/pages/biblio/1394066-primed-snarecomplexinsynaptotagmin-complex-neuronal-exocytosis
3. https://rcsb.org/structure/5w5c
4. https://rcsb.org/structure/5W5D
5. https://elifesciences.org/reviewed-preprints/92438v3/reviews
6. https://www.cambridge.org/core/product/D638EB410F562E86535798DF96106B26
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC5520065
8. https://panelapp.genomicsengland.co.uk/panels/402/gene/CPLX1/
9. https://clinvarminer.genetics.utah.edu/variants-by-gene/CPLX1
10. https://dismech.monarchinitiative.org/pages/disorders/CPLX1-Related_Developmental_and_Epileptic_Encephalopathy.html
11. https://www.genecards.org/card/CPLX1