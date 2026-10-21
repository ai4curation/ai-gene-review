# Akt1 review notes

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: this review keeps conserved kinase and canonical PI3K/insulin signaling functions, while removing or downranking many donor-derived developmental, neuronal, immune, stress-response, and context-specific terms as ISO over-annotation.

## 2026-10-10 - OpenScientist kinase-inhibitor follow-up

The focused OpenScientist report for `prediction-kinase-inhibitor-activity`
supports keeping GO:0030291 `protein serine/threonine kinase inhibitor
activity` as REMOVE. PMID:8524413 shows Akt/PKB catalytically phosphorylating
GSK3 on inhibitory serines; the decreased GSK3 activity is the downstream
result of AKT1 kinase signaling, not a stoichiometric molecular function in
which AKT1 binds and inhibits a protein serine/threonine kinase.

## Re-review 2026-10-10

### What GOA changed (refresh in commit a3cf70b6d)

- 40 new rows were seeded as PENDING. Most (36) are WITH/FROM or qualifier splits of terms already reviewed: ISO rows now listing human AKT1 (UniProtKB:P31749), mouse Akt1 (MGI:MGI:87986), or RGD:13974772 (pig AKT1, confirmed by RGD REST lookup) as separate donors, plus UniProt ISS rows from mouse Akt1 (P31750).
- The genuinely new rows are: plasma membrane EXP (PMID:9228007), ATP binding IEA (ARBA/InterPro), protein localization to mitochondrion ISO from human AKT1, and IPI splits for PKC binding (WITH RGD:62390), protein binding with Smad3 (P84025), and GSK3B (P18266) for the kinase inhibitor activity and kinase binding rows.
- 12 rows are retired (GOA no longer carries them). Their reviews are kept, and a sentence noting the withdrawal was added to each reason.

### Resolution of PENDING rows

- Core MF/pathway donor splits were accepted: Ser/Thr kinase, serine kinase, insulin receptor signaling, and PI3K/PKB signaling. Generic protein kinase activity and kinase activity were set to MODIFY -> GO:0004674.
- Localization splits (nucleus, cytoplasm, cytosol, plasma membrane, mitochondrial intermembrane space) are KEEP_AS_NON_CORE, consistent with their siblings.
- Plasma membrane EXP: UniProt records cell-membrane targeting from Stokoe et al. [PMID:9228007 "Its binding to the pleckstrin homology domain of PKB was required to allow phosphorylation by the upstream kinase"].
- Protein localization to mitochondrion ISO: MARK_AS_OVER_ANNOTATED. The human donor IMP used pan-AKT inhibition in a mitophagy assay [PMID:23962723 "Mitochondrial parkin recruitment was attenuated with AKT inhibition"].
- Smad3 protein binding: REMOVE. The paper argues that Akt acts on Smad3 through its kinase activity and mTOR, not through binding [PMID:16362038 "These and further data on Akt1-S3 binding do not support a recently proposed model that Akt blocks S3 activation through physical interaction"].
- PKC binding split: the WITH entity RGD:62390 resolves to rat Akt3, not a PKC isoform, so the WITH field looks inconsistent with the term. The row was kept as non-core on the paper-level claim [PMID:7488143 "the pleckstrin homology domain of the three subtypes of RAC-PK associate with both protein kinase C subspecies"]. The sibling row's WITH RGD:2802 resolves to Hmgb1 in the RGD REST API, which is also odd.
- Kinase activity ISO (row from mouse Akt1): the earlier review said neither donor still carried the generic term. QuickGO (2026-10-10) shows both do (human IDA PMID:14749367; mouse IDA PMID:23886629), so the source_status was corrected.

### Re-audit changes to existing rows

