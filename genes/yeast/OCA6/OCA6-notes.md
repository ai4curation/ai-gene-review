# OCA6 (YDR067C) — S. cerevisiae — curation notes

Reviewer journal. Provenance recorded inline as `[PMID:xxxx "verbatim supporting text"]` or `[source URL]`.
This is a DARK / understudied gene: the primary deliverable is an honest `knowledge_gaps` section
plus carefully-reasoned `description`/`core_functions` grounded in domain, orthology, and literature.
OCA6-specific evidence is carefully separated from evidence about other OCA-family members.

## Identity

- UniProt: Q12454 (OCA6_YEAST), 224 aa, MW ~26 kDa.
- Systematic name: YDR067C; SGD: S000002474; standard name OCA6 = "Oxidant-induced Cell-cycle Arrest protein 6".
- UniProt RecName: "Putative tyrosine-protein phosphatase OCA6"; EC=3.1.3.48 (marked *Putative*).
- PANTHER family PTHR31126 (TYROSINE-PROTEIN PHOSPHATASE); subfamily PTHR31126:SF14 (TYROSINE-PROTEIN PHOSPHATASE OCA6-RELATED).
- CDD: cd17663 = **PFA-DSP_Oca6** (Plant-and-Fungi Atypical Dual-Specificity Phosphatase, Oca6 clade).
- Pfam: PF03162 (Y_phosphatase2 / Siw14-like); InterPro IPR004861 (Siw14-like), IPR029021 (PTP-like fold),
  IPR020422 (TYR_PHOSPHATASE_DUAL). Gene3D 3.90.190.10 (PTP superfamily fold). SUPFAM SSF52799.

## Domain / catalytic-motif analysis (done INLINE from OCA6-uniprot.txt sequence)

Full sequence (224 aa):
```
MTLVTPLQFS TVQPNLYRGS YPREINLPFL RTLRLKYILS LTPEPLSTDP   (1-50)
LMVKFCEENN IKTIHIKCQS ERKADKTKPK IKRKKKTVPI EYDVVVRCVK   (51-100)
FLIDKGHYPC YMHCTNGELI ISLVVACMRK FSYWSTVSIL NEFLVYNSSI   (101-150)
NIHERNFIEN FNSEIEVDDL DIKDKVPWIT VRYIARTATE SKDELRVDDA   (151-200)
NASEKVARVS SVSNSLPKLK FHSM                               (201-224)
```

- UniProt annotates a single PTP DOMAIN (residues 8–170) and ACT_SITE at **Cys114** ("Phosphocysteine intermediate",
  ECO:0000255 PROSITE-ProRule PRU00160 — i.e. a rule/profile prediction, NOT experimental).
- The catalytic P-loop of PTP/DSP enzymes (and of the PFA-DSP family specifically) is the **CX5R** signature:
  the nucleophilic Cys, then five residues, then an invariant Arg that binds the substrate phosphate.
  [CDD PFA-DSP family: "C x x x x x R" active site, 7 residue positions — https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=350351]
- **Inline finding: OCA6 has NO intact CX5R motif.** Region around the predicted catalytic Cys is
  `...HYP C(110) YMH C(114) TNGELI I(120) I(121) S...`. Taking Cys114 as the nucleophile, positions 115–120 are
  `T-N-G-E-L-I`; the P-loop +6 position (where the invariant catalytic Arg must sit) is **Ile120, not Arg**.
  A regex scan of the whole protein for `C.{5}R` (CX5R) and `HC.{5}R` returns **zero matches** anywhere.
  All Cys are at 56,68,98,110,114,127; all Arg at 18,23,31,34,72,83,97,129,155,182,186,196,208 — none form a CX5R.
- Interpretation: the invariant P-loop arginine of the CX5R catalytic loop appears **absent/substituted** in OCA6.
  This is the classic signature of a **pseudophosphatase** (fold retained, catalytic machinery degenerate).
  This is my own sequence-level analysis; it should be treated as strong but not laboratory-confirmed.

