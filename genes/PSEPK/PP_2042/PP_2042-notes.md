# PP_2042 (Q88L93) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NC_017530.1_3648` (*P. putida*, 617 aa), https://gene-annotate-dashboard.kbase.us/review/NC_017530.1_3648. It is tier A, in the Dark-Function stratum.
- The exact-sequence UniProt entries are deleted ("Not part of a reference proteome"). The review is therefore filed on the KT2440 reference-proteome entry Q88L93, which is 98.9% identical over 617/617 residues (`PP_2042-bioinformatics/results.json`).
- The dashboard call and evidence are frozen in `PP_2042-dashboard-prediction-evidence/`:
  - `dashboard_page.txt` and `dashboard_call.json` come from run `20261030T210322Z-dashboard-page-nc-017530-1-3648`;
  - `dashboard_evidence.json` is the full evidence record from `user_data/dashboard_calls/`.
- Operon partner: PP_2043 (DUF1329), which is reviewed in `../PP_2043/`. The paralogous pair PP_0765/PP_0766 is reviewed separately by another agent.

## Conclusion

PP_2042 is a DUF1302 outer-membrane beta-barrel protein of **unknown function**.

- **Location is well predicted.** It has a SignalP signal peptide (1–27), and DeepTMHMM predicts an 18-strand outer-membrane barrel. Structural surveys of DUF1302 also class the family as transmembrane beta-barrels (PMID:37432995, PMID:42605071).
- **Gene context.** It is encoded in an apparent operon, PP_2042–PP_2043–PP_2044, with a divergent LysR regulator (PP_2041). The upstream genes are fatty-acid related.
- **Molecular function, cargo or ligand and process are unknown.**

## Dashboard verdict: overreach

The call was "Putative laminin-binding outer membrane adhesin (DUF1302 family)."

**Corrected annotation:** "DUF1302 family outer membrane beta-barrel protein of unknown function; co-encoded with DUF1329 periplasmic protein PP_2043."

**Is "laminin-binding" supported by anything other than name transfer? No.**

1. The only source is *P. aeruginosa* PA3923 (Paulsson et al. 2019, PMID:31796854). It binds laminin in vitro and is an outer-membrane laminin receptor. PA3923 is the **reciprocal best hit and 76.9%-identical ortholog of the paralog PP_0765**. PP_2042 is only 52.2% identical to PA3923, 51.9% to PA3422 and 53.1% to PP_0765. It is therefore a separate, uncharacterized DUF1302 subfamily.
2. The Fitness Browser reannotation "putative adhesin (DUF1302)" is attached to **PP_0765 only**. It is itself a name transfer from PA3923.
3. The KT2440 fitness row the annotator saw (48.4% identity, Tween 20, fit −4.06) is **PP_0765**, not PP_2042.
4. Laminin is a vertebrate basement-membrane protein, and the binding was shown for a pathogen. Nothing ties it to a soil-bacterium paralog.

**GO terms:**
- GO:0043236 laminin binding: **PLI** (paralog over-annotation).
- GO:0007155 cell adhesion: **UNC**.
- GO:0009279 cell outer membrane: **COR**.

## Fitness (KT2440, BERDL `kescience.fitnessbrowser`)

- `just fetch-fitness` failed because no FEBA source was reachable: fit.genomics.lbl.gov returns 403 and there is no local feba.db. The data were pulled from BERDL Spark instead (run `20261030T211615Z-pp2042-pp2043-pair-analysis`).
- **PP_2042:** 300 experiments, fitness range −0.42 to +0.46, no strong or specific phenotypes.
- **PP_0765/PP_0766:** strongly required on Tween 20 and butyl stearate (fit to −4.1).
- **Fitness-profile correlation:** PP_2042 vs PP_2043 r = 0.098; PP_0765 vs PP_0766 r = 0.951.
- PP_2042's top cofitness hits are all below 0.31.

## What is known about DUF1302/DUF1329 in any organism

- **PA3923 (*P. aeruginosa*).** An outer-membrane laminin receptor (PMID:31796854). It contributes to biofilm on laminin-coated plates (PMID:33758032). It is reduced in the outer membrane of a SurA-depleted strain (PMID:30846971; see the dashboard PaperBLAST text).
- **AmeA and AmeB (*Castellaniella defragrans*).** AmeA (DUF1302) and AmeB (DUF1329, predicted periplasmic, LolA superfamily) are part of the inducible AmeABCD cassette with a BNR protein and an HAE3 RND transporter. The cassette is required for growth at high monoterpene concentrations, and the individual roles were not dissected (PMID:30334144). This is the best-supported model for the family: an envelope export system for hydrophobic compounds.
- **The same pattern in KT2440.** PP_0765/PP_0766 are cofit with the BNR protein PP_2018 and the RND transporter PP_2019. PP_2810–PP_2813 form a complete Ame-like cassette.
- **No RND or BNR at the PP_2042 locus.**
- **Esterase hypothesis.** Thompson et al. 2020 (PMID:32826213) proposed esterase activity from the PP_0765/PP_0766 phenotypes. Neither DUF has a hydrolase motif.

## Signal peptide, lipobox, beta-barrel

- **Signal peptide:** SignalP 1–27.
- **Lipobox: none in KT2440.** Q88L93 has Gly26.
  - The dashboard sequence has Cys26 in the context A-S-A-C, which does not fit the [LVI][ASTVI][GAS]C consensus.
  - The PS51257 hit on the page has E = 5, which is not significant.
- **Beta-barrel:** DeepTMHMM predicts an 18-strand barrel, and the protein ends in an aromatic C-terminal Phe.

## Caveats

- PP_2042 itself has not been studied experimentally. Its location is predicted, not observed.
- The absence of a phenotype may only mean the operon is not expressed under the conditions tested.

## Tooling notes

- **`just fetch-gene` failed on the OLS taxon-label lookup** (www.ebi.ac.uk timed out). The UniProt and GOA files were written, but the ai-review stub was not, so it was hand-written. GOA is empty.
- **`just fetch-fitness` could not reach any FEBA source.** BERDL access works from this host with `/opt/conda/bin/python` (berdl_notebook_utils). `run_sql.py` failed because spark_connect_remote is missing.
- **The EBI InterPro API was unreachable,** so no Pfam clan or description was fetched directly. The Pfam DUF1302 description quoted in the deep-research report is unverified here.
- **The deep-research report for PP_2043 says UniProt lists CDD and Gene3D LolA-like cross-references.** The local UniProt file has only InterPro and Pfam, so that claim was not used.
- **`validate-predictions` writes `reports/prediction-evidence.json`,** a shared file.
