# NR1H4 (FXR) — curation notes

UniProtKB:Q96RI1 · *Homo sapiens* · "Bile acid receptor" / farnesoid X-activated
receptor (FXR) · nuclear receptor subfamily 1 group H member 4.
Synonyms in the record: BAR, FXR, HRR1, RIP14. `PE 1: Evidence at protein level`.

Curated because the bile-acid pathway modules in this repository
(`bile_acid_biosynthesis`, `bile_acid_synthesis_ring_modification`,
`bile_acid_synthesis_sidechain_conjugation`, `enterohepatic_bile_salt_cycling`)
all name FXR-mediated feedback as the regulation of the flux they carry, while
neither FXR nor its two downstream repressors (NR0B2/SHP, NR5A2/LRH-1) had a
gene review here. The receptor end of the intestinal arm is already covered in
`fgfr_signaling` (FGFR4/β-Klotho carries `GO:0090206 negative regulation of bile
acid biosynthetic process`); this review covers the ligand-sensing end.

## What the protein is

A ligand-activated transcription factor that binds DNA predominantly as a
heterodimer with RXRA and is the nuclear receptor for bile acids. UniProt's
curated FUNCTION block is unusually complete and carries `ECO:0000269` PubMed
evidence for most statements, so much of this review's work is checking those
statements rather than reconstructing the biology from scratch.

DNA-binding specificity, from the curated record:

> The FXR-RXR heterodimer binds predominantly to farnesoid X receptor response
> elements (FXREs) containing two inverted repeats of the consensus sequence
> 5'-AGGTCA-3' in which the monomers are spaced by 1 nucleotide (IR-1) but also
> to tandem repeat DR1 sites with lower affinity
> — `file:human/NR1H4/NR1H4-uniprot.txt` CC FUNCTION

## Ligands — the founding result

Two back-to-back 1999 *Science* papers established bile acids as the endogenous
ligands, and both are the `IDA` reference for the MF terms in GOA.

