---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:12:17.618054'
end_time: '2026-07-23T16:30:32.458019'
duration_seconds: 1094.84
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murE
  gene_symbol: murE
  uniprot_accession: Q88N81
  protein_description: 'RecName: Full=UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate
    ligase {ECO:0000255|HAMAP-Rule:MF_00208}; EC=6.3.2.13 {ECO:0000255|HAMAP-Rule:MF_00208};
    AltName: Full=Meso-A2pm-adding enzyme {ECO:0000255|HAMAP-Rule:MF_00208}; AltName:
    Full=Meso-diaminopimelate-adding enzyme {ECO:0000255|HAMAP-Rule:MF_00208}; AltName:
    Full=UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase {ECO:0000255|HAMAP-Rule:MF_00208};
    AltName: Full=UDP-MurNAc-tripeptide synthetase {ECO:0000255|HAMAP-Rule:MF_00208};
    AltName: Full=UDP-N-acetylmuramyl-tripeptide synthetase {ECO:0000255|HAMAP-Rule:MF_00208};'
  gene_info: Name=murE {ECO:0000255|HAMAP-Rule:MF_00208}; OrderedLocusNames=PP_1332;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MurCDEF family. MurE subfamily.
  protein_domains: Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf.
    (IPR036615); Mur_ligase_cen. (IPR013221); Mur_ligase_N. (IPR000713)
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
  path: murE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N81
