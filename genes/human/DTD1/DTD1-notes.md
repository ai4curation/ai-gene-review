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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM files were not opened or used; this section is based only on UniProt, Ensembl, PANTHER and cached literature.

### Identity of A0A2R8YCT7 (gene-model problem, not a canonical product)

- A0A2R8YCT7 (127 aa, TrEMBL) is the translation of Ensembl ENST00000647441 / ENSP00000493969. Ensembl annotates that transcript with biotype **nonsense_mediated_decay**. The canonical DTD1 product is Q8TEA8 (209 aa, Swiss-Prot; ENST00000377452, Ensembl canonical).
- The NMD model carries an extra 47-nt exon (chr20:18620067-18620113, length mod 3 = 2) between canonical exons 3 and 4. The CDS ends inside it (18620080).
- Protein consequence: residues 1-124 are identical to Q8TEA8, followed by a frameshifted tail `TLF` (canonical continues `GKFGAYMQVHIQNDGPVT...`). Earlier notes gave "125/127 identities over 1-127". That figure is an alignment artifact: only Phe127 matches by chance.
- Lost relative to canonical: the final core beta-strand 131-146 (PDB 2OKV), the NxGP(V/F)T motif with the cross-subunit Gly139-Pro140 chiral-selection dipeptide, and the whole disordered vertebrate-specific C-terminal extension (142-209: DNA binding, Ser197/204/205 phosphosites, Cdc45-regulating region). Retained: the Mg2+ ligands 4, 6 and 28 and the SQFTL motif (78-82).
- UniProt gives PE 1 from PeptideAtlas/ProteomicsDB only. Any peptide inside 1-124 is shared with Q8TEA8, so it does not show that this product exists.
- Analysis: [DTD1-bioinformatics/RESULTS-rereview.md](DTD1-bioinformatics/RESULTS-rereview.md) (script `compare_gene_model_rereview.py`; earlier RESULTS.md left untouched).

### Evolutionary grounding

- PANTHER PTHR10472:SF5 (D-AMINOACYL-TRNA DEACYLASE 1) holds both A0A2R8YCT7 and Q8TEA8. DTD2 (Q96FN9) is in SF1. Q8TEA8 carries IBA (GO_Central) for D-tyrosyl-tRNA(Tyr) deacylase activity and tRNA metabolic process, so the deacylase is ancestral for the subfamily and the canonical gene inherits it.
- The mechanism of the family (P. falciparum DTD, PMID:24302572): the active sites are at the dimer interface, and each subunit donates a Gly-cisPro. The fragment's failure is therefore structural loss in this gene model, not a lineage-level loss of function.
- Family review interpro/panther/PTHR10472/PTHR10472-review.yaml agrees on SF5 placement (no disagreement). It currently lists the fragment A0A2R8YCT7, not Q8TEA8, as the SF5 representative. Q8TEA8 would be a better representative once it is reviewed.

### Decisions

- The three MF rows (GO:0002161, GO:0051499, GO:0106026) are REMOVE for this product, since the editing site cannot form.
- The two BP rows (GO:0006399, GO:0106074) were changed from UNDECIDED to MARK_AS_OVER_ANNOTATED. Both are true of the gene but depend on the removed activity.
- Cytoplasm stays UNDECIDED. Canonical cytoplasm is itself only ISS, nucleus is experimental, and nothing is known for this product.
- No core functions are given for this product. The description was rewritten to describe the gene and canonical product, and the gene-model defect, without project commentary.
- No DTD-related modules were found in modules/.
- Next relative: the canonical product Q8TEA8 (same_gene_canonical), which has no review in the repo. The folder should be genes/human/DTD1__Q8TEA8.
