# acsD research and review notes

## 2026-11-06 — type I cellulose audit

Applied annotation-reviewer/core-function guidance. Normal `just fetch-gene KOMXY acsD --uniprot-id P37719` seeded two annotation rows. Their entire non-review payloads and both raw hashes were frozen before editing in `.cache/module-audit-logs/cellulose-20261105/typeI-baseline.json`. Default Falcon attempt failed with HTTP403 authentication; the actual log is retained there. No provider report was fabricated.

Identity: P37719/ACSD_KOMXY is the156aa acsD protein whose primary sequence citation PMID8083166 names ATCC53582/NQ5. ENA X54676 proteinCAA38490.1 is an exact complete match. The2010 native assays and PDB3AJ2/3A8E instead use ATCC23769; their full entity sequences exactly match all156native residues and append only HHHHHH. RCSB source organism and E.coli B834 expression host are different metadata fields. Reproducible code, immutable fetched source records, dependency configuration, justfile, independent tests and results are under acsD-bioinformatics. Retain the frozen species-level UniProt taxonomy: these historically A.xylinum strains also appear under G./K.hansenii in later literature. Exact sequence identity supports the same molecular assembly, not interchangeable strain physiology or historical taxonomy.

PMID8083166 *Characterization of genes in the cellulose-synthesizing operon (acs operon) of Acetobacter xylinum: implications for cellulose crystallization* is abstract-only after normal force retry; direct PMC PDF route returnedHTML rather thanPDF. The abstract explicitly reports residual, reduced celluloseI andII in the acsD mutant. Thus AcsD is involved in cellulose formation but is not obligatory for all polymerization or formation of either allomorph. ATCC53582's acsAB fusion is not this protein or1306-3 P19449.

PMID20921370 *Structure of bacterial cellulose synthase subunit D octamer with four inner passageways* was genuinely fetched as full text by normal force retry. The octamer occurs in two crystal forms and is supported by gel filtration and SAXS. Cellopentaose was soaked into crystals; contacts include Lys6,Asp9,Thr11. Its relatively low occupancy and high B factors indicate weak/flexible binding, and opposing ligand orientations do not establish directed movement. ATCC23769 deletion retained9.6%ofWT celluloseyield; complementation restored87.8%. Removing residues1–6, unlike1–4or1–5, impairedyield. These assays couple the channel-forming/contacting region to biological production and support direct structural participation beyond mere necessity. They do not track glucan translocation or establish a transport mechanism.

The same paper explicitly says the importance of the spiral passageways requires further studies, and that the effects on cellulose physicochemical properties remain to be addressed. Its proposed complete-terminal-complex stoichiometry is a model, not an observed native assembly. Therefore retain cellulose biosynthesis and specific identical-protein binding (both original rows, ACCEPT), but add no catalytic MF, transporter MF, generic binding or obligatory export claim. The self-association term is real but does not by itself identify the physiological organizing activity. Leave core_functions empty rather than invent a specific activity or force a generic structural term into the core. No NEWBP is needed; an existing process annotation already captures supported participation. No IBA rows are present.


## 2026-11-06 — PR2143 round15 follow-up

Added an explicit core-function summary of noncatalytic glucan organization, using the retained cellulose-biosynthetic-process assertion and structural glucan contacts. No new annotation or forced molecular-function term was added.

## PR2143 round17: bacterial process specificity

AcsD supplies noncatalytic glucan organization to the bacterial cellulose machinery. Refine its original process using MODIFY and its structural core process. This does not assert polymerase chemistry or obligatory crystallization; improve ATCC spacing only in authored prose.

QuickGO definitions checked on 2026-11-06 establish GO:0090540 as an is_a subtype of GO:0030244 with bacterial context. The parent and child share the cellulose chemistry criteria. Native output, intact-cell synthesis, crystallinity and fibrils are independent evidence questions, not extra requirements introduced by the bacterial subtype.

Original source/provider bytes and machine payloads are preserved. Supporting sources and target-specific limits are recorded in the reviewed annotation; no new annotation row is introduced in this follow-up.
