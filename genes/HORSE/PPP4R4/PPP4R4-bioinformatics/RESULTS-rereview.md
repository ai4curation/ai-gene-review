# PPP4R4 (horse): gene-model inventory and comparison with human PPP4R4 (re-review, 2026-10-20)

Script: `compare_horse_models_rereview.py` (run with `uv run compare_horse_models_rereview.py UP000002281_9796.fasta.gz`).
Raw output: `results-rereview.json`. Sequences were fetched from UniProt REST on 2026-10-20. The horse
reference-proteome canonical set came from the UniProt FTP file
`reference_proteomes/Eukaryota/UP000002281/UP000002281_9796.fasta.gz` (current release). Alignments are
global (BLOSUM62, gap open -10, extend -0.5, free end gaps). Identity is computed over paired residues.

## Gene-model inventory

UniProt has ten horse entries in PANTHER PTHR21467. All ten are Ensembl translations of one gene,
ENSECAG00000019485 (display name PPP4R4, chromosome 24). They are alternative transcripts of a single
gene, not paralogs. None is a Swiss-Prot entry.

- The UniProt gene-centric canonical horse product, the only one in the reference-proteome canonical FASTA, is A0A9L0S938 (869 aa).
- The Ensembl canonical transcript is ENSECAT00000090461, which encodes A0A9L0RAK5 (908 aa). Its N-terminus is
  extended by 51 residues compared with human and it lacks human residues 24-38.
- The benchmark accession A0A9L0S961 (865 aa, ENSECAT00000111071) is not in the canonical set.

| horse accession | length | in UniProt canonical set | identity to human Q6NUP7 (%) | human coverage (%) | indels of 5 or more residues vs human |
|---|---|---|---|---|---|
| A0A9L0S961 (benchmark) | 865 | no | 94.9 | 99.1 | none |
| A0A9L0S938 | 869 | yes | 95.4 | 99.5 | none |
| A0A9L0RAK5 | 908 | no | 93.6 | 97.8 | +51 N-terminal; lacks human 24-38 |
| A0A9L0T1D2 | 876 | no | 95.0 | 99.3 | +9 C-terminal |
| F7CC09 | 852 | no | 92.9 | 95.3 | lacks human 1-37 |
| A0A3Q2KRD2 | 843 | no | 95.3 | 96.6 | lacks human 422-447 |
| A0A9L0RGM2 | 829 | no | 95.2 | 95.0 | lacks human 383-422 |
| A0A9L0RGB6 | 794 | no | 94.0 | 90.3 | lacks human 1-81 |
| A0A3Q2KK51 | 146 | no | 75.9 | 15.2 | N-terminal fragment |
| A0A9L0R809 | 128 | no | 80.5 | 14.7 | N-terminal fragment |

## The benchmark product compared with the canonical product

A0A9L0S961 and A0A9L0S938 are identical over residues 1-861. They differ only at the extreme C-terminus.
The canonical product and human PPP4R4 both end `...QPRKATLKSRKSNP`. A0A9L0S961 ends `...QPRKATFLNI`, which
replaces the last 8 residues with 4 different ones. This most likely reflects an alternative 3' splice choice
in the last exon. The difference lies inside the C-terminal region that UniProt annotates as disordered
(MobiDB-lite, 820-865). Both HEAT repeats (PROSITE PS50077, 213-250 and 252-290), the ARM-like (Gene3D
1.25.10.10) fold region and all of the PP2A-A-like body are retained. A0A9L0S961 therefore carries the whole
structured portion of PPP4R4. It is an alternative C-terminal isoform of the gene, not a fragment.

## GO annotation placement (QuickGO, 2026-10-20)

The PAINT IBA annotations from PTN001087371 (GO:0019888 protein phosphatase regulator activity, GO:0005829
cytosol, GO:0008287 protein serine/threonine phosphatase complex; donor Q6NUP7) are attached to the canonical
A0A9L0S938 only. Ensembl Compara projections (GO_REF:0000107) are attached to A0A9L0RAK5, the Ensembl
canonical. A0A9L0S961 receives only the UniProt SubCell IEA for cytoplasm. Whether a product carries IBA rows
therefore depends on which entry the pipeline treats as canonical, not on any biological difference.

## Limits

This is a pairwise and gene-model analysis. Orthology to human PPP4R4 rests on the shared PANTHER subfamily
PTHR21467:SF0, PAINT node PTN001087371 and the Ensembl gene assignment, not on these identity values. The
analysis does not test whether the 4-residue alternative C-terminus is expressed or functional.

## PP4c-interface residues

Human PPP4R4 mutants R501W and V618D abolish PP4c binding, and V618A weakens it (UniProt Q6NUP7 MUTAGEN
features, from PMID:18715871). Both residues are conserved at the same positions in A0A9L0S961, with
identical local context: R501 in `ASLKWRTHEKL` and V618 in `LTHDPVANVRM`. The script records this under
`pp4c_interface_residues_in_A0A9L0S961` in the JSON output.
