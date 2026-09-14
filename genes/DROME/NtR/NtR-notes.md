# NtR evidence notes

Q9W288 is the native 585-residue PA product of [FBgn0029147](https://flybase.org/reports/FBgn0029147), not the 578-residue PB product A0A0B4K8A6. Its NP_651958 mapping and the original 15 GOA rows are preserved. The contributes_to qualifier on the specific acetylcholine channel annotation is retained; no monomeric channel activity is implied.

The [family evidence report](NtR-family-evidence.md) includes the primary Matthews et al. 2018 tree, [PMID:30429615](https://doi.org/10.1038/s41586-018-0692-z), Extended Data Figure 10d. NtR is outside the shaded nicotinic receptor groups, consistent with FlyBase's “UNCLASSIFIED LIGAND-GATED ION CHANNEL SUBUNITS”. This supports broad channel function but leaves the phylogenetic origin/retention of acetylcholine and calcium specificity unresolved. It is not a rejection based merely on absent target experiments or donor count.

The ancillary ProtNLM protein name highlights a farnesoic-acid O-methyltransferase domain. The exact sequence has this N-terminal domain match and a separate neuronal-channel ligand-binding region; the label does not prove methyltransferase activity, substrate identity, or that the channel annotation is wrong. The raw original name, score, donor and location metadata remain in NtR-predictions-source.json.

Falcon completed in 443.74 seconds and found no direct NtR ligand assay, but missed the target-containing published channel phylogeny and described even a generic channel role as unsupported. The primary family tree plus target architecture and current FlyBase classification support the broad conserved-function inference. ProtNLM GO:0005230 is CNN; specific cholinergic, calcium and derived synaptic calls remain UNDECIDED pending evidence about this distinct branch.
