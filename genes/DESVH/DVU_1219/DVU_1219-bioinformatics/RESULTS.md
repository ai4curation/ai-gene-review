# DVU_1219 (Q72CR4) bioinformatics results

Query: Q72CR4 (DVU_1219, *Nitratidesulfovibrio vulgaris* Hildenborough, 731 aa). The dashboard
protein NZ_CABHLV010000001.1_902 differs from it at one residue (V393M).
All numbers below come from the files under `results/`; the BERIL run logs are copied into
`results/logs/`. Runs (project `hackathon`): `20261031T001842Z-dvu1219-interproscan`,
`20261031T002441Z-dvu1219-cazy-domains`, `20261031T002410Z-dvu1219-foldseek`,
`20261031T002306Z-dvu1219-fitness`.

## 1. Domains (InterProScan 5.78-109.0, EBI)

Only two member databases return a match:

- Phobius: signal peptide 1-40, non-cytoplasmic 41-731
- SUPERFAMILY SSF51445 (Trans)glycosidases 123-583, E = 2.77e-07 (IPR017853)

There is no Pfam, CATH-Gene3D, PANTHER, NCBIfam, PROSITE or CDD match.

Lipobox: residues 39-42 are LAGC, matching the bacterial lipoprotein consensus
[LVI][ASTVI][GAS]C; Cys42 is the candidate acylated Cys of a signal peptidase II-processed
lipoprotein (sequence motif only; no LipoP/SignalP 6 run).

## 2. CAZy family (dbCAN v5.2.9 HMMs) and Pfam without gathering thresholds

`results/domains/domains_results.json`, run `dvu1219-cazy-domains`.

- dbCAN: the only CAZy hit is GH13_33.hmm, query 143-459, HMM 2-322 of 325, score 167.4, i-Evalue 1.81e-50
- Full Pfam-A scan: no domain with independent E-value <= 10
- No CBM model hits (no CBM20/CBM48 or other CBM in dbCAN at E <= 10)
- Forced alignment to the generic GH13 profiles covers only the N-terminal barrel strands:
  Pfam PF00128 Alpha-amylase query 183-214, score -0.4; dbCAN GH13 query 143-211, score 9.3

GH13_33 profile states at the query residues that the structural alignments (section 3) place
at the GH13 catalytic positions:

| Query residue | GH13_33 state | consensus | top emission | P(query residue) |
|---|---|---|---|---|
| E351 (nucleophile position) | 212 | d | D 0.472 | E 0.089 |
| R391 (acid/base position) | 257 | e | E 0.424 | R 0.038 |
| D456 (transition-state Asp position) | 322 | d | D 0.446 | D 0.446 |

GH13_33 nucleophile state: consensus D (P = 0.472); query has E351.
GH13_33 acid/base state: consensus E (P = 0.424); query has R391.
GH13_33 transition-state state: consensus D (P = 0.446); query keeps D456.

## 3. Structure (AlphaFold DB AF-Q72CR4-F1 v6, Foldseek 3Di+AA)

`results/foldseek/foldseek_results.json`, run `dvu1219-foldseek`.

- Global pLDDT 86.88; segment means: 1-45 39.3, 46-122 79.3, 123-583 91.5, 584-731 90.8
- 365 AFDB-SwissProt hits and 563 PDB100 hits; all top hits are GH13 enzymes, aligned over
  query ~100-731 (catalytic TIM barrel plus domains B and C) at 11-15% sequence identity
- Top AFDB-SwissProt hit: O06458 Trehalose synthase (Thermus thermophilus), E = 2.5e-20, query 104-731
- Next: M. tuberculosis TreS P9WQ18 (E = 8.4e-19), Pimelobacter TreS P72235 (E = 5.2e-19),
  Neisseria polysaccharea amylosucrase Q9ZEU2 (E = 3.5e-18), glucosylglycerate phosphorylase G0GBS4 (E = 3.5e-18)
- Top PDB hits: trehalose synthase structures (4wf7, 5ykb, 5h2t, 5jy7) and amylosucrase (4flr, 1jg9, 3ucq)

Catalytic residues transferred from UniProt ACT_SITE/SITE features of the AFDB-SwissProt hits
through the Foldseek alignments:

- Nucleophile Asp maps to query E351 in 17 of 18 annotated hits that align it (O06994 maps it to G349; 7 more leave it unaligned)
- Proton donor (acid/base) Glu maps to query R391 in 22 of 24 annotated hits (W389 in Q9AI62, R383 in Q9Z3R8)
- Transition-state stabilizer Asp maps to query D456 in 14 of 16 annotated hits (amylosucrase hits: V511, Y510)

O06458 trehalose synthase: Nucleophile D197 -> query E351; Proton donor E240 -> query R391.
Q9ZEU2 amylosucrase: Nucleophile D294 -> query E351; Proton donor E336 -> query R391.
P38940 neopullulanase: Nucleophile D328 -> query E351; Proton donor E357 -> query R391; transition-state D424 -> query D456.

