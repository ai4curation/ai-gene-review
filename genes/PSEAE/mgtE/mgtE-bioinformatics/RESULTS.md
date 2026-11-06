# mgtE (PA0913) bioinformatics: PAINT node PTN000227060 and Mg2+-site conservation

Scripts (run 2026-10-28):

- `panther_node_composition.py PTHR43773 PTN000227060 Q9I544 PTHR43773-tree.json`
  (PANTHER v19 `treeinfo` tree saved with curl as `PTHR43773-tree.json`;
  output `panther_node_composition_output.txt`)
- `quickgo_node_checks.py GO:0000287 PTN000227060 O34442,Q5SMG8,Q9I544` and the
  same for GO:0015693 (live QuickGO; output `quickgo_node_checks_output.txt`)
- `leaf_domain_check.py PTHR43773-tree.json PTN000227060 PF01769`
  (live UniProt; output `leaf_domain_check_output.txt`)
- `uv run mg_site_conservation.py` (Biopython global alignment of Q5SMG8 and
  Q9I544, BLOSUM62; output `mg_site_conservation_output.txt`)

## Findings (from the outputs)

- PTN000227060 is the root of the PTHR43773 tree (Eubacteria speciation node,
  is_family_root: True): 25 leaves in 21 organisms. GOA holds 25 GO:0000287
  IBA rows and 25 GO:0015693 IBA rows with with/from PTN000227060.
- Thermus thermophilus MgtE (Q5SMG8), the structurally and electrophysiologically
  characterised family member with IDA GO:0000287 (PMID:17700703), is a
  PTHR43773:SF1 member by HMM but is not a leaf of the reference tree, so it
  could not be a PAINT seed.
- Of the 22 leaves resolved in UniProt, 16 carry Pfam PF01769 (MgtE
  transmembrane domain) and 6 do not: SCO5154 (Q9FBK4) and Rv1232c (O86315),
  which form the Actinomycetales clade PTN005181931, CBO0203 (A5HY96), TM_0892
  (Q9WZZ4), the Nematostella protein A7T8Y4 and VC_0300 (Q9KV57). Five of the
  six have no predicted transmembrane segment; A7T8Y4 has two. Three leaves
  (B. subtilis mgtE, Synechocystis mgtE, FN1480) were not resolved by the
  locus-tag search.
- Q9I544 aligns with Q5SMG8 at 34.2% identity over 430 aligned pairs. Of the
  15 Q5SMG8 Mg2+-binding positions with ECO:0000269 evidence (16 site
  entries; Asp226 ligates two ions), 8 positions are identical in Q9I544
  (pore Asp432 -> Asp466, the connecting-helix/CBS sites Asp226 -> Asp259
  and Asp250 -> Asp283, and Glu59, Asp91, Asp95, Glu255, Asp418), 2 are
  conservative acidic substitutions (Asp247 -> Glu280, Asp259 -> Glu292),
  and 5 are changed (Gly136 -> Ala169, Glu216 -> Tyr249, Ala223 -> Glu256,
  Glu258 -> Ser291, Ala428 -> Thr462). Several of the
  changed Tth positions (Gly136, Ala223, Ala428) are not side-chain acidic
  ligands in Tth either.

## Interpretation

The Mg2+-binding apparatus of the Tth channel, including the pore aspartate and
most acidic cytosolic sensor ligands, is conserved in PA0913, so Mg2+ binding by
P. aeruginosa MgtE is a sound inference by sequence similarity. It is not shown
by the PseudoCAP-cited paper, whose evidence is the loss of function of
predicted-site mutants.

Magnesium ion transport at the family root is right for the full-length
transporters, but six reference leaves lack the transmembrane domain and cannot
be transporters on their own; they inherit the transport IBA anyway. This is an
over-propagation of the BP IBD to divergent soluble members, not a defect of
the PA0913 seed.

The alignment-based mapping is approximate (a single pairwise alignment;
the P. aeruginosa N-terminus is about 35 residues longer).
