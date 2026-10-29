# ARL9 review notes

## Sources
- Affinage: trust gates clear; three papers. Its "Asn in place of Thr35" claim comes from the PMID:15033445 abstract, which is ambiguous about which subfamily it covers. Human ARL9 retains the switch I threonine (T50) in an alignment to ARF1 (ARL9-bioinformatics/RESULTS.md).
- Bioinformatics (`ARL9-bioinformatics/g_motifs.py`): P-loop K31/T32, switch I T50 and NKxD retained; S73 in place of the ARF1 catalytic Q71. The paralog ARL10 has the same Q-to-S change and also a P-loop T-to-S change.
- Human Protein Atlas (antibody staining, checked 2026-10-04): main location plasma membrane, with centriolar satellite and cytosol as additional locations. Not used as evidence, because no study validates it.
- PubMed: ARL9 functional data are limited to a gastric cancer siRNA study (PMID:39776316) and a Xenopus morpholino neurogenesis screen (PMID:25818835).

## Decisions
- GTP binding (IEA) → ACCEPT, based on the conserved nucleotide-binding motifs.
- GTPase activity (IEA) → UNDECIDED: the catalytic Gln is replaced by Ser, and hydrolysis has not been measured. This matches the ARL10 review.
- No NEW terms. The knowledge gap is wholly dark.

## Review round 1 (PR #4183)
- PMID:38606629 (ARF-family BioID, already cached for ARL10) is now cited:
  - It independently lists ARL9 among the GTPases lacking the catalytic Gln.
  - Its BioID data "suggest" a mitochondrial and cytoskeletal role for ARL9, without imaging validation. The description and gap boundary are corrected.
  - ARL10's targeting sequence is 76 residues, per that paper, not "roughly 60"; the suggested question is fixed.
- PMID:15033445's Thr35-to-Asn claim is recorded as a finding_review OVERTURNED by the alignment (ARL9 T50).
- core_functions support for GTP binding now uses only binding-motif snippets.
