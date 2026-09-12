# FEN1 (human, UniProt P39748) — curation notes

## Data provenance for this review

- `FEN1-uniprot.txt`, `FEN1-goa.tsv`: fetched via `just fetch-gene human FEN1`. 97 GOA rows collapsed
  into 94 seeded annotations.
- Publications: all 31 PMIDs cited by GOA are cached under `publications/`. Many are **abstract-only**
  (`full_text_available: false`), including PMID:7961795, PMID:8621570, PMID:11986308, PMID:8131753,
  PMID:8007985, PMID:9778254, PMID:18499658, PMID:12427278. Reviews were written from the abstracts plus
  the curated UniProt entry; where the abstract could not settle a point, the curator's call was deferred to.
- **Deep research: no usable output.** `just deep-research-falcon human FEN1 --fallback perplexity-lite`
  failed twice. The falcon provider returned HTTP 402 from
  `api.platform.edisonscientific.com` (no credits) and the perplexity provider is not configured in this
  environment (`Provider 'perplexity' not available. Available: falcon, asta, openscientist`). The asta
  provider ran successfully and produced `FEN1-deep-research-asta.md`, but its retrieval is **entirely
  off-target**: all 19 retrieved papers are unrelated (M. tuberculosis annotation, LIPID MAPS, avian
  immunome DB, NK-cell proteomics, etc.) and none concern FEN1. That file is retained as the genuine
  provider artifact but contributed **nothing** to this review and should not be read as literature support.
  A future pass with a working provider would be worthwhile.
- Note: `uvx` in this environment resolves Python 3.11, but `deep-research-client` requires >=3.12.
  Setting `UV_PYTHON=3.12` is needed before any `just deep-research-*` recipe will run at all.

## Function summary as used for the review

FEN1 is a structure-specific, Mg2+-dependent nuclease of the XPG/RAD2 family with three
inter-related activities from a single two-metal-ion active site:

