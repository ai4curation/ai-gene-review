# AFF1 (P51825) annotation-provenance analysis

Computed by `analyze_aff1_annotations.py`. Every number below is derived by that script from the GOA TSV, UniProt, QuickGO and IntAct; none is hand-entered. Re-run to reproduce.

- GOA rows analysed: **20** (20 distinct)
- Subject: `P51825` / AFF1, 1210 aa, Swiss-Prot

## A. WITH/FROM resolution

| token | rows | kind | resolves to | status | note |
|---|---|---|---|---|---|
| `ARBA:ARBA00026330` | 6 | signature_or_rule | – | – | an automatic-pipeline source, not a protein |
| `FB:FBgn0041111` | 1,2,4,5 | protein | Q9VQI9 AFFL_DROME (lilli, Drosophila melanogaster) | Swiss-Prot | 3 candidate entries |
| `InterPro:IPR007797` | 7 | signature_or_rule | – | – | an automatic-pipeline source, not a protein |
| `InterPro:IPR043640` | 6 | signature_or_rule | – | – | an automatic-pipeline source, not a protein |
| `MGI:MGI:106927` | 1 | protein | P51827 AFF3_MOUSE (Aff3, Mus musculus) | Swiss-Prot | 4 candidate entries |
| `MGI:MGI:1100819` | 1 | protein | O88573 AFF1_MOUSE (Aff1, Mus musculus) | Swiss-Prot | 10 candidate entries |
| `MGI:MGI:1202294` | 4 | protein | O55112 AFF2_MOUSE (Aff2, Mus musculus) | Swiss-Prot | 3 candidate entries |
| `PANTHER:PTN000829417` | 1,2,3,4,5 | panther_node | – | – | an internal PANTHER tree node, not a protein |
| `UniProtKB-SubCell:SL-0191` | 6 | signature_or_rule | – | – | an automatic-pipeline source, not a protein |
| `UniProtKB:P04608` | 9 | protein | P04608 TAT_HV1H2 (tat, Human immunodeficiency virus type 1 group M subtype B (isolate HXB2)) | Swiss-Prot |  |
| `UniProtKB:P42568` | 8,10 | protein | P42568 AF9_HUMAN (MLLT3, Homo sapiens) | Swiss-Prot |  |
| `UniProtKB:P51825` | 1,3 | protein | P51825 AFF1_HUMAN (AFF1, Homo sapiens) | Swiss-Prot | **self-reference: the subject itself** |

## B. Donor evidence for the propagated term

For each (donor, propagated term) pair: what does the donor itself hold? "The source only carries the same family-level inference" is a testable claim, and IBA WITH/FROM lists experimentally-annotated members by construction, so it is usually false.

| donor | propagated term | donor annotations | donor evidence codes | holds the exact term | own experimental evidence |
|---|---|---|---|---|---|
| O55112 Aff2 (Mus musculus) | GO:0050877 | 2 | IBA×1, IMP×1 | yes | **yes** |
| O88573 Aff1 (Mus musculus) | GO:0006355 | 5 | IBA×1, IDA×1, ISO×2, TAS×1 | yes | **yes** |
| P51825 AFF1 (Homo sapiens) | GO:0006354 | 2 | EXP×1, IBA×1 | yes | **yes** |
| P51825 AFF1 (Homo sapiens) | GO:0006355 | 3 | IBA×1, IMP×2 | yes | **yes** |
| P51827 Aff3 (Mus musculus) | GO:0006355 | 6 | IBA×1, IDA×2, IMP×2, TAS×1 | yes | **yes** |
| Q9VQI9 lilli (Drosophila melanogaster) | GO:0003712 | 2 | IBA×1, IMP×1 | yes | **yes** |
| Q9VQI9 lilli (Drosophila melanogaster) | GO:0006355 | 5 | IBA×1, IGI×1, IMP×2, NAS×1 | yes | **yes** |
| Q9VQI9 lilli (Drosophila melanogaster) | GO:0032783 | 3 | IBA×1, IPI×1, NAS×1 | yes | **yes** |
| Q9VQI9 lilli (Drosophila melanogaster) | GO:0050877 | 2 | IBA×1, IMP×1 | yes | **yes** |

## C. Reference-projection test

How many *distinct gene products* does each cited reference annotate, and does the functional term spread across the set or stay on the perturbed gene? Entity counts are distinct id sets, not annotation totals.

