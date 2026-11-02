---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T13:35:32.163151'
end_time: '2026-10-24T13:58:56.788256'
duration_seconds: 1404.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL6
  gene_symbol: RTL6
  uniprot_accession: Q6ICC9
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 6 {ECO:0000312|HGNC:HGNC:13343};
    AltName: Full=Leucine zipper protein down-regulated in cancer cells-like; AltName:
    Full=Mammalian retrotransposon-derived protein 6 {ECO:0000250|UniProtKB:Q505G4};
    AltName: Full=Protein LDOC1L {ECO:0000305};'
  gene_info: Name=RTL6 {ECO:0000312|HGNC:HGNC:13343}; Synonyms=LDOC1L {ECO:0000305},
    MAR6, MART6 {ECO:0000250|UniProtKB:Q505G4};
  organism_full: Homo sapiens (Human).
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RTL6-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL6-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q6ICC9
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 6 {ECO:0000312|HGNC:HGNC:13343}; AltName: Full=Leucine zipper protein down-regulated in cancer cells-like; AltName: Full=Mammalian retrotransposon-derived protein 6 {ECO:0000250|UniProtKB:Q505G4}; AltName: Full=Protein LDOC1L {ECO:0000305};
- **Gene Information:** Name=RTL6 {ECO:0000312|HGNC:HGNC:13343}; Synonyms=LDOC1L {ECO:0000305}, MAR6, MART6 {ECO:0000250|UniProtKB:Q505G4};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the LDOC1 family. .
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL6" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL6' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL6** (gene ID: RTL6, UniProt: Q6ICC9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RTL6 (LDOC1L / SIRH3 / MART6): A Domesticated Retroviral Gag Protein Functioning as a Secreted Microglial Anti-Bacterial Effector in the Brain

