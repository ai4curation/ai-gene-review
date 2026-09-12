# ICS1 (SID2 / EDS16) review notes — Arabidopsis thaliana

UniProt: Q9S7H8 (ICS1_ARATH). Gene At1g74710. EC 5.4.4.2. PE 1 (protein level).
Synonyms: AtIcs1; SID2 (SALICYLIC ACID INDUCTION DEFICIENT 2); EDS16 (ENHANCED
DISEASE SUSCEPTIBILITY 16); Isochorismate mutase 1; menF-like protein 1.

## Molecular function and catalysis
- Monofunctional isochorismate synthase: chorismate <=> isochorismate, near
  equilibrium (Keq = 0.89). Does NOT convert chorismate/isochorismate to SA
  itself (no isochorismate pyruvate lyase, IPL, activity).
  [PMID:17190832 "AtICS1 acts as a monofunctional isochorismate synthase (ICS),
  catalyzing the conversion of chorismate to isochorismate (IC) in a reaction
  that operates near equilibrium (K(eq) = 0.89). It does not convert chorismate
  directly to SA (via an IC intermediate)"]
- Kinetics: Km 41.5 uM for chorismate, kcat 38.7 min-1; Mg2+ cofactor (Km 193 uM);
  pH optimum 7.5-8; active at 4 C.
  [PMID:17190832 "AtICS1 exhibits an apparent K(m) of 41.5 mum and k(cat) = 38.7
  min(-1) for chorismate"]
- Monomer (UniProt SUBUNIT). RHEA:18985; UniPathway UPA00025 (salicylate
  biosynthesis). PDB 8W6V / 8W71 (X-ray, residues 46-569).

## Localization
- Chloroplast/plastid stroma. N-terminal transit peptide 1-45.
  [PMID:17190832 "we show that AtICS1 is a plastid-localized, stromal protein
  using chloroplast import assays and immunolocalization"]
  [PMID:18451262 "the ubiquitous stromal localization of both of the ICS:GFP
  fusions"]

## Core biological process — salicylic acid biosynthesis
- Defining genetics: SID2/ICS1 required for pathogen-induced SA; committed step.
  [PMID:11734859 "SA is synthesized from chorismate by means of ICS, and that SA
  made by this pathway is required for LAR and SAR responses"]
- ics1 single mutants retain only ~5-10% SA after induction; redundancy with ICS2
  and an ICS-independent (phenylpropanoid) route account for residual SA.
  [PMID:18451262 "the ics1 mutant still exhibits 5% to 10% of SA compared to the
  wild type after adequate stimulation"]

## Phylloquinone biosynthesis (non-core, redundant with ICS2)
- ICS1 supplies isochorismate, the precursor of phylloquinone; unequal redundancy
  with ICS2.
  [PMID:18451262 "This unequal redundancy relationship was also observed for
  phylloquinone, another isochorismate-derived end product"]
- ics1 ics2 double mutant is devoid of phylloquinone and seedling lethal
  (photosynthetic lesions; phylloquinone is a PSI electron acceptor) — from UniProt
  DISRUPTION PHENOTYPE and PMID:16617180. menF-like ICS branch separated from the
  PHYLLO locus during plant evolution.
  [PMID:16617180 "enabled a metabolic branch from the phylloquinone biosynthetic
  route to independently regulate the synthesis of salicylic acid required for
  plant defense"]

## Downstream SA-dependent physiology (KEEP_AS_NON_CORE; acts_upstream)
All modeled with acts_upstream_of_or_within because ICS1 acts by making SA, not by
directly executing these processes:
- SAR / local resistance [PMID:11734859; PMID:17419843].
- Defense response to bacterium / Gram-negative bacterium; stomatal immunity
  [PMID:16959575 "stomatal closure is part of a plant innate immune response to
  restrict bacterial invasion"], [PMID:29253890 sid2 reduced DC3000 defense].
- Pathogen-/drought-triggered leaf abscission
  [PMID:29253890 "plants with reduced levels of SA, NahG and sid2, had
  quantitatively reduced abscission"]. sid2 was the LEAST compromised defense
  mutant tested (ICS2 likely partially redundant in flowering-stage tissues).
- Response to cold: ICS1 cold-induced (with CBP60g, SARD1); cold SA configures the
  transcriptome but not freezing tolerance.
  [PMID:23581962 "this chilling-induced SA biosynthesis proceeds through the
  isochorismate synthase (ICS) pathway, with cold induction of ICS1"]
- Response to bacterium (S. aureus): SA-mediated [PMID:15842626].

## Removed annotation
- GO:0031348 negative regulation of defense response (IMP, PMID:16732289): the
  cited paper concerns mlo powdery-mildew resistance and explicitly shows it is
  INDEPENDENT of SA/ET/JA. No support for ICS1 negatively regulating defense.
  [PMID:16732289 "mlo resistance in A. thaliana does not involve the signaling
  molecules ethylene, jasmonic acid or salicylic acid"]. Action: REMOVE.

## Notes on a borderline term
- GO:0050832 defense response to fungus (PMID:17513501): the actual pathogen is
  the OOMYCETE Pythium irregulare (not a true fungus), and SA plays only a minor
  role vs JA. Kept as non-core with a caveat noted in the review reason.

## Isoforms
- Two isoforms via alternative splicing: Q9S7H8-1 (displayed) and Q9S7H8-2
  (VSP_034699, altered C-terminus 553-569). Functional consequences of isoform 2
  not characterized in the available literature.

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)
Source: `file:ARATH/ICS1/ICS1-deep-research-falcon.md`. This review-level report
corroborates and extends the existing annotations; it did not surface any new
verifiable GO IDs, so no NEW annotations or proposed_new_terms were added, and no
UNDECIDED actions required resolution (none were present).

- Quantitative dominance of the ICS1/SA-biosynthesis role:
  [file "ICS1 contributes ~90% of pathogen-induced SA accumulation"] (with
  ics1/sid2/eds16 retaining only ~5-10% WT SA), reinforcing GO:0009697 as the
  core process. Added as supporting_text on the IEA SA-biosynthesis annotation
  and on the SA core_function.
- Enzymatic substrate context: chorismate is
  [file "a plastid-derived metabolite at the branch point of aromatic compound
  biosynthesis"] and its product isochorismate
  [file "is the committed precursor for SA in the Arabidopsis ICS route"].
  Added to GO:0008909 (IEA) and the SA core_function respectively.
- Chloroplast/plastid localization corroborated:
  [file "the ICS step is the only SA-biosynthetic step occurring in chloroplasts"].
  Added to the IEA chloroplast and IEA plastid localization annotations.
- SAR mechanism: de novo ICS1 induction in distal tissue, not just SA transport,
  [file "linking local-to-systemic signaling to renewed SA synthesis in distal
  tissue rather than relying solely on long-distance transport of SA from the
  infection site"]. Added to both systemic acquired resistance (GO:0009627)
  annotations.
- Additional context not used as annotation evidence (no verifiable GO IDs from
  GOA/UniProt): plastid-to-cytosol pathway architecture (ICS1 -> EDS5 ->
  PBS3/EPS1), positive regulators (SARD1/CBP60g, TGA1/4, H2O2-CHE), and negative
  regulators (NAC90/61/36, CAMTAs, WRKYs). These describe the regulatory and
  downstream network around ICS1 rather than ICS1's own molecular function, so
  they remain background only.

## PR #1417 review fixes (2026-06-06)

- GO:0050832 "defense response to fungus" (PMID:17513501, Pythium irregulare):
  P. irregulare is an OOMYCETE (stramenopile), not a true fungus. Changed
  action KEEP_AS_NON_CORE -> MODIFY with proposed_replacement_terms
  GO:0002229 "defense response to oomycetes". Verified via QuickGO API
  (https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0002229):
  name="defense response to oomycetes", isObsolete=false. (Broader verified
  options were GO:0098542 "defense response to other organism" and GO:0006952
  "defense response"; chose the most specific verified term.)
- Schema fix: core_functions[*].directly_involved_in must be a YAML list.
  Converted both single-mapping occurrences (GO:0009697 SA biosynthesis;
  GO:0042372 phylloquinone biosynthesis) to list items.
- Validation: ✓ Valid (1 non-blocking warning about phylloquinone term in
  existing_annotations; term is in fact present).
