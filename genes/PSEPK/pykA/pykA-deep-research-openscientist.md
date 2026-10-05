---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T01:51:33.447204'
end_time: '2026-08-11T02:14:22.854763'
duration_seconds: 1369.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pykA
  gene_symbol: pykA
  uniprot_accession: Q88N54
  protein_description: 'RecName: Full=Pyruvate kinase {ECO:0000256|ARBA:ARBA00012142,
    ECO:0000256|NCBIfam:TIGR01064}; EC=2.7.1.40 {ECO:0000256|ARBA:ARBA00012142, ECO:0000256|NCBIfam:TIGR01064};'
  gene_info: Name=pykA {ECO:0000313|EMBL:AAN66985.1}; OrderedLocusNames=PP_1362 {ECO:0000313|EMBL:AAN66985.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the pyruvate kinase family.
  protein_domains: Pyr_Knase. (IPR001697); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813);
    Pyrv_kinase-like_dom_sf. (IPR040442); Pyrv_Knase-like_insert_dom_sf. (IPR011037);
    Pyrv_Knase_AS. (IPR018209)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pykA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pykA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N54
- **Protein Description:** RecName: Full=Pyruvate kinase {ECO:0000256|ARBA:ARBA00012142, ECO:0000256|NCBIfam:TIGR01064}; EC=2.7.1.40 {ECO:0000256|ARBA:ARBA00012142, ECO:0000256|NCBIfam:TIGR01064};
- **Gene Information:** Name=pykA {ECO:0000313|EMBL:AAN66985.1}; OrderedLocusNames=PP_1362 {ECO:0000313|EMBL:AAN66985.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the pyruvate kinase family.
- **Key Domains:** Pyr_Knase. (IPR001697); Pyrv/PenolPyrv_kinase-like_dom. (IPR015813); Pyrv_kinase-like_dom_sf. (IPR040442); Pyrv_Knase-like_insert_dom_sf. (IPR011037); Pyrv_Knase_AS. (IPR018209)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pykA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pykA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pykA** (gene ID: pykA, UniProt: Q88N54) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pykA* (PP_1362 / UniProt Q88N54) — Pyruvate Kinase of *Pseudomonas putida* KT2440

## Summary

**pykA** (ordered locus **PP_1362**; UniProt accession **Q88N54**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a **cytoplasmic pyruvate kinase (EC 2.7.1.40)**, the enzyme that catalyzes the final, essentially irreversible step of the lower glycolytic pathway: the transfer of the high-energy phosphoryl group from **phosphoenolpyruvate (PEP)** to **ADP**, yielding **pyruvate** and **ATP**. This is a substrate-level phosphorylation reaction and requires the obligatory monovalent (**K⁺**) and divalent (**Mg²⁺**) metal cofactors characteristic of the pyruvate kinase family. The identification is unambiguous: the 484-amino-acid protein carries the two canonical pyruvate kinase domains (an N-terminal TIM-barrel catalytic domain and a C-terminal regulatory/allosteric domain) and the Pyr_Knase InterPro signatures listed in the target definition, and it is one of exactly two EC 2.7.1.40 enzymes encoded by KT2440. The gene symbol, EC number, protein family, domain architecture, and organism are all mutually consistent — **there is no ambiguity in the identity of this target**.

Functionally, PykA sits at the **PEP–pyruvate metabolic node**, the branch point that connects the lower/shared reactions of glucose catabolism to the tricarboxylic acid (TCA) cycle. In *P. putida* KT2440, glucose is degraded predominantly through the **Entner–Doudoroff pathway (EDP)** rather than classical Embden–Meyerhof–Parnas glycolysis, because KT2440 lacks a functional glycolytic phosphofructokinase. The triose-phosphate branch produced by the Edd/Eda enzymes is oxidized through the lower glycolytic reactions to PEP, which PykA then converts to pyruvate. In this architecture pyruvate kinase acts as a principal **flux-controlling "pacemaker,"** governing how carbon and energy are partitioned between catabolism (feeding acetyl-CoA into the TCA cycle) and anabolism (PEP-derived biosynthetic precursors).

Because no experimental crystal structure or detailed enzymology exists for the *P. putida* protein itself, the finer mechanistic and regulatory properties are inferred from its very close ortholog in *Pseudomonas aeruginosa* (PykA, UniProt Q9HW72), which shares **84% amino-acid identity** and has been biochemically and structurally characterized. That ortholog is a homotetramer displaying **K-type allosteric activation by glucose-6-phosphate and pentose-phosphate-pathway intermediates**, with a distinct allosteric effector pocket resolved at 2.4 Å. The high conservation of both the catalytic (85% identity) and the C-terminal regulatory (83% identity) domains between the two proteins provides strong evolutionary evidence that *P. putida* PykA operates by the same feed-forward-activated mechanism. The enzyme is a soluble cytosolic protein with no signal peptide, transmembrane segment, or secretion signal.

---

## Identity Verification

Before research, the target was verified against multiple congruent lines of evidence:

- **UniProt Q88N54** annotates the protein as *Pyruvate kinase* (EC 2.7.1.40), gene *pykA*, ordered locus **PP_1362**, in *Pseudomonas putida* strain KT2440.
- The sequence is **484 aa** and contains the two canonical pyruvate-kinase domains: a **pyruvate kinase TIM-barrel** (residues ~3–329) and a **PK C-terminal regulatory domain** (~361–476).
- The InterPro domains listed in the request (Pyr_Knase IPR001697; Pyrv/PEP-kinase domain IPR015813; PK-like domain superfamily IPR040442; PK insert domain IPR011037; PK active-site IPR018209) are the hallmark signatures of the pyruvate kinase family.

**Conclusion:** the symbol, family, domains, EC number, and organism are all consistent. This is a genuine, correctly identified pyruvate kinase.

---

## Key Findings

### F001 — PykA is a bona fide pyruvate kinase (EC 2.7.1.40)

UniProt Q88N54 annotates PP_1362 as a 484-amino-acid pyruvate kinase catalyzing the reaction **phosphoenolpyruvate + ADP + H⁺ → pyruvate + ATP**, with K⁺ as an activating cofactor. The protein contains the two hallmark pyruvate kinase modules: the N-terminal **pyruvate kinase (TIM) barrel** (approximately residues 3–329) that houses the active site, and the C-terminal **PK regulatory domain** (approximately residues 361–476). The enzyme is assigned to glycolysis as the terminal (fifth of five) step producing pyruvate from D-glyceraldehyde-3-phosphate.

Crucially, this annotation is backed by direct experimental evidence in a *P. putida* strain. In the solvent-tolerant strain *P. putida* S12, a mutation in the *pykA* gene decreased in-vitro pyruvate kinase activity, consistent with a reduced metabolic flux from phosphoenolpyruvate to pyruvate ([PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)). This moves the assignment beyond pure sequence-based inference, linking the *pykA* gene directly to measurable pyruvate kinase enzymatic activity and to the PEP→pyruvate conversion in *Pseudomonas putida*.

> *"A mutation in the pykA gene decreased in vitro pyruvate kinase activity, which is consistent with a lower flux from phosphoenolpyruvate to pyruvate."* — Wierckx et al., [PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)

### F002 — PykA operates at the PEP–pyruvate node connecting Entner–Doudoroff glycolysis to the TCA cycle

*P. putida* KT2440 catabolizes glucose primarily via the Entner–Doudoroff pathway because it lacks a functional glycolytic phosphofructokinase; the lower/shared reactions funnel triose phosphates onward to PEP and then to pyruvate. Metabolic flux analysis of the closely related *P. putida* S12 demonstrated that reduced pyruvate kinase (*pykA*) activity **redistributes carbon flux**, lowering PEP→pyruvate conversion and increasing PEP availability for anabolic (gluconeogenic/biosynthetic) routes. Specifically, gluconeogenic formation of glucose-6-phosphate from triose-3-phosphate was abolished in favor of increased PEP production when pyruvate kinase flux was constrained ([PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)). This positions PykA as a control valve at the PEP–pyruvate branch point rather than a passive downstream step.

> *"Gluconeogenic formation of glucose-6-phosphate from triose-3-phosphate was abolished, in favour of increased phosphoenolpyruvate production."* — [PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)

The transcription factor **HexR** is the master regulator of this glycolytic/pyruvate node in KT2440, coordinating expression of central-carbon genes in response to metabolic state ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)).

