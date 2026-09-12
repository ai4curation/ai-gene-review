---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:03:15.998935'
end_time: '2026-07-11T18:16:58.954208'
duration_seconds: 822.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: acnA-I
  gene_symbol: acnA-I
  uniprot_accession: Q88L24
  protein_description: 'RecName: Full=Aconitate hydratase {ECO:0000256|RuleBase:RU361275};
    Short=Aconitase {ECO:0000256|RuleBase:RU361275}; EC=4.2.1.3 {ECO:0000256|RuleBase:RU361275};'
  gene_info: Name=acnA-I {ECO:0000313|EMBL:AAN67725.1}; OrderedLocusNames=PP_2112
    {ECO:0000313|EMBL:AAN67725.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aconitase/IPM isomerase family.
  protein_domains: AcnA_IRP_Swivel. (IPR044137); Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931);
    Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase/3IPM_dehydase_swvl. (IPR015928);
    Aconitase/IRP2. (IPR006249)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: acnA-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: acnA-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88L24
- **Protein Description:** RecName: Full=Aconitate hydratase {ECO:0000256|RuleBase:RU361275}; Short=Aconitase {ECO:0000256|RuleBase:RU361275}; EC=4.2.1.3 {ECO:0000256|RuleBase:RU361275};
- **Gene Information:** Name=acnA-I {ECO:0000313|EMBL:AAN67725.1}; OrderedLocusNames=PP_2112 {ECO:0000313|EMBL:AAN67725.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aconitase/IPM isomerase family.
- **Key Domains:** AcnA_IRP_Swivel. (IPR044137); Acnase/IPM_dHydase_lsu_aba_1/3. (IPR015931); Acoase/IPM_deHydtase_lsu_aba. (IPR001030); Aconitase/3IPM_dehydase_swvl. (IPR015928); Aconitase/IRP2. (IPR006249)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "acnA-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'acnA-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **acnA-I** (gene ID: acnA-I, UniProt: Q88L24) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **acnA-I** (PP_2112, UniProt Q88L24)
### Aconitate hydratase (Aconitase, EC 4.2.1.3) — *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**acnA-I (PP_2112, Q88L24) encodes a cytoplasmic, [4Fe-4S]-cluster-dependent aconitase (aconitate hydratase, EC 4.2.1.3) that catalyzes the reversible, stereospecific isomerization of citrate to D-*threo*-isocitrate via the enzyme-bound intermediate *cis*-aconitate — the second step of the tricarboxylic acid (TCA/Krebs) cycle.** Sequence, structural, and evolutionary evidence identify it specifically as an **AcnA-type** enzyme (73% identical to the biochemically characterized *Escherichia coli* AcnA), i.e. the stable, iron/oxidative-stress-inducible "maintenance" aconitase, as opposed to the exponential-phase catabolic AcnB or the propionate/2-methylcitrate-dedicated aconitases encoded elsewhere in the genome. Like other AcnA/IRP-family proteins, it is predicted to be **bifunctional**: when its Fe-S cluster is lost under iron limitation or oxidative stress, the apo-protein can act as a post-transcriptional mRNA-binding regulator.

**Gene identity was verified** at every step: the symbol *acnA-I*, the aconitate hydratase description, the aconitase/IPM-isomerase family, the AcnA_IRP swivel and aconitase domains, and the organism *P. putida* KT2440 are all mutually consistent with the enzyme characterized below. There was **no** evidence of a same-symbol collision with an unrelated gene.

---

## 2. Molecular Function and Reaction Catalyzed

### 2.1 The reaction
AcnA-I is an **aconitate hydratase (aconitase)**, EC 4.2.1.3, catalyzing:

> **citrate ⇌ *cis*-aconitate + H₂O ⇌ D-*threo*-isocitrate**

The overall reaction is a net isomerization (a dehydration followed by a stereochemically distinct re-hydration) that moves a hydroxyl group from the C3 to the C2 position of the tricarboxylic acid, proceeding through the tightly bound intermediate *cis*-aconitate (UniProt Q88L24 catalytic activity: "citrate = D-threo-isocitrate"; UniPathway: *tricarboxylic acid cycle; isocitrate from oxaloacetate: step 2/2*). Aconitases are iron–sulfur proteins that "catalyse the reversible isomerization of citrate and isocitrate via the intermediate *cis*-aconitate in the Krebs cycle" (Baothman et al., 2013, PMID 23637460).

### 2.2 Catalytic cofactor and mechanism
Catalysis depends on a **[4Fe-4S] cluster** (UniProt cofactor annotation; keywords 4Fe-4S, Iron-sulfur). Three of the four irons are ligated by cysteine residues; the fourth iron (**Fe4**) is coordinatively unsaturated and directly binds the substrate's hydroxyl and a carboxylate, acting as a Lewis acid during the dehydration/rehydration. Crystallographic studies of the homologous mitochondrial aconitase established that "Fe4 of the [4Fe-4S] cluster is five-coordinate," and that the mechanistic model extends "to all three natural substrates of aconitase" — citrate, *cis*-aconitate, and isocitrate (Lauble et al., 1994, PMID 8151704).

**Residue-level evidence for an intact active site in AcnA-I:**
- The three cluster-ligating cysteines occur in the canonical single-Cys + Cys-X-X-Cys geometry: **Cys454, Cys520, Cys523** in PP_2112.
- These map **one-to-one** onto the curated *E. coli* AcnA ligands **Cys435, Cys501, Cys504** (UniProt P25516), whose Fe-S cluster was characterized by EPR and magnetic-CD spectroscopy and shown to "strongly resemble those of the mammalian enzymes" (Jordan et al., 1999, PMID 10585860).
- The active-site stretch **ITSCTNTSNP** (surrounding the first ligand cysteine) is **identical** in PP_2112 (452–461) and *E. coli* AcnA (433–442), indicating full conservation of the catalytic pocket.

### 2.3 Substrate specificity
AcnA-I is expected to act on the **canonical TCA tricarboxylates (citrate/*cis*-aconitate/isocitrate)**. In some AcnA enzymes the same active site can also hydrate 2-methyl-*cis*-aconitate to 2-methylisocitrate in the 2-methylcitrate (propionate) cycle (Horswill & Escalante-Semerena, 2001, PMID 11294638). However, in *P. putida* KT2440 that propionate-catabolic role is delegated to a **separate, dedicated gene cluster** (see Section 4), so AcnA-I's physiological substrate is the standard TCA-cycle citrate/isocitrate pair.

---

## 3. Subcellular Localization

AcnA-I functions in the **cytoplasm (cytosol)**. UniProt Q88L24 annotates only structural domains (aconitase large subunit, residues 76–581; AcnA/IPM swivel, 710–837) and contains **no signal peptide and no transmembrane segment**, ruling out periplasmic, membrane, or extracellular localization. This is consistent with the aconitase/IRP1 family being soluble cytosolic proteins — mammalian IRP1/cytosolic aconitase is "a well-established cytosolic protein" (Gu et al., 2022, PMID 36142654). The TCA cycle and the enzyme's potential mRNA targets both reside in the same compartment.

---

## 4. Genomic Context, Paralogs, and Pathway Placement

*P. putida* KT2440 encodes **three** aconitase-family (EC 4.2.1.3) proteins plus an aconitate isomerase, revealing a division of labour:

| Locus | Gene | UniProt | Length | Role (inferred) |
|-------|------|---------|--------|-----------------|
| **PP_2112** | **acnA-I** | **Q88L24** | **913 aa** | **Standalone AcnA-type TCA-cycle aconitase (this report)** |
| PP_2336 | acnA-II | Q88KF4 | 862 aa | AcnA-type, within the propionate/2-methylcitrate cluster |
| PP_2337 | prpF | Q88KF3 | 396 aa | Aconitate isomerase (2-methyl-aconitate handling) |
| PP_2339 | acnB | Q88KF1 | 869 aa | AcnB-type; also 2-methylisocitrate dehydratase (EC 4.2.1.99) |

**acnA-I (PP_2112) sits alone** on the chromosome, whereas acnA-II/prpF/acnB form a contiguous cluster associated with **2-methylcitrate / propionate catabolism**. This mirrors the observation that acnA-type genes recur "in a number of putative prp operons" (Horswill & Escalante-Semerena, 2001, PMID 11294638) — but importantly, PP_2112 is the copy that is *not* in such an operon, marking it as the **general TCA-cycle housekeeping/maintenance aconitase**.

**Pathway:** The reaction is step 2 of the TCA cycle (citrate → isocitrate), feeding isocitrate to isocitrate dehydrogenase and, at branch points, to the glyoxylate shunt. In *P. putida*, whose metabolism is organised around the TCA cycle and gluconeogenesis, this step is central to energy generation and to biosynthetic precursor supply (2-oxoglutarate, succinyl-CoA, oxaloacetate).

---

## 5. Evolutionary / Bioinformatic Evidence for the AcnA Assignment

Global (Needleman–Wunsch) pairwise identity of PP_2112 against reference aconitases:

| Reference | UniProt | % identity to PP_2112 |
|-----------|---------|-----------------------|
| *E. coli* **AcnA** | P25516 | **72.6%** |
| *P. putida* AcnA-II | Q88KF4 | 54.3% |
| Pig mitochondrial aconitase / IRP1 homolog | P16276 | 43.3% |
| *P. putida* AcnB | Q88KF1 | 34.5% |
| *E. coli* **AcnB** | P36683 | 34.9% |

The ~2-fold identity gap between the AcnA clade (>54%) and the AcnB clade (~35%) unambiguously assigns PP_2112 to the **AcnA subfamily**. Because *E. coli* AcnA is biochemically well characterized, this **orthology** (not merely family membership) licenses transfer of its established properties to PP_2112.

**Independent structural support:** the AlphaFold model of AcnA-I (AF-Q88L24-F1) is **very high confidence** (mean pLDDT 92.4; 96.8% of residues >70, 80.4% >90), indicating the four-domain aconitase architecture (three large-subunit domains plus the AcnA/IPM swivel domain closing over the active-site cleft) is modeled reliably — consistent with a canonical aconitase fold competent for [4Fe-4S] binding and catalysis.

**Properties of the AcnA archetype** (transferable to AcnA-I):
- A **stable, aerobic stationary-phase enzyme, specifically induced by iron and oxidative stress**, with higher affinity for citrate and a broad pH optimum — "consistent with its role as a maintenance or survival enzyme during nutritional or oxidative stress," in contrast to the catabolic, less stable AcnB (Jordan et al., 1999, PMID 10585860).
- In *Salmonella*, acnA expression is controlled by CRP (glucose starvation), FNR (oxygen starvation), Fur (iron starvation), and SoxR (oxidative stress) (Baothman et al., 2013, PMID 23637460).

---

## 6. Secondary (Moonlighting) Function: Cluster-Dependent RNA Binding

AcnA-family proteins are **bifunctional**, resembling the vertebrate iron-regulatory proteins (IRP1) in "having alternative mRNA-binding and catalytic activities" (Tang & Guest, 1999, PMID 10589714). When the labile [4Fe-4S] cluster is disassembled by oxidants or iron starvation, the **apo-protein** switches to a site-specific RNA-binding mode:
- In *E. coli*, apo-AcnA/AcnB bind the 3′UTRs of acn mRNAs, and the apo-forms have >3-fold higher mRNA affinity than the holo-enzymes; "the apo-proteins function as post-transcriptional regulators by site-specific binding to acn mRNAs," with AcnA **stabilizing sodA (superoxide dismutase) mRNA** — coupling aconitase status to the oxidative-stress defence (Tang et al., 2002, PMID 11932448).
- The switch is cluster-dependent, exactly as for mammalian IRP1, which is "a bifunctional protein with mutually exclusive RNA-binding or enzymatic activities that depend on the presence of a 4Fe-4S cluster" (Gu et al., 2022, PMID 36142654).

PP_2112 carries the UniProt **RNA-binding** keyword (GO:0003723) and the **AcnA_IRP swivel domain (IPR044137)**, so this regulatory potential is structurally encoded. Direct experimental demonstration of RNA targets specifically for the *P. putida* protein has not been reported; this role is inferred from strong orthology and conserved domain architecture.

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1 — AcnA-I is a genuine [4Fe-4S] aconitase catalyzing citrate↔isocitrate in the TCA cycle. *(Curated annotation + residue-level active-site conservation.)*
- H2 — PP_2112 is an AcnA-type (not AcnB-type) enzyme, orthologous to *E. coli* AcnA. *(73% vs 35% identity; clade separation.)*
- H3 — The enzyme is cytoplasmic. *(No signal/TM; family is cytosolic.)*
- H4 — Physiological substrate is the standard TCA citrate/isocitrate pair, with propionate/2-methylcitrate handled by the separate acnA-II/acnB/prpF cluster. *(Paralog/genomic-context analysis.)*

**Supported by inference (not yet experimentally confirmed in *P. putida*):**
- H5 — Apo-AcnA-I can moonlight as a post-transcriptional RNA-binding regulator under iron/oxidative stress. *(Orthology + IRP swivel domain + RNA-binding keyword; awaits direct experimental validation.)*

**Refuted:**
- That PP_2112 is the exponential-phase catabolic AcnB (35% identity — rejected) or a dedicated 2-methylcitrate-cycle enzyme (that function maps to PP_2336–2339 — rejected as its primary role).

---

## 8. Limitations and Future Directions

- **Direct experimental data specific to PP_2112 are sparse.** Targeted PubMed searches returned no primary *P. putida* AcnA-I characterization; conclusions rest on (i) curated database annotation, (ii) very high orthology to the experimentally characterized *E. coli*/*Salmonella* AcnA, and (iii) residue-level structural conservation. This is strong but indirect for the moonlighting role.
- **Future work:** purify AcnA-I and measure kinetic constants (Km for citrate/isocitrate) and pH profile; test single/double aconitase knockouts (acnA-I vs acnA-II/acnB) for growth-phase, iron-, and oxidative-stress phenotypes; perform EPR/MCD on the cluster; and use RNA-immunoprecipitation/CLIP to identify apo-AcnA-I mRNA targets in *P. putida*.

---

## 9. Key References
- Baothman OAS, Rolfe MD, Green J. *Characterization of Salmonella enterica serovar Typhimurium aconitase A.* Microbiology 2013. **PMID 23637460**.
- Jordan PA, Tang Y, Bradbury AJ, Thomson AJ, Guest JR. *Biochemical and spectroscopic characterization of E. coli aconitases (AcnA and AcnB).* Biochem J 1999. **PMID 10585860**.
- Tang Y, Guest JR. *Direct evidence for mRNA binding and post-transcriptional regulation by E. coli aconitases.* Microbiology 1999. **PMID 10589714**.
- Tang Y, Quail MA, Artymiuk PJ, Guest JR, Green J. *E. coli aconitases and oxidative stress: post-transcriptional regulation of sodA.* Microbiology 2002. **PMID 11932448**.
- Lauble H, Kennedy MC, Beinert H, Stout CD. *Crystal structures of aconitase with trans-aconitate and nitrocitrate bound.* J Mol Biol 1994. **PMID 8151704**.
- Horswill AR, Escalante-Semerena JC. *In vitro conversion of propionate to pyruvate ... PrpD and aconitase.* Biochemistry 2001. **PMID 11294638**.
- Gu Y, Fillebeen C, Pantopoulos K. *Human IRP1 translocates to the nucleus in a cell-specific and iron-dependent manner.* 2022. **PMID 36142654**.
- UniProt Q88L24 (acnA-I / PP_2112); P25516 (*E. coli* AcnA); P36683 (*E. coli* AcnB); Q88KF1/Q88KF4/Q88KF3 (*P. putida* paralogs).


## Artifacts

- [OpenScientist final report](acnA-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](acnA-I-deep-research-openscientist_artifacts/final_report.pdf)