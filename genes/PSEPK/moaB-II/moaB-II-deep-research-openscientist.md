---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:54:50.815159'
end_time: '2026-07-20T18:18:42.364311'
duration_seconds: 5031.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moaB-II
  gene_symbol: moaB-II
  uniprot_accession: Q88E67
  protein_description: 'RecName: Full=Molybdenum cofactor biosynthesis protein B {ECO:0000256|ARBA:ARBA00015262,
    ECO:0000256|PIRNR:PIRNR006443};'
  gene_info: Name=moaB-II {ECO:0000313|EMBL:AAN70173.1}; OrderedLocusNames=PP_4600
    {ECO:0000313|EMBL:AAN70173.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MoaB/Mog family.
  protein_domains: MoaB. (IPR012245); MoaB/Mog-like_dom_sf. (IPR036425); MoaB/Mog_dom.
    (IPR001453); MoaB_proteobac. (IPR013484); MoCF_biosynth_CS. (IPR008284)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: moaB-II-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moaB-II-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E67
- **Protein Description:** RecName: Full=Molybdenum cofactor biosynthesis protein B {ECO:0000256|ARBA:ARBA00015262, ECO:0000256|PIRNR:PIRNR006443};
- **Gene Information:** Name=moaB-II {ECO:0000313|EMBL:AAN70173.1}; OrderedLocusNames=PP_4600 {ECO:0000313|EMBL:AAN70173.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MoaB/Mog family.
- **Key Domains:** MoaB. (IPR012245); MoaB/Mog-like_dom_sf. (IPR036425); MoaB/Mog_dom. (IPR001453); MoaB_proteobac. (IPR013484); MoCF_biosynth_CS. (IPR008284)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moaB-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moaB-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moaB-II** (gene ID: moaB-II, UniProt: Q88E67) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *moaB-II* (Q88E67, PP_4600) in *Pseudomonas putida* KT2440

## 1. Identity verification (MANDATORY)

- **UniProt:** Q88E67 — 172 aa protein, *Pseudomonas putida* KT2440.
- **Gene:** `moaB-II`; ordered locus `PP_4600` (EMBL AAN70173.1).
- **Description:** Molybdenum cofactor biosynthesis protein B.
- **Family:** MoaB/Mog family. **Domains:** MoaB (IPR012245), MoaB/Mog-like domain superfamily (IPR036425), MoaB/Mog domain (IPR001453), MoaB_proteobac (IPR013484), MoCF_biosynth conserved site (IPR008284).
- **UniProt keywords:** Molybdenum cofactor biosynthesis; GTP-binding; Nucleotide-binding.

The gene symbol, organism, protein family and domain architecture retrieved from UniProt are **mutually consistent**: `moaB-II` denotes a *moaB* paralog ("copy II") of the molybdenum-cofactor (Moco) biosynthesis protein B in *P. putida*. Literature on the MoaB/Mog family (E. coli MoaB/MogA, archaeal MoaB, plant Cnx1, gephyrin) aligns with the domain/family assignment. **No literature describes a different, unrelated gene under this symbol that would create ambiguity.** The caveat is not mis-identification but *evidence type*: there is **no primary experimental study of the P. putida protein Q88E67 itself**; its annotation is by homology to characterized family members.

---

## 2. Summary answer

Q88E67/MoaB-II is a small (~19 kDa) cytoplasmic protein of the **MoaB/Mog family**, a paralog of MogA, predicted to participate in the terminal steps of **molybdenum-cofactor (Moco) / molybdopterin biosynthesis**. The MogA branch of this family catalyzes the **Mg²⁺/ATP-dependent adenylylation of molybdopterin (MPT → MPT-AMP)**, the activated intermediate from which molybdenum is inserted (by MoeA) to complete Moco. However, **MoaB-type proteins — including Q88E67 by its UniProt annotation — bind molybdopterin (and GTP) but lack MPT-adenylyltransferase activity**, and in *E. coli* MoaB is genetically dispensable for Moco synthesis. MoaB-II is therefore best described as a **MogA-like pterin/nucleotide-binding protein of the Moco pathway whose precise catalytic role is enigmatic and probably accessory/redundant**, acting in the cytoplasm.

---

## 3. Biochemical function and substrate specificity

### 3.1 The MoaB/Mog family and the reaction it centers on
The MoaB/Mog family unites bacterial MogA and MoaB, the plant multidomain protein Cnx1 (C-terminal G-domain), the animal protein gephyrin (G-domain), and *Drosophila* Cinnamon. Genetic complementation first showed that the C-terminal domain of Cnx1 "is homologous to the E. coli Moco proteins MoaB and MogA" and that these proteins act in "the last step of Moco biosynthesis, that is, the insertion of molybdenum into molybdopterin" (Stallmeyer et al., 1995, PMID 8528286). Structural work confirmed all family members are "involved in the insertion of an unknown molybdenum species into molybdopterin to form the molybdenum cofactor" (Bader et al., 2004, PMID 15159566).

Mechanistically, the reaction proceeds in two steps: the **MogA/G-domain** first **adenylylates molybdopterin**, and **MoeA/E-domain** then uses this MPT-AMP intermediate plus molybdate to insert Mo. Bevers et al. (2008) demonstrated directly that the MogA-type activity "catalyzes the adenylylation of MPT in a Mg2+ and ATP-dependent way" (PMID 18154309). Structural work on the eukaryotic G-domains confirms the chemistry and the intermediate: the plant Cnx1 G domain produces "adenylated molybdopterin (molybdopterin-AMP), a mechanistically important intermediate... subsequently processed in a magnesium-dependent reaction by the amino-terminal E domain of Cnx1 to yield active molybdenum cofactor" (Kuper et al., 2004, PMID 15306815), and in human gephyrin the "N-terminal G domain (GephG)" catalyzes "the penultimate adenylation of molybdopterin (MPT)" while the E domain performs "deadenylation as well as molybdate binding and insertion" (Kasaragod & Schindelin, 2016, PMID 27112598). These G domains are homologous to E. coli MogA (Schwarz et al., 2001, PMID 11554796) — the paralog family to which MoaB-II belongs. In *P. putida* the corresponding molybdate-insertion enzyme is MoeA (PP_2123), annotated to catalyze "the insertion of molybdate into adenylated molybdopterin with the concomitant release of AMP."

### 3.2 What distinguishes MoaB from MogA — and what Q88E67 is annotated to do
Although MoaB and MogA are close structural paralogs, they are **functionally non-equivalent**. In the same study, "only MogA is able to catalyze MPT adenylylation, whereas E. coli MoaB is inactive" (Bevers et al., 2008, PMID 18154309). The UniProt functional annotation of Q88E67 mirrors this precisely:

> "May be involved in the biosynthesis of molybdopterin. Can bind GTP and has low GTPase activity. Can bind MPT, but has no MPT adenylyl transferase activity." (UniProt Q88E67, ARBA ECO:0000256)

**Substrate/ligand specificity (by annotation transfer):** binds **molybdopterin (MPT)** and **GTP** (nucleotide-binding, GTP-binding keywords), with only **low GTPase activity** and **no adenylyltransferase catalysis**. It therefore appears to retain the pterin/nucleotide-binding pocket of the MogA scaffold without performing the defining MogA chemistry.

### 3.3 Genetic evidence for an accessory/redundant role
In *E. coli*, the physiological role of MoaB has remained "enigmatic": transposon insertions in *moaB* caused partial Moco-deficiency (likely polar effects on the *moaABCDE* operon), but "in-frame deletions of moaB, or moaB overexpression, had no effect on either phenotype," data "consistent with the lack of any role for MoaB in Moco biosynthesis in E. coli" (Kozmin & Schaaper, 2013, PMID 23680484). This supports interpreting MoaB-II as **dispensable/redundant or specialized** rather than catalyzing an essential, unique step. The "-II" designation indicates *P. putida* encodes more than one MoaB-type protein, consistent with paralog redundancy or subfunctionalization.

### 3.4 Evolutionary/genomic placement in *P. putida* (this work — bioinformatic analysis)
Enumerating the MoaB/Mog family in the *P. putida* KT2440 proteome (UniProt, taxon 160488) returns **exactly two members**: **moaB-I** (Q88L15, 179 aa, PP_2122) and **moaB-II** (Q88E67, 172 aa, PP_4600). Notably, the proteome contains **no gene annotated as MogA / molybdopterin adenylyltransferase** (0 hits), although it does encode the downstream **MoeA** (Q88L14, PP_2123) and **MobA** (Q88HA3, molybdenum cofactor guanylyltransferase).

Pairwise global alignments (Needleman–Wunsch, identity scoring) place moaB-II firmly in the **MoaB clade, not the MogA clade**:

| Comparison | % identity |
|---|---|
| MoaB-II (Q88E67) vs *E. coli* **MoaB** (P0AEZ9) | **55.2%** |
| MoaB-II (Q88E67) vs *E. coli* **MogA** (P0AF03) | 27.7% |
| MoaB-II vs MoaB-I (Q88L15) | 72.6% |
| *E. coli* MoaB vs MogA (reference) | 30.3% |

Because *E. coli* MoaB is the enzymatically **inactive** paralog and MoaB-II is ~55% identical to it (but only ~28% to the active MogA), sequence evolution independently supports the annotation that MoaB-II **lacks MogA-type adenylyltransferase activity**. MoaB-I and MoaB-II are 73% identical to each other, indicating a **gene-duplication** origin. Genomic context reinforces a division of labour: **moaB-I (PP_2122) is immediately adjacent to moeA (PP_2123)** — the two forming a syntenic Mo-insertion module — whereas **moaB-II (PP_4600) sits at a separate, distant locus**, most parsimoniously an accessory/duplicate copy.

---

## 4. Structure

MoaB proteins adopt a **modified Rossmann fold** and oligomerize. The 1.6 Å *E. coli* MoaB structure showed the protein is "assembled into a hexamer composed of two trimers" whose monomers have "high structural similarity with two proteins, MogA and MoeA," and with the G-domains of gephyrin and Cnx1; a putative active site was identified (Sanishvili et al., 2004, PMID 15269205). A second structure described a "32-symmetric hexamer" with a fold "similar to those of the MogA protein of E. coli, the G-domains of rat and human gephyrin and the G-domains of Cnx1 protein from A. thaliana" (Bader et al., 2004, PMID 15159566). Archaeal MoaB (ST2315) likewise forms trimers/hexamers with a fold "similar to those of other enzymes... involved in the molybdopterin- and molybdenum cofactor-biosynthesis pathways" (Antonyuk et al., 2009, PMID 20054111).

At 172 aa, Q88E67 is the size of a single MogA/G-type domain and is expected to fold identically and present the conserved pterin-binding pocket, most likely assembling into a trimer/hexamer. This is **structural/bioinformatic evidence** supporting the pathway assignment.

---

## 5. Localization

Moco biosynthesis is a **cytoplasmic** process, and the soluble MoaB/Mog-family proteins act there. Consequently MoaB-II is predicted to function in the **cytoplasm**, where it can access molybdopterin/MPT intermediates and nucleotides. No experimental localization for Q88E67 is available; the assignment follows from the pathway's known compartment and the protein's soluble, cofactor-binding nature.

A sequence-topology analysis performed here corroborates a soluble cytoplasmic protein: Kyte–Doolittle hydropathy (window 19) peaks at only 1.47 with **no window exceeding the ~1.6–1.8 transmembrane threshold** (zero predicted TM helices); the N-terminus lacks a cleavable Sec/Tat signal-peptide architecture (its hydrophobic start is the first β-strand of the Rossmann fold); and the protein has balanced charge (19 Asp+Glu vs 18 Lys+Arg) and near-neutral GRAVY (+0.137) — hallmarks of a soluble globular cytoplasmic enzyme rather than a membrane or secreted protein.

---

## 6. Pathway context and biological importance in *P. putida*

MoaB-II sits within **cofactor biosynthesis → molybdopterin/Moco biosynthesis** (UniProt PATHWAY annotation). This pathway is metabolically important in *P. putida*, which deploys numerous **Moco-dependent molybdenum hydroxylases**. Examples include the molybdopterin-cytosine-dinucleotide (MCD)-dependent enzymes of nicotine and N-heterocycle catabolism — where "a novel gene, PPS_4397 encoding moaE, is necessary for molybdopterin cytosine dinucleotide biosynthesis" (Jiang et al., 2015, PMID 26304596) and the 3-succinoylpyridine step uses "molybdenum molybdopterin cytosine dinucleotide as a cofactor" (Tang et al., 2013, PMID 24204321) — as well as quinoline/isoquinoline 2-oxidoreductases expressed in KT2440 (PMID 12654012, 12023088, 12730200) and heterologous xanthine oxidase (PMID 41933999). The Moco pathway that MoaB-family proteins support therefore underpins *P. putida*'s catabolic versatility toward aromatic and N-heterocyclic compounds and purine oxidation. **The report deliberately does not attribute broad pleiotropic phenotypes to MoaB-II specifically**, given the E. coli evidence that MoaB deletion is phenotypically silent.

---

## 7. Supported vs. open/refuted statements

**Supported (by homology + family biochemistry/structure):**
- Q88E67 belongs to the MoaB/Mog family and acts in the cytoplasmic Moco/molybdopterin biosynthetic pathway.
- It binds molybdopterin and GTP and adopts a MogA-like G-domain fold (likely oligomeric).
- It does **not** possess the MogA MPT-adenylyltransferase activity (per its annotation and E. coli MoaB biochemistry).

- MoaB-II belongs evolutionarily to the (inactive) proteobacterial MoaB clade, not the MogA clade (~55% vs ~28% identity), and is one of two duplicated MoaB paralogs; moaB-I is syntenic with moeA while moaB-II is at a separate locus.

**Open / not established:**
- The exact physiological reaction (if any) uniquely catalyzed by MoaB-II. In E. coli, MoaB is dispensable; whether *P. putida* MoaB-II is redundant, conditionally required, or subfunctionalized (e.g., under specific Mo/W or substrate conditions) is untested.
- *P. putida* KT2440 encodes **no canonical MogA**, so which protein supplies the adenylated-MPT (MPT-AMP) substrate that MoeA consumes is unresolved — candidates are latent activity of a MoaB paralog or a molybdate-concentration-dependent bypass (MogA is non-essential in E. coli).
- Direct experimental data on Q88E67 (activity assays, structure, deletion phenotype, localization) — none exist; all statements are inferences.

---

## 8. Limitations and future directions

- **No primary study of Q88E67.** All functional statements rest on annotation transfer from E. coli MogA/MoaB, archaeal MoaB, and eukaryotic Cnx1/gephyrin, plus automated (ARBA/PIRNR) UniProt annotation.
- **Family functional ambiguity.** Even in E. coli the role of MoaB is unresolved; this uncertainty propagates to MoaB-II.
- **Recommended experiments:** (i) construct in-frame `PP_4600` deletion and test Moco-dependent phenotypes (nitrate reductase/chlorate resistance, molybdoenzyme activities) alone and in combination with the other *P. putida moaB/mogA* paralog(s); (ii) in vitro assays for MPT adenylyltransferase and GTPase activity of purified Q88E67; (iii) solve the structure / AlphaFold-model the pterin/nucleotide pocket and compare to MogA vs. E. coli MoaB to identify residues explaining loss of adenylyltransferase activity; (iv) test conditional requirement under Mo limitation or tungsten substitution.

---

### Key references
- Bevers et al., 2008, *Function of MoaB proteins in the biosynthesis of the molybdenum and tungsten cofactors* (PMID 18154309).
- Kozmin & Schaaper, 2013, *Genetic characterization of moaB mutants of E. coli* (PMID 23680484).
- Sanishvili et al., 2004, *Crystal structure of E. coli MoaB* (PMID 15269205).
- Bader et al., 2004, *Structure of MoaB of E. coli* (PMID 15159566).
- Stallmeyer et al., 1995, *A. thaliana cnx1...* (PMID 8528286).
- Antonyuk et al., 2009, *Structure of Mo-cofactor biosynthesis protein B (ST2315)* (PMID 20054111).
- Kuper et al., 2004, *Structure of the molybdopterin-bound Cnx1G domain* (PMID 15306815).
- Kasaragod & Schindelin, 2016, *Structural framework for metal incorporation during Moco biosynthesis* (PMID 27112598).
- Schwarz et al., 2001, *Crystal structures of human gephyrin and plant Cnx1 G domains* (PMID 11554796).
- P. putida molybdoenzyme context: PMID 26304596, 24204321, 12654012, 12023088, 12730200, 41933999.


## Artifacts

- [OpenScientist final report](moaB-II-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moaB-II-deep-research-openscientist_artifacts/final_report.pdf)