---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T12:41:57.167293'
end_time: '2026-07-20T12:56:43.664893'
duration_seconds: 886.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pqqB
  gene_symbol: pqqB
  uniprot_accession: Q88QV5
  protein_description: 'RecName: Full=Coenzyme PQQ synthesis protein B {ECO:0000255|HAMAP-Rule:MF_00653};
    AltName: Full=Pyrroloquinoline quinone biosynthesis protein B {ECO:0000255|HAMAP-Rule:MF_00653};'
  gene_info: Name=pqqB {ECO:0000255|HAMAP-Rule:MF_00653}; OrderedLocusNames=PP_0379;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PqqB family. {ECO:0000255|HAMAP-
  protein_domains: Metallo-B-lactamas. (IPR001279); PQQ_synth_PqqB. (IPR011842); RibonucZ/Hydroxyglut_hydro.
    (IPR036866); Lactamase_B_2 (PF12706)
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pqqB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pqqB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QV5
- **Protein Description:** RecName: Full=Coenzyme PQQ synthesis protein B {ECO:0000255|HAMAP-Rule:MF_00653}; AltName: Full=Pyrroloquinoline quinone biosynthesis protein B {ECO:0000255|HAMAP-Rule:MF_00653};
- **Gene Information:** Name=pqqB {ECO:0000255|HAMAP-Rule:MF_00653}; OrderedLocusNames=PP_0379;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PqqB family. {ECO:0000255|HAMAP-
- **Key Domains:** Metallo-B-lactamas. (IPR001279); PQQ_synth_PqqB. (IPR011842); RibonucZ/Hydroxyglut_hydro. (IPR036866); Lactamase_B_2 (PF12706)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pqqB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pqqB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pqqB** (gene ID: pqqB, UniProt: Q88QV5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PqqB (Q88QV5, PP_0379) — Functional Annotation Report

**Gene:** *pqqB* | **Ordered locus:** PP_0379 | **UniProt:** Q88QV5
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK
**Protein family:** PqqB family (HAMAP MF_00653); metallo-β-lactamase (MBL) superfamily
**Domains:** Metallo-B-lactamase (IPR001279); PQQ_synth_PqqB (IPR011842); RibonucZ/Hydroxyglut_hydro (IPR036866); Lactamase_B_2 (PF12706)

---

## Summary

PqqB is a biosynthetic enzyme of the **pyrroloquinoline quinone (PQQ)** pathway, the small operon-encoded machinery (*pqqFABCDEG* in *P. putida* KT2440) that converts the ribosomally synthesized peptide **PqqA** into the diffusible redox cofactor PQQ. Gene identity is unambiguous and fully consistent with the UniProt annotation: *pqqB* / PP_0379, PqqB family (HAMAP MF_00653), with an MBL-superfamily fold matching the InterPro/Pfam domain calls. The literature retrieved is specific to PqqB in PQQ biosynthesis — there is no symbol collision with an unrelated gene — so the annotation can be made with confidence.

The **primary function** of PqqB is that of a **mononuclear non-heme iron-dependent hydroxylase** that performs the "middle" tailoring steps of PQQ maturation. It catalyzes the O₂-dependent, stepwise insertion of **two oxygen atoms into the tyrosine-derived ring** of a cross-linked glutamate–tyrosine (Glu–Tyr) diamino-acid intermediate, thereby generating the **quinone moiety** of the cofactor. The immediate product is **AHQQ** [3a-(2-amino-2-carboxy-ethyl)-4,5-dioxo-…-quinoline-7,9-dicarboxylic acid], which the downstream enzyme **PqqC** then oxidatively cyclizes into mature PQQ. In the ordered pathway, PqqB acts **after** the radical-SAM cross-linking enzyme PqqE (assisted by the peptide chaperone PqqD) and the PqqF/G protease, and **before** PqqC. This hydroxylase activity is unprecedented within the metallo-β-lactamase family and expands the known catalytic repertoire of non-heme iron hydroxylases.

**Localization:** PqqB acts in the **cytoplasm**, where the entire PQQ biosynthetic route operates on soluble intermediates; it is a soluble homodimeric protein with no signal peptide or membrane-spanning region and was crystallized as a recombinant soluble protein. The **finished cofactor is exported to the periplasm**, where PQQ-dependent glucose dehydrogenase (GDH) uses it to oxidize glucose to gluconic acid — the biochemical basis of *P. putida*'s mineral-phosphate-solubilizing phenotype. Genetic loss-of-function studies in related *Pseudomonas* and *Rahnella* strains confirm that *pqqB* is required in vivo for functional PQQ and PQQ-dependent quinoprotein activity, although early biochemical work showed that PqqB is **rate-enhancing but partially bypassable** (its loss reduces, rather than fully abolishes, PQQ in some systems). A minority, purely computational hypothesis that PqqB instead acts as a PQQ transporter is not supported by the direct experimental demonstration of its hydroxylase activity.

---

## Key Findings

### F001 — PqqB is an enzyme of the PQQ biosynthetic pathway

PqqB is one of **four conserved biosynthetic proteins (PqqB–E)** that together convert the ribosomally synthesized, post-translationally modified peptide **PqqA** into the redox cofactor PQQ. Martins et al. (2019) describe PQQ as being "produced from a ribosomally synthesized and post-translationally modified peptide PqqA via a pathway comprising four conserved proteins PqqB-E" ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)). In the target organism, *pqqB* is embedded in the *pqq* operon — An & Moe (2016) confirm the "PQQ biosynthesis genes (pqq operon)" in *P. putida* KT2440 ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). Gene identity is fully corroborated: gene *pqqB*, OrderedLocusName PP_0379, PqqB family (HAMAP MF_00653). This anchors the functional annotation in the correct gene and organism.

