---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-10T23:30:03.998489'
end_time: '2026-08-10T23:53:23.640666'
duration_seconds: 1399.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: galE
  gene_symbol: galE
  uniprot_accession: Q88I72
  protein_description: 'RecName: Full=UDP-glucose 4-epimerase {ECO:0000256|ARBA:ARBA00018569,
    ECO:0000256|RuleBase:RU366046}; EC=5.1.3.2 {ECO:0000256|ARBA:ARBA00013189, ECO:0000256|RuleBase:RU366046};'
  gene_info: Name=galE {ECO:0000313|EMBL:AAN68737.1}; OrderedLocusNames=PP_3129 {ECO:0000313|EMBL:AAN68737.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAD(P)-dependent epimerase/dehydratase
  protein_domains: Epimerase_deHydtase. (IPR001509); NAD(P)-bd_dom_sf. (IPR036291);
    UDP_G4E. (IPR005886); Epimerase (PF01370)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: galE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: galE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I72
- **Protein Description:** RecName: Full=UDP-glucose 4-epimerase {ECO:0000256|ARBA:ARBA00018569, ECO:0000256|RuleBase:RU366046}; EC=5.1.3.2 {ECO:0000256|ARBA:ARBA00013189, ECO:0000256|RuleBase:RU366046};
- **Gene Information:** Name=galE {ECO:0000313|EMBL:AAN68737.1}; OrderedLocusNames=PP_3129 {ECO:0000313|EMBL:AAN68737.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAD(P)-dependent epimerase/dehydratase
- **Key Domains:** Epimerase_deHydtase. (IPR001509); NAD(P)-bd_dom_sf. (IPR036291); UDP_G4E. (IPR005886); Epimerase (PF01370)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "galE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'galE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **galE** (gene ID: galE, UniProt: Q88I72) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *galE* (UDP-glucose 4-epimerase) in *Pseudomonas putida* KT2440

**UniProt:** Q88I72 | **Locus:** PP_3129 | **Gene:** *galE* | **EC:** 5.1.3.2
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)

---

## Summary

The gene *galE* (locus PP_3129; UniProt Q88I72) of *Pseudomonas putida* KT2440 encodes a **UDP-glucose 4-epimerase** (EC 5.1.3.2), a cytoplasmic, NAD⁺-dependent enzyme of the short-chain dehydrogenase/reductase (SDR) / NAD(P)-dependent epimerase–dehydratase superfamily. Its primary and defining biochemical function is the **reversible epimerization of carbon-4 of the hexose ring, interconverting UDP-α-D-glucose (UDP-Glc) and UDP-α-D-galactose (UDP-Gal)**. This is a single-substrate, single-product isomerization that requires no net input of reducing equivalents: the enzyme uses a tightly (effectively irreversibly) bound NAD⁺ cofactor that transiently oxidizes the sugar to a UDP-4-ketopyranose intermediate, allows the intermediate to rotate within the active site, and then returns the hydride to the opposite face of C4, thereby inverting the stereochemistry.

The identity of Q88I72 as a canonical GalE is supported by convergent lines of evidence: (i) UniProt/InterPro/Pfam domain diagnostics (IPR005886 UDP_glucose_4-epimerase, IPR001509, IPR036291, PF01370); (ii) an exactly conserved catalytic architecture — the Rossmann dinucleotide-binding motif GxxGxxG (residues 7–13) and the SDR catalytic Ser111/Tyr135/Lys139 triad that maps residue-for-residue onto the biochemically characterized *E. coli* GalE triad Ser124/Tyr149/Lys153; and (iii) 43% global sequence identity to *E. coli* GalE, well above the ~30% threshold for confident functional transfer. On these grounds the enzyme is assigned to substrate-specificity **"group 1"** (UDP-Glc/Gal-specific, not UDP-GlcNAc/GalNAc-active).

Physiologically, the enzyme sits at the junction between galactose (Leloir) metabolism and cell-surface glycan biosynthesis. A distinctive genomic observation for *P. putida* KT2440 is that the organism **lacks the catabolic Leloir enzymes galactokinase (galK) and galactose-1-phosphate uridylyltransferase (galT)**, and PP_3129 is physically **embedded within an exopolysaccharide (EPS) biosynthesis/export gene cluster** (PP_3126–PP_3132). This strongly implies that in KT2440 GalE acts predominantly in the **anabolic (biosynthetic) direction** — generating UDP-galactose from UDP-glucose (supplied via pgm → galU) to provide the galactosyl donor for lipopolysaccharide (LPS)/O-antigen and exopolysaccharide biosynthesis — rather than in the classic catabolic role of funneling dietary galactose into glycolysis. The gene product functions in the **cytoplasm**; the 321-residue protein has a soluble SDR fold with no signal peptide or transmembrane segment.

---

## Gene/Protein Identification — Verification

Before presenting findings, the mandatory identity check was completed and **passed**:

| Verification step | Result |
|---|---|
| Gene symbol "galE" matches protein description | ✅ UniProt RecName = UDP-glucose 4-epimerase; EC 5.1.3.2 |
| Organism correct | ✅ *P. putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Protein family/domains align with literature | ✅ SDR / NAD(P)-epimerase-dehydratase; IPR005886, IPR001509, IPR036291, PF01370 |
| No confusion with a same-symbol gene in another organism | ✅ GalE is a conserved, universally named enzyme; homology to characterized bacterial GalEs is direct |

The gene symbol *galE* is **not ambiguous** here — it denotes the canonical UDP-glucose 4-epimerase, a well-characterized enzyme conserved from bacteria to humans. Literature for GalE from many organisms (*E. coli*, *Aeromonas hydrophila*, *Bifidobacterium longum*, archaea, human) is directly relevant, and the functional annotation is transferable with high confidence.

---

## Key Findings

### F001 — GalE is a UDP-glucose 4-epimerase catalyzing reversible UDP-Glc ⇌ UDP-Gal interconversion (EC 5.1.3.2)

The core function of the PP_3129 gene product is the reversible interconversion of the two UDP-hexose diastereomers. UniProt Q88I72 (321 aa) annotates the catalytic activity as **"UDP-alpha-D-glucose = UDP-alpha-D-galactose"**, with cofactor NAD⁺ and pathway assignment "Carbohydrate metabolism; galactose metabolism." This is corroborated by database cross-references (KEGG `ppu:PP_3129`; orthology K01784; BioCyc PPUT160488:G1G01-3347-MONOMER) and by InterPro diagnostics — most tellingly IPR005886 (UDP_glucose_4-epimerase), a diagnostic TIGRFAM signature specific to this enzyme.

The reaction is the defining chemistry of the enzyme family. As stated for GalE enzymes generally, *"UDP-glucose 4-epimerase (GalE) catalyzes the interconversion of UDP-glucose (UDP-Glc) and UDP-galactose (UDP-Gal)"* ([PMID: 33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/)). GalE is one of the enzymes of the Leloir pathway and belongs to the SDR superfamily: *"UDP-sugar 4-epimerase (GalE) belongs to the short-chain dehydrogenase/reductase (SDR) superfamily of proteins and is one of enzymes in the Leloir pathway"* ([PMID: 26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/)).

### F002 — SDR-type mechanism with a tightly/irreversibly bound NAD⁺ cofactor and a transient 4-keto intermediate

The mechanism is redox-neutral overall. Although the reaction proceeds through oxidation at C4, the enzyme consumes no net NAD⁺/NADH because the cofactor is **tightly (effectively irreversibly) bound** and is oxidized and re-reduced within a single catalytic cycle. Sequence analysis of Q88I72 confirms the requisite machinery: the N-terminal Rossmann dinucleotide-binding motif GxxGxxG (residues 7–13, "GGAGYIGS") for NAD⁺ binding, and the SDR catalytic Tyr-x-x-x-Lys motif (Tyr135…Lys139, "YGLSK") corresponding to the catalytic Tyr149/Lys153 couple of *E. coli* GalE.

Literature establishes each feature. The GalE family uses *"a conserved 'transient keto intermediate' mechanism and [has] variable substrate specificity"* ([PMID: 33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/)). The cofactor is retained: reviews document *"irreversible binding of the cofactor NAD and uridine nucleotide-induced activation of this cofactor"* ([PMID: 26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/)). Structural work on the archaeal *Pyrobaculum calidifontis* enzyme identifies the mechanism of retention: *"the presence of the NAD-binding loop in GalE is largely responsible for preventing the release of the cofactor from the holoenzyme"* ([PMID: 21645492](https://pubmed.ncbi.nlm.nih.gov/21645492/)).

### F006 — Catalytic residues and stereochemistry: conserved Ser–Tyr–Lys triad and nonstereospecific hydride return

The stereochemical inversion at C4 is achieved by a well-understood two-part mechanism, defined by gold-standard studies of *E. coli* GalE (catalytic triad Ser124/Tyr149/Lys153). In Q88I72 the homologous catalytic couple maps to **Tyr135/Lys139** with the triad serine upstream (Ser111). The mechanism: **Tyr149 (Tyr135 in PP_3129) acts as the catalytic base**, abstracting the C4-hydroxyl proton; the C4 hydride is transferred to NAD⁺, forming NADH and a **UDP-4-ketopyranose intermediate**. Because the UDP moiety is tightly bound but the ketopyranose ring is only weakly held, the sugar can **rotate** in the pocket so that the returning hydride adds to the opposite face of C4 — a **nonstereospecific hydride transfer** that inverts the C4 configuration. Lysine lowers the pK_a of the tyrosine phenol/positions NAD⁺; the active site accommodates both glucose and galactose configurations mainly through water rearrangement.

Supporting literature: *"These include practically irreversible binding of NAD, nonstereospecific hydride transfer, uridine nucleotide-induced activation of NAD, Tyr149 as a base catalyst"* ([PMID: 23339688](https://pubmed.ncbi.nlm.nih.gov/23339688/)); the two-part chemistry involves *"the abstraction of a proton from the 4'-hydroxyl group of glucose or galactose by an active site base and the rotation of a 4-ketopyranose intermediate in the active site pocket"* ([PMID: 9174344](https://pubmed.ncbi.nlm.nih.gov/9174344/)); and *"UDP-galactose 4-epimerase belongs to a family of enzymes known as the short-chain dehydrogenases, which contain a characteristic Tyr-Lys couple thought to be important for catalysis"* ([PMID: 8931134](https://pubmed.ncbi.nlm.nih.gov/8931134/)).

### F009 — Quantitative ortholog evidence: 43% identity to characterized *E. coli* GalE with a fully conserved catalytic triad

A direct pairwise comparison anchors the annotation quantitatively. Global (Needleman–Wunsch) alignment gives:

| Pair | Global identity |
|---|---|
| PP_3129 (Q88I72) vs *E. coli* GalE (P09147) | **43.3%** |
| PP_3129 vs paralog PP_0501 | 35.1% |
| PP_0501 vs *E. coli* GalE | 33.2% |

The alignment maps the *E. coli* catalytic triad **Ser124/Tyr149/Lys153 exactly onto PP_3129 Ser111/Tyr135/Lys139** (no gaps at these positions), and the Rossmann GxxGxxG motif (residues 7–13) is conserved. At 43% identity — comfortably above the ~30% threshold generally accepted for confident functional transfer between enzymes — and with the complete catalytic apparatus conserved, functional assignment as a bona fide UDP-glucose 4-epimerase is secure. Notably, PP_3129 is more similar to *E. coli* GalE than to its own paralog PP_0501, indicating the two *P. putida* paralogs have diverged.

### F004 — Group-1 substrate specificity (UDP-Glc/Gal, not UDP-GlcNAc/GalNAc)

GalE enzymes are classified into three groups by substrate specificity: *"GalEs have been classified into three groups based on substrate specificity: group 1 prefers UDP-Glc/Gal, group 3 prefers UDP-GlcNAc/GalNAc, and group 2 has comparable activities for both types of the substrates"* ([PMID: 33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/)). Q88I72 carries the diagnostic IPR005886 (UDP_glucose_4-epimerase) TIGRFAM signature — the same assignment as enteric group-1 enzymes such as *E. coli* GalE — and lacks the enlarged/mobile active-site loop that allows human and group-2 enzymes to accommodate the bulky N-acetyl group. The structural determinant is established: *"Greater active site loop mobility in human GALE compared to the equivalent loop in Escherichia coli GALE explains why the former can catalyze the interconversion of UDP-N-acetylga[lactosamine]…"* ([PMID: 23732289](https://pubmed.ncbi.nlm.nih.gov/23732289/)). PP_3129 is therefore inferred to be **UDP-Glc/UDP-Gal-specific**. (This is an inference by homology/domain diagnostics; no direct enzymology on the *P. putida* protein exists.)

### F003 — Cytoplasmic localization and role in supplying UDP-galactose for cell-surface glycoconjugates

The enzyme functions in the **cytoplasm**. The 321-residue protein has a soluble SDR fold with no signal peptide or transmembrane segment, consistent with the cytosolic location where nucleotide-sugar interconversion occurs. Functionally, GalE catalyzes the last step of the Leloir pathway and supplies the UDP-galactose precursor for extracellular glycans: *"UDP-galactose 4-epimerase (GalE) catalyses the last step in the Leloir pathway of galactose metabolism and provides precursor for the biosynthesis of extracellular LPS and capsule"* ([PMID: 20461162](https://pubmed.ncbi.nlm.nih.gov/20461162/)). Knockout evidence in Gram-negative pathogens links GalE-derived nucleotide sugars to O-antigen synthesis: in Shiga toxin–producing *E. coli*, *"galE plays a significant roles in O-antigen biosynthesis and contributes to STEC pathogenicity"* ([PMID: 40783826](https://pubmed.ncbi.nlm.nih.gov/40783826/)).

### F005 & F008 — Genomic context and absent catabolic Leloir genes reframe GalE as a biosynthetic UDP-galactose supplier

Two genomic observations specific to KT2440 sharpen the physiological interpretation:

1. **Genomic embedding in an EPS cluster (F005).** In the KT2440 genome, PP_3129 *galE* is flanked by PP_3126 (polysaccharide export protein), PP_3127 (exopolysaccharide transport protein), PP_3128 (exopolysaccharide biosynthesis/transport protein), and PP_3132 (polysaccharide transporter). The gene maps to KEGG pathways ppu00052 (Galactose metabolism), ppu00520 (Amino sugar and nucleotide sugar metabolism), and ppu01250 (Biosynthesis of nucleotide sugars); orthology K01784 (EC 5.1.3.2). The gene occupies position complement(3541757..3542722), 966 nt / 321 aa, protein AAN68737. Its location within a polysaccharide biosynthesis/export operon argues that its primary output — UDP-galactose — feeds cell-surface glycan synthesis.

2. **Missing galK and galT (F008).** KEGG ortholog mapping shows that KT2440 **lacks galactokinase (galK, K00849) and Gal-1-P uridylyltransferase (galT, K00965)**, while retaining galU (K00963, PP_3821), pgm (K01835, PP_3578), and galM (K01785, PP_1165), plus **two galE paralogs** (PP_3129 in the EPS cluster and PP_0501 at a separate locus, both K01784). Without galK and galT, exogenous galactose cannot be funneled into UDP-Gal via the canonical catabolic Leloir route. Therefore, rather than running catabolically (galactose → Gal-1-P → UDP-Gal → UDP-Glc → glycolysis), GalE in KT2440 most plausibly runs **anabolically**: UDP-glucose (from glucose-1-P via galU) is epimerized to UDP-galactose to supply glycan biosynthesis.

### F007 — Dual physiological logic across bacteria: catabolism, anabolism, and UDP-Gal toxicity

Across bacteria, GalE sits at a metabolic branch-point and its product UDP-galactose is both an EPS precursor and, when it accumulates, a toxic metabolite. In *Bacillus subtilis*, galE deletion causes galactose sensitivity because UDP-galactose accumulates: *"We propose that UDP-galactose is the toxic galactose metabolite and that it is used in the synthesis of EPS"* ([PMID: 22893383](https://pubmed.ncbi.nlm.nih.gov/22893383/)). In *Acidithiobacillus ferrooxidans*, galE lies in a gal/EPS cluster and supplies EPS precursors: *"The data suggest that A. ferrooxidans is capable of synthesizing the EPS precursors UDP-glucose and UDP-galactose"* ([PMID: 15932984](https://pubmed.ncbi.nlm.nih.gov/15932984/)). This parallels the *P. putida* genomic context and reinforces the biosynthetic interpretation for PP_3129.

---

## Mechanistic Model / Interpretation

### The catalytic cycle

```
                 NAD+ (tightly bound)                 NADH
                     │                                  │
   UDP-Glc ──────────▼──────────►  UDP-4-ketopyranose ──▼── (ring rotates in pocket)
   (C4-OH "down")   Tyr135 abstracts     intermediate       hydride returns to
                    C4-OH proton;                            OPPOSITE face of C4
                    C4-H → NAD+                                    │
                                                                  ▼
                                                             UDP-Gal
                                                            (C4-OH "up")
   Net: no consumption of NAD+/NADH; only C4 stereochemistry inverted.
   Catalytic triad: Ser111 (H-bond/positioning) · Tyr135 (base) · Lys139 (lowers Tyr pKa, positions NAD+)
```

The redox-neutrality — transient oxidation followed by re-reduction with the *same* tightly held cofactor — is the elegant hallmark of this SDR enzyme. Substrate discrimination between the glucose and galactose configurations is subtle, handled largely by reorganization of active-site water rather than by large conformational change; the enzyme's inability to bind the N-acetylated substrates (group-3/group-2 activity) reflects a comparatively rigid, small active-site loop.

### Metabolic placement in *P. putida* KT2440

```
      glucose-1-phosphate
             │  galU (PP_3821, UTP:Glc-1-P uridylyltransferase)
             ▼
        UDP-glucose  ◄────────────────┐
             │                        │  pgm (PP_3578, phosphoglucomutase)
             │  galE (PP_3129)  ⇌     │
             ▼   [4-epimerization]    │
        UDP-galactose                 │
             │                        │
             ▼                        │
   ┌─────────────────────────────┐    │
   │ LPS / O-antigen             │    │   (KT2440 LACKS galK, galT →
   │ Exopolysaccharide (EPS)     │    │    no catabolic galactose entry;
   │ [PP_3126–3132 export cluster]│   │    GalE runs biosynthetically)
   └─────────────────────────────┘
```

Because KT2440 has no galactokinase (galK) or Gal-1-P uridylyltransferase (galT), the classic catabolic Leloir loop is broken. The retained enzymes galU, pgm, galM, and two galE paralogs point to a network geared toward **nucleotide-sugar biosynthesis** rather than galactose catabolism. GalE (PP_3129), sitting inside an EPS export operon, is therefore best interpreted as the **galactosyl-donor supplier** for surface glycan assembly — the flux runs predominantly UDP-Glc → UDP-Gal.

### Two paralogs

KT2440 encodes two K01784-annotated epimerases: PP_3129 (this protein, in the EPS cluster) and PP_0501 (a separate "NAD-dependent epimerase/dehydratase" locus). At 35% mutual identity they have diverged; the EPS-cluster location and higher (43%) identity of PP_3129 to characterized *E. coli* GalE make PP_3129 the stronger candidate for the canonical, glycan-supplying UDP-Glc/Gal epimerase.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/) | *Molecular evolution and functional divergence of UDP-hexose 4-epimerases* | Defines the GalE reaction (UDP-Glc ⇌ UDP-Gal), the transient-keto mechanism, and the 3-group substrate-specificity classification used to place Q88I72 in group 1 |
| [26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/) | *UDP-hexose 4-epimerases: structure, mechanism, substrate specificity* | Places GalE in SDR superfamily/Leloir pathway; documents irreversible NAD binding and nucleotide-induced cofactor activation |
| [21645492](https://pubmed.ncbi.nlm.nih.gov/21645492/) | *Crystal structure of GalE from Pyrobaculum calidifontis* | Structural basis for retention of tightly bound NAD⁺ (NAD-binding loop) |
| [23339688](https://pubmed.ncbi.nlm.nih.gov/23339688/) | *Chemical and stereochemical actions of GalE* | Establishes Tyr149 as base catalyst, nonstereospecific hydride transfer, irreversible NAD binding |
| [9174344](https://pubmed.ncbi.nlm.nih.gov/9174344/) | *Structural analysis of UDP-sugar binding to E. coli GalE* | Defines base-mediated C4-OH proton abstraction + rotation of 4-ketopyranose intermediate |
| [8931134](https://pubmed.ncbi.nlm.nih.gov/8931134/) | *High-resolution structure of GalE with UDP-phenol* | Confirms conserved SDR Tyr-Lys catalytic couple (Tyr135/Lys139 in PP_3129) |
| [23732289](https://pubmed.ncbi.nlm.nih.gov/23732289/) | *Dynamics of wildtype vs V94M human GALE* | Active-site loop mobility distinguishes group-1 (E. coli-type) from broader-specificity GALEs |
| [20461162](https://pubmed.ncbi.nlm.nih.gov/20461162/) | *Cloning/modeling of galE from Aeromonas hydrophila* | Links GalE's last-step Leloir reaction to provision of UDP-Gal precursor for LPS and capsule |
| [40783826](https://pubmed.ncbi.nlm.nih.gov/40783826/) | *GalE in LPS O-antigen synthesis, STEC O5* | Knockout evidence that galE-derived nucleotide sugars are required for O-antigen/LPS |
| [22893383](https://pubmed.ncbi.nlm.nih.gov/22893383/) | *Galactose metabolism in B. subtilis biofilm* | GalE product UDP-Gal is both toxic metabolite and EPS precursor — links catabolism/anabolism |
| [15932984](https://pubmed.ncbi.nlm.nih.gov/15932984/) | *EPS precursor gene cluster in A. ferrooxidans* | galE within a gal/EPS cluster supplies UDP-Glc/UDP-Gal EPS precursors — parallels KT2440 context |

Supporting structural context also comes from crystallographic studies of GalE and GalE-like enzymes ([PMID: 31366978](https://pubmed.ncbi.nlm.nih.gov/31366978/), *Bifidobacterium longum* broad-specificity GalE; [PMID: 20587332](https://pubmed.ncbi.nlm.nih.gov/20587332/), monomeric *Aeromonas hydrophila* GalE active site; [PMID: 11478886](https://pubmed.ncbi.nlm.nih.gov/11478886/), the homologous Ser/Thr–Tyr–Lys triad in dTDP-glucose 4,6-dehydratase). An important comparative caution: in *Vibrio vulnificus* biotype 2 it was *gne* (UDP-GalNAc 4-epimerase), not *galE*, that proved essential for LPS and virulence ([PMID: 18227162](https://pubmed.ncbi.nlm.nih.gov/18227162/)) — a reminder that GalE contributions to surface glycans are organism- and glycan-specific.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on the *P. putida* protein.** Every functional claim about Q88I72 rests on homology, domain diagnostics, and sequence-mapped catalytic residues. There is no published enzymology (kinetics, k_cat/K_m, substrate panel), crystal structure, or knockout phenotype for PP_3129 specifically. The group-1 (UDP-Glc/Gal-only) assignment is an inference, not a measurement.

2. **Direction of flux is inferred, not demonstrated.** The "biosynthetic" interpretation follows from the absence of galK/galT and the EPS-cluster genomic context, but the enzyme is intrinsically reversible; in vivo net flux direction has not been measured (e.g., by ¹³C flux analysis) in KT2440.

3. **Paralog ambiguity.** KT2440 carries two K01784 epimerases (PP_3129 and PP_0501). Their respective in vivo roles, substrate ranges, and possible functional redundancy are unresolved. Which paralog dominates UDP-Gal supply for LPS vs EPS is unknown.

4. **Localization inferred from sequence.** Cytoplasmic localization is deduced from the soluble SDR fold and absence of a signal peptide/TM segment; it has not been experimentally verified (e.g., fractionation) for this protein.

5. **Glycan destination unmapped.** Which specific KT2440 surface glycans (O-antigen structures, specific EPS such as alginate/Pea/Bce-type polymers) actually incorporate GalE-derived galactose has not been established.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express His-tagged PP_3129, confirm bound NAD⁺, and measure epimerase activity and kinetics on UDP-Glc/UDP-Gal versus UDP-GlcNAc/UDP-GalNAc to test the group-1 specificity prediction directly.

2. **Structure determination.** Solve the crystal structure (or high-confidence AlphaFold model + docking) to verify the Ser111/Tyr135/Lys139 triad geometry and active-site loop rigidity that underlie substrate selectivity.

3. **Genetics.** Construct single (ΔPP_3129, ΔPP_0501) and double knockouts; assay for growth on galactose, LPS/O-antigen profile changes (SDS-PAGE/silver stain), EPS/biofilm phenotypes, and any UDP-Gal-accumulation toxicity — mirroring the *B. subtilis* and STEC studies.

4. **Complementation and paralog dissection.** Cross-complement the two paralogs and complement *E. coli* ΔgalE to quantify functional equivalence and resolve redundancy.

5. **Flux analysis.** Use ¹³C-labeled substrates and metabolomics to determine the net in vivo direction of the UDP-Glc ⇌ UDP-Gal reaction in KT2440 and confirm the predicted biosynthetic bias.

6. **Glycan tracing.** Combine glycan compositional analysis of LPS/EPS from wild-type vs mutant strains to pinpoint which surface glycoconjugates depend on GalE-derived galactose.

---

## Conclusion

*galE* (PP_3129; Q88I72) of *P. putida* KT2440 encodes a cytoplasmic, NAD⁺-dependent **UDP-glucose 4-epimerase** (EC 5.1.3.2) that reversibly epimerizes C4 to interconvert UDP-glucose and UDP-galactose, using a tightly bound NAD⁺, a catalytic Ser111/Tyr135/Lys139 triad, and a transient UDP-4-ketopyranose intermediate with nonstereospecific hydride return. Its substrate specificity is group-1 (UDP-Glc/Gal). Because KT2440 lacks the catabolic Leloir enzymes galK and galT, and because PP_3129 lies within an exopolysaccharide biosynthesis/export cluster, the enzyme most likely operates **biosynthetically** — supplying UDP-galactose (from UDP-glucose via pgm/galU) as the galactosyl donor for LPS/O-antigen and exopolysaccharide assembly. All conclusions rest on strong homology and genomic evidence (43% identity to characterized *E. coli* GalE with a fully conserved catalytic apparatus); direct experimental characterization of the *P. putida* protein remains the principal knowledge gap.


## Artifacts

- [OpenScientist final report](galE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](galE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33171387
2. PMID:26162744
3. PMID:21645492
4. PMID:23339688
5. PMID:9174344
6. PMID:8931134
7. PMID:23732289
8. PMID:20461162
9. PMID:40783826
10. PMID:22893383
11. PMID:15932984
12. PMID:31366978
13. PMID:20587332
14. PMID:11478886
15. PMID:18227162