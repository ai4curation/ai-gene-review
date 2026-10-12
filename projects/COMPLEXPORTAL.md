---
title: "Complex Portal Annotation Correctness"
maturity: SCOPING
tags: [PIPELINE]
species: [human, yeast, DROME, worm, SCHPO, mouse, ECOLI, ARATH, rat]
genes: [gaa1, CHMP3, BAK1, DFFB, ced-3, PPP3CA, SDHB, ESPL1, MBL2, PDGFA, CLCN7, TERT, CAC2, pstS, DYNC2H1, RPL18A, Actb]
autolink_gene_symbols: false
---

# Complex Portal Annotation Correctness

**Bottom line:** Complex Portal (CP) annotates protein complexes, and GOA copies each complex's
process (BP) and location (CC) terms, but not its function (MF), to every subunit, under
`assigned_by: ComplexPortal`. This project checks whether those subunit rows are correct. The
5,005 such rows in this repo's cached GOA files all belong to reviewed genes, and 88% of them
survive review (95% of CC, 83% of BP). Fewer than 1% are outright wrong; most rejected rows are
imprecise. The typical failures are regulation terms in the wrong direction (the inhibited subunit
annotated as the inhibitor), downstream processes, a partner's activity, and promiscuous subunits
such as actin inheriting every complex's terms. Simple rules raise the rejection rate among
flagged rows to about 29% against a 10% base, so they help triage but cannot replace reading.
Corroboration works the other way: rows another group also annotated from the same paper were
almost never rejected (2 of 445). 41% of the papers CP cites are cited by no other group in GOA,
and a quarter of those are reviews; 20 rows give a review an experimental evidence code. We also
found a direct contradiction, CHMP3, where CP and UniProt draw opposite conclusions from the same
paper. The review verdicts judge terms, not references, so reference problems are under-counted.
The gaa1 case shows one: the fission-yeast GPI transamidase record rests on a paper that only
predicts GPI-modification sites.

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
4. **Process specificity.** Is a BP term the process the complex performs, or a downstream
   consequence (for example, cell wall organization for an anchoring enzyme)?

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

**GO/GOA pipeline status** (from GOA and IEA working-group minutes, April to May 2026; not
independently verified here):

- The roll-down is a documented GOA rule: complex members receive all of the complex's CC and BP
  annotations, but not its MF. A separate step generalises some membrane-child CC terms to
  `membrane`; its scope and rationale are not fully documented.
- An early-2026 Alliance release dropped CP `part_of` rows on members. GOA reported this as a
  pipeline bug, to be restored in the next release. It was not a policy change. We have not
  checked that the rows came back.
- The IEA working group judged the NAS pipeline acceptable for CPX entities. It flagged that
  deriving subunit rows associates proteins with papers that do not mention them, and proposed
  IC with a GO_REF (from the `part_of` CC annotation) instead of the complex's PMID. No decision
  had been implemented as of these minutes.

That proposal speaks to this project's reference-support question (question 2). In the gaa1 case
the PMID is weak even for the complex, so changing the evidence code alone would not fix the
pombe rows.

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
*S. pombe* 105; mouse 103; *E. coli* 100; *A. thaliana* 48; rat 4.

## First accuracy estimate from existing gene reviews

Every one of the 5,005 CP subunit rows in the cached GOA files belongs to a gene that already
has a review (1,093 genes). Each row was matched to its review action on (GO term, evidence
code, reference) using [`scripts/cp_review_join.py`](COMPLEXPORTAL/scripts/cp_review_join.py),
and all rows matched. "Acceptable" means `ACCEPT` or `KEEP_AS_NON_CORE`.

| Slice | Rows | Acceptable | Over-annotated | Modify | Remove | Undecided |
|---|---|---|---|---|---|---|
| **All** | 5,005 | **88.0%** | 4.6% | 4.6% | 0.8% | 1.9% |
| CC | 2,191 | 95.0% | 1.2% | 2.3% | 0.5% | 1.0% |
| BP | 2,814 | 82.6% | 7.2% | 6.3% | 1.1% | 2.7% |
| IPI | 686 | 94.9% | 1.9% | 2.9% | 0 | 0.3% |
| IDA | 984 | 90.4% | 3.2% | 4.5% | 0.8% | 1.1% |
| NAS | 3,131 | 85.6% | 5.9% | 5.0% | 1.0% | 2.5% |
| IMP | 153 | 89.5% | 1.3% | 3.9% | 1.3% | 3.9% |

