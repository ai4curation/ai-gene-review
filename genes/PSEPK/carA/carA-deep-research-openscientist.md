---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:58:27.937851'
end_time: '2026-08-31T21:12:55.100573'
duration_seconds: 4467.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: carA
  gene_symbol: carA
  uniprot_accession: Q88DU5
  protein_description: 'RecName: Full=Carbamoyl phosphate synthase small chain {ECO:0000255|HAMAP-Rule:MF_01209};
    EC=6.3.5.5 {ECO:0000255|HAMAP-Rule:MF_01209}; AltName: Full=Carbamoyl phosphate
    synthetase glutamine chain {ECO:0000255|HAMAP-Rule:MF_01209};'
  gene_info: Name=carA {ECO:0000255|HAMAP-Rule:MF_01209}; OrderedLocusNames=PP_4724;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the CarA family. {ECO:0000255|HAMAP-
  protein_domains: Anth_synth/Amidotransfase. (IPR050472); CarbamoylP_synth_ssu. (IPR006274);
    CarbamoylP_synth_ssu_N. (IPR002474); CarbP_synth_ssu_N_sf. (IPR036480); Class_I_gatase-like.
    (IPR029062)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: carA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: carA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88DU5
- **Protein Description:** RecName: Full=Carbamoyl phosphate synthase small chain {ECO:0000255|HAMAP-Rule:MF_01209}; EC=6.3.5.5 {ECO:0000255|HAMAP-Rule:MF_01209}; AltName: Full=Carbamoyl phosphate synthetase glutamine chain {ECO:0000255|HAMAP-Rule:MF_01209};
- **Gene Information:** Name=carA {ECO:0000255|HAMAP-Rule:MF_01209}; OrderedLocusNames=PP_4724;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the CarA family. {ECO:0000255|HAMAP-
- **Key Domains:** Anth_synth/Amidotransfase. (IPR050472); CarbamoylP_synth_ssu. (IPR006274); CarbamoylP_synth_ssu_N. (IPR002474); CarbP_synth_ssu_N_sf. (IPR036480); Class_I_gatase-like. (IPR029062)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "carA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'carA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **carA** (gene ID: carA, UniProt: Q88DU5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *carA* (Q88DU5) — Carbamoyl Phosphate Synthetase Small Chain in *Pseudomonas putida* KT2440

## Summary

The gene **carA** (locus **PP_4724**; UniProt **Q88DU5**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes the **small (glutaminase) subunit of carbamoyl phosphate synthetase (CPSase; EC 6.3.5.5)**. Its primary molecular function is that of a **Class I glutamine amidotransferase (GATase)**: it hydrolyzes the amide side chain of L‑glutamine to yield L‑glutamate plus ammonia. The ammonia so produced is not released into the cytoplasm but is instead delivered — via an internal molecular tunnel running through the enzyme — to the large subunit (CarB, PP_4723), which condenses it with bicarbonate and consumes two molecules of ATP to build **carbamoyl phosphate**. CarA is therefore the nitrogen‑donating half of a two‑subunit molecular machine that performs the committed nitrogen‑entry step feeding two of the central biosynthetic pathways of the cell.

Carbamoyl phosphate is the shared precursor of both **de novo pyrimidine nucleotide biosynthesis** (via aspartate transcarbamoylase, PyrB) and **arginine biosynthesis** (via ornithine transcarbamoylase, ArgF/ArgI). In *P. putida*, as in *Escherichia coli* and most Gram‑negative bacteria, a single **carAB operon** supplies carbamoyl phosphate for both pathways, and its activity is coordinated by allosteric effectors originating from each branch (UMP as an inhibitor; ornithine and IMP as activators). The enzyme functions in the **cytoplasm** as a CarA–CarB heterodimeric (or higher‑order oligomeric) complex.

This annotation rests on four independent and mutually reinforcing lines of evidence assembled over five investigation iterations: (1) authoritative biochemical and structural literature on the paralogous, exhaustively characterized *E. coli* CPSase; (2) organism‑specific sequence analysis showing that *P. putida* CarA conserves the complete *E. coli* catalytic array at identical positions (70.8% global identity); (3) genome‑level confirmation of the canonical *carAB* operon organization in KT2440 with dual pathway assignment; and (4) a very‑high‑confidence AlphaFold structural model displaying a textbook Cys–His–Glu glutaminase catalytic triad. Together these establish CarA's function, mechanism, subcellular localization, and pathway context with high confidence.

---

## Gene/Protein Identity Verification

The target identity was confirmed at the outset and reinforced throughout the investigation:

- **UniProt:** Q88DU5
- **Gene:** carA (OrderedLocusName PP_4724)
- **Protein:** Carbamoyl phosphate synthase small chain (EC 6.3.5.5); AltName carbamoyl phosphate synthetase glutamine chain
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950)
- **Family:** CarA family; Class I glutamine amidotransferase
- **Domains:** IPR006274 (CarbamoylP_synth_ssu), IPR002474 (CarbamoylP_synth_ssu_N), IPR036480 (CarbP_synth_ssu_N_sf), IPR029062 (Class I GATase‑like), IPR050472 (Anth_synth/Amidotransferase)

The gene symbol *carA* is unambiguous and matches the protein description, the domain architecture, and the genome context (immediately upstream of *carB*/PP_4723 in a *carAB* operon). All literature and bioinformatic evidence gathered is consistent with this identity; no conflicting gene of the same symbol was encountered.

---

## Key Findings

### Finding 1 — CarA is the glutaminase/amidotransferase small subunit of carbamoyl phosphate synthetase (EC 6.3.5.5)

CarA belongs to the **Class I (Triad) glutamine amidotransferase family**, as indicated by its InterPro domain complement (IPR006274 CarbamoylP_synth_ssu; IPR029062 Class I GATase‑like). Functionally, this family comprises "molecular machines for the production and delivery of ammonia." In the paralogous and exhaustively characterized *E. coli* enzyme, the small amidotransferase subunit catalyzes the **hydrolysis of L‑glutamine to L‑glutamate and ammonia**, whereas the large subunit uses that ammonia, together with bicarbonate and 2 ATP, to make carbamoyl phosphate ([PMID: 10387030](https://pubmed.ncbi.nlm.nih.gov/10387030/): *"The smaller of the two subunits catalyzes the hydrolysis of glutamine to glutamate and ammonia. The larger subunit catalyzes the formation of carbamoyl phosphate using 2 mol of ATP, bicarbonate, and ammonia."*).

The reaction proceeds through a **covalent γ‑glutamyl thioester intermediate** on an active‑site cysteine (Cys‑269 in *E. coli* numbering), the diagnostic hallmark of a Class I GATase mechanism ([PMID: 10625457](https://pubmed.ncbi.nlm.nih.gov/10625457/): *"the reaction mechanism of the small subunit proceeds through the formation of a gamma-glutamyl thioester with Cys-269"*). The full catalytic array of the *E. coli* small subunit includes the nucleophile Cys‑269, a His‑353/Glu‑355 dyad that acts as a general base, and Ser‑47 and Gln‑273, which stabilize the tetrahedral oxyanion intermediate. Because *P. putida* is a γ‑proteobacterium closely related to *E. coli*, this well‑established mechanism transfers directly to CarA of KT2440.

### Finding 2 — CarA delivers ammonia to the large subunit through an intramolecular tunnel (substrate channeling)

A defining feature of CPSase is that the ammonia liberated by CarA is never released to the bulk solvent. X‑ray structures of *E. coli* CPSase reveal **three active sites** — one in the small subunit (glutaminase) and two in the large subunit (the carboxyphosphate/carbamate‑forming site and the carbamoyl‑phosphate‑forming site) — separated by roughly 45 Å from one another and connected by intramolecular tunnels that span nearly 100 Å end to end ([PMID: 10387030](https://pubmed.ncbi.nlm.nih.gov/10387030/): *"The three active sites within the heterodimeric protein are separated from one another by about 45 A."*). The tunnel connecting the CarA glutaminase site to the large‑subunit sites has been directly located in the crystal structure ([PMID: 10727215](https://pubmed.ncbi.nlm.nih.gov/10727215/): *"These three active sites are connected via an intermolecular tunnel, which has been located within the X-ray crystal structure of CPS from E. coli."*).

The functional reality of this **substrate channeling** has been proven experimentally by site‑directed constriction of the ammonia tunnel. Introducing bulky residues into the tunnel uncouples the two half‑reactions: the mutant enzymes can still make carbamoyl phosphate when supplied with *external* ammonia, but they can no longer use glutamine as the nitrogen source, because the internally generated ammonia can no longer reach the large subunit ([PMID: 10727215](https://pubmed.ncbi.nlm.nih.gov/10727215/): *"these mutant enzymes are fully functional when external ammonia is utilized as the nitrogen source but are unable to use glutamine for the synthesis of carbamoyl-P"*). This establishes that CarA's biological role is intimately physically coupled to CarB — CarA is not a stand‑alone glutaminase but the entry point of a channeled, multi‑site reaction.

### Finding 3 — The product, carbamoyl phosphate, is the shared precursor of pyrimidine and arginine biosynthesis, supplied by a single *carAB* operon

Carbamoyl phosphate (CP) is a precursor common to the synthesis of arginine and pyrimidines in all organisms. In *E. coli* and most other Gram‑negative bacteria — including *P. putida* — CP is produced by a **single CPSase enzyme encoded by the carAB operon** (carA = small subunit; carB = large subunit) ([PMID: 30238253](https://pubmed.ncbi.nlm.nih.gov/30238253/): *"In all organisms, carbamoylphosphate (CP) is a precursor common to the synthesis of arginine and pyrimidines. In Escherichia coli and most other Gram-negative bacteria, CP is produced by a single enzyme, carbamoylphosphate synthase (CPSase), encoded by the carAB operon."*). CP is subsequently consumed by **aspartate transcarbamoylase (PyrB)** in the de novo pyrimidine pathway and by **ornithine transcarbamoylase (ArgF/ArgI)** in the arginine pathway.

Because a single enzyme feeds two pathways, its activity must be balanced against the demands of both. CPSase activity is tightly controlled by **allosteric effectors originating from different pathways: an inhibitor (UMP) and two activators (ornithine and IMP)** ([PMID: 30238253](https://pubmed.ncbi.nlm.nih.gov/30238253/): *"CPSase activity is tightly controlled by allosteric effectors originating from different pathways: an inhibitor (UMP) and two activators (ornithine and IMP)"*). UMP provides pyrimidine feedback inhibition, ornithine (an arginine‑pathway intermediate) signals demand for arginine synthesis, and IMP links CP supply to purine status. The physiological importance of this dual role is underscored by loss‑of‑function studies: mutation of the *carB* gene in *Halomonas eurihalina* abolishes CP synthesis and renders the cell auxotrophic for both arginine and pyrimidines ([PMID: 12768451](https://pubmed.ncbi.nlm.nih.gov/12768451/): *"carries a mutation within the carB gene that encodes the synthesis of the large subunit of the carbamoylphosphate synthetase enzyme, which in turn catalyzes the synthesis of carbamoylphosphate, an important precursor of arginine and pyrimidines"*). By supplying the nitrogen for CP, CarA is therefore functionally essential to both branches.

### Finding 4 — *P. putida* CarA conserves the complete glutaminase catalytic array of *E. coli* CarA at identical sequence positions

To confirm that the mechanistic conclusions drawn from *E. coli* apply specifically to Q88DU5, a global pairwise alignment (Needleman–Wunsch) of *P. putida* KT2440 CarA (Q88DU5, 378 aa) against *E. coli* K‑12 CarA (P0A6F1, 382 aa) was performed. The two proteins share **70.8% sequence identity** (267 of 377 aligned positions). Critically, **all six functionally characterized catalytic and interacting residues** of the *E. coli* small subunit are conserved and map to identical positions in *P. putida*:

| *E. coli* residue | Role | Conserved in *P. putida* CarA |
|---|---|---|
| Cys‑269 | Thioester nucleophile | ✔ (identical position) |
| His‑353 | General base | ✔ |
| Glu‑355 | Activates/positions His & Cys | ✔ |
| Ser‑47 | Oxyanion / intermediate stabilization | ✔ |
| Gln‑273 | Intermediate stabilization | ✔ |
| Lys‑202 | Active‑site residue | ✔ |

This is direct, organism‑specific bioinformatic evidence that the glutaminase catalytic machinery — most importantly the Cys‑269 thioester nucleophile identified experimentally in *E. coli* ([PMID: 10625457](https://pubmed.ncbi.nlm.nih.gov/10625457/): *"the reaction mechanism of the small subunit proceeds through the formation of a gamma-glutamyl thioester with Cys-269"*) — is preserved intact in Q88DU5. The high overall identity (well above the ~30% threshold at which fold and function are reliably conserved) together with 100% conservation of the catalytic set makes the mechanistic transfer from *E. coli* to *P. putida* essentially certain.

### Finding 5 — In KT2440, *carA* (PP_4724) is organized in a *carAB* operon with *carB* (PP_4723) and is assigned to both arginine and pyrimidine pathways

Genome‑level annotation of KT2440 confirms the canonical operon structure. KEGG lists **ppu:PP_4724 = carA**, orthologous to K01956 (carbamoyl‑phosphate synthase small subunit, EC 6.3.5.5), at genomic coordinates complement(5,372,033..5,373,169). The immediately adjacent gene **ppu:PP_4723 = carB** corresponds to K01955 (large subunit, EC 6.3.5.5) at complement(5,368,706..5,371,936). Both genes lie on the minus strand, with *carA* directly upstream of *carB* separated by only a ~96 bp intergenic gap — the exact *carAB* arrangement conserved from *E. coli*. Both genes are mapped by KEGG to pathway **ppu00220 (Arginine biosynthesis)** and pathway **ppu00240 (Pyrimidine metabolism)**, reflecting CP's dual downstream fate. The other flanking gene, PP_4725 (a *dapB*‑like dihydrodipicolinate reductase, EC 1.17.1.8), is functionally unrelated and not part of the operon.

This genomic organization exactly matches the reviewed model of a single *carAB* operon supplying CP for both pathways in Gram‑negative bacteria ([PMID: 30238253](https://pubmed.ncbi.nlm.nih.gov/30238253/): *"CP is produced by a single enzyme, carbamoylphosphate synthase (CPSase), encoded by the carAB operon"*). The co‑transcription of *carA* and *carB* ensures stoichiometric production of the two subunits that must assemble into the functional heterodimeric enzyme.

### Finding 6 — The AlphaFold model of Q88DU5 shows a pre‑assembled Cys269–His353–Glu355 catalytic triad with canonical glutaminase geometry

The AlphaFold Protein Structure Database v6 model **AF‑Q88DU5‑F1** is of very high confidence, with a mean pLDDT of **97.8** across all 378 residues and a mean pLDDT of **98.6** over the catalytic residues specifically. Direct measurement of interatomic distances in the model confirms a classic Class I GATase catalytic triad:

| Interaction | Distance (Å) | Interpretation |
|---|---|---|
| His353 ND1 – Glu355 OE1 | 2.70 | H‑bond orienting/polarizing His (charge‑relay) |
| Cys269 SG – His353 NE2 | 3.72 | His poised as general base to deprotonate Cys thiol |
| Cys269 SG – Ser47 OG | 5.14 | Oxyanion‑hole environment adjacent to nucleophile |
| Cys269 SG – Gln273 NE2 | 5.10 | Intermediate stabilization adjacent to nucleophile |

The predicted fold shows the expected **two‑domain architecture** — an N‑terminal domain (residues ~1–150) and a C‑terminal GATase domain — both well folded (region mean pLDDT 97.5 and 97.9, respectively). This modeled active‑site geometry is precisely that required for the glutamine‑hydrolysis reaction attributed to the small subunit ([PMID: 10387030](https://pubmed.ncbi.nlm.nih.gov/10387030/): *"The smaller of the two subunits catalyzes the hydrolysis of glutamine to glutamate and ammonia."*). The structural evidence thus independently corroborates the sequence‑based conclusion (Finding 4) that Q88DU5 possesses a fully functional glutaminase active site.

---

## Mechanistic Model / Interpretation

Integrating the six findings yields a coherent mechanistic picture of CarA's role in *P. putida* KT2440. CarA is the **nitrogen‑supplying half** of a two‑subunit, three‑active‑site molecular machine. The reaction can be summarized as three coupled half‑reactions occurring at three spatially separated sites, connected by internal tunnels:

```
                CarA (small subunit, Q88DU5)         CarB (large subunit, PP_4723)
                ┌───────────────────────────┐        ┌────────────────────────────────────────────┐
                │   GLUTAMINASE SITE         │        │  Carboxyphosphate site   Carbamoyl-P site   │
                │  Cys269–His353–Glu355      │        │  (ATP #1, HCO3-)         (ATP #2)            │
                │  triad + Ser47/Gln273      │        │                                              │
 L-Gln ───────► │  L-Gln + H2O →             │        │                                              │
                │    L-Glu + NH3             │        │                                              │
                │            │               │        │                                              │
                │            ▼               │        │                                              │
                │        [ NH3 ] ══ammonia tunnel (~45–100 Å)══► HCO3- + ATP → carboxyphosphate     │
                │                            │        │        + NH3 → carbamate                      │
                │                            │        │        ══carbamate tunnel══► + ATP →          │
                │                            │        │            CARBAMOYL PHOSPHATE ───────────────┼──►
                └───────────────────────────┘        └──────────────────────────────────────────────┘

 Net: L-Gln + 2 ATP + HCO3- + H2O → carbamoyl phosphate + L-Glu + 2 ADP + Pi     (EC 6.3.5.5)
```

**Step 1 (CarA):** L‑glutamine binds in the CarA GATase domain. The His353–Glu355 dyad deprotonates the Cys269 thiol, and the resulting thiolate attacks the glutamine amide carbon to form a covalent γ‑glutamyl thioester, releasing ammonia. Hydrolysis of the thioester regenerates the enzyme and produces L‑glutamate. Ser47 and Gln273 stabilize the oxyanion tetrahedral intermediate. This is the reaction that Findings 1, 4, and 6 collectively establish and localize to a specific, conserved, structurally verified active site in Q88DU5.

**Step 2 (channeling):** The ammonia migrates through the internal ammonia tunnel to the large subunit rather than escaping to solvent (Finding 2). This channeling protects the reactive intermediate and couples glutaminase turnover to CP synthesis.

**Step 3 (CarB):** In the large subunit, bicarbonate is phosphorylated by ATP to carboxyphosphate, which reacts with the channeled ammonia to form carbamate; a second ATP phosphorylates carbamate to yield carbamoyl phosphate. (These steps are CarB's function; CarA supplies only the nitrogen.)

**Downstream fate and regulation:** The carbamoyl phosphate produced is partitioned between two biosynthetic destinations (Findings 3, 5): the pyrimidine branch (PyrB → … → UMP/UTP/CTP) and the arginine branch (ArgF/ArgI → citrulline → arginine). Because a single *carAB* operon feeds both, the enzyme integrates signals from both pathways through allostery — UMP inhibits (pyrimidine sufficiency), while ornithine and IMP activate. CarA thus sits at a **metabolic crossroads**, and its glutaminase activity is the nitrogen‑entry step for the entire node.

**Localization:** All available evidence — the absence of signal peptides or membrane‑spanning segments in the family, the soluble two‑domain fold, and the nature of the substrates (glutamine, ATP, bicarbonate) and products (charged small metabolites feeding cytoplasmic pathways) — places CarA in the **cytoplasm**, functioning as part of the soluble CarA–CarB complex.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [10387030](https://pubmed.ncbi.nlm.nih.gov/10387030/) | *The amidotransferase family of enzymes: molecular machines for the production and delivery of ammonia* | Defines the small subunit as the glutaminase producing ammonia for the large subunit; gives 45 Å inter‑site distance (Findings 1, 2, 6) |
| [10625457](https://pubmed.ncbi.nlm.nih.gov/10625457/) | *Deconstruction of the catalytic array within the amidotransferase subunit of CPS* | Establishes the covalent γ‑glutamyl thioester mechanism on Cys‑269, the residue shown conserved in Q88DU5 (Findings 1, 4) |
| [10727215](https://pubmed.ncbi.nlm.nih.gov/10727215/) | *An engineered blockage within the ammonia tunnel of CPS prevents the use of glutamine but not ammonia* | Directly documents the ammonia tunnel and proves substrate channeling from the small subunit (Finding 2) |
| [30238253](https://pubmed.ncbi.nlm.nih.gov/30238253/) | *Regulation of carbamoylphosphate synthesis in E. coli: an amazing metabolite at the crossroad of arginine and pyrimidine biosynthesis* | Establishes single *carAB* operon supplying CP to both pathways and its allosteric regulation (UMP/ornithine/IMP) (Findings 3, 5) |
| [12768451](https://pubmed.ncbi.nlm.nih.gov/12768451/) | *Identification and characterization of the carAB genes in Halomonas eurihalina* | Loss‑of‑function of the operon causes dual arginine + uracil auxotrophy, defining the pathway role (Finding 3) |
| [15322282](https://pubmed.ncbi.nlm.nih.gov/15322282/) | *Long-range allosteric transitions in CPS* | Independent structural confirmation of three active sites, intramolecular tunnel, and allosteric control by ornithine/UMP/IMP |
| [10950966](https://pubmed.ncbi.nlm.nih.gov/10950966/) | *Restricted passage of reaction intermediates through the ammonia tunnel of CPS* | Biochemical (NMR/isotope) evidence for ammonia tunneling within native CPS |
| [15081891](https://pubmed.ncbi.nlm.nih.gov/15081891/) | *Access to the carbamate tunnel of CPS* | Characterizes the second (carbamate) tunnel in the large subunit, completing the channeling model |
| [12379099](https://pubmed.ncbi.nlm.nih.gov/12379099/) | *Structural defects within the carbamate tunnel of CPS* | Shows tunnel blockages impair CP synthesis without altering individual active‑site chemistry (channeling) |
| [26592762](https://pubmed.ncbi.nlm.nih.gov/26592762/) | *Structure of human CPS1* | Cross‑kingdom confirmation of the tunnel/channeling architecture in a CPS homolog |
| [15743958](https://pubmed.ncbi.nlm.nih.gov/15743958/) | *Repression of the pyr operon in Lactobacillus plantarum…* | Confirms CP as the shared arginine/pyrimidine precursor and the operon's link to growth phenotypes |
| [33837829](https://pubmed.ncbi.nlm.nih.gov/33837829/) | *Enhanced L-arginine production by improving carbamoyl phosphate supply* | Demonstrates CP (and glutamine supply) as the limiting node for arginine production, illustrating pathway importance |
| [19128030](https://pubmed.ncbi.nlm.nih.gov/19128030/) | *Dihydroorotase/ATCase one-pot reactor for pyrimidine biosynthesis* | Places CP downstream in the pyrimidine assembly line |

The evidence is notably convergent: structural biology, enzyme kinetics, mutagenesis, genome organization, and comparative sequence analysis all point to the same conclusion. No source examined contradicts the annotation of Q88DU5 as the glutaminase small subunit of CPSase.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88DU5 itself.** All enzymatic, kinetic, and structural mechanistic data derive from the paralogous *E. coli* enzyme (and human CPS1). The transfer to *P. putida* is an inference — albeit a very strong one — grounded in 70.8% sequence identity and 100% conservation of the catalytic array, not in a purified‑protein assay of the *P. putida* protein.

2. **Structural evidence is a prediction, not an experimental structure.** The catalytic‑triad geometry comes from an AlphaFold model. Although the confidence is exceptionally high (mean pLDDT 97.8; catalytic residues 98.6), no crystal or cryo‑EM structure of *P. putida* CarA has been determined, and the model represents an apo, static snapshot rather than a substrate‑bound or channeling‑competent conformation.

3. **Operon regulation in *P. putida* is inferred from other organisms.** The allosteric effectors (UMP, ornithine, IMP) and transcriptional control of *carAB* are established in *E. coli* and other bacteria. Species‑specific regulatory details in *P. putida* (promoter architecture, exact effector affinities, potential integration with its distinctive amino‑acid/carbon metabolism) have not been experimentally verified here.

4. **Quantitative kinetic parameters are unknown for Q88DU5.** Km for glutamine, kcat, the degree of coupling between glutaminase and synthetase activities, and the tunnel geometry specific to the *P. putida* enzyme remain undetermined.

5. **Single‑enzyme assumption.** It is assumed, based on genome annotation, that *P. putida* KT2440 relies on a single CPSase (the *carAB* product) for both pathways, as is typical of Gram‑negative bacteria. Any accessory or condition‑specific CP source was not exhaustively excluded.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and glutaminase assay.** Clone and purify Q88DU5 (co‑expressed with CarB/PP_4723) and measure glutamine‑dependent CPSase activity, glutaminase partial activity, and ammonia‑dependent activity to confirm function directly and obtain Km/kcat.

2. **Complementation / auxotrophy test.** Delete *carA* (PP_4724) in KT2440 and test for the predicted dual arginine + uracil auxotrophy; complement with wild‑type and with a Cys269→Ser catalytic‑null variant to prove the nucleophile's requirement in vivo.

3. **Catalytic‑residue mutagenesis.** Individually mutate the conserved Cys269, His353, and Glu355 and assay for loss of glutamine‑dependent (but retention of ammonia‑dependent) CP synthesis — the signature of a glutaminase‑specific lesion.

4. **Experimental structure determination.** Solve the crystal or cryo‑EM structure of the *P. putida* CarA–CarB complex, ideally with a glutamine analog (e.g., DON or acivicin) bound, to validate the AlphaFold‑predicted triad and visualize the ammonia tunnel.

5. **Regulatory characterization.** Test allosteric modulation of the *P. putida* enzyme by UMP, ornithine, and IMP, and map the *carAB* promoter/regulatory region to determine whether transcriptional control responds to arginine and/or pyrimidine status as in *E. coli*.

6. **Metabolic‑flux relevance.** Given *P. putida*'s biotechnological importance, quantify how CarA/CP flux limits arginine and pyrimidine production under industrially relevant conditions, informing metabolic‑engineering strategies analogous to those reported for *Corynebacterium* ([PMID: 33837829](https://pubmed.ncbi.nlm.nih.gov/33837829/)).

---

## Conclusion

The gene **carA (PP_4724, Q88DU5)** of *Pseudomonas putida* KT2440 encodes the **small glutaminase subunit of carbamoyl phosphate synthetase (EC 6.3.5.5)**. Its primary function is a **Class I glutamine amidotransferase reaction** — hydrolysis of L‑glutamine to L‑glutamate plus ammonia via a covalent Cys269 thioester intermediate — with the ammonia channeled through an internal tunnel to the large subunit CarB, which builds carbamoyl phosphate from bicarbonate and two ATP. The enzyme operates as a **cytoplasmic CarA–CarB complex** encoded by the **carAB operon**, and the carbamoyl phosphate it produces is the **shared precursor of de novo pyrimidine and arginine biosynthesis**. This annotation is supported convergently by definitive literature on the paralogous *E. coli* enzyme, by organism‑specific conservation of the entire catalytic array (70.8% identity; all six catalytic residues conserved), by genome‑level operon organization and pathway mapping, and by a very‑high‑confidence AlphaFold model displaying a canonical Cys–His–Glu catalytic triad.


## Artifacts

- [OpenScientist final report](carA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](carA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10387030
2. PMID:10625457
3. PMID:10727215
4. PMID:30238253
5. PMID:12768451
6. PMID:33837829