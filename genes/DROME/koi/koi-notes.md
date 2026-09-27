# DROME koi review notes

## 2026-09-27 (claude-code)

Sources: UniProt koi entry, GOA-cited publications; added PMID:32066907 (PubMed-verified; fat-body ncMTOC paper,
source of UniProt MTOC/perinuclear location). Full text: PMID:22927463, PMID:29689197, PMID:32066907; abstract-only:
PMID:18820457, PMID:20702563. Falcon deep research not available at time of review.

Key findings
- Klaroid is the SUN protein that tethers the KASH protein Klarsicht [PMID:18820457 "Here, we identify Drosophila Klaroid, a SUN protein that tethers Klarsicht"];
  koi mutants phenocopy klar and lack apical nuclear migration in the eye disc [PMID:18820457 "we find that klaroid and klarsicht are required for nuclear migration in differentiating neurons and in non-neural cells"].
- Muscle: [PMID:29689197 "Hence, in muscles, myonuclear positioning is determined by LINC complexes that consist of the KASH proteins Klarsicht and Msp-300, as well as the SUN protein Koi"];
  [PMID:29689197 "koi84 / Def mutants display a strong nuclear clustering phenotype with 100% penetrance"]; Ari-1/Parkin mono-ubiquitinate Koi.
- Fat body: Koi at NE, mild positioning effects; ncMTOC is anchored by Msp300 [PMID:32066907 "Null alleles of klar or koi had little or moderate effect on nuclear centricity"].

Decisions
- GO:0034993 meiotic LINC IBA -> MODIFY to GO:0106094 (no meiotic evidence in fly; module convention).
- Perinuclear region of cytoplasm (IDA, IEA) -> MODIFY to nuclear envelope (SUN protein must span INM).
- MTOC (IEA) -> MARK_AS_OVER_ANNOTATED (ncMTOC is Msp300-anchored on the cytoplasmic face).
- Nuclear migration, nucleus localization, NE rows -> ACCEPT.
