# YARS1 (P54577) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: YARS1 is reviewed in its own right as the closest experimentally characterised
relative of Drosophila TyrRS (Q9VV60). No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human YARS1 --fallback perplexity-lite` failed on 2026-10-21:
falcon raised "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists. The review is based on the cached
publications listed below plus the UniProt record.

Additional PMIDs cached for this review (beyond the GOA set): 12427973, 14671330,
16429158, 27633801, 29232904, 36307205.

### Evolutionary placement

- UniProt: PANTHER PTHR11586:SF43 "TYROSINE--TRNA LIGASE, CYTOPLASMIC" (verified in
  `interpro/panther/panther.obo`); Pfam PF00579 tRNA-synt_1b (catalytic + anticodon
  domains) and PF01588 tRNA_bind (C-terminal EMAP-II-like domain, residues 364-468).
- The only IBA (GO:0004831) comes from PAINT node PTN000236303, whose sources include
  Drosophila TyrRS (FB:FBgn0027080) and YARS1 itself. The target in its own WITH/FROM is
  expected, not circular: YARS1 has direct IDA evidence for the activity.
- PAINT propagated only the ligase activity to this node. No IBA exists for nuclear
  localisation, PARP1 activation, cytokine or receptor-binding functions; these are
  treated as human-established, not clade-level, functions.
- The mitochondrial paralog YARS2 is in a different PANTHER family; nothing here is
  transferred from or to it.

### What is experimentally established in human (vs inferred)

Experimental, human protein:
- Tyrosine-tRNA ligase activity on human tRNA(Tyr) (PMID:9162081 kinetics; PMID:25533949
  inhibition by resveratrol, Ki 22 uM; PMID:16429158 CMT mutants with partial loss of
  aminoacylation; PMID:22291016 NLS mutants attenuate aminoacylation).
- Homodimer; P167T disrupts dimerisation and catalysis (PMID:30304524; crystal structure
  PMID:12427973).
- Cytoplasmic in resting cells; tRNA(Tyr)-controlled nuclear import via a hexapeptide NLS in
  the anticodon-recognition domain (PMID:22291016). Serum starvation or resveratrol
  promotes nuclear translocation (PMID:25533949).
- Resveratrol-bound TyrRS binds the PARP1 C-terminal domain and stimulates PARP1
  auto-PARylation; TyrRS also activates PARP1 in vitro without resveratrol (PMID:25533949).
  Basis for MODIFY of the PARP1 IPI protein-binding row to GO:0008047 enzyme activator
  activity.
- Secretion under apoptotic conditions; elastase cleavage gives mini-TyrRS (binds CXCR1/
  IL-8 type A receptor, IL-8-like cytokine via ELR motif) and an EMAP-II-like C-domain
  (chemotactic) (PMID:10102815). Full-length TyrRS lacks cytokine activity (PMID:12427973).
  These are fragment functions and are kept as non-core.

Inferred only:
- tRNA binding (IEA, InterPro tRNA-bd domain), ATP/nucleotide binding (IEA), response to
  stress (ARBA). The tRNA-binding claim is strongly backed by the NLS/tRNA interaction data.

### Decisions summary

- GO:0004831 (all 5 rows): ACCEPT.
- GO:0006437 (obsolete; replaced_by GO:0006418 per QuickGO): MODIFY -> GO:0006418.
- GO:0004812 IEA: MODIFY -> GO:0004831.
- cytoplasm rows: MODIFY -> cytosol (cytosol is carried by IDA/TAS rows).
- nucleus rows: KEEP_AS_NON_CORE (conditional, regulated pool). Nuclear body (HPA only):
  UNDECIDED.
- Apoptotic process TAS: MARK_AS_OVER_ANNOTATED (the paper only speculates that secretion
  "may contribute to apoptosis").
- Protein binding: REMOVE for Y2H/screen partners and Npro; PARP1 -> MODIFY to enzyme
  activator activity.
- small molecule binding (resveratrol IDA): MODIFY -> L-tyrosine binding (co-crystal with
  tyrosine, same paper); resveratrol binding itself is a pharmacological interaction.
- NEW: GO:0042803 protein homodimerization activity (PMID:30304524, PMID:12427973).

### Comparison with Drosophila TyrRS

Fly TyrRS (same PANTHER subfamily SF43) is also secreted by apoptotic loser cells and cleaved
into MiniTyr and EMAP fragments, with EMAP attracting haemocytes (PMID:26658841). This is a
parallel to the human secreted cytokine fragments, but the receptor-level claims (IL-8 type A
receptor binding via the ELR motif) are established only for human mini-TyrRS and should
not be transferred to the fly protein.

Revision (same session): the three nucleus rows were changed from KEEP_AS_NON_CORE to ACCEPT,
because the nucleus is where the experimentally established PARP1-activating function is
performed (second core function). The nuclear pool is still conditional.
