---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T04:39:18.081607'
end_time: '2026-11-14T04:57:04.745856'
duration_seconds: 1066.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: OPN1SW
  gene_symbol: OPN1SW
  uniprot_accession: P03999
  protein_description: 'RecName: Full=Short-wave-sensitive opsin 1 {ECO:0000303|Ref.10};
    AltName: Full=Blue cone photoreceptor pigment; AltName: Full=Blue-sensitive opsin
    {ECO:0000303|PubMed:1531728}; Short=BOP;'
  gene_info: Name=OPN1SW {ECO:0000312|HGNC:HGNC:1012}; Synonyms=BCP;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G protein-coupled receptor 1 family. Opsin
  protein_domains: GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM.
    (IPR017452); Opsin. (IPR001760); Opsin_blue. (IPR001521)
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
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: OPN1SW-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: OPN1SW-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P03999
- **Protein Description:** RecName: Full=Short-wave-sensitive opsin 1 {ECO:0000303|Ref.10}; AltName: Full=Blue cone photoreceptor pigment; AltName: Full=Blue-sensitive opsin {ECO:0000303|PubMed:1531728}; Short=BOP;
- **Gene Information:** Name=OPN1SW {ECO:0000312|HGNC:HGNC:1012}; Synonyms=BCP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G protein-coupled receptor 1 family. Opsin
- **Key Domains:** GPCR_opsins. (IPR050125); GPCR_Rhodpsn. (IPR000276); GPCR_Rhodpsn_7TM. (IPR017452); Opsin. (IPR001760); Opsin_blue. (IPR001521)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OPN1SW" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OPN1SW' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OPN1SW** (gene ID: OPN1SW, UniProt: P03999) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# OPN1SW (P03999): The Short-Wave-Sensitive "Blue" Cone Opsin — A Functional Annotation Report

**Gene:** OPN1SW (synonym BCP) · **UniProt:** P03999 · **Organism:** *Homo sapiens* (human)
**Protein family:** G protein-coupled receptor class A (rhodopsin-like), opsin subfamily
**Key domains:** Opsin (IPR001760), Blue opsin (IPR001521), 7TM rhodopsin-like GPCR (IPR017452), GPCR_opsins (IPR050125)

## Summary

**OPN1SW encodes the short-wave-sensitive (SWS/blue) cone opsin, a class-A (rhodopsin-like) G protein-coupled receptor (GPCR) that serves as the light receptor of short-wavelength "blue" cone photoreceptors in the human retina.** Its primary molecular function is not enzymatic in the classical sense but is that of a *light-activated signal transducer*: the apoprotein (opsin) covalently binds the chromophore 11-*cis*-retinal through a protonated Schiff base to a conserved lysine in transmembrane helix 7 (Lys290 in the P03999 numbering, equivalent to Lys296 of rhodopsin). Absorption of a violet/blue photon (λmax ≈ 414–420 nm) isomerizes the retinal to all-*trans*, driving the receptor into its active Meta-II conformation. In this state OPN1SW acts as a guanine-nucleotide-exchange factor (GEF) that catalyzes GDP→GTP exchange on cone transducin (the Gα_t2 heterotrimeric G protein), thereby launching the cone phototransduction cascade.

The downstream cascade is the canonical opsin pathway: activated transducin stimulates cone phosphodiesterase (PDE6C), cGMP is hydrolyzed, cyclic-nucleotide-gated (CNG) channels close, and the S-cone hyperpolarizes. Deactivation proceeds through opsin phosphorylation/arrestin quenching of the active Meta-II state and through the RGS9–R9AP GTPase-activating protein (GAP) complex that accelerates transducin shutoff. The receptor performs this function specifically in the **outer-segment membranes of S-cones**, where immunohistochemistry localizes the protein. Functionally, OPN1SW provides the first stage of the **S-versus-(L+M), or "blue-yellow," color-opponent channel**, feeding the blue-cone (S-ON) bipolar cell → small bistratified ganglion cell circuit.

