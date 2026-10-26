# met10 (SPCC584.01c, UniProt Q09878) notes

Naming: UniProt Q09878 has no gene name (only ORF SPCC584.01c), so `just fetch-gene SCHPO met10`
failed; fetched with `-u Q09878`. PomBase symbol met10, ortholog of S. cerevisiae MET10
(sulfite reductase alpha, flavoprotein). Partner beta subunit in pombe is sir1 (MET5 ortholog).

## Evidence journal

- Activity: NADPH-sulfite reductase flavoprotein component, EC 1.8.1.2 by similarity
  [UniProt:Q09878 "FUNCTION: This enzyme catalyzes the 6-electron reduction of sulfite to"].
- Domains: N-terminal pyruvate-flavodoxin oxidoreductase-like region (IPR002869,
  IPR009014), CysJ-like FAD-binding (PF00667) and FNR-type NAD(P)-binding (PF00175) modules;
  FAD-binding FR-type domain 622..852 [UniProt:Q09878]. No flavodoxin (FMN) domain is
  detected (no IPR001094/IPR008254/PF00258), mirroring S. cerevisiae MET10, whose FMN domain
  is absent and found instead on MET5 (sir1 here has PF00258).
- UniProt lists FMN as cofactor "by similarity" [UniProt:Q09878 "Note=Binds 1 FMN per
  subunit. {ECO:0000250};"], presumably from CysJ; not supported by the domain content.
- Localization: cytosol (ORFeome YFP, PMID:16823372).
- No pombe-specific experimental functional data for met10 in GOA; ISO rows are transfers
  from S. cerevisiae MET10 (SGD:S000001926).
- PomBase GO-CAM gomodel:66a3e0bb00001342 activity 66a3e0bb00001449: met10 enables GO:0004783
  in cytosol, part_of GO:0000103.
- Module: aps_dependent_assimilatory_sulfate_reduction, met10_flavoprotein_subunit of the
  fungal Met10/Met5 variant. S. cerevisiae MET10 core: contributes_to GO:0004783, in_complex
  GO:0009337, cytoplasm, sulfate assimilation + H2S biosynthesis. Consistent here.

## Observations
- FMN binding IBA (from the diflavin reductase node PTN000453956: P450 reductase, NOS, MSR)
  is an over-propagation to a member that lost the flavodoxin domain: REMOVE, as for MET10.
- PANTHER places met10 in PTHR19384 (nitric oxide synthase-related) SF109 (sulfite reductase
  flavoprotein component), the same subfamily as S. cerevisiae MET10.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 11 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

The alpha subunit contributes the NADPH/FAD electron-input portion of the sulfite-reductase complex. Exact fungal subunit architecture is inferred from conserved domains and budding-yeast primary studies, not claimed as purified native fission-yeast holoenzyme measurements. FMN binding on alpha remains rejected with the existing PTHR19384 fungal-subfamily adjudication: positive PF00258 flavodoxin-domain evidence is on Sir1, whereas met10 lacks that module. PMID:11319255 full text contains an old S. pombe sequence identifier; its mapping to current Sir1 Q1K9C2 was not independently established, so the current Sir1 domain record remains the target-specific computational support. The competing broad UniProt cofactor inference is acknowledged rather than attributed to a guessed donor. Native experimental annotations are not removed from incomplete abstracts.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids SCHPO met10` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-SCHPO-met10-*.log`.