Local sequence: E351 in `PLVGLEIAPLA`; R391 in `GWTWMRDVLPF`; D456 in `TLPSADGIDYS`.

**Conclusion.** DVU_1219 is a full-length GH13-fold protein (CAZy subfamily GH13_33 by dbCAN,
structurally closest to trehalose synthase and amylosucrase), but both catalytic carboxylates of
the GH13 alpha-retaining mechanism are replaced: the nucleophile Asp by Glu351 and the
acid/base Glu by Arg391. Only the transition-state Asp (D456) is kept. Structure-based and
profile-based mappings agree independently. This pattern predicts a non-catalytic (pseudo-glycosidase)
GH13-like protein, as for the non-catalytic GH13-fold heavy chains rBAT/4F2hc; activity has not been tested.

## 4. Fitness (Fitness Browser DvH, BERDL `kescience.fitnessbrowser`)

`results/fitness/fitness_results.json`, run `dvu1219-fitness`. Strong = |fit| >= 1 and |t| >= 4.

DVU1219: 757 experiments; strong 132 (neg 117, pos 15); min -4.35 max 5.39

Strong phenotypes by experiment group: nitrogen source 44 of 125 (all negative); stress 52 negative and 15 positive of 268;
nutrient 15 of 202; respiratory growth 6 of 145; fermentative growth 0 of 17.

Fitness Browser specific-phenotype calls for DVU1219: none (specificphenotype table returns 0 rows).

Condition keyword tallies (strong / experiments):
- tungstate 18/42, from -3.96 (N2 gas + tungstate) to +5.39 (pyruvate-sulfite + tungstate 2 mM)
- molybdate 14/39, all negative, down to -3.52
- nitrate 5/5 strong, all positive (1.96 to 3.07)
- N2 gas 6/6 strong, all negative; FCCP 6/6 strong, all negative; urea 4/6
- lactate 1/57; formate 3/67

Tungstate is not consistently beneficial: MoYLS4 with Tungstate 2mM gives fit -0.82 to -1.06,
MoYLS4 with Tungstate 4mM +1.44 and +1.99, pyruvate-sulfite with tungstate 2 mM +4.06 to +5.39,
and N2 gas with tungstate 2 mM -3.57 to -3.96.

Top cofitness partners:
- 1 0.97 DVU3097 outer membrane efflux protein (TIGR)
- 2 0.59 DVU0438 AcrB/AcrD/AcrF family protein (TIGR)
- 3 0.57 DVU2439 efflux transporter, RND family, MFP subunit (TIGR)
- 6 0.56 DVU0437 efflux transporter, RND family, MFP subunit (TIGR)
- nitrogenase (nif) genes DVUA0007-DVUA0016 at 0.35-0.37

Molybdate experiments in yeast-extract medium (few genes affected): MoYLS4 with Molybdate 100uM: DVU1219 fit -3.34 t -16.1; strong neg 34 pos 13; rank 3
The co-ranked genes are the RND efflux module: DVU0438(-3.4) AcrB/AcrD/AcrF family protein (TIGR); DVU0437(-3.3) efflux transporter, RND family, MFP subu; DVU1219(-3.3) conserved hypothetical protein (TIGR); DVU3097(-3.3) outer membrane efflux protein (TIGR)

Tungstate benefit in pyruvate media is shared with ~50-100 genes: Pyruvate-Sulfite (60-20mM) with Tungstate 2mM: DVU1219 fit 5.39 t 26.1; strong neg 33 pos 97; rank 10
The largest gains there are in the DVU0245-DVU0251 cluster and DVU0771: DVU0250(13.4) hypothetical protein (TIGR); DVU0251(13.4) membrane protein, putative (TIGR); DVU0247(12.5) response regulator (TIGR)

N2 fixation with tungstate is a broad defect: MoLS4 with N2 gas (N) with Tungstate 2mM: DVU1219 fit -3.96 t -12.0; strong neg 130 pos 13; rank 44

Genomic neighbours: none of DVU1210-DVU1228 is cofit with DVU1219 (Pearson r <= 0.33;
DVU1214 PMT-family mannosyltransferase r = 0.29, DVU1215 PAP2 r = 0.33).

Fitness Browser "orthologs" in other organisms are TreS proteins at BLAST score ratio 0.15-0.16
(not true orthologues), none with a strong phenotype.

**Conclusion.** The molybdate and tungstate phenotypes are real and reproducible, but they are not
specific to DVU1219: DVU1219 is part of a 132-condition pleiotropic profile that it shares almost
exactly with the TolC-family outer membrane factor DVU3097 (cofitness 0.97) and the RND pump
DVU0437-DVU0438. Under molybdate excess these four genes are the top sick genes together; the
tungstate gain is part of a large response led by the DVU0245-0251 cluster. The data support a
role for DVU1219 together with the DVU0437/0438/3097 RND efflux system, not a dedicated metal
stress-response function.
