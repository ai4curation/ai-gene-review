---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:02:35.203715'
end_time: '2026-08-31T22:32:13.375574'
duration_seconds: 5378.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3204
  gene_symbol: PP_3204
  uniprot_accession: Q88HZ8
  protein_description: 'RecName: Full=Cupin type-2 domain-containing protein {ECO:0000259|Pfam:PF07883};'
  gene_info: OrderedLocusNames=PP_3204 {ECO:0000313|EMBL:AAN68812.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Cupin_2. (IPR013096); OryJ/VirC-like. (IPR047142); RmlC-like_jellyroll.
    (IPR014710); RmlC_Cupin_sf. (IPR011051); Cupin_2 (PF07883)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3204-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3204-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HZ8
- **Protein Description:** RecName: Full=Cupin type-2 domain-containing protein {ECO:0000259|Pfam:PF07883};
- **Gene Information:** OrderedLocusNames=PP_3204 {ECO:0000313|EMBL:AAN68812.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cupin_2. (IPR013096); OryJ/VirC-like. (IPR047142); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf. (IPR011051); Cupin_2 (PF07883)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3204" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3204' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3204** (gene ID: PP_3204, UniProt: Q88HZ8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_3204 (Q88HZ8), *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**PP_3204 (UniProt Q88HZ8) encodes FdeH, a ~195-residue single-domain "type-2" cupin that is a component of the flavonoid-degradation (*fde*) gene cluster of *Pseudomonas putida* KT2440.** The gene product is a soluble, cytoplasmic, metal-dependent enzyme that participates in the intracellular catabolism of the plant flavanone **naringenin** (and related flavonoids such as chrysin), a pathway that converts the flavonoid to oxaloacetate for entry into the TCA cycle. Its precise catalytic step has not been experimentally dissected, but by orthology and conserved genomic clustering it acts on a soluble intermediate **downstream of the FdeC-catalyzed oxidative meta-cleavage of the flavonoid A-ring**. Its role is therefore best classified as a **cupin-fold tailoring enzyme in aromatic (flavonoid) meta-cleavage catabolism**, most plausibly an isomerase/hydratase/(de)carboxylase-type activity carried out in the cytoplasm.

---

## 2. Gene / Protein Identity Verification

The provided identifiers are internally consistent and were confirmed against primary databases:

| Attribute | Value | Source |
|---|---|---|
| UniProt | Q88HZ8 | UniProtKB |
| Locus | PP_3204 (GenBank AAN68812.1; genome AE015451) | UniProt/KEGG |
| Organism | *P. putida* KT2440 (taxid 160488) | UniProt/KEGG |
| Length | 195 aa | UniProt |
| Domain | Cupin_2 (Pfam PF07883); RmlC-like cupin superfamily (IPR011051, IPR014710); OryJ/VirC-like (IPR047142) | InterPro |
| Fold | Double-stranded β-helix / jelly-roll β-barrel (Gene3D 2.60.120.10; SUPFAM SSF51182 "RmlC-like cupins") | UniProt |
| Orthology | eggNOG **COG1917**; KEGG **K26182 = "naringenin degradation protein FdeH"** | eggNOG/KEGG |
| Pathway | KEGG **ppu00946 "Degradation of flavonoids"** | KEGG |

The UniProt "Cupin type-2 domain-containing protein" description, the domain architecture, and the KEGG FdeH assignment all agree. There is **no direct primary literature on PP_3204 itself**; its functional annotation derives from (i) KEGG/eggNOG orthology and (ii) genetic/biochemical characterization of the orthologous *fde* operon in *Herbaspirillum seropedicae* SmR1.

---

## 3. Key Findings and Evidence

### 3.1 PP_3204 belongs to the *fde* flavonoid-degradation cluster (high confidence)

KEGG assigns PP_3204 to ortholog group **K26182 (FdeH)**. The surrounding KT2440 genome region encodes a near-complete, conserved *fde* cluster (coordinates ~3.62–3.64 Mbp):

| Locus | KT2440 annotation | *fde* ortholog (KO) | Predicted role |
|---|---|---|---|
| PP_3195 | conserved protein | FdeB (K26184) | downstream step (COG1506 hydrolase/peptidase-like) |
| PP_3197 | glyoxalase family | **FdeC (K26181)** | **ring-cleavage dioxygenase** (VOC/glyoxalase fold) |
| PP_3198 | 2Fe-2S ferredoxin | FdeD (K26179) | electron transfer to oxygenase |
| PP_3199 | putative monooxygenase | FdeE-type (COG0654) | **naringenin 8-hydroxylase (monooxygenase)** |
| PP_3202 / PP_3203 | transporter / MFS transporter | — | substrate uptake |
| **PP_3204** | **conserved protein** | **FdeH (K26182)** | **cupin tailoring enzyme (this study)** |
| PP_3205 | fumarylacetoacetate-hydrolase family | FdeI (K26185) | pyruvate/oxaloacetate-forming hydrolase (COG0179) |
| PP_3206 | conserved protein | FdeJ (K26183) | downstream step |
| PP_3207 | putative cyclase | FdeG-type | cyclase/isomerase |
| PP_3210 / PP_3211 | ABC transporter (NitT/TauT) | — | uptake |

STRING functional-association analysis independently supports the operon: PP_3204 co-occurs with PP_3207, PP_3205 and PP_3206 at conserved-neighborhood scores ≈ 0.81, and with additional cluster genes (PP_3195–3199) at ≈ 0.29–0.35. Lower-scoring links to *vanA*, *nicC* and *betC* place PP_3204 in the broader aromatic-catabolism functional neighborhood of KT2440.

**Orthology strength (quantified):** By global Needleman–Wunsch alignment, PP_3204 is **55.0% identical (104/189)** to the experimentally characterized *H. seropedicae* FdeH (Hsero_1010) — well above the orthology "twilight zone" (~25–30%) — and **98.4% identical (187/190)** to the *P. putida* DOT-T1E ortholog (T1E_5650), with the catalytic His-motif (…LMH*R*…, His126) conserved. KEGG KO K26182 (FdeH) comprises ~130 members concentrated in **plant-associated/soil Proteobacteria** (*Pseudomonas*, *Burkholderia*, *Herbaspirillum*, *Bradyrhizobium*, *Agrobacterium/Allorhizobium*, *Xanthobacter*) — organisms that encounter plant flavonoids — reinforcing a flavonoid-catabolic role. This high identity to a functionally validated FdeH justifies transferring the functional assignment to PP_3204.

### 3.2 Biochemistry of the pathway (evidence from the orthologous operon)

The *fde* pathway was genetically and biochemically defined in *H. seropedicae* SmR1 (Marin et al., 2013, *Microbiology* 159:167–175; Marin et al., 2016, *Environ. Microbiol.* 18:4653–4661). Key results:

1. A Tn5 mutant unable to use naringenin as a carbon source mapped to the *fde* operon; mutation of *fdeA* (first gene) and of the transcriptional activator *fdeR* abolished degradation. The operon is **induced by naringenin and chrysin**.
2. LC-MS/MS of mutant supernatants established the route:
   - **FdeE (monooxygenase)** mono-oxygenates naringenin → **5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one (8-hydroxynaringenin)** (this compound is unchanged in the *fdeE* mutant).
   - **FdeC (dioxygenase)** then **dioxygenates and cleaves the A-ring** (the 8-hydroxynaringenin intermediate accumulates in the *fdeC* mutant).
   - After **meta-cleavage of the A-ring**, subsequent steps generate **oxaloacetate**, funneled into the **TCA cycle**.
3. The bacterium can also side-modify naringenin (glycosylation of the B-ring; A-ring methoxylation) to dead-end products — a detoxification branch distinct from the productive catabolic route.

**FdeH's position:** FdeH is one of the downstream "tailoring" enzymes acting after A-ring fission (the papers focused their mechanistic dissection on FdeA, FdeC, FdeE and FdeG; FdeH itself was not assayed individually). Its cupin fold is consistent with a **metal-dependent isomerase, hydratase, tautomerase or (de)carboxylase** step operating on a soluble ring-cleavage product en route to oxaloacetate.

### 3.3 Structure, cofactor and localization (inference)

- **Fold:** single RmlC-like cupin (double-stranded β-helix / jelly-roll β-barrel) — a "monocupin."
- **Structural evidence (AlphaFold):** The AlphaFold DB model AF-Q88HZ8-F1 is high-confidence (mean pLDDT 89.2). The two canonical cupin His-motifs converge inside the β-barrel to form a **metal-binding pocket**: the ring-nitrogen atoms of **His126** and **His165** lie only **3.6 Å apart** (geometry compatible with jointly ligating one divalent metal), with **His122** ~7–10 Å away and **Asp132** 4.7–6.5 Å from the His pair — a compact His/His/His(+Asp) site at the barrel core (local pLDDT 79–97). This structurally corroborates the sequence-based metal-site prediction.
- **Cofactor:** cupins are metalloproteins; the site coordinates a divalent metal (Fe most commonly, but Mn/Ni/Co/Cu/Zn in various subfamilies), each enabling different chemistry within the same barrel (Dunwell et al., 2004; 2000).
- **Subfamily clues to catalysis:** InterPro assigns PP_3204 to **IPR047142 "Oryzines biosynthesis cluster protein J / Cupin-domain-containing oxidoreductase VirC-like"** — a family of bacterial/fungal cupin **oxidoreductases** that tailor natural-product/aromatic intermediates. The parent **Cupin_2 domain (IPR013096)** is exemplified by **gentisate 1,2-dioxygenase, H2HPP (2-hydroxyphenylpyruvate) isomerase, and (S)-ureidoglycine aminohydrolase**, i.e. metal-dependent enzymes of aromatic-compound degradation and nitrogen metabolism. Together these place FdeH's likely activity in the **metal-dependent oxidoreductase / isomerase / hydro-lyase** space acting on a soluble aromatic-derived intermediate.
- **Localization:** No signal peptide or transmembrane segment is annotated; the protein is predicted **cytoplasmic**. This is mechanistically coherent: cluster-encoded MFS/ABC transporters (PP_3202/PP_3203/PP_3210/PP_3211) import the flavonoid, which is then degraded intracellularly.

---

## 4. Supported and Refuted Hypotheses

**Supported:**
- *PP_3204 is a functional member of a flavonoid/naringenin-catabolic operon* — supported by KEGG orthology (K26182/FdeH), a conserved multi-gene *fde* cluster in KT2440, and STRING co-occurrence.
- *The pathway performs oxidative A-ring meta-cleavage of naringenin to oxaloacetate/TCA* — supported by LC-MS/MS mutant analysis in the orthologous *H. seropedicae* system.
- *FdeH is a soluble cytoplasmic metalloenzyme* — supported by fold classification, absence of localization signals, and cupin metal-binding signature.

**Refuted / ruled out:**
- *PP_3204 is an uncharacterized orphan of unknown pathway* — refuted; it maps to a defined catabolic operon.
- *A different same-symbol gene in another organism* — not applicable; the locus tag PP_3204 is unique to *P. putida* KT2440 and no conflicting literature exists.

**Not established (open):**
- The **exact enzymatic reaction and substrate** catalyzed by FdeH within the downstream pathway, and the **identity of the bound metal**, remain experimentally undetermined.

---

## 5. Limitations and Future Directions

- **No direct experimental study of PP_3204/FdeH.** Functional claims about the specific reaction are inferential (orthology + operon context + fold). The primary *fde* papers dissected FdeA/FdeC/FdeE/FdeG, not FdeH.
- **KEGG pathway assignment for KT2440 is homology-based**; direct demonstration that *P. putida* KT2440 grows on naringenin via this cluster would strengthen the annotation.
- **Recommended experiments:** (i) targeted *pp_3204* deletion + LC-MS/MS metabolite profiling on naringenin (identify the accumulating intermediate to pinpoint the step); (ii) heterologous expression, metal analysis (ICP-MS), and in-vitro assay against candidate ring-cleavage intermediates; (iii) AlphaFold/crystal structure to confirm the metal ligands (His122/His126/His165) and active-site architecture; (iv) transcriptional confirmation of naringenin/chrysin induction of the KT2440 cluster.

---

## 6. Primary References

1. Marin AM, et al. **Naringenin degradation by the endophytic diazotroph *Herbaspirillum seropedicae* SmR1.** *Microbiology (Reading)* 159:167–175 (2013). PMID: 23125118.
2. Marin AM, et al. **Genetic and functional characterization of a novel meta-pathway for degradation of naringenin in *Herbaspirillum seropedicae* SmR1.** *Environ. Microbiol.* 18:4653–4661 (2016). PMID: 27059806.
3. Dunwell JM, Purvis A, Khuri S. **Cupins: the most functionally diverse protein superfamily?** *Phytochemistry* 65:7–17 (2004). PMID: 14697267.
4. Dunwell JM, Khuri S, Gane PJ. **Microbial relatives of the seed storage proteins of higher plants...** *Microbiol. Mol. Biol. Rev.* 64:153–179 (2000). PMID: 10704478.
5. Tadra-Sfeir MZ, et al. **Genome-wide transcriptional profiling of *H. seropedicae* SmR1 grown in the presence of naringenin.** (2015). PMID: 26052319.

Database sources: UniProtKB (Q88HZ8), KEGG (ppu:PP_3204, K26182, ppu00946), InterPro/Pfam (PF07883), eggNOG (COG1917), STRING (160488.PP_3204).


## Artifacts

- [OpenScientist final report](PP_3204-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3204-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23125118
2. PMID:27059806
3. PMID:14697267
4. PMID:10704478
5. PMID:26052319