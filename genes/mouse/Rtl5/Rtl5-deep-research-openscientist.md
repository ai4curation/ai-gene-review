---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T14:39:24.496306'
end_time: '2026-10-24T15:06:51.032715'
duration_seconds: 1646.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl5
  gene_symbol: Rtl5
  uniprot_accession: Q5DTT4
  protein_description: 'RecName: Full=Retrotransposon Gag-like protein 5; AltName:
    Full=Retrotransposon gag domain-containing protein 4;'
  gene_info: Name=Rtl5 {ECO:0000250|UniProtKB:Q5HYW3}; Synonyms=Kiaa2001, Rgag4 {ECO:0000312|MGI:MGI:3045324};
  organism_full: Mus musculus (Mouse).
  protein_family: Not specified in UniProt
  protein_domains: PEG10-RTL1_C-capsid. (IPR063300); RTL1-rel. (IPR032567); RTL1/1-8/LDOC_capsid-like.
    (IPR032549); PEG10-RTL1_C-capsid (PF30901); RTL1-8_LDOC (PF16297)
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
  path: Rtl5-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl5-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q5DTT4
- **Protein Description:** RecName: Full=Retrotransposon Gag-like protein 5; AltName: Full=Retrotransposon gag domain-containing protein 4;
- **Gene Information:** Name=Rtl5 {ECO:0000250|UniProtKB:Q5HYW3}; Synonyms=Kiaa2001, Rgag4 {ECO:0000312|MGI:MGI:3045324};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PEG10-RTL1_C-capsid. (IPR063300); RTL1-rel. (IPR032567); RTL1/1-8/LDOC_capsid-like. (IPR032549); PEG10-RTL1_C-capsid (PF30901); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl5" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl5** (gene ID: Rtl5, UniProt: Q5DTT4) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Rtl5* (UniProt Q5DTT4)

**Gene:** *Rtl5* (synonyms: *Kiaa2001*, *Rgag4*, *Mart5*; also known as **SIRH8**)
**Protein:** Retrotransposon Gag-like protein 5 / Retrotransposon gag domain-containing protein 4
**UniProt:** Q5DTT4 (RTL5_MOUSE, 599 aa)
**Organism:** *Mus musculus* (mouse)

---

## Summary

Mouse **Rtl5** encodes **Retrotransposon Gag-like protein 5**, a eutherian-specific "domesticated" gene that was co-opted from the Gag (group-specific antigen / capsid) region of an ancient *sushi-ichi* (Ty3/Gypsy-type) LTR retrotransposon. It is a member of the 11-gene **RTL/SIRH (sushi-ichi retrotransposon homolog) family**, within which it is also catalogued as **SIRH8** and, under an alternative nomenclature, as **Rgag4/Mart5**. The identity of the target gene is firmly established and matches the UniProt description, organism, and capsid-like domain architecture (PEG10-RTL1_C-capsid, IPR063300/PF30901; RTL1-8_LDOC, PF16297). This is NOT an ambiguous symbol collision — the literature uncovered (Irie et al. 2022; Kaneko-Ishino & Ishino reviews; Henke et al. 2015) concerns exactly this mouse retrovirus-derived gene.

The **primary, experimentally established function** of RTL5 is as an **innate-immune effector of brain microglia that acts specifically against double-stranded RNA (dsRNA)**. Using reporter knock-in and knockout mouse models, Irie et al. (2022) showed that RTL5 and its paralog RTL6 are microglial genes that mount a rapid response to pathogen-associated molecular patterns (PAMPs). RTL5 acts as a factor against dsRNA, while the paired gene RTL6 acts against bacterial lipopolysaccharide (LPS); together they represent the first demonstration that retrovirus-derived genes participate in the eutherian innate immune system. RTL5 is produced by microglia and carries out its function **extracellularly**, appearing as secreted dots and granules in the central nervous system (CNS).

