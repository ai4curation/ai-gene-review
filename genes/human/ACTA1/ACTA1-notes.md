# ACTA1 (P68133) — review notes

> Historical review journal: the 2026-09-26 source and annotation re-audit at the end supersedes earlier judgments, including stress-fiber, interaction-screen and HDA interpretations.
Skeletal muscle α-actin. 377 aa, PANTHER PTHR11937, `PE 1: Evidence at protein level`.
Reviewed as part of the PAINT + affinage campaign, after ten actin-family siblings
(ACTL7A/7B, ACTL8, ACTL10, ACTR1A/1B, ACTR5, ACTR8, ACTR10, ACTRT3).

## Why this gene is the inverse of its siblings

Every actin-family gene reviewed before ACTA1 was a *divergent* member, where the risk
was inheriting canonical actin biology it does not have. ACTA1 **is** the canonical
actin, so the phylogenetic transfers that had to be argued down elsewhere are here
correct, and had to be argued *up*.

The concrete demonstration is `GO:0005200` structural constituent of cytoskeleton.
Within PTHR11937 that term is asserted **once**, at `PTN000940351`, the
conventional-actin node, by IBD from ten seeds — and **negated by IRD at eight
descendant nodes** (counted from `interpro/panther/PTHR11937/PTHR11937-paint.tsv`:
1 IBD + 8 IRD). ACTL7A, ACTL7B and ACTRT3 each needed their `GO:0005200` row removed
or generalised. ACTA1 sits on the *accepting* side of that split and is the recipient
the assertion was made for. All ten of its donors resolve and all ten carry their own
experimental evidence for the term.

The negation sweep ran in two dated batches — five nodes on 2025-08-05
(`PTN000233752`, `PTN000233887`, `PTN000234048`, `PTN001732543`, `PTN008986528`) and
three on 2026-04-16 (`PTN000233596`, `PTN000233796`, `PTN007551901`). **ACTA1's presence
in the retained set was checked positively, not inferred from the absence of a
negation**: a QuickGO query for `GO:0005200` in human with evidence `ECO:0000318` returns
ACTA1 among the recipients, alongside the other conventional actins (ACTA2, ACTC1, ACTG2,
ACTB, ACTG1, ACTBL2, the POTE paralogues), ACTR10, and the divergent genes not yet
adjudicated. Absence of a negation would have been an absence, not a finding.

So the campaign's reflex — that an IBA over-reaches — is wrong here, and PAINT's node
placement in this family is demonstrably working: it discriminates ACTA1 from ACTL8
correctly. That is worth recording as a positive result, because the family's PAINT
handling has otherwise only been reported when it failed.

## The actual defect: three pipelines each substitute a generic actin for ACTA1

ACTA1's over-annotations do not come from disease pleiotropy (there are no
nemaline-myopathy phenotype rows in GOA at all — the 7 BP rows cover only 5 distinct
terms). They come from **isoform substitution**: three independent pipelines treat
"actin" as one thing, and each injects non-muscle actin biology into a
skeletal-muscle-restricted gene.

This matters because ACTA1's tissue restriction is not a soft claim:
[PMID:16288873 "gestation and is the exclusive isoform expressed in muscle from infancy through"]
— α-skeletal actin is the *exclusive* sarcomeric isoform in skeletal muscle from
infancy, and α-cardiac actin, not ACTA1, predominates in heart
[PMID:16288873 "birth. Although alpha-skeletal actin is thought to be the predominant sarcomeric"].

### (a) AgBase ISS — a chicken *smooth-muscle* actin donates five terms

Rows 19-23 (`GO:0010628`, `GO:0030027`, `GO:0030175`, `GO:0044297`, `GO:0090131`) all
have WITH/FROM `UniProtKB:P08023`, which resolves to **ACTA2, actin aortic smooth
muscle, of *Gallus gallus***.

The donor is not weak — P08023 holds all five terms by its own IDA/IMP — but all five
come from **one paper**, PMID:10633868, an antisense study of endothelial-mesenchymal
transformation in chick cardiogenesis:
[PMID:10633868 "alpha-Smooth-muscle actin (SMA) is the major isoform of adult vascular tissues."],
[PMID:10633868 "lamellipodia/filopodia of invading mesenchymal cells. Antisense"],
[PMID:10633868 "oligodeoxynucleotide (ODNs) specific for SMA reduced both SMA expression and"].

Three things are wrong with the transfer:

1. **Wrong paralog.** Chicken ACTA2 is the ortholog of human *ACTA2*. Chicken has its
   own ACTA1 (`P68139` ACTS_CHICK) — the correct ortholog exists in the same species
   and was not used.
2. **Wrong context.** `GO:0044297` cell body is defined as "The portion of a cell
   bearing surface projections such as axons, dendrites, cilia, or flagella"; ACTA1 is
   a sarcomeric thin-filament protein, not a migratory mesenchymal cell.
3. **ISS is uninformative between α-actins.** Measured (see
   `ACTA1-bioinformatics/RESULTS.md`): ACTA1 is **97.9%** identical to ACTA2 and
   **98.9%** to ACTC1. A sequence-similarity transfer among α-actins is satisfied
   trivially and carries no isoform information — which is exactly why the block
   landed on four genes at once.

**Scope, from QuickGO** — the block is on all four human α-actins *and* mouse Acta1:
ACTA2 (legitimate, true ortholog), ACTG2 (arguable, smooth muscle), **ACTA1**
(sarcomeric — wrong), **ACTC1** (sarcomeric — wrong), **mouse Acta1** (wrong). The
cytoplasmic actins ACTB and ACTG1 did **not** receive it. The block is therefore keyed
on α-actin-ness, not on actin-ness, which is the positive control: it discriminates,
and it discriminates on the wrong feature. Retracting it from ACTA1, ACTC1 and mouse
Acta1 fixes three genes in one edit.

