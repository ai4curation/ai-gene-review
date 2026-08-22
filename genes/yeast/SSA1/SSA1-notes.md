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
- Plasma-membrane IBA/HDA annotations are retained conservatively as non-core.
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
- The UNFOLDED_PROTEIN_BINDING project row now uses GO:0140662 for SSA1 and
  describes its constitutive cytosolic Hsp70 role. SSA1 is also part of the
  BIOREASON_COMPARISON benchmark, but that project consumes the review through
  generated benchmark outputs rather than a manually maintained per-gene claim.
