---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T01:31:01.767641'
end_time: '2026-10-16T01:54:27.755693'
duration_seconds: 1405.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MYH2
  gene_symbol: MYH2
  uniprot_accession: Q9UKX2
  protein_description: 'RecName: Full=Myosin-2 {ECO:0000305}; AltName: Full=Myosin
    heavy chain 2 {ECO:0000312|HGNC:HGNC:7572}; AltName: Full=Myosin heavy chain 2a;
    Short=MyHC-2a; AltName: Full=Myosin heavy chain IIa; Short=MyHC-IIa; AltName:
    Full=Myosin heavy chain, skeletal muscle, adult 2;'
  gene_info: Name=MYH2 {ECO:0000312|HGNC:HGNC:7572}; Synonyms=MYHSA2;
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MYH2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MYH2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q9UKX2
- **Protein Description:** RecName: Full=Myosin-2 {ECO:0000305}; AltName: Full=Myosin heavy chain 2 {ECO:0000312|HGNC:HGNC:7572}; AltName: Full=Myosin heavy chain 2a; Short=MyHC-2a; AltName: Full=Myosin heavy chain IIa; Short=MyHC-IIa; AltName: Full=Myosin heavy chain, skeletal muscle, adult 2;
- **Gene Information:** Name=MYH2 {ECO:0000312|HGNC:HGNC:7572}; Synonyms=MYHSA2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class myosin-kinesin ATPase
- **Key Domains:** IQ_motif_EF-hand-BS. (IPR000048); Kinesin_motor_dom_sf. (IPR036961); Myosin_head_motor_dom-like. (IPR001609); Myosin_S1_N. (IPR008989); Myosin_tail. (IPR002928)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MYH2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MYH2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MYH2** (gene ID: MYH2, UniProt: Q9UKX2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Human MYH2 (Myosin-2a / Myosin heavy chain IIa)

**Gene:** MYH2 (synonym MYHSA2) · **UniProt:** Q9UKX2 · **HGNC:** 7572
**Organism:** *Homo sapiens* · **Locus:** chromosome 17p13.1 sarcomeric MyHC gene cluster
**Family:** TRAFAC class myosin-kinesin ATPase superfamily; conventional (class II) sarcomeric myosin

---

## 1. Summary

MYH2 encodes **myosin heavy chain IIa (MyHC-IIA)**, the heavy (motor) subunit of the class II sarcomeric myosin that powers contraction of **fast-twitch type 2A skeletal muscle fibers**. Its primary molecular function is that of an **ATP-powered, actin-based molecular motor**: the N-terminal motor head is an actin-activated Mg²⁺-ATPase that, through the cross-bridge cycle, converts the chemical energy of ATP hydrolysis into the mechanical force that slides actin thin filaments past myosin thick filaments and shortens the sarcomere. The protein carries out this function **inside the cytoplasm of skeletal myofibers, as a structural component of the bipolar thick filament in the A-band of the sarcomere**. Its long C-terminal coiled-coil tail is a structural element that dimerizes and self-assembles into the thick-filament backbone. MYH2 operates within the actomyosin / excitation–contraction coupling system of striated muscle; its loss in humans selectively ablates type 2A fibers and causes congenital myopathy with ophthalmoplegia, confirming a non-redundant contractile role.

## 2. Gene/Protein Identity Verification

All lines of evidence agree with the UniProt target. Literature consistently defines MYH2 as "the skeletal muscle myosin heavy chain IIA (MyHC-IIA) isoform, expressed in the fast twitch type 2A fibers" (PMID 33926564), and places it among the three major human extremity-muscle MyHC isoforms — MYH7 (type 1), **MYH2 (type 2A)**, MYH1 (type 2B/2X) (PMID 36380287). Immunohistochemical fiber typing confirms MYH2 → type IIa (PMID 39765480). The domain architecture in UniProt (myosin S1 N-terminal, myosin head motor domain, IQ EF-hand light-chain-binding motif, myosin tail) matches the canonical two-headed coiled-coil myosin II molecule. **Identity is confirmed; no gene-symbol ambiguity.**

## 3. Primary Molecular Function — the Catalyzed Reaction

**Reaction catalyzed:** ATP + H₂O → ADP + inorganic phosphate (Pi), i.e. an **actin-activated Mg²⁺-ATPase**, mechanochemically coupled to force/motion.

**Substrates / partners:**
- **ATP** (substrate hydrolyzed in the motor-head nucleotide pocket)
- **Filamentous (F-)actin** (the track; binding to actin dramatically activates the otherwise slow basal ATPase)
- Associated **essential and regulatory myosin light chains** bound at the IQ-motif neck/lever arm (the IQ_motif/EF-hand domain in UniProt).

**Mechanism (cross-bridge cycle):** "Cyclic interactions between myosin II motors and actin filaments driven by ATP turnover underlie muscle contraction" (PMID 30021113). ATP binding dissociates myosin from actin; hydrolysis to ADP·Pi "recocks" the lever arm (recovery stroke); rebinding to actin triggers Pi release and the **power stroke**, with the force-generating strongly-bound ADP·Pi state being load-sensitive (PMID 39374027, PMID 30021113). The reaction chemistry is conserved across muscle myosins, kinesins and dyneins (PMID 41819442). A disease mutation in the "highly conserved catalytic motor head relay loop" (p.Phe516Val) alters the motor's affinity state, directly implicating the head domain in catalysis and force generation (PMID 33926564).

**Residue-level (bioinformatic) evidence:** Analysis of the retrieved Q9UKX2 sequence (1941 aa) localizes the canonical P-loop NTPase catalytic motifs within the N-terminal ~780-residue motor head: the **Walker-A/P-loop `GESGAGKT` at residues 179–186** (binds ATP phosphates), **Switch I (`SSRFG`, ~244)**, and **Switch II (`DIAGFE`, the DxxG motif, ~464)** — the elements that sense the γ-phosphate and couple hydrolysis to the actin-binding cleft and lever arm. The disease residue p.Phe516Val (relay loop) lies just downstream of Switch II, and the filament assembly-competence sequence maps to the distal coiled coil (~aa 1877–1905). This confirms, independently of database annotation, that MYH2 is a genuine myosin-family P-loop ATPase.

**Fiber-level consequence:** Type 2A fibers are fast, fatigue-resistant oxidative-glycolytic fibers. Single-fiber mechanics studies that classify fibers by MyHC content (SDS-PAGE) show MyHC-IIa fibers have high maximal unloaded shortening velocity and power relative to slow type I fibers (PMID 16322375, PMID 15142838), reflecting the intrinsic fast ATPase/cross-bridge kinetics of the MYH2 motor.

## 4. Structural Role and the Myosin Molecule

MYH2 is a **bipartite structural-plus-catalytic protein**:
- **N-terminal globular motor head (S1):** actin-binding + ATPase catalytic machinery.
- **Neck / lever arm:** IQ motifs bind essential and regulatory light chains; acts as a rigid lever amplifying small nucleotide-pocket conformational changes into a large working stroke.
- **C-terminal α-helical coiled-coil tail (rod / S2 + LMM):** two heavy chains dimerize into a coiled coil; many dimers pack in a staggered, bipolar array to build the **thick filament**. A "filament assembly region (aa 1877–1905)" in the distal tail is required for incorporation into filaments; a splice variant deleting residues 1860–1891 disrupts type 2A fibers (PMID 36380287). Truncation of the proximal tail (p.Gln1111*) likewise causes myopathy with myofilamentous tangles (PMID 33926564). Thus the tail is a genuine **structural self-assembly domain**, not merely a spacer.

## 5. Subcellular Localization / Site of Action

MYH2 acts **intracellularly within the cytoplasm of skeletal muscle fibers**, specifically as part of the **thick filament of the sarcomere (A-band)** of the myofibril. Its motor heads project radially to engage actin thin filaments; its tails form the filament backbone. The mapping of pathogenic variants to the filament-assembly tail region and the appearance of disorganized myofibrils / myofilamentous tangles in MYH2 myopathy (PMID 33926564, PMID 36380287) directly place the protein in the contractile apparatus of the muscle cell.

## 5b. Regulation of the Motor (Lever Arm, Light Chains, and the Super-Relaxed State)

**Lever-arm amplification and light chains.** Myosins are allosteric enzymes whose small active-site changes are amplified by a **lever arm** (converter + elongated light-chain-binding neck) as Pi then ADP are released (PMID 22171985). The **IQ-motif/EF-hand neck** (matching UniProt's IPR000048 annotation) binds **essential (ELC) and regulatory (RLC) light chains**, which stabilize the lever arm and track its pre-/post-power-stroke rotation (PMID 21819137). Light-chain identity *tunes* output: skeletal S1 bearing the A1 ELC undergoes a markedly larger power stroke and has higher catalytic efficiency and actin affinity than S1 with A2 ELC (PMID 25825773). Thus MYH2's force magnitude is set not only by its heavy-chain sequence but by its associated light chains.

**Thick-filament "off" state (super-relaxed state, SRX).** In resting muscle a large fraction of sarcomeric myosin heads enter a **super-relaxed state** with ultraslow ATP turnover (~30 min turnover vs. seconds when active), structurally the **interacting-heads motif (IHM)** in which the paired heads fold back and dock onto the thick-filament core, switching off ATPase activity (PMID 21763701, PMID 26851071). This off state is a conserved, energy-conserving contractile reserve, released by RLC phosphorylation, and different sarcomeric isoforms partition differently into it (PMID 36334627). MYH2 therefore participates in **thick-filament-based regulation**, not only thin-filament (Ca²⁺/troponin) control.

## 5c. Molecular Interaction Context (Thick-Filament Co-Assembly)

In situ the MYH2 motor is the backbone of a regulated macromolecular assembly. Its thick filament is decorated by **myosin binding protein-C (MyBP-C)**, a major thick-filament-associated protein that organizes at defined axial repeats in the A-band C-zone and regulates sarcomere assembly and cross-bridge formation; skeletal MyBP-C mutations cause distal arthrogryposis (PMID 22415774). The motor heads engage **F-actin** thin filaments (with associated tropomyosin/troponin providing Ca²⁺ gating) and the filament is spanned by titin. Thus MYH2's activity is embedded in, and tuned by, the thin-filament regulatory system and thick-filament accessory proteins.

## 6. Pathway / Physiological Context

MYH2 is the effector motor of the **actomyosin cross-bridge cycle** within **excitation–contraction coupling**: a motor-neuron action potential → acetylcholine → sarcolemmal depolarization → Ca²⁺ release from sarcoplasmic reticulum → Ca²⁺–troponin/tropomyosin de-repression of actin → **MYH2 cross-bridge cycling and force production** → sarcomere shortening. MYH2 specifically endows **fast type 2A fibers** with their rapid, powerful, fatigue-resistant contractile phenotype. These type 2A fibers are not fixed entities but occupy a plastic functional/metabolic continuum between slow type I and faster type IIx; hybrid fibers co-expressing MyHC isoforms (I–IIa, IIa–IIx) are transitional states that shift with training and aging (PMID 30907516), and type IIA is a major, reproducible component of human limb muscle (PMID 37424380). Fiber-type identity (and hence MYH2 expression) is developmentally and activity-regulated: soft-substrate/low-load and PGC-1α signaling push toward MYH7/MYH2 (slow/oxidative) programs (PMID 40781258), and during prenatal development embryonic/neonatal MyHC isoforms transition to mature type I/IIA/IIB, with type IIA becoming predominant (PMID 40959669).

## 6b. Upstream Regulation and Evolution

**Neural/activity control of expression.** MYH2 abundance and fiber distribution are not fixed: the firing pattern of the innervating motor neuron is transduced by **Ca²⁺/calcineurin–NFAT** signaling, which acts as a nerve-activity sensor controlling activity-dependent MyHC switching (PMID 15247427). Denervation and exercise training remodel the MyHC IIa/IIx/I balance in parallel with calcineurin/NFATc1 activity (PMID 25435788). MYH2 is thus a tunable downstream effector in the neural control of muscle phenotype.

**Evolution.** Sarcomeric MYH genes (including MYH2) form a tandemly duplicated multigene family in vertebrates; the catalytic **head and the structural rod evolve at different rates**, reflecting distinct functional constraints on the motor versus the coiled-coil tail (PMID 15014174) — consistent with the two-module architecture described above.

## 7. Genetic Evidence for Non-redundant Function (Human Loss-of-Function)

- **Recessive MYH2 myopathy:** early-onset, non-progressive diffuse weakness with ophthalmoplegia; biopsy shows "near or complete absence of type 2A fibers" (PMID 29934118) — the cleanest proof that MYH2 is the fiber-defining motor of type 2A fibers.
- **Dominant MYH2 myopathy:** ophthalmoplegia + progressive proximal weakness with rimmed vacuoles/inclusions, historically "hereditary inclusion body myopathy 3 (IBM3)" (PMID 29934118, PMID 15548556); additional phenotypes include nemaline rods and myofilamentous tangles (PMID 33926564) and dominant splice variants in the assembly domain (PMID 36380287). The clinical spectrum continues to expand (PMID 41851877).
- The prominent **ophthalmoplegia** indicates extraocular muscles are especially MYH2-dependent.
- MYH2 lies in the **chromosome 17p13.1 sarcomeric MyHC gene cluster** with MYH1/MYH3/MYH8 etc. (PMID 15548556).

## 8. Supported vs. Refuted Hypotheses

**Supported:**
- MYH2 is an ATP-powered actin-based motor (actin-activated ATPase) — supported by myosin-II mechanistic literature and motor-head mutation data.
- MYH2 = heavy chain of type 2A fast-fiber myosin — supported by fiber typing + loss-of-function biopsies.
- C-terminal tail is a structural thick-filament assembly domain — supported by assembly-region mutation data.
- Localization to sarcomere/thick filament — supported by pathology.

**Refuted / not supported:** No evidence that MYH2 is a signaling molecule, transporter, or enzyme acting on small-molecule metabolites; it is a structural-motor protein. No evidence of extracellular or nuclear function.

## 9. Limitations & Future Directions

- Most quantitative biophysics (single-molecule force, ATPase rates, load dependence) derives from cardiac/slow (β) or rodent fast myosins; direct single-molecule kinetic constants for the **human MyHC-IIA** isoform specifically are comparatively sparse. Isoform-resolved human MyHC-IIA biophysics would refine substrate kinetics.
- Light-chain composition and super-relaxed (SRX)/disordered-relaxed state regulation, well studied for cardiac myosin, remain less characterized for MyHC-IIA.
- A high-resolution human MyHC-IIA motor-domain structure would allow precise mapping of catalytic residues and disease variants.

---

### Key References (PMIDs)
33926564 (gene product identity, motor relay loop); 36380287 (isoform-fiber assignment, tail filament-assembly domain); 29934118 (recessive/dominant myopathy, type 2A fiber loss); 15548556 (chr17 MyHC cluster, IBM3); 39765480 (MYH2→type IIa immunohistochemistry); 30021113 & 39374027 & 41819442 (myosin-II ATPase/cross-bridge mechanism); 16322375 & 15142838 (MyHC-IIa fiber contractile velocity/power); 40781258 & 40959669 (fiber-type regulation/development); 41851877 (clinical spectrum).


## Artifacts

- [OpenScientist final report](MYH2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MYH2-deep-research-openscientist_artifacts/final_report.pdf)