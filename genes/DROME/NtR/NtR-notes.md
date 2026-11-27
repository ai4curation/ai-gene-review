# NtR evidence notes

Q9W288 is the native 585-residue PA product of [FBgn0029147](https://flybase.org/reports/FBgn0029147), not the 578-residue PB product A0A0B4K8A6. Its NP_651958 mapping and the original 15 GOA rows are preserved. The contributes_to qualifier on the specific acetylcholine channel annotation is retained; no monomeric channel activity is implied.

The [family evidence report](NtR-family-evidence.md) includes the primary Matthews et al. 2018 tree, [PMID:30429615](https://doi.org/10.1038/s41586-018-0692-z), Extended Data Figure 10d. NtR is outside the shaded nicotinic receptor groups, consistent with FlyBase's “UNCLASSIFIED LIGAND-GATED ION CHANNEL SUBUNITS”. This supports broad channel function but leaves the phylogenetic origin/retention of acetylcholine and calcium specificity unresolved. It is not a rejection based merely on absent target experiments or donor count.

The ancillary ProtNLM protein name highlights a farnesoic-acid O-methyltransferase domain. The exact sequence has this N-terminal domain match and a separate neuronal-channel ligand-binding region; the label does not prove methyltransferase activity, substrate identity, or that the channel annotation is wrong. The raw original name, score, donor and location metadata remain in NtR-predictions-source.json.

Falcon completed in 443.74 seconds and found no direct NtR ligand assay, but missed the target-containing published channel phylogeny and described even a generic channel role as unsupported. The primary family tree plus target architecture and current FlyBase classification support the broad conserved-function inference. ProtNLM GO:0005230 is CNN; specific cholinergic, calcium and derived synaptic calls remain UNDECIDED pending evidence about this distinct branch.


## Full-gene re-review, 2026-09-20

All 15 annotations were assessed. Ion transport and membrane MODIFY decisions were restored to ACCEPT: broad true ancestors remain valid. The nine specific ligand/ion/synaptic rows remain UNDECIDED, grounded in the separately branching Dmel NTR lineage, not absence of a native assay alone. The original Matthews2018 Extended Data10d image was inspected directly; Dmel NTR lies outside both shaded nAChR groups. The complete Falcon report was incorporated with its limitation: it missed this primary family evidence and therefore undercalled broad channel function. Root manages the new focused ligand/selectivity/synaptic adjudication. No source rows or isoform mappings changed.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9W288 is the 585-residue NtR-PA product of FBgn0029147 (CG6698), the FlyBase/UniProt canonical gene-model product (the alternative PB product is A0A0B4K8A6, 578 aa). It is not a fragment; the full architecture (signal peptide 1-27, Methyltransf_FA-like domain 51-197, Neur_chan_LBD 213-429, four Phobius TM segments 432-582) is present.

PANTHER placement: the UniProt cross-reference still gives PTHR36695:SF12 (AGAP008648-PA), but the PANTHER 19.0 classification files (.cache/panther/PTHR19.0_fruit_fly) place Q9W288 in PTHR18945:SF430 "ACETYLCHOLINE RECEPTOR SUBUNIT ALPHA-LIKE 2-RELATED", whose only other model-organism member is Dmel nAChRalpha2 (P17644). All IBA rows come from PTHR18945 PAINT nodes (PTN001054635 plasma membrane; PTN000434994 ion transport, Ca2+ transport, membrane potential; PTN000435923 nAChR complex, Bilateria; PTN001054960 cholinergic transmission; PTN001825467 ACh-gated cation channel, seeded by Dalpha1/2/5). interpro/panther/PTHR36695 review already records this conflict as unresolved; I agree.

Independent tree: re-inspected Matthews et al. 2018 Extended Data Fig. 10d (PMID:30429615). Dmel NTR is a long unpaired branch sister to the whole nAChR clade (core plus divergent groups), with no Aedes counterpart in the tree. So the PANTHER subfamily placement next to Dalpha2 is not reproduced by an ML tree.

New sequence analysis (NtR-bioinformatics/compare_motifs_rereview.py, RESULTS-rereview.md): Cys-loop disulfide retained (C337-C351) but FPFD motif replaced by NWPSE; loop-C vicinal Cys of alpha subunits (Dalpha2 C243-C244) align to NtR M412-M413, and NtR has no Cys pair after the signal peptide; M2 GEK intermediate ring (Dalpha2 G290-E291-K292) aligns to NtR R459-S460-S461. About 15% identity to Dalpha2. Residue claims recorded in propagation_review and verified by gene_residue_claims (27 pass).

Decisions: broad Cys-loop superfamily terms (GO:0005230, GO:0005886, GO:0034220) ACCEPT; GO:0006811 and GO:0016020 MODIFY to the specific terms already on the gene (GO:0034220, GO:0005886); GO:0042391 KEEP_AS_NON_CORE; the acetylcholine/calcium/cholinergic IBAs (GO:0005892, GO:0022848 contributes_to, GO:0006816, GO:0007271) and their GO_REF:0000108 synaptic derivatives (GO:0045202, GO:0098794, GO:0060078, GO:0060079, GO:0099565) changed from UNDECIDED to MARK_AS_OVER_ANNOTATED, because target-specific divergence (independent tree plus loss of ACh-binding and selectivity hallmarks) now argues against the node placement rather than merely leaving it unverified. Not REMOVE: heteromeric assembly with nAChR subunits is not excluded, and no experiment tests it.

Literature: no NtR-specific functional paper (Falcon and earlier searches agree). FlyBase RNAi (GD2144) with several GAL4 drivers including elav is viable; no informative phenotype. No human ortholog in DIOPT.

Relative for next review: Dmel nAChRalpha2 (P17644, FBgn0000039), paralog in the same PANTHER 19.0 subfamily SF430 and a seed of the PTN001825467 node; no review exists in genes/DROME. Modules: none found for nAChR/cholinergic channels.
