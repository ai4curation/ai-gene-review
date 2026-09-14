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
