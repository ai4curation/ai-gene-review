# P. putida KT2440 enolase — plasminogen-binding determinants vs pathogen enolases

## Purpose

UniProt attaches `Secreted`/`Cell surface` (SL-0243 → GO:0005576) to essentially every
bacterial enolase through the HAMAP family rule **MF_00318**, because enolase moonlights as a
surface plasmin(ogen) receptor in numerous pathogens. The PSEPK `eno` review flags the
resulting annotation as an over-annotation, but on an **argument from absence**: "no
organism-specific surface/secretome evidence was found".

This analysis replaces that with a positive, checkable test. If surface display is a
clade-specific accessory role rather than a family-wide property, the sequence determinants
that mediate it should be recognisable in the pathogens that carry the role and degenerate or
absent in *P. putida*.

Two determinants are described for pathogen enolases:

1. an **internal** nine-residue plasmin(ogen)-binding motif identified in surface-displayed
   alpha-enolase of *Streptococcus pneumoniae* (Bergmann et al. 2003, PMID:12828639), and
2. **C-terminal lysines**, the feature classically invoked for plasminogen binding.

## Method

`check_plasminogen_motif.py` fetches sequences from UniProt, locates the pneumococcal motif in
the reference (Q97QS2, *S. pneumoniae* TIGR4), maps that region onto each query by global
pairwise alignment (Biopython `Align.PairwiseAligner`; match +2, mismatch −1, gap-open −5,
gap-extend −0.5), and reports the mapped residues, the lysine counts, and the C-terminal
residues. *S. aureus* N315 (P99088) is included as a second pathogen control.

Reproduce with `uv run --with biopython python check_plasminogen_motif.py`. The script prints
what it finds and hardcodes no conclusion.

## Results

```
Reference Q97QS2 (S. pneumoniae TIGR4); length 434
  motif FYDKERKVYD found at residues 248-257
  reference C-terminal 6 residues: FYNLKK

Q88MF9 (P. putida KT2440 (the gene under review)); length 429
  identity to reference: 260/423 = 61.5%
  motif region maps to residues 252-263
    reference : FYDKERKVYD
    query     : FYGKYNLSGE
    identical : 3/10
    lysines in query region: 1 (reference has 2)
  C-terminal 6 residues: RAEFRG

P99088 (S. aureus N315 (second pathogen control)); length 434
  identity to reference: 354/432 = 81.9%
  motif region maps to residues 250-257
    reference : FYERKVYD
    query     : FYENGVYD
    identical : 6/8
    lysines in query region: 0 (reference has 1)
  C-terminal 6 residues: FYNLDK
```

## Interpretation

**P. putida KT2440 enolase lacks both plasminogen-binding determinants.**

- The internal motif is **degenerate**: `FYGKYNLSGE` against the pneumococcal `FYDKERKVYD`,
  3/10 identical, and lysine-depleted (1 vs 2). The conserved `FY` dipeptide that anchors the
  alignment is retained — this is the same structural position, not a mis-mapping — but the
  lysine-bearing core that does the plasminogen binding is not.
- The **C-terminus carries no lysines at all**: `RAEFRG`. The pneumococcal enolase ends
  `FYNLKK` and *S. aureus* ends `FYNLDK`, both retaining terminal lysine.

The *S. aureus* control is informative in a way that was not anticipated: its internal motif is
also imperfect (6/8) while its C-terminal lysine is intact. So the two determinants vary
somewhat independently across pathogens, and *P. putida* is distinguished by lacking **both**.

This supports the review's `MARK_AS_OVER_ANNOTATED` verdict on GO:0005576, and upgrades its
basis from absence of evidence to positive sequence evidence: the specific mechanism that the
HAMAP rule generalises from is not present in this protein.

## Limitations

- This is a sequence-level argument about **one known mechanism**. Absence of the pneumococcal
  determinants does not prove absence of surface localization; non-classical secretion could in
  principle use determinants not tested here, and *P. putida* enolase could reach the surface
  without binding plasminogen at all.
- Motif mapping is by pairwise global alignment against a single reference. A profile built
  from many surface-displaying enolases would be a stronger test, as would a check of whether
  *Pseudomonas* species with documented surface enolase (if any) differ from KT2440.
- No secretome or surface-proteomics data were consulted here; that evidence class would be
  decisive either way and is not addressed by sequence.

## Data provenance

Sequences fetched live from the UniProt REST API: Q97QS2 (*S. pneumoniae* TIGR4), Q88MF9
(*P. putida* KT2440, the reviewed gene), P99088 (*S. aureus* N315). Motif definition from
PMID:12828639.

---

# Cross-ortholog GO audit — verifying the blinded OpenScientist run

## Purpose

