# FANCC (Q00597) — gene review notes

## Identity
- Human Fanconi anemia group C protein (FACC / FAC). UniProt Q00597, HGNC:3584, GeneID 2176, chr 9q22.32. 558 aa, ~63 kDa.
- One of the FA "core complex" subunits. First FA gene cloned by functional complementation
  [PMID:1574115 "Cloning of cDNAs for Fanconi's anaemia by functional complementation."].

## Core biology — FA core complex subunit required for FANCD2-FANCI monoubiquitination / ICL repair
- The FA core complex is a multisubunit E3 ubiquitin ligase; FANCC is a non-catalytic subunit of it.
  [PMID:22266823 "Eight of the FA proteins comprise the FA core complex, a multisubunit complex required for DNA damage recognition at a stalled replication fork. In response to DNA damage, the complex, an E3 ligase, monoubiquitinates the FANCD2/FANCI heterodimer"].
- FANCC is co-immunoprecipitated as an integral member of the core complex
  [PMID:22266823 "Flag-tagged FAAP20 co-immunoprecipitated with FANCA, FANCE, and FANCC, indicating that FAAP20 associates with the FA core complex"].
- The five-subunit nuclear complex (FANCA/C/E/F/G) is required for FANCD2 monoubiquitination
  [PMID:12649160 "The FANCA, FANCC, FANCE, FANCF, and FANCG proteins form a nuclear complex required for the monoubiquination of the FANCD2 protein."].
- FANCC binds FANCE directly; the disease mutation L554P abolishes this
  [PMID:12649160 "A central region of FANCE was sufficient for FANCC binding. A Leu554Pro mutant of FANCC failed to interact with FANCE."].
- Structural placement (cryo-EM, not in GOA): FANCC-FANCE-FANCF constitute the substrate-recognition
  module of the FA core E3 ligase, present in a single copy, that positions the FANCD2-FANCI substrate
  for monoubiquitination by the FANCL RING/UBE2T module (Shakeel et al. 2019 Nature, PMID:31666700;
  deep-learning atomic model PMID:32939280; PDB 7KZP chain C = FANCC 1-558). This supports a
  molecular-adaptor / substrate-scaffold role and contribution to the complex's ubiquitin-ligase activity.
