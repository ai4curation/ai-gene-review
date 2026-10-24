---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:15:59.590312'
end_time: '2026-09-01T10:46:10.220799'
duration_seconds: 1810.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pdxJ
  gene_symbol: pdxJ
  uniprot_accession: Q88MY2
  protein_description: 'RecName: Full=Pyridoxine 5''-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00279};
    Short=PNP synthase {ECO:0000255|HAMAP-Rule:MF_00279}; EC=2.6.99.2 {ECO:0000255|HAMAP-Rule:MF_00279};'
  gene_info: Name=pdxJ {ECO:0000255|HAMAP-Rule:MF_00279}; OrderedLocusNames=PP_1436;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PNP synthase family. {ECO:0000255|HAMAP-
  protein_domains: Aldolase_TIM. (IPR013785); PyrdxlP_synth_PdxJ. (IPR004569); Pyridoxine-5'_phos_synth.
    (IPR036130); PdxJ (PF03740)
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
  path: pdxJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pdxJ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MY2
- **Protein Description:** RecName: Full=Pyridoxine 5'-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00279}; Short=PNP synthase {ECO:0000255|HAMAP-Rule:MF_00279}; EC=2.6.99.2 {ECO:0000255|HAMAP-Rule:MF_00279};
- **Gene Information:** Name=pdxJ {ECO:0000255|HAMAP-Rule:MF_00279}; OrderedLocusNames=PP_1436;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PNP synthase family. {ECO:0000255|HAMAP-
- **Key Domains:** Aldolase_TIM. (IPR013785); PyrdxlP_synth_PdxJ. (IPR004569); Pyridoxine-5'_phos_synth. (IPR036130); PdxJ (PF03740)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pdxJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pdxJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pdxJ** (gene ID: pdxJ, UniProt: Q88MY2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pdxJ* (Q88MY2) — Pyridoxine 5′-Phosphate Synthase of *Pseudomonas putida* KT2440

**UniProt:** Q88MY2 · **Gene:** pdxJ (PP_1436) · **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
**EC:** 2.6.99.2 · **Family:** PNP synthase family (HAMAP MF_00279) · **Fold/domains:** Aldolase TIM-barrel (IPR013785), PdxJ (PF03740, IPR004569, IPR036130)

---

## Summary

The gene **pdxJ** (ordered locus **PP_1436**; UniProt **Q88MY2**) of *Pseudomonas putida* strain KT2440 encodes **pyridoxine 5′-phosphate synthase (PNP synthase; EC 2.6.99.2)**, the enzyme that catalyzes the final, committed ring-closure step of the *de novo* biosynthesis of vitamin B6. This identity was verified against every criterion supplied in the research brief: the gene symbol, EC number, protein family (PNP synthase family, HAMAP rule MF_00279), and diagnostic domains (Aldolase_TIM IPR013785; PyrdxlP_synth_PdxJ IPR004569; PdxJ PF03740) all align consistently, and the organism is the correctly identified γ-proteobacterium *P. putida* KT2440. There is **no gene-symbol ambiguity**: the literature for PdxJ/PNP synthase describes exactly this enzymatic activity, and the family/domain signatures match the biochemically and structurally characterized orthologs.

PdxJ catalyzes an intramolecular ring-closure condensation between two phosphorylated substrates — **1-deoxy-D-xylulose 5-phosphate (DXP)** and **3-amino-2-oxopropyl phosphate (1-amino-acetone-3-phosphate; supplied by the partner enzyme PdxA from 4-phosphohydroxy-L-threonine)** — assembling the aromatic pyridine ring to yield **pyridoxine 5′-phosphate (PNP) + inorganic phosphate + 2 H₂O + H⁺**. PNP is the first true B6 vitamer produced *de novo*; it is subsequently oxidized by PdxH (PNP/PMP oxidase) to **pyridoxal 5′-phosphate (PLP)**, the catalytically active cofactor used by more than a hundred distinct enzymes. The enzyme is a soluble, **cytoplasmic homooctamer** in which each subunit folds into a single (β/α)₈ **TIM-barrel**, with active sites shared between neighboring monomers.

No experimental study directly characterizes the *P. putida* KT2440 protein itself, but the functional assignment is exceptionally well supported by convergent evidence from close orthologs and from bioinformatic/structural analysis of Q88MY2 specifically: (i) direct *in vitro* enzymology on the *E. coli* enzyme establishing substrates and product; (ii) multiple ligand-bound crystal structures of the *E. coli* ortholog defining the catalytic mechanism; (iii) 63% pairwise sequence identity to *E. coli* PdxJ with a fully conserved catalytic triad (His48/Glu75/His196); (iv) a very-high-confidence AlphaFold model (mean pLDDT 96.3) that superposes onto experimental *E. coli* PdxJ at 2.06 Å Cα RMSD; and (v) conserved *rnc–era–recO–pdxJ* genomic synteny.

---

## Key Findings

### 1. pdxJ encodes pyridoxine 5′-phosphate synthase (EC 2.6.99.2), catalyzing the final ring-closure of de novo vitamin B6 biosynthesis

The primary function of the *pdxJ* product is enzymatic: it is **pyridoxine 5′-phosphate synthase**, performing the last step of the *de novo* vitamin B6 pathway — a complex, multistep intramolecular ring-closure condensation of two phosphorylated substrates. Direct enzymatic characterization of the *E. coli* ortholog by Laber and colleagues established the true substrates and product. The sugar substrate is **1-deoxy-D-xylulose 5-phosphate (DXP)** — not the previously assumed non-phosphorylated 1-deoxy-D-xylulose — and the amino substrate is **1-amino-acetone-3-phosphate (3-amino-2-oxopropyl phosphate)**, produced by PdxA from 4-phosphohydroxy-L-threonine. Radiolabel from [2-¹⁴C]DXP was incorporated into the product, confirming DXP as the direct carbon donor, and the first vitamin B6 vitamer synthesized *de novo* is the phosphorylated form **PNP**, not free pyridoxine. As stated in the study: *"The sugar used as substrate by PdxJ is 1-deoxy-D-xylulose-5-phosphate rather than the previously assumed 1-deoxy-D-xylulose. The first vitamin B6 vitamer synthesised is PNP, and not pyridoxine"* ([PMID: 10225425](https://pubmed.ncbi.nlm.nih.gov/10225425/)).

The overall balanced reaction, as annotated for Q88MY2 under EC 2.6.99.2, is:

> **3-amino-2-oxopropyl phosphate + 1-deoxy-D-xylulose 5-phosphate → pyridoxine 5′-phosphate + phosphate + 2 H₂O + H⁺**

Garrido-Franco and colleagues described the enzyme directly as *"the last enzyme in the de novo biosynthesis of vitamin B(6) catalyzing the complicated ring-closure reaction between 1-deoxy-D-xylulose-5-phosphate and 1-amino-acetone-3-phosphate"* ([PMID: 12206776](https://pubmed.ncbi.nlm.nih.gov/12206776/)). Q88MY2 carries the EC 2.6.99.2 annotation and belongs to the PNP synthase family (HAMAP MF_00279). Because *P. putida* KT2440 is a γ-proteobacterium — the exact taxonomic group in which the DXP-dependent PdxA/PdxJ pathway operates — this functional assignment transfers with high confidence.

### 2. PdxJ is a homooctameric TIM-barrel enzyme with shared active sites and a two-phosphate-site, water-relay mechanism

The architecture and mechanism of PNP synthase are well established from crystallographic studies of the *E. coli* ortholog. Each monomer is a single compact (β/α)₈ **TIM-barrel** domain: *"The monomer of PNP synthase consists of one compact domain that adopts the abundant TIM barrel fold"* ([PMID: 11286891](https://pubmed.ncbi.nlm.nih.gov/11286891/)). The biological assembly is a **homooctamer** — a tetramer of symmetric dimers with 422 symmetry — and the active sites are **shared between partner monomers** (e.g., Arg20 of one subunit contributes to substrate binding in its neighbor's active site). This inter-subunit active-site architecture makes the octameric quaternary structure functionally essential.

Ligand-complex structures dissected the mechanism in detail: two phosphate-binding subsites of distinct affinity accommodate the two phosphorylated substrates, a Schiff-base (imine) intermediate forms with the amino substrate, and a dedicated water-relay system channels reaction waters out of the closed active site — *"The most important mechanistic features are the presence of two phosphate-binding sites with distinct affinities and the existence of a water relay system for the release of reaction water molecules"* ([PMID: 12206776](https://pubmed.ncbi.nlm.nih.gov/12206776/)). Catalysis is coupled to an open→closed transition of a C-terminal flexible loop that closes only when both substrates are bound, sequestering the chemistry from bulk solvent. A high-resolution (1.96 Å) DXP complex captured multiple binding states across the eight sites: *"The octameric enzyme possesses eight distinct binding sites, and three different binding states are observed"* ([PMID: 12269807](https://pubmed.ncbi.nlm.nih.gov/12269807/)).

### 3. Sequence-level evidence for Q88MY2: 63% identity to E. coli PdxJ with a fully conserved catalytic triad and substrate-binding residues

Direct bioinformatic analysis of the target anchors the functional transfer. A pairwise global (Needleman–Wunsch) alignment of Q88MY2 (246 aa) against *E. coli* PdxJ (P0A794, 243 aa) yields **63.4% identity** (154 identical residues over 243 aligned columns) — far above the ~30–40% threshold at which enzyme function is typically conserved, indicating strict orthology. Every catalytic/binding residue defined in *E. coli* maps to a conserved position in Q88MY2 (E. coli D11→D14, R20→R23, E72→E75, H193→H196).

The UniProt/HAMAP (MF_00279) feature table for Q88MY2 specifies the catalytic machinery explicitly:

| Functional role | Q88MY2 residue(s) |
|---|---|
| Proton acceptors (catalytic) | His48, Glu75 |
| Proton donor (catalytic) | His196 |
| Transition-state stabilizer | Glu156 |
| DXP binding | Asp14–His15, Arg50, His55, Thr105 |
| 3-amino-2-oxopropyl phosphate binding | Asn12, Arg23, Gly197, Gly218–His219 |

The pathway annotation places PdxJ at **step 5 of 5** in "pyridoxine 5′-phosphate biosynthesis from D-erythrose 4-phosphate," the subunit field confirms the **homooctamer (tetramer of dimers)**, and the subcellular-localization keyword is **Cytoplasm** — each consistent with the experimentally characterized orthologs. This confirms Q88MY2 is a genuine, catalytically competent PNP synthase rather than a divergent paralog.

### 4. PP_1436 lies in a conserved rnc–era–recO–pdxJ neighborhood, is not linked to pdxA, and maps to KEGG module M00124

Genomic-context analysis independently corroborates that PP_1436 is authentic *pdxJ*. KEGG assigns **ppu:PP_1436** the orthology **K03474** (pyridoxine 5′-phosphate synthase, EC 2.6.99.2), pathways **ppu00750** (Vitamin B6 metabolism) and **ppu01240** (Biosynthesis of cofactors), and module **M00124** (Pyridoxal phosphate biosynthesis, erythrose-4P ⇒ pyridoxal-P). The gene occupies genome position 1,636,551–1,637,291 (741 bp, 246 aa, GTG start codon).

In the KT2440 chromosome, *pdxJ* (PP_1436, + strand) lies only ~44 bp downstream of, and on the same strand as, ***recO*** (PP_1435, DNA-repair), which is itself preceded by ***era*** (PP_1434, an essential GTPase) and ***rnc*** (PP_1433, RNase III). This **rnc–era–recO–pdxJ** arrangement is a conserved gene neighborhood also found in *E. coli* and other γ-proteobacteria — a deep evolutionary signal supporting the identity of PP_1436. Notably, ***pdxA* is not adjacent** to *pdxJ* (the downstream gene, PP_1437, is an unrelated heavy-metal two-component sensor kinase on the opposite strand). The two sequential pathway enzymes are transcribed independently, giving no genomic evidence for a stable PdxA–PdxJ channeling complex.

### 5. The AlphaFold model of Q88MY2 is very high confidence and superposes onto experimental E. coli PdxJ at 2.06 Å

Structural bioinformatics closes the loop between sequence and experimentally verified fold. The AlphaFold DB model **AF-Q88MY2-F1** has a global mean **pLDDT of 96.3** ("very high"): 93.1% of residues exceed pLDDT 90, 98.0% exceed 70, and only the five disordered N-terminal residues fall below 70. Every annotated catalytic and substrate-binding residue is modeled with very high confidence (pLDDT 84.6–98.9), including His48 (98.7), Glu75 (98.8), His196 (98.3), Glu156 (98.9), Asp14 (98.8), Arg50 (96.3), His55 (98.1), Thr105 (84.6), Asn12 (98.9), Arg23 (98.3), Gly197 (98.2), and His219 (98.8).

A rigid-body (Kabsch) superposition of the AlphaFold model onto the experimental *E. coli* PdxJ crystal structure (**PDB 1M5W**, the DXP complex, 63.2% sequence identity) over all 242 aligned Cα atoms gives an **RMSD of 2.06 Å**, with 95% of residues < 2 Å and 97% < 3 Å after superposition. As a negative control, superposition onto an unrelated protein (PDB 1B4X, aspartate aminotransferase) gave ~17.8 Å, confirming the low RMSD is specific. This is direct structural evidence that Q88MY2 independently adopts the (β/α)₈ TIM-barrel PdxJ scaffold with a spatially conserved active site.

---

## Mechanistic Model / Interpretation

PdxJ is the terminal biosynthetic node that funnels central-metabolism precursors into the vitamin B6 cofactor supply of the cell. The DXP-dependent pathway can be summarized as two converging branches whose products are joined by PdxJ:

```
 Branch 1 (amino/aza donor):
   D-erythrose 4-phosphate --Epd/PdxB/SerC--> ... --PdxA--> 3-amino-2-oxopropyl phosphate
                                                            (1-amino-acetone-3-phosphate)
                                                                      |
 Branch 2 (sugar/carbon donor):                                       v
   pyruvate + G3P --Dxs--> 1-deoxy-D-xylulose 5-phosphate (DXP)       |
                                                        \             |
                                                         v            v
                             +--------------------------------------------+
                             |   PdxJ  (PP_1436, Q88MY2)                  |
                             |   PNP synthase, EC 2.6.99.2                |
                             |   homooctameric (β/α)8 TIM-barrel · cytosol|
                             +--------------------------------------------+
                                                    |
                                                    v
                          Pyridoxine 5'-phosphate (PNP) + Pi + 2 H2O + H+
                                                    |
                                              --PdxH (oxidase)-->
                                                    v
                             Pyridoxal 5'-phosphate (PLP) = active cofactor
```

Within the octameric assembly, each of the eight (β/α)₈ TIM-barrel subunits contributes to a shared active site with its neighbor. Catalysis proceeds through binding of both phosphorylated substrates at two phosphate subsites of distinct affinity, formation of a Schiff-base intermediate with the amino substrate, a series of dehydration/aromatization steps that construct the pyridine ring, and expulsion of reaction waters via a dedicated water-relay channel — a process gated by closure of the C-terminal loop that occurs only when both substrates are present. The product PNP is released and handed off to PdxH for the final oxidation to PLP.

The biological significance of this single step is large relative to its metabolic footprint: PLP is a required cofactor for a broad swath of enzymes (transaminases, decarboxylases, racemases, and many others), so loss of PdxJ renders the cell a pyridoxine auxotroph. Because the PdxA/PdxJ route is confined to γ-proteobacteria and entirely absent from humans, PdxJ has long been discussed as a candidate antimicrobial drug target ([PMID: 12686115](https://pubmed.ncbi.nlm.nih.gov/12686115/)).

The convergence of evidence for Q88MY2 is worth underscoring. Three independent modalities — sequence (63% identity, conserved catalytic triad), genomic context (conserved *rnc–era–recO–pdxJ* synteny; correct KEGG module), and structure (pLDDT 96 AlphaFold model superposing on experimental PdxJ at 2.06 Å) — all point to the same conclusion. This is the strongest form of functional inference available in the absence of a direct biochemical assay on the *P. putida* protein.

### Localization

PdxJ is a **soluble cytoplasmic enzyme** (UniProt Q88MY2 subcellular keyword: *Cytoplasm*). Its substrates and product are phosphorylated, membrane-impermeant small metabolites; it carries no signal peptide or transmembrane segment and functions as a cytosolic oligomer, consistent with all crystallized orthologs being soluble proteins. It performs its reaction in the cytoplasm in coordination with the other soluble Pdx pathway enzymes.

---

## Evidence Base

| PMID | Study (abbrev.) | How it supports the annotation |
|---|---|---|
| [10225425](https://pubmed.ncbi.nlm.nih.gov/10225425/) | Formation of PNP from 4-PHT and DXP by PdxA and PdxJ | **Primary enzymology.** Establishes DXP (not deoxyxylulose) as the sugar substrate and PNP (not free pyridoxine) as the product; defines substrate specificity. |
| [12206776](https://pubmed.ncbi.nlm.nih.gov/12206776/) | Enzyme-ligand complexes of PNP synthase | **Primary structure/mechanism.** Defines the two substrates, the ring-closure reaction, two phosphate sites, and the water-relay mechanism. |
| [11286891](https://pubmed.ncbi.nlm.nih.gov/11286891/) | Structural basis for the function of PNP synthase | **Primary structure.** Establishes the (β/α)₈ TIM-barrel monomer and homooctamer with shared active sites. |
| [12269807](https://pubmed.ncbi.nlm.nih.gov/12269807/) | Multistate binding in PNP synthase (1.96 Å DXP complex) | **Primary structure.** Confirms octameric quaternary structure and multistate substrate binding across eight sites. |
| [17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/) | Two independent routes of de novo B6 biosynthesis | **Authoritative review.** Defines the DXP-dependent pathway and PdxJ's concerted action with PdxA. |
| [11200221](https://pubmed.ncbi.nlm.nih.gov/11200221/) | Phylogenetic/comparative genomics of B6 pathways | **Comparative genomics.** Places PdxA/PdxJ in γ-proteobacteria (the clade containing *P. putida*). |
| [15094056](https://pubmed.ncbi.nlm.nih.gov/15094056/) | Functional complementation of E. coli pdxJ by PDX1 | **Genetic evidence.** Confirms *pdxJ* function via restoration of pyridoxine prototrophy; establishes the ring-synthesis role. |
| [12686115](https://pubmed.ncbi.nlm.nih.gov/12686115/) | PNP synthase: de novo synthesis of B6 and beyond | **Review.** Summarizes PNP synthase as the key pdx-group enzyme catalyzing multistep ring closure to PNP + Pi; notes drug-target relevance. |
| [17217963](https://pubmed.ncbi.nlm.nih.gov/17217963/) | Structure of erythronate-4-phosphate dehydrogenase (PdxB), *P. aeruginosa* | **Pathway context.** Structural characterization of an upstream *Pseudomonas* pathway enzyme, reinforcing that the PdxA/PdxJ route operates in this genus. |
| [10430950](https://pubmed.ncbi.nlm.nih.gov/10430950/) | A highly conserved gene (SOR1) in de novo B6 biosynthesis | **Pathway divergence.** Documents the mutually exclusive alternative (SOR1/Pdx1) pathway, clarifying why PdxJ is diagnostic of the γ-proteobacterial route. |

The evidence base is internally consistent. Primary enzymology and crystallography (on the *E. coli* ortholog) define the reaction and mechanism; comparative-genomics and review literature place the pathway in the correct taxonomic clade; and bioinformatic/structural analysis of Q88MY2 itself (63% identity, conserved catalytic residues, AlphaFold 2.06 Å superposition, conserved synteny) transfers those conclusions to the *P. putida* protein. No paper in the set contradicts the annotation.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the P. putida KT2440 protein.** All enzymatic and structural data derive from orthologs, principally *E. coli*. There is no published *in vitro* kinetic assay, crystal structure, or genetic knockout specifically for Q88MY2 / PP_1436. The assignment rests on homology transfer plus bioinformatic/structural inference — robust for such a highly conserved housekeeping enzyme, but not a direct assay.

2. **Kinetic parameters are unknown.** Substrate affinities (Kₘ for DXP and for 3-amino-2-oxopropyl phosphate), turnover number (k_cat), and any regulatory behavior have not been measured for Q88MY2.

3. **Structural evidence is predictive, not experimental.** The 2.06 Å superposition is between an AlphaFold model and an experimental *E. coli* structure; no experimental structure of Q88MY2 exists, and the loop dynamics of this ortholog have not been observed directly.

4. **Regulation and essentiality in P. putida are uncharacterized.** Transcriptional control of B6 biosynthesis in KT2440, flux under different conditions, and *pdxJ* essentiality versus salvage of environmental pyridoxine/pyridoxal have not been established.

5. **Partner-enzyme relationship is inferred.** PdxA and PdxJ act sequentially and are both cytoplasmic, but they are not operonically linked and no physical PdxA–PdxJ complex or substrate channeling was demonstrated.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_1436, purify Q88MY2, and measure PNP synthase activity directly (coupled spectrophotometric assay via PdxH, or LC-MS detection of PNP) with DXP and 3-amino-2-oxopropyl phosphate. Determine Kₘ and k_cat for both substrates to confirm specificity quantitatively.

2. **Genetic essentiality / auxotrophy test.** Construct a *pdxJ* deletion in KT2440 and test for pyridoxine auxotrophy (rescue by pyridoxine/pyridoxal), confirming the *de novo* role and distinguishing it from salvage.

3. **Cross-species complementation.** Test whether PP_1436 restores pyridoxine prototrophy to an *E. coli pdxJ* mutant — a direct functional confirmation analogous to [PMID: 15094056](https://pubmed.ncbi.nlm.nih.gov/15094056/).

4. **Experimental structure determination.** Solve the crystal or cryo-EM structure of Q88MY2, ideally with DXP and/or a substrate analog, to validate the AlphaFold prediction and capture catalytic-loop states directly.

5. **Quaternary-structure verification.** Confirm the predicted homooctamer in solution by SEC-MALS or analytical ultracentrifugation.

6. **Pathway/regulation profiling.** Use transcriptomics or reporter assays to determine how the B6 biosynthesis genes (*pdxJ*, *pdxA*, *pdxB*, *pdxH*) are regulated in KT2440 under B6-replete versus B6-limited conditions.

---

*Verification note:* The gene symbol **pdxJ**, EC number (2.6.99.2), protein family (PNP synthase family, HAMAP MF_00279), and domain signatures (Aldolase_TIM IPR013785; PyrdxlP_synth_PdxJ IPR004569; PdxJ PF03740) supplied in the UniProt record are mutually consistent and match the biochemically/structurally characterized PdxJ/PNP synthase family throughout the literature. The organism was confirmed as the γ-proteobacterium *Pseudomonas putida* KT2440, the correct clade for the DXP-dependent (PdxA/PdxJ) pathway. There is **no** gene-symbol ambiguity or misassignment.


## Artifacts

- [OpenScientist final report](pdxJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pdxJ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10225425
2. PMID:12206776
3. PMID:11286891
4. PMID:12269807
5. PMID:12686115
6. PMID:15094056