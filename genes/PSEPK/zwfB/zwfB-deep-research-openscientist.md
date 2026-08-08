---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T08:08:43.660344'
end_time: '2026-07-15T09:07:09.481743'
duration_seconds: 3505.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: zwfB
  gene_symbol: zwfB
  uniprot_accession: Q88FP7
  protein_description: 'RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966};
    Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};'
  gene_info: Name=zwfB {ECO:0000313|EMBL:AAN69632.1}; Synonyms=zwf {ECO:0000256|HAMAP-Rule:MF_00966};
    OrderedLocusNames=PP_4042 {ECO:0000313|EMBL:AAN69632.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glucose-6-phosphate dehydrogenase family.
  protein_domains: G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675);
    G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: zwfB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: zwfB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FP7
- **Protein Description:** RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966}; Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};
- **Gene Information:** Name=zwfB {ECO:0000313|EMBL:AAN69632.1}; Synonyms=zwf {ECO:0000256|HAMAP-Rule:MF_00966}; OrderedLocusNames=PP_4042 {ECO:0000313|EMBL:AAN69632.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glucose-6-phosphate dehydrogenase family.
- **Key Domains:** G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675); G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "zwfB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'zwfB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **zwfB** (gene ID: zwfB, UniProt: Q88FP7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *zwfB* (PP_4042, UniProt Q88FP7) in *Pseudomonas putida* KT2440

**Gene:** *zwfB* (synonym *zwf*; ordered locus PP_4042)
**Protein:** Glucose-6-phosphate 1-dehydrogenase B (G6PDH-B / G6PD-B)
**UniProt:** Q88FP7 · **EC:** 1.1.1.49 · **Length:** 501 aa
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK

---

## Summary

**Identity confirmed.** The gene symbol *zwfB*, the organism *Pseudomonas putida* KT2440, and the glucose-6-phosphate dehydrogenase (G6PD) family/domain architecture in the target definition all match the primary literature and curated databases. There is no ambiguity: PP_4042 is unambiguously one of the three *bona fide zwf* paralogs of *P. putida* KT2440 (*zwfA* = PP_1022, *zwfB* = PP_4042, *zwfC* = PP_5351), and it has been purified, kinetically characterized, and genetically dissected in a dedicated study. This report therefore proceeds with high confidence on the correct target.

**Primary function.** *zwfB* encodes a soluble, cytoplasmic **glucose-6-phosphate 1-dehydrogenase (EC 1.1.1.49)** that catalyzes the first, committed step of the oxidative pentose-phosphate branch: the oxidation of intracellular **D-glucose 6-phosphate (G6P) to 6-phospho-D-glucono-1,5-lactone**, coupled to the reduction of NAD(P)⁺ to NAD(P)H. The lactone is subsequently hydrolyzed to 6-phosphogluconate (6PG), which feeds the Entner–Doudoroff (ED) pathway that dominates sugar catabolism in this bacterium. Structurally the protein is a canonical bilobal G6PD enzyme with an N-terminal Rossmann dinucleotide-binding domain and a C-terminal β+α domain, and it carries the conserved catalytic histidine (H189) that serves as the general base of the reaction.

**What makes ZwfB distinctive.** Among the three KT2440 G6PDH isozymes, ZwfB is the **constitutively expressed, NAD⁺-preferring/dual-cofactor** enzyme (cofactor specificity constant φ ≈ 0.86, i.e., a slight preference for NAD⁺), in contrast to the glucose/HexR-induced, NADP⁺-leaning ZwfA (φ ≈ 3.34) and the strongly NADP⁺-specific ZwfC (φ ≈ 2,082). *zwfB* is cotranscribed with *gnd/gntZ* (6-phosphogluconate dehydrogenase) and is **functionally redundant with *zwfA***: single Δ*zwfB* mutants grow normally on glucose, gluconate, and fructose, but the Δ*zwfAB* double mutant shows synergistic growth defects and cannot grow on ribose. Together, ZwfA and ZwfB carry essentially all of the physiologically relevant G6PDH activity in the cell, functioning as metabolic "gatekeepers" that gate carbon into the ED/EDEMP redox cycle and set cellular redox balance by supplying NAD(P)H. These conclusions rest on curated annotation, purified-enzyme kinetics, deletion genetics ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)), ¹³C flux analysis ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)), and a high-confidence AlphaFold model.

---

## Key Findings

### Finding 1 — ZwfB is a cytoplasmic glucose-6-phosphate 1-dehydrogenase catalyzing the first committed step of the oxidative PP branch

