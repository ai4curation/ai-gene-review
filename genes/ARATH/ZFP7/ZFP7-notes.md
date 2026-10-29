# ZFP7 (Q39266, At1g24625) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ZFP7 was reviewed as the closest experimentally characterised relative of the
soybean ProtNLM2 benchmark gene C6T1A2. This review treats ZFP7 in its own right; no
ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon ARATH ZFP7 --fallback perplexity-lite` failed: Falcon returned
"Edison API request failed: Failed to authenticate" (403) and the perplexity-lite fallback
also failed. No deep-research file exists. The review is based on the cached publications
and a direct PubMed search (`ZFP7 OR At1g24625` and `"zinc finger protein 7" OR ZFP7`
with Arabidopsis), which returned only PMID:24808098 and PMID:38250442 as ZFP7-specific
papers. PMID:7599312 (cDNA cloning) was also cached.

### What is experimentally established for ZFP7 itself (Arabidopsis)

- Cloning: one of eight single-finger C2H2 cDNAs; family members are expressed in
  different but overlapping organs [PMID:7599312 "the eight cDNAs isolated from
  Arabidopsis each contain only a single zinc finger"].
- ABA: estradiol-inducible overexpression of ZFP7 (with ZFP1, ZFP3, ZFP4, ZFP6) makes seed
  germination ABA-insensitive [PMID:24808098 "regulated overexpression of ZFP3 and the
  closely related ZFP1, ZFP4, ZFP6, and ZFP7 zinc finger factors confers ABA insensitivity
  to seed germination"]. Loss-of-function evidence for the ABA role is from the zfp3 zfp4
  double mutant, not from ZFP7 [PMID:24808098 "the zfp3 zfp4 double mutant displays
  enhanced ABA susceptibility"]. The cached record is abstract-only, so ZFP7-specific
  details (constructs, effect sizes) are not visible here.
- Vegetative growth: amiR silencing of ZFP7 (alone or with ZFP4) had no strong phenotype
  [PMID:38250442 "amiR-mediated silencing of ZFP1, ZFP3, ZFP4, and ZFP7 genes had no
  dramatic consequence on plant phenotype and growth"].
- Transcriptome: induced ZFP7 overexpression changes fewer genes than ZFP3, and does not
  repress the ZFP3 cell-wall/root-hair targets [PMID:38250442 "These results suggest that
  fewer target genes are regulated by ZFP7 compared to ZFP3."]. So the ZFP3 root-hair /
  cell-wall role should not be transferred to ZFP7.
- DNA binding: ZFP7 was recovered as a promoter-binding TF in several enhanced yeast
  one-hybrid (eY1H) screens (stele promoters, glucosinolate, secondary cell wall, nitrogen
  and PXY vascular networks; PMIDs 22037706, 25352272, 25533953, 30356219, 31806676).
  These are heterologous yeast assays; in planta binding is not shown for ZFP7.
- Glucosinolate: in the Li et al. screen, mutant TFs were profiled for aliphatic
  glucosinolate; TAIR annotated ZFP7 IMP to glucosinolate metabolic process with
  acts_upstream_of_or_within. The table with ZFP7's data is not in the cached text.
- Protein interactions: Y2H with TCP13 (PMID:21798944, PMID:28650476), and bZIP1 (BZIP1,
  Q9FGX2) in Y2H/BiFC screens (PMID:20080816, abstract only).
- Localisation: no ZFP7 experiment. Nucleus is inferred from ZFP2 (ISS), AtSubP, and the
  PAINT node; ZFP3 is described as nuclear in PMID:24808098.

### Sequence (ZFP7-bioinformatics/RESULTS.md)

Single C2H2 finger 61-81 with the plant Q-type QALGGH motif (72-77); LxLxL EAR-like
matches at 35-39 and the C-terminus (205-209). No DLNxxP.

### Phylogeny

PAINT: PTN009184003 (nucleus, transcription cis-regulatory region binding; seeds include
ZFP7 itself, ZFP4, KNU, ZFP3) and PTN008158895 (GO:0009788; seeds ZFP7 and ZFP4). ZFP7
appearing as its own seed is expected. Family assignment differs between UniProt's HMM
cross-reference (PTHR47593:SF8) and the PANTHER 19 tree (PTHR45730:SF104), per the
C6T1A2 re-review analysis.

### Decisions

- Accept MF transcription cis-regulatory region binding (IBA + multiple eY1H IPI) and
  DNA-binding transcription factor activity; accept nucleus.
- Accept GO:0009788 (IMP overexpression + IBA); note that ZFP7-specific evidence is
  gain-of-function only.
- Glucosinolate metabolic process: keep as non-core (screen-level mutant phenotype,
  acts upstream).
- Protein binding (TCP13): remove as uninformative per policy; the interaction is not
  disputed.
- Protein heterodimerization activity (bZIP1): undecided; abstract-only; a single-finger
  C2H2 protein is not known to dimerise via a dimerisation domain, but the curator saw the
  full text.

### For transfer to C6T1A2

Only domain-level features (Q-type C2H2 finger, putative TF activity, nucleus) are safe
family-level transfers. GO:0009788 is a PAINT node decision on the ZFP7/ZFP4 clade that
C6T1A2 does not descend from.
