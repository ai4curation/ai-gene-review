# DYNLT2B/TCTEX1D2: evidence and transfer notes

The human reference Q8WW35 is DYNLT2B, historically TCTEX1D2. It is a non-motor light chain of cytoplasmic dynein-2; DYNLT1 and DYNLT3 are distinct partner light chains. The 2025 mouse paper explicitly identifies Tctex1d2 as Dynlt2b. [PMID:39827215](https://pubmed.ncbi.nlm.nih.gov/39827215/)

## Human mechanism

Biochemical composition studies establish TCTEX1D2 as a dynein-2 light chain. [PMID:25205765](https://pubmed.ncbi.nlm.nih.gov/25205765/)

> we identify TCTEX1D2 as a unique dynein-2 light chain

Human knockout experiments establish retrograde ciliary trafficking defects, complementing patient and Chlamydomonas evidence. The light chain supports the motor; it is not itself an ATPase or a membrane transporter. [PMID:29742051](https://pubmed.ncbi.nlm.nih.gov/29742051/), [PMID:26044572](https://pubmed.ncbi.nlm.nih.gov/26044572/)

The human localization study distinguishes endogenous ciliary-base/MTOC signal from tagged-protein overexpression in the axoneme. This distinction is retained in the annotation review. [PMID:25830415](https://pubmed.ncbi.nlm.nih.gov/25830415/)

## Structural evidence

The 2024 study determined the isolated DYNLT1–DYNLT2B heterodimer structure. [PMID:38454149](https://pubmed.ncbi.nlm.nih.gov/38454149/), [DOI:10.1038/s44318-024-00060-1](https://doi.org/10.1038/s44318-024-00060-1), [PDB:8RGI](https://www.rcsb.org/structure/8RGI)

The RCSB entity record maps the second polymer to Q8WW35 and includes its complete terminal sequence. Human UniProt records a beta-strand at residues 128–140 from this structure. The paired horse alignment lacks human residues 129–142, placing the deletion in an observed structured region rather than a presumed dispensable tail. This is evidence for a consequential model uncertainty, not a folding assay on the horse protein.

## Mouse sperm evidence

The peer-reviewed 2025 mouse study reports sperm flagellar dysplasia and disrupted axonemal structure in Tctex1d2-null males, with preserved motile cilia in the examined tissues. It also reports testis interactions with cytoplasmic dynein-2 and inner-arm dynein proteins. This supports a tissue-dependent axonemal role in mouse and does not establish human infertility or equine localization by itself. [PMID:39827215](https://pubmed.ncbi.nlm.nih.gov/39827215/), [DOI:10.1038/s41598-024-83424-1](https://doi.org/10.1038/s41598-024-83424-1)

The Falcon report lists this work as a 2024 preprint; the source check above uses the published 2025 paper. Its cautious description of human retrograde-IFT evidence is supplemented by the direct 2018 knockout study, rather than adopted as a bare verdict.

## Unresolved source-specific annotations

The NAS male-germ-cell-nucleus annotation cites PMID:36973253. The cached full text examines DYNLRB1/DYNLRB2 and does not establish the DYNLT2B-specific localization in the material inspected. It remains UNDECIDED; no experimental annotation is removed merely because the paper foregrounds another gene. Dynein axonemal particle residence is also distinct from ciliary-base, axoneme or dynein-complex localization and remains unresolved.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files or prediction-evidence folders were consulted.

**Identity.** Q8WW35 is the reviewed canonical human DYNLT2B/TCTEX1D2 entry (142 aa, full Tctex-1 domain PF03645), not an isoform or fragment. PANTHER places it in PTHR21255:SF7 (DYNEIN LIGHT CHAIN TCTEX-TYPE PROTEIN 2B), which also contains mouse Dynlt2b Q9CQ66, bovine Q32P71 and zebrafish F1QMY1 (interpro/panther/PTHR21255/PTHR21255-entries.csv). The family review interpro/panther/PTHR21255/PTHR21255-review.yaml agrees with this subfamily placement.

**Evidence I re-read.**
- PMID:26044572: affinity proteomics puts TCTEX1D2/Tctex2b in IFT dynein, recovering WDR34, WDR60, DYNLT1, DYNLT3 and DYNLRB1 ["We were able to identify interactions of TCTEX1D2 with IFT dynein intermediate chains WDR34 and WDR60, and light chains DYNLT1, DYNLT3 and DYNLRB1 (Supplementary Table 7)."]. Patient fibroblasts and Chlamydomonas Tctex2b mutants show a retrograde IFT defect, and the motor is partially destabilized.
- PMID:25205765: TCTEX1D2 is dynein-2-specific ["Here, we now also identify the TCTEX1D2 light chain (Tctex-2) as a light chain for dynein-2, not present in dynein-1."]. Depleted cells still form cilia, but the cilia are longer ["In all cases, we can detect a statistically significant increase in cilia length following TCTEX1D2 depletion."]. This bears on the cilium assembly and regulation-of-cilium-assembly IMP rows.
- PMID:38454149: crystal structure of the DYNLT1-DYNLT2B heterodimer ["X-ray crystallography structure of DYNLT1-DYNLT2B heterodimer."].
- PMID:39827215 (mouse ortholog, same subfamily SF7): ["TCTEX1D2 is an axoneme component and interacts with subunits of inner dynein arm"], via co-IP with WDR63/WDR78. This is mouse-sperm evidence and is not transferred as a human annotation. It makes a DAP/inner-arm role plausible but does not show it.
- PMID:36973253: I searched the full text and DYNLT2B/TCTEX1D2 does not appear (it is a DYNLRB1/DYNLRB2 spindle paper).

**Changes vs previous review.**
- GO:0005515 rows, under the protein-binding policy: the three DYNLT1 rows are MODIFIED to GO:0045503 dynein light chain binding, and the WDR60 (Q8WVS4) row to GO:0045505 dynein intermediate chain binding. The GTF2F2, ACTN2 and CDKN2D screen hits are REMOVED as uninformative.
- GO:0007018 IBA is MODIFIED to GO:0035721. The node PTN000478852 is family-wide, spanning dynein-1 and dynein-2 Tctex members, so the general term fits the node, but the specific supported process for this gene is retrograde IFT.
- GO:1905799 regulation of intraciliary retrograde transport is MODIFIED to GO:0035721. Its loss impairs the process the protein is part of, so this is participation rather than regulation.
- GO:0001673 male germ cell nucleus (ComplexPortal NAS) is changed from UNDECIDED to MARK_AS_OVER_ANNOTATED, because the cited paper does not study this protein.
- Centrosome, cytoplasm and cilium assembly are now KEEP_AS_NON_CORE. Regulation of cilium assembly stays non-core, with the cilia-length evidence added.
- The quote supports were corrected: several rows had cited a 25205765 abstract sentence under PMID:29742051 or with line-wrap problems.
- A second core function was added (DYNLT1 heterodimerization, GO:0045503), and the description was rewritten.

**Relative to review next.** Mouse Dynlt2b (Q9CQ66), the ortholog in the same PANTHER subfamily SF7, is experimentally characterised (PMID:39827215, sperm flagellum, axoneme, inner-arm IC interactions). The repo has no review for it. The Chlamydomonas ortholog Tctex2b also has experimental data (PMID:26044572), but I did not verify its PANTHER placement.

**Modules.** modules/intraflagellar_transport.yaml covers retrograde IFT by dynein-2. DYNLT2B is not currently listed as a part there.
