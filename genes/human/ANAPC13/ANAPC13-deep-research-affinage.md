---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANAPC13
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9BS18
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

# Affinage mechanistic annotation for ANAPC13 (human)

## Current model (mechanistic narrative)

ANAPC13 (Swm1/Apc13) is a small, evolutionarily conserved core subunit of the anaphase-promoting complex/cyclosome (APC/C), the E3 ubiquitin ligase that drives cell cycle transitions [PMID:15060174, PMID:12609981]. Within the complex it promotes the stable association of the essential TPR subunits CDC16/Cdc16 and CDC27/Cdc23 with the APC/C, and structural mapping places APC13 in the 'Arc Lamp' sub-complex alongside APC16 and CDC26, in proximity to the homodimerizing TPR subunits APC3, APC6, APC7, and APC8 [PMID:15060174, PMID:25490258]. Loss of the subunit reduces APC/C ubiquitin ligase activity in vitro and delays APC/C-dependent cell cycle events in vivo, with deletion causing G2/M accumulation [PMID:15060174, PMID:12609981]. Biallelic loss-of-function mutations in ANAPC13 cause human and mouse oocyte maturation arrest at metaphase I by disrupting APC/C subunit composition and impairing the ubiquitin ligase activity required for the metaphase I-to-anaphase I transition, without altering spindle assembly checkpoint dynamics; wild-type mRNA partially rescues polar body extrusion [PMID:41997520]. In budding yeast the orthologue is additionally required for late sporulation and cell wall integrity, functions mechanistically tied to its APC/C role [PMID:10022899, PMID:15135545].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-392499 Metabolism of proteins
- **partners:** CDC16, CDC27, CDC23, APC5, APC16, CDC26
- **complexes:** APC/C, APC/C Arc Lamp sub-complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | Swm1/Apc13 (ANAPC13) is an evolutionarily conserved subunit of the APC/C that promotes the stable association of the essential TPR subunits Cdc16 and Cdc27 with the complex; deletion of SWM1 reduces APC/C ubiquitin ligase activity in vitro and delays APC/C-dependent cell cycle events in vivo. Human and fission yeast homologues associate with APC/C subunits and complement the yeast swm1Δ phenotype. | PMID:15060174 | Molecular and cellular biology |
| 2003 | High | Swm1 (ANAPC13) was identified as a constitutive core subunit of the budding yeast APC/C, present throughout G1, S, and M phases and in meiotic cells. Swm1 interacts with Cdc23 (APC8) and Apc5 in an in vitro transcription/translation system. Deletion of SWM1 causes slow growth and G2/M accumulation consistent with an APC defect. | PMID:12609981 | The Journal of biological chemistry |
| 2014 | Medium | Crystal structures of human APC3 alone and in complex with the C-terminal domain of APC16 reveal that APC13 (together with APC16 and CDC26) is a component of the APC/C 'Arc Lamp' sub-complex; structural and biochemical data place APC13 in proximity to the TPR subunits APC3, APC6, APC7, and APC8 that homodimerize and stack within the Arc Lamp. | PMID:25490258 | Journal of molecular biology |
| 2024 | Medium | The cancer-associated SF3B1-K700E mutation induces aberrant splicing of ANAPC13, inserting a 231-bp fragment into the 5′ UTR and reducing ANAPC13 protein expression. Reduced ANAPC13 in Tregs impairs Treg differentiation and inhibitory function; forced re-expression of ANAPC13 restores Treg differentiation and the ability to prevent adoptive-transfer colitis. | PMID:39303038 | Science advances |
| 2025 | High | Biallelic mutations in ANAPC13 (p.D2E and p.L24R) cause oocyte maturation arrest at metaphase I in humans and in a knock-in mouse model (Anapc13M/M). Mechanistically, mutant ANAPC13 disrupts the protein composition of the APC/C, impairs APC/C ubiquitin ligase function during the metaphase I-to-anaphase I transition, and causes abnormal APC/C subunit interactions, without altering spindle assembly checkpoint dynamics. Microinjection of wild-type Anapc13 mRNA partially rescues first polar body extrusion (49%). | PMID:41997520 | American journal of obstetrics and gynecology |
| 2025 | Low | Compound heterozygous missense mutations in APC13 (c.C6A and c.116_126del) found in an infertile female cause aberrant cellular localization of the ANAPC13 protein, as determined by in vitro experiments, and structural modelling predicts disrupted chemical bonds between APC13 and other APC/C subunits. | PMID:40238067 | Journal of assisted reproduction and genetics |
| 1999 | Medium | In Saccharomyces cerevisiae, Swm1p (the yeast orthologue of ANAPC13) is a nuclear protein required for the completion of late sporulation events, including spore wall assembly. Swm1p is not epistatic to the Sps1p-Smk1p MAP kinase sporulation pathway, indicating it acts in a separate signal transduction pathway controlling late sporulation gene expression. | PMID:10022899 | Molecular and cellular biology |
| 2004 | Medium | In S. cerevisiae, Swm1p (ANAPC13 yeast orthologue) is required to maintain cell wall integrity during growth at high temperature; swm1Δ cells show a 7-fold reduction in glucan synthase activity and a 3.5-fold increase in chitin content deposited delocalized across the cell wall, with the excess chitin synthesized primarily by chitin synthase III (Chs3p), as shown by the swm1 chs3 double mutant. | PMID:15135545 | FEMS microbiology letters |

## Citations

- PMID:10022899
- PMID:12609981
- PMID:15060174
- PMID:15135545
- PMID:25490258
- PMID:39303038
- PMID:40238067
- PMID:41997520
