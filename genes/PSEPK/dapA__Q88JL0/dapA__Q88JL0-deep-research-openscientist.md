---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T09:53:41.660912'
end_time: '2026-09-01T10:09:18.394403'
duration_seconds: 936.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dapA__Q88JL0
  gene_symbol: dapA
  uniprot_accession: Q88JL0
  protein_description: 'RecName: Full=4-hydroxy-tetrahydrodipicolinate synthase {ECO:0000256|ARBA:ARBA00012086,
    ECO:0000256|HAMAP-Rule:MF_00418}; Short=HTPA synthase {ECO:0000256|HAMAP-Rule:MF_00418};
    EC=4.3.3.7 {ECO:0000256|ARBA:ARBA00012086, ECO:0000256|HAMAP-Rule:MF_00418};'
  gene_info: Name=dapA {ECO:0000256|HAMAP-Rule:MF_00418}; Synonyms=dapA-II {ECO:0000313|EMBL:AAN68247.1};
    OrderedLocusNames=PP_2639 {ECO:0000313|EMBL:AAN68247.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DapA family. {ECO:0000256|ARBA:ARBA00007592,
  protein_domains: Aldolase_TIM. (IPR013785); DapA. (IPR005263); DapA-like. (IPR002220);
    Schiff_base-form_aldolases_AS. (IPR020625); DHDPS (PF00701)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: dapA__Q88JL0-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dapA__Q88JL0-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JL0
- **Protein Description:** RecName: Full=4-hydroxy-tetrahydrodipicolinate synthase {ECO:0000256|ARBA:ARBA00012086, ECO:0000256|HAMAP-Rule:MF_00418}; Short=HTPA synthase {ECO:0000256|HAMAP-Rule:MF_00418}; EC=4.3.3.7 {ECO:0000256|ARBA:ARBA00012086, ECO:0000256|HAMAP-Rule:MF_00418};
- **Gene Information:** Name=dapA {ECO:0000256|HAMAP-Rule:MF_00418}; Synonyms=dapA-II {ECO:0000313|EMBL:AAN68247.1}; OrderedLocusNames=PP_2639 {ECO:0000313|EMBL:AAN68247.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DapA family. {ECO:0000256|ARBA:ARBA00007592,
- **Key Domains:** Aldolase_TIM. (IPR013785); DapA. (IPR005263); DapA-like. (IPR002220); Schiff_base-form_aldolases_AS. (IPR020625); DHDPS (PF00701)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dapA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dapA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dapA** (gene ID: dapA__Q88JL0, UniProt: Q88JL0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: dapA (Q88JL0) — 4-hydroxy-tetrahydrodipicolinate synthase in *Pseudomonas putida* KT2440

**Target:** dapA / dapA-II (OrderedLocusName PP_2639), UniProt **Q88JL0**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) (PSEPK)
**Family:** DapA family; Class I aldolase; (β/α)8 TIM-barrel (Aldolase_TIM IPR013785; DapA IPR005263; DHDPS PF00701; Schiff-base aldolase signature IPR020625)
**EC:** 4.3.3.7 (formerly 4.2.1.52)

---

## 1. Summary (Answer to the Research Question)

**dapA (Q88JL0) encodes 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase), historically called dihydrodipicolinate synthase (DHDPS).** Its primary function is to catalyze the first committed, rate-limiting step of the **diaminopimelate (DAP) pathway** to L-lysine: the aldol-type condensation of **pyruvate** with **L-aspartate-4-semialdehyde (ASA)** to give **(2S,4S)-4-hydroxy-2,3,4,5-tetrahydrodipicolinate (HTPA)** (Rhea RHEA:34171), a cyclic product that spontaneously dehydrates to dihydrodipicolinate. The enzyme is a **soluble, cytoplasmic homotetramer** (dimer-of-dimers) that operates through a **Class I aldolase, ping-pong mechanism** involving a Schiff-base intermediate on a conserved active-site lysine, and is subject to **allosteric feedback inhibition by L-lysine**. The pathway supplies both L-lysine (protein synthesis) and meso-diaminopimelate (peptidoglycan cross-linking). In *P. putida* the gene is a **paralog ("dapA-II")** of a small DHDPS isoenzyme family, paralleling the redundant DHDPS isoforms characterized in *P. aeruginosa*.

---

## 2. Gene/Protein Identity Verification

The gene symbol **dapA** is fully consistent with the UniProt annotation and with the domain architecture:
- The protein description (4-hydroxy-tetrahydrodipicolinate synthase, EC 4.3.3.7, DapA family) matches the canonical DHDPS/HTPA synthase enzyme.
- Domains **PF00701 (DHDPS)**, IPR005263 (DapA), IPR002220 (DapA-like), IPR013785 (aldolase TIM-barrel) and IPR020625 (Schiff-base-form aldolase active site) are the defining features of DHDPS.
- The synonym **dapA-II** (from EMBL AAN68247.1) indicates this is one of multiple dapA paralogs in *P. putida* KT2440 — a pattern experimentally documented in the related species *P. aeruginosa*.

No conflicting identity was found; literature on "DHDPS/DapA" corresponds directly to this protein family. Direct experimental characterization of the specific *P. putida* KT2440 protein Q88JL0 is limited, so its function is established by (i) strong sequence/domain homology to biochemically characterized bacterial DHDPS enzymes and (ii) direct studies in the closely related *Pseudomonas aeruginosa*.

---

## 3. Primary Function: The Reaction Catalyzed

**Reaction (authoritative, UniProt/Rhea RHEA:34171 for Q88JL0 specifically):** L-aspartate 4-semialdehyde + pyruvate → **(2S,4S)-4-hydroxy-2,3,4,5-tetrahydrodipicolinate (HTPA)** + H₂O + H⁺.

- DapA "converts pyruvate and L-aspartate-4-semialdehyde to 4-hydroxy-2,3,4,5-tetrahydrodipicolinic acid" and "is involved in the production of lysine and precursor molecules for peptidoglycan synthesis" (Schmitz et al., 2020, PMID 32356521).
- It "catalyzes the first committed step in the lysine biosynthesis pathway" (Gupta et al., 2018, PMID 29744651; Sridharan et al., 2014, PMID 24996798), and this condensation is the **rate-limiting step** of the DAP pathway (Impey et al., 2020, PMID 31330085).
- **Substrate specificity:** the two substrates are pyruvate (donor, forming the Schiff base) and ASA (acceptor aldehyde). Reported Km values across bacterial orthologs are ~0.15–0.57 mM (pyruvate) and ~0.04–0.55 mM (ASA) (Laber et al., 1992, PMID 1463470; Dogovski et al., 2013, PMID 24349508). The enzyme is specific for the (S)-stereochemistry of ASA and for pyruvate as the ketoacid donor.
- **EC reclassification:** originally annotated as a dehydratase (EC 4.2.1.52) on the assumption the product was dihydrodipicolinate; once HTPA was recognized as the true, direct enzymatic product (dehydration being a subsequent, largely spontaneous step), the enzyme was reclassified as a lyase, **EC 4.3.3.7** (reflected in current annotations, e.g., Gupta et al., PMID 29744651; Gupta et al., 2018 Vibrio, PMID 29337198).

---

## 4. Catalytic Mechanism

DHDPS is a **Class I (Schiff-base) aldolase** operating by a **ping-pong bi-bi** mechanism:
1. Pyruvate binds first and forms a **Schiff base (iminium)** with the ε-amino group of the **absolutely conserved active-site lysine** (Lys161 in *E. coli* numbering), captured by the IPR020625 Schiff-base aldolase signature present in Q88JL0.
2. ASA then binds; aldol addition, transimination/cyclization and dehydration yield HTPA (Laber et al., 1992, PMID 1463470).

Mutagenesis quantifies the lysine's role: *E. coli* **K161A/K161R** retain fold and substrate binding but lose ~280–750-fold in kcat (0.06–0.16 s⁻¹ vs 45 s⁻¹ wild type), with essentially unchanged Km and lysine Ki (Soares da Costa et al., 2010, PMID 20353808). A conserved catalytic Tyr/Thr proton-relay, contributed across the tight dimer, completes the active site.

---

## 5. Structure, Oligomeric State, and Localization

- **Fold:** each monomer is a (β/α)8 **TIM-barrel** (IPR013785) with a C-terminal α-helical domain.
- **Quaternary structure:** a **homotetramer ("dimer of dimers")**; two monomers jointly form each active site at the **tight-dimer interface**, and dimers associate around a solvent-filled central cavity (Soares da Costa et al., 2018, PMID 29204887; Reboul et al., 2012, PMID 22685390). Bacterial DHDPS adopts a **"head-to-head"** tetramer (contrasting the "back-to-back" plant form).
- **Functional role of oligomerization:** tetramerization rigidifies the active-site dynamics; disrupting the tetramer increases flexibility and lowers catalytic efficiency and substrate specificity (Reboul et al., 2012, PMID 22685390; Atkinson et al., 2018, PMID 29804823).
- **Localization:** a soluble **cytoplasmic** enzyme of amino-acid/cell-envelope precursor metabolism — it acts in the cytosol, upstream of membrane-associated peptidoglycan assembly. (No signal peptide/membrane domain is present; consistent with all characterized DHDPS enzymes being cytosolic.)

---

## 5b. Protein-Specific Sequence Evidence (this study)

To move beyond family-level homology, I aligned the actual Q88JL0 sequence (288 aa) to biochemically characterized *E. coli* DHDPS (P0A6L2) by global Needleman–Wunsch (BLOSUM62). Overall identity is **33.1%** (94/284), typical for cross-genus DHDPS orthologs, but **every catalytic residue is strictly conserved and co-numbered**:

| Function | *E. coli* residue | Q88JL0 residue |
|---|---|---|
| Schiff-base lysine (covalent catalysis) | Lys161 | **Lys161** ✓ |
| Catalytic proton-relay tyrosine | Tyr133 | **Tyr133** ✓ |
| Proton-relay tyrosine (2nd) | Tyr107 | **Tyr107** ✓ |
| Substrate-binding threonine | Thr44 | **Thr45** ✓ |
| ASA carboxylate-binding arginine | Arg138 | **Arg138** ✓ |
| Allosteric lysine-binding site | His56 | **Gln57** ✗ (non-canonical) |

**Interpretation:** the complete, conserved catalytic tetrad (Thr, Tyr, Tyr, Lys) plus the ASA-anchoring Arg confirm Q88JL0 is a **catalytically competent HTPA synthase** performing the canonical pyruvate + ASA condensation. However, the allosteric position 56 — where a **His or Glu is required for strong lysine feedback inhibition** (Soares da Costa et al., 2018, PMID 29204887) — is a **glutamine (Gln57)** in Q88JL0. This predicts that the dapA-II isoform is only **weakly, or not, lysine-feedback-inhibited**, providing a concrete molecular rationale for the reported divergence of allosteric regulation among *Pseudomonas* DHDPS paralogs (Impey et al., 2020, PMID 31330085).

## 6. Regulation

DHDPS is the principal **feedback-regulated valve** of the DAP/lysine pathway. The end-product **L-lysine binds allosterically** at the tight-dimer interface (~50 Å from the catalytic sites) to inhibit activity (Skovpen et al., 2016, PMID 26836694). Sensitivity is governed largely by a single residue: strong allosteric inhibition requires a **His or Glu at position 56** (*E. coli* numbering) rather than a basic residue; consequently many bacterial DHDPS enzymes are only weakly, or not, lysine-inhibited (Soares da Costa et al., 2018, PMID 29204887; Vauterin et al., 2000, PMID 10758475). In *Pseudomonas*, distinct DHDPS isoforms differ specifically in their allosteric lysine regulation (Impey et al., 2020, PMID 31330085).

---

## 7. Pathway Context and Biological Role

DapA opens the **diaminopimelate (DAP) pathway**, which branches from aspartate metabolism (aspartate → aspartyl-phosphate → ASA). HTPA is reduced by DHDPR (dapB) and processed through subsequent Dap enzymes (e.g., DapD/DapC/DapE or alternative routes) to **meso-2,6-diaminopimelate**, which is (i) a direct **cross-linking residue in Gram-negative peptidoglycan** and (ii) decarboxylated (LysA) to **L-lysine** for protein synthesis (Fazius et al., 2013, PMID 23504110; Schnell et al., 2012, PMID 22359568). Because animals lack this pathway, DHDPS is a long-standing **antibiotic/herbicide target** — though target validation must account for isoform redundancy (below).

**KEGG pathway assignment (this study):** PP_2639 is mapped to KEGG ortholog **K01714** (HTPA synthase, EC 4.3.3.7) and to pathway maps **ppu00300 (Lysine biosynthesis)** and ppu00261 (Monobactam biosynthesis), and to modules **M00016 (succinyl-DAP pathway, aspartate ⇒ lysine)** and **M00527 (DAP-aminotransferase pathway, aspartate ⇒ lysine)** — i.e. the enzyme feeds both DAP-pathway variants used by *P. putida*.

**Genomic context (this study):** dapA-II (PP_2639; genome coords 3,023,319–3,024,185, 867 bp) is **not embedded in a canonical *dap*/lysine operon**. It lies on the same strand immediately (338 bp) downstream of a **cellulose-synthase (*bcs*) operon** (PP_2634–PP_2638: cellulose synthase catalytic/translocator subunits, endo-1,4-D-glucanase, cellulose-synthase operon C protein), with a convergent GNAT acetyltransferase (PP_2640), an Fe–S protein (PP_2641) and a GntR-family regulator (PP_2642) downstream. This atypical location (versus the scattered classical *dap* genes, and versus dapA-I/PP_1237 at a separate locus) raises the hypothesis that dapA-II expression may be linked to the exopolysaccharide/biofilm-matrix context, though co-transcription with the *bcs* operon is not established.

---

## 8. *Pseudomonas*-Specific Considerations (dapA-II)

Unlike most bacteria, which carry a single dapA, *Pseudomonas* encode **multiple functional DHDPS isoforms**:
- *P. aeruginosa* encodes **two functional DHDPS enzymes (PaDHDPS1, PaDHDPS2)** with similar catalytic activity but **different allosteric regulation** (Impey et al., 2020, PMID 31330085).
- Deletion of the primary dapA in *P. aeruginosa* is **viable** (including growth in a mouse lung infection model) because homologues (e.g., PA0223, PA4188) **substitute for DapA** (Schnell et al., 2012, PMID 22359568).

The UniProt synonym **dapA-II** for PP_2639 explicitly marks Q88JL0 as a **second dapA paralog** in *P. putida* KT2440, consistent with this multi-isoform arrangement. Functionally it performs the canonical HTPA-synthase reaction; regulatory sensitivity and flux contribution may be partitioned across the paralogs, and loss of a single paralog can be buffered by the others.

### 8.1 The *P. putida* KT2440 DHDPS/DapA paralog landscape (this study)

Querying the KT2440 proteome for PF00701 (DapA/DHDPS-like) proteins and aligning each to *E. coli* DHDPS resolves the isoform relationships:

| Locus / UniProt | Gene | Length | %id vs *E. coli* DHDPS | Catalytic residues (Thr44/Tyr107/Tyr133/Arg138/Lys161) | Allosteric pos. 56 | Assessment |
|---|---|---|---|---|---|---|
| **PP_2639 / Q88JL0** | **dapA-II (target)** | 288 | 33.1% | all conserved | **Gln** (non-canonical) | competent DHDPS, likely lysine-**insensitive** |
| PP_1237 / Q88NH2 | dapA-I | 295 | 57.4% | all conserved | **His** (canonical) | canonical, lysine-**regulated** DHDPS |
| PP_2036 / Q88L99 | — | 295 | 26.3% | Thr44→**Ser**, Arg138→**Thr** altered | Trp | auto-annotated HTPA synthase; DHDPS activity **uncertain** |
| PP_3599 / Q88GW8 | — | 303 | — | — | — | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41) — different function |
| PP_1257 / Q88NF4 | — | 315 | — | — | — | 1-pyrroline-4-hydroxy-2-carboxylate deaminase (EC 3.5.4.22) — different function |

Key inferences:
- **dapA-I (PP_1237)** is the canonical, His56-bearing, lysine-feedback-**sensitive** "housekeeping" DHDPS.
- **dapA-II (PP_2639/Q88JL0)** — the target — is a **catalytically intact but divergent paralog** (only 30.4% identical to dapA-I) predicted to be **lysine-feedback-insensitive** (Gln at position 56). This division of labor mirrors the two-isoform DHDPS system experimentally characterized in *P. aeruginosa* (Impey et al., 2020, PMID 31330085).
- The PF00701 superfamily in *P. putida* also contains **non-DHDPS enzymes** (a glucarate dehydratase, a pyrroline deaminase) and a residue-degenerate member (PP_2036), reinforcing that DHDPS function must be assigned from active-site conservation — not family membership alone (Impey et al., 2020, PMID 31943170).

---

## 9. Supported and Refuted Hypotheses

**Supported:**
- H1 — Q88JL0 is a DHDPS/HTPA synthase catalyzing pyruvate + ASA → HTPA (domain/family homology + direct *Pseudomonas* studies). **Supported.**
- H2 — Mechanism is a Schiff-base (Class I aldolase) ping-pong reaction on a conserved active-site Lys. **Supported** (mutagenesis, kinetics).
- H3 — The functional unit is a cytoplasmic homotetramer with shared inter-subunit active sites. **Supported** (crystallography/AUC/SAXS across many orthologs).
- H4 — Activity is feedback-regulated by L-lysine, with sensitivity set by the position-56 residue. **Supported.**
- H5 — In *Pseudomonas*, dapA is one of several redundant isoforms (dapA-II). **Supported** (P. aeruginosa data + UniProt synonym).
- H6 — Q88JL0 itself has an intact catalytic apparatus. **Supported** by direct sequence alignment: all catalytic residues (Lys161, Tyr133, Tyr107, Thr45, Arg138) are strictly conserved vs *E. coli* DHDPS.
- H7 — Q88JL0 is likely lysine-feedback-insensitive (or weakly sensitive). **Supported bioinformatically** — the allosteric His56 is replaced by Gln57; requires biochemical confirmation.

**Refuted / revised:**
- The historical belief that the direct product is dihydrodipicolinate (and that the enzyme is a dehydratase, EC 4.2.1.52) is **refuted**; the direct product is HTPA and the enzyme is a lyase (EC 4.3.3.7).

---

## 10. Limitations and Future Directions

- **No direct biochemical study of the specific protein Q88JL0** was found; function is inferred from (i) strong homology and conserved catalytic residues verified here by sequence alignment, and (ii) experimental work on orthologs/paralogs (notably *P. aeruginosa* and *E. coli*). Confirmation would benefit from recombinant *P. putida* dapA-II kinetics, lysine-inhibition assays, and a crystal structure.
- The predicted **lysine-insensitivity of Q88JL0** (Gln57 at the allosteric site, versus His/Glu in feedback-sensitive DHDPS) is a bioinformatic inference that should be tested by direct lysine-inhibition kinetics. The **division of labor** between *P. putida* DHDPS paralogs (dapA-I vs dapA-II) also remains to be characterized experimentally.
- Whether both *P. putida* paralogs are simultaneously essential, or mutually redundant as in *P. aeruginosa*, should be tested by single and double knockouts.

---

### Key References (PMIDs)
32356521; 29744651; 24996798; 1463470; 20353808; 29204887; 22685390; 29804823; 26836694; 10758475; 31330085; 31943170; 22359568; 23504110; 24349508; 29337198.

*Bioinformatic analyses (sequence retrieval from UniProt; Needleman–Wunsch/BLOSUM62 alignments; KT2440 paralog survey) were performed in this study.*


## Artifacts

- [OpenScientist final report](dapA__Q88JL0-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dapA__Q88JL0-deep-research-openscientist_artifacts/final_report.pdf)