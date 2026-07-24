---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCF
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q9NPI8
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCF (human)

## Current model (mechanistic narrative)

FANCF is a nuclear adaptor protein essential for assembly of the Fanconi anemia (FA) core complex, which drives monoubiquitination of FANCD2 to enable repair of DNA interstrand cross-links [PMID:11063725, PMID:21915857]. It functions as a flexible bridging subunit: its C-terminus binds FANCG to nucleate assembly of other FA proteins, while its N-terminus stabilizes FANCA/FANCG contacts and is required to recruit the FANCC/FANCE subcomplex [PMID:15262960]. The C-terminal domain adopts a Cand1-like helical repeat fold whose two surface loops are critical both for interaction with other core complex components and for FANCD2 monoubiquitination and cellular resistance to mitomycin C [PMID:17082180]. Loss of FANCF abolishes FANCD2 monoubiquitination and produces G2 arrest, chromosomal aberrations, sensitivity to cross-linking agents, and, in mice, defective gametogenesis and ovarian tumors, establishing its non-redundant role in the FA/BRCA pathway in vivo [PMID:21915857]. The FANCC-FANCE-FANCF subcomplex is evolutionarily conserved to plants, where it additionally acts as an anti-crossover factor during meiotic recombination [PMID:36652992]. FANCF expression is transcriptionally activated by ICSBP/IRF8 during myeloid differentiation [PMID:19801548] and is suppressed by p53-driven miR-30c, such that p53 loss in cancer cells upregulates FANCF and confers chemoresistance [PMID:31511498]; silencing FANCF inactivates the FA/BRCA pathway and sensitizes breast and ovarian cancer cells to chemotherapeutic agents through p38/JNK MAPK signaling [PMID:22952942, PMID:23440494].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1474165 Reproduction
- **partners:** FANCA, FANCC, FANCG, FANCE
- **complexes:** Fanconi anemia core complex, FANCC-FANCE-FANCF subcomplex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | FANCF forms a nuclear complex with FANCA, FANCC, and FANCG in human lymphoblasts. Each FA protein (except FANCD) is required for complex formation, as interactions were detected in wild-type and FA-D cells but not in lymphoblasts of other FA complementation groups. | PMID:11063725 | Human molecular genetics |
| 2004 | High | FANCF acts as a flexible adaptor protein in the FA core complex: its C-terminus interacts directly with FANCG to allow assembly of other FA proteins, while the N-terminus stabilizes interactions with FANCA and FANCG and is essential for binding of the FANCC/FANCE subcomplex. FANCF does not have a ROM-like function as previously suggested. | PMID:15262960 | The Journal of biological chemistry |
| 2006 | High | X-ray crystallography of the FANCF C-terminal domain reveals a helical repeat structure similar to Cand1, a regulator of a Cul1-Rbx1-Skp1-Fbox ubiquitin ligase complex. Two C-terminal loops are essential for FANCD2 monoubiquitination and cellular resistance to mitomycin C; mutations in this surface abolish interaction with other FA core complex components. | PMID:17082180 | The Journal of biological chemistry |
| 2009 | Medium | ICSBP/IRF8 directly activates transcription of FANCF during myeloid differentiation by binding a cis element in the FANCF promoter. ICSBP-deficient myeloid cells show impaired DNA cross-link repair in a FANCF-dependent manner. | PMID:19801548 | The Journal of biological chemistry |
| 2012 | Medium | FANCF silencing by shRNA blocks FANCD2 monoubiquitination (inactivating the FA/BRCA pathway), inhibits cell proliferation, induces apoptosis and chromosome fragmentation, and sensitizes breast cancer cells to mitoxantrone. Sensitization involves activation of p38 and JNK MAPK pathways; BCRP expression is restored by p38 inhibitor SB203580. | PMID:22952942 | PloS one |
| 2013 | Medium | FANCF silencing by siRNA inactivates the FA/BRCA pathway (decreasing FANCD2 monoubiquitination and focus formation), reduces cell proliferation, induces apoptosis, and sensitizes OVCAR3 ovarian cancer cells to adriamycin through JNK-dependent mitochondrial apoptosis pathway activation. | PMID:23440494 | Oncology reports |
| 2023 | Medium | The FANCC-FANCE-FANCF subcomplex is evolutionarily conserved from vertebrates to plants (Arabidopsis). Physical interaction among FANCC, FANCE, and FANCF is conserved, and this subcomplex acts as an anti-crossover factor during meiotic recombination; loss of any of the three genes partially rescues CO-defective mutants and causes synthetic meiotic catastrophe with the pro-CO factor MUS81. | PMID:36652992 | Nucleic acids research |
| 2019 | Medium | Wild-type p53 activates transcription of miR-30c by binding its promoter; miR-30c in turn targets FANCF (and REV1), thereby suppressing FANCF expression. In p53-mutant breast cancer cells, loss of this regulation leads to FANCF upregulation and increased adriamycin resistance. | PMID:31511498 | Cell death & disease |
| 2011 | High | Fancf-deficient mouse embryonic fibroblasts are unable to monoubiquitinate FANCD2, show G2 arrest, chromosomal aberrations, and reduced survival in response to DNA cross-linking agents, confirming FANCF is required for FANCD2 activation in vivo. Fancf knockout mice show compromised follicle development and spermatogenesis, and increased incidence of ovarian tumors. | PMID:21915857 | The Journal of pathology |

## Citations

- PMID:11063725
- PMID:15262960
- PMID:17082180
- PMID:19801548
- PMID:21915857
- PMID:22952942
- PMID:23440494
- PMID:31511498
- PMID:36652992
