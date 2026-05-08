# scRNA-seq × Function → BP Inference: Cephalopod Gene Annotation Synthesis

## Concept

If we know:
- **Gene G** has molecular function **F** (from UniProt/GO/biochemistry)
- **Gene G** is a marker for cell type **C** (from scRNA-seq)
- **Cell type C** has known biological role **R**

Then we can infer: Gene G is involved in biological process **BP** = F operating in R context.

This is essentially the logic behind GO-CAM models and IEP (Inferred from Expression Pattern)
annotations, but applied systematically to cephalopod scRNA-seq data.

## Available scRNA-seq Datasets

| Dataset | Species | Tissue | Cell Types | GEO | Reference |
|---------|---------|--------|------------|-----|-----------|
| Optic lobe atlas | *O. bimaculoides* | Optic lobe | 6 neuronal classes + subtypes | GSE211208 | Songco-Casey 2022 |
| Brain snRNA-seq | *A. fangsiao* | Supra-esophageal brain | 8 cell types | - | Jiang 2022 |
| Whole-body atlas | *L. vulgaris* | Whole body | Chromatophores, suckers, neurons, etc. | - | Duruz 2023 |

## Known Marker Genes × Swiss-Prot Entries

### Genes with BOTH scRNA-seq expression data AND Swiss-Prot entries

| Marker Gene | scRNA-seq Cell Type | Species (scRNA) | Swiss-Prot Entry | Known MF | Known BP | **Inferable New BP** |
|-------------|--------------------|----|----------|----------|----------|---------------------|
| **RHO (rhodopsin)** | Photoreceptor neurons (optic lobe) | *O. bimaculoides* | P09241, P31356, O16005 | Photoreceptor activity | Visual perception, phototransduction | **Dermal light sensing** (expressed in skin chromatophores per Ramirez 2015) |
| **FMRFa** | FMRFa+ dopaminergic subtype | *O. bimaculoides* optic lobe | P91889 (*S. officinalis*), B6E465 (*D. pealeii*) | Neuropeptide activity | Neuropeptide signaling | **Visual processing modulation** (marker of optic lobe dopaminergic neurons) |
| **Gq-alpha** | Photoreceptor neurons | *O. bimaculoides* optic lobe | P38412 (*L. forbesii*) | GTPase activity | GPCR signaling | **Visual phototransduction** (part of rhabdomeric photoreceptor cascade) |
| **dat** (dopamine transporter) | Dopaminergic neurons | *O. bimaculoides*, *A. fangsiao* | — (no Swiss-Prot) | — | — | Would need TrEMBL entry |
| **vacht** (vesicular ACh transporter) | Cholinergic neurons | *O. bimaculoides*, *A. fangsiao* | — (no Swiss-Prot) | — | — | Would need TrEMBL entry |
| **NOS** (NO synthase) | NOS+ cholinergic subtype | *O. bimaculoides* | — (no Swiss-Prot) | — | — | Would need TrEMBL entry |
| **tyrbh** (tyramine β-hydroxylase) | Octopaminergic neurons | *O. bimaculoides* | — | — | — | Would need TrEMBL entry |

### The problem: most scRNA-seq markers lack Swiss-Prot entries

The overlap between scRNA-seq marker genes and Swiss-Prot is very small because:
1. scRNA-seq uses *O. bimaculoides* gene models (obimac IDs) — only 1 Swiss-Prot entry (CRT1)
2. Most markers are conserved neurotransmitter pathway genes (transporters, TFs) — annotated in vertebrates but not in cephalopod UniProt
3. The cephalopod-specific markers are novel genes with no homologs in Swiss-Prot

## Inferrable BP Annotations: What's Actually Possible

### Tier 1: Strong inferences (MF known + cell type specific + published)

These combine Swiss-Prot MF data with scRNA-seq cell type localization to propose new BP annotations:

#### 1. Rhodopsin → dermal photoreception / body patterning
- **MF**: Photoreceptor activity (GO:0009881) — IDA
- **Cell type evidence**: Expressed in skin chromatophore cells (Ramirez & Oakley 2015), 
  sucker cells (Maselli et al. 2025), optic lobe neurons (Songco-Casey 2022)
- **Inferable BP**: 
  - GO:0009585 (red, far-red light phototransduction) → **NO**, λmax is 480nm (blue)
  - GO:0071482 (cellular response to light stimulus) — in skin context
  - GO:0043473 (pigmentation) — via chromatophore LACE response
- **Evidence type**: IEP + IDA combined (expression in chromatophores + known photoreceptor function)
- **Strength**: STRONG — published functional data in skin (LACE response)

#### 2. FMRFamide → visual circuit modulation
- **MF**: Neuropeptide activity
- **Cell type evidence**: Marker of FMRFa+ dopaminergic neuron subtype in optic lobe
- **Inferable BP**: GO:0007602 (phototransduction) or GO:0050890 (cognition) — in visual processing context
- **Strength**: MODERATE — expression is clear but functional role in visual processing is speculative

