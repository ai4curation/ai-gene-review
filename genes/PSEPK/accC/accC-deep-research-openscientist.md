---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T06:53:39.355729'
end_time: '2026-07-23T08:33:58.847560'
duration_seconds: 6019.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: accC
  gene_symbol: accC
  uniprot_accession: Q88QD6
  protein_description: 'RecName: Full=Biotin carboxylase {ECO:0000256|ARBA:ARBA00017242,
    ECO:0000256|RuleBase:RU365063}; EC=6.3.4.14 {ECO:0000256|ARBA:ARBA00013263, ECO:0000256|RuleBase:RU365063};
    AltName: Full=Acetyl-coenzyme A carboxylase biotin carboxylase subunit A {ECO:0000256|ARBA:ARBA00033786,
    ECO:0000256|RuleBase:RU365063};'
  gene_info: Name=accC {ECO:0000313|EMBL:AAN66185.1}; OrderedLocusNames=PP_0558 {ECO:0000313|EMBL:AAN66185.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ACC_Biotin_Carboxylase. (IPR051602); Acetyl_CoA_COase_biotin_COase.
    (IPR004549); ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); BC-like_N.
    (IPR005481)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: accC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: accC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QD6
- **Protein Description:** RecName: Full=Biotin carboxylase {ECO:0000256|ARBA:ARBA00017242, ECO:0000256|RuleBase:RU365063}; EC=6.3.4.14 {ECO:0000256|ARBA:ARBA00013263, ECO:0000256|RuleBase:RU365063}; AltName: Full=Acetyl-coenzyme A carboxylase biotin carboxylase subunit A {ECO:0000256|ARBA:ARBA00033786, ECO:0000256|RuleBase:RU365063};
- **Gene Information:** Name=accC {ECO:0000313|EMBL:AAN66185.1}; OrderedLocusNames=PP_0558 {ECO:0000313|EMBL:AAN66185.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACC_Biotin_Carboxylase. (IPR051602); Acetyl_CoA_COase_biotin_COase. (IPR004549); ATP-grasp. (IPR011761); ATP_grasp_subdomain_1. (IPR013815); BC-like_N. (IPR005481)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "accC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'accC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **accC** (gene ID: accC, UniProt: Q88QD6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *accC* (Biotin Carboxylase, Q88QD6) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**accC** (gene locus **PP_0558**; UniProt **Q88QD6**) of *Pseudomonas putida* KT2440 encodes **biotin carboxylase (BC)**, the **biotin carboxylase subunit A of acetyl-CoA carboxylase (ACC)** (EC 6.3.4.14). Its primary, and essentially sole, molecular function is to catalyze the **ATP-dependent carboxylation of the biotin prosthetic group** that is covalently attached to the biotin carboxyl carrier protein (BCCP/AccB), using **bicarbonate (HCO₃⁻)** as the carboxyl donor and requiring **Mg²⁺**. This is the **first of the two half-reactions of acetyl-CoA carboxylase**, which together constitute the **first committed and rate-limiting step of fatty acid (membrane phospholipid) biosynthesis**. BC is a **soluble, cytoplasmic** enzyme that functions as a **homodimer** within the transient multi-subunit ACC complex.

Reaction catalyzed (BC half-reaction):
> ATP + HCO₃⁻ + biotinyl-[BCCP]  →  ADP + phosphate + carboxybiotinyl-[BCCP]

Overall ACC pathway (UniPathway UPA00655, "malonyl-CoA from acetyl-CoA: step 1/1"):
> acetyl-CoA + HCO₃⁻ + ATP  →  malonyl-CoA + ADP + Pi

---

## 2. Gene/Protein Identity Verification

The gene symbol **accC is unambiguous** and universally denotes **biotin carboxylase** across bacteria; there is no conflicting gene using this symbol. The assignment is fully consistent across every line of evidence:

| Attribute | Value (UniProt Q88QD6 / this analysis) |
|---|---|
| Protein | Biotin carboxylase; ACC biotin carboxylase subunit A |
| EC number | 6.3.4.14 (biotin carboxylase) |
| Gene / locus | *accC* / PP_0558 |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) |
| Length | 451 aa |
| Key domains | Biotin_carboxylation (res. 4–448); **ATP-grasp** (res. 123–320); Pfam PF00289, PF02785, PF02786; InterPro IPR004549, IPR011761, IPR013815, IPR005481 |
| Pathway | Lipid metabolism → malonyl-CoA biosynthesis (UPA00655), step 1/1 |
| Ligands (keywords) | ATP, biotin, Mg²⁺ |
| KEGG / BioCyc | ppu:PP_0558 / PPUT160488:G1G01-608-MONOMER |

