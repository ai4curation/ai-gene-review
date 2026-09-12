# P3R3URF microprotein: evidence for stable, independently functional expression

**Iteration 1 — autonomous discovery report**
Date: 2026-07-06

---

## 1. Summary (answer to the research question)

Human **P3R3URF** is a genuinely *annotated and detectable* upstream-ORF (uORF) microprotein:
UniProt **A0A087WWA1** (P3R3URF_HUMAN), a **reviewed (Swiss‑Prot), 95‑amino‑acid** protein with
protein‑existence level **PE1 ("Evidence at protein level")**, a **MANE‑Select** transcript
(ENST00000506599.2) and a **CCDS** entry, plus cross‑references in mass‑spectrometry repositories
(PeptideAtlas, MassIVE, jPOST, PaxDb). So it passes the "translated + molecularly detected" bar.

**However, there is essentially no direct evidence that it is an *independently functional* microprotein.**
There is **no dedicated primary‑literature characterization** of P3R3URF (no PubMed paper reports its
Ribo‑seq initiation, ORF‑specific perturbation, endogenous tagging, localization, or interactors). Its
**only functional annotation — "cytokine‑mediated signaling pathway" (GO:0019221) — is IBA (phylogenetic)
only**, with zero P3R3URF‑specific experimental support, and is best explained as over‑transfer from the
adjacent/canonical **PIK3R3 (p55‑gamma)** family. Its expression is **testis‑exclusive** (Human Protein
Atlas: "tissue enriched", "detected in single", testis nTPM 133.6), the classic signature of
spermatogenesis transcriptional permissiveness, which lowers the prior for a conserved somatic function.
Net assessment: **P3R3URF is a bona‑fide "peptidein" — evidence of synthesis but unresolved biological
status — and no molecular function or pathway role is currently supported by direct evidence.**

---

## 2. Key findings (with evidence)

### Finding 1 — Direct protein-level evidence: real, but only "detection", not function
- UniProt **A0A087WWA1**, reviewed/Swiss‑Prot, **PE1 = evidence at protein level**, 95 aa,
  "PIK3R3 upstream open reading frame protein". **HGNC:53451**, **NCBI GeneID 110117498**, chr **1p34.1**.
- Tracked as a real coding transcript: **MANE‑Select ENST00000506599.2** + **CCDS**.
- MS support underpinning PE1: **PeptideAtlas, MassIVE, jPOST, PaxDb** cross‑references.
- ⚠️ Caveat: the two literature references on the entry are **nucleotide‑level only** —
  **PMID 16710414** (chr1 genomic sequence) and **PMID 15489334** (MGC full‑length cDNA). The protein‑level
  claim rests on high‑throughput MS repositories, **not** a targeted P3R3URF study. This is exactly the
  regime the TransCODE consortium calls a **"peptidein": evidence of synthesis but unresolved biological
  status** (review PMID **42392898**; primary Deutsch et al. TransCODE study *[uncached — not retrieved
  here; verify PMID/DOI]*). Community MS benchmarking cautions that unannotated‑microprotein MS calls need
  careful validation (PMID **42230598**).

### Finding 2 — The cytokine-signaling annotation is phylogenetic over-transfer
- The **sole** GO term on P3R3URF is **GO:0019221 "cytokine‑mediated signaling pathway"**, evidence
  **IBA (ECO:0000318)**, reference **GO_REF:0000033**, propagated from **PANTHER ancestral node
  PTN008494619** (with/from **MGI:2385459**). No EXP/IDA/IMP/IPI/IGI annotation exists.
- NCBI independently records it as **"Predicted to be involved in cytokine‑mediated signaling pathway
  [Alliance of Genome Resources]"** — a prediction, not an observation.
- **Interpretation:** IBA = *Inferred from Biological aspect of Ancestor*. Because P3R3URF sits in/near the
  PIK3R3 / p55‑gamma (PI3K regulatory subunit) family and shares its genomic locus, this is
  **phylogenetic over‑transfer from canonical PI3K‑regulatory‑subunit biology**, not P3R3URF evidence.

### Finding 3 — Testis-exclusive expression + strong PIK3R3 conflation risk
- **Human Protein Atlas** (ENSG00000250719): RNA specificity **"Tissue enriched"**, distribution
  **"Detected in single"**, only tissue = **testis (nTPM 133.6)**. This single‑tissue, testis‑restricted
  pattern is the hallmark of the **permissive transcriptional/translational environment of late
  spermatogenesis**, where many ORFs are expressed without demonstrable selected function.
