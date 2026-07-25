---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:45.261070'
end_time: '2026-07-18T19:11:44.398979'
duration_seconds: 4679.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: visC
  gene_symbol: visC
  uniprot_accession: Q88CI4
  protein_description: 'SubName: Full=Oxidoreductase involved in anerobic synthesis
    of ubiquinone, FAD/NAD(P)-binding domain {ECO:0000313|EMBL:AAN70762.1};'
  gene_info: Name=visC {ECO:0000313|EMBL:AAN70762.1}; OrderedLocusNames=PP_5197 {ECO:0000313|EMBL:AAN70762.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiH/COQ6 family.
  protein_domains: FAD-bd. (IPR002938); FAD/NAD-bd_sf. (IPR036188); Ubi_Hdrlase_CS.
    (IPR018168); UbiH/COQ6. (IPR010971); UbiH/COQ6_monooxygenase. (IPR051205)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: visC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: visC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CI4
- **Protein Description:** SubName: Full=Oxidoreductase involved in anerobic synthesis of ubiquinone, FAD/NAD(P)-binding domain {ECO:0000313|EMBL:AAN70762.1};
- **Gene Information:** Name=visC {ECO:0000313|EMBL:AAN70762.1}; OrderedLocusNames=PP_5197 {ECO:0000313|EMBL:AAN70762.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiH/COQ6 family.
- **Key Domains:** FAD-bd. (IPR002938); FAD/NAD-bd_sf. (IPR036188); Ubi_Hdrlase_CS. (IPR018168); UbiH/COQ6. (IPR010971); UbiH/COQ6_monooxygenase. (IPR051205)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "visC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'visC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **visC** (gene ID: visC, UniProt: Q88CI4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *visC* (PP_5197 / Q88CI4) in *Pseudomonas putida* KT2440

## Summary

The gene **visC** (ordered locus **PP_5197**; UniProt **Q88CI4**) of *Pseudomonas putida* strain KT2440 encodes a **FAD-dependent aromatic-ring monooxygenase (hydroxylase)** that functions in the **aerobic biosynthesis of ubiquinone (coenzyme Q)**. The protein belongs to the **UbiH/UbiI/COQ6 family** of flavoprotein monooxygenases and is the *P. putida* ortholog of *Escherichia coli* **UbiI** — a gene that was itself originally named *visC* before its function was resolved. Its primary enzymatic role is to catalyze one of the three sequential hydroxylations of the benzene ring of a polyprenyl-phenol intermediate, using **FAD as cofactor, NAD(P)H as the reducing agent, and molecular O₂ as the oxygen donor** (EC 1.14.13.240). Because *P. putida* uses ubiquinone-9 (Q9) as its principal respiratory quinone, the physiological substrate carries a nonaprenyl (C45) isoprenoid tail.

Multiple concordant lines of evidence — orthology (48% amino-acid identity to *E. coli* UbiI, its reciprocal best hit among the three *E. coli* Ubi ring-hydroxylases), the legacy gene symbol *visC* (historically the *E. coli* name for *ubiI*), the KEGG orthology assignment K18800 (=*ubiI*), conserved FAD-binding and Ubi-hydroxylase sequence motifs, and its position in a compact *ubi* hydroxylase gene cluster (PP_5197–PP_5198–PP_5199) — all pin PP_5197 to the **UbiI clade** and specifically to the **first ("C5") ring-hydroxylation step** of the aerobic pathway. The enzyme is expected to act in the **cytoplasm** as a component of a soluble **Ubi biosynthetic metabolon** that associates peripherally with the inner membrane, consistent with the demonstrated biochemistry of the homologous *E. coli* complex.

Two important caveats frame this annotation. First, the UniProt SubName describing the protein as involved in *"anaerobic synthesis of ubiquinone"* is a **legacy misannotation** dating to the original 2002 genome submission: the UbiI/VisC enzyme is strictly the **aerobic, oxygen-dependent** hydroxylase, and a distinct, unrelated system performs the corresponding chemistry under anoxia. Second, the functional assignment for PP_5197 itself rests on **strong homology inference (evidence level PE3)** rather than a direct enzymatic assay of the purified *P. putida* protein; the exact regioselectivity is transferred from the well-characterized *E. coli* ortholog.

---

## Key Findings

### Finding 1 — Identity: PP_5197/visC is the *P. putida* ortholog of *E. coli* UbiI (formerly VisC)

The target protein Q88CI4 is a 407-amino-acid flavoprotein that UniProt classifies within the **UbiH/COQ6 family**, with keywords FAD, Flavoprotein, Monooxygenase, Oxidoreductase, and Ubiquinone, and an annotated PATHWAY of ubiquinone biosynthesis with an FAD cofactor. The KEGG entry `ppu:PP_5197` is assigned to KEGG Orthology **K18800**, whose canonical gene name is **ubiI**. Critically, the legacy gene symbol **visC** carried on this locus is precisely the historical *E. coli* name for *ubiI*: Hajj Chehade and colleagues explicitly renamed the *E. coli* gene *visC* → *ubiI* when they characterized its function. This makes the symbol "visC" a direct and unambiguous marker of the UbiI clade rather than a source of ambiguity.

The InterPro domain architecture reinforces this: IPR010971 (UbiH/COQ6), IPR002938 (FAD-binding), and IPR018168 (Ubi hydroxylase conserved site), together with the eggNOG assignment to COG0654 (2-polyprenyl-6-methoxyphenol hydroxylase and related FAD-dependent oxidoreductases). The identity is thus established by the convergence of family classification, KO assignment, gene symbol history, and domain composition. Evidence level for the specific *P. putida* protein is **PE3 (inferred from homology)** — the assignment is by strong orthology plus a conserved FAD-binding domain, not by direct experiment on PP_5197.

> Supporting quote: *"we show that the uncharacterized conserved visC gene is involved in Q biosynthesis in Escherichia coli, and we have renamed it ubiI"* — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)

### Finding 2 — Primary catalytic function: aromatic-ring hydroxylation in coenzyme Q biosynthesis

The primary function of the gene product is to catalyze an **aromatic C5-hydroxylation** in the ubiquinone biosynthetic pathway. KEGG KO K18800 corresponds to **2-polyprenylphenol 6-hydroxylase, EC 1.14.13.240**; the associated Gene Ontology terms are GO:0019168 (2-polyprenylphenol 6-hydroxylase activity), GO:0006744 (ubiquinone biosynthetic process), and GO:0071949 (FAD binding). The reaction is that of a classic Class A flavoprotein monooxygenase:

> **2-polyprenylphenol + NAD(P)H + H⁺ + O₂ → hydroxylated (catechol) intermediate + NAD(P)⁺ + H₂O**

FAD is reduced by NAD(P)H, reacts with O₂ to form a C4a-hydroperoxyflavin, and this reactive species inserts a single oxygen atom into the aromatic ring. In *E. coli*, the orthologous UbiI protein was shown both genetically and biochemically to catalyze the C5-hydroxylation step, and its crystal structure resembles the canonical FAD-dependent *para*-hydroxybenzoate hydroxylase (PHBH), with flavin-pocket residues required for activity. Because *P. putida* synthesizes ubiquinone-9, the physiological substrate carries a **nonaprenyl (C45) tail** rather than the octaprenyl (C40) tail of the *E. coli* Q8 series.

> Supporting quotes — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/):
> - *"we establish that the UbiI protein functions in the C5-hydroxylation reaction"*
> - *"This structure shares many features with the canonical FAD-dependent para-hydroxybenzoate hydroxylase"*
> - *"UbiI is only implicated in aerobic Q biosynthesis and that an alternative enzyme catalyzes the C5-hydroxylation reaction in the absence of oxygen"*