### F003 — PykA is predicted to be a homotetramer under K-type allosteric activation by glucose-6-phosphate / PPP intermediates

The *P. putida* protein (Q88N54, 484 aa) shares **84.4% amino-acid identity** (405/480 aligned positions by global Needleman–Wunsch alignment) with the biochemically and structurally characterized *P. aeruginosa* PykA (Q9HW72, 483 aa). For that ortholog, enzyme-kinetics assays revealed potent **K-type allosteric activation by glucose-6-phosphate and by pentose-phosphate-pathway intermediates**, and a 2.4 Å X-ray structure revealed a distinct allosteric G6P-binding pocket ([PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)). In that organism PykA is the dominant PK isoform and the main "pacemaker" of the Entner–Doudoroff pathway. Given the very high identity, *P. putida* PykA is predicted to assemble as a **homotetramer** (the canonical bacterial pyruvate kinase quaternary state) and to be regulated by the same feed-forward activators.

> *"Enzyme kinetics assays revealed that PykA displays potent K-type allosteric activation by glucose 6-phosphate and by intermediates from the pentose phosphate pathway."* — Abdelhamid et al., [PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)

> *"Pyruvate kinase (PK) is the main 'pacemaker' of the EDP, and its activity is also relevant for P. aeruginosa virulence."* — [PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)

