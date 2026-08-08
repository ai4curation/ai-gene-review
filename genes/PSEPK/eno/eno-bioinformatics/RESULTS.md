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
