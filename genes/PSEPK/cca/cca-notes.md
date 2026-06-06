# cca (Multifunctional CCA protein) — Pseudomonas putida KT2440 (PSEPK)

UniProt: Q88QU2 (CCA_PSEPK); Gene: cca; OrderedLocusNames=PP_0394; 368 aa.
Evidence level: PE 3 (Inferred from homology). Annotation derives from HAMAP-Rule MF_01261
(Bacterial CCA-adding enzyme, type 1 subfamily). No gene-specific experimental publications
exist for this ortholog; the genome reference is PMID:12534463 (KT2440 complete genome).

## FUNCTION
The CCA protein is the tRNA nucleotidyltransferase (CCA-adding enzyme) that builds and
maintains the universal 3'-terminal CCA sequence of tRNAs by template-independent addition
of CTP and ATP.

[UniProt "Catalyzes the addition and repair of the essential 3'- terminal CCA sequence in tRNAs without using a nucleic acid template."]

[UniProt "Adds these three nucleotides in the order of C, C, and A to the tRNA nucleotide-73, using CTP and ATP as substrates and producing inorganic pyrophosphate."]

[UniProt "tRNA 3'-terminal CCA addition is required both for tRNA processing and repair."]

It is also involved in tRNA quality control/surveillance via tandem (CCACCA) addition that
marks unstable tRNAs for degradation.

[UniProt "Also involved in tRNA surveillance by mediating tandem CCA addition to generate a CCACCA at the 3' terminus of unstable tRNAs."]

[UniProt "While stable tRNAs receive only 3'-terminal CCA, unstable tRNAs are marked with CCACCA and rapidly degraded."]

## CATALYTIC ACTIVITY
Primary (EC 2.7.7.72): CCA-adding nucleotidyltransfer.

[UniProt "Reaction=a tRNA precursor + 2 CTP + ATP = a tRNA with a 3' CCA end + 3 diphosphate"]

Secondary (tandem) CCACCA addition (CCACCA tRNA nucleotidyltransferase, GO:0160016 / RHEA:76235):

[UniProt "Reaction=a tRNA with a 3' CCA end + 2 CTP + ATP = a tRNA with a 3' CCACCA end + 3 diphosphate"]

The protein is described as multifunctional, including 2'-nucleotidase (EC 3.1.3.-),
2',3'-cyclic phosphodiesterase (EC 3.1.4.-) and phosphatase (EC 3.1.3.-) activities for
tRNA end repair, located in a C-terminal HD domain.

[UniProt "Comprises two domains: an N-terminal domain containing the nucleotidyltransferase activity and a C-terminal HD domain associated with both phosphodiesterase and phosphatase activities."]

[UniProt "A single active site specifically recognizes both ATP and CTP and is responsible for their addition."]

## COFACTOR
Mg(2+) is required for nucleotidyltransferase activity; Ni(2+) is noted for the phosphatase
activity.

[UniProt "Magnesium is required for nucleotidyltransferase activity."]

[UniProt "Nickel for phosphatase activity."]

Mg2+-binding residues: positions 21 and 23 (BINDING /ligand="Mg(2+)"). ATP/CTP-binding
residues: 8, 11, 91, 137, 140 (shared single active site for both nucleotides).

## SUBUNIT / FAMILY
[UniProt "Monomer. Can also form homodimers and oligomers."]

[UniProt "Belongs to the tRNA nucleotidyltransferase/poly(A) polymerase family. Bacterial CCA-adding enzyme type 1 subfamily."]

eggNOG COG0617; Pfam PF01743 (PolyA_pol) + PF12627 (PolyA_pol_RNAbd); PANTHER PTHR47545
(Multifunctional CCA protein).

## Curation reasoning (for review)
- Core MF: GO:0004810 CCA tRNA nucleotidyltransferase activity — ACCEPT (defining activity,
  EC 2.7.7.72, RHEA:14433).
- GO:0160016 CCACCA tRNA nucleotidyltransferase activity — ACCEPT (tandem CCACCA addition,
  RHEA:76235; supported directly by the second CATALYTIC ACTIVITY block).
- GO:0004112 cyclic-nucleotide phosphodiesterase activity and GO:0016791 phosphatase
  activity — KEEP_AS_NON_CORE: these are the multifunctional end-repair (HD-domain)
  activities, real per the record but non-core relative to CCA addition.
- GO:0001680 tRNA 3'-terminal CCA addition (BP) — ACCEPT (core process).
- GO:0042780 tRNA 3'-end processing (BP) — ACCEPT/KEEP (broader but accurate parent process).
- GO:0006396 RNA processing (BP) — MARK_AS_OVER_ANNOTATED (very broad; specific tRNA terms
  present).
- GO:0000287 magnesium ion binding (MF) — ACCEPT (Mg2+ is the catalytic cofactor; specific
  metal, supported by COFACTOR + BINDING residues 21/23).
- GO:0005524 ATP binding (MF) — KEEP_AS_NON_CORE / accept: ATP is a substrate; binding is
  real (BINDING residues) but generic relative to the nucleotidyltransferase MF.
- GO:0000049 tRNA binding (MF) — ACCEPT (substrate binding; specific and informative).
- GO:0003723 RNA binding (MF) — MARK_AS_OVER_ANNOTATED (broad parent of tRNA binding).
- GO:0000166 nucleotide binding (MF) — MARK_AS_OVER_ANNOTATED (broad; ATP binding and the
  nucleotidyltransferase MF are more specific).
- GO:0016779 nucleotidyltransferase activity (MF) — MARK_AS_OVER_ANNOTATED (broad parent of
  the specific CCA tRNA nucleotidyltransferase activity).
