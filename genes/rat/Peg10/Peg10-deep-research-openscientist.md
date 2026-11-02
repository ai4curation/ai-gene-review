---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T16:08:19.723767'
end_time: '2026-10-24T16:25:36.664441'
duration_seconds: 1036.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: rat
  gene_id: Peg10
  gene_symbol: Peg10
  uniprot_accession: A0ABK0LI09
  protein_description: 'SubName: Full=Paternally expressed 10 {ECO:0000313|Ensembl:ENSRNOP00000105220.1};'
  gene_info: Name=Peg10 {ECO:0000313|Ensembl:ENSRNOP00000105220.1, ECO:0000313|RGD:1595574};
  organism_full: Rattus norvegicus (Rat).
  protein_family: Not specified in UniProt
  protein_domains: PEG10-RTL1_C-capsid. (IPR063300); RTL1-rel. (IPR032567); RTL1/1-8/LDOC_capsid-like.
    (IPR032549); Znf_CCHC. (IPR001878); Znf_CCHC_sf. (IPR036875)
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
  path: Peg10-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Peg10-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** A0ABK0LI09
- **Protein Description:** SubName: Full=Paternally expressed 10 {ECO:0000313|Ensembl:ENSRNOP00000105220.1};
- **Gene Information:** Name=Peg10 {ECO:0000313|Ensembl:ENSRNOP00000105220.1, ECO:0000313|RGD:1595574};
- **Organism (full):** Rattus norvegicus (Rat).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PEG10-RTL1_C-capsid. (IPR063300); RTL1-rel. (IPR032567); RTL1/1-8/LDOC_capsid-like. (IPR032549); Znf_CCHC. (IPR001878); Znf_CCHC_sf. (IPR036875)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Peg10" matches the protein description above**
2. **Verify the organism is correct:** Rattus norvegicus (Rat).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Peg10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Peg10** (gene ID: Peg10, UniProt: A0ABK0LI09) in rat.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Rat PEG10 (Paternally Expressed Gene 10): A Domesticated Retroviral Gag/Gag-Pol Capsid Protein Essential for Placental Development

**Target:** Peg10 (Rattus norvegicus) | **UniProt:** A0ABK0LI09 | **Gene ID:** Peg10 (RGD:1595574) | **Ensembl protein:** ENSRNOP00000105220.1
**Key domains (InterPro):** PEG10-RTL1_C-capsid (IPR063300); RTL1-related (IPR032567); RTL1/1-8/LDOC capsid-like (IPR032549); CCHC zinc finger (IPR001878/IPR036875)

---

## Summary

Rat **Peg10** is a **domesticated LTR-retrotransposon-derived, paternally expressed imprinted gene** whose protein product is a **retroviral Gag/Gag-Pol-like protein**. Unlike a classical enzyme, transporter, or signaling receptor, PEG10's primary function is **structural and nucleic-acid-handling**: it uses a canonical retroviral **CCHC zinc-finger nucleocapsid motif** to bind RNA—preferentially its own mRNA—self-assembles into **virus-like particles (VLPs)/capsids**, and buds from cellular membranes to package and secrete RNA. This is the molecular behavior of a "domesticated" retrovirus: the host genome captured a *Ty3/gypsy* (sushi-ichi) retroelement and repurposed its Gag capsid and Pol protease machinery for endogenous developmental functions. X-ray crystallography directly confirms that the folded PEG10 domain is structurally homologous to the C-terminal capsid (CA) domain of cognate retroviral Gag proteins ([PMID: 34357660](https://pubmed.ncbi.nlm.nih.gov/34357660/)).

