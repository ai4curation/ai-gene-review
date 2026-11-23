# PA2126 (CgrC, Q9I1Y9) review notes

ParB-like N-terminal domain (Pfam PF02195) and IbrB_C region (PF30335); 211 aa. Gene names from McManus and Dove 2011: CgrA residues 2-408 and CgrC
residues 2-211 match PA2127 (408 aa) and PA2126 (211 aa).

## Literature (no deep-research provider; own reading, 2026-11-05)

- Vallet-Gely et al. 2007 (abstract only; PMC2168922 returned no body text via
  the PubMed MCP): cgrABC and Anr are positive regulators of cupA; [PMID:17890313
  "the cgr genes are essential for this expression"] and cgr expression is
  [PMID:17890313 "positively controlled by Anr and anaerobiosis"]. Source of the
  PseudoCAP IEP rows.
- Trunk et al. 2010 (abstract only): Anr/Dnr regulons after oxygen depletion
  [PMID:20553552 "the P. aeruginosa response to an immediate oxygen
  depletion"]; the abstract does not name the cgr genes.
- McManus and Dove 2011 (full text, PMC3209204): CgrA and CgrC interact
  directly [PMID:21926232 "Here, we show that CgrA and CgrC interact with one
  another directly."]; the interaction is needed for cupA expression
  [PMID:21926232 "interaction between CgrA and CgrC is required for the
  phase-variable expression of the cupA fimbrial genes"]; CgrC, not CgrA, is
  at the cupA promoter [PMID:21926232 "However, ChIP experiments performed with
  CgrA-TAP did not reveal any detectable association between CgrA and the cupA
  promoter region (data not shown)."]; CgrA has a putative PAPS reductase
  domain, CgrB is GNAT-like, CgrC ParB-like.
- PubMed search via MCP and NCBI eutils returned errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000764275 | GO:0071453 cellular response to oxygen levels | 2 | 12 (5 taxa) | GO:0071453, IEP, PMID:17890313 (PseudoCAP) | SOUND (as IEP) | Abstract states cgr expression is induced by anaerobiosis via Anr. Correct as an expression annotation; anoxia is the more precise stimulus. | the other cgr gene (PA2127/PA2126), same two IEP papers | No. The only other seed is the partner cgr gene with the same IEP evidence; an Anr-dependent expression response in one species is not an inheritable function of the clade |
| PTN000764275 | GO:0071453 cellular response to oxygen levels | 2 | 12 (5 taxa) | GO:0071453, IEP, PMID:20553552 (PseudoCAP) | UNVERIFIABLE | Abstract only; does not name the cgr genes. | as above | as above |

No PSEUDOCAP defect: the IEP rows are a conventional use of IEP for a
response term. The node-level GO_CENTRAL defect for PTN000764275 is recorded once, on genes/PSEAE/PA2127 (CgrA); this review cross-references it and makes the same row-level calls.

## Other decisions

- IEP and IBA rows on GO:0071453 MODIFY to GO:0071454 cellular response to
  anoxia (the stimulus is anaerobiosis/oxygen depletion); same action on all
  three rows, so the gene-level claim is consistent.
- GO:0005515 IPI REMOVE (protein-binding policy); the CgrA-CgrC interaction is
  real and is reflected in the coregulator description.
- NEW GO:0045893 positive regulation of DNA-templated transcription (IMP,
  PMID:21926232), added on both PA2127 and PA2126.
