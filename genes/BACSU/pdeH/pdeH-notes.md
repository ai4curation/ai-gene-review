# pdeH curation notes

## 2026-11-05

Manual literature review completed after `just deep-research-falcon BACSU pdeH` returned HTTP 403 (Edison authentication failure). No provider report was fabricated. Full texts of the cited primary studies were read; the original UniProt/GOA records and all seeded annotation payloads were preserved.

### Evidence and decisions

- [PMID:23893111 Functional characterization of core components of the Bacillus subtilis cyclic-di-GMP signaling pathway.](https://pubmed.ncbi.nlm.nih.gov/23893111/): PdeH directly hydrolyzes c-di-GMP to pGpG. Supporting text: “c-di-GMP was hydrolyzed to pGpG when incubated with PdeH”
- [PMID:32156823 Cyclic di-GMP Signaling in Bacillus subtilis Is Governed by Direct Interactions of Diguanylate Cyclases and Cognate Receptors.](https://pubmed.ncbi.nlm.nih.gov/32156823/): PdeH-mediated degradation can regulate the global pool while DGC–receptor inputs are local. Supporting text: “downregulation occurs via the sole known PDE, PdeH, and thus this aspect of motility may occur via a global pool of c-di-GMP.”

### Strain identity and evidence coding

The reviews identify the UniProt strain-168 protein. The c-di-GMP studies use NCIB 3610 or its derivatives; they are not represented as tests of strain-168 biofilm behavior. To establish protein identity, the full local UniProt sequence was compared by exact equality against every translated CDS from the experimentally relevant strain reference chromosome CP020102.1 (NCIB 3610 comI-Q12L reference; Nye et al., 2017, DOI:10.1128/genomeA.00364-17). The resulting full-length sequence match supports transfer of molecular activity; it does not establish equivalent whole-cell physiology.

- Reviewed accession: P14203
- Length: 409 amino acids
- Sequence SHA-256: `54807337ef10cd79b57a70fe42997029554972aece6cb31d4f68642b099ff1f9`
- Exact matched source header: `lcl|CP020102.1_prot_AQZ92060.1_3316 [gene=pdeH] [locus_tag=B4U62_17165] [protein=hypothetical protein] [protein_id=AQZ92060.1] [location=complement(3258052..3259281)] [gbkey=CDS]`
- Source URL: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=CP020102.1&db=nuccore&report=fasta_cds_aa&retmode=text
- Retrieval and comparison date: 2026-11-05. Strip whitespace from the local UniProt sequence after `SQ   SEQUENCE` and before `//`; parse each FASTA record from the source URL, concatenate its sequence lines, compare whole strings and compute SHA-256 over UTF-8 sequence text.

Existing machine-supplied evidence codes remain unchanged. Newly proposed receptor/regulator annotations use ISS for the explicit strain transfer, despite complete sequence identity.

### PAINT check

```text
uv run python -m ai_gene_review.validation.gene_paint_losses BACSU pdeH
# PAINT losses on the pdeH (P14203) lineage

No IRD or IKR loss on this gene's lineage.
```
