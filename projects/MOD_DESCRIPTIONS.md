---
title: "MOD gene descriptions as review input"
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
species: [worm, yeast, DROME]
autolink_exclude: [MOD, MODS, GET3, EGF]
manifest:
  slides:
    - href: MOD_DESCRIPTIONS/slides/MOD_DESCRIPTIONS-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/Uak8ttS9nu4C36Fh9JypKg
      title: Project brief
index_group: CROSS_CUTTING
---

# MOD gene descriptions as review input

**Bottom line:** model organism databases (MODs) publish hand-written gene
descriptions, for example WormBase's paragraph for
[rab-11.1](https://www.alliancegenome.org/gene/WB:WBGene00004274). This project
fetches them for every worm, yeast and fly gene we review, saves each as a
deep-research source, scores it against our review, and acts on what it finds.

| | Worm (WormBase) | Yeast (SGD) | Fly (FlyBase) |
|---|---|---|---|
| Genes reviewed (at the time of each run) | 452 | 890 | 539 (+8 new reviews) |
| With a curated MOD description | 385 (85%) | 890 (100%) | 345 (64%) (+8) |
| Median MOD text length (words) | 75 | 33 | 37 |
| MOD text correctness, 1-5 (UniProt) | 4.2 (4.5) | 4.8 (4.6) | 4.7 (4.6) |
| Description-text defects recorded (MOD + UniProt) | 131 (90 + 41) | 92 (47 + 45) | 85 (43 + 42) |
| Of which cite a quoted paper as evidence | 121 | 84 | 82 |
| Of which recorded as `CONFIRMED` | 50 | 40 | 32 |
| Reviews edited in the follow-up | about 60 | 249 | 124 |
| NEW annotation rows | 1 | 2 | 1 (+2 in new reviews) |

What we learned:

- **The MOD text is a recall checklist, not an authority.** Our review descriptions
  are usually more mechanistic and more current. The MOD text still names roles,
  phenotypes and regulators our reviews had missed. fshr-1's synaptic role is the
  clearest case: the worm review never mentioned it.
- **SGD and FlyBase are the most accurate sources, WormBase the least.** SGD and
  FlyBase score above UniProt on correctness; WormBase scores below it. UniProt is
  often the more informative source, especially for fly.
- **Most errors are stale, transferred or copied text, in both MOD and UniProt
  descriptions.** There are 308 recorded defects, 180 in MOD text and 128 in UniProt
  text: 204 wrong or outdated statements, 103 omissions and one wrong citation. 287 cite
  a quoted paper as evidence, and 122 carry the reviewer's `CONFIRMED` confidence (the
  rest are `PROBABLE`, apart from one `SUSPECTED`); the two measures do not coincide. Typical cases are a claim later
  overturned (FlyBase says amon cleaves Slit; Tolkin is the Slit protease), text carried
  over from another species (UniProt gives fly SCAP the mammalian sterol-sensing
  mechanism) and a copy error (UniProt names Gurken, another ligand, as the receptor for
  Spitz). Each defect quotes the offending sentence, and `just export-source-defects`
  turns them into per-resource reports. Filing those reports is a manual step that has
  not been done yet.
