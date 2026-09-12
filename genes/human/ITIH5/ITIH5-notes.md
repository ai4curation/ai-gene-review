# ITIH5 review notes

## Research provenance

The automated deep-research attempt was made with Falcon and the configured Perplexity-lite fallback. Falcon returned HTTP 402 and the fallback returned HTTP 401, so this review uses the reviewed UniProt record, cached primary publications, and a manual inspection of the open-access article for PMID:27143355. Detailed evidence is recorded in ITIH5-deep-research-manual.md.

## Identity, architecture, and isoforms

ITIH5 (UniProt Q86UX2) is a 942-residue inter-alpha-trypsin inhibitor heavy-chain family protein with an N-terminal signal peptide, VIT domain, and von Willebrand factor type A domain. The founding study noted that ITIH5 diverged early from the other heavy-chain subfamilies [PMID:14744536 "However, ITIH5 diverged early from a common ancestor of the other subfamilies."]. Canonical isoform 1 is predicted to enter the secretory pathway. Isoforms 3 and 4 lack the canonical N terminus and signal peptide; none of the functional studies reviewed here resolves the tested isoform.

## HC5, bikunin, and the hyaluronan matrix

In human lung fibroblasts, HC5 forms chondroitinase-sensitive high-molecular-weight complexes with bikunin. TSG-6 and bikunin are required for cell-surface HC5, and hyaluronidase releases HC5, directly tying it to cell-surface hyaluronan [PMID:27143355 "HC5 was released by hyaluronidase treatment, confirming its association with cell surface HA"]. More than 95% HC5 knockdown reduced TGF-beta1-induced alpha-smooth-muscle actin by more than half, supporting a positive role in fibroblast-to-myofibroblast differentiation. This establishes a human HC5-bikunin-TSG-6-hyaluronan matrix pathway.

## Protease-inhibitor boundary

The family name does not make the heavy chain a serine protease inhibitor. Biochemical work on inter-alpha-inhibitor explicitly describes the heavy subunits as noninhibitory [PMID:2476436 "Inter-alpha-trypsin inhibitor contains noninhibitory heavy chains of 65,000 and 70,000 Da"]. The Kunitz-containing bikunin light chain carries protease-inhibitory activity. ITIH5 lacks a Kunitz domain, so the InterPro-derived inhibitor annotation is removed as component-level overpropagation.

## Adipose and endothelial effects

Mouse Itih5 deletion increased adipose mass and caused adipose stem cells to proliferate and differentiate more strongly toward adipocytes; recombinant ITIH5 reversed the cellular phenotype [PMID:39198923 "ITIH5-/- cells exhibited increased proliferation and adipogenic differentiation"]. This supports a conserved negative effect on fat-cell differentiation, transferred to human ITIH5 with ISS rather than direct human experimental evidence.

A 2026 study found a direct effect of recombinant ITIH5 on human aortic endothelial monolayers: ITIH5 reduced leukocyte recruitment [PMID:42025695 "ITIH5 treatment in human endothelial cells reduced leukocyte recruitment"]. The same study connects adipocyte-derived ITIH5 to endothelial and immune behavior, suggesting an extracellular signaling role that is at least partly separable from stable heavy-chain linkage to bikunin.

## Tumor-associated evidence

ITIH5 is frequently reduced by promoter methylation in breast cancer. Forced expression in MDA-MB-231 cells reduced proliferation [PMID:17653090 "ITIH5-expressing clones showed a 40% reduced proliferation rate"]. This supports a context-dependent negative regulation of cell population proliferation annotation, but tumor suppression is kept outside the conserved core-function summary.

## Existing annotation decisions

| GO annotation | Decision | Rationale |
|---|---|---|
| serine-type endopeptidase inhibitor activity | REMOVE | Inhibitory activity belongs to bikunin; ITIH heavy chains are noninhibitory. |
| extracellular region | ACCEPT | Signal peptide plus direct extracellular/cell-surface matrix evidence. |
| hyaluronan metabolic process | ACCEPT | HC5 participates in TSG-6-dependent heavy-chain organization on hyaluronan. |
| extracellular matrix, PMID:25037231 | ACCEPT | Direct human matrisome proteomics. |
| extracellular matrix, PMID:28675934 | ACCEPT | Direct human tissue ECM proteomics. |

## Proposed annotations

- Hyaluronic acid binding (GO:0005540), IDA from the hyaluronidase-release experiment in human fibroblasts.
- Cell surface (GO:0009986), IDA from cell-surface HC5 detection in human fibroblasts.
- Positive regulation of myofibroblast differentiation (GO:1904762), IMP from human HC5 knockdown.
- Negative regulation of cell population proliferation (GO:0008285), IMP from forced expression in human breast-cancer cells; non-core context.
- Negative regulation of fat cell differentiation (GO:0045599), ISS from mouse knockout and recombinant rescue.
- Negative regulation of leukocyte adhesion to vascular endothelial cell (GO:1904995), IDA from recombinant ITIH5 treatment of human endothelial monolayers.

## Open questions

- Which isoforms are secreted in fibroblasts and adipose tissue, given that isoforms 3 and 4 lack the canonical signal peptide?
- Is the adipocyte-endothelial activity mediated by a receptor, a matrix interaction, or both?
- Does human ITIH5 undergo the same covalent bikunin and hyaluronan transfer chemistry in vivo, and which residue is used?
- Are the anti-proliferative tumor-cell effects a direct physiological function or a consequence of ectopic expression?

