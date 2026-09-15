---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:57:16.385500'
end_time: '2026-08-19T08:39:53.840876'
duration_seconds: 2557.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pucL
  gene_symbol: pucL
  uniprot_accession: Q88F12
  protein_description: 'RecName: Full=2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline
    decarboxylase {ECO:0000256|ARBA:ARBA00012257}; EC=4.1.1.97 {ECO:0000256|ARBA:ARBA00012257};'
  gene_info: Name=pucL {ECO:0000313|EMBL:AAN69867.1}; OrderedLocusNames=PP_4287 {ECO:0000313|EMBL:AAN69867.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: OHCU_decarboxylase. (IPR018020); OHCU_decarboxylase-1. (IPR017580);
    OHCU_decarboxylase_sf. (IPR036778); OHCU_decarbox (PF09349)
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
  path: pucL-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pucL-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F12
- **Protein Description:** RecName: Full=2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline decarboxylase {ECO:0000256|ARBA:ARBA00012257}; EC=4.1.1.97 {ECO:0000256|ARBA:ARBA00012257};
- **Gene Information:** Name=pucL {ECO:0000313|EMBL:AAN69867.1}; OrderedLocusNames=PP_4287 {ECO:0000313|EMBL:AAN69867.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** OHCU_decarboxylase. (IPR018020); OHCU_decarboxylase-1. (IPR017580); OHCU_decarboxylase_sf. (IPR036778); OHCU_decarbox (PF09349)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pucL" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pucL' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pucL** (gene ID: pucL, UniProt: Q88F12) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pucL* / PP_4287 (UniProt Q88F12) in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

The gene **pucL** (ordered locus **PP_4287**; UniProt **Q88F12**) of *Pseudomonas putida* KT2440 encodes **2‑oxo‑4‑hydroxy‑4‑carboxy‑5‑ureidoimidazoline (OHCU) decarboxylase (EC 4.1.1.97)**, a small (171 aa) soluble, cofactor‑independent enzyme. It catalyzes the **third and final step of the uricase‑dependent purine/urate degradation pathway**, converting the unstable intermediate OHCU into **(S)‑allantoin + CO₂**. Its function is to guarantee **rapid and stereospecific** production of the (S)‑enantiomer of allantoin — the biologically relevant form used by downstream ureide‑catabolizing enzymes — rather than the slow, racemic product formed by spontaneous non‑enzymatic decay. The enzyme acts in the **cytoplasm**, integrated into purine catabolism that ultimately allows bacteria to use purines/allantoin as a nitrogen (and sometimes carbon) source.

> **Identity verification (per task requirement):** UniProt Q88F12 is annotated `2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline decarboxylase`, EC 4.1.1.97, gene `pucL`/`PP_4287`, organism *Pseudomonas putida* KT2440, with the diagnostic **OHCU_decarboxylase** domain (Pfam **PF09349**; InterPro IPR018020, IPR017580, IPR036778). The catalytic-activity and pathway annotations retrieved directly from UniProt match the protein description exactly. **Caveat on the symbol:** the label *pucL* elsewhere (notably *Bacillus subtilis*) denotes **urate oxidase (uricase)**; in this *P. putida* genome annotation *pucL* is simply the assigned locus symbol, and the domain/EC evidence unambiguously identifies the product as an **OHCU decarboxylase**, not a uricase. All functional literature below concerns the OHCU decarboxylase (URAD/UraD) family, which is the correct protein.

---

## 2. Molecular Identity and Sequence Features

| Property | Value | Source |
|---|---|---|
| UniProt accession | Q88F12 (Q88F12_PSEPK) | UniProt |
| Gene / locus | *pucL* / PP_4287 | UniProt / EMBL AAN69867.1 |
| Length | 171 aa (soluble, α‑helical; no signal peptide/TM segment) | UniProt sequence |
| EC number | 4.1.1.97 | UniProt |
| Reaction | 5‑hydroxy‑2‑oxo‑4‑ureido‑2,5‑dihydro‑1H‑imidazole‑5‑carboxylate (OHCU) + H⁺ → (S)‑allantoin + CO₂ | UniProt catalytic activity |
| Pathway | Purine metabolism; urate degradation; (S)‑allantoin from urate: **step 3/3** (UniPathway UPA00394) | UniProt |
| Domain / family | OHCU_decarboxylase (Pfam PF09349; InterPro IPR018020/IPR017580/IPR036778); eggNOG **COG3195** | UniProt/InterPro |
| Evidence level | Protein existence: **4 – Predicted** (function inferred from homology/annotation; no direct experimental study of this specific protein) | UniProt |

---

## 3. Primary Function: The Catalyzed Reaction and Substrate Specificity

The **uricase (urate‑oxidase) degradation pathway** converts the poorly soluble purine end‑product uric acid to the much more soluble ureide **allantoin** in three enzymatic steps [Ramazzina et al., 2006, PMID 16462750]:

1. **Urate oxidase (uricase)** — urate → **5‑hydroxyisourate (HIU)**
2. **HIU hydrolase (HIUase / transthyretin‑related)** — HIU → **OHCU**
3. **OHCU decarboxylase (this protein, pucL/PP_4287)** — **OHCU → (S)‑allantoin + CO₂**

Ramazzina and colleagues established this three‑enzyme scheme by phylogenetic genome comparison, showing that the two genes downstream of uricase (HIUase and OHCU decarboxylase) "catalyze two consecutive steps following urate oxidation to 5‑hydroxyisourate (HIU): hydrolysis of HIU to give 2‑oxo‑4‑hydroxy‑4‑carboxy‑5‑ureidoimidazoline (OHCU) and **decarboxylation of OHCU to give S‑(+)‑allantoin**" [PMID 16462750].

**Substrate specificity:** The enzyme is highly specialized for its single natural substrate, OHCU. Its product complex with **(S)-allantoin** was captured crystallographically [Kim, Park & Rhee 2007, PMID 17567580], and a structural isomer of the purine hypoxanthine, **allopurinol**, acts as a **competitive inhibitor** of the bacterial enzyme (Kᵢ = 30 ± 2 µM in *Klebsiella pneumoniae*), consistent with an active site tuned to the imidazoline/purine‑derived scaffold [French & Ealick 2010, PMID 20826786].

---

## 4. Physiological Rationale: Why the Cell Needs This Enzyme

OHCU is an **unstable intermediate** that spontaneously decarboxylates. Without the enzyme, the reaction still proceeds but is slow and **non‑stereospecific**: "Urate oxidation produces **racemic allantoin on a time scale of hours**, whereas the full enzymatic complement produces **dextrorotatory allantoin on a time scale of seconds**" [Ramazzina et al., 2006, PMID 16462750].

Thus pucL/OHCU decarboxylase performs two coupled jobs:
- **Kinetic acceleration** — converting OHCU to allantoin in seconds rather than hours.
- **Stereochemical control** — producing exclusively **(S)-(+)-allantoin**, the enantiomer recognized by downstream ureide‑pathway enzymes (allantoinase, allantoate amidohydrolase, etc.).

This resolves the long‑standing question of how organisms selectively make (S)-allantoin [Kim et al., 2007, PMID 17567580].

---

## 5. Structural Basis and Catalytic Mechanism

Crystallographic and mutagenesis studies of family members (zebrafish, *Klebsiella pneumoniae*, human) define the mechanism that Q88F12 is expected to share (Pfam PF09349):

- **Fold / oligomer:** a **homodimeric, all‑α‑helical protein of a novel structural motif** [Kim et al., 2007, PMID 17567580].
- **Cofactor independence:** "the active site in each monomer contains **no cofactors**, distinguishing this enzyme mechanistically from other cofactor‑dependent decarboxylases" [PMID 17567580]. Catalysis is direct, with no metal ion, PLP, or thiamine cofactor.
- **Catalytic residue / stereocontrol:** "the **invariant histidine** residue in the OHCU decarboxylase family plays an essential role in producing (S)‑allantoin through a **proton transfer from the hydroxyl group at C4 to C5 at the re‑face of OHCU**" [PMID 17567580].
- **Induced‑fit organization:** apo vs. allantoin‑bound structures of the *K. pneumoniae* enzyme show that "**ligand binding organizes the active site residues for catalysis**"; the inhibitor allopurinol disrupts this organization (confirmed by circular dichroism) [French & Ealick 2010, PMID 20826786].

The 171‑aa length, all‑helical prediction, and conserved OHCU_decarboxylase domain of Q88F12 are fully consistent with this family architecture.

**Sequence-based confirmation of the catalytic residue (this work):** A Needleman–Wunsch alignment of Q88F12 against reviewed *standalone* OHCU decarboxylase orthologs — human URAD (A6NGE7), zebrafish (A1L259), and mouse (Q283N4) — shows the family's single conserved histidine mapping to **His73 of Q88F12** in all three orthologs (~30–35% overall identity). His73 thus corresponds to the invariant active-site histidine that Kim et al. (2007) demonstrated is essential for the proton transfer generating (S)-allantoin, giving evolutionary/sequence evidence that Q88F12 is catalytically competent.

---

## 6. Subcellular Localization

No experimental localization data exist for Q88F12 (UniProt evidence level "Predicted"). However, multiple lines of inference place it in the **cytoplasm**:
- The protein has **no signal peptide and no transmembrane segment** (soluble 171‑aa helical protein).
- Its substrate OHCU is generated intracellularly by soluble upstream enzymes (uricase and HIU hydrolase), so the enzyme must act where these intermediates are produced.
- Family members characterized biochemically are soluble cytosolic proteins.

**Conclusion:** cytoplasmic (soluble), acting in a metabolon-like sequence with uricase and HIU hydrolase.

---

## 7. Pathway Context and Broader Biological Role

OHCU decarboxylase sits at the end of the **purine catabolism → ureide** route. In many bacteria this pathway enables purines/urate/allantoin to be used as **nitrogen (and sometimes carbon) sources**:

- In *Klebsiella pneumoniae*, "purines can be used as the sole source of nitrogen … under aerobic conditions," with allantoin further degraded by allantoinase and allantoate amidohydrolase, under nitrogen‑responsive regulation (NtrC/NAC and a GntR‑family repressor HpxS) [Guzmán et al., 2011, PMID 21357483].
- In *Streptomyces coelicolor*, allantoin catabolic genes are controlled by the repressor **AllR**, responding to allantoic acid/glyoxylate [Navone et al., 2015, PMID 26187964], underscoring that this branch of metabolism is tightly regulated by nutrient availability.
- The evolutionary logic of the pathway is highlighted by its **loss in hominids**: humans retain a pseudogenized/inactivated set (UOX, URAHP, URAD), and recombinant human OHCU decarboxylase is a well‑folded but catalytically impaired enzyme, reflecting relaxed selection after uricase loss [Rodrigues et al., 2026, PMID 41956358]. This confirms URAD/pucL as an evolutionarily conserved, functional enzyme in organisms (like *P. putida*) that retain the complete pathway.

**Genomic-context evidence in *P. putida* KT2440 (this work):** *pucL*/PP_4287 lies within a contiguous, same-strand **purine/urate catabolic gene cluster** (KEGG genome, ~4.877–4.879 Mb):

| Locus | Product | KO / EC |
|---|---|---|
| PP_4284 | adenine/guanine/hypoxanthine permease | K06901 |
| PP_4285 | **5-hydroxyisourate (HIU) hydrolase** (pathway step 2, makes OHCU) | K07127 / EC 3.5.2.17 |
| PP_4286 | allantoinase | K16842 / EC 3.5.2.5 |
| **PP_4287** | **OHCU decarboxylase (pucL, step 3)** | K13485 / EC 4.1.1.97 |
| PP_4288 | ureidoglycolate lyase | K01483 / EC 4.3.2.3 |
| PP_4290 | uric acid permease | K24206 |

The enzyme that generates *pucL*'s substrate (HIU hydrolase, PP_4285) is immediately adjacent, and downstream allantoin-degrading enzymes (allantoinase, ureidoglycolate lyase) and purine/urate transporters are clustered together. This "guilt-by-association" organization independently confirms that PP_4287 operates *in situ* within a coordinated **urate → allantoin → glyoxylate/ammonia** degradation route.

In *P. putida* KT2440 — a soil saprophyte that thrives on diverse organic substrates — this cluster contributes to **purine/urate scavenging for nitrogen recycling**, converting urate into assimilable allantoin and beyond.

**Pathway-completeness note (this work):** KEGG KO-link queries confirm KT2440 encodes the entire *downstream* module — HIU hydrolase (PP_4285), OHCU decarboxylase (PP_4287), allantoinase (PP_4286), ureidoglycolate lyase (PP_4288) — but **no canonical urate oxidase** is annotated (neither K00365 uricase, K16838 HpxO, nor K13484 PuuD-type). Because HIU hydrolase acts specifically on 5-hydroxyisourate (the direct product of urate oxidation), an upstream urate-oxidizing activity must nonetheless exist, implying a **divergent/unannotated urate oxidase** in KT2440. This does not change the assignment of PP_4287 as the step-3 OHCU decarboxylase, but flags the first step as annotation-incomplete and a target for experimental verification.

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- H1 — Q88F12/pucL is an **OHCU decarboxylase (EC 4.1.1.97)** catalyzing OHCU → (S)-allantoin + CO₂. *(UniProt annotation + domain + family literature.)*
- H2 — It performs **step 3/3** of the urate→(S)-allantoin pathway and enforces **fast, stereospecific** (S)-allantoin formation. *(PMID 16462750, 17567580.)*
- H3 — The enzyme is **cofactor‑independent**, a **helical homodimer**, using an **invariant histidine** for stereocontrol. *(PMID 17567580, 20826786.)*
- H4 — It functions in the **cytoplasm**, embedded in nitrogen‑yielding purine catabolism. *(Sequence inference + pathway context, PMID 21357483.)*
- H5 — In *P. putida* KT2440, PP_4287 is embedded in a **physically clustered purine/urate–allantoin catabolic operon** (HIU hydrolase, allantoinase, ureidoglycolate lyase, purine/urate permeases). *(KEGG genomic-context analysis, this work.)*
- H6 — Q88F12 retains the **invariant catalytic His73** of the family. *(Ortholog alignment, this work; mechanism per PMID 17567580.)*

**Refuted / excluded:**
- The symbol *pucL* does **NOT** here indicate **urate oxidase/uricase** (its meaning in *B. subtilis*); the EC number, catalytic reaction, and Pfam PF09349 domain exclude a uricase assignment.

---

## 9. Limitations and Future Directions

- **Direct experimental evidence is lacking for the specific *P. putida* protein** (UniProt "Predicted"). All mechanistic and structural detail derives from orthologs (mouse, zebrafish, *K. pneumoniae*, human) and from robust domain/pathway conservation.
- No experimental subcellular localization or in‑vitro kinetics for Q88F12 itself; these are inferred.
- **Upstream step not annotated:** KT2440 lacks a KEGG-annotated classical urate oxidase, so the identity of the enzyme producing 5-hydroxyisourate (the substrate source for the module) remains to be established experimentally.
- **Future work:** recombinant expression and steady‑state kinetics of Q88F12 with OHCU; confirmation of the His73 catalytic residue by site-directed mutagenesis; identification of the divergent urate oxidase feeding PP_4285/PP_4287; growth assays testing urate/allantoin as sole nitrogen sources in KT2440 and its regulation; and an experimental (or AlphaFold-validated) structure to confirm the homodimeric helical fold.

---

## 10. Key References
- Ramazzina et al. *Nat. Chem. Biol.* 2006 — pathway completion; racemic vs. (S)-allantoin kinetics. **PMID 16462750**
- Kim, Park & Rhee 2007 — OHCU decarboxylase–(S)-allantoin structure; cofactor‑free mechanism; invariant His. **PMID 17567580**
- French & Ealick 2010 — *K. pneumoniae* OHCU decarboxylase structures, kinetics, allopurinol inhibition. **PMID 20826786**
- Rodrigues et al. 2026 — human OHCU decarboxylase (URAD) characterization; evolutionary conservation. **PMID 41956358**
- Guzmán et al. 2011 — purines as nitrogen source; allantoin pathway regulation in *K. pneumoniae*. **PMID 21357483**
- Navone et al. 2015 — AllR regulation of allantoin pathway in *S. coelicolor*. **PMID 26187964**


## Artifacts

- [OpenScientist final report](pucL-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pucL-deep-research-openscientist_artifacts/final_report.pdf)