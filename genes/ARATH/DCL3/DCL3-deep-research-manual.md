# DCL3 (Arabidopsis thaliana, AT3G43920, UniProt Q9LXW7) - manual literature synthesis

No deep-research API was available for this review. This file summarises a manual
literature survey using the cached publications in `publications/` and PubMed searches.
All statements carry inline provenance.

## Identity and domain architecture

- 1580-aa Dicer-family endoribonuclease; UniProt: "Belongs to the helicase family. Dicer
  subfamily." Domains: DExH helicase ATP-binding (51-223, DECH box 170-173), helicase
  C-terminal (394-562), PAZ (836-960), two tandem RNase III domains (985-1157,
  1198-1340) and C-terminal dsRBD region (UniProt Q9LXW7 FT lines; Pfam PF00636 x2,
  PF02170, PF00270, PF00271).
- Cryo-EM structure of a DCL3-pre-siRNA complex (PDB 7VG2) [PMID:34648373 "we determined
  the structure of a DCL3–pre-siRNA complex in an active dicing-competent state"].

## Molecular function: 24-nt siRNA-producing ribonuclease III

- DCL3 cleaves dsRNA into 24-nt siRNAs [PMID:24214956 "Dicer-like 3 (DCL3) and Dicer-like 4
  (DCL4) cleave long, perfect double-stranded RNAs (dsRNAs) into 24 and 21 nucleotides (nt)
  small interfering RNAs, respectively"].
- Substrate preference: short dsRNAs with 5'-phosphorylated A/U and 1-nt 3' overhang
  [PMID:24214956 "DCL3 preferentially cleaves short dsRNAs with 5' phosphorylated adenosine
  or uridine and a 1 nt 3' overhang"]. ATP and Mg2+ required in crude/IP assays, but not
  ATP hydrolysis [PMID:24214956 "ATP, but not ATP hydrolysis, is necessary for the
  dsRNA-cleaving activity of DCL3."]. The structure paper calls dicing ATP-independent
  [PMID:34648373 "DCL3 possesses ATP-independent dicing activity"].
- Two RNase III domains form the intramolecular dimer: RNase IIIa cuts the complementary
  strand, RNase IIIb the guide strand [PMID:34648373 "confirming that RNaseIIIa and RNaseIIIb
  are responsible for complementary strand and guide strand cleavage, respectively"].
  Note: residue numbers in PMID:34648373 (e.g. RNase IIIb E1224/D1228/D1316/E1319) are
  about 10 lower than the current UniProt canonical sequence (version 2), where the
  corresponding acidic residues are E1234, D1326, E1329 (UniProt Mg2+ BINDING features).
  I have not established which sequence the paper used, so no residue claims are recorded
  in the review.
- In vivo, DCL3 dices Pol IV-RDR2 ~30-bp dsRNAs into 24- and 23-nt siRNAs
  [PMID:31398324 "The dicer endonuclease DCL3 cuts resulting duplexes to generate 24- and
  23-nt siRNAs."]; precursor-end features form a "dicing code" [PMID:35098919].
- dsRNA binding: [PMID:15821876 "DCL1, DCL3, HYL1 and the four HYL1 homologs exhibit
  significant dsRNA-binding activity"] (abstract only).

## Biological process

- Required for endogenous RDR2-dependent (heterochromatic) siRNAs [PMID:15024409 "unique
  functions for three DCL proteins in miRNA (DCL1), endogenous siRNA (DCL3), and viral siRNA
  (DCL2) biogenesis were identified"]; dcl3 shows loss of heterochromatic marks and
  asymmetric (non-CG) methylation at AtSN1 [PMID:15024409 "In the dcl3-1 mutant, however,
  cytosine methylation was decreased only at asymmetric sites"].
- Partial redundancy: DCL2/DCL4 make some RDR2-dependent siRNAs in dcl3, and DCL3 makes some
  RDR6-dependent siRNAs (tasiRNAs) in dcl4 [PMID:16040244 "In the absence of DCL4, some
  RDR6-dependent siRNAs were produced by DCL2 and DCL3"]; DCL2-4 redundant for siRNA,
  tasiRNA and DNA methylation [PMID:16699516].
- Antiviral: geminivirus genome methylation and recovery require DCL3, with DRB3 and AGO4
  [PMID:24352449 "like dcl3 and ago4 mutants, drb3 plants fail to recover from infection"].
  RNA-virus effects are mostly from dcl2 dcl3 dcl4 triple mutants (PMID:24603811,
  PMID:26023161, PMID:25385769), where DCL4/DCL2 dominate.
- Flowering: dcl1 dcl3 double mutants flower late through elevated FLC [PMID:17579240].
  This is a genetic, indirect phenotype.
- Expression regulation: IBM1 protects DCL3 (and RDR2) from H3K9/non-CG hypermethylation;
  ibm1 lowers DCL3 expression [PMID:22772985 "The mutation of IBM1 induced the
  hypermethylation of H3K9 and DNA non-CG sites within RDR2 and DCL3, which repressed their
  expression."]. This paper concerns regulation of DCL3 expression, not DCL3 activity.

## Localization

- Nuclear GFP fusion [PMID:15024409 "The DCL3–GFP, HEN1–GFP, and GFP–AGO4 fusion proteins
  were detected exclusively in the nucleus"]; nucleolar processing centre with RDR2, AGO4
  and NRPD1b [PMID:16839878 "We show that RDR2, DCL3, AGO4, and NRPD1b (the largest subunit
  of Pol IVb) colocalize with siRNAs within the nucleolus."].

## Partners

- DRB3 (BiFC/co-IP) [PMID:24352449]; DRB2 and DRB5 (Y2H, UniProt citing PMID:15821876).
