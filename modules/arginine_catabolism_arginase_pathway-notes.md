# Arginase/OAT catabolism: comparative audit

## 2026-10-26 — boundary and evidence

The module covers arginine hydrolysis, ornithine transamination, and alternative disposal of glutamate semialdehyde/P5C. Eukaryota is an envelope for demonstrated yeast, Arabidopsis and human implementations, not a claim of universal occurrence, localization or flux. The review panel comprises eleven budding/fission yeast proteins, three human proteins and four Arabidopsis proteins (eighteen unique representatives). The complete panel is being reviewed individually; initial fungal validation preserves 185 original rows without additions.

The comparative search used arginase/OAT/arginine catabolism with plant, yeast and cross-species terms. Normally fetched PubMed/PMC caches include reviews PMID:28272331, PMID:41887919, PMID:26284079, PMID:39952693 and PMID:29412048. Additional general reviews PMID:27934648 and PMID:37358082 were consulted but add little to the module's specific reaction claims. No manually written text is represented as provider-generated research. Actual member provider failures and manual replacement research are recorded in the gene notes.

## Reference appraisal and mined findings

- **PMID:28272331 (2017 OAT review): high relevance.** The comparative localization section distinguishes demonstrated cytosolic OAT in Neurospora and budding yeast from inference in other fungi. Its discussion of mammalian intestinal synthesis prevents treating OAT expression as proof of net catabolism. The module uses the catabolic reaction direction conditionally.
- **PMID:41887919 (2026 human OAT review): high mechanistic relevance, limited comparative coverage.** Reversible PLP chemistry and spontaneous GSA/P5C equilibration are useful. Its broad fungal statement does not establish every fungal route. The new review does not replace direct human enzyme measurements (PMID:28345116).
- **PMID:26284079 (2015 plant arginine review): high relevance for nitrogen remobilization and compartment boundaries.** Carrier expression and physiological contribution are explicitly condition dependent. Its overview is corroborated by Arabidopsis OAT and P5CDH experiments. Generalized statements about yeast biosynthesis are not used here.
- **PMID:39952693 (2025 arginase review): high relevance for ARG1/ARG2 boundaries and mammalian comparisons.** It explicitly warns of human/rodent differences. Immune, vascular and tissue phenotypes are not converted into invariant catalytic-module steps.
- **PMID:29412048 (2018 arginase review): useful mammalian background, a specific comparative passage is unsuitable.** Its statement that most bacteria, plants and yeasts possess one mitochondrial ARG2 cannot support the module: bacteria lack mitochondria, fission yeast has two functionally demonstrated arginases, and Arabidopsis has ARGAH1/ARGAH2. The module records this source limitation rather than propagating it.

## Primary evidence and scope corrections

PMID:6997271 and PMID:7009582 demonstrate the budding-yeast proline detour and separation of the reductase and dehydrogenase compartments. They do not demonstrate a compulsory detour in all fungi. PMID:12620851 tests anaerobic budding yeast and an engineered bypass: deleting PRO3 and URE2 and expressing targeting-sequence-deleted PUT2 permits recovery of the fourth arginine nitrogen. That construct is not endogenous cytosolic PUT2. PMID:3125423 distinguishes oxygen-regulated expression from respiratory competence; high PUT1 expression persists in rho-minus cells. Molecular oxygen is not represented as the direct quinone-linked enzyme substrate.

PMID:32978391 identifies Put6/Put7 as regulators and still describes the mitochondrial proline transporter as unknown. It also discusses exchange between P5C/proline pools, so compartmentation is not described as an absolute prohibition on cycling. No carrier identity is invented from regulatory mutant phenotypes.

The old assertion that fission yeast lacks an ornithine-carbamoyltransferase-dependent route was wrong. PMID:26075619 explicitly proposes Arg3-dependent arginine re-synthesis to explain isotope pre-peaks, and reports their elimination in car1/aru1 double mutants. The isotope observations and the proposed detailed flux mechanism are kept distinct. PomBase GO:0000050 is not rejected merely because fission yeast is not a mammalian ureotelic organism. PMID:20435771 further distinguishes iron-repressed car1 from constitutive car3/aru1, so the paralogs are not physiologically interchangeable in every condition.

PMID:1939179 measured a catalytic Mn site and a predominantly Zn structural site in purified yeast CAR1. The module therefore does not assert identical binuclear-Mn occupancy across all arginases. Plant ARGAH1 has direct Mn-containing structural evidence (PMID:32754173). ARGAH2 arginine hydrolysis has independent recombinant-enzyme evidence (PMID:35752016). Additional agmatinase activity in PMID:28716421 supports another pathway; its Nicotiana transient chloroplast localization and proposed stress flux are not evidence for universal native plastid arginine catabolism.

PMID:18419821 localizes Arabidopsis OAT to mitochondria and demonstrates failure to use supplied arginine or ornithine as nitrogen after OAT loss, while stress-induced proline accumulation remains intact in the tested conditions. PMID:11532180 identifies plant P5CDH by yeast complementation and mitochondrial targeting; PMID:15548746 establishes native proline degradation and sensitivity to arginine/ornithine in p5cdh mutants. These support catabolic convergence, with direct Arabidopsis matrix sublocalization and NAD-versus-NADP kinetics kept separate from findings in other plants.

Human ARG2 import is directly assayed in PMID:8898077; murine macrophage induction in the same paper is not relabeled as human evidence. Human OAT catalytic dimers are demonstrated in PMID:28345116, replacing obligatory-hexamer language in its gene review. Human ALDH4A1 catalysis and mutant inactivation are demonstrated in PMID:22516612; high-resolution ligand structures in that paper use mouse protein. These primary sources replace circular citations to gene review YAMLs.

