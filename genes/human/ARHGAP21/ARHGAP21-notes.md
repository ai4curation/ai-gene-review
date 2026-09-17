# ARHGAP21 (Q5T5U3) — review notes

Human Rho GTPase-activating protein 21, 1958 aa, HGNC:23725, chromosome 10p12.

## 1. Nomenclature: this gene used to be called ARHGAP10, and ARHGAP10 is now a different gene

The two founding papers, and several later ones, call this protein **ARHGAP10**
[PMID:12056806 "We have identified a novel human gene, termed ARHGAP10, that codes for a 1957-aminoacid Rho-GAP, containing a PDZ, a PH, and a Rho-GAP domain."].
UniProt still lists `ARHGAP10` as a synonym of `ARHGAP21`. HGNC has since assigned the
symbol **ARHGAP10** to a *different* gene (UniProt `A1A4S6`, a GRAF/oligophrenin-family
protein). The later literature flags the collision explicitly
[PMID:20525016 "ARF1 also regulates Cdc42 function by binding the Cdc42-specific GAP ARHGAP21 (also referred to as ARHGAP10) (23, 24)."].

**Checked, and clean.** `reference_coverage.py` queries QuickGO *by reference* for every
primary paper and asks whether any annotation landed on `A1A4S6`. None did. The
`PMID:15793564` and `PMID:16184169` annotations sit on `Q5T5U3` (and, for the latter, on
`P35221` CTNNA1), which is correct. Recording the negative so the next reviewer knows the
check was run rather than skipped.

ARHGAP10/`A1A4S6` is also **not** a member of ARHGAP21's PANTHER family (see §6), so it is
not a paralog in the phylogenetic sense either — only a symbol collision.

## 2. Domain architecture — there is no ArfGAP domain

UniProt's feature table gives exactly three domains
[file:human/ARHGAP21/ARHGAP21-uniprot.txt "FT   DOMAIN          1147..1339"]:

| domain | residues | role |
|---|---|---|
| PDZ | 50–159 | binds PDZ-binding motifs (§5) |
| PH | 931–1040 | part of the ARF-binding domain |
| Rho-GAP | 1147–1339 | catalytic |

plus two mapped interaction regions: **930–1097 "Interaction with ARF1 and ARF6"**
(`ECO:0000269|PubMed:15793564`) and **1592–1861 "Interaction with CTNNA1"**
(`ECO:0000269|PubMed:16184169`).