PEG10 is expressed as two products through **programmed −1 ribosomal frameshifting (−1 PRF)**: an ORF1 (Gag) protein, and an ORF1-2 (Gag-Pol) fusion that appends a **catalytically active aspartic protease** derived from the retroviral POL region. In developing placenta and amnion, this frameshift operates at >60% efficiency, and mutagenesis confirms the ORF2 protease autoprocesses the Gag-Pol precursor ([PMID: 17942406](https://pubmed.ncbi.nlm.nih.gov/17942406/)). Direct sequence analysis of the rat 408-aa ORF1 isoform (A0ABK0LI09) confirms a single C-X2-C-X4-H-X4-C CCHC zinc finger (CLYCGNGGHFADTC, ~residues 378–391) and the absence of the D[ST]G protease motif, consistent with this being the Gag product; the protease resides in the separate ORF2 frame.

Functionally, PEG10 is **essential for placental development**. *Peg10*-knockout mice die at ~E10.5 from severe placental defects, and a targeted point mutation in the viral protease active-site motif causes defective fetal placental vasculature. PEG10 operates in the **cytoplasm, at cellular membranes, in cytoplasmic stress granules, and extracellularly inside secreted vesicles/VLPs**. Beyond its structural/RNA-packaging role, it acts as a **signaling adapter/modulator**—binding and inhibiting TGF-β superfamily type-I receptors ALK1 and ALK5—and as an **anti-apoptotic, oncogenic factor** whose abundance is set by the balance of SIAH1/2 ubiquitination versus USP9X deubiquitination. The most precise answer to "what does PEG10 do" is therefore: *it is a domesticated retroviral capsid (Gag) protein that packages RNA into virus-like particles, with an accessory protease, acting primarily in placental trophoblast to support cell differentiation and fetal capillary maintenance.*

---

## Gene/Protein Identity Verification

A mandatory identity check was performed. The gene symbol **Peg10** matches the UniProt description ("Paternally expressed 10"), the organism (*Rattus norvegicus*) is correct, and the InterPro domain architecture (PEG10-RTL1 capsid, RTL1/LDOC capsid-like, CCHC zinc finger) aligns precisely with the published literature on PEG10 as a domesticated retroviral Gag/Gag-Pol protein. Critically, direct in-sequence analysis of the rat protein A0ABK0LI09 (408 aa) confirmed the diagnostic CCHC nucleocapsid motif, matching InterPro IPR001878/IPR036875. There is **no ambiguity**: this is the authentic PEG10 ortholog, and functional inference from the well-characterized mouse and human orthologs is justified by strong sequence and domain conservation.

---

## Key Findings

### 1. PEG10 is a domesticated *Ty3/gypsy* (sushi-ichi) LTR-retrotransposon-derived imprinted gene encoding a Gag/Pol-like protein

PEG10 is a **paternally expressed imprinted gene** that originated from capture of a *Ty3/gypsy* (sushi-ichi) LTR retrotransposon into the mammalian genome, retaining Gag- and Pol-like coding domains. The rat target protein (A0ABK0LI09) carries the diagnostic retroelement domain architecture noted in the UniProt/InterPro annotation: **PEG10-RTL1 C-capsid (IPR063300)**, **RTL1/LDOC capsid-like (IPR032549)**, and a **CCHC zinc finger (IPR001878/IPR036875)**—the hallmark Gag nucleocapsid motif. Ono/Nagasaki and colleagues established that Ty3/gypsy retrotransposon-derived genes such as PEG10 are "actively transcribed… with highly conserved DNA sequences and insertion sites" across species ([PMID: 16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/)). Decisively, X-ray crystallography demonstrated that the stably folded domains of PEG10 (and the related MOAP1) are "highly similar to the C-terminal capsid (CA) domains of cognate Gag proteins," confirming classification as a **domesticated retroviral Gag** ([PMID: 34357660](https://pubmed.ncbi.nlm.nih.gov/34357660/)).

This places PEG10 squarely in a structural/capsid protein class rather than a metabolic enzyme class. Its "substrate" is RNA (see Finding 4), and its mechanistic role is assembly and packaging.

### 2. PEG10 is essential for placental development; its viral protease domain maintains fetal placental vasculature

Genetic ablation provides the strongest evidence for the physiological importance of PEG10. *Peg10*-knockout mice exhibit **early embryonic lethality at ~E10.5 due to defects in the placenta**, demonstrating an essential, non-redundant role: "The Peg10 knockout mice showed early embryonic lethality owing to defects in the placenta" ([PMID: 16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/)). More precise dissection of the Gag-Pol function came from a targeted point mutation in the **conserved viral aspartic protease motif** of the POL-like region: this mutation causes perinatal lethality with fetal/placental growth retardation and **severe defects in the fetal vasculature**, "where PEG10 is expressed in the three trophoblast cell layers that surround fetal capillary endothelial cells" ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)). This pinpoints both the cell type and the molecular requirement (an active protease) for its vascular role.

### 3. PEG10 expresses ORF1 (Gag) and an ORF1-2 (Gag-Pol) fusion via high-efficiency −1 ribosomal frameshifting, and the ORF2 protease is catalytically active

PEG10 contains **two overlapping reading frames**, mirroring retroviral *gag* and *gag-pol* organization. Synthesis of the downstream ORF2 product requires **programmed −1 ribosomal frameshifting** during ORF1 translation. Clark and colleagues showed that endogenous ORF1 and the ORF1-2 frameshift protein "were detected in the developing placenta and amniotic membrane from 9.5 days post-coitus through to term with a very high frameshift efficiency (>60%)"—an unusually high recoding rate ([PMID: 17942406](https://pubmed.ncbi.nlm.nih.gov/17942406/)). Crucially, they demonstrated by mutagenesis that "the active site motif of a putative protease within ORF2 showed that this enzyme is active and participates in post-translational processing of PEG10 ORF1-2," establishing the aspartic protease as **catalytically functional and self-processing**. Frameshifting and protein were embryonic-tissue specific and not detected in adult mouse tissues, tying the Gag-Pol machinery to development.

### 4. PEG10 Gag binds RNA, drives vesicle budding, and forms virus-like particles that package and secrete its own mRNA

The capsid behavior of PEG10 is experimentally verified. Abed and colleagues showed that "the Gag domain of PEG10 can promote **vesicle budding similar to the HIV p24 Gag protein**," and that PEG10 "expressed in wild-type, differentiating TSCs was bound to many cellular RNAs including Hbegf"—stabilizing RNAs important for placentation; PEG10-deficient trophoblast stem cells show impaired differentiation into placental lineages ([PMID: 30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/)). Independently, Segel and colleagues demonstrated that PEG10 "preferentially binds and facilitates **vesicular secretion of its own messenger RNA**," forming virus-like particles; its mRNA cargo can be reprogrammed by flanking genes of interest with PEG10's untranslated regions, enabling engineered mRNA delivery (the SEND platform) ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)). Together these establish PEG10's primary molecular activity: **RNA binding → capsid self-assembly → membrane budding → extracellular secretion of an RNA-loaded VLP.**

### 5. Rat PEG10 ORF1/Gag (408 aa) carries the canonical retroviral CCHC nucleocapsid zinc finger

Direct sequence analysis of the rat UniProt entry A0ABK0LI09 (408 aa, PE=4, GN=Peg10) identified a single **C-X2-C-X4-H-X4-C CCHC zinc-finger motif (CLYCGNGGHFADTC)** at approximately residues 378–391, matching InterPro annotations IPR001878/IPR036875. This is the exact motif retroviral nucleocapsid proteins use to bind and package genomic RNA, providing the structural basis for the RNA-binding activity in Finding 4. Importantly, **no D[ST]G retroviral aspartic-protease motif is present in this isoform**, consistent with A0ABK0LI09 being the ORF1 (Gag) product; the protease resides in the separate ORF2 frame accessed only by −1 frameshifting. An N-terminal proline-rich stretch (PPPPPPPPP) is also present, a feature characteristic of these domesticated Gag proteins. This analysis directly confirms the rat ortholog retains the molecular hallmark of a functional nucleocapsid/Gag.

### 6. PEG10 Gag binds and inhibits TGF-β superfamily type-I receptors (ALK1/ALK5)—a candidate pathway for its vascular role

Beyond its capsid/RNA function, PEG10 has a defined **signaling adapter activity**. In a yeast two-hybrid screen, PEG10-RF1 (the Gag-like protein) was identified as a binding partner of **activin receptor-like kinase 1 (ALK1)**, a TGF-β type-I receptor. Lux and colleagues found that "PEG10-RF1 also interacts with different members of TGF-beta superfamily type I and II receptors. PEG10-RF1 binding to ALK1 is mediated by a 200-amino acid domain with no recognized motif. **PEG10-RF1 inhibits ALK1 as well as ALK5 signaling**" ([PMID: 15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/)). Because ALK1 loss-of-function causes hereditary hemorrhagic telangiectasia (abnormal vascular remodeling), this interaction provides a mechanistically plausible link between PEG10 and its documented role in maintaining fetal placental vasculature (Finding 2).

### 7. PEG10 is an anti-apoptotic, oncogenic protein regulated by SIAH ubiquitin ligases and localized to stress granules

PEG10 has a well-documented **anti-apoptotic/oncogenic** role. Okabe and colleagues showed that "PEG10 protein associated with SIAH1, a mediator of apoptosis, and that overexpression of PEG10 decreased the cell death mediated by SIAH1"; PEG10 is highly expressed in most hepatocellular carcinomas (HCC) but absent in normal liver ([PMID: 12810624](https://pubmed.ncbi.nlm.nih.gov/12810624/)). The regulatory logic was later refined: SIAH1 and SIAH2 bind the **PAIR domain** of PEG10, with "both proteins bound to the PAIR domain of PEG10 and promoted its polyubiquitination via K48/63-linked chains"—SIAH1 destabilizing PEG10 (tumor-suppressive) and SIAH2 stabilizing it (tumor-promoting) ([PMID: 42168988](https://pubmed.ncbi.nlm.nih.gov/42168988/)). PEG10 is also a **core component of cytoplasmic stress granules**, where it forms virus-like particles and, with RTL8, "drives the recruitment of UBQLN2 to stress granules" ([PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)).

### 8. PEG10 protein stability is set by opposing deubiquitination (USP9X) and ubiquitination (SIAH1/2); it belongs to the RTL/SIRH domesticated-retrovirus family

The ubiquitin–proteasome balance that governs PEG10 abundance includes a stabilizing arm. PEG10 is a substrate of the deubiquitinase **USP9X**, which "interacted with and deubiquitinated PEG10, thereby stabilizing PEG10"; USP9X knockdown/inhibition downregulates PEG10 and impairs tumor growth (e.g., in cutaneous T-cell lymphoma) ([PMID: 38677662](https://pubmed.ncbi.nlm.nih.gov/38677662/)). This directly opposes SIAH1/2-mediated polyubiquitination (Finding 7). PEG10 (also called SIRH1) is one of **11 eutherian retrotransposon Gag-like (RTL)/sushi-ichi retrotransposon homolog (SIRH) genes** "presumably derived from a certain retrovirus"; the family functions in placenta, brain, and innate immunity in a eutherian-specific manner ([PMID: 37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/)).

### 9. PEG10 acts primarily in the cytoplasm/at membranes and is secreted extracellularly inside virus-like particles and vesicles

Localization data converge on **cytoplasmic and membrane-associated compartments with extracellular secretion**: (1) the Gag domain "can promote vesicle budding similar to the HIV p24 Gag protein," implying plasma-membrane/endomembrane association ([PMID: 30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/)); (2) PEG10 self-assembles into VLPs that "preferentially bind and facilitate vesicular secretion of its own messenger RNA" into the extracellular space ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)); (3) PEG10 is "a core component of stress granules" in the cytoplasm ([PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)). In the placenta, it is expressed in the three trophoblast cell layers surrounding fetal capillaries ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)).

### 10. Within the RTL/SIRH family, PEG10/SIRH1 drives placental cell differentiation/maturation and cooperates with PEG11/RTL1 in fetal capillary maintenance

Authoritative reviews place PEG10 within a functional module of domesticated retroviral genes. Kaneko-Ishino and Ishino's review states that "PEG10/SIRH1 as well as PEG11/RTL1/SIRH2 and SIRH7/LDOC1 play essential roles in placenta formation, maintenance of fetal capillaries and the differentiation/maturation of a variety of placental cells" ([PMID: 28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/)). Experimentally, PEG10 and RTL1/PEG11 cooperate: "an interaction occurs between two retrovirus-derived genes, Peg10 and retrotransposon Gag like 1 (Rtl1, also called Peg11), that is essential for the maintenance of fetal capillary endothelial cells" ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)). Together with impaired trophoblast differentiation in PEG10-deficient stem cells (Finding 4), this defines PEG10's precise developmental role at the feto-maternal interface.

---

## Mechanistic Model / Interpretation

PEG10 is best understood as a **self-contained, host-domesticated retroviral core-particle machine** whose domains map one-to-one onto the retroviral replication cycle, repurposed for endogenous RNA logistics and placental biology.

```
                      PEG10 gene (imprinted, paternally expressed)
                                   |
                      transcription of a single mRNA
                                   |
          +------------------------+-------------------------+
          |                                                  |
    ORF1 translation                            -1 ribosomal frameshift (>60%)
          |                                                  |
     ORF1 / Gag (408 aa, rat)                      ORF1-2 / Gag-Pol fusion
   - N-terminal Pro-rich region                    - Gag capsid (CA-like)
   - Capsid (CA)-like fold  <-- X-ray confirmed    - + viral ASPARTIC PROTEASE (active)
   - CCHC zinc finger (RNA binding)                       |
          |                                        autoprocessing of precursor
          v                                                |
   RNA binding (own mRNA, Hbegf, etc.)                     v
          |                                     protease activity required for
   capsid self-assembly -> VLP                  fetal capillary maintenance
          |
   membrane budding (like HIV p24)
          |
   secretion of RNA-loaded VLP  ----> extracellular / vesicular mRNA transfer
```

**Structural/RNA-handling core (the primary function).** The CCHC zinc finger (Finding 5) binds RNA; the CA-like capsid fold (Finding 1) drives oligomerization into a shell; and the Gag membrane-budding activity (Finding 4) exports a loaded VLP. This recapitulates the retroviral assembly pathway—RNA genome recognition, capsid assembly, and budding—now used for **intercellular RNA transfer** and **RNA stabilization** in developing tissues. The ORF2 protease (Finding 3), accessed only via −1 frameshifting, provides the maturation step analogous to retroviral protease cleavage of Gag-Pol.

**Developmental deployment.** This machine is deployed in **placental trophoblast** (Findings 2, 9, 10). It stabilizes/packages RNAs that promote trophoblast differentiation and, acting with its paralog RTL1/PEG11, maintains fetal capillary endothelial integrity—explaining why both whole-gene knockout and a protease-dead point mutant produce placental/vascular failure and embryonic/perinatal lethality.

**Signaling and regulatory overlay.** Layered on top of the structural role are two accessory activities. First, PEG10 Gag binds and inhibits TGF-β type-I receptors ALK1/ALK5 (Finding 6)—a direct, receptor-level signaling adapter function with obvious relevance to vascular remodeling. Second, PEG10 protein level is a tightly contested node set by opposing ubiquitin writers/erasers (Findings 7, 8):

| Regulator | Activity | Effect on PEG10 | Biological consequence |
|---|---|---|---|
| SIAH1 | E3 ligase (K48/K63 on PAIR domain) | Destabilizes | Pro-apoptotic; tumor-suppressive |
| SIAH2 | E3 ligase (K48/K63 on PAIR domain) | Stabilizes | Promotes HCC progression |
| USP9X | Deubiquitinase | Stabilizes | Promotes tumor growth (e.g., CTCL) |

These data recast PEG10's "oncogenic" and "anti-apoptotic" phenotypes not as its primary purpose but as consequences of aberrant re-expression of a normally placenta-restricted capsid machine in cancer cells.

**Localization summary.**

| Compartment | Evidence | Finding |
|---|---|---|
| Cytoplasm / endomembrane | Gag budding activity | 4, 9 |
| Plasma membrane | HIV p24-like budding | 4, 9 |
| Cytoplasmic stress granules | Core SG component; recruits UBQLN2 | 7, 9 |
| Extracellular (in VLPs/vesicles) | Secretes own mRNA | 4, 9 |
| Trophoblast layers at feto-maternal interface | IHC in 3 trophoblast layers | 2, 9, 10 |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/) | *Deletion of Peg10… causes early embryonic lethality* | Establishes Ty3/gypsy origin AND essential placental role (KO lethal ~E10.5) |
| [34357660](https://pubmed.ncbi.nlm.nih.gov/34357660/) | *Structural evidence MOAP1 and PEG10 derived from Gag* | X-ray proof PEG10 folds as a retroviral capsid (CA) domain |
| [17942406](https://pubmed.ncbi.nlm.nih.gov/17942406/) | *PEG10 expresses two reading frames by −1 frameshifting* | Demonstrates >60% −1 PRF and a catalytically active, self-processing ORF2 protease |
| [30951545](https://pubmed.ncbi.nlm.nih.gov/30951545/) | *Gag protein PEG10 binds RNA… trophoblast lineage* | RNA binding, HIV p24-like budding, trophoblast differentiation |
| [34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/) | *PEG10 packages its own mRNA; pseudotyped delivery* | VLP formation, selective packaging and secretion of own mRNA (SEND) |
| [34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/) | *PEG10 protease domain essential for fetal capillaries* | Protease point-mutant disrupts fetal vasculature; trophoblast localization; PEG10–RTL1 interaction |
| [15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/) | *Gag/gag-pol proteins interact with ALK1* | PEG10 binds and inhibits TGF-β type-I receptors ALK1/ALK5 |
| [12810624](https://pubmed.ncbi.nlm.nih.gov/12810624/) | *PEG10 in HCC via SIAH1* | Anti-apoptotic SIAH1 interaction; oncogenic in HCC |
| [42168988](https://pubmed.ncbi.nlm.nih.gov/42168988/) | *Polyubiquitination of PEG10 by SIAH1/2 in HCC* | SIAH1/2 bind PAIR domain; opposing K48/K63 ubiquitination |
| [38677662](https://pubmed.ncbi.nlm.nih.gov/38677662/) | *USP9X decreases PEG10 in CTCL* | USP9X deubiquitinates and stabilizes PEG10 |
| [40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/) | *ERV-like proteins recruit UBQLN2 to stress granules* | PEG10 is a core stress-granule component in proteostasis |
| [37892118](https://pubmed.ncbi.nlm.nih.gov/37892118/) | *RTL/SIRH roles in eutherian development* | Places PEG10/SIRH1 in the 11-member domesticated-retrovirus family |
| [28484174](https://pubmed.ncbi.nlm.nih.gov/28484174/) | *Evolution of brain/placenta via LTR genes* | Review: PEG10/SIRH1 drives placental differentiation and capillary maintenance |

**Consistency.** The evidence is strikingly convergent. Independent approaches—genetics (KO and protease point mutant), crystallography, biochemistry (RNA binding, budding, VLP secretion), and in-sequence motif analysis of the rat ortholog itself—all point to the same structural/RNA-packaging identity. No reviewed study contradicts the core model. The rat ortholog A0ABK0LI09 was directly verified to carry the diagnostic CCHC motif, confirming we are researching the correct gene and that functional inference from the better-studied mouse/human orthologs is justified.

**Note on orthology.** Most mechanistic experiments were performed in mouse and human PEG10. Given the high conservation of insertion sites and sequence among Ty3/gypsy-derived imprinted genes ([PMID: 16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/)) and the confirmed presence of the CCHC motif and capsid-like domains in the rat protein (Finding 5), these functions are expected to be conserved in rat, but species-specific rat experiments remain largely absent.

---

## Limitations and Knowledge Gaps

1. **Species gap.** The functional literature is overwhelmingly mouse/human. Direct rat (A0ABK0LI09) functional assays—RNA binding specificity, VLP secretion, protease activity, placental phenotype—have not been performed. Our rat-specific evidence is limited to sequence/domain analysis.
2. **Substrate specificity of the protease is incompletely defined.** The ORF2 aspartic protease is proven active and self-processing ([PMID: 17942406](https://pubmed.ncbi.nlm.nih.gov/17942406/)), but its full cleavage-site repertoire and any trans-substrates (beyond autoprocessing) are not catalogued.
3. **RNA cargo breadth.** PEG10 binds its own mRNA and select transcripts (e.g., Hbegf), but a comprehensive, quantitative map of its physiological RNA cargo in trophoblast is incomplete.
4. **ALK1/ALK5 inhibition mechanism.** The 200-aa interacting domain has "no recognized motif" ([PMID: 15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/)); the structural basis and in vivo relevance to placental vasculature remain to be established.
5. **Reconciling roles.** How the structural/RNA-packaging function mechanistically produces anti-apoptotic and TGF-β-modulatory outcomes (e.g., whether these require VLP assembly) is not resolved.
6. **Localization quantification.** Partitioning between stress granules, membranes, and secreted VLPs under physiological vs. stress conditions has not been quantified in placental cells.

---

## Proposed Follow-up Experiments / Actions

1. **Rat-specific validation.** Express tagged rat PEG10 (A0ABK0LI09 ORF1 and the −1-frameshift ORF1-2) in rat trophoblast cells; assay RNA binding (CLIP-seq), VLP budding/secretion (density gradients, EM), and protease autoprocessing. Mutate the CCHC zinc finger (CLYCGNGGHFADTC) to test RNA-packaging dependence.
2. **Protease substrate mapping.** Use N-terminomics/mass spectrometry on protease-active vs. protease-dead (D[ST]G→A) Gag-Pol to define cleavage sites and any trans-substrates.
3. **RNA cargo atlas.** Perform CLIP-seq and VLP RNA-seq in differentiating rat/mouse trophoblast stem cells to define the physiological packaged transcriptome and link cargo to placentation phenotypes.
4. **ALK1/ALK5 structural interface.** Map the 200-aa interacting region by truncation/alanine scanning and test whether disrupting ALK1 binding phenocopies the fetal-vasculature defect in vivo.
5. **Ubiquitin-balance perturbation.** Modulate SIAH1/SIAH2/USP9X in trophoblast to determine whether PEG10 level setpoints control differentiation vs. capillary maintenance, distinguishing developmental from oncogenic regulation.
6. **Stress-granule vs. secretion switch.** Live-imaging and fractionation under stress to quantify how PEG10 partitions among stress granules, membranes, and secreted VLPs, and whether UBQLN2 recruitment competes with mRNA export.

---

## Conclusion

Rat **Peg10** encodes a **domesticated retroviral Gag/Gag-Pol-like protein** whose **primary function is structural rather than catalytic**: using a CCHC zinc-finger nucleocapsid motif it **binds RNA (preferentially its own mRNA), self-assembles into virus-like particle capsids, and buds from membranes to package and secrete RNA**, while an overlapping ORF2 reached by programmed −1 ribosomal frameshifting adds a **catalytically active aspartic protease** that autoprocesses the Gag-Pol precursor. It operates in the **cytoplasm, at cellular membranes, in stress granules, and extracellularly within secreted vesicles**, and is **essential for placental development**—supporting trophoblast proliferation/differentiation and, with its paralog RTL1/PEG11, maintaining fetal capillary endothelial cells. Accessory activities include inhibition of TGF-β type-I receptors ALK1/ALK5 and an anti-apoptotic partnership with SIAH1, with protein abundance governed by the opposing actions of SIAH1/2 ubiquitination and USP9X deubiquitination.


## Artifacts

- [OpenScientist final report](Peg10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Peg10-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34357660
2. PMID:17942406
3. PMID:16341224
4. PMID:34559199
5. PMID:30951545
6. PMID:34413232
7. PMID:15611116
8. PMID:12810624
9. PMID:42168988
10. PMID:40680123
11. PMID:38677662
12. PMID:37892118
13. PMID:28484174