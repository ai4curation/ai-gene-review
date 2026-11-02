---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:58:28.013193'
end_time: '2026-08-31T20:28:54.665065'
duration_seconds: 1826.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pyrF
  gene_symbol: pyrF
  uniprot_accession: Q88LW2
  protein_description: 'RecName: Full=Orotidine 5''-phosphate decarboxylase {ECO:0000255|HAMAP-Rule:MF_01200};
    EC=4.1.1.23 {ECO:0000255|HAMAP-Rule:MF_01200}; AltName: Full=OMP decarboxylase
    {ECO:0000255|HAMAP-Rule:MF_01200}; Short=OMPDCase {ECO:0000255|HAMAP-Rule:MF_01200};
    Short=OMPdecase {ECO:0000255|HAMAP-Rule:MF_01200};'
  gene_info: Name=pyrF {ECO:0000255|HAMAP-Rule:MF_01200}; OrderedLocusNames=PP_1815;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the OMP decarboxylase family. Type 1 subfamily.
  protein_domains: Aldolase_TIM. (IPR013785); OMPdecase. (IPR014732); OMPdecase_AS.
    (IPR018089); OMPdecase_bac. (IPR047596); OMPdeCOase_dom. (IPR001754)
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
  path: pyrF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pyrF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LW2
- **Protein Description:** RecName: Full=Orotidine 5'-phosphate decarboxylase {ECO:0000255|HAMAP-Rule:MF_01200}; EC=4.1.1.23 {ECO:0000255|HAMAP-Rule:MF_01200}; AltName: Full=OMP decarboxylase {ECO:0000255|HAMAP-Rule:MF_01200}; Short=OMPDCase {ECO:0000255|HAMAP-Rule:MF_01200}; Short=OMPdecase {ECO:0000255|HAMAP-Rule:MF_01200};
- **Gene Information:** Name=pyrF {ECO:0000255|HAMAP-Rule:MF_01200}; OrderedLocusNames=PP_1815;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the OMP decarboxylase family. Type 1 subfamily.
- **Key Domains:** Aldolase_TIM. (IPR013785); OMPdecase. (IPR014732); OMPdecase_AS. (IPR018089); OMPdecase_bac. (IPR047596); OMPdeCOase_dom. (IPR001754)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pyrF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pyrF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pyrF** (gene ID: pyrF, UniProt: Q88LW2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: pyrF (Q88LW2) — Orotidine 5′-Monophosphate Decarboxylase in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

| Field | Value |
|---|---|
| UniProt accession | Q88LW2 |
| Gene name | *pyrF* (OrderedLocusName PP_1815) |
| Organism | *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK |
| Protein | Orotidine 5′-phosphate decarboxylase (OMP decarboxylase; OMPDCase) |
| EC number | 4.1.1.23 |
| Family | OMP decarboxylase family, **Type 1 subfamily** (bacterial) |
| Fold/domains | (β/α)₈ TIM barrel; Aldolase_TIM (IPR013785); OMPdecase (IPR014732, IPR001754); OMPdecase_AS (IPR018089); OMPdecase_bac (IPR047596) |

**Identity is unambiguous.** The gene symbol *pyrF*, the EC number, the OMP-decarboxylase family assignment, and the TIM-barrel/OMPdecase domain architecture are mutually consistent and standard for this enzyme across all domains of life. There is no gene-symbol ambiguity: *pyrF* denotes OMP decarboxylase in bacteria (the eukaryotic ortholog is often fused with orotate phosphoribosyltransferase as *URA3*/UMPS). The findings below are drawn from primary and review literature on OMP decarboxylase (OMPDC/ODCase), with the *P. putida*-specific role inferred from the enzyme's conserved biochemistry and from genetics in the same organism.

---

## 1. Summary (Answer to the Research Question)

pyrF (Q88LW2) is **orotidine 5′-monophosphate decarboxylase (OMPDC, EC 4.1.1.23)**, a cytoplasmic metabolic enzyme that catalyzes the **cofactor-independent decarboxylation of orotidine 5′-monophosphate (OMP) to uridine 5′-monophosphate (UMP)** — the sixth and final step of the *de novo* pyrimidine nucleotide biosynthesis pathway. It is a highly substrate-specific enzyme (its natural substrate is OMP) and is renowned as one of the most catalytically proficient enzymes known. In *P. putida* KT2440 it supplies UMP, the common precursor of all pyrimidine nucleotides required for RNA, DNA, and activated-sugar metabolism.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction:** orotidine 5′-monophosphate (OMP) → uridine 5′-monophosphate (UMP) + CO₂.

OMPDC removes the carboxylate at C6 of the orotate ring of OMP, generating UMP. This is the terminal reaction of *de novo* pyrimidine biosynthesis, immediately downstream of orotate phosphoribosyltransferase (PyrE), which forms OMP from orotate and PRPP [PMID 21898650]. The reaction requires **no metal ion and no organic cofactor** — a defining and unusual feature for a decarboxylase [PMID 21870810].

**Substrate specificity.** The physiological substrate is OMP; catalysis is exquisitely tuned to the orotidine-monophosphate scaffold. The 5′-phosphate and ribosyl moieties provide most of the binding energy (used for conformational activation, see §4), while chemistry occurs at the orotate C6. The enzyme also acts on close analogs — e.g., it decarboxylates 5-fluoro-OMP (FOMP) faster than OMP, and binds transition-state analogs such as 6-hydroxy-UMP (BMP) and 6-aza-UMP extremely tightly — properties widely used to probe the mechanism [PMID 24559040]. This analog activity is biologically important: OMPDC converts **5-fluoroorotate-derived FOMP into toxic 5-fluoro-UMP**, the basis of 5-FOA counterselection (§6).

**Catalytic proficiency.** OMPDC is a benchmark for enzymatic power, with a rate acceleration k_cat/k_non = 7.1 × 10¹⁶ and catalytic proficiency (k_cat/K_M)/k_non = 4.8 × 10²² M⁻¹ — a rate enhancement exceeding 17 orders of magnitude over the uncatalyzed reaction [PMID 21870810; PMID 21898650]. For the natural substrate, decarboxylation is fully rate-determining [PMID 19435313].

---

## 3. Catalytic Mechanism

Despite the absence of cofactors, OMPDC achieves enormous rate enhancement through a combination of **ground-state destabilization** and **transition-state stabilization**:

- **Carbanion intermediate.** Decarboxylation proceeds through a stabilized vinyl carbanion/carbene intermediate at C6, which is subsequently protonated to give UMP [PMID 21870810; PMID 19435313].
- **Substrate (electrostatic) destabilization.** A conserved active-site aspartate is positioned next to the substrate carboxylate, creating unfavorable electrostatic repulsion that raises the ground-state energy and lowers the activation barrier; mutating this Asp (e.g., D70N/D70G in the *Methanothermobacter* enzyme, D91 in yeast) impairs decarboxylation while leaving product-exchange chemistry largely intact [PMID 19435314].
- **Conserved charged tetrad.** Catalysis depends on a conserved quartet of alternating charged residues (Lys–Asp–Lys–Asp; e.g., Lys44–Asp71–Lys73–Asp76 in *E. coli* pyrF numbering). Several of these positions are absolutely intolerant of substitution; the catalytic lysine serves as the general acid that protonates the C6 carbanion [PMID 21898650].
- **Non-classical chemistry via the catalytic Lys.** The active-site lysine can act as a nucleophile toward C6-substituted UMP derivatives, explaining alternate reactions and enabling mechanism-based inhibitor design [PMID 19472232].

---

### 3a. Strain-specific sequence evidence (PP_1815 / Q88LW2)

Direct analysis of the KT2440 protein sequence (233 aa) confirms it is a bona fide, active OMPDC. All hallmark catalytic elements are present and correctly positioned:

- **Catalytic charged tetrad:** Lys35 – Asp62 – Lys64 – Asp67 (a DxKxxD-type active-site signature; InterPro OMPdecase_AS, IPR018089), the ortholog of the experimentally validated E. coli Lys44–Asp71–Lys73–Asp76 quartet [PMID 21898650].
- **Proton donor:** UniProt annotates **Lys64** as the catalytic proton donor (general acid that protonates the C6 carbanion).
- **Substrate-anchoring residues** at positions 13, 35, 62–71, 122, 182, 191, 211, 212 coordinate the 5′-phosphate/ribose moiety.
- **Reaction (UniProt):** orotidine 5′-phosphate + H⁺ = UMP + CO₂; pathway assignment "UMP biosynthesis via de novo pathway; UMP from orotate: step 2/2."
- **No signal peptide or transmembrane segments** → consistent with a soluble cytoplasmic enzyme.

## 4. Structure and the Role of Substrate Binding Energy

OMPDC adopts the classic **(β/α)₈ TIM-barrel fold** (Aldolase_TIM, IPR013785) and functions as a **homodimer**, with each active site completed at the subunit interface. A key catalytic principle is that the enzyme uses the **intrinsic binding energy of the substrate's 5′-phosphate group** — remote from the site of chemistry — to drive loop-closure/conformational changes that move catalytic side chains into positions complementary to the reaction transition state [PMID 41115254]. Because unliganded active sites are not pre-organized for the transition state, this substrate-driven "phosphate-gripper" activation is essential for the full rate enhancement [PMID 41115254; PMID 29595949]. Extensive mutagenesis, MD simulation, and X-ray structures of substrate/inhibitor complexes support this model [PMID 24559040; PMID 21870810].

---

## 5. Pathway Context and Biological Process

pyrF catalyzes the last of the six committed steps of **de novo pyrimidine biosynthesis** (carbamoyl-phosphate → carbamoyl-aspartate → dihydroorotate → orotate → OMP → **UMP**). UMP is the universal precursor from which all pyrimidine nucleotides are derived (UMP → UDP → UTP → CTP; and via reduction/methylation to dCTP and dTTP). Thus pyrF activity is required for RNA and DNA synthesis, phospholipid and cell-wall precursor synthesis (UDP-sugars), and general growth whenever exogenous pyrimidines are not available for salvage [PMID 21898650, PMID 24361203]. Loss-of-function in pyrF produces **uracil/pyrimidine auxotrophy**. In *P. putida* KT2440, an aerobic soil bacterium of major biotechnological interest, this pathway provides the pyrimidine building blocks that support its robust growth and metabolic versatility.

---

### 5a. Genomic organization in KT2440

In the KT2440 chromosome, *pyrF* (PP_1815) is **not** embedded in a *pyr* operon. Its immediate neighbors are functionally unrelated genes — PP_1813 (ComEA-related protein), PP_1814 (DUF2897 family protein), PP_1816 (zinc-containing alcohol dehydrogenase), PP_1817 (short-chain dehydrogenase/reductase) — and no other *de novo* pyrimidine genes (*pyrB, pyrC, pyrD, pyrE*) are adjacent. This indicates *pyrF* is a dispersed, apparently monocistronic gene, consistent with the scattered, individually regulated arrangement of pyrimidine-biosynthesis genes typical of *Pseudomonas* and most Gram-negative bacteria.

## 6. Localization and Biotechnological Relevance

**Subcellular localization: cytoplasm.** OMPDC is a soluble metabolic enzyme with no signal peptide or transmembrane segments; it carries out its function in the cytosol as part of the nucleotide-biosynthetic machinery (consistent with HAMAP-Rule MF_01200 and the OMP decarboxylase family).

**Essentiality and druggability.** OMPDC is an essential "choke-point" enzyme of *de novo* pyrimidine biosynthesis: when pyrimidine salvage substrates are unavailable, it provides the sole route to UMP, so loss of *pyrF* forces pyrimidine auxotrophy. Metabolic-network analyses prioritize OMPDC as a validated antimicrobial drug target because in pathogens (e.g., *Plasmodium falciparum* PfODCase) it is sequentially and structurally distinct from the human enzyme [PMID 23859267]. Its narrow specificity for the phosphoribosyl-pyrimidine core is reflected in the exceptionally tight binding of transition-state/product analogs such as 6-hydroxy-UMP (BMP) and 6-aza-UMP.

**pyrF as a genetic tool.** Because a functional pyrF also converts 5-fluoroorotic acid (5-FOA, via FOMP) into cytotoxic 5-fluoro-UMP, pyrF is a classic **counterselectable marker**: pyrF⁺ cells die on 5-FOA whereas pyrF-deletion mutants survive, enabling scarless/markerless genome editing. The same pyrimidine-metabolism counterselection principle (using *upp*/5-fluorouracil) has been implemented in *P. putida* KT2440 for genome reduction and pathway engineering [PMID 25828098], underscoring the practical importance of this enzyme class in *Pseudomonas* synthetic biology.

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- pyrF/Q88LW2 = OMP decarboxylase (EC 4.1.1.23) catalyzing OMP → UMP (final de novo pyrimidine step). ✔ (family, domains, EC, literature all concordant)
- Cofactor-independent, extremely proficient catalysis via a stabilized carbanion intermediate. ✔ [PMID 21870810, 19435313]
- Conserved Lys–Asp–Lys–Asp catalytic tetrad in a TIM-barrel; substrate-binding-energy-driven conformational activation. ✔ [PMID 21898650, 41115254]
- Cytoplasmic localization; usable as a 5-FOA counterselection marker. ✔

**Refuted / ruled out:**
- Gene-symbol ambiguity was considered and **rejected**: *pyrF* consistently denotes bacterial OMP decarboxylase; no conflicting gene shares this symbol/family for this protein.
- A cofactor- or metal-dependent mechanism is **refuted** by the established cofactor-free chemistry [PMID 21870810].

---

## 8. Limitations and Future Directions

- No *P. putida* KT2440–specific enzymological or structural study of PP_1815 was located; the mechanistic and structural conclusions are inferred from highly conserved orthologs (E. coli, yeast, *Methanothermobacter*, human) and from the strong sequence/domain conservation captured by HAMAP MF_01200. Direct kinetic characterization of the KT2440 enzyme and an experimental structure would strengthen strain-specific claims.
- Because *pyrF* (PP_1815) is a dispersed, apparently monocistronic gene rather than part of a *pyr* operon, its precise transcriptional regulation and flux control in KT2440 remain uncharacterized and merit follow-up (e.g., promoter mapping, response to pyrimidine availability).

---

*Prepared from primary and review literature (PubMed) and UniProt/InterPro annotation. Key references: PMID 21870810, 21898650, 29595949, 19435314, 19435313, 19472232, 24559040, 41115254, 24361203, 25828098, 23859267.*


## Artifacts

- [OpenScientist final report](pyrF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pyrF-deep-research-openscientist_artifacts/final_report.pdf)