**Target:** RTL6 (Retrotransposon Gag-like protein 6) — Human (*Homo sapiens*)
**UniProt:** [Q6ICC9](https://www.uniprot.org/uniprotkb/Q6ICC9) · **HGNC:** 13343 · **Ensembl:** ENSG00000188636
**Synonyms:** LDOC1L, SIRH3, MAR6, MART6, "Leucine zipper protein down-regulated in cancer cells-like"
**Protein family:** LDOC1 family · **Domain:** RTL1/1-8/LDOC capsid-like (InterPro IPR032549; Pfam PF16297)

---

## Summary

Human **RTL6** (UniProt Q6ICC9; also known as **LDOC1L**, **SIRH3**, **MART6**) is a 239-amino-acid, ~26 kDa protein that is **not** an enzyme, a transporter, or a classical cell-surface receptor. It is one of a set of eutherian-specific, **"domesticated" (co-opted) genes derived from an ancient retrovirus/LTR retrotransposon**. RTL6 retains a single retroviral **Gag/capsid-like domain** (Pfam PF16297; InterPro IPR032549) and belongs to the LDOC1 family, but it is a neofunctionalized retrogene — it does not encode an active mobile element. Gene-symbol verification confirms the target: the symbol "RTL6", the human organism, the LDOC1 family assignment, and the RTL1-8/LDOC capsid-like domain are all mutually consistent with the published literature on RTL6/SIRH3.

The **primary, experimentally established function** of RTL6 is as a **secreted microglial innate-immune effector in the central nervous system (CNS) that captures and mediates the removal/clearance of bacterial lipopolysaccharide (LPS)**, the major endotoxin of Gram-negative bacteria. This function was defined in the mouse ortholog (Irie et al., 2022; Ishino et al., 2023), where RTL6 is produced by microglia, released as extracellular "dots and granules" in the CNS, and shown by knockout analysis to act specifically against LPS. RTL6 is the **bacteria-directed member of a coordinated, non-redundant trio** of retrovirus-derived microglial defense genes: **RTL5 → viruses (double-stranded RNA)**, **RTL6 → bacteria (LPS)**, and **RTL9 → fungi (zymosan)**. These three genes represent the first demonstration that retrovirus-derived (Gag-domesticated) genes contribute to the eutherian innate immune system.

Mechanistically, RTL6 acts **extracellularly**. It lacks a classical N-terminal signal peptide and any transmembrane segment, yet is secreted — implying a **non-classical/unconventional secretion route**. Its structure comprises a high-confidence **N-terminal coiled-coil** (the historical basis of the "leucine zipper" alias) joined to a well-folded central **Gag/capsid-like core**, flanked by disordered termini (AlphaFold model, mean pLDDT 77.3). The protein is **strongly basic and arginine-rich** (26 Arg, net charge ≈ +13, predicted pI ≈ 11.7), which provides a direct electrostatic rationale for binding the anionic LPS molecule (and other anionic pathogen-associated patterns such as CpG DNA). By analogy with its paralog RTL9 — in which the C-terminal Gag-like region is essential for pathogen degradation — the Gag-like domain is inferred to be the functional effector module of RTL6. Important caveat: **direct human experimental data are still lacking**; human function is inferred from the well-conserved mouse ortholog and from sequence/structure analysis.

---

## Key Findings

### Finding 1 — RTL6 is a domesticated retroviral Gag gene, not an active retrotransposon

RTL6 is one of at least **11 Mar/Mart (RTL/SIRH) genes** in eutherian mammals that are derived from an ancient LTR retrovirus or retrotransposon and have been **neofunctionalized** — that is, exapted ("domesticated") for new host functions. These genes retain the retroviral **Gag/capsid-like** coding region but do not encode functional, mobile retrotransposons. UniProt annotates Q6ICC9 (RTL6_HUMAN, 239 aa, ~26 kDa) with a single retrotransposon Gag/capsid-like domain (**Pfam PF16297 "RTL1-8_LDOC"**; **InterPro IPR032549 "RTL1/1-8/LDOC_capsid-like"**) and places it in the **LDOC1 family**. The gene-symbol equivalences are firmly established: **RTL6 = SIRH3 = MART6/MAR6 = LDOC1L**.

This identity and evolutionary derivation are directly supported by the literature. Irie et al. (2022) state that *"RTL6 (also known as SIRH3) are eutherian-specific genes presumably derived from a retrovirus"* [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/), which simultaneously confirms the RTL6=SIRH3 equivalence and the retroviral origin. The review by Kaneko-Ishino & Ishino (2023) places RTL6 within the broader family: *"Eutherians have 11 retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes presumably derived from a certain retrovirus"* [PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/). Together these establish RTL6 as a bona fide, correctly identified member of the domesticated Gag-derived gene family.

### Finding 2 — RTL6 is a microglial innate-immune effector acting against bacterial LPS

The central functional discovery about RTL6 comes from Irie et al. (2022), who generated an **RTL6-Venus knock-in fusion** mouse. The fusion protein is expressed in **microglia** — the resident immune cells of the brain — and is **secreted** as extracellular dots/granules in the CNS. RTL6 displays a **rapid response to pathogen-associated molecules**, including bacterial LPS, a double-stranded (ds) RNA analog, and non-methylated CpG DNA. Critically, **Rtl6 knockout mice** demonstrated that RTL6 acts specifically **as a factor against LPS** (bacterial endotoxin), whereas its paralog RTL5 acts against dsRNA. This work was described as the **first demonstration that retrovirus-derived genes function in the eutherian innate immune system**.

The supporting evidence is explicit. Irie et al. state that *"RTL5 and RTL6 are microglial genes with roles in the front line of innate brain immune response"* [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/); that *"These proteins display a rapid response to pathogens such as lipopolysaccharide (LPS), double-stranded (ds) RNA analog and non-methylated CpG DNA, acting both cooperatively and/or independently"*; and that *"RTL6 and RTL5 act as factors against LPS and dsRNA, respectively, in the brain."* The knockout-based assignment of RTL6 to the anti-LPS (anti-bacterial) role is the strongest single line of functional evidence in the current literature.

### Finding 3 — RTL6 is secreted and extracellular, and is a strongly basic protein consistent with LPS binding

Localization data place RTL6's site of action **outside the cell**. In the knock-in mice, RTL6-Venus *"appeared as extracellular dots and granules in the central nervous system"* [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/), indicating that RTL6 functions extracellularly rather than intracellularly.

An independent bioinformatic analysis of the human sequence (UniProt Q6ICC9, 239 aa) performed during this investigation quantified the protein's charge: **26 arginine + 5 lysine** residues versus **6 aspartate + 12 glutamate**, giving a **net charge of ≈ +13 at pH 7**, a **predicted isoelectric point of ≈ 11.7**, and an **arginine content of ~10.9%**. This confirms the published description of an "extremely basic protein" and provides a clear **biophysical rationale for binding anionic LPS** (and other anionic pathogen patterns such as CpG DNA). The original paper notes that the RTL5/RTL6 locus encodes *"a strongly acidic and extremely basic protein"* [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) — RTL6 being the extremely basic member, matching the computed pI ≈ 11.7. Electrostatic complementarity between RTL6's arginine-rich surface and the negatively charged phosphate/carboxylate groups of LPS is the most parsimonious model for substrate capture.

### Finding 4 — RTL6 removes/clears LPS as part of a three-gene (RTL5 / RTL6 / RTL9) microglial defense system

Subsequent work refined the mechanism to **removal/clearance** of the pathogen molecule and embedded RTL6 within a coordinated three-gene system. Ishino et al. (2023) state that RTL5 and RTL6 *"are microglial genes that play important roles in the brain's innate immunity against viruses and bacteria through their removal of double-stranded RNA and lipopolysaccharide, respectively"* [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/). This frames RTL6's action as **removal of LPS** — i.e., scavenging/clearance of the endotoxin — rather than signal transduction.

The same body of work establishes a **functional trio** of retrovirus-derived microglial genes, each tuned to a different class of pathogen: *"the importance of three retrovirus-derived microglial RTL genes as eutherian-specific constituents of the current brain innate immune system: RTL9, RTL5 and RTL6, responding to fungi, viruses and bacteria, respectively"* [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/). Mechanistic insight into the shared effector module comes from RTL9: *"in Rtl9 knockout mice expressing RTL9ΔC protein lacking the C-terminus retroviral GAG-like region, the zymosan degrading activity was lost"* [PMID: 37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/). This demonstrates that the **retroviral Gag-like region is the essential functional module** in this gene family — by direct analogy, RTL6's Gag-like domain is inferred to be its functional effector against LPS.

### Finding 5 — RTL6 lacks a classical signal peptide yet is secreted, and carries an N-terminal coiled-coil ("leucine zipper")

UniProt annotations for the human (Q6ICC9) and mouse (Q505G4) orthologs record **no signal peptide and no transmembrane segment**, but a **coiled-coil region at residues 29–69** and intrinsically disordered regions (82–106 and 214–239). The experimental finding that RTL6 is nonetheless secreted extracellularly as dots/granules in the CNS [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) implies that it reaches the extracellular space via a **non-classical / unconventional secretion pathway** (signal-peptide-independent export, potentially vesicle- or granule-mediated, consistent with the observed granular appearance).

The N-terminal coiled-coil accounts for the protein's historical alias, *"Leucine zipper protein down-regulated in cancer cells-like"* (**LDOC1L**) — a name predating the discovery of its immune function and reflecting only the predicted leucine-zipper-like coiled-coil, not a transcription-factor role. UniProt also notes that mouse Rtl6 is "widely expressed" at the tissue level, although the **functional protein is concentrated in microglia**, reconciling broad transcriptional detection with a focused physiological role.

### Finding 6 — AlphaFold structure and genomic context confirm the domain architecture and retrogene origin

The AlphaFold DB model for Q6ICC9 (v6, 239 residues; **mean pLDDT 77.3**, with 68.2% of residues at confident pLDDT > 70) reveals a clear **two-part architecture**:

| Region | Residues | Mean pLDDT | Interpretation |
|---|---|---|---|
| Disordered N-terminus | 1–28 | 61.9 | Flexible tail |
| **Coiled-coil** | 29–69 | **92.5** | Very high confidence; "leucine zipper" element |
| Internal loop | 82–106 | 58.9 | Disordered linker |
| **Gag/capsid-like core** | ~70–213 | **80.4** | Well-folded retroviral effector module |
| Disordered C-terminus | 214–239 | 53.0 | Flexible tail |

This structure — a high-confidence coiled-coil fused to a folded Gag/capsid-like core, flanked by disordered termini — matches the domain annotations precisely and visualizes the two functional elements (interaction/oligomerization coiled-coil + effector Gag core). Genomically, RTL6 (Ensembl **ENSG00000188636**, HGNC:13343) maps to **human chromosome 22 (~44.49 Mb, minus strand)**, is annotated **protein_coding**, and its coding sequence is contained in essentially a **single coding exon** (2-exon canonical transcript ENST00000341255). The intronless coding structure is the hallmark of a **retrotransposon/retrovirus-derived retrogene**, independently corroborating the evolutionary origin inferred from the Gag domain.

### Finding 7 — RTL5 and RTL6 cooperate in *trans*, across different chromosomes (not a gene cluster)

Although RTL5 and RTL6 are phylogenetically related and functionally cooperative, they are **not a syntenic gene cluster**. Ensembl coordinates determined in this analysis place **RTL6 = ENSG00000188636 on chromosome 22 (~44.49 Mb)** and its partner **RTL5 = ENSG00000242732 on chromosome X (~72.13 Mb)**. Other family members are likewise dispersed (RTL3, RTL4, RTL8A on chromosome X). Thus the RTL5/RTL6 (and RTL9) microglial innate-immune partners **act in *trans* at the protein level** — they are co-expressed in microglia and functionally coordinated, but encoded at distinct, non-adjacent genomic loci rather than arising from a single tandem duplication cluster.

---

## Mechanistic Model / Interpretation

The convergent lines of evidence support the following coherent model of RTL6 function:

```
            ANCIENT LTR RETROVIRUS / RETROTRANSPOSON
                          │  (domestication / exaptation
                          │   in the eutherian lineage)
                          ▼
        RTL6 / SIRH3 / LDOC1L  — single-exon retrogene, chr22
        (retains Gag/capsid-like domain; loses mobility)
                          │
                          ▼
        Expressed in MICROGLIA (brain-resident immune cells)
                          │
                          │  non-classical secretion
                          │  (no signal peptide)
                          ▼
     Released EXTRACELLULARLY as "dots and granules" in the CNS
                          │
                          ▼
  Strongly basic surface (net +13, pI ≈ 11.7, Arg-rich)
  binds anionic bacterial LPS  ──►  REMOVAL / CLEARANCE of LPS
                          │
                          ▼
        Protects the eutherian brain from Gram-negative
        bacterial endotoxin (innate immune defense)
```

RTL6 is best understood as a **secreted, Gag-derived pattern-scavenging effector** of the microglial innate immune system. It is not a signaling receptor (no transmembrane domain, no catalytic motif) but rather a **binding/clearance module**. Its arginine-rich, highly basic surface provides electrostatic complementarity to the anionic LPS molecule; the retroviral Gag-like core — shown to be the essential functional region in the paralog RTL9 — is inferred to drive the effector activity (capture and/or degradation), while the N-terminal coiled-coil likely mediates oligomerization or partner interactions.

RTL6 operates within a **division-of-labor defense system** of three domesticated Gag genes, each specialized for a pathogen class:

| Gene (aliases) | Chromosome | Target pathogen class | Molecular ligand | Evidence |
|---|---|---|---|---|
| **RTL5** (SIRH8) | chr X | Viruses | double-stranded RNA | Knockout + knock-in (mouse) |
| **RTL6** (SIRH3, LDOC1L) | chr 22 | **Bacteria** | **lipopolysaccharide (LPS)** | **Knockout + knock-in (mouse)** |
| **RTL9** (SIRH10) | — | Fungi | zymosan | Knockout; Gag C-terminus required |

These genes are co-opted retroviral capsid proteins that the eutherian lineage has repurposed into a **brain-specific innate immune surveillance network**, representing a striking example of molecular domestication contributing to mammalian immune evolution.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Strength |
|---|---|---|---|
| [36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) | *Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain* (Irie et al., 2022) | **Primary functional study.** Defines RTL6 as a secreted microglial gene acting against LPS; knock-in localization (extracellular dots/granules); knockout functional assignment; "extremely basic protein." | **Strong — primary experimental (mouse)** |
| [37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/) | *Retrovirus-Derived RTL...* (Ishino et al., 2023) | Frames RTL6's mechanism as **removal/clearance of LPS**; establishes the RTL9/RTL5/RTL6 trio (fungi/viruses/bacteria); shows Gag C-terminus is essential (RTL9). | **Strong — primary + synthesis** |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *Retrovirus-Derived RTL/SIRH: Their Diverse Roles in the Current Eutherian Developmental System and Contribution to Eutherian Evolution* (Kaneko-Ishino & Ishino, 2023) | **Authoritative review.** Places RTL6 among the 11 domesticated RTL/SIRH Gag genes; evolutionary and functional context. | **Strong — review** |

**How the evidence fits together:** The 2022 primary study (36162816) supplies the direct experimental backbone — microglial expression, extracellular secretion, and knockout-based assignment of RTL6 to the anti-LPS role. The 2023 study (37834332) refines the mechanism to *removal* of LPS and generalizes it into the three-gene defense system, while the RTL9 Gag-truncation experiment provides the strongest available clue that the Gag domain is the functional effector module — an inference that applies to RTL6 by homology. The 2023 review (37892118) supplies the evolutionary framing that confirms gene identity and places RTL6 among the 11 domesticated Gag-derived genes. Structural (AlphaFold) and genomic (Ensembl) analyses performed in this investigation independently corroborate the domain architecture, the basic/arginine-rich surface chemistry, and the intronless retrogene origin.

**No contradicting evidence** was found. All sources are mutually consistent, and all corroborate the gene-identity verification required at the outset. One note on citation metadata: the snippets drawn from PMID 37834332 were flagged as "mismatch" during automated verification (likely a stored-abstract formatting discrepancy), so claims attributed to that paper should be treated with slightly lower confidence than those from PMID 36162816, whose snippets were verified verbatim.

---

## Limitations and Knowledge Gaps

1. **No direct human experimental data.** Every functional result (microglial expression, secretion, anti-LPS activity) derives from the **mouse ortholog** (Q505G4). Human RTL6 function is inferred from strong sequence/structure conservation and family membership, but has not been directly demonstrated in human cells or tissue. This is the single most important caveat.

2. **Binding and clearance are not biochemically resolved.** The electrostatic LPS-binding model is strongly suggested by the +13 net charge and arginine-rich surface, but **no direct binding affinity (Kd), stoichiometry, or structural co-complex** with LPS has been reported. Whether RTL6 neutralizes, sequesters, traffics, or enzymatically processes LPS remains undefined.

3. **Secretion mechanism unknown.** RTL6 lacks a signal peptide yet is secreted. The specific **non-classical secretion route** (e.g., vesicular, granule-mediated, or exosomal) has not been characterized.

4. **Role of the Gag domain in RTL6 specifically is inferred, not proven.** The essential-functional-module evidence comes from **RTL9**, not RTL6. A domain-truncation experiment in RTL6 is lacking.

5. **Structure is predicted, not experimental.** The two-part architecture rests on an AlphaFold model (mean pLDDT 77.3), with low confidence in the disordered termini and internal loop. No experimental structure exists.

6. **Expression breadth vs. function.** Mouse Rtl6 is "widely expressed" transcriptionally, yet functional protein is concentrated in microglia; the significance (if any) of non-microglial expression is unexplored.

---

## Proposed Follow-up Experiments / Actions

1. **Direct LPS-binding biochemistry.** Express and purify recombinant human RTL6 (Q6ICC9) and measure LPS binding by surface plasmon resonance / isothermal titration calorimetry; determine Kd and stoichiometry. Test the electrostatic hypothesis by mutating clusters of surface arginines and measuring loss of binding.

2. **Human-cell validation.** Confirm RTL6 expression and secretion in **human microglia** (e.g., iPSC-derived microglia or ex vivo microglia) and test anti-LPS activity directly in a human system, closing the mouse-to-human inference gap.

3. **Gag-domain truncation in RTL6.** Generate an RTL6ΔGag (or RTL6 with the Gag core deleted/mutated) construct, mirroring the RTL9ΔC experiment, to prove that the Gag-like domain is the functional effector for LPS removal.

4. **Secretion-route dissection.** Use pharmacological inhibitors and markers of conventional vs. unconventional secretion to map how signal-peptide-less RTL6 reaches the extracellular space; test for exosome/granule association.

5. **Structural determination of the RTL6–LPS complex.** Pursue cryo-EM or X-ray crystallography of RTL6 alone and with LPS to validate the AlphaFold model and reveal the binding interface.

6. **In vivo bacterial challenge.** Test whether Rtl6-knockout mice have increased susceptibility to Gram-negative bacterial / LPS challenge in the CNS, and whether human RTL6 can rescue the phenotype, establishing physiological relevance and cross-species conservation of function.

---

## Conclusion

Human RTL6 (LDOC1L / SIRH3 / MART6; UniProt Q6ICC9) is a **domesticated retroviral Gag/capsid-like protein** — not an enzyme, transporter, or classical receptor — whose **primary function is as a secreted microglial innate-immune effector that binds and mediates the removal/clearance of bacterial LPS in the eutherian brain**. It acts **extracellularly**, released by microglia as dots/granules via non-classical (signal-peptide-independent) secretion, using a strongly basic, arginine-rich surface for electrostatic capture of anionic endotoxin and a retroviral Gag-like core as the effector module. RTL6 is the **bacteria-directed member of a coordinated, *trans*-acting trio** of domesticated Gag genes (RTL5 → viruses/dsRNA; RTL6 → bacteria/LPS; RTL9 → fungi/zymosan). Direct human experimental data remain lacking, so the human function is inferred from the well-conserved mouse ortholog and from sequence, structure, and evolutionary analysis.


## Artifacts

- [OpenScientist final report](RTL6-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL6-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36162816
2. PMID:37892118
3. PMID:37834332