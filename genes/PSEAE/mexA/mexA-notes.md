# mexA (PA0425, P52477) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P52477 --alias mexA`; accession matches the
worklist. Reviewed Swiss-Prot entry. No deep-research provider was used. Cached
papers: PMID:33009415, PMID:30944318 and PMID:11114896 have full text;
PMID:8540696 (the PseudoCAP seed paper), PMID:25901994, PMID:9973347 and
PMID:15226509 are abstract-only (the PMC copy of PMID:8540696 returned no text).
The PubMed MCP search returned API errors.

### Literature

- MexA is the inner-membrane-anchored periplasmic adaptor of MexAB-OprM; six MexA
  molecules join the MexB trimer to the OprM trimer
  [PMID:30944318 "MexB does not directly contact OprM; instead, MexA joins MexB and OprM by forming a funnel-like hexamer."].
- MexA is required for MexB proton-coupled transport in proteoliposomes
  [PMID:33009415 "in the absence of MexA almost no proton transport is measured for MexB-solo despite the presence of substrate"],
  and the reconstituted pump transports substrate
  [PMID:25901994 "By combining proteoliposomes containing the MexAB and OprM portions of the complex, we are able to assay energy-dependent substrate translocation in a system that mimics the dual-membrane architecture of Gram-negative bacteria."].
- Seed paper: null mutants accumulate more drug and are more susceptible
  [PMID:8540696 "Thus, the steady-state accumulation levels of tetracycline and norfloxacin were increased in mexA and oprM null mutants."].
- Efflux of the quorum-sensing signal 3OC12-HSL
  [PMID:9973347 "Instead, the mexA-mexB-oprM-encoded efflux pump is involved in active efflux of 3OC12-HSL."].

### Decisions

- ACCEPT: plasma membrane (IBA, IEA); antiporter activity (contributes_to, IDA);
  efflux transmembrane transporter activity (IBA, IDA x2, IMP); cell envelope (IDA);
  xenobiotic export from cell (IDA); GO:0140330 (IBA, IDA); efflux pump complex
  (IDA x3).
- KEEP_AS_NON_CORE: response to antibiotic (IBA; PseudoCAP IDA with evidence-code
  defect); identical protein binding and protein homooligomerization (IMP; MexA
  hexamer).
- TOO_GENERAL: membrane (IEA); transmembrane transporter activity (IEA);
  transmembrane transport (IDA, IMP, IEA).
- Counts: ACCEPT 14, KEEP_AS_NON_CORE 4, TOO_GENERAL 5.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001249140 | GO:0046677 response to antibiotic | 6 | 38 (12 taxa) | GO:0046677, IDA, PMID:8540696 (PseudoCAP) | SOUND | Abstract: mexA null mutants accumulate more tetracycline, norfloxacin and benzylpenicillin and are more susceptible to beta-lactams. The term is right; the experiments are on null and overproducing mutants, so the code should be IMP (PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE: abstract only). | E. coli AcrA (P0AE06; EcoCyc IMP/IGI), E. coli MdtE (P37636; EcoCyc IMP), MexE (Q9I0Y9; IGI), MexC (G3XD25; IGI), MexX (G3XD21; PseudoCAP EXP/IMP) | Yes |

No GO_CENTRAL defect. The node-level assessment (clade of RND-pump membrane fusion
proteins, term suitable, IBD supported by several independent seeds) is recorded
once on mexX: `genes/PSEAE/mexX/mexX-notes.md`. MexA is also the seed of the
PTN001249140 GO:0140330 IBD (with AcrA and AcrE), supported here by UniProt IDA
(PMID:25901994).
