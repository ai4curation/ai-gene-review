---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T16:46:23.964464'
end_time: '2026-07-17T17:42:47.138856'
duration_seconds: 3383.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argC2
  gene_symbol: argC2
  uniprot_accession: P59308
  protein_description: 'RecName: Full=N-acetyl-gamma-glutamyl-phosphate reductase
    2 {ECO:0000255|HAMAP-Rule:MF_01110}; Short=AGPR 2 {ECO:0000255|HAMAP-Rule:MF_01110};
    EC=1.2.1.38 {ECO:0000255|HAMAP-Rule:MF_01110}; AltName: Full=N-acetyl-glutamate
    semialdehyde dehydrogenase 2 {ECO:0000255|HAMAP-Rule:MF_01110}; Short=NAGSA dehydrogenase
    2 {ECO:0000255|HAMAP-Rule:MF_01110};'
  gene_info: Name=argC2 {ECO:0000255|HAMAP-Rule:MF_01110}; OrderedLocusNames=PP_3633;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAGSA dehydrogenase family. Type 2
  protein_domains: AGPR. (IPR050085); AGPR_AS. (IPR023013); AGPR_dimerisation_dom.
    (IPR058924); AGPR_type-2. (IPR010136); NAD(P)-bd_dom_sf. (IPR036291)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: argC2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argC2-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P59308
- **Protein Description:** RecName: Full=N-acetyl-gamma-glutamyl-phosphate reductase 2 {ECO:0000255|HAMAP-Rule:MF_01110}; Short=AGPR 2 {ECO:0000255|HAMAP-Rule:MF_01110}; EC=1.2.1.38 {ECO:0000255|HAMAP-Rule:MF_01110}; AltName: Full=N-acetyl-glutamate semialdehyde dehydrogenase 2 {ECO:0000255|HAMAP-Rule:MF_01110}; Short=NAGSA dehydrogenase 2 {ECO:0000255|HAMAP-Rule:MF_01110};
- **Gene Information:** Name=argC2 {ECO:0000255|HAMAP-Rule:MF_01110}; OrderedLocusNames=PP_3633;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAGSA dehydrogenase family. Type 2
- **Key Domains:** AGPR. (IPR050085); AGPR_AS. (IPR023013); AGPR_dimerisation_dom. (IPR058924); AGPR_type-2. (IPR010136); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argC2" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argC2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argC2** (gene ID: argC2, UniProt: P59308) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **argC2** (UniProt P59308, locus PP_3633) in *Pseudomonas putida* KT2440

## 0. Gene/Protein Identity Verification (PASSED)

The target gene symbol **argC2** is **consistent** with the UniProt protein description, organism, and domain architecture — there is **no** identity ambiguity or same-symbol homonym problem:

| Attribute | Target (UniProt) | Verified against databases | Match |
|---|---|---|---|
| Accession | P59308 | UniProtKB P59308 | ✔ |
| Protein | N-acetyl-γ-glutamyl-phosphate reductase 2 (AGPR 2 / NAGSA dehydrogenase 2), EC 1.2.1.38 | UniProt FUNCTION + KEGG K00145 (EC 1.2.1.38) | ✔ |
| Gene / locus | argC2 / PP_3633 | KEGG `ppu:PP_3633`; GenBank AAN69233 | ✔ |
| Organism | *P. putida* KT2440 (taxid 160488) | UniProt organism = taxid 160488 | ✔ |
| Family | NAGSA dehydrogenase family, Type 2 | UniProt SIMILARITY; InterPro IPR010136 (AGPR type-2) | ✔ |

All literature and database evidence below refers to the AGPR (ArgC) enzyme family and to *P. putida* KT2440 specifically. **The gene is correctly identified.**

---

## 1. Summary (Answer to the Research Question)

