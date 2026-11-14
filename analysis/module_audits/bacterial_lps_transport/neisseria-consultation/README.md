# Neisseria Lpt review consultation

Three seeded reviews are COMPLETE: H44/76 LptD F0MIT7 (6 rows), MC58 LptE Q9K0A7 (4), and MC58 LptH Q7DDQ9 (9). All 19 ordered source payloads are preserved. No NEW annotation, deletion, retirement, raw-source replacement or provider fabrication was made.

## Mechanism and strain boundaries

* **LptD:** PMID15192148 directly studies H44/76 imp/lptD. Deletion leaves residual LPS inaccessible to extracellular neuraminidase and a heterologous PagL surface reporter. Control assays establish that PagL remains functional and low LPS abundance alone does not explain failed accessibility. The native outer-membrane localization plus these controls support the surface insertion role. H44/76 survives loss of LPS; survival is not a transport assay. The core records a contribution to LPS transmembrane transport in the Lpt machinery, not autonomous complete seven-component transport or an obligatory LptE requirement.
* **LptE:** H44-derived LptE co-purifies LptD from membrane extracts, with untagged-LptE and BamA controls. Deletion selectively reduces LptD abundance; complementation restores it. The same deletion retains detectable surface-accessible LPS in both the PagL and neuraminidase assay contexts. MC58 Q9K0A7 is identical to the natural H44/76 sequence (159/159), supporting a protein-role inference, not transfer of native expression or mutant phenotype. The core is LptD biogenesis/stability and outer-membrane assembly. It does not invent a purified foldase activity or assert the enterobacterial obligatory translocation role. Membership in the Lpt complex remains supported, and is narrower than a claim that every member catalyzes transport.
* **LptH:** The paper uses this name for the LptA-family carrier, distinct from the unrelated neisserial lipid A phosphoethanolamine transferase called LptA. UniProt calls MC58 NMB0355 lptA; the root-seeded symbol/path lptH is retained. Its 176-residue sequence exactly matches H44/76. Native homolog deletion impairs LPS surface accessibility. Carrier chemistry remains an inference from specific LptA architecture, the PAINT carrier lineage, and comparative purified E. coli LptA transfer (PMID20720015); no isolated MC58 carrier kinetics are claimed. Peripheral outer-membrane association is retained as a phylogenetic bridge-contact inference, not an integral membrane assignment or target fractionation experiment.

The three proteins do **not** establish a complete reviewed Neisseria extractor/bridge panel. Native LptC deletion causes a transport defect; this work supplies no normal-genotype LptC bypass. Meningococcal LPS is also commonly termed LOS; terminology does not create a new assay or extend these experiments to an O-antigen-bearing strain.

## Independent identity and preserved sources

`check_preservation.py` compares every ordered non-review annotation field with `seed-baseline.json`, checks all six seed raw files plus 82 original module sources, and independently re-parses the archived H44/76 genome translations to reproduce exact unique matches (802/802, 159/159, 176/176). The source archive and its SHA256 come from the frozen literature/identity package; no sequence was invented. Natural CDS identity is not a complete tagged-plasmid sequence proof.

The normal PMID21705335 cache is abstract-only and unchanged. Full PMC3190676 was acquired by the literature consultant at `https://pmc.ncbi.nlm.nih.gov/articles/PMC3190676/?report=xml`; `primary-evidence.md` contains checked scoped excerpts with the acquired-text hash. PMID15192148 and PMID20720015 full caches were read without modification. No new publication was fetched by this worker. Full acquired articles remain ignored; only scoped excerpts/provenance are included here.

Fresh official QuickGO definitions are saved in `go-definitions.json`. The LPS-transfer replacement for glycolipid transfer is a supported specificity correction, not an invented parent–child claim. PAINT source nodes were inspected: LptH PTN002194456 and LptE PTN002866256. Normal lineage checks found no applicable IRD/IKR for E/H; F0MIT7 was absent as a target leaf, so its lineage loss status is unavailable, not proven loss-free.

## Validation and research limitations

Three normal Falcon attempts failed HTTP403 authentication; manual notes disclose this and no provider report was fabricated. All three focused gene validations, renders and helper-generated history validations passed. One advisory remains on LptH: its supported core complex membership lacks an annotation row. No NEW row was manufactured to silence that coverage suggestion. Runtime pkg_resources deprecation messages are separate from scientific validation. File-scoped Ruff and the reproducible preservation/identity checker pass. No full-corpus validation or module/family/project edits were performed.

Run:

```sh
uv run python analysis/module_audits/bacterial_lps_transport/neisseria-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_lps_transport/neisseria-consultation/check_preservation.py
```