### (b) Reactome — a generic `F-actin (all)` polymer

Eight of the 50 GOA rows are `GO:0005829` cytosol TAS, one per Reactome reaction. They
are not eight findings; they are one export. Four are Striated Muscle Contraction
reactions (ATP Hydrolysis By Myosin, Calcium Binds Troponin-C, Release Of ADP From
Myosin, Myosin Binds ATP) and one is a dystrophin-glycoprotein-complex reaction —
genuine ACTA1 pathways.

The other three are **E-cadherin adherens-junction** reactions: `R-HSA-9934294`
CDH1-associated CTNNA1 binds VCL, `R-HSA-9934410` CDH1 forms homotypic trans-dimers,
`R-HSA-9934486` CDH1-associated CTNNA1 binds F-actin. ACTA1 is in them because
Reactome's participant is a generic polymer, `F-actin (all) [cytosol]`, whose
reference entities are **all six human actins** — ACTB, ACTA2, ACTG1, ACTG2, ACTC1 and
ACTA1 (checked via `ContentService/data/participants/R-HSA-9934486/referenceEntities`).
UniProt's own DR block records the consequence:
[file:human/ACTA1/ACTA1-uniprot.txt "DR   Reactome; R-HSA-9764561; Regulation of CDH1 Function."]

So skeletal-muscle α-actin is placed in an epithelial adherens junction by set
membership. The GO term that results, `cytosol`, is bland enough that the error is
invisible from the GO record alone — which is why it is worth naming.

**But the defect is in the pathway membership, not in the GO term, and the actions have
to reflect that.** A first draft of this review split the eight rows — `KEEP_AS_NON_CORE`
for the five muscle reactions, `MARK_AS_OVER_ANNOTATED` for the three epithelial ones —
and the repo validator was right to flag it: what each of these rows actually *asserts in
GO* is only that ACTA1 is in the cytosol, and that claim is exactly as true (and as
uninformative) for the CDH1 reactions as for the cross-bridge cycle. Giving an identical
term two different verdicts implied the term was more wrong in some rows than others,
which it is not. All eight are now `KEEP_AS_NON_CORE`, the routing argument lives in the
three reasons, and the fixable item is filed as a Reactome-side correction in
`suggested_questions`. Worth recording because the same temptation will arise on any gene
whose over-annotation is upstream of the GO term it produces.

### (c) PAN-GO/PAINT — the same substitution running *outward* from ACTA1

The one row where ACTA1 is the *source* of the problem. `GO:0001725` stress fiber is an
IDA on ACTA1 from PMID:15198992, whose actin-localisation experiments are
transfections: [PMID:15198992 "patients. Transfection of C2C12 myoblasts with mutant actin(EGFP) constructs"].
Stress fibers are a property of the undifferentiated C2C12 myoblast host, which
incorporates any actin; the paper's abstract never mentions stress fibers, and the
strong result is in patient muscle
[PMID:15198992 "present within insoluble actin filaments isolated from muscle from two ACTA1 NM"].
By the campaign's own rule, an ectopic-expression readout is IMP, not IDA.

That single datum then fanned out. PAN-GO promoted it to **core**: the PAINT file shows
`PTN000233075 GO:0001725 C IBD false UniProtKB:P68133 taxon:32523`, i.e. one of the six
PAN-GO annotations UniProt advertises for ACTA1 is stress fiber, seeded by ACTA1
itself. And QuickGO shows **all four** of mouse Acta1's `GO:0001725` rows carry
WITH/FROM `P68133`: ISS (UniProt), IEA (Ensembl), ISO (GO_Central) and IBA (PAN-GO).
One transfection readout became five annotations across two species and four pipelines.

The three sarcomeric siblings on the same PAN-GO node (`GO:0005865`, `GO:0005884`,
`GO:0030240`) are correct and stay; the point is specific to stress fiber.

## Peptide-level measurement, and what it does *not* show

Five rows place ACTA1 outside the cell by high-throughput MS: exosomes from prostatic
secretions (PMID:23533145), parotid gland (PMID:19199708) and trabecular meshwork
(PMID:21362503), plasma microparticles (PMID:22516433) and tears (PMID:23580065). None
sampled skeletal muscle; HPA calls ACTA1 "Tissue enriched (skeletal)".

`actin_peptide_specificity.py` asks whether shotgun MS can attribute an actin peptide
to ACTA1 at all. Of 63 ACTA1 tryptic peptides in a 7-30 aa window, only **9 (14.3%)**
occur in no other human actin, and those 9 collapse to just **3 independent regions**
(most are nested missed-cleavage variants — reporting 9 would overstate it). Of the 54
shared peptides, **29** are shared with ACTB and/or ACTG1, which are expressed in every
tissue those five studies sampled.

**This does not refute the rows.** Three distinguishing regions exist, so ACTA1-specific
attribution is achievable and a study reporting one of those peptides would settle it.
What it shows is that the attribution cannot be *assumed* — the rows are untested, not
refuted. Deliberately the same distinction ACTL8 drew between its refuted
filament-interface result and its untested ATP-site result.

## Interactions: one Y2H screen counted three ways (the ACRV1 pattern again)

Eleven `GO:0005515` rows. The `fetch-gene` stub collapsed seven of them into one; all
seven were restored so each partner gets its own verdict (the ACTR5 lesson —
`existing_annotations` is counted against the 50-row TSV, not the 44-row stub).

