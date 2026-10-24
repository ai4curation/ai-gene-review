---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:23:27.025234'
end_time: '2026-08-31T08:34:05.900502'
duration_seconds: 638.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pvdY
  gene_symbol: pvdY
  uniprot_accession: Q88F54
  protein_description: 'SubName: Full=Hydroxyproline acetylase {ECO:0000313|EMBL:AAN69825.2};
    EC=2.3.1.- {ECO:0000313|EMBL:AAN69825.2};'
  gene_info: Name=pvdY {ECO:0000313|EMBL:AAN69825.2}; OrderedLocusNames=PP_4245 {ECO:0000313|EMBL:AAN69825.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Acyl_CoA_acyltransferase. (IPR016181); Acyltransferase_MbtK/IucB-like.
    (IPR019432); Acetyltransf_8 (PF13523)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pvdY-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pvdY-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F54
- **Protein Description:** SubName: Full=Hydroxyproline acetylase {ECO:0000313|EMBL:AAN69825.2}; EC=2.3.1.- {ECO:0000313|EMBL:AAN69825.2};
- **Gene Information:** Name=pvdY {ECO:0000313|EMBL:AAN69825.2}; OrderedLocusNames=PP_4245 {ECO:0000313|EMBL:AAN69825.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Acyl_CoA_acyltransferase. (IPR016181); Acyltransferase_MbtK/IucB-like. (IPR019432); Acetyltransf_8 (PF13523)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pvdY" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pvdY' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pvdY** (gene ID: pvdY, UniProt: Q88F54) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pvdY* (PP_4245, UniProt Q88F54) in *Pseudomonas putida* KT2440

## Summary

The gene **pvdY** (ordered locus **PP_4245**, UniProt accession **Q88F54**) of *Pseudomonas putida* KT2440 encodes a **cytoplasmic, acetyl-CoA–dependent N-acyltransferase** of the MbtK/IucB-like acyltransferase superfamily (Pfam PF13523 *Acetyltransf_8*; InterPro IPR019432 and IPR016181; EC 2.3.1.–). Its primary biochemical function is to **acetylate N5-hydroxy-L-ornithine**, producing N5-acetyl-N5-hydroxy-L-ornithine, the **iron-chelating hydroxamate building block** of the fluorescent siderophore **pyoverdine**. This reaction places PvdY immediately downstream of the ornithine N5-oxygenase PvdA in the cytoplasmic **hydroxamate-precursor branch** of pyoverdine biosynthesis, and PvdY activity is required for pyoverdine production.

A central conclusion of this investigation concerns a **misannotation**. The UniProt "SubName" for Q88F54 reads *"Hydroxyproline acetylase"* (EC 2.3.1.–), a label derived automatically from an EMBL genome-annotation record (ECO:0000313|EMBL:AAN69825.2). This label is **not supported by any experimental evidence** and is inconsistent with both the gene name (*pvdY*) and the domain architecture of the protein. The biochemically demonstrated substrate for PvdY orthologs is **N5-hydroxy-L-ornithine**, not hydroxyproline. The corrected functional assignment is grounded in the direct characterization of the *P. aeruginosa* ortholog PvdY (Lamont et al. 2006, [PMID: 16585778](https://pubmed.ncbi.nlm.nih.gov/16585778/)), which used bioinformatic, genetic, and biochemical approaches to show that PvdY acetylates hydroxyornithine, is repressed by iron, and is essential for pyoverdine synthesis.

Structural evidence from *P. putida* KT2440 itself corroborates that this strain operates an active ornithine→N5-hydroxyornithine hydroxamate branch: mass-spectrometric elucidation of KT2440 pyoverdine reveals a heptapeptide backbone containing both an ornithine residue and a C-terminal cyclic N5-hydroxyornithine (a hydroxamate), confirming that the pathway in which PvdY acts is complete and functional in this organism. Taken together, the evidence supports assigning PvdY/PP_4245 as an **N5-hydroxyornithine acetyltransferase functioning in the cytoplasmic precursor-supply phase of pyoverdine biosynthesis**.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check required by this research task was completed:

| Attribute | Value | Assessment |
|---|---|---|
| UniProt accession | Q88F54 | Target confirmed |
| Gene name | *pvdY* (ECO:0000313\|EMBL:AAN69825.2) | Matches pyoverdine-biosynthesis nomenclature |
| Ordered locus | PP_4245 | *P. putida* KT2440 locus tag |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) | Confirmed |
| UniProt SubName | "Hydroxyproline acetylase," EC 2.3.1.– | **Automated misannotation — not experimentally supported** |
| Key domains | Acyl_CoA_acyltransferase (IPR016181); Acyltransferase MbtK/IucB-like (IPR019432); Acetyltransf_8 (PF13523) | Consistent with siderophore-precursor N-acyltransferases |

**Verdict:** The gene symbol *pvdY* is **not** ambiguous in the confusing sense. It is a *bona fide* pyoverdine-biosynthesis gene, and the domain architecture (MbtK/IucB-like acyl-CoA acyltransferase) is exactly the family that acylates hydroxylated amino-acid amines during siderophore assembly. The only ambiguity is the incorrect substrate label ("hydroxyproline") inherited from an automated EMBL record; the correct substrate is N5-hydroxy-L-ornithine. Direct literature exists for the *P. aeruginosa* ortholog, and structural literature exists for KT2440 pyoverdine, so research proceeded on the correct target.

---

## Key Findings

### Finding 1 — PvdY is an N5-hydroxyornithine acetyltransferase, not a "hydroxyproline acetylase"

The most direct evidence for PvdY function comes from characterization of the *Pseudomonas aeruginosa* ortholog. Lamont and colleagues (2006, [PMID: 16585778](https://pubmed.ncbi.nlm.nih.gov/16585778/)) applied **bioinformatic, genetic, and biochemical approaches** and reported that *"the PvdYII enzyme catalyzes acetylation of hydroxyornithine."* This is a direct assignment of the enzymatic activity: PvdY transfers an acetyl group onto the N5-hydroxylamine of hydroxyornithine, generating the hydroxamate N5-acetyl-N5-hydroxy-L-ornithine.

The same study established the **genetic requirement** of *pvdY* for siderophore production: *"A mutation in pvdY(II) prevented pyoverdine synthesis."* This links the acetyltransferase activity causally to the biosynthetic output. Furthermore, the gene displayed the **iron-responsive regulation** that is a hallmark of siderophore-biosynthesis genes: *"Expression of pvdY(II) is repressed by the presence of iron and upregulated by the presence of type II pyoverdine."* Iron repression is mediated in *Pseudomonas* by the ferric uptake regulator (Fur), and its presence is a strong signature of a gene dedicated to iron acquisition.

The *P. putida* KT2440 gene PP_4245 carries the gene name *pvdY* and belongs to the **MbtK/IucB-like acyltransferase family** (Pfam PF13523 *Acetyltransf_8*; InterPro IPR019432 and IPR016181; EC 2.3.1.–). This is the same acyl-CoA–dependent N-acyltransferase family responsible for acylating hydroxylated amino-acid amines in other siderophore systems — most notably **IucB**, which N-acetylates N6-hydroxylysine during aerobactin assembly. The convergence of (i) the *pvdY* gene name, (ii) the MbtK/IucB-like domain architecture, and (iii) the characterized activity of the ortholog provides a coherent, mutually reinforcing case that PP_4245 is an N5-hydroxyornithine acetyltransferase. The UniProt "hydroxyproline acetylase" SubName is an automated EMBL-derived misannotation; the biochemically supported substrate is **N5-hydroxy-L-ornithine**.

### Finding 2 — PvdY acts downstream of the ornithine N5-oxygenase PvdA in the hydroxamate branch

Pyoverdine's iron-chelating hydroxamate groups are built in two enzymatic steps from L-ornithine. The **first committed step** is catalyzed by **PvdA**, an FAD/NADPH-dependent L-ornithine N5-oxygenase that hydroxylates the side-chain amine of ornithine to yield **N5-hydroxy-L-ornithine**. Olucha et al. (2011, [PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)) describe PvdA as an enzyme that *"catalyzes the FAD-dependent hydroxylation of the side chain amine of ornithine, which is subsequently formylated to generate the iron-chelating hydroxamates of the siderophore pyoverdin."* Ge & Seah (2006, [PMID: 17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/)) similarly state that *"formation of the iron-chelating hydroxamate functional group in pyoverdine requires the enzyme PvdA, a flavin-dependent monooxygenase that catalyzes the N(5) hydroxylation of l-ornithine."*

Once N5-hydroxy-L-ornithine is generated, the hydroxylamine must be **acylated** to complete the hydroxamate. Two alternative acyl groups are used across the pyoverdine structural types: **formylation by PvdF** (characteristic of type I pyoverdine) or **acetylation by PvdY** (type II). PvdY thus occupies the **acylation node** immediately downstream of PvdA, providing the acetyl-transfer alternative to PvdF's formyl transfer. The biochemical characterization of PvdA as a soluble monomer most active at pH 8.0 (Meneely & Lamb 2007, [PMID: 17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/)) and the demonstration that PvdA orthologs are expressed under iron limitation across fluorescent pseudomonads including *P. putida* (Putignani et al. 2004, [PMID: 14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/)) place the entire ornithine-hydroxamate module firmly within the iron-starvation response.

The logical ordering — PvdA hydroxylates, then PvdY acetylates — defines a two-enzyme sub-pathway that converts a proteinogenic-like amino acid (ornithine) into a metal-binding hydroxamate that is subsequently incorporated by nonribosomal peptide synthetases (NRPS) into the pyoverdine peptide backbone.

### Finding 3 — PvdY functions in the cytoplasm during the precursor-supply/assembly phase

Pyoverdine biosynthesis is **spatially compartmentalized** between cytoplasm and periplasm. Schalk & Guillon (2013, [PMID: 23126435](https://pubmed.ncbi.nlm.nih.gov/23126435/)) describe it as *"a complex process involving at least 12 different proteins, starting in the cytoplasm and ending in the periplasm,"* and note that *"in the cytoplasm, pyoverdine appears to be assembled at the inner membrane and particularly at the old cell pole."* The early biosynthetic steps — including generation and acylation of the hydroxamate precursors — occur in the **cytoplasm**.

The non-fluorescent precursor **ferribactin** is synthesized in the cytoplasm and then exported for maturation. Sugue et al. (2022, [PMID: 35764171](https://pubmed.ncbi.nlm.nih.gov/35764171/)) state that *"after its synthesis in the cytoplasm, the nonfluorescent pyoverdine precursor ferribactin is exported into the periplasm, where the enzymes PvdQ, PvdP, PvdO, PvdN, and PtaA are responsible for fluorophore maturation."* Because PvdA is a soluble cytoplasmic monomer ([PMID: 17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/)) and PvdY acetylates the N5-hydroxyornithine that is then incorporated by cytoplasmic NRPS modules into ferribactin, **PvdY performs its acetyl-transfer reaction in the cytoplasm, upstream of the periplasmic maturation machinery**. Its subcellular location is therefore the cytoplasm (or cytoplasmic face of the inner membrane where the NRPS assembly line is organized), not the periplasm or extracellular space where the mature siderophore ultimately functions.

### Finding 4 — KT2440 pyoverdine contains hydroxyornithine-derived hydroxamate residues, confirming an active PvdA/PvdY branch

The strongest organism-specific evidence that the PvdY branch is active in KT2440 is the **structure of KT2440 pyoverdine itself**. MS/MS structural elucidation (Wei & Aristilde 2015, [PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/)) shows that *"the three PVDs of P. putida possess the same peptide chain of seven amino acids, Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn, with a cyclicized portion present in two of the PVDs."* The presence of an **ornithine (Orn)** residue and a **C-terminal cyclic N5-hydroxyornithine (cOHOrn, a hydroxamate)** in the backbone demonstrates directly that KT2440 operates the ornithine→N5-hydroxyornithine hydroxamate branch — the branch in which PvdA and its downstream acyltransferase (PvdY) act.

Baune et al. (2017, [PMID: 28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/)) independently confirmed the previously characterized KT2440 pyoverdines "G4R and G4R A," which differ only in their acyl side chains. Matthijs et al. (2009, [PMID: 19459056](https://pubmed.ncbi.nlm.nih.gov/19459056/)) reported that *"structural analysis of the pyoverdine produced by the closely related P. putida KT2440 showed that this strain produces an already characterised pyoverdine,"* and that KT2440 produces a single, strain-specific pyoverdine and can utilize its own pyoverdine plus that of *P. syringae* LMG 1247. Collectively, these structural studies establish that KT2440 makes a defined, functional pyoverdine containing hydroxamate residues, consistent with a complete biosynthetic pathway that includes PvdY.

---

## Mechanistic Model and Interpretation

### The two-step hydroxamate-precursor module

The core of the mechanistic model is a **two-enzyme conversion of L-ornithine into a hydroxamate building block**, followed by NRPS incorporation and periplasmic maturation:

```
                         CYTOPLASM
  L-ornithine
      |
      |   PvdA  (L-ornithine N5-oxygenase; FAD/NADPH)
      |         "N5 hydroxylation of L-ornithine"
      v
  N5-hydroxy-L-ornithine
      |
      |   ACYLATION NODE  ── branch point ──┐
      |                                     │
      |   PvdY (acetyl-CoA)          PvdF (formyl donor)
      |   "acetylation of                "formylation"
      |    hydroxyornithine"                │
      v                                     v
  N5-acetyl-N5-hydroxy-Orn         N5-formyl-N5-hydroxy-Orn
  (type II hydroxamate)            (type I hydroxamate)
      |
      |   NRPS assembly line (incorporates hydroxamate + other residues)
      v
  Ferribactin (non-fluorescent precursor)   [assembled at inner membrane / old cell pole]
      |
      |   EXPORT to periplasm
      v
                         PERIPLASM
  Ferribactin --PvdQ/PvdP/PvdM/PvdO/PvdN/PtaA--> mature fluorescent PYOVERDINE
      |
      |   SECRETION
      v
                         EXTRACELLULAR
  Pyoverdine chelates Fe(III); ferri-pyoverdine re-imported via FpvA receptor
```

**PvdY sits at the acylation node inside the cytoplasm.** It is the acetyl-transfer alternative to the formyl-transfer enzyme PvdF. The acetyl group it installs, together with the N5-hydroxyl installed by PvdA, forms the **hydroxamate** (–N(OH)–C(=O)–CH3) functional group that is one of the two principal iron(III)-coordinating moieties of pyoverdine (the other being the catecholate-like groups of the chromophore and the β-hydroxyaspartate residues).

### Why the "hydroxyproline acetylase" label is wrong

The UniProt SubName "hydroxyproline acetylase" is an automated annotation (evidence code ECO:0000313, meaning imported from a sequence database record without curator review). Three independent lines of reasoning contradict it and support "N5-hydroxyornithine acetyltransferase":

1. **Gene name.** The locus is named *pvdY* — the "pvd" prefix is the standard nomenclature for **p**yo**v**er**d**ine biosynthesis genes. There is no plausible role for a hydroxyproline acetylase in this pathway.
2. **Domain architecture.** The MbtK/IucB-like acyl-CoA acyltransferase fold (PF13523) is dedicated in characterized systems to acylating **N-hydroxylated amino-acid side chains** (N6-hydroxylysine in aerobactin by IucB; N5-hydroxyornithine in pyoverdine). It is not a proline-modifying fold.
3. **Ortholog biochemistry.** The *P. aeruginosa* PvdY ortholog was directly shown to acetylate **hydroxyornithine** and to be essential for pyoverdine synthesis ([PMID: 16585778](https://pubmed.ncbi.nlm.nih.gov/16585778/)).

The likely origin of the erroneous label is a spurious substrate assignment during automated genome annotation of AAN69825, propagated into UniProt as a SubName. The corrected reaction is:

> **N5-hydroxy-L-ornithine + acetyl-CoA → N5-acetyl-N5-hydroxy-L-ornithine + CoA** (EC 2.3.1.–, acetyltransferase)

### Localization summary

| Phase | Compartment | Enzymes | PvdY role |
|---|---|---|---|
| Precursor supply | Cytoplasm | PvdA, **PvdY**/PvdF | **Acetylates N5-OH-ornithine** |
| Peptide assembly | Cytoplasm / inner membrane, old cell pole | NRPS (PvdL, PvdI, PvdJ, PvdD, etc.) | Provides hydroxamate substrate |
| Precursor export | Inner membrane → periplasm | Transporter (e.g., PvdE) | — |
| Fluorophore maturation | Periplasm | PvdQ, PvdP, PvdM, PvdO, PvdN, PtaA | — |
| Iron capture | Extracellular | Secreted pyoverdine | — |
| Re-import | Outer membrane | FpvA receptor | — |

PvdY's site of action is therefore **cytoplasmic**, even though the ultimate product functions extracellularly.

---

## Evidence Base

| PMID | Study (short title) | Relevance to PvdY function |
|---|---|---|
| [16585778](https://pubmed.ncbi.nlm.nih.gov/16585778/) | *Characterization of a gene encoding an acetylase required for pyoverdine synthesis in P. aeruginosa* (Lamont et al. 2006) | **Primary evidence.** Direct assignment: PvdY acetylates hydroxyornithine; *pvdY* mutation prevents pyoverdine synthesis; iron-repressed, pyoverdine-inducible expression. |
| [21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/) | *Two structures of an N-hydroxylating flavoprotein monooxygenase (PvdA)* (Olucha et al. 2011) | Defines the upstream PvdA step producing N5-hydroxyornithine, which is subsequently acylated to form hydroxamates — the node where PvdY acts. |
| [17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/) | *Heterologous expression of L-ornithine N5-hydroxylase (PvdA)* (Ge & Seah 2006) | Establishes PvdA as generator of the N5-hydroxyornithine substrate that PvdY acetylates. |
| [17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/) | *Biochemical characterization of ornithine hydroxylase (PvdA)* (Meneely & Lamb 2007) | Shows PvdA is a soluble cytoplasmic monomer, anchoring the hydroxamate module in the cytoplasm. |
| [14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/) | *Expression of PvdA in fluorescent Pseudomonas species* (Putignani et al. 2004) | Demonstrates PvdA-type oxygenases are iron-regulated and conserved across *P. putida* and relatives. |
| [23126435](https://pubmed.ncbi.nlm.nih.gov/23126435/) | *Pyoverdine biosynthesis and secretion in P. aeruginosa* (Schalk & Guillon 2013) | Establishes cytoplasm-to-periplasm compartmentalization; early precursor steps (incl. PvdY) are cytoplasmic. |
| [35764171](https://pubmed.ncbi.nlm.nih.gov/35764171/) | *PvdM required for oxidation of ferribactin by PvdP* (Sugue et al. 2022) | Confirms ferribactin is cytoplasmically synthesized, then exported for periplasmic maturation — locating PvdY upstream in the cytoplasm. |
| [25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/) | *Structural characterization of P. putida KT2440 pyoverdines* (Wei & Aristilde 2015) | KT2440 pyoverdine backbone Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn contains hydroxyornithine hydroxamate — the PvdY branch is active. |
| [28631237](https://pubmed.ncbi.nlm.nih.gov/28631237/) | *Pyoverdines of KT2440 and P. taiwanensis* (Baune et al. 2017) | Confirms known KT2440 pyoverdines G4R/G4R A differing only in acyl side chains. |
| [19459056](https://pubmed.ncbi.nlm.nih.gov/19459056/) | *Siderophore-mediated iron acquisition in P. entomophila and KT2440* (Matthijs et al. 2009) | Confirms KT2440 produces a defined, functional pyoverdine — consistent with a complete pathway including PvdY. |
| [15743962](https://pubmed.ncbi.nlm.nih.gov/15743962/) | *Diversifying selection at the pyoverdine locus* (Smith et al. 2005) | Notes *pvdY* is genetically linked (linkage disequilibrium) to the pyoverdine structural locus though physically separated — evolutionary evidence *pvdY* belongs to the pyoverdine system. |
| [23766117](https://pubmed.ncbi.nlm.nih.gov/23766117/) | *The acylase PvdQ conserved among fluorescent Pseudomonas* (Bokhove et al. 2013) | Shows pyoverdine maturation machinery (incl. PvdQ) conserved in KT2440 — supports pathway conservation. |

### How the evidence converges

No paper reports the *in vitro* enzymology of the *P. putida* KT2440 protein PP_4245 specifically. The functional assignment therefore rests on a **strong chain of orthology and pathway logic**:

- The **ortholog** (*P. aeruginosa* PvdY) is directly characterized as a hydroxyornithine acetylase essential for pyoverdine ([PMID: 16585778](https://pubmed.ncbi.nlm.nih.gov/16585778/)).
- The **upstream substrate-supply enzyme** (PvdA) is well characterized in multiple studies, and its product (N5-hydroxyornithine) is exactly the substrate PvdY requires.
- The **KT2440 pyoverdine product** contains hydroxyornithine hydroxamate residues ([PMID: 25895945](https://pubmed.ncbi.nlm.nih.gov/25895945/)), proving the branch is active *in vivo*.
- The **domain architecture** (MbtK/IucB-like) matches the enzyme class that performs exactly this acylation chemistry.
- **Evolutionary genetics** independently ties *pvdY* to the pyoverdine locus ([PMID: 15743962](https://pubmed.ncbi.nlm.nih.gov/15743962/)).

---

## Limitations and Knowledge Gaps

1. **No direct enzymology of PP_4245.** The functional assignment is by orthology to *P. aeruginosa* PvdY and by pathway/product logic. The KT2440 protein itself has not, to our knowledge, been purified and assayed for hydroxyornithine acetyltransferase activity. Kinetic parameters (Km for N5-hydroxyornithine and acetyl-CoA, kcat, substrate specificity vs. hydroxylysine) are unknown for the KT2440 enzyme.

2. **Acyl-donor identity assumed.** Acetyl-CoA is the presumed acetyl donor based on family membership (acyl-CoA acyltransferase, IPR016181) and the "acetylation" chemistry reported for the ortholog. Direct demonstration of the cofactor for PP_4245 is lacking.

3. **Type II vs. KT2440 side-chain nuance.** The direct PvdY characterization was on the "type II" pyoverdine system of *P. aeruginosa*. KT2440's pyoverdine differs in peptide sequence and acyl side chains; whether PP_4245 acetylates the same N5-hydroxyornithine node with identical specificity is inferred, not directly shown. The KT2440 backbone contains a *cyclic* N5-hydroxyornithine (cOHOrn) at the C-terminus and a non-cyclized Orn internally; the precise residue(s) acetylated in KT2440 would benefit from confirmation.

4. **Genetic knockout in KT2440 not reported here.** A clean *pvdY*/PP_4245 deletion in KT2440 with a pyoverdine-negative phenotype and precursor-feeding rescue (as done historically for *pvdA*) would provide organism-specific causal proof. Such a mutant was not identified in the reviewed literature.

5. **Subcellular localization is inferred.** PvdY's cytoplasmic location is deduced from the compartmentalization of pyoverdine biosynthesis and from PvdA's demonstrated cytoplasmic solubility, not from direct localization of the PvdY protein (e.g., fluorescent fusion, fractionation).

6. **Residual annotation error in databases.** The "hydroxyproline acetylase" label remains in UniProt and could continue to propagate; downstream users should treat it as erroneous.

---

## Proposed Follow-up Experiments / Actions

1. **In vitro enzyme assay of purified PP_4245.** Heterologously express and purify Q88F54; assay acetyl-CoA–dependent acetylation of chemically synthesized N5-hydroxy-L-ornithine (monitor CoA release or product by LC-MS). Determine Km, kcat, and test alternative substrates (N6-hydroxylysine, hydroxyproline as a negative control) to formally exclude the "hydroxyproline" annotation and quantify specificity.

2. **Acyl-donor specificity.** Test acetyl-CoA vs. other short-chain acyl-CoAs and vs. a formyl donor to confirm PvdY installs an acetyl (not formyl) group in KT2440, distinguishing it functionally from PvdF.

3. **Targeted KT2440 knockout and complementation.** Construct an in-frame ΔPP_4245 mutant; assess pyoverdine production by CAS assay / fluorescence and LC-MS. Confirm loss of the hydroxamate-containing pyoverdine and rescue by feeding N5-acetyl-N5-hydroxyornithine or by genetic complementation, mirroring classic *pvdA* precursor-feeding experiments.

4. **Product structural confirmation.** In a Δ*pvdY* background, use LC-MS/MS to determine whether the pyoverdine hydroxamate residues lose their acetyl modification or the siderophore fails to assemble, pinpointing which residue(s) PvdY acetylates.

5. **Subcellular localization.** Build a functional PvdY–fluorescent-protein fusion and/or perform cell fractionation to directly confirm cytoplasmic (or inner-membrane–associated, old-cell-pole) localization.

6. **Structural biology.** Solve or model the PP_4245 structure (AlphaFold + experimental) to confirm the MbtK/IucB-like fold, identify the acetyl-CoA and hydroxyornithine binding pockets, and rationalize substrate specificity. This would also provide residue-level evidence against a proline-binding site.

7. **Database curation.** Submit a correction to UniProt recommending re-annotation of Q88F54 from "Hydroxyproline acetylase" to "N5-hydroxy-L-ornithine acetyltransferase (pyoverdine biosynthesis), EC 2.3.1.–."

---

## Conclusion

The weight of evidence — direct biochemical/genetic characterization of the *P. aeruginosa* ortholog, the conserved MbtK/IucB-like acyltransferase domain architecture, the demonstrated presence of hydroxyornithine-derived hydroxamate residues in KT2440 pyoverdine, and the established cytoplasm-to-periplasm compartmentalization of pyoverdine biosynthesis — supports assigning **pvdY / PP_4245 / Q88F54 as a cytoplasmic, acetyl-CoA–dependent N5-hydroxy-L-ornithine acetyltransferase** that supplies the iron-chelating hydroxamate building block of pyoverdine. It functions immediately downstream of the ornithine N5-oxygenase PvdA in the cytoplasmic precursor-supply branch of pyoverdine biosynthesis and is required for siderophore production. The UniProt "hydroxyproline acetylase" designation is an automated misannotation and should be corrected. Direct enzymology and a targeted knockout in KT2440 remain the key outstanding experiments to convert this well-supported inference into organism-specific proof.


## Artifacts

- [OpenScientist final report](pvdY-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pvdY-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16585778
2. PMID:21757711
3. PMID:17015659
4. PMID:17900176
5. PMID:14684153
6. PMID:23126435
7. PMID:35764171
8. PMID:25895945
9. PMID:28631237
10. PMID:19459056
11. PMID:15743962