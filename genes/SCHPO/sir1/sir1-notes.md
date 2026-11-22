# sir1 (SPAC10F6.01c, UniProt Q1K9C2) notes

Naming trap: PomBase `sir1` is the sulfite reductase beta (hemoprotein) subunit, the
ortholog of S. cerevisiae MET5/ECM17 (UniProt entry MET5_SCHPO). It is unrelated to
S. cerevisiae SIR1 (silent information regulator). In pombe, met10 (SPCC584.01c) is the
alpha flavoprotein partner.

## Evidence journal

- Activity: sulfite reductase (NADPH), sulfite + 3 NADPH -> H2S (EC 1.8.1.2, RHEA:13801), by
  similarity to MET5 [UniProt:Q1K9C2 "FUNCTION: Catalyzes the reduction of sulfite to sulfide,
  one of several"]; siroheme and [4Fe-4S] cofactors by similarity to E. coli CysI
  [UniProt:Q1K9C2 "Note=Binds 1 siroheme per subunit."]; alpha2beta2 by similarity
  [UniProt:Q1K9C2 "SUBUNIT: Alpha(2)-beta(2). The alpha component is a flavoprotein, the"].
- Domains: flavodoxin-like FMN domain (Pfam PF00258, ~728-876), nitrite/sulfite reductase
  ferredoxin-like (PF03460 x2) and 4Fe-4S/siroheme (PF01077) domains; [4Fe-4S]/siroheme Cys
  ligands at 1328, 1334, 1373, 1377 [UniProt:Q1K9C2]. As for S. cerevisiae MET5, the FMN
  flavodoxin domain sits on the beta subunit, not on the alpha flavoprotein.
- Localization: cytoplasm/cytosol in the ORFeome YFP screen (PMID:16823372).
- GOA IMP for sulfate assimilation cites PMID:10224084 (hmt2 sulfide:quinone oxidoreductase
  paper; abstract-only cache does not mention sir1). Curator saw full text; the process is
  certainly correct for sulfite reductase. Deferred.
- Indirect pombe evidence: sulfite reductase activity is a labile cytosolic Fe-S enzyme
  activity that falls in gpx1 mutants [PMID:18162174 "Activity of sulfite reductase, a
  labile Fe-S enzyme in the cytosol, was also dramatically lowered in the mutant in the
  stationary phase."].
- PomBase GO-CAM gomodel:66a3e0bb00001342 activity 66a3e0bb00001438: sir1 enables GO:0004783
  in cytosol, part_of GO:0000103 (met10 is a separate GO:0004783 activity, 66a3e0bb00001449).
- Module: aps_dependent_assimilatory_sulfate_reduction, sulfite reduction step, fungal
  Met10/Met5 variant (met5_hemoprotein_subunit). S. cerevisiae MET5 core function:
  contributes_to GO:0004783, in_complex GO:0009337, cytoplasm; consistent here.

## Observations
- GO-CAM models sir1 and met10 each as independently enabling GO:0004783; the GOA IBA uses
  contributes_to. contributes_to + complex is the more accurate representation of a
  heteromeric enzyme; the module already notes this discrepancy.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 16 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

Sir1 supplies the sulfite-reducing siroheme/[4Fe-4S] module to the assembled enzyme, with alpha-subunit electron input. The broad Fe-S binding term is refined to the supported [4Fe-4S] site. A positive PF00258/Flavodoxin_1 match at residues 728–876 supports inferred FMN binding; the holoenzyme FMN assay is from budding yeast (PMID:6751400), not isolated native Sir1. PMID:11319255 uses old S. pombe O14167; mapping that historical accession to Q1K9C2 has not been independently completed and is not silently assumed. PMID:10224084 foregrounds Hmt2 in the abstract, which does not establish that sir1 controls or mutants were absent from the full text. The biologically supported native sulfite-reduction claim is retained with curator deference, not falsely removed as misattributed. All localization and secondary phenotype rows were considered.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids SCHPO sir1` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-SCHPO-sir1-*.log`.