**argC2 (P59308, PP_3633) encodes N-acetyl-γ-glutamyl-phosphate reductase (AGPR; also called N-acetyl-glutamate-5-semialdehyde / NAGSA dehydrogenase), a cytoplasmic, NADPH-dependent oxidoreductase (EC 1.2.1.38).** It catalyzes the third (and only reductive) step of de novo **L-arginine biosynthesis** via the acetylated-ornithine route: the reduction of the acyl-phosphate **N-acetyl-L-glutamyl-5-phosphate** to the aldehyde **N-acetyl-L-glutamate-5-semialdehyde**, consuming NADPH and releasing inorganic phosphate and NADP⁺ (Rhea:21588). Its substrate is specifically the **N-acetylated** glutamyl-phosphate intermediate, not free glutamate derivatives, because the acetyl "protecting group" is retained throughout the pathway and recycled by ornithine acetyltransferase (ArgJ).

A distinctive feature uncovered here: *P. putida* KT2440 is **unusual in carrying two AGPR paralogs**. Comparative genomics shows that the **conserved, single-copy housekeeping AGPR** of *Pseudomonas* corresponds to **argC1/PP_0432** (91.5% identical to the sole AGPR of *P. aeruginosa*), whereas **argC2 is a divergent, lineage-restricted "Type-2" second isozyme** (~52% identical to the housekeeping enzyme). argC2 retains every catalytic determinant and is therefore predicted to catalyze the same reaction, most plausibly as an **accessory/conditionally-expressed isozyme**.

The functional annotation of P59308 itself is **computational/homology-based** (UniProt protein-existence level 3, HAMAP-Rule MF_01110); the reaction assignment is strongly supported by direct biochemistry on orthologous ArgC enzymes and by conservation of the catalytic machinery.

---

## 2. Primary Function: the Catalyzed Reaction and Substrate Specificity

### 2.1 Reaction
AGPR catalyzes (physiological direction = reductive, right→left as written by UniProt):

> **N-acetyl-L-glutamyl-5-phosphate + NADPH + H⁺ → N-acetyl-L-glutamate-5-semialdehyde + phosphate + NADP⁺**
> (EC 1.2.1.38; Rhea:21588; GO:0003942 "N-acetyl-γ-glutamyl-phosphate reductase activity")

UniProt (HAMAP MF_01110) states the FUNCTION verbatim: *"Catalyzes the NADPH-dependent reduction of N-acetyl-5-glutamyl phosphate to yield N-acetyl-L-glutamate 5-semialdehyde."* KEGG places PP_3633 under EC 1.2.1.38 (oxidoreductase acting on the aldehyde/oxo group of donors, with NAD⁺/NADP⁺ as acceptor).

Mechanistically this is an unusual "reverse" dehydrogenase step: it reductively dephosphorylates a **high-energy acyl-phosphate** to an aldehyde. The reaction is energetically costly and is described in the literature as *"the high-energy-consuming third step in the arginine synthesis pathway"* (Vargas-Lagunas et al., 2017, PMID 29121239).

### 2.2 Substrate specificity
- **Acyl-phosphate substrate:** N-acetyl-L-glutamyl-5-phosphate (the product of N-acetylglutamate kinase, ArgB).
- **Reductant/cofactor:** NADPH (the enzyme carries an NAD(P)-binding Rossmann-type fold; InterPro IPR036291; GO:0051287 "NAD binding").
- The **N-acetyl group is obligatory**: the entire pathway operates on N-acetylated intermediates so that the α-amino group of glutamate is masked, preventing spontaneous cyclization of the glutamate-5-semialdehyde to Δ¹-pyrroline-5-carboxylate (which would divert flux toward proline). ArgC therefore has strict specificity for the *acetylated* semialdehyde/acyl-phosphate pair, distinguishing it from the analogous non-acetylated enzymes of proline/ornithine metabolism.

