---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:44:43.715052'
end_time: '2026-10-24T13:56:25.714764'
duration_seconds: 702.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL8A
  gene_symbol: RTL8A
  uniprot_accession: Q9BWD3
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 8A {ECO:0000312|HGNC:HGNC:24514};
    AltName: Full=Mammalian retrotransposon derived protein 8A;'
  gene_info: Name=RTL8A {ECO:0000312|HGNC:HGNC:24514}; Synonyms=CXX1B, FAM127B {ECO:0000305},
    MAR8A;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the FAM127 family. .
  protein_domains: RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)
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
  path: RTL8A-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL8A-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q9BWD3
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 8A {ECO:0000312|HGNC:HGNC:24514}; AltName: Full=Mammalian retrotransposon derived protein 8A;
- **Gene Information:** Name=RTL8A {ECO:0000312|HGNC:HGNC:24514}; Synonyms=CXX1B, FAM127B {ECO:0000305}, MAR8A;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the FAM127 family. .
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL8A" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL8A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL8A** (gene ID: RTL8A, UniProt: Q9BWD3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RTL8A (Q9BWD3) — Functional Annotation Report

**Gene:** RTL8A (synonyms: CXX1B, FAM127B, MAR8A, Mart8A)
**Protein:** Retrotransposon Gag-like protein 8A
**UniProt:** Q9BWD3 · **HGNC:** 24514 · **Organism:** *Homo sapiens*
**Family:** RTL/SIRH (Mart) family of domesticated retroelement genes; FAM127 family
**Domain:** RTL1/1-8/LDOC capsid-like (InterPro IPR032549; Pfam PF16297)

---

## 1. Summary (Answer to the Research Question)

RTL8A is **not an enzyme, transporter, or classical signaling molecule**. It is a small
(113-residue, ~13 kDa) protein corresponding to a **single, truncated retroviral/retrotransposon
Gag "capsid" (CA) domain** that has been domesticated from a *Ty3/gypsy* sushi-ichi-related LTR
retrotransposon in the eutherian lineage. Functionally it behaves as a **capsid-derived
protein–protein interaction / adaptor module**. Its two best-documented molecular roles are:

1. **Regulation of the ubiquitin–proteasome shuttle factor UBQLN2** — RTL8 binds UBQLN2 and drives
   its translocation into the nucleus/nucleolus to ubiquitin-rich protein-quality-control (PQC)
   compartments; UBQLN2 reciprocally stabilizes RTL8 (PMID 35247097).
2. **Antagonistic regulation of the related capsid protein PEG10** — RTL8 hetero-oligomerizes with
   the PEG10 N-terminal capsid domain, is packaged into PEG10 virus-like particles (VLPs), and
   **inhibits PEG10 VLP formation/release** while raising intracellular PEG10; it is also the
   obligatory bridge that lets UBQLN2 complex with PEG10 and be recruited into cytoplasmic stress
   granules under stress (PMID 39775359; PMID 40680123).

Thus RTL8A acts at the interface of **endogenous retroelement (PEG10) capsid biology** and
**cellular proteostasis (UBQLN2 / ubiquitin–proteasome system / stress granules)**, operating in
both the **nucleolus/nucleus** and **cytoplasmic stress granules**.

**Identity verification:** The gene symbol, organism (human), FAM127/RTL family membership, and the
PF16297 capsid-like domain are all internally consistent with the primary literature. This is a
genuine, correctly identified human protein — **not** a case of symbol ambiguity. The only caveat is
that RTL8A is one of three near-identical paralogs (see §6), so published functional work refers to
"RTL8" collectively rather than resolving RTL8A individually.

---

## 2. Molecular Identity and Origin

RTL8A belongs to the **RTL (Retrotransposon Gag-Like) / SIRH (Sushi-Ichi Retrotransposon Homolog)
family**, also called the **Mart genes**. Eutherian mammals possess **11 RTL/SIRH genes "presumably
derived from a certain retrovirus"**, which were co-opted ("domesticated") and now function in the
placenta, brain, and innate immune system in a eutherian-specific manner (Kaneko-Ishino & Ishino,
PMID 37892118). These genes derive from a *Ty3/gypsy* LTR-retroelement with homology to the
pufferfish *sushi-ichi* retrotransposon (Henke et al., PMID 25888968).

Within this family, RTL8A corresponds to **Mart8 / CXX1**. Full-length family members such as PEG10
(Mart2) and RTL1 (Mart1) retain a multidomain Gag(-Pol)-like organization and can form **virus-like
particles** and bind nucleic acids (Segel et al., Science 2021, PMID 34413232). **RTL8 is a
"truncated form of PEG10 that shares homology with the N-terminal gag-like capsid domain"**
(Campodonico et al., PMID 39775359) — i.e., it retains essentially only the capsid (CA) module.