- **Protein binding (GO:0005515):** all 8 rows (3 retired) remain REMOVE. Each now has a partner- and paper-specific reason and states that removal does not mean the interaction is false. No cited abstract supports a more informative MF term.
- **Experimental REMOVE rows** were re-checked against the policy against overruling curators:
  - dendrite IDA (PMID:31071414): REMOVE -> KEEP_AS_NON_CORE. The full text reports [PMID:31071414 "pAKT-ir is found primarily in CA1 pyramidal cells and, to a lesser extent, in dendrites within SO and SR"].
  - negative regulation of calcium import into the mitochondrion IMP (PMID:24601882): REMOVE -> MARK_AS_OVER_ANNOTATED. The abstract supports it in an ischemia-reperfusion model [PMID:24601882 "suppressed mitochondrial calcium overload"].
  - spinal cord development IDA (PMID:23681769): REMOVE -> MARK_AS_OVER_ANNOTATED. The evidence is age-dependent p-Akt levels.
  - protein phosphatase 2A binding IPI (PMID:11884620): REMOVE -> KEEP_AS_NON_CORE, deferring to the curator. The abstract is about PP2A-Shc, and the full text is unavailable.
  - negative regulation of cell size IDA (PMID:16286931): REMOVE -> UNDECIDED. The abstract is about Tsc1/Tsc2, and the full text is unavailable.
  - positive regulation of apoptotic process IMP (PMID:20403980): REMOVE -> MARK_AS_OVER_ANNOTATED [PMID:20403980 "blockade of PKB activity caused significant reduction of CK release and cell death"].
  - positive regulation of vasoconstriction IMP (PMID:21532183): kept as REMOVE, with a new reason. The abstract states the opposite direction [PMID:21532183 "pravastatin inhibits constrictor responses by increasing endothelial NO bioavailability via the Akt pathway"].
  - enzyme binding IPI (PMID:10454575): kept as REMOVE (generic term), with the policy wording added.
- **Summaries:** 69 summaries on IBA, IEA, ISS, TAS, IDA, IMP and IEP rows wrongly began "The rat ISO traces to mouse Akt1 and human AKT1". They were rewritten to describe the actual evidence source. Rat-specific wording was dropped where the abstract shows non-rat cells (e.g. 3T3-L1 adipocytes in PMID:10454575 and PMID:9632753).
- **UniProt quotes:** 9 stale quotes (DR GO lines whose evidence codes changed) and 34 self-referential DR GO quotes on IBA, IEA, ISS, TAS and core ISO rows were replaced with CC-line quotes (FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, DOMAIN) or deep-research quotes. 131 quotes on legacy (mostly ISO) rows still cite DR GO lines; these are present in the current flat file but are weak support.
- **Description:** rewritten as standalone biology. The ISO over-annotation commentary was removed.
- **core_functions:** unchanged (protein serine/threonine kinase activity; PI3K/PKB signaling; insulin receptor signaling).

### Open questions

- GO:0045907 positive regulation of vasoconstriction (IMP, PMID:21532183): the abstract's conclusion runs opposite to the term. Is the RGD annotation a direction error that should be GO:0045906?
- GO:0045792 negative regulation of cell size (IDA, PMID:16286931): this needs a full-text check. It is inconsistent with AKT1's growth-promoting role.
- PMID:7488143 PKC binding rows: should RGD fix the WITH fields (RGD:62390 = Akt3, RGD:2802 = Hmgb1)?
- Many legacy ISO rows use REMOVE for donor phenotypes judged too context-specific (e.g. inflammatory response, neuron projection development). MARK_AS_OVER_ANNOTATED may describe these better, since the donor evidence is experimental. They were left unchanged in this pass for consistency. (Resolved 2026-10-17; see "Review follow-up 2026-10-17" below.)

### Review follow-up 2026-10-17

Changes made in response to the PR #4628 review:

- **MODIFY reasons:** the four GO:0004672 MODIFY rows that are not ISO (IEA GO_REF:0000002; IDA PMID:9112399, PMID:7774014, PMID:12084817) no longer say "transferred ISO term". Each reason now states the actual basis: an InterPro domain mapping, or a rat assay of a serine/threonine kinase. Their title-only quotes were replaced with abstract sentences. The three genuine ISO rows keep the original reason.
- **Open question 4 resolved:** the 38 legacy ISO REMOVE rows with the boilerplate "too narrow" reason (plus the two donor-split siblings) were re-reviewed one by one:
  - 27 contextual donor phenotypes became MARK_AS_OVER_ANNOTATED, with a per-row reason naming the donor study. They now use `root_cause: NO_FAILURE_NON_CORE` and `SUPPORTS_TRANSFER`, because the donor evidence is experimental and no rat divergence is argued.
  - GO:0010629 became MARK_AS_OVER_ANNOTATED for GRANULARITY_MISMATCH, consistent with GO:0010628.
  - Locations no longer carry CONTEXT_OR_TISSUE_MISMATCH. Ciliary basal body is KEEP_AS_NON_CORE (activated Akt-1 seen at the basal body, PMID:19596798). Cell-cell junction and spindle are MARK_AS_OVER_ANNOTATED (one immunological-synapse study; a phospho-epitope survey).
  - Five rows stay REMOVE with a participation argument (TERM_SCOPING_PROBLEM / ROLE_CONFLATION). Protein ubiquitination and protein catabolic process: Mdm2 does the ubiquitination, and AKT1 regulates Mdm2. Execution phase of apoptosis: AKT1 is a caspase substrate cleaved at Asp-462. Apoptotic mitochondrial changes: AKT1 opposes them. Gene expression: AKT1 is a regulator, not a participant.
  - Re-grounding moved three rows to KEEP_AS_NON_CORE. GO:1903898: Akt phosphorylates PERK Thr-799 (PMID:21954288). GO:2000010: GLUT4 translocation in rat adipose cells (PMID:9415393). GO:0010975 (ISO, ISS and the donor split): UniProt FUNCTION text plus PMID:19778506.
