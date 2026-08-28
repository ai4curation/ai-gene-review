# SSA1 review notes

## 2026-08-22 re-review

- Identity was rechecked as *Saccharomyces cerevisiae* SSA1/YAL005C, UniProt
  P10591: the major constitutively expressed cytosolic Ssa-family Hsp70. The
  standalone description was narrowed to the core ATP-dependent chaperone
  mechanism and no longer presents every reported high-throughput localization
  as an equivalent site of function.
- The core molecular function remains ATP-dependent protein folding chaperone
  (GO:0140662), supported by direct Ssa1 ATPase regulation and Ssa1/2 folding
  and refolding experiments. The broader GO:0044183 IBA is modified to this
  mechanistically precise child, and generic nucleotide binding is marked
  over-annotated. [PMID:7737974 "Polypeptide substrates and Ydj1p both serve to
  stimulate ATPase activity of Ssa1p."] [PMID:8947547 "had a dramatic effect on
  the ability of the lysate to refold chemically denatured luciferase"]
- The two GO:0006616 annotations are modified to GO:0031204 because the
  SSA/Ydj1 evidence concerns post-translational precursor import rather than
  SRP-dependent cotranslational targeting. The negative cell-free result from
  PMID:8947547 is retained as a scope limitation. [PMID:8754838 "The processing
  of prepro-alpha-factor was inhibited within 2 min ... suggesting a direct
  effect ... on translocation."]
- Nuclear, vacuolar-membrane, and cell-wall localizations are retained as
  non-core because they have experimental support but are secondary to the
  predominant cytosolic chaperone function. The cell-wall evidence includes
  intact-cell immunofluorescence and extracellular biotinylation; the
  vacuolar-membrane evidence is tied to Ape1 transport. [PMID:8755907 "A cell
  wall location was further confirmed by indirect immunofluorescence with
  intact cells and biotinylation of extracellular Hsp70."] [PMID:10745074
  "Ssa1/2p was prominently localized to the vacuolar membrane"]
- The plasma-membrane IBA and HDA rows are now separated by evidence source.
  The pinned IBA cites PTN002500132, but the current local PTHR19375 PAINT
  snapshot has nucleus and cytosol at that node and no GO:0005886; the IBA is
  therefore removed as `SOURCE_STALE_OR_MISSING`, based on node content rather
  than donor count. The HDA is retained conservatively as non-core.
  The cached PMID:16622836 record is abstract-only and confirms a stripped
  plasma-membrane proteomics workflow but does not itself name Ssa1, so the
  citation is marked UNVERIFIED rather than used to claim a primary functional
  localization. A targeted OpenScientist run independently concluded that
  non-core retention is defensible because the experiment is bulk
  co-purification rather than a demonstrated functional site. Its live QuickGO
  claim that P10591 has no plasma-membrane IBA conflicts with the pinned SSA1
  GOA snapshot, which still contains GO:0005886 IBA from GO_Central dated
  2025-09-03. That claim is marked DISPUTED and is not used to alter the source
  evidence code. [file:yeast/SSA1/SSA1-hypotheses/existing-go-0005886-keep-as-non-core/openscientist.md
  "treating plasma membrane as non-core is the correct handling of the evidence
  weight"]
- The inherited review collapsed 242 pinned GOA rows to 70 review records,
  chiefly by representing eight high-throughput IPI datasets once each. The
  2026-08-27 audit expands every repeated dataset row with its exact WITH/FROM
  identifier and removes a redundant `NEW` pseudo-row from
  `existing_annotations`; the review now reconciles exactly 242/242.
- A stricter post-rebase audit also confirmed one-to-one WITH/FROM provenance
  for every IPI row after adding the exact pinned accession to ten singleton
  review summaries.
- PR review follow-up separated two targeted Ssa1-Sse1 biochemical/structural
  studies from bulk interaction screens: the former support refinement of
  generic protein binding to heat shock protein binding, whereas partner
  identity alone does not. The GO:0031072 IBA rationale is now anchored to
  PAINT node PTN000452648 and those targeted studies rather than to discounted
  high-throughput IPI rows. [PMID:16688211 "that the yeast homologue, Sse1p,
  acts as an efficient nucleotide exchange factor"] [PMID:18555782 "Here we
  present the crystal structure of the yeast NEF Sse1p (Hsp110) in complex with
  the nucleotide-binding domain (NBD) of Hsp70."]
- The UNFOLDED_PROTEIN_BINDING project row now uses GO:0140662 for SSA1 and
  describes its constitutive cytosolic Hsp70 role. SSA1 is also part of the
  BIOREASON_COMPARISON benchmark, but that project consumes the review through
  generated benchmark outputs rather than a manually maintained per-gene claim.
- Every PMID supporting an experimental, high-throughput, or NAS row now has a
  manual `reference_review`. Dataset papers and abstract-only records are marked
  `UNVERIFIED` whenever the SSA1-specific edge or assay is not visible; direct
  Ssa1 experiments are marked `VERIFIED` only when the cached text exposes the
  relevant evidence. With the exact 242-row reconciliation and all actions
  resolved, the review is promoted to `COMPLETE`.