Queried IntAct directly (`/intact/ws/interaction/findInteractions/P68133`, 142
interactions). All seven PMID:32814053 partners — ZNF20, INCA1, ASCL4, LIAT1, PNMA5,
SYNC, CAMK2A — are logged as **`two hybrid pooling` + `validated two hybrid` +
`two hybrid array`**, three sub-methods of the *same* screen, MI-score **0.56**, no
orthogonal assay. So UniProt's `NbExp=3` is one experiment counted three times, exactly
as found on ACRV1. The panel coheres as a neurodegeneration bait set, i.e. as the
screen's design rather than ACTA1's biology.

One partner deserves a flag rather than dismissal: **SYNC (syncoilin)** is a genuine
muscle intermediate-filament-associated protein, so an ACTA1–syncoilin interaction is
biologically plausible. It is still a single 0.56 Y2H hit, so it belongs in
`suggested_experiments`, not in an annotation.

ANXA8 (rows 8, 16) is `anti tag coip` in BioPlex 2.0 and 3.0 — two datasets, one
method and one pipeline, in HEK293T and HCT116, neither a muscle line.

All ten annotated partners resolve to **reviewed** Swiss-Prot entries with canonical
lengths; the only non-canonical identifier, `Q6ZQX7-4`, is a declared LIAT1 *isoform*,
not a partial ORFeome clone. So the ACRV1 TrEMBL/ORFeome check is negative here.

## The asymmetry: GOA has the screens and not the studies

Worth stating separately because it is the one place where ACTA1's record is *missing*
something rather than carrying too much, and it was only noticed by asking why two
pipeline-fetched publications had ended up uncited.

All eleven `GO:0005515` rows come from screens or from incidental observations. UniProt,
meanwhile, records two ACTA1 interactions with **experimental `ECO:0000269` tags**, from
dedicated studies, and neither has any GO row:

- **TTID / myotilin**
  [file:human/ACTA1/ACTA1-uniprot.txt "TMSB4X (By similarity). Interacts with TTID (PubMed:10958653)."]
- **USP25**, mapped to a region and with an isoform preference
  [file:human/ACTA1/ACTA1-uniprot.txt "Interacts (via its C-terminus) with USP25; the interaction occurs for"]

Queried by PMID in QuickGO: `PMID:10958653` carries **7** annotations in all of GO and
every one is on MYOT or mouse Myot — including MYOT's own `GO:0051393` alpha-actinin
binding IDA — so it was curated from the myotilin side and never reciprocated onto actin.
`PMID:16501887` carries **zero** annotations anywhere in GO, despite being titled for
sarcomeric-protein interactions and despite UniProt reading an ACTA1 result out of it.

So the shape of this gene's interaction record is: nine weakly-supported rows from two
high-throughput sources present, two experimentally-supported interactions from
hypothesis-driven studies absent. Adding the latter two would improve the record more than
removing any of the former nine, which is why this is filed as a question rather than as a
set of REMOVEs. (No `NEW` row is proposed for them, because `GO:0005515` is exactly the
uninformative term the project guideline discourages and neither partner has a specific
binding term available.)

## Two interactions that are real and stay

- **DNASE1** (`P24855`, row 49, PMID:12849983): the classic actin–DNase I interaction,
  measured on genuine human skeletal α-actin
  [PMID:12849983 "similarly to native actin, as shown by DNase I affinity purification, Western"].
  I considered and **rejected** upgrading this to `GO:0060703` deoxyribonuclease
  inhibitor activity. Two reasons: the paper demonstrates *affinity purification*, i.e.
  binding, not inhibition; and DNase I is not a physiological partner of sarcomeric
  actin, so the term would assert an in vitro activity as a biological function. (For
  what it is worth, `GO:0060703`'s 279 annotations are almost all phage/bacterial
  Gam-like inhibitors by IEA; no actin carries it.)
- **HBHA** (`P9WIP9`, row 24, PMID:18835984): *M. tuberculosis* adhesin binding actin by
  single-molecule force spectroscopy
  [PMID:18835984 "HBHA is able to specifically bind actin, via both its N-terminal and C-terminal"].
  Real and specific, but host-pathogen rather than core. Note the abstract never states
  **which** actin isoform was assayed, so the assignment to ACTA1 specifically is
  unverified — a fourth instance of the same generic-actin question. I did not push this
  to REMOVE: full text is unavailable and MTBBASE curators may have had it.

## What ACTA1 is missing

`GO:0051371` **muscle alpha-actinin binding** is absent from GOA, yet it is one of
ACTA1's best-evidenced molecular functions. UniProt maps it to two discrete segments —
[file:human/ACTA1/ACTA1-uniprot.txt "FT   REGION          112..125"] and
[file:human/ACTA1/ACTA1-uniprot.txt "FT   REGION          360..372"], both noted
"Interaction with alpha-actinin" — and the affinity has been *measured on actin isolated
from human muscle*: [PMID:16945537 "isolated from the muscle biopsy and examined by in vitro motility assay. The"],
[PMID:16945537 "Z-line protein alpha-actinin was reduced 10 fold. This is the first report on a"].
A mutation that reduces the affinity 10-fold presupposes the wild-type affinity.
Proposed as a `NEW` annotation.

`GO:0006936` muscle contraction (TAS, PMID:10508519) is correct but one level too
general for a gene whose isoform is skeletal-exclusive; `GO:0003009` skeletal muscle
contraction is the right term. The cited paper's own framing is skeletal-specific
[PMID:10508519 "that mutations in the human skeletal muscle alpha-actin gene (ACTA1) are"], and
the exclusivity is established independently [PMID:16288873].