- **Re-grounding of the self-referential rows the reviewer named:**
  - GO:0099104 potassium channel activator activity (ISO and ISS) is now KEEP_AS_NON_CORE. PMID:33505021 shows TMEM175 is opened by a conformational change in AKT, not by its catalytic activity, which contradicts the earlier "kinase-substrate event recast as activator" reasoning.
  - GO:1902018 is now KEEP_AS_NON_CORE, grounded on the WDR44/Rab11 mechanism (PMID:31204173). The uncited "opposite signs" claim was dropped.
  - GO:0150033 is now KEEP_AS_NON_CORE, grounded on Akt-mediated TSC2 phosphorylation (PMID:24529379).
  - GO:0060416 stays MARK_AS_OVER_ANNOTATED. It is now grounded on the bovine donor IDA (PMID:16698222, fetched for this pass), in which GH acts indirectly through IGFBP-5.
- **GO:0045907:** changed from REMOVE to MODIFY with GO:0045906 negative regulation of vasoconstriction (verified on QuickGO), because PMID:21532183 supports the negative direction.
- **suggested_questions:** a new section holds the GO:0045907 direction question, the PMID:7488143 WITH-field question (RGD:62390 = Akt3, RGD:2802 = Hmgb1) and the GO:0045792 cell-size question.
- **Remaining work:** 108 rows, mostly the KEEP_AS_NON_CORE ISO tail, still cite only the UniProt DR GO line. Re-grounding them is left for a later pass, as the reviewer allowed.

### Review follow-up 2 (2026-10-17)

Changes made in response to the second review on PR #4628:

- **Non-ISO rows with the ISO boilerplate:** three rows still had the reason "the transferred term is too specific to retain as a general rat ISO annotation", and none of them is ISO. All three are fixed:
  - GO:1901653 (IEP, PMID:18772167) and GO:0019901 (IPI, PMID:24583056, WITH mTOR RGD:68371) now give their rat-direct basis. Both stay MARK_AS_OVER_ANNOTATED: one is a generic stimulus class, the other a generic binding MF.
  - GO:0042981 (ISS) and its ISO sibling are now MODIFY to GO:0043066 negative regulation of apoptotic process. The summary had argued the term was too general while the reason said too specific. Both rows' support is anti-apoptotic (UniProt IGF1 line; donor IDA PMID:18977203).
  - No reason string anywhere in the file still describes non-ISO evidence as a transfer. All 12 copies of that boilerplate are gone.
- **CONTEXT_OR_TISSUE_MISMATCH on terms that are not contexts:**
  - Relabelled GO:0050821, GO:0045944, GO:0010628 (both rows), GO:1901653 (ISO) and GO:0019901 (ISO). They are now TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH or NO_FAILURE_NON_CORE, with `SUPPORTS_TRANSFER`.
  - Osteoblast differentiation (both rows) keeps CONTEXT_OR_TISSUE_MISMATCH, because it is a genuine cell-type context, but now uses NO_FAILURE_NON_CORE.
  - Re-grounding moved GO:1904515 positive regulation of TORC2 signaling to KEEP_AS_NON_CORE (MAPKAP1/SIN1 feedback, UniProt).
  - It also moved GO:0032436 (both rows) to KEEP_AS_NON_CORE (Akt phosphorylation of Mdm2, PMID:12145204). The removed ubiquitination and catabolism rows therefore now point at a kept regulation row.
- **GO:0032991 protein-containing complex:** I tried TOO_GENERAL, but the validator showed that no more specific complex term is asserted in this review, so the action's definition is not met. The row stays MARK_AS_OVER_ANNOTATED.
- **Smaller fixes:** the GO:0005829 cytosol title-only quote is now the fractionation sentence from PMID:9112399. The capitalisation typo is fixed, and 4 cited references were added.
