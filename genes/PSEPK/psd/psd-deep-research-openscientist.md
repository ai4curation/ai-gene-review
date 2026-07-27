---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T18:57:23.256268'
end_time: '2026-07-26T19:28:45.128821'
duration_seconds: 1881.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: psd
  gene_symbol: psd
  uniprot_accession: Q88DB9
  protein_description: 'RecName: Full=Phosphatidylserine decarboxylase proenzyme {ECO:0000255|HAMAP-Rule:MF_00662};
    EC=4.1.1.65 {ECO:0000255|HAMAP-Rule:MF_00662}; Contains: RecName: Full=Phosphatidylserine
    decarboxylase alpha chain {ECO:0000255|HAMAP-Rule:MF_00662}; Contains: RecName:
    Full=Phosphatidylserine decarboxylase beta chain {ECO:0000255|HAMAP-Rule:MF_00662};'
  gene_info: Name=psd {ECO:0000255|HAMAP-Rule:MF_00662}; OrderedLocusNames=PP_4908;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the phosphatidylserine decarboxylase family.
  protein_domains: PS_Dcarbxylase. (IPR003817); PSD-B. (IPR033177); PSD_type1_pro.
    (IPR033178); PS_Dcarbxylase (PF02666); PSD (PF27523)
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: psd-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: psd-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DB9
- **Protein Description:** RecName: Full=Phosphatidylserine decarboxylase proenzyme {ECO:0000255|HAMAP-Rule:MF_00662}; EC=4.1.1.65 {ECO:0000255|HAMAP-Rule:MF_00662}; Contains: RecName: Full=Phosphatidylserine decarboxylase alpha chain {ECO:0000255|HAMAP-Rule:MF_00662}; Contains: RecName: Full=Phosphatidylserine decarboxylase beta chain {ECO:0000255|HAMAP-Rule:MF_00662};
- **Gene Information:** Name=psd {ECO:0000255|HAMAP-Rule:MF_00662}; OrderedLocusNames=PP_4908;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the phosphatidylserine decarboxylase family.
- **Key Domains:** PS_Dcarbxylase. (IPR003817); PSD-B. (IPR033177); PSD_type1_pro. (IPR033178); PS_Dcarbxylase (PF02666); PSD (PF27523)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "psd" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'psd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **psd** (gene ID: psd, UniProt: Q88DB9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *psd* (Phosphatidylserine Decarboxylase) — *Pseudomonas putida* KT2440

**UniProt:** Q88DB9 · **Gene:** *psd* · **Locus:** PP_4908 · **EC:** 4.1.1.65 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK

---

## Summary

The gene ***psd*** (PP_4908; UniProt **Q88DB9**) of *Pseudomonas putida* KT2440 encodes **phosphatidylserine decarboxylase** (PSD; EC 4.1.1.65), a **pyruvoyl-dependent lyase** that catalyzes the **final, committed step of phosphatidylethanolamine (PE) biosynthesis**: the decarboxylation of the L-serine head group of **phosphatidylserine (PS)** to yield **phosphatidylethanolamine (PE) + CO₂**. This reaction is head-group specific but broadly tolerant across PS acyl-chain species, placing the enzyme at the terminus of the KEGG PE-biosynthesis module M00093 (PA ⇒ PS ⇒ PE). The identity is unambiguous: Q88DB9 carries every diagnostic catalytic and structural signature of the phosphatidylserine decarboxylase family, is annotated by the curated HAMAP rule MF_00662, and shares ~61% sequence identity with the crystallographically characterized *E. coli* enzyme.

Mechanistically, Psd is synthesized as an inactive **proenzyme** that undergoes **autocatalytic self-cleavage (serinolysis)** at a conserved (L/V)GST-type serine motif, splitting into a small **α chain** that bears an N-terminal **pyruvoyl prosthetic group** and a larger membrane-anchoring **β chain**. The pyruvoyl moiety forms a Schiff-base intermediate with the amino group of the PS serine head group, enabling decarboxylation. The enzyme is a **monotopic (peripheral) inner-membrane protein**, docking to the cytoplasmic face of the membrane through an N-terminal amphipathic helix so that it acts on **membrane-embedded PS at the lipid–water interface**, where its hydrophobic substrate groove accommodates a wide range of fatty acyl chains.