OPN1SW is **non-redundant**: loss-of-function missense mutations in the gene cause autosomal-dominant tritanopia (tritan color-vision deficiency), a progressive S-cone dystrophy — direct human-genetic proof of its unique role in S-cone signaling. This is mechanistically distinct from blue cone monochromacy (BCM), which is caused by defects in the X-linked OPN1LW/OPN1MW cluster and *spares* OPN1SW-expressing S-cones. Transcriptionally, OPN1SW expression and S-cone identity are driven by the orphan nuclear receptor RORβ acting in synergy with the cone-rod homeobox factor CRX. Recent (2026) cryo-EM structures of the three human cone opsins, each solved bound to a G protein and 11-*cis*-retinal, confirm the canonical 7-transmembrane opsin GPCR architecture inferred from sequence and genetics.

---

## Gene/Protein Identity Verification

Before research, the target identity was confirmed against the UniProt record and the primary literature. All verification checks passed:

| Check | Result |
|-------|--------|
| Gene symbol matches protein description | ✅ OPN1SW = "Short-wave-sensitive opsin 1" / Blue cone photoreceptor pigment (BOP) |
| Organism correct | ✅ *Homo sapiens* (human), chromosome 7 |
| Protein family/domains align with literature | ✅ GPCR class A / opsin subfamily; InterPro Opsin (IPR001760), Opsin_blue (IPR001521), GPCR_Rhodpsn_7TM (IPR017452) |
| Literature is for the correct gene | ✅ Primary human-genetic, structural, and physiological literature all concern the blue/S-cone opsin |

The gene symbol is **unambiguous** and well-supported by a deep primary literature. No conflicting gene with the same symbol confounded the research. One important clarification uncovered during the investigation: much of the "blue cone" clinical literature concerns **blue cone monochromacy (BCM)**, which despite its name is caused by OPN1LW/OPN1MW and *not* OPN1SW — a distinction carefully maintained throughout this report.

---

## Key Findings

### Finding 1 — OPN1SW encodes the blue/short-wave-sensitive cone opsin, a light-activated GPCR of S-cone photoreceptors

The product of OPN1SW is a canonical class-A (rhodopsin-like) G protein-coupled receptor belonging to the opsin subfamily. UniProt P03999 names it "Short-wave-sensitive opsin 1," with alternative names "Blue cone photoreceptor pigment" and "Blue-sensitive opsin (BOP)." Domain analysis places it firmly in the opsin subfamily, with InterPro signatures Opsin (IPR001760), Opsin_blue (IPR001521), and the seven-transmembrane rhodopsin GPCR fold (IPR017452). The decisive experimental confirmation came in 2026, when cryo-electron microscopy structures of all three human cone opsins — including the SWS/blue opsin — were solved, each captured bound to a G protein and the 11-*cis*-retinal chromophore, demonstrating that OPN1SW is a bona fide 7-TM opsin GPCR that couples to transducin.

