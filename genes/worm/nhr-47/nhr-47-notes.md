# nhr-47 (C. elegans) — research notes

Gene: **nhr-47** / sequence name **C24G6.4** / WormBase **WBGene00003637** / UniProt **Q17370** (NHR47_CAEEL).
Locus: Chromosome V. Protein: 579 aa nuclear hormone receptor.

## Provenance conventions
Inline provenance uses `[PMID:xxxxx "verbatim quote"]`. WormBase/Alliance-curated statements
(no direct primary PMID to hand) are marked `[WormBase/AGR]` and are NOT used as verbatim
`supporting_text` in the review; only cached-publication PMID quotes are used for that.

## Summary: nhr-47 is a "dark" HNF4-derived orphan nuclear receptor
nhr-47 is one of the ~280 nuclear hormone receptors (NHRs) of C. elegans, the great majority of
which arose by a nematode-specific expansion of an ancestral HNF4-like orphan receptor and remain
functionally uncharacterized ("supplementary nuclear receptors", supnrs)
[PMID:15983867 "the supplementary\nnuclear receptors (supnrs) originated from an explosive burst of duplications of\na unique orphan receptor, HNF4"]. Its DNA-binding domain is HNF4-like (CDD cd06960 NR_DBD_HNF4A;
InterPro IPR049636 HNF4-like_DBD).

## Molecular architecture (KNOWN, from sequence/UniProt Q17370)
- Two C4-type (Cys4) zinc-finger motifs (ZN_FING 11–31 and 47–71) forming a canonical nuclear-receptor
  DNA-binding domain (DNA_BIND 8–83). Coordinates zinc (KW Metal-binding, Zinc, Zinc-finger).
- A nuclear-receptor ligand-binding domain (NR LBD, residues 164–553; PROSITE PS51843).
- UniProt FUNCTION: "Orphan nuclear receptor." SUBCELLULAR LOCATION: Nucleus.
- Documented physical interaction (IntAct EBI-2412077/EBI-2412071): Q17370 (nhr-47) <-> Q17589 (nhr-17),
  NbExp=3. nhr-17 is itself another nuclear hormone receptor.
- Therefore, from sequence + family, nhr-47 is confidently a zinc-finger, sequence-specific
  DNA-binding transcription factor of the nuclear-receptor superfamily that acts in the nucleus.
  (This is what the IBA/IEA GO annotations capture.)

## Expression (KNOWN, curated) [WormBase/AGR]
Alliance/WormBase automated + MOD-provided descriptions for WBGene00003637:
- Expressed in head neurons, tail neurons, ventral nerve cord, spermatheca, intestine, and pharynx.
- "gene expression of nhr-47 appears to be induced upon exposure of worm cultures to estradiol"
  (WormBase MOD-provided gene description; primary microarray reference not located in cache — recorded
  here as curated context only, not used as review supporting_text).

## Functional data (the only experimental phenotypes reported for nhr-47)
Two toxicology studies from one group (Southeast University / Dayong Wang lab) are the only primary
papers that assign nhr-47 a phenotype, both in the **germline** and in an **environmental-toxicant**
context:

1. Nanoplastics, transgenerational toxicity [PMID:38922100]:
   - nhr-47 is one of only 4 of 33 germline-expressed NHRs whose expression responds to polystyrene
     nanoparticles; it is UP-regulated
     [PMID:38922100 "the expressions of nhr-14, nhr-47, and daf-12 were significantly increased by exposure to 10 μg/L of PS-NPs"].
   - Germline RNAi of nhr-47 makes animals RESISTANT to transgenerational nanoplastic toxicity
     [PMID:38922100 "daf-12(RNAi), nhr-14(RNAi), and nhr-47(RNAi) nematodes showed resistance to transgenerational PS-NP toxicity"].
   - Under exposure, nhr-47 RNAi changes downstream secreted-ligand gene expression
     [PMID:38922100 "the RNAi of nhr-47 decreased expressions of germline ins-3, ins-39, daf-28, and efn-3 in PS-NP-exposed animals"]
     (ins-3/ins-39/daf-28 = insulin ligands; efn-3 = Ephrin) — i.e. nhr-47 sits upstream of insulin/Ephrin
     signalling in this stress context. These are downstream/indirect readouts, NOT demonstrated direct targets.

2. 6-PPD-quinone, reproductive toxicity [PMID:40482507]:
   - nhr-47 is among germline NHRs whose knockdown SUPPRESSES 6-PPDQ reproductive toxicity
     [PMID:40482507 "6-PPDQ reproductive toxicity was suppressed by nhr-47, nhr-14, daf-12, and nhr-249 RNAi and accelerated by nhr-12, nhr-145, and nhr-171 RNAi"].
   - nhr-47 expression is modulated by DNA-damage-checkpoint and ferroptosis-related signals under 6-PPDQ.

Consistent theme: in the germline, nhr-47 acts (with daf-12/nhr-14) as a positive mediator of
toxicant-induced reproductive/transgenerational toxicity; knocking it down is protective.

## Interaction / network context
- Y2H interactome maps nhr-47 into the worm protein interaction network [PMID:19123269] (WI8);
  the specific nhr-47<->nhr-17 interaction is recorded in IntAct/UniProt (not stated verbatim in the paper text).
