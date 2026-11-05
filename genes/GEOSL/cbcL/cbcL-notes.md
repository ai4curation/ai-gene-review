# cbcL (GSU0274, UniProtKB:Q74GH2) notes

Geobacter sulfurreducens PCA, TrEMBL entry Q74GH2_GEOSL, 619 aa, PE 4 (predicted).
UniProt has no gene name, only the ordered locus GSU0274; "cbcL" (c- and b-type
cytochrome for low potential) is the name used in the literature since Zacharoff et al.
2016. The folder was fetched with `just fetch-gene GEOSL Q74GH2 --alias cbcL`.

No deep-research provider was available, so these notes are a manual literature
review (PubMed eutils search for "cbcL AND Geobacter" and "Zacharoff Bond Geobacter").

## Sequence and domain architecture (from the UniProt record and own motif count)

- SignalP signal peptide 1-22; Phobius predicts six transmembrane helices
  (286-314, 351-373, 399-421, 476-495, 507-532, 589-614).
- A regex scan of the sequence for CXXCH finds nine motifs starting at residues
  35, 58, 83, 106, 130, 159, 187, 230 and 258, all N-terminal to the first TM helix,
  which agrees with the nine c-type hemes reported for the periplasmic domain. The scan
  is reproducible: `cbcL-bioinformatics/cxxch_scan.py` reads the sequence out of
  `cbcL-uniprot.txt` and prints the motif positions; see
  `cbcL-bioinformatics/RESULTS.md`.
- Pfam PF14537 (Cytochrom_c3_2, "Tetraheme cytochrome" domain 98-167), InterPro
  IPR036280 multiheme cytochrome superfamily, IPR012286 tetraheme cytochrome; Gene3D
  1.20.950.20 "Transmembrane di-heme cytochromes, Chain C" covers the membrane domain
  (the NarI/FdnI-type diheme cytochrome b fold).
- PANTHER places it in PTHR35038 (Multiheme cytochrome electron transporters /
  "dissimilatory sulfite reductase SirA") subfamily SF6. Only the N-terminal multiheme c
  domain is shared with the family; the b-type membrane domain is not.
- The SF6 name is misleading rather than a defect. UniProt records the assignment as
  `DR   PANTHER; PTHR35038:SF6; SURFACE LOCALIZED DECAHEME CYTOCHROME C LIPOPROTEIN; 1.`,
  which fits neither an inner-membrane protein nor a nonaheme one. PANTHER subfamily
  names are routinely dominated by one characterised member, so this is most likely a
  correctly-assigned id carrying another member's name, not a misplacement; the id is
  therefore not flagged as a source defect. It does reinforce the
  `FUNCTIONAL_DIVERGENCE` argument behind the GO:0016491 MODIFY: the family's naming
  tracks neither CbcL's topology nor its heme count.
- Comparator accessions used in the review reasons were verified directly (2026-10-28):
  UniProtKB Q747K6 is IMCH_GEOSL, "Cytochrome c-type protein ImcH", Geobacter
  sulfurreducens PCA; UniProtKB Q8E8S0 is CYMA_SHEON, "Tetraheme c-type cytochrome
  CymA", Shewanella oneidensis MR-1. A QuickGO annotation query returns GO:0009055
  (IBA, enables) and GO:0019645 (IBA, involved_in) for both, and GO:0005886 located_in
  on experimental evidence for both, as the reasons state.
- GO:0005887 integral component of plasma membrane, considered as a more specific
  location than GO:0005886, is obsolete: OLS reports it replaced by GO:0005886, and
  QuickGO resolves the id to plasma membrane with "integral component of plasma
  membrane" as a narrow synonym. Plasma membrane is therefore the most specific
  location term available here.

## Literature

