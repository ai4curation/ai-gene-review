---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:16:20.804179'
end_time: '2026-08-31T13:44:18.010742'
duration_seconds: 5277.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: algC
  gene_symbol: algC
  uniprot_accession: Q88C93
  protein_description: 'RecName: Full=Phosphomannomutase/phosphoglucomutase; Short=PMM
    / PGM; EC=5.4.2.2; EC=5.4.2.8;'
  gene_info: Name=algC; OrderedLocusNames=PP_5288;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the phosphohexose mutase family. .
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: algC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: algC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C93
- **Protein Description:** RecName: Full=Phosphomannomutase/phosphoglucomutase; Short=PMM / PGM; EC=5.4.2.2; EC=5.4.2.8;
- **Gene Information:** Name=algC; OrderedLocusNames=PP_5288;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the phosphohexose mutase family. .
- **Key Domains:** A-D-PHexomutase_a/b/a-I. (IPR005844); A-D-PHexomutase_a/b/a-I/II/III. (IPR016055); A-D-PHexomutase_a/b/a-II. (IPR005845); A-D-PHexomutase_a/b/a-III. (IPR005846); A-D-PHexomutase_C. (IPR005843)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "algC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'algC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **algC** (gene ID: algC, UniProt: Q88C93) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AlgC (Q88C93 / PP_5288) — Functional Annotation Report

**Gene:** *algC* · **Ordered locus:** PP_5288 · **UniProt:** Q88C93
**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
**Enzyme:** Phosphomannomutase / phosphoglucomutase (PMM/PGM) · **EC 5.4.2.8 / EC 5.4.2.2**
**Superfamily:** α‑D‑phosphohexomutase (phosphohexose mutase family)

---

## Summary

**AlgC of *Pseudomonas putida* KT2440 is a soluble, cytoplasmic, bifunctional phosphomannomutase/phosphoglucomutase (PMM/PGM) of the α‑D‑phosphohexomutase superfamily.** Its primary biochemical function is the reversible, Mg²⁺‑dependent intramolecular transfer of a phosphoryl group across a hexose sugar, interconverting the 6‑phosphate and 1‑phosphate forms of two substrates: glucose‑6‑phosphate ⇌ glucose‑1‑phosphate (PGM activity, EC 5.4.2.2) and mannose‑6‑phosphate ⇌ mannose‑1‑phosphate (PMM activity, EC 5.4.2.8). A single active‑site "hot spot" accommodates both the glucose and the mannose phosphosugars, which is the structural basis of the enzyme's dual specificity. This identity is directly consistent with the UniProt annotation for Q88C93 and is corroborated by direct enzymatic assays of AlgC orthologs across multiple gammaproteobacteria and other lineages.

**The reaction proceeds by a distinctive, well‑characterized processive mechanism.** A conserved catalytic serine (Ser108 in the closely studied *P. aeruginosa* ortholog) exists as a phosphoserine and serves as both the phosphoryl donor and acceptor. Catalysis requires two sequential phosphoryl transfers separated by a 180° reorientation of a glucose‑1,6‑bisphosphate (or mannose‑1,6‑bisphosphate) intermediate that remains bound in the active site — a textbook example of enzymatic processivity. A conserved histidine (His329) acts as the general base that deprotonates the sugar hydroxyl, and a mobile C‑terminal domain (domain 4) closes over the deep catalytic cleft to complete an efficient active site. Dephosphorylation of the catalytic serine during the cycle increases enzyme flexibility, which is thought to facilitate the intermediate's reorientation.

**Biologically, AlgC is a central upstream supplier of activated‑sugar (nucleotide‑sugar) precursors.** Its 1‑phosphate products are converted to GDP‑mannose (from mannose‑1‑phosphate), UDP‑glucose (from glucose‑1‑phosphate), and dTDP‑L‑rhamnose, feeding the biosynthesis of alginate, the lipopolysaccharide (LPS) core/O‑antigen, and rhamnolipid. Because it sits at this metabolic branch point, loss of AlgC simultaneously abolishes several glycoconjugate pathways. In the soil bacterium *P. putida* KT2440 specifically — which, unlike *P. aeruginosa*, encodes a stand‑alone cytoplasmic enzyme without an N‑terminal periplasmic sensor domain — AlgC's ecologically most prominent role is provisioning **alginate**, an exopolysaccharide induced by matric (water‑limitation) stress that creates a hydrated biofilm microenvironment and confers desiccation tolerance.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks were confirmed:

