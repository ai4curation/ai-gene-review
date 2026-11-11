# KDM4C (human, Q9H3R0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: KDM4C is the experimentally characterised reference relative for the
donkey (EQUAS) KDM4C benchmark gene (A0A9L0K3L6), which sits in the same PANTHER
subfamily PTHR10694:SF104 (LYSINE-SPECIFIC DEMETHYLASE 4C). ProtNLM2 output was
not opened or used.

### Deep research

`just deep-research-falcon human KDM4C --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (403) and the
perplexity-lite fallback also failed. No deep-research file was produced. The
review is built from the UniProt record, the GOA-cited papers and additional
primary papers cached with `just fetch-pmid`.

### Evolutionary grounding

- UniProt: PANTHER PTHR10694:SF104 (LYSINE-SPECIFIC DEMETHYLASE 4C); "Belongs to
  the JHDM3 histone demethylase family". Domains JmjN, JmjC, two PHD fingers,
  double Tudor.
- IBA rows for H3K9 and H3K36 demethylase activity descend from PANTHER:PTN000075207
  (KDM4 clade); the nucleus/chromatin/gene-expression IBA rows from the deeper
  PTN000075014 node. Q9H3R0 itself is among the descendant evidence.
- Hillringhaus et al. 2011 [PMID:21914792 "KDM4A–C, which are highly conserved in
  all vertebrates, and demethylate both H3K9 and H3K36 and KDM4D/E, which only
  accept H3K9 substrates"]. So dual H3K9/H3K36 specificity is a KDM4A-C subgroup
  property, not shared with KDM4D/E; it should transfer to vertebrate KDM4C orthologs
  (including donkey/horse) but not to KDM4D-like paralogs.

### Experimentally established in human KDM4C

- H3K9me3/me2 demethylase (in vitro kinetics with KDM4C catalytic domain)
  [PMID:21914792 table 1: KDM4C Km/kcat for H3K9me2 and H3K9me3 peptides];
  [PMID:16732293 "three members of this subfamily of proteins demethylate H3K9me3/me2
  in vitro through a hydroxylation reaction requiring iron and alpha-ketoglutarate as
  cofactors"].
- H3K36me3/me2 demethylation [PMID:21914792 "KDM4A/B/C accepted both H3K9 and H3K36
  as substrates"], with lower activity than H3K9 [PMID:21914792 "We were unable to
  obtain reliable kinetic parameters for the H3K36 substrates because of the
  relatively low levels of activity at this site"].
- Catalytic-dead H190A/E192A used as control in cellular demethylation assays
  [PMID:28262558].
- Crystal structure of JmjN-JmjC (PDB 2XML) with Ni2+/NOG and structural Zn
  [PMID:21914792].
- Double Tudor domain recognises H3K4me3; KDM4C binds H3K4me3-positive TSSs
  [PMID:24396064 "the double Tudor domains of mouse and human JMJD2C specifically
  recognize H3K4me3"].
- AR coactivator: interacts with AR, demethylates H3K9me3 at AR targets, stimulates
  AR-dependent transcription, cooperates with LSD1 [PMID:17277772]; PKN1 H3T11
  phosphorylation accelerates KDM4C demethylation [PMID:18066052].
- ATF4 partner in activating serine/glycine synthesis genes by H3K9me3 removal
  [PMID:26774480].
- Cancer-cell knockdown reduces proliferation (oesophageal, prostate, PMBL/HL)
  [PMID:16732293; PMID:17277772; PMID:21156283] — cancer amplicon context, treated as
  non-core.

### Mouse genetics (ortholog, not human)

- Jmjd2c knockout mice viable; Kdm4c dispensable for development and ESC self-renewal
  [PMID:24396064]; Kdm4a/Kdm4c double loss is lethal, redundant removal of promoter
  H3K9me3/H3K36me3 [PMID:27266524]. Earlier knockdown work linked Jmjd2c to Nanog
  regulation [PMID:17938240]. No ESC/pluripotency process term proposed (redundancy;
  mouse-only; necessity evidence).

### Decisions

- Generic `histone demethylase activity`, `histone H3K9 demethylase activity`,
  `histone H3K36 demethylase activity` -> MODIFY to the methylation-state-specific
  children GO:0140684 (H3K9me2/me3) and GO:0140681 (H3K36me2/me3).
- GO:0050681 is labelled obsolete in GOA; QuickGO says obsolete with consider
  GO:0016922 nuclear receptor binding (OLS still lists it active). MODIFY to
  GO:0016922.
- NEW: GO:0140002 histone H3K4me3 reader activity (Tudor domain, human protein tested).
- UniProt's FUNCTION line says no activity on dimethylated residues; Cloos 2006 and
  Hillringhaus 2011 kinetics show H3K9me2 is a substrate in vitro. The me2/me3 term is
  used.
