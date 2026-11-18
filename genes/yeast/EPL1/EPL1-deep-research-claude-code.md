---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:19:53.945827'
end_time: '2026-11-18T15:21:43.613647'
duration_seconds: 109.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: EPL1
  gene_symbol: EPL1
  uniprot_accession: P43572
  protein_description: 'RecName: Full=Enhancer of polycomb-like protein 1;'
  gene_info: Name=EPL1; OrderedLocusNames=YFL024C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the enhancer of polycomb family. .
  protein_domains: Enhancer_polycomb. (IPR024943); Enhancer_polycomb-like_N. (IPR019542);
    EPL1 (PF10513)
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
  web_search_requests: 9
  num_turns: 15
  total_cost_usd: 1.9200889
  session_id: d1375d7b-4778-415e-a5f5-665536e368a9
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P43572
- **Protein Description:** RecName: Full=Enhancer of polycomb-like protein 1;
- **Gene Information:** Name=EPL1; OrderedLocusNames=YFL024C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the enhancer of polycomb family. .
- **Key Domains:** Enhancer_polycomb. (IPR024943); Enhancer_polycomb-like_N. (IPR019542); EPL1 (PF10513)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EPL1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EPL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EPL1** (gene ID: EPL1, UniProt: P43572) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# EPL1 (YFL024C; UniProt P43572): Enhancer of Polycomb-like Protein 1 of *Saccharomyces cerevisiae*

**Scope and provenance.** This report draws on the UniProt record and SGD description cached in the repository, the GOA annotation list, and web searches run on 2026-11-18. I worked from abstracts, database records and search summaries, not full texts. Statements marked *(from memory)* are my recollection of the literature and were not re-checked in this session; verify them before quoting.

## 1. Identity verification