| Check | Result |
|---|---|
| Gene symbol *algC* matches protein description | **Yes** — *algC* is the canonical name for bacterial PMM/PGM |
| Organism correct (*P. putida* KT2440) | **Yes** — locus PP_5288, UniProt Q88C93 |
| Protein family/domains align with literature | **Yes** — α‑D‑phosphohexomutase superfamily (IPR005843–46, IPR016055) |
| Literature refers to the same enzyme | **Yes** — extensive, directly relevant primary literature |

The gene symbol is **not** ambiguous in this case. AlgC is well characterized, and although the deepest mechanistic and structural work was performed on the *P. aeruginosa* ortholog, that protein is the direct functional homolog of *P. putida* AlgC (same superfamily, same reaction, conserved active‑site residues). Where *P. putida*‑specific data exist (localization/domain architecture, alginate physiology), they are cited explicitly.

---

## Key Findings

### F001 — AlgC is a bifunctional PMM/PGM of the α‑D‑phosphohexomutase superfamily

UniProt Q88C93 annotates PP_5288/*algC* as a phosphomannomutase/phosphoglucomutase carrying two EC activities, EC 5.4.2.8 (PMM) and EC 5.4.2.2 (PGM), and assigns it to the phosphohexose mutase family with the four signature α‑D‑phosphohexomutase domains (IPR005844/45/46, IPR005843, IPR016055). This annotation is not merely computational: multiple orthologs are experimentally confirmed to be bifunctional. In *P. aeruginosa*, "the *algC* gene … is involved in alginate production through its phosphomannomutase activity and in LPS synthesis through its phosphoglucomutase activity" ([PMID: 10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/)). The *Stenotrophomonas maltophilia* ortholog SpgM "was shown to encode a bifunctional enzyme with both PGM and phosphomannomutase activities" ([PMID: 12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/)). Further homologs — *Sphingomonas paucimobilis* PgmG ([PMID: 10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/)) and *Prochlorothrix hollandica* PmmA, which is 37% identical to AlgC and possesses "both PGM and PMM activities as judged by both enzyme assays and complementation analysis" ([PMID: 8765122](https://pubmed.ncbi.nlm.nih.gov/8765122/)) — confirm that bifunctionality is a conserved family trait. Evolutionary‑trace analysis of 71 superfamily members demonstrated that "key residues in the active site, including many of those involved in substrate contacts … are conserved throughout the enzyme family" ([PMID: 15238632](https://pubmed.ncbi.nlm.nih.gov/15238632/)), placing AlgC firmly within a superfamily that shares a conserved catalytic apparatus.

### F002 — A processive mechanism via a reorienting glucose‑1,6‑bisphosphate intermediate

The catalytic mechanism has been resolved in structural and kinetic detail in the *P. aeruginosa* ortholog. "The reaction entails two phosphoryl transfers, with an intervening 180° reorientation of the reaction intermediate (e.g. glucose 1,6‑bisphosphate) during catalysis" ([PMID: 16595672](https://pubmed.ncbi.nlm.nih.gov/16595672/)). Critically, this reorientation happens "without dissociation from the active site of the enzyme and is, thus, a simple example of processivity" ([PMID: 16595672](https://pubmed.ncbi.nlm.nih.gov/16595672/)). Transient‑state kinetic studies confirmed that "glucose 1,6‑bisphosphate is formed as an intermediate in the reaction" and behaves as an obligatory enzyme‑bound species, partitioning forward to product roughly 14‑fold more often than it dissociates ([PMID: 15865428](https://pubmed.ncbi.nlm.nih.gov/15865428/)). Site‑directed mutagenesis identified active‑site residues that are critical for retaining the bisphosphate during its reorientation ([PMID: 16595672](https://pubmed.ncbi.nlm.nih.gov/16595672/)). This mechanism is why the enzyme is often used as a model of "simple processivity."

### F003 — AlgC is a central cytoplasmic supplier of nucleotide‑sugar precursors

AlgC sits at the top of several glycoconjugate biosynthetic pathways. Its PMM activity (mannose‑6‑P → mannose‑1‑P) feeds GDP‑mannose synthesis for **alginate**, while its PGM activity (glucose‑6‑P → glucose‑1‑P) feeds UDP‑glucose for the **LPS core** and dTDP‑L‑rhamnose for **rhamnolipid**. In *P. aeruginosa*, "the AlgC protein plays a central role in the production of the three … virulence‑associated saccharides: alginate, LPS and rhamnolipid" ([PMID: 10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/)). Genetic evidence shows that "the *P. aeruginosa algC* gene is required for biosynthesis of alginate and lipopolysaccharide" ([PMID: 7558335](https://pubmed.ncbi.nlm.nih.gov/7558335/)). Substrate specificity of an AlgC ortholog was quantified in *Sphingomonas* PgmG: "the catalytic efficiency was about 50‑fold higher for G1P than it was for mannose‑1‑phosphate (M1P). The estimated apparent Kₘ values for G1P and M1P were … 0.33 and 1.27 mM" ([PMID: 10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/)), indicating a kinetic preference for the glucose substrate. In *P. putida* KT2440, "alginate, an exopolysaccharide (EPS) produced by *P. putida*, is known to create hydrated environments and alleviate the effect of water limitation" ([PMID: 24912454](https://pubmed.ncbi.nlm.nih.gov/24912454/)) — a downstream AlgC‑dependent product — while alginate and other EPS also stabilize KT2440 biofilms ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)).

| AlgC product | Activated to | Feeds pathway | Cellular product |
|---|---|---|---|
| Mannose‑1‑phosphate | GDP‑mannose | Alginate biosynthesis | Alginate EPS |
| Glucose‑1‑phosphate | UDP‑glucose | LPS core assembly | Complete LPS core / O‑antigen |
| Glucose‑1‑phosphate | dTDP‑L‑rhamnose | Rhamnolipid biosynthesis | Rhamnolipid (biosurfactant) |

### F004 — *P. putida* AlgC is a stand‑alone cytoplasmic enzyme lacking the periplasmic sensor domain

A key organism‑specific distinction: some gammaproteobacterial AlgC‑type PMMs carry a ~200‑amino‑acid N‑terminal periplasmic dCache sensor domain anchored by two transmembrane segments. Qian, Fei & Galperin found that these "previously overlooked N‑terminal periplasmic sensor domains were detected in the well‑characterized PMMs of *Pseudomonas aeruginosa* and *Xanthomonas campestris*, albeit **not in the enzymes from *Pseudomonas fluorescens*, *Pseudomonas putida* or *Azotobacter vinelandii***" ([PMID: 30938049](https://pubmed.ncbi.nlm.nih.gov/30938049/)). This directly establishes that *P. putida* AlgC is the stand‑alone, soluble PMM/PGM enzymatic module — a **cytoplasmic** protein — without the membrane anchor or extracytoplasmic sensor found in some relatives. Consequently, while mechanistic inferences from the *P. aeruginosa* ortholog's catalytic core transfer directly to *P. putida* AlgC, the regulatory/sensory features associated with the membrane‑bound form (e.g., the requirement of the membrane‑bound form for twitching motility in *Lysobacter enzymogenes*) do not apply to the KT2440 enzyme.

### F005 — Direct assays confirm both PMM and PGM activity and a requirement for a complete LPS core

The most direct experimental proof that a single AlgC polypeptide carries both activities comes from Coyne et al. Genetically defined *P. aeruginosa algC* mutants "had no detectable phosphomannomutase activity and … neither *algC* strain had detectable phosphoglucomutase (PGM) activity" ([PMID: 7515870](https://pubmed.ncbi.nlm.nih.gov/7515870/)), and the cloned intact *algC* gene complemented an *E. coli pgm* mutant — showing that one enzyme provides both activities. Functionally, the "algC mutants of a serotype O5 strain (PAO1) and a serotype O3 strain (PAC1R) did not express lipopolysaccharide (LPS) O side chains or the A‑band (common antigen) polysaccharide," and their LPS migrated like glucose‑deficient rough mutants ([PMID: 7515870](https://pubmed.ncbi.nlm.nih.gov/7515870/)), demonstrating that "the synthesis of glucose 1‑phosphate is necessary in the biosynthesis of the *P. aeruginosa* LPS core" ([PMID: 7515870](https://pubmed.ncbi.nlm.nih.gov/7515870/)). This is direct enzymatic + genetic‑complementation evidence, superseding pure sequence inference.

### F006 — In *P. putida*, AlgC‑dependent alginate is induced by matric water stress and confers desiccation tolerance

The ecological role of AlgC's output in *P. putida* has been defined physiologically. Chang et al. showed that "total exopolysaccharide (EPS) and alginate production increased with increasing matric, but not solute, stress severity" ([PMID: 17601783](https://pubmed.ncbi.nlm.nih.gov/17601783/)), and that "alginate deficiency decreased survival of desiccation not only by *P. putida* but also by *Pseudomonas aeruginosa* PAO1 and *Pseudomonas syringae* pv. *syringae* B728a" ([PMID: 17601783](https://pubmed.ncbi.nlm.nih.gov/17601783/)). Independent matric‑stress‑controlled gene screens in *P. putida* recovered alginate‑biosynthesis and cell‑envelope genes as contributors to desiccation tolerance ([PMID: 15101980](https://pubmed.ncbi.nlm.nih.gov/15101980/)), and alginate acts as a biofilm structural stabilizer alongside other KT2440 EPS systems ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)). Because alginate synthesis depends on GDP‑mannose derived from the mannose‑1‑phosphate that AlgC produces, AlgC is the essential upstream metabolic gateway to this protective response.

### F007 — Atomic mechanism: phosphoserine Ser108, general base His329, and a closing C‑terminal domain

Structural and mutational studies of the *P. aeruginosa* ortholog complete the atomic picture. The conserved catalytic serine acts as both phosphoryl donor and acceptor: "the S108C substitution of the phosphoryl donor and acceptor slowed transformation of the glucose 1‑phosphate substrate by impairing kcat" ([PMID: 22242625](https://pubmed.ncbi.nlm.nih.gov/22242625/)). The serine's phosphorylation state governs enzyme compactness and flexibility — dephosphorylation makes the enzyme "less compact in solution," and increased flexibility is proposed to facilitate reorientation of the reaction intermediate ([PMID: 24403075](https://pubmed.ncbi.nlm.nih.gov/24403075/)). A histidine general base was identified: "a histidine (His329) in the active site is critical for enzyme activity in a well‑studied member of the superfamily, phosphomannomutase/phosphoglucomutase from *Pseudomonas aeruginosa*" ([PMID: 23517223](https://pubmed.ncbi.nlm.nih.gov/23517223/)), positioned to abstract a proton from the O1/O6 hydroxyl of the phosphosugar (a structurally analogous lysine performs this role in the PGM subgroup). The enzyme's four‑domain architecture includes a mobile C‑terminal domain 4 that closes over the catalytic cleft and is required for full catalytic efficiency ([PMID: 23893395](https://pubmed.ncbi.nlm.nih.gov/23893395/), [PMID: 20512975](https://pubmed.ncbi.nlm.nih.gov/20512975/), [PMID: 20589904](https://pubmed.ncbi.nlm.nih.gov/20589904/)). A single active‑site hot spot underlies bifunctionality: "one of the most important hot spots is in the active site, consistent with the ability of the enzyme to bind both glucose and mannose phosphosugar substrates" ([PMID: 20589904](https://pubmed.ncbi.nlm.nih.gov/20589904/)).

---

## Mechanistic Model / Interpretation

### The catalytic cycle

```
   Substrate: glucose-6-P (or mannose-6-P)
        │
        ▼
  ┌─────────────────────────────────────────────────────────┐
  │  Enzyme-Ser108-phosphate  (phosphoenzyme, Mg2+ bound)    │
  │                                                          │
  │  STEP 1: phosphoryl transfer from P-Ser108 to sugar 1-OH │
  │          → glucose-1,6-bisphosphate  (bound intermediate)│
  │          Enzyme now dephosphorylated → more flexible     │
  │                                                          │
  │  STEP 2: 180° REORIENTATION of the bisphosphate          │
  │          intermediate WITHIN the active site (processive)│
  │          His329 general base positions/deprotonates OH   │
  │                                                          │
  │  STEP 3: phosphoryl transfer from sugar 6-P back to Ser108│
  │          → regenerates P-Ser108 phosphoenzyme            │
  └─────────────────────────────────────────────────────────┘
        │
        ▼
   Product: glucose-1-P (or mannose-1-P)
        (C-terminal domain 4 closes over cleft during turnover)
```

The elegance of this system is that a **single** catalytic serine performs two phosphoryl transfers on opposite ends of the sugar, requiring the bisphosphate intermediate to flip 180° between steps. The enzyme holds the intermediate throughout (processivity), and modulates its own conformational flexibility through the phosphorylation state of Ser108 to permit the reorientation. His329 provides the general‑base chemistry; a Mg²⁺ ion coordinates the phosphoryl groups.

### From reaction to biology: the metabolic branch point

```
        Fructose-6-P
        /          \
   (PMI)            (glycolysis)
      │
  Mannose-6-P                Glucose-6-P
      │  ⇅ AlgC (PMM)            │  ⇅ AlgC (PGM)
  Mannose-1-P                Glucose-1-P
      │                      /          \
   GDP-mannose         UDP-glucose    dTDP-L-rhamnose
      │                     │               │
   ALGINATE            LPS CORE /        RHAMNOLIPID
  (desiccation,        O-ANTIGEN        (biosurfactant)
   biofilm EPS)
```

AlgC is the shared node feeding all of these. This explains why *algC* loss is pleiotropic (alginate⁻, LPS⁻, rhamnolipid⁻ simultaneously) yet the **primary molecular function** is singular and precise: a sugar‑phosphate mutase. In *P. putida* KT2440, the branch of greatest ecological consequence is the alginate branch, because alginate production is triggered by water/matric stress and protects the soil bacterium against desiccation.

### Localization

All evidence points to a **cytoplasmic** site of action: the substrates (hexose‑6/1‑phosphates) and downstream nucleotide‑sugar synthesis are cytoplasmic processes, and the *P. putida* enzyme specifically lacks the membrane anchor / periplasmic sensor domain present in some orthologs ([PMID: 30938049](https://pubmed.ncbi.nlm.nih.gov/30938049/)). AlgC therefore performs its catalytic function in the cytosol, upstream of the membrane‑associated polymerization/export machineries that build alginate, LPS, and rhamnolipid.

---

## Evidence Base

| PMID | Study focus | How it supports the findings |
|---|---|---|
| [10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/) | *P. aeruginosa* AlgC in rhamnolipid biosynthesis | Establishes bifunctional PMM/PGM roles and central supply of alginate/LPS/rhamnolipid precursors (F001, F003) |
| [7515870](https://pubmed.ncbi.nlm.nih.gov/7515870/) | *algC* encodes PGM; LPS core | Direct enzymatic proof of both activities; glucose‑1‑P required for LPS core (F005) |
| [7558335](https://pubmed.ncbi.nlm.nih.gov/7558335/) | Avirulence of *algC* mutant | Genetic requirement of AlgC for alginate + LPS (F003) |
| [12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/) | *S. maltophilia* SpgM | Ortholog confirmed bifunctional; LPS/virulence role (F001) |
| [10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/) | *Sphingomonas* PgmG | Ortholog bifunctional; quantifies G1P vs M1P specificity (~50× higher for G1P) (F001, F003) |
| [8765122](https://pubmed.ncbi.nlm.nih.gov/8765122/) | *Prochlorothrix* PmmA | 37% identical to AlgC, dual PMM/PGM activity confirmed (F001) |
| [15238632](https://pubmed.ncbi.nlm.nih.gov/15238632/) | Evolutionary trace of superfamily | Conserved active‑site residues across 71 members (F001) |
| [16595672](https://pubmed.ncbi.nlm.nih.gov/16595672/) | Processive mechanism | Two phosphoryl transfers + 180° intermediate reorientation (F002) |
| [15865428](https://pubmed.ncbi.nlm.nih.gov/15865428/) | Transient‑state kinetics | Glucose‑1,6‑bisphosphate is an obligatory bound intermediate (F002) |
| [22242625](https://pubmed.ncbi.nlm.nih.gov/22242625/) | NMR / phosphoryl transfer | Ser108 is the phosphoryl donor/acceptor; S108C impairs kcat (F007) |
| [24403075](https://pubmed.ncbi.nlm.nih.gov/24403075/) | HDX‑MS / SAXS flexibility | Dephosphorylation increases flexibility to aid reorientation (F007) |
| [23517223](https://pubmed.ncbi.nlm.nih.gov/23517223/) | Essential active‑site residue | His329 identified as critical general base (F007) |
| [20589904](https://pubmed.ncbi.nlm.nih.gov/20589904/) | Domain motion / hot spots | Single active site binds both glucose & mannose sugars (F007) |
| [23893395](https://pubmed.ncbi.nlm.nih.gov/23893395/) | Domain 4 NMR | C‑terminal domain closes over active site; needed for efficiency (F007) |
| [20512975](https://pubmed.ncbi.nlm.nih.gov/20512975/) | Fragment complementation | Chain connectivity of domain 4 optimizes catalysis (F007) |
| [30938049](https://pubmed.ncbi.nlm.nih.gov/30938049/) | Two forms of PMM | *P. putida* AlgC lacks periplasmic sensor → stand‑alone cytoplasmic enzyme (F004) |
| [17601783](https://pubmed.ncbi.nlm.nih.gov/17601783/) | Alginate & water limitation | Matric‑stress induction; desiccation protection in *P. putida* (F006) |
| [15101980](https://pubmed.ncbi.nlm.nih.gov/15101980/) | Cell envelope / desiccation | Alginate/envelope genes contribute to desiccation tolerance (F006) |
| [21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) | KT2440 EPS biofilm | Alginate/EPS act as biofilm structural stabilizers (F003, F006) |
| [24912454](https://pubmed.ncbi.nlm.nih.gov/24912454/) | KT2440 colony/transcriptome | Alginate creates hydrated environment under water limitation (F003) |
| [25186153](https://pubmed.ncbi.nlm.nih.gov/25186153/) | ErsA sRNA regulation of *algC* | *algC* is post‑transcriptionally regulated (context for expression control) |

**Note on organism scope:** The deep structural/mechanistic evidence (F002, F007) derives from the *P. aeruginosa* PMM/PGM. Because that enzyme is the direct functional ortholog of *P. putida* AlgC — same superfamily, same reaction, conserved active site ([PMID: 15238632](https://pubmed.ncbi.nlm.nih.gov/15238632/)) — these mechanistic conclusions transfer with high confidence to the KT2440 enzyme. Organism‑specific claims about localization/domain architecture (F004) and alginate physiology (F006) are supported by direct *P. putida* data.

---

## Limitations and Knowledge Gaps

1. **Absence of direct KT2440 enzyme kinetics.** No crystal structure or purified‑enzyme kinetic characterization exists specifically for *P. putida* KT2440 AlgC (Q88C93). The mechanism, catalytic residues (Ser108, His329), and processivity are inferred from the highly conserved *P. aeruginosa* ortholog and other family members. Residue numbering (Ser108, His329) is that of the *P. aeruginosa* protein; the equivalent positions in Q88C93 should be confirmed by alignment.

2. **Substrate‑specificity ratios are from orthologs.** The ~50‑fold kinetic preference for glucose‑1‑phosphate over mannose‑1‑phosphate is measured in *Sphingomonas* PgmG ([PMID: 10788412](https://pubmed.ncbi.nlm.nih.gov/10788412/)); the exact PMM:PGM activity ratio for KT2440 AlgC is not experimentally established and may differ.

3. **Localization is inferred.** Cytoplasmic localization is strongly supported by domain architecture and substrate chemistry but has not been directly demonstrated (e.g., by fractionation) for KT2440 AlgC.

4. **Regulation in *P. putida* is less defined.** The ErsA/σ²² post‑transcriptional regulatory circuit ([PMID: 25186153](https://pubmed.ncbi.nlm.nih.gov/25186153/)) was characterized in *P. aeruginosa*; whether an equivalent circuit operates in KT2440 is unknown.

5. **Relative importance of the three downstream pathways in KT2440** (alginate vs LPS vs rhamnolipid) has not been dissected with an *algC*‑specific mutant series in this strain; the alginate/desiccation link is the best‑supported.

---

## Proposed Follow‑up Experiments / Actions

1. **Purify and assay KT2440 AlgC (Q88C93).** Express the recombinant protein and directly measure PMM and PGM activities, Kₘ/kcat for glucose‑1‑P and mannose‑1‑P, Mg²⁺ dependence, and the PMM:PGM ratio — closing the largest gap (organism‑specific kinetics).

2. **Structural determination or confident homology model.** Solve a crystal/cryo‑EM structure of KT2440 AlgC, or build an AlphaFold model, and map the catalytic serine and histidine to their Q88C93 residue numbers; validate the four‑domain architecture and the mobile C‑terminal domain.

3. **Targeted active‑site mutagenesis in KT2440.** Alanine/cysteine substitutions at the predicted catalytic Ser and His to confirm their roles in the native enzyme via loss of PMM/PGM activity.

4. **Clean *algC* deletion + complementation in KT2440.** Quantify effects on alginate, LPS core/O‑antigen, and rhamnolipid, and on desiccation/matric‑stress survival, to establish the relative contribution of each downstream branch in this strain.

5. **Localization assay.** Cell fractionation or fluorescent fusion to confirm cytoplasmic localization and the absence of membrane association predicted from the domain architecture.

6. **Regulatory circuit mapping.** Test whether a σ²²/sRNA‑type post‑transcriptional control (analogous to ErsA in *P. aeruginosa*) modulates *algC*/PP_5288 under envelope or water stress in KT2440.

