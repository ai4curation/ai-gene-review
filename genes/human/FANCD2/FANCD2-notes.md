# FANCD2 (Q9BXW9) review notes

## Summary of biology
FANCD2 (Fanconi anemia group D2 protein; 1451 aa) is the central effector of the Fanconi
anemia (FA)/BRCA DNA interstrand crosslink (ICL) repair pathway. With its paralog FANCI it
forms the ID2 heterodimer. Upon replication stress/ICLs, FANCD2 is monoubiquitinated at
Lys561 by the FA core complex (E3 = FANCL, E2 = UBE2T), which converts the open ID2 trough
into a closed sliding DNA clamp that encircles duplex DNA, loading ID2 onto chromatin to
coordinate nucleolytic incision (unhooking), translesion synthesis (POLN) and homologous
recombination. It is deubiquitinated by the USP1–UAF1(WDR48) complex. FANCD2 also protects
stalled replication forks, restrains nucleases, and localizes to common fragile sites /
ultrafine anaphase bridges (with BLM). Loss causes Fanconi anemia complementation group D2:
bone marrow failure, congenital malformations, chromosomal instability, MMC/DEB
hypersensitivity, cancer predisposition.

## Key provenance (verbatim)

- ID2 clamp / monoubiquitination function:
  [PMID:32269332 "monoubiquitination triggers a complete rearrangement of the open, trough-like ID structure through the ubiquitin of one protomer binding to the other protomer in a reciprocal fashion"]
  [PMID:32269332 "the monoubiquitinated ID complex loses its preference for ICL and related branched DNA structures, and becomes a sliding DNA clamp that can coordinate the subsequent repair reactions"]
  [PMID:32269332 "a closed ring that encircles the DNA"]

