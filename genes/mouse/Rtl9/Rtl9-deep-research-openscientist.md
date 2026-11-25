---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:46:23.794367'
end_time: '2026-10-24T16:08:14.459617'
duration_seconds: 1310.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl9
  gene_symbol: Rtl9
  uniprot_accession: Q32KG4
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 9 {ECO:0000250|UniProtKB:Q8NET4};
    AltName: Full=Retrotransposon gag domain-containing protein 1 {ECO:0000312|MGI:MGI:2685231};
    AltName: Full=Sushi-XF2 {ECO:0000305};'
  gene_info: Name=Rtl9 {ECO:0000250|UniProtKB:Q8NET4}; Synonyms=Gm385, Kiaa1318, Rgag1
    {ECO:0000312|MGI:MGI:2685231};
  organism_full: Mus musculus (Mouse).
  protein_family: Not specified in UniProt
  protein_domains: PEG10-RTL1_C-capsid. (IPR063300); RTL9. (IPR042919); PEG10-RTL1_C-capsid
    (PF30901)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rtl9-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl9-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q32KG4
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 9 {ECO:0000250|UniProtKB:Q8NET4}; AltName: Full=Retrotransposon gag domain-containing protein 1 {ECO:0000312|MGI:MGI:2685231}; AltName: Full=Sushi-XF2 {ECO:0000305};
- **Gene Information:** Name=Rtl9 {ECO:0000250|UniProtKB:Q8NET4}; Synonyms=Gm385, Kiaa1318, Rgag1 {ECO:0000312|MGI:MGI:2685231};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PEG10-RTL1_C-capsid. (IPR063300); RTL9. (IPR042919); PEG10-RTL1_C-capsid (PF30901)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl9" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl9' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl9** (gene ID: Rtl9, UniProt: Q32KG4) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Rtl9 (Q32KG4) — Functional Annotation Report

**Gene:** *Rtl9* (Retrotransposon Gag-like 9) — synonyms *Gm385*, *Kiaa1318*, *Rgag1*, *SIRH10*
**UniProt:** Q32KG4 · **Organism:** *Mus musculus* (mouse) · **Chromosome:** X
**Protein:** Retrotransposon Gag-like protein 9 (AltName: Retrotransposon gag domain-containing protein 1; "Sushi-XF2"), 1339 aa (~138 kDa)

---

## Summary

Mouse **Rtl9** (also called **SIRH10** or **Rgag1**; UniProt **Q32KG4**) is a **domesticated, retrovirus-derived gene** whose primary, experimentally established function is **innate antifungal immunity in the brain**. The protein is expressed in **microglia**, the resident immune cells of the central nervous system, and localizes specifically to **microglial lysosomes**, where it is required for the **degradation of internalized fungal material** — demonstrated directly using the fungal cell-wall preparation **zymosan** ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)). This makes Rtl9 a bona fide effector component of the brain's innate immune system rather than a transporter, classical enzyme, or signaling ligand.

Mechanistically, the antifungal activity depends on the protein's **C-terminal retroviral Gag/capsid-like domain** (PEG10/RTL1 C-capsid; Pfam **PF30901**, InterPro **IPR063300**), which maps to approximately **residues 1219–1285** of the 1339-residue protein. A knock-in truncation that removes this region (**RTL9ΔC**) **abolishes zymosan-degrading activity**, providing loss-of-function evidence that the ancestral viral capsid module is the functional business end of the protein ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)).

Rtl9 is the fungal-responding member of a **eutherian-specific, microglial RTL "trio"**: **RTL9 (fungi)**, **RTL5/SIRH8 (viruses / double-stranded RNA)**, and **RTL6/SIRH3 (bacteria / lipopolysaccharide)**. These three genes belong to the family of **11 RTL/SIRH genes** that mammals captured and domesticated from an ancient sushi-ichi retrotransposon (a metavirus/retrovirus-like element) ([PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/); [PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)). No alternative molecular function (e.g., enzymatic catalysis, nucleic-acid transport, or a role as a transcription factor) is documented for mouse Rtl9 or its human ortholog *RGAG1*; the microglial antifungal role is the single characterized function in the literature.

---

## Gene / Protein Identity Verification

As required before reporting, the target identity was verified:

