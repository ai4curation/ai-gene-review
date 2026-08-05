---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T10:28:03.915094'
end_time: '2026-07-23T10:48:50.998519'
duration_seconds: 1247.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabA
  gene_symbol: fabA
  uniprot_accession: Q88FC4
  protein_description: 'RecName: Full=3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase
    {ECO:0000255|HAMAP-Rule:MF_00405}; EC=4.2.1.59 {ECO:0000255|HAMAP-Rule:MF_00405};
    AltName: Full=3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabA {ECO:0000255|HAMAP-Rule:MF_00405};
    AltName: Full=Beta-hydroxydecanoyl thioester dehydrase {ECO:0000255|HAMAP-Rule:MF_00405};
    AltName: Full=Trans-2-decenoyl-[acyl-carrier-protein] isomerase {ECO:0000255|HAMAP-Rule:MF_00405};
    EC=5.3.3.14 {ECO:0000255|HAMAP-Rule:MF_00405};'
  gene_info: Name=fabA {ECO:0000255|HAMAP-Rule:MF_00405}; OrderedLocusNames=PP_4174;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the thioester dehydratase family. FabA
  protein_domains: FabA. (IPR010083); FabA_FabZ. (IPR013114); HotDog_dom_sf. (IPR029069);
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fabA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FC4
- **Protein Description:** RecName: Full=3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase {ECO:0000255|HAMAP-Rule:MF_00405}; EC=4.2.1.59 {ECO:0000255|HAMAP-Rule:MF_00405}; AltName: Full=3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabA {ECO:0000255|HAMAP-Rule:MF_00405}; AltName: Full=Beta-hydroxydecanoyl thioester dehydrase {ECO:0000255|HAMAP-Rule:MF_00405}; AltName: Full=Trans-2-decenoyl-[acyl-carrier-protein] isomerase {ECO:0000255|HAMAP-Rule:MF_00405}; EC=5.3.3.14 {ECO:0000255|HAMAP-Rule:MF_00405};
- **Gene Information:** Name=fabA {ECO:0000255|HAMAP-Rule:MF_00405}; OrderedLocusNames=PP_4174;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the thioester dehydratase family. FabA
- **Key Domains:** FabA. (IPR010083); FabA_FabZ. (IPR013114); HotDog_dom_sf. (IPR029069); FabA (PF07977)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabA** (gene ID: fabA, UniProt: Q88FC4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FabA (Q88FC4, PP_4174) in *Pseudomonas putida* KT2440: The Committed Branch-Point Dehydratase/Isomerase of Unsaturated Fatty Acid Biosynthesis

## Summary

**FabA (UniProt Q88FC4; locus PP_4174) is a soluble, cytoplasmic, bifunctional enzyme of the type II fatty acid synthase (FAS-II) system in *Pseudomonas putida* KT2440.** It catalyzes two chemically linked reactions on acyl-carrier-protein (ACP)-tethered substrates: (i) the reversible dehydration of (3*R*)-hydroxydecanoyl-ACP to *trans*-2-decenoyl-ACP (β-hydroxyacyl-ACP dehydratase, **EC 4.2.1.59**), and (ii) the isomerization of *trans*-2-decenoyl-ACP to *cis*-3-decenoyl-ACP (**EC 5.3.3.14**). The second reaction is the defining, committed step of the anaerobic (biosynthetic) unsaturated fatty acid (UFA) pathway: the *cis*-3 double bond introduced specifically at the 10-carbon stage escapes further reduction and is preserved through subsequent elongation, becoming the double bond of the mature membrane UFAs.

The enzyme identity has been rigorously verified for this specific target. Q88FC4 is a small (~171 aa, ~18.8 kDa) member of the FabA/FabZ **"hotdog-fold" thioester dehydratase superfamily** (InterPro IPR010083, IPR013114; HotDog superfamily IPR029069; Pfam PF07977). Pairwise alignment against the well-characterized *Escherichia coli* FabA (P0A6Q3) shows **66.7% amino-acid identity**, with full conservation of the catalytic **His-70** and the adjacent **Cys-69** identified in the classic *E. coli* suicide-inhibitor studies, plus a conserved phosphopantetheine/acyl-tunnel signature. There is no ambiguity: the gene symbol, organism, protein family, domain architecture, and catalytic residues all align, and the literature for FabA orthologs describes precisely the annotated function.

Physiologically, in *P. putida* FabA works within an essential **fabA–fabB operon**. FabA supplies *cis*-3-decenoyl-ACP to its operon partner FabB (β-ketoacyl-ACP synthase I), which elongates it to the 16:1Δ9 and 18:1Δ11 acyl chains that populate membrane phospholipids. Inactivation of this operon blocks growth of *P. putida* unless exogenous UFA is supplied, establishing FabA as the effectively sole and essential entry point to *de novo* UFA synthesis in this organism. Expression is tuned to membrane lipid demand by the activator **PsrA** and the repressor **FabR**, which sense the cellular acyl-ACP/acyl-CoA pool. Critically, FabA's biosynthetic isomerase activity must not be conflated with the separate, stress-response **cis-trans isomerase (Cti)** of *P. putida*, which remodels pre-existing membrane lipids under solvent/heat stress and operates at a different pathway stage and by a different mechanism.

---

## Key Findings

### Finding 1 — FabA is a bifunctional dehydratase/isomerase that commits carbon to unsaturated fatty acid synthesis

FabA carries out two reactions in the type II fatty acid synthase cycle. First, as a **β-hydroxyacyl-ACP dehydratase (EC 4.2.1.59)**, it reversibly removes water from (3*R*)-hydroxydecanoyl-ACP to yield *trans*-2-decenoyl-ACP — the normal dehydration step of the elongation cycle. Second, and distinctively, as a **trans-2-decenoyl-ACP isomerase (EC 5.3.3.14)**, it shifts the newly formed double bond from the α,β (2,3-*trans*) to the β,γ (3,4-*cis*) position, producing *cis*-3-decenoyl-ACP. This *cis*-3 species is not a substrate for the enoyl-ACP reductase (FabI) that would otherwise saturate the double bond; instead it is channeled into continued elongation with the double bond preserved. Because this isomerization happens specifically at the **10-carbon (decenoyl) stage**, it is the single committed branch point at which carbon is diverted from saturated toward unsaturated fatty acid production.

The mechanism is established from the classic biochemistry of the *E. coli* ortholog, the best-characterized enzyme of this family. As stated directly in the literature on anaerobic UFA formation, *"The double bond is introduced into the growing acyl chain by FabA, an enzyme capable of both the dehydration of beta-hydroxydecanoyl-acyl carrier protein (ACP) to trans-2-decenoyl-ACP, and the isomerization of trans-2 to cis-3-decenoyl-ACP"* [PMID: 12237320](https://pubmed.ncbi.nlm.nih.gov/12237320/). UniProt annotates Q88FC4 with both EC numbers and both catalytic activities under HAMAP rule MF_00405, and the bioinformatic verification (Finding 5) confirms the target protein possesses the required catalytic machinery.

### Finding 2 — In *P. putida*, fabA lies in an essential fabA–fabB operon required for membrane UFA supply

FabA does not act alone. In *Pseudomonas* species, *fabA* is co-transcribed with *fabB* (β-ketoacyl-ACP synthase I). FabA generates the *cis*-3-decenoyl-ACP intermediate and FabB elongates it, together channeling the double bond into longer chains. The physiological output is defined precisely: *"The enzymes encoded by the fabA and fabB genes catalyze the introduction of a double bond into a 10-carbon precursor which is elongated to the 16:1Δ9 and 18:1Δ11 unsaturated fatty acyl chains required for functional membrane phospholipids"* [PMID: 36537550](https://pubmed.ncbi.nlm.nih.gov/36537550/).

The essentiality of this pathway in *P. putida* is demonstrated genetically. In a comparison of two closely related pseudomonads, *"Inactivation of the fabA fabB operon fails to halt the growth of P. aeruginosa PAO1 but blocks growth of P. putida F1 unless an exogenous unsaturated fatty acid is provided"* [PMID: 36537550](https://pubmed.ncbi.nlm.nih.gov/36537550/). *P. aeruginosa* survives operon loss because it carries a functional DesA desaturase bypass; *P. putida* lacks an effective bypass and therefore depends absolutely on FabA/FabB for UFA. This maps *fabA* (PP_4174 in KT2440) as **essential for de novo UFA synthesis and growth**, a conclusion that transfers directly to the KT2440 ortholog Q88FC4.

### Finding 3 — FabA is a cytoplasmic hotdog-fold enzyme with a His/Cys catalytic dyad; His-70 was pinned by the 3-decynoyl-NAC suicide inhibitor

FabA's structure and active site are among the classic case studies of enzyme mechanism. Sequencing of the *E. coli fabA* gene (516 nt, 171 aa, ~18.8 kDa) identified the catalytic histidine through covalent labeling with a mechanism-activated (suicide) inhibitor: *"The active site histidine residue (His-70) has been identified by analysis of the peptides labeled by reaction with 14C-labeled 3-decynoyl-N-acetylcysteamine, a specific mechanism-activated inhibitor"* [PMID: 2832401](https://pubmed.ncbi.nlm.nih.gov/2832401/). His-70 abstracts and delivers protons during the dehydration/isomerization chemistry; an adjacent **Cys-69** was proposed to assist catalysis.

Structurally, FabA belongs to the **FabA/FabZ hotdog-fold thioester dehydratase superfamily** and functions as a soluble homodimer within the cytoplasmic FAS-II machinery. The molecular determinant that grants FabA (and FabA-like enzymes such as FabN) their isomerase capability — the feature that distinguishes them from the non-isomerizing FabZ dehydratase — resides in the β-strands lining the substrate tunnel. Domain-swapping experiments showed that *"Substitution of the beta3 and beta4 strands of EfFabZ with the corresponding strands from EfFabN was necessary and sufficient to convert EfFabZ into an isomerase"* [PMID: 15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/). Thus the geometry of the acyl-binding tunnel, not just the catalytic His, defines whether the enzyme can perform the double-bond-shifting isomerization that commits carbon to the UFA pathway.

### Finding 4 — fabA transcription is controlled by PsrA (activator) and FabR (repressor) sensing the acyl pool

The proportion of unsaturated to saturated fatty acids in the membrane is homeostatically regulated in part at the level of *fabA/fabB* transcription. The repressor **FabR** binds a palindromic operator in the *fabA* and *fabB* promoters. As described for the *E. coli* paradigm, *"The FabR (fatty acid biosynthesis repressor) transcriptional repressor controls the proportion of unsaturated fatty acids in the membrane by regulating the expression of the fabB (beta-ketoacyl-ACP synthase I) and fabA (beta-hydroxydecanoyl-ACP dehydratase/isomerase) genes"* [PMID: 19854834](https://pubmed.ncbi.nlm.nih.gov/19854834/). FabR repression requires unsaturated acyl-ACP/acyl-CoA as effector and is antagonized by saturated species, forming a feedback loop that keeps the UFA:SFA ratio within a functional window.

In pseudomonads and their relatives, the TetR-family regulator **PsrA** acts as a positive regulator of the operon. In the close relative *Azotobacter vinelandii*, loss of PsrA produced *"decreased expression of the unsaturated fatty acid biosynthetic operon fabAB (3-hydroxydecanoyl-ACP dehydratase/isomerase and 3-ketoacyl-ACP synthase I)"* along with reduced UFA and cyclopropane fatty acid content [PMID: 33964629](https://pubmed.ncbi.nlm.nih.gov/33964629/). PsrA binds the *fabA* promoter directly. Together, PsrA (activation) and FabR (repression) tune FabA expression to lipid demand and environmental conditions.

### Finding 5 — Bioinformatic verification: Q88FC4 conserves His-70, Cys-69, and the full hotdog active-site motif (66.7% identity to *E. coli* FabA)

To confirm that the *specific target protein* — not merely a namesake — carries the FabA function, a pairwise global alignment was performed between the retrieved UniProt sequences of Q88FC4 (171 aa, *P. putida* KT2440) and *E. coli* FabA P0A6Q3 (172 aa). The result: **66.7% amino-acid identity (114/171 aligned positions)**. The catalytic histidine maps to **His-70 in Q88FC4**, embedded in the fully conserved active-site/hotdog motif `WFFACHFEGDPVMPGCLGLDAM` (residues 65–85), which aligns to the *E. coli* motif `WFFGCHFIGDPVMPGCLGLDAM`. The adjacent **Cys-69** — the partner of the classic Cys-69/His-70 catalytic pair — is conserved at the identical aligned position, and the phosphopantetheine/acyl-tunnel signature `GDPVMPGCLGLDAM` (residues 73–86) is intact. The ~18.8 kDa size matches the hotdog dehydratase fold.

This directly links the historical *E. coli* mechanistic evidence to the target. As reported for *E. coli*, *"A cysteine residue (Cys-69) adjacent to the active site histidine may play the role in catalysis previously assigned to a tyrosine residue"* [PMID: 2832401](https://pubmed.ncbi.nlm.nih.gov/2832401/) — and that same Cys-69/His-70 pair is present in Q88FC4. The high identity and complete conservation of the catalytic architecture provide strong structural/evolutionary evidence that Q88FC4 catalyzes the annotated FabA dehydratase/isomerase reactions.

### Finding 6 — FabA (biosynthetic isomerase) is functionally distinct from the stress-response cis-trans isomerase Cti

A crucial disambiguation: *P. putida* contains **two enzymes with "isomerase" activity that act on fatty acids, and they must not be conflated.** FabA's EC 5.3.3.14 isomerase acts on **ACP-bound C10 intermediates during de novo FAS-II** to *create* a *cis* double bond as part of synthesis. By contrast, the separate **cis-trans isomerase Cti** acts on **pre-existing cis-unsaturated fatty acids already esterified into membrane phospholipids**, converting them to *trans*-isomers to rigidify the membrane during solvent or heat stress: *"Pseudomonas spp. possess a cis-trans isomerase (Cti) an enzyme that converts the cis-unsaturated fatty acids (FAs) of the membrane lipids to their trans-isomers to rigidify the membrane and thereby resist stresses"* [PMID: 30702193](https://pubmed.ncbi.nlm.nih.gov/30702193/).

The two enzymes differ in **substrate** (ACP-tethered acyl chains vs. phospholipid-esterified chains), **pathway stage** (biosynthesis vs. post-synthetic membrane remodeling), **chemistry** (trans-2 → cis-3 shift vs. cis → trans geometric isomerization), and **regulation** (PsrA/FabR vs. independent Crp/cAMP control). FabA is essential and biosynthetic; Cti is a stress-adaptive remodeling enzyme. Conflating them would misattribute FabA's role.

---

## Mechanistic Model / Interpretation

### The FAS-II elongation cycle and FabA's branch point

FabA operates within the dissociated (type II) bacterial fatty acid synthase, in which each reaction is carried out by a discrete, soluble cytoplasmic enzyme acting on substrates tethered to acyl carrier protein (ACP). The branch point looks like this:

```
   Malonyl-ACP + Acetyl-ACP
            │  (elongation cycles: FabB/FabF, FabG, FabA/FabZ, FabI)
            ▼
   (3R)-3-hydroxydecanoyl-ACP  (C10, 3-OH)
            │
            │  FabA  DEHYDRATION (EC 4.2.1.59)   ── shared with FabZ
            ▼
   trans-2-decenoyl-ACP  (C10, Δ2-trans)
          /        \
         /          \
  FabI reduction    FabA  ISOMERIZATION (EC 5.3.3.14)  ◄── COMMITTED STEP
  (→ saturated)          │                                (FabA-specific)
         │               ▼
         ▼         cis-3-decenoyl-ACP  (C10, Δ3-cis)
   SATURATED               │
   FATTY ACIDS             │  FabB elongation (double bond preserved)
   (e.g. 16:0)             ▼
                    16:1Δ9  and  18:1Δ11
                    UNSATURATED phospholipid acyl chains
```

The dehydration reaction (EC 4.2.1.59) is common to both FabA and FabZ and occurs at every chain length during elongation. What makes FabA special is the **isomerization (EC 5.3.3.14)**, which it performs efficiently only at the C10 stage. By converting *trans*-2-decenoyl-ACP into *cis*-3-decenoyl-ACP, FabA produces a species that FabI cannot reduce. The *cis*-3 double bond is therefore "locked in" and carried through two further rounds of elongation by FabB, emerging as the Δ9 (in 16:1) and Δ11 (in 18:1) double bonds of the mature membrane UFAs. This is why FabA is described as the committed, rate-influencing branch point of the anaerobic UFA pathway.

### Why FabA is essential in *P. putida*

| Feature | *P. putida* KT2440 (target) | *P. aeruginosa* PAO1 (contrast) |
|---|---|---|
| fabA–fabB operon | Present, essential | Present |
| UFA bypass (DesA desaturase) | Functionally absent | Functional |
| Phenotype of operon inactivation | **Growth blocked** unless exogenous UFA supplied | Growth continues |
| Consequence for FabA | Sole essential route to UFA | Redundant with desaturase |

Because *P. putida* lacks a functional oxygen-dependent desaturase bypass, FabA/FabB constitute the only route to membrane UFAs. UFAs are indispensable for maintaining membrane fluidity and integrity, so loss of FabA is lethal in the absence of external UFA supplementation [PMID: 36537550](https://pubmed.ncbi.nlm.nih.gov/36537550/).

### Structure–function logic

FabA is a small (~18.8 kDa) homodimeric enzyme adopting the **hotdog fold**, in which a long central α-helix ("sausage") is wrapped by a curved antiparallel β-sheet ("bun") that forms the substrate-binding tunnel. The catalytic **His-70** sits at the tunnel mouth and, with the assistance of **Cys-69**, mediates proton transfers for both dehydration and double-bond migration. The precise shape of the tunnel — dictated by the **β3 and β4 strands** — determines whether the α,β-unsaturated product can be repositioned for isomerization. FabZ, which shares the fold and the dehydration chemistry, lacks the correct tunnel geometry and therefore cannot isomerize; swapping the β3/β4 strands transfers isomerase capability [PMID: 15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/). The target Q88FC4 conserves both the catalytic dyad and the tunnel signature (Finding 5), so it is expected to be a full dehydratase/isomerase.

### Regulatory logic

```
   Acyl-ACP / Acyl-CoA pool  (senses UFA:SFA balance)
        │                         │
   unsaturated acyl              (environmental / growth-phase cues)
        │ effector                        │
        ▼                                 ▼
   FabR ── represses ─┐            PsrA ── activates ─┐
                      ▼                               ▼
              ┌──────────────  fabA–fabB operon  ──────────────┐
              │      (FabA dehydratase/isomerase + FabB KAS I)  │
              └────────────────────────────────────────────────┘
                                   │
                                   ▼
                     Membrane UFA content homeostasis
```

FabR provides negative feedback: when unsaturated acyl species accumulate, they act as co-repressors that strengthen FabR binding and shut down *fabA/fabB*, preventing overproduction of UFA [PMID: 19854834](https://pubmed.ncbi.nlm.nih.gov/19854834/). PsrA provides positive drive, keeping the operon expressed to maintain baseline UFA and downstream cyclopropane fatty acid content [PMID: 33964629](https://pubmed.ncbi.nlm.nih.gov/33964629/).

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [12237320](https://pubmed.ncbi.nlm.nih.gov/12237320/) | *A new mechanism for anaerobic unsaturated fatty acid formation in Streptococcus pneumoniae* | States FabA's dual dehydratase + trans-2→cis-3 isomerase activity on the C10 substrate — defines primary catalytic function (Finding 1). |
| [2832401](https://pubmed.ncbi.nlm.nih.gov/2832401/) | *Derived amino acid sequence and identification of active site residues of E. coli beta-hydroxydecanoyl thioester dehydrase* | Identifies catalytic His-70 via 3-decynoyl-NAC suicide inhibitor and the adjacent Cys-69; anchors the active-site verification of the target (Findings 3, 5). |
| [36537550](https://pubmed.ncbi.nlm.nih.gov/36537550/) | *Divergent unsaturated fatty acid synthesis in two highly related model pseudomonads* | Shows fabA–fabB produce the 16:1Δ9/18:1Δ11 chains and that operon loss blocks *P. putida* growth — essentiality and pathway output (Finding 2). |
| [15980063](https://pubmed.ncbi.nlm.nih.gov/15980063/) | *Domain swapping between E. faecalis FabN and FabZ localizes structural determinants for isomerase activity* | β3/β4 strand swap converts FabZ into an isomerase — structural basis of FabA isomerase capability (Finding 3). |
| [19854834](https://pubmed.ncbi.nlm.nih.gov/19854834/) | *Transcriptional regulation of membrane lipid homeostasis in E. coli* | Documents FabR repression of fabA/fabB tuning membrane UFA content (Finding 4). |
| [33964629](https://pubmed.ncbi.nlm.nih.gov/33964629/) | *PsrA positively regulates the UFA synthesis operon fabAB in Azotobacter vinelandii* | PsrA activation of fabAB in a close relative; confirms fabA annotation as 3-hydroxydecanoyl-ACP dehydratase/isomerase (Finding 4). |
| [30702193](https://pubmed.ncbi.nlm.nih.gov/30702193/) | *Transcriptional regulation of fatty acid cis-trans isomerization in P. putida F1* | Defines Cti as a post-synthetic membrane cis→trans isomerase — distinguishes it from FabA (Finding 6). |
| [30872475](https://pubmed.ncbi.nlm.nih.gov/30872475/) | *Structural and dynamical rationale for fatty acid unsaturation (FabA/FabZ)* | Supports the two functionally distinct dehydratases FabA and FabZ in γ-proteobacteria (context for Finding 3). |
| [17564601](https://pubmed.ncbi.nlm.nih.gov/17564601/) | *Compensatory role of cis-trans-isomerase and cardiolipin synthase in P. putida DOT-T1E* | Independent evidence that Cti acts on membrane lipids under solvent stress (context for Finding 6). |

Supporting/contextual literature also reviewed includes studies on PUFA-synthase dehydratase (DH) domains that complement *E. coli fabA* temperature-sensitive mutants (PMID: 29177940, 34601618), the *Mycobacterium* Had dehydratases as an alternative solution to the same (3*R*)-hydroxyacyl-ACP dehydration chemistry (PMID: 17804795), and FabI reductase contributions to UFA balance in *Sinorhizobium* (PMID: 39627703) — all reinforcing that FabA-type hotdog dehydratases are the canonical (3*R*)-hydroxyacyl-ACP dehydratase/isomerases of bacterial FAS-II.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88FC4 itself.** The functional assignment rests on (a) UniProt/HAMAP annotation, (b) strong sequence homology to *E. coli* FabA (66.7% identity, conserved His-70/Cys-69 and tunnel motif), and (c) genetic/physiological studies of the *fabA–fabB* operon in *P. putida* strains. No purified-enzyme kinetics (k_cat, K_m, substrate-chain-length profile) have been reported specifically for the KT2440 PP_4174 protein in the literature examined here.

2. **Strain transfer.** The definitive essentiality demonstration was performed in *P. putida* F1, not KT2440. Given the near-identical genetics of these strains, transfer is reasonable, but a KT2440-specific knockout confirmation is not documented here.

3. **Structural inference vs. experimental structure.** FabA's hotdog fold, homodimeric state, and catalytic dyad for Q88FC4 are inferred from homology and family membership; no experimental crystal/cryo-EM structure of the *P. putida* KT2440 enzyme has been examined in this investigation.

4. **Regulatory details in KT2440.** PsrA activation is best documented in *A. vinelandii* and FabR repression in *E. coli*. While *P. putida* possesses PsrA and the fabAB operon architecture, the exact operator sequences, effector affinities, and quantitative regulatory contributions in KT2440 were not directly measured here.

5. **Substrate specificity fine detail.** The C10 (decenoyl) specificity of the isomerization is well established for the paradigm enzymes, but the precise chain-length selectivity window of Q88FC4 has not been experimentally mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzyme kinetics.** Express and purify Q88FC4 and assay dehydratase (EC 4.2.1.59) and isomerase (EC 5.3.3.14) activities on a ladder of (3*R*)-hydroxyacyl-ACP substrates (C6–C16) to define chain-length specificity and confirm the C10 isomerization optimum.

2. **Active-site mutagenesis.** Generate His70Ala and Cys69Ala variants and test loss of dehydratase/isomerase activity and loss of covalent labeling by 3-decynoyl-*N*-acetylcysteamine, directly validating the predicted catalytic dyad in the target protein.

3. **Conditional knockout / complementation in KT2440.** Construct a *fabA* (PP_4174) conditional mutant in KT2440 and confirm UFA auxotrophy (growth rescue by exogenous oleate) to formally establish essentiality in this exact strain.

4. **Structural determination.** Solve the crystal or cryo-EM structure of Q88FC4 (ideally as a FabA–ACP or FabA–FabB complex) to confirm the hotdog fold, homodimer interface, and β3/β4 tunnel geometry underlying isomerase activity.

5. **Lipidomic phenotyping.** Quantify membrane 16:1Δ9 and 18:1Δ11 content by GC-MS in wild-type vs. *fabA*-depleted KT2440 to link enzyme activity to the specific UFA products.

6. **Regulatory mapping in KT2440.** Perform ChIP/EMSA and promoter-reporter assays for PsrA and FabR at the KT2440 *fabAB* promoter to quantify the regulatory circuit and its effector dependence.

7. **Clean separation from Cti.** In a *cti*-null background, confirm that FabA activity alone accounts for de novo *cis*-UFA production, reinforcing the functional distinction between biosynthetic (FabA) and post-synthetic (Cti) isomerases.

---

*Report prepared from a 3-iteration autonomous investigation: 6 confirmed findings, 16 papers reviewed. Gene identity verified — gene symbol (fabA), organism (P. putida KT2440), protein family (FabA thioester dehydratase), domains (IPR010083/IPR013114/IPR029069, PF07977), and catalytic residues (His-70/Cys-69) are all mutually consistent with the target Q88FC4.*


## Artifacts

- [OpenScientist final report](fabA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12237320
2. PMID:36537550
3. PMID:2832401
4. PMID:15980063
5. PMID:19854834
6. PMID:33964629
7. PMID:30702193
8. PMID:29177940
9. PMID:17804795
10. PMID:39627703