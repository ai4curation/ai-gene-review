# CG42763 / M9MRG9

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This review did not use ProtNLM2 output. CG42763 was reviewed because it is the only
detectable D. melanogaster paralog of the ProtNLM2 benchmark gene CG31606 (Q8IPG8). The
evidence used is the UniProt record and a new reproducible homology analysis
([RESULTS.md](CG42763-bioinformatics/RESULTS.md), script `homology_check.py`, raw output
`homology_check.json`).

- **Deep research:** `just deep-research-falcon DROME CG42763 --fallback perplexity-lite` failed.
  Falcon raised "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
  (insufficient quota). No deep-research file exists for this gene.
- **Literature:** PubMed (esearch "CG42763": 0 records) and Europe PMC (full-text queries
  "CG42763" and "FBgn0261831": 0 hits) found no publication that mentions the gene. The only
  references are the genome-sequencing and annotation papers listed in UniProt. The GOA file has
  only the three FlyBase ND root annotations (GO_REF:0000015, 2014-05-30).
- **Identity:** M9MRG9 (191 aa) is the only UniProtKB entry for FBgn0261831. The cDNA fragment
  F3YD93 (MIP30261p) is 100% identical over residues 2-191, so the gene is transcribed.
- **Family:** InterPro has no matches (integrated or member database) and UniProt lists no
  PANTHER family, so there is no PAINT/IBA node. The only feature is the SignalP signal peptide
  (1-22). There is no transmembrane segment and no C-terminal KDEL/HDEL.
- **Phylogeny:** OMA has no HOG for M9MRG9. blastp found no Swiss-Prot hit. All UniProtKB
  Eukaryota hits are from *Drosophila*; the full-length orthologs are in D. mauritiana, D. yakuba,
  D. erecta and D. suzukii (melanogaster group). The only paralog signal is CG31606 (E = 4.2e-4,
  33.7% identity over residues 7-95). The D. yakuba ortholog's "TsetseEP domain-containing" name
  is a ProtNLM machine-generated name with no supporting domain signature, so it says nothing
  about function.
- **Experimental status:** No function of CG42763 is experimentally established in D.
  melanogaster or any other species. Nothing can be transferred from it to CG31606, and nothing
  can be transferred to it, because no relative in the lineage is characterised.
- **Annotations:** MF ND is ACCEPTED and BP ND is ACCEPTED. CC ND is MODIFIED to GO:0005576
  extracellular region, based on the signal peptide and soluble mature chain. This is a sequence
  inference, not an observed localisation. core_functions is left empty on purpose. A BIOLOGY
  knowledge gap (WHOLLY_DARK) was added.
- **Modules / GO-CAMs:** none apply (no PANTHER family; gene absent from gocams/index.tsv).
