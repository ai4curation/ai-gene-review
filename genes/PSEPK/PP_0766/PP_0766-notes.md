# PP_0766 (Q88PT2) notes

Dashboard protein: NZ_KZ987399.1_4512 (https://gene-annotate-dashboard.kbase.us/review/NZ_KZ987399.1_4512), P. putida, tier A, Dark-Function.
Reviewed on Q88PT2 (KT2440 PP_0766), 99.6% identical over all 454 residues (452/454). The exact-sequence UniParc entries are deleted.
Operon partner of PP_0765 (`../PP_0765/`; same strand, 25 bp intergenic). The sequence analysis script is in `../PP_0765/PP_0765-bioinformatics/analyze_pair.py`, run as BERIL run `20261030T211502Z-pp0765-pp0766-pair-analysis`.

## Conclusion

PP_0766 is a soluble periplasmic DUF1329 protein with a LolA/LolB/LppX-like fold. Its molecular function is unknown. With PP_0765 it is required for growth on long-chain fatty acid esters. No evidence shows that it sorts or targets proteins, or that it acts in adhesion.

- **Topology.**
  - Signal peptide at 1-24 (SignalP; DeepTMHMM).
  - No transmembrane segment.
  - **No cysteine anywhere in the protein**, so it has no lipobox and is not a lipoprotein. As a positive control, the lipobox regex finds LTAC in E. coli LolB.
- **Fold, not sequence.**
  - CDD cd16329 LolA_like and Gene3D 2.50.20.10 "Lipoprotein localisation LolA/LolB/LppX".
  - Global alignment to E. coli LolB or LolA is at or below the shuffled background (LolB z = -1.7, LolA z = -0.7).
  - The LolA/LppX fold also carries lipids and other hydrophobic cargo (LppX/LprG), so the fold does not imply protein cargo.
- **Orthologue.** P. aeruginosa PA3922 is 78.0% identical, is detected in OMVs, and is uncharacterized. The paralogue PP_2043 is 46.9% identical.
- **Fitness** (from the frozen dashboard evidence):
  - KT2440 Tween 20: -3.65 and -3.51;
  - KT2440 butyl stearate: -3.43 and -2.18;
  - P. fluorescens orthologues: Tween 20 defects as well.
- **Hypotheses.**
  - Esterase (PMID:32826213): untested; PP_0766 has no hydrolase motifs.
  - Periplasmic link between PP_2019 (RND/MMPL-type) and the outer membrane barrel PP_0765 in a transport system (PMID:38306398): AlphaFold-based, with weak predicted contacts.
  - The Pfam DUF1302 text says DUF1329 is a "LolA-like chaperone" of an MMPL exporter system.
  - The most coherent model is a carrier of a hydrophobic small molecule across the envelope. Its direction (import of ester or fatty acid, or export of an envelope lipid) is unknown.

## Dashboard verdict

**overreach** ("partially supported"): the pairing with PP_0765 is real and well supported, but "adhesin-associated sorting" is a hypothesis stacked on a name transfer.

Suggested corrected annotation: "DUF1329 family periplasmic protein (LolA-like fold), operon partner of the DUF1302 outer membrane protein PP_0765; required for growth on long-chain fatty acid esters; molecular function unknown."

| GO term | Code | Note |
|---|---|---|
| GO:0006605 protein targeting | UNC (1) | LolB relation is fold-only; no lipobox; Pfam and structural models imply non-protein cargo; untested |
| GO:0007155 cell adhesion | UNC (1) | reaches PP_0766 at two removes (PA3923 laminin -> PP_0765 "adhesin" -> cofitness); no adhesion data |

The GO extractor justified "protein targeting" by analogy to sortases. Sortases are unrelated Gram-positive transpeptidases.

## Caveats

- Pooled RB-TnSeq only. There are no clean deletions, no localization and no biochemistry.
- `just fetch-fitness` failed: no FEBA source was reachable.
- `just fetch-gene` hit the OLS timeout; the same ubergraph workaround as PP_0765 was used.