The K-type mechanism — in which activators lower the apparent Kₘ / S₀.₅ for substrate rather than raising Vmax — is consistent with the broader pyruvate kinase literature, where allosteric effectors and the K⁺ cofactor tune substrate affinity and active-site closure ([PMID: 16147999](https://pubmed.ncbi.nlm.nih.gov/16147999/)).

### F004 — PykA functions in the cytoplasm

UniProt Q88N54 lists **no signal peptide, no transmembrane region, and no membrane/secretion keywords**; its keyword set is limited to ATP-binding, Glycolysis, Kinase, Magnesium, Metal-binding, Nucleotide-binding, Pyruvate, and Transferase. Pyruvate kinases across bacteria are soluble cytosolic enzymes, and the 84%-identical *P. aeruginosa* ortholog was purified as a soluble protein and crystallized ([PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)). PykA therefore carries out its function in the **cytoplasm**, where its substrates (PEP, ADP) and cofactors (K⁺, Mg²⁺) reside.

### F005 — KT2440 has two PK isozymes; PP_1362 is the PykA-type ortholog

Enumeration of EC 2.7.1.40 in *P. putida* KT2440 returns exactly two genes: **pykA/PP_1362** (Q88N54, 484 aa) and **pyk/PP_4301** (Q88EZ9, 471 aa; the PykF-type isozyme). Global-alignment identities unambiguously assign PP_1362 to the PykA subfamily:

| Comparison | Identity | Interpretation |
|---|---|---|
| PP_1362 vs *P. aeruginosa* PykA (Q9HW72) | **84.4%** | Same subfamily; closest characterized ortholog |
| PP_1362 vs *E. coli* PykA (P21599) | 64.3% | PykA subfamily |
| PP_1362 vs *E. coli* PykF (P0AD61) | 48.1% | Distinct (PykF) subfamily |

The distribution of identities places PP_1362 firmly in the **PykA subfamily** and distinguishes it from the second KT2440 isozyme, PP_4301 (PykF-type). This matters mechanistically because PykA-subfamily and PykF-subfamily enzymes typically differ in their allosteric regulators.

### F006 — PykA acts downstream of the Entner–Doudoroff pathway that dominates glucose catabolism

Combined genomic and ¹³C-flux analysis established that glucose catabolism in *P. putida* KT2440 proceeds via **three convergent peripheral pathways** that meet at 6-phosphogluconate, which is processed by the Edd and Eda Entner–Doudoroff enzymes into the central metabolites pyruvate and glyceraldehyde-3-phosphate ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)). The glyceraldehyde-3-phosphate branch is oxidized through lower glycolysis to PEP, and PykA (PP_1362) catalyzes the terminal PEP→pyruvate step. TCA anaplerosis in KT2440 relies heavily on a pyruvate shunt, further underscoring the centrality of the pyruvate pool that PykA helps generate.

> *"glucose catabolism in Pseudomonas putida occurs through the simultaneous operation of three pathways that converge at the level of 6-phosphogluconate, which is metabolized by the Edd and Eda Entner/Doudoroff enzymes to central metabolites"* — del Castillo et al., [PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)