The core enzymatic identity of PP_4042 is firmly established. UniProt Q88FP7 (curated under HAMAP-Rule MF_00966) assigns the function "*Catalyzes the oxidation of glucose 6-phosphate to 6-phosphogluconolactone*," with the catalytic activity (Rhea RHEA:15841): **D-glucose 6-phosphate + NADP⁺ → 6-phospho-D-glucono-1,5-lactone + NADPH + H⁺**, EC 1.1.1.49. The enzyme is placed in the pentose-phosphate pathway as "*D-ribulose 5-phosphate from D-glucose 6-phosphate (oxidative stage): step 1/3.*" It is a 501-residue monomer of the G6PD family (Pfam PF00479 G6PD_N NAD-binding + PF02781 G6PD_C; InterPro IPR001282/IPR022674/IPR022675), and KEGG maps ppu:PP_4042 to ortholog K00036 (EC 1.1.1.49 / 1.1.1.363) within pathway ppu00030 (Pentose phosphate pathway).

The reaction and its downstream context are corroborated by primary literature. In the dedicated isozyme study, G6PDH "*catalyzes the first committing step in the oxidative branch of the pentose phosphate (PP) pathway, feeding either the reductive PP or the Entner-Doudoroff pathway*" ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). Independently, the flux-and-genomics analysis of *P. putida* glucose catabolism states that G6P is "*converted by glucose-6-phosphate dehydrogenase (encoded by the zwf genes) to 6-phosphogluconate*" ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)). Because both substrate (G6P) and product (the phospho-lactone → 6PG) are intracellular phosphorylated intermediates, the enzyme operates in the **cytoplasm**.

### Finding 2 — ZwfB is one of three G6PDH isozymes and, with ZwfA, carries most of the cellular G6PDH activity

*P. putida* KT2440 encodes **three** G6PDH paralogs — *zwfA* (PP_1022), *zwfB* (PP_4042), and *zwfC* (PP_5351), all mapping to KEGG K00036. Volke, Olavarría & Nikel (2021) systematically characterized all three ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). Genomic, genetic, and biochemical analyses showed that the enzymes differ in cofactor specificity, and that "*the isoforms encoded by zwfA and zwfB carry most of the activity, acting as metabolic*" gatekeepers for carbon entering the network at different nodes. The authors further note that "*the three G6PDHs of strain KT2440 have different cofactor specificities.*" The very existence of multiple isozymes is not idiosyncratic: "*multiplication of G6PDH isoforms is a widespread strategy in bacteria, correlating with the presence of an incomplete Embden-Meyerhof-Parnas pathway*" — precisely the situation in *P. putida*, which lacks a functional EMP glycolysis.

### Finding 3 — ZwfB acts within the ED/EDEMP-cycle architecture that dominates glucose catabolism and biases metabolism toward NADPH

*P. putida* KT2440 does not run canonical glycolysis (it lacks phosphofructokinase). Instead, ¹³C-flux analysis shows that "*90% of the consumed sugar was converted into gluconate, entering central carbon metabolism as 6-phosphogluconate and further channeled into the ED pathway*" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). Glucose reaches the cytoplasm in part via an ABC uptake system — "*Glucose is transported to the cytoplasm in a process mediated by an ABC uptake system*" ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)) — where it is phosphorylated by glucokinase to G6P and then oxidized by Zwf. This "phosphorylative" intracellular branch is one of three convergent peripheral routes that meet at 6-phosphogluconate. The cyclic operation of the ED/EMP/PP enzymes (the "EDEMP cycle") recycles a fraction of triose phosphates back to G6P, and "*cells growing on glucose thus run a biochemical cycle that favors NADPH formation*" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). ZwfB, acting in the cytosol on G6P, is one of the entry enzymes into this redox-biased cycle, and its reduced-cofactor output contributes to anabolic and anti-stress reducing power.

### Finding 4 — ZwfB is a constitutively expressed, NAD⁺-preferring/dual-cofactor isozyme, biochemically distinct from ZwfA and ZwfC

Volke, Olavarría & Nikel purified recombinant G6PDH-B and measured steady-state kinetics at 30 °C, finding a rapid-equilibrium random-ordered mechanism ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). The defining metric is the **cofactor specificity constant** φ = [k_cat/K_m(NADP⁺)] / [k_cat/K_m(NAD⁺)]. The three isozymes span nearly four orders of magnitude:

