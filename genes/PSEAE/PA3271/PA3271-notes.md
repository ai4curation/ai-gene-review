# PA3271 (mxtR, Q9HYX0) notes

## Literature

No deep-research provider was available. PubMed E-utilities returned HTTP 500
on 2026-11-05. The cached publications were searched for MxtR/PA3271, and only
PMID:22168309 (abstract only) was found.

- MxtR is an orphan sensor kinase that modulates AQ production [PMID:22168309
  "AQ production is modulated by an orphan P. aeruginosa sensor kinase"].
- The mutant induces MexT and MexEF-OprN, which delays AQ biosynthesis gene
  expression.
- In vitro autophosphorylation is inhibited by ubiquinone [PMID:22168309
  "autophosphorylation of MxtR was inhibited by ubiquinone, the central
  electron carrier of respiration in in vitro experiments"].
- Domain content (UniProt InterPro/Pfam/SMART): SSF symporter-family 13-TM
  domain, PAS-like, HisKA (His808), HATPase_c, REC (Asp1090). There is no HPt
  domain.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001976860 | GO:0000155 phosphorelay sensor kinase activity | 3 | 330 (86 taxa) | GO:0000155, IDA, PMID:22168309 (PseudoCAP) | SOUND | The abstract states outright that MxtR autophosphorylation was assayed in vitro and inhibited by ubiquinone. That is direct kinase evidence with a sensory input; HisKA/HATPase/REC architecture is intact. | M. tuberculosis SenX3 P9WGK5 (IDA); P. aeruginosa RpfC PA1611 Q9I3B1 (IDA, PMID:16182517; see genes/PSEAE/PA1611) | Yes. SenX3 alone grounds the node, and PA1611 is also sound. No PSEUDOCAP or GO_CENTRAL defect for this term. |

Node-level issue on another term: PTN001976860 also carries an IBD for
GO:0009927 histidine phosphotransfer kinase activity (seeds RcsD P39838, with an
HPt domain, and SGD:S000001409). It reaches MxtR, which has no HPt domain.
The IBA row is REMOVE here. The single GO_CENTRAL defect (PROBABLE) is
recorded on PA1611 (`genes/PSEAE/PA1611`), which shares the node and the
problem; this review cross-references it and does not duplicate it.

## Other decisions

- GO:0022857 and GO:0055085 (SSF-domain transport): MARK_AS_OVER_ANNOTATED.
- GO:1900376 regulation of secondary metabolite biosynthesis (IMP):
  KEEP_AS_NON_CORE, an indirect effect through MexT.
- GO:0004673, GO:0007165, GO:0016020, GO:0016301, GO:0016740, GO:0016772:
  TOO_GENERAL.
