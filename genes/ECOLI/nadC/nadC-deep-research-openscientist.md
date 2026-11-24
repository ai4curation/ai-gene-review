---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T04:16:32.961304'
end_time: '2026-11-12T04:27:15.547389'
duration_seconds: 642.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P30011
  gene_symbol: nadC
  uniprot_accession: P30011
  protein_description: 'RecName: Full=Nicotinate-nucleotide pyrophosphorylase [carboxylating];
    EC=2.4.2.19 {ECO:0000269|PubMed:8561507}; AltName: Full=Quinolinate phosphoribosyltransferase
    [decarboxylating] {ECO:0000303|PubMed:8561507}; Short=QAPRTase;'
  gene_info: Name=nadC; OrderedLocusNames=b0109, JW0105;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the NadC/ModD family. .
  protein_domains: Aldolase_TIM. (IPR013785); NadC. (IPR004393); NadC/ModD. (IPR027277);
    Nicotinate_pribotase-like_C. (IPR036068); Quinolinate_PRibosylTase_N_sf. (IPR037128)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P30011
- **Protein Description:** RecName: Full=Nicotinate-nucleotide pyrophosphorylase [carboxylating]; EC=2.4.2.19 {ECO:0000269|PubMed:8561507}; AltName: Full=Quinolinate phosphoribosyltransferase [decarboxylating] {ECO:0000303|PubMed:8561507}; Short=QAPRTase;
- **Gene Information:** Name=nadC; OrderedLocusNames=b0109, JW0105;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the NadC/ModD family. .
- **Key Domains:** Aldolase_TIM. (IPR013785); NadC. (IPR004393); NadC/ModD. (IPR027277); Nicotinate_pribotase-like_C. (IPR036068); Quinolinate_PRibosylTase_N_sf. (IPR037128)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadC" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadC** (gene ID: P30011, UniProt: P30011) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# nadC (P30011): Quinolinate Phosphoribosyltransferase — The Committed Gateway of De Novo NAD⁺ Biosynthesis in *Escherichia coli*

## Summary

The *E. coli* K-12 gene **nadC** (ordered locus names b0109 / JW0105; UniProt **P30011**) encodes **quinolinate phosphoribosyltransferase** (QAPRTase/QPRTase; EC 2.4.2.19), a soluble cytoplasmic enzyme that catalyzes the **committed, decarboxylating step of de novo NAD⁺ biosynthesis**. In a Mg²⁺-dependent, ordered reaction, NadC condenses **quinolinic acid (pyridine-2,3-dicarboxylic acid)** with **5-phospho-α-D-ribosyl-1-pyrophosphate (PRPP)** to yield **nicotinate mononucleotide (NaMN)**, with the simultaneous release of **CO₂** and **pyrophosphate (PPi)**. This reaction is the point at which the pyridine ring synthesized de novo first enters the NAD⁺ pool. The enzyme's identity, reaction, substrate specificity, and kinetics are established by direct biochemical work on the purified *E. coli* protein and corroborated in the closely related *Salmonella* ortholog ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/); [PMID: 11876660](https://pubmed.ncbi.nlm.nih.gov/11876660/)).

