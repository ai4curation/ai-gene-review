---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:13:43.001776'
end_time: '2026-10-24T15:46:18.930205'
duration_seconds: 1955.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Ldoc1
  gene_symbol: Ldoc1
  uniprot_accession: Q7TPY9
  protein_description: 'RecName: Full=Protein LDOC1;'
  gene_info: Name=Ldoc1; Synonyms=Gm366;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the LDOC1 family. .
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ldoc1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ldoc1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q7TPY9
- **Protein Description:** RecName: Full=Protein LDOC1;
- **Gene Information:** Name=Ldoc1; Synonyms=Gm366;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the LDOC1 family. .
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Ldoc1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Ldoc1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Ldoc1** (gene ID: Ldoc1, UniProt: Q7TPY9) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Ldoc1* (Q7TPY9 / Sirh7 / Mart7)

**Target:** *Ldoc1* (synonym *Gm366*; also **Sirh7**, **Mart7**), *Mus musculus*, UniProt **Q7TPY9**, Ensembl **ENSMUSG00000057615**, MGI:2685212.
**Protein family:** LDOC1 family; retrotransposon Gag/capsid-derived domain **RTL1/1-8/LDOC_capsid-like** (InterPro IPR032549; Pfam PF16297 RTL1-8_LDOC).

## Summary

Mouse **Ldoc1** (UniProt **Q7TPY9**; gene synonyms *Sirh7*, *Mart7*, *Gm366*) encodes a small (151-residue, ~17.5 kDa) nuclear regulatory/adaptor protein that is **not an enzyme, transporter, or conventional structural protein**. Instead, it is a **domesticated retrotransposon Gag/capsid-derived regulatory protein** whose defining molecular activity is the **negative regulation of NF-κB (Nuclear Factor-kappa B) signaling**. The Mouse Genome Informatics (MGI) database formally names the gene a "regulator of NFKB signaling." Ldoc1 belongs to the **sushi-ichi-related retrotransposon homolog (SIRH / Mart) family** of Ty3/gypsy LTR-retroelement-derived genes, carrying an **RTL1/1-8/LDOC capsid-like domain** (InterPro IPR032549; Pfam PF16297). The identity verification mandated in the research brief is fully satisfied: the gene symbol, organism (*Mus musculus*), protein family (LDOC1/SIRH), and key domains all align consistently across UniProt, MGI, Ensembl, and the primary literature. There is **no ambiguity** — the mouse gene *Sirh7/Ldoc1* is the same locus as UniProt Q7TPY9, and the human ortholog *LDOC1* has been independently characterized and serves as cross-species corroboration (not a namesake confusion).

