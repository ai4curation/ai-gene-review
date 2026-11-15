# SLC38A4 (SNAT4 / ATA3 / NAT3) — curation notes

UniProt: Q969I6 (S38A4_HUMAN), 547 aa, 11-TM multi-pass membrane protein.
Family: amino acid/polyamine transporter 2 family; SLC38 (System N/A) gene family.
PANTHER: PTHR22950:SF222 (SODIUM-COUPLED NEUTRAL AMINO ACID TRANSPORTER 4).

No deep-research-*.md provider file was present; these notes synthesize the cached
publications and the curated UniProt record.

## Core function

System A-like sodium-coupled neutral amino acid transporter, liver-enriched, also
expressed in placental syncytiotrophoblast.

- Na+-coupled, electrogenic, pH-dependent symport of small **neutral** amino acids;
  partially tolerates Li+ substitution for Na+.
  [PMID:11414754 "hNAT3 is a Na(+)- and pH-dependent, low-affinity transporter and partially tolerates substitution of Na(+) by Li(+)"]
- Strongest activity for L-alanine.
  [PMID:11414754 "the strongest transport activities were specific for l-alanine"]
- Substrate preference (UniProt FUNCTION): glycine, L-alanine, L-serine, L-asparagine,
  L-threonine, then L-cysteine, L-histidine, L-proline, L-glutamine, L-methionine.
- Direct LC-MS / radiolabel confirmation of neutral substrates:
  [PMID:33928121 "LC-MS analysis confirmed glycine, alanine, serine, threonine and glutamine as SNAT4 substrates"]
  [PMID:33928121 "[14C]-alanine and [14C]-glycine were confirmed as substrates of SNAT4"]

## Distinction from other System A / System N transporters

- **MeAIB-INSENSITIVE** and **low affinity for MeAIB**, unlike SNAT1/SNAT2 (System A).
  [PMID:11342143 "hATA3 also differs from hATA1 and hATA2 in exhibiting low affinity for MeAIB"]
- Liver-specific; provides major route for hepatic arginine uptake (per the original
  report).
  [PMID:11342143 "expressed almost exclusively in the liver"; "ATA3 is likely to provide the major route for the uptake of arginine in this tissue"]

## Cationic amino acid transport — DISPUTED (UniProt CAUTION)

- Original report: Na+-INDEPENDENT transport of cationic amino acids (arginine, lysine),
  with higher affinity than for neutral AAs (KM 0.3 mM arginine).
  [PMID:11342143 "mediates ... the transport of cationic amino acids in a Na(+)-independent manner. The affinity of hATA3 for cationic amino acids is higher than for neutral amino acids"]
- Recent quantitative refutation: no substantial cationic accumulation detected.
  [PMID:33928121 "we could not detect substantial accumulation of cationic amino acids by SNAT4 and ATB0,+ in contrast to previous reports"]
  [PMID:33928121 "Using [14C]-arginine we were also unable to detect SNAT4-mediated uptake above levels seen with un-injected oocytes"]
- UniProt flags this as a CAUTION (disagreement between Hatanaka and Fairweather).
- Consequence for review: L-arginine transporter-activity (GO:0061459) and
  L-arginine transmembrane transport (GO:1903826) IEA rows (transferred from mouse
  Q8R1S9) are treated as MARK_AS_OVER_ANNOTATED for the human protein given the
  explicit dispute and the recent failure to reproduce.

## Localization

- Cell (plasma) membrane, multi-pass.
  [PMID:11414754], [PMID:16148032]
- Placental syncytiotrophoblast microvillous (and basal) plasma membrane.
  [PMID:16148032 "SNAT4 is localized to the microvillous and basal plasma membranes of the syncytiotrophoblast"]
  [PMID:19015196 — functional in human placental microvillous plasma membrane]
- Topology / glycosylation at Asn-260, Asn-264 [PMID:21917917].

## Physiology

- Placental System A has an essential role in fetal neutral amino-acid supply.
  [PMID:16148032 "In the placenta, system A has an essential role in the supply of neutral amino acids needed for fetal growth"]
- SNAT4 mRNA higher early first trimester; protein higher at term.
  [PMID:16148032]
- (Background) SLC38A4 is an imprinted gene in mouse with a role in fetal/placental
  growth; not directly assayed in the cached human papers.

## Protein interaction

- GJA8 (P48165) reported as a binary Y2H hit in the HuRI reference interactome
  [PMID:32296183]. Uninformative generic protein binding → REMOVE per project policy.
