# Provenance: the zinc-finger alternative for ADNP2 DNA binding

Run 2026-11-23 in the job's `execute_code` Python executor. Sources: UniProt REST
(`rest.uniprot.org/uniprotkb/{acc}.json?fields=sequence,ft_zn_fing`), the UniProt search endpoint for
the human C2H2 background, the InterPro API
(`ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/`), and the AlphaFold DB API.

## Why this analysis

The seed context states that ADNP2 "carries a homeodomain and nine C2H2 zinc fingers with intact
zinc-coordinating residues". Iterations 1 and 2 showed the homeodomain cannot read DNA bases. If the
zinc-finger array were competent, GO:0003677 could be re-grounded on the fingers instead of removed.
Kaaij et al. (PMID 31491387) describe ChAHP as "a distinct zinc-finger protein complex", which makes
the fingers the obvious competing module. This cell tests both halves: are the nine fingers intact,
and do they carry base-reading chemistry.

## Method

Each UniProt `ZN_FING` feature interval was padded by 4 residues either side and searched for the
canonical pattern `C-x(2,4)-C-x(12)-H-x(3,5)-H`, falling back to a permissive
`C-x(1,5)-C-x(9,15)-H-x(2,6)-H`. The recognition positions -1, +2, +3 and +6 were read from the
C2-to-H1 spacer. The mapping was derived from Zif268 finger 1, whose spacer `DRRFSRSDELTR` places the
known contact residues R(-1), D(+2), E(+3), R(+6) at spacer indices 6, 8, 9 and 12, so for a spacer of
length L the positions are L-6, L-4, L-3 and L.

Background: the 400 reviewed human proteins returned by `xref:pfam-PF00096 AND organism_id:9606 AND
reviewed:true` (UniProt reports 681 in total, so this is the first page, not the whole set), restricted
to features described as C2H2-type. That gives 3566 fingers across 400 proteins.

## Bug found and fixed

A first pass located the zinc-coordinating residues by taking the first two `C` and the first `H`
inside the matched substring. That is wrong in two situations, and both occur in ADNP2:

- An extra Cys next to C1. ADNP2 ZF1 came out as `C-x(0)-C-x(15)-H`, which is not what the regex
  matched.
- A His inside the 12-residue spacer. ADNP2 ZF7 came out as `C-x(2)-C-x(4)-H-x(12)-H` with
  recognition quadruplet `LCPF`, scoring 0.00 for base-reading chemistry.

The corrected version pins C1, C2, H1 and H2 with regex capture groups, so their positions are exact.
ZF1 becomes `C-x(3)-C-x(12)-H-x(4)-H` and ZF7 becomes `C-x(2)-C-x(12)-H-x(4)-H` with quadruplet
`DKGE`. The uncorrected numbers (ADNP2 mean base-reading fraction 0.469, 9.8th percentile) are
discarded. `provenance/plot_7.png` and `provenance/plot_8.png` are from the buggy pass and are
superseded by `provenance/plot_9.png`.

## Output, corrected pass

