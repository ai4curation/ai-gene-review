---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:44:37.959068'
end_time: '2026-07-17T07:06:58.400434'
duration_seconds: 1340.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: bioF
  gene_symbol: bioF
  uniprot_accession: Q88QX1
  protein_description: 'RecName: Full=8-amino-7-oxononanoate synthase {ECO:0000255|HAMAP-Rule:MF_01693};
    Short=AONS {ECO:0000255|HAMAP-Rule:MF_01693}; EC=2.3.1.47 {ECO:0000255|HAMAP-Rule:MF_01693};
    AltName: Full=7-keto-8-amino-pelargonic acid synthase {ECO:0000255|HAMAP-Rule:MF_01693};
    Short=7-KAP synthase {ECO:0000255|HAMAP-Rule:MF_01693}; Short=KAPA synthase {ECO:0000255|HAMAP-Rule:MF_01693};
    AltName: Full=8-amino-7-ketopelargonate synthase {ECO:0000255|HAMAP-Rule:MF_01693};'
  gene_info: Name=bioF {ECO:0000255|HAMAP-Rule:MF_01693}; OrderedLocusNames=PP_0363;
    ORFNames=PP0363;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-II pyridoxal-phosphate-dependent
  protein_domains: Aminotransferase_I/II_large. (IPR004839); AON_synthase_class-II.
    (IPR050087); AONS_Archaea/Proteobacteria. (IPR004723); AONS_Proteobacteria. (IPR022834);
    PyrdxlP-dep_Trfase. (IPR015424)
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
  path: bioF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bioF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QX1
- **Protein Description:** RecName: Full=8-amino-7-oxononanoate synthase {ECO:0000255|HAMAP-Rule:MF_01693}; Short=AONS {ECO:0000255|HAMAP-Rule:MF_01693}; EC=2.3.1.47 {ECO:0000255|HAMAP-Rule:MF_01693}; AltName: Full=7-keto-8-amino-pelargonic acid synthase {ECO:0000255|HAMAP-Rule:MF_01693}; Short=7-KAP synthase {ECO:0000255|HAMAP-Rule:MF_01693}; Short=KAPA synthase {ECO:0000255|HAMAP-Rule:MF_01693}; AltName: Full=8-amino-7-ketopelargonate synthase {ECO:0000255|HAMAP-Rule:MF_01693};
- **Gene Information:** Name=bioF {ECO:0000255|HAMAP-Rule:MF_01693}; OrderedLocusNames=PP_0363; ORFNames=PP0363;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-II pyridoxal-phosphate-dependent
- **Key Domains:** Aminotransferase_I/II_large. (IPR004839); AON_synthase_class-II. (IPR050087); AONS_Archaea/Proteobacteria. (IPR004723); AONS_Proteobacteria. (IPR022834); PyrdxlP-dep_Trfase. (IPR015424)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "bioF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'bioF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **bioF** (gene ID: bioF, UniProt: Q88QX1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *bioF* (Q88QX1) — 8-Amino-7-Oxononanoate Synthase in *Pseudomonas putida* KT2440

**Gene:** `bioF` (ordered locus **PP_0363**; ORF PP0363) · **UniProt:** Q88QX1 (BIOF_PSEPK), 390 aa · **EC:** 2.3.1.47
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**), a Gammaproteobacterium

---

## Summary

The gene **bioF** (UniProt **Q88QX1**; locus **PP_0363**) of *Pseudomonas putida* KT2440 encodes **8-amino-7-oxononanoate synthase** (AONS), also called **7-keto-8-aminopelargonate synthase** or **KAPA synthase** (**EC 2.3.1.47**). This is a 390-amino-acid, **pyridoxal-5′-phosphate (PLP)-dependent enzyme** of the **α-oxoamine synthase (AOS) family**, within the class-II (fold-type I) aminotransferase superfamily. The gene symbol is **not ambiguous** for this organism: the symbol, EC number, protein family (class-II PLP-dependent aminotransferase), and diagnostic InterPro domains (IPR004839, IPR050087, IPR004723, IPR022834, IPR015424) all converge on a single, well-defined enzymatic function, and the retrieved literature pertains specifically to biotin-biosynthetic AONS/BioF enzymes.