## Families, chemistry and verification

The arginase step has alternatives for PTHR43782 (fungal/animal) and PTHR11358 (plant arginase/agmatinase). Direct mitochondrial P5CDH has distinct PTHR14516 and PTHR43521 implementations. Official family names are preserved verbatim; the PTHR43521 label names another aldehyde-dehydrogenase activity, so required-function and representative constraints are essential. OAT, P5C reductase, proline dehydrogenase and fungal P5CDH retain their existing family selectors pending refreshed member-index checks. No ancestral PTN placement is inferred from a family label.

All four module connections now carry source evidence. The two root edges are metabolic continuity assertions and therefore VERIFIED, not NOT_APPLICABLE: that enum is not restricted to CoA carriers. The OAT output is open-chain semialdehyde; the reductase uses equilibrating P5C while P5CDH consumes the aldehyde. Spontaneous interconversion is not assigned to a fabricated enzyme. Charged ChEBI labels follow the ontology, with readable chemical names retained in preferred_term; the PUT1 quinone/quinol identifiers match its curated Rhea:23784 reaction.

Schema validation passed after the structural edits. Initial grounding validation passed with expected unfinished-member, missing-local-index and chemical-label advisories. Chemical labels were reconciled only after checking the reaction identities; the PANTHER member index is being refreshed. Final member integration, module QA, complete validation and a dedicated PR remain outstanding.


## Independent integration QA — 2026-10-26

Read the module against the eighteen current individual reviews, cached primary
papers and comparative reviews, and all three cited cached GO-CAM models. The
selected enzyme activities match the member cores. All eight PANTHER selectors
pass official-label/member validation using the refreshed local index. In
particular, PTHR11358 is the plant arginase/agmatinase family and PTHR43521
contains plant P5CDH despite its official alpha-aminoadipic-semialdehyde name.
The required molecular functions remain necessary restrictions; neither family
name licenses unreviewed substrate promiscuity. The two remaining
`FAMILY_FUNCTION_UNREVIEWED` advisories concern family-level adjudication of
these plant activities, not missing member evidence or mismatched accessions.

All four metabolic connections have suitable evidence with the stated limits:
budding-yeast genetics establishes the proline detour, Arabidopsis OAT and P5CDH
mutants support catabolic convergence, and human coupling denotes compatible
mitochondrial chemistry rather than tissue-independent measured flux. Fission
yeast has direct arginine-to-proline conversion but the complete compulsory
shuttle remains a comparative inference. Neither molecular oxygen as Put1's
immediate acceptor nor an identified mitochondrial proline carrier is asserted.
The OAT intestinal reverse reaction, ARGAH agmatinase chemistry, urea disposal,
arginine re-synthesis and epiarginase regulation remain outside the catalytic
chain. Retain the distinction between partial isotope-conversion suppression
and the proposed detailed recycling mechanism.

Strengthened the evidence without changing reactions, family selectors,
representatives, route logic or GO-CAM links:

- Added already normally cached PMID:20450881 at PUT1: purified yeast Put1p
  accepts ubiquinone-1, supporting the quinone-linked reaction independently of
  expression or respiratory phenotypes.
- Added already normally cached PMID:3025596 at PUT2: native enzyme matrix
  localization was tested by mitochondrial fractionation and substrate latency;
  imported fusion experiments are separate corroboration. This improves the
  earlier "presumably mitochondrial" fractionation evidence.
- Replaced weak quotation fragments with source text directly addressing OAT
  mutant nitrogen utilization, the unknown mitochondrial proline transporter,
  transient Nicotiana ARGAH localization and the plant nitrogen-remobilization
  hypothesis. Qualified car1/aru1 deletion as preventing virtually all measured
  conversion, and PRO1/PRO2 growth as consistent with the proposed P5C supply.

The cached SGD GO-CAMs contain exactly the stated CAR1/CAR2/PRO3 and PUT1/PUT2
activities, including their imported cytosol placements. Primary mitochondrial
localization evidence appropriately governs the module's PUT1/PUT2 locations.
The PomBase model identifies the stated car1 and aru1 nodes as GO:0004053,
cytosolic and part of GO:0000050, car2 as cytosolic GO:0004587, and put1/put2 as
mitochondrial-matrix activities. Its interpretation is preserved rather than
rejecting the urea-cycle term on non-ureotelic taxonomy. Both live YeastPathways
URLs were inaccessible through the web tool during this QA; cached GO-CAM
assertions were verified directly, and the historical pathway-import note is
not presented as a fresh live-site observation.

Fourteen Boolean checks pass: empty context fails; complete human and plant
direct routes pass; the budding-yeast proline endpoint and full shuttle pass;
the shuttle without reductase fails; either fission-yeast arginase can supply
the complete inferred route, while an unsupported fission-yeast-only endpoint
does not pass the representative-accession check. Omitting any of arginase,
OAT or disposal fails. These tests concern the represented activity requirements,
not proof of expression, flux, oxygen state or transport in a particular sample.

Final module retains three top-level required parts, nine annotons, four
supported connections, eighteen unique protein representatives and three
GO-CAM models. It now has 34 top-level source entries (30 PubMed papers) and
56 literal-quote occurrences (24 distinct source/quote pairs). Focused schema,
grounding and quote checks passed; rendering and the complete module-logic test
file are recorded with final results in the helper-created integration history.
Machine-readable evidence and route-check reports are in
`.cache/module-audit-logs/arginase-module-independent-evidence.json` and
`arginase-module-independent-logic.json`. No gene, tracker or source-cache
content was edited in this integration QA.
