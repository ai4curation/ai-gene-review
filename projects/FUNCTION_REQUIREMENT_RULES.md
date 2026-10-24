---
title: "Function Requirement (NOT) Rules"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [ECOLI, METEA, PSEPK, human]
genes: [ftsI, mdcD, traB, yjdM, kguE, GCH1, AYR1, RAM1, CAD, TGFBR3, HDAC5, MEN1, GPER1, ADRB3, CSGALNACT1, ARHGDIB, TBCC]
---

# Function Requirement (NOT) Rules

**Bottom line:** a rule of the form "a protein that enables GO term *T* carries at
least one of these features" turns the contrapositive into a **lead generator**: a
protein lacking all of them is worth a second look. The rules are a way of finding
candidate misannotations, not a validation gate; a flag is never by itself a reason
to change an annotation. Ten pilot rules were tested against every experimental
(ECO:0000269 and descendants) `enables` annotation in GOA. They flag 4% to 8% of the
experimentally supported proteins for the five large rules (497 to 3984 proteins
each), and most flags are themselves annotation problems: non-catalytic subunits
annotated `enables` instead of `contributes_to`, regulators annotated with the
activity they regulate, or wrong terms. Applied to the GOA files in this repository,
the rules flag 178 rows; reviewers removed, modified, marked over-annotated or left
undecided 149 of them (84%). Seven new full reviews started from rule flags each
confirmed the flag (see [Full reviews from leads](#full-reviews-from-leads)).

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

## Rules and acceptance results (2026-10-24)

| Rule | Term | Strength | Experimental proteins flagged |
|---|---|---|---|
| FRR:0001 | peptidoglycan glycosyltransferase activity: needs GT51 or SEDS | REQUIRED | 2 / 10 |
| FRR:0002 | acetyl-CoA carboxylase activity: needs biotin carboxylase, BCCP or carboxyltransferase; excluded by malonate decarboxylase beta | REQUIRED | 1 / 20 |
| FRR:0003 | DNA-directed DNA polymerase activity: needs a catalytic polymerase fold | REQUIRED | 11 / 89 |
| FRR:0004 | transmembrane transporter activity: needs a TM segment or membrane beta-barrel/carrier/channel family | REQUIRED | 173 / 3984 |
| FRR:0005 | protein kinase activity: needs a known protein kinase fold | ADVISORY | 132 / 2207 |
| FRR:0006 | ATP hydrolysis activity: needs a known ATPase fold | ADVISORY | 41 / 683 |
| FRR:0007 | phosphonoacetate hydrolase activity: needs the alkaline phosphatase fold | ADVISORY | 1 / 3 |
| FRR:0008 | phosphogluconate 2-dehydrogenase activity: needs an NAD(P)-binding domain | ADVISORY | 0 / 2 |
| FRR:0009 | DNA-binding transcription factor activity: needs one of 60 DNA-binding domain families | ADVISORY | 221 / 2759 |
| FRR:0010 | GTPase activity: needs a P-loop or tubulin/FtsZ GTPase domain | ADVISORY | 30 / 497 |

### The transcription factor rule

The DNA-binding domain list was built from the data: starting from the families
most common among the 2759 proteins with experimental `enables` annotations to
`GO:0003700` and its descendants, entries were added (each name checked against
InterPro) until the remaining flags were mostly not transcription factors. Eleven
superfamilies (homeodomain-like, winged helix, C2H2 zinc finger, HLH, bZIP, nuclear
receptor zinc finger, Zn2Cys6, lambda repressor-like, HMG box, p53-like, GATA) cover
79%; the full list of 60 covers 92%.

The remaining 221 flagged proteins mix two kinds:

- **Likely misannotations, worth reviewing:** chromatin enzymes (human HDAC4 and
  HDAC5, IDA/IMP), menin, mediator MED12 (four zebrafish entries, IGI), ribosomal
  protein uS3, alpha-enolase, the lipase ABHD2, yeast FKBP1, and membrane receptors
  given a nuclear activity (GPER1 in human and mouse, the membrane progestin receptor,
  olfactory receptor OR51E2, LRP2, the FemA siderophore receptor).
- **Rule or data gaps:** isoform entries without InterPro matches (zebrafish nuclear
  receptor and AHR isoforms), and transcription factors with non-canonical DNA
  binding, such as NME2 binding the MYC promoter element and CC2D1A.

### The GTPase rule

Of 30 flagged proteins, the clearest leads are the beta-3 adrenergic receptor (human,
mouse, rat; IDA), a GPCR that activates G proteins rather than hydrolysing GTP;
regulators of GTPases (Rho GDI 2, the tubulin-folding cofactor TBCC); and proteins
with no GTPase relationship at all (SEC14L8, an annexin, a sarcoplasmic
calcium-binding protein, methylmalonyl-CoA mutase). G beta and gamma subunits
annotated `enables` should be `contributes_to`.

### Other flags on experimental annotations

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
  subunits) and respiratory complex subunits.
- **FRR:0005.** Kinase regulatory subunits and cyclins, receptor ectodomain proteins,
  phosphatases, and contested metabolic-kinase moonlighting claims (PGK1, PKM, PEPCK).
- **FRR:0007.** E. coli YjdM (P0AFJ1, IDA), which this repository already marks
  over-annotated.

## Local sweep (2026-10-24)

Flagged GOA rows in `genes/`, by the existing review action (after the seven new
reviews below):

| Rule | REMOVE | MODIFY | MARK_AS_OVER_ANNOTATED | UNDECIDED | KEEP_AS_NON_CORE | ACCEPT |
|---|---|---|---|---|---|---|
| FRR:0001 | 6 | | | | | |
| FRR:0002 | 1 | | | | | |
| FRR:0003 | 6 | | | | | |
| FRR:0004 | 12 | 21 | 6 | 1 | 2 | 4 |
| FRR:0005 | 8 | 10 | 8 | 2 | 9 | 1 |
| FRR:0006 | 2 | 2 | 2 | | 3 | 3 |
| FRR:0007 | | | 2 | | | |
| FRR:0008 | 1 | | | | | |
| FRR:0009 | 9 | 32 | 5 | | 1 | 6 |
| FRR:0010 | 4 | 5 | 3 | 1 | | |

HDAC4, RPS3 and ABHD2, which were also on the lead list, already had reviews, and
each flagged row had already been modified or removed.

### Review of the kept or accepted leads

Each flagged row that reviewers had kept or accepted (25 genes, before the rule
fixes below) was looked at again. Outcomes:

| Gene | Flagged row | Outcome |
|---|---|---|
| GCH1 | GTPase activity (IDA) | **Changed to MODIFY → GTP cyclohydrolase I activity**, with a `source_defects` entry. GO defines GTPase activity as GTP → GDP + phosphate; GCH1 makes dihydroneopterin triphosphate and formate. The previous ACCEPT said "not a classical GTPase", so action and reason disagreed. |
| TGFBR3 (EQUAS) | TGF-beta receptor activity, type III | No change; the problem is in GO, which places `GO:0070123` under protein serine/threonine kinase activity although betaglycan has no kinase domain. The review already raises this as a suggested question. |
| AYR1 (yeast) | ligand-gated channel activity (IDA) | No change. The full-text bilayer study reports an NADPH-gated channel, and AYR1 has no transmembrane segment; the existing KEEP_AS_NON_CORE already says it is a single unconfirmed study. |
| RAM1 (MEDTR) | DNA-binding TF activity (IBA, IMP) | No change. The review already notes that direct DNA binding by this GRAS protein is not shown and defers to the curators; whether the GRAS domain binds DNA is an open question. |
| CAD | protein kinase activity (ISS) | No change. The review already addresses the missing kinase fold (autophosphorylation, plausibly by the ATP-grasp domain). |
| PGK1, PCK1, CRY1 | protein kinase activity | No change; contested moonlighting or autophosphorylation claims, already kept as non-core. |
| ATP6V1B1, B2, C1, F | proton transmembrane transporter activity | No change. These V1 subunits also carry the rotational proton-ATPase term, which is in the exempt subtree and implies this parent; the flag is a rule gap. |
| SCHPO asp1, SPAC694.03; mouse Alpl; lambda Nu1 | ATP hydrolysis activity | No change; genuine activities on ATP-grasp, alkaline phosphatase or terminase scaffolds. asp1's RimK-type ATP-grasp was added to the rule. |
| skn-1, atfs-1 (worm); ROF1 (yeast) | DNA-binding TF activity | Rule gaps, fixed by adding the bZIP domain, Skn-1 DNA-binding domain and WOPR (Gti1/Pac2) families. |
| CC2D1A, NME2 | DNA-binding TF activity | No change; experimentally reported non-canonical DNA binding. |
| gbfA (DICDI) | DNA-binding TF activity | Data gap: the UniProt entry has no InterPro matches. |
| T7 0.7 | protein kinase activity | Rule gap, fixed by adding the T7-type protein kinase family. |
| zebrafish trpm7 | channel activity | Data gap (no TRANSMEM features in the entry); fixed by adding the ion transport domain. |
| ECOLI manX | PTS phosphotransferase activity | Rule gap; PTS group translocation is now exempt, as its soluble IIA/IIB components carry `enables`. |

## Full reviews from leads

Seven human genes flagged on experimental annotations were given full reviews
(2026-10-24). Falcon deep research failed with an Edison authentication error, so the
reviews are built from the cached papers and recorded in each gene's notes file. In
every case the flag was right about the term, and the experiment itself stood:

| Gene | Flagged row | Rule | Outcome |
|---|---|---|---|
| ADRB3 | G protein activity (IDA, IEA) | FRR:0010 | MODIFY → beta3-adrenergic receptor activity. The paper shows the receptor driving GTP loading of Gs/Gi, which is receptor (exchange) activity. The same UniProt IDA sits on the mouse and rat orthologs. |
| ARHGDIB | GTPase activity (IMP) | FRR:0010 | MODIFY → Rho GDP-dissociation inhibitor activity; RhoGDI2 holds Rac1 inactive. |
| TBCC | GTPase activity (IDA) | FRR:0010 | MODIFY → GTPase activator activity; TBCC stimulates tubulin GTP hydrolysis through an arginine finger. |
| GPER1 | nuclear estrogen receptor activity (IDA, IBA, IEA) | FRR:0009 | MODIFY → G protein-coupled estrogen receptor activity. The IBA node's placement is sound; the term it carries is not. |
| HDAC5 | DNA-binding transcription activator activity (IMP) and related rows | FRR:0009 | MODIFY → transcription coactivator, coregulator or corepressor activity. The weak intrinsic deacetylase activity is marked over-annotated (class IIa His for the catalytic Tyr). |
| MEN1 | DNA-binding transcription activator activity (IEA from mouse IDA) | FRR:0009 | MODIFY → transcription coactivator activity; menin binds DNA without sequence specificity, as a scaffold for MLL complexes. |
| CSGALNACT1 | peptidoglycan glycosyltransferase activity (IDA) | FRR:0001 | REMOVE. Wrong term and wrong gene: the cited abstract describes an 802-residue chromosome-15 chondroitin synthase (CHSY1); CSGALNACT1 is 532 residues. |

Each review records the upstream errors as `source_defects`, mostly WRONG_TERM for
UniProt, plus CACAO, PINC, ARUK-UCL/BHF-UCL, MGI and GO Central (PAINT). They appear
in `reports/source-defects/`.

## Next steps

- Review the remaining out-of-repository leads: zebrafish MED12, mouse GPER1, the
  membrane progestin and olfactory receptors given TF activity, and the accessory
  subunits annotated `enables` (record those as `WRONG_QUALIFIER`).
- File the accumulated source defects upstream (`just export-source-defects`).
- More rules for common absence arguments: heme or quinone binding without a binding
  site; RNA polymerase or helicase activities; receptor activities without a
  ligand-binding domain.
- Suppress flags on a parent term when the same protein carries an exempt
  descendant (the V1-ATPase case).
- Link REQUIRED rules to family-review residue sites, so a rule can say "this
  domain, with this residue intact".
