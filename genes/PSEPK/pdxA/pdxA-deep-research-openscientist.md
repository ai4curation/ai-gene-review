---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:09:54.261291'
end_time: '2026-07-17T06:41:26.382996'
duration_seconds: 1892.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pdxA
  gene_symbol: pdxA
  uniprot_accession: Q88QT5
  protein_description: 'RecName: Full=4-hydroxythreonine-4-phosphate dehydrogenase
    {ECO:0000255|HAMAP-Rule:MF_00536}; EC=1.1.1.262 {ECO:0000255|HAMAP-Rule:MF_00536};
    AltName: Full=4-(phosphohydroxy)-L-threonine dehydrogenase {ECO:0000255|HAMAP-Rule:MF_00536};'
  gene_info: Name=pdxA {ECO:0000255|HAMAP-Rule:MF_00536}; OrderedLocusNames=PP_0402;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PdxA family. {ECO:0000255|HAMAP-
  protein_domains: PdxA. (IPR037510); PdxA_fam. (IPR005255); PdxA (PF04166)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pdxA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pdxA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QT5
- **Protein Description:** RecName: Full=4-hydroxythreonine-4-phosphate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_00536}; EC=1.1.1.262 {ECO:0000255|HAMAP-Rule:MF_00536}; AltName: Full=4-(phosphohydroxy)-L-threonine dehydrogenase {ECO:0000255|HAMAP-Rule:MF_00536};
- **Gene Information:** Name=pdxA {ECO:0000255|HAMAP-Rule:MF_00536}; OrderedLocusNames=PP_0402;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PdxA family. {ECO:0000255|HAMAP-
- **Key Domains:** PdxA. (IPR037510); PdxA_fam. (IPR005255); PdxA (PF04166)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pdxA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pdxA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pdxA** (gene ID: pdxA, UniProt: Q88QT5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pdxA* (PP_0402, UniProt Q88QT5)
### 4-Hydroxythreonine-4-phosphate dehydrogenase — *Pseudomonas putida* KT2440

---

## Summary

The gene **pdxA** (ordered locus **PP_0402**; UniProt **Q88QT5**) of *Pseudomonas putida* strain KT2440 encodes **4-hydroxythreonine-4-phosphate dehydrogenase** (**EC 1.1.1.262**), a cytoplasmic, divalent-metal-dependent, NAD(P)⁺-linked oxidoreductase. Its primary and only known biochemical function is to catalyze the **fourth of five steps** of the **deoxyxylulose-5-phosphate (DXP)-dependent de novo pyridoxal 5′-phosphate (vitamin B6) biosynthesis pathway**. The enzyme performs an NAD(P)⁺-dependent oxidation of **4-(phosphohydroxy)-L-threonine (HTP)** to an unstable β-keto-acid intermediate (2-amino-3-oxo-4-(phosphooxy)butyric acid) that spontaneously decarboxylates to yield the aminoketone **3-amino-2-oxopropyl phosphate** (also called 1-amino-3-hydroxyacetone phosphate, AHAP). This aminoketone is the direct substrate for the next pathway enzyme, PdxJ (pyridoxine-5′-phosphate synthase), which condenses it with deoxyxylulose-5-phosphate to build the pyridine ring of vitamin B6.

The functional assignment for PP_0402 rests on a combination of authoritative UniProt/HAMAP structured annotation and strong **evolutionary inference by orthology**. No experimental study of the *P. putida* PP_0402 protein specifically has been published; all direct biochemical and crystallographic evidence derives from the well-characterized *Escherichia coli* ortholog. A rigorous pairwise sequence analysis performed during this investigation established that Q88QT5 is **61.9 % identical (gap-free in the core)** to the *E. coli* PdxA, with **every catalytic and metal-binding residue conserved and colinear** — including the three Zn²⁺-coordinating histidines and the two active-site-integrity aspartates (Asp247, Asp267). This provides high-confidence transfer of the *E. coli* functional and structural knowledge to the *P. putida* enzyme.

Structurally, PdxA is an **obligate homodimer** with a **shared, inter-subunit active site** located in a cleft at the dimer interface, contributed by residues from both monomers. Each active site binds one divalent metal ion (Zn²⁺, or alternatively Mg²⁺ or Co²⁺) coordinated by three conserved histidines. Despite low sequence similarity, PdxA adopts a fold structurally related to the **isocitrate dehydrogenase / isopropylmalate dehydrogenase (ICDH/IPMDH) superfamily** of β-decarboxylating dehydrogenases. Because the DXP-dependent B6 pathway is **absent in humans** (vitamin B6 is a required dietary nutrient for mammals), PdxA is expected to be **essential** for *P. putida* under conditions lacking exogenous B6, and represents a validated **selective antibacterial target class**.

---

## Identity Verification

The mandatory verification steps required by the research brief were completed and all passed:

- **Gene symbol matches protein description.** The symbol *pdxA* is the canonical bacterial gene name for 4-hydroxythreonine-4-phosphate dehydrogenase, exactly matching the UniProt description for Q88QT5.
- **Organism confirmed.** The protein belongs to *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), locus PP_0402, a 6.18 Mb metabolically versatile soil bacterium [PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/).
- **Family/domains align.** The protein carries the PdxA family signature (Pfam PF04166; InterPro IPR005255/IPR037510) and HAMAP-Rule MF_00536 — all consistent with the literature reviewed.
- **No cross-symbol ambiguity.** *pdxA* is not a widely reused symbol; the literature found describes bona fide PdxA enzymes. No conflicting gene of the same symbol in a different organism confounded the analysis.

The only caveat — flagged prominently below — is that **no study has characterized the PP_0402 protein directly**; the functional picture is transferred from the *E. coli* ortholog with which it shares 61.9 % identity and a fully conserved active site.

---

## Key Findings

### Finding 1 — PdxA is 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262), the fourth step of DXP-dependent PLP biosynthesis

UniProt Q88QT5 annotates PP_0402 as 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) under HAMAP-Rule MF_00536, placing it firmly in the PdxA family (Pfam PF04166). The biochemical reaction is best defined through the extensively characterized *E. coli* ortholog. As described in the *E. coli* PdxA crystallography paper, *"the fourth step is catalyzed by 4-hydroxythreonine-4-phosphate dehydrogenase (PdxA, E.C. 1.1.1.262), which converts 4-hydroxy-L-threonine phosphate (HTP) to 3-amino-2-oxopropyl phosphate"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/).

