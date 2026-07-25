---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T09:41:28.443432'
end_time: '2026-07-23T10:10:48.540799'
duration_seconds: 1760.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0262
  gene_symbol: PP_0262
  uniprot_accession: Q88R72
  protein_description: 'RecName: Full=Thioesterase putative domain-containing protein
    {ECO:0000259|Pfam:PF09500};'
  gene_info: OrderedLocusNames=PP_0262 {ECO:0000313|EMBL:AAN65893.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: HotDog_dom_sf. (IPR029069); YiiD_C. (IPR012660); YiiD_C (PF09500)
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
  path: PP_0262-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0262-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R72
- **Protein Description:** RecName: Full=Thioesterase putative domain-containing protein {ECO:0000259|Pfam:PF09500};
- **Gene Information:** OrderedLocusNames=PP_0262 {ECO:0000313|EMBL:AAN65893.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** HotDog_dom_sf. (IPR029069); YiiD_C. (IPR012660); YiiD_C (PF09500)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0262" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0262' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0262** (gene ID: PP_0262, UniProt: Q88R72) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_0262 (UniProt Q88R72) in *Pseudomonas putida* KT2440

**Target:** PP_0262 / Q88R72 · *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) · 151 aa, ~17 kDa
**UniProt annotation (baseline):** "Thioesterase putative domain-containing protein" (HotDog superfamily; Pfam PF09500 *YiiD_C*; InterPro IPR029069 HotDog_dom_sf, IPR012660 YiiD_C; TIGR02447; eggNOG COG2050)

---

## 1. Summary (Answer to the Research Question)

**PP_0262 is *madB*, encoding MadB — a malonyl-[acyl-carrier-protein] decarboxylase (malonyl-ACP decarboxylase).** Despite a generic UniProt annotation as a "putative thioesterase," PP_0262 is a **characterized enzyme with a solved 1.04 Å crystal structure (PDB 8AYV)** and a dedicated primary study (McNaught et al., *Metabolic Engineering* 2023, PMID 36796578). Its primary function is to **catalyze the decarboxylation of malonyl-ACP to acetyl-ACP + CO₂**, thereby generating the acetyl-ACP "primer" that **initiates type II (dissociated) fatty acid biosynthesis (FAS II)**. This is a **FabH-independent initiation route**: it bypasses the canonical condensation of acetyl-CoA with malonyl-ACP by β-ketoacyl-ACP synthase III (FabH). MadB is **one of three parallel FAS-initiation pathways** operating in KT2440 (alongside FabH1 and FabH2). The enzyme acts in the **cytoplasm** on an ACP-tethered substrate, adopts a **HotDog fold** (the standalone C-terminal *YiiD_C* domain), and its homologs are **conserved throughout the Bacteria/Proteobacteria**.

> ⚠️ **Identity verification (as required):** The gene symbol "PP_0262" and the organism (*P. putida* KT2440) match the UniProt record exactly. The HotDog/thioesterase-fold domain (PF09500 YiiD_C) is precisely the fold used by MadB. The identity is confirmed by an unambiguous structural link: UniProt Q88R72 reference [3] cites **PDB 8AYV**, whose RCSB title is *"Crystal structure of the Malonyl-ACP Decarboxylase MadB from Pseudomonas putida"* (gene = PP_0262, taxid 160488). **No ambiguity: this report concerns the correct protein.**

---

## 2. Molecular Function — The Reaction Catalyzed

### 2.1 Reaction and substrate specificity
MadB catalyzes:

> **malonyl-ACP → acetyl-ACP + CO₂**

- **Substrate:** malonyl-ACP (malonate thioester on the phosphopantetheine arm of acyl carrier protein). The substrate is **ACP-tethered**, not a free CoA thioester.
- **Product:** acetyl-ACP, the C₂ starter unit for fatty-acid elongation.
- **Class:** a **decarboxylase (lyase)**, *not* a hydrolytic thioesterase — an important distinction, because the protein's structural scaffold (HotDog fold, "thioesterase/thiol-ester dehydrase-isomerase" superfamily, SUPFAM SSF54637) is shared with true thioesterases, which is why databases default to a "putative thioesterase" label.
- **Downstream fate of the product:** acetyl-ACP is condensed with a second malonyl-ACP by the elongation-type β-ketoacyl-ACP synthases (KAS I/II; FabB/FabF) to yield acetoacetyl-ACP, which then enters the standard FAS II reduction/dehydration/reduction cycle (FabG → FabA/FabZ → FabI). In *P. putida* F1, the FabB synthase itself can perform both the decarboxylation and the subsequent condensation (Guo et al. 2024, PMID 38335573), underscoring that the acetyl-ACP made by MadB feeds directly into elongation.

### 2.2 Mechanism and catalytic residues
McNaught et al. (2023) determined the mechanism by combining **exhaustive in vivo alanine-scanning mutagenesis, in vitro biochemical assays, 1.04 Å X-ray crystallography (PDB 8AYV), and QM/computational modeling**. The active site sits in the HotDog-fold cavity. Key conserved, functionally essential residues (P. putida MadB numbering) are **Asn43, Asn45, Phe51, and Arg124**; **Asn45→Ala abolishes decarboxylase activity**. These positions are present and conserved in the Q88R72 sequence (…⁴¹AANVNHKSTM⁵⁰, ⁵¹F…, …R¹²²AR¹²⁴…) and are retained even in distant homologs (~34 % identity) in *Xanthomonas*, confirming their catalytic importance (Yan et al. 2025, PMID 40197034). Arg124 is positioned to stabilize the developing negative charge/carboxylate during decarboxylation; the asparagines and Phe51 shape the oxyanion/substrate pocket — a mechanism analogous to other HotDog-fold decarboxylases.

### 2.3 Biochemical assay support
MadB-family activity is measured by reconstituting FAS in vitro: with malonyl-ACP as sole acyl donor plus FabB/FabG (± FabA/FabI) and NAD(P)H, MadB drives production of long-chain acyl-ACPs and NADPH oxidation (340 nm), whereas no-MadB controls do not (Yan et al. 2025). Reported specific activities for orthologs are high (e.g., *Xanthomonas oryzae* MadB ≈ 135 nmol·µg⁻¹·s⁻¹). MadB-type enzymes do **not** catalyze the FabH-type condensation of acetyl-CoA with malonyl-ACP (they make no butyryl-ACP in that assay), confirming a decarboxylase — not a KAS — activity.

---

## 3. Biological Process / Pathway

- **Pathway:** de novo **fatty acid biosynthesis (type II FAS)** — specifically the **initiation** step.
- **Role:** provides the acetyl-ACP primer that seeds the elongation cycle, an **alternative to FabH-catalyzed initiation**. In KT2440 there are **three initiation routes**: (i) FabH1 (a canonical KAS III using short-chain acyl-CoAs/acetyl-CoA), (ii) FabH2 (a KAS III accepting short- and medium-chain acyl-CoAs), and (iii) **MadB** (malonyl-ACP decarboxylation). This redundancy explains why single deletions are tolerated (e.g., growth of KT2440 is not fully blocked by deleting *madB* together with *fabH1*).
- **Precedent and relationships:** MadB is the *P. putida* counterpart of *E. coli* **MadA** (the *yiiD* product), the first-described malonyl-ACP decarboxylase that rescues *E. coli* ΔfabH strains. MadA is a **two-domain** protein (N-terminal GNAT/N-acetyltransferase domain fused to the C-terminal HotDog *YiiD_C* decarboxylase domain), whereas **MadB is the standalone HotDog domain**, which is by itself sufficient for decarboxylase activity.
- **Downstream metabolic connections:** the acetyl-ACP/acetyl groups generated by this route also supply acetylation reactions such as **UDP-GlcNAc synthesis** (feeding cell-envelope/EPS biosynthesis) in some proteobacteria; in *Xanthomonas*, *madB* loss reduces exopolysaccharide production, biofilm, and virulence, illustrating how the primary FAS-initiation activity ramifies into envelope/lipid physiology (Yan et al. 2025). These are secondary/pleiotropic consequences of the **primary decarboxylase function**.

---

## 4. Subcellular Localization

MadB functions in the **bacterial cytoplasm**. Rationale/evidence:
- The entire FAS II system (ACP, FabD, FabH, FabB/F, FabG, FabA/Z, FabI) is soluble and cytoplasmic, and MadB's substrate is the **cytosolic, ACP-tethered malonyl-ACP**.
- The 151-aa sequence contains **no signal peptide and no transmembrane segment**; the protein crystallized as a soluble globular HotDog-fold domain (PDB 8AYV, from recombinant cytoplasmic expression).
- Consistent with a soluble cytoplasmic enzyme, orthologs are purified as soluble His-tagged proteins for in vitro assays.

---

## 5. Structure and Evolution (Evidence from Structure/Bioinformatics)

- **Fold:** single **HotDog fold** (Gene3D 3.10.129.10 "Hotdog Thioesterase"; SUPFAM SSF54637). Domain family = **YiiD C-terminal domain** (Pfam PF09500; InterPro IPR012660; NCBIfam/TIGR TIGR02447 *yiiD_Cterm*; orthology COG2050).
- **Experimental structure:** **PDB 8AYV**, X-ray, **1.04 Å** (near-atomic resolution), chains A/B (residues 1–151); UniProt evidence level **PE1 (protein level)**.
- **Architecture insight:** the standalone MadB domain corresponds to the catalytic C-terminal half of the E. coli MadA (YiiD) fusion protein, showing the GNAT domain is dispensable for decarboxylase catalysis.
- **Conservation:** functional MadB/MadA homologs are **widespread across domain Bacteria** and **highly conserved within Proteobacteria**; catalytic residues (Asn43/Asn45/Phe51/Arg124) are retained even at ~30 % sequence identity, a strong evolutionary signature of a conserved catalytic mechanism.

---

## 6. Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| PP_0262 is merely a "putative thioesterase" of unknown function | **Refuted** | It is a characterized enzyme (MadB) with solved structure and mechanism. |
| PP_0262 = MadB malonyl-ACP decarboxylase | **Supported (high confidence)** | PDB 8AYV title + gene PP_0262; McNaught 2023. |
| Primary reaction is hydrolytic thioester cleavage (thioesterase) | **Refuted** | Enzyme is a decarboxylase (malonyl-ACP → acetyl-ACP + CO₂); it does not act as a hydrolase in assays. |
| Function is FAS **initiation** (provides acetyl-ACP primer) | **Supported** | In vivo complementation of ΔfabH strains; in vitro reconstitution; alanine scan. |
| MadB is essential/sole initiator in KT2440 | **Refuted** | KT2440 has three redundant initiation routes (FabH1, FabH2, MadB). |
| Acts in the cytoplasm on ACP-tethered substrate | **Supported** | Soluble FAS II machinery; no signal/TM sequence; soluble recombinant protein. |

---

## 7. Limitations and Future Directions

- The definitive primary paper (McNaught et al. 2023, PMID 36796578) is **not open-access**; catalytic-residue specifics and kinetic constants were corroborated here from the structure metadata (PDB 8AYV), the abstract, and open follow-up work (Guo 2024; Yan 2025). Exact *k*cat/*K*m for KT2440 MadB were not retrievable in this session.
- The **strict physiological indispensability** of MadB in KT2440 under different carbon sources/growth conditions warrants targeted single- and double-mutant characterization (redundancy with FabH1/FabH2 and possibly FabB complicates loss-of-function phenotypes).
- Whether KT2440 MadB, like FabB in *P. putida* F1, contributes to **branched/unsaturated** fatty acid initiation or channels acetyl-ACP into UDP-GlcNAc/envelope pathways in vivo remains to be quantified.
- The regulatory logic of *madB* expression in KT2440 (operon context, inducers) is not yet defined.

---

## References
1. McNaught KJ, Kuatsjah E, Zahn M, *et al.* **Initiation of fatty acid biosynthesis in *Pseudomonas putida* KT2440.** *Metab Eng* 2023;76:193–203. **PMID 36796578.** (Defines MadB/PP_0262; PDB 8AYV.)
2. Guo S, Zhong Q, Dong Q, Cronan JE, Wang H. **Diversity in fatty acid elongation enzymes: The FabB long-chain β-ketoacyl-ACP synthase I initiates fatty acid synthesis in *Pseudomonas putida* F1.** 2024. **PMID 38335573.** (MadA/MadB context; malonyl-ACP → acetyl-ACP initiation.)
3. Yan Y, Yu, Luo, Su, Ma, Hu, Wang. **Functional disparities of malonyl-ACP decarboxylase between *Xanthomonas campestris* and *Xanthomonas oryzae*.** 2025. **PMID 40197034.** (MadB conservation, catalytic residues, standalone YiiD_C domain, physiology.)
4. Nelson KE, *et al.* **Complete genome sequence… *Pseudomonas putida* KT2440.** *Environ Microbiol* 2002;4:799–808. **PMID 12534463.** (Genome/locus PP_0262.)
5. RCSB PDB **8AYV** — *Crystal structure of the Malonyl-ACP Decarboxylase MadB from Pseudomonas putida* (X-ray, 1.04 Å).
6. UniProtKB **Q88R72** (Q88R72_PSEPK); Pfam PF09500 (YiiD_C); InterPro IPR012660/IPR029069; TIGR02447; eggNOG COG2050.


## Artifacts

- [OpenScientist final report](PP_0262-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0262-deep-research-openscientist_artifacts/final_report.pdf)