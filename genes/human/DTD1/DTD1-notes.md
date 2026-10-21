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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20 full re-review

This re-review was done independently of any machine-learning name or function
prediction for this entry; the earlier notes (which discussed such predictions)
were replaced. Sequence analysis in `DTD1-bioinformatics/` now reads the
sequence from the UniProt flat file and Ensembl transcript data directly.

#### Identity of the benchmark accession

- A0A2R8YCT7 is an unreviewed TrEMBL entry (127 aa) imported from Ensembl
  ENSP00000493969 / transcript ENST00000647441 (DTD1-203).
- Ensembl REST (`DTD1-bioinformatics/RESULTS.md`, `ensembl-gene.json`) gives this
  transcript the biotype `nonsense_mediated_decay`; the canonical transcript is
  ENST00000377452, which encodes the 209-aa reviewed product Q8TEA8.
- Residues 1-124 are identical to Q8TEA8 1-124; the product then ends with a
  three-residue alternative tail `TLF` (Q8TEA8 continues `GKFGAYMQVH...`).
- Missing relative to Q8TEA8: the beta strand 131-146 (from the human DTD1 crystal
  structure features in Q8TEA8), the Gly139-cisPro140 chiral-selection motif, and the
  whole disordered basic C-terminal region 142-209 that DUE-B work showed is needed
  for DNA binding [PMID:17264083 "this region is essential for DNA binding in vitro and becomes ordered in the presence of DNA"].
- Conclusion: A0A2R8YCT7 is the predicted product of an NMD-targeted alternative
  transcript, i.e. a C-terminally truncated alternative gene model of DTD1, not the
  canonical gene product. PE 1 in UniProt comes from proteomics peptides, which can be
  explained by the 124-residue segment shared with Q8TEA8; no peptide specific to the
  `TLF` tail is documented.

#### Family and evolutionary placement

- PANTHER PTHR10472:SF5 (D-AMINOACYL-TRNA DEACYLASE 1), shared with Q8TEA8, mouse
  Dtd1 (Q9DD18), yeast DTD1 (Q07648), E. coli dtd (P0A6M4) and P. falciparum DTD
  (Q8IIS0) (`interpro/panther/PTHR10472/PTHR10472-entries.csv`). DTD2 (ATD-like) is a
  separate subfamily (SF1) and is not relevant here.
- PAINT node PTN000049487 propagates D-tyrosyl-tRNA(Tyr) deacylase activity
  (GO:0051500), tRNA metabolic process (GO:0006399) and cytoplasm (is_active_in) to the
  canonical human DTD1 Q8TEA8, with donors including mouse Dtd1 (MGI:1923485), yeast
  DTD1 (SGD S000002378) and E. coli dtd (QuickGO, Q8TEA8 annotations, retrieved
  2026-10-20). The benchmark accession A0A2R8YCT7 does not carry these IBAs.
- PANTHER family review `interpro/panther/PTHR10472/PTHR10472-review.yaml` places
  A0A2R8YCT7 in SF5 as well; no disagreement on subfamily placement.

#### Biology of the gene (canonical product)

- DTD hydrolyses D-aminoacyl-tRNAs; E. coli and yeast mutants lacking the deacylase
  are hypersensitive to several D-amino acids [PMID:10918062 "d-Tyr-tRNA(Tyr) deacylase has a specificity broad enough to recycle any of these molecules"].
- The E. coli enzyme is an obligate dimer whose beta-barrel is formed by both subunits
  [PMID:11568181 "This barrel results from the assembly of the two subunits."].
- The cross-subunit Gly-cisPro motif captures the chiral centre of the substrate and
  rejects L-aminoacyl-tRNAs [PMID:24302572 "'cross-subunit' Gly-cisPro dipeptide to capture the chiral centre of incoming"].
- DTD also edits Gly-tRNAAla, conserved across bacteria and eukaryotes
  [PMID:28362257 "DTD's activity on non-cognate Gly-tRNAAla is conserved across all bacteria and eukaryotes"].
- Human DTD1 (as DUE-B): N-terminal core has deacylase and ATPase activity; C-terminus
  needed for DNA binding [PMID:17264083]. DUE-B binds replication origins with CDC45
  and TOPBP1 [PMID:20065034].
- Human DTD1 is enriched at the nuclear envelope and its silencing sensitises HeLa cells
  to D-amino acids [PMID:18700836 "h-DTD (human DTD) is enriched in the nuclear envelope region of"].

#### Implications for A0A2R8YCT7 annotations

All six GOA rows are IEA, transferred from InterPro/UniRule/Rhea family signatures
that match the N-terminal portion. The product lacks the final beta strand and the
Gly-cisPro motif that, in the dimer, form the editing site; it is encoded by an
NMD-biotype transcript. Catalytic MF rows and the BP rows that are derived from them
are removed for this accession; the gene-level functions remain correctly annotated
on Q8TEA8. Cytoplasm is left UNDECIDED (no evidence the product accumulates).

#### Closest characterised relative

- Same-gene canonical product Q8TEA8 is the primary experimental reference (not a
  relative). Closest characterised ortholog in SF5 with PAINT donor status: yeast
  DTD1 (Q07648, YDL219W); no repo review exists (`genes/yeast/` has no DTD1 folder).
- No module under `modules/` covers aminoacyl-tRNA editing / DTD.

#### Deep research

`DTD1-deep-research-falcon.md` (2026-09-10) is a sound gene-level summary; it
correctly flags that A0A2R8YCT7 is a non-canonical Ensembl-derived entry.
