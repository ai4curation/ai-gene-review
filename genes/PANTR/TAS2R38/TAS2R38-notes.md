# Curation notes: TAS2R38 (Pan troglodytes, UniProt Q697L5)

## Session: 2026-09-06

Cross-species companion review to `genes/human/TAS2R38/` (reviewed in parallel by a
separate agent). This gene has **no chimpanzee-specific PMIDs seeded from GOA** — all
10 GOA rows are IBA (PAINT phylogenetic inference from the PTHR11394/TAS2R family
node) or IEA (InterPro2GO / ARBA / combined electronic methods). No experimental
(IDA/IPI/etc.) rows exist for chimp TAS2R38 in `TAS2R38-goa.tsv`.

Source used for all literature-derived claims: `TAS2R38-deep-research-falcon.md`
(Falcon/Edison Scientific deep-research report, generated 2026-09-06). Its cited
primary literature is real, correctly attributed, and directly relevant
(chimpanzee-specific population genetics and functional assays), but none of the
underlying PMIDs are cached locally in `publications/`, so this review cites the
deep-research file directly (`file:PANTR/TAS2R38/TAS2R38-deep-research-falcon.md`)
rather than fabricating unverifiable PMID citations. Key primary sources it
synthesizes (not independently fetched/cached here):

- Hayakawa T et al. 2012. "Eco-Geographical Diversification of Bitter Taste Receptor
  Genes (TAS2Rs) among Subspecies of Chimpanzees (Pan troglodytes)." PLoS ONE
  7:e43277. doi:10.1371/journal.pone.0043277 — direct chimpanzee population genetics:
  ATG->AGG start-codon-loss allele at 76% (70/92) in western chimpanzee alleles, 0%
  in eastern/central/Nigeria-Cameroon samples; FST=0.614 west-east differentiation.
- Suzuki-Hashido N et al. 2015. "Rapid expansion of phenylthiocarbamide non-tasters
  among Japanese macaques." PLoS ONE 10:e0132016. doi:10.1371/journal.pone.0132016 —
  contains the heterologous (HEK293T + Gα16gust44 + Fluo-4 calcium imaging) functional
  assay framework applied to chimpanzee TAS2R38 start-loss vs rescued constructs.
- Wooding S et al. 2006. "Independent evolution of bitter-taste sensitivity in humans
  and chimpanzees." Nature 440:930-934. doi:10.1038/nature04655 — establishes that
  PTC-tasting was ancestral and reduced sensitivity arose independently by different
  mutations in the human and chimpanzee lineages after ~5-6 Mya divergence.
- Campbell MC et al. 2012. Mol Biol Evol 29:1141-53. doi:10.1093/molbev/msr293 —
  corroborates independent human/chimp evolutionary origins of PTC insensitivity.
- Meyerhof W et al. 2011. Flavour Fragr J 26:260-268. doi:10.1002/ffj.2041 — general
  mammalian T2R/gustducin/PLCβ2/IP3R3/TRPM5 signaling review used for the canonical
  pathway description.
- Itoigawa A, Nakagita T, Toda Y. 2024. Int J Mol Sci 25:12654.
  doi:10.3390/ijms252312654 — recent (Nov 2024) review of vertebrate T2R structural
  class and diversity; confirms no newer chimp-TAS2R38-specific localization/structure
  data exists beyond the 2012/2015 chimpanzee-specific studies.
- Purba LHPS et al. 2020. Primates 61:485-494. doi:10.1007/s10329-020-00799-1 —
  comparative colobine TAS2R38 evolution, used only as general candidate-ligand
  context (sinigrin, allyl isothiocyanate, goitrin).

## GO term hierarchy checks (via QuickGO API, 2026-09-06)

Verified before assigning ACCEPT/KEEP_AS_NON_CORE, per the project's term-id
validation guidance (existing_annotations ids are trusted/not hard-validated, but
hierarchy claims made in `review.reason` should be checked, not asserted from
memory):

