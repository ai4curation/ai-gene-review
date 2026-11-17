---
title: "Non-coding RNA curation"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, rat]
genes: [MIR155, XIST, KCNQ1OT1, SNORD3A, SNORD116-1, TERC, Mir30e, Mir100, Mir127, Mir26a-1, Mir384]
---

# Non-coding RNA curation

**Bottom line:** GO annotation of ncRNAs is two different things that need two
different kinds of review. About 80% of human ncRNA rows (38,114 of 47,274) come
from a single source, the Rfam2GO family mapping (`GO_REF:0000115`). That is
reviewed once per Rfam family, not once per locus. The rest is a much smaller
body of experimental curation, almost all of it on microRNAs: 590 human
RNAcentral sequences carry an experimental row, and 528 of those are miRNAs. Only
a handful of lncRNAs and ribonucleoprotein RNAs (TERC, RN7SK, XIST, MALAT1, NEAT1,
H19) have enough literature-backed rows to justify a gene review. For tRNA, rRNA,
snRNA, SRP RNA and almost all snoRNAs, every row is a family-level inference, so
gene-by-gene review of them adds nothing that reviewing the Rfam mapping would not.

## Which sequence is the gene product

An ncRNA gene product in GOA is an RNAcentral sequence id (`URS…_taxid`), and
one gene usually has several. A miRNA gene has a precursor hairpin and mature 5p
and 3p arms, each a separate URS. RNAcentral also often has duplicate URS ids for
the same mature sequence. **Which one carries the annotations depends on the
group that made them:**

| Species | Experimental miRNA rows sit on | Main groups |
|---|---|---|
| Mouse | the precursor (`mmu-mir-30e precursor`), sometimes also the mature arm | MGI |
| Human | the mature arm (`hsa-miR-155-5p`) | BHF-UCL, ARUK-UCL |
| Rat | precursor and both arms | RGD, BHF-UCL |

The rule therefore is: **review the sequences GOA annotates, not the one a
nomenclature authority points to.** HGNC's RNAcentral cross-reference for
`MIR155` is the precursor (URS000062749E_9606), which has two Rfam2GO rows. The
mature 5p arm (URS0000338542_9606) has 132 rows, 105 of them experimental, and a
duplicate 5p sequence (URS0000D54CAD_9606) has 7 more IDA rows. The review in
`genes/human/MIR155` was made on the precursor and so never saw that evidence;
it is being redone.

**One review per gene.** A review covers every GO-annotated sequence of the
gene. `ai-gene-review fetch-ncrna` now:

1. searches RNAcentral (EBI Search, `gene:"SYMBOL" AND TAXONOMY:"taxid"`) for the
   gene's sequences in that species only;
2. counts each candidate's GOA rows and experimental rows in QuickGO;
3. takes the sequence with the most experimental rows as the review `id`, and
   refuses to choose when several tie (e.g. the ten Rfam-only copies of U3);
4. downloads GOA rows for all annotated sequences of the gene into one
   `GENE-goa.tsv`;
5. sets `product_type` from RNAcentral's `rna_type`.

Seeded rows that were asserted on a sequence other than the review's `id` carry
`gene_products: [URS…]`. GOA matching is by term, evidence, reference, qualifier
and WITH/FROM, so the same claim made on two arms is one row with both ids
listed. `--rnacentral-id` still overrides the resolver.

## What is curatable

Every number below comes from `projects/NCRNA/ncrna_intake.py`, which writes
`projects/NCRNA/intake/<species>.yaml`. It downloads all QuickGO rows with
`geneProductType=rna`, counts experimental rows (EXP, IDA, IMP, IGI, IPI, IEP and
the HTP family) per sequence, and types each sequence with RNAcentral's own
`rna_type`. Data retrieved 2026-11-16.

| | Human | Mouse | Rat |
|---|---|---|---|
| RNA sequences with any GO row | 20,694 | 10,213 | 5,670 |
| … with an experimental row | 590 | 670 | 225 |
| … of which miRNA | 528 | 544 | 200 |
| … of which lncRNA / antisense | 46 | 93 | 24 |
| … with ≥3 experimental references | 174 | 269 | 66 |
| … non-miRNA with ≥3 experimental references | 8 | 8 | 2 |
| Rfam2GO rows (`GO_REF:0000115`) | 38,114 of 47,274 | 15,002 of 30,091 | 12,508 of 26,305 |

How each class should be handled:

| Class | Approach | Why |
|---|---|---|
| **miRNA** | Gene review, ranked by experimental references (hsa-miR-21-5p 84, miR-29b-3p 35, miR-221-3p 33, …) | Hundreds of sequences with real evidence. Expect heavy IEP and target-reporter rows, judged as in [IEP](IEP.md) |
| **lncRNA** | Gene review for the few with ≥2 references: XIST, KCNQ1OT1, MALAT1, HOTAIR, NEAT1, GAS5, H19 (rat), Mir17hg, Firre, Fendrr, lincRNA-p21 | Small set; mechanisms are gene-specific, so there is no family rule to review instead |
| **RNP RNAs** | Gene review: TERC, RN7SK, RMRP, RPPH1, SNORD3A (U3), SNORD116 | Few genes, each with a defined molecular role inside a complex |
| **snoRNA, snRNA, tRNA, rRNA, SRP RNA** | Review the Rfam2GO mapping per family; gene review only for the rare sequence with experimental rows | Thousands of loci, all with the same family-level rows |
| **piRNA** | Not a priority | 3 human sequences with experimental rows; piRNAs act as populations, not as individually studied genes |