#### 3. Complexin → synaptic transmission in visual circuits
- **MF**: SNARE binding (GO:0000149) — IDA
- **Cell type evidence**: Expected in presynaptic terminals throughout optic lobe
- **Inferable BP**: Already well-annotated from squid giant synapse data
- **Strength**: REDUNDANT — we already have this from biochemistry

#### 4. Hemocyanin → innate immune defense
- **MF**: Oxygen carrier activity (GO:0005344)
- **Cell type evidence**: Not from scRNA-seq, but hemocyanin-derived antimicrobial peptides reported (PMID:35877752)
- **Inferable BP**: GO:0006955 (immune response), GO:0042742 (defense response to bacterium)
- **Strength**: MODERATE — dual function supported by peptide characterization

### Tier 2: Weaker inferences (MF known + expression data but function in that context unclear)

| Gene | MF | Expression Context | Possible BP | Why Weak |
|------|----|--------------------|-------------|----------|
| Gq-alpha | GTPase | Photoreceptor neurons | Rhabdomeric phototransduction | Already inferred from visual system by similarity |
| Kinesin HC | Motor protein | Optic lobe neurons | Visual system axonal transport | Too generic |
| DDO | D-aspartate oxidase | CNS (liver/kidney confirmed, CNS expression unknown) | Neuromodulation via D-Asp/NMDA | CNS expression not yet demonstrated |
| S-crystallins | Structural/GST | Eye lens | Lens development, light refraction | Already annotated |

### Tier 3: Most interesting but least tractable — cephalopod-specific cell types

The *L. vulgaris* whole-body atlas identified cell types with **no vertebrate equivalent**:
- **Chromatophore muscle cells** — express muscle-specific genes + cephalopod-specific factors
- **Iridophore cells** — express reflectin genes (no Swiss-Prot entries)
- **Sucker disc cells** — express chemotactile receptors (CRT1 has Swiss-Prot: A0A0L8FVQ9)
- **Ink gland cells** — produce melanin + tyrosinase

For **CRT1 (chemotactile receptor)** in sucker cells:
- **MF**: Ion channel activity (GO:0005230), receptor activity (GO:0004888) — from Swiss-Prot
- **Cell type**: Sucker disc sensory cells (from scRNA-seq)
- **Inferable BP**: 
  - GO:0050912 (detection of chemical stimulus involved in sensory perception of taste) — contact chemosensation
  - GO:0007638 (mechanosensory behavior) — sucker-mediated prey capture
- **Strength**: STRONG — published functional data (van Giesen et al. 2020)

## Synthesis: What's the yield?

### Realistic new annotations from scRNA-seq integration

| Gene | New BP | Evidence | Species for annotation |
|------|--------|---------|----------------------|
| RHO | Dermal light sensing / body patterning | IEP+IDA | *O. bimaculoides* |
| CRT1 | Contact chemosensation / prey capture | IEP+IDA | *O. bimaculoides* |
| Hemocyanin | Innate immune defense | IDA (antimicrobial peptide) | *N. pompilius*, *S. maindroni* |
| FMRFa | Visual circuit neuromodulation | IEP | *O. bimaculoides* |

### Why the yield is small

1. **Swiss-Prot bottleneck**: Only ~35 interesting Swiss-Prot entries exist for all cephalopods. Most scRNA-seq markers are in TrEMBL or genome-predicted genes.
2. **Cross-species mapping**: scRNA-seq is in *O. bimaculoides* but most Swiss-Prot entries are in *O. vulgaris*, *D. pealeii*, *S. officinalis*. One-to-one ortholog mapping is not straightforward.
3. **IEP is weak evidence**: Expression in a cell type ≠ function in that cell type's biology. A gene expressed in chromatophore cells might be housekeeping.
4. **Most strong inferences are already known**: The best MF→BP inferences (rhodopsin→vision, complexin→synaptic transmission) are already captured from direct biochemistry.

### Where this approach becomes powerful

The real value isn't in annotating individual Swiss-Prot genes — it's in:

1. **Validating/challenging existing annotations**: e.g., if a gene annotated to "nuclear migration" (like kinesin) is NOT expressed in dividing cells but IS in post-mitotic neurons, that supports our decision to mark it as over-annotated.

2. **Prioritizing new genes for review**: The top marker genes for cephalopod-specific cell types (chromatophore, iridophore, sucker) that lack ANY GO annotations are the most valuable targets — but they need Swiss-Prot entries first.

3. **GO-CAM models**: Linking MF + BP + CC in a single causal model benefits enormously from cell-type context. "Rhodopsin (MF) enables phototransduction (BP) in chromatophore cells (CC) as part of body pattern regulation" is more informative than any single annotation.

## Recommendations

1. **Immediate**: Add dermal photoreception BP to rhodopsin review (strong evidence)
2. **Immediate**: Add contact chemosensation BP to CRT1 review (strong evidence)  
3. **Short-term**: Request Swiss-Prot review of *O. bimaculoides* TrEMBL entries for scRNA-seq marker genes (dat, vacht, nos, tyrbh)
4. **Medium-term**: Build GO-CAM models for cephalopod visual system and chromatophore system integrating scRNA-seq cell type data
5. **Long-term**: As more CRISPR knockouts become available in *E. berryi*, scRNA-seq cell type data becomes increasingly useful for functional inference