| reference | annotations | distinct entities | verdict |
|---|---|---|---|
| PMID:20159561 | 1 | 1 | single-entity: no projection |
| PMID:21729782 | 26 | 17 | 17 entities – inspect per-term spread |
| PMID:22190034 | 183 | 104 | 104 entities – inspect per-term spread |
| PMID:22195968 | 61 | 26 | 26 entities – inspect per-term spread |
| PMID:22547686 | 1 | 1 | single-entity: no projection |
| PMID:23260655 | 8 | 4 | 4 entities – inspect per-term spread |
| PMID:41062835 | 8 | 2 | 2 entities – inspect per-term spread |

### PMID:21729782: 17 entities

| term | entities |
|---|---|
| GO:0005515 None | 17: UniProtKB:A0JLT2, UniProtKB:O00472, UniProtKB:O43513, UniProtKB:O60563, UniProtKB:O60583, UniProtKB:O95402, UniProtKB:P42568, UniProtKB:P50750, UniProtKB:P51825, UniProtKB:P55199, UniProtKB:Q03111, UniProtKB:Q659A1 … |

### PMID:22190034: 104 entities

| term | entities |
|---|---|
| GO:0005515 None | 104: UniProtKB:O00303, UniProtKB:O14734, UniProtKB:O14929, UniProtKB:O15355, UniProtKB:O15371, UniProtKB:O15372, UniProtKB:O15379, UniProtKB:O43324, UniProtKB:O43865, UniProtKB:O60232, UniProtKB:O60518, UniProtKB:O60563 … |

### PMID:22195968: 26 entities

| term | entities |
|---|---|
| GO:0000791 None | 4: UniProtKB:Q659A1, UniProtKB:Q9ESC8, UniProtKB:Q9VQI9, UniProtKB:Q9Y2F5 |
| GO:0003682 None | 2: UniProtKB:Q9VW51, UniProtKB:Q9W1R4 |
| GO:0005515 None | 3: UniProtKB:P55199, UniProtKB:Q659A1, UniProtKB:Q9Y2F5 |
| GO:0005634 None | 3: UniProtKB:Q9ESC8, UniProtKB:Q9VW51, UniProtKB:Q9Y2F5 |
| GO:0005694 None | 1: UniProtKB:Q9ESC8 |
| GO:0008023 None | 17: UniProtKB:O00472, UniProtKB:O96433, UniProtKB:P42568, UniProtKB:P50750, UniProtKB:P51825, UniProtKB:P55199, UniProtKB:Q03111, UniProtKB:Q659A1, UniProtKB:Q7JRJ1, UniProtKB:Q8SZZ8, UniProtKB:Q96CJ1, UniProtKB:Q96JC9 … |
| GO:0015030 None | 2: UniProtKB:P55199, UniProtKB:Q9Y2F5 |
| GO:0032783 None | 10: UniProtKB:A0A0B4KG69, UniProtKB:A1Z7L5, UniProtKB:A1Z7L6, UniProtKB:O17432, UniProtKB:O96433, UniProtKB:Q7JRJ1, UniProtKB:Q8SZZ8, UniProtKB:Q9VF92, UniProtKB:Q9VQI9, UniProtKB:Q9W1R4 |
| GO:0042795 None | 7: UniProtKB:O00472, UniProtKB:O08856, UniProtKB:P55199, UniProtKB:Q9HB65, UniProtKB:Q9VW51, UniProtKB:Q9W1R4, UniProtKB:Q9Y2F5 |
| GO:1905382 None | 5: ComplexPortal:CPX-2710, UniProtKB:Q7JRJ1, UniProtKB:Q8SZZ8, UniProtKB:Q9VW51, UniProtKB:Q9W1R4 |

### PMID:23260655: 4 entities

| term | entities |
|---|---|
| GO:0005515 None | 4: UniProtKB:P42568, UniProtKB:P51825, UniProtKB:Q8TEK3, UniProtKB:Q9HC52 |
| GO:0060090 None | 1: UniProtKB:P42568 |

### PMID:41062835: 2 entities

| term | entities |
|---|---|
| GO:0000785 None | 1: UniProtKB:P51825 |
| GO:0003711 None | 1: UniProtKB:P51825 |
| GO:0005634 None | 1: UniProtKB:P51825 |
| GO:0006974 None | 1: UniProtKB:P51825 |
| GO:0032786 None | 1: UniProtKB:P51825 |
| GO:0032968 None | 1: UniProtKB:P51825 |
| GO:0090734 None | 2: UniProtKB:P09874, UniProtKB:P51825 |

