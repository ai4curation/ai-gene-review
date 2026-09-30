# Cell 2026 NaUGT1 identity check

The Cell NaUGT1 assays strongly identify the **same g26396 locus** represented by UniProt **A0A2H4GSI3**, but the published cloning primers specify an **N-terminally extended construct**, not the exact 485-aa annotated protein. Retaining the deposited splice junctions yields a primer-compatible, stop-free 530-aa ORF containing all 485 target residues unchanged after a 45-aa extension. The complete expressed construct was not deposited as a separately identifiable sequence in the materials retrieved here; the 530-aa sequence is explicitly a primer/genome reconstruction, not a reported sequence.

## Primary identity evidence

- [Cell article, DOI 10.1016/j.cell.2026.03.034](https://doi.org/10.1016/j.cell.2026.03.034), PMID:41928514, Chang et al., *Complete biosynthesis of nicotine*. Both [in-press author PDF](https://pure.mpg.de/rest/items/item_3702304_2/component/file_3702377/content) and [final author PDF](https://pure.mpg.de/rest/items/item_3702304_3/component/file_3710298/content) were inspected. The Methods describe cloning full-length ORFs from the N. attenuata genome v2.0, followed by sequence verification. No explicit UniProt/GenBank accession is supplied for NaUGT1 in those sections.
- [Final supplemental Table S1](https://pure.mpg.de/rest/items/item_3702304_3/component/file_3710299/content), Sheet1, rows 13–14, 31–36, 55–56, 75–78, 87–88, 95–96, 111–114, 125–128, 137–138, labels 28 oligonucleotides **NaUGT1**. The in-press supplement supplies the same relevant primer sequences. This is actual construct/assay sequence evidence, not a match inferred from the gene name.
- [GenBank MJEQ01001183.1](https://www.ncbi.nlm.nih.gov/nuccore/MJEQ01001183.1) explicitly links **UGT85A2_0**, **A4A49_26396**, and protein **OIT31852.1**. Its CDS is `complement(join(276924..277867,278740..279253))`. Translation is exactly the 485-aa A0A2H4GSI3 sequence.
- [GenBank KX752161.1](https://www.ncbi.nlm.nih.gov/nuccore/KX752161.1) explicitly links **NaUGT_g26396** to **AQQ16684.1**, also exactly the 485-aa target. This record is a separate deposited genomic sequence with CDS `join(81..594,1467..2410)`.
- [The genome-release peptide FASTA](https://solgenomics.net/ftp/genomes/Nicotiana_attenuata/NIATTr2.an5.aa.fa) contains **NIATv7_g26396.t1**, labelled UDP-glycosyltransferase 85A2. After removing the terminal stop character, its 485 aa are identical to A0A2H4GSI3. The extracted record is `identity-cell-NIATv7_g26396.fasta`.

## Primer evidence and construct boundary

The script finds exact genomic matches for the 3′ gene-specific portions of **26 of 28** NaUGT1 primers. The two CRISPR oligos contain internal guide sequences followed by scaffold/adaptor sequence, so the 3′-suffix algorithm is deliberately not an alignment test for those guides. Their nonmatches are not evidence against identity.

Examples from Table S1:

| Rows | Purpose | Gene-specific sequence | Exact match |
|---|---|---|---|
| 87 | qPCR | `TTGGGTTGGACATGAAAGAT` | KX752161 CDS nt 1244–1263; scaffold minus strand |
| 88 | qPCR | `TAAGACGATCCACCTTCTTT` | Reverse complement of KX752161 CDS nt 1375–1394 |
| 95 | VIGS | `GCTGAACTTCTTTGTTTTTCTGGC` | Exact g26396 coding-region match |
| 96 | VIGS | `AGAACTAAGCCAACCAGAAGTCA` | Exact reverse-complement g26396 coding-region match |
| 77 | Sequencing | `ACGGGATACTTTGTGCACCG` | Exact intronic match, KX752161 nt 1312–1331 |
| 111/113/125/127/137 | Full-length cloning | `ATGATGCTAATTTCTACCAACTTGACA` | MJEQ01001183.1 nt 279362–279388, minus strand |
| 114/128/138 | Reverse cloning | `TCAATGATGACGAACTTTATCACTTAAG` | Target C-terminal coding region; overlapping reverse primers encode terminal `SLSDKVRHH*` |

The forward primer starts at genomic coordinate **279388**, whereas the deposited OIT31852.1 start is **279253**, on the same minus strand. The difference is **135 nt**, or **45 codons**. Extending the first coding exon to that start, preserving the annotated intron and remaining exon, yields:

```text
MMLISTNLTNISFPLITLNSQKKTINLRSKYSTNQTTILPFFNQK
+ the complete 485-aa A0A2H4GSI3 sequence, beginning MNQESLPPHV...
```

All 485 target residues match without substitution or deletion, at zero-based offset 45 of the inferred ORF. Thus the N-terminal mismatch is explained locally at the **same genomic locus**; it is not evidence for a different paralog. This does not establish whether the extended N terminus is the native major isoform, an annotation correction, or a construct-specific choice.

## Additional supplemental gene identifiers

The actual publisher Data S2 and S3 workbooks were retrieved, rather than treating a query hit as evidence:

- [Data S2](https://ars.els-cdn.com/content/image/1-s2.0-S0092867426003351-mmc3.xlsx), `microarray data`, row 14185: probe `CUST_32495_PI429436614`, gene **NIATv7_g26396**, SplineCluster 75; row 18921: probe `CUST_32496_PI429436614`, gene **NIATv7_g26396**, SplineCluster 121. The paper uses clusters 121/124 to construct the candidate network. These are gene-inventory/expression records, not by themselves an explicit NaUGT1-name crosswalk.
- [Data S3](https://ars.els-cdn.com/content/image/1-s2.0-S0092867426003351-mmc4.xlsx), `scRNA-seq ZMAD_transformed`, row 12152: **NIATv7_g26396**. Relevant rows and headers are preserved in `identity-cell-data2-rows.json` and `identity-cell-data3-rows.json`. These do not supply a full cloned sequence.

## What the actual Cell experiments establish

Figure 3D assays purified recombinant NaUGT1 expressed in E. coli and detects nicotinic acid N-glucoside from nicotinic acid. Figures 3E/F and S3G/H independently test VIGS and CRISPR disruption of the NaUGT1 locus; induced nicotine accumulation is abolished in ugt1 mutant lines. Heterologous pathway reconstruction and omission tests support the reaction's pathway role. These are direct biochemical and genetic data, not solely necessity evidence or coexpression. The sequence gate above makes them strong evidence for the g26396 gene product while preserving the 45-aa construct-boundary caveat.

The exact assay conditions for NaUGT1 are delegated in the Methods to a prior enzyme-expression/assay protocol; the paper supplies detailed reaction mixtures separately for A622, NAMNH and BGL enzymes. Do not fabricate a NaUGT1-specific kinetic constant or reaction condition from those neighboring methods.

## Reproduction and checks

Run `just -f identity-cell.justfile reproduce` and `just -f identity-cell.justfile control` from this directory. The script pins Biopython 1.85 and openpyxl 3.1.5; the first run here used the repository environment with those exact installed versions. Inputs are preserved under `identity-cell-inputs/`; output JSON records their SHA256 checksums and all primer coordinates.

- [x] Sequence identities, genomic boundaries and translations are computed from external inputs; no results are encoded in the script.
- [x] All gene/record/primer labels are command-line inputs.
- [x] The same script was tested with the independent **NaA622** primer set as a negative control against this g26396 locus.
- [x] Direct JSON results and source inputs are retained.
- [x] The 530-aa protein is explicitly marked as reconstruction under a fixed-splice-junction assumption.
- [ ] A complete deposited sequence of the specific assayed NaUGT1 expression construct was not located. Exact construct identity beyond the mapped primer boundaries is therefore inferred, not directly verified.

No gene review YAML was changed by this identity analysis. This evidence should replace name/family-based categorical rejection with an assessment that accounts for direct assays on the same locus and the explicit construct boundary.