| Isozyme | Gene / locus | φ (NADP⁺/NAD⁺ preference) | Cofactor character | Expression |
|---|---|---|---|---|
| G6PDH-A | *zwfA* / PP_1022 | ~3.34 | Dual; uses NADP⁺ and NAD⁺ similarly | Glucose/HexR-induced |
| **G6PDH-B** | ***zwfB* / PP_4042** | **~0.86** | **Dual; slight NAD⁺ preference** | **Constitutive** |
| G6PDH-C | *zwfC* / PP_5351 | ~2,082 | Strongly NADP⁺-specific | Low in vivo activity |

Representative ZwfB kinetic parameters: with **NAD⁺**, k_cat ≈ 337 s⁻¹, K_m(NAD⁺) ≈ 113 µM, K_m(G6P) ≈ 291 µM; with **NADP⁺**, k_cat ≈ 190 s⁻¹, K_m(NADP⁺) ≈ 165 µM, K_m(G6P) ≈ 790 µM. The paper explicitly states that "G6PDH-B (which is constitutively expressed) prefers NAD⁺ as the cofactor." Sequence identities among the isozymes are moderate (54% ZwfB–ZwfC; 60% ZwfA–ZwfC), and cofactor discrimination is governed by residues in the β2–α2 region that contact (or fail to contact) the NADP⁺ 2′-phosphate, analogous to the R72 determinant in *Trypanosoma cruzi* G6PDH. Functionally, the reduced cofactors matter: this dehydrogenase "*provides reduced cofactors, thereby affecting redox balance*" ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). ZwfB's NAD⁺-leaning output makes it a contributor to both NADH- and NADPH-linked redox pools.

### Finding 5 — *zwfB* is cotranscribed with *gnd*, is HexR-independent (constitutive), and is functionally redundant with *zwfA*

The genomic organization of the three paralogs is diagnostic of their distinct regulation ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)):

- ***zwfB*** is cotranscribed with ***gntZ/gnd*** (6-phosphogluconate dehydrogenase) — coupling the first two oxidative-branch dehydrogenases in one transcriptional unit — and is **constitutively expressed**, i.e., not part of the HexR-controlled sugar regulon.
- ***zwfA*** lies in the **HexR-controlled operon *zwfA–pgl–eda***; HexR "*controls the genes that encode glucokinase/glucose 6-phosphate dehydrogenase*" ([PMID: 18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/)), making ZwfA the glucose-inducible, dominant isozyme on glucose/gluconate.
- ***zwfC*** is divergently transcribed relative to a transcriptional regulator and shows near-zero in vivo activity.

Reverse-genetics across the eight *zwf* deletion combinations demonstrated redundancy: single Δ*zwfB* mutants show **no significant growth defect** on glucose, gluconate, or fructose, but the **Δ*zwfAB* double mutant** shows synergistic defects, **fails to grow on ribose**, and the triple Δ*zwfABC* grows ~70% slower on fructose. On gluconate — which bypasses G6PDH entirely by entering downstream at 6-phosphogluconate — only Δ*zwfA* matters, because HexR-driven ZwfA is dominant there. The convergent-pathway context is that "*glucose catabolism in Pseudomonas putida occurs through the simultaneous operation of three pathways that converge at the level of 6-phosphogluconate*" ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)). The overall conclusion is that "G6PDH-A and G6PDH-B carry most of the G6PDH activity in this bacterial species," and are mutually redundant, jointly essential contributors to EDEMP/PP flux.

### Finding 6 — Sequence and AlphaFold structure confirm the canonical G6PD fold with conserved catalytic and dinucleotide-binding motifs

Bioinformatic analysis of the 501-aa Q88FP7 sequence supports the annotation by structure and evolution:

1. **Dinucleotide-binding fingerprint.** The N-terminal glycine-rich fingerprint of the G6PD family is present at residues ~17–23 ("FGANGDLV," a GxxGDLx Rossmann-type motif; InterPro IPR022674 G6PD_NAD-bd / IPR036291 NAD(P)-bd domain superfamily).
2. **Active-site signature.** The strictly conserved G6PD active-site motif "RIDHYLGKE" occurs at residues 186–194 and contains the **catalytic His (H189)**, which acts as the general base abstracting the C1 proton of glucose-6-phosphate, plus a downstream catalytic Lys (InterPro IPR019796 G6P_DH active site).
3. **High-confidence fold.** The AlphaFold model AF-Q88FP7-F1 is high confidence (mean pLDDT = 91.0 across 501 residues; 94% of residues pLDDT > 70, 75.8% > 90) and displays the characteristic bilobal G6PD architecture — an N-terminal Rossmann NAD(P)-binding domain plus a C-terminal β+α domain forming the large antiparallel β-sheet. Pfam PF00479 (G6PD_N) + PF02781 (G6PD_C); eggNOG COG0364.