Because the UniProt protein-existence level is **"Predicted"**, the functional annotation here rests primarily on **orthology and conservation** to biochemically and structurally characterized biotin carboxylases (*E. coli*, *H. influenzae*), reinforced below by direct sequence analysis.

---

## 3. Primary Function: The Reaction Catalyzed

Acetyl-CoA carboxylase in *P. putida*, as in other Gram-negative bacteria, is a **multi-component (dissociable) enzyme** built from four separate polypeptides: biotin carboxylase (AccC), biotin carboxyl carrier protein (BCCP/AccB), and the two carboxyltransferase subunits (AccA, AccD). Catalysis proceeds in two spatially separated half-reactions [PMID 16707089, 26020841]:

1. **BC half-reaction (this gene, AccC):** ATP-dependent carboxylation of the biotin covalently bound to BCCP, using bicarbonate as the CO₂ source.
2. **Carboxyltransferase half-reaction (AccA/AccD):** transfer of the carboxyl group from carboxybiotin-BCCP to acetyl-CoA, yielding **malonyl-CoA**.

The BC subunit "**catalyzes the ATP-dependent carboxylation of biotin using bicarbonate as the carboxylate source and has a distinct architecture that is characteristic of the ATP-grasp superfamily of enzymes**" [PMID 11346647]. Because ACC "**catalyzes the first committed and regulated step in fatty acid biosynthesis in bacteria**" [PMID 16707089] and is essential for membrane lipid production, it — and BC specifically — is a validated antibacterial drug target [PMID 16707089, 28469974].

**Substrate specificity.** BC is highly specific: it requires **MgATP** (not other NTPs efficiently), **bicarbonate** (the true substrate; free CO₂ is not used), and the **biotin** moiety (physiologically presented on BCCP; small free-biotin analogues such as biotin or N-1-methylbiotin are used in vitro). Steady-state kinetics of the *E. coli* enzyme show that "**MgATP and bicarbonate add to the enzyme randomly, followed by addition of biotin**," with both MgATP and bicarbonate binding in rapid equilibrium and a catalytic base of pK ≈ 6.6 in the active site [PMID 2971391].

---

## 4. Catalytic Mechanism (ATP-grasp fold, carboxyphosphate intermediate)

BC belongs to the **ATP-grasp superfamily** (which also includes D-Ala-D-Ala ligase, glutathione synthetase, carbamoyl-phosphate synthetase, and N⁵-CAIR synthetase) [PMID 11346647]. Its mechanism proceeds through an **unstable carboxyphosphate intermediate**:

1. **ATP activates bicarbonate.** The γ-phosphate of ATP is transferred to bicarbonate, forming **carboxyphosphate** + ADP. Isotope-tracer and positional-isotope-exchange experiments on the *E. coli* BC subunit showed that the bicarbonate-dependent, biotin-independent ATPase "**goes via carboxyphosphate**," with ¹⁸O transferred from bicarbonate into product Pi [PMID 2976600].
2. **Carboxyphosphate decomposes** to CO₂ + phosphate. The liberated phosphate acts as the general base that deprotonates the N1′ of biotin, and the resulting enolate/nucleophilic biotin attacks CO₂. High-resolution *Haemophilus influenzae* BC structures with substrate, intermediate-analogue, and product complexes support "**direct transfer of CO₂ from the carboxyphosphate intermediate to biotin**," with bicarbonate, phosphate, and the carboxyl group all occupying the same tetrahedral-stabilizing pocket [PMID 26020841].
3. Crystal structures of wild-type *E. coli* BC with biotin, bicarbonate and Mg-ADP indicate that **Glu296 is the general base that extracts the proton from bicarbonate** and **Arg338 stabilizes the enolate-biotin intermediate**; a mobile "B domain" closes over the active site to align the nucleotide for catalysis [PMID 19213731].