- **Protein Description:** RecName: Full=UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase {ECO:0000255|HAMAP-Rule:MF_00208}; EC=6.3.2.13 {ECO:0000255|HAMAP-Rule:MF_00208}; AltName: Full=Meso-A2pm-adding enzyme {ECO:0000255|HAMAP-Rule:MF_00208}; AltName: Full=Meso-diaminopimelate-adding enzyme {ECO:0000255|HAMAP-Rule:MF_00208}; AltName: Full=UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase {ECO:0000255|HAMAP-Rule:MF_00208}; AltName: Full=UDP-MurNAc-tripeptide synthetase {ECO:0000255|HAMAP-Rule:MF_00208}; AltName: Full=UDP-N-acetylmuramyl-tripeptide synthetase {ECO:0000255|HAMAP-Rule:MF_00208};
- **Gene Information:** Name=murE {ECO:0000255|HAMAP-Rule:MF_00208}; OrderedLocusNames=PP_1332;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MurCDEF family. MurE subfamily.
- **Key Domains:** Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf. (IPR036615); Mur_ligase_cen. (IPR013221); Mur_ligase_N. (IPR000713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murE** (gene ID: murE, UniProt: Q88N81) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MurE (Q88N81, PP_1332) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

The research target is confirmed to be correctly identified. UniProt **Q88N81** describes **UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase** (EC **6.3.2.13**; gene *murE*; OrderedLocusName **PP_1332**) from *Pseudomonas putida* strain KT2440. The protein belongs to the **MurCDEF family, MurE subfamily**, and carries the diagnostic Mur ligase domains: Mur_ligase_N (IPR000713), Mur_ligase_cen (IPR013221, the central ATP/mononucleotide-binding domain), and Mur_ligase_C (IPR004101). Every piece of the literature consulted matches this identity — the gene symbol *murE*, the EC number, the substrate/product chemistry, the three-domain fold, and the meso-diaminopimelate (m-DAP) substrate are all mutually consistent. There is no gene-symbol ambiguity: *murE* uniformly denotes this ligase across all bacteria.

**Note on organism-specific literature:** No primary studies of the *P. putida* MurE enzyme itself were found. However, MurE is one of the most highly conserved and best-characterized enzymes in bacteriology. Its function is defined by extensive structural and biochemical work in *E. coli*, *Mycobacterium* spp., and *Corynebacterium glutamicum*, and by demonstrated cross-species functional complementation. Because *P. putida* is a Gram-negative γ-proteobacterium with meso-DAP–type peptidoglycan, the mechanistic conclusions below transfer directly and with high confidence.

---

## 1. Summary (Answer to the Research Question)

MurE (Q88N81 / PP_1332) is a **cytoplasmic, ATP-dependent amide ligase** that catalyzes the **fourth step of the cytoplasmic phase of peptidoglycan biosynthesis**: it adds **meso-diaminopimelic acid (meso-DAP)** as the third residue of the peptidoglycan stem peptide, converting **UDP-MurNAc-L-Ala-γ-D-Glu** (UDP-MurNAc-dipeptide) into **UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP** (UDP-MurNAc-tripeptide), with concomitant hydrolysis of ATP to ADP + Pi. It works in the cytoplasm as the third of four sequential Mur ligases (MurC→MurD→**MurE**→MurF), and its product is the obligate substrate for MurF. The reaction is essential for cell-wall assembly and cell viability.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction (EC 6.3.2.13):**

> ATP + UDP-MurNAc-L-Ala-γ-D-Glu + meso-2,6-diaminopimelate → ADP + phosphate + UDP-MurNAc-L-Ala-γ-D-Glu-meso-2,6-diaminopimelate

MurE catalyzes "the addition of meso-diaminopimelic acid to nucleotide precursor UDP-N-acetylmuramoyl-l-alanyl-d-glutamate in the biosynthesis of bacterial cell-wall peptidoglycan" (Gordon et al., 2001; PMID 11124264). The new bond is an amide linkage between the ε-amino group (the *D*-center amino group) of meso-DAP and the γ-carboxylate of the D-Glu residue already present on the nucleotide precursor.

**Substrate specificity.** MurE is the amino-acid-adding ligase that selects a **single free amino acid** to place at position 3 of the stem peptide — it is "the last Mur ligase to incorporate a free amino acid" (Rossini et al., 2023; PMID 36944394). The identity of that residue is a key taxonomic determinant of peptidoglycan chemistry:
- In Gram-negative bacteria (including *Pseudomonas*) and in bacilli/mycobacteria/corynebacteria, MurE is specific for **meso-DAP**.
- In many Gram-positive cocci, the orthologous MurE instead adds **L-lysine**.

The structural determinant that dictates this meso-DAP-vs-L-Lys selection was localized in the E. coli MurE crystal structure (Gordon et al., 2001; PMID 11124264). As a Gram-negative enzyme with UniProt annotation explicitly naming meso-DAP, *P. putida* MurE is a **meso-DAP-specific** ligase, ensuring the DAP-containing stem peptide required for the direct (A1γ) cross-linking chemistry typical of Pseudomonas peptidoglycan. The 1.4 Å *M. thermoresistibile* MurE·ADP·m-DAP complex directly visualized the m-DAP binding pocket and confirmed UDP-MurNAc-L-Ala-D-Glu (UAG) plus free m-DAP as the physiological substrates (Rossini et al., 2023; PMID 36944394).

**Catalytic mechanism.** Like all Mur ligases, MurE uses a two-step, ATP-dependent mechanism: (i) the D-Glu γ-carboxylate is phosphorylated by ATP to form a reactive **acyl-phosphate intermediate** (releasing ADP), and (ii) the meso-DAP amino group performs nucleophilic attack on this intermediate to form the amide bond, releasing inorganic phosphate. Modeling/docking of the substrates supports this acyl-phosphate route, with the substrate carboxylate positioned near the ATP γ-phosphate and the m-DAP amino group oriented for nucleophilic attack (Shanmugam & Natarajan, 2012; PMID 21491188). The active site contains a **carbamylated (CO₂-modified) lysine**, as directly observed in the E. coli structure (Gordon et al., 2001; PMID 11124264), and catalysis has an **absolute requirement for divalent cations (Mg²⁺)** (Munshi et al., 2013; PMID 23555903).

---

## 3. Position in the Biochemical Pathway

MurE catalyzes the fourth committed cytoplasmic step of the de novo peptidoglycan (murein) biosynthetic pathway. The Mur ligases act in strict sequence on UDP-N-acetylmuramic acid (UDP-MurNAc):

| Step | Enzyme | Residue added | Product |
|------|--------|---------------|---------|
| 1 | MurC | L-Ala | UDP-MurNAc-L-Ala |
| 2 | MurD | D-Glu | UDP-MurNAc-L-Ala-γ-D-Glu |
| 3 | **MurE** | **meso-DAP** | **UDP-MurNAc-tripeptide** |
| 4 | MurF | D-Ala-D-Ala | UDP-MurNAc-pentapeptide |

"MurC, MurD, MurE and MurF catalyze the synthesis of the peptidoglycan precursor UDP-N-acetylmuramoyl-L-alanyl-γ-D-glutamyl-meso-diaminopimelyl-D-alanyl-D-alanine by the sequential addition of amino acids onto UDP-N-acetylmuramic acid (UDP-MurNAc)" (Das et al., 2011; PMID 21445265). MurE's product (the UDP-MurNAc-tripeptide) is the obligatory substrate of MurF; the resulting UDP-MurNAc-pentapeptide is then transferred by MraY to the membrane carrier undecaprenyl phosphate (forming lipid I), glycosylated by MurG (lipid II), flipped across the inner membrane, and polymerized by penicillin-binding proteins into the mature sacculus. MurE therefore sits at a **non-redundant, committed node** midway through the linear cytoplasmic assembly line. (A parallel recycling route via murein peptide ligase, Mpl, can regenerate UDP-MurNAc-tripeptide from recovered tripeptide, bypassing MurC–E during cell-wall recycling — Das et al., 2011; PMID 21445265 — but de novo synthesis of the tripeptide is MurE's role.)