Mechanistically, NadC is the prototype of the **type II phosphoribosyltransferase** class. It adopts a **completely novel two-domain fold** — an N-terminal mixed α/β domain plus a C-terminal seven-stranded α/β (TIM-barrel-like) domain — and, crucially, builds each catalytic site **across a subunit interface**, so that the active site of one monomer is completed in trans by the N-terminal domain of a neighboring subunit. This architecture mandates oligomerization: the functional enzyme is an **obligate hexamer organized as a trimer of dimers**, and disrupting the dimer–dimer interface abolishes both assembly and activity. These structural principles, first defined in the *Salmonella* crystal structure, are conserved across bacterial and human orthologs ([PMID: 9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/); [PMID: 17763926](https://pubmed.ncbi.nlm.nih.gov/17763926/); [PMID: 26805589](https://pubmed.ncbi.nlm.nih.gov/26805589/)).

Biologically, NadC sits immediately **downstream of NadB (L-aspartate oxidase) and NadA (quinolinate synthase)** in the cytoplasmic de novo pathway and provides the **sole enzymatic route for quinolinate utilization**. Loss of *nadC* causes quinolinate accumulation/secretion and NAD auxotrophy, confirming it as an essential, non-redundant node. Flux into NadC is governed largely upstream by the NAD-responsive repressor **NadR**, which coordinately controls *nadA*, *nadB*, and the salvage gene *pncB*; *nadC* itself maps to a separate chromosomal region (the *guaC–nadC–aroP* cluster at ~2.5 min) and behaves as an independently expressed committed gateway. Because this step is indispensable for prokaryotic survival and has no bypass, NadC is widely regarded as an attractive antibacterial drug target ([PMID: 203571](https://pubmed.ncbi.nlm.nih.gov/203571/); [PMID: 22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/); [PMID: 2198247](https://pubmed.ncbi.nlm.nih.gov/2198247/); [PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)).

---

## Identity Verification

The target gene symbol and metadata are internally consistent and unambiguous. The gene symbol **nadC**, the UniProt description (*Nicotinate-nucleotide pyrophosphorylase [carboxylating] / Quinolinate phosphoribosyltransferase [decarboxylating], QAPRTase*; EC 2.4.2.19), the organism (*Escherichia coli* K-12), the ordered locus names (b0109 / JW0105), the **NadC/ModD protein family**, and the InterPro domain set (Aldolase_TIM; NadC; NadC/ModD; Nicotinate_pribotase-like_C; Quinolinate_PRibosylTase_N_sf) all converge on one protein. The primary literature retrieved — including direct enzymology of the *E. coli* protein ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)) and genetic mapping of E. coli K-12 *nadC* ([PMID: 3275629](https://pubmed.ncbi.nlm.nih.gov/3275629/)) — matches this identity exactly. There is **no ambiguity**: this report concerns the authentic *E. coli* K-12 QAPRTase. (Note: an unrelated plant enzyme "QPT" shares the QAPRTase activity but is a distinct gene family; it is discussed only as cross-kingdom corroboration, not as the target.)

---

## Key Findings

### F001 — NadC catalyzes the committed decarboxylating step of de novo NAD⁺ synthesis

The central function of *nadC* is enzymatic. The purified *E. coli* NadC protein catalyzes the reaction:

> **Quinolinic acid + PRPP (Mg²⁺) → Nicotinate mononucleotide (NaMN) + CO₂ + PPi**

This is a phosphoribosyl transfer coupled to **decarboxylation** of the pyridine ring: the N1 of quinolinate attacks C1 of the ribose moiety of PRPP, forming a glycosidic bond while one of quinolinate's two carboxyl groups is lost as CO₂. The result, NaMN, is the first pyridine nucleotide of the pathway and the convergence point of the de novo and salvage routes to NAD⁺. The *E. coli* study described the mechanism precisely: "the magnesium ion complex of 5-phosphoribosyl-1-pyrophosphate binds first followed by quinolinic acid. The products are pyrophosphate CO2, and nicotinate mononucleotide" ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)).

The steady-state kinetics directly define the enzyme's **substrate specificity**: the Michaelis constants are **Km = 15.6 µM for PRPP** and **Km = 6.4 µM for quinolinic acid**, indicating tight, physiologically relevant affinity for both substrates ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)). The reaction and its EC assignment (2.4.2.19) were independently confirmed in the *Salmonella typhimurium* ortholog, where QAPRTase was shown to catalyze "the formation of nicotinate mononucleotide, carbon dioxide, and pyrophosphate from 5-phosphoribosyl 1-pyrophosphate (PRPP) and quinolinic acid (QA, pyridine 2,3-dicarboxylic acid)" ([PMID: 11876660](https://pubmed.ncbi.nlm.nih.gov/11876660/)). Because this step is committed and essentially irreversible (CO₂ release makes it thermodynamically favorable), NadC defines the entry of de-novo-synthesized pyridine ring carbon into the cellular NAD⁺ economy.

### F002 — NadC is a type II PRTase with an ordered kinetic mechanism; phosphoribosyl transfer is rate-determining

Beyond the overall reaction, the *order* of events on the enzyme is well characterized. The *E. coli* enzyme follows an **ordered binding mechanism**: the **Mg·PRPP complex binds first**, followed by quinolinic acid; the product NaMN is a competitive inhibitor with respect to PRPP, consistent with both ligands occupying overlapping regions of the active site ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)).

Deeper mechanistic dissection of the *Salmonella* ortholog — "the only type II PRTase whose X-ray structure is known" — established the rate-limiting step. Equilibrium binding measurements (KD ≈ 53 µM for PRPP, ≈ 21 µM for quinolinate), isotope-trapping experiments demonstrating that the E·QA complex is catalytically competent, and pre-steady-state kinetics showing a **linear rate of NaMN formation** together indicate that **on-enzyme phosphoribosyl transfer chemistry is rate-determining** ("Pre-steady-state kinetics gave a linear rate of NAMN formation, indicating that on-enzyme phosphoribosyl transfer chemistry is rate-determining"), within a predominantly ordered mechanism ([PMID: 11876660](https://pubmed.ncbi.nlm.nih.gov/11876660/)). This places NadC firmly in the **type II PRTase** family — mechanistically and structurally distinct from the larger type I PRTase group — a classification reinforced by the structural data below.

### F003 — NadC acts downstream of NadB and NadA; its loss causes quinolinate accumulation and NAD auxotrophy

NadC's place in the pathway is defined genetically and biochemically. In the de novo route, **NadB (L-aspartate oxidase)** and **NadA (quinolinate synthase)** together synthesize quinolinate from L-aspartate and dihydroxyacetone phosphate: "Quinolinic acid (pyridine 2,3-dicarboxylic acid) which is an immediate precursor of the pyridine nucleotides, is synthesised from L-asparate and dihydroxyacetone phosphate in Escherichia coli" ([PMID: 238844](https://pubmed.ncbi.nlm.nih.gov/238844/)). NadC then converts quinolinate to NaMN. Classic genetic work in *Salmonella* demonstrated that "the product of the *nadC* locus in S. typhimurium LT-2 is the enzyme quinolinic acid phosphoribosyltransferase," and that "**all nadC mutants of S. typhimurium secreted between 2 and 8 mumol of quinolinic acid**" — direct physiological evidence that NadC is the enzyme that normally consumes quinolinate, so that in its absence the metabolite backs up and is excreted ([PMID: 203571](https://pubmed.ncbi.nlm.nih.gov/203571/)).

The essentiality of the step is underscored by the fact that "**NAD auxotrophy can be rendered by mutation in any of the three genes nadB, nadA and nadC**" ([PMID: 22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/)). This establishes NadC as a non-redundant, committed node: there is no alternative enzyme that bypasses it within the de novo pathway.

### F004 — NadC is a ~32.4 kDa, 297-residue subunit that oligomerizes; it maps to the *guaC–nadC–aroP* region at ~2.5 min

The gene encodes a **297-residue polypeptide** ("The protein predicted from this second open reading frame is 297 residues in length") with a mature mass of **32,428 Da**. When purified, the protein runs at a subunit Mr of ~35,000 by SDS-PAGE but gives a native Mr of ~72,000 by gel filtration ("Upon gel filtration, the protein gave an M(r) of 72,000, and sodium dodecyl sulfate-polyacrylamide gel electrophoresis gave a subunit M(r) of 35,000"), providing the first direct biochemical evidence that NadC **oligomerizes** ([PMID: 8419294](https://pubmed.ncbi.nlm.nih.gov/8419294/)). The 297-residue length is notably conserved across orthologs, including human QPRT, which is also 297 residues.

Genomically, "the guaC (GMP reductase), nadC (quinolinate phosphoribosyltransferase), and aroP (aromatic amino acid permease) genes of Escherichia coli K-12 were located in the **2.5-min region of the chromosome**," in the gene order *muT–guaC–nadC–aroP–aceE* ([PMID: 3275629](https://pubmed.ncbi.nlm.nih.gov/3275629/)). Importantly, this locus is **physically separate** from the *nadA*, *nadB*, and *pncB* genes, a fact relevant to its regulation (F007).

### F005 — QAPRTase is catalytically active only as a hexamer (a trimer of dimers) with inter-subunit active sites

A defining mechanistic feature of NadC is that oligomerization is not merely structural but **obligatory for catalysis**. Crystallographic studies of NadC orthologs reveal a conserved **hexameric architecture organized as a "trimer of dimers."** In *Helicobacter pylori* QAPRTase, "the enzyme exists as a hexamer organized as a trimer of dimers, which is essential for full enzymatic activity." A single point mutation at the dimer–dimer interface — **Phe181Pro in the α7–β8 loop** — "disrupts the hexamerization of QAPRTase, and the resultant dimer shows dramatically reduced protein stability and no activity," directly linking the quaternary assembly to function ([PMID: 17763926](https://pubmed.ncbi.nlm.nih.gov/17763926/)).

The same principle holds in the human ortholog, where apo and reactant/product-bound crystal structures show active sites located at the **dimer–dimer interface**, flanked by two flexible catalytic loops, with the N-terminal helix α1 stabilizing the hexamer. Human QPRT "acts as a hexamer for cooperative reactant binding via three dimeric subunits and maintaining stability" ([PMID: 26805589](https://pubmed.ncbi.nlm.nih.gov/26805589/)). The conservation of this feature from bacteria to humans indicates it is a fundamental, ancient property of the enzyme family.

### F006 — NadC is the sole route for quinolinate utilization and an attractive antibacterial target

Because NadC is the only enzyme that consumes quinolinate en route to NAD⁺, it occupies a uniquely non-redundant position. In *H. pylori*, "Quinolinic acid phosphoribosyltransferase (QAPRTase; NadC) catalyzes an indispensable step in NAD biosynthesis, one that is essential for cell survival in prokaryotes, which makes it an attractive target for antibacterial drug therapy" ([PMID: 17763926](https://pubmed.ncbi.nlm.nih.gov/17763926/)). In group A streptococci, "the quinolinate (Qa) phosphoribosyltransferase activity of NadC from S. pyogenes allows the organism to sustain growth when Qa is present as a sole pyridine precursor," even in backgrounds lacking the rest of the de novo machinery — defining NadC as the unique, indispensable gateway for quinolinate salvage into NAD⁺ ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)). The absence of any bypass enzyme is what makes the step both metabolically essential and pharmacologically attractive.

### F007 — Flux into NadC is set upstream by NAD-responsive NadR repression; *nadC* itself is at an independent locus

Regulation of de novo NAD⁺ synthesis is imposed primarily *upstream* of NadC. The **NAD-sensing transcriptional repressor NadR** coordinately represses the de novo genes *nadA* and *nadB* and the salvage gene *pncB* in response to intracellular NAD levels: "de novo synthesis of NAD is regulated through the transcriptional control of the nadA and nadB loci. Likewise, the pyridine nucleotide salvage pathway is controlled at pncB. The transcriptional expression of these three loci is coordinately regulated by the product of nadR" ([PMID: 2198247](https://pubmed.ncbi.nlm.nih.gov/2198247/)). NadR is a **trifunctional protein** whose N-terminal DNA-binding domain "represses transcription of genes for NAD synthesis and salvage," gated by an NAD-responsive central/adenylyltransferase domain ([PMID: 15805524](https://pubmed.ncbi.nlm.nih.gov/15805524/)). More recently, the second messenger **c-di-GMP** was shown to bind NadR and "upregulate NAD biosynthesis by activating NadR-repressed genes," adding another layer of de-repression control ([PMID: 40823837](https://pubmed.ncbi.nlm.nih.gov/40823837/)).

Critically, *nadC* is **not** among the genes named as NadR targets, and it maps to a separate chromosomal region (*guaC–nadC–aroP*; [PMID: 3275629](https://pubmed.ncbi.nlm.nih.gov/3275629/)). This supports a model in which the *supply* of quinolinate (via NadR-controlled *nadA/nadB*) is the primary regulatory lever, while *nadC* is expressed as a comparatively constitutive, committed gateway that converts whatever quinolinate is produced.

### F008 — QAPRTase adopts a novel two-domain fold with the active site built across the subunit interface

The structural basis for all of the above was established by the crystal structures of *Salmonella typhimurium* QAPRTase at 2.8 Å (quinolinate-bound) and 3.0 Å (NaMN-bound). These revealed that "the enzyme shows a completely novel fold for a PRTase enzyme comprising a two-domain structure: a mixed alpha/beta N-terminal domain and an alpha/beta barrel-like domain containing seven beta strands." The **active site is located at the C-terminal ends of the β strands of the α/β barrel** and "is bordered by the N-terminal domain of the second subunit of the dimer" — the structural explanation for why the enzyme must oligomerize to function ([PMID: 9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/)).

The structure also explains the type I vs. type II distinction: "A conserved sequence motif of 13 residues is common to these 'type I' PRTases but is not observed in the QAPRTase sequence, suggestive of a different fold for this enzyme," confirming that NadC belongs to a structurally separate class. These features map directly onto the InterPro domain annotations assigned to P30011 — the **Quinolinate_PRibosylTase_N_sf / Aldolase_TIM** (N-terminal) and **Nicotinate_pribotase-like_C** (C-terminal barrel) domains — providing structural grounding for the database annotations.

---

## Mechanistic Model / Interpretation

### The reaction and pathway context

NadC occupies the pivotal junction where de-novo-synthesized pyridine ring carbon enters the universal NAD⁺ pool:

```
 L-Aspartate + DHAP
      │
      │  NadB (L-aspartate oxidase) → iminoaspartate
      │  NadA (quinolinate synthase)
      ▼
  QUINOLINATE  ──────────────┐  (secreted/accumulated when nadC is lost)
      │                      │
      │  NadC (QAPRTase, EC 2.4.2.19)
      │  + PRPP, Mg²⁺
      │  − CO₂, − PPi
      ▼
  NICOTINATE MONONUCLEOTIDE (NaMN)  ◄── convergence with salvage (PncB)
      │
      │  NadD (NaMN adenylyltransferase)
      ▼
  NICOTINATE ADENINE DINUCLEOTIDE (NaAD)
      │
      │  NadE (NAD synthetase)
      ▼
     NAD⁺
```

NaMN is the metabolic hub at which the de novo pathway (via NadC) and the salvage pathway (via PncB, nicotinate phosphoribosyltransferase) converge; downstream, NadD and NadE complete the synthesis of NAD⁺. NadC is therefore the de-novo-specific entry valve.

### Ordered catalytic cycle

```
 E ──(+Mg·PRPP)──► E·Mg·PRPP ──(+QA)──► E·Mg·PRPP·QA
                                             │
                                             │  phosphoribosyl transfer
                                             │  (RATE-DETERMINING) + decarboxylation
                                             ▼
                               E·NaMN·CO₂·PPi ──► E + NaMN + CO₂ + PPi
```

Mg·PRPP binds first; quinolinate binds second; the chemical phosphoribosyl-transfer/decarboxylation step is slowest; NaMN release regenerates free enzyme. NaMN product inhibition is competitive versus PRPP, consistent with overlapping binding determinants.

### Quaternary architecture (why oligomerization is obligatory)

| Feature | Description | Evidence |
|---|---|---|
| Monomer fold | Two domains: N-terminal mixed α/β; C-terminal 7-stranded α/β barrel | [PMID: 9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/) |
| Active site location | C-terminal ends of barrel β-strands, completed *in trans* by N-terminal domain of the neighboring subunit | [PMID: 9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/) |
| Functional oligomer | Hexamer = "trimer of dimers" | [PMID: 17763926](https://pubmed.ncbi.nlm.nih.gov/17763926/); [PMID: 26805589](https://pubmed.ncbi.nlm.nih.gov/26805589/) |
| Assembly–activity coupling | Phe181Pro at α7–β8 dimer–dimer interface → loss of hexamer, destabilization, no activity | [PMID: 17763926](https://pubmed.ncbi.nlm.nih.gov/17763926/) |
| PRTase class | Type II (lacks the 13-residue type I motif) | [PMID: 9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/); [PMID: 11876660](https://pubmed.ncbi.nlm.nih.gov/11876660/) |

Because each catalytic site is assembled from two subunits, the enzyme cannot function as a monomer. The *E. coli* protein's native Mr of ~72,000 observed by gel filtration ([PMID: 8419294](https://pubmed.ncbi.nlm.nih.gov/8419294/)) reflects this obligate oligomerization, which the ortholog crystal structures resolve as a hexamer.

### Localization

NadC is a **soluble cytoplasmic** enzyme. It carries no signal peptide or membrane-spanning segments, its substrates (quinolinate, PRPP, Mg²⁺) and product (NaMN) are cytosolic metabolites, and its purification as a soluble protein and function in the cytoplasmic de novo pathway all place its activity in the **cytoplasm**.

### Regulatory logic

Flux through NadC is controlled chiefly by substrate supply. The NAD-responsive repressor **NadR** throttles *nadA/nadB* (quinolinate production) and *pncB* (salvage) when NAD⁺ is plentiful, with c-di-GMP providing a de-repressing input. *nadC*, residing at an independent locus and absent from the core NadR regulon, behaves as a comparatively constitutive committed gateway — the cell regulates how much quinolinate is made more than how much NadC is present.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/) | *Sequencing, expression, purification, steady-state kinetics of QAPRTase from E. coli* | **Primary E. coli enzymology**: defines reaction, ordered Mg·PRPP-first mechanism, Km (15.6 µM PRPP; 6.4 µM QA); NaMN competitive inhibition |
| [11876660](https://pubmed.ncbi.nlm.nih.gov/11876660/) | *QAPRTase: kinetic mechanism for a type II PRTase* | Confirms reaction/EC in Salmonella; identifies type II class; rate-determining phosphoribosyl transfer via pre-steady-state kinetics and isotope trapping |
| [9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/) | *A new function for a common fold: crystal structure of QAPRTase* | **Structure**: novel two-domain fold; inter-subunit active site; lacks type I motif |
| [8419294](https://pubmed.ncbi.nlm.nih.gov/8419294/) | *The Salmonella nadC gene; purification of QAPRTase* | 297-residue subunit; native Mr ~72 kDa vs subunit ~35 kDa → oligomerization |
| [3275629](https://pubmed.ncbi.nlm.nih.gov/3275629/) | *guaC–nadC–aroP region of E. coli K-12* | **Genomic localization** of E. coli K-12 nadC (2.5 min); gene identity |
| [203571](https://pubmed.ncbi.nlm.nih.gov/203571/) | *Mapping/characterization of nad genes in Salmonella* | nadC product = QAPRTase; nadC mutants secrete 2–8 µmol quinolinate |
| [238844](https://pubmed.ncbi.nlm.nih.gov/238844/) | *De novo NAD biosynthesis in E. coli (NadB/NadA)* | Defines upstream origin of quinolinate (NadC substrate) |
| [22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/) | *Nicotinamide dependence of UPEC; nadB insertion site* | Mutation of nadB/nadA/nadC each causes NAD auxotrophy |
| [17763926](https://pubmed.ncbi.nlm.nih.gov/17763926/) | *Phe181 in hexamerization of H. pylori QAPRTase* | Hexamer (trimer of dimers) required; interface mutation abolishes activity; drug-target rationale |
| [26805589](https://pubmed.ncbi.nlm.nih.gov/26805589/) | *Quaternary catalytic mechanism of hexameric human QPRT* | Confirms inter-subunit active sites and functional hexamer in a eukaryotic ortholog |
| [23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/) | *Quinolinate salvage in group A streptococci* | NadC is the unique enzyme enabling growth on quinolinate as sole precursor |
| [2198247](https://pubmed.ncbi.nlm.nih.gov/2198247/) | *nadR regulator and nadA-pnuC operon* | NadR coordinately represses nadA, nadB, pncB (upstream of NadC) |
| [15805524](https://pubmed.ncbi.nlm.nih.gov/15805524/) | *Trifunctional NadR protein of Salmonella* | NadR N-terminal domain represses NAD synthesis/salvage genes |
| [40823837](https://pubmed.ncbi.nlm.nih.gov/40823837/) | *c-di-GMP regulates NAD biosynthesis via NadR* | Second-messenger de-repression of NadR-controlled genes upstream of NadC |

**Cross-kingdom corroboration.** The functional conservation of NadC is striking: the *E. coli nadC* mutant has been used as a universal complementation host, where introduction of human brain QPRT cDNA ([PMID: 9473669](https://pubmed.ncbi.nlm.nih.gov/9473669/)), plant *Nicotiana* QPT genes ([PMID: 22525250](https://pubmed.ncbi.nlm.nih.gov/22525250/)), and bacterial orthologs all restore QAPRTase activity and NAD prototrophy. Conversely, overexpression of *E. coli nadC* in *Arabidopsis* enables inducible NAD overproduction ([PMID: 22268572](https://pubmed.ncbi.nlm.nih.gov/22268572/)). These experiments confirm that NadC's function is portable and conserved "beyond the phylogenic boundary."

**Consistency assessment.** The evidence base is internally consistent and mutually reinforcing. The reaction defined biochemically in *E. coli* ([PMID: 8561507](https://pubmed.ncbi.nlm.nih.gov/8561507/)) matches the Salmonella mechanism ([PMID: 11876660](https://pubmed.ncbi.nlm.nih.gov/11876660/)), the Salmonella structure ([PMID: 9016724](https://pubmed.ncbi.nlm.nih.gov/9016724/)), and the hexamer requirement seen in *H. pylori* and human orthologs. No paper in the reviewed set contradicts the core functional annotation.

---

## Limitations and Knowledge Gaps

1. **Structure of the *E. coli* protein specifically.** The definitive crystal structures are of the **Salmonella**, **H. pylori**, and **human** orthologs. While *E. coli* NadC shares very high sequence identity with the Salmonella enzyme and all functional/kinetic data agree, no high-resolution structure of the *E. coli* K-12 protein itself is cited here. The inferred hexameric assembly for *E. coli* rests on ortholog structures plus the native-mass evidence.

2. **Oligomeric state ambiguity from early biophysics.** The *E. coli* gel-filtration estimate (~72 kDa, roughly a dimer; [PMID: 8419294](https://pubmed.ncbi.nlm.nih.gov/8419294/)) does not by itself establish the hexamer; the hexameric "trimer of dimers" conclusion derives from crystallography of orthologs. The apparent discrepancy may reflect concentration-dependent assembly or gel-filtration limitations rather than a true difference.

3. **Active-site residue mapping in *E. coli*.** The specific catalytic/substrate-binding residues of P30011 (e.g., those contacting PRPP, the Mg²⁺, and the quinolinate carboxylates) are inferred from ortholog structures rather than directly mutagenized in the *E. coli* protein in the reviewed literature.

4. **Regulation of *nadC* itself.** The evidence shows NadR controls *nadA/nadB/pncB* and that *nadC* lies outside this regulon, but the reviewed literature does not fully define whether/how *nadC* transcription responds to NAD status, growth phase, or stress. Its "constitutive gateway" characterization is a reasonable inference, not a directly measured expression profile.

5. **Quantitative flux control.** Whether NadC activity is ever flux-limiting in vivo (versus quinolinate supply) has not been directly quantified here.

6. **Post-translational and interaction data.** No information on metabolic channeling, protein–protein interactions, or regulatory modifications of *E. coli* NadC was found in the reviewed set.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the *E. coli* K-12 NadC structure (apo + QA/PRPP/NaMN complexes)** by X-ray crystallography or cryo-EM to confirm the hexameric "trimer of dimers" assembly directly for P30011 and map its active-site residues, rather than inferring from orthologs.

2. **Determine the oligomeric state in solution** by SEC-MALS and/or analytical ultracentrifugation across a concentration range to reconcile the ~72 kDa gel-filtration estimate with the expected hexamer and to test for concentration-dependent assembly.

3. **Alanine-scanning mutagenesis of predicted catalytic/interface residues** (including the *E. coli* equivalent of the Phe181 dimer–dimer interface position) to confirm both catalytic determinants and the assembly–activity coupling in the *E. coli* enzyme.

4. **Measure *nadC* transcription dynamics** (RT-qPCR / reporter fusions / RNA-seq) across NAD-replete vs. NAD-limited conditions, growth phases, and stress, and directly test for NadR binding at the *nadC* promoter to resolve whether *nadC* is truly outside NadR control.

5. **In vivo ¹³C/¹⁵N metabolic flux analysis** of the de novo pathway to quantify whether NadC is ever rate-limiting relative to quinolinate supply.

6. **Structure-guided inhibitor screening** against *E. coli* NadC, exploiting the inter-subunit active site and the obligate dimer–dimer interface (a potential allosteric/assembly-disruption site) as antibacterial strategies, building on the drug-target rationale from the *H. pylori* and group A streptococcal work.

---

## Conclusion

The functional annotation of *E. coli* **nadC (P30011)** is secure and well-evidenced. It encodes **quinolinate phosphoribosyltransferase (QAPRTase, EC 2.4.2.19)**, the soluble cytoplasmic, obligate-hexameric **type II PRTase** that catalyzes the committed, decarboxylating, Mg²⁺-dependent conversion of **quinolinate + PRPP → NaMN + CO₂ + PPi**. It is the indispensable, non-redundant gateway through which de-novo-synthesized (and salvaged) quinolinate enters the NAD⁺ pool, acting immediately downstream of NadB/NadA, with its active sites built across subunit interfaces and flux into the step governed largely by NadR-controlled quinolinate supply upstream.


## Artifacts

- [OpenScientist final report](nadC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8561507
2. PMID:11876660
3. PMID:9016724
4. PMID:17763926
5. PMID:26805589
6. PMID:22174382
7. PMID:2198247
8. PMID:23204464
9. PMID:3275629
10. PMID:8419294
11. PMID:15805524
12. PMID:40823837
13. PMID:9473669
14. PMID:22525250
15. PMID:22268572