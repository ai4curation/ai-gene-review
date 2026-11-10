# Shadow log: go-annotation 6596

Worker: claude-opus-5-5. Blinding: BLIND (opening post only, via
`ai-gene-review shadow-issues show 6596 --opening-only`).

## 2026-11-10

### What I read

- The opening post: PTN000122012 (PTHR11117) propagates GO:0004776
  succinate-CoA ligase (GDP-forming) activity to S. cerevisiae LSC1 (P53598).
  The issue says the yeast enzyme is ADP-forming only.
- `genes/yeast/LSC1/LSC1-goa.tsv`: the IBA row (dated 20260528, with/from
  PTN000122012, RGD:619821, O19069, P0AGE9, P53597, Q51567,
  dictyBase:DDB_G0289325) sits beside SGD's `contributes_to GO:0004775` IDA/IMP
  rows from PMID:9874242.
- The existing repo work: the LSC1 review already had REMOVE on this row. The
  PTHR11117 family review had the node assessment UNRESOLVED. The S. pombe alpha
  review (SPAC16E8.17c) had MARK_AS_OVER_ANNOTATED.
- PAINT data for both subunit families (`interpro/panther/PTHR11117/`,
  `interpro/panther/PTHR11815/`), the PANTHER 19 tree for PTHR11117 (treeinfo
  service), and QuickGO annotations for the seeds and recipients.
- Publications: PMID:9874242 (yeast SCS genes), PMID:10353839 (E. coli SCS
  nucleotide site), PMID:9765291 (ATP- and GTP-specific SCS share one alpha),
  PMID:10671455 (P. aeruginosa broad-specificity SCS), PMID:16270230 (tomato
  SCS), all abstract-only.

### Reasoning

1. **What the term asserts.** GO:0004776 is the GTP/GDP reaction of the
   succinyl-CoA synthetase heterodimer. An alpha subunit can only contribute to
   it if its beta partner accepts GTP.
2. **Which subunit sets specificity.** The beta subunit.
   PMID:10353839: "It was concluded that the nucleotide-binding site is located
   in the N-terminal domain of the beta-subunit." PMID:9765291: "Highly ATP- and
   GTP-specific isoforms of succinyl-CoA synthetase in pigeon incorporate the
   same alpha-subunit, but different beta-subunits". The same abstract places
   the beta duplication early in the evolution of multicellular eukaryotes.
3. **The beta family already models this.** PTHR11815 has GO:0004776 IBD at
   PTN000929335 (the GTP-specific beta clade, seeds RGD:1305008, P53590,
   Q96I99) with an IKR NOT for GO:0004775 there, and GO:0004775 at the root
   PTN000212531. Yeast LSC2 and S. pombe SPCC1620.08 inherit only GO:0004775.
4. **The alpha family seeds.** Every GDP-forming seed has experimental support
   in its own organism: human SUCLG1 (EXP PMID:40108300), pig O19069 (EXP
   PMID:27487822), E. coli SucD (EXP PMID:10353839), P. aeruginosa SucD (EXP
   PMID:10671455, an enzyme that makes ATP and GTP about equally), and
   Dictyostelium P36967 (IDA PMID:8448193). So the curator's evidence is sound
   for those organisms. Placing the term at LUCA (PTN000122012) is a
   simplification that treats nucleotide specificity as an alpha-lineage
   property.
5. **Where it fails.** Fungi (PTN000874203): 19 IBA recipients in QuickGO on
   2026-11-10, including LSC1 and SPAC16E8.17c. Fungi have a single beta
   subunit of the ATP type, and the purified yeast enzyme "was shown to utilize
   ATP but not GTP" (PMID:9874242). Viridiplantae (PTN000122078) has 66
   recipients. The plant enzyme is usually described as ATP-forming, and the
   tomato alpha subunits are seeds for GO:0004775 only, but I did not find a
   plant nucleotide-specificity assay, so I leave plants as a candidate.
6. **The issue's framing.** I agree with the diagnosis for LSC1. One detail
   differs: the 2017 precedent's SPCC1620.08 is the S. pombe beta subunit, not
   the alpha orthologue. The alpha orthologue SPAC16E8.17c (O13750) carries the
   same IBA now and should be fixed with LSC1.

### Conclusion

- REMOVE GO:0004776 on LSC1 (P53598). Keep GO:0004775 (contributes_to).
- At source: add an IKR NOT for GO:0004776 at the PTHR11117 Fungi node
  PTN000874203. This also fixes S. pombe O13750 and the other fungal recipients.
- Possibly add the same NOT at Viridiplantae PTN000122078 after a check of the
  plant literature. The more principled alternative is to keep nucleotide
  specificity on the beta family (PTHR11815), where PAINT already models it, and
  drop or narrow the GDP-forming IBD at the alpha-family root.

### Work products

- `genes/yeast/LSC1/LSC1-ai-review.yaml`: added a `reason` to the REMOVE with
  the beta-subunit evidence and the source-fix recommendation. Added
  PMID:10353839 and PMID:9765291 to the references. `just validate yeast LSC1`
  passes.
- `interpro/panther/PTHR11117/PTHR11117-review.yaml`: the GO:0004776 node
  assessment changed from UNRESOLVED to NEEDS_PRUNING, with the reasoning and
  quotes. Schema, reference and quote checks pass.
- `history/genes/yeast/LSC1/2026-11-10T015606Z-claude-opus-5-5-bb2d89.yaml`.

### What remains

- Plant nucleotide specificity (does any plant SCS use GTP?) before a NOT at
  Viridiplantae.
- Protist and other eukaryotic clades under PTN000122014 (e.g. Plasmodium,
  trypanosomes, diatoms) are unchecked.
- I did not review the other 17 fungal recipients individually.
- The `enables` qualifier for an alpha subunit on a heterodimer activity is
  arguably `contributes_to` (SGD uses contributes_to). This is a general PAINT
  convention question and outside this issue.

### Tooling notes

- The worktree started one commit behind the commit that added `issues/`. I
  had to fast-forward it to 9d4905a9b5 before the mirror existed.
- The worktree-isolation guard refuses shell loops and `$(...)` with computed
  arguments, even for read-only `sed` or `python` calls, so several queries had
  to be rewritten as scratch scripts.
