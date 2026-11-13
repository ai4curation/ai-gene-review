---
provider: claude_code
cached: false
start_time: '2026-11-13T15:51:35.910993'
end_time: '2026-11-13T15:53:26.049022'
duration_seconds: 110.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TSPOAP1
  gene_symbol: TSPOAP1
  uniprot_accession: O95153
  protein_description: 'RecName: Full=Peripheral-type benzodiazepine receptor-associated
    protein 1; Short=PRAX-1; AltName: Full=Peripheral benzodiazepine receptor-interacting
    protein; Short=PBR-IP; AltName: Full=RIMS-binding protein 1; Short=RIM-BP1; AltName:
    Full=TSPO-associated protein 1 {ECO:0000312|HGNC:HGNC:16831};'
  gene_info: Name=TSPOAP1 {ECO:0000312|HGNC:HGNC:16831}; Synonyms=BZRAP1, KIAA0612,
    RBP1, RIMBP1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the RIMBP family. .
  protein_domains: FN3_dom. (IPR003961); FN3_RIM-BP1/2/3. (IPR057884); FN3_sf. (IPR036116);
    Ig-like_fold. (IPR013783); RIM-BP_SH3_2. (IPR035753)
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
  web_search_requests: 12
  num_turns: 17
  total_cost_usd: 1.6429609
  session_id: 3330df9a-aa33-44dd-8e86-ca3e78c51c9a
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O95153
- **Protein Description:** RecName: Full=Peripheral-type benzodiazepine receptor-associated protein 1; Short=PRAX-1; AltName: Full=Peripheral benzodiazepine receptor-interacting protein; Short=PBR-IP; AltName: Full=RIMS-binding protein 1; Short=RIM-BP1; AltName: Full=TSPO-associated protein 1 {ECO:0000312|HGNC:HGNC:16831};
- **Gene Information:** Name=TSPOAP1 {ECO:0000312|HGNC:HGNC:16831}; Synonyms=BZRAP1, KIAA0612, RBP1, RIMBP1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RIMBP family. .
- **Key Domains:** FN3_dom. (IPR003961); FN3_RIM-BP1/2/3. (IPR057884); FN3_sf. (IPR036116); Ig-like_fold. (IPR013783); RIM-BP_SH3_2. (IPR035753)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TSPOAP1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TSPOAP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TSPOAP1** (gene ID: TSPOAP1, UniProt: O95153) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TSPOAP1 (RIM-BP1 / PRAX-1; UniProt O95153): Research Report for Functional Annotation

## Identity verification

The target is unambiguous. TSPOAP1 (formerly BZRAP1; synonyms RIMBP1, RBP1, KIAA0612, PRAX-1, PBR-IP) is a 1,857-residue human protein of the RIM-binding protein (RIMBP) family, and the literature retrieved matches the UniProt description, organism and domain architecture. One caution: the synonym "RBP1" is shared with unrelated genes (retinol-binding protein 1; RNA polymerase II subunit RPB1), so searches on that alias return irrelevant papers.

Evidence comes from web searches (abstracts and secondary summaries, not full texts) and the local UniProt record for O95153. Items marked "(from memory)" were not re-verified in this session and should be checked before being cited in a review.

## 1. Summary

TSPOAP1 encodes RIM-BP1, a large multidomain scaffold of the presynaptic active zone. It has no enzymatic or transport activity. Its function is as an adaptor: its SH3 domains bind proline-rich motifs in RIM1/RIM2 and in the cytoplasmic tails of voltage-gated Ca²⁺ channel α1 subunits, physically linking the channels to the vesicle-release machinery. The best-supported biological role is positioning Ca²⁺ channels close to release sites, so that action-potential-evoked Ca²⁺ influx is tightly coupled to synaptic vesicle fusion.

The original description of the protein as a mitochondrial partner of the peripheral benzodiazepine receptor (TSPO) rests on a single 1999 study and is flagged by UniProt as not supported in brain.

## 2. Domain architecture and family