The 10 mitochondrial tRNA reviews (`MT-TC` … `MT-TW`) were made when their GOA
files had no rows at all. They are biologically sound but are not evidence
audits, and they should not be used as a model for further tRNA work.

## Rfam2GO: reviewing the family mappings

Rfam2GO (release 15.1, dated 2026-01-16) is 5,983 mappings over 3,185 Rfam
families. Like InterPro2GO, a mapping is applied to every sequence the family's
covariance model hits, so one wrong mapping is wrong on every locus. It is
reviewed at family level, with the same entry-centric pattern as
`src/ai_gene_review/schema/pfam_entry_review.yaml`: the family, the GO terms it
maps to, supporting and counter examples, and a per-mapping verdict.

Mappings to look at first:

- **miRNA precursor families → `GO:0016442` RISC complex.** All 1,598 miRNA
  families map to RISC complex and `GO:0035195` miRNA-mediated
  post-transcriptional gene silencing. Rfam models the precursor hairpin, and the
  precursor is not loaded into RISC; only the mature strand is. The process term
  is defensible for the gene, but the component term is wrong for the sequence it
  lands on. These are the two IEA rows on the MIR155 precursor.
- **`GO:0005515` protein binding on 41 families** (CsrB, CsrC, RsmZ, McaS, ArcZ,
  RRE, …). Several of these are protein-sequestering sRNAs, which an informative
  MF term can describe, and the project's protein-binding policy removes bare
  `GO:0005515` anyway.
- **Self-cleaving ribozymes → `GO:0004540` RNA nuclease activity** (hammerhead,
  HDV, hairpin, CPEB3). A cis self-cleavage is a different claim from an RNase
  acting on other RNAs.
- **cis-regulatory elements mapped as if they were genes** (RNA thermometers
  such as ROSE and PrfA, `Hsp90_CRE` → response to temperature stimulus). The
  element is part of an mRNA, so the annotation's subject should be the
  transcript the element sits in.
- **snoRNA families → `GO:0006396` RNA processing (795) and `GO:0005730`
  nucleolus (783).** Mostly sound, but scaRNAs act in Cajal bodies, and orphan
  snoRNAs have no known processing target.

## Families

Two family levels matter: Rfam families (above), and miRNA seed families, where
paralogous mature miRNAs share a seed and hence most of their targets (miR-17/20/
93/106, miR-29a/b/c, miR-221/222). A seed-family review is the ncRNA counterpart
of a PANTHER family review: it would place the shared function at the family
and record which members carry a paralog-specific role. That needs a family
descriptor for seed families, since there is no PANTHER or PTN id to anchor it.

## Data problems found while scoping

- **Experimental rows on retired RNAcentral ids.** Mouse has 29 such sequences
  and rat 15. RNAcentral reports `is_active: false` (for example rat
  URS00022AE95D, "selenoprotein W"), but GOA still annotates them. These are
  source-defect candidates for MGI and RGD.
- **A lncRNA transcript carrying TERC's evidence.** Human "lnc-ACTRT3-2:2",
  typed `telomerase RNA` by RNAcentral, has experimental rows from 14
  references. It looks like a transcript model that overlaps TERC; check this
  before reviewing TERC.
- **Silent empty GOA files.** `fetch_goa_data` used to turn a failed QuickGO
  request into a header-only TSV. During a QuickGO outage on 2026-11-16 (its
  taxonomy back end refused connections, so every request with
  `includeFields=taxonName` returned HTTP 500), that would have written an empty
  GOA file for any gene, and overwritten a real one under `--force`. It now
  raises instead.

## Plan

- [x] Resolver: species-restricted RNAcentral search, GOA-driven choice of
      primary id, error on ties, all annotated sequences fetched
      (`src/ai_gene_review/etl/gene.py`)
- [x] `gene_products` slot on existing annotations; seeding fills it
- [x] Intake rankings for human, mouse and rat (`projects/NCRNA/intake/`)
- [x] Fix `product_type` on KCNQ1OT1 (LNCRNA) and SNORD3A (SNORNA)
- [ ] Re-review MIR155 on its mature sequences
- [ ] Gene reviews: TERC, RN7SK, MALAT1, NEAT1, then the top human miRNAs
- [ ] Rfam family review schema (from `pfam_entry_review.yaml`) and the first
      reviews: a miRNA family (RISC complex), CsrB/RsmZ (protein binding), a
      hammerhead ribozyme
- [ ] Decide how a miRNA seed family is anchored
- [ ] Turn the workflow into a `ncrna-curation` skill once MIR155 and one Rfam
      family review have been done by hand