- **How the defects are counted.** [defect_tally.py](MOD_DESCRIPTIONS/defect_tally.py)
  counts the `WRONG_STATEMENT`, `OUTDATED_STATEMENT` and `MISSING_STATEMENT` defects
  (plus one worm `WRONG_REFERENCE`) on the cited MOD and UniProt files in `genes/worm`,
  `genes/yeast` and `genes/DROME`, and writes them with their quotes and evidence to
  [defect-tally.yaml](MOD_DESCRIPTIONS/defect-tally.yaml) (as of 2026-11-17). Other source
  defects in those folders, mostly on GO annotations, are left out. The total was 262 on
  2026-11-02; reviews merged by 2026-11-15 added 10, the nine new worm reviews of
  2026-11-16 added 26 (see [More worm genes](#more-worm-genes-2026-11-16)), and the eight
  new fly reviews added 10 (see
  [Fly: new reviews](#fly-new-reviews-of-genes-with-non-duplicative-iba-rows)).
- **Gaps rarely become annotations.** 794 gap and discrepancy findings produced 3
  NEW rows (yeast MIH1 and HOG1, fly Tango5); the fourth, worm fshr-1, came from the
  hand comparison. Most gaps are mutant phenotypes, which show that the gene is needed,
  not that it does the work, so they become description sentences instead.
- **The Alliance automated text is the weakest source.** It is generated from the
  GO annotations under review, so it is never cited as evidence, and it scores lowest
  on every species. Several automated texts have also lost content between releases,
  listed in [alliance-automated-regressions](MOD_DESCRIPTIONS/alliance-automated-regressions.md).
- **No other MOD adds anything.** MGI's note is a phenotype summary, RGD's is
  automated text, and ZFIN and Xenbase have none.

**Decision (2026-10-30): treat the curated description as a deep-research
source**, the same way as Affinage. It is written verbatim to
`<gene>-deep-research-<mod>.md` (`wormbase`, `sgd`, `flybase`) by
`just mod-description-deep-research`. It is cited as a `file:` reference, and the
reviewer's judgment goes in `references[].reference_review`. The source is sparse,
uncited, undated and only partly trusted, but no new data structures or processes
are needed for it. See [Deep-research integration](#deep-research-integration).

The work began with repairs. A fetcher and sidecar format existed
(`ai-gene-review fetch-descriptions`, `<gene>-descriptions.yaml`). They had only been
run on 118 yeast genes, nothing in `fetch-gene` or the reviewer skills read the
files, and the fetcher had stopped working. The Alliance API had changed its response
shape, and the worm cross-reference was parsed wrongly. Both are now fixed.

## Data and method

- Fetch: `uv run ai-gene-review fetch-descriptions-bulk worm`. This writes
  `genes/worm/<gene>/<gene>-descriptions.yaml` with UniProt FUNCTION, Alliance
  curated (`Alliance_Imported`, the MOD's own hand-written text), Alliance
  automated, and NCBI RefSeq summaries.
- Alliance now returns synopses as `gene.relatedNotes` with
  `noteType.name` set to `MOD_provided_gene_description` (curated) or
  `automated_gene_description`. The old `geneSynopsis` keys are gone, so the
  previous code returned nothing without raising an error.
- Compare: [compare_descriptions.py](MOD_DESCRIPTIONS/compare_descriptions.py)
  writes [worm-comparison.yaml](MOD_DESCRIPTIONS/worm-comparison.yaml), which
  lists, per gene, the WormBase content words that do not appear in our
  `description`. This is a lexical pointer for choosing genes to read, not a
  quality score.

| Measure (worm) | Value |
|---|---|
| Genes fetched | 432 |
| With curated WormBase description | 374 |
| Median words, WormBase curated | 75 |
| Median words, our `description` | 143 (139 before the follow-up) |
| Median share of WormBase content words found in ours | 0.37 (0.35 before the follow-up) |

Acting on the findings (below) raised both numbers: the descriptions gained
sentences for verified gaps, so more of the WormBase content now appears in them.

## Hand comparison (16 genes)

There were eight lowest-overlap genes (cep-1, let-60, fshr-1, lgg-2, gst-4,
mpk-1, ced-4, atg-18) and eight random ones (skn-1, sup-17, fasn-1,
hsp-16.41, rsks-1, lag-2, gpr-1, lipl-4). Low lexical overlap mostly reflects
different emphasis, not error.

**Gaps in our reviews that WormBase points to**

- fshr-1: WormBase describes a role in acetylcholine release at neuromuscular
  synapses (a large-scale synaptic screen; FLP-1 and NLP-12 are possible
  ligands). Our review is entirely about intestinal innate immunity and stress,
  and neither the review YAML nor the notes mention synapses or acetylcholine.
  This needs a follow-up literature check.
- gst-4: WormBase describes a putative prostaglandin D synthase needed for
  sperm guidance towards an oocyte PUFA signal. Our description frames GST-4
  only as a SKN-1-induced detoxifying GST. The review raises the prostaglandin
  question only in a suggested question.
- cep-1: WormBase mentions meiotic chromosome segregation and hypoxia
  sensitivity. The review YAML covers them, but the description does not.
- let-60 and mpk-1: WormBase lists phenotypes our short descriptions omit (male
  spicule, sex myoblast migration, chemotaxis, pachytene progression,
  NOS-3/TRA-1 regulation in the germline). For let-60 none of these appear
  anywhere in the review. For mpk-1 they appear in the annotations but not in
  the description.
- lag-2 and skn-1: WormBase gives detailed expression patterns and their
  regulation (LET-23/SUR-2 regulation of lag-2 in the vulval precursor cells),
  which our descriptions largely leave out.

**Where WormBase is stale or weaker**

- ced-4 is still a "novel protein" with sequestration by CED-9 to membranes. It
  has no apoptosome and no Apaf-1 homology.
- lgg-2 is said to have "no obvious function" and a speculative MAP1
  microtubule role. Our review describes its established autophagosome
  maturation role through VPS-39/HOPS.
- rsks-1 is a "putative" S6K, and hsp-16.41 is a "passive ligand". The
  WormBase texts were written years ago and, like UniProt FUNCTION text for
  yeast SAN1 in the earlier pilot, are not updated as the field moves.
- Several WormBase texts contain formatting damage (words run together, such as
  "PUFA-basedsignal"), which suggests they were not cleaned when imported.

## Deep-research integration

- **Emit:** `just mod-description-deep-research <org> [genes...]`
  (`src/ai_gene_review/etl/mod_description_deep_research.py`). The file holds
  the curated note exactly as served, including WormBase's run-together words,
  with frontmatter recording provider, `authorship` (MOD curators),
  `source_url`, MOD gene id, UniProt accession, fetch date, and
  `citations_provided: false` / `authoring_date_provided: false`. As with the
  Affinage emitter, it contains no AIGR judgment.
- **Only the curated note is used.** The Alliance automated description is
  generated from GO annotations, so citing it would cite the annotations under
  review as evidence for themselves.
- **Wrong-gene check:** the MOD id comes from the UniProt cross-reference.
  Writing is refused (unless `--force`) when the symbol or systematic name of
  the Alliance record matches neither the folder nor any UniProt gene name.
  Human is out of scope.
- **Reviewer guidance** (review and annotation-reviewer skills): run the
  emitter for every non-human review, check each claim, and record a verdict in
  `reference_review`. A claim found only in the MOD text is a lead for a
  literature search.
- The `DEEP_RESEARCH` publication type now covers external narrative sources
  in general, not only AI reports. The frontmatter records authorship.
- `<gene>-descriptions.yaml` stays as the input for the description comparison
  ([compare_descriptions.py](MOD_DESCRIPTIONS/compare_descriptions.py)). It is
  not a review source, because it stores the source text together with our AI's
  rubric scores.

**Worked example: fshr-1.** The WormBase text led to Buckley et al. 2024
(PMID:39561202). That paper shows that intestinal FSHR-1 is necessary and
sufficient for acetylcholine release at the neuromuscular junction, with
GSA-1/Gas and ACY-1 acting downstream and the glycoprotein hormone subunits
GPLA-1 and GPLB-1 upstream. The review now has a NEW
`GO:1900075 positive regulation of neuromuscular synaptic transmission` (IMP)
row, a corrected description (which had wrongly said FSHR-1 had been
"repurposed" away from hormone signaling), stronger support for the IBA
adenylate-cyclase row, and updated open questions. The WormBase reference's
`reference_review` records which claims were traced (synaptic role) and which
were judged stale (FLP-1 and NLP-12 as candidate ligands).

## Description reviews (all 432 worm genes)

The review of each text is stored in the gene's `<gene>-descriptions.yaml`,
separate from both the gene review and the deep-research file. Every source
(UniProt FUNCTION, WormBase curated, Alliance automated, RefSeq) gets a 1–5
score on correctness, utility, compactness, completeness and specificity, with a
note. The file also gets an `overall_concordance` score across sources and
`findings` (gap, discrepancy, insight). All 432 worm files are `COMPLETE`
(`ai-gene-review descriptions-status worm`). Scores are AI judgments made
against each gene's review and the literature it cites. 16 genes were scored by
hand, and parallel agents scored the other 416, calibrated on those 16. Their
output was schema-checked, and several of their
discrepancy calls (sem-5, spg-7, met-2) were spot-checked against the reviews.

| Source (genes) | Correctness | Utility | Compactness | Completeness | Specificity |
|---|---|---|---|---|---|
| UniProt FUNCTION (315) | 4.5 | 3.7 | 3.7 | 3.5 | 3.7 |
| WormBase curated (374) | 4.2 | 3.4 | 3.6 | 3.1 | 3.3 |
| Alliance automated (432) | 3.9 | 2.7 | 4.0 | 2.6 | 2.7 |

Concordance across sources: mean 4.25 (5: 187 genes, 4: 177, 3: 57, 2: 10, 1: 1).
RefSeq is left out of the table. It is usually a copy of the Alliance automated
text, but for about a third of genes it comes from an older or newer Alliance
release and was scored separately.

The 313 findings (142 gaps, 105 discrepancies, 66 insights; one lgg-2 discrepancy
was added later) are collected in
[worm-findings.yaml](MOD_DESCRIPTIONS/worm-findings.yaml), which is a curator
worklist. Recurring patterns:

- **Stale WormBase "no obvious function" texts.** Twelve WormBase texts score 2
  or less on correctness. Most say "no obvious function in mass RNAi assays"
  for genes with established mutant phenotypes: atg-2, atg-3, atg-5,
  atg-16.2, lgg-2, gst-44 and pef-1. meg-3 is described as a somatic protein,
  but it is the germline P-granule scaffold.
- **WormBase or UniProt contradicting the review.** Examples: SEM-5 "negatively"
  regulating vulval induction (both sources); spg-7 called the paraplegin
  ortholog (it is AFG3L2; ppgn-1 is SPG7); MET-2 as an H3K36 methyltransferase
  (it is H3K9); SDF-9 as an active phosphatase (it is a pseudophosphatase);
  akt-2 single mutants as dauer-constitutive.
- **Mammalian text carried over in UniProt.** Examples: "motile cilium" for
  the non-motile worm sensory cilia (dyf and osm genes, ift-20); myelin and
  sebaceous-gland roles for fath-1; SHH signaling for ift-81.
- **Automated texts that lead with removed or over-annotated terms.** Examples:
  slicer (RNA endonuclease) activity for WAGO Argonautes that lack the catalytic
  residues (wago-1, wago-4, hrde-1); kinase activity for the vps-15 pseudokinase;
  protein tyrosine phosphatase rather than PIP3 phosphatase for daf-18.
- **Regressions in the current automated text.** For ced-5, che-2, daf-15,
  nud-1, ppgn-1 and nsy-1, the current Alliance text has lost function
  sentences (and, for nsy-1, its core MAP3K activity) that the older RefSeq copy
  still carries. This is worth reporting to the Alliance.
- **Gaps in our reviews.** Some MOD claims appear nowhere in the review and
  are leads for follow-up. Examples: bbs-1/2/5/7/8/9 dense-core-vesicle
  secretion phenotypes, ddb-1 in LET-23 vulval signaling, lys-1 regulators,
  gsk-3 axon guidance, and the let-60 phenotypes.

## Follow-up: acting on the findings

The 244 gap and discrepancy findings (216 genes) were each checked against the
literature, and acted on under the CLAUDE.md curation rules. Parallel agents did
the work; each edited gene was validated and given a history record. Batch
results were spot-checked (pek-1, lrx-1, sem-5).

- **Upstream defects:** 100 errors in description text across 93 genes (73
  WormBase, 27 UniProt) are now recorded as `source_defects` on the cited
  reference: 31 WRONG_STATEMENT, 28 OUTDATED_STATEMENT, 40 MISSING_STATEMENT and 1
  WRONG_REFERENCE. Of these, 28 were recorded as CONFIRMED and the rest as
  PROBABLE. `just export-source-defects` writes them to
  `reports/source-defects/WORMBASE.md` and `UNIPROT.md` for filing. Examples:
  - UniProt says IRE-1 retains unspliced mRNAs, but its cited paper says the opposite.
  - UniProt names nlp-29 as its own receptor; the receptor is NPR-12.
  - UniProt's sma-9 FUNCTION text cites an unrelated paper.
  - WormBase says the GPR-2 GoLoco motif is a GEF feature.
  - WormBase says SOD-2 promotes lifespan, but sod-2 mutants are long-lived.
  - WormBase calls ASNA-1 a membrane transporter, but it is the GET3 targeting ATPase.
- **Our reviews:**
  - About 60 descriptions gained sentences for verified gaps. Examples include
    the let-60 phenotypes, the BBS dense-core-vesicle secretion phenotypes and
    the sem-5 PLC-gamma/PI3K outputs.
  - No NEW annotation rows were added. Every gap was an indirect or
    pleiotropic phenotype that does not meet the NEW bar.
  - Four reviews were corrected where they, not the source, were wrong:
    - pek-1: pek-1;atf-6 silencing has no phenotype (PMID:16184190).
    - lrx-1: its own analysis wrongly rejected the LDL-A repeats that Pfam,
      SMART and CDD detect.
    - lys-1: it is a screened candidate, not an established DAF-16 target.
    - gcy-8: GCY-18 also contributes to the role.
- **Unverified:** about 30 claims could not be traced to a paper (for example
  gcy-23 lifespan and rps-23 vulval morphogenesis). They are noted in the
  reference's `review_notes`, with no annotation change.
- **Alliance:** nine automated descriptions lost content that the RefSeq copy
  of an earlier release still has; see
  [alliance-automated-regressions.md](MOD_DESCRIPTIONS/alliance-automated-regressions.md).
- **Open:** the apa-2 review removes "GTPase activating protein binding" because
  RME-6 is a GEF, but RME-6 also has a RasGAP-related domain (PMID:15895077).
  The lrx-1 suggested questions look as if they belong to another gene. Both need
  a human look.

## More worm genes (2026-11-16)

This round applied the standing rule (the WormBase text is an input to every new worm
review) to new genes, and brought the reviews added after the worm run into the
comparison. Worm now has 452 scored sidecars, all `COMPLETE`, and 385 of them (85%)
have a WormBase-written description.

- **Eleven later reviews.** F54F2.7, T04F3.1, Y54E10BR.2, abhd-11.1, abhd-11.2,
  abhd-14, abi-1, acbp-5, cec-10, npp-20 and pnk-1 were reviewed after the worm run and
  had no sidecar. All were fetched and scored. Only abi-1 and acbp-5 have WormBase text,
  and both reviews already cite it as a deep-research source. The 18 findings are mostly
  automated texts that lead with terms the reviews reject:
  - transaminase activity for T04F3.1;
  - phosphatase activity for pnk-1, which keeps the pantothenate kinase catalytic residues;
  - fungal Swi6-family G1/S transcription terms for cec-10;
  - a fission-yeast septum term for npp-20.

  No review needed an edit.
- **Decision (2026-11-16): score only genes with a curated MOD text.** Scoring
  sidecars whose only texts are the Alliance automated one and its RefSeq copy is not
  worth the effort. Those texts are generated from the GO annotations under review, so
  scoring them repeats the annotation review. They are also never written as
  deep-research files. The nine automated-only sidecars in this round (abhd-11.1, for
  example) produced no review edits; the curated ones (cki-1, for example) are where the
  findings come from. From now on, an automated-only sidecar is fetched for the
  comparison table and left unscored. Existing scores are kept.
- **Choosing new genes.** Candidates were genes that the WormBase texts of reviewed
  genes name but that have no review of their own. They were ranked by how many texts
  name them ([worm_candidates.py](MOD_DESCRIPTIONS/worm_candidates.py)). For example, mes-1 is named in the texts for gpr-1, gpr-2, meg-1 and meg-2,
  and mec-3 in those for cct-2, cct-4, mec-14 and ric-4. The top of the raw ranking
  holds non-genes, which were dropped: human bcl-2, and mkrs-1, a misspelling of mksr-1.
  (A first version of the script also listed hsp-16, by cutting hsp-16.41 at the
  dot; the committed script reads the full name.) So was lag-3, which is sel-8 (Q09260) and already reviewed
  under that name. Nine genes with a Swiss-Prot entry and a WormBase text were reviewed,
  in three related groups:
  - touch-neuron fate transcription factors: egl-44, egl-46, mec-3;
  - germline P-lineage regulators: pie-1, pos-1, mes-1;
  - signalling outputs and cell-cycle control: lin-31, cki-1, yap-1.

| Gene | GOA rows | NEW rows | WormBase text | UniProt text | Text defects (WormBase + UniProt) |
|---|---|---|---|---|---|
| egl-44 | 30 | 0 | UNVERIFIED | UNVERIFIED | 3 (2 + 1) |
| egl-46 | 33 | 0 | DISPUTED | VERIFIED | 4 (3 + 1) |
| mec-3 | 31 | 0 | VERIFIED | VERIFIED | 2 (1 + 1) |
| pie-1 | 36 | 2 | VERIFIED | DISPUTED | 3 (1 + 2) |
| pos-1 | 24 | 2 | DISPUTED | DISPUTED | 4 (2 + 2) |
| mes-1 | 17 | 0 | VERIFIED | DISPUTED | 2 (1 + 1) |
| lin-31 | 14 | 0 | DISPUTED | VERIFIED | 3 (2 + 1) |
| cki-1 | 21 | 0 | VERIFIED | VERIFIED | 2 (1 + 1) |
| yap-1 | 20 | 1 | UNVERIFIED | DISPUTED | 3 (1 + 2) |

The verdict columns are the `reference_review.correctness` of each cited file, under the
convention above. The 26 description-text defects are 17 omissions, 6 wrong statements
and 3 outdated statements; 17 are `CONFIRMED`, 8 `PROBABLE` and 1 `SUSPECTED`.

| Source (9 new genes) | Correctness | Utility | Compactness | Completeness | Specificity |
|---|---|---|---|---|---|
| UniProt FUNCTION (9) | 4.6 | 3.9 | 3.6 | 3.3 | 4.0 |
| WormBase curated (9) | 4.3 | 3.6 | 3.7 | 2.6 | 3.7 |
| Alliance automated (9) | 3.7 | 2.2 | 4.0 | 2.1 | 2.2 |

Concordance across sources averages 3.6 (five genes score 4 and four score 3), against
4.24 for all 452 worm genes. These are well-studied genes, so the sources have more to
disagree about. The 41 findings (17 gaps, 15 discrepancies, 9 insights) are in
[worm-findings.yaml](MOD_DESCRIPTIONS/worm-findings.yaml) with the rest.

- **WormBase text: mostly omissions, a few errors.** 10 of the 14 WormBase defects are
  omissions of later work. Examples:
  - the YAP-1/WTS-1 Hippo roles of egl-44;
  - the PVD role of mec-3;
  - the cytoplasmic second function of PIE-1, which promotes mom-2 and nos-2 expression.

  The wrong or outdated statements are:
  - egl-46 "required for ... terminal divisions of the Q neuroblasts": mutants make an extra
    division.
  - egl-46 "TFIIA-like zinc-finger protein family": EGL-46 is an INSM-family protein, and
    TFIIA has no zinc fingers.
  - lin-31: the 1998 phosphorylation model is stated as fact. Endogenous alleles lacking all
    four MAPK sites give only vulval morphology defects (PMID:23995389).
  - pos-1: mex-6 3' UTR binding called "in vitro", when it came from a yeast three-hybrid
    assay.
- **UniProt text: fewer omissions, harder errors.** Two FUNCTION sentences contradict the
  paper they cite:
  - pie-1 "Inhibits the histone deacetylase activity of hda-1 (PubMed:34003111)": that paper
    shows PIE-1 promoting HDA-1 SUMOylation and germline hypoacetylation.
  - pos-1 promotes endo-mesoderm "in anterior blastomeres": POS-1 acts posteriorly and
    restricts NEG-1 to the anterior (PMID:26096734).

  Also: mes-1's GPR-1/2 enrichment mechanism has since been revised, and yap-1's S104A
  mutagenesis note contradicts itself.
- **Automated text** leads with removed terms here too: kinase activities for the MES-1
  pseudokinase, a pseudokinase confirmed by a residue analysis in
  `genes/worm/mes-1/mes-1-bioinformatics/`. The egl-44 and egl-46 texts give exit from
  mitosis for a defect in which a cell divides once too often.
- **NEW rows.** There are five, all from the literature rather than from a gap finding:
  - positive regulation of translation for pie-1 (PMID:24131629) and pos-1 (PMID:16499902);
  - defense response to Gram-negative bacterium for yap-1 (PMID:32857822). A comparator check
    showed that the worm transcription factors with that role carry the term.
  - nucleolus for pie-1 and P-body for pos-1, both by IDA.

  One proposed NEW row was withdrawn in the coordinator's check. mec-3 mechanoreceptor
  differentiation (GO:0042490) is a direct child of neuron differentiation, which the gene
  already carries. It became a MODIFY of the two IMP rows whose papers are about touch
  receptors, and the family-level IBA and IEA rows stay `ACCEPT`.
- **Lexical overlap.** The new descriptions recover a median 0.46 of their WormBase
  content words, against 0.37 for the worm corpus. That is expected when the text is an
  input. The corpus median is unchanged at 0.37 (452 genes; see
  [worm-comparison.yaml](MOD_DESCRIPTIONS/worm-comparison.yaml)).
- **How the reviews were run.**
  - No deep-research provider was configured, so each notes file records the literature
    searches that were done by hand.
  - UniProt's gene-symbol search returned HTTP 429, so `just fetch-gene` was given
    `--uniprot-id`.
  - The reviews were written in parallel, in sparse registered worktrees that shared the
    main runtime. The project's PostToolUse validation hook runs `uv run` in the edited
    file's checkout without the `UV_PROJECT_ENVIRONMENT` setting. In two worktrees, one
    review edit each built a 1.4 GB `.venv` and rewrote `uv.lock`. Both were reverted, and
    the remaining edits were made without the editor tools.

## Yeast (SGD)

- `fetch-descriptions-bulk yeast` refreshed all 890 sidecars, and
  `mod-description-deep-research yeast` wrote 890 `-deep-research-sgd.md`
  files. Every yeast gene has an SGD-written description.
- Re-fetching kept the 2026-03 pilot scores wherever a source text was
  unchanged. Where SGD or the Alliance had changed a text since then, that
  source's score and the cross-source review were dropped as stale: 17 files
  stay `COMPLETE`, 101 are `IN_PROGRESS` and 772 are new (`STUB`).
- SGD texts are much shorter than WormBase's (median 33 words, against 75 for
  WormBase and 111 for our yeast reviews). On lexical overlap they are closer to
  ours: a median 0.42 of SGD content words appeared in our descriptions (0.44 after
  the follow-up below), against
  0.37 for worm (0.35 before the worm follow-up). See
  [yeast-comparison.yaml](MOD_DESCRIPTIONS/yeast-comparison.yaml).
- Guard against automated text filed as curated (`looks_automated`): it
  rejects all 12 RGD notes sampled, and flags none of the 902 WormBase and SGD
  curated texts on disk. A first version that matched on the opening alone
  wrongly rejected SGD's CAF120 ("Part of the CCR4-NOT ... complex; involved
  in ..."), and was fixed before any file used it.
- All 890 yeast files are now `COMPLETE`. The 873 incomplete files were scored by
  16 parallel agents, calibrated on the worm examples and on the yeast pilot. Sources
  that kept a pilot review were not rescored, and each batch was schema-checked.
  Spot-checked findings (GTT2, IRC24, RIB7) hold against the source texts.

| Source (yeast genes) | Correctness | Utility | Compactness | Completeness | Specificity |
|---|---|---|---|---|---|
| SGD curated (890) | **4.8** | 4.1 | 4.3 | 4.0 | 4.0 |
| UniProt FUNCTION (798) | 4.6 | 3.7 | 4.0 | 3.5 | 3.8 |
| Alliance automated (890) | 4.4 | 2.9 | 3.8 | 3.1 | 2.9 |

The counts include one protein twice: `genes/yeast/ERG19` and `genes/yeast/MVD1`
are the same entry (P32377; MVD1 is the SGD standard name and ERG19 a synonym). Merging them is
[issue 5837](https://github.com/ai4curation/ai-gene-review/issues/5837). Two genes, HKR1 and
MSB2, have no gene review, so their concordance scores compare the sources with
each other only.

  The test the worm run could not make: **SGD's maintained text is the best source**.
  It scores above UniProt on every rubric, whereas WormBase scored below it (4.2
  against 4.5). Only two SGD texts score 2 or less on correctness:
  - ALG11: Man5 rather than Man3-to-Man5.
  - RIB7: called a deaminase; it is the reductase.

  Twelve WormBase texts did. Concordance is a mean 4.48 (worm 4.25). The 354
  findings (182 gaps, 163 discrepancies, 9 insights) are in
  [yeast-findings.yaml](MOD_DESCRIPTIONS/yeast-findings.yaml). Most discrepancies
  involve the **automated** text (108 of 163), which picks GO terms the reviews
  reject. Examples:
  - kinase activity for the pseudo- or non-kinases KDX1 and CAF120;
  - THI3 decarboxylase activity.

  SGD text is involved in 61 discrepancies and UniProt in 51 (one discrepancy can
  involve several sources). The UniProt cases are often dated or transferred text,
  for example:
  - ACP1: a Complex I subunit, in a species that has no Complex I.
  - ACH1 and VIP1: claims transferred from mammalian or S. pombe homologues.
  - ERG12, ERG19 (also filed as MVD1) and ERG20: mevalonate pathway steps placed
    in the vacuole; the reviews have these enzymes in the cytosol.

  Yeast has only 9 insight findings against 66 for worm, while gaps and
  discrepancies rose. That may be because SGD's shorter text yields fewer side
  observations, or because the yeast agents used the category more narrowly; the
  data cannot tell the two apart.
  SGD has two self-referencing copy errors: GTT2 "overlaps with Gtt2p", and IRC24
  is "a putative paralog of IRC24".
- **Follow-up on the yeast findings.** Eight parallel agents worked through the 345 gap
  and discrepancy findings (316 genes) under the same rules as for worm. Each edited
  gene was validated and given a history record.
  - 89 description-text `source_defects` across 81 genes: 44 SGD and 45 UniProt (one in a UniProt SUBUNIT comment);
    49 `WRONG_STATEMENT`, 25 `OUTDATED_STATEMENT`, 15 `MISSING_STATEMENT`; 38 of them
    recorded as CONFIRMED. These counts are from the follow-up run (2026-11-01); the table
    above has the current totals.
  - 249 reviews edited, mostly with a description sentence for a verified gap.
  - Two `NEW` rows, both checked against the NEW bar:
    - MIH1 GO:1905279 regulation of retrograde transport, endosome to Golgi:
      purified Mih1 dephosphorylates Vps26.
    - HOG1 GO:0071243 cellular response to arsenic-containing substance: Hog1
      senses arsenic through conserved cysteines.
  - Three action changes. RAS2's duplicate IEA bud-neck row is now ACCEPT, matching
    the accepted IGI row. DCI1's two dienoyl-CoA isomerase rows are now UNDECIDED,
    because purified Dci1 shows no activity (PMID:19830908), against an earlier
    crude-extract result.
  - As for worm, lexical overlap rose (recall 0.42 to 0.44, median 111 to 115 words).
  - Examples of SGD defects:
    - RIB7 called a deaminase;
    - ALG11's Man5 substrate;
    - PFK1 ribosome association, which belongs to Pfk2;
    - KDX1 called a kinase;
    - GUT1 regulators swapped.
  - Examples of UniProt defects:
    - THI3 decarboxylase activity that direct assays do not find;
    - BTS1 contradicted by its own kinetic data;
    - CPT1 given Ept1's substrate;
    - the vacuolar mevalonate module.
- **`correctness` convention**, now in the review skill: `DISPUTED` if any claim is
  wrong, otherwise `UNVERIFIED` if any claim could not be traced, otherwise `VERIFIED`.
  53 earlier worm and yeast MOD and UniProt references were brought into line with it.

## Fly (FlyBase)

- `mod-description-deep-research DROME` wrote 345 `-deep-research-flybase.md` files
  for the 539 fly reviews; 189 genes have no FlyBase-written description. Every gene
  has a descriptions sidecar.
- Two fetcher fixes came out of the run:
  - Unreviewed UniProt entries often lack the `DR   FlyBase` line and carry only
    `DR   AGR; FB:FBgn...`. Both fetchers now fall back to the AGR line for any MOD,
    which recovered 8 genes.
  - FlyBase writes Greek letters as characters ("α-Man-Ia"), so the identity check
    now spells them out and ignores case.

  Two genes are still not fetched. CG4592's UniProt entry gives only a VectorBase id,
  and the Alliance API rejects GatB's `FBgn0039153` with HTTP 400.
- FlyBase texts are a median 37 words (SGD 33, WormBase 75), and a median 0.50 of their
  content words appear in our descriptions, the highest of the three MODs. See
  [fly-comparison.yaml](MOD_DESCRIPTIONS/fly-comparison.yaml).
- 531 files are `COMPLETE`, scored by 8 parallel agents with the yeast brief adapted for
  fly. Eight genes have no description from any source and were left unscored.

| Source (fly genes) | Correctness | Utility | Compactness | Completeness | Specificity |
|---|---|---|---|---|---|
| FlyBase curated (345) | **4.7** | 3.7 | 4.8 | 3.4 | 3.5 |
| UniProt FUNCTION (319) | 4.6 | 3.8 | 3.9 | 3.6 | 3.8 |
| Alliance automated (529) | 4.3 | 2.9 | 3.7 | 3.0 | 2.8 |

  As with SGD, the curated MOD text is the most accurate source. Unlike SGD, it is not
  the most informative: UniProt scores higher on utility, completeness and specificity,
  and FlyBase's lead is in compactness. Concordance is a mean 4.34. The 211 findings
  (116 discrepancies, 89 gaps, 5 insights, 1 consensus) are in
  [fly-findings.yaml](MOD_DESCRIPTIONS/fly-findings.yaml). The automated text is
  involved in 74 of the 116 discrepancies, UniProt in 38 and FlyBase in 37.
- **Follow-up on the fly findings.** Eight agents worked through the 205 gap and
  discrepancy findings (187 genes) under the yeast rules.
  - 73 description-text `source_defects` across 64 genes: 39 FlyBase and 34 UniProt;
    34 `WRONG_STATEMENT`, 13 `OUTDATED_STATEMENT`, 26 `MISSING_STATEMENT`; 25 of them
    recorded as CONFIRMED. These counts are from the follow-up run (2026-11-01); the table
    above has the current totals.
  - 124 reviews edited, mostly with a description sentence or a `reference_review`.
  - One `NEW` row: Tango5 GO:0000045 autophagosome assembly (IMP, PMID:34019822).
    Tango5 is the fly VMP1, the ER scramblase that does part of the work, and human
    VMP1 carries the term.
  - Lexical overlap did not move (median recall 0.50; review median 125 to 128 words).
  - Examples of FlyBase defects:
    - Pxd called a catalase-like, glutathione-oxidising enzyme; it is the chorion
      peroxidase that makes di-tyrosine cross-links.
    - Br140 and Ing5 called histone acetyltransferases; Enok is the enzyme.
    - Lis-1 called a PAF-AH subunit; fly Lis-1 does not bind the fly alpha homolog.
    - amon said to cleave Slit; Tolkin is the Slit protease.
    - SREBP said to respond to cholesterol; fly SREBP responds to phosphatidylethanolamine.
  - UniProt defects are mostly mammalian text carried over to the fly entry:
    - smo and SCAP: cilium and sterol mechanisms.
    - cact and IKKbeta: IKK as the Cactus kinase; Pelle phosphorylates Cactus.
    - spi: Gurken named as the EGF receptor.
    - Ccs: described as a dismutase; it is the copper chaperone for Sod1.
    - borr: copied from the Australin paper and contradicted by the borr paper it cites.
  - Alliance automated text: two losses (Mtpalpha, IKKepsilon) and two doubtful human
    orthologs (ey given PAX4, tin given NKX2-2), in
    [alliance-automated-regressions](MOD_DESCRIPTIONS/alliance-automated-regressions.md).

## Fly: new reviews of genes with non-duplicative IBA rows

The earlier runs scored MOD text against reviews that already existed. This batch
(2026-11-16) used the FlyBase description as the deep-research source for eight **new**
reviews. No Falcon or Perplexity report was run; the reviewers' own literature reading
filled the gaps. The batch tests two things at once: the FlyBase text, and the IBA
(PAINT) rows that nothing else on the gene already asserts.

- **Selection.** [iba_novel_candidates.py](MOD_DESCRIPTIONS/iba_novel_candidates.py)
  reads the FlyBase GAF from the GO Consortium and `go-basic.obo`. It lists unreviewed
  genes with an IBA row that no other annotation covers, either by the same term or a
  more specific one, of any evidence code. There are 5,755 such genes. With at least two
  such rows and ten experimental PMIDs, 185 remain. Eight of these, all with a FlyBase
  description, were chosen for a substantive IBA molecular-function call. The other 177
  are the worklist for later batches, in
  [fly-iba-novel-candidates.yaml](MOD_DESCRIPTIONS/fly-iba-novel-candidates.yaml). That
  list does not check whether FlyBase text exists.
- **Method.** Reviews followed the standard workflow: `just mod-description-deep-research`,
  a `reference_review` and any `source_defects` on the FlyBase file, a scored
  descriptions sidecar, and a history record. Four parallel agents reviewed two genes
  each, and all eight reviews pass `just validate` in the merged branch.

| Gene | Non-duplicative IBA rows: verdict | FlyBase text | Description defects |
|---|---|---|---|
| puc | 5: 4 ACCEPT, 1 non-core (MAPK Tyr phosphatase names half the reaction) | DISPUTED | FlyBase: "serine/threonine" phosphatase; Puc is a dual-specificity MKP (CONFIRMED) |
| Pka-R1 | 5: all ACCEPT (cAMP binding, PKA inhibitor, C-subunit binding) | DISPUTED | FlyBase: actin/microtubule and NMJ/molting/ethanol sentences (2, PROBABLE); UniProt: no FUNCTION text (MISSING) |
| Atg18a | 7: 3 ACCEPT, 2 non-core, 1 MODIFY (term now obsolete), 1 over-annotated (nucleophagy, yeast-only) | UNVERIFIED | none |
| Syt1 | 6: 4 ACCEPT, plasma membrane over-annotated (seeded by Syt4/Syt7/Syt-alpha), dense core granule UNDECIDED | VERIFIED | UniProt: "may have a regulatory role" (OUTDATED, CONFIRMED) |
| tim | 5: 4 REMOVE, DNA binding over-annotated | DISPUTED | FlyBase: "DNA replication" (PROBABLE) |
| Sirt1 | 9: 5 ACCEPT (H3K9/H3K14/H4K16 deacetylase, corepressor), 1 non-core, 2 over-annotated, 1 REMOVE (subtelomeric heterochromatin) | VERIFIED | UniProt: PEV direction inverted, Polycomb sentence inverted (CONFIRMED); ex10-allele phenotypes (OUTDATED) |
| mei-9 | 6: 3 ACCEPT (NEF1 complex, ICL repair, 3'-flap endonuclease), 1 non-core, 2 over-annotated | VERIFIED | UniProt: meiotic mismatch repair (OUTDATED) |
| Fadd | 4: caspase binding ACCEPT; death receptor binding and CD95 DISC REMOVE; extrinsic apoptosis over-annotated | VERIFIED | none |

What the batch showed:

- **About two-thirds of non-duplicative IBA rows hold.** Of 47 rows, 31 are kept: 25
  ACCEPT, 5 KEEP_AS_NON_CORE, and 1 MODIFY to the replacement of an obsoleted term.
  The other 16 are not: 8 MARK_AS_OVER_ANNOTATED, 7 REMOVE, 1 UNDECIDED. The failures
  cluster where the PAINT node sits above a lineage-specific function:
  - **tim:** all five replication-fork IBDs sit at the eukaryote root of PTHR22940
    (PTN000533813), above the metazoan tim/timeout duplication (PTN008585095). PAINT
    records no loss on the insect TIM clade, but timeout is the paralog needed for
    chromosome integrity (PMID:20153199), and mammals have lost the tim1-type gene
    (PMID:17065608).
  - **Fadd:** vertebrate death-receptor biology. Flies have no CD95, and the fly TNF
    receptors lack a death domain.
  - **Sirt1:** yeast Sir2 heterochromatin terms.
  - **Atg18a:** the yeast-only nucleophagy term.
  - **Syt1:** a family-level plasma membrane node seeded by other synaptotagmins.

  Each failed row suggests a PAINT change, a loss or a node move, that is worth raising
  upstream.
- **FlyBase text was right in 4 of 8 cases and compact in all**: correctness 4.0, utility
  3.2, compactness 5.0, completeness 2.5, specificity 3.1, for 18–34 words. These are
  lower than the 4.7 correctness of the earlier fly run, which scored mostly
  well-reviewed genes. The tim case points to a new failure mode: FlyBase's "DNA
  replication" claim traces to no paper and seems to restate the IBA rows that the
  review rejects. Hand-written MOD text can therefore echo the computational
  annotations under test, so it is no independent check on them.
- **The automated text is weaker on these genes** (correctness 3.2, against 4.3 for the
  earlier run). It leads with IBA terms; for example, "Predicted to enable DNA binding
  activity" opens the tim text. Concordance across sources is 3.6, against 4.34. The
  sidecars hold 31 findings: 14 discrepancies, 13 gaps and 4 insights.
- **NEW rows remain rare.** There are 2 in eight reviews, both direct assays: Atg18a at
  the phagophore assembly site (IDA, PMID:24374083), and Fadd protein-macromolecule
  adaptor activity, bridging dSTING to Dredd (IDA, PMID:41904322).
- **Tooling problems seen in this run.**
  - On 2026-11-16, QuickGO returned HTTP 500 for every request that included
    `includeFields=taxonName`. `fetch_goa_data` (`src/ai_gene_review/etl/gene.py`)
    treats a first-page error as "no annotations", so `just fetch-gene` wrote header-only
    GOA files without failing. Its docstring says it raises `ValueError`. The reviewers
    re-fetched with that one field dropped and the taxon name filled from taxon 7227.
    `fetch-gene` should fail loudly, or retry without the field.
  - For puc, the default accession choice picked A0A0B4LHX7, the first UniProt search
    hit, which has no GOA rows; Q9VHV8 carries the annotations. For genes with only
    unreviewed entries, check that the fetched accession is the one with the GOA rows.
    Atg18a resolved correctly to M9PER1, which carries all 31 rows; Q9VSF0 has 13.
  - QuickGO already serves GO:0034045 as obsolete with replacement GO:7770114
    phagophore membrane, which the `go-basic.obo` release does not yet have.

## Mouse (MGI): not used

MGI's `MOD_provided_gene_description` is a summary of mutant phenotypes, not a
description of what the gene does. In a random sample of 25 of the 221 mouse
genes, 22 have text and all 22 describe allele phenotypes:

- mouse/Src: "Homozygotes for a targeted null mutation exhibit growth retardation, failure of
  tooth eruption, osteopetrosis ...".
- Ccne1: "Mice homozygous for disruptions in this gene display no abnormal phenotype."

Cd79a and Cd79b, outside the sample, share the same sentence word for word. The sample
and these two notes are in [mouse-mgi-sample.yaml](MOD_DESCRIPTIONS/mouse-mgi-sample.yaml),
written by [mgi_sample.py](MOD_DESCRIPTIONS/mgi_sample.py). Mutant phenotypes establish
necessity, not participation, so under the NEW bar they almost never support an
annotation, and a worm- or fly-style review would mostly list phenotypes that are
correctly left out. The mouse run was therefore stopped after the sample (2026-11-02),
and `mod-description-deep-research` now skips MGI, so no `-deep-research-mgi.md` files
are written. The sample also exposed a latent bug,
now fixed: MGI's own UniProt line carries the prefix (`DR   MGI; MGI:106913;`), so the
descriptions fetcher would have asked the Alliance API for `MGI:MGI:106913`.

## Recommendations

1. **Use the curated MOD description as an input, not as an authority.** This
   is done through the deep-research file above. Each claim in the curated text
   should be either covered by the review or set aside in `reference_review`
   (for example, "stale: CED-4 is the Apaf-1-like apoptosome adaptor").
2. **Treat a claim that appears only in the MOD text as a literature lead.**
   fshr-1 is the model case: the gap is a missed role, not wording.
3. **Re-audit existing reviews** with the comparison script, starting with the
   lowest-overlap genes. The remaining Alliance MODs add nothing here: MGI's note is a
   phenotype summary, RGD's is automated text, and ZFIN and Xenbase have none.
4. The NCBI step hits rate limits (HTTP 429) on bulk runs. It should honour an
   `NCBI_API_KEY`, or back off and retry.
5. The review-validation hook should honour `UV_PROJECT_ENVIRONMENT` (or call the
   shared interpreter directly). Otherwise every edit in a separate worktree builds a
   new environment there
   ([issue 6457](https://github.com/ai4curation/ai-gene-review/issues/6457)).

## Status and next steps

- [x] Fix the Alliance parser and the WormBase gene-id extraction
- [x] Fetch worm descriptions (432 genes) and write the comparison table
- [x] Hand-compare 16 genes
- [x] Decide how to feed the text to reviews: as a deep-research file (2026-10-30)
- [x] Emitter, tests, `just` recipe and skill guidance
- [x] Write `-deep-research-wormbase.md` for the worm genes
- [x] Follow up the fshr-1 synaptic role (PMID:39561202) in its review
- [x] Rubric reviews of all description sources for all 432 worm genes, with a findings worklist
- [x] Work through the gap and discrepancy findings in `worm-findings.yaml`
- [x] Record the contradicted MOD and UniProt statements as `source_defects`
- [x] Worm: score the 11 reviews added after the run (all 452 worm sidecars `COMPLETE`)
- [x] Worm: nine new reviews written with the WormBase text as input (26 text defects, 5 NEW rows)
- [ ] Worm: more new reviews from the same ranking, only for genes with a WormBase text
  (next candidates: gex-3, ced-10, goa-1, lin-5, npr-1, daf-1, cav-1, oma-1)
- [ ] File the WormBase, UniProt and Alliance reports (manual step) and set `report_status`
- [x] Yeast: fetch descriptions and write SGD deep-research files (890 genes)
- [x] Yeast: score descriptions (890 COMPLETE)
- [x] Yeast: act on gap and discrepancy findings (89 source defects, 249 reviews edited)
- [x] Fly: fetch, score and act on findings (345 FlyBase files, 73 source defects, 124 reviews edited)
- [x] Fly: 8 new reviews of genes with non-duplicative IBA rows, using FlyBase text as the deep-research source (47 IBA rows judged, 10 source defects)
- [ ] Fly: continue with [fly-iba-novel-candidates.yaml](MOD_DESCRIPTIONS/fly-iba-novel-candidates.yaml) (177 genes)
- [ ] Raise the tim, Fadd and Sirt1 PAINT over-propagations with PANTHER/PAINT curators
- [ ] Make `fetch-gene` fail (or retry) when QuickGO errors, instead of writing an empty GOA file
- [x] Mouse (MGI): sampled and not used, because the note is a phenotype summary; rat (RGD) has only automated text; zebrafish and frog have none
