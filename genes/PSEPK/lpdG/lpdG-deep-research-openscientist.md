---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:38:53.292854'
end_time: '2026-07-11T18:52:06.263482'
duration_seconds: 792.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lpdG
  gene_symbol: lpdG
  uniprot_accession: Q88FB1
  protein_description: 'RecName: Full=Dihydrolipoyl dehydrogenase {ECO:0000256|ARBA:ARBA00016961,
    ECO:0000256|RuleBase:RU003692}; EC=1.8.1.4 {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692};'
  gene_info: Name=lpdG {ECO:0000313|EMBL:AAN69768.1}; OrderedLocusNames=PP_4187 {ECO:0000313|EMBL:AAN69768.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-I pyridine nucleotide-disulfide
  protein_domains: Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188);
    FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156);
    Lipoamide_DH. (IPR006258)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lpdG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lpdG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FB1
- **Protein Description:** RecName: Full=Dihydrolipoyl dehydrogenase {ECO:0000256|ARBA:ARBA00016961, ECO:0000256|RuleBase:RU003692}; EC=1.8.1.4 {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692};
- **Gene Information:** Name=lpdG {ECO:0000313|EMBL:AAN69768.1}; OrderedLocusNames=PP_4187 {ECO:0000313|EMBL:AAN69768.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-I pyridine nucleotide-disulfide
- **Key Domains:** Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156); Lipoamide_DH. (IPR006258)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lpdG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lpdG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lpdG** (gene ID: lpdG, UniProt: Q88FB1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lpdG* (LPD-glc) — Dihydrolipoyl Dehydrogenase of *Pseudomonas putida* KT2440

**UniProt:** Q88FB1 | **Locus:** PP_4187 | **Gene:** *lpdG* | **EC:** 1.8.1.4
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)

---

## Summary

The gene ***lpdG*** (PP_4187; UniProt **Q88FB1**) of *Pseudomonas putida* KT2440 encodes **LPD-glc**, the "general" or "glucose-type" **dihydrolipoyl dehydrogenase** (also called lipoamide dehydrogenase; **EC 1.8.1.4**). This FAD-dependent flavoenzyme is the **E3 component** shared by two of the cell's α-keto-acid dehydrogenase multienzyme complexes — pyruvate dehydrogenase (PDH) and 2-oxoglutarate (α-ketoglutarate) dehydrogenase (OGDH) — and it additionally serves as the **L-protein (L-factor)** of the glycine cleavage system. Its catalytic job is to regenerate the oxidized lipoyl cofactor: it accepts two electrons and two protons from the reduced dihydrolipoyl group covalently attached to the lysine residues of the E2 (acyltransferase) or H-protein components, and transfers them to NAD⁺, producing NADH. This reaction closes the catalytic cycle of these complexes and represents a key node linking central carbon metabolism to the cellular NADH/NAD⁺ redox pool.

Four independent lines of evidence converge on this assignment. **(1) Direct experimental characterization:** Palmer, Hatter & Sokatch cloned and sequenced *lpdG* and identified its product biochemically as LPD-glc, the E3 of PDH and OGDH and the L-factor of glycine oxidation ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/)); Sokatch & Burns showed experimentally that glycine oxidation specifically requires LPD-glc ([PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)). **(2) Mechanistic/enzymological homology:** the reaction, cofactor (non-covalent FAD), redox-active disulfide, and flavin catalytic cycle are well established for lipoamide dehydrogenases of the pyridine-nucleotide-disulfide oxidoreductase family ([PMID: 12463758](https://pubmed.ncbi.nlm.nih.gov/12463758/); [PMID: 7557016](https://pubmed.ncbi.nlm.nih.gov/7557016/)). **(3) Sequence-level architecture:** Q88FB1 contains the two diagnostic Rossmann dinucleotide-binding folds (for FAD and NAD), the redox-active Cys49–Cys54 disulfide, and the catalytic His451, exactly as expected for this enzyme family. **(4) Genomic context:** *lpdG* lies within the 2-oxoglutarate dehydrogenase operon (*sucA-sucB-lpdG*), embedded in a contiguous TCA-cycle gene cluster, and is one of three distinct *lpd* paralogs in the genome.

The protein functions as a **homodimer in the cytoplasm**, binding one FAD per subunit. It is functionally and genetically distinct from the two other *P. putida* lipoamide dehydrogenases: **LPD-val** (*lpdV*/PP_4404), the dedicated E3 of the branched-chain 2-oxoacid dehydrogenase, and the orphan paralog **LPD-3** (PP_5366). This division of labor — dedicated E3s for the branched-chain and 2-oxoglutarate complexes, but a "borrowed" general E3 (LPD-glc) supplying PDH and the glycine cleavage system in *trans* — is a hallmark of *Pseudomonas* central-metabolism organization.

---

## Key Findings

### Finding 1 — *lpdG* encodes LPD-glc, the shared E3 dihydrolipoyl dehydrogenase

The foundational identification comes from **Palmer, Hatter & Sokatch (1991)**, who cloned and sequenced the *lpdG* structural gene (476 codons plus a stop codon) and identified its product as **LPD-glc**, described verbatim as *"the E3 component of the pyruvate and 2-ketoglutarate dehydrogenase complexes and the L-factor for the glycine oxidation system"* ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/)). This single sentence assigns the *lpdG* product to all three of its multienzyme roles.

