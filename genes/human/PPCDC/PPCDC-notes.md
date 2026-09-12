# PPCDC (Q96CD2) review notes

Human **PPCDC** = phosphopantothenoylcysteine decarboxylase (gene synonym COAC; ORF names MDS018,
UNQ9365/PRO34154). UniProt entry `COAC_HUMAN`, 204 aa, chromosome 15, HGNC:28107, EC 4.1.1.36.
Source of record: `genes/human/PPCDC/PPCDC-uniprot.txt` (authoritative).

## Core biology (all grounded in the UniProt record unless noted)

- **Function / catalytic activity.** "Catalyzes the decarboxylation of the cysteine moiety of 4-
  phosphopantothenoylcysteine to form 4'-phosphopantotheine and this reaction forms part of the
  biosynthesis of coenzyme A." [file:human/PPCDC/PPCDC-uniprot.txt, CC FUNCTION;
  ECO:0000269|PubMed:11923312, ECO:0000269|PubMed:15581364]. Reaction: `N-[(R)-4-phosphopantothenoyl]-
  L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2` (RHEA:16793, EC=4.1.1.36).
- **Pathway.** "Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5."
  [file:human/PPCDC/PPCDC-uniprot.txt, CC PATHWAY; ECO:0000269|PubMed:11923312]. UniPathway
  UPA00241/UER00354. This is the **third** step of the five-step CoA pathway (pantothenate → CoA).
- **Cofactor.** FMN — "Binds 1 FMN per subunit." [file:human/PPCDC/PPCDC-uniprot.txt, CC COFACTOR;
  ECO:0000269|PubMed:14501115]. FMN-binding residues: pos 59 and 104–107 (BINDING features).
  Member of the **HFCD (homooligomeric flavin containing Cys decarboxylase) superfamily**
  [CC SIMILARITY]. Note: PPCDC/CoaC-type flavoproteins use a bound FMN as a *catalytic* cofactor
  (thiol → thioaldehyde oxidation to delocalize charge during decarboxylation), then re-reduce the
  enethiol; see mechanism paper below.
- **Subunit / complex.** "Homotrimer." [file:human/PPCDC/PPCDC-uniprot.txt, CC SUBUNIT;
  ECO:0000269|PubMed:14501115]. Crystallized in complex with FMN (PDB 1QZU). The
  "phosphopantothenoylcysteine decarboxylase complex" (GO:0071513) in human is the homotrimer; in
  *Saccharomyces* it is a heterotrimer (Cab3/Hal3/Vhs3) — see GO:0071513 definition and PMID:26514574.
- **Active site.** Cys-173 is the proton donor / active-site acid [ACT_SITE 173,
  ECO:0000305|PubMed:15581364]; C173S abolishes activity [MUTAGEN 173: "C->S: Loss of activity."].
