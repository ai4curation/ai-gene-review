# Bacterial cellulose biosynthesis comparative audit

## 2026-11-06 foundation and existing-PR integration

This audit extends the existing draft [PR #2143](https://github.com/ai4curation/ai-gene-review/pull/2143), rather than opening a competing module PR. Its approved head `8a00ca36a30b94c0460a2116a680c5dd0321ee8d` was merged locally onto main `86397521d39020add4e01314e4aae83c6154b000` as `35963935e7`. The integration preserves the original four changed files and adds provenance records; it has not been pushed. Prior approval does not establish the expanded audit or current-main validation.

The existing PSEPK bcsA, bcsB, PP_2638 and PP_2634 reviews were snapshotted before further work: 13 annotation rows, including an inherited authored NEW proposal on PP_2634, and eight raw UniProt/GOA hashes. Existing raw records and provider reports are not refreshed. The baseline and operational logs are in `.cache/module-audit-logs/cellulose-20261105/`.

## Comparative review literature

- [PMID:26077867, Bacterial cellulose biosynthesis: diversity of operons, subunits, products, and functions](https://pubmed.ncbi.nlm.nih.gov/26077867/) is available in normally fetched full text. It separates the in vitro BcsA/BcsB polymerization core from taxon-variable export and accessory proteins. It reports BcsC-lacking type III systems and BcsB-lacking cyanobacterial systems, with proposed alternative export components whose activities were unresolved. These observations prevent a universal BcsAB/BcsC inventory claim; they do not establish the function of each proposed alternative protein.
- [PMID:38688160, Bacterial synthase-dependent exopolysaccharide secretion: a focus on cellulose](https://pubmed.ncbi.nlm.nih.gov/38688160/) is a 2024 review of shared and system-specific secretion mechanisms. The current cache is abstract-only, so detailed mechanistic claims must be checked against accessible primary work.
- [PMID:41617292, Unraveling the biosynthesis and regulation mechanism of bacterial cellulose: Challenges and strategies toward industrial production](https://pubmed.ncbi.nlm.nih.gov/41617292/) reviews synthase-subunit diversity and regulation; currently abstract-only.
- [PMID:39319708, Research progress in bacterial cellulose synthase subunit diversity and fiber structure formation](https://pubmed.ncbi.nlm.nih.gov/39319708/) also addresses cross-strain subunit differences; currently abstract-only. Its abstract is useful for identifying the review's scope, not for attributing a particular protein assay.

The module's final boundary is still under review. The existing draft describes a Gram-negative BcsA/BcsB/BcsC synthase-export mechanism with optional BcsQ; its title is broader than that inventory. The audit must make the chosen mechanism and taxon context explicit while accounting for genuine alternatives, not silently restrict the biology to make the existing conjunction pass. BcsQ can be required within a particular type II system without being universal across bacterial cellulose synthesis.

## Primary mechanisms and strain identity

[PMID:23222542](https://pubmed.ncbi.nlm.nih.gov/23222542/) and [PMID:24704788](https://pubmed.ncbi.nlm.nih.gov/24704788/) establish BcsA/BcsB synthesis/translocation and c-di-GMP activation using Rhodobacter sphaeroides proteins. The first paper explicitly identifies the 2.4.1 genomic source. These are not KT2440 protein assays.

[PMID:31604608](https://pubmed.ncbi.nlm.nih.gov/31604608/) resolves a BcsC outer-membrane channel; the exact source strain and construct must be established before choosing its accession. [PMID:39242554](https://pubmed.ncbi.nlm.nih.gov/39242554/) supplies a more complete E. coli envelope mechanism, including BcsB/BcsC organization and cellulose modification. The specific transferase and cellulase roles must not be assigned to unrelated accessory components from co-occurrence alone.

[PMID:39394223](https://pubmed.ncbi.nlm.nih.gov/39394223/) is now available in full text after a normal forced refresh. It distinguishes native E. coli 1094 phenotype assays from recombinant complex production in a Δbcs BL21*(DE3) host. Expression host, protein source and reference accession are separate identities. Its BcsE/R/Q/F regulation can inform the type II implementation without becoming a universal requirement for every cellulose system.

## Research provenance and remaining work

The normal Falcon module-research command failed with HTTP 403 authentication error. No provider-branded report was fabricated; this file records manual research. The four original PSEPK genes are undergoing an annotation-reviewer reassessment. Expanded experimental exemplars, source-to-accession matches, taxon/architecture alternatives, step evidence, family verification and production-compiler coverage remain to be completed. The module is not yet audited or ready to merge.


## 2026-11-06: comparative literature and accession audit

Curated 13 references, including the 2015 architecture review (PMID:26077867), the 2024 secretion review (PMID:38688160; abstract-only), and the 2025 cyanobacterial review (PMID:40941819). All existing draft steps and connections now have primary evidence, and the BcsA function no longer cites GOA as evidence. The module remains DRAFT while architecture requirements are reconciled.

The 2015 review explicitly reports typeIII BcsAB systems without BcsC and typeIV cyanobacterial systems without BcsB. Neither the current three-component conjunction nor a universal PilZ switch can be assumed across all bacterial cellulose systems. The 2025 review's suggestion of HlyD/BcsW functional equivalence is not direct biochemical evidence. The 2018 RKN primary paper describes a proposed tripartite mechanism; it must not be represented as a reconstituted exporter.

Rhodobacter sphaeroides2.4.1 assayed BcsA/BcsB map to current Cereibacter CERS4 Q3J125/RSP_0333 and Q3J126/RSP_0332 by paper methods and PDBe SIFTS4HG6/4P00. E. coli BcsC6TZK maps to P37650. The exploratory6TZP lookup instead mapped to Bacillus oxalate decarboxylase and is rejected, not used as cellulose evidence. The 2024 BcsB/BcsC study includes a Rhodobacter/E. coli BcsA chimera and a TPR/BcsB fusion; their construct geometry is not assumed native in other taxa.

E. coli K12 requires accession-level distinctions: P37655 is the predicted242-residue BcsQ pseudogene fragment; P0DP92 represents the intact250-residue protein, including restored reading-frame evidence in AR3110. Neither an intact engineered record nor gene-family presence establishes native K12 pathway output. PMID18599830 examines csgD-overexpressing MG1655, whereas PMID24097954 examines W3110 repair; these conditions must remain separate.

The assayed RKN cyanobacterial synthase is E5RST0/Tvtll0007 (AB571479/BAJ61012.1), currently Thermostichus vulcanus THEVL. BP1 Q8DMV4 and its accessory homologs belong to a different strain/species record. The primary2011 study reports a BP1 phenotype difference; its cause is unresolved, so BP1 accessory homologs are comparators rather than proven positive route members.

Agrobacterium CelG is not an established outer-membrane pore. The primary2005 study reports cellulose overproduction in celG insertion mutants, and the current C58 sequence does not establish a signal peptide or membrane barrel. Gene reviews are resolving sequence/locus and strain differences before this component is assigned a mechanistic role.

Progress: six gene reviews complete (four original KT2440 plus two directly assayed CERS4 proteins); E. coli, Agrobacterium and cyanobacterial reviews continue. Falcon module and gene research requests returnedHTTP403, documented in operational logs; no provider report was fabricated.

Current official InterPro IPR018513 (family name: Cellulose synthase BcsB, bacterial) and Pfam PF03170 (first BcsB CBM domain) descriptions also retain outdated functional prose: the former calls BcsB catalytic/multi-TM and the latter assigns direct c-di-GMP binding. Their sequence signatures remain useful, but those function statements conflict with the primary BcsAB structures and must not become annotation evidence. Official API responses are preserved in the operational source audit pending integration.

The BcsA selector now intersects PTHR43867:SF2 with supported GO:0016760 activity rather than requiring IPR003919, which excluded authentic E5RST0. BcsB uses verified IPR018513 membership, covering assayed Q3J126 despite its absent PANTHER cross-reference. Rhodobacter, Agrobacterium and RKN exemplars have been added with exact frozen protein labels and strain/construct boundaries. Official InterPro/Pfam responses are preserved under the module source-analysis directory; their obsolete BcsB functional prose is explicitly excluded from the evidence argument. Architecture integration remains unfinished.


## 2026-11-06: architecture obligations and production-compiler checks

The model now separates common UDP-glucose polymerization from the envelope/assembly architecture. The sampled non-enterobacterial BcsB/BcsC implementation retains lineage-dependent accessory factors; the E. coli implementation explicitly requires intact BcsQ. TypeIII and cyanobacterial branches contain required unresolved annotons. These lack invented molecular-function or family identifiers and cannot be satisfied by candidate homology. This matters technically: a bare node carrying only a knowledge gap compiles to an empty, satisfied conjunction. The explicit unresolved annotons preserve a real mechanistic obligation. Native cellulose production in C58 and RKN is positive evidence; unresolved capacity is an abduction target, not a biological negative.

TypeI coverage adds P19449 BcsA from1306-3 and P37719 BcsD fromATCC53582/NQ5. The complete native BcsD sequence matches theATCC23769 crystal constructs after excluding tags. BcsD is represented as structural membership, without a directional BcsC-to-BcsD transport edge or invented MF.

Nineteen completed reviews preserve85seeded annotation payloads, including one inheritedNEW, and38rawfiles. Seven additionalNEW rows are separately counted. Seventeen production-compiler scenarios pass, including RKN and Rhodobacter selector coverage, required intactE.coliBcsQ, and rejection of polymerase-only or candidate-only closure of unknown export mechanisms. The checker and baseline live under the module source-analysis and analysis/module_audits directories. Five missing-core reviews are intentional: CelG, twoBP1accessorycomparators, nativeK12BcsQfragment, andBcsD.

Further literature search identified the directly characterized Streptomyces CslA/GlxA monoderm system (PMID38557137); its two gene reviews are being integrated before finalizing the broad bacterial scope. The retired1326CslAaccession has an exact-sequence currentTK24counterpart, while GlxA requires the experimentally supported extended645-residue model. The2024Sarcina mixed-linkageglucan paper also requires comparative treatment before using old cellulose-staining claims as specificity evidence.

## 2026-11-06 — monoderm integration and completed member panel

The panel now has 21 COMPLETE reviews, preserving 88 seeded annotation payloads (including one inherited NEW) and 42 raw source hashes. Eleven new proposals are distinguished from that inherited proposal. Five reviews intentionally assert no core function; six annotation claims remain UNDECIDED. The production compiler passes 23 reviewed-panel scenarios. This is a machinery-compatibility audit, not an exhaustive genome screen or a prediction of native expression.

PMID:38557137 supplies a distinct CslA–GlxA monoderm architecture. Exact source/construct bridges support transfer of catalytic capacity from 1326 CslA to sequence-identical TK24 CslA; native TK24 cellulose production is not asserted. Native glycan composition, direct c-di-GMP recognition and the role of GlxA redox chemistry in the complex remain open. PMID:38750617 documents Sarcina mixed-linkage glucan, while PMID:33264329 assays clostridial CcsZ hydrolase and models CcsA. Neither substitutes for a demonstrated cellulose-polymerase exemplar.

Seventeen module references are curated, including three comparative reviews. The module schema and biological validation pass, with five advisory binding/core conformance warnings: retained c-di-GMP-binding annotations support those switches, while the gene cores synthesize their coupled polymerase activity rather than repeating every binding event. CelG and GlxA descriptors intentionally have no unverified family identifier. TypeIII and cyanobacterial unknown envelope roles remain explicit abduction targets. The single repository-wide validation is live; no full-pass claim is made.


## 2026-11-06 — terminal validation and current-main integration

The full 10,553-review validation completed with exit 1 solely for 19 reference-quote errors in 17 unrelated yeast reviews. Their reviews, two cited sources and validation inputs are byte-identical to the audit base; the exact proof is committed with the audit. Schema and ontology checks pass; best practices report zero errors and 27,998 advisory warnings; all 54 PMID-bearing pathway files pass. Current main ce73640bac adds the independent ERG1 review and source; integration preserves all 212 audit files and four excluded dirty cache files byte-for-byte. The expanded audit requires fresh PR review and CI and is not covered by the old four-file approval.


Final independent biological review found no blocker at the declared reviewed-panel scope. The sampled generic BcsB/BcsC branch now explicitly names Pseudomonas, Cereibacter and Komagataeibacter contexts. The 25-case production-compiler replay includes two external-oracle contract controls: family matches alone admit an E. coli BC bypass; enforcing the declared context rejects it. This is not a claim that the compiler itself enforces taxa or that BcsQ is dispensable throughout those genera. Streptomyces positive capacity remains limited to the characterized complex and does not establish native extracellular cellulose production or direct membrane-translocation evidence.

## PR2143 round17: bacterial process specificity

QuickGO definitions checked on 2026-11-06 establish GO:0090540 as an is_a subtype of GO:0030244 with bacterial context. The parent and child share the cellulose chemistry criteria. Native output, intact-cell synthesis, crystallinity and fibrils are independent evidence questions, not extra requirements introduced by the bacterial subtype.

All already-asserted generic cellulose process concepts, replacements and cores are refined consistently across the reviewed bacterial panel. CERS4 purified-complex capacity remains distinct from native output. Restore PSEPK BcsA RuleBase evidence and explicit ISS donor; retain the current official IPR044846 label with scoped metadata provenance. The five catalytic donor/product checks require GO:0090540 in reviewed functions and core processes. The immutable 88-row ledger comprises 87 unchanged machine payloads plus one exactly archived/refined historical PP_2634 proposal; the 13 additional NEW rows remain separate and their count is unchanged. No CslA/GlxA process proposal is manufactured.