---

## Conclusion

*algC* (PP_5288, Q88C93) encodes **AlgC**, a soluble cytoplasmic bifunctional **phosphomannomutase/phosphoglucomutase** (EC 5.4.2.8 / 5.4.2.2) of the α‑D‑phosphohexomutase superfamily. It reversibly interconverts glucose‑6‑P ⇌ glucose‑1‑P and mannose‑6‑P ⇌ mannose‑1‑P by a Mg²⁺‑dependent processive mechanism using a catalytic phosphoserine as phosphoryl donor/acceptor, a histidine general base, and an enzyme‑bound sugar‑1,6‑bisphosphate intermediate that reorients 180° while a C‑terminal domain closes over the active site. The hexose‑1‑phosphates it produces are activated to GDP‑mannose, UDP‑glucose, and dTDP‑L‑rhamnose, supplying precursors for alginate, the LPS core/O‑antigen, and rhamnolipid; in *P. putida* KT2440 its ecologically primary output is alginate, an exopolysaccharide induced by matric water stress that protects cells against desiccation through a hydrated biofilm microenvironment.


## Artifacts

- [OpenScientist final report](algC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](algC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10481091
2. PMID:12761084
3. PMID:10788412
4. PMID:8765122
5. PMID:15238632
6. PMID:16595672
7. PMID:15865428
8. PMID:7558335
9. PMID:24912454
10. PMID:21507178
11. PMID:30938049
12. PMID:7515870
13. PMID:17601783
14. PMID:15101980
15. PMID:22242625
16. PMID:24403075
17. PMID:23517223
18. PMID:23893395
19. PMID:20512975
20. PMID:20589904
21. PMID:25186153