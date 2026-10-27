# Curation Notes: Mycobacteriophage L5 gene 54 (Calcineurin-like metallophosphoesterase Gp54, Q05264)

## Summary
- **Gene symbol**: `54`
- **UniProt ID**: `Q05264` (`VG54_BPML5`)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)
- **Protein length**: 255 amino acids (28,726 Da)

## Literature & Bioinformatic Findings
- Identified in the complete genome sequence of mycobacteriophage L5 [PMID:8459766, "We describe here the complete DNA sequence of the L5 genome and initial characterization of L5 virion structure and gene expression."].
- Located in the right-arm nucleotide metabolism and DNA replication cluster of L5 [PMID:18248423, "The genomes of mycobacteriophages of the L5 family, which includes the lytic phage D29, contain several genes putatively linked to nucleotide-metabolizing functions."].
- Contains a conserved calcineurin-like metallophosphoesterase domain (`InterPro:IPR004843` `Calcineurin-like_PHP`, `InterPro:IPR029052` `Metallo-depent_PP-like`, `Pfam:PF00149` `Metallophos`, `SUPFAM:SSF56300` `Metallo-dependent phosphatases`; `file:genes/BPML5/54/54-uniprot.txt`), preserving the canonical binuclear metal-coordinating motifs (`GD...GD...GNH...H...GH...H`) characteristic of phosphoesterases acting on phosphomonoester or phosphodiester bonds.

## Review of Existing GOA Annotations
- The single GOA annotation `GO:0016787` (`hydrolase activity`, IEA from `InterPro:IPR004843`) is modified (`MODIFY`) to the more specific descendant term `GO:0016788` (`hydrolase activity, acting on ester bonds`), reflecting the conserved calcineurin-like metallophosphoesterase catalytic domain (`IPR004843` / `PF00149`).
