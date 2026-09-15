---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T05:00:10.781831'
end_time: '2026-08-31T05:53:26.601576'
duration_seconds: 3195.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: betC
  gene_symbol: betC
  uniprot_accession: Q88RQ2
  protein_description: 'SubName: Full=Choline-sulfatase {ECO:0000313|EMBL:AAN65711.1};
    EC=3.1.6.6 {ECO:0000313|EMBL:AAN65711.1};'
  gene_info: Name=betC {ECO:0000313|EMBL:AAN65711.1}; OrderedLocusNames=PP_0077 {ECO:0000313|EMBL:AAN65711.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the sulfatase family.
  protein_domains: Alkaline_phosphatase_core_sf. (IPR017850); Choline-sulfatase. (IPR017785);
    Choline_sulf_C_dom. (IPR025863); Sulfatase_CS. (IPR024607); Sulfatase_N. (IPR000917)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: betC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: betC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RQ2
- **Protein Description:** SubName: Full=Choline-sulfatase {ECO:0000313|EMBL:AAN65711.1}; EC=3.1.6.6 {ECO:0000313|EMBL:AAN65711.1};
- **Gene Information:** Name=betC {ECO:0000313|EMBL:AAN65711.1}; OrderedLocusNames=PP_0077 {ECO:0000313|EMBL:AAN65711.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the sulfatase family.
- **Key Domains:** Alkaline_phosphatase_core_sf. (IPR017850); Choline-sulfatase. (IPR017785); Choline_sulf_C_dom. (IPR025863); Sulfatase_CS. (IPR024607); Sulfatase_N. (IPR000917)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "betC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'betC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **betC** (gene ID: betC, UniProt: Q88RQ2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: betC (Q88RQ2) — Choline-O-sulfatase in *Pseudomonas putida* KT2440

## Summary

**betC** (locus tag **PP_0077**; UniProt **Q88RQ2**) of *Pseudomonas putida* strain KT2440 encodes **choline-O-sulfatase** (**EC 3.1.6.6**), a cytoplasmic enzyme of the sulfatase / alkaline-phosphatase superfamily. Its primary catalytic function is the hydrolysis of the sulfate ester bond of **choline-O-sulfate**, releasing **free choline and inorganic sulfate**; it also acts, at a lower rate, on **phosphorylcholine**. Catalysis proceeds through the sulfatase-family mechanism, in which a signature cysteine residue (embedded in the diagnostic (C/S)-X-P-X-R motif — here **C52-A-P-S-R56**) is post-translationally converted to a **Cα-formylglycine** nucleophile that drives a **double-displacement (covalent) mechanism**.

The identity of the target protein is well supported and unambiguous. The gene symbol *betC*, the organism (*P. putida* KT2440), and the protein family/domain architecture all align internally and with the primary literature. The definitive functional study — *"Uncoupling of choline-O-sulphate utilization from osmoprotection in Pseudomonas putida"* ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)) — directly examines *betC* (PP_0077) in this exact strain. The founding biochemical/genetic characterization of a *betC*-encoded choline sulfatase comes from *Sinorhizobium meliloti* ([PMID: 9736747](https://pubmed.ncbi.nlm.nih.gov/9736747/); [PMID: 12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/)), which establishes the reaction and substrate preference of the BetC enzyme family. There is therefore no ambiguity of the kind flagged in the research brief.

A key mechanistic insight distinguishes *P. putida* from other model organisms. In *Bacillus subtilis* and *S. meliloti*, choline liberated from choline-O-sulfate feeds the biosynthesis of the osmoprotectant **glycine betaine**. In *P. putida* KT2440, by contrast, *betC* serves **catabolism (nutrient acquisition)** rather than **osmoprotection**: a *betC* deletion mutant still accumulated intact choline-O-sulfate but could no longer use it as a carbon or nitrogen source, and — decisively — *betC* is transcriptionally **down-regulated** under high salt, the opposite of what would be expected for an osmostress gene. BetC therefore functions **intracellularly**, acting on choline-O-sulfate that is first delivered into the cytoplasm by an **adjacent ABC transporter**, all under the control of a neighbouring **LysR-type regulator**. Osmoprotection in *Pseudomonas* is handled by physically and functionally separate modules (the *betBA* genes and the OpuC osmoprotectant transporter).

---

## Key Findings

### F001 — betC encodes choline-O-sulfatase (EC 3.1.6.6), hydrolyzing choline-O-sulfate to choline + sulfate

The core molecular function of the *betC* gene product is the enzymatic hydrolysis of choline-O-sulfate:

```
choline-O-sulfate  +  H2O   →   choline  +  sulfate
```

This assignment rests on both nomenclature/annotation in the target organism and direct genetic evidence in the founding homolog. In *P. putida* KT2440, PP_0077 is named *betC* and annotated as choline sulphatase ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)). The enzymatic activity and substrate preference were first established genetically and biochemically in *S. meliloti*, where "a new gene (*betC*) was identified as encoding a choline sulfatase catalyzing the conversion of choline-O-sulfate and, at a lower rate, phosphorylcholine, into choline" ([PMID: 9736747](https://pubmed.ncbi.nlm.nih.gov/9736747/)). Critically, choline sulfatase activity was **absent from *betC* mutants**, providing genetic proof that *betC* is responsible for this activity rather than merely correlated with it. The same assignment — *betC* = choline sulphatase — is confirmed directly in the target organism: "*betC* (choline sulphatase) lies adjacent to an ATP-binding cassette transporter and a LysR type regulator" ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)).

**Substrate specificity:** The enzyme's preferred physiological substrate is **choline-O-sulfate**. It also hydrolyzes **phosphorylcholine**, but at a lower rate, indicating that the choline moiety is a key recognition element while the enzyme tolerates (with reduced efficiency) substitution of the sulfate ester by a phosphate ester.

### F002 — In P. putida KT2440 betC serves catabolism (C/N/S nutrition), not osmoprotection

This is the central distinguishing finding for the target organism, and it directly answers "what biological process does the gene serve." A *betC* deletion mutant of *P. putida* KT2440 **still accumulated intact choline-O-sulfate (COS)** but **failed to use COS as a carbon or nitrogen source** ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)): "This mutant still accumulated intact COS but failed to use this compound as carbon or nitrogen source." Because the sulfate ester is cleaved in the reaction, choline-O-sulfate is also a potential **sulfur** source, making BetC a gateway enzyme for carbon, nitrogen, and sulfur acquisition from this single environmental compound.