## Checks that came back negative (recorded so they are not re-run blind)

- **Reference projection** (the ACTR8 ComplexPortal defect): every functional/localisation
  reference queried by PMID in QuickGO and counted by entity. `PMID:1423520` → **1**
  annotation total; `PMID:11333380` → **1**; `PMID:15198992` → **3** (all ACTA1);
  `PMID:12849983` → **3** (2 ACTA1 + the reciprocal DNASE1); `PMID:10508519` → **5** (all
  ACTA1). No complex-plus-subunits pattern, and no phenotype term spreading past the gene
  assayed. **Negative.**
- **Retraction / erratum / expression of concern**: 28 cited PMIDs read from
  `CommentsCorrections/RefType` on each cited article's own record — not by a
  publication-type search, which cannot see a Publisher Correction. **Zero flagged.**
- **IBA landing above its donor** (the ACRV1 defect): rows 3-6 land at the same terms
  their donor holds, the donor being ACTA1 itself. No downward MODIFY available.
- **Heterogeneous-donor/LCA caveat** (AADACL4) on `GO:0005200`: does **not** apply. All
  ten donors agree and hold the term themselves, so it is not a broad LCA over a mixed
  clade and no specificity upgrade exists.
- **Unresolved WITH/FROM tokens**: zero, across all 26 rows that carry the field. Four
  WormBase donors initially came back empty because `xref:wormbase-WBGene…` does not
  resolve in UniProt; fixed with a plain identifier query, then each mapping verified
  against the resolved entry's own cross-references.

## Three checks added after the coordinator flagged them mid-review

- **Duplicate YAML keys.** PyYAML keeps the *last* of a duplicated mapping key, so a
  second `supported_by:` silently deletes the first one's entries — and no existing gate
  can see it, because the quote checker and both validators walk the *parsed* document.
  `audit_claims.py` now checks it two ways, a strict loader plus a raw-versus-parsed count
  of provenance entries. Result here: **51 raw `- reference_id:` lines = 51 parsed
  entries, no duplicate keys anywhere.** (Note `original_reference_id:` also contains the
  substring, which is why the pattern is anchored to the list-item form.)
- **Comparator sequence length, before any scoring.** A truncated Swiss-Prot entry
  manufactures divergence out of residues the sequence never reaches. `actin_peptide_
  specificity.py` now refuses to score a panel containing an entry more than 5 aa below
  the panel median. All six conventional actins pass (377/377/377/376/375/375, median
  377), so the distinguishing-peptide count is not a truncation artefact. ACTA1 being a
  conventional actin, this was always more likely to bite the comparators than the
  subject — but it is now asserted rather than assumed.
- **Annotation count is not entity count, and results paginate.** Corrected in
  RESULTS.md: entities are enumerated from the returned rows for the small
  gene-specific references, and for the three high-throughput ones (20,010 / 9,514 /
  3,731 annotations) the entity count is recorded as **unavailable** rather than
  estimated from a page. Nothing in the review rests on an entity count for them.

## Notes on the tooling (both cost a cycle, both are guarded now)

- **QuickGO's annotation endpoint rejects every non-UniProtKB gene-product id** used in
  this file's WITH/FROM fields — `MGI:`, `SGD:`, `RGD:`, `WB:`, `dictyBase:`, `PomBase:`,
  `FB:`, `CGD:` all return HTTP 400. The first version of the resolver reported `0`
  annotations for four donors, which reads as "these sources carry no evidence" when they
  had never been asked. Now 400 is treated as non-retryable, the query is re-routed via
  the resolved UniProt accession, and the route is recorded in the output.
- **The dead-accession guard needed correcting.** `O15507` (the accession the ACTR10
  review found dead) returns an entry **with its own `primaryAccession`** and nothing
  else, so an accession-match check passes it. The authoritative signal is
  `entryType: "Inactive"`; UniProt also gives `inactiveReason: {MERGED → P56159}`. The
  self-test now requires the guard to fire on `O15507` *and* to let `P68133` through, so
  it discriminates rather than refusing everything.

## Three of my own errors, caught by the repo's own checks

Recorded because each is a general trap, not an ACTA1 quirk.

1. **I wrote a reference title from memory and the pre-write hook blocked it.** For
   PMID:16288873 I invented a plausible descriptive title beginning "Comparison of…" and
   naming skeletal and cardiac muscle; the real title begins "Defining alpha-skeletal and
   alpha-cardiac actin expression in human heart and skeletal muscle…" and goes on to
   state the paper's conclusion about the absence of cardiac involvement in ACTA1 nemaline
   myopathy. (The invented string is deliberately not reproduced here: `audit_claims.py`
   treats it as a retracted phrasing and fails if it reappears on any prose surface.)
   Plausible, wrong, and it is a *load-bearing* reference — it carries the exclusivity fact behind both the
   `GO:0003009` MODIFY and the whole AgBase argument. The same hook also caught
   PMID:23580065, where the cached title spells "naïve" with a diaeresis. Titles must be
   copied from `publications/PMID_*.md`, never typed.
2. **My dead-accession guard did not work, and its own self-test proved it.** I wrote the
   liveness check as "`primaryAccession` must equal the accession requested", then tested
   it on `O15507` — the accession the ACTR10 review found dead. It **passed the check**:
   an inactive UniProt entry comes back *with its own accession* and nothing else, no
   protein name, no gene, no organism. The authoritative signal is `entryType:
   "Inactive"`, and UniProt additionally reports `inactiveReason: {MERGED → P56159}`. The
   guard now reads that field and names the replacement, and a fifth self-test case
   requires a live accession (`P68133`) to still pass, so it discriminates rather than
   refusing everything. Note the shape: the accession check was not weak, it was blind to
   the exact class of thing it was written to catch.
