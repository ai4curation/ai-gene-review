---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKAP10
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: O43572
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKAP10 (human)

## Current model (mechanistic narrative)

AKAP10 (D-AKAP2) is a dual-specific A-kinase anchoring protein that organizes compartmentalized PKA signaling at mitochondria and the endocytic recycling system [PMID:11248059, PMID:19797056]. It anchors both type I (RIα) and type II (RIIα) PKA regulatory subunits through a C-terminal amphipathic helix that engages the dimerization/docking domains of each subunit, with dual specificity arising from a register shift in how the AKAP helix packs against RIα versus RIIα [PMID:9326583, PMID:20159461]. Beyond PKA, AKAP10 nucleates a polyvalent membrane scaffold: a C-terminal PDZ-binding motif recruits PDZK1 (and to a lesser extent NHERF-1), and high-affinity PDZK1 engagement requires prior formation of the AKAP10:PKA complex, coupling kinase anchoring to transporter regulation [PMID:14531807, PMID:25348485]. Its N-terminal tandem RGS domains bind GTP-loaded Rab4 and Rab11 and promote accumulation of recycling cargo such as the transferrin receptor in the Rab4/Rab11-positive recycling compartment [PMID:19797056]. In vivo, disruption of the AKAP10 C-terminus in mice heightens cholinergic cardiac responses and produces arrhythmias, establishing AKAP10 as a regulator of cardiac rhythm through the autonomic signaling pathway [PMID:17485678].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion, GO:0005768 endosome
- **pathway (Reactome):** *(none)*
- **partners:** PRKAR1A, PRKAR2A, PDZK1, NHERF1, RAB11A, RAB4A
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | Medium | D-AKAP2 (AKAP10) binds both type I (RIα) and type II (RIIα) regulatory subunits of PKA via a 40-residue C-terminal R-binding domain that interacts with the N-terminal dimerization domain of RIα and RIIα, making it a dual-specific AKAP. A putative RGS domain was identified near the N-terminal region. | PMID:9326583 | Proceedings of the National Academy of Sciences of the United States of America |
| 2001 | High | Full-length human D-AKAP2 (AKAP10, 662 residues) localizes predominantly to mitochondria, as demonstrated by immunocytochemistry, immunohistochemistry, and tissue fractionation in mouse, rat, and human cells. In vivo association with PKA in mouse brain was confirmed by cAMP-agarose pull-down. | PMID:11248059 | Proceedings of the National Academy of Sciences of the United States of America |
| 2002 | Medium | Deuterium exchange-mass spectrometry and limited proteolysis revealed that D-AKAP2 has two distinctly folded domains: an N-terminal putative RGS domain and a C-terminal region containing a highly protected PKA binding site and a solvent-accessible PDZ binding motif, flanked by disordered regions. | PMID:12206784 | Journal of molecular biology |
| 2003 | Medium | D-AKAP2 binds PDZK1 (and to a lesser extent NHERF-1) through its C-terminal PDZ binding motif, anchoring PKA to these scaffold proteins in renal proximal tubular cells. The interaction was confirmed by pull-down experiments and co-immunoprecipitation from transfected opossum kidney cells. | PMID:14531807 | Kidney international |
| 2007 | Medium | Heterozygous disruption of the Akap10 C-terminus (final 51 aa) in mice increases cardiac response to cholinergic signals and causes cardiac arrhythmias and premature death, establishing AKAP10 as a regulator of heart rhythm via the cholinergic/autonomic pathway. | PMID:17485678 | Proceedings of the National Academy of Sciences of the United States of America |
| 2009 | High | The two tandem RGS domains of D-AKAP2 interact with Rab11 and GTP-bound Rab4 (the first demonstration of RGS domains binding small GTPases). D-AKAP2 regulates endocytic recycling: knockdown by RNAi redistributes Rab11 and transferrin receptor to the cell periphery and increases the rate of transferrin recycling, indicating D-AKAP2 promotes accumulation of recycling cargo in the Rab4/Rab11-positive endocytic recycling compartment. | PMID:19797056 | The Journal of biological chemistry |
| 2010 | High | Crystal structure of the D-AKAP2 AKB helix in complex with the RIα D/D domain revealed a novel helical register shift compared to the RIIα:D-AKAP2 complex, explaining the molecular basis for D-AKAP2 dual-specificity. The RIα D/D domain presents an extensive surface through a well-formed N-terminal helix, and a redox-sensitive disulfide in RIα affects AKAP binding. | PMID:20159461 | Structure (London, England : 1993) |
| 2014 | High | Crystal structure of the D-AKAP2:PKA RII:PDZK1 ternary complex showed that the disordered C-terminal segment of D-AKAP2 becomes ordered upon binding, presenting an α-helix to PKA RII and a β-strand to PDZK1. Formation of the D-AKAP2:PKA binary complex is a prerequisite for high-affinity interaction with PDZK1, nucleating a polyvalent scaffold that links PKA signaling to transporter regulation. | PMID:25348485 | Protein science : a publication of the Protein Society |

## Citations

- PMID:11248059
- PMID:12206784
- PMID:14531807
- PMID:17485678
- PMID:19797056
- PMID:20159461
- PMID:25348485
- PMID:9326583
