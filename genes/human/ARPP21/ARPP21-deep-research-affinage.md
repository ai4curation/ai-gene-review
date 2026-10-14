---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARPP21
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9UBL0
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

# Affinage mechanistic annotation for ARPP21 (human)

## Current model (mechanistic narrative)

ARPP21 is a bifunctional protein that operates as a cAMP-regulated phosphoprotein in striatal neurons and as a uridine-rich-RNA-binding post-transcriptional regulator in both neurons and thymocytes [PMID:2538584, PMID:29581509, PMID:38467629]. In neurons it is an excellent and highly selective substrate for cAMP-dependent protein kinase (PKA), which phosphorylates it exclusively at Ser55 within the sequence -Glu-Arg-Arg-Lys-Ser55-Lys-Ser-Gly-Ala-Gly-, while protein phosphatase-2A reverses this modification [PMID:2540203, PMID:10854908]. This phosphorylation is the readout of dopaminergic signaling: D1 receptor activation drives Ser55 phosphorylation whereas D2 activation decreases it, integrating ARPP21 into the dopamine-responsive circuitry of striatonigral neurons where the protein is enriched along the striatonigral pathway [PMID:8436957, PMID:10854908, PMID:1966823]. Its expression in medium spiny neurons depends on BDNF [PMID:10377350]. Independently of its phosphoprotein role, ARPP21 binds uridine-rich 3'UTR sequences and acts as a positive post-transcriptional regulator: in neurons it antagonizes its host intronic miRNA miR-128 by engaging the eIF4F translation initiation complex to promote target mRNA expression and to drive dendritic branching, and in thymocytes the same R3H-domain RNA-binding activity stabilizes Rag1 mRNA to promote TCR gene rearrangement and repertoire diversity [PMID:29581509, PMID:38467629]. In thymocytes ARPP21 is itself eliminated through phosphorylation, polyubiquitination, and proteasomal degradation triggered by TCR/Ca2+ signaling acting through Stim1/Stim2 and CaMK4 [PMID:38467629].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003723 RNA binding, GO:0140110 transcription regulator activity, GO:0045182 translation regulator activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-8953854 Metabolism of RNA, R-HSA-168256 Immune System, R-HSA-112316 Neuronal System
- **partners:** EIF4F
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1989 | High | ARPP-21 is purified to homogeneity from bovine caudate nucleus as two isoforms (ARPP-21A and ARPP-21B). It is an excellent substrate for cAMP-dependent protein kinase (PKA), which incorporates ~1.2 mol phosphate/mol ARPP-21 exclusively on seryl residues. It is not phosphorylated (or only poorly) by cGMP-dependent protein kinase, CaM kinase I, CaM kinase II, casein kinase II, or protein kinase C. Phospho-ARPP-21 is dephosphorylated by protein phosphatase-1 or -2A, but not by PP-2B or PP-2C. The protein has an elongated tertiary structure (frictional ratio 1.7). | PMID:2538584 | The Journal of neuroscience |
| 1989 | High | The PKA phosphorylation site of ARPP-21 is Ser55, within the sequence -Glu-Arg-Arg-Lys-Ser(P)-Lys-Ser-Gly-Ala-Gly-. PKA catalyzes incorporation of 1.1 mol phosphate/mol ARPP-21 exclusively on seryl residues (single tryptic phosphopeptide). Apparent Km for PKA phosphorylation is 0.78 µM and kcat is 2.2 s⁻¹. The same site is phosphorylated in intact rat striatal brain slices treated with 8-bromo-cAMP. | PMID:2540203 | The Journal of biological chemistry |
| 1989 | High | ARPP-21B consists of 88 residues (calculated molecular mass 9,561 Da) with an N-terminal acetyl group; the PKA-phosphorylated seryl residue is at position 55. The protein contains no methionine, tyrosine, phenylalanine, tryptophan, or histidine, and has a single cysteine at position 71. | PMID:2552036 | The Journal of neuroscience |
| 1990 | High | ARPP-21 is enriched in striatonigral neurons: unilateral quinolinic acid lesion of caudate-putamen caused a ~75% decrease in ARPP-21 in the lesioned striatum and ~70% decrease in the ipsilateral substantia nigra, demonstrating axonal/terminal localization in the striatonigral pathway. Phosphorylation of ARPP-21 in striatal, nigral, and cortical slices is enhanced by 8-Br-cAMP (EC50 ~0.5 µM forskolin in striatum). | PMID:1966823 | Neuroscience |
| 1993 | Medium | Dopamine D1 receptor activation by SKF 38393 increases ARPP-21 phosphorylation by ~26% in substantia nigra slices; this effect is blocked by the D1 antagonist SCH 23390, placing ARPP-21 phosphorylation downstream of D1 receptor signaling in striatonigral nerve terminals. | PMID:8436957 | Journal of neurochemistry |
| 1999 | High | BDNF is required for ARPP-21 expression in medium spiny neurons (MSNs): ARPP-21-positive neurons increased from <1% to ~29–51% with BDNF supplementation in vitro; ARPP-21 expression is reduced in BDNF knockout mice in vivo, establishing a neurotrophin-dependent regulatory mechanism for ARPP-21 induction. | PMID:10377350 | The Journal of neuroscience |
| 2000 | High | D1 receptor activation increases ARPP-21 phosphorylation at Ser55 in mouse striatal slices; D2 receptor activation causes a large decrease in phosphorylation. Methamphetamine and cocaine increase ARPP-21 phosphorylation in vivo. Protein phosphatase-2A (not PP-1) is primarily responsible for dephosphorylation of ARPP-21 in striatum, as shown by specific phosphatase inhibitors and DARPP-32 knockout mice. | PMID:10854908 | Neuropharmacology |
| 2001 | Medium | TARPP is a high-molecular-mass (~100 kDa) variant of ARPP-21 expressed specifically in thymocytes. It is a cytosolic protein expressed in immature thymocytes and downregulated upon TCR engagement during positive selection, correlating with TCR gene rearrangement. | PMID:11298339 | European journal of immunology |
| 2018 | High | ARPP21 is an RNA-binding protein that recognizes uridine-rich sequences with high specificity for 3'UTRs (characterized by iCLIP). ARPP21 antagonizes its hosted intronic miRNA miR-128 by co-regulating a subset of miR-128 target mRNAs enriched for neurodevelopmental functions. ARPP21 acts as a positive post-transcriptional regulator by interacting with the translation initiation complex eIF4F. During dendritogenesis: miR-128 overexpression or ARPP21 knockdown reduces dendritic complexity; ectopic ARPP21 increases dendritic complexity. | PMID:29581509 | Nature communications |
| 2024 | High | Arpp21 directly binds RNA through its R3H domain with preference for uridine-rich motifs. In thymocytes, Arpp21 binds the Rag1 3'-UTR and promotes Rag1 mRNA expression. Arpp21-deficient thymocytes show reduced Rag1 expression, delayed TCR rearrangement, and a less diverse TCR repertoire. Arpp21 downregulation requires Stim1/Stim2 and CaMK4 expression and involves protein phosphorylation, polyubiquitination, and proteasomal degradation following TCR and Ca2+ signals. This was confirmed in Rag1 3'-UTR mutant mice with deletion of the Arpp21 response region. | PMID:38467629 | Nature communications |

## Citations

- PMID:10377350
- PMID:10854908
- PMID:11298339
- PMID:1966823
- PMID:2538584
- PMID:2540203
- PMID:2552036
- PMID:29581509
- PMID:38467629
- PMID:8436957
