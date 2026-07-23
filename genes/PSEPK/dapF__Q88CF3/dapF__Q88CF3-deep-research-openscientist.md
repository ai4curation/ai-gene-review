---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T14:22:45.921818'
end_time: '2026-07-17T14:55:46.897211'
duration_seconds: 1980.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapF__Q88CF3
  gene_symbol: dapF
  uniprot_accession: Q88CF3
  protein_description: 'RecName: Full=Diaminopimelate epimerase {ECO:0000255|HAMAP-Rule:MF_00197};
    Short=DAP epimerase {ECO:0000255|HAMAP-Rule:MF_00197}; EC=5.1.1.7 {ECO:0000255|HAMAP-Rule:MF_00197};
    AltName: Full=PLP-independent amino acid racemase {ECO:0000255|HAMAP-Rule:MF_00197};'
  gene_info: Name=dapF {ECO:0000255|HAMAP-Rule:MF_00197}; OrderedLocusNames=PP_5228;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the diaminopimelate epimerase family.
  protein_domains: DAP_epimerase_AS. (IPR018510); DAP_epimerase_DapF. (IPR001653);
    DAP_epimerase (PF01678)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dapF__Q88CF3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapF__Q88CF3-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CF3
- **Protein Description:** RecName: Full=Diaminopimelate epimerase {ECO:0000255|HAMAP-Rule:MF_00197}; Short=DAP epimerase {ECO:0000255|HAMAP-Rule:MF_00197}; EC=5.1.1.7 {ECO:0000255|HAMAP-Rule:MF_00197}; AltName: Full=PLP-independent amino acid racemase {ECO:0000255|HAMAP-Rule:MF_00197};
- **Gene Information:** Name=dapF {ECO:0000255|HAMAP-Rule:MF_00197}; OrderedLocusNames=PP_5228;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the diaminopimelate epimerase family.
- **Key Domains:** DAP_epimerase_AS. (IPR018510); DAP_epimerase_DapF. (IPR001653); DAP_epimerase (PF01678)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapF** (gene ID: dapF__Q88CF3, UniProt: Q88CF3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *dapF* (PP_5228, UniProt Q88CF3) — Diaminopimelate Epimerase of *Pseudomonas putida* KT2440

**Gene:** `dapF` (ordered locus **PP_5228**) · **UniProt:** Q88CF3 (DAPF_PSEPK, 276 aa) · **EC 5.1.1.7** · **KEGG ortholog:** K01778
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / **KT2440**), a Gram-negative gammaproteobacterium.

## Summary

The gene **dapF** (ordered locus name **PP_5228**; UniProt **Q88CF3**; protein DAPF_PSEPK, 276 aa) of *Pseudomonas putida* KT2440 encodes **diaminopimelate epimerase** (DAP epimerase; **EC 5.1.1.7**), a small, cytoplasmic, cofactor-independent amino-acid racemase/epimerase. Its primary and defining function is the reversible stereoinversion of **LL-2,6-diaminopimelate (LL-DAP) to meso-(D,L)-2,6-diaminopimelate (meso-DAP)**. This reaction constitutes the **penultimate step of the diaminopimelate (DAP) branch of L-lysine biosynthesis**. The identity of the target is unambiguous: the UniProt annotation, HAMAP rule MF_00197, KEGG orthology K01778, and the conserved Pfam DAP_epimerase (PF01678) domain architecture all converge on a canonical DAP epimerase, and the organism assignment (*P. putida* KT2440) is confirmed by the locus tag PP_5228 in the KEGG genome. There is no ambiguity or literature conflict for this gene symbol in this context.