By species, the acceptable share is 88.0% for human (3,820 rows), 86.6% for budding yeast (382),
94.7% for fly (228), 90.2% for worm (215), 94.3% for pombe (105), 86.0% for *E. coli* (100),
97.9% for *Arabidopsis* (48), 100% for rat (4) and 65.0% for mouse (103). The mouse figure comes almost entirely
from Actb: 27 of its 36 rejected rows are β-actin inheriting the processes of every complex it
belongs to.

**How to read this.** About 88% of CP-derived subunit annotations survive review, 95% for CC and
83% for BP. Outright wrong rows are under 1%; most problems are imprecision (wrong-direction
regulation terms, downstream outcomes, over-general terms). All 502 rejected rows, with the
review's reason, are in [`data/cp_rejected_rows.yaml`](COMPLEXPORTAL/data/cp_rejected_rows.yaml).

### Examples of rejected rows

| Pattern | Gene | CP-derived term | Evidence | Why rejected (from the gene review) |
|---|---|---|---|---|
| Regulation in the wrong direction | human/BAK1 | negative regulation of release of cytochrome c from mitochondria (GO:0090201) | IDA PMID:15901672 | BAK is the restrained target, not the negative regulator, in the anti-apoptotic complex |
| Regulation in the wrong direction | human/DFFB | negative regulation of apoptotic DNA fragmentation (GO:1902511) | IDA PMID:11371636 | DFFB is the nuclease being inhibited, not the inhibitor |
| Regulation in the wrong direction | worm/ced-3 | negative regulation of execution phase of apoptosis (GO:1900118) | IMP PMID:10101135 | The inhibitor is MAC-1; CED-3 is the inhibited protease (ced-4 likewise) |
| Regulation in the wrong direction | human/PPP3CA | positive regulation of calcium ion import across plasma membrane (GO:1905665) | NAS PMID:17640527 | Anchored calcineurin suppresses PKA enhancement of CaV1.2 current |
| Downstream or neighbouring process | human/SDHB | proton motive force-driven mitochondrial ATP synthesis (GO:0042776) | NAS PMID:30030361 | Complex II pumps no protons (SDHA and SDHC likewise; 20 rows of this term rejected) |
| Downstream or neighbouring process | human/ESPL1 | maintenance of mitotic sister chromatid cohesion (GO:0034088) | NAS PMID:34290405 | Separase cleaves cohesin; cohesion is maintained by cohesin, shugoshin-PP2A and separase inhibitors |
| Activity of a partner | human/MBL2 | proteolysis (GO:0006508) | IDA PMID:22691502 | The MASP proteases cleave C4/C2; MBL has no protease activity |
| Activity of a partner | human/PDGFA | peptidyl-tyrosine autophosphorylation (GO:0038083) | NAS PMID:11297552 | Autophosphorylation is done by the receptor, not the ligand |
| Wrong process for the protein | human/CLCN7 | transepithelial chloride transport (GO:0030321) | IDA PMID:32851177 | ClC-7 is an endolysosomal antiporter |
| Wrong process for the protein | human/TERT | telomere maintenance via recombination (GO:0000722) | NAS PMID:20351177 | Recombination-based telomere maintenance (ALT) is the telomerase-independent pathway |
| Wrong location for a subunit | yeast/CAC2 | nucleosome (GO:0000786) | IDA PMID:30239791 (a review) | CAF-1 deposits histones but is not part of the nucleosome (MSI1, RLF2 likewise) |
| Wrong location for a subunit | ECOLI/pstS | membrane (GO:0016020) | NAS PMID:3881386 | PstS is a periplasmic binding protein |
| Reference does not cover the subunit | human/DYNC2H1 | male germ cell nucleus (GO:0001673) | NAS PMID:36973253 | Paper is about dynein-1 (DYNLRB1/2) complexes and does not mention dynein-2 |
| Reference does not cover the subunit | human/RPL18A | striated muscle contraction (GO:0006941) | NAS PMID:34081545 | Paper studies RPL3L, not RPL18A |
| Promiscuous subunit | mouse/Actb | kinetochore (GO:0000776) | NAS PMID:11078522 | Transferred from chromatin-remodeller complexes that contain actin; 27 Actb rows rejected |

