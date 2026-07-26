---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T14:51:41.904501'
end_time: '2026-07-17T15:22:11.036165'
duration_seconds: 1829.13
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lysA
  gene_symbol: lysA-II
  uniprot_accession: Q88CF4
  protein_description: 'RecName: Full=Diaminopimelate decarboxylase {ECO:0000256|ARBA:ARBA00074972,
    ECO:0000256|HAMAP-Rule:MF_02120}; Short=DAP decarboxylase {ECO:0000256|HAMAP-Rule:MF_02120};
    Short=DAPDC {ECO:0000256|HAMAP-Rule:MF_02120}; EC=4.1.1.20 {ECO:0000256|ARBA:ARBA00066427,
    ECO:0000256|HAMAP-Rule:MF_02120};'
  gene_info: Name=lysA-II {ECO:0000313|EMBL:AAN70792.1}; Synonyms=lysA {ECO:0000256|HAMAP-Rule:MF_02120};
    OrderedLocusNames=PP_5227 {ECO:0000313|EMBL:AAN70792.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the Orn/Lys/Arg decarboxylase class-II family.
  protein_domains: Ala_racemase/Decarboxylase_C. (IPR009006); DAP_deCOOHase_LysA.
    (IPR002986); De-COase2_C. (IPR022643); De-COase2_CS. (IPR022657); De-COase2_N.
    (IPR022644)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lysA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lysA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CF4
- **Protein Description:** RecName: Full=Diaminopimelate decarboxylase {ECO:0000256|ARBA:ARBA00074972, ECO:0000256|HAMAP-Rule:MF_02120}; Short=DAP decarboxylase {ECO:0000256|HAMAP-Rule:MF_02120}; Short=DAPDC {ECO:0000256|HAMAP-Rule:MF_02120}; EC=4.1.1.20 {ECO:0000256|ARBA:ARBA00066427, ECO:0000256|HAMAP-Rule:MF_02120};
- **Gene Information:** Name=lysA-II {ECO:0000313|EMBL:AAN70792.1}; Synonyms=lysA {ECO:0000256|HAMAP-Rule:MF_02120}; OrderedLocusNames=PP_5227 {ECO:0000313|EMBL:AAN70792.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Orn/Lys/Arg decarboxylase class-II family.
- **Key Domains:** Ala_racemase/Decarboxylase_C. (IPR009006); DAP_deCOOHase_LysA. (IPR002986); De-COase2_C. (IPR022643); De-COase2_CS. (IPR022657); De-COase2_N. (IPR022644)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lysA-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lysA-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lysA-II** (gene ID: lysA, UniProt: Q88CF4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lysA-II* (Q88CF4, PP_5227) — meso-Diaminopimelate Decarboxylase of *Pseudomonas putida* KT2440

## Summary

**lysA-II** (UniProt **Q88CF4**; ordered locus **PP_5227**) of *Pseudomonas putida* strain KT2440 encodes a **pyridoxal-5′-phosphate (PLP)-dependent meso-2,6-diaminopimelate decarboxylase (DAPDC; EC 4.1.1.20)**. Its primary and defining biochemical function is to catalyze the **terminal, committed step of L-lysine biosynthesis via the diaminopimelate (DAP) pathway**: the decarboxylation of **meso-diaminopimelate (meso-DAP)** to yield **L-lysine + CO₂**. This assignment is supported convergently by (i) the InterPro DAP_deCOOHase_LysA signature (IPR002986) carried by the protein and HAMAP rule MF_02120, (ii) strict conservation of every catalytic and substrate-specificity residue of characterized DAPDCs, and (iii) the enzyme's genomic embedding directly adjacent to *dapF*, the epimerase that manufactures its meso-DAP substrate. The gene identity given in the prompt (DAP decarboxylase, class-II Orn/Lys/Arg decarboxylase family, *P. putida* KT2440) is **fully consistent** with the literature and database evidence gathered; **no gene-symbol ambiguity was encountered** and no conflicting literature for a different gene under the same symbol was found.

The enzyme is a **soluble cytoplasmic protein** (no signal peptide, no transmembrane segment) that operates as an obligate **fold-type III (ornithine-decarboxylase-fold) homodimer** with a shared, inter-subunit active site. Catalysis uses PLP bound as an internal aldimine (Schiff base) to the active-site lysine (Lys60 in Q88CF4) and proceeds with a mechanistically distinctive **inversion of configuration** at the reacting carbon — a hallmark that separates DAPDC from most other PLP-dependent α-decarboxylases. Substrate specificity for meso-DAP is enforced by stereochemical recognition of the L-chiral center combined with a system of ionic "molecular rulers" (notably a conserved distal arginine that ion-pairs with the L-carboxylate of DAP), making DAPDCs highly selective enzymes.

A notable organism-specific feature is that *P. putida* KT2440 carries **two DAPDC paralogs**: **lysA-I (PP_2077, Q88L58)**, the close ortholog of the canonical *E. coli* housekeeping enzyme, and the target **lysA-II (PP_5227, Q88CF4)**, a more sequence-divergent second copy (only ~38% identical to lysA-I and to *E. coli* LysA). Despite this scaffold divergence, lysA-II retains a fully intact, wild-type DAPDC active site and — uniquely among the two paralogs — sits in a genuine DAP-biosynthetic genomic neighborhood next to *dapF*. The product of the reaction, L-lysine, feeds both protein synthesis and, together with meso-DAP, the cross-linking of the Gram-negative peptidoglycan cell wall, placing lysA-II at a metabolic branch point essential to cell-wall integrity and growth.

### Gene/Protein Identity Verification

| Attribute | Value |
|---|---|
| UniProt | Q88CF4 |
| Gene | *lysA-II* (synonym *lysA*); locus PP_5227 |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) |
| Enzyme | Diaminopimelate decarboxylase (DAPDC), EC 4.1.1.20 |
| Length | 415 aa |
| Family | Orn/Lys/Arg decarboxylase class-II (fold-type III PLP) |
| Key domains | IPR002986 (DAP_deCOOHase_LysA), IPR009006 (Ala racemase/decarboxylase C, TIM-barrel), IPR022643/IPR022644/IPR022657 |

**Verification outcome: CONFIRMED, unambiguous.** The DAPDC-specific InterPro signature (IPR002986), HAMAP rule MF_02120, EC number, and the complete DAPDC catalytic residue set all coincide. This is a genuine meso-DAP decarboxylase, not a mis-annotated ornithine/arginine decarboxylase of the same fold family.

---

## Key Findings

### Finding 1 — lysA-II is a meso-diaminopimelate decarboxylase catalyzing the terminal step of L-lysine biosynthesis

The core functional assignment is that Q88CF4 is a **DAPDC (EC 4.1.1.20)** catalyzing:

> **meso-2,6-diaminopimelate + H⁺ → L-lysine + CO₂**

This is the **final, single-step ("step 1/1") committed reaction** of the bacterial DAP pathway for lysine biosynthesis. The assignment rests on the InterPro **DAP_deCOOHase_LysA signature (IPR002986)** carried by the protein and is corroborated by direct experimental statements in the DAPDC structural literature: the enzyme "catalyzes the final step in the lysine biosynthetic pathway converting meso-diaminopimelic acid (DAP) to l-lysine" ([PMID: 12637582](https://pubmed.ncbi.nlm.nih.gov/12637582/)), and it is "a PLP-dependent enzyme … responsible for the final step of L-lysine biosynthesis in bacteria" ([PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/)).

The UniProt residue-level annotation for Q88CF4 reinforces the machinery expected of a DAPDC: a **415-amino-acid** protein using **PLP as cofactor**, forming the internal aldimine at **Lys60** (N6-(pyridoxal phosphate)lysine), with an active-site **proton donor at position 342**, PLP-binding residues at 239 and 273–276 and 370, and substrate-binding residues at 276, 312, 316, 343 and 370. The pathway annotation assigns it to "L-lysine biosynthesis via DAP pathway; L-lysine from DL-2,6-diaminopimelate: step 1/1" — a single terminal decarboxylation.

### Finding 2 — Substrate specificity for meso-DAP arises from stereochemical recognition plus ionic "molecular rulers"

DAPDCs are described as **"highly selective enzymes"** ([PMID: 34258615](https://pubmed.ncbi.nlm.nih.gov/34258615/)). Cocrystal structures of DAPDC (e.g., *Methanocaldococcus jannaschii* with an azelaic-acid substrate analog and with the L-lysine product) established that "substrate specificity derives from recognition of the L-chiral center of diaminopimelate and a system of ionic 'molecular rulers' that dictate substrate length" ([PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/)). Because meso-DAP has two stereocenters (one D, one L), the enzyme recognizes the **L-center** at a distal binding site while decarboxylating the **D-center**. A key element of this ruler is a conserved distal arginine: "the distal binding site of DAPDC contains a conserved arginine that forms an ion pair with the l-carboxylate end of DAP" ([PMID: 30699288](https://pubmed.ncbi.nlm.nih.gov/30699288/)). In Q88CF4 this distal-carboxylate recognition is provided by conserved arginine/glutamate residues (Arg276, Arg312, Glu343) that are strictly maintained (see Finding 6). This same distal-arginine/re-face-tyrosine machinery discriminates DAPDC from the ornithine/arginine decarboxylases of the same fold, which lack it.

### Finding 3 — DAPDC is a fold-type III PLP enzyme acting as a head-to-tail homodimer with a shared active site

The crystal structure of *Mycobacterium tuberculosis* DAPDC established the architecture shared by this enzyme family: "a stable 2-fold dimer in head-to-tail arrangement of a triose-phosphate isomerase (TIM) barrel-like alpha/beta domain and a C-terminal beta sheet domain, similar to the ornithine decarboxylase (ODC) fold family" ([PMID: 12637582](https://pubmed.ncbi.nlm.nih.gov/12637582/)). Critically, "PLP is covalently bound via an internal aldimine, and residues from both domains **and both subunits** contribute to the binding pocket" ([PMID: 12637582](https://pubmed.ncbi.nlm.nih.gov/12637582/)) — the active site is inter-subunit, making the homodimer the obligate functional unit. This matches the InterPro domain complement of Q88CF4: **Ala_racemase/Decarboxylase_C (IPR009006, the TIM-barrel), De-COase2_N (IPR022644) and De-COase2_C (IPR022643)**. UniProt annotates Q88CF4 as a homodimer. **Functional implication:** the monomer is not catalytically competent on its own.

### Finding 4 — Catalysis proceeds with inversion of configuration, a mechanistic hallmark of DAPDC

Stereochemical NMR labeling studies of meso-DAP decarboxylases from *Bacillus sphaericus* and wheat germ demonstrated that the reaction "operates with **inversion of configuration**. This suggests similar mechanisms for the prokaryotic and eukaryotic enzymes and contrasts the retention mode observed with other pyridoxal phosphate dependent alpha-decarboxylases" ([PMID: 3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/)). Structural work on *Helicobacter pylori* DAPDC placed the scissile carboxylate at the *si* face of the cofactor, capturing the first reported external aldimine of DAPDC and revealing an induced-fit "down/up" active-site loop that shields the intermediate and releases product ([PMID: 18508763](https://pubmed.ncbi.nlm.nih.gov/18508763/)). Inversion of configuration is therefore a defining catalytic signature of the DAPDC branch of fold-type III decarboxylases and applies to lysA-II by homology.

### Finding 5 — DAPDC sits at a metabolic branch point; its product supplies protein synthesis and peptidoglycan, and the enzyme is essential and drug-targetable

The DAP/lysine pathway "provides lysine for protein synthesis and both lysine and meso-diaminopimelate for construction of the bacterial peptidoglycan cell wall" ([PMID: 17579770](https://pubmed.ncbi.nlm.nih.gov/17579770/)). meso-DAP itself "is a unique component of the cell wall of Gram-negative bacteria" ([PMID: 36040174](https://pubmed.ncbi.nlm.nih.gov/36040174/)), where it serves as the peptidoglycan cross-linking residue — directly relevant to *P. putida*, a Gram-negative organism. Because the pathway is absent in mammals and essential in bacteria, DAPDC is a validated antibacterial target: "the lysA gene of M. tuberculosis H37Rv has been established as essential for bacterial survival in immunocompromised mice, demonstrating that de novo biosynthesis of lysine is essential for in vivo viability" ([PMID: 12637582](https://pubmed.ncbi.nlm.nih.gov/12637582/)).

Upstream, four distinct enzymatic branches (succinylase, acetylase, dehydrogenase, and aminotransferase routes) convert tetrahydrodipicolinate to meso-DAP: "In bacteria, there have been four separate pathways identified from tetrahydrodipicolinate to meso-diaminopimelate, which is the immediate precursor to lysine" ([PMID: 28271480](https://pubmed.ncbi.nlm.nih.gov/28271480/)). All converge on meso-DAP, which DAPDC decarboxylates as the single universal final step; bacteria "with some exceptions, rely on variations of the meso-diaminopimelate pathway for lysine biosynthesis" ([PMID: 23504110](https://pubmed.ncbi.nlm.nih.gov/23504110/)). In some bacteria DAPDC is feedback-inhibited by the end-product L-lysine (e.g., *Bacillus methanolicus* DAPDC, Ki ≈ 0.93 mM, Km ≈ 0.8 mM for DAP; [PMID: 8215365](https://pubmed.ncbi.nlm.nih.gov/8215365/)), providing a regulatory tie-back on flux — although whether the *P. putida* lysA-II isoform is lysine-inhibited has not been directly measured.

### Finding 6 — Residue-level conservation confirms an intact DAPDC active site in lysA-II

Mapping the catalytic residues of Q88CF4 onto both the paralog lysA-I (Q88L58) and *E. coli* LysA (P00861) by global alignment shows **8/8 identity at every functional position**:

| Functional role | Q88CF4 (lysA-II) | lysA-I (Q88L58) | *E. coli* LysA (P00861) |
|---|---|---|---|
| PLP Schiff base (internal aldimine) | Lys60 | Lys | Lys |
| PLP binding | Gly239 | Gly | Gly |
| Substrate / PLP binding | Arg276 | Arg | Arg |
| Substrate binding (distal) | Arg312 | Arg | Arg |
| *re*-face | Tyr316 | Tyr | Tyr |
| Proton donor | Cys342 | Cys | Cys |
| Distal carboxylate recognition | Glu343 | Glu | Glu |
| *re*-face | Tyr370 | Tyr | Tyr |

Despite only **37.8% overall identity** between the two paralogs (and 38.8% between lysA-II and *E. coli* LysA), the **active-site chemistry is identical**, confirming lysA-II is a bona fide meso-DAP decarboxylase rather than a diverged pseudo-enzyme or a substrate-shifted paralog. This is important because the fold-type III / ODC-fold superfamily also contains ornithine, arginine, and lysine decarboxylases whose specificity is tuned by a 3₁₀-helix specificity element ([PMID: 17626020](https://pubmed.ncbi.nlm.nih.gov/17626020/), [PMID: 30699288](https://pubmed.ncbi.nlm.nih.gov/30699288/)); the strict conservation of the DAPDC distal-carboxylate machinery (distal arginine + re-face tyrosines that "preclude the binding of l-amino acids") argues specifically for meso-DAP, not a basic amino acid, as the substrate.

### Finding 7 — lysA-II is a divergent second DAPDC paralog embedded in the DAP-biosynthetic genomic context

A UniProt search of *P. putida* KT2440 (taxid 160488) returns **two** DAP decarboxylases: the target **lysA-II (Q88CF4, PP_5227, 415 aa)** and **lysA-I (Q88L58, PP_2077, 410 aa)**. Pairwise identities (Needleman–Wunsch):

| Comparison | % identity |
|---|---|
| lysA-I (PP_2077) vs *E. coli* LysA (P00861) | 58.7% |
| lysA-II (PP_5227) vs *E. coli* LysA (P00861) | 38.8% |
| lysA-II (PP_5227) vs lysA-I (PP_2077) | 37.8% |

Thus **lysA-I is the close ortholog of the canonical housekeeping DAPDC**, whereas **lysA-II (the target) is a more divergent paralog** — the two are ancient duplicates rather than recent copies. Genomic context, however, tells a striking story that reverses the naïve expectation from sequence similarity alone:

- **lysA-II / PP_5227 is immediately flanked by PP_5228 = *dapF* (diaminopimelate epimerase).** DapF interconverts LL-DAP and meso-DAP, generating the exact substrate that DAPDC decarboxylates:

```
   LL-DAP  ──[DapF / PP_5228]──►  meso-DAP  ──[LysA-II / PP_5227]──►  L-lysine + CO2
```

  i.e., the **two consecutive terminal steps of the DAP pathway are encoded side-by-side**, a classic operonic/functional-coupling arrangement.

- By contrast, **lysA-I / PP_2077** lies among a LysR-family transcriptional regulator (PP_2078), a GNAT acetyltransferase (PP_2073), a second LysR regulator (PP_2074), and a VasX/T6SS toxin-domain gene (PP_2076) — **no DAP/lysine-biosynthesis neighbors**.

This suggests the divergent lysA-II is the copy most tightly wired into de novo meso-DAP → lysine production, while the sequence-canonical lysA-I sits in a regulatory/secretion-associated locus that may reflect a distinct physiological role.

### Finding 8 — LysA-II is a soluble cytoplasmic enzyme

The UniProt feature table for Q88CF4 contains only Domain, Active-site, Binding-site, and Modified-residue features — **no signal peptide and no transmembrane segment** — identifying it as a soluble **cytoplasmic** protein. This is consistent with all characterized DAP-pathway and lysine-biosynthetic enzymes, which are cytosolic, and with the fact that amino-acid biosynthesis and the cytoplasmic steps of peptidoglycan-precursor (UDP-MurNAc-pentapeptide) assembly proceed in the cytoplasm. LysA-II therefore carries out its function in the cytosol, delivering L-lysine and meso-DAP to downstream cytoplasmic steps of translation and peptidoglycan precursor assembly. (Note: this localization is a strong inference from sequence features and pathway biochemistry; no direct experimental localization study exists for this specific protein.)

---

## Mechanistic Model / Interpretation

Integrating the eight findings yields a coherent mechanistic and physiological model for lysA-II.

**Pathway position.** LysA-II operates at the very end of the DAP/lysine biosynthetic pathway, at the funnel point where the branched pathway collapses into one terminal reaction:

```
  aspartate
     │  (multiple steps)
     ▼
 tetrahydrodipicolinate
     │  four alternative branches:
     │  succinylase / acetylase / dehydrogenase / aminotransferase
     ▼
   LL-2,6-diaminopimelate
     │  DapF (PP_5228, diaminopimelate epimerase)   ◄─ genomic neighbor of lysA-II
     ▼
  meso-2,6-diaminopimelate ───────────────┐
     │                                     │ (also drawn off directly for
     │  LysA-II (PP_5227, DAPDC,           │  peptidoglycan cross-linking)
     │           EC 4.1.1.20)              │
     ▼                                     ▼
   L-lysine + CO2                    peptidoglycan (Gram-negative cell wall)
     │
     ├──► protein synthesis (translation)
     └──► lysine-derived metabolism / cell-wall lysine
```

**Catalytic cycle.** In the resting enzyme, PLP is anchored as an internal aldimine (Schiff base) to Lys60 of Q88CF4. Incoming meso-DAP displaces Lys60 to form an external aldimine; the enzyme selects the substrate by recognizing its L-chiral center and clamping its two carboxylate ends via ionic "molecular rulers," including the conserved distal arginine that ion-pairs the far L-carboxylate ([PMID: 12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/), [PMID: 30699288](https://pubmed.ncbi.nlm.nih.gov/30699288/)). The D-configured α-carboxylate, positioned at the *si* face of the cofactor ([PMID: 18508763](https://pubmed.ncbi.nlm.nih.gov/18508763/)), is decarboxylated, PLP stabilizing the resulting carbanion as a quinonoid. Reprotonation from the opposite face — by the proton-donor cysteine (Cys342 in Q88CF4) — delivers the product with **inversion of configuration** ([PMID: 3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/)), yielding L-lysine, which is released as the internal aldimine reforms. A mobile active-site loop cycles between "down" (protecting the intermediate) and "up" (releasing product) conformations ([PMID: 18508763](https://pubmed.ncbi.nlm.nih.gov/18508763/)). The complete active site is assembled from two subunits, so the head-to-tail homodimer is the minimal catalytic unit ([PMID: 12637582](https://pubmed.ncbi.nlm.nih.gov/12637582/)).

**Two-paralog interpretation.** The most interesting organism-specific feature is the presence of two DAPDCs in *P. putida* KT2440. The paradox — that the sequence-divergent copy (lysA-II), not the *E. coli*-like copy (lysA-I), is the one sitting next to *dapF* — is resolved by recognizing that genomic context is a stronger indicator of committed metabolic role than raw sequence identity. The lysA-II/dapF gene pair encodes the last two enzymatic steps that convert LL-DAP → meso-DAP → L-lysine, strongly implying that lysA-II is the physiologically dedicated de novo lysine-biosynthetic decarboxylase, while lysA-I (embedded among LysR regulators, an acetyltransferase, and a T6SS toxin gene) may serve a conditionally regulated or secondary role. Both enzymes, however, possess a fully conserved DAPDC active site (8/8 catalytic residues), so both are competent meso-DAP decarboxylases; they are not substrate-shifted toward ornithine/arginine/lysine substrates as some other fold-type III paralogs are.

**Localization and output.** As a soluble cytoplasmic enzyme, lysA-II performs its chemistry in the cytosol and feeds two essential downstream fates: L-lysine for ribosomal protein synthesis, and lysine/meso-DAP for peptidoglycan cross-linking in the Gram-negative envelope. This dual output places lysA-II at an essential metabolic node whose disruption would compromise both translation and cell-wall integrity.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges the findings |
|---|---|---|
| [12637582](https://pubmed.ncbi.nlm.nih.gov/12637582/) | *M. tuberculosis* DAPDC crystal structure | Defines the reaction (meso-DAP → L-lysine), the fold-type III head-to-tail homodimer, covalent PLP internal aldimine and inter-subunit active site, and lysA essentiality/drug-target status (F1, F3, F5) |
| [12429091](https://pubmed.ncbi.nlm.nih.gov/12429091/) | Cocrystal structures of DAPDC | PLP dependence, final step of lysine biosynthesis, and molecular-ruler basis of meso-DAP specificity (F1, F2) |
| [34258615](https://pubmed.ncbi.nlm.nih.gov/34258615/) | Thermostable D-amino acid decarboxylases from *T. maritima* DAPDC | States DAPDCs are highly selective; defines meso-DAP → L-lysine substrate/product pair (F2) |
| [30699288](https://pubmed.ncbi.nlm.nih.gov/30699288/) | D-Orn/D-Lys decarboxylase structure | Identifies the conserved distal arginine that ion-pairs the L-carboxylate of DAP; specificity/stereospecificity of fold III (F2, F6) |
| [3927976](https://pubmed.ncbi.nlm.nih.gov/3927976/) | Stereochemistry of meso-DAP decarboxylase (wheat germ) | Establishes inversion of configuration as the DAPDC mechanistic hallmark, contrasting retention in other PLP α-decarboxylases (F4) |
| [18508763](https://pubmed.ncbi.nlm.nih.gov/18508763/) | *H. pylori* DAPDC external aldimine structure | si-face placement of scissile carboxylate; induced-fit "down/up" active-site loop (F4) |
| [36040174](https://pubmed.ncbi.nlm.nih.gov/36040174/) | Diaminopimelic acid metabolism | meso-DAP is a unique Gram-negative cell-wall component (F5) |
| [17579770](https://pubmed.ncbi.nlm.nih.gov/17579770/) | Inhibition of lysine biosynthesis (review) | Dual role: lysine for protein synthesis + lysine/meso-DAP for peptidoglycan; antibiotic target (F5, F8) |
| [28271480](https://pubmed.ncbi.nlm.nih.gov/28271480/) | DHDPS structure/evolution review | Four upstream branches converge on meso-DAP, the DAPDC substrate (F5) |
| [23504110](https://pubmed.ncbi.nlm.nih.gov/23504110/) | Lysine biosynthesis as drug target (review) | Bacteria use meso-DAP pathway; DAPDC is terminal enzyme (F5) |
| [8215365](https://pubmed.ncbi.nlm.nih.gov/8215365/) | *B. methanolicus* DAPDC cloning | Lysine feedback inhibition (Ki ≈ 0.93 mM) and kinetics (Km ≈ 0.8 mM DAP) for a bacterial DAPDC (F5) |
| [17626020](https://pubmed.ncbi.nlm.nih.gov/17626020/) | β/α-barrel basic amino acid decarboxylases | Contextualizes fold-type III specificity determinants; some *Pseudomonas* enzymes in this family prefer L-ornithine, underscoring the value of DAPDC residue conservation for correct substrate assignment (F6) |

Findings F6, F7, and F8 are additionally grounded in direct bioinformatic analysis of UniProt Q88CF4/Q88L58/P00861 and the *P. putida* KT2440 genome (residue-level feature tables, pairwise global alignments, and gene-neighborhood inspection) performed during the investigation.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the Q88CF4 protein.** The functional assignment is inference-based: it rests on InterPro/UniProt annotation, strict active-site residue conservation, homology to structurally characterized DAPDCs from other organisms (*M. tuberculosis*, *M. jannaschii*, *H. pylori*, *B. methanolicus*, wheat germ), and genomic context. There is no purified-enzyme kinetic study, crystal structure, or gene-knockout phenotype specifically for *P. putida* lysA-II (PP_5227). Q88CF4 is annotated at ProteinExistence level 3 (inferred from homology).

2. **Relative roles of the two paralogs are unresolved.** We infer from genomic context that lysA-II is the dedicated de novo lysine-biosynthetic decarboxylase and lysA-I a secondary/regulated copy, but this has not been tested. Which paralog carries the bulk of flux in vivo, whether either is conditionally expressed, and whether they are functionally redundant remain open.

3. **Regulation is not established for this isoform.** Although lysine feedback inhibition is documented for some bacterial DAPDCs, whether *P. putida* lysA-II is lysine-inhibited (and its Km/kcat) is unmeasured.

4. **Substrate specificity is inferred, not measured.** Residue conservation strongly predicts meso-DAP as the substrate, but the fold-type III superfamily includes ornithine/arginine/lysine decarboxylases; direct assay would be needed to exclude minor activity on alternative substrates.

5. **Localization is predicted from sequence.** The cytoplasmic assignment follows from the absence of signal/transmembrane features and family precedent, not from experimental fractionation of *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and kinetic assay.** Clone and purify recombinant Q88CF4; measure DAPDC activity on meso-DAP (Km, kcat) using a coupled decarboxylase assay, confirm PLP dependence, and test L-lysine feedback inhibition. Counter-screen against LL-DAP, D,D-DAP, L-ornithine, L-arginine and L-lysine to confirm strict meso-DAP specificity.

2. **Genetics of the two paralogs.** Construct single (ΔlysA-I, ΔlysA-II) and double knockouts in *P. putida* KT2440 and test lysine auxotrophy and growth on minimal medium. Complementation and cross-complementation would quantify functional redundancy and reveal which paralog is required for de novo lysine biosynthesis.

3. **Expression profiling.** Use RT-qPCR/RNA-seq (± exogenous lysine, ± cell-wall stress) to determine whether lysA-II and lysA-I are differentially regulated and whether lysA-II is co-transcribed with *dapF* (PP_5228) as an operon.

4. **Structural determination.** Solve or model (AlphaFold) the structure of LysA-II (apo, PLP-bound internal aldimine, and with a meso-DAP substrate analog) to confirm the fold-type III homodimer, the Lys60 Schiff base, and the distal-arginine molecular ruler, and to compare the distal pockets of the two paralogs.

5. **Localization confirmation.** Fluorescent-fusion or cell-fractionation experiments to verify cytoplasmic localization in *P. putida*.

6. **Inhibitor/antibacterial relevance.** Given DAPDC's validated status as an antibacterial target, screen the enzyme against known DAPDC inhibitors to assess whether the divergent lysA-II scaffold offers a distinct inhibitor-binding profile.

---

*Report prepared from a 5-iteration autonomous investigation comprising 11 confirmed findings and 23 reviewed papers. All gene-identity verification steps (gene symbol, organism, protein family, and domain architecture) were satisfied: the target lysA-II / Q88CF4 / PP_5227 of* Pseudomonas putida *KT2440 is unambiguously a meso-diaminopimelate decarboxylase, and no conflicting literature for a different gene under the same symbol was encountered.*


## Artifacts

- [OpenScientist final report](lysA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lysA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12637582
2. PMID:12429091
3. PMID:34258615
4. PMID:30699288
5. PMID:3927976
6. PMID:18508763
7. PMID:17579770
8. PMID:36040174
9. PMID:28271480
10. PMID:23504110
11. PMID:8215365
12. PMID:17626020