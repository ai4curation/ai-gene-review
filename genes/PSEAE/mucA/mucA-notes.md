# mucA (PA0763, P38107) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P38107 --alias mucA`; accession matches the worklist.
Reviewed (Swiss-Prot) entry. No deep-research provider was used. Literature from the cached
papers; PubMed and Europe PMC searches failed (NCBI eutils HTTP 500, Europe PMC 503) during
this session. Read with the algU, mucB and fpvR/PA0471/foxR reviews for consistency.

### Literature

- PMID:8759866 (Schurr et al. 1996), abstract only in cache: [PMID:8759866 "MucA was shown to
  act as an anti-sigma factor by binding to AlgU and inhibiting its activity."]
- PMID:19226327 (Wood and Ohman 2009), abstract: [PMID:19226327 "MucA sequesters
  extracytoplasmic function (ECF) sigma(22) (algT/U encoded) from target promoters including
  PalgD for alginate biosynthesis."]; cell wall stress triggers AlgW then YaeL cleavage (RIP).
- PMID:19298369 (Cezairliyan and Sauer 2009), full text: [PMID:19298369 "proteolytic cleavage
  of MucA, a transmembrane protein that inhibits the transcription factor AlgU"]; MucB binding
  blocks AlgW cleavage.
- PMID:22842599 (Pulcrano et al. 2012), abstract only: mucA mutations in CF isolates and algU
  expression.
- UniProt P38107: RseA family, RseA_N (PF03872) and RseA_C (PF03873), TM helix 89-105;
  structures 6IN7/8Z6G (residues 1-80) and 6IN9/6JAU (106-194).

### Annotation decisions

- GO:0016989 sigma factor antagonist activity: IBA, IEA, IMP all ACCEPT (core).
- GO:0045892 (IEA): MODIFY to GO:2000143 (as on fpvR, PA0471, foxR).
- GO:0032885 regulation of polysaccharide biosynthetic process (IMP): KEEP_AS_NON_CORE; GO has
  no negative-regulation child.
- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0005515 protein binding x3 (MucB x2, AlgW): REMOVE per the protein-binding policy.
- Action counts: ACCEPT 4, MODIFY 1, KEEP_AS_NON_CORE 1, REMOVE 3.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002211401 | GO:0016989 sigma factor antagonist activity | 2 | 8 (8 taxa) | GO:0016989, IMP, PMID:22842599 | SOUND | Truncating mucA mutations in CF isolates derepress algU (autoregulated) and alginate genes: the standard derepression evidence for an anti-sigma factor; direct binding and inhibition in PMID:8759866. | E. coli RseA (P0AFX7; EcoCyc IMP PMID:9159522, ComplexPortal IPI) | Yes |

MucA is not on PTN001250434 (the FecR-family node of fpvR, PA0471, foxR); its node is the
RseA family. Leaves (`.cache/paint/leaf.gaf.gz`): RseA of E. coli, Salmonella, Yersinia,
Haemophilus, Shewanella, Vibrio and Xanthomonas XCC1268, plus MucA. All are RseA-family
anti-sigma-E factors, so the node term suits the clade. No PSEUDOCAP or GO_CENTRAL defects.
