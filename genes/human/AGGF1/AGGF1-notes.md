# AGGF1 (Q8N302) — review notes

## The question this gene poses

The symbol *Angiogenic factor with G-patch and FHA domains 1* is a function claim
wrapped around two domain claims, and the three have to be adjudicated
separately. They come out differently:

| claim | verdict |
|---|---|
| **angiogenic factor** | supported by a large, mostly organismal literature — but that is a BP and a receptor-ligand MF, not what the rest of the protein does; and the human-genetic evidence that named it is now retracted in substance |
| **G-patch domain** | intact and canonical (8/8 conserved columns). The *derived* GO term `GO:0003676 nucleic acid binding` is nevertheless a domain-name mapping that no G-patch protein anywhere holds experimentally |
| **FHA domain** | every phosphothreonine-anchoring residue retained (G437-R438, S454, N478) — and **not one phosphopeptide has ever been measured**. Untested, not refuted |

## Domain architecture — an RNA-processing protein wearing a vascular name

From `AGGF1-uniprot.txt` (714 aa, PE 1: Evidence at protein level):

- `FT   COILED          18..88` — homodimerisation module
- OCRE domain (`DR   CDD; cd16164; OCRE_VG5Q`, `DR   InterPro; IPR041591; OCRE`,
  `DR   Pfam; PF17780; OCRE`) at ~residues 230–260, the Tyr-repeat module shared
  with the splicing regulators RBM5/RBM10
- `FT   DOMAIN          434..487` FHA
- residues 604–613 `FQRDDAPAS`, the mapped angiogenic motif (PMID:34551592) —
  note it sits in neither named domain
- `FT   DOMAIN          619..665` G-patch
- **no `FT   SIGNAL`** — secretion, if it happens, is non-classical

OCRE + FHA + G-patch is the architecture of a nuclear RNA-processing factor. The
angiogenic activity maps to a ten-residue linker motif between the two named
domains. That is the shape of the whole problem: the name attributes the
function to the domains, and the mapping says otherwise.

## The human genetics that named the gene does not hold up

This matters because it is the origin of every "angiogenic factor" framing, and
because UniProt still presents the variant as functional.

- Origin: [PMID:14961121 "One mutation is chromosomal translocation t(5;11), which increases VG5Q transcription. The second is mutation E133K identified in five KTS patients, but not in 200 matched controls."]
- Refuted: [PMID:16443853 "Nine (3.3%) of the controls carried the E133K sequence change, indicating that this variant has reached polymorphic frequency in population controls"] and, decisively, the one affected carrier inherited it from a healthy parent: [PMID:16443853 "One parent, who was clinically normal, also harboured the E133K mutation (fig 1C)."] Their conclusion: [PMID:16443853 "The findings bring into question the assertion that VG5Q, E133K is a mutation and that it causes KTS."]
- Independently refuted in a second population — the title says it:
  PMID:17103452, *"The G397A (E133K) change in the AGGF1 (VG5Q) gene is a single
  nucleotide polymorphism in the Spanish population."* (letter, no indexed
  abstract, body not retrievable; cited for its title claim only)
- The originating lab itself moved on: [PMID:18564129 "previously identified as a candidate susceptibility gene for KTS, but further"] In that paper's Discussion (full text not in the local cache, so not quoted here) they report E133K at P=0.59 between 163 cases and 465 controls and state it is unlikely to be associated with KTS.
- External databases agree: ClinVar VCV000402345 classifies
  `NM_018046.5(AGGF1):c.397G>A (p.Glu133Lys)` **Benign/Likely benign** (multiple
  submitters, no conflicts, last evaluated 2026-01-01); gnomAD v4 gives an overall
  **allele** frequency of ~1.4% (exomes AC 20,774 / AN 1,461,240), highest in
  Ashkenazi Jewish (~2.7%) and Non-Finnish European (~1.6%), and **lowest**, at
  ~0.27%, in African/African-American samples.

  **Provenance for those two figures**, which are the only quantities in this
  review with no script and no cached quote behind them: the gnomAD numbers were
  read from the gnomAD v4 GraphQL API for variant `5-77035624-G-A` (GRCh38) and
  cross-checked against Ensembl REST `/variation/human/rs34203073?pops=1`; the
  ClinVar classification from NCBI eutils `esummary` for `VCV000402345`. Neither
  is reproduced by a committed script — flagged here rather than left implicit.

  **Allele frequency is not carrier frequency**, and an earlier draft of the
  `description` conflated them. At AF = 0.0142 the carrier frequency is
  2·AF·(1−AF) = **2.8%**, which is what the primary source actually measured:
  Barker et al. found the change in **3.3%** of 275 controls (9/275 = 3.27%). The
  three numbers agree; the description now names the right one.

