# ydaK curation notes

## 2026-11-05

Manual literature review completed after `just deep-research-falcon BACSU ydaK` returned HTTP 403 (Edison authentication failure). No provider report was fabricated. Full texts of the cited primary studies were read; the original UniProt/GOA records and all seeded annotation payloads were preserved.

### Evidence and decisions

- [PMID:23893111 Functional characterization of core components of the Bacillus subtilis cyclic-di-GMP signaling pathway.](https://pubmed.ncbi.nlm.nih.gov/23893111/): The inactive GGDEF domain retains direct c-di-GMP binding. Supporting text: “we were able to measure c-di-GMP binding to this domain, likely at the conserved I-site, with a dissociation constant of ∼1.1 μM”
- [PMID:28536559 New Functions and Subcellular Localization Patterns of c-di-GMP Components (GGDEF Domain Proteins) in B. subtilis.](https://pubmed.ncbi.nlm.nih.gov/28536559/): YdaK I-site integrity is required for the DgcK-linked unknown-EPS phenotype. Supporting text: “the presence of dgc genes and particularly the presence of dgcK and furthermore an intact conserved I-site motif (RxxD) of YdaK are indispensable for the production of an unknown EPS” The native biofilm function remains unresolved. Supporting text: “The function of the unknown EPS in terms of BF formation, however, requires further examinations.”
- [PMID:32156823 Cyclic di-GMP Signaling in Bacillus subtilis Is Governed by Direct Interactions of Diguanylate Cyclases and Cognate Receptors.](https://pubmed.ncbi.nlm.nih.gov/32156823/): Ligand binding rearranges the inactive GGDEF domain. Supporting text: “binding of c-di-GMP to YdaK leads to major conformational changes in the entire GGDEF domain” The membrane cyclase and receptor have direct physical interaction. Supporting text: “Purified soluble domains of DgcK, an integral membrane protein with 6 transmembrane helices (TMs), and of YdaK, which harbors 4 TMs”

### Strain identity and evidence coding

The reviews identify the UniProt strain-168 protein. The c-di-GMP studies use NCIB 3610 or its derivatives; they are not represented as tests of strain-168 biofilm behavior. To establish protein identity, the full local UniProt sequence was compared by exact equality against every translated CDS from the experimentally relevant strain reference chromosome CP020102.1 (NCIB 3610 comI-Q12L reference; Nye et al., 2017, DOI:10.1128/genomeA.00364-17). The resulting full-length sequence match supports transfer of molecular activity; it does not establish equivalent whole-cell physiology.

- Reviewed accession: P96585
- Length: 283 amino acids
- Sequence SHA-256: `f4ea091b9c8ef888c98b65cac082c356e74f75d3c201d68e7e9de095c4190af1`
- Exact matched source header: `lcl|CP020102.1_prot_AQZ89334.1_441 [gene=ydaK] [locus_tag=B4U62_02450] [protein=GGDEF domain-containing protein] [protein_id=AQZ89334.1] [location=480053..480904] [gbkey=CDS]`
- Source URL: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=CP020102.1&db=nuccore&report=fasta_cds_aa&retmode=text
- Retrieval and comparison date: 2026-11-05. Strip whitespace from the local UniProt sequence after `SQ   SEQUENCE` and before `//`; parse each FASTA record from the source URL, concatenate its sequence lines, compare whole strings and compute SHA-256 over UTF-8 sequence text.

Existing machine-supplied evidence codes remain unchanged. Newly proposed receptor/regulator annotations use ISS for the explicit strain transfer, despite complete sequence identity.

### PAINT check

```text
uv run python -m ai_gene_review.validation.gene_paint_losses BACSU ydaK
# PAINT losses on the ydaK (P96585) lineage

- PTHR33121: P96585 is not a leaf of this tree; losses not checked.
No IRD or IKR loss on this gene's lineage.
```

The NEW binding assignment is based on direct calorimetry in PMID:23893111 and I-site-dependent conformational responses in PMID:32156823, not on generic GGDEF-domain membership. No cyclase annotation is added. YdaK participates in regulation of the Yda-associated EPS system, but its precise interaction with polymer synthesis/export machinery remains incompletely resolved; no catalytic glycosyltransferase or generic biofilm assignment is manufactured.