- Replication-coupled ICL repair, incision + TLS:
  [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase. Removal of FANCD2 from extracts inhibits both nucleolytic incisions near the ICL and translesion DNA synthesis past the lesion. Reversal of these defects requires ubiquitylated FANCI-FANCD2"]

- ssDNA binding / ring-like particle:
  [PMID:19609304 "Purified FANCD2, a ring-like particle by electron microscopy, preferentially bound ssDNA over various DNA substrates"]
  [PMID:19609304 "We propose that FANCD2 binds to ssDNA arising from MRE11-processed DNA double-strand breaks"]

- FANCI as monoubiquitinated paralog / partner:
  [PMID:17460694 "A FANCD2 protein sequence-based homology search facilitated the discovery of FANCI, a second monoubiquitinated component of the FA pathway"]

- BRCA2 direct interaction (HR):
  [PMID:15115758 "it bound to a highly conserved C-terminal site in BRCA2 that also binds FANCG/XRCC9. FANCD2 and BRCA2 can be coimmunoprecipitated from cell extracts"]
  [PMID:18212739 "phosphorylation of FANCG serine 7 is required for its co-precipitation with BRCA2, XRCC3 and FANCD2, as well as the direct interaction of BRCA2-FANCD2"]

- FAN1 nuclease recruitment by monoubiquitinated FANCD2:
  [PMID:20603015 "KIAA1018/MTMR15/FAN1, that interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2"]

- POLN interaction (crosslink repair / HR):
  [PMID:19995904 "we obtained evidence for physical and functional interaction of POLN with factors belonging to the Fanconi anemia pathway, a master regulator of cross-link repair"]

- UHRF1/UHRF2 promote FANCD2 recruitment/monoubiquitination (nucleus/chromatin):
  [PMID:30335751 "UHRF2 cooperates with UHRF1, to ensure recruitment of FANCD2 to ICLs"]
  [PMID:30335751 "the essential monoubiquitination of FANCD2 is stimulated by UHRF1/UHRF2 ... by a retention of FANCD2 on chromatin"]

- MEN1/menin interaction; enhanced by gamma-irradiation:
  [PMID:12874027 "menin specifically interacts with FANCD2 ... The interaction between menin and FANCD2 is enhanced by gamma-irradiation"]

- CEBPD/IPO4 nuclear import:
  [PMID:20805509 "C/EBPδ interacts with FANCD2 and importin 4 (IPO4 ...) via separate domains, mediating FANCD2-IPO4 association and augmenting nuclear import of FANCD2, a prerequisite for its monoubiquitination"]

- Monoubiquitination at Lys561 by FANCL/UBE2T; DUB USP1; chromatin binding requirement
  (UniProt Q9BXW9 PTM/SUBUNIT sections).

## Curation decisions (high level)
- Core: interstrand cross-link repair (GO:0036297); ssDNA/damaged DNA binding (clamp);
  DNA-repair (ID2) complex; nuclear/chromatin localization; HR-mediated DSB repair.
- protein binding (GO:0005515, 11 IPI rows): REMOVE — uninformative MF; the underlying
  interactions (FANCI, BRCA2, MEN1, MRE11/NBS1, FAN1, CEBPD, EGFR) are recorded here/in
  more specific terms.
- DNA polymerase binding (GO:0070182, IBA + POLN IPI): KEEP_AS_NON_CORE — real but peripheral.
- Meiotic terms (GO:0007129, GO:1990918): KEEP_AS_NON_CORE (germline-restricted, IBA).
- nucleolus (GO:0005730), response to gamma radiation (GO:0010332): KEEP_AS_NON_CORE.
- Added NEW GO:0003697 single-stranded DNA binding (IDA, PMID:19609304).
</content>

## 2026-10-25 — Direct-source reassessment and inherited proposals

The current source export contains 21 direct contexts across 16 whole PMID groups. These map to 18 older imported records; the two older records for PMID:19609304 and PMID:20603015 group distinct partners. This assessment supplies each current partner decision separately and preserves all 46 older source objects in their original order. The 31 inherited quotation/reference/path associations, four natural products, existing description, core and status remain unchanged. The 24 unassigned current database contexts remain PENDING in the separate context audit. Older decisions and counts above are historical; the source-specific reassessment below supersedes them where stated.

The direct contexts are 5 ACCEPT, 9 MODIFY, 6 KEEP_AS_NON_CORE and 1 UNDECIDED. Specific binding refinements distinguish FANCI heterodimerization, MRE11/FAN1 enzyme binding, CEBPD DNA-binding transcription-factor binding and EGFR protein-kinase binding. These terms identify the partner or assembly role; they do not assign the partner's catalysis, transcriptional regulation or import-adaptor activity to FANCD2. Menin, BRCA2 and NBS1 retain positive non-core generic binding after the specificity search. Exact AP-MS and BRET target rows are positive for EGFR; the latter reports both wild type and L858R, not a mutant-only interaction.

A concrete source discrepancy concerns the fresh FSCN1/Q16658 partner in PMID:20603015. The original Figure 1A names FAN1/Q9Y2M0, and its Methods/Figure 4 assay the 114-kDa FAN1 nuclease. Current IntAct records instead map six FANCD2-associated experiments to Q16658 and include FAN1 as an FSCN1 alias. The partner-specific row is UNDECIDED with a CONFIRMED CHECK request. No source identifier has been silently repaired and no upstream report has been sent. The independently imported FAN1 context remains positive. Integration must make these partner distinctions machine-readable while preserving the old grouped row and inherited quotation provenance explicitly.

The five inherited proposals were reassessed without adding quotations. Single-stranded DNA binding, chicken-derived HR inference, human aphidicolin fork recovery and mouse-derived mitochondrial localization remain NEW historical proposals. The R-loop proposal becomes UNDECIDED: current GO:0062176 specifies disassembly, whereas the inspected 2018 and 2023 human studies resolve suppression/formation prevention and mRNA-export mechanisms. The positive R-loop phenotype is retained; disassembly is not inferred from steady-state accumulation. This packet does not retire or delete the historical proposal. The mitochondrial reason corrects the authored mouse accession from Q80V54 to official Q80V62/Fancd2, without changing its source, ISO code or quotation.

All 22 new whole-reference assessments preserve identifiers, titles, findings and earlier assessment text, labeled historical where superseded. Cache availability flags derive from immutable normal metadata. External complete originals, selected author/publisher passages, supplement access and actual reading are described independently. The inaccessible operative PMID:20603016 remains explicitly unverified at that scope; the corresponding target interaction is corroborated by independently read originals. No full-paper or figure-pixel reading is claimed beyond the exact ledger.

See the [FANCD2 source guide](FANCD2-source-guide.md) for the biological source distinctions and public locators. The private evidence packet contains exact original captures, target table rows, official term responses, a literal read ledger, full before/after review objects and a deterministic preservation checker. Schema checks pass for the legacy candidate, reference-overlay candidate and current context audit; the current source audit matches GOA strictly. The full legacy diagnostic reports only the historical R-loop proposal now UNDECIDED and absent from GOA. That expected lifecycle mismatch is retained for explicit integration, not concealed by changing the biological action. No normal source, canonical file, Git state or history was changed here.

## 2026-10-25: database-derived annotation reassessment

Reviewed 24 current database contexts, with 20 ACCEPT and four KEEP_AS_NON_CORE decisions. Twenty-three map to inherited reviews; the current mouse-derived condensed-chromosome context is recorded separately. The inherited nuclear electronic reference and its newer combined source version remain distinguishable. All 46 inherited source objects, 31 quotation paths and 23 unowned whole annotations are preserved in this partial candidate. The direct experimental annotations, five inherited proposals, description and core are assessed in the companion review.

Actual PAINT ancestry and the exact target sequence support seven inherited functions without treating donor count or human self-WITH as failure. The mouse synapsis result and plant completed-synapsis/crossover result were kept distinct. Likewise, the negative primary-mouse checkpoint experiment was retained alongside positive human complementation evidence. The POLN association remains non-core and does not establish a purified binary interface.

HPA images and antigen mapping support gene-level nuclear locations without resolving natural products. Twenty-five Reactome target routes across eleven source events establish the target's own nucleoplasmic compartment; substrate or output-set membership does not transfer ligase, kinase, nuclease, polymerase or transcription activity. The source guide provides public original-paper locators and the limits of actual reading.

Eight normal publication records were genuinely fetched in an isolated runtime with all 293 pre-existing files preserved; no cache record was rewritten. Five focused schema/strict-GOA commands passed. Independent bounded peer review found no required scientific or preservation correction, reconstructing all source and quotation invariants and the selected phylogeny, localization and primary-evidence distinctions. This is a partial review handoff, not a final status or merge claim.

## 2026-10-25 — Integrated source assessment and core synthesis

The source-specific assessments above are historical partial stages. The current combined legacy candidate contains 46 original source objects with 24 ACCEPT, 8 MODIFY, 9 KEEP_AS_NON_CORE, 4 inherited NEW and 1 UNDECIDED review. All 46 complete accepted review objects are preserved. Its 48 references comprise the original 38, including 22 whole-reference assessments, and ten database additions. The database candidate preserved the old 38 references exactly; no arbitrary field union or fabricated shared assessment was needed. Both full source guides and actual read ledgers remain pinned.

One DNA-binding/ID2 core now spans isolated ssDNA binding and the duplex-associated ubiquitinated clamp state. It retains three nonancestor ICL, homologous-recombination and fork-processing facets. The previous checkpoint BP is removed only from the core activity grouping, not from the accepted annotation or biological discussion. Source-specific human/mouse checkpoint contexts are retained. FANCD2 is not assigned clamp-loader ATP hydrolysis or the catalytic activities of its partners. The complete prior core quotation list remains at the same three paths, followed only by bare citations.

The [FANCD2 source guide](FANCD2-source-guide.md) gives the whole-gene biological explanation, public source/ontology locators and product/access limits. The four natural products and all 31 inherited quotation text/reference/path associations remain exact. The old notes prefix occurs once; the direct and database appendices are each retained once. This synthesis was authored by the direct-source reviewer and uses the separately authored, ROOT-accepted database review; it is not an independent whole-gene scientific signoff.

The current 45-context diagnostic is separate from the 46-source legacy candidate. It preserves every fresh source and combines 25 ACCEPT, 9 MODIFY, 10 KEEP_AS_NON_CORE and 1 UNDECIDED reviews. Quotation text is omitted only in that nondelivery diagnostic so no inherited anchor is reassigned to a new index. Current-source adoption, supporting-entity backfills, partner splitting, source-version archival of old row 7, and withdrawal lifecycle of the unresolved historical row 44 are separate explicitly authorized successors; none is silently applied here. The six PR5481 record-section metadata additions also remain a separate reconciliation. Status is preserved pending canonical processing.

## 2026-10-25 — Explicit current-source adoption and proposal lifecycle

This successor supersedes the preceding 46-source integration counts. It adopts the genuine fetched GOA and the actual frozen-runtime seeder output, with 20 supporting-entity backfills and five appended contexts. No gene identity, term, evidence code or original reference is guessed or silently repaired. The original UniProt bytes remain unchanged.

There are now 51 stored annotations, of which 49 are active: all 45 current imported contexts and four retained inherited NEW proposals. Old row 7 is retired solely because its GO_REF:0000044 source version is superseded by the current GO_REF:0000120 nucleus context at row 50. Its positive ACCEPT review remains intact; this is source-version archival, not loss of nuclear localization. Old row 44 is retired as a curator withdrawal of the historical authored R-loop-disassembly assertion. Its UNDECIDED review, original source and quotations remain exact. It was not a vanished GO consortium annotation, and neither retirement asserts biological absence.

Partner contexts are now explicit. Old row 13 carries the literal NBS1/O60934 source and its accepted non-core association review; appended row 47 carries MRE11/P49959 and enzyme-binding refinement. Old row 14 carries the literal Q16658/FSCN1 source, the accepted UNDECIDED review and confirmed identifier CHECK. Appended rows 48 and 49 separately carry FANCI/Q9NVI1 heterodimerization and FAN1/Q9Y2M0 enzyme binding. The historical FAN1 quotation remains at old row 14's original path as preserved provenance, not evidence for FSCN1. No IntAct source identifier is repaired here or reported upstream. Appended row 46 is the separately assessed current mouse-derived chromosome context.

All 31 quotation text/reference/path associations are unchanged. The old supported_by lists at rows 13 and 14 remain exactly in place; new contexts contain only bare references. All 48 references, four natural products, one core, description and questions/experiments remain identical to the sealed core packet. The [source guide](FANCD2-source-guide.md) records the current interpretation. PR5481 record-section metadata remains for ROOT's separate fresh-main reconciliation; canonical status and publication are not computed here.

### Archived grouped annotation objects

The complete inherited and accepted grouped contexts below are retained for provenance. They precede partner-specific source adoption and do not override the current review.

```json
[
  {
    "legacy_index": 13,
    "inherited_before_review": {
      "term": {
        "id": "GO:0005515",
        "label": "protein binding"
      },
      "evidence_type": "IPI",
      "original_reference_id": "PMID:19609304",
      "qualifier": "enables",
      "review": {
        "summary": "This IPI records interaction with the MRE11-RAD50-NBS1 (MRN) complex, which regulates FANCD2 stability and function at DSBs. Protein binding is uninformative as an MF term.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "GO:0005515 is too generic. The MRN relationship is captured as a regulatory interaction in the notes; it does not correspond to a defined FANCD2 molecular activity.",
        "supported_by": [
          {
            "reference_id": "PMID:19609304",
            "supporting_text": "Our data establish MRN as a crucial regulator of FANCD2 stability and function in the DNA damage response."
          }
        ]
      }
    },
    "accepted_grouped_context_before_split": {
      "term": {
        "id": "GO:0005515",
        "label": "protein binding"
      },
      "evidence_type": "IPI",
      "original_reference_id": "PMID:19609304",
      "qualifier": "enables",
      "review": {
        "summary": "The source supports FANCD2 association with both MRE11 and NBS1; the catalytic MRE11 partner supports enzyme binding.",
        "action": "MODIFY",
        "reason": "PMID:19609304 reports MRN association and Supplementary Figure 2A shows human FANCD2–MRE11 coimmunoprecipitation in Sf9 coinfection, with IgG controls. GO:0019899 denotes binding an enzyme and does not require activation of it. The known MRE11 nuclease partner provides a more informative class than generic protein binding. The assay does not resolve an isolated binary interface; the supplemental nuclease assay does not show FANCD2 nuclease activity or MRE11 stimulation under those conditions. The separately resolved NBS1 context retains non-core generic binding. Both current partner-specific judgments are supplied in the context audit; the legacy source object is preserved pending explicit expansion.",
        "proposed_replacement_terms": [
          {
            "id": "GO:0019899",
            "label": "enzyme binding"
          }
        ],
        "supported_by": [
          {
            "reference_id": "PMID:19609304",
            "supporting_text": "Our data establish MRN as a crucial regulator of FANCD2 stability and function in the DNA damage response."
          }
        ]
      }
    }
  },
  {
    "legacy_index": 14,
    "inherited_before_review": {
      "term": {
        "id": "GO:0005515",
        "label": "protein binding"
      },
      "evidence_type": "IPI",
      "original_reference_id": "PMID:20603015",
      "qualifier": "enables",
      "review": {
        "summary": "This IPI records interactions from the FAN1 discovery study (including FAN1/MTMR15 recruited by monoubiquitinated FANCD2). Protein binding is uninformative as an MF term.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "GO:0005515 is too generic. FAN1 recruitment by monoubiquitinated FANCD2 is a key mechanistic finding but is best represented through process/complex annotations rather than generic binding.",
        "supported_by": [
          {
            "reference_id": "PMID:20603015",
            "supporting_text": "KIAA1018/MTMR15/FAN1, that interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2"
          }
        ]
      }
    },
    "accepted_grouped_context_before_split": {
      "term": {
        "id": "GO:0005515",
        "label": "protein binding"
      },
      "evidence_type": "IPI",
      "original_reference_id": "PMID:20603015",
      "qualifier": "enables",
      "review": {
        "summary": "Resolved FAN1 and FANCI interactions support enzyme binding and heterodimerization; the imported FSCN1 context requires an identifier check.",
        "action": "MODIFY",
        "reason": "PMID:20603015 identifies human FAN1 as Q9Y2M0 and demonstrates DNA-independent coassociation with FANCD2, endogenous controls, and dependence on the FAN1 UBZ domain and FANCD2 monoubiquitination. GO:0019899 names binding an enzyme and does not require FANCD2 to catalyze or activate that enzyme. FAN1 supplies the nuclease chemistry; FANCD2 is a regulated interaction partner. The assays do not establish identical behavior of all four natural FANCD2 products. Independent human ID2 reconstitution in PMID:32269332 supports FANCI heterodimerization. The separately imported FSCN1/Q16658 context is UNDECIDED because the source identifies FAN1/Q9Y2M0; the confirmed IntAct mapping discrepancy is documented for upstream checking. These distinct partner decisions are supplied separately and must not be collapsed into one asserted partner.",
        "proposed_replacement_terms": [
          {
            "id": "GO:0019899",
            "label": "enzyme binding"
          },
          {
            "id": "GO:0046982",
            "label": "protein heterodimerization activity"
          }
        ],
        "additional_reference_ids": [
          "PMID:32269332"
        ],
        "source_defects": [
          {
            "defect_type": "WRONG_WITH_FROM",
            "resource": "INTACT",
            "record": "IM-15159-2; IM-15159-3; IM-15159-6; IM-15159-7; IM-15159-9; IM-15159-10",
            "slot": "interactor identifier / GOA With/From",
            "requested_change": "CHECK",
            "asserted_value": "UniProtKB:Q16658",
            "corrected_value": "UniProtKB:Q9Y2M0",
            "corrected_label": "FAN1, FANCD2/FANCI-associated nuclease 1",
            "cause": "SYMBOL_COLLISION",
            "confidence": "CONFIRMED",
            "explanation": "PMID:20603015 Figure 1A explicitly identifies human KIAA1018/MTMR15/FAN1 as Q9Y2M0. Figure 4 and the Methods study that 114-kDa nuclease in FANCD2 complexes. The saved current IntAct records instead identify Q16658/FSCN1 and list FAN1 as its alias. Please check the participant mapping and downstream GOA partner context against the original constructs and experiment records. No source bytes are changed here, and this does not assert that FANCD2 cannot bind FSCN1 in another setting.",
            "supported_by": [
              {
                "reference_id": "PMID:20603015"
              }
            ],
            "report_status": "NOT_REPORTED"
          }
        ],
        "supported_by": [
          {
            "reference_id": "PMID:20603015",
            "supporting_text": "KIAA1018/MTMR15/FAN1, that interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2"
          }
        ]
      }
    }
  }
]
```

The two newly adopted source contexts require GO_REF:0000107 and GO_REF:0000120 in the reference closure. The genuine seeder emitted placeholder titles; these were not accepted. Their complete official GO reference pages and existing HTTP 200 receipts were independently read, and two separate whole metadata objects with exact official titles were appended. All 48 accepted reference objects remain exact; the final total is 50. These are source-method references, not new biological experiments or normal-cache files.

## 2026-10-25 — Citation-section metadata reconciliation

The six FANCD2 `record_section` additions from PR #5481 (head `7e400719ad96920b9242c159c71df73362ca5848`) are preserved at their original annotation and supporting-reference paths. Each section was checked against the unchanged UniProt record. Only citation-location metadata is adopted; all 31 quotation texts, reference associations and paths, source contexts, review decisions, core functions and four natural products remain unchanged. The overlapping PR contains other genes whose changes are outside this review.

## 2026-10-25 — Canonical validation

All six canonical checks pass, including term labels, ontology components, source matching and rendering of all 110 narratives. Computed status is DRAFT with six advisories: four supported generic-binding rows retained as non-core under the standing campaign instruction; the unused inherited Affinage file; and the broad DNA-binding core term lacking an exact annotation row. The latter summarizes the supported DNA-binding activities without proposing a redundant ancestor annotation. All 31 original quotation paths, four natural products and prior histories are preserved. Nine genuinely fetched publication caches are added; existing sources remain unchanged. For the donor paper already present on main, the existing cache is reused: its body and bibliographic identity agree with the private fetch, which differs only in optional publication-type metadata and trailing spaces.

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Row: GO:0005739 ISO (NEW, from mouse PMID:28378742); GOA has no mitochondrion row for human
FANCD2. No sub-compartment rows.

Checks (PMID:28378742, full text cached):
- [PMID:28378742 "Cytoplasmic Fancd2 exhibited co-localization with the mitochondrial maker Mito tracker RED (Fig. 4A), suggesting that Fancd2 is also localized to the mitochondria."]
- [PMID:28378742 "Importantly, a significant amount of Fancd2 was co-fractionated with Atp5a1 in the mitochondria fraction, adding further support to mitochondrial localization of Fancd2."]
  Fraction markers were Atp5a1, GAPDH and Histone2B; no ER marker.
- Nucleoid association is by co-IP only: [PMID:28378742 "Collectively, these results suggest that Fancd2 is part of the mitochondrion nucleoid complex"]
- Atad3 knockdown removes mitochondrial Fancd2 (Fig. 4I).
- Not in MitoCarta3.0; no presequence or TM in UniProt.

Outcome: NEW ISO row kept (non-core), reason records the check. Stay at root: one study,
co-IP-only nucleoid association, no protease protection or sub-mitochondrial fractionation.
