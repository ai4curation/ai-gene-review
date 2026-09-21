# ARHGEF18 / p114RhoGEF — curation notes

Journal for the PAINT-campaign review of human ARHGEF18 (UniProt Q6ZSZ5, HGNC:17090).

## Deep-research provider

`affinage` (human-only), run 2026-09-19 against the 2026-06-09 Affinage record.
Blocking trust gates (accession match, human organism) passed; the soft gate tripped —
Affinage's own head-to-head self-evaluation scored this record `pairwise = tie` rather
than `win` against the curated UniProt reference. Recorded in
`references[].reference_review` for `file:human/ARHGEF18/ARHGEF18-deep-research-affinage.md`.

A clean gate is a precision claim, and that is how it behaved here: every PMID Affinage
returned resolves to a real paper about this gene. Its recall was the problem.

### What the provider missed, and why

| missed paper | what it decides | why a symbol search misses it |
|---|---|---|
| PMID:11085924 Blomquist 2000 | the **founding in-vitro exchange assay**; RhoA yes, Rac1 and Cdc42 no | title names the *function* ("a novel Rho-specific guanine nucleotide exchange factor"), never the gene |
| PMID:15558029 Nagata & Inagaki 2005 | the source of UniProt's AltName **SA-RhoGEF**; SEPT9b binds and *inhibits* it | title names the **partner** (Sept9b) |
| PMID:29876405 Chen 2018 | **1.4 Å structure of the p114RhoGEF PH domain bound to RhoA** (PDB 6BCB) | title names the **family** ("Lbc family of RhoGEFs") |
| PMID:23493395 Medina 2013 | activated RhoA binds the PH domains of all seven Lbc RhoGEFs — positive feedback | title names the **family** |
| PMID:28536193 Schell 2017 | EPB41L5 binds and recruits ARHGEF18 in podocytes | title names a **different protein**, and the abstract **misspells the gene as "ARGHEF18"** |
| PMID:36912772 Safavian 2023 | SEPTIN9 binds and activates ARHGEF18 at the ciliary base | title names the **partner** ("Septin-mediated") |
| PMID:31409654 Silver 2019 | *Drosophila* ortholog **Cysts** recruited by Crumbs/Bazooka, activates Rho1 | title names the **fly gene** |

Both of the first two are in UniProt's own `RN` list, which is why reading it is not
optional. The Schell case is the misspelling trap in its purest form: the sentence in
PubMed reads "by binding and recruiting the RhoGEF ARGHEF18 to the leading edge".

Free-supplementary check: PMID:11085924 is free at PMC1221462 and its abstract carries
the decisive substrate sentence, so the paywall on the Circ Res paper (PMID:14512443,
no free route found) does not block the comparison.

## The substrate disagreement

Two primary papers, both cited by UniProt, disagree:

- PMID:11085924 — "p114-Rho-GEF interacted specifically with RhoA, in its nucleotide-free
  and guanosine 5'-[gamma-thio]triphosphate-bound states, but not with Rac1 and Cdc42,
  and efficiently catalysed guanine nucleotide exchange of RhoA" (purified protein).
- PMID:14512443 — "we have determined that p114RhoGEF activated RhoA and Rac1 but not
  Cdc42 proteins" (in-cell pull-down plus dominant-negative GTPases).

A third, independent in-cell result sides with Blomquist: PMID:21258369 — "depletion of
p114RhoGEF resulted in reduced levels of active RhoA in HCE cells without significantly
affecting Rac and Cdc42". Both papers agree on Cdc42 (no).

UniProt carries both, and so should we. The sequence analysis in
`ARHGEF18-bioinformatics/` was run to see whether residues could arbitrate; they cannot
(see RESULTS.md §1.3). The one systematic Dbl-family exchange-kinetics panel does not
include p114RhoGEF, so the disagreement has never been retested with modern methods.

## What GO can and cannot say

Checked across three independent services (QuickGO, OLS4, the GO API) because QuickGO
silently resolves merges and cannot be read at face value in either direction:

- `GO:0005089` **Rho guanyl-nucleotide exchange factor activity** is obsolete,
  `term replaced by GO:0005085`, obsolescence reason `IAO:0000227` (terms merged).
- The same is true of `GO:0030676` (Rac), `GO:0005088` (Ras), `GO:0005086` (ARF),
  `GO:0017112` (Rab) and `GO:0005087` (Ran). **Every substrate-specific GEF activity term
  has been merged into `GO:0005085`, which now has zero `is_a` children** (QuickGO returns
  two children, both via `negatively_regulates` and `capable_of`; OLS4 returns none).
- `GO:0017048` **Rho GTPase binding** is likewise merged into `GO:0031267` small GTPase
  binding, which also has zero children in both services.

This is the same decision GO made for the RhoGAPs (all merged into `GO:0005096`). So the
answer to "which GTPase" is inexpressible in the molecular-function branch by design, and
proposing a replacement would be asking GO to undo a deliberate merge. Substrate identity
is carried instead in `core_functions[].substrates` and the limitation is recorded as an
`ONTOLOGY` knowledge gap.

