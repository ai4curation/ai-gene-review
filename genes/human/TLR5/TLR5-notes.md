# TLR5 (O60602, human) — curation notes

Toll-like receptor 5. Cell-surface pattern recognition receptor for bacterial flagellin.

## Deep research
`TLR5-deep-research-falcon.md` arrived after the review was drafted; the review itself is
based on the cached UniProt record, cached PMIDs and Reactome/OLS/QuickGO. See the
cross-check section at the end.

## Core biology
- TLR5 recognizes bacterial flagellin (from Gram-positive and Gram-negative bacteria);
  ligand binding activates NF-kappaB and induces proinflammatory cytokines (TNF, IL-6, IL-8)
  [PMID:11323673 "mammalian TLR5 recognizes bacterial flagellin from both Gram-positive and Gram-negative bacteria, and that activation of the receptor mobilizes the nuclear factor NF-kappaB and stimulates tumour necrosis factor-alpha production"].
- TLR5 recognizes a conserved buried site on flagellin required for protofilament formation
  and motility; monomeric (not filamentous) flagellin stimulates; flagellin coprecipitates with TLR5
  [PMID:14625549 "flagellin coprecipitated with TLR5, indicating close physical interaction between the molecules"].
- Cell-surface receptor; the response needs the extracellular LRRs and the intracellular TIR
  domain plus MyD88; TLR5 is on the basolateral surface of intestinal epithelia
  [PMID:11489966 "cell surface expression of Toll-like receptor 5 (TLR5) conferred NF-kappaB gene expression in response to flagellin. The response depended on both extracellular leucine-rich repeats and intracellular Toll/IL-1R homology region of TLR5 as well as the adaptor protein MyD88"; "TLR5 is expressed exclusively on the basolateral surface of intestinal epithelia"].
- TLR5 also engages TRIF (TICAM1), not only MyD88, in intestinal epithelial cells
  [PMID:20855887 "TLR5 activation by flagellin permits the physical interaction between TLR5 and TRIF in human colonic epithelial cells (NCM460)"].
- TLR5 forms an asymmetric homodimer in the absence of flagellin (EM structure)
  [PMID:22173220 "TLR5 forms an asymmetric homodimer via ectodomain interactions"].
- Phosphorylation of Ser805 in the TIR domain by PKD is required for inflammatory signalling
  [PMID:17442957 "mutation of serine 805 to alanine abrogated responses of transfected HEK 293T cells to flagellin"].
- A common dominant stop-codon polymorphism (R392STOP / C1174T) abolishes flagellin signalling;
  associated with susceptibility to Legionnaires' disease and protection from SLE
  [PMID:14623910 "a common stop codon polymorphism in the ligand-binding domain of TLR5 (TLR5392STOP) is unable to mediate flagellin signaling"; PMID:16027372 "the TLR5 stop codon polymorphism is associated with protection from the development of SLE"].

## UNC93B1 dependence (project-relevant)
- Unexpectedly, TLR5 (a cell-surface TLR) requires UNC93B1 for plasma membrane localization and
  signalling, unlike TLR1/2/4/6 [PMID:24778236 "TLR5, a cell surface receptor for bacterial protein flagellin, also requires UNC93B1 for plasma membrane localization and signaling"].

## Specific annotation notes
- GO:0005149 interleukin-1 receptor binding (IPI, PMID:12925853): partner SIGIRR/IL-1R8, a
  negative regulator of TLR-IL-1R signalling. Abstract-only. SIGIRR is an IL-1R-family protein so
  the term is satisfiable, but it reflects negative feedback, not a TLR5 core function. KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI, PMID:30158114) x2, partners APP-derived amyloid-beta chains
  (PRO_0000000092/093): the paper (TLR5 decoy) shows soluble TLR5 ectodomain-Fc binds oligomeric/
  fibrillar Abeta with high affinity by ELISA and BLI. Informative MF is amyloid-beta binding
  (GO:0001540) -> MODIFY. Shown with engineered soluble ectodomain; not core.
  [PMID:30158114 "sTLR5Fc binds to oligomeric and fibrillar Aβ with high affinity, forms complexes with Aβ, and blocks Aβ toxicity"].
