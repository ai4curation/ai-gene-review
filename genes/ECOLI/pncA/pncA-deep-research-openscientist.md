---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T04:37:04.776922'
end_time: '2026-11-12T04:47:16.538764'
duration_seconds: 611.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P21369
  gene_symbol: pncA
  uniprot_accession: P21369
  protein_description: 'RecName: Full=Nicotinamidase {ECO:0000303|PubMed:4399474,
    ECO:0000303|PubMed:8726014}; EC=3.5.1.19 {ECO:0000269|PubMed:4399474, ECO:0000305|PubMed:8726014};
    AltName: Full=Nicotinamide deamidase {ECO:0000303|PubMed:4399474}; Short=NAMase
    {ECO:0000303|PubMed:8726014}; AltName: Full=Pyrazinamidase {ECO:0000303|PubMed:8726014};
    Short=PZAase {ECO:0000303|PubMed:8726014}; EC=3.5.1.- {ECO:0000305|PubMed:8726014};'
  gene_info: Name=pncA {ECO:0000303|PubMed:8726014}; Synonyms=nam, ydjB; OrderedLocusNames=b1768,
    JW1757;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the isochorismatase family. .
  protein_domains: Isochorismatase-like_dom. (IPR000868); Isochorismatase-like_sf.
    (IPR036380); Isochorismatase_Nicotinamidase. (IPR052347); Isochorismatase (PF00857)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pncA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pncA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P21369
- **Protein Description:** RecName: Full=Nicotinamidase {ECO:0000303|PubMed:4399474, ECO:0000303|PubMed:8726014}; EC=3.5.1.19 {ECO:0000269|PubMed:4399474, ECO:0000305|PubMed:8726014}; AltName: Full=Nicotinamide deamidase {ECO:0000303|PubMed:4399474}; Short=NAMase {ECO:0000303|PubMed:8726014}; AltName: Full=Pyrazinamidase {ECO:0000303|PubMed:8726014}; Short=PZAase {ECO:0000303|PubMed:8726014}; EC=3.5.1.- {ECO:0000305|PubMed:8726014};
- **Gene Information:** Name=pncA {ECO:0000303|PubMed:8726014}; Synonyms=nam, ydjB; OrderedLocusNames=b1768, JW1757;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the isochorismatase family. .
- **Key Domains:** Isochorismatase-like_dom. (IPR000868); Isochorismatase-like_sf. (IPR036380); Isochorismatase_Nicotinamidase. (IPR052347); Isochorismatase (PF00857)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pncA" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pncA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pncA** (gene ID: P21369, UniProt: P21369) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pncA* (Nicotinamidase, P21369) in *Escherichia coli* K-12

## Summary