A distinctive feature of *Pseudomonas* biochemistry, unlike *E. coli* which uses a single lipoamide dehydrogenase, is that *P. putida* produces **three** distinct lipoamide dehydrogenases: **LPD-glc** (the *lpdG* product), **LPD-val** (the *lpdV* product, specific to branched-chain 2-oxoacid dehydrogenase), and **LPD-3**. This multiplicity makes the specific functional assignment of each isozyme non-trivial and is precisely why experimental discrimination was necessary.

The role in glycine oxidation was demonstrated directly by **Sokatch & Burns (1984)**, who showed that the 56 kDa LPD-glc — *not* the branched-chain LPD-val — is the enzyme used by the glycine oxidation system: *"These results indicate that LPD-glc is specifically utilized for glycine oxidation in P. putida"* ([PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)). This is experimental, not merely inferential, evidence tying the *lpdG* product to the glycine cleavage system.

### Finding 2 — Catalytic reaction and mechanism (EC 1.8.1.4)

The enzyme catalyzes the **NAD⁺-dependent oxidation of protein-bound dihydrolipoyl cofactors**. The curated reaction (Rhea RHEA:15045) is:

> **N⁶-[(R)-dihydrolipoyl]-L-lysyl-[protein] + NAD⁺ ⇌ N⁶-[(R)-lipoyl]-L-lysyl-[protein] + NADH + H⁺**

