# PROS1 (vitamin K-dependent protein S, UniProt P07225) — review notes

## 2026-11-23 session

### Setup
- `just fetch-gene human PROS1`: 42 GOA rows (20 distinct term/evidence pairs), seeded stub.
- `just deep-research human PROS1 --provider perplexity` failed in this sandbox (the uvx
  tool resolution for `deep-research-client[cyberian]==0.2.12` cannot run with
  `UV_OFFLINE=1`). No provider file was produced. Literature research below was done by
  hand with PubMed searches; key papers were cached with `ai-gene-review fetch-pmid`.
- Literature queries run (PubMed): "protein S cofactor tissue factor pathway inhibitor
  Hackeng"; "Walker FJ[Author] AND protein S AND activated protein C AND 1980[pdat]";
  "Serum-derived protein S binds to phosphatidylserine and stimulates the phagocytosis of
  apoptotic cells"; "protein S C4b-binding protein complex Dahlback"; "human protein S
  cofactor activated protein C inactivation factor Va cleavage Arg306".

### Domain architecture (UniProt P07225)
Signal peptide 1-24, propeptide 25-41, mature chain 42-676: Gla domain, thrombin-sensitive
region (88-116), four EGF-like domains (three calcium-binding), and a C-terminal
SHBG-like region made of two laminin G-type (LG) domains (Pfam Laminin_G_1/Laminin_G_2;
SMART LamG x2). Note: the SHBG-like region is a pair of laminin G domains, not a
serine-protease-like domain; PROS1 has no peptidase domain and no catalytic activity.
PANTHER PTHR24040:SF0 (VITAMIN K-DEPENDENT PROTEIN S), sister of GAS6.

