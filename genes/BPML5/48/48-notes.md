# Curation Notes: Mycobacteriophage L5 gene 48 (Flavin-dependent thymidylate synthase ThyX / Gp48, Q05259)

## Summary
- **Gene symbol**: `48`
- **UniProt ID**: `Q05259` (`THYX_BPML5`)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)
- **Protein length**: 243 amino acids (27,784 Da)
- **EC number**: EC 2.1.1.148 (flavin-dependent thymidylate synthase)

## Literature & Bioinformatic Findings
- First identified in the complete genome sequence of mycobacteriophage L5 [PMID:8459766, "We describe here the complete DNA sequence of the L5 genome and initial characterization of L5 virion structure and gene expression."].
- Overexpressed in *Escherichia coli* and biochemically characterized by Bhattacharya et al. (2008) [PMID:18248423, "Two such genes, 48 and 50, encoding thymidylate synthase and ribonucleotide reductase (RNR), respectively, were overexpressed in Escherichia coli and the recombinant proteins were biochemically characterized."].
- Shown to be a functional flavin-dependent thymidylate synthase (ThyX) with properties similar to the *Paramecium bursaria* chlorella virus-1 ThyX enzyme [PMID:18248423, "It was established that Gp50 was a class II RNR having properties similar to that of the corresponding enzyme from Lactobacillus leichmanni, whereas Gp48 was a flavin-dependent thymidylate synthase (ThyX) that resembled the Paramecium bursaria chlorella virus-1 ThyX enzyme in its properties."].
- Expressed early in the lytic cycle when host thymidylate synthase (ThyA) activity declines, compensating for the loss of host enzyme activity, and co-immunoprecipitates with the phage class II ribonucleotide reductase Gp50 [PMID:18248423, "Gp48 and 50 were also found to coimmunoprecipitate, which indicates the possible existence of an L5 thymidylate synthase complex."].
- Catalyzes the reductive methylation of dUMP to dTMP using 5,10-methylenetetrahydrofolate as the methyl donor and NADPH/FADH2 as the reductant (`RHEA:29043`, `EC:2.1.1.148`), binding FAD at subunit interfaces of the homotetramer (`file:genes/BPML5/48/48-uniprot.txt`).

## Review of Existing GOA Annotations
- `GO:0050797` (`thymidylate synthase (FAD) activity`, both IEA and ISS rows), `GO:0050660` (`flavin adenine dinucleotide binding`), and `GO:0006231` (`dTMP biosynthetic process`) are accepted (`ACCEPT`) as core functions.
- `GO:0006235` (`dTTP biosynthetic process`) is kept as non-core (`KEEP_AS_NON_CORE`) because Gp48 catalyzes the committed synthesis of dTMP (`GO:0006231`), which is subsequently phosphorylated to dTTP by nucleotide kinases.
- Broader ancestor terms (`GO:0008168` `methyltransferase activity`, `GO:0009165` `nucleotide biosynthetic process`, `GO:0016740` `transferase activity`) are marked `TOO_GENERAL` because they are directly entailed by `GO:0050797` and `GO:0006231`.