- **Symbol match:** "Rtl9" matches the UniProt protein description "Retrotransposon Gag-like protein 9"; the alias **SIRH10** and synonym **Rgag1** are consistent with the Q32KG4 record — ✓ consistent.
- **Organism:** All functional data (Ishino et al. 2023) are in *Mus musculus* — ✓ correct organism.
- **Domain alignment:** The literature's "retroviral GAG-like region" corresponds to the UniProt/Pfam PEG10-RTL1_C-capsid domain (PF30901) — ✓ consistent.
- **Ambiguity check:** The synonym *Rgag1* could superficially be confused with other "gag domain" genes, but the X-linked locus, the SIRH10 designation, the capsid domain, and the human ortholog *RGAG1* (Xq13) all converge on the same gene. No conflicting literature for a differently-identified gene under the same symbol was used.

The gene is correctly identified; the report proceeds on **Rtl9 / SIRH10 / Q32KG4** in mouse. The functional literature is **limited but unambiguous and directly on-target** — almost entirely from the Ishino/Kaneko-Ishino group who performed the defining mouse genetic experiments.

---

## Key Findings

### Finding 1 — Rtl9 mediates innate antifungal immunity in the eutherian brain

The defining functional study for this gene is **Ishino et al. 2023** (*Retrovirus-Derived RTL9 Plays an Important Role in Innate Antifungal Immunity in the Eutherian Brain*, *Int. J. Mol. Sci.*, [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)). Using **RTL9-mCherry knock-in reporter mice**, the authors showed that RTL9 protein is expressed in **brain microglia**. Functionally, they demonstrated that RTL9 **degrades fungal zymosan** — a β-glucan/mannan-rich preparation of the yeast cell wall that is a standard surrogate for fungal pathogen-associated molecular patterns (PAMPs). In the authors' words: *"Here, we demonstrate that RTL9 plays an important role, degrading zymosan in the brain."*

This finding establishes the **primary biological process** for Rtl9: it is an **effector of innate immunity directed against fungal cell-wall material**, operating in the central nervous system. Its documented role is specific and immunological rather than broadly developmental.

### Finding 2 — The C-terminal retroviral Gag-like domain is essential for activity

The same study provides decisive **loss-of-function evidence** pinpointing the functional module. In **Rtl9 knockout mice re-expressing a truncated RTL9ΔC protein** — a variant lacking the **C-terminal retroviral GAG-like region** — the **zymosan-degrading activity was lost**: *"in Rtl9 knockout mice expressing RTL9ΔC protein lacking the C-terminus retroviral GAG-like region, the zymosan degrading activity was lost"* ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)).

This is the strongest mechanistic statement available for the gene: the **ancestral viral capsid/Gag domain**, not the large non-viral N-terminal region, carries the activity required to digest fungal material. It directly links the protein's **evolutionary origin** (a captured retroviral Gag) to its **present-day host function** (antifungal defense).

### Finding 3 — Rtl9 localizes to microglial lysosomes, the site of fungal digestion

Subcellular localization was resolved using **RTL9-mCherry fusion knock-in mice** challenged with fungal zymosan. The RTL9 protein was found **within microglial lysosomes**, co-localized with the compartment in which **internalized zymosan is digested**: *"The RTL9 protein is localized in the microglial lysosomes where incorporated zymosan is digested."* ([PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)).

This establishes **where the gene product carries out its function**: it acts **intracellularly, in the lysosomal/phagolysosomal compartment of microglia**, consistent with a role in the degradative arm of phagocytic clearance of fungal particles. This is notably distinct from its sibling proteins RTL5 and RTL6, which appear as **extracellular dots and granules** in the CNS ([PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)) — implying a division of labor across compartments within the same microglial defense system.

### Finding 4 — Rtl9 belongs to the eutherian-specific SIRH/RTL family of domesticated sushi-ichi retrotransposon genes

Rtl9 is one of **11 RTL/SIRH (Retrotransposon Gag-Like / Sushi-ichi Retrotransposon Homolog) genes** that eutherian mammals derived from an ancient sushi-ichi retrotransposon (a metavirus) ([PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)). Within this family, **RTL9 = SIRH10**. Reviews of the family establish that these genes were "domesticated" (co-opted) and now serve host functions in the **placenta, brain, and innate immune system** in a eutherian-specific manner.

Critically, three family members function together inside microglia as an innate-immune module: *"SIRH3/RTL6, SIRH8/RTL5, and SIRH10/RTL9 mediate innate immune responses against bacterial-, viral-, and fungal-derived pathogen-associated molecular patterns, respectively"* ([PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)). This confirms both the identity (**RTL9 = SIRH10**) and the **antifungal specificity** of Rtl9 within the trio. The shared molecular hallmark is the **retroviral Gag/capsid-like domain** (PEG10-RTL1_C-capsid; PF30901 in UniProt Q32KG4).

