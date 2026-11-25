---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T02:02:07.718797'
end_time: '2026-10-04T02:27:40.411111'
duration_seconds: 1532.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: SIZ1
  gene_symbol: SIZ1
  uniprot_accession: Q680Q4
  protein_description: 'RecName: Full=E3 SUMO-protein ligase SIZ1 {ECO:0000303|PubMed:15894620};
    EC=2.3.2.- {ECO:0000305}; AltName: Full=E3 SUMO-protein transferase SIZ1 {ECO:0000305};'
  gene_info: Name=SIZ1 {ECO:0000303|PubMed:15894620}; OrderedLocusNames=At5g60410
    {ECO:0000312|Araport:AT5G60410}; ORFNames=MUF9.5 {ECO:0000312|EMBL:BAB08225.1},
    MUF9.70;
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the PIAS family. .
  protein_domains: SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); SIZ1/2_SP-RING.
    (IPR031141); Zinc_finger_PHD-type_CS. (IPR019786); Znf_FYVE_PHD. (IPR011011)
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
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SIZ1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SIZ1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q680Q4
- **Protein Description:** RecName: Full=E3 SUMO-protein ligase SIZ1 {ECO:0000303|PubMed:15894620}; EC=2.3.2.- {ECO:0000305}; AltName: Full=E3 SUMO-protein transferase SIZ1 {ECO:0000305};
- **Gene Information:** Name=SIZ1 {ECO:0000303|PubMed:15894620}; OrderedLocusNames=At5g60410 {ECO:0000312|Araport:AT5G60410}; ORFNames=MUF9.5 {ECO:0000312|EMBL:BAB08225.1}, MUF9.70;
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the PIAS family. .
- **Key Domains:** SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); SIZ1/2_SP-RING. (IPR031141); Zinc_finger_PHD-type_CS. (IPR019786); Znf_FYVE_PHD. (IPR011011)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SIZ1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SIZ1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SIZ1** (gene ID: SIZ1, UniProt: Q680Q4) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *Arabidopsis thaliana* SIZ1 (E3 SUMO-protein ligase SIZ1)

**UniProt:** Q680Q4 · **Gene:** SIZ1 · **Locus:** At5g60410 (ORF MUF9.5/MUF9.70) · **Organism:** *Arabidopsis thaliana* (mouse-ear cress) · **EC:** 2.3.2.- · **Family:** Siz/PIAS SUMO E3 ligase family

---

## Summary

**SIZ1 (SAP AND MIZ1 DOMAIN-CONTAINING LIGASE 1; At5g60410; UniProt Q680Q4) is the principal SUMO (Small Ubiquitin-like MOdifier) E3 ligase of *Arabidopsis thaliana*.** It belongs to the Siz/PIAS (SP-RING) family of SUMO ligases and catalyzes the final, substrate-selective step of the SUMO conjugation cascade (EC 2.3.2.-): using its catalytic SP-RING (MIZ1) zinc-binding domain, it accelerates the transfer of the SUMO1/SUMO2 modifier from the charged E2 conjugating enzyme SCE1 onto specific lysine residues of target proteins. Gene identity is unambiguous and confirmed — the UniProt accession Q680Q4, the gene symbol SIZ1, the locus At5g60410, the PIAS family assignment, and the SAP + PINIT + SP-RING + PHD domain architecture all match the primary experimental literature ([PMID: 15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/), [PMID: 19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/)). There was no gene-symbol ambiguity: a direct, well-populated primary literature exists for this exact protein.