**Primary function:** BioF catalyzes the **first committed step of biotin (vitamin B7) biosynthesis** — a **PLP-dependent, decarboxylative Claisen-type condensation** of **L-alanine** with a **pimeloyl thioester** (physiologically **pimeloyl-ACP** in this Proteobacterium; pimeloyl-CoA in classic in vitro assays) to produce **(8S)-8-amino-7-oxononanoate (KAPA/AON)**, releasing **CO₂** and the free thiol carrier. The reaction is stereospecific for the 8(S) configuration, and the PLP cofactor is covalently anchored through a Schiff base (internal aldimine) to **Lys236**.

**Localization and pathway context:** BioF is a **soluble, cytoplasmic, homodimeric** enzyme whose active site lies at the dimer interface. In *P. putida* KT2440 the gene sits in a **dedicated biotin-biosynthesis cluster (bioB-bioF-bioH-bioC, PP_0362–PP_0365)**. Upstream, **BioC** and **BioH** manufacture the pimeloyl-ACP substrate by "hijacking" fatty-acid synthesis; downstream, the KAPA product is processed by **BioA → BioD → BioB** to complete biotin. The annotation is corroborated by ~49% sequence identity plus a conserved PLP-lysine motif shared with the crystallographically and mechanistically characterized *E. coli* enzyme, a very-high-confidence AlphaFold model (mean pLDDT 96.7), and biotin-rescuable genetic and chemical-genetic evidence in multiple organisms.

---

## Key Findings

### The catalyzed reaction: BioF is the first committed enzyme of biotin biosynthesis

UniProt Q88QX1, annotated under HAMAP-Rule MF_01693, assigns bioF the function of **8-amino-7-oxononanoate synthase (EC 2.3.1.47)**. The precise catalytic activity is:

> **6-carboxyhexanoyl-[ACP] (pimeloyl-ACP) + L-alanine + H⁺ → (8S)-8-amino-7-oxononanoate + holo-[ACP] + CO₂**

