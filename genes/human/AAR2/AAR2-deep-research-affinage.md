---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AAR2
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: Q9Y312
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AAR2 (human)

## Current model (mechanistic narrative)

AAR2 (yeast Aar2p / human C20ORF4) is an assembly factor for the U5 small nuclear ribonucleoprotein (snRNP) that controls the timing of spliceosome maturation, first identified through its requirement for pre-mRNA splicing in yeast [PMID:1922071]. It is a component of a cytoplasmic precursor U5 snRNP containing Prp8, Snu114, U5 snRNA, and Sm proteins, but is excluded from the tri-snRNP and assembled spliceosome, and its loss impairs snRNP recycling across rounds of splicing [PMID:11720285, PMID:16945917]. Mechanistically, Aar2 binds the RNase H domain of Prp8 and, by extending its C terminus to dock the Jab1/MPN domain onto a composite Aar2-RNase H platform, sterically occludes the binding sites for the Brr2/SNRNP200 helicase while also occupying the RNase H RNA-binding surface to block U4/U6 di-snRNA loading, thereby preventing premature spliceosome activation [PMID:21764848, PMID:23442228]. Crystal structures of the Aar2-Prp8 assembly establish that Aar2 and Brr2 are mutually exclusive binders of Prp8, so that upon nuclear import Brr2 displaces Aar2 to generate the mature, catalytically competent U5 snRNP [PMID:23442228, PMID:23727230]. This handoff is governed by phosphorylation: a phospho-mimetic substitution (S253E in yeast) lowers Aar2 affinity for Prp8 and shifts the equilibrium toward Brr2-Prp8 and U4/U6 binding, and CK2α1 and SGK2 are candidate kinases that abrogate the AAR2-PRPF8 interaction in human cells [PMID:21764848, PMID:23442228, PMID:35225431]. Human AAR2 is a conserved ortholog that binds the PRPF8 RNase H domain, but its structure reveals a distinct interaction in which AAR2 locks PRPF8 RH in a conformation compatible only with the first transesterification step, indicating a regulatory role beyond simple placeholder activity for SNRNP200 [PMID:26527271, PMID:36322420].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA
- **partners:** PRPF8, SNRNP200, SNU114, CSNK2A1, SGK2
- **complexes:** precursor (16S) U5 snRNP

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1991 | Medium | AAR2 (yeast) is required for splicing of the two introns in MATa1 pre-mRNA; aar2 mutants accumulate unspliced a1 pre-mRNA but not unspliced ACT1 pre-mRNA, establishing a role in pre-mRNA splicing with some substrate specificity. | PMID:1922071 | Molecular and cellular biology |
| 2001 | High | Aar2p is a component of a simple 16S U5 snRNP (containing Prp8p, Snu114p, and Sm proteins) that is co-isolated with U1 snRNP; Aar2p is not present in the [U4/U6.U5] tri-snRNP or spliceosomal complexes, and depletion of Aar2p interferes with later rounds of splicing (snRNP recycling), but it is not required for in vitro splicing. | PMID:11720285 | RNA |
| 2006 | Medium | A mutant allele of AAR2 was identified as a suppressor of splicing defects caused by mutations in Prp38p and Prp8p, placing Aar2p in a spliceosome recycling/turnover pathway; Aar2p is found in a complex with Spp382p recovered with a mutant Prp8p. | PMID:16945917 | Proceedings of the National Academy of Sciences of the United States of America |
| 2011 | High | Aar2p binds to the RNaseH domain of Prp8p, while Brr2p binds to the Jab1/MPN domain; the Aar2p-RNaseH complex sequesters the Jab1/MPN domain, sterically preventing Brr2p binding. Aar2p is phosphorylated in vivo, and a phospho-mimetic S253E mutation disrupts the Aar2p-Prp8p complex in favor of Brr2p-Prp8p complex formation, establishing Aar2p as a phosphorylation-controlled U5 snRNP assembly factor. | PMID:21764848 | Genes & development |
| 2013 | High | Crystal structure of yeast Prp8 (residues 885–2413) in complex with Aar2 revealed that Aar2 contacts Prp8 within its C-terminal region; the structure showed active site cavity formed by reverse transcriptase thumb, endonuclease-like and RNaseH-like domains. | PMID:23354046 | Nature |
| 2013 | High | Crystal structure of yeast Aar2p in complex with Prp8p RNase H and Jab1/MPN domains shows Aar2p binds one side of the RNase H domain and extends its C terminus to dock the Jab1/MPN domain onto a composite Aar2p-RNase H platform, sterically blocking known Brr2p interaction sites. Aar2p also occupies known RNA-binding sites of the RNase H domain and interferes with binding of U4/U6 di-snRNA to Prp8p C-terminal region. Phospho-mimetic mutations reduce Aar2p affinity for Prp8p, allowing Brr2p and U4/U6 binding. | PMID:23442228 | Genes & development |
| 2013 | High | In the cytoplasm, Prp8 forms a precursor U5 snRNP complex with Aar2 (and U5 snRNA, Sm proteins, Snu114); after nuclear import, Brr2 replaces Aar2 to form mature U5 snRNP. Crystal structure and mutagenesis of the Brr2-Prp8 Jab1/MPN complex confirmed that Aar2 and Brr2 are mutually exclusive binders of Prp8. | PMID:23727230 | Structure |
| 2015 | Medium | Human AAR2 (C20ORF4) is expressed in HeLa cells and binds to the RNase H domain of human PRPF8, establishing it as a true ortholog of yeast Aar2p with conserved binding to Prp8. Initial crystal structure of human AAR2-PRPF8 RH complex obtained at 2.35 Å resolution. | PMID:26527271 | Acta crystallographica. Section F, Structural biology communications |
| 2022 | Medium | CK2α1 and SGK2 kinases can abrogate the interaction between spliceosomal proteins AAR2 and PRPF8 in a phospho-yeast two-hybrid assay, identifying candidate kinases that mediate the phosphorylation-dependent regulation of AAR2-PRPF8 complex assembly. | PMID:35225431 | Molecular systems biology |
| 2022 | High | Crystal structure of human AAR2 in complex with the RNase H-like domain of PRPF8 revealed a significantly different interaction compared to yeast. AAR2 variants designed based on the structure failed to stably bind PRPF8 in vitro. AAR2 appears to lock PRPF8 RH in a conformation compatible only with the first transesterification step and blocks a conformational switch to the step-2-like Mg2+-coordinated conformation, suggesting a function beyond SNRNP200 (Brr2) placeholder activity. Phosphorylation-dependent regulation is conserved from yeast to human. | PMID:36322420 | Acta crystallographica. Section D, Structural biology |

## Citations

- PMID:11720285
- PMID:16945917
- PMID:1922071
- PMID:21764848
- PMID:23354046
- PMID:23442228
- PMID:23727230
- PMID:26527271
- PMID:35225431
- PMID:36322420
