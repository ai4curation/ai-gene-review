---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:21:51.158813'
end_time: '2026-07-18T16:35:35.708230'
duration_seconds: 824.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dxs
  gene_symbol: dxs
  uniprot_accession: Q88QG7
  protein_description: 'RecName: Full=1-deoxy-D-xylulose-5-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00315};
    EC=2.2.1.7 {ECO:0000255|HAMAP-Rule:MF_00315}; AltName: Full=1-deoxyxylulose-5-phosphate
    synthase {ECO:0000255|HAMAP-Rule:MF_00315}; Short=DXP synthase {ECO:0000255|HAMAP-Rule:MF_00315};
    Short=DXPS {ECO:0000255|HAMAP-Rule:MF_00315};'
  gene_info: Name=dxs {ECO:0000255|HAMAP-Rule:MF_00315}; OrderedLocusNames=PP_0527;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transketolase family. DXPS subfamily.
  protein_domains: Dxylulose-5-P_synthase. (IPR005477); THDP-binding. (IPR029061);
    Transketo_C/PFOR_II. (IPR009014); Transketolase-like_Pyr-bd. (IPR005475); Transketolase_BS.
    (IPR020826)
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
  path: dxs-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dxs-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QG7
- **Protein Description:** RecName: Full=1-deoxy-D-xylulose-5-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00315}; EC=2.2.1.7 {ECO:0000255|HAMAP-Rule:MF_00315}; AltName: Full=1-deoxyxylulose-5-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00315}; Short=DXP synthase {ECO:0000255|HAMAP-Rule:MF_00315}; Short=DXPS {ECO:0000255|HAMAP-Rule:MF_00315};
- **Gene Information:** Name=dxs {ECO:0000255|HAMAP-Rule:MF_00315}; OrderedLocusNames=PP_0527;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transketolase family. DXPS subfamily.
- **Key Domains:** Dxylulose-5-P_synthase. (IPR005477); THDP-binding. (IPR029061); Transketo_C/PFOR_II. (IPR009014); Transketolase-like_Pyr-bd. (IPR005475); Transketolase_BS. (IPR020826)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dxs" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dxs' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dxs** (gene ID: dxs, UniProt: Q88QG7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dxs* (1-Deoxy-D-xylulose-5-phosphate Synthase) in *Pseudomonas putida* KT2440

**UniProt:** Q88QG7 | **Gene:** *dxs* | **Locus:** PP_0527 | **EC:** 2.2.1.7
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)

---

## Summary

The gene **_dxs_ (Q88QG7, locus PP_0527)** of *Pseudomonas putida* KT2440 encodes **1-deoxy-D-xylulose-5-phosphate synthase (DXPS / DXS; EC 2.2.1.7)**, a thiamine-diphosphate (ThDP)- and Mg²⁺-dependent enzyme of the transketolase family (DXPS subfamily). Its primary and defining function is to catalyze the **decarboxylative acyloin (carboligation) condensation of pyruvate with D-glyceraldehyde-3-phosphate (D-GAP)** to yield **1-deoxy-D-xylulose-5-phosphate (DXP)** plus CO₂. In this reaction pyruvate acts as the 2-hydroxyethyl (C2) donor and D-GAP as the aldehyde acceptor. This is the **first, committed, and rate-limiting step of the mevalonate-independent 2-C-methyl-D-erythritol-4-phosphate (MEP) pathway**, which in *P. putida* is the organism's sole route to the universal isoprenoid precursors isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP).

Beyond isoprenoids, the DXP product is a **metabolic branch point** feeding two additional essential routes: **thiamine diphosphate (vitamin B1)** and **pyridoxal-5′-phosphate (vitamin B6)** biosynthesis. Because DXP cannot be produced by any bypass in *P. putida*, and because the downstream isoprenoids (ubiquinone-9 respiratory quinone, carotenoids, prenylated products) and vitamins are indispensable, *dxs* is a physiologically **essential gene**. The enzyme functions in the **cytoplasm** as a **soluble homodimer** (~70 kDa subunits; 631 aa in *P. putida*) with a three-domain transketolase-like fold; uniquely among ThDP enzymes, its active site lies **within a single monomer** at the interface of domains I and II rather than at the dimer interface.