The biological-process branch is only slightly better: `GO:0035023` retains `is_a`
children (`GO:0035024`, `GO:0035025`, and — asymmetrically — `GO:0032489` regulation of
Cdc42 protein signal transduction), but `GO:0035025` positive regulation of Rho protein
signal transduction has none, so there is no RhoA-specific or Rac1-specific process term
either. What GO *can* express and GOA does not is the **direction**: this protein is a
GEF and every primary paper shows activation, so `GO:0035025` rather than the
sign-agnostic `GO:0035023`. UniProt itself already phrases the RP78 variant effect as
"decreased function in positive regulation of Rho protein signal transduction".

## Disease and tissue, kept separate from molecular function

RP78 (MIM:617433, autosomal recessive adult-onset retinal degeneration) is caused by
biallelic ARHGEF18 variants (PMID:28132693). That is a *phenotype*, and it does not by
itself license any molecular-function or process annotation. The one thing in that paper
that does bear on function is the missense allele: "the p.Thr270Ala missense variant
affects a highly conserved residue in the DBL homology domain, which is required for the
interaction and activation of RHOA". UniProt records it as `VARIANT 458 T->A`.

The tissue work likewise stays attributed to its system:

- **epithelia** (Caco-2, MDCK, HCE): junctional RhoA activation, tight-junction assembly,
  3D cyst morphogenesis (PMID:21258369); apical actomyosin belt via Lulu2/Patj
  (PMID:22006950); LKB1 (PMID:23648482); CRB3A/Ehm2 (PMID:26217016); lumen consolidation
  (PMID:26483385);
- **endothelia**: ZO-1/JACOP-dependent recruitment, junctional tension, barrier
  (PMID:25753039); shear-stress-responsive phosphorylation (PMID:39977269);
- **retinal neuroepithelium** (medaka): apicobasal polarity and neurogenic-vs-proliferative
  division ratio, rescued by the human protein (PMID:23698346);
- **podocytes**: EPB41L5-dependent recruitment, focal-adhesion maturation (PMID:28536193);
- **trophoblast**: syncytiotrophoblast differentiation via AKAP12/PKA/CREB (PMID:33842485);
- **eosinophils**: LOCGEF isoforms, nucleopod tip on activation (PMID:29601110);
- **cortical neurons**: horizontal axon branching on overexpression (PMID:31768529);
- **cardiomyocytes**: conditional-knockout cardiomyopathy (PMID:40159883).

None of these is the molecular function. All of them are the same GEF acting in different
places, which is exactly why the location and partner annotations matter more here than
another process term.

## The stress-fibre sign flip

`GO:0051497` **negative** regulation of stress fiber assembly (IMP, PMID:25753039) looks
backwards for a RhoA activator, and it is worth being explicit about why it is not an
error. The two observations are made in different systems:

- sparse cells, gain of function — "the overexpression of p114-Rho-GEF in J82 and HEK-293
  cells induced the formation of actin stress fibres" (PMID:11085924);
- confluent monolayer, loss of function — "p114RhoGEF depletion led to a loss of junctional
  vinculin and induction of vinculin-stained focal adhesions and stress fibers"
  (PMID:25753039), reproduced in epithelia as "reduced perijunctional f-actin and increased
  formation of stress fibres" (PMID:21258369).

Terry's own explanation: "RhoA activity is downregulated in response to cell confluence;
hence, interfering with junction formation stimulates RhoA signalling in the rest of the
cell." So the negative regulation is a downstream consequence of failing to build
junctions, not a direct molecular action — non-core, kept.

## PAINT propagation

Three IBD nodes, from `interpro/panther/PTHR47440/PTHR47440-paint.tsv` and the GOA
WITH/FROM fields, every token resolved against its own authority:

- `PTN002677784` → `GO:0005085`, seeded by `FB:FBgn0032796` (Drosophila *cyst*/CG10188,
  = Dp114RhoGEF), `MGI:MGI:103264` (mouse *Arhgef2*), `UniProtKB:Q12802` (AKAP13),
  `UniProtKB:Q8N1W1` (ARHGEF28), `UniProtKB:Q92974` (ARHGEF2) and the target itself.
  The fly gene is a genuine ortholog — PMID:31409654 calls Cysts "the Drosophila
  orthologue of mammalian p114RhoGEF, GEF-H1, p190RhoGEF, and AKAP-13" — so this is an
  ancestral node predating the vertebrate expansion of the Lbc clade, not a paralog
  mix-up. Worth registering rather than repairing: current PANTHER assigns Q6ZSZ5 and
  mouse Q6P9R4 to **PTHR47440:SF1** while *every other seed*, including the fly ortholog,
  sits in **PTHR13944**. The family label on the annotation no longer matches the family
  labels on its seeds.
- `PTN002677784` → `GO:0035023`, seeded only by mouse *Arhgef2* and human AKAP13 — two
  paralogs, neither the target nor its ortholog.
