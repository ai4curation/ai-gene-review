---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T00:17:30.547035'
end_time: '2026-08-11T00:34:19.178048'
duration_seconds: 1008.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cyoB
  gene_symbol: cyoB
  uniprot_accession: Q88PN6
  protein_description: 'RecName: Full=Cytochrome bo(3) ubiquinol oxidase subunit 1
    {ECO:0000256|ARBA:ARBA00014691}; EC=7.1.1.3 {ECO:0000256|ARBA:ARBA00012941}; AltName:
    Full=Cytochrome o ubiquinol oxidase subunit 1 {ECO:0000256|ARBA:ARBA00032190};
    AltName: Full=Oxidase bo(3) subunit 1 {ECO:0000256|ARBA:ARBA00030075}; AltName:
    Full=Ubiquinol oxidase polypeptide I {ECO:0000256|ARBA:ARBA00032435}; AltName:
    Full=Ubiquinol oxidase subunit 1 {ECO:0000256|ARBA:ARBA00031883};'
  gene_info: Name=cyoB {ECO:0000313|EMBL:AAN66438.1}; OrderedLocusNames=PP_0813 {ECO:0000313|EMBL:AAN66438.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the heme-copper respiratory oxidase family.
  protein_domains: Cyt_c_oxase-like_su1_dom. (IPR023616); Cyt_c_oxase-like_su1_sf.
    (IPR036927); Cyt_C_Oxase_1. (IPR000883); Cyt_c_Oxase_su1_BS. (IPR023615); Cyt_c_ubiqinol_oxidase_su1.
    (IPR014207)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: cyoB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cyoB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PN6
- **Protein Description:** RecName: Full=Cytochrome bo(3) ubiquinol oxidase subunit 1 {ECO:0000256|ARBA:ARBA00014691}; EC=7.1.1.3 {ECO:0000256|ARBA:ARBA00012941}; AltName: Full=Cytochrome o ubiquinol oxidase subunit 1 {ECO:0000256|ARBA:ARBA00032190}; AltName: Full=Oxidase bo(3) subunit 1 {ECO:0000256|ARBA:ARBA00030075}; AltName: Full=Ubiquinol oxidase polypeptide I {ECO:0000256|ARBA:ARBA00032435}; AltName: Full=Ubiquinol oxidase subunit 1 {ECO:0000256|ARBA:ARBA00031883};
- **Gene Information:** Name=cyoB {ECO:0000313|EMBL:AAN66438.1}; OrderedLocusNames=PP_0813 {ECO:0000313|EMBL:AAN66438.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the heme-copper respiratory oxidase family.
- **Key Domains:** Cyt_c_oxase-like_su1_dom. (IPR023616); Cyt_c_oxase-like_su1_sf. (IPR036927); Cyt_C_Oxase_1. (IPR000883); Cyt_c_Oxase_su1_BS. (IPR023615); Cyt_c_ubiqinol_oxidase_su1. (IPR014207)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cyoB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cyoB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cyoB** (gene ID: cyoB, UniProt: Q88PN6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *cyoB* (PP_0813, UniProt Q88PN6)
### Cytochrome *bo*₃ ubiquinol oxidase subunit I — *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**cyoB** (locus **PP_0813**, UniProt **Q88PN6**) encodes **subunit I of the cytochrome *bo*₃ ubiquinol oxidase** (EC 7.1.1.3), a member of the heme–copper respiratory oxidase superfamily. This subunit is the **catalytic core** of a terminal oxidase of the aerobic respiratory chain. It binds all of the enzyme's redox-active metal centers — a **low-spin heme *b*** and the **high-spin heme *o*₃–Cu_B binuclear center** — and there it carries out the enzyme's primary chemistry: **oxidation of ubiquinol (2 e⁻) coupled to the four-electron reduction of molecular O₂ to water**, using the released free energy to **pump protons across the cytoplasmic (inner) membrane** and generate proton-motive force. In *P. putida* KT2440 the enzyme (Cyo) is the **dominant terminal oxidase during aerobic exponential growth** and additionally acts as a **respiratory redox sensor** that feeds into global metabolic gene regulation.

The target identity is unambiguous and fully consistent with the UniProt record: gene symbol, EC number, protein family, and InterPro domains all match the primary literature on cytochrome *bo*₃/*cyo*.

---

## 2. Target Identity Verification

| Attribute | UniProt record | Verified in this study |
|---|---|---|
| Gene symbol | *cyoB* | ✔ Matches subunit I of *cyo* operon |
| Locus | PP_0813 | ✔ Confirmed within PP_0812–PP_0816 *cyoABCDE* cluster |
| Product | Cytochrome *bo*(3) ubiquinol oxidase subunit 1 | ✔ Consistent with all literature |
| EC | 7.1.1.3 | ✔ Ubiquinol:O₂ oxidoreductase (proton-pumping) |
| Family | Heme–copper respiratory oxidase | ✔ A-type oxygen reductase |
| Organism | *P. putida* KT2440 (taxid 160488) | ✔ |

**Bioinformatic confirmation.** A Needleman–Wunsch alignment of Q88PN6 (672 aa) against *E. coli* CyoB (P0ABI8) gave **69.1 % amino-acid identity**, and **all six catalytic metal-ligand histidines were strictly conserved at identical positions**: His106/His421 (low-spin heme *b*), His419 (high-spin heme *o*₃), and His284/His333/His334 (Cu_B). The **D-channel proton-pumping glutamate Glu286** was likewise strictly conserved, as were the **active-site cross-linked tyrosine Tyr288** (covalently linked to the Cu_B ligand His284; supplies the fourth electron/proton for O–O bond scission) and the **K-pathway lysine Lys362** — i.e., the entire canonical A-type catalytic and proton-input apparatus is intact in the *P. putida* protein. UniProt predicts **14 transmembrane helices** and a "Cytochrome oxidase subunit I profile" domain (res 39–559), matching the polytopic subunit-I fold. This conservation licenses transfer of the detailed, experimentally derived *E. coli* mechanism to the *P. putida* protein.

> The gene symbol *cyoB* is **not** ambiguous here; abundant primary literature on cytochrome *bo*₃ (chiefly from *E. coli*, plus *P. putida*-specific studies) directly describes this exact protein.

---

## 3. Primary Function: The Catalyzed Reaction and Substrate Specificity

### 3.1 Reaction
Cytochrome *bo*₃ catalyzes the **two-electron oxidation of ubiquinol and the reduction of molecular oxygen to water** [Welter et al. 1994, PMID 7961841]:

> 2 ubiquinol + O₂ (+ 8 H⁺_in) → 2 ubiquinone + 2 H₂O (+ 4 H⁺_out)

i.e., four electrons drawn from two ubiquinol molecules fully reduce O₂ to two H₂O, while additional protons are vectorially translocated (see §4). Subunit I (CyoB) is where the O₂ chemistry occurs: **"subunit I contains the binuclear center where oxygen is reduced to water"** [Park et al. 2002, PMID 12080058]. The center comprises **heme B at the low-spin site and heme O at the high-spin site of the binuclear center** [Uchida et al. 2000, PMID 11132640].

### 3.2 Substrate specificity
The physiological electron-donating substrate is **ubiquinol** — the reduced form of the membrane isoprenoid quinone pool (ubiquinol-8 in *E. coli*; *Pseudomonas* species use ubiquinone-9 as their major quinone). The enzyme also harbors a **single, tightly bound high-affinity ubiquinone-8** that is a genuine redox cofactor: because cytochrome *bo*₃ **lacks the Cu_A center** of cytochrome *c* oxidases, this bound quinone acts as the **"fourth electron" donor (a Cu_A substitute)** that rapidly re-reduces low-spin heme *b* and lets the O₂ reaction run to completion instead of stalling at the ferryl intermediate; reconstitution with ubiquinone-8 converts monophasic to multiphasic kinetics [Puustinen et al. 1996, PMID 8643669]. Thus there are effectively two quinone-binding sites (high- and low-affinity) [Musser & Chan 1998, PMID 9545462], and photoaffinity labelling with azido-ubiquinone localizes quinol binding to the subunit I/II region [Welter et al. 1994, PMID 7961841; Abramson et al. 2000, PMID 11017202].

### 3.3 Structural basis of the active site
The first structure of a ubiquinol oxidase — *E. coli* cytochrome *bo*₃ — revealed that **the membrane-spanning region of subunit I contains a cluster of polar residues exposed to the lipid bilayer that forms a quinone-binding site**, and mutagenesis supports specific roles for these residues in electron/proton transfer [Abramson et al. 2000, PMID 11017202]. The metal centers all reside in subunit I, the **common functional core** shared with cytochrome *c* oxidases [Gohlke et al. 1997, PMID 9135135].

---

## 4. Mechanism: Proton Pumping and Energy Conservation

Cytochrome *bo*₃ is an **A-type heme–copper oxygen reductase**. Proton transfer to the catalytic site uses **two well-defined pathways, the D- and K-pathways** [Lee et al. 2012, PMID 22056517]. The **D-pathway terminates at the strictly conserved Glu286** (helix VI of subunit I), which controls proton delivery **both to the active site for O₂ chemistry and to a proton-loading site for pumping**; mutation of E286 blocks proton flux and abolishes turnover, exclusively by inhibiting proton transfer in the *bo*₃ enzyme [Egawa et al. 2011, PMID 21684251; Svensson-Ek et al. 1996, PMID 8885847]. Time-resolved FTIR shows redox-linked perturbation of E286 during the catalytic cycle, implicating it directly in proton pumping [Bailey et al. 2002, PMID 11851414].

The net result is an **electrogenic, redox-driven proton pump**: electrons flow from ubiquinol through heme *b* to the heme *o*₃–Cu_B center to reduce O₂, while protons are pumped from the cytoplasm to the periplasm, contributing to the proton-motive force that powers ATP synthesis, transport, and motility. A quinol (Q-loop) contribution from the two quinone sites adds further charge separation unique to quinol oxidases [Musser & Chan 1998, PMID 9545462].

---

## 5. Holoenzyme Architecture and Cofactor Biosynthesis

CyoB is subunit I of a **four-subunit complex**. Partial sequencing of the purified *E. coli* enzyme identified subunits I, II and III as the **cyoB, cyoA and cyoC gene products** (~58, 33, 22 kDa), plus subunit IV (cyoD, ~17 kDa) [Minghetti et al. 1992, PMID 1322173]. Metal analysis shows **2 equivalents of iron (heme *b* + heme *o*₃) but only 1 equivalent of copper (Cu_B); the Cu_A center is absent** [Minghetti et al. 1992, PMID 1322173]. Accessory-subunit studies show **subunit IV (CyoD) is required for Cu_B insertion into subunit I**, acting as a domain-specific assembly chaperone that contacts helices VII/VIII (the Cu_B-binding region) of subunit I [Saiki et al. 1997, PMID 9169436].

**Operon and cofactor supply (bioinformatic, *P. putida*-specific).** A UniProt query of *P. putida* KT2440 resolves a **syntenic *cyoABCDE* operon**: PP_0812 *cyoA* (subunit II, Q88PN7) – **PP_0813 *cyoB* (subunit I, Q88PN6)** – PP_0814 *cyoC* (subunit III, Q88PN5) – PP_0815 *cyoD* (subunit IV, Q88PN4) – PP_0816 *cyoE2* (**protoheme IX farnesyltransferase / heme-O synthase**, Q88PN3). CyoE converts protoheme IX to **heme O**, the cofactor inserted into subunit I's high-spin (o₃) site [Minghetti et al. 1992, PMID 1322173]. The operon organization matches the *E. coli* prototype, corroborating that CyoB assembles and functions identically.

---

## 6. Localization

CyoB carries out its function **embedded in the cytoplasmic (inner) membrane**. UniProt predicts **14 helical transmembrane spans** (res 16–604), consistent with a deeply membrane-embedded catalytic subunit. The cytochrome *bo*₃ complex is an inner-membrane protein assembly: its subunit II (CyoA) is integrated/translocated across the *E. coli* inner membrane via the **YidC and SecYEG** pathways [van Bloois et al. 2006, PMID 16481320; Celebi et al. 2008, PMID 18155041]. The hemes and Cu_B of subunit I lie within the membrane; ubiquinol (a lipid-soluble substrate) is oxidized at a membrane-buried Q-site, and protons are translocated vectorially across the same membrane (cytoplasm → periplasm).

---

## 7. Biological Process / Pathway Context in *P. putida* KT2440

*P. putida* KT2440 has a **branched aerobic respiratory chain with multiple terminal oxidases** — Cyo (*bo*₃), CIO (cyanide-insensitive), cbb₃-1, cbb₃-2 and aa₃ — whose relative use varies with O₂ and growth phase [Morales et al. 2006, PMID 16958757; Ugidos et al. 2008, PMID 18341582]. Functional assays show **Cyo has a leading role during aerobic exponential growth**, while cbb₃-1 dominates in stationary phase/low O₂ [Ugidos et al. 2008, PMID 18341582]. Expression is oxygen-responsive and coordinated by the **ANR global regulator**, which binds the *cyo* promoter [Ugidos et al. 2008, PMID 18341582].

Beyond bioenergetics, the Cyo oxidase acts as a **respiratory signal transmitter**: inactivation of *cyo* has little effect on growth rate but **broadly remodels the transcriptome and relieves the global (catabolite) control that represses alkane-degradation genes**, identifying *cyo* specifically as **"the oxidase that transmits a regulatory signal related to the activity of the electron transport chain"**; loss of *cyo* is compensated by up-regulation of the CIO and cbb₃-1 oxidases [Morales et al. 2006, PMID 16958757]. This links CyoB's catalytic (electron-transport) activity to metabolic gene regulation in this environmentally and biotechnologically important soil bacterium.

---

## 8. Evidence Summary

| Claim | Evidence type | Source |
|---|---|---|
| Subunit I holds the O₂-reducing binuclear center | Biochemistry / two-hybrid | PMID 12080058 |
| Cofactors: low-spin heme *b* + high-spin heme *o*₃ | EPR / Raman | PMID 11132640 |
| Reaction: 2e⁻ ubiquinol oxidation + O₂→H₂O | Enzymology | PMID 7961841 |
| Quinone-binding site in subunit I | X-ray structure + mutagenesis | PMID 11017202 |
| Bound Q8 substitutes for Cu_A | Flow-flash kinetics | PMID 8643669 |
| Glu286 required for proton transfer/pumping | Mutagenesis / FTIR | PMID 8885847, 21684251, 11851414 |
| A-type oxidase; D-/K-pathways | Review | PMID 22056517 |
| Six conserved His in subunit I | Comparative / structural | PMID 9545462; this study (69.1 % id, all 6 His conserved) |
| Active-site Tyr288 + K-pathway Lys362 conserved | Sequence alignment | This study |
| 2 Fe + 1 Cu, no Cu_A; four subunits = cyoBAC(D) | Metal analysis / sequencing | PMID 1322173 |
| CyoD chaperones Cu_B insertion | Mutagenesis | PMID 9169436 |
| Inner-membrane localization | Biogenesis studies | PMID 16481320, 18155041 |
| Dominant oxidase in aerobic exponential growth (*P. putida*) | Functional assays | PMID 18341582 |
| Respiratory signalling role (*P. putida*) | Microarray / RT-PCR | PMID 16958757 |
| cyoABCDE operon = PP_0812–0816 | Genomic query | This study (UniProt) |

---

## 9. Supported and Refuted Hypotheses

**Supported**
- CyoB is the catalytic subunit I of cytochrome *bo*₃ ubiquinol oxidase (identity confirmed by annotation, 69.1 % identity to *E. coli* CyoB, and strict conservation of all six metal ligands + Glu286).
- Primary function = ubiquinol:O₂ oxidoreductase that reduces O₂ to water and pumps protons.
- Localizes to and functions within the inner membrane.
- In *P. putida*, it is the principal aerobic-growth terminal oxidase and a respiratory regulatory sensor.

**Refuted / excluded**
- CyoB is **not** a cytochrome *c* oxidase (no Cu_A; electrons enter from ubiquinol, not cytochrome *c*).
- The gene is **not** ambiguous or mis-assigned; no competing gene with the same symbol confounds the annotation.

---

## 10. Limitations and Future Directions

- Most mechanistic/structural data derive from the orthologous *E. coli* enzyme; no *P. putida* CyoB crystal/cryo-EM structure or direct enzymology was found. The very high conservation makes transfer of mechanism robust, but organism-specific kinetic parameters (e.g., quinol specificity for ubiquinol-9, O₂ affinity) remain to be measured directly.
- The precise molecular link between Cyo electron-transport activity and the alkane-degradation regulatory signal in *P. putida* is phenomenological; the downstream signalling components are not fully defined.
- Proton-pumping stoichiometry (H⁺/e⁻) was not directly quantified here; the A-type consensus (~1 pumped H⁺ per electron, plus scalar/chemical protons) is inferred from the superfamily.

---

*Report compiled from primary literature and bioinformatic analysis (sequence alignment and genome operon mapping). All quantitative sequence claims were computed in this study against UniProt reference sequences Q88PN6 and P0ABI8.*


## Artifacts

- [OpenScientist final report](cyoB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cyoB-deep-research-openscientist_artifacts/final_report.pdf)