- Downstream: monoubiquitinated FANCI-FANCD2 drives replication-coupled ICL repair in S phase
  [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex" ; "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase."].

## FANCC and translesion synthesis (TLS) — branch of the pathway
- Genetic (DT40) epistasis links FANCC to REV1-mediated error-prone TLS; the FA core (not FANCD2) is
  needed for REV1 focus formation and point mutagenesis
  [PMID:22266823 "Studies by Niedzwiedz et al. in chicken DT40 cells demonstrated an epistatic relationship between FANCC of the FA core complex and the error-prone TLS polymerase, Rev1, suggesting that the FA pathway regulates TLS through this mechanism."]
  [PMID:22266823 "FANCC-deficient DT40 cells display a reduced frequency of spontaneous point mutations, suggesting that the FA pathway is required for Rev1-mediated TLS of abasic sites or other spontaneously generated DNA lesions"].

## FA core complex assembly / integrity — FANCA-FANCC interaction
- FANCA (FAA) and FANCC (FAC) bind each other; binding correlates with function and is lost in L554P
  [PMID:9398857 "we demonstrate the FAA and FAC bind each other and form a complex. Protein binding correlates with the functional activity of FAA and FAC, as patient-derived mutant FAC (L554P) fails to bind FAA."].
- Unbound FAA/FAC are largely cytoplasmic; the assembled complex is both cytoplasmic and nuclear
  [PMID:9398857 "Although unbound FAA and FAC localize predominantly to the cytoplasm, the FAA-FAC complex is found in similar abundance in both cytoplasm and nucleus."].
- FA core also present in a larger BLM-containing "BRAFT" super-complex
  [PMID:12724401 "one of the complexes, termed BRAFT, also contains five of the Fanconi anemia (FA) complementation group proteins"].
- FAAP20 is an integral core-complex protein needed for DNA-damage-induced chromatin loading of the core
  [PMID:22343915 "We show that FAAP20 is an integral component of the FA nuclear core complex." ; "The FAAP20-UBZ domain is not required for interaction with FANCA, but is required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway."].

## Non-core / additional proposed roles (context-specific, separable from ICL-repair function)
- Cytoplasmic chaperone GRP94/HSP90B1 binds FANCC and regulates its steady-state level; interaction is
  cytosolic, not nuclear
  [PMID:9596688 "Binding was confirmed by coimmunoprecipitation of FAC and GRP94 from cytosolic, but not nuclear, lysates" ; "Ribozyme-mediated inactivation of GRP94 ... led to significantly reduced levels of immunoreactive FAC and concomitant hypersensitivity to mitomycin C"]. This is a stability/localization interaction, not a distinct MF.
- Cytokine signaling / apoptosis: FANCC promotes IFN-gamma-induced STAT1 activation and suppresses
  cytokine-induced apoptosis via modulation of PKR (EIF2AK2). These functions are STRUCTURALLY SEPARABLE
  from the cross-linker-resistance/FANCD2 function
  [PMID:11520787 "FANCC is also required for optimal activation of STAT1 in response to cytokine and growth factors and for suppressing cytokine-induced apoptosis by modulating the activity of double-stranded RNA-dependent protein kinase."]
  [PMID:11520787 "All mutants complemented mitomycin C (MMC) hypersensitive phenotype of FA-C cells and corrected aberrant posttranslational activation of FANCD2 in FA-C mutant cells. However, 2 of the mutants, S249A and E251A, failed to correct defective STAT1 activation."].
  => Treat oxidative-stress/redox and cytokine/apoptosis roles as NON-CORE.

## Localization summary
- UniProt: Nucleus + Cytoplasm; "The major form is nuclear. The minor form is cytoplasmic." Assembled
  FA core acts in the nucleoplasm/on chromatin; cytosolic pool associates with chaperones (GRP94) and a
  PKR/HSP70 complex (Reactome R-HSA-9835411). Nucleoplasm (HPA IDA) and chromatin (ComplexPortal IDA)
  are well supported.

## Annotation-review decisions (summary)
- GO:0043240 Fanconi anaemia nuclear complex (part_of; IBA/IEA/NAS/IDA x5): ACCEPT — CORE.
- GO:0036297 interstrand cross-link repair (IEA, NAS): ACCEPT — CORE.
- GO:0006281 DNA repair (TAS): ACCEPT (general parent, correct).
- GO:0065003 protein-containing complex assembly (TAS): ACCEPT (FANCC needed for FA core assembly/integrity).
- GO:0034599 cellular response to oxidative stress (IBA): KEEP_AS_NON_CORE (mouse-driven phylogenetic;
  redox role real but peripheral, separable from ICL repair).
- GO:0006289 nucleotide-excision repair (IBA): MARK_AS_OVER_ANNOTATED — FANCC is not a canonical NER
  factor; its process is ICL repair / TLS regulation. Over-propagated IBA.
- GO:0005515 protein binding (IPI x6): MARK_AS_OVER_ANNOTATED — uninformative MF; specific partners
  (FANCE, GRP94, SMAD4, FBXW7, MEOX2, AKT1) are largely HT/network or captured better by complex terms.
- Locations nucleus/cytoplasm/nucleoplasm/cytosol/chromatin: ACCEPT (all supported).

## References not in GOA but used for context (notes only; not cited as supporting_text)
- PMID:31666700 Shakeel et al., Structure of the FA monoubiquitin ligase complex, Nature 2019.
- PMID:32939280 Deep-learning atomic structure of FA core complex (PDB 7KZP), 2020.


## 2026-10-25 — preserved acquisition and source-review chronology

The original journal remains exact above. The following three checkpoint appendices are historical: their counts, status and isolated scope describe those stages. The final integration entry supersedes the old adaptor/ligase/chromatin core interpretation, while preserving the accepted source-specific reviews and all inherited quotation associations.

# FANCC intake journal — 2026-10-25

ROOT authorized a private refresh after accepting the finite identity/ownership preflight. The original six-file review remains frozen with 37 rows, 32 references and 27 inherited quotation anchors. A new acquisition snapshot contains 39 PENDING contexts from 40 raw/TSV rows. It is kept separately and is not an authorization to reset the old review.

All 37 existing normal sources remain exact. Ten missing PMID records were fetched by genuine repository tooling; no source text or flags were rewritten. The actual falcon/perplexity-lite attempt failed and is retained as a failure. The original affinage document remains an inherited input only.

The displayed558 sequence and absent ALTPROD are independently checked. PTHR16798 v19 target tree/MSA and three exact source IBDs are mechanically reconciled, including legitimate self-WITH. No function, source paper, donor assay or evolutionary placement was scientifically adjudicated.

Future review must keep the 27 exact quotation paths and their original reference associations, inherited NEW36 and all old core/reference objects intact until a separately authorized manual delta. Whole PMID groups stay together. Current binding partner expansion at legacy8 and11 requires explicit source-aware reconciliation rather than automatic copying of an old judgment.


## 2026-10-25 — FANCC database-source reassessment

This is the database lane only: 20 current contexts map one-to-one to 20 inherited positions. The inherited 37 source objects (36 imported plus one NEW), all 27 quotation paths and reference associations, old description/core/status and unowned 17 reviews remain intact. Fresh acquisition has 39 PENDING contexts and stays separate; its two partner-split groups belong to the direct lane. Current recommendations are 16 ACCEPT, 3 KEEP_AS_NON_CORE and 1 MODIFY. These counts supersede only the corresponding older database judgments, not the entire gene review.

The NER IBA is changed to interstrand cross-link repair as a lateral lesion/role correction. The actual v19 PTHR16798 target path and PTN000423656 IBD are valid; the complete mouse PMID:8704201 original measured MMC/DEB chromosome damage and MMC G2 accumulation. This does not establish loss of all NER biology or faulty orthology. Human complex/reconstitution and FANCC rescue evidence supports the positive ICL role. The inherited quotation is preserved as historical evidence, without upgrading it to a direct excision assay.

The oxidative-stress IBA remains positive and contextual. Mouse PMID:24483844 separates Fancc/Foxo3a genetics from Fancd2-specific ROS/neurosphere work. The latter is not relabeled as a Fancc assay. Independently, PMID:27133164 directly measures human FANCC patient-fibroblast WT rescue of CCCP-associated mitochondrial ROS; its actual Figure 5 and selected supplemental Methods were inspected. This is not merely a presumed consequence of nuclear repair. No mitophagy NEW row or core update is proposed by this lane.

Actual HPA antigen and images support a nucleoplasmic pool. Broad nucleus and contextual cytoplasm are retained; no natural-product identity follows from UniProt's major/minor-form wording. Twelve exact Reactome target routes distinguish FANCC membership/location from FANCL/UBE2T, nuclease, polymerase, USP1 and ATR chemistry. TP53 stimulates FANCC gene expression: FANCC is the protein output, not the transcriptional performer. The PKR route has actual cytosolic FANCC and positive target evidence; complete PKR-paper Methods remain unavailable here.

Four genuine missing publications were fetched in a copied private runtime (8704201, 24483844, 9063748, 27133164); every preimage retained bytes/mode and no restoration was needed. PMID:27986592 is an exact existing-source reuse. Cache availability flags reflect immutable normal metadata; complete external main access and selected reading are recorded separately. No publication quotation was added or moved. The detailed, public source boundaries are in [FANCC-source-guide.md](FANCC-source-guide.md).


## 2026-10-25 direct-source reassessment

Reviewed 19 current direct contexts from 12 whole PMID groups: 6 ACCEPT, 3 MODIFY, 3 KEEP_AS_NON_CORE and 7 UNDECIDED. The exact partner expansions and source-access limits are recorded in the [authored source guide](FANCC-source-guide.md). Inherited source objects and quotation anchors are preserved. The historical partner-unspecified PMID:35512704 assertion remains unresolved while its AKT1 context is separately refined and SMAD4/FBXW7 target matrices remain unreadable.

Newly recovered authentic PMID:22343915 supplement S1C directly identifies FANCC in HeLa FAAP20 co-IP. Main Figure 5H still assays A/G/FAAP20/H2A rather than resolving C chromatin residence; no wrong-gene conclusion follows. The inherited NEW adaptor source is preserved and reassessed U after actual current adaptor/scaffold definitions and human CEF-module evidence; no isolated C bridging mechanism is inferred. This new access does not retroactively imply that earlier FANCA assessments had read the supplement. Stable core membership remains distinct from a FANCC-specific adaptor mechanism.

All 27 inherited quotation paths and reference associations, 36 imported source objects plus the separately inherited proposed-annotation source, and the absent alternative-products field remain exact. One existing fixed-main original, PMID:27986592, is reused as an additional supporting reference. No publication cache or provider output was authored or rewritten, no new quotation was added, and unavailable original experiments are not treated as negative results.


## 2026-10-25 — combined review and core synthesis

The combined historical view preserves all 36 imported source objects plus the separately inherited proposed-annotation source, in their original order. Its actions are 22 ACCEPT, 3 MODIFY, 6 KEEP_AS_NON_CORE and 6 UNDECIDED. The distinct fresh-source audit contains 39 imported contexts: 22 ACCEPT, 4 MODIFY, 6 KEEP_AS_NON_CORE and 7 UNDECIDED. Two old partner-unspecified rows expand into five current partner contexts. SMAD4/FBXW7 remain unresolved; the separately resolved AKT1 binding refinement is preserved in the current audit and the historical reason without attaching an AKT-specific replacement to all partners. Both historical GOA and fresh source snapshots remain literal; neither is silently substituted for the other.

All accepted direct and database review objects are integrated exactly, including inherited adaptor source 36 now UNDECIDED. No accepted review overlay is applied. The 32 original reference identities, titles and findings survive. Six reference additions from the source reviews plus two literal pre-existing structural sources produce 40 references. Five shared assessments retain both complete labeled notes. PMID:9398857 conservatively uses UNVERIFIED for unresolved operative experiments/directness while explicitly retaining verified identity and positive abstract claims. PMID:27986592 normalizes absent findings to an empty list only.

One repair-complex core replaces the old adaptor/contributes-to-ligase claim. It retains ICL repair, complex assembly, nucleoplasm and FA nuclear-complex membership, but does not force an MF from membership or whole-CEF activity. Chromatin is not assigned as a core location while its exact C-specific imported experiment remains unresolved. The three original core support quotations remain at their exact paths: they support association and complex-level function, not a newly demonstrated FANCC-specific substrate bridge or ubiquitin-transfer assay. No new publication quotation or annotation source is added. The two BP roles are mutually nonancestral under current is_a/part_of closure.

The 2019 structural experiment uses recombinant chicken proteins; the 2020 integrative reconstruction reuses its data and changes an earlier C/E density assignment to FANCG. Its C–E interface and mapped human residue-295 variant are positive model evidence, not a human mutant binding experiment. Both originals were independently read at the selected Methods/Results/caption locators recorded in the private ledger; no new structural pixels, maps or coordinates were inspected.

A minor private reading-locator correction is explicit: the database ledger's supplemental Methods ranges for PMID:27133164 did not extend far enough to include the stated SV40/rescue and MitoSOX details. In this successor the exact extracted lines 127–133 and 527–537 were independently read: patient R548X fibroblasts, SV40 large-T immortalization, WT/vector rescue, 5 micromolar MitoSOX for 30 minutes and flow cytometry. The sealed prior packet is unchanged; the biological interpretation was correct and the exact successor read scope repairs the locator boundary.

Two question/experiment pairs address FANCC-specific assembly versus partner effects and separation of mitochondrial/ROS from nuclear repair functions. The normal union contains 54 literal files, with 39 selected and 15 unused private sources, plus the two exact inherited machine files. No source cache or canonical file was rewritten. Historical COMPLETE is preserved pending ROOT's canonical status computation; this private integration is not a new canonical status assertion.

The [FANCC source guide](FANCC-source-guide.md) combines the public source locators and biological limitations for the whole gene. Exact reference unions, historical/current mapping, quotation checks and executed focused validation remain in the private reproducibility packet.


## 2026-10-25 — withdraw the unsupported historical adaptor proposal

The inherited GO:0030674 proposal is now explicitly retired, with its UNDECIDED assessment, source fields and both quotations preserved. This withdraws our earlier active proposal because the available FANCC-specific evidence does not establish the proposed adaptor mechanism. It does not claim that GO withdrew a source annotation: this was an authored proposal and never occurred in the preserved GOA snapshot. The unresolved mechanism remains a question for targeted experiments; no scaffold or catalytic replacement is asserted.

There are 37 retained historical records and 36 active imported records. The active decisions are 22 ACCEPT, 3 MODIFY, 6 KEEP_AS_NON_CORE and 5 UNDECIDED; the one retired proposal is also UNDECIDED. All original source fields and all 27 quotation/path/reference associations remain unchanged. The schema's existing retirement field records this lifecycle separately from the biological verdict, consistent with the earlier DHODH withdrawn-proposal treatment. Initial normal and ontology-enabled checks reported the old proposal as absent from GOA after its action changed from NEW; those failures are retained in execution provenance. No validator, ontology, GOA or publication cache was changed to bypass that check.


## 2026-10-25: expose partner-specific decisions

PR review identified that the AKT1 refinement was present only in prose while two historical source rows combined multiple partners. The normal `seed-goa` command was run against an exact private copy of the committed machine GOA file. Its five distinct source objects for PMID:24412244 and PMID:35512704 were matched to the independently reviewed current contexts. The structured review now records each partner separately: AKT1 is MODIFY to GO:0043422 (protein kinase B binding); both SMAD4 contexts and both FBXW7 contexts remain UNDECIDED because their original target matrices were unavailable. The evidence standard is unchanged: inspected AKT1 co-IP and MEOX2 Y2H support their respective partner-binding terms, without inferring kinase activity or transcriptional regulation.

The first partner occupies each old, unquoted row position, and the three additional contexts are appended. All 27 inherited quotation/path/reference associations, all unrelated source rows, the retired adaptor record, references, products and core functions remain unchanged. The original collapsed review objects follow verbatim as JSON values; they are historical accounts, not additional active annotations. The machine GOA and UniProt files are unchanged.

The cytosol IDA is now KEEP_AS_NON_CORE. Re-reading the actual PMID:9596688 abstract confirms the explicitly reported cytosolic co-IP, which supports the broad compartment together with the curator attribution and independent Reactome model. Complete Methods and figure availability remain unresolved; this decision does not claim those were read. The earlier UNDECIDED assessment was more cautious than required for this well-supported location. No unused consistency_exception field was added: the actual configured conflict table does not classify the former NC/U pair as a conflict.

### Historical collapsed source objects

```json
{
  "8": {
    "term": {
      "id": "GO:0005515",
      "label": "protein binding"
    },
    "evidence_type": "IPI",
    "original_reference_id": "PMID:24412244",
    "qualifier": "enables",
    "review": {
      "action": "UNDECIDED",
      "summary": "Both current partner expansions remain limited by the unavailable original target table.",
      "reason": "Current context 2: PMID:24412244 is the verified colorectal-cancer interaction-screen paper, but its operative main text and target interaction table were not recovered from the exact publisher route. The imported WITH identifies SMAD4; the abstract alone does not establish the target assay, controls or native-versus-mutant scope. DNA-binding-transcription-factor binding was considered, but no specific replacement or removal is justified without the operative target evidence. Positive curated attribution is retained as unresolved, not contradicted. Current context 3: The verified PMID:24412244 abstract reports the screen globally, while the complete target table and operative Methods remain unavailable. The imported partner Q969H0 is FBXW7, an SCF substrate-recognition subunit; partner identity alone does not establish binding to a complete ubiquitin ligase, enzyme regulation or FANCC substrate status. The annotation is not removed or declared false because the target experiment cannot be inspected."
    }
  },
  "11": {
    "term": {
      "id": "GO:0005515",
      "label": "protein binding"
    },
    "evidence_type": "IPI",
    "original_reference_id": "PMID:35512704",
    "qualifier": "enables",
    "review": {
      "action": "UNDECIDED",
      "summary": "The collapsed historical binding context combines a supported AKT refinement with two unresolved target matrices.",
      "reason": "The historical source object does not name a partner and is preserved intact. Its three fresh contexts are adjudicated separately: AKT1 context 6 is MODIFY to protein kinase B binding; SMAD4 context 7 and FBXW7 context 8 are UNDECIDED. No AKT-specific replacement is applied wholesale to this collapsed object. Current context 6: PMID:35512704 Data S1, Figure iiiA, directly displays FLAG-tagged FANCC recovered with GST-AKT1 in transfected HEK293T cells, with a wild-type AKT1 signal and a stronger E17K-mutant signal. The panel was visually inspected; no new densitometry is claimed. Table S3B row 10 separately records positive AKT1-E17K/FANCC validation. The paper’s main Methods distinguish tagged proximity, split-luciferase and pull-down assays; the semi-endogenous MCF7 panel does not show FANCC. GO:0043422 precisely names binding to protein kinase B/AKT, without assigning FANCC kinase activity, substrate status or an established native-cell DNA-repair mechanism. The unreadable Table S2 file and mutation annotations remain explicit source limits. Current context 7: PMID:35512704 main Methods establish the human tagged BRET screen and its wild-type/mutant comparisons. Actual IntAct records EBI-63711113, EBI-63706663, EBI-63715006 and EBI-63702524 identify FANCC/SMAD4 BRET contexts with mutation-with-no-effect features; these are positive curated records, not evidence of mutant-only or absent wild-type binding. However, both preserved downloads of the primary Table S2 workbook lack a readable ZIP directory, and no target-specific SMAD4 panel was inspected. A transcription-factor-binding refinement is plausible but is not asserted from curated features alone. UNDECIDED records that target-source limit without rejecting the interaction. Current context 8: Actual PMID:35512704 IntAct records EBI-63689535, EBI-63693940, EBI-63684551 and EBI-63698153 identify FANCC/FBXW7 BRET contexts with mutation-with-no-effect features. The main Methods were read, but the primary Table S2 target matrix could not be parsed from either preserved download. FBXW7 is the SCF substrate-recognition subunit; the record does not on its own demonstrate FANCC binding to the assembled ligase, ligase regulation or a direct enzymatic reaction. Retain the positive curator attribution as unresolved pending readable target measurements; no wrong-gene or no-binding claim is made."
    }
  }
}
```


## 2026-10-25 — partner metadata and current-checkpoint clarification

The partner-resolved checkpoint has 39 active imported contexts: 22 ACCEPT, 4 MODIFY, 7 KEEP_AS_NON_CORE and 6 UNDECIDED. One retired UNDECIDED adaptor proposal is retained separately. The review has 40 references, one core unit and 27 inherited quotation paths. Earlier 36-context counts and the verbatim superseded objects above document earlier checkpoints and remain historical. The current published PR body already reported the correct 39-context counts when inspected.

The cytoplasm reason no longer describes the PMID:9596688 cytosol verdict as unresolved: that location is retained as non-core, while its detailed assay Methods remain unavailable. Four missing supporting_entities fields were copied from genuine seeder output against the unchanged committed GOA: FANCE/Q9HB96 in PMID:12649160 and PMID:33961781, MEOX2/Q6FHY5 in PMID:26871637, and GRP94/P14625 in PMID:9596688. No action, term, source identifier or order changed. The duplicate GRP94 source provenance remains explicit.

Current source-guide and reference-note locator spacing is corrected. The earlier journal prefix is not rewritten; its compressed spellings denote the displayed 558-residue product and the historical row or table locators described with spaces in the current [source guide](FANCC-source-guide.md). That guide also clarifies the distinction between official comparator annotations and sibling review assertions, and the evidence-resolution reason for deferring a contributes-to molecular function. The existing question and experiment already state the unresolved step.

All 27 inherited quotation paths, texts, reference associations and order are unchanged. The requested title-quote replacement and Xenopus-quote reordering are declined under the standing preservation instruction; no new publication quotations are added. All review actions, the retired proposal, biological description, core, reference identities/findings, status and absent alternative-products field remain unchanged.


## 2026-10-25: GRP94 association retained; specific refinement deferred

The current review retains the PMID:9596688 FANCC–GRP94/P14625 generic binding context as KEEP_AS_NON_CORE. The complete cached primary abstract explicitly reports yeast two-hybrid interaction and coimmunoprecipitation, consistent with the curator's positive IPI assertion. The previous UNDECIDED action conflated incomplete assessment of a more specific replacement with uncertainty about the already supported association. GO:0051879 Hsp90 protein binding remains deferred pending the unavailable operative Methods, controls and Results. No purified binary interaction, FANCC chaperone activity, or natural-product equivalence is inferred from the abstract's deletion constructs.

There are now 39 active imported contexts: 22 ACCEPT, 4 MODIFY, 8 KEEP_AS_NON_CORE and 5 UNDECIDED, plus the unchanged retired UNDECIDED adaptor proposal. The 40 references, one core unit, all source fields, and all 27 inherited quotation/path/reference associations are unchanged. Earlier journal entries remain historical. The source guide removes a redundant superseded-count sentence and states this claim-versus-refinement distinction. No source cache, publication quotation or additional annotation was created.
