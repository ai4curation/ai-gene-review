# PA3677 (mexJ, Q9HXW3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HXW3 --alias PA3677`; accession matches the worklist.
Unreviewed entry; the gene is mexJ, the membrane fusion protein (MFP) of the MexJK RND efflux
system, encoded next to its repressor mexL (PA3678, already reviewed). No deep-research
provider. The seed paper (PMID:12193619) is abstract only; the PubMed MCP returned no full text
for PMC135324, and PubMed and Europe PMC searches failed (HTTP 500/503) during the session.

### Literature

- PMID:12193619 (Chuanchuen et al. 2002), abstract: MexJK effluxes tetracycline and
  erythromycin only with OprM; [PMID:12193619 "Triclosan efflux required neither of the outer
  membrane protein channels tested but necessitated the MexJ membrane fusion protein and the
  MexK inner membrane RND transporter."]
- UniProt Q9HXW3: MFP family (TIGR01730 RND_mfp; PANTHER PTHR30469 MDTA), signal peptide 1-20
  and a lipoprotein lipidation site at Cys21 (PROSITE-ProRule PRU00303), as in MexA, the
  inner-membrane-anchored MFP of MexAB-OprM.

### Annotation decisions

- GO:0046677 response to antibiotic (IMP, IBA): KEEP_AS_NON_CORE, consistent with the efflux
  transporter PA4218 and mexZ reviews.
- GO:0055085 transmembrane transport (IEA): MODIFY to GO:1990961 xenobiotic detoxification by
  transmembrane export across the plasma membrane.
- GO:0022857 transmembrane transporter activity (IEA): MARK_AS_OVER_ANNOTATED; an MFP is a
  periplasmic adaptor that contributes to, but does not itself enable, transport.
- GO:0016020 membrane (IEA): MODIFY to GO:0005886 plasma membrane (lipoprotein anchor plus MFP
  family architecture; two lines agree).
- NEW GO:1990281 efflux pump complex (IC).
- Action counts: KEEP_AS_NON_CORE 2, MODIFY 2, MARK_AS_OVER_ANNOTATED 1, NEW 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002427209 | GO:0046677 response to antibiotic | 2 | 5 (5 taxa) | GO:0046677, IMP, PMID:12193619 | SOUND | The abstract states that triclosan efflux requires MexJ; the MexJK-OprM pump effluxes tetracycline and erythromycin. A resistance phenotype for an efflux component is the conventional basis for this term. | E. coli YbhG (P75777; EcoCyc IDA PMID:27112147, acts_upstream_of_or_within) | Yes |

Node PTN002427209 leaves: YbhG of E. coli and Salmonella, Shewanella SO_1705, Vibrio VC_1659
and PA3677: membrane fusion proteins of efflux systems. The broad process term suits the clade.
No PSEUDOCAP or GO_CENTRAL defects.
