# DREB2A (At5g05410, UniProt O82132) — Gene Review Notes

Arabidopsis thaliana DEHYDRATION-RESPONSIVE ELEMENT-BINDING PROTEIN 2A.
AP2/ERF-family transcription factor. ORF/locus AT5G05410; synonym ERF045.

## Summary of biology

DREB2A is a sequence-specific DNA-binding transcription factor of the AP2/ERF
superfamily (ERF/DREB subfamily) that binds the dehydration-responsive
element / C-repeat (DRE/CRT) cis-element, core motif A/GCCGAC, in target gene
promoters and activates their transcription. It is a master regulator of the
ABA-independent branch of drought-, high-salinity- and heat-stress-responsive
gene expression in Arabidopsis. A central negative regulatory domain (NRD; the
~30 aa region between residues 136-165, containing a PEST sequence) targets the
protein for ubiquitin-mediated degradation by the RING E3 ligases DRIP1/DRIP2
and the 26S proteasome; deletion of this region produces a constitutively active
form (DREB2A-CA) that confers drought and heat tolerance. Under heat stress
DREB2A is stabilized and induces the heat-stress regulatory cascade, including
the heat-shock transcription factor gene HsfA3.

## DNA binding / TF activity / nucleus (core functions)

- DREB2A binds the DRE sequence in vitro and activates DRE-driven reporter
  transcription in Arabidopsis protoplasts. [PMID:9707537 "Both the DREB1A and DREB2A proteins specifically bound to the DRE sequence in vitro and activated the transcription of the b-glucuronidase reporter gene driven by the DRE sequence in Arabidopsis leaf protoplasts."]
- Core binding motif A/GCCGAC; DREB2A prefers ACCGAC and can also recognize
  A/GCCGACNA/G/C. [PMID:16617101 "We found that the DREB2A protein could recognize not only A/GCCGACNT, but also A/GCCGACNA/G/C, and prefers ACCGAC to GCCGAC."]
- AP2/ERF DNA-binding domain (UniProt FT DNA_BIND 78..135); mutagenesis of
  V91 and E96 affects CRT/DRE binding. [file:ARATH/DREB2A/DREB2A-uniprot.txt "MUTAGEN 91 ... V->A: Affects the binding to the CRT/DRE cis-element."]
- Nuclear localization: GFP-DREB2A localizes to the nucleus; the protein
  carries an N-terminal NLS. [PMID:16617101 "Synthetic green fluorescent protein gave a strong signal in the nucleus under unstressed control conditions when fused to constitutive active DREB2A but only a weak signal when fused to full-length DREB2A."]
  IDA nuclear localization also reported by PMID:18552202 and PMID:25490919.
- Transcriptional activation domain maps to the acidic C-terminus (residues
  254-335). [PMID:16617101 "DREB2A domain analysis using Arabidopsis protoplasts identified a transcriptional activation domain between residues 254 and 335"]

## Drought / water deprivation / osmotic stress

- DREB2A (and DREB2B) genes are induced by dehydration and high-salt stress.
  [PMID:10809011 "Northern analysis showed that both genes are induced by dehydration and high-salt stress."]
- DREB2A-CA overexpression confers drought tolerance and upregulates many water
  stress-inducible genes. [PMID:16617101 "Overexpression of constitutive active DREB2A resulted in significant drought stress tolerance but only slight freezing tolerance in transgenic Arabidopsis plants."]
- IMP annotation to "response to water deprivation" via dreb2a phenotype.
  [PMID:17030801 "DREB2A up-regulated genes were down-regulated in DREB2A knockout mutants under stress conditions."]

## Heat stress / heat acclimation

- DREB2A has dual function in water- and heat-stress responses; DREB2A-CA
  overexpression induces heat-shock-related genes including AtHsfA3 and HSPs,
  and increases thermotolerance; dreb2a knockouts have reduced thermotolerance.
  [PMID:17030801 "Thermotolerance was significantly increased in plants overexpressing DREB2A CA and decreased in DREB2A knockout plants. Collectively, these results indicate that DREB2A functions in both water and HS-stress responses."]
- DREB2A controls HsfA3 as a downstream gene in the heat-stress regulatory
  network. [PMID:17030801 "DREB2A controls HSF as one of the downstream genes."]