### 2.3 Enzyme identity — experimental support from orthologs
Because P59308 has not itself been assayed, the reaction assignment rests on **direct biochemical characterization of orthologous ArgC enzymes**, all of which complement *E. coli argC* mutants and display AGPR/semialdehyde-dehydrogenase activity:
- *Corynebacterium glutamicum* ArgC: *"the cloned gene indeed codes for N-acetylglutamate 5-semialdehyde dehydrogenase"* (Chun et al., 1998, PMID 9818083).
- *Streptomyces clavuligerus* ArgC: *"The argC gene … encoding N-acetylglutamyl-phosphate reductase (AGPR) has been cloned by complementation of argC mutants"* (Ludovice et al., 1992, PMID 1339424).
- *Sinorhizobium meliloti* ArgC: *"argC encodes N-acetyl-gamma-glutamyl phosphate reductase, the enzyme that catalyzes the … third step in the arginine synthesis pathway"* (Vargas-Lagunas et al., 2017, PMID 29121239).

---

## 3. Structural Basis and Catalytic Mechanism (inference from sequence/structure)

P59308 is a **313-residue** soluble protein built on the semialdehyde-dehydrogenase fold (Pfam Semialdhyde_dh / Semialdhyde_dhC), comprising an N-terminal NAD(P)-binding (Rossmann-like) domain and a C-terminal catalytic/dimerization domain (InterPro IPR058924 "AGPR dimerisation domain"). AGPRs are typically **homodimers**, consistent with the dedicated dimerization domain.

Two lines of structure/evolution evidence support catalytic competence:
1. **Conserved active-site motif.** The diagnostic AGPR signature **P-G-C-Y-P-T** (InterPro IPR023013 "AGPR_AS") is present at residues 115–120 (context `…RVSN`**`PGCYPT`**`GAI…`), placing the **invariant catalytic cysteine at position 117**. Ludovice et al. (1992) identified this PGCYPT motif as conserved across all AGPRs and proposed it as *"the active center of the protein"* (PMID 1339424). The active-site cysteine forms the covalent thioacyl/tetrahedral intermediate during hydride transfer from NADPH to the acyl-phosphate carbon.
2. **Cofactor-binding elements.** A C-terminal glycine-rich segment (K-G-A-S-G, residues 291–296) and the NAD(P)-binding domain superfamily fold (IPR036291) provide the dinucleotide-binding platform (GO:0051287).

**Structural-model corroboration.** The AlphaFold model (AF-P59308-F1, v6) is **very high confidence** — global pLDDT **96.1**, with 93% of residues at pLDDT ≥ 90 and the catalytic segment (residues 115–120, PGCYPT/Cys117) modeled at pLDDT 97–99. This indicates a compact, well-ordered globular fold with a structurally well-defined active site, providing structure-based support — beyond sequence homology — that argC2 is a folded, catalytically configured AGPR.

**Type-1 vs Type-2 distinction (a defining feature of argC2):** the classical (Type-1) ArgC — e.g., *P. aeruginosa* PA0662 and *P. putida* argC1/PP_0432 — carries the canonical N-terminal Rossmann fingerprint **G-x-G-x-x-G** ("GIVGGTGY", residues 5–10). **argC2 lacks this canonical N-terminal motif**, the structural hallmark of the InterPro **Type-2** AGPR subfamily (IPR010136). Despite the rearranged dinucleotide-binding region, argC2 retains the catalytic Cys and C-terminal binding motifs, so it is predicted to be a functional, if divergent, NADPH-dependent AGPR.

---

## 4. Biological Process and Pathway Context

AGPR operates in the **de novo L-arginine biosynthetic pathway** (glutamate → ornithine → citrulline → arginine) via **N-acetylated intermediates**, the general route in microorganisms (Xu, Labedan & Glansdorff, 2007, PMID 17347518; Caldovic & Tuchman, 2003, PMID 12633501). KEGG assigns PP_3633 to **module M00028** ("Ornithine biosynthesis, glutamate => ornithine") and pathway **ppu00220** (Arginine biosynthesis); UniProt places it at **step 3 of 4** in the sub-pathway "N(2)-acetyl-L-ornithine from L-glutamate."

The reaction sequence and the *P. putida* genes involved:

1. **Glutamate acetylation** → N-acetylglutamate (NAG). *P. putida* uses the **cyclic/economical** variant in which **ornithine acetyltransferase ArgJ (PP_1346)** transfers the acetyl group from N-acetylornithine back onto glutamate — *"NAG can be produced by … NAG synthase (NAGS) and … ornithine acetyltransferase (OAT)"* (Caldovic & Tuchman, 2003, PMID 12633501).
2. **NAG phosphorylation** by N-acetylglutamate kinase **ArgB (PP_5289)** → N-acetyl-L-glutamyl-5-phosphate.
3. **Reduction by AGPR (argC / argC2)** → **N-acetyl-L-glutamate-5-semialdehyde** ⟵ *the step catalyzed by P59308*.
4. **Transamination** by acetylornithine aminotransferase **ArgD (PP_0372)** → N-acetylornithine.
5. Conversion to **ornithine** (via ArgJ acetyl-recycling and/or ArgE deacetylation), then carbamoylation → citrulline → argininosuccinate → **L-arginine**.

Thus the precise metabolic role of argC2 is to supply **N-acetyl-glutamate-5-semialdehyde** — the amino-group acceptor for the downstream transaminase — as the **sole reductive (NADPH-consuming) node** of ornithine biosynthesis. This is a strictly anabolic, biosynthetic role (not catabolic and not regulatory).

---

## 5. Subcellular Localization

**Cytoplasm.** UniProt SUBCELLULAR LOCATION = Cytoplasm (GO:0005737, cytoplasm). This is expected and well supported: AGPR is a soluble metabolic dehydrogenase with no signal peptide, no transmembrane segments, and a cofactor-dependent globular fold; all substrates/products (acetyl-glutamyl-phosphate, semialdehyde, NADPH/NADP⁺, Pi) are cytosolic metabolites. The enzyme therefore carries out its function in the bacterial cytosol.

---

## 6. Paralogy, Evolution, and the Special Status of *argC2*

A central result of this investigation concerns **why *P. putida* has an "argC2" at all**:

- **Copy number is unusual.** Across representative genomes, *P. aeruginosa* (PA0662), *P. protegens* (PFL_5611), *P. stutzeri* (PSPTO_0604), *P. syringae* (Psyr_4569) and *E. coli* (b3958 = argC) each encode **one** AGPR (K00145). **Only *P. putida* KT2440 encodes two** — PP_0432 (argC1) and PP_3633 (argC2).
- **argC1 is the conserved ortholog.** The single-copy *P. aeruginosa* AGPR (PA0662) is **91.5%** identical to argC1/PP_0432 but only **52.3%** identical to argC2/PP_3633 (Needleman–Wunsch, this work). argC1 and PA0662 share the Type-1 N-terminal Rossmann motif. Hence **argC1 is the housekeeping ArgC**; **argC2 is a divergent, taxonomically restricted second isozyme** (Type 2), sharing only ~53% identity with argC1.
- **Genomic context suggests an accessory role.** argC2/PP_3633 is **not** in an arg operon (the core arg genes are dispersed). Its immediate neighbors are a **divergent LysR-family transcriptional regulator (PP_3632)**, a **GNAT-family acetyltransferase (PP_3634)**, and a **sulfonate/nitrate NitT/TauT ABC transporter (PP_3635–37)**. Co-location with a dedicated regulator and an acetyltransferase (a potential source/recycler of acetyl groups) is consistent with a **conditionally regulated or sub-/neo-functionalized** copy, rather than the constitutive biosynthetic enzyme — though this is inference from gene neighborhood and awaits experimental test.

**Interpretation.** argC2 most likely arose by gene duplication/divergence (or acquisition) in the *P. putida* lineage and provides a **second, divergent AGPR activity**. Its retained catalytic machinery makes it a bona fide predicted AGPR (EC 1.2.1.38); its divergence and genomic setting hint at a specialized physiological trigger. Whether it acts on the canonical N-acetyl-glutamyl-phosphate substrate exclusively, or has shifted specificity, is not experimentally resolved.

---

## 7. Evidence Summary and Confidence

