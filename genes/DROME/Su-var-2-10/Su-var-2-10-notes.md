# Su(var)2-10 (Drosophila melanogaster) — curation notes

UniProt Q7KNF5 (TrEMBL, isoform A, 554 aa). FlyBase FBgn0003612; synonyms dPIAS, ZIMP, CG8068.
PANTHER PTHR10782:SF94 (PIAS family). No Swiss-Prot entry; GOA spreads Su(var)2-10 annotations
across isoform accessions. The rich experimental set (SUMO ligase IMP, piRNA TE silencing IPI/IMP,
JAK-STAT IGI/IDA, lamina/telomere IDA) sits on **A1Z7P5** (QuickGO, checked 2026-10-04); Q7KNF5
carries only 14 rows. Several NEW rows here mirror the A1Z7P5 set.

## Domain architecture (UniProt Q7KNF5)
- SAP 2-36, PINIT 113-278, SP-RING-type zinc finger 310-391, disordered 402-525
  [file:DROME/Su-var-2-10/Su-var-2-10-uniprot.txt].

## Identity and chromosome biology
- Cloned as the PIAS ortholog; essential; PEV suppressor [PMID:11390354 "Su(var)2-10 encodes a
  member of the PIAS protein family, a group of highly conserved proteins that control diverse functions."].
- Localization: [PMID:11390354 "Surprisingly, SU(VAR)2-10 proteins are not localized to mitotic
  chromosomes and in interphase cells are localized to telomeres, the nuclear lamina, and the nuclear lumen."]
- Interphase organisation: [PMID:11390354 "We conclude that telomere–telomere and telomere–lamina
  associations are severely disrupted in Su(var)2-10 mutant polytene nuclei"]. 72% vs 26% of telomeres
  within 1 um of lamina in WT vs mutant.

## SUMO E3 ligase activity
- In vitro auto-SUMOylation; SP-RING C341S abolishes it [PMID:31901446 "Tethering of Su(var)2–10
  C341S mutant failed to promote SUMOylation at the reporter locus, confirming that this mutation
  abolishes SUMO E3 ligase activity of Su(var)2–10"].
- Substrate Bonus (TIF1) [PMID:37999956 "Finally, we showed that Bonus SUMOylation is mediated by the
  SUMO E3-ligase Su(var)2-10"].

## piRNA-guided transcriptional silencing
- [PMID:31901446 "Su(var)2-10 links the piRNA-guided target recognition complex to the silencing
  effector by binding the piRNA/Piwi complex and inducing SUMO-dependent recruitment of the SetDB1/Wde
  histone methyltransferase effector."]
- Co-IP with Piwi, Panx, Arx (ovary and S2) and with SetDB1; SetDB1/Wde bind SUMO via SIMs;
  ligase-dead C341S fails to repress or deposit H3K9me3 [PMID:31901446].
- Genome-wide: [PMID:31901448 "deposition of most of the H3K9me3 mark depends on SUMO and the SUMO
  ligase Su(var)2-10, which recruits the histone methyltransferase complex SetDB1/Wde"]; also
  piRNA-independent repression of tissue-specific euchromatic genes and negative feedback on
  heterochromatin factors.

## JAK/STAT
- [PMID:11504941 "We conclude that the correct dpias/stat92E ratio is crucial for blood cell and eye
  development."]; "dPIAS counteracts the activated STAT92E".
- Reactome R-DME-209296: SU(VAR)2-10 binds phospho-STAT92E dimer and blocks DNA binding.
- Intestinal infection screen: PIAS RNAi -> earlier death after Serratia; gut overexpression ->
  increased survival; mechanism = JAK-STAT control of ISC proliferation / epithelial homeostasis
  [PMID:19520911]. Hence innate-immune-regulation row marked over-annotated.

## NEW-term tests (CLAUDE.md)
- GO:0141006 TE silencing by piRNA-mediated heterochromatin formation: participation = Su(var)2-10
  catalyses the SUMOylation step that recruits SetDB1/Wde. Comparators carrying the term in FlyBase
  GOA: piwi, Panx, arx, egg, wde, Su(var)205, and Su(var)2-10 itself on A1Z7P5. Passes.
- GO:0061665 SUMO ligase activity: direct catalytic-mutant evidence. Ancestor terms in GOA
  (acyltransferase activity, catalytic activity acting on a protein) -> MODIFY to this term.
- GO:0046426 negative regulation of JAK-STAT: direct antagonist of activated Stat92E; PIAS family IBA.
- GO:0005652 nuclear lamina, GO:0000781 chromosome telomeric region: IDA in PMID:11390354.
- Not added: GO:0031507 heterochromatin formation (ancestor of GO:0141006 path; redundant).

## Deep research check
Su-var-2-10-deep-research-openscientist.md: core claims verified against the primary papers above.
Domain-mechanism details (PINIT substrate selection, SAP targeting) are ortholog inferences (Siz1/SIZ1)
and were not independently verified. PMID:41500791 (autophagic degradation of Su(var)2-10, 2026)
cached but not used for annotation.

## Human ortholog
No ISO rows on Q7KNF5, so no donor-side review of genes/human/PIAS1 was needed; PIAS1 review unchanged.
