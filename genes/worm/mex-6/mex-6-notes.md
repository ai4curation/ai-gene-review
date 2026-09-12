# mex-6 (C. elegans) research notes

UniProt: Q09436 (MEX6_CAEEL) · WormBase: WBGene00003231 · ORF: AH6.5 · 467 aa
Gene: mex-6 ("Muscle EXcess 6"). Paralog: mex-5 (Q9XUB2, WBGene00003230).

These are a working research journal for the AI GO-annotation review. Provenance is
recorded inline as `[PMID:xxxxx "verbatim quote"]`. **All cached publications for this
gene are abstract-only** (`full_text_available: false` in each `publications/PMID_*.md`),
so experimental IDA/IPI/IGI annotations are curated by WormBase from full text I cannot
see — I defer to the curator on those per project guidelines and use UNDECIDED only where
neither the abstract nor UniProt can corroborate.

## Overriding caution: mex-5 is the dominant paralog

mex-5 and mex-6 are "two nearly identical genes" [PMID:10882103 "We provide evidence that
two nearly identical genes, mex-5 and mex-6, link PAR asymmetry to those subsequent protein
asymmetries"]. Almost every mechanistic / biochemical study foregrounds **mex-5**:
- The RNA-recognition biochemistry (poly-U tract, low specificity, discriminator residue)
  was done on **MEX-5** [PMID:17264081 "the TZF protein MEX-5, a primary anterior
  determinant, is an RNA-binding protein that recognizes linear RNA sequences with high
  affinity but low specificity"]. There is **no equivalent mex-6-specific biochemistry**.
- The P-granule/phase-separation mRNA-competition mechanism (PMID:27594427) was demonstrated
  for **MEX-5**, not mex-6.
Therefore, for mex-6 I treat shared-family/paralog properties as inference and flag them,
and I rely on the sources that name **mex-6 explicitly** for the strongest calls.

## What is KNOWN about mex-6 specifically (mex-6 named in the source)

1. **Redundant polarity/soma-germline function with mex-5.** mex-5 and mex-6 together link
   PAR cortical asymmetry to downstream cytoplasmic protein asymmetries; loss of both (not
   either alone) produces the strong phenotype [PMID:10882103 "two nearly identical genes,
   mex-5 and mex-6, link PAR asymmetry to those subsequent protein asymmetries"].
   UniProt summarizes: mex-6 "Functions with mex-5 to affect embryonic viability, establish
   soma germline asymmetry in embryos and establish plk-1, pie-1, mex-1, and pos-1 asymmetry
   in embryos ... Also affects formation of intestinal cells" (Q09436 CC FUNCTION, cites
   PubMed:10882103, PubMed:18199581).

2. **MEX-6 is one of two cytoplasmic CCCH-finger proteins acting in the establishment phase
   of zygote polarity.** [PMID:12588843 "The kinase PAR-1 and the CCCH finger proteins MEX-5
   and MEX-6 also function during the establishment phase in a feedback loop to regulate
   growth of the posterior domain"]. MEX-6 localization dynamics were imaged by GFP fusion
   alongside MEX-5 [PMID:12588843 "we have analyzed the localization dynamics of PAR-2,
   PAR-6, MEX-5, MEX-6 and PIE-1 in wild-type and mutant embryos"].

3. **MEX-6 binds polo kinases PLK-1 and PLK-2 via their polo-box domains** (direct, mex-6
   named). [PMID:18199581 "polo kinases, via their polo box domains, bind to and regulate
   the activity of two key polarity proteins, MEX-5 and MEX-6"]. This underpins the IPI
   annotations GO:0019901 (protein kinase binding) and GO:0019904 (protein domain specific
   binding), curated by WormBase with `with` = plk-1 (WBGene00004042) and plk-2
   (WBGene00004043). UniProt: mex-6 "Interacts (probably when phosphorylated on Thr-190)
   with plk-1 (via POLO box domain) and plk-2 (via POLO box domain)" (Q09436 CC SUBUNIT).

4. **The polo docking is primed by MBK-2/DYRK2 phosphorylation of a Thr near the fingers.**
   In MEX-5 the primed residue is T186; the paralogous residue in MEX-6 is **Thr-190**
   (UniProt MOD_RES 190 "Phosphothreonine", MUTAGEN T190A "Severe reduction in binding to
   plk-1 and plk-2"; MUTAGEN T190E phosphomimetic "severely abolishes interaction with plk-1
   and plk-2"), both citing PubMed:18199581. The paper's abstract describes the mechanism on
   MEX-5's T186 [PMID:18199581 "MBK-2, a developmentally regulated DYRK2 kinase activated at
   meiosis II, primes T(186) for subsequent polo kinase-dependent phosphorylation"], with
   mex-6 assayed in the full text (UniProt MUTAGEN evidence is ECO:0000269|PubMed:18199581).

5. **MEX-6 is required (redundantly with mex-5) for PLK-1 asymmetry.** UniProt DISRUPTION
   PHENOTYPE: "RNAi-mediated knockdown in mex-5 zu199 mutant background causes a loss in
   plk-1 asymmetric distribution during the first embryonic cell divisions"
   (ECO:0000269|PubMed:18199581). This is the sensitized (mex-5 null) background that exposes
   the mex-6 contribution — the clearest statement of a mex-6 role beyond mex-5.
   Supports GO:0032880 (regulation of protein localization), curated IGI with `with` = mex-5.

6. **Subcellular location: cytoplasm.** UniProt SUBCELLULAR LOCATION "Cytoplasm"
   (ECO:0000250|UniProtKB:Q9XUB2, i.e. by similarity to mex-5). Also curated experimentally:
   GO:0005737 cytoplasm IDA from PMID:12588843.

7. **PTM (by similarity):** "Phosphorylation on Ser-457 by par-1 promotes localization of the
   protein to the anterior cytoplasm of the zygote" (Q09436 MOD_RES 457, ECO:0000250|
   UniProtKB:Q9XUB2) — inferred from mex-5, consistent with an anterior gradient like mex-5.

## Domain / sequence facts (mex-6, from UniProt Q09436)

- Two C3H1-type (CCCH) tandem zinc fingers: 273–302 and 317–347 (PROSITE PS50103).
- InterPro: IPR045877 (ZFP36-like), IPR000571 + IPR036855 (CCCH znf). PANTHER PTHR12547
  (CCCH ZINC FINGER/TIS11-RELATED), subfamily PTHR12547:SF18 (PROTEIN TIS11).
- Pfam PF00642 (zf-CCCH ×2), SMART SM00356. => zinc binding intrinsic to the fold
  (supports GO:0046872 metal ion binding IEA from InterPro).
- Reactome cross-ref R-CEL-450513 "Tristetraprolin (TTP, ZFP36) binds and destabilizes mRNA"
  — i.e. the family reference pathway; this is the ancestral TTP-family framing behind the
  IBA deadenylation/AU-rich terms.
- Disordered/low-complexity N-term and central regions; not a DNA-binding protein: CCCH
  fingers are RNA-binding (the historical UniProt "DNA-binding" keyword annotation
  GO:0003677 has been dropped from the current GOA / QuickGO set for this gene).

## Mapping to existing GOA annotations (17 in the stub) + planned action

MF (molecular function):
- GO:0035925 mRNA 3'-UTR AU-rich region binding (IBA) — **MODIFY**. Ancestral TTP/ZFP36
  (AU-rich) specificity; nematode MEX proteins diverged (discriminator residue) and MEX-5
  binds poly-U with low specificity, not AREs [PMID:17264081 "human TZF homologs
  tristetraprolin and ERF-2 bind with high specificity to UUAUUUAUU elements ... mutation of
  a single amino acid in each MEX-5 zinc finger confers tristetraprolin-like specificity"].
  Replace with the more accurate, already-curated GO:0003730 (mRNA 3'-UTR binding).
- GO:0000289 nuclear-transcribed mRNA poly(A) tail shortening (IBA) — **MARK_AS_OVER_ANNOTATED**.
  Ancestral TTP deadenylation function (Reactome R-CEL-450513); no direct mex-6 deadenylation
  evidence; MEX-5/6 literature is about polarity/translational control, not decay.
- GO:0000900 mRNA regulatory element binding translation repressor activity (IBA) — **UNDECIDED**.
  Mechanism of MEX-5/6 translational control is not a clean sequence-specific repressor;
  the best-supported translational output (zif-1 3'UTR) is *positive* (relieving POS-1
  repression). No direct mex-6 evidence. (Mirrors mex-5 review.)
- GO:0005829 cytosol (IBA) — **ACCEPT** (cytoplasmic; consistent with IDA cytoplasm).
- GO:0160134 protein-RNA sequence-specific adaptor activity (IBA) — **MODIFY** to GO:0003729
  mRNA binding. Binding is not sequence-specific (poly-U, low specificity in the paralog).
- GO:0003729 mRNA binding (IEA InterPro) — **ACCEPT** (core MF; CCCH TZF).
- GO:0046872 metal ion binding (IEA InterPro) — **ACCEPT** (zinc in CCCH fold).
- GO:0019901 protein kinase binding (IPI PMID:18199581) — **ACCEPT** (binds PLK-1/PLK-2).
- GO:0019904 protein domain specific binding (IPI PMID:18199581) — **ACCEPT** (polo-box).
- GO:0003730 mRNA 3'-UTR binding (IDA PMID:17264081) — **ACCEPT**, defer to curator. The
  cited paper's abstract characterizes MEX-5, but WormBase curated this as a mex-6 IDA from
  full text; mex-6 is a genuine mRNA/3'UTR-binding TZF protein. Core MF.

CC (cellular component):
- GO:0005737 cytoplasm (IEA SubCell) — **ACCEPT**.
- GO:0005737 cytoplasm (ISS from mex-5 Q9XUB2) — **ACCEPT** (ortholog transfer; also IDA-backed).
- GO:0005737 cytoplasm (IDA PMID:12588843) — **ACCEPT** (experimental, core location).
- GO:0043186 P granule (IDA PMID:12588843) — **KEEP_AS_NON_CORE**. Experimental WormBase IDA;
  MEX-6 is predominantly *anterior* cytoplasmic (where P granules dissolve), so P-granule
  association is at best transient/minor and not the core localization. I do NOT REMOVE an
  experimental IDA whose full text I cannot read (unlike mex-5, mex-6 has no dedicated
  phase-separation paper establishing it *dissolves* rather than *resides in* P granules).
- GO:0043186 P granule (IEA ARBA, GO_REF:0000117) — **MARK_AS_OVER_ANNOTATED**. Pure
  machine-learning (ARBA) prediction of P-granule residency for an anterior-enriched TZF
  protein; redundant with the IDA and exactly the kind of electronic over-propagation to
  down-weight. Localization (if real) is already captured non-core by the IDA.

BP (biological process):
- GO:0017148 negative regulation of translation (IEA, logical inference from GO:0000900) —
  **UNDECIDED** (inherits the uncertainty of GO:0000900; directionality doesn't match the
  positive zif-1 output).
- GO:0032880 regulation of protein localization (IGI PMID:18199581, with mex-5) — **ACCEPT**.
  mex-6 (redundantly with mex-5) establishes plk-1/pie-1/mex-1/pos-1 asymmetry
  (UniProt CC FUNCTION; DISRUPTION PHENOTYPE for plk-1 asymmetry).

## What is genuinely NOT known about mex-6 (for knowledge_gaps)

- **The non-redundant/unique contribution of mex-6 vs mex-5 is undefined.** mex-6 single loss
  is largely silent; phenotypes require removing mex-5 too [PMID:10882103 nearly-identical,
  redundant]. Whether mex-6 has *any* private target, tissue, or timing distinct from mex-5
  is unknown. Boundary: we know the *pair* is required (UniProt DISRUPTION uses a mex-5(zu199)
  background to reveal mex-6).
- **Direct mex-6 mRNA targets are unknown.** No CLIP/biochemistry on MEX-6 itself; RNA-binding
  properties are inferred from MEX-5 (poly-U, low specificity) [PMID:17264081].
- **Whether MEX-6 RNA binding is required for its polarity function is untested for mex-6.**
  The RNA-binding→gradient→polarity link is argued for MEX-5; no mex-6 RNA-binding-mutant
  in vivo test is published.
- **Whether MEX-6 residence in P granules is real or a gradient artefact** (see IDA vs the
  anterior-enrichment biology).

## Falcon deep research
First attempt: `just deep-research-falcon worm mex-6 --fallback perplexity-lite` — the falcon
(Edison) provider **timed out after 600s**, and the perplexity-lite fallback returned **HTTP 401
(insufficient_quota)**, so no deep-research file was produced on the first pass. A second
falcon-only retry was launched; the wrapper again reported a 600s timeout, but the underlying
Edison client **did complete just after the timeout and wrote a genuine report**
(`mex-6-deep-research-falcon.md`, Edison Scientific Literature, 33 citations, 636s duration,
+ `_artifacts/`). That file is retained as a committed research artifact. Its citations use
falcon's internal `authorYYYY pages` format (not PMIDs), and the validator does not check
non-PMID quotes, so — per project guidance — **I did NOT cite the falcon file in the review**;
every `supporting_text` in the review is instead a verbatim substring of a cached PMID abstract,
grep-verified. The falcon report is consistent with (and corroborates) the review: it independently
describes mex-6 as the partially redundant paralog of mex-5, the CCCH-TZF poly-U RNA binding, the
PAR-1/PP2A diffusion gradient, PLK-1/2 polo-box association, and the zif-1/ZIF-1 anti-germ-plasm
axis. No content in the review was taken uncritically from it, and nothing was fabricated.
Annotations that could not be corroborated from cached primary sources remain UNDECIDED
(GO:0000900, GO:0017148).