## D. Term relations (fetched, not inferred from labels)

| claim | expected | observed | agrees | why the review needs it |
|---|---|---|---|---|
| is `GO:0008023` an ancestor of `GO:0032783`? | True | True | yes | SEC is a kind of transcription elongation factor complex, so the GO:0008023 IDA is the less precise of the two complex rows |
| is `GO:0032786` an ancestor of `GO:0032968`? | True | True | yes | the Pol II elongation-activation term is a child of the generic one, so the two IMP rows from one reference are parent+child, not independent |
| is `GO:0006355` an ancestor of `GO:0032786`? | True | True | yes | positive regulation of elongation sits under regulation of DNA-templated transcription, so the IBA GO:0006355 row is an ancestor of what the human IMP rows already assert |
| is `GO:0010468` an ancestor of `GO:0006355`? | True | True | yes | regulation of DNA-templated transcription is under regulation of gene expression, so the InterPro2GO GO:0010468 row is the least specific of the regulation rows |
| is `GO:0003712` an ancestor of `GO:0003711`? | False | False | yes | transcription elongation factor activity is NOT under transcription coregulator activity -- the two MF rows are different claims, not a general/specific pair |
| is `GO:0005634` an ancestor of `GO:0000785`? | False | False | yes | chromatin is not part_of nucleus in GO's is_a/part_of closure, so the chromatin and nucleus rows are separate location claims |
| is `GO:0000785` an ancestor of `GO:0090734`? | False | False | yes | site of DNA damage is not under chromatin, so the two damage-associated location rows are not a general/specific pair |
| is `GO:0006355` an ancestor of `GO:0032968`? | True | True | yes | raised by the PR reviewer: GO:0006355 is an ancestor of GO:0032968, so listing both in one core_function's directly_involved_in is redundant by the same logic used to collapse GO:0032786 onto GO:0032968 in the rows |
| is `GO:0006355` an ancestor of `GO:0045668`? | False | False | yes | the osteoblast-differentiation term is NOT under regulation of DNA-templated transcription, so core function 3 may legitimately carry both |

## E. PANTHER node reach

Node `PANTHER:PTN000829417` carries **395** IBA annotations over **79** recipient gene products.

| term | recipients | human recipients under this node |
|---|---|---|
| GO:0003712 | 79 | 4: AFF2, AFF1, AFF3, AFF4 |
| GO:0006354 | 79 | 4: AFF2, AFF1, AFF3, AFF4 |
| GO:0006355 | 79 | 4: AFF2, AFF1, AFF3, AFF4 |
| GO:0032783 | 79 | 4: AFF2, AFF1, AFF3, AFF4 |
| GO:0050877 | 79 | 4: AFF2, AFF1, AFF3, AFF4 |

Full recipient lists are in `results.json` under `node_reach.terms_on_node`; only the count and the human members are shown here (nothing is filtered from the stored data).

Reciprocally, which PANTHER nodes give each term to a **human** gene product. Only nodes reaching AFF-family members are tabulated; the complete node lists, including the many unrelated nodes that supply the generic terms to other families, are in `results.json` under `node_reach.human_iba_holders_by_term`.

| term | total human IBA rows | nodes reaching an AFF gene | AFF recipients |
|---|---|---|---|
| GO:0003712 | 81 | `PANTHER:PTN000829417` (44 nodes total) | AFF2, AFF1, AFF3, AFF4 |
| GO:0006354 | 6 | `PANTHER:PTN000829417` (2 nodes total) | AFF2, AFF1, AFF3, AFF4 |
| GO:0006355 | 192 | `PANTHER:PTN000829417` (60 nodes total) | AFF2, AFF1, AFF3, AFF4 |
| GO:0032783 | 4 | `PANTHER:PTN000829417` (2 nodes total) | AFF2, AFF1, AFF3, AFF4 |
| GO:0032783 | 4 | `PANTHER:PTN002575678` (2 nodes total) | AFF2 |
| GO:0050877 | 4 | `PANTHER:PTN000829417` (1 nodes total) | AFF2, AFF1, AFF3, AFF4 |

## H. Is the true ortholog among the donors?

A paralog donor set is legitimate for IBA, but it means no ortholog-strength inference is available on that row. Mouse `Aff1` (`O88573`) is AFF1's 1:1 ortholog.

