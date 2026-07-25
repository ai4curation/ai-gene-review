---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T15:03:30.106199'
end_time: '2026-07-23T15:15:11.397536'
duration_seconds: 701.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaB
  gene_symbol: paaB
  uniprot_accession: Q88HS6
  protein_description: 'SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase regulatory
    subunit {ECO:0000313|EMBL:AAN68884.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68884.1};'
  gene_info: Name=paaB {ECO:0000313|EMBL:AAN68884.1}; OrderedLocusNames=PP_3277 {ECO:0000313|EMBL:AAN68884.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: PaaB. (IPR009359); PaaB_sf. (IPR038693); PaaB (PF06243)
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
  path: paaB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS6
- **Protein Description:** SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase regulatory subunit {ECO:0000313|EMBL:AAN68884.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68884.1};
- **Gene Information:** Name=paaB {ECO:0000313|EMBL:AAN68884.1}; OrderedLocusNames=PP_3277 {ECO:0000313|EMBL:AAN68884.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PaaB. (IPR009359); PaaB_sf. (IPR038693); PaaB (PF06243)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaB** (gene ID: paaB, UniProt: Q88HS6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: paaB (Q88HS6 / PP_3277) in *Pseudomonas putida* KT2440

## Gene / Protein Identity Verification

- **UniProt accession:** Q88HS6
- **Gene name / locus:** *paaB* / PP_3277
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
- **UniProt description:** "Ring 1,2-phenylacetyl-CoA epoxidase regulatory subunit," EC 1.14.13.149
- **Domains:** PaaB (Pfam PF06243; InterPro IPR009359, IPR038693)

**Verification outcome — CONFIRMED.** The gene symbol *paaB*, the EC number 1.14.13.149 (1,2-phenylacetyl-CoA epoxidase), the PaaB Pfam/InterPro domain, and the position of PP_3277 within the *P. putida* KT2440 *paa* gene cluster all consistently identify this protein as a subunit of the **phenylacetyl-CoA ring-1,2-epoxidase (monooxygenase) complex** of the aerobic phenylacetate degradation pathway. This is the correct gene; the literature cited below is specific to this protein family and pathway, which is explicitly documented in *P. putida* (Teufel et al. 2010, PMID 20660314). A minor nomenclature caveat is noted in Limitations (subunit-letter usage differs slightly between organisms/authors).

---

## 1. Summary (Answer to the Research Question)

*paaB* encodes a small **structural/assembly subunit** of the multicomponent **phenylacetyl-CoA epoxidase (monooxygenase) complex, PaaABCE**, which catalyzes the committed, oxygen-dependent step of the bacterial aerobic phenylacetate catabolic pathway: insertion of oxygen into the aromatic ring of phenylacetyl-CoA to form ring-1,2-epoxyphenylacetyl-CoA (EC 1.14.13.149). PaaB is **not catalytic** — it carries no metal or substrate site — but instead forms a **homodimer that bridges two catalytic PaaAC heterodimers**, organizing the complex into an active heterohexamer. The complex operates in the **cytoplasm** on the CoA-thioester substrate as the ring-activating funnel step feeding phenylalanine, styrene, and environmental aromatics into central metabolism (acetyl-CoA + succinyl-CoA).

---

## 2. Primary Function

### 2.1 The reaction and the complex
The phenylacetate (PA) pathway processes intermediates as **coenzyme A thioesters**. Free PA is first activated to **phenylacetyl-CoA (PA-CoA)** by a PA-CoA ligase (PaaK/PaaF). The central enzyme, the **four-subunit phenylacetyl-CoA monooxygenase (PA-CoA MO)**, then epoxidizes the aromatic ring:

> phenylacetyl-CoA + O₂ + NADPH → ring-1,2-epoxyphenylacetyl-CoA + NADP⁺ + H₂O (EC 1.14.13.149)

The aromatic ring "becomes activated to a ring 1,2-epoxide by a distinct multicomponent oxygenase" (Teufel et al. 2010, PMID 20660314). Remarkably, the same complex is **bifunctional**: it can also run in reverse, mediating "the NADPH-dependent removal of the epoxide oxygen, regenerating phenylacetyl-CoA with formation of water," an intrinsic detoxification/escape mechanism to prevent accumulation of the reactive epoxide (Teufel, Friedrich & Fuchs 2012, PMID 22398448). Catalysis depends on a **carboxylate-bridged di-iron centre** housed in the oxygenase subunit PaaA.

### 2.2 Subunit roles and PaaB's specific function
The complex is a **new family of monooxygenases** that "differs in subunit organization from other monooxygenases" (Grishin et al. 2013, PMID 24055609). Assigning the subunits:

- **PaaA** — the **oxygenase (catalytic) subunit**, containing the di-iron active site where ring epoxidation occurs.
- **PaaC** — a **structural subunit** that partners PaaA to form the catalytic **PaaAC heterodimer**.
- **PaaE** — the **NAD(P)H-dependent reductase** that supplies electrons to the di-iron centre; a conserved "lysine bridge" constellation (Lys68, Glu49, Glu72, Asp126) near the Fe site in PaaA forms part of the electron-transfer path from PaaE. Mutating this bridge reduced activity 20–50-fold (Grishin et al. 2013, PMID 24055609).
- **PaaB (this protein, Q88HS6)** — a **structural/scaffolding subunit**. Structural studies (low-resolution crystallography, electron microscopy, small-angle X-ray scattering) showed "the PaaACB complex forms **heterohexamers, with a homodimer of PaaB bridging two PaaAC heterodimers**" (Grishin et al. 2013, PMID 24055609). PaaB "is **unrelated to the small subunits of homologous monooxygenases**," making it a distinctive feature of this enzyme family.

Thus PaaB's precise role is **architectural/regulatory**: it does not bind iron, O₂, NAD(P)H, or the CoA substrate itself, but is required for correct **oligomerization and assembly** of the active PaaABCE complex. The UniProt label "regulatory subunit" reflects this non-catalytic, assembly/organizing function.

---

## 3. Substrate Specificity

The complex acts specifically on **phenylacetyl-CoA (the CoA thioester), not on free phenylacetate**. The CoA-thioester activation both delivers the substrate to the enzymes and, mechanistically, is part of a "hybrid" strategy combining aerobic ring oxygenation with anaerobic-style CoA derivatization (Grishin & Cygler 2015, PMID 26075354). The PA pathway is the convergence point ("phenylacetyl-CoA catabolon") for many aromatic sources — phenylalanine, 2-phenylethylamine, styrene, lignin-related compounds, and man-made pollutants — all of which funnel into PA-CoA before the PaaABCE epoxidation step (Teufel et al. 2010, PMID 20660314; Alonso et al. 2003, PMID 14597173). PaaB, as a structural subunit, does not independently confer substrate specificity; specificity resides in the PaaA catalytic site.

---

## 4. Subcellular Localization

The PaaABCE complex is a **soluble, cytoplasmic** enzyme. Its substrates and products are intracellular CoA thioesters, and all downstream steps (isomerization to an oxepin, hydrolytic ring opening, and β-oxidation-like chemistry) are carried out by soluble cytoplasmic enzymes (Teufel et al. 2010, PMID 20660314). There is no evidence of membrane association or secretion; the complex has been purified and characterized biochemically and structurally as a soluble multiprotein assembly (Grishin et al. 2013, PMID 24055609). Therefore PaaB carries out its scaffolding function **inside the cell, in the cytoplasm**.

---

## 5. Pathway Context

The full aerobic PA / phenylacetyl-CoA catabolon operates as follows (Teufel et al. 2010, PMID 20660314; Grishin & Cygler 2015, PMID 26075354):

1. **Activation:** phenylacetate → phenylacetyl-CoA (PA-CoA ligase, PaaK/PaaF).
2. **Ring epoxidation (PaaB's step):** PA-CoA → ring-1,2-epoxyphenylacetyl-CoA by **PaaABCE** (di-iron monooxygenase; PaaB = structural subunit). The complex can also deoxygenate the epoxide back to PA-CoA to limit toxicity (Teufel et al. 2012, PMID 22398448).
3. **Isomerization:** epoxide → oxepin (a seven-membered O-heterocyclic enol ether) by a ring-1,2-epoxyphenylacetyl-CoA isomerase (PaaG).
4. **Hydrolytic ring opening** (PaaZ / oxepin-CoA hydrolase-aldehyde dehydrogenase).
5. **β-oxidation-like degradation** (PaaFGHIJ) → **acetyl-CoA + succinyl-CoA**, entering the TCA cycle.
6. **Detoxification support:** thioesterases **PaaI and PaaY** hydrolyze reactive intermediates to non-reactive products (Teufel et al. 2012, PMID 22398448).

This pathway is present in ~16% of sequenced bacterial genomes, including *E. coli* and *P. putida*, and is important both environmentally (styrene/aromatic pollutant remediation) and in the biology of certain pathogens where reactive early intermediates can contribute to virulence (Teufel et al. 2010, PMID 20660314). In *Pseudomonas*, the *paa* cluster also connects to biotechnologically relevant processes such as polyhydroxyalkanoate (aromatic bioplastic) metabolism (García et al. 1999, PMID 10506180).

---

## 6. Evidence Base

- **Experimental (structural):** Crystallography + EM + SAXS defined the PaaACB heterohexamer and PaaB's bridging homodimer role; mutagenesis of the PaaA "lysine bridge" quantified electron-transfer importance (Grishin et al. 2013, PMID 24055609). Precise, low-throughput structural/biochemical evidence.
- **Experimental (biochemical/mechanistic):** Purification and characterization of PaaABCE demonstrated bifunctional oxygenase/deoxygenase activity and the di-iron centre (Teufel et al. 2012, PMID 22398448).
- **Experimental (pathway elucidation):** Isotope-labeling and intermediate identification established the epoxide→oxepin route across *E. coli*/*P. putida* (Teufel et al. 2010, PMID 20660314).
- **Genetic:** *paa* gene-cluster characterization and complementation in *Pseudomonas* strains (Alonso et al. 2003, PMID 14597173; Ferrández et al. 1998, PMID 9748275; Mohamed et al. 2002, PMID 12189419).
- **Bioinformatic/evolutionary:** PaaB defines a distinct InterPro/Pfam family (PF06243) unrelated to small subunits of other monooxygenases, underscoring its unique structural role (Grishin et al. 2013, PMID 24055609).

---

## 7. Supported and Refuted Hypotheses

**Supported**
- PaaB is a subunit of the PaaABCE phenylacetyl-CoA ring-1,2-epoxidase (EC 1.14.13.149). ✔
- PaaB is a **structural/assembly (non-catalytic) subunit** forming a homodimer bridging two PaaAC catalytic dimers. ✔
- The complex functions in the **cytoplasm** on the **CoA-thioester** substrate. ✔
- The complex is bifunctional (epoxidase + deoxygenase) for epoxide detoxification. ✔

**Refuted / Not supported**
- PaaB is the catalytic (metal-binding) or substrate-binding subunit — **refuted**; catalysis resides in PaaA's di-iron site. ✘
- PaaB acts on free phenylacetate — **refuted**; the substrate is phenylacetyl-CoA. ✘

---

## 8. Limitations and Future Directions

- **Nomenclature:** Subunit letters differ between organisms and authors (e.g., "PaaABCDE" in *E. coli*/*Azoarcus* vs. "PaaACBE" in Grishin's structural work). This report maps the *P. putida* PP_3277 *paaB* gene (Q88HS6) to the structurally characterized bridging subunit; direct crystallographic work was performed largely on orthologous complexes, so the assignment relies on strong sequence/domain conservation across the family rather than a *P. putida*-specific structure.
- **Direct localization data** (e.g., fractionation) for *P. putida* PaaB specifically are inferred from the soluble nature of the purified complex; explicit *in vivo* localization studies would strengthen this.
- **Mechanistic role of PaaB in regulation vs. pure assembly** is not fully resolved — whether PaaB modulates the oxygenase/deoxygenase balance beyond simply enabling oligomerization is an open question worth targeted biochemical study.

---

## References
- Teufel R, Mascaraque V, Ismail W, Voss M, Perera J, Eisenreich W, Haehnel W, Fuchs G. *Bacterial phenylalanine and phenylacetate catabolic pathway revealed.* PNAS 2010. PMID 20660314.
- Teufel R, Friedrich T, Fuchs G. *An oxygenase that forms and deoxygenates toxic epoxide.* Nature 2012. PMID 22398448.
- Grishin AM, Ajamian E, Tao L, Bostina M, Zhang L, Trempe JF, Menard R, Rouiller I, Cygler M. *Family of phenylacetyl-CoA monooxygenases differs in subunit organization from other monooxygenases.* 2013. PMID 24055609.
- Grishin AM, Cygler M. *Structural Organization of Enzymes of the Phenylacetate Catabolic Hybrid Pathway.* 2015. PMID 26075354.
- Alonso S, et al. *Genetic characterization of the styrene lower catabolic pathway of Pseudomonas sp. strain Y2.* 2003. PMID 14597173.
- Ferrández A, et al. *Catabolism of phenylacetic acid in Escherichia coli.* 1998. PMID 9748275.
- Mohamed ME, Ismail W, Heider J, Fuchs G. *Aerobic metabolism of phenylacetic acids in Azoarcus evansii.* 2002. PMID 12189419.
- García B, et al. *Novel biodegradable aromatic plastics from a bacterial source.* 1999. PMID 10506180.


## Artifacts

- [OpenScientist final report](paaB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaB-deep-research-openscientist_artifacts/final_report.pdf)