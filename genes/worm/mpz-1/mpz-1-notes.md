# mpz-1 review notes

## Session 1 (create review)

- Fetched with `just fetch-gene worm mpz-1`; UniProt G5ECZ8 (TrEMBL,
  unreviewed, PE 1). GOA has 8 rows.
- Papers read: PMID:22363657 (full text), PMID:21110867 (full text, only the
  MPZ-1 sentence is relevant), PMID:35247383 (full text), PMID:40472775 (full
  text, expression only), PMID:20207731, PMID:16890216 and PMID:30417267
  (abstract only; PMC full text of PMID:20207731 could not be retrieved via
  the PubMed MCP or Europe PMC, which returned an error).
- Literature summary is in `mpz-1-deep-research-manual.md` (no provider deep
  research was run).

### Decisions

- GO:0032794 GTPase activating protein binding (IPI, WB, PMID:22363657, with
  RHGF-2/Q22354): the partner is a RhoGEF, not a GAP
  [PMID:22363657 "RHGF-2 GEF activity is specific to RHO-1, the C. elegans RhoA
  homolog"]. The full text was read; nowhere is RHGF-2 described as a GAP. GO
  has no "guanyl-nucleotide exchange factor binding" term, so there is no
  correct sibling to repoint to. REMOVE, with a WRONG_TERM source defect
  (requested_change CHECK) for WormBase. The interaction itself is real.
- Three GO:0005515 protein binding rows (PMID:21110867 Y2H PDZ-array):
  REMOVE per protein-binding policy.
- GO:0030424 axon (IDA, PMID:22363657): ACCEPT; nerve-ring axon localization
  of MPZ-1::tagRFP is in the full text.
- GO:0016020 membrane (IEA, ARBA-derived SubCell): no TM segment; the source
  is an ARBA rule. PDZ scaffolds are peripheral membrane proteins and MPZ-1 is
  synaptic, so the claim is plausible but unproven -> KEEP_AS_NON_CORE.
- GO:0046628 positive regulation of insulin receptor signaling pathway (NAS,
  ComplexPortal): consistent with the abstract of PMID:20207731 -> KEEP_AS_NON_CORE
  (a regulatory role, peripheral to the scaffold activity; full text not seen).
- GO:0062049 protein phosphatase inhibitor complex (NAS, ComplexPortal): the
  abstract supports the ARR-1/MPZ-1/DAF-18 complex; that it inhibits DAF-18 is
  Complex Portal's inference ("probably inhibits"). KEEP_AS_NON_CORE.

### NEW rows (strict bar)

- GO:0031821 G protein-coupled serotonin receptor binding, IPI, PMID:16890216
  (SER-1 binds PDZ10, GST pull-down and co-IP). This is a binding activity of
  MPZ-1 itself, not a process inference.
- GO:0045202 synapse, IDA, PMID:16890216 (punctate GFP-MPZ-1 colocalizing with
  synaptobrevin).
- Not added: any process term for egg laying, serotonin receptor signalling,
  lifespan or locomotion. The SER-1 data (RNAi plus PDZ-ligand dependence) is
  suggestive of positive regulation of SER-1 signalling, but it is RNAi
  phenotype plus binding in an abstract-only paper; left as a question.

### Gaps

- MPZ-1's own activity beyond ligand binding (does it bridge partners?) is
  untested; no structural/biochemical data on the ternary ARR-1/MPZ-1/DAF-18
  arrangement were visible.