### Finding 3 — Position in the pathway: the first of three ring hydroxylations

Ubiquinone biosynthesis requires three distinct hydroxylations of the aromatic ring, at positions C5, C6, and C1, each performed by a dedicated FAD-dependent monooxygenase (UbiI, UbiH, and UbiF respectively in *E. coli*). UbiI/VisC catalyzes the **first** of these. Evidence for this ordering comes from the *E. coli* mutant phenotype: a *ubiI*-deficient strain has a low level of Q and accumulates **2-octaprenylphenol** — the un-hydroxylated precursor — which was purified and characterized. Accumulation of this early, un-hydroxylated intermediate places UbiI at the first ring-hydroxylation position.

By orthology, *P. putida* PP_5197 occupies the same first-hydroxylation position, converting **2-nonaprenylphenol** (the Q9-series precursor) to its 6-hydroxy (catechol) product; the subsequent C6 hydroxylation is performed by UbiH (PP_5199) and the C1 hydroxylation by a UbiF-type enzyme encoded elsewhere in the genome.

> Supporting quote: *"A strain deficient in ubiI has a low level of Q and accumulates a compound derived from the Q biosynthetic pathway, which we purified and characterized"* — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)

### Finding 4 — Reciprocal-best-hit orthology distinguishes UbiI from its paralogs UbiH and UbiF

