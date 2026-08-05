---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T14:15:39.900918'
end_time: '2026-07-23T14:43:03.826140'
duration_seconds: 1643.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murF
  gene_symbol: murF
  uniprot_accession: Q88N80
  protein_description: 'RecName: Full=UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine
    ligase {ECO:0000256|HAMAP-Rule:MF_02019, ECO:0000256|RuleBase:RU004136}; EC=6.3.2.10
    {ECO:0000256|HAMAP-Rule:MF_02019, ECO:0000256|RuleBase:RU004136}; AltName: Full=D-alanyl-D-alanine-adding
    enzyme {ECO:0000256|HAMAP-Rule:MF_02019};'
  gene_info: Name=murF {ECO:0000256|HAMAP-Rule:MF_02019, ECO:0000313|EMBL:AAN66956.1};
    OrderedLocusNames=PP_1333 {ECO:0000313|EMBL:AAN66956.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MurCDEF family. MurF subfamily.
  protein_domains: Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf.
    (IPR036615); Mur_ligase_cen. (IPR013221); Mur_ligase_N. (IPR000713)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N80
- **Protein Description:** RecName: Full=UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase {ECO:0000256|HAMAP-Rule:MF_02019, ECO:0000256|RuleBase:RU004136}; EC=6.3.2.10 {ECO:0000256|HAMAP-Rule:MF_02019, ECO:0000256|RuleBase:RU004136}; AltName: Full=D-alanyl-D-alanine-adding enzyme {ECO:0000256|HAMAP-Rule:MF_02019};
- **Gene Information:** Name=murF {ECO:0000256|HAMAP-Rule:MF_02019, ECO:0000313|EMBL:AAN66956.1}; OrderedLocusNames=PP_1333 {ECO:0000313|EMBL:AAN66956.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MurCDEF family. MurF subfamily.
- **Key Domains:** Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf. (IPR036615); Mur_ligase_cen. (IPR013221); Mur_ligase_N. (IPR000713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murF** (gene ID: murF, UniProt: Q88N80) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MurF (Q88N80, PP_1333) in *Pseudomonas putida* KT2440: The D-Alanyl-D-Alanine-Adding Ligase Completing the Cytoplasmic Peptidoglycan Precursor

**Gene:** murF (OrderedLocusName PP_1333) · **UniProt:** Q88N80 · **Organism:** *Pseudomonas putida* KT2440 (PSEPK) · **EC:** 6.3.2.10

## Summary

**murF** (UniProt **Q88N80**; ordered locus name **PP_1333**) of *Pseudomonas putida* KT2440 encodes **MurF**, the **ATP-dependent UDP-N-acetylmuramoyl-tripeptide : D-alanyl-D-alanine ligase (EC 6.3.2.10)**, also called the **D-alanyl-D-alanine-adding enzyme**. MurF catalyzes the **final cytoplasmic step of peptidoglycan (murein) precursor biosynthesis**: it condenses the preformed dipeptide **D-Ala-D-Ala** onto the terminal carboxylate of the **UDP-MurNAc-tripeptide** (UDP-N-acetylmuramoyl-L-Ala-γ-D-Glu-*meso*-diaminopimelate) to produce **UDP-MurNAc-pentapeptide** ("Park's nucleotide"), with concomitant hydrolysis of ATP to ADP and inorganic phosphate. This is the last soluble, cytoplasmic reaction before the nucleotide precursor is handed off to the membrane-associated translocase MraY and the rest of the lipid-linked pathway.

The identity of the target is well supported. The UniProt description, the MurCDEF/MurF-subfamily assignment, and the diagnostic InterPro Mur-ligase domains (Mur_ligase_N IPR000713, Mur_ligase_cen IPR013221, Mur_ligase_C IPR004101) all match a canonical MurF ligase. Although no biochemical study has yet been published on the *P. putida* KT2440 enzyme itself, its closest characterized ortholog — **MurF of *Pseudomonas aeruginosa* (PaMurF)** — has been crystallized and enzymatically characterized, and both organisms are γ-proteobacteria that build *meso*-diaminopimelate (*meso*-DAP)-type peptidoglycan. Deep mechanistic and structural knowledge from *P. aeruginosa* and *Escherichia coli* orthologs therefore transfers with high confidence to PP_1333, and this report draws on that body of work while flagging where evidence is by homology rather than direct measurement.

The core conclusions are: (1) MurF performs a defined ATP-dependent amide-bond-forming ligation via an **acyl-phosphate intermediate** and an **ordered kinetic mechanism**, placing it in the Mur/folyl-poly-γ-glutamate ligase superfamily; (2) it is a soluble **cytoplasmic** three-domain enzyme that undergoes a large **open-to-closed conformational change** upon substrate binding; (3) it is **essential and bacteria-specific with no human homolog**, making it a validated antibacterial drug target; and (4) it is **permissive at the incoming dipeptide** (accepting D-Ala-D-Lac depsipeptides and fluorinated analogs) while remaining specific for the UDP-MurNAc-tripeptide acceptor. The D-Ala-D-Ala terminus that MurF installs is the eventual substrate for transpeptidase cross-linking and is the molecular target of glycopeptide antibiotics such as vancomycin.

---

## Gene and Protein Identity Verification

Before presenting the functional analysis, the target identity was verified against the UniProt reference data, as mandated by the research brief:

| Attribute | Expected (UniProt Q88N80) | Assessment |
|-----------|---------------------------|------------|
| Gene symbol | *murF* | ✔ Canonical name for the D-Ala-D-Ala-adding enzyme |
| Protein / EC | UDP-N-acetylmuramoyl-tripeptide–D-alanyl-D-alanine ligase; EC 6.3.2.10 | ✔ Matches characterized MurF orthologs |
| Organism | *Pseudomonas putida* KT2440 (PSEPK) | ✔ γ-proteobacterium, *meso*-DAP peptidoglycan |
| Family | MurCDEF family, MurF subfamily | ✔ Consistent with domain architecture |
| Domains | Mur_ligase_N/cen/C (IPR000713/013221/004101) | ✔ Diagnostic three-domain Mur-ligase fold |

**Conclusion of verification:** The gene symbol *murF* is **not ambiguous** in this context; it unambiguously denotes the D-Ala-D-Ala-adding ligase. The domain complement and family assignment align precisely with the well-studied MurF orthologs. The only caveat is that the primary experimental literature characterizes the *E. coli* and *P. aeruginosa* enzymes rather than the *P. putida* KT2440 protein directly; functional claims for PP_1333 are therefore made by strong orthology, which is appropriate given the extreme conservation of this essential housekeeping enzyme across γ-proteobacteria.

---

## Key Findings

### Finding 1 — MurF is the ATP-dependent D-Ala-D-Ala-adding ligase catalyzing the final cytoplasmic step of peptidoglycan precursor synthesis

MurF catalyzes the reaction:

```
UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP  +  D-Ala-D-Ala  +  ATP
        │
        ▼   (MurF, EC 6.3.2.10)
UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala-D-Ala  +  ADP  +  Pi
        (UDP-MurNAc-pentapeptide = "Park's nucleotide")
```

This is the **last cytoplasmic step** of the nucleotide-precursor (Mur pathway) branch of peptidoglycan synthesis. The enzyme forms a peptide (amide) bond between the free amino group of the D-Ala-D-Ala dipeptide and the C-terminal carboxyl group of the *meso*-DAP (third) residue of the UDP-MurNAc-tripeptide, using the energy of ATP hydrolysis to activate the acceptor carboxylate. For the *P. aeruginosa* ortholog — the closest characterized relative to the *P. putida* enzyme — the substrate is explicitly **UDP-MurNAc-Ala-Glu-*meso*-A2pm** ([PMID: 19099588](https://pubmed.ncbi.nlm.nih.gov/19099588/)): *"MurF catalyzes the formation of a peptide bond between D-Alanyl-D-Alanine (D-Ala-D-Ala) and the cell wall precursor uridine 5'-diphosphoryl N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-diaminopimelic acid ... with the concomitant hydrolysis of ATP to ADP and inorganic phosphate, yielding UDP-N-acetylmuramyl-pentapeptide."* The presence of *meso*-DAP as the third stem residue is characteristic of *Pseudomonas* and most Gram-negative bacteria, and confirms that the *P. putida* enzyme operates on the DAP-type precursor.

Quantitative biochemistry of the purified *E. coli* enzyme establishes the catalytic parameters: MurF is a **~49 kDa monomer** with a **turnover number of 784 min⁻¹** for ATP-driven amide bond formation ([PMID: 2186811](https://pubmed.ncbi.nlm.nih.gov/2186811/)): *"The enzyme is a monomer of molecular weight 49,000, and it has a turnover number of 784 min-1 for ATP-driven amide bond formation."* That MurF represents the **last step in the cytoplasmic phase** of peptidoglycan biosynthesis is directly stated for the *P. aeruginosa* ortholog ([PMID: 23695563](https://pubmed.ncbi.nlm.nih.gov/23695563/)): *"The ATP-dependent UDP-MurNAc-tripeptide:D-Ala-D-Ala ligase MurF catalyses the last step in the cytoplasmic phase of peptidoglycan biosynthesis."*

### Finding 2 — Mechanism: ordered kinetics and an acyl-phosphate intermediate within the Mur/folyl-polyglutamate ligase superfamily

MurF belongs to the **MurCDEF amide-ligase family**, which shares four conserved sequence motifs with the **folyl-poly-γ-glutamate ligases**, together forming a defined ligase superfamily. Both families operate by the same chemical logic: **ATP first phosphorylates the C-terminal carboxylate** of the nucleotide substrate (the *meso*-DAP carboxylate in the case of MurF), generating a reactive **acyl-phosphate intermediate**; the amino group of the incoming nucleophile (D-Ala-D-Ala for MurF) then attacks this activated carbonyl, displacing phosphate and forming the new amide bond. The reaction follows an **ordered kinetic mechanism**. This was established through comparative sequence and mutational analysis ([PMID: 9166795](https://pubmed.ncbi.nlm.nih.gov/9166795/)): *"both enzyme families proceed through an ordered kinetic mechanism and form product via an acyl phosphate intermediate."*

The same study validated the catalytic importance of conserved residues by site-directed mutagenesis. Mutation of conserved *E. coli* MurF residues (**E158** and **H188**) reduced specific activity by **200- to 4500-fold** ([PMID: 9166795](https://pubmed.ncbi.nlm.nih.gov/9166795/)): *"All mutations were highly detrimental to activity with enzyme specific activity reductions of 200-4500-fold, validating the critical nature of these residues."* Consistent with this, the temperature-sensitive *murF2* (A288T) allele was 181-fold less active, linking the biochemical lesion to the physiological cell-shape/lysis phenotype of *murF* mutants. These conserved residues are expected to be present in the *P. putida* ortholog given the family-wide conservation.

### Finding 3 — Three-domain architecture with a large open-to-closed conformational change

The crystal structure of *E. coli* MurF (2.3 Å) reveals **three consecutive open α/β-sheet domains** ([PMID: 11090285](https://pubmed.ncbi.nlm.nih.gov/11090285/)): *"It contains three consecutive open alpha/beta-sheet domains."* These comprise (i) a topologically unique N-terminal domain, (ii) a central mononucleotide-binding fold, and (iii) a C-terminal dinucleotide-binding (Rossmann-like) fold — the classic Mur-ligase architecture corresponding to the InterPro domains carried by Q88N80 (Mur_ligase_N IPR000713, Mur_ligase_cen IPR013221, Mur_ligase_C IPR004101).

Critically, the **apo enzyme is catalytically incompetent**: it adopts an open, crescent-like conformation with a wide substrate-binding cleft in which the substrates cannot be brought into productive alignment ([PMID: 11090285](https://pubmed.ncbi.nlm.nih.gov/11090285/)): *"The apo-enzyme of MurF crystal structure reveals an open conformation with the three domains juxtaposed in a crescent-like arrangement creating a wide-open space where substrates are expected to bind. As such, catalysis is not feasible and significant domain closure is expected upon substrate binding."* This **induced-fit domain closure** is a hallmark of the Mur ligase family and a key consideration for structure-based inhibitor design.

Direct structural evidence in the *Pseudomonas* lineage comes from **PaMurF**, which was crystallized in complex with its UDP-MurNAc-tripeptide substrate (1.92 Å, space group P2₁2₁2₁), capturing the substrate-liganded form for the first time ([PMID: 23695563](https://pubmed.ncbi.nlm.nih.gov/23695563/)): *"allowing study of the enzyme in the substrate-liganded form for the first time."* Because PaMurF is the nearest characterized ortholog of PP_1333, this substrate-bound structure is the best available structural proxy for the *P. putida* enzyme.

### Finding 4 — Essential, cytoplasmic, bacteria-specific enzyme and validated antibacterial target

MurF is **essential for bacterial viability** and is **confined to eubacteria with no human homolog**, making it an attractive target for new antibacterials. The enzyme functions in the **cytoplasm** (intracellular stage of peptidoglycan synthesis). Its essentiality and drug-target status are stated explicitly for *P. aeruginosa* ([PMID: 19099588](https://pubmed.ncbi.nlm.nih.gov/19099588/)): *"we targeted the essential MurF enzyme of the antibiotic resistant pathogen Pseudomonas aeruginosa"* — and generally for MurF ([PMID: 23878932](https://pubmed.ncbi.nlm.nih.gov/23878932/)): *"MurF is an essential bacterial enzyme that is involved in the last intracellular stage of peptidoglycan biosynthesis, and therefore it has the potential to be exploited as a target for the development of new antibacterials."*

The target has been experimentally engaged: a **phage-display-derived peptide inhibitor (MurFp1)** was raised against *P. aeruginosa* MurF (IC₅₀ ≈ 250 µM, Ki ≈ 420 µM), acting by interfering with utilization of the D-Ala-D-Ala substrate. Multiple additional inhibitor classes have been developed against the MurC–F ligases, including **azastilbenes** ([PMID: 33744441](https://pubmed.ncbi.nlm.nih.gov/33744441/)), **flavonoids** (quercitrin, myricetin, (-)-epicatechin) ([PMID: 37796382](https://pubmed.ncbi.nlm.nih.gov/37796382/)), and virtual-screening hits against *S. pneumoniae* and *E. coli* MurF ([PMID: 23878932](https://pubmed.ncbi.nlm.nih.gov/23878932/)).

Genomically, *murF* sits within the **division-and-cell-wall (dcw) gene cluster** that co-locates peptidoglycan-synthesis and cell-division genes; in *E. coli*, *murE* and *murF* may be **translationally coupled** ([PMID: 2681153](https://pubmed.ncbi.nlm.nih.gov/2681153/)): *"the murE and murF genes, encoding the meso-diaminopimelic acid and D-alanyl-D-alanine-adding enzymes, respectively, may be translationally coupled."* This organization couples MurF expression to that of the upstream ligases, ensuring stoichiometric precursor flux.

### Finding 5 — Relaxed specificity at the dipeptide: incorporation of D-Ala-D-Lac and fluorinated analogs

MurF is **permissive at the incoming dipeptide** while remaining specific for the UDP-MurNAc-tripeptide acceptor. In *Lactobacillus plantarum*, the depsipeptide **D-alanyl-D-lactate (D-Ala-D-Lac)** produced by the Ddl ligase is added to the precursor by MurF, generating a D-Lac-terminated pentapeptide that confers **intrinsic vancomycin resistance** (vancomycin binds D-Ala-D-Ala but not D-Ala-D-Lac) ([PMID: 17400741](https://pubmed.ncbi.nlm.nih.gov/17400741/)): *"The ligase Ddl of L. plantarum plays a central role in this specificity by synthesizing D-alanyl-D-lactate depsipeptides that are added to the precursor peptide chain by the enzyme MurF."* Similarly, *E. coli* MurF incorporates **fluorinated dipeptides** (D-trifluoroAla-D-trifluoroAla) synthesized by the upstream Ddl ligase ([PMID: 2186811](https://pubmed.ncbi.nlm.nih.gov/2186811/)): *"which the D-Ala-D-Ala-adding enzyme can then incorporate to form UDP-N-acetylmuramyl-L-Ala-gamma-D-Glu-meso-2,6-diaminopimelyl-D-trifluoroAla-D-trifluoroAla."* This tolerance has two implications: mechanistically, it shows the dipeptide-binding subsite accepts ester/depsipeptide and halogenated substitutions; and physiologically, the substrate specificity that determines the D-Ala-D-Ala vs. D-Ala-D-Lac terminus is set largely by the upstream Ddl ligase rather than by MurF itself.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent picture of MurF as the terminal cytoplasmic node of the Mur pathway. The full cytoplasmic assembly line, with MurF at the end, is:

```
UDP-GlcNAc
   │ MurA (enolpyruvyl transfer) + MurB (reduction)
   ▼
UDP-MurNAc
   │ MurC  (+ L-Ala)
   ▼
UDP-MurNAc-L-Ala
   │ MurD  (+ D-Glu)
   ▼
UDP-MurNAc-L-Ala-γ-D-Glu
   │ MurE  (+ meso-DAP)          ← translationally coupled to murF in E. coli
   ▼
UDP-MurNAc-tripeptide  ──────────────┐
                                      │  Ddl:  2 D-Ala → D-Ala-D-Ala
                                      │        (or D-Ala-D-Lac / fluoro-analogs)
   ┌──────────────────────────────────┘
   │ ***MurF*** (+ D-Ala-D-Ala, + ATP)   ← THIS ENZYME, PP_1333
   ▼
UDP-MurNAc-PENTAPEPTIDE  ("Park's nucleotide")   [cytoplasm — final soluble step]
   │ MraY (membrane) → Lipid I → MurG → Lipid II → flippase → PBP transpeptidation
   ▼
Cross-linked peptidoglycan sacculus
```

**Chemical mechanism (single active site, sequential/ordered):**

```
Step 1 (activation):   R–COO⁻  +  ATP  →  R–CO–OPO₃²⁻ (acyl-phosphate)  +  ADP
                       (R–COO⁻ = meso-DAP terminal carboxylate of UDP-MurNAc-tripeptide)

Step 2 (ligation):     R–CO–OPO₃²⁻  +  H₂N–(D-Ala-D-Ala)  →  R–CO–NH–(D-Ala-D-Ala)  +  Pi
                       (amide-bond formation, releasing inorganic phosphate)
```

Catalysis requires the enzyme to transition from its **open, incompetent apo conformation** to a **closed conformation** that clamps the three domains around the nucleotide substrate, the dipeptide, and Mg·ATP, aligning the acyl-phosphate with the attacking amine. Conserved residues such as E158 and H188 (E. coli numbering) participate in this chemistry; their mutation collapses activity by orders of magnitude.

Two specificity principles emerge. First, MurF is **highly specific for the nucleotide-sugar acceptor** (the UDP-MurNAc-tripeptide with its *meso*-DAP third residue) — this is the recognition element that keeps the enzyme committed to peptidoglycan synthesis. Second, MurF is **comparatively relaxed toward the dipeptide donor**, incorporating D-Ala-D-Lac and fluorinated dipeptides. The physiological consequence is that the choice between a vancomycin-sensitive (D-Ala-D-Ala) and vancomycin-resistant (D-Ala-D-Lac) precursor is dictated upstream by the Ddl ligase and by dipeptidases (e.g., Aad/VanX-like enzymes), not by MurF. In *P. putida* KT2440, which uses standard D-Ala-D-Ala chemistry, MurF supplies the canonical pentapeptide whose terminal D-Ala-D-Ala is subsequently consumed by penicillin-binding-protein transpeptidases during wall cross-linking.

**Localization:** MurF is a **soluble cytoplasmic protein**. It has no signal peptide or transmembrane segment, and its product (Park's nucleotide) is the last water-soluble intermediate before MraY tethers the muramyl-pentapeptide to the membrane carrier undecaprenyl phosphate. Its ~49 kDa monomeric character and three-domain α/β fold are consistent with a freely diffusing cytoplasmic enzyme.

---

## Evidence Base

| PMID | Study (organism / type) | How it supports the findings |
|------|-------------------------|------------------------------|
| [19099588](https://pubmed.ncbi.nlm.nih.gov/19099588/) | Phage-display inhibitor of *P. aeruginosa* MurF | Defines the exact reaction and substrates (incl. *meso*-A2pm) for the closest *Pseudomonas* ortholog; establishes essentiality and drug-target status (F1, F4) |
| [23695563](https://pubmed.ncbi.nlm.nih.gov/23695563/) | Crystallization of PaMurF (*P. aeruginosa*) | Confirms MurF as the last cytoplasmic step; substrate-liganded structure of the nearest ortholog (F1, F3) |
| [2186811](https://pubmed.ncbi.nlm.nih.gov/2186811/) | Purification/characterization of *E. coli* MurF | 49 kDa monomer, kcat 784 min⁻¹; incorporation of fluorinated dipeptides (F1, F5) |
| [9166795](https://pubmed.ncbi.nlm.nih.gov/9166795/) | Mutational/ligase-superfamily analysis (*E. coli*) | Acyl-phosphate intermediate, ordered mechanism, catalytic residues E158/H188 (F2) |
| [11090285](https://pubmed.ncbi.nlm.nih.gov/11090285/) | Crystal structure of *E. coli* MurF, 2.3 Å | Three-domain α/β architecture; open apo conformation requiring domain closure (F3) |
| [17400741](https://pubmed.ncbi.nlm.nih.gov/17400741/) | *L. plantarum* Aad/D-Lac incorporation | MurF adds D-Ala-D-Lac depsipeptides → relaxed dipeptide specificity, vancomycin resistance (F5) |
| [2681153](https://pubmed.ncbi.nlm.nih.gov/2681153/) | *E. coli* murE-murG region organization | *murF* in the dcw cluster; *murE-murF* translational coupling (F4) |
| [23878932](https://pubmed.ncbi.nlm.nih.gov/23878932/) | *S. pneumoniae* MurF biochemistry + inhibitor screen | Essentiality, intracellular localization, drug-target validation (F4) |
| [37796382](https://pubmed.ncbi.nlm.nih.gov/37796382/) | Flavonoid MurF inhibitors | MurF as antibacterial target; conserved, bacteria-exclusive Mur ligases (F4) |
| [33744441](https://pubmed.ncbi.nlm.nih.gov/33744441/) | Azastilbene Mur ligase inhibitors | Mur ligases essential and druggable (F4) |
| [28201974](https://pubmed.ncbi.nlm.nih.gov/28201974/) | Review: Mur ligase inhibitors | Places MurF within the peptidoglycan pathway; shared catalytic mechanism/structure (F1, F4) |
| [34118719](https://pubmed.ncbi.nlm.nih.gov/34118719/) | Review: *M. tuberculosis* Mur enzymes | MurA–F confined to eubacteria, absent in humans; conserved catalytic mechanism (F4) |
| [39202871](https://pubmed.ncbi.nlm.nih.gov/39202871/) | Multi-pharmacology antibacterials | Supports MurF as an antibacterial target (F4) |

The literature is internally consistent: structural, kinetic, mutational, and genetic lines of evidence converge on the same reaction and mechanism, and there are no contradictory reports. The main gap is that all direct enzymology derives from orthologs (*E. coli*, *P. aeruginosa*, *S. pneumoniae*, *L. plantarum*) rather than from *P. putida* KT2440 itself.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on PP_1333.** Every mechanistic, kinetic, and structural claim is transferred by orthology, chiefly from *P. aeruginosa* (structural proxy) and *E. coli* (enzymology). While the conservation of this essential housekeeping enzyme across γ-proteobacteria makes this inference strong, the specific kinetic constants (Km, kcat), optimal Mg²⁺/pH conditions, and exact catalytic residues of the *P. putida* enzyme have not been measured.
2. **Essentiality inferred, not demonstrated in *P. putida*.** MurF is essential in *E. coli*, *P. aeruginosa*, and *S. pneumoniae*; the same is expected in *P. putida* KT2440, but no conditional-knockout or transposon-essentiality confirmation specific to PP_1333 is cited here.
3. **Structural model is an ortholog, not the target.** The best structure is PaMurF (similar but not identical sequence). A *P. putida* structure or an AlphaFold model validated against PaMurF would refine active-site details.
4. **Catalytic-residue numbering is from *E. coli*.** The E158/H188 assignments require sequence alignment to map onto Q88N80; the equivalent residues in PP_1333 were not explicitly identified in this investigation.
5. **Regulation and interactions.** Whether *P. putida* MurF is translationally coupled to *murE* (as in *E. coli*), and whether it participates in any cytoplasmic precursor-channeling complex with other Mur enzymes, is unverified for this organism.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm the ortholog mapping in silico.** Align Q88N80 against *E. coli* MurF and PaMurF to (i) confirm conservation of the catalytic E158/H188-equivalent residues and the four Mur/folyl-polyglutamate ligase motifs, and (ii) generate/validate an AlphaFold model against the PaMurF substrate-bound structure ([PMID: 23695563](https://pubmed.ncbi.nlm.nih.gov/23695563/)).
2. **Recombinant enzymology.** Clone, express, and purify PP_1333; measure Km for ATP, D-Ala-D-Ala, and UDP-MurNAc-tripeptide, plus kcat, using a coupled phosphate-release or radiochemical assay — benchmarking against the *E. coli* kcat of 784 min⁻¹ ([PMID: 2186811](https://pubmed.ncbi.nlm.nih.gov/2186811/)).
3. **Test dipeptide permissiveness in *P. putida*.** Assay incorporation of D-Ala-D-Lac and D-Ala-D-Ser analogs to determine whether PP_1333 shares the relaxed donor specificity seen in *L. plantarum* MurF ([PMID: 17400741](https://pubmed.ncbi.nlm.nih.gov/17400741/)) — relevant to intrinsic glycopeptide susceptibility.
4. **Genetic essentiality.** Construct a conditional (e.g., arabinose- or IPTG-dependent) *murF* allele in KT2440 to formally demonstrate essentiality and characterize the depletion phenotype (cell shape, lysis).
5. **Structure determination.** Crystallize or cryo-EM the *P. putida* enzyme with substrate/ADP to capture the closed, catalytically competent conformation directly for this organism.
6. **Inhibitor cross-testing.** Evaluate reported Mur ligase inhibitors (azastilbenes, flavonoids, MurFp1-type peptides) against purified PP_1333 to assess conservation of druggable pockets across *Pseudomonas* species ([PMID: 19099588](https://pubmed.ncbi.nlm.nih.gov/19099588/), [37796382](https://pubmed.ncbi.nlm.nih.gov/37796382/), [33744441](https://pubmed.ncbi.nlm.nih.gov/33744441/)).

---

## Conclusion

**murF / PP_1333 / Q88N80** in *Pseudomonas putida* KT2440 encodes **MurF**, the essential, cytoplasmic, ATP-dependent **UDP-N-acetylmuramoyl-tripeptide : D-alanyl-D-alanine ligase (EC 6.3.2.10)**. It catalyzes the **final soluble step of peptidoglycan-precursor biosynthesis**, ligating **D-Ala-D-Ala** onto **UDP-MurNAc-L-Ala-γ-D-Glu-*meso*-DAP** to make **UDP-MurNAc-pentapeptide**, using an **acyl-phosphate intermediate** and an **ordered kinetic mechanism** in a **three-domain fold that closes over its substrates**. The enzyme is **specific for the UDP-MurNAc-tripeptide acceptor but permissive at the dipeptide donor**, is **bacteria-specific with no human homolog**, and is a **validated antibacterial drug target**. All conclusions rest on strong orthology to the well-characterized *P. aeruginosa* and *E. coli* enzymes; direct characterization of the *P. putida* protein remains the principal outstanding experimental need.


## Artifacts

- [OpenScientist final report](murF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19099588
2. PMID:2186811
3. PMID:23695563
4. PMID:9166795
5. PMID:11090285
6. PMID:23878932
7. PMID:33744441
8. PMID:37796382
9. PMID:2681153
10. PMID:17400741