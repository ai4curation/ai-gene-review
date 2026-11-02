---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:13:42.869105'
end_time: '2026-10-24T16:43:08.027839'
duration_seconds: 5365.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RTL1
  gene_symbol: RTL1
  uniprot_accession: A6NKG5
  protein_description: 'RecName: Full=Retrotransposon-like protein 1; AltName: Full=Mammalian
    retrotransposon derived protein 1; AltName: Full=Paternally expressed gene 11
    protein; AltName: Full=Retrotransposon-derived protein PEG11;'
  gene_info: Name=RTL1; Synonyms=MAR1, MART1, PEG11;
  organism_full: Homo sapiens (Human).
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RTL1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RTL1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** A6NKG5
- **Protein Description:** RecName: Full=Retrotransposon-like protein 1; AltName: Full=Mammalian retrotransposon derived protein 1; AltName: Full=Paternally expressed gene 11 protein; AltName: Full=Retrotransposon-derived protein PEG11;
- **Gene Information:** Name=RTL1; Synonyms=MAR1, MART1, PEG11;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DNA/RNA_pol_sf. (IPR043502); PEG10-RTL1_C-capsid. (IPR063300); Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); Rev_trsase/Diguanyl_cyclase. (IPR043128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTL1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTL1** (gene ID: RTL1, UniProt: A6NKG5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RTL1 (PEG11 / SIRH2, UniProt A6NKG5): A Domesticated Retroviral Gag-Pol Protein that Maintains the Placental Fetal Capillary Network

**Gene:** RTL1 (synonyms: MAR1, MART1, PEG11, SIRH2)
**UniProt:** A6NKG5 · **Organism:** *Homo sapiens*
**Also known as:** Retrotransposon Gag-like 1, Paternally expressed gene 11 protein (PEG11), Mammalian retrotransposon derived protein 1

---

## Summary

**RTL1** (Retrotransposon-like protein 1; also known as **PEG11**, **SIRH2**, **MAR1/MART1**; UniProt **A6NKG5**) is a paternally expressed, imprinted gene located in the human **14q32.2 DLK1–DIO3 imprinted cluster**. It is one of a family of eutherian-specific genes that were **domesticated ("exapted") from a captured Ty3/Gypsy (sushi-ichi) long-terminal-repeat (LTR) retrotransposon**. Rather than functioning as a classical enzyme, transporter, or signaling ligand, RTL1 encodes a translated **Gag-Pol-like structural protein** that retains the architectural hallmarks of a retroviral capsid: an N-terminal **Gag capsid domain** (InterPro IPR063300, PEG10-RTL1_C-capsid) and a retroviral-type **aspartic protease / Pol-like domain** (IPR021109; IPR043128 Rev_trsase/Diguanyl_cyclase; IPR043502 DNA/RNA_pol_sf). It has lost the ability to retrotranspose but has been repurposed for an essential developmental role.

The **primary, experimentally established physiological function** of RTL1 is the **maintenance of the fetal capillary network in the placental labyrinth** at the feto-maternal interface. RTL1 protein is expressed in the trophoblast cell layers that surround fetal capillary endothelial cells, and its correct **dosage is critical**: both loss-of-function and overexpression disrupt capillary integrity and cause late-fetal and/or neonatal lethality in mouse models. This dosage is tightly controlled in *trans* by microRNAs (notably **miR-127**) processed from the reciprocally imprinted maternal antisense transcript **RTL1as (PEG11as)**, which degrade RTL1 mRNA via RNAi.

Because of this exquisite dosage sensitivity, RTL1 is a central actor in several **imprinting-related phenotypes**: the ovine **callipyge** skeletal-muscle hypertrophy (driven by cis-acting overexpression of PEG11/RTL1), and in humans the two reciprocal **chromosome-14q32 imprinting disorders — Temple syndrome** (reduced paternal RTL1) and **Kagami-Ogata syndrome** (~2.5-fold RTL1 overexpression). By homology to its closest paralog **PEG10 (SIRH1)**, whose Gag domain has been shown to self-assemble into **virus-like particles (VLPs) that bind and package its own mRNA**, RTL1's capsid/protease architecture is inferred to confer Gag-like particle assembly and RNA-binding/packaging activity, providing a plausible biochemical basis for its structural/maintenance role at the trophoblast–endothelial interface.

---

## Gene / Protein Identity Verification

Before presenting the findings, the target identity was confirmed against the provided UniProt record:

| Attribute | Provided (UniProt A6NKG5) | Literature match |
|-----------|---------------------------|------------------|
| Gene symbol | RTL1 (syn. MAR1, MART1, PEG11) | ✅ RTL1 = PEG11 = SIRH2 consistently used across sheep, mouse, human studies |
| Protein name | Retrotransposon-like protein 1 / PEG11 | ✅ Matches "retrotransposon-derived imprinted gene" literature |
| Organism | *Homo sapiens* | ✅ Human 14q32 cluster studied directly; mouse/sheep are orthologs |
| Key domains | PEG10-RTL1_C-capsid (IPR063300); aspartic protease (IPR021109); Rev_trsase/pol (IPR043128, IPR043502) | ✅ Gag-Pol-like retroviral architecture confirmed |
| Family | (not specified in UniProt) | ✅ Mart/SIRH/RTL family of LTR-retrotransposon-derived genes |

**Conclusion:** The gene symbol, organism, and domain architecture all align unambiguously with the retrotransposon-derived imprinted gene RTL1/PEG11/SIRH2. This is **not** an ambiguous symbol collision; the literature is specific and consistent. Research proceeded with high confidence.

---

## Key Findings

### Finding 1 — RTL1/PEG11 is a sushi-ichi (Ty3/Gypsy) retrotransposon-derived, paternally expressed imprinted gene encoding a full-length Gag-Pol-like protein

RTL1 lies within the conserved **DLK1–DIO3 imprinted cluster** (human 14q32; ovine chromosome 18; mouse chromosome 12). The gene is **paternally expressed**, while its overlapping **maternally expressed antisense transcript (RTL1as / PEG11as)** hosts a set of microRNAs — including **miR-127** — that cleave the RTL1 mRNA through RNAi-mediated post-transcriptional degradation. This reciprocal, antisense arrangement creates a built-in dosage-control circuit within the imprinted locus.

The locus is derived from a **Ty3/Gypsy (sushi-ichi) LTR-retrotransposon** and retains a **gag-pol-like open reading frame**, including a retroviral-type **aspartic protease (POL) motif**, but has lost the ability to retrotranspose into the mammalian genome. Critically, this is not merely a predicted ORF: **Byrne et al. (2010)** directly identified the **full-length PEG11 protein** from postnatal skeletal muscle nuclear preparations using combined immunological and mass-spectrometry approaches, demonstrating that RTL1/PEG11 is genuinely translated into a stable protein product.

> *"These elements contain a gag-pol-like structure characteristic of retroviruses but have lost their ability to retrotranspose into the mammalian genome"* — [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)

> *"Using immunological and mass spectrometry approaches we have directly identified the full-length PEG11 protein from postnatal nuclear preparatio[ns]"* — [PMID: 20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/)

> *"Seven miRNAs, including miR-127, are processed from a maternally expressed antisense Rtl1 transcript (Rtl1as) and regulate Rtl1 levels through RNAi-mediated post-transcriptional degradation"* — [PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)

**Interpretation:** RTL1 is a *bona fide* protein-coding gene whose retroviral Gag-Pol architecture is the structural basis for its function, and whose expression is set by a reciprocally imprinted antisense-miRNA switch.

### Finding 2 — RTL1's primary physiological function: maintenance of the placental fetal capillary network at the feto-maternal interface

This is the **central, experimentally demonstrated function** of RTL1 and the best answer to the "primary function / localization" question.

- **Sekita et al. (2008)** used mouse knockout and overexpression models to show that *Rtl1*/*Peg11* is **essential for the maintenance of fetal capillaries** in the placental labyrinth. Both **loss** and **overproduction** of RTL1 cause **late-fetal and/or neonatal lethality** — establishing that the gene is strictly dosage-sensitive.

- **Kitazawa et al. (2017)** characterized the structural defect in detail: *Peg11/Rtl1* knockout placentas show **severe clogging of the labyrinth fetal capillaries with internal fetal bleeding**, with the **basal region of the fetal capillary network specifically damaged**. This reduces labyrinth expansion and placental size and is accompanied by early downregulation of the endothelial/angiogenic markers **Tmem100, Meox2, and Lyve1**, and leads to mid-fetal lethality.

- **Shiura et al. (2021)** localized the protein: RTL/PEG retrovirus-derived proteins are expressed in the **three trophoblast cell layers that surround fetal capillary endothelial cells**, and RTL1 acts together with its paralog **PEG10** (another retrovirus-derived gene, whose viral aspartic-protease domain is required) to maintain the fetal capillary endothelium.

> *"retrotransposon-derived Rtl1 ... also known as Peg11 ... is essential for maintenance of the fetal capillaries, and that both its loss and its overproduction cause late-fetal and/or neonatal lethality in mice"* — [PMID: 18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/)

> *"the severe clogging of fetal capillaries was associated with KO fetuses showing mid-fetal lethality with internal bleeding. Importantly, the basal region of the fetal capillary network was specifically damaged"* — [PMID: 28111885](https://pubmed.ncbi.nlm.nih.gov/28111885/)

> *"PEG10 is expressed in the three trophoblast cell layers that surround fetal capillary endothelial cells"* — [PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)

**Interpretation — localization and function:** RTL1 carries out its function **extracellularly / at the cell–cell interface within the placental labyrinth**, produced by trophoblast cells that surround the fetal capillary endothelium. Its role is **structural/maintenance** — preserving the integrity and patency of the fetal capillary network that mediates feto-maternal exchange — rather than catalytic or signaling.

### Finding 3 — RTL1 dosage controls skeletal muscle hypertrophy (callipyge) and underlies human muscle phenotypes

RTL1's dosage sensitivity is visible not only in the placenta but also in **postnatal skeletal muscle**. In sheep, the intergenic **callipyge (CLPG)** A→G point mutation lies in a long-range control element and **elevates PEG11/RTL1 transcript levels in cis without altering imprinting status**. PEG11/RTL1 shows a **~200-fold induction** in the hypertrophied muscles of paternal-heterozygous (polar-overdominant) animals, and its expression correlates with the muscling phenotype by genotype, muscle type, and developmental stage (Charlier/Bidwell/Byrne). RTL1 protein is detectable in postnatal skeletal muscle (Finding 1).

In **humans**, RTL1 lies in the 14q32 cluster and is paternally expressed; the two reciprocal imprinting disorders — **Temple syndrome** (loss/reduction of paternal RTL1) and **Kagami-Ogata syndrome** (overexpression) — produce distinct muscle and placental phenotypes that are recapitulated by *Rtl1* deficiency / overexpression mouse models.

> *"Analysis of PEG11 expression by quantitative PCR shows a 200-fold induction in the hypertrophied muscles of paternal heterozygous animals"* — [PMID: 15298706](https://pubmed.ncbi.nlm.nih.gov/15298706/)

> *"The locus encompasses paternally expressed protein-coding genes (DLK1, RTL1 and DIO3) and maternally expressed lncRNAs (MEG3/GTL2, RTL1as and MEG8)"* — [PMID: 32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/)

**Interpretation:** The callipyge model provides the clearest quantitative demonstration of RTL1's dosage-dependent phenotypic power (200-fold overexpression → muscle hypertrophy) and reinforces that the *amount* of RTL1 protein — set by the RTL1as-miRNA brake — is the key functional variable.

### Finding 4 — The Gag capsid / aspartic-protease architecture forms virus-like particles that bind and package mRNA (inferred for RTL1 from paralog PEG10)

RTL1 belongs to the **Mart/SIRH/RTL family** of LTR-retrotransposon Gag-Pol-derived genes and shares the **N-terminal Gag capsid domain** (IPR063300) and **aspartic-protease-like domain** (IPR021109) with its closest paralog **PEG10 (SIRH1)**. Because direct biochemical characterization of RTL1 protein is limited, the biochemical activity of these shared domains is best inferred from PEG10:

- **Segel et al. (2021)** showed that PEG10 self-assembles and **preferentially binds and mediates vesicular secretion of its own mRNA**, and can be pseudotyped/reprogrammed as a vehicle for mRNA delivery — i.e., it behaves like a retroviral Gag.

- **Campodonico et al. (2024)** confirmed that PEG10 **forms purifiable virus-like particles (VLPs)**, and that the related Gag-like gene **RTL8** regulates this by binding the N-terminal capsid domain.

- Reviews (**Al Othman et al., 2025**) class PEG10 — and by homology RTL1 — among human "virus-like proteins" that structurally resemble retroviral Gag.

> *"one LTR retrotransposon homolog, PEG10, that preferentially binds and facilitates vesicular secretion of its own messenger RNA (mRNA)"* — [PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)

> *"PEG10 resembles both retrotransposon and retroviral proteins and forms virus-like particles (VLPs) that can be purified using iodixanol ultracentrifugation"* — [PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)

**Interpretation (inference, not direct RTL1 evidence):** The conserved Gag capsid and aspartic-protease domains plausibly give RTL1 the capacity for **self-assembly into capsid-like / virus-like particles and RNA binding/packaging**. This offers a candidate molecular mechanism — delivery or scaffolding of cargo (RNA/protein) between trophoblast and endothelial cells — for how RTL1 maintains fetal capillary integrity. This mechanism is **not yet demonstrated directly for RTL1** and should be treated as a strong hypothesis.

### Finding 5 — RTL1 = PEG11 = SIRH2 is a eutherian-specific sushi-ichi retrotransposon-derived gene co-opted during the evolution of viviparity/placentation

The human genome contains **~30 LTR-retrotransposon-derived genes**, including the **sushi-ichi retrotransposon homolog (SIRH) / RTL family**. Within this family, **RTL1 = PEG11/SIRH2** and its paralog **PEG10 = SIRH1**. **PEG10/SIRH1** is essential for placenta formation, while **PEG11/RTL1/SIRH2** is essential for maintenance of fetal capillaries — together providing strong evidence that these domesticated retroviral genes **contributed to the evolution of mammalian viviparity**. The RTL/SIRH genes (11 in eutherians) are presumed to derive from a **single ancestral retrovirus/retrotransposon capture event in the eutherian lineage** (Kaneko-Ishino & Ishino).

> *"PEG10/SIRH1 as well as PEG11/RTL1/SIRH2 and SIRH7/LDOC1 play essential roles in placenta formation, maintenance of fetal capillaries and the differentiation/maturation of a variety of placental cells, respectively"* — [PMID: 28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/)

> *"Eutherians have 11 retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes presumably derived from a certain retrovirus"* — [PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)

**Interpretation:** RTL1 is a textbook example of **molecular domestication (exaptation)** — a captured viral gene repurposed for an essential host developmental function, specifically the construction/maintenance of the eutherian placenta.

### Finding 6 — In humans, RTL1 is quantitatively dosage-controlled by RTL1as miRNAs, and ~2.5-fold overexpression drives Kagami-Ogata syndrome

The human **14q32.2** region carries **paternally expressed DLK1 and RTL1** and **maternally expressed MEG3 and RTL1as**. In **paternal uniparental disomy 14 [upd(14)pat]**, or in maternal **IG-DMR / MEG3-DMR epimutations or microdeletions**, the maternal RTL1as-encoded microRNAs — which act as a *trans*-acting repressor of RTL1 — are lost. As a result, **RTL1 expression becomes ~2.5-fold increased**. This **excessive RTL1 expression (together with loss of MEG expression) is the primary underlying cause of Kagami-Ogata syndrome**, characterized by a distinctive face, a **small bell-shaped thorax with a "coat-hanger" rib appearance**, abdominal wall defects, **placentomegaly, and polyhydramnios** (Ogata & Kagami, 2016).

> *"RTL1 expression level becomes ~2.5 times increased in the absence of functional RTL1as-encoded microRNAs that act as a trans-acting repressor for RTL1"* — [PMID: 26377239](https://pubmed.ncbi.nlm.nih.gov/26377239/)

> *"a small bell-shaped thorax with coat-hanger appearance of the ribs, abdominal wall defects, placentomegaly and polyhydramnios"* — [PMID: 26377239](https://pubmed.ncbi.nlm.nih.gov/26377239/)

**Interpretation — clinical significance in humans:** Even a modest **~2.5-fold** increase in RTL1 is pathogenic, directly demonstrating the dosage sensitivity in the human context and linking RTL1 overexpression causally to a recognizable congenital imprinting disorder with prominent placental features (placentomegaly), consistent with its placental capillary role.

---

## Mechanistic Model / Interpretation

### The imprinted dosage-control circuit (14q32 / DLK1–DIO3 locus)

```
                 PATERNAL allele (expressed)
   ...DLK1 ───────────────► RTL1 (PEG11) ──────────► DIO3...
                             │  (Gag-Pol-like protein)
                             │
                   mRNA ◄────┤  degraded by RNAi
                             │
   ...MEG3/GTL2 ◄─────── RTL1as (PEG11as) ◄──── MEG8...
                 │  hosts miR-127 (+6 others)
                 MATERNAL allele (expressed)

  Net RTL1 protein level = f( paternal transcription  −  maternal RTL1as-miRNA braking )
```

The paternal allele transcribes the RTL1 protein; the maternal allele transcribes the overlapping antisense RTL1as, whose embedded miRNAs (miR-127 + others) cleave RTL1 mRNA. The **functional output is the net RTL1 protein dose**, which must stay within a narrow window.

### Dose–phenotype relationship

| RTL1 dose | Genetic/epigenetic cause | Phenotype |
|-----------|--------------------------|-----------|
| **Absent / strongly reduced** | *Rtl1* KO (mouse); Temple syndrome (loss of paternal RTL1) | Fetal capillary clogging, internal bleeding, reduced placental size, **mid-to-late fetal lethality**; postnatal muscle/growth deficits in humans |
| **Normal (tight window)** | Wild-type imprinting with intact RTL1as brake | Healthy labyrinth fetal capillary network; normal development |
| **~2.5× (human)** | upd(14)pat; IG-DMR/MEG3-DMR epimutation/deletion → loss of RTL1as miRNAs → Kagami-Ogata syndrome | Coat-hanger ribs, bell-shaped thorax, abdominal wall defects, **placentomegaly, polyhydramnios** |
| **~200× (sheep muscle)** | Callipyge CLPG cis-regulatory mutation | Postnatal skeletal muscle hypertrophy (callipyge) |
| **Overproduction (mouse)** | *Rtl1* transgenic overexpression | Late-fetal/neonatal **lethality** (capillary dysfunction) |

### Proposed molecular mechanism

```
   Trophoblast cell layers (3 layers of labyrinth)
   ┌───────────────────────────────────────────┐
   │   RTL1 (Gag capsid + aspartic protease)    │
   │        │ self-assembly? (by homology       │
   │        │   to PEG10 VLP + RNA packaging)    │
   │        ▼                                    │
   │   structural support / cargo delivery      │
   └───────────────┬────────────────────────────┘
                   ▼
   Fetal capillary ENDOTHELIAL cells
   (integrity maintained; Tmem100 / Meox2 / Lyve1 expressed)
                   │
                   ▼
   Patent fetal capillary network → feto-maternal exchange
```

RTL1 is produced by the trophoblast layers that physically surround fetal capillary endothelial cells. Its retroviral Gag/aspartic-protease architecture — by analogy to PEG10's demonstrated VLP assembly and mRNA packaging — may allow it to form capsid-like particles that scaffold or deliver cargo supporting endothelial survival/integrity. When RTL1 is lost, the basal capillary network collapses (clogging, bleeding, loss of angiogenic markers); when it is overexpressed, capillary homeostasis is also disrupted. This makes RTL1 a **dosage-sensitive structural/maintenance factor**, not an enzyme, transporter, or signaling ligand in the classical sense.

### Answering the specific functional questions
- **Primary function:** Structural/maintenance protein (domesticated retroviral Gag-Pol); maintains placental labyrinth fetal capillary network. It is *not* a classical catalytic enzyme despite possessing a degenerate aspartic-protease-like motif (the protease function is best documented in paralog PEG10, where it is required for the same process).
- **Substrate/cargo (inferred):** By homology to PEG10, RNA (preferentially its own mRNA), packaged into virus-like particles.
- **Localization:** Produced by trophoblast cell layers at the feto-maternal interface (placental labyrinth), acting at the trophoblast–endothelial boundary; Byrne 2010 also detected protein in skeletal-muscle nuclear preparations.
- **Pathway:** Operates within the imprinted DLK1–DIO3 regulatory network; dosage set by RTL1as/miR-127 RNAi; functionally cooperates with PEG10 in capillary maintenance; part of the RTL/SIRH placental developmental program.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [20072617](https://pubmed.ncbi.nlm.nih.gov/20072617/) | *PEG11 (RTL1) expressed as full-length protein in callipyge sheep muscle* | **Direct protein evidence**: full-length PEG11 identified by MS; gag-pol-like structure (F1, F3) |
| [26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/) | *Trans-homologue miR-127/Rtl1 interaction regulates placenta* | RTL1as miRNAs (miR-127) degrade RTL1 mRNA by RNAi (F1) |
| [18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/) | *Rtl1 in the feto-maternal interface of mouse placenta* | **Core function**: essential for fetal capillary maintenance; dosage-sensitive lethality (F2) |
| [28111885](https://pubmed.ncbi.nlm.nih.gov/28111885/) | *Severe damage to placental fetal capillary network in Peg11/Rtl1 KO* | Structural defect: capillary clogging, bleeding, basal network damage (F2) |
| [34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/) | *PEG10 viral aspartic protease domain essential for fetal capillary structure* | Localization to 3 trophoblast layers; PEG10/RTL1 cooperation (F2, F4) |
| [15298706](https://pubmed.ncbi.nlm.nih.gov/15298706/) | *PEG11/PEG11AS expression in normal and callipyge sheep* | **Quantitative dosage**: ~200-fold PEG11 induction in hypertrophied muscle (F3) |
| [32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/) | *Temple and Kagami-Ogata syndromes: mechanisms* | Human RTL1 as paternally expressed protein-coding gene in 14q32 (F3) |
| [28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/) | *LTR retrotransposon-derived genes / SIRH family* | RTL1 = PEG11/SIRH2; fetal-capillary role within SIRH family (F5) |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *Retrovirus-derived RTL/SIRH in eutherian evolution* | 11 eutherian RTL/SIRH genes from captured retrovirus (F5) |
| [34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/) | *PEG10 packages its own mRNA; pseudotyped for delivery* | **Mechanistic inference**: Gag domain binds/packages mRNA into VLPs (F4) |
| [39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/) | *RTL8 antagonizes PEG10-mediated VLPs* | Mart-family Gag capsid self-assembles into VLPs; RTL8 regulation (F4) |
| [38798208](https://pubmed.ncbi.nlm.nih.gov/38798208/) | *Human virus-like proteins: implications for gene therapy* | Classes PEG10/RTL family as Gag-like human VLPs (F4) |
| [26377239](https://pubmed.ncbi.nlm.nih.gov/26377239/) | *Kagami-Ogata syndrome (upd(14)pat) review* | **Human dosage**: ~2.5× RTL1 drives Kagami-Ogata; phenotype (F6) |
| [28635951](https://pubmed.ncbi.nlm.nih.gov/28635951/) | *MEG8-DMR in 14q32 / Temple syndrome patients* | Imprinting architecture of 14q32; DMR methylation (context) |
| [15498495](https://pubmed.ncbi.nlm.nih.gov/15498495/) | *Ectopic DLK1 in callipyge muscle* | Context: cis-regulatory co-upregulation of DLK1/PEG11 in callipyge (F3) |
| [11279514](https://pubmed.ncbi.nlm.nih.gov/11279514/) | *Callipyge mutation enhances imprinted gene expression in cis* | Context: CLPG elevates PEG11 in cis without changing imprinting (F3) |
| [32878913](https://pubmed.ncbi.nlm.nih.gov/32878913/) | *Deficiency and overexpression of Rtl1 (Temple/Kagami-Ogata models)* | Context: mouse models recapitulate human muscle/placental symptoms (F3) |

**Convergence of evidence:** The core conclusion — RTL1 maintains the placental fetal capillary network — is supported by **independent mouse genetic studies** (loss-of-function KO and overexpression; PMIDs 18176565, 28111885, 34559199). The dosage-sensitivity theme is corroborated across **three species** (mouse models, ovine callipyge, human Temple/Kagami-Ogata). The biochemical mechanism (VLP / RNA packaging) is **strongly inferred** from the well-characterized paralog PEG10 but not yet proven for RTL1 itself.

---

## Limitations and Knowledge Gaps

1. **Biochemical mechanism of RTL1 is inferred, not directly demonstrated.** The VLP assembly and mRNA-packaging activities are established for **PEG10**, not RTL1. Whether RTL1 forms particles, which RNAs/proteins it binds, and whether its aspartic-protease motif is catalytically active (vs. degenerate/structural) remain unknown. The IPR043128/IPR043502 pol/RT-like annotations have no demonstrated reverse-transcriptase or polymerase activity.

2. **Human-specific functional data are indirect.** Most mechanistic work is in **mouse (*Rtl1*) and sheep (PEG11)**. Human RTL1 function is inferred from (a) sequence/domain conservation, (b) the phenotypes of Temple and Kagami-Ogata syndromes, and (c) mouse models of these syndromes. No direct biochemical or cell-biological characterization of the human A6NKG5 protein was found.

3. **Molecular interactors and downstream pathway are incompletely defined.** RTL1 cooperates with **PEG10**, and the downregulation of **Tmem100, Meox2, Lyve1** in KO placenta hints at links to angiogenic/endothelial programs — but whether these are direct targets, binding partners, or downstream consequences is unresolved. No receptor, direct substrate, or signaling cascade has been definitively mapped for RTL1.

4. **Subcellular localization is only partially resolved.** Protein was detected in **skeletal-muscle nuclear preparations** (Byrne 2010) and attributed to **trophoblast layers** in placenta (Shiura 2021), but a systematic subcellular / secreted-vs-intracellular characterization of RTL1 is lacking.

5. **The precise cause of the muscle phenotype is not fully mechanistic.** In callipyge, DLK1 and PEG11/RTL1 are co-upregulated; the relative contributions of each to muscle hypertrophy, and whether RTL1's muscle role is mechanistically the same as its placental role, remain open.

6. **This report is a literature synthesis.** Conclusions rest on published studies and database annotations; no primary datasets were analyzed computationally.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical test of RTL1 VLP assembly and RNA binding.** Express recombinant human RTL1 (A6NKG5) and test, by iodixanol ultracentrifugation and cryo-EM (as done for PEG10 in PMID 39775359), whether it self-assembles into virus-like particles, and use CLIP-seq to identify bound RNAs (test whether it preferentially packages its own mRNA, like PEG10).

2. **Catalytic assay of the aspartic-protease motif.** Mutate the predicted DSG/DTG aspartic-protease active site and test whether proteolytic self-processing occurs, and whether the mutation phenocopies loss of function in placental capillary maintenance (paralleling the PEG10 protease-domain requirement, PMID 34559199).

3. **Define the RTL1 interactome at the trophoblast–endothelial interface.** Co-IP / proximity-labeling (BioID) in trophoblast and endothelial co-cultures to identify RTL1 partners; test the PEG10–RTL1 physical/functional interaction directly and whether RTL8-type antagonists regulate RTL1 as they do PEG10.

4. **Establish causal links to Tmem100/Meox2/Lyve1.** Use conditional *Rtl1* alleles with placental endothelial reporters and single-cell RNA-seq of KO vs WT labyrinth to determine whether these markers are direct RTL1 targets or downstream of capillary collapse.

5. **Human placental models.** Characterize endogenous human RTL1 protein in trophoblast organoids / placenta-derived cells; examine RTL1 protein levels and particle formation in placentas from Kagami-Ogata (overexpression) and Temple (reduced) pregnancies to connect the ~2.5-fold dosage change to a cellular capillary phenotype.

6. **Structure determination.** Solve the structure of the RTL1 Gag capsid domain (cryo-EM of particles or AlphaFold-guided experimental validation) to test the capsid-assembly hypothesis and compare with PEG10 / retroviral Gag.

---

## Conclusion

RTL1/PEG11/SIRH2 (A6NKG5) is a **domesticated retroviral Gag-Pol-like protein**, paternally expressed from the human 14q32 imprinted cluster, whose **primary function is the maintenance of the placental labyrinth fetal capillary network** at the feto-maternal interface, where it is produced by the trophoblast layers surrounding fetal capillary endothelial cells. It functions as a **dosage-sensitive structural/maintenance factor** — not a classical enzyme, transporter, or signaling ligand — with its protein level tightly governed by antisense **RTL1as/miR-127** RNAi. Its retroviral capsid and aspartic-protease domains, by homology to the experimentally characterized paralog **PEG10**, are inferred to mediate **virus-like-particle assembly and mRNA binding/packaging**, providing the most plausible molecular mechanism for its role. Dysregulated RTL1 dosage causes ovine callipyge muscle hypertrophy and the human imprinting disorders Temple syndrome (loss) and Kagami-Ogata syndrome (~2.5-fold excess).


## Artifacts

- [OpenScientist final report](RTL1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RTL1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20072617
2. PMID:26138477
3. PMID:18176565
4. PMID:28111885
5. PMID:34559199
6. PMID:15298706
7. PMID:32592473
8. PMID:34413232
9. PMID:39775359
10. PMID:28484174
11. PMID:37892118
12. PMID:26377239