Mechanistically, DapF is a paradigm **pyridoxal-5′-phosphate (PLP)-independent, metal-independent amino acid racemase**. It abstracts and re-adds the proton at the α-carbon of one of the two stereocenters of DAP using **two catalytic cysteines** that alternate roles as a base (thiolate) and an acid (thiol). In Q88CF3 these are **Cys75 (proton donor active site) and Cys219 (proton acceptor active site)**, both experimentally supported by homology to structurally characterized DapF enzymes and confirmed by sequence analysis to sit within the diagnostic DAP-epimerase signature motifs. The enzyme adopts a two-domain α/β "DAP-epimerase fold," functions as a **homodimer**, and undergoes **substrate-induced domain closure** that encapsulates DAP and positions the two cysteines for catalysis. A conserved dimerization tyrosine (Tyr270 in Q88CF3) is required for the active dimer.

Biologically, DapF operates in the **cytoplasm** and supplies **meso-DAP**, a metabolite with a dual and essential fate in Gram-negative bacteria: (i) it is the direct precursor for L-lysine (decarboxylated by the genomically adjacent LysA/PP_5227), and (ii) it is directly incorporated as the cross-linking residue of the peptidoglycan pentapeptide. In *P. putida* KT2440, dapF sits immediately downstream of, and overlaps, lysA, coupling the final two steps of the pathway. Because DapF is the sole route to meso-DAP and the entire DAP/lysine pathway is absent in mammals, the enzyme is a validated, selective antibacterial/herbicide target. A distinct, well-characterized **moonlighting function** — physical stimulation of the RNA pyrophosphohydrolase RppH to promote 5′-end-dependent mRNA decay — has been documented for *E. coli* DapF and represents a second potential role for the *P. putida* orthologue.

---

## Gene/Protein Identity Verification

Per the mandatory verification protocol, all identity checks passed:

| Check | Result |
|-------|--------|
| Gene symbol matches protein description | ✅ "dapF" is the standard symbol for diaminopimelate epimerase; matches EC 5.1.1.7 annotation |
| Organism correct | ✅ *Pseudomonas putida* KT2440; KEGG locus **ppu:PP_5228** confirms the strain assignment |
| Protein family/domains align with literature | ✅ Pfam **PF01678 (DAP_epimerase)**; InterPro IPR001653/IPR018510; PhzF/DAP-epimerase-like superfamily — all consistent with the DAP epimerase literature |
| No conflicting literature for a same-symbol gene | ✅ No ambiguity; "dapF" refers consistently to DAP epimerase across bacteria |

**Conclusion:** The research target is correctly identified as diaminopimelate epimerase. The report below proceeds with high confidence.

---

## Key Findings

### Finding 1 — DapF catalyzes the stereoinversion of LL-diaminopimelate to meso-DAP (EC 5.1.1.7)

The core function of Q88CF3 is the reversible epimerization **LL-DAP ⇌ meso-(D,L)-DAP**. UniProt (DAPF_PSEPK, 276 aa) annotates the enzyme under EC 5.1.1.7 and HAMAP rule MF_00197, with the FUNCTION statement "Catalyzes the stereoinversion of LL-2,6-diaminopimelate," and assigns it to L-lysine biosynthesis via the DAP pathway. This reaction is the **penultimate step of the DAP/lysine pathway**: DapF inverts one of the two stereocenters of the symmetric diaminopimelate scaffold, converting the LL-isomer into the meso-isomer.