- **Location.** Cytosolic (Reactome R-HSA-196840: "PPCDC is cytosolic and exists as a homotrimer,
  binding one FMN cofactor per subunit"). No signal peptide / TM in the UniProt feature table despite
  historical annotation as a "secreted/transmembrane" candidate in the SPDI cDNA screen (PubMed:12975309).
- **Expression.** HPA: low tissue specificity; expressed broadly (Bgee: blood + 145 other tissues).

## Key primary references

- **PMID:11923312** (Daugherty et al. 2002, J Biol Chem) — comparative-genomics identification and
  reconstitution of the human CoA pathway; identified human PPCDC, verified activity by E. coli
  complementation and in-vitro reconstitution. RP line: "IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY,
  AND PATHWAY." Abstract-only in cache (`full_text_available: false`) but the abstract explicitly names
  "phosphopantothenoylcysteine decarboxylase" among the four human enzymes identified and verified.
  Basis for the EXP/IDA `phosphopantothenoylcysteine decarboxylase activity` and IDA
  `coenzyme A biosynthetic process` annotations.
- **PMID:15581364** (Strauss et al. 2004, Biochemistry) — mechanistic study on human PPC-DC; trapped
  a covalently bound enethiolate intermediate via a mechanism-based inhibitor; established Cys-173 as
  active-site acid (C173S mutant). RP line: "FUNCTION, IDENTIFICATION BY MASS SPECTROMETRY, CATALYTIC
  ACTIVITY, AND MUTAGENESIS OF CYS-173." Abstract-only in cache but abstract states enzyme "catalyzes
  the decarboxylation of the cysteine moiety of 4'-phosphopantothenoylcysteine (PPC) to form
  4'-phosphopantetheine (PPantSH)" and uses "a tightly bound flavin cofactor." Basis for the EXP/IDA
  catalytic-activity annotations.
- **PMID:14501115** (Manoj & Ealick 2003, Acta Cryst D) — crystallization/structure of human PPC-DC
  (PDB 1QZU), in complex with FMN. RP line: "X-RAY CRYSTALLOGRAPHY (2.91 ANGSTROMS) IN COMPLEX WITH FMN,
  SUBUNIT, AND COFACTOR." Abstract confirms "essential enzyme in the biosynthesis of coenzyme A" and
  the R3 crystal with four monomers/asymmetric unit. Basis (via UniProt/ComplexPortal) for FMN binding
  (IDA), the decarboxylase complex (part_of), identical-protein-binding (homotrimer), and NAS CoA-process.

## Interaction annotations (IPI / IntAct high-throughput screens)

`protein binding` (GO:0005515) IPI annotations derive from three large binary-interactome / proteomics
screens: **PMID:25416956** (Rolland et al., human interactome map), **PMID:31515488** (variant-effect
interactome), **PMID:32296183** (HuRI reference interactome). These cached full texts are high-throughput
screen reports that do not name PPCDC/Q96CD2 in prose; the interactions are recorded in IntAct
(with/from partners include PPIG/Q13427, FOXR1/Q6PIV2, TXN2/Q99757, ZNF232/Q9UNY5, RNF8/O76064, UBE2I,
NAA80, NTAQ1, PLEKHF2, TGM7, SREK1IP1, DDIT4L, and PPCDC self). None of these partners is an established
biological (as opposed to screen-level) interactor of a cytosolic CoA-biosynthesis enzyme; treated as
non-informative `protein binding` and marked over-annotated (per policy: not removed).

`identical protein binding` (GO:0042802): the biologically meaningful self-association is the
**homotrimer** (UniProt SUBUNIT, PMID:14501115; PDB 1QZU). PMID:26514574 (Ríos et al. 2015, yeast
Hal3/Vhs3) is a *S. cerevisiae* study on the heterotrimeric yeast PPCDC and its moonlighting Hal3/Vhs3
subunits; its citation for the human GO:0042802 IDA/IPI (self) is tangential — it supports the
family-level oligomerization concept but is not a human self-interaction assay. Kept (IPI experimental,
not removed) but flagged low-relevance in reference_review.

## Isoform note

Two isoforms. Isoform 2 (Q96CD2-2, VSP_044802) deletes residues 1–78, removing part of the FMN-binding
region; Reactome R-HSA-196840 notes it "lacks the protein's FMN-binding domain and would thus appear to
be nonfunctional if it is expressed." Its Met-1 is also affected by a polymorphism (rs2304899) replacing
the initiation ATG. No annotations are isoform-specific in GOA.

## Curation summary

Core = the FMN-dependent decarboxylase catalyzing CoA-pathway step 3, in the cytosol, as a homotrimer.
- ACCEPT experimental / well-supported: EXP & IDA GO:0004633 (decarboxylase activity), IDA GO:0010181
  (FMN binding), IDA GO:0015937 (CoA biosynthesis, PMID:11923312), IBA equivalents, TAS Reactome CoA
  process & cytosol, IPI part_of decarboxylase complex (ComplexPortal/PMID:14501115).
- ACCEPT `identical protein binding` IDA (PMID:14501115, homotrimer) as it reflects the real quaternary
  structure; keep the IPI/screen versions but note lower specificity.
- MARK_AS_OVER_ANNOTATED the three bare `protein binding` (GO:0005515) IPI screen annotations (policy:
  never REMOVE IPI protein binding).
- MODIFY the generic IEA `catalytic activity` (GO:0003824, GO_REF:0000002/InterPro) → specific
  GO:0004633 (the specific activity is already independently supported).
- KEEP the IEA/IBA `phosphopantothenoylcysteine decarboxylase activity` and CoA-process as ACCEPT
  (they agree with experiment).
