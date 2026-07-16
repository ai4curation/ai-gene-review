---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T16:46:54.475581'
end_time: '2026-07-15T17:02:42.905960'
duration_seconds: 948.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_1907
  gene_symbol: PP_1907
  uniprot_accession: Q88LM3
  protein_description: 'SubName: Full=Hydrolase, haloacid dehalogenase-like family
    {ECO:0000313|EMBL:AAN67525.1};'
  gene_info: OrderedLocusNames=PP_1907 {ECO:0000313|EMBL:AAN67525.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: HAD-like_hydrolase_sf. (IPR050155); HAD-like_sf. (IPR036412); HAD-SF_hydro_IA.
    (IPR006439); HAD_2. (IPR041492); HAD_sf. (IPR023214)
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
  path: PP_1907-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_1907-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LM3
- **Protein Description:** SubName: Full=Hydrolase, haloacid dehalogenase-like family {ECO:0000313|EMBL:AAN67525.1};
- **Gene Information:** OrderedLocusNames=PP_1907 {ECO:0000313|EMBL:AAN67525.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** HAD-like_hydrolase_sf. (IPR050155); HAD-like_sf. (IPR036412); HAD-SF_hydro_IA. (IPR006439); HAD_2. (IPR041492); HAD_sf. (IPR023214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_1907" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_1907' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_1907** (gene ID: PP_1907, UniProt: Q88LM3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_1907 (UniProt Q88LM3) — *Pseudomonas putida* KT2440

**Gene:** PP_1907 (OrderedLocusName) · **UniProt:** Q88LM3 · **RefSeq:** WP_010952931.1 · **Protein length:** 224 aa
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**) · **Genome position:** NC_002947.4, 2,152,277–2,152,951 (+ strand)

---

## 1. Summary (Answer to the Research Question)

PP_1907 encodes a **small, soluble, cytoplasmic enzyme of the haloacid dehalogenase (HAD) hydrolase superfamily, subfamily IA** — a **Mg²⁺-dependent phosphomonoesterase (phosphatase)**. Its aspartate-nucleophile catalytic machinery is fully intact, so it is confidently a functional phosphatase that hydrolyses a phosphomonoester substrate via a phospho-aspartyl enzyme intermediate. Every automated functional-classification resource (KEGG ortholog **K01091**, PANTHER PTHR43434, UniProt/TreeGrafter) assigns it the specific activity **2-phosphoglycolate phosphatase (Gph; EC 3.1.3.18)**, catalysing:

> **2-phosphoglycolate + H₂O → glycolate + inorganic phosphate (Pᵢ)**

placing it in **glyoxylate and dicarboxylate metabolism** (KEGG pathway ppu00630). By analogy to the biochemically characterised *Escherichia coli* Gph, the physiological role is a **cytoplasmic housekeeping "salvage" reaction** that disposes of 2-phosphoglycolate — most notably the 2-phosphoglycolate liberated during repair of oxidatively damaged 3′-phosphoglycolate DNA ends — recovering the two-carbon unit as glycolate for central metabolism.

**Important caveat:** This assignment is **inferential (bioinformatic / structural / evolutionary), not experimental.** PP_1907 itself has never been biochemically characterised, and it is **one of three paralogous HAD-IA phosphatases** in *P. putida* that carry the K01091 annotation. A closer paralog (**PP_0416**, 43% identical to *E. coli* Gph) is the more likely *principal* 2-phosphoglycolate phosphatase, so PP_1907's precise physiological substrate should be regarded as a well-motivated prediction that may include 2-phosphoglycolate and/or related small phosphometabolites, potentially with partial functional redundancy.

---

## 2. Identity Verification

The requested identifiers are internally consistent and unambiguous:
- Gene symbol **PP_1907** ↔ protein description "Hydrolase, haloacid dehalogenase-like family" ↔ organism *P. putida* KT2440 — all match across UniProt (Q88LM3), NCBI (AAN67525.1 / WP_010952931.1), KEGG (ppu:PP_1907) and STRING (160488.PP_1907).
- The listed InterPro domains (HAD-SF_hydro_IA IPR006439; HAD_2 IPR041492; HAD-like_sf IPR036412; HAD_sf IPR023214) exactly match what is found for this accession.
- No conflicting literature for a different gene of the same symbol exists (PP_ locus tags are unique to the *P. putida* KT2440 genome).

There is **no ambiguity of identity**; the only uncertainty concerns the *precise substrate*, discussed below.

---

## 3. Molecular Function — What Reaction Is Catalysed, and Substrate Specificity

### 3.1 Enzyme superfamily and catalytic mechanism
PP_1907 belongs to the **HAD superfamily** (eggNOG **COG0546**; Pfam **PF13419** HAD_2; SUPFAM SSF56784; NCBIfam TIGR01509/TIGR01549 "HAD-SF-IA"). HAD-superfamily enzymes are overwhelmingly **phosphotransferases/phosphohydrolases** that use an **aspartate nucleophile** to form a covalent phospho-aspartyl intermediate, with an essential **Mg²⁺** cofactor. All four diagnostic HAD sequence motifs are present in PP_1907:

| Motif | Sequence in PP_1907 | Residue(s) | Role |
|-------|--------------------|-----------|------|
| I (DxDxT/V) | ¹⁰F-**D11**-W-**D13**-G-**T15**-L | Asp11 (nucleophile), Asp13 (general acid/base), Thr15 | Nucleophilic attack; proton shuttle; phosphate binding |
| II (S/T) | cap/core loop | conserved Ser/Thr | H-bonds transferring phosphoryl group |
| III (K) | ¹¹⁰LAVA-T-G-**K113** | Lys113 | Neutralises phosphate negative charge |
| IV (GDxxxD / DD) | ¹⁶⁷**G-D168**-S-A-F-**D172** | Asp168, Asp172 | Coordinate catalytic Mg²⁺ |

UniProt lists **Mg²⁺ (ChEBI:18420)** as the cofactor (ARBA rule), consistent with this mechanism. This constitutes strong structural/bioinformatic evidence that PP_1907 is a *bona fide* Mg²⁺-dependent phosphatase, independent of any substrate assignment.

**Residue-level conservation with a characterized enzyme.** A pairwise global alignment of PP_1907 against the biochemically characterised *E. coli* Gph (P32662) shows that **all six catalytic residues align one-to-one to identical residues** (Asp11, Asp13, Thr15, Lys113, Asp168, Asp172 — every position invariant), even though overall identity is only ~29%. Because 2-phosphoglycolate phosphatases of diverse origins share highly conserved catalytic features implying a common mechanism (Pellicer et al., 2003, PMID 13129953), this invariance is strong evolutionary evidence that PP_1907 is a **catalytically competent phosphatase using the same aspartyl-phosphotransferase mechanism**.

### 3.2 Structural architecture and substrate-size class
The protein has the canonical **two-domain HAD-IA fold**: a Rossmann-like α/β core (**Gene3D 3.40.50.1000**) plus a small α-helical **"C1 cap"** inserted immediately after Motif I (**Gene3D 1.10.150.240** "putative phosphatase domain 2"; **IPR023198** "phosphoglycolate-phosphatase-like domain 2"; cap region ≈ residues 17–95). In the HAD superfamily the **cap domain is the principal determinant of substrate specificity and catalytic efficiency** (Daughtry et al., 2013, PMID 23848398; Biswas et al., 2009, PMID 19726684). A **small C1 cap of this type is characteristic of subfamily-IA phosphatases that act on small, mono-anionic phosphometabolites** — precisely the class that includes 2-phosphoglycolate phosphatase.

### 3.3 Specific substrate assignment and its confidence
Multiple independent resources converge on **2-phosphoglycolate phosphatase (EC 3.1.3.18)**:
- **KEGG**: ppu:PP_1907 → **K01091** (phosphoglycolate phosphatase), pathway ppu00630 (glyoxylate/dicarboxylate metabolism).
- **PANTHER**: family **PTHR43434 = PHOSPHOGLYCOLATE PHOSPHATASE**.
- **UniProt/TreeGrafter GO**: molecular function **GO:0008967 phosphoglycolate phosphatase activity**.
- **Sequence homology**: among characterised HAD-IA enzymes, PP_1907 is **closest to the experimentally validated *E. coli* Gph** (2-phosphoglycolate phosphatase, P32662; 29.0% global identity) — above *E. coli* YniC (23.6%), YidA sugar-phosphatase (20.4%), NagD (17.6%), and human PGP (24.6%). The *E. coli* Gph enzyme is **highly specific for 2-phosphoglycolate with high catalytic efficiency** (Pellicer et al., 2003, PMID 13129953).

**Tempering evidence (see §5):** *P. putida* KT2440 contains **three** K01091-annotated paralogs (PP_0094, PP_0416, PP_1907). **PP_0416** is 43.1% identical to *E. coli* Gph and is explicitly named "Phosphoglycolate phosphatase", making it the strongest candidate for the organism's principal 2-phosphoglycolate phosphatase; PP_0094 (25% identity) is annotated "5′-nucleotidase". The three paralogs share only 25–28% pairwise identity (ancient divergence). Because HAD-IA phosphatases frequently display **broad, overlapping substrate spectra** (Kuznetsova et al., 2006, PMID 16990279), PP_1907 may act on 2-phosphoglycolate and/or additional small phosphorylated metabolites; the single-substrate label is a prediction, not a measurement.

---

## 4. Localization and Biological Process / Pathway

### 4.1 Subcellular localization
PP_1907 is predicted **cytoplasmic** (**GO:0005829 cytosol**). It is a 224-residue soluble protein with **no signal peptide and no transmembrane segments**, consistent with the soluble, cytoplasmic nature of HAD-IA small-molecule phosphatases. Its function is therefore carried out **intracellularly, in the cytosol**.

### 4.2 Pathway context and physiological role
The reaction sits at the entry of **glyoxylate/dicarboxylate metabolism**. 2-Phosphoglycolate is a two-carbon phospho-metabolite; its dephosphorylation yields **glycolate**, which *P. putida* KT2440 can further oxidise and assimilate — the organism encodes a complete downstream route: **glycolate oxidase GlcDEF** (PP_3744/PP_3746/PP_3747; glycolate → glyoxylate), **glyoxylate carboligase Gcl** (PP_4297), and **malate synthase** (PP_0356), feeding carbon into central metabolism.

The **biological rationale** comes from the characterised *E. coli* ortholog: Gph is a **constitutively expressed housekeeping enzyme** that performs the **dissimilation/salvage of intracellular 2-phosphoglycolate formed during DNA repair of 3′-phosphoglycolate ends** — DNA lesions generated by oxidative and radiomimetic damage (e.g., bleomycin) — converting it to glycolate that re-enters general metabolism (Pellicer et al., 2003, PMID 13129953). This directly explains the **GO:0006281 (DNA repair)** annotation attached to PP_1907: the enzyme is not a DNA-repair protein itself but processes a **by-product** of DNA-end repair. (In photosynthetic/autotrophic organisms 2-phosphoglycolate arises mainly from RuBisCO oxygenase activity; *P. putida* is a heterotroph, so the DNA-repair/oxidative source is the physiologically relevant one.)

### 4.3 Genomic context
PP_1907's neighbours (PP_1904 *murB*, PP_1905 *rne*/RNase E, PP_1906 *rluC*, PP_1908 protease IV, PP_1909 pyrophosphatase) are **unrelated housekeeping genes**; the gene is **not part of a substrate-specific operon**, consistent with the constitutive housekeeping expression pattern reported for *E. coli gph*. STRING functional-partner networks link PP_1907 to the glycolate-oxidation machinery (GlcDEF) and glyoxylate reductases (GhrB, HprA), but these associations are **near-identical for all three paralogs** and therefore reflect **family-level co-annotation rather than PP_1907-specific evidence**.

---

## 5. Hypotheses: Supported and Refuted / Tempered

**Supported**
1. *PP_1907 is a Mg²⁺-dependent HAD-superfamily subfamily-IA phosphomonoesterase.* — Strongly supported by domain signatures, intact catalytic motifs (Asp11/Asp13/Thr15/Lys113/Asp168/Asp172), Mg²⁺ cofactor, and the two-domain C1-capped fold.
2. *Its default/primary predicted activity is 2-phosphoglycolate phosphatase (EC 3.1.3.18), acting in cytosolic glyoxylate/dicarboxylate metabolism as a 2-phosphoglycolate salvage enzyme.* — Supported by convergent KEGG/PANTHER/GO annotation, top homology to characterised *E. coli* Gph, and the intact downstream glycolate-utilisation pathway.
3. *The enzyme functions intracellularly (cytosol).* — Supported by GO and absence of signal/TM features.

**Tempered / partially refuted**
4. *PP_1907 is THE 2-phosphoglycolate phosphatase of P. putida.* — **Tempered.** PP_1907 is one of three paralogs; **PP_0416** (43% identity to Gph; explicitly named phosphoglycolate phosphatase) is a better candidate for the principal enzyme. PP_1907's exact substrate is unconfirmed and may be broader.
5. *STRING network proves PP_1907 acts in glycolate metabolism.* — **Refuted as specific evidence.** The network is a paralog/co-annotation artifact shared identically by all three K01091 genes.

---

## 6. Evidence Quality and Limitations

- **No experimental (ECO:0000269) data exist for PP_1907**; all annotations are imported (ECO:0000313) or automatic (ECO:0000256/ARBA). The functional picture is built entirely from **structure, evolution and bioinformatics**.
- The strongest *experimental anchor* is the characterisation of the orthologous **E. coli Gph** (Pellicer et al., 2003, PMID 13129953), transferred by homology.
- **Paralog ambiguity** (three K01091 genes) means enzyme-specific substrate and physiological roles cannot be assigned with certainty from sequence alone.
- The AlphaFold model for Q88LM3 could not be retrieved during this study, so active-site geometry was inferred from InterPro/Gene3D domain assignments and motif analysis rather than direct 3D inspection.

### Future directions
- **Direct biochemistry**: recombinant expression of PP_1907 (and PP_0416, PP_0094) and phosphatase substrate profiling (e.g., against 2-phosphoglycolate, sugar phosphates, nucleotide monophosphates, phosphoglycerate) with kinetic constants — the definitive test of substrate specificity, following the HAD substrate-screening approach of Kuznetsova et al. (2006, PMID 16990279).
- **Genetics**: single and combinatorial deletions of the three paralogs, testing bleomycin/oxidative-stress sensitivity and growth on glycolate, to resolve which paralog performs the physiological 2-phosphoglycolate salvage and whether they are redundant.
- **Structure**: experimental structure or validated AlphaFold model with docked 2-phosphoglycolate to examine cap-domain substrate-recognition residues.

---

## 7. Key References
- Pellicer MT, Nuñez F, Aguilar J, Badia J, Baldoma L. *Role of 2-phosphoglycolate phosphatase of Escherichia coli in metabolism of the 2-phosphoglycolate formed in DNA repair.* J Bacteriol. 2003. **PMID 13129953**.
- Kuznetsova E, et al. *Genome-wide analysis of substrate specificities of the Escherichia coli haloacid dehalogenase-like phosphatase family.* J Biol Chem. 2006. **PMID 16990279**.
- Daughtry KD, et al. *Structural basis for the divergence of substrate specificity and biological function within HAD phosphatases…* Biochemistry. 2013. **PMID 23848398**.
- Biswas T, et al. *The tail of KdsC: conformational changes control the activity of a HAD superfamily phosphatase.* 2009. **PMID 19726684**.
- Dos Santos VAPM, Heim S, Moore ERB, Strätz M, Timmis KN. *Insights into the genomic basis of niche specificity of Pseudomonas putida KT2440.* Environ Microbiol. 2004. **PMID 15560824**.

*Database resources consulted:* UniProt (Q88LM3), NCBI (AAN67525.1/WP_010952931.1), KEGG (ppu:PP_1907; K01091), InterPro/Pfam/Gene3D/PANTHER/SUPFAM, eggNOG (COG0546), STRING (160488.PP_1907), BioCyc.


## Artifacts

- [OpenScientist final report](PP_1907-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_1907-deep-research-openscientist_artifacts/final_report.pdf)