The gene **pncA** (synonyms *nam*, *ydjB*; ordered locus b1768 / JW1757) of *Escherichia coli* strain K-12 encodes **nicotinamidase** (nicotinamide deamidase; EC 3.5.1.19; UniProt **P21369**). The enzyme catalyzes the hydrolytic deamidation of **nicotinamide to nicotinic acid plus ammonia**. This reaction is the committed entry step of the bacterial **NAD⁺ salvage pathway** (the pyridine nucleotide cycle), by which cells recapture the pyridine ring liberated from NAD⁺ turnover and resynthesize the essential redox cofactor. The identification is unambiguous: the gene symbol, organism, EC number, protein family (isochorismatase-like / cysteine-hydrolase superfamily), and catalytic domains all match, and the enzyme is directly supported by genetic and biochemical studies in *E. coli* K-12 ([PMID: 8726014](https://pubmed.ncbi.nlm.nih.gov/8726014/)).

Mechanistically, PncA is a **Zn²⁺-dependent cysteine hydrolase** belonging to the isochorismatase-like superfamily (Pfam PF00857). Catalysis proceeds through a conserved **Asp–Lys–Cys catalytic triad** and a non-proline *cis*-peptide bond, with an active-site metal ion (Zn²⁺) acting as a Lewis acid that polarizes the substrate carbonyl and positions the catalytic water. The reaction passes through a covalent **nicotinoyl–thioester intermediate** on the catalytic cysteine, which is then hydrolyzed to release nicotinic acid. These features are conserved across the family and are supported by multiple crystal structures of homologs and by QM/MM computation.

Functionally, PncA acts in the **cytoplasm**. Together with nicotinic acid phosphoribosyltransferase (**PncB**, the Preiss–Handler enzyme), it constitutes the major route for recycling the pyridine ring into NAD⁺ in *E. coli*. Its physiological substrate is **nicotinamide**; the structurally related tuberculosis prodrug **pyrazinamide** is hydrolyzed only as a fortuitous, lower-efficiency secondary substrate (the "pyrazinamidase" activity for which the enzyme is also named). Beyond cofactor regeneration, by clearing intracellular nicotinamide — a feedback inhibitor of NAD⁺-dependent sirtuin deacetylases — PncA indirectly modulates the activity of the *E. coli* sirtuin **CobB**, linking NAD⁺ salvage to protein-deacetylation signaling.

---

## Key Findings

### Finding 1 — *pncA* encodes a single bifunctional nicotinamidase/pyrazinamidase (EC 3.5.1.19)

The defining biochemical identity of PncA in *E. coli* was established by Frothingham and colleagues ([PMID: 8726014](https://pubmed.ncbi.nlm.nih.gov/8726014/)). Transposon mutagenesis identified a single 639-bp open reading frame (*pncA*, b1768) whose disruption abolishes pyrazinamidase (PZAase) activity. Critically, multicopy (plasmid) expression of this ORF raised **both** pyrazinamidase and nicotinamidase (EC 3.5.1.19) activities **in parallel, by roughly 10-fold**, demonstrating that a single polypeptide carries both activities rather than two separate enzymes. The authors concluded directly that "*a single E. coli enzyme accounts for both PZAase and nicotinamidase activities*."

The physiological reaction — deamidation of nicotinamide — was confirmed *in vivo*: the overexpressing strain "*could utilize nicotinamide as a sole nitrogen source*." This is only possible if PncA cleaves the amide bond of nicotinamide, releasing ammonia that feeds nitrogen assimilation while generating nicotinic acid. This single observation simultaneously establishes the reaction chemistry (amide hydrolysis/deamidation) and its biological productivity.

**Reaction catalyzed:**

```
   Nicotinamide  +  H2O   --PncA-->   Nicotinic acid  +  NH3
   (pyridine-3-carboxamide)            (pyridine-3-carboxylate)
```

### Finding 2 — PncA is a Zn²⁺-dependent cysteine hydrolase using an Asp–Lys–Cys triad and a thioester intermediate

Although the *E. coli* enzyme itself has not been crystallized in the records reviewed, the catalytic machinery is strongly conserved across the nicotinamidase/pyrazinamidase family (isochorismatase-like / cysteine-hydrolase superfamily, matching P21369's annotated domains: Isochorismatase-like_dom IPR000868, Isochorismatase PF00857). Three independent, complementary lines of structural and computational evidence define the mechanism:

- **Crystal structure of *Pyrococcus horikoshii* pyrazinamidase** revealed a catalytic "*triad (D10, K94, and C133) and a cis-peptide (between V128 and A129)*" together with an active-site metal (Zn²⁺) site ([PMID: 11714269](https://pubmed.ncbi.nlm.nih.gov/11714269/)). This defines the conserved three-residue catalytic center and the characteristic non-proline *cis*-peptide bond of the family.

- **High-resolution structures of *Streptococcus pneumoniae* nicotinamidase** captured reaction intermediates: "*a trapped nicotinoyl thioester in a complex with SpNic reveals the structure of the proposed thioester reaction intermediate*" ([PMID: 20853856](https://pubmed.ncbi.nlm.nih.gov/20853856/)). This is direct structural proof of the **covalent cysteinyl–thioester** that forms when the catalytic cysteine attacks the substrate carbonyl, displacing ammonia. The metal ion coordinates the substrate and the catalytic water, while an oxyanion hole stabilizes developing negative charge.

- **QM/MM modeling of yeast nicotinamidase Pnc1** provided the energetic and mechanistic detail, confirming that "*the activated C167 serves as the nucleophile*," with the aspartate acting as a general base, the lysine stabilizing intermediates, and the metal site functioning as a Lewis acid ([PMID: 24413890](https://pubmed.ncbi.nlm.nih.gov/24413890/)).

Together these establish a two-step mechanism: (1) nucleophilic attack by the thiolate of the catalytic Cys on the amide carbonyl, forming a tetrahedral intermediate that collapses to release ammonia and a covalent acyl-enzyme (nicotinoyl–thioester); (2) metal-activated water hydrolyzes the thioester, releasing nicotinic acid and regenerating the enzyme. Recent spectroscopic work on a Co²⁺-substituted *S. pneumoniae* enzyme has further characterized a catalytically relevant thioester intermediate during turnover with nicotinamide and highlighted a conserved second-sphere aspartate that maintains metal-site geometry ([PMID: 43001968](https://pubmed.ncbi.nlm.nih.gov/43001968/)), reinforcing the metallo-cysteine-hydrolase model.

**Catalytic architecture (consensus family model):**

| Element | Role | Representative residue |
|---|---|---|
| Catalytic Cys | Nucleophile; forms thioester intermediate | Cys133 (*P. horikoshii*) / Cys167 (yeast Pnc1) |
| Catalytic Asp | General base; deprotonates Cys / activates water | Asp10 / Asp8 |
| Catalytic Lys | Transition-state / intermediate stabilization | Lys94 / Lys122 |
| *cis*-peptide bond | Active-site geometry | V128–A129 |
| Metal ion (Zn²⁺) | Lewis acid; polarizes carbonyl, positions water | Active-site metal |
| Oxyanion hole | Stabilizes tetrahedral oxyanion | Backbone/metal |

### Finding 3 — PncA catalyzes the first committed step of NAD⁺ salvage and acts in the cytoplasm

Nicotinamidases convert nicotinamide to nicotinic acid, "*essential for the recycling of nicotinamide into NAD(+) in most prokaryotes and most single-cell and multicellular eukaryotes, but not in mammals*" ([PMID: 20853856](https://pubmed.ncbi.nlm.nih.gov/20853856/)). This positions PncA at the **entry point of the NAD⁺ salvage (pyridine nucleotide) cycle**: the nicotinic acid it produces is handed to the Preiss–Handler pathway via nicotinate phosphoribosyltransferase (PncB) for resynthesis of NAD⁺. The absence of this enzyme family in mammals is why nicotinamidases are of interest as selective antimicrobial targets ([PMID: 39537945](https://pubmed.ncbi.nlm.nih.gov/39537945/)).

The site of action is **intracellular**. In localization studies using complemented strains, "*the PZase activity was detected exclusively in the cytoplasm, suggesting an intracellular localization for PzaA and PncA*" ([PMID: 10986252](https://pubmed.ncbi.nlm.nih.gov/10986252/)). This is consistent with PncA being a soluble enzyme operating on the intracellular nicotinamide pool, with no signal peptide or membrane-targeting features expected for a cytoplasmic salvage enzyme.

### Finding 4 — In *E. coli*, PncA + PncB form the major pyridine-ring salvage pathway

The authoritative EcoSal review of NAD biogenesis in *E. coli* K-12 (Osterman, [PMID: 26443758](https://pubmed.ncbi.nlm.nih.gov/26443758/)) places PncA at the center of pyridine-ring recycling: nicotinic acid phosphoribosyltransferase (PncB), "*together with nicotinamide deamidase (PncA), compose the major pathway for utilization of the pyridine ring in the form of amidated (Nm) or deamidated (Na) precursors.*" PncA deamidates nicotinamide to nicotinic acid, and PncB performs the single Preiss–Handler step converting niacin to nicotinate mononucleotide (NaMN), which is then adenylylated and amidated to regenerate NAD⁺.

The physiological source of the nicotinamide substrate is NAD⁺ turnover itself. Classic isotopic in vivo studies showed that "*in E. coli, pyrophosphate bond cleavage of intracellular NAD predominates*" ([PMID: 7021549](https://pubmed.ncbi.nlm.nih.gov/7021549/)) — i.e., NAD⁺-consuming reactions (such as DNA ligase sealing nicks, which cleaves NAD⁺) release nicotinamide mononucleotide / nicotinamide, which re-enters the cycle through PncA-catalyzed deamidation. PncA therefore closes the loop of a continuous intracellular recycling cycle rather than acting only on exogenous vitamin.

**NAD⁺ salvage / pyridine nucleotide cycle in *E. coli*:**

```
        NAD(+)
          |  (consumed by DNA ligase, ADP-ribosylation, etc.;
          |   pyrophosphate-bond cleavage predominates)
          v
   Nicotinamide (Nm) ---------+
          |                   |
   PncA   | deamidation       |  (NAD+ salvage)
   (+H2O, -NH3)               |
          v                   |
   Nicotinic acid (Na) ---PncB (Preiss-Handler, +PRPP)---> NaMN
                                                            |
                                              NadD (adenylyltransferase)
                                                            v
                                                          NaAD
                                                            |
                                              NadE (NAD synthetase, +NH3/Gln)
                                                            v
                                                          NAD(+)  --> (cycle repeats)
```

### Finding 5 — PncA modulates CobB (sirtuin) signaling by clearing the inhibitor nicotinamide

Nicotinamide is not only a metabolite but also a product and **feedback inhibitor** of NAD⁺-dependent sirtuin deacetylases. Gallego-Jara et al. ([PMID: 29253849](https://pubmed.ncbi.nlm.nih.gov/29253849/)) kinetically characterized **CobB**, the principal *E. coli* sirtuin deacetylase, demonstrated nicotinamide inhibition in vitro, measured intracellular nicotinamide concentrations, and tested a *pncA* deletion strain. They found that "*a nicotinamidase deletion strain was thus phenotypically characterized, and it behaved similarly to the ΔcobB strain*" — the expected result if loss of PncA causes nicotinamide to accumulate and inhibit CobB. They concluded that "*the results suggest that nicotinamide can act as a CobB regulator in vivo.*"

This finding sharpens the mechanistic role of PncA: beyond feeding NAD⁺ synthesis, by keeping intracellular nicotinamide low PncA **relieves feedback inhibition of CobB**, thereby permitting sirtuin-dependent protein deacetylation. PncA thus sits at the junction of NAD⁺ metabolism and acetylation-based regulatory signaling.

### Finding 6 — Substrate specificity: nicotinamide strongly preferred; pyrazinamide a secondary analog substrate

The enzyme's two names — nicotinamidase and pyrazinamidase — reflect its dual activity, but the two are not equal. In *E. coli*, both nicotinamide and the analog pyrazinamide are hydrolyzed by the same enzyme, with activities that co-purify and co-vary ([PMID: 8726014](https://pubmed.ncbi.nlm.nih.gov/8726014/)). Quantitatively, however, nicotinamide is strongly favored. Kinetic characterization of a bacterial nicotinamidase homolog (*Oceanobacillus iheyensis* OiNIC) showed "*the enzyme was more nicotinamidase (kcat/Km = 43.5 mM⁻¹s⁻¹) than pyrazinamidase (kcat/Km = 3.2 mM⁻¹s⁻¹)*" — roughly a **14-fold preference** for nicotinamide ([PMID: 23451075](https://pubmed.ncbi.nlm.nih.gov/23451075/)). Site-directed mutagenesis in that study confirmed that the catalytic cysteine and metal-binding residues govern amide specificity.

Specificity is also bounded by the ring: family nicotinamidases are selective for **pyridine/pyrazine-ring carboxamides** and exclude non-pyridine amides. In the mycobacterial comparison, "*benzamide is hydrolyzed by PzaA but not by PncA*" ([PMID: 10986252](https://pubmed.ncbi.nlm.nih.gov/10986252/)), showing that PncA-type enzymes discriminate against benzamide. The practical upshot is that **nicotinamide is the true physiological substrate**, while the pyrazinamidase activity — famous because it activates the tuberculosis prodrug pyrazinamide to pyrazinoic acid in mycobacteria — is an adventitious, lower-efficiency reaction on a structural analog.

**Substrate comparison:**

| Substrate | Ring | Relative efficiency | Role |
|---|---|---|---|
| Nicotinamide | Pyridine-3-carboxamide | High (kcat/Km ≈ 43.5 mM⁻¹s⁻¹ in OiNIC) | Physiological substrate |
| Pyrazinamide | Pyrazine-2-carboxamide | ~14× lower (≈ 3.2 mM⁻¹s⁻¹) | Fortuitous analog substrate |
| Benzamide | Benzene (non-N) | Not hydrolyzed by PncA | Excluded (specificity boundary) |

---

## Mechanistic Model / Interpretation

PncA is best understood as a **soluble, cytoplasmic, Zn²⁺-dependent cysteine hydrolase that opens the NAD⁺ salvage cycle** in *E. coli*. The coherent narrative connecting all six findings is as follows.

*E. coli* continuously consumes NAD⁺ in reactions that break its pyrophosphate bond — most prominently DNA ligase, which uses NAD⁺ as the adenylyl donor and releases nicotinamide mononucleotide; downstream processing yields free nicotinamide (Finding 4; [PMID: 7021549](https://pubmed.ncbi.nlm.nih.gov/7021549/)). Rather than discarding this pyridine ring, the cell recycles it. **PncA performs the first committed, irreversible step: deamidation of nicotinamide to nicotinic acid** (Findings 1, 3). The chemistry is a classic metallo-cysteine-hydrolase mechanism — the catalytic cysteine thiolate (activated by the aspartate general base) attacks the amide carbonyl held in place by the Zn²⁺ Lewis acid, ammonia leaves, a nicotinoyl–thioester acyl-enzyme forms, and a metal-activated water hydrolyzes it to nicotinic acid (Finding 2; [PMID: 11714269](https://pubmed.ncbi.nlm.nih.gov/11714269/), [PMID: 20853856](https://pubmed.ncbi.nlm.nih.gov/20853856/), [PMID: 24413890](https://pubmed.ncbi.nlm.nih.gov/24413890/)). Nicotinic acid is then handed to PncB and the Preiss–Handler/NAD-synthetase steps to regenerate NAD⁺ (Finding 4; [PMID: 26443758](https://pubmed.ncbi.nlm.nih.gov/26443758/)).

This deamidation has a **second, regulatory consequence**. Nicotinamide is a feedback inhibitor of the NAD⁺-dependent sirtuin CobB. By keeping cytoplasmic nicotinamide low, PncA relieves CobB inhibition and thereby licenses sirtuin-mediated deacetylation — so a *pncA* deletion phenocopies a *cobB* deletion (Finding 5; [PMID: 29253849](https://pubmed.ncbi.nlm.nih.gov/29253849/)). PncA thus serves two intertwined purposes with a single reaction: it **feeds carbon/nitrogen back into NAD⁺ biosynthesis** and **tunes an NAD⁺-dependent signaling node** by controlling the inhibitor concentration.

The enzyme's dual naming (nicotinamidase = pyrazinamidase) is a historical artifact of substrate promiscuity. The physiologically meaningful substrate is nicotinamide; pyrazinamide is simply the closest medically relevant analog, differing by a single ring nitrogen, and is turned over ~14-fold less efficiently (Finding 6; [PMID: 23451075](https://pubmed.ncbi.nlm.nih.gov/23451075/)). The clinical fame of the pyrazinamidase activity (prodrug activation in *M. tuberculosis*) should not be mistaken for the enzyme's biological purpose in *E. coli*, which is NAD⁺ salvage.

**Integrated role of PncA:**

```
                        +------------------------------+
   Nicotinamide ------> |   PncA (cytoplasm)           |
   (from NAD+ turnover) |   Zn2+/Cys-Asp-Lys hydrolase |---> Nicotinic acid --> PncB --> NAD+
                        +------------------------------+                         (salvage)
                                     |
                                     |  lowers [nicotinamide]
                                     v
                        Relieves feedback inhibition of CobB (sirtuin)
                                     |
                                     v
                        Permits NAD+-dependent protein deacetylation
```

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [8726014](https://pubmed.ncbi.nlm.nih.gov/8726014/) | *Identification, cloning, and expression of the E. coli pncA gene* | **Primary identity evidence.** Genetic + biochemical proof that one *E. coli* enzyme has both nicotinamidase and pyrazinamidase activity; deamidation lets cells use nicotinamide as sole N source. |
| [11714269](https://pubmed.ncbi.nlm.nih.gov/11714269/) | *Crystal structure of a pyrazinamidase from Pyrococcus horikoshii* | Defines the conserved Asp–Lys–Cys triad, *cis*-peptide, and metal site of the family. |
| [20853856](https://pubmed.ncbi.nlm.nih.gov/20853856/) | *High-resolution structures of S. pneumoniae nicotinamidase* | Traps the covalent nicotinoyl–thioester intermediate; situates the family as the entry step of NAD⁺ salvage, absent in mammals. |
| [24413890](https://pubmed.ncbi.nlm.nih.gov/24413890/) | *QM/MM study of nicotinamidase mechanism* | Confirms catalytic Cys nucleophile, Asp base, Lys stabilization, Zn Lewis acid. |
| [10986252](https://pubmed.ncbi.nlm.nih.gov/10986252/) | *Expression of M. smegmatis pyrazinamidase in M. tuberculosis* | Cytoplasmic localization of PncA/PZase; benzamide excluded → pyridine/pyrazine-ring specificity. |
| [26443758](https://pubmed.ncbi.nlm.nih.gov/26443758/) | *Biogenesis and Homeostasis of NAD Cofactor* (EcoSal review) | Authoritative statement that PncA + PncB are the major *E. coli* pyridine-ring salvage pathway. |
| [7021549](https://pubmed.ncbi.nlm.nih.gov/7021549/) | *The pyridine nucleotide cycle in E. coli* | Shows NAD⁺ turnover (pyrophosphate cleavage) generates the nicotinamide that PncA recycles. |
| [29253849](https://pubmed.ncbi.nlm.nih.gov/29253849/) | *Characterization of CobB kinetics and inhibition by nicotinamide* | Links PncA to sirtuin signaling: Δ*pncA* phenocopies Δ*cobB*; nicotinamide is an in vivo CobB regulator. |
| [23451075](https://pubmed.ncbi.nlm.nih.gov/23451075/) | *Novel nicotinamidase from Oceanobacillus iheyensis* | Quantifies ~14× kinetic preference for nicotinamide over pyrazinamide; mutagenesis maps specificity residues. |
| [39537945](https://pubmed.ncbi.nlm.nih.gov/39537945/) | *In silico nicotinamide analogs as nicotinamidase inhibitors (MRSA)* | Reaffirms PncA = NAD⁺ salvage entry enzyme feeding Preiss–Handler; antibiotic-target rationale. |
| [43001968](https://pubmed.ncbi.nlm.nih.gov/43001968/) | *Mechanistic insights into nicotinamidase by Co(II) EPR* | Independent spectroscopic confirmation of the thioester intermediate and metal-site geometry. |

**Supporting/contextual literature.** Salmonella genetics (*pncA/pncB/pncC* mutants; [PMID: 220211](https://pubmed.ncbi.nlm.nih.gov/220211/), [PMID: 6222034](https://pubmed.ncbi.nlm.nih.gov/6222034/)) corroborate the deamidase role and genetic organization of the salvage cycle. Comparative mycobacterial studies ([PMID: 9811635](https://pubmed.ncbi.nlm.nih.gov/9811635/), [PMID: 10049264](https://pubmed.ncbi.nlm.nih.gov/10049264/), [PMID: 506551](https://pubmed.ncbi.nlm.nih.gov/506551/)) document the shared nicotinamidase/pyrazinamidase activity and the "pyrazinamidase is an artifact of low substrate specificity" interpretation. Related cysteine-hydrolase structures such as maleamate amidohydrolase NicF ([PMID: 22214383](https://pubmed.ncbi.nlm.nih.gov/22214383/)) independently reproduce the Asp–Lys–Cys/*cis*-peptide fold. Yeast and microbiome studies ([PMID: 22539348](https://pubmed.ncbi.nlm.nih.gov/22539348/), [PMID: 36864222](https://pubmed.ncbi.nlm.nih.gov/36864222/), [PMID: 40817598](https://pubmed.ncbi.nlm.nih.gov/40817598/)) illustrate the broader physiological reach of nicotinamidase-driven nicotinamide→nicotinic acid conversion in NAD⁺ homeostasis and sirtuin regulation.

---

## Limitations and Knowledge Gaps

1. **No crystal structure of the *E. coli* enzyme in the reviewed records.** The detailed mechanism (triad, *cis*-peptide, metal site, thioester intermediate) is established on homologs (*P. horikoshii*, *S. pneumoniae*, yeast Pnc1). While sequence/domain conservation makes transfer of the mechanism to *E. coli* PncA secure, direct structural confirmation of P21369 and explicit identification of its catalytic residue numbering would strengthen the annotation.

2. **Metal identity in *E. coli* PncA not directly measured here.** The family uses Zn²⁺ (and tolerates other divalent metals experimentally, e.g., Co²⁺ substitution). The specific metal content and stoichiometry of the native *E. coli* enzyme were inferred from homologs rather than measured in the records reviewed.

3. **Quantitative kinetics of *E. coli* PncA are indirect.** The strong nicotinamide-over-pyrazinamide preference (~14×) is from the *O. iheyensis* homolog; *E. coli*-specific kcat/Km values for nicotinamide vs. pyrazinamide were not tabulated here, although parallel co-variation of the two activities is documented.

4. **Regulatory wiring of CobB modulation is correlational.** The Δ*pncA*/Δ*cobB* phenocopy and in vitro nicotinamide inhibition are strong, but the exact intracellular nicotinamide thresholds that gate CobB activity under different growth conditions remain to be mapped.

5. **Pathway flux under physiological conditions.** The relative contribution of PncA-mediated recycling versus de novo NAD⁺ synthesis across growth phases and nutrient states is not fully quantified in this review.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the *E. coli* PncA structure** (apo, substrate-bound, and intermediate-trapped) by X-ray crystallography or cryo-EM to confirm the catalytic Cys/Asp/Lys residue numbering, metal coordination, and *cis*-peptide directly in P21369.

2. **Steady-state kinetics on purified *E. coli* PncA** with nicotinamide, pyrazinamide, and negative controls (benzamide, isonicotinamide), reporting kcat, Km, and kcat/Km to quantify the physiological preference natively and benchmark against homologs.

3. **Metal-dependence and metal-identity assays** (ICP-MS for native metal content; activity vs. chelators; Co²⁺/Mn²⁺ substitution with EPR) to establish the native cofactor and its catalytic role in the *E. coli* enzyme.

4. **Targeted metabolomics in Δ*pncA* vs. wild type** to measure intracellular nicotinamide, nicotinic acid, and NAD⁺ pools, directly testing the salvage-flux and CobB-inhibition models.

5. **Acetylome profiling (quantitative MS) in Δ*pncA*, Δ*cobB*, and double mutants** to confirm that nicotinamide accumulation in Δ*pncA* raises protein acetylation via CobB inhibition, cementing the signaling link.

6. **Growth/physiology assays** using nicotinamide as sole nitrogen source and ¹⁵N/¹⁴C isotope tracing to quantify in vivo deamidation flux and the fraction of NAD⁺ regenerated through the PncA–PncB route under defined conditions.

---

*Gene verification note:* The gene symbol **pncA**, organism (*E. coli* K-12), EC number (3.5.1.19), protein family (isochorismatase-like / cysteine-hydrolase superfamily; Pfam PF00857), and the literature all consistently describe the same entity — nicotinamidase/pyrazinamidase. There is no ambiguity: the primary *E. coli* study ([PMID: 8726014](https://pubmed.ncbi.nlm.nih.gov/8726014/)) matches UniProt P21369 (gene b1768) directly. Mycobacterial *pncA* literature concerns orthologs of the same enzyme family (sharing ~28% identity with the *E. coli* protein) and is used here only as mechanistic/comparative support, not as a substitute identity.


## Artifacts

- [OpenScientist final report](pncA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pncA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8726014
2. PMID:11714269
3. PMID:20853856
4. PMID:24413890
5. PMID:43001968
6. PMID:39537945
7. PMID:10986252
8. PMID:26443758
9. PMID:7021549
10. PMID:29253849
11. PMID:23451075
12. PMID:6222034
13. PMID:9811635
14. PMID:10049264
15. PMID:22214383
16. PMID:22539348
17. PMID:36864222
18. PMID:40817598