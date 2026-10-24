# ppk18 curation notes

## 2026-09-27 Initial review (Q8TFG6, SPAPB18E9.02c)

### Inputs

- `ppk18-uniprot.txt` (entry version 150), `ppk18-goa.tsv` (17 rows, 10
  references), `ppk18-deep-research-falcon.md` (Edison/Falcon synthesis, 13
  citations; none of its primary sources are cached as PMIDs).
- Cached publications: PMID:26776736 Chica et al. 2016 (abstract only),
  PMID:29079657 Laboucarié et al. 2017 (abstract only; publisher blocks XML
  download, but the PMC HTML full text was consulted for the ppk18 data),
  PMID:31553675 Schutt & Moseley 2019 (full text), PMID:16823372 Matsuyama
  et al. 2006 ORFeome screen (abstract only).
- Comparators: human MASTL / ENSA / ARPP19 / PPP2R2A reviews (complete), yeast
  IGO1 (complete), yeast RIM15 and S. pombe igo1 / pab1 (queued);
  `modules/g2_m_transition.yaml` cites Ppk18 as the fission-yeast Greatwall
  exemplar in the optional Greatwall-endosulfine-PP2A-B55 part. Ppk18 is not
  in `gocams/index.tsv`.

### Gene identity

Ppk18 = Greatwall-family AGC kinase, PANTHER PTHR24356:SF1 ("SERINE_THREONINE-
PROTEIN KINASE GREATWALL"), 1318 aa; kinase domain 566-934, AGC C-terminal
935-1044, CheY-like response-regulatory domain 1200-1316, PAS-like N-terminus
(InterPro IPR000014). Paralogs: Cek1 (SPCC1450.11c, P38938; co-seed of the
regulation-of-mitotic-cell-cycle IBA node) and the more distant Ppk31. The
Falcon report stresses partial redundancy [file:ppk18-deep-research-falcon.md
"Ppk18 acts partly redundantly with the related Greatwall kinases Cek1 and
Ppk31; consequently, results from ppk18Δ cek1Δ or broader pathway mutants must
not be attributed solely to Ppk18."]. Substrate: Igo1 (SPAC10F6.16 / mug134,
P79058), Ser64 in the conserved endosulfine motif.

### Holistic picture

1. **Core function: TORC1-restrained Igo1 kinase that switches off PP2A-B55.**
   [PMID:26776736 "In the presence of nutrients, greatwall (Ppk18) protein
   kinase is inhibited by TORC1 and PP2A·B55 is active."; "When nutrients are
   limiting, TORC1 activity falls off, and the activation of greatwall (Ppk18)
   leads to the phosphorylation of endosulfine (Igo1) and inhibition of
   PP2A·B55, which in turn allows full activation of Cdk1·CyclinB and entry
   into mitosis with a smaller cell size."]. ppk18Δ fails to reduce size in
   poor nitrogen; moderate overexpression advances mitosis in rich medium
   (Falcon, from Pérez-Hidalgo & Moreno 2017). This is GO:1905287 (IMP) and
   its parents GO:1901992 (ARBA IEA) and GO:0007346 (IBA).
2. **Nutrient relay to differentiation.** Laboucarié 2017: ppk18Δ, igo1Δ and
   igo1-S64A weakly induce ste11+/mei2+ and differentiation, fail to
   phosphorylate Taf12, and pab1Δ suppresses ppk18Δ sterility (Fig 5, Appendix
   Fig S8; full text at PMC). Cached abstract only supports the framework
   [PMID:29079657 "Taf12 phosphorylation increases early upon starvation and
   is controlled by the opposing activities of the PP2A phosphatase, which is
   activated by TORC1, and the TORC2-activated Gad8AKT kinase."]. Falcon adds
   G1-arrest and sporulation defects of ppk18Δ. GO:0031139 IMP kept as ACCEPT
   and made the second core function.
3. **Quiescence / translation (Falcon only, not cached).** del Dedo 2024 Nat
   Commun: pathway supports Elongator-dependent tRNA modification and
   translation of AAA-rich transcripts on quiescence entry; most experiments
   used igo1Δ or ppk18Δ cek1Δ, so not attributable to Ppk18 alone. Not
   annotated in GOA; not proposed as NEW (double-mutant evidence, and the work
   of translation is done by Elongator/TORC2-Gad8 downstream).
4. **Sds23 genetic interaction (full text).** [PMID:31553675 "Both igo1∆ and
   ppk18∆ mutants alone did not display defects in cell shape, cell length at
   division, or division symmetry under normal growing conditions"]; double
   mutants larger and more bent, but for division symmetry "the double mutants
   were not significantly different from sds23∆ alone despite this trend
   (Figure 5E)". The IGI to GO:1902472 (division site positioning) rests on
   that non-significant trend, hence MARK_AS_OVER_ANNOTATED rather than
   REMOVE (the curator's reading of the IGI is not wrong; the term overstates
   it).
5. **Localisation.** Only direct datum: ORFeome YFP screen, cytosol (rich
   medium, Ppk18 inactive). UniProt: "SUBCELLULAR LOCATION: Cytoplasm
   {ECO:0000269|PubMed:16823372}." Falcon: "No direct, experimentally resolved
   localization of Ppk18 itself was identified in the retrieved literature."
   Nucleus IBA (node PTN001220116, seeded by Rim15) kept as non-core: no
   contradiction, but no target evidence either; cytoplasm IBA/IEA and cytosol
   HDA accepted.

### Decisions summary

- ACCEPT: all MF rows (0004672 IEA; 0004674 IBA/IDA/IEA; 0005524; 0106310),
  cytoplasm IBA + IEA, cytosol HDA, 0007346 IBA, 0031139 IMP, 0035556 IBA +
  IMP, 1901992 IEA, 1905287 IMP.
- KEEP_AS_NON_CORE: nucleus IBA.
- MARK_AS_OVER_ANNOTATED: 1902472 IGI (sds23).
- No REMOVE, MODIFY, NEW. Considered MODIFY of 0035556 IMP to TORC1 signaling
  (GO:0038202) and rejected: the paper does not establish Ppk18 as a direct
  TORC1 target (Falcon: Sck2 may be the intermediary), and PomBase applies the
  same generic term to Igo1 for the same paper.
- Validation: passes; the single warning (inconsistent actions on 0035556)
  was resolved by accepting both rows.

### Open items

- Mechanism of TORC1 inhibition of Ppk18 (direct, via Sck2, or 14-3-3 as for
  Rim15) and whether Cdk1 phosphorylates Ppk18's Ser/Thr-Pro sites.
- Ppk18 versus Cek1 versus Ppk31 division of labour; role of the CheY-like
  receiver and PAS-like domains.
- Live localisation of Ppk18 after nitrogen removal.