- DREB2A is stabilized in the nucleus under heat stress. [PMID:17030801 "These data indicate that the DREB2A protein is stabilized by HS stress and nuclear-localized during stress conditions."]
- Heat-stress-specific positive regulation (IDA, response to heat + positive
  regulation of transcription) via the DPB3-1/NF-YA2/NF-YB3 trimer that enhances
  DREB2A transactivation of HsfA3. [PMID:25490919 "The identified trimer comprising NF-YA2, NF-YB3, and DPB3-1 enhanced HsfA3 promoter transactivation by DREB2A"]
- Heat-acclimation expression study (transcript-level only): DREB2-subfamily
  genes induced under heat stress in suspension cultures — this is an
  expression/cross-talk observation, not a DREB2A-function knockout assay.
  [PMID:16807682 "the transcriptional induction of DREB2 (dehydration responsive element-binding factor 2) subfamily genes and COR47/rd17 under heat stress suggested cross-talk between the signaling pathways for heat and dehydration responses."]

## Post-translational regulation / degradation (DRIP1/DRIP2)

- Central NRD (residues ~136-165) contains a PEST sequence; full-length DREB2A
  is unstable and degraded by the 26S proteasome; deletion gives DREB2A-CA.
  [PMID:16617101 "The DREB2A FL protein containing the PEST sequence may be degraded rapidly by the ubiquitin-proteasome system, whereas DREB2A CA may have a long lifetime in the nucleus."]
- DRIP1 and DRIP2 are C3HC4 RING-domain E3 ubiquitin ligases that interact with
  DREB2A in the nucleus and mediate its ubiquitination and proteasomal
  degradation, negatively regulating drought-responsive gene expression.
  [PMID:18552202 "DRIP1 and DRIP2 act as novel negative regulators in drought-responsive gene expression by targeting DREB2A to 26S proteasome proteolysis."]
- The DRIP1 interaction underpins the GO:0005515 IPI (WITH UniProtKB:Q9M9Y4 =
  DRIP1, and Q94AY3 = DRIP2). [file:ARATH/DREB2A/DREB2A-goa.tsv "PMID:18552202\tUniProtKB:Q9M9Y4"]

## Protein-protein interactions (GO:0005515 IPI annotations)

These are real, experimentally supported interactions but "protein binding"
(GO:0005515) is uninformative as a molecular function. Underlying interactors:
- DRIP1 (Q9M9Y4) / DRIP2 (Q94AY3) — RING E3 ligases. [PMID:18552202]
- RCD1 (Q8RY59) — Radical-induced Cell Death1; SLiM-mediated binding to the
  RCD1 RST domain. [PMID:27881680] and [PMID:19548978 RCD1/SRO1].
- MED25 (Q7XYY2 / Q7XYY2-1) — Mediator subunit; interaction reported, with NMR
  structural data on a DREB2A peptide (PDB 5OAP, residues 255-272). [PMID:21536906], [PMID:22447446]
- DPB3-1 / NF-YC10 (Q9LN09) — heat-stress coactivator. [PMID:25490919]
- DOG1 (A0SVK0) and IMPA6 (Q9FWY7) — large-scale interactome. [PMID:32612234]

UniProt INTERACTION block confirms DOG1, DRIP1, IMPA6, MED25, RCD1.
[file:ARATH/DREB2A/DREB2A-uniprot.txt "O82132; Q9M9Y4: DRIP1; NbExp=4"]

## Target-promoter binding annotations (GO:0000976, IPI, WITH AGI loci)

Multiple TAIR annotations to "transcription cis-regulatory region binding"
(GO:0000976) with WITH-field AGI loci come from large yeast-one-hybrid /
gene-regulatory-network screens (enhanced Y1H, secondary cell wall network,
nitrogen network, PXY/vascular network, PRC2 regulation, plant-defense network).
These document DREB2A binding to specific target promoters and support the
sequence-specific DNA-binding TF function, although several of the networks
(secondary cell wall, vascular development, nitrogen metabolism, PRC2) are
contexts where DREB2A is a node in a large Y1H matrix rather than an established
in planta regulator. [PMID:22037706 Enhanced Y1H], [PMID:25533953 secondary cell wall GRN], [PMID:31806676 PXY vascular network], [PMID:30356219 nitrogen network], [PMID:27650334 PRC2], [PMID:25352272 plant-defense promoter integration].

## Weaker / expression-readout annotations (candidates for non-core or over-annotation)