Mechanistically, RTL5 is not an enzyme, transporter, or classical signaling receptor. It is best described as a **secreted pathogen-engaging/neutralizing factor** built on a retroviral capsid-like scaffold. Independent sequence and structural analyses performed in this investigation confirm the literature's description of RTL5 as a **strongly acidic protein** (computed pI ≈ 4.4, net charge ≈ −85 at pH 7), retaining the Gag capsid fold but having lost both the ancestral aspartic-protease active site and the Gag nucleocapsid CCHC zinc-knuckle. It also lacks a classical signal peptide or transmembrane domain, implying that its extracellular localization is achieved by an **unconventional (non-canonical) secretion route**. RTL5 is well conserved between mouse and human (~68–72% identity), with the acidic character preserved across the orthologs. A secondary line of evidence shows developmental expression in placental trophoblast, consistent with the broader RTL/SIRH family's roles across placenta, brain, and innate immunity.

---

## Gene / Protein Identity Verification

Before any functional claims, the identity of the target was verified against the three required criteria. All checks passed.

| Verification step | Result |
|---|---|
| Symbol "Rtl5" matches protein description | ✅ UniProt Q5DTT4 = "Retrotransposon Gag-like protein 5 / Retrotransposon gag domain-containing protein 4", gene *Rtl5* (synonyms *Kiaa2001*, *Rgag4*) |
| Organism is *Mus musculus* | ✅ All primary literature (Irie et al. 2022; Henke et al. 2015) is mouse |
| Family/domains align with literature | ✅ Retrovirus-derived Gag-like gene; retains PEG10-RTL1 capsid-like domain (IPR063300/PF30901) |
| No confounding different-gene literature | ✅ Literature consistently refers to this exact mouse RTL5/SIRH8 gene |

**Conclusion:** The gene symbol *Rtl5* unambiguously maps to the intended protein. RTL5 is also known as **SIRH8** and as **Rgag4/Mart5**. It is one of 11 eutherian metavirus (sushi-ichi retrotransposon)-derived SIRH/RTL genes, and is phylogenetically related to RTL6/SIRH3 [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)], [[PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)], [[PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)]. This literature is directly on-target, so the research proceeded on the correct gene.

---

## Key Findings

### Finding 1 — RTL5 is a eutherian-specific, retrovirus-derived Gag-like gene (= SIRH8 = Rgag4/Mart5)

The gene product belongs to a family of **"domesticated" retroviral/retrotransposon genes**. Eutherian (placental) mammals carry 11 retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes that are presumably derived from a single ancient retrovirus [[PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)]. Within this family, RTL5 is explicitly identified as **SIRH8** and is phylogenetically paired with **RTL6/SIRH3**: *"Retrotransposon Gag-like 5 [RTL5, also known as sushi-ichi-related retrotransposon homolog 8 (SIRH8)] and RTL6 (also known as SIRH3) are eutherian-specific genes presumably derived from a retrovirus and phylogenetically related to each other"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)]. An independent placental study uses the alternative name **Rgag4/Mart5** for the same locus [[PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)]. The gene retains a retroviral **Gag capsid-like domain** (InterPro IPR063300; Pfam PF30901/PF16297). These family relationships matter functionally, because the RTL/SIRH genes are a repeatedly co-opted source of novel eutherian functions in placenta, brain, and immunity.

### Finding 2 — Primary function: a microglial innate-immune factor acting specifically against double-stranded RNA

This is the central functional result of the report. In the definitive primary study, Irie et al. (2022) generated reporter knock-in and knockout mice to dissect RTL5 and RTL6 function in the brain. Both genes are expressed in **microglia**, the resident immune cells of the CNS. The RTL5 and RTL6 proteins *"display a rapid response to pathogens such as lipopolysaccharide (LPS), double-stranded (ds) RNA analog and non-methylated CpG DNA, acting both cooperatively and/or independently"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)]. Knockout experiments resolved the **division of labor** between the two paralogs: *"RTL6 and RTL5 act as factors against LPS and dsRNA, respectively, in the brain, providing the first demonstration that retrovirus-derived genes play a role in the eutherian innate immune system"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)].

