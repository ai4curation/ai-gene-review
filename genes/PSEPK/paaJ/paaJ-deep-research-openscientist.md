---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T17:19:07.513462'
end_time: '2026-07-23T17:48:30.371264'
duration_seconds: 1762.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaJ
  gene_symbol: paaJ
  uniprot_accession: Q88HS3
  protein_description: 'SubName: Full=3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA
    thiolase {ECO:0000313|EMBL:AAN68887.1}; EC=2.3.1.- {ECO:0000313|EMBL:AAN68887.1};
    EC=2.3.1.174 {ECO:0000313|EMBL:AAN68887.1};'
  gene_info: Name=paaJ {ECO:0000313|EMBL:AAN68887.1}; OrderedLocusNames=PP_3280 {ECO:0000313|EMBL:AAN68887.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the thiolase-like superfamily. Thiolase family.
  protein_domains: PcaF. (IPR012793); Thiolase. (IPR002155); Thiolase-like. (IPR016039);
    Thiolase-like_sf_Thiolase. (IPR050215); Thiolase_acyl_enz_int_AS. (IPR020615)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: paaJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaJ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS3
- **Protein Description:** SubName: Full=3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase {ECO:0000313|EMBL:AAN68887.1}; EC=2.3.1.- {ECO:0000313|EMBL:AAN68887.1}; EC=2.3.1.174 {ECO:0000313|EMBL:AAN68887.1};
- **Gene Information:** Name=paaJ {ECO:0000313|EMBL:AAN68887.1}; OrderedLocusNames=PP_3280 {ECO:0000313|EMBL:AAN68887.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the thiolase-like superfamily. Thiolase family.
- **Key Domains:** PcaF. (IPR012793); Thiolase. (IPR002155); Thiolase-like. (IPR016039); Thiolase-like_sf_Thiolase. (IPR050215); Thiolase_acyl_enz_int_AS. (IPR020615)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaJ** (gene ID: paaJ, UniProt: Q88HS3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *paaJ* (PP_3280, UniProt Q88HS3) in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**paaJ** (locus **PP_3280**; UniProt **Q88HS3**; EMBL AAN68887.1) encodes the **3‑oxoadipyl‑CoA / 3‑oxo‑5,6‑dehydrosuberyl‑CoA thiolase** of the aerobic **phenylacetate (phenylacetyl‑CoA) catabolic pathway** in *Pseudomonas putida* KT2440. It is a **soluble, cytoplasmic β‑ketothiolase** (thiolase‑like superfamily; acetyl‑CoA C‑acyltransferase, EC 2.3.1.174 / EC 2.3.1.223‑type) that catalyzes the **thiolytic (retro‑Claisen) cleavage of two β‑keto‑CoA intermediates** in the lower, β‑oxidation‑like segment of the pathway, releasing **acetyl‑CoA** at each step and ultimately producing **succinyl‑CoA**, which enters the TCA cycle. It is the terminal carbon‑harvesting enzyme of the phenylacetyl‑CoA catabolon.

## 2. Gene / Protein Identity Verification (mandatory check)

The task flagged possible ambiguity because Q88HS3 carries an InterPro **"PcaF" tag (IPR012793)**. This was resolved:

- **The InterPro PcaF tag denotes broad thiolase-family membership, not identity with PcaF.** PcaF proper is the **β‑ketoadipyl‑CoA thiolase of the β‑ketoadipate (protocatechuate/catechol) pathway**. Q88HS3 instead carries the diagnostic substrate **3‑oxo‑5,6‑dehydrosuberyl‑CoA**, which is unique to the **aerobic phenylacetyl‑CoA (paa) degradation pathway**.
- Genomic analysis of KT2440 (Jiménez et al. 2002) explicitly separates the **phenylacetate pathway (pha/paa genes)** from the **β‑ketoadipate pathway (pca/cat genes)** [PMID 12534466]. *paaJ*/PP_3280 belongs to the former.
- **Nomenclature note:** the same enzyme appears in the literature under several names across strains — **paaJ** (E. coli‑type unified nomenclature and the EMBL annotation used here), **phaD** (the KT2440 "pha" annotation of Jiménez 2002 / Kim 2006), and the paa‑cluster thiolase in *P. putida* U. All refer to the phenylacetate‑pathway thiolase, distinct from PcaF.

**Conclusion:** The gene symbol is correctly matched; the organism is *P. putida* KT2440; the family/domain content is consistent with a degradative thiolase. Research proceeds on the correct protein.

## 3. Primary Molecular Function

### Reaction catalyzed
PaaJ is a **degradative β‑ketothiolase (acetyl‑CoA C‑acyltransferase)** that runs the Claisen condensation in the **thiolytic (cleavage) direction**, using a conserved **active-site cysteine nucleophile** (thiolase acyl‑enzyme intermediate signature, IPR020615) to form a covalent acyl‑enzyme and split a β‑keto‑CoA into a shortened acyl‑CoA plus acetyl‑CoA.

Within the phenylacetate pathway it performs **two consecutive thiolytic cleavages**:

1. **3‑oxo‑5,6‑dehydrosuberyl‑CoA → 2,3‑dehydroadipyl‑CoA + acetyl‑CoA** (EC 2.3.1.223‑type), the first thiolase step after ring opening; and
2. **3‑oxoadipyl‑CoA (β‑ketoadipyl‑CoA) → succinyl‑CoA + acetyl‑CoA** (EC 2.3.1.174), the **final step** of the pathway.

### Substrate specificity
The enzyme is specific for the **β‑keto‑CoA thioesters of the phenylacetyl‑CoA lower pathway** (3‑oxo‑5,6‑dehydrosuberyl‑CoA and 3‑oxoadipyl‑CoA). This dual‑substrate capacity — the reason the UniProt name is compound ("3‑oxoadipyl‑CoA/3‑oxo‑5,6‑dehydrosuberyl‑CoA thiolase") — reflects that both physiological substrates are dicarboxylic β‑keto‑CoA intermediates differing only by the 5,6‑double bond.

### Direct experimental evidence
Nogales et al. 2007 demonstrated, by **both in vivo and in vitro assays in *P. putida* and *E. coli***, that the paa‑cluster thiolase catalyzes the last pathway step — thiolytic cleavage of β‑ketoadipyl‑CoA to **succinyl‑CoA + acetyl‑CoA** — and identified succinyl‑CoA as a final product [PMID 17259607]. Teufel et al. 2010 (PNAS), which elucidated the entire pathway, confirmed that after ring 1,2‑epoxidation, oxepin formation and hydrolytic ring cleavage, **β‑oxidation steps lead to acetyl‑CoA and succinyl‑CoA** [PMID 20660314].

## 4. Pathway Context — the Phenylacetyl‑CoA Catabolon

PaaJ is the terminal enzyme of the **aerobic "hybrid" phenylacetate pathway**, which is unusual in processing an aromatic substrate as **CoA thioesters** rather than by classical ring‑dioxygenation:

1. **Activation:** phenylacetate → phenylacetyl‑CoA by the CoA ligase **PaaK**.
2. **Ring activation:** the multicomponent oxygenase **PaaABC(D)E** epoxidizes the ring (ring‑1,2‑epoxide) [PMID 20660314].
3. **Ring rearrangement/opening:** **PaaG** (isomerase) and **PaaZ** (oxepin ring‑opening/aldehyde dehydrogenase) generate an open‑chain 3‑oxo‑dicarboxylyl‑CoA.
4. **β‑oxidation‑like lower segment:** the **PaaFGHIJ** enzymes (enoyl‑CoA hydratase, 3‑hydroxyacyl‑CoA dehydrogenase, and **PaaJ thiolase**) shorten the chain — "gene products … show significant similarity to fatty acid β‑oxidation enzymes, likely involved in further mineralization to Krebs cycle intermediates" [PMID 9748275]. **PaaJ closes the pathway**, delivering succinyl‑CoA to the TCA cycle and liberating two acetyl‑CoA.

This pathway is the **catabolon core** onto which multiple peripheral routes converge — phenylacetate, 2‑phenylethylamine, 2‑phenylethanol, styrene, n‑phenylalkanoates and phenylalanine are all funneled to **phenylacetyl‑CoA** and then through PaaJ [PMID 9600981; PMID 18177365]. Thus PaaJ is a **metabolic convergence point** for aromatic carbon assimilation.

## 5. Subcellular Localization

- PaaJ is a member of the **cytoplasmic thiolase superfamily**; it has no signal peptide, lipobox, or transmembrane segments, and all of its substrates/products are **soluble CoA thioesters**. Its site of action is therefore the **cytoplasm**.
- Consistent with cytosolic pathway operation, KT2440 **proteomics detected the pha‑cluster β‑ketoacyl‑CoA thiolase (PhaD) among induced soluble degradation enzymes** upon exposure to a pathway substrate [PMID 16470664].

## 6. Regulation (context, briefly)

Expression of the paa/pha operon is controlled by the **PaaX repressor**, which is released by the true inducer **phenylacetyl‑CoA** — the first aromatic‑pathway regulator shown to respond to a CoA thioester [PMID 9748275; PMID 16788190]. PaaJ is therefore expressed specifically when phenylacetyl‑CoA accumulates, i.e., during growth on phenylacetate or its precursors.

## 7. Supported vs. Refuted Hypotheses

| Hypothesis | Outcome | Basis |
|---|---|---|
| Q88HS3 is the β‑ketoadipate‑pathway thiolase PcaF | **Refuted** | Substrate (3‑oxo‑5,6‑dehydrosuberyl‑CoA), cluster membership (pha/paa ≠ pca), and pathway distinction [PMID 12534466] |
| Q88HS3 is the phenylacetate‑pathway thiolase (PaaJ) | **Supported** | UniProt annotation + pathway biochemistry [PMID 20660314; 17259607] |
| The enzyme catalyzes thiolytic cleavage to acetyl‑CoA + succinyl‑CoA | **Supported (experimental)** | In vitro + in vivo demonstration [PMID 17259607] |
| The enzyme acts in the cytoplasm | **Supported (inference + proteomics)** | Soluble thiolase family; CoA‑thioester substrates; induced soluble protein [PMID 16470664] |

## 8. Limitations & Future Directions

- **Strain‑specific enzymology:** the most direct kinetic characterization (Nogales 2007) was performed on *P. putida*/*E. coli* paa thiolases; a dedicated purified‑enzyme kinetic/structural study of the exact KT2440 PP_3280 product (Km, kcat for each of the two substrates, 3‑D structure) would strengthen the annotation, though sequence and pathway conservation make the transfer of function reliable.
- **Bifunctionality quantification:** the relative activity on 3‑oxo‑5,6‑dehydrosuberyl‑CoA vs. 3‑oxoadipyl‑CoA in KT2440 has not been measured directly.
- **Structure:** no experimental structure of Q88HS3 is cited here; the catalytic Cys/His/Cys triad is inferred from thiolase‑family conservation (IPR020615) and could be confirmed by mutagenesis or AlphaFold‑guided analysis.

## Key References
- Teufel R, et al. *Bacterial phenylalanine and phenylacetate catabolic pathway revealed.* PNAS 2010. **PMID 20660314**
- Nogales J, et al. *Characterization of the last step of the aerobic phenylacetic acid degradation pathway.* Microbiology 2007. **PMID 17259607**
- Jiménez JI, et al. *Genomic analysis of the aromatic catabolic pathways from Pseudomonas putida KT2440.* Environ Microbiol 2002. **PMID 12534466**
- Ferrández A, et al. *Catabolism of phenylacetic acid in Escherichia coli — a new aerobic hybrid pathway.* JBC 1998. **PMID 9748275**
- Olivera ER, et al. *Molecular characterization of the phenylacetic acid catabolic pathway in Pseudomonas putida U: the phenylacetyl‑CoA catabolon.* PNAS 1998. **PMID 9600981**
- Kim YH, et al. *Analysis of aromatic catabolic pathways in P. putida KT2440 (proteomics).* 2006. **PMID 16470664**
- Arias S, et al. *Conversion of 2‑phenylethylamine/2‑phenylethanol into phenylacetic acid in P. putida U.* 2008. **PMID 18177365**


## Artifacts

- [OpenScientist final report](paaJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaJ-deep-research-openscientist_artifacts/final_report.pdf)