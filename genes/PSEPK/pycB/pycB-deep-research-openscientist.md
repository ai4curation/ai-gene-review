---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T19:14:31.980224'
end_time: '2026-07-11T19:29:45.956577'
duration_seconds: 913.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pycB
  gene_symbol: pycB
  uniprot_accession: Q88C37
  protein_description: 'SubName: Full=Pyruvate carboxylase subunit B {ECO:0000313|EMBL:AAN70911.1};
    EC=6.4.1.1 {ECO:0000313|EMBL:AAN70911.1};'
  gene_info: Name=pycB {ECO:0000313|EMBL:AAN70911.1}; OrderedLocusNames=PP_5346 {ECO:0000313|EMBL:AAN70911.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Aldolase_TIM. (IPR013785); Biotin_lipoyl. (IPR000089); Carboxylase_cons_dom.
    (IPR003379); OadA. (IPR005776); PCB-like. (IPR055268)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pycB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pycB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C37
- **Protein Description:** SubName: Full=Pyruvate carboxylase subunit B {ECO:0000313|EMBL:AAN70911.1}; EC=6.4.1.1 {ECO:0000313|EMBL:AAN70911.1};
- **Gene Information:** Name=pycB {ECO:0000313|EMBL:AAN70911.1}; OrderedLocusNames=PP_5346 {ECO:0000313|EMBL:AAN70911.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aldolase_TIM. (IPR013785); Biotin_lipoyl. (IPR000089); Carboxylase_cons_dom. (IPR003379); OadA. (IPR005776); PCB-like. (IPR055268)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pycB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pycB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pycB** (gene ID: pycB, UniProt: Q88C37) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pycB* (PP_5346, UniProt Q88C37) in *Pseudomonas putida* KT2440

## Summary

**pycB (PP_5346; UniProt Q88C37; EC 6.4.1.1) encodes the β subunit of a two-subunit, biotin-dependent pyruvate carboxylase in *Pseudomonas putida* KT2440.** The PycB polypeptide (602 amino acids) carries two of the three catalytic modules of pyruvate carboxylase (PC): the **carboxyltransferase (CT) domain** (approximately residues 5–265) and the **biotin carboxyl carrier protein (BCCP) domain** (residues ~526–601), which bears the covalently attached biotin cofactor on Lys566. Its operon partner, **pycA (PP_5347; ortholog K01959)**, encodes the α subunit that supplies the third module — the ATP-dependent **biotin carboxylase (BC)**. Together the two proteins assemble a holoenzyme that catalyzes the physiologically important anaplerotic reaction: **pyruvate + HCO₃⁻ + ATP → oxaloacetate + ADP + Pᵢ**.

Mechanistically, PC operates as a biotin-swinging-arm, two-active-site machine. The BC domain (on PycA) first uses MgATP and bicarbonate to carboxylate the biotin prosthetic group tethered to Lys566 in PycB's BCCP domain, generating carboxybiotin. The biotinylated BCCP "arm" then swings to the CT active site within PycB, where the carboxyl group is transferred to the C3 methyl carbon of pyruvate — via a metal-stabilized enolpyruvate intermediate in a ping-pong bi-bi mechanism — to form oxaloacetate. This domain division (BC on the α subunit; CT + BCCP on the β subunit) is the hallmark of the "two-subunit" class of bacterial pyruvate carboxylases and matches Q88C37's exact domain architecture.

Physiologically, PycB functions in the **cytoplasm** as a soluble enzyme (no signal peptide or transmembrane segment). Its role is **anaplerotic**: it replenishes tricarboxylic acid (TCA) cycle oxaloacetate that is siphoned off for biosynthesis, thereby linking glycolytic/Entner-Doudoroff-derived pyruvate to the C4 pool of central carbon metabolism. In KT2440 — an organism whose glycolysis runs almost exclusively through the Entner-Doudoroff route within the cyclic EDEMP architecture — this anaplerotic bridge is one of two parallel carboxylating routes at the C3↔C4 node, working alongside PEP carboxylase (PP_1505). Pyruvate carboxylase (PycA/PycB) is strongly induced (up to ~30-fold at the protein level) during growth on aromatic, lignin-derived carbon substrates, reflecting metabolic remodeling toward anaplerosis when carbon enters central metabolism through the TCA cycle.

---

## Gene/Protein Identity Verification

Before presenting findings, the target identity was confirmed against the UniProt record and independent databases:

| Attribute | Value | Source/Verification |
|---|---|---|
| UniProt accession | Q88C37 | Provided; matches KEGG/EMBL |
| Gene symbol | *pycB* | UniProt, EMBL AAN70911.1 |
| Ordered locus | PP_5346 | UniProt, KEGG (ppu) |
| KEGG ortholog | K01960 (PC subunit B) | KEGG |
| EC number | 6.4.1.1 | UniProt, KEGG |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125) | UniProt |
| Protein length | 602 aa | UniProt |
| Domains | CT (Pfam PF00682/PF02436; IPR003379/IPR005776/IPR013785) + BCCP (Pfam PF00364; IPR000089 Biotin_lipoyl) | InterPro / Pfam |

**Conclusion of verification:** The gene symbol, ordered locus, EC number, organism, and domain architecture are fully internally consistent and match the two-subunit pyruvate carboxylase β-subunit model. The domains listed in the research brief (Aldolase_TIM IPR013785, Biotin_lipoyl IPR000089, Carboxylase_cons_dom IPR003379, OadA IPR005776, PCB-like IPR055268) are precisely the CT (TIM-barrel/OadA/carboxylase) plus biotinyl-lipoyl signatures expected for PycB. No conflicting-gene ambiguity was encountered; the literature on two-subunit bacterial PC and on *P. putida* central metabolism applies directly.

---

## Key Findings

### Finding 1 — PycB is the β subunit of a two-subunit pyruvate carboxylase, carrying the CT and BCCP domains

PycB (Q88C37, PP_5346) is a 602-amino-acid protein whose domain organization places it unambiguously as the **β subunit** of a two-subunit biotin-dependent pyruvate carboxylase. Its N-terminal region (~residues 5–265) constitutes a **pyruvate carboxyltransferase (CT) domain** (Pfam PF00682 HMGL-like / PF02436 PYC_OADA; InterPro IPR003379/IPR005776 OadA, IPR013785 Aldolase_TIM), and its C-terminal region (~residues 526–601) is a **biotinyl/lipoyl-binding BCCP domain** (Pfam PF00364; InterPro IPR000089 Biotin_lipoyl). Orthology assignments (eggNOG COG5016, oxaloacetate/pyruvate carboxyltransferase; COG0511, biotin carboxyl carrier protein) reinforce this dual-domain identity. The third catalytic component of PC — the biotin carboxylase (BC) — is absent from PycB and is instead encoded by the adjacent *pycA* gene.

This architecture matches the defining feature of the two-subunit PC class. As stated by the structural study of two-subunit PC ([PMID: 27708276](https://pubmed.ncbi.nlm.nih.gov/27708276/)): *"PC is a two-subunit enzyme in a collection of Gram-negative bacteria, with the α subunit containing the BC and the β subunit the CT and BCCP domains."* The same work notes that *"PC contains biotin carboxylase (BC), carboxyltransferase (CT) and biotin carboxyl carrier protein (BCCP) components."* Both statements map directly onto Q88C37: PycB is the β subunit, contributing the CT and BCCP functions while relying on PycA (α subunit) for the BC half-reaction.

### Finding 2 — The PycA/PycB holoenzyme carboxylates pyruvate to oxaloacetate through a swinging-biotin mechanism

The catalytic identity of the enzyme is fixed by EC 6.4.1.1, which defines the reaction:

```
ATP + pyruvate + HCO3-  →  ADP + Pi + oxaloacetate
```

Mechanistically, the enzyme executes a **two-step, ping-pong reaction** distributed across two spatially separated active sites:

1. **Biotin carboxylation (on PycA's BC domain):** MgATP and bicarbonate carboxylate the biotin prosthetic group that is covalently linked to a conserved lysine (Lys566) in PycB's BCCP domain, forming carboxybiotin.
2. **Carboxyl transfer (on PycB's CT domain):** The carboxybiotinylated BCCP arm swings to the CT active site, which transfers the activated carboxyl group to the C3 methyl of pyruvate, yielding oxaloacetate.

The authoritative review by Jitrapakdee et al. (2008) documents both the overall reaction and the biotin-mediated carboxyl shuttle. As stated ([PMID: 18613815](https://pubmed.ncbi.nlm.nih.gov/18613815/)): *"PC (pyruvate carboxylase) is a biotin-containing enzyme that catalyses the HCO(3)(-)- and MgATP-dependent carboxylation of pyruvate to form oxaloacetate."* The same review describes the swinging-arm shuttle: *"the biotin moiety transfers the carboxy group between the biotin carboxylase domain active site on one polypeptide chain and the carboxyltransferase active site on the adjacent antiparallel polypeptide chain."* In the two-subunit *P. putida* enzyme, this inter-active-site translocation occurs between PycA (BC) and PycB (CT), with PycB's own BCCP arm serving as the carrier.

The classical tetrameric PCs are additionally subject to allosteric activation by acetyl-CoA and inhibition by aspartate; whether the *P. putida* two-subunit enzyme retains these regulatory features has not been experimentally established here and remains an open question (see Limitations).

### Finding 3 — Cytoplasmic anaplerosis of TCA-cycle oxaloacetate, strongly induced on aromatic/lignin carbon

PycB's physiological role is **anaplerotic**: it replenishes oxaloacetate that is continuously withdrawn from the TCA cycle for amino-acid and other biosynthesis. Jitrapakdee et al. describe the pyruvate carboxylase reaction as *"a very important anaplerotic reaction, replenishing oxaloacetate withdrawn from the tricarboxylic acid cycle for various pivotal biochemical pathways"* ([PMID: 18613815](https://pubmed.ncbi.nlm.nih.gov/18613815/)).

This role is particularly salient in *P. putida* KT2440, whose central carbon metabolism has an unusual topology. Nikel et al. showed that in KT2440 *"glycolysis is known to proceed almost exclusively through the Entner-Doudoroff (ED) route"* within the cyclic EDEMP architecture (a combination of Entner-Doudoroff, Embden-Meyerhof-Parnas, and pentose-phosphate enzymes), and the organism lacks a functional conventional EMP glycolysis ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). In this context, pyruvate carboxylase provides a direct anaplerotic link from glycolytic/ED-derived pyruvate into the C4 pool (oxaloacetate) that feeds the TCA cycle and gluconeogenic/biosynthetic demand.

The physiological importance of this anaplerotic route is underscored by proteomics of KT2440 grown on aromatic (lignin-derived) substrates. Zhou et al. (2025) reported an *"Up to 30-fold increase in pyruvate carboxylase and glyoxylate shunt proteins [that] implies a metabolic remodeling"* ([PMID: 40883435](https://pubmed.ncbi.nlm.nih.gov/40883435/)). Because aromatic compounds are funneled (via the β-ketoadipate pathway) into acetyl-CoA and TCA-cycle intermediates, cells must upregulate anaplerotic and glyoxylate-shunt machinery to maintain the C4 pool — and pyruvate carboxylase (PycA/PycB) is a principal responder.

**Localization:** Q88C37 has no predicted signal peptide or transmembrane segment, consistent with a **soluble, cytoplasmic** enzyme — the compartment in which all characterized pyruvate carboxylases operate and where central carbon metabolism occurs.

### Finding 4 — Operon structure and the biotinyl-lysine (Lys566) attachment site

Genomic context corroborates the split-enzyme model. KEGG annotates **PP_5346** as *pyruvate carboxylase subunit B* (K01960, EC 6.4.1.1) and the immediately adjacent **PP_5347** as *pyruvate carboxylase subunit A* (K01959, EC 6.4.1.1, the biotin carboxylase). The two genes form a compact two-gene arrangement encoding the complementary halves of one holoenzyme. Downstream, **PP_5348** is a **LysR-family transcriptional regulator** (annotated K21711 as a putative pyruvate carboxylase regulator), suggesting local transcriptional control of the *pyc* locus; the upstream gene PP_5345 is an unrelated GNAT acetyltransferase.

At the sequence level, the canonical biotin-attachment motif **A-M-K-M** is located at residues 565–568 of PycB, placing the **biotinyl lysine at Lys566** within the C-terminal BCCP domain (526–601). The local sequence context (…ITEAMK⁵⁶⁶METEVQAAIAGKV…) matches the conserved biotin-carboxyl-carrier signature found across biotin-dependent carboxylases. This lysine is the covalent attachment point for the biotin prosthetic group that shuttles the carboxyl group between active sites.

The two-gene division (pycA = BC subunit A; pycB = CT + BCCP subunit B) matches the established subunit organization for two-subunit PC ([PMID: 27708276](https://pubmed.ncbi.nlm.nih.gov/27708276/)): *"the α subunit containing the BC and the β subunit the CT and BCCP domains."*

### Finding 5 — PycB is one of two parallel anaplerotic carboxylases at the C3↔C4 node

Mapping KEGG orthologs onto the KT2440 genome reveals the full anaplerotic node topology:

| Enzyme | KO | Locus in KT2440 | Reaction | Present? |
|---|---|---|---|---|
| PEP carboxylase | K01595 | PP_1505 | PEP + HCO₃⁻ → OAA + Pᵢ | Yes |
| Pyruvate carboxylase subunit A (BC) | K01959 | PP_5347 (*pycA*) | (with PycB) pyruvate + HCO₃⁻ + ATP → OAA | Yes |
| Pyruvate carboxylase subunit B (CT+BCCP) | K01960 | PP_5346 (*pycB*) | (with PycA) carboxyl transfer to pyruvate | Yes |
| Single-chain pyruvate carboxylase | K01958 | — | — | Absent |
| NADP-malic enzyme | K00029 | PP_5085 | malate → pyruvate + CO₂ + NADPH | Yes |
| NAD-malic enzyme | K00027 | — | — | Absent |
| Malate dehydrogenase | K00024 | PP_0654 | malate ↔ OAA | Yes |

Thus the C3↔C4 (PEP/pyruvate ↔ oxaloacetate/malate) node in KT2440 possesses **two anaplerotic carboxylases** — PEP carboxylase (PP_1505) and the two-subunit pyruvate carboxylase (PycA/PycB) — with NADP-malic enzyme (PP_5085) providing the opposing decarboxylating (cataplerotic) flux. Notably, KT2440 lacks the single-chain PC (K01958), confirming that its only pyruvate-to-oxaloacetate route is the two-subunit PycA/PycB system. This redundancy at the anaplerotic node provides metabolic flexibility for switching between substrates that enter metabolism above (sugars → PEP/pyruvate) versus within (aromatics → TCA) the cycle.

### Finding 6 — Structurally defined carboxyltransferase chemistry: carboxybiotin → pyruvate, metal-dependent, BCCP docks into CT

Crystallographic studies of homologous pyruvate carboxylases define the precise chemistry that PycB's CT domain performs. Although these structures are from *Rhizobium etli*, human, and *Staphylococcus aureus* PC (not *P. putida* directly), the CT domain is highly conserved and the mechanistic conclusions transfer to PycB, which contains the same CT and BCCP modules.

Lietzan and St Maurice (2013) state that *"The carboxyltransferase (CT) domain of PC catalyzes the transfer of a carboxyl group from carboxybiotin to the accepting substrate, pyruvate"* ([PMID: 24157795](https://pubmed.ncbi.nlm.nih.gov/24157795/)), proceeding via a reactive enolpyruvate intermediate stabilized by a divalent metal ion in the CT active site. Lietzan, Lin, and St Maurice (2014) further establish that *"During catalysis, carboxybiotin is translocated to the carboxyltransferase domain where the carboxyl group is transferred to the acceptor substrate, pyruvate"* and that the isolated CT domain retains a biotin-independent oxaloacetate decarboxylation activity *"through a simple ping-pong bi bi mechanism"* ([PMID: 25157442](https://pubmed.ncbi.nlm.nih.gov/25157442/)). Finally, the full-length PC structures of Xiang and Tong (2008) provided the first direct visualization of the biotin-CT interaction: *"A BCCP domain is located in the active site of the CT domain, providing the first molecular insights into how biotin participates in the carboxyltransfer reaction"* ([PMID: 18297087](https://pubmed.ncbi.nlm.nih.gov/18297087/)).

These structural results map directly onto PycB, which houses both the CT domain (res. 5–265) and the biotinyl BCCP domain (res. 526–601, biotinyl-Lys566). They collectively confirm: (i) the substrate accepted is pyruvate; (ii) the carboxyl donor is carboxybiotin; (iii) catalysis requires a divalent metal ion; (iv) the reaction is ping-pong bi-bi; and (v) the biotinyl BCCP domain physically docks into the CT active site to deliver the carboxyl group.

---

## Mechanistic Model / Interpretation

The unified model for PycB function within the *P. putida* KT2440 two-subunit pyruvate carboxylase is summarized below.

### Domain architecture of PycB (602 aa)

```
N-term                                                              C-term
|----- Carboxyltransferase (CT) domain -----|        |-- BCCP --|
|  res ~5–265                               |        | 526–601  |
|  TIM-barrel / OadA fold                   |  ...   | biotinyl |
|  metal-dependent carboxyl transfer        |        | Lys566   |
|  Pfam PF00682/PF02436                     |        | PF00364  |
|-------------------------------------------|        |----------|
                                                          |
                                                     biotin–Lys566
                                                     (swinging arm)
```

### Two-subunit holoenzyme and the swinging-biotin cycle

```
        PycA (α subunit, PP_5347)              PycB (β subunit, PP_5346)
     ┌───────────────────────────┐         ┌──────────────────────────────┐
     │   Biotin Carboxylase (BC) │         │  Carboxyltransferase (CT)     │
     │                           │         │                               │
     │  ATP + HCO3-  ─────────►  │         │   pyruvate ──► oxaloacetate   │
     │       │                   │         │       ▲                       │
     └───────┼───────────────────┘         └───────┼───────────────────────┘
             │                                      │
             │   biotin–Lys566 (BCCP swinging arm on PycB)
             │   carboxylated here ...              ... delivered here
             └──────────────────────────────────────┘
        Step 1: BC carboxylates biotin        Step 2: CT transfers carboxyl
        (MgATP + HCO3- → carboxybiotin)        (carboxybiotin + pyruvate → OAA)
```

**Overall reaction:** pyruvate + HCO₃⁻ + ATP → oxaloacetate + ADP + Pᵢ (EC 6.4.1.1)

### Metabolic placement at the C3↔C4 anaplerotic node

```
   Glucose ──(Entner–Doudoroff / EDEMP cycle)──► Pyruvate ──► Acetyl-CoA ──► TCA cycle
                                                    │                          │
                                                    │ PycA/PycB (PC)           │ (OAA drained
                                                    │ + HCO3- + ATP            │  for biosynthesis)
                                                    ▼                          ▼
   PEP ──(PEP carboxylase, PP_1505)──────────► Oxaloacetate ◄───────────── TCA cycle
                                                    ▲
                                        NADP-malic enzyme (PP_5085): malate → pyruvate (cataplerotic)

   Aromatics / lignin ──(β-ketoadipate)──► Acetyl-CoA + TCA intermediates
        └─► strong induction (~30×) of pyruvate carboxylase for anaplerosis
```

**Interpretation:** PycB is a catalytic half of the sole pyruvate-carboxylating enzyme in KT2440. Its function is to fix bicarbonate onto pyruvate, creating oxaloacetate and thereby topping up the C4 pool of the TCA cycle. This is essential whenever oxaloacetate is drained for biosynthesis faster than the cycle regenerates it — a condition intensified during growth on aromatic/lignin carbon, which enters metabolism at the acetyl-CoA/TCA level. The parallel presence of PEP carboxylase gives the cell two anaplerotic entry points (from PEP and from pyruvate), while NADP-malic enzyme provides the reverse decarboxylating flux, together forming a flexible "metabolic node" that balances C3 and C4 pools and NADPH supply.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [27708276](https://pubmed.ncbi.nlm.nih.gov/27708276/) | *A distinct holoenzyme organization for two-subunit pyruvate carboxylase* | Establishes that in two-subunit bacterial PC the β subunit (PycB) carries CT + BCCP and the α subunit (PycA) carries BC — the core structural claim (Findings 1, 4) |
| [18613815](https://pubmed.ncbi.nlm.nih.gov/18613815/) | *Structure, mechanism and regulation of pyruvate carboxylase* (Jitrapakdee et al., 2008) | Authoritative review defining the overall reaction, the swinging-biotin mechanism, and the anaplerotic role (Findings 2, 3) |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through EDEMP cycle* (Nikel et al.) | Establishes the ED/EDEMP central-metabolism context in which PycB anaplerosis operates (Finding 3) |
| [40883435](https://pubmed.ncbi.nlm.nih.gov/40883435/) | *Quantitative decoding of coupled carbon and energy metabolism…lignin* (Zhou et al., 2025) | Experimental proteomic evidence of ~30-fold PC upregulation during aromatic/lignin catabolism (Finding 3) |
| [24157795](https://pubmed.ncbi.nlm.nih.gov/24157795/) | *Insights into the carboxyltransferase reaction of PC…* (Lietzan & St Maurice, 2013) | Crystallographic definition of the CT reaction (carboxybiotin → pyruvate), metal dependence (Finding 6) |
| [25157442](https://pubmed.ncbi.nlm.nih.gov/25157442/) | *The role of biotin and oxamate in the carboxyltransferase reaction of PC* (Lietzan et al., 2014) | Establishes carboxybiotin translocation to CT and the ping-pong bi-bi mechanism (Finding 6) |
| [18297087](https://pubmed.ncbi.nlm.nih.gov/18297087/) | *Crystal structures of human and S. aureus PC…* (Xiang & Tong, 2008) | First structural view of BCCP domain docked in the CT active site (Finding 6) |

**Additional supporting literature reviewed:** proteomic/functional-genomics studies of *P. putida* KT2440 including para-coumarate/aromatic conversion transposon screens ([PMID: 33964456](https://pubmed.ncbi.nlm.nih.gov/33964456/)), fatty-acid/alcohol metabolism RB-TnSeq analysis ([PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/)), and a companion lignin-carbon-metabolism study ([PMID: 40196702](https://pubmed.ncbi.nlm.nih.gov/40196702/)). These provide the systems-level context (substrate range, fitness, aromatic catabolism) in which the anaplerotic role of PycB is embedded.

**How the evidence coheres and where it is inferential:** The domain assignment, operon structure, biotinyl-lysine position, and metabolic-node topology are grounded in direct sequence/genome annotation of Q88C37 and the KT2440 genome. The reaction chemistry and mechanism are grounded in a strong review and in crystal structures — but those structures are of *homologous* PCs (human, *S. aureus*, *R. etli*), not *P. putida* PycB itself. The transfer of mechanistic detail to PycB is therefore an inference from high sequence/domain conservation rather than a direct structural determination of Q88C37. The anaplerotic induction on aromatics is direct experimental (proteomic) evidence in KT2440.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of *P. putida* PycB.** No purified-enzyme kinetics (kcat, Km for pyruvate/HCO₃⁻/ATP), no crystal structure of Q88C37, and no direct demonstration of biotinylation at Lys566 for this specific protein were found. All mechanistic conclusions are inferred from homologous PCs and the conserved domain architecture.

2. **Regulation is unresolved.** Classical tetrameric PCs are allosterically activated by acetyl-CoA and inhibited by aspartate. Whether the two-subunit *P. putida* PycA/PycB enzyme retains these effectors is not established. The downstream LysR-type regulator (PP_5348) is annotated as a putative *pyc* regulator, but its actual role, effectors, and regulon have not been experimentally defined here.

3. **Physiological essentiality/flux contribution not quantified.** Because KT2440 has a parallel anaplerotic route (PEP carboxylase, PP_1505), the individual flux contribution and conditional essentiality of PycA/PycB are unknown from the evidence gathered. Transposon-fitness datasets exist for KT2440 but were not specifically mined for PP_5346/PP_5347 fitness phenotypes across carbon sources.

4. **Holoenzyme stoichiometry and assembly** of the two-subunit enzyme in *P. putida* (e.g., the higher-order organization described for two-subunit PC) were not directly verified for this organism.

5. **Structural-transfer caveat.** The CT-domain mechanism is drawn from human/*S. aureus*/*R. etli* structures; subtle active-site or metal-coordination differences in the *P. putida* enzyme cannot be excluded.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetics.** Co-express PycA (PP_5347) and PycB (PP_5346) in *E. coli* (with BirA biotin ligase to ensure biotinylation), purify the holoenzyme, and measure steady-state kinetics for pyruvate, bicarbonate, and MgATP; confirm oxaloacetate production coupled to malate dehydrogenase/NADH assay.

2. **Biotinylation site mapping.** Use mass spectrometry (intact + peptide) to confirm covalent biotin attachment at Lys566 within the AMKM motif, and test a K566A/K566R mutant for loss of activity.

3. **Allosteric regulation.** Assay activity ± acetyl-CoA and ± L-aspartate (and other candidate effectors) to determine whether the two-subunit *P. putida* enzyme retains classical PC regulation.

4. **In-frame deletion and ¹³C-metabolic flux analysis.** Construct ΔpycB and ΔpycA strains, and a Δppc (PEP carboxylase) background, then perform ¹³C-MFA on glucose vs. aromatic (e.g., p-coumarate/ferulate) carbon to quantify the relative anaplerotic flux carried by PC vs. PEP carboxylase and confirm conditional essentiality on TCA-entering substrates.

5. **Regulator characterization.** Define the role of the LysR-family regulator PP_5348 via deletion, promoter-reporter, and DNA-binding/effector studies to determine how the *pyc* operon is transcriptionally controlled.

6. **Structural determination.** Solve the cryo-EM or crystal structure of the *P. putida* PycA/PycB holoenzyme to directly validate the CT/BCCP/BC arrangement and the biotin-swinging geometry in this organism.

7. **Mine existing fitness datasets.** Extract PP_5346/PP_5347 fitness scores from published RB-TnSeq/transposon libraries across carbon conditions ([PMID: 33964456](https://pubmed.ncbi.nlm.nih.gov/33964456/), [PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/)) to test the predicted condition-dependent importance during aromatic growth.

---

## Conclusion

*pycB* (PP_5346; Q88C37) encodes the **β subunit of *P. putida* KT2440's two-subunit, biotin-dependent pyruvate carboxylase**, contributing the **carboxyltransferase (CT)** and **biotinylated carboxyl-carrier (BCCP, biotinyl-Lys566)** domains, while its operon partner **pycA (PP_5347)** supplies the **biotin carboxylase (BC)**. The holoenzyme catalyzes the ATP- and bicarbonate-dependent carboxylation of pyruvate to oxaloacetate (EC 6.4.1.1); PycB's CT domain performs the metal-dependent, ping-pong carboxyl transfer from carboxybiotin to pyruvate, with the BCCP swinging arm docking into the CT active site. Functionally, this soluble cytoplasmic enzyme performs **anaplerotic replenishment of TCA-cycle oxaloacetate** — one of two parallel carboxylating routes alongside PEP carboxylase (PP_1505) — and is strongly upregulated (~30-fold) during growth on aromatic/lignin-derived carbon, when carbon enters metabolism at the TCA level and the C4 pool must be replenished.


## Artifacts

- [OpenScientist final report](pycB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pycB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27708276
2. PMID:18613815
3. PMID:26350459
4. PMID:40883435
5. PMID:24157795
6. PMID:25157442
7. PMID:18297087
8. PMID:33964456
9. PMID:32826213
10. PMID:40196702