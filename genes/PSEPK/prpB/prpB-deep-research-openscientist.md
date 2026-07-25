---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T12:56:54.882376'
end_time: '2026-07-23T13:04:03.177305'
duration_seconds: 428.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: prpB
  gene_symbol: prpB
  uniprot_accession: Q88KF6
  protein_description: 'RecName: Full=2-methylisocitrate lyase {ECO:0000256|ARBA:ARBA00073849,
    ECO:0000256|HAMAP-Rule:MF_01939}; Short=2-MIC {ECO:0000256|HAMAP-Rule:MF_01939};
    Short=MICL {ECO:0000256|HAMAP-Rule:MF_01939}; EC=4.1.3.30 {ECO:0000256|ARBA:ARBA00012260,
    ECO:0000256|HAMAP-Rule:MF_01939}; AltName: Full=(2R,3S)-2-methylisocitrate lyase
    {ECO:0000256|HAMAP-Rule:MF_01939};'
  gene_info: Name=prpB {ECO:0000256|HAMAP-Rule:MF_01939}; Synonyms=mmgF {ECO:0000313|EMBL:AAN67947.1};
    OrderedLocusNames=PP_2334 {ECO:0000313|EMBL:AAN67947.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the isocitrate lyase/PEP mutase superfamily.
  protein_domains: ICL/PEPM. (IPR039556); Isocitrate_lyase_ph_CS. (IPR018523); PrpB.
    (IPR012695); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813); Pyrv_kinase-like_dom_sf.
    (IPR040442)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: prpB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: prpB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KF6
- **Protein Description:** RecName: Full=2-methylisocitrate lyase {ECO:0000256|ARBA:ARBA00073849, ECO:0000256|HAMAP-Rule:MF_01939}; Short=2-MIC {ECO:0000256|HAMAP-Rule:MF_01939}; Short=MICL {ECO:0000256|HAMAP-Rule:MF_01939}; EC=4.1.3.30 {ECO:0000256|ARBA:ARBA00012260, ECO:0000256|HAMAP-Rule:MF_01939}; AltName: Full=(2R,3S)-2-methylisocitrate lyase {ECO:0000256|HAMAP-Rule:MF_01939};
- **Gene Information:** Name=prpB {ECO:0000256|HAMAP-Rule:MF_01939}; Synonyms=mmgF {ECO:0000313|EMBL:AAN67947.1}; OrderedLocusNames=PP_2334 {ECO:0000313|EMBL:AAN67947.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the isocitrate lyase/PEP mutase superfamily.
- **Key Domains:** ICL/PEPM. (IPR039556); Isocitrate_lyase_ph_CS. (IPR018523); PrpB. (IPR012695); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813); Pyrv_kinase-like_dom_sf. (IPR040442)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "prpB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'prpB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **prpB** (gene ID: prpB, UniProt: Q88KF6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: prpB (Q88KF6) — 2-Methylisocitrate Lyase from *Pseudomonas putida* KT2440

## Summary

**prpB** (ordered locus **PP_2334**; synonym *mmgF*; UniProt **Q88KF6**) of *Pseudomonas putida* KT2440 encodes **2-methylisocitrate lyase** (MICL, also abbreviated 2-MIC; **EC 4.1.3.30**). This is a **Mg²⁺-dependent carbon–carbon lyase** that catalyzes the **terminal, committed step of the 2-methylcitrate cycle**: the cleavage of **(2R,3S)-2-methylisocitrate into succinate and pyruvate**. The 2-methylcitrate cycle is the principal aerobic route by which bacteria oxidize and detoxify **propionate/propionyl-CoA**, the three-carbon acyl unit generated during catabolism of odd-chain-length fatty acids, branched-chain amino acids, and related substrates. By splitting 2-methylisocitrate, PrpB channels odd-chain carbon into the TCA cycle (via succinate) and central metabolism (via pyruvate).

