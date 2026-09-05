# aldh1a2 (XENTR, Q28CC8) — curation notes

## Re-review (2026-08-29)

Triggered by a validation warning that `existing_annotations[1]` (GO:0006081, IBA)
carried `action: MODIFY` without structured `propagation_review`. Investigating the
propagation showed the action itself was wrong, not merely under-documented.

### IBA source tracing

Both IBA rows were traced through the GOA `WITH/FROM` column and every source
identifier was resolved against UniProt / the GO API (no identifiers were guessed):

**GO:0004029 (aldehyde dehydrogenase (NAD+) activity), node PANTHER:PTN000192421**
- UniProtKB:P00352 = human ALDH1A1; P05091 = human ALDH2 (mitochondrial);
  P08157 = *Emericella nidulans* aldA; P17445 = *E. coli* betaine aldehyde
  dehydrogenase BetB; P48644 = bovine ALDH1A1; P49189 = human ALDH9A1;
  Q43274 = maize rf2; Q4WCK7 = *A. fumigatus* ALDH.
- MGI:1340024 = mouse Aldh1l1; MGI:1353450 = mouse Aldh1a1; MGI:1861722 = mouse Aldh1a3.
- RGD:2087 = rat Aldh1a1; RGD:68409 = rat Aldh9a1; RGD:69219 = rat Aldh2.
  (RGD:620252 did not resolve through the GO API and was not asserted.)
- SGD:S000000875 = ALD5; SGD:S000005901 = ALD4. FB:FBgn0012036 = *Drosophila* Aldh.

This is a deep, pan-eukaryotic ALDH node spanning bacteria, fungi, plants and
animals. The only activity shared across those seeds is generic NAD+-dependent
aldehyde oxidation, so the node could not have carried a retinal-specific term.

**GO:0006081 (aldehyde metabolic process), node PANTHER:PTN002619055**
- MGI:MGI:107928 = mouse **Aldh1a2** — i.e. the direct one-to-one ortholog of the
  target is itself a seed.
- UniProtKB:P47895 = human ALDH1A3 (RALDH3), the closest characterized paralog.
- UniProtKB:P05091 = human ALDH2, RGD:69219 = rat Aldh2, FB:FBgn0012036 = *Drosophila* Aldh.

Because ALDH2 and *Drosophila* Aldh are not retinaldehyde dehydrogenases, a
retinoid-specific process term (GO:0002138) is **not** assertable at this node.
The IBA is correctly conservative, not mis-scoped, so `MODIFY` → `KEEP_AS_NON_CORE`
with `propagation_review.root_cause: NO_FAILURE_NON_CORE` and
`failure_modes: [GRANULARITY_MISMATCH]`. The specific process is proposed
separately as a `NEW` annotation grounded in primary literature.

### Ontology check that changed two more actions

QuickGO `is_a` ancestors of GO:0001758 are GO:0004029, GO:0016620, GO:0016491,
GO:0004030, GO:0016903, GO:0003824, GO:0003674. The two IEA rows previously
marked `REMOVE` (GO:0016491, GO:0016620) are therefore **true ancestors** of the
accepted core molecular function. Removing a correct ancestor is not warranted;
both became `KEEP_AS_NON_CORE`. GO:0004029 (IBA) also had contradictory
`proposed_replacement_terms` alongside `KEEP_AS_NON_CORE`; those were dropped.

### Supporting-text integrity

30 of 31 `supporting_text` strings in the previous version were paraphrases, not
verbatim quotes — including all `file:...deep-research.md` citations and three
`PMID:11688558` citations that quoted only the paper's **title** (a hindbrain
paper) as support for limb development and A/P patterning. All were replaced with
strings verified verbatim against the cached sources. Post-edit check: 33/33
verbatim.

Primary quotes now used (all verified against `publications/`):
- PMID:10570467 (full text cached) — Raldh2 mRNA injection into *Xenopus* embryos
  drives high-level RA synthesis; the direct enzymatic-activity support.
- PMID:11688558 (abstract only) — *neckless* inactivates RALDH2; A/P truncation,
  absent pectoral fins, delayed/reduced hoxb4 and RARα, RA rescue,
  non-cell-autonomous mesoderm→neural-tube signalling.