The mechanism has been resolved in exquisite detail in the closely related mycobacterial enzyme by **Argyrou, Blanchard & Palfey (2002)**, who describe that *"Lipoamide dehydrogenase catalyses the NAD(+)-dependent oxidation of the dihydrolipoyl cofactors that are covalently attached to the acyltransferase components of the pyruvate dehydrogenase, alpha-ketoglutarate dehydrogenase, and glycine reductase multienzyme complexes. It contains a tightly, but noncovalently, bound FAD and a redox-active disulfide, which cycle between the oxidized and reduced forms during catalysis"* ([PMID: 12463758](https://pubmed.ncbi.nlm.nih.gov/12463758/)).

Stopped-flow kinetics in that study resolved the discrete flavin intermediates of the catalytic cycle: rapid formation of a FADH₂·NAD⁺ charge-transfer species, intramolecular electron transfer from FADH₂ to the redox-active disulfide generating the two-electron-reduced enzyme (**EH₂**), and subsequent reoxidation. This establishes the reducing-equivalent path: **dihydrolipoyl → redox-active disulfide → FAD → NAD⁺**.

**Williams (1995)** places the enzyme firmly in the **pyridine nucleotide-disulfide oxidoreductase family** of flavoenzymes — which also includes glutathione reductase, thioredoxin reductase, trypanothione reductase, mercuric reductase, and NADH peroxidase — and notes that *"The path of reducing equivalents in catalysis by glutathione reductase and lipoamide dehydrogenase is clear"* ([PMID: 7557016](https://pubmed.ncbi.nlm.nih.gov/7557016/)). The mechanistic clarity for lipoamide dehydrogenase provides a well-validated template for LPD-glc's catalytic behavior. Related studies of thioredoxin reductase reinforce that these enzymes cycle between defined oxidation states with pyridine nucleotide bound ([PMID: 8664260](https://pubmed.ncbi.nlm.nih.gov/8664260/)).

### Finding 3 — Pathway roles, operon context, and localization

Genetically, **Palmer et al. (1991)** found that *lpdG* *"is preceded by a partial open reading frame with strong similarity to the E2 component of 2-ketoglutarate dehydrogenase of Escherichia coli. This suggests that lpdG is part of the 2-ketoglutarate dehydrogenase operon"* ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/)). Importantly, they also showed *lpdG* can be expressed separately from the other operon genes (a plasmid, pHP4, carrying the E2 partial ORF plus intergenic DNA plus *lpdG* expressed the enzyme), which is consistent with LPD-glc needing to be supplied to multiple complexes beyond OGDH.

For the glycine cleavage system, **Sokatch & Burns (1984)** quantified the biochemical preference: glycine-grown cells produce only the 56 kDa LPD-glc, and the purified glycine oxidation system was stimulated specifically by LPD-glc and inhibited by anti-LPD-glc antibody. Notably, *"LPD-glc was five times as active as LPD-val in catalyzing the oxidation of purified protein H, the heat-stable, lipoic acid-containing protein of the glycine oxidation system"* ([PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)) — a 5-fold catalytic preference that mechanistically explains the isozyme specialization. Protein H is the lipoyl-carrier ("H-protein") of the glycine cleavage system, and LPD-glc acts as its L-protein.

**Localization:** the enzyme is **cytoplasmic** (UniProt subcellular location: cytoplasm), consistent with the soluble location of the α-keto-acid dehydrogenase complexes and the glycine cleavage system in bacteria.

### Finding 4 — Sequence-level catalytic architecture confirms the fold

The Q88FB1 protein is **478 amino acids, 49,912 Da** (UniProt). Direct motif analysis of the sequence identifies every diagnostic feature of a glutathione-reductase-family lipoamide dehydrogenase:

| Feature | Position | Motif / annotation | Role |
|---|---|---|---|
| FAD-binding Rossmann fold | residues 11–16 | GxGxxG (GAGPGG) | Binds the FAD dinucleotide |
| NAD-binding Rossmann fold | residues 188–193 | GxGxxG (GAGVIG) | Binds the NAD⁺ dinucleotide |
| Redox-active disulfide | Cys49–Cys54 | CxxxxC (GGTC⁴⁹LNVGC⁵⁴) | Two-electron redox center adjacent to FAD |
| Catalytic base | His451 | His–Glu catalytic dyad | Proton acceptor from dihydrolipoyl dithiol |

UniProt domain architecture reports an **FAD/NAD(P)-binding domain (residues 5–334)** and a **pyridine nucleotide-disulphide oxidoreductase dimerisation domain (residues 353–462)**. The enzyme binds **one FAD per subunit** and is a **homodimer** — the two active sites of the dimer are formed at the subunit interface, a defining structural characteristic of this family. This sequence-level analysis independently corroborates the biochemical assignment: the protein has exactly the catalytic hardware required to perform the dihydrolipoyl→NAD⁺ reaction. The InterPro signatures reported for Q88FB1 (Class-I_Pyr_Nuc-Dis_Oxidored IPR050151; FAD/NAD-bd_sf IPR036188; Lipoamide_DH IPR006258) are fully consistent with this assignment.

### Finding 5 — Genomic operon context and paralog distinctness in KT2440

Mapping the PP_4187 neighborhood in the KT2440 genome places *lpdG* immediately downstream of the 2-oxoglutarate dehydrogenase **E1 (*sucA*/PP_4189)** and **E2 (*sucB*/PP_4188, dihydrolipoyllysine-residue succinyltransferase)**, forming a **_sucA–sucB–lpdG_ operon**, and directly upstream of **succinyl-CoA synthetase (*sucC*/PP_4186, *sucD*/PP_4185)** — a contiguous TCA-cycle gene cluster. This modern genome mapping experimentally corroborates the 1991 observation of a 2-ketoglutarate-DH-E2-like ORF preceding *lpdG* ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/)).