---

## 4. Subcellular Localization

MurE functions in the **cytoplasm**. The enzyme is explicitly described as "a cytoplasmic enzyme" (Gordon et al., 2001; PMID 11124264), consistent with its soluble, nucleotide-sugar substrate and its role in the intracellular (cytoplasmic) phase of peptidoglycan precursor synthesis, which precedes the membrane-associated (lipid I/II) and periplasmic (polymerization/cross-linking) phases. In *Pseudomonas* and other rod-shaped bacteria, the cytoplasmic Mur machinery is functionally coupled to the divisome and elongasome that operate at the inner-membrane/septal interface, but the MurE catalytic reaction itself occurs in the cytosol.

---

## 5. Structure–Function and Genetic Organization

**Three-domain architecture.** The E. coli MurE structure "consists of three domains, two of which have a topology reminiscent of the equivalent domain found in the … UDP-N-acetylmuramoyl-L-alanine:D-glutamate-ligase (MurD)" (Gordon et al., 2001; PMID 11124264): an N-terminal domain binding the UDP-MurNAc-peptide, a central Rossmann-like mononucleotide (ATP)-binding domain bearing the P-loop, and a C-terminal domain that contributes to substrate binding and specificity. These three domains map precisely onto the Q88N81 InterPro annotations (Mur_ligase_N, Mur_ligase_cen, Mur_ligase_C), giving strong bioinformatic confirmation of function by homology. Catalysis is accompanied by large **induced-fit domain closure**: binding of UAG and m-DAP triggers "key conformational changes … [and] movements of domains or loop regions" that assemble the productive active site (Rossini et al., 2023; PMID 36944394).

**Genetic context and regulation.** *murE* is a member of the conserved **division and cell-wall (dcw / mra) gene cluster**. In mycobacteria a single promoter drives "co-transcription of mur synthetases along with key cell division genes such as ftsQ and ftsW" (Munshi et al., 2013; PMID 23555903), coupling PG-precursor supply to septation; in *P. putida* KT2440, PP_1332 (*murE*) lies in the analogous *mra/dcw* locus flanked by *murD*, *murF*, *ftsW/ftsI* and *pbp/fts* genes. This organization coordinates MurE expression with the cell-division machinery.

