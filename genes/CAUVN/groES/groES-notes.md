# groES evidence notes

## Evidence and identity audit — 2026-11-07

Primary source: PMID:30482828, full cached article, Figure 3 and Methods, and official supplementary Table S2/Text S1. Table S2 identifies JN17 as CB15N and the Caulobacter expression constructs in BL21. The frozen UniProt records explicitly equate strain NA1000 with CB15N (taxon 565050); this is not a transfer from the separate CB15 reference proteome. Recombinant BL21 is the expression host, not the biological origin of the proteins. Text S1 specifies untagged CcCnoX and CcGroEL and C-terminally His-tagged CcGroES. Supplement provenance and original PDF hashes are in `modules/bacterial_groel_groes_chaperonin_folding-source-analysis/PMID30482828-supplement-provenance.json`; no source cache was edited.

The main study uses Caulobacter GroEL14/ES7 and Mg-ATP to recover activity of chemically unfolded citrate synthase preserved by CnoX [PMID:30482828, “In contrast, addition of GroEL/ES or DnaK/J/GrpE led to ∼60% or ∼30% recovery of initial CS activity, respectively”]. This is positive biochemical cooperation and client recovery. The activity readout is not a direct client-transfer measurement or a stable CnoX–GroEL binding assay. The article itself calls for further interaction characterization. No such interaction or universal CnoX mechanism is inferred here.

Current QuickGO definitions were fetched on 2026-11-07 and retained in `analysis/module_audits/bacterial_groel_groes_chaperonin_folding/caulobacter-ontology.json`. GO:0044183 includes binding a protein-containing complex to assist folding; GO:0140662 adds ATP-hydrolysis-driven folding. GO:0051082 is obsolete. GO:0140309 is an unfolded-protein **carrier** that escorts a client to an acceptor or location; general holdase activity without resolved escort is represented by the established general holdase NTR, not a fabricated GO id.

Actual `just deep-research CAUVN groES --provider falcon` attempted for each of the three records, but each returned 403 Failed to authenticate. No provider report was produced or invented. Manual primary-source research and this journal document the fallback. Logs are `.cache/module-audit-logs/groel-20261107/caulobacter-groES-falcon.log`.

`just paint-losses CAUVN groES` ran. Each accession is absent as a leaf in the available family tree (PTHR45633 GroEL, PTHR10772 GroES, PTHR45663 CnoX); the output explicitly says “losses not checked.” Its final generic “No IRD or IKR” message is not evidence that the lineage lacks losses. All 16 seeded rows are IEA, with no IBA rows. No fabricated PAINT-loss records are added.

All ordered seeded annotation payloads remain unchanged. Review decisions, core functions, supporting references, and notes are authored separately. No NEW GO annotation rows are added.

Identity: B8H164 = CCNA_00722; the frozen reviewed record identifies groES/groS/mopB in NA1000/CB15N, 96 aa, with curated HAMAP MF_00580 and GroES architecture. The study names the same-strain groES construct without an accession; clone sequence identity is not independently demonstrated.

GroES is a structural cofactor that binds GroEL and caps its chamber. GO:0044183 is accepted according to its current definition, which includes binding a protein-containing complex to assist folding. Core GO:0051087 records the specific binding activity, with contributes_to GO:0140662; no intrinsic GroES ATPase is asserted.

ATP binding is UNDECIDED. The E. coli negative experiment PMID:7867782 reports “no interaction between GroES and nucleotides could be detected,” using calorimetry and equilibrium binding. It cautions against transferring ATP binding from the whole complex or nonspecific photolabeling but is not a negative assay on Caulobacter. Metal binding is likewise UNDECIDED: no target-specific coordinating site or binding experiment was established. Lack of Cys/His in this sequence is **not** disproof, because acidic residues can coordinate metals. The family-level TreeGrafter node is not a target assay. These judgments preserve uncertainty rather than inventing a demonstrated source-mapping defect.

## Completion status — 2026-11-07

Promoted to COMPLETE after coordinator review: every seeded annotation has a substantive evidence-backed judgment. UNDECIDED is a completed adjudication of unresolved target-specific evidence, not a pending review. The two complex-core warnings on GroEL/GroES are documented advisory annotation-coverage notices and do not indicate incomplete scientific assessment. No scientific claim or annotation payload changed in this status update.
