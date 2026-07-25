---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T14:02:36.034174'
end_time: '2026-07-17T14:22:26.347617'
duration_seconds: 1190.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapC
  gene_symbol: dapC
  uniprot_accession: Q88MI3
  protein_description: 'SubName: Full=N-succinyl-L,L-diaminopimelate aminotransferase
    alternative {ECO:0000313|EMBL:AAN67209.1}; EC=2.6.1.17 {ECO:0000313|EMBL:AAN67209.1};'
  gene_info: Name=dapC {ECO:0000313|EMBL:AAN67209.1}; OrderedLocusNames=PP_1588 {ECO:0000313|EMBL:AAN67209.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Aminotransferase_I/II_large. (IPR004839); DapC_beta/gammaproteobac.
    (IPR019878); LL-DAP_aminotransferase. (IPR050881); PyrdxlP-dep_Trfase. (IPR015424);
    PyrdxlP-dep_Trfase_major. (IPR015421)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dapC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MI3
- **Protein Description:** SubName: Full=N-succinyl-L,L-diaminopimelate aminotransferase alternative {ECO:0000313|EMBL:AAN67209.1}; EC=2.6.1.17 {ECO:0000313|EMBL:AAN67209.1};
- **Gene Information:** Name=dapC {ECO:0000313|EMBL:AAN67209.1}; OrderedLocusNames=PP_1588 {ECO:0000313|EMBL:AAN67209.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aminotransferase_I/II_large. (IPR004839); DapC_beta/gammaproteobac. (IPR019878); LL-DAP_aminotransferase. (IPR050881); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapC** (gene ID: dapC, UniProt: Q88MI3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: dapC (PP_1588 / Q88MI3) in *Pseudomonas putida* KT2440

## Summary

The gene **dapC** (ordered locus **PP_1588**; UniProt **Q88MI3**) of *Pseudomonas putida* strain KT2440 encodes a **pyridoxal 5′-phosphate (PLP)-dependent N-succinyl-L,L-diaminopimelate aminotransferase** (EC 2.6.1.17; KEGG ortholog K14267). It is a 398-amino-acid, fold-type I (class-I) aminotransferase that catalyzes a single, well-defined reaction in the **succinylase branch of the meso-diaminopimelate (DAP) / L-lysine biosynthetic pathway**. Specifically, it transfers an amino group from L-glutamate onto the keto acid **N-succinyl-2-L-amino-6-oxoheptanedioate**, producing **N-succinyl-L,L-2,6-diaminoheptanedioate (N-succinyl-L,L-DAP)** with 2-oxoglutarate as the by-product (KEGG reaction R04475). The identity of the target protein is unambiguous and fully consistent with its UniProt annotation, its domain architecture, its KEGG pathway assignment, and the enzymology established for DapC orthologs in other bacteria.

Biologically, DapC occupies the transamination step that converts a keto intermediate into the L,L-configured diaminopimelate scaffold. The pathway downstream of DapC yields two essential end products: **L-lysine**, required for protein synthesis, and **meso-diaminopimelate (meso-DAP)**, a cross-linking building block of the Gram-negative peptidoglycan cell wall. Because this pathway is absent in humans and essential in most bacteria, its enzymes — including the desuccinylase DapE and the epimerase DapF that flank DapC in the route — are actively pursued as antibacterial drug targets. As a soluble enzyme of intermediary amino-acid metabolism with no signal peptide or transmembrane segment, DapC carries out its function in the **bacterial cytoplasm**, most likely as a **homodimer** with two active sites built at the subunit interface, each anchored by a catalytic Schiff-base lysine (Lys246) and the PLP cofactor.

A distinctive feature emerged from this investigation: whereas *Escherichia coli* lacks a dedicated *dapC* gene and instead relies on a **bifunctional ArgD** (N-acetylornithine aminotransferase) that "moonlights" to perform both the arginine and lysine transamination steps, *P. putida* KT2440 encodes a **separate, dedicated DapC** (PP_1588) that is distinct from its own arginine-pathway ArgD paralog (PP_0372, ~26% sequence identity). This indicates a **division of labor** in *P. putida* between lysine and arginine transamination, and places PP_1588 firmly within the beta/gammaproteobacterial DapC family (InterPro IPR019878).

---

## Key Findings

### Finding 1 — DapC is a PLP-dependent N-succinyl-L,L-diaminopimelate aminotransferase (EC 2.6.1.17)

The primary function of DapC/Q88MI3 is that of a **pyridoxal 5′-phosphate-dependent aminotransferase** acting on N-succinyl-L,L-diaminopimelate. The UniProt entry describes the 398-amino-acid product of gene *dapC* / *PP_1588* as an "N-succinyl-L,L-diaminopimelate aminotransferase" carrying EC number 2.6.1.17, and lists PLP (ChEBI:597326) as the required cofactor. This annotation is corroborated by the domain architecture: Pfam **PF00155** (aminotransferase class I/II) and InterPro **IPR004839** (aminotransferase class I/II large domain), together with the PLP-dependent transferase fold signatures **IPR015421/IPR015422/IPR015424**. The family-level assignments are highly specific — **IPR019878** ("Succinyldiaminopimelate transaminase, DapC, beta/gammaproteobacteria"; NCBIfam TIGR03538) and **IPR050881** (LL-DAP aminotransferase) — and the Gene Ontology terms attached to the protein (GO:0009016 N-succinyldiaminopimelate aminotransferase activity; GO:0030170 PLP binding; GO:0009089 lysine biosynthesis via diaminopimelate) reinforce the assignment.

The enzymology of this reaction has been established experimentally in related organisms. In *E. coli*, the DapATase activity (i.e. the dapC function) was purified and shown to be a **PLP-dependent N-succinyl-L,L-diaminopimelate:α-ketoglutarate aminotransferase** ([PMID: 10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/)), which defines the reaction as a transamination of N-succinyl-L,L-DAP using α-ketoglutarate as the amino acceptor — exactly matching EC 2.6.1.17. In *Corynebacterium glutamicum*, overexpression of the *dapC* gene produced a **9-fold increase in specific aminotransferase activity** ([PMID: 12948639](https://pubmed.ncbi.nlm.nih.gov/12948639/)), directly demonstrating that *dapC* encodes the N-succinyl-aminoketopimelate aminotransferase activity in a bacterium that, like *P. putida*, uses the succinylase branch.

> Supporting quote (PMID 10074354): *"the dapC gene encoding the PLP-dependent N-succinyl-L, L-diaminopimelate:alpha-ketoglutarate aminotransferase (DapATase)"*
>
> Supporting quote (PMID 12948639): *"Overexpression of the dapC gene in C. glutamicum resulted in a 9-fold increase of the specific aminotransferase activity."*

### Finding 2 — DapC catalyzes reaction R04475 as a standalone gene in the succinyl-DAP module

KEGG assigns PP_1588 to ortholog **K14267** (N-succinyldiaminopimelate aminotransferase, EC 2.6.1.17), pathway **ppu00300** (Lysine biosynthesis), and module **M00016** (Lysine biosynthesis, succinyl-DAP pathway, aspartate ⇒ lysine). The precise catalyzed reaction is **R04475**:

> N-succinyl-2-L-amino-6-oxoheptanedioate + L-glutamate ⇌ N-succinyl-L,L-2,6-diaminoheptanedioate (N-succinyl-L,L-DAP) + 2-oxoglutarate

Within the module, DapC sits between **DapD** (K00674; tetrahydrodipicolinate N-succinyltransferase, EC 2.3.1.117, reaction R04365) upstream and **DapE** (K01439; N-succinyl-L,L-DAP desuccinylase, EC 3.5.1.18, reaction R02734), **DapF** (K01778; DAP epimerase) and **LysA** (diaminopimelate decarboxylase) downstream. The gene occupies coordinates complement(1780147..1781343) — 1197 nt / 398 aa — and its immediate chromosomal neighbors are functionally unrelated (PP_1587, an NhaP Na⁺/H⁺ antiporter; PP_1589, *glnD* uridylyltransferase; PP_1590, *map* methionine aminopeptidase). DapC is therefore **not co-transcribed in a canonical *dap* operon**; it is dispersed on the chromosome, as is typical for *dap* genes in many bacteria. KEGG BRITE classifies the protein as a Class I aminotransferase (Pfam Aminotran_1_2, Asp_aminotransf).

### Finding 3 — Placement in the cytoplasmic succinylase branch supplying lysine and meso-DAP

DapC operates in the **succinylase (acyl) branch** of the DAP pathway, one of several variants (succinylase, acetylase, and the DapL aminotransferase bypass) by which bacteria synthesize meso-DAP and lysine from aspartate and pyruvate. The pathway topology has been made explicit by structural work on the DapL bypass enzyme: DapL catalyzes the direct conversion of tetrahydrodipicolinate (THDPA) to L,L-DAP "**in one step bypassing the DapD, DapC and DapE enzymatic reactions present in the acyl DAP pathways**" ([PMID: 21633707](https://pubmed.ncbi.nlm.nih.gov/21633707/)). This unambiguously places DapC between DapD and DapE in the succinylase route.

The end products of the pathway define its biological importance. As summarized in a review of lysine-biosynthesis drug targets, the pathway "**provides lysine for protein synthesis and both lysine and meso-diaminopimelate for construction of the bacterial peptidoglycan cell wall**" ([PMID: 17579770](https://pubmed.ncbi.nlm.nih.gov/17579770/); see also [PMID: 12570844](https://pubmed.ncbi.nlm.nih.gov/12570844/)). Because these enzymes have no human counterpart, they are recognized antibacterial targets ([PMID: 20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/)). DapC's subcellular location is the **cytoplasm**: it is a soluble PLP-dependent transaminase of intermediary metabolism, and the 398-aa sequence contains no signal peptide or transmembrane region.

> Supporting quote (PMID 21633707): *"DapL catalyzes the conversion of tetrahydrodipicolinate (THDPA) to L,L-diaminopimelate (L,L-DAP), in one step bypassing the DapD, DapC and DapE enzymatic reactions present in the acyl DAP pathways"*
>
> Supporting quote (PMID 17579770): *"it provides lysine for protein synthesis and both lysine and meso-diaminopimelate for construction of the bacterial peptidoglycan cell wall"*

### Finding 4 — Conserved fold-type I catalytic machinery (Schiff-base Lys246 and PLP-binding motifs)

Sequence-motif analysis of the 398-aa protein identifies the diagnostic **class-I (fold-type I) aminotransferase catalytic residues**, supporting a canonical PLP Schiff-base transamination mechanism:

| Feature | Motif | Approx. residue(s) | Role |
|---|---|---|---|
| N-terminal substrate/PLP loop | S-I-G-E-P | 34–38 | Glycine-rich loop positioning substrate/PLP |
| Phosphate-binding loop | S-P-G-N-P-T-G | 175–181 | Conserved **GNP** motif anchoring the PLP 5′-phosphate |
| Pyridine-N1 anchor | A-A-**D**-E-C-Y | ~Asp206 | Aspartate H-bonds the PLP pyridine N1 |
| Catalytic Schiff-base lysine | H-S-L-S-**K**-R | **Lys246** | Forms internal aldimine with PLP |

These features match the two-domain (large α/β/α sandwich PLP-binding domain plus small domain) transaminase fold assigned by Pfam PF00155 and InterPro IPR004839/IPR015421. The catalytic lysine (Lys246) forms the internal aldimine (Schiff base) with pyridoxal 5′-phosphate, which is displaced by the incoming amino group of the substrate during catalysis — the hallmark ping-pong bi-bi mechanism of fold-type I aminotransferases. UniProt lists PLP as the cofactor (ChEBI:597326) and annotates GO:0030170 (PLP binding), consistent with this mechanistic model.

### Finding 5 — A dedicated DapC distinct from the arginine-pathway ArgD paralog

A key comparative-genomics result is that *P. putida* KT2440 encodes **two separate, distinctly orthologous transaminases** for the lysine and arginine pathways:

| Gene | Locus | KO | Activity | Pathway |
|---|---|---|---|---|
| **dapC** | PP_1588 | K14267 | N-succinyldiaminopimelate aminotransferase (EC 2.6.1.17) | Lysine (M00016) |
| **argD** | PP_0372 | K00821 | Acetylornithine aminotransferase | Arginine |

A pairwise Needleman–Wunsch alignment of the two proteins (398 aa vs 426 aa) yields only **25.7% identity (116/452 aligned positions)** — they are distant paralogs within the fold-type I PLP-transaminase superfamily. This contrasts sharply with *E. coli*, where a single *argD*-encoded N-acetylornithine aminotransferase performs **both** the arginine and lysine (DapC) transamination steps. As reported for the *E. coli* enzyme, "**This enzyme exhibits both NAcOATase and DapATase activity, with similar specificity constants for N-acetylornithine and N-succinyl-L,L-DAP, suggesting that it can function in both lysine and arginine biosynthesis. This finding may explain why numerous investigations have failed to identify genetically the bacterial dapC locus**" ([PMID: 10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/)). A parallel case exists in *Mycobacterium tuberculosis*, whose ArgD "**also possesses succinyl diaminopimelate aminotransferase activity and can thus carry out the corresponding step in lysine biosynthesis**" ([PMID: 34922100](https://pubmed.ncbi.nlm.nih.gov/34922100/)). The presence of a **distinct DapC** in *P. putida* — a member of the dedicated beta/gammaproteobacterial DapC family (IPR019878) — indicates a genuine division of labor between the two pathways rather than moonlighting.

> Supporting quote (PMID 10074354): *"This enzyme exhibits both NAcOATase and DapATase activity, with similar specificity constants for N-acetylornithine and N-succinyl-L,L-DAP, suggesting that it can function in both lysine and arginine biosynthesis. This finding may explain why numerous investigations have failed to identify genetically the bacterial dapC locus"*

### Finding 6 — High-confidence AlphaFold model; predicted homodimer with shared active sites

The AlphaFold DB model **AF-Q88MI3-F1** covers the full 1–398 sequence with a **very high mean pLDDT of 97.2**, indicating a confidently predicted two-domain class-I aminotransferase fold (a large α/β/α sandwich PLP-binding domain plus a small domain), consistent with Pfam PF00155 / InterPro IPR015421. Related DAP-pathway PLP aminotransferases are **obligate homodimers** in which each of the two active sites is assembled from residues contributed by **both** subunits. The structurally characterized ortholog DapL from *Chlamydomonas reinhardtii* is dimeric, and "**the active site comprises residues from both monomers in the dimer**" ([PMID: 21633707](https://pubmed.ncbi.nlm.nih.gov/21633707/)). By homology, DapC/PP_1588 is expected to function as a homodimer, positioning the catalytic Lys246 and the PLP cofactor at the subunit interface.

> Supporting quote (PMID 21633707): *"The active site comprises residues from both monomers in the dimer"*

### Finding 7 — The complete succinylase DAP branch is intact in *P. putida*

KEGG ortholog mapping confirms that **every step of the succinylase branch is encoded** in *P. putida* KT2440:

| Step | Gene | KO | Locus (PP_) |
|---|---|---|---|
| Dihydrodipicolinate synthase | dapA | K01714 | 1237, 2036, 2639 |
| Dihydrodipicolinate reductase | dapB | K00215 | 4725 |
| THDP N-succinyltransferase | dapD | K00674 | 1530 |
| **N-succinyl-DAP aminotransferase** | **dapC** | **K14267** | **1588** |
| N-succinyl-DAP desuccinylase | dapE | K01439 | 1525 |
| DAP epimerase | dapF | K01778 | 3790, 5228 |
| DAP decarboxylase | lysA | K01586 | 2077, 5227 |

This confirms that the **DapD → DapC → DapE succinylase route is the operative pathway** and that DapC (PP_1588) is the sole K14267-type succinyl-DAP aminotransferase in the genome. A KEGG K10206 (LL-DAP aminotransferase / DapL bypass, EC 2.6.1.83) assignment exists for PP_3786, but that gene is annotated as *aspC* / aminotransferase, indicating the assignment is ambiguous and likely reflects a broad-specificity aspartate aminotransferase rather than a validated DapL bypass enzyme. The separate *argD* (K00821, PP_0372) handles arginine transamination.

---

## Mechanistic Model / Interpretation

DapC catalyzes the transamination step of L-lysine biosynthesis in the succinylase branch of the DAP pathway. The following diagram places DapC in its metabolic context:

```
 L-aspartate
     │  (aspartokinase, ASA dehydrogenase)
     ▼
 L-aspartate-4-semialdehyde  +  pyruvate
     │  DapA (K01714)  → dihydrodipicolinate (DHDP)
     ▼
 DapB (K00215)  → tetrahydrodipicolinate (THDPA)
     │
     │  DapD (K00674, EC 2.3.1.117)  + succinyl-CoA
     ▼
 N-succinyl-2-L-amino-6-oxoheptanedioate   (keto acid)
     │
     │  ┌─────────────────────────────────────────────────┐
     │  │  DapC  (PP_1588, K14267, EC 2.6.1.17)            │
     │  │  Reaction R04475 — PLP-dependent transamination │
     │  │  keto acid + L-glutamate                        │
     │  │      ⇌ N-succinyl-L,L-DAP + 2-oxoglutarate      │
     │  └─────────────────────────────────────────────────┘
     ▼
 N-succinyl-L,L-2,6-diaminoheptanedioate  (N-succinyl-L,L-DAP)
     │  DapE (K01439, EC 3.5.1.18)  − succinate
     ▼
 L,L-diaminopimelate (L,L-DAP)
     │  DapF (K01778)  epimerization
     ▼
 meso-DAP ──────────────► peptidoglycan cross-linking (cell wall)
     │  LysA (K01586)  − CO2
     ▼
 L-lysine ──────────────► protein synthesis
```

**Reaction chemistry.** DapC uses the ping-pong bi-bi mechanism characteristic of fold-type I aminotransferases. In the resting enzyme, the ε-amino group of Lys246 forms an internal aldimine (Schiff base) with the PLP cofactor. The amino donor, **L-glutamate**, displaces Lys246 to form an external aldimine; a 1,3-prototropic shift produces a ketimine, which is hydrolyzed to release **2-oxoglutarate** and leave the cofactor as pyridoxamine 5′-phosphate (PMP). In the second half-reaction, the keto substrate **N-succinyl-2-amino-6-oxoheptanedioate** accepts the amino group from PMP, regenerating PLP and releasing the transamination product **N-succinyl-L,L-DAP**. The succinyl group on the distal amino group is critical: it is installed by DapD to render the intermediate a good substrate for the aminotransferase and desuccinylase, and is later removed by DapE. The acyl-group specificity that commits intermediates to the succinylase (rather than acetylase) branch is set at the DapD step, where at least three active-site residues distinguish succinyl- from acetyl-CoA usage ([PMID: 11910040](https://pubmed.ncbi.nlm.nih.gov/11910040/)).

**Quaternary structure and localization.** The very high-confidence AlphaFold model, together with the known dimeric architecture of DAP-pathway PLP aminotransferases, supports a **homodimeric** enzyme with two interfacial active sites. The enzyme functions in the **cytoplasm** — it lacks any secretion or membrane-anchoring signal, consistent with its role in soluble intermediary metabolism.

**Evolutionary interpretation.** The most interesting mechanistic insight is the contrast between *P. putida* and *E. coli*. The DAP transamination step can be filled either by a **dedicated DapC** (as in *P. putida*, *C. glutamicum*, and other beta/gammaproteobacteria carrying the IPR019878 family enzyme) or by a **bifunctional ArgD** that moonlights across the arginine and lysine pathways (as in *E. coli* and *M. tuberculosis*). The genetic "invisibility" of *dapC* in *E. coli* — long puzzling to researchers — is explained by ArgD's dual activity. *P. putida*'s possession of a separate DapC (only ~26% identical to its ArgD) shows it has resolved this ambiguity into two specialized enzymes, likely allowing independent regulation of lysine and arginine biosynthesis.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [10074354](https://pubmed.ncbi.nlm.nih.gov/10074354/) | *The dual biosynthetic capability of N-acetylornithine aminotransferase in arginine and lysine biosynthesis* | Defines the DapC reaction as PLP-dependent transamination of N-succinyl-L,L-DAP with α-ketoglutarate (Finding 1); documents *E. coli* ArgD bifunctionality and the "missing dapC locus," providing the direct contrast for the dedicated *P. putida* DapC (Finding 5). |
| [12948639](https://pubmed.ncbi.nlm.nih.gov/12948639/) | *Identification of dapC and dapF in the succinylase branch of C. glutamicum* | Experimental demonstration that *dapC* overexpression raises aminotransferase activity 9-fold, confirming gene→activity assignment (Finding 1). |
| [21633707](https://pubmed.ncbi.nlm.nih.gov/21633707/) | *L,L-diaminopimelate aminotransferase from C. reinhardtii: a target for algaecide development* | Places DapC between DapD and DapE in the acyl pathway (Finding 3); establishes that DAP-pathway PLP aminotransferases are homodimers with interfacial active sites (Finding 6). |
| [17579770](https://pubmed.ncbi.nlm.nih.gov/17579770/) | *Inhibition of lysine biosynthesis: an evolving antibiotic strategy* | Establishes downstream products (lysine, meso-DAP) and their roles in protein synthesis and peptidoglycan (Finding 3). |
| [12570844](https://pubmed.ncbi.nlm.nih.gov/12570844/) | *Inhibitors of lysine biosynthesis as antibacterial agents* | Reinforces pathway end-products and drug-target relevance (Finding 3). |
| [20138056](https://pubmed.ncbi.nlm.nih.gov/20138056/) | *Structural basis for catalysis by DapE* | Confirms the DapE step immediately downstream and the pathway's antibacterial-target status (Finding 3). |
| [34922100](https://pubmed.ncbi.nlm.nih.gov/34922100/) | *ArgD of M. tuberculosis is a functional N-acetylornithine aminotransferase* | Second example of ArgD moonlighting with succinyl-DAP aminotransferase activity, supporting the bifunctional-vs-dedicated contrast (Finding 5). |
| [11910040](https://pubmed.ncbi.nlm.nih.gov/11910040/) | *Acyl group specificity at the active site of tetrahydrodipicolinate N-succinyltransferase* | Clarifies how the succinyl group (installed by upstream DapD) commits intermediates to the branch DapC acts in (Mechanistic model). |
| [37459673](https://pubmed.ncbi.nlm.nih.gov/37459673/) | *DapE alternate substrate analog N,N-dimethyl-l,l-SDAP* | Confirms the DapE-catalyzed desuccinylation step (the product of DapC is the substrate of DapE). |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *The revisited genome of P. putida KT2440* | Genomic/annotation context for KT2440 loci and functional re-annotation (Findings 2, 7). |

**Consistency of the identification.** Every line of evidence — UniProt annotation, Pfam/InterPro domain architecture, KEGG ortholog and reaction assignment, gene-neighborhood analysis, sequence-motif catalytic residues, AlphaFold structure, and orthologous enzymology in *E. coli* and *C. glutamicum* — converges on the same conclusion. There is **no ambiguity** in this case: the gene symbol *dapC*, the organism (*P. putida* KT2440), the domain complement, and the literature are mutually consistent. The only annotation caveat concerns the unrelated PP_3786/K10206 (DapL-type) assignment, which is a broad-specificity aspartate aminotransferase rather than a bona fide DapL and does not affect the DapC assignment.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* enzyme.** The functional assignment for PP_1588 rests on high-confidence bioinformatic inference (domain family IPR019878, KEGG K14267) plus experimental enzymology from **orthologs** (*E. coli*, *C. glutamicum*). Kinetic parameters (Km, kcat) for N-succinyl-L,L-DAP and L-glutamate, and confirmation of substrate specificity, have not been measured for the *P. putida* protein itself.

2. **No experimental structure.** The homodimer and active-site interpretation rely on an AlphaFold model (pLDDT 97.2) and homology to DapL/DapC structures. No crystal or cryo-EM structure of Q88MI3 has been determined, and the catalytic residue numbering (Lys246, Asp206, GNP loop) is inferred from motif analysis rather than an experimental active-site map.

3. **Essentiality not directly tested in KT2440.** While DAP-pathway enzymes are essential in many bacteria, a *dapC* knockout in *P. putida* has not been reported here; the possibility of partial functional redundancy (e.g., a promiscuous aminotransferase compensating in vivo) cannot be fully excluded without a genetic test.

4. **Regulation unknown.** The dispersed gene location (no *dap* operon) suggests independent regulation, but the transcriptional/allosteric control of *dapC* in *P. putida* is uncharacterized.

5. **Amino-donor specificity.** EC 2.6.1.17 nominally uses 2-oxoglutarate/L-glutamate, but whether the *P. putida* enzyme accepts alternative amino donors is untested.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_1588, purify the His-tagged protein, and measure PLP-dependent aminotransferase activity on N-succinyl-L,L-DAP with L-glutamate/2-oxoglutarate. Determine Km, kcat, and pH optimum using a coupled or ninhydrin-based assay analogous to those used for DapE.

2. **Substrate-specificity panel.** Test activity against N-acetyl-L,L-DAP and N-acetylornithine/N-succinylornithine to quantify how specialized DapC is versus the bifunctional ArgD, directly testing the "division of labor" hypothesis.

3. **Genetic essentiality and complementation.** Construct a *dapC* deletion (or CRISPRi knockdown) in KT2440 and test for DAP/lysine auxotrophy; complement with PP_1588 and, separately, with *argD* (PP_0372) to test whether ArgD can substitute in vivo.

4. **Structural determination.** Solve the crystal structure of Q88MI3 (with and without PLP/substrate analogs) to confirm the homodimeric fold, the interfacial active site, and the catalytic Lys246 aldimine — validating the AlphaFold prediction.

5. **Active-site mutagenesis.** Mutate the predicted Lys246 (Schiff base), Asp206 (N1 anchor), and GNP-loop residues to confirm their catalytic roles.

6. **Antibacterial-target exploration (comparative).** Given the pathway's established drug-target status, evaluate whether *P. putida* DapC (a tractable, non-pathogenic model of the beta/gammaproteobacterial DapC family) is a useful surrogate for inhibitor screening relevant to pathogens such as *Klebsiella pneumoniae*.

---

## Conclusion

**dapC (PP_1588 / Q88MI3)** of *Pseudomonas putida* KT2440 is confidently annotated as a **cytoplasmic, PLP-dependent N-succinyl-L,L-diaminopimelate aminotransferase (EC 2.6.1.17; KEGG K14267)** — a fold-type I transaminase with a catalytic Schiff-base Lys246, most likely functioning as a homodimer. It catalyzes reaction **R04475**, the transamination of N-succinyl-2-amino-6-oxopimelate using L-glutamate, within the **succinylase branch of the meso-DAP / L-lysine biosynthetic pathway**, thereby supplying L-lysine for protein synthesis and meso-DAP for peptidoglycan cross-linking. Unlike *E. coli*, which relies on a bifunctional moonlighting ArgD, *P. putida* deploys a **dedicated DapC** distinct from its separate arginine-pathway ArgD paralog (PP_0372), reflecting a division of labor between the two amino-acid biosynthetic pathways.


## Artifacts

- [OpenScientist final report](dapC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10074354
2. PMID:12948639
3. PMID:21633707
4. PMID:17579770
5. PMID:12570844
6. PMID:20138056
7. PMID:34922100
8. PMID:11910040