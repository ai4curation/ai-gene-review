---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:04:06.434471'
end_time: '2026-07-23T13:30:24.411933'
duration_seconds: 1577.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: acnA-II
  gene_symbol: acnA-II
  uniprot_accession: Q88KF4
  protein_description: 'RecName: Full=aconitate hydratase {ECO:0000256|ARBA:ARBA00012926};
    EC=4.2.1.3 {ECO:0000256|ARBA:ARBA00012926};'
  gene_info: Name=acnA-II {ECO:0000313|EMBL:AAN67949.1}; OrderedLocusNames=PP_2336
    {ECO:0000313|EMBL:AAN67949.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aconitase/IPM isomerase family.
  protein_domains: 2Me_IsoCit_deHydtase_FeS-dep. (IPR012708); Acnase/IPM_dHydase_lsu_aba_1/3.
    (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase/3IPM_dehydase_swvl.
    (IPR015928); Aconitase/IRP2. (IPR006249)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: acnA-II-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: acnA-II-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88KF4
- **Protein Description:** RecName: Full=aconitate hydratase {ECO:0000256|ARBA:ARBA00012926}; EC=4.2.1.3 {ECO:0000256|ARBA:ARBA00012926};
- **Gene Information:** Name=acnA-II {ECO:0000313|EMBL:AAN67949.1}; OrderedLocusNames=PP_2336 {ECO:0000313|EMBL:AAN67949.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aconitase/IPM isomerase family.
- **Key Domains:** 2Me_IsoCit_deHydtase_FeS-dep. (IPR012708); Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase/3IPM_dehydase_swvl. (IPR015928); Aconitase/IRP2. (IPR006249)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "acnA-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'acnA-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **acnA-II** (gene ID: acnA-II, UniProt: Q88KF4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *acnA-II* (PP_2336, UniProt Q88KF4) in *Pseudomonas putida* KT2440

**Target:** Gene *acnA-II*; OrderedLocusName **PP_2336**; UniProt **Q88KF4** (TrEMBL, unreviewed; protein existence = inferred from homology).
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**).
**Report date:** 2026-07-23.

---

## 1. Summary (answer to the research question)

PP_2336 encodes a **cytoplasmic, [4Fe‑4S]‑cluster–dependent dehydratase of the aconitase superfamily**. Although the automated gene symbol ("acnA‑II") and the generic UniProt label ("aconitate hydratase, EC 4.2.1.3") suggest an ordinary tricarboxylic‑acid (TCA)‑cycle aconitase, the ortholog assignment, protein‑family signature, and — most decisively — its position within the *P. putida* **methylcitrate (prp) operon** identify it as an **AcnD‑type 2‑methylcitrate dehydratase (EC 4.2.1.117; KEGG K20455)**. Its specific, committed role is the dehydration of **(2S,3S)‑2‑methylcitrate to 2‑methyl‑*trans*‑aconitate** (and, by the same aconitase‑like half‑reaction, citrate → *cis*‑aconitate) in the **2‑methylcitrate cycle** that catabolises propionate (and propionyl‑CoA from odd‑chain fatty acids / amino‑acid degradation) to pyruvate and succinate. It works obligately with the adjacent accessory isomerase **PrpF (PP_2337)**, which converts the *trans* product to 2‑methyl‑*cis*‑aconitate for downstream hydration by the housekeeping aconitase **AcnB (PP_2339)**.

---

## 2. Molecular identity and biophysical properties

| Property | Value | Source |
|---|---|---|
| Length / mass | 862 aa / ~93.96 kDa, monomeric | UniProt Q88KF4 |
| Cofactor | one **[4Fe‑4S] cluster** | UniProt Q88KF4 (keywords: 4Fe‑4S, Iron, Iron‑sulfur, Metal‑binding) |
| Domains | Aconitase/3‑IPM‑dehydratase large α/β/α (res 65–533); Aconitase A "swivel" small‑subunit domain (res 656–788) | UniProt features; Pfam PF00330 + PF00694 |
| Family signatures | **IPR012708 "2‑methylisocitrate dehydratase AcnD, Fe/S‑dependent"**; IPR006249 "Aconitase/IRP2"; IPR001030/IPR015928/IPR015931/IPR000573; **COG1048** | InterPro / eggNOG |
| Orthology | **KEGG K20455 — 2‑methylcitrate dehydratase (2‑methyl‑*trans*‑aconitate forming), EC 4.2.1.117** | KEGG ppu:PP_2336 |
| Localization | Cytoplasmic (no signal peptide/TM segment; universal for aconitase‑family enzymes) | Inferred (sequence + family) |
| Evidence level | Inferred from homology (PE3); no structure or direct assay for PP_2336 itself | UniProt |

All members of the aconitase superfamily are soluble **cytoplasmic** enzymes that carry a catalytic [4Fe‑4S] cluster in which three iron atoms are Cys‑ligated and the fourth (Fe‑a) is solvent‑exposed and coordinates the substrate hydroxyl/carboxylate during dehydration–rehydration [Lauble 1994, PMID 8151704]. Bacterial aconitases are "distantly related **monomeric Fe‑S proteins** that contain different arrangements of four structural domains" [Jordan 1999, PMID 10585860] — exactly the two‑lobe (large α/β/α + swivel) architecture annotated for PP_2336.

---

## 3. Primary function: the reaction catalysed and substrate specificity

**PP_2336 catalyses the dehydration of 2‑methylcitrate to 2‑methyl‑*trans*‑aconitate (EC 4.2.1.117), and the analogous aconitase‑like dehydration of citrate to *cis*‑aconitate / hydration of *cis*‑aconitate.** It does **not** carry out the second (isocitrate‑forming) half of the classical aconitase reaction.

The definitive biochemistry comes from the experimentally characterised AcnD orthologs (*Shewanella oneidensis* MR‑1 and *Vibrio cholerae*), whose sequences, KO (K20455) and family signature (IPR012708/COG1048) are shared by PP_2336:

- "**AcnD dehydrated 2‑methylcitrate and citrate to 2‑methyl‑cis‑aconitate and cis‑aconitate, respectively; AcnD also hydrated cis‑aconitate. However, 2‑methylisocitrate and isocitrate were not substrates for AcnD, indicating that AcnD only catalyzes the first half of the aconitase‑like dehydration reactions.**" [Grimek & Escalante‑Semerena 2004, PMID 14702315]
- "**The AcnD protein required reconstitution of an Fe/S cluster for activity.** All detectable AcnD activity was lost after incubation with iron‑chelating agents…" [PMID 14702315] — consistent with the [4Fe‑4S] cofactor annotated for Q88KF4.
- The KEGG EC 4.2.1.117 designation ("2‑methyl‑*trans*‑aconitate forming") and later mechanistic work show the AcnD product is the *trans* (not *cis*) isomer, which is why a dedicated isomerase (PrpF) is required downstream [Rocco et al. 2017, PMID 29145506].

**Substrate specificity, precisely stated:** tricarboxylate substrates bearing a C2 hydroxyl and (for the physiological substrate) a 2‑methyl branch — i.e. **(2S,3S)‑2‑methylcitrate** (physiological) and **citrate** (promiscuous) — undergoing *anti*/*syn* elimination of water to the corresponding aconitate. The enzyme is specialised for the **dehydration (first) half‑reaction only**.

---

## 4. Pathway context: the AcnD–PrpF variant of the 2‑methylcitrate cycle

PP_2336 lies in a contiguous, co‑oriented **prp/methylcitrate gene cluster** in KT2440 (KEGG module **M00982 Methylcitrate cycle**; pathway **ppu00640 Propanoate metabolism**; GO:0019679 "propionate metabolic process, methylcitrate cycle"):

| Locus | Gene / enzyme | KO / EC |
|---|---|---|
| PP_2333 | GntR‑family regulator (PrpR‑like) | — |
| PP_2334 | 2‑methylisocitrate lyase (PrpB) | K03417 / 4.1.3.30 |
| PP_2335 | 2‑methylcitrate synthase (PrpC) | K01659 / 2.3.3.5 |
| **PP_2336** | **AcnD — 2‑methylcitrate dehydratase (this gene)** | **K20455 / 4.2.1.117** |
| PP_2337 | 2‑methylaconitate isomerase (PrpF) | K09788 / 5.3.3.– |
| PP_2338 | 2‑methylcitrate dehydratase (PrpD) | K01720 / 4.2.1.79 |
| PP_2339 | bifunctional aconitate hydratase 2 / 2‑methylisocitrate dehydratase (AcnB) | K01682 / 4.2.1.3, 4.2.1.99 |

**Reaction sequence of the cycle** (propionate entry):
1. Propionyl‑CoA + oxaloacetate → **2‑methylcitrate** (PrpC, PP_2335).
2. **2‑methylcitrate → 2‑methyl‑*trans*‑aconitate** — **AcnD (PP_2336)**.
3. 2‑methyl‑*trans*‑aconitate → 2‑methyl‑*cis*‑aconitate — **PrpF (PP_2337)**.
4. 2‑methyl‑*cis*‑aconitate → **(2R,3S)‑2‑methylisocitrate** — hydration by **AcnB (PP_2339)**.
5. 2‑methylisocitrate → **pyruvate + succinate** — PrpB (PP_2334).

The obligatory hand‑off is established directly: "**We show that the SoPrpF protein isomerizes the product of the AcnD reaction into the PrpD product (2‑MCA], a known substrate of the housekeeping aconitase (AcnB]**" [Rocco et al. 2017, PMID 29145506], and the AcnD+PrpF pair is functionally sufficient: "**the AcnD and PrpF proteins restored the ability of a prpD mutant strain of *Salmonella enterica* to grow on propionate as a source of carbon and energy**" [Grimek & Escalante‑Semerena 2004, PMID 14702315].

**Why two routes?** KT2440 encodes *both* an Fe/S‑independent PrpD (PP_2338; forms 2‑methyl‑*cis*‑aconitate directly [Horswill & Escalante‑Semerena 2001, PMID 11294638; Brock et al. 2002, PMID 12473114]) *and* the AcnD–PrpF pair. These provide **parallel/redundant 2‑methylcitrate‑dehydration capacity**; the AcnD route (Fe/S‑dependent) is thought to predominate or be favoured under particular redox/iron conditions, whereas PrpD (Fe/S‑independent) is robust to oxidative stress. This redundancy explains why *acnA*/*acnD* single mutants in related organisms often show no propionate‑growth defect [Horswill 2001, PMID 11294638].

**Biological significance:** the methylcitrate cycle is the principal aerobic route for catabolising **propionate/propionyl‑CoA** — derived from odd‑chain fatty acids, branched‑chain amino acids (Ile, Val, Met, Thr), cholesterol side chains and environmental short‑chain acids — and for **detoxifying** the growth‑inhibitory intermediate propionyl‑CoA in this soil bacterium. This is directly relevant to KT2440's role as a metabolically versatile bioremediation/biotechnology chassis.

---

## 5. Distinction from the housekeeping TCA aconitases

*P. putida* KT2440 encodes several aconitase‑superfamily proteins with distinct jobs (KEGG EC linkage):
- **PP_2112** and **PP_2339 (AcnB)** — EC 4.2.1.3 / 4.2.1.99, the **canonical TCA‑cycle aconitases** (full citrate ⇌ isocitrate isomerisation) and AcnB additionally the 2‑methylisocitrate dehydratase.
- **PP_2338 (PrpD)** — EC 4.2.1.79, Fe/S‑independent 2‑methylcitrate dehydratase.
- **PP_2336 (this gene) — the unique EC 4.2.1.117 / AcnD**, specialised for the *trans*‑forming first half‑reaction in the methylcitrate cycle.

Thus PP_2336 is **not** the enzyme that supplies isocitrate to the TCA cycle; that role belongs to PP_2112/PP_2339. The bacterial paradigm in which two aconitases (AcnA = stationary‑phase/stress‑induced, more stable, moonlighting mRNA‑binding; AcnB = major exponential‑phase enzyme) partition function and can act as post‑transcriptional regulators [Tang & Guest 1999, PMID 10589714; Tang et al. 2002, PMID 11932448; Baothman et al. 2013, PMID 23637460] is informative background, but PP_2336 belongs to the **methylcitrate‑dedicated AcnD subfamily**, a functionally separate branch. There is no evidence that PP_2336 itself moonlights as an RNA‑binding regulator.

---

## 6. Localization

The enzyme functions in the **cytoplasm**. Aconitase‑superfamily proteins are soluble; the sequence lacks a signal peptide or transmembrane region, and the methylcitrate‑cycle intermediates it processes are cytosolic. No experimental localization data exist for PP_2336 specifically; this assignment is by strong homology and biochemical logic.

---

## 7. Supported and refuted hypotheses

**Supported**
- **H1 — PP_2336 is an aconitase‑superfamily [4Fe‑4S] dehydratase.** Supported by UniProt cofactor annotation, InterPro/Pfam signatures, COG1048.
- **H2 — Its specific/primary function is AcnD‑type 2‑methylcitrate dehydratase (EC 4.2.1.117), forming 2‑methyl‑*trans*‑aconitate.** Strongly supported by KEGG K20455, InterPro IPR012708, and the *prp*‑operon context; mechanism validated in orthologs [PMID 14702315; 29145506].
- **H3 — It operates in the 2‑methylcitrate cycle for propionate catabolism, obligately partnered with PrpF (PP_2337) and feeding AcnB (PP_2339).** Supported by operon structure, KEGG module M00982, and ortholog reconstitution/complementation studies.

**Refuted / not supported**
- **H4 — PP_2336 is a canonical TCA‑cycle aconitase interconverting citrate and isocitrate.** Refuted: AcnD enzymes do not use isocitrate/2‑methylisocitrate as substrates (only the first half‑reaction) [PMID 14702315]; the TCA aconitase role in KT2440 is filled by PP_2112/PP_2339. The "acnA‑II"/"EC 4.2.1.3" labels are automated over‑generalisations.
- **H5 — PP_2336 is a moonlighting mRNA‑binding regulator (IRP/AcnA‑type).** Not supported for this subfamily; no evidence.

---

## 8. Limitations and future directions

- **Evidence is inferential for PP_2336 itself** (UniProt PE3 "inferred from homology"; unreviewed TrEMBL). All enzymology derives from AcnD/PrpF orthologs in *Shewanella*, *Vibrio*, and *Salmonella*, plus the KT2440 genomic context — no purified‑enzyme assay, kinetics, or structure exists for Q88KF4.
- **Recommended validation:** (i) heterologous expression + in‑vitro assay of PP_2336 with 2‑methylcitrate/citrate (product stereochemistry by NMR) and Fe/S reconstitution; (ii) ΔPP_2336, ΔPP_2337, ΔPP_2338 and combinatorial mutants tested for growth on propionate vs glucose to define redundancy with PrpD; (iii) transcriptional analysis of the *prp* operon (PP_2333 PrpR/2‑methylcitrate induction); (iv) an AlphaFold model + docking to confirm the [4Fe‑4S] active site and *trans*‑forming geometry.
- **Open mechanistic question:** the precise identity of the AcnD product isomer (2‑methyl‑*trans*‑aconitate vs 4‑methylaconitate) and the exact accessory role of PrpF (isomerase vs Fe/S‑protecting) remain debated even in the model organisms [Rocco et al. 2017, PMID 29145506].

---

## 9. Key references

- Grimek TL, Escalante‑Semerena JC. *J Bacteriol* (2004). AcnD is a new Fe/S‑dependent 2‑methylcitrate dehydratase requiring PrpF. **PMID 14702315.**
- Rocco CJ, Wetterhorn KM, Garvey GS, Rayment I, Escalante‑Semerena JC. (2017). PrpF isomerizes 2‑methyl‑aconitate for the AcnD‑dependent 2‑methylcitrate cycle. **PMID 29145506.**
- Horswill AR, Escalante‑Semerena JC. (2001). In‑vitro reconstitution of the 2‑methylcitrate cycle; PrpD and AcnA. **PMID 11294638.**
- Brock M, et al. (2002). Propionate → pyruvate in *E. coli*; PrpD and AcnB. **PMID 12473114.**
- Jordan PA, Tang Y, et al. (1999). Biochemical/spectroscopic characterization of *E. coli* AcnA/AcnB. **PMID 10585860.**
- Lauble H, Kennedy MC, Beinert H, Stout CD. (1994). Aconitase crystal structures; [4Fe‑4S] catalytic mechanism. **PMID 8151704.**
- Tang Y, Guest JR. (1999). mRNA binding / post‑transcriptional regulation by *E. coli* aconitases. **PMID 10589714.**
- Baothman OA, Rolfe MD, Green J. (2013). *Salmonella* AcnA; dual‑aconitase model. **PMID 23637460.**
- Manoli MT, et al. (2026). Isozyme functional redundancy and TCA flux modes in *P. putida* KT2440 (context). **PMID 42464328.**
- Database records: UniProt **Q88KF4**; KEGG **ppu:PP_2336** (K20455); InterPro **IPR012708/IPR006249**; Pfam PF00330/PF00694; eggNOG **COG1048**.


## Artifacts

- [OpenScientist final report](acnA-II-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](acnA-II-deep-research-openscientist_artifacts/final_report.pdf)