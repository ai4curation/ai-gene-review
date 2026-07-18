---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T17:44:07.158528'
end_time: '2026-07-17T17:58:54.371612'
duration_seconds: 887.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argB
  gene_symbol: argB
  uniprot_accession: P59300
  protein_description: 'RecName: Full=Acetylglutamate kinase {ECO:0000255|HAMAP-Rule:MF_00082};
    EC=2.7.2.8 {ECO:0000255|HAMAP-Rule:MF_00082}; AltName: Full=N-acetyl-L-glutamate
    5-phosphotransferase {ECO:0000255|HAMAP-Rule:MF_00082}; AltName: Full=NAG kinase
    {ECO:0000255|HAMAP-Rule:MF_00082}; Short=NAGK {ECO:0000255|HAMAP-Rule:MF_00082};'
  gene_info: Name=argB {ECO:0000255|HAMAP-Rule:MF_00082}; OrderedLocusNames=PP_5289;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the acetylglutamate kinase family. ArgB
  protein_domains: AceGlu_kinase-like_sf. (IPR036393); AcgluKinase_fam. (IPR004662);
    ArgB. (IPR037528); Asp/Glu/Uridylate_kinase. (IPR001048); Glu/AcGlu_kinase. (IPR001057)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: argB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P59300
- **Protein Description:** RecName: Full=Acetylglutamate kinase {ECO:0000255|HAMAP-Rule:MF_00082}; EC=2.7.2.8 {ECO:0000255|HAMAP-Rule:MF_00082}; AltName: Full=N-acetyl-L-glutamate 5-phosphotransferase {ECO:0000255|HAMAP-Rule:MF_00082}; AltName: Full=NAG kinase {ECO:0000255|HAMAP-Rule:MF_00082}; Short=NAGK {ECO:0000255|HAMAP-Rule:MF_00082};
- **Gene Information:** Name=argB {ECO:0000255|HAMAP-Rule:MF_00082}; OrderedLocusNames=PP_5289;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the acetylglutamate kinase family. ArgB
- **Key Domains:** AceGlu_kinase-like_sf. (IPR036393); AcgluKinase_fam. (IPR004662); ArgB. (IPR037528); Asp/Glu/Uridylate_kinase. (IPR001048); Glu/AcGlu_kinase. (IPR001057)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argB** (gene ID: argB, UniProt: P59300) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *argB* (N-Acetyl-L-Glutamate Kinase, NAGK) in *Pseudomonas putida* KT2440

**UniProt Accession:** P59300 | **Gene:** *argB* | **Ordered Locus:** PP_5289 | **EC:** 2.7.2.8
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)

---

## Summary

The *argB* gene of *Pseudomonas putida* KT2440 (UniProt **P59300**, locus **PP_5289**) encodes **N-acetyl-L-glutamate kinase (NAGK; EC 2.7.2.8)**, also called N-acetyl-L-glutamate 5-phosphotransferase. NAGK is a soluble, cytoplasmic enzyme that catalyzes the **ATP-dependent phosphorylation of the γ-carboxyl group of N-acetyl-L-glutamate (NAG)** to yield **N-acetyl-L-glutamyl-5-phosphate** and ADP. This is the **second, committed step** of the acetylated ("cyclic") ornithine branch of the L-arginine biosynthetic pathway, in which glutamate is progressively converted, through eight enzymatic steps, into arginine. The identity of the enzyme is unambiguous: gene symbol, EC number, protein family, catalytic domains, and curated GO annotations all converge on the same NAGK assignment, and no evidence of gene-symbol ambiguity was found.