This assignment is strongly supported by the primary literature. A 2025 study on cofactor-independent epimerases describes "diaminopimelic acid epimerase (DapF-CC), which produces D,L-diaminopimelic acid (DAP) as the penultimate step in lysine biosynthesis in most bacteria and photosynthetic organisms, and for Gram-negative bacterial peptidoglycan" ([PMID: 40774471](https://pubmed.ncbi.nlm.nih.gov/40774471/)). This directly states both the product (meso/D,L-DAP) and its dual biological role. The foundational mechanistic paper on *Haemophilus influenzae* DapF states plainly that "D,L-Diaminopimelate is generated from the corresponding L,L-isomer by the dapF-encoded epimerase" ([PMID: 10194362](https://pubmed.ncbi.nlm.nih.gov/10194362/)), defining the exact reaction catalyzed.

The product meso-DAP has two essential fates in a Gram-negative organism like *P. putida*: it is decarboxylated by LysA (diaminopimelate decarboxylase) to yield L-lysine, and it is directly incorporated into the peptidoglycan pentapeptide where it forms the 3→4 cross-link of the murein sacculus.

### Finding 2 — Cofactor-independent, two-cysteine (thiol/thiolate) catalytic mechanism

DapF is a defining member of the **PLP-independent amino-acid racemases**. Unlike alanine racemase and most amino-acid racemases, it requires no pyridoxal-5′-phosphate cofactor and no metal ion. Instead, catalysis proceeds through **two cysteine residues acting in concert**, one serving as a catalytic base (thiolate) to abstract the α-proton and the other as a catalytic acid (thiol) to reprotonate the resulting planar carbanion intermediate from the opposite face — a "two-base" 1,1-proton-transfer mechanism that achieves net inversion of configuration at the α-carbon.

For Q88CF3, UniProt assigns **ACT_SITE 75 (proton donor)** and **ACT_SITE 219 (proton acceptor)**, and sequence analysis confirms **position 75 = Cys and position 219 = Cys**, both embedded in the diagnostic DAP-epimerase signature motifs (…EQ-**C**GN-GAR-C… and …QA-**C**GT-GAC…). The mechanistic literature is explicit: DapF "requires no cofactors and it functions through an unusual mechanism involving two cysteine residues acting in concert and alternating as a base (thiolate) and as an acid (thiol)" ([PMID: 19013471](https://pubmed.ncbi.nlm.nih.gov/19013471/)). The *H. influenzae* study establishes that "Diaminopimelate epimerase is a representative of the pyridoxal phosphate-independent amino acid racemases, for which substantial evidence exists supporting the role of two cysteine residues as the catalytic acid and base" ([PMID: 10194362](https://pubmed.ncbi.nlm.nih.gov/10194362/)). Kinetic/pH analysis of the *H. influenzae* enzyme shows a single catalytic group with pK ≈ 6.1–7.0 that must be unprotonated for activity — consistent with a cysteine thiolate base.

### Finding 3 — Cytoplasmic, two-domain homodimer with substrate-induced domain closure

DapF is a **cytoplasmic** enzyme (UniProt SUBCELLULAR LOCATION = Cytoplasm) that functions as a **homodimer** (UniProt SUBUNIT = Homodimer). It adopts a two-domain α/β architecture — the "DAP-epimerase fold" — in which the active site lies in the cleft between an N-terminal and a C-terminal domain, each contributing one of the two catalytic cysteines.

Two structural principles are firmly established. First, **dimerization is essential for catalysis**: in *E. coli* DapF, the monomeric Y268A mutant is catalytically dead — "Y268A is catalytically inactive, thus demonstrating that dimerization of DAP epimerase is essential for catalysis" ([PMID: 23426375](https://pubmed.ncbi.nlm.nih.gov/23426375/)). Q88CF3 conserves the analogous dimerization tyrosine at **Tyr270** (UniProt SITE 270, confirmed in sequence), supporting the homodimer annotation. Second, catalysis is coupled to a **conformational switch**: "Substrate binding to the C-terminal domain triggers the closure of the N-terminal domain coupled with tight encapsulation of the ligand" ([PMID: 17889830](https://pubmed.ncbi.nlm.nih.gov/17889830/)). This open→closed motion sequesters the substrate from solvent and juxtaposes the two cysteines with the α-carbon, protecting the carbanion intermediate and enforcing stereocontrol.

### Finding 4 — Substrate specificity: DAP-specific, symmetric two-subsite active site; druggable by aziridine and α-methyl-amino-acid inhibitors

DapF is highly specific for the **diaminopimelate scaffold**. Crystallography of *Arabidopsis* DapF bound to the substrate-mimicking irreversible inhibitor LL-2-(4-amino-4-carboxybutyl)-aziridine-2-carboxylate reveals a **highly symmetric catalytic site** that binds both the L and D stereocenters of DAP at a "proximal" subsite, while specific interactions at a "distal" subsite confer substrate recognition: "the highly symmetric catalytic site that can accommodate both the L and D stereogenic centers of DAP at the proximal site, whereas specific interactions at the distal site" determine specificity ([PMID: 19013471](https://pubmed.ncbi.nlm.nih.gov/19013471/)). The symmetry of the proximal subsite is what allows the enzyme to act on the pseudo-symmetric DAP molecule in both directions.

Specificity for DAP (rather than other amino acids) is encoded in the **distal-site residues**. Homologs sharing the same fold achieve entirely different specificities by substitutions at these positions — e.g., **DcsC** (O-ureidoserine racemase) and **CntK** (histidine racemase) — demonstrating that DapF's DAP selectivity is a tunable property of the distal subsite. In Q88CF3, the predicted binding residues include Asn13, Gln46, Asn66, Asn159, and Asn192, plus backbone contributions from the 210–211 and 220–221 loops. The enzyme is druggable: beyond the aziridine irreversible inhibitor, 2025 work reports "inhibition of diaminopimelic acid epimerase by slow-binding α-methyl amino acids" ([PMID: 40299312](https://pubmed.ncbi.nlm.nih.gov/40299312/)), which act as substrate mimics. Critically, DapF has **no mammalian homolog**, underpinning its value as an antibacterial/herbicide target.

### Finding 5 — Moonlighting function: DapF stimulates RppH-dependent 5′-end mRNA decay

Beyond metabolism, *E. coli* DapF has a well-characterized **second ("moonlighting") role** in mRNA turnover. It physically binds and potentiates the **RNA pyrophosphohydrolase RppH**, the enzyme that removes pyrophosphate from 5′-triphosphorylated/diphosphorylated mRNA termini to generate the 5′-monophosphate ends that trigger 5′-end-dependent RNA degradation. Structural and kinetic work shows "the RNA pyrophosphohydrolase RppH, which can be stimulated by DapF, a diaminopimelate epimerase involved in amino acid and cell wall biosynthesis" ([PMID: 29733359](https://pubmed.ncbi.nlm.nih.gov/29733359/)). DapF enhances RppH reactivity toward diphosphorylated RNAs (the predominant natural substrates) in a length-dependent manner and also boosts triphosphorylated-RNA reactivity via DapF-induced conformational changes in RppH — mechanistically paralleling eukaryotic decapping stimulation. This role is distinct from the epimerase activity and, given the conservation of both proteins, is plausibly retained in *P. putida* (to be confirmed experimentally).

### Finding 6 — Potential redox regulation via a reversible active-site disulfide

Because DapF's two catalytic cysteines sit in close proximity, the enzyme is susceptible to **redox regulation**. Crystal structures of *Corynebacterium glutamicum* DapF under oxidizing vs. reducing conditions show that "the function of CgDapF is regulated by redox-switch modulation via reversible disulfide bond formation between two catalytic cysteine residues" ([PMID: 28176858](https://pubmed.ncbi.nlm.nih.gov/28176858/)). When oxidized, Cys–Cys disulfide formation reorganizes the dynamic active-site loop and locks the enzyme in an inactive state; reduction restores free thiols and activity. A product (D,L-DAP) complex captured the large open→closed domain movement that fully buries the substrate. Since Q88CF3 conserves the same two proximal catalytic cysteines (Cys75/Cys219), an analogous redox switch is structurally plausible in *P. putida* DapF, potentially linking cell-wall/lysine flux to cellular redox state.

### Finding 7 — Pathway placement in *P. putida* KT2440: penultimate step of two DAP-based lysine routes

KEGG assigns **ppu:PP_5228** the orthology **K01778** (diaminopimelate epimerase, EC 5.1.1.7) and maps it to **Lysine biosynthesis (ppu00300)**, **D-Amino acid metabolism (ppu00470)**, **Biosynthesis of amino acids (ppu01230)**, and the global metabolic-pathways maps. *P. putida* KT2440 possesses two DAP-pathway variants that both route through DapF: **module M00016** (succinyl-DAP pathway, aspartate ⇒ lysine) and **module M00527** (DAP-aminotransferase pathway, aspartate ⇒ lysine). In every variant, DapF performs the **LL-DAP → meso-DAP** epimerization immediately upstream of meso-DAP decarboxylation. The protein carries the Pfam **DAP_epimerase (PF01678)** domain and belongs to the **PhzF/DAP-epimerase-like superfamily**.

### Finding 8 — Genomic linkage: dapF is tandem with and overlaps lysA

In the KT2440 genome, dapF is **physically coupled to lysA**. KEGG coordinates place **PP_5227 (lysA-II, diaminopimelate decarboxylase, K01586/EC 4.1.1.20)** at 5,961,105–5,962,352 and **PP_5228 (dapF)** at 5,962,324–5,963,187 on the **same strand**, with the two genes **overlapping by ~29 bp** (the start of dapF precedes the end of lysA). This arrangement is a hallmark of **translational coupling/operonic organization** and physically links the final two enzymatic steps of the pathway: DapF produces meso-DAP, which LysA immediately decarboxylates to L-lysine. The immediate neighbors are a lipoprotein (PP_5226) and an uncharacterized conserved protein (PP_5229).

### Finding 9 — DapF is essential and a validated, mammalian-homolog-free drug target

DapF provides the **only enzymatic route to meso-DAP**, which is indispensable for both L-lysine synthesis and peptidoglycan cross-linking. Loss of DapF therefore blocks cell-wall assembly. In *Mycobacterium tuberculosis*, "The interconversion of L,L-DAP and meso-DAP is catalysed by the DAP epimerase DapF, a gene product that is essential in M. tuberculosis" ([PMID: 19307721](https://pubmed.ncbi.nlm.nih.gov/19307721/)). Because the entire DAP/lysine pathway is absent in mammals, its enzymes are attractive selective targets; a review "discusses the suitability of interrupting lysine biosynthesis as target for new antibacterial and antifungal compounds" ([PMID: 23504110](https://pubmed.ncbi.nlm.nih.gov/23504110/)). As a Gram-negative bacterium that incorporates meso-DAP directly into peptidoglycan, *P. putida* KT2440 is expected, by strong inference, to depend on DapF for viability.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of DapF as the stereochemical gatekeeper at the end of the lysine/DAP pathway.

### Pathway context

```
   L-aspartate
       │  (aspartokinase, ASADH, DapA/B, ...)
       ▼
   ... tetrahydrodipicolinate ...
       │  (succinyl-DAP route M00016  OR  DAP-aminotransferase route M00527)
       ▼
   LL-2,6-diaminopimelate  (LL-DAP)
       │
       │   ┌─────────────────────────────────────────┐
       │   │  DapF (PP_5228, Q88CF3)  EC 5.1.1.7      │
       └──▶│  LL-DAP  ⇌  meso-(D,L)-DAP              │   ← THIS ENZYME
           │  cofactor-independent, 2-Cys mechanism  │
           └─────────────────────────────────────────┘
                         │
          ┌──────────────┴───────────────┐
          ▼                               ▼
   LysA (PP_5227)                 Peptidoglycan
   meso-DAP decarboxylase         (meso-DAP is the 3→4
   EC 4.1.1.20                     cross-linking residue in
          │                        Gram-negative murein)
          ▼
     L-LYSINE
```

### Catalytic model (two-cysteine acid/base epimerization)

```
        Cys75-S⁻ (base)                    Cys75-SH (acid)
             │                                  │
   LL-DAP    │  α-C–H abstraction     planar    │  reprotonation
   H–Cα ─────┼──────────────▶  [ Cα carbanion ] ─┼─────────────▶  meso-DAP
             │                  (stabilized,      │   from opposite face
        Cys219-SH (acid)         encapsulated)   Cys219-S⁻ (base)
```

The reaction is a **1,1-proton transfer**: one thiolate removes the α-proton to generate a resonance-stabilized carbanion, and the second cysteine (thiol) delivers a proton to the opposite face, inverting the stereocenter. Substrate-induced **domain closure** (Finding 3) is essential — it excludes water (preventing non-stereospecific protonation and hydrolysis of the intermediate) and precisely positions the two cysteines. **Dimerization** (Tyr270) is required to complete the catalytically competent active site. The two proximal cysteines that make DapF such an efficient PLP-free catalyst also make it **redox-sensitive** (Finding 6): oxidative disulfide formation switches the enzyme off, offering a plausible regulatory link between cell-wall/lysine flux and redox status.

### Two functions, one protein

| Function | Location | Partner/Substrate | Evidence class |
|----------|----------|-------------------|----------------|
| **Diaminopimelate epimerase** (primary) | Cytoplasm | LL-DAP → meso-DAP | Direct (annotation + extensive DapF structural/kinetic literature) |
| **RppH-stimulating factor** (moonlighting) | Cytoplasm | RppH / mRNA 5′-ends | Direct in *E. coli* ([PMID: 29733359](https://pubmed.ncbi.nlm.nih.gov/29733359/)); inferred for *P. putida* |

### Why the enzyme matters

meso-DAP is a metabolic node unique to bacteria (and plants). Its production by DapF feeds two indispensable outputs — **protein synthesis (via L-lysine)** and **cell envelope integrity (via peptidoglycan cross-linking)**. The genomic fusion-like overlap of dapF with lysA (Finding 8) suggests selection for co-expression/co-regulation of the final two steps, channeling meso-DAP efficiently toward lysine while leaving a pool for peptidoglycan. The absence of the pathway in humans (Finding 9) is the basis for its status as an antibacterial and herbicide target.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports/informs the annotation |
|------|-----------------|----------------------------------------|
| [10194362](https://pubmed.ncbi.nlm.nih.gov/10194362/) | *Chemical mechanism of H. influenzae DAP epimerase* | Defines the LL→D,L(meso)-DAP reaction and establishes PLP-independence + two-cysteine acid/base roles; pH-dependence data (Findings 1, 2) |
| [40774471](https://pubmed.ncbi.nlm.nih.gov/40774471/) | *Cofactor-independent amino acid epimerases with catalytic serines* | States product (D,L-DAP) and dual role in lysine biosynthesis and Gram-negative peptidoglycan (Finding 1) |
| [19013471](https://pubmed.ncbi.nlm.nih.gov/19013471/) | *Crystal structure of Arabidopsis DAP epimerase* | Two-cysteine cofactor-free mechanism; symmetric proximal / specific distal two-subsite active site; aziridine irreversible inhibitor (Findings 2, 4) |
| [17889830](https://pubmed.ncbi.nlm.nih.gov/17889830/) | *Dynamics of catalysis from mutant DAP epimerase structures* | Substrate-induced domain closure encapsulating the ligand (Finding 3) |
| [23426375](https://pubmed.ncbi.nlm.nih.gov/23426375/) | *Dimerization of bacterial DAP epimerase is essential for catalysis* | Y268A monomer is inactive → dimerization required; supports Tyr270/homodimer annotation (Finding 3) |
| [40299312](https://pubmed.ncbi.nlm.nih.gov/40299312/) | *Inhibition of DAP epimerase by slow-binding α-methyl amino acids* | Documents substrate-mimic inhibitors; druggability (Finding 4) |
| [29733359](https://pubmed.ncbi.nlm.nih.gov/29733359/) | *Stimulation of RppH-dependent RNA degradation by DapF* | Direct evidence of DapF moonlighting to stimulate 5′-end mRNA decay (Finding 5) |
| [28176858](https://pubmed.ncbi.nlm.nih.gov/28176858/) | *Redox sensitivity of C. glutamicum DAP epimerase* | Reversible disulfide between catalytic cysteines as a redox switch (Finding 6) |
| [19307721](https://pubmed.ncbi.nlm.nih.gov/19307721/) | *Structure of M. tuberculosis DAP epimerase DapF* | dapF essential in M. tuberculosis; supports inferred essentiality (Finding 9) |
| [23504110](https://pubmed.ncbi.nlm.nih.gov/23504110/) | *Lysine biosynthesis as a drug target* | Validates DAP/lysine pathway (incl. DapF) as antibacterial target absent in mammals (Finding 9) |
| [14747737](https://pubmed.ncbi.nlm.nih.gov/14747737/) | *H. influenzae DapF at 1.75 Å* | High-resolution structure; stereocontrol mechanism; supports fold/mechanism (Findings 2, 3) |
| [34877716](https://pubmed.ncbi.nlm.nih.gov/34877716/) | *O-ureidoserine racemase (DcsC) structure* | Homolog with altered specificity via distal residues (Thr72/Thr198/Tyr219); supports distal-site specificity model (Finding 4) |
| [31129210](https://pubmed.ncbi.nlm.nih.gov/31129210/) | *CntK histidine racemase structure* | Same fold, different specificity via distal residues; two-base mechanism; supports specificity model (Finding 4) |
| [19559030](https://pubmed.ncbi.nlm.nih.gov/19559030/) | *3-methylitaconate-Δ-isomerase (Mii)* | Illustrates the broader DAP-epimerase-fold superfamily and two-domain open/closed architecture |

Database evidence: **UniProt Q88CF3** (DAPF_PSEPK; EC 5.1.1.7; HAMAP MF_00197; ACT_SITE 75/219; SITE 270; Cytoplasm; Homodimer) and **KEGG ppu:PP_5228** (K01778; maps ppu00300/00470/01230; modules M00016, M00527; genomic overlap with PP_5227/lysA).

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 orthologue.** All enzymatic, structural, and kinetic evidence derives from orthologues (*H. influenzae*, *E. coli*, *M. tuberculosis*, *C. glutamicum*, *Arabidopsis*). Q88CF3's function is assigned by strong homology, conserved catalytic residues (Cys75/Cys219, Tyr270), and database annotation — not by a dedicated study of the *P. putida* protein. No purified-enzyme kinetics (kcat, Km for LL-/meso-DAP), no crystal structure, and no gene-knockout phenotype exist specifically for PP_5228.
2. **Essentiality in *P. putida* is inferred, not demonstrated.** Essentiality is established in *M. tuberculosis*; the corresponding gene-deletion experiment has not been reported for KT2440. *P. putida* has two DAP-pathway variants (M00016, M00527), but both converge on DapF, so essentiality is strongly expected.
3. **Moonlighting RppH role is unconfirmed in *P. putida*.** The DapF–RppH interaction is characterized in *E. coli*. Whether the KT2440 orthologue retains this activity, and its physiological significance, is untested.
4. **Redox regulation is a structural inference.** The disulfide redox switch is demonstrated in *C. glutamicum*. Conservation of both cysteines makes it plausible for Q88CF3, but the *in vivo* redox sensitivity of *P. putida* DapF is unknown.
5. **Distal-site binding residues are predicted.** The specific residues (Asn13, Gln46, Asn66, Asn159, Asn192) proposed to determine DAP specificity in Q88CF3 are assigned by homology modeling, not by co-crystal structures of the *P. putida* enzyme.
6. **Possible paralogy (PP_5227 annotated "lysA-II").** The naming implies additional lysine-pathway paralogy in KT2440 that was not exhaustively mapped here; whether any paralog could bypass DapF is not established (biochemically unlikely, as DapF is the only DAP epimerase).

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic validation.** Heterologously express and purify Q88CF3; measure epimerase activity and steady-state kinetics (kcat, Km) for LL-DAP and meso-DAP using a coupled assay (e.g., with meso-DAP dehydrogenase or LysA/decarboxylase readout). Confirm cofactor independence and the pH-rate profile predicted for a two-cysteine mechanism.
2. **Catalytic-residue mutagenesis.** Generate C75S, C219S (and the double mutant) and the Y270A dimerization mutant; test activity to confirm the two-cysteine mechanism and the essentiality of dimerization in the *P. putida* protein.
3. **Genetic essentiality test.** Attempt a clean dapF deletion (or CRISPRi knockdown) in KT2440 with and without exogenous meso-DAP/lysine supplementation to establish essentiality and distinguish the lysine vs. peptidoglycan requirements.
4. **Structure determination.** Solve the crystal or cryo-EM structure of *P. putida* DapF, ideally as a complex with the aziridine inhibitor or meso-DAP, to confirm the two-domain fold, domain closure, distal-site specificity residues, and the geometry of Cys75/Cys219.
5. **Redox-switch assay.** Test whether purified Q88CF3 is reversibly inactivated by oxidation (disulfide formation between Cys75/Cys219) and reactivated by reductant (DTT/thioredoxin), assessing physiological redox regulation.
6. **Moonlighting test.** Perform pull-down/interaction and RNA-deprotection kinetic assays between *P. putida* DapF and its RppH orthologue to determine whether the RNA-decay-stimulating moonlighting function is conserved.
7. **Operon/co-expression analysis.** Use RT-PCR or RNA-seq to confirm whether PP_5227 (lysA) and PP_5228 (dapF) are co-transcribed as a translationally coupled operon, as the ~29 bp overlap suggests.
8. **Inhibitor profiling for biotech relevance.** Given *P. putida*'s use as an industrial chassis, characterize DapF inhibition (aziridine, α-methyl amino acids) to inform metabolic engineering of lysine flux and to explore selective antibacterial leads.

---

## Conclusion

*dapF* (PP_5228, UniProt Q88CF3) of *Pseudomonas putida* KT2440 encodes **diaminopimelate epimerase (EC 5.1.1.7)**, a small, cytoplasmic, cofactor-independent amino-acid epimerase that catalyzes the reversible stereoinversion of **LL-2,6-diaminopimelate to meso-(D,L)-diaminopimelate** — the penultimate step of the DAP branch of L-lysine biosynthesis. It uses a **two-cysteine (Cys75/Cys219) thiol/thiolate acid–base mechanism** with no PLP or metal cofactor, is highly specific for the diaminopimelate scaffold via a symmetric proximal / discriminating distal two-subsite active site, and functions as a **substrate-clamping homodimer** (Tyr270). Its product, **meso-DAP**, is both the direct precursor of L-lysine (decarboxylated by the genomically adjacent LysA/PP_5227) and the cross-linking residue of Gram-negative peptidoglycan, making DapF essential and a validated, mammalian-homolog-free antibacterial/herbicide target. A conserved active-site cysteine pair additionally renders the enzyme potentially redox-regulated, and the *E. coli* orthologue exhibits a documented moonlighting role stimulating RppH-dependent 5′-end mRNA decay.


## Artifacts

- [OpenScientist final report](dapF__Q88CF3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapF__Q88CF3-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:40774471
2. PMID:10194362
3. PMID:19013471
4. PMID:23426375
5. PMID:17889830
6. PMID:40299312
7. PMID:29733359
8. PMID:28176858
9. PMID:19307721
10. PMID:23504110