**Correction to report to UniProt.** `FT VARIANT 133 /note="E -> K (displays a
stronger angiogenic activity; dbSNP:rs34203073)"` presents a benign common
polymorphism as a functional disease variant. The *in vitro* CAM-assay difference
Tian et al. measured may well be real; the disease attribution is not.

**What this does and does not touch.** It does not refute the biochemistry —
purified AGGF1 promotes angiogenesis in the CAM assay, binds endothelial cells,
and drives proliferation regardless of what E133K means. It does mean that
"AGGF1 is the Klippel-Trenaunay gene" should not be stated flatly, and that no
GO annotation should be propagated from the KTS association.

## The G-patch: intact domain, unmeasured activity, misdirected GO term

Measured (see `AGGF1-bioinformatics/RESULTS.md`): AGGF1 matches **8/8** of the
columns conserved at ≥80% across 34 annotated G-patch domains in 33 reviewed
human proteins, including the invariant Gly at 631 and 639 (100% of the panel).

The InterPro2GO consequence is `GO:0003676 nucleic acid binding` from
`InterPro:IPR000467`. Querying the whole reference class settles what that term
is worth: **11 of 11 reviewed human G-patch proteins carry `GO:0003676` by IEA
and by nothing else; zero carry it with any experimental code; six carry
`GO:0003723 RNA binding` (or a child) experimentally.** The term is the
mapping's uniform output, not anybody's finding — and where it has been tested,
the answer is the child term.

This is reinforced by what G-patch domains are now understood to be. The
crystal structure of DHX15 bound to the NKRF G-patch shows the motif tethering
the helicase's catalytic core to its flexibly attached C-terminal domains:
[PMID:32179686 "conformation across the helicase surface. It tethers the catalytic core to the"]
and [PMID:32179686 "ATPase activity of DHX15 are increased when G-patch is bound."]
It is a helicase-activation peptide, not an autonomous nucleic-acid-binding
module.

For AGGF1 specifically, RNA binding *has* been measured directly — RNA
immunoprecipitation against NEAT1 in human cells, [PMID:35608889 "AGGF1 interacts with NEAT1, which may be another possible mechanism underlying"] So the IEA's conclusion survives on
independent grounds, at the more informative term. Hence MODIFY rather than
REMOVE.

**Helicase cofactor status, stated carefully.** GOA carries an AGGF1–DHX15
interaction, and DHX15 is *the* canonical G-patch client. But the evidence is a
single HuRI Y2H (PMID:32296183) logged as three sub-methods; a peer-reviewed 2026
survey of the family still lists AGGF1's interacting helicase as **Unknown**
(PMID:42052570, Table 3). A bioRxiv preprint posted 2026-06-30
(doi:10.64898/2026.06.30.735655, Memet et al.) reports that AGGF1's isolated
G-patch stimulates DHX15 ATPase and tightens its RNA binding — **unrefereed, no
PMID, and therefore not used as evidence anywhere in this review.** Recorded as a
watch item and as a suggested experiment.

## The FHA: every anchor residue retained, no phosphopeptide ever tested

Anchors from CHEK2 and Rad53 FHA1, verified against the live sequences and
transferred by domain-local alignment, all land inside AGGF1's annotated FHA:
**G437, R438, S454, N478**. The two anchor sets agree exactly wherever both
resolve. (A first attempt aligned full-length sequences globally and mapped every
CHEK2 anchor into AGGF1 residues 112–169 — a clean-looking "the FHA is
degenerate" result that was pure alignment noise. The script now refuses to align
anything but the domain windows, and the docstring records why.)

The mutational data point at the same surface. PMID:33069768 tested six COSMIC
somatic FHA variants: **G437E**, Q467H, Y469N and N483T impair AGGF1's
tumour-suppressor activity, while **R447Q and V497I do not**. G437 is the
conserved Gly of the pThr-anchoring G-R pair; R447 is *not* the conserved Arg
(that is R438) and V497 lies outside the 434–487 core.

And yet: **no phosphopeptide, phosphothreonine or phospho-dependence experiment
on AGGF1's FHA exists.** Both published FHA functions are plain co-IP with
deletion constructs —

