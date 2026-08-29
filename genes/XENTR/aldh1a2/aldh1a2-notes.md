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