- **Conflation risk:** P3R3URF is the uORF immediately 5′ of **PIK3R3**, and there is an annotated
  **read‑through locus P3R3URF‑PIK3R3**. A separate TrEMBL entry **F6TDL0** (507 aa, "Inferred from
  homology") maps to the **P3R3URF** symbol but is auto‑annotated (ARBA) as **"Phosphatidylinositol
  3‑kinase regulatory subunit gamma / p55PIK"** with an SH2 domain — i.e., the read‑through / p55‑gamma
  protein mislabeled under the P3R3URF gene symbol. **Any RNA‑seq, antibody, or "P3R3URF knockdown"
  experiment therefore risks measuring canonical PIK3R3/p55‑gamma biology** (well‑documented in cancer and
  PI3K/AKT signaling: e.g., PMIDs 37212524, 35761259, 39862908) rather than the 95‑aa microprotein.

### Finding 4 — Biophysics: extreme arginine-rich, low-complexity, likely disordered
- Sequence (95 aa):
  `MGPSRLVRGPRPQGMRSPYRRPGMGWPRPRFPRMFKCSRRRYQQGLRGRTASSAAINPATRAMGINNTHTDTTIVWIFPPQVLRHLRQPGIFLIL`
- **17 Arg (18%), 1 Lys, 12 Pro (13%), 9 Gly; 18 basic vs 1 acidic → net charge ≈ +17.**
  N‑terminal ~40 aa are **50% R/K/P** (low‑complexity, arginine/proline‑rich); C‑terminal 20 aa
  (`WIFPPQVLRHLRQPGIFLIL`) are hydrophobic (mean Kyte–Doolittle +0.66). UniProt cross‑refs include
  **RNAct** and **AlphaFoldDB**.
- **Interpretation (hypothesis‑generating):** this composition is typical of intrinsically disordered
  microproteins (cf. review PMID **42247584**) and is compatible with **nucleic‑acid/RNA binding or a
  nucleolar/RNA‑granule localization**; the short C‑terminal hydrophobic patch could mediate
  membrane/hydrophobic‑partner contacts. Not established — arginine‑rich low complexity is also common in
  young/testis ORFs and is not itself evidence of function.

---

## 3. Supported vs refuted hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| P3R3URF is translated and detectable at the protein level | **Supported (direct)** | Swiss‑Prot PE1; MS repositories; MANE/CCDS |
| P3R3URF has a dedicated experimental characterization in the literature | **Refuted** | No PubMed paper reports P3R3URF‑specific function/Ribo‑seq/perturbation/tagging |
| The "cytokine‑mediated signaling" role is P3R3URF‑specific | **Refuted** | Only GO annotation is IBA phylogenetic (GO_REF:0000033, PANTHER PTN008494619); NCBI = "Predicted" |
| P3R3URF is testis‑enriched | **Supported (direct)** | HPA "tissue enriched / detected in single", testis nTPM 133.6 |
| Testis expression + locus proximity risk conflation with PIK3R3/p55‑gamma | **Supported** | Read‑through P3R3URF‑PIK3R3; TrEMBL F6TDL0 (507 aa) mislabeled as p55PIK under the P3R3URF symbol |
| P3R3URF is an established independently functional microprotein | **Not supported (no direct evidence)** | No interactors, localization, loss‑of‑function, or conservation‑of‑function data |

**Direct P3R3URF evidence** = PE1/MS detection + testis‑enriched expression + genomic uORF status.
**Field-general inference only** (NOT P3R3URF‑specific) = any claim of cytokine/PI3K signaling function,
disorder‑based RNA binding, or "microproteins are often functional regulators."

---

## 4. Experiments that would resolve whether P3R3URF is a real functional microprotein
1. **ORF‑specific Ribo‑seq / P‑site analysis** in human testis/spermatid samples to confirm bona‑fide
   initiation at the P3R3URF AUG independent of PIK3R3 CDS translation (and quantify translation
   efficiency vs read‑through).
2. **Endogenous epitope tagging** (CRISPR knock‑in of a small tag at the P3R3URF locus, respecting the
   uORF/read‑through architecture) → immunofluorescence localization (nucleolus vs cytoplasm vs membrane)
   and **AP‑MS interactomics**; test the arginine‑rich RNA/nucleic‑acid‑binding hypothesis via **CLIP/RNA
   pulldown**.
3. **ORF‑specific perturbation** that spares canonical PIK3R3: start‑codon mutation or frameshift confined
   to the uORF, or targeting the P3R3URF‑unique 3′ region, with phenotyping in spermatogenesis models —
   **critical to avoid the PIK3R3/p55‑gamma conflation** documented above.
4. **Evolutionary test of selected function**: dN/dS and ORF‑conservation across mammals/primates; a young,
   lineage‑restricted ORF under neutral evolution would argue for spermatogenesis "translational noise."
5. **Targeted MS with P3R3URF‑unique peptides** (its sequence shares no tryptic peptides with p55‑gamma) to
   independently confirm the endogenous microprotein and distinguish it from the read‑through product.

## 5. Limitations
- No wet‑lab data or omics files were provided; findings derive from curated resources
  (UniProt/Swiss‑Prot, QuickGO, NCBI Gene/Alliance of Genome Resources, Human Protein Atlas) accessed
  programmatically on 2026‑07‑06.
- PE1 status reflects MS **detection**, which does not establish function; MS calls for
  small/basic peptides warrant orthogonal validation (PMID 42230598).
- The primary TransCODE "peptideins" study (Deutsch et al.) was **not retrieved/cached** here — cited
  only via the review PMID 42392898; **verify the primary PMID/DOI before quoting**.
- HPA nTPM values summarize bulk‑testis RNA; single‑cell/spermatid‑stage resolution was not directly
  confirmed in this iteration.

---

### Key identifiers
- UniProt (microprotein): **A0A087WWA1** — reviewed, PE1, 95 aa
- UniProt (read‑through/p55γ mislabel): **F6TDL0** — TrEMBL, 507 aa, "inferred from homology"
- HGNC: **HGNC:53451** · NCBI Gene: **110117498** · Ensembl gene **ENSG00000250719** · transcript
  **ENST00000506599.2** (MANE‑Select)
- GO: **GO:0019221** cytokine‑mediated signaling — **IBA only** (GO_REF:0000033; PANTHER PTN008494619)
- Nucleotide references: PMID **16710414**, PMID **15489334**
- Field context (cited, cached): PMID **42392898** (peptideins/TransCODE review), PMID **42230598**
  (MS microprotein benchmarking), PMID **42247584** (disordered microproteins)
- PIK3R3 canonical biology (conflation context): PMID **37212524**, **35761259**, **39862908**