**Where it acts:** SIZ1 functions predominantly in the **nucleus**, where it is observed in nuclear foci and, during pathogen challenge, in MAC-dependent nuclear condensates ([PMID: 15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/), [PMID: 41986387](https://pubmed.ncbi.nlm.nih.gov/41986387/)). Consistent with this, SIZ1 drives the bulk of stress-induced sumoylation, with most SUMO1/SUMO2 conjugates accumulating in the nucleus ([PMID: 17644626](https://pubmed.ncbi.nlm.nih.gov/17644626/)). Its substrate repertoire is dominated by nuclear transcription factors and chromatin regulators.

**What it does functionally:** SIZ1 is a post-translational **signaling hub**. By SUMO-modifying defined lysines on specific transcription factors and regulators, it tunes their stability, activity, or localization, thereby integrating multiple environmental and developmental signaling pathways: phosphate-starvation responses (via PHR1), cold/freezing tolerance (via ICE1→CBF3/DREB1A), heat/thermotolerance (via NF-YC10 and HAT1), ABA signaling (via ABI5 and MYB30), salicylic-acid-dependent innate immunity (via the PAD4 pathway and the MOS4-Associated Complex), and flowering time (via FLD and FLC). Its own activity is further tuned by condition-specific post-translational modification — drought favors SIZ1 sumoylation while heat triggers COP1-dependent ubiquitination, with the retromer protein VPS29 stabilizing the ligase. The function is strongly conserved across plants, as rice (OsSIZ1), tomato (SlSIZ1), and pepper (CaDSIZ1) orthologs confer analogous stress tolerance.

---

## Key Findings

### Finding 1 — SIZ1 is a SUMO E3 ligase of the SP-RING/PIAS family that drives global sumoylation

The founding characterization of this protein by Miura et al. (2005) established that AtSIZ1 possesses **SUMO E3 ligase activity in vitro**, and that `siz1` T-DNA insertion mutants display an **impaired global protein sumoylation profile** on immunoblots ([PMID: 15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/)). This places SIZ1 as a focal SUMO-conjugation enzyme rather than a narrow, single-substrate regulator. The protein's identity is firmly tied to UniProt Q680Q4: gene SIZ1, locus At5g60410, PIAS family, bearing SAP, PINIT, SP-RING, and PHD domains. The verbatim evidence: *"AtSIZ1 has SUMO E3 ligase activity in vitro, and immunoblot analysis revealed that the protein sumoylation profile is impaired in siz1 plants."*

### Finding 2 — SIZ1 is a nuclear enzyme acting in nuclear foci and pathogen-induced condensates

AtSIZ1-GFP localizes to **nuclear foci** ([PMID: 15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/): *"AtSIZ1-GFP was localized to nuclear foci"*). This localization is mechanistically consistent with its substrate set, which comprises nuclear transcription factors and regulators (PHR1, ICE1, ABI5, MYB30, TPR1, HLS1, FLD, FLC, NF-YC10, HAT1, AL6). Importantly, subcellular targeting can be redirected by alternative splicing: a heat-induced splice variant (SSV2) localizes instead to the **plasma membrane** and sumoylates the cyclic-nucleotide-gated channel CNGC6, while canonical SIZ1 and the other splice variants (SSV1/SSV3/SSV4) remain nuclear ([PMID: 38497423](https://pubmed.ncbi.nlm.nih.gov/38497423/): *"SSV2 mainly localized to the plasma membrane, whereas SIZ1, SSV1/SSV4, and SSV3 localized to the nucleus"*). This demonstrates that the baseline functional compartment of SIZ1 is the nucleus, with specialized isoforms expanding its reach.

### Finding 3 — SIZ1 controls phosphate-starvation responses by sumoylating the MYB transcription factor PHR1

`siz1` mutants display exaggerated phosphate (Pi) starvation morphology — arrested primary root growth, enhanced lateral root and root hair proliferation, increased root/shoot ratio, and anthocyanin accumulation — despite having wild-type intracellular Pi levels ([PMID: 15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/)). The mechanistic link is **PHR1**, a MYB transcriptional activator of the Pi-responsive genes AtIPS1 and AtRNS1, which is a direct SIZ1 sumoylation target: *"PHR1, a MYB transcriptional activator of AtIPS1 and AtRNS1, is an AtSIZ1 sumoylation target."* AtIPS1 and AtRNS1 are induced more slowly in `siz1` under Pi limitation, showing that SIZ1-mediated sumoylation of PHR1 shapes the kinetics and amplitude of the phosphate-deficiency transcriptional program.

### Finding 4 — SIZ1-mediated sumoylation of ICE1 promotes CBF3/DREB1A cold signaling and freezing tolerance

Miura et al. (2007) showed that `siz1` alleles cause **freezing and chilling sensitivity** that is rescued by SIZ1, and that cold-induced CBF3/DREB1A expression is repressed in `siz1` ([PMID: 17416732](https://pubmed.ncbi.nlm.nih.gov/17416732/)). The specific mechanism is sumoylation of the transcription factor **ICE1** at lysine 393: *"A K393R substitution in ICE1 [ICE1(K393R)] blocked SIZ1-mediated sumoylation in vitro and in protoplasts identifying the K393 residue as the principal site of SUMO conjugation."* SUMO conjugation stabilizes ICE1 by antagonizing its ubiquitination — *"Sumoylation of recombinant ICE1 reduced polyubiquitination of the protein in vitro"* — while the non-sumoylatable ICE1(K393R) represses CBF3, elevates the CBF repressor MYB15, and increases freezing sensitivity ([PMID: 19704769](https://pubmed.ncbi.nlm.nih.gov/19704769/)). This is a paradigmatic example of SUMO/ubiquitin cross-talk controlling a key stress transcription factor.

### Finding 5 — SIZ1 negatively regulates salicylic-acid-dependent innate immunity through the PAD4 pathway

Lee et al. (2007) found that `siz1` mutants exhibit **constitutive systemic acquired resistance (SAR)**: elevated salicylic acid (SA), increased PR (pathogenesis-related) gene expression, and enhanced resistance to *Pseudomonas syringae* pv. tomato DC3000, all reverted to wild type by the SA-degrading NahG transgene ([PMID: 17163880](https://pubmed.ncbi.nlm.nih.gov/17163880/): *"Mutant siz1 plants exhibit constitutive systemic-acquired resistance (SAR) characterized by elevated accumulation of salicylic acid (SA), increased expression of pathogenesis-related (PR) genes"*). Epistasis analyses (with `npr1`, `pad4`, `ndr1`) place SIZ1 in the **PAD4-dependent** branch of SA signaling: *"SIZ1 interacts epistatically with PAD4 to regulate PR expression and disease resistance."* JA/PDF1.2 responses and *Botrytis* susceptibility were unchanged, indicating specificity for the SA arm.

### Finding 6 — SIZ1 negatively regulates ABA signaling by sumoylating ABI5 and MYB30

`siz1` mutants are **ABA-hypersensitive** (enhanced germination arrest and root-growth inhibition), and SIZ1 sumoylates the bZIP transcription factor **ABI5** at lysine 391 ([PMID: 19276109](https://pubmed.ncbi.nlm.nih.gov/19276109/): *"A K391R substitution in ABI5 [ABI5(K391R)] blocked SIZ1-mediated sumoylation of the transcription factor ... K391 is the principal site for SUMO conjugation"*). The mutant `abi5-4` is epistatic to `siz1`, placing ABI5 downstream. SUMO conjugation to ABI5 represses its activity while also protecting it from degradation ([PMID: 20514240](https://pubmed.ncbi.nlm.nih.gov/20514240/)). A second ABA-pathway substrate is **MYB30**, sumoylated at lysine 283 ([PMID: 22814374](https://pubmed.ncbi.nlm.nih.gov/22814374/): *"A K283R substitution in MYB30 blocks its SUMO E3 ligase SIZ1-mediated sumoylation in Arabidopsis protoplasts ... K283 is the principal site"*). SIZ1 thus coordinates sumoylation of two transcription factors to balance ABA-responsive gene expression.

### Finding 7 — Domain architecture: SP-RING is catalytic and nuclear-targeting; PHD and PINIT are required for in vivo sumoylation

Structure–function dissection by Cheong et al. (2009) mapped SIZ1's domains ([PMID: 19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/)). SIZ1 contains **SAP, PINIT, SP-RING, and SXS motifs plus a plant-specific PHD finger**. Point-mutation complementation of `siz1-2` established a division of labor among the domains:

| Domain | Role established by mutagenesis |
|---|---|
| **SP-RING (MIZ1)** | *"Domain SP-RING is required for SUMO conjugation activity and nuclear localization of SIZ1"* — catalytic core and nuclear targeting |
| **PHD zinc finger** | *"Mutations of the PHD zinc finger domain and the PINIT motif affected in vivo SUMOylation"* — efficient substrate sumoylation in vivo |
| **PINIT** | Required for in vivo sumoylation |
| **SXS** | Controls SA accumulation and cotyledon greening |
| **SAP** | DNA/chromatin association (scaffold attachment); PHD/PINIT alleles also affected sugar- and light-responsive hypocotyl elongation |

This explains how a single enzyme couples substrate engagement (PHD/PINIT/SAP) to catalysis (SP-RING).

### Finding 8 — SIZ1 promotes heat-stress tolerance by sumoylating heat-response transcription factors (NF-YC10, HAT1)

SIZ1 is central to thermotolerance. Huang et al. (2023) showed that SIZ1 interacts with and **SUMOylates NF-YC10** during heat stress, facilitating NF-YB3 nuclear translocation and assembly of the NF-Y complex required for heat-responsive gene expression ([PMID: 36282496](https://pubmed.ncbi.nlm.nih.gov/36282496/): *"the SUMO ligase SIZ1 ... interacts with NF-YC10 and enhances its SUMOylation during HS"*). Lao et al. (2026) demonstrated that high temperature induces SIZ1 accumulation; SIZ1 then **SUMOylates HAT1**, promoting HAT1 degradation and thereby relieving HAT1's repression of heat-shock protein genes ([PMID: 42260756](https://pubmed.ncbi.nlm.nih.gov/42260756/): *"high temperature induces the accumulation of the SIZ1 protein, which promotes its interaction with HAT1 and SUMOylation of HAT1, thereby facilitating the degradation of HAT1"*). SIZ1 is also required for warm-temperature thermomorphogenesis at 28 °C ([PMID: 34106243](https://pubmed.ncbi.nlm.nih.gov/34106243/)).

### Finding 9 — SIZ1 regulates flowering time via FLC: sumoylating FLD and stabilizing FLC

SIZ1 promotes FLC-mediated floral repression through two converging mechanisms. First, it **sumoylates FLD**, an autonomous-pathway component, thereby repressing FLD and maintaining FLC expression ([PMID: 18069938](https://pubmed.ncbi.nlm.nih.gov/18069938/): *"SIZ1 facilitates sumoylation of FLD that can be suppressed by mutations in three predicted sumoylation motifs in FLD"*); the non-sumoylatable FLD-K3R reduces FLC transcription and histone H4 acetylation. Second, SIZ1 directly **stabilizes FLC protein** ([PMID: 24218331](https://pubmed.ncbi.nlm.nih.gov/24218331/): *"inducible AtSIZ1 overexpression led to an increase in the concentration of FLC and delayed the post-translational decay of FLC, indicating that AtSIZ1 stabilizes FLC through direct binding"*). Consistently, `siz1` flowers early under short days, a phenotype that is partly SA-dependent (reversed by NahG).

### Finding 10 — SIZ1 activity is itself tuned by condition-specific post-translational modification (COP1, VPS29)

The ligase is a regulated node, not a constitutive enzyme. Kim et al. (2017) showed that **drought induces sumoylation of AtSIZ1** (accumulation of sumoylated forms), whereas **heat induces COP1-dependent ubiquitination** of AtSIZ1, with the SUMO protease ESD4 enhancing heat-induced ubiquitination ([PMID: 28979848](https://pubmed.ncbi.nlm.nih.gov/28979848/): *"drought stress induced sumoylation rather than ubiquitination of AtSIZ1 and sumoylated forms of AtSIZ1 accumulated"*). Min et al. (2025) identified the retromer protein **VPS29** as a positive stabilizer: it binds AtSIZ1 and inhibits its ubiquitin-dependent degradation ([PMID: 40286281](https://pubmed.ncbi.nlm.nih.gov/40286281/): *"AtVPS29 inhibits ubiquitination pathway-dependent degradation of AtSIZ1"*); loss of VPS29 depletes SIZ1, accumulates COP1, and produces `siz1`-like SA/ROS phenotypes.

### Finding 11 — SIZ1 is the principal plant SUMO E3 ligase coordinating a broad stress and developmental program, with conserved orthologs

The authoritative review by Elrouby (2017) summarizes SUMO/SIZ1-regulated processes: *"roles in biotic and abiotic stress responses, phosphate starvation, nitrate and sulphur metabolism, freezing and drought tolerance and response to excess copper"*, intersecting with SA, ABA, gibberellin, and auxin signaling and with COP1/PhyB light signaling ([PMID: 28197916](https://pubmed.ncbi.nlm.nih.gov/28197916/)). Functional conservation is strong: heterologous overexpression of the rice ortholog **OsSIZ1** confers simultaneous drought, heat, and salt tolerance and higher proline in Arabidopsis and crops ([PMID: 30092010](https://pubmed.ncbi.nlm.nih.gov/30092010/): *"over-expression of the rice gene OsSIZ1 in Arabidopsis leads to increased tolerance to multiple abiotic stresses"*; [PMID: 28340002](https://pubmed.ncbi.nlm.nih.gov/28340002/)). Tomato SlSIZ1 ([PMID: 27995772](https://pubmed.ncbi.nlm.nih.gov/27995772/)) and pepper CaDSIZ1 ([PMID: 35672943](https://pubmed.ncbi.nlm.nih.gov/35672943/)) likewise confer drought tolerance.

### Finding 12 — SIZ1 catalyzes the E3 step of the SUMO cascade, conjugating SUMO1/SUMO2 to nuclear proteins, and drives bulk stress-induced sumoylation

Saracco et al. (2007) placed SIZ1 within the complete Arabidopsis SUMO cascade: E1 (SAE1/SAE2), E2 (SCE1), E3 (SIZ1) ([PMID: 17644626](https://pubmed.ncbi.nlm.nih.gov/17644626/)). SAE2 and SCE1 nulls are embryo-lethal, and `sum1 sum2` double mutants are embryo-lethal, demonstrating that SUMO1/2 conjugation is essential. Stress (e.g., heat shock) dramatically increases SUMO1/SUMO2 conjugates, an increase *"mainly driven by the SUMO protein ligase SIZ1, with most of the conjugates accumulating in the nucleus."* Kwak et al. (2024) directly defined substrate–modifier specificity: SIZ1 and its splice variants *"exhibited similar E3 SUMO ligase activities and preferred SUMO1 and SUMO2 for their E3 ligase activity"* ([PMID: 38497423](https://pubmed.ncbi.nlm.nih.gov/38497423/)). This fixes the core biochemistry: **SIZ1 is the E3 that conjugates SUMO1/SUMO2 (not the non-canonical paralogs) to predominantly nuclear substrates.**

### Finding 13 — SIZ1 acts within MAC-dependent nuclear condensates to potentiate immune signaling

A more recently discovered positive, context-dependent immune role complements the negative SA role of Finding 5. Jia et al. (2026) showed that SIZ1 overaccumulation activates robust immune responses and cell death dependent on its E3 ligase activity ([PMID: 41986387](https://pubmed.ncbi.nlm.nih.gov/41986387/)). Proximity-labeling proteomics revealed convergence on the **MOS4-Associated Complex (MAC)**: *"Both SIZ1 and the immune receptor SNC1 are recruited to MAC-dependent nuclear condensates (MDNCs) upon pathogen challenge, where they synergistically potentiate immune responses and cell death."* Mechanistically, *"SIZ1 SUMOylates and stabilizes MAC components, reinforcing MDNC formation and sustaining immune signaling,"* counteracting karyopherin KA120-mediated condensate disassembly. SIZ1 therefore both restrains basal SA immunity and reinforces activated immune condensates in a dose- and context-dependent manner.

---

## Mechanistic Model / Interpretation

### The SUMO conjugation cascade and SIZ1's position in it

```
        SUMO1 / SUMO2  (preferred modifiers; essential, nuclear)
             |
   [E1]  SAE1 / SAE2  — ATP-dependent activation (embryo-lethal if lost)
             |
   [E2]  SCE1          — conjugating enzyme, charged with SUMO (embryo-lethal if lost)
             |
   [E3]  >>> SIZ1 <<<  — SP-RING ligase: substrate selection + catalysis
             |          (PHD/PINIT/SAP engage substrate; SP-RING transfers SUMO)
             v
   Substrate-Lys–SUMO  (mostly NUCLEAR transcription factors / chromatin regulators)
             ^
   [reversal] ESD4 / ULP1c / ULP1d  — SUMO proteases (deSUMOylation)
```

SIZ1 is the **specificity-conferring enzyme** of an otherwise essential, housekeeping cascade. Whereas E1 and E2 losses are embryo-lethal, `siz1` plants are viable but stress-hypersensitive and developmentally altered — the signature of a regulator that shapes *which* proteins get modified *under which conditions*, rather than a core-survival factor.

### SIZ1 as a signaling hub: one enzyme, many pathways

| Pathway / Stress | Substrate(s) | Site | Molecular consequence | SIZ1 role | Key refs |
|---|---|---|---|---|---|
| Phosphate starvation | PHR1 (MYB) | — | Tunes Pi-response gene kinetics | Modulator | [15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/) |
| Cold / freezing | ICE1 (bHLH) | K393 | SUMO blocks ubiquitin → ICE1 stable → CBF3↑, MYB15↓ | Positive | [17416732](https://pubmed.ncbi.nlm.nih.gov/17416732/) |
| Heat / thermotolerance | NF-YC10; HAT1 | — | NF-Y assembly↑; HAT1 degraded → HSP genes derepressed | Positive | [36282496](https://pubmed.ncbi.nlm.nih.gov/36282496/), [42260756](https://pubmed.ncbi.nlm.nih.gov/42260756/) |
| ABA signaling | ABI5 (bZIP); MYB30 | K391; K283 | Represses TF activity; balances ABA genes | Negative | [19276109](https://pubmed.ncbi.nlm.nih.gov/19276109/), [22814374](https://pubmed.ncbi.nlm.nih.gov/22814374/) |
| SA innate immunity | PAD4 pathway; TPR1 | — | Restrains constitutive SAR | Negative (basal) | [17163880](https://pubmed.ncbi.nlm.nih.gov/17163880/) |
| Activated immunity | MAC components | — | Stabilizes MDNCs, sustains signaling | Positive (induced) | [41986387](https://pubmed.ncbi.nlm.nih.gov/41986387/) |
| Flowering time | FLD; FLC | FLD motifs; — | FLD repressed → FLC maintained; FLC stabilized | Represses flowering | [18069938](https://pubmed.ncbi.nlm.nih.gov/18069938/), [24218331](https://pubmed.ncbi.nlm.nih.gov/24218331/) |
| Cadmium tolerance | (GSH/PC pathway) | — | GSH1/2, PCS1/2 induced | Positive | [35718335](https://pubmed.ncbi.nlm.nih.gov/35718335/) |
| Apical hook / light | HLS1 | — | SUMO promotes active HLS1 oligomers | Positive | [36890719](https://pubmed.ncbi.nlm.nih.gov/36890719/) |
| Seed dormancy | AL6 | K181 | Protects AL6; represses DOG1 | Positive | [39562527](https://pubmed.ncbi.nlm.nih.gov/39562527/) |

A recurring biochemical theme is **SUMO–ubiquitin cross-talk**: SUMO conjugation competes with ubiquitination to stabilize substrates (ICE1, FLC, AL6), or — in the opposite direction — primes a substrate for degradation (HAT1). The net effect depends on the substrate and context, which is why SIZ1 can act as a positive regulator in one pathway and a negative regulator in another.

### Self-regulation closes the loop

SIZ1 abundance and modification state are themselves environmentally gated: **drought → SIZ1 sumoylation (stabilizing/active)**, **heat → COP1-dependent ubiquitination (turnover)**, with **ESD4** promoting heat-induced ubiquitination and **VPS29** opposing degradation. This provides a mechanism by which the cell sets the overall "gain" of nuclear sumoylation according to the prevailing stress.

---

## Evidence Base

| PMID | Study (abbrev.) | Contribution |
|---|---|---|
| [15894620](https://pubmed.ncbi.nlm.nih.gov/15894620/) | Miura 2005 | Founding paper: SIZ1 = SUMO E3 ligase; nuclear foci; PHR1/phosphate |
| [17644626](https://pubmed.ncbi.nlm.nih.gov/17644626/) | Saracco 2007 | SUMO cascade genetics; SIZ1 drives nuclear SUMO1/2 conjugation under stress |
| [38497423](https://pubmed.ncbi.nlm.nih.gov/38497423/) | Kwak 2024 | SUMO1/SUMO2 modifier preference; splice variants / localization |
| [17416732](https://pubmed.ncbi.nlm.nih.gov/17416732/) | Miura 2007 | ICE1-K393 sumoylation; cold/freezing; SUMO vs ubiquitin |
| [19704769](https://pubmed.ncbi.nlm.nih.gov/19704769/) | Miura 2009 (addendum) | ICE1 sumoylation represses MYB15; cold model |
| [17163880](https://pubmed.ncbi.nlm.nih.gov/17163880/) | Lee 2007 | SIZ1 negatively regulates SA/SAR via PAD4 |
| [19276109](https://pubmed.ncbi.nlm.nih.gov/19276109/) | Miura 2009 | ABI5-K391 sumoylation; ABA signaling |
| [22814374](https://pubmed.ncbi.nlm.nih.gov/22814374/) | Zheng 2012 | MYB30-K283 sumoylation; ABA |
| [19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/) | Cheong 2009 | Domain dissection: SP-RING catalytic/nuclear; PHD/PINIT for in vivo activity |
| [36282496](https://pubmed.ncbi.nlm.nih.gov/36282496/) | Huang 2023 | NF-YC10 sumoylation; NF-Y assembly; thermotolerance |
| [42260756](https://pubmed.ncbi.nlm.nih.gov/42260756/) | Lao 2026 | HAT1 sumoylation/degradation; thermotolerance |
| [34106243](https://pubmed.ncbi.nlm.nih.gov/34106243/) | Hammoudi 2021 | SIZ1 required for thermomorphogenesis at 28 °C |
| [18069938](https://pubmed.ncbi.nlm.nih.gov/18069938/) | Jin 2008 | FLD sumoylation; FLC chromatin; flowering |
| [24218331](https://pubmed.ncbi.nlm.nih.gov/24218331/) | Son 2014 | SIZ1 stabilizes FLC protein |
| [28979848](https://pubmed.ncbi.nlm.nih.gov/28979848/) | Kim 2017 | Condition-specific SIZ1 PTM (drought SUMO vs heat/COP1 ubiquitin) |
| [40286281](https://pubmed.ncbi.nlm.nih.gov/40286281/) | Min 2025 | VPS29 stabilizes SIZ1 against ubiquitin-dependent degradation |
| [41986387](https://pubmed.ncbi.nlm.nih.gov/41986387/) | Jia 2026 | SIZ1 in MAC-dependent nuclear condensates potentiates immunity |
| [28197916](https://pubmed.ncbi.nlm.nih.gov/28197916/) | Elrouby 2017 | Authoritative review of SUMO/SIZ1 processes |
| [30092010](https://pubmed.ncbi.nlm.nih.gov/30092010/), [28340002](https://pubmed.ncbi.nlm.nih.gov/28340002/) | OsSIZ1 | Ortholog conservation; multi-stress tolerance |
| [27995772](https://pubmed.ncbi.nlm.nih.gov/27995772/), [35672943](https://pubmed.ncbi.nlm.nih.gov/35672943/) | SlSIZ1 / CaDSIZ1 | Conservation in tomato and pepper (drought) |
| [37786257](https://pubmed.ncbi.nlm.nih.gov/37786257/) | Bao 2023 | SIZ1/NUA-ESD4 balance TPR1 SUMOylation homeostasis |
| [36890719](https://pubmed.ncbi.nlm.nih.gov/36890719/) | HLS1 | SIZ1 sumoylates HLS1; apical hook/light |
| [35718335](https://pubmed.ncbi.nlm.nih.gov/35718335/) | Cd tolerance | SIZ1 activates GSH/PC synthesis |
| [39562527](https://pubmed.ncbi.nlm.nih.gov/39562527/) | AL6 | Seed dormancy / thermoinhibition via DOG1 |
| [39657674](https://pubmed.ncbi.nlm.nih.gov/39657674/) | PROPEP | SUMOylation controls DAMP (Pep) generation |
| [27325215](https://pubmed.ncbi.nlm.nih.gov/27325215/) | ULP1c/d | SUMO proteases act downstream of SIZ1 in water-deficit |

**Consistency of the evidence.** The core enzymatic identity (SUMO E3 ligase, SP-RING family, SUMO1/2 preference, nuclear localization) is supported by multiple independent biochemical and genetic studies spanning 2005–2026 with no contradictory reports. Substrate-specific claims are unusually strong because most rest on **mapped lysine residues** demonstrated by K→R substitution (ICE1-K393, ABI5-K391, MYB30-K283, AL6-K181, and orthologous CaDRHB1-K138), which is the gold standard for sumoylation-site assignment. The apparent paradox of SIZ1 being both a negative regulator of basal SA immunity ([PMID: 17163880](https://pubmed.ncbi.nlm.nih.gov/17163880/)) and a positive potentiator of activated immune condensates ([PMID: 41986387](https://pubmed.ncbi.nlm.nih.gov/41986387/)) is best interpreted as dose- and context-dependence rather than a conflict.

---

## Limitations and Knowledge Gaps

1. **No high-resolution structure of AtSIZ1 or its catalytic complex.** Domain roles are inferred from mutagenesis ([PMID: 19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/)), not from a crystal/cryo-EM structure of SIZ1 bound to SCE1~SUMO and substrate. The precise geometry of SUMO transfer by the plant SP-RING is unresolved.

2. **In vitro vs in vivo substrate validation.** Several substrates were validated with protoplast/in vitro assays. Physiological stoichiometry (what fraction of each substrate is sumoylated at any time) is largely unknown, limiting quantitative interpretation.

3. **Directionality of SUMO cross-talk is substrate-specific and incompletely predictable.** SUMO stabilizes some substrates (ICE1, FLC) but promotes degradation of others (HAT1). The rules governing which outcome occurs are not established.

4. **Positive vs negative immune roles.** The reconciliation of SIZ1's basal immune-suppressive role with its condensate-potentiating role ([PMID: 17163880](https://pubmed.ncbi.nlm.nih.gov/17163880/) vs [PMID: 41986387](https://pubmed.ncbi.nlm.nih.gov/41986387/)) is proposed but not experimentally dissected across a dose/time series.

5. **Pleiotropy vs direct mechanism.** Because `siz1` affects SA, and SA itself influences flowering and other traits, some phenotypes may be indirect. This report prioritized findings anchored to mapped substrates/sites to minimize this confounder.

6. **Specificity determinants.** How SIZ1 selects its substrates (role of the SAP/PHD domains in reading chromatin or specific motifs) is only partially understood.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination** of the SIZ1 SP-RING in complex with SCE1~SUMO1 (cryo-EM or crystallography) to define the catalytic mechanism and the role of the plant-specific PHD finger in substrate presentation.

2. **Quantitative site-specific SUMO proteomics** (SUMO-remnant immunoaffinity + MS) in wild type vs `siz1` under defined stresses (cold, heat, drought, Pi-starvation, pathogen) to measure substrate-level occupancy and build a condition-resolved SIZ1 substrate atlas.

3. **Decode the SUMO/ubiquitin switch**: for paired substrates (ICE1 stabilized vs HAT1 degraded), identify the SUMO-interacting ubiquitin ligases (STUbLs) or readers that convert a SUMO mark into opposite fates.

4. **Dose/time dissection of the immune paradox**: use inducible SIZ1 titration combined with MDNC imaging and SA/PR readouts to map where SIZ1 transitions from immune-suppressive to immune-potentiating.

5. **Test the self-regulation module in planta**: non-ubiquitinatable and non-sumoylatable SIZ1 variants, plus `vps29`/`cop1`/`esd4` genetic combinations, to quantify how SIZ1 PTM state sets global nuclear sumoylation gain under drought vs heat.

6. **Translational validation**: field trials of optimized SIZ1/OsSIZ1 expression (promoter tuning) to confirm multi-stress tolerance without the autoimmunity/developmental penalties associated with constitutive overaccumulation.

---

## Conclusion

*Arabidopsis* SIZ1 (At5g60410, Q680Q4) is definitively identified and characterized as the **principal nuclear SUMO E3 ligase** of the Siz/PIAS family. Its primary biochemical function (EC 2.3.2.-) is to catalyze, via its SP-RING domain, the transfer of SUMO1/SUMO2 from the E2 enzyme SCE1 onto specific lysines of target proteins. It operates predominantly in the nucleus — in nuclear foci and pathogen-induced MAC-dependent condensates — and drives the bulk of stress-induced sumoylation. Functionally, it is a post-translational signaling hub that integrates phosphate, cold, heat, ABA, salicylic-acid immunity, and flowering pathways by SUMO-modifying defined transcription factors and chromatin regulators, with its own activity gated by condition-specific sumoylation/ubiquitination. The function is conserved across plant species.


## Artifacts

- [OpenScientist final report](SIZ1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SIZ1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15894620
2. PMID:19837819
3. PMID:41986387
4. PMID:17644626
5. PMID:38497423
6. PMID:17416732
7. PMID:19704769
8. PMID:17163880
9. PMID:19276109
10. PMID:20514240
11. PMID:22814374
12. PMID:36282496
13. PMID:42260756
14. PMID:34106243
15. PMID:18069938
16. PMID:24218331
17. PMID:28979848
18. PMID:40286281
19. PMID:28197916
20. PMID:30092010
21. PMID:28340002
22. PMID:27995772
23. PMID:35672943