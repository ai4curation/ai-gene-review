# Metro guanylate-kinase-domain comparison

[Results and biological interpretation](RESULTS.md).

The question is whether the exact benchmark protein A1Z8G0 retains the nucleotide
recognition sites of an active guanylate kinase. Inputs comprise the target, two
active enzymes, and two MAGUK scaffold controls. The downloaded JSON records are
immutable inputs; [sources.json](sources.json) records URLs, local file timestamps
and checksums. Re-fetch into a separate directory to compare a later release.

From this directory, run `just fetch` then `just analyze`. The scripts require
Python 3.12 or later (standard library only) and external **MAFFT 7.526**. The
`pyproject.toml` declares no Python package dependencies. `fetch.py` retains
existing inputs. `analyze.py` accepts any directory of UniProt JSON records with
one annotated Guanylate kinase-like domain per record, a reference accession and
full-sequence reference positions. It does not encode a biological verdict.

Domains are extracted from UniProt feature boundaries, with no hand-selected
sequence edits. MAFFT L-INS-i (`--localpair --maxiterate 1000`) and G-INS-i
(`--globalpair --maxiterate 1000`) run with one thread. The script maps reference
positions through each alignment into original full-protein coordinates and
writes both alignments, MAFFT diagnostics and JSON results. A second run changes
the reference to the independently characterized human enzyme. Positions listed
in the recipe are explicit analysis inputs derived from the source records and
published nucleotide-pocket experiments, not results embedded in code.

Source metadata for domain boundaries and binding sites can themselves be
computational. They define the comparison regions; biological interpretation
also uses the primary mutagenesis and structural literature, not the mere
presence of an enzyme-like domain label.
