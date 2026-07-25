---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T12:09:04.018121'
end_time: '2026-07-25T12:23:47.154258'
duration_seconds: 883.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: purD
  gene_symbol: purD
  uniprot_accession: Q88DK2
  protein_description: 'RecName: Full=Phosphoribosylamine--glycine ligase {ECO:0000255|HAMAP-Rule:MF_00138};
    EC=6.3.4.13 {ECO:0000255|HAMAP-Rule:MF_00138}; AltName: Full=GARS {ECO:0000255|HAMAP-Rule:MF_00138};
    AltName: Full=Glycinamide ribonucleotide synthetase {ECO:0000255|HAMAP-Rule:MF_00138};
    AltName: Full=Phosphoribosylglycinamide synthetase {ECO:0000255|HAMAP-Rule:MF_00138};'
  gene_info: Name=purD {ECO:0000255|HAMAP-Rule:MF_00138}; OrderedLocusNames=PP_4823;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the GARS family. {ECO:0000255|HAMAP-
  protein_domains: ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); PreATP-grasp_dom_sf.
    (IPR016185); PRibGlycinamid_synth_ATP-grasp. (IPR020561); PRibGlycinamide_synth.
    (IPR000115)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: purD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: purD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DK2
- **Protein Description:** RecName: Full=Phosphoribosylamine--glycine ligase {ECO:0000255|HAMAP-Rule:MF_00138}; EC=6.3.4.13 {ECO:0000255|HAMAP-Rule:MF_00138}; AltName: Full=GARS {ECO:0000255|HAMAP-Rule:MF_00138}; AltName: Full=Glycinamide ribonucleotide synthetase {ECO:0000255|HAMAP-Rule:MF_00138}; AltName: Full=Phosphoribosylglycinamide synthetase {ECO:0000255|HAMAP-Rule:MF_00138};
- **Gene Information:** Name=purD {ECO:0000255|HAMAP-Rule:MF_00138}; OrderedLocusNames=PP_4823;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the GARS family. {ECO:0000255|HAMAP-
- **Key Domains:** ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); PreATP-grasp_dom_sf. (IPR016185); PRibGlycinamid_synth_ATP-grasp. (IPR020561); PRibGlycinamide_synth. (IPR000115)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "purD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'purD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **purD** (gene ID: purD, UniProt: Q88DK2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *purD* (PP_4823, UniProt Q88DK2) in *Pseudomonas putida* KT2440

**Gene:** *purD* | **Protein:** Phosphoribosylamine–glycine ligase / Glycinamide ribonucleotide (GAR) synthetase
**UniProt:** Q88DK2 (PUR2_PSEPK) | **Locus:** PP_4823 | **EC:** 6.3.4.13 | **KEGG KO:** K01945
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)

---

## Summary

The gene ***purD*** (locus **PP_4823**, UniProt **Q88DK2**) of *Pseudomonas putida* KT2440 encodes **glycinamide ribonucleotide (GAR) synthetase**, also called **phosphoribosylamine–glycine ligase** (**EC 6.3.4.13**), a member of the **GARS protein family** (HAMAP rule MF_00138). The gene identity is unambiguous: the gene symbol, EC number, protein family (GARS), and diagnostic ATP-grasp domain architecture all converge on a single, well-defined biochemical role. This enzyme catalyzes the **second committed step of de novo purine (IMP) biosynthesis**, condensing **5-phospho-β-D-ribosylamine (PRA)**, **glycine**, and **ATP** into **N¹-(5-phospho-β-D-ribosyl)glycinamide (GAR)**, releasing **ADP**, **inorganic phosphate (Pi)**, and a proton. The reaction requires a divalent metal cofactor (**Mg²⁺ or Mn²⁺**) and proceeds via an **ATP-grasp ligase mechanism** in which the glycine carboxylate is first phosphorylated to a reactive **glycyl-phosphate (acyl-phosphate) intermediate** that is then attacked by the amine of PRA to form the amide bond of GAR.

No *P. putida*-specific experimental characterization of this protein exists. However, the functional annotation rests on extremely strong evidence transfer. Q88DK2 is **75.1% identical (83.8% similar)** across its full length to the biochemically and structurally characterized *Escherichia coli* PurD (P15640), with no insertions or deletions in the catalytic regions and full conservation of the diagnostic active-site motifs. The *E. coli* enzyme has been definitively characterized by steady-state enzymology and isotope-labeling studies (Cheng et al., 1990), which established the **ordered sequential kinetic mechanism**, the **glycyl-phosphate intermediate** (via ¹⁸O transfer from glycine to Pi), and the enzyme's **strict specificity for glycine**. Crystal structures of thermophilic PurD orthologs further define the ATP-grasp fold and its mobile "B-domain." Because sequence identity across the catalytic and ATP-grasp regions is so high, these experimentally defined properties can be transferred to the *P. putida* enzyme with high confidence.