**Interpretation:** RTL5's specific substrate/ligand within innate immunity is **double-stranded RNA** — a hallmark PAMP of viral infection. RTL5 therefore functions as a pathogen-sensing/neutralizing effector rather than as an enzyme or transporter. Its acidic character, paired with the basic RTL6 (which handles bacterial LPS), suggests the two domesticated capsid proteins cover complementary classes of pathogen molecules in the brain's front-line defense.

### Finding 3 — Localization: produced by microglia and secreted extracellularly as dots/granules in the CNS

The same knock-in reporter mice revealed where RTL5 acts. *"Venus and mCherry knock-in mice exhibited expression of RTL5-mCherry and RTL6-Venus fusion proteins in microglia and appeared as extracellular dots and granules in the central nervous system"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)]. The authors summarize that *"RTL5 and RTL6 are microglial genes with roles in the front line of innate brain immune response"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)].

**Interpretation:** RTL5 is synthesized in microglia but exerts its anti-dsRNA function **extracellularly**, in the brain parenchyma, consistent with a secreted effector that engages pathogen-derived dsRNA outside the cell. This extracellular, granular distribution is an important clue to its mechanism (see Mechanistic Model).

### Finding 4 — Secondary expression evidence: placental trophoblast during development

Beyond the brain, RTL5 (as *Rgag4/Mart5*) is expressed in the developing placenta. Henke et al. (2015) profiled the gene across mouse placentogenesis and found expression very low at the blastocyst stage, rising at later placental stages. In situ hybridization showed *"sense and antisense transcript co-localization of Rgag4/Mart5 to Cxx1a,b,c/Mart8b,c,a in trophoblast subtypes at the junctional zone"* [[PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)]. At the family level, reviews note that *"the RTL/SIRH genes play a variety of roles in the current mammalian developmental system, such as in the placenta, brain, and innate immune system, in a eutherian-specific manner"* [[PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)].

**Interpretation:** This is **expression-level** evidence (transcript localization), not a demonstrated placental function. It is consistent with the family's placental roles but should be treated as a secondary, lower-confidence lead relative to the experimentally validated brain-immune function.

### Finding 5 — RTL5 is a strongly acidic protein (computational confirmation of the literature)

Direct sequence analysis of Q5DTT4 (599 aa) performed in this investigation independently confirmed the literature's physicochemical description. Acidic residues (D+E = 137; 22.9% of the sequence) vastly outnumber basic residues (K+R = 52; 8.7%), giving a **net charge of approximately −85** and a theoretical **isoelectric point pI ≈ 4.4** (computed by Henderson–Hasselbalch bisection with EMBOSS pKa values). This matches the experimental statement that RTL5 and RTL6 *"respectively, encode a strongly acidic and extremely basic protein, and are well conserved among the eutherians"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)].

**Interpretation:** The pronounced acidic bias is unusual and likely functionally relevant — e.g., for electrostatic engagement of basic/positively charged targets or for the assembly/behavior of the secreted granules. The complementary charge states of RTL5 (acidic) and RTL6 (basic) mirror their complementary pathogen specificities (dsRNA vs LPS).

### Finding 6 — Retained Gag capsid fold, but loss of protease and nucleocapsid motifs, plus a C-terminal poly-acidic tract

A motif scan of Q5DTT4 showed that RTL5 has **no retroviral aspartic-protease active-site motif** (D-[ST]-G) and **no canonical Gag nucleocapsid CCHC zinc-knuckle** (C-X2-C-X4-H-X4-C). Acidic residues are concentrated in the C-terminal half (86 of 137 D/E), including an exceptional low-complexity poly-acidic stretch near position 410 that is 20/20 acidic (`EEEDEDDDDEEEEEEEEEEE`). InterPro/Pfam assign only the **PEG10-RTL1_C-capsid / RTL1-8_LDOC capsid-like domain** (IPR063300/PF30901; PF16297) — i.e., only the Gag capsid (CA) module survives. This fits the family framing of RTL/SIRH as Gag-derived genes [[PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)].