The **primary in-vivo function** of mouse Ldoc1, established by gene knockout, is in the **placenta**: it restrains the differentiation and endocrine output of trophoblast giant cells (TGCs). *Sirh7/Ldoc1* knockout mice overproduce placental progesterone (P4) and placental lactogen 1 (PL1), and pregnant knockout females show delayed parturition and poor pup weaning ([PMID: 25468940](https://pubmed.ncbi.nlm.nih.gov/25468940/)). At the **molecular level**, LDOC1 acts predominantly in the **nucleus** (nucleoplasm and nucleolus) as a pro-apoptotic adaptor that **inhibits NF-κB activation**, an activity first characterized in human pancreatic cancer cells ([PMID: 12712434](https://pubmed.ncbi.nlm.nih.gov/12712434/)) and repeatedly confirmed in thyroid, biliary, and lung cancer models. It engages a defined set of protein partners — the pattern-recognition receptor **NOD2**, the nucleolar GTPase **GNL3L**, and the transcription factor **MZF-1** — that connect it to innate-immune and proliferative NF-κB circuits.

The coherent picture is of a **retrotransposon-exapted nuclear tuning protein** for the NF-κB pathway. In the placenta, this NF-κB/apoptosis-modulating activity is deployed to control the timing and extent of trophoblast differentiation and hormone secretion; in somatic and cancer cells, the same activity manifests as tumor-suppressive, pro-apoptotic NF-κB repression. This report details the evidence behind each component of this model, the subcellular localization, the pathway connections, and the remaining knowledge gaps.

---

## Gene and Protein Identity Verification

Before presenting functional findings, the research brief requires explicit confirmation of identity. All databases and primary sources converge on a single, unambiguous locus:

| Attribute | Value | Source |
|-----------|-------|--------|
| UniProt accession | Q7TPY9 | UniProt |
| Protein | Protein LDOC1 | UniProt |
| Gene name / synonyms | *Ldoc1* / *Sirh7*, *Mart7*, *Gm366* | UniProt, MGI |
| Organism | *Mus musculus* (Mouse) | UniProt |
| Length / mass | 151 aa / 17,546 Da | UniProt |
| Protein family | LDOC1 / SIRH / Mart family | UniProt, [PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/) |
| Key domain | RTL1/1-8/LDOC capsid-like (IPR032549; Pfam PF16297 RTL1-8_LDOC) | InterPro/Pfam |
| Chromosomal location | X chromosome (ENSMUSG00000057615; GRCm39 ChrX:60,747,229–60,754,561, + strand) | Ensembl/MGI |
| MGI official description | "regulator of NFKB signaling" (MGI:2685212) | MGI |

The gene symbol "Ldoc1" **matches** the UniProt protein description ("Protein LDOC1"); the organism is correctly mouse; and the retroviral Gag/capsid-like domain is consistent with the SIRH/Mart retrotransposon-derived family described in the literature. The mouse X-linkage is consistent with the human ortholog's location at Xq27. **No conflicting gene of the same symbol in another organism was mistaken for the target** — the human *LDOC1* literature describes the direct ortholog, not a namesake, and is used here as cross-species corroboration of conserved molecular function.

---

## Key Findings

### Finding 1 — The primary in-vivo function is placental: restraining trophoblast giant cell differentiation and endocrine output

The strongest, most direct evidence for the physiological role of mouse Ldoc1 comes from a targeted knockout study. Naruse and colleagues generated *Sirh7/Ldoc1* knockout mice and found that they **exhibit abnormal placental cell differentiation and maturation**, leading to an **overproduction of placental progesterone (P4) and placental lactogen 1 (PL1)** from **trophoblast giant cells (TGCs)** ([PMID: 25468940](https://pubmed.ncbi.nlm.nih.gov/25468940/)). The verbatim finding states: *"Sirh7/Ldoc1 knockout (KO) mice exhibited abnormal placental cell differentiation/maturation, leading to an overproduction of placental progesterone (P4) and placental lactogen 1 (PL1) from trophoblast giant cells (TGCs)."*

Crucially, the knockout produced a reproductive-physiology phenotype: *"Pregnant Sirh7/Ldoc1 knockout females also displayed delayed parturition associated with a low pup weaning rate."* Because progesterone maintains pregnancy and its withdrawal is required to trigger labor, the overproduction of P4 in knockout placentas provides a mechanistic explanation for the delayed parturition. This establishes that the **normal role of Ldoc1 is to limit (negatively regulate) TGC differentiation and endocrine secretion** — acting as a brake on placental hormone output.

A subsequent authoritative review reinforces this placental assignment at the family level: *"PEG10/SIRH1 as well as PEG11/RTL1/SIRH2 and SIRH7/LDOC1 play essential roles in placenta formation, maintenance of fetal capillaries and the differentiation/maturation of a variety of placental cells, respectively"* ([PMID: 28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/)). The review attributes the **differentiation/maturation of diverse placental cell types** specifically to SIRH7/LDOC1.

This function is reflected in the curated GO annotations for Q7TPY9: **maternal placenta development** (GO:0001893, evidence code IMP:MGI) and **maternal process involved in parturition** (GO:0060137, IMP:MGI) — both "Inferred from Mutant Phenotype," directly encoding the knockout result.

### Finding 2 — The defining molecular activity is inhibition of NF-κB signaling, promoting apoptosis

The conserved biochemical function of LDOC1 is **negative regulation of the NF-κB transcription-factor pathway**. This was first characterized by Nagasaki and colleagues, who showed that transient LDOC1 expression **inhibits TNF-α/PMA-induced NF-κB reporter activation in a dose-dependent manner** and enhances the antiproliferative/apoptotic effects of these stimuli in BxPC-3 pancreatic cancer cells, while **not affecting p53, AP1, or CRE reporters** — demonstrating specificity for NF-κB ([PMID: 12712434](https://pubmed.ncbi.nlm.nih.gov/12712434/)). The authors concluded: *"LDOC1 is a novel regulator of NF-kappaB that can affect the PMA or TNF-alpha-mediated pathway to apoptosis through inhibition of NF-kappaB activation in BxPC3 pancreatic cancer cells."*

This activity has been independently reproduced. In papillary thyroid carcinoma, LDOC1 **inhibits proliferation and promotes apoptosis by repressing NF-κB activation** (reducing nuclear p65), and inhibiting NF-κB reverses the effect of LDOC1 ablation ([PMID: 26637328](https://pubmed.ncbi.nlm.nih.gov/26637328/); [PMID: 31889386](https://pubmed.ncbi.nlm.nih.gov/31889386/)). The title of the former paper is explicit: *"LDOC1 inhibits proliferation and promotes apoptosis by repressing NF-κB activation in papillary thyroid carcinoma."*

A nuance in the literature concerns the direction of the LDOC1–NF-κB relationship across cell contexts. In human intrahepatic biliary epithelial cells, overexpression of LDOC1 was reported to **increase** NF-κB expression and inhibit apoptosis ([PMID: 23942005](https://pubmed.ncbi.nlm.nih.gov/23942005/)), the opposite directionality from the pancreatic/thyroid data. The preponderance of evidence (pancreatic, thyroid, and the mouse placental brake phenotype) supports LDOC1 as a **negative** regulator of NF-κB and a **pro-apoptotic** factor, but the biliary result indicates the functional output is context-dependent. The consistent core is that **LDOC1 is a regulatory node of the NF-κB pathway**, matching the MGI name "regulator of NFKB signaling."

### Finding 3 — LDOC1 is a nucleocytoplasmic adaptor interacting with GNL3L and MZF-1

LDOC1 physically engages specific partners that connect its NF-κB activity to proliferation control. Thoompumkal and colleagues identified LDOC1 as *"a novel interacting partner of GNL3L"* (Guanine nucleotide-binding protein-like 3-like, a nucleolar GTPase), and showed that *"ectopic expression of LDOC1 destabilizes endogenous GNL3L levels and down modulates GNL3L-induced cell proliferation"* ([PMID: 27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/)). Because GNL3L drives NF-κB-dependent proliferation, LDOC1 opposes it by destabilizing GNL3L — a mechanistic bridge between the protein-interaction data and the NF-κB-repression phenotype. This LDOC1/GNL3L/NF-κB axis was later shown to be pharmacologically targetable: calycosin inhibits gemcitabine-resistant lung cancer proliferation by **increasing LDOC1 and decreasing GNL3L/NF-κB** ([PMID: 37635478](https://pubmed.ncbi.nlm.nih.gov/37635478/)).

LDOC1 also interacts with the transcription factor **MZF-1 (myeloid zinc finger gene 1)**, which *"enhance[s] LDOC1 activity favoring apoptosis"* ([PMID: 27076087](https://pubmed.ncbi.nlm.nih.gov/27076087/)). This cooperative interaction amplifies the pro-apoptotic output of LDOC1.

Localization is **regulated and dynamic**: although primarily nuclear, *"LDOC1 was translocated from the nucleus to the cytoplasm in human thyroid cancer"* ([PMID: 31889386](https://pubmed.ncbi.nlm.nih.gov/31889386/)), indicating that nucleocytoplasmic shuttling is coupled to its tumor-suppressive function and that mislocalization accompanies loss of function in disease.

### Finding 4 — LDOC1 interacts with NOD2, placing it in pattern-recognition-receptor innate-immune signaling

A yeast two-hybrid screen for NOD2-interacting proteins identified LDOC1, with the interaction confirmed by co-immunoprecipitation and/or BRET ([PMID: 27812135](https://pubmed.ncbi.nlm.nih.gov/27812135/)): *"The primary interaction was confirmed by coimmunoprecipitation and/or bioluminescence resonance energy transfer (BRET) experiments for 11 of these proteins (ANKHD1, CHMP5, SDCCAG3, TRIM41, LDOC1, PPP1R12C, DOCK7, VIM, KRT15, PPP2R3B, and C10Orf67)."* NOD2 is a cytosolic pattern-recognition receptor that senses the bacterial peptidoglycan fragment muramyl dipeptide (MDP) and signals via RICK/RIPK2: *"In response to its bacterial ligand, NOD2 interacts with RICK and activates the NF-κB and MAPK pathways, inducing gene transcription and synthesis of proteins required to initiate a balanced immune response."*

This interaction is significant because it ties LDOC1's NF-κB-regulating activity to a **defined upstream innate-immune receptor**. Consistently, UniProt Q7TPY9 records "Interacts with NOD2" and the GO terms **cellular response to lipopolysaccharide** (GO:0071222, ISS) and **cellular response to muramyl dipeptide** (GO:0071225, ISS). Together these suggest LDOC1 can modulate NOD2-driven NF-κB/MAPK responses, providing a receptor-proximal context for its role as an NF-κB tuner.

### Finding 5 — Ldoc1/Sirh7 is a domesticated Ty3/gypsy (sushi-ichi) retrotransposon Gag-derived gene

The evolutionary origin of Ldoc1 explains its unusual properties. Henke and colleagues established that *"Mammalian retrotransposon transcripts (Mart1-9), also called sushi-ichi-related retrotransposon-homolog (SIRH) genes, are a class of Ty3/gypsy LTR-retroelements showing moderate homology to the sushi-ichi LTR-retrotransposon in pufferfish"* ([PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)), and documented selective expression of SIRH-family sense/antisense transcripts in trophoblast subtypes during mouse placentogenesis. Ldoc1 is *Sirh7/Mart7* within this family.

Structurally, Q7TPY9 contains the **RTL1/1-8/LDOC capsid-like domain** (InterPro IPR032549; Pfam PF16297 "RTL1-8_LDOC"), a module derived from a **retroviral Gag capsid protein**. This domain origin is important for interpreting function: Gag/capsid proteins are self-associating, nucleic-acid/protein-binding scaffolds, consistent with LDOC1 acting as a **non-enzymatic adaptor/scaffold** rather than a catalytic protein. The broader significance of retrotransposon exaptation in mammals is emphasized by multiple reviews: such genes made *"crucial contributions to the establishment and diversification of mammals via placental formation"* ([PMID: 20646026](https://pubmed.ncbi.nlm.nih.gov/20646026/)), and placental-specific retrotransposon-derived genes are proposed to be reactivated in cancer ([PMID: 28976008](https://pubmed.ncbi.nlm.nih.gov/28976008/)) — a theme that unifies the placental and tumor-suppressor literatures for LDOC1.

### Finding 6 — A small nuclear protein with an acidic, disordered C-terminus

UniProt Q7TPY9 describes a protein of **151 residues (~17.5 kDa)** with the keyword and subcellular location **Nucleus**, and GO cellular components **nucleoplasm** (GO:0005654) and **nucleolus** (GO:0005730). A single predicted **disordered, acidic-residue-biased region** spans positions **133–151** (the C-terminal tail). Acidic disordered tails frequently mediate protein–protein interactions and transcriptional/regulatory contacts, consistent with LDOC1's adaptor role. The nucleolar localization dovetails with its interaction with the nucleolar GTPase GNL3L (Finding 3). The placental/parturition functions carry MGI genetic (IMP) support as noted in Finding 1.

### Finding 7 — Mouse Ldoc1 is X-linked and officially annotated as a "regulator of NFKB signaling"

Ensembl/MGI place *Ldoc1* on the **X chromosome** (ENSMUSG00000057615; GRCm39 ChrX:60,747,229–60,754,561, + strand), as a protein-coding gene. The official MGI gene description is **"regulator of NFKB signaling" (MGI:2685212)**. The X-linkage is consistent with the human ortholog's Xq27 location and with the SIRH family's retrotransposon-derived, often imprinted/X-linked character. This annotation — derived independently from the experimental NF-κB literature — provides a database-level consensus that NF-κB regulation is the gene's signature molecular function.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent model in which a **retrotransposon-exapted nuclear adaptor tunes NF-κB signaling**, with the physiological readout depending on cell type.

```
   EVOLUTIONARY ORIGIN
   Ty3/gypsy (sushi-ichi) LTR retrotransposon
          │  exaptation / domestication (eutherian mammals)
          ▼
   Ldoc1 / Sirh7 / Mart7  (X-linked, 151 aa, ~17.5 kDa)
   RTL1-8/LDOC Gag-capsid-like domain + acidic disordered C-terminus (133–151)
          │
          ▼  localizes to NUCLEUS (nucleoplasm + nucleolus);
          │  shuttles to cytoplasm when dysregulated
   ┌───────────────────────────────────────────────────────────┐
   │  MOLECULAR ACTIVITY: negative regulation of NF-κB          │
   │                                                            │
   │  Partners:                                                 │
   │   • NOD2  ── innate-immune PRR (MDP/LPS) → RICK → NF-κB/MAPK│
   │   • GNL3L ── nucleolar GTPase; LDOC1 destabilizes it,      │
   │              lowering GNL3L-driven NF-κB proliferation     │
   │   • MZF-1 ── enhances LDOC1 pro-apoptotic activity         │
   └───────────────────────────────────────────────────────────┘
          │                                   │
          ▼                                   ▼
   SOMATIC / CANCER CELLS              PLACENTAL TROPHOBLAST (in vivo)
   ↓ NF-κB activation                  Brakes TGC differentiation &
   ↑ apoptosis                         endocrine output (P4, PL1)
   → tumor-suppressor behavior         KO → P4/PL1 overproduction,
                                          delayed parturition
```

The unifying principle is that **LDOC1 is a non-enzymatic nuclear regulatory protein**, not a catalyst, transporter, or classical structural protein. The questions "what reaction does it catalyze / what does it transport" therefore have a specific answer: **none** — its primary function is as a **signaling adaptor/modulator that dampens NF-κB transcriptional output and biases cells toward apoptosis/differentiation control**. The Gag-capsid-derived domain supplies a self-associating scaffold fold rather than enzymatic machinery, and the acidic disordered C-terminus likely mediates the protein–protein contacts (GNL3L, MZF-1, NOD2) that implement regulation.

In the **placenta** — the one tissue with direct mouse loss-of-function data — this NF-κB/apoptosis-tuning activity translates into **control of trophoblast giant cell differentiation and hormone secretion**. NF-κB signaling is a known driver of trophoblast differentiation and endocrine programs; by restraining it, Ldoc1 prevents premature or excessive TGC maturation and hormone (P4, PL1) overproduction. Loss of this brake elevates progesterone, which maintains pregnancy and consequently **delays parturition**. Thus the molecular function (NF-κB repression) and the organismal phenotype (placental endocrine restraint, parturition timing) are two faces of the same activity.

In **somatic/cancer cells**, the identical NF-κB-repressing, pro-apoptotic activity presents as **tumor-suppressor behavior**, consistent with the gene's name (Leucine zipper, Down-regulated in Cancer 1) and its frequent silencing in tumors. The LDOC1/GNL3L/NF-κB axis is a pharmacologically actionable node (e.g., calycosin).

| Cell/tissue context | LDOC1 action on NF-κB | Functional outcome | Evidence |
|---|---|---|---|
| Pancreatic cancer (BxPC-3) | Inhibits (dose-dependent) | ↑ TNF-α/PMA-induced apoptosis | [PMID: 12712434](https://pubmed.ncbi.nlm.nih.gov/12712434/) |
| Papillary thyroid carcinoma | Represses (↓ nuclear p65) | ↓ proliferation, ↑ apoptosis | [PMID: 26637328](https://pubmed.ncbi.nlm.nih.gov/26637328/), [PMID: 31889386](https://pubmed.ncbi.nlm.nih.gov/31889386/) |
| Gemcitabine-resistant lung cancer | ↑LDOC1 → ↓GNL3L/NF-κB | ↓ proliferation, ↓ stemness | [PMID: 37635478](https://pubmed.ncbi.nlm.nih.gov/37635478/) |
| Biliary epithelial cells | Increases NF-κB (context exception) | ↓ apoptosis | [PMID: 23942005](https://pubmed.ncbi.nlm.nih.gov/23942005/) |
| Mouse placental TGCs (in vivo KO) | Restrains NF-κB-driven differentiation | KO → P4/PL1 overproduction, delayed parturition | [PMID: 25468940](https://pubmed.ncbi.nlm.nih.gov/25468940/) |

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|------|---------------------|--------------|
| [25468940](https://pubmed.ncbi.nlm.nih.gov/25468940/) | *Sirh7/Ldoc1 knockout mice exhibit placental P4 overproduction and delayed parturition* | **Keystone in-vivo mouse evidence**: KO → abnormal placental differentiation, P4/PL1 overproduction from TGCs, delayed parturition. Defines primary physiological function. |
| [28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/) | *Evolution of brain functions ... and LTR retrotransposon-derived genes* (review) | Attributes placental cell differentiation/maturation role to SIRH7/LDOC1; places gene in SIRH family. |
| [12712434](https://pubmed.ncbi.nlm.nih.gov/12712434/) | *Leucine-zipper protein LDOC1 inhibits NF-κB and sensitizes pancreatic cancer cells to apoptosis* | **Foundational molecular mechanism**: dose-dependent NF-κB inhibition, specificity (no effect on p53/AP1/CRE), pro-apoptotic. |
| [26637328](https://pubmed.ncbi.nlm.nih.gov/26637328/) | *LDOC1 inhibits proliferation and promotes apoptosis by repressing NF-κB in PTC* | Independent confirmation of NF-κB repression and pro-apoptotic function in thyroid cancer. |
| [31889386](https://pubmed.ncbi.nlm.nih.gov/31889386/) | *LDOC1 ... tumor-suppressive function in PTC* | Confirms NF-κB repression; documents nucleus→cytoplasm translocation in cancer. |
| [27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/) | *LDOC1 interacts with GNL3L to modulate NF-κB during proliferation* | Defines GNL3L interaction; LDOC1 destabilizes GNL3L and down-modulates NF-κB-dependent proliferation. |
| [27076087](https://pubmed.ncbi.nlm.nih.gov/27076087/) | *LDOC1 gene expression in Klinefelter syndrome* | Documents MZF-1 interaction enhancing LDOC1 pro-apoptotic activity. |
| [27812135](https://pubmed.ncbi.nlm.nih.gov/27812135/) | *New genes coding for NOD2 interacting proteins* | Validates LDOC1–NOD2 interaction by co-IP/BRET; links LDOC1 to NOD2–RICK–NF-κB/MAPK innate immunity. |
| [25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/) | *Sense/antisense transcripts of sushi-ichi-related retrotransposon family in placentogenesis* | Defines SIRH/Mart family (Ty3/gypsy origin); Sirh7/Ldoc1 membership; placental expression. |
| [37635478](https://pubmed.ncbi.nlm.nih.gov/37635478/) | *Calycosin inhibits lung cancer via LDOC1/GNL3L/NFκB* | Shows the LDOC1/GNL3L/NF-κB axis is pharmacologically targetable. |
| [23942005](https://pubmed.ncbi.nlm.nih.gov/23942005/) | *LDOC1 in biliary epithelial cells inhibits apoptosis through NF-κB* | Context-dependent exception (LDOC1 increases NF-κB); flags tissue-specific output. |
| [20646026](https://pubmed.ncbi.nlm.nih.gov/20646026/) | *Retrotransposon silencing ... evolution of placentation and imprinting* (review) | Evolutionary framework: retrotransposon exaptation enabled placental formation. |
| [28976008](https://pubmed.ncbi.nlm.nih.gov/28976008/) | *Placental-specific genes in cancer* (review) | Links placental retrotransposon-derived genes to cancer, unifying LDOC1's dual contexts. |

**How the evidence aligns:** Three independent cancer systems (pancreatic, thyroid, lung) plus the database annotation (MGI) converge on **NF-κB repression / pro-apoptosis** as the core molecular activity. The single mouse knockout study provides the only direct in-vivo physiological evidence and firmly localizes the primary function to **placental trophoblast endocrine control**. Protein-interaction studies (GNL3L, MZF-1, NOD2) supply mechanistic bridges, and family/evolutionary studies explain the protein's non-enzymatic, scaffold-like nature. The lone discordant result (biliary epithelium) is noted transparently as evidence of context-dependence rather than contradiction of the central model.

---

## Limitations and Knowledge Gaps

1. **Single in-vivo mouse study.** The entire physiological characterization of mouse Ldoc1 rests on one knockout paper ([PMID: 25468940](https://pubmed.ncbi.nlm.nih.gov/25468940/)). Independent replication of the placental/parturition phenotype would strengthen confidence.

2. **Mechanism of the placental phenotype is inferred, not demonstrated.** The link between LDOC1's NF-κB-repressing activity and the TGC overproduction of P4/PL1 is a logical synthesis; the specific NF-κB target genes and signaling events in trophoblast have not been directly mapped in the mouse knockout.

3. **Molecular NF-κB studies are predominantly human and cancer-derived.** The detailed mechanistic data (GNL3L, MZF-1, p65 nuclear levels, cytoplasmic translocation) come from human cancer cell lines. Whether these exact interactions operate in mouse placental trophoblast remains to be confirmed.

4. **Direction of NF-κB regulation is context-dependent.** Most data support LDOC1 as an NF-κB inhibitor/pro-apoptotic, but the biliary epithelial study shows the opposite. The structural/mechanistic basis for this context-dependence is unknown.

5. **No high-resolution structure or defined binding interface.** Functional assignment relies on InterPro/Pfam domain inference (Gag/capsid-like) and disorder prediction, not experimental structure. The regions of LDOC1 that contact NOD2, GNL3L, or MZF-1 are undefined.

6. **No enzymatic/transport activity has been excluded experimentally;** the "non-enzymatic adaptor" conclusion is inferred from the Gag-capsid-derived domain and the absence of any catalytic motif or reported activity.

7. **Possible redundancy/imprinting effects.** SIRH-family genes can be imprinted or partially redundant; the mild, incompletely penetrant knockout phenotype may reflect compensation that masks additional functions.

---

## Proposed Follow-up Experiments / Actions

1. **Trophoblast-specific mechanistic dissection.** Perform RNA-seq and NF-κB (p65) ChIP-seq in wild-type vs *Sirh7/Ldoc1*-KO trophoblast giant cells to directly test whether loss of Ldoc1 derepresses NF-κB target genes that drive P4/PL1 synthesis (e.g., steroidogenic and prolactin-family genes).

2. **Rescue and separation-of-function.** Re-express wild-type Ldoc1, an NF-κB-binding-deficient mutant, and a C-terminal-tail (133–151) deletion in KO trophoblast to determine whether NF-κB regulation and the acidic disordered tail are each required to restore normal P4/PL1 output.

3. **Map interaction interfaces.** Use truncation/point-mutant co-IP and BRET to define the LDOC1 regions contacting NOD2, GNL3L, and MZF-1, and test whether these interactions occur in placental cells, not just cancer lines.

4. **Test the NOD2 axis functionally.** Stimulate Ldoc1-expressing vs Ldoc1-deficient cells with muramyl dipeptide/LPS and measure NF-κB/MAPK output to determine whether LDOC1 tunes NOD2-driven innate-immune signaling (relevant to placental immune tolerance).

5. **Resolve the context-dependence.** Directly compare LDOC1's effect on NF-κB in matched epithelial vs cancer vs trophoblast cells to identify the cofactor(s) (e.g., GNL3L abundance, MZF-1) that switch LDOC1 between NF-κB inhibition and activation.

6. **Structural characterization.** Obtain an experimental or high-confidence predicted structure (AlphaFold) of the Gag-capsid-like domain and test for self-association/oligomerization, which Gag-derived proteins commonly exhibit.

---

## Conclusion

Mouse **Ldoc1 (Q7TPY9; Sirh7/Mart7)** is a small, X-linked, **nuclear, non-enzymatic regulatory/adaptor protein** derived from a domesticated sushi-ichi (Ty3/gypsy) LTR-retrotransposon Gag/capsid module. Its **defining molecular function is negative regulation of NF-κB signaling**, acting as a pro-apoptotic nuclear tuner that interacts with NOD2, GNL3L, and MZF-1. Its **primary in-vivo function in the mouse**, demonstrated by knockout, is to **restrain trophoblast giant cell differentiation and placental progesterone/placental-lactogen output**, thereby controlling placental endocrine function and the timing of parturition. It operates predominantly in the **nucleus (nucleoplasm and nucleolus)** of placental trophoblast cells, with regulated shuttling to the cytoplasm associated with loss of function in disease.


## Artifacts

- [OpenScientist final report](Ldoc1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ldoc1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25468940
2. PMID:12712434
3. PMID:25888968
4. PMID:28484174
5. PMID:26637328
6. PMID:31889386
7. PMID:23942005
8. PMID:27764577
9. PMID:37635478
10. PMID:27076087
11. PMID:27812135
12. PMID:20646026
13. PMID:28976008