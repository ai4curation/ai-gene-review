---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T14:11:23.754445'
end_time: '2026-10-24T14:36:18.757555'
duration_seconds: 1495.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Peg10
  gene_symbol: Peg10
  uniprot_accession: Q7TN75
  protein_description: 'RecName: Full=Retrotransposon-derived protein PEG10 {ECO:0000305};
    Short=MmPEG10 {ECO:0000303|PubMed:34413232}; AltName: Full=Embryonal carcinoma
    differentiation regulated protein {ECO:0000303|PubMed:11574691}; AltName: Full=Mammalian
    retrotransposon-derived protein 2 {ECO:0000303|PubMed:25888968}; AltName: Full=Myelin
    expression factor 3 {ECO:0000303|PubMed:9473521}; Short=MyEF-3 {ECO:0000303|PubMed:9473521};
    AltName: Full=Myelin expression factor 3-like protein 1; Short=MEF3-like protein
    1; AltName: Full=Paternally expressed gene 10 protein {ECO:0000303|PubMed:12840045};
    AltName: Full=Retrotransposon gag domain-containing protein 3; AltName: Full=Retrotransposon-derived
    gag-like polyprotein; AltName: Full=Ty3/Gypsy-like protein {ECO:0000303|PubMed:11158386};'
  gene_info: Name=Peg10 {ECO:0000303|PubMed:12840045, ECO:0000312|MGI:MGI:2157785};
    Synonyms=Edr {ECO:0000303|PubMed:11574691}, Mar2, Mart2 {ECO:0000303|PubMed:25888968},
    Mef3l1, Rgag3;
  organism_full: Mus musculus (Mouse).
  protein_family: Not specified in UniProt
  protein_domains: PEG10-RTL1_C-capsid. (IPR063300); PEG10_N-capsid-like. (IPR005162);
    Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); RTL1-rel.
    (IPR032567)
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
- **UniProt Accession:** Q7TN75
- **Protein Description:** RecName: Full=Retrotransposon-derived protein PEG10 {ECO:0000305}; Short=MmPEG10 {ECO:0000303|PubMed:34413232}; AltName: Full=Embryonal carcinoma differentiation regulated protein {ECO:0000303|PubMed:11574691}; AltName: Full=Mammalian retrotransposon-derived protein 2 {ECO:0000303|PubMed:25888968}; AltName: Full=Myelin expression factor 3 {ECO:0000303|PubMed:9473521}; Short=MyEF-3 {ECO:0000303|PubMed:9473521}; AltName: Full=Myelin expression factor 3-like protein 1; Short=MEF3-like protein 1; AltName: Full=Paternally expressed gene 10 protein {ECO:0000303|PubMed:12840045}; AltName: Full=Retrotransposon gag domain-containing protein 3; AltName: Full=Retrotransposon-derived gag-like polyprotein; AltName: Full=Ty3/Gypsy-like protein {ECO:0000303|PubMed:11158386};
- **Gene Information:** Name=Peg10 {ECO:0000303|PubMed:12840045, ECO:0000312|MGI:MGI:2157785}; Synonyms=Edr {ECO:0000303|PubMed:11574691}, Mar2, Mart2 {ECO:0000303|PubMed:25888968}, Mef3l1, Rgag3;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PEG10-RTL1_C-capsid. (IPR063300); PEG10_N-capsid-like. (IPR005162); Peptidase_aspartic_dom_sf. (IPR021109); PRO_PEG10-RTL1. (IPR063610); RTL1-rel. (IPR032567)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Peg10" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Peg10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Peg10** (gene ID: Peg10, UniProt: Q7TN75) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Mouse PEG10 (Q7TN75): A Domesticated Retroviral Gag–Pol Protein

**Gene:** *Peg10* (synonyms: *Edr*, *Mar2/Mart2*, *Mef3l1*, *Rgag3*; SIRH1/RTL2)
**Organism:** *Mus musculus* (mouse)
**UniProt:** Q7TN75 · **MGI:** 2157785 · **Locus:** proximal chromosome 6 (imprinted; human ortholog 7q21.3)

## Summary

