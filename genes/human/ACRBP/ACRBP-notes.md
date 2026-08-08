# ACRBP (Q8NEB7) — review notes

Human ACRBP / sp32 / OY-TES-1 / CT23. Acrosin-binding protein, 543 aa, testis-restricted,
chromosome 12p12-p13.

## What the protein is

ACRBP is an acrosomal matrix protein of the sperm head. It is synthesised as a ~60-kDa
precursor with a cleaved signal peptide and is post-translationally processed to a 32-kDa
mature form by removal of the N-terminal half. The mature form binds the acrosin zymogen
(proacrosin, pro-ACR) and controls when that zymogen becomes active protease.

Two literatures exist and both matter:

1. **Reproductive biology** — pig, mouse, guinea-pig and boar work spanning 1994–2021 that
   established the pro-ACR binding, the processing, the tyrosine phosphorylation during
   capacitation, and the knockout phenotype.
2. **Tumour immunology** — ACRBP is the cancer/testis antigen OY-TES-1 / CT23, discovered
   independently and studied almost entirely as an immunogen and as a knockdown target in
   cancer lines. This literature says essentially nothing about the protein's molecular
   function, and none of it has produced a GO annotation.

The two never merged: the human gene was named and characterised *as a CT antigen*, and all
of its GO annotations come from ortholog transfer out of the reproductive literature.

## Human-specific evidence

The only human primary paper is the cloning/CT-antigen paper.

