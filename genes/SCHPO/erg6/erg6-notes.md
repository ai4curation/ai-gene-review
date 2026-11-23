# erg6 (SPBC16E9.05; UniProt O14321) notes

- Fetched accession verified O14321 (ERG6_SCHPO). Sterol 24-C-methyltransferase, Erg6/SMT family [UniProt:O14321 "Erg6/SMT family"].
- Reaction: [UniProt:O14321 "Reaction=zymosterol + S-adenosyl-L-methionine = fecosterol + S-"]; UniProt also lists lanosterol -> eburicol [UniProt:O14321 "Reaction=lanosterol + S-adenosyl-L-methionine = eburicol + S-adenosyl-"] based on [PMID:8586261 "the transmethylation process on the C-24 may occur directly on lanosterol and not only on zymosterol"] (inference from sterol profiles, not an enzyme assay). GO has no lanosterol 24-C-methyltransferase term; GO:0003838 is defined on zymosterol.
- Deletion: [PMID:18310029 "Disruption mutants of these genes were unable to synthesize ergosterol"]; [PMID:23145048 "On the other hand, in Δerg6 cells, Δerg31Δerg32 cells, and Δerg5 cells, the ergosterol levels were extremely lower than that in wild-type cells"]; erg6 deletion strongly raises lanosterol [PMID:23145048 "lanosterol levels in Δerg6 cells were about 136 folds higher"] - consistent with the lanosterol-methylation branch being blocked.
- Localisation: ORFeome called nucleus (UniProt: "Nucleus {ECO:0000269|PubMed:16823372}"), ER only inferred. Kept nucleus as non-core (cannot check images; possibly nuclear envelope/ER). Budding-yeast Erg6 is ER + lipid droplet.
- Induction by Sre1 under anaerobiosis [PMID:16537923 "Oxygen-requiring biosynthetic pathways for ergosterol, heme, sphingolipid, and ubiquinone were primary targets of Sre1p."].
- Budding-yeast ERG6 review: core GO:0003838, LD + ER. S. pombe core location set to ER only (no LD evidence in fission yeast).
- GO-CAM 66c7d41500002088: erg6 GO:0003838 in ER, -> erg2. Agrees.
- 2026-11-06 PTHR44068 re-review: refreshed UniProt from entry version 160
  to 161; the only functional-adjacent drift was UniProt's `GO:0003838
  sterol 24-C-methyltransferase activity` cross-reference changing from a
  UniProtKB-EC IEA to the current GO_Central IBA, plus an OMA xref change.
  Re-checked the PTN002226525 sterol-SMT and PTN000802684 fungal Erg6 PAINT
  nodes against the `PTHR44068` family review. The S. pombe IBAs for sterol
  24-C-methyltransferase activity, ER location, and ergosterol biosynthesis
  remain sound; newer web/PubMed searches did not find a newer direct
  fission-yeast Erg6 enzyme-assay or localization paper.
