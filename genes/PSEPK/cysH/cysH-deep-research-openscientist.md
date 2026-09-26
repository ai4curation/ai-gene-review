---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T15:56:44.166865'
end_time: '2026-07-25T16:08:50.804278'
duration_seconds: 726.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cysH
  gene_symbol: cysH
  uniprot_accession: Q88KG2
  protein_description: 'RecName: Full=Adenosine 5''-phosphosulfate reductase {ECO:0000256|ARBA:ARBA00029514,
    ECO:0000256|HAMAP-Rule:MF_00063}; Short=APS reductase {ECO:0000256|HAMAP-Rule:MF_00063};
    EC=1.8.4.10 {ECO:0000256|ARBA:ARBA00024386, ECO:0000256|HAMAP-Rule:MF_00063};
    AltName: Full=5''-adenylylsulfate reductase {ECO:0000256|ARBA:ARBA00032041, ECO:0000256|HAMAP-Rule:MF_00063};
    AltName: Full=Thioredoxin-dependent 5''-adenylylsulfate reductase {ECO:0000256|ARBA:ARBA00030894,
    ECO:0000256|HAMAP-Rule:MF_00063};'
  gene_info: Name=cysH {ECO:0000256|HAMAP-Rule:MF_00063, ECO:0000313|EMBL:AAN67941.1};
    OrderedLocusNames=PP_2328 {ECO:0000313|EMBL:AAN67941.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PAPS reductase family. CysH subfamily.
  protein_domains: APS_reductase. (IPR011798); PAPS/APS_Rdtase. (IPR004511); PAPS_reduct_dom.
    (IPR002500); Rossmann-like_a/b/a_fold. (IPR014729); PAPS_reduct (PF01507)
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
  path: cysH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cysH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KG2
- **Protein Description:** RecName: Full=Adenosine 5'-phosphosulfate reductase {ECO:0000256|ARBA:ARBA00029514, ECO:0000256|HAMAP-Rule:MF_00063}; Short=APS reductase {ECO:0000256|HAMAP-Rule:MF_00063}; EC=1.8.4.10 {ECO:0000256|ARBA:ARBA00024386, ECO:0000256|HAMAP-Rule:MF_00063}; AltName: Full=5'-adenylylsulfate reductase {ECO:0000256|ARBA:ARBA00032041, ECO:0000256|HAMAP-Rule:MF_00063}; AltName: Full=Thioredoxin-dependent 5'-adenylylsulfate reductase {ECO:0000256|ARBA:ARBA00030894, ECO:0000256|HAMAP-Rule:MF_00063};
- **Gene Information:** Name=cysH {ECO:0000256|HAMAP-Rule:MF_00063, ECO:0000313|EMBL:AAN67941.1}; OrderedLocusNames=PP_2328 {ECO:0000313|EMBL:AAN67941.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PAPS reductase family. CysH subfamily.
- **Key Domains:** APS_reductase. (IPR011798); PAPS/APS_Rdtase. (IPR004511); PAPS_reduct_dom. (IPR002500); Rossmann-like_a/b/a_fold. (IPR014729); PAPS_reduct (PF01507)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cysH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cysH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cysH** (gene ID: cysH, UniProt: Q88KG2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *cysH* (Q88KG2) — Adenosine 5′-Phosphosulfate Reductase from *Pseudomonas putida* KT2440

## Summary

The gene **cysH** (locus **PP_2328**; UniProt **Q88KG2**) of *Pseudomonas putida* strain KT2440 encodes a **thioredoxin-dependent adenosine-5′-phosphosulfate (APS) reductase** (EC 1.8.4.10). This ~28 kDa, 244-residue cytoplasmic enzyme catalyzes the **first committed reductive step of assimilatory sulfate reduction**: the two-electron reduction of APS to sulfite plus AMP, with reduced thioredoxin serving as the physiological electron donor. This reaction commits activated sulfate to the reductive branch of sulfur metabolism, ultimately supplying sulfide for the biosynthesis of cysteine, methionine, glutathione, iron–sulfur clusters, and other sulfur-containing metabolites. The identification is unambiguous: Q88KG2 contains both C-terminal signature motifs (CCGIRKIEPL and SIGCEPCT) that are diagnostic of true **APS reductases** and that distinguish them from the mechanistically related **PAPS reductases**.

The mechanistic and structural understanding of this enzyme rests on exceptionally firm ground because Q88KG2 is **85.7% identical** to the CysH of *Pseudomonas aeruginosa* PAO1 (UniProt O05927), whose crystal structure has been solved to 2.7 Å resolution and whose catalytic cycle has been captured biochemically. The enzyme harbors an **essential [4Fe-4S] cluster** coordinated in an unusual mode by tandem cysteine residues (a CC-X~80-CXXC motif; Cys116/Cys117 and Cys205/Cys208 in Q88KG2). This cluster does not directly transfer electrons but instead enhances the rate of APS reduction by nearly 1000-fold and is a key determinant of substrate specificity for APS over PAPS. Catalysis proceeds through a **two-step covalent mechanism**: a conserved C-terminal catalytic cysteine (Cys233, in the ECGLH motif) attacks the sulfate of APS to form an enzyme-bound **S-sulfocysteine (thiosulfonate) intermediate**, which is subsequently resolved by thioredoxin to release free sulfite.

Functionally, cysH operates in the cytoplasm and sits at a **metabolic branch point** downstream of ATP sulfurylase/APS kinase (CysNC/CysDN) and upstream of sulfite reductase (CysIJ) and O-acetylserine sulfhydrylase (CysK/CysM). In *P. putida*, expression of cysH is embedded in the CysB-controlled **sulfate-starvation regulon**, connecting sulfate assimilation to the organism's broader sulfur-scavenging physiology. Genetic disruption of cysH in the closely related *P. aeruginosa* produces cysteine auxotrophy, and deletion in mycobacteria yields a cysteine/methionine auxotroph, confirming that this enzyme is required for de novo reductive sulfur assimilation.

---

## Gene/Protein Identity Verification

The mandatory identity checks required by this research task were satisfied:

| Verification item | Result |
|---|---|
| Gene symbol matches protein description | **Yes** — cysH encodes APS reductase (CysH subfamily of the PAPS reductase family) |
| Organism correct | **Yes** — *Pseudomonas putida* KT2440 (PSEPK) |
| Protein family/domains align with literature | **Yes** — PF01507 (PAPS_reduct), IPR011798 (APS_reductase), Rossmann-like α/β/α fold |
| Diagnostic APS-reductase motifs present | **Yes** — CCGIRKIEPL (res 116) and SIGCEPCT (res 205) present in Q88KG2 |
| Risk of confusion with a different gene | **Low** — Pseudomonas/bacterial CysH literature is directly relevant and internally consistent |

**A note on nomenclature.** In *Escherichia coli* the gene named *cysH* encodes a **PAPS reductase** (which reduces 3′-phosphoadenosine-5′-phosphosulfate, PAPS, and lacks an Fe–S cluster), whereas in *Pseudomonas*, plants, and many other organisms the *cysH*/CysH-family enzyme is an **APS reductase** (reducing APS directly and containing a [4Fe-4S] cluster). Both are members of the same PAPS reductase (sulfonucleotide reductase) family and share a common fold and catalytic cysteine, but they differ in substrate and cofactor. The UniProt annotation, the diagnostic C-terminal motifs, and the 85.7%-identical *P. aeruginosa* ortholog all confirm that **Q88KG2 is a genuine APS reductase**, not a PAPS reductase. This distinction is central to the correct functional annotation and is addressed explicitly below.

---

## Key Findings

### Finding 1 — cysH is a thioredoxin-dependent APS reductase (EC 1.8.4.10) catalyzing the first committed reductive step of sulfate assimilation

The primary function of the cysH gene product is to catalyze:

> **APS + reduced thioredoxin → sulfite + AMP + oxidized thioredoxin**

This is the first committed reductive step of the assimilatory sulfate reduction pathway. Two independent lines of evidence establish this identity for Q88KG2. First, at the sequence level, the 244-residue protein contains **both** C-terminal signature motifs diagnostic of true APS reductases: **CCGIRKIEPL** (matching the consensus CCXXRKXXPL at residue 116) and **SIGCEPCT** (matching SXGCXXCT at residue 205). These motifs are found in the C-termini of all APS reductases but not in PAPS reductases, and they can be used to predict substrate specificity within this enzyme family ([PMID: 12072441](https://pubmed.ncbi.nlm.nih.gov/12072441/)): *"two conserved sequence motifs, CCXXRKXXPL and SXGCXXCT, found in the C termini of all APS reductases, but not in PAPS reductases, may be used to predict the substrate specificity of these enzymes."*

Second, and most directly, the *P. aeruginosa* ortholog — 85.7% identical to Q88KG2 — has been purified and biochemically characterized. Recombinant His-tagged *P. aeruginosa* CysH reduces APS but **not** PAPS, with a specific activity of **5.8 µmol·min⁻¹·mg⁻¹** at pH 8.5 and 30 °C, using thioredoxin as the electron donor ([PMID: 10613872](https://pubmed.ncbi.nlm.nih.gov/10613872/)): *"Purified P. aeruginosa CysH expressed as a His-tagged recombinant protein is able to reduce APS, but not PAPS. The enzyme has a specific activity of 5.8 micromol. min(-1). mg of protein(-1) at pH 8.5 and 30 degrees C with thioredoxin supplied as an electron donor."* Because Q88KG2 carries the identical diagnostic motifs and is nearly identical in sequence, this experimentally-verified enzymology transfers directly to the *P. putida* protein.

The requirement for thioredoxin as the physiological reductant places APS reductase within the thioredoxin superfamily; classic *E. coli* genetics showed that thioredoxin or glutaredoxin is essential for sulfate reduction (as hydrogen donors for the sulfonucleotide reductase step) but not for deoxyribonucleotide synthesis ([PMID: 2180911](https://pubmed.ncbi.nlm.nih.gov/2180911/)), and plant APS reductases were redefined as members of the thioredoxin superfamily ([PMID: 9566743](https://pubmed.ncbi.nlm.nih.gov/9566743/)).

### Finding 2 — The enzyme harbors an essential [4Fe-4S] cluster coordinated by a tandem-cysteine CC-X~80-CXXC motif

APS reductases of the CysH subfamily are **iron–sulfur metalloenzymes**. Q88KG2 contains a tandem cysteine pair (**Cys116–Cys117**) and a downstream CXXC element (**Cys205-Glu-Pro-Cys208**), producing the characteristic **CC-X~80-CXXC** arrangement that coordinates a single [4Fe-4S] cluster in all characterized APS reductases. In the *P. aeruginosa* ortholog, the crystal structure directly reveals a **[4Fe-4S] cluster that is essential for catalysis**, coordinated in an unusual mode by tandem cysteine residues ([PMID: 17010373](https://pubmed.ncbi.nlm.nih.gov/17010373/)): *"P. aeruginosa APS reductase contains an [4Fe-4S] cluster that is essential for catalysis. The structure reveals an unusual mode of cluster coordination by tandem cysteine residues."*

Remarkably, the cluster does not appear to serve a conventional electron-relay role. Instead, iron–sulfur cluster engineering demonstrates that the cofactor **enhances APS reduction by nearly 1000-fold**, playing a pivotal role in both substrate specificity and catalysis ([PMID: 22023093](https://pubmed.ncbi.nlm.nih.gov/22023093/)): *"the iron-sulfur cluster cofactor enhances APS reduction by nearly 1000-fold, thereby playing a pivotal role in substrate specificity and catalysis."* Spectroscopic and computational studies of the homologous *M. tuberculosis* enzyme show the cluster remains in the [4Fe-4S]²⁺ state in both native and substrate-bound forms and that the tandem-cysteine coordination "fine-tunes" the electronic structure to prevent reduction of the cluster ([PMID: 21678934](https://pubmed.ncbi.nlm.nih.gov/21678934/)). The essentiality of the four coordinating cysteines was independently confirmed by site-directed mutagenesis in the *Acidithiobacillus ferrooxidans* APS reductase (Cys110/111, Cys193/196), a soluble 28 kDa protein ([PMID: 19225840](https://pubmed.ncbi.nlm.nih.gov/19225840/)).

It is worth noting that the Fe–S cluster is not strictly required for APS reduction chemistry per se: the moss *Physcomitrella patens* enzyme PpAPR-B reduces APS **without** an Fe–S cluster, albeit with lower turnover and higher protein stability ([PMID: 17519237](https://pubmed.ncbi.nlm.nih.gov/17519237/)). This shows the cluster is a catalytic accelerator and specificity determinant rather than an absolute chemical requirement — but in the *Pseudomonas*/CysH-subfamily enzyme it is genuinely essential for physiological activity.

### Finding 3 — Catalysis proceeds by a two-step covalent mechanism through an S-sulfocysteine (thiosulfonate) intermediate resolved by thioredoxin

The catalytic cycle of APS reductase is a **two-step covalent (ping-pong-like) mechanism**. In the first step, a conserved C-terminal catalytic cysteine performs nucleophilic attack on the sulfur of the APS sulfate group, cleaving the O–S bond, releasing AMP, and forming a covalent enzyme **S-sulfocysteine (thiosulfonate, Cys-S-SO₃⁻) intermediate**. In the second step, thioredoxin reduces this intermediate, releasing free sulfite and regenerating the active enzyme. Q88KG2 carries the conserved C-terminal catalytic cysteine within the **ECGLH** motif at **Cys233**.

The 2.7 Å crystal structure of the *P. aeruginosa* enzyme was captured in the **thiosulfonate intermediate form with substrate bound**, and it established that the two chemically discrete steps of the overall reaction take place at **distinct sites** on the enzyme, mediated by conformational flexibility of the C-terminal ~18 residues ([PMID: 17010373](https://pubmed.ncbi.nlm.nih.gov/17010373/)): *"the two chemically discrete steps of the overall reaction take place at distinct sites on the enzyme, mediated via conformational flexibility of the C-terminal 18 residues."* The mobile C-terminal tail thus shuttles the covalent sulfonyl intermediate between the APS-binding site and the thioredoxin-interaction site.

The active site couples the substrate directly to the metallocofactor. In the *M. tuberculosis* enzyme, spectroscopy and mutagenesis identified an essential role for the active-site residue **Lys144**, whose side chain interacts with **both** the iron–sulfur cluster and the sulfate group of APS ([PMID: 21075841](https://pubmed.ncbi.nlm.nih.gov/21075841/)): *"identified an essential role for the active site residue Lys-144, whose side chain interacts with both the iron-sulfur cluster and the sulfate group of adenosine 5'-phosphosulfate."* DFT calculations independently confirmed that mutating Lys144 to alanine disrupts the interactions linking the [4Fe-4S] cluster and APS ([PMID: 21678934](https://pubmed.ncbi.nlm.nih.gov/21678934/)), reinforcing that this residue is a crucial catalytic link. This intimate coupling between substrate and cluster explains how the cofactor contributes ~1000-fold to catalytic rate and to specificity.

### Finding 4 — The enzyme functions in the cytoplasm at a metabolic branch point committing APS-sulfur to cysteine/methionine biosynthesis

APS reductase acts in the **cytoplasm** as a soluble ~28 kDa protein. Q88KG2 has no predicted signal peptide or transmembrane region, consistent with a cytosolic localization, and the entire assimilatory sulfate reduction pathway (ATP sulfurylase/APS kinase → APS reductase → sulfite reductase → cysteine synthase) operates in the cytoplasm.

The biological role of cysH is to define the **committed, rate-controlling entry** into reductive sulfur assimilation. Genetic evidence in the direct Pseudomonas ortholog is decisive: an **insertional knockout of *P. aeruginosa* cysH produces cysteine auxotrophy** ([PMID: 10613872](https://pubmed.ncbi.nlm.nih.gov/10613872/)): *"Insertional knockout mutation of P. aeruginosa cysH produced cysteine auxotrophy, indicating its role in sulfate assimilation."* Consistently, deletion of CysH from *Mycobacterium smegmatis* yields a **cysteine and methionine auxotroph**, demonstrating that the enzyme lies at a metabolic branch point centered on APS ([PMID: 12072441](https://pubmed.ncbi.nlm.nih.gov/12072441/)): *"Deletion of CysH from M. smegmatis afforded a cysteine and methionine auxotroph consistent with a metabolic branch point centered on APS."*

The "branch point" concept is important. APS can be either (i) reduced by APS reductase (cysH) toward sulfide and cysteine, or (ii) phosphorylated by APS kinase to PAPS for sulfotransferase reactions and secondary metabolism. cysH channels activated sulfate into the **reductive/biosynthetic** branch. The centrality of this branch point is underscored by the observation that in *E. coli*, blocking cysH causes accumulation of the upstream intermediate PAPS, which acts as a signaling molecule affecting cell-surface structures, curli fiber production, adhesion, and cAMP-dependent gene expression ([PMID: 24934621](https://pubmed.ncbi.nlm.nih.gov/24934621/); [PMID: 27091548](https://pubmed.ncbi.nlm.nih.gov/27091548/)). A related applied study of *Citrobacter* sp. treats cysH as a rate-limiting sulfur-metabolism gene affecting cadmium/CdS immobilization ([PMID: 39153279](https://pubmed.ncbi.nlm.nih.gov/39153279/)). These pleiotropic effects, while informative about pathway architecture, are secondary consequences of intermediate accumulation rather than the enzyme's primary function.

### Finding 5 — Q88KG2 is 85.7% identical to the structurally characterized *P. aeruginosa* APS reductase, licensing direct mechanistic/structural transfer

A global Needleman–Wunsch alignment of *P. putida* KT2440 CysH (Q88KG2, 244 aa) against the reviewed, structurally characterized *P. aeruginosa* PAO1 CysH (UniProt O05927 / CYSH_PSEAE, 267 aa, protein-existence evidence level 1) gives **210/245 = 85.7% identical positions**. All three functionally diagnostic elements are conserved in both proteins: the two APS-reductase C-terminal motifs (**CCGIRKIEPL** and **SIGCEPCT**) and the **ECGLH** catalytic-cysteine motif. The *P. aeruginosa* protein carries a short N-terminal extension (~23 aa) upstream of the shared MSQPFD… start, accounting for most of the length difference.

This very high identity is what makes the functional annotation of Q88KG2 robust: the *P. aeruginosa* CysH is precisely the enzyme whose crystal structure was solved in the thiosulfonate-intermediate form with substrate bound ([PMID: 17010373](https://pubmed.ncbi.nlm.nih.gov/17010373/)): *"We report the 2.7 A resolution crystal structure of Pseudomonas aeruginosa APS reductase in the thiosulfonate intermediate form of the catalytic cycle and with substrate bound."* At 85.7% identity, the active-site architecture, Fe–S cluster coordination, catalytic residues, and reaction mechanism can be transferred with high confidence to the *P. putida* enzyme.

### Finding 6 — In *P. putida*, cysH belongs to the CysB-controlled sulfate-starvation regulon (cysNC → cysH → cysI)

In *P. putida*, the assimilatory sulfate reduction genes are organized under the control of the LysR-type master regulator **CysB**, which governs the sulfate-starvation response. The pathway around CysH consists of **CysNC** (ATP sulfurylase/APS kinase — sulfate → APS), **CysH** (APS → sulfite), and **CysI** (sulfite reductase — sulfite → sulfide). CysB directly activates sulfate-starvation-induced (sfn) genes and acts as the master regulator of the sulfate-starvation response ([PMID: 18456803](https://pubmed.ncbi.nlm.nih.gov/18456803/)): *"a LysR-type transcriptional regulator, CysB, directly activates the expression of sfnECR by binding to its upstream region. CysB is a master regulator that controls the sulfate starvation response."* The study further establishes a hierarchical CysB/SfnR regulatory system, in which downstream sulfur-scavenging operons are repressed by sulfate and by metabolites of the assimilatory pathway.

This regulatory context situates cysH physiologically: its expression is induced under sulfate/sulfur limitation, ramping up flux through the reductive assimilation route when the cell must scavenge and reduce inorganic sulfate to meet its demand for reduced sulfur.

---

## Mechanistic Model and Interpretation

### Position in the assimilatory sulfate reduction pathway

```
                          ATP    PPi           ATP   ADP
  Sulfate (SO4^2-)  ──────────────────►  APS  ──────────────►  PAPS
                        ATP sulfurylase          APS kinase        │
                          (CysN/CysD)             (CysC)           │ (sulfotransfer /
                                │                                  │  secondary metabolism)
                                │                                  ▼
                                │                          sulfated metabolites
                                │
                                ▼   *** cysH / PP_2328 / Q88KG2 ***
                        ┌───────────────────────────────────────────┐
                        │   APS REDUCTASE  (EC 1.8.4.10)             │
                        │   APS + Trx(red) → sulfite + AMP + Trx(ox) │
                        │   [4Fe-4S] cluster; Cys233 catalytic       │
                        └───────────────────────────────────────────┘
                                │  sulfite (SO3^2-)
                                ▼
                        Sulfite reductase (CysI/CysJ), NADPH
                                │  sulfide (S^2-)
                                ▼
                        O-acetylserine sulfhydrylase (CysK/CysM)
                                │
                                ▼
                          L-CYSTEINE ──► methionine, glutathione,
                                          Fe-S clusters, CoA, biotin ...
```

APS reductase is the **branch-point enzyme** that decides whether activated sulfate is committed to reduction (toward cysteine) or diverted (via PAPS) toward sulfotransfer reactions. In *P. putida*, cysH channels APS into the reductive branch.

### Catalytic cycle (two half-reactions)

```
  Step 1 (reductive sulfonyl transfer):
     E-Cys233-SH  +  APS  ──►  E-Cys233-S-SO3^-  +  AMP
     (nucleophilic attack on APS sulfate; thiosulfonate intermediate;
      [4Fe-4S] cluster + Lys144 orient/activate substrate, ~1000x rate boost)

  Step 2 (thioredoxin-mediated release):
     E-Cys233-S-SO3^-  +  Trx(SH)2  ──►  E-Cys233-SH  +  SO3^2-  +  Trx(S-S)

  Net:  APS + Trx(SH)2  ──►  sulfite + AMP + Trx(S-S)
```

The mobile C-terminal ~18 residues (bearing Cys233) shuttle the covalent intermediate between the APS-binding pocket (near the Fe–S cluster) and the surface where thioredoxin docks — physically separating the two chemistries in space and time.

### Comparison of key orthologs

| Property | *P. putida* KT2440 (Q88KG2) | *P. aeruginosa* PAO1 (O05927) | *M. tuberculosis* CysH | *E. coli* CysH |
|---|---|---|---|---|
| Enzyme class | APS reductase | APS reductase | APS reductase | **PAPS** reductase |
| Substrate | APS | APS | APS | PAPS |
| [4Fe-4S] cluster | Yes (inferred) | Yes (crystallographic) | Yes | No |
| Catalytic Cys | Cys233 (ECGLH) | conserved | conserved | conserved |
| Diagnostic C-term motifs | Present | Present | Present | Absent |
| Electron donor | Thioredoxin | Thioredoxin | Thioredoxin | Thioredoxin/glutaredoxin |
| Structural data | Homology (85.7% to PAO1) | 2.7 Å crystal structure | Spectroscopy/DFT | Crystal structure |
| Localization | Cytoplasm | Cytoplasm | Cytoplasm | Cytoplasm |

### Synthesis

The convergent picture is that Q88KG2 is a cytoplasmic, thioredoxin-dependent, iron–sulfur APS reductase that gates the reductive assimilation of sulfate in *P. putida*. Its function is highly specific — reduction of APS (not PAPS) to sulfite — and this specificity is enforced by the [4Fe-4S] cluster and active-site architecture. Physiologically, it is the committed step feeding sulfide into cysteine and downstream sulfur biochemistry, and it is transcriptionally tuned to sulfur availability through the CysB master regulator. Loss of function collapses de novo cysteine biosynthesis (auxotrophy) and causes accumulation of upstream intermediates (PAPS) that carry their own signaling consequences. Notably, the bacterial assimilatory APS reductase class is evolutionarily and structurally distinct from the unrelated **dissimilatory** APS reductase of sulfate-reducing/sulfur-oxidizing bacteria; the two arose by convergent evolution and should not be conflated.

---

## Evidence Base

| PMID | Study focus | How it supports the annotation |
|---|---|---|
| [10613872](https://pubmed.ncbi.nlm.nih.gov/10613872/) | New class of APS reductases in sulfate-assimilating bacteria (incl. *P. aeruginosa*) | **Direct ortholog:** purified Pseudomonas CysH reduces APS not PAPS (5.8 µmol·min⁻¹·mg⁻¹, thioredoxin donor); cysH knockout → cysteine auxotrophy |
| [17010373](https://pubmed.ncbi.nlm.nih.gov/17010373/) | 2.7 Å crystal structure of *P. aeruginosa* APS reductase | Establishes [4Fe-4S] cluster, tandem-Cys coordination, thiosulfonate intermediate, two-site/two-step mechanism, C-terminal flexibility (85.7% identical to Q88KG2) |
| [12072441](https://pubmed.ncbi.nlm.nih.gov/12072441/) | APS at a metabolic branch point in mycobacteria | Defines diagnostic C-terminal motifs (present in Q88KG2); CysH deletion → cys/met auxotroph; branch point centered on APS |
| [22023093](https://pubmed.ncbi.nlm.nih.gov/22023093/) | Fe-S cluster engineering & evolution of substrate specificity | Cluster enhances APS reduction ~1000-fold; drives substrate specificity and catalysis |
| [21075841](https://pubmed.ncbi.nlm.nih.gov/21075841/) | Spectroscopy of [4Fe-4S] cluster in *M. tuberculosis* APS reductase | Identifies essential Lys144 bridging Fe-S cluster and APS sulfate |
| [21678934](https://pubmed.ncbi.nlm.nih.gov/21678934/) | DFT + EXAFS of the [4Fe-4S] cluster | Cluster stays [4Fe-4S]²⁺; tandem-Cys coordination fine-tunes electronics; confirms Lys144 role |
| [18456803](https://pubmed.ncbi.nlm.nih.gov/18456803/) | CysB/SfnR regulation of sulfate starvation in *P. putida* | Places cysH in the CysB-controlled regulon (cysNC → cysH → cysI) |
| [19225840](https://pubmed.ncbi.nlm.nih.gov/19225840/) | *A. ferrooxidans* [Fe4S4] APS reductase | 28 kDa soluble protein; site-directed mutagenesis confirms four cluster-ligating cysteines |
| [17519237](https://pubmed.ncbi.nlm.nih.gov/17519237/) | Moss PpAPR-B, an APS reductase lacking Fe-S cluster | Shows Fe-S cluster is a rate/specificity determinant, not an absolute chemical requirement |
| [2180911](https://pubmed.ncbi.nlm.nih.gov/2180911/) | Thioredoxin/glutaredoxin essential for sulfate reduction in *E. coli* | Establishes thioredoxin as physiological electron donor for the sulfonucleotide reductase step |
| [9566743](https://pubmed.ncbi.nlm.nih.gov/9566743/) | APS reductase as a thioredoxin-superfamily enzyme (plants) | Supports thioredoxin-domain-dependent reduction of APS to sulfite |
| [24934621](https://pubmed.ncbi.nlm.nih.gov/24934621/), [27091548](https://pubmed.ncbi.nlm.nih.gov/27091548/) | PAPS accumulation as a signal in *E. coli* cysH mutants | Illustrate pathway architecture; consequences of blocking the branch point |
| [25710356](https://pubmed.ncbi.nlm.nih.gov/25710356/) | Fe-S–targeted APR inhibitors | APS reductase as a validated antibacterial/antitubercular drug target with no human homolog |

**Strength of evidence.** The core annotation (APS reductase, EC 1.8.4.10, thioredoxin-dependent, [4Fe-4S], cytoplasmic, committed step of sulfate assimilation) rests on a combination of (i) direct biochemical and genetic characterization of the 85.7%-identical *P. aeruginosa* ortholog, (ii) a high-resolution crystal structure of that ortholog, (iii) mechanistic/spectroscopic studies of closely related bacterial enzymes, and (iv) sequence-motif diagnostics applied directly to Q88KG2. This is a high-confidence, multi-modal evidence base. The only inferential steps specific to Q88KG2 itself are homology-based (structure, cluster, mechanism transferred from PAO1), which is well justified at 85.7% identity.

---

## Supported and Refuted Hypotheses

| Statement | Verdict | Basis |
|---|---|---|
| Q88KG2/cysH is an APS reductase (EC 1.8.4.10), not a PAPS reductase | **Supported** | Both APS-reductase signature motifs present; direct *P. aeruginosa* ortholog reduces APS not PAPS ([PMID: 10613872](https://pubmed.ncbi.nlm.nih.gov/10613872/), [PMID: 12072441](https://pubmed.ncbi.nlm.nih.gov/12072441/)) |
| Enzyme uses thioredoxin as electron donor | **Supported** | [PMID: 10613872](https://pubmed.ncbi.nlm.nih.gov/10613872/), [PMID: 2180911](https://pubmed.ncbi.nlm.nih.gov/2180911/), [PMID: 9566743](https://pubmed.ncbi.nlm.nih.gov/9566743/) |
| Enzyme contains an essential [4Fe-4S] cluster (CC…CXXC ligands) | **Supported** | Sequence motif Cys116/117…Cys205xxCys208; structure [PMID: 17010373](https://pubmed.ncbi.nlm.nih.gov/17010373/); [PMID: 22023093](https://pubmed.ncbi.nlm.nih.gov/22023093/) |
| Reaction proceeds via a covalent C-terminal-cysteine thiosulfonate intermediate | **Supported** | Trapped intermediate in crystal structure [PMID: 17010373](https://pubmed.ncbi.nlm.nih.gov/17010373/) |
| Cytoplasmic localization | **Supported (inferred)** | No signal/TM segment; soluble in all characterized orthologs |
| It functions in the *dissimilatory* (energy-conserving) sulfate pathway | **Refuted** | Assimilatory enzyme; dissimilatory APS reductase is a structurally unrelated enzyme ([PMID: 10613872](https://pubmed.ncbi.nlm.nih.gov/10613872/)) |

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 protein.** All enzymological, structural, and metallocofactor data derive from orthologs (*P. aeruginosa*, *M. tuberculosis*, *A. ferrooxidans*) and from sequence analysis. While the 85.7% identity to the crystallized *P. aeruginosa* enzyme makes transfer robust, kinetic constants (Kₘ, kcat), specific activity, and Fe–S cluster stoichiometry have not been measured for Q88KG2 directly. UniProt evidence level for the protein is inferred from homology.

2. **Residue-numbering caveats.** Some cited residue numbers (e.g., Lys144; Cys110/111/193/196 in *A. ferrooxidans*) are from orthologs of slightly different length. The functionally equivalent residues in Q88KG2 were mapped by motif alignment (Cys116/117, Cys205/208, Cys233), but a precise structural superposition of Q88KG2 has not been performed.

3. **Regulation inferred, not demonstrated, for PP_2328 specifically.** The CysB-controlled sulfate-starvation regulon in *P. putida* is documented, but direct promoter mapping or CysB-binding data for the PP_2328 promoter were not established.

4. **Electron-donor identity in vivo.** Thioredoxin is the demonstrated donor for the Pseudomonas ortholog and the *E. coli* system; whether glutaredoxin can substitute in *P. putida*, and which thioredoxin isoform is used, is unconfirmed for this organism.

5. **Quantitative flux/branch-point control.** The extent to which cysH is rate-limiting relative to CysNC and CysI under *P. putida* physiological conditions has not been measured.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymology of Q88KG2.** Express His-tagged PP_2328 in *E. coli*, purify anaerobically, and measure APS-vs-PAPS specificity, specific activity, Kₘ/kcat, pH optimum, and thioredoxin dependence — directly confirming the transferred annotation for the *P. putida* protein.

2. **Metallocofactor verification.** Use UV-visible/EPR spectroscopy and iron/sulfide quantitation to confirm a single [4Fe-4S]²⁺ cluster, and use site-directed mutagenesis of Cys116/117/205/208 to confirm cluster ligation and essentiality.

3. **Structural confirmation.** Solve or model (e.g., AlphaFold) the Q88KG2 structure and superpose onto the *P. aeruginosa* crystal structure to validate active-site residue positions (Cys233, the Lys144 equivalent) and C-terminal tail architecture.

4. **Genetic knockout in *P. putida* KT2440.** Construct a ΔPP_2328 strain and test for cysteine auxotrophy (growth on sulfate vs cysteine), complementation, and any PAPS-accumulation phenotypes analogous to *E. coli*.

5. **Promoter/regulation analysis.** Perform RT-qPCR or reporter assays under sulfate-replete vs sulfate-starved conditions, and EMSA/ChIP for CysB binding at the PP_2328 promoter, to confirm membership in the CysB regulon.

6. **Electron-donor mapping.** Test *P. putida* thioredoxin and glutaredoxin isoforms as reductants in vitro to determine the physiological donor.

---

## Conclusion

*Pseudomonas putida* KT2440 **cysH** (PP_2328, Q88KG2) encodes a cytoplasmic, thioredoxin-dependent **adenosine-5′-phosphosulfate reductase** (EC 1.8.4.10) that catalyzes the reduction of APS to sulfite plus AMP — the first committed and rate-controlling reductive step of assimilatory sulfate reduction and the branch point that channels activated sulfate toward cysteine, methionine, and downstream reduced-sulfur biochemistry. The enzyme is specific for APS over PAPS, uses an essential tandem-cysteine-coordinated [4Fe-4S] cluster that boosts catalysis ~1000-fold and dictates specificity, and operates via a covalent C-terminal-cysteine (Cys233) thiosulfonate intermediate resolved by thioredoxin. This annotation is supported by diagnostic sequence motifs in Q88KG2, by 85.7% identity to the crystallographically and biochemically characterized *P. aeruginosa* ortholog, and by the CysB-regulated genetic organization of the sulfate-assimilation pathway in *P. putida*.


## Artifacts

- [OpenScientist final report](cysH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cysH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12072441
2. PMID:10613872
3. PMID:2180911
4. PMID:9566743
5. PMID:17010373
6. PMID:22023093
7. PMID:21678934
8. PMID:19225840
9. PMID:17519237
10. PMID:21075841
11. PMID:24934621
12. PMID:27091548
13. PMID:39153279
14. PMID:18456803