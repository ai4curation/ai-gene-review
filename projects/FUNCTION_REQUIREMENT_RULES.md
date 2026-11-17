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
the rules flagged 285 rows on 2026-11-10; reviewers rejected the flagged term on the
protein in 171 of them (60%) and kept it in 104 (36%), with wide variation between
rules (see [How often a flag is right](#how-often-a-flag-is-right)). Seven new full
reviews started from rule flags each agreed with the flag, but those reviews were
written knowing the flag, so they are not an independent test (see
[Full reviews from leads](#full-reviews-from-leads)).

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
| Reports | `reports/function-requirements/acceptance.tsv`, `acceptance-summary.tsv`, `sweep.tsv`: generated and git-ignored, never committed. They aggregate every review, so committing them makes parallel PRs conflict; regenerate with `just function-requirements acceptance` or `sweep`. The tables on this page are dated snapshots. |

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
annotated `enables` do not hydrolyse GTP; they hold G alpha in the GDP-bound state,
so the term is wrong for them and a qualifier change would not fix it.

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

## How often a flag is right

An earlier version of this page said reviewers "removed, modified, marked
over-annotated or left undecided" 84% of flagged rows. That figure overstated the
agreement in four ways, so it is withdrawn:

- it counted UNDECIDED as agreement;
- it counted every MODIFY, although a MODIFY to a more specific descendant keeps
  the flagged claim (this repository's rule for a correct but general term);
- it was computed after the rules had been amended to stop flagging rows that
  reviewers had kept (skn-1, atfs-1, ROF1, T7 0.7, trpm7, manX, asp1), which
  removes disagreements from the denominator;
- it included the seven reviews written because of a flag.

Recount on 2026-11-10 (`just function-requirements sweep`, 285 flagged rows; each
MODIFY row classed by whether a proposed replacement has the flagged term as an
is_a ancestor in QuickGO):

| Rule | Flagged | Term rejected | Term kept | Open |
|---|---:|---:|---:|---:|
| FRR:0001 | 6 | 6 | 0 | 0 |
| FRR:0002 | 1 | 1 | 0 | 0 |
| FRR:0003 | 20 | 20 | 0 | 0 |
| FRR:0004 | 74 | 41 | 30 | 3 |
| FRR:0005 | 80 | 30 | 48 | 2 |
| FRR:0006 | 17 | 6 | 9 | 2 |
| FRR:0007 | 2 | 2 | 0 | 0 |
| FRR:0008 | 1 | 1 | 0 | 0 |
| FRR:0009 | 60 | 42 | 17 | 1 |
| FRR:0010 | 24 | 22 | 0 | 2 |
| All | 285 | 171 (60%) | 104 (36%) | 10 (4%) |

"Term rejected" is REMOVE (64), MARK_AS_OVER_ANNOTATED (28) and MODIFY to a term
that is not a descendant (79). "Term kept" is ACCEPT (45), KEEP_AS_NON_CORE (30),
MODIFY to a descendant (28) and TOO_GENERAL (1). "Open" is UNDECIDED or PENDING.
The protein kinase rule (FRR:0005) is wrong more often than right, and the
transporter and ATPase rules are close to even; only the narrow rules and the
GTPase rule are reliable as leads. The reviews are not independent of the rules
either: reviewers and rules share the same domain arguments, so even these figures
are an upper bound on precision.

What the rules cannot support, and should not be read as supporting:

- **"Should be `contributes_to`" does not follow from "lacks the catalytic
  domain".** The flag shows the protein does not catalyse the reaction. Whether it
  is a necessary part of a complex that does (`contributes_to`), a regulator, or
  neither is a separate question answered per protein. G beta and gamma subunits
  are the clear case: FRR:0010's own rationale says they regulate GTPases without
  carrying the activity, which argues for a regulator term or removal, not
  `contributes_to`.
- **Peripheral ATPase subunits are treated inconsistently.** FRR:0004 exempts
  primary active transporter terms because their peripheral catalytic subunit
  (SecA, F1/V1) correctly carries `enables`, while this page lists ABC
  nucleotide-binding subunits among the misannotations. An ABC ATPase subunit is
  the same kind of subunit. It is flagged only when annotated to a term outside
  the exempt subtree, and then the right fix is usually the ABC-type term, not a
  qualifier change.
- **REQUIRED rests on a claim that no other family exists.** FRR:0001 names the
  "two known" peptidoglycan polymerase families. SEDS proteins were recognised as
  polymerases only in 2016; the same rule written earlier would have flagged FtsW
  and RodA. A REQUIRED flag on an experimental annotation is a reason to read the
  paper, never a verdict.
- **FRR:0007 and FRR:0008 are untested.** They were written from one case each
  and have three and two experimental proteins to test against. FRR:0008 asserts
  for one term the inference ("NAD(P)-dependent, so Rossmann fold") that failed
  for 151 of 998 proteins at the parent term.
- **FRR:0009's coverage is in-sample.** Its domain list was extended until the
  remaining flags "were mostly not transcription factors", on the same 2759
  proteins the 92% coverage is measured on.

## Local sweep (2026-10-24)

The table below is the 2026-10-24 snapshot and predates the recount above.

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
every case the review agreed with the flag about the term, and the experiment itself
stood. The reviews were started from the flags, so this is consistency, not
confirmation:

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
