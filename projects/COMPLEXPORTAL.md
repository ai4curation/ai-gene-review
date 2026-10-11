---
title: "Complex Portal Annotation Correctness"
maturity: SCOPING
tags: [PIPELINE]
species: [SCHPO, DROME, human, yeast]
genes: [gaa1]
autolink_gene_symbols: false
---

# Complex Portal Annotation Correctness

**Bottom line:** Complex Portal (CP) curates protein complexes and pushes GO annotations to every
subunit it lists, under `assigned_by: ComplexPortal`. This project checks whether those rows are
correct: whether the complex is real in that species, whether its listed members are right, whether
the cited reference supports it, and whether a complex-level GO term holds for each subunit. In the
GOA files cached in this repo there are 5,005 such rows, and 3,131 of them (63%) are NAS. The first
case, the GPI-anchor transamidase (GPI-T) subunit Gaa1 in fly and fission yeast, shows two different
problems. The fission-yeast complex cites a paper that only predicts GPI-modification sites from
sequence. Both records also carry outcome terms that belong to the GPI-anchored proteins rather
than to the enzyme.

## Scope and questions

For each CP complex, and for each GO row it generates, we ask:

1. **Existence and membership.** Is the complex shown to exist in this species, or carried over
   from an ortholog complex? Are the participant accessions the right orthologs?
2. **Reference support.** Does the cited PMID say anything about this complex in this organism?
   CP uses `ECO:0005547` ("inferred by curator") as the evidence for the complex, and the GO rows
   it pushes are NAS against the complex's reference. This is the main point to check.
3. **Term distribution.** Is every subunit annotated with every complex-level BP and CC term? This
   is the same over-propagation problem as in [PROTEIN_COMPLEX_FUNCTIONS](PROTEIN_COMPLEX_FUNCTIONS.md),
   but at the BP level.

### Two annotation layers

CP annotates in GOA at two levels (checked in QuickGO for CPX-10141 and CPX-2687):

- **The complex itself** (`ComplexPortal:CPX-*` as the gene product) carries `enables` MF,
  `involved_in` BP and `located_in` CC, all NAS against the complex's reference.
- **Every subunit** (`UniProtKB:*`) receives a derived copy: the same BP and CC terms, plus
  `part_of` the GO complex term (IPI where CP has interaction evidence, as for the fly record,
  otherwise NAS). The MF is **not** copied, so even the catalytic subunit (gpi8, PIG-K) gets no MF
  from CP. None of the 5,005 subunit rows cached here is `molecular_function`.

So the MF over-propagation issue does not arise from CP, but every BP and CC on the complex
reaches every subunit unchanged, with the complex's evidence code and reference. In this
repo's gene reviews only the subunit layer is visible, because `*-goa.tsv` is fetched per
UniProt accession.
4. **Process specificity.** Is a BP term the process the complex performs, or a downstream
   consequence (for example, cell wall organization for an anchoring enzyme)?

### Size of the problem in this repo

These counts come from the `*-goa.tsv` files under `genes/`, filtered to `ASSIGNED BY = ComplexPortal`
(snapshot of 2026-10-11):

| Evidence | Rows |
|---|---|
| NAS | 3,131 |
| IDA | 984 |
| IPI | 686 |
| IMP | 153 |
| ISS / EXP / ISO | 51 |
| **Total** | **5,005** (2,814 BP, 2,191 CC) |

By species: human 3,820; *S. cerevisiae* 382; *D. melanogaster* 228; *C. elegans* 215;
*S. pombe* 105; mouse 103; *E. coli* 100; *A. thaliana* 48.

## Case 1: Gaa1 in the GPI-anchor transamidase complex

Records were fetched from the CP web service on 2026-10-11 (`/intact/complex-ws/complex/<CPX>`).
A search for `gaa1` returns four curated GPI-T complexes (human CPX-6503, fly CPX-2687, pombe CPX-10141,
budding yeast CPX-1275) and four predicted human complexes containing GPAA1.

### SCHPO: CPX-10141 (curated by UniProt, released 2024-11-29)

- **Members:** gaa1 (Q9US48), gpi8 (Q9USP5, catalytic), gpi16 (O94380, PIG-T), gpi17 (Q10351, PIG-S)
  and gab1 (O13883, PIG-U). The gab1 participant is labelled with its UniProt entry name
  `pigu_schpo` rather than its gene name.
- **Evidence:** `ECO:0005547` inferred by curator. The single reference is PMID:15003443.
- **GO xrefs:** GO:0042765 GPI-anchor transamidase complex; GO:0003923 GPI-anchor transamidase
  activity; GO:0016255 attachment of GPI anchor to protein; GO:0005789 ER membrane; GO:0031505
  fungal-type cell wall organization.
- **Pushed to GOA for gaa1:** four NAS rows citing PMID:15003443, for GO:0042765, GO:0016255,
  GO:0005789 and GO:0031505. The same four rows are pushed for each pombe subunit.

**Assessment:**

- **The reference does not support the claim.** PMID:15003443 (Eisenhaber et al. 2004, J Mol Biol)
  is "A sensitive predictor for potential GPI lipid modification sites in fungal protein sequences…".
  It describes a sequence-based predictor of GPI-modification sites on substrate proteins. Its
  abstract refers generically to "the fungal transamidase complex" and does not characterise the
  *S. pombe* complex or its subunits. The complex itself is plausible: all five subunits are
  conserved, PAINT places gaa1 in GO:0042765 by IBA, and budding-yeast GPI-T is well characterised.
  But this inference rests on orthology, and the GO rows should say so (ISO/ISS, or IBA, which
  already exists). They should not be NAS against a predictor paper. This is the pattern to test
  first across the pombe set: PMID:15003443 is tied with PMID:12477395 as the most
  frequently cited reference on the 105 pombe CP rows, appearing on 8 of them.
