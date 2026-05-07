# cmd-1 notes

## 2026-03-19 ISO-focused review pass

- GOA snapshot after `just fetch-gene worm cmd-1`: 21 annotations total. There are no current `ISO` evidence-code annotations for `cmd-1`; the transfer-style set is `IBA` plus `IEA`, so the ISO-focused review mainly evaluates whether those orthology/electronic calls are conservative enough.
- `cmd-1` is the single C. elegans calmodulin. UniProt describes it as a 149 aa calmodulin with four functional calcium-binding sites and broad Ca2+-dependent regulation of enzymes, ion channels, and other proteins [PMID:17854888 Ca(2+)/Calmodulin-binding proteins from the C. elegans proteome., "Calmodulin (CaM) is the primary Ca(2+)-sensor that regulates a wide variety of cellular processes in eukaryotes."].
- The 2003 RNAi study supports broad developmental phenotypes but not a narrow mechanistic process model: `cmd-1` knockdown caused embryonic lethality, disturbed morphogenesis, aberrant cell migration, hyperproliferation, and apoptosis defects [PMID:14703012 Functional analysis of the single calmodulin gene in the nematode Caenorhabditis elegans by RNA interference and 4-D microscopy., "Embryos show disturbed morphogenesis, aberrant cell migration patterns, a striking hyperproliferation of cells and multiple defects in apoptosis."].
- The 2007 early embryo paper is important because it separates localization from function in cytokinesis: CMD-1 is not required for cytokinesis, but GFP-tagged CMD-1 localizes to spindle/centrosomal and membrane-associated structures [PMID:17716666 Cytokinesis is not controlled by calmodulin or myosin light chain kinase in the Caenorhabditis elegans early embryo., "GFP-tagged CMD-1 does not accumulate at the furrow, but does accumulate on the spindle and centrosomes (as well as to the interphase nuclear membrane and the borders of abutting cells)"].
- The 2009 spindle paper supports the strongest specific non-core process annotation: CMD-1 participates in a spindle-pole complex with ASPM-1/LIN-5 and is required for meiotic spindle organization/orientation [PMID:19219036 NuMA-related LIN-5, ASPM-1, calmodulin and dynein promote meiotic spindle rotation independently of cortical LIN-5/GPR/Galpha., "ASPM-1, together with calmodulin (CMD-1), promotes meiotic spindle organization and the accumulation of LIN-5 at meiotic and mitotic spindle poles."].
- The 2021 CAMTA paper supports a context-specific transcriptional feedback loop and neuronal behavioral phenotypes, not a general gene-expression role [PMID:34499028 Neuronal calmodulin levels are controlled by CAMTA transcription factors., "high levels of CMD-1 can repress expression from the cmd-1 promoter"] [PMID:34499028 Neuronal calmodulin levels are controlled by CAMTA transcription factors., "Supplementing CMD-1 in the nervous system ... restored normal chemotaxis toward salt, benzaldehyde, and diacetyl"].

## Curation take

- Keep `calcium ion binding`, `cytoplasm`, and `enzyme regulator activity` as core.
- Keep spindle/pole localizations and spindle-orientation annotations as valid but non-core.
- Treat the `IBA` microtubule organization term as plausible but non-core rather than as a defining calmodulin function.
- `protein binding` is too generic for calmodulin; preferred replacement is `GO:0048306 calcium-dependent protein binding`.
- `negative regulation of gene expression` is over-annotated relative to the specific cmd-1 autoregulatory feedback described in PMID:34499028.
- `apoptotic cell clearance` remains the weakest call because the accessible abstract for PMID:14703012 supports apoptosis defects generally, but not clearly corpse clearance specifically.
