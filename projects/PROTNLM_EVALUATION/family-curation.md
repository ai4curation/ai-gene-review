---
title: "ProtNLM benchmark family curation"
autolink_gene_symbols: false
---

# ProtNLM benchmark family curation

**All 282 selected protein records now have family-level coverage:** 264 map to 210 curated PANTHER families, and the remaining 18 have individual domain/family assessments. An additional SPCS2 family review supplies verified canonical gene context for a short mouse input. The central finding is functional divergence: **129 of the 211 reviewed families are heterogeneous**, with important differences in substrates, catalytic competence, complex roles and cellular context.

[Browse every gene](family-curation/gene-index.md) · [Browse family assessments](family-curation/family-index.md) · [Unassigned inputs and identity checks](family-curation/unassigned-cases.md) · [Download coverage](family-curation/coverage.csv) · [ProtNLM project](../PROTNLM_EVALUATION.md)

## Coverage

The scope includes selected prediction targets, queued cohorts and paired human references. It does not include unselected entries from the larger species censuses. There are **242 distinct prediction-target accessions and 40 paired human references**. Six fly accessions occur in more than one selected tier, giving 288 cohort memberships across 282 distinct protein records.

| Cohort | Memberships |
|---|---:|
| Original ARGO-ProtNLM-50 | 50 |
| Horse benchmark | 40 |
| Paired human references | 40 |
| Fly functional cohort | 41 |
| Fly localization/keyword tier | 29 |
| Additional fly cohort | 20 |
| Pombe functional cohort | 20 |
| Remaining pombe cohort | 8 |
| Neurospora cohort | 20 |
| Human and MOD evolutionary challenge set | 20 |
| **Total memberships** | **288** |

## Functional boundaries worth investigating

| Case | Family-level finding | Useful next comparison |
|---|---|---|
| [ACAD9](family-curation/family-index.md#pthr43884) | Catalytic fatty-acid oxidation and complex-I assembly are context-dependent roles; ECSIT-dependent deflavination makes a simple pseudoenzyme label misleading. | Compare catalytic architecture, FAD state and assembly interfaces with acyl-CoA dehydrogenase relatives. |
| [FTSH12](family-curation/family-index.md#pthr43655) | FTSH12 and FtsHi partners participate in chloroplast import, but their protease competence differs. Dispensability of the FTSH12 zinc-binding site for its essential function does not establish absence of every proteolytic activity. | Separate ATPase, protease and import functions using characterized branches and complete sequences. |
| [FAM20](family-curation/family-index.md#pthr12450) | FAM20A regulatory/pseudokinase, FAM20B sugar-kinase and FAM20C protein-kinase functions occupy different branches. | Test whether a protein-kinase prediction crossed a substrate or catalytic boundary. |
| [PNKD](family-curation/family-index.md#pthr11935) | A glyoxalase-II-related fold does not establish S-lactoylglutathione hydrolysis by PNKD. | Distinguish loss of a particular substrate activity from loss of all possible catalysis. |
| [RlmF/METTL16/PsiM](family-curation/family-index.md#pthr13393) | Even one PANTHER subfamily contains methyltransferases with different substrates. | Establish substrate-specific branches instead of using the subfamily identifier as a sufficient functional rule. |
| [Hsp60/Tcm62](family-curation/family-index.md#pthr45633) | The broad family includes divergent Tcm62; its chaperone-associated functions do not establish the ATP-dependent folding mechanism of Hsp60/GroEL. | Define the ATP-dependent chaperonin branch before granting that activity. |
| [Fly protease homologues](family-curation/family-index.md#pthr24256) | Several selected proteins share protease architecture; cascade participation and noncatalytic regulation must be separated from intrinsic peptidase activity. | Compare complete catalytic regions and experimentally characterized processing substrates. |
| [Spo2/Vps1302](family-curation/unassigned-cases.md) | Spo2 exactly matches the Vps1302 C-terminus, but the records have different PomBase loci. | Resolve transcript, locus and sequence provenance before making an evolutionary or gene-identity claim. |

## Scope of the curated assertions

The reviews contain **213 GO term assessments**: 34 family-wide and 179 with an explicitly unresolved family/subfamily transfer boundary. An unresolved family-wide rule does not mean that a characterized member's function is uncertain. Conversely, an experimentally supported member does not automatically establish a function in every related protein. No restricted grant is encoded as an exhaustive allowed set until the complete applicable branch boundary is established; the reviews retain positive member evidence and divergent examples in their reasons and subfamily descriptions.

Four families include sequence-version-anchored active-site sets with independent controls. Other residue or ancestral-node claims are left unstated when the required alignment, reference or descendant-tree evidence is missing.

**Exact sequences and gene context remain separate.** The short mcm-4, UBE2F and Spcs2 inputs have verified same-gene canonical references, but their PANTHER assignments have not been replaced with those of the longer proteins. SPCS2 is the one additional context-only family; MCM4 and UBE2F context falls in families already represented by other benchmark records. CG45100 is an upstream-ORF microprotein associated with the Hdac3 locus, not evidence for a histone-deacetylase protein.

Evidence includes experimental publications, curated records with explicit evidence codes, domain architecture and reproducible analyses. Generated family descriptions are identifiable in the preserved sources. Family membership is classification evidence; a specific biological grant needs the appropriate functional and evolutionary support. OpenScientist analyses remain substantial evidence where they integrate relevant sequence, structural and experimental results.

## Validation and reproducibility

The [validation report](family-curation/validation-all.json) covers all 211 family reviews: schema validation passes, with **630 successful membership/node/residue checks**, **980 source-reference checks**, and **597 exact supporting-quotation checks**. [Current QuickGO validation](family-curation/validation-go-final.json) checks all 211 reviews against the preserved authoritative responses. The [family–gene cross-check](family-curation/family-gene-crosscheck.txt) finds no conflicts among actionable grants or exclusions; unresolved boundaries are not treated as established agreement. These checks verify structure, identifiers and evidence traceability; they do not replace biological review.

The [scope manifest](family-curation/scope.csv), [exact-accession mapping](family-curation/mapping.csv), [coverage summary](family-curation/coverage-summary.json) and [reproduction instructions](family-curation/README.md) retain cohort and source provenance. All 282 exact UniProt records were retrieved successfully, with six initial requests resolved in a separate retry snapshot. Three cached integrated InterPro links return HTTP 410; those retired-entry responses are preserved and are not treated as functional evidence.
