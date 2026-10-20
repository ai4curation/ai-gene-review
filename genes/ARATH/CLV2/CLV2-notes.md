# CLV2 (CLAVATA2, AtRLP10, At1g65380; UniProt O80809) curation notes

## Identity
- UniProt O80809, receptor-like protein with extracellular LRRs, a single TM helix, and a short cytoplasmic tail with no kinase domain [PMID:10521522 "We isolated the CLV2 gene and found that it encodes a receptor-like protein (RLP), with a presumed extracellular domain composed of leucine-rich repeats"].

## Key findings
- Genetics: clv2 enlarges shoot and floral meristems, acting in the CLV1/CLV3 pathway for meristems but separately for organ development [PMID:9729492 "CLV2 may function in the same pathway as CLV1 and CLV3 in the regulation of meristem development, but function separately in the regulation of organ development."].
- CLV2/CRN acts in parallel with CLV1 [PMID:18381924 "We show here that the novel receptor kinase CORYNE (CRN) and CLV2 act together, and in parallel with CLV1, to perceive the CLV3 signal."].
- CLV2 and CRN need each other for ER export [PMID:19933383 "We found that CLV2 and CRN require each other for export from the endoplasmic reticulum and localization to the plasma membrane (PM)."].
- Ligand binding is disputed:
  - Radioligand binding gives a Kd of about 32 nM for CLV2 [PMID:20626648 "Binding was saturable for all receptors with a very similar Kd for each receptor: 30 nM for CLV1, 32 nM for CLV2, 26 nM for BAM1, and 36 nM for BAM2"].
  - Photoaffinity labelling found no binding [PMID:25754504 "We showed that CLV2 and RPK2 exhibited no direct binding to the CLV3 peptide."; "the CLV2/CRN complex and RPK2 are not involved in direct ligand interactions but may act as co-receptors."].
  - The deep research (falcon) also notes that direct binding by the physiological heteromer is not established.
  - Decision: core MF is coreceptor activity (GO:0015026). The IMP GO:0001653 is MODIFIED to it, and the CLE IPI rows are MODIFIED to peptide hormone binding (GO:0017046), matching the CLV1 review's use of that term. The MODIFY rests on the radioligand data the curator used; the photoaffinity refutation is stated in each row's summary rather than cited as support, and GO:0017046 is not used as a core function.
- Root: CLV2 is required for the response to CLE peptides that consume the root meristem [PMID:16055633 "Interestingly, clv2 failed to respond to the peptide treatment, suggesting that CLV2 is involved in the CLE peptide signaling."]. CLV2/CRN is needed to sense root-active CLEs, with the main action in the protophloem [PMID:28607033]. CLE14 acts through CLV2 under low phosphate [PMID:28586647 "CLV2 and PEPR2 receptors perceive CLE14 and trigger RAM differentiation"].
- CIK co-receptors [PMID:29581511 "CIKs function as co-receptors of CLV1, CLV2/CRN and RPK2 to mediate CLV3 signalling through phosphorylation."].
- Nematode CLE mimics [PMID:21265896 "CLV2 and CRN are required for perception of nematode CLEs"].

## Decisions summary
- Accepted: plasma membrane, regulation of meristem growth, meristem development, and IBA signaling receptor activity.
- Kept as non-core: ER membrane (transit compartment), root, phloem and organ phenotypes.
- Modified:
  - Protein binding with CRN to signaling receptor binding.
  - Protein binding with CLE peptides to peptide hormone binding.
  - Signal transduction to cell surface receptor signaling pathway.


## PR #4384 review follow-up (2026-10-06)
- Removed PMID:25754504 ("no direct binding") from `supported_by` of the CLE-peptide MODIFY rows: it refutes rather than supports the action; the dispute stays in each row's summary. Reworded `reason` so it justifies the MODIFY instead of claiming non-core.
- Trimmed the GO:0015026 reason: coreceptor activity entails combining with the messenger, so it is not fully neutral on the binding dispute.