The mechanistic and kinetic framework was established in the *E. coli* system. Webster and colleagues state directly that "**8-Amino-7-oxononanoate synthase (also known as 7-keto-8-aminopelargonate synthase, EC 2.3.1.47) is a pyridoxal 5′-phosphate-dependent enzyme which catalyzes the decarboxylative condensation of L-alanine with pimeloyl-CoA in a stereospecific manner to form 8(S)-amino-7-oxononanoate. This is the first committed step in biotin biosynthesis**" ([PMID: 10642176](https://pubmed.ncbi.nlm.nih.gov/10642176/)). This single sentence captures the enzyme's cofactor requirement, substrate specificity, reaction chemistry, product stereochemistry, and pathway role.

The chemistry proceeds through a reactive β-ketoacid PLP-aldimine (Claisen) intermediate. Kerbarh and colleagues trapped and characterized this species directly, reporting that "**the reactive beta-ketoacid pyridoxal-5′-phosphate aldimine formed in the condensation step of the 8-amino-7-oxononanoate synthase reaction was 'trapped' in the enzyme-bound form**" ([PMID: 16353092](https://pubmed.ncbi.nlm.nih.gov/16353092/)) — direct experimental confirmation of the AOS-family Claisen-condensation mechanism.

The **amino-donor is strictly L-alanine** and the product is stereospecifically the **8(S)** epimer, matching the UniProt catalytic-activity annotation for the *P. putida* enzyme, which specifies that AONS "**catalyzes the decarboxylative condensation of L-alanine with pimeloyl-CoA in a stereospecific manner to form 8(S)-amino-7-oxononanoate**" ([PMID: 10642176](https://pubmed.ncbi.nlm.nih.gov/10642176/)).

### Structure and family: a PLP-dependent homodimer of the α-oxoamine synthase class

The three-dimensional architecture of AONS was solved for the *E. coli* ortholog in apo, PLP-bound (internal aldimine), and product external-aldimine forms at 1.7–2.0 Å resolution. Alexeev and colleagues describe the enzyme: "**The protein is a symmetrical homodimer with a tertiary structure and active site organisation similar to, but distinct from, those of other PLP-dependent enzymes whose three-dimensional structures are known. The critical PLP-binding lysine of AONS is located at the end of a deep cleft that allows access of the pantothenate arm of pimeloyl-CoA**" ([PMID: 9813126](https://pubmed.ncbi.nlm.nih.gov/9813126/)).

This establishes three features that transfer to the *P. putida* enzyme by orthology: (1) a **homodimeric quaternary structure** with active sites at the dimer interface, (2) a **PLP-binding lysine** at the base of a deep substrate cleft, and (3) a **binding site for the acyl-thioester carrier arm**. The mechanism is analogous to 5-aminolevulinate synthase (ALAS) and other α-oxoamine synthases. This is fully consistent with the UniProt family assignment (class-II PLP-dependent aminotransferase) and the InterPro signatures IPR004839 (Aminotransferase I/II large), IPR050087/IPR004723/IPR022834 (AON synthase class-II subfamilies), and IPR015424 (PLP-dependent transferase).

### Cofactor attachment and localization: PLP–Lys236, cytoplasmic and soluble

The UniProt entry specifies that PLP is **covalently bound as N6-(pyridoxal phosphate)lysine at Lys236** — the internal-aldimine Schiff base. The KEGG orthology entry ppu:PP_0363 = **K00652**, EC 2.3.1.47, Pfam Aminotran_1_2, gene coordinates 441120..442292. Localization is **cytoplasmic**: BioF is a soluble enzyme of a cytoplasmic biosynthetic pathway, with no signal peptide, transmembrane segment, or membrane anchor, consistent with the soluble, crystallizable *E. coli* homodimer ([PMID: 9813126](https://pubmed.ncbi.nlm.nih.gov/9813126/)).

### Substrate supply: the BioC–BioH fatty-acid "hijack" pathway

BioF requires a **pimeloyl thioester** as its acyl donor. In Proteobacteria this C7 diacid moiety is generated by a **modified round of fatty-acid synthesis**. Lin, Hanson, and Cronan showed that "**the pimeloyl moiety is synthesized by a modified fatty acid synthetic pathway in which the omega-carboxyl group of a malonyl-thioester is methylated by BioC, which allows recognition of this atypical substrate by the fatty acid synthetic enzymes**" ([PMID: 20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/)). The methyl ester disguises the terminal carboxylate so that the standard FAS machinery elongates the chain by two rounds to **pimeloyl-ACP methyl ester**.

The methyl ester is then removed by **BioH**, the pathway gatekeeper. Agarwal and colleagues used the structure "**to demonstrate that BioH is the gatekeeper and its physiological substrate is pimeloyl-ACP methyl ester**" ([PMID: 23045647](https://pubmed.ncbi.nlm.nih.gov/23045647/)), releasing **pimeloyl-ACP** — the immediate acyl donor for BioF.

### Genomic context: a dedicated biotin-biosynthesis cluster in *P. putida*

Analysis of the genomic neighborhood in KEGG places bioF within a compact biotin cluster:

| Locus | Gene | KEGG ortholog | EC | Enzyme |
|-------|------|---------------|-----|--------|
| PP_0362 | *bioB* | K01012 | 2.8.1.6 | Biotin synthase |
| **PP_0363** | ***bioF*** | **K00652** | **2.3.1.47** | **8-amino-7-oxononanoate synthase (AONS)** |
| PP_0364 | *bioH* | K02170 | 3.1.1.85 | Pimeloyl-[ACP] methyl ester carboxylesterase |
| PP_0365 | *bioC* | K02169 | 2.1.1.197 | Malonyl-[ACP] O-methyltransferase |

All four genes belong to KEGG module **M00123** ("Biotin biosynthesis, pimeloyl-ACP/CoA => biotin") and pathway **ppu00780**. The physical co-localization of **bioC** and **bioH** with **bioF** demonstrates that *P. putida* carries the **BioC–BioH modified-fatty-acid route**, exactly as in *E. coli*, where "**the malonyl-thioester methyl ester enters fatty acid synthesis as the primer and undergoes two reiterations of the fatty acid elongation cycle to give pimeloyl-acyl carrier protein (ACP) methyl ester, which is hydrolyzed to pimeloyl-ACP and methanol by BioH**" ([PMID: 20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/)). This clustering both confirms the substrate-supply route and reinforces the functional assignment of PP_0363.

### Orthology: ~49% identity to the characterized *E. coli* enzyme with a conserved PLP-lysine motif

A global pairwise alignment of Q88QX1 (*P. putida*, 390 aa) against P12998 (*E. coli* BioF, 384 aa) yields **~48.9% amino-acid identity over 396 aligned columns** — far above the ~30% "twilight zone", indicating conserved fold and function. The **catalytic PLP-binding lysine sits within a conserved glycine-rich motif** (*P. putida* residues 231–242 = `IGTLGKACGTAG`, where K = **Lys236**), matching the ALAS/AOS-family PLP-lysine signature. Because the *E. coli* structure "**enables identification of the key residues of the PLP-binding site and thus provides a framework with which to understand the biochemical mechanism**" ([PMID: 9813126](https://pubmed.ncbi.nlm.nih.gov/9813126/)), the high orthologous identity transfers these mechanistic conclusions to the *P. putida* enzyme.

### Organism-dependent acyl-donor and biotin-rescuable essentiality

The **identity of BioF's acyl-thioester donor is not universal**. Manandhar and Cronan noted that "**the BioF acyl chain donor has long been thought to be pimeloyl-CoA**" ([PMID: 29054876](https://pubmed.ncbi.nlm.nih.gov/29054876/)), but showed that *E. coli* BioF physiologically uses **pimeloyl-ACP** (from the BioC/BioH route), whereas *Bacillus subtilis* BioF uses **pimeloyl-CoA** — the carrier tracks the organism's pimelate-synthesis pathway. Given the clustered bioC/bioH and AONS_Proteobacteria signature, *P. putida* uses the **pimeloyl-ACP** route.

Two independent lines confirm BioF is on-pathway and functionally required:

- **Genetic (knockout):** a *Riemerella anatipestifer bioF* mutant impairs biotin biosynthesis; it "**displayed a decreased growth rate at the exponential phase in tryptic soy broth culture and in BeaverBeads Streptavidin treated tryptic soy broth culture, but recovered when biotin was supplemented**" ([PMID: 30279476](https://pubmed.ncbi.nlm.nih.gov/30279476/)), with altered morphology and virulence — a hallmark biotin-dependent, biotin-rescuable phenotype.
- **Chemical-genetic (inhibitor):** AONS inhibitors are lethal to *Arabidopsis thaliana* and cause L-alanine accumulation, and the toxicity is reversed by biotin: "**Foliar supplement of 1mM biotin at 1 and 2days before KHG23844 application effectively recovered the growth inhibition of A. thaliana plant treated with KHG23844**" ([PMID: 26615154](https://pubmed.ncbi.nlm.nih.gov/26615154/)). Biotin rescue confirms that AONS acts specifically on the biotin pathway.

### Structural inference: a very-high-confidence AlphaFold model

The AlphaFold DB entry **AF-Q88QX1-F1** spans all 1–390 residues with a **mean pLDDT of 96.7**; **94.4%** of residues exceed pLDDT 90 (very high confidence) and **98.7%** exceed 70. This confidently modeled structure is consistent with the class-II (fold-type I) PLP aminotransferase/α-oxoamine synthase fold expected from the ~49% identity to *E. coli* BioF and from InterPro domains IPR004839/IPR015424. The experimental *E. coli* structures — where the authors "**cloned, over-expressed and purified AONS from Escherichia coli and determined the crystal structures of the apo and PLP-bound forms of the enzyme**" ([PMID: 9813126](https://pubmed.ncbi.nlm.nih.gov/9813126/)) — define the fold that the AlphaFold model recapitulates.

---

## Mechanistic Model / Interpretation

BioF (PP_0363) operates as the **gateway enzyme of biotin biosynthesis** in the cytoplasm of *P. putida* KT2440. The diagram places it within the complete pathway and its clustered gene neighborhood:

```
   FATTY-ACID SYNTHESIS "HIJACK" (substrate supply)
   ───────────────────────────────────────────────
   malonyl-ACP
        │  BioC (PP_0365)  — O-methylation of ω-carboxyl (EC 2.1.1.197)
        ▼
   malonyl-ACP methyl ester
        │  FAS elongation × 2 rounds
        ▼
   pimeloyl-ACP methyl ester
        │  BioH (PP_0364)  — esterase / gatekeeper (EC 3.1.1.85)
        ▼
   pimeloyl-ACP ───────────────┐
                                │  (acyl-thioester donor)
   L-alanine ───────────────────┤
                                ▼
             ╔══════════════════════════════════════════╗
             ║  BioF  (PP_0363, Q88QX1)  EC 2.3.1.47     ║
             ║  8-amino-7-oxononanoate synthase (AONS)   ║
             ║  PLP-Lys236 · homodimer · cytoplasmic     ║
             ║  Decarboxylative Claisen condensation     ║
             ╚══════════════════════════════════════════╝
                                │  + H⁺
                                ▼
        (8S)-8-amino-7-oxononanoate (KAPA/AON) + CO₂ + holo-ACP
                                │  BioA — DAPA aminotransferase (SAM amino donor)
                                ▼
        7,8-diaminononanoate (DAPA)
                                │  BioD — dethiobiotin synthetase (EC 6.3.3.3)
                                ▼
        dethiobiotin
                                │  BioB (PP_0362) — biotin synthase (EC 2.8.1.6)
                                ▼
                             BIOTIN (vitamin B7)
```

**Catalytic cycle at the active site (fold-type I / AOS mechanism):**

1. Resting state: PLP forms an **internal aldimine** (Schiff base) with **Lys236**.
2. **L-alanine** displaces Lys236 to form an **external aldimine**; Lys236 acts as catalytic base.
3. Deprotonation of the α-carbon gives a resonance-stabilized **quinonoid/carbanion**.
4. **Claisen condensation** with the thioester carbonyl of **pimeloyl-ACP** forms a new C–C bond, releasing the ACP thiol.
5. The **β-ketoacid PLP-aldimine intermediate** (trapped experimentally, [PMID: 16353092](https://pubmed.ncbi.nlm.nih.gov/16353092/)) undergoes **decarboxylation** (loss of CO₂).
6. Stereospecific **reprotonation** yields the **8(S)** product; transaldimination with Lys236 releases **KAPA** and regenerates the internal aldimine.

The convergence of evidence is strong: rule-based annotation (UniProt HAMAP MF_01693; KEGG K00652); ~49% identity plus a conserved PLP-lysine motif to the crystallographically defined *E. coli* enzyme; a very-high-confidence AlphaFold model; genomic clustering with bioB/bioH/bioC that both confirms the pathway and identifies the substrate-supply route; and orthogonal biotin-rescue experiments demonstrating an on-pathway, essential role. The one organism-specific subtlety is the **acyl-donor carrier**: *P. putida*, as a Proteobacterium with bioC/bioH, uses **pimeloyl-ACP** rather than pimeloyl-CoA.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|------|--------------------|--------------|
| [10642176](https://pubmed.ncbi.nlm.nih.gov/10642176/) | *Mechanism of AONS: spectroscopic, kinetic, crystallographic studies* | Defines EC 2.3.1.47, PLP cofactor, L-alanine + pimeloyl-CoA substrates, 8(S) stereochemistry, "first committed step" |
| [16353092](https://pubmed.ncbi.nlm.nih.gov/16353092/) | *Intermediate Claisen product in the AONS reaction* | Direct trapping of the β-ketoacid PLP-aldimine intermediate, confirming the Claisen mechanism |
| [9813126](https://pubmed.ncbi.nlm.nih.gov/9813126/) | *Crystal structure of AONS* | Homodimer; PLP-binding lysine in a deep acyl-CoA cleft; fold-type I architecture; mechanistic framework |
| [20693992](https://pubmed.ncbi.nlm.nih.gov/20693992/) | *Biotin synthesis begins by hijacking fatty-acid synthesis* | BioC methylation route producing the pimeloyl-ACP substrate consumed by BioF |
| [23045647](https://pubmed.ncbi.nlm.nih.gov/23045647/) | *Enzyme-ACP substrate gatekeeper complex* | BioH is the gatekeeper; physiological substrate is pimeloyl-ACP methyl ester |
| [29054876](https://pubmed.ncbi.nlm.nih.gov/29054876/) | *BioF uses different acyl donors in* B. subtilis *and* E. coli | Acyl-donor carrier (ACP vs CoA) is organism-dependent; Proteobacteria use pimeloyl-ACP |
| [30279476](https://pubmed.ncbi.nlm.nih.gov/30279476/) | R. anatipestifer bioF *responsible for biotin synthesis* | Knockout impairs biotin-dependent growth, rescued by biotin; confirms on-pathway role |
| [26615154](https://pubmed.ncbi.nlm.nih.gov/26615154/) | *AONS inhibitors as potential herbicides* | Inhibitor toxicity reversed by biotin; AONS is the committed on-pathway step and a target |
| [11255013](https://pubmed.ncbi.nlm.nih.gov/11255013/) | *Biotin biosynthetic genes of* Kurthia *sp.* | bioF clusters with other bio genes; modified FAS route inferred in bacteria lacking bioW (context) |
| [30218044](https://pubmed.ncbi.nlm.nih.gov/30218044/) | N. gargensis bioABDF *+ ΔbioH-complementing esterase* | Comparative genomics of bio clusters across domains (context) |

**Supporting vs challenging.** All ten papers **support** the functional assignment; none challenges the core identification. The primary caveat-introducing paper, [PMID: 29054876](https://pubmed.ncbi.nlm.nih.gov/29054876/), refines rather than contradicts the annotation, showing the historical "pimeloyl-CoA" assumption is organism-dependent and that Proteobacteria like *P. putida* use pimeloyl-ACP. Retrieved papers on AONS-domain megasynthases in natural-product biosynthesis (e.g., SxtA in saxitoxin, PqrA in perquinolines) confirm that AONS chemistry generalizes to related α-amino-ketone-forming condensations but are **not** part of *P. putida* biotin metabolism and were correctly excluded.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 enzyme.** All mechanistic, kinetic, and structural data derive from orthologs (principally *E. coli*). The assignment for Q88QX1 is an **inference by orthology** (~49% identity) plus rule-based annotation, not direct biochemistry on PP_0363. No purified-enzyme kinetics (kcat, Km), crystal structure, or gene-knockout phenotype exist specifically for PP_0363. (UniProt evidence level: "inferred from homology.")

2. **Substrate carrier not experimentally verified in *P. putida*.** The pimeloyl-ACP (vs pimeloyl-CoA) assignment is inferred from genomic context (clustered bioC/bioH) and the *E. coli* paradigm; it has not been directly demonstrated in this organism.

3. **Localization is inferred, not measured.** Cytoplasmic localization is deduced from soluble orthologs and the absence of targeting signals; no fractionation or imaging data exist for PP_0363.

4. **Structural inference relies on AlphaFold.** The high-pLDDT model supports the fold but does not capture bound PLP, substrate poses, or dynamic active-site conformations; no experimental structure of the *P. putida* protein exists.

5. **Regulation and BioD/BioA loci.** The regulatory logic of the *P. putida* bio cluster and the precise genomic locations of *bioD* and *bioA* were not resolved in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymatic assay.** Clone PP_0363, express in *E. coli*, purify, confirm PLP loading (~420 nm internal-aldimine absorbance), and measure steady-state kinetics for L-alanine and for both pimeloyl-ACP and pimeloyl-CoA to determine the physiological carrier and substrate preference.

2. **Genetic complementation and knockout.** Test whether PP_0363 complements an *E. coli* ΔbioF mutant for biotin prototrophy, and construct a *P. putida* PP_0363 deletion; verify a biotin-auxotroph phenotype rescuable by exogenous biotin (mirroring [PMID: 30279476](https://pubmed.ncbi.nlm.nih.gov/30279476/)).

3. **Active-site validation.** Generate a K236A (PLP-lysine) variant and confirm loss of activity and of the 420 nm chromophore, directly testing the Lys236 cofactor-attachment annotation.

4. **Experimental structure determination.** Solve the crystal or cryo-EM structure of *P. putida* BioF (apo, PLP-bound, product-external-aldimine forms) to validate the AlphaFold model and define the ACP-binding cleft.

5. **Substrate-supply reconstitution.** Biochemically reconstitute the BioC (PP_0365) → BioH (PP_0364) → BioF (PP_0363) segment in vitro to confirm pimeloyl-ACP channeling to BioF.

6. **Pathway/regulatory mapping.** Locate *bioD* and *bioA* in the KT2440 genome and characterize biotin-responsive transcriptional regulation of the cluster to complete the pathway context.

---

## Conclusion

The evidence — rule-based database annotation, strong orthology to the mechanistically and structurally characterized *E. coli* enzyme, a conserved PLP-Lys236 active-site motif, a very-high-confidence AlphaFold model, an intact biotin-biosynthesis gene cluster, and biotin-rescuable genetic/chemical validation in related organisms — converges unambiguously. *P. putida* KT2440 **bioF (PP_0363, Q88QX1)** encodes the **PLP-dependent, homodimeric, cytoplasmic 8-amino-7-oxononanoate synthase (AONS/KAPA synthase, EC 2.3.1.47)** that catalyzes the **first committed step of biotin biosynthesis**: the decarboxylative Claisen condensation of **L-alanine** with **pimeloyl-ACP** to yield **(8S)-8-amino-7-oxononanoate**, CO₂, and free ACP. The gene symbol is not ambiguous for this organism, and all retrieved literature supports the assignment.


## Artifacts

- [OpenScientist final report](bioF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bioF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10642176
2. PMID:16353092
3. PMID:9813126
4. PMID:20693992
5. PMID:23045647
6. PMID:29054876
7. PMID:30279476
8. PMID:26615154