### F007 — The regulatory C-terminal domain is highly conserved, supporting shared G6P activation

Domain-resolved global alignment of *P. putida* PykA (Q88N54) against *P. aeruginosa* PykA (Q9HW72) shows high conservation of both functional modules:

| Domain | Residue range | Identity |
|---|---|---|
| Catalytic TIM-barrel domain | aa 3–329 | **85.0%** (277/326) |
| C-terminal regulatory/allosteric domain | aa 361–476 | **83.3%** (95/114) |

The C-terminal domain is where the allosteric effector-binding site resides in pyruvate kinases. Its strong conservation (83% identity) relative to the *P. aeruginosa* ortholog — which is K-type activated by glucose-6-phosphate/PPP intermediates via a defined allosteric pocket ([PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)) — provides structural-evolutionary evidence that *P. putida* PykA retains the same feed-forward activation. Conservation of the catalytic barrel likewise supports identical substrate chemistry.

---

## Mechanistic Model / Interpretation

### The reaction catalyzed

```
   Phosphoenolpyruvate (PEP)  +  ADP  +  H⁺
                    │
                    │   PykA (EC 2.7.1.40)
                    │   cofactors: K⁺ (monovalent), Mg²⁺ (divalent)
                    ▼
        Pyruvate  +  ATP        (substrate-level phosphorylation)
```

PykA transfers the phosphoryl group from PEP — the highest-energy phosphate donor in central metabolism — to ADP, generating ATP and pyruvate. The reaction is essentially irreversible under physiological conditions and constitutes one of the pathway's principal ATP-yielding steps. K⁺ is an obligatory activator that promotes closure of the active site and independent (random) binding of the two substrates; without it the mechanism becomes ordered and Vmax collapses by roughly two orders of magnitude, a general property of the enzyme family ([PMID: 16147999](https://pubmed.ncbi.nlm.nih.gov/16147999/)). Two-Mg²⁺-assisted phosphoryl transfer, with pyruvate release preceding ADP binding, has been demonstrated kinetically for pyruvate kinases ([PMID: 4850216](https://pubmed.ncbi.nlm.nih.gov/4850216/)).

### Position in the metabolic network

```
   Glucose
     │  (three convergent peripheral pathways)
     ▼
  6-Phosphogluconate ──Edd/Eda (Entner–Doudoroff)──► Pyruvate + Glyceraldehyde-3-P
                                                              │
                                          lower glycolysis    │
                                                              ▼
                                                    Phosphoenolpyruvate (PEP)
                                                              │
                        Glucose-6-P / PPP intermediates ═════►│  (K-type allosteric
                                                              │   feed-forward activation)
                                                        ┌─────┴─────┐  PykA (PP_1362)
                                                        ▼
                                                    Pyruvate + ATP
                                                        │
                                                        ▼
                                              Acetyl-CoA ► TCA cycle
```

PykA occupies the **PEP–pyruvate node**, the key branch point of *P. putida* central metabolism. The enzyme's allosteric activation by glucose-6-phosphate and pentose-phosphate-pathway intermediates constitutes a **feed-forward loop**: when upstream sugar-phosphate pools are high (i.e., carbon is abundant), the activators build up and switch on pyruvate kinase, accelerating conversion of PEP to pyruvate and pulling carbon into the TCA cycle for energy generation. When upstream flux is low, PykA activity drops, sparing PEP for gluconeogenic and biosynthetic routes — precisely the flux redistribution observed experimentally in *P. putida* S12 when *pykA* activity was reduced ([PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)). Because PEP is a high-value branch-point metabolite (used for gluconeogenesis, anaplerosis, aromatic amino-acid biosynthesis and the PTS), PykA activity effectively governs the split of carbon between catabolic pyruvate/ATP generation and PEP-conserving anabolic demands — a property directly exploited in metabolic engineering of *P. putida*.

### Two isozymes, divided labor