- response to UV-B (GO:0010224): DREB2A (At5g05410) appears as a UV-B-*induced*
  transcript whose induction depends on HY5; it is a downstream readout, not an
  effector demonstrated to act in the UV-B response.
  [PMID:14739338 "we found that loss of HY5 impairs the UV-B-responsive expression of several genes, including ... At5g05410 ( DREB2A )"]
  PMID:18266923 is about a novel UV-B cis-element (UVBox) on ANAC13 and does not
  establish a DREB2A UV-B function; its abstract does not mention DREB2A.
  [PMID:18266923 "two cis-regulatory elements, designated MRE(ANAC13) and UVBox(ANAC13), are required for maximal UV-B induction of the ANAC13 gene"]
- response to hydrogen peroxide (GO:0042542, IEP, PMID:17030801): the cited
  paper is the dual drought/heat function paper; H2O2 response is not its focus.
  Treat as non-core expression-association.
- cellular response to hypoxia (GO:0071456, HEP, PMID:31519798): high-throughput
  expression/epigenome study; DREB2A/heat-stress transcripts are progressively
  upregulated during hypoxia. HEP = inferred from high-throughput expression
  pattern; a transcript-level association, non-core.
  [PMID:31519798 "Hypoxia promoted a progressive upregulation of heat stress transcripts"]
- heat acclimation (GO:0010286, IEP, PMID:16807682): transcript induction in
  suspension cultures; expression-based, non-core (but biologically consistent
  with the heat role).

## Provenance / IEA backbone annotations

- GO:0003677 DNA binding (IEA, InterPro IPR016177) — correct, subsumed by the
  experimental DNA-binding TF activity.
- GO:0003700 DNA-binding transcription factor activity (IEA InterPro;
  IDA PMID:9707537; ISS PMID:11118137) — core, experimentally supported.
- GO:0005634 nucleus (IEA SubCell; ISM AtSubP; IDA PMID:16617101/18552202/25490919/21443605)
  — core, multiple IDA.
- GO:0006355 regulation of DNA-templated transcription (IEA InterPro) — correct
  but general; the experimental data support positive regulation specifically.

## Conclusions for review actions

Core: GO:0003700 (DNA-binding TF activity), GO:0000976 (DRE/CRT cis-regulatory
region binding), GO:0005634 (nucleus), GO:0045893 (positive regulation of
transcription), GO:0009414 (response to water deprivation), GO:0009408 (response
to heat). DNA binding (GO:0003677) and regulation of transcription (GO:0006355)
are accepted as correct but general/non-core electronic backbone.
The eight GO:0005515 "protein binding" IPI annotations are real interactions but
uninformative as MF; mark over-annotated (do not endorse as core).
UV-B, H2O2, hypoxia, heat-acclimation are expression-readout associations →
keep as non-core.

---

## Earlier notes carried over from the retired AT5G05410 folder

These notes were written for the duplicate `genes/ARATH/AT5G05410` review of the same protein (O82132), which was merged into this folder. Claims tagged `[deep-research]` come from AI deep-research summaries, not from primary papers, and have not been re-verified against the literature.


### Gene Summary
**DREB2A** = Dehydration-Responsive Element Binding Protein 2A
**CRITICAL INTEGRATOR**: Drought AND Heat stress responses through distinct pathways [deep-research]

### UNIQUE FUNCTION - Cross-Stress Integrator

**DREB2A coordinates BOTH drought and heat stress responses through stress-specific transcriptional programs** [deep-research]

#### Mechanism:
- **Drought stress**: Activates LEA proteins, osmoprotective genes (osmotic adjustment) [deep-research]
- **Heat stress**: Activates HSFA3 → heat shock proteins (protein protection) [deep-research]
- **Same transcription factor, different outputs** depending on stress context [deep-research]
- Stress-specific cofactors (e.g., DPB3-1/NF-YC enhances heat targets only) [deep-research]

### Primary Function

#### Sequence-Specific Transcription Factor (CORE)
- **AP2/ERF family**: Conserved ERF/AP2 DNA-binding domain (aa 68-133) [deep-research]
- **DNA recognition**: Binds DRE (Dehydration-Responsive Element) sequences [deep-research]
- **Sequence preference**: ACCGAC (vs DREB1A preferring A/GCCGACNT) [deep-research]
- **Transcriptional activator**: C-terminal activation domain (aa 254-335) [deep-research]

#### Domain Architecture:
- **N-terminal**: Nuclear localization signals (NLS1, NLS2) [deep-research]
- **Central**: ERF/AP2 DNA-binding domain (aa 68-133) [deep-research]
- **Negative Regulatory Domain (NRD)**: aa 136-165, CRITICAL for regulation [deep-research]
- **C-terminal**: Transcriptional activation domain (acidic residues) [deep-research]
- **PEST sequence**: Phosphorylation target sites [deep-research]

