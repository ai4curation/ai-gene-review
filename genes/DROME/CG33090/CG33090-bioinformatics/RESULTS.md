# CG33090 native isoform and catalytic-site comparison

The benchmark protein X2JE45 is the native 799-residue PC isoform, not the 948-residue PB protein Q7KT91. PC has a distinct 28-residue N-terminus followed by a 771-residue sequence identical to PB residues 178–948. Thus PB residues 1–177 are replaced by PC residues 1–28; this is not a simple catalytic-site substitution.

Both global and local MAFFT alignments map human GBA2 Glu527 to PC Glu362 and Asp677 to PC Asp575 (PB Glu511 and Asp724). The catalytic nucleophile and acid/base residue types are retained. These site identities support GH116 catalytic potential but do not establish that the shortened native isoform is active.

The alteration overlaps the beginning of PB's annotated GH116 N-terminal domain (132–445), while the shared C-terminal sequence includes its catalytic domain (505–937). PB position 132 aligns to a gap in PC; PB positions 445, 505 and 937 map to PC positions 296, 356 and 788. N-terminal-domain integrity is therefore a specific uncertainty distinct from the retained active-site chemistry.

## Evidence and interpretation

Human GBA2 Glu527/Asp677 were experimentally identified by mutagenesis, substrate hydrolysis, azide rescue and activity-based labeling in [Kallemeijn et al. 2014, PMID:25344605](https://pmc.ncbi.nlm.nih.gov/articles/PMC4271221/), [DOI:10.1074/jbc.M114.593376](https://doi.org/10.1074/jbc.M114.593376). The publication cache has its abstract; the site-specific results were verified in the primary full-text search result. Neither experiment assayed Drosophila PC.

[PMID:33261081](https://pmc.ncbi.nlm.nih.gov/articles/PMC7761373/), [DOI:10.3390/metabo10120488](https://doi.org/10.3390/metabo10120488), is cached with full text. Expressed human alternative isoforms, including N-terminal-domain variants, showed background-like glucoside hydrolysis despite detectable protein; only isoform 1 changed glucosylceramide/ceramide levels substantially. This demonstrates that retaining a nominal catalytic domain is insufficient across GBA2 isoforms. The human changes are not identical to fly PC and do not prove PC inactive.

The exact PC hydrolase claim is consequently unresolved pending an isoform-resolved activity or convincing fold analysis. The conserved long C-terminal sequence argues against declaring a pseudoenzyme solely from this comparison. This work provides no evidence of a wrong input sequence: PC is a native annotated protein.

## Reproduction and controls

Run `just` in this directory. Dependencies are Biopython 1.85 (locked with uv) and MAFFT 7.526. The workflow extracts immutable benchmark UniProt JSON and separately downloaded reference Swiss-Prot sequences, computes independent G-INS-i (`--globalpair --maxiterate 1000`) and L-INS-i (`--localpair --maxiterate 1000`) alignments, maps supplied reference sites, and independently computes exact common suffixes without alignment. Input FASTA, alignment files/logs, hashes and numeric JSON results are in `inputs/` and `outputs/`.

Inputs: frozen X2JE45 record in `../CG33090-uniprot-source.json`; [Q7KT91 PB](https://rest.uniprot.org/uniprotkb/Q7KT91.txt) and [Q9HCG7 human GBA2](https://rest.uniprot.org/uniprotkb/Q9HCG7.txt), preserved as adjacent `CG33090-reference-*-uniprot.txt` files. Native isoform assignment is independently recorded in the local FlyBase report for [FBgn0028916](https://flybase.org/reports/FBgn0028916).

- [x] Scripts accept input/output paths, reference IDs and positions as arguments; biological conclusions are confined to this report.
- [x] The mapping script was exercised with the different human reference and the fly PB reference; the human self-map is exact, while the PB comparison checks a native alternate protein.
- [x] Both alignment strategies completed and agree on both catalytic-site mappings.
- [x] Raw inputs, computed outputs, logs and dependency lock are retained.
- [x] Interpretation distinguishes observed sequence differences, inferred structural risk, and unmeasured activity.