### Finding 5 — Protein architecture: a large protein with a single C-terminal capsid-like domain

Based on **UniProt Q32KG4** and **InterPro** domain mapping, RTL9 is a **large, 1339-amino-acid (~138 kDa) protein**. Its domain organization is:

| Feature | Location (aa) | Source | Interpretation |
|---|---|---|---|
| **PEG10/RTL1 C-terminal capsid-like domain** (retroviral Gag) | ~1219–1285 | Pfam PF30901 / IPR063300 | The functional module; viral capsid-derived |
| **RTL9-family signature** | 108–1335 | PANTHER PTHR47702 / IPR042919 | Family-defining region spanning most of the protein |
| Disordered / low-complexity regions | e.g., 533–555, 679–711, 1078–1116 | UniProt | Central flexible/linker segments |
| **No** CCHC zinc-knuckle, protease, or reverse-transcriptase domains | — | UniProt annotation | Only the capsid module survives from the ancestral retroelement |

The **capsid-like domain sits at the extreme C-terminus** — precisely the region whose deletion (RTL9ΔC) abolishes function (Finding 2). The **extended, unique N-terminal region (~residues 1–~1200)** has no recognized viral-derived domains and no assigned catalytic function. The absence of the protease and reverse-transcriptase modules present in autonomous retroelements (and in PEG10/RTL1) is the molecular signature of **domestication**: the host retained the structural (Gag/capsid) part while discarding the replicative machinery.

### Finding 6 — Genomic context: an X-linked, single-copy gene conserved to human RGAG1

Per **Ensembl GRCm39** (gene **ENSMUSG00000085584**; **MGI:2685231**), mouse *Rtl9* maps to the **X chromosome** (~141,876,886–141,887,293, plus strand) and has a **single canonical protein-coding transcript** (Rtl9-201 / ENSMUST00000165829). The gene is **syntenic with the human ortholog *RGAG1* on Xq13**, indicating conservation of the locus across eutherians. X-linkage is biologically relevant because it situates Rtl9 within the broader theme of X-chromosomal placement of several domesticated retroelement-derived genes, with potential implications for sex-biased expression/dosage that remain unexplored.

### Finding 7 (consolidating / negative) — No alternative molecular function is documented

Targeted literature searches for alternative functions of mouse *Rtl9* / human *RGAG1* — including roles in **spermatogenesis, RNA binding, testis biology, or transcription-factor activity** — returned **no specific primary literature** supporting such functions. The **only experimentally characterized function** is innate antifungal immunity in brain microglia (Ishino et al. 2023, [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)). Importantly, the supporting literature derives essentially from a **single research group** (Ishino / Kaneko-Ishino / Irie), a notable caveat for independent corroboration (see Limitations).

---

## Mechanistic Model / Interpretation

The data converge on a parsimonious model in which an ancient retrovirus was "disarmed" and repurposed by the host as a lysosomal antifungal effector in brain immune cells.

```
   EVOLUTIONARY ORIGIN                     PRESENT-DAY FUNCTION (mouse brain)
   ------------------                     ----------------------------------
  Sushi-ichi retrotransposon
   (metavirus / retrovirus-like)
            |
            |  domestication in a
            |  eutherian ancestor
            v
   11 RTL/SIRH genes  ----------->  Microglial innate-immune "trio":
   (Gag/capsid retained;              RTL6/SIRH3  -> bacteria (LPS)
    protease & RT discarded)          RTL5/SIRH8  -> viruses (dsRNA)
                                       RTL9/SIRH10 -> FUNGI (zymosan)  <= this gene


   RTL9 PROTEIN (1339 aa, X-linked)
   +------------------------------------------------+---------------+
   |   Unique N-terminal region (~1-1200 aa)        | Gag/capsid    |
   |   no catalytic/viral domains; disordered links | PF30901       |
   |                                                | (~1219-1285)  |
   +------------------------------------------------+-------+-------+
                                                           | ESSENTIAL
                                                           | (RTL9dC = inactive)
                                                           v
   MICROGLIA: fungal particle (zymosan) phagocytosed
            |
            v
   LYSOSOME  --- RTL9 localizes here --->  DEGRADATION of fungal material
```