- GO:0001580 ("detection of chemical stimulus involved in sensory perception of
  bitter taste") ancestors include GO:0050912, GO:0050913, GO:0050909 — i.e.
  GO:0050909 ("sensory perception of taste") IS a formal ancestor/generalization of
  GO:0001580. Confirms the GO:0050909 IEA row is a correct-but-generic restatement,
  used to justify KEEP_AS_NON_CORE (not REMOVE — it's true, just uninformative).
- GO:0033038 ("bitter taste receptor activity") ancestors do NOT include GO:0004930
  ("G protein-coupled receptor activity") — the two terms are formally unrelated
  siblings in the MF DAG (GO:0033038 sits under "taste receptor activity" ->
  "transmembrane signaling receptor activity", not under the GPCR-activity branch).
  So the GO:0004930 IEA row is not formally redundant with GO:0033038, but it is
  still far less informative for this specific, well-characterized receptor —
  KEEP_AS_NON_CORE on informativeness grounds, consistent with the project's
  guidance to prefer specific/informative MF terms.
- GO:0016020 ("membrane") is a formal ancestor of GO:0005886 ("plasma membrane") —
  confirms KEEP_AS_NON_CORE for both membrane rows as strictly subsumed by the
  plasma-membrane annotation.
- GO:0007186 ("G protein-coupled receptor signaling pathway") is NOT a formal
  ancestor/descendant of GO:0001580 (they sit on different BP sub-branches:
  signal-transduction vs. sensory-perception) — so it is not simply redundant, but
  it is a generic pan-GPCR term; kept as KEEP_AS_NON_CORE since GO:0001580 is the
  more informative, taste-specific process annotation, and no taste-receptor-specific
  child of GO:0007186 exists in the current ontology (checked via QuickGO search —
  the only taste-specific MF/BP/CC terms found were GO:0033038, GO:0090682 (GPCR
  bitter taste receptor activity), GO:0170022 (ionotropic bitter taste receptor
  activity), GO:0050913 (sensory perception of bitter taste), GO:1904660/1/2
  (regulation of ...), GO:0031883 (taste receptor binding), GO:1903768 (taste
  receptor complex), GO:0008527 (taste receptor activity) — none of these is a
  bitter-taste-specific signaling-pathway BP term).

### Note on GO:0090682 ("GPCR bitter taste receptor activity")

This term exists (not obsolete) and is formally a more specific descendant of BOTH
GO:0033038 (bitter taste receptor activity) and GO:0004930 (GPCR activity) — i.e. it
is exactly the intersection term that would most precisely describe TAS2R38, which is
unambiguously a GPCR-type (not ionotropic) bitter taste receptor. However, GO:0033038
is the term consistently used by GO_Central/PAINT across the entire TAS2R gene family
(confirmed in both the human and chimp GOA files, and in TAS2R16's GOA file), so this
review does not MODIFY the existing GO:0033038 annotations to GO:0090682 — that would
create an inconsistency with the rest of the family's curation and is better raised as
a broader ontology-curation question (e.g. whether GO_Central should adopt GO:0090682
for the whole GPCR-type T2R subfamily) rather than a single-gene MODIFY call. Noted
here for future reference / potential cross-gene follow-up.

## Curation outcome summary

All 10 existing_annotations rows: 5x ACCEPT (core BP GO:0001580 x2, core MF
GO:0033038 x2, core CC GO:0005886), 5x KEEP_AS_NON_CORE (generic/subsumed terms:
GO:0004930, GO:0007186, GO:0016020 x2, GO:0050909). No REMOVE, MODIFY, or UNDECIDED
calls — the IBA/IEA evidence base for this gene is standard, biologically coherent
family-level TAS2R annotation, and is independently and strongly corroborated by
chimpanzee-specific population genetics and functional (heterologous calcium-imaging)
literature on PTC/thiocarbamide bitter-taste detection [Hayakawa 2012; Suzuki-Hashido
2015 — see TAS2R38-deep-research-falcon.md]. No experimental annotations exist to
second-guess, so the "do not overrule curators from incomplete evidence" caveat did
not come into play here.

The most biologically interesting finding for this species — the western-chimpanzee
ATG->AGG start-codon-loss non-taster allele, independently evolved from the human
PAV/AVI polymorphism — is not itself a GOA annotation target (it's an allelic/
population-variation fact, not a distinct molecular function) and so is captured in
`description` and `knowledge_gaps` rather than as a new proposed GO term.