Together these features independently verify that PP_4042 is a genuine glucose-6-phosphate dehydrogenase rather than a mis-annotated paralog.

---

## Mechanistic Model / Interpretation

*P. putida* KT2440 lacks a functional EMP glycolysis and instead routes the bulk of glucose carbon through the Entner–Doudoroff pathway, embedded in a cyclic "EDEMP" architecture that recycles triose phosphates back to hexose phosphate and net-generates NADPH. G6PDH (Zwf) sits at the **entry to the intracellular phosphorylative branch** and provides the oxidative-PP-branch input to this network. ZwfB is one of the enzymes gating carbon into that cycle.

```
                         Glucose (extracellular)
                             |
          +------------------+------------------+
          |                                     |
   ABC uptake into cytoplasm            Periplasmic gluconate shunt
          |                              (Gcd/Gad -> gluconate,
     glucokinase                         2-ketogluconate)
          |                                     |
     Glucose-6-P (G6P)  <-- EDEMP recycle       |
          |                                     |
  ==> ZwfB / ZwfA / ZwfC  (G6PDH, EC 1.1.1.49)  |
          |   + NAD(P)+ -> NAD(P)H              |
   6-P-glucono-1,5-lactone                      |
          |   (pgl)                             |
          v                                     v
   6-phosphogluconate (6PG)  <-------------------+  <-- convergence node
          |                        |
        Gnd/GntZ                 Edd (ED)
     (6PG dehydrogenase)          |
          |                     KDPG -> Eda
     Ribulose-5-P               |
     (reductive PP)         pyruvate + GAP -> central metabolism
```

**Division of labor among the three isozymes.** The three paralogs are not simple duplicates; they are tuned for different regulatory and redox niches:

| Property | ZwfA (PP_1022) | **ZwfB (PP_4042)** | ZwfC (PP_5351) |
|---|---|---|---|
| Regulation | HexR-induced (glucose) | **Constitutive** | Divergent, minor |
| Operon | *zwfA–pgl–eda* | ***zwfB–gnd/gntZ*** | near a regulator |
| Cofactor φ (NADP⁺/NAD⁺) | ~3.34 (dual) | **~0.86 (dual, NAD⁺-leaning)** | ~2,082 (NADP⁺-specific) |
| In vivo contribution | Major (dominant on glucose/gluconate) | **Major (redundant with ZwfA)** | Negligible |
| Δ single phenotype | defect on gluconate | **none on glucose/gluconate/fructose** | none |

The redundancy is asymmetric and condition-dependent. On **glucose**, ZwfA and ZwfB share the load, so neither single deletion is deleterious, but the double Δ*zwfAB* is synergistically impaired and cannot grow on **ribose**. On **gluconate**, carbon bypasses G6PDH (entering at 6PG), so only the loss of HexR-driven ZwfA is felt. ZwfB's **constitutive expression** provides a baseline of G6PDH activity that is available even when the HexR regulon is not induced, and its cotranscription with *gnd* couples the two consecutive oxidative-branch dehydrogenases. Its **NAD⁺-leaning cofactor preference** diversifies the redox output of the oxidative branch, complementing the NADPH-specialized ZwfC and the dual ZwfA and helping the cell balance NADH and NADPH pools according to demand.

In short: **ZwfB is a constitutive, NAD⁺-preferring, cytoplasmic G6PDH gatekeeper** that, redundantly with ZwfA, initiates oxidation of G6P and feeds 6-phosphogluconate into the ED/EDEMP redox cycle while contributing reduced cofactors to cellular redox balance.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/) | *Cofactor Specificity of G6PDH Isozymes in P. putida…* | **Primary source.** Purified-enzyme kinetics, φ values, cofactor preference, constitutive expression, operon structure, deletion genetics establishing ZwfA/ZwfB redundancy and gatekeeper role. Supports Findings 1, 2, 4, 5. |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through a cycle (ED/EMP/PP)* | ¹³C-flux evidence that ED dominates (~90% via gluconate → 6PG) and the cycle favors NADPH. Supports Finding 3. |
| [17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/) | *Convergent peripheral pathways… genomic and flux analysis* | Establishes the three convergent peripheral routes meeting at 6PG, the cytoplasmic glucose→G6P→6PG branch, and that *zwf* genes encode the G6PDH step. Supports Findings 1, 3, 5. |
| [18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/) | *Activators and repressors control peripheral glucose pathways* | Documents HexR control of the glucokinase/G6PDH (*zwfA*) genes, contrasting with the HexR-independent, constitutive *zwfB*. Supports Finding 5. |
| [36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/) | *G6PDH ZwfA, a dual cofactor-specific isozyme… P. bharatica* | Comparative context: Zwf generates NAD(P)H during G6P→6-phosphogluconolactone, aiding anabolism, energy yield, and oxidative-stress responses — the general physiological role shared by ZwfB. |
| [37454792](https://pubmed.ncbi.nlm.nih.gov/37454792/) | *Time-resolved deuterium fluxomics of sugar processing in P. putida* | Context on the periplasmic gluconate shunt and convergent peripheral pathways yielding 6PG, framing where the ZwfB phosphorylative branch fits. |

**How the evidence coheres:** The enzymatic reaction and pathway placement are supported both by curated annotation (UniProt/HAMAP/KEGG) and by two independent flux-and-genomics studies ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/), [PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). The isozyme-specific properties — cofactor preference, constitutive expression, operon structure, and redundancy — derive from a single but rigorous, purpose-built study that purified each enzyme and built every deletion combination ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). The structural annotation is independently confirmed by conserved sequence motifs and a high-confidence AlphaFold model. No source contradicts the assignment.

