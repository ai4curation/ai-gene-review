---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T15:13:57.549471'
end_time: '2026-07-23T15:21:34.297528'
duration_seconds: 456.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaG
  gene_symbol: paaG
  uniprot_accession: Q88HS0
  protein_description: 'SubName: Full=1,2-epoxyphenylacetyl-CoA isomerase {ECO:0000313|EMBL:AAN68890.1};
    EC=5.3.3.18 {ECO:0000313|EMBL:AAN68890.1};'
  gene_info: Name=paaG {ECO:0000313|EMBL:AAN68890.1}; OrderedLocusNames=PP_3283 {ECO:0000313|EMBL:AAN68890.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the enoyl-CoA hydratase/isomerase family.
  protein_domains: ClpP/crotonase-like_dom_sf. (IPR029045); Enoyl-CoA_hydra/iso. (IPR001753);
    Enoyl-CoA_hydra_C. (IPR014748); PaaB1. (IPR011968); ECH_1 (PF00378)
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
  path: paaG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS0
- **Protein Description:** SubName: Full=1,2-epoxyphenylacetyl-CoA isomerase {ECO:0000313|EMBL:AAN68890.1}; EC=5.3.3.18 {ECO:0000313|EMBL:AAN68890.1};
- **Gene Information:** Name=paaG {ECO:0000313|EMBL:AAN68890.1}; OrderedLocusNames=PP_3283 {ECO:0000313|EMBL:AAN68890.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the enoyl-CoA hydratase/isomerase family.
- **Key Domains:** ClpP/crotonase-like_dom_sf. (IPR029045); Enoyl-CoA_hydra/iso. (IPR001753); Enoyl-CoA_hydra_C. (IPR014748); PaaB1. (IPR011968); ECH_1 (PF00378)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaG** (gene ID: paaG, UniProt: Q88HS0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: paaG (PP_3283, UniProt Q88HS0)
## *Pseudomonas putida* KT2440 — ring-1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18)

---

## 1. Summary (Answer to the Research Question)

**paaG** encodes **ring-1,2-epoxyphenylacetyl-CoA isomerase** (also called oxepin-CoA–forming isomerase; EC 5.3.3.18), a **cytoplasmic**, crotonase-superfamily enzyme that catalyzes a key step of the **aerobic "hybrid" phenylacetate (PAA) degradation pathway**. Its primary reaction is the intramolecular isomerization of the reactive, non-aromatic **1,2-epoxyphenylacetyl-CoA** into the seven-membered oxygen-heterocycle **oxepin-CoA** (2-oxepin-2(3H)-ylideneacetyl-CoA). This step converts the toxic ring-epoxide produced by the PaaABC(D)E oxygenase into an α,β-unsaturated CoA-ester that is poised for hydrolytic ring cleavage (by PaaZ) and β-oxidation, ultimately yielding **acetyl-CoA and succinyl-CoA** that feed central metabolism. The protein is a soluble homotrimer of the enoyl-CoA hydratase/isomerase (crotonase) fold and works together with the pathway's other β-oxidation-like enzymes (notably PaaF, with which it forms a PaaFG complex).

**Gene-identity verification:** The UniProt target (Q88HS0; gene *paaG*; locus PP_3283; family = enoyl-CoA hydratase/isomerase; domains ClpP/crotonase-like IPR029045, Enoyl-CoA hydratase/isomerase IPR001753, PaaB1 IPR011968, PF00378 ECH_1; EC 5.3.3.18) is **fully consistent** with the literature on bacterial PaaG. The landmark pathway paper explicitly states the pathway operates in *Pseudomonas putida* as well as *E. coli*, so mechanistic knowledge transfers directly to PP_3283. No gene-symbol ambiguity was encountered.

---

## 2. Biological Context: The Phenylacetate (paa) Catabolon

Phenylacetic acid (PAA) is a central hub intermediate in the aerobic catabolism of many aromatic compounds — phenylalanine, 2-phenylethylamine, 2-phenylethanol, styrene, lignin-related aromatics, and various environmental pollutants all converge on PAA (Teufel et al. 2010, PMID 20660314; Ismail et al. 2003, PMID 12846838). In *P. putida* this is organized as the **phenylacetyl-CoA "catabolon"**: peripheral routes that convert diverse substrates to PAA, feeding a common core that degrades phenylacetyl-CoA (Olivera et al. 1998, PMID 9600981; García et al. 2000, PMID 11010921). The true inducer of the core pathway is **phenylacetyl-CoA itself** (García et al. 2000, PMID 11010921).

Unlike classical aerobic aromatic catabolism (which uses ring-hydroxylating dioxygenases and oxygenolytic ring cleavage of free acids), the PAA pathway is a **"hybrid" pathway**: all intermediates are handled as **coenzyme-A thioesters**, and ring cleavage is **non-oxygenolytic** (Fuchs 2008, PMID 18378589; Teufel et al. 2010, PMID 20660314). The pathway occurs in ~16% of sequenced bacterial genomes (Teufel et al. 2010, PMID 20660314).

### Pathway sequence and PaaG's position

1. **PaaK** — phenylacetate–CoA ligase → **phenylacetyl-CoA**
2. **PaaABC(D)E** — multicomponent (di-iron) ring-1,2-monooxygenase/epoxidase → **1,2-epoxyphenylacetyl-CoA** (an unusual, reactive, non-aromatic ring epoxide; this enzyme is also a bifunctional oxygenase/deoxygenase that can reverse epoxidation to limit toxic epoxide build-up — Teufel, Friedrich & Fuchs 2012, PMID 22398448)
3. **PaaG (this gene)** — **ring-1,2-epoxyphenylacetyl-CoA isomerase** → **oxepin-CoA** ⭐
4. **PaaZ** — bifunctional (R)-enoyl-CoA hydratase + NADP⁺ aldehyde dehydrogenase → hydrolytic ring-opening then oxidation to **3-oxo-5,6-dehydrosuberyl-CoA** (Teufel et al. 2011, PMID 21296885)
5. **PaaF / PaaH / PaaJ** — enoyl-CoA hydratase / 3-hydroxyacyl-CoA dehydrogenase / thiolase (β-oxidation-like steps)
6. **Products:** **acetyl-CoA + succinyl-CoA** → TCA cycle (Teufel et al. 2010, PMID 20660314)

---

## 3. Primary Function: The Reaction Catalyzed

### 3.1 Core reaction and substrate specificity

PaaG catalyzes:

> **1,2-epoxyphenylacetyl-CoA → oxepin-CoA (2-oxepin-2(3H)-ylideneacetyl-CoA)**

This is an **intramolecular isomerization** — the epoxide oxygen is incorporated into a ring-expanded seven-membered oxepin enol-ether without net change in molecular formula, consistent with its EC class **5.3.3 (intramolecular oxidoreductases, transposing C=C bonds)** and specific number **EC 5.3.3.18**.

- Teufel et al. (2010, PMID 20660314): *"The reactive nonaromatic epoxide is isomerized to a seven-member O-heterocyclic enol ether, an oxepin."*
- Spieker, Saleem-Batcha & Teufel (2019, PMID 31689071): *"1,2-epoxyphenylacetyl-CoA is converted by PaaG into the heterocyclic oxepin-CoA."*

**Substrate specificity:** PaaG acts specifically on the CoA-thioester ring-epoxide of the PAA pathway; the CoA moiety and the aromatic-derived ring are both accommodated in a large active-site cavity (Kichise et al. 2009, PMID 19452559). By generating an **α,β-unsaturated CoA-ester**, PaaG "predisposes" the molecule for the subsequent hydrolytic ring-cleavage and β-oxidation (Spieker et al. 2019, PMID 31689071).

### 3.2 A verified second (moonlighting) isomerase role

Spieker et al. (2019, PMID 31689071) *"verify that PaaG adopts a second role in aromatic catabolism"* — i.e., beyond forming oxepin-CoA it catalyzes a further isomerization step in the pathway, consistent with the enzyme's Δ³,Δ²-enoyl-CoA-isomerase-like active site. This dual functionality is efficient use of a single crotonase scaffold.

### 3.3 Physiological requirement (genetic evidence)

Precise single-gene genetics confirm the step:
- In *E. coli* K-12, *"mutants with a deletion of the paaF, paaG, paaH, paaJ or paaZ gene are unable to grow with phenylacetate as carbon source"* (Ismail et al. 2003, PMID 12846838).
- A *paaG* mutant fed ¹³C-phenylacetate accumulated **ring-1,2-dihydroxy-1,2-dihydrophenylacetyl lactone**, and *paaG/paaZ* mutants also formed **ortho-hydroxyphenylacetate** (a known dead-end product) — showing that in the absence of PaaG the reactive epoxide collapses non-enzymatically, and pinpointing PaaG immediately downstream of ring epoxidation (Ismail et al. 2003, PMID 12846838).

---

## 4. Structure and Mechanism (Evidence from Structural Biology)

- **Fold/family:** PaaG is a member of the **crotonase (enoyl-CoA hydratase/isomerase) superfamily** — matching the Q88HS0 annotations (ClpP/crotonase-like IPR029045; Enoyl-CoA hydratase/isomerase IPR001753; PF00378). Kichise et al. (2009, PMID 19452559): *"A phenylacetic acid degradation protein PaaG is a member of the crotonase superfamily, and is a candidate non-oxygenolytic ring-opening enzyme."*
- **Quaternary structure:** homotrimer — *"PaaG consists of three identical subunits related by local three-fold symmetry"* (T. thermophilus PaaG, 1.85 Å; Kichise et al. 2009, PMID 19452559). Crotonase enzymes typically assemble as trimers/dimers-of-trimers (hexamers).
- **Active site / catalytic residue:** *"Asp136 is the only conserved polar residue in the active site"*, positioned analogously to the catalytic residues of 4-chlorobenzoyl-CoA dehalogenase and peroxisomal Δ³,Δ²-enoyl-CoA isomerase, *"indicating that PaaG may undergo isomerization or a ring-opening reaction"* (Kichise et al. 2009, PMID 19452559). The active-site cavity is large enough to accommodate the ring substrate, and helix H2 adopts alternative conformations, implying substantial conformational motion during catalysis.
- **Complex formation:** PaaG forms a **stable PaaFG complex** with PaaF: *"another stable complex, PaaFG, an enoyl-CoA hydratase and enoyl-Coa isomerase, both belonging to the crotonase superfamily"*, with *"a four-layered structure composed of homotrimeric discs of PaaF and PaaG"* (Grishin et al. 2012, PMID 22961985). This physical coupling of consecutive β-oxidation-like steps may allow substrate channeling.

The catalytic strategy (crotonase oxyanion hole + a single acidic residue promoting enolate/carbanion intermediates) is well suited to opening the strained epoxide and re-forming the C–O ring as the oxepin enol-ether.

---

## 5. Subcellular Localization

PaaG functions in the **cytoplasm (cytosol)**:
- It acts on **CoA-thioester** substrates generated intracellularly (phenylacetyl-CoA is produced by cytoplasmic PaaK and is the pathway inducer; García et al. 2000, PMID 11010921).
- The protein is a **soluble crotonase-fold homotrimer** with no signal peptide or transmembrane region, and it forms a soluble multi-enzyme assembly with PaaF (Grishin et al. 2012, PMID 22961985; Kichise et al. 2009, PMID 19452559).

There is no evidence for membrane association or secretion; the entire PAA core pathway is a soluble cytoplasmic module.

---

## 6. Pathway Significance and Downstream Connections

- **Detoxification / channeling:** By rapidly converting the reactive ring-epoxide to oxepin-CoA, PaaG prevents accumulation of the toxic epoxide and of dead-end products (2-hydroxyphenylacetate, dihydrodiol lactone). The upstream oxygenase (PaaABC(D)E) has its own "escape" deoxygenase activity to limit epoxide toxicity when downstream steps stall (Teufel, Friedrich & Fuchs 2012, PMID 22398448), underscoring how tightly the epoxide→oxepin transition (PaaG) is controlled.
- **Metabolic branch point / secondary metabolism:** Oxepin-CoA (the PaaG product) and the downstream reactive aldehyde are precursors of tropone/tropolone secondary metabolites, including **tropodithietic acid** (an antibiotic/quorum-sensing signal) and ω-cycloheptyl fatty acids (Teufel et al. 2011, PMID 21296885; Spieker et al. 2019, PMID 31689071). Thus PaaG activity connects primary aromatic catabolism to natural-product biosynthesis.
- **Environmental/biotech relevance in *P. putida*:** The PAA catabolon underlies degradation of styrene and phenyl-derived pollutants and is linked to biosynthesis of medium-chain-length polyhydroxyalkanoate (PHA) bioplastics in *Pseudomonas* (O'Leary et al. 2005, PMID 16085828; García et al. 1999, PMID 10506180).

---

## 7. Supported vs. Refuted Hypotheses

| Hypothesis | Verdict | Key evidence |
|---|---|---|
| paaG (Q88HS0/PP_3283) encodes ring-1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18) producing oxepin-CoA | **Supported** | Teufel 2010 (PMID 20660314); Spieker 2019 (PMID 31689071) |
| PaaG belongs to the crotonase (enoyl-CoA hydratase/isomerase) superfamily; homotrimeric; single catalytic Asp | **Supported** | Kichise 2009 (PMID 19452559); UniProt domain annotation |
| PaaG is essential for growth on phenylacetate | **Supported** | Ismail 2003 (PMID 12846838) |
| PaaG acts in the cytoplasm on CoA-thioesters, in a PaaFG complex | **Supported** | Grishin 2012 (PMID 22961985); García 2000 (PMID 11010921) |
| PaaG has an additional (second) isomerase role in the pathway | **Supported** | Spieker 2019 (PMID 31689071) |
| PaaG is a membrane-bound or oxygenolytic ring-cleavage enzyme | **Refuted** | Ring cleavage is non-oxygenolytic and performed by PaaZ; PaaG is a soluble isomerase (Teufel 2010, PMID 20660314; Teufel 2011, PMID 21296885) |
| The gene symbol "paaG" is ambiguous for this protein | **Refuted** | Symbol, organism, family, domains and EC all coherent with the PAA-pathway PaaG literature |

---

## 8. Limitations and Future Directions

- **Direct biochemistry is on orthologs, not PP_3283 itself.** The enzymatic and structural characterizations were performed in *E. coli*, *Thermus thermophilus*, *Azoarcus evansii*, and related systems; *P. putida* KT2440 PaaG function is inferred by strong orthology and the explicit inclusion of *P. putida* in the pathway paradigm (Teufel et al. 2010, PMID 20660314). Strain-specific enzymology (kinetics, kcat/KM, substrate scope) of Q88HS0 has not been individually reported.
- **No experimental 3D structure of Q88HS0.** Structural inferences rely on the *T. thermophilus* PaaG structure and the *E. coli* PaaFG complex; an AlphaFold model of Q88HS0 could confirm the crotonase fold, trimer interface, and Asp active-site geometry.
- **The precise nature of PaaG's "second role"** (the exact downstream isomerization substrate/product) merits closer reading of Spieker et al. 2019 full text.
- **Regulation specifics** (σ⁵⁴/PaaX control of the KT2440 paa operon) were not deeply examined here but are relevant to when PaaG is expressed (cf. O'Leary et al. 2011, PMID 21995721 for *P. putida* CA-3).

---

## 9. Key References

1. Teufel R, Mascaraque V, Ismail W, et al. **Bacterial phenylalanine and phenylacetate catabolic pathway revealed.** *PNAS* 2010. PMID 20660314. *(Landmark pathway elucidation; oxepin isomerization.)*
2. Spieker M, Saleem-Batcha R, Teufel R. **Structural and Mechanistic Basis of an Oxepin-CoA Forming Isomerase in Bacterial Primary and Secondary Metabolism.** 2019. PMID 31689071. *(Direct PaaG mechanism; second role.)*
3. Ismail W, El-Said Mohamed M, et al. **Functional genomics by NMR spectroscopy. Phenylacetate catabolism in Escherichia coli.** 2003. PMID 12846838. *(paaG deletion genetics; trapped intermediates.)*
4. Kichise T, Hisano T, Takeda K, Miki K. **Crystal structure of phenylacetic acid degradation protein PaaG from Thermus thermophilus HB8.** 2009. PMID 19452559. *(Crotonase fold; homotrimer; Asp136.)*
5. Grishin AM, et al. **Protein–protein interactions in the β-oxidation part of the phenylacetate utilization pathway: crystal structure of the PaaF–PaaG hydratase–isomerase complex.** 2012. PMID 22961985.
6. Teufel R, Gantert C, Voss M, et al. **Studies on the mechanism of ring hydrolysis in phenylacetate degradation: a metabolic branching point.** 2011. PMID 21296885. *(PaaZ ring cleavage; oxepin fate; tropodithietic acid link.)*
7. Teufel R, Friedrich T, Fuchs G. **An oxygenase that forms and deoxygenates toxic epoxide.** 2012. PMID 22398448. *(PaaABCE epoxidase/deoxygenase; epoxide toxicity.)*
8. Olivera ER, et al. **Molecular characterization of the phenylacetic acid catabolic pathway in Pseudomonas putida U: the phenylacetyl-CoA catabolon.** 1998. PMID 9600981.
9. García B, et al. **Phenylacetyl-CoA is the true inducer of the phenylacetic acid catabolism pathway in Pseudomonas putida U.** 2000. PMID 11010921.
10. Fuchs G. **Anaerobic metabolism of aromatic compounds.** 2008. PMID 18378589. *(Hybrid pathway concept.)*


## Artifacts

- [OpenScientist final report](paaG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaG-deep-research-openscientist_artifacts/final_report.pdf)