NAGK belongs to the **amino-acid-kinase (AAK) family** and is, in fact, the structural paradigm of that family, which also includes carbamate kinase, UMP kinase, glutamate-5-kinase, and aspartokinase. In pseudomonads specifically, NAGK is the **rate-limiting, pathway-controlling enzyme** of arginine biosynthesis and is **allosterically feedback-inhibited by the end-product L-arginine**. Structurally, arginine-inhibitable *Pseudomonas* NAGK is a distinctive **ring-shaped hexamer** built from three E. coli-like dimers linked by an N-terminal kinked α-helix (the "N-helix"). Arginine binds each subunit and stabilizes an enlarged, catalytically unproductive active-centre conformation, while the substrate acetylglutamate counters this by promoting active-centre closure. This makes NAGK the principal regulatory valve that matches arginine production to cellular demand.

While no experimental crystal structure exists for the *P. putida* protein itself (only an AlphaFold model), the functional and mechanistic assignment rests on exceptionally strong comparative evidence. P59300 shares **92.1% sequence identity** with the exhaustively characterized *P. aeruginosa* NAGK (Q9HTN2), including full conservation of the catalytic residues, the substrate-binding residues, the allosteric N-helix, and the specific N-helix residues (E17, R24) known to tune arginine affinity. In contrast, it shares only ~33% identity with the arginine-insensitive, dimeric *E. coli* enzyme. The *P. putida* enzyme is regulated **solely** by arginine feedback — unlike phototrophic NAGKs, it lacks the PII nitrogen-signalling regulatory interaction, consistent with a position-233 glycine rather than the PII-interacting arginine.

---

## Key Findings

### Finding 1 — *argB* encodes N-acetyl-L-glutamate kinase, the second committed step of arginine biosynthesis

