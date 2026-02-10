# Transcription Factor Annotation Guidelines (Synthesized)

Operational guidelines for GO annotation of transcription regulators, synthesized from:
- GO Consortium guidelines PDF (Gaudet, Logie, Lovering, 2023)
- BBA Gene Regulatory Mechanisms paper (PMID:34461313, 2021)

---

## Three Classes of Transcription Regulators

| Class | Definition | Key MF Term | DNA Binding |
|-------|------------|-------------|-------------|
| **GTF** | Assembles with RNA polymerase at promoter → pre-initiation complex | GO:0140223 | No sequence-specific binding |
| **dbTF** | Binds specific DNA sequences (TFBS) to control where/when genes are expressed | GO:0003700 | Yes, sequence-specific |
| **coTF** | Bridges GTF↔dbTF, modifies chromatin, or modulates dbTF activity | GO:0003712 | Usually none (or non-specific) |

**Critical distinction:** coTFs act on dbTFs as input; dbTFs act on target genes as input.

---

## GO Terms Quick Reference

### GTF
```
MF: GO:0140223 general transcription initiation factor activity
BP: GO:0006351 transcription, DNA-templated
CC: GO:0097550 transcriptional preinitiation complex
```

### dbTF
```
MF: GO:0003700 DNA-binding transcription factor activity
    ├─ GO:0001228 activator activity, RNA pol II-specific
    └─ GO:0001227 repressor activity, RNA pol II-specific
MF: GO:0000987 cis-regulatory region sequence-specific DNA binding
BP: GO:0006355 regulation of transcription, DNA-templated
    ├─ GO:0045893 positive regulation
    └─ GO:0045892 negative regulation
CC: GO:0005667 transcription factor complex
```

### coTF
```
MF: GO:0003712 transcription coregulator activity
    ├─ GO:0003713 transcription coactivator activity
    └─ GO:0003714 transcription corepressor activity
MF: GO:0140097 catalytic activity, acting on DNA (e.g., methyltransferase)
MF: GO:0140096 catalytic activity, acting on protein (e.g., histone deacetylase)
BP: GO:0006355 regulation of transcription, DNA-templated
```

### dbTF Inhibitors
```
MF: GO:0140416 DNA-binding transcription factor inhibitor activity
```
Use when protein sequesters dbTF away from chromatin (does NOT act at target gene locus).

---

## 4-Question Checklist

Before annotating a transcription regulator:

### 1. What is the hypothesis?
Is the paper actually characterizing a transcription regulator? Check the introduction for the authors' intent.

### 2. Do domains/orthologs support it?

| Evidence | Implication |
|----------|-------------|
| Known DBD (homeobox, GATA, bHLH, bZIP) | Strong support for dbTF |
| Zinc finger domain | **Caution**: many ZnF proteins are NOT dbTFs |
| Enzymatic domain (HAT, HDAC, HMT) | Points to coTF |
| No recognizable domain | Requires strong experimental evidence |

### 3. Are existing annotations consistent?
Check UniProt, existing GO annotations. Flag conflicts for review.

### 4. Does experimental evidence support the annotation?
See evidence requirements below.

---

## Evidence Requirements

### For dbTF (GO:0003700)

**Minimum requirements:**
1. Evidence of DNA binding
2. Evidence that binding regulates transcription of target gene(s)

| Protein Family | DNA Binding Evidence Needed |
|----------------|----------------------------|
| Well-characterized DBD (homeobox, GATA) | ChIP sufficient |
| Zinc finger or enzymatic domain | Strong direct binding evidence required |
| Novel/uncharacterized | Sequence-specific binding + regulation of target |

**DBD presence alone is NOT sufficient** — must show transcriptional regulation.

### For coTF (GO:0003712)

- Interacts with dbTF or cis-regulatory region
- Activates or represses transcription (often via chromatin modification)
- Does NOT require sequence-specific DNA binding

### For GTF (GO:0140223)

