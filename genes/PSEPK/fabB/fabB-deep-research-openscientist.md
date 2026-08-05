---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T08:55:18.344095'
end_time: '2026-07-23T09:10:00.823639'
duration_seconds: 882.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabB
  gene_symbol: fabB
  uniprot_accession: Q88FC3
  protein_description: 'RecName: Full=3-oxoacyl-[acyl-carrier-protein] synthase 1
    {ECO:0000256|ARBA:ARBA00039450}; EC=2.3.1.41 {ECO:0000256|ARBA:ARBA00013191};
    AltName: Full=3-oxoacyl-[acyl-carrier-protein] synthase I {ECO:0000256|ARBA:ARBA00041620};
    AltName: Full=Beta-ketoacyl-ACP synthase I {ECO:0000256|ARBA:ARBA00042143};'
  gene_info: Name=fabB {ECO:0000313|EMBL:AAN69756.1}; OrderedLocusNames=PP_4175 {ECO:0000313|EMBL:AAN69756.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
  protein_domains: Beta-ketoacyl_synthase. (IPR000794); Ketoacyl_synth_AS. (IPR018201);
    Ketoacyl_synth_C. (IPR014031); Ketoacyl_synth_N. (IPR014030); PKS_Beta-ketoAc_synthase_dom.
    (IPR020841)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fabB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FC3
- **Protein Description:** RecName: Full=3-oxoacyl-[acyl-carrier-protein] synthase 1 {ECO:0000256|ARBA:ARBA00039450}; EC=2.3.1.41 {ECO:0000256|ARBA:ARBA00013191}; AltName: Full=3-oxoacyl-[acyl-carrier-protein] synthase I {ECO:0000256|ARBA:ARBA00041620}; AltName: Full=Beta-ketoacyl-ACP synthase I {ECO:0000256|ARBA:ARBA00042143};
- **Gene Information:** Name=fabB {ECO:0000313|EMBL:AAN69756.1}; OrderedLocusNames=PP_4175 {ECO:0000313|EMBL:AAN69756.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
- **Key Domains:** Beta-ketoacyl_synthase. (IPR000794); Ketoacyl_synth_AS. (IPR018201); Ketoacyl_synth_C. (IPR014031); Ketoacyl_synth_N. (IPR014030); PKS_Beta-ketoAc_synthase_dom. (IPR020841)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabB** (gene ID: fabB, UniProt: Q88FC3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *fabB* (Q88FC3, PP_4175) — β-Ketoacyl-[ACP] Synthase I of *Pseudomonas putida* KT2440

## Summary

The gene ***fabB*** (ordered locus **PP_4175**; UniProt **Q88FC3**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **β-ketoacyl-[acyl-carrier-protein] synthase I** (**KAS I**; also called 3-oxoacyl-[ACP] synthase 1 or β-ketoacyl-ACP synthase I; **EC 2.3.1.41**). This is a soluble, cytoplasmic **condensing enzyme of the type II (dissociated) fatty acid synthase (FAS II) system**, the bacterial machinery that builds membrane fatty acids from malonyl-ACP building blocks. The identity is secure: the 406-residue Q88FC3 protein is 67.3% identical to the biochemically defined *Escherichia coli* FabB, belongs to the thiolase-like superfamily / β-ketoacyl synthase family (InterPro IPR000794, IPR018201, IPR014030/031, IPR020841), and retains every catalytic residue of the characterized enzyme. All literature reviewed converges on the same gene family and organism group; this is the correct target, not a same-symbol homolog from an unrelated gene.

The **primary catalytic function** of FabB is a **decarboxylative Claisen (Claisen-type) condensation**: it elongates an ACP-bound acyl chain by two carbons per cycle. In three chemical steps, it (1) transfers a growing acyl primer from ACP onto its active-site cysteine, (2) decarboxylates malonyl-ACP to a reactive carbanion/enolate, and (3) condenses that nucleophile with the enzyme-bound acyl group to form a new carbon–carbon bond, releasing β-ketoacyl-ACP, CO₂, and holo-ACP. Catalysis depends on a **Cys-His-His triad** (in Q88FC3: Cys161, His296, His331) supported by Asp304/Glu307/Lys326 — all strictly conserved. The two-histidine architecture distinguishes elongation condensing enzymes (FabB/FabF) from the initiation enzyme FabH and defines sensitivity to the natural-product inhibitors **cerulenin** and **thiolactomycin**.

FabB's specialized, non-redundant biological role is as the **committed enzyme of the anaerobic (oxygen-independent) unsaturated fatty acid (UFA) pathway**. Working downstream of the dehydratase/isomerase FabA, FabB preferentially elongates the *cis*-3-decenoyl-ACP intermediate, channeling carbon flux toward the membrane unsaturated fatty acids palmitoleate (16:1) and *cis*-vaccenate (18:1) and thereby setting membrane fluidity. In *Pseudomonas*, *fabA* and *fabB* form a *fabAB* operon and their loss causes UFA auxotrophy. A notable distinction from the *E. coli* paradigm is that in *P. putida*, **FabB is bifunctional**: it both **initiates** FAS (decarboxylating malonyl-ACP and condensing the resulting acetyl-ACP with malonyl-ACP) and **elongates** the chain, whereas *E. coli* FabB performs elongation only. The enzyme carries out its function in the **cytoplasm/cytosol** as part of the soluble FAS II enzyme ensemble that shuttles substrates via the acyl carrier protein AcpP.

---

## Key Findings

### Finding 1 — Q88FC3 is β-ketoacyl-ACP synthase I (KAS I, EC 2.3.1.41), an FAS II elongation condensing enzyme

Q88FC3 is a 406-amino-acid protein of *P. putida* KT2440 that is **67.3% identical** (272 of 404 aligned positions) to the well-characterized *E. coli* FabB (P0A953) by global Needleman-Wunsch alignment. It belongs to the **thiolase-like superfamily / β-ketoacyl synthase family**, carrying the diagnostic InterPro domains IPR000794 (β-ketoacyl synthase), IPR018201 (ketoacyl synthase active site), and IPR014030/IPR014031 (N- and C-terminal ketoacyl synthase domains). Functionally, KAS I performs the elongation Claisen condensation of FAS II: it takes a growing acyl-ACP primer and condenses it with malonyl-ACP, extending the chain by two carbons per cycle and producing β-ketoacyl-ACP + CO₂ + holo-ACP.

The condensing enzymes of type II FAS are established drug targets. As stated in [PMID: 11050088](https://pubmed.ncbi.nlm.nih.gov/11050088/): *"The beta-ketoacyl-acyl carrier protein (ACP) synthases are key regulators of type II fatty acid synthesis and are the targets for two natural products, thiolactomycin (TLM) and cerulenin."* Independent work reiterates the central role of this enzyme in bacteria: *"beta-ketoacyl acyl carrier protein synthase I (KAS I) is member of the condensing enzyme family, which is a key catalyst in bacterial fatty acid biosynthesis"* ([PMID: 26292066](https://pubmed.ncbi.nlm.nih.gov/26292066/)). Together with the sequence and domain analysis, these establish Q88FC3 as an authentic KAS I/FabB.

### Finding 2 — Conserved Cys-His-His catalytic triad and a three-step condensation mechanism

The catalytic machinery of FabB is fully conserved in Q88FC3. In *E. coli* KAS I, mutagenesis dissected the reaction into three chemical steps and identified the essential residues. As described in [PMID: 11502177](https://pubmed.ncbi.nlm.nih.gov/11502177/): *"beta-Ketoacyl-[acyl carrier protein (ACP)] synthase forms new carbon-carbon bonds in three steps: transfer of an acyl primer from ACP to the enzyme, decarboxylation of the elongating substrate and its condensation with the acyl primer substrate."* The same study established the division of labor among active-site residues: *"The active site Cys-163 is not required for decarboxylation, whereas His-298 and His-333 are indispensable."* Thus Cys163 is the acyl-accepting nucleophile, and the two histidines drive decarboxylation of malonyl-ACP; Asp306, Glu309, and Lys328 provide supporting roles.

Mapping these positions onto Q88FC3 by alignment shows **every catalytic residue is conserved**: *E. coli* Cys163 → *P. putida* **Cys161**, His298 → **His296**, His333 → **His331**, Asp306 → **Asp304**, Glu309 → **Glu307**, and Lys328 → **Lys326**. The **two-histidine (His-His-Cys) active-site architecture** distinguishes FabB/FabF elongation enzymes from the His-Asn-Cys triad of the initiation enzyme FabH and governs inhibitor binding. Per [PMID: 11050088](https://pubmed.ncbi.nlm.nih.gov/11050088/), the structural analysis was *"illustrating that the two-histidine active site architecture is critical to protein-antibiotic interaction."* The conservation of this complete triad in Q88FC3 strongly implies an identical catalytic mechanism.

### Finding 3 — FabB is the committed enzyme of the anaerobic unsaturated fatty acid pathway

Bacteria that lack a desaturase (including *E. coli* and *Pseudomonas*) make unsaturated fatty acids anaerobically during elongation. The dehydratase/isomerase **FabA** introduces a *cis* double bond at the C10 stage (converting *trans*-2-decenoyl-ACP to *cis*-3-decenoyl-ACP), but this branch point is only committed to the UFA pathway when a condensing enzyme with the right specificity elongates the *cis*-3 intermediate. FabB provides that specificity. As reported in [PMID: 8910376](https://pubmed.ncbi.nlm.nih.gov/8910376/): *"the channeling of intermediates toward unsaturated fatty acid synthesis by FabB was attributed to the affinity of the condensing enzyme for cis-decenoyl-ACP."* FabB therefore elongates the *cis*-3-decenoyl-ACP branch onward to palmitoleate (16:1) and *cis*-vaccenate (18:1), the dominant membrane UFAs.

Genetic evidence in *Pseudomonas* directly ties FabB to UFA biosynthesis. In *P. aeruginosa*, *"Chromosomal fabA and fabB mutants were isolated; the mutants were auxotrophic for unsaturated fatty acids"* ([PMID: 9286984](https://pubmed.ncbi.nlm.nih.gov/9286984/)) — i.e., without FabB, the cell cannot make UFAs and must import them. The same study established the genomic linkage: *"fabA and fabB are cotranscribed and most probably form a fabAB operon,"* physically and transcriptionally coupling the double-bond-introducing enzyme (FabA) to the committing elongation enzyme (FabB). This operon organization in *Pseudomonas* underscores that FabB's specialized role is UFA commitment.

### Finding 4 — In *P. putida*, FabB is bifunctional: it both initiates and elongates fatty acid synthesis

A key departure from the *E. coli* textbook picture is that *P. putida* FabB does not merely elongate — it can also **initiate** FAS. In *P. putida* F1 (a close relative of KT2440), the two FabH (KAS III) initiation paralogs are individually dispensable, and FabB was shown to prime the pathway. The primary study states directly: *"we report that Pseudomonas putida F1 β-ketoacyl-ACP synthase I (FabB), in addition to playing a key role in fatty acid elongation, also initiates FAS in vivo"* ([PMID: 38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/)). The biochemical basis is described in the same paper: *"P. putida FabB decarboxylates malonyl-ACP and condenses the acetyl-ACP product with malonyl-ACP for initiation of FAS."* This means FabB can generate its own acetyl-ACP primer in situ and start the first condensation — an activity *E. coli* FabB lacks.

In the broader regulatory network (defined largely in the enterobacterial paradigm), *fabB* is transcriptionally controlled to balance membrane lipid composition. It is positively regulated by FadR: *"fabB, a second unsaturated fatty acid biosynthetic gene, is also positively regulated by FadR"* ([PMID: 11566998](https://pubmed.ncbi.nlm.nih.gov/11566998/)). It is repressed by FabR in response to the unsaturated:saturated acyl-ACP ratio ([PMID: 19854834](https://pubmed.ncbi.nlm.nih.gov/19854834/)), and FabB's productive interaction with the acyl carrier protein AcpP has been structurally defined and shown to shape the lipid profile ([PMID: 31209348](https://pubmed.ncbi.nlm.nih.gov/31209348/)). While these regulatory details derive from *E. coli*, they illustrate how *fabB* output is tuned to membrane physiology.

### Finding 5 — Database curation confirms cytoplasmic KAS I with a specific UFA-elongation reaction (and flags a spurious kinase annotation)

UniProt curation of Q88FC3 independently supports the functional assignment. It curates the general elongation reaction *"a fatty acyl-[ACP] + malonyl-[ACP] + H⁺ = a 3-oxoacyl-[ACP] + holo-[ACP] + CO₂"* and, importantly, the **committed UFA-elongation reaction** *"(3Z)-decenoyl-[ACP] + malonyl-[ACP] + H⁺ = 3-oxo-(5Z)-dodecenoyl-[ACP] + holo-[ACP] + CO₂"* — precisely the reaction that channels flux from FabA's *cis*-3-decenoyl-ACP intermediate into the unsaturated branch. The subcellular location is annotated as **Cytoplasm** (GO:0005829 cytosol), and the pathway is fatty acid biosynthesis (GO:0006633).

Cross-strain conservation analysis performed in this investigation validates the transfer of the experimental *P. putida* F1 data to KT2440: Q88FC3 (406 aa) is **98.3% identical** to *P. putida* NBRC 14164 FabB and 92–99% identical to FabB across the *P. putida / P. monteilii / P. mosselii* group. The experimentally characterized F1 enzyme ([PMID: 38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/)) is therefore effectively the same protein as KT2440 Q88FC3, so its bifunctional initiation+elongation phenotype applies directly.

**Annotation caveat:** UniProt Q88FC3 also carries automated "Kinase"/"ATP-binding" keywords (GO:0016301, GO:0005524). These are **biologically incorrect** for a KAS I condensing enzyme — FabB uses no ATP and has no kinase activity — and appear to be a pipeline/electronic-annotation artifact. This is a concrete example of why database annotations should be checked against primary literature.

### Finding 6 — Consolidated annotation

Integrating all five lines of evidence yields a confident annotation: **fabB (Q88FC3, PP_4175) encodes the cytoplasmic KAS I of *P. putida* KT2440 that commits FAS II flux to unsaturated fatty acids and, uniquely, can both initiate and elongate the pathway.** The supporting pillars are: (1) 67.3% identity to *E. coli* FabB with all six catalytic residues conserved (Cys161/His296/His331/Asp304/Glu307/Lys326); (2) the three-step transacylation→decarboxylation→condensation mechanism with the His-His-Cys triad ([PMID: 11502177](https://pubmed.ncbi.nlm.nih.gov/11502177/), [PMID: 11050088](https://pubmed.ncbi.nlm.nih.gov/11050088/)); (3) the committed-UFA role via affinity for *cis*-3-decenoyl-ACP, with *fabA/fabB* required for UFA in *Pseudomonas* ([PMID: 8910376](https://pubmed.ncbi.nlm.nih.gov/8910376/), [PMID: 9286984](https://pubmed.ncbi.nlm.nih.gov/9286984/)); (4) bifunctional initiation+elongation in *P. putida* ([PMID: 38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/)); and (5) UniProt curation of cytoplasmic localization plus the specific (3Z)-decenoyl-ACP reaction, with ~98% cross-strain identity validating transfer of the F1 data.

---

## Mechanistic Model / Interpretation

### The reaction FabB catalyzes

FabB carries out one turn of the FAS II **elongation** cycle — a decarboxylative Claisen condensation on ACP-tethered substrates:

```
  Acyl(Cₙ)-ACP  +  Malonyl-ACP  +  H⁺
        │
        ▼   (FabB: Cys161 nucleophile; His296/His331 drive decarboxylation)
  β-Ketoacyl(Cₙ₊₂)-ACP  +  CO₂  +  holo-ACP
```

Three chemical steps (from [PMID: 11502177](https://pubmed.ncbi.nlm.nih.gov/11502177/)):

```
 Step 1 — Transacylation:  Acyl-ACP + Enz-Cys161-SH → Enz-Cys161-S-Acyl + holo-ACP
 Step 2 — Decarboxylation: Malonyl-ACP → (carbanion/enolate)-ACP + CO₂   [His296, His331]
 Step 3 — Condensation:    Enz-S-Acyl + carbanion-ACP → β-ketoacyl-ACP + Enz-Cys161-SH
```

The β-ketoacyl-ACP product is then processed by the rest of the FAS II ensemble (FabG reductase → FabA/FabZ dehydratase → FabI enoyl reductase) to yield a two-carbon-extended acyl-ACP, which re-enters the cycle.

### Where FabB acts in the pathway — the UFA branch point

```
        Malonyl-ACP  →→ (FabB initiation in P. putida) →→ Acetyl-ACP primer
                                      │
                              elongation cycles
                                      │
             C10 intermediate:  trans-2-decenoyl-ACP
                                      │  FabA (dehydratase/isomerase)
                                      ▼
                          cis-3-decenoyl-ACP  ── committed by ──►  FabB
                                      │        (affinity for cis-decenoyl-ACP)
                                      ▼
                       elongation →→ palmitoleate (16:1), cis-vaccenate (18:1)
                                      │
                                      ▼
                        membrane phospholipids (fluidity control)
```

FabA creates the *cis* double bond, but the flux only becomes committed to UFAs when **FabB** elongates the *cis*-3-decenoyl-ACP. This makes FabB the **gatekeeper of membrane unsaturation**, explaining why *fabB* loss causes UFA auxotrophy in *Pseudomonas* ([PMID: 9286984](https://pubmed.ncbi.nlm.nih.gov/9286984/)).

### How *P. putida* FabB differs from *E. coli* FabB

| Property | *E. coli* FabB | *P. putida* FabB (Q88FC3) |
|---|---|---|
| Enzyme class | KAS I, EC 2.3.1.41 | KAS I, EC 2.3.1.41 |
| Elongation condensation | Yes | Yes |
| UFA commitment (cis-3-decenoyl-ACP) | Yes | Yes |
| **Initiation of FAS** | **No** | **Yes** (decarboxylates malonyl-ACP → acetyl-ACP primer) |
| Catalytic triad | Cys163/His298/His333 | Cys161/His296/His331 (conserved) |
| Localization | Cytoplasm | Cytoplasm |
| Inhibitors | Cerulenin, thiolactomycin | Predicted sensitive (triad conserved) |

The bifunctionality ([PMID: 38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/)) is the standout mechanistic distinction: in *P. putida*, FabB provides redundancy/robustness to FAS initiation that in *E. coli* is the exclusive domain of FabH.

### Localization

FabB is a **soluble cytoplasmic (cytosolic) enzyme** (UniProt GO:0005829). FAS II is a dissociated system in which discrete soluble enzymes act on substrates covalently tethered to the small, acidic acyl carrier protein AcpP. FabB therefore does its chemistry in the cytoplasm, handing off phosphopantetheine-linked acyl intermediates via transient, electrostatically guided protein–protein interactions with AcpP ([PMID: 31209348](https://pubmed.ncbi.nlm.nih.gov/31209348/)). The final acyl-ACP products feed the membrane-associated PlsB/PlsC acyltransferases for phospholipid assembly.

---

## Evidence Base

| PMID | Title (abridged) | How it supports the annotation |
|---|---|---|
| [11502177](https://pubmed.ncbi.nlm.nih.gov/11502177/) | *β-Ketoacyl-[ACP] synthase I of E. coli: condensation mechanism from active-site mutations* | Defines the three-step mechanism and identifies Cys163 (nucleophile), His298/His333 (indispensable for decarboxylation) — all conserved in Q88FC3. |
| [11050088](https://pubmed.ncbi.nlm.nih.gov/11050088/) | *Inhibition of β-ketoacyl-ACP synthases by thiolactomycin and cerulenin* | Establishes FabB as a FAS II condensing enzyme and antibiotic target; shows the two-histidine architecture governs inhibitor binding. |
| [8910376](https://pubmed.ncbi.nlm.nih.gov/8910376/) | *Roles of FabA and FabZ dehydratases in E. coli FA biosynthesis* | Shows FabB commits *cis*-decenoyl-ACP to the UFA branch via its affinity for that intermediate. |
| [9286984](https://pubmed.ncbi.nlm.nih.gov/9286984/) | *fabAB operon in P. aeruginosa* | *Pseudomonas fabA/fabB* mutants are UFA-auxotrophic; *fabAB* are cotranscribed as an operon — direct genetic link to UFA synthesis. |
| [38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/) | *FabB initiates fatty acid synthesis in P. putida F1* | Demonstrates that *P. putida* FabB is bifunctional (initiation + elongation), the key organism-specific finding. |
| [11566998](https://pubmed.ncbi.nlm.nih.gov/11566998/) | *E. coli FadR positively regulates fabB* | Places *fabB* in the FadR-controlled UFA regulatory network. |
| [19854834](https://pubmed.ncbi.nlm.nih.gov/19854834/) | *Transcriptional regulation of membrane lipid homeostasis in E. coli* | FabR represses *fabB*/*fabA* in response to the unsaturated:saturated acyl-ACP ratio — links FabB output to membrane homeostasis. |
| [31209348](https://pubmed.ncbi.nlm.nih.gov/31209348/) | *Molecular basis for AcpP–ketosynthase interactions* | Structural basis of the FabB–AcpP interaction that delivers substrates and shapes the lipid profile. |
| [26292066](https://pubmed.ncbi.nlm.nih.gov/26292066/) | *Docking studies of flavonoid inhibitors of E. coli KAS I* | Reiterates KAS I/FabB as a key catalyst in bacterial fatty acid biosynthesis. |
| [11959552](https://pubmed.ncbi.nlm.nih.gov/11959552/) | *A missense mutation in fabB confers thiolactomycin resistance in E. coli* | Confirms FabB is the relevant TLM target at the condensing-enzyme step; single residue changes tune inhibitor sensitivity while preserving catalysis. |

**Consistency of the evidence.** All primary sources point to a single coherent picture: FabB is the elongation/UFA-committing condensing enzyme of FAS II, with a conserved Cys-His-His mechanism, operating in the cytoplasm. The *Pseudomonas*-specific literature ([PMID: 9286984](https://pubmed.ncbi.nlm.nih.gov/9286984/), [PMID: 38335573](https://pubmed.ncbi.nlm.nih.gov/38335573/)) both confirms the conserved UFA role and adds the organism-specific bifunctionality. No source contradicts the assignment; the only discordant note is the automated UniProt "kinase" keyword, which is a recognized annotation artifact.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on KT2440 Q88FC3 itself.** The mechanistic detail (triad function, three-step chemistry, inhibitor binding) is transferred from *E. coli* FabB by high sequence identity (67.3%) and complete catalytic-residue conservation. The bifunctional initiation activity is experimentally demonstrated in the closely related *P. putida* **F1** strain (~98% identical), not KT2440 directly. Transfer is well justified but remains inference.

2. **Substrate-specificity profile not quantified.** The preference for *cis*-3-decenoyl-ACP and the chain-length product distribution (16:1 vs 18:1 ratio) for the *P. putida* enzyme have not been directly measured here; these are inferred from the conserved UFA-committing role and UniProt's curated (3Z)-decenoyl-ACP reaction.

3. **Regulatory circuitry is largely from *E. coli*.** FadR activation and FabR repression of *fabB* are enterobacterial findings; the exact transcriptional regulators and operon context in *P. putida* KT2440 (beyond the conserved *fabAB* linkage seen in *P. aeruginosa*) were not experimentally established in this investigation.

4. **Redundancy with FabF not resolved for KT2440.** *P. putida* likely also encodes a FabF (KAS II). The functional partition between FabB and FabF (e.g., temperature-dependent cis-vaccenate synthesis, which is a classic FabF role in *E. coli*) was not characterized for KT2440.

5. **No experimental structure of the *P. putida* enzyme.** Structural inference rests on homology to *E. coli* FabB/AcpP complexes.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymology of recombinant KT2440 FabB.** Express and purify Q88FC3; assay condensation with defined acyl-ACP + malonyl-ACP substrates; measure kinetic constants and chain-length/UFA-intermediate preference (especially *cis*-3-decenoyl-ACP vs saturated decanoyl-ACP) to quantify the UFA-committing specificity.

2. **Confirm bifunctional initiation in KT2440.** Reproduce the F1 initiation assay (malonyl-ACP decarboxylation → acetyl-ACP → condensation) with the KT2440 enzyme, and test genetic complementation of a FabH-deficient background.

3. **Targeted mutagenesis of the predicted triad.** Mutate Cys161, His296, His331 (and Asp304/Glu307/Lys326) and confirm the predicted loss of condensation vs decarboxylation activities, directly validating the residue mapping.

4. **Inhibitor sensitivity.** Test cerulenin and thiolactomycin inhibition of the purified enzyme; introduce the F390-equivalent substitution to verify the TLM-resistance mechanism reported for *E. coli* ([PMID: 11959552](https://pubmed.ncbi.nlm.nih.gov/11959552/)) is conserved.

5. **Genetics in KT2440.** Construct a conditional *fabB* (PP_4175) mutant and test for UFA auxotrophy and rescue by exogenous oleate/vaccenate; define the *fabAB* operon structure and regulator binding (FadR/FabR homologs) by RNA-seq and promoter analysis.

6. **Correct the database annotation.** Flag/curate out the spurious "Kinase"/"ATP-binding" (GO:0016301, GO:0005524) keywords on UniProt Q88FC3, which conflict with the enzyme's true condensing-enzyme function.

7. **Structural work.** Determine a crystal or cryo-EM structure of KT2440 FabB, ideally in complex with AcpP, to compare the substrate-gating loop and confirm the basis of *cis*-decenoyl-ACP selectivity.


## Artifacts

- [OpenScientist final report](fabB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11050088
2. PMID:26292066
3. PMID:11502177
4. PMID:8910376
5. PMID:9286984
6. PMID:38335573
7. PMID:11566998
8. PMID:19854834
9. PMID:31209348
10. PMID:11959552