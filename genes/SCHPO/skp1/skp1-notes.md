# skp1 (SPBC409.05, Q9Y709) - curation notes

Fission yeast Skp1 (historical names psh1 "pombe skp1 homologue" and sph1). Not to be
confused with S. cerevisiae Psh1, a Cse4-directed E3 ligase. Exemplars used for style:
`genes/yeast/SKP1/` and `genes/human/SKP1/`. Sibling SCHPO reviews: pop1 (COMPLETE),
cul1 and rbx1 (INITIALIZED at time of writing).

## Sources

- Deep research: `skp1-deep-research-falcon.md` (present; Edison/falcon). Its key
  quotable framing: "Skp1 itself does not possess a catalytic ubiquitin-transfer residue
  and does not determine one fixed substrate specificity." It also reports the 2021
  SCF(Pof3)-Hst4 study (Aricthota & Haldar, eLife) which is not in GOA for skp1 and not
  cached, so it is used only in prose.
- Full-text caches available: PMID:12167173 (Seibert 2002), PMID:25165823 (Tsutsui 2014),
  PMID:22292001 (Okamoto 2012), PMID:20230746 (Takayama 2010), PMID:23349636 (Roseaulin
  2013), PMID:18441123 (Dawson 2008), PMID:19243310 (Jourdain 2009). PMID:17016471
  (Tafforeau 2006) is flagged full text but holds only abstract + introduction.
- Abstract-only: PMID:11163211, 11820777, 12511573, 15147268, 15147872, 15555586,
  16823372, 16997270. Publisher pages returned 403 and none are in Europe PMC, so these
  were reviewed from the abstract and curators were deferred to wherever the abstract is
  consistent with the annotation.

## Biology, with provenance