- PMID:16774994 (abstract only) — RA permissive for pectoral fin induction at the
  6–8 somite stage; somite-derived RA required *and* sufficient. Now cited (it was
  previously listed in `references` but never used) and is the proper support for
  GO:0060173.
- PMID:35372345 (full text cached) — the only *Xenopus* paper here that assays
  aldh1a2 directly; organizer→trunk expression.

### Annotations removed (previously `NEW`, now dropped)

- **GO:0001757 somite specification** — the only available evidence was
  *expression* in/around paraxial mesoderm and somites (PMID:10570467 mouse
  immunostaining; deep research). Expression in a tissue does not support a
  "specification" process term. Dropped rather than downgraded; also removed from
  `core_functions`.
- **GO:0042573 retinoic acid metabolic process** — the direct parent of
  GO:0002138, which is already proposed. Proposing both is redundant
  over-annotation; kept only the informative child.

### Other changes

- `evidence_type` on four proposals was `IEA` with no reference (auto-generated
  "identified from core_functions analysis" stubs). Changed to `ISS` with real
  reference ids, and the placeholder summaries/reasons were rewritten.
- `description`: removed the adult immune-regulation / tissue-homeostasis claim,
  which is mammalian (gut dendritic cells) and sourced in the deep research only
  to Wikipedia, with nothing for *Xenopus*. Added the *Xenopus*-specific
  expression trajectory and corrected the protein length to 511 aa (UniProt
  Q28CC8; the deep research says "~519").
- Added `reference_review` blocks recording what was and was not verifiable.

### Known weaknesses left in place

- **GO:0003007 heart morphogenesis and GO:0030324 lung development** rest on
  `PMC:PMC8555986` (Rankin et al., Tbx5/RA cardiopulmonary program), which is
  cited by PMC id only and is **not** in `publications/`. The biology is
  *Xenopus*-specific and plausible, so the entries were kept, but their `reason`
  fields now state explicitly that the support is deep-research text rather than
  a quotation from the paper, and the reference is marked `UNVERIFIED`. Fetching
  this paper is the highest-value next step.
- All three `core_functions` share the same `molecular_function` (GO:0001758).
  This is accurate — the gene has one activity deployed in several contexts —
  but it means the second and third entries are really process/context
  groupings rather than distinct activities.
- The developmental BP proposals (hindbrain, neural tube, limb, heart, lung) are
  all downstream of a single diffusible product. They are conventionally
  annotated for Aldh1a2 in other vertebrates and are kept, but none is treated as
  a core molecular function.
- PMID:35372345 shows aldh1a3, *not* aldh1a2, is the enzyme required for head
  formation in *Xenopus*. Recorded in its `reference_review` so the paper is not
  later mined for head/brain-morphogenesis annotations on this gene.
- `PMC:PMC2826194` remains listed in `references` but is cited by nothing.
- `aldh1a2-pathway.md` still contains the same non-verbatim deep-research
  paraphrases and an "Adult Tissue Homeostasis and Immune Function" section that
  the review no longer asserts. Left untouched as it is outside the scope of this
  annotation re-review.

## Family-level pass (2026-08-31): PTHR11699 FamilyReview + machine-checkable residue claims

