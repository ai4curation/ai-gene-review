# E. coli Lpt member consultation

Seven COMPLETE reviews were independently re-audited against their original claims, current ontology definitions and accessible primary literature. This receipt covers genes ECOLI/lptA through lptG only; it does not certify a module, family-wide grant, new species panel or full-corpus validation.

## Scientific decisions

* LptA and LptC supply periplasmic LPS transfer; LptB supplies ATP hydrolysis; LptF/G contribute to extraction/transfer; LptD/E contribute to outer-membrane insertion. Complex activity is not treated as autonomous activity of every component. Membrane-fraction association is not equivalent to integral membrane topology.
* LptC identical-protein binding (GO:0042802, IPI, PMID:21169485) changes from MARK_AS_OVER_ANNOTATED to KEEP_AS_NON_CORE. Wild-type LptC gave a DSP-dependent approximately 46-kDa product in AM604 cells, reversed by reduction. Soluble tagged LptC also showed dimerization in that study. PMID:20720015 reports predominantly monomeric soluble LptC under other conditions; a single LptC per pump does not exclude self-binding. The GO term requires binding, not an obligate physiological homodimer. No assembly-stoichiometry claim is added.
* PMID:42844470 supports LPS-dependent movement of TM-LptC following bridge assembly and increased ATP binding/hydrolysis. Its structure uses an engineered LptC–LptA fusion; LPS-free preparations express E. coli proteins in LPS-null Acinetobacter baylyi. These are not native Acinetobacter ortholog experiments or proof of universal bridge stoichiometry. The frozen normal publication cache is abstract-only; the full publisher text was read from the literature consultant's acquired source.
* PMID:41285762 supports LptM/LptY effects on the mature E. coli LptDE translocon, bridge stability and transport efficiency, in addition to assembly. BW25113 cellular assays, purified structures and molecular-dynamics proposals are distinguished. This does not establish universal accessory necessity or an independently assayed complete flux cycle in every modeled state.
* Location evidence was made claim-specific. LptA periplasm is supported by fractionation; LptF/G six-transmembrane architecture is supported by primary biochemical/structural work. Original proteomics assignments remain preserved, without pretending abstract-only datasets were independently inspected.
* LptG's core partner typo is corrected to LptF. LptC contacts the periplasmic beta-jellyroll of LptF, not an undifferentiated assertion about both F and G.

All 145 historical source payloads remain in order, including four historical NEW rows. No rows were added, retired or deleted. Only the LptC action above changes; all other actions remain. The four NEW rows retain their original actions and lifecycle metadata. The reusable checker compares every non-review field, all 82 root-protected files, the immutable root baseline and append-only notes. `row-audit.json` provides each final row's term, action and claim-specific rationale.

## Evidence access and ontology

`source-access.json` records hashes and access levels for primary literature used here. Shared newly fetched PMID:42844470 and PMID:41285762 caches were acquired by the literature consultant, not overwritten by this consultation. Full acquired articles remain in ignored cache; this handoff contains no full external article copies. Abstract-only originals are not treated as disproven curator claims. In particular, PMID:24990744 supports a conserved LptDE mechanism without being labeled an E. coli native structural sample (the parallel source audit maps 4N4R to Salmonella Typhimurium LT2); PMID:24990751 is Shigella flexneri.

`go-terms.json` and `go-ancestors.json` preserve official QuickGO responses. GO:0140332 describes outer-leaflet extraction, carriage through an aqueous phase and delivery; GO:0015221 describes crossing a membrane. These are not silently interchangeable. GO:0042802 does not require obligate homodimerization. Broader lipid-transfer and lipid-transport replacements are identified as functional refinements rather than invented ontology ancestry.

All seven normal Falcon attempts failed HTTP 403 authentication; no provider output was fabricated. All seven normal PAINT-loss checks returned no IRD/IKR loss on the queried lineage. That result is not a new ancestral-function assertion or a donor-count argument. `research-checks.json` records commands and real exits.

## Checks and limits

Run `uv run python analysis/module_audits/bacterial_lps_transport/ecoli-consultation/check_preservation.py` to reproduce preservation and row accounting. Focused `just validate ECOLI <gene>`, seven helper-generated history validations and seven renders passed. There were no gene-validation warnings; the runtime emitted the pre-existing pkg_resources deprecation notice. File-scoped Ruff passed. Validation logs and hashes are included in this consultation. No full corpus was run and no shared module, family, project, raw source or provider artifact was edited.
