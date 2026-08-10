---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T16:18:26.180817'
end_time: '2026-07-25T16:29:02.507069'
duration_seconds: 636.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fruK
  gene_symbol: fruK
  uniprot_accession: Q88PQ4
  protein_description: 'RecName: Full=Phosphofructokinase {ECO:0000256|PIRNR:PIRNR000535};'
  gene_info: Name=fruK {ECO:0000313|EMBL:AAN66419.1}; OrderedLocusNames=PP_0794 {ECO:0000313|EMBL:AAN66419.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the carbohydrate kinase PfkB family.
  protein_domains: 1-PFruKinase. (IPR022463); Carboh/pur_kinase_PfkB_CS. (IPR002173);
    PfkB_dom. (IPR011611); Ribokinase-like. (IPR029056); Tagatose/fructose_Pkinase.
    (IPR017583)
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
  path: fruK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fruK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PQ4
- **Protein Description:** RecName: Full=Phosphofructokinase {ECO:0000256|PIRNR:PIRNR000535};
- **Gene Information:** Name=fruK {ECO:0000313|EMBL:AAN66419.1}; OrderedLocusNames=PP_0794 {ECO:0000313|EMBL:AAN66419.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the carbohydrate kinase PfkB family.
- **Key Domains:** 1-PFruKinase. (IPR022463); Carboh/pur_kinase_PfkB_CS. (IPR002173); PfkB_dom. (IPR011611); Ribokinase-like. (IPR029056); Tagatose/fructose_Pkinase. (IPR017583)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fruK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fruK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fruK** (gene ID: fruK, UniProt: Q88PQ4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: fruK (PP_0794 / Q88PQ4) in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**fruK** (locus PP_0794; UniProt **Q88PQ4**) of *Pseudomonas putida* KT2440 encodes **1-phosphofructokinase (fructose-1-phosphate kinase, FruK; EC 2.7.1.56)**, a soluble cytoplasmic enzyme of the **PfkB (ribokinase-like) carbohydrate-kinase family**. Its primary function is to catalyze the **ATP-dependent phosphorylation of β-D-fructose 1-phosphate to β-D-fructose 1,6-bisphosphate**:

> β-D-fructose 1-phosphate + ATP → β-D-fructose 1,6-bisphosphate + ADP + H⁺  (Rhea:14213)

FruK is the committed cytoplasmic step of the **fructose phosphotransferase (PTS) utilization pathway**. Fructose is imported and simultaneously phosphorylated to **fructose-1-phosphate (F1P)** by the fructose-specific PTS (FruB/FruA); FruK then converts F1P to fructose-1,6-bisphosphate, which is cleaved by fructose-bisphosphate aldolase and channelled into central carbon metabolism. Because *P. putida* KT2440 **lacks glycolytic 6-phosphofructokinase and metabolizes sugars exclusively via the Entner–Doudoroff pathway**, FruK is the obligatory, dedicated kinase that admits fructose to central metabolism. FruK is encoded in the **fruBKA operon**, which is repressed by the regulator **Cra (FruR)** and de-repressed specifically by FruK's own substrate, **F1P** — placing FruK at the heart of a feed-forward regulatory circuit for fructose catabolism.

---

## 2. Gene / Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88PQ4 | UniProt |
| Gene name / locus | *fruK* / PP_0794 | UniProt (EMBL AAN66419.1) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | UniProt |
| Protein | Phosphofructokinase → **1-phosphofructokinase** | UniProt |
| EC number | **2.7.1.56** | UniProt / Rhea |
| Length | 315 aa | UniProt |
| Family | Carbohydrate kinase **PfkB** family | UniProt SIMILARITY |
| Domains | PF00294 (PfkB); IPR011611 (PfkB domain); IPR029056 (ribokinase-like); IPR017583 (tagatose/fructose PfkB-type kinase); IPR002173 (PfkB conserved site) | InterPro/Pfam |
| KEGG | ppu:PP_0794 | UniProt xref |

**Verification outcome — IDENTITY CONFIRMED.** The gene symbol *fruK*, the organism, the UniProt catalytic annotation (F1P + ATP → FBP), the EC number 2.7.1.56, and the PfkB/ribokinase-like domain architecture are all mutually consistent and match the literature for 1-phosphofructokinase. A primary study (Yoon et al. 2021, PMID 33476373) explicitly names **"Pseudomonas putida … the 1-phosphofructokinase FruK"** within the fru operon, giving direct, organism-specific corroboration. There is no evidence of a mistaken-identity conflict with a same-symbol gene in another organism.

> ⚠️ Note on nomenclature: In *P. putida* the operon is written **fruBKA** (FruB = PTS EI/FPr-like fusion component, FruK = 1-PFK, FruA = PTS EII permease). In *E. coli* the equivalent operon is **fruFKA**. "FruK" should not be confused with the glycolytic **PfkA/PfkB 6-phosphofructokinases**, which act on fructose-**6**-phosphate and belong (for PfkA) to a different family.

### 2.1 Genomic context (fruBKA operon) — independent bioinformatic verification
Locus-name resolution against *P. putida* KT2440 (taxid 160488) places *fruK* within a compact, functionally coherent gene cluster, exactly matching the operon architecture in the literature:

| Locus | Gene | UniProt | Product |
|---|---|---|---|
| PP_0792 | *cra* (fruR) | Q88PQ6 | Catabolite repressor-activator (Cra), DNA-binding dual regulator |
| PP_0793 | *fruB* | Q88PQ5 | Phosphoenolpyruvate–protein phosphotransferase (PTS multiphosphoryl-transfer/EI component) |
| **PP_0794** | ***fruK*** | **Q88PQ4** | **Phosphofructokinase (1-PFK) — this study** |
| PP_0795 | *fruA* | Q88PQ3 | Protein-Nπ-phosphohistidine–D-fructose phosphotransferase (fructose PTS EII permease) |
| PP_0796 | – | Q88PQ2 | Cytoplasmic protein |

The co-localization of *fruK* between *fruB* (PTS phosphotransfer) and *fruA* (fructose EII permease), with the *cra* regulator immediately upstream, independently corroborates FruK's role in the fructose-PTS utilization module and its Cra/F1P control (see §5.3). Conserved gene neighborhood is itself strong evidence of shared function and co-regulation.

---

## 3. Primary Function: The Catalyzed Reaction and Substrate Specificity

FruK is an **ATP-dependent sugar-phosphate kinase** that phosphorylates the C6 hydroxyl of **fructose-1-phosphate**, generating **fructose-1,6-bisphosphate** (UniProt Q88PQ4; Rhea:14213; EC 2.7.1.56). Associated molecular functions annotated for the protein are **1-phosphofructokinase activity** (GO:0008662) and **ATP binding** (GO:0005524).

**Substrate specificity.** The physiological substrate is the fructose-PTS product fructose-1-phosphate — *not* fructose-6-phosphate. This distinction is functionally critical: the fructose PTS phosphorylates the incoming sugar at C1, so a specialized 1-phosphofructokinase (rather than the glycolytic 6-phosphofructokinase) is required to complete phosphorylation to the bis-phosphate. Biochemical characterization of orthologous FruK enzymes confirms this reaction directly:

- In *Aeromonas hydrophila*, "1-Phosphofructokinase (1-PFK), which converts the product of the PTS reaction to fructose 1,6-diphosphate, was present … grown with fructose" (Binet et al. 1998, PMID 9579084).
- In *Xanthomonas campestris*, "The fructose 1-phosphate produced by the phosphotransferase system is phosphorylated into fructose 1,6-bisphosphate by a 1-phosphofructokinase" (de Crécy-Lagard et al. 1991, PMID 1655739).

**Structure/sequence-based evidence of catalytic competence.** The 315-aa sequence carries a single Carbohydrate-kinase PfkB domain (UniProt feature, residues 12–290) and displays the two diagnostic ribokinase-superfamily signatures: (i) an N-terminal glycine-rich loop `…GGFLGGDN…` (GG at positions 58 and 62), and (ii) the C-terminal catalytic motif **`GAGD` (residues 251–254**, within `…VASTVGAGDSLVAG…`). In the ribokinase/PfkB fold, the aspartate of the GAGD motif is the conserved catalytic base that deprotonates the sugar hydroxyl to permit in-line phosphoryl transfer from ATP. The presence and spacing of these motifs provide sequence-level evidence — independent of database text annotation — that FruK is a bona fide, catalytically competent PfkB-family sugar kinase.

**Family / structural basis.** FruK belongs to the **PfkB family** of carbohydrate kinases, which share a **ribokinase-like α/β/α fold** and include *E. coli* PfkB, ribokinase, and phosphotagatokinase (Wu et al. 1991, PMID 1850730). The family is evolutionarily and mechanistically distinct from the major glycolytic PfkA-type 6-phosphofructokinase: the *E. coli* FruK sequence shows "little similarity to the major 6-phosphofructokinase (pfkA) … but there is 27% … identity … with the minor 6-phosphofructokinase (pfkB)" (Orchard & Kornberg 1990, PMID 1981619). The five InterPro signatures on Q88PQ4 (PfkB domain, ribokinase-like, PfkB conserved site, tagatose/fructose PfkB-type kinase) place the *P. putida* protein squarely in this family.

---

**Quaternary structure (inference).** No experimental oligomeric-state data exist for *P. putida* FruK; characterized PfkB-family 1-phosphofructokinases (e.g., *E. coli* FruK) are typically homo-oligomers (commonly dimeric), and *E. coli* FruK has additionally been shown to form higher-order hetero-complexes with the Cra regulator (Weeramange et al. 2024, PMID 38723750). The oligomeric state of the *P. putida* enzyme remains to be determined experimentally.

## 4. Subcellular Localization

FruK carries out its function in the **cytoplasm (cytosol)**. UniProt assigns the cytosol (GO:0005829) by phylogenetic inference. Consistent with this, the 315-aa sequence contains no signal peptide or transmembrane segment, and PfkB-family sugar kinases are canonically soluble cytoplasmic enzymes. Mechanistically the localization is expected: the membrane-embedded fructose PTS (FruA/FruB) delivers fructose-1-phosphate into the cytoplasm, where soluble FruK phosphorylates it using cytoplasmic ATP. *(Evidence class: inference from sequence, family, and biochemical logic — no direct experimental localization study specific to P. putida FruK was found.)*

---

## 5. Biochemical Pathway and Physiological Role

### 5.1 Fructose utilization pathway (the "fru" system)
*P. putida* KT2440 has an unusually minimal PTS: the genome encodes only five PTS proteins, of which **FruA and FruB constitute the complete fructose intake system** (Pflüger & de Lorenzo 2008, PMID 18296519). The pathway operates as:

1. **Import + phosphorylation:** fructose → **fructose-1-phosphate (F1P)** by the fructose PTS (PEP-dependent; FruB relays phosphate to the FruA EII permease).
2. **FruK step:** **F1P + ATP → fructose-1,6-bisphosphate** (this enzyme).
3. **Aldol cleavage:** fructose-1,6-bisphosphate → dihydroxyacetone-P + glyceraldehyde-3-P (fructose-bisphosphate aldolase), feeding lower central metabolism.

### 5.2 Why FruK is obligatory in *P. putida*
*P. putida* catabolizes hexoses **exclusively through the Entner–Doudoroff (ED) pathway "due to the absence of 6-phosphofructokinase"** (Chavarría et al. 2013, PMID 23301697). There is therefore **no glycolytic F6P→FBP reaction**; forcing the Embden–Meyerhof–Parnas route by heterologous *E. coli* pfkA was even detrimental to growth and oxidative-stress tolerance. Consequently, FruK's 1-PFK reaction is the *only* route by which PTS-imported fructose is converted to a bisphosphate that aldolase can cleave — making FruK indispensable for fructose catabolism. The essentiality of FruK for fructose growth is directly demonstrated in *E. coli*, where "The fruK mutants were unable to utilize … fructose and fructose-1-phosphate" (Molchanova et al. 1992, PMID 1332910).

### 5.3 Regulatory role — a feed-forward circuit
FruK is embedded in a tight regulatory loop. The **fruBKA operon is repressed by the Cra (FruR) transcription factor**, and the *sole physiological effector* that relieves this repression in *P. putida* is **fructose-1-phosphate — FruK's own substrate**: "Cra(PP) represses expression in vivo of the cognate fruBKA operon in a fashion dependent just on F1P, ruling out any other physiological effector" (Chavarría et al. 2014, PMID 24918052). Thus arriving fructose (as F1P) both (a) feeds FruK catalysis and (b) induces transcription of *fruK* itself, giving feed-forward activation of the pathway. In the wider gammaproteobacterial context, "transcription of the fru operon … and the 1-phosphofructokinase FruK is repressed by FruR in the absence of the inducer F1P" (Yoon et al. 2021, PMID 33476373).

### 5.4 Possible moonlighting / broader connections (lower confidence, from orthologs)
- In *E. coli*, FruK can run its **reverse reaction** (FBP→F1P) at physiological concentrations and **binds the Cra regulator directly with nanomolar affinity**, adding a protein-level layer to central-metabolism regulation; the authors note these findings "might have wide-spread relevance to other γ-proteobacteria, which conserve both Cra and FruK" (Weeramange et al. 2024, PMID 38723750). Whether *P. putida* FruK moonlights similarly is untested.
- The *P. putida* fructose PTS **cross-talks with the nitrogen-related PTS branch** (EIIAᴺᵗʳ), linking carbon and nitrogen sensing (Pflüger & de Lorenzo 2008, PMID 18296519). This is upstream of FruK but defines the regulatory neighbourhood in which the enzyme operates.

---

## 6. Supported and Refuted Hypotheses

**Supported:**
- H1 — FruK is a 1-phosphofructokinase (EC 2.7.1.56) converting F1P + ATP → fructose-1,6-bisphosphate. **Strongly supported** (UniProt/Rhea annotation; ortholog biochemistry PMIDs 9579084, 1655739).
- H2 — FruK belongs to the PfkB/ribokinase-like family, distinct from glycolytic PfkA. **Strongly supported** (InterPro/Pfam; PMIDs 1850730, 1981619).
- H3 — FruK acts in the fructose-PTS (fruBKA) catabolic pathway, downstream of FruA/FruB. **Supported** (PMIDs 33476373, 18296519, 24918052).
- H4 — FruK is functionally obligatory for fructose use because *P. putida* lacks 6-PFK and uses the ED pathway. **Supported** (PMID 23301697; ortholog essentiality PMID 1332910).
- H5 — FruK's substrate F1P is the physiological inducer of its own operon via Cra. **Supported** (PMID 24918052).
- H6 — FruK is a soluble cytoplasmic enzyme. **Supported by inference** (UniProt GO cytosol; no signal/TM; family logic).
- H7 — Genomic context: *fruK* lies in the fruBKA operon with *cra* upstream, and its sequence carries the PfkB catalytic motifs. **Supported by bioinformatics** (locus map PP_0792 *cra* – PP_0793 *fruB* – PP_0794 *fruK* – PP_0795 *fruA*; GAGD catalytic-Asp motif + Gly-rich loop).

**Refuted / excluded:**
- FruK is **not** a glycolytic 6-phosphofructokinase and does **not** act on fructose-6-phosphate (excluded by substrate specificity and family divergence from PfkA).
- The gene is **not** a mis-annotation of a different same-symbol gene: organism-specific literature confirms *P. putida* FruK identity.

---

## 7. Limitations and Future Directions

- **No enzyme-specific experimental study of *P. putida* Q88PQ4 itself** (kinetics, Km/kcat, structure) was located; the catalytic assignment rests on high-quality UniProt/Rhea annotation plus biochemistry of close orthologs (*E. coli*, *Xanthomonas*, *Aeromonas*, *Rhodobacter*).
- **Localization is inferred**, not experimentally demonstrated for this protein.
- **Possible moonlighting** (direct Cra binding, reverse FBP→F1P reaction) is documented only in *E. coli* FruK (PMID 38723750) and remains to be tested in *P. putida*.
- Future work: recombinant purification and steady-state kinetics of PP_0794; a crystal/AlphaFold-guided active-site analysis of the ribokinase-like fold; a ΔfruK strain growth/flux study on fructose vs. glucose; and testing whether *P. putida* FruK physically interacts with Cra.

---

## 8. Key References
- Yoon et al. 2021, *J Biol Chem*/*J Bacteriol* — PMID 33476373 (P. putida fru operon; FruK = 1-PFK; F1P inducer).
- Chavarría et al. 2014 — PMID 24918052 (F1P is the sole Cra effector; fruBKA operon).
- Chavarría et al. 2013, *Environ Microbiol* — PMID 23301697 (P. putida lacks 6-PFK; ED pathway exclusive).
- Pflüger & de Lorenzo 2008, *J Bacteriol* — PMID 18296519 (FruA/FruB = complete fructose PTS; C/N cross-talk).
- Weeramange et al. 2024 — PMID 38723750 (E. coli FruK reverse reaction & Cra binding; relevance to γ-proteobacteria).
- Wu et al. 1991 — PMID 1850730 (PfkB family definition).
- Orchard & Kornberg 1990 — PMID 1981619 (fruK vs pfkA/pfkB; fruFKA operon).
- de Crécy-Lagard et al. 1991 — PMID 1655739 (Xanthomonas FruK biochemistry).
- Binet et al. 1998 — PMID 9579084 (Aeromonas 1-PFK on PTS product).
- Molchanova et al. 1992 — PMID 1332910 (E. coli fruK essential for fructose growth).


## Artifacts

- [OpenScientist final report](fruK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fruK-deep-research-openscientist_artifacts/final_report.pdf)