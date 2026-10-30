# agxta / agxtb protein, targeting-signal, expression and synteny comparison

Scripts (run from the repo root):

- `pair_analysis.py agxt` → `output.txt` (run 2026-09-28)
- `bgee_gar_coverage.py` → `bgee_gar_coverage.txt` (which gar tissues Bgee samples)

Zebrafish sequences come from the cached UniProt records (agxta Q6DG86, 391 aa; agxtb Q6PHK4, 423 aa). Human
AGXT (P21549) and its annotated sites come from UniProt. Orthologues in other species are the Ensembl Compara
member proteins of the orthologues Compara assigns to each zebrafish copy. Global alignments: Biopython
PairwiseAligner, BLOSUM62, gap open -10 / extend -0.5; identity = identical columns / alignment length. The
N-terminal extension is counted with end gaps free, so a leading extension is not forced to align with the
human N-terminus.

## Duplication

Ensembl Compara calls agxta / agxtb within-species paralogues with the duplication at the Osteoglossocephalai
node, and gives one spotted gar gene (ENSLOCG00000006520) as a one-to-many orthologue of both copies. Every
teleost in the panel except fugu (which has only a b-type copy in Compara) has one one-to-one orthologue of
each zebrafish copy, including the osteoglossomorph Asian arowana, so both copies were kept across the teleost
radiation.

## Protein

| Comparison | Identity |
|---|---|
| agxta vs agxtb | 62.4% (423 columns) |
| agxta vs human AGXT | 58.8% |
| agxtb vs human AGXT | 53.4% |
| agxta vs gar AGXT (428 aa) | 61.5% |
| agxtb vs gar AGXT | 71.8% |

Both copies keep the PLP-binding lysine (human K209) and the substrate-binding arginine (human R360), so both are
predicted to be active aminotransferases. Neither has any change at annotated catalytic positions.

**Relative rate (gar outgroup).** Of 390 gar positions aligned in both copies, 59 changed only in agxta and 32
only in agxtb (chi2 = 8.01, P<0.05). agxta has evolved faster; agxtb is closer to gar.

## Targeting signals

| Sequence | N-terminal extension before human Met1 | C-terminal tripeptide |
|---|---|---|
| agxta | none | SRV |
| agxtb | 32 aa, Arg-rich (net charge +4) | SKA |
| spotted gar AGXT | 38 aa, Arg-rich (net charge +5) | SKV |
| coelacanth AGXT | 34 aa | NKM |
| Xenopus tropicalis AGXT | 23 aa | NKM |
| chicken AGXT | 24 aa | SRL |
| mouse AGXT | 22 aa | NKL |
| human AGXT | none (no in-frame upstream ATG) | KKL |

The agxtb extension (MMPRTVLSRCARLTQQVPLESALSGKQSVQRG) and the gar extension (MMQRTLFCRGAFLAQQVALESALPTRV...)
share an MMxRTxxxRxAxLxQQVxLESAL motif; both have the positively charged, acid-poor composition of a mitochondrial
targeting sequence. The mouse and chicken extensions are the known MTS-bearing upstream-start products.

Upstream start check: the agxta canonical transcript (ENSDART00000073881) has a 101-nt 5' UTR with an in-frame stop
16 codons upstream of the start codon and no in-frame ATG before it; the genomic flank gives the same result. agxta
therefore cannot make an MTS-bearing isoform from this locus. For agxtb the annotated start is already the
extension-bearing Met (in-frame genomic stop 20 codons upstream, no upstream ATG). As a control, human AGXT has no
in-frame ATG in 50 codons upstream, and the translated upstream sequence ends SAAPGSRAAGWVRT, matching the end of the
mouse MTS (SRAAGWVRT): the MTS-coding region is still there in human but lacks a start codon, as described in the
literature.

**Pattern across teleosts.** Orthologues of agxtb in the panel (arowana, herring, cavefish, pike, salmon, cod,
medaka, stickleback, fugu, tilapia) all carry an N-terminal extension of 24-73 residues, and 7 of 10 end SKA (arowana
and stickleback SKV, cod VKR). Orthologues of agxta in cavefish, salmon, medaka and stickleback start at the
MS(S/A)(L/V)S(V/I)PPP motif without an extension; the arowana orthologue has a 35-residue Arg-rich extension, and the
herring, pike, cod and tilapia models have short extensions, several of which do not begin with Met and look like
gene-model artefacts. agxta orthologues end SRV, SKV, NKM or SNK.

Interpretation: the unduplicated outgroup (gar) and the tetrapods carry both an MTS-like N-terminal extension and a
C-terminal tripeptide. After the duplication the zebrafish copies each kept one signal: agxta kept a C-terminal
PTS1-like end and lost the extension (and any upstream start), agxtb kept the extension and its C-terminus became
SKA, which does not fit the PTS1 consensus. Whether SRV, SKV or NKM work as PTS1 in fish has not been tested, and
in Xenopus an NKM-ending AGT is mitochondrial, so the peroxisomal prediction for agxta is weaker than the
mitochondrial prediction for agxtb.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** Both copies are nearly silent until hatching and rise in
larvae; agxtb is about three times higher than agxta from day 3 on:

| Stage | agxta | agxtb |
|---|---|---|
| prim-25 | 1 | 0 |
| long-pec | 4 | 0.9 |
| protruding mouth | 24 | 62 |
| day 4 | 40 | 128 |
| day 5 | 50 | 175 |

**Bgee (only "expressed" calls are returned).** Both copies are liver-dominant with near-identical scores in liver,
spleen, head kidney, intestine and bone. RNA-Seq entities called for agxta only: embryo, integument, mesonephros;
for agxtb only: male organism, pharyngeal gill. These one-sided calls have moderate scores and do not suggest a
clean tissue split. Gar AGXT has calls in embryo, larva, liver, mesonephros and intestine (and low calls in
muscle, gonad, skin and testis), a liver-kidney-gut pattern shared by both zebrafish copies. Bgee samples 14 gar
tissues (`bgee_gar_coverage.txt`).

**ZFIN.** agxta: liver and pronephric duct by in situ hybridization (20-25 somites to day 5). agxtb: RT-PCR only
(whole larva; adult male kidney).

## Synteny

agxta (chr6) and agxtb (chr2) sit in a duplicated block. Of the 7 genes within 1.5 Mb of agxta that have a
teleost-level zebrafish paralogue, 6 have that paralogue within 1.5 Mb of agxtb: hs2st1, stk25, espnl, amotl2, sap130
and myo7b (a/b pairs). The reverse search from agxtb finds the same 6 pairs (`output.txt` section 10). This
double-conserved neighbourhood supports origin in a large-scale (whole-genome) duplication.

## Conclusion

The two copies have the same enzyme core and largely the same tissue expression. They differ in subcellular
targeting signals: agxta has only the C-terminal peroxisomal-type signal, and agxtb has only the N-terminal
mitochondrial-type signal. The outgroup and tetrapod orthologues carry both, so each copy appears to have lost one of
the two ancestral signals. This is a prediction from sequence; no zebrafish localization or enzyme data exist.