**Limitations.**

- The reviews are AI reviews, not an independent gold standard, and they lean towards `ACCEPT`.
- They judge whether a term is right for the gene, not whether the cited reference supports it.
  So the reference-support failures that the IEA working group flagged, and that gaa1 shows, are
  mostly not counted here. The three pombe gaa1 `REMOVE` rows are counted as removed only because
  they duplicate the IBA rows.
- Human rows dominate the total (76%).
- Treat 88% as an upper bound on term correctness, and as saying nothing about evidence
  correctness. A manual audit of a random sample is the next step, scoring term and reference
  separately.

## Rules for flagging suspect rows

Spot checks do not scale, so we tested simple rules that could flag CP rows for review. Each rule
was scored against the same review verdicts: precision is the share of flagged rows that the
review rejected, compared with a base rate of 10.0% (502 of 5,005). Script:
[`scripts/cp_flag_rules.py`](COMPLEXPORTAL/scripts/cp_flag_rules.py); full output with examples:
[`data/cp_rule_eval.yaml`](COMPLEXPORTAL/data/cp_rule_eval.yaml).

| Rule | Flagged | Rejected | Precision | Lift | Recall |
|---|---|---|---|---|---|
| Outcome-type BP term (regulation, response to, development, morphogenesis, differentiation) **and** subunit has ≥5 CP references | 396 | 116 | 29.3% | 2.9× | 23% |
| "response to" term | 85 | 20 | 23.5% | 2.4× | 4% |
| Regulation term not corroborated by another group | 720 | 164 | 22.8% | 2.3× | 33% |
| Regulation term (any) | 751 | 164 | 21.8% | 2.2× | 33% |
| Outcome-type term, paper cited only by CP | 396 | 89 | 22.5% | 2.2× | 18% |
| Outcome-type term, paper is a review | 119 | 25 | 21.0% | 2.1× | 5% |
| BP, subunit has ≥5 CP references | 960 | 182 | 19.0% | 1.9× | 36% |
| BP, gene not named in the cached full text | 345 | 77 | 22.3% | 2.2× | 15% |
| Any BP | 2,814 | 414 | 14.7% | 1.5× | 82% |
| Gene not named in cached full text | 572 | 88 | 15.4% | 1.5× | 18% |
| Paper is a review | 812 | 105 | 12.9% | 1.3× | 21% |
| Paper cited only by CP anywhere in GOA | 2,121 | 229 | 10.8% | 1.1× | 46% |
| **Same gene, term and paper also annotated by another group** | 445 | **2** | **0.4%** | 0.04× | — |

What this shows:

- **No single rule is precise enough to act on automatically.** The best combination roughly
  triples the rejection rate, to about 29%. These rules are for triage: they order the review
  queue but do not replace reading.
- **These precisions are optimistic, for two reasons.** First, about 20 rules were scored on the
  same 5,005 rows and the best combination was chosen afterwards, with no held-out set, so the
  top figure is biased upwards. Second, the verdicts come from AI gene reviews that probably apply
  the same heuristics the rules encode (regulation direction, downstream outcomes, promiscuous
  subunits). Precision here therefore partly measures agreement with the reviewers' own priors,
  not with the truth. A curator-adjudicated sample is needed before quoting these figures as
  rule performance.
- **Regulation terms are the clearest content signal.** They account for a third of all
  rejections, and the failure is usually direction or target confusion: the complex regulates X,
  but a subunit is the thing being regulated.
- **Promiscuous subunits** (actin, shared ATPase or ubiquitin-ligase subunits) are the clearest
  gene-level signal.