- nhr-47 is one node in the C. elegans multiparameter transcription-factor network [PMID:23791784],
  a study of protein-DNA / protein-protein / TF-TF network rewiring across paralogs.
- These two PMIDs underlie the two GOA IPI "protein binding" annotations (with_from UniProtKB:Q17589 = nhr-17).

## KNOWN vs NOT-KNOWN (explicit)
KNOWN:
- Molecular identity: zinc-finger, sequence-specific DNA-binding transcription factor of the
  nuclear-receptor (HNF4-derived supnr) family; nuclear localization; binds zinc.
- Physically interacts with nhr-17.
- Expressed in neurons, ventral nerve cord, spermatheca, pharynx, intestine.
- Germline knockdown modulates susceptibility to two environmental toxicants (nanoplastics, 6-PPDQ),
  positioning it upstream of insulin/Ephrin/Wnt ligand-gene expression in that stress context.

NOT KNOWN (knowledge gaps):
- Ligand: whether nhr-47 has any endogenous small-molecule ligand, and its identity — it is an orphan
  receptor, and supnrs may have altered/lost ligand-dependence
  [PMID:15983867 "This origin has specific implications for the\nrole of ligand binding in the function and evolution of the nematode\nsupplementary nuclear receptors"].
- Direct target genes / response element: no ChIP, reporter, or motif defines the nhr-47 regulon;
  it is unknown whether it is an activator or repressor, and whether the toxicant-context downstream
  genes (ins-3, daf-28, efn-3, …) are direct or indirect targets.
- Definitive loss-of-function role: no baseline null-mutant developmental/metabolic/immune phenotype;
  the only phenotypes are germline RNAi effects in toxicant-challenge assays.

## GO annotation review orientation
- All 14 GOA annotations are IBA (phylogenetic), IEA (InterPro/UniProt), or IPI (interactome).
- MF/CC core (nuclear receptor activity, RNA Pol II cis-regulatory sequence-specific DNA binding,
  sequence-specific DNA binding, DNA-binding TF activity, zinc ion binding, nucleus) is well supported
  by the diagnostic domain architecture → ACCEPT as core.
- BP terms are family-propagated/inferred (regulation of transcription, intracellular receptor
  signaling) → KEEP; "cell differentiation" (IBA) has no nhr-47-specific support → KEEP_AS_NON_CORE
  (generic pan-NHR propagation).
- Two IPI "protein binding" annotations (nhr-17): experimental but uninformative term; do not REMOVE
  (real interaction), KEEP_AS_NON_CORE and flag that a more informative MF term is not warranted from
  a single Y2H edge.

## Falcon deep-research addendum (genes/worm/nhr-47/nhr-47-deep-research-falcon.md)
Genuine Edison "deep research" report (23-min run, 22 citations). Key points, each attributed
to the falcon-cited primary source (NOT independently full-text-verified here unless noted):

- **csr-1 synonym caution**: the UniProt `Synonyms=csr-1` for nhr-47 is an OLD locus synonym and
  must NOT be confused with the CSR-1 Argonaute (a distinct gene). Falcon flags this explicitly.
- **Estradiol responsiveness (the source of the WormBase estradiol statement)**: Novillo et al. 2005
  [PMID:21676746] microarray of steroid-exposed C. elegans; falcon reports "10 μM estradiol increased
  nhr-47 expression 3.4-fold". NOTE: the cached PubMed abstract of PMID:21676746 does NOT name nhr-47
  (the per-gene 3.4-fold value is in the full text / supplementary data and in WormBase curation), so I
  do NOT attach a verbatim nhr-47 supporting_text to this PMID; it is added to references as the
  estradiol-induction source with correctness VERIFIED and no gene-specific quote.
- **No robust RNAi phenotype**: falcon reports genome-wide RNAi of nhr-47 in C. elegans gave "no
  observable phenotype" (via Ciche & Sternberg 2007, which also reports the H. bacteriophora ortholog
  Hba-nhr-47 RNAi is mostly phenotype-free, ~3-12% sterility in some trials). Consistent with knowledge
  gap #3 (no defined loss-of-function role); treated as supporting context, not review provenance,
  because the C. elegans nhr-47 no-phenotype claim is a secondary summary.
- **Family/metabolic context**: Taubert, Ward & Yamamoto 2011 (NHRs in nematodes) and Arda et al. 2010
  (metabolic gene-regulatory network; NHRs enriched as metabolic-promoter regulators, modular, MDT-15
  cofactor). Places nhr-47 in the HNF4-derived supnr class plausibly linked to metabolism — but nhr-47
  itself is uncharacterized in these.
- **Discrepancy**: falcon states nhr-47 is on "chromosome II"; UniProt Q17370 says Chromosome V. Trust
  UniProt (Chromosome V). Did NOT propagate falcon's chromosome claim.

Net effect on review: falcon corroborates the orphan/dark framing, the estradiol angle, and the
absence of a robust loss-of-function phenotype; it did not surface any definitive ligand, direct
target, or physiological role. No core-function or knowledge-gap conclusion was changed by it.
