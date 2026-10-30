---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T01:30:57.203603'
end_time: '2026-10-16T01:41:37.957829'
duration_seconds: 640.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MYH8
  gene_symbol: MYH8
  uniprot_accession: P13535
  protein_description: 'RecName: Full=Myosin-8; AltName: Full=Myosin heavy chain 8;
    AltName: Full=Myosin heavy chain, skeletal muscle, perinatal; Short=MyHC-perinatal;'
  gene_info: Name=MYH8;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class myosin-kinesin ATPase
  protein_domains: Kinesin_motor_dom_sf. (IPR036961); Myosin_head_motor_dom-like.
    (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail. (IPR002928); P-loop_NTPase.
    (IPR027417)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MYH8-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MYH8-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P13535
- **Protein Description:** RecName: Full=Myosin-8; AltName: Full=Myosin heavy chain 8; AltName: Full=Myosin heavy chain, skeletal muscle, perinatal; Short=MyHC-perinatal;
- **Gene Information:** Name=MYH8;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class myosin-kinesin ATPase
- **Key Domains:** Kinesin_motor_dom_sf. (IPR036961); Myosin_head_motor_dom-like. (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail. (IPR002928); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MYH8" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MYH8' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MYH8** (gene ID: MYH8, UniProt: P13535) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MYH8 (Myosin-8 / Perinatal Skeletal Muscle Myosin Heavy Chain): Functional Annotation Report

**Gene:** MYH8 | **UniProt:** P13535 | **Organism:** *Homo sapiens* (Human)
**Protein:** Myosin-8; Myosin heavy chain 8; Myosin heavy chain, skeletal muscle, perinatal (MyHC-perinatal)

---

## Summary

**MYH8 encodes Myosin-8, the perinatal (neonatal) isoform of the skeletal-muscle myosin heavy chain (MyHC) — the force-generating motor subunit of the sarcomeric thick filament.** Its identity is unambiguous and fully consistent with the UniProt record: it is a member of the TRAFAC class myosin-kinesin ATPase superfamily, with a globular N-terminal S1 motor/head domain (an actin-activated ATPase) followed by a neck/lever-arm that binds light chains and a long C-terminal α-helical coiled-coil tail. The symbol "MYH8" matches the protein description, the organism (human) is correct, and the domain architecture (Myosin_S1_N, Myosin_head_motor_dom-like, P-loop NTPase, Myosin_tail) aligns precisely with the experimental and bioinformatic literature. No gene-symbol ambiguity was encountered; the literature consistently concerns this protein.

**Primary molecular function:** The S1 head of MYH8 hydrolyzes ATP (ATP + H₂O → ADP + Pᵢ) in an actin-activated manner and converts the chemical energy into mechanical work via a lever-arm "power stroke." Classic motility studies on the myosin motor domain demonstrate that the compact ATPase head alone is sufficient to drive actin-filament sliding and generate force ([PMID: 8250907](https://pubmed.ncbi.nlm.nih.gov/8250907/)). Two heavy chains dimerize through their coiled-coil tails and, together with one essential light chain (ELC) and one regulatory light chain (RLC) per head, build the hexameric conventional myosin II molecule. Electrostatic interactions between tail domains drive self-assembly into bipolar thick filaments that engage actin thin filaments to produce contractile force ([PMID: 12952069](https://pubmed.ncbi.nlm.nih.gov/12952069/)). These filaments localize to the **A-band of the sarcomere** in the cytoplasm of striated muscle fibers ([PMID: 21177250](https://pubmed.ncbi.nlm.nih.gov/21177250/)).

**Biological context and significance:** MYH8 is a developmentally restricted isoform. It is expressed during fetal/perinatal skeletal-muscle development, down-regulated by ~4–6 months after birth, and re-expressed during satellite-cell-driven muscle regeneration — making it a widely used histological marker of regenerating fibers ([PMID: 29761627](https://pubmed.ncbi.nlm.nih.gov/29761627/); [PMID: 33685841](https://pubmed.ncbi.nlm.nih.gov/33685841/)). Beyond its structural/motor role, MYH8 also influences myogenic differentiation and fiber-type/oxidative metabolism ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/)). The essential contractile role of MYH8 is proven in humans by a recurrent actin-binding-region mutation, **p.Arg674Gln**, which disrupts the muscle contractile complex and causes autosomal-dominant **Trismus-pseudocamptodactyly (Hecht) syndrome / distal arthrogryposis type 7** ([PMID: 15282353](https://pubmed.ncbi.nlm.nih.gov/15282353/); [PMID: 17041932](https://pubmed.ncbi.nlm.nih.gov/17041932/)).

---

## Gene/Protein Identity Verification

Per the mandatory verification protocol, the following checks were performed and **all passed**:

| Check | Result |
|-------|--------|
| Gene symbol "MYH8" matches protein description | ✅ MYH8 = Myosin-8 = MyHC-perinatal throughout the literature |
| Organism is *Homo sapiens* | ✅ Human cDNA, human disease genetics, and human muscle histology all concordant |
| Protein family/domains align with literature | ✅ Myosin II; S1 motor head + coiled-coil rod; TRAFAC myosin-kinesin ATPase |
| No conflicting gene with same symbol | ✅ No ambiguity found; literature is specific to perinatal MyHC |

The literature is specific and consistent: MYH8 is the perinatal skeletal myosin heavy-chain gene, located in the chromosome-17 fast/developmental MyHC cluster, encoding a protein with an S1 head and a rod domain ([PMID: 2373371](https://pubmed.ncbi.nlm.nih.gov/2373371/)).

---

## Key Findings

### Finding 1 — MYH8 is a developmentally restricted sarcomeric motor protein (perinatal MyHC)

MYH8 encodes **Myosin heavy chain-perinatal (MyHC-perinatal)**, one of only two development-specific myosin heavy chains that are expressed essentially exclusively during skeletal-muscle development and regeneration ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/)). It belongs to the fast skeletal MyHC gene family, which includes the embryonic isoform (MYH3), the adult fast isoforms (MYH1, MYH2, MYH4), and the extraocular isoform (MYH13). Consistent with the UniProt P13535 record, the protein is a member of the **TRAFAC class myosin-kinesin ATPase** superfamily and carries the canonical myosin domain set: a myosin S1 motor/head domain (IPR001609, IPR008989), a P-loop NTPase fold (IPR027417) responsible for nucleotide binding/hydrolysis, and a myosin tail (IPR002928) responsible for filament assembly.

> *"Myosin heavy chain-perinatal (MyHC-perinatal) is one of two development-specific myosin heavy chains expressed exclusively during skeletal muscle development and regeneration."* ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/))

### Finding 2 — The myosin motor (ATPase) head generates force by actin-activated ATP hydrolysis driving filament sliding

The defining molecular function of any myosin heavy chain, including MYH8, resides in its globular head. The head comprises a catalytic ATPase/motor domain plus a neck/lever-arm. A landmark structure-function study demonstrated that a **truncated myosin head is by itself sufficient** to drive the sliding movement of actin filaments and to generate force in a dedicated in-vitro assay — establishing the motor domain as the force-generating machine ([PMID: 8250907](https://pubmed.ncbi.nlm.nih.gov/8250907/)). The standard biochemical readouts of this function are **actin-activated ATPase activity** (parameterized by the Km for actin) and **in-vitro actin-sliding velocity** ([PMID: 21177250](https://pubmed.ncbi.nlm.nih.gov/21177250/); [PMID: 25911107](https://pubmed.ncbi.nlm.nih.gov/25911107/)). Mechanistically, each ATPase cycle couples nucleotide binding, hydrolysis and product release to conformational changes in the head that rotate the lever-arm — the "power stroke" — translating ATP chemistry into directed mechanical displacement of the actin thin filament.

> *"The truncated head drove sliding movement of actin filaments and generated force in a novel in vitro assay system."* ([PMID: 8250907](https://pubmed.ncbi.nlm.nih.gov/8250907/))

### Finding 3 — A recurrent R674Q mutation in the actin-binding region causes Trismus-pseudocamptodactyly (Hecht) syndrome

The physiological necessity of the MYH8 motor function in humans is demonstrated by disease genetics. A missense mutation **p.Arg674Gln** in MYH8 causes autosomal-dominant **Trismus-pseudocamptodactyly syndrome (TPS; Hecht syndrome; distal arthrogryposis type 7, DA7)**. Arg674 is **highly conserved evolutionarily and localizes to the actin-binding domain of the perinatal myosin head** ([PMID: 15282353](https://pubmed.ncbi.nlm.nih.gov/15282353/)). Strikingly, the identical p.R674Q substitution has recurred across independent Dutch and North American pedigrees through independent mutation events, and the broader distal arthrogryposis family of disorders is, in general, caused by **disruption of the contractile complex of muscle** ([PMID: 17041932](https://pubmed.ncbi.nlm.nih.gov/17041932/)). Clinically, Hecht syndrome manifests with trismus (limited jaw opening, often due to coronoid-process hyperplasia) and pseudocamptodactyly (finger flexion on wrist extension), reflecting impaired actomyosin interaction in the developing/perinatal muscle ([PMID: 26335328](https://pubmed.ncbi.nlm.nih.gov/26335328/)). This pinpoints the pathogenic residue to the actin-binding interface of the motor, directly linking MYH8 molecular function (actomyosin coupling) to a defined human phenotype.

> *"Arg674 is highly conserved evolutionarily, localizes to the actin-binding domain of the perinatal myosin head."* ([PMID: 15282353](https://pubmed.ncbi.nlm.nih.gov/15282353/))
>
> *"distal arthrogryposis syndromes share a similar pathogenesis and are, in general, caused by disruption of the contractile complex of muscle."* ([PMID: 17041932](https://pubmed.ncbi.nlm.nih.gov/17041932/))

### Finding 4 — MYH8 regulates myogenic differentiation, fiber-type/oxidative phenotype, and regeneration

Beyond its direct motor role, MYH8 has a regulatory influence on muscle biology. Loss of MyHC-perinatal function **enhances myogenic differentiation** (increased myogenic regulatory factors, higher differentiation index, fewer reserve cells) and **switches myofiber metabolism from oxidative to glycolytic**, consistent with a shift from slow type I toward fast type IIb fibers and reduced mitochondrial content. In vivo knockdown during regeneration increases myogenin and impairs differentiation, producing smaller myofibers, more fibrosis, and fewer satellite cells; the effects engage paracrine non-apoptotic caspase-3, Bcl2, and NF-κB signaling ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/)). This positions MYH8 not merely as a passive structural component but as a modulator of the differentiation program and the oxidative/glycolytic balance during muscle formation and repair.

> *"loss of MyHC-perinatal function results in a switch from oxidative to glycolytic metabolism in myofibers, suggesting a shift from slow type I to fast type IIb fiber type."* ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/))

### Finding 5 — MYH8 lies in the chromosome-17 fast/developmental MyHC cluster and encodes an S1 head plus coiled-coil rod

The perinatal skeletal MHC gene (MYH8) is localized to the **cluster of skeletal MHC-encoding genes on human chromosome 17** ([PMID: 2373371](https://pubmed.ncbi.nlm.nih.gov/2373371/)). This cluster also contains the embryonic (MYH3), adult fast (MYH1, MYH2, MYH4), and extraocular superfast (MYH13) isoforms ([PMID: 9806854](https://pubmed.ncbi.nlm.nih.gov/9806854/)). The MYH8 transcript encodes **both the subfragment-1 (S1) head and the rod (tail)** portion of the molecule ([PMID: 2373371](https://pubmed.ncbi.nlm.nih.gov/2373371/)), directly matching the UniProt domain architecture (motor head IPR001609/IPR008989 plus myosin tail IPR002928). Evolutionary analysis of this cluster shows that MYH13 was the first fast/developmental member to diverge and that the **motor and rod domains evolved under different selective pressures** ([PMID: 12110653](https://pubmed.ncbi.nlm.nih.gov/12110653/)), reinforcing the modular, two-part (motor + rod) design that MYH8 shares.

> *"The gene encoding the perinatal skeletal MHC has been localized to the cluster of skeletal MHC-encoding genes on chromosome 17."* ([PMID: 2373371](https://pubmed.ncbi.nlm.nih.gov/2373371/))
>
> *"a 2.6-kb cDNA that encodes the subfragment 1 or head of a human perinatal skeletal MHC."* ([PMID: 2373371](https://pubmed.ncbi.nlm.nih.gov/2373371/))

### Finding 6 — Perinatal MyHC is down-regulated after birth and re-expressed in regenerating muscle

Developmental MyHCs present in embryonic and fetal/neonatal skeletal muscle are **re-expressed during muscle regeneration** and are used to identify regenerating fibers in muscle diseases ([PMID: 29761627](https://pubmed.ncbi.nlm.nih.gov/29761627/)). Immunohistochemical baseline data from normal human quadriceps show that **fetal (perinatal) myosin heavy chains are down-regulated by 4–6 months of age**, and that their persistence or re-appearance signals delayed maturation, regeneration, or disease ([PMID: 33685841](https://pubmed.ncbi.nlm.nih.gov/33685841/)). This temporal expression profile — high perinatally, silenced in healthy mature muscle, and reactivated upon injury — is the hallmark of MYH8 as a developmental/regeneration isoform and underlies its diagnostic utility in myopathology.

> *"Developmental MyHCs present in embryonic and fetal/neonatal skeletal muscle are re-expressed during muscle regeneration and can be used to identify regenerating fibers in muscle diseases."* ([PMID: 29761627](https://pubmed.ncbi.nlm.nih.gov/29761627/))
>
> *"Fetal myosin heavy chains are down-regulated by 4-6 months."* ([PMID: 33685841](https://pubmed.ncbi.nlm.nih.gov/33685841/))

### Finding 7 — MYH8 is a conventional myosin II hexamer that self-assembles into bipolar thick filaments in the A-band

Conventional (two-headed) myosin II consists of **two heavy chains plus one essential light chain (ELC) and one regulatory light chain (RLC) per head**. Each heavy chain has an N-terminal motor domain, a neck region that binds the RLC and ELC, and a C-terminal α-helical coiled-coil tail. **Electrostatic interactions between the tail domains mediate self-assembly of myosin II into bipolar filaments** that are capable of interacting with actin filaments to generate contractile force ([PMID: 12952069](https://pubmed.ncbi.nlm.nih.gov/12952069/)). In striated muscle these thick filaments reside in the **A-band of the sarcomere** ([PMID: 21177250](https://pubmed.ncbi.nlm.nih.gov/21177250/)). This describes the structural role MYH8 performs: it is the backbone of the perinatal thick filament, both bearing the motor heads that pull on actin and providing (via its rod) the scaffold that organizes bipolar filament architecture.

> *"Electrostatic interactions between the tail domains mediate the self-assembly of myosin II into bipolar filaments that are capable of interacting with actin filaments to generate a contractile force."* ([PMID: 12952069](https://pubmed.ncbi.nlm.nih.gov/12952069/))

### Finding 8 — MYH8 is re-expressed in adult masticatory (jaw) muscle during functional adaptation

Although developmental MyHCs are normally silenced after infancy, perinatal MYH8 (and embryonic MYH3) transcripts remain detectable and are modulated in **adult human masseter muscle**. Following orthognathic surgery, MYH8 was up-regulated in retrognathic patients (fold ≈ 4.0, P < 0.063, a suggestive trend) and down-regulated in prognathia; the authors proposed that MYH3/MYH8 participate in the **functional adaptation of masticatory muscle** ([PMID: 20673635](https://pubmed.ncbi.nlm.nih.gov/20673635/)). This specialized adult expression niche in jaw muscle is notable because it is consistent with the jaw-centered (trismus) phenotype of MYH8-associated Hecht syndrome, tying the expression domain of the protein to its disease presentation.

> *"MYH3 and MYH8 could play a role in functional adaptation after orthognathic surgery and orofacial orthopaedics."* ([PMID: 20673635](https://pubmed.ncbi.nlm.nih.gov/20673635/))

---

## Mechanistic Model / Interpretation

### Domain architecture (modular motor + rod)

```
MYH8 heavy chain (N → C)
┌───────────────────────────┬──────────────┬───────────────────────────────────┐
│   S1 MOTOR / HEAD DOMAIN   │  NECK / LEVER │       COILED-COIL ROD (TAIL)       │
│  (ATPase + actin-binding)  │  (ELC + RLC   │  (self-assembly, filament backbone)│
│   P-loop NTPase fold       │   binding)    │                                    │
│   ← Arg674 (actin-binding) │               │                                    │
└───────────────────────────┴──────────────┴───────────────────────────────────┘
  IPR001609 / IPR008989 /        light-chain          IPR002928 (Myosin_tail)
  IPR027417 (P-loop NTPase)      lever arm
```

### From molecule to contraction

```
Two MYH8 heavy chains + 2 ELC + 2 RLC  ─►  one hexameric myosin II molecule
          │ (tails dimerize via coiled-coil)
          ▼
Electrostatic tail–tail interactions  ─►  BIPOLAR THICK FILAMENT
          │                                   (localized to sarcomere A-band)
          ▼
   S1 heads bind actin thin filament
          │
   ATP binds → hydrolysis (ATP+H2O→ADP+Pi) → Pi release → LEVER-ARM POWER STROKE
          │
          ▼
  Actin thin filaments slide toward sarcomere center  ─►  SARCOMERE SHORTENING
          │
          ▼
          MUSCLE CONTRACTION (force generation)
```

### Where and when MYH8 acts

| Axis | MYH8 specifics |
|------|----------------|
| **Subcellular location** | Cytoplasm; sarcomeric A-band of striated-muscle myofibrils; the rod forms the thick-filament backbone, the heads project toward actin thin filaments ([PMID: 12952069](https://pubmed.ncbi.nlm.nih.gov/12952069/); [PMID: 21177250](https://pubmed.ncbi.nlm.nih.gov/21177250/)) |
| **Tissue/developmental window** | Fetal/perinatal skeletal muscle; silenced by 4–6 months postnatally; reactivated in regenerating fibers; residual/adaptive expression in adult masticatory muscle ([PMID: 29761627](https://pubmed.ncbi.nlm.nih.gov/29761627/); [PMID: 33685841](https://pubmed.ncbi.nlm.nih.gov/33685841/); [PMID: 20673635](https://pubmed.ncbi.nlm.nih.gov/20673635/)) |
| **Primary function** | Mechanoenzyme (molecular motor): actin-activated ATPase that converts ATP hydrolysis into mechanical sliding of actin ([PMID: 8250907](https://pubmed.ncbi.nlm.nih.gov/8250907/)) |
| **Substrate(s)** | ATP (hydrolyzed to ADP + Pᵢ); actin filament (the "track"/binding partner activating ATPase) |
| **Pathway/process** | Striated-muscle contraction; also modulates myogenic differentiation and oxidative-vs-glycolytic fiber phenotype ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/)) |
| **Human disease link** | p.Arg674Gln (actin-binding region) → Trismus-pseudocamptodactyly / Hecht syndrome (DA7) ([PMID: 15282353](https://pubmed.ncbi.nlm.nih.gov/15282353/); [PMID: 17041932](https://pubmed.ncbi.nlm.nih.gov/17041932/)) |

### Synthesis

The findings converge on a single, coherent narrative. MYH8 is **not a metabolic enzyme but a mechanoenzyme** — its "reaction" is the actin-activated hydrolysis of ATP (ATP + H₂O → ADP + Pᵢ), and its "product" is mechanical force/displacement. Its substrate specificity is twofold: ATP as the chemical fuel at the P-loop NTPase active site, and filamentous actin as the binding partner that both activates the ATPase and serves as the track along which the motor steps. The protein is structural *and* enzymatic simultaneously: the head is the motor, while the coiled-coil rod builds the thick-filament scaffold. Its role in the contraction pathway is the terminal effector — downstream of excitation–contraction coupling and Ca²⁺-mediated thin-filament regulation, MYH8 heads perform the actual work that shortens the sarcomere. The developmental specificity (perinatal window, regeneration reactivation) defines *when* this motor is deployed, and the Hecht-syndrome mutation provides a human genetic proof that corrupting the actomyosin interface of this specific isoform disrupts the contractile complex with a defined clinical phenotype.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [8250907](https://pubmed.ncbi.nlm.nih.gov/8250907/) | *Force-generating domain of myosin motor* | Direct experimental proof that the myosin head/ATPase domain drives actin sliding and force — defines the molecular function of MYH8 (F2) |
| [12952069](https://pubmed.ncbi.nlm.nih.gov/12952069/) | *Signaling pathways regulating Dictyostelium myosin II* | Describes conventional myosin II hexamer structure and tail-mediated bipolar filament self-assembly (F7) |
| [21177250](https://pubmed.ncbi.nlm.nih.gov/21177250/) / [25911107](https://pubmed.ncbi.nlm.nih.gov/25911107/) | *HDAC3 reversible acetylation of cardiac MHC* | Localizes myosin/A-band proteins to the sarcomere A-band; establishes actin-activated ATPase Km and sliding velocity as motor readouts (F2, F7) |
| [15282353](https://pubmed.ncbi.nlm.nih.gov/15282353/) | *Mutation of perinatal MHC (Carney complex variant)* | Pinpoints pathogenic Arg674 to the conserved actin-binding region of the MYH8 head (F3) |
| [17041932](https://pubmed.ncbi.nlm.nih.gov/17041932/) | *TPS caused by recurrent MYH8 mutation* | Shows recurrent R674Q and that distal arthrogryposis arises from disruption of the muscle contractile complex (F3) |
| [38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/) | *MyHC-perinatal regulates differentiation, oxidative phenotype, regeneration* | Establishes MYH8 identity as development-specific isoform and its regulatory role in differentiation and fiber-type metabolism (F1, F4) |
| [2373371](https://pubmed.ncbi.nlm.nih.gov/2373371/) | *Full-length human perinatal MHC cDNA* | Maps MYH8 to chromosome-17 skeletal MHC cluster; shows transcript encodes S1 head + rod (F5) |
| [12110653](https://pubmed.ncbi.nlm.nih.gov/12110653/) / [9806854](https://pubmed.ncbi.nlm.nih.gov/9806854/) | *Superfast myosin in extraocular muscles / MYH13 mapping* | Evolutionary/genomic context of the chromosome-17 fast/developmental cluster; distinct motor vs rod selective pressures (F5) |
| [29761627](https://pubmed.ncbi.nlm.nih.gov/29761627/) | *Muscle fiber type diversity revealed by anti-MyHC antibodies* | Authoritative review: developmental MyHCs re-expressed in regeneration; used as regeneration markers (F6) |
| [33685841](https://pubmed.ncbi.nlm.nih.gov/33685841/) | *IHC of developmentally regulated MyHCs in human biopsies* | Documents postnatal down-regulation timing (4–6 months) of fetal/perinatal myosin (F6) |
| [20673635](https://pubmed.ncbi.nlm.nih.gov/20673635/) | *Developmental MyHC mRNA in masseter after orthognathic surgery* | Adult masticatory-muscle expression niche; functional adaptation relevance to jaw phenotype (F8) |
| [19181095](https://pubmed.ncbi.nlm.nih.gov/19181095/) | *Thick filament diseases* | Context: MYH3/MYH8 mutations cause distal arthrogryposis with minor muscle weakness, as expected for developmentally restricted isoforms (supports F1, F3) |
| [21370490](https://pubmed.ncbi.nlm.nih.gov/21370490/), [24220225](https://pubmed.ncbi.nlm.nih.gov/24220225/) | *Myoblast / MSC differentiation markers* | Corroborate MYH8 as a time-dependent marker of myogenic differentiation (supports F4, F6) |

**Note on cross-species myosin evidence:** Several mechanistic references (e.g., *Dictyostelium* myosin II, cardiac MHC acetylation) are used to establish the conserved, generic properties of conventional myosin II — hexameric assembly, tail-mediated filament formation, and the actin-activated ATPase cycle. These are legitimately transferable because the myosin II motor and rod architecture is deeply conserved across the TRAFAC myosin superfamily, and the human perinatal-isoform-specific claims (identity, chromosome-17 locus, R674Q disease, developmental expression, regulatory role) are each anchored to human MYH8-specific primary literature.

---

## Limitations and Knowledge Gaps

1. **No MYH8-isoform-specific enzyme kinetics.** The actin-activated ATPase rate, Km for actin, and unloaded actin-sliding velocity have been measured for cardiac and other myosins, but **isoform-specific kinetic constants for purified human perinatal MyHC (P13535) were not identified** in the reviewed literature. The motor properties of MYH8 are inferred from the conserved myosin II mechanism rather than measured directly.

2. **Mechanistic basis of R674Q is inferential.** Arg674 lies in the conserved actin-binding region, and disease is attributed to disruption of the contractile complex, but the **precise biophysical consequence** (altered actin affinity, impaired power stroke, filament instability, dominant-negative poisoning of co-assembled filaments) has not been resolved by single-molecule or structural studies on the mutant MYH8 head.

3. **Light-chain partners not defined for the perinatal isoform.** The hexameric model assumes canonical ELC/RLC pairing (established generically for myosin II), but the **specific essential and regulatory light-chain isoforms** that co-assemble with perinatal MyHC in vivo were not pinned down.

4. **Regulatory signaling is incompletely mapped.** The reported links to caspase-3/Bcl2/NF-κB signaling in differentiation ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/)) describe correlations and knockdown phenotypes; the **direct molecular pathway** by which a structural motor protein modulates the differentiation program remains unclear (could be indirect, via contractility-dependent mechanotransduction).

5. **Cross-species transfer.** Some foundational mechanistic claims rely on non-human myosins (*Dictyostelium*, cardiac). While architecture is conserved, isoform- and species-specific quantitative differences cannot be excluded.

6. **Adult masseter expression is a trend, not a confirmed effect.** The orthognathic-surgery masseter result (fold ≈ 4.0, P < 0.063) is **suggestive only** and from a small preliminary study ([PMID: 20673635](https://pubmed.ncbi.nlm.nih.gov/20673635/)).

---

## Proposed Follow-up Experiments / Actions

1. **Direct motor characterization of human perinatal MyHC.** Express and purify the human MYH8 S1 head (wild-type and R674Q) and measure actin-activated ATPase kinetics (Km, Vmax), in-vitro motility sliding velocity, and single-molecule step size/force. This would convert the inferred motor function into isoform-specific quantitative data and reveal the biophysical defect caused by R674Q.

2. **Structural study of the R674Q actomyosin interface.** Use cryo-EM of the perinatal myosin head bound to F-actin (±ADP/Pᵢ analogs) to visualize how Arg674 contacts actin and how the Gln substitution perturbs the interface and the power stroke.

3. **Define the light-chain complement.** Co-immunoprecipitation / mass-spectrometry from perinatal or regenerating human muscle to identify the ELC and RLC isoforms that partner with MYH8 in native thick filaments.

4. **Dominant-negative mechanism test.** In a heterozygous model (e.g., iPSC-derived myotubes carrying R674Q), test whether mutant heavy chains co-assemble with and poison wild-type filaments, and quantify effects on sarcomere assembly and contractile force.

5. **Dissect the differentiation/fiber-type regulatory axis.** Determine whether MYH8's influence on differentiation and oxidative metabolism ([PMID: 38358038](https://pubmed.ncbi.nlm.nih.gov/38358038/)) is contractility-dependent (mechanotransduction) versus a signaling role, using motor-dead vs rod-only constructs and inhibitors of caspase-3/NF-κB.

6. **Confirm and extend the masticatory-muscle niche.** Adequately powered RNA/protein quantification of MYH8 in adult human masseter under functional-adaptation conditions to validate the preliminary orthognathic-surgery trend and clarify relevance to the trismus phenotype.

---

## Conclusion

MYH8 encodes **Myosin-8, the perinatal skeletal-muscle myosin heavy chain** — a conventional myosin II motor and the force-generating subunit of the developmental/regenerating thick filament. Its globular S1 head is an **actin-activated ATPase** that hydrolyzes ATP (ATP + H₂O → ADP + Pᵢ) and, through a lever-arm power stroke, drives actin thin-filament sliding to produce muscle contraction. Two heavy chains dimerize via coiled-coil tails and, with essential and regulatory light chains, self-assemble into bipolar thick filaments localized to the **A-band of the sarcomere** in the cytoplasm of perinatal and regenerating skeletal-muscle fibers. Expression is developmentally restricted (silenced ~4–6 months postnatally, reactivated during regeneration), and the protein additionally modulates myogenic differentiation and fiber-type metabolism. The essential contractile role is confirmed in humans by the recurrent actin-binding-region mutation **p.Arg674Gln**, which disrupts the muscle contractile complex and causes Trismus-pseudocamptodactyly (Hecht) syndrome.


## Artifacts

- [OpenScientist final report](MYH8-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MYH8-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8250907
2. PMID:12952069
3. PMID:21177250
4. PMID:29761627
5. PMID:33685841
6. PMID:38358038
7. PMID:15282353
8. PMID:17041932
9. PMID:2373371
10. PMID:25911107
11. PMID:26335328
12. PMID:9806854
13. PMID:12110653
14. PMID:20673635