A blinded OpenScientist run was launched on the same hypothesis ("eno has extracellular
region, GO:0005576") with the analysis above withheld, so that its conclusion could be
scored against a genuine holdout. The run is at
`../eno-hypotheses/function-hypothesis-go-0005576/openscientist.md`.

It reached the same verdict — over-annotated — and, working from sequence alone, independently
recovered the C-terminal result above: it reports Q88MF9 ending `…RGRAEFRG` with **no C-terminal
lysine**, matching the `RAEFRG` found here. It did not attempt the internal pneumococcal motif
and says so in its Limitations, so the two analyses are complementary on that point.

Its headline *new* argument was a cross-ortholog audit concluding that the extracellular and
cell-surface GO terms are **anti-correlated with real biology** — applied by rule to enolases
with no surface evidence, and *absent* from enolases where surface display is experimentally
established. That is a strong, checkable claim about public records, so `check_ortholog_go_audit.py`
checks it: for each accession in the report's table it asks UniProt what the protein actually is,
and QuickGO which of GO:0005576 and GO:0009986 it carries.

## Method

`check_ortholog_go_audit.py` queries the UniProt REST API for protein name and organism, and the
QuickGO annotation API for the two cellular-component terms with evidence codes and references.
It hardcodes no expected answer and prints whatever the APIs return.

Reproduce with `uv run --with requests python check_ortholog_go_audit.py`.

## Results

```
Q88MF9  claimed: P. putida KT2440 enolase (the query)
        actual: Enolase | Pseudomonas putida (strain ATCC 47054 ...)
        GO:0005576  IEA   GO_REF:0000044
        GO:0009986  IEA   GO_REF:0000120

P0A6P9  claimed: E. coli enolase
        actual: Enolase | Escherichia coli (strain K12)
        GO:0005576  EXP   PMID:15003462
        GO:0005576  IEA   GO_REF:0000044
        GO:0009986  IEA   GO_REF:0000120

P64075  claimed: M. tuberculosis enolase
        actual: Enolase | Listeria innocua serovar 6a (strain ATCC BAA-680 / CLIP 11262)
        GO:0005576  IEA   GO_REF:0000120
        GO:0009986  IEA   GO_REF:0000120

P77972  claimed: Bifidobacterium enolase
        actual: Enolase | Synechocystis sp. (strain ATCC 27184 / PCC 6803 / Kazusa)
        GO:0005576  IEA   GO_REF:0000044
        GO:0009986  IEA   GO_REF:0000120

P9WNV9  claimed: M. tuberculosis enolase   <-- IDENTITY MISMATCH
        actual: Chaperone protein DnaJ 1 | Mycobacterium tuberculosis (H37Rv)
        no GO:0005576 / GO:0009986 annotation

Q8DR60  claimed: S. pneumoniae enolase   <-- IDENTITY MISMATCH
        actual: Endo-alpha-N-acetylgalactosaminidase | Streptococcus pneumoniae (R6)
        no GO:0005576 / GO:0009986 annotation

P0A4G2  claimed: S. aureus enolase   <-- IDENTITY MISMATCH
        actual: Manganese ABC transporter substrate-binding lipoprotein PsaA
                | Streptococcus pneumoniae serotype 4 (TIGR4)
        no GO:0005576 / GO:0009986 annotation

Enolases of the organisms the report said lack the terms:

Q97QS2  actual: Enolase | Streptococcus pneumoniae serotype 4 (TIGR4)
        GO:0005576  IEA   GO_REF:0000044
        GO:0009986  EXP   PMID:11442827
        GO:0009986  EXP   PMID:12435062
        GO:0009986  IEA   GO_REF:0000120

P99088  actual: Enolase | Staphylococcus aureus (strain N315)
        GO:0005576  IEA   GO_REF:0000044
        GO:0009986  IEA   GO_REF:0000120
```

## Interpretation

**The anti-correlation does not exist. It is an artifact of misidentified accessions.**

Of the seven rows in the report's table, only two are fully correct — the query itself and
*E. coli*. Three cite proteins that are not enolase at all: `P9WNV9` is the *M. tuberculosis*
DnaJ1 chaperone, `Q8DR60` is a pneumococcal endo-alpha-N-acetylgalactosaminidase, and `P0A4G2`
is pneumococcal PsaA, a manganese ABC transporter lipoprotein — and it is labelled
*S. aureus* when it is *S. pneumoniae*. Two more are enolases of the wrong organism:
`P64075` is *Listeria innocua*, not *M. tuberculosis*; `P77972` is *Synechocystis*, not
*Bifidobacterium*.

Those three non-enolases are precisely the rows carrying "no CC term", which is what generated
the apparent anti-correlation. They have no surface GO terms because they are unrelated
proteins that the HAMAP enolase rule never touched.

Looked up properly, the enolases of the two organisms said to lack the terms both carry them:
*S. pneumoniae* TIGR4 enolase (Q97QS2) and *S. aureus* N315 enolase (P99088) each have
GO:0005576 by `IEA / GO_REF:0000044`, exactly as *P. putida* does.

**The corrected pattern is uniformity, not anti-correlation** — and it supports the same verdict
by a cleaner argument. Every enolase checked, across six genera spanning soil saprophytes,
enteric bacteria, cyanobacteria and pathogens, carries GO:0005576 from the same rule. A term
applied to every member of a family regardless of that member's biology carries **no
organism-specific information**, which is the essence of the over-annotation. The pathogens
where surface enolase is real are not distinguished from *P. putida* by this annotation, so the
annotation cannot be evidence about *P. putida*.

One further correction: the report states that no experimental GO:0005576 annotation exists on
any enolase examined. *E. coli* enolase carries `GO:0005576 EXP PMID:15003462` — a paper asking
whether 2-phosphoglycerate-dependent automodification of bacterial enolases is implicated in
their export. So non-classical enolase export is an active question with at least one
experimental GO annotation behind it, and the argument here should stay organism-specific: no
*P. putida* surface or secretome evidence, and both plasminogen-binding determinants absent in
this protein. It should not be generalised into a claim that bacterial enolases are never
exported.

## What the blinded comparison showed

- **Verdict: converged.** Both independently called GO:0005576 over-annotated for this organism,
  by the same route — a HAMAP `MF_00318` rule propagation with no *P. putida* evidence behind it.
- **One computed result: converged exactly.** The absent C-terminal lysine was found by both,
  from sequence, without either seeing the other.
- **The novel argument: refuted.** The run's most striking contribution, and the one a curator
  would have been most tempted to adopt, is the one that failed verification. Its verdict was
  right for reasons partly wrong.

The practical lesson is narrow and reusable: a generated table of accessions is a claim about
identity, and identity is cheap to check. The verdict survived; the evidence offered for it did
not, and nothing from that table should be cited without resolving each accession first.
