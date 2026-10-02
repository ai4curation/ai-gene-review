# TMEM187 review notes

## Why this gene was selected

TMEM187 (formerly CXorf12/ITBA1) is a gene whose *name* says only that it is a membrane protein, and
until 2026 that was the whole of what was known. GOA carries three CC rows and a `GO:0005515 protein
binding` from a single binary-interactome screen - no biological process, no molecular function beyond
bare binding. A 2026 Blood paper supplies a cellular localisation and a biological role, but the
molecular function is still not determined, and the temptation here is to invent one.

## What the 2026 paper establishes

[PMID:41824385 "Here, we identify human TMEM187, a Golgi transmembrane protein of unknown function, as a
novel negative regulator of erythropoiesis."]

Localisation, stated more precisely in the body than in the abstract:
[PMID:41824385 "We found that TMEM187, primarily localized to the trans-Golgi network, interacts with
RAB11A, one of the members of the Rab (small guanine triphosphatases [GTPases]) protein family, and
modulates the endosomal vesicle release from the Golgi."]. The topology is six transmembrane helices,
consistent with the UniProt record (TRANSMEM 8-28, 43-63, 88-108, 113-133, 140-162, 190-210):
[PMID:41824385 "TMEM187 encodes a 261-amino-acid, 6-transmembrane protein located on chromosome Xq28. The
precise function of TMEM187 remains unknown."]

Biological role, with loss-of-function and gain-of-function in three systems:
[PMID:41824385 "Lack of TMEM187 in cell models initiates erythropoiesis without the normal induction
protocol and accelerates iron uptake."],
[PMID:41824385 "In zebrafish embryos, tmem187 deletion leads to enhanced early erythropoiesis, although
this phenotype is later compensated"], and - the cleanest test, since mice have no endogenous orthologue -
[PMID:41824385 "whereas hematopoietic stem cell expression of human TMEM187 in mice, which lack a
homologous gene endogenously, results in compromised erythropoiesis and moderate anemia"].
Summary: [PMID:41824385 "Together, we have demonstrated that TMEM187 acts as a novel negative regulator of
erythroid differentiation and maturation."]

Mechanism: [PMID:41824385 "Mechanistically, we demonstrate that TMEM187 interacts with RAB11A to restrain
endosomal recycling by interfering with RAB11A-GRAB association, involved with endosomal vesicle back to
the plasma membrane, that activates RAB11A."] and
[PMID:41824385 "Consequently, TMEM187 modulates TfR1 recycling to the cell membrane to fine-tune iron
uptake efficiency for erythropoiesis."] The binding is nucleotide-state-selective:
[PMID:41824385 "Interestingly, we found that TMEM187 preferentially interacts with GDP-bound RAB11A (S25N)."]

## Why I did not assert a molecular function

The CC and BP claims are reasonably clear. The MF is not, and the right response is to say so rather than
to reach for a plausible-sounding term.

What is actually demonstrated at the molecular level is one thing: TMEM187 binds RAB11A, preferentially in
its GDP-bound state, by co-immunoprecipitation in HEK293 and K562 cells. That supports `GO:0031267 small
GTPase binding` and nothing beyond it. Everything past that point is inference:

- **Not an adaptor.** No cargo has been shown to bind TMEM187, and TfR1 is affected downstream of RAB11A,
  not by contact with TMEM187.
- **Not a cargo receptor.** TfR1's behaviour changes because RAB11A activation changes; there is no
  evidence of TMEM187-TfR1 binding.
- **Not demonstrated to be a GEF inhibitor.** The competition model (TMEM187 occupying GDP-RAB11A so that
  the GEF GRAB cannot reach it) fits the data, but the paper itself flags that this preference runs
  opposite to what was reported for GRAB in axon outgrowth, no reconstituted nucleotide-exchange assay is
  presented, and the competition is inferred from colocalisation and expression changes rather than
  measured directly.
- **Not a transporter or channel**, despite six TM helices: there is no permeation or transport assay, and
  the protein has no recognisable transporter signature - Pfam PF15100 is a family of its own, and the
  PANTHER family PTHR15066 contains only TMEM187 itself.

So `core_functions` asserts locations and processes and deliberately asserts **no** `molecular_function`.
Per CLAUDE.md, an omitted id says "not established"; a wrong id says something false in a machine-readable
field that other tooling will believe. The RAB11A binding is instead recorded where it belongs, as a
curatable `GO:0031267` annotation in `existing_annotations`, and the missing activity is written up as a
`MF_DARK` knowledge gap.

## A caution about the rest of the TMEM187 literature

Searching PubMed for TMEM187 returns mostly two things that are not about TMEM187's function: Xq28
fine-mapping studies of systemic lupus erythematosus, where TMEM187 is one of several genes in a linkage
block around IRAK1/MECP2 and is not itself implicated (e.g. PMID:22904263), and machine-learning
"biomarker" papers that list TMEM187 among five genes correlated with osteoporosis. Neither supports any
GO annotation, and neither is cited here.

## Curation position taken

- `GO:0030133` transport vesicle (IBA + IDA) → **ACCEPT**. Correct in kind. The IBA's WITH/FROM is
  `PANTHER:PTN001030718|UniProtKB:Q14656`, i.e. it is seeded by this gene's own IDA - which per project
  guidance is expected and not circular. Noted in the reason that `GO:0005802 trans-Golgi network` is now
  the more precise compartment and is proposed as an addition rather than a replacement.
- `GO:0016020` membrane (IEA) → **MODIFY** to `GO:0032588 trans-Golgi network membrane`; TMEM187 is a
  six-pass protein of a specific membrane.
- `GO:0005515` protein binding (IPI) → **MARK_AS_OVER_ANNOTATED**, replaced by small GTPase binding.
- New: `GO:0031267` small GTPase binding, `GO:0005802` trans-Golgi network, `GO:0001920` negative
  regulation of receptor recycling, `GO:0045647` negative regulation of erythrocyte differentiation.

## Open question for experts

Does TMEM187 inhibit GRAB-catalysed nucleotide exchange on RAB11A directly? That is the single experiment
that would convert the current binding annotation into a real molecular function - and, if it failed,
would send the field looking for a different activity for a six-pass Golgi protein.
