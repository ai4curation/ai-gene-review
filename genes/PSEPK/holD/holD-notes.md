# holD / PP_0696 manual review — 2026-11-06

Standard `just fetch-gene PSEPK holD --uniprot-id Q88Q02` seeded zero GOA rows. The pristine document/raw hashes were frozen in pseudomonas-new-members-baseline.json before editing. Default Falcon was attempted and failed HTTP403; no provider content was fabricated.

The current UniProt label Energy transducer TonB is a ProtNLM prediction and is contradicted by primary source mapping. PMID21955458 explicitly cloned KT2440 holC and holD. Its official Additional file9 forward/reversepsi primers map uniquely to PP_0696, not PP_0978. See ../holC/holC-source-analysis for source PDF, unmodified extraction, genomic coordinates, corrected-start calculation and executable check. The older291-residue protein matches the official sequence. The corrected TTG native start predicts261 residues; the GST expression insert begins at the following CTG codon and covers database residues32–291 (260native residues). GST was cleaved during purification. Do not claim the full older291-residue protein or its upstream30-residue extension was assayed.

[PMID:21955458] directly measures low-salt ssDNA binding by KT2440chi–psi. Attribution to psi comes from chimeric and deletion experiments on P. aeruginosa; complex-level qualifier contributes_to is therefore retained for the KT2440 binding row. Its in vivo importance remains a question, not a second conserved core assertion. [PMID:16210315] discovers endogenous P. aeruginosa psi and demonstrates stimulation of the minimal replicase. [PMID:17210572] dissects E. coli psi stabilization of the ATP-induced loader state. These comparative data support the loader-contribution core, explicitly distinguished from direct KT2440 chemistry.

Three NEW rows: ISS contributes_to clamp loader; IDA contributes_to ssDNA binding of the complex; IC DNA replication. The BP is direct structural machinery participation. Current QuickGO comparator queries returned5 replication annotations each for E. coli HolA/P28630, HolB/P28631 and HolC/P28905. GO0006260 parent check and empty Q88Q02 GO-CAM-index lookup found no convention conflict or redundant proposed BP. No transporter, TonB, origin-firing-regulation, nuclease or polymerase activity is asserted.

No PANTHER/InterPro membership was present in the frozen target record; do not invent a family identifier. Use a descriptive divergent pseudomonad psi family with the actual reviewed gene and the explicit sequence/start limitation.


## PR #6117 round-1 follow-up (2026-11-06)

- Add structured WRONG_START_SITE with reviewed_segment 32-291 and a source correction query for the 291-residue UniProt model.
- Distinguish predicted native positions 31–291 from the assayed initiator-free insert 32–291; retain inherited NEW GO:0006260 and refine the core process only.

All historical annotation payloads, inherited NEW proposals, and frozen raw/provider files are preserved. Source confidence distinguishes direct target assays from comparative Pseudomonas evidence. No publication cache was refreshed.