- **"Gene not named in the paper" is weak on its own.** Matching on gene symbols and UniProt
  synonyms misses protein names, and it is uninformative for abstract-only papers. A paper
  counts as full text only if it is flagged `full_text_available` *and* at least 20,000
  characters are cached, because some HTML extractions carry the flag but little more than the
  abstract (PMID:20616062 is one). On that basis the rule reaches 1.5×, and 2.2× for BP terms.
- **Corroboration is the strongest signal in the other direction.** When another group has
  annotated the same gene, term and paper, the row was almost never rejected (2 of 445). Rows
  like these could be skipped in an audit.
- **Having been read by another curator, without corroboration, is not a conflict signal.** Rows
  whose paper another group used for the same gene, but for other terms, are rejected at 8.7%,
  slightly below the base rate.

### Direct conflicts with other annotations

Only 4 CP rows clash with a `NOT` annotation on the same gene and term. Three of them are a direct
contradiction from the same paper with the same evidence code:

| Gene | Term | CP row | Contradicting row |
|---|---|---|---|
| human/CHMP3 | nucleus organization (GO:0006997) | IMP PMID:20616062 | NOT, UniProt, IMP PMID:20616062 |
| human/CHMP3 | mitotic metaphase chromosome alignment (GO:0007080) | IMP PMID:20616062 | NOT, UniProt, IMP PMID:20616062 |
| human/CHMP3 | regulation of mitotic spindle assembly (GO:1901673) | IMP PMID:20616062 | NOT, UniProt, IMP PMID:20616062 |
| human/SIRT1 | nucleolus (GO:0005730) | IDA PMID:18485871 | NOT, UniProt, IDA PMID:16079181 (a different paper) |

PMID:20616062 (Morita et al. 2010) depleted each of the 11 human ESCRT-III proteins and reports
spindle and nuclear defects for "most" of them. The per-protein results are in figures that the
cached text does not include, so we cannot tell from here which curator is right for CHMP3.
UniProt's NOT suggests CHMP3 depletion was one of the exceptions, and CP's positive rows look
like the ESCRT-III complex-level result rolled down to every subunit. The CHMP3 review currently
accepts or keeps all three rows. They should be re-examined against the figures, and this check
should run routinely.

## Papers cited only by Complex Portal

QuickGO was queried for every PMID cited on a CP row, counting all annotations in GOA that cite
it and how many of those are CP's. PubMed publication types were added from NCBI E-utilities.
Data: [`data/cp_pmid_usage.yaml`](COMPLEXPORTAL/data/cp_pmid_usage.yaml); scripts:
[`cp_pmid_usage.py`](COMPLEXPORTAL/scripts/cp_pmid_usage.py),
[`cp_pmid_pubtypes.py`](COMPLEXPORTAL/scripts/cp_pmid_pubtypes.py).

- **447 of the 1,084 PMIDs (41%) are cited only by CP** anywhere in GOA. They support 2,121 of
  the 5,005 subunit rows (42%). By species, the share of CP rows resting on such papers is
  highest for human (1,809 of 3,793 PMID-cited rows) and lowest for pombe (15 of 105) and
  *Arabidopsis* (3 of 48).
- **A quarter of them are reviews.** PubMed tags 110 of the 447 CP-only papers as Review,
  against 3 of the 637 papers that other groups also cite. GO curators generally avoid
  annotating from reviews, so CP is close to the only route by which these reviews become GO
  evidence. The largest are reviews of V-ATPase structure (PMID:32001091, 77 rows), OXPHOS
  complex assembly (PMID:30030361, 70 rows, 20 rejected), the SCF complex (PMID:34445249, 63 rows)
  and TRAPP complexes (PMID:27066478, 48 rows, 20 rejected).
- **CP-only papers are newer**, with a median year of 2015 against 2009 for papers that other
  groups also cite. This fits CP curating recent structural and complex-composition papers that
  MOD curators have not reached.
- **On their own they are not much worse.** Rows resting on CP-only papers are rejected at
  10.8%, against 9.5% for shared papers. The review verdicts judge the term rather than the
  reference, though, so this is the place where reference problems most likely go uncounted.

**A deterministic evidence-code check.** 812 CP rows cite a review, and almost all of them are NAS,
which is the right code. But 20 rows assign an experimental code to a review:

