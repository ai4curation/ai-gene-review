# PR #6144 review follow-up

Reviewed head: `6342c397981015f8463fd8c09a4c64d96d1a3ffc`. The annotation-reviewer and aigr-pr-review skills and repository CLAUDE guidance were applied to all six findings in the [changes-requested review](https://github.com/ai4curation/ai-gene-review/pull/6144#issuecomment-6698960408). No annotation action, original annotation payload, or row order changes in this follow-up.

## 1. Representative protein names — corrected

Every module representative was checked against its frozen UniProt DE record. Nine unique accessions needed corrections: the seven accessions listed in the review, plus capitalization/punctuation differences for Q88PQ5 and Q88PQ3. There are ten literal edits; the shared AZOBR FruB term is reused through a YAML alias. `round1-uniprot-labels.yaml` records each literal before/after value and its source path. IDs and descriptive `preferred_term` values are unchanged.

This includes changing Q88PQ4 and A0A0P0F764 from the inferred activity descriptor to the actual record name, `Phosphofructokinase`. The more specific FruK role continues to rest on the reviewed evidence and domain/activity requirements. A source name, including an automatic name, identifies the record; it is not used as functional evidence.

## 2. Ontology-only knowledge gap — relocated

The EIIA-to-EIIB ontology request and its mechanism boundary now appear in top-level module `notes`, with explicit pointers to the existing PSEPK, RHOCA and AZOBR proposed terms. The ONTOLOGY-only `knowledge_gaps` entry was removed. The remaining Deinococcus BIOLOGY+CURATION gap is unchanged: a restored full-length FruB ORF does not establish native PEP-dependent fructose uptake or supersede the older ATP-dependent mixed-fraction experiments.

No reaction, participant, family, architecture requirement, connection or endpoint changed.

## 3. Authored GO:0006001 label — reviewer correction declined

The official [QuickGO term service](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006001), retrieved on 2026-11-07, returns:

- Preferred name: **D-fructose catabolic process**.
- Exact synonym: **fructose catabolic process**.
- Obsolete: false.

Therefore the current DEIRA authored label is already the preferred name. The reviewer's requested replacement matches an older local cache/other records and an accepted synonym, not the current preferred name. The replacement/core fields are retained, and the unchanged DEIRA review is included in focused validation. `round1-ontology-check.yaml` records the response, URL and decision; the complete JSON response is cached under `.cache/module-audit-logs/fructose-20261107/round1/GO_0006001.json`. No source annotation label or ontology cache is edited to suppress an advisory.

## 4. AZOBR FruA1 quote specificity — corrected without overstating assays

Architecture-dependent judgments now cite PMID:39817736's explicit description of membrane-bound EIIB/EIIC FruA and cytoplasmic EIIA-HPr-EI FruB. Native growth/transport participation rows retain the actual mutant-growth evidence. Reaction-specific rows additionally cite the target's fructose EIIB signature `IPR003353; PTS_IIB_fruc.` rather than relying exclusively on its EIIC signature.

Neither the architecture sentence nor the domain match is called a direct phosphocysteine experiment. The existing reasons retain the distinction between native physiological support and inferred conserved residue chemistry. The exact sequence-to-Sp7-locus bridge is unchanged. There is no new phosphosite, localization measurement, transport rate or purified target assay claim.

## 5. AZOBR primary-reference adjudication — added

All three AZOBR reviews now manually assess the full-text primary paper, PMID:39817736, with findings tied to verbatim passages:

| Member | Positive evidence | Explicit limit |
|---|---|---|
| FruA1 | Native PTS1 induction; disruption/complementation and fructose consumption; EIIB/EIIC architecture | Growth is not a measurement of each transfer intermediate; no site-resolved phosphocysteine or direct localization assay is attributed to this paper. |
| FruB1 | Native AMK58_25885 induction and reporter regulation; EIIA-HPr-EI architecture | No independently measured purified domain-to-domain kinetics or target phosphosite chemistry. |
| FruK1 | Native AMK58_25880 induction; the established fructose-1-phosphate pathway description | The introductory chemistry is not purified FruK1 substrate specificity or kinetics; the activity assignment also uses the exact target sequence/domain classification. |

The assessments distinguish PTS1 from the PTS2 paralogs. Reference IDs and machine-fetched titles are preserved.

## 6. FruB NTR wording — corrected and aligned

PSEPK no longer says its GO:0016772 row remains over-annotated: that row is MODIFY to PEP-entry activity. The separate downstream relay remains represented through the proposed core activity. PSEPK, RHOCA and AZOBR now use the same proposed definition and ontology boundary. Their justification tails remain source-specific: native KT2440 genetics, sequence-matched Rhodobacter architecture/curated domain support, and inferred Sp7 relay chemistry respectively. PSEPK's narrower existing replacement list is described accurately rather than silently expanded.

This alignment changes neither existing annotation actions nor the proposed term's name or parent. It does not equate native genetic evidence with purified transfer kinetics.

## Verification and scope

Five gene histories and one module history were generated with `just new-history`. Focused gene validation/rendering, unchanged DEIRA label validation, module schema and semantic/reference validation, module rendering, and the existing production coverage checker are recorded in `round1-validation.yaml`. Preservation against the reviewed head, including the unchanged module mechanism, source names and protected artifacts, is recorded in `round1-preservation.yaml` and its executable checker. The production checker first rejected the five stale review hashes, as intended; only those five `review_sha256` pins were refreshed after confirming unchanged fixture activities, domains and systems. All 49 coverage cases and seven constraint mutations then passed. `round1-fixture-refresh.yaml` records the exact hash replacements. No checker logic was weakened. No full-repository validation, publication, commit, family edit or shared tracker edit was performed by this consultation.

The module validator retains 13 advisories: five missing-GO-ID comparisons for the deliberately un-termed relay, four retained-annotation versus immediate-chemistry core comparisons, and four unresolved whole-family function-scope comparisons. These are the existing mechanistic/ontology boundaries, not new term or reference errors. The local DEIRA GO:0006001 label warning is separately adjudicated above.