> *"Human trichromatic color vision relies on three cone opsins [long-, middle-, and short-wavelength-sensitive opsins (LWS-, MWS-, and SWS-opsins, respectively)]"* — [PMID: 42348690](https://pubmed.ncbi.nlm.nih.gov/42348690/)

This finding establishes the **fundamental molecular identity**: OPN1SW is one of the three cone pigments mediating human trichromatic color vision, and the SWS-opsin specifically is the blue pigment.

### Finding 2 — OPN1SW signals through the cone phototransduction cascade and feeds the blue-yellow color-opponent pathway

Mechanistically, light-activated SWS-opsin catalyzes GDP→GTP exchange on cone transducin — the first amplifying step of phototransduction. Active transducin stimulates cone PDE6, lowering intracellular cGMP, which closes CNG channels and hyperpolarizes the S-cone. The 2026 cryo-EM structure showing SWS-opsin in complex with a G protein provides direct structural support for this transducin-coupling step.

Downstream of the photoreceptor, the S-cone signal is routed through a remarkably segregated circuit. The central elements of synaptic triads in the relevant retinal region arise almost exclusively from the "blue-cone" (S-ON) bipolar cell, which is presynaptic to the small bistratified "blue-ON" ganglion cell. The S-versus-(L+M), or "blue-yellow," opponency is first established in the S-cone itself and completed at the ganglion-cell level.

> *"central elements of synaptic triads arise almost exclusively from the 'blue-cone' bipolar cell"* — [PMID: 23895762](https://pubmed.ncbi.nlm.nih.gov/23895762/)

> *"S versus L + M or 'blue-yellow' opponency is first established in the S-cone"* — [PMID: 23895762](https://pubmed.ncbi.nlm.nih.gov/23895762/)

This places OPN1SW-expressing S-cones at the **origin of the blue-yellow color-opponent computation**, one of the two cardinal chromatic axes of human vision.

### Finding 3 — OPN1SW mutations cause tritan color-vision deficiency; blue cone monochromacy is instead caused by OPN1LW/OPN1MW

Reviews of inherited cone disease state that disruptions in the cone opsin gene array cause a spectrum of disorders including blue cone monochromacy, Bornholm eye disease, and tritan color-vision deficiency. Crucially, the gene responsible differs by disorder. OPN1SW (chromosome 7) defects specifically impair S-cone function, producing **tritanopia/tritan defect**. In contrast, **blue cone monochromacy** results from mutations or deletions in the X-linked OPN1LW/OPN1MW cluster, in which the S-cones (OPN1SW) are structurally and functionally *preserved*. Adaptive-optics imaging of BCM patients found S-cone waveguiding density of 2073 ± 963 cones/mm² (n = 9), consistent with normal histological estimates — confirming S-cone preservation.

> *"Disruptions in the cone opsin gene array cause a variety of inherited retinal disorders, including blue cone monochromacy, Bornholm eye disease, and tritan color vision deficiency."* — [PMID: 42346125](https://pubmed.ncbi.nlm.nih.gov/42346125/)

> *"Waveguiding cone density was 2073 ± 963 cones/mm2 (n = 9), which was consistent with published histological estimates of S-cone density in the normal eye."* — [PMID: 36301530](https://pubmed.ncbi.nlm.nih.gov/36301530/)

This finding resolves a crucial nomenclature pitfall and demonstrates the **genetic separation of function** between the S-cone opsin (OPN1SW) and the L/M opsins.

### Finding 4 — OPN1SW expression and S-cone identity are driven by RORβ in synergy with CRX

The orphan nuclear receptor RORβ (retinoid-related orphan receptor beta) activates the S-opsin gene (Opn1sw) through binding sites upstream of the gene. RORβ acts only modestly alone but strongly in synergy with the cone-rod homeobox factor CRX. RORβ-binding sites are required for Opn1sw expression in the mouse retina, and RORβ-deficient mice fail to induce S-opsin during postnatal cone development.

> *"the orphan nuclear receptor RORbeta (retinoid-related orphan receptor beta) activates the S opsin gene (Opn1sw) through binding sites upstream of the gene"* — [PMID: 16574740](https://pubmed.ncbi.nlm.nih.gov/16574740/)

> *"activates the Opn1sw promoter modestly alone but strongly in synergy with the retinal cone-rod homeobox factor (CRX)"* — [PMID: 16574740](https://pubmed.ncbi.nlm.nih.gov/16574740/)

This establishes the **transcriptional control logic** that specifies S-cone identity and drives OPN1SW expression.

### Finding 5 — Specific missense substitutions in OPN1SW cause autosomal-dominant tritanopia — direct genetic proof of a non-redundant S-cone role

Three complementary human-genetic studies anchor OPN1SW's causal role:

| Study | Finding | Evidence |
|-------|---------|----------|
| Weitz et al. 1992 ([PMID: 1531728](https://pubmed.ncbi.nlm.nih.gov/1531728/)) | Two point mutations in the blue-sensitive opsin gene in 4/9 unrelated autosomal-dominant tritanopes | Pedigree segregation + allele-specific oligonucleotide analysis |
| Gunther et al. 2006 ([PMID: 16961973](https://pubmed.ncbi.nlm.nih.gov/16961973/)) | Heterozygous Leu56Pro at a highly conserved residue | Absent from 564 control S-opsin genes |
| Baraas et al. 2007 ([PMID: 17429491](https://pubmed.ncbi.nlm.nih.gov/17429491/)) | Two relatives, same novel OPN1SW mutation, different severity; disrupted S-cone mosaics | Adaptive-optics retinal imaging |

> *"two different point mutations in the gene encoding the blue-sensitive opsin, each leading to an amino acid substitution"* — [PMID: 1531728](https://pubmed.ncbi.nlm.nih.gov/1531728/)

> *"heterozygous for a mutation that caused the amino acid proline to be substituted in place of a highly conserved leucine at amino acid position 56 in the S cone opsin"* — [PMID: 16961973](https://pubmed.ncbi.nlm.nih.gov/16961973/)

> *"tritan deficiency is progressive in nature"* — [PMID: 17429491](https://pubmed.ncbi.nlm.nih.gov/17429491/)

Together these establish OPN1SW as the **non-redundant S-cone pigment** whose coding mutations produce a progressive S-cone dystrophy — not a purely stationary defect — with physical disruption of the S-cone mosaic.

### Finding 6 — Immunohistochemistry confirms blue cone opsin is restricted to S-cone outer segments

In human donor retina, immunofluorescence with well-characterized cone-opsin antibodies showed blue cone opsin restricted to the outer segments of blue cones. In a dystrophy case, red/green opsins were abnormally distributed along the entire plasma membrane, but the blue cone opsin localization held in both macula and periphery.

> *"blue cone opsin was restricted to the outer segments of blue cones in the affected retina"* — [PMID: 16020309](https://pubmed.ncbi.nlm.nih.gov/16020309/)

This provides **direct subcellular localization**: OPN1SW protein carries out its function in the S-cone outer-segment membrane — the organelle specialized for phototransduction.

### Finding 7 — Bioinformatic analysis confirms canonical class-A opsin functional architecture

Sequence analysis of P03999 (345 aa) identifies all hallmark opsin/GPCR functional elements:

| Functional element | Location in P03999 | Rhodopsin equivalent | Role |
|---------------------|--------------------|--------------------|------|
| Retinal-attachment lysine (Schiff base) | Lys290 (TM7) | Lys296 | Covalent 11-*cis*-retinal attachment |
| NPxxY motif | NPIIY (296–300) | NPxxY | Activation / conformational switch |
| E/DRY motif | ERY (128–130, TM3 cytoplasmic end) | E/DRY | Gates G-protein activation |
| Conserved disulfide | Cys104 / Cys181 | Cys110 / Cys187 | Stabilizes extracellular/retinal-pocket fold |
| N-glycosylation sequons | Asn11-x-Ser; Asn72-x-Ser | — | N-terminal maturation |

> *"cryo-electron microscopy structures of the three human cone opsins, each bound to a G protein and all-[trans retinal]"* — [PMID: 42348690](https://pubmed.ncbi.nlm.nih.gov/42348690/)

The 2026 cryo-EM structures experimentally confirm the GPCR architecture and retinal/G-protein binding that were inferred bioinformatically from these sequence motifs.

### Finding 8 — Human OPN1SW is a violet/blue (not UV) SWS1-class pigment; spectral tuning is set by retinal-pocket residues

OPN1SW belongs to the SWS1 opsin class, whose members are tuned to either UV or violet/blue light primarily via a small number of retinal-pocket residues. Ancestral-sequence reconstruction indicates the therian mammalian ancestor had a UV-sensitive SWS1, with violet-sensitive pigments (like the human one, λmax ≈ 414–420 nm) evolving independently ≥12 times — favored in diurnal species with longer eyes. Mutagenesis across vertebrate SWS1 pigments shows that substitutions at site 86 (and 90) shift λmax between UV and violet. Human OPN1SW carries Phe at position 86, consistent with its violet/blue sensitivity.

> *"a short wavelength-sensitive opsin 1 (SWS1) pigment that is primarily sensitive to either ultraviolet or violet light"* — [PMID: 26582021](https://pubmed.ncbi.nlm.nih.gov/26582021/)

> *"Bowerbird SWS1 mutants C86F, S90C, and C86S/S90C all shifted λmax into the UV"* — [PMID: 24499383](https://pubmed.ncbi.nlm.nih.gov/24499383/)

This defines the **spectral-specificity axis** of human OPN1SW: it is a violet/blue pigment, and that tuning is encoded in identifiable retinal-pocket residues.

### Finding 9 — Cone-opsin signaling operates through the transducin cascade with RGS9-GAP deactivation; recovery tracks opsin regeneration

The full activation-to-recovery cycle of OPN1SW-type signaling is supported by human genetics and cone electrophysiology. In mouse rods, the light-driven outer-segment length response requires transducin, the Gα activated in the first amplifying step. In humans, bradyopsia caused by an R9AP triple-deletion (reducing RGS9, the GAP complex, in the outer segment) leaves cone activation kinetics, amplitude, and photosensitivity normal but markedly slows recovery — pinpointing the deactivation step within the G-protein cascade. Recovery from high (75%) bleaches tracks the time course of cone opsin regeneration, and unregenerated cone opsin produces activating "dark light" via the G protein, confirming cone opsins act as transducin activators. Suction-pipette recordings of blue/UV-sensitive cones show response recovery is dominated by Ca²⁺-sensitive quenching of the active Meta-II form of the cone photopigment.

> *"recovery from the highest bleaching exposure (75%) tracked the time course of cone opsin regeneration"* — [PMID: 42094530](https://pubmed.ncbi.nlm.nih.gov/42094530/)

> *"the process dominating recovery of the bright flash response represents quenching of the active Meta II form of the cone photopigment"* — [PMID: 22802362](https://pubmed.ncbi.nlm.nih.gov/22802362/)

This closes the mechanistic loop: OPN1SW signals through an **active Meta-II state** that activates transducin and is quenched (via phosphorylation/arrestin and Ca²⁺-feedback) and deactivated downstream by the RGS9–R9AP GAP complex.

---

## Mechanistic Model / Interpretation

The findings integrate into a single coherent model of OPN1SW as the molecular origin of the short-wavelength arm of human color vision.

### Molecular function (the phototransduction cascade)

```
   Violet/blue photon (λmax ≈ 414–420 nm)
            │
            ▼
   11-cis-retinal  ──isomerization──►  all-trans-retinal
   (Schiff base to Lys290, TM7)
            │
            ▼
   OPN1SW Meta-II (active GPCR conformation; E/DRY + NPxxY switches)
            │  GEF activity
            ▼
   Cone transducin (Gα_t2):  GDP ──► GTP exchange
            │
            ▼
   Cone phosphodiesterase (PDE6C) activated
            │
            ▼
   cGMP hydrolyzed  ──►  CNG channels close
            │
            ▼
   S-cone HYPERPOLARIZES  (graded light response)
            │
   ── DEACTIVATION ──
   • Meta-II quenched by opsin phosphorylation + arrestin (Ca²⁺-sensitive)
   • Transducin shutoff accelerated by RGS9–R9AP GAP complex
   • Recovery paced by 11-cis-retinal regeneration (visual cycle)
```

### From photoreceptor to perception (the circuit)

```
   S-CONE (OPN1SW outer segment)
        │  hyperpolarization → sign-inverting synapse
        ▼
   Blue-cone (S-ON) bipolar cell
        │
        ▼
   Small bistratified "blue-ON" ganglion cell
        │   (S-ON vs L+M-OFF opponency)
        ▼
   "BLUE-YELLOW" color-opponent channel → LGN → cortex
```

### Localization summary

| Scale | Location | Evidence |
|-------|----------|----------|
| Tissue | Retina, S (blue) cones, chromosome 7 gene | Immunohistochemistry, genetics |
| Cell | S-cone photoreceptor | Antibody labeling, AO imaging |
| Subcellular | **Outer-segment membrane** | [PMID: 16020309](https://pubmed.ncbi.nlm.nih.gov/16020309/) |
| Molecular | 7-TM integral membrane GPCR, retinal in TM-core pocket | Cryo-EM [PMID: 42348690](https://pubmed.ncbi.nlm.nih.gov/42348690/) |

### Developmental and evolutionary context

OPN1SW expression is specified developmentally by **RORβ synergizing with CRX** ([PMID: 16574740](https://pubmed.ncbi.nlm.nih.gov/16574740/)). Evolutionarily, the human pigment is a **violet-shifted SWS1** derived from an ancestral UV-sensitive opsin, with the violet tuning encoded by retinal-pocket residues including Phe86 ([PMID: 26582021](https://pubmed.ncbi.nlm.nih.gov/26582021/), [PMID: 24499383](https://pubmed.ncbi.nlm.nih.gov/24499383/)).

### Disease logic

OPN1SW is **non-redundant**: no other opsin substitutes for it in S-cones. Coding mutations (e.g., Leu56Pro, and the substitutions reported by Weitz et al.) produce **autosomal-dominant, progressive tritanopia** — an S-cone dystrophy. This is cleanly separable from **blue cone monochromacy**, which arises from the X-linked L/M cluster and leaves OPN1SW-expressing S-cones intact.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|---------------------|------------------------------|
| [42348690](https://pubmed.ncbi.nlm.nih.gov/42348690/) | *Cryo-EM structures of human cone visual pigments* | Direct structure of SWS/blue opsin bound to G protein + retinal; confirms GPCR architecture, retinal binding, transducin coupling (F001, F002, F007) |
| [23895762](https://pubmed.ncbi.nlm.nih.gov/23895762/) | *Distinct synaptic mechanisms create parallel S-ON and S-OFF color opponent pathways* | Shows the segregated S-cone → blue-cone bipolar → bistratified GC circuit and origin of blue-yellow opponency (F002) |
| [42346125](https://pubmed.ncbi.nlm.nih.gov/42346125/) | *Cone Opsins and Inherited Retinal Disease* | Links cone-opsin gene disruption to tritan deficiency; disorder taxonomy (F003) |
| [36301530](https://pubmed.ncbi.nlm.nih.gov/36301530/) | *Foveal Cone Structure in BCM* | S-cones preserved in BCM (normal density), proving BCM ≠ OPN1SW (F003) |
| [16574740](https://pubmed.ncbi.nlm.nih.gov/16574740/) | *Activation of the blue opsin gene by RORβ* | Transcriptional control of Opn1sw by RORβ + CRX (F004) |
| [1531728](https://pubmed.ncbi.nlm.nih.gov/1531728/) | *Human tritanopia associated with two substitutions in blue-sensitive opsin* | Primary genetic link: OPN1SW coding mutations cause AD tritanopia (F005) |
| [16961973](https://pubmed.ncbi.nlm.nih.gov/16961973/) | *Novel SWS cone pigment mutation in tritan defect* | Leu56Pro pathogenic variant, absent from 564 controls (F005) |
| [17429491](https://pubmed.ncbi.nlm.nih.gov/17429491/) | *AO imaging reveals S-cone dystrophy in tritan deficiency* | Tritan deficiency is progressive; S-cone mosaic disrupted (F005) |
| [16020309](https://pubmed.ncbi.nlm.nih.gov/16020309/) | *Abnormal distribution of red/green cone opsins…* | Blue opsin restricted to S-cone outer segments (F006) |
| [26582021](https://pubmed.ncbi.nlm.nih.gov/26582021/) | *Spectral shifts of mammalian SWS1 pigments* | SWS1 class UV-vs-violet tuning; violet evolved repeatedly (F008) |
| [24499383](https://pubmed.ncbi.nlm.nih.gov/24499383/) | *Spectral tuning in bowerbird SWS1* | Sites 86/90 control UV-vs-violet tuning experimentally (F008) |
| [42094530](https://pubmed.ncbi.nlm.nih.gov/42094530/) | *Optoretinography in R9AP-bradyopsia* | Cone recovery requires G-protein deactivation (RGS9-GAP); recovery tracks opsin regeneration (F009) |
| [22802362](https://pubmed.ncbi.nlm.nih.gov/22802362/) | *Dominant time constant of cone photoreceptors* | Response recovery = quenching of active Meta-II photopigment (F009) |

### Supporting / contextual literature

- **Red/green opsin tuning** ([PMID: 9822760](https://pubmed.ncbi.nlm.nih.gov/9822760/), [PMID: 10746123](https://pubmed.ncbi.nlm.nih.gov/10746123/)) — quantitative spectral-tuning framework for cone opsins, parallel to OPN1SW's retinal-pocket tuning logic.
- **BCM gene-therapy models** ([PMID: 38060327](https://pubmed.ncbi.nlm.nih.gov/38060327/), [PMID: 42275379](https://pubmed.ncbi.nlm.nih.gov/42275379/), [PMID: 37001420](https://pubmed.ncbi.nlm.nih.gov/37001420/)) — reinforce that BCM is an L/M-opsin (not OPN1SW) disorder; these models use Opn1sw⁻/⁻ backgrounds, underscoring the gene's distinct role.
- **Foveal color circuit connectomics** ([PMID: 39190352](https://pubmed.ncbi.nlm.nih.gov/39190352/), [PMID: 31405926](https://pubmed.ncbi.nlm.nih.gov/31405926/), [PMID: 19571128](https://pubmed.ncbi.nlm.nih.gov/19571128/)) — detail how S-cone signals are distributed to multiple ganglion-cell types beyond the classical bistratified cell.
- **RORβ/circadian regulation** ([PMID: 23351077](https://pubmed.ncbi.nlm.nih.gov/23351077/)) — Per1/Per2 clock genes modulate blue-cone opsin patterning, supporting developmental control.

---

## Limitations and Knowledge Gaps

1. **No OPN1SW-specific biochemical kinetics.** Much of the phototransduction kinetic data (transducin activation rate, Meta-II quenching, GAP effects) derives from rods, red/green-sensitive cones, or non-human cones (salamander, fish, frog). Direct biochemical measurement of the human S-cone opsin's transducin-activation rate, Meta-II lifetime, and spectral properties remains sparse — the 2026 cryo-EM work is the first high-resolution structural data specific to the human SWS opsin.

2. **Spectral tuning residues inferred, not fully mutagenized in the human pigment.** The role of Phe86 and other retinal-pocket residues in setting the human λmax ≈ 414–420 nm is inferred from comparative/evolutionary mutagenesis in non-human SWS1 pigments, not from direct human-OPN1SW mutagenesis spectroscopy.

3. **Genotype–phenotype spectrum incomplete.** Only a handful of pathogenic OPN1SW variants (e.g., Leu56Pro and the Weitz substitutions) are documented. The full mutational landscape, penetrance, and the molecular basis of progression (misfolding vs. trafficking vs. gain-of-toxicity) in tritanopia are not resolved.

4. **Dominant-negative mechanism unproven for OPN1SW.** By analogy to rhodopsin and L/M-opsin missense mutations (which misfold, mislocalize, and can be cytotoxic), autosomal-dominant tritanopia is *presumed* to involve a dominant misfolding/trafficking defect, but this has not been directly demonstrated for OPN1SW variants.

5. **S-cone deactivation machinery assumed shared.** The roles of cone arrestin (ARR3), GRK, RGS9–R9AP, and Ca²⁺-feedback are documented for cones generally; S-cone-specific deactivation has not been isolated.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous spectroscopy of human OPN1SW.** Express P03999 in HEK293/COS cells, reconstitute with 11-*cis*-retinal, and directly measure λmax and the spectral effect of site-86/90 substitutions in the *human* sequence to confirm the inferred tuning mechanism (Finding 8).

2. **In vitro transducin-activation assays.** Use purified OPN1SW and cone transducin (Gα_t2) to quantify light-dependent GDP→GTP exchange rate, directly measuring the GEF activity that is currently inferred from structure and cross-species physiology (Findings 1, 9).

3. **Structural analysis of tritan variants.** Model/express Leu56Pro and the Weitz substitutions; assess folding, 11-*cis*-retinal binding, outer-segment trafficking, and potential dominant-negative aggregation — testing the misfolding hypothesis for autosomal-dominant tritanopia (Finding 5).

4. **Adaptive-optics S-cone phenotyping in a variant cohort.** Extend AO retinal imaging ([PMID: 17429491](https://pubmed.ncbi.nlm.nih.gov/17429491/)) across a larger OPN1SW-variant cohort to map genotype → S-cone mosaic disruption → progression, clarifying whether tritanopia is uniformly progressive.

5. **Cryo-EM of the active Meta-II–transducin complex for OPN1SW.** Build on the 2026 structures by capturing the human SWS opsin in its active Meta-II state coupled to transducin to define the S-cone-specific activation switch (Findings 1, 7, 9).

6. **Dissect S-cone deactivation.** Use S-cone-targeted electrophysiology/ORG in human and model systems to isolate the contributions of RGS9–R9AP, cone arrestin, and Ca²⁺-feedback specifically in OPN1SW signaling (Finding 9).

---

## Conclusion

OPN1SW is the **short-wave-sensitive (blue) cone opsin**, a class-A GPCR that functions as the light receptor of human S-cone photoreceptors. It covalently binds 11-*cis*-retinal in its transmembrane core, absorbs violet/blue light (λmax ≈ 414–420 nm, tuned by retinal-pocket residues such as Phe86), and upon photoisomerization adopts an active Meta-II state that catalyzes GDP→GTP exchange on cone transducin — initiating the cone phototransduction cascade (PDE6C → cGMP hydrolysis → CNG closure → hyperpolarization), with deactivation by opsin phosphorylation/arrestin and the RGS9–R9AP GAP complex. It operates in the **outer-segment membrane of S-cones** and provides the input to the blue-cone bipolar → small bistratified ganglion cell circuit that forms the S-vs-(L+M) **"blue-yellow" color-opponent channel**. Its role is non-redundant: loss-of-function missense mutations cause progressive autosomal-dominant tritanopia, distinct from blue cone monochromacy (an OPN1LW/OPN1MW disorder that spares OPN1SW).


## Artifacts

- [OpenScientist final report](OPN1SW-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](OPN1SW-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:42348690
2. PMID:23895762
3. PMID:42346125
4. PMID:36301530
5. PMID:16574740
6. PMID:1531728
7. PMID:16961973
8. PMID:17429491
9. PMID:16020309
10. PMID:26582021
11. PMID:24499383
12. PMID:42094530
13. PMID:22802362
14. PMID:9822760
15. PMID:10746123
16. PMID:38060327
17. PMID:42275379
18. PMID:37001420
19. PMID:39190352
20. PMID:31405926
21. PMID:19571128
22. PMID:23351077