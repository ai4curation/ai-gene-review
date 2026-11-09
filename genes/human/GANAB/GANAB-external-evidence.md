# GANAB target evidence in original proteomic tables

These selected source joins supplement the normal publication caches. They identify the target without making the tables into new experiments or assigning modern isoform specificity.

## Melanosome preparations: PMID:17081065

[Original study](https://doi.org/10.1021/pr060363j), [ACS supporting PDF](https://ndownloader.figshare.com/files/4755490), Supplemental Table 2. The exact extracted target line is:

```text
        Q14697               GANAB             M, O
```

Table 1 defines staged MNT1 and SK-MEL-28 melanosome fractions. Table 2 groups this accession among proteins common to the studied stages. The M/O categories denote membrane and membrane-bound organelle, respectively; the table footnote says these classifications come from GO/UniProt, not independent microscopy. The PDF is 95,397 bytes, SHA256 `ad4e4e804c2f01124591a22cff06b844ed21db2a519bb6df4271e721cac45fac`; the retained text extraction is SHA256 `8490d2a04a3df419b5647fb9535fe62ced809d9fd3b26250016e11480acf4bdd`. This is positive fraction detection, without a demonstrated melanogenesis reaction or GANAB-specific topology.

## Urinary vesicle preparations: PMID:19056867

[Original study](https://doi.org/10.1681/ASN.2008040406), [expanded NIH results](https://hpcwebapps.cit.nih.gov/ESBL/Database/Exosome/). In the retained expanded HTML (SHA256 `e62dbbf0a132cea7b6650ba618f4f257370a56cfbaf42b1949ed02cd28d1cb8c`), zero-based HTML table rows 446 and 447 both name GANAB, with one peptide each and reference 2. Their historical accessions are NP_938148 and NP_938149, labeled isoforms 2 and 3 in that historical table. The current UniProt record maps NP_938148.1 and NP_938149.2 to Q14697-1 and -2, respectively, but no peptide sequence was recovered here; accession correspondence does not prove an isoform-distinguishing peptide. Imported GO columns are not additional experiments.

## Parotid-saliva vesicle preparations: PMID:19199708

[Original study](https://doi.org/10.1021/pr800658c), [original full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2693447/), supporting spreadsheet `pr800658c_si_002.xls`, sheet `Paratid Exosomes`, Excel row 362. The GANAB/IPI00383581.3 entry has 67 sequence identifications, 368 spectra, 57.6% coverage and a 944-residue historical record. The spelling of the sheet is literal. Selected original isolation and MS methods were read: differential centrifugation produced an exosome-enriched pellet, followed by peptide-based protein identification. Historical sequence grouping and possible co-isolated material limit modern product and topology claims.

## Expressed-prostatic-secretions urine vesicles: PMID:23533145

[Original study](https://doi.org/10.1002/pmic.201200561), [original full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3773505/), NIHMS502285 Supplemental Table 2, sheet `SI Table 2`, header row 6 and GANAB row 642. Q14697 has 0/0 unique peptides in the two prostate-cancer pools and 6/5 in the noncancer pools; corresponding LFQ values are 0/0 and 30,693,000/23,198,000. The workbook SHA256 is `6c76b1cd34e709839d8353a5c1584118f0a0c99d8edbfaf361bd1f275f896a70`. Positive detection in the noncancer preparations is not a claim of universal cancer absence or a disease-specific GANAB role.

## HeLa mRNA interactome: PMID:22658674

[Original study](https://doi.org/10.1016/j.cell.2012.04.031), original Table S1 workbook `mmc1.xls`, target Excel row 125. The ENSG00000089597/GANAB row is significant by ion-count quantification (adjusted P=0.00205033), but not by the separate DESeq quantification (adjusted P=0.93042745). The study accepts significant enrichment from either route. A separate whole-cell-lysate sheet lists GANAB at row 671; it is not the source of either P value. The original experiment used UV crosslinking followed by stringent oligo(dT) capture. This supports an RNA-contact observation, without a GANAB RNA target, regulatory mechanism or natural-product assignment. The distinct cCL-versus-PAR comparison is not evidence of a significant difference between crosslinking methods.

The original papers, accession records and selected worksheets are the provenance. No spectra were reanalyzed, no microscopy images were re-scored, and no source cache was edited.