KT2440 encodes exactly **three EC 1.8.1.4 paralogs**, and they are substantially divergent — not redundant copies:

| Paralog | Locus | Length | Identity vs *lpdG* | Function |
|---|---|---|---|---|
| **LPD-glc** (*lpdG*) | PP_4187 | 478 aa | — | General E3: PDH, OGDH, glycine cleavage |
| **LPD-val** (*lpdV*) | PP_4404 | 459 aa | 42.3% | Branched-chain 2-oxoacid DH E3 |
| **LPD-3** (*lpd*) | PP_5366 | 466 aa | 51.2% | Orphan; function less defined |

Pairwise global identities: *lpdG* vs *lpdV* = **42.3%**, *lpdG* vs *lpd* (PP_5366) = **51.2%**, *lpdV* vs *lpd* = **45.3%**. These modest identities (all well below 60%) confirm that the three isozymes are genuinely distinct proteins with specialized roles, not recent gene duplications. This is consistent with **Sokatch et al. (1989)** on *lpdV*, who noted that the production of two lipoamide dehydrogenases *"by Pseudomonas is so far unique"* and that LPD-val is *"somewhat more distantly related"* to the other lipoamide dehydrogenases ([PMID: 2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/)).

### Finding 6 — Operon architecture explains *trans*-supply of LPD-glc

Genome mapping reveals a clear logic to which complexes carry their own E3 versus which borrow LPD-glc:

- **Pyruvate dehydrogenase**: E1 (*aceE*/PP_0339) and E2 (*aceF*/PP_0338) have **no adjacent lipoamide-dehydrogenase gene** → must recruit LPD-glc in *trans*.
- **Glycine cleavage system**: two gene clusters (*gcvP1/gcvH1/gcvT-I* at PP_0988/PP_0989/PP_0986; and *gcvP2/gcvH2/gcvT* at PP_5192/PP_5193/PP_5194) likewise encode **no local E3** → borrow LPD-glc.
- **2-oxoglutarate dehydrogenase**: carries its own E3 (*lpdG*/PP_4187) within its operon.
- **Branched-chain 2-oxoacid dehydrogenase (bkd)**: carries a **dedicated E3** (*lpdV*/PP_4404), immediately downstream of the bkd E2 (*bkdB*/PP_4403).
- **Third paralog** *lpd*/PP_5366 is an **orphan** flanked by unrelated genes (e.g., cardiolipin synthase *clsA*/PP_5364), not embedded in any 2-oxoacid dehydrogenase operon.

This architecture elegantly explains the biochemical data: because PDH and the glycine cleavage system lack a co-transcribed E3, they depend on the operon-encoded LPD-glc from the OGDH cluster — hence LPD-glc's designation as the "general" E3.

---

## Mechanistic Model / Interpretation

LPD-glc sits at a metabolic hub where three multienzyme systems converge on a single flavoenzyme to recycle their lipoyl cofactor and feed electrons into the NADH pool.

```
   Central carbon / one-carbon metabolism            LPD-glc (lpdG, PP_4187)
   ───────────────────────────────────               homodimer, cytoplasm, 1 FAD/subunit
                                                      ┌──────────────────────────────┐
   Pyruvate ──PDH(E1/E2)──► Acetyl-CoA               │  dihydrolipoyl-[protein]     │
        aceE/aceF (PP_0339/0338)  ─── lipoyl-SH ────►│        │                     │
                                                      │        ▼ (Cys49–Cys54 S-S)   │
   2-Oxoglutarate ─OGDH(E1/E2)─► Succinyl-CoA        │   redox-active disulfide     │
        sucA/sucB (PP_4189/4188)  ─── lipoyl-SH ────►│        │                     │
        [same operon as lpdG]                         │        ▼                     │
                                                      │       FAD                    │
   Glycine ──GCS(P/H/T)──► CO2 + NH3 + CH2-THF        │        │                     │
        gcvPHT (PP_0986-89 / PP_5192-94)─ lipoyl-SH ►│        ▼                     │
                                                      │       NAD⁺ ──► NADH + H⁺     │
                                                      └──────────────────────────────┘
                                                                     │
                                                                     ▼
                                              electrons to respiratory chain / biosynthesis
```

