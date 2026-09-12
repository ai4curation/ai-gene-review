# ACTL8 (Q9H568) — review notes

Working journal for the PAINT + affinage review. Provenance is recorded inline as
`[SOURCE "verbatim quote"]`.

## 1. What the primary record actually says

UniProt Q9H568 (ACTL8_HUMAN, Swiss-Prot, 366 aa) has **no FUNCTION comment at all**. The
functional content of the entry is three lines:

- `[file:human/ACTL8/ACTL8-uniprot.txt "CC   -!- SIMILARITY: Belongs to the actin family. {ECO:0000305}."]`
  — ECO:0000305 is a curator inference, not experimental.
- `[file:human/ACTL8/ACTL8-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytoskeleton {ECO:0000250}."]`
  — ECO:0000250 is *by similarity*, and **no source entry is cited after the ECO code**, so the
  similarity is untraceable. This matters because GOA converts this line into an IEA annotation
  (`GO:0005856 cytoskeleton`, GO_REF:0000044, WITH `UniProtKB-SubCell:SL-0090`).
- `[file:human/ACTL8/ACTL8-uniprot.txt "CC   -!- TISSUE SPECIFICITY: Strongly expressed in testis and pancreas. Weak"]`
  attributed to `ECO:0000269|PubMed:15905330`, corroborated by
  `[file:human/ACTL8/ACTL8-uniprot.txt "DR   HPA; ENSG00000117148; Tissue enriched (testis)."]`.

`PE 1: Evidence at protein level` — so the protein is detected (proteomics, and IHC, see §4).
There is no *functional or biochemical* data. The distinction matters: this is not a gene with no
data, it is a gene with no molecular-function data.

The entry also records one interaction:
`[file:human/ACTL8/ACTL8-uniprot.txt "CC       Q9H568; Q9Y5P4: CERT1; NbExp=3; IntAct=EBI-10306917, EBI-739994;"]`

An `AltName: Full=Cancer/testis antigen 57; Short=CT57` reflects its identification in the
CT-antigen survey PMID:15905330.

**The affinage record was not empty and must not be treated as if it were.** It returned
clear trust gates at fetch time, 8 citations, and a coherent oncology narrative. Checking UniProt's own
`RN`/`RX` list independently confirms only sequencing papers plus PMID:15905330 — so the
tumour-biology literature reaches this review *only* through affinage, and every claim taken from
it was re-read against the cached PMID.

## 2. GOA: 16 rows, zero IDA/IMP

`ACTL8-goa.tsv` (16 rows): 11 × IBA (GO_REF:0000033, GO_Central), 2 × IEA, 2 × IPI, 1 × IEP.
There is **no IDA, IMP, IGI or IC anywhere**. Per-aspect QuickGO tallies computed in
`ACTL8-bioinformatics/results.json`: MF 2 experimental of 4 total (both are the two
`GO:0005515 protein binding` IPI rows), BP 1 of 4 (the IEP), CC 0 of 8.

Note what PAINT did **not** transfer: no `ATP binding`, no `actin filament polymerization`, no
`structural constituent of cytoskeleton`. The brief anticipated those; they are absent. What it
*did* transfer is more specific and more surprising — β-actin's synapse, axon, NuA4-complex,
protein-kinase-binding and postsynaptic-cytoskeleton biology.

## 3. The central finding: ACTL8 is mis-placed in PANTHER's cytoplasmic-actin subfamily

Three PANTHER ancestral nodes appear in ACTL8's WITH/FROM fields. Asking QuickGO which *human*
genes each node donates to, and aligning each of those genes locally to β-actin
(`ACTL8-bioinformatics/analyze_actl8.py`, §4 of RESULTS.md), gives:

| node | terms donated to ACTL8 | human members | identity to ACTB |
|---|---|---|---|
| `PTN002631484` | GO:0015629 only | 18 (ACTA1/2, ACTB, ACTBL2, ACTC1, ACTG1/2, ACTL8/9/10, ACTRT1/2/3, POTE×5) | 33.7–100% |
| `PTN002631586` | GO:0005884, GO:0098973 | 9 | 8 members ≥ 90.7%; **ACTL8 = 33.8%** |
| `PTN007551913` | GO:0005737, GO:0007409, GO:0016020, GO:0019901, GO:0030424, GO:0035267, GO:0045202, GO:0048870 | 9 | 8 members ≥ 90.7%; **ACTL8 = 33.8%** |

