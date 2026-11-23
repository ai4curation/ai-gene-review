# ccpA (PA4587, P14532) notes

Di-heme cytochrome c551 peroxidase (CCP, EC 1.11.1.5), periplasmic. No deep-research provider
was available; literature search by hand (PubMed metadata for PMID:1657179; cached abstract for
PMID:8591033 fetched with `ai-gene-review fetch-pmid`; QuickGO for the E. coli Ccp seed P37197).

## Literature

- Fülöp et al. 1995 (PMID:8591033; abstract): crystal structure; two class-I cytochrome c-like
  domains each with a covalent heme c; low-potential heme (-330 mV) is the peroxidatic site, the
  high-potential heme (+320 mV) takes electrons from cytochrome c and azurin ["one of them is a
  low-potential (-330 mV) centre where hydrogen peroxide is reduced (the peroxidatic site)"];
  periplasmic, likely peroxide protection ["The enzyme is located in the bacterial periplasm where
  its likely function is to provide protection against toxic peroxides."].
- Ellfolk et al. 1991 (PMID:1657179; abstract only): structure-function study of purified
  Pseudomonas CCP, native enzyme versus elastase two-fragment complex; Lys replaces Met at heme 1
  "thus making peroxidatic activity possible". UniProt cites this paper for EC 1.11.1.5.
- E. coli Ccp (P37197): EcoCyc IDA GO:0004130 and GO:0019645 (PMID:28696311); a quinol
  peroxidase used for H2O2 respiration under anaerobiosis, a different electron donor and
  membrane association from CcpA.

## Review decisions

- GO:0004130 (IBA, IDA, IEA): ACCEPT, core.
- GO:0016491: TOO_GENERAL (entailed by GO:0004130). GO:0009055: MARK_AS_OVER_ANNOTATED
  (internal electron relay is part of the peroxidase reaction). GO:0020037: KEEP_AS_NON_CORE.
- GO:0019645 IBA (PTN002023662, E. coli Ccp sole seed): MARK_AS_OVER_ANNOTATED; respiratory role
  not shown for CcpA. GO:0042743 IBA: MODIFY to GO:0042744 hydrogen peroxide catabolic process.
- GO:0042597, GO:0098869: ACCEPT.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000779264 | GO:0004130 cytochrome-c peroxidase activity | 2 | 44 (17 taxa) | GO:0004130, IDA, PMID:1657179 (PseudoCAP) | SOUND | The term is correct for CcpA (type member of the di-heme CCP family; structure and UniProt-curated EC). Abstract-only: the paper studies the purified enzyme's structure-function; whether activity was assayed in this paper is not visible, but nothing suggests a wrong term. Node term suits a di-heme CCP clade. | E. coli Ccp P37197 (EcoCyc IDA GO:0004130, PMID:28696311) | Yes, on E. coli Ccp |

No PSEUDOCAP or GO_CENTRAL defect.
