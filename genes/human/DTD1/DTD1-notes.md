# DTD1 (A0A2R8YCT7): evidence and exact-input prediction review

A0A2R8YCT7 is shorter than the experimentally characterized DTD1 editing core and lacks the conserved Gly-cisPro motif. ProtNLM describes the full editing mechanism, but the selected sequence does not preserve the machinery needed for that inference.

## Input identity and functional boundary

A0A2R8YCT7 and Q8TEA8 share HGNC:16219. The selected 127 residues align to reference 1–127 with 125 identities. Reference Gly139–Pro140 is outside the selected product. This is a sequence deletion, not a measured cis-to-trans conformational change or evidence of conversion into the DTD2/ATD paralog.

## Biological evidence

- [PMID:17264083 — Structure and function of the c-myc DNA-unwinding element-binding protein DUE-B.](https://pubmed.ncbi.nlm.nih.gov/17264083/): Purified human DUE-B/DTD1 N-terminal core has D-aminoacyl-tRNA deacylase and ATPase activities; C-terminal material is required for DNA binding.

> the N-terminal
> core of DUE-B is shown to display both D-aminoacyl-tRNA deacylase activity and
> ATPase activity.

- [PMID:24302572 — Mechanism of chiral proofreading during translation of the genetic code.](https://pubmed.ncbi.nlm.nih.gov/24302572/): Structural and biochemical analysis establishes the conserved cross-subunit Gly-cisPro substrate-selection mechanism in the DTD family.

> how it uses an invariant
> 'cross-subunit' Gly-cisPro dipeptide to capture the chiral centre of incoming
> D-aminoacyl-tRNA.

## Exact non-GO claims

The complete emitted record is preserved in [DTD1-protnlm-source.json](DTD1-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> D-tyrosyl-tRNA(Tyr) deacylase

NPI (CS 0) as an enzymatic name for A0A2R8YCT7: the short sequence lacks the reference Gly-cisPro motif needed for the conserved editing site. “DTD1-derived fragment” captures the supported identity without assigning deacylase activity. [Sequence mapping](DTD1-bioinformatics/RESULTS.md); [PMID:24302572](https://pubmed.ncbi.nlm.nih.gov/24302572/).

### Function

> An aminoacyl-tRNA editing enzyme that deacylates mischarged D-aminoacyl-tRNAs. Also deacylates mischarged glycyl-tRNA(Ala), protecting cells against glycine mischarging by AlaRS. Acts via tRNA-based rather than protein-based catalysis; rejects L-amino acids rather than detecting D-amino acids in the active site. By recycling D-aminoacyl-tRNA to D-amino acids and free tRNA molecules, this enzyme counteracts the toxicity associated with the formation of D-aminoacyl-tRNA entities in vivo and helps enforce protein L-homochirality

NPI (CS 0) for the composite assertion that this selected protein executes the complete DTD editing mechanism. The family mechanism, D-aminoacyl-tRNA hydrolysis and chiral rejection are real, but its conserved Gly-cisPro element is deleted here. Gly-tRNA(Ala) hydrolysis and an in vivo protection phenotype have not been demonstrated for this truncated product. This does not challenge the full-length human DTD1 activity measured in PMID:17264083 or infer an ATD-like alternative specificity. [PMID:17264083](https://pubmed.ncbi.nlm.nih.gov/17264083/); [PMID:24302572](https://pubmed.ncbi.nlm.nih.gov/24302572/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

PTHR10472:SF5 supports DTD1 ancestry. Functional transfer still requires the dimeric editing pocket: the benchmark target lacks a conserved motif present in the same-gene reference. No paralog switch or ancestral function change is asserted.

## Evidence limits

PMID:17264083 is abstract-only in the cache; the DTD structural/mechanistic paper has full text. Activity of the exact 127-residue product was not measured in these sources. No core MF is assigned. Proteomics-database cross-references alone do not establish the short product’s activity.

Exact sequence mapping: [DTD1-bioinformatics/RESULTS.md](DTD1-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Research integration

The genuine [Falcon report](DTD1-deep-research-falcon.md) supplies literature synthesis for DTD1. Its full-length enzyme mechanism is interpreted through the exact127-residue input and the mapped absence of the Gly-cisPro site; activity of the longer human editing core is not an assay of this short product.
