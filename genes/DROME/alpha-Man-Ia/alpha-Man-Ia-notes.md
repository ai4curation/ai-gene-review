# alpha-Man-Ia (P53624) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

I did not consult the ProtNLM2 predictions or any prediction-evidence files.

### Identity
- P53624 (MA1A1_DROME) is the reviewed, canonical UniProt entry for alpha-Man-Ia/mas-1/CG32684 (FBgn0259170).
  It is 667 aa, displayed isoform H (synonym A). Isoform K (synonym B; P53625 merged as P53624-2) differs only in
  its N-terminus, from an alternative promoter (VSP_057904). The benchmark accession is the canonical full-length product,
  not a fragment or alternative gene model. Its features are a TM segment at 19-39 (type II topology) and the full GH47 domain (PF01532).
- Do not confuse this gene with alpha-Man-Ib (CG42275/Q9VAP8, ER-type SF55), alpha-Man-Ic (Q8IMK0, SF6 paralog), or the GH38 class II enzymes.

### Phylogenetic placement
- PANTHER 19.0 reference-genome classification puts alpha-Man-Ia in PTHR11742:SF6 ("IA-related"), together with
  alpha-Man-Ic (fly), mans-1 (C. elegans P90787), MNS1 (Arabidopsis Q9C512, AT1G51590), POPTR_008G007500
  and five Dictyostelium paralogs. The vertebrate Golgi class I enzymes form separate subfamilies:
  MAN1A1 SF31, MAN1A2 SF40, MAN1C1 SF28. The ER enzymes MAN1B1 and yeast MNS1 are in SF55.
- PAINT nodes: PTN000201533 (GH47 root) carries GO:0004571, GO:0005783 (ER; seeds all ER-branch) and GO:0036503 (ERAD; seeds
  ER branch plus human MAN1A1). PTN000201534 (Golgi class I clade, seeds AT1G51590, AT3G21160, Man1a1, Man1a2) carries GO:0000139.
- The family review interpro/panther/PTHR11742/PTHR11742-review.yaml lists SF6 with alpha-Man-Ia as representative. I found no
  disagreement about subfamily placement. It has no term assessments, so it raises no family/gene conflict.

### Evidence (abstract-only caches)
- PMID:7729592: two promoters, type II TM isoforms, null mutants with low-penetrance PNS/wing/eye defects, redundancy.
- PMID:9654102: null flies make the same range of N-glycans in different ratios, with Man8GlcNAc2 accumulating.
- PMID:23979800: recombinant mas-1 (Pichia) is active on oligomannosidic glycans.
- PMID:19317464: embryo LOPIT places the protein in the endomembrane system.

### Changes from the previous version
- ER IBA: REMOVE -> MARK_AS_OVER_ANNOTATED. The ER assertion is correct for the ER-branch seeds and was placed too deep for
  cellular component. No fly data contradict transient ER presence, so this is over-propagation, not a false claim.
- membrane (IEA) and endomembrane system (HDA): KEEP_AS_NON_CORE -> MODIFY to Golgi membrane, following the rule that a correct but
  general term is refined.
- ERAD IBA: stays UNDECIDED. The PAINT curator deliberately included a Golgi IA enzyme (MAN1A1) among the seeds, but there is no fly test,
  the fly enzyme is in a different subfamily (SF6) from that seed, and I could not read the MAN1A1 ERAD evidence.
- Description rewritten. I added reference_review blocks, suggested questions and experiments, and set status to COMPLETE.
- I did not annotate the developmental phenotypes (PNS, wing, eye) as processes; they are downstream effects of loss of glycan processing.

### Relative to review next
- The closest characterised relative in the same PANTHER subfamily (SF6) is Arabidopsis MNS1 (Q9C512, AT1G51590), a
  Golgi class I alpha-mannosidase with experimental evidence that seeds both PAINT nodes. There is no review in the repo (no genes/ARATH/MNS1).
- Module: modules/dmel_n_glycan_processing.yaml (annoton golgi_mannosidase_i_alpha_man_ia), consistent with this review.
