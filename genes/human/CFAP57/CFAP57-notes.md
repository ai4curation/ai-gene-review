# CFAP57 (WDR65) review notes

## Deep research status

- `just deep-research human CFAP57 --provider falcon` failed: Edison API authentication
  error ("Failed to authenticate", HTTP 403 Forbidden).
- `just deep-research human CFAP57 --provider perplexity` failed: provider not available
  in this environment ("Provider 'perplexity' not available. Available: falcon, asta,
  openscientist").
- No deep-research file was written. Literature research was done manually (PubMed search
  for CFAP57 / FAP57 / WDR65) using the cached publications in `publications/`.

## Identity

- UniProt Q96MR6, Cilia- and flagella-associated protein 57; alias WDR65. N-terminal WD40
  repeats (EML-like beta-propeller) and long C-terminal coiled coils; PANTHER
  PTHR32215:SF0. Chains i4/i5 in the human respiratory axoneme model PDB 8J07.
- Two transcripts: a long isoform needed in sperm and a short isoform; in mouse both are
  present in testis and trachea [PMID:36752199].
- Disease: spermatogenic failure 95 (SPGF95, MIM:620917), MMAF. One PCD case report.
- Note: an older report linked a WDR65 missense variant to Van der Woude syndrome
  (PMID:21574244, not cached, not used); not relevant to ciliary function.

## Literature findings (with provenance)

### Chlamydomonas FAP57 (IDA8/BOP2)

- "IDA8 encodes flagellar-associated polypeptide (FAP)57/WDR65, a highly conserved WD
  repeat, coiled coil domain protein"; required "for targeting the assembly of a subset of
  inner dynein arms (IDAs) to a specific location in the 96 nm repeat"; "FAP57 forms an
  extended structure that interconnects multiple IDAs and regulatory complexes"
  [PMID:31483737] (full text).
- "FAP57 is important for stabilizing the binding of IDA g (and to a lesser extent the
  binding of IDA d)"; "FAP57 is not required for docking of the N-DRC" [PMID:31483737].
- Orthologues "have been identified in other organisms with motile cilia, but only in
  those species that assemble IDAs" [PMID:31483737].

### Human airway (PCD)

- Bustamante-Marin et al. 2020: homozygous CFAP57 nonsense variant causing exon 11 skipping
  in one PCD subject; "In normal human nasal epithelial cells, CFAP57 localizes throughout
  the ciliary axoneme"; mutant protein "is not incorporated into the axoneme"; "A reduced
  beat frequency and an alteration in ciliary waveform was observed. Knockdown of CFAP57 in
  human tracheobronchial epithelial cells (hTECs) recapitulates these findings"
  [PMID:32764743] (full text).
- fap57 Chlamydomonas mutants "show reduced swimming velocity and altered waveforms"; the
  "g" (DHC7, DHC3) and "d" (DHC2) inner dyneins are reduced [PMID:32764743].
- Only a single PCD subject has been reported; the PCD association is weaker than the
  sperm association.

### Sperm (MMAF)

- Ma et al. 2023: two loss-of-function CFAP57 variants in three Pakistani MMAF families
  "who had no overt ciliary symptoms"; a mouse model of R958* recapitulates MMAF; "CFAP57
  deficiency disrupted the inner dynein arm (IDA) assembly in sperm flagella and that
  single-headed IDAs were more likely to be affected"; mutations affect only the long
  transcript [PMID:36752199] (full text).
- "Ultrastructural analysis of the sperm flagella from CFAP57-mutated individuals revealed
  the presence of a normal 9 + 2 structure with only IDAs' absence" [PMID:36752199].
- Chen et al. 2025: further biallelic variants; mutant mice recapitulate MMAF; CFAP57
  interacts with MYH10, and "both MYH10 and CFAP57 localize to the sperm flagella"
  [PMID:41466333]. The MYH10/IFT88 mechanism is single-study and not used for annotation.
- Tlili et al. 2026: homozygous nonsense variant in an Emirati asthenozoospermic man with
  no PCD signs [PMID:41793497] (abstract only).
- CCDC113 interacts with CFAP57 in co-immunoprecipitation [PMID:39671309].

## Curation judgements

- GOA has only four CC rows (cilium x2, axoneme, sperm flagellum), no MF and no BP.
- Cilium (HPA IDA; ARBA IEA): MODIFY to `GO:0031514 motile cilium`; CFAP57 localizes to the
  axoneme of human airway motile cilia and to sperm flagella, and has no known role in
  primary cilia.
- Axoneme (IEA): ACCEPT. Sperm flagellum (Ensembl Compara IEA from mouse): ACCEPT, supported
  by human patient sperm data.
- NEW `GO:0036159 inner dynein arm assembly`: participation is structural (CFAP57 provides
  the docking/targeting structure for IDAs g and d). Comparator check (QuickGO,
  2026-10-16): CCDC39 and CCDC40, axonemal docking/ruler proteins that specify binding
  sites of IDAs and other complexes, carry this term by IMP.
- NEW `GO:0003341 cilium movement`: reduced beat frequency and altered waveform in patient
  nasal cells and hTEC knockdown, and in Chlamydomonas mutants. Comparator: CCDC39/CCDC40
  carry cilium movement (IMP).
- `GO:0120316 sperm flagellum assembly` not proposed: it has cilium movement among its GO
  ancestors, so proposing both would violate the ancestor/descendant rule. Cilium movement
  was preferred because the airway and Chlamydomonas data are direct measurements of
  ciliary beating. Raised as a question.
- NEW `GO:0005200 structural constituent of cytoskeleton`, consistent with CFAP61 review.