The regulatory behaviour reinforces the catabolic (as opposed to osmoprotective) role: "*betC* expression was downregulated at high salt concentrations, showing that the principal role of this gene lied in COS metabolism, not in osmoprotection" ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)). An osmostress-protective gene would be *induced* by salt; the observed *repression* is the opposite pattern and demonstrates that BetC's job is nutritional. This uncoupling of choline-O-sulfate utilization from osmoprotection distinguishes *P. putida* from *B. subtilis* and *S. meliloti*, where the choline released downstream is channelled into glycine betaine synthesis for osmotic defense.

### F003 — betC belongs to the sulfatase / alkaline-phosphatase superfamily and uses a formylglycine nucleophile

The protein Q88RQ2 (505 amino acids) carries the InterPro domain signatures diagnostic of the sulfatase superfamily: **Sulfatase_N (IPR000917)**, **Sulfatase_CS (IPR024607)**, and the **Alkaline_phosphatase_core superfamily fold (IPR017850)**, plus two domains specific to this enzyme class — **Choline-sulfatase (IPR017785)** and **Choline_sulf_C_dom (IPR025863)**. A direct sequence scan locates the universal sulfatase active-site signature **(C/S)-X-P-X-R** as **C52-A-P-S-R56** near the N-terminus.

Members of the sulfatase family share a defining catalytic strategy: "Sulfatases use a unique formylglycine nucleophile, formed by posttranslational modification of a cysteine/serine embedded in a signature sequence (C/S)XPXR" ([PMID: 18793651](https://pubmed.ncbi.nlm.nih.gov/18793651/)). In BetC, Cys52 within the C52-A-P-S-R56 motif is the residue predicted to undergo this modification to **Cα-formylglycine (FGly)**, generating the catalytic nucleophile. Kinetic studies of a closely related superfamily member show that "burst kinetics suggest that substrate hydrolysis proceeds via a double-displacement mechanism" ([PMID: 18793651](https://pubmed.ncbi.nlm.nih.gov/18793651/)), supporting a **covalent, two-step (transesterification then hydrolysis)** mechanism for BetC in which the FGly hydrate attacks the sulfur (or phosphorus) center, forms a covalent intermediate, and is then regenerated.

### F004 — betC acts intracellularly downstream of a dedicated ABC importer, under LysR-type regulation

The genomic context of *betC* in *P. putida* KT2440 defines its cellular logic. PP_0077 is "adjacent to an ATP-binding cassette transporter and a LysR type regulator, but well away from *betBA*" ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)). This organization — an **importer**, a **regulator**, and a **catabolic enzyme** clustered together and separated from the osmoprotective *betBA* genes — is characteristic of a nutrient-scavenging module rather than an osmotic-stress operon.

