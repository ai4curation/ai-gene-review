# AAD3 (YCR107W) — S. cerevisiae — Curation Notes

Journal of research and reasoning for the AI GO-annotation review. Provenance recorded inline.

## Deep research status (provenance)

Automated deep research was attempted but did not produce a report:
- `just deep-research-falcon yeast AAD3 --fallback perplexity-lite`: falcon timed out at 600s;
  perplexity-lite fallback returned HTTP 401 "insufficient_quota" (billing/quota exhausted).
- Retry `just deep-research-falcon yeast AAD3`: falcon timed out again (SIGTERM at the 600s cap).

No `-deep-research-{provider}.md` file was fabricated (per repo policy). The review is instead
grounded in the primary sources actually available: the UniProt record (P25612), the QuickGO GOA
export, the cached Delneri et al. 1999 abstract (PMID:10572264), and the InterPro/PANTHER family
metadata (PTHR43364), plus the inline sequence/domain analysis recorded below. This documentation
serves in place of a deep-research report.

## Identity

- **Gene**: AAD3 (SGD standard name); systematic name **YCR107W** (chromosome III).
- **UniProt**: P25612 (AAD3_YEAST), Reviewed/Swiss-Prot.
- **Length / MW**: 363 aa; 40911 Da. CHAIN 1..363 (full-length; no signal peptide, no reported fragment/truncation).
- **Name meaning**: "Putative aryl-alcohol dehydrogenase AAD3"; EC=1.1.1.- (partial/unassigned).
- **Family (UniProt SIMILARITY)**: "Belongs to the aldo/keto reductase family. Aldo/keto reductase 2 subfamily." (ECO:0000305 = curator inference from sequence).
- **Domain**: Pfam PF00248 (Aldo_ket_red), full-length match; Gene3D 3.20.20.100 (NADP-dependent oxidoreductase domain); SUPFAM SSF51430 (NAD(P)-linked oxidoreductase); CDD cd19147 (AKR_AKR9A3_9B1-4); InterPro IPR050523 (AKR_Detox_Biosynth), IPR023210, IPR036812.
- **PANTHER**: PTHR43364 ("NADH-SPECIFIC METHYLGLYOXAL REDUCTASE-RELATED" / family name "Aldo/Keto Reductase Detoxification and Biosynthesis") and subfamily PTHR43364:SF2 ("ARYL-ALCOHOL DEHYDROGENASE AAD10-RELATED").
- **PE (protein existence)**: PE=3, "Inferred from homology" — i.e. no protein-level or transcript-level experimental evidence recorded in UniProt for AAD3 itself.

## The AAD gene family in S. cerevisiae (important — separate AAD3 from paralogs)

The AAD (Aryl-Alcohol Dehydrogenase) genes are a family of paralogous ORFs in S. cerevisiae,
most located in subtelomeric regions. Members include AAD3 (YCR107W), AAD4 (YDL243C),
AAD6 (YFL056C), AAD10 (YJR155W), AAD14 (YNL331C), AAD15 (YOL165C), AAD16 (YFL057C).
They were identified by in-silico similarity to a *bona fide* fungal enzyme, and none has a
demonstrated enzymatic activity or loss-of-function phenotype in S. cerevisiae. Evidence for
AAD3-specific function must therefore be distinguished carefully from family-level statements.

## KNOWN (evidence-supported)

1. **AAD3 is a member of the aldo/keto reductase (AKR) superfamily.** Sequence/domain evidence:
   Pfam PF00248 covers the full 363-aa ORF; AKR fold assignments (Gene3D, SUPFAM, CDD, InterPro
   IPR050523). This is solid at the level of *fold/superfamily membership*, not specific catalysis.
   [UniProt P25612 DR lines: Pfam PF00248; Gene3D 3.20.20.100; SUPFAM SSF51430; InterPro IPR050523]

