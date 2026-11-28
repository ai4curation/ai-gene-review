---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.165230'
end_time: '2026-09-01T00:05:38.006116'
duration_seconds: 4045.84
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ftsW
  gene_symbol: ftsW
  uniprot_accession: Q88N77
  protein_description: 'RecName: Full=Probable peptidoglycan glycosyltransferase FtsW
    {ECO:0000256|HAMAP-Rule:MF_00913}; Short=PGT {ECO:0000256|HAMAP-Rule:MF_00913};
    EC=2.4.99.28 {ECO:0000256|HAMAP-Rule:MF_00913}; AltName: Full=Cell division protein
    FtsW {ECO:0000256|HAMAP-Rule:MF_00913}; AltName: Full=Cell wall polymerase {ECO:0000256|HAMAP-Rule:MF_00913};
    AltName: Full=Peptidoglycan polymerase {ECO:0000256|HAMAP-Rule:MF_00913}; Short=PG
    polymerase {ECO:0000256|HAMAP-Rule:MF_00913};'
  gene_info: Name=ftsW {ECO:0000256|HAMAP-Rule:MF_00913, ECO:0000313|EMBL:AAN66959.1};
    OrderedLocusNames=PP_1336 {ECO:0000313|EMBL:AAN66959.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the SEDS family. FtsW subfamily.
  protein_domains: Cell_cycle_FtsW-rel_CS. (IPR018365); FtsW. (IPR013437); FtsW/RodA.
    (IPR001182); FTSW_RODA_SPOVE (PF01098)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ftsW-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ftsW-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N77
- **Protein Description:** RecName: Full=Probable peptidoglycan glycosyltransferase FtsW {ECO:0000256|HAMAP-Rule:MF_00913}; Short=PGT {ECO:0000256|HAMAP-Rule:MF_00913}; EC=2.4.99.28 {ECO:0000256|HAMAP-Rule:MF_00913}; AltName: Full=Cell division protein FtsW {ECO:0000256|HAMAP-Rule:MF_00913}; AltName: Full=Cell wall polymerase {ECO:0000256|HAMAP-Rule:MF_00913}; AltName: Full=Peptidoglycan polymerase {ECO:0000256|HAMAP-Rule:MF_00913}; Short=PG polymerase {ECO:0000256|HAMAP-Rule:MF_00913};
- **Gene Information:** Name=ftsW {ECO:0000256|HAMAP-Rule:MF_00913, ECO:0000313|EMBL:AAN66959.1}; OrderedLocusNames=PP_1336 {ECO:0000313|EMBL:AAN66959.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the SEDS family. FtsW subfamily.
- **Key Domains:** Cell_cycle_FtsW-rel_CS. (IPR018365); FtsW. (IPR013437); FtsW/RodA. (IPR001182); FTSW_RODA_SPOVE (PF01098)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ftsW" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ftsW' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ftsW** (gene ID: ftsW, UniProt: Q88N77) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FtsW (Q88N77) — Probable Peptidoglycan Glycosyltransferase FtsW

**Gene:** *ftsW* (Ordered locus PP_1336)
**UniProt:** Q88N77
**Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / NCIMB 11950)
**EC:** 2.4.99.28 | **Family:** SEDS family, FtsW subfamily (Pfam PF01098 FTSW_RODA_SPOVE; InterPro IPR013437 FtsW, IPR001182 FtsW/RodA, IPR018365 Cell_cycle_FtsW-rel conserved site)

---

## 1. Identity verification

The gene symbol *ftsW*, the UniProt description ("Probable peptidoglycan glycosyltransferase FtsW / Cell division protein FtsW / Cell wall polymerase"), the EC number 2.4.99.28, and the assigned family/domains (SEDS family, FtsW subfamily; FtsW/RodA transmembrane fold PF01098) are fully **self-consistent**. This is the canonical, unambiguous cell-division protein FtsW. The name is conserved across essentially all bacteria and refers to the same protein. The *P. putida* KT2440 ortholog PP_1336 is annotated by the HAMAP rule MF_00913, i.e. by orthology to biochemically characterized homologues in *Escherichia coli*, *Bacillus subtilis*, *Staphylococcus aureus* and *Thermus thermophilus*. No conflicting gene with the same symbol was encountered. Direct wet-lab characterization of the *P. putida* protein itself is limited; the functional narrative below is therefore built on the well-established biology of FtsW/SEDS proteins and inferred for PP_1336 by strong sequence/domain orthology.

---

## 2. Primary molecular function — what reaction is catalyzed

FtsW is a **peptidoglycan glycosyltransferase (PGT), i.e. a peptidoglycan polymerase**. It catalyzes the polymerization of the lipid-linked precursor **Lipid II** (undecaprenyl-pyrophosphoryl-MurNAc(-pentapeptide)-GlcNAc) into linear **glycan strands** — the glycan backbone of the peptidoglycan (murein) sacculus (EC 2.4.99.28).

Until ~2016, Lipid II polymerization was thought to be the exclusive province of the class A penicillin-binding proteins (aPBPs). Two landmark studies redefined this:

- Meeske et al. (2016) showed genetically and biochemically that SEDS proteins (the family containing RodA and FtsW) "**constitute a family of peptidoglycan polymerases**," representing a second, distinct class of PG polymerase used by most bacteria (PMID 27525505).
- Taguchi et al. (2019) demonstrated that **FtsW itself is a peptidoglycan polymerase** in vitro (PMID 30692671).

**Substrate specificity and mechanism.** The substrate is **Lipid II**. Welsh et al. (2019) showed that SEDS polymerases synthesize peptidoglycan by "**adding new Lipid II monomers to the reducing end of the growing glycan chain**," and that the glycosyl-donor and glycosyl-acceptor positions have distinct lipid requirements (PMID 31386359). The conserved transmembrane cavity that binds Lipid II is catalytically essential; a small-molecule FtsW inhibitor was shown to **compete with Lipid II for binding to FtsW** (Park et al. 2023, PMID 37099323), reinforcing Lipid II as the direct substrate.

**Historical note (correcting an outdated annotation).** FtsW was for many years proposed to be the **Lipid II "flippase"** that translocates the precursor across the inner membrane. That transport role has since been reassigned to **MurJ**, and FtsW's true, primary role is now firmly established as the **glycan-strand polymerase** of the septum (Kumar et al. 2022 review, PMID 35274942). Databases that still list FtsW as a flippase are outdated.

---

## 3. The functional partnership — FtsW works with FtsI (PBP3)

FtsW does not act alone. It functions as the polymerase half of a bifunctional **septal peptidoglycan synthase**, paired with its cognate **class B penicillin-binding protein FtsI (PBP3)**, a monofunctional transpeptidase:

- **FtsW** polymerizes Lipid II → glycan strands.
- **FtsI/PBP3** cross-links adjacent strands via peptide bridges (transpeptidation).

Crucially, Taguchi et al. (2019) titled their work "**FtsW is a peptidoglycan polymerase that is functional only in complex with its cognate penicillin-binding protein**" (PMID 30692671) — the FtsW–FtsI (FtsWI) complex is an obligate functional unit. This division-dedicated FtsWI pair is the structural/functional analogue of the cell-**elongation** pair RodA–PBP2 (elongasome); FtsW/FtsI build the **septum/division site**, RodA/PBP2 elongate the **lateral wall** (Straume et al. 2021 review, PMID 33709487).

---

## 4. Subcellular localization — where FtsW acts

- **Membrane.** FtsW is a **polytopic integral protein of the cytoplasmic (inner) membrane**. The SEDS fold, resolved from the *T. thermophilus* RodA crystal structure (Sjodt et al. 2018, PMID 29590088), is a "**ten-pass transmembrane fold with large extracellular loops**" and "**a highly conserved cavity in the transmembrane domain**" that is catalytically essential. FtsW shares this architecture (Pfam PF01098).
- **Site of catalysis.** Because Lipid II is embedded in the membrane and the glycan product emerges on the periplasmic side, catalysis occurs at the **outer (periplasmic) leaflet of the inner membrane**. Li et al. (2022) mapped the FtsW **active site to conserved extracellular-loop residues clustered around a central cavity**; dominant-negative mutations there "**blocked septal PG synthesis but did not affect FtsW localization to the division site, interaction with its partners nor its substrate lipid II**" (PMID 34986161).
- **Cellular position.** FtsW localizes to **midcell / the division septum**, recruited as part of the divisome downstream of the FtsZ ring (den Blaauwen & Luirink 2019, PMID 30808703).

---

## 4b. Direct database and orthology verification (this study)

To ensure the annotation is grounded in the actual target record rather than family generalization, the UniProt entry for **Q88N77** was retrieved and analyzed programmatically:

- **Sequence/topology:** 404 aa, 44.2 kDa, with **exactly 10 annotated transmembrane helices** — matching the canonical SEDS 10-TM fold (Sjodt et al. 2018).
- **Curated function:** the record's own FUNCTION line reads "**Peptidoglycan polymerase that is essential for cell division**"; SUBCELLULAR LOCATION = "**Cell inner membrane**"; SIMILARITY = "**SEDS family, FtsW subfamily**"; keywords include *Cell division, Cell shape, Peptidoglycan synthesis, Glycosyltransferase*.
- **Orthology to characterized FtsW:** a global (Needleman–Wunsch) alignment of *P. putida* FtsW (Q88N77, 404 aa) against experimentally characterized ***E. coli* FtsW (P0ABG4, 414 aa)** gives **~50% identity over the full length** (202/404; 54.6% over aligned columns) even with conservative unit scoring — far above the ~30% orthology threshold. This quantitatively justifies transferring the *E. coli*/*S. aureus* FtsW biochemistry to PP_1336.
- **Catalytic-residue conservation:** aligning the two proteins maps the invariant, catalytically implicated SEDS aspartate (*E. coli* FtsW **D297**) onto *P. putida* **D276**, and the conserved aromatic *E. coli* Y159 onto *P. putida* Y138. Conservation of the invariant active-site aspartate is residue-level evidence that PP_1336 has a functional glycosyltransferase active site (not a degenerate pseudo-enzyme).

## 5. Pathway and biological process — cell division / septal PG synthesis

FtsW is a core, essential component of the **divisome**, the multiprotein machine that carries out bacterial cytokinesis. Its place in the pathway:

1. The tubulin-like **FtsZ** polymerizes into the Z-ring at midcell (with FtsA/ZipA), defining the division plane.
2. Late divisome proteins are recruited, forming the **FtsBLQ–PBP1b–FtsW–FtsI(PBP3)** complex (den Blaauwen & Luirink 2019, PMID 30808703).
3. **FtsW+FtsI synthesize septal peptidoglycan**, building the new cell wall that will form the two daughter-cell poles.

**Regulation (spatiotemporal control).** FtsW activity is tightly gated so that wall synthesis is coupled to division:
- Park, Du & Lutkenhaus (2020) showed "**spatiotemporal regulation of septal PG synthesis is achieved by coupling assembly and activation of the synthetic enzymes (FtsWI) to the Z ring**," with **FtsL essential for activating** FtsWI (PMID 33293384).
- The **FtsQLB (FtsBLQ)** subcomplex holds the synthase in an OFF state; accumulation of **FtsN** relieves this inhibition and triggers the onset of constriction (den Blaauwen & Luirink 2019, PMID 30808703). Thus FtsN is an activator and FtsQLB a brake on FtsW/FtsI activity.

This regulatory logic (FtsZ recruitment → FtsQLB restraint → FtsN activation) is broadly conserved among Gram-negative bacteria and is expected to operate in *P. putida*.

**Dynamic spatial guidance by FtsZ treadmilling.** Beyond static recruitment, FtsW's activity is steered around the division circumference by the treadmilling dynamics of the FtsZ ring. Yang et al. (2017) showed that "**GTPase activity-coupled treadmilling of the bacterial tubulin FtsZ organizes septal cell wall synthesis**" (PMID 28209899), and McCausland et al. (2021) demonstrated that "**treadmilling FtsZ polymers drive the directional movement of sPG-synthesis enzymes via a Brownian ratchet mechanism**," controlling the spatiotemporal distribution of active FtsW/FtsI (PMID 33504807). Thus FtsZ treadmilling determines where and how fast FtsW deposits new glycan strands.

---

## 6. Evidence summary and confidence

| Claim | Type of evidence | Strength for PP_1336 |
|---|---|---|
| PGT/polymerase catalytic activity on Lipid II | In vitro biochemistry in homologues (PMID 27525505, 30692671, 31386359) | High (orthology inference) |
| Obligate FtsW–FtsI(PBP3) complex | Biochemistry/genetics (PMID 30692671, 33709487) | High |
| 10-TM inner-membrane fold, TM catalytic cavity | Crystal structure of RodA + FtsW mutagenesis (PMID 29590088, 34986161) | High (family-level) |
| Midcell/septal localization within divisome | Cell biology/genetics (PMID 30808703, 34986161) | High |
| FtsQLB/FtsN/FtsL regulation | Genetics/biochemistry (PMID 33293384, 30808703) | High (Gram-negative) |
| Not the Lipid II flippase (MurJ is) | Review synthesis (PMID 35274942) | High |
| FtsZ-treadmilling directs FtsW movement | Single-molecule imaging (PMID 28209899, 33504807) | High (conserved) |
| Target record: 404 aa, 10 TM, inner membrane, essential PG polymerase | UniProt Q88N77 curated record (this study) | Direct |
| ~50% identity + conserved catalytic Asp (D276) vs E. coli FtsW | Sequence alignment (this study) | Direct (orthology) |

---

## 7. Limitations and future directions

- **No direct experimental data on the *P. putida* KT2440 protein** were found; all functional assignments are by strong orthology (HAMAP MF_00913) to characterized enzymes in *E. coli*, *B. subtilis*, *S. aureus* and *T. thermophilus*. This is standard and well-justified given the deep conservation of FtsW, but species-specific features (e.g. exact partner PBP repertoire, regulation) remain to be confirmed in *Pseudomonas*.
- A *P. putida*-specific validation would ideally include: (i) confirming essentiality and midcell localization (fluorescent fusion); (ii) identifying the cognate FtsI/PBP3 ortholog and demonstrating the FtsWI complex; (iii) in vitro polymerase assays with *P. putida* Lipid II.
- FtsW is an **attractive, essentially universal antibiotic target** (essential, membrane-accessible, druggable Lipid II-binding cavity; PMID 37099323), of interest for *Pseudomonas*.

---

## 8. Conclusion

**FtsW (Q88N77, PP_1336)** is the essential **SEDS-family peptidoglycan glycosyltransferase (polymerase)** of the *Pseudomonas putida* divisome. Located in the cytoplasmic membrane at the division septum, it polymerizes the membrane-anchored precursor **Lipid II** into glycan strands (adding monomers to the reducing end), functioning obligately in complex with the transpeptidase **FtsI/PBP3** to build septal peptidoglycan during cytokinesis. Its activity is spatiotemporally controlled by the divisome via FtsZ-ring recruitment, FtsQLB inhibition and FtsN/FtsL activation. It is **not** a Lipid II flippase (that role belongs to MurJ), correcting an earlier annotation.


## Artifacts

- [OpenScientist final report](ftsW-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ftsW-deep-research-openscientist_artifacts/final_report.pdf)