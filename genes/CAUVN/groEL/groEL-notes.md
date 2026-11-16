# groEL evidence notes

## Evidence and identity audit — 2026-11-07

Primary source: PMID:30482828, full cached article, Figure 3 and Methods, and official supplementary Table S2/Text S1. Table S2 identifies JN17 as CB15N and the Caulobacter expression constructs in BL21. The frozen UniProt records explicitly equate strain NA1000 with CB15N (taxon 565050); this is not a transfer from the separate CB15 reference proteome. Recombinant BL21 is the expression host, not the biological origin of the proteins. Text S1 specifies untagged CcCnoX and CcGroEL and C-terminally His-tagged CcGroES. Supplement provenance and original PDF hashes are in `modules/bacterial_groel_groes_chaperonin_folding-source-analysis/PMID30482828-supplement-provenance.json`; no source cache was edited.

The main study uses Caulobacter GroEL14/ES7 and Mg-ATP to recover activity of chemically unfolded citrate synthase preserved by CnoX [PMID:30482828, “In contrast, addition of GroEL/ES or DnaK/J/GrpE led to ∼60% or ∼30% recovery of initial CS activity, respectively”]. This is positive biochemical cooperation and client recovery. The activity readout is not a direct client-transfer measurement or a stable CnoX–GroEL binding assay. The article itself calls for further interaction characterization. No such interaction or universal CnoX mechanism is inferred here.

Current QuickGO definitions were fetched on 2026-11-07 and retained in `analysis/module_audits/bacterial_groel_groes_chaperonin_folding/caulobacter-ontology.json`. GO:0044183 includes binding a protein-containing complex to assist folding; GO:0140662 adds ATP-hydrolysis-driven folding. GO:0051082 is obsolete. GO:0140309 is an unfolded-protein **carrier** that escorts a client to an acceptor or location; general holdase activity without resolved escort is represented by the established general holdase NTR, not a fabricated GO id.

Actual `just deep-research CAUVN groEL --provider falcon` attempted for each of the three records, but each returned 403 Failed to authenticate. No provider report was produced or invented. Manual primary-source research and this journal document the fallback. Logs are `.cache/module-audit-logs/groel-20261107/caulobacter-groEL-falcon.log`.

`just paint-losses CAUVN groEL` ran. Each accession is absent as a leaf in the available family tree (PTHR45633 GroEL, PTHR10772 GroES, PTHR45663 CnoX); the output explicitly says “losses not checked.” Its final generic “No IRD or IKR” message is not evidence that the lineage lacks losses. All 16 seeded rows are IEA, with no IBA rows. No fabricated PAINT-loss records are added.

All ordered seeded annotation payloads remain unchanged. Review decisions, core functions, supporting references, and notes are authored separately. No NEW GO annotation rows are added.

Identity: B8H163 = CCNA_00721; the frozen reviewed record identifies groEL/groL/mopA in NA1000/CB15N, 547 aa, with curated HAMAP MF_00600 and GroEL domain architecture. The study names the Caulobacter groEL construct without a UniProt accession; this is a same-strain gene/locus attribution, not a resequenced clone identity claim. Old sequence conflicts recorded against the 1996 submission are left unchanged and are not silently equated to the experimental clone.

Core ATP-dependent folding/refolding is supported by primary system reconstitution and curated family mechanism. The ATP-binding sites in the frozen record are HAMAP inference rather than a binding assay. Cytoplasm is retained at the supported granularity. Broad GO:0044183 is MODIFY to the existing ATP-dependent descendant GO:0140662. Protein folding is retained as physiological folding is not limited to the measured stress-recovery assay.

## Completion status — 2026-11-07

Promoted to COMPLETE after coordinator review: every seeded annotation has a substantive evidence-backed judgment. UNDECIDED is a completed adjudication of unresolved target-specific evidence, not a pending review. The two complex-core warnings on GroEL/GroES are documented advisory annotation-coverage notices and do not indicate incomplete scientific assessment. No scientific claim or annotation payload changed in this status update.
