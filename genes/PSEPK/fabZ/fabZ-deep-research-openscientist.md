---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T10:45:05.535618'
end_time: '2026-07-23T11:31:37.667924'
duration_seconds: 2792.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabZ
  gene_symbol: fabZ
  uniprot_accession: Q88MG9
  protein_description: 'RecName: Full=3-hydroxyacyl-[acyl-carrier-protein] dehydratase
    FabZ {ECO:0000255|HAMAP-Rule:MF_00406}; EC=4.2.1.59 {ECO:0000255|HAMAP-Rule:MF_00406};
    AltName: Full=(3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase {ECO:0000255|HAMAP-Rule:MF_00406};
    Short=(3R)-hydroxymyristoyl-ACP dehydrase {ECO:0000255|HAMAP-Rule:MF_00406}; AltName:
    Full=Beta-hydroxyacyl-ACP dehydratase {ECO:0000255|HAMAP-Rule:MF_00406};'
  gene_info: Name=fabZ {ECO:0000255|HAMAP-Rule:MF_00406}; OrderedLocusNames=PP_1602;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the thioester dehydratase family. FabZ
  protein_domains: FabA_FabZ. (IPR013114); FabZ. (IPR010084); HotDog_dom_sf. (IPR029069);
    FabA (PF07977)
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
  path: fabZ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabZ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MG9
- **Protein Description:** RecName: Full=3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ {ECO:0000255|HAMAP-Rule:MF_00406}; EC=4.2.1.59 {ECO:0000255|HAMAP-Rule:MF_00406}; AltName: Full=(3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase {ECO:0000255|HAMAP-Rule:MF_00406}; Short=(3R)-hydroxymyristoyl-ACP dehydrase {ECO:0000255|HAMAP-Rule:MF_00406}; AltName: Full=Beta-hydroxyacyl-ACP dehydratase {ECO:0000255|HAMAP-Rule:MF_00406};
- **Gene Information:** Name=fabZ {ECO:0000255|HAMAP-Rule:MF_00406}; OrderedLocusNames=PP_1602;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the thioester dehydratase family. FabZ
- **Key Domains:** FabA_FabZ. (IPR013114); FabZ. (IPR010084); HotDog_dom_sf. (IPR029069); FabA (PF07977)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabZ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabZ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabZ** (gene ID: fabZ, UniProt: Q88MG9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FabZ (3-hydroxyacyl-[acyl-carrier-protein] dehydratase) in *Pseudomonas putida* KT2440

**UniProt:** Q88MG9 · **Gene:** *fabZ* (PP_1602) · **EC:** 4.2.1.59 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)

---

## Summary

**FabZ (Q88MG9, PP_1602) is the (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase (EC 4.2.1.59) that catalyzes the third, dehydration step of every elongation cycle in the bacterial type II fatty acid synthase (FAS-II) system of *Pseudomonas putida* KT2440.** In each turn of the elongation cycle, FabZ removes water from a (3R)-β-hydroxyacyl-ACP intermediate to produce a *trans*-2-enoyl-ACP, which is then reduced by FabI to complete the two-carbon chain extension. Unlike its paralog FabA, FabZ is a *general* elongation dehydratase that acts on acyl-ACP substrates across a broad range of chain lengths but **lacks the *trans*-2 → *cis*-3 isomerase activity** that commits carbon flux to anaerobic unsaturated fatty acid (UFA) synthesis. This division of labor is confirmed in *P. putida*, which encodes a separate FabA (Q88FC4, PP_4174) carrying the isomerase function.

The enzyme is a **soluble, cytoplasmic protein of ~16 kDa (146 aa)** that adopts the characteristic "hot-dog" fold and assembles into a homohexamer (a trimer of dimers), with each of the six active sites formed at a dimer interface. Catalysis proceeds through a strictly conserved active-site histidine — mapped by sequence homology to **His49** in Q88MG9 — that abstracts a proton during the syn dehydration of the ACP-tethered substrate. Structural studies of bacterial and parasite FabZ orthologs reveal a gated substrate tunnel whose length and geometry tune chain-length specificity, and a dynamic "seesaw-like" mechanism by which the hexamer sequentially loads and processes ACP-bound acyl chains.

Functionally, FabZ sits at the heart of membrane biogenesis. Its product pool of β-hydroxyacyl- and enoyl-ACP intermediates feeds directly into **membrane glycerophospholipid** synthesis and, via the shared (3R)-hydroxyacyl-ACP pool, into **lipid A (LPS) biosynthesis**. In *Pseudomonas aeruginosa* — a close relative of *P. putida* — *fabZ* is **essential for viability**, with conditional loss producing lethality and cell-morphology defects, establishing FabZ as a validated antibacterial drug target. Bioinformatic analysis confirms Q88MG9 is a bona fide, near-canonical FabZ: it is ~59% identical to the experimentally characterized *E. coli* FabZ, ~86% identical to *P. aeruginosa* FabZ, carries all hot-dog signature motifs and the catalytic His, and has no signal peptide or transmembrane segment, consistent with cytoplasmic localization.

---

## Key Findings

### Finding 1 — FabZ is the elongation-cycle (3R)-hydroxyacyl-ACP dehydratase (EC 4.2.1.59)

FabZ catalyzes the **third step of each FAS-II elongation cycle**: the dehydration of a (3R)-β-hydroxyacyl-ACP to a *trans*-2-enoyl-ACP. This assignment is anchored in the original genetic identification of the enzyme in *Escherichia coli*. Mohan and colleagues demonstrated that overproduction of the *orf17* gene product raised (3R)-hydroxymyristoyl-ACP dehydrase specific activity **as much as ~170-fold**, establishing *orf17* (subsequently named *fabZ*) as the structural gene for the dehydratase ([PMID: 7806516](https://pubmed.ncbi.nlm.nih.gov/7806516/)): *"Wild-type cells that overproduced the protein encoded by orf17 overproduced (3R)-hydroxymyristoyl-ACP dehydrase activity as much as 170-fold, suggesting that orf17 is the structural gene for the dehydrase."*

The biochemical reaction and its position in the pathway were defined through characterization of the *Plasmodium falciparum* ortholog, which *"catalyzes the dehydration of beta-hydroxyacyl-ACP to trans-2-acyl-ACP, the third step in the elongation phase of the FAS cycle"* ([PMID: 12930838](https://pubmed.ncbi.nlm.nih.gov/12930838/)). In in-vitro assays using surrogate substrates, FabZ acts on β-hydroxybutyryl-CoA (Km ≈ 199 µM) and the reverse-direction crotonoyl-CoA (Km ≈ 86 µM). This step is universal to FAS-II and is required in each round of two-carbon chain elongation, making FabZ one of the indispensable "core" enzymes of bacterial fatty acid synthesis.

The reaction can be summarized as:

```
   (3R)-β-hydroxyacyl-ACP  ── FabZ (EC 4.2.1.59) ──▶  trans-2-enoyl-ACP  +  H₂O
```

### Finding 2 — FabZ is a hexameric hot-dog-fold enzyme with a dynamic, ACP-dependent catalytic mechanism

FabZ belongs to the **thioester dehydratase (hot-dog fold) family**. Crystallographic studies across multiple organisms consistently show that the hot-dog monomers assemble into a **trimer of dimers (a homohexamer)**, with an active site located at each of the six dimer interfaces. In *Helicobacter pylori* FabZ, the substrate-binding tunnel is gated: *"Residue Tyr-100 at the entrance of the tunnel adopts either an open or closed conformation in the crystal structure"* ([PMID: 18093984](https://pubmed.ncbi.nlm.nih.gov/18093984/)). Aromatic residues lining the tunnel (e.g., Phe-83, Phe-169) switch conformations to reshape the tunnel between "L-" and "U-" shaped geometries, thereby controlling the length of acyl chain that can be accommodated — the structural basis for chain-length specificity. The *P. falciparum* FabZ structures corroborated this, showing Phe169 toggling between open and closed states to lengthen the tunnel for longer substrates ([PMID: 21843645](https://pubmed.ncbi.nlm.nih.gov/21843645/)).

Crucially, FabZ processes acyl chains that are covalently tethered to **acyl carrier protein (ACP)**, not free acyl-CoAs, in vivo. A landmark 2.55 Å structure of a FabZ–holo-ACP complex revealed *"a highly symmetrical FabZ hexamer-ACP"* assembly ([PMID: 27874013](https://pubmed.ncbi.nlm.nih.gov/27874013/)) and established a **"seesaw-like" alternating catalytic mechanism** in which ACP docking at one active site is coupled to conformational changes across the hexamer. This dynamic model was refined by identifying a **back-door phenylalanine (Phe83)** that *"regulates the stepwise hexameric loading of ACP"* ([PMID: 30677439](https://pubmed.ncbi.nlm.nih.gov/30677439/)), working together with a front-door Tyr100 gate. Together these studies portray FabZ not as a static catalyst but as an allosterically coordinated hexameric machine that sequentially engages ACP-delivered substrates.

| Structural feature | Role | Evidence |
|---|---|---|
| Hot-dog fold monomer | Basic catalytic unit | [PMID: 18093984](https://pubmed.ncbi.nlm.nih.gov/18093984/) |
| Trimer-of-dimers hexamer | Six active sites at dimer interfaces | [PMID: 18093984](https://pubmed.ncbi.nlm.nih.gov/18093984/), [PMID: 21843645](https://pubmed.ncbi.nlm.nih.gov/21843645/) |
| Tyr100 front-door gate | Open/closed control of tunnel entrance | [PMID: 18093984](https://pubmed.ncbi.nlm.nih.gov/18093984/), [PMID: 30677439](https://pubmed.ncbi.nlm.nih.gov/30677439/) |
| Phe83 back-door / Phe169 | Tune tunnel length / chain-length specificity; coordinate ACP loading | [PMID: 30677439](https://pubmed.ncbi.nlm.nih.gov/30677439/), [PMID: 21843645](https://pubmed.ncbi.nlm.nih.gov/21843645/) |
| FabZ–holo-ACP hexamer complex | Seesaw-like alternating catalysis | [PMID: 27874013](https://pubmed.ncbi.nlm.nih.gov/27874013/) |

### Finding 3 — FabZ is essential and supplies intermediates for both phospholipid and lipid A (LPS) biosynthesis in *Pseudomonas*

FabZ activity is required for viability in *Pseudomonas*. A conditional *fabZ* mutant of the close relative *P. aeruginosa* — a chromosomal ΔfabZ complemented only by a temperature-sensitive plasmid copy — is **lethal with cell-morphology defects at the restrictive temperature** ([PMID: 40294648](https://pubmed.ncbi.nlm.nih.gov/40294648/)): *"FabZ, a β-hydroxyacyl-acyl carrier protein dehydratase in the type II fatty acid synthesis pathway, is essential for the viability of Pseudomonas aeruginosa by ensuring proper fatty acid elongation and membrane stability."* The same study showed genetic interaction with the lipid A pathway: deletion of *lpxA* or *lpxC* failed to rescue lethality, whereas loss of *lpxH* suppressed it, and the resulting ΔfabZ ΔlpxH strain accumulated **odd-chain fatty acids (C15:0, C17:0)** — a signature of perturbed acyl-ACP flux.

This connection between FabZ and lipid A was first uncovered genetically in *E. coli*, where mutations in *fabZ* (*orf17*) were isolated as suppressors of a lipid A biosynthesis defect (*lpxA2*). The mechanism was attributed to a shift in the shared intermediate pool ([PMID: 7806516](https://pubmed.ncbi.nlm.nih.gov/7806516/)): *"bypass of the lpxA2 phenotype by mutations in orf17 may be due to an increased (3R)-hydroxymyristoyl-ACP pool."* Because (3R)-hydroxymyristoyl-ACP is both a FabZ substrate and the acyl donor for the first committed step of lipid A synthesis (LpxA), FabZ activity directly modulates the branch point between membrane phospholipid elongation and outer-membrane LPS assembly. FabZ's essentiality and its position at this metabolic node make it a **validated antibacterial target**.

```
                          ┌─────────────────────────────┐
   Acetyl-CoA ──▶ ... ──▶ │ (3R)-β-hydroxyacyl-ACP pool │
                          └───────────┬─────────────────┘
                                      │
                 ┌────────────────────┼─────────────────────┐
                 │ FabZ (elongation)  │  LpxA (lipid A)      │
                 ▼                    │                      ▼
        trans-2-enoyl-ACP            │              Lipid A / LPS
                 │                    │            (outer membrane)
                 ▼                    ▼
        Membrane glycerophospholipids (inner/outer membrane)
```

### Finding 4 — FabZ is the general elongation dehydratase and, unlike FabA, lacks isomerase activity

In α- and γ-proteobacteria (the lineage containing *P. putida*), two functionally distinct dehydratases operate: **FabA and FabZ**. FabA is bifunctional, catalyzing both the dehydration of β-hydroxydecanoyl-ACP and the **isomerization of *trans*-2-decenoyl-ACP to *cis*-3-decenoyl-ACP** — the committed step of anaerobic unsaturated fatty acid biosynthesis. FabZ, by contrast, *"functions in acyl chain elongation but cannot carry out the isomerization reaction"* ([PMID: 15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/)). This distinction was reinforced by structural/dynamical work confirming that *"Fatty acid biosynthesis in α- and γ-proteobacteria requires two functionally distinct dehydratases, FabA and FabZ"* ([PMID: 30872475](https://pubmed.ncbi.nlm.nih.gov/30872475/)).

The molecular determinant of isomerase potential lies in the **β3/β4 strands** that shape the substrate tunnel: domain-swapping experiments showed that transplanting these strands can convert a FabZ-type enzyme into an isomerase-competent enzyme ([PMID: 15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/)). Some bacteria that lack FabA instead deploy a single **bifunctional FabZ/FabN/FabQ** homolog to satisfy both roles — for example, *Enterococcus faecalis* FabZ1 functionally replaces *E. coli* FabA ([PMID: 15194690](https://pubmed.ncbi.nlm.nih.gov/15194690/)), and *Aerococcus viridans* FabQ combines dehydratase and isomerase activities ([PMID: 23972938](https://pubmed.ncbi.nlm.nih.gov/23972938/)). Because *P. putida* possesses a dedicated FabA (see Finding 6), its FabZ is confidently assigned the **general, isomerase-negative elongation role**.

| Enzyme | Dehydratase | Isomerase | Role |
|---|---|---|---|
| **FabZ** (Q88MG9, P. putida) | ✔ | ✗ | General chain elongation, all chain lengths |
| **FabA** (Q88FC4, P. putida) | ✔ | ✔ | Commits flux to anaerobic UFA synthesis |
| FabN / FabQ (other bacteria) | ✔ | ✔ | Bifunctional substitute where FabA is absent |

### Finding 5 — Sequence analysis confirms Q88MG9 is a bona fide FabZ with the conserved catalytic His49

Bioinformatic verification places Q88MG9 squarely within the canonical FabZ family. The *P. putida* KT2440 protein is **146 aa (~16 kDa)** and shares **59.4% amino-acid identity (85/143 aligned columns)** with the experimentally characterized *E. coli* FabZ (P0A6Q6) by global Needleman–Wunsch alignment. It carries the hot-dog signature motifs LPHR(Y/F)PF, F(F/Q)xGHFP, and the C-terminal VDGK…C motif.

The catalytic histidine was mapped by tracing the mechanism-based inhibitor evidence from *E. coli* FabA. Cronan and colleagues used the specific mechanism-activated inhibitor 3-decynoyl-N-acetylcysteamine to label the active-site residue ([PMID: 2832401](https://pubmed.ncbi.nlm.nih.gov/2832401/)): *"The active site histidine residue (His-70) has been identified by analysis of the peptides labeled by reaction with 14C-labeled 3-decynoyl-N-acetylcysteamine, a specific mechanism-activated inhibitor. A cysteine residue (Cys-69) adjacent to the active site histidine."* Propagating this catalytic His through FabA → FabZ → *P. putida* FabZ alignments places the conserved catalytic histidine at **His49** of Q88MG9, embedded in the F-F-N-G-**H49**-F-P motif (homologous to *E. coli* FabZ His54). Finally, the protein has **no signal peptide and no transmembrane segment**, consistent with a soluble, cytoplasmic enzyme — the expected localization for a FAS-II component.

### Finding 6 — *P. putida* encodes a separate FabA (PP_4174), and FabZ/His49 are conserved across *Pseudomonas*

The genome of *P. putida* KT2440 encodes a **distinct FabA** (UniProt Q88FC4, gene *fabA*/PP_4174, 171 aa) annotated with both dehydratase (EC 4.2.1.59) and *trans*-2-decenoyl-ACP isomerase (EC 5.3.3.14) activities. Its presence confirms that FabZ (Q88MG9/PP_1602) and FabA are physically and functionally separate enzymes in this organism, cementing the division of labor described in Finding 4. Consistent with the general rule that when a dedicated FabA is present the FabZ serves the elongation role ([PMID: 15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/)), *P. putida* FabZ can be assigned the general dehydratase function.

Conservation analysis across the genus reinforces the annotation: *P. putida* FabZ is **86.3% identical (126/146)** to *P. aeruginosa* FabZ (Q9HXY7) and near-identical to *P. syringae* FabZ orthologs. Both the N-terminal His13 and the catalytic His49 (in the F-F-N-G-H-F-P motif) are strictly conserved across these species, underscoring the functional importance of these residues.

---

## Mechanistic Model / Interpretation

FabZ operates within the iterative **bacterial type II fatty acid synthase (FAS-II)** cycle. Unlike the mammalian single-polypeptide FAS-I, the bacterial system is a set of discrete, soluble enzymes that act on acyl chains shuttled between them by the small acyl carrier protein (ACP). Each elongation cycle adds two carbons through four sequential steps:

```
  Acyl-ACP (Cn) + Malonyl-ACP
          │  FabB/FabF (condensation)
          ▼
  β-ketoacyl-ACP (Cn+2)
          │  FabG (NADPH reduction)
          ▼
  (3R)-β-hydroxyacyl-ACP  ◀── FabZ substrate
          │  ★ FabZ (dehydration, EC 4.2.1.59)  — THIS ENZYME
          ▼
  trans-2-enoyl-ACP
          │  FabI (NADH reduction)
          ▼
  Acyl-ACP (Cn+2)  ──▶ next cycle, or exported to phospholipid / lipid A synthesis
```

FabZ occupies the **third (dehydration) position** in this cycle. Its substrate, the (3R)-β-hydroxyacyl-ACP produced by the FabG reductase, is bound with the acyl chain threaded into the hot-dog tunnel and the ACP phosphopantetheine arm delivering the thioester into the active site. The conserved **His49** acts as the catalytic base/acid that mediates a *syn* elimination of water across the Cα–Cβ bond, generating the *trans*-2-enoyl product that FabI subsequently reduces.

Three layers of structural sophistication distinguish FabZ:

1. **Quaternary structure** — the hexamer (trimer of dimers) provides six composite active sites, each contributed by two subunits, and enables allosteric coordination.
2. **Substrate gating** — the Tyr100 front door and Phe83 back door open and close to admit ACP and tune tunnel length, allowing FabZ to process the full spectrum of chain lengths that a growing acyl chain passes through (a *general* dehydratase, not restricted like the C10-specialized FabA isomerization step).
3. **Seesaw loading** — ACP molecules dock and undock in a coordinated, stepwise fashion across the hexamer, coupling catalysis at one site to conformational states at neighbors.

The **biological significance** of FabZ flows from its position as a gatekeeper of the acyl-ACP intermediate pool. Its products are the precursors of all membrane glycerophospholipids and, through the shared (3R)-hydroxymyristoyl-ACP node, of lipid A / LPS. This explains three observations at once: (i) *fabZ* essentiality (blocking the cycle halts membrane biogenesis and kills the cell); (ii) the genetic interaction with the lipid A (*lpx*) pathway (perturbing FabZ shifts the shared intermediate pool); and (iii) the accumulation of odd-chain fatty acids when the balance is disrupted. In *P. putida* specifically — a metabolically versatile, solvent-tolerant soil bacterium whose membrane adaptation (fatty-acid saturation, *cis/trans* isomerization, cardiolipin content) is central to its stress physiology — FabZ is the workhorse elongation dehydratase feeding this adaptable membrane lipidome, while its paralog FabA handles the committed step toward unsaturated acyl chains.

---

## Evidence Base

| PMID | Study focus | How it supports the annotation |
|---|---|---|
| [7806516](https://pubmed.ncbi.nlm.nih.gov/7806516/) | *E. coli fabZ* (orf17) genetic identification | Establishes FabZ as the structural gene for (3R)-hydroxyacyl-ACP dehydrase (~170-fold activity on overexpression); links product pool to lipid A synthesis |
| [12930838](https://pubmed.ncbi.nlm.nih.gov/12930838/) | *P. falciparum* FabZ characterization | Defines the reaction: dehydration of β-hydroxyacyl-ACP to trans-2-acyl-ACP, third step of the elongation cycle; provides kinetic parameters |
| [27874013](https://pubmed.ncbi.nlm.nih.gov/27874013/) | FabZ–holo-ACP crystal complex (2.55 Å) | Documents the hexamer–ACP assembly and the seesaw-like alternating mechanism |
| [18093984](https://pubmed.ncbi.nlm.nih.gov/18093984/) | *H. pylori* FabZ structure | Reveals gated substrate tunnel (Tyr100 open/closed), hot-dog fold, chain-length control |
| [30677439](https://pubmed.ncbi.nlm.nih.gov/30677439/) | FabZ ACP-loading mechanism | Identifies back-door Phe83 regulating stepwise hexameric ACP loading |
| [21843645](https://pubmed.ncbi.nlm.nih.gov/21843645/) | *P. falciparum* FabZ + inhibitors | U-shaped tunnel; Phe169 conformational switch controls accommodated chain length |
| [40294648](https://pubmed.ncbi.nlm.nih.gov/40294648/) | *P. aeruginosa* conditional *fabZ* mutant | Directly establishes FabZ essentiality in *Pseudomonas*; genetic interaction with lipid A pathway; odd-chain FA accumulation |
| [15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/) | FabN/FabZ domain swapping | Defines FabZ as elongation dehydratase lacking isomerase activity; localizes β3/β4 isomerase determinants |
| [30872475](https://pubmed.ncbi.nlm.nih.gov/30872475/) | Structural rationale for FA unsaturation | Confirms FabA and FabZ are two functionally distinct dehydratases in α/γ-proteobacteria |
| [15194690](https://pubmed.ncbi.nlm.nih.gov/15194690/) | *E. faecalis* FabZ/FabF | Shows some FabZ homologs are bifunctional dehydratase/isomerase where FabA is absent (contrast case) |
| [23972938](https://pubmed.ncbi.nlm.nih.gov/23972938/) | *A. viridans* FabQ | Single FabA/FabZ homolog with dual dehydratase/isomerase function (contrast case) |
| [2832401](https://pubmed.ncbi.nlm.nih.gov/2832401/) | *E. coli* FabA active-site mapping | Experimentally identifies the catalytic active-site histidine of the FabA/FabZ family (basis for His49 assignment in Q88MG9) |

**Direct vs. inferred evidence for *P. putida* Q88MG9.** No study to date has biochemically characterized the *P. putida* KT2440 FabZ protein itself. The functional annotation rests on: (a) strong, experimentally grounded characterization of orthologs (*E. coli*, *H. pylori*, *P. falciparum*, *P. aeruginosa*); (b) the demonstrated essentiality of *fabZ* in the very close relative *P. aeruginosa*; and (c) sequence/structural bioinformatics establishing that Q88MG9 is a canonical FabZ with the conserved catalytic His49 and no isomerase-associated features, alongside a separate FabA in the same genome. This constitutes a robust, convergent case by homology and orthology, in line with the HAMAP-Rule (MF_00406) annotation.

---

## Limitations and Knowledge Gaps

- **No direct biochemical data on Q88MG9.** The *P. putida* KT2440 FabZ has not been purified, assayed, or crystallized. Kinetic parameters (kcat, Km), precise chain-length preference, and hexameric assembly are inferred from orthologs rather than measured.
- **His49 assignment is homology-based.** The catalytic histidine has been mapped by multiple sequence alignment through FabA→FabZ chains, not by site-directed mutagenesis or structure of the *P. putida* enzyme. Confidence is high given strict conservation, but experimental confirmation is lacking.
- **Chain-length specificity not resolved.** FabZ is a "general" dehydratase, but the exact substrate profile in *P. putida* (which produces a characteristic membrane lipidome including C16/C18 species and *cis/trans* isomers) has not been mapped. The tunnel-gating residues that set specificity in other species have not been examined in Q88MG9.
- **Essentiality inferred from *P. aeruginosa*.** While highly likely given ~86% identity and the shared FAS-II architecture, *fabZ* essentiality has not been formally demonstrated in *P. putida* KT2440.
- **FabZ/FabA functional partitioning not directly tested in *P. putida*.** The clean division of labor is inferred from genome content and general proteobacterial biology; genetic complementation/knockout experiments in *P. putida* would confirm it.
- **Interaction with FabA and ACP in vivo.** The physical/functional coordination of FabZ with *P. putida* ACP and FabA (e.g., whether they form transient complexes, or share substrate channeling) is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify *P. putida* FabZ (Q88MG9) and measure dehydratase activity on a chain-length panel of (3R)-β-hydroxyacyl-ACP substrates to define kcat/Km and confirm the absence of isomerase activity (e.g., no *cis*-3 product from *trans*-2-decenoyl-ACP). Consider the fused-dimer construct strategy shown to improve FabZ solubility/activity ([PMID: 29520922](https://pubmed.ncbi.nlm.nih.gov/29520922/)).
2. **Catalytic His49 mutagenesis.** Generate an H49A (or H49Q) variant and demonstrate loss of dehydratase activity to experimentally validate the catalytic residue predicted here.
3. **Genetic essentiality test.** Attempt a clean *fabZ* deletion in *P. putida* KT2440 with a rescue copy (temperature-sensitive or inducible), mirroring the *P. aeruginosa* design ([PMID: 40294648](https://pubmed.ncbi.nlm.nih.gov/40294648/)), to confirm essentiality and characterize morphological/membrane phenotypes.
4. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* FabZ (apo and, ideally, in complex with *P. putida* holo-ACP) to verify the hexameric hot-dog architecture, the His49 active site, and the identity of tunnel-gating residues governing chain-length specificity.
5. **Lipidomic flux analysis.** Perturb *fabZ* expression (knockdown/overexpression) and quantify membrane glycerophospholipid and LPS/lipid A composition by LC-MS/MS (building on established *P. putida* lipidomics, [PMID: 21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/)) to map how FabZ activity partitions flux between phospholipid elongation and lipid A synthesis, and whether odd-chain FA accumulation recurs.
6. **FabZ/FabA epistasis.** Test genetic interactions between *fabZ* (PP_1602) and *fabA* (PP_4174) in *P. putida* to confirm the division of labor and probe whether either can compensate for the other.
7. **Antibacterial target validation.** Given FabZ essentiality, screen known FabZ inhibitor chemotypes (e.g., naphthoquinones/juglone, flavonoid gallates) against purified *P. putida* FabZ to assess whether it is a tractable target for narrow-spectrum antibacterials.

---

*Report compiled from 6 confirmed findings and 30 reviewed papers over 3 investigation iterations. All functional claims for Q88MG9 are supported by experimentally characterized orthologs and by sequence/structural bioinformatics; no direct biochemical study of the P. putida KT2440 protein currently exists.*


## Artifacts

- [OpenScientist final report](fabZ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabZ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7806516
2. PMID:12930838
3. PMID:18093984
4. PMID:21843645
5. PMID:27874013
6. PMID:30677439
7. PMID:40294648
8. PMID:15980063
9. PMID:30872475
10. PMID:15194690
11. PMID:23972938
12. PMID:2832401
13. PMID:29520922
14. PMID:21895997