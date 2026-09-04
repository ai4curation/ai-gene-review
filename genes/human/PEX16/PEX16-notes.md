# PEX16 curation notes

## 2026-09-04 — PAINT no-IBA project finishing pass (AI-assisted)

First journal entry for this gene. The review already had all actions assigned and a
`core_functions` block; this pass was a critical quality review of the calls themselves.

### Material changes to existing annotations

- **GO:0005515 (IPI, PMID:19114594): MODIFY target corrected.** The draft proposed
  GO:0022615 *protein to membrane docking* as the replacement for a molecular-function
  annotation. That is a biological process term — a branch mismatch that would have
  produced a nonsense MF annotation if acted on. Changed to GO:0060090 *molecular adaptor
  activity*, which is the term already used in `core_functions` and already proposed as a
  NEW annotation from the same paper. GO:0022615 remains correctly annotated separately as
  the process. [PMID:19114594 "we demonstrate that Pex16p functions as the Pex3p-docking
  site and serves as the peroxisomal membrane receptor that is specific to the Pex3p-Pex19p
  complexes"]
- **GO:0005515 (IPI, PMID:14709540 and PMID:15713480): MODIFY → MARK_AS_OVER_ANNOTATED.**
  Both drafts proposed GO:0045046 (a BP term) as an MF replacement — the same branch
  mismatch. In these two rows PEX16 is PEX19's *cargo*: PEX19 recognises PEX16's two mPTS
  regions in the course of chaperoning it. Being recognised by a receptor is not a molecular
  function of the substrate, and there is no GO MF term for it, so MODIFY has no valid
  target and the honest action is over-annotation.
- **GO:0006625 protein targeting to peroxisome (IMP, PMID:9837814): ACCEPT → MODIFY** with
  `proposed_replacement_terms: GO:0045046`. GO:0006625 lumps what PEX16 does (PMP delivery)
  with what merely fails downstream of it (matrix import, whose machinery is
  PEX5/PEX13/PEX14). GO:0045046's definition explicitly separates the two ["The targeting of
  proteins into the peroxisomal membrane. The process is not well understood, but both
  signals and mechanism differ from those involved in peroxisomal matrix protein import."],
  and it is already independently annotated as IMP from PMID:12223482.
- **GO:0016558 protein import into peroxisome matrix (IMP, PMID:9922452):
  MARK_AS_OVER_ANNOTATED → KEEP_AS_NON_CORE.** The draft objected that matrix import is only
  an indirect consequence of PEX16 loss. True, but the GOA row carries the qualifier
  `acts_upstream_of_or_within`, not `involved_in` — the MGI curator had already encoded the
  relation as upstream/indirect, so the annotation is not making the claim being objected
  to. The observed ordering is exactly what that qualifier is for. [PMID:9922452 "Peroxisome
  synthesis and peroxisomal membrane protein import could be detected within 2-3 h of PEX16
  injection and was followed by matrix protein import"]
- **GO:0005829 cytosol ×3 (TAS, Reactome): REMOVE retained, reasoning tightened.** The draft
  said "PEX16 is never found in the cytosol", which is stronger than the evidence and sits
  awkwardly next to PMID:14709540 showing PEX19 binding PEX16 mPTS fragments. The precise
  argument is that the Reactome reactions model PEX16 as a class I PMP with a cytosolic
  PEX19-bound intermediate, and PEX16 does not follow that route: it is inserted
  cotranslationally into the ER and fractionates entirely into the non-soluble fraction.
  [PMID:16717127 "The data thus confirmed that PEX16 undergoes cotranslational insertion
  into the ER"] Note this is a *deliberate divergence* from the sibling PEX13 review, where
  the same Reactome cytosol rows are kept as non-core — PEX13 genuinely is a
  post-translationally inserted class I PMP with PEX19-bound cytosolic intermediates. The
  divergence is now stated explicitly in both reviews so it does not look like an
  inconsistency.

### Deep research

Cited `file:human/PEX16/PEX16-deep-research-falcon.md` on the GO:0060090 NEW annotation and
in `core_functions`. The draft's core-function description already leaned on Lee et al.
(2024) for the PEX16 loop 132–214 / PEX3 interface and the trimer model, but that paper is
not in the GOA record and was not cited as a reference — the deep-research file is the
in-repo source for it. ["The authors propose a **trimeric complex** in which PEX16 anchors
PEX3 at the peroxisomal membrane, while PEX19 binds PEX3 on the opposite face and can
deliver PMPs"]

### Notable

- Like PEX13, PEX16 is on the project's "human no-IBA" list but in fact receives two IBAs
  (GO:0007031, GO:0005778) from PANTHER node PTN000329346, one of them refreshed as recently
  as 2025-09-03. The source spreadsheet row for PEX16 reads "uncharacterized pthr13299 / No
  data found", which is no longer accurate. As with PEX13, the real gap is that PTHR13299
  has **no molecular-function IBD at all**. See
  `interpro/panther/PTHR13299/PTHR13299-review.yaml`.
- Validation is clean (0 errors, 0 warnings); status set to COMPLETE.