The 930–1097 region is an **ARF-*binding*** domain (the authors' "ArfBD"), not an ArfGAP
domain. The crystal structure resolves it as a PH domain plus a C-terminal helix
[PMID:17347647 "We show that ArfBD comprises a PH domain adjoining a C-terminal alpha helix, and that ARF1 interacts with both of these structural motifs through its switch regions and triggers structural rearrangement of the PH domain."].
An independent ARF6 study classifies ARHGAP21 as an **effector**, explicitly contrasting it
with the Arf GAPs in the same experiment
[PMID:16527809 "We also found that the tandem mutation Q37E/S38I prevented the binding of two Arf GAPs, but not the effector ARHGAP10, and blocked the formation of membrane protrusion and actin reorganization."].

So ARHGAP21 is a **Rho-family GAP that is an ARF effector**, not a dual-specificity
Rho/ARF GAP. This matters because the name-implied-catalysis error (a GAP term inferred
from a domain or region name that was never assayed) is the commonest defect class in this
campaign — here GOA has *not* made it: there is no ARF-GAP annotation on the gene.

## 3. The catalytic machinery is not in dispute

The arginine finger is R1184, and UniProt records the mutagenesis as
`R->A: Loss of GTPase activity and loss of function.` with evidence from **both** founding
papers (`ECO:0000269|PubMed:15793564, ECO:0000269|PubMed:16184169`). Both groups
independently built the same catalytically-dead mutant and both saw loss of function.

That is the key framing for §4: the disagreement is about **which GTPase**, never about
whether ARHGAP21 is a GAP.

## 4. Substrate specificity is genuinely contested — and GO cannot express the disagreement

### 4a. What the papers actually say

| paper | system | reported substrate(s) |
|---|---|---|
| Dubois 2005 [PMID:15793564] | in vitro GAP assay; Golgi | Cdc42 "preferentially" |
| Sousa 2005 [PMID:16184169] | in vitro GAP assay; adherens junctions | **RhoA and Cdc42** |
| Klein 2006 [PMID:16527809] | ARF6 cycle | (effector, not substrate) |
| Hehnly 2010 [PMID:20525016] | Golgi repositioning | Cdc42 ("Cdc42-specific") |
| Anthony 2011 [PMID:21173159] | AT1AR / stress fibres | **RhoA** |
| Barcellos 2013 [PMID:23235160] | cell–cell junctions, EMT | Cdc42 ("particularly") |
| Lazarini 2013 [PMID:23200924] | PC3 prostate cells | **RhoA and RhoC** |
| Rodrigues 2017 [PMID:29212046] | mouse haematopoiesis | **RhoC** |

Verbatim anchors:
[PMID:15793564 "We show that ARHGAP10 functions preferentially as a GAP for Cdc42 and"],
[PMID:16184169 "The GAP domain of ARHGAP10 has GAP activity for RhoA and Cdc42."],
[PMID:23200924 "In PC3 cells, ARHGAP21 presented GAP activity for RhoA and RhoC and induced changes in cell morphology."],
[PMID:23235160 "ARHGAP21 is a negative regulator of Rho-GTPases, particularly Cdc42."].

**The dispute is narrower than "RhoA vs Cdc42".** Both 2005 papers agree ARHGAP21 has
Cdc42 GAP activity; Dubois says Cdc42 is *preferred* (not exclusive), Sousa says RhoA is
*also* a substrate. What is genuinely unresolved is (i) the rank order of preference and
(ii) whether the RhoA/RhoC activity is constitutive or context-restricted. Lazarini's own
data argue for context: the same protein showed the activity in PC3 but the phenotype was
absent in LNCaP. UniProt records both without adjudicating
[file:human/ARHGAP21/ARHGAP21-uniprot.txt "CC   -!- FUNCTION: Functions as a GTPase-activating protein (GAP) for RHOA and"].

**I have not collapsed this into one verdict, and the review should not either.**

### 4b. GO cannot record which GTPase — measured, not assumed

`check_gap_terms.py` resolves each historical substrate-specific GAP term through QuickGO's
`/complete` endpoint (the only endpoint that distinguishes a **merged** id from an **absent**
one — OLS reports both identically):

| requested | resolves to |
|---|---|
| `GO:0005099` Ras GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0005100` Rho GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0008060` ARF GTPase activator activity | **MERGED** → `GO:0005096` |
| `GO:0005097` Rab GTPase activator activity | **MERGED** → `GO:0005096` |

and `GO:0005096` has **zero `is_a` children** (its only child is `GO:1902773 GTPase
activator complex`, via `capable_of`).

So `GO:0005096` is **already maximal**: there is no more specific term to move to, and
per the campaign's standing rule I am **not** filing a `proposed_new_terms` entry to
re-create what GO deliberately merged. The consequence is recorded as a `KnowledgeGap`
instead: *the substrate identity of a GAP is not expressible in the GO molecular-function
branch at all.* The machine-readable alternative is `core_functions[].substrates` plus a
`has_input` (`RO:0002233`) extension on the annotation, which is what this review uses.

The same merge applies on the binding side: `GO:0017137` (Rab) and `GO:0017048` (Rho)
GTPase binding both resolve to `GO:0031267 small GTPase binding`.

### 4c. The GO record is silent on RhoA/RhoC for a second, independent reason

`reference_coverage.py` (QuickGO by reference) shows that **every** paper reporting RhoA or
RhoC activity — `PMID:16184169`, `PMID:21173159`, `PMID:23200924`, `PMID:29212046` —
produced **zero** GO annotations anywhere in GOA. So even setting the ontology gap aside,
the RhoA/RhoC half of the literature was never curated.

Note the precision this needs: because `GO:0005096` is substrate-agnostic, GOA does **not**
assert "Cdc42" either. GO says only "this is a GAP". The disagreement is invisible in GO
twice over — once because the term cannot carry a substrate, and once because the papers on
one side of it were never read into GOA.

## 5. The PDZ domain is a validated PDZ-binding-motif receptor, and GO has no term for that side

Ten of the 24 `GO:0005515` rows come from one paper, `PMID:36115835` (Gogl 2022), a
systematic PDZ-domain / PDZ-binding-motif affinity survey
[PMID:36115835 "Here, we measure the affinities of 65,000 interactions involving PDZ "].
Its full text **never names ARHGAP21** (0 occurrences of the string `ARHGAP` in 302 kB), so
"these rows measure the PDZ domain" had to be checked rather than assumed.

`intact_methods.py` checks it against IntAct's recorded participant ranges: all ten
`holdup assay` rows map onto residues **50–159**, i.e. the PDZ domain. Five of the ten
(AXIN1, APC, CTNNB1, MYO18A, SAPCD1) additionally carry an orthogonal `anti tag coip` row
from a different publication, so they are not single-method hits.

**But there is no GO term for this.** A QuickGO full-text search over GO returns exactly two
PDZ terms, one of them obsolete; the survivor is `GO:0030165`, defined as
*"Binding to a PDZ domain of a protein"* — the **ligand** side, for proteins that carry a
PBM and bind someone else's PDZ. It has no descendants. ARHGAP21 is on the opposite side of
that interaction, and GO offers nothing for it.

This is why these ten rows cannot be upgraded to something informative and are removed as
uninformative generic binding rather than modified. Removal does not mean the interactions
are false — recorded as a second `KnowledgeGap`.

## 6. Provenance checks

### 6a. All seven IBA rows are self-referential — which is correct, not circular

Every IBA row's WITH/FROM is `PANTHER:PTN…|UniProtKB:Q5T5U3`, i.e. the PANTHER ancestral
node plus **ARHGAP21's own accession**. Per the PAINT convention this marks a curator
judging the function core on the strength of the target's own experimental annotation; it
is `NO_FAILURE_CORE`, never `CIRCULAR_OR_REDUNDANT`.

Two distinct nodes are involved:

- `PTN008592632` → `GO:0005096` (the GAP activity)
- `PTN002754039` → the six Golgi / actin / junction / microtubule-transport terms

### 6b. PANTHER family

`PTHR23175` ("PDZ domain-containing protein"), **5182 proteins**, of which **7 are
reviewed (Swiss-Prot)** — the row count of the cached entries CSV is the Swiss-Prot subset,
not the family. Those seven are ARHGAP21 (human, mouse, *X. tropicalis*, two *X. laevis*)
in subfamily **SF16**, and ARHGAP23 (human `Q9P227`, mouse `Q69ZH9`) in **SF5**.

So **ARHGAP23 is the genuine close paralog** and it sits in a different subfamily.
ARHGAP10 (`A1A4S6`) is absent from the family entirely (§1).

### 6c. The one non-human WITH/FROM accession is harmless

`resolve_partners.py` resolves all 15 distinct WITH/FROM accessions: 0 dead, 0 TrEMBL, 15
reviewed Swiss-Prot, 3 non-human (mouse Arf1 `P84078`; HPV16 and HPV18 E6).

UniProt flags `P84078` `Xeno`, which would normally mean an `IPI` row asserts a
cross-species interaction. Here it does not matter: human ARF1 (`P84077`) and mouse Arf1
(`P84078`) are **sequence-identical**, both 181 aa (checked by fetching both FASTA records
and comparing). So the accession choice is bookkeeping, not a biological defect. Negative
result, recorded.

### 6d. Retractions and errata

`check_corrections.py` reads `CommentsCorrectionsList/RefType` off each cited article's own
PubMed record — the only way a Publisher Correction is discoverable, since a
publication-type query cannot see one. All 30 cited PMIDs returned; **one** flag:
`PMID:36115835` → `PMID:36477203`, an Author Correction whose scope is
*"errors in Fig. 2, Fig. 4 and Fig. 5"* consisting of missing PCC values, axis labels,
legends and panel ordering. **Cosmetic; no data changed**, so the ARHGAP21 interactions it
reports stand. No retractions anywhere.

The checker was mutation-tested by inserting `PMID:32125225` (a known retracted paper),
which it correctly flagged `retracted_by_pubtype=True` with `RetractionIn: PMID:35078223`.

### 6e. Interaction evidence quality per partner

From `intact_methods.py` (502 IntAct rows, 440 distinct partners):

- **YWHAZ** — 5 rows, **4 distinct publications**, 3 orthogonal methods (`anti tag coip`,
  `proximity-dependent biotin identification`, `pull down`). This is real replication, not
  one screen logged several ways.
- **SFN** — 4 rows, 2 publications, BioID + TAP.
- **ARF1** — 3 rows, methods `cosedimentation` and **`x-ray diffraction`**, mapped to the
  **PH** domain. That is the 2.1 Å structure; the strongest single interaction datum on the
  gene.
- The ten PDZ holdup partners — see §5.
- **EEF1D** — `display technology` + `tap` only, no domain mapping; the weakest row.

14-3-3 binding across four independent papers is consistent with the gene's heavy
phosphorylation (UniProt lists ~20 phosphoserine sites), and is the one generic-binding
cluster that supports a specific replacement term, `GO:0071889 14-3-3 protein binding`.

## 7. Coverage, not over-annotation, is this gene's problem

`reference_coverage.py`, per primary paper (none of the ten is truncated, so these counts
are complete):

| PMID | annotations in all of GOA | on ARHGAP21 |
|---|---|---|
| 15793564 Dubois 2005 | 1 | `GO:0005096` IDA |
| 16184169 Sousa 2005 | 2 | **0** (both on CTNNA1) |
| 16527809 Klein 2006 | 0 | 0 |
| 17347647 Ménétrey 2007 | 2 | `GO:0005515` IPI |
| 20525016 Hehnly 2010 | 12 | 5 rows |
| 21173159 Anthony 2011 | 0 | 0 |
| 22922005 Bigarella 2012 | 0 | 0 |
| 23200924 Lazarini 2013 | 0 | 0 |
| 23235160 Barcellos 2013 | 0 | 0 |
| 29212046 Rodrigues 2017 | 0 | 0 |

**Seven of ten primary papers produced no GO annotation anywhere.** ARHGAP21's entire GO
record rests on three papers, and a 2.1 Å crystal structure is recorded as bare
`protein binding`.

The single largest gap is `PMID:16184169` — a *Nature Cell Biology* paper whose title
finding is that ARHGAP21 is required for α-catenin recruitment at adherens junctions. It
produced two annotations, **both on α-catenin**, none on ARHGAP21, even though UniProt
carries the interaction with a mapped region (1592–1861) and states it in FUNCTION and
SUBUNIT. Hence three `NEW` rows in this review:

- `GO:0045294` **alpha-catenin binding** (IPI) — verified active, defined
  *"Binding to catenin complex alpha subunit."*
- `GO:0034333` **adherens junction assembly** (IMP)
- `GO:0032956` **regulation of actin cytoskeleton organization** (IMP) — the Dubois
  Arp2/3-and-F-actin finding likewise has no BP term on the gene.

Affinage's record (`gates_passed: true`) returned 15 citations and **missed both founding
2005 papers** and Hehnly 2010 — i.e. it missed every paper that actually carries a GOA row,
plus the α-catenin paper that drives the largest gap here. Consistent with the campaign
finding that the gates certify precision and say nothing about recall; the α-catenin paper
is titled for the *partner* and for *Listeria*, which is exactly the shape that gets missed.

### 6f. Sibling cross-check on `GO:0005096` — no divergence

The campaign has seen three independently-reviewed paralogs give three different
answers to a byte-identical row, so sibling reviews are checked before finalising.
The repository has no other ARHGAP review, but it does hold three reviewed GAPs of
a different family (ACAP1, ACAP2, ACAP3) carrying seven `GO:0005096` rows between
them. **All seven are `ACCEPT`**, which is what this review does with its three.
No inconsistency to flag — recorded because a negative cross-check is still a
result.

## 8. Things I could not resolve

- **Rank order of GAP preference.** No study has assayed Cdc42, RhoA and RhoC side by side
  with the same purified protein and the same assay. The 2005 in-vitro comparisons used
  different constructs and readouts.
- **Whether the RhoA/RhoC activity is context-restricted.** Lazarini's PC3-vs-LNCaP split
  is suggestive but is a single paper with a cell-line comparison, not a mechanism.
- **The PDZ ligand in cells.** The holdup survey gives affinities for isolated fragments;
  which PBM ARHGAP21's PDZ engages *in vivo*, and in which compartment, is untested.
- **The cell system of the α-catenin knockdowns.** `PMID:16184169` and `PMID:23235160` are
  both abstract-only in the cache, neither abstract names a cell line, and `PMID:16184169`
  is absent from PMC and Europe PMC full text with no text-mined annotations. An
  experimental evidence code asserts the experiment was done in the annotated organism, so
  this matters: the two `IMP` NEW rows keep that code because the two-hybrid partner is
  human α-catenin and the target is human ARHGAP21, but both rows now carry an explicit
  caveat asking a curator with full-text access to confirm the cell line. An earlier draft
  asserted "in human cells" in the summary; that claim could not be verified and was removed.
- `GO:0051645 Golgi localization` appears in UniProt's GO cross-references as
  `IBA:GO_Central` but is absent from the GOA TSV, which instead carries `GO:0051683` and
  `GO:0051684`. Not acted on — it is a cross-reference snapshot difference, not an
  annotation this review can change.

## 9. Scripts

All committed under `ARHGAP21-bioinformatics/` and rerunnable
(`uv run --with requests python <script>`):

| script | output | question |
|---|---|---|
| `resolve_partners.py` | `partners.json` | who is every WITH/FROM and IPI accession |
| `check_corrections.py` | `corrections.json` | retraction / erratum / EoC on every cited PMID |
| `check_gap_terms.py` | `gap_terms.json` | can GO express GAP substrate specificity |
| `reference_coverage.py` | `reference_coverage.json` | what did each paper produce in GOA; symbol collision |
| `intact_methods.py` | `intact_methods.json` | per-partner method, publication count, domain mapping |
