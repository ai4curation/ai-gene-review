# CG34171-PB (A8DZ15) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder for the full-length CG34171-PB product (A8DZ15, 292 aa). The truncated PC
product X2JEK1 has its own review in `genes/DROME/CG34171/`. Fetched with
`just fetch-gene DROME A8DZ15 --alias CG34171__A8DZ15`, following the
`CG33453__A1ZBI2` precedent. No ProtNLM2 file or prediction-evidence folder was opened.

Deep research: I reused the gene-level Falcon report in the sibling folder
(`CG34171/CG34171-deep-research-falcon.md`, run with X2JEK1). It found no
CG34171-specific study [file:DROME/CG34171/CG34171-deep-research-falcon.md "No CG34171-specific
loss-of-function, gain-of-function, RNAi, infection, developmental, or biochemical phenotype was
found."]. Its "CLIP subfamily" framing comes from ARBA. A8DZ15 has no clip domain: the
S1 domain starts at residue 38, right after the 16-residue signal peptide.

### Sequence and catalytic status
- The S1 domain (38-265) has H72 and D124 at the trypsin His and Asp columns and F222 at the Ser
  column [file:DROME/CG34171__A8DZ15/CG34171__A8DZ15-bioinformatics/RESULTS.md]. This agrees with
  the earlier two-mode MAFFT analysis [file:DROME/CG34171/CG34171-bioinformatics/RESULTS.md
  "A8DZ15 has F222 at the serine-equivalent position."].
- The C-terminal residues 274-292 (FIADRFSLFSFIILMLSIV) are strongly hydrophobic (mean KD 2.01).
  UniProt does not annotate them. This could be a GPI signal or a membrane anchor. Unresolved.

### Evolutionary placement
- In the PANTHER 19.0 fly HMM file, A8DZ15 is in PTHR24260:SF136, which has 13 fly members. UniProt
  says PTHR24276:SF96, and the GOA IBAs come from PTHR24256 PTN000667087. The three placements
  disagree.
- The triad is intact in only 3 of the 13 SF136 members (modSP, CG6592, CG30091).
- modSP is the only SF136 member that is a PAINT seed at PTN000667087. It is 23% identical to
  A8DZ15 and has a different architecture (4 LDLa and 2 Sushi modules), so its Toll-initiating role
  is not transferred. A8DZ15 is at most 28.8% identical to any SF136 member, and there is no
  one-to-one ortholog. This is consistent with the task brief's statement that DIOPT finds no
  ortholog scoring above 1.

### Actions
- NOT GO:0004252 (IKR): ACCEPT.
- NOT GO:0008233 (IKR): ACCEPT.
- GO:0005576 (IBA): ACCEPT, with the caveat about the C-terminal anchor.
- GO:0006508 (IEA): MARK_AS_OVER_ANNOTATED. PAINT gave this gene no proteolysis IBA. Same action
  as on the X2JEK1 row.
- GO:0045087 (IBA): KEEP_AS_NON_CORE. The node seeds include a noncatalytic CLIPA8, so losing
  the catalytic serine is not evidence that the immune function was lost. There is no target
  evidence either way.
- No NEW terms proposed.

### Note for transfer
Nothing about this gene is experimentally established. The only firm statements are the
sequence-based ones: the catalytic serine is replaced, and there is a predicted signal
peptide. All process and location terms are phylogenetic inferences.