- Identity of the human gene: [PMID:11248070 "Sequence analysis indicates that OY-TES-1 is
  the human homologue of porcine, guinea pig, and mouse proacrosin binding protein sp32
  precursor"]
- Function stated for the family, in the human paper: [PMID:11248070 "sp32 is located in the
  sperm acrosome and appears to function as a binding protein to proacrosin for packaging and
  condensation of the acrosin zymogen in the acrosomal matrix."]
- Ortholog identity, which is what licenses the ISS transfers: [PMID:11248070 "The deduced
  amino acid sequence of OY-TES-1 shows a high degree of homology with the corresponding
  porcine (81.9%), guinea pig (77.2%), and mouse (75.2%) sp32 precursor product."]
- Processing site, human: [PMID:11248070 "The mature sp32 is produced by posttranslational
  cleavage between 273 arginine and 274 glutamic acid of the precursor molecule."] This
  matches UniProt's `PROPEP 26..273` / `CHAIN 274..543`.
- Secretory targeting: [PMID:11248070 "The amino terminal region is highly hydrophobic,
  suggesting that it serves as a signal sequence."]
- Expression: [PMID:11248070 "OY-TES-1 expression was restricted to testis in normal adult
  tissues, whereas it was detected in a range of different human tumor types."]

There is **no human functional or biochemical assay** of ACRBP. `PE 1: Evidence at protein
level` in UniProt reflects proteomic detection, not a functional experiment. Every functional
GO annotation on Q8NEB7 is ISS or IEA.

Caution recorded for future work: [PMID:11248070 "Southern blot analysis suggests the presence
of two OY-TES-1-related genes in the human genome."] Only one reviewed human ACRBP entry
exists; the second signal is not resolved in the current literature and should not be assumed
to be a functional paralog.

## The core molecular function, from the ortholog literature

- Original characterisation, pig: [PMID:8144514 "Purified sp32 gave a single 32-kDa protein
  band on SDS-polyacrylamide gel electrophoresis and was characterized as a binding protein
  specific for 55-, 53-, and 49-kDa forms of (pro)acrosin."] and the negative half of the
  specificity: [PMID:8144514 "This protein was not capable of binding a 43-kDa acrosin
  intermediate and 35-kDa mature acrosin."]
- Direction of the effect *in vitro*: [PMID:8144514 "sp32 significantly accelerated
  autoactivation of proacrosin at a basic pH in vitro and affected the maturation pathway of
  proacrosin."]
- Proposed role: [PMID:8144514 "The binding of sp32 to proacrosin may be involved in packaging
  the acrosin zymogen into the acrosomal matrix."]
- Direction of the effect *in vivo*, mouse: [PMID:27303034 "The major function of ACRBP-W is
  to retain the inactive status of proacrosin in the acrosome until acrosomal exocytosis."]

So the sign of the regulation is context-dependent — it holds pro-ACR latent inside the
acrosome and accelerates its autoactivation once conditions change. MGI captured only the
positive direction: mouse Acrbp carries `GO:0016504 peptidase activator activity` (ISA,
PMID:8144514, with/from pig Q29016). Human ACRBP has **no molecular-function annotation at
all**, which is the largest single gap in its GO record — the protein is named for an activity
GO does not record for the human gene.

Domain caution: UniProt lists `SUPFAM SSF100895 Kazal-type serine protease inhibitors` for the
fold. ACRBP is *not* reported to inhibit a protease through a Kazal mechanism; it binds the
zymogen and does not bind mature acrosin at all. The fold name must not be read as an activity.

## The isoform question — and why the obvious objection fails

Mouse produces two ACRBP forms by alternative splicing, and the 2016 knockout paper partitions
the phenotype between them:

- [PMID:23426433 "Unlike other mammalian ACRBPs, two forms of Acrbp mRNA-wild-type Acrbp-W and
  variant Acrbp-V5 mRNAs-were generated by alternative splicing of Acrbp in the mouse."]
- [PMID:23426433 "The intron 5-retaining splice variant mRNA produced a predominant form of
  ACRBP, ACRBP-V5, that was present in pachytene spermatocytes and round spermatids, but was
  absent in elongating spermatids."]
- [PMID:23426433 "Glutathione S-transferase pull-down assays revealed that ACRBP-V5 and
  ACRBP-C possess a different domain capable of binding each of two segments in the C-terminal
  region of pro-ACR."]
- [PMID:27303034 "The acrosome malformation was rescued by transgenic expression of ACRBP-V5
  in ACRBP-null spermatids."]
- [PMID:27303034 "Thus, ACRBP-V5 functions in the formation and configuration of the acrosomal
  granule during early spermiogenesis."]

Read together, these say the *acrosome-assembly* half of the mouse phenotype is attributable
to ACRBP-V5, described as absent from other mammals. That is a serious prima facie objection
to the human `GO:0001675 acrosome assembly` ISS/IEA annotations, and I set out to mark them as
over-annotated on that basis.

**The bioinformatics check refuted my own hypothesis.** See
`file:human/ACRBP/ACRBP-bioinformatics/RESULTS.md`:

- Human `ACRBP-204` / `ENST00000536350` is an annotated protein-coding transcript encoding a
  319-aa product that shares the canonical N-terminus at 98.4% identity.
- Its exon chain is the first five canonical exons, with the terminal exon extended 82 bp past
  the exon-5 donor site into intron 5 — the same architecture as mouse `Acrbp-205` /
  `ENSMUST00000112414`, whose terminal exon extends 242 bp into intron 5.
- The protein consequence is the same substitution at the equivalent position: human `SLLQL →
  RYRKF` at 315-319, mouse `SLQQL → RYRKL` at 312-316 (the mouse change is UniProt
  `VSP_051965`/`VSP_051966`, i.e. exactly ACRBP-V5).

One conserved intron-5 read-through event at the sequence level, then, not a rodent invention.

**But the sequence level is only half the objection, and the other half survives.** The 2019
paper — same laboratory, three years after the knockout study, and a paper this review already
cites for the acrosome-reaction mechanism — states the human negative outright in its
introduction: [PMID:30606959 "Porcine, guinea pig, and human spermatogenic cells produce only a
single form of Acrbp (termed Acrbp-W) mRNA, whereas two mRNA forms, wild-type Acrbp-W and intron
5-retaining variant Acrbp-V5 mRNAs, are synthesized by pre-mRNA alternative splicing of the Acrbp
gene in mouse"]. That is an RT-PCR claim about what is transcribed, and it outranks a genome
annotation on precisely that question.

So the honest conclusion is a **discrepancy, not a refutation**: GENCODE annotates
`ENST00000536350`, and the primary literature reports that human spermatogenic cells do not make
the corresponding mRNA. Nobody has looked for the protein. The two claims have never been
reconciled, and reconciling them is the point of the `GO:0001675` knowledge gap in the review.

`GO:0001675 acrosome assembly` is nonetheless ACCEPTed, for a reason that does not depend on the
isoform argument at all: the mouse source annotation is an IMP on a knockout of the **whole gene**,
which ablates both forms, so what transferred is a gene-level requirement for normal acrosome
formation rather than a V5-specific activity. UniProt's curator reading of the same full text also
credits the mature form with partially contributing to acrosomal-granule assembly.

Process note, recorded because it is the kind of error worth remembering: the first draft of this
review concluded that the isoform objection "fails and the term stands", and marked PMID:23426433
`DISPUTED` on the strength of the GENCODE annotation. Both were wrong, and the evidence against
them was in a cached full text this review was already citing four times — found by the PR
reviewer, not by me. A genome annotation does not outrank an expression experiment. The reference
is now `VERIFIED` and the conclusion is scoped to the sequence level.

Consequence for curation: UniProt Q8NEB7 has no `ALTERNATIVE PRODUCTS` section, so there is no
human isoform identifier to put in the review's `isoform:` field even though the mouse function
is isoform-partitioned. This is a concrete UniProt correction to report, and it is why every
human annotation here is left isoform-agnostic.

The two pro-ACR-binding regions map onto this cleanly: human `REGION 26..106` (93.8% identical
to mouse) lies inside the propeptide and inside the V5 span — it is the V5/granule-associated
site; human `REGION 319..427` (73.4% identical) lies in the mature chain — it is the
ACRBP-C/zymogen-retention site.

## Downstream phenotype

- Whole-gene mouse knockout: [PMID:27303034 "ACRBP-null male mice lacking both proteins showed
  a severely reduced fertility, because of malformation of the acrosome."] Both isoforms are
  ablated, so the mouse source annotations for acrosome assembly, spermatid development and
  fertilization (all IMP on PMID:27303034) are gene-level, not isoform-level.
- Mechanism of the subfertility: [PMID:30606959 "These data suggest that male subfertility of
  ACRBP-deficient mice may be attributed to incompleteness of the acrosome reaction rather than
  impairment in sperm migration from the uterus to the oviduct."] with normal motility retained:
  [PMID:30606959 "However, ACRBP-deficient sperm recovered from the oviduct possessed
  morphologically normal head shape and retained normal motility."]
- Boar surface-blocking: [PMID:34086710 "Anti-ACRBP antibodies reduced capacitation and
  spontaneous AR (P<0.05)."] and [PMID:34086710 "The localisation of anti-ACRBP antibodies on
  the sperm head, reduced the ability of the sperm to undergo the AR in response to solubilized
  ZP or by inhibiting the sarco/endoplasmic reticulum Ca2+-ATPase."]

Together these support a role in **regulating the acrosome reaction** (`GO:0060046`), which no
ACRBP entry in any species currently carries. Proposed as a new human annotation at ISS
strength.

- Capacitation-linked phosphorylation, pig: [PMID:15955892 "These results demonstrate that
  sp32, a (pro)acrosin binding protein, is the p32, a tyrosine phosphorylated protein related
  to capacitation."] Pig Q29016 carries `GO:0048240 sperm capacitation` (TAS) on this paper; not
  proposed for human, where there is no evidence and the pig call is author-statement only.
- Maturation dependency: [PMID:22357636 "we report that the sperm fertilization molecule
  acrosin-binding protein (ACRBP)/sp32, which normally undergoes processing from a 58.5 kDa
  precursor to a 27.5 kDa mature form, is not proteolytically processed in PCSK4 null mice and
  thus may be a substrate for PCSK4."] Note the authors' own hedge: [PMID:22357636 "analysis of
  the ACRBP sequence did not show a strong consensus site for convertase cleavage, suggesting
  that ACRBP processing may require the activity of a yet unknown enzyme"]. ACRBP is the
  substrate here, not the agent — no GO annotation for ACRBP follows.

## WITH/FROM resolution (every accession in the GOA TSV)

| Accession | Identity | Verdict |
|---|---|---|
| `UniProtKB:Q29016` | ACRBP_PIG, *Sus scrofa* ACRBP | true 1:1 ortholog, 81.9% identical to human; legitimate donor |
| `UniProtKB:Q3V140` | ACRBP_MOUSE, *Mus musculus* Acrbp | true 1:1 ortholog, 75.2% identical to human; legitimate donor |
| `MGI:MGI:1859515` | mouse Acrbp | same gene as Q3V140 |
| `PANTHER:PTN001085565` | ACRBP node of PTHR21362 | family has one member per mammalian genome; no paralog expansion |
| `ensembl:ENSMUSP00000085632` | mouse Acrbp protein | same gene as Q3V140 |
| `UniProtKB-SubCell:SL-0007` | "Acrosome" | maps to GO:0001669 |
| `UniProtKB-SubCell:SL-0243` | "Secreted" | maps to GO:0005576 |

No paralog transfer anywhere. PANTHER PTHR21362 has 904 members across 1596 taxa but only one
reviewed protein per mammalian genome (pig, mouse, rat, guinea pig, human), so
`WRONG_ORTHOLOG_OR_PARALOG` is not available as a failure mode for any of these rows.

The IBA (`GO_REF:0000033`) is **not** self-referential: its with/from cites mouse and pig, not
human ACRBP. It is the PAN-GO annotation counted by UniProt's `PAN-GO; Q8NEB7; 1 GO annotation`
cross-reference.

## Family-wide GO state (QuickGO, checked for this review)

Annotations on all five reviewed ACRBP orthologs, to establish what is and is not already
recorded before proposing anything new:

| Species | MF annotations | Experimental (non-ISS/ISO/IBA/IEA) rows |
|---|---|---|
| human Q8NEB7 | **none** | GO:0005634 HDA only |
| mouse Q3V140 | GO:0016504 (ISA), GO:0005515 (IPI) | GO:0001675/0007286/0009566 IMP, GO:0001669 IDA |
| pig Q29016 | GO:0005515 (IPI ×2, partner P08001 = pig acrosin) | GO:0001669 IDA, GO:0002080 IDA, GO:0005576 IDA+EXP, GO:0048240 TAS |
| rat Q6AY33 | **none** | none — all 16 rows are ISS/ISO/IBA/IEA |
| guinea pig Q60485 | **none** | none — all 10 rows are ISS/IEA |

So the entire experimental base for this family is mouse and pig, and four of the five entries
have no molecular function at all. Direct queries confirm that **GO:0035375 zymogen binding,
GO:0061135 endopeptidase regulator activity, GO:0097341 zymogen inhibition and GO:0060046
regulation of acrosome reaction each return zero annotations across all five orthologs** — so
all four proposed rows are genuinely new to the family, not duplicates of something already
recorded elsewhere in it.

Two further points from that table. The mouse `GO:0005515` IPI (PMID:11164898) cites Q08279
(guinea-pig IGF2) and Q6UW60 (human PCSK4) as partners, neither of which is proacrosin; PCSK4 is
the convertase of PMID:22357636, and the IGF2 entry looks like a with/from artefact. Neither was
used here. And the single pig `GO:0002080` IDA has propagated by ISS
(`GO_REF:0000024`, with/from `UniProtKB:Q29016`) to **four** entries — human Q8NEB7, mouse Q3V140,
rat Q6AY33 and guinea pig Q60485 — plus a further rat ISO row (`GO_REF:0000121`, with/from
`RGD:14255780`). So the MODIFY argued below is not a one-gene correction: one
resolution-limited immunofluorescence call is currently the sole basis for acrosomal-membrane
localisation across the whole reviewed family.

## Annotations that do not survive review

**`GO:0002080 acrosomal membrane` (ISS from pig Q29016)** — traced to pig's own
`GO:0002080 ... IDA PMID:15955892`, an indirect-immunofluorescence localisation. Light
microscopy of the acrosome cannot separate the acrosomal matrix from the acrosomal membrane.
The protein has no basis for residing in a bilayer: all five reviewed orthologs have a cleaved
signal peptide and no transmembrane, intramembrane or lipidation feature, and sp32 was
originally purified as a soluble protein from acid extracts of ejaculated sperm
[PMID:8144514 "An acrosomal protein, sp32, was completely purified from acid extracts of
ejaculated porcine sperm."]. `GO:0043159 acrosomal matrix` is both more accurate and more
informative, and is the term the primary literature actually uses
[PMID:11248070 "packaging and condensation of the acrosin zymogen in the acrosomal matrix"].
→ MODIFY to `GO:0043159`.

**`GO:0005634 nucleus` (HDA, PMID:21630459)** — from a human sperm-nucleus proteome. The
authors claim high purity, [PMID:21630459 "sperm nuclei were obtained through CTAB treatment
and isolated to over 99.9% purity without any tail fragments, acrosome or mitochondria as
assessed by optical microscopy and transmission electron microscopy."] but ACRBP is a
signal-peptide-bearing secretory-pathway protein and the acrosome physically caps the sperm
nucleus; carry-over is the parsimonious reading. The dataset is also broad —
[PMID:21630459 "More than half (52.6%) of the proteins had not been detected in the previous
human whole sperm cell proteome reports."] and it reports "zinc fingers and transcription
factors, so far not known to be associated with the sperm chromatin". The same PMID has been
handled as an over-annotation for other genes in this repository (AAAS, ACADS, ACADM).
→ MARK_AS_OVER_ANNOTATED, not REMOVE: the peptide detection itself is not in dispute.

## Process notes

- `self_evaluation_pairwise: win` and clear trust gates on the affinage record; all 12 citations
  are numeric PMIDs. Its narrative
  is accurate on the mechanism, and its own GO grounding (`GO:0098772`, `GO:0140313`,
  `GO:0031410`, `GO:0005886`) was not imported: `GO:0005886 plasma membrane` rests only on the
  boar antibody-accessibility experiment, and `GO:0140313 molecular sequestering activity` frames
  the activity as sequestration when the primary papers describe modulation of zymogen
  autoactivation in both directions. `GO:0061135 endopeptidase regulator activity` is used
  instead — it is a descendant of the `GO:0098772` that affinage proposed, and it is sign-neutral,
  which the evidence requires.
- The GOA TSV has 14 rows but 13 distinct annotations: `GO:0005576 extracellular region` ISS
  from `UniProtKB:Q29016` under `GO_REF:0000024` appears twice, dated 2016-05-24 and 2020-02-06.
  The seeder de-duplicated it; one reviewed entry covers both rows.
- Working hypothesis abandoned mid-review: that `GO:0001675 acrosome assembly` should be marked
  over-annotated because it derives from a rodent-specific isoform. The bioinformatics check was
  written to support that and instead falsified it. The annotation is accepted.