- p53: [PMID:33069768 "amino acids 434 and 509 is the FHA domain of AGGF1. Co-IP showed that the AGGF1"]
- 14-3-3α/β: [PMID:33471274 "localization. The distribution of AGGF1 in cytoplasm needs both FHA domain and"]

— neither with a phosphatase control, a phospho-site mutant, or peptide
competition. There is also no experimental structure of any part of human AGGF1
(Q8N302 carries zero PDB cross-references). So **no phosphoprotein-binding term
is proposed**; the hypothesis is filed as an experiment.

Worth flagging as odd: 14-3-3 is itself the canonical pSer/pThr reader, so "FHA
domain binds 14-3-3" is a mechanistically unusual claim in exactly the direction
that a phosphatase control would test.

## The nucleus is missing from GOA entirely

AGGF1's GOA localisation record is cytoplasm (×2), extracellular region (×3) and
perinuclear region of cytoplasm (×1). There is **no nucleus annotation at all**,
against three independent lines:

1. [PMID:35608889 "and PSF. Here, we show that AGGF1 is a key regulatory and structural component"]
2. [PMID:33471274 "Angiogenic factor with G-patch and FHA domains 1 (AGGF1) exhibits a dynamic"] — headed by Tian XL, the first author of the 2004 discovery paper, so a different group but the same lineage; maps an NLS to residues 260–288
3. AGGF1's own interaction record: three of the four HuRI partners — DHX15, MCRS1 and FBXO28 — carry
   `GO:0005634` nucleus with experimental evidence (EXP or IDA), while the
   fourth, MAB21L3, has **no** cellular-component annotation in GOA at all and
   no UniProt `SUBCELLULAR LOCATION` comment; and AGGF1 was included as a
   spliceosome-associated protein in the Hegele 2012 Y2H matrix (PMID:22365833)

The interaction rows in AGGF1's own GO record already point at the nucleus while
its localisation rows do not.

## Is "secreted" solid?

Yes, on more than one lab's data, and worth stating because there is no signal
peptide. Tian 2004 used competitive ELISA on matrigel-culture media from
untransfected HUVECs plus ³⁵S metabolic labelling, and was explicit about the
route: [PMID:14961121 "The molecular mechanisms for trafficking and secretion of VG5Q remain to be established; however, it may be released via a non-classical secretory pathway similar to the angiogenic factor FGF-2"]. Independently, AGGF1 protein is measurable in human vitreous fluid
(PMID:39905000), and purified extracellular AGGF1 engages a cell-surface
receptor (PMID:34551592). The extracellular rows stand; the *mechanism* of export
is still unknown, which is a legitimate ontology-free gap rather than a
curation error.

## Per-partner judgements on the binding rows

Nine `GO:0005515` rows and three `GO:0042802` rows, from seven partners. They do
not all deserve the same verdict (`AGGF1-bioinformatics/RESULTS.md` §4):

- **TNFSF12 / TWEAK** — the strongest. Three orthogonal assays in the original
  paper (Y2H, GST pull-down, co-IP) and an independent co-IP 21 years later in
  human retinal endothelial cells (PMID:39905000). MODIFY to
  `GO:0019955 cytokine binding`. `GO:0043120 tumor necrosis factor binding` was
  considered and rejected on its definition, which names TNF specifically as a
  cytokine produced by monocytes and macrophages — that does not cover TNFSF12 —
  even though GO places `GO:0038057 TNFSF11 binding` beneath it. That
  inconsistency, and the missing `TNFSF12 binding` term, are raised separately.
- **DHX15** — one Y2H screen, but it is the single most mechanistically predicted
  partner a G-patch protein can have. MODIFY to `GO:0017151 DEAD/H-box RNA
  helicase binding`: the same fact, stated informatively, with no new claim about
  activity.
- **MAB21L3, BLOC1S6** — two independent methods each; kept non-core, nothing more
  specific sayable.
- **MCRS1, FBXO28** — single HuRI Y2H each; kept non-core. Both nuclear, which is
  the only reason they are not over-annotation calls: they cohere with the
  nuclear evidence the rest of the record ignores.
- **self-interaction** — two of the three rows are real (independent Y2H screens,
  and a 70-residue coiled coil to explain them). The third, from the BioID screen,
  is an artefact: IntAct gives AGGF1 `experimentalRoleA=bait` in all 635 proximity
  records, and a BirA*-fusion bait biotinylates itself whether or not it dimerises.

