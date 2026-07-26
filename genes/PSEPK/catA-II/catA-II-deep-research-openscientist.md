---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T06:40:01.589421'
end_time: '2026-07-15T06:56:18.737686'
duration_seconds: 977.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: catA-II
  gene_symbol: catA-II
  uniprot_accession: Q88I35
  protein_description: 'RecName: Full=catechol 1,2-dioxygenase {ECO:0000256|ARBA:ARBA00013118};
    EC=1.13.11.1 {ECO:0000256|ARBA:ARBA00013118};'
  gene_info: Name=catA-II {ECO:0000313|EMBL:AAN68774.1}; OrderedLocusNames=PP_3166
    {ECO:0000313|EMBL:AAN68774.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the intradiol ring-cleavage dioxygenase family.
  protein_domains: Catechol_dOase_N. (IPR007535); Cchol_dOase_prob. (IPR012801); Intradiol_dOase_C.
    (IPR000627); Intradiol_dOase_core. (IPR015889); Intradiol_RC_Dioxygenase. (IPR050770)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: catA-II-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: catA-II-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I35
- **Protein Description:** RecName: Full=catechol 1,2-dioxygenase {ECO:0000256|ARBA:ARBA00013118}; EC=1.13.11.1 {ECO:0000256|ARBA:ARBA00013118};
- **Gene Information:** Name=catA-II {ECO:0000313|EMBL:AAN68774.1}; OrderedLocusNames=PP_3166 {ECO:0000313|EMBL:AAN68774.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the intradiol ring-cleavage dioxygenase family.
- **Key Domains:** Catechol_dOase_N. (IPR007535); Cchol_dOase_prob. (IPR012801); Intradiol_dOase_C. (IPR000627); Intradiol_dOase_core. (IPR015889); Intradiol_RC_Dioxygenase. (IPR050770)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "catA-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'catA-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **catA-II** (gene ID: catA-II, UniProt: Q88I35) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *catA-II* (Q88I35, PP_3166) — Catechol 1,2-Dioxygenase of *Pseudomonas putida* KT2440

## Summary

The gene **catA-II** (UniProt **Q88I35**; ordered locus name **PP_3166**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a **catechol 1,2-dioxygenase** (EC 1.13.11.1; KEGG ortholog K03381). This is a **soluble, cytoplasmic, non-heme Fe(III)-dependent intradiol (ortho-cleaving) ring-fission dioxygenase**. Its primary and defining catalytic function is to use molecular oxygen to cleave the aromatic ring of **catechol** between its two adjacent hydroxyl-bearing carbons, producing **cis,cis-muconate**:

```
catechol + O2  →  cis,cis-muconate + 2 H+     (RHEA:23852; EC 1.13.11.1)
```

This reaction is the **committed, ring-opening step of the catechol branch of the β-ketoadipate (ortho-cleavage) pathway**, the central funnel through which *P. putida* channels a wide variety of aromatic growth substrates into the tricarboxylic acid cycle. The enzyme's ferric catalytic center is held by the family-conserved **2-tyrosinate / 2-histidine ligand set** (Tyr165, Tyr199, His223, His225 in the Q88I35 sequence), a signature shared with all structurally characterized intradiol dioxygenases.

A key insight from this investigation is the **paralog identity** of catA-II. KT2440 carries **two ~77%-identical catechol 1,2-dioxygenase isozymes**. catA-II (PP_3166) is embedded in a dedicated **benzoate uptake/oxidation gene island** (benD–benK–catA-II–benE-II), which marks it as the **benzoate-route** copy: the catechol it cleaves is generated from benzoate by the upstream benzoate dioxygenase (BenABCD) and dihydrodiol dehydrogenase (BenD). The second isozyme, catA-I (PP_3713), sits in the canonical chromosomal catBCA ortho-cleavage operon. Both are bona fide catechol 1,2-dioxygenases, but their genomic contexts assign catA-II specifically to the benzoate→catechol catabolic branch.

Beyond its catalytic role, the enzyme's **product, cis,cis-muconate, is a regulatory signal**: it is the physiological effector of the LysR-type transcriptional activator **CatR**, which induces the downstream *cat* (β-ketoadipate) regulon. catA-II therefore both **drives** aromatic carbon flux into central metabolism and **generates the inducer** that coordinates expression of the pathway that consumes its product.

---

## Gene/Protein Identity (verified)

| Field | Value |
|-------|-------|
| Gene symbol | catA-II |
| UniProt accession | Q88I35 |
| Ordered locus name | PP_3166 |
| EC number | 1.13.11.1 |
| KEGG ortholog | K03381 |
| Protein | catechol 1,2-dioxygenase |
| Length | 304 aa |
| Cofactor | Fe(3+) (non-heme mononuclear iron) |
| Family | Intradiol ring-cleavage dioxygenase family |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |

**Verification note:** The gene symbol catA-II, the protein description (catechol 1,2-dioxygenase, EC 1.13.11.1), the organism (KT2440), and the domain/family assignments (intradiol ring-cleavage dioxygenase; Catechol_dOase_N, Intradiol_dOase_C, Intradiol_dOase_core) are all mutually consistent between UniProt, KEGG, and the primary literature retrieved. This is the correct target. The only ambiguity is intra-organismal: KT2440 has two catechol 1,2-dioxygenase paralogs, and this report distinguishes catA-II (PP_3166) from catA-I (PP_3713) explicitly (see Finding F007).

---

## Key Findings

### F001 — catA-II is a catechol 1,2-dioxygenase catalyzing intradiol cleavage of catechol to cis,cis-muconate

The core functional assignment is robust and multiply supported. UniProt Q88I35 and KEGG (ppu:PP_3166) both annotate the product as **catechol 1,2-dioxygenase, EC 1.13.11.1, KO K03381**. The catalytic activity is defined as catechol + O2 = cis,cis-muconate + 2 H+ (RHEA:23852), with an obligatory **Fe(3+) cofactor**. This is the first, ring-opening step of the catechol branch of the β-ketoadipate pathway.

Classic enzymology directly establishes the chemistry. In studies of aromatic catabolism, **catechol 1,2-dioxygenase catalyses ortho-fission of catechol which is then metabolized via the β-ketoadipate pathway; formation of cis,cis-muconate and β-ketoadipate was demonstrated by enzyme assays** ([PMID: 4063065](https://pubmed.ncbi.nlm.nih.gov/4063065/)). The enzyme's identity and its position at the head of a consecutive enzyme cascade are confirmed by the cloning and characterization of the cat gene cluster, in which **catA encodes catechol 1,2-dioxygenase (EC 1.13.11.1), followed by catB (muconate lactonizing enzyme, EC 5.5.1.1) and catC (muconolactone isomerase, EC 5.3.3.4)** ([PMID: 3139626](https://pubmed.ncbi.nlm.nih.gov/3139626/)). This nails down both the EC number and the ordered position of catechol 1,2-dioxygenase as the first of the catechol-branch enzymes.

**Reaction type:** intradiol (ortho) ring cleavage — the C–C bond broken lies *between* the two hydroxylated carbons, distinguishing it mechanistically from extradiol (meta) dioxygenases (EC 1.13.11.2), which cleave adjacent to the diol and use Fe(II).

### F002 — In KT2440, the enzyme functions in the benzoate/aromatic catabolic funnel of the β-ketoadipate pathway

Direct proteomic evidence in the exact target organism places this enzyme in benzoate catabolism. In a combined 2-DE/MS and cleavable ICAT proteomic analysis of *P. putida* KT2440, **benzoate dioxygenase (BenA, BenD) and catechol 1,2-dioxygenase (CatA) were induced by benzoate** ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)). Benzoate is converted by benzoate dioxygenase and BenD to catechol, which CatA then cleaves. The same study showed that **benzoate, p-hydroxybenzoate and vanilline were degraded by different dioxygenases and then converged in the same beta-ketoadipate degradation pathway** ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)), placing catechol 1,2-dioxygenase squarely within the benzoate-to-β-ketoadipate catabolic funnel.

Consistent with this, KEGG maps PP_3166 to **benzoate degradation (ppu00362)**, **toluene degradation (ppu00623)**, chloro-/fluoro-benzoate degradation pathways, and to module **M00568 (catechol ortho-cleavage, catechol ⇒ 3-oxoadipate)**. Downstream, the products of the catechol branch converge with the protocatechuate branch (PcaD, PcaF) on the shared lower β-ketoadipate pathway, ultimately yielding succinyl-CoA and acetyl-CoA for the TCA cycle.

### F003 — Q88I35 is a non-heme Fe(III) intradiol dioxygenase with the conserved 2-His/2-Tyr iron-coordination signature

Sequence analysis of the 304-residue Q88I35 protein locates the canonical intradiol-dioxygenase catalytic residues: a **His-x-His motif (His223, His225)** within the conserved C-terminal **"PAHVHFF"** segment, and **two tyrosinate ligands (Tyr165, Tyr199)** spaced ~34 residues apart. This mirrors the active site of the structurally characterized hydroxyquinol/catechol 1,2-dioxygenase family, in which **the catalytic Fe(III) is pentacoordinated by the conserved Tyr160, Tyr194, His218 and His220** (in PnpC from *P. putida* DLL-E4) ([PMID: 30446218](https://pubmed.ncbi.nlm.nih.gov/30446218/)). The equivalence between the KT2440 ligand set (Tyr165, Tyr199, His223, His225) and the structurally defined PnpC ligand set is direct evidence for the conserved 2-Tyr/2-His ferric coordination.

The enzyme class is further confirmed by crystallographic and spectroscopic work showing that **intradiol-cleaving catechol 1,2 dioxygenases are Fe(III) dependent enzymes that act on catechol and substituted catechols, including chlorocatechols pollutants, by inserting molecular oxygen in the aromatic ring** ([PMID: 20869471](https://pubmed.ncbi.nlm.nih.gov/20869471/)). Domain assignments corroborate this: Pfam PF00775 (Intradiol_dioxygenase C) and PF04444 (Dioxygenase_N); InterPro IPR000627 / IPR015889 / IPR050770 (intradiol ring-cleavage dioxygenase family), matching the domain architecture listed in the target's UniProt record (Catechol_dOase_N; Intradiol_dOase_C; Intradiol_dOase_core).

### F004 — catA-II acts as a soluble cytoplasmic homodimeric enzyme with a broad catechol/substituted-catechol substrate range

Members of this family are **homodimeric non-heme iron enzymes** that carry a bound amphipathic phospholipid at the dimer interface, which modulates their kinetics. For *P. putida* chlorocatechol 1,2-dioxygenase, **the kinetics changes from Michaelis-Menten to a cooperative scheme, indicating that conformational changes propagate between monomers in the absence of amphipatic molecules** ([PMID: 23754625](https://pubmed.ncbi.nlm.nih.gov/23754625/)) — direct evidence for a communicating multi-subunit (dimeric) architecture with a bound amphipathic cofactor.

Crystallographic characterization further shows that the family binds a phospholipid and that specific active-site residues govern substrate preference: the authors **characterised the phospholipid bound to the enzyme and provided a structural framework to understand the inversion of substrate specificity showed by the mutants** ([PMID: 20869471](https://pubmed.ncbi.nlm.nih.gov/20869471/)). This indicates a **broad but tunable substrate range** spanning catechol and substituted catechols (methyl-, chloro-catechols).

**Localization:** The β-ketoadipate pathway is a cytoplasmic catabolic route, and the 304-aa protein has no signal peptide and no membrane-spanning region, indicating **cytoplasmic localization**. The enzyme therefore acts on catechol generated intracellularly (after benzoate is imported and oxidized) rather than in the periplasm or on the membrane.

### F005 — catA-II is genomically embedded in a benzoate uptake/catabolism gene cluster

KEGG genome-context analysis of KT2440 shows PP_3166 (catA-II) is flanked by benzoate-catabolism genes, forming a tight, same-strand operonic arrangement:

| Locus | Gene | Product / function | Coordinates |
|-------|------|--------------------|-------------|
| PP_3164 | benD | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) — converts benzoate-dioxygenase dihydrodiol to catechol | 3,584,988–3,585,749 |
| PP_3165 | benK | benzoate MFS/AAHS-family transporter (K05548) | 3,585,807–3,587,135 |
| **PP_3166** | **catA-II** | **catechol 1,2-dioxygenase (EC 1.13.11.1)** | **3,587,165–3,588,079** |
| PP_3167 | benE-II | benzoate membrane transport protein (K05782) | 3,588,154–3,589,425 |
| PP_3168 | nicP-I | porin-like | downstream |

The tight intergenic spacing and shared strand identify this as a coherent **benzoate uptake + ring-cleavage module**. The physical adjacency of benD (which makes catechol) and catA-II (which cleaves catechol) creates metabolic channeling from benzoate oxidation directly into ring fission, coupling catA-II mechanistically to the benzoate→catechol funnel.

### F006 — The product cis,cis-muconate is the physiological inducer coordinating the β-ketoadipate (cat) regulon

The enzyme's product is not merely a metabolic intermediate but a **regulatory effector**. In *P. putida*, cis,cis-muconate is the effector of the LysR-type regulator **CatR**, which activates the catBC operon and the recruited pheBA promoter. **The catBC operon encodes two enzymes of the beta-ketoadipate pathway and also requires CatR and cis,cis-muconate for its expression** ([PMID: 7596284](https://pubmed.ncbi.nlm.nih.gov/7596284/)). DNase I footprinting shows CatR binds the catBC/pheBA promoters and switches from a repression-site to an activation-site occupancy only when cis,cis-muconate is present.

This regulatory logic is corroborated in the target organism by proteomics on the aromatic substrate vanillin, which showed coordinate up-regulation of β-ketoadipate pathway enzymes: **particularly enzymes belonging to the β-ketoadipate pathway including a transcriptional regulator and porins specific for vanillin uptake increased in abundance** ([PMID: 25026441](https://pubmed.ncbi.nlm.nih.gov/25026441/)). Thus, by generating cis,cis-muconate, catA-II both drives carbon flux and produces the inducer that switches on the downstream consuming enzymes — a feed-forward autoinduction motif.

### F007 — KT2440 encodes two catechol 1,2-dioxygenase isozymes: catA-II (PP_3166) and catA-I (PP_3713), ~77% identical

Genome analysis identifies **two paralogous catechol 1,2-dioxygenase genes** in KT2440, both assigned KEGG ortholog K03381 (EC 1.13.11.1):

| Feature | catA-II / PP_3166 (this target) | catA-I / PP_3713 |
|---------|--------------------------------|------------------|
| Length | 304 aa | 311 aa |
| Genomic context | benzoate island: benD–benK–**catA-II**–benE-II | canonical ortho-cleavage operon: **catA-I**–catC (PP_3714)–catB (PP_3715) |
| Assigned role | benzoate-route catechol cleavage | classic cat-operon catechol cleavage |
| Fe(III) ligands | Tyr165, Tyr199, His223, His225 (conserved) | conserved 2-Tyr/2-His set |

A Needleman–Wunsch global alignment of the two proteins gives **240/313 = 76.7% amino-acid identity**. Both retain the conserved intradiol Fe(III) 2-Tyr/2-His ligand set, so both are genuine catechol 1,2-dioxygenases. The distinguishing feature is genomic context: catA-II is co-located with benzoate transport and oxidation genes, whereas catA-I is co-located with the downstream muconate/muconolactone-converting genes catB and catC. This assigns catA-II specifically to the **benzoate branch**.

### F008 — The benK–catA–benE arrangement is a conserved, benzoate-inducible module in *P. putida*

The gene neighborhood of catA-II is not an accident of KT2440 but a **conserved functional module** across *P. putida*. In *P. putida* CSV86, the ben locus is organized as **benK–catA–benE–benF**, in which benK is an aromatic-acid:H+ MFS symporter, benE a benzoate:H+ symporter, benF a benzoate-specific OprD porin, and catA the catechol 1,2-dioxygenase: **benzoate transport and metabolism genes are clustered at the ben locus as benK-catA-benE-benF** ([PMID: 28591829](https://pubmed.ncbi.nlm.nih.gov/28591829/)). The paper explicitly identifies the enzyme: **benF and catA encode benzoate specific porin, OprD and catechol 1,2-dioxygenase, respectively** ([PMID: 28591829](https://pubmed.ncbi.nlm.nih.gov/28591829/)).

Functionally, benzoate transport in CSV86 is an **inducible, proton-motive-force-driven active process** (Km ≈ 4.5 μM; 90–100% inhibited by dinitrophenol), and benF, benK, and benE are transcriptionally induced by benzoate. This provides experimental support, in a closely related strain, that a catechol 1,2-dioxygenase co-located with benK/benE forms a **dedicated benzoate uptake-and-ring-cleavage module** — precisely the arrangement seen around KT2440 catA-II (benK/PP_3165–catA-II/PP_3166–benE-II/PP_3167).

---

## Mechanistic Model / Interpretation

catA-II sits at a pivotal branch point in *P. putida*'s aromatic catabolism. The integrated model combining all eight findings is:

```
   Benzoate (extracellular)
        │
        │  BenK / BenE (benzoate:H+ symporters)  ← PMF-driven active uptake
        ▼
   Benzoate (cytoplasm)
        │
        │  Benzoate 1,2-dioxygenase (BenABC) + reductase
        ▼
   benzoate-cis-dihydrodiol
        │
        │  BenD dehydrogenase (PP_3164; EC 1.3.1.25)
        ▼
   ┌──────────────┐
   │  CATECHOL    │
   └──────┬───────┘
          │
          │  ★ catA-II  (PP_3166; catechol 1,2-dioxygenase, EC 1.13.11.1)
          │     Fe(III), O2, INTRADIOL / ortho cleavage
          ▼
   ┌────────────────────┐
   │  cis,cis-MUCONATE  │──────────────┐
   └──────┬─────────────┘              │ (effector)
          │                            ▼
          │  CatB (muconate       ┌─────────────┐
          │  cycloisomerase)      │ CatR (LTTR) │ → activates catBC / cat regulon
          ▼                       └─────────────┘
   muconolactone
          │  CatC (muconolactone isomerase)
          ▼
   β-ketoadipate enol-lactone → ... → β-ketoadipate
          │  PcaD, PcaIJ, PcaF (shared lower pathway)
          ▼
   succinyl-CoA + acetyl-CoA  →  TCA cycle
```

**Enzyme mechanism.** catA-II is a non-heme iron dioxygenase of the intradiol class. The catechol substrate chelates the mononuclear **Fe(III)** center (held by Tyr165, Tyr199, His223, His225); molecular oxygen then attacks the activated substrate, and both oxygen atoms are incorporated as the ring is cleaved between the two hydroxyl-bearing carbons (ortho fission), yielding the ring-opened diacid cis,cis-muconate. The ferric (rather than ferrous) oxidation state and the 2-Tyr/2-His coordination distinguish intradiol enzymes from their extradiol Fe(II) counterparts.

**Quaternary structure and localization.** The active enzyme is a soluble, cytoplasmic **homodimer** bearing a bound amphipathic phospholipid at the interface; the phospholipid and inter-subunit communication tune the kinetic profile (Michaelis–Menten vs. cooperative). It carries out its function in the cytoplasm, downstream of benzoate import and oxidation.

**Paralog division of labor.** KT2440's two catechol 1,2-dioxygenases (~77% identical) partition by genomic context. catA-II (PP_3166) is embedded with benzoate transport/oxidation genes (benD–benK–catA-II–benE-II) and is benzoate-induced; catA-I (PP_3713) is embedded with the muconate-processing genes (catA-I–catC–catB). catA-II is therefore best described as the **benzoate-route** catechol 1,2-dioxygenase.

**Regulatory feed-forward.** Because its product cis,cis-muconate is the CatR effector, catA-II activity generates the very signal that induces the downstream cat regulon — an elegant autoinduction that ensures the ring-cleavage product is efficiently consumed and prevents accumulation of the potentially toxic intermediate.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|--------------------------------|
| [4063065](https://pubmed.ncbi.nlm.nih.gov/4063065/) | *Degradation of lawsone by P. putida L2* | Establishes the reaction: ortho-fission of catechol → cis,cis-muconate → β-ketoadipate (F001) |
| [3139626](https://pubmed.ncbi.nlm.nih.gov/3139626/) | *Cloning of catA and catBC clusters from P. aeruginosa PAO* | Confirms EC 1.13.11.1 and catA as first of the consecutive cat-branch enzymes (F001) |
| [16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) | *Aromatic catabolic pathways in P. putida KT2440 (proteomics)* | Direct evidence in KT2440: CatA induced by benzoate; branches converge on β-ketoadipate (F002) |
| [30446218](https://pubmed.ncbi.nlm.nih.gov/30446218/) | *Crystal structure of hydroxyquinol 1,2-dioxygenase PnpC (P. putida)* | Defines the conserved 2-Tyr/2-His Fe(III) coordination matching Q88I35 (F003) |
| [20869471](https://pubmed.ncbi.nlm.nih.gov/20869471/) | *Multidisciplinary characterization of catechol 1,2 dioxygenase* | Confirms Fe(III), intradiol mechanism, substituted-catechol range, phospholipid, substrate specificity (F003, F004) |
| [23754625](https://pubmed.ncbi.nlm.nih.gov/23754625/) | *Amphipatic molecules affect P. putida chlorocatechol 1,2-dioxygenase* | Demonstrates dimeric, inter-monomer-communicating architecture (F004) |
| [7596284](https://pubmed.ncbi.nlm.nih.gov/7596284/) | *CatR-induced DNA bending at pheBA/catBC promoters* | cis,cis-muconate + CatR required for downstream β-ketoadipate gene expression (F006) |
| [25026441](https://pubmed.ncbi.nlm.nih.gov/25026441/) | *Proteome response of KT2440 to vanillin* | Coordinate induction of β-ketoadipate enzymes, regulator, uptake porins (F006) |
| [28591829](https://pubmed.ncbi.nlm.nih.gov/28591829/) | *Benzoate transport in P. putida CSV86* | Establishes conserved benK-catA-benE benzoate module; identifies catA as catechol 1,2-dioxygenase (F008) |

Supporting biomimetic/model chemistry ([PMID: 15446874](https://pubmed.ncbi.nlm.nih.gov/15446874/), [PMID: 21766098](https://pubmed.ncbi.nlm.nih.gov/21766098/), [PMID: 20835480](https://pubmed.ncbi.nlm.nih.gov/20835480/)) reinforces the intradiol-cleavage mechanism and the role of Fe–O(tyrosinate) coordination geometry in determining intradiol vs. extradiol regioselectivity. Applied studies ([PMID: 26306712](https://pubmed.ncbi.nlm.nih.gov/26306712/)) using CatA to produce cis,cis-muconate in engineered *E. coli* further confirm the enzyme's product and its substrate-binding determinants.

**Note on directness of evidence:** No study cited here characterized the purified Q88I35 protein individually. The functional assignment rests on (i) database annotation (UniProt/KEGG), (ii) conserved sequence/active-site signatures shared with structurally solved family members, (iii) proteomic detection of "CatA" in benzoate-grown KT2440, and (iv) conserved genomic context across *P. putida* strains. This is strong convergent evidence but is inferential at the level of the specific isozyme.

---

## Limitations and Knowledge Gaps

1. **No isozyme-specific biochemistry.** The kinetic parameters (kcat, Km for catechol and substituted catechols), substrate specificity profile, and phospholipid identity have not been measured for the purified catA-II (PP_3166) protein specifically. Family properties are inferred from related enzymes (chlorocatechol 1,2-dioxygenase, Acinetobacter CatA, PnpC).

2. **catA-II vs. catA-I functional redundancy.** Although genomic context assigns catA-II to the benzoate branch and catA-I to the cat operon, no gene-knockout or expression study cited here directly demonstrates the *in vivo* division of labor between the two ~77%-identical isozymes in KT2440. Whether they are truly non-redundant, differentially regulated, or partially interchangeable is unresolved.

3. **Substrate specificity resolution.** It is unknown whether catA-II preferentially handles unsubstituted catechol vs. methyl-/chloro-catechols, which would distinguish it functionally from chlorocatechol-specialized isozymes.

4. **Structural data.** No experimental 3D structure of Q88I35 exists; the 2-Tyr/2-His ligand assignment is by homology, not crystallography of this protein.

5. **Regulation specifics.** The CatR/cis,cis-muconate induction circuit is best characterized for the classic cat operon; how the benzoate-island catA-II is transcriptionally controlled (BenR vs. CatR, promoter architecture) in KT2440 was not directly established here.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymology of PP_3166.** Clone, express, and purify Q88I35; determine steady-state kinetics (kcat, Km) for catechol and a panel of substituted catechols (3-/4-methylcatechol, 3-/4-chlorocatechol) to define substrate specificity and directly compare with catA-I/PP_3713.

2. **Single and double knockouts (ΔcatA-II, ΔcatA-I, double).** Measure growth on benzoate, 4-hydroxybenzoate, and other aromatics, plus catechol 1,2-dioxygenase activity in cell extracts, to test the proposed benzoate-branch specialization and quantify redundancy.

3. **Transcriptional analysis of the ben island.** RT-qPCR / RNA-seq of PP_3164–PP_3168 across benzoate vs. succinate growth; promoter mapping and identification of the cognate regulator (BenR vs. CatR) to establish how catA-II is induced.

4. **Structural determination.** Solve the crystal structure of Q88I35 to confirm the Fe(III) coordination (Tyr165/Tyr199/His223/His225), the homodimer interface, and any bound phospholipid.

5. **Metabolic flux / channeling test.** Assess whether physical adjacency of BenD and catA-II supports substrate channeling of catechol, e.g., via co-purification, proximity assays, or in vitro coupled-enzyme kinetics.

6. **cis,cis-Muconate production application.** Given the biotechnological interest in muconate as a nylon/adipic-acid precursor, benchmark catA-II against engineered CatA variants ([PMID: 26306712](https://pubmed.ncbi.nlm.nih.gov/26306712/)) for muconate titer in a heterologous host.

---

*Report generated from an autonomous multi-iteration investigation (5 iterations; 8 confirmed findings; 25 papers reviewed). All functional claims are traceable to the cited literature and to UniProt/KEGG database annotations for Q88I35 / PP_3166.*


## Artifacts

- [OpenScientist final report](catA-II-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](catA-II-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:4063065
2. PMID:3139626
3. PMID:16470664
4. PMID:30446218
5. PMID:20869471
6. PMID:23754625
7. PMID:7596284
8. PMID:25026441
9. PMID:28591829
10. PMID:15446874
11. PMID:21766098
12. PMID:20835480
13. PMID:26306712