| term | donors | ortholog cited? | ortholog's own annotations in that subtree |
|---|---|---|---|
| GO:0003712 | Q9VQI9 fly lilli | **no** | 1 (IBA×1) |
| GO:0006354 | P51825 AFF1 | **no** | 1 (IBA×1) |
| GO:0006355 | Q9VQI9 fly lilli, P51827 mouse Aff3, O88573 mouse Aff1, P51825 AFF1 | yes | 5 (IBA×1, IDA×1, ISO×2, TAS×1) |
| GO:0032783 | Q9VQI9 fly lilli | **no** | 2 (IBA×1, ISO×1) |
| GO:0050877 | Q9VQI9 fly lilli, O55112 mouse Aff2 | **no** | 1 (IBA×1) |

## I. One reference, two levels of precision, split by clade

`PMID:22195968` annotates both `GO:0008023` and the more specific `GO:0032783`. Resolving every recipient's organism shows which clade got which term.

- recipients of the specific `GO:0032783`: 10, organisms Drosophila melanogaster
- recipients of only the general `GO:0008023`: 12, organisms Drosophila melanogaster, Homo sapiens

| recipient | organism / gene | got the specific term? |
|---|---|---|
| `UniProtKB:A0A0B4KG69` | Drosophila melanogaster / ear | yes |
| `UniProtKB:A1Z7L5` | Drosophila melanogaster / Uspl1l | yes |
| `UniProtKB:A1Z7L6` | Drosophila melanogaster / Dmel\CG8229 | yes |
| `UniProtKB:O00472` | Homo sapiens / ELL2 | no |
| `UniProtKB:O17432` | Drosophila melanogaster / Cdk9 | yes |
| `UniProtKB:O96433` | Drosophila melanogaster / CycT | yes |
| `UniProtKB:P42568` | Homo sapiens / MLLT3 | no |
| `UniProtKB:P50750` | Homo sapiens / CDK9 | no |
| `UniProtKB:P51825` | Homo sapiens / AFF1 | no |
| `UniProtKB:P55199` | Homo sapiens / ELL | no |
| `UniProtKB:Q03111` | Homo sapiens / MLLT1 | no |
| `UniProtKB:Q659A1` | Homo sapiens / ICE2 | no |
| `UniProtKB:Q7JRJ1` | Drosophila melanogaster / Eaf | yes |
| `UniProtKB:Q8SZZ8` | Drosophila melanogaster / Ice2 | yes |
| `UniProtKB:Q96CJ1` | Homo sapiens / EAF2 | no |
| `UniProtKB:Q96JC9` | Homo sapiens / EAF1 | no |
| `UniProtKB:Q9HB65` | Homo sapiens / ELL3 | no |
| `UniProtKB:Q9UHB7` | Homo sapiens / AFF4 | no |
| `UniProtKB:Q9VF92` | Drosophila melanogaster / ear | yes |
| `UniProtKB:Q9VQI9` | Drosophila melanogaster / lilli | yes |
| `UniProtKB:Q9VW51` | Drosophila melanogaster / Ell | no |
| `UniProtKB:Q9W1R4` | Drosophila melanogaster / Ice1 | yes |

## F. IntAct records expanded per partner

`NbExp` is not an experiment count -- it has been observed counting sub-methods of one screen, replicates, and even a partner's domains. Distinct publications and distinct detection methods are counted here.

All **104** IntAct records are accounted for: **102** protein records over **43** partner entities, plus **2** records in which the subject appears as its own Ensembl **transcript** paired with an RNAcentral ncRNA (an RNA-RNA record, not a protein interaction of AFF1). The run fails if any record is unassigned; a predicate that silently drops records yields a wrong partner *set* even when the count looks plausible.

Partner entities that are not proteins (a gene id, a fusion construct): `EBI-2620048`, `EBI-2620068`, `EBI-2620075`, `ENSG00000136997`.

Partners supported by **two or more distinct PMIDs**: `O00472`, `P42568`, `P48426`, `P50750`, `Q03111`, `Q96JC9`, `Q9HB65`, `Q9UHB7`.