```
Corrected per-finger parse. spacing = (C-x?-C, C-x?-H, H-x?-H); canonical is (2-4, 12, 3-5)

ADNP2 (Q6IQ32), 9 annotated zinc fingers
   #  range        UniProt description        canonical  spacing       recog(-1,+2,+3,+6)
   1    73-96    C2H2-type 1                 True       (3, 12, 4)    VTSN
   2   106-128   C2H2-type 2; degenerate     False      (2, 11, 4)    QKVR
   3   155-178   C2H2-type 3; degenerate     True       (2, 12, 4)    LYSK
   4   215-240   C2H2-type 4                 False      (2, 12, 6)    SDAY
   5   694-716   C2H2-type 5; degenerate     False      (2, 11, 6)    PNVV
   6   747-768   C2H2-type 6; degenerate     False      (4, 9, 3)     SEEH
   7   770-793   C2H2-type 7                 True       (2, 12, 4)    DKGE
   8   875-898   C2H2-type 8                 True       (2, 12, 5)    TEAL
   9   913-937   C2H2-type 9; degenerate     False      None          None
  canonical C-x(2,4)-C-x(12)-H-x(3,5)-H: 4 of 9

ADNP (Q9H2P0), 9 annotated zinc fingers
   1    74-97    C2H2-type 1                 True       (3, 12, 4)    FSAS
   2   107-129   C2H2-type 2; atypical       False      (2, 11, 4)    DKTT
   3   165-188   C2H2-type 3                 True       (2, 12, 4)    LEIK
   4   221-244   C2H2-type 4                 True       (2, 12, 4)    SEAQ
   5   447-469   C2H2-type 5; atypical       False      (2, 11, 4)    PNVV
   6   489-510   C2H2-type 6; atypical       False      (2, 11, 3)    PDTN
   7   512-535   C2H2-type 7                 True       (2, 12, 4)    DEKA
   8   622-647   C2H2-type 8; atypical       False      (2, 14, 4)    IDAH
   9   662-686   C2H2-type 9; atypical       False      (2, 15, 2)    TSTL
  canonical C-x(2,4)-C-x(12)-H-x(3,5)-H: 4 of 9

human C2H2 background: 400 proteins, 3566 recognition quadruplets
per-protein fraction of canonical fingers: mean 0.933, median 1.000, sd 0.114
  ADNP2  fraction canonical = 0.444  -> percentile 0.8, z = -4.28
  ADNP   fraction canonical = 0.444  -> percentile 0.8, z = -4.28

fraction of the four recognition positions with base-reading chemistry (R K N Q D E S T H)
  background per finger: mean 0.738, sd 0.219 (n=3566)
  ADNP2  ZF1=VTSN(0.75)  ZF2=QKVR(0.75)  ZF3=LYSK(0.50)  ZF4=SDAY(0.50)  ZF5=PNVV(0.25)
         ZF6=SEEH(1.00)  ZF7=DKGE(0.75)  ZF8=TEAL(0.50)
         mean 0.625, z = -0.52, percentile 28.9
  ADNP   ZF1=FSAS(0.50)  ZF2=DKTT(1.00)  ZF3=LEIK(0.50)  ZF4=SEAQ(0.75)  ZF5=PNVV(0.25)
         ZF6=PDTN(0.75)  ZF7=DEKA(0.75)  ZF8=IDAH(0.50)  ZF9=TSTL(0.75)
         mean 0.639, z = -0.45, percentile 28.9
  Mann-Whitney ADNP2 fingers vs background (one-sided, less): U=10269, p=0.073, n=8
  Mann-Whitney ADNP  fingers vs background (one-sided, less): U=12036, p=0.085, n=9
```

## Output, InterPro signatures over the zinc-finger region

```
  ADNP2 (Q6IQ32): 18 entries total, 9 matching 'zinc/C2H2'
     interpro     IPR013087      n=8   Zinc finger C2H2-type            [(73, 96), (106, 128), (155, 178)]
     interpro     IPR045762      n=1   ADNP, zinc finger domain         [(2, 129)]
     interpro     IPR060138      n=1   Adnp2-like, C2H2-type zinc finger[(693, 717)]
     pfam         PF26748        n=1   Adnp2-like, C2H2-type zinc finger[(693, 717)]
     pfam         PF32320        n=1   ADNP2 tandem C2H2-type zinc fingers [(155, 256)]
     pfam         PF33250        n=1   ADNP zinc finger region          [(730, 859)]
     profile      PS50157        n=1   Zinc finger C2H2 type domain profile [(770, 798)]
     prosite      PS00028        n=1   Zinc finger C2H2 type domain signature [(772, 793)]
     smart        SM00355        n=8   zinc finger                      [(73, 96), (106, 128), (155, 178)]
     PF00096 (zf-C2H2) present: False

  ADNP (Q9H2P0): 21 entries total, 9 matching 'zinc/C2H2'
     cathgene3d   G3DSA:3.30.160.60 n=1 Classic Zinc Finger            [(70, 152)]
     interpro     IPR013087      n=8   Zinc finger C2H2-type            [(74, 97), (107, 129), (165, 188)]
     interpro     IPR045762      n=1   ADNP, zinc finger domain         [(2, 130)]
     interpro     IPR060138      n=1   Adnp2-like, C2H2-type zinc finger[(446, 470)]
     pfam         PF26748        n=1   Adnp2-like, C2H2-type zinc finger[(446, 470)]
     pfam         PF33250        n=1   ADNP zinc finger region          [(472, 533)]
     profile      PS50157        n=1   Zinc finger C2H2 type domain profile [(512, 540)]
     prosite      PS00028        n=1   Zinc finger C2H2 type domain signature [(514, 535)]
     smart        SM00355        n=8   zinc finger                      [(74, 97), (107, 129), (165, 188)]
     PF00096 (zf-C2H2) present: False

  reviewed human proteins with a PF00096 cross-reference (UniProt total): 681
```