PrpB is a **cytoplasmic** enzyme, consistent with its role in a soluble intermediary-metabolism pathway alongside the other Prp enzymes (methylcitrate synthase PrpC, methylcitrate dehydratase PrpD, and the aconitase-like AcnD/PrpF activity). Structurally, PrpB belongs to the **isocitrate lyase / phosphoenolpyruvate (PEP) mutase superfamily**, adopting a TIM-barrel (β/α)₈ fold and typically assembling into a **homotetramer** of ~32 kDa subunits. Catalysis proceeds through a mobile **"active-site loop"** that closes over the bound substrate to exclude solvent, and the reaction runs via an **α-carboxy-carbanion intermediate** with inversion of configuration at C3 of 2-methylisocitrate. Two residues — **cysteine 123 and aspartate 58** (Salmonella numbering) — are essential for catalysis, and Mg²⁺ is strictly required to coordinate the pyruvate product/enolpyruvate intermediate. Substrate specificity is strict: the closely related molecule isocitrate binds but acts as a **dead-end inhibitor** rather than a substrate.

The identity of Q88KF6 as prpB/2-methylisocitrate lyase is **well supported and unambiguous**. The gene symbol, protein family, and catalytic domains from UniProt align precisely with an extensive body of biochemical and structural literature on PrpB in *Salmonella enterica*, *Escherichia coli*, and *Pseudomonas* species. While the deepest mechanistic characterization comes from enterobacterial orthologs, the *Pseudomonas*-specific literature directly confirms both the identity and the physiological importance of PrpB for propionate oxidation, including downstream consequences for polyhydroxyalkanoate (PHA) biopolymer composition.

---

## Key Findings

### Finding 1 — PrpB is a Mg²⁺-dependent 2-methylisocitrate lyase catalyzing the terminal step of the 2-methylcitrate cycle

PrpB (EC 4.1.3.30) catalyzes the **retro-aldol cleavage of (2R,3S)-2-methylisocitrate into succinate + pyruvate**, which is the **last step of the 2-methylcitrate cycle** for propionate oxidation. This reaction is directly analogous to the isocitrate-lyase reaction of the glyoxylate shunt (which cleaves isocitrate into succinate + glyoxylate), but with strict selectivity for the methyl-branched substrate.

