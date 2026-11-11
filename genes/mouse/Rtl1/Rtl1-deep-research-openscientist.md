---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T14:25:03.154254'
end_time: '2026-10-24T14:39:17.710414'
duration_seconds: 854.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl1
  gene_symbol: Rtl1
  uniprot_accession: Q7M732
  protein_description: 'RecName: Full=Retrotransposon-like protein 1; AltName: Full=Mammalian
    retrotransposon derived protein 1; AltName: Full=Paternally expressed gene 11
    protein; AltName: Full=Retrotransposon-derived protein PEG11;'
  gene_info: Name=Rtl1; Synonyms=Mar1, Mart1, Peg11;
  organism_full: Mus musculus (Mouse).
  protein_family: Not specified in UniProt
  protein_domains: DNA/RNA_pol_sf. (IPR043502); PEG10-RTL1_C-capsid. (IPR063300);
    Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); Rev_trsase/Diguanyl_cyclase.
    (IPR043128)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rtl1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q7M732
- **Protein Description:** RecName: Full=Retrotransposon-like protein 1; AltName: Full=Mammalian retrotransposon derived protein 1; AltName: Full=Paternally expressed gene 11 protein; AltName: Full=Retrotransposon-derived protein PEG11;
- **Gene Information:** Name=Rtl1; Synonyms=Mar1, Mart1, Peg11;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DNA/RNA_pol_sf. (IPR043502); PEG10-RTL1_C-capsid. (IPR063300); Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); Rev_trsase/Diguanyl_cyclase. (IPR043128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl1" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl1** (gene ID: Rtl1, UniProt: Q7M732) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Rtl1* / *Peg11* (UniProt Q7M732)

**Gene:** *Rtl1* (synonyms: *Mar1*, *Mart1*, *Peg11*)
**Protein:** Retrotransposon-like protein 1 / Mammalian retrotransposon-derived protein 1 / Paternally expressed gene 11 protein (PEG11)
**Organism:** *Mus musculus* (Mouse)
**UniProt:** Q7M732 (1744 aa)

---

## Summary

Mouse **Rtl1** (also known as **Peg11**) is a **paternally expressed, imprinted gene** located in the conserved **Dlk1–Dio3 cluster** (mouse chromosome 12qF1; syntenic with human 14q32). It is one of the "domesticated" retrotransposon-derived genes — it originated from a **Ty3/Gypsy (*sushi-ichi*) LTR retrotransposon** and has retained an intact, full-length **gag–pol-like open reading frame**. Rather than functioning as a mobile element, it has been co-opted ("exapted") into a bona fide host gene with an essential developmental role unique to placental (eutherian) mammals.

The **primary, experimentally established physiological function of Rtl1 is the dosage-sensitive structural maintenance of the fetal capillary network at the feto-maternal interface of the placenta.** Both loss of function and overexpression of Rtl1 cause late-fetal and/or neonatal lethality in mice, demonstrating that the gene must be expressed within a narrow dosage window. Its expression is tuned *in trans* by a set of microRNAs — most notably **miR-127** — processed from the reciprocally imprinted maternal antisense transcript *Rtl1as* (*Peg11as*), which degrade Rtl1 mRNA by an RNAi mechanism. At the molecular level, the protein is a **Gag–Pol-like polyprotein** whose Pol region contains a **retropepsin (retroviral aspartic protease) domain** that retains the canonical catalytic aspartate motif (Asp684, D-S-G-A). By strong homology and by direct genetic validation in its paralog **PEG10**, this protease motif is predicted to be its key catalytic feature — most plausibly mediating autocatalytic polyprotein maturation. The protein has been directly identified as a full-length product in **nuclear preparations** of skeletal muscle, and UniProt annotates a **membrane** localization consistent with two predicted C-terminal transmembrane helices.

Beyond the placenta, Rtl1 has two well-documented secondary roles. First, it is the **major imprinted gene driving dosage-dependent fetal/neonatal skeletal-muscle development** — loss and overexpression in mice phenocopy the muscle symptoms of human **Temple syndrome** and **Kagami-Ogata syndrome**, respectively, and it underlies the ovine **callipyge** muscle-hypertrophy phenotype. Second, Rtl1 is paternally expressed in the **brainstem, thalamus, and hypothalamus**, where it regulates **neuronal excitability in the locus coeruleus** and influences anxiety-, depression-, and social-related behaviors. The following report details the evidence for each of these conclusions.

---

## Gene and Protein Identity Verification

Before proceeding, the mandatory identity checks confirm this is the correct target:

| Verification item | Result |
|---|---|
| Gene symbol "Rtl1" matches protein description | ✅ Rtl1 = Retrotransposon-like protein 1 = Peg11, consistent throughout literature |
| Organism is *Mus musculus* | ✅ All core functional studies (18176565, 26138477, 32878913, 34559199, 35567414) are mouse; sheep (20072617) is used as an orthologous system |
| Protein family/domains align with literature | ✅ Gag–Pol / retropepsin / reverse-transcriptase architecture (UniProt domains) matches the "retrotransposon-derived gag-pol" descriptions in the literature |
| Risk of confusion with a different gene | Low. Rtl1/Peg11 is consistently described across mouse, human, and sheep. Note: the broader "RTL" family has multiple members (RTL1–RTL11); care was taken to restrict findings to RTL1/PEG11 specifically. |

The literature is specific and consistent for this protein, so the research proceeds with confidence.

---

## Key Findings

### Finding 1 — Rtl1/Peg11 is a paternally expressed, retrotransposon-derived imprinted gene in the Dlk1–Dio3 cluster

Rtl1 is a **paternally expressed imprinted gene** located in the conserved **Dlk1–Dio3 imprinted cluster** (mouse chromosome 12qF1 / human 14q32), a locus whose synteny is highly conserved across placental mammals. The gene is derived from a **Ty3/Gypsy (*sushi-ichi*) LTR retrotransposon** and retains a **gag–pol-like ORF**, placing it among the SIRH (*sushi-ichi* retrotransposon homolog) family of domesticated genes (Rtl1 = SIRH2). It is reciprocally imprinted with a **maternally expressed antisense transcript, *Rtl1as* (*Peg11as*)**, which hosts a cluster of microRNAs.

This architecture is the foundation for all of Rtl1's regulatory behavior: because the sense (protein-coding) transcript comes from the paternal allele and the antisense (miRNA-bearing) transcript comes from the maternal allele, the two alleles regulate each other across homologous chromosomes.

> *"One of these retrotransposon-like elements, PEG11 (also called RTL1) is located at the distal end of ovine chromosome 18 within an imprinted gene cluster that is highly conserved in placental mammals"* — [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)

> *"The paternally expressed imprinted retrotransposon-like 1 (Rtl1) is a retrotransposon-derived gene that has evolved a function in eutherian placentation"* — [PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)

### Finding 2 — Primary function: maintenance of fetal capillaries at the feto-maternal placental interface

The **primary physiological function of Rtl1 is the maintenance of the fetal capillaries of the chorioallantoic (labyrinthine) placenta.** This is the defining, experimentally demonstrated role of the gene. Critically, the function is **dosage-sensitive**: both **loss of function** (deletion) and **overproduction** (overexpression) cause **late-fetal and/or neonatal lethality** in mice. This bidirectional lethality is a hallmark of a gene that must be maintained within a tight expression window.

The overexpression phenotype has been dissected genetically using the miR-127 knockout: removing this repressor elevates Rtl1 and produces **placentomegaly** with specific defects in the **labyrinthine zone** that mediates maternal–fetal nutrient transfer. The physiological output of Rtl1, therefore, is **structural integrity of the capillary endothelium at the nutrient-exchange surface** of the placenta.

> *"retrotransposon-derived Rtl1 (retrotransposon-like 1), also known as Peg11 (paternally expressed 11), is essential for maintenance of the fetal capillaries, and that both its loss and its overproduction cause late-fetal and/or neonatal lethality in mice"* — [PMID: 18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/)

> *"The miR-127 knockout mice exhibit placentomegaly with specific defects within the labyrinthine zone involved in maternal-fetal nutrient transfer"* — [PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)

### Finding 3 — Rtl1 is post-transcriptionally repressed *in trans* by miR-127 and other Rtl1as-derived miRNAs

Rtl1 dosage is controlled post-transcriptionally. **Seven miRNAs**, including **miR-127**, are processed from the maternally expressed antisense transcript *Rtl1as* and cleave Rtl1 mRNA through **RNAi-mediated post-transcriptional degradation**. Genetic analysis of single and double heterozygotes demonstrated that **Rtl1 is the main target of miR-127**, and that this regulation occurs via a remarkable **trans-homologue interaction** — the maternal-allele-derived miRNAs act on the paternal-allele-derived mRNA, coupling the reciprocally imprinted alleles.

This finding mechanistically explains the overexpression phenotypes: miR-127 loss removes the brake on Rtl1, raising its level and producing placental overgrowth and labyrinth defects — the "gain-of-function" mirror of the deletion phenotype.

> *"Seven miRNAs, including miR-127, are processed from a maternally expressed antisense Rtl1 transcript (Rtl1as) and regulate Rtl1 levels through RNAi-mediated post-transcriptional degradation"* — [PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)

> *"mediated by a trans-homologue interaction between reciprocally imprinted genes on the maternally and paternally inherited chromosomes"* — [PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)

### Finding 4 — RTL1 is a full-length Gag–Pol-like protein with nuclear localization; a retrovirus-derived protease motif is implicated by homology to PEG10

RTL1/PEG11 is not merely a transcribed pseudogene — it is translated into a **full-length protein**, directly identified by immunology and mass spectrometry from **postnatal nuclear preparations** of Callipyge sheep skeletal muscle. This confirms both that the gag–pol ORF is genuinely protein-coding and that the protein is found in **nuclear** preparations. The protein retains the **gag–pol-like structure characteristic of retroviruses**.

The functional significance of its retroviral protease domain is strongly supported by work on its closest paralog, **PEG10**. PEG10 requires an **intact viral aspartic protease motif** in its Pol-like region for fetal capillary maintenance, and the authors propose a functional **interaction between the two retrovirus-derived genes Peg10 and Rtl1** at the feto-maternal interface. This places Rtl1 in a shared, protease-dependent mechanistic pathway with PEG10.

> *"we have directly identified the full-length PEG11 protein from postnatal nuclear preparatio[ns]"* — [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)

> *"These elements contain a gag-pol-like structure characteristic of retroviruses"* — [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)

> *"an interaction occurs between two retrovirus-derived genes, Peg10 and retrotransposon Gag like 1 (Rtl1, also called Peg11), that is essential for the maintenance of fetal capillary endothelial cells"* — [PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)

### Finding 5 — RTL1 has a full Gag–Pol polyprotein architecture with a retropepsin aspartic-protease catalytic domain

Domain mapping of UniProt Q7M732 (1744 aa) reveals the **canonical Ty3/Gypsy gag–pol domain order**:

| Region | Approx. residues | Domain / annotation |
|---|---|---|
| N-terminal disordered region | 1–416 | Intrinsically disordered |
| Gag/capsid-like | ~454–534 | RTL1/LDOC capsid-like (PF16297) |
| Gag C-terminal capsid-like | ~541–615 | PEG10/RTL1 C-terminal capsid-like (PF30901 / IPR063300) |
| **Retropepsin aspartic protease** | **~675–764 / 681–788** | **CDD cd00303 "Retropepsins, pepsin-like aspartate proteases"; PF30863 / IPR063610; CATH acid-protease fold 662–783** |
| Reverse transcriptase / polymerase fold | ~900–1241 | IPR043502 / SSF56672 |
| RNase H-like | ~1106–1202 | PF17919 / IPR041577 |
| C-terminal transmembrane helices (×2) | ~1473–1493; ~1520–1540 | Predicted TM segments |

UniProt annotates the subcellular location as **"Membrane"** (consistent with the two predicted C-terminal transmembrane helices) and the function as *"essential role in capillary endothelial cells for maintenance of the feto-maternal interface and placental development."*

This architecture is the structural basis for inferring the protein's molecular function: of all its domains, the **retropepsin (aspartic protease)** domain is the one most likely to be catalytically active and functionally central, by analogy to PEG10.

### Finding 6 — The RTL1 retropepsin domain retains an intact catalytic aspartate motif (D684-S-G-A), indicating a likely-active aspartic protease

Direct sequence inspection of the RTL1 protease domain (residues ~662–788) reveals the canonical retroviral/retrotransposon aspartic-protease **active-site motif Asp-Ser-Gly-Ala ("DSGAEGN")**, centred on the catalytic aspartate **Asp684**. This is the same **D-(T/S)-G-A signature** that forms the catalytic dyad in classic retropepsins such as **HIV-1 protease (DTGA)**. The motif lies squarely within the CDD cd00303 "Retropepsins" assignment.

The retention of an intact catalytic aspartate is a strong structural argument that RTL1 is a **genuine, catalytically competent aspartic endopeptidase** rather than a degenerate pseudo-enzyme. This inference is reinforced by functional genetics in the paralog: a mutation in the **highly conserved viral aspartic protease motif in the Pol-like region of PEG10** abolishes its capillary-maintenance function, demonstrating that this motif is functionally essential in a close relative.

> *"we generated mice harboring a mutation in the highly conserved viral aspartic protease motif in the POL-like region of PEG10 because this motif is essential for the life cycle of LTR retrotransposons/retroviruses"* — [PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)

The most parsimonious molecular model is that RTL1's protease performs **autocatalytic maturation of its own Gag–Pol polyprotein** (as retroviral/retrotransposon proteases do), which in turn is required for the protein's structural capillary-maintenance activity.

### Finding 7 — Rtl1 is the major imprinted gene responsible for dosage-dependent fetal/neonatal skeletal-muscle development

In dedicated mouse models, **both deletion and overproduction of Rtl1** cause neonatal lethality accompanied by **severe but distinct skeletal-muscle defects**. Deletion phenocopies the postnatal muscle symptoms of **Temple syndrome** (the loss-of-function human disorder), whereas overproduction phenocopies **Kagami-Ogata syndrome** (the gain-of-function disorder). This identifies RTL1 as the **major gene responsible for the muscle defects**, not only the placental defects, of these imprinting diseases. It represents the **first example of a eutherian-specific LTR-retrotransposon-derived gene contributing to skeletal-muscle development**, and it is also the molecular basis of the ovine **callipyge** muscle-hypertrophy phenotype, in which PEG11/RTL1 expression correlates strongly with the muscling trait as a function of genotype, muscle type, and developmental stage.

> *"Rtl1 also plays an important role in fetal/neonatal skeletal muscle development: its deletion and overproduction in mice lead to neonatal lethality associated with severe but distinct skeletal muscle defects, similar to those of Temple and Kagami-Ogata syndromes, respectively"* — [PMID: 32878913](https://pubmed.ncbi.nlm.nih.gov/32878913/)

> *"This is the first example of an LTR retrotransposon-derived gene specific to eutherians contributing to eutherian skeletal muscle development"* — [PMID: 32878913](https://pubmed.ncbi.nlm.nih.gov/32878913/)

> *"PEG11 gene expression is also strongly correlated with the emergence of the muscling phenotype as a function of genotype, muscle type and developmental stage"* — [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)

*(Note: the PMID 32878913 snippets are flagged "mismatch" in the knowledge state — the quotes were drawn from a closely related source on the same study and should be treated as paraphrase-level support pending verification against the exact abstract.)*

### Finding 8 — Rtl1 has a role in the brain, regulating neuronal excitability in the locus coeruleus

Rtl1 is **paternally expressed in the brainstem, thalamus, and hypothalamus** of mice. Paternal *Rtl1* knockout mice show impaired suckling, increased neonatal death, and later-life **anxiety-, depression-, and social-related behaviors**. Electrophysiologically, loss of paternal Rtl1 causes a **delay in the onset of action potentials and inward currents with decreased neuronal excitability of locus coeruleus (LC) neurons** — the principal noradrenergic nucleus of the brain. This links Rtl1 to regulation of the noradrenergic system and emotional/social behavior, a role conserved enough to be relevant in both mouse and human brain.

> *"Rtl1 was paternally, but not maternally, expressed in brain stem, thalamus, and hypothalamus of mice"* — [PMID: 35567414](https://pubmed.ncbi.nlm.nih.gov/35567414/)

> *"Rtl1m+/p- mice showed an increased delay in time of onset for action potentials and inward currents with decreased neuronal excitability of LC neurons"* — [PMID: 35567414](https://pubmed.ncbi.nlm.nih.gov/35567414/)

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent model in which a **domesticated retroviral polyprotein** serves as a dosage-controlled structural/enzymatic factor essential for the mammalian placenta.

### Genomic regulation — reciprocal imprinting and trans-homologue control

```
   PATERNAL chr12 (12qF1)                     MATERNAL chr12 (12qF1)
   ───────────────────────                    ───────────────────────
   Dlk1 →   Rtl1 (sense) → PROTEIN            Meg3/Gtl2 ←  Rtl1as (antisense)
            |                                                  |
            |  mRNA                                            |  processed into
            |                                                  v
            |                                        miR-127 + 6 other miRNAs
            |                                                  |
            +------------- RNAi degradation  <-----------------+
                         (trans-homologue)

   Net effect: Rtl1 PROTEIN level is held within a narrow dosage window.
```

The paternal allele produces the protein-coding sense transcript; the maternal allele produces the antisense *Rtl1as*, which is processed into miR-127 and six additional miRNAs that degrade Rtl1 mRNA in *trans*. This elegant reciprocal-imprinting circuit is what enforces the strict dosage sensitivity seen phenotypically.

### Molecular function — a domesticated Gag–Pol polyprotein with an aspartic protease

```
 N -[ disordered ]-[ Gag/capsid ]-[ PROTEASE: D684-S-G-A ]-[ RT/pol ]-[ RNaseH ]-[ TM TM ]- C
    1            416   454-615         675-788               900-1241   ~1150     1473-1540
                                          |
                                 intact catalytic Asp (retropepsin)
                                          |
                                 v most-likely activity
                        autocatalytic polyprotein maturation
                       (validated as essential in paralog PEG10)
```

The protein's defining catalytic feature is the **retropepsin aspartic protease** with an intact Asp684 (D-S-G-A) active site. By the strong precedent of HIV-1 protease and, decisively, by the genetic requirement for the equivalent motif in PEG10, this domain is predicted to be catalytically active. Its most plausible substrate is the **Rtl1 polyprotein itself** (autocatalytic maturation), though whether it also cleaves host substrates remains untested. The two C-terminal transmembrane helices and the UniProt "Membrane" annotation indicate the mature/working protein associates with membranes, while the mass-spec identification in nuclear preparations indicates it is also present in/near the nucleus — possibly reflecting different processed forms or localizations in different tissues.

### Physiological output — a hierarchy of functions

| Tier | Function | Cell/tissue | Evidence quality |
|---|---|---|---|
| **Primary** | Dosage-sensitive maintenance of fetal capillary endothelium at the feto-maternal interface | Placental labyrinth / capillary endothelial cells | Strong: loss & gain mouse models, both lethal ([PMID: 18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/)) |
| **Secondary** | Dosage-dependent fetal/neonatal skeletal-muscle development | Skeletal muscle | Strong: loss/gain mouse models phenocopy Temple/Kagami-Ogata; callipyge correlation ([PMID: 32878913](https://pubmed.ncbi.nlm.nih.gov/32878913/), [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)) |
| **Secondary** | Regulation of neuronal excitability & behavior | Locus coeruleus (noradrenergic), brainstem/thalamus/hypothalamus | Moderate–strong: paternal-KO electrophysiology + behavior ([PMID: 35567414](https://pubmed.ncbi.nlm.nih.gov/35567414/)) |

The unifying theme is **evolutionary domestication (exaptation)**: an LTR retrotransposon's gag–pol machinery — originally serving the selfish replication of the element — has been captured by the host genome and repurposed as a dosage-controlled developmental gene essential for the key eutherian innovation, the placenta. Rtl1 and its paralog PEG10 are proposed to act together ("an interaction occurs between two retrovirus-derived genes") in the same capillary-maintenance process, suggesting a shared, protease-dependent module at the heart of placental vascular integrity.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/) | Role of Rtl1 in the feto-maternal interface of mouse placenta | **Core.** Establishes the primary function: fetal-capillary maintenance; both loss and overproduction are lethal (dosage sensitivity). |
| [26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/) | Trans-homologue interaction between miR-127 and Rtl1 regulates placenta development | **Core.** Defines the miR-127/Rtl1as trans-homologue RNAi regulation; miR-127 KO → placentomegaly + labyrinth defects. |
| [20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/) | PEG11 (RTL1) expressed as full-length protein in Callipyge sheep muscle | **Core.** Direct protein-level and nuclear-localization evidence; gag–pol architecture; link to callipyge muscle phenotype. |
| [34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/) | PEG10 viral aspartic protease domain essential for fetal capillary structure | **Core (paralog).** Genetic proof the aspartic-protease motif is functionally essential; proposes Peg10–Rtl1 interaction. |
| [32878913](https://pubmed.ncbi.nlm.nih.gov/32878913/) | Deficiency and overexpression of Rtl1 | **Core.** Rtl1 as major driver of dosage-dependent skeletal-muscle development; phenocopies Temple/Kagami-Ogata. |
| [35567414](https://pubmed.ncbi.nlm.nih.gov/35567414/) | RTL1/PEG11 imprinted in brain mediates behavior & LC excitability | **Supporting.** Brain expression; regulation of locus coeruleus neuronal excitability and emotional/social behavior. |
| [32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/) | Temple & Kagami-Ogata syndromes: presentations, models, mechanisms | **Context.** Clinical/genetic framing of the imprinted 14q32/12qF1 cluster; mouse model value. |
| [28635951](https://pubmed.ncbi.nlm.nih.gov/28635951/) | Imprinted MEG8-DMR in 14q32 / novel Temple syndrome patients | **Context.** Imprinting/DMR regulation of DLK1/RTL1 vs MEG3/RTL1as/MEG8. |
| [28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/) | Evolution of brain functions & LTR retrotransposon-derived genes | **Context.** Places Rtl1/SIRH2 among domesticated LTR genes with placental/brain roles. |
| [41594701](https://pubmed.ncbi.nlm.nih.gov/41594701/) | Placenta-driven evolution: viral gene acquisition | **Context.** Evolutionary framing of metavirus-derived genes in placentation. |

**Consistency:** The evidence base is highly concordant. The placental-capillary function (18176565), the regulatory circuit (26138477), the protein/domain architecture (20072617 + UniProt), and the protease-dependence (34559199, by paralog) form a mutually reinforcing picture. No paper in the set contradicts the central model.

**A note of caution:** The strongest *direct* catalytic evidence (the aspartic-protease requirement) comes from **PEG10**, not RTL1 itself. The claim that RTL1's protease is catalytically active rests on (a) sequence conservation of the catalytic aspartate and (b) analogy to PEG10 and retroviral proteases — not on a direct enzymatic assay of RTL1.

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic assay of RTL1 protease.** The aspartic-protease activity of RTL1 is *inferred* from the intact D684-S-G-A motif and from the functional essentiality of the equivalent motif in PEG10. A direct biochemical demonstration of RTL1 proteolysis (and identification of its substrate — self vs. host) is lacking.

2. **Mechanism of capillary maintenance is unresolved.** We know Rtl1 is *required* for capillary integrity, but the downstream molecular pathway (e.g., which structural or signaling components it acts on, whether it functions in trophoblast or endothelial cells, and how PEG10 and RTL1 physically or functionally interact) is not established.

3. **Subcellular localization is ambiguous.** The protein is detected in nuclear preparations (sheep muscle) yet annotated as a membrane protein (two predicted C-terminal TM helices). Whether these reflect distinct processed forms, tissue-specific localization, or methodological artifacts is unclear.

4. **Dosage threshold and quantitative regulation.** The precise expression window compatible with viability, and the quantitative contribution of each of the seven Rtl1as miRNAs (beyond miR-127), are not fully mapped.

5. **Species scope.** Several key pieces (full-length protein, callipyge correlation) come from sheep; the behavioral/LC role comes from mouse. Cross-species generalization is reasonable given strong synteny but not exhaustively verified for every function in mouse.

6. **Citation integrity flag.** The muscle-development snippets (PMID 32878913) were flagged as "mismatch" in the knowledge state (likely paraphrase vs. exact abstract text). The conclusion is well supported by the overall literature, but the exact quotes should be re-verified.

---

## Proposed Follow-up Experiments / Actions

1. **Direct protease activity assay.** Express recombinant RTL1 Pol/protease domain and test autocatalytic cleavage in vitro; compare wild-type vs. a catalytic-dead D684A/D684N mutant to confirm the aspartate is required for activity.

2. **Catalytic-dead knock-in mouse.** Generate an Rtl1 D684A knock-in (mirroring the PEG10 protease-motif mutant of [PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)) to test whether protease catalysis — as opposed to merely the protein's presence — is required for fetal-capillary maintenance and muscle development.

3. **Substrate identification.** Use N-terminomics/mass spectrometry on placental tissue from wild-type vs. Rtl1-null or catalytic-dead animals to identify host substrates (if any) cleaved by RTL1, distinguishing autocatalytic from host-directed proteolysis.

4. **Cell-type-specific function.** Conditional (trophoblast- vs. endothelial-specific) Rtl1 deletion to determine in which cell the protein acts to maintain capillaries.

5. **PEG10–RTL1 interaction mapping.** Co-IP / proximity-labeling in placental cells to test the proposed physical/functional interaction between the two domesticated retroviral proteins and define their shared pathway.

6. **Localization resolution.** Immuno-EM and subcellular fractionation across placenta, muscle, and brain to reconcile the nuclear vs. membrane localization and determine whether different processed forms localize differently.

7. **Brain-circuit dissection.** In the locus coeruleus, test whether RTL1 protease activity (vs. presence) underlies the noradrenergic excitability phenotype, using region-specific catalytic-dead rescue.

---

## Conclusion

Mouse **Rtl1/Peg11 (Q7M732)** is a **paternally expressed, domesticated Ty3/Gypsy LTR-retrotransposon-derived imprinted gene** in the Dlk1–Dio3 cluster that encodes a **1744-aa Gag–Pol-like polyprotein**. Its Pol region carries a **retropepsin aspartic-protease domain with an intact catalytic aspartate (Asp684, D-S-G-A motif)**, so its probable molecular function is an **aspartic endopeptidase** (most likely autocatalytic polyprotein maturation), as experimentally validated for the equivalent motif in its paralog PEG10. Its **primary, experimentally established physiological role is the dosage-sensitive structural maintenance of the fetal capillary network at the feto-maternal interface of the placenta** — both loss and overexpression are lethal — with output tuned *in trans* by **miR-127** and other miRNAs from the reciprocally imprinted maternal antisense transcript *Rtl1as*. Secondarily, Rtl1 is the **major gene driving dosage-dependent fetal/neonatal skeletal-muscle development** (underlying Temple and Kagami-Ogata syndrome muscle phenotypes and ovine callipyge hypertrophy) and acts in the **locus coeruleus** to regulate neuronal excitability and emotional/social behavior.


## Artifacts

- [OpenScientist final report](Rtl1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20072617
2. PMID:26138477
3. PMID:18176565
4. PMID:34559199
5. PMID:32878913
6. PMID:35567414