3. **A silent zero read as a finding.** The first resolver run reported that the four
   *C. elegans* WITH/FROM donors carry no evidence for `GO:0015629`. They had never been
   asked: QuickGO rejects every non-UniProtKB gene-product id in this file's WITH/FROM
   fields with HTTP 400, and UniProt does not cross-reference WormBase by `WBGene` id, so
   both halves of the lookup failed quietly. Fixed by treating 400 as non-retryable,
   re-routing through the resolved UniProt accession, recording the route in the output,
   and verifying every model-organism mapping against the resolved entry's own
   cross-references. The corrected count is **24/24 donors with their own experimental
   evidence**, not 20/24 — and it is the number that makes the `GO:0015629` ACCEPT solid.

## What PR review caught (two factual, three presentational)

The reviewer approved with no blocking findings, and two of its five suggestions were real
errors that I verified before conceding:

1. **The peptide analysis digested the ORF, not the protein.** ACTA1 has `INIT_MET 1
   "Removed"` and `CHAIN 3..377`, the acetylated Cys-2 of the intermediate form being
   cleaved by ACTMAP, so the ORF's N-terminal tryptic peptide does not exist in vivo — and
   my `suggested_experiments` entry named it, and gave the region as starting at residue 1
   rather than 3. The observable peptide is **`DEDETTALVCDNGSGLVK`**, region **3-30**.
   (The two retracted strings are deliberately not reproduced on any prose surface;
   `audit_claims.py` fails if either reappears.) Recomputed on the mature
   chain, with comparators contributing both their ORF and mature digests: **all counts are
   unchanged** (63 / 9 / 14.3% / 54 / 29 / 3 regions), and the script now asserts that the
   two forms agree. So the numbers were never wrong; the experiment was unbuildable. The
   general shape is worth keeping — *a sequence analysis is only as biological as the
   sequence it starts from*, and a UniProt `CHAIN` feature is where that is decided.
2. **A by-similarity residue assignment stated as fact.** The description gave the two
   MARTX cross-link residue positions as though they had been measured on ACTA1;
   UniProt tags both `CROSSLNK` features `ECO:0000250|UniProtKB:P60709`, i.e. transferred
   from beta-actin. The cross-linking itself is real, the residue numbering on the skeletal
   isoform is not measured, and the description now says so.

The other three were presentational and all three were taken: `GO:0015629` now appears in
`core_functions.locations` and its row explains why the child is accepted while the bare
`GO:0005856` parent is demoted; the `GO:0051371` row explains why the evidence code is IDA
rather than IPI (the paper names only "the Z-line protein alpha-actinin", so there is no
partner accession to put in a with/from field, and inventing ACTN2 or ACTN3 would be a
guess); and the `GO:0043531` reason now leads with the nucleotide cycle — ATP-bound G-actin
is the assembly-competent species, the ADP protomer is the aged form that gives the
filament polarity and that cofilin recognises — with the cross-review precedent demoted to
corroboration.

## A third error of my own: I relayed a sibling's claim as a fact

Found while auditing my own numbers after the review round, and the most instructive of the
three because nothing flagged it — it was internally consistent, verbatim-sourced and wrong.

The `GO:0043531` row placed ACTA1 among a supposed pair of family members holding both
nucleotide terms. That came from the merged ACTR10 review, whose line reads
`GO:0005524` ATP binding: ACTA1, ACT1 — a list about **ATP binding alone**, which I turned
into a **count about two terms**. Measured across all 533 reviewed (Swiss-Prot) PTHR11937
members: **31 reviewed members carry** `GO:0005524` and exactly **1** carries `GO:0043531` —
ACTA1. It is the **sole** ADP binding holder among reviewed entries, not one of two, and the
corrected fact is stronger than the wrong one.

**The scope qualifier is not a hedge, and PR review was right to insist on it.** That member
list comes from InterPro's reviewed-only endpoint, so 533 is ~0.6% of the 88,887 proteins
PTHR11937's metadata reports. An earlier draft called it the whole family, which the
measurement does not support. The family-wide version is an *argument* and is now labelled as
one: ACTA1's `GO:0043531` is manual TAS, unreviewed entries get only IEA, and no IEA pipeline
maps the actin fold to ADP binding — so an unreviewed holder is unlikely, but unlikely is not
measured.

The brief's rule is *relay a sibling's claim as a claim, not as a fact*, and I broke it in
the specific way that is hardest to catch: a coordinator's or sibling's summary carries more
apparent authority than the review it came from, and this one arrived pre-formatted as a
quotable line.

Getting the *right* answer took two attempts, and the first failure is the same shape as the
WormBase one earlier in this review: querying by GO term alone returns page 1 of ~205,000
(`GO:0043531`) and ~9.6 million (`GO:0005524`) annotations, and intersecting that page with
the family yields an **empty set for both terms** — which reads as "no member carries this",
the exact opposite of the truth. `nucleotide_terms_in_family.py` keys the query on the
family's accessions instead, batches them, and asserts no batch was itself truncated.

## A fourth error, and the reviewer found it in a guard I had just written

The second review approved but left three notes on the new script code. All three were
real, and two were defects in guards — the class this review had already tripped over twice.

