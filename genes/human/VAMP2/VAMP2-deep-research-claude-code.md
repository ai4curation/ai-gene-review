---
provider: claude_code
cached: false
start_time: '2026-11-13T00:09:04.280734'
end_time: '2026-11-13T00:10:56.576493'
duration_seconds: 112.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: VAMP2
  gene_symbol: VAMP2
  uniprot_accession: P63027
  protein_description: 'RecName: Full=Vesicle-associated membrane protein 2 {ECO:0000305|PubMed:7803399};
    Short=VAMP-2 {ECO:0000303|PubMed:7803399}; AltName: Full=Synaptobrevin-2 {ECO:0000303|PubMed:1976629};'
  gene_info: Name=VAMP2 {ECO:0000312|HGNC:HGNC:12643}; Synonyms=SYB2 {ECO:0000303|PubMed:1976629};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the synaptobrevin family. .
  protein_domains: Synaptobrevin-like. (IPR001388); Synaptobrevin/VAMP. (IPR016444);
    V_SNARE_CC. (IPR042855); Synaptobrevin (PF00957)
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
  num_turns: 15
  total_cost_usd: 1.5828545
  session_id: b6d4213d-fe07-4ab2-9c2c-494eb6f43111
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P63027
- **Protein Description:** RecName: Full=Vesicle-associated membrane protein 2 {ECO:0000305|PubMed:7803399}; Short=VAMP-2 {ECO:0000303|PubMed:7803399}; AltName: Full=Synaptobrevin-2 {ECO:0000303|PubMed:1976629};
- **Gene Information:** Name=VAMP2 {ECO:0000312|HGNC:HGNC:12643}; Synonyms=SYB2 {ECO:0000303|PubMed:1976629};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the synaptobrevin family. .
- **Key Domains:** Synaptobrevin-like. (IPR001388); Synaptobrevin/VAMP. (IPR016444); V_SNARE_CC. (IPR042855); Synaptobrevin (PF00957)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VAMP2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VAMP2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VAMP2** (gene ID: VAMP2, UniProt: P63027) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# VAMP2 (Synaptobrevin-2; UniProt P63027, *Homo sapiens*): Functional Research Report

## Identity verification

The symbol VAMP2 matches the UniProt description (vesicle-associated membrane protein 2 / synaptobrevin-2, synaptobrevin family, Pfam PF00957). The literature below concerns this protein or its rat and mouse orthologs (P63045, P63044), where much of the mechanistic work was done. No symbol ambiguity was found.

Sourcing note: claims come from the UniProt record, web-search summaries of the cited papers, and textbook knowledge. I did not open full texts. PMIDs given without a link are from memory and should be checked before reuse; I omitted PMIDs where I was unsure.

## 1. Key concepts: what VAMP2 is