**Conserved catalytic architecture in *P. putida* (direct evidence from this analysis).** A global Needleman–Wunsch alignment of Q88QD6 (451 aa) against the biochemically characterized *E. coli* AccC (P24182, 449 aa) gives **70.5 % identity (316/448)**. Critically, **every experimentally validated catalytic and ATP-binding residue is strictly conserved**:

| Function | *E. coli* residue | *P. putida* (Q88QD6) residue | Status |
|---|---|---|---|
| ATP binding | Lys116 | Lys119 | conserved |
| ATP binding | Lys159 | Lys162 | conserved |
| ATP binding | His209 | His212 | conserved |
| ATP binding / catalysis | Glu276 | Glu279 | conserved |
| Active-site Arg | Arg292 | Arg295 | conserved |
| **General base (bicarbonate)** | **Glu296** | **Glu299** | conserved |
| **Enolate-biotin stabilization** | **Arg338** | **Arg341** | conserved |

The intact ATP-grasp fold (UniProt domain res. 123–320) plus this complete, unbroken catalytic constellation constitute strong structural/evolutionary evidence that Q88QD6 is a fully active biotin carboxylase operating by the canonical carboxyphosphate mechanism.

---

## 5. Subcellular Localization and Quaternary Structure

- **Localization:** BC is a **soluble cytoplasmic** protein. In Gram-negative bacteria the four ACC components are separate cytosolic polypeptides that assemble into a large but **labile, transient complex**; BC has no signal peptide or membrane anchor (consistent with the intracellular site of fatty-acid initiation). The malonyl-CoA produced is subsequently handed to the cytoplasmic type II fatty-acid synthase (FAS II) machinery.
- **Oligomeric state:** BC functions as a **homodimer**. UniProt annotates the assembled ACC as "**a heterohexamer of biotin carboxyl carrier protein, biotin carboxylase and the two subunits of carboxyl transferase in a 2:2 complex**." Isolation of the *E. coli* BC·BCCP subcomplex demonstrated that "**the complex consists of a dimer of BC plus four BCCP molecules**," with the N-terminal ~30 residues of BCCP mediating the BC interaction [PMID 12794081]. Thus BC carries out catalysis as a dimer, tightly coupled to the mobile biotinylated BCCP that ferries the carboxyl group to carboxyltransferase.

---

## 5b. Genomic Context in *P. putida* KT2440

In the KT2440 chromosome, *accC* (PP_0558) is **immediately adjacent to *accB* (PP_0559)**, which encodes the **biotin carboxyl carrier protein (BCCP, Q88QD5, 153 aa)** — the very substrate that BC carboxylates. This constitutes the canonical bacterial **accBC gene cluster**, physically coupling the carboxylase (AccC) to its carrier (AccB) (locus mapping from UniProt/KEGG; neighbors PP_0557 *acoR* and PP_0560 *aroQ1*). This genetic linkage mirrors the tight functional coupling of the two proteins and is a hallmark of the **multi-subunit (dissociable) class of ACC (MS-ACC)** used by bacteria and plant chloroplasts, as opposed to the single-chain eukaryotic ACC [PMID 12121720, 34132100].

The biotin prosthetic group that BC acts upon is not synthesized on AccB directly; it is **post-translationally attached to a single, highly conserved lysine of BCCP within an Ala/Val-Met-**Lys**-Met consensus** by **biotin protein ligase BirA** (EC 6.3.4.15) in an ATP-dependent two-step reaction (biotinyl-5′-AMP formation, then transfer) [PMID 20443544, 15033356]. Thus AccC's physiological substrate is *holo*-BCCP (biotinylated AccB).

## 6. Pathway Context and Biological Process

