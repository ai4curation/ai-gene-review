# NLRP3 review notes

Reviewer journal. 188 existing annotations over 56 distinct GO terms; every decision was taken
once per term and applied to all instances of that term regardless of evidence code.

## The 2026 dispute, and what it does (and does not) bear on

Two 2026 papers give partly conflicting accounts of where and in what oligomeric state NLRP3 acts.

**Mateo-Tórtola et al., Nat Commun 2026** ([PMID:42215451]) - two parallel pathways:
[PMID:42215451 "NLRP3 forms an inactive decameric cage, that upon interaction with the
trans-Golgi network (TGN) and microtubule organization center (MTOC), leads to inflammasome
activation, yet whether non-decamer NLRP3 species form functional inflammasomes remains
unclear."] and
[PMID:42215451 "nigericin, a K+-dependent NLRP3 stimulus, can trigger two distinct activation
pathways: (i) the rapidly engaged decameric cage-dependent pathway; and (ii) a decameric
cage-independent, TGN/MTOC-distal, and slow-reacting pathway employed by low molecular weight
NLRP3 species, that dominates in human neutrophils."].

**Wu & Wu, PNAS 2026** ([PMID:42378282]) - everything converges on the centrosome:
[PMID:42378282 "The NLRP3 inflammasome is central to host defense and sterile inflammation and
forms condensates at the microtubule-organizing center (also known as the centrosome), although
the mechanisms regulating this process remain unclear."],
[PMID:42378282 "Microtubules, priming, and NEK7 synergistically converge on PCM abundance,
thereby creating a permissive centrosomal environment for NLRP3 condensation and inflammasome
assembly."], and the bypass result
[PMID:42378282 "Elevated NLRP3 expression compensates for limited PCM abundance, rendering K+
efflux-induced activation independent of both NEK7 and priming in human and mouse macrophages."].

**The curation discipline that matters here:** almost all of this is about *localisation and
assembly state*. It is CC and BP evidence, not MF. Neither paper measures a new molecular
activity of NLRP3, and neither was used to change a molecular-function action. What they did
change is the `reason` text on the MTOC (`GO:0005815`), trans-Golgi network membrane
(`GO:0032588`) and condensate-scaffold (`GO:0140693`) annotations, which now say explicitly
that the MTOC/dTGN route is a major but non-obligatory pathway.

The NEK7 disagreement is recorded in `suggested_questions` rather than adjudicated. The two
results may be compatible - both involve NLRP3 abundance thresholds - but nothing in either
abstract settles it, and PMC access to the PNAS paper was blocked, so only its abstract could
be read (recorded as `full_text_unavailable: true`).

## Molecular sensor activity: the central MF call

`GO:0140299` is defined as **"Binding to a molecule and eliciting a change in the protein's
activity in response to the intracellular level of that molecule"** (QuickGO). That definition
requires the sensed species to be *bound*. NLRP3 has no established direct agonist ligand at
all - it is thought to read a common cellular perturbation.

Worse, the papers cited as the IDA support argue against direct binding themselves:
[PMID:18604214 "NALP3 activation required phagocytosis of crystals, and this uptake
subsequently led to lysosomal damage and rupture."] and
[PMID:18604214 "Our results indicate that the NALP3 inflammasome senses lysosomal damage as an
endogenous 'danger' signal."].

The convergence model is stated most cleanly by Chen & Chen:
[PMID:30487600 "These results indicate that recruitment of NLRP3 to dTGN is an early and common
cellular event that leads to NLRP3 aggregation and activation in response to diverse stimuli."].

**Call: `MARK_AS_OVER_ANNOTATED`**, not REMOVE (these are experimental annotations recording
real activation events) and not ACCEPT (the term asserts a ligand that does not exist). The one
NLRP3 binding event that *does* satisfy the definition - PtdIns4P on the dispersed TGN - is
already separately annotated as `GO:0070273`, and that is where the ACCEPT went:
[PMID:30487600 "NLRP3 is recruited to the dispersed TGN (dTGN) through ionic bonding between its
conserved polybasic region and negatively charged phosphatidylinositol-4-phosphate (PtdIns4P) on
the dTGN."].

Because this leaves NLRP3 with no ligand-independent sensor MF, I proposed a new term,
**inflammasome sensor activity**, under `GO:0038187 pattern recognition receptor activity`. The
gap is general (NLRP1, NLRP6, NLRC4, pyrin).

## Peptidoglycan binding: the one REMOVE

`GO:0042834 peptidoglycan binding`, TAS from [PMID:15967716], a 2005 NLR review. The abstract
contains no peptidoglycan claim, and no primary study ever demonstrated NLRP3-peptidoglycan
binding. This descends from the mid-2000s proposal that NALP3 senses bacterial peptidoglycan and
MDP; the dedicated peptidoglycan sensors turned out to be NOD1/NOD2. REMOVE is appropriate here
and only here: it is a curator assertion from a review, not an experimental call, so no
curator's reading of a primary dataset is being second-guessed. Leaving a ligand-binding MF
asserted for a protein with no known ligand is the kind of machine-readable falsehood downstream
tooling believes.

## The sequence-specific DNA binding annotations

`GO:0043565` (IBA + ISS), `GO:0140297` DNA-binding transcription factor binding (IBA + ISS),
`GO:0005634` nucleus, `GO:0045944`, and the four Th2 terms (`GO:0002830`, `GO:0032753`,
`GO:0045630`, `GO:2000553`) - **nine terms, one source**. Traced through the GOA WITH/FROM
columns: the IBAs come from node `PANTHER:PTN000648032` with donor `MGI:2653833` (mouse Nlrp3);
every ISS has donor `UniProtKB:Q8R4B8` (mouse Nlrp3). Both trails end at Bruchard et al. 2015:
[PMID:26098997 "In TH2 cells, NLRP3 bound the Il4 promoter and transactivated it in conjunction
with the transcription factor IRF4."] and
[PMID:26098997 "NLRP3, but not the inflammasome adaptor ASC or caspase-1, positively regulated a
TH2 program."].

Against it: single laboratory; mouse only; a published corrigendum ([PMID:26580508], verified in
PubMed as Nat Immunol 2015;16(12):1292); no human experimental evidence; and no NLRP3 DNA-binding
domain or NLRP3-DNA structure in the decade since, despite very heavy structural work on this
protein. In its favour: the NACHT-LRR architecture is shared with CIITA, a genuine
transcriptional activator, so it is not biologically absurd.

**Call: `KEEP_AS_NON_CORE` across all nine**, with the provenance spelled out. Not REMOVE -
surprise is not evidence. Not challenged on propagation grounds either: the IBD node placement
follows correctly from the mouse experimental annotation, so no `propagation_review` was
fabricated; the issue is the strength of the source, not the phylogeny. The question of whether
these should be retired is put to experts in `suggested_questions`.

## A systematic sign error in the CAPS annotations

Four annotations invert the direction of the biology:
- `GO:0032691` negative regulation of IL-1beta production, IMP from [PMID:12483741] (NOMID)
- `GO:0050728` negative regulation of inflammatory response, IMP from [PMID:12483741],
  [PMID:16531551], [PMID:17178985]
- `GO:0002674` negative regulation of acute inflammatory response, IMP from [PMID:11687797]

All four are CAPS genotype-phenotype studies. CAPS mutations are dominant **gain-of-function**
alleles causing constitutive inflammasome activity and excess IL-1beta - which is precisely why
two of these papers are reports of clinical improvement on IL-1 receptor antagonism. GOA already
carries the positive counterparts with 13 (`GO:0032731`) and 9 (`GO:0050729`) annotations.

**Call: `MODIFY` with the positive term as replacement**, not REMOVE. The patient data are
sound; only the direction of the inference is wrong, so a sign correction is the right
instrument. One alternative reading is recorded in the `reason` for completeness: early work did
report that wild-type cryopyrin suppresses NF-kappaB ([PMID:14662828]), which could motivate a
negative annotation - but that is captured separately by `GO:1901223`, and these references are
not NF-kappaB assays.

## Both directions of NF-kappaB regulation are in GOA

`GO:1901223` negative regulation of non-canonical NF-kappaB (IBA + IDA from [PMID:14662828]:
"Transfection of full-length CIAS1 or either of two shorter, naturally occurring isoforms
dramatically inhibited TNF-alpha-induced activation of NF-kappaB reporter activity") and
`GO:1901224` **positive** regulation of the same pathway (IPI from [PMID:15817483], WITH/FROM
`UniProtKB:Q9ULZ3` = ASC), consistent with [PMID:11786556 "Furthermore, coexpression of PYPAF1
with ASC results in a potent synergistic activation of NF-kappaB."].

Both are overexpression reporter assays from the early 2000s; neither has been tested at
endogenous levels. **Both KEEP_AS_NON_CORE**, deliberately, so the contradiction stays visible
in the record rather than being silently resolved by a reviewer who has no basis to pick a side.

## A broken PMID in GOA

`GO:0060090 molecular adaptor activity` and `GO:0030674 protein-macromolecule adaptor activity`
are both IDA from **PMID:1189953**. Fetched and checked: that identifier resolves to
"[Profanities and the profane person].", Alva Quiñones J, *Acta Psiquiatr Psicol Am Lat* 1975 - a
Spanish-language psychiatry abstract. It is a digit-dropped **PMID:31189953** (Sharif et al.,
Nature 2019, NEK7-licensed NLRP3 activation), which supports the neighbouring annotations made on
the same dates. Recorded as `correctness: WRONG_IDENTIFIER` / `relevance: NONE` in
`reference_review`; the two annotations are MODIFYed to `GO:0035591 signaling adaptor activity`
on their merits (both are under-specific parents).

## Contested localisations: mitochondrion and ER

GOA carries mitochondrion (IEA + EXP [PMID:21124315] + IDA [PMID:23582325]) and ER (IEA + ISS)
alongside dTGN and MTOC. The mitochondrial model is real experimental work -
[PMID:23582325 "MAVS mediates recruitment of NLRP3 to mitochondria, promoting production of
IL-1β and the pathophysiologic activity of the NLRP3 inflammasome in vivo."] and
[PMID:21124315 "Resting NLRP3 localizes to endoplasmic reticulum structures, whereas on
inflammasome activation both NLRP3 and its adaptor ASC redistribute to the perinuclear space
where they co-localize with endoplasmic reticulum and mitochondria organelle clusters."] - but
it has been largely displaced by the dTGN/MTOC account, which explains activation by
structurally unrelated stimuli, and neither 2026 paper invokes mitochondria.
**KEEP_AS_NON_CORE for both**, with the displacement stated.

## Resting oligomer: decamer vs dodecamer

Worth flagging because it feeds the 2026 dispute. [PMID:35114687 "Inactive, ADP-bound NLRP3 is a
decamer composed of homodimers of intertwined leucine-rich repeat (LRR) domains that assemble
back-to-back as pentamers."] versus [PMID:35254907 "The inactive NLRP3 oligomer represents the
NLRP3 resting state, capable of binding to membranes and is likely disrupted for its
activation."] - the latter paper describes a **dodecamer**. This does not change any action
(`GO:0042802` and `GO:0051260` are ACCEPTed either way) but it is recorded in those `reason`
fields and raised in `suggested_questions`.

## Core functions selected

Five, each a distinct mechanistic step rather than five names for one thing:
1. `GO:0035591` signaling adaptor activity - PYD filament nucleates ASC polymerisation.
2. `GO:0140608` cysteine-type endopeptidase activator activity - caspase-1 activation, the output.
3. `GO:0070273` phosphatidylinositol-4-phosphate binding - dTGN recruitment; the only
   well-established direct binding event.
4. `GO:0016887` ATP hydrolysis activity - the NACHT nucleotide switch between the ADP-bound cage
   and the ATP-bound active disc; also the MCC950 site.
5. `GO:0140693` molecular condensate scaffold activity - centrosomal condensation, with the
   MTOC-distal caveat.

Deliberately **not** core: molecular sensor activity (see above), bare protein binding (24 IPI
annotations, MARK_AS_OVER_ANNOTATED), apoptotic process (NAS, a relic of the "Apaf1-like" naming
era - NLRP3's death modality is pyroptosis), and the entire Th2/transcription cluster.
