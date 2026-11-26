# asd-1 (C. elegans, UniProt G5EEW7): manual literature synthesis

No deep-research provider was available for this review, so this synthesis was
compiled by hand from cached publications (`publications/PMID_*.md`), PubMed
searches and the UniProt record. Every claim carries inline provenance.

## Identity and domain architecture

- asd-1 (R74.5, WBGene00011279) encodes a 404-aa protein with one RRM domain (residues 100-176) [file:worm/asd-1/asd-1-uniprot.txt "DOMAIN          100..176"].
- It belongs to the RBFOX1-like family [file:worm/asd-1/asd-1-uniprot.txt "InterPro; IPR047131; RBFOX1-like."] and has the FOX1-type RRM [file:worm/asd-1/asd-1-uniprot.txt "InterPro; IPR034237; FOX1_RRM."]. PANTHER subfamily: PTHR15597:SF49.
- The NMR structure of residues 97-189 is PDB 2MGZ [file:worm/asd-1/asd-1-uniprot.txt "STRUCTURE BY NMR OF 97-189."].
- The C-terminus (...RRFAPY) is a PY-type NLS. Deleting the last 7 residues abolishes nuclear localization of HA-ASD-1 in HeLa cells [PMID:23468662 "indicating that the C-terminal portions of ASD-1 and FOX-1 are the sole NLSs"].

## Discovery and the egl-15 FGFR splicing switch

- asd-1 was isolated in a forward screen using fluorescent mutually exclusive exon reporters for egl-15 exons 5A/5B [PMID:17060915 "We identified alternative-splicing defective-1 (asd-1), encoding a new RNA-binding protein of the evolutionarily conserved Fox-1 family, as a regulator of the egl-15 reporter."].
- asd-1 is redundant with fox-1. The double mutant lacks EGL-15(5A) [PMID:17060915 "an asd-1;fox-1 double mutant was defective in the expression of endogenous egl-15 (5A) and phenocopied egl-15 (5A) mutant"].
- SUP-12 is a muscle-specific co-regulator. ASD-1/FOX-1 and SUP-12 bind the egl-15 RNA together [PMID:17923701 "The Fox-1 family and the SUP-12 proteins form a stable complex with egl-15 RNA, depending on the cis elements."], and the asd-1; sup-12 double mutant phenocopies egl-15(5A) [PMID:17923701 "the asd-1; sup-12 double mutant is defective in sex myoblast migration, phenocopying the isoform-specific egl-15(5A) mutant"].
- Structure: the ASD-1 RRM and the SUP-12 RRM sandwich a shared G base on egl-15 intronic RNA [PMID:25132178 "The two RRM domains cooperatively interact with the RNA by sandwiching a G base to form the stable complex."].
- Affinity studies indicate no simple binding cooperativity [PMID:26430555 "there is no simple contribution of binding cooperativity"]. The RBFOX RRM selects UGCAUG [PMID:26430555 "whereas the Fox-1 (RBFOX) family is selective for a (U)-G-C-A-U-G sequence"].

## Neuronal unc-32 exon 7 selection

- ASD-1 and FOX-1 promote unc-32 exon 7a selection in neurons through a UGCAUG stretch in intron 7b [PMID:23468662 "These results led to the conclusion that ASD-1 and FOX-1 regulate the selection of exon 7a from the unc-32 exon 7 reporter via the UGCAUG stretch in intron 7b in the nervous system."].
- EMSA with full-length recombinant ASD-1 shows direct, sequence-dependent binding [PMID:23468662 "demonstrating direct and specific binding of ASD-1 and FOX-1 to the UGCAUG stretch"].

## Genome-wide targets

- ASD-1 and FOX-1 are widely expressed in the neuromuscular system [PMID:29121637 "Both ASD-1 and FOX-1 are widely expressed in the neuromuscular system"].
- RNA-seq of asd-1 mutants finds exon changes with GCAUG motifs enriched in flanking introns. Targets overlap with those of FOX-1, MEC-8 and EXC-7, which suggests combinatorial control [PMID:29121637].

## Physical interactions

- A genome-scale Y2H screen reported an ASD-1-SUP-12 interaction (PMID:14704431; source of the GO IPI row). UniProt lists the same pair [file:worm/asd-1/asd-1-uniprot.txt "G5EEW7; O45189: sup-12; NbExp=3"].

## Gaps

- No CLIP data exist for ASD-1. No isoform-specific cytoplasmic function is known. Most ASD-1 papers are abstract-only in the cache (17060915, 17923701, 25132178, 25183497).
