---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:47:21.771639'
end_time: '2026-10-24T14:10:47.853736'
duration_seconds: 1406.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL8B
  gene_symbol: RTL8B
  uniprot_accession: Q17RB0
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 8B {ECO:0000312|HGNC:HGNC:33156};
    AltName: Full=Mammalian retrotransposon derived protein 8B;'
  gene_info: Name=RTL8B; Synonyms=CXX1C, FAM127C, MAR8B;
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
  path: RTL8B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL8B-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q17RB0
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 8B {ECO:0000312|HGNC:HGNC:33156}; AltName: Full=Mammalian retrotransposon derived protein 8B;
- **Gene Information:** Name=RTL8B; Synonyms=CXX1C, FAM127C, MAR8B;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the FAM127 family. .
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL8B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL8B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL8B** (gene ID: RTL8B, UniProt: Q17RB0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: RTL8B (Retrotransposon Gag-like protein 8B)

**Gene:** RTL8B (synonyms: CXX1C, FAM127C, MAR8B / MART8B)
**UniProt:** Q17RB0 · **Organism:** *Homo sapiens* · **Locus:** X chromosome (Xq23)
**Family:** FAM127 / Mart / SIRH (Sushi-ichi-related retrotransposon homolog) family
**Domain:** RTL1/LDOC capsid-like (InterPro IPR032549; Pfam PF16297)
**Date:** 2026-10-24

---

## 1. Summary (Answer to the Research Question)

RTL8B is a small (~113 aa, ~13 kDa) **domesticated retrotransposon Gag/capsid-derived protein**. It is not an enzyme, transporter, or classical signaling molecule; rather it is a **capsid-homology adaptor/modulator** consisting essentially of a single N-terminal Gag "capsid-like" domain. Its established primary function is **protein–protein interaction with two other retroelement-derived human proteins — the Gag-like protein PEG10 (RTL2) and the ubiquitin-proteasome shuttle factor UBQLN2 — to control their subcellular localization and activity**. Specifically, RTL8(B):

1. **binds the N-terminal capsid domain of PEG10** and acts as a **dominant-negative "capsid poison,"** reducing assembly/release of PEG10 virus-like particles (VLPs) and retaining PEG10 intracellularly;
2. **promotes nuclear/nucleolar translocation of UBQLN2** into ubiquitin-rich sub-nuclear protein-quality-control (PQC) compartments; and
3. is the **obligatory bridging factor** that enables PEG10 to recruit UBQLN2 into cytoplasmic **stress granules**, thereby shaping stress-granule dynamics and proteostasis.

Thus RTL8B operates at the **intersection of endogenous retroelement capsid biology and cellular protein quality control**, acting in both the **nucleolus/nucleus** and the **cytoplasm (stress granules)**.

> **Identity caveat (addressed):** "RTL8B" (Q17RB0) is unambiguously the human FAM127/Mart Gag-like gene described below. The published functional literature refers to the protein collectively as **"RTL8"** because humans carry three X-linked paralogs — RTL8A, RTL8B, RTL8C — encoding **near-identical** proteins. Sequence comparison performed in this analysis shows RTL8B is **96.5% identical (109/113 residues)** to RTL8A (Q9BWD3) and nearly identical to RTL8C (A6ZKI3). The paralogs cannot be distinguished by the antibodies or knockdown/overexpression reagents used in the primary studies, so the functional conclusions apply to RTL8B.

---

## 2. Molecular Identity and Structure

- **Protein:** 113 residues, ~13 kDa; sequence (Q17RB0):
  `MEGRVQLMKALLARPLRPAARRWRNPIPFPETFDGDTDRLPEFIVQTSSYMFVDENTFSNDALKVTFLITRLTGPALQWVIPYIKKESPLLSDYRGFLAEMKRVFGWEEDEDF`
- **Domain architecture:** a single **RTL1/LDOC capsid-like domain** (PF16297) spanning essentially the whole protein. It corresponds to the **N-terminal Gag capsid (CA) region of a Sushi-ichi/LTR retrotransposon**, and resembles a **truncated PEG10** that retains only the capsid-homology portion — it **lacks any Pol/protease, reverse-transcriptase, or nucleocapsid (zinc-knuckle) region** (Campodonico et al. 2024, PMID 39775359).
- **Paralog set (this analysis):** RTL8B vs RTL8A = 96.5% identity; RTL8C near-identical. All three are small single-exon-like Gag capsid genes clustered on the X chromosome.
- **Family placement:** member of the **SIRH/Mart/RTL family** of genes domesticated from LTR retrotransposons in mammals; related members include PEG10 (SIRH1/RTL2), RTL1/PEG11 (SIRH2), and LDOC1 (RTL7/SIRH7) (Kaneko-Ishino & Ishino 2012, PMID 22866050).

**Functional inference from structure/evolution:** Possessing only a capsid-homology domain and no catalytic module, RTL8B is predicted to act through **homotypic/heterotypic capsid–capsid interactions** rather than catalysis — consistent with all experimental data showing it works by binding and modulating partner proteins.

**Bioinformatic corroboration (this analysis):** A BLOSUM62 Smith-Waterman alignment of RTL8B against PEG10 shows RTL8B residues **26–105 align to PEG10 residues ~79–158** at **35% identity / 54% similarity** (80-aa window), with conserved capsid motifs (…PE·FDG…, and a C-terminal …**MK·VF** block: RTL8B `AEMKRVF` vs PEG10 `MMEMKHVF`). The alignment covers ~70% of RTL8B — i.e. essentially the **entire protein is one copy of PEG10's N-terminal Gag capsid domain** — and the homologous stretch **coincides with the experimentally-mapped RTL8-binding region of PEG10 capsid** (PMID 39775359). This independently supports a capsid–capsid heterodimerization mechanism.

---

## 3. Primary Function and Mechanism

### 3.1 Antagonist of PEG10 capsid / virus-like-particle assembly
PEG10 is a Gag-Pol–like, retroelement-derived protein that **self-assembles into virus-like particles (VLPs)** which package mRNA and are secreted in extracellular vesicles (Segel et al. 2021, PMID 34413232). RTL8 shares homology with the PEG10 **N-terminal capsid domain** and binds there. On its own RTL8 **cannot form VLPs**, but it is **incorporated into PEG10 particles**; when co-expressed, RTL8 **decreases PEG10 VLP abundance and raises intracellular PEG10**, i.e., it **inhibits PEG10 VLP formation/release** (Campodonico et al. 2024, PMID 39775359).

> **Mechanistic model:** RTL8B behaves like a **capsid "chain terminator"/dominant-negative subunit** — it co-assembles with PEG10 capsid via the shared Gag interface but, lacking the full assembly determinants, caps or poisons higher-order particle formation, thereby limiting VLP output and retaining PEG10 in the cell.

### 3.2 Adaptor controlling UBQLN2 localization (nuclear PQC)
RTL8 was discovered as a **UBQLN2 interactor** by mass spectrometry and validated with recombinant proteins and in mouse brain (Mohan et al. 2022, PMID 35247097). Endogenous and overexpressed **RTL8 localizes to nucleoli**; co-expressed RTL8 **promotes nuclear translocation of UBQLN2**, including under heat-shock stress, and the two **colocalize in ubiquitin-enriched sub-nuclear structures containing protein-quality-control components**. The effect is **selective for UBQLN2** (not UBQLN1 or UBQLN4), and UBQLN2 reciprocally stabilizes RTL8 protein levels.

### 3.3 Obligatory bridge in the UBQLN2–PEG10 stress-granule axis
RTL8 **"confers on UBQLN2 the ability to complex with and regulate PEG10."** PEG10 is a core stress-granule component and recruits UBQLN2 to stress granules under stress, **but only when RTL8 is present**. Perturbing RTL8 (or UBQLN2/PEG10) levels **remodels stress-granule disassembly kinetics and translation recovery**; within stress granules PEG10 forms VLPs (Mohan et al. 2025, PMID 40680123; preprint PMID 39484508).

**Synthesis of mechanism:** RTL8B is a **molecular linchpin** that uses its single capsid interface to simultaneously engage PEG10 (another capsid protein) and the UBQLN2 proteostasis shuttle, thereby (i) tuning PEG10 capsid/VLP assembly and (ii) routing UBQLN2 between cytoplasmic stress granules and nuclear/nucleolar PQC compartments.

---

## 4. Subcellular Localization

| Compartment | Evidence |
|---|---|
| **Nucleolus** (steady state) | RTL8 localizes to nucleoli under endogenous and overexpressed conditions (PMID 35247097); rationalized by an N-terminal arginine-rich NoLS-like motif (see below) |
| **Nucleus / sub-nuclear PQC foci** | RTL8 + UBQLN2 colocalize in ubiquitin-enriched sub-nuclear structures (PMID 35247097) |
| **Cytoplasm / stress granules** | RTL8 required for PEG10-mediated UBQLN2 recruitment to stress granules (PMID 40680123) |
| **Incorporated into PEG10 VLPs** | RTL8 packaged into PEG10-derived particles (PMID 39775359) |

RTL8B therefore acts in **multiple compartments**, shuttling/partitioning between the nucleolus/nucleus and cytoplasmic condensates depending on its partners and cellular stress state.

**Sequence rationale for nucleolar targeting (this analysis):** RTL8B's N-terminus is strongly basic — **6 arginines in the first 25 residues**, with a maximal positive-charge window at residues ~13–26 (`RPLRPAARRWRN`, net +4), conserved across RTL8A/B/C and lying just upstream of the capsid-homology region. This architecture matches a canonical **arginine-rich nucleolar-localization signal (NoLS)/nucleic-acid-binding motif**, providing a mechanistic explanation for RTL8B's steady-state nucleolar localization. Notably, the PEG10 N-terminus lacks a comparable arginine cluster, consistent with PEG10 not being intrinsically nucleolar. (Bioinformatic inference; not yet confirmed by mutagenesis.)

---

## 5. Pathways and Biological Context

- **Endogenous retroelement capsid pathway:** regulator of PEG10 VLP biogenesis (PMID 39775359, 34413232).
- **Protein quality control / ubiquitin-proteasome system (proteostasis):** governs localization of the UBQLN2 shuttle factor and the kinetics of stress-granule assembly/disassembly (PMID 35247097, 40680123).
- **Tissue/expression context:** RTL8 is broadly expressed and co-expressed with PEG10 in many tissues including **human brain** (PMID 39775359). Because UBQLN2 and PEG10 are implicated in **ALS/FTD and other neurodegenerative disease**, RTL8B's control of their localization and assembly is of likely neurobiological relevance.
- **Evolutionary pathway:** domesticated from a **Sushi-ichi/LTR retrotransposon Gag** during mammalian evolution; part of the SIRH/Mart family whose founding members (PEG10, RTL1) are essential for placentation, situating RTL8 within a retroelement-derived regulatory network (PMID 22866050).

---

## 6. Supported and Refuted Hypotheses

**Supported (experimental evidence):**
- H1 — RTL8B is a capsid-homology adaptor, not an enzyme. ✔ (domain structure; truncated-Gag homology, PMID 39775359)
- H2 — RTL8 directs UBQLN2 to the nucleus/nucleolus and PQC foci. ✔ (PMID 35247097)
- H3 — RTL8 binds PEG10 capsid and antagonizes VLP formation. ✔ (PMID 39775359)
- H4 — RTL8 is required to bridge PEG10 and UBQLN2 at stress granules. ✔ (PMID 40680123)

**Refuted / unsupported:**
- RTL8B is NOT an active retrotransposon, reverse transcriptase, or protease — it retains no Pol/catalytic domain.
- RTL8B does NOT act on UBQLN1 or UBQLN4 — the effect is UBQLN2-selective (PMID 35247097).

---

## 7. Limitations and Future Directions

- **Paralog resolution:** reagents do not distinguish RTL8A/B/C; the specific, non-redundant contribution of **RTL8B** versus its paralogs has not been isolated. Paralog-specific CRISPR/degron studies are needed. This near-identity (~96–97%) also defeats high-throughput resources: in this analysis **GTEx v8 returned no median expression** for RTL8B/A/C and the **AlphaFold DB has no deposited model for Q17RB0** (HTTP 404) — multi-mapping reads and redundant sequences prevent unique assignment. Expression context therefore rests on the primary-literature statement that RTL8 is broadly expressed, including in human brain (PMID 39775359).
- **In-vivo physiology:** no dedicated RTL8B knockout phenotype is reported; organismal function is inferred from in-vitro/cell and mouse-brain interaction data.
- **Structure:** no experimental 3D structure of RTL8B–PEG10 or RTL8B–UBQLN2 complexes; the predicted capsid fold and binding interface merit structural confirmation (cryo-EM/AlphaFold-Multimer).
- **Directionality:** whether RTL8B's nucleolar role and its cytoplasmic stress-granule role are competing or sequential activities remains open.

---

## 8. Key References
- Mohan et al. 2022, *J Biol Chem/Hum Mol Genet* — RTL8 promotes nuclear localization of UBQLN2 (PMID 35247097).
- Campodonico et al. 2024, *(Whiteley/Sharkey labs)* — RTL8 antagonizes PEG10 VLPs (PMID 39775359).
- Mohan et al. 2025 — Retrovirus-like proteins recruit UBQLN2 to stress granules (PMID 40680123; preprint 39484508).
- Segel et al. 2021, *Science* — PEG10 packages its own mRNA / VLPs (PMID 34413232).
- Kaneko-Ishino & Ishino 2012 — Domesticated LTR-retrotransposon genes in mammals (PMID 22866050).


## Artifacts

- [OpenScientist final report](RTL8B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL8B-deep-research-openscientist_artifacts/final_report.pdf)