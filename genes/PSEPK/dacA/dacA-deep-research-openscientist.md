---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.175365'
end_time: '2026-09-01T00:13:40.045386'
duration_seconds: 4527.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dacA
  gene_symbol: dacA
  uniprot_accession: Q88DM2
  protein_description: 'RecName: Full=serine-type D-Ala-D-Ala carboxypeptidase {ECO:0000256|ARBA:ARBA00012448};
    EC=3.4.16.4 {ECO:0000256|ARBA:ARBA00012448};'
  gene_info: Name=dacA {ECO:0000313|EMBL:AAN70372.1}; OrderedLocusNames=PP_4803 {ECO:0000313|EMBL:AAN70372.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase S11 family.
  protein_domains: Beta-lactam/transpept-like. (IPR012338); Peniciliin-bd_prot_C_sf.
    (IPR015956); Peptidase_S11. (IPR018044); Peptidase_S11_C. (IPR012907); Peptidase_S11_C_sf.
    (IPR037167)
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
  path: dacA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dacA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DM2
- **Protein Description:** RecName: Full=serine-type D-Ala-D-Ala carboxypeptidase {ECO:0000256|ARBA:ARBA00012448}; EC=3.4.16.4 {ECO:0000256|ARBA:ARBA00012448};
- **Gene Information:** Name=dacA {ECO:0000313|EMBL:AAN70372.1}; OrderedLocusNames=PP_4803 {ECO:0000313|EMBL:AAN70372.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase S11 family.
- **Key Domains:** Beta-lactam/transpept-like. (IPR012338); Peniciliin-bd_prot_C_sf. (IPR015956); Peptidase_S11. (IPR018044); Peptidase_S11_C. (IPR012907); Peptidase_S11_C_sf. (IPR037167)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dacA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dacA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dacA** (gene ID: dacA, UniProt: Q88DM2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dacA* / PP_4803 (UniProt Q88DM2)

**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), taxid 160488
**Gene:** *dacA* (ordered locus PP_4803) — EMBL AAN70372.1
**Protein:** serine-type D-Ala-D-Ala carboxypeptidase, EC 3.4.16.4
**Family:** Peptidase S11 (Pfam PF00768 + PF07943); penicilloyl-serine transferase / β-lactam-transpeptidase-like fold (InterPro IPR012338, IPR015956, IPR018044, IPR012907, IPR037167)
**Length:** 386 aa (Sec signal peptide 1–24; mature chain 25–386)

---

## 1. Summary (answer to the research question)

*dacA* (PP_4803) encodes a **low-molecular-weight penicillin-binding protein (LMW-PBP), specifically a serine-type D-alanyl-D-alanine carboxypeptidase (DD-carboxypeptidase; EC 3.4.16.4)** and the *P. putida* ortholog of *Escherichia coli* PBP5. Its primary reaction is **hydrolytic removal of the terminal D-alanine from the C-terminal D-Ala-D-Ala of muramyl-pentapeptide stems in peptidoglycan**, converting pentapeptides to tetrapeptides. By depleting the pentapeptide donor substrate used by transpeptidases, it **regulates (limits/tunes) the degree of peptidoglycan cross-linking**, which is required for normal cell shape and for buffering the envelope against β-lactam stress. The enzyme acts **in the periplasm on the peptidoglycan sacculus**, tethered to the outer face of the inner (cytoplasmic) membrane by a C-terminal amphipathic anchor after Sec-dependent export. It functions in the **peptidoglycan biosynthesis / cell-wall maturation pathway**, and — like its *Pseudomonas aeruginosa* ortholog — its penicilloyl-serine fold additionally supports intrinsic β-lactam resistance.

> **Note on evidence base:** No experimental study has been published on PP_4803 itself. The functional assignment is high-confidence and rests on (i) unambiguous sequence/domain identity, (ii) conservation of all catalytic motifs, and (iii) an extensive body of experimental work on the orthologous PBP5/DD-carboxypeptidase enzymes of *E. coli* and *P. aeruginosa*. Claims are labeled as direct database annotation, bioinformatic inference, or ortholog-based experimental evidence.

---

## 2. Identity verification

The gene symbol, EC number, organism, family, and domain architecture from UniProt are internally consistent and match the peptidase-S11 DD-carboxypeptidase (PBP5) group. This is **not** the ambiguous "dacA" of Firmicutes (the di-adenylate cyclase / c-di-AMP synthase, an unrelated protein); the peptidase-S11 fold, EC 3.4.16.4, and the "dacA/PBP5" nomenclature in Gram-negatives are distinct and correct here.

Bioinformatic confirmation (this work): the 386-aa sequence contains **all three canonical penicillin-recognizing active-site motifs** of the penicilloyl-serine transferase superfamily:

| Motif | Residues in Q88DM2 | Role |
|-------|--------------------|------|
| **S**xx**K** | Ser64–Leu–Thr–Lys67 | Catalytic nucleophile (Ser64 forms acyl-enzyme) + general base (Lys67) |
| **S**x**N** | Ser124–Gly–Asn126 | Active-site cleft / oxyanion & substrate positioning |
| **K**T**G** | Lys226–Thr–Gly | D-Ala-D-Ala substrate-binding (β3 strand) |

UniProt independently annotates active sites at Ser64 (acyl-ester intermediate), Lys67 (proton acceptor), position 124, and a binding site at position 226 — in exact agreement. An N-terminal Sec signal peptide (1–24) and a hydrophobic/amphipathic C-terminus (…FFRRMWDSIRLFFYGLFN) complete the classic PBP5 topology.

---

## 3. Key findings (with evidence)

### 3.1 Primary reaction and mechanism
- **Reaction:** DD-carboxypeptidase — preferential cleavage of (Ac)₂-L-Lys-D-Ala-|-D-Ala; "removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors" (UniProt catalytic activity / FUNCTION, EC 3.4.16.4). In peptidoglycan terms it removes the terminal D-Ala from the pentapeptide stem (L-Ala–D-Glu–*meso*-DAP–D-Ala–**D-Ala**), yielding a tetrapeptide.
- **Mechanism:** a two-step acyl-enzyme (ping-pong) mechanism via the Ser64 nucleophile — the same chemistry that makes these enzymes covalent targets ("penicillin-binding proteins") of β-lactams.
- **Ortholog evidence:** *E. coli* PBP5 "cleaves the terminal D-alanine from the muramyl pentapeptide in the peptidoglycan layer… In doing so, it varies the substrates for transpeptidation and plays a key role in maintaining cell shape" (Skoog et al., PMID 21674665). In Gram-negatives, DD-CPases generate the majority tetrapeptide muropeptides (Tehrani et al., PMID 40777447).

### 3.2 Substrate specificity
- Specificity is centered on the **terminal D-Ala-D-Ala** dipeptide: "Beyond the C-terminal d-alanyl-d-alanine moiety, PBP5… has little specificity for other elements of peptidoglycan structure" (Nemmara et al., PMID 27420403).
- It belongs to the membrane-bound **LMMA class** of DD-peptidases, which "catalyze DD-carboxypeptidase and endopeptidase reactions in vivo" and — unlike the soluble R39/R61 enzymes — do not require a free stem-peptide N-terminus, consistent with acting on the polymeric sacculus in situ (Nemmara et al., PMID 22029692).

### 3.3 Subcellular localization / site of action
- **Periplasm, anchored to the outer leaflet of the inner membrane.** The Sec signal peptide exports the protein; the C-terminal amphipathic helix anchors it so the catalytic domain projects into the periplasm where peptidoglycan resides (the "periplasm… contains the peptidoglycan layer"; PMID 40777447).
- *E. coli* PBP5 was characterized "in its native environment, the inner membrane," where it forms homo-oligomers (likely dimers) that position the catalytic domain to reach pentapeptides at varying distances from the membrane (Skoog et al., PMID 21674665). *P. aeruginosa* PBP5 was solubilized "by deletion of its C-terminal membrane anchor" (Smith et al., PMID 23629710), confirming the same topology in *Pseudomonas*.
- **Direct sequence-based corroboration (this work):** Kyte–Doolittle hydropathy analysis of Q88DM2 shows a hydrophobic N-terminal Sec signal peptide (residues 1–24, mean KD ≈ +1.27) and a C-terminal **amphipathic** segment (residues 367–386, …GGFF**RR**MWDSIRLFFYGLFN) — a basic Arg-Arg doublet (positive-inside) followed by an aromatic/aliphatic run — i.e., a monotopic amphipathic membrane anchor rather than a fully hydrophobic transmembrane helix. This is the diagnostic PBP5 topology and independently rules out a cytoplasmic or polytopic-transporter localization.

### 3.4 Biological process / pathway
- Pathway: **cell-wall biogenesis; peptidoglycan biosynthesis / maturation** (UniProt PATHWAY). GO: serine-type D-Ala-D-Ala carboxypeptidase activity (GO:0009002); regulation of cell shape (GO:0008360); cell-wall organization (GO:0071555); peptidoglycan biosynthetic process (GO:0009252).
- Mechanistically, by trimming pentapeptides to tetrapeptides the enzyme **controls the pool of transpeptidation donor substrate**, thereby setting the density/pattern of DD-cross-links. This is a *regulatory/maturation* role, not a wall-building (synthetic) one.

### 3.5 Physiological role (precise, not pleiotropic)
- **Cell-shape maintenance** and **intrinsic β-lactam resistance.** In the *E. coli* ortholog, *dacA*/PBP5 deletion sensitizes cells 4–8-fold to all β-lactams tested, reversibly (Sarkar et al., PMID 20047819), and the DD-carboxypeptidase catalytic activity is *essential* for this intrinsic resistance (Sarkar et al., PMID 21719544).
- **Functional redundancy:** bacteria encode several DD-CPases that act redundantly for robust cell-shape maintenance across conditions (Peters et al., PMID 27329754); hence *dacA* is typically individually non-essential, with defects unmasked only when paralogs are also removed.

### 3.6 *Pseudomonas*-specific / evolutionary context
- The closest structurally characterized ortholog, ***P. aeruginosa* PBP5**, is "one of the most abundant PBPs"; "its main function is that of a cell wall dd-carboxypeptidase, [but] it possesses sufficient β-lactamase activity to contribute to… resist… β-lactams," and its 2.05-Å structure "shows features closely resembling those of the class A β-lactamases" (Smith et al., PMID 23629710). This documents (i) the DD-CPase/β-lactamase dual activity likely shared by *P. putida* DacA and (ii) the evolutionary relationship between DD-carboxypeptidases and class A β-lactamases.
- Ecological relevance in *P. putida*: this soil bacterium actively edits its peptidoglycan with non-canonical D-amino acids (e.g., via its broad-spectrum racemase acting on plant-derived amino acids such as canavanine; Aliashkevich et al., PMID 33830599). LMW-PBPs including PBP4/PBP5 can process peptidoglycan bearing non-canonical D-amino acids (Miyamoto et al., PMID 32108264), placing DacA within *P. putida*'s cell-wall chemical-editing physiology.

---

## 4. Supported and refuted hypotheses

**Supported**
- H1: Q88DM2 is a serine DD-carboxypeptidase of peptidase family S11 (PBP5 ortholog) — supported by domain architecture and full catalytic-motif conservation.
- H2: Its reaction is removal of the terminal D-Ala from muramyl-pentapeptide, regulating cross-linking — supported by UniProt catalytic activity + ortholog data.
- H3: It localizes to the periplasm/inner-membrane and acts on the sacculus — supported by signal peptide, C-terminal amphipathic anchor, and ortholog membrane studies.
- H4: It contributes to cell shape and intrinsic β-lactam resistance — supported by ortholog knockouts.

**Refuted / rejected alternatives**
- Not the Firmicute *dacA* di-adenylate cyclase (c-di-AMP synthase): different fold, EC, and function — ruled out by family/domain identity.
- Not a wall-*synthesizing* transpeptidase (HMW-PBP): it is a LMW-PBP carboxypeptidase that *limits* cross-linking substrate, not a primary polymerizing/cross-linking enzyme.
- Not a soluble cytoplasmic enzyme: signal peptide + C-terminal membrane anchor place it in the periplasm.

---

## 5. Limitations and future directions

- **No direct experimental data on PP_4803**; conclusions are inferred from strong orthologs (*E. coli* PBP5, *P. aeruginosa* PBP5) and bioinformatics. Direct biochemical kinetics (kcat/Km on pentapeptide and β-lactams), a crystal/cryo-EM or AlphaFold-validated structure, and a *P. putida* Δ*dacA* (single and multi-CPase) phenotype would confirm specificity, dual β-lactamase activity, and the precise contribution to morphology.
- The **quantitative relative contribution of DacA vs. other *P. putida* DD-CPases** (redundancy structure) is unknown.
- Whether DacA preferentially processes **non-canonical D-amino-acid-substituted peptidoglycan** in *P. putida*'s soil/rhizosphere niche is an open, testable question.

---

## References (PMIDs)
- 21674665 — Skoog et al. PBP5 homo-oligomer in the *E. coli* inner membrane; reaction and localization.
- 40777447 — Tehrani et al. Gram-negative DD-CPases generate tetrapeptides; periplasmic PG.
- 27420403 — Nemmara et al. PBP5 substrate specificity centered on terminal D-Ala-D-Ala.
- 22029692 — Nemmara et al. Substrate specificity/classification of LMM DD-peptidases.
- 20047819 — Sarkar et al. *dacA*/PBP5 deletion → β-lactam sensitization.
- 21719544 — Sarkar et al. PBP5 DD-CPase activity essential for intrinsic β-lactam resistance.
- 27329754 — Peters et al. Redundancy of PG carboxypeptidases for cell-shape robustness.
- 23629710 — Smith et al. *P. aeruginosa* PBP5 structure; DD-CPase + β-lactamase; membrane anchor.
- 33830599 — Aliashkevich et al. *P. putida* PG chemical editing with non-canonical D-amino acids.
- 32108264 — Miyamoto et al. LMW-PBPs process PG containing non-canonical D-amino acids.


## Artifacts

- [OpenScientist final report](dacA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dacA-deep-research-openscientist_artifacts/final_report.pdf)