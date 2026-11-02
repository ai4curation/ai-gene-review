# RHPN2 (Q8IUC4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RHPN2 is reviewed as the closest experimentally characterised relative of fly Rhp
(Q9XYY9, PANTHER PTHR23031:SF15). RHPN2 is in SF5, RHPN1 in SF6, and PAINT node PTN001126281
covers all three. No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon human RHPN2 --fallback perplexity-lite` failed. Falcon gave
"Failed to authenticate" and perplexity-lite gave HTTP 401 insufficient_quota. No deep-research file
exists. The review uses PubMed searches (esearch RHPN2/rhophilin-2, 53 hits) and these cached
papers: PMID:12221077, 12473120, 17054945, 15767687, 22445486 (full text), 23774217 (full text),
40254160, 25071083 (full text).

### Experimentally established for RHPN2 (human protein unless stated)
- Rho binding: nucleotide-independent RhoA binding by GST capture; E58/N59 mutation abolishes it
  [PMID:12221077 "Glutathione S-transferase-capture experiments revealed that Rhophilin-1 and
  Rhophilin-2 interacted with both GDP- and GTP-bound RhoA in vitro"]. GTP-RhoB-selective binding
  by Y2H/co-IP [PMID:12473120 "p76RBE is a specific binding protein of RhoB and binds selectively
  to the GTP-bound form of this small GTPase"]. The two studies disagree about RhoA.
- Stress fibres: overexpression in HeLa dissolves stress fibres, which needs the BRO1 and PDZ
  domains; RhoA-GTP rises rather than falls [PMID:12221077]. Confirmed in HeLa cells, where the
  PDZ lipid-binding mutants K576/K579 are inactive [PMID:22445486 "both mutations abrogated the
  activity of rhophilin-2 to disassemble stress fibers"]. Both are overexpression studies.
- Lipid binding: the PDZ domain binds anionic lipids non-specifically [PMID:22445486].
- Localization: cytoplasmic and perinuclear, at the plasma membrane via the PDZ domain, and
  recruited by activated RhoB to CD63+ late endosomes in a BRO1-dependent way [PMID:12473120,
  17054945, 22445486].
- Mouse Rhpn2 knockout: normal development, fertility and thyroid [PMID:15767687].
- Cancer: overexpression or amplification raises RhoA activity and invasion in glioma
  [PMID:23774217]. Not annotated.
- Zebrafish rhpn2 mutant: vestibular hair-cell defects [PMID:40254160]. This is an organismal
  phenotype and is not annotated.

### Key finding: mis-keyed MGI rows
PMID:25071083 (Lal et al. 2015, Rhophilin-1 in podocytes) is cited for two MGI IDA rows on human
RHPN2, GO:0005886 and GO:0051497. The full-text methods say: "Human Rhpn1 was expressed in
mammalian cells using the pcDNA4/TO/myc-His-A expression vector". The only mentions of RHPN2 are
that it was "only nominally detected in glomeruli" and as an allele in a mouse cross. QuickGO
shows that human RHPN1 (Q8TCX5) has no rows from this paper, and that mouse Rhpn1 Q61085 has ISO
rows with With/From Q8IUC4. This is a clear WRONG_GENE_PRODUCT defect (Q8IUC4 should be Q8TCX5).
It also means one of the two seeds of PAINT node PTN001126281 is the mis-keyed row.

Even so, both claims are true for RHPN2 on its own evidence (Peck 2002; Chen et al. 2012,
PMID:22445486), so the claims are ACCEPTed and the defect is recorded in `source_defects` rather
than removing the rows. The IBA for GO:0051497 is accepted: the conclusion is sound for RHPN2 and
for both vertebrate paralogs, but the node should be re-seeded with PMID:12221077.

### Implications for transfer to fly Rhp
- Directly shown for RHPN2: small GTPase (Rho) binding, PDZ phospholipid binding, and
  stress-fibre inhibition when overexpressed. The paralog RHPN1 independently has the
  stress-fibre activity (podocytes), which supports placing it at the family node.
- Not established for RHPN2: any in vivo requirement (the mouse KO is normal), a physiological
  PDZ ligand, or ESCRT/BRO1 partners. The late-endosome localization depends on co-expressed
  activated RhoB.
- Fly Rhp is a pre-duplication co-ortholog (SF15). Only family-level properties (Rho binding,
  BRO1/PDZ architecture, the node-level GO:0051497) should be transferred. RHPN2-specific
  features such as TSH/cAMP induction should not.