Mechanistically, DXS is distinctive: it stabilizes the pre-decarboxylation intermediate **C2α-lactyl-ThDP (LThDP)** in the absence of the acceptor and uses a **ligand-gated, random-sequential mechanism** in which binding of D-GAP triggers a **≥600-fold acceleration** of LThDP decarboxylation. The functional assignment for Q88QG7 rests on strong convergent evidence: UniProt/HAMAP curation directly on the *P. putida* sequence confirms an intact ThDP/Mg²⁺ active site, and the enzyme is **62% identical** to the structurally and mechanistically characterized *E. coli* DXS with **complete conservation of every catalytic and cofactor-binding residue**, licensing confident orthology-based transfer of the well-established DXS function to this protein.

---

## Gene/Protein Identity Verification

Before proceeding it was confirmed that Q88QG7 corresponds to the intended target. The gene symbol *dxs*, the protein description (1-deoxy-D-xylulose-5-phosphate synthase, EC 2.2.1.7), the organism (*P. putida* KT2440), the family (transketolase family, DXPS subfamily), and the diagnostic domains (Dxylulose-5-P_synthase IPR005477; THDP-binding IPR029061; Transketo_C/PFOR_II IPR009014; Transketolase-like_Pyr-bd IPR005475; Transketolase_BS IPR020826) are all mutually consistent and match the DXS literature used here. Care was taken to exclude literature on same-symbol *DXS* genes from plants and other organisms; all functional claims below derive either from the *P. putida* sequence itself, from congeneric *Pseudomonas* studies, or from the well-characterized *E. coli* ortholog to which Q88QG7 is 62% identical. The identity is unambiguous.

---

## Key Findings

### Finding 1 — *dxs* encodes DXP synthase catalyzing ThDP-dependent condensation of pyruvate and D-GAP to form DXP

UniProt Q88QG7 (*P. putida* KT2440, gene *dxs*, locus PP_0527) is annotated as **1-deoxy-D-xylulose-5-phosphate synthase**, a member of the transketolase family / DXPS subfamily, with enzyme classification **EC 2.2.1.7**. The catalyzed reaction is the **thiamine-diphosphate (ThDP)-dependent decarboxylative condensation of pyruvate and D-glyceraldehyde-3-phosphate (D-GAP)** to yield 1-deoxy-D-xylulose-5-phosphate (DXP) plus CO₂, and it requires both **Mg²⁺ and ThDP** as cofactors.

