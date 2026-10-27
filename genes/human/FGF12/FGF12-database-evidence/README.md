# FGF12 database evidence

This compact record traces the database annotations to actual official sources. It establishes target matches and ancestry; it does not turn every automated output into experimentally verified biology.

## What is established

- **ARBA:** P61328 has FunFam `2.80.10.50:FF:000001`. Its official lineage matches ARBA00028183 condition set 21 (Haplorrhini; cell-cell signaling), ARBA00027428 set 46 (Homo; nervous-system development), and ARBA00093068 set 1 (Primates; growth-factor activity). Set indices are zero-based. The three complete official rule records are included.
- **InterPro:** IPR002209 maps to GO:0008083. The official target response identifies reviewed human P61328, length 243, matching the family at residues 15–216. Family membership is not a growth/proliferation assay.
- **PAINT:** Four positive IBD rows join exactly to the repository PTHR11486 TSV. Human FGF12 leaf PTN002479516 descends from both relevant nodes, PTN000160075 and PTN000160077. These are ancestral curator judgments; neither donor count nor the target's presence among donors invalidates them.
- **Canonical sequence:** The target alignment ungaps to the exact 243-aa canonical UniProt sequence. This does not assign localization or activity to the shorter natural product.

## Important capture boundary

The official PANTHER API reports version 19. The MSA response was complete, but the tree request stopped at the acquisition size guard. The received prefix already contains every edge on the target path and the complete target leaf. A parser reads only received tokens; it adds no missing fields or delimiters. The complete leaf is separately decoded from its original byte range.

The multi-megabyte MSA and incomplete tree are **not included here**. `projections.json` contains their target-specific extraction. `source-receipts.json` retains the actual URLs, acquisition times, hashes, byte counts and the tree failure. The URLs are not immutable content-addressed archives: a future server response may differ. The exact original captures are needed to reproduce the extraction, not merely the projections and their hashes.

## Verify without downloads or writes

From this directory, using the repository's existing Python:

```sh
python -B verify.py
```

The default reads the adjacent `FGF12-uniprot.txt` and the repository's `interpro/panther/PTHR11486/PTHR11486-paint.tsv`. Alternate paths may be supplied with `--uniprot` and `--paint`.

This checks hashes of all included official records, recomputes ARBA target matches, verifies the InterPro mapping, joins the four IBD rows, checks the projected path's internal consistency, and matches the projected aligned sequence to canonical UniProt. It explicitly reports that tree/MSA extraction was not independently reproduced.

With access to the exact preserved raw captures:

```sh
python -B verify.py --tree-raw /path/to/PTHR11486-tree.json --msa-raw /path/to/PTHR11486-MSA.json
```

That mode checks their recorded hashes and reproduces the target path, edge ordinals, complete leaf and aligned target sequence. Both modes passed when this compact evidence was prepared. Neither mode claims a complete-tree download or rereads descendant experiments.

## Biological interpretation remains separate

Current GO:0008083 requires stimulation of growth or proliferation. FGFR binding, downstream signaling and survival effects alone do not establish that activity. Conversely, absence of a conventional signal peptide cannot establish universal non-secretion or rule out cell-cell signaling. The historical NOT annotations refer to P61328-2 and require comparison with the particular constructs and endpoints in later papers.

`data/GO-owned-terms.json` preserves the actual official definitions. The strict is_a/part_of ancestor response also places neurogenesis under nervous-system development; it does not itself supply a new developmental experiment. PANTHER gene-info GO-slim summaries are preserved as source output, not treated as additional measured functions.