Because the three *E. coli* ring hydroxylases are all homologous (>37% mutual identity), it is essential to confirm that PP_5197 belongs specifically to the UbiI clade rather than to UbiH or UbiF. Global pairwise alignment of Q88CI4 against the three paralogs gives:

| *E. coli* paralog | UniProt | Identity to Q88CI4 | Alignment length |
|-------------------|---------|--------------------|------------------|
| **UbiI / VisC** (C5) | P25535 | **48.2%** | 396 aa |
| UbiF (C1) | P75728 | 44.6% | 386 aa |
| UbiH / VisB (C6) | P25534 | 37.2% | 387 aa |

**UbiI is the clear best match.** This is fully concordant with the KEGG KO assignment (K18800 = *ubiI*), the legacy gene symbol *visC* (= *E. coli ubiI*), and the presence of a separate UbiH ortholog at the neighboring locus PP_5199. The three paralogs remain closely related (>37% identity), consistent with the documented evolutionary plasticity of regioselectivity within this enzyme clade — a point relevant to how confidently the exact hydroxylation position can be transferred across species.

> Framing quote: *"Multiple Proteobacterial Enzymes with Various Regioselectivities To Catalyze Three Contiguous Aromatic Hydroxylation Reactions"* — [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)

### Finding 5 — Structural and sequence evidence: a PHBH/GR2-class FAD hydroxylase fold

The Q88CI4 sequence carries the diagnostic features of the p-hydroxybenzoate-hydroxylase (PHBH)/GR2 glutathione-reductase-2 structural class of flavoprotein monooxygenases. It contains the N-terminal βαβ dinucleotide-binding (Rossmann) fingerprint **GxGxxG** at residues 10–16 (¹⁰VGAGMVGS), which forms the FAD-binding cradle, plus the conserved **DAAHTIH** motif at approximately residue 293 that defines the InterPro Ubi_Hdrlase conserved site (IPR018168). These motifs match the crystallographically characterized *E. coli* UbiI, which "shares many features with the canonical FAD-dependent para-hydroxybenzoate hydroxylase."

