---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T09:11:25.393881'
end_time: '2026-07-15T09:48:04.202436'
duration_seconds: 2198.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: gntZ
  gene_symbol: gntZ
  uniprot_accession: Q88FP6
  protein_description: 'SubName: Full=6-phosphogluconate dehydrogenase, decarboxylating
    {ECO:0000313|EMBL:AAN69633.1}; EC=1.1.1.44 {ECO:0000313|EMBL:AAN69633.1};'
  gene_info: Name=gntZ {ECO:0000313|EMBL:AAN69633.1}; OrderedLocusNames=PP_4043 {ECO:0000313|EMBL:AAN69633.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the 6-phosphogluconate dehydrogenase family.
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6DGDH_YqeC. (IPR004849);
    6PGD_dom2. (IPR013328); 6PGDH_C. (IPR006114); 6PGDH_NADP-bd. (IPR006115)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: gntZ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: gntZ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FP6
- **Protein Description:** SubName: Full=6-phosphogluconate dehydrogenase, decarboxylating {ECO:0000313|EMBL:AAN69633.1}; EC=1.1.1.44 {ECO:0000313|EMBL:AAN69633.1};
- **Gene Information:** Name=gntZ {ECO:0000313|EMBL:AAN69633.1}; OrderedLocusNames=PP_4043 {ECO:0000313|EMBL:AAN69633.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the 6-phosphogluconate dehydrogenase family.
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6DGDH_YqeC. (IPR004849); 6PGD_dom2. (IPR013328); 6PGDH_C. (IPR006114); 6PGDH_NADP-bd. (IPR006115)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "gntZ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'gntZ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **gntZ** (gene ID: gntZ, UniProt: Q88FP6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *gntZ* (PP_4043 / UniProt Q88FP6) in *Pseudomonas putida* KT2440

## Summary

**gntZ (PP_4043; UniProt Q88FP6) in *Pseudomonas putida* KT2440 encodes a 6-phosphogluconate dehydrogenase, decarboxylating (6PGDH; EC 1.1.1.44).** The enzyme catalyzes the NADP⁺-dependent oxidative decarboxylation of 6-phospho-D-gluconate to D-ribulose-5-phosphate, CO₂, and NADPH — the third step and second oxidative step of the pentose phosphate pathway (PPP). The gene symbol *gntZ*, the EC number, the protein family assignment (6-phosphogluconate dehydrogenase family), and the InterPro domain architecture all agree with this identity, and there is no evidence of gene-symbol ambiguity confounding the annotation for this organism. The identity of the target is therefore secure.

A key refinement produced by this investigation is structural. Although some UniProt domain listings suggest a "long-chain" 6PGDH, the actual Q88FP6 sequence is only **327 residues (~35.4 kDa)** — far shorter than the canonical ~470-residue long-chain dimeric 6PGDHs (e.g., *E. coli* Gnd, human PGD). Sequence-based classification (NCBIfam TIGR00872 "gnd_rel", PRK09599) and the presence of the short-chain-specific InterPro domain **IPR004849 (6DGDH_YqeC)** place Q88FP6 firmly in the **short-chain (Gnd-related / YqeC-type) 6PGDH subclass**, the same structural family as the tetrameric *Gluconobacter oxydans* enzyme (Go6PGDH) whose 2.0 Å crystal structure was recently solved. This subclass uses a substrate-induced quaternary-compaction mechanism and a conserved catalytic histidine, rather than the hinged domain-closure motion of long-chain dimeric enzymes.

Functionally, gntZ operates at the central **6-phosphogluconate (6PG) branch point** of *P. putida* central carbon metabolism. In this organism glucose is funneled to 6PG via three convergent peripheral pathways, and 6PG is then partitioned between the dominant Entner–Doudoroff (ED) route (via Edd/Eda) and the oxidative PPP branch (via 6PGDH/gntZ). Because *P. putida* lacks a functional Embden–Meyerhof–Parnas (EMP) glycolysis, ED carries most catabolic flux, while gntZ diverts a fraction of 6PG into the oxidative PPP to generate NADPH reducing power and ribulose-5-phosphate for biosynthesis. This activity is embedded in the cyclic **EDEMP** architecture that gives *P. putida* its characteristic catabolic overproduction of NADPH — the biochemical basis of its renowned robustness to oxidative and solvent stress. gntZ is the **sole 6PGDH** encoded in the KT2440 genome, is genomically **paired with zwfB (glucose-6-phosphate dehydrogenase)**, and is a repeated target of adaptive mutation when engineers redirect 6PG flux away from carbon-wasting oxidative dissipation.

---

## Gene / Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and all passed:

| Verification step | Result |
|---|---|
| Gene symbol *gntZ* matches protein description | ✔ *gntZ* is annotated as 6-phosphogluconate dehydrogenase (EC 1.1.1.44) in UniProt Q88FP6 |
| Organism correct | ✔ *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), locus PP_4043 |
| Protein family / domains align with literature | ✔ 6-phosphogluconate dehydrogenase family; Rossmann NADP-binding fold + C-terminal all-α domain confirmed |
| No confounding literature on a same-symbol gene in another organism | ✔ Central-metabolism/flux literature for KT2440 consistently references the same PPP node |

**One important nuance:** the gene symbol *gntZ* is used in some organisms (notably *Bacillus subtilis*) for a 6PGDH involved in gluconate catabolism, and in *E. coli* the primary 6PGDH is *gnd*. In *P. putida* KT2440 the symbol *gntZ* is applied to PP_4043, the organism's single 6PGDH. The identity is not ambiguous here: the EC number, family, domain architecture, and genomic context all converge on the same biochemical function. Literature is genuinely limited for the *P. putida* enzyme *specifically* (no dedicated biochemical/structural study of Q88FP6 exists), so parts of this report necessarily rely on well-supported inference from close homologs and from the organism's central-metabolism flux literature. These inferences are flagged explicitly throughout.

---

## Key Findings

### Finding 1 — gntZ encodes 6-phosphogluconate dehydrogenase (6PGDH, EC 1.1.1.44), the decarboxylating oxidative-PPP enzyme

UniProt Q88FP6 annotates the PP_4043 gene product as "6-phosphogluconate dehydrogenase, decarboxylating; EC 1.1.1.44," gene *gntZ*, in *P. putida* KT2440. The protein carries the canonical 6PGDH domain series: an N-terminal NADP-binding Rossmann domain (IPR006115, 6PGDH_NADP-bd), a central domain (IPR013328, 6PGD_dom2), and an all-α C-terminal domain (IPR006114, 6PGDH_C; IPR008927, 6-PGluconate_DH-like C superfamily). The reaction catalyzed is:

```
6-phospho-D-gluconate + NADP⁺  →  D-ribulose-5-phosphate + CO₂ + NADPH
```

This is the committed oxidative-decarboxylating step of the oxidative pentose phosphate pathway (oxPPP). The recent structural review of 6PGDHs states that "**6-Phosphogluconate dehydrogenases (6PGDHs) catalyze a key oxidative step in the oxidative pentose phosphate pathway (oxPPP), a route essential for NAD(P)H generation and carbon metabolism in bacteria and eukaryotes**" ([PMID: 41765070](https://pubmed.ncbi.nlm.nih.gov/41765070/)), confirming both the reaction and its metabolic significance. The substrate specificity of the enzyme family is narrow — 6-phospho-D-gluconate is the physiological substrate, with NADP⁺ (GO:0050661 "NADP binding") as the strongly preferred electron acceptor, and the catalytic activity annotated as GO:0004616 "phosphogluconate dehydrogenase (decarboxylating) activity."

### Finding 2 — CORRECTION: Q88FP6 is a SHORT-CHAIN (Gnd-related / YqeC-type) 6PGDH (~327 aa), not the long-chain dimeric type

A central refinement of this investigation is that the *P. putida* enzyme is **not** a member of the classical long-chain dimeric 6PGDH class despite some database domain listings. The Q88FP6 sequence is only **327 residues (35.4 kDa)**, well short of the ~470-residue long-chain enzymes (*E. coli* Gnd, human PGD). Key sequence-based evidence:

- Classified by NCBIfam **TIGR00872 "gnd_rel"** (6-phosphogluconate dehydrogenase, related/short type) and **PRK09599**.
- Carries the short-chain-specific InterPro domain **IPR004849 (6DGDH_YqeC)**, alongside the Rossmann NADP-binding fold (IPR006115 / IPR036291; Pfam PF03446 NAD_binding_2, PF00393 6PGD) and the C-terminal all-α domain (IPR006114 / IPR008927).
- The N-terminus begins **MQLGIIGLGRMGG…**, containing the canonical GxGxxG dinucleotide-binding fingerprint.
- UniProt GO annotations: F: phosphogluconate dehydrogenase (decarboxylating) activity (GO:0004616); F: NADP binding (GO:0050661); P: pentose-phosphate shunt (GO:0006098); P: D-gluconate metabolic process (GO:0019521).

This places Q88FP6 in the **same structural subclass as the tetrameric *Gluconobacter oxydans* enzyme (Go6PGDH)**. The distinction matters mechanistically. The review notes: "**While the structural basis of substrate recognition is well established for long-chain dimeric 6PGDHs, the mechanisms used by short-chain tetrameric enzymes remain poorly defined. Here, we present a 2.0 Å crystal structure of tetrameric 6PGDH from *Gluconobacter oxydans* (Go6PGDH) in complex with 6-phosphogluconate (6PG)**" ([PMID: 41765070](https://pubmed.ncbi.nlm.nih.gov/41765070/)). The likely quaternary state of Q88FP6 is therefore **tetrameric**, in contrast to the dimeric long-chain enzymes.

### Finding 3 — Glucose is funneled to 6-phosphogluconate via three convergent peripheral pathways; 6PGDH operates at this hub

¹³C-flux and genomic analyses established that *P. putida* KT2440 catabolizes glucose through three simultaneously operating, convergent routes that all meet at **6-phosphogluconate (6PG)**: (i) direct uptake and phosphorylation to glucose-6-phosphate followed by oxidation via Zwf; (ii) periplasmic oxidation of glucose to gluconate, uptake, then gluconokinase; and (iii) further oxidation of gluconate to 2-ketogluconate and its subsequent phosphorylation/reduction. The primary study states that "**glucose catabolism in Pseudomonas putida occurs through the simultaneous operation of three pathways that converge at the level of 6-phosphogluconate, which is metabolized by the Edd and Eda Entner/Doudoroff enzymes to central metabolites**" ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)). A complementary regulatory study confirmed that "**Pseudomonas putida KT2440 channels glucose to the central Entner-Doudoroff intermediate 6-phosphogluconate through three convergent pathways**" ([PMID: 18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/)).

6PG is thus the branch-point metabolite at which the Edd/Eda ED enzymes and the decarboxylating 6PGDH (gntZ) compete for carbon flux. Because *P. putida* lacks a functional EMP glycolysis (it has no 6-phosphofructokinase), the ED pathway is the dominant catabolic route, while gntZ draws a smaller fraction of 6PG into the oxidative PPP branch.

### Finding 4 — 6PGDH participates in the EDEMP cycle and is a cytoplasmic source of NADPH reducing power

Nikel et al. combined ¹³C-metabolic flux analysis, quantitative physiology, and in vitro enzyme assays to show that in glucose-grown KT2440, ~90% of sugar is converted to gluconate/6-phosphogluconate and channeled into the ED pathway, while ~10% of the triose phosphates are recycled back to hexose phosphates through a cyclic architecture that merges ED, gluconeogenic EMP, and pentose-phosphate enzymes — the **EDEMP cycle**. The authors report: "**This set of reactions merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle). Determination of the NADPH balance revealed that the default metabolic state of P. putida KT2440 is characterized by a slight catabolic overproduction of reducing power**" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)).

The oxidative-PPP steps within this cycle — Zwf (glucose-6-P dehydrogenase) and 6PGDH (gntZ) — are the NADPH-generating reactions responsible for this reducing-power surplus. As a soluble dehydrogenase with no signal peptide or membrane-anchoring features, **6PGDH/gntZ carries out its reaction in the cytoplasm.** This cytoplasmic NADPH overproduction is widely regarded as the biochemical basis of *P. putida*'s exceptional tolerance to oxidative and solvent stress, since NADPH fuels antioxidant and redox-repair systems as well as anabolism.

### Finding 5 — gntZ is the SOLE 6-phosphogluconate dehydrogenase encoded in the KT2440 genome

A proteome-wide query of *P. putida* KT2440 (organism_id 160488) for "phosphogluconate dehydrogenase" / EC 1.1.1.44 / EC 1.1.1.343 returns exactly one hit: **Q88FP6 (gntZ, PP_4043, 327 aa)**. No second (e.g., long-chain dimeric) 6PGDH paralog is annotated. This is functionally important: the "6-phosphogluconate dehydrogenase (Gnd)" activity invoked throughout the KT2440 central-metabolism and flux literature (e.g., Nikel et al. 2015) is attributable **specifically and uniquely** to this gene product. There is no genetic redundancy, so gntZ is a genuine single point of control over oxidative-PPP flux from the 6PG node, and its function cannot be compensated by a redundant isozyme.

### Finding 6 — gntZ (PP_4043) is genomically paired with zwfB (PP_4042), reinforcing its oxidative-PPP role

Inspection of the PP_4040–PP_4046 locus shows that **PP_4042 = zwfB** encodes glucose-6-phosphate 1-dehydrogenase (Zwf, 501 aa), located immediately upstream of and adjacent to **PP_4043 = gntZ** (6PGDH, 327 aa). Zwf catalyzes the *first* committed oxidative-PPP step (glucose-6-P → 6-phosphogluconolactone, + NADPH), and 6PGDH/gntZ catalyzes the *third* (6-phosphogluconate → ribulose-5-P + CO₂ + NADPH). Their adjacency — a **zwfB–gntZ pair** — is the classic bacterial arrangement that clusters the two NADP⁺-reducing oxidative-PPP dehydrogenases. This genomic context is strong corroborating evidence, independent of the sequence annotation, that gntZ functions in the oxidative pentose phosphate branch, likely under coordinated expression with Zwf. (KT2440 carries multiple *zwf* paralogs; PP_4042/*zwfB* is the one co-located with *gntZ*.)

### Finding 7 — gntZ is a repeated target of adaptive mutation when 6PG flux is redirected in engineered *P. putida*

Bentley et al. (2020), while engineering glucose→muconate conversion in KT2440, performed adaptive laboratory evolution (ALE) of strains lacking glucose dehydrogenase (*gcd*). Whole-genome resequencing of improved isolates revealed that "**The genes gntZ and gacS were also disrupted in several evolved clones**" ([PMID: 31931111](https://pubmed.ncbi.nlm.nih.gov/31931111/)). This is direct, strain-level genetic evidence that inactivating gntZ is *selectively advantageous* when carbon must be conserved for product formation — consistent with gntZ's role in diverting 6PG into the **carbon-losing** oxidative branch (each turn of 6PGDH releases one carbon as CO₂). The same study identified the central-carbon repressor HexR as a key regulatory node: "**Deletion of the transcriptional repressor gene hexR improved strain growth and increased the muconate production rate**" ([PMID: 31931111](https://pubmed.ncbi.nlm.nih.gov/31931111/)). HexR governs the regulon that includes the 6PG node where gntZ acts, tying gntZ's expression to the organism's central carbon control circuitry (the genome-scale HexR regulon was subsequently mapped in [PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)).

### Finding 8 — Inferred catalytic mechanism of the short-chain subclass: substrate-induced quaternary tightening and a conserved catalytic histidine

Because no structure of the *P. putida* enzyme exists, the best structural model is the closest well-characterized homolog: the tetrameric Go6PGDH from *Gluconobacter oxydans*, solved at 2.0 Å in complex with 6PG (Maturana et al.). That work shows that short-chain 6PGDHs do **not** use the hinged domain-closure motion of long-chain dimeric enzymes. Instead: "**6PG induces a compaction of the tetramer mediated by two conserved C-terminal elements: an inter-protomer ionic 'lock' and an intra-subunit C-terminal 'latch' that together stabilize a closed catalytic pocket. Molecular-dynamics simulations identify His328 as a central residue that couples C-terminal tail closure to direct ligand coordination, and mutagenesis analysis confirms its essential role in catalytic efficiency**" ([PMID: 41765070](https://pubmed.ncbi.nlm.nih.gov/41765070/)). 6PG binding is strongly enthalpy-driven. Since Q88FP6 (327 aa, Gnd-related/YqeC-type, TIGR00872) is in this same short-chain subclass, this substrate-recognition and catalytic paradigm — a conserved catalytic His and C-terminal "lock/latch" closure — is the most credible model for the *P. putida* enzyme, pending direct structural determination.

---

## Mechanistic Model / Interpretation

### The reaction and its place in metabolism

gntZ catalyzes the oxidative, irreversible decarboxylation step of the pentose phosphate pathway:

```
   Glucose-6-P                6-Phosphogluconate           Ribulose-5-P
        │                            │                          │
        │  Zwf (zwfB, PP_4042)       │  6PGDH (gntZ, PP_4043)    │
        │  +NADP⁺ → +NADPH           │  +NADP⁺ → +NADPH + CO₂    │
        ▼                            ▼                          ▼
   [oxidative PPP step 1]      [oxidative PPP step 3]     → PPP / biosynthesis
                                     │
                                     │ (competing fate)
                                     ▼
                              Edd / Eda (Entner–Doudoroff)
                                     │
                                     ▼
                         pyruvate + glyceraldehyde-3-P  → central metabolism
```

### The 6-phosphogluconate branch point

The defining feature of gntZ's biology is that it sits at a **carbon-partitioning branch point**. In *P. putida* KT2440, glucose from three convergent peripheral pathways all arrives at 6PG. At that node, two enzyme systems compete:

| Fate of 6PG | Enzymes | Carbon economy | Redox output |
|---|---|---|---|
| **Entner–Doudoroff (dominant)** | Edd + Eda | Carbon-conserving (→ pyruvate + G3P) | — |
| **Oxidative PPP (gntZ)** | 6PGDH | Carbon-losing (releases 1 C as CO₂) | +NADPH |

Because *P. putida* has no functional EMP glycolysis, ED carries the bulk of catabolic flux, and gntZ handles a minority fraction. The gntZ branch is not a waste pathway, however — it is the organism's principal route for balancing NADPH supply and generating ribulose-5-phosphate (a precursor for nucleotides and aromatic amino acids). This dual role — reducing power + biosynthetic pentose — is why the reaction is retained despite its carbon cost.

### The EDEMP cycle and NADPH overproduction

gntZ's oxidative-PPP activity is woven into the **EDEMP cycle**, in which ~10% of triose phosphates are recycled back to hexose phosphates and re-oxidized through Zwf and 6PGDH. Each recycling turn extracts additional NADPH. The net effect, quantified by Nikel et al. via ¹³C-flux analysis, is a **catabolic overproduction of NADPH** — the redox surplus that underlies *P. putida*'s well-known robustness to oxidative and solvent stress. gntZ, as the sole 6PGDH and one of only two NADP⁺-reducing oxidative-PPP dehydrogenases (with Zwf), is a direct contributor to this surplus.

### Regulatory and engineering logic

The engineering literature closes the loop on gntZ's physiological role. When metabolic engineers want to maximize carbon yield toward products (e.g., muconate), the carbon-losing oxidative branch is a liability. Adaptive laboratory evolution repeatedly *disrupts gntZ*, and deletion of the HexR repressor (which controls the 6PG-node regulon) improves flux and growth. This is a striking, orthogonal confirmation that gntZ's function is exactly what the biochemistry predicts: to shunt 6PG into the oxidative branch, at the cost of one carbon per turn, in exchange for NADPH.

### Localization

All evidence — a soluble dehydrogenase fold, absence of any signal peptide or transmembrane segment, GO annotation to cytoplasmic pentose-phosphate-shunt activity, and its participation in cytoplasmic flux cycles — indicates that gntZ operates in the **cytoplasm**, where its substrate 6PG, cofactor NADP⁺, and downstream ED and PPP enzymes reside.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [41765070](https://pubmed.ncbi.nlm.nih.gov/41765070/) | *Structural, dynamic, evolutionary determinants of substrate binding in tetrameric 6PGDH from* Gluconobacter oxydans | Defines the reaction/oxPPP context (F1); defines the short-chain tetrameric subclass to which Q88FP6 belongs (F2); provides the catalytic-mechanism model — C-terminal lock/latch + catalytic His (F8) |
| [17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/) | *Convergent peripheral pathways catalyze initial glucose catabolism in* P. putida | Establishes 6PG as the convergent hub metabolite and gntZ's substrate pool (F3) |
| [18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/) | *A set of activators and repressors control peripheral glucose pathways in* P. putida | Confirms the three convergent pathways feeding 6PG (F3) |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through the EDEMP cycle* | Documents the EDEMP cycle and NADPH overproduction driven by oxidative-PPP enzymes including 6PGDH (F4) |
| [31931111](https://pubmed.ncbi.nlm.nih.gov/31931111/) | *Engineering glucose metabolism for enhanced muconic acid production in* P. putida KT2440 | Direct genetic evidence that gntZ is disrupted during selection for improved carbon yield; identifies HexR regulation of the 6PG node (F7) |

**Supporting / contextual literature.** Additional KT2440-focused papers ([PMID: 34403199](https://pubmed.ncbi.nlm.nih.gov/34403199/), [PMID: 39590355](https://pubmed.ncbi.nlm.nih.gov/39590355/), [PMID: 34508142](https://pubmed.ncbi.nlm.nih.gov/34508142/), [PMID: 41858775](https://pubmed.ncbi.nlm.nih.gov/41858775/), [PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/), [PMID: 41141486](https://pubmed.ncbi.nlm.nih.gov/41141486/)) consistently describe the three-pathway convergence on 6PG, ED dominance, and HexR-centered regulation of central carbon metabolism, reinforcing the metabolic context in which gntZ acts. The HexR systems-biology study ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)) maps the regulon governing this node in detail. A second listing of the Go6PGDH structural work ([PMID: 41648376](https://pubmed.ncbi.nlm.nih.gov/41648376/)) restates the short-chain-vs-long-chain distinction central to Finding 2.

**Cross-organism 6PGD literature** ([PMID: 42276385](https://pubmed.ncbi.nlm.nih.gov/42276385/), mouse depression model; [PMID: 40742331](https://pubmed.ncbi.nlm.nih.gov/40742331/), 6PGD as an oncology target; [PMID: 40680683](https://pubmed.ncbi.nlm.nih.gov/40680683/), an antimicrobial peptide derived from a 6PGDH minimal domain; [PMID: 41339799](https://pubmed.ncbi.nlm.nih.gov/41339799/), 6PGD as a *Toxoplasma* virulence gene) confirms the enzyme family's conserved role in NADPH generation via the PPP across kingdoms, but none pertains directly to the *P. putida* protein, and none was used to attribute organism-specific claims.

---

## Supported and Refuted / Revised Hypotheses

| Hypothesis | Status | Evidence |
|---|---|---|
| gntZ/PP_4043 encodes 6PGDH (EC 1.1.1.44) catalyzing NADP⁺-dependent oxidative decarboxylation of 6PG | **Supported** | UniProt annotation + GO:0004616/GO:0050661; family/domain signatures; oxPPP literature (F1) |
| Substrate is 6-phospho-D-gluconate; cofactor NADP⁺ | **Supported** | GO annotations; family; homolog structure with bound 6PG (F1, F8) |
| Enzyme acts in the cytoplasm | **Supported** | No signal/TM sequence; soluble oxPPP dehydrogenase (F4) |
| Functions in oxidative PPP / EDEMP cycle providing NADPH + ribulose-5-P | **Supported** | Nikel 2015 flux analysis; del Castillo 2007/2008 (F3, F4) |
| Protein is a **long-chain dimeric** 6PGDH | **Revised → Refuted** | 327-aa length + TIGR00872/IPR004849 show it is a **short-chain (YqeC-type) tetrameric** subclass member (F2) |
| gntZ activity influences carbon partitioning at the 6PG node | **Supported (genetic)** | gntZ repeatedly disrupted in ALE muconate-overproducers (Bentley 2020) (F7) |
| gntZ is the sole 6PGDH in the genome | **Supported** | Proteome-wide UniProt query returns exactly one 6PGDH (F5) |

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88FP6.** There is no published enzyme-kinetics study (kcat, Km for 6PG and NADP⁺, cofactor preference NADP⁺ vs NAD⁺) or crystal structure of the *P. putida* KT2440 enzyme itself. All catalytic and quaternary-structure statements are inferences from the short-chain subclass and the Go6PGDH structure.

2. **Quaternary state inferred, not measured.** Q88FP6 is assigned to the short-chain (tetrameric) subclass by sequence, but its oligomeric state has not been experimentally confirmed for the *P. putida* protein.

3. **Domain-annotation inconsistency in databases.** UniProt lists long-chain-style domains (IPR006114/IPR006115/IPR013328) while the sequence length and TIGR00872/IPR004849 assignments indicate a short-chain enzyme. This report resolves the discrepancy in favor of the short-chain classification based on sequence length and family-specific signatures, but the underlying database entry is internally mixed.

4. **Flux magnitude through gntZ is context-dependent.** The ¹³C-flux data establish that oxidative-PPP flux is a minority of total 6PG flux under glucose growth, but the exact fraction attributable to gntZ varies with carbon source, growth rate, and redox demand and has not been isolated for gntZ alone.

5. **Regulation of gntZ specifically.** While HexR governs the 6PG-node regulon, direct evidence that HexR binds the gntZ promoter and quantitatively controls gntZ transcription in *P. putida* is inferential rather than gene-specific; this should be confirmed against the genome-scale HexR regulon map ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)).

6. **The catalytic His is homology-inferred.** The essential catalytic histidine (His328 in Go6PGDH) is proposed for Q88FP6 by homology; the exact residue position in the *P. putida* sequence has not been experimentally validated.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme kinetics.** Express Q88FP6, purify, and measure kcat and Km for 6-phospho-D-gluconate, plus NADP⁺ vs NAD⁺ cofactor preference, to confirm EC 1.1.1.44 activity and quantify substrate specificity directly.

2. **Determine oligomeric state.** Use size-exclusion chromatography with multi-angle light scattering (SEC-MALS) or native mass spectrometry to test the predicted tetrameric quaternary structure of the short-chain subclass.

3. **Structure determination.** Solve the crystal or cryo-EM structure of Q88FP6, ideally in complex with 6PG and NADP(H), to confirm the C-terminal "lock/latch" closure mechanism and identify the catalytic histidine.

4. **Targeted mutagenesis of the predicted catalytic His.** Align Q88FP6 to Go6PGDH His328, mutate the corresponding residue, and test the loss of catalytic efficiency to validate the mechanistic model.

5. **Clean gntZ deletion and phenotyping.** Construct a markerless Δ*gntZ* mutant in KT2440 and characterize growth, NADPH/NADP⁺ ratio, oxidative-stress and solvent tolerance, and ¹³C-flux redistribution to quantify gntZ's contribution to the NADPH surplus and its role in stress robustness.

6. **Promoter/regulation mapping.** Use ChIP-exo or EMSA to test direct HexR binding at the gntZ promoter and RT-qPCR across glycolytic vs gluconeogenic carbon sources to define gntZ-specific transcriptional control.

7. **Flux-engineering validation.** Systematically compare muconate (or other product) yield in Δ*gntZ* vs wild-type engineered strains to confirm that removing the carbon-losing oxidative branch improves product carbon yield, as the adaptive-evolution data predict.

---

## Conclusion

*gntZ* (PP_4043; UniProt Q88FP6) in *Pseudomonas putida* KT2440 is the organism's **single 6-phosphogluconate dehydrogenase (6PGDH; EC 1.1.1.44)** — a soluble cytoplasmic, short-chain (Gnd-related/YqeC-type, ~327 aa) enzyme that catalyzes the NADP⁺-dependent oxidative decarboxylation of 6-phospho-D-gluconate to D-ribulose-5-phosphate, CO₂, and NADPH. It acts at the central 6-phosphogluconate branch point, diverting carbon from the dominant Entner–Doudoroff route into the oxidative pentose-phosphate branch of the EDEMP cycle, thereby supplying NADPH (reducing power for anabolism and stress defense) and ribulose-5-phosphate for biosynthesis. The identity, biochemistry, localization, and metabolic role are all well supported by convergent domain, genomic-context, ¹³C-flux, and adaptive-evolution evidence; the principal outstanding gaps are the absence of direct enzymatic and structural characterization of the *P. putida* protein itself.


## Artifacts

- [OpenScientist final report](gntZ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](gntZ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:41765070
2. PMID:17483213
3. PMID:18245293
4. PMID:26350459
5. PMID:31931111
6. PMID:41260329
7. PMID:34403199
8. PMID:39590355
9. PMID:34508142
10. PMID:41858775
11. PMID:41141486
12. PMID:41648376
13. PMID:42276385
14. PMID:40742331
15. PMID:40680683
16. PMID:41339799