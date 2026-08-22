# SSA2 review notes

## Identity and core function

- SSA2 is P10592/YLL024C, a constitutively expressed cytosolic Ssa-family Hsp70.
- The best molecular-function summary is GO:0140662, ATP-dependent protein folding
  chaperone. Ssa-class Hsp70s cooperate with Ydj1 to suppress aggregation and use ATP,
  and Ssa1/2 depletion strongly impairs luciferase refolding
  [PMID:7867784; PMID:8947547].
- In-vivo reporter and nascent-enzyme experiments support protein folding/refolding as
  the central biological role [PMID:9448096; PMID:9789005].

## Annotation decisions

- Replaced the obsolete/generic chaperone terms GO:0044183 and GO:0051082 with
  GO:0140662 where the evidence supports ATP-dependent folding chaperone activity.
- Replaced GO:0006616 with GO:0031204. The experimental evidence concerns an Ssa/Ydj1
  contribution to post-translational import of a subset of ER precursors, not
  SRP-dependent cotranslational targeting [PMID:8754838; PMID:8947547].
- Retained nucleus, plasma membrane, vacuolar membrane, cell wall, and mitochondrion as
  non-core localizations. The cell-wall and vacuolar-membrane evidence is directly
  supported [PMID:8755907; PMID:10745074]; the plasma-membrane cache is abstract-only
  and does not name SSA2 [PMID:16622836].
- Marked generic nucleotide binding as over-annotated because ATP binding/hydrolysis and
  ATP-dependent chaperone activity are already represented more informatively.

## Citation correction

- PMID:12761219 concerns *Candida albicans* Ssa1/2 proteins, not *S. cerevisiae* SSA2.
  It is retained in the reference inventory but marked `MISCITED`/`NONE` and is not used
  to support any SSA2 claim.

## Project relevance

- SSA2 is directly relevant to `UNFOLDED_PROTEIN_BINDING`; its row now points to
  GO:0140662 and describes its constitutive cytosolic Hsp70 role.
- No curated module membership was found for SSA2/YLL024C/P10592.

## Focused hypothesis research

- OpenScientist independently supported `KEEP_AS_NON_CORE` for GO:0005886, emphasizing
  that PMID:16622836 used a stripped plasma-membrane fraction and does not establish a
  primary membrane-resident function.
- Its live QuickGO query reported only the HDA row and asserted that no IBA exists. This
  conflicts with the pinned `SSA2-goa.tsv`, which contains both an IBA/GO_REF:0000033 row
  (dated 2025-09-03) and an HDA/PMID:16622836 row. The report also treated the Candida
  histatin paper as SSA2 evidence. The provider report is therefore marked `DISPUTED`;
  its conservative localization judgment is retained, but those database/species claims
  are not propagated into the review.
