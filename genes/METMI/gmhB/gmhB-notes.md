# gmhB: source-specific archaeal ADP-heptose review

## 2026-10-25 manual primary-source review
The official archived record A0A2L1CCN4 is from DSM2067/JJ, not S2. The archived identifier was retired because its proteome is not a reference proteome. See the adjacent source snapshot and the archival-fetch wrapper under ../gmhA1/gmhA1-bioinformatics for URL, entry version and hashes. Current UniProt returned an empty text record; the archival source was fed unchanged through the existing fetch/seed pipeline. Live QuickGO returned zero annotations. GOA seeded no annotation rows to adjudicate, and that absence is not an ND assertion; one NEW molecular-function row was added in the 2026-11-02 round below. Only one specific molecular function is synthesized in core_functions; no NEW process annotation is manufactured.

Primary PMID39116220, DOI10.1126/science.adk7314, was read in the author-uploaded main article at https://www.researchgate.net/publication/382971859_The_b-_d_-_manno_-heptoses_are_immune_agonists_across_kingdoms . The local cache is abstract-only. The authors introduced four DSM2067 HBE genes into an HBE-negative S2 strain and obtained ADP-heptose. This is heterologous archaeal expression of a DSM2067 ensemble, not native S2 metabolism. Supplementary tables/figureS11 were not accessible (publisher403). We have not verified native DSM2067 product accumulation, pathway flux or its final glycan destination.

GmhB-family hydrolysis of the C7 phosphate of D-glycero-beta-D-manno-heptose 1,7-bisphosphate. PIRNR004682, the specific InterPro/PANTHER classification and genomic context support the beta-HBP phosphatase assignment; exact linkage to the experimental construct remains unverified.

The deposited synthetic construct PP708527.1 (WZW45421.1; HldAMM; source WP_104838492) is exactly identical to A0A2L1CCT7 across all306 residues. The other three archived proteins have no exact match among PP708519–PP708545, which is not proof that they were unassayed. Their direct construct-to-accession link remains unresolved. See ../hldE_2/hldE_2-bioinformatics/RESULTS.md and rawinputs for reproducible comparison. The genome CP026606 places MMJJ_17670(gmhB), MMJJ_17680(hldE_2), MMJJ_17690(hldE_3) and MMJJ_17700(gmhA1) adjacently; independent family/domain annotations support the four activities. This is genomic-context inference for the three without a direct construct match. Another hldE_1 gene exists elsewhere; no role is transferred to it based on its name.

## Scope and annotation decisions
Specific HAMAP/PIRNR rules and InterPro/PANTHER domain classifications support functions. ARBA-only catalytic text, DE labels and electronic GO lines are not used as evidence. The misleading bifunctional HldE labels do not override the separate kinase-only and transferase-only architectures. AMP (not ADP) is transferred from ATP. The product is D,D-heptose; L,D product formation would require the additional HldD epimerase, whose adjacent genomic presence does not prove it participated in the four-gene experiment. No LPS biosynthetic process, DnaA replication role, innate immune receptor activity, broad viral/eukaryotic pathway completeness or nucleotide-donor promiscuity is transferred to these genes.

## Research availability
Falcon/perplexity deep research was attempted for this module and failed with provider authorization/quota errors; no provider report is fabricated. This review uses manual primary-source reading, original sequence deposits and curated family inference. Fitness fetch attempts for this module were unavailable; no archaeal fitness result is claimed. The unresolved construct mapping is recorded explicitly rather than converted into confident direct-assay evidence.

## 2026-10-25 PR #5542 follow-up: anomer inference
The review correctly identified that the generic PIRNR004682 family quotation cannot establish beta-anomer activity by itself. The core now quotes the archived DR:PANTHER PTHR42891:SF1 classification explicitly. That independent sequence classification, the contiguous MMJJ_17670–17700 pathway locus, and the DSM2067 ensemble result jointly justify predicted beta-substrate competence. They do not demonstrate beta preference, alpha inactivity, or an exact match to the assayed phosphatase construct. The description and core state these limits. PMID20050615 supplies comparative evidence that GmhB orthologs differ in anomer preference; its bacterial kinetics are not transferred as measurements of this archaeal protein. No new GOA rows or native S2 pathway claim were added.

## 2026-11-02 — one NEW molecular-function row added

This entry had **zero** GOA rows, so `module_qc.review_completeness`, which requires
`total > 0 and reviewed == total`, could never count it complete however well the
`core_functions` section was argued. Rather than fabricate GOA rows or drop A0A2L1CCN4
from the ADP-heptose module's groundings, one `NEW` `existing_annotation` was added
for the molecular function this review already argued.

- **Term**: GO:0034200 D-glycero-beta-D-manno-heptose 1,7-bisphosphate 7-phosphatase activity
- **Evidence**: `ISS` against `GO_REF:0000024`, the repository's established pattern
  for a curator sequence-similarity assertion.
- **Basis**: InterPro IPR004446 Heptose_bisP_phosphatase, which names this exact activity, plus the curated PIRNR004682 gmhB-family rule and the HAD subfamily IIIA signatures IPR006549 and NCBIfam TIGR01662. Genome context corroborates the step, since the four DSM2067
  loci MMJJ_17670, 17680, 17690 and 17700 are consecutive and their GmhB, RfaE domain
  I, RfaE domain II and GmhA classifications make a complete four-step ensemble
  [file:METMI/hldE_2/hldE_2-bioinformatics/RESULTS.md, "Their GmhB, RfaE domain I,
  RfaE domain II and GmhA classifications identify a complete four-step ensemble."].

Three restraints were kept deliberately. No experimental code is claimed, because the
published reconstitution in PMID:39116220 was ensemble-level in an engineered host and
no assay on this protein alone was reported. No ARBA-only statement is cited as
support anywhere. And no process term was added — the row is molecular function only,
so the earlier note that no NEW process annotation is manufactured still holds.
