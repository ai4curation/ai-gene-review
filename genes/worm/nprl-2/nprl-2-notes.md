# nprl-2 review notes

- 2026-10-28: Created review. fetch-gene resolved UniProt W6RQZ3 (WormBase
  WBGene00018635, GeneID 177532) as requested; GOA has 6 rows (5 IBA, 1 ARBA IEA).
  No deep-research API keys; manual survey in `nprl-2-deep-research-manual.md`.
- Key worm paper PMID:23705068 (full text): nprl-2 RNAi suppresses elo-5 L1 arrest
  [PMID:23705068 "nprl-2 dsRNA injection also rescued 42.4% of elo-5(−) animals to or
  beyond L3 stage (n = 128)."]. TORC1 epistasis was done with nprl-3, not nprl-2.
- Molecular function and location are ortholog-derived (human GATOR1:
  PMID:23723238, PMID:29590090, PMID:28199306; fly PMID:24786828).
- Decisions:
  - GTPase activator activity (contributes_to, IBA): ACCEPT; correct qualifier for a
    subunit of a complex whose GAP activity is executed by the NPRL2-NPRL3 heterodimer.
  - vacuolar membrane (IBA): MODIFY to lysosomal membrane (metazoan vacuole =
    lysosome; human and fly orthologs lysosomal). No worm localization data.
  - negative regulation of TORC1 signaling (IBA, IEA): ACCEPT; supported by worm
    genetics (nprl-2 RNAi phenocopies nprl-3, whose suppression is TORC1-dependent).
  - cellular response to amino acid starvation (IBA): KEEP_AS_NON_CORE; conserved
    family role, untested in worm.
  - GATOR1 complex (IBA): ACCEPT.
- Not proposed as NEW: L1 larval development / autophagy regulation terms. These rest
  on RNAi phenotypes only (PMID:23705068, PMID:30192747) and are downstream outcomes of
  TORC1 regulation, so they fail the NEW-term bar.
- Open: whether C. elegans has a KICSTOR equivalent to recruit GATOR1 to lysosomes; and
  whether the NPRL2 arginine finger is retained in worm NPRL-2 (not checked here).
