# ARATH: reports for upstream curators

Back to [ARATH](../ARATH.md).

These are draft reports for upstream curators, collected from the ARATH gene and GO-CAM
reviews. **None has been filed yet.** Each report is written to stand alone so it
can be pasted into the curators' channel (GO helpdesk or the `geneontology/go-annotation`
tracker for GO-CAMs, TAIR curator contact for TAIR annotations). After filing one,
record the ticket link and date in its Status line.

| # | Target | Recipient | Kind | Status |
|---|--------|-----------|------|--------|
| 1 | GO-CAM `67e5e74400000148` (HAM1 activity on SCL27) | GO (model author) | wrong gene product | not filed |
| 2 | SUR1 (Q9SIV0) GO:0050832 IDA | TAIR | reference does not support annotation | not filed |
| 3 | RIC7 / F4JLB7 (AT4G28560) rows from PMID:11752391 | TAIR | wrong locus | not filed |
| 4 | GSTF6 (P42760) GO:2001147 and GO:2001227 IDA | TAIR | possible legacy-alias mapping | not filed |

## 1. GO-CAM 67e5e74400000148: histone acetyltransferase activity enabled by the wrong locus

**Model:** [gomodel:67e5e74400000148](http://model.geneontology.org/67e5e74400000148)
"Arabidopsis MRG domain proteins bridge two histone modifications" (provided by
geneontology.org, 2025-03-28). Our review:
[`gocams/67e5e74400000148/67e5e74400000148-review.yaml`](../../gocams/67e5e74400000148/67e5e74400000148-review.yaml).

**Problem.** Activity `67e5e74400000172`, histone H4K5 acetyltransferase activity
(GO:0043995), is enabled by **AT2G45160**. That locus is SCARECROW-LIKE 27
(UniProtKB:Q7XJM8), a GRAS-family transcription regulator that also has the alias
HAM1 (HAIRY MERISTEM 1). It has no acetyltransferase domain. The HAM1 that
acetylates H4K5 in the three cited papers (PMID:17877703, PMID:23273925,
PMID:25183522) is the MYST acetyltransferase **AT5G64610** (UniProtKB:Q9FLF7);
HAM2 (AT5G09740) acts redundantly with it. This looks like a symbol collision on
"HAM1" when the gene product was chosen.

The same wrong locus is also the second `has input` of the MRG2 (AT1G02740)
H3K36me3 reader activity `67e5e74400000149`.

**Requested changes.**
1. Change `enabled_by` on activity `67e5e74400000172` from AT2G45160 to AT5G64610
   (and optionally add HAM2, AT5G09740).
2. Remove AT2G45160 as a `has input` of the MRG2 reader activity. The recruitment of
   the acetyltransferase is already captured by the "directly positively regulates"
   edge.

**Why it matters.** As it stands, the model asserts histone acetyltransferase
activity for a GRAS protein, and this will propagate to annotation of SCL27.

**Also worth raising (lower priority).** Every activity is `part_of` GO:0140673
(transcription elongation-coupled chromatin remodeling). PMID:25183522 argues that
plant MRG proteins diverged from the yeast/animal Eaf3/MRG15 role. They raise
acetylation at the promoter and 5' region to increase FT and FLC transcription, so a
positive regulation of transcription process fits the paper better.

## 2. SUR1 (Q9SIV0, At2g20610): GO:0050832 defense response to fungus, IDA, PMID:32213638

**Annotation:** SUR1 `acts_upstream_of_or_within` GO:0050832 defense response to
fungus, IDA, PMID:32213638, assigned by TAIR.

**Problem.** PMID:32213638 (Liu et al. 2020) is a study of ODR1/bHLH57 control of ABA
biosynthesis and seed dormancy. We read the full text (PMC7268807). It does not
mention SUR1, SUPERROOT1, At2g20610, glucosinolates, fungi or any pathogen assay.
At2g20610 is also missing from its accession-number list, which names every gene
studied. QuickGO returns this SUR1 row as the only annotation on that reference.
The paper's own genes (ODR1, bHLH57) have no annotations from it. The reference
therefore looks mis-keyed in the TAIR record.

**Question for TAIR.** Which paper was intended for this annotation? If it was a
different SUR1 study, please correct the reference. If no supporting paper exists,
please withdraw the row. An indirect role of SUR1-derived indole glucosinolates in
antifungal defense is plausible, so this report is about the citation, not the
biology.

Review: [`genes/ARATH/SUR1/SUR1-ai-review.yaml`](../../genes/ARATH/SUR1/SUR1-ai-review.yaml)
(action REMOVE); notes in `SUR1-notes.md`, 2026-10-15 entry.

## 3. RIC7: PMID:11752391 annotations attached to AT4G28560 (F4JLB7) instead of AT4G28556 (Q1G3K8)

**Annotations (all assigned by TAIR, on UniProtKB:F4JLB7 / AT4G28560, symbol RIC7):**
- GO:0005515 protein binding, IPI, PMID:11752391
- GO:0009860 pollen tube growth, IMP, PMID:11752391
- GO:0016324 apical plasma membrane, IDA, PMID:11752391

**Problem.** Wu et al. 2001 (PMID:11752391) characterise RIC7 as a CRIB-motif
ROP-interactive protein, and they report that the CRIB motif is required for Rop1
binding. F4JLB7 has no CRIB motif; it is an LRR receptor-like protein with a signal
peptide. The published RIC7 cloning and RT-PCR primers, from Wu et al. 2001 and two
later papers, all map to the adjacent, oppositely oriented locus **AT4G28556**
(transcript NM_001036663.2, encoding the CRIB protein UniProtKB:Q1G3K8). None of the
six primers has an exact 3' match of 14 or more bases in the AT4G28560 transcript.
See the analysis in
[`genes/ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md`](../../genes/ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md).

**Requested change.** Move the three PMID:11752391 annotations, and the RIC7 symbol
if TAIR agrees, from AT4G28560 to AT4G28556. The function is not in doubt, only the
locus.

Reviews: [`genes/ARATH/F4JLB7/F4JLB7-ai-review.yaml`](../../genes/ARATH/F4JLB7/F4JLB7-ai-review.yaml)
(the three rows REMOVEd as wrong locus) and
[`genes/ARATH/Q1G3K8/Q1G3K8-ai-review.yaml`](../../genes/ARATH/Q1G3K8/Q1G3K8-ai-review.yaml).

## 4. GSTF6 (P42760, At1g02930): camalexin and quercitrin binding from PMID:21631432

**Annotations (IDA, assigned by TAIR):**
- GO:2001147 camalexin binding, PMID:21631432
- GO:2001227 quercitrin binding, PMID:21631432

**Problem (to verify, not asserted).** Dixon et al. 2011 (PMID:21631432) report
camalexin and quercetin-3-O-rhamnoside binding by GSTF2, and heterocycle binding by
"GSTF2 and GSTF3". QuickGO has this reference annotated only to GSTF2 (P46422) and
GSTF6 (P42760), with identical terms. Nothing is annotated to GSTF3 under current
nomenclature (Q9SLM6, At2g02930). At1g02930, now GSTF6, carried the legacy name
AtGSTF3. The paper's "GSTF3" may therefore have been mapped to the legacy alias
rather than to At2g02930. We could not read the full text (publisher 403), so we
cannot tell which protein was assayed.

**Question for TAIR.** In PMID:21631432, is "GSTF3" At2g02930 (current GSTF3) or
At1g02930 (current GSTF6)? If it is At2g02930, the two rows belong on Q9SLM6. GSTF6
acts in camalexin biosynthesis, so camalexin binding by GSTF6 is not implausible;
the question is about the name mapping.

Review: [`genes/ARATH/GSTF6/GSTF6-ai-review.yaml`](../../genes/ARATH/GSTF6/GSTF6-ai-review.yaml)
(both rows UNDECIDED pending this answer).

## Candidates from the 2026-10-19 reviews (not yet written up)

These rows came out of the new reviews. Each needs a write-up like those above
before it can be filed. The reasoning is in each review's `reason` field.

| Gene | Annotation | Suggested change |
|------|------------|------------------|
| CBL4 (O81223) | GO:0004723 calcium-dependent protein serine/threonine phosphatase activity, ISS, PMID:9632394 | withdraw; SOS3 is a calcineurin-B-like regulatory subunit, and its effector is the kinase SOS2 |
| CBL4 (O81223) | GO:0005955 calcineurin complex, ISS, PMID:9632394 | withdraw, for the same reason |
| CBL4 (O81223) | GO:0042539 hypotonic salinity response, IMP, PMID:9405721 | sos3 is hypersensitive to high NaCl, so GO:0042538 hyperosmotic salinity response |
| SnRK2.3 (Q39193) | NOT located_in GO:0005829 cytosol, RCA, PMID:21166475 | withdraw; contradicted by BiFC and IDA cytoplasm evidence |
| SnRK2.2 (Q39192) | GO:0009738 abscisic acid-activated signaling pathway is missing | add; OST1 and SnRK2.3 carry it, and the evidence is shared (PMID:19420218) |
| SLAC1 (Q9LD83) | GO:0090333 regulation of stomatal closure, IMP, PMID:29463779 | GO:0090332 stomatal closure; SLAC1 carries out the anion efflux that closes the pore |
| SLAC1 (Q9LD83) | GO:0005634 nucleus, ISM (AtSubP) | withdraw; SLAC1 is a plasma-membrane channel |
| SERRATE (Q9ZVD0) | GO:0003677 DNA binding and GO:0003700 DNA-binding transcription factor activity, ISS | withdraw; the zinc finger binds RNA and DCL1 |
| SERRATE (Q9ZVD0) | part_of GO:0005846 nuclear cap binding complex, PMID:24137006 | SE binds CBP20/CBP80 but is not a subunit; GO:0140262 mRNA cap binding complex binding |

The others are now recorded as structured `source_defects` on the gene reviews,
except for four rows. The SnRK2.2 GO:0009738 gap is a missing annotation, not a defective
record. The SnRK2.3 RCA NOT-cytosol row and the SLAC1 AtSubP nucleus row are computational
predictions that the reviews REMOVE, not curation errors to report. The SLAC1 GO:0090333
→ GO:0090332 change is a term-choice judgement, which the review records as a MODIFY. The
recorded set also includes the CBL4, SnRK2.2 and SERRATE defects found later. To get the
per-resource reports, run `just export-source-defects`. It writes `reports/source-defects.tsv`
and one Markdown report per resource into `reports/source-defects/`. These are generated and
not committed; see [Source defects](../../docs/source_defects.md).