KT2440 encodes two pyruvate kinases. PP_1362 (**PykA**-type) is the subject of this report and, by analogy to *P. aeruginosa*, is expected to be the dominant EDP pacemaker regulated by G6P/PPP intermediates. PP_4301 (**PykF**-type, Q88EZ9) is a separate isozyme that in other bacteria typically responds to a different allosteric activator (classically fructose-1,6-bisphosphate). The presence of two isozymes with distinct regulatory inputs is a recurring theme of metabolic robustness in KT2440, paralleling the dual isocitrate dehydrogenases ([PMID: 42464328](https://pubmed.ncbi.nlm.nih.gov/42464328/)) and the dual glucose-6-phosphate dehydrogenases ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)) that give this organism its noted metabolic flexibility.

### Localization

All evidence — the absence of any targeting/secretion signal in Q88N54, the universal cytosolic character of bacterial pyruvate kinases, and the successful purification/crystallization of the soluble *P. aeruginosa* ortholog — points to PykA functioning as a **soluble cytoplasmic enzyme**.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/) | *Metabolic flux analysis of a phenol-producing mutant of P. putida S12* | **Primary experimental support.** A *pykA* mutation lowered in-vitro PK activity and reduced PEP→pyruvate flux, redistributing carbon toward PEP/anabolism (F001, F002). |
| [31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/) | *Evolutionary plasticity in the allosteric regulator-binding site of pyruvate kinase isoform PykA* (P. aeruginosa) | **Closest characterized ortholog (84% identity).** Defines K-type allosteric activation by G6P/PPP intermediates, the "pacemaker" role of PK in the EDP, and provides a 2.4 Å structure with an allosteric pocket (F003, F004, F007). |
| [17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/) | *Convergent peripheral pathways catalyze initial glucose catabolism in P. putida* | Establishes the Entner–Doudoroff-dominated architecture whose lower branch produces the PEP substrate PykA consumes (F006). |
| [41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/) | *Redefining HexR regulatory landscape in P. putida KT2440* | Identifies HexR as the master transcriptional regulator of the glycolytic/pyruvate node in which PykA participates (F002). |
| [16147999](https://pubmed.ncbi.nlm.nih.gov/16147999/) | *Pyruvate kinase revisited: the activating effect of K⁺* | Mechanistic basis for the obligatory K⁺ cofactor and active-site closure common to the family (reaction mechanism). |
| [4850216](https://pubmed.ncbi.nlm.nih.gov/4850216/) | *A kinetic study of pig-liver pyruvate kinase* | Family precedent for the two-Mg²⁺ phosphoryl-transfer mechanism and product-release order (reaction mechanism). |
| [34867929](https://pubmed.ncbi.nlm.nih.gov/34867929/) | *Structure, Function and Regulation of a Second Pyruvate Kinase Isozyme* (Pseudomonas) | Context for the two-isozyme (PykA/PykF) system in Pseudomonas (F005). |
| [42464328](https://pubmed.ncbi.nlm.nih.gov/42464328/) | *Functional redundancy driven by isocitrate dehydrogenase in KT2440* | Parallel example of dual-isozyme metabolic robustness in KT2440 (interpretation). |
| [33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/) | *Cofactor specificity of G6PDH isozymes in P. putida* | Parallel dual-isozyme system feeding the EDP/PPP branch point (interpretation). |

**How the evidence coheres:** The identity of PykA rests on a convergence of (i) direct sequence/domain annotation from UniProt, (ii) direct experimental enzymology in a *P. putida* strain ([PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)), (iii) very high identity to a fully characterized *Pseudomonas* ortholog ([PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)), and (iv) an established metabolic context ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)). No source contradicts the assignment.

---

## Supported and Refuted Hypotheses

**Supported:**
- PP_1362/Q88N54 is a genuine pyruvate kinase catalyzing PEP + ADP → pyruvate + ATP (UniProt annotation + direct in-vitro activity evidence in *P. putida*, [PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/); conserved catalytic domains).
- The enzyme is cytoplasmic and metal-dependent (K⁺/Mg²⁺).
- PP_1362 is the PykA-subfamily isozyme (84% identity to *P. aeruginosa* PykA; two-isozyme genome architecture).
- PykA functions downstream of the Entner–Doudoroff pathway at the PEP–pyruvate node and controls PEP/pyruvate flux partitioning ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/); [PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)).
- Predicted allosteric activation by glucose-6-phosphate / PPP intermediates (homology to [PMID: 31484721](https://pubmed.ncbi.nlm.nih.gov/31484721/)).

**Not established / open:**
- Direct kinetic constants (Kₘ for PEP/ADP, S₀.₅, Hill coefficient) and the specific allosteric effector profile of the **KT2440** PykA protein have not been measured directly; these are inferred from the *P. aeruginosa* ortholog.
- No experimental 3-D structure of the KT2440 protein exists (only the close *P. aeruginosa* ortholog).

---

## Limitations and Knowledge Gaps

1. **No direct structure or enzymology for the *P. putida* KT2440 protein.** The homotetramer assembly, K-type activation, and G6P/PPP effector specificity are **inferred by orthology** from *P. aeruginosa* PykA (84% identity), not measured for Q88N54 itself. The 16% sequence divergence, though modest, includes the allosteric-pocket region and could in principle alter effector affinities or specificity — indeed the characterized ortholog's study was explicitly framed around "evolutionary plasticity" of that binding site.

2. **The one direct experiment was in strain S12, not KT2440.** *P. putida* S12 is a closely related solvent-tolerant strain; the *pykA* activity/flux result ([PMID: 19560494](https://pubmed.ncbi.nlm.nih.gov/19560494/)) is highly relevant but was obtained in a different genetic background and via metabolic-flux inference rather than purified-enzyme kinetics.

3. **Division of labor between the two isozymes is not experimentally resolved in KT2440.** Which isozyme (PP_1362 vs PP_4301) carries the dominant in-vivo flux under a given carbon source, and whether they are differentially regulated (e.g., by HexR or by distinct effectors), remains to be measured directly.

4. **Physiological effector concentrations and kinetic constants** (Kₘ for PEP and ADP, S₀.₅ shifts on activation, Hill coefficients, kcat) are unknown for the *P. putida* enzyme.

5. **Regulatory integration** with the HexR regulon and with the pyruvate shunt/anaplerotic network is described at a systems level but not dissected specifically for *pykA*.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Overexpress and purify His-tagged Q88N54 from *E. coli* and determine Kₘ(PEP), Kₘ(ADP), kcat, the K⁺/Mg²⁺ dependence, and Hill coefficients — directly confirming EC 2.7.1.40 activity for the KT2440 protein.

2. **Allosteric-effector screen.** Test glucose-6-phosphate, 6-phosphogluconate, and PPP intermediates (ribose-5-P, fructose-6-P), plus fructose-1,6-bisphosphate and AMP, as candidate activators, quantifying the K-type shift in S₀.₅(PEP) to verify that the *P. putida* enzyme shares the *P. aeruginosa* feed-forward regulation.

3. **Quaternary-structure determination.** Use SEC-MALS to confirm the homotetramer, and pursue an X-ray, cryo-EM, or AlphaFold model of Q88N54 with and without G6P to map its allosteric pocket directly.

4. **Isozyme knockout / flux study in KT2440.** Construct single (ΔPP_1362, ΔPP_4301) and double deletion mutants and perform ¹³C-metabolic flux analysis on glucose, glycerol, and gluconeogenic substrates to establish the in-vivo contribution and condition-dependence of each PK isozyme.

5. **Regulatory mapping.** Test whether *pykA* (PP_1362) expression is within the HexR regulon using available ChIP-exo / RNA-seq datasets ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)) to connect transcriptional control to the allosteric layer.

---

## Conclusion

**pykA (PP_1362, UniProt Q88N54)** encodes the cytoplasmic pyruvate kinase of *Pseudomonas putida* KT2440 — a K⁺/Mg²⁺-dependent enzyme (EC 2.7.1.40) that catalyzes the terminal, ATP-generating step of the lower glycolytic pathway, converting phosphoenolpyruvate + ADP to pyruvate + ATP. It is a PykA-subfamily isozyme (one of two PKs in KT2440) that acts as the flux-controlling pacemaker at the PEP–pyruvate node downstream of the dominant Entner–Doudoroff pathway, and is predicted — by 84% identity to the structurally characterized *P. aeruginosa* ortholog — to function as a homotetramer under feed-forward K-type allosteric activation by glucose-6-phosphate and pentose-phosphate-pathway intermediates.


## Artifacts

- [OpenScientist final report](pykA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pykA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19560494
2. PMID:41260329
3. PMID:31484721
4. PMID:16147999
5. PMID:17483213
6. PMID:4850216
7. PMID:42464328
8. PMID:33727391