**Interpretation of molecular function.** RTL9 is best classified not as a conventional enzyme, transporter, or signaling ligand, but as a **domesticated capsid-derived effector protein** that acts in the **lysosomal degradation of fungal PAMPs**. The precise biochemical mechanism — whether RTL9 directly disrupts the fungal β-glucan/chitin cell wall, binds and traffics fungal material, scaffolds other hydrolases, or exploits the self-assembly/binding capacity of the ancestral capsid fold within the lysosome — is **not yet resolved** by the available data. What is firmly established is (i) the **compartment** (microglial lysosome), (ii) the **substrate target** (fungal cell-wall material, modeled by zymosan), and (iii) the **essential module** (C-terminal Gag/capsid domain). In retroviruses the Gag capsid domain mediates protein–protein oligomerization and particle assembly; the strict requirement of this domain for zymosan degradation suggests RTL9 may repurpose that binding/assembly capacity as the structural basis for antifungal effector activity.

**Pathway placement.** RTL9 operates downstream of **fungal particle recognition and phagocytosis** by microglia, in the **degradative (phagolysosomal) arm of innate immunity**. It functions in parallel with — and complementary to — RTL6 (anti-bacterial) and RTL5 (anti-viral), which handle distinct PAMP classes and reside partly in the extracellular space. This positions the RTL trio as a **eutherian-specific layer of CNS innate defense**, likely acting alongside canonical pattern-recognition pathways (e.g., C-type lectin/Dectin-1 and TLR signaling) rather than replacing them, though direct links to those pathways have not been experimentally mapped for RTL9.

---

## Evidence Base