Second IBA-curation pass using the FamilyReview framework (PR #2757). Created
`interpro/panther/PTHR11699/PTHR11699-review.yaml` (structured; the free-text
`PTHR11699-review.md` remains as the legacy Falcon integration, with which the
structured review agrees: no family-wide GO mapping is safe) and upgraded both
IBA `propagation_review` blocks here to cite it.

### Node assessments (both SOUND)

- **PANTHER:PTN000192666 → GO:0004029** (paint snapshot 20260828). Deep
  pan-kingdom node; 33 seeds copied verbatim from `PTHR11699-paint.tsv`
  spanning bacteria (*E. coli* betB), fungi (*A. nidulans* aldA, yeast
  ALD4/ALD5), *Drosophila* Aldh, and mammalian ALDH1A/2/9A1/1L1 members —
  generic NAD+-dependent aldehyde oxidation is the only assertable shared
  activity, so the generic term is the *correct* call, and the target's own
  ortholog group (human ALDH1A2 O94788, mouse Aldh1a2 MGI:107928) is among
  the seeds. **Node-id discrepancy documented**: the GOA row (20250411) cites
  `PANTHER:PTN000192421` in WITH/FROM; that id is absent from the current
  paint slice, whose GO:0004029 IBD sits at PTN000192666 with an essentially
  matching, expanded seed list — read as a PANTHER re-release renumbering,
  recorded in both files rather than silently swapped.
- **PANTHER:PTN002619055 → GO:0046185** (paint snapshot 20260409, Eumetazoa,
  seed human ALDH2). The GOA row (20250320) still shows this node asserting
  GO:0006081 seeded by mouse Aldh1a2 + human ALDH1A3 + human/rat ALDH2 +
  *Drosophila* Aldh. Conservative-but-correct under either version (the clade
  mixes retinaldehyde-specific and non-retinoid members, so GO:0002138 is not
  assertable at the node) — confirms the 2026-08-29 KEEP_AS_NON_CORE call.
  The second GO:0004029 IBD at PTN000192422 (seeds human ALDH7A1 P49419 +
  AT5G62530, i.e. the ALDH7 branch) does not back this gene's IBA and was
  deliberately not assessed.

### Residue verification (all positions checked against real sequences)

Fetched live UniProt records on 2026-08-31 and verified feature-table
positions against the actual sequences, then mapped to the target by ad hoc
pairwise alignment (biopython, blastp scoring) against three anchors —
identical correspondences from all three:

| protein | general-base Glu | catalytic Cys | context |
|---|---|---|---|
| human ALDH1A2 O94788 (SV3, anchor) | E286 (ACT_SITE Proton acceptor) | C320 (ACT_SITE Nucleophile) | LKRVTL[E]LGGKSP / FNQGQC[C] |
| human ALDH2 P05091 (SV2) | E285 | C319 | identical blocks |
| human ALDH1A1 P00352 (SV2) | E269 | C303 | identical blocks |
| **XENTR aldh1a2 Q28CC8 (SV1, target)** | **E279** | **C313** | identical blocks |

Recorded as two family `residue_sites` (`catalytic_cys`, `general_base_glu`,
anchored on O94788 with P05091/P00352 as independent positive controls) and
two `RETAINED` residue claims on the GO:0004029 row (`site_ref`
`PANTHER:PTHR11699#catalytic_cys` / `#general_base_glu`). The BP row carries
`residue_claims_not_applicable` (granularity judgment, not a residue question).

**Error found and fixed**: the previous review reason said the frog protein
retains "the catalytic cysteine (PROSITE ALDEHYDE_DEHYDR_CYS, active site
Cys279)". Position 279 of Q28CC8 is the general-base **glutamate** (the
record's single ACT_SITE feature is evidenced by PROSITE-ProRule PRU10007,
the Glu rule); the catalytic cysteine is at 313. The conclusion (no catalytic
loss) survives; the stated mechanism was wrong — exactly the failure class
the residue-claim machinery exists to catch.

### Honest omissions

- **ALDH16A1 (Q8IZ83)** carries the UniProt CAUTION "The active site cysteine
  and glutamate residues are not conserved in this protein. Its activity is
  therefore unsure." — the family's documented degenerate member. Global and
  local alignments to O94788 both fail to map its active-site region
  confidently (4/21 window identity at the Glu, Cys unaligned), so it is
  documented in prose only, **not** as a machine-checkable negative control.
  Consequently both `required_for` strengths are held at CONTRIBUTES (REQUIRED
  demands positive *and* negative controls, rightly).
- **Subfamily ids**: only SF102 (RETINAL DEHYDROGENASE 2) is anchored by a
  locally indexed member (O94788 per `panther-members.tsv`). Q28CC8's own
  UniProt record carries a family-level PANTHER xref only, so the target's SF
  is not asserted; SF209/SF140/SF303 grants in the GO:0001758 term assessment
  rest on PANTHER's official subfamily names (stated explicitly in the
  scope_reason). Two SFs share the official name RETINAL DEHYDROGENASE 2
  (SF102, SF303).
- Q28CC8 and P05091/P00352 are not yet in `panther-members.tsv`;
  `just refresh-panther-members` deliberately **not** run (shared file —
  orchestrator runs it once).

### Validation

`just validate-families`: PTHR11699-review.yaml passes all four stages
(schema; GO id/label; residue sites vs UniProt sequences — 0 fail; family/gene
cross-check — 0 conflicts; the only UNRESOLVED rows are another family's
membership gaps). `just validate XENTR aldh1a2`: pass (see below).