- **Layout:** UniProt places one SH3 domain at residues 653–720, three contiguous fibronectin type III domains at 791–1081, and two C-terminal SH3 domains at 1625–1693 and 1764–1831. Long disordered regions flank these, and there is an N-terminal RIMB1_N region (Pfam PF25566).
- **Family definition:** RIM-BPs were defined as a new class of SH3-domain proteins that bind a proline-rich sequence between the two C2 domains of α-RIMs ([Wang, Sugita & Südhof 2000, J Biol Chem 275:20033, PMID 10748113](https://scilit.com/publications/1978462e95b87456392d4208fdf28b34)).
- **Evolution:** Invertebrates have one RIM-BP gene and vertebrates at least two; RIM-BP3 is mammal-specific. All members keep three SH3 domains and two to three FN3 repeats, which the authors read as evidence of a conserved adaptor role ([Mittelstaedt & Schoch 2007, Gene](https://sigmaaldrich.com/AU/en/tech-docs/paper/477034)).
- **Isoforms:** UniProt lists three splice isoforms (O95153-1, -2, -3).

## 3. Molecular function: SH3-mediated scaffold between RIMs and Ca²⁺ channels

- **Channel and RIM binding:** RIM-BPs bind the α1D (L-type, CaV1.3) and α1B (N-type, CaV2.2) subunits. Their SH3 domains recognise proline-rich motifs in both the α1 subunits and RIMs. In PC12 cells, fusion proteins that disrupt these interactions altered depolarisation-evoked exocytosis ([Hibino et al. 2002, Neuron 34:411, PMID 11988172](https://pubmed.ncbi.nlm.nih.gov/11988172/); [PMC2151925](https://pmc.ncbi.nlm.nih.gov/articles/PMC2151925)).
- **Human protein:** UniProt records a direct interaction of human TSPOAP1 with CACNA1A (CaV2.1, P/Q-type) from the 2021 dystonia study, and with RIMS1/RIMS2 by similarity. It assigns RIM binding to the second SH3 domain.
- **BK channels:** RIM-BPs bind BK channels through their FN3 domains. Deleting RIM-BPs at the calyx of Held reduced presynaptic BK currents and depleted BK channels from active zones ([Sclip et al. 2018](https://bohrium.dp.tech/paper/arxiv/29967030)).
- **Phase separation:** RIM and RIM-BP form condensates in vitro through multivalent binding, and Ca²⁺ channel C-terminal tails are enriched in them and cluster on supported lipid bilayers ([Wu et al. 2019, Mol Cell 73:971, PMID 30661983](https://www.pubmed.gov/30661983/)). This work used RIM1 and RIM-BP2 ([PhaSepro entry](https://phasepro.elte.hu/entry/Q9JIR1)), so its application to RIM-BP1 is by homology.

The most accurate molecular-function description is a protein–protein adaptor or scaffold (SH3-domain binding to RIMs and to Ca²⁺ channel tails). The GOA row for "voltage-gated calcium channel activity involved in regulation of presynaptic cytosolic calcium levels" (IEA) is not supported: RIM-BP1 positions channels and is not itself a channel.

## 4. Biological process: coupling Ca²⁺ influx to vesicle release

- **Double knockout:** In RIM-BP1/RIM-BP2 conditional double-knockout mice, release itself persists in cultured hippocampal neurons and at the calyx of Held. What is lost is high-fidelity coupling of action-potential-evoked Ca²⁺ influx to vesicle fusion ([Acuna et al. 2015, Neuron 87:1234](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_1727674289)).
- **Paralog dominance:** At hippocampal synapses, adding RIM-BP1 loss to RIM-BP2 loss had no further effect, indicating RIM-BP2 is the dominant paralog there ([Grauel et al. 2016, PNAS; PMC5068320](https://pmc.ncbi.nlm.nih.gov/articles/PMC5068320)).
- **Priming role (RIM-BP2):** At mossy fibre synapses RIM-BP2 promotes vesicle docking and priming by stabilising Munc13-1, while at CA3–CA1 synapses it only tunes Ca²⁺–secretion coupling ([Brockmann et al. 2019, eLife](https://elifesciences.org/articles/43243)). RIM-BPs, RIMs and Munc13s act as a functional trio ([Brockmann et al. 2020, Cell Rep 32:107960](https://doaj.org/article/7763280415ec449685a6a81ebc00a72b)).
- **Other synapses (RIM-BP2):** RIM-BP2 loss reduced Ca²⁺ currents and release probability at mossy fibre terminals ([Miyano et al. 2024, eLife](https://elifesciences.org/reviewed-preprints/90799)).
- **Invertebrate ortholog:** The single Drosophila RIM-BP is essential for Ca²⁺ channel clustering and release at the neuromuscular junction (Liu et al. 2011, Science; from memory).

Most mechanistic detail therefore comes from RIM-BP2 or from combined RIM-BP1/2 deletions. RIM-BP1-specific evidence is mainly the mouse knockout and human genetics below.

## 5. RIM-BP1-specific evidence: human disease and mouse knockout

[Mencacci et al. 2021, J Clin Invest 131:e140625 (PMID 33539324)](https://pubmed.ncbi.nlm.nih.gov/33539324/) is the key paper on the human gene:

- **Patients:** Homozygous frameshift, nonsense and missense variants were found in 7 people from 3 unrelated families.
- **Loss-of-function phenotype:** Juvenile-onset progressive generalised dystonia with intellectual disability and cerebellar atrophy (DYT22JO, MIM 620453).
- **Missense phenotype:** p.Gly1808Ser gave isolated adult-onset focal dystonia (DYT22AO, MIM 620456). By the UniProt coordinates this residue lies in the third SH3 domain.
- **Mouse knockout:** Complete loss of RIMBP1 caused dystonia-like motor abnormalities, reduced Purkinje cell dendritic arborisation and fewer cerebellar synapses.
- **Variant function:** p.Gly1808Ser produced larger spike-evoked Ca²⁺ transients and enhanced neurotransmission in vitro.

This is the source of the UniProt function statement and of the GOA IMP annotation to regulation of neurotransmitter secretion. UniProt words the disease link cautiously ("may be caused by").

## 6. Localization

- **Presynaptic active zone:** This is the site of function supported by the RIM/Ca²⁺ channel interactions, the knockout physiology and the disease study. Direct imaging evidence is stronger for RIM-BP2 than for RIM-BP1.
- **Cytoplasm and mitochondrion:** These come from the 1999 PRAX-1 study, which found the overexpressed protein cytoplasmic and partially co-localised with TSPO at mitochondria ([Galiègue et al. 1999, J Biol Chem 274:2938, PMID 9915832](https://thebiogrid.org/12826/publication/cloning-and-characterization-of-prax-1-a-new-protein-that-specifically-interacts-with-the-peripheral-benzodiazepine-receptor.html)). UniProt notes the mitochondrial pattern was seen preferentially in the presence of TSPO.
- **Expression:** Predominantly brain, pituitary and thymus in adults, with highest brain levels in temporal lobe and putamen (same study, via UniProt).

## 7. The TSPO (peripheral benzodiazepine receptor) question

PRAX-1 was isolated in a yeast two-hybrid screen using the cytoplasmic domain of TSPO as bait, and both the SH3-like domain and a proline-rich region were needed for binding (Galiègue et al. 1999). UniProt carries an explicit caution that later work on the rat ortholog (PMID 12435798) found it is not associated with TSPO in brain. I could not retrieve that paper in this session, so the caution is reported from the UniProt record only.

The GOA rows for benzodiazepine receptor binding and mitochondrion (IPI/IDA plus IBA and IEA) all trace back to this one study. The gene name itself reflects that history, not the current understanding of function.

## 8. Other associations

- **Alzheimer's disease GWAS:** The 17q22 locus has been reported at the antisense transcript BZRAP1-AS1/TSPOAP1-AS1 ([Jun et al. 2017](https://ncradbio.sitehost.iu.edu/docs/Publications/457_Jun.pdf)), with a candidate functional variant annotated to MIR142 ([Ghanbari et al. 2019](https://repub.eur.nl/pub/109094/109094_Chapter_6-A_functional_variant_in_the_miR-142_prom.pdf)). TSPOAP1 reached only suggestive significance in a later meta-analysis ([Schwartzentruber et al. 2021; PMC7610386](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610386)). The causal gene is unresolved, and this does not inform protein function.
- **IntAct:** An interaction with ADAM19 is listed in UniProt; its functional meaning is unknown.

## 9. Implications for annotation

| Aspect | Best-supported statement | Strength |
|---|---|---|
| Molecular function | SH3-mediated adaptor linking RIM1/2 to CaV channel α1 subunits | Strong for the family; CACNA1A binding shown for the human protein |
| Biological process | Regulation of neurotransmitter release through Ca²⁺ channel positioning at release sites | Human variant and mouse knockout data, plus RIM-BP1/2 double knockout |
| Cellular component | Presynaptic active zone | Strong by family and function; limited direct imaging of RIM-BP1 |
| TSPO binding, mitochondrion | Single 1999 overexpression/two-hybrid study | Weak; disputed by UniProt caution |
| Ca²⁺ channel activity | None | Electronic annotation that is not supported |

## 10. Open questions

- What RIM-BP1 contributes that RIM-BP2 does not, given RIM-BP2 dominance in hippocampus but a clear cerebellar and motor phenotype for RIM-BP1 loss.
- Whether the TSPO interaction occurs in any native tissue (for example thymus or pituitary, where the gene is also expressed).
- How p.Gly1808Ser increases Ca²⁺ transients: altered channel or RIM binding by the third SH3 domain is the obvious hypothesis, but the abstract does not establish the mechanism.

## Sources

- [Mencacci et al. 2021, J Clin Invest — PubMed 33539324](https://pubmed.ncbi.nlm.nih.gov/33539324/)
- [Mencacci et al., bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2020.05.24.086215.full.pdf)
- [Hibino et al. 2002, Neuron — PubMed 11988172](https://pubmed.ncbi.nlm.nih.gov/11988172/) and [PMC2151925](https://pmc.ncbi.nlm.nih.gov/articles/PMC2151925)
- [Galiègue et al. 1999, J Biol Chem — BioGRID record](https://thebiogrid.org/12826/publication/cloning-and-characterization-of-prax-1-a-new-protein-that-specifically-interacts-with-the-peripheral-benzodiazepine-receptor.html)
- [Wang, Sugita & Südhof 2000, J Biol Chem](https://scilit.com/publications/1978462e95b87456392d4208fdf28b34)
- [Mittelstaedt & Schoch 2007, Gene](https://sigmaaldrich.com/AU/en/tech-docs/paper/477034)
- [Acuna et al. 2015, Neuron](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_1727674289)
- [Grauel et al. 2016, PNAS — PMC5068320](https://pmc.ncbi.nlm.nih.gov/articles/PMC5068320)
- [Brockmann et al. 2019, eLife](https://elifesciences.org/articles/43243)
- [Brockmann et al. 2020, Cell Reports](https://doaj.org/article/7763280415ec449685a6a81ebc00a72b)
- [Miyano et al. 2024, eLife](https://elifesciences.org/reviewed-preprints/90799)
- [Sclip et al. 2018, RIM-BPs recruit BK channels](https://bohrium.dp.tech/paper/arxiv/29967030)
- [Wu et al. 2019, Mol Cell — PubMed 30661983](https://www.pubmed.gov/30661983/) and [PhaSepro entry](https://phasepro.elte.hu/entry/Q9JIR1)
- [Jun et al. 2017, transethnic AD GWAS](https://ncradbio.sitehost.iu.edu/docs/Publications/457_Jun.pdf)
- [Ghanbari et al. 2019, MIR142 variant](https://repub.eur.nl/pub/109094/109094_Chapter_6-A_functional_variant_in_the_miR-142_prom.pdf)
- [Schwartzentruber et al. 2021 — PMC7610386](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610386)
- [NCBI Gene: TSPOAP1-AS1](https://www.ncbi.nlm.nih.gov/gene/100506779)
- UniProtKB O95153 (local copy: `genes/human/TSPOAP1/TSPOAP1-uniprot.txt`)

## Citations

1. https://scilit.com/publications/1978462e95b87456392d4208fdf28b34
2. https://sigmaaldrich.com/AU/en/tech-docs/paper/477034
3. https://pubmed.ncbi.nlm.nih.gov/11988172/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC2151925
5. https://bohrium.dp.tech/paper/arxiv/29967030
6. https://www.pubmed.gov/30661983/
7. https://phasepro.elte.hu/entry/Q9JIR1
8. https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_1727674289
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC5068320
10. https://elifesciences.org/articles/43243
11. https://doaj.org/article/7763280415ec449685a6a81ebc00a72b
12. https://elifesciences.org/reviewed-preprints/90799
13. https://pubmed.ncbi.nlm.nih.gov/33539324/
14. https://thebiogrid.org/12826/publication/cloning-and-characterization-of-prax-1-a-new-protein-that-specifically-interacts-with-the-peripheral-benzodiazepine-receptor.html
15. https://ncradbio.sitehost.iu.edu/docs/Publications/457_Jun.pdf
16. https://repub.eur.nl/pub/109094/109094_Chapter_6-A_functional_variant_in_the_miR-142_prom.pdf
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7610386
18. https://www.biorxiv.org/content/10.1101/2020.05.24.086215.full.pdf
19. https://www.ncbi.nlm.nih.gov/gene/100506779