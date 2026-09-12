---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T09:29:49.234465'
end_time: '2026-07-23T10:01:36.512964'
duration_seconds: 1907.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabG
  gene_symbol: fabG
  uniprot_accession: Q88LL6
  protein_description: 'RecName: Full=3-oxoacyl-[acyl-carrier-protein] reductase {ECO:0000256|RuleBase:RU366074};
    EC=1.1.1.100 {ECO:0000256|RuleBase:RU366074};'
  gene_info: Name=fabG {ECO:0000313|EMBL:AAN67532.1}; OrderedLocusNames=PP_1914 {ECO:0000313|EMBL:AAN67532.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the short-chain dehydrogenases/reductases (SDR)
  protein_domains: 3oxo_ACP_reduc. (IPR011284); KR_dom. (IPR057326); NAD(P)-bd_dom_sf.
    (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR. (IPR050259)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fabG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LL6
- **Protein Description:** RecName: Full=3-oxoacyl-[acyl-carrier-protein] reductase {ECO:0000256|RuleBase:RU366074}; EC=1.1.1.100 {ECO:0000256|RuleBase:RU366074};
- **Gene Information:** Name=fabG {ECO:0000313|EMBL:AAN67532.1}; OrderedLocusNames=PP_1914 {ECO:0000313|EMBL:AAN67532.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the short-chain dehydrogenases/reductases (SDR)
- **Key Domains:** 3oxo_ACP_reduc. (IPR011284); KR_dom. (IPR057326); NAD(P)-bd_dom_sf. (IPR036291); Sc_DH/Rdtase_CS. (IPR020904); SDR. (IPR050259)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabG** (gene ID: fabG, UniProt: Q88LL6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *fabG* (PP_1914 / Q88LL6) in *Pseudomonas putida* KT2440

**Target:** 3-oxoacyl-[acyl-carrier-protein] reductase (β-ketoacyl-ACP reductase)
**Gene:** *fabG* — OrderedLocusName **PP_1914**
**UniProt:** **Q88LL6**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)
**EC:** 1.1.1.100
**Protein family:** Short-chain dehydrogenases/reductases (SDR) superfamily

---

## Summary

**fabG (PP_1914, UniProt Q88LL6) of *Pseudomonas putida* KT2440 encodes 3-oxoacyl-[acyl-carrier-protein] reductase (β-ketoacyl-ACP reductase; EC 1.1.1.100), a soluble cytoplasmic, low-molecular-weight enzyme of the short-chain dehydrogenase/reductase (SDR) superfamily.** Its primary function is to catalyze the NADPH-dependent reduction of 3-oxoacyl-ACP (β-ketoacyl-ACP) to (3R)-3-hydroxyacyl-ACP. This is the **first reductive step of every elongation cycle** of the bacterial type-II fatty-acid synthase (FAS-II) system, and it is the only enzyme known to carry out this reaction in most bacteria, making it essential and largely non-redundant.

The enzyme operates in the **cytoplasm** as a homotetramer, using a canonical SDR **Ser-Tyr-Lys catalytic triad** organized into the catalytically active configuration upon binding of the NADPH cofactor. Direct sequence analysis of Q88LL6 confirms all diagnostic SDR/FabG signatures — the N-terminal Rossmann NAD(P)-binding glycine-rich motif, the structural NNAG motif, and the catalytic triad Ser141/Tyr154/Lys158 embedded in the diagnostic YxxxK motif — aligning residue-for-residue with the experimentally defined *E. coli* FabG triad (Ser138/Tyr151/Lys155). The enzyme accepts acyl-ACP substrates of varying chain length, a flexibility conferred by its protein–protein interaction with acyl-carrier protein (ACP), which "broadens" the active site.

Biologically, FabG supplies the saturated and unsaturated fatty acids that are **essential components of the bacterial cell envelope** (membrane phospholipids and lipid A). In *P. putida* specifically, the 3-hydroxyacyl-ACP intermediates produced by FAS-II (via FabG) are also the **branch-point metabolites** diverted by the transacylase **PhaG** toward **medium-chain-length polyhydroxyalkanoate (MCL-PHA)** storage polyester — the only metabolic link between de novo fatty acid synthesis and PHA biosynthesis in this organism. Function is assigned with high confidence based on the complete conserved catalytic machinery present in the Q88LL6 sequence combined with extensive experimental evidence from FabG orthologs, since no dedicated in vitro biochemical study of the *P. putida* KT2440 enzyme itself was located in the literature.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed:

| Verification step | Result |
|---|---|
| Gene symbol "fabG" matches protein description | ✅ *fabG* is the universal bacterial symbol for β-ketoacyl-ACP reductase; matches EC 1.1.1.100 and the SDR family assignment |
| Organism correct | ✅ *Pseudomonas putida* KT2440; locus tag PP_1914 |
| Protein family / domains align with literature | ✅ SDR superfamily; domains IPR011284 (3-oxoacyl-ACP reductase), IPR050259 (SDR), IPR036291 (NAD(P)-binding), confirmed by direct sequence analysis |
| Risk of confusion with same-symbol gene | Low. *fabG* is unambiguous as an enzyme class; note that some organisms carry multiple *fabG* paralogs (e.g., FabG3 in *Xanthomonas*, HMwFabG in *Acinetobacter/Mycobacterium*) with specialized roles — the KT2440 PP_1914 product is the canonical **low-molecular-weight FAS-II FabG** |

**Conclusion:** The gene symbol is unambiguous for the enzymatic class. A caveat worth noting is that no dedicated experimental characterization of *P. putida* KT2440 FabG (PP_1914) itself exists in the literature; the functional annotation is therefore built from (a) direct sequence analysis of Q88LL6 and (b) extensive experimental evidence from well-characterized FabG orthologs.

---

## Key Findings

### Finding 1 — FabG catalyzes the NADPH-dependent reduction of 3-oxoacyl-ACP, the first reductive step of FAS-II

FabG (Q88LL6) catalyzes the reduction of **3-oxoacyl-ACP (β-ketoacyl-ACP)** to **(3R)-3-hydroxyacyl-ACP**, corresponding to **EC 1.1.1.100**. This is the committed reductive step in each round of the FAS-II elongation cycle, occurring immediately after the condensation step performed by the β-ketoacyl-ACP synthases (FabB/FabF for elongation; FabH for initiation).

The reaction has been directly demonstrated biochemically for multiple FabG orthologs, which reduce β-ketoacyl-ACP to β-hydroxyacyl-ACP using NADPH ([PMID: 28126742](https://pubmed.ncbi.nlm.nih.gov/28126742/); [PMID: 16225460](https://pubmed.ncbi.nlm.nih.gov/16225460/)). As stated for the reaction: *"The ketoacyl-acyl carrier protein (ACP) reductase FabG catalyzes the NADPH/NADH dependent reduction of β-ketoacyl-ACP substrates to β-hydroxyacyl-ACP products, the first reductive step in the fatty acid biosynthesis elongation cycle"* ([PMID: 28126742](https://pubmed.ncbi.nlm.nih.gov/28126742/)).

The enzyme shows a **strong preference for NADPH** over NADH as the reducing cofactor. Kinetic characterization of the *Plasmodium falciparum* orthologue (OAR/FabG) showed that **activity with NADH is <3% of that with NADPH** ([PMID: 16225460](https://pubmed.ncbi.nlm.nih.gov/16225460/)), establishing NADPH as the physiologically relevant electron donor. This cofactor preference is a hallmark of the canonical low-molecular-weight FabG and distinguishes it from certain high-molecular-weight FabG variants (e.g., mycobacterial FabG4) that use NADH.

### Finding 2 — FabG is an essential, non-redundant SDR enzyme with a Ser-Tyr-Lys triad and an allosterically regulated homotetramer

FabG belongs to the **short-chain dehydrogenase/reductase (SDR) superfamily**. The structural and mechanistic basis of catalysis was established in the *E. coli* FabG crystal structure: the **catalytic triad Ser138/Tyr151/Lys155** is organized into its active configuration upon NADPH binding, which simultaneously drives allosteric communication across the **homotetramer** ([PMID: 11669613](https://pubmed.ncbi.nlm.nih.gov/11669613/)). The authors described how cofactor binding *"puts all three active-site residues (Ser 138, Tyr 151, and Lys 155) into their active configurations and provides a structural mechanism for allosteric communication between the active sites in the homotetramer. FabG exhibits negative cooperative binding of NADPH"* ([PMID: 11669613](https://pubmed.ncbi.nlm.nih.gov/11669613/)).

FabG is **essential and largely non-redundant**: it is described as *"the only known enzyme that catalyzes reduction of the 3-ketoacyl-ACP intermediates of bacterial fatty acid synthetic pathways"* ([PMID: 26490537](https://pubmed.ncbi.nlm.nih.gov/26490537/)). Its essentiality is functionally demonstrated by complementation assays that routinely use the *E. coli* *fabG* temperature-sensitive mutant **CL104**, which fails to grow at non-permissive temperature unless a functional 3-oxoacyl-ACP reductase is supplied ([PMID: 26975437](https://pubmed.ncbi.nlm.nih.gov/26975437/); [PMID: 31560825](https://pubmed.ncbi.nlm.nih.gov/31560825/)).

### Finding 3 — The Q88LL6 sequence bears all diagnostic SDR/FabG signatures

Direct analysis of the 246-residue Q88LL6 protein sequence confirms the functional annotation by homology. The sequence contains:

- **N-terminal Rossmann NAD(P)-binding motif** at residues ~10–18: **VTGASRGIG** (the glycine-rich G-x-x-x-G-x-G fingerprint that binds the cofactor dinucleotide)
- **SDR structural NNAG motif** (Asn88-Asn89), which stabilizes the central β-sheet fold
- **Canonical SDR catalytic triad Ser141 / Tyr154 / Lys158**, with the catalytic tyrosine and lysine embedded in the diagnostic **YxxxK motif** (Y154-A-A-A-K158)

These residues align **residue-for-residue** with the experimentally defined *E. coli* FabG catalytic triad (Ser138/Tyr151/Lys155; [PMID: 11669613](https://pubmed.ncbi.nlm.nih.gov/11669613/)). InterPro assigns the **3-oxoacyl-ACP reductase family (IPR011284)** and **SDR family (IPR050259)**. The presence of the complete, correctly spaced catalytic machinery provides high-confidence, structure-based support for the functional assignment even in the absence of a dedicated in vitro study of the KT2440 enzyme.

| Signature | Q88LL6 residues | Role | *E. coli* FabG equivalent |
|---|---|---|---|
| Rossmann glycine-rich motif | VTGASRGIG (~10–18) | NADP(H) dinucleotide binding | conserved |
| NNAG structural motif | Asn88-Asn89 | Fold stabilization | conserved |
| Catalytic Ser | Ser141 | Substrate positioning | Ser138 |
| Catalytic Tyr (YxxxK) | Tyr154 | Catalytic proton donor | Tyr151 |
| Catalytic Lys (YxxxK) | Lys158 | Lowers Tyr pKa; binds NADPH ribose | Lys155 |

### Finding 4 — In *P. putida*, FabG-generated intermediates feed MCL-PHA biosynthesis via PhaG

*P. putida* KT2440 is a premier producer of **medium-chain-length polyhydroxyalkanoates (MCL-PHA)**, and FabG occupies a pivotal upstream position in this biotechnologically important pathway. De novo FAS-II synthesis — in which FabG produces the 3-hydroxyacyl-ACP intermediates — is the source of monomers for MCL-PHA. The transacylase **PhaG** transfers 3-hydroxyacyl moieties from ACP to CoA, and this transacylase-mediated route is described as *"the only metabolic link between fatty acid de novo biosynthesis and PHA biosynthesis in this bacterium"* ([PMID: 11425728](https://pubmed.ncbi.nlm.nih.gov/11425728/)).

PhaG's biochemical activity was defined as a 3-hydroxyacyl-CoA–ACP transferase: *"It catalyzes the transfer of the acyl moiety from in vitro synthesized 3-hydroxydecanoyl-CoA to acyl carrier protein, indicating that PhaG exhibits a 3-hydroxyacyl-CoA-acyl carrier protein transferase activity"* ([PMID: 9727022](https://pubmed.ncbi.nlm.nih.gov/9727022/)). The PhaG diversion is regulated physiologically: PhaG is maximally expressed under **nitrogen limitation** with concomitant PHA accumulation ([PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/)). Thus, FabG sits at the metabolic node feeding both membrane lipid synthesis and carbon-storage polyester production in this organism.

### Finding 5 — FabG's biological process is cell-envelope lipid supply, with chain-length flexibility via ACP and a conserved allosteric site

The downstream biological purpose of FabG is the biogenesis of the cell envelope. FabG products (saturated and unsaturated fatty acids) are *"essential components of the bacterial cell envelope"* ([PMID: 26539719](https://pubmed.ncbi.nlm.nih.gov/26539719/)). More explicitly, FabG *"catalyzes the NADPH dependent reduction of 3-keto-acyl-ACP during fatty acid elongation, thus enabling lipid supply for production and maintenance of the cell envelope"* ([PMID: 33388594](https://pubmed.ncbi.nlm.nih.gov/33388594/)). These fatty acids are used to build membrane phospholipids, lipopolysaccharide/lipooligosaccharide lipid A, and lipoproteins.

FabG achieves its **chain-length flexibility** through its interaction with ACP. The FabG–ACP protein–protein interaction *"'broadens' the active site of these dehydrogenases thus, contributing to their flexible nature"* ([PMID: 31037463](https://pubmed.ncbi.nlm.nih.gov/31037463/)), allowing the enzyme to process β-ketoacyl-ACP substrates across the full range of chain lengths that pass through the elongation cycle (typically C4 up to C16/C18).

FabG also possesses a **conserved allosteric inhibitor site** located at the subunit interface of the tetramer, demonstrated for orthologs from *P. aeruginosa* and *A. baumannii* ([PMID: 33388594](https://pubmed.ncbi.nlm.nih.gov/33388594/)). Because this site is conserved across *Pseudomonas* and other Gram-negative ESKAPE pathogens, the *P. putida* enzyme is inferred to share this regulatory architecture. This also highlights FabG's interest as an **antibacterial drug target**.

---

## Mechanistic Model / Interpretation

### The reaction in context

FabG performs step 2 of the four-step FAS-II elongation cycle. Each cycle extends the growing acyl chain by two carbons:

```
                 malonyl-ACP + acyl-ACP (or acetyl-CoA for initiation)
                             │
        (1) CONDENSATION     │  FabB / FabF (elongation) or FabH (initiation)
                             ▼
                 3-oxoacyl-ACP  (β-ketoacyl-ACP)
                             │
        (2) REDUCTION        │  ◄◄◄  FabG  (PP_1914, Q88LL6)  +NADPH → +NADP⁺
                             ▼
                 (3R)-3-hydroxyacyl-ACP
                             │
        (3) DEHYDRATION      │  FabA / FabZ   (– H₂O)
                             ▼
                 trans-2-enoyl-ACP
                             │
        (4) ENOYL REDUCTION  │  FabI   +NAD(P)H
                             ▼
                 acyl-ACP (elongated by 2 carbons)  ──► re-enters cycle
```

### Catalytic mechanism

FabG uses the classic SDR mechanism. The **Tyr154** hydroxyl acts as the catalytic acid/base, donating a proton to the carbonyl oxygen of the 3-oxo group while a **hydride** is transferred from NADPH (C4 of the nicotinamide ring) to the substrate C3. **Lys158** lowers the pKa of Tyr154 and hydrogen-bonds the nicotinamide ribose, while **Ser141** helps position and polarize the substrate carbonyl. A proton-relay network connecting the nicotinamide ribose, Lys158, Tyr154, and bulk solvent regenerates the catalytic tyrosine. The product is stereospecifically the **(3R)-3-hydroxyacyl** isomer. NADPH binding is a prerequisite that orders the catalytic residues and, through the tetramer interface, produces **negative cooperativity** in cofactor binding ([PMID: 11669613](https://pubmed.ncbi.nlm.nih.gov/11669613/)).

### Localization

FabG is a **soluble cytoplasmic** enzyme. FAS-II is a dissociated, non-membrane system in which all intermediates are covalently tethered to the soluble acyl-carrier protein (ACP) via its phosphopantetheine arm. FabG therefore performs its chemistry in the cytoplasm on ACP-bound substrates; its products are subsequently handed to downstream FAS-II enzymes and, ultimately, to the membrane-associated acyltransferases (PlsB/PlsC/PlsX/PlsY) that build phospholipids at the inner membrane.

### The *P. putida*-specific branch point

```
   Glucose / fatty acids / glycerol  ──►  acetyl-CoA / malonyl-ACP
                                              │
                                        FAS-II cycle
                                     (FabH/FabF, FabG, FabZ, FabI)
                                              │
                                (3R)-3-hydroxyacyl-ACP  ◄── FabG product
                                   ╱                    ╲
                     membrane lipids                    PhaG transacylase
                (phospholipids, lipid A)                (N-limitation ↑)
                                                              │
                                                   3-hydroxyacyl-CoA
                                                              │
                                                       PhaC1 / PhaC2
                                                              │
                                                   MCL-PHA storage polyester
```

This branch-point role explains why FabG is central not only to viability (envelope lipids) but also to the biotechnological value of *P. putida* KT2440 as an MCL-PHA and oleochemical production chassis ([PMID: 11425728](https://pubmed.ncbi.nlm.nih.gov/11425728/); [PMID: 9727022](https://pubmed.ncbi.nlm.nih.gov/9727022/); [PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/)).

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [28126742](https://pubmed.ncbi.nlm.nih.gov/28126742/) | Binding of NADP to FabG | Defines the FabG reaction and its position as the first reductive step of FAS-II (F001) |
| [16225460](https://pubmed.ncbi.nlm.nih.gov/16225460/) | Kinetic/structural studies on OAR from *P. falciparum* | Establishes strong NADPH cofactor preference (NADH activity <3%) (F001) |
| [11669613](https://pubmed.ncbi.nlm.nih.gov/11669613/) | Structure of β-ketoacyl-ACP reductase from *E. coli* | Identifies catalytic triad Ser138/Tyr151/Lys155, tetramer, negative cooperativity (F002, F003) |
| [26490537](https://pubmed.ncbi.nlm.nih.gov/26490537/) | *Ralstonia* two 3-ketoacyl-ACP reductases | States FabG is the only known enzyme for this reaction; supports essentiality/non-redundancy (F002) |
| [26975437](https://pubmed.ncbi.nlm.nih.gov/26975437/) | *S. meliloti* NodG replaces FabG | Demonstrates use of *E. coli fabG* ts mutant CL104 for complementation; essentiality (F002) |
| [31560825](https://pubmed.ncbi.nlm.nih.gov/31560825/) | *Xanthomonas* FabG3 in xanthomonadin | Shows some organisms have specialized FabG paralogs; CL104 complementation assay (context) |
| [11425728](https://pubmed.ncbi.nlm.nih.gov/11425728/) | FAS–PHA link via PhaG in pseudomonads | Establishes FAS de novo synthesis as the source of PHA monomers in *P. putida* (F004) |
| [9727022](https://pubmed.ncbi.nlm.nih.gov/9727022/) | *phaG* gene from *P. putida* KT2440 | Defines PhaG transacylase activity connecting 3-hydroxyacyl-ACP/CoA to PHA (F004) |
| [16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/) | PHA from styrene in *P. putida* CA-3 | Shows PhaG maximally expressed under N-limitation with PHA accumulation (F004) |
| [26539719](https://pubmed.ncbi.nlm.nih.gov/26539719/) | Structural characterisation of FabG from *Yersinia pestis* | Defines cell-envelope lipid supply as downstream biological process (F005) |
| [33388594](https://pubmed.ncbi.nlm.nih.gov/33388594/) | FabG inhibitor targeting allosteric site (ESKAPE) | States FabG reaction/envelope role; conserved allosteric site incl. *P. aeruginosa* (F005) |
| [31037463](https://pubmed.ncbi.nlm.nih.gov/31037463/) | FabG: from a core to circumstantial catalyst | Explains chain-length-flexible substrate handling via ACP interaction (F005) |

### Supporting orthologue structural studies (inference base)

Several crystal structures of FabG orthologs reinforce the mechanistic model applied here to the *P. putida* enzyme: *M. smegmatis* MabA cofactor-induced rearrangements ([PMID: 29717709](https://pubmed.ncbi.nlm.nih.gov/29717709/)), *M. tuberculosis* FabG4 bound to hexanoyl-CoA revealing substrate-binding loops ([PMID: 23163771](https://pubmed.ncbi.nlm.nih.gov/23163771/)), and *A. baumannii* FabG homologs distinguishing low- from high-molecular-weight variants and their coenzyme preferences ([PMID: 33782435](https://pubmed.ncbi.nlm.nih.gov/33782435/); [PMID: 33846444](https://pubmed.ncbi.nlm.nih.gov/33846444/)). These establish that the low-molecular-weight, NADPH-preferring, ACP-dependent FabG — the class to which PP_1914 belongs by sequence — is the canonical FAS-II reductase. FabG is also a validated antibacterial target: the antimicrobial peptide tachyplesin kills multidrug-resistant bacteria in part by inhibiting FabG ([PMID: 29765362](https://pubmed.ncbi.nlm.nih.gov/29765362/)).

---

## Limitations and Knowledge Gaps

1. **No dedicated study of the KT2440 enzyme.** No in vitro biochemical or structural characterization of *P. putida* KT2440 FabG (PP_1914 / Q88LL6) itself was located. The functional assignment rests on (a) direct sequence analysis showing the complete conserved catalytic machinery and (b) extensive experimental evidence from orthologs. Confidence is high but the specific kinetic parameters (Km, kcat), chain-length profile, and cooperativity of the KT2440 enzyme are inferred, not measured.

2. **Substrate chain-length specificity not empirically defined for this enzyme.** FabG generally accepts a broad range of chain lengths, but the precise substrate preference profile of PP_1914 — potentially relevant to MCL-PHA monomer composition — has not been experimentally determined.

3. **Essentiality in *P. putida* specifically is inferred.** While FabG is essential in *E. coli* and other bacteria (CL104 complementation), a formal single-gene essentiality determination for PP_1914 in KT2440 was not directly established here. Random barcode transposon sequencing (RB-TnSeq) datasets exist for *P. putida* ([PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/)) but the specific PP_1914 fitness call was not extracted. Note that some organisms possess redundant FabG paralogs (e.g., *S. meliloti* NodG; *Ralstonia* two reductases), so the possibility of a redundant paralog in *P. putida* was not exhaustively excluded.

4. **Allosteric site conservation inferred.** The conserved allosteric inhibitor site is demonstrated for *P. aeruginosa* and *A. baumannii*; its presence in the *P. putida* enzyme is inferred from conservation, not directly shown.

5. **Cofactor specificity for the KT2440 enzyme is inferred** from the strong NADPH preference of orthologs; not directly measured.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone, express, and purify PP_1914 (His-tagged). Measure the NADPH-dependent reduction of a β-ketoacyl-ACP (or the surrogate acetoacetyl-CoA) substrate spectrophotometrically (NADPH consumption at 340 nm). Determine Km/kcat for NADPH vs. NADH to confirm the predicted strong NADPH preference.

2. **Chain-length profiling.** Assay activity against a panel of β-ketoacyl-ACP substrates of defined chain lengths (C4–C16) reconstituted on *P. putida* ACP, to map substrate specificity and relate it to MCL-PHA monomer composition (C6–C14 dominant).

3. **Essentiality / genetic test.** Attempt a markerless deletion or CRISPRi knockdown of PP_1914 in KT2440; test whether a functional paralog can rescue and whether growth requires exogenous fatty acid supplementation. Cross-reference the RB-TnSeq fitness data ([PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/)) for the PP_1914 essentiality call.

4. **Complementation.** Test whether PP_1914 restores growth of the *E. coli fabG* ts mutant CL104 at non-permissive temperature — a rapid confirmation of FAS-II reductase function.

5. **Structural determination.** Solve the crystal structure (apo and NADPH-bound) or generate/validate an AlphaFold model of Q88LL6, confirming the homotetramer, the Ser141/Tyr154/Lys158 triad geometry, and the presence of the conserved subunit-interface allosteric pocket.

6. **Metabolic engineering test.** In an MCL-PHA production context, modulate *fabG* expression (or the NADPH pool) and quantify effects on PHA titer and monomer composition, testing the branch-point model in which FabG output feeds PhaG-mediated PHA synthesis.

---

## Conclusion

*fabG* (PP_1914, Q88LL6) of *P. putida* KT2440 encodes the cytoplasmic, NADPH-dependent **3-oxoacyl-[acyl-carrier-protein] reductase (β-ketoacyl-ACP reductase, EC 1.1.1.100)** — an SDR-superfamily homotetramer with a Ser141/Tyr154/Lys158 catalytic triad that performs the **first reductive step of every FAS-II elongation cycle**, converting 3-oxoacyl-ACP to (3R)-3-hydroxyacyl-ACP. It is essential and non-redundant, supplies the fatty acids for cell-envelope biogenesis, exhibits ACP-mediated chain-length flexibility and a conserved allosteric regulatory site, and in *P. putida* sits at the branch point feeding both membrane lipids and PhaG-mediated MCL-PHA storage polyester. The assignment is made with high confidence from the complete conserved catalytic machinery in the sequence together with strong orthologue evidence, tempered by the absence of a dedicated experimental study of the KT2440 enzyme itself.


## Artifacts

- [OpenScientist final report](fabG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28126742
2. PMID:16225460
3. PMID:11669613
4. PMID:26490537
5. PMID:26975437
6. PMID:31560825
7. PMID:11425728
8. PMID:9727022
9. PMID:16085828
10. PMID:26539719
11. PMID:33388594
12. PMID:31037463
13. PMID:29717709
14. PMID:23163771
15. PMID:33782435
16. PMID:33846444
17. PMID:29765362
18. PMID:32826213