**Reducing-equivalent flow within the enzyme:** reduced dihydrolipoyl dithiol → redox-active Cys49–Cys54 disulfide → FAD → NAD⁺. The catalytic base His451 deprotonates the incoming dithiol; the two electrons pass to the disulfide, then to FAD (forming FADH₂), and finally as a hydride to NAD⁺. The enzyme cycles between the oxidized and two-electron-reduced (EH₂) states, as demonstrated for the family by stopped-flow flavin kinetics ([PMID: 12463758](https://pubmed.ncbi.nlm.nih.gov/12463758/)).

**Division of labor among the three isozymes:**

| Complex | E3 used | Source |
|---|---|---|
| Pyruvate dehydrogenase | LPD-glc (*lpdG*) | borrowed *in trans* |
| 2-Oxoglutarate dehydrogenase | LPD-glc (*lpdG*) | same operon |
| Glycine cleavage system | LPD-glc (*lpdG*) | borrowed *in trans* |
| Branched-chain 2-oxoacid dehydrogenase | LPD-val (*lpdV*) | dedicated, co-operonic |
| (unassigned) | LPD-3 (PP_5366) | orphan |

The functional logic is that LPD-glc is the housekeeping / general-purpose E3 for the glucose- and TCA-linked complexes plus one-carbon (glycine) metabolism, while LPD-val is a specialist reserved for branched-chain amino-acid catabolism, where the branched-chain complex requires a compatible, dedicated E3. The 5-fold catalytic preference of LPD-glc over LPD-val on the glycine-cleavage H-protein ([PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)) shows that this specialization is enforced at the level of protein–protein recognition and catalytic efficiency, not merely gene regulation.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/) | *Cloning and sequence analysis of the LPD-glc structural gene of P. putida* | **Primary.** Cloned/sequenced *lpdG* (476 codons); assigns product LPD-glc as E3 of PDH & OGDH and L-factor of glycine oxidation; establishes 2-KG-DH operon context. |
| [6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/) | *Oxidation of glycine by P. putida requires a specific lipoamide dehydrogenase* | **Primary/experimental.** Shows LPD-glc (not LPD-val) is specifically used in glycine oxidation; 5× more active on protein H; antibody inhibition. |
| [12463758](https://pubmed.ncbi.nlm.nih.gov/12463758/) | *Lipoamide dehydrogenase from M. tuberculosis: direct observation of flavin intermediates* | **Mechanistic.** Defines the reaction, non-covalent FAD, redox-active disulfide, and the flavin catalytic cycle for a close homolog. |
| [7557016](https://pubmed.ncbi.nlm.nih.gov/7557016/) | *Mechanism and structure of thioredoxin reductase from E. coli* | **Family context.** Places lipoamide dehydrogenase in the pyridine-nucleotide-disulfide oxidoreductase family; clarifies reducing-equivalent path. |
| [2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/) | *Sequence analysis of the lpdV gene of P. putida* | **Comparative.** Characterizes the sister isozyme LPD-val (branched-chain-specific), confirming LPD-glc's distinct role; notes the two-isozyme system is unique to *Pseudomonas*. |
| [8664260](https://pubmed.ncbi.nlm.nih.gov/8664260/) | *Enzyme-monitored turnover of E. coli thioredoxin reductase* | **Family context.** Reinforces the shared flavin/disulfide catalytic paradigm across the family. |

The two *P. putida*-specific primary papers ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/) and [PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)) directly and unambiguously establish the identity and function of the *lpdG* product. The mechanistic and family papers provide the well-validated enzymological framework, and the sequence/genomic analyses (Findings 4–6) independently corroborate the assignment at the levels of protein architecture and genome organization. No evidence in any of the reviewed literature challenges the assignment.

---

## Limitations and Knowledge Gaps

1. **Studies predate the KT2440 genome.** The definitive biochemical characterization of LPD-glc ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/); [PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)) was performed on *P. putida* isolates rather than specifically the KT2440 reference strain. The mapping of *lpdG* to PP_4187 and its operon relies on genome annotation and sequence homology rather than KT2440-specific biochemistry. Given the near-identity of the sequence and conserved operon structure, this is a low-risk inference, but strictly it remains an inference.