1. **`orf_and_mature_counts_agree` compared cardinalities, not sets.** Fixing it
   immediately exposed a live disagreement the count had masked: both forms yield exactly
   **9** distinguishing peptides, but the sets differ in **4** members. So the cheap check
   was certifying an agreement that did not hold.

   The right invariant turned out to be *narrower* than "sets agree", because the sets are
   not supposed to be identical — modelling the N-terminal processing is the whole point, so
   the N-terminal peptides must differ. What is asserted now is: the counts agree **and every
   peptide the two forms disagree about lies at the N-terminus**. A divergence anywhere else
   would mean the offset had corrupted the digest.

2. **And then that guard did not fire when I broke it.** Setting `MATURE_START = 50` should
   have been rejected; instead the script produced a confident, wrong region (`50-64
   GQKDSYVGDEAQSKR`) with no complaint. The cause: I had written the tolerance as
   `MATURE_START + 1`, so it **scaled with the parameter under test** — a bigger offset bought
   itself a wider window. *A guard whose tolerance is set by the thing it guards is worse than
   no guard, because it still reports success.* The tolerance is now a fixed constant grounded
   in the biology (N-terminal processing removes at most a couple of residues), and
   `MATURE_START = 50` is rejected outright.

   Break-testing further showed an honest limit: `MATURE_START = 4` passes every check and
   yields region `4-30`. The guard distinguishes a *corrupting* offset from a *plausible* one,
   not a correct one from an off-by-one. So the number is no longer typed in at all —
   `mature_chain_start()` parses it from the CHAIN feature in `ACTA1-uniprot.txt` whose note
   matches the entry's RecName, and fails if that is not exactly one feature. It returns 3,
   agreeing with the value I had hand-typed; the point is that it is now derived rather than
   transcribed. *Any constant read out of prose and typed in is a latent bug.*

3. **`MATURE_START = 3` was documented for ACTA1 but reused for all six comparators.** ACTB
   is annotated `CHAIN 1..375` *and* `CHAIN 2..375` "N-terminally processed", so its
   observable forms begin at residue 1 or 2 and slicing it at 3 both mis-stated its processing
   and missed a form. Comparators now contribute their digests at offsets 0, 1 and 2, which
   only enlarges the comparator pool and so only shrinks the distinguishing set — conservative
   by construction, and independent of any per-gene annotation being complete.

4. **The reviewer also found a hole in the claim lint itself:** a retracted phrasing had
   survived in a post-mortem because an embedded quotation mark split the matched substring.
   The guard was evadable by punctuation while still reporting OK. `flatten()` now strips
   quotation marks and normalises dashes, and it caught the surviving instance on the next
   run.

Every headline number survived all of this unchanged: 63 peptides, 9 distinguishing (14.3%),
54 shared, 29 shared with ACTB/ACTG1, 3 regions at 3-30, 287-317 and 338-361.

## Action summary (50 GOA rows + 1 NEW)

| action | n | what |
|---|---|---|
| ACCEPT | 15 | thin filament / sarcomere / actin filament CCs, `GO:0005200` (×2), ATP + ADP binding, ATP hydrolysis, myosin binding, thin-filament assembly (×2), actin cytoskeleton (×2) |
| MARK_AS_OVER_ANNOTATED | 16 | 9 bare `GO:0005515` (7 Y2H + 2 BioPlex ANXA8), 5 extracellular HDA, both `GO:0001725` stress fiber rows |
| KEEP_AS_NON_CORE | 13 | `GO:0005856`, 2× `GO:0048741`, all 8 `GO:0005829` Reactome cytosol, the DNASE1 and HBHA interactions |
| REMOVE | 5 | the chick smooth-muscle-actin ISS block |
| MODIFY | 1 | `GO:0006936` → `GO:0003009` skeletal muscle contraction |
| NEW | 1 | `GO:0051371` muscle alpha-actinin binding |

Counts are read off the finished YAML, not tallied by hand; 50 non-`NEW` rows against 50 GOA
rows, asserted by `build_source_entities.py`.

## 2026-09-26 source and annotation re-audit

This section supersedes the earlier annotation judgments and biological interpretations in this journal. The earlier record is retained as provenance, including decisions now corrected. The saved bioinformatics outputs remain historical computational results, not evidence that a particular experiment observed a shared peptide or that an interaction was false.

### Baseline, scope and research access

