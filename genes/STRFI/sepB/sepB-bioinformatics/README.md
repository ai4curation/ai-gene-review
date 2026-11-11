# Original septacidin cluster identity check

Purpose: determine whether current UniProt entries represent the proteins assayed in PMID:29483275, despite updated genome and gene names.

Input `data/MF372757.1.embl` was downloaded on 2026-10-25 from https://www.ebi.ac.uk/ena/browser/api/embl/MF372757.1?download=false . It is the original deposited S. fimbriatus CGMCC 4.1598 septacidin cluster and explicitly cites PMID:29483275. The three UniProt flat files are maintained by the repository fetch pipeline in the neighboring gene folders.

Run from this folder with `just run`, or from repository root with `just --justfile genes/STRFI/sepB/sepB-bioinformatics/justfile run`. Requires uv and just; the script pins Biopython 1.85 through PEP 723 metadata. Python 3.10 or newer is required.

The reusable script takes any EMBL record and one or more `gene=UniProt-file` pairs. It translates each CDS under its deposited genetic code, checks that translation against the annotated protein, compares the entire protein against the supplied UniProt sequence, and reports lengths and SHA256 digests. It does not encode expected identities or functions. The negative control deliberately supplies SepC's UniProt record for the SepB CDS. No alignment score or arbitrary similarity threshold is used.

Outputs: `results/identity.tsv`, `results/negative-control.tsv`; interpretation in `RESULTS.md`.
