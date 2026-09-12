# Metro: enzyme-derived guanylate-kinase-like scaffold domain

**The selected Metro protein A1Z8G0 has an altered nucleotide pocket consistent
with a catalytically inactive MAGUK scaffold. Its electronic kinase and
transferase annotations are not supported by retention of the guanylate-kinase
fold.** This conclusion combines target-sequence observations with experimental
work on the enzyme-to-scaffold transition; it is not a direct Metro enzyme assay.

## Sequence observations

The target is the exact 595-aa benchmark protein. Its UniProt-annotated GUK-like
domain spans residues 389–580. Both MAFFT L-INS-i and G-INS-i give the same
correspondences for every inspected reference site. The independent run using
human GUK1 as the positional reference reproduces the key mapping.

| Reference feature | Yeast active GUK1 P15454 | Human active GUK1 Q16774 | Metro A1Z8G0 | Rat PSD-95 P31016 | Human MPP1 Q00013 |
|---|---|---|---|---|---|
| ATP-loop lysine | Lys15 | Lys17 | Arg402 | Lys544 | Arg295 |
| Following ATP-loop residue | Ser16 | Ser18 | Asn403 | Asp545 | Ser296 |
| GMP recognition site | Ser35 | Ser37 | Pro422 | Pro564 | Pro315 |
| GMP recognition site | Asp101 | Asp103 | His488 | Ser631 | Glu381 |

The complete target segment corresponding to yeast residues 9–16 is
**GAPGVGRN** (Metro396–403), compared with **GPSGTGKS** in yeast. A Lys-to-Arg
substitution alone would not establish inactivity; the broader pocket changes
and the experimentally characterized Ser-to-Pro correspondence are more
informative. Several other GMP-contacting positions remain conserved, including
the equivalents of yeast Arg39, Arg42, Tyr51 and Glu70. The domain has retained
substantial recognition-site structure rather than losing every ligand contact.

Direct outputs: [site mappings](results/results.json),
[local-pair alignment](results/localpair.fasta),
[global-pair alignment](results/globalpair.fasta), and
[human-reference control](results/human-reference-control/results.json).
Full accession records and their SHA-256 checksums are in
[sources.json](sources.json); [methods and reproduction](README.md).

## Experimental grounding and scope

Olsen and Bredt, *Functional analysis of the nucleotide binding domain of
membrane-associated guanylate kinases* (2003),
[PMID:12482754](https://pubmed.ncbi.nlm.nih.gov/12482754/),
[DOI:10.1074/jbc.M210165200](https://doi.org/10.1074/jbc.M210165200),
experimentally connected altered GMP-pocket residues to deficient nucleotide
recognition. Reciprocal substitutions restored GMP binding to PSD-95 without
restoring its catalysis. The reproduced PSD-95 positions Pro564/Ser631 provide a
control on this analysis; active yeast/human enzymes retain Ser/Asp at the
corresponding sites. The cached publication is abstract-only; the sequence
coordinates themselves are independently calculated here.

Zhu et al., *Guanylate kinase domains of the MAGUK family scaffold proteins as
specific phospho-protein-binding modules* (2011),
[PMID:22117215](https://pubmed.ncbi.nlm.nih.gov/22117215/),
[DOI:10.1038/emboj.2011.428](https://doi.org/10.1038/emboj.2011.428),
provides full-text structural and biochemical evidence for this functional
repurposing. Its comparison includes MPP-family domains, making it relevant to
Metro's p55/MPP architecture. The paper is cached with full text. This supports
the family-level interpretation but does not identify a specific phosphopeptide
partner of the Metro GUK domain.

The direct Metro study,
[Bachmann et al., PMID:20427642](https://pubmed.ncbi.nlm.nih.gov/20427642/),
[DOI:10.1523/JNEUROSCI.0778-10.2010](https://doi.org/10.1523/JNEUROSCI.0778-10.2010),
establishes an L27-dependent synaptic scaffold role. Together with the observed
pocket substitutions, it supports rejecting the electronic catalytic transfer.
The present data do **not** establish complete absence of ATP/GMP binding,
exclude all possible residual chemistry, or justify annotating Metro with a
particular phosphopeptide-binding specificity. Generic nucleotide-binding
annotations can remain unresolved separately from the catalytic claim.

## Verification checklist

- [x] Scripts accept inputs and positions as parameters; no biological verdict
  or expected target residue is hardcoded in the analysis.
- [x] The pipeline ran on two active enzymes and two independent MAGUK controls
  in addition to Metro; a second run used human GUK1 as the reference.
- [x] Both alignment strategies completed successfully and preserve every input
  domain sequence exactly.
- [x] Raw source records, alignments, diagnostics and numerical results are saved.
- [x] Findings distinguish sequence observations, experimental comparator
  evidence and inference about Metro; no target biochemical assay is claimed.
