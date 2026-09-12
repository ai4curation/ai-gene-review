# ZTL (ZEITLUPE / ADAGIO 1 / ADO1) — Arabidopsis thaliana — research notes

UniProt: F4KAN2 (TrEMBL, AT5G57360). Synonyms: ADAGIO 1 (ADO1), LKP1 (LOV KELCH PROTEIN 1),
FKL2 (FKF1-LIKE PROTEIN 2), ZEITLUPE. 626 aa.

## Domain architecture (from UniProt F4KAN2)
- N-terminal LOV/PAS domain: FT DOMAIN 39..114 "PAS" (LOV is a specialized PAS domain that
  binds an FMN chromophore as a blue-light sensor).
- F-box domain: FT DOMAIN 208..241 "F-box".
- C-terminal Kelch repeats forming a beta-propeller (multiple "FGG" Kelch motifs across
  residues ~280-600; UniProt InterPro Kelch-type beta-propeller; Gene3D 2.120.10.80 Kelch x2).
- UniProt keywords: Flavoprotein, FMN, Chromophore, Photoreceptor protein, Receptor,
  Kelch repeat, Biological rhythms, Flowering, Sensory transduction, Ubl conjugation pathway, Nucleus.
- UniProt PATHWAY: "Protein modification; protein ubiquitination."
- UniProt SIMILARITY: "Belongs to the ADAGIO family."

