# HNRNPA1 (P09651) curation notes

Working journal for the HNRNPA1 review. No provider deep-research file was generated for
this gene: the scanner environment that produced this review has no Perplexity/OpenAI/Falcon
credentials, so `just deep-research` could not run. Everything below is my own reading of
the cached publications in `publications/` and of the UniProt record, with inline
provenance. Nothing here is provider output and this file must not be renamed to
`-deep-research-*.md`.

## What the protein is

hnRNP A1 is one of the most abundant nuclear RNA-binding proteins. The N-terminal half is
two tandem RRMs (UniProt `FT DOMAIN 14..97`, `105..184`), historically purified as the
proteolytic fragment UP1; the C-terminal half is a glycine-rich low-complexity /
prion-like domain containing an RGG box (`FT REGION 218..240`) and the M9 shuttling
sequence (`FT REGION 320..357`, "Nuclear targeting sequence (M9)"). Pfam records both
halves: `PF00076 RRM_1` ×2 and `PF11627 HnRNPA1_LC`. UniProt lists three isoforms, with
A1-A (P09651-2) "twenty times more abundant than isoform A1-B" (`CC MISCELLANEOUS`).

Curated function statement, tied to publications rather than to a rule
[file:human/HNRNPA1/HNRNPA1-uniprot.txt, "Involved in the packaging of pre-mRNA into hnRNP
particles, transport of poly(A) mRNA from the nucleus to the cytoplasm and modulation of
splice site selection (PubMed:17371836)"].

## Core activity: sequence-specific pre-mRNA binding and splice-site choice

- hnRNP A1 and A2 are "RNA binding proteins with well established roles as sequence-specific
  repressors of splicing", and on the PKM pre-mRNA the binding site is intronic:
  [PMID:20010808 "These data confirm the presence of an inhibitory hnRNPA1/hnRNPA2 binding
  site immediately downstream of the E9 5′ splice site."] Depleting hnRNPA1/A2 shifts PKM
  splicing towards PKM1, so the binding is functional, not incidental.
- The same intronic interaction is the target of a micropeptide: the HOXB-AS3 peptide
  "antagonizes the hnRNP A1-mediated regulation of pyruvate kinase M (PKM) splicing by
  blocking the binding of the ariginine residues in RGG motif of hnRNP A1 to the sequences
  flanking PKM exon 9" [PMID:28985503] (the misspelling of "arginine" is in the source).
- Splice-site antagonism also runs through partner proteins: [PMID:17371836 "Finally, Sam68
  interacted with heterogenous nuclear RNP (hnRNP) A1, and depletion of hnRNP A1 or
  mutations that impair this interaction attenuated Bcl-x(s) splicing."]
- RAGE (AGER) alternative splicing is hnRNP A1-dependent and responds to glucose
  deprivation [PMID:25689357]; this is the source of both the `GO:0000381` IMP and the
  `GO:0042149` cellular response to glucose starvation IMP.
- Structural membership of the spliceosome is curated from the C-complex purification
  [file:human/HNRNPA1/HNRNPA1-uniprot.txt, "Identified in the spliceosome C complex
  (PubMed:11991638)"], consistent with the earlier spliceosome mass-spectrometry
  characterisation [PMID:9731529].

## Shuttling and mRNA export

M9 is both an import and an export determinant: "A 38 amino acid domain within A1, termed
M9, which bears no resemblance to classical nuclear localization signal (NLS) sequences,
localizes A1 to the nucleus", and the same element exports a nucleus-restricted reporter,
which the authors read as support for the idea that A1 and relatives "function as carriers
for RNA during export to the cytoplasm" [PMID:8521471].

Curation consequence: the `GO:0051170 import into nucleus` row from that paper records that
hnRNP A1 **is imported** (M9 is its own PY-NLS, read by transportin-1), not that it imports
anything. That is the cargo-versus-carrier distinction, so this review marks that row as an
over-annotation while keeping `GO:0006405 RNA export from nucleus`, which is the claim the
paper actually argues for, and refining the generic `GO:0051168 nuclear export` row to it.

## Condensates and stress granules — the main annotation gap

HNRNPA1 had **no** stress-granule or condensate annotation in GOA at the time of this
review, although it is one of the founding examples of low-complexity-domain-driven phase
separation.

- Dedicated cell-biological paper: "the stress-induced cytoplasmic accumulation of hnRNP A1
  occurs in discrete phase-dense particles, the cytoplasmic stress granules (SGs)", with
  recruitment requiring mRNA binding and Mnk1/2-dependent phosphorylation downstream of p38;
  "depletion of hnRNP A1 affects the recovery of cells from stress" [PMID:16847328].
- Landmark LLPS paper: "the disease-related RBP hnRNPA1 undergoes liquid-liquid phase
  separation (LLPS) into protein-rich droplets mediated by a low complexity sequence domain
  (LCD)", and "while not required for LLPS, fibrillization is enhanced in protein-rich
  droplets" [PMID:26406374].
- Independent reconstitution, including heterotypic recruitment, which is what makes this a
  scaffold activity rather than just self-assembly: "hnRNPA1 droplets generated in low salt
  effectively recruit the IDRs of Lsm4, Pub1, eIF4GII and Fus" and "Thus, hnRNPA1 can
  undergo IDR-dependent LLPS on its own at low ionic strength" [PMID:26412307].
- Disease context: the PrLD steric-zipper mutations accelerate fibrillisation and SG
  recruitment, assayed for hnRNPA1 alongside hnRNPA2 [PMID:23455423 "Similar results were
  obtained upon examination of endogenous hnRNPA1 as well as exogenous wild-type and mutant
  hnRNPA1"]; the flail-arm ALS P288S variant in the PY-NLS gives "cytoplasmic inclusions
  that colocalized with stress granules in transfected cells" [PMID:27694260].

### Comparator check before proposing

Two candidate terms, two different answers from the same check (QuickGO by term id,
human, verified to return positives):

- `GO:0140693 molecular condensate scaffold activity` — carried by FUS (IDA/EXP/IMP),
  TARDBP (IDA) and HNRNPA2B1 (IDA), i.e. by the same-role comparators, and absent from
  HNRNPA1. That is a genuine gap; proposed as a `NEW` IDA row.
- `GO:0034063 stress granule assembly` — 87 human annotations, and the nucleators are the
  ones that carry it (G3BP1, G3BP2, TIA1, UBAP2L, ATXN2, ATXN2L, YTHDF1-3, PRRC2C). FUS,
  TARDBP, HNRNPA2B1 and HNRNPA1 are all absent. A systematic absence across the whole
  class of PrLD client RBPs is a convention, not an oversight, so this review does **not**
  propose it, and records the open question instead. `GO:0010494 cytoplasmic stress granule`
  (the location) is proposed, which is what the Guil data actually show.

## Nucleic-acid binding beyond pre-mRNA

- Single-stranded G-rich DNA: the UP1 crystal structure with 12-nt telomeric ssDNA
  "reveals the basis for sequence-specific recognition of the single-stranded overhangs of
  human telomeres by hnRNP A1", and the authors note it "provides insights into the basis
  for high-affinity binding of hnRNP A1 to certain RNA sequences" [PMID:10323862] — i.e.
  the telomeric and the splicing-silencer specificities are the same RRM activity.
- TERRA and telomerase: hnRNPA1 binding to TERRA relieves TERRA's inhibition of telomerase
  ("The telomerase-inhibitory effects of TERRA are alleviated on hnRNPA1 association with
  TERRA"), while "excess of hnRNPA1 also inhibits telomerase through binding and
  sequestration of the DNA primer", with "no notable direct effects on the telomerase
  catalysis" [PMID:23935072]. The apparently contradictory `GO:0032211`/`GO:0032212` pair in
  GOA is therefore not an error: both directions come from this one three-state model. Kept
  as non-core because the assays are in vitro reconstitutions.
- pri-miRNA: "we show that hnRNP A1 binds specifically to the primary RNA sequence
  pri-miR-18a before Drosha processing", and "HeLa cells depleted of hnRNP A1 have reduced in
  vitro processing activity with pri-miR-18a and also show reduced abundances of endogenous
  pre-miR-18a" [PMID:17558416]. Comparator check: `GO:0031053 primary miRNA processing` is
  carried by auxiliary RBPs of exactly this kind (DDX5, SRSF3, SRRT, PUS10) **and by
  HNRNPA2B1**, so the absence on HNRNPA1 is a gap; `GO:0070878 primary miRNA binding` is
  likewise carried by DDX5, SRSF3 and PUS10. Both proposed.
- The existing `GO:0035198 miRNA binding` IDA comes from a pre-miRNA pull-down compendium
  [PMID:28431233], and UniProt reads it as "May bind to specific miRNA hairpins". Hairpins
  are pre-miRNA, and `GO:0070883 pre-miRNA binding` is a sibling of `GO:0035198` (mature
  21-23-nt miRNA) under RNA binding, not its child — so this is a lateral MODIFY, not a
  refinement.

## Translational repression of APAF1

hnRNP A1 binds the apaf-1 IRES and represses it; removing the binding de-represses:
"EV71 infection or ectopic expression of 3C protease cleaves hnRNP A1, which abolishes its
binding to the apaf-1 IRES. This allows IRES-dependent synthesis of apaf-1, activation of
caspase-3, and apoptosis" [PMID:31498791]. UniProt curates this as function with
ECO:0000269. Comparator check: `GO:0045947 negative regulation of translational initiation`
is carried by RNA-binding repressors of this kind (RBM4, LARP1, AGO2, PAIP2, EIF4E2), so the
term is used for this role; proposed as a `NEW` IDA row. No GO term exists for IRES binding
as a molecular function (searched OLS: only `GO:0075522 IRES-dependent viral translational
initiation`, a process), so no MF is proposed for it.

## Two rows I could not verify

`GO:0019904 protein domain specific binding` is annotated twice, from [PMID:10332027] and
[PMID:10749975]. Both abstracts are entirely about the **hnRNP G family** — RBMY/RBMX and
hnRNP G-T — and their partners T-STAR/SAM68 and Tra2beta; neither abstract mentions hnRNP
A1, and the `With/From` values are RBMY1C (P0DJD4) and TRA2B (P62995), which are the two
proteins those papers actually pair with hnRNP G. Neither paper is cached with full text, so
I cannot exclude that hnRNP A1 was also assayed (it is the classic 5'-splice-site modulator
and would be a natural comparator in PMID:10749975, which reports effects on 5' splice site
selection). Recorded as `UNDECIDED` with a `SUSPECTED` / `CHECK` source defect naming RBMX as
a candidate, not as a correction: per repository policy a wrong-gene claim needs the full
text or an abstract that settles it, and this is neither.

## Not supported

- `GO:0016020 membrane` (HDA, [PMID:19946888]): no transmembrane segment, lipid anchor or
  signal peptide in the UniProt feature table. The same high-throughput membrane-fraction
  dataset produced the same spurious row on HNRNPA2B1, where this project already marked it
  an over-annotation.
- Bare `GO:0005515 protein binding`: 30 rows from IntAct/UniProt. hnRNP A1 is abundant and
  phase-separating, which makes it a frequent affinity-proteomics hit; the rows carry no
  functional information and are removed under the repository's protein-binding policy. The
  underlying interactions are not disputed, and several (KHDRBS1/Sam68, the HOXB-AS3
  peptide, UBQLN2, C9orf72) are discussed above or in the row reasons.

## Open questions recorded in the review

1. Does hnRNP A1's condensate scaffold activity do anything in cells beyond partitioning —
   i.e. is SG assembly or SG material state measurably hnRNPA1-dependent? The reconstitution
   work is strong, the cellular requirement is not established, and this is why
   `GO:0034063` is not proposed.
2. Which pri-miRNAs besides miR-18a does it license, and is the pre-miRNA binding from the
   compendium the same activity?
3. Is the IBMPFD3/ALS20 pathology a gain of fibrillisation or a loss of normal nuclear
   function? UniProt records three distinct disease entries (IBMPFD3, ALS20, MPD3
   [PMID:34722876]) for the same small PrLD region.
