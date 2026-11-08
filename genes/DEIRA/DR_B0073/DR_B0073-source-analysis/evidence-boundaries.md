# Deinococcus FruA/FruK evidence boundaries

2026-11-06 manual review. All shared publication and sequence-bridge files are read-only.

## Identity

The committed sequence bridge at analysis/module_audits/bacterial_fructose_pts_catabolism/deinococcus-sequence-bridge.json maps Supplementary Table S2 coordinates on CP150842.1 to KDR_B0073 (89218–91014, reverse strand, 598 aa) and KDR_B0074 (91153–92100, reverse strand, 315 aa). Independent comparison during this review confirmed exact identity of these translations to the frozen Q9RZP7 and Q9RZP6 sequences. Thus both current protein sequences occur in ATCC13939K, irrespective of the broader historical R1 aliases in UniProt. Exact protein identity does not identify the stock or accessory donor proteins used in the older fraction experiment.

## PMID21822900, accessibility and interpretation

DOI https://doi.org/10.1007/s00253-011-3514-x . Publisher article and PDF URLs returned subscription-preview HTML, not the full article. Author/full-text searches did not locate an accessible manuscript; OpenAlex lists this as closed with no repository full text. Requests, responses and extraction are retained only in the ignored deinococcus-review cache. The cached abstract was preserved.

The abstract explicitly reports ATP dependence with deinococcal cytosol and PEP dependence with Rhodobacter capsulatus cytosol coupled to deinococcal membranes. This supports membrane-component compatibility with a PTS relay; it does not locate ATP binding on FruA or identify the replacement cytosolic kinase. No unreported strain stock, purification, kinetic constant or product-isomer measurement is assumed. GO0022877 is retained as a component-capability inference from the membrane result and EIIB/EIIC architecture, not proof of native ATCC13939K PEP-driven uptake.

## PMID38962131 and supplement

DOI https://doi.org/10.3389/fmicb.2024.1410024 . Full cached text and the committed supplement/sequence analysis establish the intact ATCC13939K locus and restored 826-aa FruB ORF. They do not measure its phosphate-transfer activity. Supplementary Table S2 calls KDR_B0074 tagatose-6-phosphate kinase, whereas Table S3 calls counterparts 1-phosphofructokinase. Neither label is a substrate assay. The FruK inference rests independently on NCBIfam TIGR03168, IPR022463, PTHR46566:SF5 and the curated RuleBase reaction in the frozen record.

## Chemistry and topology

QuickGO definitions were checked directly. The net phosphohistidyl-donor fructose PTS reaction (GO0022877) and terminal phosphocysteine-to-fructose step (GO0090582) are compatible levels of description. GO0005351 instead asserts carbohydrate/proton symport. GO0008443 is the generic phosphofructose kinase parent, not a specific assertion of 6-phosphofructokinase.

Q9RZP7 has two type-2 EIIB domains (4–99 and118–213), an EIIC region (247–592), and predicted phosphocysteines at10 and124. These are predictions; no two-turnover stoichiometry or inactive first-repeat designation is inferred. The catalytic and donor roles of the repeats need experimental testing. No ATP-binding annotation is added to FruA. No NEW process annotation is proposed for either protein.