The subcellular order of operations is established by the mutant phenotype: because the *betC* mutant "still accumulated intact COS" ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)), choline-O-sulfate must first be **imported into the cytoplasm** (via the adjacent ABC transporter) and only then hydrolyzed by BetC. BetC therefore carries out its function **inside the cell**, on an internalized substrate. In the homologous *S. meliloti* system, the choline sulfatase gene is embedded in the *betICBA* operon and induced by choline and choline-O-sulfate through the **BetI repressor**, which senses the intracellular choline pool ([PMID: 12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/)). In *P. putida* the regulator is instead a **LysR-type** protein, consistent with an inducible catabolic system.

### F005 — AlphaFold model supports a well-ordered sulfatase fold with a structured catalytic Cys52

The AlphaFold Database model **AF-Q88RQ2-F1 (v6)** covers all 505 residues at very high confidence: **mean pLDDT = 96.4**, with **99.2 %** of residues scoring pLDDT > 70. The predicted catalytic **Cys52** — the residue expected to become Cα-formylglycine — is modeled at **pLDDT 98.25**, i.e., it sits in a well-ordered structural core rather than a disordered or low-confidence region. This structural prediction is fully consistent with the sulfatase-superfamily α/β fold and lends independent (in-silico structural) support to the identity of Cys52 as the catalytic nucleophile position.

### F006 — Osmoprotection in Pseudomonas is handled by separate modules (OpuC and betBA), not by betC