The two narrow nodes contain ACTB, ACTG1, ACTBL2 and the five POTE actin-fusion genes — every
one of them ≥ 90.7% identical to β-actin over its actin block, because the POTE genes arose by
a C-terminal actin-family domain (UniProt SIMILARITY) that is nearly identical to beta-actin.
ACTL8 is the ninth member at **33.8%**, a
57-percentage-point gap to the next-least-similar member of its own subfamily.

So 10 of the 11 IBA rows are not family-level inferences at all: they are transfers of
**β-actin's specific cell biology** from nodes whose ancestral state was reconstructed entirely
from near-identical cytoplasmic actins. The one row from the deep node, `GO:0015629 actin
cytoskeleton`, is the one whose donating clade actually spans the divergent actin-like proteins,
and it is correspondingly generic. That contrast is the review's spine: the problem is not that
PAINT annotated ACTL8, it is that ACTL8 sits at the wrong depth in the tree.

This is the reciprocal of the `blow`/ACAP2 pattern from earlier in this campaign — a
mis-clustered member inheriting a tight subfamily's specifics — but here it is quantified rather
than argued, and the donor side is blameless.

### The comparison that closes it: none of ACTL8's own relatives is there

Asking QuickGO, for each divergent human actin-like / actin-related-T protein, which PANTHER nodes
appear in the WITH/FROM of its **own** IBA annotations:

| gene | own IBA rows | PANTHER nodes | under a narrow node? |
|---|---|---|---|
| **ACTL8** | **11** | PTN002631484, **PTN002631586, PTN007551913** | **yes, both** |
| ACTL7A | 3 | PTN000940351, PTN001377938, PTN008986520, PTN008986528 | no |
| ACTL7B | 3 | PTN000940351, PTN001377938, PTN008986520, PTN008986528 | no |
| ACTL9 | 2 | PTN000940351, PTN002631484 | no |
| ACTL10 | 2 | PTN000940351, PTN002631484 | no |
| ACTRT1 | 5 | PTN000748066, PTN000940351, PTN002631484 | no |
| ACTRT2 | 2 | PTN000940351, PTN002631484 | no |
| ACTRT3 | 2 | PTN000940351, PTN002631484 | no |

**ACTL8 is the only one of the eight.** Every relative either uses the ACTL7-specific nodes or the
same deep node PTN002631484 that gives ACTL8 its one defensible IBA. The consequence is
quantitative: ACTL8 carries **11 IBA rows against a median of 2** for its seven relatives, a roughly
five-fold inflation of its GO record traceable to a single tree placement. Verified against QuickGO
directly rather than read off the sibling ACTL7A/ACTL7B reviews, so it does not depend on their
conclusions.

## 4. Do the sources themselves carry evidence? Yes — all 47 of them

62 WITH/FROM tokens across the GOA rows (parsed programmatically from the TSV, never by hand;
the script asserts the count). 47 resolve to protein entries, 13 are non-protein sources
(PANTHER nodes, a GO id, and the `UniProtKB-SubCell` vocabulary id), 0 unresolved. **All 47
resolved sources carry their own experimental-code annotation for the exact term they donated**,
and 25 are distinct reviewed Swiss-Prot proteins.

Therefore `SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK` would be factually false here. The
correct classification for the failing rows is `PROPAGATION_BAD`: the source annotations are
sound; the transfer to this target is not.

Two resolver details worth recording:

- `MGI:MGI:87906` and `MGI:MGI:87904` each return 5 candidate entries (1 Swiss-Prot, 4 TrEMBL)
  and `RGD:628837` returns 3 (1 Swiss-Prot, 2 TrEMBL). Every lookup used `size=5` and every
  candidate is listed in RESULTS.md; the reviewed entry was used and its status printed.
- `WB:WBGene00000067` resolves only to **O45815, an unreviewed (TrEMBL) entry** for *C. elegans*
  act-5. It carries its own IDA×2 for the donated term, so its *evidence* is real — but its
  *name* is an automatic label, and the two facts are kept separate.
