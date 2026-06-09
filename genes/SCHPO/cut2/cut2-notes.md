# cut2 (Securin, P21135) — review notes

Fission yeast (S. pombe) cut2 encodes Securin, the ortholog of budding-yeast Pds1
and human PTTG/securin. It is the inhibitory chaperone partner of the separase
Cut1 (Esp1 ortholog). Together they form the separase-securin (separin-securin)
complex (ComplexPortal CPX-2573).

## Core biology
- Cut1 (separase, ~200 kDa) and Cut2 (~42 kDa apparent / 296 aa, 32 kDa calc.)
  associate and co-sediment as large complexes (30S and 40S).
  [PMID:8978688 "Cut1 (approximately 200 kDa) and Cut2 (42 kDa) associate, as shown by immunoprecipitation, and co-sediment as large complexes (30 and 40S) in sucrose gradient centrifugation."]
- Both genes are essential for viability and for sister chromatid separation;
  ts cut2-364 phenocopies cut1 (the "cut" phenotype — nuclear bisection without
  chromosome separation).
  [PMID:8978688 "We show here that the phenotype of ts cut2-364 is highly similar to that of cut1 and that the functions of the gene products of cut1+ and cut2+ are closely interrelated. The cut1+ and cut2+ genes are essential for viability and interact genetically."]
- Cut2 localizes to the nucleus, concentrated along the short metaphase spindle.
  [PMID:8632802 "Cut2 is located in the nucleus, where it is concentrated along the short metaphase spindle."]
  [PMID:8978688 "Cut1 protein concentrates along the short spindle in metaphase as does Cut2."]

## Regulated proteolysis (degradation timing central to anaphase)
- Cut2 is degraded anaphase-specifically by the APC/cyclosome (Cut9 component),
  the same machinery that degrades cyclin B; degradation requires its N-terminal
  region.
  [PMID:8632802 "The rapid degradation of Cut2 at anaphase requires its amino-terminal region and the activity of Cut9 (ref. 14), a component of the 20S cyclosome/anaphase-promoting complex (APC), which is necessary for cyclin destruction."]
- Non-degradable Cut2 blocks sister-chromatid separation but not cell-cycle
  progression; rescued by grafting cyclin B N-terminus.
  [PMID:8632802 "Expression of non-degradable Cut2 blocks sister-chromatid separation but not cell-cycle progression. This defect can be overcome by grafting the N terminus of cyclin B onto the truncated Cut2, demonstrating that the regulated proteolysis of Cut2 is essential for sister-chromatid separation."]
- Cut2 has two N-terminal destruction boxes (D-box 1 at 28-31, D-box 2 at 47-50);
  mutating both abolishes ubiquitination and degradation (UniProt MUTAGEN, PMID:9312055 — not cached).

## Cut1 loading / mutual dependence
- The C-terminus of Cut2 binds the N-terminus of Cut1; Cut2 is required to load
  Cut1 onto the spindle at prophase, and Cut2 proteolysis is required for Cut1's
  active participation in separation.
  [PMID:9635190 "The carboxyl terminus of Cut2 interacts with the amino terminus of Cut1... The association between Cut2 and Cut1 is needed for the localization of Cut1 to the spindles, as Cut1 remains unbound to the spindle if complex formation is impaired."]
  [PMID:9635190 "Cut2 is required for loading Cut1 onto the spindle at prophase and Cut2 proteolysis is needed for the active participation of Cut1 in sister chromatid separation."]

## Mechanism / inhibitor activity
- Securin, like cyclins, is an APC/cyclosome target, polyubiquitinated before
  destruction; anaphase fails without securin destruction. Separin is inhibited by
  association with securin.
  [PMID:10651900 "Securin, like mitotic cyclins, is the target of the anaphase promoting complex (APC)/cyclosome and is polyubiquitinated before destruction in a manner dependent upon the destruction sequence. The anaphase never occurs properly in the absence of securin destruction."]
  [PMID:10651900 "Separin is a large protein (MW approximately 180 kDa), the C-terminus of which is conserved, and is thought to be inhibited by association with securin at the nonconserved N-terminus."]
