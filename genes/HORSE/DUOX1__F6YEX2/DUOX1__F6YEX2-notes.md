# DUOX1 (horse, F6YEX2) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This review did not open any ProtNLM2 file or prediction-evidence folder and uses none of their output.

### Why this folder
F6YEX2 is the UniProt gene-centric canonical product of horse DUOX1 (Ensembl canonical transcript ENSECAT00000026134 of ENSECAG00000023918). `genes/HORSE/DUOX1/` is keyed to the alternative product A0A9L0SQG9, so this accession gets its own `HOST__ACC` folder, fetched with `just fetch-gene HORSE F6YEX2 --alias DUOX1__F6YEX2` (32 GOA rows, all IBA or IEA).

### Deep research
`just deep-research-falcon HORSE DUOX1__F6YEX2 --fallback perplexity-lite` failed: falcon returned "Edison API request failed: Failed to authenticate" and the perplexity-lite fallback got HTTP 403 Forbidden. No deep-research file exists. The review uses the cached primary literature already used for human DUOX1 (genes/human/DUOX1), the PTHR11972 PAINT table and family review, and the existing horse model comparison.

### Gene model
Source: [RESULTS-rereview.md](../DUOX1/DUOX1-bioinformatics/RESULTS-rereview.md) from the sibling folder, which compares all four horse DUOX1 TrEMBL products with human Q9NRD9. I did not run a new analysis because that one already covers F6YEX2.
- F6YEX2 (1516 aa) aligns to human residues 1-1516 with no internal gaps and 91.4% identity. It keeps all 15 Ca2+-ligand residues, all 13 heme and all 8 FAD contacts, all 7 TM helices and both EF-hand motifs.
- It lacks the final 35 human residues (1517-1551), so only 6 of 11 NADPH contacts are present (missing human C1520, G1524, N1528, E1549, N1550).
- The canonical transcript's last coding exon is 18 nt; the three other horse DUOX1 transcripts end with a 123-nt exon and cover human 1-1551 with all 11 NADPH contacts. The truncation is therefore most likely a property of this gene model, and the horse gene encodes the full C-terminus. Raised as a suggested question.

### Evolutionary grounding
- UniProt and PANTHER place F6YEX2 in PTHR11972:SF75 (DUAL OXIDASE 1), the subfamily of human DUOX1.
- PAINT: GO:0016174 (H2O2-forming NAD(P)H oxidase) is an IBD at the DUOX node PTN000944147, seeded by human DUOX1/DUOX2, pig and rat DUOX, fly and worm Duox. GO:0016175 (superoxide) and GO:0042554 are at the deeper NOX node PTN000239643 (NOX seeds); I read the split as the curators' decision and follow it, so both superoxide rows are MODIFIED to the H2O2 terms, as in the human review.
- No PAINT node in PTHR11972 carries peroxidase activity, response to oxidative stress or oxidant detoxification.
- Nothing has been measured on horse DUOX1 protein. Every function is an orthology-based inference; none is experimentally established in this species.

### Decisions (32 rows)
- REMOVE: peroxidase activity (human NOT IDA, PMID:19460756; PROSITE PRU00298 residue caution on the horse record), response to oxidative stress, cellular oxidant detoxification (both derived from the peroxidase signature), cuticle development (nematode-only biology).
- MODIFY: superoxide-generating NAD(P)H oxidase activity -> GO:0016174; superoxide anion generation -> GO:0050665; oxidoreductase activity -> GO:0016174; cytokine-mediated signaling pathway -> GO:0071345 (expression induction is a response, not pathway participation).
- ACCEPT: GO:0016174 (IBA, IEA), GO:0050665, plasma membrane (IBA, IEA), apical plasma membrane, NADPH oxidase complex (IBA, IEA), protein heterodimerization (DUOXA1), calcium ion binding, heme binding, FAD binding, NADPH binding (with the gene-model caveat).
- KEEP_AS_NON_CORE: ER, cell surface, cell leading edge, thyroid hormone generation (DUOX2 is the main thyroid paralog), defense response (IBA), IL-8 production, wound healing, cell motility, antiviral innate immune response, defense response to bacterium, response to cAMP. All match the human DUOX1 review.
- No NEW terms: GOA already has the H2O2 process and activity.
