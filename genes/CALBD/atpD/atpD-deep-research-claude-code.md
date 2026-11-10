---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-31T00:33:17.855286'
end_time: '2026-10-31T00:34:49.023816'
duration_seconds: 91.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: CALBD
  gene_id: atpD
  gene_symbol: atpD
  uniprot_accession: B9MS68
  protein_description: 'RecName: Full=ATP synthase subunit beta {ECO:0000255|HAMAP-Rule:MF_01347};
    EC=7.1.2.2 {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=ATP synthase F1 sector
    subunit beta {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=F-ATPase subunit
    beta {ECO:0000255|HAMAP-Rule:MF_01347};'
  gene_info: Name=atpD {ECO:0000255|HAMAP-Rule:MF_01347}; OrderedLocusNames=Athe_1424;
  organism_full: Caldicellulosiruptor bescii (strain ATCC BAA-1888 / DSM 6725 / KCTC
    15123 / Z-1320) (Anaerocellum thermophilum).
  protein_family: Belongs to the ATPase alpha/beta chains family.
  protein_domains: AAA+_ATPase. (IPR003593); ATP-synt_VA_C. (IPR055190); ATP_synth_F1_bsu.
    (IPR005722); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053)
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 7
  total_cost_usd: 0.6468323
  session_id: b84cef90-0d4f-4c40-9265-160dad6a68f8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** B9MS68
- **Protein Description:** RecName: Full=ATP synthase subunit beta {ECO:0000255|HAMAP-Rule:MF_01347}; EC=7.1.2.2 {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=ATP synthase F1 sector subunit beta {ECO:0000255|HAMAP-Rule:MF_01347}; AltName: Full=F-ATPase subunit beta {ECO:0000255|HAMAP-Rule:MF_01347};
- **Gene Information:** Name=atpD {ECO:0000255|HAMAP-Rule:MF_01347}; OrderedLocusNames=Athe_1424;
- **Organism (full):** Caldicellulosiruptor bescii (strain ATCC BAA-1888 / DSM 6725 / KCTC 15123 / Z-1320) (Anaerocellum thermophilum).
- **Protein Family:** Belongs to the ATPase alpha/beta chains family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ATP-synt_VA_C. (IPR055190); ATP_synth_F1_bsu. (IPR005722); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atpD" matches the protein description above**
2. **Verify the organism is correct:** Caldicellulosiruptor bescii (strain ATCC BAA-1888 / DSM 6725 / KCTC 15123 / Z-1320) (Anaerocellum thermophilum).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atpD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atpD** (gene ID: atpD, UniProt: B9MS68) in CALBD.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# atpD (B9MS68), ATP synthase subunit beta, *Caldicellulosiruptor bescii* DSM 6725: research report

## 1. Identity check and how much literature exists

The identity checks out. UniProt B9MS68 (ATPB_CALBD, 467 aa, locus Athe_1424) has the gene name *atpD*. Its curated name is "ATP synthase subunit beta" (EC 7.1.2.2), and it is placed in the "ATPase alpha/beta chains family" by HAMAP rule MF_01347 (local file `genes/CALBD/atpD/atpD-uniprot.txt`). The organism is *C. bescii* strain ATCC BAA-1888 / DSM 6725 (NCBI taxon 521460), formerly called *Anaerocellum thermophilum*. It is an extremely thermophilic, strictly anaerobic, cellulolytic bacterium in the phylum Bacillota.

Several independent signatures say this protein is the catalytic F1 beta subunit, not some other P-loop ATPase:
- NCBIfam TIGR01039 (atpD)
- HAMAP MF_01347 (bacterial ATP synthase beta)
- PIRSF039072
- InterPro IPR005722 (ATP_synth_F1_bsu)
- PROSITE PS00152 (ATPASE_ALPHA_BETA)
- Pfam PF02874, PF00006 and PF22919, which together make the N-terminal β-barrel, nucleotide-binding and C-terminal domain layout of F/V/A-ATPase α/β subunits

**How much is known.** No study characterises this particular protein experimentally. UniProt rates its existence at level 3, "Inferred from homology", and every functional statement in the record comes from HAMAP-Rule MF_01347 (`ECO:0000255`). The GO annotations in `atpD-goa.tsv` are all electronic:
- ATP binding (GO:0005524)
- proton-transporting ATP synthase activity, rotational mechanism (GO:0046933)
- plasma membrane (GO:0005886)
- proton-transporting ATP synthase complex (GO:0045259)
- proton motive force-driven ATP synthesis (GO:0015986)
- ATP metabolic process (GO:0046034)
- proton transmembrane transport (GO:1902600)

The function below is therefore inferred. The basis is that the F-type ATP synthase β subunit is extremely conserved, and its mechanism has been worked out in *E. coli*, bovine mitochondria, *Bacillus* PS3 and other systems. *C. bescii*-specific information is limited to genome-level and physiological context.

## 2. Primary function: the catalytic subunit of the F1F0 ATP synthase

### 2.1 The reaction

UniProt, by HAMAP rule MF_01347, assigns:

> "Produces ATP from ADP in the presence of a proton gradient across the membrane. The catalytic sites are hosted primarily by the beta subunits." Catalytic activity: **ATP + H2O + 4 H⁺(in) = ADP + phosphate + 5 H⁺(out)** (RHEA:57720; EC 7.1.2.2).

- **Direction.** EC 7.1.2.2 is written in the hydrolysis direction, as is the convention for translocases. Physiologically the enzyme is reversible. Under a sufficient proton-motive force (PMF) it synthesises ATP from ADP and inorganic phosphate (Pi). When PMF is low it can hydrolyse ATP and pump protons outward, building or keeping a membrane potential.
- **Substrates.** In the synthesis direction the substrates are ADP and Pi with Mg²⁺. In the hydrolysis direction it is Mg-ATP. F1 β subunits strongly prefer adenine nucleotides. The coupling ion here is the proton, as the HAMAP/Rhea assignment states.
- **Proton or sodium?** Whether *C. bescii* ATP synthase pumps Na⁺ rather than H⁺ has not been tested experimentally. That question is decided by the c subunit (AtpE), not by β, so it does not change β's catalytic role.

### 2.2 Place in the complex

UniProt's SUBUNIT comment (HAMAP) describes the canonical bacterial architecture:
- **F1 (catalytic):** α₃β₃γδε.
- **F0 (membrane proton channel):** a₁b₂c₉₋₁₂.
- The α and β subunits alternate to form a hexameric ring that surrounds the coiled-coil γ subunit.
- A central stalk (γε) and a peripheral stalk (δ plus b₂) connect F1 to F0.

Three of the six nucleotide-binding sites, the catalytic ones, sit mainly on the β subunits at the α/β interfaces. The other three, on α, are non-catalytic.

### 2.3 Mechanism: binding change and rotary catalysis

Proton flow through the a/c-ring interface of F0 turns the c-ring and the attached γε rotor. The asymmetric γ subunit, turning inside the α₃β₃ ring, forces each β subunit in turn through three conformations: open/empty, loose (ADP + Pi bound) and tight (ATP formed). This is Boyer's binding change mechanism, later confirmed by the asymmetric F1 crystal structure and by single-molecule rotation experiments.

- Each β subunit "sequentially binds ADP and Pi, then undergoes a conformational transition and makes ATP, and finally changes conformation again with release of product" (see the ATP synthase evolution/energetics review, arXiv 2006.09357, and Boyer's review on PubMed, PMID 1429543).
- The energy of the proton gradient goes mainly into **releasing tightly bound ATP**, not into forming the phosphoanhydride bond. The equilibrium constant at the catalytic site is close to 1 (PMC2610185; PMC2670139).
- The DELSEED loop in the C-terminal domain of β couples catalysis to rotation. It sits "up" when the β catalytic site holds nucleotide and "down" when the site is empty (PMC3191020; PMC1236596).
- Rotation is driven by conformational changes carried through the β subunit's P-loop, helix B and β-sheet 4 module (PMC4894397).

### 2.4 Conserved catalytic residues in B9MS68

I checked the sequence directly (it is in the local UniProt file). The motifs that define a working catalytic β subunit are all present:

| Feature | Position in B9MS68 | Sequence | Role (by homology) |
|---|---|---|---|
| Walker A / P-loop | 152–159 (UniProt FT BINDING, HAMAP) | **GGAGVGKT** | Binds the β/γ-phosphates of ATP; Lys158 and Thr159 coordinate the phosphates and Mg²⁺ |
| Catalytic glutamate | Glu184, in "GV**GER**TREG" (183–192) | GER | Equivalent to *E. coli* βGlu181 and bovine βGlu188, the general base that activates water for hydrolysis or synthesis |
| Adenine-binding / Walker B region | "RIPSAVGYQPTLA" at 264–276 | YQPTL | Conserved β-subunit segment lining the catalytic site |
| DELSEED loop | 384–390 | **DELSEED** | Couples catalysis to γ rotation; contacts γ |

These invariant motifs are retained, nothing suggests divergence or pseudoenzyme status, and HAMAP, TIGRFAM and PROSITE all match. Together this strongly supports B9MS68 as a catalytically active F1 β subunit.

## 3. Where it acts

- **Location.** UniProt (HAMAP) gives "Cell membrane; Peripheral membrane protein". β has no transmembrane segment. It is held at the cytoplasmic face of the plasma membrane as part of the F1 head, which is anchored to F0 through the central and peripheral stalks.
- **Catalytic side.** The nucleotide-binding sites face the **cytoplasm**, where ATP is made from cytoplasmic ADP and Pi. *C. bescii* is a Gram-positive-type monoderm bacterium, so the relevant membrane is the plasma (cytoplasmic) membrane.
- **GO.** Reasonable terms are plasma membrane (GO:0005886) and, more specifically, the proton-transporting ATP synthase complex (GO:0045259). For a complete F1 the catalytic core term GO:0045261, "proton-transporting ATP synthase complex, catalytic core F(1)", may be preferable. I have not run the OLS/QuickGO lookup this needs to confirm it.

## 4. Physiological and pathway context in *C. bescii*

*C. bescii* gets energy mainly by fermenting plant polysaccharides (cellulose and hemicellulose) through the Embden–Meyerhof pathway. Its main products are acetate, lactate, H₂ and CO₂. Most ATP comes from **substrate-level phosphorylation**, at phosphoglycerate kinase, pyruvate kinase or PPi-dependent enzymes, and at acetate kinase. The ATP synthase connects redox metabolism to the membrane's energy state.

- **Ech hydrogenase plus ATP synthase.** *C. bescii* lacks the Rnf complex: it "does not contain the six genes (rnfCDGEAB) that encode the Rnf complex". When Rnf from *Thermoanaerobacter* sp. X514 was expressed heterologously, product profiles changed (Williams-Rhaesa et al., *Metabolic Engineering Communications*, Dec 2018; [DOAJ](https://doaj.org/article/be6d04fbfac94dcea6fb9b8736075cf4)). Without Rnf, the membrane-bound Ech hydrogenase is the likely main ion-pumping complex. It oxidises reduced ferredoxin to H₂ while translocating protons (or Na⁺). The ATP synthase then uses the resulting gradient to make ATP. A 2019 JBC figure on *C. bescii* hydrogenases describes a pathway in which "oxidation of the resulting reduced ferredoxin by the Ech hydrogenase and the associated ATP synthase" serves energy conservation ([PMC6597818](https://pmc.ncbi.nlm.nih.gov/articles/PMC6597818/figure/F4)).
- **Genome-scale metabolic model.** A *C. bescii* model concluded that optimal ethanol production from biomass sugars depends on ATP production, redox balancing and proton translocation. These are mediated through "the interplay of an ATP synthase, a membrane-bound hydrogenase, a bifurcating hydrogenase and a bifurcating NAD- and NADP-dependent oxidoreductase" ([PMC8269263](https://pmc.ncbi.nlm.nih.gov/articles/PMC8269263)).
- **Pyrophosphate as an energy carrier.** In the close relative *C. saccharolyticus*, cells in exponential growth held high PPi (about 4 ± 2 mM) and relatively low ATP (0.43 ± 0.07 mM). PPi appears to act as a central energy carrier alongside ATP, and the PPi/ATP ratio falls sharply in stationary phase (Bielen et al., Wageningen University; [WUR record](https://research.wur.nl/en/publications/pyrophosphate-as-a-central-energy-carrier-in-the-hydrogen-produci/)). This suggests the PMF–ATP synthase axis is one part of a mixed energy economy in *Caldicellulosiruptor*, not its only source of ATP. Whether the enzyme mainly synthesises ATP or, under some conditions, hydrolyses it to keep up PMF for transport has not been measured in *C. bescii*.
- **Pathway terms.** At the pathway level, atpD takes part in proton motive force-driven ATP synthesis (GO:0015986) and proton transmembrane transport coupled to ATP synthesis (GO:1902600, as part of the complex). "ATP metabolic process" (GO:0046034) is a broad parent term and adds little.

## 5. Evolutionary and structural inference

- F-type β subunits belong to the RecA-like P-loop NTPase fold. They are homologous to the catalytic A subunits of V/A-type ATPases; the shared PF22919 ATP-synt_VA_C domain reflects this. The α/β paralogous pair arose by gene duplication before the last universal common ancestor (LUCA), and β kept catalysis while α became non-catalytic.
- PANTHER places B9MS68 in PTHR15184 ("ATP SYNTHASE"), subfamily PTHR15184:SF71 ("ATP SYNTHASE SUBUNIT BETA, MITOCHONDRIAL"). That subfamily name reflects the family's dominant members, not a mitochondrial location for this protein. GO IBA terms for this family typically rest on experimental annotations in *E. coli* AtpD, yeast ATP2 and human ATP5F1B.
- The β subunit is among the most conserved proteins known, roughly 60–70% identical between bacteria and mitochondria. So transferring catalytic function by homology is unusually reliable here.

## 6. Summary for GO curation

| Aspect | Supported conclusion | Evidence basis |
|---|---|---|
| Molecular function | Catalytic subunit of the rotary proton-translocating ATP synthase (GO:0046933); ATP/ADP binding (GO:0005524) | HAMAP MF_01347, TIGR01039, PROSITE PS00152; conserved Walker A (152–159), Glu184, DELSEED (384–390) |
| Reaction | ADP + Pi + n H⁺(out) ⇌ ATP + H₂O + n H⁺(in) (EC 7.1.2.2; RHEA:57720) | HAMAP/Rhea |
| Complex | F1 α₃β₃γδε of the F1F0 ATP synthase (GO:0045259) | HAMAP SUBUNIT |
| Location | Cytoplasmic face of the plasma membrane, peripheral (GO:0005886) | HAMAP SUBCELLULAR LOCATION; no TM segment |
| Process | Proton motive force-driven ATP synthesis (GO:0015986) | Homology; *C. bescii* model and hydrogenase studies place ATP synthase alongside Ech in energy conservation |
| Experimental data on B9MS68 itself | None | UniProt PE 3 |

Open questions: whether the coupling ion is H⁺ or Na⁺, which would need c-subunit analysis; how much the enzyme works in synthesis versus hydrolysis mode given *Caldicellulosiruptor*'s reliance on PPi and substrate-level phosphorylation; and how the enzyme adapts to work at about 75–80 °C.

## Sources

- UniProtKB B9MS68 (ATPB_CALBD), entry version 94, 02-Sep-2026: local file `genes/CALBD/atpD/atpD-uniprot.txt`; GO annotations in `genes/CALBD/atpD/atpD-goa.tsv`
- Williams-Rhaesa AM et al., Rnf complex expression in *C. bescii*, *Metab Eng Commun* (Dec 2018): https://doaj.org/article/be6d04fbfac94dcea6fb9b8736075cf4
- *C. bescii* genome-scale metabolic model: https://pmc.ncbi.nlm.nih.gov/articles/PMC8269263
- *C. bescii* bifurcating/Ech hydrogenase figure (JBC 2019): https://pmc.ncbi.nlm.nih.gov/articles/PMC6597818/figure/F4
- Related *C. bescii* engineering paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC6041484
- Bielen et al., PPi as central energy carrier in *C. saccharolyticus*: https://research.wur.nl/en/publications/pyrophosphate-as-a-central-energy-carrier-in-the-hydrogen-produci/
- *Caldicellulosiruptor* metabolism (Biotechnol Biofuels 2013): https://biotechnologyforbiofuels.biomedcentral.com/articles/10.1186/1754-6834-6-85/figures/1
- URI theses and publications on *Caldicellulosiruptor* bioenergetics: https://digitalcommons.uri.edu/theses/2331 ; https://digitalcommons.uri.edu/cmb_facpubs/155
- Literature index entry, PMID 34060912: https://neuinfo.org/literature/pmid:34060912?rpKey=on
- *C. saccharolyticus* proteome (UniProt UP000000256): https://uniprot.org/proteomes/UP000000256
- Waterloo thesis on *Caldicellulosiruptor* growth and regulatory metabolism: https://uwspace.uwaterloo.ca/handle/10012/9360
- ATP synthase evolution, energetics and membrane interactions (review): https://arxiv.org/pdf/2006.09357
- Flexibility of F1-ATPase α/β chains: https://arxiv.org/pdf/1608.02976
- Boyer PD, binding change mechanism review (PubMed 1429543): https://pubmed.ncbi.nlm.nih.gov/1429543/
- Binding change, catalytic site and DELSEED studies: https://pmc.ncbi.nlm.nih.gov/articles/PMC2610185 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2670139 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC1236596 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3191020 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4894397/figure/f1
- Springer, *J Bioenerg Biomembr* on F1 catalysis: https://link.springer.com/doi/10.1007/BF00762364

## Citations

1. https://doaj.org/article/be6d04fbfac94dcea6fb9b8736075cf4
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6597818/figure/F4
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC8269263
4. https://research.wur.nl/en/publications/pyrophosphate-as-a-central-energy-carrier-in-the-hydrogen-produci/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6041484
6. https://biotechnologyforbiofuels.biomedcentral.com/articles/10.1186/1754-6834-6-85/figures/1
7. https://digitalcommons.uri.edu/theses/2331
8. https://digitalcommons.uri.edu/cmb_facpubs/155
9. https://neuinfo.org/literature/pmid:34060912?rpKey=on
10. https://uniprot.org/proteomes/UP000000256
11. https://uwspace.uwaterloo.ca/handle/10012/9360
12. https://arxiv.org/pdf/2006.09357
13. https://arxiv.org/pdf/1608.02976
14. https://pubmed.ncbi.nlm.nih.gov/1429543/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC2610185
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC2670139
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC1236596
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC3191020
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC4894397/figure/f1
20. https://link.springer.com/doi/10.1007/BF00762364