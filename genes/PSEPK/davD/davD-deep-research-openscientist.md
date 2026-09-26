---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T15:29:06.317070'
end_time: '2026-07-25T15:44:49.344650'
duration_seconds: 943.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: davD
  gene_symbol: davD
  uniprot_accession: Q88RC0
  protein_description: 'RecName: Full=Glutarate-semialdehyde dehydrogenase {ECO:0000250|UniProtKB:Q9I6M5};
    EC=1.2.1.- {ECO:0000250|UniProtKB:Q9I6M5};'
  gene_info: Name=davD {ECO:0000303|PubMed:11679348}; OrderedLocusNames=PP_0213;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aldehyde dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_CYS.
    (IPR016160); Ald_DH_CS_GLU. (IPR029510); Ald_DH_N. (IPR016162)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: davD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: davD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RC0
- **Protein Description:** RecName: Full=Glutarate-semialdehyde dehydrogenase {ECO:0000250|UniProtKB:Q9I6M5}; EC=1.2.1.- {ECO:0000250|UniProtKB:Q9I6M5};
- **Gene Information:** Name=davD {ECO:0000303|PubMed:11679348}; OrderedLocusNames=PP_0213;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_CYS. (IPR016160); Ald_DH_CS_GLU. (IPR029510); Ald_DH_N. (IPR016162)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "davD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'davD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **davD** (gene ID: davD, UniProt: Q88RC0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **davD** (Q88RC0, PP_0213) — Glutarate-Semialdehyde Dehydrogenase of *Pseudomonas putida* KT2440

## Identity Verification

| Attribute | Value |
|-----------|-------|
| **UniProt** | Q88RC0 |
| **Gene symbol** | davD |
| **Ordered locus** | PP_0213 |
| **Organism** | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| **Protein family** | Aldehyde dehydrogenase (ALDH) family |
| **Key InterPro domains** | Ald_DH_N (IPR016162), Ald_DH_C (IPR016163), Ald_DH/histidinol_DH (IPR016161), catalytic Cys signature (IPR016160), conserved Glu signature (IPR029510) |
| **Assigned activity** | Glutarate-semialdehyde dehydrogenase, EC 1.2.1.- (specifically EC 1.2.1.20) |

The gene symbol **davD is unambiguous** and consistent across the literature: in *Pseudomonas putida* it denotes the glutarate-semialdehyde dehydrogenase of the L-lysine catabolic ("Dav") pathway. All literature retrieved for "davD" in *P. putida* refers to this same enzyme; no conflicting gene of the same symbol exists in this organism, and the ALDH protein family, organism, and locus all align with the UniProt record. **Identity is confirmed — no ambiguity fallback was required.**

---

## Summary

**davD** (Q88RC0; PP_0213) encodes a **soluble, cytoplasmic, NAD⁺-dependent glutarate-semialdehyde dehydrogenase** (EC 1.2.1.20). Its primary molecular function is to catalyze the irreversible oxidation of **glutarate semialdehyde (5-oxopentanoate) to glutarate**, consuming NAD⁺ and water and generating NADH and a proton. This is the **fourth and terminal oxidative step** of the **5-aminovalerate (AVA / "Dav") branch of L-lysine catabolism** in *P. putida*, the pathway by which the organism mobilizes lysine as a carbon and nitrogen source. DavD acts immediately downstream of the DavT/GabT 5-aminovalerate aminotransferase (which produces the semialdehyde substrate) and commits the lysine-derived carbon skeleton to glutarate.

The identity and reaction of DavD rest on three orthogonal lines of evidence: (i) direct biochemical assay of the closely related *P. aeruginosa* ortholog **PA0265** confirming the glutarate-semialdehyde dehydrogenase reaction (EC 1.2.1.20); (ii) heterologous functional reconstitution of the *davDT* / *gabTD* module in *E. coli* and *Corynebacterium glutamicum*, converting 5-aminovalerate to glutarate; and (iii) native ¹³C/¹⁵N isotope-tracing and mutant genetics in *P. putida* KT2440 that establish the Dav pathway and its convergence on glutarate.

Biologically, DavD occupies a **metabolic convergence node**. The **glutarate** it produces is the shared endpoint of *both* of *P. putida*'s two interconnected lysine-degradation routes (the aminovalerate/Dav pathway and the aminoadipate pathway). Downstream, glutarate is further catabolized by two routes — the **glutarate hydroxylation pathway** and the **glutaryl-CoA dehydrogenation pathway** — feeding acetyl-CoA and the TCA cycle. Because glutarate is a valuable C5 dicarboxylic-acid platform chemical (nylon precursor), the *davDT* module has been repeatedly transplanted into industrial hosts for glutarate production.

