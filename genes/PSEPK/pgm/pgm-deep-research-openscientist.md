---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:16:14.125311'
end_time: '2026-08-31T13:55:16.012702'
duration_seconds: 5941.89
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pgm
  gene_symbol: pgm
  uniprot_accession: Q88GY7
  protein_description: 'RecName: Full=Phosphoglucomutase {ECO:0000256|NCBIfam:TIGR01132};
    EC=5.4.2.2 {ECO:0000256|NCBIfam:TIGR01132};'
  gene_info: Name=pgm {ECO:0000313|EMBL:AAN69179.1}; OrderedLocusNames=PP_3578 {ECO:0000313|EMBL:AAN69179.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the phosphohexose mutase family.
  protein_domains: A-D-PHexomutase_a/b/a-I. (IPR005844); A-D-PHexomutase_a/b/a-I/II/III.
    (IPR016055); A-D-PHexomutase_a/b/a-II. (IPR005845); A-D-PHexomutase_a/b/a-III.
    (IPR005846); A-D-PHexomutase_C. (IPR005843)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pgm-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pgm-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GY7
- **Protein Description:** RecName: Full=Phosphoglucomutase {ECO:0000256|NCBIfam:TIGR01132}; EC=5.4.2.2 {ECO:0000256|NCBIfam:TIGR01132};
- **Gene Information:** Name=pgm {ECO:0000313|EMBL:AAN69179.1}; OrderedLocusNames=PP_3578 {ECO:0000313|EMBL:AAN69179.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the phosphohexose mutase family.
- **Key Domains:** A-D-PHexomutase_a/b/a-I. (IPR005844); A-D-PHexomutase_a/b/a-I/II/III. (IPR016055); A-D-PHexomutase_a/b/a-II. (IPR005845); A-D-PHexomutase_a/b/a-III. (IPR005846); A-D-PHexomutase_C. (IPR005843)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pgm" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pgm' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pgm** (gene ID: pgm, UniProt: Q88GY7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Phosphoglucomutase (Pgm, PP_3578, Q88GY7) of *Pseudomonas putida* KT2440

**Gene:** *pgm* | **Locus:** PP_3578 | **UniProt:** Q88GY7 | **EC:** 5.4.2.2
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Protein family:** α-D-phosphohexomutase superfamily; phosphohexose mutase family (TIGRFAM TIGR01132)

---

## Summary

The gene **pgm** (locus tag **PP_3578**; UniProt **Q88GY7**) of *Pseudomonas putida* strain KT2440 encodes a **phosphoglucomutase (EC 5.4.2.2)**, a cytoplasmic metabolic enzyme of the **α-D-phosphohexomutase superfamily** (phosphohexose mutase family). Its primary function is to catalyze the **reversible, Mg²⁺-dependent interconversion of α-D-glucose-1-phosphate (G1P) and α-D-glucose-6-phosphate (G6P)**. This isomerization proceeds by an intramolecular phosphoryl-transfer mechanism that relies on a phosphorylated active-site serine and an obligatory **glucose-1,6-bisphosphate** reaction intermediate. Direct sequence analysis of Q88GY7 performed in this investigation confirms the diagnostic catalytic-serine motif (**Ser147**, within the conserved T-P-S-H-N-P signature) and a protein size (545 residues, 58.6 kDa) that places it firmly in the dedicated, glucose-specialized phosphoglucomutase class rather than the shorter, bifunctional AlgC/PMM-PGM class.

Functionally, Pgm sits at a **critical branch point in central carbon metabolism**. *P. putida* KT2440 catabolizes glucose predominantly through the Entner-Doudoroff pathway (in its cyclic EDEMP variant), and the resulting hexose-phosphate pool is connected, via Pgm, to the biosynthetic machinery that produces nucleotide sugars. By converting G6P (a central-metabolism intermediate) into G1P (the obligatory precursor of UDP-glucose and ADP-glucose), Pgm feeds the biosynthesis of glycogen, trehalose, lipopolysaccharide (LPS)/O-antigen, exopolysaccharides, and dTDP-L-rhamnose. In the reverse direction (G1P → G6P), the enzyme channels carbon derived from gluconeogenesis, galactose, maltose, and trehalose back into central metabolism. This bidirectional gatekeeping makes Pgm a classic **housekeeping metabolite router**.

The enzyme performs its function **in the cytoplasm**, consistent with its role as a soluble isomerase acting on charged, phosphorylated sugar intermediates that never leave the cytosol; the phosphohexomutase family carries no signal peptide or membrane-spanning features. A key clarification of this report is the distinction between Pgm — the dedicated, glucose-specific enzyme encoded by *pgm* (TIGRFAM **TIGR01132**) — and the paralogous, much-better-studied bifunctional **AlgC** enzyme of *Pseudomonas*, which supplies mannose-1-phosphate for alginate and other virulence polysaccharides. Because direct biochemical characterization of the specific PP_3578 product is limited in the primary literature, the mechanistic detail here is inferred with high confidence from closely related, structurally and kinetically characterized *Pseudomonas* phosphohexomutases and from sequence/domain conservation.

### Gene-identity verification (mandatory check)

- The gene symbol **"pgm" matches** the protein description (phosphoglucomutase, EC 5.4.2.2). ✔
- Organism confirmed as *P. putida* KT2440 (PP_3578). ✔
- Protein family/domains (α-D-phosphohexomutase domains IPR005844/5/6, IPR005843, IPR016055; TIGR01132) **align with the phosphoglucomutase/phosphohexomutase literature**. ✔
- **Disambiguation:** Pgm (PP_3578) is a *dedicated glucose-specific* phosphoglucomutase and must **not** be confused with the paralogous bifunctional **AlgC (phosphomannomutase/phosphoglucomutase, PMM/PGM)**. Much deep mechanistic literature was generated on *P. aeruginosa* AlgC; that work informs the shared superfamily mechanism, but AlgC's mannose-1-P–producing role in alginate biosynthesis is distinct from Pgm's housekeeping glucose-phosphate mutase role.

---

## Key Findings

### F001 — Pgm catalyzes the reversible interconversion of glucose-1-phosphate and glucose-6-phosphate (EC 5.4.2.2)

The core catalytic function of Pgm is the reversible isomerization **G1P ⇌ G6P**, a phosphoryl-transfer reaction that effectively relocates the phosphate group between the C1 and C6 hydroxyls of the glucose ring. This activity is directly implied by the UniProt annotation (EC 5.4.2.2, phosphoglucomutase, phosphohexose mutase family).

The reaction has been characterized in exquisite biochemical detail in the closely related *Pseudomonas* α-D-phosphohexomutase. Transient-state kinetic studies of the *P. aeruginosa* phosphomannomutase/phosphoglucomutase (PMM/PGM) demonstrate that **glucose-1,6-bisphosphate is formed as an obligatory intermediate**, and that the phosphosugar interconversion is highly reversible (Keq ~0.14 for G1P → glucose-1,6-bisP formation) ([PMID: 15865428](https://pubmed.ncbi.nlm.nih.gov/15865428/): *"The interconversion of glucose 1-phosphate and glucose 6-phosphate, catalyzed by Pseudomonas aeruginosa phosphomannomutase/phosphoglucomutase, has been studied by transient-state kinetic techniques. Glucose 1,6-bisphosphate is formed as an intermediate in the reaction"*). Purified enzyme of this family interconverts G1P and G6P with an apparent Km for G1P of ~22 µM ([PMID: 8050998](https://pubmed.ncbi.nlm.nih.gov/8050998/): *"The enzyme catalyzed the interconversion of mannose 1-phosphate (M1P) and mannose 6-phosphate, as well as that of glucose 1-phosphate (G1P) and glucose 6-phosphate."*).

Because these studies were performed on the bifunctional *P. aeruginosa* homolog, they establish the chemistry of the reaction that the dedicated Pgm carries out; the substrate specificity of PP_3578 itself is inferred from its TIGR01132 (glucose-specific) annotation and its size class (F003, F006).

### F002 — Catalytic mechanism: phosphoserine relay, Mg²⁺ dependence, and intermediate reorientation

The enzyme operates through an **intramolecular phosphoryl-transfer mechanism** anchored by a conserved active-site serine. In the resting state the enzyme is phosphorylated on this serine (Ser108 in AlgC numbering; **Ser147** in Q88GY7). Catalysis begins when the phospho-serine transfers its phosphoryl group to a hydroxyl of the incoming monophosphate substrate, generating the **bisphosphorylated intermediate (glucose-1,6-bisphosphate)** ([PMID: 12924943](https://pubmed.ncbi.nlm.nih.gov/12924943/): *"catalyzes the transfer of a phosphoryl group from serine 108 to the hydroxyl group at the 1-position of the substrate"*).

The reaction requires **Mg²⁺ for maximal activity** ([PMID: 8050998](https://pubmed.ncbi.nlm.nih.gov/8050998/): *"Purified PMM/phosphoglucomutase (PGM) required Mg2+ for maximum activity"*), reflecting the metal's role in coordinating the phosphate groups within the active site. A hallmark of the mechanism is that the bisphosphorylated intermediate must undergo a **~180° reorientation** within the active site so that the phosphate originally residing on the enzyme is presented for transfer back to the serine, completing the isomerization ([PMID: 15865428](https://pubmed.ncbi.nlm.nih.gov/15865428/): *"the glucose 1,6-bisphosphate intermediate undergoes the 180 degrees reorientation that is required for completion of the catalytic cycle"*).

Site-directed mutagenesis of several active-site residues (Arg20, Lys118, Arg247, His308, His329 in the AlgC frame) each reduced Vmax to only 4–12% of wild type, indicating that catalysis relies on an **ensemble of positively charged residues** generating a favorable electrostatic environment rather than a single classical general acid/base ([PMID: 12924943](https://pubmed.ncbi.nlm.nih.gov/12924943/)). Complementary HDX-MS and SAXS studies show that phosphorylation of the catalytic serine and ligand binding drive **large, coordinated conformational changes** across the multidomain enzyme, and that the dephosphorylated state is more flexible — a flexibility proposed to facilitate the demanding 180° reorientation of the intermediate ([PMID: 24403075](https://pubmed.ncbi.nlm.nih.gov/24403075/)). Interdomain "hot spots" identified by computational solvent mapping across open, half-open, and closed conformers reinforce this picture of a dynamic, four-domain catalytic machine ([PMID: 20589904](https://pubmed.ncbi.nlm.nih.gov/20589904/)).

### F003 — Pgm is a dedicated glucose-specific phosphoglucomutase, distinct from the bifunctional AlgC paralog

A central clarification of this investigation is that PP_3578/Pgm is a **dedicated, glucose-specialized phosphoglucomutase**, and should not be conflated with the bifunctional AlgC (PMM/PGM) enzyme that dominates the *Pseudomonas* literature. The target is annotated by **TIGRFAM TIGR01132** (PGM, α-D-glucose-phosphate-specific phosphoglucomutase; EC 5.4.2.2) and is named *pgm*, distinguishing it from the *algC*-encoded phosphomannomutase/phosphoglucomutase.

The distinction is functionally meaningful. In *P. aeruginosa*, the bifunctional AlgC accepts four substrates (G1P, G6P, mannose-1-P, and mannose-6-P) using a single active site in which the phosphate group of each substrate is held in place by a **conserved network of hydrogen bonds** ([PMID: 14725765](https://pubmed.ncbi.nlm.nih.gov/14725765/): *"High-resolution structures with glucose 1-phosphate, glucose 6-phosphate, mannose 1-phosphate, and mannose 6-phosphate show that the position of the phosphate group of each substrate is held constant by a conserved network of hydrogen bonds."*), and it shows only ~2-fold catalytic preference for G1P over M1P. By contrast, related bifunctional homologs such as *Sphingomonas* PgmG display a **~50-fold preference for glucose-1-phosphate** ([PMID: 10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/): *"Purified PgmG protein showed a marked preference for glucose-1-phosphate (G1P); the catalytic efficiency was about 50-fold higher for G1P than it was for mannose-1-phosphate (M1P)."*).

The dedicated Pgm class (TIGR01132) is specialized toward **glucose phosphosugars** and performs the housekeeping G1P/G6P interconversion rather than the mannose-1-phosphate production that feeds alginate biosynthesis. This specialization is corroborated at the sequence level by the size class of Q88GY7 (F006).

### F004 — Pathway role: linking Entner-Doudoroff central metabolism to nucleotide-sugar and polysaccharide biosynthesis

Pgm occupies the **G1P/G6P node** that bridges catabolic and biosynthetic carbon flux. *P. putida* KT2440 catabolizes glucose primarily through the **Entner-Doudoroff pathway** (in the cyclic EDEMP variant that recycles trioses back to hexose-phosphates) ([PMID: 39837196](https://pubmed.ncbi.nlm.nih.gov/39837196/): *"While all three primarily use the Entner-Doudoroff pathway for glucose metabolism"*). This central metabolism converges on the hexose-phosphate pool, of which G6P is a member.

Phosphoglucomutase interconverts G6P with **G1P, the obligatory precursor of UDP-glucose and ADP-glucose**, and therefore the gateway to glycogen, trehalose, LPS/O-antigen, exopolysaccharides, and dTDP-L-rhamnose. In *Pseudomonas*, the analogous G6P → G1P step is the entry point to the dTDP-L-rhamnose pathway and to the biosynthesis of alginate, LPS, and rhamnolipid, as demonstrated for AlgC ([PMID: 10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/): *"the conversion of glucose-6-phosphate to glucose-1-phosphate"*). Operating in the **reverse (G1P → G6P) direction**, Pgm channels gluconeogenic carbon and carbon derived from galactose, maltose, and trehalose degradation back into central metabolism — for example, maltodextrin phosphorylase produces G1P from maltodextrins, which phosphoglucomutase then converts to G6P for entry into glycolytic/ED flux ([PMID: 10348846](https://pubmed.ncbi.nlm.nih.gov/10348846/)).

This positioning is highly relevant to *P. putida* biotechnology: rhamnolipid production in engineered KT2440 depends on the supply of dTDP-L-rhamnose, whose precursor G1P is produced by phosphoglucomutase activity ([PMID: 41672327](https://pubmed.ncbi.nlm.nih.gov/41672327/)).

### F005 — A cytoplasmic housekeeping enzyme coupled to glycogen metabolism and gluconeogenic flux

Multiple lines of comparative genomics and physiology indicate that Pgm is a **cytoplasmic housekeeping enzyme tied to carbon-storage metabolism**. In diverse bacteria, the dedicated *pgm* gene is embedded within or adjacent to the **glycogen biosynthesis operon**. In *Agrobacterium tumefaciens* and *Rhizobium tropici*, the *glgP-glgB-glgC-glgA-pgm* operon co-transcribes phosphoglucomutase with glycogen phosphorylase, branching enzyme, ADP-glucose pyrophosphorylase, and glycogen synthase, such that the G1P produced by Pgm supplies **ADP-glucose pyrophosphorylase (GlgC)** for glycogen synthesis ([PMID: 11208782](https://pubmed.ncbi.nlm.nih.gov/11208782/): *"phosphoglucomutase (pgm), and glycogen debranching enzyme (glgX)"*; see also [PMID: 9851999](https://pubmed.ncbi.nlm.nih.gov/9851999/) for the *A. tumefaciens glg* operon organization).

Regulatory data reinforce the storage/gluconeogenic role. In *Escherichia coli*, phosphoglucomutase activity is co-regulated with the gluconeogenic enzymes fructose-1,6-bisphosphatase and PEP synthetase, all under negative control of the global regulator **csrA**, and peaks in early stationary phase alongside glycogen accumulation ([PMID: 7493933](https://pubmed.ncbi.nlm.nih.gov/7493933/): *"Phosphoglucomutase and the gluconeogenic enzymes fructose-1,6-bisphosphatase and phosphoenolpyruvate synthetase were found to be under the negative control of csrA"*). As a soluble metabolic isomerase acting on phosphorylated sugar intermediates, Pgm functions in the **cytoplasm**; the phosphohexomutase family carries no signal peptide or membrane-spanning segment.

### F006 — Sequence analysis of Q88GY7 confirms the catalytic serine and the dedicated-Pgm size class

Direct retrieval and inspection of the UniProt Q88GY7 sequence provide the strongest target-specific evidence in this investigation. The protein is **545 residues long (58.6 kDa)** and contains the diagnostic α-D-phosphohexomutase catalytic-serine motif `...GIVITPSHNPP...`, with the conserved phosphoryl-accepting serine at **Ser147** (the S within the T-P-**S**-H-N-P signature). It also carries the N-terminal domain-1 `TSGHRGSS` motif (~residues 44–51) that contributes to the metal- and phosphate-coordinating active site.

The **545 aa / 58.6 kDa** size matches the *E. coli*-type dedicated phosphoglucomutase class (~545–560 aa) rather than the shorter bifunctional AlgC/PMM-PGM class (~460 aa / ~50 kDa). This size-class distinction independently supports the conclusion of F003 that PP_3578 is a dedicated, glucose-specific phosphoglucomutase rather than a bifunctional PMM/PGM enzyme, and confirms at the sequence level for this specific protein that the phospho-serine relay mechanism applies to Pgm.

---

## Mechanistic Model / Interpretation

Bringing the findings together, Pgm is a soluble, Mg²⁺-dependent isomerase that acts as a reversible router between the central hexose-phosphate pool and sugar-nucleotide biosynthesis.

### Reaction and catalytic cycle

```
                 Mg2+                             Mg2+
   G1P  +  E-Ser147-P  ⇌  E-Ser147 · [Glucose-1,6-bisP]  ⇌  E-Ser147-P  +  G6P
                              |  180° reorientation  |
                              +----------------------+
   (phospho-enzyme)     (dephospho-enzyme + bisphosphate intermediate)   (phospho-enzyme)
```

1. The resting enzyme is phosphorylated on **Ser147**.
2. Substrate (G1P or G6P) binds; the serine phosphate is transferred to the free hydroxyl, producing enzyme-bound **glucose-1,6-bisphosphate** and the transiently **dephosphorylated** enzyme.
3. The bisphosphate intermediate **reorients ~180°** in the active site (facilitated by the increased flexibility of the dephospho-enzyme).
4. The phosphate now positioned toward the serine is transferred back, re-phosphorylating the enzyme and releasing the isomerized product (G6P or G1P).

Mg²⁺ and a constellation of positively charged active-site residues stabilize the phosphate groups and the transition states throughout the cycle.

### Metabolic position

```
      Glucose
        |  (ED / EDEMP pathway, cyclic)
        v
   ┌─────────────────────────────────────────────┐
   │   Central hexose-phosphate pool  (G6P) <──── gluconeogenesis,
   │                 ^                              maltose/trehalose/galactose
   │                 │                              catabolism (via G1P)
   │            Pgm  │  (EC 5.4.2.2, reversible)
   │                 v
   │               (G1P)
   └─────────────────┬───────────────────────────┘
                     │
        ┌────────────┼─────────────┬───────────────┐
        v            v             v               v
   UDP-glucose   ADP-glucose   dTDP-L-rhamnose   (LPS / O-antigen,
   (trehalose,   (glycogen)    (rhamnolipid,      exopolysaccharide)
   glucosylation)              O-antigen)
```

In the **forward (G6P → G1P)** direction, Pgm feeds anabolism: G1P is the committed precursor for UDP-glucose (glycogen/trehalose glucosyl donation and glucosylation reactions), ADP-glucose (glycogen), and — via dTDP-glucose — dTDP-L-rhamnose used in rhamnolipid and O-antigen biosynthesis. In the **reverse (G1P → G6P)** direction, Pgm reclaims carbon entering as G1P from storage-polymer breakdown and from disaccharide/monosaccharide catabolism, routing it into the Entner-Doudoroff/EDEMP machinery. This bidirectional gatekeeping is the essence of its housekeeping role, and its co-regulation with gluconeogenic enzymes and its genetic linkage to *glg* operons in other bacteria reflect the same underlying logic. Importantly, this is a **precise, non-pleiotropic biochemical role** even though the downstream products (glycogen, trehalose, LPS, EPS, rhamnolipid) are diverse.

### Distinction from AlgC

| Feature | Dedicated Pgm (PP_3578, Q88GY7) | Bifunctional AlgC (PMM/PGM) |
|---|---|---|
| Gene | *pgm* | *algC* |
| TIGRFAM | TIGR01132 (glucose-specific PGM) | — (PMM/PGM) |
| Preferred substrates | Glucose phosphosugars (G1P/G6P) | G1P, G6P, M1P, M6P (4 substrates) |
| Length / mass | ~545 aa / 58.6 kDa | ~460 aa / ~50 kDa |
| Catalytic serine | Ser147 (T-P-S-H-N-P) | Ser108 |
| Primary metabolic role | Housekeeping G1P/G6P interconversion; nucleotide-sugar + glycogen supply | Mannose-1-P supply for alginate; also G1P for LPS/rhamnolipid |

The great majority of the deep biochemical and structural characterization in the *Pseudomonas* literature was performed on the AlgC-type enzyme; the mechanistic conclusions (phosphoserine relay, Mg²⁺ dependence, bisphosphate intermediate, conformational dynamics) transfer to Pgm by virtue of shared active-site architecture, while the substrate-specificity conclusion (glucose-specialized) is what separates the two classes.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [15865428](https://pubmed.ncbi.nlm.nih.gov/15865428/) | Formation and reorientation of glucose-1,6-bisphosphate in the PMM/PGM reaction | Establishes G1P⇌G6P interconversion, the glucose-1,6-bisphosphate intermediate, and its 180° reorientation (F001, F002) |
| [8050998](https://pubmed.ncbi.nlm.nih.gov/8050998/) | Purification/characterization of PMM/PGM from *P. aeruginosa* | Confirms G1P/G6P (and M1P/M6P) interconversion, Km~22 µM for G1P, and Mg²⁺ requirement (F001, F002) |
| [12924943](https://pubmed.ncbi.nlm.nih.gov/12924943/) | Roles of active-site residues in *P. aeruginosa* PMM/PGM | Documents phosphoserine → substrate phosphoryl transfer; residue-ensemble catalysis (F002) |
| [14725765](https://pubmed.ncbi.nlm.nih.gov/14725765/) | Structural basis of diverse substrate recognition by PMM/PGM | Shows multi-substrate breadth of bifunctional AlgC, contrasting with glucose-specialized Pgm (F003) |
| [10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/) | Identification of *pgmG* in *Sphingomonas paucimobilis* | ~50-fold G1P preference illustrating glucose specialization in the family (F003) |
| [39837196](https://pubmed.ncbi.nlm.nih.gov/39837196/) | Comparing industrial cell factories incl. *P. putida* KT2440 | Confirms Entner-Doudoroff glucose catabolism context for Pgm's node (F004) |
| [10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/) | *P. aeruginosa* AlgC participates in rhamnolipid biosynthesis | Identifies G6P→G1P as entry to nucleotide-sugar/polysaccharide biosynthesis (F004) |
| [10348846](https://pubmed.ncbi.nlm.nih.gov/10348846/) | Maltose metabolism in *Thermococcus litoralis* | Illustrates G1P from maltodextrin phosphorylase feeding PGM into central metabolism (F004) |
| [41672327](https://pubmed.ncbi.nlm.nih.gov/41672327/) | Rhamnolipid production in engineered *P. putida* | Biotechnological relevance of G1P/dTDP-rhamnose supply (F004) |
| [11208782](https://pubmed.ncbi.nlm.nih.gov/11208782/) | *Rhizobium tropici* glycogen synthase mutants | Shows *pgm* within the glycogen (*glg*) operon coupling G1P to glycogen (F005) |
| [9851999](https://pubmed.ncbi.nlm.nih.gov/9851999/) | *A. tumefaciens glg* operon organization | *glgPBCA-pgm* single operon; genetic linkage of *pgm* to glycogen metabolism (F005) |
| [7493933](https://pubmed.ncbi.nlm.nih.gov/7493933/) | Pleiotropic regulation via *csrA* in *E. coli* | Co-regulation of PGM with gluconeogenesis/glycogen — housekeeping role (F005) |
| [24403075](https://pubmed.ncbi.nlm.nih.gov/24403075/) | Dephosphorylation promotes enzyme flexibility (HDX-MS/SAXS) | Conformational dynamics coupling flexibility to intermediate reorientation (F002) |
| [20589904](https://pubmed.ncbi.nlm.nih.gov/20589904/) | Domain motion and interdomain hot spots in PMM/PGM | Multidomain conformational changes underpinning catalysis (F002) |
| [11716469](https://pubmed.ncbi.nlm.nih.gov/11716469/) | Kinetic mechanism and pH dependence of PMM/PGM | Bisphosphorylated-intermediate reorientation, general acid/base pK analysis (F002) |

**Note on evidence provenance:** The deepest mechanistic and structural evidence (PMIDs 15865428, 8050998, 12924943, 14725765, 24403075, 20589904, 11716469) derives from the *P. aeruginosa* bifunctional AlgC (PMM/PGM) enzyme or from other family homologs, not from direct study of PP_3578. These are used as strong homology-based inference. The most target-specific evidence is the direct sequence analysis of Q88GY7 (F006) and the UniProt/TIGRFAM annotations (F001, F003).

---

## Supported and Refuted Hypotheses

**Supported:**

- **H1** — Pgm catalyzes reversible G1P ⇌ G6P interconversion (EC 5.4.2.2). ✔ (annotation + kinetic/structural literature on the family)
- **H2** — Mechanism uses a phospho-serine (Ser147) and a glucose-1,6-bisphosphate intermediate, and is Mg²⁺-dependent. ✔
- **H3** — Pgm is glucose-specific and distinct from the bifunctional AlgC (PMM/PGM). ✔ (TIGR01132 annotation + 545 aa / 58.6 kDa size class)
- **H4** — Pgm is cytoplasmic and functions as a hub linking central carbon metabolism to nucleotide-sugar/glycogen biosynthesis and gluconeogenesis. ✔

**Refuted / ruled out:**

- Pgm is **not** the mannose-1-P–producing enzyme of alginate biosynthesis (that role belongs to AlgC); its physiologically defining activity is the glucose-phosphate mutase reaction.
- No evidence supports a signaling, catabolic-transporter, or extracytoplasmic role.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of PP_3578.** No published purification, kinetic, or structural study of the *P. putida* KT2440 Pgm (Q88GY7) specifically was located. The reaction chemistry, mechanism, Mg²⁺ dependence, and intermediate are inferred (with high confidence) from closely related *Pseudomonas* and family homologs. Km, kcat, and substrate-specificity constants for the actual PP_3578 gene product remain to be measured.

2. **Substrate-specificity inference.** The conclusion that Pgm is glucose-specialized rests on TIGRFAM classification (TIGR01132), the protein size class, and analogy to dedicated PGMs — not on a measured G1P-vs-M1P specificity ratio for PP_3578. Minor secondary activity on other phosphohexoses cannot be formally excluded.

3. **Localization inferred, not demonstrated.** Cytoplasmic localization is inferred from the absence of signal peptide/transmembrane features and from the nature of the substrates. No experimental subcellular fractionation or imaging for PP_3578 is cited.

4. **Genetic context in *P. putida* not resolved.** While *pgm* is embedded in *glg* operons in *Agrobacterium* and *Rhizobium*, the operon context and regulation of PP_3578 in KT2440 specifically (e.g., relationship to *glg* genes, GnuR, or csrA-like control) were not directly established here.

5. **Physiological essentiality / phenotype unknown.** Whether *pgm* deletion in *P. putida* KT2440 impairs growth on gluconeogenic substrates, glycogen accumulation, LPS/O-antigen synthesis, or rhamnolipid production was not experimentally verified in the literature reviewed.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and kinetic characterization of PP_3578.** Clone, express, and purify Q88GY7; measure Km/kcat for G1P and G6P and assay activity on mannose-1-P/mannose-6-P to quantify the glucose-vs-mannose specificity ratio and confirm the dedicated-Pgm classification directly.

2. **Active-site mutagenesis of Ser147.** Construct an S147A variant to confirm that Ser147 is the catalytic phosphoryl-accepting residue predicted from the T-P-S-H-N-P motif, and verify loss of activity.

3. **Structural determination.** Solve a crystal structure (or generate a validated AlphaFold model) of PP_3578, ideally with G1P/G6P and glucose-1,6-bisphosphate bound, to confirm the four-domain architecture and the phosphate-coordination network relative to AlgC.

4. **Gene-deletion phenotyping in KT2440.** Generate a Δ*pgm* (ΔPP_3578) mutant and test growth on glucose vs. gluconeogenic and G1P-generating substrates (maltose, trehalose, galactose), plus glycogen content, LPS/O-antigen profile, and rhamnolipid titer, to establish the in vivo pathway role and any essentiality.

5. **Operon/regulation mapping.** Use RNA-seq/RT-PCR to determine the *pgm* transcriptional unit and its regulation in KT2440 (e.g., response to carbon source, relationship to glucose/gluconate regulators such as GnuR), clarifying how flux through the G1P/G6P node is controlled.

6. **¹³C metabolic flux analysis.** Quantify the directionality and magnitude of flux through the Pgm node under glucose (catabolic) vs. gluconeogenic conditions to define its physiological set-point in central carbon metabolism.

---

## Conclusion

The *pgm* gene (PP_3578, Q88GY7) of *Pseudomonas putida* KT2440 encodes a **cytoplasmic, Mg²⁺-dependent phosphoglucomutase (EC 5.4.2.2)** of the α-D-phosphohexomutase superfamily that reversibly interconverts glucose-1-phosphate and glucose-6-phosphate via a phospho-Ser147 relay and an obligatory glucose-1,6-bisphosphate intermediate. It is a **glucose-specialized, dedicated enzyme (TIGR01132), distinct from the bifunctional AlgC (PMM/PGM)**, and it functions at the **G1P/G6P branch point** that couples Entner-Doudoroff central carbon metabolism to nucleotide-sugar-dependent biosynthesis (UDP-/ADP-glucose for glycogen, trehalose, LPS/O-antigen, exopolysaccharides, and dTDP-L-rhamnose) while also reclaiming gluconeogenic and storage-derived carbon back into the central hexose-phosphate pool. Its mechanism and structural dynamics are established with high confidence by homology to well-characterized *Pseudomonas* family members, while direct biochemical characterization of the specific PP_3578 gene product remains an open experimental target.


## Artifacts

- [OpenScientist final report](pgm-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pgm-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15865428
2. PMID:8050998
3. PMID:12924943
4. PMID:24403075
5. PMID:20589904
6. PMID:14725765
7. PMID:10788412
8. PMID:39837196
9. PMID:10481091
10. PMID:10348846
11. PMID:41672327
12. PMID:11208782
13. PMID:9851999
14. PMID:7493933