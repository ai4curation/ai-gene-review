---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:18:07.184130'
end_time: '2026-07-20T20:11:24.580392'
duration_seconds: 6797.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moaA
  gene_symbol: moaA
  uniprot_accession: Q88E69
  protein_description: 'RecName: Full=GTP 3'',8-cyclase {ECO:0000255|HAMAP-Rule:MF_01225};
    EC=4.1.99.22 {ECO:0000255|HAMAP-Rule:MF_01225}; AltName: Full=Molybdenum cofactor
    biosynthesis protein A {ECO:0000255|HAMAP-Rule:MF_01225};'
  gene_info: Name=moaA {ECO:0000255|HAMAP-Rule:MF_01225}; OrderedLocusNames=PP_4597;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the radical SAM superfamily. MoaA family.
  protein_domains: Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638);
    MoaA. (IPR013483); MoaA-like. (IPR040064); MoaA_NifB_PqqE_Fe-S-bd_CS. (IPR000385)
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
  path: moaA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moaA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E69
- **Protein Description:** RecName: Full=GTP 3',8-cyclase {ECO:0000255|HAMAP-Rule:MF_01225}; EC=4.1.99.22 {ECO:0000255|HAMAP-Rule:MF_01225}; AltName: Full=Molybdenum cofactor biosynthesis protein A {ECO:0000255|HAMAP-Rule:MF_01225};
- **Gene Information:** Name=moaA {ECO:0000255|HAMAP-Rule:MF_01225}; OrderedLocusNames=PP_4597;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the radical SAM superfamily. MoaA family.
- **Key Domains:** Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638); MoaA. (IPR013483); MoaA-like. (IPR040064); MoaA_NifB_PqqE_Fe-S-bd_CS. (IPR000385)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moaA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moaA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moaA** (gene ID: moaA, UniProt: Q88E69) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MoaA (GTP 3',8-cyclase) in *Pseudomonas putida* KT2440

**Gene:** *moaA* (OrderedLocusName PP_4597) · **UniProt:** Q88E69 · **EC:** 4.1.99.22
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) (PSEPK)
**Family:** Radical SAM superfamily, MoaA family (HAMAP MF_01225)

---

## 1. Summary (Answer to the Research Question)

MoaA is a **radical S-adenosyl-L-methionine (SAM) metalloenzyme, GTP 3',8-cyclase**, that catalyzes the **first and committed step of molybdenum cofactor (Moco) biosynthesis**. Acting in the **cytoplasm**, it converts **5'-GTP** into the intermediate **3',8-cyclo-7,8-dihydro-GTP**, which the partner protein MoaC then converts into **cyclic pyranopterin monophosphate (cPMP, "precursor Z")**. Its primary molecular function is a chemically difficult, radical-initiated **intramolecular C–C bond–forming rearrangement** that inserts the guanine C8 carbon between the ribose C2' and C3', building the first two pterin ring carbons. The product cPMP is subsequently elaborated to molybdopterin and then to Moco, the cofactor required by molybdoenzymes.

> **Identity verification:** The gene symbol, EC number, protein description, radical-SAM/MoaA family assignment, and the InterPro domain set provided (Aldolase_TIM IPR013785; Elp3/MiaA/NifB-like rSAM IPR006638; MoaA IPR013483; MoaA-like IPR040064; MoaA_NifB_PqqE_Fe-S-bd_CS IPR000385) are **fully consistent** with the extensively characterized bacterial MoaA enzyme. The mechanistic and structural literature below derives from orthologs (*Staphylococcus aureus*, *E. coli*, *Thermus thermophilus*, human MOCS1A), which are highly conserved with the *P. putida* protein. No conflicting gene-symbol ambiguity was found.

---

## 2. Primary Function — Reaction and Substrate Specificity