### POST-TRANSLATIONAL REGULATION (CRITICAL MECHANISM)

#### Constitutive Degradation Under Normal Conditions:

**Paradox**: DREB2A mRNA is constitutively expressed, but protein is RAPIDLY degraded [deep-research]

##### DRIP1/DRIP2-Mediated Degradation:
- **DRIP1, DRIP2**: C3HC4 RING E3 ubiquitin ligases [deep-research]
- **Nuclear localization**: Interact with DREB2A in nucleus [deep-research]
- **Ubiquitination**: DRIP1/DRIP2 + E2 (UBCH5c) → polyubiquitination [deep-research]
- **26S proteasome**: Degrades ubiquitinated DREB2A [deep-research]
- **drip1 drip2 double mutants**: DREB2A accumulates, enhanced drought tolerance [deep-research]

#### Stress-Induced Stabilization:

##### Casein Kinase 1 (CK1)-Mediated Phosphorylation:
- **Normal conditions**: CK1 phosphorylates NRD (Ser/Thr residues) → degradation signal [deep-research]
- **Heat stress (40°C)**: NRD becomes DEPHOSPHORYLATED → blocks ubiquitination [deep-research]
- **Temperature sensor**: Dephosphorylation at 40°C, minimal at 32°C [deep-research]
- **PF-670462 (CK1 inhibitor)**: Causes DREB2A accumulation in non-phosphorylated form [deep-research]
- **Mechanism**: NRD = temperature-sensitive conditional degradation signal [deep-research]

#### Result:
- **Rapid response capacity**: mRNA already present, protein stabilization triggers activation [deep-research]
- **Prevents inappropriate activation**: Degradation under normal conditions prevents growth retardation [deep-research]
- **Elegant thermosensor**: Phosphorylation status changes with temperature [deep-research]

### Target Genes and Transcriptional Programs

#### Microarray Analysis (DREB2A-CA overexpression):
- **36 genes >8-fold induced** [deep-research]
- **29/36 have DRE sequences** in 1000-bp upstream regions (direct targets) [deep-research]

#### Direct Target Gene Classes:

##### 1. Late Embryogenesis Abundant (LEA) Proteins (9 genes):
- **Function**: Protect proteins, enzymes, lipids from dehydration [deep-research]
- **Examples**: RD29A, RD29B, RD17, LEA14 [deep-research]
- **Drought-responsive** [deep-research]

##### 2. Heat Shock Factor A3 (HSFA3):
- **CRITICAL**: DREB2A → HSFA3 → Heat Shock Proteins cascade [deep-research]
- **Highest expression ratio** in DREB2A-CA plants [deep-research]
- **Heat-specific**: Amplifies heat stress response signal [deep-research]
- **Hierarchical regulation**: Master regulator (DREB2A) → Amplifier (HSFA3) → Effectors (HSPs) [deep-research]

##### 3. Osmoprotective Genes:
- **Galactinol synthase (GolS)**: Raffinose family oligosaccharide synthesis [deep-research]
- **Function**: Osmoprotectants, maintain turgor, protect macromolecules [deep-research]

##### 4. Stress-Responsive Genes:
- **COR15A, KIN1, KIN2, COR15B**: Osmotic stress tolerance [deep-research]

#### Stress-Dependent Target Selectivity:
- **Drought stress**: Preferentially induces LEA proteins, osmolyte genes [deep-research]
- **Heat stress**: Preferentially induces HSPs, heat shock factors [deep-research]
- **Both stresses**: Third group induced by both [deep-research]
- **NOT simple on-off switch**: Stress-dependent transcriptional programs [deep-research]

### Upstream Regulation

#### Transcriptional Induction:

##### Heat Stress Pathway:
- **Heat Shock Elements (HSE)** in DREB2A promoter [deep-research]
- **HSFA1a, HSFA1b, HSFA1d**: Essential positive regulators [deep-research]
- **hsfa1a/b/d triple mutant**: Complete suppression of heat-induced DREB2A [deep-research]
- **HsfA1b rescue**: Restores DREB2A expression [deep-research]

##### Osmotic Stress Pathway:
- **ABRE (ABA-responsive element)** in DREB2A promoter [deep-research]
- **CE3-like sequence** (coupling element 3) [deep-research]
- **AREB/ABF transcription factors**: Activate through ABRE [deep-research]
- **Up to 250-fold induction** under dehydration [deep-research]

#### Transcriptional Repression:

##### GRF7 (Growth-Regulating Factor 7):
- **Binds DREB2A promoter** at "Region S" (GTE element: TGTCAGG) [deep-research]
- **Negative regulator** under normal conditions [deep-research]
- **grf7 mutants**: Elevated DREB2A expression basally [deep-research]
- **Function**: Balance growth vs stress preparedness (growth-promoting) [deep-research]

##### Phosphoinositide-Specific Phospholipase C (PI-PLC):
- **Constitutive repression** of DREB2A under normal conditions [deep-research]
- **PI-PLC inhibition**: Rapid DREB2A upregulation [deep-research]
- **Lipid signaling**: DAG, phosphatidic acid maintain repression [deep-research]

### Alternative Splicing - Regulatory Diversity

#### DREB2A.2 Isoform:
- **Heat stress-induced** alternative splicing [deep-research]
- **Truncated protein**: Lacks CMIV-3 motif (RCD1-binding domain) [deep-research]
- **Function**: Removes RCD1-mediated inhibition during heat stress [deep-research]
- **Mechanism**: Molecular switch - RNA processing tunes DREB2A activity [deep-research]

#### Functional Significance:
- **Full-length DREB2A**: Subject to RCD1 regulation [deep-research]
- **DREB2A.2**: Liberated from RCD1 inhibition → full activation [deep-research]
- **Stress-dependent switch**: Different protein forms for different conditions [deep-research]

### Protein-Protein Interactions

#### Cofactors (Enhance Activity):

##### Nuclear Factor Y (NF-Y) Complex:
- **DPB3-1 (NF-YC subunit)**: Interacts with DREB2A [deep-research]
- **Enhanced transactivation**: Specifically for HEAT-responsive targets [deep-research]
- **Stress-specific**: DPB3-1 overexpression enhances heat targets, NOT drought targets [deep-research]
- **Mechanism**: Cofactor-dependent target selectivity [deep-research]

#### Negative Regulators:

##### RCD1 (Radical-Induced Cell Death 1):
- **Poly(ADP-ribose) polymerase (PARP) superfamily** [deep-research]
- **Modulates DREB2A function** during stress and senescence [deep-research]
- **Inhibitory interaction**: Removed by alternative splicing (DREB2A.2) [deep-research]

### Subcellular Localization

- **Nuclear** (primary site of function) [deep-research]
- **NLS1, NLS2**: Either alone sufficient for nuclear import [deep-research]
- **Weak nuclear signal** under normal conditions (rapid degradation) [deep-research]
- **Strong nuclear accumulation** during heat stress (stabilization) [deep-research]
- **Tissue-specific**: Prominent in root tips, cotyledons; absent/weak in guard cells [deep-research]
- **Nucleus-specific degradation**: DRIP1/DRIP2 interact in nucleus [deep-research]

### Functional Roles

#### 1. Drought and Salt Stress Tolerance (PRIMARY):
- **DREB2A-CA overexpression**: Significant drought tolerance improvement [deep-research]
- **dreb2a mutants**: Reduced drought tolerance, diminished target gene expression [deep-research]
- **Osmotic adjustment**: LEA proteins, osmoprotectants [deep-research]
- **Necessary and sufficient** for drought tolerance [deep-research]

#### 2. Heat Stress Tolerance (CO-PRIMARY):
- **DREB2A-CA overexpression**: Increased thermotolerance [deep-research]
- **dreb2a mutants**: Reduced basal thermotolerance [deep-research]
- **DREB2A → HSFA3 cascade**: Amplifies heat response [deep-research]
- **Unexpected discovery**: Initially identified as dehydration factor [deep-research]
- **Crosstalk**: Water and temperature stress responses integrated [deep-research]

#### 3. ABA-Independent Osmotic Stress Pathway:
- **Dual pathways**: ABA-dependent AND ABA-independent [deep-research]
- **ABRE elements**: Connect to ABA-dependent pathway [deep-research]
- **SnRK2 triple mutants**: DREB2A still induced by osmotic stress (ABA-independent) [deep-research]
- **Robust system**: Multiple parallel pathways [deep-research]

### DREB2 Family Context

#### Arabidopsis DREB2 Subfamily:
- **8 members**: DREB2A-H [deep-research]
- **Stress-inducible**: DREB2A, DREB2B (major members) [deep-research]
- **Other 6 members**: Very low/undetectable stress induction [deep-research]
- **Functional specialization**: DREB2A/B = primary stress responders [deep-research]

