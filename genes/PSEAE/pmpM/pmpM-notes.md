# pmpM (PA1361, Q9I3Y3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I3Y3 --alias pmpM`; accession matches the worklist.
Reviewed (Swiss-Prot) entry. No deep-research provider; PubMed and Europe PMC searches failed
(HTTP 500/503) during the session. The seed paper PMID:14679249 is cached with full text and
was read in full.

### Literature

- PMID:14679249 (He et al. 2004), full text: pmpM cloned into drug-hypersensitive E. coli KAM32
  raises MICs of fluoroquinolones, benzalkonium chloride, ethidium, TPP and others;
  energy-dependent ethidium efflux is Na+-independent; in everted membrane vesicles benzalkonium
  drives H+ efflux [PMID:14679249 "Addition of benzalkonium chloride to the assay mixture caused
  efflux of H + , indicating that H + -benzalkonium chloride antiport took place."]. Deleting
  pmpM in the Mex-deficient strain PMX52 lowers MICs of benzalkonium, ethidium, acriflavine and
  TPPCl. No localization, fractionation or topology experiment is reported; the only
  membrane-related data are transport assays in E. coli everted membrane vesicles.
- UniProt Q9I3Y3: MATE family (TIGR00797, PF01554 x2), 12 predicted transmembrane helices;
  Swiss-Prot location cell inner membrane, multi-pass (ECO:0000250).

### Annotation decisions

- GO:0005886 plasma membrane (IDA, IEA): ACCEPT. The IDA rests on H+/drug antiport measured in
  everted (inner) membrane vesicles of E. coli expressing pmpM; together with 12 TM helices.
- GO:0098567 periplasmic side of plasma membrane (IDA): REMOVE, PSEUDOCAP WRONG_TERM defect
  (CONFIRMED; full text read).
- GO:0016020 membrane (IBA, IEA): TOO_GENERAL (plasma membrane accepted, is_a membrane).
- GO:0042910 xenobiotic transmembrane transporter activity (IBA, IEA): ACCEPT.
- GO:0015297 antiporter activity (IEA): MODIFY to GO:0140968 polyspecific organic
  cation:proton antiporter activity (substrates are organic cations; H+ coupling shown).
- GO:0042908 xenobiotic transport (IEA): MODIFY to GO:1990961 xenobiotic detoxification by
  transmembrane export across the plasma membrane.
- GO:0055085 transmembrane transport (IEA): TOO_GENERAL (GO:1990961 in core_functions entails it).
- GO:0046677 response to antibiotic (IBA): KEEP_AS_NON_CORE.
- Action counts: ACCEPT 4, MODIFY 2, TOO_GENERAL 3, KEEP_AS_NON_CORE 1, REMOVE 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000129144 | GO:0016020 membrane | 19 | 2231 (102 taxa) | GO:0005886 plasma membrane, IDA, PMID:14679249 | SOUND | H+/benzalkonium antiport measured in everted inner-membrane vesicles of E. coli expressing pmpM; a membrane location of the transporter follows, and the node term is broader still. | 18 others: E. coli MdtK (P37340), human MATE1/MATE2-K (Q96FL8, Q86VL8), mouse and rat MATEs, 12 Arabidopsis DTX/MATE proteins | Yes |
| PTN000129144 | GO:0016020 membrane | 19 | 2231 (102 taxa) | GO:0098567 periplasmic side of plasma membrane, IDA, PMID:14679249 | WRONG | No sidedness or topology experiment in the paper; PmpM is a 12-helix integral membrane protein spanning both leaflets. The row adds nothing the plasma membrane row does not, and its term is wrong. | as above | Yes |

The membrane IBD at the MATE-family root (2231 leaves) is supported by many independent
experimental seeds across bacteria, plants and mammals, and membrane is a term that suits every
MATE transporter. No GO_CENTRAL defect. One PSEUDOCAP defect (GO:0098567, CONFIRMED).
