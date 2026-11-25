# glpD review notes

## Identity and scope

- Target: `glpD`, PP_1073, UniProt Q88NY0, *Pseudomonas putida* KT2440.
- Reviewed target files: `glpD-ai-review.yaml`, `glpD-goa.tsv`, and `glpD-uniprot.txt`.
- Read-only pathway context: `genes/PSEPK/glpK/glpK-ai-review.yaml`, `glpK-uniprot.txt`, and `glpK-deep-research-asta.md`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/glpD/glpD-uniprot.txt`.

- `"DE   RecName: Full=Glycerol-3-phosphate dehydrogenase"`
- `"DE            EC=1.1.5.3"`
- `"CC       Reaction=a quinone + sn-glycerol 3-phosphate = dihydroxyacetone"`
- `"CC       Name=FAD; Xref=ChEBI:CHEBI:57692;"`
- `"DR   GO; GO:0004368; F:glycerol-3-phosphate dehydrogenase (quinone) activity; IEA:UniProtKB-EC."`
- `"DR   GO; GO:0046168; P:glycerol-3-phosphate catabolic process; IEA:TreeGrafter."`

### Direct KT2440 pathway description

Source: Nikel et al., 2015, PMID:25827416, PMCID:PMC4453509, DOI:10.1128/mBio.00340-15. Full text accessed through PMC/web search.

- `"Glycerol-3-P is then oxidized in an ubiquinone-dependent reaction catalyzed by the membrane-bound GlpD"`
- `"G3P is the substrate for GlpD, a membrane-bound G3P dehydrogenase that yields dihydroxyacetone-P"`
- The abstract states that a transcriptional `glpD-gfp` fusion was used as `"a proxy of the glycerol-3-phosphate [G3P] dehydrogenase activity"` and that GlpR controls the `glpFKRD` cluster.

### Read-only GlpK context

`glpK-ai-review.yaml` identifies GlpK as the ATP-dependent first committed step that produces sn-glycerol-3-phosphate. No glpK file was edited.

### OpenScientist report

Source: `file:PSEPK/glpD/glpD-deep-research-openscientist.md`.

- The report completed with HTML and PDF artifacts even though the wrapper returned a timeout status.
- Its target identity, reaction, and `glpFKRD` pathway placement agree with the UniProt record and PMID:25827416.
- The report also quotes a secondary source as calling GlpD a six-transmembrane enzyme while elsewhere correctly describing the characterized enzyme as monotopic. That contradictory topology claim was not used as evidence.

## Curation conclusions

- Accept GO:0004368 specifically as quinone-dependent activity.
- Do not substitute an NAD-dependent glycerol-3-phosphate dehydrogenase term; that would reverse the physiological chemistry and use the wrong acceptor.
- Accept G3P catabolism and plasma-membrane association; keep the broader G3P metabolic process as non-core.
- Leave the transferred FAD-complex component term UNDECIDED because no
  target-specific oligomerization evidence or distinct GlpB/GlpC partners were
  found. The available evidence establishes a monotopic GlpD enzyme, not the
  composition of a molecular complex.

## 2026-11-03 review completion (Claude, AI-assisted)

Deep research was available: `glpD-deep-research-openscientist.md` (provider
report, used only for locus context; its "six transmembrane" quote was not used).
PMID:25827416 is abstract-only in the cache; full-text statements above were
already recorded from PMC. The E. coli ortholog structure paper PMID:18296637
(full text cached) was added as the experimental basis for ISS-level transfer.

Changes, reviewed together with `genes/ECOLI/glpD` so shared terms get the same
actions:

- GO:0009331 glycerol-3-phosphate dehydrogenase (FAD) complex (IEA, UniRule
  GO_REF:0000104): UNDECIDED -> ACCEPT. The GO definition explicitly covers "a
  GlpD homodimer that functions in aerobic conditions", so no GlpB/GlpC partners
  are needed. Q88NY0 is an aerobic GlpD (about 57% identical to P13035, same
  PTHR11985:SF15 subfamily). The E. coli dimer interface helps form the active
  site (PMID:18296637). The ECOLI IDA row on the same term is also ACCEPT.
  Added `in_complex` GO:0009331 to core_functions.
- GO:0006072 (IEA GO_REF:0000120): KEEP_AS_NON_CORE -> MODIFY to GO:0046168
  (correct but general parent).
- GO:0005886 plasma membrane NEW row: changed from ISS citing the deep-research
  file to ISS with original_reference_id PMID:18296637 (ortholog P13035). It is
  backed by the ortholog localization and bilayer-embedding quotes, the KT2440
  "membrane-bound GlpD" statement, and the shared PANTHER subfamily.
- GO:0004368 and GO:0046168 stay ACCEPT. Added vetted support (UniProt RuleBase
  reaction, InterPro IPR000447, PANTHER lines, PMID:18296637,
  PMID:25827416 abstract) and named the routes (Combined IEA; TreeGrafter
  PTN002279478, with the PAINT IBD for GO:0046168 at PTN008531994).
- Every row now has supported_by. Status set to COMPLETE. Added one suggested
  experiment.

## 2026-11-04 (PR #5936 review follow-up)

- PMID:25827416 full text is now cached; quotes previously attributed to this notes file now cite the PMID directly. Added a suggested question recording that in_complex GO:0009331 is homology-based (about 57% identity to E. coli GlpD), with no KT2440 oligomerization assay.


## 2026-11-07 comparative glycerol audit

Rechecked all five rows, preserving the historical plasma-membrane NEW payload and action. Quinone-dependent oxidation remains supported by curated RuleBase specificity and native pathway context; exact native quinone identity, membrane face and homodimeric assembly are qualified ortholog inferences. PMID25827416 measures growth/reporters and GlpK, not purified GlpD quinone specificity. The pre-existing OpenScientist report is genuine; its contradictory six-TM statement is not accepted. A lack of TM helices is not affirmative membrane-localization evidence.

Existing genuine provider research was inspected and preserved byte-for-byte; conclusions were checked against primary sources. All original ordered annotation payloads are preserved, with no new GO rows. Focused validation, source preservation, and helper-history results are recorded in analysis/module_audits/bacterial_glycerol_uptake_catabolism/existing-member-consultation/. COMPLETE denotes completed adjudication, including explicit unresolved claims.


## PR6162 review follow-up (2026-11-07 UTC)

Retained the exact historical NEW membrane payload/action and strengthened its positive ISS rationale with a reproducible frozen-sequence bridge:286/500 aligned residues identical (57.2%), or286/515 total columns(55.53%). Verified family/reaction compatibility and native pathway description accompany direct Ecoli donor topology. Target membrane-face orientation and oligomerization remain inferred.

Original ordered annotation payloads, raw/provider/publication bytes and historical NEW assertions are preserved. No new GO row was added.
