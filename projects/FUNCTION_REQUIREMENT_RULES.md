---
title: "Function Requirement (NOT) Rules"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [ECOLI, METEA, PSEPK, human]
genes: [ftsI, mdcD, traB, yjdM, kguE]
---

# Function Requirement (NOT) Rules

**Bottom line:** a rule of the form "a protein that enables GO term *T* carries at
least one of these features" lets us say, from sequence features alone, that a
protein lacking all of them is unlikely to enable *T*. Eight pilot rules, tested
against every experimental (ECO:0000269 and descendants) `enables` annotation in
GOA, flag 4% to 6% of the experimentally supported proteins for the four large
rules (683 to 3990 proteins each) and 0 to 11 proteins for the four small ones. Most
flags are themselves annotation problems: non-catalytic subunits annotated
`enables` instead of `contributes_to`, or outright wrong terms. Applied to the GOA
files in this repository, the rules flag 115 rows, and reviewers had already
removed, modified, marked over-annotated or left undecided 85 of them (74%).

## Why

Reviews in this repository argue from absence all the time ("lacks the catalytic
residues", "no transmembrane segment", "no DNA-binding domain"). A scan of
REMOVE, MARK_AS_OVER_ANNOTATED and MODIFY reasons found roughly 880 such arguments
outside protein-binding rows, all written as prose and none checked. The residue-level
version already exists for family reviews (`FunctionRequirement` with
`strength: REQUIRED` in `src/ai_gene_review/schema/family_review.yaml`, checked by
`family_residue_validator.py`). These rules extend the idea to domains, folds and
sequence features, across families.

The pilot came out of [OpenScientist runs](ENZYME_SPECIFICITY.md) on bacterial
misannotations, which kept making the same kind of argument: KguE is a TIM-barrel
isomerase with no Rossmann domain, so it cannot be a phosphogluconate
dehydrogenase; MdcD has the carboxyltransferase fold but is a malonate
decarboxylase subunit with no biotin domains; F-plasmid TraB has no ATPase fold.

## Rules must be specific to a term

General fold rules are false, so every rule names one term and lists every scaffold
known to carry it:

- "A TIM barrel cannot be an NAD(P)-dependent dehydrogenase" is wrong: aldo-keto
  reductases are NADPH-dependent TIM barrels. A rule for all NAD(P)-dependent CH-OH
  oxidoreductases (`GO:0016616`) flagged 151 of 998 experimental proteins
  (isocitrate dehydrogenases, IMP dehydrogenase, iron-dependent alcohol
  dehydrogenases) and was dropped; the rule is kept at phosphogluconate
  2-dehydrogenase.
- "No P-loop means no ATPase" is wrong: actin/Hsp70, GHKL, ATP-grasp, P-type,
  chaperonin and GDA1/CD39 proteins hydrolyse ATP too.
- Multi-subunit enzymes need a qualifier scope. A non-catalytic subunit of a
  complex that has the activity is correctly `contributes_to`, so rules cover
  `enables` rows only. GO also gives `enables` to the peripheral catalytic subunit
  of primary active transporters (SecA, F1/V1 ATPase, complex I), so the
  transporter rule exempts that subtree.

## Files

| What | Where |
|---|---|
| Schema | `src/ai_gene_review/schema/function_requirement_rules.yaml` |
| Rules | `rules/function_requirements/function-requirement-rules.yaml` |
| Checker | `src/ai_gene_review/tools/function_requirements.py` (`just function-requirements acceptance` / `sweep`) |
| Tests | `tests/test_function_requirements.py` |
| Reports | `reports/function-requirements/acceptance.tsv`, `acceptance-summary.tsv`, `sweep.tsv` |

Features are InterPro entries (from UniProt cross-references) and UniProt TRANSMEM
features. The acceptance test fetches experimental annotations from QuickGO and
features from the UniProt REST API, cached under `.cache/function-requirements/`;
the sweep reads only the cached `*-uniprot.txt` and `*-goa.tsv` files and runs in
about 10 s.

## Pilot rules and acceptance results (2026-10-24)

| Rule | Term | Strength | Experimental proteins flagged |
|---|---|---|---|
| FRR:0001 | peptidoglycan glycosyltransferase activity: needs GT51 or SEDS | REQUIRED | 2 / 10 |
| FRR:0002 | acetyl-CoA carboxylase activity: needs biotin carboxylase, BCCP or carboxyltransferase; excluded by malonate decarboxylase beta | REQUIRED | 1 / 20 |
| FRR:0003 | DNA-directed DNA polymerase activity: needs a catalytic polymerase fold | REQUIRED | 11 / 89 |
| FRR:0004 | transmembrane transporter activity: needs a TM segment or membrane beta-barrel/carrier family | REQUIRED | 175 / 3990 |
| FRR:0005 | protein kinase activity: needs a known protein kinase fold | ADVISORY | 132 / 2207 |
| FRR:0006 | ATP hydrolysis activity: needs a known ATPase fold | ADVISORY | 42 / 683 |
| FRR:0007 | phosphonoacetate hydrolase activity: needs the alkaline phosphatase fold | ADVISORY | 1 / 3 |
| FRR:0008 | phosphogluconate 2-dehydrogenase activity: needs an NAD(P)-binding domain | ADVISORY | 0 / 2 |

What the flags on experimental annotations are:

- **FRR:0001.** E. coli FtsI (P0AD68, IDA/IMP; EcoliWiki), a historical attribution
  this repository's review already removes, and human chondroitin sulfate
  N-acetylgalactosaminyltransferase 1 (Q8TDX6, IDA; UniProt), which looks like a
  wrong-term annotation.
- **FRR:0002.** The M. tuberculosis epsilon accessory subunit (P96886, IDA; MTBBASE),
  which should be `contributes_to`.
- **FRR:0003.** Almost all accessory subunits annotated `enables`: E. coli pol III
  theta, chi and psi (EcoCyc), yeast pol delta subunits (SGD), rat pol alpha
  subunit B (RGD), mouse pol gamma-2 (MGI), UmuD. Two are data gaps (a PrimPol-like
  protein with no InterPro entry, a phage replication protein).
- **FRR:0004.** Mainly ABC nucleotide-binding subunits, periplasmic substrate-binding
  proteins, channel accessory subunits (such as voltage-gated calcium channel beta
  subunits) and respiratory complex subunits. Some flags are UniProt entries that
  lack predicted TRANSMEM features.
- **FRR:0005.** Kinase regulatory subunits and cyclins, receptor ectodomain proteins,
  phosphatases, and contested metabolic-kinase moonlighting claims (PGK1, PKM, PEPCK).
- **FRR:0007.** E. coli YjdM (P0AFJ1, IDA), which this repository already marks
  over-annotated.

## Local sweep (2026-10-24)

Flagged GOA rows in `genes/`, by the existing review action:

| Rule | REMOVE | MODIFY | MARK_AS_OVER_ANNOTATED | UNDECIDED | KEEP_AS_NON_CORE | ACCEPT |
|---|---|---|---|---|---|---|
| FRR:0001 | 5 | | | | | |
| FRR:0002 | 1 | | | | | |
| FRR:0003 | 6 | | | | | |
| FRR:0004 | 13 | 22 | 6 | 1 | 2 | 9 |
| FRR:0005 | 8 | 10 | 8 | 2 | 9 | 3 |
| FRR:0006 | 2 | 2 | 2 | | 4 | 3 |
| FRR:0007 | | | 2 | | | |
| FRR:0008 | 1 | | | | | |

The 30 rows kept or accepted are the follow-up list. Several are worth a second
look: V1-ATPase subunits (ATP6V1B1, ATP6V1B2, ATP6V1F) accepted for proton
transmembrane transporter activity, which they do not carry out alone; EQUAS
TGFBR3 (betaglycan, which has no kinase domain) accepted for `GO:0005024`
transforming growth factor beta receptor activity, which GO places under protein
serine/threonine kinase activity, when its own term is the type III receptor activity
`GO:0070123`; and the T7 0.7 protein kinase rows. Others are rule gaps or data gaps:
ManX (a PTS component accepted for the PTS phosphotransferase term, which is a
transporter descendant), zebrafish TRPM7 (a UniProt entry without TRANSMEM features),
and the lambda Nu1 terminase.

## Next steps

- Review the 30 kept or accepted rows listed in `sweep.tsv` and the flagged
  experimental annotations; record real errors as `source_defects`
  (`WRONG_QUALIFIER` for accessory subunits).
- Wire violations into gene review validation as warnings, so a reviewer who
  ACCEPTs a flagged row has to say why.
- Add rules for the other common absence arguments: DNA-binding transcription
  factor activity without a DNA-binding domain, and heme or quinone binding without
  a binding site.
- Link REQUIRED rules to family-review residue sites, so a rule can say "this
  domain, with this residue intact".