- `FB:FBgn0011743` is Drosophila **Arp53D**, a divergent actin-like protein rather than a
  conventional actin — a paralog-strength rather than ortholog-strength donor. That is legitimate
  PAINT practice, not a defect, and Arp53D turns out to retain both the nucleotide site (19/19
  compatible) and the filament interface (33/38 compatible), so it argues *against* rather than
  for ACTL8's annotations: a divergent actin that really does polymerise looks nothing like ACTL8.

## 5. Does the actin fold come with actin's residues? Partly for ATP, hardly at all for the filament

Computed from coordinates, not from memory (`ACTL8-bioinformatics/RESULTS.md`).

**Nucleotide site** — 19 residues within 4.0 Å of ATP or its divalent cation in PDB 2BTF chain A
(β-actin·ATP). ACTL8: 11 identical, 3 conservative, **5 non-conservative**. Retained: the entire
P1 phosphate loop (G13-S14-G15 → G11-S12-G13), K18 → K16, the Mg-coordinating Q137 → Q132,
G156/G158 → G151/G153, G182 → G177, the adenine-contacting G301-G302 → G299-G300 and Y306 → Y304.
Lost non-conservatively: **D157 → Y152, K213 → Q208, E214 → M209, T303 → N301, K336 → N334**.
For comparison all four conventional actins score 19/19 compatible, Arp2 16 + 3, Drosophila
Arp53D 16 + 3.

So this is genuinely intermediate. It is **not** a case of "fold without residues": most of the
phosphate-binding and adenosine-binding machinery is intact, so ATP binding cannot be excluded and
would be worth testing. Equally it is not intact: five direct contacts, including the P2-loop
aspartate, are gone. The honest conclusion is *untested*, which is why no ATP-binding term is
proposed here — proposing one would repeat the fold-name-to-activity slip in the opposite
direction.

**Filament protomer interface** — 38 residues within 4.0 Å of a neighbouring protomer in PDB 6DJO
(four F-actin protomers, chain C analysed). ACTL8: 8 identical, 3 conservative, **24
non-conservative, 3 gaps** — only 11 of 38 positions chemically compatible. β-actin scores 37 + 1;
Arp53D 29 + 4. Within the D-loop (structure residues 38–49), which makes the principal
longitudinal contact and is anchored in the alignment by an invariant proline, ACTL8 has **1
identical, 1 conservative and 8 non-conservative** of 10 contacts: `R39→C38, Q41→E40, G42→N41,
V43→P42, M44→G43, V45→P44, M47→Y46, Q49→R48`.

Both tallies are unchanged under a second scoring scheme (BLOSUM45 with harsher gaps), so they are
not an artefact of one gap model. The least reliable stretch of the alignment is the actin 60–67
loop, where ACTL8 carries a three-residue deletion — but the D-loop block, which carries the
argument, is independently anchored.

**Consequence.** Terms that assert ACTL8 is a structural part of an actin filament, or performs
β-actin's role in a postsynaptic actin network, are asserting exactly the property the sequence has
lost. Terms that merely place it in the actin cytoskeleton are not contradicted by this.

## 6. Family context: MF-dark is the rule for the divergent actin-like clade

32 human members of PTHR11937. 24 have at least one experimental-code MF annotation, but only
**7** have an *informative* one once bare `GO:0005515 protein binding` is excluded — nearly every
human protein has that from interactome screens, so counting it would make the survey say nothing.
Among the eight divergent actin-like / actin-related-T members (ACTL7A, ACTL7B, ACTL8, ACTL9,
ACTL10, ACTRT1, ACTRT2, ACTRT3) **only ACTRT1** has one (`GO:0003682 chromatin binding`). Most of
that set is testis-restricted but not all of it — UniProt calls ACTRT3 "Ubiquitously expressed" —
so it is grouped by sequence divergence rather than by tissue.

So "no molecular function is currently justifiable for ACTL8" is not a claim about ACTL8's
peculiarity; it is the normal state of this clade. And it is not because the family is
uncharacterisable — the conventional actins, Arp2/3 and the INO80/SRCAP actin-related subunits
(ACTR5, ACTR6, ACTR8) all have real MFs.

## 7. The two `protein binding` IPI rows are one interaction from one pipeline