The genomic context corroborates the assignment. PP_5197 (*ubiI*/*visC*, K18800) lies immediately adjacent to PP_5199 (*ubiH*; 2-octaprenyl-6-methoxyphenol hydroxylase, K03185), flanking PP_5198 ("conserved protein of unknown function"), forming a compact **ubiquinone-hydroxylase gene cluster**. The surrounding genes — PP_5195/5196 (an iron ABC transporter) and PP_5200 (*pepP*) — are functionally unrelated, delimiting the cluster.

> Supporting quote: *"This structure shares many features with the canonical FAD-dependent para-hydroxybenzoate hydroxylase"* — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)

### Finding 6 — Subcellular localization: cytoplasmic soluble Ubi metabolon

The enzyme carries out its function in the **cytoplasm** as part of a soluble multiprotein assembly. UniProt annotates Q88CI4 with the cellular-component term GO:0110142 (ubiquinone biosynthesis complex). In *E. coli*, seven Ubi proteins — including UbiI/VisC — assemble into a stable ~1-MDa soluble **metabolon** that catalyzes the last six reactions of the UQ biosynthetic pathway. This complex was purified from cytoplasmic extracts and shown to be catalytically active there, challenging the older view that UQ biosynthesis is strictly a membrane-embedded process. The SCP2 lipid-binding domain of the accessory protein UbiJ sequesters the highly hydrophobic polyprenyl intermediates, allowing the otherwise water-insoluble substrates to be processed by soluble enzymes.

Thus, although ubiquinone ultimately functions within the inner membrane as the respiratory electron carrier, its *biosynthesis* — including the VisC/UbiI hydroxylation step — occurs in a cytoplasmic complex that is peripherally associated with, rather than integral to, the inner membrane.

> Supporting quotes — [PMID: 30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/):
> - *"seven Ubi proteins form the Ubi complex, a stable metabolon that catalyzes the last six reactions of the UQ biosynthetic pathway in Escherichia coli"*
> - *"We purify the Ubi complex from cytoplasmic extracts and demonstrate that UQ biosynthesis occurs in this fraction, challenging the current thinking of a membrane-associated biosynthetic process"*

### Finding 7 — Physiological role: aerobic ubiquinone supply for respiration and O₂/redox-linked phenotypes

The broader biological role of the VisC/UbiI hydroxylation step is to supply **ubiquinone for the aerobic respiratory chain**, where UQ serves as the central lipophilic electron carrier. The physiological consequences of losing this step were demonstrated in uropathogenic *E. coli* (UPEC): deletion of *ubiI* (formerly *visC*) reduced membrane potential, diminished motility, and reduced type 1 pilus (chaperone-usher pathway) expression and biofilm formation — but only under **aerobic (oxic)** conditions. Under anoxia, where alternative oxygen-independent quinone synthases operate, the deletion had no such effect. This ties the hydroxylation step specifically to **oxygen-dependent UQ supply and aerobic respiratory competence**. In *P. putida*, an obligate aerobe that relies heavily on aerobic respiration, this function is expected to be central to respiratory metabolism.

> Supporting quote: *"Consistent with its function as an aerobic ubiquinone-8 synthase, deletion of ubiI in UPEC resulted in reduced membrane potential, diminished motility, and reduced expression of chaperone-usher pathway pili"* — [PMID: 27161114](https://pubmed.ncbi.nlm.nih.gov/27161114/)

### Finding 8 — Correcting the UniProt "anaerobic" misannotation

The UniProt SubName for Q88CI4 — *"Oxidoreductase involved in anerobic synthesis of ubiquinone"* — derives from the original 2002 KT2440 genome submission (EMBL AAN70762.1) and is a **legacy misannotation**. Biochemical and genetic characterization of the *E. coli* ortholog unambiguously established that UbiI is implicated **only in aerobic** Q biosynthesis, using molecular O₂ as co-substrate; a distinct, unrelated system performs the corresponding hydroxylation under anaerobic conditions. KEGG and GO consistently annotate PP_5197 as an O₂-utilizing monooxygenase (EC 1.14.13.240, incorporating one atom of molecular oxygen). The correct descriptor for this protein is therefore the **aerobic** ubiquinone ring hydroxylase.

> Supporting quote: *"UbiI is only implicated in aerobic Q biosynthesis and that an alternative enzyme catalyzes the C5-hydroxylation reaction in the absence of oxygen"* — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)

---

## Mechanistic Model and Interpretation

### The reaction catalyzed

VisC/UbiI is a **Class A (single-component) flavoprotein monooxygenase** of the PHBH/GR2 structural class. Its catalytic cycle proceeds as follows:

```
   NAD(P)H          O2                    Aromatic substrate
      |              |                          |
      v              v                          v
  FAD --> FADH2 --> C4a-hydroperoxy-FAD --> ring hydroxylation
                          |                     |
                          +--> FAD + H2O <------+
                                (H2O2 uncoupling minor)

  2-nonaprenylphenol  +  NAD(P)H  +  O2  -->  6-hydroxy-2-nonaprenylphenol
                                              (catechol intermediate)  +  NAD(P)+  +  H2O
```

The flavin is reduced by NAD(P)H, then reacts with molecular oxygen to form a **C4a-hydroperoxyflavin**, the reactive intermediate that transfers a single oxygen atom to the aromatic ring. This oxygen dependence is the mechanistic basis for the enzyme's strict aerobic requirement (Finding 8).

### Position in the ubiquinone pathway

Ubiquinone biosynthesis in proteobacteria proceeds from 4-hydroxybenzoate (4-HB) through prenylation, decarboxylation, three ring hydroxylations, and three O-methylations. The three hydroxylations are the work of a paralogous trio:

```
  4-hydroxybenzoate
        | (prenylation: UbiA; decarboxylation: UbiD/UbiX)
        v
  2-polyprenylphenol
        | ---- C5 hydroxylation ----> [ UbiI / VisC = PP_5197 ]   <-- THIS PROTEIN
        v
  (methylation by UbiG; C6 hydroxylation by UbiH = PP_5199)
        |
        v
  (C1 hydroxylation by UbiF; methylations by UbiE/UbiG)
        v
  Ubiquinone-9 (Q9)  --->  inner-membrane respiratory chain
```

Each hydroxylase inserts a hydroxyl at a specific ring carbon; the O-methyltransferases (UbiG, UbiE) then cap these hydroxyls, building the fully substituted benzoquinone head group. VisC/UbiI performs the earliest of the three hydroxylations, acting on the still-un-hydroxylated 2-polyprenylphenol (Finding 3).

### Localization and the metabolon

Although the final product Q9 resides in and functions at the inner membrane, the biosynthetic chemistry — including VisC/UbiI — occurs in a **soluble cytoplasmic metabolon** (Finding 6). The polyprenyl intermediates are extremely hydrophobic; the metabolon solves the solubility problem by using the SCP2 domain of UbiJ as a lipid chaperone that shuttles intermediates between the active sites of the assembled enzymes. This physical organization couples the sequential hydroxylation and methylation steps and likely enforces the ordered progression of the pathway.

### Synthesis

Bringing these threads together: **visC/PP_5197 encodes the aerobic, FAD-dependent C5 ring-hydroxylase of ubiquinone-9 biosynthesis in *P. putida* KT2440.** It works in the cytoplasm within a soluble Ubi metabolon, uses O₂ and NAD(P)H, and supplies the respiratory quinone that powers aerobic energy metabolism. Its function is inferred with high confidence from convergent orthology, domain, KO, and genomic-context evidence, but has not been assayed directly in *P. putida*.

---

## Evidence Base

| PMID | Title | Role in this report |
|------|-------|---------------------|
| [23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/) | *ubiI, a new gene in Escherichia coli coenzyme Q biosynthesis, is involved in aerobic C5-hydroxylation* | **Primary source.** Establishes visC = ubiI; defines the C5-hydroxylation reaction; demonstrates strict aerobic (O₂-dependent) requirement; shows PHBH-like structural fold; places UbiI at the first hydroxylation via intermediate accumulation. Underpins Findings 1, 2, 3, 5, 8. |
| [30686758](https://pubmed.ncbi.nlm.nih.gov/30686758/) | *A Soluble Metabolon Synthesizes the Isoprenoid Lipid Ubiquinone* | Establishes the cytoplasmic soluble metabolon localization and the role of UbiJ's SCP2 domain in sequestering hydrophobic intermediates. Underpins Finding 6. |
| [27161114](https://pubmed.ncbi.nlm.nih.gov/27161114/) | *The UbiI (VisC) Aerobic Ubiquinone Synthase Is Required for Expression of Type 1 Pili, Biofilm Formation, and Pathogenesis in Uropathogenic E. coli* | Demonstrates aerobic-specific physiological consequences of losing UbiI/VisC — reduced membrane potential, motility, piliation. Underpins Finding 7. |
| [27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/) | *Evolution of Ubiquinone Biosynthesis: Multiple Proteobacterial Enzymes with Various Regioselectivities...* | Frames the paralog-assignment problem and the plasticity of regioselectivity across UbiI/UbiH/UbiF. Underpins Finding 4 and the interpretation of orthology confidence. |
| [18323682](https://pubmed.ncbi.nlm.nih.gov/18323682/) | *Pseudomonas japonica sp. nov...* | Corroborating background: confirms that *Pseudomonas* strains of the *putida* subcluster use **ubiquinone-9 (Q9)** as the main respiratory quinone, supporting identification of the Q9-series substrate. |

All five papers support (none fundamentally challenge) the annotation. The one point of nuance is [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/), which cautions that regioselectivity within this hydroxylase family can vary across lineages — a reason to treat the exact "C5" position for *P. putida* as an inference rather than a certainty.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical assay of the *P. putida* protein.** The functional assignment for PP_5197 rests entirely on homology inference (UniProt evidence level PE3). The enzyme has not been purified from *P. putida*, and its activity, substrate specificity, and kinetic parameters have not been measured directly. All catalytic claims are transferred from the *E. coli* UbiI ortholog.

2. **Regioselectivity is inferred, not proven.** Because UbiI, UbiH, and UbiF are homologous (37–48% identity) and the family shows documented plasticity in regioselectivity ([PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)), the precise hydroxylation position catalyzed by PP_5197 in *P. putida* cannot be assumed to be identical to that of *E. coli* UbiI without experimental confirmation.

3. **Substrate tail length.** The Q9 substrate (nonaprenyl tail) is inferred from the respiratory quinone profile of *P. putida*-group organisms rather than confirmed for this specific enzyme; the enzyme's tolerance for different prenyl chain lengths is unknown.

4. **Metabolon composition in *P. putida* is unverified.** The soluble Ubi metabolon was characterized in *E. coli*; whether *P. putida* assembles an equivalent complex, and whether PP_5198 (the "conserved protein of unknown function" between visC and ubiH) participates, remains untested.

5. **Legacy database annotation.** The UniProt "anaerobic" descriptor is demonstrably incorrect and should be flagged; downstream automated annotations that propagate this label may be misleading.

---

## Proposed Follow-up Experiments and Actions

1. **Genetic complementation.** Test whether cloned PP_5197 restores ubiquinone synthesis and aerobic respiratory growth in an *E. coli* Δ*ubiI* mutant — a direct, tractable test of orthologous function.

2. **Targeted gene deletion in *P. putida* KT2440.** Construct a clean PP_5197 deletion and quantify ubiquinone-9 levels (HPLC/LC-MS) and accumulation of the predicted 2-nonaprenylphenol precursor; assess aerobic respiratory phenotypes (growth rate, membrane potential, oxygen consumption).

3. **In vitro enzymology.** Heterologously express and purify Q88CI4, reconstitute with FAD and NAD(P)H, and assay hydroxylation of a synthetic polyprenyl-phenol substrate under O₂; determine the exact ring position hydroxylated by LC-MS/NMR to confirm C5 regioselectivity.

4. **Structural determination.** Solve the crystal or cryo-EM structure of PP_5197 (or use an AlphaFold model validated against the *E. coli* UbiI structure) to confirm the PHBH-like fold and map the FAD-binding and substrate pockets.

5. **Metabolon reconstitution.** Test co-purification/interaction of PP_5197 with PP_5199 (UbiH) and PP_5198 to determine whether *P. putida* forms an analogous soluble Ubi metabolon, and clarify the role of PP_5198.

6. **Database correction.** Submit an annotation update to correct the "anaerobic" descriptor in UniProt Q88CI4 to reflect the aerobic, O₂-dependent function.


## Artifacts

- [OpenScientist final report](visC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](visC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23709220
2. PMID:27822549
3. PMID:30686758
4. PMID:27161114