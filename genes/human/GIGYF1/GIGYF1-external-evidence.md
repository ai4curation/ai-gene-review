# GIGYF1 evidence and assay boundaries

The association sources and the evidence for informative binding mechanisms are distinguished below. Positive pairs remain recorded even when generic protein binding is omitted. Historical evidence is preserved in the [context archive](GIGYF1-context-archive.json).

## PMID:12771153 — Mouse GYF recognition and signaling

Selected author-original Methods/Results map GIGYF1 GYF residues and GRB10 proline boxes. A mouse fragment spanning residues 410–598 increased stimulated signaling in receptor-rich fibroblasts. Full-length signaling was not tested; the human sequence was not the functional reagent. Receptor bridging is inferred through GRB10. [Original source](https://doi.org/10.1074/jbc.M211572200).

## PMID:20878056 — Human signaling assembly

Human assays map RQCD1 binding to GIGYF1 residues 620–665. RQCD1 depletion weakens GRB10 co-IP and EGF/Akt signaling; these are RQCD1 perturbations, not GIGYF1-loss tests. No RQCD1 proline-rich interface is mapped. [Original source](https://doi.org/10.3892/ijo_00000760).

## PMID:28698298 — 4EHP specificity

Human GIGYF1 K33–M103 and 4EHP A52–F234 were used for the crystal complex. Purified binding and mutagenesis establish the 4EHP interface. Cellular selectivity distinguishes 4EHP/EIF4E2 from EIF4E1; the reporter-rescue and SAXS work chiefly tests GIGYF2. [Original source](https://doi.org/10.1101/gad.299420.117).

## PMID:31439631 — DDX6 interface

Human GIGYF1 motif–DDX6 RecA2 pull-down and pocket mutants establish binding. The solved GIGYF–Me31B structure is from fly proteins. Human TTP reporter complementation uses GIGYF2. Main Results/Methods and textual captions were read; supplementary construct details and figure pixels were not. [Original source](https://doi.org/10.1101/gad.329219.119).

## PMID:33053355 — Translating mRNA decay

Human GIGYF1 rescue distinguishes WT from DDX6/GYF mutants. Broader RNA-IP/polysome assays mainly test GIGYF2. Intronless reporters establish no precursor restriction. The resource table’s GIGYF1 WT accession O60573-1 identifies 4EHP; retain that unresolved mismatch. [Original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC8984682/).

## PMID:39018414 — Translation repression via eIF3

Human-cell lysate recruitment assays and RNase-containing co-IP support GIGYF1-dependent TTP–eIF3 bridging (Figure 4E–I). TTP depletion reduces joint GIGYF1/eIF3 recruitment to RNA; the GYF mutant retains eIF3 association while reducing TTP binding and target-RNA recruitment. Engineered-reagent, stimulus and non-purified assay limits apply. [Original source](https://doi.org/10.1126/sciadv.adl5638).

## Adaptor annotation scope

GO:0030674 is the protein-macromolecule-specific child of GO:0060090. The source-specific adaptor annotation complements translation repression; it does not assign this mechanism to every screening pair. The ZNF598 associations and named ComplexPortal variants remain positive, without a demonstrated contact-specific ligase-recruitment function. The mapped eIF3 and EIF4E2 contacts are distinct. Another GO:0031369 assertion would add evidence for a different partner without adding term-level coverage; the eIF3 contact remains explicit in the adaptor mechanism. No narrower eIF3-binding term was established by the bounded search. ComplexPortal identifiers remain distinct from GO complex terms; no unverified GO identifier is supplied.

## PMID:38225382 — SNRPB proline-repeat recognition

Human BRET tests SNRPB proline repeats and GIGYF1 W498E/L508F. Exact ORFs match O75420/P14678-2; separate co-IP uses mouse Snrpb. Region dependence is distinct from modeling, without retrospectively validating HuRI clone sequences. [Original source](https://doi.org/10.1038/s44320-023-00005-6).

## PMID:32296183 — HuRI source scope

Thirty positive pairs join 96 source rows from human proteins assayed in yeast. Three method projections are not independent physiological tests; map-level orthogonal validation is not assigned to individual pairs. Target ORF100069089 has partial-DNA identification. NEK6 incoming Q9HC98-4 versus source Q9HC98-1 remains unresolved. [Original source](https://doi.org/10.1038/s41586-020-2188-x).

## PMID:33961781 — BioPlex source scope

The 293T AP-MS network records GIGYF1–DDX6 line 104237 and GIGYF1–ZNF598 line 104240. The latter source specifies Q86UK7-2. These are associations, not binary contacts or peptide-level proof of every product. [Original source](https://doi.org/10.1016/j.cell.2021.04.011).

## PMID:36950384 — Neuronal interaction scope

Endogenous GIGYF1 IP-MS in induced human neurons identifies DYNC1H1, SMARCC2 and STAC3. CNCR controls compare other negative IPs, not matched IgG. Two biological replicates and gene-level grouping do not establish direct contact or exact natural product sequence. [Original source](https://pubmed.ncbi.nlm.nih.gov/36950384/).

## PMID:39251607 — DDX6 proximity scope

K562 N-terminal BioID2–DDX6 with 24-hour biotin labeling and untreated controls identifies GIGYF1 in publisher S6/S7 row 255, column 9. This source supplies proximity evidence; the independent direct/functionally tested pair supports the specific binding refinement. [Original source](https://pubmed.ncbi.nlm.nih.gov/39251607/).

## Current interaction inventory

Raw indices refer to the lossless current archive. Partner products remain literal source identifiers; they are not target isoform fields.

| Raw index | Source | Partner / group | Decision |
| --- | --- | --- | --- |
| 0 | PMID:20878056 | UniProtKB:P00533 AND UniProtKB:P31749 AND UniProtKB:Q13322 AND UniProtKB:Q6Y7W6 AND UniProtKB:Q92600 | REMOVE |
| 1 | PMID:20878056 | UniProtKB:Q13322 AND UniProtKB:Q92600 | MODIFY |
| 2 | PMID:20878056 | UniProtKB:Q92600 | REMOVE |
| 3 | PMID:28698298 | UniProtKB:O60573-1 | MODIFY |
| 4 | PMID:32296183 | UniProtKB:P09012 | REMOVE |
| 5 | PMID:32296183 | UniProtKB:P09234 | REMOVE |
| 6 | PMID:32296183 | UniProtKB:P0CG20 | REMOVE |
| 7 | PMID:32296183 | UniProtKB:P14678-2 | MODIFY |
| 8 | PMID:32296183 | UniProtKB:P26196 | MODIFY |
| 9 | PMID:32296183 | UniProtKB:P54646 | REMOVE |
| 10 | PMID:32296183 | UniProtKB:Q08117-2 | REMOVE |
| 11 | PMID:32296183 | UniProtKB:Q12815 | REMOVE |
| 12 | PMID:32296183 | UniProtKB:Q15560 | REMOVE |
| 13 | PMID:32296183 | UniProtKB:Q2TAC2-2 | REMOVE |
| 14 | PMID:32296183 | UniProtKB:Q8NEH6 | REMOVE |
| 15 | PMID:32296183 | UniProtKB:Q8NI38 | REMOVE |
| 16 | PMID:32296183 | UniProtKB:Q92993 | REMOVE |
| 17 | PMID:32296183 | UniProtKB:Q96EZ8 | REMOVE |
| 18 | PMID:32296183 | UniProtKB:Q96GM5 | REMOVE |
| 19 | PMID:32296183 | UniProtKB:Q96MF2 | REMOVE |
| 20 | PMID:32296183 | UniProtKB:Q99932-2 | REMOVE |
| 21 | PMID:32296183 | UniProtKB:Q9BSW2 | REMOVE |
| 22 | PMID:32296183 | UniProtKB:Q9BVG8-5 | REMOVE |
| 23 | PMID:32296183 | UniProtKB:Q9BWG6 | REMOVE |
| 24 | PMID:32296183 | UniProtKB:Q9H0I2 | REMOVE |
| 25 | PMID:32296183 | UniProtKB:Q9H5Z6-2 | REMOVE |
| 26 | PMID:32296183 | UniProtKB:Q9H6L4 | REMOVE |
| 27 | PMID:32296183 | UniProtKB:Q9HC52 | REMOVE |
| 28 | PMID:32296183 | UniProtKB:Q9HC98-4 | REMOVE |
| 29 | PMID:32296183 | UniProtKB:Q9NRE2 | REMOVE |
| 30 | PMID:32296183 | UniProtKB:Q9NW64 | REMOVE |
| 31 | PMID:32296183 | UniProtKB:Q9NX04 | REMOVE |
| 32 | PMID:32296183 | UniProtKB:Q9NXR5-2 | REMOVE |
| 33 | PMID:32296183 | UniProtKB:Q9UPN6 | REMOVE |
| 34 | PMID:33053355 | UniProtKB:Q86UK7 | REMOVE |
| 35 | PMID:33961781 | UniProtKB:P26196 | MODIFY |
| 36 | PMID:33961781 | UniProtKB:Q86UK7 | REMOVE |
| 37 | PMID:36950384 | UniProtKB:Q14204 | REMOVE |
| 38 | PMID:36950384 | UniProtKB:Q8TAQ2 | REMOVE |
| 39 | PMID:36950384 | UniProtKB:Q96MF2 | REMOVE |
| 40 | PMID:38225382 | UniProtKB:P14678-2 | MODIFY |
| 41 | PMID:39251607 | UniProtKB:P26196 | MODIFY |

## Phylogenetic interpretation

The actual PTHR14445 tree places the human 1035-residue sequence at AN60. The two root assertions and the Euteleostomi assertion reach that leaf, with literal experimental donors conserved. The IRD concerns direct nucleic-acid-binding translation repression; it does not invalidate initiation repression, cytosol, or protein-interface binding. GYF conservation alone is not used to invent an RNA-loss mechanism.