Functionally, PurD is a **soluble, monomeric, cytoplasmic enzyme** with no membrane-targeting or secretion signals — consistent with de novo purine biosynthesis being a cytosolic process in bacteria. In *P. putida* KT2440, *purD* (PP_4823) lies immediately downstream of and co-oriented with *purH* (PP_4822), recapitulating the conserved bacterial *purHD* gene arrangement. Its product GAR feeds directly into the downstream steps of the 10-reaction pathway that builds inosine monophosphate (IMP), the branch-point precursor of both AMP and GMP. Genetic studies in other bacteria confirm that loss of *purD* causes **purine auxotrophy** (and, in pathogens, attenuated growth and virulence), and that *purD* expression is controlled by cellular purine status through purine-responsive transcriptional regulators.

---

## Key Findings

### Finding 1 — purD encodes GAR synthetase, the second step of de novo purine biosynthesis

The core annotation of PP_4823 / Q88DK2 is **glycinamide ribonucleotide synthetase (GAR-syn, PurD)**, a 431-amino-acid, ~45.8 kDa enzyme assigned **EC 6.3.4.13** and classified in the **GARS family** by HAMAP rule MF_00138. The catalytic activity (Rhea:17453) is:

> **5-phospho-β-D-ribosylamine (PRA) + glycine + ATP → N¹-(5-phospho-β-D-ribosyl)glycinamide (GAR) + ADP + phosphate + H⁺**

This is the **second reaction of the de novo purine biosynthetic pathway**, following the amidophosphoribosyltransferase (PurF) step that produces PRA from 5-phosphoribosyl-1-pyrophosphate (PRPP) and glutamine. The enzyme contains an ATP-grasp domain (residues ~108–315). The crystallographic study of thermophilic PurD orthologs states the reaction and pathway position explicitly:

> *"Glycinamide ribonucleotide synthetase (GAR-syn, PurD) catalyses the second reaction of the purine biosynthetic pathway; the conversion of phosphoribosylamine, glycine and ATP to glycinamide ribonucleotide (GAR), ADP and Pi."* — [PMID: 20716513](https://pubmed.ncbi.nlm.nih.gov/20716513/)

This precisely defines both the chemical transformation and the enzyme's position as the second, committed step following formation of the unstable intermediate PRA.

### Finding 2 — ATP-grasp fold with a mobile B-domain; catalysis via a glycyl-phosphate intermediate

Q88DK2 carries an **ATP-grasp domain** (UniProt residues 108–315; InterPro IPR011761, IPR013815, IPR016185, IPR020561, IPR000115) and requires a divalent metal (**Mg²⁺ or Mn²⁺**). ATP-grasp enzymes are ATP-dependent ligases that characteristically clamp ATP between two lobes and use it to phosphorylate a carboxylate, generating a reactive **acyl-phosphate** intermediate. For GAR synthetase, ATP phosphorylates the glycine carboxylate to form **glycyl-phosphate**, which is then attacked by the amine of PRA to form the amide bond of GAR.

Crystal structures of PurD orthologs from *Thermus thermophilus*, *Geobacillus kaustophilus*, and *Aquifex aeolicus* (apo and ligand-bound) reveal a conserved multi-domain architecture with a **mobile B-domain** that closes over the active site during catalysis:

> *"the orientations of the B domains are varied among GAR-syn's and the MD simulation suggested the mobility of the B domain. Furthermore, it was demonstrated that the B loop in the B domain fixes the position of the β- and γ-phosphate groups of the bound ATP."* — [PMID: 20716513](https://pubmed.ncbi.nlm.nih.gov/20716513/)

The mobile B-loop positions the β- and γ-phosphates of ATP for in-line phosphoryl transfer — the structural basis for the ATP-grasp mechanism inferred for the *P. putida* enzyme.

### Finding 3 — Ordered kinetic mechanism, glycyl-phosphate intermediate, and strict glycine specificity

The definitive enzymology comes from the *E. coli* PurD ortholog (Cheng et al., 1990), a 430-residue, Mr 45,945 protein essentially identical in size to *P. putida* Q88DK2 (431 aa, ~45,837 Da). Initial-velocity, product-inhibition, and dead-end-inhibition studies established a **sequential ordered mechanism**:

- **Substrate binding order:** PRA first → MgATP → glycine
- **Product release order:** Pi first → MgADP → GAR

Isotope labeling directly demonstrated the phosphorylated intermediate: incubation of [¹⁸O]glycine with ATP and PRA gave **quantitative transfer of ¹⁸O from the glycine carboxylate to Pi**, proving that the glycine carboxylate is phosphorylated (forming glycyl-phosphate) before amide bond formation. The enzyme was also shown to be **strictly specific for glycine**:

> *"Initial velocity studies and product and dead-end inhibition studies are most consistent with a sequential ordered mechanism of substrate binding and product release in which PRA binds first followed by MgATP and then glycine; Pi leaves first, followed by loss of MgADP and finally GAR. Incubation of [18O]glycine, ATP, and PRA results in quantitative transfer of the 18O to Pi. GAR synthetase is very specific for its substrate glycine."* — [PMID: 2182115](https://pubmed.ncbi.nlm.nih.gov/2182115/)

This is the strongest mechanistic evidence available and, given the near-identity of the two enzymes, is transferable to the *P. putida* protein.

### Finding 4 — High-confidence orthology (75% identity) to biochemically characterized E. coli PurD

A Needleman–Wunsch global alignment (BLOSUM62) of Q88DK2 (*P. putida*, 431 aa) against P15640 (*E. coli* K-12 PurD / PUR2_ECOLI, 429 aa, UniProt evidence level 1) yields **325/433 = 75.1% identity** and **83.8% similarity**. Both share the same length class, the GARS family assignment, EC 6.3.4.13, and the ATP-grasp domain. Because the *E. coli* enzyme is experimentally characterized (steady-state kinetics; mechanism; crystallizable), and because the sequence identity is high and gap-free across the catalytic/ATP-grasp regions, the experimentally defined **reaction, substrate specificity, and mechanism can be transferred** to the *P. putida* protein with strong confidence. This orthology is the backbone licensing the functional annotation in the absence of direct *P. putida* experiments.

| Property | *P. putida* PurD (Q88DK2) | *E. coli* PurD (P15640) |
|---|---|---|
| Length | 431 aa | 429–430 aa |
| Mass | ~45.8 kDa | ~45.9 kDa |
| EC | 6.3.4.13 | 6.3.4.13 |
| Family | GARS | GARS |
| Domain | ATP-grasp | ATP-grasp |
| Oligomeric state | Monomer (inferred) | Monomer (experimental) |
| Global identity | — | 75.1% vs Q88DK2 |
| Evidence level | Inferred by orthology | Experimental (level 1) |

### Finding 5 — Conserved active-site signature motifs confirm an intact catalytic apparatus

Motif-level comparison of Q88DK2 vs *E. coli* P15640 confirms that the catalytic machinery is intact in the *P. putida* enzyme. The **N-terminal glycine-rich PRA/phosphosugar-binding loop** of the GxGGRE class is present in both (P. putida ⁷GSGGRE vs E. coli ⁷GNGGRE), and the **ATP-grasp lysine motif** (…KAD…) is conserved (P. putida K144 ≈ E. coli K145). The ATP-grasp region is near-identical (P. putida residues 108–140 `KDFLARHEIPTADYQNFTEIEPALAYLQEKGAP` vs E. coli `TKDFLARHKIPTAEYQNFTEVEPALAYLREKGA`), with no insertions or deletions in the catalytic regions. Conservation of both the substrate-binding loop and the ATP-binding lysine indicates a fully functional GAR-synthetase catalytic site.

### Finding 6 — Soluble, monomeric, cytoplasmic enzyme (no membrane targeting)

Q88DK2 has **no transmembrane segments, signal peptide, or lipidation features** in UniProt, and no localization-conferring keywords — its keywords are purely functional (ATP-binding, Ligase, Magnesium, Manganese, Metal-binding, Nucleotide-binding, Purine biosynthesis). Its biochemically characterized *E. coli* ortholog is annotated as a **monomer** and was purified to homogeneity as a single ~46 kDa polypeptide:

> *"Construction of an overproducing strain behind a lambda pL promoter allowed a 4-fold purification of the protein to homogeneity."* — [PMID: 2182115](https://pubmed.ncbi.nlm.nih.gov/2182115/)

Because de novo purine biosynthesis is a cytosolic process in bacteria, PurD acts as a **soluble, monomeric, cytoplasmic enzyme**. In mammalian cells, the homologous activities are combined into a trifunctional polypeptide (GARS-AIRS-GART) that may transiently assemble into a "purinosome" metabolon (see Evidence Base), but the bacterial enzyme is a standalone monomeric protein.

### Finding 7 — Genomic context: purHD-like gene pair feeding the IMP pathway

In *P. putida* KT2440, **PP_4823 (purD**, 5,485,241–5,486,536, + strand**)** lies immediately downstream of and co-oriented with **PP_4822 = purH** (K00602, AICAR transformylase / IMP cyclohydrolase, 5,483,487–5,485,094; 147 bp intergenic gap). This **purH–purD tandem** recapitulates the well-known *E. coli* *purHD* operon organization. The next gene, PP_4824, is an unrelated RetS-type sensor histidine kinase. KEGG assigns PP_4823 to KO **K01945** in the purine metabolism map (ppu00230). PurD's product **GAR** is the substrate of the next step, GAR transformylase (PurN/PurT), continuing the 10-step de novo route to **IMP**, from which AMP and GMP are subsequently made.

### Finding 8 — purD function is required for purine prototrophy; expression is purine-regulated

Genetic evidence from other bacteria establishes the physiological importance of the *purD* step:

- In *Xanthomonas oryzae* pv. *oryzae*, a *purD::Tn5* insertion mutant became **auxotrophic** (required exogenous purines plus thiamine in minimal medium) and showed **reduced virulence** on rice, without affecting expression of other *pur* genes:
  > *"the M793 mutant required exogenous purines and thiamine for growth in minimal media. These results indicate that the purD gene plays a crucial role in the growth and virulence of Xoo"* — [PMID: 17888004](https://pubmed.ncbi.nlm.nih.gov/17888004/)

- In *Lactococcus lactis*, the *purDEK* operon is required for growth in milk (a purine-poor medium), and its expression is transcriptionally regulated **~35-fold** by purine availability via a **PurBox activator element**:
  > *"The expression of the genes was regulated approximately 35-fold at the transcription level by the availability of purines in the growth medium."* — [PMID: 9797284](https://pubmed.ncbi.nlm.nih.gov/9797284/)

- In *Salmonella*/*E. coli*, *purD* transcription is repressed by the **PurR repressor** binding a PUR-box operator ([PMID: 11733076](https://pubmed.ncbi.nlm.nih.gov/11733076/); [PMID: 9683487](https://pubmed.ncbi.nlm.nih.gov/9683487/)).

These establish *purD* as an essential step whose loss blocks IMP synthesis (purine auxotrophy) and whose expression is tightly coupled to cellular purine status.

---

## Mechanistic Model / Interpretation

### Position in the pathway

De novo purine biosynthesis builds the purine ring stepwise onto a ribose-5-phosphate scaffold. PurD catalyzes step 2:

```
   PRPP
    │  glutamine  (PurF, amidophosphoribosyltransferase, EC 2.4.2.14)  ← step 1
    ▼
   PRA  (5-phospho-β-D-ribosylamine)   [unstable intermediate]
    │  + glycine + ATP → ADP + Pi
    │  ►►► PurD / GAR synthetase (EC 6.3.4.13)  ← step 2  [PP_4823, Q88DK2]
    ▼
   GAR  (N¹-(5-phospho-β-D-ribosyl)glycinamide)
    │  + N10-formyl-THF   (PurN/PurT, GAR transformylase)  ← step 3
    ▼
   FGAR  →  ... (further steps: PurL, PurM, PurE, PurK, PurC, PurB, PurH) ...
    ▼
   IMP  ──► AMP  (PurA/PurB)
       └──► GMP  (GuaB/GuaA)
```

Because PRA is chemically labile (half-life on the order of seconds at physiological pH), the PurD step effectively "captures" the fragile intermediate produced by PurF and locks the growing purine precursor into a stable amide.

### Catalytic mechanism (ATP-grasp)

```
Step A (phosphorylation):
   Glycine–COO⁻  +  ATP·Mg²⁺  ──►  Glycine–CO–O–PO₃²⁻ (glycyl-phosphate)  +  ADP·Mg²⁺

Step B (amide bond formation):
   Glycyl-phosphate  +  H₂N–(ribose-5-P)  ──►  GAR (amide bond)  +  Pi
```

Ordered binding (PRA → MgATP → glycine) and ordered release (Pi → MgADP → GAR) were established for the *E. coli* ortholog, and the ¹⁸O-transfer experiment provides direct chemical proof of the glycyl-phosphate intermediate. The mobile **B-domain** closes over the active site to sequester the reactive acyl-phosphate and align the ATP phosphates, a hallmark of the ATP-grasp superfamily.

### Localization and quaternary structure

PurD is a **soluble cytoplasmic monomer**. The reaction, its substrates, and its products are all cytosolic metabolites, and the protein bears no membrane anchor, signal peptide, or secretion tag. In bacteria the pathway enzymes act as discrete proteins (contrast the mammalian trifunctional GARS-AIRS-GART polypeptide and the transient purinosome metabolon).

### Regulation

Flux through this step is controlled at the transcriptional level in response to purine availability — via PurR repression (Enterobacteria) or PurBox activation (*Lactococcus*). This keeps GAR synthetase output matched to the cell's demand for purine nucleotides.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [20716513](https://pubmed.ncbi.nlm.nih.gov/20716513/) | *Crystal structures of GAR synthetase, PurD, from thermophilic eubacteria* | Defines the reaction/pathway position and the ATP-grasp fold with mobile B-domain (Findings 1, 2) |
| [2182115](https://pubmed.ncbi.nlm.nih.gov/2182115/) | *GAR synthetase from E. coli: cloning, overproduction, sequencing, isolation, characterization* | Ordered kinetic mechanism, ¹⁸O-transfer evidence for glycyl-phosphate, strict glycine specificity, monomeric homogeneous protein (Findings 3, 6) |
| [17888004](https://pubmed.ncbi.nlm.nih.gov/17888004/) | *Virulence/growth of a purine auxotroph of Xanthomonas oryzae pv. oryzae* | Genetic proof that *purD* loss → purine auxotrophy + reduced virulence (Finding 8) |
| [9797284](https://pubmed.ncbi.nlm.nih.gov/9797284/) | *Cloning/expression of L. lactis purDEK, required for growth in milk* | *purD* expression regulated ~35-fold by purine availability (Finding 8) |
| [9683487](https://pubmed.ncbi.nlm.nih.gov/9683487/) | *Activation control of pur genes in L. lactis (PurBox)* | PurBox activator element at *purD* promoter (Finding 8 context) |
| [11733076](https://pubmed.ncbi.nlm.nih.gov/11733076/) | *Adaptive mutations via purR super-repressor in S. typhimurium* | PurR represses *purD* via PUR-box operator (Finding 8 context) |
| [2147474](https://pubmed.ncbi.nlm.nih.gov/2147474/) | *Trifunctional GARS-AIRS-GART cloned by complementation of E. coli* | Establishes homology of bacterial purD/purM/purN to eukaryotic trifunctional enzyme |
| [33179964](https://pubmed.ncbi.nlm.nih.gov/33179964/) | *Human de novo purine biosynthesis* (review) | Pathway overview; purinosome/metabolon context (contrast to bacterial monomer) |
| [35331738](https://pubmed.ncbi.nlm.nih.gov/35331738/) | *Multienzyme interactions of PAICS facilitate purinosome formation* | Metabolic channeling context in eukaryotes |
| [32299949](https://pubmed.ncbi.nlm.nih.gov/32299949/) | *Metabolomics/MS imaging reveal channeled de novo purine synthesis* | Evidence for channeled synthesis in human cells (contrast) |
| [24413256](https://pubmed.ncbi.nlm.nih.gov/24413256/) | *Revisiting and revising the purinosome* | Critical view of purinosome; underscores bacterial enzymes act as discrete proteins |
| [30102358](https://pubmed.ncbi.nlm.nih.gov/30102358/) | *VAL1 (PurD) regulates rice leaf colour/cell division* | Plant PurD ortholog (chloroplast-localized); confirms conserved second-step enzyme identity |

**How the evidence fits together.** The two most decisive papers are the *E. coli* biochemical study ([PMID: 2182115](https://pubmed.ncbi.nlm.nih.gov/2182115/)) and the thermophilic crystal-structure study ([PMID: 20716513](https://pubmed.ncbi.nlm.nih.gov/20716513/)). Together they define both the chemistry (ordered mechanism, glycyl-phosphate intermediate, glycine specificity) and the structural basis (ATP-grasp fold, mobile B-domain). The 75% sequence identity of Q88DK2 to the *E. coli* enzyme, plus full conservation of active-site motifs, licenses transfer of these properties to *P. putida*. Genetic studies across diverse bacteria ([PMID: 17888004](https://pubmed.ncbi.nlm.nih.gov/17888004/), [PMID: 9797284](https://pubmed.ncbi.nlm.nih.gov/9797284/)) confirm the physiological role and regulation. The eukaryotic purinosome literature is included for completeness/contrast — it explains the multienzyme organization of this pathway in mammals but does **not** apply to the standalone bacterial monomer.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific experimental data.** There is no published biochemical, kinetic, structural, or genetic characterization of PP_4823 / Q88DK2 itself. Every mechanistic and structural claim is inferred by orthology (chiefly from *E. coli*) or family assignment. While the 75% identity and motif conservation make this inference robust, *P. putida*-specific kinetic parameters (Km, kcat, metal preference) are unknown.

2. **Regulation in *P. putida* not directly demonstrated.** The purine-responsive regulation described here (PurR repression; PurBox activation) is established in other taxa. Whether *P. putida* uses PurR, a PurBox-type activator, or another mechanism at the *purD* promoter has not been experimentally verified.

3. **Operon structure inferred from coordinates.** The *purHD*-like arrangement is inferred from genome coordinates and orientation. Direct transcriptional evidence (co-transcription, transcription start sites, operon boundaries) for *P. putida* PP_4822–PP_4823 was not examined.

4. **Structure is homology-based only.** No experimental structure of the *P. putida* enzyme exists; structural inferences derive from thermophilic orthologs and the *E. coli* enzyme.

5. **Metal cofactor specificity unresolved.** Mg²⁺ vs Mn²⁺ preference is annotated generically; the physiologically relevant metal in *P. putida* is not established.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic assay.** Clone PP_4823, purify the His-tagged protein, and measure GAR-synthetase activity (e.g., ADP/Pi release or [¹⁴C]glycine incorporation into GAR) to determine Km for PRA, glycine, and ATP, and kcat — confirming activity and quantifying substrate affinities for the *P. putida* enzyme specifically.

2. **Metal-dependence titration.** Assay activity across Mg²⁺ and Mn²⁺ concentrations to establish the preferred divalent cofactor.

3. **Substrate-specificity panel.** Test glycine analogs (alanine, serine, D-glycine) to confirm the strict glycine specificity predicted from the *E. coli* ortholog.

4. **Genetic complementation / auxotrophy test.** Construct a PP_4823 deletion in *P. putida* KT2440 and confirm purine auxotrophy (growth rescued by hypoxanthine/adenine); complement with the wild-type gene.

5. **Operon and regulation mapping.** Use RT-PCR/RNA-seq and 5′-RACE to test co-transcription of PP_4822–PP_4823 and identify the transcription start site; use reporter fusions ± exogenous purines to test purine-responsive regulation and search the promoter for PurR-box / PurBox-like elements.

6. **Structural validation.** Solve a crystal or cryo-EM structure of the *P. putida* enzyme (apo and ATP/PRA-bound) to confirm the ATP-grasp fold and B-domain closure, or generate and validate an AlphaFold model against the thermophilic templates.

---

## Conclusion

*purD* (PP_4823, UniProt Q88DK2) in *Pseudomonas putida* KT2440 encodes **glycinamide ribonucleotide (GAR) synthetase / phosphoribosylamine–glycine ligase (EC 6.3.4.13)**, the **ATP-grasp, Mg²⁺/Mn²⁺-dependent** enzyme catalyzing the **second step of de novo purine (IMP) biosynthesis**: condensation of **PRA + glycine + ATP → GAR + ADP + Pi**, via an ordered mechanism with a **glycyl-phosphate intermediate** and **strict glycine specificity**. It is a **soluble, monomeric, cytoplasmic** enzyme, encoded in a conserved *purHD*-like arrangement, whose product GAR feeds the downstream pathway to IMP and thence to AMP and GMP. The annotation is inferred from **75% identity** to the biochemically and structurally characterized *E. coli* enzyme, with all catalytic motifs conserved; no *P. putida*-specific experimental study yet exists.


## Artifacts

- [OpenScientist final report](purD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](purD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20716513
2. PMID:2182115
3. PMID:17888004
4. PMID:9797284
5. PMID:11733076
6. PMID:9683487