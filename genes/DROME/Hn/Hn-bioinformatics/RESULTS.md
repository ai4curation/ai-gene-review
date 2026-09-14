# Hn exact-isoform sequence comparison

E8NH57 is the native 178-residue Hn-PD protein (FlyBase FBpp0306708), matching residues 275–452 of reviewed 452-residue Hn/P17276 without substitutions. Iron-ligand positions His284, His289 and Glu329 map to target His10, His15 and Glu55. The regulatory ACT domain is entirely absent; the missing N-terminal 274 residues also remove much of the hydroxylase catalytic scaffold. Structural studies of mammalian PAH characterize active constructs substantially larger than this fragment; retention of the metal ligands alone is not evidence of a complete catalytic pocket. The human PAH mapping below resolves missing substrate/cofactor architecture; no direct assay of native PD was identified. 

## Reproducibility

Global BLOSUM62 alignment, gap-open -10, gap-extension -0.5, Biopython 1.85. Inputs, alignment and JSON results are retained; run `just` in this directory. Source feature positions are read from comparator JSON. A separate reference self-alignment verifies indexing and full sequence recovery; the generic script was also run on independent fly gene proteins. The self-control is a computational check, not biological validation. Prediction-time input sequence is not supplied by the release API.

- [x] No biological results or conclusions hardcoded in analysis.
- [x] Same algorithm run on other protein inputs.
- [x] Analysis and control completed successfully.
- [x] Direct inputs/results retained.
- [x] Sequence provenance and inference limitations stated.

## Human PAH structural-site mapping

The human PAH P00439 catalytic domain (118–424; PMID:10694386) maps completely to full-length Hn residues 117–423, but only 149 of 307 positions remain in PD. The human substrate-responsive loop 131–155 (PMID:12126628), pterin-binding loop 245–250 and cofactor-stacking Phe254 (PMID:10694386) are absent in PD. The full-length Hn control preserves these regions at 130–154, 244–249 and Phe253. Human Glu286 maps to retained PD Glu11. Thus metal-coordinating residues remain while essential substrate/cofactor architecture is missing. This contradicts the conventional pteridine-dependent hydroxylase reaction by PD, beyond a generic short-length concern. It does not establish absence of metal binding or every possible noncatalytic process role.

The literature positions are explicit inputs in `human-literature-sites.json`, not hardcoded outputs. `just human` regenerates target and full-length positive-control mappings from the downloaded human source record. The cited abstracts were read: PMID:10694386 describes catalytic-domain structure and site-specific mutagenesis confirming Phe254/Glu286 contributions to cofactor positioning and catalysis; PMID:12126628 describes substrate-dependent movement of loop 131–155.