- PMID:30239791 (CAF-1 mechanism review): 9 IDA and 3 IPI rows for yeast CAC2, MSI1 and RLF2,
  including the three "nucleosome" rows that were removed.
- PMID:29249570: IDA for CUL3, KEAP1 and RBX1 (proteasome-mediated catabolism).
- PMID:17101441: IPI for RPD3 and RCO1 (Rpd3S complex).
- PMID:22898774: IDA for MAD2L1.
- PMID:24984776: IPI for BLM.
- PMID:12067652: EXP for GEMIN5.

Most of these terms are biologically fine, but the evidence code says an experiment was reported
in a paper that only reviews experiments. This needs no biological judgement to check, though
PubMed's Review tag should be confirmed for each paper, since some primary papers carry it too.

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

- [x] First estimate: join CP GOA rows to existing review actions (88% acceptable).
- [x] Flagging rules scored against review verdicts; papers cited only by CP characterised.
- [ ] Re-examine human/CHMP3 against the PMID:20616062 figures (CP IMP vs UniProt NOT, same paper).
- [ ] Confirm PubMed Review status for the 6 papers carrying experimental codes, and report them to CP.
      Two of them (PMID:17101441, PMID:30239791) are also used by other groups, so for those the
      feedback concerns the evidence code only, not CP being the sole route to GO.
- [ ] Manual audit of a stratified random sample (by species, aspect and evidence), scoring
      term correctness and reference support separately.
- [ ] Fetch CP records for every complex behind a `ComplexPortal` GOA row in reviewed genes. Cache
      them as YAML (for example `projects/COMPLEXPORTAL/complexes/CPX-*.yaml`), joined to the GOA rows.
- [ ] For NAS rows, flag papers whose cached text does not name the organism or the complex
      (as with PMID:15003443); gene-name matching alone proved weak.
- [ ] List the BP terms that CP pushes to all subunits and that describe a downstream outcome rather
      than the complex's own process (cell wall organisation, development, signalling outcomes).
- [ ] Check CP ECO evidence and template provenance: was the complex inferred from an ortholog
      complex, and from which one?
- [ ] Compare CP membership with PAINT/IBA and with existing gene reviews, and track disagreements.
- [ ] Decide how gene reviews should record "correct term, wrong or unsupporting reference" for
      CP NAS rows. Options: `MODIFY` toward an ISO/IBA basis, or `ACCEPT` with a
      `reference_review` `MISCITED`.
- [ ] Prepare feedback for CP and UniProt curators once there are several confirmed cases.

## Reproduce

Run from the repo root. Step 1 parses every gene review (about 2 minutes) and writes an
intermediate file that is not committed. Steps 2 and 3 call QuickGO and NCBI E-utilities, so
their output is a snapshot (2026-10-11 for the committed copy).

```bash
D=projects/COMPLEXPORTAL
uv run python $D/scripts/cp_review_join.py /tmp/cp_joined.json $D/data/cp_rejected_rows.yaml  # CP rows + review actions
uv run python $D/scripts/cp_pmid_usage.py $D/data/cp_pmid_usage.yaml        # GOA-wide PMID usage
uv run python $D/scripts/cp_pmid_pubtypes.py $D/data/cp_pmid_usage.yaml     # add PubMed types
uv run python $D/scripts/cp_flag_rules.py /tmp/cp_joined.json $D/data/cp_pmid_usage.yaml $D/data/cp_rule_eval.yaml
```

Step 1 also writes `data/cp_rejected_rows.yaml` (rows whose action is `MARK_AS_OVER_ANNOTATED`,
`MODIFY` or `REMOVE`). It matches review annotations on (term, evidence, reference), skips
`negated` review rows so that a CP row cannot inherit the verdict on a NOT row with the same key,
and reports any remaining ambiguous matches.

## Sources

- Complex Portal web service: `https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-10141`,
  `.../CPX-2687`, `.../search/gaa1`
- QuickGO annotation API for UniProtKB:Q9W464
- `genes/SCHPO/gaa1/gaa1-goa.tsv`, `genes/SCHPO/gaa1/gaa1-ai-review.yaml`
- PMID:15003443, PMID:23250212, PMID:33496978
