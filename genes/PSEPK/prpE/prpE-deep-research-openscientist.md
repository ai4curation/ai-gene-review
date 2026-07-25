---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T09:05:26.604171'
end_time: '2026-07-23T09:17:06.484855'
duration_seconds: 699.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: prpE
  gene_symbol: prpE
  uniprot_accession: Q88KD9
  protein_description: 'SubName: Full=Propionyl-CoA synthetase {ECO:0000313|EMBL:AAN67964.1};
    EC=6.2.1.17 {ECO:0000313|EMBL:AAN67964.1};'
  gene_info: Name=prpE {ECO:0000313|EMBL:AAN67964.1}; OrderedLocusNames=PP_2351 {ECO:0000313|EMBL:AAN67964.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ATP-dependent AMP-binding enzyme family.
  protein_domains: ACAS_N. (IPR032387); AMP-bd_C. (IPR025110); AMP-bd_C_sf. (IPR045851);
    AMP-binding_CS. (IPR020845); AMP-dep_synth/lig_dom. (IPR000873)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: prpE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: prpE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KD9
- **Protein Description:** SubName: Full=Propionyl-CoA synthetase {ECO:0000313|EMBL:AAN67964.1}; EC=6.2.1.17 {ECO:0000313|EMBL:AAN67964.1};
- **Gene Information:** Name=prpE {ECO:0000313|EMBL:AAN67964.1}; OrderedLocusNames=PP_2351 {ECO:0000313|EMBL:AAN67964.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ATP-dependent AMP-binding enzyme family.
- **Key Domains:** ACAS_N. (IPR032387); AMP-bd_C. (IPR025110); AMP-bd_C_sf. (IPR045851); AMP-binding_CS. (IPR020845); AMP-dep_synth/lig_dom. (IPR000873)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "prpE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'prpE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **prpE** (gene ID: prpE, UniProt: Q88KD9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *prpE* (Propionyl-CoA Synthetase, PP_2351 / Q88KD9) in *Pseudomonas putida* KT2440

## Summary

The gene **prpE** (locus tag **PP_2351**; UniProt **Q88KD9**) of *Pseudomonas putida* KT2440 encodes **propionyl-CoA synthetase** (also called propionate–CoA ligase, **EC 6.2.1.17**). It is a soluble, cytoplasmic enzyme of the **ATP-dependent AMP-binding (adenylate-forming acyl-CoA synthetase, "ANL") superfamily**, defined by the InterPro AMP-binding domains supplied in the target identification (IPR000873, IPR020845, IPR025110, IPR045851) and the N-terminal ACAS_N region (IPR032387). The gene symbol, EC number, protein family, and domain architecture given for Q88KD9 are all internally consistent, and the surrounding literature on orthologous PrpE enzymes (most extensively from *Salmonella enterica*) maps cleanly onto this protein. This report therefore treats Q88KD9 as a *bona fide* propionyl-CoA synthetase and describes its function primarily by inference from close, well-characterized orthologs together with the conserved biochemistry of the enzyme family.

The **primary function** of PrpE is to catalyze the ATP-dependent activation of the short-chain fatty acid **propionate** into its coenzyme A thioester: **propionate + ATP + CoA → propionyl-CoA + AMP + PPi**. Like all members of its family, it performs this in two half-reactions through a tightly bound **propionyl-AMP (acyl-adenylate) intermediate**. Enzymological characterization of the orthologous *Salmonella* PrpE established that **propionate is the strongly preferred substrate** (kcat/Km ≈ 1644 mM⁻¹·s⁻¹; Km ≈ 50 µM), with acetate, butyrate, and 3-hydroxypropionate activated far less efficiently. This substrate preference distinguishes PrpE from its paralog acetyl-CoA synthetase (Acs), which prefers acetate.

Functionally, PrpE catalyzes the **committed first step of propionate catabolism via the 2-methylcitrate cycle (2-MCC)**. It is the "E" gene of the **prpBCDE operon**, whose products — 2-methylisocitrate lyase (PrpB), 2-methylcitrate synthase (PrpC), 2-methylcitrate dehydratase (PrpD), and propionyl-CoA synthetase (PrpE) — together convert propionyl-CoA to pyruvate. This pathway serves a dual role: it **assimilates propionate** as a carbon/energy source and **detoxifies** propionate and its downstream metabolite 2-methylcitrate, which are growth-inhibitory. PrpE activity is further governed **post-translationally** by reversible N-lysine acylation of a conserved active-site lysine (Lys592 in *Salmonella*), which blocks the adenylation half-reaction and is reversed by NAD⁺-dependent sirtuin deacylases (bacterial CobB / Sir2). The enzyme operates in the **cytosol**, where propionate activation and the 2-MCC take place.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was performed:

| Verification item | Result |
|---|---|
| Gene symbol *prpE* matches protein description | **Yes** — *prpE* is the canonical symbol for propionyl-CoA synthetase across bacteria |
| EC 6.2.1.17 consistent with "propionyl-CoA synthetase" | **Yes** — EC 6.2.1.17 is propionate–CoA ligase |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) — confirmed |
| Protein family | ATP-dependent AMP-binding enzyme family — consistent with adenylate-forming acyl-CoA synthetases |
| Domains (IPR000873, IPR020845, IPR025110, IPR045851, IPR032387) | AMP-binding / adenylate-forming domains — consistent with an acyl-CoA synthetase |

No conflicting-identity problem was encountered. The literature retrieved describes propionyl-CoA synthetase enzymes and the propionate/2-methylcitrate pathway, which align with the target. Where direct experimental data on the *P. putida* KT2440 protein itself were unavailable, function is inferred from **close orthologs** (chiefly *Salmonella enterica* PrpE, the most rigorously characterized member) and from the **conserved mechanism of the adenylate-forming enzyme family**. This inferential basis is stated explicitly throughout.

---

## Key Findings

### Finding 1 — PrpE is a propionyl-CoA synthetase (EC 6.2.1.17) that activates propionate through a propionyl-AMP intermediate

*P. putida* PrpE belongs to the ATP-dependent AMP-binding family of adenylate-forming acyl-CoA synthetases, as indicated by its InterPro AMP-binding domain complement (IPR000873/IPR020845) and its EC assignment 6.2.1.17. The defining reaction of the enzyme is the two-step activation of a carboxylic acid to its CoA thioester at the expense of ATP:

```
Step 1 (adenylation):        propionate + ATP  →  propionyl-AMP + PPi
Step 2 (thioesterification):  propionyl-AMP + CoA  →  propionyl-CoA + AMP
Net:  propionate + ATP + CoA  →  propionyl-CoA + AMP + PPi
```

The strongest direct evidence comes from the orthologous *Salmonella enterica* PrpE, which was purified and characterized enzymatically. Kinetic experiments demonstrated that **propionate is the preferred acyl substrate (kcat/Km = 1644 mM⁻¹·s⁻¹)**, and inhibition studies using the intermediate analog adenosine-5′-propylphosphate identified a **Bi Uni Uni Bi Ping Pong mechanism**, consistent with formation and consumption of an enzyme-bound acyl-adenylate intermediate ([PMID: 11841231](https://pubmed.ncbi.nlm.nih.gov/11841231/)).

A second characterization of recombinant *Salmonella* PrpE quantified the substrate specificity directly: with propionate as substrate the enzyme showed a **Km of 50 µM and a specific activity of 120 µmol·min⁻¹·mg⁻¹** at saturation. The enzyme also activated **acetate, 3-hydroxypropionate, and butyrate** to their corresponding CoA esters, but **much less efficiently than propionate** ([PMID: 11097899](https://pubmed.ncbi.nlm.nih.gov/11097899/)). This establishes that PrpE is a genuine short-chain acyl-CoA synthetase with a marked preference for the three-carbon acid propionate — the biochemical rationale for the enzyme being named for, and physiologically dedicated to, propionate.

The generality of the two-step, acyl-AMP mechanism across this enzyme family is well supported by structural and biochemical work on close relatives such as acetyl-CoA synthetase and 4-chlorobenzoate:CoA ligase (see Finding 3 and the Evidence Base). The narrow, short-chain acyl-binding pocket typical of these enzymes underlies the C3 preference, as comparative structural analysis of acyl-CoA synthetases has shown ([PMID: 19544569](https://pubmed.ncbi.nlm.nih.gov/19544569/)).

### Finding 2 — PrpE feeds the 2-methylcitrate cycle, the pathway for propionate assimilation and detoxification

*prpE* is the terminal gene of the **prpBCDE operon**, which in bacteria typically comprises *prpB*, *prpC*, *prpD*, and *prpE*, encoding **2-methylisocitrate lyase, 2-methylcitrate synthase, 2-methylcitrate dehydratase, and propionyl-CoA synthetase**, respectively. Together these enzymes constitute the **2-methylcitrate cycle (2-MCC)**, the principal microbial route for propionate metabolism ([PMID: 42271202](https://pubmed.ncbi.nlm.nih.gov/42271202/)).

PrpE performs the **committed, activating step** of this pathway. The propionyl-CoA that PrpE produces is the direct substrate for PrpC (2-methylcitrate synthase), which condenses propionyl-CoA with oxaloacetate to form 2-methylcitrate. This substrate dependency was made explicit in studies of *Salmonella*, where the *prpE* gene "encoding the propionyl-CoA synthetase enzyme is part of the prpBCDE operon," and where 2-methylcitrate synthesis by PrpC "requires propionyl-CoA as a substrate" ([PMID: 12700259](https://pubmed.ncbi.nlm.nih.gov/12700259/)). Through the successive action of PrpC, PrpD, an aconitase, and PrpB, the 2-MCC ultimately converts propionyl-CoA to **pyruvate**, which enters central carbon metabolism.

The pathway has a **dual physiological logic**. On one hand, it lets the cell use propionate as a carbon and energy source. On the other, **propionate and propionate-derived catabolites are toxic**, so propionate catabolism "can alternatively be viewed as a detoxification mechanism" ([PMID: 29458664](https://pubmed.ncbi.nlm.nih.gov/29458664/)). The toxicity is not diffuse: in *Salmonella*, the specific metabolite **2-methylcitrate** was identified as a potent inhibitor of growth, and blocking the 2-MCC increased propionate sensitivity ([PMID: 11376009](https://pubmed.ncbi.nlm.nih.gov/11376009/)). By initiating the pathway that both consumes propionate and prevents accumulation of these toxic intermediates, PrpE occupies a pivotal control point.

In *Pseudomonas* and other PHA-producing bacteria, PrpE-initiated propionate flux is also biotechnologically relevant because propionyl-CoA is a precursor of odd-chain-length hydroxyalkanoate monomers such as 3-hydroxyvalerate. Disrupting downstream 2-MCC steps (e.g., *prpB*) diverts propionyl-CoA toward odd-chain PHA ([PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/)), and the 2-MCC's detoxifying capacity governs how much propionate a producing strain can tolerate ([PMID: 39729712](https://pubmed.ncbi.nlm.nih.gov/39729712/)). *P. putida* KT2440 grows on propionate and other short-chain carboxylic acids as carbon sources ([PMID: 40988068](https://pubmed.ncbi.nlm.nih.gov/40988068/)). In the related *P. aeruginosa*, the 2-MCC is interlinked with the glyoxylate shunt through enzymatic redundancy, showing the cycle is embedded in central metabolism ([PMID: 40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/)).

### Finding 3 — PrpE activity is regulated post-translationally by reversible N-lysine acylation of an active-site lysine, and the enzyme is a soluble cytoplasmic two-step adenylating enzyme

PrpE is regulated not only at the level of operon transcription (via the PrpR activator using 2-methylcitrate as coactivator; [PMID: 12700259](https://pubmed.ncbi.nlm.nih.gov/12700259/)) but also **post-translationally**. In *Salmonella enterica*, PrpE is **propionylated in vivo at lysine 592, and this modification inactivates the enzyme**. The propionyl-lysine mark is installed by bacterial GCN5-related N-acetyltransferases and removed by bacterial and human Sir2 enzymes (sirtuins) ([PMID: 17684016](https://pubmed.ncbi.nlm.nih.gov/17684016/)).

The mechanistic basis for this switch lies in the catalytic role of the modified lysine. Site-directed mutagenesis of *Salmonella* PrpE showed that both K592A and K592E mutants **failed to convert propionate to propionyl-CoA**, yet both mutants **could still convert propionyl-AMP to propionyl-CoA** — demonstrating that **Lys592 is specifically required for the adenylation (propionyl-AMP-forming) half-reaction but plays no discernible role in thioester bond formation** ([PMID: 11841231](https://pubmed.ncbi.nlm.nih.gov/11841231/)). Acylating this lysine therefore blocks step 1 of the reaction while leaving step 2 intact, effectively switching the enzyme off.

This regulatory logic is directly paralleled by the homologous **acetyl-CoA synthetase (Acs)**, the paradigm for the system. In Acs, acetylation of the active-site lysine (Lys609 in *Salmonella*) "blocks synthesis of the adenylate intermediate but does not affect the thioester-forming activity," and reactivation "requires the NAD⁺-dependent protein deacetylase activity of the CobB Sir2 protein" ([PMID: 12493915](https://pubmed.ncbi.nlm.nih.gov/12493915/)). The acetyltransferase responsible (Pat) modifies Acs-Lys609 using acetyl-CoA ([PMID: 15236963](https://pubmed.ncbi.nlm.nih.gov/15236963/)), and the CobB sirtuin removes it in an NAD⁺-dependent reaction ([PMID: 15019790](https://pubmed.ncbi.nlm.nih.gov/15019790/); [PMID: 29253849](https://pubmed.ncbi.nlm.nih.gov/29253849/)).

The structural explanation for why a single lysine can control one half-reaction but not the other comes from crystallographic studies of this enzyme family. These adenylate-forming enzymes possess a **single active site that alternates between the two half-reactions**: "upon completion of the initial adenylation reaction, the C-terminal domain of these enzymes undergoes a **140° rotation** to perform the second thioester-forming half-reaction" ([PMID: 17497934](https://pubmed.ncbi.nlm.nih.gov/17497934/)). The catalytic lysine sits on this mobile C-terminal domain and is presented to the active site only in the adenylation-competent conformation ([PMID: 12627952](https://pubmed.ncbi.nlm.nih.gov/12627952/)). Acylating that lysine therefore selectively disables the adenylation chemistry.

Regarding **localization**: PrpE possesses no signal peptide or membrane-spanning features and, like its Acs/PrpE family relatives, is a **soluble cytoplasmic protein**. This is consistent with the 2-MCC operating in the cytosol, where propionate is activated and metabolized. (The mammalian short-chain acyl-CoA synthetase ACSS3, a distant relative with propionyl-CoA synthetase activity, is targeted to the mitochondrial matrix in eukaryotes — [PMID: 28003429](https://pubmed.ncbi.nlm.nih.gov/28003429/) — but bacterial PrpE lacks any such targeting and functions in the bacterial cytoplasm.)

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of PrpE as the **gatekeeper of propionate metabolism** in *P. putida* KT2440.

**1. Reaction and mechanism (the "what").** PrpE activates propionate at the cost of one ATP (hydrolyzed to AMP + PPi), producing propionyl-CoA via a bound propionyl-AMP intermediate. It strongly prefers propionate (Km ≈ 50 µM in the *Salmonella* ortholog) over acetate, butyrate, and 3-hydroxypropionate.

**2. Pathway context (the "where in metabolism").** Propionyl-CoA is the entry metabolite of the 2-methylcitrate cycle:

```
   propionate
      │  PrpE (EC 6.2.1.17)  ── ATP + CoA → AMP + PPi
      ▼
  propionyl-CoA
      │  PrpC  (+ oxaloacetate)
      ▼
  2-methylcitrate   ◄── toxic intermediate (growth inhibitor if it accumulates)
      │  PrpD (dehydratase)
      ▼
  2-methyl-cis-aconitate
      │  aconitase
      ▼
  2-methylisocitrate
      │  PrpB (lyase)
      ▼
   pyruvate  +  succinate  → central carbon metabolism
```

**3. Dual role (the "why").** By channeling propionate into the 2-MCC, PrpE simultaneously enables propionate **assimilation** (carbon/energy, and precursor supply for odd-chain PHAs in *Pseudomonas*) and **detoxification** (preventing lethal accumulation of propionate and 2-methylcitrate).

**4. Regulation (the "when").** PrpE is controlled at two levels:

| Level | Mechanism | Effect |
|---|---|---|
| Transcriptional | PrpR activator + 2-methylcitrate coactivator induces prpBCDE | Enzyme made only when propionate flux is present (feed-forward loop) |
| Post-translational | Acylation of active-site Lys (Lys592 in *Salmonella*) by GNAT acyltransferase; removal by NAD⁺-dependent sirtuin (CobB) | Rapid on/off switch gating the adenylation half-reaction |

The post-translational switch is elegant because it ties enzyme activity to cellular energy/redox state (via NAD⁺-dependent deacylation) and to acyl-CoA availability (the acyl donor for the modifying GNAT). The 140° C-terminal domain rotation that lets one active site catalyze both half-reactions is exactly what makes a single lysine a viable regulatory target: the mark disables only the adenylation step.

**Overall interpretation:** PrpE is a soluble cytoplasmic propionate-activating enzyme that opens and gates the only well-described propionate-oxidation route in *Pseudomonas* (the 2-MCC), and its activity is dynamically tuned by reversible lysine acylation. All statements about the *P. putida* KT2440 protein specifically are **inferences from close orthologs plus conserved family mechanism** — a strong but not experimentally direct basis for this particular protein.

---

## Evidence Base

| PMID | Study (abbrev.) | How it supports the findings |
|---|---|---|
| [11841231](https://pubmed.ncbi.nlm.nih.gov/11841231/) | Characterization of *Salmonella* PrpE; Lys592 required for propionyl-AMP synthesis | Direct enzymology of PrpE: propionate preferred (kcat/Km 1644 mM⁻¹s⁻¹); Bi Uni Uni Bi Ping Pong mechanism; Lys592 required for adenylation, not thioesterification |
| [11097899](https://pubmed.ncbi.nlm.nih.gov/11097899/) | Propionyl-CoA synthetase for poly(3HP-co-3HB) | Quantifies PrpE substrate specificity: Km(propionate)=50 µM, specific activity 120 µmol/min/mg; acetate/3HP/butyrate activated much less efficiently |
| [42271202](https://pubmed.ncbi.nlm.nih.gov/42271202/) | Functions of the *prp* operon (*Acetobacter pasteurianus*) | Defines prpBCDE operon composition and PrpE as the propionyl-CoA synthetase feeding the 2-MCC |
| [12700259](https://pubmed.ncbi.nlm.nih.gov/12700259/) | Propionyl-CoA common intermediate; prpBCDE expression (*Salmonella*) | PrpE-generated propionyl-CoA is PrpC's substrate; operon under PrpR/2-methylcitrate control |
| [29458664](https://pubmed.ncbi.nlm.nih.gov/29458664/) | *Loving the poison*: methylcitrate cycle and pathogenesis | Supports the dual assimilation/detoxification role of the 2-MCC |
| [11376009](https://pubmed.ncbi.nlm.nih.gov/11376009/) | 2-methylcitrate as a potent inhibitor of cell growth | Identifies 2-methylcitrate as the specific toxic metabolite the pathway must manage |
| [17684016](https://pubmed.ncbi.nlm.nih.gov/17684016/) | N-lysine propionylation controls PrpE activity | Documents reversible propionylation at Lys592 (inactivating) by GNATs, reversed by Sir2 sirtuins |
| [12493915](https://pubmed.ncbi.nlm.nih.gov/12493915/) | Sir2-dependent activation of Acs by deacetylation | Paradigm: acylation blocks adenylate synthesis, not thioester formation; CobB (NAD⁺-dependent) reactivates |
| [15236963](https://pubmed.ncbi.nlm.nih.gov/15236963/) | Identification of Pat acetyltransferase (*Salmonella*) | Identifies the acetyltransferase modifying Acs-Lys609; establishes the Pat/CobB system |
| [17497934](https://pubmed.ncbi.nlm.nih.gov/17497934/) | Conformational changes in acetyl-CoA synthetase | Establishes the 140° C-terminal domain rotation enabling one active site to catalyze both half-reactions |
| [12627952](https://pubmed.ncbi.nlm.nih.gov/12627952/) | 1.75 Å structure of Acs with adenosine-5′-propylphosphate + CoA | Structural basis for the mobile catalytic lysine and acetylation-based control |
| [19544569](https://pubmed.ncbi.nlm.nih.gov/19544569/) | Acyl-CoA synthetase structure / acyl-binding pocket | Structural rationale for short-chain acyl substrate selectivity in this family |
| [15019790](https://pubmed.ncbi.nlm.nih.gov/15019790/); [29253849](https://pubmed.ncbi.nlm.nih.gov/29253849/) | CobB structure / kinetics | Characterize the NAD⁺-dependent sirtuin deacylase that reverses the modification |
| [28003429](https://pubmed.ncbi.nlm.nih.gov/28003429/) | Rat ACSS3 propionyl-CoA synthetase | Distant eukaryotic relative preferring propionate (Km 0.19 mM); mitochondrial in eukaryotes — contrasts with bacterial cytoplasmic PrpE |
| [37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/); [39729712](https://pubmed.ncbi.nlm.nih.gov/39729712/); [40988068](https://pubmed.ncbi.nlm.nih.gov/40988068/); [40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/) | 2-MCC in *Pseudomonas*/*Halomonas*; PHA production; glyoxylate crosstalk | Physiological/biotech relevance of PrpE-initiated propionate flux and 2-MCC integration into central metabolism |

**Consistency of the evidence:** All primary enzymological data on PrpE derive from the *Salmonella enterica* ortholog, a very close functional homolog (same EC, same operon, same regulation). The mechanistic details (acyl-AMP intermediate, domain rotation, active-site lysine, sirtuin-reversible acylation) are conserved across the broader adenylate-forming family (Acs, 4-chlorobenzoate:CoA ligase, and others), giving high confidence that they apply to *P. putida* PrpE. No retrieved study contradicts the annotation of Q88KD9 as a propionyl-CoA synthetase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical data on the *P. putida* KT2440 protein itself.** Every quantitative parameter cited (Km, kcat/Km, specific activity, Lys592 modification) comes from orthologs, chiefly *Salmonella enterica* PrpE. The *P. putida* enzyme's own kinetic constants and exact substrate profile have not been measured in the retrieved literature.

2. **The regulatory lysine position is inferred.** Lys592 is the *Salmonella* numbering. The corresponding catalytic lysine in Q88KD9 is expected by homology, but its exact residue number, and whether *P. putida* actually propionylates/acetylates it in vivo, were not directly established here.

3. **The *P. putida* Pat/CobB machinery was not verified.** Whether *P. putida* KT2440 possesses the specific GNAT acyltransferase and CobB sirtuin that act on PrpE, and under what conditions they operate, remains an inference from the *Salmonella*/*E. coli* paradigm.

4. **Localization is inferred bioinformatically.** The cytoplasmic assignment rests on the absence of signal/membrane features and analogy to the family, not on experimental fractionation of the *P. putida* protein.

5. **Possible redundancy/promiscuity not resolved.** In *P. aeruginosa*, 2-MCC and glyoxylate-shunt enzymes show enzymatic redundancy ([PMID: 40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/)). Whether other acyl-CoA synthetases in *P. putida* can partially substitute for PrpE (e.g., under acetate-rich conditions) was not tested.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and kinetically characterize recombinant *P. putida* KT2440 PrpE (PP_2351).** Measure Km and kcat for propionate, acetate, butyrate, and 3-hydroxypropionate to confirm that the *Salmonella*-derived substrate preference holds for this ortholog.

2. **Map and mutate the catalytic lysine.** Align Q88KD9 to *Salmonella* PrpE to identify the residue equivalent to Lys592, then generate K→A/R/Q mutants and test for loss of adenylation activity (with retention of thioesterification from propionyl-AMP), replicating the diagnostic result of [PMID: 11841231](https://pubmed.ncbi.nlm.nih.gov/11841231/).

3. **Test post-translational acylation in *P. putida*.** Use mass spectrometry to detect in vivo acylation of PrpE, and test reactivation by an NAD⁺-dependent CobB/Sir2 deacylase, to confirm the regulatory switch operates in *P. putida*.

4. **Construct a ΔprpE mutant and phenotype it.** Assess growth on propionate as sole carbon source, sensitivity to propionate toxicity, and accumulation of 2-methylcitrate; complement with *prpE* to confirm causality.

5. **Assess redundancy.** Combine ΔprpE with deletions of other candidate short-chain acyl-CoA synthetases (and probe the 2-MCC/glyoxylate crosstalk noted for *P. aeruginosa*) to determine whether propionate activation can proceed by alternative routes.

6. **Experimentally verify localization** by cell fractionation or fluorescent tagging to confirm the predicted cytoplasmic distribution, and model the structure (AlphaFold + superposition on Acs) to confirm the mobile C-terminal domain and catalytic-lysine geometry.

---

## Conclusion

*prpE* (PP_2351 / Q88KD9) encodes **propionyl-CoA synthetase (EC 6.2.1.17)**, a soluble cytoplasmic enzyme of the ATP-dependent AMP-binding family that activates **propionate to propionyl-CoA** via a propionyl-AMP intermediate, with strong specificity for propionate over other short-chain acids. It catalyzes the **committed first step of the prpBCDE 2-methylcitrate cycle**, funneling propionate into central metabolism for both **assimilation and detoxification**, and its activity is gated by **reversible N-lysine acylation of its active-site catalytic lysine**, which blocks the adenylation half-reaction and is reversed by NAD⁺-dependent sirtuin (CobB/Sir2) deacylases. These conclusions rest on rigorous enzymology of close orthologs and the conserved mechanism of the enzyme family; direct characterization of the *P. putida* KT2440 protein itself is the principal outstanding gap.


## Artifacts

- [OpenScientist final report](prpE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](prpE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11841231
2. PMID:11097899
3. PMID:19544569
4. PMID:42271202
5. PMID:12700259
6. PMID:29458664
7. PMID:11376009
8. PMID:37995793
9. PMID:39729712
10. PMID:40988068
11. PMID:40015638
12. PMID:17684016
13. PMID:12493915
14. PMID:15236963
15. PMID:15019790
16. PMID:29253849
17. PMID:17497934
18. PMID:12627952
19. PMID:28003429