| partner | name | records | distinct PMIDs | all pub. ids | distinct methods | max MI | subject form |
|---|---|---|---|---|---|---|---|
| `P50750` | CDK9 | 16 | 7 | 16 | 5 | 0.9 | P51825 |
| `Q96JC9` | EAF1 | 5 | 3 | 8 | 1 | 0.64 | P51825 |
| `Q9HB65` | ELL3 | 4 | 3 | 8 | 1 | 0.64 | P51825 |
| `Q03111` | MLLT1 | 9 | 2 | 5 | 3 | 0.6 | P51825 |
| `Q9UHB7` | AFF4 | 8 | 2 | 4 | 3 | 0.6 | P51825 |
| `P42568` | MLLT3 | 7 | 2 | 5 | 5 | 0.73 | P51825 |
| `O00472` | ELL2 | 2 | 2 | 7 | 1 | 0.53 | P51825 |
| `P48426` | PIP4K2A | 2 | 2 | 6 | 1 | 0.53 | P51825 |
| `O60563` | CCNT1 | 8 | 1 | 2 | 3 | 0.53 | P51825 |
| `P53367` | ARFIP1 | 3 | 1 | 2 | 3 | 0.56 | P51825-3 (isoform only) |
| `P04608` | tat | 3 | 1 | 3 | 2 | 0.56 | P51825 |
| `Q9ERL0` | Mllt1 | 2 | 1 | 5 | 1 | 0.35 | P51825 |
| `Q03164-PRO_0000390949` | Q03164-PRO_0000390949 | 2 | 1 | 2 | 1 | 0.35 | P51825 |
| `O95402` | MED26 | 2 | 1 | 2 | 1 | 0.35 | P51825 |
| `Q2Q440` | q2q440_human | 1 | 1 | 2 | 1 | 0.35 | P51825 |
| `Q8TD98` | q8td98_human | 1 | 1 | 2 | 1 | 0.35 | P51825 |
| `EBI-2620048` | mll_aff4_fusion | 1 | 1 | 2 | 1 | 0.35 | P51825 |
| `EBI-2620068` | mll_enl_human_protein | 1 | 1 | 2 | 1 | 0.35 | P51825 |
| `EBI-2620075` | mll_aff4_fusion-1 | 1 | 1 | 2 | 1 | 0.4 | P51825 |
| `Q5NEM9` | q5nem9_fratt | 1 | 1 | 2 | 1 | 0.37 | P51825 |
| `A0A2U2GVV5` | a0a2u2gvv5_yerpe | 1 | 1 | 2 | 1 | 0.37 | P51825 |
| `ENSG00000136997` | myc_human_gene | 1 | 1 | 2 | 1 | 0.35 | P51825 |
| `Q8NCB2-2` | CAMKV | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `Q9DCX1` | Mad2l1bp | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `A2AM29` | Mllt3 | 1 | 1 | 3 | 1 | 0.44 | P51825 |
| `P50750-2` | CDK9 | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `Q8NCB2` | CAMKV | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `Q99PL5` | Rrbp1 | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `Q8TF50` | ZNF526 | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `Q8VE37` | Rcc1 | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `Q8N3E9` | PLCD3 | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `P61328` | FGF12 | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `O95218` | ZRANB2 | 1 | 1 | 2 | 1 | 0.27 | P51825 |
| `O15198` | SMAD9 | 1 | 1 | 5 | 1 | 0.37 | P51825 |
| `O15403` | SLC16A6 | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `P52815` | MRPL12 | 1 | 1 | 3 | 1 | 0.4 | P51825 |
| `Q96T37` | RBM15 | 1 | 1 | 2 | 1 | 0.27 | P51825 |
| `Q9Y3A5` | SBDS | 1 | 1 | 2 | 1 | 0.27 | P51825 |
| `Q9H4G0` | EPB41L1 | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `P12883` | MYH7 | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `Q9Y2J2` | EPB41L3 | 1 | 1 | 3 | 1 | 0.35 | P51825 |
| `Q13547` | HDAC1 | 1 | 1 | 5 | 1 | 0.35 | P51825 |
| `P06748` | NPM1 | 1 | 1 | 2 | 1 | 0.27 | P51825 |

## J. Disorder coverage (computed from the UniProt feature table)

4 `Disordered` REGION features cover **901 of 1210** residues (**74.5%**): 1-45, 73-314, 366-957, 1098-1119. Derived rather than asserted, because a first draft of the review rounded this to "about a thousand", overstating it by ~11%.

## G. affinage recall against the GOA reference set

- affinage citations: **23** (non-numeric PMID-shaped ids: none)
- PMIDs cited by AFF1's GOA rows: **7**
- of those, found by affinage: **0** (0%)
- missed: PMID:20159561, PMID:21729782, PMID:22190034, PMID:22195968, PMID:22547686, PMID:23260655, PMID:41062835

`gates_passed: True` is a statement about **precision** -- that the citations returned are real and correctly quoted. It carries no recall guarantee, and the number above is what recall actually was on the reference set that decides this gene's annotations.