- [PMID:10334992 "bile acids are physiological ligands for the farnesoid X
  receptor"] — and in the same abstract, the output: [PMID:10334992 "FXR
  repressed transcription of the gene encoding cholesterol 7alpha-hydroxylase,
  which is the rate-limiting enzyme in bile acid synthesis, and activated the
  gene encoding intestinal bile acid-binding protein"]. Both halves of the
  feedback loop are in that one sentence: CYP7A1 down, FABP6/I-BABP up.
- [PMID:10334993 "Physiological concentrations of free and conjugated
  chenodeoxycholic acid, lithocholic acid, and deoxycholic acid activated the
  farnesoid X receptor"], acting through coactivator recruitment:
  [PMID:10334993 "these bile acids and their conjugates modulated interaction of
  FXR with a peptide derived from steroid receptor coactivator 1"].

CDCA is the most potent of these, which is why GOA carries both the general
`GO:0032052 bile acid binding` and the specific `GO:1902122 chenodeoxycholic
acid binding`. Ursodeoxycholic acid is a natural agonist and an approved drug
for primary biliary cirrhosis, per the record's MISCELLANEOUS block
(`ECO:0000305|PubMed:23235576` — an inference by the UniProt curator, not a
primary result).

## Feedback repression of bile acid synthesis runs through two arms

This is the core biology and the reason the gene matters to the pathway modules.
FXR does not repress `CYP7A1` directly — it induces intermediaries, in two
tissues.

**Hepatic arm (FXR → NR0B2/SHP ⊣ CYP7A1, CYP8B1).** From the curated record:

> In the liver activates transcription of the corepressor NR0B2 thereby
> indirectly inhibiting CYP7A1 and CYP8B1 (involved in BA synthesis) implicating
> at least in part histone demethylase KDM1A resulting in epigenomic repression,
> and SLC10A1/NTCP (involved in hepatic uptake of conjugated BAs)
> — `file:human/NR1H4/NR1H4-uniprot.txt` CC FUNCTION

Note that this arm carries a `By similarity` qualifier in part, and SHP acts by
antagonising NR5A2/LRH-1 and HNF4A at the *CYP7A1* promoter — neither of which
has a gene review here yet. `MAFG` is named as a second FXR-induced repressor of
BA synthesis, also `By similarity`.

**Intestinal arm (FXR → FGF19 → FGFR4/KLB ⊣ CYP7A1).**

> In the intestine activates FGF19 expression and secretion leading to hepatic
> CYP7A1 repression — `file:human/NR1H4/NR1H4-uniprot.txt` CC FUNCTION

The primary result: [PMID:12815072 "We demonstrate that FXR directly regulates
expression of fibroblast growth factor-19"] and [PMID:12815072 "FGF-19 strongly
suppresses expression of CYP7A1 in primary cultures of human hepatocytes and
mouse liver through a c-Jun N-terminal kinase (JNK)-dependent pathway"]. Human
hepatocytes and mouse liver in the same sentence — so an evidence item quoting
it needs care over which organism the quoted clause covers.

The record adds that the arm requires "the coordinated induction of hepatic
KLB/beta-klotho expression", again `By similarity`.

**Tissue split matches the isoforms.** The record's TISSUE SPECIFICITY states
liver expresses mainly FXRα1-type isoforms and intestine/kidney mainly
FXRα2-type, which is a structural correlate of the two-arm division worth
keeping in mind when reading isoform-specific transactivation results.

## Target genes

Grouped from the curated FUNCTION block. Each is a target, not a function of
FXR; several of these targets are the parts of the modules this review supports.

**Induced:** `NR0B2`/SHP, `FGF19`, `ABCB11`/BSEP (by directly recruiting the
histone methyltransferase CARM1), `SLC27A5`/BACS and `BAAT` (conjugation),
`ABCC2`/MRP2, `ABCB4`, `FABP6`/I-BABP, `UGT2B4` and `SULT2A1` (detoxification;
UGT2B4 apparently by a monomeric, RXRA-independent mechanism), `MAFG`, `KLB`,
`PLTP`, `SCARB1`, `APOE`, `APOC1`, `APOC2`, `APOC4`, `PPARA`, `VLDLR`, `SDC1`.

**Repressed:** `CYP7A1` and `CYP8B1` (via SHP), `SLC10A1`/NTCP, `SREBF1` (de
novo lipogenesis, via SHP), `MTTP` (VLDL assembly), `APOC3` and `ANGPTL3` (both
LPL inhibitors), `APOA1` (by monomeric competition with NR2A1 at a DR1 element),
`PLA2G12B`.

Five of the induced targets — `ABCB11`, `FABP6`, `SLC27A5`, `BAAT`, `SLC10A1` —
are parts of the bile-acid modules in this repository, and `ABCB11` and `FABP6`
are two of the three participants `enterohepatic_bile_salt_cycling` records as
lacking gene reviews (its own note at line 82). So this review's target list is
directly the regulation layer those modules say they exclude.

## Lipoprotein effects

Relevant because this is where FXR activity reaches LDL and cholesterol, and
where the GOA terms are the least comfortable fit.

- `GO:0010988 regulation of low-density lipoprotein particle clearance` (IDA,
  PMID:12660231) rests on SDC1 induction: [PMID:12660231 "resulted in both
  induction of SDC1 mRNA and enhanced binding, internalization, and degradation
  of low density lipoprotein"]. Human hepatocytes, agonist-driven (CDCA and
  GW4064). The same paper reports the effect is **isoform-specific** — only the
  FXR isoforms lacking the four-amino-acid hinge insert activated the SDC1
  promoter — which is a point the `isoform:` field should carry if the GOA row
  does not already.
- `GO:0010903 negative regulation of very-low-density lipoprotein particle
  remodeling` (IDA, PMID:27471003) rests on PLA2G12B repression via SHP:
  [PMID:27471003 "PLA2G12B expression was transcriptionally repressed due to an
  FXR-mediated up-regulation of small heterodimer partner (SHP) which
  functionally suppresses HNF-4"] with the physiological readout [PMID:27471003
  "CDCA treatment lowered hepatic VLDL-TG secretion"]. **Flag for review:** the
  paper measures VLDL *secretion*, while the GO term says particle
  *remodeling* — those are different processes, and the term may be a
  mis-selection rather than a mis-attribution. Check the term definition before
  deciding between MODIFY and ACCEPT.

The record notes SDC1 induction "may account in part for the hypotriglyceridemic
effect that can result from the administration of chenodeoxycholic acid to
humans" — a curator inference, not a measured result.

## Complex, cofactors and PTMs

Heterodimer with RXRA via its C-terminus to RXRA's DBD; heterodimerization
enhances affinity for coactivator LXXLL motifs (PubMed:23462506, PubMed:30275017).
Coactivators/cofactors named with `ECO:0000269`: NCOA1, NCOA2, PPARGC1A, CARM1,
SETD7, PRMT1, GPS2, SMARCA4, MED1; PAGR1 and NCOA6 (an MLL2/MLL3 ASCOM
association); XRCC5 and XRCC6, which *decrease* transactivation toward ABCB11.
EP300 and SMARCD1 are `By similarity` only.

PTMs, all `ECO:0000269`: acetylation by EP300 with Lys-227 the major site, which
**inhibits** RXRA heterodimerization and transactivation, reversed by SIRT1
deacetylation (PubMed:18755856); methylation increasing transactivation
(PubMed:22345554); PKC/PRKCA phosphorylation increasing transactivation by
promoting PPARGC1A association (PubMed:18755856). Sumoylation is required for
TLR4 trans-repression (PubMed:19864602).

Note the protein-binding IPI rows in GOA (five of them, `GO:0005515`) are
removed under this repository's protein-binding policy as uninformative; the
specific partners above are better expressed through `GO:0001221 transcription
coregulator binding` (already present, IPI, PMID:14701856) and the complex terms.

## Immunity and inflammation

A substantive secondary role, with human IDA evidence (PMID:21242261) behind
`GO:0032689`, `GO:0032720`, `GO:0032740` and `GO:0043124`. The record describes
down-regulation of inflammatory cytokines in macrophages and mononuclear cells,
TLR4 trans-repression requiring sumoylation and preventing N-CoR clearance from
IL1B and NOS2, and a TLR9-mediated protective mechanism in intestinal
inflammation. Several of the surrounding claims (intestinal barrier preservation,
protection against bacterial overgrowth, anti-inflammatory role in liver
inflammation, NF-κB inhibition) are `By similarity` from mouse/rat orthologs
(Q60641, Q62735) rather than human results.

`GO:0032740 positive regulation of interleukin-17 production` sits oddly beside
the otherwise uniformly anti-inflammatory set; worth reading PMID:21242261
before accepting it at face value.

## Disease

- **PFIC5** — progressive familial intrahepatic cholestasis 5, MIM:617049,
  autosomal recessive, neonatal-onset intralobular cholestasis progressing to
  fibrosis and cirrhosis (`ECO:0000269|PubMed:26888176`). Caused by variants in
  this gene. This is the loss-of-function phenotype that makes FXR a required
  part of the bile-acid system rather than a modulator of it.
- Two weaker associations, both `ECO:0000305` (curator inference): intrahepatic
  cholestasis of pregnancy (PubMed:17681172) and cholesterol cholelithiasis
  (PubMed:17931734). Do not promote either to an annotation.

## Isoforms

Five, from alternative promoter usage *and* alternative splicing — FXRα1 vs α2
at the N-terminus (promoter), and ± a four-residue hinge insert (splicing).
All four tested isoforms are nuclear (`ECO:0000269|PubMed:23928191`). The hinge
insert changes target-gene selectivity (SDC1, above), so isoform identity is
functionally load-bearing here and not merely "what was tested". The stub already
carries the `alternative_products` block from the fetch.

## Annotation shape to expect

112 GOA rows seeded: 37 IEA, 35 IDA, 13 TAS, 11 IBA, 7 IPI, 3 IMP, 2 ISS, 2 ISA,
2 EXP, 1 IC. 57 BP, 27 MF, 12 CC (deduplicated by term+code).

The MF/CC backbone is in good shape and mostly needs ACCEPT: `GO:0038186 bile
acid nuclear receptor activity`, `GO:0032052 bile acid binding`, `GO:1902122
chenodeoxycholic acid binding`, `GO:0004879 nuclear receptor activity`,
`GO:0001228 DNA-binding transcription activator activity, RNA polymerase
II-specific`, `GO:0000977`/`GO:0000978` RNA Pol II regulatory-region DNA
binding, `GO:0005634 nucleus`, `GO:0043235 signaling receptor complex`.

The BP set is where the judgement is, and it is long and pleiotropic: bile-acid
and cholesterol homeostasis (core), lipid and triglyceride homeostasis,
glucose/insulin, immunity, plus several that look like over-reach from single
papers — `GO:0000050 urea cycle` and `GO:2001250 positive regulation of ammonia
assimilation cycle` (IMP/IEA from PMID:21757002, a glutamine/glutamate transport
paper), `GO:1904179 positive regulation of adipose tissue development`,
`GO:0007043 cell-cell junction assembly`. Expect a lot of `KEEP_AS_NON_CORE` and
a handful of `MARK_AS_OVER_ANNOTATED`.

## How the four open questions resolved

1. **`GO:0010903` is the wrong term.** `GO:0034372` defines VLDL particle
   remodeling as post-secretory acquisition, loss or modification of protein or
   lipid within the particle, including lipase-mediated triglyceride hydrolysis.
   PMID:27471003 measured hepatic VLDL-TG *secretion*. And FXR's effects on
   genuine remodeling point the other way: it induces APOC2 and represses the
   lipoprotein-lipase inhibitors APOC3 and ANGPTL3, all of which *raise* lipase
   activity. GO has no regulation-of-VLDL-assembly term (checked: `GO:0034379`
   exists, no regulation child), so the row is `MODIFY` to the lateral
   `GO:0070328 triglyceride homeostasis` the entry already carries, and the gap
   is filed in `proposed_new_terms`.
2. **`GO:0032740` could not be settled** — left `UNDECIDED`, with a
   `source_defects` entry asking UniProt to check the sign. See
   "The IL-17 row" below; this turned out to be the most interesting row in the
   set.
3. **The urea-cycle pair is better than it looks** — `KEEP_AS_NON_CORE`, not
   over-annotated. PMID:21757002 maps an FXRE in the human and mouse *NAGS*
   promoters by EMSA, ChIP and reporter assay, and N-acetylglutamate is the
   obligate allosteric activator of the cycle's first enzyme, so this is a
   direct-target effect rather than one of the diffuse metabolic correlations
   that make a transcription factor's downstream process terms suspect. The
   `acts_upstream_of_positive_effect` qualifiers already keep FXR outside the
   process it regulates.
4. **Both arms belong in `core_functions`, as a second entry.** The activity is
   one thing and is recorded once (`GO:0038186`, first core function); the
   feedback repression is a separate process-level claim whose direct molecular
   function is still transactivation (`GO:0001228`), because SHP and FGF19 do the
   repressing. A third entry covers the conjugation/export/reuptake programme.

## Outcome

112 rows reviewed: 62 `ACCEPT`, 32 `KEEP_AS_NON_CORE`, 6 `TOO_GENERAL`, 5
`REMOVE`, 4 `MARK_AS_OVER_ANNOTATED`, 2 `MODIFY`, 1 `UNDECIDED`.

- `TOO_GENERAL` is used only for generic ancestors of terms accepted on direct
  evidence in the same review (`GO:0003677`, `GO:0003700`, `GO:0006355`,
  `GO:0006357`, `GO:0045893`). The action-consistency table lists
  `TOO_GENERAL ANCESTOR_OF ACCEPT` as the intended use.
- `REMOVE` is used only for the five bare `GO:0005515` rows, under the
  protein-binding policy. The partners are not doubted: `GO:0016922 nuclear
  receptor binding` (RXRA) and `GO:0001221 transcription coregulator binding`
  carry them.
- `GO:0046965` is obsolete, so it is `MODIFY` to `GO:0016922` rather than
  removed — the RXRA heterodimerisation claim is correct and central.
- `GO:0070857 regulation of bile acid biosynthetic process` is `MODIFY` to the
  signed child `GO:0070858`, not `ACCEPT`. The row's own reason says FXR
  *represses* CYP7A1 and CYP8B1 and its quote states the direction outright, so
  accepting the unsigned parent would have been accepting a term while arguing
  it was too general. FGFR4 and KLB — the two downstream members of the same
  circuit — already carry `GO:0070858` for it, so this also makes the three
  agree. Caught in review on #5845.
- Two `proposed_new_terms` came out of the review, both genuine GO gaps found by
  curating this gene: regulation of VLDL particle assembly, and regulation of
  bile acid import across the plasma membrane.

**The second gap is narrower than it first looked**, and the first version of
these notes overstated it. The export arm of what FXR does is annotatable after
all — its induction of the canalicular pumps is `GO:0120189` — so `GO:0015721`
is `MODIFY` to that rather than over-annotated. What has no term is the
**uptake** arm: FXR represses SLC10A1/NTCP, and GO has no bile-acid import
*process* term at all, so there is nothing for a regulation term to regulate.
The proposal is therefore two entries — the import process, then its regulation
— since minting the regulation class alone would leave it with nothing to
regulate. The row also carries a `WRONG_TERM` source defect for Reactome: with
`GO:0120189` in place the `involved_in` qualifier is correct, so the term was
the defect, not the qualifier.

### The bile-acid transport and secretion terms, verbatim

Recorded in full because the sign of `GO:0120189` is load-bearing — it is the
`MODIFY` replacement and a `corrected_value` headed upstream — and because
`GO:0070857/8/9` is ordered regulation/**negative**/positive, so the obvious
guess for this triple is wrong. QuickGO, queried 2026-11-01:

| CURIE | Label |
|---|---|
| `GO:0120188` | regulation of bile acid secretion |
| `GO:0120189` | **positive** regulation of bile acid secretion |
| `GO:0120190` | negative regulation of bile acid secretion |

So this triple runs regulation/**positive**/negative — the opposite order to
`GO:0070857/8/9`. Definitions, to pin it beyond the labels: `GO:0120189` is
*"Any process that activates or increases the frequency, rate or extent of the
controlled release of bile acid from a cell or a tissue"*, and `GO:0120190` is
the *"stops, prevents or reduces"* counterpart. FXR induces the canalicular
pumps, so `GO:0120189` is the right one.

And the surrounding space, same query date: `GO:0015721 bile acid and bile salt
transport` has exactly two children, `GO:0015125` (a molecular function, via
`part_of`) and `GO:0015722 canalicular bile acid transport`, so it has no
regulation child of its own. `GO:0032782 bile acid secretion` is what the
`GO:0120188` triple regulates. A search of the bile-acid space returns no
import, uptake or influx process term in any direction, which is the gap the two
proposed terms address.

## The IL-17 row

`GO:0032740 positive regulation of interleukin-17 production`, IDA from
PMID:21242261. The direction is wrong-looking, and the reason it is worth
writing down is that **the contradiction is internal to UniProt**, not a
disagreement between us and a curator.

- UniProt's curated `CC FUNCTION` block cites this exact paper for the opposite
  claim: *"Down-regulates inflammatory cytokine expression in several types of
  immune cells including macrophages and mononuclear cells (PubMed:21242261)."*
- The sibling GOA rows UniProt created from this paper in the **same curation
  session** (2016-01-19) are all negative: `GO:0032689` type II interferon,
  `GO:0032720` TNF, and `GO:0043124` canonical NF-kappaB. One row out of **four**
  carries the opposite sign.
- The paper's own conclusion is that FXR activation *inhibits* proinflammatory
  cytokine production.
- IL-17 appears nowhere in its abstract, nowhere in its MeSH terms, and nowhere
  in the 16-citation deep-research report for this gene.

What could not be checked: the full text. The paper is not in PMC, and Europe
PMC and BMJ both refuse access. So the one scenario that would make the row
correct — an IL-17 panel in one of the four assayed human immune populations
(PBMCs, CD14 monocytes, dendritic cells, IBD lamina propria mononuclear cells)
showing a genuine positive effect against the anti-inflammatory trend — cannot
be excluded from outside.

Hence `UNDECIDED` plus a `source_defects` entry: `WRONG_TERM`, resource
`UNIPROT`, `requested_change: CHECK`, `confidence: SUSPECTED`, proposing
`GO:0032700 negative regulation of interleukin-17 production` as the expected
term if IL-17 was measured at all.

**The first version of this proposal named `GO:0032703`, which is negative
regulation of interleukin-*2*.** Caught in review on #5845. It is worth recording
rather than quietly fixing, because it is precisely the failure the *Every CURIE
is read from a source in the same step it is written* rule exists to prevent, and
because `source_defects` is the one field here that gets exported and sent
upstream — so the defect report would have reached UniProt naming a term about
the wrong cytokine. This same file already used `GO:0032703` correctly for IL-2
eleven hundred lines earlier, and the gene's own UniProt flat file states its
label on line 1048. Nothing checked the two against each other: a CURIE inside
`corrected_value` is free text as far as validation is concerned, which is the
same blind spot that `qualifiers` has in dismech. `just export-source-defects` now carries it
in the UniProt report. This keeps the action honest — the rule against
overruling an experimental annotation from an unread full text applies — while
not losing the finding, which bare `UNDECIDED` would have done.

**On the term class itself.** `GO:0032740` is coarse but not broken, and the
coarseness is worth knowing about. Its definition covers "any member of the
interleukin-17 family", which lumps IL-17A/F (Th17 effectors) with IL-17E/IL-25
(a Th2 alarmin) and IL-17B/C/D, cytokines with substantially different biology.
And "production" conflates transcription, translation and secretion, so the term
does not say which step a regulator acts on. For a transcription factor it is
also a downstream-output term of the kind this repository treats as
over-annotation when the gene is not itself part of the axis.

The corpus already applies that distinction consistently: of the eight human
genes carrying `GO:0032740` here, the three reviews that `ACCEPT` it are IL15,
IL21 and IL23R — genes that *are* IL-17-axis components — while every regulator
(MYD88, OPA1, PRKCQ, SPHK1) has it as `KEEP_AS_NON_CORE`. So had the direction
been right, `KEEP_AS_NON_CORE` would have been the action here, not `ACCEPT`.

## The deep-research run

It completed (OpenScientist, 644 s) and is committed with its artifacts. It
agreed with the curated UniProt record and the primary papers on every point
checked, and it is **deliberately not cited as `supporting_text` for any
annotation** — it is AI-generated, so it is leads. It is recorded in
`references` with a `reference_review` saying so (relevance MEDIUM, correctness
UNVERIFIED). The validator's advisory "No annotations reference available deep
research files" warning is therefore expected here, not an omission.

What it was worth: three primary references this review then fetched and quoted
directly.

- **PMID:12393883** — four FXR transcripts, and the four-residue hinge insert
  raises FXRE binding affinity. This is the mechanism behind the isoform-specific
  SDC1 induction in PMID:12660231, which the LDL-clearance row now records.
- **PMID:30275017** — crystal structure of the human FXR/RXRα LBD heterodimer,
  with higher coactivator affinity in the heterodimer than in either monomer.
  Supports the obligate-heterodimer core function.
- **PMID:31201556** — the biallelic FXR truncation/deletion patients with severe
  early-onset PFIC and liver failure. The loss-of-function evidence that the
  receptor is required and uncompensated.

## What this review does not do

- `NR0B2`/SHP and `NR5A2`/LRH-1 still have no gene reviews. They are the
  intermediaries through which every repression claim here runs.
- `ABCB11`, `FABP6` and `SLC51B` are named as parts of
  `enterohepatic_bile_salt_cycling` with no gene reviews. That module's own note
  records this, and now lists `SLC51A` stalely, since `SLC51A` has since been
  reviewed.
- No module was created for the feedback circuit itself. The three core
  functions here describe it, but there is no `bile_acid_feedback_regulation`
  module tying FXR, SHP, LRH-1, FGF19 and FGFR4/KLB into one pathway record.

## Provenance of this file

Written from `NR1H4-uniprot.txt` and the cached publications PMID:10334992,
PMID:10334993, PMID:12815072, PMID:12660231, PMID:27471003, PMID:21242261,
PMID:21757002, PMID:20447400, PMID:23767959, plus PMID:12393883, PMID:30275017
and PMID:31201556 fetched from the deep-research leads.

Every quote used here and in the review was checked as a whitespace-normalized
substring of its source using the repository's own normalizer
(`ai_gene_review.validation.local_source_text`), which is what unwraps the
UniProt flat file's `CC`/`FT` line codes — a plain `grep -F` fails on every
multi-line UniProt quote and on any publication quote that crosses a line wrap,
which is most of them. Three `record_section` values initially said
`CC:FUNCTION` for a quote that sits in `CC:SUBUNIT`; `backfill-record-sections`
reported the mismatch and they were corrected.

Only PMID:12815072 and PMID:23767959 have full text in the cache; the rest are
abstract-only, so annotations resting on them cannot be second-guessed from what
is cached here (see the "Do not overrule curators from incomplete evidence"
rule). That constraint is what left `GO:0032740` `UNDECIDED`.

The OpenScientist deep-research run completed; see "The deep-research run" above. It
is in `NR1H4-deep-research-openscientist.md` and is read as leads rather
than as evidence.
