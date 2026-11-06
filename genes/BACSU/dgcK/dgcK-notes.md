# dgcK curation notes

## 2026-11-05

Manual literature review completed after `just deep-research-falcon BACSU dgcK` returned HTTP 403 (Edison authentication failure). No provider report was fabricated. Full texts of the cited primary studies were read; the original UniProt/GOA records and all seeded annotation payloads were preserved.

### Evidence and decisions

- [PMID:23893111 Functional characterization of core components of the Bacillus subtilis cyclic-di-GMP signaling pathway.](https://pubmed.ncbi.nlm.nih.gov/23893111/): DgcK is an active diguanylate cyclase in purified-domain and cellular assays. Supporting text: “We conclude that DgcK, DgcP, and DgcW possess diguanylate cyclase activity both in vivo and in vitro”
- [PMID:28536559 New Functions and Subcellular Localization Patterns of c-di-GMP Components (GGDEF Domain Proteins) in B. subtilis.](https://pubmed.ncbi.nlm.nih.gov/28536559/): DgcK participates in the YdaK-dependent unknown-EPS system; direct cell adhesion is not demonstrated. Supporting text: “the presence of dgc genes and particularly the presence of dgcK and furthermore an intact conserved I-site motif (RxxD) of YdaK are indispensable for the production of an unknown EPS” The EPS contribution to biofilm formation remains unresolved. Supporting text: “The function of the unknown EPS in terms of BF formation, however, requires further examinations.”
- [PMID:32156823 Cyclic di-GMP Signaling in Bacillus subtilis Is Governed by Direct Interactions of Diguanylate Cyclases and Cognate Receptors.](https://pubmed.ncbi.nlm.nih.gov/32156823/): DgcK is a six-pass membrane protein that interacts with YdaK. Supporting text: “Purified soluble domains of DgcK, an integral membrane protein with 6 transmembrane helices (TMs), and of YdaK, which harbors 4 TMs” DgcK also interacts directly with DgrA/MotI. Supporting text: “Both, DgcK and DgcP interact with DgrA in vitro”

### Strain identity and evidence coding

The reviews identify the UniProt strain-168 protein. The c-di-GMP studies use NCIB 3610 or its derivatives; they are not represented as tests of strain-168 biofilm behavior. To establish protein identity, the full local UniProt sequence was compared by exact equality against every translated CDS from the experimentally relevant strain reference chromosome CP020102.1 (NCIB 3610 comI-Q12L reference; Nye et al., 2017, DOI:10.1128/genomeA.00364-17). The resulting full-length sequence match supports transfer of molecular activity; it does not establish equivalent whole-cell physiology.

- Reviewed accession: P54595
- Length: 359 amino acids
- Sequence SHA-256: `a9bd910b6bdc414aca5e5632e96b13bd683640c2489ccd30ca2bc5b40b433dcc`
- Exact matched source header: `lcl|CP020102.1_prot_AQZ89810.1_949 [gene=dgcK] [locus_tag=B4U62_05160] [protein=GGDEF domain-containing protein] [protein_id=AQZ89810.1] [location=complement(985772..986851)] [gbkey=CDS]`
- Source URL: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=CP020102.1&db=nuccore&report=fasta_cds_aa&retmode=text
- Retrieval and comparison date: 2026-11-05. Strip whitespace from the local UniProt sequence after `SQ   SEQUENCE` and before `//`; parse each FASTA record from the source URL, concatenate its sequence lines, compare whole strings and compute SHA-256 over UTF-8 sequence text.

Existing machine-supplied evidence codes remain unchanged. Newly proposed receptor/regulator annotations use ISS for the explicit strain transfer, despite complete sequence identity.

### PAINT check

```text
uv run python -m ai_gene_review.validation.gene_paint_losses BACSU dgcK
# PAINT losses on the dgcK (P54595) lineage

No IRD or IKR loss on this gene's lineage.
```

DgcK retains cyclase and motility-regulatory assignments. IPR011620 is a transmembrane sensory-region signature, not evidence that the protein has a histidine kinase catalytic domain. The three kinase/phosphorelay IEAs are removed, and an upstream InterPro mapping defect is recorded on each. Cell-wall organization and a specific cell-adhesion step are overextensions: the DgcK–YdaK system regulates an unknown extracellular polymer and native biofilm relevance remains unresolved.

PAINT IBD tracing additionally confirms GO:0043709 on node PTN002895351 (2018-02-09; descendant seed P31129) above the DgcK leaf PTN002895402. The challenge concerns the specificity of the inferred adhesion process on this branch, not donor count or the correctness of the source protein's own annotation.
