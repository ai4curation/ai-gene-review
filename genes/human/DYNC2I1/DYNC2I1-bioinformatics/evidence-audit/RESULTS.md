# DYNC2I1 evidence-audit results

The saved-input replay and comparison passed. The archive contains 34 members (15,147,135 uncompressed bytes; 2,653,360 archive bytes). These are measured file sizes, not downloaded-size estimates.

| Computation | Executed result |
|---|---|
| PANTHER tree and alignment | 49 nodes and 49 sequences; Q8WVS4 leaf PTN002488191 matches the official 1,066-residue sequence exactly. |
| Literal PAINT joins | All seven inherited IBA assertions join to matching IBD terms at PTN008562642 on the actual target path. Human target descendant evidence is legitimate grounding, not circularity. |
| IntAct | 61 raw records; seven source-pair assertions select seven records in total. Three source pairs have no match in this snapshot and remain assessed from their primary evidence. |
| Sequence identity | All 14 compared participant ROGIDs match the corresponding saved official sequences. |
| Original AP-MS network | One DYNC2I1-incident edge, also the selected DYNC2I1-bait to DYNC2I2-prey edge, identifier 556070. Complete node attributes retain bait direction. |
| Reactome | Six reaction roots trace through twelve paths to Q8WVS4 entities covering residues 1–1066 in cilium or ciliary tip. These are twelve model paths, not twelve experiments. |
| Typed ontology | Ciliary base and ciliary tip both descend from cilium and neither descends from the other. Cilium assembly and intraciliary retrograde transport are also nonredundant under the queried `is_a`/`part_of` relations. |
| Alternate parser input | Mouse Q8C761 independently matches its 999-residue official sequence in the same tree/alignment. No human functional claim is inferred from that parser check. |

Matched NUDC associations support a chaperone-partner class when combined with the separate purified-NUDC experiment in PMID:21530541. They do not demonstrate chaperone activity of DYNC2I1. Light-chain and intermediate-chain associations are distinguished by the literal partner identities. The structural motor contribution belongs to the assembled dynein-2 complex; this audit does not assign autonomous ATPase activity to the intermediate chain.

All raw record counts, selected identities, graph paths and ontology results are recomputed by `replay.py`; biological judgments remain in the review and source guide. The script was executed both to generate `results.json` and independently with `--check`, then exercised with the mouse target.