- **Class:** VAMP2 is a small (116 aa) tail-anchored (type IV) membrane protein and the principal vesicular R-SNARE of neurons and neuroendocrine cells. It is not an enzyme or transporter; it is a structural component of the membrane fusion machinery.
- **Domain layout:** A short proline-rich N-terminal region is followed by a ~60-residue SNARE motif (roughly residues 31–91) with the conserved "zero-layer" arginine (R56). Then come a juxtamembrane linker (about 86–95, including W89/W90) and a C-terminal transmembrane domain (about 95–114) ([Yan et al. 2022 review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9816800/)).
- **Conformation:** Free VAMP2 is largely unstructured and becomes helical on binding partner SNAREs ([Yan et al. 2022](https://dx.doi.org/10.3389/fnmol.2022.948160)).
- **Abundance:** It is the most abundant synaptic vesicle protein, at about 70 copies per vesicle (Takamori et al. 2006, Cell, PMID:17110340), though only about 2–3 are needed for fusion ([Hu et al. 2021 / PMC10796598 context](https://pmc.ncbi.nlm.nih.gov/articles/PMC10796598)).

## 2. Primary molecular function: v-SNARE driving membrane fusion

**Core complex.** VAMP2 on the vesicle pairs with the plasma-membrane t-SNAREs syntaxin-1 (STX1A/1B) and SNAP-25. The result is a parallel four-helix bundle, with one helix from VAMP2, one from syntaxin and two from SNAP-25.
- The crystal structure was solved at 2.4 Å (Sutton et al. 1998, Nature 395:347, PMID:9759724).
- A later structure shows the helices continuing through the linker into the transmembrane domains ([Stein et al. 2009, PDB 3HD7](https://rcsb.org/structure/3hd7)).
- UniProt states that VAMP2 assembles with SNAP25 and STX1A "to mediate the fusion of synaptic vesicles with the presynaptic plasma membrane in neurotransmitter release" (PubMed:30929742).

**Energy transduction.** N-to-C "zippering" of the trans-SNARE complex releases the energy that pulls the two bilayers together.
- SNAREs alone are a minimal fusion machine in reconstituted liposomes (Weber et al. 1998, Cell, PMID:9529252).
- Optical-tweezers work shows stepwise, reversible zippering through a half-zippered intermediate, which is the main regulatory point for synaptotagmin and complexin ([Frontiers 2022 review, PMC9588726](https://pmc.ncbi.nlm.nih.gov/articles/PMC9588726); [PMC4859083](https://pmc.ncbi.nlm.nih.gov/articles/PMC4859083)).

**Transmembrane and juxtamembrane roles.** The transmembrane domain is more than an anchor.
- Its conformational flexibility (β-branched residues) sets the rate of fusion-pore expansion ([Dhara et al. 2016, eLife](https://elifesciences.org/articles/17571.pdf)).
- It has been proposed to line the nascent fusion pore ([Chang et al. 2015, PMC4103061 context](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103061)).
- Helical extension to W89/W90 is a prerequisite for membrane merger (Hu, Zhu and Ma 2021, per [PMC10796598](https://pmc.ncbi.nlm.nih.gov/articles/PMC10796598)).

**Chaperoned assembly.** VAMP2 does not simply collide with t-SNAREs. Munc18-1 (STXBP1) binds syntaxin-1 and VAMP2 together in a "template complex" that aligns the N-terminal halves of their SNARE motifs for SNAP-25 entry.
- Cryo-EM structures at 3.5–3.7 Å are PDB 7UDB and 7UDC ([Stepien et al. 2022, Sci Adv, PMID:35731863](https://pubmed.ncbi.nlm.nih.gov/35731863/)).
- Single-molecule work shows the template is dynamic and nucleates assembly ([PNAS 2022, PMC9894263](https://pmc.ncbi.nlm.nih.gov/articles/PMC9894263)).
- After fusion, NSF and α-SNAP disassemble cis-SNARE complexes so VAMP2 can be reused (Söllner et al. 1993, Nature, PMID:8455717).

**Genetic evidence.** Synaptobrevin-2 knockout mice die at birth.
- Fast Ca²⁺-triggered release falls more than 100-fold, while spontaneous and sucrose-evoked release fall about 10-fold (Schoch et al. 2001, Science, PMID:11691998; [summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC2739239)).
- Residual release is attributed to synaptobrevin-1 ([Zimmermann et al. 2014](https://pubmed.ncbi.nlm.nih.gov/24944211/)).
- Removing both abolishes evoked transmission at the neuromuscular junction, while spontaneous release persists ([Liu et al. 2019, PMC6668203](https://pmc.ncbi.nlm.nih.gov/articles/PMC6668203)).

**Toxin evidence.** Clostridial neurotoxins are zinc proteases that cleave VAMP2 within the SNARE motif and block release.
- Tetanus toxin and BoNT/B cut Gln76–Phe77 (Schiavo et al. 1992, Nature, PMID:1331807; UniProt PubMed:7803399).
- BoNT/F cuts Gln58–Lys59 and BoNT/D cuts Lys59–Leu60 (UniProt PubMed:19543288, 22289120).
- VAMP2 is the substrate here, not the enzyme.

## 3. Localization

- **Main site:** synaptic vesicle membrane, with the SNARE motif in the cytoplasm (UniProt; Takamori 2006). It is also found on neuroendocrine secretory granules, GLUT4 storage vesicles and, transiently after fusion, the plasma membrane.
- **Biogenesis:** VAMP2 inserts post-translationally into the ER by an SRP/Sec61-independent route (Kutay et al. 1995, PMID:7835332) using the TRC40/GET pathway with SGTA and Bag6 ([PMC5788257](https://pmc.ncbi.nlm.nih.gov/articles/PMC5788257)).
- **Retrieval after exocytosis:** The ANTH domains of AP180 and CALM (PICALM) recognise the free SNARE motif, so only disassembled VAMP2 is sorted ([Koo et al. 2011, PMC3158172](https://pmc.ncbi.nlm.nih.gov/articles/PMC3158172); Miller et al. 2011, Cell, PMID:22118466). Synaptophysin acts as a retrieval chaperone ("iTRAP") ([Gordon & Cousin 2016](https://www.frontiersin.org/articles/10.3389/fnsyn.2016.00001)).
- **Role in endocytosis:** VAMP2 is itself required for fast synaptic vesicle endocytosis (Deák et al. 2004, Nat Cell Biol; not confirmed in this search).
- **Tissue expression:** nervous system and skeletal muscle (UniProt, PubMed:8760387), plus adipocytes and β-cells.

## 4. Pathways and other contexts

| Context | Partners | Evidence and caveats |
|---|---|---|
| Synaptic vesicle exocytosis (core) | STX1A/B, SNAP25, Munc18-1, Munc13, synaptotagmin-1, complexin | Knockout, toxins, structures, reconstitution (above) |
| α-Synuclein | SNCA C-terminus binds VAMP2 N-terminal/juxtamembrane region | Promotes SNARE assembly (Burré et al. 2010, PMID:20798282) and vesicle clustering ([Diao et al. 2013](https://elifesciences.org/articles/592)). VAMP2 co-condensates protect α-synuclein from aggregation ([Wang et al. 2024, Nat Cell Biol](https://x-mol.com/paper/1807852604308910080)) |
| Insulin-stimulated GLUT4 exocytosis | STX4, SNAP23 | VAMP2 is the major v-SNARE in 3T3-L1 adipocytes ([Sadler et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4310743)). VAMP3 and VAMP8 can substitute, and knockout studies report it dispensable ([J Cell Sci 2022](https://cob.silverchair.com/jcs/article-pdf/135/1/jcs258375/2126002/jcs258375.pdf); [JCB 2008](https://rupress.org/jcb/article/180/2/375/45178/Mapping-of-R-SNARE-function-at-distinct)). Treat as real but redundant |
| Postsynaptic AMPA receptor exocytosis | STX3, SNAP-47 (LTP-specific) | VAMP2 contributes to constitutive and regulated AMPA receptor insertion ([Jurado et al. 2013, PMID:23395379](https://pubmed.ncbi.nlm.nih.gov/23395379/)) |
| Insulin granule exocytosis | STX1A/STX4, SNAP25 | VAMP2 peptide impairs glucose-stimulated secretion in MIN6 cells (Nevins & Thurmond 2005, via secondary summary) |
| KCNB1 (Kv2.1) gating | N-terminus of VAMP2 | SNARE-independent; by similarity to rat only (UniProt) |
| WDFY2 / PKCζ | Phosphorylation by PRKCZ in vitro | PubMed:17313651; physiological relevance unclear |

## 5. Human disease

Heterozygous de novo VAMP2 variants cause a neurodevelopmental disorder with hypotonia and autistic features, with or without hyperkinetic movements (NEDHAHM, MIM:618760).
- The founding report described five individuals: two single-residue deletions and three missense variants at conserved residues in the C-terminal half of the SNARE motif ([Salpietro et al. 2019, AJHG, PMID:30929742](https://pubmed.ncbi.nlm.nih.gov/30929742/)).
- C-terminal missense variants gave the more severe phenotype, adding epilepsy, central visual impairment and a movement disorder.
- Reconstituted lipid-mixing assays showed impaired fusion.
- A secondary knowledge base proposes dominant-negative action for SNARE-motif missense variants and haploinsufficiency for truncating ones ([dismech](https://dismech.monarchinitiative.org/pages/disorders/VAMP2-Related_Neurodevelopmental_Disorder.html)). This is not primary evidence.
- My searches found no 2020–2024 case series. I recall later reports (Sunaga et al. 2020; Simmons et al. 2020, which tested 4-aminopyridine), but did not verify them here.

## 6. Recent developments (2022–2024)

- Cryo-EM of the Munc18-1 template complex with syntaxin-1 and synaptobrevin (Stepien 2022) and its single-molecule dynamics (PNAS 2022).
- VAMP2–α-synuclein co-condensates in vesicle clustering and protection from aggregation (Wang 2024).
- Reassessment of v-SNARE redundancy in GLUT4 traffic using knockouts (2022).
- A domain-by-domain review of VAMP2 (Yan et al. 2022).

## 7. Summary for annotation

- **Molecular function:** SNARE (SNAP receptor) activity; binding to syntaxin-1 and SNAP-25. VAMP2 is the vesicular R-SNARE whose zippering with t-SNAREs supplies the force for bilayer merger.
- **Core process:** synaptic vesicle fusion with the presynaptic active-zone membrane (Ca²⁺-evoked neurotransmitter release), including SNARE complex assembly and vesicle priming or docking.
- **Secondary processes:** synaptic vesicle endocytosis and recycling; regulated exocytosis in endocrine cells and adipocytes (GLUT4), with redundancy; postsynaptic AMPA receptor insertion.
- **Location:** synaptic vesicle membrane, as a tail-anchored protein with a cytoplasmic SNARE motif. Also secretory granule membrane, the plasma membrane after fusion, and the SNARE complex.
- **Not core:** KCNB1 modulation, the WDFY2/PKCζ interaction, and in-vitro STX11 pairing.

## Sources

- [Yan et al. 2022, The function of VAMP2 in mediating membrane fusion (Front Mol Neurosci)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9816800/)
- [SNARE single-molecule/fusion pore review, PMC9588726](https://pmc.ncbi.nlm.nih.gov/articles/PMC9588726)
- [Half-zippered intermediate review, PMC4859083](https://pmc.ncbi.nlm.nih.gov/articles/PMC4859083)
- [Stein et al. 2009, PDB 3HD7](https://rcsb.org/structure/3hd7)
- [Dhara et al. 2016, eLife 17571](https://elifesciences.org/articles/17571.pdf)
- [PMC10796598 (syb2 copy number / juxtamembrane)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10796598)
- [PMC4103061 (TMD and fusion pore)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103061)
- [Stepien et al. 2022, PMID:35731863](https://pubmed.ncbi.nlm.nih.gov/35731863/)
- [Template complex dynamics, PMC9894263](https://pmc.ncbi.nlm.nih.gov/articles/PMC9894263)
- [Schoch 2001 summary, PMC2739239](https://pmc.ncbi.nlm.nih.gov/articles/PMC2739239)
- [Zimmermann et al. 2014, PMID:24944211](https://pubmed.ncbi.nlm.nih.gov/24944211/)
- [Liu et al. 2019, PMC6668203](https://pmc.ncbi.nlm.nih.gov/articles/PMC6668203)
- [Salpietro et al. 2019, PMID:30929742](https://pubmed.ncbi.nlm.nih.gov/30929742/)
- [dismech VAMP2-related disorder page](https://dismech.monarchinitiative.org/pages/disorders/VAMP2-Related_Neurodevelopmental_Disorder.html)
- [Sadler et al. 2015, PMC4310743](https://pmc.ncbi.nlm.nih.gov/articles/PMC4310743)
- [J Cell Sci 2022, VAMP2/3 knockout and GLUT4](https://cob.silverchair.com/jcs/article-pdf/135/1/jcs258375/2126002/jcs258375.pdf)
- [JCB 2008, R-SNARE mapping in GLUT4 traffic](https://rupress.org/jcb/article/180/2/375/45178/Mapping-of-R-SNARE-function-at-distinct)
- [Koo et al. 2011, PMC3158172](https://pmc.ncbi.nlm.nih.gov/articles/PMC3158172)
- [Gordon & Cousin 2016, iTRAPs](https://www.frontiersin.org/articles/10.3389/fnsyn.2016.00001)
- [Jurado et al. 2013, PMID:23395379](https://pubmed.ncbi.nlm.nih.gov/23395379/)
- [Diao et al. 2013, eLife 00592](https://elifesciences.org/articles/592)
- [Wang et al. 2024, Nat Cell Biol (listing)](https://x-mol.com/paper/1807852604308910080)
- [TRC40 pathway and VAMP2, PMC5788257](https://pmc.ncbi.nlm.nih.gov/articles/PMC5788257)
- UniProt P63027 flat file (local copy `genes/human/VAMP2/VAMP2-uniprot.txt`)

## Citations

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9816800/
2. https://dx.doi.org/10.3389/fnmol.2022.948160
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC10796598
4. https://rcsb.org/structure/3hd7
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC9588726
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC4859083
7. https://elifesciences.org/articles/17571.pdf
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC4103061
9. https://pubmed.ncbi.nlm.nih.gov/35731863/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC9894263
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC2739239
12. https://pubmed.ncbi.nlm.nih.gov/24944211/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC6668203
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC5788257
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3158172
16. https://www.frontiersin.org/articles/10.3389/fnsyn.2016.00001
17. https://elifesciences.org/articles/592
18. https://x-mol.com/paper/1807852604308910080
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC4310743
20. https://cob.silverchair.com/jcs/article-pdf/135/1/jcs258375/2126002/jcs258375.pdf
21. https://rupress.org/jcb/article/180/2/375/45178/Mapping-of-R-SNARE-function-at-distinct
22. https://pubmed.ncbi.nlm.nih.gov/23395379/
23. https://pubmed.ncbi.nlm.nih.gov/30929742/
24. https://dismech.monarchinitiative.org/pages/disorders/VAMP2-Related_Neurodevelopmental_Disorder.html