- GO:0038187 pattern recognition receptor activity (IDA x2, PMID:14625549 and PMID:17128265):
  core MF for TLR5 — recognizes the flagellin PAMP. ACCEPT.
- GO:0034146 toll-like receptor 5 signaling pathway (IDA x2): core process. ACCEPT.
- GO:0032757 positive regulation of interleukin-8 production (IDA, PMID:17128265): PMID:17128265 is
  the apical/basolateral TLR9 IEC paper (abstract does not describe a TLR5 IL-8 experiment). Flagellin/
  TLR5 induction of IL-8 in IECs is well established elsewhere (e.g. PMID:29934223). Deferring to
  curator (full text not in cache); KEEP_AS_NON_CORE (downstream inflammatory output, not core).
- GO:0071260 cellular response to mechanical stimulus (IEP, PMID:19593445): the cited PMID is
  "Expression of the Bcl-2 protein BAD promotes prostate cancer growth" (PLoS One) — full text
  cached, contains no mention of TLR or mechanical stimulus. This looks like a wrong/mismatched
  PMID for a TLR5 mechanotransduction IEP. Cannot verify the claim from the cited paper -> UNDECIDED,
  flag citation as likely WRONG_IDENTIFIER in reference_review.
- Many GO:0005886 plasma membrane rows (IBA/IDA/IEA/TAS Reactome): all consistent; ACCEPT.
- Reactome TAS rows for plasma membrane are the Myddosome-cascade reactions; ACCEPT as location.

## Comparator note (participation)
TLR5 itself performs the recognition step (binds flagellin) and initiates signalling, so PRR
activity and the TLR5 pathway term are genuine participation, not substrate/necessity artefacts.

## Deep-research cross-check (2026-09-30)

Compared the completed review against `TLR5-deep-research-falcon.md`.
**No annotation action, term, description or core function was changed.**

Agreement:
- TLR5 is a signalling receptor, not an enzyme, whose specific ligand is bacterial
  flagellin; recognition targets conserved D1-domain determinants (around residues 88-98)
  that are buried in the assembled filament, so soluble/exposed monomers are the effective
  ligand. This matches the accepted `pattern recognition receptor activity` rows and the
  core functions, and matches PMID:14625549 and PMID:11323673 already quoted.
- Plasma-membrane localisation with basolateral enrichment in intestinal epithelium, used
  to discriminate breaching pathogens from luminal commensals. Supports the accepted
  plasma-membrane rows and the description.
- MyD88/myddosome to TRAF6-TAK1, then NF-kappaB and MAPK, with IL-8/CXCL8, CXCL1/2/5,
  CCL2, CCL20, TNF and IL-6 as outputs. Supports keeping the IL-8 row as a non-core
  downstream output rather than a core function.
- A 2:2 flagellin-TLR5 signalling complex, consistent with the description's homodimer
  statement and with PMID:22173220.

Additions not acted on:
- "Silent" commensal flagellins (e.g. Roseburia hominis) that engage the canonical D1
  interface but dissociate too fast to form a productive complex. The primary source is a
  December 2024 preprint cited only through the report, so nothing was asserted; this is a
  property of the ligand rather than a new TLR5 function.
- Bacterial evasion by motif substitution, filament sequestration and flagellin
  downregulation; cancer-prognosis and vaccine-adjuvant/entolimod translational material.
  All indirect; no NEW terms proposed.
- The report does not mention the UNC93B1 requirement (PMID:24778236); the review's
  treatment of it is unaffected and the existing suggested question stands.

Conflict: the report states that TLR5 signals "exclusively" through MyD88, whereas the
review's description and second core function also credit TRIF/TICAM1 in intestinal
epithelium. The review's statement rests on a primary paper quoted verbatim
[PMID:20855887 "TLR5 activation by flagellin permits the physical interaction between TLR5
and TRIF in human colonic epithelial cells (NCM460)"], while the report's claim comes from
secondary reviews, so the review was left unchanged. The existing suggested question on the
MyD88/TRIF balance already records the tension.
