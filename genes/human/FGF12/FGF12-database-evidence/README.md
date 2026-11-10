# FGF12 database evidence

This compact record traces the database annotations to official sources. It establishes target matches, actual ancestry and the assertions in the preserved PAINT family slice; it does not turn automated outputs into measured functions.

## Rule and sequence matches

- **ARBA:** P61328 FunFam `2.80.10.50:FF:000001` and lineage match ARBA00028183 set 21 (Haplorrhini; cell-cell signaling), ARBA00027428 set 46 (Homo; nervous-system development), and ARBA00093068 set 1 (Primates; growth-factor activity). Set indices are zero-based. Complete official rule records are retained in `data/`.
- **InterPro:** IPR002209 maps to GO:0008083. The target response identifies human P61328, length 243, matching residues 15–216. Membership is not a growth/proliferation assay.
- **Canonical sequence:** The target MSA sequence ungaps to the exact 243-aa canonical UniProt sequence. This does not assign location or activity to the shorter natural product.

## Complete preserved PAINT inventory

The earlier projection selected four positive IBD joins and omitted relevant negative assertions. `projections.json` now includes **all 35 literal TSV rows in original order**: 23 positive IBD and 12 negated IRD rows. Eighteen are on the verified root-to-FGF12 path (11 positive and seven negative); the other 17 are explicitly classified as off that path. This is complete coverage of the preserved TSV, not a complete current family tree or every global PAINT record.

Human FGF12 leaf **PTN002479516** descends from **PTN000160077**, which descends from **PTN000160075**. All seven path IRDs are at PTN000160077 with literal `negated=true` and `seeds=PANTHER:PTN000160075`:

| Zero-based TSV index | Negated term | Same-term positive IBD index at PTN000160075 |
|---|---|---|
| 9 | GO:0005576 extracellular region | 0 |
| 11 | GO:0005104 fibroblast growth factor receptor binding | 2 |
| 12 | GO:0008083 growth factor activity | 3 |
| 14 | GO:0008284 positive regulation of cell population proliferation | 4 |
| 15 | GO:0008543 fibroblast growth factor receptor signaling pathway | 5 |
| 16 | GO:0030334 regulation of cell migration | 7 |
| 17 | GO:0043410 positive regulation of MAPK cascade | 8 |

These curated assertions block those same-term positive ancestral transfers along the target path. The other four path IBDs are nucleus and sodium-channel regulator activity at PTN000160077, and cytoplasm and neurogenesis at PTN000160075. They join the four imported positive IBA contexts exactly. The verifier derives the complete partition rather than selecting only positive rows.

**IRD means Inferred from Rapid Divergence**, a phylogenetic evidence code in the [official GO guide](https://geneontology.org/docs/guide-go-evidence-codes/). Its literal WITH/FROM source here is the ancestral gain node. The positive IBD donor lists are preserved in the projection but are not negative experimental donors. Neither the TSV nor the captured tree identifies the publications or experiments motivating these losses. Independence from older FHF studies, including Olsen 2003, is **not established**. Curated MGI, PAINT and UniProt channels must not be counted as independent experimental replication without tracing their underlying studies.

The API's broad GO-slim `(NOT)` summaries remain in the original records but are not extra literal IRDs. In particular, this TSV has no GO:0007267 cell-cell-signaling IRD. A negative specific receptor pathway cannot itself negate all cell-cell signaling or broader parent functions. No new GOA NOT row is manufactured here.

## Capture boundary and verification

The official API reports version 19. The complete MSA contains 982 sequences. The tree request hit its size guard, but the received prefix contains every target-path edge and the complete target leaf. The parser consumes received tokens without adding missing fields or delimiters; the leaf is independently decoded from its recorded character range and hash.

The multi-megabyte MSA and incomplete tree are not duplicated here. `source-receipts.json` records actual URLs, times, hashes, byte counts and the tree failure. Those URLs are not immutable archives. Reproducing extraction requires the exact retained captures, not merely projections and hashes.

Run using the existing Python:

```sh
python -B verify.py
```

Default inputs are adjacent `FGF12-uniprot.txt` and repository `interpro/panther/PTHR11486/PTHR11486-paint.tsv`. `--uniprot`, `--paint` and `--records-dir` can select the same immutable sources in another layout. Default mode verifies included records, rule conditions, InterPro mapping, every TSV row and path classification, all seven negative-to-positive source joins, the four remaining positive joins and projected canonical alignment. It reports that tree/MSA extraction was not reproduced from raw captures.

```sh
python -B verify.py --tree-raw /path/to/PTHR11486-tree.json --msa-raw /path/to/PTHR11486-MSA.json
```

This mode also checks captured hashes and reproduces the target path, edge ordinals, complete leaf and aligned sequence. Neither mode rereads descendant experiments or establishes publication-level independence of the IRDs.

## Biological interpretation

The IRDs are material negative evidence, not an automatic veto on later measured binding, receptor activation or release under specific conditions. Growth-factor activity, GO:0008083, requires stimulation of growth or proliferation; receptor binding, ERK activation and survival alone do not establish it. The broad ARBA/InterPro growth mapping warrants a biological over-annotation assessment while its mechanical provenance remains correct. Historical P61328-2 NOT claims require source-specific comparison with later experiments; original flags, isoforms and source relations remain unchanged. Cell-cell signaling requires separate assessment of physiological information transfer, not merely response to an applied recombinant ligand.