2. **The AAD family was defined by similarity to the *Phanerochaete chrysosporium* aryl-alcohol
   dehydrogenase (AAD), a lignin-degradation enzyme.** The ISS annotations on AAD3 use
   `with/from = UniProtKB:Q01752`, which is the *P. chrysosporium* AAD (a white-rot fungus enzyme),
   NOT a yeast protein. [PANTHER PTHR43364-entries.csv: "Q01752 ... Phanerodontia chrysosporium ...
   Aryl-alcohol dehydrogenase [NADP(+)]"] [PMID:10572264 abstract: "seven open reading frames (ORFs)
   in Saccharomyces cerevisiae whose protein products show a high degree of amino acid sequence
   similarity to the aryl alcohol dehydrogenase (AAD) of the lignin-degrading fungus Phanerochaete
   chrysosporium"].

3. **Deletion of the seven yeast AAD genes (including AAD3) produced NO aryl-aldehyde-degradation
   phenotype.** [PMID:10572264 abstract: "None of the knock-out strains revealed any mutant phenotype
   when tested for the degradation of aromatic aldehydes using both spectrophotometry and high
   performance liquid chromatography (HPLC)."] Ergosterol/phospholipid profiles, mating and
   sporulation were also unaffected in the septuple deletant. Note: the stationary-phase aryl-alcohol
   dehydrogenase activity observed in wild-type yeast [same abstract] was NOT abolished by deleting
   all seven AAD genes, implying the measured cellular AAD activity is contributed by other (non-AAD)
   enzymes, and that the AAD genes are functionally redundant or silent under the conditions tested.

## NOT known / open (knowledge gaps)

- Whether AAD3 encodes a catalytically active enzyme at all. No in vitro activity, no substrate,
  and no kcat/Km have ever been reported for the AAD3 gene product specifically. EC is 1.1.1.- .
- The physiological substrate and biological role (if any). The "aryl-alcohol dehydrogenase" name is
  purely a homology transfer from the *P. chrysosporium* enzyme; S. cerevisiae is not a lignin
  degrader, so the ancestral aryl-alcohol/lignin-related context does not obviously apply.
- Subcellular localization is unassigned (GOA has an ND `is_active_in cellular_component` root
  annotation, GO_REF:0000015).
- Whether AAD3 is a functional gene, a conditionally-expressed paralog, or a degenerate/relic
  subtelomeric duplicate. The AAD family expansion sits in subtelomeric regions that are hotspots
  for gene duplication, rapid evolution, and pseudogenization.

## Domain / truncation reasoning (inline bioinformatics)

I inspected the UniProt sequence directly (no sub-agent).

- **Full length, not truncated**: FT CHAIN 1..363 spans the whole sequence; MW 40911 is typical of a
  complete ~360-aa AKR (AKRs are ~320-360 aa). There is no `FT ... FRAGMENT`, no premature-stop
  evidence, and the Pfam PF00248 match covers the full ORF. So AAD3 is NOT a truncated ORF/relic at
  the sequence level; it is an intact reading frame.
- **AKR fold features present**: the N-terminal glycine-containing cofactor-loop region is present
  (`...PLILGEV...` around residues 29-34), the AKR core His/Trp region is present
  (`...DILYVHWWDY...` around residues 143-152, containing His147 and the conserved Trp pair), and a
  C-terminal NADP-binding-loop-like region is present (`...AYVRSKA...` around 294-300). These are
  consistent with a foldable AKR domain.
- **BUT**: presence of the fold and generic catalytic-type residues does NOT establish a specific,
  physiologically relevant catalytic activity. AKR-fold proteins are notoriously promiscuous and
  many paralogs are pseudo-/orphan enzymes. Given (a) no experimental activity for AAD3,
  (b) the ISS is transferred from a distant fungal enzyme, and (c) the loss-of-phenotype on
  septuple deletion, a *specific* "aryl-alcohol dehydrogenase (NADP+) activity" (GO:0047681)
  assignment for AAD3 is an over-annotation. The defensible statement is superfamily-level
  oxidoreductase/AKR membership, with substrate unknown.
- I did not have a residue-level MSA against a curated AKR catalytic tetrad reference in the cache,
  so I deliberately do NOT claim the catalytic tetrad is "intact and competent" or "degenerate" —
  I claim only that the ORF is full-length and adopts an AKR fold, and that specific activity is
  unproven. This keeps the review honest.

## Annotation-by-annotation reasoning

GOA (AAD3-goa.tsv) has 4 annotations:

1. `GO:0047681 aryl-alcohol dehydrogenase (NADP+) activity` / IEA / GO_REF:0000117 (ARBA machine rule).
   Over-annotation: an electronic rule assigning a *specific* activity to a putative enzyme with no
   demonstrated activity and a full-family loss-of-phenotype. → MARK_AS_OVER_ANNOTATED
   (propagation_review IEA rule; the correct grounded statement is superfamily-level AKR/oxidoreductase).

2. `GO:0006081 aldehyde metabolic process` / ISS / PMID:10572264, with Q01752.
   ISS from the *P. chrysosporium* AAD. Family-level; not demonstrated for AAD3. Aldehyde metabolism
   is the plausible superfamily-level process but is unproven for AAD3 and the deletion had no aldehyde
   phenotype. → KEEP_AS_NON_CORE (retain as a plausible, unverified process-level annotation; do not
   elevate to core). Consider MARK_AS_OVER_ANNOTATED — but the parent process is broad enough that it
   is defensible as a low-confidence homology inference; keep non-core with caveat.

3. `GO:0047681 aryl-alcohol dehydrogenase (NADP+) activity` / ISS / PMID:10572264, with Q01752.
   Same specific-activity over-annotation as (1), but via ISS from the fungal enzyme. The deletion
   phenotype directly argues against a demonstrable aryl-aldehyde activity for the yeast AAD genes.
   → MARK_AS_OVER_ANNOTATED; propose generalization to superfamily-level oxidoreductase in the review
   rationale. Do NOT REMOVE (defer: it is a curator ISS, and superfamily context is real).

4. `GO:0005575 cellular_component` (root) / ND / GO_REF:0000015.
   Root "no data" placeholder. Standard. → ACCEPT (keep as-is; it is the GO ND convention for
   unknown localization).

## Term-id notes

- existing_annotations ids are from GOA and are trusted (not rewritten).
- For core_functions I will use only well-supported author-checked ids. Candidate broader MF:
  GO:0016616 "oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor"
  (verified via OLS) — this is the honest superfamily-level activity I can defend from fold + family.

## Update 2026-09-02 — direct biochemistry supersedes homology annotations

Re-review found an oversight: the prior review treated the aryl-alcohol dehydrogenase
annotations as merely *over-specific* homology transfers (MARK_AS_OVER_ANNOTATED, plus a
proposed broad GO:0016616 oxidoreductase term). The direct biochemical characterization of
the AAD3 gene product was not incorporated.

Yang et al. 2018 (PMID:29079624, Appl Environ Microbiol; full text now cached) purified all
seven recombinant Sc Aad proteins and assayed them:

- Only Aad4p and Aad14p reduced aryl-aldehydes with NADPH; **purified Aad3p was inactive on
  the whole panel.** [PMID:29079624 "only ScAad14p and ScAad4p were able to reduce a group of
  candidate aryl-aldehydes with the consumption of NADPH"]
- Aad3p has **Cys73 at the position of the catalytically essential Tyr** of the AKR tetrad,
  and **reverting Cys73→Tyr did not restore activity** ("correction of the missense mutation
  in ScAadCys73Tyrp failed to produce a functional enzyme"), so additional inactivating
  changes are present → the authors call the AAD genes (AAD3 included) **pseudogenizing**.
- **Overexpression of AAD3** did not raise aryl-aldehyde reductase activity in crude extracts
  and gave no aryl-aldehyde resistance (Fig. S7).

Consequence for annotation actions:
- The two aryl-alcohol dehydrogenase (GO:0047681) annotations (IEA and ISS) are now **REMOVE**,
  not MARK_AS_OVER_ANNOTATED: the specific function has been tested on the target and refuted
  (contradicted, not just over-specific).
- The aldehyde metabolic process (GO:0006081) ISS is now **REMOVE**: its premise (an active
  aldehyde reductase) is refuted and no phenotype ties AAD3 to aldehyde metabolism.
- The previously proposed **NEW GO:0016616 broad oxidoreductase** term is **withdrawn** and
  core_functions rewritten to "no assignable molecular function" — asserting even a broad
  catalytic activity is not defensible for a protein shown to be catalytically dead.
- ND root CC (GO:0005575) unchanged → ACCEPT.

Adamczyk et al. 2016 (PMID:27299603) added as LOW-relevance context: copy-number loss of
several AAD genes (AAD3 among them) correlates with redox imbalance in brewing strains, but is
a family-level correlation and establishes no AAD3-specific function.

## 2026-09-02 — PR #2929 review follow-up: bring knowledge_gaps and suggested_* into line

The automated review of PR #2929 correctly flagged that `knowledge_gaps`,
`suggested_questions` and `suggested_experiments` were left byte-for-byte unchanged when the
PMID:29079624 evidence was incorporated, so the file simultaneously asserted "purified Aad3p
is catalytically inactive" and "AAD3 has never been characterized". Fixed:

- **Gap 1 (MF_DARK)** narrowed and moved `OPEN` → `NARROWING`. The aryl-alcohol dehydrogenase
  activity is no longer an open question — it was assayed on the target and refuted. The
  residual gap is whether Aad3p has activity on substrate classes *outside* the tested panel
  or a non-catalytic role. Note that both cofactors were covered: [PMID:29079624 "While
  PcAad1p can use both NADPH (Km, 39 μM) and NADH (Km, 220 μM), neither of the yeast Aad
  proteins was active with NADH as a reduction cofactor."] Provenance re-pointed from
  PMID:10572264 (deletion phenotype) to PMID:29079624 (direct assay).
- **Gap 2 (BP_DARK)** kept OPEN — a biological role genuinely remains undetermined — but the
  boundary is re-anchored on the new *negative* gain-of-function and expression data, which
  exclude the aryl-aldehyde detoxification hypothesis from both directions: [PMID:29079624
  "Contrary to expectation, none of the seven AAD transcript levels increased following 1 to
  2 h treatment with aryl-aldehydes, relative to a no-aldehyde control"] and [PMID:29079624
  "None of the transformants exhibited growth improvement on the four aryl-aldehydes"].
- **Gap 3 (family expansion)** kept OPEN but restated: AAD3's functional status is now settled
  (relic), so the open question is why a catalytically dead member is retained as a
  full-length ORF across strains rather than eroded, given that AAD15 *was* truncated.
- **Q1 / experiment 1** previously proposed verbatim the experiment Yang et al. already
  performed. Rewritten to target untested space (non-aryl-aldehyde AKR substrate classes,
  direct NADP(H)-binding measurement, structure); added a question and experiment on a
  possible non-catalytic role, which is the live hypothesis for ORF retention.

Also, per the same review:
- The 4th PMID:29079624 finding's `supporting_text` was the Tyr73-repair sentence while the
  statement was about the authors' pseudogenization conclusion. Replaced with the matching
  verbatim sentence ["Our observation that the majority of BY4741 AAD genes were undergoing
  pseudogenization prompted us to survey their distribution..."].
- Added a caveat to the PMID:29079624 `review_notes` that the Cys73→Tyr revertant assay — the
  single result carrying the step from "inactive" to "irreversibly pseudogenized" — is
  reported as "data not shown". The REMOVE actions rest on the shown Fig. 1 negative result,
  not on that revertant.

Left alone (flagged for a human): the `failure_modes` asymmetry between the IEA row
(`FUNCTIONAL_DIVERGENCE`) and the ISS rows (`WRONG_ORTHOLOG_OR_PARALOG`), the suggestion to
propose a `NOT|enables GO:0047681` annotation to SGD/UniProt, and `status: INITIALIZED`.