- **Pathway:** *De novo* **fatty acid biosynthesis** (type II FAS). BC/ACC produces **malonyl-CoA**, the universal two-carbon donor that is loaded onto acyl carrier protein (via FabD) and iteratively condensed (FabB/F, FabG, FabA/Z, FabI) to elongate acyl chains for **membrane phospholipids**. This is the **committed, rate-limiting entry step** of the pathway [PMID 16707089, 28469974].
- **Cofactor/prosthetic group dependency:** The reaction depends on the **biotin** prosthetic group carried by BCCP (attached by biotin protein ligase, BirA), and on **Mg²⁺** and **ATP**. BC itself does not carry biotin; it modifies the biotin on its partner subunit.
- **Physiological importance:** ACC activity governs the flux of acetyl-CoA into lipids; malonyl-CoA is essential and its synthesis is required for growth. In diverse bacteria ACC components are **essential genes**, making BC an antibacterial target [PMID 16707089, 28469974].
- **Regulatory note (post-translational):** In *E. coli*, BC (AccC) activity and folding can be modulated by the peptidyl-prolyl isomerase PpiB, which directly interacts with and increases AccC enzyme activity [PMID 27306110] — illustrating that BC function can be tuned at the protein level, though this is a peripheral observation rather than the core catalytic role.

---

## 6b. Pseudomonas-Specific Validation and Downstream Metabolic Fate

Beyond the strong cross-species inference from *E. coli*/*H. influenzae*, the AccC = biotin-carboxylase assignment is **experimentally supported within the *Pseudomonas* genus**. In a FAS II reporter screen in *P. aeruginosa*, genetic and biochemical follow-up of sulfonamidobenzamide inhibitors showed they "**target the enzyme (AccC) catalyzing the biotin carboxylase half-reaction of the acetyl coenzyme A (acetyl-CoA) carboxylase step in the initiation phase of FASII in E. coli and P. aeruginosa**" [PMID 26169404]. Given that *P. putida* AccC is 70.5 % identical to *E. coli* AccC with a fully conserved active site, this genus-level evidence applies directly to PP_0558.

**Downstream fate of the malonyl-CoA product.** The malonyl-CoA generated by ACC is the committed two-carbon donor for **type II fatty-acid synthesis (FAS II)**, producing the acyl chains of membrane phospholipids. In *P. putida* specifically, de novo FAS II output is additionally channeled by the transacylase **PhaG** ((R)-3-hydroxyacyl-ACP:CoA transacylase) into **medium-chain-length polyhydroxyalkanoate (mcl-PHA)** storage polymers — PhaG being "**the only metabolic link between fatty acid de novo biosynthesis and PHA biosynthesis in this bacterium**" [PMID 11425728; see also PMID 36763117] — and the related pathway supplies lipid moieties for **rhamnolipids**. Thus accC sits at the metabolic apex feeding membrane lipid, storage-polymer, and biosurfactant biosynthesis in *P. putida*. (These are downstream consequences; the precise role of AccC itself remains the BC half-reaction.)

**Drug-target relevance.** Because bacterial ACC/BC is essential and structurally divergent from the eukaryotic single-chain enzyme, it is a **validated, selectively druggable antibacterial target**; structural and inhibitor studies distinguish the BC and CT subsites and demonstrate phylum-selective inhibition [PMID 22183085, 22339356].

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1 — Q88QD6/accC is a biotin carboxylase catalyzing ATP-dependent carboxylation of biotin (EC 6.3.4.14). **Strongly supported** (UniProt EC/pathway annotation; ATP-grasp + biotin-carboxylation domains; 70.5 % identity to characterized *E. coli* BC; full catalytic-residue conservation).
- H2 — It performs the first half-reaction of ACC, committing acetyl-CoA to malonyl-CoA/fatty-acid synthesis. **Supported** (UniProt FUNCTION/PATHWAY; literature on ACC as first committed step).
- H3 — Mechanism proceeds via a carboxyphosphate intermediate with Glu296/Arg338-equivalent catalytic residues. **Supported** by conserved-residue mapping plus *E. coli*/*H. influenzae* mechanistic and structural studies.
- H4 — BC is a cytoplasmic homodimer within a labile multi-subunit ACC complex. **Supported** (UniProt subunit annotation; BC·BCCP stoichiometry study).

**Refuted / ruled out:**
- The gene symbol is **not** ambiguous; no alternative "accC" gene competes for this designation. Q88QD6 is **not** a eukaryotic-type single-chain ACC (in *P. putida* the components are separate polypeptides). BC does **not** itself carry biotin (that is BCCP/AccB).