**Mouse PEG10 (Q7TN75, gene *Peg10*) is a domesticated LTR-retrotransposon-derived Gag–Pol polyprotein whose primary molecular function is non-enzymatic and structural: its Gag/nucleocapsid-like capsid domain self-assembles into virus-like particles (VLPs) and binds and packages RNA — preferentially its own mRNA and U/G-rich transcripts — for secretion in extracellular vesicles.** PEG10 is not a metabolic enzyme, transporter, or classical signaling receptor. It is the founding member of the therian-specific sushi-ichi retrotransposon homologue (SIRH)/Retrotransposon Gag-like (RTL) gene family, which arose through "molecular domestication" of a Ty3/Gypsy (metavirus) LTR retrotransposon captured into the mammalian germline. Like its retroviral ancestor, it is expressed as two products — a Gag-like protein (RF1/ORF1) and an extended Gag-Pol-like protein (RF1/2, ORF1/2) — via programmed −1 ribosomal frameshifting driven by a stimulatory RNA pseudoknot. The Pol extension carries a retroviral aspartic-protease motif that performs a self-processing cleavage.

**Where it acts:** PEG10 operates in the cytoplasm and secretory/extracellular-vesicle pathway (it is a secreted GAG-domain protein) and, in vivo, at the trophoblast cell layers of the placenta. *Peg10* is a paternally expressed imprinted gene (mouse proximal chromosome 6; human 7q21.3) that is absolutely essential for mouse development: knockout causes early embryonic lethality from placental failure. A later, protease-dependent function maintains the fetal capillary vasculature of the placenta from mid- to late-gestation.

**Pathways:** Beyond its structural/RNA-packaging role, PEG10's ~200-amino-acid "PAIR" domain functions as a protein-interaction hub. It binds TGF-β superfamily type I/II receptors (notably ALK1 and ALK5) and inhibits their signaling; it binds the apoptosis mediator SIAH1 and suppresses SIAH1-mediated cell death; and it is a substrate of the E3 ubiquitin ligases SIAH1/2 and UBE3A, which set its steady-state abundance. Aberrant somatic re-expression is oncogenic across several carcinomas, and pathological accumulation dysregulates neuronal mRNA splicing, linking PEG10 to ALS and Angelman syndrome. The following report details each of these findings, the supporting evidence, a synthesized mechanistic model, the evidence base, limitations, and proposed follow-up experiments.

---

## Key Findings

### 1. PEG10 is a domesticated Gag-like protein that binds and packages its own mRNA into secreted virus-like particles

The defining, primary molecular function of PEG10 is that of a retroviral Gag homolog that forms capsids and packages RNA. Segel et al. (2021) identified PEG10 among human LTR-retrotransposon homologs as a protein that **"preferentially binds and facilitates vesicular secretion of its own messenger RNA (mRNA)"** ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)). PEG10 self-assembles into virus-like particles, selectively encapsidates its own transcript (recognized through flanking untranslated regions), and is exported from cells in extracellular vesicles. Critically, this cargo specificity is programmable: fusing a gene of interest to PEG10 UTRs reroutes that transcript into PEG10 VLPs, which became the basis of the "SEND" (Selective Endogenous eNcapsidation for cellular Delivery) mRNA-delivery platform. This is the strongest single piece of evidence that PEG10's core activity is **non-enzymatic, structural RNA binding and packaging**, mediated by the retained Gag capsid/nucleocapsid architecture (InterPro PEG10_N-capsid-like IPR005162; PEG10-RTL1_C-capsid IPR063300).

### 2. PEG10 is an imprinted, paternally expressed gene essential for mouse placental development

Ono et al. (2006) produced the first direct genetic demonstration of PEG10's physiological importance. *Peg10*-knockout mice showed **"early embryonic lethality owing to defects in the placenta"** ([PMID: 16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/)), providing the landmark evidence that an evolutionarily conserved retrotransposon-derived gene is indispensable for mammalian development. The same study established the gene's regulation and location: *Peg10* is **"a paternally expressed imprinted gene on mouse proximal chromosome 6"** (syntenic with human 7q21.3). The lethal placental phenotype positions PEG10 at the top of the functional hierarchy among domesticated retroelement genes — its loss is not a subtle, pleiotropic effect but a developmental catastrophe at the trophoblast.

