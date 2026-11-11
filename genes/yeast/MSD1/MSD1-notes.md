# MSD1 (YPL104W, P15179) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: MSD1 reviewed de novo as the closest experimentally characterised relative of
human DARS2 (Q6PI48). ProtNLM2 outputs were not consulted.

### Deep research
- `just deep-research-falcon yeast MSD1 --fallback perplexity-lite` FAILED: falcon
  "Failed to authenticate"; perplexity-lite returned HTTP 401 insufficient_quota.
  No deep-research file exists. Review is based on cached literature (5 GOA PMIDs plus
  PMID:35820270, found by PubMed esearch for MSD1/YPL104W + tRNA/synthetase) and the
  UniProt record.

### Evolutionary grounding
- UniProt: MSD1 is PANTHER PTHR22594:SF5 (ASPARTATE--TRNA LIGASE, MITOCHONDRIAL), same
  subfamily as human DARS2; HAMAP MF_00044 (Asp_tRNA_synth_type1), NCBIfam TIGR00459 aspS_bact
  -> bacterial-type AspRS lineage with GAD insertion domain.
- Cytoplasmic yeast AspRS DPS1 (P04802, SGD:S000003941) is in a different PANTHER family
  (PTHR43450:SF1; UniProt REST query). The ISA row from DPS1 is therefore a paralog-level
  similarity call; accepted only because the activity is shown directly in the same paper.
- IBA rows: GO:0004815 and GO:0006422 at PTN000502597 (donors MSD1, E. coli AspS P21889,
  DARS2); mitochondrion at PTN000502598 (donors MSD1, DARS2). MSD1 as its own donor is
  expected, not circular.

### Experimental evidence in yeast (what is actually established)
- [PMID:2668951 "Mitochondria from a mutant with a disrupted chromosomal copy of MSD1 are
  unable to acylate mitochondrial aspartyl-tRNA."] - loss-of-activity in mitochondrial
  extracts; abstract-only cache. Also: "In situ disruption of MSD1 ... induces a pleiotropic
  phenotype consistent with a lesion in mitochondrial protein synthesis."
- [PMID:10710420 "...revealed a G to A transition that causes the replacement of amino acid
  serine (AGU) by an asparagine (AAU) at position 388."] NSM3 = MSD1 S388N suppresses a
  mitochondrial tRNA(Asp) C72U acceptor-stem mutation; single copy sufficient; aminoacylation
  of the mutant tRNA not measured. Also states "The MSD1 gene activity is required for
  maintenance of the mitochondrial genome." - a secondary phenotype; not annotated as
  mitochondrial genome maintenance (downstream of loss of translation).
- [PMID:35820270 "MSD1-knock out yeast (msd1Δ) transformed with the empty vector exhibited
  complete inability to grow on the media containing non-fermentable carbon sources"] -
  complementation model for DARS2 variants; E259K (human E277K) null-like, Q137V partial.
  Phenotype only; no new GO process.
- Mitochondrion: three HDA proteomics datasets.

### Not established in yeast (inferred by homology only)
- Purified-enzyme kinetics; homodimerization; matrix (vs membrane) sub-mitochondrial
  location; residue-level Asp/ATP binding (UniProt ECO:0000250); any tRNA(Asn) misacylation.

### Decisions
- GO:0004815: ACCEPT all four rows (IMP, ISA, IBA, IEA).
- Obsolete GO:0006422 / GO:0070146 -> MODIFY to GO:0070127 (per QuickGO obsoletion
  comment; OLS4 still shows them active - known service disagreement).
- Broad terms (nucleotide binding, aa-tRNA ligase, ligase, cytoplasm, GO:0006418) TOO_GENERAL.
- Nucleic acid binding -> MODIFY to tRNA binding (OB-fold anticodon-binding domain).
- No NEW annotations proposed.