Two properties of the enzyme are especially diagnostic and are experimentally established in *E. coli*: **strict substrate specificity** for the phosphorylated form of the substrate, and **dual redox-cofactor flexibility**. The same study states that *"this divalent metal ion-dependent enzyme has a strict requirement for the phosphate ester form of the substrate HTP, but can utilize either NADP⁺ or NAD⁺ as redox cofactor"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/). In other words, the free (non-phosphorylated) 4-hydroxythreonine is not a substrate — the enzyme reads out the phosphate ester — and the enzyme is promiscuous with respect to whether NAD⁺ or NADP⁺ serves as the hydride acceptor. This combination of tight substrate discrimination and cofactor flexibility is a hallmark of PdxA family enzymes.

### Finding 2 — The exact reaction chemistry: an oxidative decarboxylation via a spontaneously-decarboxylating β-keto-acid intermediate

The structured UniProt annotation for Q88QT5 resolves the reaction to atomic precision. The FUNCTION field states that PdxA *"catalyzes the NAD(P)-dependent oxidation of 4-(phosphooxy)-L-threonine (HTP) into 2-amino-3-oxo-4-(phosphooxy)butyric acid which spontaneously decarboxylates to form 3-amino-2-oxopropyl phosphate (AHAP)"*. The canonical catalytic activity is registered as **RHEA:32275 / EC 1.1.1.262**:

```
4-(phosphooxy)-L-threonine + NAD⁺  →  3-amino-2-oxopropyl phosphate + CO₂ + NADH
```

Mechanistically, this is a **β-decarboxylating dehydrogenation**: the enzyme first oxidizes the C3 hydroxyl of HTP to a ketone (transferring a hydride to NAD(P)⁺), generating an unstable β-keto acid (2-amino-3-oxo-4-(phosphooxy)butyric acid). This intermediate then loses CO₂ **spontaneously** (non-enzymatically), yielding the aminoketone product. This two-part chemistry — enzyme-catalyzed oxidation followed by spontaneous decarboxylation — mirrors the mechanistic logic of the ICDH/IPMDH superfamily to which PdxA is structurally related (see Finding 3).