The most precise kinetic characterization comes from the *Salmonella enterica* ortholog, whose properties are expected to closely mirror those of the *P. putida* enzyme given their shared family and reaction. In *S. enterica*, PrpB acts on 2-methylisocitrate with a **Kₘ of 19 µM and a kcat of 105 s⁻¹**, indicating a high-affinity, catalytically efficient enzyme [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/). The enzyme has a **strict Mg²⁺ requirement** (Mn²⁺ substitutes poorly, giving only ~28% of activity), a pH optimum near 7.5, a temperature optimum around 50 °C, and assembles as a **homotetramer with ~32 kDa subunits**. Crystal structures of the *E. coli* and *S. typhimurium* enzymes confirm the reaction chemistry and reveal how the pyruvate product is coordinated by the essential divalent metal ion [PMID: 12706720](https://pubmed.ncbi.nlm.nih.gov/12706720/); [PMID: 14575713](https://pubmed.ncbi.nlm.nih.gov/14575713/).

> "The K(m) of PrpB for 2-MIC was measured at 19 micro M, with a k(cat) of 105 s(-1)." — [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/)

> "the cleavage of 2-methylisocitrate to succinate and pyruvate, is catalysed by 2-methylisocitrate lyase (PrpB)" — [PMID: 14575713](https://pubmed.ncbi.nlm.nih.gov/14575713/)

The reaction PrpB catalyzes can be written as:

```
(2R,3S)-2-methylisocitrate  --(PrpB, Mg2+)-->  succinate + pyruvate
```

This positions PrpB as the **carbon-releasing exit valve** of the methylcitrate cycle: the two products feed directly into central carbon metabolism, with succinate entering the TCA cycle and pyruvate available for oxidation, gluconeogenesis, or biosynthesis.

### Finding 2 — PrpB belongs to the ICL/PEP-mutase superfamily and uses active-site-loop closure with an α-carboxy-carbanion mechanism; C123 and D58 are catalytically essential

PrpB adopts the **isocitrate lyase / PEP mutase (ICL/PEPM) fold**, a variant of the TIM-barrel architecture shared across a superfamily that includes isocitrate lyase, phosphoenolpyruvate mutase, and carboxyphosphonoenolpyruvate mutase. A defining mechanistic feature of this superfamily — directly observed for PrpB — is the movement of a **mobile "active-site loop"** from an open to a closed conformation upon substrate binding, sequestering the reactants from bulk solvent during catalysis [PMID: 12706720](https://pubmed.ncbi.nlm.nih.gov/12706720/); [PMID: 15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/).

The detailed catalytic mechanism was resolved through structures of an active-site **C123S variant** captured in complex with product and with the inhibitor isocitrate. These structures support a mechanism proceeding through an **α-carboxy-carbanion intermediate / transition state**, consistent with prior stereochemical experiments demonstrating **inversion of configuration at C3** of 2-methylisocitrate. Crucially, isocitrate — which lacks the C2 methyl group but is otherwise similar — binds in the active site as a **dead-end inhibitor**, explaining the enzyme's strict substrate and stereochemical selectivity [PMID: 15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/). Site-directed mutagenesis independently identified **Cys123 and Asp58** as residues essential for catalysis [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/).

> "We propose a catalytic mechanism involving an alpha-carboxy-carbanion intermediate/transition state, which is consistent with previous stereochemical experiments showing inversion of configuration at the C(3) of 2-methylisocitrate." — [PMID: 15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/)

> "A common feature of members of this enzyme family is the movement of a so-called 'active site loop' from an open into a closed conformation upon substrate binding thus shielding the reactants from the surrounding solvent." — [PMID: 12706720](https://pubmed.ncbi.nlm.nih.gov/12706720/)

Together these studies establish PrpB as a mechanistically well-understood lyase whose fold, metal dependence, and residue-level chemistry are conserved features of the ICL/PEPM superfamily. The strict discrimination between 2-methylisocitrate (substrate) and isocitrate (inhibitor) is the structural basis for keeping the methylcitrate cycle biochemically distinct from the glyoxylate shunt, despite their chemical parallels.

### Finding 3 — In *Pseudomonas*, PrpB is required for propionate oxidation via the only known propionate pathway, with consequences for PHA composition

The physiological importance of PrpB in *Pseudomonas* is directly documented. In *Pseudomonas* sp. LFM693, a **prpB (2-methylisocitrate lyase) disruption mutant** blocks the 2-methylcitrate cycle — explicitly described as **the only known and characterized pathway for propionate oxidation in this organism**. With the cycle interrupted, propionyl-CoA is no longer fully oxidized and is instead redirected into **odd-chain-length polyhydroxyalkanoate (PHA) monomers** and accumulating 2-methylisocitrate, providing a whole-cell readout of PrpB's metabolic role [PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/); [PMID: 39492536](https://pubmed.ncbi.nlm.nih.gov/39492536/).

> "Pseudomonas sp. LFM693 is a 2-methylisocitrate lyase (prpB) disrupted mutant. This enzyme catalyzes a step in the 2-methylcitrate cycle, the only known and described pathway for propionate oxidation in this organism." — [PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/)

In the closely related *P. aeruginosa*, the 2-methylcitrate and glyoxylate cycles are further shown to be **linked through enzymatic redundancy**: the glyoxylate-cycle isocitrate lyase **AceA exhibits secondary 2-methylisocitrate lyase activity**, demonstrated through structural analysis, kinetics, metabolomics, and PrpB mutation. This means that in some *Pseudomonas* backgrounds a portion of MICL activity can be supplied by the bifunctional ICL enzyme, echoing the situation in *Mycobacterium tuberculosis*, where ICL isoforms substitute for a missing dedicated MICL [PMID: 40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/); [PMID: 18048912](https://pubmed.ncbi.nlm.nih.gov/18048912/).

> "isocitrate lyase (AceA) exhibiting secondary 2-methylisocitrate lyase activity" — [PMID: 40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/)

These functional-genetics results confirm the biochemical annotation at the physiological level: PrpB is the dedicated MICL that enables *Pseudomonas* to grow on and detoxify propionate, and its loss has measurable, characteristic metabolic consequences.

---

## Mechanistic Model / Interpretation

### The 2-methylcitrate cycle and PrpB's place in it

Propionate (or propionyl-CoA generated internally) is oxidized aerobically through the **2-methylcitrate cycle**, a pathway analogous to the citric-acid and glyoxylate cycles but adapted for the three-carbon propionyl unit. PrpB catalyzes the final, carbon-releasing step:

```
   propionate
       │  (PrpE / acyl-CoA synthetase)
       ▼
   propionyl-CoA  + oxaloacetate
       │  PrpC  (2-methylcitrate synthase)
       ▼
   (2S,3S)-2-methylcitrate
       │  PrpD / AcnD  (2-methylcitrate dehydratase)
       ▼
   2-methyl-cis-aconitate
       │  PrpF / AcnB  (aconitase-type hydratase/isomerase)
       ▼
   (2R,3S)-2-methylisocitrate
       │  ★ PrpB  (2-METHYLISOCITRATE LYASE)  ── requires Mg2+
       ▼
   SUCCINATE  +  PYRUVATE
       │                 │
       ▼                 ▼
   TCA cycle       central metabolism
   (regenerates    (oxidation, gluconeogenesis,
    oxaloacetate)    biosynthesis)
```

The succinate product re-enters the TCA cycle and ultimately regenerates the oxaloacetate consumed by PrpC, making the pathway catalytically self-sustaining; the net effect is the complete oxidation of propionate while the pyruvate output supplies carbon to the rest of the cell. PrpB is therefore both the **exit point** of the cycle and a **detoxification valve**: without it, propionyl-CoA and pathway intermediates accumulate and can be toxic, as seen in mycobacterial models where blocking MICL activity is deleterious [PMID: 18048912](https://pubmed.ncbi.nlm.nih.gov/18048912/).

### Structural/mechanistic model

| Property | Value / description | Evidence |
|---|---|---|
| EC number | 4.1.3.30 | UniProt / [PMID: 14575713](https://pubmed.ncbi.nlm.nih.gov/14575713/) |
| Reaction | (2R,3S)-2-methylisocitrate → succinate + pyruvate | [PMID: 14575713](https://pubmed.ncbi.nlm.nih.gov/14575713/) |
| Metal cofactor | Mg²⁺ required (Mn²⁺ ~28% activity) | [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) |
| Kₘ (2-MIC) | 19 µM (*S. enterica*) | [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) |
| kcat | 105 s⁻¹ (*S. enterica*) | [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) |
| pH / T optimum | ~7.5 / ~50 °C | [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) |
| Quaternary structure | Homotetramer, ~32 kDa/subunit | [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) |
| Fold / superfamily | ICL/PEPM TIM-barrel; isocitrate lyase/PEP mutase superfamily | [PMID: 12706720](https://pubmed.ncbi.nlm.nih.gov/12706720/) |
| Catalytic mechanism | α-carboxy-carbanion intermediate; inversion at C3 | [PMID: 15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/) |
| Essential residues | Cys123, Asp58 (Salmonella numbering) | [PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) |
| Substrate specificity | Strict for 2-methylisocitrate; isocitrate is a dead-end inhibitor | [PMID: 15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/) |
| Subcellular localization | Cytoplasm | Inferred from soluble intermediary-metabolism pathway; consistent with family |

Catalysis is a coordinated cycle: the substrate binds in the TIM-barrel active site, the **mobile loop closes** to exclude water, Mg²⁺ stabilizes the developing negative charge, the **C–C bond is cleaved** through an α-carboxy-carbanion (enolpyruvate-like) transition state with inversion at C3, and the loop reopens to release succinate and pyruvate. The methyl branch of the substrate is essential for productive binding — its absence (i.e., isocitrate) converts the ligand into a non-cleavable inhibitor, which is how the cell keeps the methylcitrate and glyoxylate cycles chemically insulated even though both use ICL-family folds.

### Localization

PrpB carries out its function in the **cytoplasm**. The 2-methylcitrate cycle is a soluble intermediary-metabolism pathway; its enzymes (PrpC, PrpD, AcnD/PrpF, PrpB) act on small polar organic acids and CoA thioesters within the cytosol, and PrpB has no signal peptide or membrane-anchoring features characteristic of secreted or membrane proteins. Its products (succinate, pyruvate) are cytosolic metabolites feeding the central carbon network.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism | Contribution |
|---|---|---|---|
| [12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/) | Residues C123 and D58 of PrpB essential for catalysis | *S. enterica* | Kinetics (Kₘ, kcat), Mg²⁺ dependence, quaternary structure, essential residues |
| [12706720](https://pubmed.ncbi.nlm.nih.gov/12706720/) | Crystal structure of *E. coli* PrpB | *E. coli* | Fold, ICL/PEPM superfamily membership, active-site-loop closure |
| [14575713](https://pubmed.ncbi.nlm.nih.gov/14575713/) | Crystal structure of *S. typhimurium* PrpB + pyruvate/Mg²⁺ | *S. typhimurium* | Reaction definition; Mg²⁺-pyruvate coordination |
| [15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/) | PrpB with product and isocitrate inhibitor | *E. coli/Salmonella* | α-carboxy-carbanion mechanism; C3 inversion; substrate specificity |
| [37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/) | Fed-batch cultivation; PHA composition | *Pseudomonas* sp. LFM693 | prpB mutant; MICL as only propionate-oxidation route |
| [39492536](https://pubmed.ncbi.nlm.nih.gov/39492536/) | Propionate oxidation & odd-chain PHA | *Pseudomonas* sp. LFM046 | Physiological role; propionyl-CoA rerouting on MICL loss |
| [40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/) | Methylcitrate/glyoxylate cycles linked by redundancy | *P. aeruginosa* | AceA (ICL) has secondary MICL activity; PrpB mutation |
| [18048912](https://pubmed.ncbi.nlm.nih.gov/18048912/) | Methylcitrate cycle in propionate detoxification | *M. smegmatis* | prpB clustering with prpC/prpD; detoxification role; ICL redundancy |
| [30745367](https://pubmed.ncbi.nlm.nih.gov/30745367/) | Nitrogen regulator GlnR controls transcription | (regulatory) | Context for prp operon transcriptional control |

**How the evidence fits together.** The four enterobacterial structural/biochemical papers ([PMID: 12897003](https://pubmed.ncbi.nlm.nih.gov/12897003/), [12706720](https://pubmed.ncbi.nlm.nih.gov/12706720/), [14575713](https://pubmed.ncbi.nlm.nih.gov/14575713/), [15723538](https://pubmed.ncbi.nlm.nih.gov/15723538/)) provide the gold-standard molecular characterization of PrpB — the reaction, kinetics, metal dependence, fold, mechanism, essential residues, and substrate specificity. Because *P. putida* PrpB shares the same gene symbol, EC number, family, and diagnostic domains (ICL/PEPM, PrpB IPR012695), these mechanistic conclusions transfer with high confidence. The *Pseudomonas*-specific papers ([PMID: 37995793](https://pubmed.ncbi.nlm.nih.gov/37995793/), [39492536](https://pubmed.ncbi.nlm.nih.gov/39492536/), [40015638](https://pubmed.ncbi.nlm.nih.gov/40015638/)) confirm the physiological role in this genus and reveal the AceA/PrpB redundancy that connects the methylcitrate and glyoxylate cycles. The mycobacterial paper ([PMID: 18048912](https://pubmed.ncbi.nlm.nih.gov/18048912/)) reinforces the detoxification theme and the recurring evolutionary theme of ICL/MICL functional overlap. No cited evidence contradicts the annotation; all sources converge on the same identity and function.

---

## Limitations and Knowledge Gaps

1. **No *P. putida* KT2440–specific enzymology.** The most rigorous kinetic and structural data (Kₘ, kcat, Mg²⁺ dependence, C123/D58, mechanism) come from *S. enterica* and *E. coli* orthologs, not from Q88KF6 itself. Transfer of these parameters relies on strong sequence/family homology rather than direct measurement on the *P. putida* protein. Absolute kinetic constants may differ modestly.

2. **Localization is inferred, not directly demonstrated.** Cytoplasmic localization is deduced from pathway biochemistry and the absence of targeting signals; no experimental localization study for the *P. putida* enzyme is cited.

3. **Residue numbering is from Salmonella.** The essential Cys123/Asp58 map onto conserved positions, but exact residue numbers in the *P. putida* sequence require alignment to confirm.

4. **Redundancy in *P. putida* is not directly established.** The AceA secondary-MICL-activity result is from *P. aeruginosa*. Whether *P. putida* KT2440's isocitrate lyase similarly backs up PrpB has not been directly demonstrated, so the strict "only known pathway" statement (from *Pseudomonas* sp. LFM693) may be organism/strain-dependent.

5. **Regulation is only lightly covered.** The transcriptional/regulatory control of the *prp* operon in *P. putida* (e.g., PrpR activation, 2-methylcitrate as inducer) was not deeply investigated here; the GlnR paper ([PMID: 30745367](https://pubmed.ncbi.nlm.nih.gov/30745367/)) provides only partial context.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical validation of Q88KF6.** Recombinantly express and purify *P. putida* KT2440 PrpB and measure Kₘ, kcat, and metal dependence on authentic (2R,3S)-2-methylisocitrate to confirm parameters transferred from *Salmonella*.

2. **Confirm essential residues by alignment + mutagenesis.** Align Q88KF6 to *S. enterica* PrpB, identify the residues corresponding to Cys123/Asp58, and verify catalytic essentiality by site-directed mutagenesis.

3. **Test genetic redundancy in KT2440.** Construct ΔprpB, ΔaceA (icl), and double mutants and assay growth on propionate (and propionate + glucose) to determine whether *P. putida* isocitrate lyase provides backup MICL activity as in *P. aeruginosa*.

4. **Metabolite and localization studies.** Use metabolomics to confirm 2-methylisocitrate accumulation in a KT2440 ΔprpB mutant, and perform fractionation or fluorescent-tagging to confirm cytoplasmic localization.

5. **Structural confirmation.** Solve or model (AlphaFold) the *P. putida* PrpB structure, verify the ICL/PEPM TIM-barrel fold and the mobile active-site loop, and dock 2-methylisocitrate to confirm the α-carboxy-carbanion mechanistic geometry.

6. **Regulatory mapping.** Characterize the *prpBCDF* operon promoter and its regulator(s) in KT2440 to define how propionate exposure induces PrpB expression.

---

*Report compiled from an autonomous, literature-grounded investigation. All quantitative claims are drawn from the cited primary literature; where data derive from orthologous enzymes (chiefly *S. enterica* and *E. coli*), this is stated explicitly.*


## Artifacts

- [OpenScientist final report](prpB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](prpB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12897003
2. PMID:12706720
3. PMID:14575713
4. PMID:15723538
5. PMID:37995793
6. PMID:39492536
7. PMID:40015638
8. PMID:18048912
9. PMID:30745367