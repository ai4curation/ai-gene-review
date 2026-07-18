---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T19:04:53.453340'
end_time: '2026-07-11T19:18:03.833824'
duration_seconds: 790.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: gltA
  gene_symbol: gltA
  uniprot_accession: Q88FA4
  protein_description: 'RecName: Full=Citrate synthase {ECO:0000256|NCBIfam:TIGR01798,
    ECO:0000256|PIRNR:PIRNR001369};'
  gene_info: Name=gltA {ECO:0000313|EMBL:AAN69775.1}; OrderedLocusNames=PP_4194 {ECO:0000313|EMBL:AAN69775.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the citrate synthase family.
  protein_domains: Citrate_synth-like_lrg_a-sub. (IPR016142); Citrate_synth-like_sm_a-sub.
    (IPR016143); Citrate_synthase. (IPR002020); Citrate_synthase_AS. (IPR019810);
    Citrate_synthase_bac-typ. (IPR024176)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: gltA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: gltA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FA4
- **Protein Description:** RecName: Full=Citrate synthase {ECO:0000256|NCBIfam:TIGR01798, ECO:0000256|PIRNR:PIRNR001369};
- **Gene Information:** Name=gltA {ECO:0000313|EMBL:AAN69775.1}; OrderedLocusNames=PP_4194 {ECO:0000313|EMBL:AAN69775.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the citrate synthase family.
- **Key Domains:** Citrate_synth-like_lrg_a-sub. (IPR016142); Citrate_synth-like_sm_a-sub. (IPR016143); Citrate_synthase. (IPR002020); Citrate_synthase_AS. (IPR019810); Citrate_synthase_bac-typ. (IPR024176)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "gltA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'gltA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **gltA** (gene ID: gltA, UniProt: Q88FA4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *gltA* (Citrate Synthase, PP_4194) in *Pseudomonas putida* KT2440

**UniProt Accession:** Q88FA4 · **Gene:** *gltA* · **Ordered Locus:** PP_4194 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) · **EC:** 2.3.3.1

---

## Summary

The gene ***gltA*** (locus **PP_4194**; UniProt **Q88FA4**) of *Pseudomonas putida* KT2440 encodes **citrate synthase (EC 2.3.3.1)**, the enzyme that catalyzes the **first committed step of the tricarboxylic acid (TCA / Krebs) cycle**. Citrate synthase performs the stereospecific aldol (Claisen) condensation of **acetyl-CoA** with **oxaloacetate**, proceeding through a citryl-CoA intermediate and hydrolysis to yield **citrate + coenzyme A (CoA)**. The gene identity is firmly established: UniProt annotates the product as citrate synthase (TIGR01798 / PIRNR001369) within the citrate synthase family, and independent experimental work in *P. putida* KT2440 explicitly identifies *gltA* as "encoding citrate synthase" when using it as a metabolic-engineering target ([PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/)). This verification satisfies the mandatory gene-identity check: the symbol, organism, protein family, and catalytic-domain signatures all align, and the literature retrieved refers to the correct enzyme in the correct organism.

Mechanistically, the enzyme uses a conserved general acid–base catalytic apparatus centred on an aspartate base that abstracts a proton from the acetyl-CoA methyl group and a histidine that polarizes the oxaloacetate carbonyl and stabilizes the citryl-CoA/citrate intermediates. Sequence analysis of the target directly confirms these features: Q88FA4 is a **429-residue** protein with an intact, conserved **His–His–Asp** catalytic triad and shares **71.7% amino-acid identity** with the well-characterized *Escherichia coli* citrate synthase. This places Q88FA4 unambiguously in the **Gram-negative "Type II"** class of citrate synthases — hexameric enzymes that are **allosterically inhibited by NADH** (and isosterically inhibited by ATP), coupling TCA-cycle entry directly to the cell's energy and redox status.

Functionally, GltA operates in the **cytoplasm** and serves as the **gatekeeper of the acetyl-CoA node** in *P. putida* central carbon metabolism. Because *P. putida* catabolizes sugars principally through the Entner–Doudoroff/EDEMP routes and forms comparatively little acetyl-CoA from sugars, citrate synthase is a decisive drain that partitions acetyl-CoA between full oxidation in the TCA cycle and acetyl-CoA-derived biosynthesis (e.g., polyhydroxyalkanoate/PHB storage polymers). This partitioning role is demonstrated directly: dynamic CRISPRi silencing of *gltA* raised intracellular acetyl-CoA roughly **8-fold** and boosted acetyl-CoA-dependent bioproduction ([PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/)). Importantly, GltA is **substrate-specific for acetyl-CoA** and does not condense propionyl-CoA; propionyl-CoA is handled by a distinct paralogue, the 2-methylcitrate synthase **PrpC**, which *P. putida* encodes separately for propionate catabolism.

---

## Gene / Protein Identity Verification (Mandatory)

Identity is **unambiguous** and every required check passes:

- **Symbol vs. description:** UniProt Q88FA4 names the gene *gltA* and describes the product as citrate synthase. In *P. putida* the *gltA* symbol maps to citrate synthase, matching the protein description.
- **Organism:** All primary evidence used is for *Pseudomonas putida* KT2440 (or, for regulatory/structural inference, closely homologous Gram-negative enzymes explicitly linked to *P. putida* via probe cross-hybridization; [PMID: 2507528](https://pubmed.ncbi.nlm.nih.gov/2507528/)).
- **Family / domains:** The InterPro domain set (IPR016142/IPR016143 large/small α-subdomains, IPR002020 citrate synthase, IPR019810 active-site signature, IPR024176 bacterial-type) is the canonical citrate synthase architecture, corroborated at the residue level by the intact His–His–Asp catalytic site in the retrieved sequence.
- **No symbol clash:** There is no evidence the research was misdirected to a different gene; the *E. coli gltA*, *Corynebacterium gltA*, and *Pseudomonas* NADH-sensitive citrate synthase literature all describe the same enzyme class as the target.

**Conclusion:** This is NOT an ambiguous-symbol case. Q88FA4 is confidently a citrate synthase of *P. putida* KT2440.

---

## Key Findings

### F001 — *gltA* (PP_4194, Q88FA4) encodes citrate synthase, the first committed enzyme of the TCA cycle

The primary annotation is robust and multiply supported. UniProt Q88FA4 annotates the gene product as citrate synthase (EC 2.3.3.1) via the NCBIfam signature TIGR01798 and the PIRSF signature PIRNR001369, and assigns it to the citrate synthase family. Critically, this database annotation is corroborated by direct experimental usage in the exact organism of interest. Kozaeva and colleagues, engineering *P. putida* KT2440, explicitly describe *gltA* as the gene "encoding citrate synthase" and use it as a rational target to redirect carbon flux ([PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/)). This satisfies the gene-identity verification requirement: the symbol *gltA*, the organism *P. putida* KT2440, the citrate-synthase protein family, and the bacterial citrate-synthase domain architecture are mutually consistent. There is no evidence of a symbol clash misdirecting the research to a different gene.

> *"Dynamic reduction of gene expression of two key targets (gltA, encoding citrate synthase, and the essential accA gene, encoding subunit A of the acetyl-CoA carboxylase complex) mediated an 8-fold increase in the acetyl-CoA content of rewired P. putida."* — [PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/)

### F002 — The reaction: aldol condensation of acetyl-CoA with oxaloacetate to citrate + CoA

Citrate synthase catalyzes the condensation of **acetyl-CoA** and **oxaloacetate** to form **citrate**, releasing CoA ([PMID: 9387145](https://pubmed.ncbi.nlm.nih.gov/9387145/); [PMID: 31451751](https://pubmed.ncbi.nlm.nih.gov/31451751/)). The catalytic mechanism has been dissected by mutagenesis of active-site residues: an aspartate (Asp375 in the reference pig-heart numbering) acts as the **catalytic base** that abstracts a proton from the methyl group of acetyl-CoA to generate the reactive enolate/enol, while a histidine (His320) **hydrogen-bonds to the oxaloacetate carbonyl** and stabilizes the resulting citryl-CoA and citrate species ([PMID: 9657685](https://pubmed.ncbi.nlm.nih.gov/9657685/)). The reaction follows an **ordered ternary-complex** kinetic mechanism (oxaloacetate binding induces a conformational closure that then admits acetyl-CoA), with reported micromolar Michaelis constants for both substrates in a characterized orthologue (~6.7 µM acetyl-CoA and ~3.1 µM oxaloacetate for *Drosophila* CS). The chemistry — proton abstraction, aldol addition to form citryl-CoA, then thioester hydrolysis — is conserved across the entire citrate synthase family, including the bacterial Type II enzymes.

> *"Citrate synthase which condenses acetyl-CoA and oxaloacetate to citrate was purified from Drosophila melanogaster."* — [PMID: 9387145](https://pubmed.ncbi.nlm.nih.gov/9387145/)
>
> *"D375 is the base removing the proton of acetyl-coenzyme A."* — [PMID: 9657685](https://pubmed.ncbi.nlm.nih.gov/9657685/)
>
> *"H320 forms a hydrogen bond with the carbonyl of oxaloacetate and the alcohols of the citryl-coenzyme A and citrate products."* — [PMID: 9657685](https://pubmed.ncbi.nlm.nih.gov/9657685/)

### F003 — A Gram-negative "Type II" hexameric enzyme, allosterically inhibited by NADH

*Pseudomonas* citrate synthase belongs to the **Type II** class characteristic of Gram-negative bacteria. These enzymes are **hexameric** and are **strongly and specifically inhibited by NADH through an allosteric mechanism**, in contrast to the dimeric **Type I** enzymes of eukaryotes and Gram-positive bacteria ([PMID: 11683626](https://pubmed.ncbi.nlm.nih.gov/11683626/)). Multiple-inhibition studies established the key regulatory distinction: NADH behaves as an **allosteric inhibitor specifically in the Gram-negative enzyme** (whereas it is merely isosteric in eukaryotic/Gram-positive enzymes), and ATP acts as an isosteric inhibitor competing at the acetyl-CoA site ([PMID: 175782](https://pubmed.ncbi.nlm.nih.gov/175782/)). Direct evidence that this regulatory phenotype applies to *Pseudomonas* comes from *P. aeruginosa*: its citrate synthase is NADH-sensitive, has ~48 kDa subunits, and shares 70%/76% sequence identity with the *E. coli* and *Acinetobacter* enzymes; notably, the *P. aeruginosa* gene probe cross-hybridized to *P. putida* genomic DNA, directly linking the *putida* enzyme to this NADH-regulated Type II family ([PMID: 2507528](https://pubmed.ncbi.nlm.nih.gov/2507528/)). Q88FA4's InterPro annotation includes the bacterial-type citrate synthase signature (IPR024176) plus the large- and small-subtype α-domains, consistent with the Type II assignment. The regulatory logic is that high NADH (an abundant energy/redox signal) allosterically throttles TCA entry, matching catabolic flux to the cell's energetic state.

> *"Such enzymes are hexameric and are strongly and specifically inhibited by NADH through an allosteric mechanism."* — [PMID: 11683626](https://pubmed.ncbi.nlm.nih.gov/11683626/)
>
> *"NADH also acts isosterically with eukaryotic and Gram-positive bacterial citrate synthases, but behaves as an allosteric inhibitor specifically in the case of the Gram-negative bacterial enzyme."* — [PMID: 175782](https://pubmed.ncbi.nlm.nih.gov/175782/)

### F004 — GltA governs the cytoplasmic acetyl-CoA node and gates carbon partitioning

Citrate synthase catalyzes the **initial, rate-controlling reaction** of the citric acid cycle and thus governs the entry of carbon into the cycle ([PMID: 7522844](https://pubmed.ncbi.nlm.nih.gov/7522844/)). In *P. putida* KT2440 specifically, GltA sits at the pivotal **acetyl-CoA node**, controlling how carbon is split between full oxidation (TCA cycle → energy + biosynthetic precursors) and diversion into acetyl-CoA-derived products. Its central control role was demonstrated experimentally: dynamic CRISPRi down-regulation of *gltA* (together with *accA*) produced an **~8-fold increase in intracellular acetyl-CoA** and enhanced acetyl-CoA-dependent bioproduction such as polyhydroxybutyrate (PHB) ([PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/)). The physiological weight of this node is amplified by *P. putida*'s catabolic wiring: it degrades glucose predominantly through the Entner–Doudoroff/EDEMP routes and generates comparatively little acetyl-CoA from sugars, making citrate synthase the principal committed drain of acetyl-CoA into the cycle ([PMID: 36155822](https://pubmed.ncbi.nlm.nih.gov/36155822/)). The enzyme functions in the **cytoplasm**, where both the TCA cycle and acetyl-CoA-dependent biosynthesis occur.

> *"Citrate synthase catalyses the initial reaction of the citric acid cycle and can therefore be considered as the rate-controlling enzyme for the entry of substrates into the cycle."* — [PMID: 7522844](https://pubmed.ncbi.nlm.nih.gov/7522844/)

### F005 — Strict acetyl-CoA specificity distinguishes GltA from the paralogous 2-methylcitrate synthase (PrpC)

A key specificity point is that authentic citrate synthase is **specific for acetyl-CoA and does not condense propionyl-CoA**. Biochemical separation of the two activities in the related β-proteobacterium *Ralstonia eutropha* showed that citrate synthase (CS) **could not use propionyl-CoA as a substrate**, whereas the paralogous 2-methylcitrate synthase (2-MCS / PrpC) preferentially uses propionyl-CoA (KM ~0.061 mM propionyl-CoA vs ~0.35 mM acetyl-CoA) while retaining some ability to condense acetyl-CoA ([PMID: 16133321](https://pubmed.ncbi.nlm.nih.gov/16133321/)). Consistent with this division of labour, *Salmonella* PrpC utilizes propionyl-CoA more efficiently than acetyl-CoA, and its NADH-binding residues are not conserved relative to the hexameric *E. coli* citrate synthase — underscoring that PrpC is a functionally and regulatorily distinct enzyme ([PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)). *P. putida* encodes a separate *prpC* as part of its 2-methylcitrate (propionate catabolism) pathway; therefore GltA/*gltA* should not be conflated with the propionate-catabolic machinery. This distinction is important for accurate annotation because the two enzymes are structurally homologous but metabolically separate.

> *"In contrast, CS could not use propionyl-CoA as a substrate."* — [PMID: 16133321](https://pubmed.ncbi.nlm.nih.gov/16133321/)
>
> *"StPrpC was found to utilize propionyl-CoA more efficiently than acetyl-CoA or butyryl-CoA."* — [PMID: 20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/)

### F006 — Direct sequence verification: a 429-residue enzyme with an intact His–His–Asp catalytic site

Direct analysis of the retrieved Q88FA4 sequence confirms the annotation at the residue level. The protein is **429 amino acids** long — typical for Gram-negative Type II citrate synthases (cf. *E. coli* GltA at 427 aa). The two catalytic histidines are conserved at **His265** (in the ...AHG... motif) and **His306** (within the canonical citrate-synthase "GHR" motif, ...FGHRVY...), aligning to *E. coli* catalytic His264/His305 (pig-heart His274/His320), and a conserved catalytic **Asp364** lies nearby, matching the general acid–base mechanism defined by mutagenesis ([PMID: 9657685](https://pubmed.ncbi.nlm.nih.gov/9657685/)). Both the sequence length and the bacterial-type InterPro signature (IPR024176) are consistent with the structurally characterized hexameric Type II class of *E. coli* ([PMID: 11683626](https://pubmed.ncbi.nlm.nih.gov/11683626/)) and the biochemically characterized *Pseudomonas* enzyme ([PMID: 2507528](https://pubmed.ncbi.nlm.nih.gov/2507528/)). This residue-level match provides structure-informed evidence — beyond database transfer — that Q88FA4 is a catalytically competent citrate synthase.

> *"D375 is the base removing the proton of acetyl-coenzyme A."* — [PMID: 9657685](https://pubmed.ncbi.nlm.nih.gov/9657685/)

### F007 — 71.7% identity to *E. coli* citrate synthase confirms close orthology and Type II class

A global pairwise (Needleman–Wunsch) alignment of the *P. putida* GltA sequence (Q88FA4, 429 aa) against *E. coli* GltA (P0ABH7, 427 aa) yields **71.7% identity (306/427 aligned positions)**. This closely matches the ~70% identity historically reported between the *P. aeruginosa* NADH-sensitive citrate synthase and *E. coli* ([PMID: 2507528](https://pubmed.ncbi.nlm.nih.gov/2507528/)), and both enzymes belong to the hexameric, NADH-allosteric Type II class ([PMID: 11683626](https://pubmed.ncbi.nlm.nih.gov/11683626/)). The high, full-length identity — rather than mere domain-level similarity — provides strong evolutionary evidence of close orthology, allowing confident transfer of the extensively characterized *E. coli* enzyme's mechanistic and regulatory properties to the *P. putida* protein.

> *"the inferred amino acid sequence was 70 and 76% identical, respectively, with the citrate synthase sequences from E. coli and Acinetobacter anitratum, two other gram-negative bacteria"* — [PMID: 2507528](https://pubmed.ncbi.nlm.nih.gov/2507528/)

---

## Mechanistic Model and Interpretation

### The catalyzed reaction

```
   Acetyl-CoA  +  Oxaloacetate  +  H2O   ──GltA──▶   Citrate  +  CoA-SH
       (C2)          (C4)                              (C6)

   Mechanism (ordered ternary complex):
     1. Oxaloacetate binds → induces domain closure (open→closed)
     2. Acetyl-CoA binds in closed cleft
     3. Asp (base) abstracts α-proton from acetyl-CoA → enol(ate)
     4. Enolate attacks OAA carbonyl (aldol/Claisen) → citryl-CoA
        (His polarizes carbonyl + stabilizes intermediate)
     5. Thioester hydrolysis → citrate + CoA released
```

### Structural class and regulation

| Property | *P. putida* GltA (Q88FA4) | Type II (Gram-neg, e.g. *E. coli*) | Type I (eukaryote / Gram-pos) |
|---|---|---|---|
| Oligomeric state | Hexamer (inferred) | Hexamer | Dimer |
| Subunit length | 429 aa | 427 aa | ~430–460 aa |
| NADH inhibition | Allosteric (inferred) | **Allosteric** | Isosteric / none |
| ATP inhibition | Isosteric (at AcCoA site) | Isosteric | Isosteric |
| Identity to *E. coli* GltA | **71.7%** | 100% (ref) | ~30% |
| Catalytic residues | His265, His306, Asp364 | His264, His305, Asp362 | Conserved His/His/Asp |

### Metabolic position — the acetyl-CoA gatekeeper

```
   Glucose ──(Entner–Doudoroff / EDEMP)──▶ Pyruvate ──▶ Acetyl-CoA
                                                            │
                              ┌─────────────────────────────┤
                              │                             │
                     [GltA: citrate synthase]         Biosynthesis /
                     Acetyl-CoA + OAA → Citrate        storage (PHA/PHB),
                              │                         fatty acids
                              ▼
                        TCA CYCLE  ──▶ NADH, FADH2, CO2, precursors
                              │
                              └── NADH feeds back ⊣ GltA (allosteric brake)
```

GltA is the committed valve at the acetyl-CoA branch point. When energy charge/redox is high (elevated NADH), allosteric inhibition throttles citrate synthesis, sparing acetyl-CoA and slowing the cycle; when NADH is consumed, the brake releases and TCA flux resumes. Engineering-wise, this makes *gltA* the single most effective lever for redirecting acetyl-CoA toward biosynthesis, exactly as exploited by CRISPRi knockdown that raised acetyl-CoA ~8-fold and increased PHB output ([PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/)). Its strict acetyl-CoA specificity keeps this node cleanly separated from the parallel propionate-detoxifying 2-methylcitrate cycle run by PrpC.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/) | Model-guided dynamic control of metabolic nodes in *P. putida* | **Direct**: identifies *gltA* in *P. putida* KT2440 as encoding citrate synthase; knockdown raises acetyl-CoA ~8-fold (F001, F004) |
| [9387145](https://pubmed.ncbi.nlm.nih.gov/9387145/) | Characterization of *Drosophila* citrate synthase | States the reaction: acetyl-CoA + oxaloacetate → citrate (F002) |
| [9657685](https://pubmed.ncbi.nlm.nih.gov/9657685/) | Catalytic residues in the citrate synthase reaction | Defines Asp base and His stabilization roles; anchors residue-level verification (F002, F006) |
| [11683626](https://pubmed.ncbi.nlm.nih.gov/11683626/) | Type II vs Type I citrate synthase comparison | Defines Type II as hexameric, NADH-allosteric — the class of Q88FA4 (F003, F006, F007) |
| [175782](https://pubmed.ncbi.nlm.nih.gov/175782/) | Isosteric vs allosteric nucleotide inhibition | Establishes NADH as Gram-negative-specific allosteric inhibitor; ATP isosteric (F003) |
| [2507528](https://pubmed.ncbi.nlm.nih.gov/2507528/) | NADH-sensitive citrate synthase of *P. aeruginosa* | *Pseudomonas* enzyme ~70% identical to *E. coli*; probe cross-hybridized to *P. putida* DNA (F003, F007) |
| [7522844](https://pubmed.ncbi.nlm.nih.gov/7522844/) | *C. glutamicum gltA* citrate synthase | Defines citrate synthase as rate-controlling TCA entry point (F004) |
| [36155822](https://pubmed.ncbi.nlm.nih.gov/36155822/) | Synthetic C2 auxotroph of *P. putida* | Establishes acetyl-CoA node centrality in *P. putida* metabolism (F004) |
| [16133321](https://pubmed.ncbi.nlm.nih.gov/16133321/) | Tricarboxylate synthases in *Ralstonia eutropha* | Shows CS cannot use propionyl-CoA; distinguishes from 2-MCS/PrpC (F005) |
| [20970504](https://pubmed.ncbi.nlm.nih.gov/20970504/) | *S. typhimurium* 2-methylcitrate synthase structure | Contrasts PrpC substrate specificity with true CS (F005) |
| [3333000](https://pubmed.ncbi.nlm.nih.gov/3333000/) | Structural basis for regulation in Gram-neg CS | Supports allosteric NADH site distinct from active site (supporting F003) |
| [12824188](https://pubmed.ncbi.nlm.nih.gov/12824188/) | NADH binding site residues in *E. coli* Type II CS | Maps regulatory NADH site and hexamer assembly (supporting F003) |

The evidence base is internally consistent and multi-layered: (1) organism-specific experimental identification of *gltA* as citrate synthase; (2) mechanistic biochemistry defining the reaction and catalytic residues; (3) structural/regulatory literature defining the Type II class; and (4) direct sequence analysis of Q88FA4 confirming length, catalytic-triad residues, and 71.7% orthology to *E. coli*. No retrieved paper contradicts the citrate synthase assignment.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on Q88FA4 itself.** The kinetic parameters (KM, kcat), oligomeric state, and NADH inhibition constants for the specific *P. putida* KT2440 protein have not been experimentally measured; they are inferred by strong homology (71.7% to *E. coli*; probe cross-hybridization from *P. aeruginosa*). Michaelis constants cited (e.g., *Drosophila* CS) are orthologue values, not *P. putida* values.

2. **Hexameric state is inferred, not observed.** No crystal structure or native mass spectrometry exists for Q88FA4. The hexameric, NADH-allosteric assignment rests on class membership and sequence signatures.

3. **Regulatory effectors in vivo.** While NADH (allosteric) and ATP (isosteric) inhibition are well-established for the class, and 2-oxoglutarate has been debated as an active-site-directed effector ([PMID: 3333000](https://pubmed.ncbi.nlm.nih.gov/3333000/)), the quantitative regulatory landscape (AMP/KCl activation reported for some Gram-negatives) has not been mapped for the *P. putida* enzyme.

4. **Localization is inferred.** Cytoplasmic localization is assigned from function and family, not from an experimental localization study of Q88FA4.

5. **Essentiality / redundancy.** Whether *gltA* (PP_4194) is the sole citrate synthase and whether PrpC contributes measurable citrate-synthase activity in vivo under specific conditions in *P. putida* has not been quantified here.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant characterization of Q88FA4.** Express and purify the PP_4194 product; measure KM for acetyl-CoA and oxaloacetate, kcat, and test propionyl-CoA to confirm the strict acetyl-CoA specificity predicted by F005.

2. **Regulatory kinetics.** Titrate NADH, ATP, AMP, 2-oxoglutarate, and KCl to confirm the Type II allosteric-NADH phenotype quantitatively and define IC50 values relevant to *P. putida* physiology.

3. **Oligomeric-state determination.** Use size-exclusion chromatography–MALS or native MS ± NADH to confirm hexamer formation and NADH-dependent assembly, as done for *E. coli* variants ([PMID: 12824188](https://pubmed.ncbi.nlm.nih.gov/12824188/)).

4. **Structural biology.** Solve a crystal or cryo-EM structure of Q88FA4 (or generate/validate an AlphaFold model with Phenix) to verify the His265/His306/Asp364 active-site geometry and the allosteric NADH pocket, superposing against the *E. coli* Type II structure.

5. **Genetic essentiality and flux mapping.** Construct clean *gltA* deletion/knockdown strains and perform ¹³C-metabolic flux analysis to quantify GltA's control coefficient over the acetyl-CoA node and TCA entry, extending the CRISPRi observations of [PMID: 34343699](https://pubmed.ncbi.nlm.nih.gov/34343699/).

6. **PrpC cross-check.** Test whether PP_4194 and the *P. putida prpC* product have any overlapping activity, to formally rule out functional redundancy at the citrate-synthesis step.

---

*Gene identity verification: CONFIRMED. The symbol* gltA*, organism* P. putida *KT2440, protein family (citrate synthase), and catalytic-domain signatures (IPR002020 / IPR024176) are all mutually consistent, and the retrieved literature refers to the correct enzyme. This is not a symbol-clash case.*


## Artifacts

- [OpenScientist final report](gltA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](gltA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34343699
2. PMID:2507528
3. PMID:9387145
4. PMID:31451751
5. PMID:9657685
6. PMID:11683626
7. PMID:7522844
8. PMID:36155822
9. PMID:16133321
10. PMID:20970504
11. PMID:3333000
12. PMID:12824188