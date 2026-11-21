# ENDOG notes

## 2026-09-30

ENDOG is a nuclear-encoded, mitochondrial DNA/RNA endonuclease with a mitochondrial
transit peptide and catalytic Mg-dependent nuclease fold. The human protein is in the
same PANTHER `PTHR13966:SF5` subfamily as mouse Endog, yeast NUC1, and worm cps-6,
which supports the broad DNA/RNA nonspecific endonuclease PAINT transfers.

The best direct human and mammalian process evidence splits into three branches:

- **Modified nuclear DNA cleavage and recombination.** Robertson et al. purified EndoG
  as the activity in mouse liver extracts that preferentially cleaves
  5-hydroxymethylcytosine-modified DNA, showed recombinant EndoG cleavage, and showed
  that 5hmC stimulates conservative recombination in an EndoG-dependent manner
  [PMID:25355512 Endonuclease G preferentially cleaves 5-hydroxymethylcytosine-modified
  DNA creating a substrate for recombination., "recombinant EndoG preferentially
  recognizes and cleaves a core sequence"; "promote conservative recombination in an
  EndoG-dependent manner"].
- **Mitochondrial DNA turnover.** Wiehe et al. used human-cell knockdown, knockout,
  re-expression, and nuclease-mutant assays to show that ENDOG stimulates mitochondrial
  DNA depletion and compensatory mitochondrial DNA replication in a nuclease-dependent
  manner, especially under oxidative stress [PMID:29719607 Endonuclease G promotes
  mitochondrial genome cleavage and replication., "EndoG stimulates both mtDNA
  replication"].
- **Starvation autophagy.** Wang et al. showed that starvation-released, GSK3beta-
  phosphorylated ENDOG binds YWHAG/14-3-3gamma, freeing TSC2 and VPS34 from YWHAG to
  suppress mTORC1 and initiate autophagy; they also support an endonuclease-dependent
  DNA damage-response branch of the same autophagy phenotype [PMID:33473107
  Endonuclease G promotes autophagy by suppressing mTOR signaling and activating the DNA
  damage response., "mTOR pathway suppression and autophagy initiation"; "enhances its
  interaction with 14-3-3"].

The inherited apoptotic DNA-fragmentation row is plausible and should stay specific:
ENDOG can itself cleave DNA after mitochondrial release, so `GO:0006309 apoptotic DNA
fragmentation` is preferable to any broad `GO:0006915 apoptotic process` row. It is not
the central CAD/DFF40 nuclease, though, and the more recent human papers point toward
mtDNA maintenance, 5hmC-biased cleavage/recombination, and starvation autophagy as the
core ENDOG axes.

The rat-derived stimulus rows for mechanical stimulus, calcium, glucose, hypoxia,
estradiol, oxidative stress, and hydrogen-peroxide cell death look over-propagated into
human. They describe conditions or cell-death outcomes in which rat Endog was mobilized
rather than a molecular step performed by human ENDOG. The DNAJA4 and ITLN2 protein
binding rows from high-throughput interactome/chaperone studies were removed as generic
edges with no ENDOG-specific functional interpretation.

## 2026-10-26 — family, orthologs, human disease, and the dataset landscape

### Family and evolution

ENDOG sits in PANTHER PTHR13966 subfamily SF5 with worm CPS-6, yeast NUC1, fission
yeast pnu1 and the secreted bacterial nucleases NucA (*Serratia*, *Nostoc*). Two
sibling subfamilies matter for interpretation. SF19 is EXOG, a metazoan paralog
produced by duplication of an ancestral mitochondrial endo/exonuclease
[PMID:18187503 "during metazoan evolution duplication of an ancestral nuclease gene
obviously generated the paralogous EndoG- and EXOG-protein subfamilies in higher
eukaryotes"]; a Wing domain converts it into a 5' exonuclease for mtDNA base-excision
repair [PMID:28466855 "A Wing domain, absent in other ββα-Me members, suppresses
endonuclease activity"]. SF17 is secreted insect salivary DNases, one of which
destroys neutrophil extracellular traps to help *Leishmania* survive
[PMID:24516388 "Lundep hydrolyzes both ss- and dsDNA with little sequence
specificity"]. So the same His-Me finger fold is used for mtDNA housekeeping, for
mtDNA repair, and — on a secreted branch — for host-DNA destruction.

Regulation by a dedicated inhibitor is conserved in outline. Flies have EndoGI
[PMID:19129189 "We propose that EndoGI protects the cell against low levels of EndoG
outside mitochondria"], and two 2026 papers independently identify KU80 as the
mammalian equivalent [PMID:41837724 "The KU80 C-terminal domain (CTD) shares
structural homology with Drosophila EndoG inhibitor (EGI), directly binds ENDOG and
inhibits its nuclease activity in vitro"].

Ortholog phenotypes do not transfer cleanly. Worm CPS-6 and fly EndoG degrade
paternal mtDNA [PMID:27338704, PMID:22421049], but mouse Endog knockouts have normal
spermatogenesis and sperm mtDNA [PMID:39373150 "our results indicate that ENDOG is
not essential for spermatogenesis or the elimination of sperm mtDNA in mice"].

### Human disease: mitochondrial, not immune

One genetically defined patient is reported: biallelic ENDOG variants with absent
protein, progressive external ophthalmoplegia, mitochondrial myopathy and multiple
mtDNA deletions in muscle [PMID:35326425 "we report biallelic ENDOG variants
identified by NGS in a patient with progressive external ophthalmoplegia,
mitochondrial myopathy and multiple mtDNA deletions in muscle"], plus low-level
heteroplasmic point mutations in fibroblasts [PMID:35326425 "we detected an
accumulation of low-level heteroplasmy mtDNA point mutations compared with
age-matched controls"]. dismech's Gene Table of Neuromuscular Disorders transcription
classifies ENDOG under `mitochondrial_myopathies`. MONDO has no ENDOG-specific term;
such a disease would sit under MONDO:0000090 progressive external ophthalmoplegia
with mitochondrial DNA deletions.

The other established mammalian phenotype is cardiac. Rat systems genetics mapped a
blood-pressure-independent left-ventricular-mass locus to Endog [PMID:21979051 "we
found a loss-of-function mutation in Endog that is associated with increased LVM and
impaired cardiac function"], with depleted mitochondria and elevated ROS in the
knockout heart [PMID:21979051 "the Endog-deleted mouse heart had depleted
mitochondria, mitochondrial dysfunction and elevated levels of reactive oxygen
species"]; the hypertrophy is ROS-dependent [PMID:29502044 "Cardiomyocyte hypertrophy
induced by Endonuclease G deficiency requires reactive oxygen radicals
accumulation"].

**No immune phenotype is reported for ENDOG loss in any organism.** Human LoF is
entirely unconstrained in gnomAD v4 (pLI 4.5e-08; o/e LoF 0.97, 22 observed vs 22.6
expected; LOEUF 1.39), so heterozygous LoF is not selected against and no
dominant immune phenotype is plausible. This is the opposite of DNASE1L3, whose loss
causes monogenic SLE.

### The immune-adjacent mechanism that *is* supported — in yeast

Two recent yeast papers put the EndoG family on the mtDNA-escape route that feeds
cytosolic DNA sensing. Nuc1 degrades mtDNA destined to leave the organelle
[PMID:41638207 "We identify the mechanism by which an intermembrane space nuclease,
endonuclease G (human ENDOG; yeast Nuc1), prevents mtDNA escape to the cytosol in
yeast"], and both its catalytic activity and its mitochondrial localization are
required [PMID:41638207 "Nuc1 nuclease activity and mitochondrial localization are
essential for preventing mtDNA escape"]; escape runs through mitophagy and the
vacuole. Separately, Nuc1 limits transfer of long mtDNA to the nucleus
[PMID:39227600 "nuclease limits insertion of cDNA and transfer of very long mtDNA"],
in a paper that frames the metazoan question explicitly [PMID:39227600
"mitochondrial DNA (mtDNA) or retrotransposon cDNA released to cytoplasm are degraded
by nucleases to prevent sterile inflammation"].

Whether human ENDOG does either job is untested. That is the gap worth an
OpenScientist run, and it is a mechanistic question rather than a disease-gene one.

### Dataset landscape (checked, not assumed)

- **No public ENDOG perturbation expression data.** A GEO query for ENDOG knockout
  or knockdown returns two datasets, both incidental text matches, and none of the
  mechanistic papers (PMID:29719607, PMID:33473107, PMID:37794041, PMID:39752519)
  has a GEO series indexed by PMID. So an "ENDOG-null interferon signature" cannot be
  read off public transcriptomes today.
- **NUMT catalog.** 1,637 NUMTs with mtDNA coordinates across 66,083 genomes
  [PMID:36198798 "More than 99% of individuals had at least one of 1,637 different
  NUMTs"], including the observation that [PMID:36198798 "NUMTs preferentially
  involved non-coding mitochondrial DNA, linking transcription and replication to
  their origin"]. The per-individual genotypes are UK Biobank and restricted, but the
  NUMT breakpoint coordinates are published, so breakpoint-versus-motif analysis is
  open.
- **mtDNA population variation.** gnomAD v3.1 mtDNA [PMID:35074858 "Our gnomAD v3.1
  release contains population frequencies for 10,850 unique mtDNA variants"] is open
  and queryable; it reports heteroplasmy at >=10% only, and explicitly treats NUMT
  misalignment as a false-positive source.
- **Sub-mitochondrial reference proteomes.** MitoCarta3.0 (PMID:33174596) carries
  sub-mitochondrial localization assignments, and APEX2 proximity-labeling proteomes
  exist for matrix and IMS; these are the resources that could settle the
  intermembrane-space-versus-matrix conflict without new wet-lab work.
- **MITOMAP** deletion tables returned HTTP 403 to automated access; a deletion
  breakpoint catalog would need another route.

## 2026-10-26 — OpenScientist H1: mtDNA breakpoints vs ENDOG motifs (negative)

Ran the breakpoint-versus-motif test as a hypothesis job
(`ENDOG-hypotheses/mtdna-breakpoint-motif-enrichment/`). It computed rather than
summarised: it fetched the rCRS, the MitoBreak deletion table, the PMID:36198798
supplementary NUMT tables and the UCSC NumtS track, and ran a GC-decile-matched
permutation test.

Result, in two parts:

- **mtDNA deletions.** Breakpoints are enriched at G-quadruplex and C-rich motifs over
  GC-matched controls (fold 1.17, z +13). But stratifying by junction repeats puts the
  whole signal in deletions flanked by a direct repeat of >=5 bp (fold 1.24) and none in
  repeat-free deletions (fold 0.97, p 0.91). mtDNA direct repeats are themselves G/C-rich,
  so the motif enrichment is collinear with the classical mechanism
  [file:human/ENDOG/ENDOG-hypotheses/mtdna-breakpoint-motif-enrichment/openscientist.md
  "a mechanism that does not require ENDOG and fully accounts for the observed G/C-rich
  localization"].
- **NUMTs.** No enrichment in the 66,083-genome catalogue (germline p 0.39, somatic p 0.10)
  or the independent UCSC set (p 0.59). That arm of the hypothesis is refuted.

What I verified independently, rather than taking on trust: the rCRS base composition the
report quotes is right (C 31.3%, G 13.1%, 16,569 bp), and the 9-bp deletion hotspot it
leans on really is a C-rich direct repeat, `ACCCCCTCTAC` at 8271-8281 — which is the
report's own central point, that at the hotspot the "motif" and the repeat are the same
sequence.

What cannot be checked: only an HTML and a PDF report were saved, with no code or
intermediate tables, so the test statistics are not replayable. Treat the numbers as
indicative.

Consequences for the review. No action changed and no annotation added. The core-function
sentence claiming G-quadruplex cleavage "may generate the common 9-bp mtDNA deletion" is
now qualified, because the population data do not separate ENDOG from slipped replication.
The eLife direct assay (PMID:36394256) is untouched — it shows ENDOG binds and cuts there;
what is unsupported is the inference from that to ENDOG shaping the breakpoint landscape.
The report's own GO suggestions were not adopted: `GO:0051880 G-quadruplex DNA binding` may
well be right, but it should come from the primary assay, not from a coordinate analysis.

The decisive experiment is now a suggested experiment on the review: breakpoint mapping in
ENDOG-null versus wild-type cells, analysing repeat-free deletions separately, plus an
in-vitro cleavage map on damaged templates. A static reference scan cannot see
lesion-driven site selection, which PMID:41854021 says is ENDOG's actual preference — so
this negative result does not exclude ENDOG involvement, it only removes the sequence-motif
argument for it.

## 2026-10-27 — OpenScientist H2: intermembrane space vs matrix (narrowed, not settled)

Ran the sub-compartment question as a hypothesis job
(`ENDOG-hypotheses/submitochondrial-localization-ims-vs-matrix/`). This run saved its
executed code as provenance, which fetches the reference sequences from UniProt, so the
analysis is inspectable in a way H1's was not.

It computed sequence features for ENDOG against eight matrix and seven intermembrane-space
reference proteins, with EXOG, worm CPS-6 and yeast NUC1 as controls. Every sequence fact
it reports I checked against our own UniProt record and all are correct: transit peptide
1-48 with mature chain 49-297, three cysteines in total (positions 84, 113, 196),
presequence 16.7% arginine with net charge +5, and no twin CX9C or CX3C motif.

The one solid gain is a negative. ENDOG enters by the cleavable-presequence TIM23 route and
is **not** a MIA40 disulfide-relay substrate
[file:human/ENDOG/ENDOG-hypotheses/submitochondrial-localization-ims-vs-matrix/openscientist.md
"ENDOG is imported via the cleavable-presequence (TOM/TIM23) pathway, not the MIA40
twin-cysteine pathway"], which rules out the twin-cysteine class of intermembrane-space
residents such as CHCHD4 and TIMM13. That rests on a cysteine count anyone can repeat.

It does not settle the compartment, and the run is clear about why. The presequence route
delivers to both destinations
[same file "Many IMS proteins (DIABLO/SMAC, HTRA2) are delivered by the same presequence
machinery, then arrested or sorted into the IMS"], and its classifier failed on exactly
those proteins while reaching only [same file "LOO-CV accuracy = 60.0% (9/15)"] against a
53% majority-class baseline. The presequence signature is also shared with EXOG, so it is a
family trait, not a discriminator. A dual or regulated localization fits everything computed
[same file "reconciles all observations and is not excluded by any sequence feature computed
here"].

Two limitations it stated plainly rather than papering over: no external localization
predictor was reachable (DeepMito returned 404, MitoFates refused the connection), so the
result rests on its own classifiers; and it did not retrieve the four context papers I
supplied, taking them as given.

Consequences for the review. No action changed and no annotation added. The decision to stay
at the root mitochondrion term is unchanged and now better argued: the import route is
settled, the compartment is not. The sub-compartment check on the inner-membrane row records
the import-pathway finding alongside the conflicting fractionation and imaging evidence. I
did not adopt the run's suggestion to add `GO:0042645 mitochondrial nucleoid` from the TFAM
colocalization — that is a judgement about whether one imaging result supports a
sub-organelle component term, and it belongs to a curator reading PMID:36394256 directly,
not to a sequence analysis that never opened the paper.

What would settle it is unchanged from the organelle-policy note above and is cheap: mitoplast
protease protection, where intermembrane-space proteins are degraded on swelling and matrix
proteins are protected.

## 2026-10-30 — review round 1 on PR #5618

Four blocking items. All addressed; the first changed a curation judgement, the rest
were corrections to how evidence was cited.

**`GO:0005743` had no positive support for its own term.** The reviewer was right: the
two quotes I attached asserted the intermembrane space and the matrix, which contradict
each other and neither of which names the inner membrane, and my `reason` argued about
whether to *add* a sub-compartment row rather than whether *this* row should stand. So I
ran the donor check the organelle policy prescribes, and it settles the row in the
keep direction. Both PAINT donors carry `GO:0005743`: yeast Nuc1, where the purification
of the major yeast mitochondrial nuclease places the activity in the inner membrane
[PMID:3286639 "in the mitochondrial inner membrane"], and human EXOG, by IDA from
PMID:18187503. That EXOG paper turns out to carry the decisive evidence for ENDOG itself,
not just for the donor [PMID:18187503 "Following mitochondrial subfractionation EXOG and
EndoG were both found in membrane fractions, co-localizing with CYTC, COX-IV and TOM20"],
and it explicitly [PMID:18187503 "exclude their presence as soluble proteins of the
intermembrane space or the mitochondrial matrix"]. Two limits recorded on the row: the
assay used tagged expressed protein, and the membrane fractions co-stained for inner
(COX-IV) and outer (TOM20) markers together, so it supports membrane association without
separating inner from outer. The row stays `KEEP_AS_NON_CORE`, now for a stated reason.

That result also tidies the sub-compartment conflict rather than deepening it: a protein
in neither soluble compartment is consistent with fractionation studies disagreeing about
which soluble compartment it is in.

**`GO:0051880` G-quadruplex DNA binding is now a `NEW` IDA row.** My reason for declining
it was wrong, and the reviewer identified exactly why: I justified it as "should come from
a curator reading the primary assays", but I had read PMID:36394256, cached its full text,
and was already quoting it for a core function. That reason correctly rejects run 1's
inference about the breakpoint landscape; it says nothing about the binding activity. The
paper shows selectivity in cells [PMID:36394256 "The findings from mito IP studies suggest
that Endonuclease G only binds to the G-quadruplex forming regions and not to the other
areas of mtDNA"] plus BG4 colocalisation and in vitro structure work. The gene otherwise
carries no DNA-binding molecular function once `GO:0003676` is narrowed to the catalytic
terms. The substantive caveat is recorded on the row: selectivity is shown by
immunoprecipitation and imaging, not by a measured affinity comparison against
unstructured duplex DNA.

**Two citation corrections.** The `GO:0004521` quote stopped one clause short, at "could be
cleaved by EndoG" — a speculation — while the `reason` asserted a demonstration; it now
runs on into the result. And both `KEEP_AS_NON_CORE` rows carried
`root_cause: NO_FAILURE_CORE`, which asserts the propagated annotation is core for the
target and contradicts the action; both are now `NO_FAILURE_NON_CORE`. The three
`NO_FAILURE_CORE` rows that remain are all `ACCEPT`.

**`GO:0042645` mitochondrial nucleoid stays declined, for the reviewer's sharper reason.**
Mine was procedural. The real objection is that adding a nucleoid component term would
quietly resolve the matrix side of the intermembrane-space-versus-matrix conflict that this
same review says is unresolved — it would assert by annotation what the evidence does not
settle.

## 2026-10-30 — review round 2 on PR #5618

One blocking item and four suggestions, all taken.

**`PMID:3286639` was cited but never declared.** The yeast half of the `GO:0005743` donor
check rested on it, yet it appeared only in a `reason` and a `supported_by`, never in
`references:`. That is a real gap and not a cosmetic one: an undeclared reference gets no
title cross-check against the fetched record and no `reference_review`, so a 1988
abstract-only paper was doing load-bearing work with no recorded adjudication. Declared,
with the abstract-only state stated, and its quote extended from the bare fragment to the
clause that carries its subject [PMID:3286639 "The enzyme is located in the mitochondrial
inner membrane"]. Worth noting that local validation passes either way — nothing in the
tooling catches a cited-but-undeclared reference, which is why a reader caught it.

**Figure 3B removes the limit the row was conceding.** I had recorded that
subfractionation cannot separate inner from outer membrane, which is true of panel A. The
reviewer pointed at panel B, immunogold electron microscopy, whose legend does separate
them [PMID:18187503 "Both proteins are often found delineating the cristae, pointing
towards an association with the inner mitochondrial membrane"]. Cristae are inner
membrane, so this speaks to the row's own term. Taken, with the discrepancy inside that
paper recorded rather than smoothed over: the running text describes the EM for EXOG and
cites earlier work for mammalian EndoG, so the legend's statement about both proteins is
the stronger of the two, and the experiment used tagged expressed protein throughout.

A further detail from the same paper, not used for an annotation but worth knowing: its
summary table lists mammalian EndoG's localization as [PMID:18187503 "IMS, IMM, MM"] —
intermembrane space, inner membrane and matrix together. The paper that established the
EndoG/EXOG split already recorded the multi-compartment picture this review has been
circling.

**The `GO:0006309` argument was leaning on a result from the paper it discounts.** My
closing clause said the cleaner allele "still leaves the reduced fragmentation reported in
heterozygous cells" — but that is PMID:14663139's result, and PMID:15601850 names the
heterozygote finding specifically as the suspect one. Discounting a paper and then relying
on its weakest datum is incoherent, and the conclusion never needed it: the purified human
enzyme on isolated nuclei (PMID:11606588) and fragmentation in CAD-deficient cells
(PMID:11452314) already carry "the activity is real". Clause replaced with those.

**`GO:0051880` now also sits on the `GO:0003676` MODIFY.** The reviewer noted that row's
reason had gone stale — it argued for replacing the binding ancestor with catalytic terms
only, which was written when the review held that no binding function was supported. That
stopped being true this round. Adding the term to the replacement list makes the narrowing
a real refinement of binding rather than narrowing all binding away while re-adding a
binding term elsewhere in the same file. The `NEW` IDA row stays, as the thing that
establishes the term; this mirrors `GO:0006308` pointing at `GO:0006309`.

## 2026-10-30 — review round 3 on PR #5618

Two blocking items, both prose in a `reason` asserting more than the source does, in a
review whose whole point is not doing that. Both verified independently before editing.

**The `PMID:18187503` EndoG construct is bovine, not human.** The reviewer corrected
credit it had given me in round 2, and it is right. That paper's methods say
[PMID:18187503 "we expressed 3 × FLAG fusion proteins of human EXOG, and, for comparison,
of bovine EndoG in mammalian cell lines"], and its Table 1 lists the organisms as
[PMID:18187503 "OrganismS. cerevisiaeB. taurusH. sapiens"] — yeast Nuc1, bovine EndoG,
human EXOG. I had read that sentence while pulling the membrane quotes and missed what it
meant for the claim I then wrote, which was that this is "direct evidence for membrane
association of ENDOG itself". The mitochondria are human; the EndoG is not. Reworded to
name the bovine ortholog expressed in human cells, and the species added as a third stated
limit beside the tagged-protein and marker limits. The action does not change: bovine
EndoG is not one of the PAINT donors, so the evidence is still independent of the
annotations the row inherits rather than a restatement of them.

**`GO:0004520` and `GO:0004521` are not descendants of `GO:0003676`.** My rewritten
`GO:0003676` reason closed by calling all three replacements descendants of it. Checked
against the local GO build: the two endonuclease terms have `GO:0004518` nuclease activity
and `GO:0003824` catalytic activity among their ancestors and neither `GO:0003676` nor
`GO:0005488`; only `GO:0051880` has `GO:0003677` and `GO:0003676`. Binding and catalytic
activity are separate children of molecular_function. The reviewer flagged that it could
not reach OLS and asked for confirmation before I edited, which was the right instinct on
a claim of that shape. The reason now says what is true and is a better argument anyway:
the two catalytic terms are a lateral correction, which CLAUDE.md explicitly sanctions for
a MODIFY whose replacement is not a descendant, and `GO:0051880` is the one genuine
descendant, kept so that narrowing a binding proxy does not discard binding altogether.

**The qualifier suggestion, taken as a source defect.** `GO:0005743` is inherited as
`is_active_in`, but everything now supporting it is localization — immunogold at the
cristae, exclusion from both soluble fractions, the yeast purification — and the same row
argues that cleaving mtDNA needs matrix access. So `located_in` fits the support and
`is_active_in` asserts more. No review action changes a qualifier, so this is recorded as a
`WRONG_QUALIFIER` source defect against GO_CENTRAL with `confidence: PROBABLE`, raised as
a query rather than a correction, since the PAINT node may rest on evidence not visible
from here.

## 2026-10-30 — review round 4 (approved, three prose suggestions taken)

Round 4 approved the review and raised three suggestions, all prose inside a `reason`, none touching an action, term, replacement list or quote. All three are taken.

The `GO:0051880` row's stated motivation had gone stale and made the two rows read in a small circle. Its reason opened by saying the gene carried no DNA-binding molecular function once `GO:0003676` was narrowed "to the two catalytic terms" — but round 2 made that replacement list three terms, `GO:0051880` among them. So the MODIFY pointed here for its binding descendant while this row said binding was needed because the MODIFY had left none, and the premise named a state of the file round 2 had removed. The reason now follows the `GO:0006308`→`GO:0006309` pattern already used elsewhere in this review: the MODIFY names the term, and this row is what establishes it by IDA on the primary assays. The caveat about qualitative selectivity is unchanged, and the sentence duplicating the new opening was dropped.

The `GO:0003676` reason said "all three are terms the gene carries elsewhere in this review", which blurred two different statuses: `GO:0004520` and `GO:0004521` are existing GOA rows, while `GO:0051880` is proposed as NEW here. Both are now stated separately, since a reader checking the replacement list against GOA will find only two of the three.

The `source_defects` entry used `slot: qualifier`; the repository's convention is the GAF column name, `Qualifier`, which 49 other entries use and which `just export-source-defects` groups on. Corrected.

The reviewer recorded that it could not re-run the QuickGO donor queries or re-query the GO ancestor paths from its sandbox, and that both now sit in the file itself rather than only in a review thread. That is the intent of the round-3 rewording and is left as is.

## 2026-10-30 — round 5 approved; one rewrap, and why the branch was touched again

Round 5 approved the review and left one trivial nit: the round-4 rewrite of the `GO:0051880` reason left a 124-character source line where the file wraps near 78. My tidy-up pass had rewrapped the line I was looking at and pushed the overflow onto the next one, which is how that survived a reread of my own diff. The reviewer's disposition was to fold it in only if the branch were touched again for another reason, and not to spend an approval on it. That other reason then arrived.

The deterministic auto-merge controller skipped the PR with `checks not passing: claude-review=cancelled, suite (3.12)=cancelled, test (3.12)=failure, validation (3.12)=cancelled`. None of those is a content failure. They belong to a duplicate `pull_request` run created one second before the surviving run on the identical commit and cancelled by the concurrency group; its gate job read `cancelled` from its own upstream jobs and exited 1. Both runs post check runs under the same four names, so the commit ends up carrying a good and a bad copy of each. Branch protection reads the latest per name and reported the PR clean, which is why this stayed invisible; the controller's rollup reads all of them and requires that nothing be failing or cancelled.

The consequence is worth recording, because it is not specific to this gene: a duplicate-run race can park cancelled check runs on a head commit and block that PR from auto-merging indefinitely, while every human-visible signal — branch protection, the PR's own merge state, the review verdict — says the PR is ready. The shepherd's own `retry-reviews` job cannot clear it either, since it looks for a missing current-commit verdict and this commit has one. Re-running the cancelled run returns HTTP 403 for this agent, so a new head commit was the only lever I had — and it turned out not to be a remedy at all. The push reproduced the race within the same second (runs 41098739065 and 41098738900 cancelled alongside their survivors), parking the same four check runs on the new commit. The race is deterministic on push, so no amount of pushing clears it.

So the rewrap is the content of a commit whose intended purpose was to mint a clean head, which it failed to do. Parsing the file before and after yields an identical document, so nothing semantic moved: no annotation, action, term, replacement list, quote, qualifier or rendered page. The `reason` is a plain multi-line scalar rather than a folded block scalar — there is no `>` indicator — but line breaks fold to single spaces either way, so the identical-document result stands.

## 2026-10-30 — round 6 approved; correcting a claim this file had already been refuted on

Round 6 approved `084e6c9` and raised two suggestions. Both are taken, and the first was the one worth taking.

**The committed record asserted something the thread had already retracted.** The paragraph above, and the `details` of the history record for that commit, both said a new head commit "was the only remedy available" for the cancelled-duplicate check runs. That commit's own check runs refute it: the race reproduced within the same second on the new head (runs 41098739065 and 41098738900 cancelled alongside their survivors), so pushing is not a remedy and never was. The correction had been posted as a PR comment and left out of the file — which is precisely the failure mode this review has invoked three times in its own favour, that a claim belongs in the file rather than in a closed thread. The paragraph is corrected in place. The history record is append-only and accurately describes what I believed while that session ran, so it stays as written and the correction is carried by the record for this commit instead.

**Three source lines over 100 characters, all in text this PR authored**, are rewrapped: two in `description` and one in a `reference_review`. Round 5's nit was closed for the line it named and left open for its siblings, which is a fair reading of what "fold it in" should have meant.

**Terminology, noted for accuracy rather than consequence.** I called the `GO:0051880` `reason` a folded block scalar in the previous commit message and in these notes. It is a plain multi-line scalar — no `>` indicator. Line breaks fold to single spaces in both forms, so every claim that rested on the folding behaviour still holds; the name was simply wrong.

The merge block itself is unchanged and is not this PR's to fix. Round 6 independently confirmed both halves from the code: the `test` gate at `.github/workflows/main.yaml:443-458` is `if: always()` where the same file already uses `!cancelled()` twice, and `check_rollup_decision` in `scripts/auto_merge_ready_prs.py:309-332` iterates every rollup entry without collapsing to the latest per name, with `PASSING_CONCLUSIONS` at `:84` excluding `CANCELLED`. Fixing only the workflow would remove the `failure` and leave the three `cancelled` entries, so the controller change is the necessary one. Both are repo-wide and await a maintainer's decision.
