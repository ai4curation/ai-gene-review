# Aspartate-family trunk and threonine biosynthesis audit

## 2026-10-26 — initial evidence and scope assessment

The starting module has 19 representatives and a five-reaction backbone. Ten
fungal reviews already exist (221 annotation rows); six E. coli and three
Arabidopsis members require normal seeding. Three review panels are now working
in this independent worktree. The tentative panel is 24 proteins after adding
five candidates identified from literature or a missing plant step. Inclusion
and assertion strength remain subject to the source review.

The initial literature search identified these comparative sources:

- PMID:11352712, *The central enzymes of the aspartate family of amino acid
  biosynthesis*: original module review source for the trunk and architectures.
- PMID:9636232, *The specific features of methionine biosynthesis and metabolism
  in plants*: plant branch-point context.
- PMID:19946135, *Cohesion group approach for evolutionary analysis of
  aspartokinase, an enzyme that feeds a branched network of many biochemical
  pathways*: cross-domain distribution, divergent regulatory architectures and
  downstream pathways. Proposed evolutionary scenarios need their own evidence;
  they must not be converted into guessed PAINT nodes.
- PMID:22303247, *Aspartate-Derived Amino Acid Biosynthesis in Arabidopsis
  thaliana*: plant pathway organization and biochemical evidence boundaries.
- PMID:20019093, *Recent progress in deciphering the biosynthesis of
  aspartate-derived amino acids in plants*: regulatory and physiological context.

Normal publication fetching is underway. These leads are not yet a completed
reference assessment or a substitute for primary target evidence.

Decisive questions for the module revision:

1. The opening assertion that homoserine kinase commits substrate exclusively to
   threonine contradicts the plant branch: O-phosphohomoserine also supplies
   cystathionine gamma-synthase. The branch point must be taxon specific.
2. Pseudomonas ThrH (Q9I2Y2) offers a distinct homoserine-phosphorylation
   implementation. PMID:14699121 establishes phosphoserine-dependent transfer,
   whereas PMID:10220164 establishes in-vivo substitution for ThrB. Neither
   makes ThrH an ATP-dependent kinase; phosphoserine and the serine coproduct
   need explicit modeling.
3. PMID:12602885 characterizes Arabidopsis AKHSDH2, while the original sole plant
   fusion exemplar was AKHSDH1. Both functions and their evidence must be assigned
   to the correct isoform; failure to assay one isoform does not make it inactive.
4. Arabidopsis At1g14810/Q8VYI4 is a candidate ASAD representative. Its current
   UniProt record has no official gene symbol and its activity text is prediction
   heavy. Use the locus name and assess independent evidence. Family membership
   can support a qualified homology inference; it cannot be described as a direct
   biochemical assay.
5. Methanocaldococcus Q57991 (locus MJ0571) and ThrB/Q58504 have directly studied
   activities [PMID:17012784, PMID:11188689]. They improve archaeal sampling but
   do not, by themselves, demonstrate every reaction in an archaeal route.
6. Feedback inhibition must remain enzyme/isozyme specific; E. coli MetL, ThrA,
   LysC and the plant fusions are not interchangeable regulatory examples.
7. New fungal studies require reassessment of blanket statements that these
   metabolic proteins have no nuclear roles. PMID:39349514 distinguishes Hom6
   repair-associated results from threonine-rescuable silencing effects;
   PMID:26936955 and PMID:31784357 provide further leads. No new mechanistic
   annotation follows automatically from localization or rescue.
8. The fungal lysine-pathway boundary should use the modern functional analysis
   of putative DHDPS [PMID:29959064], rather than repeating an older generalization
   about a DAP pathway in lower fungi.

No original module assertions have been changed yet. Primary source assessment,
family/representative verification, explicit step/edge evidence, final gene
reviews, validation and a separate reviewed PR remain to be completed.

## 2026-10-26 — completed comparative module revision

The module now represents 24 reviewed proteins: ten fungi, six E. coli proteins,
Pseudomonas aeruginosa ThrH, two Methanocaldococcus jannaschii enzymes, and five
Arabidopsis proteins. Its two substantive parts contain the five required
transformations, nine alternative activity leaves, and four product-to-substrate
connections. No gene review or project tracker was edited in this module session.

### Chemistry and source assessment

