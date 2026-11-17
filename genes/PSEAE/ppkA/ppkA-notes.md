# ppkA (PA0074, Q9I758) notes

## Literature

No deep-research provider was available. PubMed MCP and E-utilities returned
errors on 2026-11-05, and PMC107787 (PMID:9852028) returned no body text. The
cached publications were searched for PpkA: PMID:9852028 (abstract),
PMID:17558395 (abstract), PMID:19400797 (full text), PMID:20114026 and
PMID:31208722 (context).

- PpkA is a Hanks-type Ser/Thr kinase homolog, induced in infection and
  required for full virulence [PMID:9852028 "A ppkA null mutant strain shows
  reduced virulence in neutropenic mice compared to the wild type."].
- The seed paper's kinase evidence is an in vivo catalytic-site mutant
  [PMID:9852028 "a single amino acid change at the catalytic site of the kinase
  domain eliminated the toxic effect of PpkA on bacterial cells, suggesting that
  the kinase domain of PpkA is functional within bacterial cells"].
- PpkA phosphorylates Fha1 and triggers H1-T6SS; PppA antagonises
  [PMID:17558395 "PpkA activity is antagonized by PppA, a Ser-Thr phosphatase."].
- In vitro kinase activity on Fha1 [PMID:19400797 "This reaction is efficiently
  catalyzed in vitro by the kinase domain of PpkA (Mougous et al., 2007)."].
- Autophosphorylation sites Thr158/Thr161; dimerisation of the extracellular
  domains activates; TagR acts upstream (PMID:19400797).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001981567 | GO:0004674 protein serine/threonine kinase activity | 17 | 353 (73 taxa) | GO:0004674, IDA, PMID:9852028 (PseudoCAP) | INDIRECT-PHENOTYPE | The cited abstract infers kinase function from an in vivo catalytic-site mutant (overexpression toxicity), not from a kinase assay. The term is right: in vitro Fha1 phosphorylation and autophosphorylation are shown elsewhere (PMID:17558395, PMID:19400797). Row kept; evidence code questioned at SUSPECTED (full text not available), as for parS/parR. | M. tuberculosis PknA-L paralogs (P9WI81, P9WI79, P9WI67, P9WI65, P9WI75, P9WI77, P9WI83, P9WI71), B. subtilis PrkC O34507, human NEK6 Q9HC98, NEK7 Q8TDX7, MAP3K20 Q9NYL2, Plasmodium Q8I629, rat RGD:1311160, mouse MGI:1289156, worm WBGene00008956 | Yes. Many seeds are directly assayed Ser/Thr kinases; the generic term suits a Hanks-kinase node. No GO_CENTRAL defect. |

PSEUDOCAP defect: one WRONG_EVIDENCE_CODE, SUSPECTED. pppA (PA0075) is the
cognate phosphatase and is reviewed separately; it is not on this node. parS
and parR are two-component proteins on different nodes, so no consistency
issue arises.

## Other decisions

- GO:0050714 positive regulation of protein secretion (IDA): ACCEPT; no
  T6SS-specific regulation term exists.
- NEW GO:0005886 plasma membrane (IC): type II TM topology plus
  periplasmic-dimerisation activation.
- GO:0000166, GO:0004672, GO:0016301, GO:0016740: TOO_GENERAL.
