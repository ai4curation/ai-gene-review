---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:07:37.581364'
end_time: '2026-07-23T16:14:43.676246'
duration_seconds: 426.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: accD
  gene_symbol: accD
  uniprot_accession: Q88LD9
  protein_description: 'RecName: Full=Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit beta {ECO:0000255|HAMAP-Rule:MF_01395}; Short=ACCase subunit beta {ECO:0000255|HAMAP-Rule:MF_01395};
    Short=Acetyl-CoA carboxylase carboxyltransferase subunit beta {ECO:0000255|HAMAP-Rule:MF_01395};
    EC=2.1.3.15 {ECO:0000255|HAMAP-Rule:MF_01395};'
  gene_info: Name=accD {ECO:0000255|HAMAP-Rule:MF_01395}; OrderedLocusNames=PP_1996;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the AccD/PCCB family. {ECO:0000255|HAMAP-
  protein_domains: AcCoA_carboxyl_beta. (IPR034733); Acetyl_CoA_COase_Trfase_b_su.
    (IPR000438); ClpP/crotonase-like_dom_sf. (IPR029045); COA_CT_N. (IPR011762); Znf-ACC.
    (IPR041010)
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
  path: accD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: accD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LD9
- **Protein Description:** RecName: Full=Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta {ECO:0000255|HAMAP-Rule:MF_01395}; Short=ACCase subunit beta {ECO:0000255|HAMAP-Rule:MF_01395}; Short=Acetyl-CoA carboxylase carboxyltransferase subunit beta {ECO:0000255|HAMAP-Rule:MF_01395}; EC=2.1.3.15 {ECO:0000255|HAMAP-Rule:MF_01395};
- **Gene Information:** Name=accD {ECO:0000255|HAMAP-Rule:MF_01395}; OrderedLocusNames=PP_1996;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the AccD/PCCB family. {ECO:0000255|HAMAP-
- **Key Domains:** AcCoA_carboxyl_beta. (IPR034733); Acetyl_CoA_COase_Trfase_b_su. (IPR000438); ClpP/crotonase-like_dom_sf. (IPR029045); COA_CT_N. (IPR011762); Znf-ACC. (IPR041010)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "accD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'accD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **accD** (gene ID: accD, UniProt: Q88LD9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **accD** (Q88LD9) — Acetyl-CoA carboxylase carboxyltransferase β-subunit

**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), abbrev. **PSEPK**
**Gene:** *accD* — OrderedLocusName **PP_1996**
**Protein:** Acetyl-coenzyme A carboxylase carboxyltransferase subunit β (ACCase subunit β)
**EC number:** 2.1.3.15
**Protein family:** AccD/PCCB family
**UniProt:** Q88LD9

---

## 1. Summary (Answer to the Research Question)

**accD** encodes the **β-subunit of the carboxyltransferase (CT) component of acetyl-CoA carboxylase (ACC)**, a large biotin-dependent multi-subunit enzyme that catalyzes the **first committed and rate-limiting step of fatty-acid (and membrane phospholipid) biosynthesis**: the ATP-dependent carboxylation of acetyl-CoA to **malonyl-CoA** (overall EC 6.4.1.2; the CT partial reaction is EC 2.1.3.15). In bacteria the holoenzyme is built from four separately encoded proteins — **AccC** (biotin carboxylase, BC), **AccB** (biotin carboxyl carrier protein, BCCP), and the two carboxyltransferase subunits **AccA** (α) and **AccD** (β). AccA and AccD assemble into an **α₂β₂ heterotetramer** that catalyzes the **second half-reaction**: transfer of the carboxyl group from carboxybiotin (carried on BCCP) onto acetyl-CoA to form malonyl-CoA [PMID 23594205; 19965770]. AccD's substrate is acetyl-CoA (with carboxybiotin-BCCP as the CO₂ donor), and its product is malonyl-CoA. The enzyme is a **soluble cytoplasmic** protein. A defining, **bacteria-specific zinc-binding domain** resides on the β/AccD subunit, making the bacterial CT a validated selective antibacterial drug target [PMID 16460018].

> **Identity verification.** The UniProt description (accD; carboxyltransferase β-subunit; EC 2.1.3.15; AccD/PCCB family; domains COA_CT_N, AcCoA_carboxyl_beta, ClpP/crotonase-like fold, Znf-ACC) matches the well-characterized bacterial ACC carboxyltransferase β-subunit exactly. All literature cited below concerns this enzyme family in Gram-negative γ-proteobacteria (*E. coli*, *Haemophilus*, *Pseudomonas*), of which *P. putida* KT2440 is a member. The gene symbol is **not** ambiguous. Because no primary study is devoted specifically to *P. putida* PP_1996, its function is assigned by **strong homology/HAMAP rule MF_01395**, with the mechanism established biochemically and structurally in closely related bacteria.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

### 2.1 Overall reaction
Acetyl-CoA carboxylase catalyzes:

> **acetyl-CoA + HCO₃⁻ + ATP → malonyl-CoA + ADP + Pᵢ**

This is **the first committed step in fatty-acid synthesis** and is the pathway's principal regulatory/rate-limiting valve [PMID 29100983; 39572150].

### 2.2 Two half-reactions — AccD acts in the second
The biotin-dependent mechanism proceeds in two spatially separated half-reactions [PMID 23594205; 29100983; 26020841]:

1. **Half-reaction 1 (biotin carboxylase, AccC + AccB):** ATP-dependent carboxylation of the vitamin **biotin**, which is covalently attached to a lysine of **BCCP (AccB)**, using **bicarbonate** as the CO₂ source → **carboxybiotin-BCCP**.
2. **Half-reaction 2 (carboxyltransferase, AccA + AccD + AccB):** **AccD together with AccA** catalyzes transfer of the carboxyl group from **carboxybiotin-BCCP onto acetyl-CoA**, yielding **malonyl-CoA** and regenerating biotin-BCCP.

**AccD is one of the two catalytic subunits of the carboxyltransferase (CT) active site.** The CT is an **α₂β₂ heterotetramer** (α = AccA, β = AccD); its two active sites are each formed at an **α/β subunit interface**, and the two sites are functionally coupled ("active-site communication") [PMID 19965770; 18156466; 23594205].

### 2.3 Substrate specificity
- **Carboxyl acceptor / defining substrate:** **acetyl-CoA** (a 2-carbon acyl-CoA). The bacterial ACC is specific for acetyl-CoA (distinguishing it from the homologous propionyl-CoA carboxylases of the AccD/PCCB family that act on propionyl-CoA).
- **Carboxyl donor:** **carboxybiotin** tethered to BCCP (AccB).
- **Product:** **malonyl-CoA** (+ regenerated biotin-BCCP).
- The reaction is readily reversible in vitro (malonyl-CoA + biotin ⇌ acetyl-CoA + carboxybiotin), which is the basis of standard CT activity assays [PMID 16460018; 39572150].

---

## 3. Structure and Structural Basis of Function

### 3.1 Fold and domain architecture
The CT subunits (AccA and AccD) belong to the **ClpP/crotonase-like superfamily fold** (InterPro IPR029045), the conserved "CoA carboxyltransferase" (CT) fold shared with the β-subunits of propionyl-/methylcrotonyl-CoA carboxylases (AccD/PCCB family) [UniProt Q88LD9 domains]. The Q88LD9 domain complement — **COA_CT_N (IPR011762)**, **Acetyl_CoA_COase_Trfase_b_su (IPR000438)**, **AcCoA_carboxyl_beta (IPR034733)** — is the canonical β-CT signature.

### 3.2 The bacteria-specific zinc domain (a key discovery)
High-resolution crystal structures of the CT component from *E. coli* (3.0 Å) and *Staphylococcus aureus* (2.0 Å) revealed a **small, independent zinc-binding domain that has no counterpart in the eukaryotic ACC** [PMID 16460018]. This zinc finger:
- resides on the **β-subunit (AccD)** and is coordinated by **four cysteines** (a Cys₄ Zn site; corresponds to the Q88LD9 annotation **Znf-ACC, IPR041010**);
- is **required for catalytic activity** — mutation of the four cysteines to alanine abolishes nucleic-acid binding **and** diminishes catalysis, indicating the Zn domain is important for CT structural integrity/function [PMID 19965770].

The structural distinctiveness of this domain is the central reason bacterial CT (and the AccD subunit specifically) is repeatedly highlighted as a **selective antibacterial target** that spares the human enzyme [PMID 16460018; 23499019; 39572150].

### 3.3 Assembly into the holoenzyme
Individual bacterial ACC subunits (BC homodimer, BCCP, and the α₂β₂ CT) associate into a **multimeric holo-complex**; pull-down and kinetic studies in *E. coli* show that the two catalytic sites (BC and CT) **interact** and that complex formation occurs (and is not abolished by acetyl-CoA, ATP analogs, or mRNA) [PMID 23594205; 23499019]. Thus AccD functions **in the context of an assembled ACC complex**, not as an isolated protein.

---

## 4. Subcellular Localization

In bacteria, acetyl-CoA carboxylase — including the AccA/AccD carboxyltransferase — is a **soluble, cytoplasmic enzyme complex** [PMID 23594205]. Catalysis (malonyl-CoA formation) occurs in the **cytosol**, where malonyl-CoA is then handed to the soluble type II fatty-acid-synthase (FAS II) machinery. (This contrasts with plants, where the heteromeric ACCase is plastid-localized and its α-CT associates with the plastid inner-envelope membrane [PMID 39489480]; and with the cytosolic multidomain ACC of mammals.) For *P. putida*, a Gram-negative γ-proteobacterium, the *E. coli* cytoplasmic paradigm applies.

---

## 5. Pathway Context and Biological Process

### 5.1 Position in metabolism
AccD/ACC sits at the **entry point of type II fatty-acid biosynthesis (FAS II)**:

`acetyl-CoA → (ACC: AccABCD) → malonyl-CoA → (FabD: malonyl-CoA:ACP transacylase) → malonyl-ACP → iterative condensation/reduction (FabB/F, FabG, FabA/Z, FabI) → acyl-ACP → membrane phospholipids`

Malonyl-CoA produced by the AccD-containing CT is the **universal two-carbon extender unit** for every elongation cycle of fatty-acid synthesis and is therefore essential for **membrane phospholipid biogenesis** [PMID 19362649; 8246839]. In many bacteria malonyl-CoA is additionally the extender for **polyketide** biosynthesis, linking ACC to secondary metabolism [PMID 19362649; 41203165].

### 5.2 Regulation of the step
Because this is the committed step, it is tightly controlled:
- **Product/end-product feedback:** ACC is allosterically inhibited by long-chain **acyl-ACP** (e.g., palmitoyl-ACP), which acts in a time-dependent (hysteretic) manner — coupling ACC output to the cell's demand for acyl chains [PMID 29100983].
- **Metabolic sensing / proposed moonlighting:** The CT (AccA/AccD) was proposed to act as a "dimmer switch," binding *accA*/*accD* mRNA through the β-subunit zinc finger to repress its own translation, an effect relieved by the substrate acetyl-CoA [PMID 19965770]. **However, subsequent in vivo work found no detectable effect of excess CT tetramer on translation of the CT mRNAs, arguing against physiologically significant translational repression** [PMID 25157077]. Nonspecific nucleic-acid (DNA/RNA/heparin) binding by CT also inhibits catalysis in vitro and was used to probe active-site communication [PMID 18156466]. The **primary, well-supported role of AccD is enzymatic** (carboxyl transfer); the regulatory RNA-binding role remains unresolved.
- **Transcriptional control:** dedicated activators tuning *acc* gene expression in response to acetyl-CoA have been described in other γ-proteobacteria (e.g., AccR in *Shewanella*) [PMID 39475184].

### 5.3 Gene organization in Pseudomonas
In *P. aeruginosa* (a close relative), **accB and accC form a two-gene operon**, while **accA and accD are dispersed elsewhere on the genome**, not adjacent to accBC — mirroring the four separately located *acc* loci of *E. coli* [PMID 7693652]. The *P. putida* KT2440 locus tag **PP_1996** for *accD* is consistent with this dispersed arrangement. This physical separation of the four subunit genes creates a **subunit-stoichiometry coordination problem** that motivated the (now-disputed) autoregulation hypothesis above.

---

## 6. Essentiality and Significance as a Drug Target

Fatty-acid synthesis is **essential** in most bacteria, and ACC catalyzes its committed step; consequently AccD/ACC is essential for viability and growth. The bacterial CT's **unique zinc domain and the two-component (BC + CT) architecture** — absent from the single-chain eukaryotic ACC — make it an actively pursued **antibacterial (and herbicidal/insecticidal in eukaryotic ACC contexts) drug target** [PMID 16460018; 23499019; 36459397; 39572150]. Comparative structural/in-silico analyses continue to nominate bacterial ACCase as a target across Gram-positive and Gram-negative pathogens [PMID 42379113].

---

## 7. Evidence Summary and Confidence

| Claim | Evidence type | Confidence | Key refs |
|---|---|---|---|
| accD = β-subunit of ACC carboxyltransferase (α₂β₂) | Genetics + biochemistry (*E. coli*); homology for PSEPK | High | 19965770, 23594205 |
| Catalyzes 2nd half-reaction: carboxybiotin + acetyl-CoA → malonyl-CoA | Enzyme kinetics, mechanism | High | 23594205, 29100983 |
| Substrate = acetyl-CoA; product = malonyl-CoA | Biochemistry | High | 29100983, 16460018 |
| First committed / rate-limiting step of FAS | Biochemistry, review | High | 29100983, 39572150 |
| Bacteria-specific Cys₄ Zn domain on β-subunit, needed for catalysis | X-ray crystallography + mutagenesis | High | 16460018, 19965770 |
| Cytoplasmic, soluble multi-subunit complex | Biochemistry / pull-downs | High | 23594205 |
| Feedback inhibition by acyl-ACP | Kinetics | High | 29100983 |
| accA/accD unlinked from accBC in Pseudomonas | Cloning/hybridization (*P. aeruginosa*) | Medium–High (relative) | 7693652 |
| CT mRNA-binding autoregulation ("dimmer switch") | In vitro (proposed) vs in vivo (refuted) | Contested | 19965770 (for) / 25157077 (against) |
| PSEPK-specific functional assignment | Homology / HAMAP MF_01395 | Inferred (by similarity) | UniProt Q88LD9 |

---

## 8. Supported and Refuted Hypotheses

**Supported**
- AccD is the β-subunit of the carboxyltransferase that produces malonyl-CoA (2nd half-reaction of ACC). ✔
- The enzyme is cytoplasmic and functions within an assembled multi-subunit ACC complex. ✔
- AccD bears a bacteria-specific Cys₄ zinc domain required for catalysis, marking it as a selective drug target. ✔
- The reaction is the committed, feedback-regulated (acyl-ACP) entry step of fatty-acid/phospholipid biosynthesis. ✔

**Refuted / Contested**
- CT (AccA/AccD) acts as a physiologically significant translational repressor of its own mRNAs — **not supported in vivo** [PMID 25157077], despite an in-vitro "dimmer switch" proposal [PMID 19965770]. AccD's principal role is enzymatic; any nucleic-acid-binding/moonlighting function is unresolved and likely minor.

---

## 9. Limitations and Future Directions

- **No primary study on PP_1996 itself.** The functional assignment for *P. putida* KT2440 rests on strong homology (HAMAP MF_01395) and mechanism established in *E. coli*, *S. aureus*, and *Haemophilus*. Direct biochemical/structural confirmation of the KT2440 protein is lacking.
- **Structural specifics of the *Pseudomonas* CT** (e.g., a species structure, exact Zn-domain geometry) have not been reported; a *P. putida* CT crystal/cryo-EM structure would confirm domain conservation.
- **Regulatory role of the AccD zinc domain in RNA binding** remains contested and merits definitive in vivo testing in Pseudomonads.
- **Subunit stoichiometry coordination** from dispersed *acc* loci in *Pseudomonas* is mechanistically unresolved.

---

### Key References (PMID)
- 16460018 — Bilder et al. (2006) *Biochemistry*. Structure of bacterial CT reveals the unique zinc-binding motif.
- 19965770 — Meades et al. (2010) *Nucleic Acids Res.* CT enzymatic activity + proposed translational repression via β-subunit zinc finger.
- 25157077 — Smith & Cronan (2014) *J. Bacteriol.* In vivo evidence against CT translational repression.
- 23594205 — Broussard et al. (2013) *Biochemistry.* Complex formation and interacting active sites of *E. coli* ACC.
- 23499019 — Broussard et al. (2013) *Structure.* BC–BCCP complex structure.
- 29100983 — Evans et al. (2017) *Biochim. Biophys. Acta.* Hysteretic acyl-ACP feedback inhibition of ACC.
- 18156466 — Benson et al. (2008) *Biochemistry.* DNA inhibits CT; active-site communication.
- 26020841 — Broussard et al. (2015) *Biochemistry.* Biotin carboxylase mechanism/structures.
- 7693652 — Best & Knauf (1993) *J. Bacteriol.* Genetic organization of *P. aeruginosa* ACC (accBC operon; accA/accD dispersed).
- 19362649 — Cronan & Thomas (2009) *Methods Enzymol.* Bacterial fatty-acid synthesis (review).
- 8246839 — Magnuson et al. (1993) *Microbiol. Rev.* Regulation of *E. coli* fatty-acid biosynthesis (review).
- 39572150 — Čavužić et al. (2024). Methodology of ACC inhibition (review).


## Artifacts

- [OpenScientist final report](accD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](accD-deep-research-openscientist_artifacts/final_report.pdf)