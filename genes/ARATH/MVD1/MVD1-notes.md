# MVD1 (At2g38700, O23722) notes

## Identity

- UniProt O23722 (MVD1_ARATH), TAIR and NCBI Gene symbol MVD1; synonyms MDD1 (Henry 2015), AtMVD1.
- 412 aa, diphosphomevalonate decarboxylase family (GHMP superfamily), PANTHER PTHR10977:SF3,
  NCBIfam TIGR01240, InterPro IPR029765 (Mev_diP_decarb) and IPR005935 (Mev_decarb).
- Paralog MVD2 (At3g54250, F4JCU3), 89% identical over the global alignment; Cordier 1999 already inferred a second gene
  [PMID:10344201 "Southern blot analysis on genomic DNA showed that A. thaliana could have at least one homologous MVD gene"].
- Crystal structure with (R)-mevalonate 5-diphosphate (PDB 6N10; Thomas et al. 2019, PMID:31268677).

## Literature search (2026-11-18)

PubMed queries as in the PMK notes (Europe PMC gave HTTP 503). MVD1-specific primary papers found:
Cordier 1999 (PMID:10344201), Simkin 2011 (PMID:21655959), Dellas 2013 (PMID:24327557), Henry 2015
(PMID:26216978), Thomas 2019 (PMID:31268677); genome survey Lange & Ghassemian 2003 (PMID:12777052);
proteomics Aryal 2014 (PMID:25293756). Henry 2015 (PNAS, PMC4538610) full text could not be retrieved
(publisher blocks PMC XML; Europe PMC returned 500), so its MDD data are taken from the curated
UniProt statements that cite it.

## Activity

- Complements yeast MVD mutants [PMID:10344201 "When expressed in yeast, the A. thaliana cDNA complemented both the thermosensitive MN19-34 strain deficient in MVD, and the lethal phenotype of an ERG19 deleted strain."].
- Recombinant enzyme: Km 15.7 uM, kcat 2.0 s-1 for MVAPP (Dellas 2013, via UniProt), and no MPD activity in the in vitro alternative-pathway test [PMID:24327557 "indicating that these MDDs behave as expected from their gene annotations and lack detectable MPD activity"].
- Henry 2015 (via UniProt CC FUNCTION, ECO:0000269): specific for MVAPP; MVAP turned over 10,000-fold less efficiently (Km 26 uM and kcat 3.2 s-1 for MVAPP; Km 2800 uM and kcat 0.033 s-1 for MVAP). MVAP decarboxylation by MVD1 is noise-level relative to the MVAPP reaction and is not annotated.
- Thomas 2019 found no eukaryotic MPD [PMID:31268677 "Finally, no eukaryotic MPD candidates were identified, suggesting the absence of the alternative MVA (altMVA) pathway in all eukaryotes, including, paradoxically, plants"].
- Homodimer by two-hybrid (Cordier 1999; UniProt SUBUNIT, ECO:0000269).

## In vivo

- UniProt DISRUPTION PHENOTYPE (Henry 2015): mvd1 mutant has 50% less campesterol, 30% less sitosterol and 35% less beta-caryophyllene emission. The mild phenotype suggests MVD2 contributes; not verified against the paper.

## Localisation

- Simkin 2011: Arabidopsis MVD-YFP peroxisomal in C. roseus cells [PMID:21655959 "These compartmentalisation results were confirmed using the Arabidopsis thaliana MVK, PMK and MVD sequences fused to YFP."]. The abstract does not say which Arabidopsis MVD was used; UniProt assigns the location to MVD1 (ECO:0000269) and to MVD2 only by similarity.
- Periwinkle MVD exclusively peroxisomal with cycloheximide (PMID:22459325).
- Aryal 2014 crude leaf cytosolic fraction contains MVD1, but also CAT1/2/3, GLO1 and HPR (my QuickGO check, `MVD1-bioinformatics/RESULTS.md`): released peroxisomal matrix contaminates the fraction, so the HDA cytosol row does not distinguish.
- Sequence: the UniProt "PTS2" (40-48, SVTLDPDHL) does not match the PTS2 consensus, is 67% identical to the corresponding segment of cytosolic human and yeast MVD, and overlaps a beta-strand of the crystal structure (`genes/ARATH/PMK/PMK-bioinformatics/RESULTS.md`). No PTS1 (C-terminus ...GLPK).
- Decision: peroxisome rows ACCEPT (direct evidence, rule 2); cytosol rows (HDA, IBA from animal donors, InterPro2GO) MARK_AS_OVER_ANNOTATED.

## IBA / PAINT

- PTN000104601 (PTHR10977 root) gives GO:0004163, GO:0019287 and cytosol (is_active_in). MF and BP are
  sound (AT2G38700 is among the seeds). The cytosol IBD is seeded only by human and mouse MVD; plant
  members' own data say peroxisome, so the cytosol propagation is a lineage/compartment mismatch for
  the plant clade (gene-level MARK_AS_OVER_ANNOTATED; the family review calls it SOUND).
- `just paint-losses ARATH MVD1`: no IRD/IKR on the lineage.