### F002 — PqqB is an iron-dependent hydroxylase catalyzing quinone-forming oxygen insertion

The defining catalytic activity of PqqB was established by Koehn et al. (2019), who demonstrated that "the remaining essential biosynthetic enzyme PqqB is an iron-dependent hydroxylase catalyzing oxygen-insertion reactions that are proposed to produce the quinone moiety of the mature PQQ cofactor" ([PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)). This activity is mechanistically striking because "the demonstrated reactions of PqqB are unprecedented within the metallo β-lactamase protein family and expand the catalytic repertoire of nonheme iron hydroxylases." An independent review characterized PqqB as "a dual hydroxylase" ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)), consistent with the insertion of two oxygen atoms. This is the single most important functional finding: **PqqB builds the quinone chemistry of PQQ.**

### F003 — PqqB adopts a metallo-β-lactamase fold with a plastic, degenerate metal site

Tu et al. (2017) solved crystal structures of *P. putida* PqqB and confirmed it "is an enzyme involved in the biosynthesis of pyrroloquinoline quinone and a distal member of the metallo-β-lactamase (MBL) superfamily" ([PMID: 28825148](https://pubmed.ncbi.nlm.nih.gov/28825148/)). Crucially, "PqqB lacks two residues in the conserved signature motif HxHxDH that makes up the key metal-chelating elements," explaining why its active site accommodates metals with unusual plasticity rather than performing canonical β-lactam hydrolysis. This structural work directly supports the InterPro/Pfam domain annotations (IPR001279, IPR011842, PF12706) and rationalizes the non-canonical hydroxylase chemistry uncovered biochemically.

### F004 — *pqqB* expression modulates cellular PQQ levels and phosphate solubilization

An & Moe (2016) mapped the *P. putida* KT2440 *pqq* operon (*pqqFABCDEG*) as at least two independent transcripts and showed a quantitative link between expression and cofactor output: "the levels of expression of the pqqF and pqqB genes mirror the levels of PQQ synthesized, suggesting that one or both of these genes may serve to modulate PQQ levels" ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). They further defined the operon architecture — "The pqq gene cluster (pqqFABCDEG) encodes at least two independent transcripts" — and observed that PQQ, GDH activity, and downstream phosphate solubilization peaked under glucose as sole carbon source with low soluble phosphate. This positions *pqqB* not merely as a structural pathway member but as an expression node that can tune PQQ availability.

### F005 — PqqB is stimulatory but partially bypassable; PQQ synthesis requires O₂

Velterop et al. (1995), studying the *Klebsiella pneumoniae pqqABCDEF* operon expressed in *E. coli*, found that "mutants lacking the PqqB or PqqF protein synthesized small amounts of PQQ, however" — in contrast to loss of most other Pqq proteins, which abolished PQQ entirely ([PMID: 7665488](https://pubmed.ncbi.nlm.nih.gov/7665488/)). Cell-free experiments reinforced a rate-enhancing role: "extracts lacking PqqB synthesized PQQ slowly." Importantly, the same study established the pathway's oxygen dependence — "synthesis of PQQ most likely requires molecular oxygen, since PQQ was not synthesized under anaero[bic conditions]" — which is fully consistent with PqqB's later-demonstrated O₂-dependent hydroxylase mechanism. The partial bypass suggests either residual non-enzymatic oxidation of the intermediate or functional redundancy under some conditions.

### F006 — PqqB acts mid-pathway, between PqqE cross-linking and PqqC final oxidation

The ordering of the pathway is well established. Barr et al. (2016) showed that "PqqE, in conjunction with PqqD, carries out the first step in PQQ biosynthesis: a radical-mediated formation of a new carbon-carbon bond between two amino acid side chains on PqqA" ([PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/)). A two-component protease then excises the intermediate — "a protease/peptidase required for the excision of an early, cross-linked di-amino acid precursor to pyrroloquinoline quinone" ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)). The same review lays out the enzymatic sequence that "span[s] radical SAM activity (PqqE), aided by a peptide chaperone (PqqD), a dual hydroxylase (PqqB), and an eight-electron, eight-proton oxidase (PqqC)" — placing PqqB unambiguously **between PqqE/PqqD and PqqC**. The 2020 Klinman review synthesizes the mechanisms of PqqE, PqqF/G, and PqqB ([PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)).

### F007 — Cytoplasmic biosynthesis; periplasmic cofactor utilization

PQQ biosynthesis begins with the cytoplasmic peptide PqqA and proceeds through soluble enzymes. PqqB was crystallized as a soluble recombinant protein ([PMID: 28825148](https://pubmed.ncbi.nlm.nih.gov/28825148/)) and carries no signal peptide or membrane-spanning region, consistent with a **cytoplasmic** site of action. The mature cofactor, by contrast, functions extracytoplasmically: An & Moe (2016) note that gluconic acid "is produced from glucose by a periplasmic glucose dehydrogenase (GDH) that requires pyrroloquinoline quinone (PQQ) as a redox coenzyme" ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). Thus PqqB's biochemistry is cytoplasmic, while the product it helps make is exported to the periplasm.

### F008 — Mechanism and substrate specificity: two-step O insertion into the tyrosine ring

A QM/MM computational study (Liu & Liu, 2022) resolved the chemical mechanism at atomic detail: "PqqB catalyzes the stepwise insertions of two oxygen atoms into the tyrosine ring of the diamino acid substrate, generating the quinone moiety of PQQ" ([PMID: 35362953](https://pubmed.ncbi.nlm.nih.gov/35362953/)). The two insertions proceed via distinct iron–oxygen species: "the first hydroxylation is performed by the highly reactive FeIV-oxo species and follows the typical H-abstraction/hydroxyl rebound mechanism" (as in α-ketoglutarate-dependent enzymes), whereas "the second hydroxylation is achieved by the Fe-O2 species" (an FeII-superoxide). Second-sphere residues Asp90 and His240 act as acid–base catalysts. This defines PqqB's **substrate** (the tyrosine ring of the cross-linked Glu–Tyr diamino-acid intermediate) and its **product** (the quinone-bearing AHQQ, the immediate substrate for PqqC).

### F009 — Minority hypothesis: a contested PQQ-transport role

The functional history of PqqB has not been entirely settled. Choudhary et al. (2022) note that "the role of PqqB is quite ambiguous as its functional role has been contradicted in many studies" ([PMID: 33287678](https://pubmed.ncbi.nlm.nih.gov/33287678/)). Using homology modeling, docking, and molecular-dynamics simulation of *Pseudomonas stutzeri* PqqB, they reported binding of mature PQQ (binding energy −182.7 ± 16.6 kJ/mol) and proposed that "PQQ can be taken up by PqqB and transported to periplasm for the oxidation of glucose." This is a **computational inference** and should be weighed against the direct experimental demonstration of hydroxylase activity ([PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)). The two are not strictly mutually exclusive, but the biosynthetic hydroxylase role rests on far stronger evidence.

### F010 — Homodimer with a structural Zn²⁺ (CxCxxC) site and a plastic catalytic metal site

Tu et al. (2017) determined *P. putida* PqqB structures "bound to Mn2+, Mg2+, Cu2+, and Zn2+" at the canonical MBL active site, demonstrating metal-binding plasticity on a uniform main-chain scaffold ([PMID: 28825148](https://pubmed.ncbi.nlm.nih.gov/28825148/)). Beyond the catalytic site, "PqqB belongs to a small subclass of MBLs that contain an additional CxCxxC motif that binds a structural Zn2+," and the authors' "data support a key role for this motif in dimerization." PqqB is therefore a **homodimer**, with one metal site dedicated to catalysis (physiologically iron) and a second, structural Zn²⁺ site stabilizing the quaternary assembly.

### F011 — In vivo genetics: *pqqB* is required for functional PQQ and quinoprotein activity

Loss-of-function genetics in related bacteria confirm the physiological requirement. In *Pseudomonas extremaustralis*, PQQ-dependent alcohol/ethanol dehydrogenase "activity was abolished in a pqqB mutant strain," and "the exaA and pqqB genes are essential for growth under low temperature" on sodium octanoate (Tribelli et al., 2015; [PMID: 26671564](https://pubmed.ncbi.nlm.nih.gov/26671564/)). In *Rahnella aquatilis* HX2, "mutants of HX2 unable to produce PQQ were obtained by in-frame deletion of either the pqqA or pqqB gene," and "pqqA and pqqB genes individually play important functions in PQQ biosynthesis and are required for antibacterial activity and phosphorous solubilization," with all phenotypes restored by complementation (Li et al., 2014; [PMID: 25502691](https://pubmed.ncbi.nlm.nih.gov/25502691/)). These clean deletion/complementation experiments provide the strongest in vivo evidence that *pqqB* is required for PQQ biosynthesis.

---

## Mechanistic Model / Interpretation

PqqB sits in the middle of a compact, conserved biosynthetic assembly line that builds one of nature's most complex small-molecule cofactors from a short peptide. The pathway can be summarized as:

```
          Ribosome
             │
        PqqA (peptide; contains conserved Glu + Tyr)
             │
   PqqE (radical-SAM) + PqqD (peptide chaperone)
             │   de novo C–C cross-link between Glu and Tyr side chains
             ▼
   Cross-linked PqqA
             │
   PqqF / PqqG (two-component protease)
             │   excision of the cross-linked di-amino-acid intermediate
             ▼
   Glu–Tyr diamino-acid intermediate  ────────────┐
             │                                     │  SUBSTRATE
   ┌─────────┴──────────┐                          │
   │  PqqB              │  non-heme Fe hydroxylase │
   │  (this protein)    │  O2-dependent            │
   │                    │                          │
   │  Step 1: Fe(IV)=O  →  1st OH  (H-abstraction / OH rebound)
   │  Step 2: Fe–O2 (superoxide) → 2nd OH          │
   │  Asp90 / His240 = acid–base catalysts         │
   └─────────┬──────────┘                          │
             ▼                                     │
   AHQQ  (quinone moiety formed) ──────────────────┘  PRODUCT
             │
   PqqC (8 e⁻ / 8 H⁺ oxidase)
             │   final oxidative ring closure
             ▼
   PQQ (mature cofactor, cytoplasm)
             │
     Export to periplasm
             ▼
   PQQ-dependent Glucose Dehydrogenase (GDH, periplasm)
             │   glucose → gluconic acid
             ▼
   Mineral phosphate solubilization / periplasmic redox metabolism
```

**Chemical logic.** PQQ's defining feature is its *ortho*-quinone, the redox-active center that cycles between quinone, semiquinone, and quinol states in quinoprotein dehydrogenases. Building that quinone requires installing two oxygen atoms onto the aromatic ring derived from the PqqA tyrosine. PqqB accomplishes exactly this via two chemically distinct oxygenation events (F002, F008): a classic Fe(IV)=O hydroxylation followed by an Fe–superoxide-mediated second insertion. The requirement for molecular oxygen observed decades earlier (F005) is the physiological signature of this chemistry. The MBL scaffold — repurposed from hydrolysis to oxygen chemistry by a degenerate metal-binding motif (F003, F010) — provides the iron site, making PqqB a genuine evolutionary novelty within its superfamily.

**Structure–function integration.** The crystallographic picture (F003, F010) explains the biochemistry: a plastic active-site metal pocket (able to bind Mn, Mg, Cu, Zn in vitro, iron in vivo) is consistent with a mononuclear non-heme iron center, while the auxiliary structural Zn²⁺ (CxCxxC) enforces the catalytically relevant homodimer.

**Spatial organization.** All of this occurs in the cytoplasm on soluble intermediates (F007). Only the finished cofactor is trafficked to the periplasm, where GDH performs the physiologically important glucose oxidation that underlies *P. putida*'s rhizosphere lifestyle and phosphate-solubilizing capability (F004, F007, F011).

**The transport question.** The historically "ambiguous" reputation of PqqB (F009) is best understood as a legacy of the era before its enzymatic activity was demonstrated in 2019. The computational transport hypothesis captures a real observation — PqqB can bind mature PQQ — but the weight of evidence now firmly favors a biosynthetic hydroxylase role. If PqqB also participates in cofactor handling/sequestration, that would be an interesting secondary function, but it cannot displace the primary catalytic assignment.

| Attribute | Assignment | Strength of evidence |
|---|---|---|
| Primary molecular function | Non-heme Fe(II)-dependent hydroxylase (dual O insertion) | **Strong** — direct biochemistry ([PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)) + QM/MM ([PMID: 35362953](https://pubmed.ncbi.nlm.nih.gov/35362953/)) |
| Substrate | Tyrosine ring of cross-linked Glu–Tyr diamino-acid intermediate | Strong (mechanistic + pathway logic) |
| Product | AHQQ (quinone-bearing precursor of PQQ) | Strong |
| Pathway position | After PqqE/PqqD + PqqF/G; before PqqC | Strong ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)) |
| Quaternary structure | Homodimer; structural Zn²⁺ (CxCxxC) | Strong (crystallography) |
| Fold | Degenerate metallo-β-lactamase superfamily | Strong (crystallography) |
| Localization (enzyme) | Cytoplasm (soluble) | Strong (inference; no signal peptide) |
| Localization (product use) | Periplasm (GDH) | Strong ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)) |
| In vivo requirement | Required for PQQ / quinoprotein activity | Strong (deletion + complementation) |
| Alternative transport role | Binds PQQ; proposed periplasmic transport | **Weak** — computational only ([PMID: 33287678](https://pubmed.ncbi.nlm.nih.gov/33287678/)) |

---

## Evidence Base

| PMID | Study (paraphrased) | Contribution to this annotation |
|---|---|---|
| [30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/) | Koehn et al. 2019 — *Discovery of hydroxylase activity for PqqB* | **Cornerstone.** Direct biochemical demonstration that PqqB is an iron-dependent hydroxylase inserting O to form the PQQ quinone; unprecedented in MBL family. |
| [28825148](https://pubmed.ncbi.nlm.nih.gov/28825148/) | Tu et al. 2017 — *Crystal structures / metal-binding plasticity of P. putida PqqB* | Structural basis: MBL fold, degenerate HxHxDH motif, multi-metal binding, structural Zn²⁺/CxCxxC dimerization. Uses the exact target organism/protein. |
| [35362953](https://pubmed.ncbi.nlm.nih.gov/35362953/) | Liu & Liu 2022 — *QM/MM study of PqqB hydroxylation* | Atomistic mechanism: stepwise two-O insertion into the tyrosine ring via Fe(IV)=O then Fe–O2; Asp90/His240 catalysis; product AHQQ. |
| [31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/) | Martins et al. 2019 — *Two-component PqqF/G protease* | Places PqqB in the ordered pathway (PqqE→PqqD→protease→PqqB→PqqC); "dual hydroxylase." |
| [26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/) | Barr et al. 2016 — *PqqE radical-SAM cross-linking* | Defines the upstream step producing PqqB's substrate precursor. |
| [32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/) | Klinman 2020 — *Biogenesis of PQQ (review)* | Authoritative synthesis of PqqE, PqqF/G, PqqB mechanisms. |
| [27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/) | An & Moe 2016 — *Regulation of PQQ-GDH in P. putida KT2440* | Target-organism operon architecture (*pqqFABCDEG*), expression–PQQ coupling, periplasmic GDH utilization. |
| [7665488](https://pubmed.ncbi.nlm.nih.gov/7665488/) | Velterop et al. 1995 — *In vivo/in vitro PQQ synthesis* | PqqB is rate-enhancing but partially bypassable; PQQ synthesis requires O₂. |
| [26671564](https://pubmed.ncbi.nlm.nih.gov/26671564/) | Tribelli et al. 2015 — *P. extremaustralis pqqB* | In vivo: pqqB mutant abolishes PQQ-dependent ADH; essential at low temperature. |
| [25502691](https://pubmed.ncbi.nlm.nih.gov/25502691/) | Li et al. 2014 — *Rahnella aquatilis HX2 pqq deletions* | In vivo: clean in-frame pqqB deletion abolishes PQQ, phosphate solubilization, antibacterial activity; complementation restores. |
| [33287678](https://pubmed.ncbi.nlm.nih.gov/33287678/) | Choudhary et al. 2022 — *Biological role of PqqB (in silico)* | Minority hypothesis: computational PQQ binding/transport role; documents historical ambiguity. |

Supporting/contextual quinocofactor reviews: [PMID: 24350630](https://pubmed.ncbi.nlm.nih.gov/24350630/), [PMID: 7979241](https://pubmed.ncbi.nlm.nih.gov/7979241/), [PMID: 8910283](https://pubmed.ncbi.nlm.nih.gov/8910283/), [PMID: 1851106](https://pubmed.ncbi.nlm.nih.gov/1851106/); a biotechnology PQQ-overproduction study ([PMID: 32080751](https://pubmed.ncbi.nlm.nih.gov/32080751/)) and a pqq-promoter regulation study in *Serratia* ([PMID: 28709697](https://pubmed.ncbi.nlm.nih.gov/28709697/)).

---

## Limitations and Knowledge Gaps

1. **No PqqB structure from *P. putida* KT2440 has been reported with a physiological iron center or bound substrate/product.** The crystal structures capture surrogate metals (Mn, Mg, Cu, Zn) at the active site; the catalytically competent Fe form and an enzyme–substrate complex remain to be visualized directly.

2. **The detailed two-step mechanism (Fe(IV)=O then Fe–superoxide) rests on QM/MM computation** ([PMID: 35362953](https://pubmed.ncbi.nlm.nih.gov/35362953/)). While consistent with the biochemistry, direct spectroscopic detection of the proposed iron–oxygen intermediates has not been established here.

3. **Partial bypass of PqqB** in some heterologous systems ([PMID: 7665488](https://pubmed.ncbi.nlm.nih.gov/7665488/)) is not fully explained. Whether residual PQQ arises from slow non-enzymatic oxidation of the intermediate, or from an alternative enzyme, is unresolved.

4. **The transport hypothesis is unresolved but low-weight.** Whether PqqB has any genuine secondary role in binding/chaperoning/exporting mature PQQ ([PMID: 33287678](https://pubmed.ncbi.nlm.nih.gov/33287678/)) has not been tested experimentally and is currently speculative.

5. **Most in vivo genetic evidence comes from related organisms** (*P. extremaustralis*, *R. aquatilis*, *K. pneumoniae*) rather than *P. putida* KT2440 itself, though the operon and pathway are highly conserved and An & Moe (2016) directly address KT2440.

6. **Substrate stereochemistry / exact chemical identity of the diamino-acid intermediate that PqqB accepts** is inferred from the collective pathway model; direct isolation and structural confirmation of the PqqB substrate in *P. putida* would strengthen the annotation.

---

## Proposed Follow-up Experiments / Actions

1. **Reconstitute *P. putida* KT2440 PqqB with Fe(II) in vitro** and assay hydroxylation of the authentic cross-linked Glu–Tyr intermediate, quantifying O₂ consumption and AHQQ formation (LC–MS), to confirm the KT2440 ortholog directly (extending [PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)).

2. **Trap and spectroscopically characterize the iron–oxygen intermediates** (stopped-flow, Mössbauer, EPR, rapid-freeze-quench) to test the computational prediction of an Fe(IV)=O first step and an Fe–superoxide second step ([PMID: 35362953](https://pubmed.ncbi.nlm.nih.gov/35362953/)).

3. **Solve a substrate/product-bound, iron-loaded PqqB crystal (or cryo-EM) structure** to define active-site geometry and validate the roles of Asp90 and His240 as acid–base catalysts.

4. **Site-directed mutagenesis of the CxCxxC motif and second-sphere residues** (Asp90, His240) followed by activity, metal-content, and dimerization assays, to dissect catalytic vs. structural metal roles (building on [PMID: 28825148](https://pubmed.ncbi.nlm.nih.gov/28825148/)).

5. **Construct a clean in-frame Δ*pqqB* deletion in *P. putida* KT2440** and quantify PQQ, periplasmic GDH activity, gluconic-acid production, and phosphate solubilization, with plasmid complementation — porting the *Rahnella* design ([PMID: 25502691](https://pubmed.ncbi.nlm.nih.gov/25502691/)) into the target strain.

6. **Directly test the transport hypothesis:** measure periplasmic vs. cytoplasmic PQQ distribution in wild-type vs. Δ*pqqB* (complemented with catalytically dead PqqB) to determine whether PqqB has any role in cofactor localization independent of its biosynthetic function ([PMID: 33287678](https://pubmed.ncbi.nlm.nih.gov/33287678/)).

7. **Isotope-labeling (¹⁸O₂) metabolic tracing** to confirm that both quinone oxygens of PQQ derive from molecular O₂ via PqqB in vivo, tying together F005 and F008.

---

*Gene identity verification:* All retrieved literature is specific to PqqB in PQQ biosynthesis; there is no evidence of a gene-symbol collision with an unrelated protein. The gene symbol *pqqB*, locus PP_0379, PqqB/HAMAP MF_00653 family assignment, and MBL-fold domain architecture are mutually consistent with the UniProt record for Q88QV5 in *Pseudomonas putida* KT2440.


## Artifacts

- [OpenScientist final report](pqqB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pqqB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31427437
2. PMID:27287323
3. PMID:30811189
4. PMID:28825148
5. PMID:7665488
6. PMID:26961875
7. PMID:32731194
8. PMID:35362953
9. PMID:33287678
10. PMID:26671564
11. PMID:25502691
12. PMID:24350630
13. PMID:7979241
14. PMID:8910283
15. PMID:1851106
16. PMID:32080751
17. PMID:28709697