This is the LOV-domain F-box family (ZTL/FKF1/LKP2): an N-terminal blue-light-absorbing LOV
domain fused to an F-box and C-terminal Kelch repeats — the LOV domain confers blue-light
photoreception, the F-box recruits SKP1/CUL1 to form an SCF E3 ubiquitin ligase, and the Kelch
repeats provide the substrate-binding surface
[WebSearch / Ito et al., Molecular Plant 2012, PMID:22402262 "LOV domain-containing F-box
proteins: light-dependent protein degradation modules in Arabidopsis"].

## Core function (synthesis)
ZTL is a blue-light photoreceptor F-box protein. As the substrate-recognition subunit of an
SCF^ZTL E3 ubiquitin ligase (SKP1–CUL1–F-box) it targets the core clock proteins TOC1
(PRR1) and PRR5 for ubiquitin-dependent proteasomal degradation, setting circadian period.
Its activity is gated by blue light through the LOV/FMN photosensor and by direct interaction
with GIGANTEA (GI), which stabilizes ZTL in a blue-light-enhanced manner.

## Key literature (verified via PubMed search; ZTL-specific)

- [PMID:14654842 Más, Kim, Somers, Kay, Nature 2003 "Targeted degradation of TOC1 by ZTL
  modulates circadian function in Arabidopsis thaliana"] — Genetic + molecular evidence that
  ZTL controls proteasome-dependent degradation of TOC1. "The dark-dependent degradation of
  TOC1 protein requires functional ZTL, and is prevented by inhibiting the proteasome pathway";
  "the physical interaction of TOC1 with ZTL is abolished by the ztl-1 mutation, resulting in
  constitutive levels of TOC1 protein." (Establishes circadian period control via TOC1
  degradation; ubiquitin-dependent protein catabolism; circadian rhythm.)

- [PMID:17704763 Kim et al., Nature 2007 "ZEITLUPE is a circadian photoreceptor stabilized by
  GIGANTEA in blue light"] — Establishes ZTL as a bona fide blue-light photoreceptor.
  "GIGANTEA (GI) is essential to establish and sustain oscillations of ZTL by a direct
  protein-protein interaction"; "The ZTL-GI interaction is strongly and specifically enhanced
  by blue light, through the amino-terminal flavin-binding LIGHT, OXYGEN OR VOLTAGE (LOV)
  domain of ZTL," establishing ZTL as "a blue-light photoreceptor which facilitates its own
  stability through a blue-light-enhanced GI interaction." ZTL is localized mainly in the
  cytoplasm. (Supports response to blue light + photoreceptor activity, LOV/FMN.)

- [PMID:17693530 Kiba, Henriques, Sakakibara, Chua, Plant Cell 2007 "Targeted Degradation of
  PSEUDO-RESPONSE REGULATOR5 by an SCF^ZTL Complex Regulates Clock Function and
  Photomorphogenesis in Arabidopsis thaliana"] — "the Pseudo-Receiver (PR) domain of PRR5
  interacts directly with the F-box protein ZEITLUPE (ZTL) in vitro and in vivo, and ZTL
  targets PRR5 for degradation by 26S proteasomes in the circadian clock and in early
  photomorphogenesis." Explicitly demonstrates an SCF^ZTL E3 ligase complex. (Supports protein
  ubiquitination + ubiquitin-dependent catabolism via SCF complex.)

- [PMID:24004949 Kim et al., Development 2013 "The F-box protein ZEITLUPE controls stability
  and nucleocytoplasmic partitioning of GIGANTEA"] — ZTL and GI heterodimerize in the cytosol;
  ZTL is "localized mainly in the cytoplasm and prevents nuclear localization of GI." (Bears on
  subcellular location: cytoplasm/cytosol is the predominant site of action.)

## Notes on subcellular location
The GOA "nucleus" annotation (GO:0005634) is an IEA from UniProtKB SubCell mapping
(GO_REF:0000044). Experimental literature places ZTL predominantly in the cytoplasm/cytosol,
where it heterodimerizes with GI [PMID:17704763; PMID:24004949 "localized mainly in the
cytoplasm"]. Its substrates TOC1 and PRR5 are nucleocytoplasmic; ZTL itself is reported mainly
cytoplasmic. The bare "nucleus"-only IEA is therefore an incomplete/likely-inaccurate location
call. Kept as UNDECIDED rather than asserting a confident REMOVE, since cytoplasmic SCF action
on shuttling clock proteins does not exclude some nuclear pool, and this is an electronic call
mapped from a SubCell statement we cannot fully audit. A cytoplasm term (GO:0005737) would be
better supported by the literature.

## GO term definitions (QuickGO API, verified)
- GO:0005634 nucleus.
- GO:0006511 ubiquitin-dependent protein catabolic process: "breakdown of a protein...
  initiated by the covalent attachment of a ubiquitin group." (Fits SCF^ZTL targeting TOC1/PRR5
  to the proteasome.)
- GO:0007623 circadian rhythm: "Any biological process in an organism that recurs with a
  regularity of approximately 24 hours." (Fits clock-period control.)
- GO:0009637 response to blue light: change in state/activity as a result of blue light
  (440-500 nm). (Fits LOV photoreceptor.)
- GO:0016567 protein ubiquitination: "one or more ubiquitin groups are added to a protein."
  (Fits SCF E3 ligase activity.)
- GO:0009881 photoreceptor activity (UniProt KW-derived, not in GOA TSV): "absorbing and
  responding to incidental electromagnetic radiation... The response may involve a change in
  conformation." (Fits LOV/FMN blue-light sensing.)

## Annotations present in GOA (5)
1. GO:0005634 nucleus — IEA (GO_REF:0000044, SubCell) — UNDECIDED (see location note).
2. GO:0006511 ubiquitin-dependent protein catabolic process — IEA (ARBA) — ACCEPT (core).
3. GO:0007623 circadian rhythm — IEA (ARBA) — ACCEPT (core).
4. GO:0009637 response to blue light — IEA (ARBA) — ACCEPT (core; LOV photoreceptor).
5. GO:0016567 protein ubiquitination — IEA (UniPathway) — ACCEPT (core; SCF E3 substrate adapter).

Note: UniProt DR lines also list GO:0009881 (photoreceptor activity), GO:0009908 (flower
development), GO:0048511 (rhythmic process) as KW-derived, but these are NOT in the GOA TSV /
review stub, so they are not reviewed as existing_annotations. Photoreceptor activity
(GO:0009881) is captured in core_functions as the molecular function.
