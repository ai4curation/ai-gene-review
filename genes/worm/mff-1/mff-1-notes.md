# mff-1 (C. elegans) research notes

UniProt: Q19343 (Q19343_CAEEL, unreviewed/TrEMBL). WormBase: WBGene00008691, F11C1.2.
Gene: mff-1. Human ortholog: MFF (mitochondrial fission factor). 158 aa.

## Identity confirmation

- UniProt Q19343 is `mff-1 {ECO:0000313|WormBase:F11C1.2}`, ORF F11C1.2, "Mitochondrial fission factor",
  family Tango11 (Mff/Tango-11, IPR008518). TCDB 8.A.166.1.1 "mitochondrial fission factor (mff) family".
- Primary literature explicitly identifies this gene:
  [PMID:21248201 "C. elegans has two Fis1 homologues, encoded by fis-1 and fis-2, and two Mff homologues, encoded by mff-1(F11C1.2) and mff-2(F55F8.6)"].
  So F11C1.2 = mff-1 is confirmed by ORF name in the primary literature. mff-2 = F55F8.6 is the paralog.

## Protein architecture

- 158 aa, single C-terminal predicted transmembrane helix (UniProt FT TRANSMEM 139..156), consistent
  with a tail-anchored (type IV / single-pass) mitochondrial outer-membrane protein — the canonical MFF
  topology (cytosol-facing N-terminal domain, C-terminal TM anchor).
- UniProt FUNCTION (RuleBase, electronic): "Plays a role in mitochondrial and peroxisomal fission.
  Promotes the recruitment and association of the fission mediator dynamin-related protein 1 (DNM1L)
  to the mitochondrial surface."
- UniProt SUBCELLULAR LOCATION (RuleBase): Mitochondrion outer membrane; Single-pass type IV membrane
  protein. Peroxisome.

## KNOWN (experimental, C. elegans-specific)