**Essentiality.** MurE activity is essential: *C. glutamicum murE* was isolated by its ability to complement a temperature-sensitive *E. coli murE* mutant, restoring growth (Wijayarathna et al., 2001; PMID 11398928) — demonstrating both the conserved enzymatic role and its indispensability for viability. Because the Mur pathway is bacteria-specific with no human ortholog, MurE is a validated antibacterial drug target (Munshi et al., 2013, PMID 23555903; Hervin et al., 2023, PMID 38138566; Kumar et al., 2023, PMID 37291783).

---

## 6. Supported and Refuted Hypotheses

**Supported:**
- H1: Q88N81/PP_1332 is a meso-DAP-adding Mur ligase (EC 6.3.2.13) — supported by UniProt annotation, InterPro domains, and cross-species biochemistry/structure.
- H2: MurE acts in the cytoplasm as the third amino-acid-adding ligase (MurC→D→E→F) — supported (PMID 11124264, 21445265, 36944394).
- H3: The enzyme is ATP- and Mg²⁺-dependent and uses an acyl-phosphate mechanism — supported (PMID 23555903, 21491188, 11124264).
- H4: As a Gram-negative enzyme, it is meso-DAP-specific rather than L-Lys-specific — strongly supported by taxonomy, UniProt naming, and the identified specificity determinant (PMID 11124264).

**Refuted / not supported:**
- The gene symbol *murE* is **not** ambiguous here; no competing gene of the same symbol was found. The only naming variation is the descriptive substrate (glycyl-D-glutamate in some organisms vs L-alanyl-D-glutamate), which reflects species-specific stem-peptide chemistry, not a different enzyme.

---

## 7. Limitations and Future Directions

- **No direct experimental characterization of the *P. putida* KT2440 MurE** (PP_1332) enzyme (kinetics, structure, knockout phenotype) was located; conclusions rely on strong homology to E. coli/mycobacterial/corynebacterial orthologs and on conserved domain architecture. Direct enzymology (kcat/Km for UAG, m-DAP, ATP) and an experimental *P. putida* structure would confirm the details.
- The precise **specificity residues** governing meso-DAP selection in the *Pseudomonas* enzyme have not been mapped experimentally; they are inferred from the E. coli structural determinant.
- Regulatory coupling (e.g., possible Ser/Thr phosphorylation of Mur ligases seen in Actinobacteria; PMID 23555903) has not been tested in *Pseudomonas*.

---

## References (PMIDs)
- Gordon E. et al. Crystal structure of UDP-N-acetylmuramoyl-L-alanyl-D-glutamate:meso-diaminopimelate ligase from *Escherichia coli*. **PMID 11124264**.
- Rossini N.O. et al. Crystal structure of *M. thermoresistibile* MurE reveals the binding mode of m-diaminopimelate. **PMID 36944394**.
- Das D. et al. Structure and function of the first full-length murein peptide ligase (Mpl). **PMID 21445265**.
- Munshi T. et al. Characterisation of ATP-dependent Mur ligases in *M. tuberculosis*. **PMID 23555903**.
- Wijayarathna C.D. et al. Isolation of ftsI and murE genes from *Corynebacterium glutamicum*. **PMID 11398928**.
- Shanmugam A. & Natarajan J. Comparative modeling of MurE from *M. leprae* (docking). **PMID 21491188**.
- Hervin V. et al. Mur Ligases as an Antibacterial Target (review). **PMID 38138566**.
- Kumar S. et al. The Potential of Mur Enzymes as Targets for Antimicrobial Drug Discovery (review). **PMID 37291783**.


## Artifacts

- [OpenScientist final report](murE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murE-deep-research-openscientist_artifacts/final_report.pdf)