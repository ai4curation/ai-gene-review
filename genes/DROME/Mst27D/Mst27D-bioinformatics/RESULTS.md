# Mst27D domain architecture and PANTHER placement (2026-10-20)

Script: `domain_architecture.py` (raw output in `domain_architecture_output.txt`).
Queries PANTHER v19 geneinfo, UniProt FASTA and the InterPro API for Mst27D (Q8IPI4),
Drosophila Eb1 (A1Z6P3), Drosophila EB-SUN/CG18190 (A1ZBF1) and human MAPRE1 (Q15691).

## Findings

- PANTHER v19 assigns Mst27D, Eb1 and CG18190 to the same subfamily, PTHR10623:SF6 (EB1, ISOFORM F-RELATED). Human MAPRE1 is in a different subfamily, PTHR10623:SF20. SF6 is a fly-lineage EB subfamily, so Drosophila Eb1 is the nearest experimentally characterised relative of Mst27D. Eb1 is a paralog, not an ortholog.
- Mst27D (424 aa) matches only the N-terminal calponin-homology (CH) domain (IPR001715, residues 26-129) and the family-level RP/EB signature (IPR027328, residues 19-365).
- Mst27D has no EB1 C-terminal domain (IPR004953/PF03271). Eb1, CG18190 and MAPRE1 all have it.
- Mst27D does not end in the EB-family acidic EEY/F tail. Its C terminus is QTKVRKSLKV. The Eb1, CG18190 and MAPRE1 tails are DDAPPEDEEY, EHADPNDGLY and GGPQEEQEEY.

## Interpretation

In canonical EBs, the EBH domain and the EEY/F motif recruit +TIP partners to growing plus ends. Mst27D has lost both. Its C-terminal region (residues 151-424, PMID:37428798) is divergent; it binds Nup358 and mediates homodimerisation. This fits the experimental finding that Mst27D binds along the whole microtubule lattice rather than tracking plus ends. It argues against inheriting the plus-end-specific EB functions.
