# TRX2 (P22803, YGR209C) notes

- Cytoplasmic thioredoxin, paralog of TRX1 (78% identity) [PMID:1988444 "Thioredoxins I and II show 78% amino acid sequence identity"]
- Induced by H2O2/diamide via Yap1/Skn7; inactivates Yap1 [UniProt:P22803 "Strongly induced by hydrogen peroxide and diamide stress in a YAP1- and SKN7-dependent manner."]
- PAPS reductase cosubstrate [PMID:3060034 "Reduced thioredoxin is required as cosubstrate"]; double mutant Met auxotroph [PMID:2026619 "the loss of both thioredoxins also leads to methionine auxotrophy"]
- GSSG reduction backup to Glr1 [PMID:23242256 "we identify Trx2 and Grx2 as efficient backup systems to glutathione reductase for cytosolic GSSG reduction"]
- Yvc1 deglutathionylation mainly by Trx2 [PMID:27708136 "we observed that the trx2∆ mutant, and to a lesser extent the trx1∆ mutant, showed increased glutathionylation"]
- Deglutathionylase activity [PMID:20074363]; overlapping redox homeostasis [PMID:22561702]
- LMA1 subunit (shared with Trx1) [PMID:9015301, PMID:9657146, PMID:8603912]

## Decisions
- Core: GO:0015035 cytosol/nucleus; BPs cell redox homeostasis, deglutathionylation, sulfate assimilation (IGI accepted); LMA1 complex as separate core function.
- Golgi membrane IEA (UniProt citing Huh 2003, abstract only) UNDECIDED. Protein binding removed.
- Glutathione metabolic process IGI kept non-core.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 31 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

The sulfate-assimilation role overlaps Trx1 under standard tested conditions; the double mutant phenotype is not universal proof that no other donor can ever work. PMID:10844700 establishes conditional bypass under low-oxidant conditions and leaves the alternative donor unidentified. The former glutaredoxin-dependent-backup wording is corrected. Disulfide-reductase activity retains glutathione-disulfide as well as protein substrate scope (PMID:23242256); glutathione homeostasis, Yvc1 deglutathionylation (PMID:27708136), redox stress, and LMA1 transport roles were considered independently. Genetic redundancy and curated complex evidence support Trx2 in LMA1; redox-inactive cysteine-mutant rescue in PMID:9015301 was performed with Trx1, not Trx2. The Golgi claim remains UNDECIDED because the available localization evidence does not resolve it; no misattribution is inferred from an incomplete source. No new row is added.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids yeast TRX2` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-yeast-TRX2-*.log`.