The target is unambiguous. "EPL1" in *S. cerevisiae* (ORF YFL024C, SGD:S000001870) is the yeast homolog of *Drosophila* Enhancer of Polycomb, E(Pc). This matches the UniProt description, the family ("enhancer of polycomb family") and the domain signatures (IPR024943, IPR019542, PF10513). The yeast gene was recognised as an E(Pc) homolog when the fly gene was cloned ([Stankunas et al. 1998, Development, PMID:9735366](https://doi.org/10.1242/dev.125.20.4055)). All literature used here concerns this protein. The protein is 832 residues long, per the UniProt feature table.

## 2. Summary of primary function

Epl1 is a non-catalytic, essential scaffold and activator subunit of the NuA4 histone acetyltransferase. It has no enzymatic activity of its own. It does three separable things:

1. **Assembles the catalytic module.** Its conserved N-terminal EPcA domain binds the MYST acetyltransferase Esa1, the PHD-finger protein Yng2 and Eaf6, forming the tetrameric HAT module known as Piccolo NuA4 (picNuA4).
2. **Enables nucleosome acetylation.** It activates Esa1 and gives the module the ability to engage and acetylate nucleosomes, which Esa1 alone cannot do.
3. **Tethers the module to holo-NuA4.** Its C-terminal region docks the HAT module onto the 13-subunit complex through the scaffold subunit Eaf1.

The reaction Epl1 contributes to is the Esa1-catalysed transfer of acetyl groups from acetyl-CoA to lysines in the N-terminal tails of nucleosomal H4 and H2A (and the variant H2A.Z/Htz1). It acts in the nucleus, on chromatin.

## 3. Domain architecture and structure

| Region | Role | Key evidence |
|---|---|---|
| N-terminal EPcA domain (roughly the first half) | Binds Esa1, Yng2, Eaf6; necessary and sufficient for picNuA4 assembly; essential for viability | Boudreault 2003; Selleck 2005; Xu 2016 |
| Short basic region at the N-terminal edge of EPcA | Needed for nucleosome acetylation but not for nucleosome binding; lies near the H2A N-tail, the H4 globular domain and DNA | Huang & Tan 2013 |
| C-terminal region | Binds the HSA domain of Eaf1, anchoring picNuA4 to holo-NuA4; dispensable for viability | Boudreault 2003; Lu 2022; Zukin 2022 |
| Residues 1–56, 422–483, 776–832 | Predicted disordered | UniProt feature table |

- **EPcA conservation.** The EPcA domain is shared by yeast, worm and mammalian E(Pc) homologs ([Selleck et al. 2005, Mol Cell Biol, PMC1156996](https://pmc.ncbi.nlm.nih.gov/articles/PMC1156996)).
- **Crystal and cryo-EM structures of the core.** Xu et al. solved crystal structures of the NuA4 core (Esa1–Epl1–Yng2–Eaf6; PDB 5J9Q, 5J9T, 5J9U, 5J9W) and a cryo-EM structure with the nucleosome. They report that Esa1 is activated through its interactions with Epl1, and that the core positions the H4 tail in the active site by a "space-sequence double recognition" mechanism ([Xu et al. 2016, Mol Cell 63:965–975](https://doi.org/10.1016/j.molcel.2016.07.024); [PDB 5J9U](https://www.rcsb.org/structure/5J9U)).
- **Basic-region mechanism.** Because the Epl1 basic region and an Esa1 Tudor/chromo-barrel loop are needed for catalysis but not binding, Huang and Tan propose they act after binding, possibly by pulling histone tails away from DNA ([Huang & Tan 2013, Mol Cell Biol, PMC3536312](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536312)).
- **Nucleosome contact.** SGD summarises the conserved N-terminal region as "essential for interaction with the NPC (nucleosome core particle)" ([SGD EPL1](https://www.yeastgenome.org/locus/EPL1)). The GOA "nucleosome" row cites the EM and crosslinking study of NuA4 and picNuA4 on nucleosomes, Chittuluru et al. 2011, PMID:21984211 *(paper content from memory)*.

## 4. Molecular function within Piccolo NuA4 and NuA4

**Discovery.** Epl1 was identified as a stable NuA4 subunit by Galarneau et al., who linked the complex to epigenetic control of transcription ([Galarneau et al. 2000, Mol Cell, PMID:10911987](https://doi.org/10.1016/s1097-2765(00)80258-0)).

**Piccolo NuA4.** Boudreault et al. defined a smaller Esa1–Epl1–Yng2 complex that strongly prefers chromatin over free histones ([Boudreault et al. 2003, Genes Dev 17:1415–1428, PMC196073](https://pmc.ncbi.nlm.nih.gov/articles/PMC196073)). Their key findings:

- Cells expressing only the N-terminal half of Epl1 lose holo-NuA4 HAT activity but keep the activity responsible for global acetylation.
- Depleting Epl1 causes global loss of H4/H2A acetylation and accumulation of cells in G2/M.
- They propose a division of labour: picNuA4 performs global, untargeted H4/H2A acetylation, while holo-NuA4 is recruited to specific loci.

**Epl1 as an obligate Esa1 cofactor.** Esa1 alone cannot acetylate nucleosomes; Epl1 and Yng2 allow it to bind and act on them ([Huang & Tan 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536312)). Genetic evidence agrees:

- Among the non-catalytic NuA4 subunits, only *epl1Δ*, like *esa1Δ*, can be bypassed by loss of *SDS3*, a core component of the Rpd3L deacetylase.
- *esa1Δ* and *epl1Δ* bypass strains have strikingly similar phenotypes and transcription profiles.
- Mutational analysis ties Epl1's essential function to physical contact with Esa1, without which Esa1 is not fully active ([Searle et al. 2017, Genetics 205:1125–1137, PMC5340328](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328)).

**Anchoring to holo-NuA4.** Lu et al. show that picNuA4 is tethered through the Epl1 C-terminus and the Eaf1 HSA domain. Losing either releases picNuA4, but with opposite effects on its abundance: loss of Eaf1 or its HSA domain lowers picNuA4 levels, while loss of the Epl1 C-terminus raises them ([Lu et al. 2022, Genetics, PMC9630986](https://pmc.ncbi.nlm.nih.gov/articles/PMC9630986)).

**Holo-complex structures (2018–2022).**

- An early architecture placed the piccolo module against the FAT and HEAT repeats of Tra1 ([Wang et al. 2018, Nat Commun](https://www.nature.com/articles/s41467-018-03504-5)). Zukin et al. note this structure conflicted with crosslinking data.
- Zukin et al. resolved the central hub at 3.1 Å. Eaf1 is the main scaffold, contacting Tra1, Swc4 and Epl1, and the flexibly attached HAT module is tethered through Epl1. Their binding assays suggest the HAT module prefers H3K4me3 nucleosomes with hyperacetylated H3 tails ([Zukin et al. 2022, eLife 11:e81400](https://elifesciences.org/articles/81400)).
- Qu et al. solved nucleosome-bound NuA4. The HAT module sits on the nucleosome disc face, contacts the H2A–H2B acidic patch and nucleosomal DNA, and points the Esa1 catalytic pocket at the H4 tail ([Qu et al. 2022, Nature 610:569–574](https://www.nature.com/articles/s41586-022-05303-x)).
- Ji et al. reported a 3.8–4.0 Å structure and found that the isolated Piccolo module binds nucleosomes whereas complete NuA4 did not in their assays ([Ji et al. 2022, PNAS, PMID:36417436](https://pubmed.ncbi.nlm.nih.gov/36417436/)). This conflicts with the Qu et al. binding model and is unresolved.

**Non-histone substrates.** Esa1 also acetylates non-histone proteins, including Epl1 and Yng2 themselves, as summarised in [Searle et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328). The functional consequence of Epl1 acetylation is not established in the sources I saw.

## 5. Biological processes

- **Transcription.** NuA4 acts as a coactivator through H4/H2A acetylation. This is Epl1's best-supported process role, via targeted holo-NuA4 and global picNuA4 activity (Galarneau 2000; Boudreault 2003). GOA also carries a transcription-coupled annotation from PMID:24843044, which I recall as the Eaf5/7/3 submodule study (Rossetto et al. 2014) *(from memory)*.
- **DNA double-strand break repair.** NuA4 is recruited to break sites and spreads with end resection; Nej1 and Yku80 were identified as non-histone NuA4 targets (search summary of the NuA4/NHEJ antagonism study; I did not open the primary paper). GOA's DNA-repair rows for Epl1 cite PMID:15610740 and PMID:16135807. These are complex-level roles; Epl1's contribution is as the HAT-module scaffold.
- **Cell-cycle progression.** Epl1 depletion arrests cells in G2/M, as does loss of Esa1 (Boudreault 2003). This is most simply read as a consequence of losing essential acetylation, not as a dedicated cell-cycle function.
- **Heterochromatin boundaries and silencing.** UniProt cites Oki et al. 2004 (PMID:14966276) for barrier activity restricting the spread of silencing, and telomeric silencing phenotypes are shared with Esa1 (Searle 2017).
- **H2A.Z biology.** Esa1 acetylates Htz1, and NuA4 shares subunits (Act1, Arp4, Swc4, Yaf9) with SWR1, which deposits H2A.Z (UniProt subunit note; PMID:15045029, PMID:15485911).
- **Autophagy.** GOA annotates "positive regulation of macroautophagy" from Yi et al. 2012. That paper shows Esa1 acetylates Atg3 at K19/K48, controlling Atg3–Atg8 interaction and Atg8 lipidation ([Yi et al. 2012, Science 336:474–477, PMID:22539722](https://pubmed.ncbi.nlm.nih.gov/22539722/)). The abstract-level sources I found do not mention Epl1, so the basis of the Epl1 row needs the full text. It is likely a peripheral role mediated through Esa1.

## 6. Localization

Epl1 is nuclear by genome-wide GFP localization ([Huh et al. 2003, Nature, PMID:14562095](https://doi.org/10.1038/nature02026)) and acts on chromatin as part of NuA4 and picNuA4. It is present at about 1,110 molecules per cell in log phase ([Ghaemmaghami et al. 2003, PMID:14562106](https://doi.org/10.1038/nature02046)). The GOA "part_of nucleosome" row is better read as nucleosome binding by the HAT module than as Epl1 being a nucleosome constituent.

## 7. Conservation

Epl1 is the yeast member of the Enhancer of Polycomb family. The human orthologs EPC1 and EPC2 are subunits of the TIP60/NuA4 complex, where they play the equivalent scaffolding role for the Tip60–ING3–MEAF6 module *(from memory; Doyon et al. 2004)*. Lu et al. 2022 report that the picNuA4 balancing interactions are conserved in humans. Despite the name, the yeast protein's established role is in acetylation-dependent chromatin activation, not Polycomb repression; yeast lacks a Polycomb system.

## 8. Notes relevant to annotation

- **Molecular function.** Epl1 *contributes to* histone H4/H2A acetyltransferase activity and does not enable it. The informative function terms are adaptor/scaffold activity (bridging Esa1–Yng2–Eaf6 to Eaf1), nucleosome binding, and arguably activation of the acetyltransferase. The bare protein-binding rows reflect Esa1, Yng2, Eaf6 and Eaf1 contacts.
- **Complex membership.** Both NuA4 and Piccolo NuA4 are strongly supported by biochemistry and structures.
- **Core processes.** Chromatin acetylation in transcription and DNA repair are core. Autophagy and G2/M progression are downstream of Esa1 activity.
- **Open questions.** Whether picNuA4 exists as a free pool in vivo at the levels originally proposed; how the 2022 structures' disagreement over holo-NuA4 nucleosome binding resolves; the role of Epl1's own acetylation; and the function of the disordered central and C-terminal regions beyond Eaf1 binding.

## Sources

- [Stankunas et al. 1998, Development (PMID:9735366)](https://doi.org/10.1242/dev.125.20.4055)
- [Galarneau et al. 2000, Mol Cell (PMID:10911987)](https://doi.org/10.1016/s1097-2765(00)80258-0)
- [Boudreault et al. 2003, Genes Dev (PMID:12782659; PMC196073)](https://pmc.ncbi.nlm.nih.gov/articles/PMC196073)
- [Selleck et al. 2005, Mol Cell Biol (PMID:15964809; PMC1156996)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1156996)
- [Huang & Tan 2013, Mol Cell Biol (PMC3536312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536312)
- [Xu et al. 2016, Mol Cell 63:965–975](https://doi.org/10.1016/j.molcel.2016.07.024) and [PDB 5J9U](https://www.rcsb.org/structure/5J9U)
- [Searle et al. 2017, Genetics (PMID:28108589; PMC5340328)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328)
- [Wang et al. 2018, Nat Commun](https://www.nature.com/articles/s41467-018-03504-5)
- [Lu et al. 2022, Genetics (PMID:36066422; PMC9630986)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9630986)
- [Zukin et al. 2022, eLife 11:e81400](https://elifesciences.org/articles/81400)
- [Qu et al. 2022, Nature 610:569–574](https://www.nature.com/articles/s41586-022-05303-x)
- [Ji et al. 2022, PNAS (PMID:36417436)](https://pubmed.ncbi.nlm.nih.gov/36417436/)
- [Yi et al. 2012, Science (PMID:22539722)](https://pubmed.ncbi.nlm.nih.gov/22539722/)
- [Huh et al. 2003, Nature (PMID:14562095)](https://doi.org/10.1038/nature02026)
- [Ghaemmaghami et al. 2003, Nature (PMID:14562106)](https://doi.org/10.1038/nature02046)
- [SGD locus page for EPL1](https://www.yeastgenome.org/locus/EPL1)
- UniProt P43572 (local copy `genes/yeast/EPL1/EPL1-uniprot.txt`)

## Citations

1. https://doi.org/10.1242/dev.125.20.4055
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC1156996
3. https://doi.org/10.1016/j.molcel.2016.07.024
4. https://www.rcsb.org/structure/5J9U
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3536312
6. https://www.yeastgenome.org/locus/EPL1
7. https://doi.org/10.1016/s1097-2765(00
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC196073
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC9630986
11. https://www.nature.com/articles/s41467-018-03504-5
12. https://elifesciences.org/articles/81400
13. https://www.nature.com/articles/s41586-022-05303-x
14. https://pubmed.ncbi.nlm.nih.gov/36417436/
15. https://pubmed.ncbi.nlm.nih.gov/22539722/
16. https://doi.org/10.1038/nature02026
17. https://doi.org/10.1038/nature02046