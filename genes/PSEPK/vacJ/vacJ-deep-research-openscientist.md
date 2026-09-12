---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:37:33.949261'
end_time: '2026-09-01T02:47:48.259072'
duration_seconds: 614.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: vacJ
  gene_symbol: vacJ
  uniprot_accession: Q88KX6
  protein_description: 'SubName: Full=VacJ lipoprotein {ECO:0000313|EMBL:AAN67776.1};'
  gene_info: Name=vacJ {ECO:0000313|EMBL:AAN67776.1}; OrderedLocusNames=PP_2163 {ECO:0000313|EMBL:AAN67776.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MlaA family.
  protein_domains: MlaA. (IPR007428); MlaA (PF04333)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
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
  path: vacJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: vacJ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KX6
- **Protein Description:** SubName: Full=VacJ lipoprotein {ECO:0000313|EMBL:AAN67776.1};
- **Gene Information:** Name=vacJ {ECO:0000313|EMBL:AAN67776.1}; OrderedLocusNames=PP_2163 {ECO:0000313|EMBL:AAN67776.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MlaA family.
- **Key Domains:** MlaA. (IPR007428); MlaA (PF04333)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "vacJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'vacJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **vacJ** (gene ID: vacJ, UniProt: Q88KX6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *vacJ* / MlaA (Q88KX6, PP_2163) in *Pseudomonas putida* KT2440

## 0. Identity verification (mandatory)

| Attribute | Value | Status |
|---|---|---|
| UniProt accession | **Q88KX6** | Confirmed |
| Gene name / locus | *vacJ* / **PP_2163** | Confirmed |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | Confirmed |
| Protein length | 235 aa | Confirmed by sequence retrieval |
| Family | **MlaA family** | Confirmed |
| Domain | **MlaA** — Pfam **PF04333**, InterPro **IPR007428** | Confirmed by UniProt cross-reference |
| Signal peptide | residues 1–31 (Sec signal), mature chain 32–235 | From UniProt automated annotation |

**The gene symbol matches the protein.** "VacJ" and "MlaA" are two names for the *same* protein: MlaA "was initially identified — and called VacJ — based on its role in the intracellular spreading of *Shigella flexneri*" (Kaur & Mingeot-Leclercq 2024, PMID 38802775). The single MlaA domain that spans essentially the whole protein confirms this is the outer-membrane component of the **Mla (Maintenance of Lipid Asymmetry)** system and not an unrelated protein sharing the symbol. No conflicting gene of the same symbol was encountered. Research below therefore proceeds with confidence.

*Caveat on the "lipoprotein" label:* The EMBL/UniProt description reads "VacJ lipoprotein," but the automated UniProt feature set annotates a **cleavable Sec signal peptide (1–31)** rather than a lipobox with a lipidated +1 cysteine. Baarda et al. (2019, PMID 30845186) explicitly showed that MlaA orthologs fall into **two classes — with or without a lipoprotein signal peptide**. Whether the *P. putida* ortholog is triacylated at its N-terminus should therefore be treated as **inferred from homology, not experimentally established** here. This does not change its assignment to the MlaA family or its function.

---

## 1. Summary (answer to the research question)

*vacJ* (PP_2163) encodes **MlaA/VacJ**, the outer-membrane (OM) component of the six-protein **Mla phospholipid-trafficking system** (MlaA–OmpC/F | MlaC | MlaFEDB). Its primary molecular function is **not enzymatic**: it is a lipid-handling protein that **removes glycerophospholipids that have become mislocalized in the outer (surface-exposed) leaflet of the outer membrane** and transfers them, via the periplasmic shuttle MlaC, toward the inner-membrane ABC transporter MlaFEDB for **retrograde return to the inner membrane**. By continuously clearing phospholipids from the LPS-rich outer leaflet, MlaA **maintains outer-membrane lipid asymmetry**, which is the structural basis of the OM permeability barrier. It performs this task **embedded in the outer membrane in complex with the trimeric porin OmpC/OmpF**, acting at the periplasmic face of the OM.

---

## 2. Biological context: the Mla system

Gram-negative bacteria build an asymmetric OM with **lipopolysaccharide (LPS) in the outer leaflet and glycerophospholipids (GPLs) in the inner leaflet**; this asymmetry makes the OM an effective barrier against antibiotics, bile salts and other toxic compounds (Low & Chng 2021, PMID 34753108; Kaur & Mingeot-Leclercq 2024, PMID 38802775). Stress and normal metabolism cause GPLs to leak into the outer leaflet, degrading the barrier. The **OmpC–Mla system counteracts this by retrograde transport of the mislocalized GPLs back to the inner membrane** (Low & Chng 2021, PMID 34753108).

The system has three physical modules across the cell envelope (Wotherspoon et al. 2024, PMID 39080293):
1. **MlaA–OmpC/F** — the OM extraction complex (**the product of *vacJ***, partnered with a porin);
2. **MlaC** — a soluble periplasmic phospholipid shuttle/chaperone;
3. **MlaFEDB** — the inner-membrane ABC transporter complex (MlaD hexamer + MlaE permease + MlaF ATPase + MlaB regulator).

---

## 3. Primary function and substrate specificity

**Reaction/role:** MlaA is a **lipid transporter / lipid-extraction module, not a catalytic enzyme.** It has no active site that modifies a chemical bond; instead it selectively engages and extracts a lipid substrate.

**Substrate:** **glycerophospholipids mislocalized to the outer leaflet of the OM.** MlaA is "involved in the removal of glycerophospholipids that are mis-localized at the outer leaflet of the OM" (PMID 38802775). It does not act on LPS. The downstream periplasmic carrier MlaC accepts lipids with as many as two acyl chains across several classes (glycerophospholipids, and also fatty acids/sphingolipids in vitro; James et al. 2024, PMID 39038171), indicating the pathway's specificity is for diacyl/monoacyl-chain lipids consistent with membrane GPLs.

**Mechanism (structural evidence):** Yeow, Luo & Chng (2023, PMID 38092770) solved a 2.9 Å cryo-EM structure of a disulfide-trapped **OmpC–MlaA–MlaC complex in nanodiscs** and showed that **the OmpC–MlaA complex transfers PLs to MlaC**, with **membrane thinning proposed as the strategy that directs lipids for transport**, and electrostatic interactions recruiting MlaC to the OM. Deep-mutational-scanning + AlphaFold2 work (MacRae et al. 2023, PMID 37100290) mapped the MlaC–MlaA and MlaC–MlaD interfaces and argued MlaC binds MlaA **or** MlaD one at a time — consistent with MlaC acting as a ferry between the OM (MlaA) and IM (MlaD) ends of the pathway. On the inner-membrane side, cryo-EM of **MlaFEDB** with phospholipid/ADP/AMP-PNP plus reconstituted transport assays established the ATP-driven step and confirmed, in a proteoliposome system including MlaA–OmpF and MlaC, the **direction of phospholipid movement** (Tang et al. 2021, PMID 33199922). A 2026 computational study (Dutta et al., PMID 41047745) further proposes a **"bait–capture–pull"** ligand-transport mechanism and highlights the dynamic C-terminal extension of MlaA that protrudes into the periplasm.

> Note on directionality: The field's consensus role for MlaA in barrier maintenance is **retrograde** (OM→IM) clearance of surface phospholipids (PMID 34753108, 38092770, 38802775). MlaA's characterized activity is **extraction of GPLs from the OM outer leaflet**, which is the barrier-preserving function relevant to annotation. Evolutionary/comparative work reinforces this direction: in *Veillonella parvula* the Mla system and the **TamB** system were shown to "have opposite GPL trafficking functions" (Grasekamp et al. 2023, PMID 37993432), i.e., Mla/MlaA drives **removal** of outer-leaflet GPLs, opposite to anterograde phospholipid delivery. The Silhavy lab likewise defines the pathway concisely as "**the outer membrane channel MlaA**, the periplasmic lipid carrier MlaC, and the inner membrane transporter MlaBDEF" (Guest et al. 2023, PMID 37463202).

**Genomic organization in *P. putida* KT2440 (computational evidence).** Neighborhood analysis of the KT2440 genome shows *vacJ*/PP_2163 is flanked by functionally unrelated genes (*queF*, *parA*, a PilZ-domain protein, a response regulator) — it is **not** part of an *mla* operon. The inner-membrane transporter genes are encoded separately and adjacently as **mlaF (Q88P94) – mlaE (Q88P93) – mlaD (Q88P92)**, and the periplasmic MlaC/regulatory MlaB functions are also expected in the proteome. This is the **canonical genetic arrangement** (mlaA/vacJ transcribed apart from the mlaFEDCB operon) seen in *E. coli* and other Gram-negatives, and confirms that **all physical modules of the Mla system are present in KT2440** — i.e., PP_2163 is the OM arm of an intact, conserved pathway, not an orphan gene.

---

## 4. Localization — where the product acts

- **Outer membrane.** "Located within the outer membrane, MlaA (VacJ) acts as a channel to shuttle phospholipids from the outer leaflet" (Baarda et al. 2019, PMID 30845186). The MlaA–OmpC complex is "situated within the outer membrane" (Wotherspoon et al. 2024, PMID 39080293).
- **In complex with a porin.** MlaA does not stand alone in the OM; it associates with trimeric **OmpC/OmpF** porin, forming the OM extraction platform.
- **Functional face = periplasmic side of the OM outer leaflet.** MlaA extracts lipids from the outer leaflet and hands them to the **periplasmic** MlaC; its C-terminal extension projects into the periplasm (PMID 41047745).
- **Envelope targeting of Q88KX6.** The retrieved sequence carries an N-terminal signal (residues 1–31) that routes the protein through the Sec pathway to the envelope; the mature domain (32–235) is the MlaA module. (Lipidation status — see §0 caveat.)

The other pathway members occupy the **periplasm (MlaC)** and the **inner membrane (MlaFEDB)**, so the complete pathway spans the cell envelope, with *vacJ*'s product anchoring the OM end.

---

## 5. Pathway integration and physiological consequences

MlaA is the entry node of the retrograde phospholipid circuit: **OM outer-leaflet GPL → MlaA(–OmpC) → MlaC (periplasm) → MlaFEDB (inner membrane).** Its physiological output is **maintenance of OM lipid asymmetry and barrier integrity.** Evidence from loss-of-function studies (mechanistically consistent across species) includes:

- **Outer-membrane vesicle (OMV) biogenesis.** The VacJ/Yrb (Mla) system is a general regulator of OMV formation: "Deletion or repression of VacJ/Yrb increases OMV production" in *H. influenzae* and *V. cholerae*, with **OMVs enriched in phospholipids**, and OMV production/Mla regulation **responding to iron starvation** (Roier et al. 2016, PMID 26806181). The proposed general mechanism is **phospholipid accumulation in the OM outer leaflet** when Mla is lost. *N. gonorrhoeae* ΔmlaA released ~1.7-fold more vesicles (PMID 30845186).
- **Regulation.** MlaA levels increase in stationary phase and under anaerobiosis and decrease during iron starvation in *N. gonorrhoeae* (PMID 30845186); the *H. influenzae/V. cholerae* system is likewise iron-responsive (PMID 26806181) — indicating the pathway is tuned to envelope-stress and nutrient cues.
- **Pseudomonas-specific phenotypes.** In the close relative *P. aeruginosa*, "mlaA deletion … results in … an increase in fluoroquinolones susceptibility and in PQS … and TNF-α release and a decrease in rhamnolipids secretion, motility and biofilm formation" (Kaur et al. 2023, PMID 37660742) — i.e., a weakened OM barrier (more antibiotic entry) plus surfactant/motility/biofilm changes.

**Interpretation for *P. putida* KT2440.** KT2440 is a non-pathogenic, solvent-tolerant soil saprophyte. The *vacJ*/Mla function here is best understood as **envelope robustness and permeability-barrier maintenance** — plausibly important for its notable tolerance to organic solvents and environmental stress — rather than host-directed virulence. The virulence phenotypes reported in pathogens (Shigella spreading, gonococcal fitness) are species-specific downstream effects of the same conserved lipid-asymmetry function and should not be over-interpreted for KT2440. Direct experimental characterization of PP_2163 specifically is limited; its annotation rests on strong domain/family homology plus well-characterized orthologs.

---

## 6. Supported vs. refuted hypotheses

**Supported (by literature + sequence/domain evidence):**
- H1. Q88KX6/PP_2163 is the MlaA/VacJ OM component of the Mla system. ✔ (Pfam PF04333/IPR007428; PMID 38802775)
- H2. Its substrate is outer-leaflet glycerophospholipid; it is a lipid transporter, not an enzyme. ✔ (PMID 38802775, 38092770)
- H3. It localizes to the OM in complex with OmpC/OmpF and hands lipid to periplasmic MlaC. ✔ (PMID 30845186, 39080293, 38092770)
- H4. Its loss compromises OM asymmetry → increased OMVs/permeability. ✔ (PMID 26806181, 37660742, 30845186)

**Refuted / not supported:**
- That vacJ is a secreted virulence toxin or a catalytic enzyme — **refuted**; it is a structural/transport lipid-handling protein of the envelope.
- That the "lipoprotein" name guarantees N-terminal lipidation of the *P. putida* ortholog — **not supported** by the automated signal-peptide annotation; lipidation is uncertain (§0).

---

## 7. Limitations and future directions

- **No PP_2163-specific wet-lab study** was found; functional claims are transferred from orthologs (*E. coli*, *P. aeruginosa*, *H. influenzae*, *V. cholerae*, *N. gonorrhoeae*) supported by an unambiguous domain assignment.
- **Lipidation/exact topology** of the *P. putida* protein is unresolved — a targeted experiment (globomycin sensitivity, Edman/MS of the mature N-terminus) would settle the lipoprotein question.
- **Direct substrate/lipidomic profiling** of a *P. putida* Δ*vacJ* mutant (OM leaflet lipid composition, OMV output, solvent/antibiotic tolerance) would confirm the barrier role in this organism. Note that *P. putida* solvent tolerance is known to involve OM/phospholipid remodeling (e.g., *cis→trans* fatty-acid isomerization, cardiolipin/PE head-group changes, OprL; Ramos et al. 1997, PMID 9020089), but **no study to date directly links *vacJ*/PP_2163 to solvent tolerance**; this remains an untested but plausible hypothesis given MlaA's role in OM barrier integrity.
- **Structural confirmation** (cryo-EM of *P. putida* MlaA–OmpC) would verify porin partnership in Pseudomonas.

---

## 8. Key references
- Kaur & Mingeot-Leclercq 2024, *review*, PMID 38802775 — MlaA=VacJ, OM lipoprotein, retrograde GPL transport.
- Yeow, Luo & Chng 2023, PMID 38092770 — cryo-EM OmpC–MlaA–MlaC; MlaA→MlaC lipid transfer; membrane thinning.
- Low & Chng 2021, *review*, PMID 34753108 — integrated OmpC–Mla retrograde mechanism.
- Wotherspoon et al. 2024, PMID 39080293 — three-module architecture; MlaC–MlaD structure.
- MacRae et al. 2023, PMID 37100290 — MlaC–MlaA/MlaD interfaces (DMS + AlphaFold2).
- Tang et al. 2021, PMID 33199922 — MlaFEDB structures; transport-direction assays.
- Baarda et al. 2019, PMID 30845186 — OM localization/channel; two MlaA signal-peptide classes; vesiculation.
- Roier et al. 2016, PMID 26806181 — VacJ/Yrb controls OMV biogenesis; iron regulation.
- Kaur et al. 2023, PMID 37660742 — *P. aeruginosa* mlaA phenotypes.
- Dutta et al. 2026, PMID 41047745 — computational MlaA dynamics; "bait–capture–pull."
- Grasekamp et al. 2023, PMID 37993432 — Mla vs TamB opposite trafficking; MlaA extracts outer-leaflet GPLs; deep conservation across diderms.
- Guest et al. (Silhavy lab) 2023, PMID 37463202 — MlaA defined as the OM channel of the Mla pathway.

## 9. P. putida-specific genomic evidence (this work)
- PP_2163/*vacJ* (Q88KX6): MlaA-domain protein, unlinked from the *mla* operon (UniProt neighborhood analysis).
- KT2440 inner-membrane Mla transporter: **mlaF Q88P94, mlaE Q88P93, mlaD Q88P92** (adjacent locus) — confirming the complete pathway is present in this organism.


## Artifacts

- [OpenScientist final report](vacJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](vacJ-deep-research-openscientist_artifacts/final_report.pdf)