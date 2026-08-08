---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T09:11:25.393883'
end_time: '2026-07-15T09:44:00.560951'
duration_seconds: 1955.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rpiA
  gene_symbol: rpiA
  uniprot_accession: Q88CN0
  protein_description: 'RecName: Full=Ribose-5-phosphate isomerase A {ECO:0000255|HAMAP-Rule:MF_00170};
    EC=5.3.1.6 {ECO:0000255|HAMAP-Rule:MF_00170}; AltName: Full=Phosphoriboisomerase
    A {ECO:0000255|HAMAP-Rule:MF_00170}; Short=PRI {ECO:0000255|HAMAP-Rule:MF_00170};'
  gene_info: Name=rpiA {ECO:0000255|HAMAP-Rule:MF_00170}; OrderedLocusNames=PP_5150;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ribose 5-phosphate isomerase family.
  protein_domains: NagB/RpiA_transferase-like. (IPR037171); Ribose5P_isomerase_typA_subgr.
    (IPR020672); Ribose5P_isomerase_type_A. (IPR004788); Rib_5-P_isom_A (PF06026)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rpiA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rpiA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CN0
- **Protein Description:** RecName: Full=Ribose-5-phosphate isomerase A {ECO:0000255|HAMAP-Rule:MF_00170}; EC=5.3.1.6 {ECO:0000255|HAMAP-Rule:MF_00170}; AltName: Full=Phosphoriboisomerase A {ECO:0000255|HAMAP-Rule:MF_00170}; Short=PRI {ECO:0000255|HAMAP-Rule:MF_00170};
- **Gene Information:** Name=rpiA {ECO:0000255|HAMAP-Rule:MF_00170}; OrderedLocusNames=PP_5150;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ribose 5-phosphate isomerase family.
- **Key Domains:** NagB/RpiA_transferase-like. (IPR037171); Ribose5P_isomerase_typA_subgr. (IPR020672); Ribose5P_isomerase_type_A. (IPR004788); Rib_5-P_isom_A (PF06026)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rpiA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rpiA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rpiA** (gene ID: rpiA, UniProt: Q88CN0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: rpiA (Ribose-5-phosphate Isomerase A) in *Pseudomonas putida* KT2440

**Gene:** rpiA (OrderedLocusName PP_5150)
**UniProt:** [Q88CN0](https://www.uniprot.org/uniprotkb/Q88CN0) (RPIA_PSEPK)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**EC number:** 5.3.1.6
**Protein family:** Ribose 5-phosphate isomerase family (type A)

---

## Summary

The gene **rpiA** (PP_5150) of *Pseudomonas putida* KT2440 encodes **ribose-5-phosphate isomerase A (RpiA)**, also called phosphoriboisomerase A (PRI), a 224-residue soluble cytoplasmic enzyme classified as EC 5.3.1.6. Its single, well-defined catalytic function is the **reversible aldose–ketose isomerization of D-ribose-5-phosphate (R5P) ⇌ D-ribulose-5-phosphate (Ru5P)** — the sole isomerization step of the non-oxidative branch of the pentose phosphate pathway (PPP). This reaction connects the pentose phosphate pool to nucleotide, histidine, aromatic amino acid and cofactor biosynthesis, and to the recycling of carbon skeletons among sugar phosphates. The functional assignment rests on HAMAP rule MF_00170, on strong sequence and structural homology to biochemically characterized RpiA orthologs, and on the evolutionary invariance of the catalytic machinery.

Identity and function are assigned with **high confidence**. Q88CN0 shares **63.5% amino-acid identity** with the structurally and biochemically characterized *Escherichia coli* RpiA (P0A7Z0), and every catalytic and substrate-binding residue maps one-to-one onto its *E. coli* counterpart. The catalytic base is **Glu107** (a proton acceptor that abstracts the C2 proton to form a high-energy cis-enediol(ate) intermediate), supported by a conserved substrate-binding constellation (the TGST, DGAD and KGGG motifs, and Lys125). An AlphaFold model of Q88CN0 confirms the canonical RpiA fold at very high confidence (mean pLDDT 97.7) with a well-ordered active site. The catalytic glutamate is strictly conserved across RpiA orthologs from bacteria to human.

A key physiological feature is that **RpiA is the sole ribose-5-phosphate isomerase in *P. putida* KT2440**: unlike *E. coli*, which carries both *rpiA* and the analogous, structurally unrelated *rpiB*, the KT2440 genome encodes no RpiB paralog. RpiA therefore carries the entire physiological flux of 5-carbon sugar isomerization and is predicted to be essential. In the metabolic context of KT2440 — an organism that catabolizes glucose primarily through the Entner–Doudoroff route within a hybrid **EDEMP cycle** biased toward NADPH overproduction — RpiA operates within the non-oxidative PPP reactions that recycle triose and pentose phosphates and supply biosynthetic precursors.

---

## Key Findings

### Finding 1 — RpiA catalyzes the reversible R5P ⇌ Ru5P isomerization (EC 5.3.1.6)

UniProt entry Q88CN0 (RPIA_PSEPK; gene *rpiA*; locus PP_5150) is annotated by HAMAP rule MF_00170 as **ribose-5-phosphate isomerase A**, EC 5.3.1.6, in the ribose 5-phosphate isomerase family, carrying the NagB/RpiA_transferase-like fold and the Pfam PF06026 domain. The reaction catalyzed is the aldose–ketose interconversion between D-ribose-5-phosphate and D-ribulose-5-phosphate, which is the defining reaction of the non-oxidative pentose phosphate pathway. The protein is a 224-residue cytoplasmic enzyme.

An authoritative review of ribose-5-phosphate isomerases explicitly frames this role: RpiA "has a pivotal role in the pentose phosphate pathway and [is] responsible for catalyzing the isomerization between D-ribulose 5-phosphate and D-ribose 5-phosphate" ([PMID: 32533303](https://pubmed.ncbi.nlm.nih.gov/32533303/)). This establishes both the EC 5.3.1.6 reaction and the PPP role of the enzyme.

### Finding 2 — RpiA is the housekeeping 5-carbon-sugar isomerase; its loss causes ribose auxotrophy

Two structurally unrelated, analogous enzyme families catalyze the same isomerization: **RpiA** (the near-ubiquitous, highly conserved form) and **RpiB** (a distinct fold found in some bacteria and eukaryotes). Genetic evidence in *E. coli* pinpoints RpiA as the enzyme that carries the essential physiological flux. Strains defective in *rpiA* "are ribose auxotrophs, despite the presence of the wild-type *rpiB* gene, which encodes ribose phosphate isomerase B" ([PMID: 8576032](https://pubmed.ncbi.nlm.nih.gov/8576032/)). In other words, RpiB cannot compensate for RpiA loss under normal conditions.

Further work clarified the division of labor between the two families: "the essential 5-carbon sugars were thought to be processed by RpiA, while the primary role of RpiB was suggested to instead be interconversion of the rare 6-carbon sugars D-allose-6-phosphate (All6P) and D-allulose-6-phosphate" ([PMID: 18640127](https://pubmed.ncbi.nlm.nih.gov/18640127/)). This positions RpiA as the housekeeping enzyme for the physiological 5-carbon substrates R5P and Ru5P.

### Finding 3 — Catalytic mechanism: acid/base ring-opening and isomerization via a cis-enediol(ate) intermediate

Mechanistic and structural studies of Rpi enzymes establish that the isomerization proceeds through a **high-energy enediolate intermediate**. As stated for both Rpi types, "the reaction catalyzed by both enzymes is thought to proceed via a high energy enediolate intermediate, by analogy to other carbohydrate isomerases" ([PMID: 15590681](https://pubmed.ncbi.nlm.nih.gov/15590681/)). The enzyme opens the furanose ring of R5P, and an acidic active-site residue functions as the catalytic base: "both enzymes also have an acidic residue that acts as a base in the isomerization step" ([PMID: 15590681](https://pubmed.ncbi.nlm.nih.gov/15590681/)). In RpiA specifically, this base is a glutamate, and a conserved lysine stabilizes the developing negative charge on the enediolate. The reaction takes place in the cytoplasm, consistent with RpiA being a soluble PPP enzyme.

### Finding 4 — Q88CN0 is a confident RpiA ortholog (63.5% identity to *E. coli* RpiA with conserved motifs)

A global pairwise alignment (Needleman–Wunsch) of *P. putida* RpiA (Q88CN0, 224 aa) against *E. coli* RpiA (P0A7Z0, 219 aa) yields **139/219 = 63.5% identity** over the aligned region. This is far above the ~30% threshold generally used for reliable transfer of orthologous function. The diagnostic RpiA sequence motifs are fully conserved, including the **GTGSTA** nucleotide/sugar-phosphate-binding motif, the invariant **KGGGAALTREK** segment, and the IPMARS(H/A)VARQLVKLGG…VVTDNGNVILDV region. The combination of high overall identity and complete motif conservation makes the RpiA functional assignment secure.

### Finding 5 — Physiological context: RpiA operates within the NADPH-generating EDEMP cycle / non-oxidative PPP

*P. putida* KT2440 lacks a functional Embden–Meyerhof–Parnas (EMP) glycolysis and catabolizes glucose primarily through the **Entner–Doudoroff (ED)** route. A fraction (~10%) of triose phosphates is recycled to hexose phosphates through a hybrid metabolic architecture that "merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). The PPP branch — including RpiA — participates in this carbon recycling. Importantly, "the default metabolic state of *P. putida* KT2440 is characterized by a slight catabolic overproduction of reducing power" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)), placing RpiA within the NADPH/redox physiology that supports biosynthesis and stress resistance in this strain.

### Finding 6 — Every catalytic and substrate-binding residue maps one-to-one onto *E. coli* RpiA; catalytic base is Glu107

UniProt/HAMAP (rule MF_00170) feature annotation assigns Q88CN0 an active site at **Glu107** (proton acceptor / catalytic base) and substrate-binding residues at **32-TGST-35**, **85-DGAD-88**, **98-KGGG-101**, and **Lys125**. These align exactly to *E. coli* RpiA (P0A7Z0) active-site Glu103 and binding residues 28-TGST-31, 81-DGAD-84, 94-KGGG-97 and Lys121. The catalytic proton acceptor is therefore a conserved glutamate, and a conserved lysine (K125 in *P. putida* / K121 in *E. coli*) stabilizes the enediolate intermediate. UniProt lists the FUNCTION as the "reversible conversion of ribose-5-phosphate to ribulose 5-phosphate," the PATHWAY as "pentose phosphate pathway; non-oxidative stage, step 1/1," and the SUBUNIT as a **homodimer**.

| Feature | *P. putida* RpiA (Q88CN0) | *E. coli* RpiA (P0A7Z0) | Role |
|---|---|---|---|
| Catalytic base | **Glu107** | Glu103 | Proton acceptor (C2 abstraction) |
| Binding motif 1 | 32-**TGST**-35 | 28-TGST-31 | Substrate/phosphate binding |
| Binding motif 2 | 85-**DGAD**-88 | 81-DGAD-84 | Substrate binding |
| Binding motif 3 | 98-**KGGG**-101 | 94-KGGG-97 | Substrate/phosphate binding |
| Intermediate stabilization | **Lys125** | Lys121 | Enediolate stabilization |

### Finding 7 — RpiA is the sole (non-redundant) ribose-5-phosphate isomerase in *P. putida* KT2440

A proteome-wide search of *P. putida* KT2440 (taxid 160488) returns **only Q88CN0** (*rpiA*/PP_5150) for "ribose-5-phosphate isomerase," and **zero** proteins of the analogous RpiB/LacAB family (Pfam PF02502). That is, no *rpiB* paralog exists in this genome — a sharp contrast with *E. coli*, which encodes both *rpiA* and *rpiB*. Because there is no analogous enzyme to provide backup, RpiA carries the entire cellular flux of ribose-5-phosphate isomerization, which strongly implies that *rpiA* is **essential** in KT2440. The gene neighborhood reinforces its housekeeping character: PP_5150 is flanked by PP_5149 (*ilvA-II*, threonine dehydratase) and PP_5151 (an SdiA-regulated domain protein), functionally unrelated genes — indicating *rpiA* is a standalone housekeeping gene rather than part of a PPP operon.

### Finding 8 — AlphaFold model confirms the RpiA fold and a well-ordered active site

The AlphaFold DB model AF-Q88CN0-F1 (224 residues) has a **mean per-residue pLDDT of 97.7**, with 97.8% of residues at pLDDT ≥90 ("very high") and 100% ≥70 ("confident"). All functional residues fall in very-high-confidence regions: Glu107 (98.7), Asp85/Asp88 of the DGAD motif (98.8/98.5), Lys98 of the KGGG motif (98.8), Thr32–Thr35 of TGST (98.2/97.5), and Lys125 (97.6). The high-confidence prediction of a canonical RpiA fold with a well-ordered active site corroborates the sequence-based functional assignment and indicates a catalytically competent enzyme.

### Finding 9 — The catalytic glutamate (Glu107) is evolutionarily invariant from bacteria to human

Pairwise alignment of *P. putida* RpiA (Q88CN0) against diverse RpiA-family orthologs shows the residue aligned to catalytic Glu107 is a **glutamate** in *E. coli* (P0A7Z0, 63% identity), **human RPIA** (P49247, 46% identity), and **spinach** (P48490, 30% identity). In the two confidently alignable orthologs (*E. coli* and human), the DGAD aspartates (Asp85/Asp88) and the intermediate-stabilizing Lys125 are also strictly conserved. Very low-identity sequences (yeast Rki1, 22% identity; a short 163-aa Vibrio entry, 31% identity) could not be reliably registered by naive pairwise alignment and were not used as evidence. The strict conservation of the catalytic apparatus across a billion-plus years of divergence is powerful support for a shared, conserved catalytic mechanism.

---

## Mechanistic Model and Interpretation

### The reaction

RpiA catalyzes a single, reversible aldose–ketose isomerization at the interface between the oxidative and non-oxidative pentose phosphate pathway:

```
        RpiA (EC 5.3.1.6)
  D-ribose-5-phosphate  ⇌  D-ribulose-5-phosphate
      (aldose, R5P)          (ketose, Ru5P)
```

The catalytic cycle, inferred from mechanistic studies of RpiA/RpiB orthologs and mapped onto the conserved residues of Q88CN0, proceeds as:

```
 1. Substrate binding      R5P (furanose) docks; TGST(32-35),
                           DGAD(85-88), KGGG(98-101) & Lys125
                           anchor the 5-phosphate and sugar ring.

 2. Ring opening           Furanose ring of R5P is opened to the
                           linear aldehyde form.

 3. Proton abstraction     Glu107 (catalytic base) removes the C2
                           proton, generating a high-energy
                           cis-enediol(ate) intermediate.

 4. Intermediate           Lys125 (+ backbone/dipoles) stabilizes
    stabilization          the negatively charged enediolate.

 5. Reprotonation          Proton returns to C1, producing the
                           ketose D-ribulose-5-phosphate.

 6. Product release        Ru5P dissociates; reaction is fully
                           reversible.
```

This mechanism is shared, in broad strokes, across carbohydrate isomerases and is directly supported by studies documenting the enediolate intermediate and the acidic catalytic base ([PMID: 15590681](https://pubmed.ncbi.nlm.nih.gov/15590681/)). What makes the assignment specific and confident for Q88CN0 is the one-to-one residue mapping onto the biochemically characterized *E. coli* enzyme (Finding 6) and the evolutionary invariance of Glu107 (Finding 9).

### Where the enzyme acts

RpiA is a **soluble, cytoplasmic homodimer**. It has no signal peptide, transmembrane segment, or targeting sequence; it carries out its reaction in the cytosol as an integral component of the PPP enzyme set. This localization is consistent across the RpiA family and with the freely diffusible sugar-phosphate substrates it operates on.

### Physiological role in *P. putida* KT2440

RpiA sits at a metabolic hub that couples central carbon catabolism to biosynthesis:

```
   Glucose ──(ED pathway, primary route in KT2440)──► pyruvate/triose-P
                          │
                          │  EDEMP recycling (~10% of triose-P
                          │  back to hexose-P; NADPH overproduction)
                          ▼
        ┌─────────── Pentose Phosphate Pathway ───────────┐
        │  oxidative branch → Ru5P                          │
        │                     │                             │
        │             RpiA ⇅  │  (Ru5P ⇌ R5P)               │
        │                     ▼                             │
        │                    R5P ──► nucleotides, histidine,│
        │                            aromatic amino acids,  │
        │                            NAD(P)/cofactors        │
        └───────────────────────────────────────────────────┘
```

In KT2440, glucose is catabolized mainly via the Entner–Doudoroff route embedded in a hybrid **EDEMP cycle** ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). RpiA's isomerization allows Ru5P (produced by the oxidative PPP) to be converted to R5P for nucleotide and cofactor biosynthesis, and — running in reverse — allows R5P (e.g., from nucleotide salvage) to enter the non-oxidative pentose interconversion network that feeds back into hexose/triose phosphates. Because KT2440 metabolism is biased toward NADPH overproduction, the PPP branch that RpiA anchors is central to supplying reducing power and biosynthetic precursors that underpin this organism's notable biosynthetic capacity and stress tolerance.

### Essentiality

Because *P. putida* KT2440 has **no RpiB paralog** (Finding 7), RpiA is the only enzyme able to interconvert R5P and Ru5P. The *E. coli* genetic precedent — where *rpiA* deletion produces ribose auxotrophy even in the presence of *rpiB* ([PMID: 8576032](https://pubmed.ncbi.nlm.nih.gov/8576032/)) — implies that in an organism lacking any *rpiB* backup, *rpiA* loss would be still more deleterious. RpiA is therefore predicted to be an **essential, non-redundant housekeeping gene** in KT2440.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [32533303](https://pubmed.ncbi.nlm.nih.gov/32533303/) | *Ribose-5-phosphate isomerases: characteristics, structural features, and applications* | Authoritative review; establishes RpiA's pivotal PPP role and the EC 5.3.1.6 R5P⇌Ru5P reaction (Finding 1). |
| [8576032](https://pubmed.ncbi.nlm.nih.gov/8576032/) | *Ribose catabolism of E. coli: rpiB and rpiR* | Genetic proof that *rpiA*-null strains are ribose auxotrophs despite intact *rpiB* — RpiA carries the essential flux (Findings 2, 7). |
| [18640127](https://pubmed.ncbi.nlm.nih.gov/18640127/) | *RpiB from E. coli is also a D-allose-6-P isomerase; M. tuberculosis is not* | Defines division of labor: RpiA processes essential 5-carbon sugars, RpiB the rare 6-carbon sugars (Finding 2). |
| [15590681](https://pubmed.ncbi.nlm.nih.gov/15590681/) | *Competitive inhibitors of M. tuberculosis RpiB reveal reaction mechanism* | Establishes the enediolate-intermediate mechanism and the acidic catalytic base common to Rpi enzymes (Finding 3). |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through the EDEMP cycle* | Defines the KT2440 EDEMP cycle incorporating PPP (RpiA) reactions and its NADPH-overproducing default state (Finding 5). |
| [14687575](https://pubmed.ncbi.nlm.nih.gov/14687575/) | *M. tuberculosis Rpi has a known fold but novel active site* | Confirms RpiA and RpiB are two unrelated enzyme types catalyzing the same reaction; RpiA is the near-universal form. |
| [14499611](https://pubmed.ncbi.nlm.nih.gov/14499611/) | *Structure of RpiB/AlsB from E. coli* | Documents the completely distinct fold/active site of RpiB, underscoring that RpiA (Q88CN0's family) is structurally separate. |
| [8572885](https://pubmed.ncbi.nlm.nih.gov/8572885/) | *Genetics of PPP enzymes of E. coli K-12* | Confirms isoenzymes rpiA/rpiB exist in E. coli — context for KT2440 having only rpiA. |

**Supporting bioinformatic/structural evidence (this investigation):**
- 63.5% identity and complete motif conservation between Q88CN0 and *E. coli* RpiA (Finding 4).
- One-to-one active-site residue mapping via HAMAP MF_00170 annotation (Finding 6).
- AlphaFold model AF-Q88CN0-F1 at mean pLDDT 97.7 with a well-ordered active site (Finding 8).
- Strict evolutionary conservation of Glu107 from bacteria to human (Finding 9).

**Papers that contextualize but do not directly bear on the KT2440 enzyme:** The RpiA cancer/moonlighting literature ([PMID: 30418535](https://pubmed.ncbi.nlm.nih.gov/30418535/), [PMID: 29337987](https://pubmed.ncbi.nlm.nih.gov/29337987/)) describes a noncanonical nuclear, β-catenin-stabilizing role of *human* RPIA that depends on a C-terminal domain absent from the bacterial enzyme; these are not applicable to the *P. putida* protein and are noted only to avoid mis-transfer of function. Rare-sugar engineering studies of RpiA from *Ochrobactrum* sp. CSL1 ([PMID: 34116752](https://pubmed.ncbi.nlm.nih.gov/34116752/), [PMID: 32912675](https://pubmed.ncbi.nlm.nih.gov/32912675/)) illustrate that RpiA can act on additional aldose substrates and are relevant to substrate-specificity discussions but are not direct evidence for the KT2440 enzyme.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 enzyme.** The functional assignment for Q88CN0 rests on high-confidence homology transfer (63.5% identity to *E. coli* RpiA, invariant catalytic residues, HAMAP MF_00170, AlphaFold) rather than on purified-enzyme kinetics for this specific protein. There is no measured *k*cat, *K*m, pH optimum, or crystal structure for the KT2440 RpiA.

2. **Essentiality is predicted, not experimentally demonstrated in KT2440.** The essentiality inference is drawn from (i) the absence of an *rpiB* paralog in the genome and (ii) the *E. coli* auxotrophy precedent. A targeted gene-knockout or transposon-essentiality study in KT2440 has not been confirmed within this investigation.

3. **Substrate specificity beyond R5P/Ru5P is unquantified for this ortholog.** RpiA enzymes from other organisms show measurable activity on rare aldose sugars (e.g., D-allose, L-rhamnose). Whether KT2440 RpiA has any physiologically relevant secondary activity is unknown.

4. **Regulation is unexplored.** How *rpiA* expression is controlled in KT2440 (constitutive housekeeping vs. growth-rate or carbon-source responsive), and whether flux through RpiA is regulated at the metabolic level within the EDEMP cycle, was not investigated.

5. **Oligomeric state assumed from family annotation.** The homodimer assignment comes from UniProt/family annotation and the AlphaFold monomer model; it has not been verified experimentally for the KT2440 protein.

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant expression and enzyme kinetics.** Clone PP_5150, express and purify the His-tagged protein, and measure steady-state kinetics (R5P → Ru5P and reverse) using a coupled spectrophotometric assay. Report *k*cat, *K*m, and catalytic efficiency; compare to *E. coli* RpiA.

2. **Site-directed mutagenesis of Glu107.** Generate E107A/E107Q variants and confirm loss of catalytic activity, providing direct experimental validation that Glu107 is the catalytic base predicted by homology and conservation analysis.

3. **Essentiality test in KT2440.** Attempt a clean *rpiA* deletion; if non-viable on standard media, test rescue by ribose/nucleoside supplementation or by heterologous *rpiB* complementation, mirroring the classic *E. coli* auxotrophy experiment.

4. **Structure determination.** Solve the crystal structure (or cryo-EM) of KT2440 RpiA, ideally with substrate/inhibitor bound, to validate the AlphaFold model, confirm the homodimer, and define active-site geometry.

5. **Substrate-scope screen.** Test activity on rare aldose phosphates/sugars (e.g., D-allose, L-rhamnose) to determine whether the KT2440 enzyme has secondary specificities relevant to metabolic engineering.

6. **Metabolic-flux integration.** Use ¹³C metabolic flux analysis in KT2440 to quantify flux through RpiA within the EDEMP cycle under different carbon sources, clarifying its quantitative role in NADPH provisioning and pentose supply.

---

## Conclusion

rpiA (PP_5150, UniProt Q88CN0) in *Pseudomonas putida* KT2440 encodes **ribose-5-phosphate isomerase A**, a soluble cytoplasmic homodimeric enzyme (EC 5.3.1.6) that catalyzes the reversible isomerization of D-ribose-5-phosphate to D-ribulose-5-phosphate — the single non-oxidative pentose-phosphate-pathway isomerization step — using **Glu107** as the catalytic base and a conserved TGST/DGAD/KGGG/Lys125 constellation for substrate binding and enediolate stabilization. Functionally, it supplies R5P for nucleotide, histidine, aromatic amino acid and cofactor biosynthesis and interconverts pentose phosphates within the strain's NADPH-generating EDEMP cycle. Identity and function are assigned with high confidence from 63.5% identity and one-to-one active-site conservation with the biochemically characterized *E. coli* RpiA, supported by a very-high-confidence AlphaFold model and strict evolutionary conservation of the catalytic glutamate. Because KT2440 encodes no RpiB paralog, RpiA is the **sole, non-redundant, and predicted-essential** ribose-5-phosphate isomerase in this organism.


## Artifacts

- [OpenScientist final report](rpiA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rpiA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32533303
2. PMID:8576032
3. PMID:18640127
4. PMID:15590681
5. PMID:26350459
6. PMID:30418535
7. PMID:29337987
8. PMID:34116752
9. PMID:32912675