| Claim | Evidence type | Strength |
|---|---|---|
| Enzyme = AGPR, EC 1.2.1.38, reduces N-acetyl-glutamyl-5-phosphate → N-acetylglutamate-5-semialdehyde (NADPH) | UniProt/HAMAP + KEGG annotation; **direct biochemistry on orthologs** (PMIDs 9818083, 1339424, 29121239) | High |
| Catalytic Cys117 in conserved PGCYPT motif; NAD(P)-binding fold | Sequence/structure inference; motif defined by PMID 1339424 | High |
| Role = step 3 of acetylated arginine/ornithine pathway; substrate is N-acetylated | KEGG module M00028; pathway reviews (PMIDs 17347518, 12633501) | High |
| Localization = cytoplasm | UniProt/GO; sequence features (no signal/TM) | High |
| Well-ordered AGPR fold with defined active site | AlphaFold AF-P59308-F1, global pLDDT 96.1 (active site 97–99) | High (structural model) |
| argC2 is the divergent Type-2 second isozyme; argC1/PP_0432 is the conserved housekeeping ortholog | Comparative genomics + pairwise identity (this work) | High (bioinformatic) |
| Accessory/conditional role implied by genomic context | Gene-neighborhood inference | Moderate / hypothesis |
| Direct enzymology of P59308 itself; substrate-specificity kinetics; in vivo phenotype of a *P. putida argC2* mutant | — | **Not available (gap)** |

---

## 8. Supported and Refuted Hypotheses

- **Supported:** argC2 is an AGPR (EC 1.2.1.38) acting in arginine biosynthesis; it is cytoplasmic; it retains the catalytic Cys/PGCYPT machinery; it is a divergent Type-2 paralog distinct from the conserved housekeeping AGPR.
- **Supported (comparative-genomic):** the conserved single-copy *Pseudomonas* AGPR corresponds to argC1/PP_0432, identifying argC2 as the lineage-specific "extra" copy.
- **Not refuted, unresolved:** that argC2 is an accessory/conditionally-expressed isozyme (plausible from genomics; not experimentally tested). Whether argC2 can fully substitute for argC1 in arginine prototrophy is unknown.

## 9. Limitations and Future Directions

- P59308 is annotated by homology (existence level 3); **no direct enzymology, structure, or targeted mutant** of this specific protein exists in the retrieved literature.
- Attempts to retrieve high-throughput RB-TnSeq fitness data (LBL Fitness Browser) were blocked (HTTP 403); direct genetic-essentiality evidence for argC2 vs argC1 could not be obtained. The task prioritizes precise over high-throughput data, so this does not affect the core annotation.
- **Recommended experiments:** (i) recombinant expression + spectrophotometric AGPR assay (NADPH oxidation with N-acetyl-glutamyl-phosphate) and steady-state kinetics; (ii) single and double *argC1/argC2* deletions with arginine-auxotrophy complementation; (iii) reporter/RNA-seq to identify the condition(s) and the LysR regulator controlling argC2; (iv) crystallography/AlphaFold-guided analysis of the atypical Type-2 N-terminal dinucleotide-binding region.

---

### Key References
- Chun et al. 1998, *Mol. Cells* — *C. glutamicum* argC encodes NAGSA dehydrogenase (PMID 9818083).
- Ludovice et al. 1992, *J. Bacteriol.* — *S. clavuligerus* argC = AGPR; conserved PGCYPT active-site motif (PMID 1339424).
- Vargas-Lagunas et al. 2017, *FEMS/Mol. genetics* — argC = N-acetyl-γ-glutamyl-phosphate reductase, energy-consuming third step (PMID 29121239).
- Xu, Labedan & Glansdorff 2007, *Microbiol. Mol. Biol. Rev.* — arginine biosynthesis via acetylated intermediates (PMID 17347518).
- Caldovic & Tuchman 2003, *Biochem. J.* — N-acetylglutamate and the acetylated arginine pathway; NAGS vs OAT (PMID 12633501).
- Database records: UniProt **P59308** (HAMAP MF_01110); KEGG **ppu:PP_3633** (K00145, EC 1.2.1.38, module M00028); InterPro IPR010136/IPR023013/IPR058924/IPR036291.


## Artifacts

- [OpenScientist final report](argC2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argC2-deep-research-openscientist_artifacts/final_report.pdf)