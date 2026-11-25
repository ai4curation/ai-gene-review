# Slc16a1 (rat) review notes

## Session 1 (2026-10-28)

- fetch-gene needed three attempts (UniProt REST read timeouts); resolved P53987
  (MOT1_RAT, RGD:3690, GeneID 25027). 79 GOA rows seeded.
- No deep-research API keys; wrote `Slc16a1-deep-research-manual.md` by hand.
- Full text read: PMID:19473976 (key paper; DIDS site, Lys38, embigin
  cross-link, dimer artifact), PMID:17127621, PMID:19929853, PMID:32766828.
  Abstract-only: PMID:8526936, 9374487, 9639576, 10564700, 10714609,
  11719518, 18619525, 23506875.

### Decisions
- Core MF: lactate:proton symporter activity (GO:0015650), with monocarboxylic
  acid / pyruvate transporter activity as broader/sibling claims.
  [PMID:9639576 "Superfusion with lactate resulted in intracellular acidification of MCT1-expressing oocytes, but not in non-injected control oocytes."]
- GO:0042802 identical protein binding (IPI, PMID:19473976): the paper itself
  attributes the dimer band to detergent aggregation [PMID:19473976 "we have shown previously that this occurs as a result of aggregation of MCT1 in detergent"],
  and FRET found no MCT1-MCT1 proximity [PMID:11719518]. Removed; flagged for expert.
- Bare protein binding (basigin, PMID:11719518, 17127621): removed per policy;
  the real biology (obligate ancillary subunit) is captured in core_functions text.
- Succinate transport terms (ISO/ISS/IEA from human/mouse): kept as non-core;
  only the protonated form at acidic pH (ischaemia) [PMID:32766828].
- Centrosome / centrosome cycle: transferred from a single human study
  (PMID:23816619, left UNDECIDED in human review); marked over-annotated for rat.
- Mouse phenotype-derived processes (response to food, glucose homeostasis,
  insulin secretion, behavioral response to nutrient, lipid metabolism, pyruvate
  catabolism): downstream consequences of lactate/pyruvate flux, not processes
  MCT1 executes. Marked over-annotated (pyruvate catabolic process removed - MCT1
  moves pyruvate but does not catabolise it).
- NEW: pyruvate transmembrane transporter activity (GO:0050833), direct oocyte
  evidence [PMID:9639576].

## 2026-10-28 review-fix pass

- Removed the deep-research-manual self-citation from the GO:0042802 identical protein binding row (REMOVE); PMID:19473976 and PMID:11719518 already support it. The citations of that file on the succinate rows are kept because they record a negative result (no dicarboxylate transport in neutral-pH oocytes) that no single cited PMID states.