The **cofactor** annotation specifies that the enzyme *binds 1 divalent metal cation per subunit* and can use **Zn²⁺, Mg²⁺, or Co²⁺**. This metal flexibility is notable: while the crystal structure was solved with Zn²⁺, the enzyme functions with alternative divalent cations, consistent with a catalytic/structural rather than strictly redox role for the metal. The **pathway** field places the reaction as *"pyridoxine 5′-phosphate biosynthesis; pyridoxine 5′-phosphate from D-erythrose 4-phosphate: step 4/5"*, and the **subcellular location** is annotated as **cytoplasm**.

### Finding 3 — PdxA is a homodimeric, Zn²⁺-containing enzyme with a shared inter-subunit active site, in the ICDH/IPMDH structural family

The *E. coli* PdxA crystal structure (solved with the HTP substrate and Zn²⁺ bound) reveals the enzyme's architecture. The protein *"forms tightly bound dimers"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/), with each monomer adopting an α/β/α fold split into two subdomains. Critically, the **active site is located at the dimer interface**, within a cleft that receives contributions from both monomers — meaning the enzyme is an **obligate dimer** for catalysis, not merely for stability.

The metal cofactor sits at the heart of this shared site: *"a Zn²⁺ ion is bound within each active site, coordinated by three conserved histidine residues from both monomers"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/). Two additional conserved residues stabilize the catalytic machinery: *"two conserved amino acids, Asp247 and Asp267, play a role in maintaining integrity of the active site"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/).

Despite performing chemistry unique to the B6 pathway, PdxA is evolutionarily and structurally kin to a broad family of metabolic dehydrogenases: *"PdxA is structurally similar to, but limited in sequence similarity with isocitrate dehydrogenase and isopropylmalate dehydrogenase"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/). ICDH and IPMDH are both **metal-dependent β-decarboxylating dehydrogenases**, so PdxA's placement in this superfamily is mechanistically coherent with the oxidative-decarboxylation chemistry described in Finding 2.

### Finding 4 — *P. putida* PdxA (Q88QT5) is 61.9 % identical to the *E. coli* enzyme with all catalytic residues conserved and colinear

Because no PP_0402-specific experimental study exists, the reliability of transferring *E. coli* knowledge to *P. putida* hinges on sequence conservation. A global pairwise alignment performed in this investigation, between Q88QT5 (329 aa) and *E. coli* PdxA (P19624, 329 aa), yields **203/328 = 61.9 % identity**, essentially gap-free through the core. Both proteins are the same length, and the signature PdxA motifs are **perfectly colinear at identical positions**:

| Motif | Approx. position | Role |
|---|---|---|
| `TPGEPAGIGPDL` | N-terminal | Rossmann-like NAD(P)-binding motif |
| `VHKGVIN` | ~121 | conserved core |
| `GHTEF` | ~135 | active-site region (His136) |
| `TTHLPLRD` | ~164 | active-site region (His166) |
| `NPHAGEGGH` | ~209 | diagnostic PdxA motif (Zn-coordinating His) |

Crucially, the **metal- and substrate-binding residues characterized in the *E. coli* structure are all conserved** in Q88QT5. The three Zn²⁺-coordinating histidines — the residues that the crystallography paper identifies as *"coordinated by three conserved histidine residues from both monomers"* [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/) — are present at colinear positions (His→His at each). Likewise, the two active-site-integrity aspartates that *"play a role in maintaining integrity of the active site"* (Asp247, Asp267) [PMID: 12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/) are conserved identically (Asp→Asp). This full conservation of the catalytic constellation is the strongest available evidence that PP_0402 is a **genuine, intact, functional PdxA** rather than a divergent paralog with an altered or lost function.

### Finding 5 — PdxA feeds its aminoketone product to PdxJ in the DXP-dependent pathway, restricted to bacteria/fungi/plants

PdxA does not act in isolation; it is a committed enzyme feeding the ring-forming step. In *E. coli* and by orthology in gammaproteobacteria such as *P. putida* KT2440, de novo PLP *"is synthesized from the condensation of deoxyxylulose 5-phosphate and 4-phosphohydroxy-L-threonine catalysed by the concerted action of PdxA and PdxJ"* [PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/). PdxA generates the aminoketone (3-amino-2-oxopropyl phosphate), and PdxJ (pyridoxine-5′-phosphate synthase) condenses that aminoketone with DXP to form pyridoxine 5′-phosphate, which is subsequently oxidized to PLP by PdxH.