- Component of pre-initiation complex
- Well-established by orthology (TAF#, GTF2#, GTF3#)

---

## High-Throughput Data Interpretation

### HT-SELEX
- Shows: DNA sequence recognition
- Supports: GO:0000987 (cis-regulatory DNA binding)
- Does NOT support: GO:0003700 (dbTF) unless regulation of target shown
- **Example pitfall:** PRMT14 binds DNA for meiotic recombination, not transcription

### ChIP-seq
- Shows: Genomic binding location (may include crosslinked interactors)
- If protein has DBD + evidence of transcription regulation → supports dbTF
- If protein lacks DBD → may indicate coTF
- **Caution:** ChIP alone is inconclusive without functional data

### Reporter Assays
- Shows: Regulation of transcription
- Combined with ChIP → strong support for dbTF or coTF annotation

---

## Decision Tree

```
Is this protein involved in transcription regulation?
│
├─ Assembles at promoter with RNA pol?
│  └─ YES → GTF (GO:0140223)
│
├─ Binds specific DNA sequences?
│  ├─ YES + regulates target gene expression?
│  │  └─ YES → dbTF (GO:0003700)
│  │     ├─ Activates → GO:0001228
│  │     └─ Represses → GO:0001227
│  └─ NO or non-specific binding?
│     └─ See coTF below
│
└─ Modifies chromatin, bridges GTF↔dbTF, or modulates dbTF?
   └─ YES → coTF (GO:0003712)
      ├─ Activates → GO:0003713
      └─ Represses → GO:0003714
```

---

## Annotation Extensions

Use annotation extensions to capture:

| Relation | Use Case | Example |
|----------|----------|---------|
| `has_input` | Target gene of dbTF/coTF | `has_input(UniProtKB:P04637)` |
| `is_active_in` | Cellular location | `is_active_in(GO:0005634)` nucleus |
| `occurs_in` | Cell/tissue context | `occurs_in(CL:0000057)` fibroblast |

---

## Common Pitfalls

1. **"Transcription factor" used loosely** — authors may mean GTF, dbTF, or coTF
2. **DBD ≠ dbTF** — zinc fingers often have non-TF functions
3. **Cofactor terminology inconsistent** — "coactivator" sometimes means dbTF dimer partner
4. **ChIP peaks ≠ direct binding** — could be indirect via complex
5. **Many presumed dbTFs lack direct DNA binding evidence** — annotation by domain only
6. **Dual-function proteins exist** — can be dbTF in one context, coTF in another

---

## Examples

### GTF: GTF2H2 (PMID:10924514)
- Contains TFIIH subunit domain (IPR012170)
- UniProt: "Component of TFIID-containing RNA polymerase II pre-initiation complex"
- Existing IDA to GO:0016251 (RNA pol II general TF activity)
- **Annotation:** GO:0140223 general transcription initiation factor activity

### dbTF: NKX6.3 (PMID:26314965)
- Contains homeobox domain (IPR020479)
- ChIP shows binding to regulatory regions of target genes
- Reporter assay shows activation via TAAT motif
- **Annotations:**
  - GO:0003700 DNA-binding transcription factor activity
  - GO:0001228 activator activity (with `has_input` for targets)
  - GO:0001227 repressor activity (context-dependent)

### coTF: SIN3A (PMID:22783022)
- Contains SIN3A domain (IPR037969) → associated with GO:0003714
- No DBD — does NOT bind DNA directly
- ChIP shows recruitment to SOCS3 promoter (via STAT3 interaction)
- Represses STAT3's activator function
- **Annotations:**
  - GO:0003714 transcription corepressor activity
  - GO:0045892 negative regulation of transcription
- **Removed annotations:** GO:0003700 (was incorrect — SIN3A is coTF not dbTF)

---

## References

1. Gaudet P, Logie C, Lovering RC et al. (2021) Gene Ontology representation for transcription factor functions. *BBA Gene Regul Mech* 1864:194752. PMID:34461313
2. GO Consortium TF Annotation Guidelines (2023) - `TF-annotation-guidelines.pdf`
3. Tripathi S et al. (2013) Experiments for dbTF evidence. PMID:27270715
