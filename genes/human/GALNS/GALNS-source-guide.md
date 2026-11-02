# GALNS source guide

GALNS removes 6-sulfate groups during lysosomal degradation of chondroitin and keratan glycans. One molecular activity, GO:0043890, covers both natural sugar classes. The current review contains 15 source annotations and one separately identified inherited proposal for keratan sulfate proteoglycan catabolism. See the [review](GALNS-ai-review.yaml) for all judgments and reference assessments, and the [source archive](GALNS-source-evidence.yaml) for literal contexts, history and source locators.

## Catalytic evidence and specificity

PMID:22940367 directly measures purified human GALNS on synthetic 4-MU-sulfate and 4-MU-Gal6S. The latter assay couples desulfation to beta-galactosidase reporter release and includes omission controls. Synthetic aryl-sulfate turnover supports the arylsulfatase IBA as a real, non-core catalytic capability; it does not establish a physiological aryl substrate. The formylglycine/calcium active site and homodimer are structural findings. The GalNAc product pose is nonproductive, so it is not described as a productive sulfated-substrate pose.

PMID:820716 assays crude human kidney extracts on chondroitin-6-sulfate oligosaccharides and corrects a separate small arylsulfatase B contribution. It does not establish GALNS 4-sulfatase activity or intact-polymer cleavage. PMID:15962010 actually assays GALNS cDNA activity and SUMF1 enhancement; the detailed supplementary GALNS substrate protocol remains unread. PMID:8325655 remains abstract-only after bounded original-source checks, leaving its specific 4-sulfatase assertion UNDECIDED.

The selected author-uploaded original of PMID:18285341 confirms human GALNS expression and siRNA experiments in MCF-7 cells. GALNS activity and total chondroitin sulfate change, while C4S and ASB activity do not change with GALNS manipulation. The explicit 4-MU-sulfate recipe is for ASB; detailed GALNS assay chemistry refers to earlier work. These distinctions supersede an overly broad reading of the abstract. The unchanged keratan abundance in this cell assay is not cited as positive evidence for keratan degradation.

## Location and pathway records

PMID:30760748 directly colocalizes GALNS and LAMP1 in primary human airway fibroblasts. Both lysosome rows are accepted alongside the more precise lysosomal-lumen statements. Reactome R-HSA-1630304 describes the normal GALNS keratan-desulfation reaction. R-HSA-2263490 describes failure of defective variants and links that normal reaction; mutant failure is not mistaken for absence of wild-type activity.

The inherited keratan process proposal is retained as TAS with original reference R-HSA-1630304. Its older EXP/PMID:22940367 combination is preserved in the historical record, because the 2012 experiments use synthetic substrates rather than directly measuring natural keratan breakdown. GALNS itself performs the desulfation step. Same-role GLB1/GNS annotations and typed ancestry support the process scope without adding a redundant ancestor.

Official input and output sets for neutrophil event R-HSA-6798751 name OxA-GALNS. They support contextual azurophil-lumen/extracellular occurrence, not GALNS execution of exocytosis. Individual component-page requests returned 404, which is distinguished from the successful named-set membership.

## Urinary fraction and historical reassessment

The authentic [Supplemental Table 2 of PMID:23533145](https://www.ebi.ac.uk/biostudies/files/S-EPMC3773505/NIHMS502285-supplement-Supplemental_Table_2.xlsx), sheet SI Table 2, row 319, identifies P34059/GALNS with 7/7/10/9 unique peptides in duplicate pooled cancer/non-cancer preparations. Its 211,902-byte workbook hash and exact column names are in the source archive. This supports fraction-associated occurrence, without establishing vesicle topology, biogenesis or extracellular catalytic function. The current non-core decision explicitly reassesses the October 10 over-annotation decision; the original row and older non-core journal wording are retained.

## Products and evolutionary evidence

The current official record and direct FASTA specify one canonical 522-residue product, with a signal peptide at 1-26 and mature-chain annotation at 27-522. No alternative products are declared. Processing, purification tags and recombinant constructs do not create natural isoforms.

In the actual PTHR42693 tree, the exact target sequence at PTN002533499 descends from the arylsulfatase IBD node PTN000819263. The original incoming five-donor record and later six-donor PAINT assertion remain distinct; the latter adds P15289. This is dated provenance, not an error inferred from donor count. No negative assertion interrupts the target path.

## Access and conservation

The 15 original contexts, one part_of atom, one canonical sequence and all 29 inherited quotation associations remain recoverable. Two original quotation associations remain active, 27 are historical-only, and two new short assay quotations are introduced. Current excerpts are not repeated in this guide or the new journal section. The old review is linked at its immutable Git revision; all prior journal bytes remain as a prefix. Reference assessments distinguish normal-cache availability from selected external-original reading.

Genuine native acquisition reconciled all 15 original contexts with the actual 16-column export and private native seed. The separate TAS keratan proposal remains identifiable as an authored NEW. All 36 sources and four active quotations were checked against their actual bytes: 18 main sources were reused unchanged and 18 missing sources were acquired. The original part_of atom is restored on native row 11. The inherited review, 29 quotation associations, journal and four prior history records remain preserved. Default and strict GOA validation, history, status and private rendering passed with zero advisories. Computed COMPLETE retains the one UNDECIDED scientific judgment.