- HGNC-approved ACTA1, HGNC:129, human UniProt P68133; previous ACTA and disease aliases were checked against the [NCBI gene record](https://www.ncbi.nlm.nih.gov/gene/58) and [MedlinePlus Genetics](https://medlineplus.gov/genetics/gene/acta1/). Main baseline was `ef291d796fd8ca62db39b3549293d06e61c1004e`. Local review blob `3ae32010957cd680759886b5e3ded0359cd040ff` and the other five top-level source/render files matched GitHub's authoritative contents response. ACTA1-specific open-PR search found none; broader alias searching returned only an unrelated PSEPK PR.
- Audited all 51 existing entries: 50 seeded source assertions plus the already-proposed muscle alpha-actinin binding entry. Original term, evidence, reference, qualifier and supporting-entity fields are unchanged. No new process or additional annotation was introduced. All 38 references and four core functions were read. All 23 PMIDs cited in the YAML and notes have genuine existing publication caches.
- Publication caching ran alongside the research launch and confirmed 23/23 already cached. An initial offline tool-resolution failure was followed by one genuine online Falcon launch with the requested 1200-second timeout and Perplexity-lite fallback, using supported writable per-process uv directories. Both failed before provider execution because `deep-research-client` could not be resolved from PyPI (DNS after retries). There is no new provider report. The existing genuine Affinage report was read and preserved; primary evidence supplies the decisions.
- The local cache has 15 abstract-only PMID records. Their `full_text_unavailable: true` flags are now explicit even when an external original article was read. No publication, GOA, UniProt, provider or saved bioinformatics source was hand-edited.

### Primary recovery changed the stress-fiber judgment

PMID:15198992, Ilkovski et al., was retrieved as the original published paper from the [University of Geneva archive](https://access.archive-ouverte.unige.ch/access/metadata/91b5d40c-2de4-4ba3-9c5d-9dea570bbc60/download), DOI `10.1093/hmg/ddh185`. The successful normal curl download is `/tmp/ACTA1-PMID15198992.pdf`; `pdftotext -layout` produced `/tmp/ACTA1-PMID15198992.txt`. The web reader initially exposed the article but later timed out; the complete local PDF recovery resolved that limitation.

Results, journal page 1733, and Figure 5A show wild-type ACTA1-EGFP in C2C12 myoblast stress fibers: “stress-fibre or diffuse cytoplasmic staining”. Figure 5B(viii) and page 1734 show striated incorporation after differentiation. Thus both existing stress-fiber annotations are retained as `KEEP_AS_NON_CORE`, reflecting the observed culture context relative to mature sarcomeric function. Ectopic expression does not itself make a localization experiment IMP rather than IDA. The earlier abstract-based rejection and claim that stress-fiber incorporation was only mutant behavior were unsupported. Patient-muscle fractionation also supports the cytoskeleton and thin-filament assertions, while its insoluble fraction need not consist exclusively of normal sarcomeric filaments.

### Interaction evidence and the generic-binding policy

PMID:32814053 was retrieved as the [original full published article from the MDC repository](https://edoc.mdc-berlin.de/id/eprint/19322/1/19322oa.pdf), DOI `10.1016/j.celrep.2020.108050`. Genuine artifacts: `/tmp/ACTA1-PMID32814053.pdf` and `/tmp/ACTA1-PMID32814053.txt`. Results pages 2–4 report four independent screens, pairwise retesting and DULIP validation of a subset. The prior claim that three interaction-method labels established one experiment counted three times is withdrawn. This recovery does not establish whether any particular ACTA1 pair was included in the DULIP subset.

The seven source pairs (ZNF20, INCA1, ASCL4, LIAT1 isoform 4, PNMA5, SYNC and CAMK2A) remain intact. Their `GO:0005515` rows now use `REMOVE` because the term supplies no informative molecular function; the physical-interaction reports are not declared false. The same policy applies to the two ANXA8 BioPlex rows (PMID:28514442, PMID:33961781) and the genuine DNase I affinity-purification interaction (PMID:12849983). Neither a non-muscle cell line nor a hypothetical actin carry-over establishes contamination. Binding to DNase I does not by itself demonstrate inhibition, so no inhibitor activity is added.

PMID:18835984 differs because the exact gene-product assignment remains unresolved. The [original PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2583614/), Methods, preparation of actin-modified surfaces, specifies bovine-muscle actin. This positively supports the reported HBHA interaction with muscle actin but does not establish a direct human ACTA1 assay. Because the full source is available, the generic-binding specificity policy can be applied: the human IPI row is `REMOVE` solely for being uninformative, while its direct human attribution remains explicitly unresolved. This is not a declaration that the underlying binding is false, and no specific ACTA1 activity is invented. The zero-evidence assumption from the old abstract-only reading is replaced by the actual reagent provenance.

PMID:10958653 is left `UNVERIFIED` for its ACTA1-specific interaction interpretation: the cached abstract describes myotilin and alpha-actinin. UniProt's ACTA1 interaction statement alone does not demonstrate that curators deliberately omitted a reciprocal annotation. PMID:16501887 does explicitly identify ACTA1 among USP25m-associated proteins; no USP25 catalytic or proteolysis activity is transferred to its binding partner.

### Extracellular HDA assignments remain unresolved

The five original HDA records concern prostatic-secretions/urine exosomes (PMID:23533145), plasma microvesicles (PMID:22516433), tears (PMID:23580065), parotid exosomes (PMID:19199708), and trabecular-meshwork exosomes (PMID:21362503). Each is now `UNDECIDED`.

The main text was read for the three full-cache exosome studies. It points to supplementary protein lists; the ACTA1-specific protein/peptide entries were not recovered. The two remaining caches are abstract-only. Attempts to access PMC supplement material encountered browser gating, unavailable downloads or DNS failure. The parotid paper identifies supplementary tables 1 and 2, but the file contents were not inspected; an indexed file name is not peptide evidence. The trabecular-meshwork main list includes other actins, which neither proves nor disproves ACTA1 in the full list.

The preserved peptide analysis establishes that ACTA1 has both shared and distinguishing tryptic peptides. It does not identify which peptides were measured in any of these studies. Tissue enrichment, no classical secretion signal, and possible shared peptides are reasons to inspect source data, not grounds to overrule HDA curators. Likewise, absence of a distinguishing peptide in a future reanalysis would leave ambiguity rather than alone prove that ACTA1 was absent.

### Phylogenetic provenance and source compartment resolution

The cached PAINT table `interpro/panther/PTHR11937/PTHR11937-paint.tsv` was checked for the IBDs at PTN002631484, PTN000940351 and PTN000233075. PTNs are ancestral assertions, not irrelevant entries merely because they are not extant proteins. Their structured status now supports transfer, and IBA source_entities contain only the verified PTN proximate assertions; the extant evidence list remains in the unchanged underlying source records. ACTA1 appearing among experimental descendant sources is expected and is not circular. The retained structural-function IBD and its descendant loss annotations do not license an invented label for the entire clade. No acceptance decision is based on the number of extant donors.

No ACTA1/P68133 entry was found in the local GO-CAM index. The existing source-resolution JSON identifies pig skeletal-actin P68137, mouse Acta1 P68134 and chicken smooth-muscle ACTA2 P08023. The additional Ensembl protein token on the Compara row was preserved as `UNRESOLVED`: its exact cross-reference was not independently recovered, and it is not dismissed as “not a gene product”.

The cytoskeleton IEA now remains `ACCEPT` at the location-mapping source's resolution. The four cytosol TAS records from actual actin-myosin contractile events (R-HSA-390593, R-HSA-390595, R-HSA-390597, R-HSA-390598) also remain `ACCEPT` at the pathway's compartment resolution. The event names identify myosin or troponin chemistry, which is not attributed to actin. The four adhesion-context cytosol records (R-HSA-9914537, R-HSA-9934294, R-HSA-9934410, R-HSA-9934486) remain `KEEP_AS_NON_CORE`: the broad location is compatible, but generic actin-set participation does not establish an ACTA1-specific adhesion mechanism. Thus the differing cytosol actions reflect source context, not an allegation that the compartment is wrong or a rule that every duplicate must be demoted.

The five ISS rows from chicken ACTA2 (P08023) are `UNDECIDED`. PMID:10633868 expressly studies smooth-muscle alpha-actin in chick endocardial mesenchyme. Its source experiment is valid; conservation of these developmental/localization assertions in ACTA1 is unresolved. Independent annotation-reviewer consultation correctly identified that paralogy, tissue context and missing target-specific evidence do not alone demonstrate transfer failure. The recovered non-sarcomeric ACTA1 localization further argues against an absolute compartment-exclusion claim. An ISS may legitimately cross paralogs; positive evidence of conservation or target-specific divergence is needed to settle these rows. Mouse Acta1 developmental rows remain non-core; PMID:2731651 is expression analysis of an actin-gene-pair perturbation, not a targeted Acta1 knockout.

### Ontology and core chemistry

A live QuickGO JSON request succeeded on 2026-09-26; response saved as `/tmp/ACTA1-GO-terms.json`:

`https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0051371,GO:0044297,GO:0001725,GO:0003009,GO:0005200`

- `GO:0051371` muscle alpha-actinin binding: binding muscle actinin isoforms, including the Z-disc proteins. The already-existing specific-binding proposal is retained on the direct human muscle affinity result in PMID:16945537; no specific ACTN accession is guessed. Its 28% mutant biopsy composition limits interpretation of the ten-fold affinity change. Rabbit-derived UniProt contact regions are not independent human mapping experiments.
- `GO:0001725` describes a contractile actin-filament bundle with alternating polarity, cross-linking and periodic myosin. This is compatible with the reported myoblast stress fibers.
- `GO:0044297` describes the projection-bearing cell's body, excluding projections. Its listed projection types are examples, not a rule that only neurons can carry the term. The ACTA2 donor context is known, but transfer conservation remains unresolved.
- `GO:0003009` skeletal muscle contraction names force generation by the actin/myosin apparatus in skeletal muscle. The existing broad contraction row retains its `MODIFY` to this supported subtype; no absolute absence of ACTA1 from heart is asserted.
- `GO:0005200` describes contribution to cytoskeletal structural integrity, fitting the filament protomer.

PMID:24743229 was read in full. Its canonical biochemical control is endogenous pig skeletal-muscle alpha-actin (Methods), and Figure 6D compares phosphate release. The cached Results state: “As expected, α-actin showed an even lower release of phosphate in the Ca2+-bound compared to the Mg2+-bound form.” The paper cautions that phosphate release can lag ATP cleavage. This result-bearing support replaces the prior title-only core quote. Hydrolysis influences filament dynamics; oriented subunit polymerization establishes structural polarity. The actin ATPase is distinct from the myosin ATPase powering contraction. No claim is made that human ACTA1 kinetics have never been measured anywhere.

The description now includes dominant and recessive disease mechanisms, uses predominant skeletal-muscle expression rather than absolute tissue exclusion, and omits transferred PTM details from its core biological synopsis. PMID:23673617 centers on beta-actin/ALKBH4, and PMID:30626964 concerns SETD3-dependent actin modification; neither makes ACTA1 the modifying enzyme.

### Current action totals and verification

| Action | Entries |
|---|---:|
| ACCEPT | 20 |
| REMOVE | 11 |
| KEEP_AS_NON_CORE | 8 |
| UNDECIDED | 10 |
| MODIFY | 1 |
| NEW (retained prior proposal) | 1 |

Totals are 51 entries, including 50 unchanged source assertions. The ten UNDECIDED entries are the five extracellular HDA records and five ACTA2-source ISS transfers. All eleven generic-binding rows are removed for lack of functional information; the HBHA human-protein assignment remains unresolved in the source interpretation. All primary quotes were checked against the immutable cache; external full-text evidence is identified by source URL and section. The Figure 5A excerpt uses supporting_text_fulltext, separately checked against the genuine recovered PDF text and not represented as a cached-publication quote. Source comparison and trailing-space removal both assert parsed equality outside authored review fields. The old bioinformatics claim lint encodes earlier action counts and biological conclusions; it is preserved as historical tooling, not used to force the current review back to obsolete judgments.

Verification completed: `just validate human ACTA1` passed with two nonblocking warnings (source-specific cytosol action split and unused provider support). `just validate-history` passed for the newly scaffolded session, and `just render human ACTA1` succeeded. Independent annotation-reviewer consultation read all entries, four cores and 38 references; its two substantive provenance/transfer concerns were resolved and it reported no remaining biological blocker. No Git or remote mutation was performed.
