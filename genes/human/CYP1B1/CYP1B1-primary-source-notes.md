# CYP1B1 primary chemistry assays and source-table locators

This authored note identifies the decisive human-enzyme measurements behind the chemistry annotations. Numerical entries below are small target-specific transcriptions; surrounding explanations are paraphrases. They are not quotations inserted into the publication cache. A table value establishes the reported assay outcome, not the reaction's dominance in human tissues.

## Human estradiol regioselectivity — PMID:23821647

Original: [Nishida et al., 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3876821/), [DOI:10.1124/mol.113.087700](https://doi.org/10.1124/mol.113.087700). The Methods describe modified human CYP1B1 coexpressed with human P450 reductase in bacterial membranes. Estradiol reactions use NADPH, followed by separate chromatographic quantification of the two hydroxylation products. In the Results comparison of commercial and laboratory wild-type preparations, the reported C4:C2 product ratios are respectively 5.4 ± 0.3 and 5.0 ± 0.7. The mutation Results report a human Val395-to-Leu switch in preference. These experiments establish human product selectivity; a rodent ratio or engineered mutant is not substituted for the displayed human protein.

[RHEA:47280](https://www.rhea-db.org/rhea/47280) specifies estradiol C4 hydroxylation with reduced P450 reductase. The proposed GO term has no assigned GO identifier. The current steroid-hydroxylase closure and the limits of the term search are recorded in the [evidence index](CYP1B1-evidence-index.yaml).

## Human arachidonate regioisomers — PMID:15258110

Original: [Choudhary et al., 2004, DOI:10.1124/dmd.32.8.840](https://doi.org/10.1124/dmd.32.8.840); [public archived PDF](https://web.archive.org/web/20240413125725/https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=cb0b4dd542c37f4635c11e416a331442b835d848). **Table 3, printed page 846 (PDF page 7), human CYP1B1 column**, rather than the neighboring mouse Cyp1b1 column:

| Product row | Percentage of total products, mean ± SE |
|---|---:|
| 14,15-EET | 6.87 ± 0.72 |
| 11,12-EET | 5.20 ± 1.11 |
| 8,9-EET | 4.91 ± 0.35 |
| 5,6-EET | 6.78 ± 1.25 |

The table distinguishes these three-experiment product percentages from kinetic parameters derived using at least five substrate concentrations in a single experiment. The human reconstitution used an N-terminally modified enzyme, rabbit reductase and NADPH; human Supersomes corroborated the product pattern. The terminal 19/20 and 16/17/18 HETE peaks are grouped, so their individual formation rates are not resolved. These EET data identify positions, not stereochemistry. The paper separately demonstrates retinol-to-retinal and retinal-to-retinoate oxidation.

## Human EET stereochemistry — PMID:20972997

Original: [Mesaros et al., 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC3348553/), [DOI:10.1002/rcm.4760](https://doi.org/10.1002/rcm.4760). **Table 2, hP4501B1 row**, with each value the percentage within the indicated enantiomeric pair:

| 8S,9R | 8R,9S | 11S,12R | 11R,12S | 14R,15S | 14S,15R |
|---:|---:|---:|---:|---:|---:|
| 4 | 96 | 47 | 53 | 92 | 8 |

The Materials identify human recombinant CYP1B1 insect-cell Supersomes. The substrate-incubation Methods use arachidonate plus NADPH, with duplicate incubations and chiral LC/MS analysis. These percentages are not percentages of all arachidonate products and are not identical to enantiomeric excess. The human and rat rows differ at 14,15-EET. Mouse Hepa-cell measurements provide a separate cellular context, not an isolated human CYP1B1 assay.

## Secondary hydroperoxide dehydration — PMID:21068195

Original: [Bui et al., 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3033693/), [DOI:10.1124/dmd.110.035121](https://doi.org/10.1124/dmd.110.035121). **Table 2, CYP1B1 row**, in the listed product-column order:

| 5-oxoETE | 12-oxoETE | 15-oxoETE | 13-oxoODE |
|---:|---:|---:|---:|
| 11.8 ± 0.3 | 6.0 ± 0.3 | 11.2 ± 0.6 | 7.4 ± 0.3 |

Units are product molecules per P450 per minute (min⁻¹); the reported ± values are transcribed without assigning an unverified error statistic. The eicosanoid-metabolism Methods specify 100 nM enzyme, 50 μM substrate, five minutes at 37°C and HPLC product measurement. The target assays omit added NADPH but retain POR in the microsomes. The paper's purified CYP2S1 controls and proposed inflammatory role do not establish those properties for CYP1B1. The measured CYP1B1 activity is retained, with its intact-tissue contribution unresolved.

## Access and interpretation

The repository caches for PMID:15258110 and PMID:21068195 contain abstracts. The recovered originals above supply the table evidence; the cache files remain unchanged. The other two caches contain full-text material. Reference findings use only exact short cache excerpts, while the numerical tables here point directly to their original sources. No new figure-pixel or complete supplementary-material inspection is claimed.
