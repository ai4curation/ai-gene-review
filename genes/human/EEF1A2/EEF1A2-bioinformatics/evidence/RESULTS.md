# EEF1A2 reproducible evidence results

The raw-input replay resolves human Q05639 to PTN002508371 in the 1,162-node PTHR23115 tree. Its ungapped alignment is exactly the official 463-residue sequence. Four relevant literal IBDs lie on the target path, at PTN000561878 or PTN000562490, with no IRD/IKR loss assertion on that path. The current donor records and their evidence codes are retained separately; they include experimental and propagated assertions. The broader translation IBA is refined to elongation without disputing the valid ancestral placement.

The 281 retrieved IntAct records yield the exact source/partner contexts reported in `results.json`. Participant order, species, tags, fragments, mutations, negative flags and expansion methods are retained. All recovered participant ROGIDs match the corresponding official reference sequences. This does not authenticate the experimental insert. LRRK2 is independently classified as a protein serine/threonine kinase, TBXAS1 and ST6GALNAC1 as enzymes, and SLC13A5 as a transmembrane transporter. Those classes justify informative binding refinements; they do not assign the partner's activity to EEF1A2. TTLL12's family name is not evidence of the catalytic activities its curated record explicitly cautions against. ABTB1, HTT and viral nucleocapsid associations remain bounded by their actual assay and classification evidence.

The primary NDEx AP-MS graph yields EEF1A2 node 599840 (ENSG00000101210), TTLL12 node 555034 (ENSG00000100304), and ABTB1 node 599848 (ENSG00000114626), joined by edges 599842 and 599850, respectively. These are the original coassociation edges, not embedding-derived proximity.

The exact public IntAct URLs, PSI-MI methods, sequence digests, current donor records and ancestral evidence are machine-readable in `results.json`. See `README.md` for replay instructions and limitations. Interpretation of original papers, including the unresolved CMA paralog identity and the direct PI4KB activation experiments, is in the gene source guide and cited publications.


## BioPlex confidence and independently established partner classes

The six source contexts retain the reported association at its assay resolution. They do not establish a direct interface, native physiological regulation, or catalytic/transport activity of EEF1A2. The generated [selected records](bioplex-selection.json), [input manifest](bioplex-inputs.json) and [saved-path extractor](bioplex_reproduce.py) make the scores, direction and context counts inspectable.

| Partner | Independent class authority | 2.0 score | 3.0 score | Bait → prey |
| --- | --- | --- | --- | --- |
| TBXAS1 | [Thromboxane synthase, enzyme](https://www.uniprot.org/uniprotkb/P24557/entry) | 0.841854892390855 | 0.892770103025646 | TBXAS1 → EEF1A2 |
| ST6GALNAC1 | [Sialyltransferase, enzyme](https://www.uniprot.org/uniprotkb/Q9NSC7/entry) | 0.817084938392657 | 0.79450338033373 | ST6GALNAC1 → EEF1A2 |
| SLC13A5 | [Sodium/citrate transmembrane transporter](https://www.uniprot.org/uniprotkb/Q86YT5/entry) | 0.877315845204938 | 0.947898505501937 | SLC13A5 → EEF1A2 |

The reviewed human partner records independently support these classes. GO:0019899 classifies the enzyme partner and GO:0044325 the transmembrane transporter; neither assigns the partner activity to EEF1A2 or requires an activating role. IntAct preserves the source-specific association types and C-terminal tandem tags. Reference-sequence ROGIDs do not authenticate experimental inserts or paralog-discriminating peptide assignments.

All selected scores pass the published 0.75 network threshold. The original Methods describe multiple unique peptides, two acceptable technical runs and abundance/background-frequency filtering. These controls address common background but do not establish that nonspecific capture or indirect complexes are absent. No reciprocal selected pair is present in either directed table. BioPlex 3.0 incorporates earlier 2.0 data, so the source contexts are not independent replication.

| Dataset | All network rows | EEF1A2-incident network rows | All directed edges | EEF1A2-incident directed edges |
| --- | --- | --- | --- | --- |
| 2.0 | 56553 | 48 | 59584 | 53 |
| 3.0 | 118162 | 92 | 129687 | 98 |

These counts require the full checksum-matched upstream inputs. Selecting three partners does not interpret omitted partners negatively. The original `results.json`, `input-manifest.json` and `raw-inputs.tar.gz` are unchanged. The code refactor preserves the original output bytes.