- Independent literature corroboration of a degenerate motif in OCA6:
  the fungal pseudophosphatome analysis reports that "the **Oca1, Oca2, and Oca6 contain residue substitutions
  at the core catalytic motif**, while Oca4 appears to lose the entire catalytic motif."
  [ACS Omega "Pseudophosphatase Scanner for Genome-Wide Fungal Pseudophosphatome Analysis",
   https://pubs.acs.org/doi/10.1021/acsomega.6c00759 — abstract/summary via web search 2026-07-05]
  NOTE: full text 403-gated; recorded as web evidence, not a cached PMID quote.
- CAVEAT / conflicting signal: one secondary web summary states "Oca1, Siw14/Oca3, and Oca6 are supposed to be
  active enzymes." This is a secondary assertion; it conflicts with (a) my motif analysis and (b) the
  pseudophosphatase-scanner classification. **No paper in the cache directly measures OCA6 catalytic activity.**
  Therefore catalytic status is treated as UNRESOLVED, leaning inactive, in the review.
- MOD_RES: Thr2 phosphorylated (large-scale phosphoproteomics) [PMID:18407956]. Peripheral to function.

## What is KNOWN about OCA6 specifically (with attribution)

1. **Subcellular location = cytoplasm.** Genome-wide GFP-fusion localization.
   [PMID:14562095 — "Global analysis of protein localization in budding yeast"; abstract-only cache].
   GOA carries this as HDA (cytoplasm) plus a UniProt IEA (SubCell) duplicate.
2. **Deletion reduces Brome mosaic virus (BMV) RNA replication in yeast.** OCA6 is one of ~100 host genes from a
   genome-wide single-gene-deletion screen whose loss altered BMV replication.
   [PMID:14671320 — "Systematic, genome-wide identification of host genes affecting replication of a
   positive-strand RNA virus"; abstract-only]. This is a low-specificity, high-throughput hit; the abstract does
   NOT describe an OCA6-specific mechanism ("nearly 100 genes whose absence inhibited or stimulated BMV RNA
   replication"). UniProt promotes this to `-!- FUNCTION: Required for replication of Brome mosaic virus (BMV)`
   with ECO:0000269, but it is a screen-level phenotype, not a demonstrated biochemical role.
3. **OCA6 is a member of the fungal OCA family of PFA-DSP-related atypical DSPs.**
   [PMID:21409566 — "novel PFA-DSP-related proteins in fungi (Oca1, Oca2, Oca4 and Oca6 in Saccharomyces
   cerevisiae)"; "The closest yeast homolog for these proteins was the PFA-DSP from S. cerevisiae
   ScPFA-DSP1/Siw14/Oca3."].
4. **OCA6 participates in caffeine/rapamycin stress responses, genetically linked to the OCA family.**
   [PMID:21409566 — "Oca1, Oca2, Siw14/Oca3, Oca4, and Oca6 were involved in the yeast response to caffeine and
   rapamycin stresses"; "overexpression of Siw14/Oca3 suppressed the caffeine sensitivity of oca1, oca2, oca4,
   and oca6 deleted strains, indicating a genetic linkage and suggesting a functional relationship for these
   proteins."]. So OCA6-null caffeine sensitivity is rescued by the *active* paralog Siw14 — consistent with OCA6
   working in a shared pathway rather than providing unique catalysis.
5. **SGD phenotype survey (large-scale):** oca6Δ shows decreased oxidative-stress resistance, decreased chemical
   resistance, abnormal chemical-compound accumulation, decreased competitive fitness, vacuolar morphology
   abnormalities. [SGD locus S000002474, https://www.yeastgenome.org/locus/S000002474 — SGD summarizes
   "biological role is unknown"; molecular function ND].
6. **OCA "complex".** Transcriptional profiles of oca1/oca2/oca3(SIW14)/oca5/oca6 deletion strains are highly
   similar and there is evidence for physical interactions among OCA proteins — hence the "OCA complex" framing.
   [web summary of high-throughput yeast complex/chemical-stress mapping; PMID:22282571 (Hillenmeyer et al. /
   related large-scale complex mapping) — NOT directly quoted from cache; treat as supporting, not primary].

## What is NOT known about OCA6 (knowledge gaps)

- **Is OCA6 catalytically active?** No direct assay of OCA6 phosphatase activity exists in the cache. The 2011
  paper measured Siw14 (active) and Oca1 (inactive), NOT OCA6. Sequence analysis (no CX5R Arg) and the
  pseudophosphatase-scanner classification both point to *likely catalytically dead / pseudophosphatase*, but this
  is inferred, not measured.
- **What is its physiological substrate?** The active family prototype Siw14/Oca3 is a 5-InsP7 inositol
  pyrophosphate phosphatase (not a protein-tyrosine phosphatase). Whether OCA6 has any residual activity on
  inositol pyrophosphates, on a phosphoprotein, or acts purely as a non-catalytic scaffold/regulator within the
  OCA complex is unknown.
- **Its specific role in the OCA complex / oxidative-stress response.** The "OCA" (oxidant-induced cell-cycle
  arrest) name derives from OCA1/YNL099C [PMID:11408586, Alic et al. 2001: YNL099C required for G1 arrest on
  linoleic-acid-hydroperoxide]. OCA6 was named by family membership; there is no direct demonstration that OCA6
  itself mediates oxidant-induced cell-cycle arrest. Whether OCA6 is a catalytic subunit, a regulatory subunit,
  or functionally redundant within the complex is unresolved.
- **Mechanism of the BMV-replication phenotype.** Whether OCA6 acts directly on viral replication or indirectly
  (via stress signaling / membrane lipid / inositol-pyrophosphate homeostasis) is unknown.

## Attribution discipline: OCA6 vs other OCA members

- **Siw14/Oca3**: the biochemically characterized active PFA-DSP (5-InsP7 phosphatase). Do NOT transfer its
  measured catalytic activity to OCA6.
- **Oca1/YNL099C**: founding OCA gene (oxidant-induced G1 arrest); shown catalytically inactive in vitro.
- **Oca2, Oca4, Oca5**: other family members; Oca4 has lost its catalytic motif; Oca5 reported as an inositol
  pyrophosphatase in another study. None of their specific data should be attributed to OCA6.
- OCA6-specific direct evidence is limited to: cytoplasmic localization (HTP), BMV-screen phenotype,
  caffeine-sensitivity/genetic-linkage as an oca6Δ member of the family, SGD phenotype survey, and the Thr2
  phosphosite. Everything else is family-level or orthology-based inference.

## Annotation review plan (6 GOA annotations)

1. GO:0016791 phosphatase activity (IBA, GO_REF:0000033) — family/fold supports a phosphatase-like domain; but
   catalytic Arg is degenerate. Keep as a cautious non-core general MF (KEEP_AS_NON_CORE) — IBA reflects the fold,
   and "phosphatase activity" is general enough to be defensible for the family; flag catalytic uncertainty in
   reason. (Do not promote to a specific PTP activity.)
2. GO:0004725 protein tyrosine phosphatase activity (IEA, GO_REF:0000120 = UniProtKB-EC from the *Putative* EC
   3.1.3.48) — this is the over-annotation. It asserts a *specific* protein-tyrosine-phosphatase catalysis that
   (a) is contradicted by the degenerate CX5R motif, and (b) is biochemically wrong even for the active family
   member (Siw14 is an inositol-pyrophosphate phosphatase, not a PTP). MARK_AS_OVER_ANNOTATED (specific PTP
   activity not supported; likely pseudophosphatase).
3. GO:0005737 cytoplasm (IEA, GO_REF:0000044 SubCell) — ACCEPT (or non-core); supported.
4. GO:0005737 cytoplasm (HDA, PMID:14562095) — ACCEPT; direct HTP localization evidence, this is the core CC.
5. GO:0003674 molecular_function (ND, GO_REF:0000015) — ACCEPT as ND placeholder (SGD's honest "unknown").
6. GO:0008150 biological_process (ND, GO_REF:0000015) — ACCEPT as ND placeholder.

Core function: uncertain molecular function within a PTP-superfamily / PFA-DSP fold, acting in the cytoplasm as
a member of the OCA family implicated in caffeine/rapamycin and oxidative-stress responses; likely a
pseudophosphatase (degenerate CX5R). Location cytoplasm is the one high-confidence attribute.

## Deep research (infra failure — documented, not fabricated)

Automated deep research could not be produced for OCA6:
- `just deep-research-falcon yeast OCA6 --fallback perplexity-lite` was run TWICE (initial + one retry per policy).
  Both runs HUNG with no output and were killed (~20 min then an 8-min bounded retry; SIGTERM exit 143).
- The perplexity-lite fallback returned HTTP 401 `insufficient_quota` (Perplexity API out of quota).

Per repository policy I did NOT fabricate a `-deep-research-{provider}.md` file. All findings in this review are
grounded directly in: the cached UniProt record (Q12454), the GOA TSV, cached PMIDs
(14562095, 14671320, 21409566, 18407956, 11408586), SGD (S000002474), CDD (cd17663 / PFA-DSP family),
PANTHER (PTHR31126 / SF14), and the reviewer's own inline CX5R catalytic-motif analysis of the UniProt sequence.
The review therefore does not depend on an automated deep-research file.
