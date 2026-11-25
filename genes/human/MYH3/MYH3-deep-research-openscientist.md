---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T01:31:04.423898'
end_time: '2026-10-16T01:44:18.104653'
duration_seconds: 793.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MYH3
  gene_symbol: MYH3
  uniprot_accession: P11055
  protein_description: 'RecName: Full=Myosin-3; AltName: Full=Muscle embryonic myosin
    heavy chain; AltName: Full=Myosin heavy chain 3; AltName: Full=Myosin heavy chain,
    fast skeletal muscle, embryonic; AltName: Full=SMHCE;'
  gene_info: Name=MYH3;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class myosin-kinesin ATPase
  protein_domains: Kinesin_motor_dom_sf. (IPR036961); Myosin_head_motor_dom-like.
    (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail. (IPR002928); MYSc_Myh3. (IPR036000)
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
  path: MYH3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MYH3-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P11055
- **Protein Description:** RecName: Full=Myosin-3; AltName: Full=Muscle embryonic myosin heavy chain; AltName: Full=Myosin heavy chain 3; AltName: Full=Myosin heavy chain, fast skeletal muscle, embryonic; AltName: Full=SMHCE;
- **Gene Information:** Name=MYH3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class myosin-kinesin ATPase
- **Key Domains:** Kinesin_motor_dom_sf. (IPR036961); Myosin_head_motor_dom-like. (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail. (IPR002928); MYSc_Myh3. (IPR036000)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MYH3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MYH3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MYH3** (gene ID: MYH3, UniProt: P11055) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MYH3 (Myosin-3 / Embryonic Myosin Heavy Chain): Functional Annotation Report

**Gene:** MYH3 | **UniProt:** [P11055](https://www.uniprot.org/uniprotkb/P11055/entry) | **Organism:** *Homo sapiens* (Human)
**Protein:** Myosin-3; Muscle embryonic myosin heavy chain; Myosin heavy chain, fast skeletal muscle, embryonic (SMHCE)
**Protein family:** TRAFAC class myosin-kinesin ATPase superfamily

---

## Summary

**MYH3 encodes the heavy chain of embryonic myosin II, the ATP-powered molecular motor that drives contraction in developing and regenerating skeletal muscle.** Its primary molecular function is enzymatic and mechanical: the globular N-terminal motor domain is an actin-activated Mg²⁺-ATPase (EC 3.6.4.1) that hydrolyzes ATP (ATP + H₂O → ADP + inorganic phosphate) and transduces the released chemical energy into directed mechanical force. This force is produced by a lever-arm "power stroke" exerted against filamentous (F-)actin during the cyclical attachment–detachment of myosin cross-bridges. The long C-terminal α-helical coiled-coil tail dimerizes and packs into the bipolar sarcomeric thick filament, giving the protein a dual enzymatic and structural role.

The protein carries out its function **intracellularly, within the striated-muscle sarcomere** — specifically in the A-band thick filament of the contractile apparatus. It operates downstream of the Ca²⁺/troponin–tropomyosin thin-filament switch: cytosolic Ca²⁺ elevation relieves steric blocking of actin, permitting MYH3 motor heads to form force-generating cross-bridges. MYH3 is developmentally restricted, expressed transiently during embryonic and fetal myogenesis and re-expressed during adult muscle regeneration, where it serves as a hallmark marker of regenerating fibers. Its contractile activity during fetal life is essential not only for muscle maturation (myofibrillogenesis) but also for proper joint and craniofacial morphogenesis.

The functional importance of MYH3 is underscored by human genetics: dominant missense mutations in the motor domain that slow ATP hydrolysis and impair cross-bridge detachment cause the distal arthrogryposis spectrum — Freeman-Sheldon syndrome (DA2A), Sheldon-Hall syndrome (DA2B), and multiple pterygium syndrome — while other MYH3 variants cause spondylocarpotarsal synostosis and related bony-fusion disorders, the latter revealing an additional postnatal regulatory role for embryonic myosin in TGFβ signaling. Transcription of the gene is temporally controlled by a defined promoter-enhancer and a Zeb1/Tle3 regulatory circuit during myogenic differentiation and regeneration.

---

## Key Findings

### 1. MYH3 is the motor (ATPase) subunit of sarcomeric myosin II that generates contractile force

The core molecular function of MYH3 is as the force-generating motor of embryonic/fetal skeletal muscle myosin II. The protein belongs to the TRAFAC class myosin-kinesin ATPase superfamily (UniProt P11055) and contains a Myosin head motor domain (IPR001609). Direct biochemical characterization of the recombinant human embryonic myosin motor domain by **Walklate et al. (2016)** measured actin-activated ATPase kinetics and showed that wild-type embryonic myosin is kinetically similar to the slow type I/β-cardiac myosin, based on the rate constant for ADP release and ADP affinity for actin-myosin [PMID: 26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/). This places MYH3 at the slow end of the contractile-speed spectrum among sarcomeric myosins.

More generally, myosins are ATP-powered, force-generating motor proteins involved in cardiac and muscle contraction [PMID: 39374027](https://pubmed.ncbi.nlm.nih.gov/39374027/). Single-molecule and molecular-dynamics studies of class II myosins confirm that force is generated by the load-sensitive detachment of strongly bound actomyosin states during the cross-bridge cycle, coupled to ATP hydrolysis and phosphate/ADP release. MYH3 is therefore the enzymatic and mechanical effector that converts chemical energy into the mechanical work of muscle shortening.

> **Evidence (direct):** *"Our data suggest that the WT embryonic myosin motor is similar in contractile speed to the slow type I/β cardiac based on the rate constant for ADP release and ADP affinity for actin-myosin."* — Walklate et al., [PMID: 26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/)

### 2. The precise catalyzed reaction: actin-activated Mg²⁺-ATP hydrolysis coupled to a lever-arm power stroke

MYH3's enzymatic activity is best described as an actin-activated Mg²⁺-ATPase (EC 3.6.4.1): **ATP + H₂O → ADP + Pᵢ**, with the released chemical energy transduced into directed mechanical force on the actin thin filament. Myosins use a conserved motor mechanism that couples the chemical cycle (ATP binding → hydrolysis → Pᵢ release → ADP release) to a large swing of the force-generating lever arm, the "power stroke" [PMID: 29235081](https://pubmed.ncbi.nlm.nih.gov/29235081/). The S1 head comprises a catalytic (ATPase/actin-binding) domain, a converter domain, and the lever arm. After ATP binding, a "recovery stroke" repositions catalytic residues for hydrolysis and re-cocks the lever arm; subsequent actin binding of the ADP·Pᵢ state triggers the power stroke that gates phosphate release.

> **Evidence:** *"...have similar force-producing mechanisms that are coupled with the chemical cycles of ATP binding, hydrolysis, Pi release and subsequent ADP release"* and *"The force is generated through conformational changes in the motor domain during Pi release and ATP binding in myosin and kinesin, respectively, and then converted into the rotation of the lever arm or neck linker (referred to as a power stroke)"* — [PMID: 29235081](https://pubmed.ncbi.nlm.nih.gov/29235081/)

This defines the mechanochemical heart of MYH3: it is a chemomechanical energy transducer, not merely a passive structural protein.

### 3. Subcellular localization: the sarcomeric thick filament, developmentally restricted

MYH3 (MyHC-emb) is a **sarcomeric** myosin whose molecular structure allows thick-filament assembly [PMID: 26970499](https://pubmed.ncbi.nlm.nih.gov/26970499/). It therefore localizes to the A-band thick filament of the striated-muscle sarcomere. Its expression is developmentally restricted: embryonic MyHC (MYH3) and neonatal MyHC (MYH8) are transiently expressed during embryonic and fetal development and disappear shortly after birth as adult fast and slow myosins become prevalent. However, developmental myosins persist into adulthood in specialized muscles — the extraocular and jaw-closing (masticatory) muscles, and the intrafusal fibers of muscle spindles — and are re-expressed during muscle regeneration, where they provide a specific marker of regenerating fibers [PMID: 26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/).

> **Evidence:** *"These myosin isoforms are transiently expressed during embryonic and fetal development and disappear shortly after birth... However, developmental myosins persist throughout adult stages in specialized muscles, such as the extraocular and jaw-closing muscles, and in the intrafusal fibers of the muscle spindles. These myosins are re-expressed during muscle regeneration and provide a specific marker of regenerating fibers"* — [PMID: 26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/)

### 4. Quaternary structure: the heavy chain of a hexameric myosin II in the chromosome-17 MYH cluster

Functional myosin II is a **hexamer**: two heavy chains (MYH3) plus two essential and two regulatory light chains. Each heavy chain contributes a globular motor head, a lever-arm/neck region that binds the light chains, and a long α-helical coiled-coil rod that dimerizes and packs into the bipolar thick filament. Cryo-EM visualization of double-headed myosin II bound to F-actin localized the largest strain-dependent structural change to the heavy-chain segment between the essential and regulatory light chains [PMID: 37414375](https://pubmed.ncbi.nlm.nih.gov/37414375/) — i.e., the lever-arm/neck. This modular architecture matches the UniProt domain annotation: Myosin S1 N-terminal (IPR008989), motor domain (IPR001609), and Myosin tail (IPR002928).

The gene is a member of the fast/developmental MYH gene cluster on human chromosome 17 (syntenic to mouse chromosome 11), which also contains MYH1, MYH2, MYH4, MYH8, and MYH13 [PMID: 12110653](https://pubmed.ncbi.nlm.nih.gov/12110653/). Phylogenetic analysis indicates that the motor (head) and rod (tail) domains of these cluster myosins evolved under different selective pressures — an evolutionary signature of their distinct enzymatic versus structural functions.

> **Evidence:** *"a member of the fast/developmental MYH gene cluster on human chromosome 17 and the syntenic MYH cluster on mouse chromosome 11"* — [PMID: 12110653](https://pubmed.ncbi.nlm.nih.gov/12110653/)

*Note: the cryo-EM study [PMID: 37414375] examines myosin II generally; its relevance to MYH3 is by family homology rather than direct study of the MYH3 protein.*

### 5. Position in the Ca²⁺-regulated contractile pathway: downstream of troponin–tropomyosin thin-filament gating

MYH3 operates within the Ca²⁺-regulated actomyosin cross-bridge system of the sarcomere, acting as the force-generating effector whose access to actin is gated by the troponin–tropomyosin complex. Striated-muscle contraction is initiated by a rise in cytosolic Ca²⁺; Ca²⁺ binding to troponin C shifts the thin-filament on–off equilibrium, moving tropomyosin to expose myosin-binding sites on actin. Tropomyosin occupies one of three meta-stable configurations on actin, regulating access of myosin motorheads to their actin-binding sites and thus the cross-bridge cycle [PMID: 37249525](https://pubmed.ncbi.nlm.nih.gov/37249525/). Partial relief of steric inhibition allows weak binding of myosin heads to actin, which then transition to strong actin-bound configurations that fully activate the thin filament [PMID: 37249525](https://pubmed.ncbi.nlm.nih.gov/37249525/).

> **Evidence:** *"Tropomyosin is well-known to occupy either of three meta-stable configurations on actin, regulating access of myosin motorheads to their actin-binding sites and thus the crossbridge cycle."* and *"This partially relieves the steric inhibition and allows weak binding of myosin heads to actin, which then transition to strong actin-bound configurations, fully activating the thin filament."* — [PMID: 37249525](https://pubmed.ncbi.nlm.nih.gov/37249525/)

This places MYH3's motor head firmly within the canonical troponin–tropomyosin-gated, Ca²⁺-dependent contractile biochemical pathway.

### 6. Developmental biological role: essential for fetal myogenesis and myofibrillogenesis

MyHC-emb (MYH3) regulates skeletal muscle differentiation during mammalian development (Agarwal et al., 2020). Experimentally, patient-derived cells carrying the p.Thr178Ile MYH3 mutation showed delayed myofibrillogenesis and atrophic myotubes — although sarcomeres were still structured — alongside reduced embryonic MyHC and increased MuRF1 ubiquitin ligase, indicating enhanced protein degradation [PMID: 26544689](https://pubmed.ncbi.nlm.nih.gov/26544689/). This demonstrates a direct structural/developmental role for MYH3 in assembling the nascent contractile apparatus.

Critically, the contractile activity of MYH3 during fetal life shapes the skeleton and face. Mutations in MYH3 or MYH8 cause distal arthrogryposis syndromes characterized by congenital joint contractures and orofacial dysmorphisms, supporting the importance of muscle contractile activity and fetal body movements in joint development and in shaping the form of the face during fetal development [PMID: 26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/).

> **Evidence:** *"We also found delayed myofibrillogenesis and atrophic myotubes but structured sarcomeres."* — [PMID: 26544689](https://pubmed.ncbi.nlm.nih.gov/26544689/)
> *"Mutations in MYH3 or MYH8 are responsible for distal arthrogryposis syndromes... supporting the importance of muscle contractile activity and body movements in joint development and in shaping the form of the face during fetal development."* — [PMID: 26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/)

### 7. Disease genetics: dominant motor-domain mutations cause the distal arthrogryposis spectrum

Heterozygous variants in MYH3 cause the dominantly inherited distal arthrogryposis conditions Freeman-Sheldon syndrome (DA2A, the most severe), Sheldon-Hall syndrome (DA2B), and multiple pterygium syndrome [PMID: 38856159](https://pubmed.ncbi.nlm.nih.gov/38856159/). Bi-allelic (recessive) MYH3 variants have also been shown to cause recessively inherited arthrogryposis, and MYH3 variants underlie Contractures-Pterygia-Spondylocarpotarsal Fusion syndromes with bony fusions. These disease associations reflect the gene's indispensable developmental function and the sensitivity of the motor mechanism to point mutations.

> **Evidence:** *"Heterozygous variants in MYH3 have been identified to cause the dominantly-inherited distal arthrogryposis conditions, Freeman-Sheldon syndrome, Sheldon-Hall syndrome, and multiple pterygium syndrome."* — [PMID: 38856159](https://pubmed.ncbi.nlm.nih.gov/38856159/)

### 8. Mechanism of disease: mutations impair ATPase cycling and cross-bridge detachment

The disease mutations illuminate the precise mechanochemical role of MYH3. The three most common Freeman-Sheldon syndrome mutations (R672H, R672C, T178I) in the embryonic myosin motor cause dramatic kinetic changes — most notably slowing the apparent ATP hydrolysis step 5–9-fold, producing a longer-lived detached state and a 2–35-fold reduction in the Vmax of the ATPase, i.e., slower cycling [PMID: 26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/). At the tissue level, adult muscle cells and myofibrils from R672C patients showed reduced specific force, prolonged and incomplete relaxation, and elevated residual force. These observations are collectively explained by a small subpopulation of myosin cross-bridges with greatly reduced detachment kinetics, producing slower and less complete deactivation of thin filaments at the end of contractions [PMID: 25740846](https://pubmed.ncbi.nlm.nih.gov/25740846/).

Independent *Drosophila* models (Guo et al., 2020) of DA1 (F437I) and DA2B (A234T) myosin mutations recapitulated the human severity hierarchy (DA2B more severe than DA1) and showed reduced ATPase and in vitro motility with increased stiffness/force and enhanced actin affinity — pointing to an "enhanced actin affinity"/prolonged actomyosin interaction mechanism for contractures [PMID: 32799913](https://pubmed.ncbi.nlm.nih.gov/32799913/).

> **Evidence:** *"All three FSS mutations show dramatic changes in kinetic properties, most notably the slowing of the apparent ATP hydrolysis step (reduced 5-9-fold), leading to a longer lived detached state and a slowed Vmax of the ATPase (2-35-fold), indicating a slower cycling time."* — [PMID: 26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/)
> *"These observations can be collectively explained by a small subpopulation of myosin cross-bridges with greatly reduced detachment kinetics, resulting in a slower and less complete deactivation of thin filaments at the end of contractions."* — [PMID: 25740846](https://pubmed.ncbi.nlm.nih.gov/25740846/)

### 9. A postnatal regulatory role in TGFβ signaling

Beyond its canonical contractile function, MYH3 has a distinct postnatal role connected to skeletal patterning. Exome sequencing of spondylocarpotarsal synostosis (SCT) patients negative for FLNB mutations identified heterozygous MYH3 mutations causing autosomal dominant SCT, characterized by progressive vertebral, carpal, and tarsal fusions. Cells transfected with the MYH3 missense mutations showed reduced TGFβ signaling, revealing a regulatory role for embryonic myosin in the TGFβ pathway [PMID: 28205584](https://pubmed.ncbi.nlm.nih.gov/28205584/). In wild-type mice, embryonic myosin was persistently expressed postnatally in the small muscles joining the neural arches of the spine, suggesting that loss of myosin function in these paraspinal muscles contributes to the vertebral fusions.

> **Evidence:** *"Cells transfected with the MYH3 missense mutations had reduced TGFβ signaling, revealing a regulatory role for embryonic myosin in the TGFβ signaling pathway."* and *"In wild-type mice, there was persistent postnatal expression of embryonic myosin in the small muscles joining the neural arches of the spine suggesting that loss of myosin function in these muscles contribute to the disease."* — [PMID: 28205584](https://pubmed.ncbi.nlm.nih.gov/28205584/)

### 10. Transcriptional regulation: a dedicated promoter-enhancer and a Zeb1/Tle3 circuit

Myh3 transcription is driven by a defined cis-regulatory element and temporally controlled by specific trans-factors. Kumar et al. (2023) identified a 4,230 bp promoter-enhancer region (sequences flanking the Myh3 TATA-box) that drives Myh3 transcription in vitro during C2C12 myogenic differentiation and in vivo during muscle regeneration [PMID: 37392376](https://pubmed.ncbi.nlm.nih.gov/37392376/). Zeb1 (zinc-finger E-box binding homeobox 1) and Tle3 (Transducin-like Enhancer of Split 3) are crucial, interacting trans-factors that differentially regulate Myh3 expression: loss of Zeb1 accelerates differentiation, whereas Tle3 depletion impairs it, with Tle3 acting upstream of Zeb1 (partly via miR-200c). Additionally, miR-501 has been identified as a regulator of MYH3 induction during muscle regeneration [PMID: 27707793](https://pubmed.ncbi.nlm.nih.gov/27707793/).

> **Evidence:** *"We identify a 4230 bp promoter-enhancer region that drives Myh3 transcription in vitro during C2C12 myogenic differentiation and in vivo during muscle regeneration"* and *"Zinc-finger E-box binding homeobox 1 (Zeb1) and Transducin-like Enhancer of Split 3 (Tle3) proteins are crucial trans-factors that interact and differentially regulate Myh3 expression"* — [PMID: 37392376](https://pubmed.ncbi.nlm.nih.gov/37392376/)

---

## Mechanistic Model / Interpretation

MYH3 can be understood as a **modular chemomechanical machine** embedded in a highly regulated structural and developmental context. The following model synthesizes the findings.

### Molecular architecture (single heavy chain)

```
N-terminus                                                     C-terminus
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│  MOTOR / HEAD   │  CONVERTER + │          COILED-COIL ROD (TAIL)        │
│  (S1 domain)    │  LEVER ARM   │                                        │
│                 │  (neck)      │                                        │
│ • ATP binding   │ • binds ELC  │ • dimerizes two heavy chains           │
│ • ATP hydrolysis│   + RLC      │ • packs into bipolar THICK FILAMENT    │
│ • actin binding │ • amplifies  │   (A-band of sarcomere)                │
│ • power stroke  │   head motion│                                        │
│ IPR001609       │ IPR008989    │ IPR002928                              │
└─────────────────┴──────────────┴───────────────────────────────────────┘
```

Two heavy chains + 2 essential (ELC) + 2 regulatory (RLC) light chains = **hexameric myosin II**.

### The actomyosin cross-bridge cycle (enzymatic function)

```
        ATP binds
  A·M  ─────────────►  M·ATP        (actin released; cross-bridge detaches)
   ▲   (detachment)       │
   │                      │ hydrolysis (slowed 5–9× by FSS mutations)
   │ ADP release          ▼
  A·M·ADP  ◄───────  A·M·ADP·Pi  ◄── M·ADP·Pi   (re-primed / recovery stroke)
       ▲   POWER STROKE        actin rebinding
       │   (force on actin;    (gated by Ca²⁺/troponin–tropomyosin)
       └── Pi release ─────────────┘
```

- **Chemistry:** ATP + H₂O → ADP + Pᵢ (actin-activated Mg²⁺-ATPase, EC 3.6.4.1)
- **Mechanics:** product release drives the lever-arm swing (power stroke) → F-actin is pulled toward the filament center → sarcomere shortens
- **Regulation (upstream gate):** cytosolic Ca²⁺ → troponin C → tropomyosin shift → actin sites exposed → MYH3 heads permitted to cycle

### Regulatory and developmental context

```
  Zeb1 / Tle3 / miR-200c / miR-501  ──►  Myh3 promoter-enhancer (4230 bp)
                                             │
                                             ▼
                              MYH3 (MyHC-emb) protein expressed
                                 in fetal & regenerating muscle
                                             │
                 ┌───────────────────────────┼───────────────────────────┐
                 ▼                            ▼                           ▼
      Fetal muscle contraction      Myofibrillogenesis /       Postnatal paraspinal
      → joint & craniofacial        sarcomere assembly         muscle → TGFβ signaling
        morphogenesis                                          → vertebral patterning
```

### Genotype–phenotype logic

Dominant motor-domain mutations act by a **gain-of-function / altered-kinetics** mechanism rather than simple loss of expression: they slow ATP hydrolysis, prolong the strongly bound actomyosin state, and impair cross-bridge detachment. During fetal life this produces hypercontractile or poorly relaxing muscle, which mechanically restricts developing joints → congenital contractures (arthrogryposis). The severity hierarchy (DA2A/Freeman-Sheldon > DA2B/Sheldon-Hall > DA1) is mirrored in the magnitude of the biochemical kinetic defects, in both human motor-domain assays and *Drosophila* models. A separate class of MYH3 effects — loss of embryonic myosin function in postnatal paraspinal muscles with reduced TGFβ signaling — produces bony-fusion phenotypes (spondylocarpotarsal synostosis).

### Comparative summary of the key functional evidence

| Aspect | Finding | Primary evidence (PMID) | Evidence type |
|---|---|---|---|
| Catalyzed reaction | Actin-activated Mg²⁺-ATPase; ATP → ADP + Pᵢ coupled to power stroke | [29235081](https://pubmed.ncbi.nlm.nih.gov/29235081/), [26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/) | Structural mechanism + direct kinetics |
| Contractile speed | Slow, type I/β-cardiac-like | [26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/) | Recombinant motor-domain kinetics |
| Localization | Sarcomeric A-band thick filament | [26970499](https://pubmed.ncbi.nlm.nih.gov/26970499/) | Molecular structure/biochemistry |
| Expression timing | Embryonic/fetal; regenerating & specialized adult muscle | [26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/) | Review of expression studies |
| Quaternary structure | Heavy chain of hexameric myosin II; chr17 MYH cluster | [37414375](https://pubmed.ncbi.nlm.nih.gov/37414375/), [12110653](https://pubmed.ncbi.nlm.nih.gov/12110653/) | Cryo-EM + phylogenetics |
| Regulatory pathway | Downstream of Ca²⁺/troponin–tropomyosin | [37249525](https://pubmed.ncbi.nlm.nih.gov/37249525/) | Structural/biophysical |
| Developmental role | Myofibrillogenesis; joint & facial morphogenesis | [26544689](https://pubmed.ncbi.nlm.nih.gov/26544689/), [26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/) | Patient cells + human genetics |
| Disease mechanism | Slowed ATPase, impaired cross-bridge detachment | [26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/), [25740846](https://pubmed.ncbi.nlm.nih.gov/25740846/) | Kinetics + patient myofibrils |
| Signaling role | Regulates TGFβ pathway (postnatal paraspinal muscle) | [28205584](https://pubmed.ncbi.nlm.nih.gov/28205584/) | Cell transfection + mouse expression |
| Transcriptional control | Promoter-enhancer; Zeb1/Tle3 | [37392376](https://pubmed.ncbi.nlm.nih.gov/37392376/) | Reporter + knockdown studies |

---

## Evidence Base

The conclusions rest on a combination of **direct enzymatic/biophysical measurements on the human protein**, **human disease genetics**, **model-organism functional studies**, and **structural/evolutionary inference**. Key papers:

- **Walklate et al. 2016, *The Most Prevalent Freeman-Sheldon Syndrome Mutations in the Embryonic Myosin Motor Share Functional Defects*** [PMID: 26945064](https://pubmed.ncbi.nlm.nih.gov/26945064/). The single most direct study: recombinant human embryonic (MYH3) motor domain kinetics establish both the wild-type function (slow, β-cardiac-like ATPase) and the mechanism by which FSS mutations impair it (5–9× slower hydrolysis; 2–35× lower Vmax). Strongly supports Findings 1, 2, and 8.

- **Racca et al. 2015, *The embryonic myosin R672C mutation... impairs cross-bridge detachment and cycling in adult skeletal muscle*** [PMID: 25740846](https://pubmed.ncbi.nlm.nih.gov/25740846/). Patient myofibril mechanics tie the molecular kinetic defect to impaired cross-bridge detachment and incomplete relaxation, confirming MYH3's actin cross-bridge role (Findings 5, 8).

- **Schiaffino et al. 2015, *Developmental myosins: expression patterns and functional significance*** [PMID: 26180627](https://pubmed.ncbi.nlm.nih.gov/26180627/). Authoritative review defining MYH3's developmental/tissue localization, regeneration-marker status, and the joint/facial morphogenesis connection (Findings 3, 6, 7).

- **Mascarello et al. 2016, *Expression and identification of 10 sarcomeric MyHC isoforms...*** [PMID: 26970499](https://pubmed.ncbi.nlm.nih.gov/26970499/). Confirms MYH3 as a sarcomeric, thick-filament-forming isoform (Finding 3).

- **Hojjatian et al. 2023, *Double-headed binding of myosin II to F-actin...*** [PMID: 37414375](https://pubmed.ncbi.nlm.nih.gov/37414375/). Cryo-EM localizes strain-dependent structural change to the heavy-chain lever-arm/neck, defining the modular head–lever–tail architecture (Finding 4). *(Studies myosin II generally; relevance to MYH3 is by family homology.)*

- **Schachat & Briggs 2002, *Phylogenetic implications of the superfast myosin in extraocular muscles*** [PMID: 12110653](https://pubmed.ncbi.nlm.nih.gov/12110653/). Places MYH3 in the chromosome-17 fast/developmental MYH cluster and shows head/tail domains evolved under different pressures (Finding 4).

- **Doran/Lehman (Troponin-I-induced tropomyosin pivoting)** [PMID: 37249525](https://pubmed.ncbi.nlm.nih.gov/37249525/). Defines the troponin–tropomyosin gating of myosin-head access to actin that regulates MYH3 (Finding 5).

- **Pokrzywa et al. 2015, *Developmental MYH3 Myopathy...*** [PMID: 26544689](https://pubmed.ncbi.nlm.nih.gov/26544689/). Patient-cell evidence for delayed myofibrillogenesis and atrophic myotubes (Finding 6).

- **Zieba et al. 2017, *A postnatal role for embryonic myosin... MYH3 mutations that alter TGFβ signaling...*** [PMID: 28205584](https://pubmed.ncbi.nlm.nih.gov/28205584/). Establishes the TGFβ-signaling link and postnatal paraspinal localization (Finding 9).

- **Marston et al., *Bi-allelic variants in MYH3 cause recessively-inherited arthrogryposis*** [PMID: 38856159](https://pubmed.ncbi.nlm.nih.gov/38856159/). Defines the dominant and recessive arthrogryposis disease spectrum (Finding 7).

- **Guo et al. 2020, *Drosophila myosin mutants model... DA... enhanced actin affinity mechanism*** [PMID: 32799913](https://pubmed.ncbi.nlm.nih.gov/32799913/). Model-organism confirmation of the severity hierarchy and prolonged-actomyosin-interaction mechanism (Finding 8).

- **Kumar et al. 2023, *Zeb1 and Tle3 are trans-factors...*** [PMID: 37392376](https://pubmed.ncbi.nlm.nih.gov/37392376/). Defines the cis- and trans-regulation of Myh3 transcription (Finding 10).

- **General mechanism references** — [PMID: 29235081](https://pubmed.ncbi.nlm.nih.gov/29235081/) (cytoskeletal motor mechanism) and [PMID: 39374027](https://pubmed.ncbi.nlm.nih.gov/39374027/) (load-dependent actomyosin dissociation) — ground the conserved ATPase/power-stroke mechanism applicable to MYH3.

**Consistency:** The independent lines of evidence converge. Direct human-protein kinetics, patient myofibril mechanics, and a *Drosophila* transgenic model all agree that MYH3's function is ATP-driven cross-bridge cycling and that disease arises from slowed cycling / impaired detachment. No contradictory evidence was identified.

---

## Limitations and Knowledge Gaps

1. **Reliance on homology for some structural claims.** The hexameric architecture and lever-arm strain findings (Finding 4) derive partly from myosin II studies not performed on the MYH3 protein specifically. While myosin II is highly conserved, a direct high-resolution cryo-EM structure of the full human embryonic (MYH3) molecule bound to actin would solidify these inferences.

2. **The TGFβ regulatory mechanism is incompletely defined.** The link between embryonic myosin and TGFβ signaling [PMID: 28205584](https://pubmed.ncbi.nlm.nih.gov/28205584/) is established phenomenologically (reduced signaling in transfected cells; postnatal paraspinal expression), but the molecular intermediary — how a sarcomeric motor protein modulates a cytokine signaling pathway — remains unknown. It is unclear whether this is a direct interaction, a mechanotransduction effect, or an indirect consequence of altered muscle mechanics.

3. **Substrate specificity details.** While the enzyme is clearly an actin-activated Mg²⁺-ATPase, fine details of nucleotide/actin-isoform specificity for the human embryonic isoform (versus adult fast isoforms) are only partially characterized; the slow, β-cardiac-like phenotype is the main quantitative anchor.

4. **In vivo developmental mechanism.** The precise developmental window and quantitative contribution of MYH3 contractile force to specific joint/craniofacial morphogenetic events is inferred largely from disease phenotypes and model organisms rather than from conditional loss-of-function studies in mammals.

5. **Light-chain partners.** The specific essential and regulatory light-chain isoforms that pair with MYH3 in embryonic/fetal muscle, and how they tune its kinetics, were not resolved in this investigation.

6. **No primary data file was analyzed.** This report is a literature- and database-driven functional annotation; no experimental dataset was provided for independent statistical analysis.

---

## Proposed Follow-up Experiments / Actions

1. **High-resolution cryo-EM of the human MYH3 actomyosin complex** in multiple nucleotide states to directly confirm the lever-arm swing geometry and map disease-mutation residues onto force-generating interfaces.

2. **Full transient-kinetic dissection of the recombinant human embryonic myosin S1** across the complete ATPase cycle (ATP binding, hydrolysis, Pᵢ release, ADP release, actin association/dissociation) under load, to quantify each rate constant and the duty ratio versus adult fast/slow isoforms.

3. **Mechanistic investigation of the MYH3–TGFβ link:** test whether mutant MYH3 alters TGFβ via mechanotransduction (e.g., YAP/TAZ, latent TGFβ release from the ECM), direct protein interaction, or secondary muscle-mechanical effects, using myotube and paraspinal-muscle models. This is the highest-value gap given its disease relevance.

4. **Conditional/allelic mouse models** (knock-in of R672C, T178I, and SCT-causing alleles) with quantitative skeletal-muscle mechanics, joint morphometry, and spinal patterning readouts to connect specific kinetic defects to specific developmental phenotypes.

5. **Define the MYH3 light-chain interactome** in fetal and regenerating muscle (co-IP/mass spectrometry) and test how specific ELC/RLC isoforms modulate MYH3 motor kinetics.

6. **Dissect the Zeb1/Tle3/miR-200c/miR-501 regulatory network** at the Myh3 promoter-enhancer with CRISPR perturbation and reporter assays to define the temporal logic of MYH3 induction during regeneration — potentially informative for muscle-repair therapeutics.

---

## Gene-Identity Verification Statement

The gene symbol **MYH3** is **not ambiguous** for this target, and the literature is **fully consistent with the UniProt-provided identity**. All evidence confirms MYH3 (UniProt P11055) as the human embryonic skeletal-muscle myosin heavy chain: the protein family (TRAFAC myosin-kinesin ATPase), domains (motor domain IPR001609, Myosin S1 N IPR008989, tail IPR002928), organism (*Homo sapiens*), and function (sarcomeric myosin II motor) all align precisely with the primary and review literature cited above. No conflicting gene with the same symbol was encountered during this investigation.


## Artifacts

- [OpenScientist final report](MYH3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MYH3-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26945064
2. PMID:39374027
3. PMID:29235081
4. PMID:26970499
5. PMID:26180627
6. PMID:37414375
7. PMID:12110653
8. PMID:37249525
9. PMID:26544689
10. PMID:38856159
11. PMID:25740846
12. PMID:32799913
13. PMID:28205584
14. PMID:37392376
15. PMID:27707793