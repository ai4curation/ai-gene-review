# tol-1 (C. elegans) review notes

## Status of inputs

- No Falcon deep-research job was queued for worm tol-1 in this batch (no `dr-worm-tol-1` log and no
  `worm tol-1 dr=` line in the batch task output), so this review was done from the UniProt record,
  the GOA rows and the cached primary literature below. No `-deep-research-*.md` file exists.
- UniProt Q9N5Z3 is an unreviewed TrEMBL entry (1221 aa): signal peptide 1-23, LRR ectodomain,
  single TM helix 997-1021, cytoplasmic TIR domain 1054-1178. PDB 8SUF covers the ectodomain (26-996)
  in complex work with LAT-1.

## Identity

- TOL-1 is the sole Toll/TLR family receptor in C. elegans
  [PMID:26279230 "The sole TLR of C. elegans--TOL-1--is required for a pathogen-avoidance behavior"].
- It is a cell-surface receptor with two LRR domains, a TM helix and a TIR domain
  [PMID:40588662 "is a cell surface receptor with two extracellular leucine-rich repeat (LRR) domains, one transmembrane helix and a cytoplasmic Toll–interleukin receptor 1 receptor (TIR) domain"].
- Phylogenetically its TIR clusters with Drosophila Toll, Nv-TLR and human TLR4 TIRs
  [PMID:29109290 "the TIR domain of human TLR4 (Hu-TLR4) clusters with the TIR domains of Nv-TLR, TOL-1, and Drosophila Toll rather than with any other human TLR"].
  It is structurally a multiple-cysteine-cluster Toll-type receptor, not a vertebrate PRR-type TLR;
  C. elegans lacks MyD88 and NF-kappaB [PMID:23112184 "a clear immune function of the TLR homolog TOL-1 is controversial and central components of vertebrate TLR signaling including the key adapter protein myeloid differentiation primary response gene 88 (MyD88) and the transcription factor NF-κB are not present"].

## Development (strongest, most recent evidence)

- Pujol 2001: of tol-1, trf-1, pik-1, ikb-1 deletion mutants, only tol-1 is required for development
  [PMID:11516642 "Of these four genes, only tol-1 is required for nematode development"].
- Carmona-Rosas 2025: TOL-1 LRR binds the lectin domain of the adhesion GPCR LAT-1 (latrophilin);
  KD ~186-200 nM by SPR; crystal/cryo-EM structure
  [PMID:40588662 "we identified TOL-1, the sole Toll-like receptor in Caenorhabditis elegans, as a ligand for the C. elegans latrophilin, LAT-1"],
  [PMID:40588662 "We observed a dissociation constant (KD) of 186 nM for WT TOL-1 and LAT-1"].
  Interface mutations (TOL-1 Q712A/Y713A/G714A/N715A) that do not affect surface display phenocopy
  the deletion allele: embryonic arrest, malformed embryos, reduced brood size
  [PMID:40588662 "Because simultaneous substitution of these four TOL-1 residues, which are critical for LAT-1 binding in vitro, phenocopy the effect of the tol-1 deletion allele in vivo, we propose that the LAT-1-binding surface of TOL-1 is essential for C."].
  Interactions mostly in trans (mutually exclusive expression).
  Note that in this complex the paper frames TOL-1 as the ligand of LAT-1; whether TOL-1 itself
  transduces a signal via its TIR domain upon LAT-1 binding is not shown.

## Pathogen avoidance / BAG neuron development

- Pujol 2001: tol-1 mutants defective in avoidance of Serratia marcescens; tol-1, trf-1, pik-1,
  ikb-1 not important for resistance to several pathogens
  [PMID:11516642 "None of them are important for the resistance of C. elegans to a number of pathogens"],
  [PMID:11516642 "The tol-1 mutants are defective in their avoidance of pathogenic S. marcescens, although other chemosensory behaviors are wild type"].
- Brandt & Ringstad 2015: TOL-1 acts in BAG CO2-sensing neurons, cell-specifically required and
  rescued there, regulates BAG gene expression, and acts with trf-1, pik-1, ikb-1 and pmk-3
  (a p38) to promote BAG development and function
  [PMID:26279230 "for pathogen avoidance TOL-1 signaling is required in the chemosensory BAG neurons, where it regulates gene expression and is necessary for their chemosensory function"],
  [PMID:26279230 "Genetic studies revealed that TOL-1 acts together with many conserved components of TLR signaling"].
  This is a developmental/permissive role enabling a behaviour, not acute microbe recognition
  [PMID:26279230 "by promoting the development and function of chemosensory neurons that surveil the metabolic activity of environmental microbes"].
- 2024: TOL-1 signals in neurons via PMK-1 to limit foraging [PMID:39532199 abstract-only].

## Immunity (contested)

- Tenor & Aballay 2008: tol-1(nr2033) killed by Salmonella enterica, pharyngeal invasion; required for
  ABF-2 and HSP-16.41 expression [PMID:17975555 "C. elegans tol-1(nr2033) mutants are killed by the human pathogen Salmonella enterica"].
  Abstract only in cache.
- Conflicts: Pujol 2001 (no role in resistance to several pathogens); Hydra paper calls immune role
  "controversial" (PMID:23112184). Kamaladevi 2016 (PMID:27338631, abstract-only) reports tol-1 mutant
  hypersusceptibility to K. pneumoniae after L. casei pretreatment - weak, single-lab.
  Sugawara & Sakamoto 2019 (PMID:31384522): tol-1 mutants show *increased* expression of innate immune
  genes on B. infantis, i.e. not a simple positive immune signalling role.

## Curation decisions (summary)

- GO:0038023 signaling receptor activity (IBA): ACCEPT (TM receptor with TIR; genetics places it upstream of trf-1/pik-1/pmk-3 in BAG).
- GO:0007165 signal transduction (IEA): ACCEPT.
- GO:0007166 cell surface receptor signaling pathway (TAS): ACCEPT.
- GO:0009792 embryo development (IMP): ACCEPT - core, reinforced by 2025 LAT-1 work.
- GO:0006952 defense response (IMP, Pujol): MODIFY to GO:0002209 behavioral defense response (what was measured was avoidance behaviour; same paper found no role in resistance).
- GO:0050829 defense response to Gram-negative bacterium (IMP, Tenor): KEEP_AS_NON_CORE - single-study, pathogen-specific, contested.
- NEW: GO:0001664 G protein-coupled receptor binding (LAT-1 is an adhesion GPCR; direct binding, structure, in vivo interface mutants). Comparator: teneurins (other latrophilin partners) carry the parent GO:0005102 signaling receptor binding; GPCR ligands (NPY, POMC, Rspo1) carry GO:0001664, so GPCR binding on a latrophilin ligand is within convention.
- Not proposed: GO:0002224 TLR signaling pathway, GO:0038187 PRR activity - no evidence TOL-1 binds microbial molecules; ligand is LAT-1 (endogenous). GO:0008063 Toll signaling pathway is defined around "the receptor Toll"; raised as a question rather than asserted.