---

## Limitations and Knowledge Gaps

1. **Single decisive study for isozyme-specific properties.** The kinetic constants, cofactor preferences, constitutive expression, and deletion phenotypes all trace to one laboratory's work ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). Independent replication of the ZwfB kinetics (especially the φ ≈ 0.86 value and the NAD⁺ preference) would strengthen confidence.
2. **No experimental 3D structure.** Structural inferences rest on an AlphaFold model and conserved-motif analysis, not a crystal or cryo-EM structure of ZwfB. The catalytic His189 and cofactor-discriminating β2–α2 residues are inferred by homology, not observed directly in a ZwfB–ligand complex.
3. **In vivo flux carried specifically by ZwfB is not isolated.** Because ZwfB is redundant with ZwfA, its individual contribution to flux under any given condition has not been quantified directly; only joint (double-mutant) effects reveal its importance.
4. **Oligomeric state and allosteric regulation are unresolved.** UniProt annotates a monomer, but many G6PDHs are dimers/tetramers; the physiological quaternary state of ZwfB and any allosteric regulation (e.g., by NADPH or metabolites) has not been reported.
5. **Localization is inferential.** Cytoplasmic localization is inferred from the intracellular nature of substrate/product and the absence of secretion/membrane signals, not from direct localization experiments.
6. **Regulatory inputs beyond HexR.** ZwfB is described as constitutive/HexR-independent, but whether other regulators or growth conditions modulate *zwfB–gnd* expression remains uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Condition-resolved flux via ZwfB.** Use ¹³C metabolic flux analysis in isogenic Δ*zwfA* (leaving ZwfB as the sole major isozyme) versus wild type across glucose, fructose, and ribose to quantify the flux specifically carried by ZwfB and confirm its NAD⁺-linked output in vivo.
2. **Structural determination.** Solve a crystal or cryo-EM structure of ZwfB with G6P and NAD⁺/NADP⁺ to directly visualize H189 catalysis and the β2–α2 cofactor-discrimination determinants; test predicted 2′-phosphate-contacting residues by site-directed mutagenesis to interconvert cofactor preference.
3. **Redox-pool measurements.** Quantify NADH/NAD⁺ and NADPH/NADP⁺ ratios in Δ*zwfB*, Δ*zwfA*, and Δ*zwfAB* strains to test the model that ZwfB diversifies the redox output of the oxidative branch, particularly under oxidative stress.
4. **Promoter/transcriptional analysis.** Map the *zwfB–gnd* transcript and promoter, verify constitutivity across carbon sources and stress conditions, and screen for regulators beyond HexR.
5. **Oligomeric-state characterization.** Use size-exclusion chromatography–MALS and analytical ultracentrifugation on purified ZwfB to resolve its quaternary structure and test for cofactor-dependent oligomerization or allosteric inhibition by NADPH.
6. **Stress-phenotype tests.** Challenge Δ*zwfB* and Δ*zwfAB* strains with oxidative agents (e.g., H₂O₂, paraquat) to determine whether ZwfB's NAD(P)H supply contributes measurably to oxidative-stress resistance, as suggested by the general Zwf physiology ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)).

---

*Report generated from a 5-iteration autonomous investigation. Target identity (zwfB / PP_4042 / Q88FP7 / P. putida KT2440) verified against all provided UniProt, InterPro, and Pfam identifiers and against primary literature; no gene-symbol ambiguity was found.*


## Artifacts

- [OpenScientist final report](zwfB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](zwfB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33727391
2. PMID:26350459
3. PMID:17483213
4. PMID:18245293
5. PMID:36354357