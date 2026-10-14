# lag-1 (C. elegans) review notes

- UniProt: V6CLJ5 (LAG1_CAEEL), "Suppressor of hairless protein homolog" (CSL transcription factor lag-1); ORF K08B4.1; 790 aa (isoform d canonical; isoforms a-d).
- PANTHER: PTHR10665 (RECOMBINING BINDING PROTEIN SUPPRESSOR OF HAIRLESS); no subfamily listed in the UniProt record.
- Domains: RBP-J/Cbf11 DNA-binding (NTD, Rel-like), beta-trefoil domain (BTD), IPT/TIG (CTD).
- IBA node: PTN000071433 (nucleus; GO:0000981 DNA-binding TF activity, Pol II-specific; GO:0000978 cis-regulatory region sequence-specific DNA binding).

## Key findings
- LAG-1 binds RTGGGAA [PMID:8625826 "Furthermore, we show that LAG-1 binds specifically to the DNA sequence RTGGGAA, previously identified as a CBF-1/Su(H)-binding site."]
- Required for both lin-12 and glp-1 signaling; strong alleles = Lag phenotype [PMID:1769331 "Strong loss-of-function lag mutants are phenotypically indistinguishable from the lin-12 glp-1 double"]
- GLP-1 RAM binds LAG-1 directly [PMID:9003776 "the interaction between the RAM domain and LAG-1 is likely to be direct"]
- Crystal structure of worm LAG-1 on DNA; LIN-12 RAM peptide binds BTD [PMID:15297877 "Ultimately, we chose the C. elegans ortholog Lag-1 for structure determination."]
- Ternary CSL-NotchIC-Mastermind structure on DNA (worm components; Wilson & Kovall) [PMID:16530045 "Ternary complex formation induces a substantial conformational change within CSL, suggesting a molecular mechanism for the conversion of CSL from a repressor to an activator."]
- RAM binding allosterically creates Mastermind docking site [PMID:18381292]
- LAG-3/SEL-8 forms ternary complex with LAG-1 and ICD [PMID:10830967]
- Germline targets: only lst-1 and sygl-1 are primary GLP-1/LAG-1 targets; repression not general in germline [PMID:32196486 "transcriptional repression may not be a general property of LAG-1 in the germline."]
- Positive autoregulation via LBSs in a HOT-region enhancer; default repression in AC/VU [PMID:32839181 "However, our analysis suggests default repression in the AC/VU context."]
- Direct targets: lin-11 pi-cell enhancer [PMID:12074555], egl-43 [PMID:17215301], lag-1 itself [PMID:23615264], mir-57 (full text of PMID:20824072, PMC2932687: LAG-1 site needed for tail expression).

## Review decisions (summary)
- Core MF: GO:0000981 (DNA-binding TF activity, Pol II-specific); GO:0005112 Notch binding. BP: GO:0007221 positive regulation of transcription of Notch receptor target; GO:0000122 (default repression). Complex GO:1990433.
- MODIFY: regulation of gene expression (IMP, PMID:32196486) -> GO:0007221; positive regulation of DNA-templated transcription (NAS) -> GO:0007221.
- MARK_AS_OVER_ANNOTATED: egg-laying behavior (IMP PMID:12074555) - Egl is anatomical (pi cell fate), not behavioral.
- Developmental IMP/IGI terms kept as non-core; several (oocyte growth, dauer exit, nucleus IDA PMID:10903169) are from abstract-only papers not naming lag-1; deferred to curator.
- No REMOVE actions.

## Variant notes for the Notch module
- Single CSL in worm serving two receptors (LIN-12, GLP-1). Worm CSL-RAM affinity is ~2 uM vs ~30 nM for mouse (PMID:18381292), i.e. weaker RAM binding.
- No worm Hairless; corepressor partners for default repression not established.

## Deep research
- Falcon deep research completed (lag-1-deep-research-falcon.md). Consistent with the review. Additional points:
  - Notch-independent terminal selector role in ADF serotonergic neurons (Maicas et al. 2021; not in local publication cache): "LAG-1 has a striking Notch-independent role as a terminal selector in ADF serotonergic chemosensory neurons" - LAG-1 activates tph-1, cat-1, bas-1, cat-4 without GLP-1, LIN-12 or SEL-8. Relevant as a CSL-independent-of-Notch variant for the module; not added as NEW annotation here (primary paper not cached).
  - LST-1 feeds back on LAG-1 (Ferdous et al. 2023), dampening Notch-dependent transcription.
