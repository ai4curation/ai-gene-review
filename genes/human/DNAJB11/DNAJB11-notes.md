# DNAJB11 (ERdj3 / HEDJ / ERj3p) research notes

UniProt: Q9UBS4. 358 aa, precursor (signal 1-22), J-domain 25-90. ER-lumenal HSP40/J-protein.
Soluble, glycosylated (N-261), disulfide-bonded Cys-rich domain. Paralog within DNAJB but ER-resident.

## Core function: BiP (HSPA5) co-chaperone in ER lumen
- [UniProt FUNCTION "As a co-chaperone for HSPA5 it is required for proper folding, trafficking or
  degradation of proteins... Binds directly to both unfolded proteins that are substrates for ERAD and
  nascent unfolded peptide chains... Stimulates HSPA5 ATPase activity... necessary for maturation and
  correct trafficking of PKD1."]
- [PMID:18923428 "DnaJ proteins often bind to unfolded substrates and recruit their Hsp70 partners...
  BiP promoted the release of ERdj3 only in the presence of ATP... a functional interaction between
  ERdj3 and BiP, including both a direct interaction and the ability to stimulate BiP's ATPase
  activity are required to release ERdj3 from substrate"]. ERdj3 binds substrate first, recruits BiP,
  stimulates BiP ATPase.
- GOA: GO:0032781 positive regulation of ATP-dependent activity IDA PMID:20335166 (= stimulates BiP
  ATPase). GO:0051787 misfolded protein binding IDA PMID:28597544 + IBA. GO:0051604 protein maturation
  IMP PMID:29706351 + IBA.

## Substrate binding domain
- Binds denatured substrates ATP-independently via Cys-rich domain (Cys169/171/193/196 mutations
  abolish substrate binding, PMID:17976514). H53Q (J-domain HPD) abolishes BiP binding but not
  substrate binding (PMID:15525676).

## ER chaperone complex
- Part of large ER chaperone complex: DNAJB11, HSP90B1, HSPA5, HYOU1, PDIA2/4/6, PPIB, SDF2L1, UGGT1
  (UniProt SUBUNIT; PMID:12475965). GOA part_of GO:0101031 protein folding chaperone complex IPI
  PMID:28597544 (with SDF2/SDF2L1 Q99470/Q9HCN8). GO:0034663 ER chaperone complex IEA.

## Disease: ADPKD (PKD6)
- [PMID:29706351 "Monoallelic Mutations to DNAJB11 Cause Atypical Autosomal-Dominant Polycystic Kidney
  Disease"]; [PMID:29706351 "DNAJB11 is a co-factor of BiP... maturation and trafficking defects
  involving the ADPKD protein, PC1, and ADTKD proteins, such as UMOD."]. Phenotype = hybrid ADPKD/ADTKD.

## Localization — ER lumen (core). Conflicting IEA over-annotations to flag:
- ER lumen/ER: well established (UniProt, IDA HPA, TAS Reactome). CORE.
- Ensembl ortholog-projected (GO_REF:0000107) extracellular (GO:0005576), nucleus (GO:0005634),
  cytoplasm (GO:0005737), signaling receptor binding (GO:0005102) — these CONFLICT with the
  signal-peptide-driven ER-lumen targeting. UniProt CAUTION: cytosolic/nuclear localization was an
  artifact of N-terminal GFP tag disrupting signal peptide; APOBEC1/PWP1 interactions dubious.
  => MARK_AS_OVER_ANNOTATED for extracellular/nucleus/cytoplasm/signaling-receptor-binding.
- GO:0016020 membrane HDA PMID:19946888 (NK membrane proteome) — UniProt notes ER-membrane
  association only with C-terminally tagged construct; ERdj3 is a soluble ER-lumen protein. KEEP_AS_NON_CORE.

## Protein-binding IPIs
- HSPA5/BiP (P11021): the functionally meaningful one (PMID:18923428, 24189400, 28514442, 33961781,
  20335166). KEEP_AS_NON_CORE bare protein binding but reflects core BiP interaction.
- SIMC1 (Q8NDZ2), HTN3 (P15516 histatin-3), SlrP (Q8ZQQ2 Salmonella, xeno): HT/substrate. NON_CORE.

## MF assignment
- Core MF: GO:0001671 ATPase activator activity (stimulates BiP ATPase) — UniProt-supported.
- Core MF: GO:0051787 misfolded protein binding (IDA) / GO:0051082 unfolded protein binding (IBA) /
  GO:0140309 unfolded protein holdase activity — substrate (holdase) binding.
- GO:0006457 protein folding, GO:0051604 protein maturation: downstream BP, core process for ERdj3
  given disease relevance (protein maturation IMP is genuine). Keep protein maturation as ACCEPT/core process.
