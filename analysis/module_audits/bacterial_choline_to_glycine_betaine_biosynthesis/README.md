# Choline uptake and glycine betaine synthesis audit

The required boundary is import of extracellular choline followed by its
oxidation to glycine betaine. E. coli BetT supplies a BCCT implementation and
Bacillus OpuB supplies a four-subunit-type ABC implementation. The oxidative
segment can use separate BetA/GbsB and BetB/GbsA enzymes or two independently
evidenced activities of a single Arthrobacter CodA protein. GbsB is a type III
alcohol-dehydrogenase-family enzyme, not a GMC flavoprotein implementation.

Thirteen completed reviews span E. coli, P. putida, B. subtilis and A. globiformis.
Eighteen curated references include four comparative/mechanistic reviews and
primary evidence placed on the relevant steps, subunits and connections.
Acinetobacter remains a literature comparator: its reported PMS-coupled assay
and unresolved N-terminal construct mapping do not establish an exact current
exemplar or native BetB dispensability. KT2440 BetT-I is an unresolved negative
comparator; this does not claim every KT2440 transporter has unknown specificity.

Run `uv run python modules/bacterial_choline_to_glycine_betaine_biosynthesis-source-analysis/check_audit.py`.
The 43 cases combine production topology with explicit family, activity,
complex-member, substrate-specific and bacterial-context evidence. Both CodA
steps must be present: GO:0033713 covers the first and the independently supported
proposed betaine-aldehyde:oxygen oxidoreductase activity covers the second. A generic aldehyde oxidase does not establish oxidation
of betaine aldehyde. `curated-substrate-capabilities.yaml` binds that additional
manual judgment to the reviewed core and primary sources. Synthetic controls
test this distinction and taxon filtering; they do not assert native proteins.

All 94 historical rows, 26 raw UniProt/GOA files and four provider artifacts are
preserved. Thirteen newly added annotations give 107 current rows, including three
inherited proposals. Six unresolved claims remain explicit; COMPLETE means the
curation decisions are finished, not that every biological question is settled.
New Falcon attempts failed with HTTP403 and are documented as manual research.

Focused gene, history and module checks pass. Six module advisories remain: one official PANTHER/UniProt classification disagreement,
three heterogeneous-family activity warnings and two NO_FUNCTION_ID notices for the
proposed CodA activity. The explicit scope oracle checks that proposed activity. Characterized substrate-restricted activities are not
asserted family-wide merely to silence those warnings.

The pre-round1 full-corpus validation finished across 10,543 reviews. Schema, ontology and best-practices have zero blocking errors, and all 54 pathway files with PMIDs pass. Exit status 1 is solely due to 19 reference errors in 17 unrelated yeast reviews. The committed failure inventory proves all 23 review/source/configuration inputs are unchanged from the audit base. The run retains 52 reference advisories and 27,994 best-practice warnings repository-wide, plus 115 ontology label advisories in 109 files.

Published [PR #6108](https://github.com/ai4curation/ai-gene-review/pull/6108); remote review/CI and actual merge remain pending.

## PR6108 round1 follow-up

Claim-linked GbsA/GbsB quotes now distinguish tested substrates, native precursor genetics, soluble-family inference and metal uncertainty. The three untested GbsA aminoaldehyde activities remain UNDECIDED; the full paper does not measure them. BetT and OpuB retain membrane-crossing GO:0055085 alongside cargo transport, which is not its descendant. CodA has a supported proposed second-reaction MF and a GOC mapping-scope query. The older BetA second-activity claim is explicitly DISPUTED with the later purified-enzyme study linked.

Nine changed genes, ten new helper histories, module/schema, checker lint, 43 capacity cases, render and diff checks pass. All 105 published annotation payloads remain unchanged (94 historical plus 11 added); no archive exception is needed. Twenty-six raw files, four provider artifacts and all 91 checked source files are preserved. The subsequent round1 full run on f639eff0aeb29247c7b7b3d9ce36d8290ee9bf92 is now terminal:10,543 reviews, the same19 reference errors in17 unrelated yeast reviews,23 base-identical inputs and24 unchanged science files. Schema, ontology, best-practices and54 pathway checks passed;27,996 best-practice advisories remain. See `round1-fullrun-terminal.json` for exact tuples and the log hash. See `round1-followup.yaml` and `round1-preservation.json`.

## PR6108 round2 follow-up

OpuBC and OpuBD now explicitly propose GO:0015871 through substrate-capture and membrane-translocation participation. The current ontology keeps cargo transport distinct from membrane crossing. Same-role MalE/RbsB and MalF/RbsC annotation conventions are recorded in `round2-transport-evidence.yaml`; primary target studies remain the biological support. One duplicate GbsB reference was removed and five repeated quotes shortened; the complete shared excerpts and provenance are unchanged.

All105 prior payloads,26 raw files,four provider artifacts and91 checked sources are preserved; two new IC process rows give107 current annotations. Three focused gene checks,checker lint and43capacity cases pass. The round2 full run on `96797150bae52515f832f291d90438d540c96bbe` is terminal, exit 1: 10,543 reviews, 19 reproduced reference errors in 17 unrelated yeast reviews and 23 base-identical inputs. Schema and ontology have no blocking errors; best practices has zero errors and 27,994 warnings in 5,036 files. References retain 52 advisories, and all 54 PMID-bearing pathway files pass. Exact errors, source blobs and the log hash are in `round2-fullrun-terminal.json`. Earlier runs remain separately recorded. Renewed review/CI and actual merge remain pending. See `round2-followup.yaml` and `round2-preservation.json`.