- The plant branch point is O-phosphohomoserine, not an exclusive commitment to
  threonine at HSK. The full review [PMID:9636232] and the primary recombinant HSK
  study [PMID:10562426] explicitly support the shared Met/Thr intermediate. Its
  statement that the gene is on chromosome II is consistent with direct mapping
  and sequencing of At2g17265 in the full [PMID:19622802]. The otherwise useful
  full review [PMID:22303247] incorrectly gives At4g35295 for HSK. That error and
  its “threonine dehydrogenase” wording in an AK-HSDH paragraph are explicitly
  flagged in `reference_review`; neither is propagated into member identities.
- ThrH is a separate donor implementation: phosphoserine + homoserine yields
  serine + phosphohomoserine. Direct HPLC transfer evidence [PMID:14699121] is
  distinct from native double-mutant redundancy [PMID:10220164]. Its
  phosphoserine phosphatase activity is not modeled as a compulsory preliminary
  step; hydrolysis and transfer are distinct reaction outcomes. Live QuickGO
  confirms GO:0043899 has the phosphoserine donor definition and cites 14699121.
  This alternative requires upstream phosphoserine supply, outside the present
  aspartate-to-threonine boundary. It is not called ATP-dependent kinase.
- Arabidopsis AKHSDH2/O81852 is the specific subject of complementation in
  [PMID:12602885]. Both isoforms are directly compared in [PMID:16216875]; the
  differing threonine responses are not collapsed into identical regulation.
  A fusion can perform steps 1 and 3 but cannot replace intervening ASAD.
- ASAD/At1g14810/Q8VYI4 is supported by recombinant kinetics in
  [PMID:11812229], with the exact locus-to-primary linkage in the full
  [PMID:22303247]. The primary abstract reports NADPH oxidation, aspartyl
  phosphate kinetics and dimerization. ARBA-only text is not the basis for
  inclusion. The chemistry uses NADPH, not an unsupported equal NAD/NADP range.
- Direct yeast Hom6 assays [PMID:11341914] demonstrate NADH and NADPH use, but
  live GO:0004412 specifies NADP. The machine-readable reaction therefore uses
  NADPH; the independently measured additional Hom6 donor range remains explicit
  prose rather than a claim about every homolog. The module validator uses the
  current NADP-specific GO:0004073 label, while the gene validator's configured
  label alias differs; no machine-sourced GOA label was rewritten here.
- The M. jannaschii MJ0571 study [PMID:17012784] is full-text evidence for
  aspartate phosphorylation and threonine-sensitive regulation; lysine had no
  inhibitory effect up to 10 mM. ThrB studies [PMID:11188689, PMID:11535056,
  PMID:11114929] establish a second archaeal step. These two representatives
  do not prove the whole five-step pathway in this organism or all Archaea.
- Feedback and assembly remain enzyme-specific. The full comparative review
  [PMID:19946135] distinguishes ThrA threonine inhibition, LysC lysine inhibition,
  and MetL synthesis repression by methionine. These are not three interchangeable
  allosteric mechanisms. Direct Arabidopsis TS comparison [PMID:10429206] and
  activation study [PMID:9748328] support SAM regulation; SAM is not consumed by
  TS. PLP is its catalytic cofactor. No common oligomer count is asserted.
- Modern fungal DHDPS candidate testing [PMID:29959064] supports an AAA, rather
  than DAP, lysine-route boundary. Its experiments are in Coccidioides and
  Fonsecaea, not yeast Hom2 assays. Older broad “microorganism” statements are
  not evidence for a fungal DAP branch. The boundary also does not justify
  rejecting wider GO process participation by an upstream supply enzyme.
- Every leaf and connection has primary-source evidence and a literal quote.
  Connections express product/substrate continuity, not a physical metabolon,
  measured channeling, irreversibility, or a demonstrated interspecies assembly.
  The old PMID:14583263 mechanistic evidence item was removed because the cache
  has neither an abstract nor full text; its title alone does not establish the
  claimed details of reconstitution. The five transformations are independently
  supported by the other target primaries. PMID:11352712 and PMID:20019093 are reviews
  used only at the scope supported by their accessible abstracts. All 27 curated
  reference assessments record the actual evidential scope.

### Family grounding

