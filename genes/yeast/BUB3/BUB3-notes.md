# BUB3 (S. cerevisiae, P26449 / YOR026W) - curation notes

## Session 1 - full review of the GOA seed

### Sources used

- `BUB3-uniprot.txt` (entry version 201): 341 aa, seven WD repeats, structures 1YFQ (1.1 A),
  2I3S/2I3T (with Mad3/Bub1 GLEBS peptides), 4BL0 (Bub1-Bub3-phospho-MELT). Mutagenesis
  table from Wilson 2005 (PMID:15644329) and Primorac 2013 (PMID:24066227).
- `BUB3-deep-research-falcon.md` (Edison): agrees with UniProt; useful for the framing
  "phosphopeptide receptor and checkpoint-complex scaffold". Its 2024 items (Mukherjee meiosis
  paper; Yao GCR correction) are pathway-level context, not new Bub3 activities.
- Cached publications: full text for 10704439, 11726501, 15879521, 16651657, 17227844,
  21070969, 22940250, 23267104, 24066227, 24402315, 27170178, 37968396, 41398407; abstract
  only for 10688190, 10837255, 16429126, 18719252, 20489023.
- Exemplars: `genes/yeast/MAD2` (complete), `genes/yeast/MAD3` (complete), `genes/human/BUB3`.

### Biology, with provenance

- Bub3 is the reader of Mps1-phosphorylated Spc105/Knl1 MELT motifs
  [PMID:24066227 "In this study, we report that Bub3, a 7-bladed β-propeller, is the MELT(P) reader."].
  Bub3 alone binds MELT2P with ~10-fold lower affinity than Bub1-Bub3
  [PMID:24066227 "we observed a 10-fold reduction in the binding affinity of Bub3 for the MELT2P peptide (KD = 2 µM; Figure 4D) compared to the Bub1–Bub3 complex (Figure 1E), indicating that Bub1 does indeed positively contribute to the interaction."].
- Interface mutant R217A/R239A: no kinetochore localization, Bub1 delocalized, checkpoint lost
  [PMID:24066227 "Conversely, bub3Δ cells and bub3Δ expressing Bub3R217A–R239A-mCherry cells were unable to arrest, re-replicated their DNA, and re-budded, indicative of a disrupted SAC"].
- Kinetochore localization every cycle, shortly before budding until ~metaphase
  [PMID:24066227 "Bub3-mCherry appeared to co-localize with Mtw1 shortly before budding and until approximately metaphase"].
- Bub3's only kinetochore requirement is to localize Bub1; Mad1 binds Mps1-phosphorylated Bub1
  [PMID:24402315 "This suggests that the only requirement for Bub3 kinetochore localization in spindle checkpoint initiation is to localize Bub1."].
- Recruitment follows mass action; Mps1/Glc7 balance sets MELpT number
  [PMID:27170178 "Mps1 kinase, which phosphorylates MELT repeats to enable Bub3-Bub1 recruitment, and Glc7 phosphatase, which dephosphorylates MELpT to suppress Bub3-Bub1 recruitment"].
- Bub1 and Mad3 GLEBS motifs bind the same top-face groove, mutually exclusive
  [PMID:17227844 "Crystal structures of these peptides with Bub3 show that the interactions for Mad3 and Bub1 are similar and mutually exclusive."];
  Mad3-Bub3 is a stable heterodimer [PMID:17227844 "Mad3 forms a stable heterodimer with Bub3."].
- MCC: Bub3 co-IPs with Cdc20, Mad1, Mad2; WD40 mutants W31G/W120G lose Mad2/Mad3/Cdc20 binding
  and checkpoint [PMID:11726501 "point mutations altering the conserved WD40 motifs of Bub3 ... disrupt its association with Mad2, Mad3 and Cdc20, as well as proper checkpoint response."];
  complex forms without kinetochores [PMID:11726501 "Formation of the Bub3-Cdc20 complex requires all kinetochore checkpoint proteins but, surprisingly, not intact kinetochores."].
- Stoichiometry: small Mad2-Mad3-Bub3-Cdc20 pool vs large Mad2-Cdc20 pool, kinetochore-independent
  [PMID:15879521 "There is a small amount of Mad2-Mad3-Bub3-Cdc20 and a much larger amount of a complex that contains Mad2-Cdc20."].
- Biochemistry: Mad3-Bub3 + Mad2 lock Cdc20 on APC/C, block securin ubiquitination, promote Cdc20
  autoubiquitination [PMID:22940250 "Reconstitution with purified components revealed that a Mad3-Bub3 complex synergizes with Mad2 to lock Cdc20 on the APC/C and stimulate Cdc20 autoubiquitination, while inhibiting ubiquitination of substrates."].
  Mad3 alone is insoluble; the assayed entity is the Mad3-Bub3 heterodimer.