**Reaction (EC 4.1.99.22, GTP 3',8-cyclase):**
GTP + 2 reduced [Fe–S] equivalents + SAM → 3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate + 5'-deoxyadenosine + L-methionine (+ downstream conversion to cPMP by MoaC).

- **Substrate specificity:** The physiological substrate is **5'-GTP**. A defined in vitro system with purified MoaA + MoaC generates precursor Z and directly identified 5'-GTP as the substrate (Hänzelmann & Schindelin 2004, PMID 15317939). Biochemical mutagenesis and the MoaA·5'-GTP co-crystal structure identified the residues conferring nucleotide (guanine) specificity; the enzyme reads the guanine base through **N1 and N2 contacts to the unique iron of the C-terminal [4Fe-4S] cluster**, and the triphosphate is tightly anchored (Hänzelmann & Schindelin 2006, PMID 16632608).
- **Chemistry:** The transformation is a **radical-initiated intramolecular rearrangement of the guanine C8 atom** — a rare enzymatic C–C bond formation that reorganizes the purine/ribose skeleton into the pyranopterin precursor. MoaA is a founding, prototypical member of the radical SAM superfamily used to study C–C bond–forming radical chemistry in cofactor biosynthesis (Pang & Yokoyama 2018, PMID 30097104; Yokoyama 2017, PMID 29072833). Recent work has dissected how radical initiation is controlled to avoid unwanted side reactions (Pang et al. 2025, PMID 41183211).
- **Division of labor with MoaC:** MoaA performs the radical cyclization; the accessory protein **MoaC** releases pyrophosphate and forms the cyclic phosphate, completing cPMP (Kanaujia et al. 2010, PMID 20606263; Hänzelmann & Schindelin 2006, PMID 16632608).

---

## 3. Structural and Cofactor Basis of Function

MoaA functions as a **homodimer**; each subunit is built on an **incomplete (β/α) TIM-barrel** (Aldolase_TIM fold, IPR013785) and carries **two distinct [4Fe-4S] clusters** ~17 Å apart, flanking a large active-site pocket (Hänzelmann & Schindelin 2004, PMID 15317939):

1. **N-terminal [4Fe-4S] cluster** — the canonical radical-SAM cluster ligated by the conserved **CX₃CX₂C** motif (captured by InterPro IPR000385 / IPR006638). SAM binds this cluster's unique iron as an **N/O chelate** (the "fourth ligand"), and reductive cleavage generates the **5'-deoxyadenosyl radical (5'-dA•)** that abstracts a hydrogen to initiate catalysis.
2. **C-terminal [4Fe-4S] cluster** — **unique to MoaA proteins**, has a **non-cysteinyl unique Fe** that directly binds **5'-GTP** via guanine N1/N2, positioning and activating the substrate while the anchored triphosphate prevents escape of radical intermediates (Hänzelmann & Schindelin 2006, PMID 16632608).

This bipartite two-cluster architecture is the structural explanation for catalysis: **cluster I makes the radical from SAM; cluster II binds/activates the GTP substrate.** Both clusters and the product (precursor Z) are **oxygen-sensitive**, consistent with an anaerobically/reductively operating radical enzyme (PMID 16632608).

**Sequence-level confirmation for the *P. putida* protein (this work).** Direct inspection of the Q88E69 sequence (334 aa) shows both signature motifs are present and conserved:
- **N-terminal radical-SAM cluster:** the canonical **CX₃CX₂C** motif at **Cys27–Cys31–Cys34** (…C27-D-F-R-C31-V-Y-C34…), matching the SAM-cleaving [4Fe-4S] cluster fingerprint (IPR000385).
- **C-terminal MoaA-unique cluster:** three cysteine ligands at **Cys260, Cys263, Cys277**, positionally near-identical to the experimentally validated *E. coli*/*S. aureus* MoaA C-terminal cluster ligands.

The preservation of both cysteine constellations demonstrates that the *P. putida* enzyme retains the full catalytic machinery, so the mechanistic and structural conclusions drawn from orthologs transfer directly to Q88E69.

---

## 4. Subcellular Localization

MoaA is a **soluble cytoplasmic enzyme**. Moco biosynthesis as a whole is a conserved cytoplasmic pathway (Leimkühler 2017, PMID 28284029), and MoaA has no signal peptide or membrane-spanning region; its oxygen-sensitive Fe–S clusters require the reducing intracellular environment. It carries out its function within the cytosol upstream of membrane-associated or periplasmic molybdoenzymes that ultimately receive the mature cofactor.

---

## 5. Pathway Context and Biological Role

MoaA catalyzes **step 1** of the highly conserved, multistep Moco pathway (Leimkühler 2017, PMID 28284029):

1. **GTP → cyclic pyranopterin monophosphate (cPMP)** — **MoaA + MoaC** *(this enzyme)*
2. cPMP → molybdopterin (MPT) — MoaD/MoaE (MPT synthase), sulfur delivered via MoeB
3. Mo insertion into MPT → Mo-MPT (Moco) — MogA/MoeA (Mo-insertase)
4. *(Bacteria/archaea only)* dinucleotide modification of Moco — attachment of GMP/CMP to form the MGD/MCD variants

In *P. putida* KT2440, the resulting Moco is the essential catalytic cofactor of **molybdoenzymes** (e.g., nitrate reductases, xanthine dehydrogenase/oxidase, and other pyranopterin-dependent oxidoreductases used in respiratory/redox metabolism). KT2440 is a **Moco-competent host** — it is used as a cell factory to produce heterologous molybdoenzymes such as xanthine oxidase, whose activity depends on correct molybdenum/Moco loading (Guo et al. 2026, PMID 41933999) — evidence that its endogenous Moco biosynthetic pathway (initiated by MoaA/PP_4597) is functional in vivo. Because MoaA sits at the pathway's entry point, its activity is **rate-defining for the supply of all Moco-dependent enzymes**; loss of the orthologous first step causes **molybdenum cofactor deficiency type A** in humans (via MOCS1A), underscoring the conserved, non-redundant importance of this reaction (Hänzelmann & Schindelin 2004, PMID 15317939; Johannes et al. 2022, PMID 36296488). The pathway also intersects with **Fe–S cluster assembly** and **tRNA thiolation** machinery, and several Moco proteins moonlight in related processes (Leimkühler 2017, PMID 28284029) — though MoaA's own, precise role is the single radical cyclization described above.

---

## 6. Evidence Summary

| Claim | Type of evidence | Key references |
|---|---|---|
| Substrate is 5'-GTP; product feeds precursor Z/cPMP | Direct biochemistry (defined in vitro reconstitution) | PMID 15317939 |
| Radical-initiated C8 intramolecular rearrangement | Mechanistic/structural | PMID 16632608, 30097104 |
| Two [4Fe-4S] clusters (N-term SAM cleavage; C-term GTP binding) | X-ray crystallography (apo, +SAM, +GTP) | PMID 15317939, 16632608 |
| MoaA + MoaC division of labor | Structural + enzymology | PMID 20606263, 16632608 |
| Cytoplasmic, conserved multistep Moco pathway | Authoritative review | PMID 28284029 |
| Founding radical-SAM C–C bond–forming paradigm; controlled radical initiation | Review + recent mechanism | PMID 30097104, 29072833, 41183211 |
| Physiological importance (deficiency phenotype in ortholog) | Clinical/biochemical | PMID 36296488, 15317939 |
| Both Fe-S cluster motifs conserved in *P. putida* sequence (Cys27/31/34; Cys260/263/277) | Sequence/bioinformatic analysis (this work, UniProt Q88E69) | — |

---

## 7. Supported vs. Refuted Hypotheses

- **Supported:** MoaA is a radical-SAM GTP 3',8-cyclase; substrate = 5'-GTP; two [4Fe-4S] clusters with distinct roles; cytoplasmic localization; first step of Moco biosynthesis working with MoaC.
- **Refuted / ruled out:** MoaA is **not** the enzyme that forms the cyclic phosphate or releases pyrophosphate (that is MoaC); it is **not** a transporter, structural protein, or signaling molecule; the gene symbol was **not** ambiguous with an unrelated gene.

## 8. Limitations and Future Directions

- All mechanistic/structural data derive from **orthologs**, not the *P. putida* KT2440 protein directly; however, MoaA family conservation (HAMAP MF_01225) makes transfer of annotation robust. A KT2440-specific crystal structure or enzymatic assay would confirm kinetic parameters.
- The exact **genomic organization/regulation of PP_4597** (operon context, co-transcription with *moaC/moaB/moaE*, molybdate/anaerobiosis regulation) in KT2440 was not resolved from the retrieved literature and would refine the physiological picture.
- Which specific *P. putida* molybdoenzymes depend most on MoaA-derived Moco (nitrate reductase vs. others) could be established by targeted knockout phenotyping.


## Artifacts

- [OpenScientist final report](moaA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moaA-deep-research-openscientist_artifacts/final_report.pdf)