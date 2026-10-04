---
title: Mouse Genes Annotation Re-Review
maturity: COMPLETE
tags: [EVALUATION]
autolink_gene_symbols: true
species:
  - mouse
---

# Mouse Genes Annotation Re-Review

**Bottom line:** the mouse counterpart of the
[human re-review sweep](HUMAN_GENES_RE_REVIEW.md). Every per-annotation action
in the 85 mouse review files then in the repo (11,684 annotation rows, Acadl to
Vmn2r73) was re-read and asked the same question: do I agree? Judgments were
made from the YAML, the cached publications and domain knowledge, with no new
literature search. Agreement was about 99.8%: 22 actions were changed and 3
unevidenced NEW rows deleted, in 10 genes, every one of them an application of a rule the project already
states rather than a new biological finding. The dominant pattern was the same
one the human sweep flagged as a fence: experimental (IDA/IMP/IGI) rows removed
or re-termed on the strength of an abstract-only or truncated cached record.
Those were moved to UNDECIDED, ACCEPT or MARK_AS_OVER_ANNOTATED per the
"do not overrule curators from incomplete evidence" rule. The sweep also
adjudicated the single NOT annotation, all 33 REMOVE-on-experimental rows and
all 33 NEW rows, and logged the fence cases and literature questions below.

## Purpose

A second-pass, manual re-review of the per-annotation curation **actions**
(`ACCEPT`, `KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED`, `REMOVE`, `MODIFY`,
`NEW`, `UNDECIDED`) recorded in each `genes/mouse/<Gene>/<Gene>-ai-review.yaml`,
with the same method and calibration as the human sweep:

- **Confident disagreement** → edit the YAML (action and reason), log under
  **Edits made**, add a history record.
- **On the fence / needs more evidence** → log under **Fence cases** or
  **Needs literature**, no edit.
- **Agree** → record the gene in the **Progress log**.

The digest used for the sweep lists every row with its action and shows the
reason only for non-ACCEPT/KEEP rows, so ACCEPT/KEEP rows were scanned for
whether the core function is retained on specific child terms rather than read
individually. Three REMOVE-heavy genes were checked explicitly for the "core
looks lost" digest artefact (Hdac1, Trp53, Sox2): in each the removals are
`protein binding` rows and the specific core terms are ACCEPTed.

## Status: sweep COMPLETE

All 85 mouse review files were re-reviewed. Spcs2 (a 74-residue TrEMBL
fragment, A0A140LHW5) has no GOA rows and nothing to adjudicate.

| | |
|---|---|
| Review files | 85 (84 with annotations) |
| Annotation rows | 11,684 |
| Actions changed | 22 (8 genes) |
| Rows deleted (unevidenced NEW) | 3 (2 genes) |
| Agreement | ~99.8% |

## Method notes / calibration (mouse-specific additions)

The human-sweep calibration applies unchanged. Mouse adds three recurring
situations:

- **MGI IMP phenotype rows on process terms.** A knockout phenotype is
  legitimate evidence for "involved in" even when the gene acts upstream.
  Downgrading to KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED is discretion;
  REMOVE needs the term to be wrong, not merely downstream. One row was moved
  on this ground (Ghr taurine metabolic process).
- **MGI pathway-membership rows.** MGI annotates every enzyme of a degradative
  pathway to the catabolic terms of all upstream metabolites from the same
  paper (Uox, Urah and Urad all carry deoxyinosine, dAMP, GMP ... catabolic
  process from PMID:16462750). The comparator check shows this is a convention,
  not an error, so the twelve Uox rows were moved from REMOVE to
  MARK_AS_OVER_ANNOTATED.