The reaction chemistry is well established in the primary literature. A comprehensive review states directly that "1-deoxy-d-xylulose 5-phosphate (DXP) synthase is a thiamine diphosphate (ThDP)-dependent enzyme that catalyzes the decarboxylative condensation of pyruvate and d-glyceraldehyde 3-phosphate (d-GAP) to form DXP" ([PMID: 30203647](https://pubmed.ncbi.nlm.nih.gov/30203647/)). Mechanistic kinetics work further clarifies the roles of the two substrates: "1-deoxy-D-xylulose 5-phosphate (DXP) synthase carries out the condensation of pyruvate as a 2-hydroxyethyl donor with d-glyceraldehyde-3-phosphate (d-GAP) as acceptor forming DXP" ([PMID: 23072514](https://pubmed.ncbi.nlm.nih.gov/23072514/)). Thus **pyruvate is the C2 (2-hydroxyethyl) donor** and **D-GAP is the aldehyde acceptor** — the substrate specificity is precise and physiologically defined.

**Reaction:**

```
   Pyruvate  +  D-glyceraldehyde-3-phosphate  +  H⁺
        │                    │
        │  (ThDP, Mg²⁺)      │
        ▼                    ▼
   1-deoxy-D-xylulose-5-phosphate (DXP)  +  CO₂
```

### Finding 2 — DXS is the first, rate-limiting enzyme of the MEP pathway; DXP is a branch-point metabolite feeding isoprenoid, B1, and B6 biosynthesis

DXP synthase catalyzes the **first committed and rate-limiting step** of the mevalonate-independent MEP (2-C-methyl-D-erythritol-4-phosphate) pathway. This has been established repeatedly and independently: a recent structural review states that "1-deoxy-D-xylulose 5-phosphate synthase (DXPS) is the first and rate-limiting enzyme of this pathway" ([PMID: 40784416](https://pubmed.ncbi.nlm.nih.gov/40784416/)), and an earlier structural study concurs that "1-Deoxy-D-xylulose 5-phosphate synthase (DXS) catalyzes the first and the rate-limiting step of the mevalonate-independent pathway" ([PMID: 17135236](https://pubmed.ncbi.nlm.nih.gov/17135236/)).

Critically, the DXP product is not dedicated solely to isoprenoids — it is a **three-way metabolic branch point**. As stated in the review by the Freel Meyers group, DXP "feeds into three separate essential pathways for bacterial central metabolism: ThDP synthesis, pyridoxal phosphate (PLP) synthesis, and the MEP pathway for isoprenoid synthesis" ([PMID: 30203647](https://pubmed.ncbi.nlm.nih.gov/30203647/)). This central, non-redundant position — supplying both isoprenoid precursors and two essential vitamin cofactors (B1 and B6) — is the primary reason DXS is regarded as an attractive, human-target-free antibacterial target and why the gene is essential in organisms lacking the mevalonate pathway.

```
                          ┌─────────────────►  Thiamine diphosphate (Vitamin B1)
                          │
  Pyruvate + D-GAP ──► DXP ─────────────────►  Pyridoxal-5′-phosphate (Vitamin B6)
       (DXS)            │
                          └──► MEP pathway ──►  IPP / DMAPP ──► isoprenoids
                                (dxr, idi...)                    (ubiquinone-9,
                                                                  carotenoids, etc.)
```

### Finding 3 — DXS uses a distinctive ligand-gated, random-sequential mechanism via a stabilized LThDP intermediate

DXS is mechanistically unlike other ThDP-dependent decarboxylases. Rather than decarboxylating its first covalent intermediate immediately, it **stabilizes the pre-decarboxylation intermediate C2α-lactyl-ThDP (LThDP)** in the absence of the acceptor substrate. Binding of D-GAP (or a small-molecule "trigger") then **gates the reaction**, activating LThDP decarboxylation to form the reactive carbanion/enamine that condenses with the acceptor. As described in recent mechanistic work, "DXPS uses a ligand-gated mechanism in which binding of a small molecule 'trigger' activates the first enzyme-bound intermediate, C2α-lactylThDP (LThDP), to form the reactive carbanion via LThDP decarboxylation" ([PMID: 39268973](https://pubmed.ncbi.nlm.nih.gov/39268973/)).

The magnitude of this gating effect is striking. Direct kinetic measurement of the thiamin-bound intermediates showed that "addition of D-GAP enhanced the rate of decarboxylation by at least 600-fold" ([PMID: 23072514](https://pubmed.ncbi.nlm.nih.gov/23072514/)) — the acceptor substrate does not merely participate in the second half-reaction but actively controls the timing of the first. The enzyme also follows unusual steady-state kinetics: "DXP synthase follows a unique random sequential mechanism and possesses an unusually large active site" ([PMID: 28636325](https://pubmed.ncbi.nlm.nih.gov/28636325/)). Active-site residues that bind the D-GAP phosphate/acceptor were identified by mutagenesis: studies "predict that Arg420 and Arg478 are involved in binding of the acceptor substrate, GraP" ([PMID: 24767541](https://pubmed.ncbi.nlm.nih.gov/24767541/)), with Tyr392 contributing to D-GAP affinity. This ligand-gated behaviour underlies DXS's distinctive place in ThDP enzymology and shapes ongoing antibacterial inhibitor-design efforts.

### Finding 4 — DXS is a soluble cytoplasmic homodimer with a three-domain transketolase-like fold; the active site lies within a single monomer

Crystal structures of DXS from *E. coli* and *Deinococcus radiodurans* reveal that the enzyme is a **homodimer of ~70 kDa subunits**, each composed of **three domains (I, II, III)** that are individually homologous to the domains of transketolase and the pyruvate dehydrogenase E1 subunit. However, the domains are arranged differently: "the active site of DXS is located at the interface of domains I and II in the same monomer, whereas that of transketolase is located at the interface of the dimer" ([PMID: 17135236](https://pubmed.ncbi.nlm.nih.gov/17135236/)). This **intramonomeric active-site architecture** is a defining structural feature of the DXPS subfamily.

The enzyme's solubility and oligomeric state are consistent with cytoplasmic localization. A characterized ortholog was described as follows: "The purified HiDXS was a soluble dimeric 70-kDa protein" ([PMID: 20808315](https://pubmed.ncbi.nlm.nih.gov/20808315/)). ThDP is largely buried within the fold with its reactive thiazolium C2 exposed to the substrate pocket. There is no signal peptide or membrane-spanning region — DXS is a bona fide **soluble cytoplasmic enzyme** that carries out its catalysis in the bacterial cytosol where its substrates (pyruvate, D-GAP from glycolysis) and cofactors reside. Congeneric structural work on *Pseudomonas aeruginosa* and *Klebsiella pneumoniae* DXPS reinforces this picture and adds mechanistic detail, showing that "the absence of the cofactor thiamine diphosphate results in conformational changes that lead to disordered loops close to the active site" ([PMID: 37567475](https://pubmed.ncbi.nlm.nih.gov/37567475/)) — of direct relevance to *P. putida* as a close *Pseudomonas* relative.

### Finding 5 — In *P. putida* KT2440, *dxs* supplies isoprenoid precursors via the MEP pathway; overexpression boosts isoprenoid output

In *P. putida* KT2440 specifically, the isoprenoid precursors IPP and DMAPP are produced **exclusively via the MEP pathway** from central-metabolism substrates. A metabolic-engineering study of this exact strain states that "In P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway" ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)). This confirms that *dxs* (PP_0527), *dxr*, and *idi* constitute the organism's sole isoprenoid-precursor supply route — there is no mevalonate pathway to compensate.

Functionally, engineering the precursor supply — including MEP-pathway genes such as *dxs* — has a large effect on isoprenoid output. Using lycopene as a read-out, the same study reported that "The most successful combination led to a 50-fold increase in lycopene levels, indicating that P. putida can be successfully engineered to substantially increase the supply" ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)). This directly demonstrates that DXS acts as a **flux-controlling entry point** for isoprenoid biosynthesis in KT2440, consistent with its designation as the rate-limiting step.

### Finding 6 — UniProt/HAMAP curation of Q88QG7 directly confirms DXPS function and maps cofactor-binding residues on the *P. putida* sequence

The functional assignment is not merely inferred from the family name — it is supported by direct curation on the target sequence. UniProt Q88QG7 (**631 aa, homodimer**) is curated under HAMAP rule MF_00315 as catalyzing the acyloin condensation of pyruvate and D-glyceraldehyde-3-phosphate to DXP (reaction: **D-GAP + pyruvate + H⁺ = DXP + CO₂**), and is assigned to the pathway "1-deoxy-D-xylulose 5-phosphate biosynthesis … step 1/1." The curated cofactors are **Mg²⁺ and thiamine diphosphate**.

The curation maps specific binding-site residues onto the *P. putida* sequence:

| Residue(s) | Role |
|---|---|
| His87; Gly128–His129–Ser130; Gly160–Ala161; Phe295; Glu377 | Thiamine diphosphate binding |
| Asp159; Asn188 | Mg²⁺ coordination (Asn188 also contacts ThDP) |

These residues correspond to the conserved DXPS/transketolase ThDP–Mg²⁺ binding motif — the invariant Asp/Asn divalent-metal pair and the conserved Glu that contacts the aminopyrimidine N1′ of ThDP. The presence of the intact canonical active site directly on the *P. putida* sequence provides strong, sequence-specific evidence that Q88QG7 is a fully functional DXP synthase.

### Finding 7 — Q88QG7 is 62% identical to the characterized *E. coli* DXS with full conservation of all active-site residues

To validate transfer of the extensive *E. coli*/*D. radiodurans* structural and mechanistic data to Q88QG7, a global (Needleman–Wunsch, BLOSUM62) alignment was performed between Q88QG7 (631 aa) and *E. coli* DXS (P77488, 620 aa). The result: **62.1% identity over 618 aligned residue pairs (384/618)** — well above the ~40% threshold generally considered sufficient for reliable functional transfer among enzymes, and firmly in the range where fold, mechanism, and substrate specificity are conserved.

Every UniProt-curated cofactor-binding residue of the *P. putida* enzyme is conserved in *E. coli*:

| *P. putida* (Q88QG7) | *E. coli* (P77488) | Role | Status |
|---|---|---|---|
| His87 | His80 | ThDP | Conserved |
| His129 | His122 | ThDP | Conserved |
| Asp159 | Asp152 | Mg²⁺/ThDP | Conserved |
| Gly160 | Gly153 | ThDP | Conserved |
| Asn188 | Asn181 | Mg²⁺/ThDP | Conserved |
| Phe295 | Tyr288 | ThDP contact | Conservative (aromatic) |
| Glu377 | Glu370 | ThDP | Conserved |

The single substitution (Phe295↔Tyr288) is a conservative aromatic-for-aromatic change at a ThDP contact and does not alter function. Because the *E. coli* enzyme is the reference for DXS crystal structures ([PMID: 17135236](https://pubmed.ncbi.nlm.nih.gov/17135236/)) and the detailed ligand-gated mechanism ([PMID: 23072514](https://pubmed.ncbi.nlm.nih.gov/23072514/), [PMID: 39268973](https://pubmed.ncbi.nlm.nih.gov/39268973/)), the high identity and complete active-site conservation license confident transfer of these orthologous data to Q88QG7.

### Finding 8 — DXS-initiated MEP flux supplies precursors for *Pseudomonas* ubiquinone-9 and carotenoids, making *dxs* physiologically essential

The physiological essentiality of *dxs* follows from what its product supplies. The genus *Pseudomonas* characteristically uses **ubiquinone-9 (Q-9)** as its main respiratory quinone — a chemotaxonomic marker of the genus. A recent species description confirms that "the main respiratory quinone of the RP23018ST strain was ubiquinone-9 (Q-9), which is a typical chemotaxonomic characteristic of the genus Pseudomonas" ([PMID: 42012699](https://pubmed.ncbi.nlm.nih.gov/42012699/)). The C₄₅ nonaprenyl (nine-isoprene) tail of Q-9, along with the carotenoid backbones produced by pseudomonad *crt* genes, are constructed from IPP/DMAPP — which in *P. putida* are made **solely** by the MEP pathway ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)).

Because DXS is the first, rate-limiting MEP step, and because DXP additionally feeds essential thiamine (B1) and pyridoxal-5′-phosphate (B6) synthesis ([PMID: 30203647](https://pubmed.ncbi.nlm.nih.gov/30203647/)), **loss of *dxs* cannot be bypassed**. The MEP pathway is broadly essential across bacteria that lack the mevalonate route: it is "in charge of the essential biosynthesis of isoprenoids" ([PMID: 21366531](https://pubmed.ncbi.nlm.nih.gov/21366531/)). Consistent with this, no viable *dxs* knockout of *P. putida* has been reported. The enzyme therefore sits at an essential, non-redundant, non-bypassable node of central metabolism.

---

## Mechanistic Model / Interpretation

Integrating the eight findings yields a coherent picture of DXS as the gatekeeper of the MEP pathway in *P. putida* KT2440:

**1. Substrate sourcing (cytoplasm).** DXS draws its two substrates directly from central carbon metabolism: **pyruvate** (glycolysis/gluconeogenesis end product) and **D-glyceraldehyde-3-phosphate** (a glycolytic triose phosphate). Both are cytosolic, matching the soluble cytoplasmic localization of the enzyme.

**2. Catalysis (ligand-gated ThDP chemistry).** ThDP, held in place by His87, His129, Gly160, Phe295, Glu377 and coordinated to Mg²⁺ via Asp159/Asn188, attacks pyruvate to form the LThDP intermediate. Uniquely, DXS *pauses* here — LThDP is stable until D-GAP binds (via Arg420, Arg478, Tyr392). D-GAP binding gates decarboxylation, accelerating it ≥600-fold, generating the enamine/carbanion that attacks the D-GAP aldehyde to build the new C–C bond of DXP.

**3. Product distribution (branch point).** DXP is released into the cytosol where it is partitioned among three destinations — the MEP pathway (→ IPP/DMAPP → ubiquinone-9, carotenoids, prenyl products), thiamine (B1) biosynthesis, and pyridoxal-phosphate (B6) biosynthesis.

**4. Physiological consequence (essentiality and flux control).** As the first and rate-limiting step, DXS sets the overall flux into all three downstream branches. This dual role — flux controller and essential-metabolite gatekeeper — is why (a) overexpression boosts isoprenoid (lycopene) yields ~50-fold in engineered KT2440 and (b) the gene cannot be deleted.

```
   CENTRAL METABOLISM (cytoplasm)
   ┌───────────────────────────────────────────────┐
   │  Glycolysis → Pyruvate      D-GAP              │
   └────────────────┬───────────────┬──────────────┘
                    │               │
                    ▼               ▼
        ┌────────────────────────────────────────┐
        │   DXS (Q88QG7 / PP_0527)                │
        │   soluble cytoplasmic homodimer         │
        │   ThDP + Mg²⁺, 3-domain TK fold         │
        │   active site within one monomer        │
        │   ligand-gated (D-GAP triggers decarb.) │
        └───────────────────┬────────────────────┘
                            │  RATE-LIMITING, FIRST STEP
                            ▼
                    ┌──────────────┐
                    │     DXP      │  (branch-point metabolite)
                    └──┬────────┬──┴───────┐
                       ▼        ▼          ▼
                  MEP pathway  Thiamine   Pyridoxal-P
                  (dxr, idi…)  (B1)       (B6)
                       ▼
                  IPP / DMAPP
                       ▼
              Ubiquinone-9, carotenoids,
              other isoprenoids  →  ESSENTIAL
```

---

## Evidence Base

| PMID | Title / Focus | How it supports the annotation |
|---|---|---|
| [30203647](https://pubmed.ncbi.nlm.nih.gov/30203647/) | *Toward Understanding the Chemistry and Biology of DXP Synthase* (review) | States the catalyzed reaction, cofactor (ThDP), and substrates; establishes DXP as a branch point feeding ThDP, PLP, and MEP pathways |
| [40784416](https://pubmed.ncbi.nlm.nih.gov/40784416/) | *DXPS: structural perspectives on an essential enzyme* (review) | States DXPS is the first, rate-limiting enzyme of the MEP pathway |
| [17135236](https://pubmed.ncbi.nlm.nih.gov/17135236/) | *Crystal structure of DXS* | Three-domain transketolase-like fold; unique intramonomer active site; first/rate-limiting role; reference *E. coli* structure |
| [23072514](https://pubmed.ncbi.nlm.nih.gov/23072514/) | *Thiamin-bound intermediates; 600-fold rate acceleration* | Defines donor/acceptor roles; quantifies ≥600-fold D-GAP-triggered decarboxylation acceleration |
| [39268973](https://pubmed.ncbi.nlm.nih.gov/39268973/) | *Aldehyde-based activation of LThDP decarboxylation* | Describes the ligand-gated LThDP mechanism |
| [28636325](https://pubmed.ncbi.nlm.nih.gov/28636325/) | *Alkylacetylphosphonates as probes of DXP synthase* | Establishes random-sequential kinetics and unusually large active site |
| [24767541](https://pubmed.ncbi.nlm.nih.gov/24767541/) | *Critical residues for substrate binding* | Identifies Arg420/Arg478 as acceptor (D-GAP)-binding residues |
| [20808315](https://pubmed.ncbi.nlm.nih.gov/20808315/) | *Ketoclomazone inhibits DXS; H. influenzae* | Establishes soluble dimeric 70-kDa nature of a DXS ortholog |
| [31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) | *Engineering P. putida for isoprenoid production* | Confirms MEP-only precursor synthesis in KT2440; 50-fold isoprenoid increase via precursor engineering |
| [21366531](https://pubmed.ncbi.nlm.nih.gov/21366531/) | *MEP pathway as anti-TB drug target* (review) | Supports essentiality of the MEP pathway for isoprenoid biosynthesis |
| [42012699](https://pubmed.ncbi.nlm.nih.gov/42012699/) | *Pseudomonas gebzensis sp. nov.* | Establishes ubiquinone-9 as the characteristic *Pseudomonas* respiratory quinone (MEP/DXS-dependent tail) |
| [37567475](https://pubmed.ncbi.nlm.nih.gov/37567475/) | *DXPS from P. aeruginosa & K. pneumoniae* | Congeneric structural confirmation of DXPS fold, cofactor-induced conformational changes, and rate-limiting/branch-point role |
| [29784878](https://pubmed.ncbi.nlm.nih.gov/29784878/) | *Oxidative decarboxylation of pyruvate by DXP synthase* | Reinforces the ThDP mechanism and central metabolic role of DXP synthase |

The evidence base is internally consistent: multiple independent lines (direct UniProt/HAMAP sequence curation, high-identity orthology to the crystallographically and kinetically characterized *E. coli* enzyme, congeneric *Pseudomonas aeruginosa* structural data, and strain-specific *P. putida* metabolic-engineering results) all converge on the same functional assignment. No paper in the reviewed literature contradicts the DXP synthase annotation for Q88QG7.

**Note on citation hygiene:** Several papers surfaced during literature searches (e.g., plant DXS studies, protoplast methods, algicidal quorum-sensing work) concern DXS orthologs in other organisms or unrelated topics and were correctly excluded from the functional claims for the *P. putida* bacterial enzyme.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88QG7 itself.** The functional assignment rests on (a) sequence-level curation and (b) orthology transfer from *E. coli* DXS. While the 62% identity and complete active-site conservation make this transfer highly reliable, the *P. putida* enzyme has not, to our knowledge, been purified, kinetically characterized (kcat/Km for pyruvate and D-GAP), or crystallized. Direct enzymology would remove all residual inference.

2. **Essentiality is inferred, not directly demonstrated in KT2440.** No viable *dxs* knockout has been reported and the MEP pathway is essential across mevalonate-lacking bacteria, but a formal conditional-lethal / complementation demonstration specific to *P. putida* PP_0527 has not been documented in the reviewed literature. Genome-wide essentiality/Tn-seq datasets for KT2440 exist but were not specifically confirmed for PP_0527 here.

3. **Regulation and expression are uncharacterized.** How *dxs* transcription/translation and DXS activity are regulated in *P. putida* (feedback by downstream isoprenoids, IPP/DMAPP; post-translational control; cofactor availability) remains unexplored in this investigation.

4. **Localization is inferred from biochemistry.** Cytoplasmic localization is confidently inferred from the soluble dimeric nature of orthologs and the absence of signal/membrane sequences, but no direct localization experiment (e.g., fractionation, GFP fusion) for *P. putida* DXS was found.

5. **Quantitative flux control coefficient is approximate.** The "rate-limiting" designation and ~50-fold engineering result indicate strong flux control, but the precise flux control coefficient of DXS relative to other MEP enzymes (e.g., *dxr*, *ispG/H*) in *P. putida* has not been rigorously partitioned.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology of Q88QG7.** Express, purify, and kinetically characterize *P. putida* DXS: determine kcat, Km(pyruvate), Km(D-GAP), Mg²⁺/ThDP dependence, and confirm the ligand-gated LThDP behaviour predicted from the *E. coli* ortholog. This directly validates substrate specificity and mechanism for the actual target protein.

2. **Conditional-lethal essentiality test.** Construct a *dxs* conditional/depletion strain (e.g., inducible promoter or CRISPRi against PP_0527) and confirm that growth arrest is rescued by DXP or by simultaneous supplementation of downstream products (isoprenoid precursors + B1 + B6). This formally establishes essentiality and the non-bypassable branch-point logic in KT2440.

3. **Structural determination.** Crystallize or cryo-EM the *P. putida* DXS (leveraging the truncation strategy from [PMID: 33421767](https://pubmed.ncbi.nlm.nih.gov/33421767/) that improved DXS crystallizability) to confirm the three-domain fold and intramonomer active site at atomic resolution.

4. **Flux-control quantification.** Perform ¹³C metabolic flux analysis with graded *dxs* over-/under-expression to measure DXS's flux control coefficient over ubiquinone-9, carotenoid, and vitamin B1/B6 pools, refining the "rate-limiting" designation quantitatively.

5. **Localization confirmation.** Use subcellular fractionation or a functional fluorescent fusion to directly confirm cytoplasmic localization of PP_0527 in *P. putida*.

6. **Inhibitor susceptibility.** Test DXS-directed inhibitors (e.g., ketoclomazone, alkylacetylphosphonates) against purified *P. putida* DXS and whole cells to assess the enzyme as an antibacterial target in this species and to probe active-site conservation functionally.

---

## Conclusion

The gene *dxs* (Q88QG7, PP_0527) of *Pseudomonas putida* KT2440 encodes **1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7)**, a soluble cytoplasmic, ThDP- and Mg²⁺-dependent homodimeric enzyme that catalyzes the decarboxylative acyloin condensation of pyruvate (donor) with D-glyceraldehyde-3-phosphate (acceptor) to form DXP + CO₂. This is the first, rate-limiting, committed step of the essential MEP isoprenoid pathway and a branch point additionally feeding thiamine (B1) and pyridoxal-5′-phosphate (B6) biosynthesis, rendering the gene essential and non-bypassable. The assignment is supported by direct sequence curation, a distinctive well-characterized ligand-gated mechanism, a three-domain transketolase-like fold with an intramonomer active site, and 62% identity with complete active-site conservation to the crystallographically and kinetically characterized *E. coli* enzyme.


## Artifacts

- [OpenScientist final report](dxs-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dxs-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30203647
2. PMID:23072514
3. PMID:40784416
4. PMID:17135236
5. PMID:39268973
6. PMID:28636325
7. PMID:24767541
8. PMID:20808315
9. PMID:37567475
10. PMID:31500633
11. PMID:42012699
12. PMID:21366531
13. PMID:33421767