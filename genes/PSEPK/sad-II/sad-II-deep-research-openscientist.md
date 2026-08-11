---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T04:22:52.388936'
end_time: '2026-08-11T05:10:29.142469'
duration_seconds: 2856.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sad-II
  gene_symbol: sad-II
  uniprot_accession: Q88I50
  protein_description: 'SubName: Full=NAD+-dependent succinate semialdehyde dehydrogenase
    {ECO:0000313|EMBL:AAN68759.1}; EC=1.2.1.24 {ECO:0000313|EMBL:AAN68759.1};'
  gene_info: Name=sad-II {ECO:0000313|EMBL:AAN68759.1}; OrderedLocusNames=PP_3151
    {ECO:0000313|EMBL:AAN68759.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aldehyde dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_CYS.
    (IPR016160); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)
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
  path: sad-II-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sad-II-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I50
- **Protein Description:** SubName: Full=NAD+-dependent succinate semialdehyde dehydrogenase {ECO:0000313|EMBL:AAN68759.1}; EC=1.2.1.24 {ECO:0000313|EMBL:AAN68759.1};
- **Gene Information:** Name=sad-II {ECO:0000313|EMBL:AAN68759.1}; OrderedLocusNames=PP_3151 {ECO:0000313|EMBL:AAN68759.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_CYS. (IPR016160); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sad-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sad-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sad-II** (gene ID: sad-II, UniProt: Q88I50) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *sad-II* (PP_3151, UniProt Q88I50)
### NAD⁺-dependent succinic semialdehyde dehydrogenase of *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**sad-II** (locus **PP_3151**; UniProt **Q88I50**) of *Pseudomonas putida* KT2440 encodes a
**NAD⁺-dependent succinic semialdehyde dehydrogenase (SSADH; EC 1.2.1.24)**. Its primary,
experimentally-supported (by homology) function is to catalyze the essentially irreversible,
NAD⁺-coupled oxidation of **succinic semialdehyde (SSA) → succinate**. This is the **terminal step
of the γ-aminobutyrate (GABA) shunt / polyamine-catabolic route**, the reaction that links the
degradation of GABA and biogenic amines (e.g., putrescine, spermidine) to the **tricarboxylic acid
(TCA) cycle**. The enzyme is a **soluble cytoplasmic** aldehyde dehydrogenase that uses a **catalytic
cysteine nucleophile** and NAD⁺ hydride acceptor. It belongs to the **Sad/YneI (NAD⁺-preferring)
class** of bacterial SSADHs, distinct from the NADP⁺-preferring GabD class.

---

## 2. Gene / Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88I50 | UniProtKB |
| Gene name | *sad-II* | EMBL AAN68759.1 |
| Locus tag | PP_3151 | KT2440 genome |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | UniProtKB |
| Length | 461 aa | UniProtKB |
| EC number | 1.2.1.24 (SSADH, NAD⁺) | UniProtKB |
| Family | Aldehyde dehydrogenase superfamily | UniProtKB / InterPro |
| Domains | Ald_DH_N (IPR016162), Ald_DH_C (IPR016163), Ald_DH_CS_CYS (IPR016160), Aldehyde_DH_dom / PF00171 | InterPro / Pfam |
| Functional subfamily | **GABD/Sad-like (IPR047110)**, **ALDH_GabD1-like (IPR044148)** | InterPro |
| GO molecular function | GO:0004777 succinate-semialdehyde dehydrogenase (NAD⁺) activity; GO:0004030 aldehyde dehydrogenase [NAD(P)⁺] activity | UniProtKB/InterPro |

**Verification outcome:** The gene symbol *sad-II*, EC number, organism, protein family, and all
listed InterPro domains are internally consistent and match the SSADH function. This report describes
the correct protein. The name "*sad*" (**s**uccinic semialdehyde **d**ehydrogenase) corresponds to
the *E. coli* *sad*/*yneI* gene; the "**II**" denotes one of multiple SSADH paralogs in the KT2440
genome. *No ambiguity or misidentification was encountered.*

---

## 3. Primary Function: Reaction Catalyzed and Substrate Specificity

### 3.1 Reaction
> Succinic semialdehyde + NAD⁺ + H₂O → succinate + NADH + 2 H⁺

Succinic semialdehyde dehydrogenases "catalyze the NAD(P)⁺-coupled oxidation of succinic semialdehyde
(SSA) to succinate, the last step of the γ-aminobutyrate shunt" (de Carvalho *et al.*, 2011, PMID
21303655). The reaction is physiologically irreversible and both **detoxifies** the reactive
aldehyde SSA and **generates** the TCA-cycle intermediate succinate plus reducing equivalents (NADH).

### 3.2 Substrate specificity
SSADHs of this family are **highly specific for succinic semialdehyde** rather than general aldehydes,
and act with micromolar affinity:
- Characterized NAD⁺-type SSADH (Arabidopsis, a strict structural/functional analog): "specific for
  succinic semialdehyde (K₀.₅ = 15 µM), and exclusively used NAD⁺ as a cofactor (Km = 130 ± 77 µM)"
  with NADH a competitive inhibitor (Busch & Fromm, 1999, PMID 10517851).
- Bacterial Sad/YneI-type homolog: "shows high activity and affinity toward succinate semialdehyde
  and exhibits **substrate inhibition** at concentrations of SSA higher than 0.1 mM" (Zheng *et al.*,
  2013, PMID 23229889).

By inference, Q88I50 acts specifically on the 4-carbon SSA with micromolar affinity, using NAD⁺, with
likely substrate/product inhibition that limits flux and prevents accumulation of toxic SSA.

### 3.3 Cofactor specificity — why "NAD⁺-dependent"
Bacteria typically encode **two SSADH paralogs of distinct cofactor preference**: "Genomes of many
organisms including *Escherichia coli* and *Salmonella typhimurium* encode two succinate semialdehyde
dehydrogenases with low sequence similarity and different cofactor preference (**YneI and GabD**)"
(Zheng *et al.*, 2013, PMID 23229889). The **Sad/YneI** class prefers NAD⁺ (a conserved Lys — Lys160
in YneI — "contributes to the enzyme preference to NAD(⁺)"), whereas the **GabD** class prefers NADP⁺;
structurally, "a deletion of three amino acids in *E. coli* SSADH permits this enzyme to use NADP⁺,
whereas … the human enzyme utilises NAD⁺" (Langendorf *et al.*, 2010, PMID 20174634). Q88I50 is
classified **GABD/Sad-like (IPR047110)** and annotated **NAD⁺-dependent (EC 1.2.1.24)**, placing it in
the NAD⁺-preferring Sad branch — consistent with its "*sad*" name and distinct from the genome's
NADP⁺-preferring GabD paralogs (see §3.4).

### 3.4 Genomic context — two SSADH systems in KT2440 (KEGG analysis)
Genome analysis of *P. putida* KT2440 shows a clear division of labor, which explains the "**-II**" in
the gene name:

| Locus | Symbol | KO | Cofactor / EC | Genomic context |
|---|---|---|---|---|
| **PP_3151** | **sad-II** | **K08324** | **NAD⁺ (EC 1.2.1.24)** | **standalone**, adjacent to **PP_3152 = yneJ** (LysR regulator) |
| PP_0213 | gabD-I | K00135 | NADP⁺ (EC 1.2.1.79/1.2.1.16) | in a **gabD-I–gabT operon** (PP_0214 = 4-aminobutyrate aminotransferase, K14268) |
| PP_2488 | (gabD-like) | K00135 | NADP⁺ | ALDH paralog |
| PP_4422 | (gabD-like) | K00135 | NADP⁺ | ALDH paralog |

- **sad-II (PP_3151)** is the *sole* NAD⁺-preferring (Sad/YneI-type, K08324) SSADH in the genome; it is a
  **standalone** gene at complement(3,569,479–3,570,864), **not** co-transcribed with a *gabT* gene.
- Its immediate neighbor **PP_3152 (yneJ)** is a **LysR-family transcriptional regulator**, exactly
  reproducing the *E. coli* **sad(yneI)–yneJ** chromosomal arrangement. This conserved synteny
  independently confirms PP_3151 as the genuine **Sad/YneI ortholog** and nominates YneJ as a candidate
  regulator of sad-II. Coordinates confirm *sad-II* is **monocistronic** and **divergently transcribed**
  from *yneJ*: PP_3151 is on the minus strand (complement 3,569,479–3,570,864) while PP_3152/*yneJ* is on
  the plus strand (3,570,972–3,571,838), the two genes reading head-to-head across a short (~108 bp)
  shared intergenic region — the **canonical LysR regulatory topology** (LysR regulators are typically
  encoded divergently from the target they control), strengthening the case that YneJ directly regulates
  *sad-II* independently of the *gab* operon.
- In contrast, the classical GABA-shunt pair is **gabD-I (PP_0213, NADP⁺-SSADH) + gabT (PP_0214,
  GABA aminotransferase)**, encoded in a single operon — the route that transaminates GABA to SSA and
  oxidises it. The existence of this separate, operon-linked NADP⁺ system underscores that **sad-II is a
  distinct, independently regulated NAD⁺-dependent isozyme**.

**KEGG pathway membership of sad-II (PP_3151):** Butanoate metabolism (ppu00650; the GABA-shunt module),
Alanine/aspartate/glutamate metabolism (ppu00250; GABA metabolism), and Nicotinate/nicotinamide
metabolism (NAD⁺/NADH cofactor turnover).

---

## 4. Catalytic Mechanism and Active-Site Residues (structural / bioinformatic evidence)

Sequence analysis of Q88I50 identifies the hallmark aldehyde-dehydrogenase catalytic machinery:

- **Catalytic cysteine — Cys267** in the motif `QNTGQV`**`C`**`AAAKR`. This aligns with the
  experimentally validated catalytic **Cys268 of *Salmonella* YneI**, where "the NAD⁺ molecule is
  bound in the long channel with its nicotinamide ring positioned close to the side chain of the
  catalytic Cys268" (Zheng *et al.*, 2013, PMID 23229889).
- **Coenzyme-binding / Rossmann glutamate motif** `ELGGSDPF` (residues 233–240).
- **Aldehyde-binding motif** `MPWNFP` (residues 133–138).
- Single **Aldehyde dehydrogenase domain** spanning residues 12–456 (UniProt), i.e., an N-terminal
  NAD-binding (Rossmann) subdomain plus a C-terminal catalytic subdomain — the classic two-domain ALDH
  architecture with the active site at the interdomain interface.

**Quantitative alignment evidence (this work).** Global Needleman–Wunsch (BLOSUM62) alignment of Q88I50
against experimentally characterized SSADHs shows it is **~2× more similar to the Sad/YneI class than to
GabD**: 64.3% identity to *Salmonella* YneI (Q8ZPI3, the enzyme crystallized by Zheng *et al.* 2013),
66.3% to *E. coli* Sad/YneI (P76149), but only 35.0% to *E. coli* GabD (P25526). Critically, **every
functionally validated YneI residue is conserved at the aligned position in Q88I50**:

| YneI (Zheng 2013) | Role | Aligned residue in Q88I50 |
|---|---|---|
| Cys268 | Catalytic nucleophile | **Cys267** (conserved) |
| Trp136 | Active-site / substrate | **Trp135** (conserved) |
| Glu365 | General base (deacylation) | **Glu364** (conserved) |
| Asp426 | Active site | **Asp425** (conserved) |
| **Lys160** | **NAD⁺ vs NADP⁺ preference determinant** | **Lys159** (conserved) |

The perfect conservation of the catalytic tetrad **and** of the Lys that "contributes to the enzyme
preference to NAD(⁺)" (Zheng *et al.*, 2013, PMID 23229889) provides residue-level structural evidence
that Q88I50 is a genuine **NAD⁺-preferring Sad/YneI-type SSADH**, rationalizing its EC 1.2.1.24
annotation.

**Chemical mechanism** (established for the close homolog GabD1 and shared by the family): the Cys
thiol performs nucleophilic addition to the SSA carbonyl to form a **thiohemiacetal**; a **hydride is
transferred to NAD⁺** to give a covalent **thioacyl-enzyme** intermediate; **thioester hydrolysis**
then releases succinate. "Nucleophilic addition to SSA is very fast, followed by a modestly
rate-limiting hydride transfer and fast thioester hydrolysis," with product dissociation/conformational
change being rate-limiting (de Carvalho *et al.*, 2011, PMID 21303655). Family SSADHs are homotetramers.

---

## 5. Biological Pathway Context

### 5.1 The GABA shunt / biogenic-amine catabolic funnel
SSADH provides the **catabolic exit** of the two-step GABA shunt:

1. GABA + 2-oxoglutarate → **succinic semialdehyde** + L-glutamate (GABA aminotransferase, GabT)
2. **Succinic semialdehyde** + NAD⁺ → **succinate** + NADH **(SSADH = Q88I50)**
3. Succinate enters the **TCA cycle**.

### 5.2 Relevance in *Pseudomonas putida*
*P. putida* is a metabolically versatile soil bacterium that degrades **biogenic amines**
(polyamines such as **putrescine and spermidine**, plus other amines) as growth substrates: "*Pseudomonas*
species can grow in media containing different BAs as carbon and energy sources, a reason why these
bacteria are excellent models for studying such catabolic pathways" (Luengo & Olivera, 2020, PMID
31912965). In these routes putrescine is converted (via GABA) to succinic semialdehyde, which SSADH
oxidizes to succinate — allowing the bacterium to use these nitrogenous compounds as **carbon,
nitrogen and energy sources** while detoxifying the reactive aldehyde intermediate. Thus sad-II
funnels the degradation of GABA and polyamines into central carbon metabolism.

### 5.3 Physiological significance: detoxification + redox + anaplerosis
The single reaction catalyzed by sad-II serves three linked physiological purposes:
1. **Aldehyde detoxification** — SSADHs are "essential for preventing accumulation of toxic levels of
   succinic semialdehyde (SSA) in cells" (Langendorf *et al.*, 2010, PMID 20174634); clearing this
   reactive aldehyde protects the cell.
2. **Energy conservation (redox)** — the oxidation reduces NAD⁺ to **NADH**, feeding reducing
   equivalents into the respiratory chain.
3. **Carbon assimilation / anaplerosis** — the product **succinate** enters the TCA cycle, letting
   GABA/polyamine carbon be used for growth.
Because NAD⁺ reduction and thioester hydrolysis make the reaction thermodynamically favorable and
effectively irreversible, sad-II acts as a committed, one-way catabolic exit.

### 5.4 Regulatory/signaling note
In some bacteria the intracellular SSA level set by SSADH activity acts as a signal (e.g., succinic
semialdehyde couples stress response to quorum-sensing signal decay in *Agrobacterium tumefaciens*,
where SSADH activity "might control the intracellular SSA level"; Wang *et al.*, 2006, PMID 16942602).
While such a signaling role has not been demonstrated for PP_3151 specifically, it illustrates that
SSADH activity governs a metabolically important pool of SSA. In KT2440, *sad-II* is likely under
control of the divergently encoded LysR regulator **YneJ (PP_3152)** (see §3.4).

---

## 6. Subcellular Localization

Q88I50 comprises a single soluble aldehyde-dehydrogenase domain (residues 12–456) with **no signal
peptide and no transmembrane segment**. Bacterial SSADHs are **cytoplasmic**; the eukaryotic
orthologs are soluble matrix enzymes (e.g., plant SSADH is localized to the mitochondrial matrix;
Busch & Fromm, 1999, PMID 10517851). The enzyme therefore carries out its reaction in the **bacterial
cytoplasm**, where GABA-shunt and polyamine-catabolism intermediates are generated.

---

## 7. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| Q88I50 catalyzes SSA → succinate (EC 1.2.1.24) | **Supported** | UniProt/GO annotation; family definition (PMID 21303655) |
| Uses a catalytic Cys nucleophile + NAD⁺ hydride acceptor | **Supported** | Cys267 alignment to YneI Cys268 (PMID 23229889); mechanism (PMID 21303655) |
| Belongs to the NAD⁺-preferring Sad/YneI class (vs. NADP⁺ GabD) | **Supported** | InterPro GABD/Sad-like; EC 1.2.1.24; two-paralog system (PMIDs 23229889, 20174634) |
| Specific for succinic semialdehyde with µM affinity | **Supported (by homology)** | PMIDs 10517851, 23229889 |
| Functions in cytoplasm as terminal step of GABA/polyamine catabolism feeding TCA | **Supported** | Pathway definition (PMID 21303655); Pseudomonas BA catabolism (PMID 31912965); no signal peptide |
| Q88I50 is closer to Sad/YneI than GabD at sequence level | **Supported** | Global alignment: 64–66% id to Sad/YneI vs 35% to GabD (this work) |
| NAD⁺-specificity determinant (YneI Lys160) is conserved | **Supported** | Lys159 conserved at aligned position (this work; PMID 23229889) |
| *sad-II* is regulated separately from the *gab* operon (by YneJ) | **Supported (inference)** | Monocistronic gene divergent from LysR *yneJ*; distinct from gabD-I–gabT operon (KEGG genome context, this work) |
| Direct biochemical characterization of PP_3151 itself | **Not available** | No primary study of this exact locus found; annotation rests on strong homology |

---

## 8. Limitations and Future Directions

- **No primary biochemical or structural study of PP_3151 itself** was located in the available
  literature; the functional assignment is a robust **inference from family membership, conserved
  active-site residues, and characterized orthologs** (E. coli/Salmonella YneI & GabD, human, plant,
  *M. tuberculosis* GabD1).
- The **exact cofactor kinetics (NAD⁺ vs NADP⁺ Km), substrate-inhibition constant, and oligomeric
  state** of Q88I50 should be measured directly (recombinant expression + steady-state kinetics).
- The **paralog landscape** in KT2440 is now mapped (this work): the NADP⁺ GabD class = PP_0213
  (**gabD-I**, in a *gabD-I–gabT* operon), PP_2488, PP_4422; sad-II (PP_3151) is the lone NAD⁺ K08324
  isozyme. Which catabolic route (GABA vs putrescine vs 4-hydroxybutyrate/other SSA sources) preferentially
  recruits sad-II, and whether YneJ (PP_3152) activates it, still require **transcriptomic/genetic
  confirmation** (e.g., growth and expression of ΔPP_3151 and Δ*yneJ* on GABA/putrescine).
- A crystal structure or AlphaFold model with docked NAD⁺/SSA would confirm the roles of Cys267, the
  general-base glutamate, and the NAD⁺-specificity residues predicted here.

---

### Key References
- de Carvalho LPS *et al.* (2011) Chemical mechanism of SSADH (GabD1) from *M. tuberculosis*. **PMID 21303655**
- Zheng H *et al.* (2013) Structure and activity of NAD(P)⁺-dependent SSADH YneI from *S. typhimurium*. **PMID 23229889**
- Langendorf CG *et al.* (2010) X-ray structure of *E. coli* GabD SSADH; NADP⁺ interactions. **PMID 20174634**
- Busch KB & Fromm H (1999) Plant SSADH: purification, mitochondrial localization, NAD⁺ specificity. **PMID 10517851**
- Luengo JM & Olivera ER (2020) Catabolism of biogenic amines in *Pseudomonas* species. **PMID 31912965**
- Wang C *et al.* (2006) Succinic semialdehyde couples stress response to QS signal decay in *A. tumefaciens*. **PMID 16942602**


## Artifacts

- [OpenScientist final report](sad-II-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sad-II-deep-research-openscientist_artifacts/final_report.pdf)