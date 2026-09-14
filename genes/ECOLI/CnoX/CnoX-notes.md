# CnoX review notes

## 2026-08-30

- Refreshed the UniProt and GOA snapshots with `just fetch-gene ECOLI CnoX --force`.
  The live GOA contains 10 rows. The prior review had three stale rows
  (GO:0006950, GO:0036506, and obsolete GO:0051082) and lacked the second
  PMID:15690043 protein-interaction row.
- The current GO:0045454 IBA traces to PTN001625774 with descendant evidence
  AGI_LocusCode:AT2G15570 and UniProtKB:O53161. The fetched PAINT table retains
  this exact node assertion, so the review accepts the IBA rather than treating
  its short donor list as weak evidence.
- CnoX is an HOCl-activated holdase that protects clients from aggregation and
  irreversible oxidation [PMID:29754824, "functions as an efficient holdase,
  protecting the substrates of the major folding systems GroEL/ES and
  DnaK/J/GrpE"].
- The later structural study establishes a stable GroEL-CnoX complex outside
  GroEL's substrate-binding site and GroES-triggered CnoX release
  [PMID:36764293, "Binding of GroES (Hsp10 cofactor) to GroEL induces CnoX
  release."].
- Removed GO:0140597 from the authored core function. General in-situ holdase
  activity does not by itself establish carrier-like movement to an acceptor or
  location. Added the shared project NTR proposal for `holdase chaperone activity`.
- Kept both PMID:15690043 high-throughput interaction rows `UNDECIDED` because
  the local record is abstract-only and the combined partner sets do not support
  one common informative replacement. For PMID:18657513 and PMID:21498507,
  proposed GO:0051087 only for the explicitly demonstrated DnaK/GroEL interactions;
  the source rows need splitting so non-chaperone partners are not recast.

## 2026-08-31 PR review follow-up

- Reclassified the GO:0045454 IBA as `KEEP_AS_NON_CORE`. CnoX directly protects
  client thiols, but its deletion leaves bulk cellular protein redox state normal
  [PMID:18657513, "not to oxidative stress, a normal redox state of its cellular
  proteins"], so general redox homeostasis is not promoted into the core synthesis.
- Added PMID:21195694 and used its beta-clamp refolding result to adjudicate the
  DnaN row [PMID:21195694, "YbbN functions as a bona fide chaperone in the
  refolding of the urea-unfolded β-clamp"]. The interaction is credible, but the
  current ontology still lacks the appropriate client-directed holdase MF.
- Added pair-specific `NEW` GO:0051087 from the 2023 GroEL-CnoX study and
  `NEW` GO:0009408 from the thermal-sensitivity phenotype.
- Reconciled the mild in-vitro GroEL/GroES inhibition in PMID:21498507 with the
  later GroES-release plugin mechanism. No directional regulatory BP is proposed
  without in-vivo evidence.