---

## 3. Structure (Experimental Inference)

UniProt Q9BWD3 is a single 113-residue chain whose annotation is limited to the chain feature and a
single natural variant (rs2498776 at position 48); it carries no catalytic-motif annotation,
consistent with a non-enzymatic protein.

Bioinformatic/structural analysis performed in this study:

- **AlphaFold model (Q9BWD3):** mean pLDDT = **88.0**, with a **very-high-confidence folded core at
  residues ~21–100** (per-20-residue mean pLDDT 90–98) flanked by a lower-confidence, likely flexible
  **N-terminus (res 1–20, pLDDT 64.6)** and **C-terminus (res 101–113, pLDDT 77.1)**. This is
  consistent with a single compact capsid-like (CA) fold plus disordered tails.
- **Homology scan vs PEG10 (Q86TG7):** a crude ungapped comparison yields ~27% identity aligning to
  the PEG10 capsid region, independently supporting that the RTL8A fold is a **diverged retroviral
  Gag capsid (CA) domain** (consistent with PMID 39775359).

RTL8A **lacks** the CCHC zinc-knuckle/nucleocapsid, the aspartyl-protease (DSG) motif, and the
reverse-transcriptase/integrase regions found in full retroelements. Mechanistically, the folded
CA-like core provides the **oligomerization/interaction surface** that mediates incorporation into
PEG10 capsids and binding to UBQLN proteins, while the flexible termini likely mediate additional
partner contacts.

---

## 4. Primary Molecular Function

### 4.1 A capsid-derived protein-interaction / adaptor module (not an enzyme)
RTL8A has no catalytic activity. Its function is structural/regulatory: it uses a retroviral
capsid-like domain as an interaction surface. Curated interaction data (UniProt/IntAct) list binding
partners **PEG10 (isoform 2), UBQLN2, UBQLN1, and CCDC102B**, matching the interactions characterized
experimentally below.

### 4.2 Regulation of UBQLN2 subcellular localization and proteostasis
In an unbiased mass-spectrometry screen for UBQLN2 interactors, RTL8 was identified, and the
**UBQLN2–RTL8 interaction was confirmed both in vitro (recombinant proteins) and in vivo (mouse brain
tissue)** (Mohan et al., *J Biol Chem* 2022, PMID 35247097). Key experimental findings:

- RTL8 **localizes to nucleoli** under endogenous and overexpressed conditions.
- Co-expression of RTL8 **promotes nuclear translocation of UBQLN2**, including under heat-shock
  stress, and the two colocalize in **ubiquitin-enriched subnuclear structures containing PQC
  components**.
- The effect is **specific to UBQLN2** and does not extend to the paralogous brain ubiquilins
  UBQLN1 and UBQLN4.
- **UBQLN2 reciprocally stabilizes RTL8 protein levels** in human cell lines and mouse brain.

Because UBQLN2 is a ubiquitin–proteasome shuttle factor central to protein quality control (and
mutated in ALS/FTD), RTL8A functions as a **spatial regulator of the UBQLN2 branch of the
ubiquitin–proteasome system**, directing UBQLN2 to nuclear/nucleolar PQC sites where it can clear
aberrant nuclear proteins.

### 4.3 Antagonism of PEG10 capsid / virus-like-particle biology
PEG10 forms virus-like particles (VLPs) implicated in its roles in placentation and neurological
disease. Campodonico et al. (PMID 39775359) showed:

- RTL8 **alone cannot form VLPs** but is **incorporated into PEG10-derived particles**.
- RTL8 **binds the N-terminal capsid domain of PEG10**.
- RTL8 co-expression **decreases PEG10 VLP abundance and increases intracellular PEG10**, and
  modulating RTL8 changes VLP output in cells that naturally produce them — i.e., RTL8 **inhibits
  PEG10 VLP formation/release**.

This defines a **novel antagonistic relationship between two domesticated retroelement genes**, with
RTL8A acting as a "poison-subunit"–like capsid partner that caps or disrupts productive PEG10 capsid
assembly/egress.

### 4.4 Bridging PEG10 and UBQLN2 at stress granules
Mohan et al. (2024 preprint PMID 39484508; 2025 PMID 40680123) integrated these two activities:
**"RTL8 confers on UBQLN2 the ability to complex with and regulate PEG10,"** and PEG10 — a core
stress-granule component that forms VLPs within granules — **can recruit UBQLN2 into stress granules
only when RTL8 is present**. Changing UBQLN2, RTL8, or PEG10 levels **remodels stress-granule
disassembly kinetics and translation recovery**. RTL8A is therefore an obligatory adaptor coupling
PEG10 capsid condensates to the UBQLN2 proteostasis machinery.