- Review (Kitajima 2003 intro): separase forms a complex with guardian securin,
  transferred to nucleus and spindle MTs; proteolytic activity inhibited by
  securin until APC degrades securin at metaphase-anaphase.
  [PMID:14532136 "The separase (Cut1/Esp1 in fission/budding yeast) forms a complex with a guardian protein, securin (Cut2/Pds1), and this complex is transferred to the nucleus and spindle microtubules where the separase must be activated. But the proteolytic activity of separase is inhibited by securin until the onset of anaphase when the anaphase-promoting complex (APC) promotes the degradation of securin."]

## Meiosis
- Securin destruction is the trigger for separase activation and Rec8 cleavage
  during meiotic divisions; Cut2 is detected on short spindles at metaphase I/II
  but not at anaphase (consistent with degradation timing).
  [PMID:14532136 "Here we show that separase activation and resultant Rec8 cleavage are required for meiotic chromosome segregation in fission yeast."]
  UniProt INDUCTION: "Detected along the short spindles at metaphase I and metaphase II, but not at anaphase I, anaphase II..." (PMID:14532136).
- cut1/cut2 single mutants do not affect sporulation; the double mutant forms
  two-spored asci (genetic role in meiosis).
  [PMID:1934126 "Single mutants in cut1 or cut2 did not effect sporulation, whereas the double mutant cut1 cut2 formed two-spored asci."]

## DNA repair
- Securin (Cut2) is required for separase stability AND for proper repair of UV/
  X-ray/gamma DNA damage; the securin-separase complex aids repair by removing
  local cohesin at interphase. cut2(EA2) is UV-repair defective despite normal
  checkpoint activation.
  [PMID:15329725 "Here we show that securin is essential for separase stability and also for proper repair of DNA damaged by ultraviolet, X-ray and gamma-ray irradiation. The cut2(EA2) mutant is defective in the repair of ultraviolet damage lesions, although the DNA damage checkpoint is activated normally."]
  [PMID:15329725 "We propose that the securin-separase complex might aid DNA repair by removing local cohesin in interphase cells."]

## Localization (global)
- High-throughput YFP localization study; Cut2 reported nuclear (PMID:16823372,
  HDA). Genome-wide screen, supports nuclear localization.

## Annotation decisions summary
- Nucleus (EXP/IDA/HDA): ACCEPT — well supported core CC.
- separase-securin complex (IPI/IDA): ACCEPT — core CC.
- meiotic spindle (IDA, PMID:14532136): ACCEPT (KEEP_AS_NON_CORE) — meiosis-specific localization.
- endopeptidase inhibitor activity (TAS x2): ACCEPT — core MF (separase inhibitor).
- negative regulation of mitotic sister chromatid separation (IMP): ACCEPT — core BP.
- mitotic sister chromatid separation (NAS, ComplexPortal): KEEP_AS_NON_CORE — the
  complex enables separation, but Cut2 itself negatively regulates it; keep as the
  process it participates in.
- meiotic chromosome separation (NAS): ACCEPT/KEEP_AS_NON_CORE — meiotic role.
- meiotic nuclear division (IMP, PMID:1934126): KEEP_AS_NON_CORE — supported by genetic data.
- DNA damage response (IMP, PMID:15329725): KEEP_AS_NON_CORE — moonlighting/secondary role.
- cytoplasm (IEA InterPro): contradicted by experimental nuclear localization; Cut2
  is nuclear (it is Cut1/separase that is cytoplasmic in interphase). MARK_AS_OVER_ANNOTATED.
- chromosome organization (IEA InterPro): generic parent; MODIFY toward chromosome
  segregation / sister chromatid separation regulation.
- nucleus IEA (GO_REF:0000120): redundant with experimental; ACCEPT (NON_CORE) or keep.
