# Human dbTF Annotation Discrepancy Analysis

Analysis comparing GO dbTF annotations (GO:0003700 descendants) with InterPro domain annotations.

## Summary

| Category | Count | Notes |
|----------|-------|-------|
| **Total dbTF annotations** | 1,448 | Swiss-Prot reviewed, human |
| With experimental evidence | 503 | IDA, IMP, IPI, IGI, IEP |
| IEA-only (computational) | 945 | Candidates for ML validation |

## Evidence Code Distribution

| ECO Code | Count | Meaning |
|----------|-------|---------|
| ECO:0000318 | 1,334 | IBA (phylogenetic annotation) |
| ECO:0000314 | 1,001 | IDA (direct assay) |
| ECO:0005556 | 709 | HDA (high-throughput direct assay) |
| ECO:0000256 | 565 | IEA (electronic annotation) |
| ECO:0000265 | 471 | ISS (sequence similarity) |
| ECO:0000304 | 223 | TAS (traceable author statement) |
| ECO:0000501 | 212 | IEA (InterPro) |
| ECO:0000250 | 200 | ISS (sequence similarity) |
| ECO:0000315 | 144 | IMP (mutant phenotype) |
| ECO:0000303 | 137 | NAS (non-traceable author) |

---

## Potential False Negatives

Proteins with DNA-binding domains NOT annotated as dbTF.

### Homeobox Domain (IPR001356)

| UniProt | Gene | Protein | Why NOT dbTF |
|---------|------|---------|--------------|
| Q96G23 | CERS2 | Ceramide synthase 2 | Enzyme, not TF |
| Q9HA82 | CERS4 | Ceramide synthase 4 | Enzyme, not TF |
| Q8N5B7 | CERS5 | Ceramide synthase 5 | Enzyme, not TF |
| Q6ZMG9 | CERS6 | Ceramide synthase 6 | Enzyme, not TF |
| Q6NT76 | HMBOX1 | Homeobox-containing protein 1 | Telomere binding, not gene regulation |

**Conclusion:** These are correctly excluded — they have homeobox-like folds but function as enzymes or telomere-binding proteins, not transcription factors. **DBD ≠ dbTF**.

### bHLH Domain (IPR011598)

8 proteins with bHLH domain NOT in dbTF list:

| UniProt | Gene | Protein | Why NOT dbTF |
|---------|------|---------|--------------|
| P41134 | ID1 | DNA-binding protein inhibitor ID-1 | Lacks basic region, CANNOT bind DNA |
| Q02363 | ID2 | DNA-binding protein inhibitor ID-2 | Lacks basic region, CANNOT bind DNA |
| Q02535 | ID3 | DNA-binding protein inhibitor ID-3 | Lacks basic region, CANNOT bind DNA |
| P47928 | ID4 | DNA-binding protein inhibitor ID-4 | Lacks basic region, CANNOT bind DNA |
| Q15788 | NCOA1 | Nuclear receptor coactivator 1 | **coTF**, not dbTF |
| Q15596 | NCOA2 | Nuclear receptor coactivator 2 | **coTF**, not dbTF |
| Q9Y6Q9 | NCOA3 | Nuclear receptor coactivator 3 | **coTF**, not dbTF |
| C9JSJ3 | MEIOSIN | Meiosis initiator protein | Meiosis-specific, needs review |

**Conclusion:**
- **ID1-4**: Correctly excluded — they are dominant-negative inhibitors that heterodimerize with bHLH TFs to PREVENT DNA binding
- **NCOA1-3**: Correctly excluded — they are transcription **coactivators** (GO:0003713), not dbTFs
- **MEIOSIN**: May warrant review

### bZIP Domain (IPR004827)

0 proteins with bZIP domain missing from dbTF list.

**Conclusion:** Complete coverage.

---

## Potential False Positives

### High-Risk Category: IEA-Only Annotations

945 proteins have dbTF annotation based only on computational evidence (no experimental support).

**Recommended action:** Run DeepTFactor on these proteins to identify:
1. Low-confidence TF predictions → candidates for annotation removal
2. Saliency maps not highlighting canonical DBDs → may be coTFs misannotated as dbTFs

### Proteins to Prioritize for Review

Query to extract IEA-only dbTF proteins:
```bash
# Get proteins with only IEA evidence
comm -23 \
  <(cut -f3 human-dbTF-annotations-quickgo.tsv | tail -n +2 | sort -u) \
  <(grep -E "ECO:0000314|ECO:0000315|ECO:0000316" human-dbTF-annotations-quickgo.tsv | cut -f3 | sort -u)
```

---

## Key Findings