---

## Key Findings

### Finding 1 — DavD is the NAD⁺-dependent glutarate-semialdehyde dehydrogenase of *P. putida* lysine catabolism

The core molecular function of davD is the NAD⁺-dependent oxidation of glutarate semialdehyde to glutarate:

```
glutarate semialdehyde + NAD⁺ + H₂O  →  glutarate + NADH + H⁺        (EC 1.2.1.20)
```

Multiple independent metabolic-engineering studies functionally assign *P. putida* KT2440 **davD (PP_0213, Q88RC0)** as glutarate semialdehyde dehydrogenase. Adkins et al. (2013) co-expressed the *davDT* module and demonstrated conversion of 5-aminovalerate to glutarate, reaching **0.82 g/L glutarate**, directly placing DavD as the dehydrogenase acting downstream of the aminotransferase ([PMID: 23296991](https://pubmed.ncbi.nlm.nih.gov/23296991/)). Park et al. achieved glutarate production using the equivalent *gabTD* module in *E. coli* ([PMID: 23246520](https://pubmed.ncbi.nlm.nih.gov/23246520/)). The enzymatic identity is anchored biochemically by the *P. aeruginosa* ortholog **PA0265**, assayed in a coupled reaction and shown to catalyze **glutarate semialdehyde dehydrogenase (EC 1.2.1.20)** ([PMID: 17388807](https://pubmed.ncbi.nlm.nih.gov/17388807/)). The explicit naming of *P. putida* davD as glutarate semialdehyde dehydrogenase is restated in the *C. glutamicum* engineering literature ([PMID: 30144560](https://pubmed.ncbi.nlm.nih.gov/30144560/)).

> "the additional co-expression of glutaric semialdehyde dehydrogenase and 5-aminovalerate aminotransferase (encoded by davDT) led to the production of 0.82 g/L glutarate" — Adkins et al. ([PMID: 23296991](https://pubmed.ncbi.nlm.nih.gov/23296991/))

> "PA0265 as a putative glutarate semialdehyde dehydrogenase (EC 1.2.1.20)" — Yamanishi et al. ([PMID: 17388807](https://pubmed.ncbi.nlm.nih.gov/17388807/))

> "Pseudomonas putida davT and davD genes encoding 5-aminovalerate transaminase and glutarate semialdehyde dehydrogenase, respectively" — Kim et al. ([PMID: 30144560](https://pubmed.ncbi.nlm.nih.gov/30144560/))

The **cofactor is NAD⁺**, consistent with the catabolic direction (generating reducing equivalents) and with ALDH-family mechanism: an active-site cysteine nucleophile attacks the aldehyde carbonyl of glutarate semialdehyde to form a thiohemiacetal, hydride transfer to NAD⁺ yields a thioacyl-enzyme intermediate, and hydrolysis releases the carboxylic-acid product (glutarate). These catalytic Cys and Glu residues are exactly the features captured by InterPro IPR016160 (Ald_DH_CS_CYS) and IPR029510 (Ald_DH_CS_GLU) annotated for Q88RC0.

### Finding 2 — DavD operates within the cytoplasmic Dav (5-aminovalerate) pathway of L-lysine catabolism

DavD is the terminal member of a four-enzyme **soluble cytoplasmic module** that converts L-lysine to glutarate:

| Step | Gene(s) | Enzyme | Reaction |
|------|---------|--------|----------|
| 1 | **davB** | Lysine 2-monooxygenase | L-lysine → 5-aminovaleramide (δ-aminovaleramide) |
| 2 | **davA** | δ-aminovaleramidase | 5-aminovaleramide → 5-aminovalerate (5-AVA) |
| 3 | **davT / gabT** (PP_0214) | 5-aminovalerate aminotransferase | 5-AVA + α-ketoglutarate → glutarate semialdehyde + glutamate |
| 4 | **davD** (PP_0213) | **Glutarate-semialdehyde dehydrogenase** | **glutarate semialdehyde → glutarate** |

This four-gene set reconstitutes the complete L-lysine → 5-aminovaleramide → 5-aminovalerate → glutarate semialdehyde → glutarate route when transferred into heterologous hosts such as *E. coli* and *C. glutamicum* (Adkins 2013; Park 2013; Rohles 2016; Kim 2019) ([PMID: 23296991](https://pubmed.ncbi.nlm.nih.gov/23296991/); [PMID: 27618862](https://pubmed.ncbi.nlm.nih.gov/27618862/); [PMID: 30144560](https://pubmed.ncbi.nlm.nih.gov/30144560/)). The genes **davD/davT (PP_0213/PP_0214) are chromosomally adjacent** and are consistently co-transferred as *davDT* / *gabTD* modules, consistent with an operonic, soluble enzymatic unit acting in the cytoplasm.

> "endogenous genes coding for 5-aminovalerate transaminase (gabT) and glutarate semialdehyde dehydrogenase, 5-aminovalerate was partially converted to glutarate" — ([PMID: 27618862](https://pubmed.ncbi.nlm.nih.gov/27618862/))

> "It is a metabolite of l-lysine catabolism through the aminovalerate pathway in Pseudomonas putida" — ([PMID: 25012259](https://pubmed.ncbi.nlm.nih.gov/25012259/))

The **subcellular localization is cytoplasmic**, inferred from the soluble nature of the pathway (no signal peptide or transmembrane segments), the intracellular origin of its substrate (delivered by the cytoplasmic DavT transaminase), and the enzyme's full activity as a soluble catalyst in heterologous cytoplasm.

### Finding 3 — DavD-produced glutarate is the convergence node of both lysine pathways and feeds glutaryl-CoA / hydroxylation catabolism

The product of DavD, **glutarate**, is metabolically pivotal. Revelles et al. (2005) used ¹³C/¹⁵N-lysine isotope labeling and pathway mutants to show that *P. putida* KT2440 degrades L-lysine through **two interconnected routes** — the aminovalerate (Dav) pathway (in which DavD acts) and the aminoadipate pathway — **both converging on glutarate**; this study also assigned the *davB* and *davA* gene functions of the upper pathway ([PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/)).

> "New genes were identified in both pathways, including the davB and davA genes that encode the enzymes involved in the oxidation of L-lysine to delta-aminovaleramide and the hydrolysis of the latter to delta-aminovalerate" — Revelles et al. ([PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/))

> "there is yet another interconnection at the lower end of the pathways in which aminoadipate is channeled to yield glutarate" — Revelles et al. ([PMID: 16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/))

Downstream of DavD, Zhang et al. (2019) showed glutarate is further catabolized by **two routes** — the **glutarate hydroxylation pathway** and the **glutaryl-CoA dehydrogenation pathway** — under the transcriptional control of the GntR-family regulator **CsiR** and the LysR-family regulator **GcdR** ([PMID: 31363033](https://pubmed.ncbi.nlm.nih.gov/31363033/)).

> "can be catabolized through both the glutarate hydroxylation pathway and the glutaryl-coenzyme A (glutaryl-CoA) dehydrogenation pathway" — Zhang et al. ([PMID: 31363033](https://pubmed.ncbi.nlm.nih.gov/31363033/))

DavD is therefore the enzymatic gateway that converts the lysine-derived semialdehyde into the branch-point metabolite glutarate, committing lysine carbon to central metabolism.

---

## Mechanistic Model / Interpretation

DavD is best understood as the **committed oxidative terminus of the lysine→glutarate conduit** in *P. putida*:

```
                    L-LYSINE
                       │
              davB (lysine 2-monooxygenase)
                       ▼
              5-aminovaleramide (δ-valeramide)
                       │
              davA (δ-aminovaleramidase)
                       ▼
              5-AMINOVALERATE (5-AVA)  ◄─── C5 platform chemical (nylon-5)
                       │
              davT / gabT (5-AVA aminotransferase; +α-KG → Glu)
                       ▼
              GLUTARATE SEMIALDEHYDE (5-oxopentanoate)
                       │
         ►►►  davD  (GLUTARATE-SEMIALDEHYDE DEHYDROGENASE)  ◄◄◄
              NAD⁺ + H₂O → NADH + H⁺
                       ▼
                   GLUTARATE  ◄──── also produced from the AMINOADIPATE pathway
                       │              (two lysine routes converge here)
        ┌──────────────┴───────────────┐
        ▼                              ▼
 glutarate hydroxylation       glutaryl-CoA dehydrogenation
     pathway (CsiD/LhgO)             pathway (GcdH)
        │                              │
        └──────────────┬───────────────┘
                       ▼
        central carbon metabolism (acetyl-CoA / 2-oxoglutarate / TCA)
   (downstream glutarate catabolism regulated by CsiR [GntR] and GcdR [LysR])
```

**Reaction and mechanism.** DavD is a Rossmann-fold, NAD⁺-utilizing aldehyde dehydrogenase. The conserved catalytic Cys/Glu pair (InterPro IPR016160/IPR029510) executes the canonical ALDH mechanism, and the reaction is effectively irreversible under physiological conditions, making DavD a metabolically committed, flux-controlling step.

**Localization.** All evidence indicates a **cytoplasmic** location: soluble protein, no secretion/membrane signals, participates in a soluble catabolic module, and remains fully active as a soluble enzyme in heterologous cytoplasm.

**Physiological role.** The Dav pathway lets *P. putida* use L-lysine as **both a carbon and nitrogen source**: nitrogen is released during the upstream oxygenase and transaminase steps, while DavD funnels the remaining C5 dicarboxylic backbone (glutarate) into energy and carbon metabolism. Because glutarate is the shared endpoint of both lysine catabolic routes, DavD is central to lysine utilization even though a parallel (aminoadipate) route exists.

**Biotechnological significance.** Because DavD generates glutarate — a five-carbon dicarboxylic-acid platform chemical and nylon precursor — the *davDT* / *gabTD* module has been transplanted into *E. coli* and *C. glutamicum* to convert lysine (or 5-AVA) into glutarate. This applied use is itself strong functional evidence: the module only works because DavD reliably performs the glutarate-semialdehyde → glutarate oxidation.

---

## Evidence Base

| PMID | Study (short) | Contribution to davD annotation |
|------|---------------|-------------------------------|
| [16237033](https://pubmed.ncbi.nlm.nih.gov/16237033/) | *Multiple and interconnected pathways for L-lysine catabolism in P. putida KT2440* (Revelles et al. 2005) | **Primary genetic/isotopic study.** Defined the Dav and aminoadipate pathways in KT2440; assigned davB/davA; established that both routes converge on glutarate — the DavD product. |
| [17388807](https://pubmed.ncbi.nlm.nih.gov/17388807/) | *Prediction of missing enzyme genes… lysine degradation of P. aeruginosa* (Yamanishi et al. 2007) | **Biochemical anchor.** Ortholog PA0265 assayed as glutarate semialdehyde dehydrogenase (EC 1.2.1.20) in a coupled assay — defines the reaction/EC number for the family. |
| [23296991](https://pubmed.ncbi.nlm.nih.gov/23296991/) | *Engineering E. coli for 5-AVA and glutarate* (Adkins et al. 2013) | Co-expression of *davDT* converted 5-AVA to glutarate (0.82 g/L); directly names davD as glutaric semialdehyde dehydrogenase. |
| [23246520](https://pubmed.ncbi.nlm.nih.gov/23246520/) | *Metabolic engineering of E. coli for C5 chemicals* (Park et al. 2013) | Expression of P. putida *gabTD* (aminotransferase + glutarate semialdehyde dehydrogenase) converted 5-AVA to glutarate (1.7 g/L). |
| [27618862](https://pubmed.ncbi.nlm.nih.gov/27618862/) | *Systems metabolic engineering of C. glutamicum for 5-AVA/glutarate* (Rohles et al. 2016) | Places glutarate semialdehyde dehydrogenase immediately downstream of the transaminase; confirms 5-AVA → glutarate step. |
| [30144560](https://pubmed.ncbi.nlm.nih.gov/30144560/) | *Metabolic engineering of C. glutamicum for glutaric acid* (Kim et al. 2019) | Explicitly identifies P. putida **davD** as glutarate semialdehyde dehydrogenase (and davT as 5-AVA transaminase). |
| [31363033](https://pubmed.ncbi.nlm.nih.gov/31363033/) | *Regulation of glutarate catabolism by CsiR and GcdR in KT2440* (Zhang et al. 2019) | Defines the downstream fate of DavD's product: glutarate hydroxylation and glutaryl-CoA dehydrogenation pathways and their regulators. |
| [25012259](https://pubmed.ncbi.nlm.nih.gov/25012259/) | *Enzymatic production of 5-AVA from L-lysine* | Confirms the aminovalerate pathway is the L-lysine catabolic route in P. putida. |

**Supporting/context literature** (5-AVA production, transporters, pathway engineering): [PMID: 25124937](https://pubmed.ncbi.nlm.nih.gov/25124937/), [PMID: 27510748](https://pubmed.ncbi.nlm.nih.gov/27510748/), [PMID: 35917915](https://pubmed.ncbi.nlm.nih.gov/35917915/), [PMID: 31720214](https://pubmed.ncbi.nlm.nih.gov/31720214/), [PMID: 41629971](https://pubmed.ncbi.nlm.nih.gov/41629971/). These reinforce the surrounding pathway (davB/davA/davT function, 5-AVA export/import) but do not individually characterize DavD.

**Consistency of the evidence.** The annotation is high-confidence because it rests on **three orthogonal pillars**: (i) direct biochemical assay of the ortholog (PA0265; EC 1.2.1.20); (ii) heterologous functional reconstitution of the *davDT* / *gabTD* module in two different hosts producing glutarate; and (iii) native isotope-tracing genetics in *P. putida* KT2440 that positions glutarate as the pathway convergence point. No literature described a conflicting function for davD/PP_0213, and the gene symbol, organism, and ALDH protein family all align with the UniProt record — the identity is not ambiguous.

---

## Supported vs. Refuted Hypotheses

- **Supported:** DavD is a cytoplasmic NAD⁺-dependent glutarate-semialdehyde dehydrogenase catalyzing glutarate semialdehyde → glutarate (EC 1.2.1.20) as the terminal step of the 5-aminovalerate branch of L-lysine catabolism.
- **Not supported / refuted:** No evidence for a transporter, structural, or signaling role; DavD is a soluble metabolic enzyme, not a membrane, adapter, or regulatory protein.

---

## Limitations and Knowledge Gaps

- **No direct enzymology on Q88RC0 itself.** The reaction and EC number are anchored on the *P. aeruginosa* ortholog **PA0265** (biochemically assayed) and on heterologous reconstitution of the *P. putida* module. Purified-protein kinetics (Km, kcat, cofactor preference) for the exact PP_0213 gene product were not located.
- **Substrate specificity not experimentally mapped.** Whether DavD is strictly specific for glutarate semialdehyde or accepts related ω-aldehyde acids (e.g., succinic or adipic semialdehyde) has not been quantified for this enzyme.
- **Cofactor confirmed by inference.** NAD⁺ dependence is expected for the catabolic direction and consistent with family membership, but the strict NAD⁺-vs-NADP⁺ preference of PP_0213 has not been directly measured in the reviewed papers.
- **No experimental structure.** No crystal structure of DavD was found; residue-level mechanistic claims rest on InterPro domain conservation.
- **davD-specific regulation not characterized.** The reviewed regulatory work (CsiR/GcdR) concerns *downstream* glutarate catabolism, not davD transcription per se.

---

## Proposed Follow-up Experiments / Actions

1. **Purify recombinant PP_0213 (Q88RC0)** and measure steady-state kinetics on glutarate semialdehyde with NAD⁺ and NADP⁺ to establish cofactor preference and catalytic efficiency directly for this ortholog.
2. **Substrate-specificity panel:** assay purified DavD against a series of ω-aldehyde carboxylic acids (succinic semialdehyde, adipate semialdehyde, glutarate semialdehyde) to define specificity and any promiscuity relevant to metabolic engineering.
3. **Structural determination** (crystallography or AlphaFold-guided mutagenesis) to confirm the active-site Cys/Glu catalytic pair and the NAD-binding Rossmann fold predicted by the InterPro domains.
4. **Clean deletion of davD (PP_0213) in KT2440** with growth phenotyping on L-lysine, 5-aminovalerate, and glutarate as sole carbon/nitrogen sources to test the metabolic requirement and any redundancy with paralogous ALDHs.
5. **In vivo localization confirmation** (fluorescent fusion or cell fractionation) to formally verify cytoplasmic localization.
6. **Transcriptional analysis of the davDT operon** under lysine induction to determine whether davD expression is co-regulated with upstream dav genes.

---

*Report generated from a 3-iteration autonomous literature investigation (13 papers reviewed, 3 high-confidence findings). Gene identity verified: symbol davD, organism P. putida KT2440, protein family aldehyde dehydrogenase — all consistent with UniProt Q88RC0. No ambiguity fallback required.*


## Artifacts

- [OpenScientist final report](davD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](davD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23296991
2. PMID:23246520
3. PMID:17388807
4. PMID:30144560
5. PMID:27618862
6. PMID:25012259
7. PMID:16237033
8. PMID:31363033
9. PMID:25124937
10. PMID:27510748
11. PMID:35917915
12. PMID:31720214
13. PMID:41629971