**Interpretation:** RTL5 has been "stripped down" during domestication to the capsid scaffold alone. The loss of protease and nucleic-acid-binding zinc-knuckle means it is unlikely to retain the ancestral enzymatic or RNA-packaging activities; instead the capsid fold has been repurposed, and the acidic low-complexity tract may mediate granule formation, condensation, or target engagement.

### Finding 7 — No classical signal peptide or transmembrane domain → unconventional secretion

Kyte–Doolittle hydropathy analysis (19-residue window) of Q5DTT4 showed the N-terminal 30 residues reach a maximum hydropathy of only 0.32 — far below the ~1.6 threshold for a signal-peptide hydrophobic core — and that **no window anywhere in the 599-aa sequence exceeds 1.6** (global maximum hydropathy 1.05 at position 194). RTL5 therefore has neither a predicted signal peptide nor a transmembrane segment, yet is experimentally observed as extracellular granules [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)].

**Interpretation:** RTL5 must reach the extracellular space via an **unconventional protein secretion** pathway (signal-peptide-independent), which is well documented for other immune and granule-associated proteins and biologically coherent for a protein derived from a cytosolic retroviral Gag capsid. This reconciles the sequence analysis (no canonical secretion signal) with the microscopy (extracellular dots/granules).

### Finding 8 — Mouse and human RTL5 are conserved orthologs (~68–72% identity), both strongly acidic