---

## 5. Localization (Where It Acts)

- **Nucleolus / nucleus:** endogenous and overexpressed RTL8 localizes to **nucleoli**; with UBQLN2
  it concentrates in **ubiquitin-rich subnuclear PQC bodies** (PMID 35247097). This is the site of
  its UBQLN2-directing function.
- **Cytoplasmic stress granules:** under stress, RTL8 is found with PEG10 and UBQLN2 in stress
  granules, where PEG10 forms VLPs (PMID 40680123).
- **Site of PEG10 antagonism:** RTL8 is incorporated into cytoplasmic PEG10 capsid particles and
  influences their intracellular abundance and release (PMID 39775359).

RTL8 is **broadly expressed in many of the same tissues as PEG10, including human brain** (PMID
39775359).

---

## 6. Paralog Caveat (Important for Interpretation)

The human genome encodes **three near-identical RTL8 paralogs — RTL8A/B/C (= CXX1B/A/C = Mart8A/B/C)**
— on the X chromosome, all producing ~13 kDa proteins of nearly indistinguishable sequence; the mouse
orthologs are *Cxx1a,b,c / Mart8b,c,a* (PMID 25888968). Because the proteins are essentially
identical, the antibody-, overexpression-, and mass-spectrometry-based functional studies above
characterize **"RTL8" as a group** and do not resolve a function unique to RTL8A. RTL8A should
therefore be understood as sharing the functions documented for the RTL8 trio.

---

## 7. Pathway Context

RTL8A sits at the intersection of two pathways:

- **Proteostasis / ubiquitin–proteasome system:** via UBQLN2, routing PQC activity to nuclear/nucleolar
  compartments and modulating UBQLN2 availability at stress granules — relevant to ALS/FTD, where
  UBQLN2 is a disease gene (PMID 35247097; PMID 40680123).
- **Endogenous retroelement capsid pathway:** via PEG10, as a negative regulator of PEG10 VLP
  formation/release (PMID 39775359). PEG10 itself is implicated in placentation, ALS, and Angelman
  syndrome, so RTL8A is positioned as a cell-intrinsic modulator of PEG10-driven biology.

---

## 8. Supported vs. Refuted Hypotheses

**Supported (by direct experimental evidence):**
- RTL8 physically binds UBQLN2 (in vitro + mouse brain) and drives its nuclear/nucleolar
  translocation to PQC sites (PMID 35247097).
- RTL8 binds the PEG10 capsid domain, is packaged into PEG10 VLPs, and inhibits VLP
  formation/release (PMID 39775359).
- RTL8 is required for PEG10-dependent recruitment of UBQLN2 to stress granules (PMID 40680123).

**Supported (by structural/evolutionary inference):**
- RTL8A is a domesticated, capsid-only retroelement Gag fragment (AlphaFold + homology; PMID 37892118,
  25888968, 39775359).

**Refuted / not supported:**
- RTL8A is an enzyme, transporter, or nucleic-acid-packaging protein — no evidence; it lacks the
  catalytic and nucleocapsid modules of full retroelements.

---

## 9. Limitations and Future Directions

- Functional data derive largely from **overexpression and interaction studies**; endogenous
  loss-of-function (knockout/knockdown) phenotypes specific to RTL8A are not established.
- **Paralog resolution** (RTL8A vs B vs C) is unaddressed experimentally.
- No **experimental 3D structure** exists; the capsid-like fold is predicted (AlphaFold) and inferred
  from PEG10 homology.
- The physiological consequences in brain/placenta and the disease relevance (ALS/FTD via UBQLN2;
  PEG10-linked disorders) remain to be defined in vivo.

---

## Key References
- Mohan et al., *J Biol Chem* 2022 — RTL8 promotes nuclear/nucleolar localization of UBQLN2 (PMID 35247097).
- Campodonico et al., 2024 — RTL8 antagonizes PEG10 virus-like particles (PMID 39775359).
- Mohan et al., 2024/2025 — RTL8/PEG10 recruit UBQLN2 to stress granules (PMID 39484508; PMID 40680123).
- Kaneko-Ishino & Ishino, 2023 — RTL/SIRH family review (PMID 37892118).
- Henke et al., 2015 — Mart/SIRH genes in placentogenesis; CXX1/Mart8 nomenclature (PMID 25888968).
- Segel et al., *Science* 2021 — PEG10 VLPs and mRNA packaging (PMID 34413232).


## Artifacts

- [OpenScientist final report](RTL8A-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL8A-deep-research-openscientist_artifacts/final_report.pdf)