---

## 8. Limitations and Future Directions

- **Direct experimental characterization of the *P. putida* KT2440 protein is lacking** (UniProt evidence level "Predicted"). All mechanistic and structural conclusions are inferred by orthology from *E. coli* and *H. influenzae* enzymes; the very high identity and complete active-site conservation make this inference robust, but species-specific kinetics (Km for ATP/bicarbonate/biotin, kcat) have not been measured.
- No experimental *P. putida* BC structure exists; residue numbering was mapped by pairwise alignment rather than superposition. An AlphaFold model + structural superposition would further confirm the ATP-grasp geometry.
- **Future work:** heterologous expression and steady-state kinetics of PP_0558; confirmation of essentiality by conditional knockout in KT2440; complex-assembly/stoichiometry assays with the cognate AccB/AccA/AccD; and evaluation as an antibacterial target given ACC's validated druggability.

---

## References (PMIDs)
- **26169404** — Wallace et al. (2015) FAS II reporter screen; genetic/biochemical proof that **AccC** is the BC-half-reaction target in *E. coli* and *P. aeruginosa*.
- **11425728** — Rehm, Mitsky & Steinbüchel (2001) PhaG links de novo FAS to mcl-PHA/rhamnolipid synthesis in pseudomonads.
- **36763117** — Liu et al. (2023) β-oxidation–PHA relationship in *P. putida* KT2440 (PhaG/PhaJ routes).
- **22183085** — Polyak et al. (2012) Structure, function and selective inhibition of bacterial ACC (BC vs CT subsites).
- **22339356** — Luo et al. (2012) ACC inhibitors and therapeutic potential (BC/CT targeting).
- **34132100** — Cronan (2021) *E. coli* acetyl-CoA carboxylase: authoritative modern review of subunit structure, stoichiometry, and regulation.
- **12121720** — Cronan & Waldrop (2002) Multi-subunit acetyl-CoA carboxylases; MS-ACC vs single-chain ACC; mechanism/regulation review.
- **20443544** — Healy et al. (2010) BCCP biotinylation; conserved Ala/Val-Met-Lys-Met attachment motif.
- **15033356** — Brown, Cronan et al. (2004) Biotin repressor / two-step BirA biotinylation of BCCP.
- **20158506** — Molina-Henares et al. (2010) Genome-wide conditionally essential genes in *P. putida* KT2440 (metabolic context).
- **11346647** — Sloane et al. (2001) Site-directed mutagenesis of ATP-binding residues of biotin carboxylase; ATP-grasp fold; Lys116/Lys159/His209/Glu276.
- **19213731** — Chou, Yu & Tong (2009) Crystal structure of *E. coli* BC with substrates; Glu296 general base, Arg338 stabilizes enolate biotin.
- **26020841** — Broussard et al. (2015) Structural analysis of substrate/intermediate/product binding in *H. influenzae* BC; carboxyphosphate → CO₂ transfer.
- **2976600** — Ogita & Knowles (1988) Carboxyphosphate intermediacy in biotin-dependent carboxylation (¹⁸O tracer).
- **2971391** — Tipton & Cleland (1988) Steady-state kinetics of BC; random substrate addition; catalytic base pK 6.6.
- **12794081** — Choi-Rhee & Cronan (2003) The BC·BCCP complex of *E. coli* ACC; BC dimer + 4 BCCP.
- **16707089** — Santoro et al. (2006) ACC as the first committed step and antibacterial target; component overview.
- **28469974** — Bennett & Högbom (2017) Structure of essential biotin-dependent carboxylase AccA3; ACC = committed step of type II FAS.
- **27306110** — Skagia et al. (2016) PpiB modulates AccC activity/folding (post-translational regulation).

*Analysis performed in Iteration 1: UniProt/KEGG annotation retrieval for Q88QD6, literature synthesis, and a Needleman–Wunsch alignment to E. coli AccC (P24182) confirming 70.5 % identity and strict conservation of all catalytic residues.*


## Artifacts

- [OpenScientist final report](accC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](accC-deep-research-openscientist_artifacts/final_report.pdf)