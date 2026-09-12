# HMGCS2 (P54868) review notes

## Deep research status
- `just deep-research-falcon human HMGCS2` FAILED in this worktree: `scripts/deep_research_wrapper.py`
  raises `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'` at line 158
  (`uniprot_context: dict | None = None`) — the wrapper uses PEP 604 union syntax under a Python
  interpreter that does not support it. This is a tooling/env issue, not a transient failure, so no
  `HMGCS2-deep-research-falcon.md` was produced. Did NOT fabricate a deep-research file.
- Review grounded instead in: `HMGCS2-uniprot.txt` (P54868), seeded GOA (`HMGCS2-goa.tsv`),
  the disorder KB `~/repos/dismech/kb/disorders/3-Hydroxy-3-Methylglutaryl-CoA_Synthase_Deficiency.yaml`,
  and cached `publications/PMID_*.md`.

## Verified core biology
- HMGCS2 = mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase (mHS), EC 2.3.3.10.
- Catalytic activity (UniProt CATALYTIC ACTIVITY / RHEA:10188):
  acetoacetyl-CoA + acetyl-CoA + H2O = (3S)-3-hydroxy-3-methylglutaryl-CoA + CoA + H(+).
- It is the FIRST, rate-limiting/committed step of ketogenesis (ketone body biosynthesis), chiefly in
  liver during fasting; HMG-CoA product is then cleaved by HMG-CoA lyase (HMGCL) to acetoacetate.
  [file:HMGCS2-uniprot.txt "Catalyzes the first irreversible step in ketogenesis"]
  Disorder KB: "which is the rate-limiting step of ketone body synthesis"; "the rate-limiting step of ketogenesis".
- Localization: mitochondrion / mitochondrial matrix. UniProt SUBCELLULAR LOCATION: Mitochondrion (ISS
  from rat P22791). Reactome and Ensembl place it in mitochondrial matrix.
- Homodimer (crystal structure PMID:20346956, PDB 2WYA); catalytic Cys166 (acyl-thioester intermediate).
- Tissue: liver expression ~200-fold higher than any other tissue; induced during fasting.
- Distinct from CYTOSOLIC HMGCS1 (P54868 is mitochondrial; HMGCS1/P54869 is cytosolic mevalonate/
  cholesterol pathway). PMID:20346956 and PMID:7851882 make the mHS vs cHS distinction explicit.
- Disease: mitochondrial HMG-CoA synthase deficiency (HMGCS2D, MIM 605911): fasting hypoketotic
  hypoglycemia, encephalopathy, hepatomegaly.

## Annotation-level notes
- MF GO:0004421 (HMG-CoA synthase activity): strongly supported — EXP (PMID:11228257, PMID:29597274),
  IMP (PMID:23751782), IBA, ISS, TAS Reactome, IEA. CORE. All ACCEPT (dedup fine per guidelines).
- BP GO:0046951 (ketone body biosynthetic process): CORE — IMP (PMID:23751782), TAS Reactome, IEA. ACCEPT.
- BP GO:0006084 (acetyl-CoA metabolic process): correct but broad parent of the reaction; the enzyme
  consumes acetyl-CoA. Keep (ACCEPT the IMP/IBA; the acetyl-CoA is a substrate). Non-core relative to
  ketogenesis but not wrong.
- CC GO:0005739 mitochondrion / GO:0005759 mitochondrial matrix: correct; matrix is the more precise term.
- GO:0008299 isoprenoid biosynthetic process (InterPro2GO IEA): This is the CYTOSOLIC/prokaryotic
  HMGCS role (mevalonate/isoprenoid). HMGCS2 is the mitochondrial ketogenic isoform; it does NOT
  function in isoprenoid biosynthesis in vivo. InterPro family term over-propagated across all HMGCS.
  UniProt PATHWAY line "(R)-mevalonate biosynthesis ... step 2/3" and KW "Cholesterol biosynthesis" are
  family-level/paralog-derived and biologically incorrect for the mitochondrial ketogenic enzyme.
  MARK_AS_OVER_ANNOTATED (wrong-branch family transfer; the mitochondrial isoform does not make isoprenoids).
- GO:0016746 acyltransferase activity (InterPro IEA, thiolase-like fold): correct but far too general
  parent of GO:0004421. MODIFY -> GO:0004421.
- GO:0042802 identical protein binding (IDA, PMID:20346956): supported by crystal-structure homodimer.
  Per policy, do not REMOVE bare protein-binding IPI/IDA; keep as non-core (homodimer is structurally
  real but "identical protein binding" is uninformative vs the enzyme's function). KEEP_AS_NON_CORE.
- Large Ensembl-Compara "response to X" / "development" IEA block (GO_REF:0000107): transferred from rat
  ortholog RGD phenotype/expression annotations. HMGCS2 is transcriptionally regulated by fasting/PPARa/
  glucagon/cAMP/insulin etc., so many "response to hormone/nutrient" terms reflect regulation-of-expression
  rather than the gene product's own molecular activity in that process. These are peripheral. Keep the
  well-supported physiological ones as non-core; the many overly specific / developmental ones are
  over-annotations. Given they are IEA phenotype transfers (not experimental for HMGCS2), and per policy
  IEA over-propagation may be argued against, mark the clearly peripheral/organ-development ones
  MARK_AS_OVER_ANNOTATED and keep response-to-fasting/starvation/glucagon-type as non-core where they
  reflect known regulation.