| PMID | Paper (abbrev.) | Role in this report | How it supports / qualifies findings |
|---|---|---|---|
| [37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/) | *Retrovirus-Derived RTL9…* (Ishino et al. 2023) | **Primary functional study** | Direct experimental evidence for Findings 1–3: RTL9 is expressed in microglia, degrades zymosan, localizes to lysosomes, and requires its C-terminal Gag domain (RTL9ΔC = loss of activity). |
| [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | *Virus-Derived Domesticated Genes in Microglia and Resident Macrophages* (Irie et al. 2026) | **Synthesis / context** | Confirms RTL9 = SIRH10 and its antifungal PAMP specificity within the RTL6/RTL5/RTL9 microglial trio (Findings 3–4). |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *Retrovirus-Derived RTL/SIRH…* (Kaneko-Ishino & Ishino 2023) | **Family review** | Establishes the 11-member eutherian RTL/SIRH family derived from a sushi-ichi retrotransposon and its roles in placenta, brain, and innate immunity (Finding 4). |
| [36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) | *RTL5 and RTL6 genes are novel constituents of the innate immune system…* (Irie et al. 2022) | **Sibling-gene comparator** | Documents RTL5 (anti-dsRNA) and RTL6 (anti-LPS) as microglial innate-immune genes appearing as extracellular dots/granules — the paradigm into which RTL9 (anti-fungal, lysosomal) fits, and a contrast in subcellular localization. |

**Database annotations** (supporting, but lower-tier than primary literature): UniProt **Q32KG4** (sequence, domain, 1339-aa length), InterPro/Pfam (**IPR063300**, **IPR042919**, **PF30901**), Ensembl **ENSMUSG00000085584**, MGI **MGI:2685231** (X-linkage, single transcript, human *RGAG1* synteny).

---

## Hypotheses: Supported, Refuted, and Open

**Supported:**
- RTL9 functions in **innate antifungal immunity in the brain** (strong genetic + imaging evidence).
- RTL9 acts in **microglial lysosomes** on internalized fungal material.
- The **C-terminal Gag/capsid-like domain is functionally essential** (loss-of-function by domain truncation).

**Refuted / not supported:**
- No evidence supports alternative molecular functions for Rtl9/RGAG1 such as spermatogenesis, RNA binding, or transcription-factor activity (targeted searches returned no primary literature).

**Open / not yet established:**
- Whether RTL9 is itself catalytic (a hydrolase) or a facilitator/scaffold enabling lysosomal degradation.
- The precise molecular partner(s) and whether RTL9 directly binds β-glucan/mannan.
- Whether human *RGAG1*/RTL9 performs the same antifungal function (mouse data are the primary evidence; the gene is conserved across eutherians).

---

## Limitations and Knowledge Gaps

1. **Single-group literature base.** The entire experimental characterization of Rtl9 rests on work from one research group (Ishino / Kaneko-Ishino / Irie). **Independent replication** of the antifungal/lysosomal phenotype has not yet appeared.

2. **"Degradation" mechanism is undefined.** It remains unknown whether RTL9 is itself a catalytic/hydrolytic protein, a structural scaffold, a cargo-binding/trafficking factor, or a cofactor for canonical lysosomal hydrolases. No enzymatic activity, substrate kinetics, or direct biochemical assay of cell-wall cleavage has been reported.

3. **Zymosan is a surrogate, not a live pathogen.** Antifungal function was demonstrated against zymosan (a cell-wall preparation). Whether RTL9 confers protection against **live fungal infection** (e.g., *Candida*, *Cryptococcus*, *Aspergillus*) in vivo, and whether *Rtl9*-knockout mice show increased CNS fungal susceptibility, has not been shown.

4. **Role of the large N-terminal region is unknown.** ~1200 residues of the protein have no assigned domain or function. Their contribution (localization, oligomerization, substrate recognition) is unexplored.

5. **Structural data are absent.** No experimental structure of RTL9 exists; the capsid-like domain assignment is bioinformatic. Whether RTL9 self-assembles into capsid-like/virus-like particles (as some PEG10/RTL1 relatives do) is untested.

6. **Pathway connections not mapped.** Links between RTL9 and canonical fungal-recognition signaling (Dectin-1/CARD9, TLR2) or lysosomal maturation pathways are not established.

7. **X-linkage / dosage biology unexplored.** Potential sex-biased expression, escape from X-inactivation, and functional consequences are not addressed.

---

## Proposed Follow-up Experiments / Actions

1. **Biochemical mechanism of "degradation."** Purify recombinant RTL9 (and the isolated C-terminal capsid domain) and test for direct activity against fungal cell-wall polymers (β-1,3-glucan, mannan, chitin) in vitro; distinguish catalytic activity from binding/scaffolding using defined substrates and controls.

2. **Live-pathogen challenge.** Test *Rtl9*-knockout vs. wild-type mice for susceptibility to CNS fungal infection (*Candida albicans*, *Cryptococcus neoformans*), measuring fungal burden, microglial clearance, and survival.

3. **Structure determination.** Obtain a cryo-EM or crystal structure of the capsid-like domain; test whether RTL9 forms capsid-like/virus-like particles and how the domain engages fungal ligands.

4. **Domain dissection.** Systematically delete/mutate N-terminal subregions and the capsid domain to map the minimal functional unit and identify substrate-binding or targeting determinants, extending the RTL9ΔC result.

5. **Pathway epistasis.** Combine *Rtl9* loss with perturbation of Dectin-1/CARD9 or lysosomal hydrolase pathways to place RTL9 in the fungal-clearance signaling/degradation hierarchy.

6. **Independent replication & human relevance.** Reproduce the microglial/lysosomal antifungal phenotype independently, and test whether human *RGAG1* performs an analogous function in human microglia or iPSC-derived microglia.

7. **Proximity/interactome mapping.** Use proximity labeling (BioID/TurboID) in microglia to identify RTL9's lysosomal interaction partners and clarify whether it recruits other hydrolases.

---

## Conclusion

Mouse **Rtl9/SIRH10 (Q32KG4)** is a **domesticated retrovirus-derived gene** that functions as an **innate antifungal effector in brain microglia**. It localizes to **microglial lysosomes**, where it is required to **degrade internalized fungal material (zymosan)**, and this activity depends on its **C-terminal retroviral Gag/capsid-like domain** (PF30901; residues ~1219–1285), as shown by the loss-of-function RTL9ΔC truncation. It is the **fungus-responding member of an X-linked, eutherian-specific microglial RTL trio** (RTL9–fungi, RTL5–viruses, RTL6–bacteria). No alternative molecular function is documented, and the precise biochemical mechanism of fungal degradation remains to be defined.

---

### References

- Ishino F, Itoh J, Irie M, Matsuzawa A, Naruse M, Suzuki T, Hiraoka Y, Kaneko-Ishino T. *Retrovirus-Derived RTL9 Plays an Important Role in Innate Antifungal Immunity in the Eutherian Brain.* Int J Mol Sci. 2023. **[PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/)** (primary functional study).
- Irie M, Ishino F, Kaneko-Ishino T. *Virus-Derived Domesticated Genes in Microglia and Resident Macrophages: Insights into Placenta-Driven Evolution in Mammals.* 2026. **[PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)** (review; microglial RTL trio).
- Kaneko-Ishino T, Ishino F. *Retrovirus-Derived RTL/SIRH: Their Diverse Roles in the Current Eutherian Developmental System and Contribution to Eutherian Evolution.* Biomolecules. 2023. **[PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)** (family review).
- Irie M, Itoh J, Matsuzawa A, et al. *Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain.* 2022. **[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)** (sibling-gene context).


## Artifacts

- [OpenScientist final report](Rtl9-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl9-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:37834332
2. PMID:42511665
3. PMID:37892118
4. PMID:36162816