# PA2402 (Q9I179) — review notes

Reviewed to fill the pyoverdine NRPS-assembly segment. At 5149 residues it is the largest
protein in this corpus's PSEAE set, and it has **no experimental annotation of any kind**: all
four of its GOA rows are IEA, three of them from ARBA association rules.

## Why the folder is a locus tag, and what this gene is probably called

The pyoverdine literature calls PA2402 **PvdI**, one of the main peptide-chain NRPSs:

`[PMID:30386787 "biogenesis starts in the cytoplasm, where non-ribosomal peptide synthetases (NRPSs) such as PvdL 18, PvdI 19 and PvdD 2021 (depending on the strain) assemble an initially acylated ferribactin, the peptide precursor for"]`

But **no checkable source links that symbol to this locus tag.** Every machine-readable record
I examined uses `PA2402` and offers no `pvdI` synonym:

| source | what it says |
|---|---|
| UniProt `GN` | `OrderedLocusNames=PA2402` — no `Name=` line at all |
| GOA `SYMBOL` | `PA2402`; `GENE NAME` is "Carrier domain-containing protein" |
| `DR KEGG` / `DR PseudoCAP` | `pae:PA2402` / `PA2402` |

`just fetch-gene PSEAE pvdI` fails outright for this reason. The folder therefore uses the
locus tag, following the convention already applied to `PA5190`, `PA1268`, `PA0949`, `PA1204`,
`PA2580` and `PA4975`. The review does **not** assert that this gene is PvdI: that is a
widely-used identification in the field and very probably correct, but the project rule against
guessing identifiers applies to gene symbols as much as to term ids. It is recorded as a
question instead, with the locus evidence that makes it plausible — PA2402 lies within the pvd
cluster, two genes from `pvdJ` (PA2400) and three from `pvdD` (PA2399), both of which are
reviewed pyoverdine NRPSs.

## Consequence: no pyoverdine-pathway annotation is proposed

This is the substantive restraint in the review. The gene has no `GO:0002049` row, and the
obvious move — adding one, as the merged `pvdD`, `pvdJ` and `pvdL` reviews all carry it — would
depend entirely on the PvdI identification I cannot establish. So no `NEW` row is proposed, and
the obsolete `GO:0043041` is MODIFYed to `GO:0019184 nonribosomal peptide biosynthetic process`
rather than to `GO:0002049`.

`GO:0019184` was checked in OLS: it exists, is not obsolete, and **is** an ancestor of
`GO:0002049`, so the replacement is deliberately one level shallower than the merged siblings
used. That is the right trade: the NRPS architecture supports "makes a non-ribosomal peptide"
on its own, while "makes pyoverdine specifically" rests on the symbol identification.

If a curator confirms PA2402 = PvdI, the replacement should be deepened to `GO:0002049` and a
`NEW` process row becomes straightforward. That is noted in the row's reason.

## The architecture is solid

What the record does support, independently of any symbol:

- `[file:PSEAE/PA2402/PA2402-uniprot.txt "DR   NCBIfam; TIGR01733; AA-adenyl-dom; 4."]` — four
  amino-acid adenylation domains.
- `[file:PSEAE/PA2402/PA2402-uniprot.txt "DR   InterPro; IPR001242; Condensation_dom."]`
- `[file:PSEAE/PA2402/PA2402-uniprot.txt "DR   InterPro; IPR020806; PKS_PP-bd."]` and
  `IPR006162 Ppantetheine_attach_site` — carrier domains.
- `IPR010060 NRPS_synth`, plus an `AB_hydrolase_fold` region consistent with a terminal
  thioesterase.

So a four-module NRPS with condensation and carrier domains. `GO:0003824 catalytic activity`
MODIFYs to `GO:1904091 non-ribosomal peptide synthetase activity` on that basis — the same
replacement the merged `pvdJ` and `pvdL` reviews make, and supported here by the condensation
domain the row itself cites.

## What the absence of experimental rows means

Worth stating plainly: a 5149-residue enzyme that the field names as a core pyoverdine
synthetase has, in GOA, four electronic rows and nothing else — no IMP despite the pvd
mutagenesis surveys, and no gene symbol. That is a curation gap rather than a knowledge gap,
and it is why this gene was fetched at all.