## A live contradiction in the literature worth flagging to curators

Two co-IP-based papers disagree on the *direction* of AGGF1's effect on the
TWEAK–Fn14 axis:

- [PMID:36696895 "factor-like weak inducer of apoptosis), which reduces interaction between TWEAK"]
- [PMID:39905000 "Our results revealed that the binding of TNFSF12 to FN14 diminished when AGGF1 was silenced"]

i.e. AGGF1 blocks TWEAK–Fn14 in atrophic muscle and promotes it in retinal
endothelium. Both may be context-specific; neither is currently annotated. No GO
term is proposed for either until it is resolved.

## One laboratory has done almost all of this work

Raised by the PR reviewer and then measured rather than argued
(`AGGF1-bioinformatics/lab_independence.py`, which reads the senior author out of
each cached record):

| senior author | papers |
|---|---|
| **Wang Q / Wang QK** | **11 of 13** — 14961121, 33069768, 35608889, 34551592, 27513923, 27522498, 40035560, 23197652, 24277077, 35202649, 37081014 |
| Tian XL | 1 — 33471274; Tian XL is the **first author of the discovery paper**, so a separate group but the same lineage |
| Chen L | 1 — **39905000**, the only genuinely independent group |

One caveat, measured rather than asserted (`lab_independence.py` reports it):
**Xu C appears on PMID:39905000 and on 8 of the dominant group's 11 papers.** A
shared surname-plus-initial is not proof of the same person, the senior author
differs, and PMID:39905000's affiliations are a different institution — so the
paper is still counted as independent. The overlap is recorded rather than hidden
because "one independent replication" is load-bearing here.

This matters for how the review is worded, not for any action. An earlier draft
credited the nucleus evidence to more distinct laboratories than the author lists
support, and hedged the paraspeckle paper by anchoring the nucleus proposal on
PMID:33069768 "instead" — but that paper has the **same senior author**, so the
hedge was empty. Both statements are withdrawn. (The retracted wording is
paraphrased rather than quoted here on purpose: `audit_claims.py` greps for it,
and a guard that has to tell a retraction apart from a report of one is a guard
that will eventually let the claim back in.)

The useful version: AGGF1's mechanistic literature is essentially one group's
programme, and **PMID:39905000 is the single substantive independent replication**
— which is exactly why the review leans on it for the TNFSF12 interaction and for
the extracellular pool. Independent replication of the paraspeckle and splicing
results is the most valuable thing anyone could do for this gene's annotation.

A review that collapses `NbExp` into independent experiments and catches a
bait-labelling artefact has no business asserting laboratory independence it never
checked. The check is now committed so the claim stays a measurement.

## Process notes

- **affinage** returned 25 citations, all numeric PMIDs, trust gates clear. Its
  recall was good on the vascular/mechanistic literature but it **missed both
  halves of the two most decisive lines**: the entire E133K refutation literature
  (PMID:16443853, PMID:17103452, PMID:18564129) and the FHA/14-3-3
  nucleocytoplasmic-transport paper (PMID:33471274) — which is titled *"FHA
  domain of AGGF1 is essential for its nucleocytoplasmic transport and
  angiogenesis"*, i.e. exactly on topic. Neither is in GOA either. Consistent
  with the campaign's measurement that the gates certify precision, not recall.
- **Erratum sweep**: 22 PMIDs checked; PMID:39251607 and PMID:40205054 both carry
  errata (PMID:39468017, PMID:41039152). Scope established by reading each
  correction: a missing author affiliation and a Methods-equation subscript typo
  respectively. Neither affects any evidence used here.
- **Row reconciliation**: `AGGF1-goa.tsv` has 24 data rows; the `fetch-gene` stub
  seeded **24** `existing_annotations`, one per row, with per-partner WITH/FROM
  preserved. No collapse this time. The review adds 9 `NEW` entries on top,
  giving 33; `AGGF1-bioinformatics/reconcile_goa.py` asserts the reconciliation
  on the full (term, evidence, reference, WITH/FROM) key rather than on row
  counts, and that every extra entry is `action: NEW`.
- **Not confirmed**, and said so: the predicted
  `PSEUDOENZYME_OVERANNOTATION` pattern does not apply — AGGF1 has no catalytic
  MF term in GOA at all, so there was nothing to argue against. The name-derived
  over-reach here is a *binding* term.
