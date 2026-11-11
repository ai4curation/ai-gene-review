# GLDP1 (At4g33010, UniProt Q94B78) - curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are a manual literature summary built only from cached publications (`publications/PMID_*.md`)
and the UniProt record (`GLDP1-uniprot.txt`). No `-deep-research-*.md` file exists for this gene.

## Identity

- Glycine dehydrogenase (decarboxylating) 1, mitochondrial; the P protein of the glycine
  decarboxylase complex (GDC; glycine cleavage system). EC 1.4.4.2, PLP-dependent, GcvP family
  (PANTHER PTHR11773:SF1). Mitochondrial transit peptide 1-67; PLP-lysine at K774 (by similarity).
- Arabidopsis has two P-protein genes, At4g33010 (GLDP1) and At2g26080 (GLDP2)
  [PMID:22303256 "two genes each for P-protein (At4g33010 and At2g26080)"].

## Molecular function

- The P protein is the decarboxylating enzyme of GDC: [PMID:22303256 "P-protein (EC 1.4.4.2) is a
  pyridoxal-5-phosphate-containing homodimer, that catalyzes the actual glycine decarboxylation
  reaction"]. The aminomethyl remainder goes to the H protein:
  [PMID:22303256 "The remaining amino methylene part of glycine is transferred to the distal sulphur
  atom of the oxidized lipoamide arm of H-protein"].
- UniProt curated function [file:ARATH/GLDP1/GLDP1-uniprot.txt "The P protein binds the alpha-amino
  group of glycine through its pyridoxal phosphate cofactor"]; reaction RHEA:24304.
- Both GLDP isoforms have catalytic activity, GLDP2 weaker [PMID:33506579 "GLDP2, a paralog of GLDP1
  with weaker catalytic activity"] (abstract only). GLDPs form homo- and heterodimers
  [PMID:33506579 "both GLDPs could be O-glycosylated and form homodimers or heterodimers"].
- Redox regulation: GDC is inhibited by S-nitrosylation/glutathionylation; GLDP1 Cys residues
  identified [PMID:20089767 "GDC activity was inhibited by S-nitrosoglutathione due to
  S-nitrosylation/S-glutathionylation of several cysteine residues."] (abstract only; site list from
  UniProt).

## Complex and location

- GDC = P, H, T, L proteins; all four needed for activity [PMID:17496108 "The presence of all four
  proteins is necessary for catalytic activity of the complex."].
- Arabidopsis leaf GDC stoichiometry by MS includes both P isoforms, P1 being ~4x P2
  [PMID:32311173 "The Arabidopsis GDC contains four times more of the isoforms GCS-P1 and GCS-L1 in
  comparison with GCS-P2 and GCS-L2"] (abstract only).
- Mitochondrial: UniProt location experimental [PubMed:14671022]; plant GDC is a matrix complex
  [PMID:11286922 "In green leaves, this multienzyme system is present at tremendously high
  concentrations within the mitochondrial matrix."]. Detected in mitochondria isolated for ICP55
  study [PMID:25862457 "Gly decarboxylase P-protein2 (At2g26080 and At4g33010"].
- Plastid, cytosol, plasma membrane and apoplast detections (HDA) come from bulk proteomics of
  fractions known to carry contaminants; e.g. the chloroplast stroma study estimated
  [PMID:18431481 "proteins likely represent false positive identifications and/or non-chloroplast
  contaminations"]. Treated as contaminants of an abundant leaf mitochondrial matrix protein.

## Biological role

- GDC + SHMT form the mitochondrial part of photorespiration [PMID:22303256 "The combined reaction of
  glycine decarboxylase (GLD) and serine hydroxymethyltransferase (SHM) represents the mitochondrial
  part of the major photorespiratory pathway."].
- Genetics [PMID:17496108]: single gldp1 or gldp2 knockouts are near wild type
  ["The individual knockout of either of these two genes does not significantly alter metabolism and
  photosynthetic performance indicating functional redundancy"], but gldp1 mutants accumulate
  glycine under photorespiratory conditions ["which were significantly elevated under
  photorespiratory conditions"], and ["AtGLDP1 clearly carries a somewhat higher photorespiratory
  workload than AtGLDP2"]. The double mutant arrests at the cotyledon stage even in high CO2,
  indicating GDC is indispensable for one-carbon metabolism, not only photorespiration
  ["provides evidence for the nonreplaceable function of GDC in vital metabolic processes other than
  photorespiration"].
- Expression: [PMID:17496108 "AtGLDP1 transcripts dominate in photosynthesizing organs while AtGLDP2
  transcripts are more abundant in roots."].

## Annotation decisions (summary)

- Core: GO:0004375 (MF), GO:0019464 / GO:0006546 (BP), mitochondrion. NEW: GO:0005960 glycine
  cleavage complex (PMID:32311173) and GO:0009853 photorespiration (PMID:17496108).
- Photorespiration comparator check (QuickGO, 2026-10): other Arabidopsis enzymes catalysing C2-cycle
  steps carry GO:0009853 (SHM1 IMP, GLYK IMP/IBA, HPR TAS, GGAT1 TAS, PLGG1 IMP); the GDC subunits
  (GLDP1/2, GDCH, GDCST) lack it. GLDP1 catalyses a step of the cycle, so it passes the participation
  test.
- mRNA binding (RNA interactome capture, no follow-up): over-annotated. Protein binding to 14-3-3
  (TAP-MS): removed per protein-binding policy. Response to cadmium (IEP proteomics): non-core.
- The retracted iNOS claim (UniProt CAUTION, PubMed:12757708 retracted by 15599984) is not used.