- Identity and core complex: Psh1/Skp1 and Pip1/Rbx1 were identified by similarity and
  co-purify with Pop1, Pop2 and Pcu1 [PMID:12167173 "we identified in the S. pombe genome
  database psh1 (pombe skp1 homologue) and pip1 (pop interacting protein 1), two genes
  encoding proteins with strong similarity to human SKP1 and HRT1/RBX1/ROC1"]; endogenous
  proteins co-elute in a ~500 kDa complex [PMID:12167173 "co-elution of Pip1p with Pop1p,
  Pop2p, Pcu1p, and Psh1p in a high molecular weight complex of approximately 500 kDa"];
  the immunopurified complex polyubiquitylates phosphorylated Rum1 in vitro; the
  Pip1/Pcu1/Psh1 core is constant across the cell cycle; Pop1 and Pop2 each bind the core
  independently (cytoplasmic SCF(Pop2)).
- Localisation: GFP-Psh1 in both nucleus and cytoplasm [PMID:12167173 "While Pip1p, Psh1p,
  Pcu1p, and Pop2p were present in both the cytoplasm and the nucleus, surprisingly,
  GFP-Pop1p was largely restricted to the nucleus"]; ORFeome YFP survey agrees
  [PMID:16823372].
- F-box repertoire: two-hybrid screen with Skp1 as bait isolated six interactors including
  Pof10, whose F-box is required for Skp1 binding; Pof10 overexpression is lethal by
  sequestering Skp1 from Pop1 [PMID:11820777]. Systematic co-IP of 12 tagged F-box proteins
  and Pcu1: ts Skp1 alleles (substitutions on the F-box-binding face) retain Pcu1 binding
  but lose Pof1, Pof3 and Pof10 [PMID:15147268 "This systematic analysis showed that ts
  Skp1 retains binding to Pcu1"; "binding to three specific F-box proteins, essential
  Pof1, Pof3 involved in maintaining genome integrity, and nonessential Pof10, was
  reduced"]. UniProt records the F-box-binding region as residues 102-161 and I110T as
  losing Pof1/Pof3/Pof10 binding.
- Checkpoint: skp1 ts alleles show a G2 delay due to DNA-damage-checkpoint activation that
  is rescued by checkpoint abrogation [PMID:15147268 "skp1ts cells exhibit a G2 cell cycle
  delay, which is attributable to activation of the DNA damage checkpoint"].
- Mitosis: skp1-A7 enters mitosis but fails anaphase; arched intranuclear spindles
  collapse; attributed to failed nuclear membrane segregation [PMID:15147872 "Temperature-
  sensitive skp1-A7 mutants enter mitosis, but fail to execute anaphase."; "These abnormal
  phenotypes appear to stem from defects in nuclear membrane segregation."]. Later work
  shows the mitotic bent spindle is suppressed by rad3 deletion and that the responsible
  F-box protein is unknown [PMID:22292001 "In mitosis, the bent-spindle phenotype was no
  longer observed in either the skp1-a7 rad3Δ or the fbh1Δ rad3Δ mutants"; "The F-box
  protein responsible for this bent-spindle phenotype has not been identified."].
- Meiosis: skp1-a7 bent MI spindles are caused by chromosome entanglement from
  unresolved recombination intermediates; suppressed by rec12 deletion; Rhp51/Rad22 foci
  persist; fbh1 deletion and F-box mutants phenocopy [PMID:22292001 "Rhp51/Rad51-
  Rad22/Rad52 foci persisted until meiosis I in skp1 cells, proving accumulation of
  recombination intermediates."; "Skp1 and Fbh1 act together to resolve the meiotic
  recombination intermediates"].
- Fbh1-Skp1: Fbh1 can only be purified as a heterodimer with Skp1; the heterodimer has
  ssDNA-dependent ATPase and 3'-5' helicase activity (Skp1 alone has none), disrupts Rad51
  filaments, stimulates strand exchange after initiation, and with Pcu1-Rbx1 forms
  SCF(Fbh1) that ubiquitinates Rad51 with Ubc4 [PMID:25165823 "Because we could not purify
  Fbh1 alone, we purified Fbh1 and Skp1 as a protein complex"; "The Fbh1-Skp1 heterodimer
  exhibited a robust, ssDNA-dependent ATPase activity."; "Rad51 was ubiquitinated in an
  Ubc4- and SCFFbh1-dependent manner."].
- SCF(Pof3) substrates: Ams2 is stabilised in pof3 and skp1 cells and Skp1 co-IPs with
  Pof3-Ams2 [PMID:20230746 "Ams2 binds SCFPof3 and is stabilized in pof3 or skp1 cells."];
  Pol2 is stabilised in skp1-94 at 35 C and in pof3 deletion [PMID:23349636 "Pol2-FLAG was
  significantly stabilized when skp1-94 cells were incubated at 35°C"]. Hst4 is stabilised
  in pof3 deletion and skp1-94 (deep research; Aricthota & Haldar 2021, not in GOA).
- Cig2: G2/M instability requires Skp1 but not Pop1/Pop2 or APC/C [PMID:11163211 "The
  instability of Cig2 during G2 and M is independent of either the APC/C or Pop1/Pop2, but
  requires Skp1, a core component of SCF."].
- Pof14: forms a canonical F-box-dependent SCF; autocatalytic turnover needs its F-box,
  Skp1 and the proteasome; skp1-3 behaves as wild type under peroxide, so the Pof14 stress
  function is SCF-independent [PMID:17016471].
- Cullin-free complexes: Skp1-Pof6 lacks Pcu1 and is essential for cell separation
  [PMID:12511573 "Purification of Pof6 demonstrates association of Skp1, whereas the Pcu1
  cullin was absent from the complex."; "Other skp1-3f cells as well as the skp1-deleted
  cells accumulate abnormal thick septa leading to defects in cell separation."]; Sip1 is
  the third subunit, Skp1 is among the most abundant proteins in Sip1-TAP, no cullin
  peptides [PMID:19243310 "In summary, we describe the first non-SCF complex in S.
  pombe."]. RAVE-like complex: Skp1 co-IPs with Rav1 and with Rav2 in a Rav1-dependent way;
  rav1 loss gives V-ATPase defects [PMID:18441123 "As shown in Fig. 4A , Skp1
  coprecipitates with Rav1-myc."]. CAK subunits Mcs2 and Pmh1 associate with Skp1 without
  Pcu1 and are not degraded [PMID:15555586 "Association of Mcs2 or Pmh1 with Skp1 does not
  appear to be involved in proteolytic degradation, as these complexes do not contain
  Pcu1"].

## Decisions

- Protein binding (30 IPI rows): F-box partners (Pop1, Pop2, Pof1-14, Fbh1) -> MODIFY to
  F-box domain binding (GO:1990444), adding ubiquitin ligase complex scaffold activity
  (GO:0160072) where a Pcu1-containing SCF is documented (Pop1, Pop2, Pof1, Pof2, Pof3,
  Pof14, Fbh1); Pof6 and the uncharacterised F-box proteins get GO:1990444 only. Pcu1
  rows -> MODIFY to cullin family protein binding (GO:0097602) + GO:0160072. Pip1/Rbx1,
  Mcs2, Pmh1 and Sip1 rows -> REMOVE as uninformative (complex membership or unknown
  function; interaction not disputed), following the protein-binding policy and the yeast
  SKP1 exemplar.
- GO:0045841 negative regulation of mitotic metaphase/anaphase transition (IMP,
  PMID:15147872, abstract-only): UNDECIDED. The abstract describes a positive requirement
  for anaphase execution; the direction of the annotation cannot be checked without full
  text. Raised as a suggested question.
- GO:0006998 and GO:0101026 (same paper): KEEP_AS_NON_CORE - phenotype real but
  rad3-dependent and F-box unknown.
- GO:0000712 (meiosis, IMP): KEEP_AS_NON_CORE - follows the authors' wording; Fbh1-Skp1 is
  an anti-recombinase/helicase rather than a resolvase; flagged as a question.
- GO:0000018 and GO:0017117 (Fbh1 paper, IDA): ACCEPT - Skp1 is a stoichiometric,
  obligate subunit of the purified active heterodimer.
- GO:0030163 protein catabolic process (IMP, Cig2): MODIFY to GO:0031146.
- RAVE rows (GO:0043291 x2, GO:0070072, GO:0012505): KEEP_AS_NON_CORE, as in yeast.
- IBA rows (GO:0000278, GO:0005634, GO:0005737, GO:0031146, GO:0097602): ACCEPT.
- No NEW terms. Comparator check: PomBase annotated pof6 to GO:0000920 septum digestion
  after cytokinesis from PMID:12511573 but did not annotate skp1 from the same paper,
  which is read as a deliberate curator decision; raised as a question instead.
- Core functions: (1) SCF scaffold (GO:0160072, contributes to GO:0061630, in GO:0019005);
  (2) F-box-binding subunit of the Fbh1-Skp1 helicase heterodimer (GO:1990444, in
  GO:0017117, regulation of DNA recombination). Pof6/RAVE/CAK associations described in
  prose only.
