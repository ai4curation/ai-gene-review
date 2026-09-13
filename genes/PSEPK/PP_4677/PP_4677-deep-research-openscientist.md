---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:21:03.139741'
end_time: '2026-09-01T16:46:11.661349'
duration_seconds: 1508.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4677
  gene_symbol: PP_4677
  uniprot_accession: Q88DZ1
  protein_description: 'RecName: Full=CDP-diacylglycerol--serine O-phosphatidyltransferase
    {ECO:0000256|ARBA:ARBA00017171}; EC=2.7.8.8 {ECO:0000256|ARBA:ARBA00013174}; AltName:
    Full=Phosphatidylserine synthase {ECO:0000256|ARBA:ARBA00032361};'
  gene_info: OrderedLocusNames=PP_4677 {ECO:0000313|EMBL:AAN70250.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the CDP-alcohol phosphatidyltransferase class-I
  protein_domains: CDP-alcohol_PTase-I. (IPR050324); CDP-diaglyc--ser_O-PTrfase. (IPR004533);
    CDP-OH_P_trans. (IPR000462); CDP-OH_PTrfase_TM_dom. (IPR043130); CDP_ALCOHOL_P_TRANSF_CS.
    (IPR048254)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4677-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4677-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DZ1
- **Protein Description:** RecName: Full=CDP-diacylglycerol--serine O-phosphatidyltransferase {ECO:0000256|ARBA:ARBA00017171}; EC=2.7.8.8 {ECO:0000256|ARBA:ARBA00013174}; AltName: Full=Phosphatidylserine synthase {ECO:0000256|ARBA:ARBA00032361};
- **Gene Information:** OrderedLocusNames=PP_4677 {ECO:0000313|EMBL:AAN70250.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the CDP-alcohol phosphatidyltransferase class-I
- **Key Domains:** CDP-alcohol_PTase-I. (IPR050324); CDP-diaglyc--ser_O-PTrfase. (IPR004533); CDP-OH_P_trans. (IPR000462); CDP-OH_PTrfase_TM_dom. (IPR043130); CDP_ALCOHOL_P_TRANSF_CS. (IPR048254)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4677" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4677' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4677** (gene ID: PP_4677, UniProt: Q88DZ1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_4677 (Q88DZ1): Phosphatidylserine Synthase (PssA) of *Pseudomonas putida* KT2440

## Summary

**PP_4677 (UniProt Q88DZ1) encodes phosphatidylserine synthase (PssA; EC 2.7.8.8), the enzyme that catalyzes the committed, identity-defining step of the de novo pathway to phosphatidylethanolamine (PE) in *Pseudomonas putida* KT2440.** The enzyme transfers the phosphatidyl group of CDP-1,2-diacyl-sn-glycerol (CDP-DAG) onto the hydroxyl of L-serine, releasing CMP and producing 1,2-diacyl-sn-glycero-3-phospho-L-serine (phosphatidylserine, PS) — the reaction catalogued as RHEA:16913. The PS product is subsequently decarboxylated by phosphatidylserine decarboxylase (Psd) to yield PE, which is by far the dominant phospholipid of the *P. putida* membrane (~80% of the total). PssA therefore sits at the head of the highest-flux branch of glycerophospholipid biosynthesis in this organism and is a linchpin of membrane biogenesis and stress-responsive lipid homeostasis.

**Critically, the *P. putida* enzyme belongs to a mechanistically distinct family from the well-studied *Escherichia coli* PssA.** Bioinformatic orthology assigns PP_4677 to KEGG ortholog group K17103 / eggNOG COG1183 / Pfam PF01066 — the integral-membrane **CDP-alcohol phosphotransferase (CDP-AP) class-I superfamily**. This is the same family as archaeal and mycobacterial phosphatidylinositol(-phosphate) synthases whose crystal structures reveal a six-to-eight transmembrane-helix fold with a cytoplasm-facing active site built around a catalytic Mg²⁺ ion coordinated by four conserved aspartates. This contrasts sharply with the enterobacterial (*E. coli*) PssA, which is a peripheral membrane, phospholipase-D-superfamily enzyme (KEGG K00998) that proceeds through a covalent phosphatidyl-enzyme intermediate rather than a metal-dependent direct displacement. Direct sequence analysis of Q88DZ1 confirms the diagnostic CDP-alcohol phosphotransferase (CAPT) signature and identifies the four candidate catalytic aspartates as D95, D98, D116, and D120.

**Localization and topology:** PP_4677 is a polytopic integral protein of the cytoplasmic (inner) membrane, predicted to span the bilayer eight times, with a short disordered N-terminus and a cytoplasm-facing catalytic loop immediately following the second transmembrane helix. It functions at the cytoplasmic leaflet of the inner membrane, drawing L-serine from the cytosol and CDP-DAG from the membrane. An important caveat frames the entire report: **the functional assignment rests on convergent bioinformatic, orthology, and comparative-structural evidence (UniProt evidence level PE=3, inferred from homology). No enzymological or genetic study performed directly on the *P. putida* PP_4677 gene product was found in the literature.** The conclusions below are therefore robust inferences from sequence, domain architecture, and well-characterized homologs, not direct measurements on this specific protein.

---

## Key Findings

### Finding 1: PP_4677 is phosphatidylserine synthase (PssA), catalyzing the committed step toward phosphatidylethanolamine

The UniProt record for Q88DZ1 annotates the protein as **CDP-diacylglycerol—serine O-phosphatidyltransferase (EC 2.7.8.8)**, with the gene name PP_4677. The catalyzed reaction is:

> CDP-1,2-diacyl-sn-glycerol + L-serine → 1,2-diacyl-sn-glycero-3-phospho-L-serine (phosphatidylserine) + CMP + H⁺

This is the first, committed reaction of the de novo route to phosphatidylethanolamine (PE). The phosphatidylserine produced by PssA has no other major metabolic fate in bacteria than to be decarboxylated to PE by phosphatidylserine decarboxylase (Psd/PSD). The physiological importance of this pathway in *P. putida* is underscored by the membrane lipid composition: in *P. putida* KT2442 (a close relative of KT2440), the major phospholipids were measured as **phosphatidylethanolamine (79.9%), phosphatidylglycerol (12.7%), and cardiolipin (7.4%)** [PMID: 26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/). Because PE dominates the membrane at roughly 80% and is produced exclusively via the PS→PE route, the enzyme initiating that route (PssA/PP_4677) operates at very high metabolic flux.

The downstream, obligatory decarboxylation step is well established: "*Phosphatidylethanolamine (PE), a major component of the cellular membrane across all domains of life, is synthesized exclusively by membrane-anchored phosphatidylserine decarboxylase (PSD) in most bacteria*" [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/). This places PP_4677 unambiguously upstream in the PE biosynthetic pathway: PssA makes PS, PSD converts PS to PE.

### Finding 2: PP_4677 belongs to the integral-membrane CDP-alcohol phosphotransferase (CDP-AP) class-I superfamily and uses a Mg²⁺-dependent direct-displacement mechanism

The InterPro domain complement of Q88DZ1 is definitive for the integral-membrane CDP-AP family, comprising:
- **IPR000462** — CDP-alcohol phosphatidyltransferase
- **IPR004533** — CDP-diacylglycerol-serine O-phosphatidyltransferase (the substrate-specific subfamily)
- **IPR043130** — CDP-OH phosphatidyltransferase transmembrane domain
- **IPR048254** — CDP_ALCOHOL_P_TRANSF conserved site
- **IPR050324** — CDP-alcohol phosphatidyltransferase class-I family

The chemistry of this family is conserved and well defined: its members "*share a conserved sequence pattern and catalyse the displacement of CMP from a CDP-alcohol by a second alcohol*" [PMID: 24942835](https://pubmed.ncbi.nlm.nih.gov/24942835/). For PP_4677, the CDP-alcohol donor is CDP-DAG and the acceptor second alcohol is L-serine.

The structural and catalytic paradigm comes from crystallized homologs — the *Archaeoglobus fulgidus* IPCT-DIPPS bifunctional enzyme (PDB 4O6M) and the *Renibacterium salmoninarum* / *Mycobacterium* phosphatidylinositol-phosphate synthases (PIPS). In these, the active site contains "*a magnesium ion surrounded by four highly conserved aspartate residues from helices TM2 and TM3. We show that magnesium is essential for the enzymatic activity and is involved in catalysis*" [PMID: 24942835](https://pubmed.ncbi.nlm.nih.gov/24942835/). A recent review reinforces the family framework, noting "*the CDP-AP protein family which is divided in two classes, defined by different structures and mechanisms*" [PMID: 41308808](https://pubmed.ncbi.nlm.nih.gov/41308808/); PP_4677 falls into InterPro class I.

This mechanistic identity is the report's most important nuance. The extensively studied *E. coli* PssA is **not** a member of this family — it is a phospholipase-D-superfamily peripheral membrane protein that forms a covalent phosphatidyl-enzyme intermediate. Recent crystal structures confirm this distinct enzymology for the enterobacterial enzyme: PssA "*acts on cytidine diphosphate diacylglycerol (CDP-DG) to form cytidine monophosphate and a covalent intermediate, which is subsequently targeted by serine to produce phosphatidylserine*" [PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/). The *P. putida* enzyme, by contrast, is predicted to perform a single-step, Mg²⁺-dependent direct displacement with no covalent intermediate.

### Finding 3: The Q88DZ1 sequence contains the canonical CAPT catalytic motif and predicted transmembrane helices, indicating an inner-membrane enzyme with a cytoplasm-facing active site

Direct analysis of the 283-amino-acid Q88DZ1 sequence located the CDP-alcohol phosphotransferase (CAPT / PROSITE PS00379-type) signature, the aspartate-rich Mg²⁺-coordinating motif diagnostic of the family, beginning near Asp98. Kyte–Doolittle hydropathy analysis and family homology indicate multiple membrane-spanning segments, consistent with the six-TM core of crystallized archaeal/bacterial CAPT enzymes.

The topology (which face of the membrane the active site occupies) is inferred from the experimentally mapped homolog, yeast phosphatidylinositol synthase Pis1. Cysteine-accessibility scanning of Pis1 concluded "*The results clearly point to a cytosolic location of the CAPT motif*" [PMID: 25687304](https://pubmed.ncbi.nlm.nih.gov/25687304/), and further that "*The central 84% of the Pis1 sequence can be aligned and fitted onto the 6 transmembrane helices of two recently crystallized archaeal members of the CAPT family*" [PMID: 25687304](https://pubmed.ncbi.nlm.nih.gov/25687304/). By homology, the shared CAPT active-site motif of PP_4677 faces the cytoplasm — the enzyme collects L-serine from the cytosol and acts on membrane-embedded CDP-DAG at the cytoplasmic leaflet.

### Finding 4: PP_4677/PssA function underlies *P. putida* membrane homeostasis and solvent-stress remodeling

The glycerophospholipid inventory of *P. putida* (PE, PG, cardiolipin) is a conserved, defining feature of the species and its close relatives. A systematic survey found conserved compositions "*within the four investigated pseudomonads P. putida KT2440, DOT-T1E, S12 and Pseudomonas sp. strain VLB120*" [PMID: 21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/). Because PssA supplies PS for PE synthesis, it sits upstream of the PE pool whose abundance is adaptively modulated. Under solvent (e.g., toluene) stress, the long-term adaptive response remodels the membrane so that "*cardiolipin increases and phosphatidylethanolamine decreases*" [PMID: 9020089](https://pubmed.ncbi.nlm.nih.gov/9020089/), rigidifying the bilayer to resist solvent partitioning. PssA activity thus determines the size of the PE reservoir that this stress response acts upon. PE itself is a cone-shaped, non-bilayer-prone zwitterionic lipid that is important for membrane curvature, correct folding and insertion of membrane proteins, and barrier function — properties that make the PssA-fed PE pool central to *P. putida*'s renowned robustness as an industrial and environmental chassis.

### Finding 5: Reaction and orthology of PP_4677 are precisely defined across databases

The catalytic activity is registered as **Rhea RHEA:16913**: "a CDP-1,2-diacyl-sn-glycerol + L-serine = a 1,2-diacyl-sn-glycero-3-phospho-L-serine + CMP + H⁺", EC 2.7.8.8. KEGG catalogues the gene as **ppu:PP_4677**, orthology **K17103** (CDP-diacylglycerol—serine O-phosphatidyltransferase), and places it in module **M00093** "Phosphatidylethanolamine (PE) biosynthesis, PA => PS => PE". The eggNOG orthologous group is **COG1183** (phosphatidylserine synthase), and the Pfam domain is **PF01066** (CDP-alcohol phosphatidyltransferase).

The single most important orthology distinction is that KEGG assigns *P. putida* PssA to **K17103** — the CDP-alcohol-phosphotransferase-type ortholog group — which is a **different** ortholog group from **K00998**, the phospholipase-D-type PssA of *E. coli*. This corroborates at the orthology level the mechanistic distinction inferred structurally in Finding 2. Genomic coordinates: complement(5315081..5315932) on the KT2440 chromosome — an 852-bp ORF encoding a 283-residue protein.

### Finding 6: PP_4677 is a multi-pass inner-membrane protein (8 predicted TM helices) with a disordered cytoplasmic N-terminus, encoded by a standalone gene not embedded in a lipid-synthesis operon

UniProt annotates Q88DZ1 as a **multi-pass membrane protein** with eight predicted transmembrane helices (approximately residues 40–60, 80–97, 118–137, 143–161, 173–193, 205–224, 236–252, 258–276) plus a disordered/charged N-terminal region (residues ~1–20). The CAPT catalytic aspartate (Asp98) lies in the cytoplasmic loop immediately after TM2.

The AlphaFold model (AF-Q88DZ1, v6) supports this architecture: mean pLDDT 78.3 overall; the transmembrane core (residues 30–276) is confidently modeled as a compact helical bundle (mean pLDDT 82.5); the CAPT region (residues 95–120) is 79.7; and the N-terminus (residues 1–24) is low-confidence (45.0), consistent with the annotated disorder. Genomic context shows the gene is not part of a phospholipid-synthesis operon — immediate neighbors are functionally unrelated: PP_4675–PP_4676 encode methionine sulfoxide reductase MsrPQ (K17247/K07147) and PP_4678–PP_4679 encode branched-chain amino acid biosynthesis IlvC/IlvH (K00053/K01653). No adjacent phospholipid-metabolism gene (e.g., *psd*) is present, indicating standalone transcriptional organization.

### Finding 7: Residue-level catalytic center — four conserved aspartates (D95, D98, D116, D120) form the Mg²⁺-coordinating CAPT motif

Direct mapping of the Q88DZ1 sequence identifies the complete PROSITE PS00379-type CDP-alcohol phosphotransferase signature spanning residues 95–120:

> **D95**-G-L-**D98**-G-R-V-A-R-M-T-N-T-Q-S-A-F-G-A-E-Y-**D116**-S-L-S-**D120**

This contains the two canonical "aspartate boxes": the first box **D95/D98** (D-x-x-D-G) and the second box **D116/D120** (D-x-x-x-D). These four aspartates align with the quartet that, in the crystallized homologs (*A. fulgidus* IPCT-DIPPS, PDB 4O6M; *Renibacterium*/*Mycobacterium* PIPS), project from transmembrane helices TM2/TM3 to coordinate the essential catalytic Mg²⁺ ion. This center lies in the cytoplasm-facing loop immediately following TM2 (residues ~80–97), consistent with the cytosolic-active-site topology established for the homologous Pis1.

---

## Mechanistic Model / Interpretation

### The reaction and its pathway context

```
   Fatty acid / PA synthesis
              │
              ▼
        CDP-DAG  ──────────────┐ (CdsA, K00981)
              │                │
   L-serine   │                │  (from cytosol)
        \     │                │
         \    ▼                ▼
   ┌─────────────────────────────────────┐
   │   PssA  =  PP_4677 / Q88DZ1          │   ← THIS ENZYME
   │   EC 2.7.8.8  (RHEA:16913)           │
   │   CDP-AP class-I, K17103, COG1183    │
   │   Mg2+-dependent, 8-TM, inner mem.   │
   └─────────────────────────────────────┘
              │
              ▼
   Phosphatidylserine (PS) + CMP
              │
              ▼  Psd / PSD  (decarboxylation)
              │
   Phosphatidylethanolamine (PE)  ── ~80% of P. putida membrane
```

The enzyme operates at the **cytoplasmic leaflet of the inner (cytoplasmic) membrane**. Its 8-transmembrane-helix bundle embeds it in the bilayer, positioning a funnel-shaped active site at the membrane–cytoplasm interface. There, the aspartate quartet (D95/D98/D116/D120) chelates a catalytic Mg²⁺ ion. The Mg²⁺ polarizes and stabilizes the developing negative charge on the β-phosphate of CDP-DAG as the L-serine hydroxyl performs an in-line nucleophilic attack on the phosphatidyl phosphorus. CMP departs as the leaving group, and phosphatidylserine is released into the membrane. The reaction is a **single-step, metal-assisted direct displacement** — no covalent phosphatidyl-enzyme intermediate forms.

### Two convergent but mechanistically distinct "PssA" solutions in bacteria

A central insight of this investigation is that "phosphatidylserine synthase" (EC 2.7.8.8) is catalyzed by **two unrelated enzyme families** in different bacteria, and *P. putida* uses the opposite family from the textbook *E. coli* paradigm:

| Property | *P. putida* PssA (PP_4677) | *E. coli*-type PssA |
|---|---|---|
| Superfamily | CDP-alcohol phosphotransferase (CDP-AP), class I | Phospholipase D (PLD) superfamily |
| KEGG ortholog | **K17103** | **K00998** |
| Domain (Pfam) | PF01066 | PLDc |
| Membrane association | Polytopic integral (8 TM) | Peripheral / soluble, associates with membrane |
| Cofactor | Mg²⁺ (four aspartates) | No metal; His-based dyads |
| Mechanism | Direct displacement, single step | Covalent phosphatidyl-enzyme intermediate |
| Structural paradigm | Archaeal IPCT-DIPPS (4O6M); mycobacterial PIPS | *E. coli* PssA crystal structures |

Both make the same product (PS), but through entirely different chemistry and architecture — a striking example of convergent functional evolution. This distinction is not merely academic: it means that inferences about the *P. putida* enzyme must be drawn from CDP-AP-family homologs (phosphatidylinositol/phosphatidylinositol-phosphate/phosphatidylglycerophosphate synthases and eukaryotic choline/ethanolamine phosphotransferases), **not** from the *E. coli* PssA literature.

### Localization and physiological role

PssA works **at and in the inner membrane, facing the cytoplasm**. Its product feeds the highest-flux lipid branch in *P. putida*, generating the PE that constitutes ~80% of the membrane. Because PE is a non-bilayer-prone, cone-shaped lipid, this pool governs membrane curvature, protein insertion/folding, and permeability barrier integrity, and it is the substrate that solvent-stress remodeling (PE↓, cardiolipin↑) modulates. PssA therefore is a foundational housekeeping enzyme of membrane biogenesis whose activity constrains the organism's capacity for stress-responsive lipid homeostasis.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/) | *Structure characterization of phospholipids and lipid A of P. putida KT2442* | Establishes PE (79.9%), PG (12.7%), cardiolipin (7.4%) — quantifies the dominance of the PssA-initiated PE pathway product. |
| [33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/) | *Structural insights into phosphatidylethanolamine formation in bacterial membrane biogenesis* | Confirms downstream step: PS is decarboxylated to PE by membrane-anchored PSD, placing PssA upstream. |
| [24942835](https://pubmed.ncbi.nlm.nih.gov/24942835/) | *X-ray structure of a CDP-alcohol phosphatidyltransferase membrane enzyme* | Defines family chemistry (CMP displacement from CDP-alcohol) and the Mg²⁺/four-aspartate/TM2-TM3 catalytic architecture that PP_4677's motif implements. |
| [41308808](https://pubmed.ncbi.nlm.nih.gov/41308808/) | *CDP-alcohol phosphotransferases: structures and function of diverse sub-classes* | Frames the CDP-AP family and its two mechanistic classes; supports class-I assignment. |
| [25687304](https://pubmed.ncbi.nlm.nih.gov/25687304/) | *The active site of yeast PI synthase Pis1 is facing the cytosol* | Experimental topology of a homolog: CAPT motif is cytosolic; 6-TM fold maps onto archaeal CAPT structures. |
| [21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/) | *Glycerophospholipid inventory of P. putida conserved between strains* | Shows PE/PG/cardiolipin composition (downstream of PssA) is a conserved species feature. |
| [9020089](https://pubmed.ncbi.nlm.nih.gov/9020089/) | *Mechanisms for solvent tolerance in bacteria* | Demonstrates the PE pool fed by PssA is actively remodeled (PE↓, cardiolipin↑) during solvent tolerance. |
| [39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/) | *Structural basis for membrane association and catalysis by PssA* | Documents the mechanistically distinct *E. coli*-type PssA (covalent intermediate, peripheral membrane) — the contrast that highlights P. putida's different family. |
| [26510127](https://pubmed.ncbi.nlm.nih.gov/26510127/) | *Structural basis for phosphatidylinositol-phosphate biosynthesis* | Renibacterium/M. tuberculosis PIPS structures — CDP-AP class-I paradigm defining acceptor site and substrate specificity determinants. |
| [32389689](https://pubmed.ncbi.nlm.nih.gov/32389689/) | *PI-phosphate biosynthesis in mycobacteria* | Additional CDP-AP class-I structural/functional framework for substrate specificity and catalysis. |
| [39747155](https://pubmed.ncbi.nlm.nih.gov/39747155/) | *Catalysis and selectivity of eukaryotic choline-phosphotransferase* | Yeast CPT1 structures propose a general reaction mechanism for the CDP-AP family, including headgroup selectivity determinants relevant to serine specificity. |
| [24968740](https://pubmed.ncbi.nlm.nih.gov/24968740/) | *Intramembrane liponucleotide synthetase (CdsA)* | Characterizes the upstream enzyme that makes the CDP-DAG substrate PssA consumes; two-metal mechanism at the membrane-cytoplasm interface. |

**Strength of evidence:** The functional assignment (Findings 1, 2, 5) is very strongly supported by database orthology (KEGG/eggNOG/Pfam/InterPro/Rhea concordance) and by direct sequence detection of the diagnostic CAPT motif with its four catalytic aspartates (Finding 7). The mechanistic and topological interpretation (Findings 2, 3, 6) is well supported by high-resolution structures of multiple CDP-AP class-I homologs and by experimental topology mapping of the homolog Pis1 — but is **inferred by homology**, not measured on PP_4677 itself. The physiological/lipidomics context (Findings 1, 4) is directly measured, but in *P. putida* as a whole, not by manipulating PssA specifically.

---

## Limitations and Knowledge Gaps

1. **No enzyme-specific experimental study exists.** UniProt evidence level for Q88DZ1 is PE=3 (inferred from homology). No published work reports purification, in vitro assay, kinetics, substrate-specificity measurement, mutagenesis, gene knockout, or structure determination of the *P. putida* PP_4677 gene product. Every mechanistic and localization claim is an inference from homologs.

2. **The catalytic residues are predicted, not validated.** The assignment of D95/D98/D116/D120 as the Mg²⁺-coordinating quartet rests on motif alignment to crystallized homologs. Site-directed mutagenesis of PP_4677 has not been performed.

3. **Substrate specificity is inferred from subfamily membership.** InterPro IPR004533 (CDP-diacylglycerol-serine O-PTase) and KEGG K17103 assign serine as the acceptor. However, some CDP-AP enzymes have relaxed or dual specificity. The exact acyl-chain preference and any serine-vs-other-alcohol selectivity of PP_4677 are unmeasured.

4. **Topology is predicted (8 TM by UniProt; 6-TM core by family homology).** The precise number of membrane spans and the exact orientation have not been experimentally determined for this protein; the AlphaFold model is confident for the core but not a substitute for experimental structure.

5. **Regulation and conditional essentiality are unknown.** Whether *pssA* (PP_4677) is essential in *P. putida*, how it is transcriptionally/post-translationally regulated, and how its activity is tuned during solvent stress remain uncharacterized. The lipidomics remodeling data are correlative with respect to this specific enzyme.

6. **Possible functional redundancy is unexplored.** It is not established whether *P. putida* encodes any alternative route to PS/PE, though none was identified in genomic neighborhood analysis.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous complementation.** Express PP_4677 in an *E. coli pssA*-conditional/temperature-sensitive strain (or a PS-auxotroph) to test whether it restores PS/PE synthesis — a direct functional confirmation independent of *E. coli*'s own enzyme.

2. **In vitro enzymology.** Purify recombinant His-tagged PP_4677 in detergent/nanodiscs; assay CDP-DAG + L-serine → PS + CMP activity; determine Mg²⁺ dependence, Km for each substrate, and pH optimum. Test alternative acceptor alcohols (e.g., glycerol-3-phosphate, inositol, ethanolamine) to define specificity.

3. **Site-directed mutagenesis of the aspartate quartet.** Individually mutate D95, D98, D116, D120 to Ala/Asn and measure the loss of activity to validate their catalytic roles and Mg²⁺ coordination.

4. **Gene deletion / essentiality.** Attempt a clean ΔPP_4677 knockout in KT2440; if lethal, construct a conditional (inducible) mutant. Perform lipidomics on the mutant to confirm PS/PE depletion and any compensatory PG/cardiolipin increase.

5. **Topology mapping.** Use substituted-cysteine accessibility (SCAM) or reporter fusions (PhoA/GFP) to experimentally verify the 8-TM topology and the cytoplasmic orientation of the CAPT active-site loop.

6. **Structural determination.** Pursue cryo-EM or crystallography of PP_4677 (with/without CDP-DAG and Mg²⁺) to confirm the fold, the metal site, and the serine-acceptor pocket — directly testing the homology-based model.

7. **Stress-response linkage.** Quantify PP_4677 expression/activity under toluene and other solvent stress to test whether PE remodeling is driven at the level of PssA flux.

---

## Conclusion

PP_4677 (Q88DZ1) is the **phosphatidylserine synthase (PssA, EC 2.7.8.8)** of *Pseudomonas putida* KT2440 — a polytopic, Mg²⁺-dependent, integral inner-membrane CDP-alcohol phosphotransferase (CDP-AP class-I; K17103/COG1183/PF01066) that transfers the phosphatidyl group of CDP-diacylglycerol onto L-serine to make phosphatidylserine + CMP (RHEA:16913) at the cytoplasmic face of the membrane, using an active site built from four conserved aspartates (D95, D98, D116, D120) that coordinate the catalytic Mg²⁺. It catalyzes the committed step of the PA→PS→PE pathway (module M00093), supplying the phosphatidylserine that is decarboxylated to phosphatidylethanolamine — the dominant (~80%) membrane phospholipid — and is thereby central to membrane biogenesis and stress-responsive lipid homeostasis. Mechanistically it is distinct from the *E. coli* phospholipase-D-type PssA (K00998). This assignment is a strong, convergent inference from orthology, sequence, and comparative structural biology; it has not been confirmed by any experimental study performed directly on the *P. putida* protein.


## Artifacts

- [OpenScientist final report](PP_4677-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4677-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26579930
2. PMID:33707636
3. PMID:24942835
4. PMID:41308808
5. PMID:39693441
6. PMID:25687304
7. PMID:21895997
8. PMID:9020089