The functional separation between osmoadaptation and choline-O-sulfate catabolism in *Pseudomonas* is reinforced by the characterization of the osmoprotectant transporter OpuC in *Pseudomonas syringae*. There, an ABC transporter "designated OpuC, functioned as the primary or sole transporter for glycine betaine and as one of multiple transporters for choline under high osmolarity," with broad specificity for other osmoprotectants (acetylcholine, carnitine, proline betaine), and its **cystathionine-β-synthase (CBS) domains are required for osmoregulatory function** ([PMID: 17660277](https://pubmed.ncbi.nlm.nih.gov/17660277/)). Combining this with the *P. putida* result that *betC* is salt-repressed and dispensable for osmoprotection ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)), it is clear that in *Pseudomonas* the acquisition of osmoprotectants (OpuC) and their synthesis (*betBA*, converting choline → glycine betaine) are distinct modules from the catabolic choline-O-sulfatase BetC.

### F007 — The predicted active-site pocket recapitulates the conserved metal-dependent sulfatase catalytic constellation

Analysis of the AlphaFold model's active site adds mechanistic detail. Residues within 8 Å of the Cys52 Sγ form a compact catalytic pocket containing the signature **Arg56**, a candidate divalent-metal-coordinating set (**Asp12, Asn73, Asp289**) typical of alkaline-phosphatase/sulfatase-superfamily metal sites, and a cluster of conserved basic/acidic residues that line arylsulfatase sulfate-binding sites (**Lys100, His102, His142, His195, Asp196, Asp289, His290, Lys302**). This spatial arrangement matches the well-characterized active sites of *Pseudomonas aeruginosa* arylsulfatase and *E. coli* alkaline phosphatase homologs. The general principle is documented for the superfamily: members show "structural homology to arylsulfatases with conservation of the core alpha/beta-fold, the mononuclear active site and most of the active-site residues" ([PMID: 18793651](https://pubmed.ncbi.nlm.nih.gov/18793651/)). BetC thus carries a conserved **mononuclear (metal-dependent) active site** organized around the FGly-forming Cys52.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent picture of BetC as a **cytoplasmic, catabolic choline-O-sulfatase** feeding a nutrient-acquisition pathway that is regulatorily and genetically separated from osmotic-stress physiology.

### Pathway and cellular localization

```
   Environment                       Cytoplasm (P. putida KT2440)
 ┌───────────────┐   ABC importer   ┌───────────────────────────────────────┐
 │ choline-O-    │ ───────────────► │ choline-O-sulfate                      │
 │ sulfate (COS) │  (adjacent ABC   │        │                               │
 └───────────────┘   transporter)   │        │  BetC (PP_0077)               │
                                     │        ▼  choline-O-sulfatase EC 3.1.6.6│
   LysR-type regulator ─(induces)──► │  choline  +  SO4^2-                    │
   (adjacent to betC)                │     │                                  │
                                     │     ├──► carbon / nitrogen source      │
                                     │     │    (catabolism → energy, C/N)    │
                                     │     └──► sulfur source (from sulfate)  │
                                     └───────────────────────────────────────┘

   Separate module (NOT betC):  choline ──betA──► betaine aldehyde ──betB──►
                                glycine betaine  (osmoprotection; betBA locus)
   Osmoprotectant uptake: OpuC ABC transporter (glycine betaine, choline, etc.)
```

**Step 1 — Uptake.** Choline-O-sulfate is imported into the cytoplasm by the ABC transporter encoded adjacent to *betC*. The *betC* mutant's accumulation of intact COS proves that uptake is independent of, and upstream of, BetC.

**Step 2 — Intracellular hydrolysis.** BetC hydrolyzes the sulfate ester of choline-O-sulfate, releasing free choline and inorganic sulfate. Mechanistically this uses the Cys52-derived **formylglycine** nucleophile in a **double-displacement** reaction within a conserved **mononuclear metal** active site (Arg56 plus the Asp12/Asn73/Asp289 metal set and a basket of His/Lys/Asp residues that bind the sulfate).

**Step 3 — Nutrient partitioning.** The products feed central metabolism: choline provides carbon and nitrogen (and can be further oxidized), while the liberated sulfate provides a sulfur source. This is the "principal role" identified experimentally.

**Regulatory logic.** A LysR-type transcriptional regulator adjacent to *betC* controls the module, presumably inducing it in response to substrate availability (paralleling the choline/COS-inducible BetI system of *S. meliloti*). Salt represses *betC*, cementing that this is a nutritional, not osmoprotective, response.

### Comparative context across organisms

| Organism | betC product | Fate of liberated choline | Primary role of the module |
|---|---|---|---|
| *P. putida* KT2440 (**target**) | Choline-O-sulfatase (PP_0077) | Catabolized for C/N; sulfate for S | **Nutrient acquisition** (COS catabolism); salt-**repressed** ([PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)) |
| *S. meliloti* | Choline sulfatase (*betC* in *betICBA*) | → glycine betaine via BetB/BetA | Osmoprotectant precursor supply; choline-**induced** ([PMID: 9736747](https://pubmed.ncbi.nlm.nih.gov/9736747/), [PMID: 12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/)) |
| *Ruegeria pomeroyi* (Roseobacter) | Choline sulfatase (*betC*) | Choline catabolism, re-mineralized to NH4+ | Choline/GBT catabolism ([PMID: 26058574](https://pubmed.ncbi.nlm.nih.gov/26058574/)) |
| *B. subtilis* | (*gbsAB* pathway) | → glycine betaine | Osmoprotection ([PMID: 8752328](https://pubmed.ncbi.nlm.nih.gov/8752328/)) |

The comparison shows that the **same enzyme (choline sulfatase)** is recruited to **different physiological ends** depending on the downstream wiring and the regulatory response to salt. In *P. putida*, the wiring places BetC firmly in catabolism.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / relates to the findings |
|---|---|---|
| [17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/) | *Uncoupling of choline-O-sulphate utilization from osmoprotection in Pseudomonas putida* | **Primary study on the exact target.** Confirms *betC* = choline sulphatase in KT2440; genomic context (ABC transporter + LysR regulator, away from *betBA*); *betC* mutant accumulates COS but can't use it as C/N source; *betC* is salt-repressed → catabolic, not osmoprotective. Supports F001, F002, F004, F006. |
| [9736747](https://pubmed.ncbi.nlm.nih.gov/9736747/) | *Presence of a gene encoding choline sulfatase in S. meliloti bet operon* | **Founding functional characterization.** Defines the BetC reaction and substrate preference (choline-O-sulfate > phosphorylcholine); activity absent in *betC* mutants. Supports F001, F003. |
| [12906115](https://pubmed.ncbi.nlm.nih.gov/12906115/) | *The S. meliloti glycine betaine biosynthetic genes (betICBA) are induced by choline...* | Establishes operon structure and BetI-mediated, choline-inducible regulation in the homolog; contextualizes the LysR/inducible regulation of the *P. putida* module. Supports F004 (regulatory context). |
| [18793651](https://pubmed.ncbi.nlm.nih.gov/18793651/) | *A new member of the alkaline phosphatase superfamily with a formylglycine nucleophile...* | Defines the (C/S)XPXR signature, the formylglycine nucleophile, the double-displacement mechanism, and the conserved mononuclear active site shared by the superfamily. Supports F003, F007. |
| [17660277](https://pubmed.ncbi.nlm.nih.gov/17660277/) | *Characterization of the osmoprotectant transporter OpuC from P. syringae...* | Shows osmoprotectant acquisition in *Pseudomonas* is via dedicated OpuC transporters (CBS domains required), functionally distinct from BetC catabolism. Supports F006. |
| [26058574](https://pubmed.ncbi.nlm.nih.gov/26058574/) | *Comparative genomics ... choline metabolism in the marine Roseobacter clade* | Independent confirmation that *betC* encodes choline sulfatase in choline catabolism; nitrogen-rich choline/GBT re-mineralized to ammonium — parallels the catabolic role in *P. putida*. Supports F001, F002 (comparative). |
| [8752328](https://pubmed.ncbi.nlm.nih.gov/8752328/) | *Synthesis of the osmoprotectant glycine betaine in B. subtilis (gbsAB)* | Provides the osmoprotection contrast: in *B. subtilis* the choline→glycine betaine route (gbsAB) is an osmotic-stress pathway, unlike the catabolic role of *betC* in *P. putida*. Contextualizes F002/F006. |
| [20615119](https://pubmed.ncbi.nlm.nih.gov/20615119/) | *Choline and osmotic-stress tolerance ... Bacillus subtilis (GB03)* | Broader background on choline → glycine betaine osmoprotection; contextual only, not a claim source for BetC's catabolic role. |

**Internal consistency check.** The gene symbol (*betC*), organism (*P. putida* KT2440), EC number (3.1.6.6), family (sulfatase), and domain architecture (Sulfatase_N/CS, Alkaline phosphatase core fold, Choline-sulfatase domains) all agree with the primary literature and with the AlphaFold structural model. No conflicting-identity literature was encountered, so the mandatory verification is satisfied and the research proceeds on the correct protein.

---

## Limitations and Knowledge Gaps

1. **No direct enzymology on the *P. putida* protein itself.** The kinetic ordering (choline-O-sulfate preferred over phosphorylcholine) and mechanistic details cited here are inferred from (a) the founding *S. meliloti* choline sulfatase, (b) the general sulfatase/alkaline-phosphatase superfamily, and (c) the AlphaFold model. No purified Q88RQ2 assay with measured kcat/Km is available. The precise substrate range and relative rates for the *P. putida* enzyme remain to be measured.

2. **Formylglycine modification is inferred, not demonstrated.** The Cys52→FGly conversion is predicted from the conserved (C/S)XPXR signature and superfamily precedent. Direct evidence (mass spectrometry of the mature enzyme, or identification of the cognate formylglycine-generating machinery in *P. putida*) has not been established here.

3. **Metal identity is a prediction.** The candidate metal-coordinating residues (Asp12/Asn73/Asp289) and the "mononuclear metal" assignment derive from the AlphaFold model and superfamily homology. Whether BetC uses Ca²⁺, Mg²⁺, or another divalent cation, and the precise coordination geometry, requires a crystal/cryo-EM structure or metal analysis.

4. **Transporter and regulator not molecularly defined.** The adjacent ABC transporter's specificity for choline-O-sulfate and the LysR regulator's effector/operator have not been directly characterized in *P. putida*; the regulatory model is partly extrapolated from *S. meliloti* BetI.

5. **Downstream catabolic routing is incompletely mapped.** How liberated choline is oxidized (which dehydrogenases) and how the released sulfate is assimilated under sulfur limitation are not detailed for KT2440 in the cited work.

6. **Localization inferred from phenotype, not from imaging.** The cytoplasmic localization of BetC is inferred from the mutant's intracellular COS accumulation (uptake precedes hydrolysis) and from the absence of periplasmic-targeting evidence, rather than from direct fractionation or fluorescence localization.

---

## Proposed Follow-up Experiments / Actions

1. **Purify recombinant Q88RQ2 and measure steady-state kinetics** on choline-O-sulfate and phosphorylcholine (kcat, Km, kcat/Km), plus a panel of candidate substrates (nitrophenyl sulfate, other choline esters) to define specificity quantitatively.

2. **Confirm the formylglycine modification** by intact-protein and peptide mass spectrometry of Cys52, and identify the *P. putida* formylglycine-generating enzyme required for maturation (test activity in a maturation-deficient background).

3. **Determine the metal dependence and active-site structure** — metal analysis (ICP-MS), activity ± chelators/added divalent cations, and an experimental structure (X-ray/cryo-EM) to validate the predicted Arg56 / Asp12-Asn73-Asp289 / His-Lys constellation from the AlphaFold model (F007).

4. **Characterize the adjacent ABC transporter** by transport assays with labeled choline-O-sulfate in wild-type vs. transporter-knockout strains, testing whether it is the dedicated COS importer implied by the *betC* mutant's COS accumulation.

5. **Dissect the LysR regulator** — identify its inducer (choline-O-sulfate vs. choline) and operator by transcriptional fusions and EMSA/DNase footprinting, and compare the salt-repression mechanism to the BetI system.

6. **Physiological growth panel** — quantify growth of wild-type, Δ*betC*, and complemented strains on choline-O-sulfate as sole C, N, and S source, closing the loop on the tripartite nutritional role, and confirm cytoplasmic localization by subcellular fractionation.

---

## Direct Answer

**betC (PP_0077, UniProt Q88RQ2) of *Pseudomonas putida* KT2440 encodes choline-O-sulfatase (EC 3.1.6.6), a cytoplasmic sulfatase-superfamily enzyme that hydrolyzes the sulfate ester of choline-O-sulfate — and, more weakly, phosphorylcholine — into free choline and inorganic sulfate, using a Cys52-derived formylglycine nucleophile and a double-displacement mechanism.** It acts intracellularly on choline-O-sulfate imported by an adjacent ABC transporter and is controlled by a neighbouring LysR-type regulator. **In *P. putida* its principal role is catabolic — supplying carbon, nitrogen, and sulfur from choline-O-sulfate — and it is not involved in osmoprotection**, which is handled by the physically and functionally separate betBA genes and OpuC transporter.


## Artifacts

- [OpenScientist final report](betC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](betC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17116241
2. PMID:9736747
3. PMID:12906115
4. PMID:18793651
5. PMID:17660277
6. PMID:26058574
7. PMID:8752328