2. **No direct structural data for Q88FB1.** There is no experimental crystal or cryo-EM structure of the *P. putida* LPD-glc itself. The catalytic residue assignments (Cys49–Cys54, His451, Rossmann folds) are derived from sequence motifs and homology to characterized family members, not from an experimental Q88FB1 structure.

3. **The third paralog LPD-3 (PP_5366) remains functionally unassigned.** Its role, substrate complex, and whether it is even expressed under standard conditions are not established from the reviewed literature. It could be a cryptic/conditional E3 or serve a non-canonical redox function.

4. **Kinetic parameters for LPD-glc are not quantified here.** Km for NAD⁺ and for the dihydrolipoyl substrate, kcat, and the extent of substrate inhibition by NADH are not extracted; the mechanistic details are borrowed from homologs.

5. **Regulation and expression are under-characterized.** Although *lpdG* can be transcribed both as part of the *suc* operon and independently, the promoters, growth-condition dependence, and how supply is balanced across PDH, OGDH, and GCS demand are not resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted gene deletion / complementation in KT2440.** Construct a clean ΔPP_4187 mutant and test growth on glucose, TCA-cycle-linked carbon sources, and glycine as sole nitrogen/carbon source. Predicted phenotype: impaired growth requiring PDH/OGDH/GCS function, rescued by *lpdG* complementation but only partially (if at all) by *lpdV* or PP_5366 — directly testing the "general E3" model and isozyme non-redundancy.

2. **Recombinant enzymology.** Express and purify His-tagged Q88FB1, confirm homodimer and 1 FAD/subunit, and measure steady-state kinetics (Km, kcat) with NAD⁺ and dihydrolipoamide, plus reconstitution assays with purified PDH-E2, OGDH-E2, and H-protein to quantify complex-specific activity.

3. **Structure determination.** Solve the crystal or cryo-EM structure of LPD-glc to experimentally confirm the Cys49–Cys54 redox center, FAD pocket, His451 catalytic base, and dimer interface; compare with LPD-val to rationalize substrate-complex specificity.

4. **Characterize LPD-3 (PP_5366).** Determine its expression conditions and test whether it can substitute for LPD-glc or LPD-val in vitro and in vivo, resolving the orphan paralog's biological role.

5. **Isozyme-swap specificity assays.** Reconstitute glycine cleavage and branched-chain dehydrogenase complexes with each of the three purified LPD isozymes to map the determinants of the observed ~5-fold preference of LPD-glc for the H-protein and the dedicated pairing of LPD-val with the bkd complex.

---

## Conclusion

*lpdG* (PP_4187; UniProt Q88FB1) encodes **LPD-glc**, the general cytoplasmic **dihydrolipoyl dehydrogenase (E3, EC 1.8.1.4)** of *Pseudomonas putida*. As a homodimer with one non-covalently bound FAD and a redox-active Cys49–Cys54 disulfide per subunit, it catalyzes the NAD⁺-dependent reoxidation of protein-bound dihydrolipoyl groups, serving as the shared E3 of the pyruvate and 2-oxoglutarate dehydrogenase complexes and as the L-protein of the glycine cleavage system. It is genomically embedded in the *sucA-sucB-lpdG* (2-oxoglutarate dehydrogenase) operon and is distinct from the branched-chain-specific isozyme LPD-val (*lpdV*/PP_4404) and the orphan paralog LPD-3 (PP_5366). This assignment is supported by direct experimental characterization, well-established family enzymology, sequence-level catalytic architecture, and genomic operon context — four convergent and mutually consistent evidence streams.


## Artifacts

- [OpenScientist final report](lpdG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lpdG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:1902462
2. PMID:6546487
3. PMID:12463758
4. PMID:7557016
5. PMID:8664260
6. PMID:2917566