UniProt P59300 annotates the protein as **Acetylglutamate kinase (NAGK), EC 2.7.2.8**, gene *argB*, ordered locus PP_5289, in *P. putida* KT2440. NAGK catalyzes the ATP-dependent phosphorylation of the γ-carboxyl of N-acetyl-L-glutamate (NAG) to N-acetyl-L-glutamyl-5-phosphate — the second of the eight steps converting glutamate to arginine. The reaction and family identity were established directly by transition-state crystallography: *"N-Acetyl-L-glutamate kinase (NAGK), the structural paradigm of the enzymes of the amino acid kinase family, catalyzes the phosphorylation of the gamma-COO(-) group of N-acetyl-L-glutamate (NAG) by ATP"* ([PMID: 12875848](https://pubmed.ncbi.nlm.nih.gov/12875848/)).

The same crystallographic work resolved the phosphoryl-transfer chemistry: the transfer *"occurs in line and is strongly associative, with Lys8 and Lys217 stabilizing the transition state and the leaving group, respectively"* ([PMID: 12875848](https://pubmed.ncbi.nlm.nih.gov/12875848/)). This defines a precise catalytic mechanism rather than a generic "kinase activity," and pinpoints the active-site residues responsible.

### Finding 2 — *Pseudomonas* NAGK is a hexameric, arginine-feedback-inhibited enzyme and the rate-limiting control point of arginine biosynthesis

In *P. aeruginosa* — the closest well-characterized homolog of *P. putida argB* — NAGK is not merely one of eight enzymes but the **pathway-controlling, rate-limiting valve**. As stated directly: *"In Pseudomonas aeruginosa, but not in Escherichia coli, this step is rate limiting and feedback and sigmoidally inhibited by arginine"* ([PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/)). The sigmoidal (cooperative) response is the hallmark of an allosteric regulatory enzyme tuned to switch output sharply around a threshold arginine concentration.

The structural basis of this regulation was solved by crystallography of two arginine-inhibitable hexameric NAGKs. Both *"are highly similar ring-like hexamers having a central orifice of approximately 30 A diameter. They are formed by linking three E.coli NAGK-like homodimers through the interlacing of an N-terminal mobile kinked alpha-helix, which is absent from E.coli NAGK"* ([PMID: 16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/)). The allosteric mechanism itself was defined: *"Arginine, by gluing the C lobe of each subunit to the inter-dimeric junction, may stabilize an enlarged active centre conformation, hampering catalysis. Acetylglutamate counters arginine inhibition by promoting active centre closure"* ([PMID: 16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/)).

The functional role of the N-helix was proven by mutagenesis: deletion of 26 N-terminal residues abolished arginine inhibition and dissociated the hexamer into active dimers ([PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/)). The arginine-insensitive *E. coli* NAGK, lacking the N-helix, is a simple homodimer — establishing that the hexameric architecture and the N-helix are mechanistically inseparable from arginine feedback control.

### Finding 3 — NAGK adopts the amino-acid-kinase (AAK) fold with mutagenesis-defined catalytic and substrate-recognition residues

NAGK is the **structural paradigm** of the AAK family, which also encompasses carbamate kinase, UMP kinase, glutamate-5-kinase, and aspartokinase ([PMID: 12869195](https://pubmed.ncbi.nlm.nih.gov/12869195/); [PMID: 20386738](https://pubmed.ncbi.nlm.nih.gov/20386738/)). Site-directed mutagenesis of the *E. coli* enzyme confirmed structure-based predictions about which residues do what: *"The mutations K8R and D162E decreased V([sustrate]= infinity ) 100-fold and 1000-fold, respectively, in agreement with the predictions that K8 catalyzes phosphoryl transfer and D162 organizes the catalytic groups. R66K and N158Q increased selectively K(m)(Asp) three to four orders of magnitude, in agreement with the binding of R66 and N158 to the C(alpha) substituents of NAG"* ([PMID: 14623187](https://pubmed.ncbi.nlm.nih.gov/14623187/)).

This is a clean separation of function: **K8** and **D162** are catalytic (drop in Vmax when mutated), whereas **R66** and **N158** are substrate-recognition residues (rise in Km for the acetylglutamate substrate). The enzyme uses **MgATP** as the phosphoryl donor, and both substrates protect it against thermal denaturation: *"The substrates MgATP and N-acetyl-L-glutamate efficiently protect the enzyme against temperature denaturation"* ([PMID: 8394836](https://pubmed.ncbi.nlm.nih.gov/8394836/)), which independently confirms the two-substrate identity and shared MgATP-binding motifs across bacterial and yeast NAGKs.

### Finding 4 — *P. putida* NAGK is 92% identical to the characterized *P. aeruginosa* enzyme, with the allosteric N-helix conserved

A global Needleman-Wunsch alignment of P59300 (301 aa) against the experimentally characterized *P. aeruginosa* PAO1 NAGK (UniProt Q9HTN2, ARGB_PSEAE, 301 aa) gives **92.1% sequence identity**. Against the arginine-insensitive dimeric *E. coli* NAGK (P0A6C8, 258 aa), identity drops to only **32.9%**. Critically, P59300 possesses the N-terminal extension/kinked helix (N-helix) absent from *E. coli* NAGK, and conserves the exact residues **E17** and **R24** that tune the apparent affinity for the arginine feedback inhibitor.

| Enzyme | UniProt | Length (aa) | % identity to P59300 | N-helix present? | Quaternary form |
|--------|---------|-------------|----------------------|------------------|-----------------|
| *P. putida* NAGK (target) | P59300 | 301 | — | Yes | Predicted hexamer |
| *P. aeruginosa* NAGK | Q9HTN2 | 301 | **92.1%** | Yes | Hexamer (arginine-inhibited) |
| *E. coli* NAGK | P0A6C8 | 258 | 32.9% | No | Dimer (arginine-insensitive) |

The N-terminal alignment illustrates the near-identity to the *Pseudomonas* enzyme and the divergence from *E. coli*:

```
P59300 (P. putida)     MTLDRDAASHVAEVLSEALPYIRRFVGKTLVIKYGGNAME
Q9HTN2 (P. aeruginosa) MTLSRDDAAQVAKVLSEALPYIRRFVGKTLVIKYGGNAME
P0A6C8 (E. coli)       MMNPLIIKLGGVLLDSEEALERLF...   (lacks N-helix)
```

The functional relevance of E17/R24 is established: *"N-helix mutations affecting R24 and E17 increased and decreased, respectively, the apparent affinity of PaNAGK for arginine, as predicted from enzyme structures that revealed the respective formation by these residues of bonds favoring inaccessible and accessible arginine site conformations"* ([PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/)). Because both residues, plus the N-helix that distinguishes hexameric arginine-inhibitable NAGKs from the *E. coli* dimer ([PMID: 16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/)), are conserved in P59300, the *P. putida* enzyme is confidently assigned as an arginine-feedback-regulated hexamer.

### Finding 5 — NAGK acts in the cytoplasm, at step 2 of 4 of the acetylated (cyclic) ornithine branch

Curated UniProt annotations (HAMAP-Rule MF_00082) give: **FUNCTION** — "Catalyzes the ATP-dependent phosphorylation of N-acetyl-L-glutamate"; **CATALYTIC ACTIVITY** — "N-acetyl-L-glutamate + ATP = N-acetyl-L-glutamyl 5-phosphate + ADP" (EC 2.7.2.8); **PATHWAY** — "Amino-acid biosynthesis; L-arginine biosynthesis; N(2)-acetyl-L-ornithine from L-glutamate: step 2/4"; **SUBCELLULAR LOCATION** — "Cytoplasm." That NAGK is the second step is confirmed independently: *"N-Acetylglutamate kinase (NAGK) catalyses the second step in the route of arginine biosynthesis"* ([PMID: 16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/)).

The four-step acetylated sub-pathway from L-glutamate to N2-acetyl-L-ornithine proceeds:

```
                 ArgA (NAGS)         ArgB (NAGK)          ArgC              ArgD
  L-glutamate ──────────────▶ N-acetyl- ───────────▶ N-acetyl-  ──────▶ N-acetyl-  ──────▶ N2-acetyl-
                acetyl-CoA     L-glutamate    ATP     glutamyl-5-  NADPH  glutamate-5-  Glu  L-ornithine
                                             (STEP 2)  phosphate         semialdehyde
                                          [rate-limiting,
                                           Arg-inhibited]
```

In *Pseudomonas* the acetyl group is subsequently recycled from N-acetylornithine back to glutamate by **ornithine acetyltransferase (ArgJ)** — the economical "cyclic" pathway — rather than being hydrolyzed and lost. This makes NAGK the entry-gate kinase of a cyclically conserved acetyl-carrier route.

### Finding 6 — Catalytic and substrate-binding machinery is fully conserved in the *P. putida* enzyme

Mapping the experimentally validated NAGK catalytic residues onto the P59300 sequence shows complete conservation:

| Function | *E. coli* residue | *P. putida* (P59300) residue | Motif context |
|----------|-------------------|------------------------------|----------------|
| Phosphoryl-transfer lysine | K8 | **K33** | β1–αA catalytic loop "K33-Y-G-G" (33–36) |
| ATP-binding glycine loop | (β2–αB) | **H66-G-G-G** (66–69) | Second glycine-rich loop |
| Catalytic-group-organizing Asp | D162 | **D199** | Orients catalytic lysines |
| Transition-state / leaving-group Lys | K217 | **K255** | Stabilizes leaving group |

These residues were shown by mutagenesis and transition-state crystallography to be essential for phosphoryl transfer and NAG binding: *"The transfer occurs in line and is strongly associative, with Lys8 and Lys217 stabilizing the transition state and the leaving group, respectively"* ([PMID: 12875848](https://pubmed.ncbi.nlm.nih.gov/12875848/)) and *"the predictions that K8 catalyzes phosphoryl transfer and D162 organizes the catalytic groups"* ([PMID: 14623187](https://pubmed.ncbi.nlm.nih.gov/14623187/)). Their conservation in P59300 (as K33, D199, K255) provides direct sequence-level evidence that the *P. putida* enzyme is catalytically competent by the same mechanism.

### Finding 7 — In heterotrophic *Pseudomonas*, arginine feedback is the sole physiological regulator (no PII control)

An important distinction sets *Pseudomonas* NAGK apart from that of phototrophs. In oxygenic photosynthetic organisms (cyanobacteria, plants), NAGK is additionally controlled by the **PII nitrogen-signalling protein**, which binds NAGK and relieves arginine inhibition: *"in photosynthetic organisms NAGK is the target of the nitrogen-signalling protein PII"* ([PMID: 16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/)). This PII–NAGK system *"regulates the arginine-controlled enzyme of the cyclic ornithine pathway, N-acetyl-l-glutamate kinase (NAGK), to control arginine biosynthesis"* ([PMID: 20399792](https://pubmed.ncbi.nlm.nih.gov/20399792/)).

However, this layer of control is specific to phototrophs. *P. putida* NAGK position 233 is a **glycine**, not the PII-interacting arginine (R233) documented in *Synechococcus*, and heterotrophic proteobacteria such as *Pseudomonas* lack the PII–NAGK interaction. The only established allosteric effector of *Pseudomonas* NAGK is the pathway end-product **L-arginine**, which sigmoidally/feedback-inhibits the hexameric enzyme ([PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/); [PMID: 16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/)). This simplifies the regulatory model for the *P. putida* enzyme to a single, well-defined feedback loop.

### Finding 8 — Curated GO/database annotations independently corroborate the assignment; only an AlphaFold model exists for the *P. putida* protein

UniProt P59300 GO annotations independently support both function and localization: **C:cytoplasm (GO:0005737); F:acetylglutamate kinase activity (GO:0003991); F:ATP binding (GO:0005524); P:L-arginine biosynthetic process via ornithine (GO:0042450)**. Database cross-references (KEGG ppu:PP_5289, RefSeq WP_004575216.1, GeneID 83683097) confirm the locus. Structurally, an **AlphaFold model** is available (AlphaFoldDB P59300), but **no experimental PDB entry exists for the *P. putida* enzyme** — direct crystallographic evidence is confined to close orthologs (*P. aeruginosa* Q9HTN2, *E. coli*, *Thermotoga maritima*).

---

## Mechanistic Model / Interpretation

NAGK sits at the strategic control point of arginine biosynthesis in *P. putida*. The integrated model is as follows:

**1. The reaction.** NAGK catalyzes an in-line, associative phosphoryl transfer from MgATP to the γ-carboxylate of N-acetyl-L-glutamate, generating the acyl-phosphate N-acetyl-L-glutamyl-5-phosphate. Catalysis is executed by K33 (phosphoryl transfer) and K255 (leaving-group/transition-state stabilization), with D199 organizing the catalytic groups and R/N residues in the C-lobe reading out the Cα substituents of the acetylglutamate substrate to confer specificity.

**2. Pathway placement.** The product feeds directly into ArgC (N-acetyl-γ-glutamyl-phosphate reductase) and onward to N2-acetyl-L-ornithine (ArgD), with the acetyl group cyclically recycled by ArgJ. NAGK is thus the committed, energy-investing (ATP-consuming) gate of the acetylated ornithine route.

**3. Allosteric control.** The enzyme is a hexameric ring (three dimers bridged by the N-helix). L-arginine, the end product, binds each subunit at a site formed by the N-helix and C-lobe, "gluing" the C-lobe to the inter-dimeric junction and locking an enlarged, unproductive active centre. Substrate acetylglutamate opposes this by promoting active-centre closure. Sigmoidal kinetics amplify the response, so flux is throttled sharply once arginine accumulates.

```
                       ┌──────────────── L-arginine (end product) ────────┐
                       │  feedback inhibition (sigmoidal, allosteric)     │
                       ▼                                                   │
   Glutamate ─ArgA─▶ NAG ──[ArgB / NAGK]──▶ NAG-5-P ─ArgC─▶ ... ─▶ Ornithine ─▶ ... ─▶ ARGININE
                            (STEP 2, RATE-LIMITING)                                        │
                            hexamer, N-helix E17/R24                                       │
                            catalysis: K33, D199, K255                                     │
                       └──────────────────────────────────────────────  synthesized ──────┘
```

**4. Organism-specific tuning.** Unlike cyanobacterial/plant NAGK, the *P. putida* enzyme is *not* modulated by PII (position 233 = Gly). Arginine feedback is the exclusive allosteric input, making this a clean single-loop regulatory device.

**5. Confidence of transfer to *P. putida*.** Because P59300 is 92% identical to the biochemically and structurally dissected *P. aeruginosa* enzyme, conserves every catalytic and substrate-binding residue, retains the N-helix, and preserves the specific arginine-affinity-tuning residues E17/R24, the mechanistic model derived from *P. aeruginosa* transfers to *P. putida* with high confidence, even in the absence of a *P. putida* crystal structure.

---

## Evidence Base

| PMID | Study (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [12875848](https://pubmed.ncbi.nlm.nih.gov/12875848/) | Course of phosphorus in NAGK reaction; AlF4- transition-state mimic | Defines the exact reaction (γ-carboxyl phosphorylation of NAG by ATP), in-line associative mechanism, and catalytic lysines K8/K217. |
| [16376937](https://pubmed.ncbi.nlm.nih.gov/16376937/) | Hexameric NAGKs from *T. maritima* and *P. aeruginosa* | Establishes hexameric ring architecture, the N-helix, the arginine allosteric mechanism, second-step pathway placement, and PII specificity to phototrophs. |
| [18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/) | Basis of arginine sensitivity: mutagenesis of *P. aeruginosa* & *E. coli* NAGK | Shows NAGK is rate-limiting and sigmoidally arginine-inhibited in *Pseudomonas*; identifies N-helix residues E17/R24 tuning arginine affinity; N-helix deletion abolishes inhibition. |
| [14623187](https://pubmed.ncbi.nlm.nih.gov/14623187/) | Site-directed mutagenesis of *E. coli* NAGK and aspartokinase III | Separates catalytic (K8, D162) from substrate-binding (R66, N158) residues; anchors residue-mapping onto P59300. |
| [8394836](https://pubmed.ncbi.nlm.nih.gov/8394836/) | NAGK of *B. stearothermophilus*: gene sequence & characterization | Confirms the two substrates (MgATP, N-acetyl-L-glutamate) and conserved MgATP-binding motifs across bacteria/yeast. |
| [20386738](https://pubmed.ncbi.nlm.nih.gov/20386738/) | Conservation of slow dynamics in the AAK family: NAGK paradigm | Establishes NAGK as the structural/dynamic paradigm of the AAK family; substrate-binding dynamics conserved. |
| [12869195](https://pubmed.ncbi.nlm.nih.gov/12869195/) | UMP kinase of *B. subtilis* | Places NAGK within the AAK family sharing the carbamate-kinase/NAGK fold. |
| [20399792](https://pubmed.ncbi.nlm.nih.gov/20399792/) | PII variant from *Synechococcus* / NAGK–PII complex | Documents the phototroph-specific PII–NAGK regulatory system absent in heterotrophic *Pseudomonas*. |
| [21980279](https://pubmed.ncbi.nlm.nih.gov/21980279/) | Dynamics upon oligomerization in the AAK family | Explains how hexamerization confers cooperative arginine inhibition. |
| [28341883](https://pubmed.ncbi.nlm.nih.gov/28341883/) | Conformational dynamics of NAGK | Reviews the essential role of conformational mobility in NAGK catalysis and allostery. |
| [12037312](https://pubmed.ncbi.nlm.nih.gov/12037312/) | Cloning/crystallization of arginine-inhibited *P. aeruginosa* NAGK | Documents the arginine-inhibitable *P. aeruginosa* NAGK as the best-characterized reference enzyme. |
| [23806148](https://pubmed.ncbi.nlm.nih.gov/23806148/) | Proline production in *C. glutamicum* | Applied confirmation that feedback-alleviated NAGK increases flux through the acetylated glutamate route (uses *P. putida* pathway genes). |

**Consistency of the evidence.** Every independent line — the curated UniProt/HAMAP annotation, the GO annotations, the KEGG/RefSeq cross-references, the crystallographic and mutagenesis literature on orthologs, and the direct sequence alignment — converges on the same conclusion. No contradictory literature or gene-symbol ambiguity was encountered. The *argB* symbol, the EC number 2.7.2.8, the ArgB/AAK domain architecture (IPR037528, IPR004662, IPR001048, IPR001057, IPR036393), and the organism all align cleanly.

---

## Limitations and Knowledge Gaps

1. **No experimental structure or enzymology for the *P. putida* protein itself.** All direct mechanistic and structural evidence derives from orthologs, chiefly *P. aeruginosa* (92% identical) and *E. coli* (33% identical). Only an AlphaFold model exists for P59300. The functional assignment is therefore inference-by-homology — albeit at a very high (92%) identity that makes the inference robust.

2. **Hexameric state predicted, not directly demonstrated for *P. putida*.** Oligomeric state and arginine inhibition are inferred from N-helix conservation and *P. aeruginosa* data, not measured for the KT2440 enzyme.

3. **Kinetic parameters (Km for NAG and ATP, Ki for arginine, Hill coefficient) have not been measured for the *P. putida* enzyme.** Values are expected to resemble the *P. aeruginosa* enzyme but remain to be confirmed.

4. **Physiological/regulatory context in KT2440 in vivo** — e.g., transcriptional control of *argB*, its operon organization, and integration with nitrogen/carbon status — was not investigated here and lies outside the strict "primary function" scope.

5. **Absence of PII regulation is inferred** from the position-233 glycine and the general biology of heterotrophic proteobacteria; it has not been experimentally excluded for *P. putida* specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymology.** Overexpress His-tagged P59300 in *E. coli*, purify, and determine steady-state kinetics (Km for NAG and MgATP, Vmax) and arginine inhibition (Ki, Hill coefficient) to confirm the predicted sigmoidal feedback.

2. **Oligomeric-state determination.** Use size-exclusion chromatography–MALS or analytical ultracentrifugation to test the predicted hexamer, and cryo-EM or crystallography to obtain the first experimental *P. putida* structure (with/without arginine).

3. **N-helix / arginine-site mutagenesis.** Mutate the conserved E17 and R24 (and delete the N-helix) in P59300 to test whether they tune arginine affinity as in *P. aeruginosa*, validating transfer of the allosteric model.

4. **Active-site validation.** Mutate the mapped catalytic residues (K33, D199, K255) and confirm the predicted losses in Vmax, verifying the conserved catalytic machinery.

5. **Test for PII interaction.** Perform pull-down/ITC assays between P59300 and the *P. putida* PII protein (GlnB/GlnK) to experimentally confirm the absence of PII regulation predicted from the position-233 glycine.

6. **Physiological genetics.** Construct a KT2440 *argB* conditional/deletion mutant to confirm arginine auxotrophy, and use a feedback-alleviated NAGK variant to probe control of flux through the cyclic ornithine pathway — of direct interest for metabolic engineering (cf. arginine/ornithine/proline/polyamine production).

---

*Report compiled from 5 completed investigation iterations, 8 confirmed findings, and 16 reviewed publications. Gene identity verified: no ambiguity found — argB / PP_5289 / P59300 is unambiguously N-acetyl-L-glutamate kinase (EC 2.7.2.8) of the ArgB / amino-acid-kinase family in P. putida KT2440.*


## Artifacts

- [OpenScientist final report](argB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12875848
2. PMID:18263723
3. PMID:16376937
4. PMID:12869195
5. PMID:20386738
6. PMID:14623187
7. PMID:8394836
8. PMID:20399792