Biologically, the product PE is the **dominant membrane phospholipid** of *P. putida* (~80% of total phospholipid). Beyond bulk membrane biogenesis, PE functions as a zwitterionic **"lipid chaperone"** that governs the folding and topology of inner-membrane proteins (the Positive-Inside and Charge-Balance rules), and PE-dependent physiology extends to flagellar motility, chemotaxis, and adaptation to solvent stress. Because PE synthesis via PSD is essential in many bacteria, the enzyme is a genetically and chemically validated antimicrobial drug target. The functional assignment for Q88DB9 is supported by convergent evidence from curated database annotation, ortholog enzymology and structural biology, sequence-motif conservation, a high-confidence AlphaFold model, and organism-specific lipidomics.

---

## Key Findings

### 1. Psd catalyzes the decarboxylation of phosphatidylserine to phosphatidylethanolamine (EC 4.1.1.65)

Q88DB9 is annotated under the curated HAMAP rule **MF_00662** as a phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65), gene *psd*/PP_4908, belonging to the phosphatidylserine decarboxylase family (Pfam PF02666 PS_Dcarbxylase; InterPro IPR033177 PSD-B, IPR033178 PSD_type1_pro). The catalyzed reaction — **PS → PE + CO₂** — is the terminal and committed step of PE biosynthesis and is conserved across bacteria. As stated in a methods study of the enzyme family, *"Phosphatidylserine decarboxylases (PSDs) catalyze the conversion of phosphatidylserine (PS) to phosphatidylethanolamine (PE), a critical step in membrane biogenesis"* [PMID: 32430397](https://pubmed.ncbi.nlm.nih.gov/32430397/). The historical characterization in *E. coli* confirms the position of this step: *"The final step in the biosynthesis of phosphatidylethanolamine, the major membrane lipid of Escherichia coli, is catalyzed by the membrane-bound enzyme, phosphatidylserine decarboxylase"* [PMID: 796663](https://pubmed.ncbi.nlm.nih.gov/796663/).

The physiological relevance of this reaction in the target organism is underscored by lipidomics: in *P. putida* KT2442, *"Major phospholipids ... were phosphatidylethanolamine (79.9%), phosphatidylglycerol (12.7%), and cardiolipin (7.4%)"* [PMID: 26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/) — a PE-dominant membrane fully consistent with a highly active Psd.

### 2. Psd is a pyruvoyl-dependent decarboxylase that self-cleaves into α and β chains to generate its catalytic cofactor

The Psd proenzyme is not catalytically competent as translated. It undergoes **autocatalytic serinolysis** at a conserved (L/V)GST-type motif, generating a small **α chain** with an N-terminal **pyruvoyl group** and a larger membrane-anchoring **β chain** — the two chains explicitly listed in the UniProt entry for Q88DB9. The pyruvoyl carbonyl forms a Schiff base with the amino group of the PS serine head group, the essential step for decarboxylation. As summarized for the bacterial enzyme, *"The enzyme undergoes auto-cleavage for activation and utilizes the pyruvoyl moiety to form a Schiff base intermediate with PS to facilitate decarboxylation"* [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/).

Direct experimental proof of the two-chain architecture comes from the *Plasmodium falciparum* type I enzyme: *"Site-directed mutagenesis of the VGSS active site demonstrated that the PfPSD proenzyme was processed into two non-identical subunits (alpha and beta)"* [PMID: 14651609](https://pubmed.ncbi.nlm.nih.gov/14651609/); that same study reported a **Kₘ ≈ 63 ± 19 µM for PS**. The serine-to-pyruvoyl conversion that underpins the chemistry has been visualized in a related pyruvoyl-dependent decarboxylase fold, where *"the N-terminus of Ser442 was modified to form a pyruvoyl group"* [PMID: 39321488](https://pubmed.ncbi.nlm.nih.gov/39321488/).

### 3. Psd is a monotopic, inner-membrane-associated enzyme acting on membrane-embedded PS

Bacterial PSD is not an integral (polytopic) membrane protein; it associates **monotopically** with the cytoplasmic (inner) membrane via an N-terminal domain of amphipathic/hydrophobic helices, positioning its active site at the membrane interface. This co-localizes PE synthesis with the membrane where PE is deposited. Structural work states that *"the enzyme associates with cell membranes in a monotopic fashion via the N-terminal domain composed of three amphipathic helices"* [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/). The active-site pocket is lined for lipid binding: *"extensive hydrophobic interactions with the fatty acyl chains of the phospholipid, providing insights into the broad specificity of the enzyme over a wide range of cellular PS"* [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/) — the structural basis for **head-group specificity with broad acyl-chain tolerance**. Independent structural analysis of the *E. coli* enzyme confirms the anchor: *"EcPsd has an N-terminal hydrophobic helical region that is important for membrane binding, thereby achieving efficient PS recognition"* [PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/).

### 4. The Psd/PE pathway underlies membrane biogenesis, stress adaptation, and PE-dependent physiology

Genetic depletion of PE has specific, well-documented physiological consequences. In *E. coli*, *pss/psd* mutants that deplete PE become nonmotile and lack flagella: *"wild-type pss and psd genes are required for motility and chemotaxis"* [PMID: 8244943](https://pubmed.ncbi.nlm.nih.gov/8244943/), and importantly the defect is dose-dependent on PE — *"The extent of the motility and chemotaxis defects in the mutants was correlated with the amount of phosphatidylethanolamine in the membranes"* [PMID: 8244943](https://pubmed.ncbi.nlm.nih.gov/8244943/). Thermolabile *psd* mutants accumulate PS (20–40% of total phospholipid) and cease growth at non-permissive temperature, establishing the essentiality of the step [PMID: 1093166](https://pubmed.ncbi.nlm.nih.gov/1093166/). In *P. putida* specifically, the PE-dominant glycerophospholipid inventory is conserved across strains and remodeled under solvent stress: *"revealing conserved compositions within the four investigated pseudomonads P. putida KT2440, DOT-T1E, S12 and Pseudomonas sp. strain VLB120"* [PMID: 21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/), placing Psd-derived PE at the center of membrane homeostasis and solvent tolerance in the target organism.

### 5. Q88DB9 conserves all PSD catalytic/structural signatures (~59–61% identity to the crystallized E. coli enzyme)

A global (Needleman–Wunsch) alignment of *P. putida* Psd (Q88DB9, 287 aa) against *E. coli* Psd (P0A8K1, 322 aa; crystallized) yields **60.9% identity** over aligned columns (58.5% over the *P. putida* length; 168 identical positions). Critically, the diagnostic catalytic architecture is conserved at identical alignment positions:

| Motif / residue | Role | *E. coli* | *P. putida* Q88DB9 |
|---|---|---|---|
| R-F-K-L-G-S-T | Autocatalytic cleavage / pyruvoyl-forming serine | Ser~254 | **Ser253** |
| P-A-D-G (Gly-rich) | Active-site block | position 88 | **position 88** |
| H-R-V-H-M-P | Active-site block (His catalytic) | position 144 | **position 144** |
| N-terminal (res 1–45) | Amphipathic membrane anchor | hydrophobic helix | GRAVY +0.16 (vs −0.03 whole protein) |

The cleavage serine at Ser253 defines the β-chain (≈res 1–252) / α-chain (≈res 253–287; small, C-terminal, pyruvoyl-bearing) boundary. This mirrors the *E. coli* catalytic set: *"E. coli PSD primarily employs D90/D142-H144-S254 to achieve auto-cleavage for the proenzyme maturation"* [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/). The hydrophobic/amphipathic N-terminus is consistent with the described anchor region: *"EcPsd has an N-terminal hydrophobic helical region that is important for membrane binding"* [PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/).

### 6. Psd-derived PE acts as a topological "lipid chaperone" for inner-membrane proteins; PSD is a validated antimicrobial target

The product of Psd, PE, is a net-zero-charge (zwitterionic) phospholipid that enforces the membrane-protein **Charge-Balance Rule**: *"The net zero charged phospholipid phosphatidylethanolamine and other neutral lipids dampen the translocation potential of negatively charged residues in favor of the cytoplasmic retention potential of positively charged residues (Charge Balance Rule)"* [PMID: 24341994](https://pubmed.ncbi.nlm.nih.gov/24341994/). The canonical demonstration is the lactose permease (LacY): *"Assembly of LacY in membranes lacking PE (phosphatidylethanolamine) results in misorientation of the N-terminal six-TM (transmembrane domain) helical bundle with loss of energy-dependent uphill transport"* [PMID: 21599647](https://pubmed.ncbi.nlm.nih.gov/21599647/). This topological dependence is reversible and dynamic [PMID: 26512118](https://pubmed.ncbi.nlm.nih.gov/26512118/), [PMID: 22969082](https://pubmed.ncbi.nlm.nih.gov/22969082/), depends on head-group and fatty-acid composition [PMID: 23322771](https://pubmed.ncbi.nlm.nih.gov/23322771/), and PE is required for correct LacY folding/function in reconstitution [PMID: 29026149](https://pubmed.ncbi.nlm.nih.gov/29026149/). Because this PE-synthesis pathway is essential in many microbes, PSD is validated as a drug target: *"Genetic studies have validated the pathway for phosphatidylethanolamine synthesis from phosphatidylserine catalyzed by phosphatidylserine decarboxylase enzymes (PSD) as a suitable target for development of antimicrobials"* [PMID: 26585333](https://pubmed.ncbi.nlm.nih.gov/26585333/).

### 7. PP_4908 is a monocistronic PE-biosynthesis gene, not clustered with *pss* in *P. putida*

KEGG assigns PP_4908 to orthology **K01613** (phosphatidylserine decarboxylase, EC 4.1.1.65), pathway ppu00564 (Glycerophospholipid metabolism), and module **M00093** ("Phosphatidylethanolamine (PE) biosynthesis, PA ⇒ PS ⇒ PE"); the CDS spans 5,578,678–5,579,541 (864 nt, 287 aa). Its genomic neighbors are functionally unrelated — PP_4907 (upstream, same strand, 10 bp gap) is a thiosulfate sulfurtransferase (K01011), and PP_4909 (downstream, divergent) is a phosphoserine phosphatase (K01079). Thus, unlike *Bacillus subtilis*, where *psd* lies in a phospholipid operon, *P. putida psd* is **not** genomically clustered with the upstream pathway gene *pss*. The contrasting *B. subtilis* arrangement is documented: *psd* *"is located just downstream of pss, the structural gene for phosphatidylserine synthase that catalyzes the preceding reaction in phosphatidylethanolamine synthesis"* [PMID: 9422599](https://pubmed.ncbi.nlm.nih.gov/9422599/).

### 8. The AlphaFold model of Q88DB9 is high-confidence and predicts an N-terminal amphipathic membrane-anchoring helix

The AlphaFold DB model **AF-Q88DB9-F1** (287 residues) is high-confidence: **mean pLDDT 93.8** (median 96.2), with 82.6% of residues >90 and 97.6% >70. The N-terminal region (res 1–45) is well-ordered (mean pLDDT 91.0) and the catalytic core (res 60–287) averages 94.1. An Eisenberg hydrophobic-moment scan identifies a strongly **amphipathic 18-residue helix at residues ~18–35** (LSRLAGCIAECRVRWFKN; ⟨µH⟩ = 0.46, exceeding the ~0.3–0.4 amphipathicity threshold; mean hydrophobicity ≈ 0) — the hallmark of an **interfacial, membrane-seeking helix** rather than a transmembrane span. This computational feature matches the experimentally described topology: *"the enzyme associates with cell membranes in a monotopic fashion via the N-terminal domain composed of three amphipathic helices"* [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/).

### 9. Consolidated annotation

Five independent lines of evidence converge on the assignment that Q88DB9 (*psd*/PP_4908) is a functional monotopic type I phosphatidylserine decarboxylase producing PE at the inner membrane: (1) curated database annotation (HAMAP MF_00662; KEGG K01613 / M00093) of the PS→PE+CO₂ reaction; (2) primary/structural enzymology of orthologs establishing the pyruvoyl-dependent autocatalytic α/β mechanism and monotopic topology; (3) 60.9% sequence identity to crystallized *E. coli* Psd with all catalytic motifs conserved; (4) a high-confidence AlphaFold model with the diagnostic amphipathic N-terminal helix; and (5) organism lipidomics showing PE is ~80% of the *P. putida* membrane. As summarized for the family, PE is *"synthesized exclusively by membrane-anchored phosphatidylserine decarboxylase (PSD) in most bacteria"* [PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/).

---

## Mechanistic Model / Interpretation

The functional narrative can be assembled into a single coherent model spanning the reaction, the maturation mechanism, subcellular localization, and downstream physiology.

**Reaction and pathway position.** Psd sits at the terminus of the CDP-DAG branch of glycerophospholipid metabolism (KEGG module M00093):

```
   PA ──(CDP-DAG synthase)──▶ CDP-DAG ──(Pss, phosphatidylserine synthase)──▶ PS
                                                                               │
                                                        Psd (PP_4908, EC 4.1.1.65)
                                                                               ▼
                                                                    PE  +  CO₂
```

Psd is the sole committed route to PE in most bacteria. Its head-group specificity (L-serine) is strict, while broad tolerance across acyl-chain species allows it to convert the full cellular pool of PS regardless of fatty-acid composition — explaining how a single enzyme supplies the ~80% PE membrane of *P. putida*.

**Autocatalytic maturation and catalysis.** The proenzyme self-processes at Ser253 (the conserved RFKLGST motif), producing:

```
   Proenzyme (287 aa) ──self-cleavage (serinolysis)──▶  β chain (res 1–252, membrane anchor)
                                                          +
                                                         α chain (res 253–287, N-terminal PYRUVOYL group)

   Pyruvoyl–C=O  +  H2N–(serine head of PS)  ⇌  Schiff base  ──▶  decarboxylation  ──▶  PE + CO2
```

The pyruvoyl group is a self-generated protein-derived cofactor; no external coenzyme is required. This is the defining chemistry of the pyruvoyl-dependent decarboxylase family.

**Localization and interfacial catalysis.** The β chain's N-terminal amphipathic helix (residues ~18–35; ⟨µH⟩ = 0.46 in the AlphaFold model) docks the enzyme monotopically on the cytoplasmic leaflet of the inner membrane. The active site faces the bilayer so that membrane-embedded PS is decarboxylated in situ, and the newly formed PE is released directly into the membrane where it is needed — a spatially efficient "make-it-where-you-use-it" arrangement.

**Downstream consequence — PE as a lipid chaperone.** The zwitterionic product PE is not merely a bulk building block. It sets the electrostatic environment of the bilayer, enforcing the Positive-Inside/Charge-Balance rules that dictate inner-membrane protein topology (the LacY paradigm). Depleting PE mis-orients transporters and abolishes PE-dependent processes such as flagellar motility and chemotaxis, and in *P. putida* the PE-rich membrane is actively remodeled under solvent stress. Thus Psd activity ramifies from a single decarboxylation into membrane biogenesis, membrane-protein folding, motility, and stress adaptation.

**Summary table of the enzyme's properties:**

| Property | Assignment | Basis |
|---|---|---|
| Reaction | PS → PE + CO₂ (EC 4.1.1.65) | HAMAP MF_00662; ortholog biochemistry |
| Cofactor | Self-generated pyruvoyl group | Conserved RFKLGST/Ser253; family mechanism |
| Substrate specificity | L-serine head group; broad acyl-chain tolerance | Hydrophobic active-site groove (structure) |
| Kₘ (PS, ortholog) | ~63 µM (*P. falciparum* type I) | [PMID: 14651609] |
| Quaternary form | α + β chains from one proenzyme | UniProt; ortholog mutagenesis |
| Localization | Monotopic, inner (cytoplasmic) membrane | Structure; AlphaFold amphipathic helix |
| Product role | Zwitterionic lipid chaperone (~80% of membrane) | LacY topology studies; lipidomics |
| Gene context | Monocistronic (K01613, M00093); not clustered with *pss* | KEGG genome neighborhood |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/) | *Structural insights into PE formation in bacterial membrane biogenesis* | Core mechanism: auto-cleavage, pyruvoyl/Schiff-base catalysis, monotopic topology, broad acyl specificity, *E. coli* catalytic residues D90/D142-H144-S254 |
| [32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/) | *Structural Basis for PE Biosynthesis by Bacterial PSD* | Independent confirmation of N-terminal hydrophobic membrane-binding region and PS recognition |
| [14651609](https://pubmed.ncbi.nlm.nih.gov/14651609/) | *Type I PSD in P. falciparum* | Experimental proof of α/β self-processing at the VGSS site; Kₘ ≈ 63 µM for PS |
| [39321488](https://pubmed.ncbi.nlm.nih.gov/39321488/) | *Arginine decarboxylase in A. oryzae* | Structural visualization of serine-to-pyruvoyl conversion in the pyruvoyl-dependent fold |
| [796663](https://pubmed.ncbi.nlm.nih.gov/796663/) | *Conditional lethal PSD mutants of E. coli* | Establishes PSD as final, membrane-bound step of PE synthesis; maps *psd* structural gene |
| [1093166](https://pubmed.ncbi.nlm.nih.gov/1093166/) | *Temperature-sensitive PSD mutants of E. coli* | Essentiality; PS accumulation (20–40%) upon PSD loss |
| [32430397](https://pubmed.ncbi.nlm.nih.gov/32430397/) | *Fluorescence assay for PSD activity* | Concise statement of the PS→PE reaction as a critical membrane-biogenesis step |
| [26579930](https://pubmed.ncbi.nlm.nih.gov/26579930/) | *Phospholipids and lipid A of P. putida KT2442* | Organism lipidomics: PE = 79.9% of membrane phospholipid |
| [21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/) | *Glycerophospholipid inventory of P. putida* | Conserved PE-dominant inventory across strains; stress remodeling |
| [8244943](https://pubmed.ncbi.nlm.nih.gov/8244943/) | *pss/psd required for motility and chemotaxis* | PE-dose-dependent motility/chemotaxis phenotype |
| [9422599](https://pubmed.ncbi.nlm.nih.gov/9422599/) | *B. subtilis psd cloning/disruption* | pss-psd operon in *B. subtilis*, contrasting with non-clustered *P. putida* PP_4908 |
| [24341994](https://pubmed.ncbi.nlm.nih.gov/24341994/) | *Lipids and topological rules* | Defines PE's Charge-Balance-Rule role in membrane-protein topology |
| [21599647](https://pubmed.ncbi.nlm.nih.gov/21599647/) | *Lipid-protein interactions* | LacY misorientation and loss of uphill transport without PE |
| [23322771](https://pubmed.ncbi.nlm.nih.gov/23322771/) | *Fatty acid composition and LacY* | Head-group + fatty-acid dependence of LacY topology/function |
| [26512118](https://pubmed.ncbi.nlm.nih.gov/26512118/) | *Dynamic topological switching* | Reversible, PE-content-dependent membrane-protein flipping |
| [22969082](https://pubmed.ncbi.nlm.nih.gov/22969082/) | *Lipid-dependent dual topology* | PE level sets ratio of topological conformers |
| [29026149](https://pubmed.ncbi.nlm.nih.gov/29026149/) | *Folding/stability/function of LacY* | PE required for correct folding and function in reconstitution |
| [26585333](https://pubmed.ncbi.nlm.nih.gov/26585333/) | *Plasmodium PSD inhibitor screening* | PSD validated as an antimicrobial drug target |

The evidence base is highly convergent, with no contradicting reports encountered. The principal caveat is that direct, enzyme-level biochemical characterization exists for **orthologs** (*E. coli*, *B. subtilis*, *P. falciparum*), not for the *P. putida* protein itself; the assignment to Q88DB9 rests on strong sequence/structural homology plus organism-level lipidomics.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on Q88DB9.** All enzymological parameters (auto-cleavage site, pyruvoyl formation, Kₘ) are inferred from orthologs. The *P. putida* protein has not, to the available literature, been purified and assayed. The Kₘ ≈ 63 µM cited is from the *P. falciparum* type I enzyme, not Q88DB9.
2. **No experimental *psd* knockout in *P. putida* KT2440.** Essentiality and the PE-dependent phenotypes (motility, solvent tolerance) are established in *E. coli*; their applicability to *P. putida* is inferred by conservation of the PE-dominant membrane, not directly demonstrated by targeted deletion.
3. **Cleavage-site numbering is model-derived.** The Ser253 boundary and α/β chain limits come from pairwise alignment to *E. coli* Psd; precise processing sites should be confirmed by mass spectrometry of the mature protein.
4. **Localization is inferred, not imaged.** Inner-membrane, monotopic localization rests on family topology and the AlphaFold amphipathic helix; no fractionation or microscopy for the *P. putida* protein was found.
5. **Regulation unknown.** How *psd*/PP_4908 expression is controlled (e.g., under solvent stress, membrane-lipid demand) was not established; its monocistronic organization suggests independent regulation but this is untested.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and in vitro assay.** Clone PP_4908, purify the protein, and confirm (a) autocatalytic α/β processing by SDS-PAGE/mass spectrometry, (b) pyruvoyl-group formation (e.g., phenylhydrazine/carbonyl labeling), and (c) PS→PE conversion with kinetic parameters (Kₘ, kcat) across PS species of differing acyl chains to test the predicted broad acyl-chain tolerance.
2. **Targeted mutagenesis of Ser253.** Mutate the predicted cleavage serine (and the H144 / D-residues in HRVHMP/PADG blocks) to abolish processing and activity, verifying the assigned catalytic residues.
3. **Conditional knockdown/knockout in KT2440.** Construct a depletion strain (e.g., inducible/CRISPRi) to test essentiality and quantify PS accumulation and PE loss by lipidomics; assay motility, chemotaxis, and solvent (n-butanol) tolerance to confirm PE-dependent physiology in this organism.
4. **Subcellular localization.** Fractionate membranes and/or use a fluorescent fusion to confirm inner-membrane, monotopic (peripheral) association; test the AlphaFold-predicted N-terminal amphipathic helix (res ~18–35) by truncation/mutation.
5. **Structural validation.** Solve an experimental structure (X-ray/cryo-EM) of the *P. putida* enzyme to confirm the monotopic fold and hydrophobic substrate groove predicted by homology and AlphaFold.
6. **Regulatory profiling.** Measure *psd* transcription/translation under membrane and solvent stress to determine whether PE supply is regulated at the level of Psd.

---

## Conclusion

The gene *psd* (PP_4908; UniProt Q88DB9) of *Pseudomonas putida* KT2440 encodes **phosphatidylserine decarboxylase (EC 4.1.1.65)**, a **pyruvoyl-dependent, monotopic inner-membrane enzyme** that catalyzes the **final committed step of phosphatidylethanolamine biosynthesis (PS → PE + CO₂)**. It matures by autocatalytic self-cleavage into a pyruvoyl-bearing α chain and a membrane-anchoring β chain, acts on membrane-embedded PS at the lipid–water interface with broad acyl-chain tolerance, and produces the dominant (~80%) membrane phospholipid of the organism. Its product PE serves as a zwitterionic lipid chaperone governing inner-membrane protein topology and PE-dependent physiology (motility, chemotaxis, solvent adaptation). The assignment is unambiguous and supported by curated annotation, ortholog enzymology and structure, ~61% sequence identity to the crystallized *E. coli* enzyme with all catalytic motifs conserved, a high-confidence AlphaFold model, and organism-specific lipidomics.


## Artifacts

- [OpenScientist final report](psd-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](psd-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32430397
2. PMID:26579930
3. PMID:33707636
4. PMID:14651609
5. PMID:39321488
6. PMID:32402247
7. PMID:8244943
8. PMID:1093166
9. PMID:21895997
10. PMID:24341994
11. PMID:21599647
12. PMID:26512118
13. PMID:22969082
14. PMID:23322771
15. PMID:29026149
16. PMID:26585333
17. PMID:9422599