# fur (PA4764, Q03456) notes

## Identity

- UniProt Q03456 (Swiss-Prot, PE 1), ferric uptake regulator, homodimer [UniProt CC SUBUNIT, PubMed
  12581348]. Fur family. Essential in P. aeruginosa, so studies use point mutants selected by manganese
  resistance [PMID:8885270 "Because the ferric uptake regulator (fur) appears to be an essential gene in
  Pseudomonas aeruginosa, resistance to manganese was used as an enrichment"].
- Crystal structure with Zn2+; distinct zinc and iron sites [PMID:12581348 "Here, we present the first
  crystal structure of Fur from P. aeruginosa in complex with Zn2+ determined at a resolution of 1.8 A."].

## Function

- Fe(II)-dependent repressor: purified Fur binds Fur boxes and the pvdS and pchR promoters (activators of
  pyoverdine and pyochelin synthesis), not toxA [PMID:8522528 "are specifically recognized by Fur-Fe(II)
  are presented, suggesting that PA-Fur represses expression of pchR and pvdS during growth in an
  iron-replete environment"].
- At least 24 direct targets found by SELEX-like selection [PMID:8633080 "The expression of at least 24
  distinct genes of Pseudomonas aeruginosa PAO1 is under direct control of the "ferric uptake regulator"
  (Fur)."]; haem uptake loci phu and has [PMID:10658665]; fagA-fumC-orfX-sodA operon [PMID:9045799];
  PrrF1/2 sRNAs, each preceded by a Fur box [PMID:15210934 "a functional Fur box precedes each"].
- fur point mutants overproduce siderophores; mutant Fur binds pvdS more weakly [PMID:8885270 "The A2 and
  A4 mutants expressed higher levels of siderophores in iron-deficient media and in iron-replete media."].
- fur mutants have more Mn-SOD and less catalase; Fur binds the sodA operon iron boxes [PMID:8763923].

## Annotation decisions (29 rows)

- ACCEPT: GO:0000976 (IBA + 4 CollecTF), GO:0001217 (4 CollecTF), GO:0045892 (IBA + 5 CollecTF),
  GO:1900705 (IMP seed, IBA), GO:0005829 cytosol (IBA), GO:0008198 ferrous iron binding (TAS).
- MODIFY: GO:0003700 (IBA, IEA) to GO:0001217; GO:0006355 (IEA) to GO:0045892; GO:0005737 (IEA) to
  GO:0005829; GO:0019290 siderophore biosynthetic process (CACAO IMP) to GO:1900705 (regulator, not
  biosynthetic participant).
- KEEP_AS_NON_CORE: GO:0008270 zinc ion binding (IBA, structural Zn); GO:0032993 protein-DNA complex (4
  CollecTF).
- MARK_AS_OVER_ANNOTATED: GO:1901668 regulation of superoxide dismutase activity (IMP); the effect is
  transcriptional control of sodA.

## PseudoCAP IBA-seed assessment

Fur's experimental annotations seed five node-terms (local IBD.gaf, 2026-10-28): four at PTN002112386
(the Fur superfamily: 83 leaves, including Fur, Zur, PerR, Irr, Nur/Mur-like and archaeal paralogs) and one
at PTN002112483 (12 proteobacterial Fur leaves). Only the GO:1900705 PseudoCAP row is a PseudoCAP-only
seed; the other three PTN002112386 terms are multi-seeded from CollecTF and other MOD annotations.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002112483 | GO:1900705 negative regulation of siderophore biosynthetic process | 1 (sole) | 12 (12 taxa) | GO:1900705, IMP, PMID:8885270 (PseudoCAP) | OVER-SPECIFIC | The seed is sound: Fur point mutants derepress siderophores and Fur-Fe(II) binds the pvdS/pchR promoters, so Fur itself does the regulating. But the node includes Fur of Neisseria meningitidis, Helicobacter pylori and Coxiella burnetii, not known to synthesise siderophores, so the term overreaches part of the clade (taxon/lineage mismatch). |
| PTN002112386 | GO:1900376 regulation of secondary metabolite biosynthetic process | 2 (Fur, Zur/np20) | 71 (33 taxa) | GO:1900705, IMP, PMID:8885270 (PseudoCAP) | OVER-SPECIFIC | Sound for Fur, but the node is the whole Fur superfamily; Zur, PerR, Irr and archaeal paralogs (about half the leaves) have no known secondary-metabolite role. A Fur-lineage-specific regulatory output placed at a superfamily node. |
| PTN002112386 | GO:0045892 negative regulation of DNA-templated transcription | 16 | 83 | GO:0045892, EXP/IEP, PMID:8633080 and others (CollecTF) | SOUND | Direct repression of Fur-box promoters; repression is conserved across the superfamily. |
| PTN002112386 | GO:0003700 DNA-binding transcription factor activity | 15 | 83 | GO:0001217, IPI, PMID:8633080 and others (CollecTF) | SOUND | Footprinting/EMSA on many promoters. |
| PTN002112386 | GO:0000976 transcription cis-regulatory region binding | 15 | 83 | GO:0000976, IPI, PMID:8633080 and others (CollecTF) | SOUND | Direct operator binding. |

GO_CENTRAL defects for PTN002112483 and PTN002112386 are recorded on the GO:1900705 rows (the gene
carries no GO:1900376 IBA row because it has the more specific term).