- Zacharoff et al. 2016 (abstract only in cache): deletion and complementation study.
  [PMID:26407054 "deletion of cbcL, encoding an inner membrane protein consisting of
  b-type and multiheme c-type cytochrome domains, severely affected reduction of low
  potential electron acceptors such as Fe(III)-oxides and electrodes poised at -0.1 V vs.
  SHE"]; [PMID:26407054 "Expression of cbcL in trans increased growth at low redox
  potential and restored features to cyclic voltammetry"]; model:
  [PMID:26407054 "CbcL is a component of a second electron transfer pathway out of the G.
  sulfurreducens inner membrane that dominates when redox potential is at or below -0.1 V
  vs. SHE"].
- Levar et al. 2017 (full text): the CbcL- and ImcH-dependent pathways are both needed
  for complete reduction of Fe and Mn minerals [PMID:28045456 "G. sulfurreducens requires
  both the CbcL- and the ImcH-dependent electron transfer pathways for complete reduction
  of a variety of Fe and Mn minerals"]. With Fe(III)-citrate, [PMID:28045456 "the ΔcbcL
  mutant strain (lacking the low-potential system) was unable to reduce all Fe(III), and
  the redox potential only lowered to –0.15 V"]. Loss of CbcL raises yield:
  [PMID:28045456 "Mutants lacking the low-potential, CbcL-dependent pathway had higher
  growth yields with both soluble and insoluble Fe(III)."]. Important caveat stated by
  the authors: [PMID:28045456 "direct roles for ImcH and CbcL in the movement of electrons
  out of the quinone pool have not been demonstrated"]. Expression: [PMID:28045456 "The
  genes for ImcH and CbcL are constitutively expressed"].
- Antunes et al. 2022 (full text): first biochemistry. The periplasmic domain (residues
  30-279) was expressed in E. coli. [PMID:35620088 "CbcL has a transmembranar di-heme
  b-type cytochrome domain with six helices, linked to a periplasmic cytochrome domain
  with nine c-type heme groups"]; [PMID:35620088 "its nine hemes are low-spin and all
  coordinated by two histidine residues"]; [PMID:35620088 "Compared to the one of the
  periplasmic cytochrome PpcA (−138 mV), the reduction potential value of CbcL (−194 mV)
  is more negative."]; [PMID:35620088 "direct electron transfer from reduced CbcL to
  oxidized PpcA was observed in 1D 1H NMR titrations"]; complex is weak
  [PMID:35620088 "The solid line represents the fitting for a Kd of 57 ± 9 μM."].
  The authors call CbcL a quinone oxidoreductase [PMID:35620088 "Cytochrome CbcL is one
  of the inner membrane quinone oxidoreductases identified in G. sulfurreducens"], but
  quinol oxidation was not assayed (only the soluble c-heme domain was studied).
- Joshi et al. 2021 (abstract): CbcBA is a third, unrelated inner-membrane
  cytochrome; [PMID:34423503 "deletion of cbcL (an unrelated bc-cytochrome essential
  near -0.15 V) in ΔcbcBA increased yield to 220%"].
- Howley et al. 2023 (abstract): transcript-level association of cbcL with the
  medium-potential pathway [PMID:37459687 "inner membrane (Medium: cbcL)"].

## Synthesis

CbcL is a two-domain inner-membrane cytochrome: a six-helix membrane domain predicted to
carry two b-type hemes, and a periplasmic nonaheme c-type cytochrome domain. Genetics
place it as necessary for respiration to extracellular acceptors at or below about
-0.1 V vs SHE (Fe(III) oxides, low-potential electrodes); biochemistry shows the
periplasmic domain can pass electrons to the periplasmic triheme cytochrome PpcA. The
working model is that CbcL takes electrons from the menaquinol pool and injects them into
the periplasmic cytochrome network, but quinol oxidation has not been shown.

GO decisions:
- GO:0016491 oxidoreductase activity (IBA): the PAINT node PTN002858933 is seeded by
  S. oneidensis SirA (a catalytic sulfite reductase) and E. coli NrfB (an electron
  carrier). CbcL shares only the cytochrome-c3-like multiheme domain; the activity
  actually demonstrated for CbcL is cytochrome-to-cytochrome electron transfer, so
  MODIFY to GO:0009055 electron transfer activity.
- GO:0030313 cell envelope (IEA, ARBA SubCell): true but general; MODIFY to
  GO:0005886 plasma membrane (six Phobius TM helices plus literature "inner membrane").
- NEW: GO:0020037 heme binding (IDA, PMID:35620088), GO:0019645 anaerobic electron
  transport chain (IMP, PMID:26407054). Comparator check: ImcH (Q747K6) and S. oneidensis
  CymA (Q8E8S0), inner-membrane cytochromes in the same role, both carry GO:0009055
  and GO:0019645 in GOA (QuickGO query, 2026-10-28), so this is the established
  convention, and CbcL does part of the work (it carries the electrons).

## CMMMech claims (do not edit CMMMech; notes for its curators)

CMMMech records asbolane, feitknechtite, pyrochroite, akaganeite, rhodium and
chromite-ore-processing-residue cite Q74GH2 with functional_role "Inner-membrane
b/c-type cytochrome CbcL (GSU0274) required for extracellular electron transfer to
lower-redox-potential Fe(III) phases" (or "...metal and mineral acceptors").

- "Required ... lower-redox-potential Fe(III) phases" is supported for Fe(III)
  (oxyhydr)oxides, Fe(III)-citrate in its late, low-potential phase, and electrodes at or
  below -0.1 V (PMID:26407054, PMID:28045456).
- "metal and mineral acceptors" (rhodium, COPR) is broader than the evidence: no cbcL
  mutant has been tested with Rh(III), Pd(II) or Cr(VI); the CMMMech evidence entries
  themselves say individual cytochrome genes were not mutated. Representative-example
  status is fine; "required" should not be read as shown for those metals.
- For asbolane/Mn phases, Levar 2017 supports a role in late-stage Mn and Fe mineral
  reduction generally, but CbcL's direct contact with any mineral is not expected (it is
  an inner-membrane protein; outer-membrane and extracellular cytochromes mediate
  contact).
- The "b/c-type cytochrome" description is right; whether CbcL oxidises menaquinol is
  still an inference (PMID:28045456 caveat).