### Mitochondrial and peroxisome fission — genuine role, redundant with mff-2
- [PMID:24196833 "mff-1 and mff-2 single mutants have weak effects, and that the Mff double mutant has a
  mitochondrial fission defect similar to but not as strong as the drp-1 defect"] — direct genetic
  evidence that mff-1 (with mff-2) is required for normal mitochondrial fission. Single mff-1 mutant =
  weak (redundancy with mff-2); Mff double mutant = strong fission defect (approaching drp-1).
- [PMID:24196833 "Analogous results were obtained with a peroxisome marker, showing punctate peroxisomes
  in wild-type and Fis1 mutants and tubular peroxisomes in drp-1 mutant and Mff double mutants"] and
  [PMID:24196833 "We conclude that C. elegans Mff homologues affect mitochondrial and peroxisome fission,
  whereas Fis1 homologues have no obvious effects"] — supports both mitochondrial fission AND peroxisome
  localization/peroxisome fission for MFF (worm), and contrasts sharply with fis-1/fis-2 (no obvious
  fission role).
- Alleles: mff-1(tm2955), mff-2(tm3041) (Mitani/NBRP); quadruple fis-1 fis-2 mff-1 mff-2 mutant made.

### Mitochondrial outer membrane localization — experimentally supported
- [PMID:21248201 "Blots were probed with antibodies for EAT-3 (an inner membrane marker), MOMA-1, MFF-1
  (an outer membrane marker), and F1β subunit of the ATP synthase complex (a mitochondrial matrix
  marker)"] — MFF-1 is used as a bona fide mitochondrial outer membrane marker (anti-MFF-1 antibody).
- [PMID:21248201 "MOMA-1 is digested when no detergent is added, like MFF-1, while EAT-3 and F1β are
  protease protected"] — in a protease-protection assay on intact mitochondria, MFF-1 is digested without
  detergent, i.e. it is exposed to the cytosol / anchored in the OM (consistent with tail-anchored OM
  topology, N-terminus cytosol-facing).
- GFP/CFP-tagged mff-1 expressed in muscle cells [PMID:24196833 "Full-length fis-1, fis-2, mff-1, and
  mff-2 cDNAs were cloned in the pPD96.52 expression vector"].

### Mitophagy / stress-induced fission (non-core, downstream)
- [PMID:24196833 "significantly reduced number of spots in Mff double and Fis1 Mff quadruple mutant
  strains"] and [PMID:24196833 "their number is reduced by Mff mutations and eliminated by the Pink1
  mutation"] — Mff (mff-1/mff-2) contributes to formation of mitophagosomes (LGG-1/mito colocalizing
  spots); loss of Mff reduces (but does not abolish) mitophagosome number. This is a downstream
  consequence of the fission role, not a distinct molecular function.
- [PMID:24196833 "Mff acts upstream of the Fis1-dependent step in this process"] — places Mff early in
  the fission→mitophagy sequence (Drp1 first binds Mff, then Fis1).

## NOT known / important worm-specific nuances

- **DRP-1 recruitment in worm is NOT strictly Mff-dependent** (unlike mammals). This is the key divergence
  from the mammalian paradigm and from the UniProt RuleBase "promotes recruitment of DNM1L" statement:
  [PMID:24196833 "We conclude that Mff affects fission, but Mff and Fis1 are not essential for fission or
  for Drp1 recruitment to mitochondria in C. elegans"]. CFP::DRP-1 still forms fission-marking spots and
  fractionates to mitochondria normally in Mff double/quadruple mutants. Worm lacks MiD49/MiD51.
  => The "positive regulation of protein targeting to membrane" (DRP-1 recruitment) annotation is
  inferred from mammalian orthology (UniRule) and is only partially supported in worm — DRP-1 can reach
  mitochondria without Mff, though Mff still promotes efficient fission. Keep as non-core / note the
  caveat; do not assert as a firmly established worm function.
- No experimental characterization of a direct MFF-1–DRP-1 physical interaction in worm.
- Relative division of labor between mff-1 and mff-2 (which paralog dominates, tissue specificity,
  whether they heterooligomerize) is not resolved — single mutants are "weak", implicating redundancy,
  but the individual contribution of mff-1 vs mff-2 is not dissected.
- No worm data on peroxisome-specific vs mitochondria-specific pools of MFF-1, or on regulation
  (mammalian MFF is phospho-regulated by AMPK; not tested in worm).

## Annotation assessment summary (all 5 GOA annotations are IEA)

1. GO:0000266 mitochondrial fission (IEA, UniRule) — ACCEPT (core). Now backed by worm experimental
   genetics (Mff double mutant fission defect, PMID:24196833). Genuine fission role expected for MFF and
   confirmed in worm — unlike fis-1/fis-2.
2. GO:0005741 mitochondrial outer membrane (IEA, SubCell) — ACCEPT (core). Experimentally supported in
   worm (MFF-1 OM marker + protease protection, PMID:21248201).
3. GO:0005777 peroxisome (IEA, SubCell/UniRule) — ACCEPT / KEEP_AS_NON_CORE. Supported by worm data
   (Mff double mutant → tubular peroxisomes, i.e. peroxisome fission defect, PMID:24196833) plus ortholog.
4. GO:0090141 positive regulation of mitochondrial fission (IEA, UniRule) — ACCEPT (core). MFF promotes
   fission; loss reduces fission. Consistent with worm genetics.
5. GO:0090314 positive regulation of protein targeting to membrane (IEA, UniRule) = DRP-1 recruitment.
   MODIFY/KEEP_AS_NON_CORE with caveat — in worm, Mff is NOT essential for DRP-1 recruitment
   (PMID:24196833). Inferred from mammalian orthology; only partially holds in worm. Keep but flag.

## Deep research

- falcon deep-research launched (`just deep-research-falcon worm mff-1 --fallback perplexity-lite`).
  Falcon can take 20+ min. drp-1 falcon research already cites worm FIS-1/FIS-2 and MFF-1/MFF-2 as
  DRP-1 recruitment factors (Traa et al. GeroScience 2025; Kamerkar et al. Nat Commun 2018) — background
  cross-species context only, not worm mff-1-specific mechanism.

## Falcon deep research (completed, 1059s, 26 citations) — mff-1-deep-research-falcon.md

Genuine falcon report. Confirms and extends the primary-literature picture. Key points:
- Confirms identity: mff-1 = ORF F11C1.2, UniProt Q19343, Tango11/MFF family (metazoan-specific, absent
  in yeast). Two worm paralogs mff-1 and mff-2.
- Cites Head et al. 2011 (PMID:21248201) for the OM/protease-protection localization result (matches my
  read of that paper).
- Cites Lu, Rolland, Conradt 2011 (PNAS; = PMID:21949250, already cached) proposing MFF-1/MFF-2 as
  candidate DRP-1 receptors alongside the EGL-1–CED-9 complex — this is a PROPOSAL/inference, not a
  direct MFF-1 mechanism test.
- Mammalian MFF biology (by orthology only, NOT worm): N-terminal R1/R2 repeats bind DRP1; MFF is the
  principal DRP1 receptor; MFF mediates peroxisome fission; AMPK phosphorylates MFF (S146, S155, S172,
  S275); MFF-MAVS/innate-immunity role; human MFF LoF → encephalopathy (OMIM 617086). None of these are
  demonstrated for worm mff-1.
- Falcon did NOT retrieve Shen et al. 2014 (PMID:24196833) — so it states worm peroxisome fission "has
  not been directly tested". My review has the stronger direct evidence (Shen 2014: Mff double mutant →
  tubular peroxisomes), so I rely on the primary paper, not the falcon inference, for the peroxisome and
  the Mff-independent-DRP-1-recruitment points.

Net: my review is anchored on the two direct experimental worm papers (PMID:24196833, PMID:21248201).
Falcon confirms identity + localization and provides mammalian/ortholog context. No falcon-only claim is
used as primary evidence; all supporting_text quotes are from cached PMIDs.
