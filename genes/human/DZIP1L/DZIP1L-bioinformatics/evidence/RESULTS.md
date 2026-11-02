# DZIP1L source-identity results

The raw MITAB snapshot contains 38 records. Thirty-five records match 14 imported interaction assertions, and all 70 participant ROGIDs match their official reference sequences. The SEPTIN2 assertion is independently supported by its primary paper; absence from this particular MITAB snapshot is not negative evidence. Five matching CEP76 records and ten participant checks are recovered when the same parser is run with CEP76 as its target.

The partner and feature distinctions matter. CBY2 Q8NA61 and its 412-residue product Q8NA61-2 are not CBY1. The PRPF40A 716–930, LRRN4 338–740 and AMOTL2 314–779 binding-associated regions are on those partners, not on DZIP1L. DZIP1L's listed variants at 643, 625, 595 and 88 are recorded as having no effect on binding; they are not negative interactions. The CBY1 AP-MS record is a tagged-bait coassociation with spoke expansion, whereas the screen records use the stated two-hybrid methods. Stable IntAct identifiers and exact method strings are in the raw-derived output and source guide.

The independently curated CEP76 and CBY1 centriolar/basal-body component evidence supports cytoskeletal-protein partner classification. Neither has to form the cytoskeletal polymer itself. The AMOTL2 record documents coordination of signaling proteins and supports a scaffold-binding classification; its MAGI1/CDH5 statement is separately marked by similarity. These class refinements do not establish a DZIP1L centriole-duplication, transcriptional, ubiquitin-ligase or Hippo-pathway activity. The AMOTL2 fragment association does not demonstrate that the fragment itself carries all full-length scaffold functions.

The family tree has 284 nodes. DZIP1L PTN002502205 has a 767-residue ungapped alignment identical to the official displayed sequence. Each of the three IBA rows joins to one literal IBD on the target path: cytoplasm at PTN001469871, basal body and cilium assembly at PTN000948208. Current donor records are retained with their actual evidence codes; propagated records are not called experiments, and the target's own direct annotations are valid descendant evidence. ARBA00027837's first condition set matches the target's IPR013087, IPR032714 and Chordata membership.

HPA's individual-location summary labels basal body supported. Microtubules, cytokinetic bridge, mitotic spindle, primary cilium, nucleoplasm and cytosol are uncertain. Overall supported reliability cannot be assigned to all these locations. No image pixels were interpreted.

Both official natural sequences reconstruct exactly: 767 and 539 residues. The short sequence retains displayed residues 1–538, changes V539 to G and lacks 540–767; both retain the annotated zinc-finger region and coiled coil. The genuine archived IMAGE4940443/BC033308 translation has 767 residues but differs from the current long product at 529 A/V, 545 A/T and 593 H/R. AK057406 has 539 residues but differs from the current short product at 158 T/M, 321 W/R and 382 N/S. These are archived-versus-current sequence differences, not newly inferred isoforms or proof of the exact expressed insert. No product's activity is inferred from sequence retention alone.

## Reproduction checklist

- [x] Algorithms read external raw files and query parameters; biological conclusions and review actions are not encoded as outputs.
- [x] Exact input hashes, public URLs and retrieval metadata are recorded; the archive preserves original bytes.
- [x] The interaction parser was also run with CEP76 as target, using reversed participant roles.
- [x] All expected source joins and sequence checks completed; direct outputs are included.
- [x] A saved-input replay outside the package reproduces the outputs exactly.
- [x] Access, construct, propagation and location limitations are stated above and in the source guide.