- **ISO rows carry a human or rat experiment behind them.** A REMOVE of an ISO
  row needs a row-specific refutation; a shared boilerplate sentence ("either an
  unsupported transfer, a paralog overreach, or ...") asserts nothing. Where the
  underlying rat finding is known (Ednra nuclear-membrane ETA receptors in
  cardiomyocytes) the row was kept as non-core.

Two further patterns were observed and are flagged for a guideline line rather
than edited row by row:

- **MODIFY as a disguised REMOVE on experimental rows.** Re-terming an IDA/IGI
  row to a sibling term from an abstract-only cache overrules the curator just
  as REMOVE does (Drd1, Dnaja3 edited; Cdc42 idx 148 left as discretion).
- **MARK where the reason states a categorical refutation.** When the reason
  says "cannot be" or "incompatible with" (Musm1 insulin receptor activity on a
  secreted lipocalin) the action should be REMOVE; the two Musm1 rows were
  aligned. Musm1 nucleus and transcription-repression rows were left as MARK
  because the MUP literature does claim intracellular hepatic signalling.
- **`protein binding` is handled three ways across mouse** (MARK on Cbl, Cdc42,
  Jak1, Grb2, Akt1; REMOVE on Hdac1, Trp53, Sox2, Notch1, Rab7; MODIFY on
  Fbxo2). All are within guideline; validation already warns on MARK.

## Completed systematic audits

- **NOT annotations.** One in the mouse set: Pld4 GO:0004630 D-type
  glycerophospholipase activity (IDA, PMID:21085684), ACCEPTed. The positive
  Reactome TAS row for the same term is correctly REMOVEd against it.
- **REMOVE on experimental evidence (IDA/IMP/IPI/IGI/IEP), excluding protein
  binding: 33 rows in 13 genes.** Thirteen were moved (Uox ×12, Ccne1 ×1, see
  below). The remaining twenty are defensible: full-text contradictions
  (Tuba1a cerebellar morphogenesis, "No anatomical abnormalities were seen in
  the cerebellum"; Agtr1a inflammatory response, effect shown AT1/AT2
  independent; Bcl2 ×5 from recovered full texts), wrong-activity calls
  (App protein phosphorylation; Casp3 CDK-inhibitor activity, a substrate's
  activity assigned to the protease), explicit name collisions in cached full
  text (Ang2 ×3, "angiotensin II (Ang II)" in a ZNF418 paper), bulk IEP
  microarray rows where the full text never mentions the miRNA (Mir100, Mir127,
  Mir26a-1), and reference-level removals where the function is retained on
  other rows (Pld4 exonuclease IMP from a 2011 localization paper).
- **NEW rows: 33 in 17 genes.** Three were dropped for lacking evidence or
  failing the comparator check (Sirt2 ×2, Ndufb1 ×1). The rest cite a PMID,
  UniProt keyword or deep-research file and are not ancestors or descendants of
  an existing accepted term (Pld4's two TLR-regulation NEWs were checked: GO:0034164
  is not a descendant of GO:0034122).

## Progress log

Genes were processed in nine size-balanced batches; all rows of every gene
were covered.

| Batch | Genes | Result |
|-------|-------|--------|
| 1 | Aldh2 Cdk5r1 Ctnnb1 Ednra Epo F2rl2 Kras Mir384 | agree; 2 edits (Ednra). Cdk5r1 p35-is-not-the-kinase MODIFYs uniform; F2rl2/Kras correctly stop at UNDECIDED on suspicious IDAs |
| 2 | Cbl Cdc42 Fbxo2 Gas6 Ifi204 Jak1 Mir100 Notch1 Rab7 | agree; 2 edits (Jak1). Cdc42 E3-ligase removal, Gas6 cytoplasm-for-a-secreted-ligand removal correct |
| 3 | Akt1 Ccnt1 Drd1 Hras Mapk3 Musm1 Ndufb1 Spcs2 Stat1 Tuba1a | agree; 4 edits (Drd1, Musm1 ×2, Ndufb1). Tuba1a REMOVEs verified against full text; Spcs2 has no rows |
| 4 | Camk2a Egf Ghr Grb2 Mtor Pten Surf1 Tert Uox Vmn2r73 | agree; 13 edits (Uox ×12, Ghr). Surf1 COX-activity→assembly MODIFY, Mtor Tyr-kinase removal correct |
| 5 | Ang2 Bcl2 Calm1 Casp3 Dnmt1 Gulo Mapk1 Scgb1a1 Top2a | agree; 0 edits. Bcl2 previously re-reviewed with recovered full texts; Casp3 aspartic→cysteine endopeptidase; Top2a abstract-mismatch IDAs correctly UNDECIDED |
| 6 | App Brca1 Calm3 Dnaja3 Dnajb11 Gapdh Grpel2 Nf1 Sirt2 | agree; 3 edits (Dnaja3, Sirt2 ×2 deletions). Gapdh is not over-pruned (4 REMOVEs, GAIT RNA-binding kept as NEW) |
| 7 | Actb Agtr1a Alpl Ccnb1 Hspa8 Mir26a-1 Sdhaf2 Serpinh1 Src Trp53 | agree; 0 edits. Serpinh1 non-inhibitory-serpin and ER-retention removals; Trp53 344 protein-binding cleanup with core TF terms ACCEPTed |
| 8 | Acadl Ccne1 Cftr Cyp1a1 Egfr Frmpd2 Fyn Hsp90aa1 Mir30e Sox2 | agree; 1 edit (Ccne1). Hsp90aa1 UTP/CTP/GTP/dATP removals; Frmpd2 NEWs all IDA-backed |
| 9 | Calm2 Edn1 Hdac1 Mir127 Myc Pld4 Slc5a1 Syk Tnfrsf1a Txn1 | agree; 0 edits. Edn1/Tnfrsf1a boilerplate MARKs are downgrades not removals; Syk 16 UNDECIDEDs are all on electronic rows (harmless) |

## Edits made

(gene — annotation — old action → new action — rationale)

- **Uox** — twelve IDA rows from PMID:16462750 (deoxyinosine, deoxyadenosine,
  deoxyguanosine, guanine, hypoxanthine, inosine, adenosine, IMP, dAMP, GMP, AMP
  and dGMP catabolic process) — REMOVE → **MARK_AS_OVER_ANNOTATED**. The cached
  record is abstract-only and MGI annotates Uox, Urah and Urad identically from
  it: a pathway-membership convention, not an error. Over-specific for the
  terminal urate-oxidation enzyme, but an experimental annotation is not removed
  on the strength of an abstract.
- **Ccne1** — GO:0016055 Wnt signaling pathway (IDA, PMID:19056892) — REMOVE →
  **UNDECIDED**. The cached "full text" is a 1,400-word extraction that mentions
  cyclin D1 but never cyclin E1, so the curator's result is not visible;
  annotation looks like an over-annotation but cannot be refuted from the cache.
- **Jak1** — GO:0004713 protein tyrosine kinase activity and GO:0018108
  peptidyl-tyrosine phosphorylation (IDA, PMID:10872802) — UNDECIDED →
  **ACCEPT**. Abstract-only cache of an APS/Lnk adaptor paper; APS is a JAK
  substrate and tyrosine kinase activity is JAK1's core function, accepted on
  seven other rows. Clearly-correct experimental rows are accepted and deferred
  to the curator.
- **Drd1** — GO:0007191 adenylate cyclase-activating dopamine receptor signaling
  pathway (IGI, PMID:17194762) — MODIFY (to the Gq/PLC sibling) → **ACCEPT**.
  The curator made paired IGI rows for both arms from the full text; the
  abstract itself contrasts the heteromer with Gs/olf-coupled D1 signalling.
- **Ednra** — GO:0031965 nuclear membrane (ISO) — REMOVE →
  **KEEP_AS_NON_CORE**; GO:0030315 T-tubule (ISO) — REMOVE → **UNDECIDED**.
  Both REMOVEs carried a shared boilerplate reason and a pigmentation
  supporting_text unrelated to the term. Nuclear-envelope ETA receptors in
  rat ventricular cardiomyocytes are a documented finding, the expected source
  of the transfer.
- **Musm1** — GO:0005009 insulin receptor activity (ISS) and GO:0008286 insulin
  receptor signaling pathway (IEA, derived from it) — MARK_AS_OVER_ANNOTATED →
  **REMOVE**. A secreted 19 kDa lipocalin cannot be a receptor tyrosine kinase;
  the reviewer's own reason said so and the action now matches it.
- **Dnaja3** — GO:0005634 nucleus (IDA, PMID:11116152) — MODIFY (to
  mitochondrion) → **UNDECIDED**. Abstract-only cache; the mitochondrial IDA
  from the same paper is already accepted on its own row, so re-terming this
  one only overruled the curator.
- **Ghr** — GO:0019530 taurine metabolic process (IMP, PMID:18648510) — REMOVE
  → **MARK_AS_OVER_ANNOTATED**. Downstream metabolomic consequence of lost GH
  signalling; not wrong, so not removed.
- **Sirt2** — NEW GO:0007049 cell cycle and NEW GO:0000226 microtubule
  cytoskeleton organization (NAS, no reference, no supporting_by, reason "core
  function term not present") — **rows deleted**; GO:0007049 also dropped from
  the matching `core_functions.directly_involved_in`, where regulation of cell
  cycle remains. "cell cycle" is an ancestor of the accepted meiotic cell cycle
  row, and neither NEW cited any evidence.
- **Ndufb1** — NEW GO:0032981 mitochondrial respiratory chain complex I
  assembly (ISS, no reference) — **row deleted** and dropped from
  `core_functions`. Comparator check fails: human NDUFB1, NDUFB10, NDUFB11 and
  NDUFB4 carry no GO:0032981 in GOA. Being incorporated into an assembly
  intermediate is being part of the product, not doing the assembly; the
  structural-molecule NEW row captures the contribution.

## Fence cases (judgment call, no edit made)

- **Alpl** — GO:0140928 inhibition of non-skeletal tissue mineralization
  (IDA+IMP, PMID:21490328) REMOVEd because TNAP hydrolyses pyrophosphate and
  promotes calcification. The paper (full text cached) does show TNAP
  overexpression increases aortic calcification, and the UniProt curator
  annotated NPP1, ANK and TNAP together as the PPi-control system. Directionally
  the REMOVE is right; a curator may prefer MARK since the term names the
  homeostatic process the enzyme participates in.
- **Tuba1a** — GO:0008542 visual learning (IMP, PMID:17218254) REMOVEd. The
  full text has no visual-learning assay (T-maze working memory impaired,
  tactile reference memory intact), so the REMOVE is defensible, but the
  specific assay MGI mapped to this term is unknown.
- **Ctnnb1** — GO:0007173 EGFR signaling pathway (ISO/IEA) REMOVEd while an
  equally thin ISO row (response to cytokine) was left UNDECIDED; beta-catenin
  is an established EGFR substrate. Discretion on electronic rows.
- **Cdc42** — GO:0006468 protein phosphorylation (IMP) MODIFYed to small GTPase
  signalling; GO:0001934 positive regulation of protein phosphorylation would
  preserve the curator's observation. GO:0005819 spindle (IEA) REMOVEd while
  mitotic spindle and spindle midzone are ACCEPTed; MARK would be conventional.
- **Fbxo2** — NEW GO:0070492 oligosaccharide binding is a descendant of the
  ACCEPTed GO:0030246 carbohydrate binding IDA; cleaner as MODIFY of that row.
- **Notch1** — IBA GO:0007411 axon guidance REMOVEd on family-composition
  grounds (SLIT-seeded node); the most aggressive IBA call in the set, though
  axonogenesis IMP/IDA rows are retained. Acrosomal vesicle ISO REMOVEd where
  UNDECIDED would be safer.
- **Dnaja3** — ISO binding rows (NF-kappaB, IKK complex, TF binding) REMOVEd
  as "not supported locally"; the human source annotations are IPI-based, so
  MARK would be conventional.
- **Dnajb11** — ISO nucleus/cytoplasm REMOVEd as "likely artifactual" while the
  IDA rows for the same compartments are UNDECIDED; inconsistent but harmless.
- **Mtor** — ISO/IEA RNA polymerase III promoter DNA-binding rows REMOVEd; the
  human source is ChIP occupancy of Pol III genes, so MARK fits better than a
  "mis-assignment" claim.
- **Pld4** — GO:0045145 ssDNA exonuclease (IMP, PMID:22102906) REMOVEd as a
  reference-level error (2011 localization paper predates the nuclease
  discovery); function retained on other rows.
- **Ghr** — fourteen ISO rows REMOVEd with "too downstream"/"over-transfer"
  reasons where MARK would be conventional; one IMP row edited (above), the
  rest are electronic and left as discretion.
- **Edn1 / Agtr1a / Tnfrsf1a / Casp3 / Actb** — large blocks of
  MARK_AS_OVER_ANNOTATED carried by one boilerplate sentence each, including
  some IDA/IMP rows (Edn1 MAPK cascade IDA/IMP; Casp3 none). Downgrades, not
  removals, so no edit; but a REMOVE should never ride a template sentence.

## Needs literature (cannot adjudicate from YAML + cache)

- **Ednra** — which RGD record seeds the T-tubule and nuclear-membrane ISO
  rows, and does it show ETA at both sites in cardiomyocytes?
- **Jak1** — GO:0098761 cellular response to IL-7 and GO:0036016 cellular
  response to IL-3 (IDA): do the papers show a JAK1 requirement, or only JAK1
  presence in a JAK3/JAK2-dominant complex?
- **Fbxo2** — GO:0001540 amyloid-beta binding (IDA, PMID:9173930): was Abeta
  binding assayed directly, or is this a PrP/Abeta conflation?
- **Mir100** — GO:0071475 hyperosmotic salinity response (IDA, PMID:17028171):
  the cached PMC text is about miR-7b and never mentions miR-100.
- **Ndufb1** — did any accessory-subunit knockout series (Stroud 2016) include
  NDUFB1 with loss of complex I assembly? If so the deleted NEW could return on
  IMP-equivalent evidence.
- **Ccne1** — the full text of PMID:19056892: what cyclin E1 result supports
  the Wnt-pathway IDA?

## Related

- [Human Genes Annotation Re-Review](HUMAN_GENES_RE_REVIEW.md) — method and
  calibration.
- [IBA Review](IBA_REVIEW.md) — the September 2026 propagation re-review that
  already covered Bcl2 and other mouse genes in depth.