- `PTN002677825` → `GO:0005886`, `taxon:117571`, seeded by `UniProtKB:Q6ZSZ5` and
  `UniProtKB:A0A590UK10`. Both are **the same human gene** (A0A590UK10 is a 1089-aa
  TrEMBL entry for ARHGEF18), so no non-human member of the clade has contributed
  evidence to this node yet.

### A rule I got wrong on the first pass

I initially marked the target's own accession `CIRCULAR_OR_REDUNDANT` in the `GO:0005085`
and `GO:0007264` propagation reviews, and described the `GO:0005886` node as a "round
trip". `CLAUDE.md` prohibits exactly this, and it is right to:

> **The target appearing in its own `WITH/FROM` is correct and expected — not circular.**
> […] that annotation is one of the descendant evidences the curator used to place the
> IBD […] **Never** mark such a source `CIRCULAR_OR_REDUNDANT` or describe it as
> inflating support.

An IBD is a curator's judgment about where in the tree a function arose, made by reading
the experimental annotations of *all* extant members — so the target's own IDA being in
the donor list is the marker that experimental grounding exists on the target, and the
IBA then adds the separate claim that the function is inherited rather than
lineage-specific. Nor is a short donor list weak support. What is true, and all that is
true, is that these rows add no evidence the gene did not already have, which makes them
non-core rather than defective. The reviewer caught this; the `reason` prose had already
been saying the correct thing while the enum said something else, which is the failure
mode to watch for, since nothing in the repo validates agreement between the two.

## Which tight-junction term the imaging actually supports

The first draft proposed `GO:0005923` **bicellular** tight junction from Terry's occludin
overlap. That is one level too specific. Confocal colocalisation along a junctional belt
does not separate bicellular from tricellular contacts, and occludin is not confined to
bicellular junctions in any case — PMID:40878853 reports that occludin knockout displaces
tricellulin from tricellular junctions, i.e. occludin acts at them. `GO:0070160` tight
junction is the level the experiment supports, and both QuickGO and OLS4 report it
current.

The term choice also decides whether the companion `GO:0043296` row is informative, which
is worth recording because it is not obvious:

- `GO:0005923` has **`GO:0043296` among its hierarchical parents** (OLS4 direct parents:
  `GO:0043296`, `GO:0070160`; QuickGO ancestors include `GO:0043296`). Annotating
  `located_in GO:0005923` would therefore have *implied* the apical-junction-complex row
  by propagation, making it redundant.
- `GO:0070160` does **not** — its only hierarchical parent is `GO:0005911` cell-cell
  junction, and `GO:0043296` is absent from its QuickGO ancestor list.

So moving to the parent term is what makes the pair genuinely complementary. Checked in
both services rather than assumed.

## Coverage, not over-annotation

`ARHGEF18-bioinformatics/reference_coverage.py` queries QuickGO by reference,
species-blind: **19 of 23 primary ARHGEF18 papers have produced no GO annotation on any
gene in any species**, none undetermined. Everything GOA does assert about this gene is
defensible; the defect is the size of what is absent — the founding biochemistry, the
*Nat Cell Biol* junction paper, the *AJHG* disease paper, the only structure of the
protein, and an entire vertebrate knockout. Meanwhile the *Drosophila* ortholog *cyst*
**is** curated (`GO:0005085` IDA, `GO:0090688` IDA, `GO:1902408` IEP from PMID:36917931),
annotations that could seed ISS or IBA to the human gene and have not.

And there is no mammalian ortholog record to lean on. The same script audits the
ortholog records and finds **mouse `Arhgef18` carries 23 GO annotations of which none is
experimental** — ISO 10, IEA 6, IBA 4, ISS 3, neither set truncated — against 14
experimental rows on the human record, which is the positive control for the
evidence-code split. Ten of the mouse rows are ISO *from human*, so a similarity transfer
back would only recirculate the same four experiments. That matters for PDB 6BCB in
particular: the 1.4 Å RhoA complex was solved on the **mouse** protein and the mouse
record does not carry it either, so the proposed `GO:0031267` has no curated source in
either species and needs creating at the source as well as here.

## Residue mapping gotcha

Neither loss-of-function paper states its reference sequence, and they do not agree:

- Arno's `p.Thr270Ala` → canonical **Thr-458** (offset +188, the N-terminal extension
  UniProt added in sequence version 4 on 10-OCT-2018 — confirmed independently by
  UniProt's own `VARIANT 458 T->A`);
- Terry's `p114RhoGEF-Y260A` → canonical **Tyr-606** (offset +346, the `p114` isoform
  Q6ZSZ5-2, whose `VAR_SEQ VSP_059874` deletes residues 1–346).

Applying Arno's offset to Terry's position gives an arginine, not a tyrosine, which is
what makes the two assignments distinguishable rather than arbitrary. Tyr-606 is the
pan-Dbl catalytic tyrosine: it is present in all 14 panel members, Rac- and Cdc42-specific
GEFs included, so its retention says nothing about substrate.
