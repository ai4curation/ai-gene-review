---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T00:55:48.985143'
end_time: '2026-10-16T01:09:05.127408'
duration_seconds: 796.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MYH7
  gene_symbol: MYH7
  uniprot_accession: P12883
  protein_description: 'RecName: Full=Myosin-7; AltName: Full=Myosin heavy chain 7;
    AltName: Full=Myosin heavy chain slow isoform; Short=MyHC-slow; AltName: Full=Myosin
    heavy chain, cardiac muscle beta isoform; Short=MyHC-beta;'
  gene_info: Name=MYH7; Synonyms=MYHCB;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class myosin-kinesin ATPase
  protein_domains: IQ_motif_EF-hand-BS. (IPR000048); Kinesin_motor_dom_sf. (IPR036961);
    Myosin_head_motor_dom-like. (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail.
    (IPR002928)
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
citation_count: 28
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MYH7-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MYH7-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P12883
- **Protein Description:** RecName: Full=Myosin-7; AltName: Full=Myosin heavy chain 7; AltName: Full=Myosin heavy chain slow isoform; Short=MyHC-slow; AltName: Full=Myosin heavy chain, cardiac muscle beta isoform; Short=MyHC-beta;
- **Gene Information:** Name=MYH7; Synonyms=MYHCB;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class myosin-kinesin ATPase
- **Key Domains:** IQ_motif_EF-hand-BS. (IPR000048); Kinesin_motor_dom_sf. (IPR036961); Myosin_head_motor_dom-like. (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail. (IPR002928)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MYH7" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MYH7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MYH7** (gene ID: MYH7, UniProt: P12883) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MYH7 (β-Cardiac / Slow-Skeletal Myosin Heavy Chain) — Functional Annotation Report

**Gene:** MYH7 (synonym MYHCB) · **UniProt:** P12883 (Myosin-7) · **Organism:** *Homo sapiens*
**Protein family:** TRAFAC class myosin-kinesin ATPase superfamily
**Key domains:** Myosin S1 N-terminal (IPR008989); Myosin head motor domain-like (IPR001609); IQ motif / EF-hand binding site (IPR000048); Myosin tail (IPR002928); Kinesin motor domain superfamily fold (IPR036961)

---

## Summary

**MYH7 encodes the heavy chain of β-cardiac myosin — also known as slow (type I) skeletal muscle myosin heavy chain, MyHC-slow, or MyHC-β — an actin-activated ATPase mechanoenzyme that is the force-generating molecular motor and the principal structural building block of the sarcomeric thick filament.** The protein is a dimer of two heavy chains plus two pairs of light chains. Its N-terminal globular head (motor domain) binds and hydrolyzes ATP (ATP → ADP + Pi) and binds actin; the free energy of hydrolysis drives a cyclic conformational change — the swinging lever-arm power stroke — that pulls actin thin filaments past the myosin thick filament to produce the mechanical force of muscle contraction. Its long C-terminal α-helical rod dimerizes into a coiled coil and self-assembles with hundreds of other myosin rods to form the backbone of the thick filament. MYH7 therefore has a dual identity: it is simultaneously an **enzyme/motor** (actin-activated ATPase) and a **structural protein** (thick-filament scaffold).

MYH7 carries out its function entirely **intracellularly**, within the sarcomere — the ordered contractile apparatus of striated muscle — specifically in the A-band of the sarcomere. It is the dominant myosin of two tissues: the human ventricular myocardium (where it accounts for ~90% of ventricular myosin heavy chain) and slow-twitch type I skeletal muscle fibers. This dual expression explains why mutations in MYH7 can produce cardiomyopathy, skeletal myopathy, or both.

Functionally, MYH7 is a **slow, energetically economical motor** that is tuned by two layers of regulation. First, a **dual-filament regulatory pathway** integrates a chemical signal (a rise in cytosolic Ca²⁺ shifts troponin-tropomyosin to expose actin's myosin-binding sites — thin-filament activation) with a mechanical signal (titin- and myosin-binding protein-C-dependent thick-filament mechanosensing that releases sequestered myosin heads). This interfilament coupling underlies length-dependent activation, the molecular basis of the Frank–Starling law of the heart. Second, an **intrinsic ON/OFF autoregulatory switch** — the super-relaxed (SRX) state / interacting-heads motif (IHM) — sets the fraction of motors available to interact with actin. Hypertrophic cardiomyopathy mutations shift this switch toward ON (hypercontractility); dilated cardiomyopathy mutations shift it toward OFF (hypocontractility); and rod mutations instead disrupt thick-filament assembly to cause skeletal myopathies. This report synthesizes 12 confirmed findings drawn from 39 reviewed papers into a coherent mechanistic account.

---

## Key Findings

### 1. MYH7 is an ATP-driven actin-based molecular motor

The core function of the MYH7 gene product is mechanochemical energy transduction: it converts the chemical energy of ATP hydrolysis into directed mechanical force. The N-terminal motor (head) domain contains an **ATP-binding site with actin-activated ATPase activity** adjacent to an **actin-binding interface**. The enzymatic cycle is coupled to a cyclic conformational change — the power stroke — in which the converter sub-domain transduces force from the catalytic core to the lever arm, swinging the head relative to the rod. As stated directly in a review of myosin myopathies, "*Myosin, a molecular motor, converts chemical energy into mechanical force. The motor domain of myosin heavy chain (MyHC) includes an ATP binding region with ATPase activity and an actin-binding region. Motor function is achieved by conformational changes, at hydrolysis, of ATP causing a shift in the angle between the actin binding head and the rod region of the molecule*" ([PMID: 15605950](https://pubmed.ncbi.nlm.nih.gov/15605950/)). The converter/lever-arm force-transduction mechanism is specifically defined in human β-cardiac myosin: the converter is "*a kinetic domain that transduces force from the catalytic domain to the lever arm to accomplish the power stroke*" ([PMID: 27247418](https://pubmed.ncbi.nlm.nih.gov/27247418/)). MYH7 belongs to the TRAFAC class myosin-kinesin ATPase superfamily (InterPro IPR001609, myosin head motor domain).

### 2. MYH7 localizes to the sarcomere thick filament: rod forms the backbone, heads engage actin

The functional myosin molecule is a **hexamer**: two MYH7 heavy chains and two pairs of light chains. Each heavy chain has an N-terminal globular head and a C-terminal α-helical rod; the two rods dimerize into a two-stranded coiled coil (InterPro IPR002928, myosin tail). The distal two-thirds of these rods pack in parallel to build the thick-filament backbone, while the heads project from the filament surface to reach the thin (actin) filaments. A recent structural review states: "*The thick filaments are composed of myosin molecules, which are hexamers of two heavy chains and two pairs of light chains. The heavy chain has an N-terminal head domain and a C-terminal helical rod domain. The latter dimerises to form a two-stranded coiled-coil rod. The distal two-thirds of these rods aggregate in parallel to form the filament backbone, while the heads lie on the surface to facilitate interactions with actin*" ([PMID: 41557228](https://pubmed.ncbi.nlm.nih.gov/41557228/)). MYH7 therefore performs its function **intracellularly**, within the contractile apparatus (sarcomere) of striated muscle cells, in the A-band.

### 3. MYH7 is the dominant myosin of cardiac ventricle and slow (type I) skeletal fibers

MYH7 encodes the "slow/β-cardiac" myosin heavy chain isoform. It is simultaneously the principal myosin of the human ventricular myocardium (β-cardiac myosin) and the myosin of slow-twitch type I skeletal fibers. Human limb skeletal muscle expresses three adult MyHC isoforms: "*Three major MyHC isoforms are expressed in human skeletal muscle (type I, MYH7, expressed in type 1 fibres; IIa, MYH2, expressed in 2A fibres; IIx, MYH1, expressed in 2B fibres)*" ([PMID: 15605950](https://pubmed.ncbi.nlm.nih.gov/15605950/)). This dual cardiac/slow-skeletal identity is confirmed in disease genetics: "*The mutations of MYH7 (slow skeletal/β-cardiac myosin heavy chain) are commonly found in familial hypertrophic/dilated cardiomyopathy*" ([PMID: 29170849](https://pubmed.ncbi.nlm.nih.gov/29170849/)). The shared protein in two tissues explains the clinical spectrum spanning cardiomyopathy, skeletal myopathy, or both.

### 4. β-Cardiac myosin (MYH7) is the slow, high-economy human ventricular motor (~90% of ventricular MHC)

Direct fast-kinetic analysis of recombinant human motor domains established that β-myosin (MYH7) is intrinsically a slow motor, distinct from the fast α-isoform (MYH6), despite 91% motor-domain sequence identity. In healthy adult human ventricle the isoform ratio is approximately α:β = 1:9, i.e., β/MYH7 dominates: "*healthy human heart ventricles express these isoforms in a ratio of about 1:9 (α:β) while failing human ventricles express no detectable α-myosin*" ([PMID: 22349210](https://pubmed.ncbi.nlm.nih.gov/22349210/)). Kinetically, "*the ATP hydrolysis step of α-S1 is ~ten-fold faster than β-S1, α-S1 exhibits ~five-fold weaker actin affinity than β-S1, and actin·α-S1 exhibits rapid ADP release, which is >ten-fold faster than ADP release for β-S1*" ([PMID: 22349210](https://pubmed.ncbi.nlm.nih.gov/22349210/)). The physiological consequence: "*Alpha-MHC confers a higher ATPase activity and higher shortening velocity to the heart than beta-MHC*" ([PMID: 10494800](https://pubmed.ncbi.nlm.nih.gov/10494800/)). β-MHC is slower but more energetically economical, well suited to the sustained workload of the human heart. Notably, ADP release is the rate-limiting step of the β-cardiac motor's cycle — a kinetic signature that governs its slow, strain-sensitive behavior.

### 5. Force generation proceeds by a swinging lever-arm power stroke (~5 nm lever swing, ~10–12 nm working stroke)

The myosin S1 head comprises three functional modules: the catalytic (motor) domain that binds ATP and actin; the converter; and the lever arm (the light-chain-binding neck). As summarized from solution studies, the head "*consists of three domains that catalyze ATP and bind actin (catalytic), conduct energy transduction (converter), and transport the load (lever arm)*" ([PMID: 11294651](https://pubmed.ncbi.nlm.nih.gov/11294651/)). Structural and biophysical evidence (S1 crystal structures, insect-flight-muscle tomography of actively contracting fibers, fluorescence polarization, and X-ray diffraction during rapid length steps) supports a **two-stage power stroke**: "*a two-stage power stroke in which the catalytic domain rolls on actin from weak to strong binding; this is followed by a 5-nm lever arm swing of the light chain domain, which gives a total interaction distance of approx. 12 nm*" ([PMID: 11017871](https://pubmed.ncbi.nlm.nih.gov/11017871/)). ATP hydrolysis and the energy of actin binding re-cock the crossbridge for the next cycle.

### 6. Contractility is auto-regulated by an ON/OFF equilibrium — the super-relaxed state / interacting-heads motif

β-Cardiac myosin exists in equilibrium between an ON-state, in which both heads are free to bind actin, and an OFF-state, in which the two heads fold back onto their own coiled-coil tail and pair in the **interacting-heads motif (IHM)**: "*Human β-cardiac myosin exists in an ON-state where both myosin heads are accessible for interaction with actin, and an OFF-state where the heads are folded back onto their own coiled-coil tail, interacting with each other via an interacting-heads motif (IHM)*" ([PMID: 39192034](https://pubmed.ncbi.nlm.nih.gov/39192034/)). The IHM corresponds to the biochemically defined **super-relaxed (SRX)** state of very low ATP turnover, structurally resolved at near-atomic (3.6 Å) resolution: "*In cardiac muscle, many myosin molecules are in a resting or "OFF" state with their catalytic heads in a folded structure known as the interacting heads motif (IHM)*" ([PMID: 39713291](https://pubmed.ncbi.nlm.nih.gov/39713291/)). Solution FRET and single-ATP-turnover assays show this OFF/ON (SRX/DRX) equilibrium exchanges rapidly and is tunable by ionic strength, S2 tail length, mutations, and the therapeutic inhibitor mavacamten — thereby setting the fraction of motors available for contraction.

### 7. MYH7 operates within a dual-filament regulatory pathway integrating Ca²⁺ and mechanical load

Contraction is governed by two coordinated regulatory pathways acting on the two filament systems. **Thin-filament activation**: a rise in intracellular Ca²⁺ moves the troponin-tropomyosin complex to expose the myosin-binding sites on actin. **Thick-filament activation**: a separate mechanosensing pathway releases sequestered (IHM/OFF) myosin heads to make them available for actin binding. A review describing this emerging paradigm states: "*A novel dual-filament paradigm of muscle regulation is emerging, in which the dynamics of force generation depends on the coordinated activation of thin and thick filaments. We highlight the interfilament signaling pathways based on titin and myosin-binding protein-C that couple thin and thick filament regulatory mechanisms. This dual-filament regulation mediates the length-dependent activation of cardiac muscle that underlies the control of the cardiac output in each heartbeat*" ([PMID: 37931167](https://pubmed.ncbi.nlm.nih.gov/37931167/)). The thick-filament side specifically "*modulates the number of myosin motors available for interaction with calcium-regulated thin filaments*" ([PMID: 33850019](https://pubmed.ncbi.nlm.nih.gov/33850019/)). This interfilament coupling is the molecular mechanism of length-dependent activation — the cellular basis of the Frank–Starling law.

### 8. MYH7 assembles with light chains and partners with MyBP-C, titin, myomesin, and obscurin

Each myosin head's lever arm binds an **essential light chain** and a **regulatory light chain (RLC)** at its IQ motifs (InterPro IPR000048). Within the thick filament, myosin is intimately associated with four accessory proteins that confer structural and regulatory functions: "*In addition to myosin that makes up the backbone of the thick filament, four other proteins which are intimately bound to the thick filament, myosin binding protein-C, titin, myomesin, and obscurin play important structural and regulatory roles*" ([PMID: 29687901](https://pubmed.ncbi.nlm.nih.gov/29687901/)). Myosin-binding protein-C (MyBP-C) directly modulates the stability of the myosin OFF state: cryo-electron tomography of human cardiac thick filaments shows that "*At the third crown, the myosin heads are ordered into the interacting heads motif, but the stability of that motif is affected by myosin-binding protein C*" ([PMID: 38386705](https://pubmed.ncbi.nlm.nih.gov/38386705/)). Titin transmits passive tension and templates filament length; myomesin and obscurin organize the M-band.

### 9. Genotype–function evidence anchors the motor and structural roles

Disease mutations partition by functional sub-region in a way that validates both roles of the protein. **Head/converter mutations** cluster at the actin interface, nucleotide-binding site, and converter/"myosin mesa," and are enriched for hypertrophic cardiomyopathy (HCM); most increase the ON-state fraction, producing hypercontractility: "*cardiac hypercontractility seen in patients with hypertrophic cardiomyopathy is primarily caused by sarcomeric mutations that increase the number of myosin molecules available for actin interaction*" ([PMID: 39192034](https://pubmed.ncbi.nlm.nih.gov/39192034/)). **Rod (light meromyosin) mutations** instead impair thick-filament assembly and cause myosin storage myopathy: "*Myosin storage myopathy (MSM) is a congenital skeletal muscle disorder caused by missense mutations in the β-cardiac/slow skeletal muscle myosin heavy chain rod... MSM mutations map near or within the assembly competence domain known to be crucial for thick filament formation*" ([PMID: 28973424](https://pubmed.ncbi.nlm.nih.gov/28973424/)). A third class — proline substitutions in the rod — causes Laing distal myopathy. This structure–function mapping ties the catalytic function to the head and the scaffolding function to the rod.

### 10. DCM-causing MYH7 mutations over-stabilize the OFF/SRX state — the mirror image of HCM

The dilated cardiomyopathy (DCM) mutation E525K stabilizes the IHM/SRX state, increasing the fraction of heads sequestered away from actin: "*this mutation stabilizes the interacting heads motif (IHM) of myosin and increases the ATPase activity of mutant motor S1 heads*" ([PMID: 42395535](https://pubmed.ncbi.nlm.nih.gov/42395535/)). In iPSC-derived cardiomyocytes, heterozygous E525K reduced contraction markedly: "*Single-cell contraction for E525K hiPSC-CMs decreased by 65%, and isometric twitch force in engineered heart tissues (EHTs) decreased by 39%*" ([PMID: 42395535](https://pubmed.ncbi.nlm.nih.gov/42395535/)) — without impairing the loaded crossbridge cycling of individual motors. Hypocontractility therefore arises from reduced motor *availability* rather than defective individual motors: "*hypo-contractility of DCM myocardium results from reduced function of individual myosin molecules or from decreased myosin availability to interact with actin due to increased IHM/SRX stabilization*" ([PMID: 38709176](https://pubmed.ncbi.nlm.nih.gov/38709176/)). This is the molecular mirror image of HCM, where mutations destabilize the OFF state to increase available (ON) motors.

### 11. MYH7 expression is reciprocally regulated with MYH6 by thyroid hormone and the intronic MyomiR miR-208b

The β-MHC (MYH7) and α-MHC (MYH6) genes are arranged in tandem and reciprocally regulated. Each MHC gene hosts an intronic "MyomiR": "*miR-208a, which is encoded within an intron of alpha-cardiac muscle myosin heavy chain gene (Myh6), was actually a member of a miRNA family that also included miR-208b, which was determined to be encoded within an intron of beta-cardiac muscle myosin heavy chain gene (Myh7)*" ([PMID: 19726871](https://pubmed.ncbi.nlm.nih.gov/19726871/)). These miRNAs control the slow/β-MHC gene program and MHC isoform switching (and also repress THRAP1/MED13 and myostatin). Thyroid hormone signaling acts as a negative regulator of β-MHC via thyroid hormone receptor-α: "*α- and β-myosin heavy chain (MHC) and thyroid hormone receptor-α (TR-α), the negative regulator of β-MHC*" ([PMID: 30696455](https://pubmed.ncbi.nlm.nih.gov/30696455/)). Loss of this repression (e.g., in diabetic or stressed myocardium) raises pro-hypertrophic β-MHC.

### 12. The MYH7 motor domain is deeply conserved, enabling cross-species structural inference

The myosin head is among the most conserved protein modules in eukaryotes, which justifies transferring mechanistic models from invertebrate, avian, and rodent myosins to the human protein. Before recombinant human β-myosin structures were available, the chicken skeletal-muscle myosin S1 crystal structure was used to interpret human HCM mutations: "*The amino acid sequence similarity between chicken skeletal muscle and human beta-cardiac myosin and the three-dimensional structure of the chicken skeletal muscle myosin head have provided the opportunity to examine the structural consequences of these naturally occurring mutations in human beta-cardiac myosin*" ([PMID: 7731997](https://pubmed.ncbi.nlm.nih.gov/7731997/)). The high conservation is quantified by the finding that "*α-subfragment 1 (S1) is far more similar to adult fast skeletal muscle myosin isoforms than to the slow β isoform despite 91% sequence identity between the motor domains of α- and β-myosin*" ([PMID: 22349210](https://pubmed.ncbi.nlm.nih.gov/22349210/)). Conservation is now directly validated by recombinant human β-myosin biochemistry and the 3.6 Å human IHM structure.

---

## Mechanistic Model / Interpretation

MYH7 is best understood as a **two-function protein** — a catalytic motor and a structural scaffold — whose output is gated by overlapping layers of regulation. The following integrates the findings.

### Domain architecture and the two functions

```
   N-terminus                                                        C-terminus
   |---------- HEAD (S1) ----------|-- NECK --|------------- ROD (tail) -------------|
   [ catalytic motor domain ][converter][ lever arm/IQ ][====== coiled-coil ========]
     ATP site + actin interface     |        ELC + RLC        self-assembles into
     (actin-activated ATPase)       |      (light chains)     THICK FILAMENT BACKBONE
            |                        |
     FORCE GENERATION  <-- converter transduces force --> lever-arm swing (~5 nm)
     (power stroke, ~10-12 nm working stroke)
```

- **Enzyme/motor function (head):** Actin-activated ATPase. Substrate = ATP; products = ADP + Pi. Actin binding activates the ATPase and the free energy is transduced through the converter into a swinging lever-arm power stroke (~5 nm lever swing; ~10–12 nm working stroke). ADP release is rate-limiting, giving the slow, economical, strain-sensitive β-motor.
- **Structural function (rod):** The coiled-coil tail self-assembles into the thick-filament backbone; the "assembly competence domain" in the distal rod is essential for polymerization.

### The mechanochemical cycle (per head)

```
   M·ATP  --hydrolysis-->  M·ADP·Pi  --actin binding-->  A·M·ADP·Pi
   (detached, re-cocked)   (primed, weak)                    |
        ^                                                     | Pi release
        |                                                 POWER STROKE
   ATP binding                                                |
        |                                                     v
   A·M  <--  A·M  <----ADP release (RATE-LIMITING in β)----  A·M·ADP
   (rigor, strong)                                        (strong, strained)
```

### Two layers of regulation set the number of active motors

```
   LAYER 1 — Intrinsic ON/OFF switch (autoregulation)
   OFF/SRX (IHM: heads folded on tail, low ATPase) <===> ON/DRX (heads free)
        ^ stabilized by DCM mutations (E525K) -> hypocontractility
        v destabilized by HCM mutations        -> hypercontractility
        modulated by: mavacamten (stabilizes OFF), MyBP-C, S2 length, ionic strength

   LAYER 2 — Dual-filament activation (beat-to-beat control)
   Ca2+ rise --> troponin/tropomyosin shift --> actin sites exposed   (THIN)
   Stretch/load --> titin + MyBP-C mechanosensing --> OFF heads released (THICK)
        => coincidence of both -> length-dependent activation (Frank-Starling)
```

### Disease as a readout of mechanism

The clinical genetics provides a natural experiment confirming the model. Perturbing each functional element produces a predictable phenotype:

| Mutation location | Molecular effect | Available motors | Phenotype |
|---|---|---|---|
| Head / converter (e.g., M493I, HCM) | Destabilize OFF state; altered kinetics | Increased (ON-shift) | Hypertrophic cardiomyopathy (hypercontractile) |
| Converter / motor (E525K, DCM) | Stabilize OFF/IHM-SRX state | Decreased (OFF-shift) | Dilated cardiomyopathy (hypocontractile) |
| Rod — assembly competence domain | Impair thick-filament polymerization | N/A (structural) | Myosin storage myopathy |
| Rod — proline substitutions (e.g., R1500P) | Perturb crossbridging; DRX shift | Altered | Laing distal myopathy |

This bidirectional symmetry — HCM and DCM as opposite perturbations of the same ON/OFF switch — is the central mechanistic insight. It also rationalizes pharmacology: mavacamten (an OFF-stabilizing inhibitor) treats HCM, while myosin activators such as omecamtiv mecarbil target the opposite direction.

### Where and in what pathway MYH7 acts

- **Localization:** Intracellular, in the sarcomere A-band of ventricular cardiomyocytes and slow (type I) skeletal fibers. The rod resides in the thick-filament backbone; the heads project to the filament surface to reach actin.
- **Pathway:** The actomyosin crossbridge cycle at the heart of excitation–contraction coupling, embedded in the dual-filament (thin Ca²⁺/troponin + thick titin/MyBP-C mechanosensing) regulatory network, and transcriptionally governed by thyroid hormone (TR-α) and MyomiR (miR-208b) control of MHC isoform expression.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [15605950](https://pubmed.ncbi.nlm.nih.gov/15605950/) | *Myopathies associated with myosin heavy chain mutations* | Defines motor/ATPase/actin-binding function and the three skeletal MyHC isoforms (type I = MYH7) |
| [41557228](https://pubmed.ncbi.nlm.nih.gov/41557228/) | *Structure of the Myosin Thick Filaments in Muscle* | Hexameric composition; coiled-coil rod backbone; surface heads engage actin |
| [27247418](https://pubmed.ncbi.nlm.nih.gov/27247418/) | *Multidimensional structure-function relationships in human β-cardiac myosin* | Converter/lever-arm power-stroke definition in the human protein |
| [29170849](https://pubmed.ncbi.nlm.nih.gov/29170849/) | *MYH7 mutation associated with two phenotypes of myopathy* | Confirms slow-skeletal/β-cardiac dual identity |
| [22349210](https://pubmed.ncbi.nlm.nih.gov/22349210/) | *Functional differences between recombinant human α and β cardiac myosin motors* | Recombinant single-protein kinetics; β is slow; 1:9 α:β ratio; 91% motor-domain identity |
| [10494800](https://pubmed.ncbi.nlm.nih.gov/10494800/) | *Tuning the human heart molecular motors by myosin light chains* | β-MHC is the slower, lower-ATPase isoform |
| [11017871](https://pubmed.ncbi.nlm.nih.gov/11017871/) | *Visualizing myosin's power stroke in muscle contraction* | Two-stage power stroke; ~5 nm swing / ~12 nm working stroke |
| [11294651](https://pubmed.ncbi.nlm.nih.gov/11294651/) | *Conformation of myosin interdomain interactions during contraction* | Three motor modules: catalytic, converter, lever arm |
| [39192034](https://pubmed.ncbi.nlm.nih.gov/39192034/) | *Reassessing the unifying hypothesis for hypercontractility...* | ON/OFF (IHM) structural regulation; HCM increases ON-state motors |
| [39713291](https://pubmed.ncbi.nlm.nih.gov/39713291/) | *FRET assay for the human β-cardiac myosin IHM* | OFF/IHM resting state; near-atomic structure |
| [37931167](https://pubmed.ncbi.nlm.nih.gov/37931167/) | *Regulating Striated Muscle Contraction: Through Thick and Thin* | Dual-filament paradigm; titin/MyBP-C coupling; Frank–Starling |
| [33850019](https://pubmed.ncbi.nlm.nih.gov/33850019/) | *Stress-dependent activation of myosin in the heart...* | Thick-filament regulation sets number of available motors |
| [29687901](https://pubmed.ncbi.nlm.nih.gov/29687901/) | *Thick Filament Protein Network, Functions, and Disease Association* | MyBP-C, titin, myomesin, obscurin as thick-filament partners |
| [38386705](https://pubmed.ncbi.nlm.nih.gov/38386705/) | *Structure of mavacamten-free human cardiac thick filaments (cryo-ET)* | MyBP-C modulates IHM stability; crown architecture |
| [28973424](https://pubmed.ncbi.nlm.nih.gov/28973424/) | *Myosin storage myopathy mutations yield defective filament assembly* | Rod mutations disrupt assembly — structural role |
| [42395535](https://pubmed.ncbi.nlm.nih.gov/42395535/) | *E525K β-Myosin causes hypocontractility...* | DCM mutation stabilizes IHM; 65%/39% contraction decrease |
| [38709176](https://pubmed.ncbi.nlm.nih.gov/38709176/) | *Tail length and E525K DCM mutant alter SRX state* | DCM hypocontractility via increased IHM/SRX sequestration |
| [19726871](https://pubmed.ncbi.nlm.nih.gov/19726871/) | *MicroRNA-208a is a regulator of cardiac hypertrophy...* | Intronic MyomiR architecture: miR-208b within MYH7 |
| [30696455](https://pubmed.ncbi.nlm.nih.gov/30696455/) | *Early dysregulation of microRNA-208a in diabetic myocardium* | TR-α is the negative regulator of β-MHC |
| [7731997](https://pubmed.ncbi.nlm.nih.gov/7731997/) | *Structural interpretation of β-cardiac myosin HCM mutations* | Chicken-skeletal/human-β conservation enables structural inference |

Supporting literature consistent with the model but not individually cited above includes studies on the SRX↔DRX dynamics and mavacamten ([PMID: 40118457](https://pubmed.ncbi.nlm.nih.gov/40118457/)), the HCM mutation M493I disrupting the SRX state ([PMID: 40501550](https://pubmed.ncbi.nlm.nih.gov/40501550/)), the DCM converter mutation F764L and omecamtiv mecarbil response ([PMID: 31578282](https://pubmed.ncbi.nlm.nih.gov/31578282/)), the Laing-myopathy rod mutation R1500P mouse model ([PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)), skip-residue control of rod assembly ([PMID: 26150528](https://pubmed.ncbi.nlm.nih.gov/26150528/)), LMM-rod HCM mutations ([PMID: 11861413](https://pubmed.ncbi.nlm.nih.gov/11861413/)), and reviews of hereditary myosin myopathies and thick-filament diseases ([PMID: 17434305](https://pubmed.ncbi.nlm.nih.gov/17434305/), [PMID: 19181095](https://pubmed.ncbi.nlm.nih.gov/19181095/)).

### How the evidence converges

The findings are mutually reinforcing across independent methods: **recombinant single-protein biochemistry** (kinetics, ATPase, motility; PMID 22349210), **structural biology** (crystal, cryo-EM, cryo-ET of the IHM at 3.6 Å; PMIDs 7731997, 38386705, 39713291), **biophysics** (fluorescence polarization, X-ray diffraction during length steps; PMID 11017871), **cellular/tissue models** (iPSC cardiomyocytes and engineered heart tissue; PMID 42395535), and **human genetics** (hundreds of disease mutations partitioning by domain). No reviewed paper contradicts the core annotation. The principal area of ongoing refinement concerns whether the biochemical SRX state is strictly identical to the structural IHM — PMID 40118457 shows SRX↔DRX interconversion occurs faster than ATP turnover and persists even in S1 constructs that cannot form the IHM, indicating SRX and IHM are related but not perfectly equivalent.

---

## Limitations and Knowledge Gaps

1. **SRX vs. IHM identity.** The super-relaxed biochemical state and the structural interacting-heads motif are closely linked but may not be strictly identical; subfragment-1 constructs that cannot form the IHM still show SRX-like behavior ([PMID: 40118457](https://pubmed.ncbi.nlm.nih.gov/40118457/)). The precise structural basis of SRX requires further resolution.
2. **Mutation heterogeneity.** Not all HCM mutations are simple "ON-shifters" and not all DCM mutations are "OFF-shifters." Some purified mutant myosins show mixed gain- and loss-of-function effects (e.g., M493I; [PMID: 40501550](https://pubmed.ncbi.nlm.nih.gov/40501550/)), so the unifying ON/OFF framework is a strong first approximation rather than a universal rule.
3. **Species and model caveats.** Much mechanistic detail derives from non-human myosins (chicken, invertebrate, rodent). Although motor-domain conservation is very high and human recombinant data now exist, the full-length human filament in its native lattice remains harder to study; rodent hearts are α-MHC dominant, limiting direct transfer of isoform-switch findings.
4. **Transcriptional regulation detail.** The thyroid-hormone/TR-α and MyomiR (miR-208b) control of the β-MHC program is established, but quantitative, tissue-specific contributions in the healthy adult human heart (which is already β-dominant and does not undergo the rodent-style "fetal switch") are incompletely defined.
5. **Light-chain and partner-protein modulation.** The precise quantitative contributions of essential/regulatory light chains, MyBP-C phosphorylation, and titin-based mechanosensing to setting the ON/OFF balance in vivo are still being mapped.
6. **This report is literature-based.** No primary sequence/structure computation was performed here; conclusions rest on the cited experimental and structural literature and curated database annotations.

---

## Proposed Follow-up Experiments / Actions

1. **Resolve the SRX–IHM relationship** in full-length human β-cardiac myosin using time-resolved cryo-EM combined with single-molecule ATP-turnover measurements, systematically varying S2 tail length, MyBP-C, and ionic strength, to determine which conformational states give rise to the SRX kinetic signature.
2. **Systematic mutation-to-mechanism mapping.** Characterize a panel of HCM and DCM MYH7 mutations with a uniform pipeline (recombinant S1/HMM kinetics + FRET IHM assay + iPSC-cardiomyocyte/engineered-heart-tissue contractility) to test how generally the ON/OFF-shift model predicts phenotype, and to flag mixed-effect exceptions.
3. **Pharmacological validation of the ON/OFF axis.** Quantitatively titrate mavacamten (OFF-stabilizer) against omecamtiv mecarbil and myosin activators across matched HCM/DCM mutant backgrounds to test whether rebalancing the OFF fraction rescues contractility toward wild type.
4. **Rod-assembly structural studies.** Determine high-resolution structures of light-meromyosin segments bearing myosin-storage-myopathy and Laing-myopathy mutations to define how assembly-competence-domain and proline substitutions disrupt coiled-coil packing and filament polymerization.
5. **Human-relevant transcriptional circuits.** Use human iPSC-cardiomyocytes and slow-fiber models to dissect TR-α and miR-208b control of the MYH7/MYH6 locus under physiological and stress stimuli, clarifying the human (β-dominant) isoform-regulation logic.
6. **In-situ filament regulation.** Apply cryo-electron tomography of mechanically loaded human cardiac tissue to visualize, crown-by-crown, how titin- and MyBP-C-dependent mechanosensing releases OFF heads during length-dependent activation, directly linking the dual-filament pathway to the Frank–Starling response.

---

*Report compiled from 12 confirmed findings and 39 reviewed papers over 5 investigation iterations. All factual claims are attributed to the specific primary literature and reviews cited above.*


## Artifacts

- [OpenScientist final report](MYH7-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MYH7-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15605950
2. PMID:27247418
3. PMID:41557228
4. PMID:29170849
5. PMID:22349210
6. PMID:10494800
7. PMID:11294651
8. PMID:11017871
9. PMID:39192034
10. PMID:39713291
11. PMID:37931167
12. PMID:33850019
13. PMID:29687901
14. PMID:38386705
15. PMID:28973424
16. PMID:42395535
17. PMID:38709176
18. PMID:19726871
19. PMID:30696455
20. PMID:7731997
21. PMID:40118457
22. PMID:40501550
23. PMID:31578282
24. PMID:38690726
25. PMID:26150528
26. PMID:11861413
27. PMID:17434305
28. PMID:19181095