## PR #2958 review follow-up (2026-09-05)

Changes made in response to the review-bot findings on PR #2958.

### Finding 1 (required): PMC:PMC8555986 resolved, fetched, verified

- Resolved `PMC:PMC8555986` via the NCBI ID converter
  (`pmc.ncbi.nlm.nih.gov/tools/idconv`): **PMID:34643182**, DOI
  10.7554/eLife.69288. Cached with `just fetch-pmid 34643182` →
  `publications/PMID_34643182.md` (full text from PMC,
  `full_text_available: true`).
- The title previously listed in `references` ("Retinoic acid signaling is a
  critical component of the Tbx5 dependent forelimb initiation and
  cardiopulmonary morphogenesis programs") was **wrong for this PMC id**. The
  actual paper is Rankin SA *et al.*, eLife 2021: "Tbx5 drives Aldh1a2
  expression to regulate a RA-Hedgehog-Wnt gene regulatory network
  coordinating cardiopulmonary development." The reference entry was replaced
  (id, verbatim fetched title, `reference_review` → VERIFIED with notes).
- Full text read and it **does** support both Xenopus claims, directly:
  - Tbx5 LOF in both *X. laevis* (MO) and *X. tropicalis* (CRISPR) causes
    "a loss or strong reduction of aldh1a2 transcripts and Aldh1a2 protein in
    the foregut lpm at NF34"; Tbx5 directly maintains aldh1a2 via a conserved
    first-intron enhancer (enh1), whose single perfectly conserved T-box motif
    was functionally tested in the *X. tropicalis* enhancer.
  - **Heart (GO:0003007)**: Aldh1a2-MO and DEAB phenocopy Tbx5 LOF with loss
    of pSHF markers and expansion of aSHF gene expression; exogenous 25 nM RA
    partially rescues Tbx5-MO, Aldh1a2-MO and DEAB phenotypes.
  - **Lung (GO:0030324)**: "Aldh1a2-MO injection or DEAB treatment disrupts
    the RA>Tbx5>Aldh1a2>RA positive feedback loop ... and results in failed
    induction of Nkx2-1+ pulmonary progenitors"; Tbx5/Aldh1a2-dependent RA
    directly activates shh via the MACS1 enhancer, upstream of Wnt2/2b-driven
    pulmonary induction.
- Both NEW rows now cite `original_reference_id: PMID:34643182` with verbatim
  `supporting_text` quotes from the cached full text. The truncated quote
  ("Tbx5 directly binds an intronic enhancer in") was replaced with the
  complete verbatim sentence "Specifically, Tbx5 directly maintains expression
  of Aldh1a2 in pSHF via an evolutionarily conserved intronic enhancer".
  All deep-research-only support on these two rows was removed.
- This closes the "Known weaknesses" item from 2026-08-29 that flagged
  fetching this paper as the highest-value next step.

### Finding 2 (suggestion): parent+child CC redundancy removed

- Dropped the `NEW` proposal for GO:0005737 (cytoplasm); kept the informative
  child GO:0005829 (cytosol) — the same redundancy argument used earlier to
  drop GO:0042573 in favour of GO:0002138. The cytosol row's reason records
  the decision. `core_functions[*].locations` de-duplicated to cytosol only.

### Finding 3 (judgment call): core_functions collapsed to one entry

All three previous entries shared `molecular_function` GO:0001758 and
identical (cytosolic) localization; the 2026-08-29 notes already conceded
that entries 2 and 3 were "process/context groupings rather than distinct
activities". The gene has exactly one catalytic activity deployed from one
compartment; splitting it three ways implied distinct activities that do not
exist. **Collapsed to a single core_function** carrying the full
`directly_involved_in` list (GO:0002138, GO:0009952, GO:0030902, GO:0021915,
GO:0003007, GO:0060173, GO:0030324), with a description that preserves the
spatial-context narrative (organizer → trunk mesoderm; Tbx5-dependent foregut
lpm/pSHF; limb-flanking somites) and a merged, verbatim `supported_by` set
including two PMID:34643182 quotes. This is the more honest structure.

### Validation

`just validate XENTR aldh1a2` → ✓ Valid, all validations passed.
