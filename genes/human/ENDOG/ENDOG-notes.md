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