1. **GO annotations are high quality** — proteins with DBDs that are NOT dbTFs (ceramide synthases, ID proteins, coactivators) are correctly excluded

2. **DBD presence ≠ dbTF function** — validates the GO guidelines warning

3. **~65% of annotations lack experimental evidence** — these are candidates for ML-based validation

4. **No obvious false negatives** — major DBD families (homeobox, bHLH, bZIP) have good coverage

5. **coTF vs dbTF distinction is maintained** — NCOA1/2/3 correctly classified as coTFs, not dbTFs

---

---

## Comparison: UniProt Keywords vs GOA

UniProt maintains keyword KW-0805 ("Transcription regulation") which is **broader** than GO:0003700.

| Dataset | Count | Scope |
|---------|-------|-------|
| UniProt KW-0805 | 2,376 | All transcription regulators |
| GOA GO:0003700 | 1,448 | Sequence-specific dbTFs only |
| **Overlap** | 1,323 | Agreement |
| UniProt only | 1,053 | coTFs/GTFs (correctly NOT dbTFs) |
| GOA only | 125 | dbTFs missing UniProt keyword |

### UniProt-only proteins (1,053) — NOT false negatives

These are **correctly excluded** from dbTF — they are coTFs or GTFs:

| UniProt | Gene | Type |
|---------|------|------|
| A0JLT2 | MED19 | Mediator subunit (GTF) |
| A5YKK6 | CNOT1 | CCR4-NOT complex (coTF) |
| Q92831 | KAT2B | Histone acetyltransferase (coTF) |
| Q9UBK2 | PPARGC1A | PGC-1α coactivator (coTF) |
| A6H8Y1 | BDP1 | RNA pol III TF (GTF) |

### GOA-only proteins (125) — potential UniProt keyword gaps

These are valid dbTFs that lack the UniProt "Transcription regulation" keyword:

| UniProt | Gene | Notes |
|---------|------|-------|
| A0A087WUV0 | ZNF892 | Zinc finger TF |
| A0A0U1RQI7 | KLF18 | Krüppel-like factor |
| A0A1W2PRP0 | FOXL3 | Forkhead box TF |
| A1YPR0 | ZBTB7C | BTB/POZ zinc finger |

**Action:** These 125 could be flagged for UniProt keyword update.

---

## Files

- `human-dbTF-list.tsv` — 1,448 dbTF UniProt IDs + gene symbols
- `human-dbTF-annotations-quickgo.tsv` — Full annotation data with evidence codes
- `human-TF-uniprot-kw0805.tsv` — 2,376 UniProt "Transcription regulation" proteins
- `diff-both.txt` — 1,323 proteins in both datasets
- `diff-uniprot-only.txt` — 1,053 UniProt-only (coTFs/GTFs)
- `diff-goa-only.txt` — 125 GOA-only (potential UniProt gaps)

---

## Comparison: GREEKC Curated Target Set vs GOA

The GREEKC consortium maintains a curated dbTF target set. See [`greekc-goa-comparison.md`](./greekc-goa-comparison.md) for full analysis.

| Dataset | Count | Scope |
|---------|-------|-------|
| GREEKC dbTF target set | 1,449 | Curated by GREEKC consortium |
| GOA GO:0003700 | 1,447 | Swiss-Prot human proteins |
| **Agreement** | 1,385 | 95.6% overlap |
| GOA-only | 62 | Potential over-annotations |
| GREEKC-only | 50 | Potential false negatives (14 isoforms excluded) |

### GOA-only: Potential Over-annotations

62 proteins with GOA dbTF annotation but NOT in GREEKC curated set. Many are concerning:

| UniProt | Gene | Concern |
|---------|------|---------|
| O00287 | RFXAP | coTF, not dbTF |
| O14593 | RFXANK | coTF, not dbTF |
| O00634, O95631 | NTN3, NTN1 | Netrins (guidance molecules) |
| P08910 | ABHD2 | Enzyme |
| P22392 | NME2 | Enzyme |
| P23396 | RPS3 | Ribosomal protein |
| P56524 | HDAC4 | Enzyme |

**Key insight**: The GREEKC curated set correctly excludes many proteins that GOA includes.

### GREEKC-only: Potential False Negatives

50 proteins in GREEKC but lacking GOA dbTF annotation (mostly ZNF proteins).

---

## Next Steps

1. [ ] Extract 945 IEA-only proteins for DeepTFactor validation
2. [ ] Review MEIOSIN annotation status
3. [ ] Compare with TFCheckpoint 2.0 for additional cross-validation
4. [x] Compare with GREEKC curated target set
5. [ ] Review 62 GOA-only proteins for potential removal
6. [ ] Review 50 GREEKC-only proteins for potential annotation