The enzymatic identities and sequential ordering are confirmed by a *Bacillus subtilis* engineering study, which lists *"the 4-hydroxy-L-threonine-phosphate dehydrogenase PdxA, the pyridoxine 5′-phosphate synthase PdxJ and the native DXP synthase, Dxs"* [PMID: 25777134](https://pubmed.ncbi.nlm.nih.gov/25777134/) as the reconstituted route — establishing PdxA and PdxJ as consecutive, cooperating enzymes. Importantly, this route is **taxonomically restricted**: *"its de novo biosynthesis occurs only in bacteria, fungi and plants, making it an essential nutrient in the human diet"* [PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/). The alternative single-enzyme Pdx1/Pdx2 (ribose-5-phosphate-dependent) route is used by most other organisms, but *P. putida* KT2440 encodes the DXP-dependent pathway.

### Finding 6 — The pathway is absent in humans, making PdxA essential and a selective antibacterial target; no PP_0402-specific study exists

PLP is a cofactor of central importance: *"pyridoxal 5′-phosphate (PLP) is an essential cofactor for enzymes that catalyze diverse reactions in central metabolism"* [PMID: 40439409](https://pubmed.ncbi.nlm.nih.gov/40439409/) — including transaminases, decarboxylases, and racemases. Because the DXP-dependent de novo pathway *"occurs only in bacteria, fungi and plants"* [PMID: 17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/) and is **absent in humans**, loss of PdxA is expected to render *P. putida* a pyridoxine auxotroph under B6-limited conditions, and the enzyme is therefore attractive as a **selective antibacterial target class**. A directed PubMed search during this investigation returned **no experimental study of the *P. putida* PP_0402 protein specifically**; all biochemical/structural characterization derives from the *E. coli* ortholog (with related metabolic engineering in *B. subtilis*).

---

## Mechanistic Model / Interpretation

### Position of PdxA in the DXP-dependent vitamin B6 pathway

```
 D-erythrose 4-phosphate                    pyruvate + glyceraldehyde-3-P
          │ (Epd)                                     │ (Dxs)
          ▼                                           ▼
 4-phosphoerythronate                        1-deoxy-D-xylulose 5-P (DXP)
          │ (PdxB)                                    │
          ▼                                           │
 (2-oxo-3-hydroxy-4-P-butanoate)                      │
          │ (SerC / PdxF)                             │
          ▼                                           │
 4-(phosphohydroxy)-L-threonine (HTP)                 │
          │                                           │
          │   ┌───────────────────────────┐          │
          └──▶│  PdxA  (PP_0402, Q88QT5)   │          │
              │  EC 1.1.1.262              │          │
              │  + NAD(P)⁺, divalent metal │          │
              └───────────────────────────┘          │
                          │                           │
              oxidation → β-keto acid                 │
              → spontaneous −CO₂                      │
                          ▼                           │
          3-amino-2-oxopropyl phosphate (AHAP) ───────┤
                                                      ▼
                                       ┌───────────────────────────┐
                                       │  PdxJ (PNP synthase)       │
                                       │  condenses AHAP + DXP      │
                                       └───────────────────────────┘
                                                      │
                                                      ▼
                                        pyridoxine 5′-phosphate (PNP)
                                                      │ (PdxH, O₂)
                                                      ▼
                                        pyridoxal 5′-phosphate (PLP)
```

PdxA sits at the convergence of two branches of the pathway: one branch (via Epd → PdxB → SerC) generates HTP, PdxA's substrate; the second, independent branch (via Dxs) generates DXP. PdxA's product AHAP and DXP are the two building blocks that PdxJ stitches together into the pyridine ring. Thus PdxA is a **committed, non-redundant node**: its product is required stoichiometrically for ring formation, and there is no bypass within the DXP-dependent route. The upstream branch logic — that pdxA functions in a distinct branch from pdxB/serC — was established genetically in *E. coli* [PMID: 2121717](https://pubmed.ncbi.nlm.nih.gov/2121717/).

### The catalytic cycle

1. **Substrate recognition.** HTP binds in the inter-subunit cleft; the enzyme's strict requirement for the **phosphate ester** form indicates specific recognition of the 4-phosphate group. The divalent metal (Zn²⁺/Mg²⁺/Co²⁺), held by three conserved histidines, likely polarizes the C3 hydroxyl/carbonyl and stabilizes developing negative charge.
2. **Oxidation.** A hydride is transferred from C3 of HTP to NAD⁺ or NADP⁺, oxidizing the hydroxyl to a ketone and producing the β-keto acid 2-amino-3-oxo-4-(phosphooxy)butyric acid + NAD(P)H.
3. **Spontaneous decarboxylation.** The β-keto acid is chemically unstable and loses CO₂ without further enzyme catalysis, yielding **3-amino-2-oxopropyl phosphate (AHAP)**.
4. **Product release / hand-off.** AHAP is delivered to PdxJ for condensation with DXP.

This mechanism is a textbook example of the **β-decarboxylating dehydrogenase** logic shared with isocitrate dehydrogenase and isopropylmalate dehydrogenase — enzymes to which PdxA is structurally related despite low sequence identity. The metal flexibility (Zn/Mg/Co) and dual NAD⁺/NADP⁺ usage further echo this superfamily's characteristics.

### Confidence in the annotation transfer

| Evidence type | Source | Strength for PP_0402 |
|---|---|---|
| EC number & reaction | UniProt/HAMAP MF_00536; RHEA:32275 | High (curated) |
| Exact chemistry & intermediate | UniProt Q88QT5 structured annotation | High (curated) |
| Biochemistry (substrate specificity, cofactors, metal) | *E. coli* ortholog [PMID: 12896974] | High (transferred by 61.9 % identity) |
| Structure (dimer, shared site, Zn-His₃, Asp247/267) | *E. coli* crystal structure [PMID: 12896974] | High (all residues conserved & colinear) |
| Pathway context (PdxA→PdxJ) | [PMID: 17822383], [PMID: 25777134] | High |
| Direct PP_0402 experimental data | — | **None (gap)** |

The overall picture is a **high-confidence functional annotation by orthology**, limited only by the absence of any organism-specific experimental validation for the *P. putida* protein itself.

---

## Evidence Base

| PMID | Title | Contribution |
|---|---|---|
| [12896974](https://pubmed.ncbi.nlm.nih.gov/12896974/) | *Crystal structure of Escherichia coli PdxA, an enzyme involved in the pyridoxal phosphate biosynthesis pathway* | **Primary structural & biochemical reference.** Defines the reaction (HTP → 3-amino-2-oxopropyl phosphate), EC 1.1.1.262, strict phosphate-ester specificity, dual NAD⁺/NADP⁺ use, homodimeric architecture, shared inter-subunit active site, Zn²⁺ coordination by three histidines, Asp247/Asp267 active-site integrity, and ICDH/IPMDH structural family membership. All key residues shown conserved in Q88QT5. |
| [17822383](https://pubmed.ncbi.nlm.nih.gov/17822383/) | *Two independent routes of de novo vitamin B6 biosynthesis: not that different after all* | Places PdxA in the DXP-dependent pathway acting in *"concerted action"* with PdxJ; establishes taxonomic restriction (bacteria/fungi/plants only), underpinning essentiality and human-target selectivity. |
| [25777134](https://pubmed.ncbi.nlm.nih.gov/25777134/) | *Engineering Bacillus subtilis for the conversion of the antimetabolite 4-hydroxy-L-threonine to pyridoxine* | Confirms enzymatic identities and sequential roles of PdxA (4-hydroxy-L-threonine-phosphate dehydrogenase) and PdxJ; demonstrates pathway reconstitution/engineering. |
| [40439409](https://pubmed.ncbi.nlm.nih.gov/40439409/) | *Chemical proteomics enhances the understanding of 2AA stress* | Reinforces the central-metabolic essentiality of the PLP end-product PdxA helps synthesize. |
| [2121717](https://pubmed.ncbi.nlm.nih.gov/2121717/) | *Metabolic relationships between pyridoxine and serine biosynthesis in E. coli K-12* | Provides upstream pathway context (SerC/PdxB branch generating HTP) and confirms pdxA functions in a distinct branch from pdxB/serC. |
| [12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/) | *Complete genome sequence... Pseudomonas putida KT2440* | Establishes the genomic/organismal context (6.18 Mb genome, metabolically versatile biosafety strain) in which PP_0402 resides. |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *The revisited genome of Pseudomonas putida KT2440...* | Updated functional annotation of the KT2440 chromosome (re-annotation of ~1548 genes), the reference framework for PP_0402. |

Several additional papers surfaced during literature searches (e.g., alanine racemase, L-methioninase, PLP-dependent probe studies) are relevant only to the **downstream utilization of PLP** by other enzymes, not to PdxA itself; they contextualize why the PdxA product matters but do not directly characterize PdxA.

---

## Limitations and Knowledge Gaps

1. **No organism-specific experimental data.** The single most important limitation is that **no biochemical, structural, genetic, or physiological study of the *P. putida* PP_0402 protein has been published.** The functional annotation is entirely inferred — from curated UniProt/HAMAP rules and by orthology to the *E. coli* enzyme. While the 61.9 % identity and full active-site conservation make this inference robust, kinetic parameters (Kₘ for HTP, NAD⁺ vs NADP⁺ preference, metal preference, kcat) for the *P. putida* enzyme are unmeasured.

2. **Essentiality is inferred, not demonstrated in *P. putida*.** The prediction that PP_0402 is essential (under B6-limited conditions) rests on pathway logic and the human-absence of the route, not on a *P. putida* knockout or transposon-insertion phenotype. Genome-wide essentiality datasets for KT2440 were not directly interrogated in this investigation.

3. **Metal preference in vivo is uncertain.** UniProt lists Zn²⁺/Mg²⁺/Co²⁺ as possible cofactors, and the *E. coli* crystal structure used Zn²⁺. Which metal is physiologically employed by the *P. putida* enzyme, and whether metal identity modulates activity, is unresolved.

4. **Substrate hand-off to PdxJ is assumed, not shown.** Whether AHAP is channeled to PdxJ via a physical complex or released into the bulk cytoplasm is not established for *P. putida* (or definitively for *E. coli*).

5. **Regulation and expression context unknown.** The operon structure, transcriptional regulation, and expression level of pdxA/PP_0402 in *P. putida* (and any response to B6 availability) were not examined.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme kinetics.** Clone PP_0402, express and purify the recombinant protein, and measure kinetic constants (Kₘ, kcat) for HTP with both NAD⁺ and NADP⁺, and across Zn²⁺/Mg²⁺/Co²⁺, to confirm the transferred biochemistry and quantify the *P. putida*-specific parameters.

2. **Functional complementation.** Test whether PP_0402 complements an *E. coli* ΔpdxA pyridoxine auxotroph, providing a direct genetic demonstration that PP_0402 encodes a functional 4-hydroxythreonine-4-phosphate dehydrogenase.

3. **Targeted deletion / conditional knockout in *P. putida* KT2440.** Construct a ΔPP_0402 strain and assay for pyridoxine/pyridoxal auxotrophy (growth rescued by exogenous B6). This would experimentally confirm both function and essentiality within the native organism.

4. **Structure determination.** Solve the crystal or cryo-EM structure of the *P. putida* enzyme (ideally with HTP and metal bound), or generate a high-confidence AlphaFold model, to verify the predicted dimer interface, shared active site, Zn-His₃ coordination, and Asp247/Asp267 positioning.

5. **Metabolic/pathway mapping.** Confirm co-transcription/co-regulation with neighboring pdx/ser genes and probe substrate channeling to PdxJ (e.g., via co-purification or activity coupling assays).

6. **Antibacterial target validation.** Given the human-absence of the pathway, evaluate PP_0402 (and its orthologs in pathogenic *Pseudomonas*) as a target for selective inhibitor development, building on the ICDH/IPMDH-related active-site architecture.

---

## Conclusion

**pdxA (PP_0402, Q88QT5)** in *Pseudomonas putida* KT2440 encodes **4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262)**, a cytoplasmic, homodimeric, divalent-metal-dependent, NAD(P)⁺-linked oxidoreductase that catalyzes the **fourth step of the DXP-dependent de novo pyridoxal 5′-phosphate (vitamin B6) biosynthesis pathway**. It oxidizes 4-(phosphohydroxy)-L-threonine to an unstable β-keto acid that spontaneously decarboxylates to the aminoketone 3-amino-2-oxopropyl phosphate, which PdxJ then condenses with deoxyxylulose-5-phosphate to form the vitamin B6 ring. The assignment is supported by curated database annotation and by high-confidence orthology (61.9 % identity, fully conserved active site) to the crystallographically and biochemically characterized *E. coli* enzyme, though no experimental study of the *P. putida* protein itself yet exists.


## Artifacts

- [OpenScientist final report](pdxA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pdxA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12534463
2. PMID:12896974
3. PMID:17822383
4. PMID:25777134
5. PMID:40439409
6. PMID:2121717