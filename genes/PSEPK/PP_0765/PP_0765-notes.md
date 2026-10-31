# PP_0765 (Q88PT3) notes

Dashboard protein: NZ_NBWA01000007.1_52 (https://gene-annotate-dashboard.kbase.us/review/NZ_NBWA01000007.1_52), P. putida, tier A, Dark-Function.
Reviewed on Q88PT3 (KT2440 PP_0765), 98.7% identical over all 628 residues (620/628). The exact-sequence UniParc entries are deleted ("Not part of a reference proteome").
Reviewed together with its operon partner PP_0766 (`../PP_0766/`). The paralogous pair PP_2042/PP_2043 is reviewed separately by another agent.

## Conclusion

PP_0765 is a DUF1302 outer membrane beta-barrel protein, and its molecular function is unknown. Its one experimental phenotype is in KT2440: with PP_0766 it is required for growth on the long-chain fatty acid esters Tween 20 and butyl stearate, but not on the free fatty acids. "Laminin-binding adhesin" is a chain of name transfers, and nothing in P. putida supports it.

- **Topology.** SignalP and DeepTMHMM put a signal peptide at 1-29. DeepTMHMM also predicts an 18-stranded beta-barrel. The Pfam PF06980 description reads "predicted outer membrane beta barrel proteins ... likely part of an exporter system that includes an MMPL exporter, a DUF1329 ... LolA-like chaperone" (saved in `PP_0765-bioinformatics/pfam_descriptions.txt`).
- **Orthologue.** P. aeruginosa PA3923 is 76.9% identical over 624 aligned residues. The paralogue PP_2042 is 52.4% identical. Numbers are from BERIL run `20261030T211502Z-pp0765-pp0766-pair-analysis`.
- **Laminin.** PMID:31796854 found that recombinant PA3923 binds human laminin-111 (KD 6.9 nM), and a PA3923 Tn mutant adheres less to laminin. In the same assay, the porins OprD and OprG, the esterase EstA and the ABC SBP Paf all bound equally tightly, all through the heparin-binding LG4/LG5 domains. This looks like a generic polycationic-site interaction rather than a dedicated receptor. PMID:33758032 reports less biofilm on laminin-coated plates for PA3923 mutants.
  - The Fitness Browser "putative adhesin (DUF1302)" reannotation of PP_0765 is a transfer from PA3923; its stated rationale cites only those two papers. So the dashboard's two "independent" lines of evidence (the PA3923 papers and the curated homolog) are a single line.
- **KT2440 fitness** (from the frozen dashboard evidence, because Fitness Browser was unreachable):
  - Tween 20: -4.06 and -3.74;
  - butyl stearate: -3.03 and -2.07.
  - Orthologues in P. fluorescens and P. stutzeri show defects on Tween 20 and with quaternary ammonium biocides (benzethonium, benzalkonium).
  - Thompson et al. 2020 (PMID:32826213; I read the abstract, plus a web-fetch summary of the bioRxiv preprint) list PP_0765, PP_0766, PP_0767 (LuxR), PP_2018 (BNR) and PP_2019 (RND) as specific to Tween 20 versus laurate. They hypothesize, without testing, that DUF1302/DUF1329 are esterases, and note an alternative: export of an envelope component. A secreted esterase would be a public good in a pooled assay, which argues against it.
- **Structure prediction.** Foldy (PMID:38306398) models PP_0765 as an outer membrane beta-barrel with weak predicted contacts to periplasmic PP_0766. With PP_2019 it proposes "a novel transport system".

## Dashboard verdict

**overreach** ("partially supported"): the outer membrane beta-barrel part is right, but the laminin-binding adhesin part is unsupported for KT2440.

Suggested corrected annotation: "DUF1302 family outer membrane beta-barrel protein; with PP_0766 required for growth on long-chain fatty acid esters (Tween 20, butyl stearate); molecular function unknown."

| GO term | Code | Note |
|---|---|---|
| GO:0043236 laminin binding | UNC (1) | in vitro binding by the 77% orthologue only; physiologically implausible in a soil saprophyte, but not refuted |
| GO:0007155 cell adhesion | UNC (1) | orthologue laminin adherence and biofilm only; no P. putida adhesion data |
| GO:0019867 outer membrane | COR (2) | GOA empty; the review uses the child term GO:0009279 cell outer membrane |

The annotator saw the fatty ester fitness and set it aside ("do not establish transport or catalytic activity"). It then kept a host-matrix function that has even less in-organism support.

## Caveats

- No P. putida experiment other than pooled RB-TnSeq. There are no clean deletions, no complementation and no localization.
- The full text of PMID:32826213 was not machine-readable. The preprint statements are paraphrased here and not quoted in the YAML.
- `just fetch-fitness` failed: "no FEBA data source was reachable". The fitness values come from `PP_0765-dashboard-prediction-evidence/dashboard_call.json`.
- `just fetch-gene` failed at the OLS taxon-label lookup (EBI read timeout). The stub was seeded by calling `fetch_gene_data` with `ncbitaxon_label` routed to `ubergraph:`, as for yxcA.

## Files

- `PP_0765-ai-review.yaml`, `PP_0765-dashboard-predictions-review.yaml`
- `PP_0765-bioinformatics/`: `analyze_pair.py`, `uniprot_seqs.fasta`, `pair_results.json` and `pfam_descriptions.txt`, shared with PP_0766.
- `PP_0765-dashboard-prediction-evidence/`: the frozen dashboard call, the page and the pair results.