#### Evolutionary Conservation:
- **Crop orthologs**: Rice, wheat, barley, maize, pearl millet, soybean, chickpea, poplar [deep-research]
- **Conserved features**: NRD, post-translational regulation [deep-research]
- **GmDREB2A;2 (soybean)**: Improves drought/heat in transgenic Arabidopsis [deep-research]
- **Species-specific variations**: Fine-tuning for species-specific stress environments [deep-research]

### Biotechnological Applications

#### Challenges:
- **Growth retardation**: Constitutive DREB2A-CA overexpression retards growth [deep-research]
- **Energy cost**: Constitutive stress preparation vs normal development [deep-research]

#### Solutions:
- **Stress-inducible promoters**: RD29A promoter → enhanced tolerance, minimal growth retardation [deep-research]
- **CK1 manipulation**: Target regulatory components (CK1, DRIP1/DRIP2) [deep-research]
- **Cofactor coordination**: DPB3-1 + DREB2A for additive effects [deep-research]
- **Genome editing**: CRISPR/Cas9 for enhancer insertion, GRF7 knockout [deep-research]
- **Avoid transgenes**: Regulatory mutations via conventional breeding [deep-research]

### Curation Strategy

1. **ACCEPT** core molecular function annotations:
   - Sequence-specific DNA binding transcription factor
   - DNA-binding transcription factor activity
   - cis-regulatory region sequence-specific DNA binding
   - DRE/CRT element binding

2. **ACCEPT** biological process annotations:
   - Response to water deprivation
   - Response to salt stress
   - Response to heat
   - Response to osmotic stress
   - Cellular response to dehydration
   - Positive regulation of transcription

3. **ACCEPT** localization annotations:
   - Nucleus (primary site of function)

4. **EMPHASIZE** key features:
   - CROSS-STRESS INTEGRATOR (drought AND heat)
   - Post-translational regulation (DRIP1/DRIP2, CK1 phosphorylation)
   - DREB2A → HSFA3 → HSP cascade (hierarchical)
   - Alternative splicing (DREB2A.2 for heat stress)
   - Stress-specific cofactors (DPB3-1 for heat targets)
   - Constitutive degradation, stress-induced stabilization

5. **NOTE** important relationships:
   - Upstream: HSFA1a/b/d (heat), AREB/ABF (osmotic)
   - Downstream: HSFA3 (heat), LEA proteins (drought), HSPs
   - Negative regulators: GRF7, RCD1, DRIP1/DRIP2, PI-PLC
   - Cofactors: DPB3-1/NF-YC (heat-specific enhancement)

### Key Functional Distinctions

#### vs DREB1A:
- **DREB1A**: Cold stress, GCCGACNT preference
- **DREB2A**: Drought/heat stress, ACCGAC preference
- Different target gene sets through DNA-binding specificity

#### vs HSFA1 Family:
- **HSFA1a/b/d**: Upstream activators of DREB2A during heat
- **DREB2A**: Downstream of HSFA1, activates HSFA3
- Hierarchical relationship in heat stress network

#### vs HSFA3:
- **DREB2A**: Master regulator, activates HSFA3
- **HSFA3**: Amplifier, DREB2A-regulated
- DREB2A → HSFA3 cascade is central to heat response

### References

- Deep research: AT5G05410-deep-research-perplexity.md (37 citations)
- **Key function**: Cross-stress integrator coordinating drought AND heat responses through post-translational regulation and hierarchical transcriptional cascades

---

## 2026-09-27: merge of the AT5G05410 duplicate and GOA refresh

- The duplicate folder `genes/ARATH/AT5G05410` (same accession, O82132) was retired in favour of this one. Its perplexity report is kept here as `DREB2A-deep-research-perplexity.md`, and its notes are appended above.
- `DREB2A-goa.tsv` was refreshed from QuickGO. Seven rows were new to this review: five IBAs from PAINT nodes PTN001261703 and PTN007858567 (GO:0003700, GO:0000976, GO:0005634, GO:0045893, GO:0010286), the DisProt EXP row GO:0001221 (RCD1 binding, PMID:27881680), and an RCD1 protein-binding IPI (PMID:34473923).
- Heat acclimation (GO:0010286): the IBA row is correct, since DREB2A has its own gain- and loss-of-function thermotolerance data (PMID:17030801) and is one of the IBD seeds. It is kept non-core like the IEP row, because response to heat (GO:0009408) already carries the core heat role.
- The new RCD1 protein-binding IPI (PMID:34473923) is marked REMOVE under the GO:0005515 policy. The interaction is real and is represented by the GO:0001221 EXP row.