Both rows point at the same partner, CERT1 / Q9Y5P4 (ceramide transfer protein; UniProt: "Shelters
ceramides inside its steroidogenic acute regulatory lipid transfer (START) domain"), the second
row on isoform Q9Y5P4-2.

Both references are CCSB yeast two-hybrid maps, and the second explicitly builds on the first:
`[PMID:32296183 "we previously generated HI-II-14 consisting of ~14,000 PPIs involving 4,000 proteins from screening ~40% of the genome-by-genome search space"]`
and
`[PMID:32296183 "yeast two-hybrid (Y2H) represents the only binary PPI assay that can be operated at sufficient throughput to systematically screen the human proteome for binary PPIs"]`.

So this is one Y2H interaction detected twice by the same laboratory using the same assay class on
an expanded search space, not two independent lines of evidence. No orthogonal or functional
validation of the ACTL8–CERT1 pair is reported, and no mechanism connects an actin-fold protein to
non-vesicular ceramide transfer. Treated as an unreplicated-by-orthogonal-method screen hit.

## 8. The IEP row rests on a 2-D gel differentiation screen

`GO:0030855 epithelial cell differentiation`, IEP, PMID:21492153 — a Caco-2 differentiation
proteomics study:
`[PMID:21492153 "Two-dimensional gel analysis yielded 53 proteins that were"]` …
`[PMID:21492153 "differently regulated during the differentiation process"]`, of which
`[PMID:21492153 "34 proteins that were identified by matrix-assisted laser"]` desorption
ionization-time of flight analysis.

The annotation therefore records *differential abundance during differentiation*, which is an
expression correlation, not evidence that ACTL8 is involved in the process. That is the standard
criticism of IEP supporting `involved_in`, and it is sufficient on its own. Two further reasons for
caution, raised as questions rather than asserted as errors because the full text is not available
and a UniProt curator read it: MALDI-TOF peptide-mass-fingerprint spot assignment within the actin
family is intrinsically hard, and ACTL8 is HPA testis-enriched while Caco-2 is an intestinal line.

## 9. The tumour literature: real, reproducible, and about ectopic expression

Five studies, four tumour types (breast, gastric, oral squamous, lung adenocarcinoma), four
independent laboratories - PMID:31962007 and PMID:35116946 share a Beijing thoracic-surgery group
and both use A549, so they count once. Direction is consistent throughout. Verbatim:

- TNBC: `[PMID:33883901 "silencing ACTL8 dramatically inhibited the proliferation in MDA-MB-231 and BT-549 cells relative Control and si-NC groups"]`;
  `[PMID:33883901 "the numbers of invasive and migrated cells were markedly repressed after ACTL8 silencing"]`;
  `[PMID:33883901 "silencing ACTL8 significantly reduced the phosphorylation level of PI3K, AKT and mTOR in MDA-MB-231 and BT-549 cells when compared with Control and si-NC groups"]`.
- Lung adenocarcinoma: `[PMID:31962007 "shACTL8 had a significant impact on proliferation, cell cycle progression, apoptosis, migration and invasion, angiogenesis and epithelial to mesenchymal transition (EMT) in A549 cells."]`;
  `[PMID:31962007 "nude mice revealed that ACTL8-knockdown inhibited A549 cell tumor growth."]`
- Gastric cancer: `[PMID:39322809 "ACTL8 knockdown markedly reduced GC cell proliferation and inhibited migration and invasion."]`
- Oral SCC: `[PMID:35051678 "knockdown of ACTL8 significantly inhibited the growth and mobility, arrested cell cycle and promoted apoptosis of TCA-83 and CAL27 cells"]`
- Lung adenocarcinoma transcriptomics: `[PMID:35116946 "cell proliferation was significantly inhibited in ACTL8 knockdown A549 cells"]`
- HNSCC protein-level detection: `[PMID:41129177 "ACTL8 exhibited moderate cytoplasmic staining in a focal pattern (Figure 1C)."]`

**PMID:32125225 (endometrial cancer) is RETRACTED** — the cached record carries
`pubmed_publication_types: - Retracted Publication` and `Retraction in Biosci Biotechnol Biochem.
2022 Feb 24;86(3):423`. The affinage narrative uses it (the p21 / E-cadherin / MMP-9 / N-cadherin
EMT claims come from it alone) without noting the retraction. Nothing in this review rests on it;
it is listed with `is_invalid: true` so the next reviewer does not re-import it.

The interpretive point that must not be lost: ACTL8 is a cancer/testis antigen, so in every one of
these systems it is **ectopically expressed**. `[PMID:41129177 "In our institutional cohort of de novo tumors, we find high expression of testis-selective ACTL8."]`
Knocking down a protein that the tissue does not normally express tells you what it does when
present, which is a real result, but it is not the gene's evolved physiological role. Its function
in testis — the one tissue where it is normally abundant — has never been studied. So the tumour
phenotypes are annotated as non-core regulation, and no mechanistic MF is inferred from them: no
paper shows ACTL8 binding any PI3K/AKT/mTOR component, and "acts upstream of" in these papers means
"knockdown lowers phospho-signal", which is compatible with an indirect route.

## 10. Actions taken and why

| Row | Action | One-line reason |
|---|---|---|
| GO:0015629 actin cytoskeleton (IBA) | KEEP_AS_NON_CORE | Only row from the deep node whose clade spans the divergent actin-like proteins; correctly scoped ancestral call |
| GO:0005737 cytoplasm (IBA) | KEEP_AS_NON_CORE | Independently corroborated by IHC in human tumour tissue, but generic; nothing on this gene can be core |
| GO:0005884 actin filament (IBA) | MARK_AS_OVER_ANNOTATED | Interface degraded, but heteropolymer incorporation cannot be excluded |
| GO:0098973 structural constituent of postsynaptic actin cytoskeleton (IBA) | REMOVE | β-actin-specific MF from a node of 91–100%-identical actins; the exact property (filament structural contribution) is the one ACTL8 has lost |
| GO:0098974 postsynaptic actin cytoskeleton organization (IEA) | REMOVE | Automatic BP step from the row above; falls with it |
| GO:0045202 synapse (IBA) | REMOVE | β-actin's neuronal compartment; no expression or localisation evidence |
| GO:0030424 axon (IBA) | REMOVE | Same |
| GO:0007409 axonogenesis (IBA) | REMOVE | Same |
| GO:0035267 NuA4 histone acetyltransferase complex (IBA) | REMOVE | The term's own definition names the actin subunits: "beta-actin and BAF53/ACTL6A" |

Note on scope for the NuA4 row: PTN007551913 assigns `GO:0035267` to nine human genes. ACTB's
membership is genuine (its own IDA, and it is named in the term definition together with
BAF53/ACTL6A), so it is the **other eight** - ACTG1, ACTBL2, ACTL8 and the five POTE genes - whose
rows are similarity transfers of a purification result. Stating this as "withdraw from all nine"
would have been wrong, and the suggested question now says eight.
| GO:0016020 membrane (IBA) | MARK_AS_OVER_ANNOTATED | Cortical-actin-derived; ACTL8 has no membrane-targeting feature and cannot form a cortical network |
| GO:0019901 protein kinase binding (IBA) | MARK_AS_OVER_ANNOTATED | Promiscuous binding term, no gene-specific support |
| GO:0048870 cell motility (IBA) | REMOVE | Machinery term from the mis-placing node; MODIFY would have left it an IBA asserting a bad ancestral state (see §12) |
| GO:0005856 cytoskeleton (IEA) | KEEP_AS_NON_CORE | Parent of the kept `GO:0015629`, so they must move together; the `ECO:0000250` provenance complaint is redundancy, not over-annotation (see §12) |
| GO:0005515 protein binding ×2 (IPI) | MARK_AS_OVER_ANNOTATED | One Y2H pair, one pipeline, no orthogonal validation |
| GO:0030855 epithelial cell differentiation (IEP) | MARK_AS_OVER_ANNOTATED | Differential abundance in a 2-D gel screen is expression, not involvement |
| GO:0008284 positive regulation of cell population proliferation | NEW | Five studies, four tumour types, four independent labs, including a xenograft; non-core (ectopic context) |
| GO:0030335 positive regulation of cell migration | NEW | The migration evidence, now on an IMP row rather than as a MODIFY replacement (see §12) |

The affinage record is cited in `references:` as an explicitly-labelled **lead** source
(`reference_review.correctness: LOW_QUALITY`), with the reason stated: it passed its own gates but
cites the retracted PMID:32125225 without flagging it. Its single use in an annotation is the
non-mechanistic sentence "ACTL8 protein is detected in the cytoplasm of tumor cells", which was
independently verified against PMID:41129177. No mechanistic claim anywhere in this review is
sourced from affinage prose.

`core_functions` is left **empty**. There is no experimentally supported molecular function, and
the honest output for an MF-dark gene is an empty list plus the resulting validation warning — not
invented content to silence it.

That choice constrains the actions: `ACCEPT` means "retain as representing the core function", so
with no core function established, no row can take it. `GO:0005737 cytoplasm` was initially marked
ACCEPT and is now `KEEP_AS_NON_CORE`, which is what its own reason had said all along.

## 11. Process log

- Worktree `/private/tmp/wt-ACTL8`, branch `paint/ACTL8`.
- `just fetch-gene human ACTL8` → 16 GOA rows, 6 seeded references.
- affinage: trust gates clear at fetch time (no `self_evaluation_pairwise` score), faith 85.7%,
  8 citations, all numeric PMIDs (no bioRxiv-shaped
  ids). Every claim used was re-verified against the cached PMID; the retraction of PMID:32125225
  was found this way and is not flagged by affinage.
- `just fetch-gene-pmids` + 9 extra `just fetch-pmid` calls.
- `ACTL8-bioinformatics/analyze_actl8.py`: five analyses, all from live data; `RESULTS.md` and
  `results.json` verified byte-identical on a second run (`diff`).
- Gates: `checkquotes.py` 53 quotes / 0 problems; `just validate human ACTL8` -> `Valid` with the
  single intentional "No core functions defined" warning; `cache/go/terms.csv` deletion check run as
  the last step before commit.
- `origin/main` merged in cleanly (18 commits, no conflicts, no shared-publication add/add clashes).


## 12. Round 2: what the PR review corrected

`ai4c-reviewer` requested changes on three points. All three were checked against the data and all
three were right; the actions below changed as a result. Recording them because each is a
generalisable trap.

### 12.1 MODIFY cannot move an annotation's evidence base

I had marked `GO:0048870 cell motility` as MODIFY with `GO:0030335` as the replacement, and the
reason claimed this "moves the evidence base from phylogeny to four independent human RNAi studies".
It cannot. **MODIFY changes the term and leaves `evidence_type` and `original_reference_id`
untouched**, so the replacement would still have been an IBA on GO_REF:0000033 with
`PANTHER:PTN007551913` in WITH/FROM — i.e. a request that PAINT reconstruct *positive regulation of
cell migration* as the ancestral state at the very node this review argues mis-places ACTL8. It is
not even a defensible ancestral call: β-actin's own evidence for `GO:0048870` is that it *is* the
motility machinery (IMP), not that it regulates migration.

Worse, the file already contained the right shape: `GO:0008284` was a `NEW`/`IMP` row built from the
same four papers. Migration and proliferation were being treated asymmetrically for no reason.

Fix: `GO:0048870` → REMOVE on the same PTN007551913 grounds as its sibling rows, plus a second
`NEW` row for `GO:0030335` with `evidence_type: IMP`, carrying the four quotes unchanged.

**Rule: if the justification for a MODIFY is "this puts the annotation on better evidence", the
action is wrong — MODIFY only swaps the term. Use REMOVE + NEW.**

### 12.2 I quoted the favourable half of my own table

The filament-interface argument cited exactly two comparators, ACTB (38/38) and Arp53D (33/38). My
own `RESULTS.md` contained one that cuts the other way and appeared nowhere in the review:

| protein | compatible / 38 |
|---|---|
| ACTB, ACTG1, ACTA1, ACTC1 | 38 |
| Arp53D | 33 |
| ACTR1A centractin | 28 |
| ACTR2 (Arp2) | 22 |
| ACTRT1 | 21 |
| ACTL7B, ACTL9 | 16 |
| ACTL7A | 14 |
| **ACTL8** | **11** |
| **ACTR3 (Arp3)** | **8** |
| ACTL10 | 5 |

**Arp3 scores below ACTL8** — and Arp2/Arp3 form the first protomer pair of a daughter filament at
an Arp2/3 branch, so they demonstrably occupy protomer positions in an actin-containing structure.
So the metric bounds *canonical incorporation into a conventional two-stranded filament*; it does
**not** show that a protein cannot be part of any actin-containing assembly. Neither "Arp3" nor
"ACTR3" appeared anywhere in the YAML or these notes.

Fixed by adding the full ranking and this caveat to `RESULTS.md` (computed, not prose), citing
`| ACTR3 (human Arp3) | 8 |` as supporting text on the two rows where the tally is load-bearing, and
restating every claim built on it at the weaker strength. No action changed: the `GO:0098973` REMOVE
rests on the postsynaptic/neuronal-evidence half, and `GO:0005884` was already only
MARK_AS_OVER_ANNOTATED.

**Rule: when a script produces a comparison table, cite the rows that hurt the argument, not just
the ones that help. Selective quotation of your own output is the easiest error to miss.**

### 12.3 A parent and its child cannot get opposite verdicts

`GO:0005856 cytoskeleton` was MARK_AS_OVER_ANNOTATED while its descendant `GO:0015629 actin
cytoskeleton` was KEEP_AS_NON_CORE. Verified via QuickGO's `ancestors` endpoint that `GO:0005856` is
indeed an ancestor of `GO:0015629`, so that pair of verdicts asserts ACTL8 is in the actin
cytoskeleton but that saying "cytoskeleton" overshoots — incoherent. My own `reason` text had
already diagnosed the real problem correctly as *redundancy* ("Redundant with the GO:0015629 IBA
rather than independent of it"), which is a provenance complaint, not an over-annotation.

Fix: `GO:0005856` → KEEP_AS_NON_CORE with `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT`, keeping the
uncited-`ECO:0000250` criticism in the reason.

**Rule: before assigning actions, check the subsumption relations among the annotated terms. Two
rows on the same axis must move together.**

### 12.4 The three non-blocking suggestions, all adopted

- **Absolutes about neuronal expression.** "has never been detected in a neuron" hardened absence of
  a report into absence of the protein — and UniProt's own reference list includes an MGC cDNA clone
  isolated from *brain*, which I had read and not connected. Reworded to "no reported neuronal
  expression or localisation", with the brain-clone caveat stated.
- **NuA4 "include" vs "only".** GO definitions list subunits with "include", so naming β-actin does
  not strictly exclude γ-actin. Reworded: the definition shows the complex's actin content is
  recorded *per paralog from purification*, and no purification places ACTL8 there.
- **`core_functions`.** `molecular_function` is not a required slot on `CoreFunction`, so a
  description-only entry would validate. Kept empty on the view that a core function should assert
  something, and the decision is now recorded as a `suggested_questions` entry so it is a project
  convention question rather than a silent omission.

Final actions: **7 REMOVE, 6 MARK_AS_OVER_ANNOTATED, 3 KEEP_AS_NON_CORE, 2 NEW, 0 MODIFY.**

### 12.5 Round 2 approval, plus three residual accuracy edits

`ai4c-reviewer` re-reviewed and **approved**, confirming all three blocking items resolved against
the data rather than against the response text, and noting that moving the Arp3 caveat into the
generating script was the right fix because it cannot be re-omitted on a rerun. Three 🔵 items
remained; all three were taken rather than merged over, because each was a small factual
overstatement and those are worse left inside a curation record than a short delay:

- **One absolute survived my own softening pass.** The synapse row still read "a cell type in which
  ACTL8 has never been detected" while the sibling axon row had already been softened and given the
  brain-cDNA caveat. Two rows making the same argument must read the same way; fixed.
- **A "consequently" carried more than the premises.** The `description` said the interface loss
  meant "there is consequently no evidence that ACTL8 polymerises". The absence of evidence comes
  from the absence of experiments, not from the sequence comparison — and after the Arp3 disclosure
  the sequence half is explicitly the weaker premise. Split into two claims: the interface loss makes
  canonical two-stranded incorporation unlikely, and separately no polymerisation experiment has ever
  been done.
- **Residual arithmetic in the NuA4 reason.** It said the correction "applies to ACTL8, ACTBL2 and
  the five POTE genes" — seven of the node's nine descendants, with ACTB correctly excluded but ACTG1
  silently unaddressed. Now states all nine explicitly: ACTB stands, seven have no supporting
  purification, and ACTG1 is the borderline case the "include not only" wording covers.

**Rule from this round: a softening pass has to be re-grepped, not eye-checked. I changed one of the
two rows making the same argument and believed I had changed both.**