Neither paralog carries PF00096, the classic C2H2 Pfam model, and the stringent PROSITE profile
PS50157 matches exactly one finger in each (ADNP2 770-798 = ZF7, ADNP 512-540 = ZF7). The eight
IPR013087 and SM00355 hits come from permissive models, the same situation as SMART SM00389 over the
homeodomain. InterPro instead assigns three ADNP-family-specific Pfam entries (PF26748, PF32320,
PF33250), which means the family's fingers are modelled as their own thing, not as classic C2H2
fingers. ADNP carries CATH-Gene3D G3DSA:3.30.160.60 "Classic Zinc Finger" over 70-152; ADNP2 does not.

## Output, AlphaFold confidence per finger

From the buggy pass, but this part of the cell is unaffected by the parser bug, since it reads pLDDT
over the UniProt feature intervals.

```
AlphaFold AF-Q6IQ32-F1-model_v6.pdb: whole-chain mean pLDDT 56.9
  finger   range        mean pLDDT   % > 70
  ZF1        73-96         86.4    100.0
  ZF2       106-128        86.2    100.0
  ZF3       155-178        91.5    100.0
  ZF4       215-240        89.3    100.0
  ZF5       694-716        83.0    100.0
  ZF6       747-768        87.9    100.0
  ZF7       770-793        88.1    100.0
  ZF8       875-898        84.4     95.8
  ZF9       913-937        81.6     88.0
  homeodomain 1043-1102     85.3     90.0
```

## Reading of the numbers

The seed context statement is wrong as written. Four of nine ADNP2 fingers carry the four
zinc-coordinating residues in canonical spacing. UniProt itself calls five of the nine degenerate
(types 2, 3, 5, 6, 9). ZF9 (913-937) has no second His in register under either pattern. A per-protein
fraction of 0.444 sits at the 0.8th percentile of the human C2H2 distribution (mean 0.933, sd 0.114,
z = -4.28).

The recognition-position chemistry tells the opposite story. The four base-reading positions of the
ADNP2 fingers are ordinary: mean base-reading fraction 0.625 against a background of 0.738 (z -0.52,
28.9th percentile), Mann-Whitney p = 0.073 with n = 8, which does not reach significance. Several
quadruplets look like working DNA-contact sets (ZF2 `QKVR`, ZF6 `SEEH`, ZF7 `DKGE`).

The paralog contrast disappears here. ADNP and ADNP2 are identical at 4 of 9 canonical fingers, both
at the 0.8th percentile, and their recognition chemistry is the same (0.639 versus 0.625, both at the
28.9th percentile). Whatever makes ADNP a sequence-specific binder and ADNP2 not, this analysis does
not locate it in the finger array. The difference the data does support is in the homeodomain.

Conclusion for curation: the zinc-finger array is neither a confirmed alternative basis for GO:0003677
nor excluded as one. It is untested. Of the nine fingers, four could fold and bind in principle, and
AlphaFold models all nine with pLDDT above 80. This is an in-silico result about sequence pattern and
predicted confidence, and no DNA-binding measurement exists for either the fingers or the homeodomain
of ADNP2.

Figure: `provenance/plot_9.png` (three panels: finger-spacing distribution, recognition-position
chemistry distribution, per-finger chemistry for ADNP2).