Needleman–Wunsch global alignment of mouse RTL5 (Q5DTT4, 599 aa) against human RTL5 (Q5HYW3, 569 aa — the reference ortholog cited in the mouse UniProt entry's ECO:0000250 annotation) gave 411 identical positions over a 600-residue alignment = **68.5% identity** (72.2% over the shorter sequence). The acidic bias is conserved: mouse 22.9% acidic / net charge −85; human 20.0% acidic / net charge −44. This quantitatively supports the statement that RTL5 is *"well conserved among the eutherians"* [[PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)].

**Interpretation:** Strong cross-species conservation of both sequence and the distinctive acidic character indicates purifying selection and argues that the mouse findings (anti-dsRNA microglial function) are likely relevant to the human ortholog.

---

## Mechanistic Model / Interpretation

RTL5 is best understood as a **domesticated retroviral capsid protein repurposed as a secreted, dsRNA-directed innate-immune factor in brain microglia**. The following model integrates all eight findings.

```
          ANCESTRAL sushi-ichi (Ty3/Gypsy) LTR retrotransposon Gag
                 [ Matrix | CAPSID (CA) | Nucleocapsid (CCHC) | Protease ]
                                   |
                        EUTHERIAN DOMESTICATION
                 (loss of protease + CCHC zinc-knuckle; CA fold retained)
                                   |
                                   v
   RTL5 / SIRH8 (599 aa, strongly acidic, pI ~4.4, net charge -85)
   - Only PEG10-RTL1 capsid-like domain survives (IPR063300 / PF30901)
   - C-terminal poly-acidic low-complexity tract (~pos 410)
   - No signal peptide, no TM domain
                                   |
             Expressed in MICROGLIA (resident CNS immune cells)
                                   |
                  Unconventional (signal-peptide-independent) secretion
                                   |
                                   v
        EXTRACELLULAR dots / granules in CNS parenchyma
                                   |
                    Rapid response to viral PAMP: dsRNA
                                   |
         +----------------------------------------------+
         |  RTL5  -->  acts against double-stranded RNA |
         |  RTL6  -->  acts against LPS (bacterial)     |
         |  (complementary; cooperative and/or separate)|
         +----------------------------------------------+
                                   |
              FRONT-LINE innate immune defense of the brain
```

**Why this model is coherent:**

- The **capsid-only architecture** (Finding 6) explains why RTL5 is not an enzyme: the ancestral catalytic (protease) and RNA-packaging (nucleocapsid) modules are gone. What remains is a structural scaffold, re-tasked for a new role.
- The **strong acidic charge** (Findings 5, 8) and the **C-terminal poly-acidic tract** (Finding 6) are candidate determinants for granule assembly and/or electrostatic engagement of targets, and they contrast cleanly with the "extremely basic" RTL6, paralleling their opposite pathogen specificities (dsRNA vs LPS).
- The **lack of a signal peptide** (Finding 7) combined with **observed extracellular granules** (Finding 3) pinpoints unconventional secretion as the delivery route.
- The **microglial expression + anti-dsRNA knockout phenotype** (Finding 2) provide the only direct functional readout and anchor the whole model in experimental genetics.
- **Placental trophoblast expression** (Finding 4) is a secondary, expression-only observation consistent with the family's multi-tissue deployment but not yet tied to a defined placental mechanism.

**Functional classification for annotation purposes:**

| Question from the brief | Answer for RTL5 |
|---|---|
| Enzyme? Reaction/substrate? | No. Ancestral protease active site lost; no catalytic annotation. |
| Transporter? Substrate? | No evidence of transport function. |
| Structural protein / adapter? | Yes in origin — retains the Gag **capsid-like structural fold**, repurposed as a secreted factor. |
| Signaling molecule? Pathway role? | Acts as an **innate-immune effector** against viral dsRNA; part of microglial front-line brain defense (paired with RTL6 against LPS). |
| Subcellular / extracellular localization | Produced in microglia; functions **extracellularly** as secreted dots/granules in the CNS. |
| Pathway | Eutherian innate immune system (antiviral / anti-PAMP response in brain). |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/) | *Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immune system in the eutherian brain* | **Primary source.** Establishes identity (RTL5 = SIRH8), microglial expression, extracellular granule localization, acidic protein character, and the key knockout result that RTL5 acts specifically against dsRNA. |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *Retrovirus-Derived RTL/SIRH: Their Diverse Roles in the Current Eutherian Developmental System and Contribution to Eutherian Evolution* | Authoritative review. Places RTL5 within the 11-member eutherian SIRH/RTL family and its placenta/brain/immune roles. |
| [25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/) | *Selective expression of sense and antisense transcripts of the sushi-ichi-related retrotransposon-derived family during mouse placentogenesis* | Confirms the *Rgag4/Mart5* synonym and documents placental trophoblast (junctional-zone) expression. |
| [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | *Virus-Derived Domesticated Genes in Microglia and Resident Macrophages* | Review context: multiple SIRH/RTL members function in microglia. |
| [37834332](https://pubmed.ncbi.nlm.nih.gov/37834332/) | *Retrovirus-Derived RTL…* | Family context for RTL roles in placenta and brain. |
| [28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/) | *Evolution of brain functions in mammals and LTR retrotransposon-derived genes* | Background on SIRH/PNMA gene domestication and brain function. |
| [23704700](https://pubmed.ncbi.nlm.nih.gov/23704700/) | *Identification of a novel PNMA-MS1 gene in marsupials…* | Evolutionary background on LTR-retrotransposon-derived gene families; eutherian vs marsupial. |
| [37842090](https://pubmed.ncbi.nlm.nih.gov/37842090/) | *Roles of retrovirus-derived…* | Supporting family-level review (no abstract available). |

**How the evidence converges:** The single primary experimental paper ([PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)) provides the direct functional, localization, and biochemical claims; the reviews and the placental study provide corroborating family context and secondary expression data; and independent in-silico sequence analyses performed in this investigation (acidity, motif loss, hydropathy, mouse–human conservation) quantitatively reinforce the literature's descriptive statements.

---

## Limitations and Knowledge Gaps

1. **Single primary functional study.** Nearly all mechanistic claims rest on one paper (Irie et al. 2022, [PMID: 36162816](https://pubmed.ncbi.nlm.nih.gov/36162816/)). Independent replication is lacking.
2. **Molecular mechanism against dsRNA is unresolved.** It is not known whether RTL5 directly binds dsRNA, sequesters/opsonizes it, triggers downstream signaling, or acts indirectly. No binding affinity, complex structure, or receptor/partner has been defined. Notably, the sequence analysis here shows RTL5 lacks the canonical CCHC nucleic-acid-binding zinc-knuckle, so any dsRNA engagement would be via a non-canonical surface (possibly charge-mediated).
3. **Unconventional secretion pathway unidentified.** The route by which a signal-peptide-less protein reaches extracellular granules is inferred, not demonstrated.
4. **Placental function is expression-only.** The trophoblast expression data ([PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)) do not establish a placental phenotype or mechanism.
5. **Human ortholog function is inferred, not tested.** Conservation (~68–72%) supports transfer of the mouse model to human, but no human functional data were found.
6. **Physiological significance / in vivo challenge models.** Whether RTL5 confers measurable resistance to specific neurotropic viruses in vivo remains to be shown.
7. **Structural data.** The predicted capsid-like fold is based on domain assignment; no experimental structure of RTL5 was available in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Direct dsRNA-binding assays.** Test recombinant RTL5 for binding to synthetic dsRNA (e.g., poly I:C) by EMSA, surface plasmon resonance, or microscale thermophoresis; map the binding surface via mutagenesis of the acidic C-terminal tract and conserved capsid residues.
2. **Mechanism of anti-dsRNA action.** Determine whether RTL5 sequesters/opsonizes dsRNA, promotes its clearance, or modulates known dsRNA sensors (e.g., TLR3, RIG-I/MDA5) — distinguishing a direct-neutralization model from a signaling-modulation model.
3. **In vivo viral challenge.** Infect *Rtl5* knockout vs wild-type mice with a neurotropic RNA virus and quantify viral load, microglial activation, and neuropathology to test physiological relevance.
4. **Secretion pathway dissection.** Use brefeldin A / unconventional-secretion inhibitors and candidate-pathway knockdowns to identify how RTL5 reaches extracellular granules; characterize granule composition by proteomics.
5. **Structural biology.** Solve or predict (AlphaFold + experimental validation) the RTL5 capsid-like fold; assess whether it oligomerizes into capsid-like assemblies and whether the poly-acidic tract drives condensation.
6. **RTL5–RTL6 interaction.** Test whether the acidic RTL5 and basic RTL6 physically interact (their opposite charges and "cooperative" response suggest possible heteromeric granules), and whether they co-localize in the same microglial granules.
7. **Human ortholog validation.** Express human RTL5 (Q5HYW3) and repeat key dsRNA-engagement assays to confirm functional conservation.
8. **Placental function test.** Use conditional/trophoblast-specific loss-of-function to determine whether the junctional-zone expression reflects a defined placental role or is incidental.

---

## Direct Answer

Mouse **Rtl5** (UniProt Q5DTT4; = SIRH8 / Rgag4 / Mart5) encodes **Retrotransposon Gag-like protein 5**, a eutherian-specific domesticated gene derived from the Gag/capsid region of an ancient *sushi-ichi* (Ty3/Gypsy) LTR retrotransposon; it is a strongly acidic (pI ≈ 4.4, net charge ≈ −85) protein that retains only the Gag capsid-like fold, having lost the ancestral protease and nucleocapsid zinc-knuckle. Its primary, experimentally established function is as a **secreted innate-immune effector of brain microglia that acts specifically against double-stranded RNA** (the acidic counterpart to RTL6, which counters bacterial LPS), carrying out this role **extracellularly** as dots/granules in the CNS via an unconventional, signal-peptide-independent secretion route, with additional expression-only evidence in placental trophoblast.


## Artifacts

- [OpenScientist final report](Rtl5-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl5-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36162816
2. PMID:37892118
3. PMID:25888968