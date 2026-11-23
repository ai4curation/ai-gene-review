# FtsI/PBP3 manual review notes

## 2026-11-06 catalytic and annotation reassessment

All 48 original machine annotation payloads, raw UniProt/GOA files and the inherited Falcon report are preserved. No NEW annotation was introduced. The inherited provider is background research, not a substitute for claim-linked primary evidence. `just paint-losses ECOLI ftsI` reported no IRD/IKR loss on this lineage.

FtsI P0AD68 represents E. coli K-12 PBP3, a class-B penicillin-binding protein with an N-terminal membrane anchor and a periplasmic catalytic domain. PMID:2677607 uses beta-lactamase fusions and side-specific proteolysis to map its topology. PMID:9603865 localizes FtsI to the septum, dependent on earlier FtsZ/FtsA assembly. PMID:3531167 studies intact and ether-permeabilized cells, associating PBP3 activity with increased cross-linked, tripeptide-containing septal peptidoglycan. These cellular experiments support the physiological cross-linking role; they are not a purified natural-substrate reconstitution.

## Transfer, hydrolysis and polymerization are different claims

The full primary PMID:9324244 author postprint was retrieved from the official ORBi repository; the normal publication cache remains abstract-only. A small verified excerpt and scoped methods summary are in `ftsI-source-analysis/catalytic-specificity.md`, with URL, PDF hash and extraction provenance alongside it. The protein assayed there was the soluble, anchor-free G57–V577 construct. Its beta-lactam acylation profile supports folding, but does not establish equivalence to the intact activated divisome under all conditions.

The construct has no detectable activity on the acetylated Lys-D-Ala-D-Ala peptide specified by GO:0009002, but it hydrolyzes synthetic thioesters and transfers their acyl groups to D-alanine or a peptidoglycan-related tetrapeptide. HPLC distinguishes the hydrolysis and aminolysis products. The current GO:0009002 definition includes water as acceptor, so it is not merely the acylation half-reaction of D,D-transpeptidation. The electronic carboxypeptidase/peptidase mappings are corrected to the shared proposed **serine-type peptidoglycan D,D-transpeptidase activity**; original IDs remain intact. The proposed definition allows a stem or attached peptide-bridge amino group, rather than requiring meso-DAP in every species.

Conversely, a blanket assertion that FtsI lacks hydrolase activity would contradict the same primary paper: “The truncated PBP3 functions as a thiolesterase.” Its generic hydrolase row is refined to GO:0016790 thiolester hydrolase activity, a verified descendant, explicitly as an assayed model-substrate capacity outside the physiological core. This does not establish native thioester metabolism. Proteolysis refers to hydrolysis of proteins into smaller products and is not established by cross-link formation between peptidoglycan stems or synthetic-thioester hydrolysis.

The full PMID:9324244 study also finds no glycan polymerization from radiolabeled E. coli lipid II in two assay conditions with active PBP1b controls. The construct limitation is recorded. The full 1981 PMID:7030331 paper remained inaccessible after primary-publisher and archive attempts; therefore no purification error, specific contamination or wrong-gene attribution is asserted. Its historical bifunctional interpretation is contradicted independently by the later targeted assay, class-B domain organization, UniProt's explicit caution and the FtsW polymerase assignment. All three FtsI glycosyltransferase rows receive the same REMOVE decision on that combined evidence. PMID:6450748 measured murein incorporation in thermosensitive division mutants after specific PBP3 inhibition; this readout does not isolate glycan-polymerization chemistry from peptide cross-linking.

## Morphogenesis, antibiotic binding and interactions

GO:0008360 is not restricted to lateral rod-shape maintenance. PMID:3049550 ties a PBP3 substitution and partial inhibition to pointed polar caps and altered local surface synthesis. FtsI itself cross-links the septal material, so this is direct morphogenetic work and supports ACCEPT. Specific penicillin binding remains experimentally valid but is kept outside the physiological core as an antibiotic-target property; it does not imply resistance or detoxification. The existing response-to-xenobiotic row is retained as a peripheral pharmacological response, not a stress-defense mechanism.

Full PMID:18978050 directly identifies an FtsI segment in the FtsL two-hybrid screen and tests FtsI–YmgF association. PMID:20847002 establishes the FtsW–FtsI subcomplex; PMID:20497333 identifies FtsN proximity to both. These contacts support divisome organization, while the bare protein-binding term remains uninformative under repository policy. Six original rows with unresolved exact target-partner/source scope are UNDECIDED; a title about another protein is not treated as proof of misattribution. Current full texts or supplements would be needed to adjudicate those edges. No interaction assay alone is promoted to a new catalytic or adaptor activity.

Generic cell division is refined to the already-present FtsZ-dependent cytokinesis descendant. Cell wall organization is retained; the current ancestry snapshot does not make peptidoglycan biosynthesis its descendant, so no lateral refinement is disguised as specificity. The single physiological core couples the proposed precise transpeptidase activity to septal wall synthesis and division-site localization with actual quotes, replacing the earlier hydrolytic proxy and unsupported placeholder text.

Identity limit: PMID:6450748 explicitly assays E. coli BUG6 and JE10730 thermosensitive division mutants, the latter with thermolabile PBP3. PMID:9324244 assays the named soluble E. coli construct rather than a sequence-verified, full-length P0AD68 preparation. PMID:3049550 studies the pbpBr1 substitution phenotype. These gene-specific studies support K-12 FtsI biology, but their construct/strain-specific numerical outcomes are not silently assigned to an unmodified reference strain.


## PR6123 round-1 follow-up (2026-11-06)

- activation boundary documented without unsupported MF.
- remove title-only evidence from generic-binding policy row.
- specific IPR037532 wrong-term source defect.
- standardized DD proposal definition and verified parent.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