1. **5'-flap endonuclease** — threads onto the free 5' end of a displaced flap, tracks to the base, and
   incises one nucleotide into the annealed duplex of a *double*-flap substrate.
   [PMID:8131753 "The enzyme described here, flap endonuclease-1 (FEN-1), cleaves DNA flap strands that
   terminate with a 5' single-stranded end."]
   Specificity is strict: Holliday junctions and incomplete flaps are not cleaved
   [PMID:8131753 "Other branch structures, including Holliday junctions, are also not cleaved by FEN-1."].
2. **5'→3' exonuclease**, duplex-specific
   [PMID:8131753 "In addition to endonuclease activity, FEN-1 has a 5'-3' exonuclease activity which is
   specific for double-stranded DNA."].
3. **RNase H / RNA-DNA hybrid ribonuclease**
   [PMID:7961795 "DNase IV removes single-stranded 5' regions from splayed-arm DNA structures by
   endonucleolytic incision at the bifurcation point and possesses RNase H activity"].

Active-site chemistry and substrate engagement are mutationally separable:
[PMID:8621570 "Mutants D34A, D86A, and D181A lost their cleavage activity completely but retained
substrate binding ability"] versus
[PMID:8621570 "Loss of both binding and cleavage competency for the flap substrate by mutants E156A,
G231A, and D233A suggests that these amino acids are involved in substrate binding."].
R70 selectively controls the exonuclease mode
[PMID:11986308 "Mutation of the Arg-70 significantly reduced flap endonuclease activity and eliminated
exonuclease activity."].

PCNA is the targeting/stimulating partner and switches the enzyme between modes
[PMID:9778254 "The conserved FEN-1 C terminus binds proliferating cell nuclear antigen (PCNA) and
positions FEN-1 to act primarily as an exonuclease in DNA replication, in contrast to its endonuclease
activity in DNA repair."].

R-loop role (basis for the proposed new GO:0062176 annotation):
[PMID:36672839 "We showed that FEN1 specifically employed its endonucleolytic cleavage activity to remove
the RNA strand in an R-loop during BER."] and
[PMID:36672839 "We further demonstrated that FEN1 was recruited to R-loops in normal human fibroblasts and
senataxin-deficient (AOA2) fibroblasts, and its R-loop recruitment was significantly increased by
oxidative DNA damage."].

Mitochondrial pool:
[PMID:18995831 "We further demonstrate that hDNA2 and flap endonuclease 1 synergistically process
intermediate 5' flap structures occurring in DNA replication and long-patch base excision repair (LP-BER)
in mitochondria."]. UniProt additionally assigns the alternatively initiated isoform FENMIT (P39748-2) to
the mitochondrion and records that it has no nuclease activity but binds RNA flaps and R-loops.

## Decisions that needed judgement

**GO:0016020 membrane (HDA, PMID:19946888) — REMOVE.** The only REMOVE applied to a
localization annotation. FEN1 has no transmembrane segment, signal peptide or lipid anchor in UniProt.
The source study is explicit that its own dataset is heavily contaminated with non-membrane proteins
[PMID:19946888 "On the basis of the presence of transmembrane regions or evidence of posttranslational
modifications and prediction algorithms, approximately 40% of the identified proteins were predicted as
plausible membrane proteins."].

**GO:0003684 damaged DNA binding (TAS, PMID:8007985) — REMOVE.** The cited paper cloned the human
homolog of *S. pombe* rad2 and showed UV-sensitivity complementation; it contains no damaged-DNA-binding
experiment. Mechanistically FEN1 recognizes *branch geometry*, not chemically damaged bases.

**GO:0009650 UV protection (TAS, PMID:8007985) — MARK_AS_OVER_ANNOTATED, not REMOVE.** There *is*
evidence, but it is heterologous complementation of a fission yeast phenotype
[PMID:8007985 "Human cDNA has 55% amino acid sequence identity to the rad2 gene and is able to complement
the UV sensitivity of the rad2 null mutant."]. Nucleotide excision repair in human cells is carried out by
the paralog XPG/ERCC5, so this annotation risks conflating family members.

**GO:0007613 memory (IEA, GO_REF:0000107) — MARK_AS_OVER_ANNOTATED.** Projected from rat Fen1
(UniProtKB:Q5XIP6) by Ensembl Compara. An organism-level behavioural phenotype is not a function of a
housekeeping nuclease; any link would be a distal consequence of impaired genome maintenance in neurons.

**GO:0000724 DSB repair via homologous recombination (TAS, Reactome:R-HSA-5693538) — MODIFY to
GO:0097681.** The Reactome reaction that actually involves FEN1 in that hierarchy is
R-HSA-5687664, "FEN1 cleaves displaced ssDNA flaps during MMEJ" — microhomology-mediated (alternative)
end joining, not HR proper. FEN1 has no strand-invasion or resection activity.

**All 20 `GO:0005515 protein binding` IPI annotations — MARK_AS_OVER_ANNOTATED, none removed.** Per
project guidelines the term is uninformative, but several of these record genuinely important
partnerships (PCNA, WRN, BLM, MUS81, DDX11, WDR4, EP300, POLB). The functional content is captured by
GO:0017108. Worth flagging upstream: **GO has no PCNA-binding molecular function term**, so the single
most functionally decisive FEN1 interaction is only expressible as "protein binding".

**Generic parents left as ACCEPT rather than MODIFY.** `GO:0006281 DNA repair` (IBA and TAS) was kept,
because FEN1 genuinely acts in several repair sub-pathways (LP-BER, MMEJ, oxidative damage processing),
so the grouping term is right for this gene. By contrast `GO:0006260 DNA replication` was MODIFYed to
GO:0033567, because the replication role is confined to one pathway.

**GO:0030145 manganese ion binding (IBA) — MARK_AS_OVER_ANNOTATED.** UniProt lists only Mg2+ as the
cofactor; Mn2+ reflects in vitro metal substitution common to this nuclease fold.

## Action tally

95 annotations (94 from GOA + 1 proposed NEW):
ACCEPT 54 · MARK_AS_OVER_ANNOTATED 23 · MODIFY 9 · KEEP_AS_NON_CORE 6 · REMOVE 2 · NEW 1.
