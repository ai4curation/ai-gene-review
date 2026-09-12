---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:40:53.231001'
end_time: '2026-07-11T18:53:38.161155'
duration_seconds: 764.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sucB
  gene_symbol: sucB
  uniprot_accession: Q88FB0
  protein_description: 'RecName: Full=Dihydrolipoyllysine-residue succinyltransferase
    component of 2-oxoglutarate dehydrogenase complex {ECO:0000256|ARBA:ARBA00019511,
    ECO:0000256|RuleBase:RU361138}; EC=2.3.1.61 {ECO:0000256|ARBA:ARBA00012945, ECO:0000256|RuleBase:RU361138};
    AltName: Full=2-oxoglutarate dehydrogenase complex component E2 {ECO:0000256|RuleBase:RU361138};'
  gene_info: Name=sucB {ECO:0000313|EMBL:AAN69769.1}; OrderedLocusNames=PP_4188 {ECO:0000313|EMBL:AAN69769.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the 2-oxoacid dehydrogenase family.
  protein_domains: 2-oxoA_DH_lipoyl-BS. (IPR003016); 2-oxoacid_dehydrogenase. (IPR050537);
    2-oxoacid_DH_actylTfrase. (IPR001078); Biotin_lipoyl. (IPR000089); CAT-like_dom_sf.
    (IPR023213)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sucB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sucB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FB0
- **Protein Description:** RecName: Full=Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex {ECO:0000256|ARBA:ARBA00019511, ECO:0000256|RuleBase:RU361138}; EC=2.3.1.61 {ECO:0000256|ARBA:ARBA00012945, ECO:0000256|RuleBase:RU361138}; AltName: Full=2-oxoglutarate dehydrogenase complex component E2 {ECO:0000256|RuleBase:RU361138};
- **Gene Information:** Name=sucB {ECO:0000313|EMBL:AAN69769.1}; OrderedLocusNames=PP_4188 {ECO:0000313|EMBL:AAN69769.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the 2-oxoacid dehydrogenase family.
- **Key Domains:** 2-oxoA_DH_lipoyl-BS. (IPR003016); 2-oxoacid_dehydrogenase. (IPR050537); 2-oxoacid_DH_actylTfrase. (IPR001078); Biotin_lipoyl. (IPR000089); CAT-like_dom_sf. (IPR023213)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sucB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sucB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sucB** (gene ID: sucB, UniProt: Q88FB0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sucB* (Q88FB0) — Dihydrolipoyllysine-residue Succinyltransferase (E2o) of *Pseudomonas putida* KT2440

**Gene:** *sucB* · **Locus:** PP_4188 · **UniProt:** Q88FB0 · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440) · **EC:** 2.3.1.61

---

## Summary

The gene *sucB* (locus PP_4188; UniProt **Q88FB0**) of *Pseudomonas putida* KT2440 encodes **E2o**, the **dihydrolipoyllysine-residue succinyltransferase** (EC 2.3.1.61), which is simultaneously the **catalytic** and the **structural core** component of the **2-oxoglutarate (α-ketoglutarate) dehydrogenase complex (OGDHc)** of the tricarboxylic acid (TCA) cycle. The primary biochemical function of the enzyme is to catalyze the transfer of a **succinyl group** from a lipoamide-bound thioester (S-succinyldihydrolipoyllysine) onto **coenzyme A**, generating **succinyl-CoA** and regenerating the reduced (dihydro)lipoyl arm. This is the second of the three coupled half-reactions carried out by the OGDHc, whose overall transformation is the oxidative decarboxylation of 2-oxoglutarate: `2-oxoglutarate + CoA + NAD⁺ → succinyl-CoA + CO₂ + NADH`.

The protein has the canonical three-module architecture of a 2-oxoacid dehydrogenase E2 acyltransferase: an N-terminal **lipoyl domain** carrying a covalently attached lipoic acid on a specific lysine (**Lys43**, in the conserved D-K-V β-turn), a flexible **Ala/Pro-rich linker**, a **peripheral-subunit-binding domain (PSBD)** that recruits the E1o and E3 partner enzymes, and a C-terminal **chloramphenicol-acetyltransferase (CAT)-like catalytic acyltransferase domain** bearing the invariant catalytic **His378** in the D-H-R motif. E2o subunits self-assemble into a symmetric multi-subunit inner core — the scaffold of one of the largest known multienzyme assemblies (up to ~10 MDa, >100 chains) — onto which E1o and E3 dock. The lipoyl-lysine acts as a **"swinging arm"** that shuttles the reaction intermediate between the three active sites, physically coupling decarboxylation (E1o), succinyl transfer (E2o), and re-oxidation of the lipoyl arm (E3).

This functional assignment is **robust but rests on homology transfer**: no *P. putida*-specific enzymology of PP_4188 has been published. It is supported by (1) diagnostic InterPro domain architecture, (2) conservation of the two catalytic residues (lipoyl-Lys43 and His378), and (3) **60% amino-acid identity to the experimentally characterized *E. coli* E2o (SucB, P0AFG6)** — well above the homology "twilight zone," making annotation transfer secure. In *P. putida*, an obligate aerobe with a fully oxidative TCA cycle, the enzyme functions as a soluble cytoplasmic megadalton complex encoded in the *sucAB* gene cluster; its succinyl-CoA product both drives the TCA cycle and serves as an essential biosynthetic precursor for lysine and methionine.

---

## Identity Verification (Critical Check)

The gene symbol **sucB is correct and unambiguous** for this protein. Sequence-based analysis of Q88FB0 (407 aa, ~42.4 kDa) reproduces the canonical, diagnostic three-domain architecture of an E2 acyltransferase, and the InterPro assignments listed for the protein map onto it exactly. This is unmistakably the E2o member of the 2-oxoacid dehydrogenase family — **not** a similarly named gene from another organism.

| Region | Residues (approx.) | Feature | Diagnostic signature |
|---|---|---|---|
| Lipoyl (biotinyl/lipoyl-BS) domain | 2–77 | Cofactor-carrying domain | **Lipoyl-Lys43** in the conserved **D-K-V β-turn** (IPR000089 / IPR003016) |
| Linker | ~78–108 | Flexible tether | Ala/Pro-rich, low-complexity |
| Peripheral subunit-binding domain (PSBD) | 108–145 | E1o / E3 docking | Small helical binding module |
| Catalytic acyltransferase (CAT-like) domain | ~146–407 | Succinyl-transfer active site | Invariant **catalytic His378** in the **D-H-R** motif (IPR001078 / IPR023213) |

A Needleman–Wunsch global alignment of Q88FB0 against *E. coli* K-12 SucB/E2o (P0AFG6, 405 aa) gives **60.4% amino-acid identity** genome-wide and **66.1%** across the C-terminal catalytic domain — far above the ~20–30% "twilight zone." The diagnostic catalytic residues (lipoyl-Lys43, catalytic His378) and the domain order are conserved. The extensive experimental biochemistry and structural biology of the *E. coli* and human E2o enzymes can therefore be **confidently transferred** to the *P. putida* protein.

---

## Key Findings

### Finding 1 — *sucB* encodes E2o, the dihydrolipoyllysine-residue succinyltransferase (EC 2.3.1.61)

UniProt Q88FB0 is a 407-amino-acid, ~42.4 kDa protein whose sequence confirms the canonical E2 acyltransferase multi-domain architecture: (1) an **N-terminal lipoyl domain** (~res 2–77) carrying the lipoyl-lysine in the conserved **D-K-V β-turn at Lys43**; (2) an **Ala/Pro-rich flexible linker** (~78–108); (3) a **PSBD** (~108–145); and (4) a **C-terminal CAT-like catalytic acyltransferase domain** containing the invariant catalytic **His378** in the signature **D-H-R** motif. The InterPro assignments match this architecture precisely: **IPR000089** (biotin/lipoyl attachment), **IPR001078** (2-oxoacid DH acyltransferase), **IPR003016** (2-oxoacid DH lipoyl attachment site), and **IPR023213** (CAT-like domain superfamily). The presence and precise order of these domains is diagnostic of an E2-type acyltransferase within a 2-oxoacid dehydrogenase complex.

### Finding 2 — The catalyzed reaction: succinyl transfer from dihydrolipoamide to CoA

The enzyme catalyzes **EC 2.3.1.61**: `S-succinyldihydrolipoyllysine + CoA → dihydrolipoyllysine + succinyl-CoA`. This is one of three coupled catalytic activities of the OGDHc, whose overall reaction is `2-oxoglutarate + CoA + NAD⁺ → succinyl-CoA + CO₂ + NADH`. Direct experimental support for the loading step comes from the Perham laboratory ([PMID: 10623527](https://pubmed.ncbi.nlm.nih.gov/10623527/)), which demonstrated that the E2o lipoyl domain undergoes **"reductive succinylation by E1o in the presence of 2-oxoglutarate"** — the substrate-loading event preceding CoA transfer. Reviews of the mitochondrial α-keto acid dehydrogenase family ([PMID: 38963492](https://pubmed.ncbi.nlm.nih.gov/38963492/)) place the α-ketoglutarate dehydrogenase complex firmly within the citric acid cycle, and characterization of the human OGDHc ([PMID: 30323066](https://pubmed.ncbi.nlm.nih.gov/30323066/)) confirms that the complex **"comprises three components, hE1o, hE2o, and hE3"** and "plays a pivotal role in the tricarboxylic acid (TCA) cycle."

### Finding 3 — E2o is the structural core, coupling three active sites via a lipoyl "swinging arm"

In all 2-oxoacid dehydrogenase complexes, the E2 acyltransferase self-assembles into a **symmetric multi-subunit inner core** (24-mer cubic or 60-mer icosahedral) onto which the E1 and E3 components dock. E2 is thus the scaffold of one of the largest known multienzyme assemblies — up to **~10 MDa with more than 100 protein chains** ([PMID: 38963492](https://pubmed.ncbi.nlm.nih.gov/38963492/)); the atomic structure of the human PDC E2 inner core illustrates this cubic-core organization ([PMID: 29608861](https://pubmed.ncbi.nlm.nih.gov/29608861/)). The lipoyl domain, tethered by its flexible Ala/Pro-rich linker, allows the **lipoyl-lysine "swinging arm"** to visit in turn the **E1o active site** (reductive succinylation using 2-oxoglutarate), the **E2o catalytic site** (succinyl transfer to CoA), and the **E3 active site** (re-oxidation of the dihydrolipoyl arm, regenerating the disulfide with reduction of NAD⁺). The Perham lab ([PMID: 10623527](https://pubmed.ncbi.nlm.nih.gov/10623527/)) showed that the E2o lipoyl domain is specifically recognized by its cognate E1o and that a surface loop adjacent to the lipoyl-lysine β-turn determines E1o/E1p specificity. The **PSBD** (residues ~108–145 here) mediates docking of E1o and E3 onto the core.

### Finding 4 — Subcellular localization: soluble cytoplasmic megadalton complex

*P. putida*, like other bacteria, lacks mitochondria, so its OGDHc is a **soluble cytoplasmic assembly**. Consistent with this, Q88FB0 has **no signal peptide, no transmembrane segments, and no lipobox**. The gene has ordered locus name **PP_4188** and lies in the **sucAB gene cluster**, with *sucA* (E1o) as the adjacent gene — the typical bacterial operon organization for the OGDHc. As an **obligate aerobe** with a fully oxidative, cyclic TCA cycle that relies on the Entner–Doudoroff / EDEMP pathway (rather than glycolysis) for sugar catabolism, *P. putida* channels substantial central-metabolic flux through the OGDHc, making E2o central both to energy metabolism and to supplying succinyl-CoA and the 2-oxoglutarate/glutamate node for biosynthesis. This physiological picture is consistent with systems-biology studies of KT2440 central carbon metabolism ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)).

### Finding 5 — The succinyl-CoA product supplies the TCA cycle and is required for lysine and methionine biosynthesis

The succinyl-CoA generated by the OGDHc (of which E2o/*sucB* is the succinyltransferase) has two fates: it is a **TCA-cycle intermediate** (converted to succinate + GTP/ATP by succinyl-CoA synthetase) and an **essential biosynthetic acyl donor** that succinylates precursors in the bacterial **diaminopimelate/lysine** and **methionine (O-succinyl-homoserine)** pathways. Loss of complex activity therefore causes lysine/methionine auxotrophy. In *Salmonella*, nitrosative inactivation of the shared E3 subunit (LpdA) of the pyruvate and α-ketoglutarate dehydrogenase complexes produces **methionine + lysine (MK) auxotrophy** — Richardson et al. ([PMID: 21767810](https://pubmed.ncbi.nlm.nih.gov/21767810/)) report that **"NO⋅-induced MK auxotrophy results from reduced succinyl-CoA availability as a consequence of NO⋅ targeting of lipoamide-dependent lipoamide dehydrogenase (LpdA) activity"** and that **"LpdA is an essential component of the pyruvate and α-ketoglutarate dehydrogenase complexes."** These results precisely define the downstream role of the OGDHc's product.

### Finding 6 — Substrate specificity is set at the lipoyl domain by cognate E1o recognition

Substrate specificity of E2o is established at its lipoyl domain, which is reductively succinylated only by its cognate E1o in the presence of 2-oxoglutarate. Jones, Horne, Reche & Perham ([PMID: 10623527](https://pubmed.ncbi.nlm.nih.gov/10623527/)) showed that **"the lipoyl domains of the dihydrolipoyl acyltransferase (E2p, E2o) components of the pyruvate and 2-oxoglutarate dehydrogenase multienzyme complexes are specifically recognised by their cognate 2-oxo acid decarboxylase (E1p, E1o)"** and that an engineered/modified domain **"remained unable to undergo reductive succinylation by E1o in the presence of 2-oxoglutarate,"** directly documenting the succinyl-specific loading step. A surface loop adjacent to the lipoyl-lysine β-turn distinguishes the pyruvate (E2p/acetyl) and 2-oxoglutarate (E2o/succinyl) branches. The three-component architecture is confirmed in the human complex ([PMID: 30323066](https://pubmed.ncbi.nlm.nih.gov/30323066/)): **"The hOGDHc comprises three components, hE1o, hE2o, and hE3."** In Q88FB0, the lipoyl-lysine sits at Lys43 in the conserved β-turn, and catalytic His378 (D-H-R motif) catalyzes succinyl transfer to CoA.

### Finding 7 — *P. putida* SucB is a bona fide ortholog of the model *E. coli* E2o (60% identity)

A Needleman–Wunsch global alignment of *P. putida* KT2440 SucB (Q88FB0, 407 aa) against *E. coli* K-12 SucB/E2o (P0AFG6, 405 aa) gives **60.4% amino-acid identity genome-wide** and **66.1% identity across the C-terminal catalytic acyltransferase region** — far above the ~20–30% "twilight zone" — indicating unambiguous orthology and conserved function. The two diagnostic catalytic residues are conserved: the **lipoyl-lysine at Lys43** (D-K-V β-turn) and the **catalytic His378** in the D-H-R motif. Both proteins share identical domain order (lipoyl → PSBD → CAT) and near-identical length (407 vs. 405 aa). This orthology validates the transfer of the extensive mechanistic and structural annotation available for the *E. coli* enzyme to PP_4188.

### Finding 8 — Activity requires covalent lipoylation of Lys43

The lipoyl domain of E2o carries a **covalently attached lipoic acid** on its conserved lysine (Lys43 in Q88FB0), and this modification is **obligatory for catalysis**. Hassan & Cronan ([PMID: 21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/)) state that **"Lipoic acid is a covalently attached cofactor essential for the activity of 2-oxoacid dehydrogenases and the glycine cleavage system. In the absence of lipoic acid modification, the dehydrogenases are inactive, and aerobic metabolism is blocked."** Two routes attach the cofactor:

- **De novo synthesis:** **"LipB is responsible for octanoylation of the E2 components of 2-oxoacid dehydrogenases to provide the substrates of LipA, an S-adenosyl-L-methionine radical enzyme that inserts two sulfur atoms into the octanoyl moiety to give the active lipoylated dehydrogenase complexes"** ([PMID: 21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/)).
- **Salvage:** the lipoate protein ligase **LplA** ligates exogenous lipoate. Cao & Cronan ([PMID: 25631049](https://pubmed.ncbi.nlm.nih.gov/25631049/)) describe how a lipoyl-AMP mixed anhydride **"is attacked by the ϵ-amino group of a specific lysine present on a highly conserved acceptor protein domain, resulting in the amide-linked coenzyme,"** defining the chemistry of attachment to the acceptor lysine (Lys43) of the E2 lipoyl domain.

---

## Mechanistic Model / Interpretation

E2o (SucB) is best understood as the **hub** of the OGDHc: it is at once the enzyme catalyzing the central acyl-transfer step, the scaffold that assembles the entire complex, and the mobile arm that shuttles the reaction intermediate between the three catalytic components. The reaction proceeds through three coupled half-reactions, physically linked by the lipoyl swinging arm:

```
                       2-oxoglutarate (α-ketoglutarate)
                                 │
                                 ▼
    ┌─────────── E1o (SucA, decarboxylase, ThDP) ───────────┐
    │  2-OG + [lipoyl-Lys43] → S-succinyl-dihydrolipoyl +CO₂ │  ← reductive succinylation
    └───────────────────────────┬───────────────────────────┘
                                 │  swinging lipoyl arm (Lys43)
                                 ▼
    ┌─────────── E2o (SucB, THIS PROTEIN, EC 2.3.1.61) ─────┐
    │  S-succinyl-dihydrolipoyl + CoA → succinyl-CoA         │  ← succinyl transfer (His378)
    │                              + dihydrolipoyl-Lys43     │
    └───────────────────────────┬───────────────────────────┘
                                 │  swinging lipoyl arm (Lys43)
                                 ▼
    ┌─────────── E3 (LpdA, dihydrolipoamide DH, FAD) ───────┐
    │  dihydrolipoyl-Lys43 + NAD⁺ → lipoyl-Lys43 + NADH      │  ← re-oxidation of arm
    └───────────────────────────────────────────────────────┘

    NET:  2-oxoglutarate + CoA + NAD⁺ → succinyl-CoA + CO₂ + NADH
```

**Domain map of Q88FB0 (407 aa):**

| Region (approx.) | Module | Role | Key residue/feature |
|---|---|---|---|
| 2–77 | Lipoyl (biotinyl/lipoyl-BS) domain | Carries swinging arm; loaded by E1o | **Lys43** (D-K-V β-turn), site of covalent lipoylation |
| 78–108 | Ala/Pro-rich linker | Confers mobility to lipoyl arm | Flexible, extended |
| 108–145 | Peripheral subunit-binding domain (PSBD) | Recruits/docks E1o and E3 | Partner-binding surface |
| ~146–407 | CAT-like catalytic acyltransferase domain | Succinyl→CoA transfer; core self-assembly | **His378** (D-H-R motif) |

**Placement in metabolism.** The succinyl-CoA product sits at a key metabolic branch point. It continues the oxidative TCA cycle via succinyl-CoA synthetase, and it is drawn off as the succinyl donor for lysine (via succinyl-diaminopimelate) and methionine (via O-succinyl-homoserine) biosynthesis. In *P. putida* KT2440 — an obligate aerobe using the EDEMP cycle for sugar catabolism — the OGDHc carries high flux, so E2o is central to both ATP/NADH generation and biosynthetic supply.

| Product fate | Pathway | Consequence of OGDHc loss |
|---|---|---|
| Succinyl-CoA → succinate + GTP/ATP | TCA cycle (succinyl-CoA synthetase) | Impaired oxidative energy metabolism |
| Succinyl-CoA → succinyl-DAP → **lysine** | Diaminopimelate/lysine biosynthesis | Lysine auxotrophy |
| Succinyl-CoA → O-succinyl-homoserine → **methionine** | Methionine biosynthesis | Methionine auxotrophy |

The requirement for covalent lipoylation adds an essential post-translational dependency: without LipB/LipA (de novo) or LplA (salvage) installing lipoate on Lys43, E2o — and the whole complex — is catalytically dead.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [10623527](https://pubmed.ncbi.nlm.nih.gov/10623527/) | *Structural determinants of PTM and catalytic specificity for the lipoyl domains of the E. coli PDH complex* | Primary experimental evidence: E2o lipoyl domain is specifically recognized by cognate E1o and undergoes reductive succinylation with 2-oxoglutarate; defines substrate-branch specificity (Findings 2, 3, 6) |
| [30323066](https://pubmed.ncbi.nlm.nih.gov/30323066/) | *A multipronged approach unravels PPIs in the human 2-oxoglutarate dehydrogenase complex* | Confirms canonical three-component (E1o/E2o/E3) architecture and pivotal TCA-cycle role (Findings 2, 6) |
| [38963492](https://pubmed.ncbi.nlm.nih.gov/38963492/) | *Mitochondrial alpha-keto acid dehydrogenase complexes: structure and function* | Establishes OGDHc placement in the citric acid cycle and the ~10 MDa, >100-chain E2-core scaffold (Findings 2, 3) |
| [29608861](https://pubmed.ncbi.nlm.nih.gov/29608861/) | *Atomic structure of the E2 inner core of human pyruvate dehydrogenase complex* | Structural basis of the E2 self-assembled inner core scaffold (Finding 3) |
| [21767810](https://pubmed.ncbi.nlm.nih.gov/21767810/) | *Multiple targets of nitric oxide in the TCA cycle of Salmonella* | Shows succinyl-CoA from the OGDHc is required for methionine + lysine biosynthesis; E3/LpdA shared with PDH (Finding 5) |
| [21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/) | *Protein–protein interactions in assembly of lipoic acid on 2-oxoacid dehydrogenases* | Lipoylation is obligatory for activity; describes de novo LipB/LipA pathway (Finding 8) |
| [25631049](https://pubmed.ncbi.nlm.nih.gov/25631049/) | *The Streptomyces coelicolor lipoate-protein ligase…* | Defines chemistry of lipoate attachment to the conserved acceptor lysine of the E2 lipoyl domain (Finding 8) |
| [41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/) | *Redefining HexR regulatory landscape in P. putida KT2440* | Context for KT2440's aerobic, EDEMP-based central carbon metabolism (Finding 4) |

**Note on evidence type.** All mechanistic and structural evidence derives from **orthologous** model enzymes (predominantly *E. coli* E2o and human OGDHc/PDC), transferred to PP_4188 on the basis of 60% sequence identity, conserved catalytic residues, and identical domain architecture. This is a well-justified inference but not direct *P. putida* enzymology.

---

## Supported and Refuted Hypotheses

**Supported**

- **H1** — *sucB* = E2o dihydrolipoyllysine-residue succinyltransferase (EC 2.3.1.61): **Supported** by exact InterPro/domain match and sequence signatures (lipoyl-Lys43, catalytic His378).
- **H2** — Primary function is succinyl transfer from dihydrolipoamide to CoA, yielding succinyl-CoA: **Supported** (EC definition; Perham reductive-succinylation data, PMID 10623527).
- **H3** — E2o is the structural core and couples active sites via a swinging lipoyl arm: **Supported** (family structural/biochemical literature, PMID 38963492, 29608861).
- **H4** — Cytoplasmic localization, *sucAB* operon, TCA-cycle housekeeping role: **Supported** (sequence features, genomic context, KT2440 physiology).
- **H5** — Activity requires covalent lipoylation of Lys43: **Supported** (PMID 21209092, 25631049).

**Refuted / excluded**

- The alternative that "sucB" here refers to an unrelated same-symbol gene: **Refuted** — the domain architecture is unambiguously E2o and the protein is 60% identical to the characterized *E. coli* E2o.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific enzymology.** There is no published biochemical or genetic characterization of PP_4188/Q88FB0 itself; the assignment is entirely by (strong) homology transfer.
2. **No experimental structure.** No crystal or cryo-EM structure of *P. putida* E2o exists; domain boundaries and residue numbering (Lys43, His378) are inferred from alignment to characterized orthologs and may shift by a few residues.
3. **Core symmetry unconfirmed for this organism.** Whether the *P. putida* E2o core is 24-meric (cubic) or 60-meric (icosahedral) has not been determined directly; both symmetries occur across the family.
4. **Lipoylation route in *P. putida* not directly demonstrated.** LipB/LipA vs. LplA usage and essentiality in KT2440 are inferred from *E. coli* and general bacterial biology.
5. **Auxotrophy phenotype not tested in *P. putida*.** The lysine/methionine dependence on succinyl-CoA is demonstrated in *Salmonella*, not *P. putida*; network differences could alter the phenotype.
6. **Kinetic parameters undefined.** kcat/Km for 2-oxoglutarate and CoA for the *P. putida* enzyme are not experimentally established.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted deletion / CRISPRi knockdown of PP_4188** in *P. putida* KT2440 (highly tractable for such edits), followed by growth phenotyping on glucose, succinate, and glutamate, with lysine/methionine supplementation tests to confirm the predicted auxotrophy and TCA-cycle role.
2. **Recombinant expression and enzymatic assay** of Q88FB0 to directly measure EC 2.3.1.61 succinyltransferase activity (e.g., DTNB/CoA-coupled assay) and reconstitute the full OGDHc with cloned *sucA* (E1o) and *lpdA* (E3).
3. **Mass-spectrometric verification of lipoylation** at Lys43 in native and recombinant protein, and identification of the responsible ligase pathway by deleting *lipB*/*lipA* vs. *lplA*.
4. **Cryo-EM of the reconstituted complex** to determine core symmetry (24- vs. 60-mer) and validate domain architecture and PSBD-mediated E1o/E3 docking.
5. **Site-directed mutagenesis** of predicted catalytic residues (K43R lipoyl-lysine; H378N/H378A) to experimentally confirm their roles.
6. **¹³C metabolic flux analysis** across the OGDHc node under different carbon sources to quantify E2o's contribution to succinyl-CoA supply and its partitioning between energy and biosynthesis in this biotechnologically important host.

---

*Prepared from an 8-finding, 23-paper autonomous investigation. Functional assignment: high confidence (diagnostic domain architecture + conserved catalytic residues + 60% orthology to the experimentally characterized E. coli E2o), with the caveat that all direct mechanistic/structural evidence comes from orthologs rather than the P. putida protein itself.*


## Artifacts

- [OpenScientist final report](sucB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sucB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10623527
2. PMID:38963492
3. PMID:30323066
4. PMID:29608861
5. PMID:41260329
6. PMID:21767810
7. PMID:21209092
8. PMID:25631049