Official PANTHER labels were read from `interpro/panther/panther.obo`, checked
against the normal release-pinned member index and the current source records.
All 24 accessions resolve. The index build initially used two unavailable organism
slugs; its normal UniProt fallback resolved all 24 target memberships. No index
row was hand-written, and the cache is not a citable or staged source.

PTHR43070:SF5 contains both monofunctional fungal Hom6 and bifunctional plant
AKHSDH2. Family membership is retained but accompanied by an explicit architecture
restriction; it does not itself establish kinase activity. MetL has an actual
source disagreement: release-pinned PANTHER assigns PTHR21499:SF29 and UniProt
assigns PTHR43070:SF3. Both are preserved by the index; the module uses the verified
UniProt placement without pretending the discrepancy is resolved. TS1 resolves
to PTHR10314:SF5, THREONINE SYNTHASE 1, CHLOROPLASTIC, within the officially named
CYSTATHIONINE BETA-SYNTHASE family. The verified narrower subfamily replaces the
previous omission motivated only by the surprising parent name. ThrH belongs to
PTHR43344:SF2, officially PHOSPHOSERINE PHOSPHATASE; direct biochemical evidence
is required for its additional transfer reaction. No ancestral PAINT node was
guessed. Further architectural alternatives discussed by 19946135, including a
phosphoglycerate-mutase-like phosphorylation implementation, remain outside this
representative panel and are not conflated with HAD-like ThrH.

### Live GO-CAM reassessment

All six cited source models were normally fetched with `--force`; the normal
index builder regenerated `gocams/index.tsv`. Every retained module activity link
was checked against its current activity ID, gene product, MF and compartment.
The source snapshots now report July–September 2026 modifications:

- HOMOSERSYN-PWY now has HOM3→HOM2→HOM6 forward edges.
- HOMOSER-THRESYN-PWY now has THR1→THR4.
- THRESYN-PWY and PWY3O-7 now have the five forward biosynthetic steps and their
  upstream supply connections. The prior claims of no causal edges were stale.
- THRESYN-PWY still assigns homoserine biosynthesis to downstream THR1/THR4;
  PWY3O-7 instead uses homoserine biosynthesis for the trunk and threonine
  biosynthesis for THR1/THR4. The previous inconsistent trunk assignment in
  PWY3O-7 no longer exists. AAT1 remains incorrectly cytosolic in the broader
  source models, judged against its mitochondrial evidence, not this boundary.
- P4-PWY-1 has only a MET7→MET6 causal association. Its formerly noted reversed
  MET6→MET17→MET2→THR1 chain is absent. Its broad threonine-metabolism process
  on every activity does not establish that each methionine-specific reaction
  participates in that process.
- PomBase 678073a900003175 retains the five cytosolic functions, and includes
  Met2/homoserine acetyltransferase, aldolase, transport and tRNA-ligation context.
  It has no causal association between the five biosynthetic activities.

### Research provenance and verification

Actual module-level Falcon and Perplexity-lite research commands were attempted
in parallel with source refresh. Falcon failed authentication/HTTP 403;
Perplexity-lite failed HTTP 401 insufficient quota. No provider report was
fabricated. The manual analysis uses the cached primary sources, full review
texts and separately completed gene reviews; all source changes came through
normal fetching/index commands.

Logic verification includes 18 explicit cases: complete representative routes for
both yeasts, E. coli ThrA or MetL fusions, and Arabidopsis AKHSDH1 or AKHSDH2;
empty context; missing ASAD despite fusion; each missing chemical transformation;
incomplete two-step archaeal panel; ThrH alone; and a clearly labeled synthetic
ThrH donor-substitution case. All pass. The 16 abstract routes are architecture/
donor/synthase combinations, not 16 experimentally observed species pathways.
The existing module logic suite passed 46 tests.

Integration initially caught a real ThrH annotation sign error: its original
NOT ATP-kinase row had been MODIFY-refined to the positive phosphotransferase
term. The owning gene reviewer corrected it to ACCEPT of the true negation,
retaining the positive phosphotransferase row separately and preserving the
original machine payload. The module was not changed to evade this conflict.
Final schema, source/term/family checks, render and helper history are recorded
in `.cache/module-audit-logs/threonine-module-*`; exact staged closure and evidence
proof are generated after these checks. No unrelated cache, tracker, commit or
push is part of this module session.
