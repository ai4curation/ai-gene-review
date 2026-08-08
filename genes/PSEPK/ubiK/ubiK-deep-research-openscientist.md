---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T18:07:26.343094'
end_time: '2026-07-18T18:26:10.692939'
duration_seconds: 1124.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiK
  gene_symbol: ubiK
  uniprot_accession: Q88CE6
  protein_description: 'RecName: Full=Ubiquinone biosynthesis accessory factor UbiK
    {ECO:0000256|HAMAP-Rule:MF_02216};'
  gene_info: Name=ubiK {ECO:0000256|HAMAP-Rule:MF_02216}; OrderedLocusNames=PP_5235
    {ECO:0000313|EMBL:AAN70800.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiK family. {ECO:0000256|HAMAP-
  protein_domains: UbiK. (IPR007475); BMFP (PF04380)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CE6
- **Protein Description:** RecName: Full=Ubiquinone biosynthesis accessory factor UbiK {ECO:0000256|HAMAP-Rule:MF_02216};
- **Gene Information:** Name=ubiK {ECO:0000256|HAMAP-Rule:MF_02216}; OrderedLocusNames=PP_5235 {ECO:0000313|EMBL:AAN70800.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiK family. {ECO:0000256|HAMAP-
- **Key Domains:** UbiK. (IPR007475); BMFP (PF04380)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiK** (gene ID: ubiK, UniProt: Q88CE6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: UbiK (Q88CE6, PP_5235) in *Pseudomonas putida* KT2440

## Summary

**UbiK (UniProt Q88CE6; ordered locus PP_5235) is a small, ~88-residue cytoplasmic, non-enzymatic accessory factor that is required for the efficient biosynthesis of ubiquinone (coenzyme Q, UQ), the lipophilic electron carrier of the proteobacterial aerobic respiratory chain.** It does not catalyze any step of the pathway itself. Instead, it functions as a structural/organizational protein: through its conserved C-terminal coiled coil it forms a heterotrimeric UbiJ–UbiK₂ subcomplex that nucleates and organizes a large (~1-MDa) soluble multi-enzyme assembly — the "Ubi metabolon" — that carries out the terminal, oxygen-dependent reactions of UQ biosynthesis in the cytoplasm, and that couples this metabolon to the cytoplasmic face of the inner membrane so that finished UQ can be released into the lipid bilayer.

The functional model for UbiK derives from detailed experimental work on its ortholog in *Escherichia coli* (originally annotated as *yqiC*, renamed *ubiK*). In *E. coli*, loss of UbiK (or its partner UbiJ) does not block a single defined enzymatic step but instead stalls the pathway globally: cells accumulate octaprenylphenol, an early UQ biosynthetic intermediate, and lose efficient UQ production. UbiK physically binds the C-terminal region of UbiJ, and the UbiK–UbiJ complex binds fatty acids (palmitoleic acid), consistent with a lipid/membrane-interfacing role. The requirement for UbiK is specific to the aerobic (O₂-dependent) UQ pathway — both UbiK and UbiJ are dispensable for UQ production under anaerobiosis even though they remain expressed.

For the *P. putida* protein specifically, the annotation is inferred by homology (UniProt evidence level PE=3; HAMAP-Rule MF_02216) rather than from a direct experimental study of PP_5235. However, the inference is well-supported: *P. putida* KT2440 is an obligate aerobe that depends on UQ for respiration, it encodes the complete aerobic Ubi enzyme complement **and both accessory factors** (UbiJ = PP_5012 and UbiK = PP_5235), and the *P. putida* UbiK protein is a genuine ortholog of the experimentally characterized *E. coli* UbiK (32% global identity, with conservation focused precisely on the functional C-terminal coiled coil). An AlphaFold model of Q88CE6 confirms the predicted C-terminal coiled coil at high confidence. Taken together, the evidence places *P. putida* UbiK firmly within the proteobacterial aerobic UQ-synthesizing metabolon as the cytoplasmic, UbiJ-partnered assembly/membrane-targeting factor.

---

## Gene/Protein Identity Verification

| Attribute | Value |
|-----------|-------|
| UniProt accession | Q88CE6 |
| Protein name | Ubiquinone biosynthesis accessory factor UbiK |
| Gene name | *ubiK* |
| Ordered locus | PP_5235 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950) |
| Length | 88 aa |
| Family / domains | UbiK family; Pfam PF04380 (BMFP); InterPro IPR007475 |
| Evidence level | PE=3 (inferred from homology); HAMAP-Rule MF_02216 |

**Verification outcome:** The gene symbol *ubiK*, the protein description ("Ubiquinone biosynthesis accessory factor"), the organism (*P. putida* KT2440), and the domain/family assignment (UbiK / PF04380 / IPR007475) are all mutually consistent, and they align with the published literature on the UbiK family. No conflicting gene-symbol ambiguity was encountered. Research proceeded on the correct target.

---

## Key Findings

### F001 — UbiK is an accessory factor required for efficient ubiquinone (coenzyme Q) biosynthesis

UniProt Q88CE6, governed by HAMAP-Rule MF_02216, describes UbiK as an 88-amino-acid cytoplasmic protein that is "Required for efficient ubiquinone (coenzyme Q) biosynthesis" and is an "accessory factor of Ubi enzymes... an assembly factor, a targeting factor, or both." It is assigned to the ubiquinone biosynthesis pathway, to the UbiK protein family, and carries Pfam domain PF04380 (BMFP) / InterPro IPR007475. Critically, UbiK carries **no catalytic annotation** — it is not an enzyme and does not perform a chemical transformation on the UQ biosynthetic intermediates.

The experimental basis for this annotation lies in the *E. coli* ortholog. Loiseau et al. (2017, *J. Biol. Chem.*) showed that the gene *yqiC*, which they renamed *ubiK*, is required for efficient UQ biosynthesis. Importantly, both *ubiK* and *ubiJ* mutants accumulate **octaprenylphenol**, an early UQ biosynthetic intermediate. The accumulation of an early intermediate — rather than the specific intermediate that would flank a single missing enzymatic step — indicates that UbiK has a **global** role in the pathway, consistent with an organizational/assembly function rather than a single catalytic one.

This finding is anchored by the paper that identified and named *ubiK*, which establishes the identity and role of the pathway's end-product:

> "Ubiquinone (UQ), also referred to as coenzyme Q, is a widespread lipophilic molecule in both prokaryotes and eukaryotes in which it primarily acts as an electron carrier" — [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)

### F002 — UbiK acts within a soluble cytoplasmic Ubi metabolon, forming a UbiJ–UbiK₂ subcomplex that organizes and membrane-couples UQ biosynthesis

The mechanistic role of UbiK is to help assemble and target a large, soluble multi-enzyme complex. Hajj Chehade et al. (2019, *Cell Chem. Biol.*) demonstrated that seven Ubi proteins (UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK) form a stable **~1-MDa soluble metabolon** that catalyzes the last six reactions of UQ biosynthesis in the cytoplasm of *E. coli*. Within this assembly, the SCP2 domain of UbiJ forms an extended hydrophobic cavity that binds the highly hydrophobic UQ intermediates, effectively sequestering these lipophilic molecules away from the aqueous cytoplasm while they are being processed.

UbiK's specific place in this architecture is defined by two features. First, Loiseau et al. (2017) showed that UbiK **physically forms a complex with the C-terminal part of UbiJ**, and that the UbiK–UbiJ complex binds palmitoleic acid — a fatty acid ligand consistent with an interface to the lipid membrane. Second, Launay et al. (2022) provided a molecular model in which a **UbiJ–UbiK₂ heterotrimer is the interface between the membrane and the Ubi metabolon**, mediating the release of newly synthesized UQ into the membrane. UbiK therefore functions as the connective, membrane-coupling element of the metabolon.

Structurally, this is enabled by UbiK's C-terminal coiled coil. UniProt localizes UbiK to the cytoplasm/cytosol (GO:0005829) and annotates a C-terminal coiled coil (residues 60–87) consistent with oligomerization; the *P. putida* sequence shows the expected heptad-repeat Leu/Ala character in this region.

Supporting quotations:

> "seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in Escherichia coli" — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)

> "The SCP2 domain of UbiJ forms an extended hydrophobic cavity that binds UQ intermediates inside the 1-MDa Ubi complex" — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/)

> "UQ has important roles, notably in respiratory metabolisms which sustain cellular bioenergetics" — [PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)

### F003 — UbiK's function is specific to the O₂-dependent (aerobic) UQ pathway; the *P. putida* annotation is inferred by homology

Loiseau et al. (2017) demonstrated that UbiK and UbiJ are **dispensable for UQ biosynthesis under anaerobiosis**, even though both proteins continue to be expressed in the absence of oxygen. This establishes that the UbiK/UbiJ role is restricted to the **aerobic** UQ pathway. The physiological importance of this pathway is underscored by observations in *Salmonella enterica*, where *ubiK* is required for proliferation in macrophages and for virulence in mice.

For the *P. putida* protein Q88CE6/PP_5235 there is **no direct experimental study**: its evidence level is PE=3 (inferred from homology), with the functional annotation propagated by HAMAP-Rule MF_02216. This homology inference is biologically reasonable because *P. putida* is an obligate aerobe that relies on UQ for respiration — precisely the condition under which the UbiJ/UbiK metabolon operates. Genomic-context analysis (STRING, taxid 160488) shows that PP_5235 is **not** encoded in an operon with the *ubi* enzyme genes; its top genomic neighbors are cell-division and outer-membrane genes. This mirrors *E. coli*, where *ubiK/yqiC* is a standalone gene whose partnership with UbiJ is **physical (protein–protein), not genomic (operonic)**.

Supporting quotation (source paper whose experimental conclusions are propagated by homology):

> "Ubiquinone (UQ), also referred to as coenzyme Q, is a widespread lipophilic molecule in both prokaryotes and eukaryotes in which it primarily acts as an electron carrier" — [PMID: 28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/)

### F004 — *P. putida* KT2440 encodes the complete Ubi pathway including the UbiJ partner (PP_5012), and UbiK has a high-confidence AlphaFold coiled coil

A UniProt survey of *P. putida* KT2440 (taxid 160488) confirms that the organism possesses the **full aerobic UQ biosynthetic complement**, meaning the metabolon UbiK organizes can actually be built. The genes present include:

| Gene | Locus tag | Role |
|------|-----------|------|
| *ubiA* | PP_5318 | 4-hydroxybenzoate polyprenyltransferase |
| *ubiB* | PP_5013 | UQ biosynthesis regulatory kinase / hydroxylase-associated |
| *ubiD* | PP_5213 | 3-octaprenyl-4-hydroxybenzoate decarboxylase |
| *ubiE* | PP_5011 | C-methyltransferase |
| *ubiG* | PP_1765 | O-methyltransferase |
| *ubiH* | PP_5199 | 2-octaprenyl-6-methoxyphenol hydroxylase |
| *ubiX* | PP_0548 | flavin prenyltransferase |
| ***ubiJ*** | **PP_5012** (207 aa, cytoplasm, HAMAP MF_02215) | SCP2 accessory / intermediate-binding factor |
| ***ubiK*** | **PP_5235** (88 aa, cytoplasm, HAMAP MF_02216) | assembly/targeting accessory factor (this report) |

Crucially, the physical partner **UbiJ (PP_5012) is present**, so the UbiJ–UbiK₂ metabolon model can operate in *P. putida*. Genomic-locus inspection shows *ubiK* (PP_5235) is standalone, separate from the *ubi* cluster near PP_5011–5013 (which contains *ubiE–ubiJ–ubiB*) and from PP_5199–5213 — matching the *E. coli* arrangement.

An AlphaFold model of Q88CE6 supports the structural prediction: the overall model has a mean pLDDT of **83.9** (high confidence), with 75 of 88 residues at pLDDT > 70. The **C-terminal coiled-coil region (residues 60–87) is modeled at even higher confidence (mean pLDDT = 86.6)**, corroborating the predicted oligomerization/UbiJ-binding coiled coil that is central to UbiK's function.

### F005 — *P. putida* and *E. coli* UbiK are orthologs (32% identity) with conservation concentrated in the functional C-terminal coiled coil

A global Needleman–Wunsch alignment (BLOSUM62) of *P. putida* UbiK (Q88CE6, 88 aa) against the experimentally characterized *E. coli* UbiK (Q46868 / UBIK_ECOLI, 96 aa) yields **32.2% identity** (28/87 aligned columns) and **54.0% similarity** (47/87 positive-scoring positions). Critically, the conservation is **not uniform** — it is concentrated in the C-terminal half corresponding to the coiled coil (residues ~44–83), including a near-invariant central motif:

| Region | *P. putida* (Q88CE6) | *E. coli* (Q46868) |
|--------|----------------------|--------------------|
| Central coiled-coil motif | `KLDLVSRDEFDSQMV` | `TRLDLVSREEFDVQT` |

This conserved block is precisely the region that UniProt annotates as the coiled coil (60–87), that mediates UbiJ binding and UbiK oligomerization, and that AlphaFold models at highest confidence (pLDDT 86.6). The convergence of evolutionary conservation, functional annotation, and structural confidence on the same segment provides strong triangulated evidence that the *P. putida* protein retains the UbiJ-binding/oligomerization function of the experimentally studied ortholog.

### F006 — Review-level context: UQ is the proteobacterial respiratory electron carrier, and Ubi proteins are supramolecularly organized

The authoritative review by Abby, Kazemzadeh, Vragniau, Pelosi, and Pierrel (2020, *"Advances in bacterial pathways for the biosynthesis of ubiquinone"*) situates UbiK within the broader biology of UQ metabolism. The review states that "Ubiquinone is an important component of the electron transfer chains in proteobacteria and eukaryotes," and it explicitly discusses "the supramolecular organization of ubiquinone biosynthesis proteins" — i.e., the Ubi metabolon that contains UbiJ and UbiK. The review also notes the discovery of a newly described O₂-independent UQ pathway, which is consistent with the observation that UbiK/UbiJ are dispensable under anaerobiosis. As a Gammaproteobacterium that uses UQ for aerobic respiration, *P. putida* falls squarely within this framework.

Supporting quotations:

> "Ubiquinone is an important component of the electron transfer chains in proteobacteria and eukaryotes" — [PMID: 32663475](https://pubmed.ncbi.nlm.nih.gov/32663475/)

> "We also discuss the supramolecular organization of ubiquinone biosynthesis proteins" — [PMID: 32663475](https://pubmed.ncbi.nlm.nih.gov/32663475/)

---

## Mechanistic Model / Interpretation

The picture that emerges is coherent and internally consistent across biochemistry, structure, evolution, and genomics. UbiK is best understood as a **molecular organizer and membrane-coupling adapter**, not an enzyme.

### The pathway and where UbiK fits

Ubiquinone biosynthesis in proteobacteria proceeds through a series of modifications to a polyprenylated aromatic ring. The terminal, O₂-dependent reactions (hydroxylations and methylations) are carried out by the Ubi enzymes (UbiE, UbiF, UbiG, UbiH, UbiI). These enzymes and their hydrophobic substrates do not float freely in the cytoplasm; instead they are gathered into a soluble ~1-MDa **metabolon** whose non-catalytic scaffolding is provided by the accessory factors UbiJ and UbiK.

```
                         CYTOPLASM
   ┌─────────────────────────────────────────────────────┐
   │   ~1-MDa soluble Ubi metabolon                       │
   │                                                      │
   │    UbiE  UbiF  UbiG  UbiH  UbiI   (catalytic enzymes)│
   │        \    |    |    |    /                         │
   │         \   |    |    |   /                          │
   │        ┌──────────────────┐                          │
   │        │   UbiJ (SCP2)    │  ← hydrophobic cavity    │
   │        │  binds UQ inter- │    sequesters lipophilic │
   │        │  mediates        │    intermediates         │
   │        └────────┬─────────┘                          │
   │           C-terminus of UbiJ                         │
   │                 │  (physical interaction)            │
   │        ┌────────┴─────────┐                          │
   │        │   UbiK₂ (coiled  │  ← this protein          │
   │        │   coil dimer)    │    binds fatty acid      │
   │        └────────┬─────────┘    (palmitoleic acid)    │
   └─────────────────┼───────────────────────────────────┘
                     │  UbiJ–UbiK₂ = membrane interface
   ══════════════════▼═══════════════════════════  INNER MEMBRANE
        finished UQ released into the lipid bilayer
                     │
                     ▼
        Aerobic respiratory electron transport chain
```

### UbiK's three interlocking roles

1. **Oligomerization.** UbiK forms a homodimer (UbiK₂) via its C-terminal coiled coil. This coiled coil is the most conserved and highest-confidence-modeled part of the protein.

2. **Partnering with UbiJ.** The UbiK₂ dimer binds the C-terminal region of UbiJ, forming a UbiJ–UbiK₂ heterotrimer. UbiJ in turn brings its SCP2 hydrophobic cavity — which holds the lipophilic UQ intermediates — into the assembly. UbiK therefore anchors the intermediate-carrying subunit into the larger metabolon.

3. **Membrane coupling / product release.** The UbiJ–UbiK₂ subcomplex (with UbiK's fatty-acid-binding activity) forms the physical interface between the soluble metabolon and the inner membrane, enabling newly synthesized UQ to be released into the lipid bilayer where it functions as a respiratory electron carrier.

The **global** phenotype of *ubiK* loss (accumulation of the early intermediate octaprenylphenol, rather than a single defined intermediate) is exactly what this model predicts: removing the organizer collapses the metabolon and stalls flux through the whole downstream pathway, not one step. The **aerobic specificity** of UbiK likewise fits: the O₂-dependent enzymatic steps are those organized by the metabolon, so under anaerobiosis (where an alternative O₂-independent route operates) UbiK/UbiJ are not needed.

### Confidence in the *P. putida* assignment

For PP_5235 specifically, all evidence is inferential (homology) rather than direct, but it is triangulated:

| Line of evidence | Result | What it supports |
|------------------|--------|------------------|
| Orthology to *E. coli* UbiK | 32% identity, 54% similarity | Same protein family/function |
| Location of conservation | Concentrated in C-terminal coiled coil (residues ~44–83) | Retained UbiJ-binding/oligomerization function |
| AlphaFold structure | Mean pLDDT 83.9; coiled coil 86.6 | Predicted coiled coil is real |
| Partner present | UbiJ = PP_5012 encoded in genome | Metabolon can assemble |
| Full pathway present | All Ubi enzymes encoded | UQ made aerobically |
| Physiology | Obligate aerobe, UQ-respiring | Aerobic metabolon relevant |
| Genomic context | *ubiK* standalone, not in *ubi* operon | Matches *E. coli* (physical not genomic partnership) |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [28559279](https://pubmed.ncbi.nlm.nih.gov/28559279/) | *The UbiK protein is an accessory factor necessary for bacterial ubiquinone (UQ) biosynthesis and forms a complex with the UQ biogenesis factor UbiJ* (Loiseau et al. 2017) | **Primary experimental source.** Identified/renamed *ubiK* (*yqiC*); showed *ubiK*/*ubiJ* mutants accumulate octaprenylphenol (global role); UbiK binds C-terminal UbiJ; UbiK–UbiJ complex binds palmitoleic acid; aerobic specificity; role in *Salmonella* virulence. |
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | *A Soluble Metabolon Synthesizes the Isoprenoid Lipid Ubiquinone* (Hajj Chehade et al. 2019) | Defined the ~1-MDa soluble Ubi metabolon of seven Ubi proteins (including UbiK); showed UbiJ's SCP2 cavity binds UQ intermediates. Establishes the structural context of UbiK's function. |
| [36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/) | *Towards Molecular Understanding of the Functional Role of UbiJ-UbiK₂* (Launay et al. 2022) | Modeled the UbiJ–UbiK₂ heterotrimer as the membrane–metabolon interface mediating UQ release into the membrane. Provides the membrane-coupling mechanism. |
| [32663475](https://pubmed.ncbi.nlm.nih.gov/32663475/) | *Advances in bacterial pathways for the biosynthesis of ubiquinone* (Abby et al. 2020) | Authoritative review: UQ as the proteobacterial respiratory electron carrier; supramolecular organization of Ubi proteins; O₂-independent UQ pathway. Frames UbiK in the broader field. |
| [38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/) | *Structural Reconstruction of [the Ubi metabolon]* | Further structural characterization of the UQ-synthesizing complex, reinforcing the metabolon model. |

**How the evidence converges:** No single paper studies *P. putida* PP_5235 directly. The functional model rests on *E. coli* biochemistry (Loiseau 2017), metabolon structural biology (Hajj Chehade 2019; Launay 2022; PMID 38710096), and field-level synthesis (Abby 2020), transferred to *P. putida* through orthology, structural prediction, and genomic completeness. This is a well-justified homology-based annotation, not a direct measurement.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data for PP_5235.** All functional claims for the *P. putida* protein are inferred (UniProt PE=3). No *P. putida ubiK* knockout, UQ-quantification, or protein-interaction study has been reported here. The phenotypes (octaprenylphenol accumulation, aerobic specificity) are from *E. coli* / *Salmonella*.

2. **Moderate sequence identity.** At 32% global identity, orthology is confident but not trivial. While conservation is reassuringly concentrated in the functional coiled coil, divergence in the N-terminal region could in principle modulate species-specific interactions or regulation.

3. **Structural model, not experimental structure.** The coiled coil and UbiK₂ dimer are supported by AlphaFold (high pLDDT) and by the *E. coli* model of Launay et al. (2022), but no experimental structure of *P. putida* UbiK or its UbiJ complex exists.

4. **Membrane-coupling mechanism partly modeled.** The UbiJ–UbiK₂ membrane interface and UQ-release step are based on molecular modeling; the precise stoichiometry and dynamics in *P. putida* are unverified.

5. **Regulation unknown.** How *ubiK* (PP_5235) expression is controlled in *P. putida*, and whether UbiK abundance limits UQ flux under specific growth or stress conditions, is not addressed.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted deletion of PP_5235 in *P. putida* KT2440.** Construct a clean *ΔubiK* mutant and quantify UQ (UQ-9/UQ-8) and biosynthetic intermediates (especially octaprenylphenol) by LC-MS under aerobic vs. anaerobic/microaerophilic growth. This directly tests whether the *E. coli* phenotype transfers.

2. **Growth/respiration phenotyping.** Assess aerobic growth rate, respiratory capacity (oxygen consumption), and sensitivity to respiratory stress in *ΔubiK*, with complementation by plasmid-borne *ubiK* and by *E. coli ubiK* (cross-species complementation to confirm functional orthology).

3. **Protein–protein interaction validation.** Use co-purification / bacterial two-hybrid / crosslinking to confirm that *P. putida* UbiK (PP_5235) binds UbiJ (PP_5012) and co-assembles with the Ubi enzymes into a high-molecular-weight metabolon.

4. **Biophysical/structural characterization.** Recombinantly express UbiK; verify coiled-coil-mediated dimerization (SEC-MALS, circular dichroism); attempt to solve the UbiJ–UbiK₂ structure (cryo-EM or X-ray) to confirm the modeled membrane interface.

5. **Fatty-acid / lipid binding assay.** Test whether the *P. putida* UbiK–UbiJ complex binds palmitoleic acid or other fatty acids, mirroring the *E. coli* observation and probing the membrane-targeting mechanism.

6. **Localization.** Fluorescent-fusion or fractionation studies to confirm cytoplasmic localization with membrane association, consistent with the metabolon-at-membrane model.

---

## Conclusion

UbiK (Q88CE6, PP_5235) in *Pseudomonas putida* KT2440 is a small cytoplasmic, non-catalytic accessory factor for aerobic ubiquinone (coenzyme Q) biosynthesis. It uses a conserved C-terminal coiled coil to dimerize and to bind the accessory factor UbiJ, forming a UbiJ–UbiK₂ subcomplex that assembles and organizes the soluble ~1-MDa Ubi metabolon (which performs the terminal O₂-dependent UQ reactions) and couples it to the inner membrane for release of finished UQ. Loss of the protein stalls the pathway globally and is dispensable anaerobically. For *P. putida* this is a strong homology-based inference (32% identity to experimentally characterized *E. coli* UbiK, conservation focused on the functional coiled coil, partner UbiJ and full Ubi enzyme set present, high-confidence AlphaFold coiled coil), pending direct experimental confirmation.


## Artifacts

- [OpenScientist final report](ubiK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiK-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28559279
2. PMID:30686758
3. PMID:36142227
4. PMID:32663475