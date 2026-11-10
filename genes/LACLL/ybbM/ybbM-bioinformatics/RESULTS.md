# ybbM bioinformatics: UPF0014/FetB family placement and plasmid context

Query: KBase gene-annotate dashboard protein NZ_CP016699.1_28 (*Lactococcus lactis* subsp. *lactis*
strain 275, plasmid p275A; UniParc UPI0009C0EEE3, RefSeq WP_081144392), 251 aa. The review is filed
on UniProtKB G1FE25 (plasmid pVF18), which is 98.8% identical (248/251).

Reproduce with `just analyze` in this folder. All numbers below are from `results.json`.

## Method

1. hmmsearch (pyhmmer) of the query and reference proteins with Pfam PF03649.19 (UPF0014) and
   NCBIfam TIGR00245.2 ("iron efflux ABC transporter permease subunit FetB"), HMMs downloaded from
   the InterPro API. TIGR00245 is an equivalog model with gathering and trusted cutoffs of 410 bits.
2. Global alignment (BLOSUM62, gap -11/-1, free end gaps); identity = identical / aligned pairs.
3. GenBank record NZ_CP016699.1 (NCBI efetch): every CDS whose translation equals the query, with
   four CDSs on each side. Adjacent ABC ATP-binding CDSs are aligned to *E. coli* FetA (P77279).

## Results

| Protein | Identity to query | PF03649 bits | TIGR00245 bits | ≥ TIGR00245 TC (410) |
|---|---|---|---|---|
| query NZ_CP016699.1_28 | — | 278.9 | 359.9 | no |
| G1FE25 (*L. lactis* pVF18) | 98.8% | 280.2 | 360.4 | no |
| A4VC75 (*L. lactis* pGdh442) | 98.8% | 278.0 | 357.5 | no |
| Q5M2X9 *S. thermophilus* stu1665 | 98.4% | 277.0 | 358.2 | no |
| P77307 *E. coli* FetB | 59.0% | 274.1 | 476.8 | yes |
| O34684 *B. subtilis* YjkA | 35.2% | 253.9 | 199.6 | no |
| Q5W7C1 rice STAR2 | 34.4% | 229.6 | 188.0 | no |
| Q9ZUT3 *Arabidopsis* ALS3 | 34.0% | 224.6 | 188.4 | no |
| P74369 *Synechocystis* slr1647 | 31.9% | 292.6 | 161.6 | no |

- The query is a full-length UPF0014 protein: the PF03649 domain envelope covers residues 7-244 of
  251, at 278.9 bits against a 22.6-bit gathering cutoff.
- The query scores 359.9 bits against TIGR00245, below the 410-bit trusted cutoff that E. coli FetB
  passes (476.8 bits). It scores far higher than the plant and B. subtilis/cyanobacterial members
  (161.6-199.6 bits). The query is therefore FetB-like but outside the FetB equivalog as NCBIfam
  defines it. The query and its 98.4%-identical S. thermophilus homolog sit between E. coli FetB
  and the more distant UPF0014 members.
- Two identical copies of the query are on plasmid p275A: LL275_RS12810 (LL275_pA030) and
  LL275_RS13010 (LL275_pA069). Each is adjacent to an ABC transporter ATP-binding protein gene
  (LL275_RS12815 and LL275_RS13005, identical 216-aa proteins) in a two-gene permease/ATPase
  cassette. IS-element transposases lie within four genes of both cassettes: IS981, ISLll1 and an
  IS6-family transposase around the first; ISS1S (IS6-like), IS5/IS1182 and IS6770 (IS30-like)
  downstream of the second.
- The adjacent ATP-binding protein is 47.4% identical to E. coli FetA over 97.7% of its length.
- The query has the FetA-FetB-type two-gene organisation, so it is most likely the permease of a
  FetAB-like ABC transporter. The substrate cannot be read from these data.

## Limits

- HMM bit scores and identities show family placement, not substrate. The TIGR00245 cutoff is a
  curation boundary chosen by NCBI, not a functional threshold measured for this clade.
- No experiment on any lactococcal or streptococcal member of the family is available.