- **GO:0031505 fungal-type cell wall organization is a downstream outcome.** GPI-T attaches anchors to
  cell-wall proteins, so a GPI-T defect affects the cell wall, but the enzyme does not organise the
  wall. Pushing this term to all five subunits is the substrate/consequence error described in
  CLAUDE.md under "Do not add what curators deliberately declined to add". The existing
  [gaa1 review](../genes/SCHPO/gaa1/gaa1-ai-review.yaml) already marks it `MARK_AS_OVER_ANNOTATED`.
- The other three NAS rows are correct in content but add nothing beyond the IBA rows. The
  existing review marks them `REMOVE` as duplicates. "Correct term, unsupported reference" would be
  a more precise verdict, and we should decide how this project records that.

### DROME: CPX-2687 (curated by IntAct, released 2022-07-11)

- **Members:** GAA1 (Q9W464), PIG-K (Q8T4E1, catalytic; labelled "Putative GPI-anchor
  transamidase"), PIG-S (Q9VC10), PIG-T (Q9W3G0) and PIG-U (Q9VLK0).
- **Evidence:** `ECO:0005547` inferred by curator. References: PMID:23250212 and PMID:33496978,
  both tagged "additional information".
- **GO xrefs:** GO:0042765, GO:0003923, GO:0016255 and GO:0005789. There is no cell-wall term. The
  record cross-references FlyBase gene group FBgg0000616.
- **Pushed to GOA for GAA1 (Q9W464):** `part_of` GO:0042765 IPI PMID:33496978;
  `involved_in` GO:0016255 NAS PMID:33496978; `located_in` GO:0005789 NAS PMID:33496978.

**Assessment:**

- The references are on topic. According to PubMed, Kawaguchi et al. 2021
  ([doi:10.1002/1873-3468.14048](https://doi.org/10.1002/1873-3468.14048)) is "Subunits of the GPI
  transamidase complex localize to the endoplasmic reticulum and nuclear envelope in Drosophila".
  It studies all five fly subunits and finds PIGK mainly in the ER, while "the other four subunits
  localize to the nuclear envelope (NE) and ER". Satoh et al. 2013
  ([doi:10.1242/dev.083683](https://doi.org/10.1242/dev.083683)) is a genetic screen showing that
  GPI synthesis and attachment are needed for rhodopsin sorting. This record is much better
  supported than the pombe one.
- **The IPI row needs checking.** The abstract describes localisation and keywords "protein
  stability", but it does not mention a co-IP or other physical-interaction assay for Gaa1. Before
  accepting the IPI we need the full text to confirm the interaction experiment and its partner (the
  IPI row also has an empty WITH/FROM). If the paper shows only interdependent stability, IMP or
  IGI would fit better than IPI.
- **The CP record leaves out a result from its own reference.** FlyBase annotates GAA1
  `is_active_in` GO:0031965 nuclear membrane (IDA, PMID:33496978), and the paper's headline finding
  is NE localisation of the non-catalytic subunits. CP lists only ER membrane. This is not wrong,
  since the complex as an enzyme is placed in the ER, but it shows that CP's complex-level CC
  describes where the complex works, not where each subunit is.
- `involved_in` GO:0016255 is appropriate for all GPI-T subunits. Fly GAA1 also has its own IMP
  for it (PMID:30914202).

### Cross-cutting observations from case 1

- The two records share the same `functions` text word for word, as does the template-derived
  pombe record. This is expected for ortholog-templated complexes. It means that **species-level
  support has to be checked separately for each record**, because the text gives no sign of it.
- Both records carry an `intenz` xref whose identifier is just `3` (EC class 3, hydrolases). This
  looks like a truncated EC number and should be checked against the human and budding-yeast
  records.
- Curation source matters: the pombe record was curated by UniProt for proteome coverage and cites
  a computational paper, while the fly record was curated by IntAct with species-specific
  experimental papers.

## Plan

- [ ] Fetch CP records for every complex behind a `ComplexPortal` GOA row in reviewed genes. Cache
      them as YAML (for example `projects/COMPLEXPORTAL/complexes/CPX-*.yaml`), joined to the GOA rows.
- [ ] For NAS rows, list the distinct cited PMIDs per species, and flag those whose cached
      title or abstract does not name the organism or the complex (as with PMID:15003443).
- [ ] List the BP terms that CP pushes to all subunits and that describe a downstream outcome rather
      than the complex's own process (cell wall organisation, development, signalling outcomes).
- [ ] Check CP ECO evidence and template provenance: was the complex inferred from an ortholog
      complex, and from which one?
- [ ] Compare CP membership with PAINT/IBA and with existing gene reviews, and track disagreements.
- [ ] Decide how gene reviews should record "correct term, wrong or unsupporting reference" for
      CP NAS rows. Options: `MODIFY` toward an ISO/IBA basis, or `ACCEPT` with a
      `reference_review` `MISCITED`.
- [ ] Prepare feedback for CP and UniProt curators once there are several confirmed cases.

## Sources

- Complex Portal web service: `https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-10141`,
  `.../CPX-2687`, `.../search/gaa1`
- QuickGO annotation API for UniProtKB:Q9W464
- `genes/SCHPO/gaa1/gaa1-goa.tsv`, `genes/SCHPO/gaa1/gaa1-ai-review.yaml`
- PMID:15003443, PMID:23250212, PMID:33496978
