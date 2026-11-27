# VC_0072 (Q9KVR7) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_JAACMT010000013.1_13` (*Vibrio cholerae*, 785 aa), https://gene-annotate-dashboard.kbase.us/review/NZ_JAACMT010000013.1_13
- Strata: Human Pathogen, Core, Annotation-Promoted; homologs only in its own genus. Prior names: eggNOG "PAS fold", InterPro "EAL domain".
- Mapping (`runs/20261030T212629Z-finalize-vibch-mapping`): Q9KVR7 (N16961), 99.7% identity over 768 aligned residues (97.6% over the query length), not an exact match.
- Gene model: the dashboard sequence has an 18-residue in-frame upstream segment (`MKLKCAYFTTIKTIGLTL`). UniProt Met1 corresponds to dashboard Leu18, so the N16961 model uses a non-ATG start and the draft-genome caller chose an upstream ATG. The aligned region also has two substitutions: V84/A67 in the TM helix and E381/D364 just before the GGDEF domain. Which start is used in vivo is unknown, and the difference does not touch any domain.
- DeepTMHMM on the dashboard sequence: SP 1-50, TM 78-96, cytoplasmic 97-785. UniProt (Phobius) predicts TM 57-79 and also flags a PROSITE lipobox at C25. That lipobox is probably spurious, given the TM helix that follows.

## Dashboard call under review

> Inner-membrane-associated c-di-GMP-binding protein containing PAS, GGDEF, and EAL domains. (Tier A; GO:0035438 cyclic-di-GMP binding, GO:0005886 plasma membrane)

Verdict: **supported, but conservative**.
- GO:0035438 is COR. Lysate DRaCALA on the N16961 ORF showed binding specific for c-di-GMP over GTP and cGMP (PMID:26506097).
- GO:0005886 is CNN, because GOA already has it as IBA.
- The call's evidence text says it rejected a DGC/PDE annotation because catalytic activity was not established. That is true, but the motif analysis shows both catalytic signatures intact, and GOA already has the PDE term as IBA. "c-di-GMP binding" is the measured property. The more informative description is "probable c-di-GMP phosphodiesterase, possibly bifunctional DGC/PDE".
- Paralog flag: the STRING partners include the GGDEF-EAL paralogs MbaA (VC0703) and VC0658. The call did not transfer any paralog-specific function such as MbaA's role in biofilm/NspS signalling.

## Literature

- PMID:26506097 (Roelofs et al. 2015) is the only biochemical observation. Lysates of E. coli expressing VC0072 bound c-di-GMP (Table 1), and the authors attribute the binding to the EAL domain because there is no I-site. The deep-research report says the protein was "purified"; that is wrong, because the screen used lysates.
- PMID:29463743 (Cakar et al. 2018): VC0072 is an in vivo repressed (ivr) gene. Constitutive expression did not reduce in vivo colonization relative to in vitro, though it attenuated growth in vitro and destabilized the plasmid.
- PMID:22802636 (Massie et al. 2012) studied 7 selected DGCs. Full text was unavailable, so I could not check whether VC0072 was among them, and it is not cited.
- PMID:24490592 (Hunter et al. 2014) does not mention VC0072 in its text; any VC0072 data would be in a figure only.
- PMID:18708497 (Fong & Yildiz 2008): PaperBLAST snippets show VC0072 in its strain list (a crp VC0072 lacZ fusion). The cached full text has no VC0072 data, so it is not cited.
- No deletion phenotype, enzyme assay or localization data were found for VC0072.

## Bioinformatics

`VC_0072-bioinformatics/`: regex motif check, run as `beril run` `20261030T213409Z-vc0072-motifs`. Positions are in UniProt numbering.
- GGDEF domain: GGDEF 417, DLD 376 and HDAGD 389 are present. There is no RxxD at the I-site position.
- EAL domain: EVLVR 548, INLS 606, EITE 639, DDFGSG 669, KID 690 and EFVE 726 are present.

This was motif matching only, with no structural alignment to a characterized enzyme. An earlier run, `20261030T213353Z-vc0072-motifs`, produced no outputs because of a quoting error, which wrote a stray `$BERIL_RUN_DIR` directory into `projects/hackathon/`. That directory was deleted right away. Ignore that run.

## Tooling notes

- `just fetch-gene-pmids`: no PMIDs, since the GOA rows are all IBA.
- `just fetch-fitness VIBCH VC_0072`: failed. There is no local FEBA data for VIBCH and the bulk download failed (`recipe fetch-fitness failed on line 900`).
- `just deep-research-claude-code`: completed, with an "agentapi not found" warning.
- `just fetch-pmid 24490592` failed once and then succeeded on retry.
- I mistakenly fetched an unrelated PMID (24555839) and deleted it from `publications/`.
- `just validate-terms` on the predictions sidecar fails: `No such slot locus_tag as an attribute of GeneReview`. The recipe validates against the GeneReview class, not PredictionReview. The terms are covered by `just validate-predictions`, which runs `validate-prediction-terms` and passes.
- The first `just validate` failed because I had dropped one IBA with/from entity (Q9HYT3) when rewriting the YAML. I restored it.