### Function — APC cofactor (core)
- Discovered as an APC cofactor with bovine protein S [PMID:6892911 "These results indicate
  that protein S may be a cofactor for activated protein C."] (bovine; ortholog evidence).
- Human: [PMID:20308596 "Protein S, a vitamin K–dependent plasma anticoagulant protein,
  functions as an enhancing cofactor to activated protein C (APC) in the inactivation of
  activated factors V (FVa) and VIII (FVIIIa)."]; D95A in EGF1 abolishes cofactor activity
  and "purified protein S D95A was shown to have greatly reduced ability to enhance
  APC-induced cleavage of FVa Arg306" (full text available).
- Human chimeras: [PMID:10959700 "In the FVa degradation, protein S selectively accelerates
  the cleavage at Arg306, having no effect on the Arg506 cleavage."]; the G2 LG domain is
  needed for full cofactor activity.
- Mechanism (Reactome R-HSA-5604929): "Protein S must be membrane-bound to display this
  cofactor activity" — PROS1 is a peripheral protein on the outer leaflet of PS-exposing
  membranes, via its Gla domain.
- So the MF is non-catalytic enhancement of a serine endopeptidase (APC):
  GO:0061133 endopeptidase activator activity (definition "Binds to and increases the
  activity of an endopeptidase"). This mirrors the F5 review's use of GO:0061133 for FVa.

### Function — TFPI cofactor (core)
- [PMID:16488980 "The stimulatory effect of protein S on FXa inhibition by TFPI is caused by
  a 10-fold reduction of the K(i) of the FXa/TFPI complex"]; human proteins, plasma thrombin
  generation. Reviewed in PMID:19661488 and PMID:22425215.
- Reactome R-HSA-9931628/9931624 model the TFPIalpha:FV intermediate:PROS1 complex.
- GO representation: contributes_to GO:0004867 serine-type endopeptidase inhibitor activity
  (as in the F5 review for FV-short): PROS1 is part of the inhibitory assembly, TFPI supplies
  the Kunitz-domain inhibition.

### APC-independent direct inhibition of FVa/FXa (disputed)
- [PMID:8428962] and [PMID:8146182] reported direct binding to FVa and FXa and APC-independent
  inhibition; UniProt FUNCTION text is built on these two papers.
- Hackeng & Rosing review [PMID:19661488 "Later it was shown that the anticoagulant activity
  of purified protein S in model systems was dependent on the concentration of phospholipid
  vesicles and was explained by low amounts of protein S multimers generated during
  purification"] — the APC-independent activity in plasma is now explained largely by the
  TFPI cofactor activity. Recorded as DISPUTED; no MF annotation proposed for it.
- Reactome R-HSA-9669959 describes PROS1 binding/inhibiting FIXa (Chattopadhyay 2012, Plautz
  2018); not independently checked here; only the extracellular-region row rests on it.

### C4BP complex
- [PMID:6223625 "Protein S was found to form a 1:1 complex with the higher-molecular-weight
  form of C4b-binding protein"]; ~60-70% of plasma protein S is C4BP-bound and lacks APC
  cofactor activity [PMID:1833851 "The complexed form of protein S has no APC cofactor
  function."]. No informative MF term for C4BP-beta binding beyond protein binding; not
  proposed.

### TAM-receptor ligand; apoptotic cell clearance
- [PMID:7867073 "These ligands correspond to protein S, a protease regulator that is a potent
  anticoagulant, and Gas6"] — ligand for Tyro3/Axl (abstract only; species of the protein
  not stated in the abstract; UniProt curates the ligand statement on the human entry with
  ECO:0000269).
- Human serum protein S: [PMID:12447359 "Protein S acted by binding to phosphatidylserine
  expressed on the apoptotic cell surface."] and stimulates macrophage phagocytosis of
  apoptotic cells; the C4BP-protein S complex inhibits this [PMID:15096498].
- Mouse: protein S protects neurons via Tyro3-PI3K-Akt [PMID:21084607] — source of the
  GO:0051897 IEA (Ensembl Compara from mouse Q08761 IDA).
- Comparator check (QuickGO by geneProductId, run 2026-11-23): human GAS6 (Q14393) carries
  GO:0048018 receptor ligand activity (IDA, IBA), GO:0001786 phosphatidylserine binding (IDA),
  GO:0043277 apoptotic cell clearance (IDA); MFGE8 (Q08431) carries GO:0001786 (IPI, IBA) and
  GO:0043277 (IEA). So the query returns positives and bridging opsonins in the same role do
  carry these terms; PROS1 carries none of them. PROS1 itself performs the PS-recognition
  step (the bridge), so it passes the participation test for apoptotic cell clearance.

### GOA rows of note
- 8 x protein binding IPI from PMID:32814053 (neurodegeneration interactome Y2H): partners are
  intracellular (KAT5, SETDB1, LMO3, OPTN, YWHAG, PRKCA, PPIA, HLA-A); uninformative and not
  physiologically plausible for a secreted plasma protein -> REMOVE under protein-binding policy.
- ER membrane / Golgi membrane TAS (Reactome biosynthesis): PROS1 is a soluble lumenal
  secretory cargo; membrane locations are not supported -> MARK_AS_OVER_ANNOTATED.
- ER (ARBA IEA), Golgi lumen (ARBA IEA, Reactome TAS): biosynthetic transit of a secreted
  protein, no direct residence evidence -> MARK_AS_OVER_ANNOTATED (ORGANELLES rule 7: transit
  is not residence).
- Endosome lumen TAS (dengue entry model): virion-bridging context, not a PROS1 location ->
  MARK_AS_OVER_ANNOTATED.
- Plasma membrane TAS (APC reactions) -> MODIFY to GO:0009897 external side of plasma membrane
  (same choice as the F5 review).
- blood coagulation TAS (PMID:9657428, deficiency mutation causing thrombophilia) -> MODIFY to
  GO:0030195 negative regulation of blood coagulation (PROS1 is an anticoagulant).

## 2026-11-24 session
- Wrote the review YAML from the plan above (the 2026-11-23 attempt stopped before writing it).
  42 GOA rows plus 5 NEW: REMOVE 8 (bare protein binding), MODIFY 7 (6 plasma membrane ->
  external side of plasma membrane; blood coagulation -> negative regulation of blood
  coagulation), MARK_AS_OVER_ANNOTATED 9 (ER/Golgi transit, dengue endosome model), ACCEPT 13
  (extracellular region) + 1 (negative regulation of coagulation IBA), KEEP_AS_NON_CORE 5.
- NEW: GO:0061133 (APC cofactor), contributes_to GO:0004867 (TFPI cofactor), GO:0001786,
  GO:0048018 (TAM ligand, TAS from Reactome R-HSA-202710 since the PMID:7867073 abstract does
  not state the species), GO:0043277.
- `just validate human PROS1`: valid; quote_check 63 verified.
