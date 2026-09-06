# ZNG1 Gene Review Notes

## Scope of these notes

Working notes for the yeast ZNG1 (YNR029C; UniProt P53729) review. Provenance for
every substantive claim is given inline; see "Update 2026-09-06" at the end of this
file for a record of uncited/incorrect material that was removed.

## Key Findings

### Family placement
- ZNG1 is a member of the **COG0523 / G3E subfamily of P-loop GTPases**, whose
  members couple nucleotide hydrolysis to metal delivery
  [`ZNG1-deep-research-falcon.md`, "ZNG1-family proteins belong to the **G3E
  subfamily of P-loop GTPases** (COG0523 family) whose members use nucleotide
  hydrolysis to power metal delivery/insertions"].
- InterPro domain assignments for P53729 are CobW-like C-terminal
  (IPR036627/IPR011629), CobW/HypB/UreG nucleotide-binding (IPR003495), P-loop
  NTPase (IPR027417) and Zinc-regulated GTPase activator (IPR051316)
  [`ZNG1-deep-research-falcon.md` line 45] — i.e. metallochaperone/GTPase
  architecture, with no DNA-binding domain assigned.

### True Function: Zinc Chaperone
1. **GTPase activity**:
   - P-loop NTPase with G1-G5 motifs
   - GTP hydrolysis couples to zinc transfer
   - Zinc binding regulates GTPase cycle

2. **Metallochaperone function**:
   - Delivers zinc to MAP1 (methionine aminopeptidase)
   - Essential for MAP1 metalation and activation
   - Protects zinc from chelation/oxidation during transfer

3. **Regulatory mechanism**:
   - The zinc-coordinating motif is **CXCC**, not CxxC: UniProt P53729 annotates a
     `CXCC motif` feature and states that "zinc is transferred from the CXCC motif
     in the GTPase domain of ZNG1" to MAP1 (`ZNG1-uniprot.txt:71,160`).
   - GTP hydrolysis drives the transfer, and GTP/GDP exchange is required to
     release active MAP1 (`ZNG1-uniprot.txt`, PMID:35584675).

## GO Annotation Review

What this review actually does to the 22 GOA rows (18 `existing_annotations`
entries after folding duplicate `protein binding` WITH-entries into
`supporting_entities`):

- **ACCEPT (11)**: `GO:0140827` zinc chaperone activity (IBA + IDA),
  `GO:0003924` GTPase activity (IDA), `GO:0005525` GTP binding (IEA),
  `GO:0008270` zinc ion binding (IBA), `GO:0008047` enzyme activator activity
  (IDA), `GO:0051604` protein maturation (IBA, IMP, IGI), `GO:0005737` cytoplasm
  (IBA, HDA).
- **MODIFY (2)**: `GO:0016787` hydrolase activity → `GO:0003924` GTPase activity;
  `GO:0046872` metal ion binding → `GO:0008270` zinc ion binding. Both are
  IEA-level generalisations that the experimental evidence lets us make specific.
- **MARK_AS_OVER_ANNOTATED (3)**: both `GO:0005515` protein binding IPIs (per the
  project rule against uninformative `protein binding`) and `GO:0000166`
  nucleotide binding.
- **KEEP_AS_NON_CORE (2)**: `GO:0034224` cellular response to zinc ion starvation
  (IMP, IGI) — a real phenotype, but downstream of the molecular function.
- **REMOVE: none.** No transcription-factor or DNA-binding term appears anywhere in
  `ZNG1-goa.tsv`, so there was nothing of that kind to remove.
- **Proposed new terms: none.** `GO:0140827` was already present in GOA (IBA and
  IDA) and was accepted, not added; `proposed_new_terms` is empty.
- Single `core_functions` molecular function: `GO:0140827` zinc chaperone activity.

## Experimental Evidence
- The core experimental evidence for yeast Zng1p (GTP-dependent zinc transfer to
  apo-Map1p, GTP-hydrolysis dependence, Zn-deficiency growth/genetic-interaction
  phenotypes) is PMID:35584675 [Pasquini et al., "Zng1 is a GTP-dependent zinc
  transferase needed for activation of methionine aminopeptidase"], already cited
  throughout `ZNG1-ai-review.yaml`.
- See Update 2026-09-02 below: four previously listed PMIDs in this section
  (31992591, 29695862, 23595998, 26369868) were checked against PubMed and found
  to be unrelated papers (glycine riboswitch structure, acupuncture analgesia
  mechanism, an E. coli nitrile reductase enzyme-engineering study, and a growth
  hormone receptor antibody study, respectively). They did not describe COG0523,
  ZNG1, zinc chaperones, or Map1/MetAP1, and have been removed as incorrect
  citations. None of them were used as `original_reference_id` or
  `supported_by.reference_id` anywhere in the ai-review.yaml, so no annotation
  action changes as a result of this correction.

## Bioinformatics Analysis

**None was performed for this review.** There is no `genes/yeast/ZNG1/ZNG1-bioinformatics/`
folder, no script and no `RESULTS.md`. The domain/family statements under "Family
placement" above come from the InterPro assignments recorded in
`ZNG1-deep-research-falcon.md`, not from any analysis run here.

If a family-wide misannotation survey is wanted, it needs to be done properly under
`ZNG1-bioinformatics/` with a reproducible script, per CLAUDE.md ("Never hardcode the
results of the script... Never ever make up results").

## Remaining Questions
- How specific is zinc vs cobalt delivery?
- What determines target metalloprotein specificity?
- Can we engineer metal selectivity?
- Are there other misannotated GTPase families?

## Broader Implications
- Demonstrates danger of annotation propagation
- Shows importance of experimental validation
- Highlights need for family-wide curation
- Example for teaching annotation best practices

## Update 2026-09-02

Audited this file as part of a batch oversight review. `ZNG1-ai-review.yaml`
itself (existing_annotations, core_functions, description) is well-supported:
its cited PMIDs (35584675, 14562095, 16429126, 19536198) all resolve to the
correct papers and every `supporting_text` verified as a verbatim substring of
the cached publication (confirmed via
`ai-gene-review validate --verbose --terms` and `validate-goa`, both pass with
no changes). No action changes were made to any GO annotation.

The previous "Experimental Evidence" section of this notes file, however,
listed four PMIDs (31992591, 29695862, 23595998, 26369868) that do not
correspond to the claims made next to them. Direct lookup confirms:
- PMID:31992591 = "The asymmetry and cooperativity of tandem glycine
  riboswitch aptamers" (Torgerson et al., RNA, 2020) — glycine riboswitch
  structural biology, unrelated to ZNG1/COG0523.
- PMID:29695862 = "Critical roles of TRPV2 channels, histamine H1 and
  adenosine A1 receptors in the initiation of acupoint signals for
  acupuncture analgesia" (Sci Rep, 2018) — acupuncture pharmacology,
  unrelated.
- PMID:23595998 = "Targeting the substrate binding site of E. coli nitrile
  reductase QueF by modeling, substrate and enzyme engineering" (Wilding et
  al., Chemistry, 2013) — a QueF nitrile reductase enzyme-engineering study,
  unrelated.
- PMID:26369868 = an anti-idiotypic-antibody growth-hormone-receptor
  antagonist study — unrelated.

These citations were fabricated/mis-attributed and have been removed (see the
"Experimental Evidence" section above) per the project rule to never fabricate
identifiers or provenance. They were not used anywhere in the ai-review.yaml,
so this is a notes-file-only correction with no effect on any curated
annotation action.
## Update 2026-09-06

Follow-up to the PR review on #2947, completing the cleanup that the 2026-09-02
pass started. The 2026-09-02 commit removed the four fabricated PMIDs from the
"Experimental Evidence" section but left three further problems in this file, all
of which are fixed here:

1. **`## GO Annotation Review` described work that was never done.** It claimed
   *"Removed: All transcription factor annotations"* and *"Added: GO:0140827"*.
   Neither is true: `ZNG1-goa.tsv` contains no transcription-factor or DNA-binding
   term, `ZNG1-ai-review.yaml` contains zero `REMOVE` actions (18 entries: 11
   ACCEPT, 3 MARK_AS_OVER_ANNOTATED, 2 MODIFY, 2 KEEP_AS_NON_CORE), `GO:0140827`
   is already in GOA twice (IBA + IDA) and was accepted rather than added, and
   `proposed_new_terms` is empty. The section now enumerates the actions the YAML
   actually records.

2. **`## Bioinformatics Analysis` asserted a result that does not exist.** The
   claim *"BLAST revealed >1000 misannotated COG0523 proteins"* had no
   `ZNG1-bioinformatics/` folder, no script and no citation behind it — the same
   class of fabrication as the four PMIDs. Removed and replaced with an explicit
   statement that no analysis was run.

3. **The COG0523 subfamily list and the "misannotation problem" framing were
   uncited and partly wrong.** *"YciC subfamily: Iron-sulfur cluster assembly"*
   and *"ZigA/YeaZ subfamily"* were incorrect (YeaZ is TsaB, a t6A
   tRNA-modification protein, not a COG0523 member), and *"Widespread error
   affects hundreds of genome annotations"*, the `## Impact of Correction`
   section, and the `## Colleague Question` header were unsourced boilerplate
   that had never been reconciled against this gene. All removed in favour of the
   family placement that the deep-research file and UniProt actually support.

Also corrected the metal-binding motif from `CxxC` to **`CXCC`**, which is what
UniProt P53729 annotates (`ZNG1-uniprot.txt:71,160`).

`ZNG1-ai-review.yaml` is again untouched by this commit; the only other change is
the regenerated `ZNG1-ai-review.html`, which had been publishing the four
fabricated PMIDs as live PubMed links because `generate-pages.yaml` triggers only
on `genes/**/*.yaml` and so never re-renders on a notes-only change.