- Topo II checkpoint: Bub3 partially required
  [PMID:16651657 "The spindle checkpoint protein Bub3 appeared to be partially required for the G2/M delay"].
- BIR: bub3 reduces BIR because the SAC extends G2/M arrest
  [PMID:41398407 "Our screen identified a BIR defect in strains with deletion of the SAC genes BUB1 and BUB3, suggesting a role for the SAC in BIR."].

### Decisions and rationale

| Row(s) | Action | Why |
|---|---|---|
| GO:0000727 BIR (IMP) | MARK_AS_OVER_ANNOTATED | Necessity via checkpoint delay, not participation in repair; same call as MAD2. |
| GO:0000776 kinetochore (IBA + 3 IDA) | ACCEPT | Core site; mutant and Spc105-6A data show MELT(P)-dependent localization. |
| GO:0005515 x Bub1 (10 rows) | MODIFY -> GO:1990298 | Constitutive complex; HT rows get PMID:17227844 as additional ref. |
| GO:0005515 x Mad3 (6 rows) | MODIFY -> GO:0033597 (+ GO:0030674 for 17227844) | Mad3-Bub3 heterodimer is the Bub3 half of the MCC. |
| GO:0005515 x Cdc20/Mad2 (4 rows) | MODIFY -> GO:0033597 | MCC co-membership. |
| GO:0005515 x Mad1 (2 rows) | MODIFY -> GO:1990298 | Mad1 engages the Bub1-Bub3 complex via phospho-Bub1; both papers frame it that way. |
| GO:0005515 x Spc105 (24066227) | MODIFY -> GO:0140483 + GO:0051219 | The defining MF: phospho-MELT reading as kinetochore adaptor (same MF as human BUB3 review). |
| GO:0005515 x Bub1 (23267104) | MODIFY -> GO:1990298 | Reference is a S. pneumoniae MITOMI paper with no yeast content in the cached text; flagged UNVERIFIED/NONE in reference_review; interaction itself is certain. |
| GO:0005634 nucleus (IDA, IEA); GO:0005654 nucleoplasm (IBA) | ACCEPT | Closed mitosis; diffuse pool and kinetochore-independent MCC are nucleoplasmic. |
| GO:0007094 SAC signaling (IBA, 2 IDA, IMP, NAS) | ACCEPT | Core process. |
| GO:0033597 MCC (IDA + 5 IPI) | ACCEPT | Yeast MCC = Mad2-Mad3-Bub3-Cdc20 by GO definition. |
| GO:0043130 ubiquitin binding (IBA, IDA) | KEEP_AS_NON_CORE | In vitro propeller property; top face is GLEBS-occupied in vivo; no checkpoint role known. Cached text of PMID:21070969 never names Bub3 - deferred to the SGD curator rather than REMOVE. Same call as human BUB3. |
| GO:0044774 Topo II checkpoint (IGI) | KEEP_AS_NON_CORE | Partial requirement; secondary use of the SAC apparatus; matches MAD2. |
| GO:1902499 pos. reg. of autoubiquitination (IDA) | ACCEPT | Assayed entity is purified Mad3-Bub3; matches MAD3 review; caveat that Bub3 does not contact APC/C. |
| GO:1990298 Bub1-Bub3 complex (IBA, IDA, IPI) | ACCEPT | Structurally defined. |

No NEW terms proposed. GO:0034501 (protein localization to kinetochore) was considered for
core_functions but dropped to avoid asserting a term GOA does not carry; the Bub1-docking role
is expressed through GO:0140483 kinetochore adaptor activity instead.

### Core functions written

1. Kinetochore adaptor activity (GO:0140483) in the Bub1-Bub3 complex at the kinetochore,
   directly involved in GO:0007094.
2. Protein-macromolecule adaptor activity (GO:0030674) in the MCC (GO:0033597) in the nucleus,
   contributes_to ubiquitin ligase inhibitor activity (GO:1990948), directly involved in
   GO:0007094.

### Validation

`just validate yeast BUB3` -> Valid, 0 warnings (after moving GO:0030674 into a MODIFY row,
dropping GO:0034501 from core_functions, and citing the deep-research file in the
nucleoplasm IBA row). Rendered to `BUB3-ai-review.html`.

### Open items

- Whether PMID:23267104 really reports the yeast Bub1-Bub3 pair (supplementary control?) could
  not be checked from the cache.
- The Bub3 panel of PMID:21070969 (ubiquitin binding) is not in the cached text.
