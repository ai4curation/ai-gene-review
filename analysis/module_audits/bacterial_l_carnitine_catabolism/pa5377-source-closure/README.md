# Additive PA5377 source closure

This closure extends the approved Carnitine publication inputs with the bounded PA5377 follow-up. It does not edit science, source caches, earlier receipts, render output or project metadata.

The private approved-main-1349 publication manifest is copied byte-for-byte into `prior-publication-manifest.json`. It contains 332 paths: all 327 nonshared paths are verified unchanged. Exactly five dynamic project/tracker paths are named and excluded in `prior-and-supersession.json`; existing fixed proof files are retained. The prior 325-file historical validation count is a different provenance statement and is not altered by this closure.

The current map has 344 inputs: the complete prior nonshared map, every file and source dependency of the PA5377 follow-up handoff, all five relevant family reviews/raw sources, raw sources for the reviewed genes, and explicit curated citations. The three PA5377 science/notes/HTML successors are mapped to their exact before/after hashes. Earlier seals and their bytes are unchanged. PA5377 was an adjacent review outside the prior module publication map; this receipt does not pretend that its change supersedes one of the original 327 paths.

The citation roots comprise 14 module reviews plus the PA5377 duplicate, module/notes, five family reviews and gene notes. There are 212 resolved citation edges and 17 publication caches. Every explicit curated PMID/file citation resolves; there are no Reactome citations. Local file citations and directly linked notes are followed. Normal publications remain unchanged, with cache-specific title/access flags recorded in `publication-access.json`. An abstract-only normal cache does not erase independently recovered full-source excerpts in the existing provenance files.

Seven linked provider reports are included as immutable source bytes but their bibliographies are not expanded. `provider-boundaries.json` inventories their PMID leads and explains the boundary. This is closure of the curated evidence and declared preserved publication inputs, not a claim that every unadopted provider bibliography has been read or acquired. No private cache dependency is necessary for the checker.

The 15 reviews contain 171 ordered rows: 146 in the existing module panel and25 in the adjacent PA5377 review. Historical NEW counts remain11 total,6 active and5 retired. PA5377 and cbcW share Q9HTI7; counting both reviewed records does not create another biological module member. The approved PA5377 preservation receipt covers its exact25-row payload/order/qualifier/lifecycle check; all other reviews remain byte-identical to the prior map.

Run from the repository root:

```sh
.venv/bin/python -B analysis/module_audits/bacterial_l_carnitine_catabolism/pa5377-source-closure/check.py
```

The checker is read-only and verifies all hashes, both handoff sections, the explicit supersessions and citation targets. `capture.py` refuses regeneration after sealing. Checker and Ruff results are captured in `checks.json`. No full-corpus validation or publication action was performed; root owns final integration and publication.