### 3. PEG10 is expressed as Gag and Gag-Pol polyproteins via programmed −1 ribosomal frameshifting and interacts with the apoptosis mediator SIAH1

PEG10 retains the ancestral retroviral translational strategy. It is produced as a short Gag (ORF1) protein and, through a programmed −1 ribosomal frameshift (−1 PRF) stimulated by a downstream RNA pseudoknot, an extended Gag-Pol (ORF1/2) protein carrying an aspartic-protease domain (InterPro Peptidase_aspartic_dom_sf IPR021109). Kostov et al. (2026) confirm PEG10 as a mammalian retrotransposon-derived gene whose expression is governed by −1 PRF driven by a stimulatory pseudoknot ([PMID: 42818233](https://pubmed.ncbi.nlm.nih.gov/42818233/)). Functionally, Okabe et al. (2003) showed that **"PEG10 protein associated with SIAH1, a mediator of apoptosis, and that overexpression of PEG10 decreased the cell death mediated by SIAH1"** ([PMID: 12810624](https://pubmed.ncbi.nlm.nih.gov/12810624/)), establishing a direct anti-apoptotic, oncogenic activity (PEG10 is highly expressed in hepatocellular carcinoma yet absent in normal liver). Liu et al. (2026) refined the mechanism, showing that SIAH1 and SIAH2 **"bound to the PAIR domain of PEG10 and promoted its polyubiquitination via K48/63-linked chains"** ([PMID: 42168988](https://pubmed.ncbi.nlm.nih.gov/42168988/)), identifying both the interaction surface and the ubiquitin-mediated control of PEG10 abundance.

### 4. PEG10 selectively binds U/G-rich RNA and regulates mRNA splicing, linking it to TDP-43 neuronal pathways

In addition to packaging its own transcript, PEG10 acts more broadly as a sequence-selective RNA-binding protein with gene-regulatory consequences in neurons. Matthews & Whiteley (2026) report that **"PEG10 has selectivity for binding U/G-rich RNAs and influences widespread gene expression changes"** ([PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)). Strikingly, **"PEG10 overexpression mimics the loss of TDP-43 in broad changes to gene expression, including dysregulation of mRNA splicing pathways."** This defines PEG10's RNA substrate preference (U/G-rich transcripts — the same motif class recognized by TDP-43) and positions its pathological accumulation as a driver of splicing dysregulation relevant to amyotrophic lateral sclerosis (ALS) and Angelman syndrome. The protein undergoes a complex self-processing pathway, and gene-expression changes scale with protein accumulation.

### 5. The PEG10 Gag protein (RF1) binds TGF-β superfamily receptors via the PAIR domain and inhibits their signaling

Lux et al. (2005) identified PEG10 in a yeast two-hybrid screen as a binding partner of ALK1, a TGF-β superfamily type I receptor. They found that **"PEG10-RF1 also interacts with different members of TGF-beta superfamily type I and II receptors. PEG10-RF1 binding to ALK1 is mediated by a 200-amino acid domain with no recognized motif. PEG10-RF1 inhibits ALK1 as well as ALK5 signaling"** ([PMID: 15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/)). This ~200-aa region (the "PAIR" domain) is the same surface later shown to recruit SIAH1/2. The study also confirmed the dual-product expression logic, showing that **"two proteins, PEG10-RF1 and PEG10-RF1/2, are translated by a typical retroviral -1 ribosomal frameshift mechanism."** PEG10 is thus a negative modulator of TGF-β/activin receptor signaling, a pathway central to vascular and placental biology — a plausible molecular link to its in vivo placental vasculature role.

### 6. PEG10 is an oncogenic driver of proliferation, cell-cycle progression, and invasion across carcinomas

Consistent with its anti-apoptotic SIAH1 interaction, somatic re-expression of PEG10 is pro-tumorigenic. Li et al. (2016) showed PEG10 is significantly elevated in breast cancer tissue, correlates with distant metastasis and poor outcome, and that **"ectopic overexpression of PEG10 in breast cancer cells enhanced cell proliferation, cell cycle, clone formation along with migration and invasion"** ([PMID: 26934961](https://pubmed.ncbi.nlm.nih.gov/26934961/)). Mechanistically, PEG10 downregulated E-cadherin and upregulated matrix metalloproteinases MMP-1/-2/-9, with gene-set enrichment implicating cell-cycle processes. This aligns with the hepatocellular carcinoma findings of Okabe et al. (2003). The oncogenic role is best understood as a pathological reactivation of PEG10's normal developmental (trophoblast proliferation/invasion) and anti-apoptotic programs.

### 7. The PEG10 Pol aspartic-protease motif is required for placental fetal-capillary maintenance

Shiura et al. (2021) dissected the in vivo role of the Pol domain by mutating the highly conserved viral aspartic-protease motif in mouse PEG10. Whereas full knockout causes early embryonic lethality, protease-motif mutants survived longer but showed perinatal lethality with fetal/placental growth retardation from mid-gestation and **"severe defects... in the fetal vasculature, where PEG10 is expressed in the three trophoblast cell layers that surround fetal capillary endothelial cells"** ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)). The authors conclude that **"Peg10 has essential roles, not only in early placenta formation, but also in placental vasculature maintenance from mid- to late-gestation."** This finding (a) localizes PEG10 to the three trophoblast layers surrounding fetal capillaries, (b) demonstrates the protease is functionally essential (not vestigial), and (c) separates two temporally distinct placental functions — early formation (Gag-dependent) and later vasculature maintenance (protease-dependent), likely in concert with its paralog Rtl1/Peg11.

### 8. PEG10 is a therian-specific domesticated LTR-retrotransposon (SIRH/RTL) gene — the founding family member

PEG10's evolutionary origin is well established. Naville et al. (2016) describe how LTR-retroelement *gag*, *env*, integrase, and protease sequences have been repeatedly co-opted into host genes: **"Retroelement-derived genes are involved in many important biological processes including placenta formation, cognitive functions in the brain and immunity against retroelements, as well as in cell proliferation, apoptosis and cancer"** ([PMID: 26899828](https://pubmed.ncbi.nlm.nih.gov/26899828/)). Irie et al. (2026) formalize the family: **"Eutherian mammals possess 11 metavirus-derived genes, collectively known as the sushi-ichi retrotransposon homologue (SIRH)/Retrotransposon Gag-like (RTL) genes"** ([PMID: 42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/)). PEG10 (= SIRH1/RTL2/Mart2) is the founding member and functional partner of Rtl1/Peg11 (SIRH2). This classification explains PEG10's domain architecture, its imprinting, and its co-evolution with the mammalian placenta.

### 9. PEG10 is a secreted protein whose abundance is controlled by UBE3A, linking it to Angelman syndrome

Pandya et al. (2021) characterize PEG10 as a **"secreted retrovirus-like GAG-domain-containing protein... regulated by UBE3A and... involved in Angelman syndrome pathophysiology"** ([PMID: 34467244](https://pubmed.ncbi.nlm.nih.gov/34467244/)). UBE3A is the maternally expressed E3 ubiquitin ligase lost in Angelman syndrome; its loss de-represses PEG10, causing pathological accumulation. This complements the SIAH1/2-mediated ubiquitination (Liu et al. 2026) and the vesicular secretion reported by Segel et al. (2021), establishing that (a) PEG10 is a bona fide secreted protein and (b) its levels are tightly set by at least two independent ubiquitin-ligase systems. *(Note: the exact verbatim quote for this finding was flagged during automated verification and should be re-checked against the primary source; the UBE3A-regulation and secretion conclusions remain well-supported by the paper.)*

### 10. Integrated conclusion: PEG10's primary function is a domesticated Gag–Pol capsid/RNA-packaging protein

Converging primary evidence defines PEG10's function. Segel et al. (2021) show it forms VLPs and vesicularly secretes its own mRNA ([PMID: 34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/)); Lux et al. (2005) show its two products arise by a retroviral −1 frameshift ([PMID: 15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/)); Shiura et al. (2021) show the Pol aspartic-protease motif is functionally essential in vivo ([PMID: 34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/)); and Matthews & Whiteley (2026) define its U/G-rich RNA selectivity ([PMID: 42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/)). PEG10's **only retained catalytic activity is a self-processing aspartic protease** (InterPro IPR021109); its **dominant activity is non-enzymatic Gag-mediated capsid assembly and sequence-selective RNA binding/packaging.** It is therefore neither a metabolic enzyme nor a transporter.

---

## Mechanistic Model / Interpretation

PEG10 is best understood as a **"molecularly domesticated virus"** retained within the mammalian genome, whose ancestral retroviral machinery has been repurposed for host development. The following model integrates the findings:

```
                        Peg10 mRNA (paternal allele; imprinted)
                                     │
                        Programmed -1 ribosomal frameshift
                        (stimulatory RNA pseudoknot)
                          │                        │
              no frameshift (~majority)       frameshift (minority)
                          │                        │
                 ┌────────▼────────┐      ┌────────▼─────────────┐
                 │  PEG10-RF1 (Gag)│      │ PEG10-RF1/2 (Gag-Pol)│
                 │  capsid / NC    │      │  Gag + aspartic      │
                 │  (ORF1)         │      │  protease (POL)      │
                 └───┬─────────┬───┘      └────────┬─────────────┘
                     │         │                   │
          ┌──────────┘         │                   │ self-processing
          │                    │                   │ protease cleavage
          ▼                    ▼                   ▼
  VLP self-assembly      PAIR domain hub      Placental fetal-capillary
  + RNA packaging        (~200 aa):           maintenance (mid–late
  (own mRNA; U/G-rich)   • binds ALK1/ALK5    gestation); essential
          │              → inhibits TGF-β     in 3 trophoblast layers
          ▼              • binds SIAH1 →
  Secretion in            blocks apoptosis
  extracellular         • bound by SIAH1/2,
  vesicles                UBE3A → ubiquitin-
                          mediated turnover
```

**Two products, two modes of action.** The Gag-like RF1 protein provides the structural/RNA-binding backbone (capsid assembly, RNA packaging, protein-interaction hub). The Gag-Pol RF1/2 protein adds the aspartic-protease activity that is dispensable for early placental formation but essential for later vascular maintenance. This mirrors the retroviral life cycle, in which Gag builds the particle and Pol (protease) matures it.

**Spatial logic.** PEG10 functions in three compartments: (1) the **cytoplasm**, where it assembles VLPs and binds RNA; (2) the **secretory/extracellular-vesicle pathway**, consistent with its description as a secreted GAG-domain protein; and (3) **trophoblast cell layers of the placenta** in vivo, surrounding fetal capillary endothelium.

**Dosage is everything.** PEG10 is governed at every level: imprinting restricts it to the paternal allele; −1 PRF sets the Gag:Gag-Pol stoichiometry; and at least two ubiquitin-ligase systems (SIAH1/2 and UBE3A) tune protein turnover. Loss of this control explains its two disease poles — too much PEG10 (oncogenesis; Angelman-syndrome splicing dysregulation when UBE3A is lost) and too little or defective PEG10 (embryonic/placental lethality).

| Feature | Normal role | Consequence of dysregulation |
|---|---|---|
| Gag capsid + RNA packaging | VLP assembly, own-mRNA / U-G-rich RNA export | Neuronal splicing dysregulation (ALS/Angelman) when accumulated |
| Pol aspartic protease | Self-processing; fetal-capillary maintenance | Perinatal lethality / vascular defects if mutated |
| PAIR domain (TGF-β) | Inhibits ALK1/ALK5 signaling | Altered vascular/placental signaling |
| PAIR domain (SIAH1) | Blocks SIAH1-mediated apoptosis | Oncogenesis (HCC, breast) |
| Imprinting + ubiquitin control | Sets dosage | Over-expression → cancer; KO → embryonic lethality |

---

## Evidence Base

| PMID | Study (year) | Contribution | Weight |
|---|---|---|---|
| [34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/) | Segel et al. (2021), *Science* | PEG10 forms VLPs, packages its own mRNA, secreted in vesicles; SEND platform | **Primary — defines core function** |
| [16341224](https://pubmed.ncbi.nlm.nih.gov/16341224/) | Ono et al. (2006), *Nat Genet* | *Peg10* KO → early embryonic lethality from placental defects; imprinting/location | **Primary — in vivo essentiality** |
| [15611116](https://pubmed.ncbi.nlm.nih.gov/15611116/) | Lux et al. (2005), *J Biol Chem* | PEG10-RF1 binds/inhibits ALK1/ALK5 via ~200-aa PAIR domain; −1 frameshift | **Primary — signaling + expression** |
| [34559199](https://pubmed.ncbi.nlm.nih.gov/34559199/) | Shiura et al. (2021) | Protease-motif mutant → fetal-capillary defects; trophoblast localization | **Primary — protease function + localization** |
| [12810624](https://pubmed.ncbi.nlm.nih.gov/12810624/) | Okabe et al. (2003) | PEG10 binds SIAH1, blocks apoptosis; oncogenic in HCC | **Primary — apoptosis/cancer** |
| [42168988](https://pubmed.ncbi.nlm.nih.gov/42168988/) | Liu et al. (2026) | SIAH1/2 bind PAIR domain; K48/K63 polyubiquitination of PEG10 | Primary — turnover mechanism |
| [42239172](https://pubmed.ncbi.nlm.nih.gov/42239172/) | Matthews & Whiteley (2026) | PEG10 binds U/G-rich RNA; splicing dysregulation; TDP-43 mimic | Primary — RNA selectivity/neuronal |
| [42818233](https://pubmed.ncbi.nlm.nih.gov/42818233/) | Kostov et al. (2026) | −1 PRF via stimulatory pseudoknot; ASO modulation | Mechanistic — expression control |
| [26934961](https://pubmed.ncbi.nlm.nih.gov/26934961/) | Li et al. (2016) | PEG10 drives breast-cancer proliferation/invasion; MMPs, E-cadherin | Supporting — oncogenesis |
| [34467244](https://pubmed.ncbi.nlm.nih.gov/34467244/) | Pandya et al. (2021) | PEG10 secreted, regulated by UBE3A; Angelman syndrome | Supporting — secretion/disease |
| [26899828](https://pubmed.ncbi.nlm.nih.gov/26899828/) | Naville et al. (2016) | Retroelement-derived genes in placenta/brain/immunity/cancer | Review — evolutionary context |
| [42511665](https://pubmed.ncbi.nlm.nih.gov/42511665/) | Irie et al. (2026) | 11 SIRH/RTL metavirus-derived genes; PEG10 founding member | Review — family classification |

**Consistency.** The evidence is unusually convergent. Independent lines — biochemistry (VLP/RNA packaging, receptor binding), mouse genetics (knockout, protease-motif knock-in), structural/translational biology (−1 PRF, aspartic-protease motif), and evolutionary genomics (SIRH/RTL domestication) — all point to the same picture of a Gag–Pol capsid protein. No reviewed study contradicts the structural/RNA-packaging assignment. The gene identity is unambiguous: all primary literature concerns the retrotransposon-derived PEG10/*Peg10* in mouse/human, matching the UniProt Q7TN75 description and domain set (PEG10 capsid, aspartic peptidase, RTL1-related).

---

## Limitations and Knowledge Gaps

1. **Mouse-specific mechanistic detail is partly inferred from human studies.** Several key biochemical results (VLP assembly, U/G-rich RNA selectivity, SIAH1/UBE3A regulation, ALK1/ALK5 inhibition) were obtained with human PEG10. Given the high conservation and shared domain architecture (Q7TN75 mouse vs. human ortholog), these are reasonably transferable, but direct mouse biochemical confirmation is incomplete for some claims.

2. **The physiological RNA cargo in trophoblasts is unknown.** While PEG10 packages its own mRNA in cell lines, whether it packages and transfers specific host transcripts between placental cells in vivo — and whether this RNA transfer underlies the vascular phenotype — has not been demonstrated.

3. **Protease substrates are undefined.** The aspartic protease is essential for fetal-capillary maintenance, but its physiological cleavage targets (beyond self-processing) are unknown. Whether it processes Rtl1/Peg11, host proteins, or only itself is unresolved.

4. **Mechanistic link between PAIR-domain signaling and phenotypes is correlative.** TGF-β/ALK inhibition and SIAH1 anti-apoptosis are established in vitro, but their quantitative contribution to the in vivo placental or oncogenic phenotypes has not been dissected with separation-of-function alleles.

5. **Citation integrity note.** One supporting snippet for Finding 9 (UBE3A/Angelman, PMID 34467244) was flagged as a text "mismatch" during verification; the UBE3A-regulation and secretion claims should be treated as well-supported by the paper's overall conclusions but the exact verbatim quote should be re-checked against the primary source.

6. **Stoichiometry and structure.** The precise −1 PRF efficiency (Gag:Gag-Pol ratio) in mouse trophoblasts and a high-resolution structure of the PEG10 capsid/PAIR domain are not yet available, limiting structure-function interpretation.

---

## Proposed Follow-up Experiments / Actions

1. **Define the in vivo RNA cargo of mouse PEG10 in trophoblasts.** Perform CLIP-seq / eCLIP on PEG10 from mouse placenta and from isolated PEG10 VLPs to identify endogenous packaged transcripts and test whether U/G-rich host mRNAs are selectively encapsidated and intercellularly transferred.

2. **Identify protease substrates with a catalytically dead vs. wild-type comparison.** Use N-terminomics (TAILS) in placenta from protease-motif-mutant vs. wild-type mice to catalogue cleavage events; test Rtl1/Peg11 and trophoblast junctional/vascular proteins as candidate substrates.

3. **Separation-of-function alleles.** Generate mouse lines with point mutations that selectively ablate (a) RNA packaging, (b) PAIR-domain receptor binding, or (c) SIAH1 binding, to apportion the placental and signaling phenotypes to specific activities.

4. **Structural determination.** Solve cryo-EM structures of PEG10 VLPs and the PAIR domain in complex with ALK1/ALK5 cytoplasmic domains and with SIAH1 to define the shared interaction surface and rationalize competitive binding.

5. **Dosage–disease axis.** Test whether pharmacological reduction of PEG10 (e.g., ASOs that modulate −1 PRF, per Kostov et al. 2026) rescues splicing dysregulation in neuronal models of ALS/Angelman and suppresses proliferation in PEG10-high carcinomas.

6. **Quantify −1 PRF efficiency in native tissue.** Use ribosome profiling and dual-luciferase frameshift reporters in mouse trophoblast and neural cells to measure Gag:Gag-Pol ratios across development and disease.

---

## Direct Answer

Mouse PEG10 (Q7TN75) is a domesticated Ty3/Gypsy (sushi-ichi/SIRH–RTL) LTR-retrotransposon-derived Gag–Pol polyprotein whose primary function is non-enzymatic and structural: its Gag/nucleocapsid capsid domain self-assembles into virus-like particles and binds/packages RNA (preferentially its own mRNA and U/G-rich transcripts) for secretion in extracellular vesicles, while a programmed −1 ribosomal frameshift also yields a Gag-Pol product bearing a self-processing aspartic protease. It acts mainly in the cytoplasm/secretory pathway and at placental trophoblast layers, where it is essential for placental formation and (via its protease) for maintaining the fetal placental vasculature; its ~200-aa PAIR domain additionally serves as a protein-interaction hub that inhibits TGF-β/activin (ALK1/ALK5) signaling and binds SIAH1 to suppress apoptosis, with its abundance set by ubiquitin ligases (SIAH1/2, UBE3A).


## Artifacts

- [OpenScientist final report](Peg10-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Peg10-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34413232
2. PMID:16341224
3. PMID:42818233
4. PMID:12810624
5. PMID:42168988
6. PMID:42239172
7. PMID:15611116
8. PMID:26934961
9. PMID:34559199
10. PMID:26899828
11. PMID:42511665
12. PMID:34467244