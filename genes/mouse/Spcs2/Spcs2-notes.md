# Spcs2 (A0A140LHW5): evidence and exact-input prediction review

A0A140LHW5 is a short Spcs2-derived product lacking the membrane-spanning architecture of the full subunit. The peptidase prediction assigns catalytic activity to an accessory subunit. Complex membership and signal-peptide processing are plausible for full-length Spcs2 but unproven for this selected product.

## Input identity and functional boundary

A0A140LHW5 and Q9CYN2 share MGI:1913874. The first 66 residues are identical; the selected product has an eight-residue alternative tail. Both reference transmembrane helices (87–107 and 112–132) lie outside that conserved segment. The global alignment of the eight-residue tail to isolated reference residues is not evidence that a transmembrane helix is retained.

## Biological evidence

- [PMID:34388369 — Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage.](https://pubmed.ncbi.nlm.nih.gov/34388369/): Human structural analysis identifies distinct catalytic SEC11 subunits within the four-subunit signal peptidase complex.

> the 
> human SPC exists in two functional paralogs with distinct proteolytic subunits.

- [PMID:42173868 — Structural basis of signal peptide recognition by the signal peptidase complex.](https://pubmed.ncbi.nlm.nih.gov/42173868/): The substrate-bound human structure distinguishes SPCS2 from the catalytic SEC11 subunit.

> the catalytic SPC subunit (paralog Sec11A or Sec11C, respectively) is joined by SPCS1 (also known as SPC12), SPCS2 (SPC25), and SPCS3 (SPC22/23).

## Exact non-GO claims

The complete emitted record is preserved in [Spcs2-protnlm-source.json](Spcs2-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Signal peptidase complex subunit 2

CNN (CS 2) as a gene-of-origin label, with an essential truncation qualification: the sequence shares the Spcs2 N terminus. UNC if interpreted as an assembled, functional signal peptidase subunit. [Sequence mapping](Spcs2-bioinformatics/RESULTS.md).

### Location

> Endoplasmic reticulum membrane

UNC (CS 1). The two reference membrane helices are absent from the retained sequence. Indirect ER association remains possible through protein partners, but it is not demonstrated for A0A140LHW5; absence of a transmembrane helix alone is not proof of exclusively soluble localization.

## Emitted GO claims

All 3 emitted GO claims are individually assessed in [Spcs2-protnlm-predictions-review.yaml](Spcs2-protnlm-predictions-review.yaml).

## Family integration

The exact accession has no PANTHER assignment. Q9CYN2 provides independently verified same-gene context for PTHR13085; that family membership does not validate the selected short product as an assembled subunit or enzyme.

## Evidence limits

The exact-product GOA snapshot is empty. No core molecular function is asserted. Human complex structures establish the catalytic/accessory distinction, while exact mouse product expression, membrane binding and complex incorporation remain unresolved.

Exact sequence mapping: [Spcs2-bioinformatics/RESULTS.md](Spcs2-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Research integration

The genuine Falcon report is retained. Its gene-level synthesis is interpreted through the exact product sequence and the primary sources above; the truncation boundary and paralog distinctions are assessed independently.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used. Sources: UniProt A0A140LHW5 and Q9CYN2, Ensembl
gene ENSMUSG00000035227, PANTHER PTHR13085 family files, PMID:34388369, PMID:42173868,
and the Falcon deep-research report (gene-level; it does not notice that the accession is
a short alternative product).

### Identity: alternative transcript product, not the canonical protein

New analysis: `Spcs2-bioinformatics/compare_sequences_rereview.py` -> `RESULTS-rereview.md`
(live UniProt + Ensembl REST fetch; earlier RESULTS.md left untouched).

- A0A140LHW5 = ENSMUSP00000146574, the 74-aa translation of Ensembl transcript Spcs2-206
  (ENSMUST00000208465, protein_coding, not canonical). Canonical is Spcs2-201
  (ENSMUST00000036274) -> Q9CYN2, 226 aa, Swiss-Prot reviewed.
- Spcs2-206 has 4 exons. It skips canonical coding exon 3 (ENSMUSE00000263814, 161 nt;
  161 mod 3 = 2, frameshifting) and uses a shorter version of canonical exon 4
  (5' end at 99493966 instead of 99494041 on the minus strand). Exons 1-2 encode exactly
  66 aa of CDS (114 + 84 nt), matching the 66-residue identical prefix; the 8-residue tail
  KRPHRNGS is out-of-frame sequence from the shortened exon 4, and is not in Q9CYN2.
- Lost relative to canonical: both TM helices (87-107, 112-132), the lumenal loop, the
  C-terminal cytosolic domain (133-226) and the acetyl-lysine sites K169/K191. Retained:
  N-acetyl-Ala2 site and the Gly-rich, predicted-disordered N-terminal cytosolic segment.
- UniProt PE 1 rests on proteomics hits; because residues 1-66 are shared with Q9CYN2,
  these cannot be assigned uniquely to this product unless a tail-spanning peptide was seen.
  Not used as evidence of function.
- Record type: isoform / alternative gene model product of the same gene (MGI:1913874).

### Annotations

GOA has zero rows for A0A140LHW5, so there are no existing annotations to act on.
I propose no NEW annotations: the activities and complex membership of SPCS2 are
established for the full-length two-pass membrane protein (human Q15005 and mouse Q9CYN2,
both PANTHER PTHR13085:SF0, PAINT node PTN000317824 IBD for GO:0005787 signal peptidase
complex, GO:0045047, GO:0051604). The fragment has no PANTHER assignment and lacks the
membrane region through which SPCS2 contacts the complex
[PMID:42173868 "The TM helix of SPCS2 displays a limited set of contacts"], so neither
complex membership nor ER-membrane localization can be transferred. The SPC is catalysed
by SEC11A/C [PMID:42173868 "the catalytic SPC subunit (paralog Sec11A or Sec11C,
respectively) is joined by SPCS1 (also known as SPC12), SPCS2 (SPC25), and SPCS3
(SPC22/23)."], so peptidase activity would be wrong even for full-length Spcs2.
core_functions left empty deliberately.

### Changes vs previous review

- Description rewritten: identifies the transcript model (Spcs2-206), the exon-3 skip and
  frameshift, and the retained/lost regions explicitly.
- Added RESULTS-rereview.md, UniProt file and an extra PMID:42173868 finding as references;
  kept the earlier RESULTS.md and the ProtNLM source JSON references (the latter marked
  relevance NONE, not opened).
- Added suggested experiment and a BIOLOGY knowledge gap on whether the product exists.

### Relative, family, modules

- Relative to review next: canonical same-gene product Q9CYN2 (mouse Spcs2, Swiss-Prot).
  No review of Q9CYN2 exists in the repo (genes/mouse/Spcs2 is keyed to the fragment), so
  the folder would be genes/mouse/Spcs2__Q9CYN2. Human SPCS2 (Q15005) and DROME Spase25
  are already reviewed.
- PANTHER family review interpro/panther/PTHR13085/PTHR13085-review.yaml places Q9CYN2 in
  SF0 and treats A0A140LHW5 as unassigned gene context. No disagreement.
- Modules: only modules/dmel_signal_peptidase_complex.yaml (Drosophila SPC, includes the
  Spase25 ortholog); no mammalian SPC module exists.
