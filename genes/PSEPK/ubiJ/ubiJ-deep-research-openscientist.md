---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T18:07:21.472350'
end_time: '2026-07-18T18:33:15.283097'
duration_seconds: 1553.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiJ
  gene_symbol: ubiJ
  uniprot_accession: Q88D16
  protein_description: 'RecName: Full=Ubiquinone biosynthesis accessory factor UbiJ
    {ECO:0000256|HAMAP-Rule:MF_02215};'
  gene_info: Name=ubiJ {ECO:0000256|HAMAP-Rule:MF_02215}; OrderedLocusNames=PP_5012
    {ECO:0000313|EMBL:AAN70578.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiJ family. {ECO:0000256|HAMAP-
  protein_domains: SCP2_sterol-bd_dom. (IPR003033); SCP2_sterol-bd_dom_sf. (IPR036527);
    UbiJ. (IPR038989); SCP2 (PF02036)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiJ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D16
- **Protein Description:** RecName: Full=Ubiquinone biosynthesis accessory factor UbiJ {ECO:0000256|HAMAP-Rule:MF_02215};
- **Gene Information:** Name=ubiJ {ECO:0000256|HAMAP-Rule:MF_02215}; OrderedLocusNames=PP_5012 {ECO:0000313|EMBL:AAN70578.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiJ family. {ECO:0000256|HAMAP-
- **Key Domains:** SCP2_sterol-bd_dom. (IPR003033); SCP2_sterol-bd_dom_sf. (IPR036527); UbiJ. (IPR038989); SCP2 (PF02036)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiJ** (gene ID: ubiJ, UniProt: Q88D16) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: UbiJ (Q88D16, PP_5012) — *Pseudomonas putida* KT2440

**Gene symbol:** *ubiJ* (OrderedLocusName PP_5012)
**UniProt accession:** Q88D16
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Protein family:** UbiJ family (HAMAP MF_02215); N-terminal SCP2 sterol-carrier domain (Pfam PF02036; InterPro IPR003033, IPR036527, IPR038989)

---

## Summary

UbiJ (Q88D16, PP_5012) is a **non-enzymatic accessory/scaffold protein of the ubiquinone (coenzyme Q, UQ) biosynthesis pathway**. Its primary function is not catalysis but **lipid carriage and metabolon assembly**: its N-terminal SCP2 (sterol carrier protein 2) domain forms an extended hydrophobic cavity that binds the water-insoluble polyisoprenoid tails of ubiquinone biosynthetic intermediates, keeping these highly lipophilic molecules soluble and accessible while the pathway's enzymes chemically modify their aromatic head groups. Through this activity, UbiJ acts as the central **structural scaffold of a soluble, cytoplasmic ~1-MDa multienzyme "Ubi metabolon"** that carries out the terminal reactions of UQ synthesis. This mechanistic picture is derived from detailed biochemical, genetic and structural studies of the *Escherichia coli* and *Salmonella* orthologs and is transferred to *P. putida* on the basis of conserved gene synteny, matching domain architecture, and structural modelling.

Genetically, UbiJ is **globally required for aerobic (O₂-dependent) ubiquinone biosynthesis**. Deletion of *ubiJ* in *E. coli*/*Salmonella* blocks Q₈ synthesis and impairs aerobic growth, with mutants accumulating the early intermediate octaprenylphenol — a signature that UbiJ is needed for the pathway as a whole rather than for a single enzymatic step. Notably, UbiJ is **dispensable anaerobically**, because a paralogous SCP2 protein, UbiT, supplies the equivalent lipid-carrier function for the distinct O₂-independent branch of UQ biosynthesis. UbiJ's C-terminal coiled-coil binds the accessory factor UbiK to form a **UbiJ–UbiK₂ heterotrimer** that tethers the otherwise soluble metabolon to the inner membrane, providing the physical interface for uptake of the membrane-embedded prenylated substrate and release of the finished UQ into the lipid bilayer.

For the specific target, *P. putida* KT2440 UbiJ is a 207-residue cytoplasmic protein with an N-terminal SCP2 domain (residues ~14–111) and a C-terminal coiled-coil (residues ~173–207) — exactly the two-module architecture of functional *E. coli* UbiJ. It resides in a conserved **ubiE–ubiJ–ubiB operon** (PP_5011–PP_5012–PP_5013), its partner UbiK is encoded elsewhere on the genome (PP_5235), and no O₂-independent pathway factors (UbiT/UbiU/UbiV) are annotated in this obligate aerobe. UbiJ is therefore effectively the **sole SCP2 lipid-carrier accessory factor for UQ-9 biosynthesis in *P. putida***. All *P. putida*-specific claims are inference-by-orthology; no direct biochemical characterization of PP_5012 itself has been published.

---

## Key Findings

### 1. UbiJ is an SCP2-domain lipid-binding protein that sequesters hydrophobic UQ intermediates

The defining biochemical activity of UbiJ is **lipid binding through its SCP2 domain**. UbiJ carries an N-terminal SCP2 (sterol carrier protein 2) sterol-binding domain (Pfam PF02036; InterPro IPR003033/IPR036527), a fold that in many proteins forms an interior hydrophobic tunnel for binding sterols, fatty acids, and other lipids. In UbiJ this domain forms an **extended hydrophobic cavity that binds ubiquinone biosynthetic intermediates**. Hajj Chehade et al. (2019) demonstrated this directly by mass spectrometry of the purified Ubi complex, showing that the intermediates are physically held within the UbiJ SCP2 cavity ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)). This is the mechanistic crux of UbiJ's function: UQ intermediates carry a long polyisoprenoid tail (octaprenyl in *E. coli*, nonaprenyl/UQ-9 in *P. putida*) that makes them essentially insoluble in water. By enclosing this tail, UbiJ solubilizes the intermediates in the cytoplasm and presents their aromatic head groups to the modifying enzymes.

> *"The SCP2 domain of UbiJ forms an extended hydrophobic cavity that binds UQ intermediates inside the 1-MDa Ubi complex."* — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)

### 2. UbiJ is the scaffolding subunit of a soluble ~1-MDa Ubi metabolon that performs cytoplasmic ubiquinone biosynthesis

UbiJ does not act alone; it is a core structural component of a large multienzyme assembly. Hajj Chehade et al. (2019) showed that **seven Ubi proteins form a stable ~1-MDa metabolon** ("Ubi complex") that catalyzes the last six reactions of the UQ biosynthetic pathway in *E. coli* ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)). Critically, the same study purified this complex from **cytoplasmic (soluble) extracts** and demonstrated that UQ biosynthesis occurs in this fraction — overturning the long-standing assumption that UQ biosynthesis is an inner-membrane–bound process. UbiJ's lipid-carrier role is what makes soluble, cytoplasmic biosynthesis of an extremely hydrophobic product feasible: it shields the lipid tails from the aqueous environment while the enzymes work on the head group.

> *"we demonstrate that seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in Escherichia coli"* — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)

> *"We purify the Ubi complex from cytoplasmic extracts and demonstrate that UQ biosynthesis occurs in this fraction, challenging the current thinking of a membrane-associated biosynthetic process."* — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)

### 3. UbiJ forms a UbiJ–UbiK₂ heterotrimer and is globally required for aerobic UQ biosynthesis

The accessory factor **UbiK binds the C-terminal part of UbiJ**, forming a **UbiJ–UbiK₂ heterotrimer** within the metabolon (Loiseau et al., 2017; [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)). Genetically, loss of either *ubiJ* or *ubiK* blocks UQ synthesis globally, and the mutants accumulate **octaprenylphenol**, an early intermediate of the pathway. This accumulation pattern is diagnostic: it indicates the factors are needed for the pathway as a whole (an assembly/scaffold role) rather than for a single downstream enzymatic step. Importantly, both proteins are **dispensable under anaerobiosis** even though they are expressed without oxygen — establishing that UbiJ is specifically required for the **aerobic, O₂-dependent branch** of UQ biosynthesis. Because *P. putida* is an obligate aerobe that relies on ubiquinone (UQ-9) respiration, this aerobic role is directly physiologically relevant to the target organism.

> *"the UbiK protein forms a complex with the C-terminal part of UbiJ, another UQ biogenesis factor we previously identified"* — [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)

> *"both proteins are likely to contribute to global UQ biosynthesis rather than to a specific biosynthetic step, because both ubiK and ubiJ mutants accumulated octaprenylphenol, an early intermediate of the UQ biosynthetic pathway"* — [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)

> *"both proteins are dispensable for UQ biosynthesis under anaerobiosis, even though they were expressed in the absence of oxygen"* — [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)

### 4. UbiJ binds membrane lipids; the UbiJ–UbiK₂ complex tethers the soluble metabolon to the membrane

Although the metabolon is soluble, it must interface with the inner membrane both to acquire its lipophilic substrate and to deposit finished UQ. Loiseau et al. (2017) showed the **UbiK–UbiJ complex interacts with palmitoleic acid**, a major membrane lipid of *E. coli* ([PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)). Building on this, Launay et al. (2022) used multiscale molecular modelling of the UbiJ–UbiK₂ heterotrimer to show that it **interacts closely with the membrane** and likely provides the physical interface between the membrane and the soluble Ubi enzymes, offering a route to **release newly made UQ into the membrane** ([PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)). The same modelling work reinforced that the SCP2 domain of UbiJ binds the **hydrophobic polyisoprenoid tail** of UQ intermediates.

> *"the UbiK-UbiJ complex interacts with palmitoleic acid, a major lipid in E. coli"* — [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)

> *"UbiJ-UbiK2 interacts closely with the membrane and suggests possible pathways to enable the release of UQ into the membrane"* — [PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)

> *"The SCP2 domain of UbiJ was proposed to bind the hydrophobic polyisoprenoid tail of UQ biosynthetic intermediates in the Ubi metabolon"* — [PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)

### 5. *P. putida* PP_5012 sits in a conserved ubiE–ubiJ–ubiB operon with a domain architecture matching functional *E. coli* UbiJ

Direct examination of UniProt/genomic records for the target confirms the orthology. Q88D16 is a **207-amino-acid cytoplasmic protein** with an N-terminal SCP2 sterol-carrier domain (residues ~14–111) and a C-terminal coiled-coil (residues ~173–207) — precisely the two functional modules of *E. coli* UbiJ (an SCP2 lipid cavity plus a C-terminal UbiK-oligomerization region). Its genomic neighborhood is **syntenic with *E. coli***: PP_5011 = *ubiE* (a C-methyltransferase), PP_5012 = *ubiJ*, and PP_5013 = *ubiB* — the conserved **ubiE–ubiJ–ubiB operon**. *P. putida* KT2440 encodes a complete Ubi pathway and uses ubiquinone (UQ-9) for aerobic respiration. This makes the functional transfer from the well-characterized *E. coli* ortholog robust. The conserved SCP2 module whose activity is characterized in *E. coli* ([PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)) corresponds directly to the SCP2 domain identified in the *P. putida* protein.

### 6. Original genetic characterization: *ubiJ* (formerly *yigP*) is required for aerobic coenzyme Q biosynthesis, and its lipid-interacting C-terminus is sufficient to restore function

Aussel et al. (2014) provided the foundational genetics. They showed that the previously uncharacterized gene *yigP* — located between *ubiE* and *ubiB* in a probable operon — is **required for Q₈ biosynthesis in both *E. coli* and *Salmonella***, and renamed it *ubiJ* ([PMID: 24142253](https://pubmed.ncbi.nlm.nih.gov/24142253/)). Under aerobic conditions, an *ubiJ* mutant was impaired for Q₈ biosynthesis and for growth in rich medium but showed **no anaerobic defect**. Remarkably, the **C-terminal ~50 amino acids**, predicted to interact with lipids, were **sufficient to restore** Q₈ biosynthesis and growth — direct structure–function evidence that the lipid-interacting portion of the protein is a critical functional element. An authoritative review (Abby et al., 2020, BBA Bioenergetics, [PMID: 32663475](https://pubmed.ncbi.nlm.nih.gov/32663475/)) later situated UbiJ within the supramolecular organization (metabolon) of the bacterial UQ pathway.

> *"we showed that the uncharacterized yigP gene was involved in Q8 biosynthesis in both strains, and we have renamed it ubiJ"* — [PMID: 24142253](https://pubmed.ncbi.nlm.nih.gov/24142253/)

> *"Under aerobic conditions, an ubiJ mutant was found to be impaired for Q8 biosynthesis and for growth in rich medium but did not present any defect anaerobically"* — [PMID: 24142253](https://pubmed.ncbi.nlm.nih.gov/24142253/)

> *"the C-terminal 50 amino acids, predicted to interact with lipids, were sufficient to restore Q8 biosynthesis and growth of the ubiJ mutant"* — [PMID: 24142253](https://pubmed.ncbi.nlm.nih.gov/24142253/)

(Note: in *E. coli* the *yigP/ubiJ* locus also encodes an overlapping 3′-UTR small RNA, EsrE, a γ-proteobacterial feature — Xia 2017, [PMID: 28900423](https://pubmed.ncbi.nlm.nih.gov/28900423/); Tang 2019, [PMID: 31553492](https://pubmed.ncbi.nlm.nih.gov/31553492/). The UbiJ *protein* is the factor indispensable for UQ synthesis.)

### 7. AlphaFold structural inference: a confidently folded, hydrophobic SCP2 module and a low-confidence oligomerization C-terminus

Analysis of the AlphaFold model of the target (AF-Q88D16-F1, 207 aa; global pLDDT 63.9) is consistent with the two-module functional model. The **N-terminal SCP2 domain (residues 14–111) is the confidently modelled core** (mean pLDDT 75.9) and is **enriched in hydrophobic residues** (50% A/V/L/I/M/F/C; mean Kyte–Doolittle hydropathy +0.31 vs −0.07 for the whole chain) — exactly what is expected for an SCP2 fold that encloses an interior hydrophobic cavity for a polyisoprenoid tail. In contrast, the middle region (112–172) and the C-terminal coiled-coil (173–207) are modelled with **low confidence (pLDDT ~51)**, as expected for a segment whose ordered structure forms only upon oligomerization with UbiK rather than in the isolated monomer. This structural inference links the confidently folded hydrophobic SCP2 domain to its proposed lipid-tail-binding function ([PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)).

### 8. UbiJ is the SCP2 factor specifically of the O₂-dependent pathway; UbiT serves the O₂-independent pathway

Pelosi et al. (2019) characterized a conserved **O₂-independent ubiquinone biosynthesis pathway** operating alongside the classical O₂-dependent one, relying on the factors UbiT, UbiU and UbiV. Crucially, **UbiT contains an SCP2 lipid-binding domain and is an accessory factor** analogous to UbiJ, while UbiU–UbiV are a novel class of O₂-independent hydroxylases ([PMID: 31289180](https://pubmed.ncbi.nlm.nih.gov/31289180/)). UbiT is thus a **paralog of UbiJ** that supplies the SCP2 lipid-carrier function under anaerobiosis, whereas UbiJ supplies it for the aerobic pathway. This elegantly explains the phenotype seen by Aussel (2014) and Loiseau (2017): *ubiJ* deletion impairs UQ synthesis aerobically but not anaerobically because, under low O₂, the paralogous factor UbiT substitutes. These factors are distributed across alpha-, beta- and gammaproteobacteria.

> *"UbiT contains an SCP2 lipid-binding domain and is likely an accessory factor of the biosynthetic pathway, while UbiU and UbiV (UbiU-UbiV) are involved in hydroxylation reactions and represent a novel class of O2-independent hydroxylases"* — [PMID: 31289180](https://pubmed.ncbi.nlm.nih.gov/31289180/)

### 9. *P. putida* KT2440 encodes UbiK (PP_5235) but lacks O₂-independent factors, making UbiJ the sole SCP2 accessory factor for its UQ biosynthesis

A UniProt search of the *P. putida* KT2440 reference proteome (organism_id 160488) confirms that the **UbiJ partner UbiK is present as PP_5235** (Q88CE6, "Ubiquinone biosynthesis accessory factor UbiK"), located separately from the *ubiE–ubiJ–ubiB* operon — mirroring *E. coli*, where *ubiK*/*yqiC* is likewise not in the *ubiEJB* operon. Critically, **no genes annotated as *ubiT*, *ubiU*, or *ubiV*** (the O₂-independent pathway factors) were found in the KT2440 proteome. This absence fits the obligately aerobic physiology of *P. putida* and leaves **UbiJ as the sole SCP2 accessory factor** available for its UQ-9 biosynthesis.

---

## Mechanistic Model / Interpretation

UbiJ is best understood as a **lipid chaperone and structural organizer** that makes it possible to run the chemistry of an intensely hydrophobic biosynthetic pathway in the aqueous cytoplasm. The following model synthesizes the findings:

```
                    INNER MEMBRANE (lipid bilayer, UQ-9 pool)
   ================================================================
        ▲  UQ-9 released                     octaprenyl/nonaprenyl-PHB
        │  into membrane                      substrate acquired
        │                                            │
   -----│-------------------- UbiJ–UbiK2 ------------│------------
        │                    (membrane tether)       │
        │                                             ▼
   ┌───────────────────────────────────────────────────────────┐
   │   SOLUBLE ~1-MDa Ubi METABOLON  (cytoplasm)                │
   │                                                            │
   │   UbiE  UbiF  UbiG  UbiH  UbiI ...  (catalytic enzymes)    │
   │        \      |      |     /                               │
   │         \     |      |    /   head-group modifications     │
   │          ┌──────────────────┐                             │
   │          │  UbiJ SCP2 cavity │ ← binds polyisoprenoid TAIL │
   │          │  (holds lipid     │   keeping intermediate      │
   │          │   tail of intermediate) soluble & positioned    │
   │          └──────────────────┘                             │
   │             |         C-terminal coiled-coil               │
   │             └──────── binds UbiK2 (heterotrimer) ──────────┘
   └───────────────────────────────────────────────────────────┘
```

**Division of labor within the two modules of UbiJ:**

| Module | Residues (P. putida) | Structure | Function |
|---|---|---|---|
| N-terminal SCP2 domain | ~14–111 | Confidently folded hydrophobic cavity (pLDDT 75.9) | Binds the polyisoprenoid tail of UQ intermediates; keeps them soluble and presented to enzymes |
| Middle + C-terminal coiled-coil | ~112–207 | Low-confidence in monomer (pLDDT ~51); ordered upon oligomerization | Binds UbiK to form UbiJ–UbiK₂ heterotrimer; membrane/lipid interaction; C-terminal ~50 aa sufficient to restore function in E. coli |

**Why this architecture matters:** UQ biosynthesis modifies the aromatic head group of a molecule whose tail is a long, membrane-partitioning polyprenyl chain. Free intermediates would either aggregate or partition irreversibly into the membrane. By threading the tail into the SCP2 cavity, UbiJ converts an intractable lipid into a "soluble" substrate that the metabolon enzymes can process in sequence — a classic substrate-channeling/metabolon logic. The UbiJ–UbiK₂ module then docks this soluble factory onto the membrane to receive prenylated starting material and off-load finished UQ-9 into the respiratory quinone pool.

**Localization:** cytoplasm (soluble metabolon), with the UbiJ–UbiK₂ module providing a peripheral interface to the cytoplasmic face of the inner membrane. This is where UbiJ performs its function.

**Pathway placement:** UbiJ acts across the **last six (terminal) reactions of the O₂-dependent aerobic UQ biosynthetic pathway**, not at a single step — consistent with mutants accumulating an *early* intermediate (octaprenylphenol) when the scaffold is lost.

---

## Evidence Base

| PMID | Paper (abbreviated) | How it supports the annotation |
|---|---|---|
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | *A Soluble Metabolon Synthesizes the Isoprenoid Lipid Ubiquinone* | Direct MS evidence that UbiJ's SCP2 domain binds UQ intermediates; defines the ~1-MDa cytoplasmic Ubi metabolon; localizes UQ biosynthesis to the soluble fraction. Foundation for Findings 1, 2, 5. |
| [28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/) | *The UbiK protein… forms a complex with UbiJ* (Loiseau et al. 2017) | Defines UbiJ–UbiK₂ heterotrimer via UbiJ C-terminus; shows global (whole-pathway) role via octaprenylphenol accumulation; establishes aerobic-specific requirement; membrane-lipid (palmitoleic acid) binding. Findings 3, 4. |
| [36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/) | *Towards Molecular Understanding of… UbiJ-UbiK* (Launay et al. 2022) | Multiscale modelling: UbiJ–UbiK₂ is the membrane interface enabling UQ release; SCP2 binds the polyisoprenoid tail. Findings 4, 7. |
| [24142253](https://pubmed.ncbi.nlm.nih.gov/24142253/) | *ubiJ, a new gene required for aerobic growth…* (Aussel et al. 2014) | Original genetics: yigP→ubiJ required for Q₈; aerobic-only defect; lipid-interacting C-terminal 50 aa sufficient to restore function. Finding 6. |
| [31289180](https://pubmed.ncbi.nlm.nih.gov/31289180/) | *O₂-independent UQ pathway (UbiT/UbiU/UbiV)* (Pelosi et al. 2019) | Identifies UbiT as the SCP2 accessory factor of the anaerobic pathway — the paralog of UbiJ — explaining UbiJ's aerobic specificity. Findings 8, 9. |

**Supporting context.** The review by Abby et al. (2020, BBA Bioenergetics; [PMID: 32663475](https://pubmed.ncbi.nlm.nih.gov/32663475/)) places UbiJ within the supramolecular metabolon of the bacterial UQ pathway. Taxonomic quinone surveys confirm *P. putida* uses UQ-9 as its respiratory quinone (e.g., [PMID: 11359512](https://pubmed.ncbi.nlm.nih.gov/11359512/), [PMID: 18323682](https://pubmed.ncbi.nlm.nih.gov/18323682/)), reinforcing the physiological relevance of an intact aerobic UQ pathway in this organism. HskA sensor-kinase work ([PMID: 24249291](https://pubmed.ncbi.nlm.nih.gov/24249291/)) shows *P. putida* actively senses ubiquinone redox state, underscoring the importance of UQ homeostasis (and thus UbiJ-dependent UQ supply) in this species.

**Nature of the evidence.** All mechanistic evidence derives from the **E. coli/Salmonella orthologs** (experimental biochemistry and genetics) plus **structural modelling**. Evidence for the *P. putida* protein itself is **bioinformatic/comparative** (synteny, domain architecture, AlphaFold, proteome content), i.e., inference by orthology rather than direct measurement.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_5012.** Every functional claim about *P. putida* UbiJ is inferred from *E. coli*/*Salmonella* orthologs. There are no published *P. putida* KT2440 *ubiJ* knockout phenotypes, no purified PP_5012 lipid-binding assays, and no *P. putida* Ubi-complex isolation.
2. **Substrate identity in *P. putida* is assumed, not measured.** *P. putida* uses UQ-9 (nonaprenyl tail) rather than *E. coli*'s UQ-8. The SCP2 cavity is presumed to accommodate the longer tail, but this has not been experimentally verified.
3. **The metabolon composition may differ.** The exact set of Ubi enzymes assembling with UbiJ in *P. putida*, and whether pathway-specific enzymes (e.g., decarboxylative hydroxylases like the UbiN described in *Rhodobacter*, [PMID: 37716914](https://pubmed.ncbi.nlm.nih.gov/37716914/)) participate, is unknown for this organism.
4. **Structural confidence is partial.** The AlphaFold monomer models the SCP2 domain well but the functionally critical C-terminal coiled-coil poorly; no experimental structure of *P. putida* UbiJ or its UbiK complex exists.
5. **Quantitative binding parameters are unavailable.** Affinities, stoichiometries and selectivity of UbiJ for specific intermediates vs. bulk membrane lipids are not quantified for any ortholog in a way that establishes substrate specificity numerically.
6. **The EsrE sRNA overlap is *E. coli*-specific** and its presence/absence at the *P. putida* locus was not directly resolved here; this does not affect the protein's annotation but is a locus-level caveat.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted *ubiJ* (PP_5012) deletion in *P. putida* KT2440**, followed by HPLC-MS quantification of UQ-9 and detection of accumulated intermediates (predicted: nonaprenylphenol) under aerobic growth — the direct test of the orthology-based annotation.
2. **Complementation and domain-dissection:** test whether the *P. putida* UbiJ C-terminal region alone rescues a Δ*ubiJ* mutant (mirroring Aussel 2014), and whether *E. coli* UbiJ cross-complements, to confirm functional conservation.
3. **Purify PP_5012 and the PP_5012–PP_5235 (UbiJ–UbiK) complex;** use native MS / lipidomics to identify bound isoprenoid intermediates and confirm the SCP2 cavity accommodates the UQ-9 tail.
4. **Isolate the *P. putida* Ubi metabolon** by pulldown of tagged UbiJ and characterize its enzyme composition and molecular mass (test the ~1-MDa metabolon model in this organism).
5. **Cryo-EM / crystallography** of the *P. putida* UbiJ–UbiK₂ complex to resolve the low-confidence coiled-coil and the membrane-interacting surface.
6. **Aerobic vs. microaerobic phenotyping:** confirm UbiJ's aerobic-specific requirement in *P. putida*, and verify (bioinformatically and genetically) the absence of a UbiT-type anaerobic paralog, cementing UbiJ as the sole SCP2 factor.

---

## Conclusion

UbiJ (Q88D16, PP_5012) in *Pseudomonas putida* KT2440 is a **cytoplasmic, non-enzymatic SCP2-domain accessory protein that serves as the lipid-carrier scaffold of the ubiquinone (UQ-9) biosynthetic metabolon**. Its N-terminal SCP2 domain sequesters the polyisoprenoid tails of hydrophobic UQ intermediates, enabling soluble, cytoplasmic biosynthesis, while its C-terminal coiled-coil binds UbiK (PP_5235) to form a UbiJ–UbiK₂ complex that tethers the metabolon to the inner membrane. UbiJ is globally required for the aerobic, O₂-dependent UQ pathway and — given the absence of anaerobic UbiT/UbiU/UbiV factors in this obligate aerobe — is effectively the sole SCP2 lipid-carrier for coenzyme Q synthesis in *P. putida*. The annotation rests on strong orthology to experimentally characterized *E. coli*/*Salmonella* UbiJ plus conserved synteny, domain architecture and structural modelling; direct experimental validation in *P. putida* itself remains to be performed.


## Artifacts

- [OpenScientist final report](ubiJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiJ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30686758
2. PMID:28559279
3. PMID:36142227
4. PMID:24142253
5. PMID:32663475
6. PMID:28900423
7. PMID:31553492
8. PMID:31289180
9. PMID:11359512
10. PMID:18323682
11. PMID:24249291
12. PMID:37716914