---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T14:46:24.815471'
end_time: '2026-07-23T15:10:13.803486'
duration_seconds: 1428.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ddlB
  gene_symbol: ddlB
  uniprot_accession: Q88N74
  protein_description: 'RecName: Full=D-alanine--D-alanine ligase B {ECO:0000255|HAMAP-Rule:MF_00047};
    EC=6.3.2.4 {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-Ala-D-Ala ligase
    B {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-alanylalanine synthetase
    B {ECO:0000255|HAMAP-Rule:MF_00047};'
  gene_info: Name=ddlB {ECO:0000255|HAMAP-Rule:MF_00047}; OrderedLocusNames=PP_1339;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the D-alanine--D-alanine ligase family.
  protein_domains: ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); D-Ala_lig_Van_CS.
    (IPR000291); D_ala_D_ala. (IPR005905); Dala_Dala_lig_C. (IPR011095)
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
  path: ddlB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ddlB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N74
- **Protein Description:** RecName: Full=D-alanine--D-alanine ligase B {ECO:0000255|HAMAP-Rule:MF_00047}; EC=6.3.2.4 {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-Ala-D-Ala ligase B {ECO:0000255|HAMAP-Rule:MF_00047}; AltName: Full=D-alanylalanine synthetase B {ECO:0000255|HAMAP-Rule:MF_00047};
- **Gene Information:** Name=ddlB {ECO:0000255|HAMAP-Rule:MF_00047}; OrderedLocusNames=PP_1339;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the D-alanine--D-alanine ligase family.
- **Key Domains:** ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); D-Ala_lig_Van_CS. (IPR000291); D_ala_D_ala. (IPR005905); Dala_Dala_lig_C. (IPR011095)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ddlB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ddlB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ddlB** (gene ID: ddlB, UniProt: Q88N74) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *ddlB* (D-Alanine—D-Alanine Ligase B, Q88N74) in *Pseudomonas putida* KT2440

## Gene / Protein Identity (verified)

| Field | Value |
|---|---|
| Gene symbol | *ddlB* |
| Ordered locus | PP_1339 |
| UniProt | Q88N74 |
| Protein | D-alanine—D-alanine ligase B (D-Ala-D-Ala ligase B; D-alanylalanine synthetase B) |
| EC | 6.3.2.4 |
| Organism | *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK |
| Family | D-alanine—D-alanine ligase family (HAMAP-Rule MF_00047) |
| Domains | ATP-grasp (IPR011761); ATP-grasp subdomain 1 (IPR013815); D-Ala ligase Van conserved site (IPR000291); D-ala_D-ala (IPR005905); Dala_Dala_lig_C (IPR011095) |

**Identity check:** The gene symbol *ddlB*, the EC number 6.3.2.4, the ATP-grasp and D-Ala-D-Ala-ligase domain signatures, and the family assignment are fully mutually consistent. This is unambiguously a member of the D-alanine—D-alanine ligase (Ddl) family. There is no evidence of gene-symbol ambiguity; the only caveat is organism-level: essentially all mechanistic and structural work on this enzyme has been performed on orthologues (*E. coli* DdlB, and Ddl from *M. tuberculosis*, *Y. pestis*, *T. thermophilus*, *T. maritima*, *H. pylori*, enterococci). No study is specific to *P. putida* PP_1339. The function below is therefore assigned to Q88N74 by strong, unambiguous homology/family inference and validated by biochemistry of well-characterized orthologues, most directly the canonical *E. coli* DdlB, which is the structural reference for the family.

---

## Summary (Answer to the Research Question)

**Primary function.** *ddlB* encodes **D-alanine—D-alanine ligase B (DdlB, EC 6.3.2.4)**, a cytoplasmic, ATP-dependent ligase of the **ATP-grasp** superfamily. It catalyzes the condensation of **two molecules of D-alanine** into the dipeptide **D-alanyl-D-alanine (D-Ala-D-Ala)**, consuming ATP (2 D-Ala + ATP → D-Ala-D-Ala + ADP + Pᵢ) [PMID 34047462; 35382715]. Its substrate specificity is for D-alanine at both binding subsites; unlike the resistance ligases VanA/VanB, wild-type DdlB strongly disfavours D-lactate/α-hydroxy acids at the second (C-terminal) subsite [PMID 10801495].

**Localization.** The enzyme functions in the **bacterial cytoplasm**, catalyzing one of the cytosolic steps of peptidoglycan precursor synthesis [PMID 23286234]. Its product, however, is ultimately consumed **extracytoplasmically**: the terminal D-Ala-D-Ala of the completed precursor is the substrate/leaving group for periplasmic penicillin-binding-protein transpeptidases and the direct binding target of glycopeptide antibiotics at the cell surface.

**Pathway.** DdlB provides the D-Ala-D-Ala dipeptide that the ligase **MurF** adds to UDP-MurNAc-tripeptide, completing **UDP-MurNAc-pentapeptide** (the Park nucleotide) — the cytoplasmic end-product of the Mur pathway and the muropeptide unit later polymerized and cross-linked into the cell-wall sacculus [PMID 34047462; 35382715].

---

## Detailed Findings

### 1. Reaction catalyzed and substrate specificity

DdlB catalyzes the ATP-dependent ligation of two D-alanine molecules to form D-Ala-D-Ala:

> "D-alanyl-D-alanine ligase (Ddl) is an indispensable adenosine triphosphate-dependent bacterial enzyme … which catalyzes the ligation of two D-alanine molecules into one D-alanyl-D-alanine dipeptide." [PMID 34047462]

The "B" isoform designation reflects the situation in *E. coli* and many other Gram-negatives, where two paralogous ligases, **DdlA** and **DdlB**, both supply D-Ala-D-Ala; either alone is sufficient, and only the **ddlA ddlB double mutant** is a D-Ala-D-Ala **auxotroph**, demonstrating that this dipeptide-forming activity is essential for viability [PMID 15948948]. DdlB was directly identified as "responsible for the condensation of two alanines, forming D-Ala-D-Ala" [PMID 35382715].

The enzyme has **two D-alanine subsites** with distinct affinities. In the *M. tuberculosis* orthologue, K_m,D-Ala1 = 0.075 mM (N-terminal, high-affinity subsite) and K_m,D-Ala2 = 3.6 mM (C-terminal, low-affinity subsite) [PMID 23286234]. The chemistry of subsite 2 is the key determinant of specificity: naturally vancomycin-resistant and Van-type ligases replace an amide-accepting subsite 2 with one that accepts D-lactate (yielding D-Ala-D-Lac); comparison of the D-Ala-D-Lac ligase structure with wild-type **DdlB** revealed "alterations in the size and hydrophobicity of the site for D-lactate binding (subsite 2)" and reduced H-bonding to the second substrate [PMID 10801495]. Wild-type DdlB thus is a true D-Ala:D-Ala (amide-forming) ligase.

### 2. Structure and catalytic mechanism (ATP-grasp fold)

DdlB is one of the **three founding members of the ATP-grasp superfamily**, alongside biotin carboxylase and glutathione synthetase:

> "The founding members of the family consist of biotin carboxylase, d-ala-d-ala ligase and glutathione synthetase, all of which catalyze the ATP-assisted reaction of a carboxylic acid with a nucleophile via the formation of an acylphosphate intermediate." [PMID 21920581]

Mechanistically, the enzyme follows an **ordered ter-ter** kinetic mechanism: **ATP binds first**, then the two D-Ala substrates bind sequentially [PMID 23286234]. Catalysis proceeds by (i) phosphoryl transfer from ATP to the carboxylate of the first (N-terminal) D-Ala, generating a **D-alanyl-phosphate (acyl-phosphate) intermediate**; (ii) nucleophilic attack by the α-amino group of the second (C-terminal) D-Ala, forming the peptide bond and releasing inorganic phosphate. General-base chemistry participates in the catalytic step [PMID 23286234]. The intermediate has been captured structurally with **phosphinophosphate transition-state analogs** [PMID 10801495].

The protein is built from **three domains** (N-terminal, central, C-terminal), and catalysis is **conformationally gated**: flexible loops (the "serine loop" recognizing nucleotide phosphates, and the "ω-loop") and rigid-body rotation of the central domain drive an **open → semi-open → closed** transition that sequesters the substrates for chemistry [PMID 26894530; 19770507]. Activity is typically stimulated by monovalent cations (K⁺) [PMID 23286234]. Biophysically, recombinant *E. coli* DdlB is a compact, folded enzyme whose stability peaks near its pI (~5.0) [PMID 35382715].

### 3. Cellular localization and pathway context

DdlB is a **soluble cytoplasmic enzyme** acting in the cytosolic phase of peptidoglycan biosynthesis. Its product feeds directly into the Mur ligase cascade: **MurF** condenses D-Ala-D-Ala onto UDP-MurNAc-L-Ala-γ-D-Glu-*meso*-DAP (UDP-MurNAc-tripeptide) to produce **UDP-MurNAc-pentapeptide** [PMID 34047462]. This nucleotide precursor is then transferred to the lipid carrier (lipid I → lipid II), flipped across the membrane, and polymerized; the **terminal D-Ala-D-Ala** is the acyl-donor recognized by **penicillin-binding-protein transpeptidases** that cross-link glycan strands in the periplasm/cell wall — i.e., the step "required for subsequent extracellular transpeptidase crosslinking of the mature peptidoglycan polymer" [PMID 35382715].

Direct in-cell evidence that DdlB is the committed dipeptide-forming step comes from inhibitor studies: blocking Ddl produces "an increase in D-Ala intracellular pools accompanied by a commensurate decrease in D-Ala-D-Ala" [PMID 30300845].

### 4. Physiological / pharmacological significance

Because D-Ala-D-Ala is essential and has no human counterpart, Ddl/DdlB is a **validated antibacterial target** [PMID 34047462; 32497961]. The D-alanine analog **D-cycloserine** inhibits Ddl (and alanine racemase), competitively occupying the D-Ala subsites [PMID 23286234; 15948948]. Numerous DdlB-directed inhibitor chemotypes have been developed against the *E. coli* enzyme (diazenedicarboxamides, thiosemicarbazides, hydroxyethylamine phosphonates, flavonoids such as quercetin/apigenin) [PMID 17267218; 30300845; 19196510; 18774266]. The same subsite-2 chemistry that DdlB enforces (amide, not ester) is what glycopeptides (vancomycin) exploit by binding D-Ala-D-Ala directly; Van-type resistance re-routes the pathway to D-Ala-D-Lac, bypassing this step [PMID 32277698; 10801495]. These points are mechanistically informative for the precise role of PP_1339 in *P. putida*, though *P. putida* itself is not a clinical glycopeptide-resistance model.

---

## Supported vs. Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| Q88N74/PP_1339 is a D-Ala:D-Ala ligase (EC 6.3.2.4) forming D-Ala-D-Ala | **Supported** | Family/domain assignment + orthologue biochemistry [34047462; 35382715] |
| Reaction proceeds via ATP-grasp, acyl-phosphate intermediate, ordered mechanism | **Supported** | [21920581; 23286234; 19770507] |
| Enzyme is cytoplasmic; product used downstream (MurF → UDP-MurNAc-pentapeptide → extracellular cross-linking) | **Supported** | [34047462; 35382715; 30300845] |
| Wild-type DdlB is a D-Ala-D-Lac (Van-type) resistance ligase | **Refuted** | Subsite-2 of DdlB is amide-specific, distinct from VanA/VanB [10801495] |

---

## Evidence Quality and Limitations

- **Direct experimental evidence for PP_1339 (Q88N74) itself is lacking**; no *P. putida*-specific enzymology, structure, or knockout was found. The functional assignment rests on (a) unambiguous membership in the D-Ala-D-Ala ligase family via HAMAP MF_00047 and multiple InterPro domain signatures, and (b) deep, consistent biochemical/structural characterization of orthologues — most directly *E. coli* DdlB, the canonical family reference.
- The Ddl family is highly conserved and functionally uniform for the D-Ala:D-Ala reaction; the specificity-determining subsite-2 residues that distinguish D-Ala:D-Ala from D-Ala:D-Lac ligases are well defined, and DdlB-type enzymes are amide-forming. Kinetic parameters (K_m values, K⁺ activation) are expected to differ quantitatively in *P. putida* but not qualitatively.
- **Future directions:** direct confirmation for PP_1339 would come from recombinant expression + ADP/phosphate-coupled ligase assays, an AlphaFold/experimental structure superposed on *E. coli* DdlB to verify the two D-Ala subsites and ATP-grasp loops, and complementation of an *E. coli* ddlA ddlB auxotroph.

---

## References (PMIDs)
34047462, 35382715, 21920581, 23286234, 26894530, 19770507, 10801495, 15948948, 30300845, 32497961, 17267218, 19196510, 18774266, 32277698, 17090922.


## Artifacts

- [OpenScientist final report](ddlB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ddlB-deep-research-openscientist_artifacts/final_report.pdf)