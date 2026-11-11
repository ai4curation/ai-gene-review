# SHLD2 (horse, A0A9L0TUF0) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This review did not open or use any ProtNLM2 output. The folder is `SHLD2__A0A9L0TUF0` because the
plain `genes/HORSE/SHLD2` folder holds a different horse SHLD2 entry (A0A9L0RGD6, an 883-aa
non-canonical model) from the same Ensembl gene (ENSECAG00000001626). A0A9L0TUF0 is the 1047-aa
product of the Ensembl canonical transcript ENSECAT00000122467 and is the only horse SHLD2 model
with GO annotations in QuickGO (see `genes/HORSE/SHLD2/SHLD2-bioinformatics/RESULTS-rereview.md`).

**Deep research.** `just deep-research HORSE SHLD2__A0A9L0TUF0 --provider falcon` failed with
"Exception: Failed to authenticate". No deep-research file was created. No horse-specific SHLD2
study is known. The review relies on the cached human literature (PMID:29656893, PMID:29789392,
PMID:30022168), the human SHLD2 review (`genes/human/SHLD2`), the PTHR14495 PAINT table and a new
sequence comparison.

**Evolutionary grounding.**
- UniProt places A0A9L0TUF0 in PTHR14495:SF2, the only subfamily of PTHR14495, with human Q86V20.
- PAINT (`interpro/panther/PTHR14495/PTHR14495-paint.tsv`): one node, PTN001025652 (taxon 6072,
  Eumetazoa), seeded by human Q86V20 only, with IBD nucleus, site of DSB and the unsigned
  regulation of DSB repair via HR. The signed human terms (negative regulation of HR, positive
  regulation of NHEJ) and isotype switching were not placed at this node. I read that as a
  deliberate restriction for a node that spans Eumetazoa. The horse rows carrying the signed terms
  come from Ensembl Compara one-to-one orthology (GO_REF:0000107), a separate phylogenetic
  inference restricted to the mammalian ortholog.
- Sequence (`SHLD2__A0A9L0TUF0-bioinformatics/RESULTS.md`, `compare_to_human.py`): 73.9% identity
  to human long isoform Q86V20-2 over all 904 human residues. Human 6-11 (deletion abolishes
  SHLD3/MAD2L2 binding) is identical at horse 45-50. SHLD2C (human 421-904, binds ssDNA) is 81.8%
  identical. The OB-fold-B exon is present (85.5%). All four zinc-ribbon cysteines of OB fold C are
  conserved. Horse-specific: a 39-aa N-terminal and a 100-aa C-terminal extension, possibly
  gene-model artefacts (not tested).

**Experimental status in horse.** None. Every function in the review is inferred from human
(and mouse) experiments on the ortholog in the same subfamily, and the review text says so.

**Decisions.**
- ACCEPT: nucleus (IBA, IEA), nucleoplasm (IEA from human HPA), site of DSB (IBA, IEA), negative
  regulation of HR (IEA), positive regulation of NHEJ (IEA).
- MODIFY: chromosome -> site of DSB; regulation of HR (IBA) -> negative regulation of HR, which
  the gene already carries.
- KEEP_AS_NON_CORE: positive regulation of isotype switching (immune-specific context).
- NEW (ISS from PMID:30022168): single-stranded DNA binding and protein-macromolecule adaptor
  activity, the two human core activities, both missing from GOA. No new process terms were
  proposed; telomere-related and CSR mechanism terms on human were not transferred as NEW.
