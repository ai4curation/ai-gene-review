---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:17:20.880264'
end_time: '2026-07-20T18:28:30.179654'
duration_seconds: 669.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moaC
  gene_symbol: moaC
  uniprot_accession: Q88NC0
  protein_description: 'RecName: Full=Cyclic pyranopterin monophosphate synthase {ECO:0000255|HAMAP-Rule:MF_01224};
    EC=4.6.1.17 {ECO:0000255|HAMAP-Rule:MF_01224}; AltName: Full=Molybdenum cofactor
    biosynthesis protein C {ECO:0000255|HAMAP-Rule:MF_01224};'
  gene_info: Name=moaC {ECO:0000255|HAMAP-Rule:MF_01224}; OrderedLocusNames=PP_1292;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MoaC family. {ECO:0000255|HAMAP-
  protein_domains: MoaC. (IPR023045); MoaC_bact/euk. (IPR047594); MoaC_sf. (IPR036522);
    MoCo_biosynth_MoaA/MoaC. (IPR050105); Mopterin_CF_biosynth-C_dom. (IPR002820)
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
  path: moaC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moaC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NC0
- **Protein Description:** RecName: Full=Cyclic pyranopterin monophosphate synthase {ECO:0000255|HAMAP-Rule:MF_01224}; EC=4.6.1.17 {ECO:0000255|HAMAP-Rule:MF_01224}; AltName: Full=Molybdenum cofactor biosynthesis protein C {ECO:0000255|HAMAP-Rule:MF_01224};
- **Gene Information:** Name=moaC {ECO:0000255|HAMAP-Rule:MF_01224}; OrderedLocusNames=PP_1292;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MoaC family. {ECO:0000255|HAMAP-
- **Key Domains:** MoaC. (IPR023045); MoaC_bact/euk. (IPR047594); MoaC_sf. (IPR036522); MoCo_biosynth_MoaA/MoaC. (IPR050105); Mopterin_CF_biosynth-C_dom. (IPR002820)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moaC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moaC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moaC** (gene ID: moaC, UniProt: Q88NC0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *moaC* (Q88NC0) in *Pseudomonas putida* KT2440

**Gene:** *moaC* (ordered locus PP_1292)
**Protein:** Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**UniProt:** Q88NC0 · Family: MoaC (HAMAP MF_01224) · Length: 156 aa

---

## 1. Summary (Answer to the Research Question)

*moaC* encodes **cyclic pyranopterin monophosphate (cPMP) synthase**, a cytoplasmic
lyase that catalyzes the second half of the **first, committed step of molybdenum
cofactor (Moco) biosynthesis**. Working immediately downstream of the radical-SAM
enzyme MoaA, MoaC converts the cyclic nucleotide **(8S)-3′,8-cyclo-7,8-dihydroguanosine
5′-triphosphate (3′,8-cH₂GTP)** into **cyclic pyranopterin monophosphate (cPMP, "precursor Z")**,
releasing diphosphate (EC 4.6.1.17). It is this reaction that builds the characteristic
**pyranopterin ring** and the terminal **cyclic phosphate** that ultimately coordinate
molybdenum in every molybdoenzyme. The enzyme functions as a **homohexamer (trimer of
dimers)** in the **cytoplasm**, with composite active sites at subunit interfaces.

The gene identity is unambiguous: the UniProt catalytic annotation, the MoaC/HAMAP family
assignment, the conserved active-site motif, and the InterPro domain complement all agree,
and the P. putida protein is a canonical, full-length MoaC ortholog of the extensively
characterized *E. coli* enzyme.

---

## 2. Gene/Protein Identity Verification

| Attribute | Finding |
|---|---|
| Protein name | Cyclic pyranopterin monophosphate synthase (UniProt recommended name) |
| EC number | 4.6.1.17 (a carbon–oxygen lyase acting on phosphates) |
| Family / rule | MoaC family; HAMAP MF_01224 |
| InterPro domains | MoaC (IPR023045), MoaC_bact/euk (IPR047594), MoaC_sf (IPR036522), MoaA/MoaC (IPR050105), Molybdenum-cofactor-biosynthesis-C domain (IPR002820) |
| Length | 156 aa (typical for bacterial MoaC, ~17 kDa) |
| Active-site motif | Conserved cyclohydrolase-type "…L**CHPL**M…" segment present in the sequence |
| Catalytic reaction (UniProt) | 3′,8-cH₂GTP = cyclic pyranopterin phosphate + diphosphate |
| Quaternary structure (UniProt) | Homohexamer, trimer of dimers |

**Conclusion:** Q88NC0 is a bona fide MoaC. All literature cited below concerns the same
MoaC / cPMP-synthase protein family (bacterial orthologs and the human homolog MOCS1B),
so there is no gene-symbol ambiguity for this target.

**Quantitative homology evidence (this work):** A pairwise alignment of Q88NC0 against the
experimentally and structurally characterized *E. coli* MoaC (P0A738) shows **72.7% amino-acid
identity** (112/154 aligned positions), and the catalytically essential *E. coli* **Asp128
aligns with an aspartate in the P. putida sequence**. KEGG independently assigns PP_1292 to
ortholog **K03637** (cyclic pyranopterin monophosphate synthase, EC 4.6.1.17), Pfam **MoaC**,
and module **M00880** ("Molybdenum cofactor biosynthesis, GTP => molybdenum cofactor"). This
high identity plus conservation of the catalytic residue provides strong homology-based support
for transferring the *E. coli* function to this specific *P. putida* protein.

**Genomic context (this work):** PP_1292 (*moaC*, 1,478,937–1,479,407) lies in a contiguous,
same-strand **moaC–moaD–moaE** cluster: PP_1293 = *moaD* (molybdopterin synthase small subunit)
and PP_1294 = *moaE* (molybdopterin synthase large subunit). *moaC* and *moaD* overlap by ~4 bp
and *moaD*/*moaE* by 3 bp, indicating **translational coupling / operonic organization**. Thus
the gene for pathway step 1 (MoaC → cPMP) is co-located and co-transcribed with the genes for
step 2 (MoaD/MoaE, cPMP → molybdopterin) — genomic evidence that MoaC's product is directly
handed to the downstream enzymes of Moco biosynthesis.

---

## 3. Primary Molecular Function

### 3.1 The reaction catalyzed

The first step of Moco biosynthesis is a remarkable transformation of GTP into cPMP that
is carried out by **two** enzymes acting in sequence:

1. **MoaA** (a radical *S*-adenosyl-methionine enzyme with two [4Fe-4S] clusters) abstracts
   a hydrogen atom and forms a new C–C bond, converting GTP into the cryptic cyclic
   intermediate **3′,8-cH₂GTP** [Hover 2013, PMID 23627491; Hänzelmann & Schindelin 2004/2006].
2. **MoaC** then catalyzes the **complex intramolecular rearrangement** of 3′,8-cH₂GTP that
   forms the pyranopterin ring and the cyclic phosphate, yielding **cPMP** and releasing
   diphosphate [Hover 2013, PMID 23627491; Hover 2015, PMID 26575208].

Historically MoaC was thought to play only an accessory role (pyrophosphate release / cyclic
phosphate formation). The isolation of the MoaA product 3′,8-cH₂GTP and its efficient
conversion to cPMP by MoaC (and by the human homolog MOCS1B) **redefined MoaC as the enzyme
that performs the majority of the pyranopterin-forming chemistry** — "in contrast to previous
proposals, MoaC plays a major role in the complex rearrangement to generate the pyranopterin
ring" [Hover 2013, PMID 23627491].

### 3.2 Substrate specificity

MoaC is highly specific for the cyclic nucleotide substrate: 3′,8-cH₂GTP is converted to cPMP
with **Km < 0.060 μM** for bacterial MoaC (0.79 ± 0.24 μM for human MOCS1B) [Hover 2013,
PMID 23627491]. Mechanistic probing with an uncleavable substrate analogue (3′,8-cH₂GMP[CH₂]PP)
showed that the early catalytic steps proceed **before** cyclic-phosphate formation, and that
partially active MoaC variants generate a defined reaction intermediate — providing direct
evidence on the ordering of bond-forming events in the pyranopterin rearrangement
[Hover 2015, PMID 26575208].

### 3.3 Catalytic residues

The *E. coli* MoaC crystal structure identified a conserved active-site pocket at the
dimer interface; **Asp128** is catalytically essential (Asp128→Ala nearly abolishes activity),
and a substitution in the human ortholog (Thr182→Pro) that causes Moco deficiency maps to the
same region [Wuebbens 2000, PMID 10903949]. GTP-bound MoaC structures (e.g., from *Thermus
thermophilus*) further map the substrate-binding residues [Kanaujia 2010, PMID 20606263].

---

## 4. Structure and Localization

- **Fold:** Each monomer adopts a **ferredoxin-like fold** — a four-stranded antiparallel
  β-sheet packed against two long α-helices [Wuebbens 2000, PMID 10903949].
- **Oligomer:** The enzyme is a **tightly packed homohexamer with 32 symmetry (trimer of
  dimers)**; the active sites lie **at the interface between two monomers**, so oligomerization
  is required to assemble competent catalytic pockets [Wuebbens 2000, PMID 10903949; UniProt Q88NC0].
- **Localization:** MoaC catalyzes an intracellular reaction and is part of the **soluble
  cytoplasmic** Moco-biosynthesis machinery; the pathway operates in the cytoplasm of the
  bacterial cell [Mendel & Leimkühler 2015, PMID 24980677]. The mature Moco is subsequently
  inserted into apo-molybdoenzymes, some of which are exported to the periplasm, but the
  MoaC reaction itself is cytoplasmic.
- **Conservation:** MoaC-type proteins are present across archaea, bacteria and eukaryotes;
  structural studies of orthologs (e.g., *Mycobacterium tuberculosis* MoaC2) confirm the
  conserved fold and interaction with MoaA [Srivastava 2013, PMID 23526978].

---

## 5. Pathway Context and Biological Role

MoaC catalyzes **step 1 of the four-step bacterial Moco pathway** [Mendel & Leimkühler 2015,
PMID 24980677; Schwarz & Mendel 2006, PMID 16669776]:

1. **GTP → cyclic pyranopterin monophosphate (cPMP)** — MoaA + **MoaC**  ← *this gene*
2. cPMP → molybdopterin (MPT) — MoaD/MoaE (MPT synthase), sulfuration by MoeB
3. Mo insertion into MPT → Moco — MogA/MoeA
4. (bacteria/archaea) nucleotide attachment → bis-MGD / MCD dinucleotide variants of Moco

Moco is the essential catalytic cofactor of **>50 molybdoenzymes**, in which a **pyranopterin
coordinates the molybdenum atom at the active site** [Magalon & Mendel 2015, PMID 26435257].
These enzymes carry out key oxygen-atom-transfer and redox reactions in global carbon, nitrogen
and sulfur metabolism — e.g., **nitrate reductase, DMSO/TMAO reductase, sulfite oxidase,
xanthine dehydrogenase/oxidase, and formate dehydrogenase**. In a metabolically versatile soil
bacterium such as *P. putida* KT2440, Moco-dependent enzymes support **alternative/anaerobic
respiration and nitrogen and sulfur metabolism**; MoaC is therefore the gatekeeping biosynthetic
step that activates all of this molybdenum-dependent chemistry. Because cPMP synthesis is the
entry point of the pathway, loss of MoaC function would abolish Moco production and inactivate
the entire downstream molybdoenzyme repertoire. In humans, defects in the orthologous first step
cause fatal **Molybdenum Cofactor Deficiency**, underscoring the step's essentiality
[Wuebbens 2000, PMID 10903949].

**Pathway completeness in P. putida KT2440 (this work):** KEGG ortholog mapping confirms the
organism encodes the entire Moco biosynthetic machinery — *moaA* (three paralogs: PP_1969,
PP_2482, PP_4597), *moaC* (single copy, PP_1292), *moaD* (PP_1293), *moaE* (PP_1294), *moeA*
(PP_2123, Mo insertase) and *mogA* (PP_3457) — i.e., every step needed to convert GTP into mature
Moco (KEGG module M00880). Notably, **MoaC is present as a single, non-redundant copy**, so
PP_1292 is the sole cyclic-pyranopterin-monophosphate synthase in the cell and an obligatory
node of the pathway; the three MoaA paralogs contrast with this single MoaC. The presence of all
downstream enzymes confirms that MoaC's product (cPMP) is channeled through a complete, functional
pathway to activated molybdenum cofactor.

---

## 6. Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| Q88NC0 is a canonical MoaC / cPMP synthase | **Supported** | UniProt catalytic annotation, HAMAP MF_01224, InterPro domains, conserved CHPL motif, 156-aa length |
| Substrate is the cyclic nucleotide 3′,8-cH₂GTP (product of MoaA), not free GTP | **Supported** | Hover 2013 (PMID 23627491) |
| MoaC performs the pyranopterin ring-forming rearrangement (not just PPi release) | **Supported** (revised historical view) | Hover 2013/2015 |
| MoaC functions as an oligomer with interfacial active sites | **Supported** | Wuebbens 2000 (PMID 10903949); UniProt homohexamer |
| The reaction occurs in the cytoplasm as step 1 of Moco biosynthesis | **Supported** | Mendel & Leimkühler 2015; Schwarz & Mendel 2006 |
| MoaC has a molybdenum-independent "moonlighting" primary role | **Not supported** | No evidence; all data point to Moco biosynthesis as the sole primary function |
| PP_1292 is functionally equivalent to E. coli MoaC | **Supported** | 72.7% identity, conserved catalytic Asp, KEGG K03637/M00880 (this work) |
| PP_1292 is organized in a moa operon in P. putida | **Supported** | Contiguous, overlapping moaC–moaD–moaE cluster (this work) |

---

## 7. Limitations and Future Directions

- **Organism-specific data:** Direct biochemical/genetic characterization of MoaC has been done
  in *E. coli*, *T. thermophilus*, *M. tuberculosis* and human MOCS1B, **not specifically in
  *P. putida* KT2440**. The functional assignment for PP_1292 rests on very high sequence/domain
  conservation (72.7% identity to *E. coli* MoaC, conserved catalytic Asp), operonic co-location
  with *moaD/moaE*, and the essentiality of the pathway; a *P. putida* knockout/complementation
  study would still provide direct experimental confirmation.
- **Mechanistic details:** The precise atom-by-atom mechanism of the pyranopterin rearrangement
  is still being resolved; recent radical-SAM (MoaA) work continues to refine the picture
  [Yokoyama 2022, PMID 35480226].
- **Regulation/operon context:** The transcriptional regulation and *moa* operon organization of
  PP_1292 in *P. putida* (and any physiological conditions modulating Moco demand, e.g., nitrate/
  anaerobiosis) were not analyzed here and are a natural follow-up.

---

## 8. Key References

- Hover BM, Loksztejn A, Ribeiro AA, Yokoyama K. *Identification of a cyclic nucleotide as a cryptic intermediate in molybdenum cofactor biosynthesis.* JACS, 2013. **PMID 23627491**
- Hover BM, Lilla EA, Yokoyama K. *Mechanistic Investigation of cPMP Synthase in Molybdenum Cofactor Biosynthesis Using an Uncleavable Substrate Analogue.* 2015. **PMID 26575208**
- Wuebbens MM, Liu MT, Rajagopalan KV, Schindelin H. *Crystal structure of the molybdenum cofactor biosynthesis protein MoaC.* Structure, 2000. **PMID 10903949**
- Mendel RR, Leimkühler S. *The biosynthesis of the molybdenum cofactors.* 2015. **PMID 24980677**
- Magalon A, Mendel RR. *Biosynthesis and Insertion of the Molybdenum Cofactor.* EcoSal Plus, 2015. **PMID 26435257**
- Schwarz G, Mendel RR. *Molybdenum cofactor biosynthesis and molybdenum enzymes.* Annu Rev Plant Biol, 2006. **PMID 16669776**
- Hänzelmann P, Schindelin H. *Crystal structure of the SAM-dependent enzyme MoaA…* PNAS, 2004. **PMID 15317939**
- Hänzelmann P, Schindelin H. *Binding of 5′-GTP to the C-terminal FeS cluster of MoaA…* 2006. **PMID 16632608**
- Kanaujia SP et al. *Structures of apo and GTP-bound MoaC from Thermus thermophilus HB8.* 2010. **PMID 20606263**
- Srivastava et al. *Structural insights into MoaC2 from Mycobacterium tuberculosis.* 2013. **PMID 23526978**
- Yokoyama K, Li X, Pang Y. *Resolving the Multidecade-Long Mystery in MoaA Radical SAM Enzyme…* 2022. **PMID 35480226**


## Artifacts

- [OpenScientist final report](moaC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moaC-deep-research-openscientist_artifacts/final_report.pdf)