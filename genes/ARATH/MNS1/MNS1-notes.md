# MNS1 (At1g51590, Q9C512) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: MNS1 is reviewed as the closest experimentally characterised relative of
DROME/alpha-Man-Ia (P53624). Both sit in PANTHER subfamily PTHR11742:SF6
(MANNOSYL-OLIGOSACCHARIDE ALPHA-1,2-MANNOSIDASE IA-RELATED) per
`interpro/panther/PTHR11742/PTHR11742-entries.csv`. No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon ARATH MNS1 --fallback perplexity-lite` failed on 2026-10-21:
falcon "Exception: Failed to authenticate"; perplexity fallback "HTTP error: 401 ...
insufficient_quota". No deep-research file exists; the review is built from the cached
primary literature below plus the UniProt record and PANTHER/PAINT files.

### Literature read

- Kajiura et al. 2010 [PMID:19914916, abstract only]: recombinant AtMANIa (MNS2) and
  AtMANIb (MNS1) are 1-deoxymannojirimycin-sensitive alpha-mannosidase I enzymes that
  convert Man8GlcNAc2 and Man9GlcNAc2 to Man5GlcNAc2; GFP/DsRed fusions in Golgi stacks;
  single mutants wild-type glycans, double mutant accumulates Man8GlcNAc2 and lacks
  complex/hybrid N-glycans ["either AtMANIa or AtMANIb can function as the Golgi
  alpha-mannosidase I that produces the Man(5)GlcNAc(2) N-glycan structure necessary for
  complex N-glycan synthesis"].
- Liebminger et al. 2009 [PMID:20023195, abstract only]: MNS1/MNS2 Golgi
  alpha-mannosidase I; MNS3 ER-type but also in Golgi-like puncta; "MNS1/2 readily removed
  three alpha1,2-mannose residues from Man(8)GlcNAc(2)"; mns1 mns2 Man8 accumulation; triple
  mutant short radially swollen roots, altered cell walls.
- Hüttner et al. 2014 [PMID:24737672, full text]: MNS4/MNS5 (ER, EDEM/HTM1-like) are the
  plant ERAD mannosidases; "MNS1 to MNS3 appear dispensable for this ERAD process"; the
  bri1-5 and bri1-9 phenotypes are not suppressed in mns1 mns2. MNS1-GFP labels Golgi;
  MNS1/MNS2 "preferentially cleave off a terminal α1,2-linked Man residue from the
  A-branch".
- Liu et al. 2018 [PMID:29409894, abstract only]: mns1 mns2 severely salt-sensitive root
  growth; reduced cellulose; RSW2/KOR abundance depends on mannose trimming. This is a
  downstream physiological consequence of loss of glycan maturation, not a separate process
  that MNS1 performs; not annotated.
- Proteomics HDA: Dunkley 2006 LOPIT [PMID:16618929]; Parsons 2012 Golgi proteome
  [PMID:22430844]; Nikolovski 2012 LOPIT [PMID:22923678], which states "The Golgi apparatus
  and the TGN proteins were combined into one class because they have a similar
  fractionation profile" — so TGN and endosome rows from that paper cannot distinguish
  TGN/endosome from Golgi; Parsons 2019 cisternal separation [PMID:31266899, abstract only],
  source of Golgi cis cisterna.

### Evolutionary grounding

- PANTHER: PTHR11742:SF6, same subfamily as fly alpha-Man-Ia (P53624) and Spodoptera
  O18498. Vertebrate MAN1A1/MAN1A2/MAN1C1 are in other subfamilies (per task brief; not
  re-verified here).
- PAINT (`PTHR11742-paint.tsv`): root node PTN000201533 carries mannosyl-oligosaccharide
  1,2-alpha-mannosidase activity (GO:0004571; MNS1 itself an experimental seed), ER
  (GO:0005783) and ERAD (GO:0036503; seeds are ER-type MAN1B1/yeast Mns1/EDEM-like/HTM1,
  none from the Golgi clade). PTN000201534 carries Golgi membrane (GO:0000139) seeded by
  AT1G51590 (MNS1), AT3G21160 (MNS2) and mouse Man1a1/Man1a2.
- ER and ERAD therefore reach MNS1 only by inheritance from the family root, not from any
  Golgi-clade evidence; MNS1 has species-specific negative genetic evidence for ERAD
  (PMID:24737672) and is detected only in Golgi.

### Decisions summary

- Core MF: GO:0004571 mannosyl-oligosaccharide 1,2-alpha-mannosidase activity (EXP/IDA,
  in vitro on Man8/Man9GlcNAc2). Ca2+/Mn2+ cofactor requirement (UniProt, from
  PMID:20023195).
- Core BP: GO:0006491 N-glycan processing (IMP/IGI, redundant with MNS2).
- Core CC: GO:0000139 Golgi membrane (type II signal-anchor; Golgi FP fusions).
- ERAD IBA: REMOVE (dispensable for ERAD of BRI1-5/BRI1-9; Golgi enzyme; ERAD trimming in
  plants is MNS4/MNS5).
- ER IBA: MARK_AS_OVER_ANNOTATED (biosynthetic transit only; never detected in ER).
- Plasma membrane ISM: REMOVE (prediction contradicted by experimental Golgi residence).
- TGN/endosome HDA: MARK_AS_OVER_ANNOTATED (Golgi/TGN merged class in the LOPIT analysis).
- General terms (membrane, Golgi apparatus, alpha-mannosidase activity, carbohydrate
  metabolic process): MODIFY to the specific terms above.
- No NEW process terms: root development, cell wall biogenesis and salt-stress tolerance are
  downstream phenotypes of failed glycan maturation.

Transfer guidance for alpha-Man-Ia: the activity (GO:0004571) and Golgi-membrane location
are supported at the SF6/PTN000201534 level. Branch preference (A-branch first; Man8 ->
Man5 but Man9 -> Man6 only) is an Arabidopsis-measured property, and the noted divergence
from mammalian MANI hydrolytic pathways (PMID:19914916) argues against transferring fine
linkage/branch specificity.
