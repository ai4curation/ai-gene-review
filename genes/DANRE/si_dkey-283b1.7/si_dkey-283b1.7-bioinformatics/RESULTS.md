# si:dkey-283b1.7 / vwc2 (brorin family): bioinformatics results

All numbers below come from the scripts in this folder. Each script's output is saved next to it
(`*_output.md`). Run the scripts from the repository root with `uv run python <script>`.
They query UniProt, Ensembl, Bgee, ZFIN and PANTHER live, so reruns against later releases may differ.

| script | output | question |
|---|---|---|
| `protein_compare.py` | `protein_compare_output.md` | VWC2 vs VWC2L assignment, core cysteines, N-terminal region |
| `synteny.py` | `synteny_output.md` | double-conserved synteny with gar (PANTHER orthology, Ensembl positions) |
| `compara_check.py` | `compara_check_output.md` | Ensembl Compara paralogy and orthologs of si:dkey-283b1.7, vwc2, vwc2l |
| `expression.py` | `expression_output.md` | Bgee and ZFIN expression calls, with gar vwc2 |
| `morpholino_check.py` | `morpholino_check_output.md` | specificity of the brorin morpholinos of PMID:28448525 |

## 1. Protein comparison

- si:dkey-283b1.7 (E7F8B1, 242 aa) is only 32.6% identical to vwc2 (B0I1T8, 309 aa) over the full length.
  vwc2 is 53.8% identical to human VWC2 and 65.7% to gar vwc2.
- si:dkey-283b1.7 has a predicted signal peptide (residues 1-18), as do all family members examined.
- Architecture: si:dkey-283b1.7 lacks the long N-terminal region of VWC2. Only 26 of its residues align to
  human VWC2 28-152, compared with 94 for vwc2 and 109 for gar vwc2. In length and architecture it
  resembles VWC2L (222-229 aa in human, gar and zebrafish vwc2l).
- Conserved core (residues aligned to human VWC2 153-274, the two VWFC domains): si:dkey-283b1.7 keeps all
  20 core cysteines of human VWC2 (as does every family member tested). Its core identity is 59.8% to
  human VWC2, 54.9% to human VWC2L, 54.9% to gar vwc2, 57.4% to gar vwc2l and 54.9% to zebrafish vwc2.
  By contrast, the vwc2 core is 83.6% identical to human VWC2 and 89.3% to gar vwc2, and the vwc2l core is
  95.1% identical to human VWC2L.
- The medaka protein that PANTHER assigns as the co-ortholog of si:dkey-283b1.7 (A0A3B3HFT2) is its
  closest relative (58.8% full length, 71.3% core). The si:dkey-283b1.7 lineage is therefore shared by
  zebrafish and medaka and evolves fast.
- Pairwise identity cannot assign si:dkey-283b1.7 confidently to either VWC2 or VWC2L. It is slightly
  closer to VWC2 in the core and slightly closer to VWC2L over the full length, because of the shared
  short architecture.
- The human VWC2 RGD motif (114-116) is not conserved in any fish protein.

## 2. Gene-tree placement (Ensembl Compara, independent of PANTHER)

Ensembl Compara gives si:dkey-283b1.7 no ortholog in gar or human, only a one-to-one ortholog in medaka
(Clupeocephala). It relates si:dkey-283b1.7 and vwc2 only as "other paralogs" at the Bilateria level, while
vwc2 has one-to-one orthologs in gar (Neopterygii) and human (Euteleostomi). PANTHER instead places the
si:dkey-283b1.7/vwc2 split on the Neopterygii|Teleostei branch, with gar vwc2 as the shared co-ortholog.
This conflict is what would be expected if a fast-evolving TGD copy were pulled toward the base of one
tree (long-branch attraction), but it is also what an old family branch lost in tetrapods and gar would
look like. See section 3.

## 3. Synteny

Windows of +/- 1.5 Mb; zebrafish-gar orthology from PANTHER v19; gene positions from Ensembl (GRCz11,
LepOcu1).

- The gar vwc2 window (LG11) holds 20 protein-coding genes.
- The vwc2 window on zebrafish chromosome 13 shares three genes with it: fignl1, ikzf1 and the gar SPMIP7
  ortholog. This conserved block matches the published synteny of vwc2 with ikzf1 (PMID:28448525).
- The si:dkey-283b1.7 window on zebrafish chromosome 3 holds 167 protein-coding genes, 51 of them with a
  PANTHER gar ortholog. None of those orthologs lies in the gar vwc2 window.
- No gar-window gene has orthologs in both zebrafish windows. There is no double-conserved synteny
  for this pair.

So synteny with gar does not support the PANTHER TGD call: the si:dkey-283b1.7 region is not
recognizably the duplicate of the vwc2 region. This does not rule out a TGD origin. The gar window is
small, and a TGD block can be broken up by rearrangement, or lose most of its duplicate genes. Combined
with the Ensembl Compara placement (section 2), though, the TGD origin of this pair rests on the PANTHER
gene tree alone and is not established.

## 4. Expression

- si:dkey-283b1.7 has Bgee RNA-Seq calls in retina, brain and whole larva (scores 61.2, 58.2, 28.8).
  It has no ZFIN curated expression.
- vwc2 has Bgee RNA-Seq calls in brain (64.1), head, larva, testis and bone element. It also has
  in situ calls in forebrain, hindbrain, spinal cord, pituitary and olfactory placode (34 ZFIN records
  from PMID:19852960 and PMID:28448525).
- Gar vwc2 has RNA-Seq calls in eye (63.3), brain (50.5), mesonephros, liver and larva.
- The two zebrafish copies share brain and larva. Retina is a call for si:dkey-283b1.7 only, while gar
  vwc2 is expressed in the eye. Bgee lists only present calls, so the missing retina call for vwc2 is
  not evidence of absence.

## 5. Morpholino specificity

The brorin morpholinos of PMID:28448525 match vwc2 perfectly and have 9 or more mismatches to si:dkey-283b1.7
(MO1: 0 mismatches in vwc2, 9 in si:dkey-283b1.7, 9 in vwc2l; MO2: 0, 10, 8). The published morphant
phenotypes are therefore vwc2-specific.

## Interpretation (limits)

The sequence data establish that si:dkey-283b1.7 is a brorin-family protein with an intact cysteine-rich
core and a signal peptide. They do not establish which vertebrate family member it descends from, and
synteny does not support its pairing with vwc2 as TGD ohnologs.
The expression data are thin: three RNA-Seq calls and no in situ data.
