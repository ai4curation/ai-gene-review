---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:26:13.778864'
end_time: '2026-07-18T16:46:03.683048'
duration_seconds: 1189.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ispE
  gene_symbol: ispE
  uniprot_accession: Q88PX5
  protein_description: 'RecName: Full=4-diphosphocytidyl-2-C-methyl-D-erythritol kinase
    {ECO:0000255|HAMAP-Rule:MF_00061}; Short=CMK {ECO:0000255|HAMAP-Rule:MF_00061};
    EC=2.7.1.148 {ECO:0000255|HAMAP-Rule:MF_00061}; AltName: Full=4-(cytidine-5''-diphospho)-2-C-methyl-D-erythritol
    kinase {ECO:0000255|HAMAP-Rule:MF_00061};'
  gene_info: Name=ispE {ECO:0000255|HAMAP-Rule:MF_00061}; OrderedLocusNames=PP_0723;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the GHMP kinase family. IspE subfamily.
  protein_domains: GHMP_kinase_C_dom. (IPR013750); GHMP_kinase_C_sf. (IPR036554);
    GHMP_kinase_N_dom. (IPR006204); IspE. (IPR004424); Ribosomal_Su5_D2-typ_SF. (IPR020568)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ispE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ispE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PX5
- **Protein Description:** RecName: Full=4-diphosphocytidyl-2-C-methyl-D-erythritol kinase {ECO:0000255|HAMAP-Rule:MF_00061}; Short=CMK {ECO:0000255|HAMAP-Rule:MF_00061}; EC=2.7.1.148 {ECO:0000255|HAMAP-Rule:MF_00061}; AltName: Full=4-(cytidine-5'-diphospho)-2-C-methyl-D-erythritol kinase {ECO:0000255|HAMAP-Rule:MF_00061};
- **Gene Information:** Name=ispE {ECO:0000255|HAMAP-Rule:MF_00061}; OrderedLocusNames=PP_0723;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the GHMP kinase family. IspE subfamily.
- **Key Domains:** GHMP_kinase_C_dom. (IPR013750); GHMP_kinase_C_sf. (IPR036554); GHMP_kinase_N_dom. (IPR006204); IspE. (IPR004424); Ribosomal_Su5_D2-typ_SF. (IPR020568)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ispE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ispE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ispE** (gene ID: ispE, UniProt: Q88PX5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *ispE* (CMK / IspE; UniProt Q88PX5; PP_0723) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

The *ispE* gene (locus **PP_0723**; UniProt **Q88PX5**) of *Pseudomonas putida* KT2440 encodes **4-diphosphocytidyl-2-C-methyl-D-erythritol kinase** (abbreviated **CMK** or **IspE**; **EC 2.7.1.148**). It is a cytoplasmic, ATP-dependent small-molecule kinase of the **GHMP kinase superfamily (IspE subfamily)** that catalyzes the **fourth of the eight steps** of the **2-C-methyl-D-erythritol-4-phosphate (MEP) / non-mevalonate / DOXP pathway** of isoprenoid precursor biosynthesis. Specifically, it phosphorylates the **2-hydroxyl group** of 4-diphosphocytidyl-2-C-methyl-D-erythritol (CDP-ME), using ATP (and Mg²⁺), to give 4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P) plus ADP. This committed step channels carbon toward the universal isoprenoid building blocks isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), which in *P. putida* are used for respiratory quinones (ubiquinone/menaquinone), cell-envelope carrier lipids, carotenoids, and other terpenoids. Because the MEP pathway is essential in most bacteria yet absent from humans, IspE is an established antibacterial drug target.

**Gene-identity verification (mandatory):** The gene symbol *ispE*, the protein name CMK, EC 2.7.1.148, the GHMP-kinase/IspE-subfamily assignment, and the InterPro domains (IPR004424 IspE; IPR006204/IPR013750/IPR036554 GHMP N/C domains) in the UniProt record are all mutually consistent and are corroborated by the primary literature on IspE from *E. coli*, *Plasmodium*, and plants. No conflicting "same-symbol, different-gene" literature was encountered. There is no *P. putida* KT2440–specific experimental paper on this enzyme; the functional assignment for Q88PX5 rests on the HAMAP rule MF_00061 and on high orthology to biochemically and structurally characterized IspE enzymes (chiefly *E. coli*), which is the standard and robust basis for annotating this highly conserved housekeeping enzyme.

---

## 2. Primary Function: The Catalyzed Reaction and Substrate Specificity

**Reaction (EC 2.7.1.148):**

> 4-diphosphocytidyl-2-C-methyl-D-erythritol (CDP-ME) + ATP → 4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P) + ADP

The reaction was first demonstrated biochemically by Lüttgen *et al.* (2000), who identified the then-unannotated *E. coli* *ychB* gene (= *ispE*) as a MEP-pathway enzyme. Comparative genomics showed that *ychB* orthologs co-distribute with *dxs*, *dxr*, and *ygbP* (*ispD*) — genes already known to encode enzymes of the deoxyxylulose-phosphate pathway — suggesting *ychB* also belongs to that pathway. The recombinant protein, purified to homogeneity, "was shown to phosphorylate 4-diphosphocytidyl-2C-methyl-D-erythritol in an ATP-dependent reaction. The reaction product was identified as 4-diphosphocytidyl-2C-methyl-D-erythritol 2-phosphate by NMR" using multiple ¹³C-labeled substrates [PMID 10655484]. The paper's title states the regiochemistry explicitly — the enzyme "phosphorylates the 2-hydroxy group" of CDP-ME [PMID 10655484].

**Substrate specificity.** The physiological phosphoryl acceptor is the cytidine-containing intermediate **CDP-ME**, and the phosphoryl donor is **ATP** (Mg²⁺-dependent, as for GHMP kinases generally). Phosphorylation is strictly **regiospecific for the 2-hydroxyl** of the methylerythritol moiety [PMID 10655484]. This narrow specificity places IspE as a dedicated, committed step of the MEP pathway rather than a promiscuous kinase.

**Downstream fate confirms on-pathway role.** A ¹⁴C-labeled sample of the IspE product (CDP-ME2P) "was converted efficiently into carotenoids by isolated chromoplasts" of *Capsicum annuum* [PMID 10655484], demonstrating that the product is a genuine on-pathway isoprenoid intermediate. In the pathway, CDP-ME2P is next cyclized by IspF (2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase) with release of CMP [PMID 29335298], then reduced by IspG and IspH to yield IPP and DMAPP.

---

## 3. Structure, Family, and Catalytic Mechanism

**Family and fold.** IspE belongs to the **GHMP kinase superfamily** (named for Galactokinase, Homoserine kinase, Mevalonate kinase, and Phosphomevalonate kinase), consistent with the UniProt/InterPro domain set (GHMP N-domain IPR006204; GHMP C-domain IPR013750/IPR036554; IspE-specific IPR004424). GHMP kinases are two-lobed (N- and C-terminal domains) enzymes whose active site lies in the cleft between the domains [PMID 11751891].

**Experimental structures.** *E. coli* IspE has been crystallized as an **IspE–ADP binary complex** and a **ternary complex at ~2 Å resolution**; these confirm that "IspE produces 4-diphosphocytidyl-2C-methyl-D-erythritol 2-phosphate by ATP-dependent phosphorylation of 4-diphosphocytidyl-2C-methyl-D-erythritol" and place the ATP and CDP-ME substrates in the bilobed cleft [PMID 20208151]. Reassessment of the quaternary structure showed that an apparent "triclinic dimer" is a crystal-lattice artefact whose interface occludes the substrate sites, supporting a **functional monomer** [PMID 20208151]. Structural modeling of *Plasmodium* IspE orthologues likewise describes "a critically conserved canonical … (GHMP) domain within the active site lying in a deep cleft sandwiched between ATP and CDPME-binding domains" [PMID 29550587].

**Target-specific sequence confirmation.** The actual *P. putida* KT2440 protein (UniProt `Q88PX5`, `ISPE_PSEPK`, 286 aa, gene *ispE*) contains the diagnostic **GHMP-kinase glycine-rich phosphate-binding motif** `GGGIGGGSSD` (matching the GGG-x-GGGS "motif 2" consensus) in its N-terminal domain, within the context `WLTKVLPM-GGGIGGGSSD-AATTL`. This is the loop that cradles the ATP phosphates for phosphoryl transfer in GHMP kinases, directly corroborating — at the level of the target sequence itself, not merely by orthology — the HAMAP (MF_00061)/InterPro assignment of Q88PX5 to the GHMP-kinase family/IspE subfamily (analysis of the UniProt sequence).

**Catalytic mechanism (inferred from GHMP-family structures).** The active-site cleft contains conserved motifs including a **glycine-rich phosphate-binding loop**, and an **invariant aspartate** near the phosphate-binding site serves as the catalytic residue — in *Methanococcus jannaschii* mevalonate kinase, "Asp(155), an invariant residue …, is located close to the putative phosphate-binding site and has been assumed to play the catalytic role" [PMID 11751891]. QM/MM analysis of the related phosphomevalonate kinase shows that a conserved lysine "functions to neutralize the negative charge developed at the β-, γ-bridging oxygen atom of ATP during phosphoryl transfer," reflecting "the common catalytic mechanism of the GHMP kinase superfamily" [PMID 27676321]. Applied to IspE, the model is: the catalytic aspartate deprotonates the **2-OH** of CDP-ME, generating an alkoxide that performs in-line nucleophilic attack on the ATP γ-phosphate (stabilized by Mg²⁺, the phosphate-binding loop, and the conserved lysine), transferring the phosphate to yield CDP-ME2P + ADP. This explains the strict 2-OH regiospecificity observed experimentally [PMID 10655484].

---

## 4. Pathway Context and Biological Processes

**Pathway position.** IspE is the **fourth enzyme of the MEP (non-mevalonate) pathway** [PMID 29550587]. The full route is: DXS → DXR (IspC) → IspD (CDP-ME synthase) → **IspE (CMK)** → IspF → IspG → IspH → IPP + DMAPP. IspE therefore sits at the committed midpoint, converting the cytidylylated intermediate CDP-ME to CDP-ME2P before ring closure by IspF [PMID 29335298]. The pathway "relies on eight enzyme-catalyzed stages exploiting a range of cofactors and metal ions" [PMID 21619509].

**End-products and physiology.** The MEP pathway supplies IPP and DMAPP, and "all isoprenoids are synthesized by the consecutive condensation of the five-carbon monomer isopentenyl diphosphate (IPP) to its isomer, dimethylallyl diphosphate (DMAPP)" [PMID 22450534]. In bacteria these building blocks are used for functions including "electron transport (e.g., ubiquinone), and cell wall biosynthesis intermediates" [PMID 22450534] (e.g., the undecaprenyl-phosphate carrier lipid for peptidoglycan/O-antigen assembly), as well as carotenoids. Direct isotope-labeling evidence in *E. coli* — a Gram-negative that, like *Pseudomonas*, uses only the MEP pathway — shows that MEP intermediates processed through IspE are incorporated into product isoprenoids: labeled 2-C-methyl-D-erythritol hydrogens appear "without any loss in the prenyl chain of menaquinone and/or ubiquinone on the carbon atoms derived from C-4 of isopentenyl diphosphate (IPP) and on the E-methyl group of dimethylallyl diphosphate (DMAPP)" [PMID 10698701]. Thus IspE activity directly underpins **respiratory quinone biosynthesis** (aerobic/anaerobic electron transport) and cell-envelope biogenesis in *P. putida*.

**Essentiality.** The mevalonate-independent pathway "does not occur in humans, but is present and has been shown to be essential in many dangerous pathogens" [PMID 20208151], and the fourth enzyme "4-diphosphocytidyl-2C-methyl-d-erythritol kinase (IspE) has been proved essential in pathogenic bacteria" [PMID 29550587]. Because *P. putida* is a Gram-negative Proteobacterium possessing a complete MEP pathway and lacking the mevalonate route, IspE is expected to be essential for viability by orthology.

**Subcellular localization.** In bacteria the MEP pathway operates in the **cytoplasm** (there is no signal/transit peptide in the IspE sequence). The distinction is illustrated by the plant/plastid situation, where the orthologue is compartmentalized: the rice OsIspE "encoded protein is targeted to the chloroplast" [PMID 29893915]. For a non-plastid-bearing Gram-negative bacterium such as *P. putida*, the enzyme carries out its function as a soluble cytoplasmic protein.

---

## 5. Translational Significance (Drug Target)

Because the MEP pathway is essential in bacteria and absent in humans, "IspE catalyzes the ATP-dependent phosphorylation of 4-diphosphocytidyl-2-…" and its pathway is regarded as an attractive antibacterial target [PMID 41695590]. Structure-based virtual screening on the *E. coli* IspE crystal structure produced a novel inhibitor class that also showed "activity … against the more pathogenic bacteria *Pseudomonas aeruginosa* and *Acinetobacter baumannii*" [PMID 37718320], and fragment-based campaigns continue to target IspE [PMID 41439264, 41695590]. The cross-activity against *Pseudomonas aeruginosa* supports the inference that IspE performs the same essential function in *P. putida*.

---

## 6. Supported and Refuted Hypotheses

**Supported:**
- **H1 — IspE is CMK (EC 2.7.1.148), the fourth MEP-pathway enzyme.** Supported by UniProt/HAMAP annotation and primary biochemistry [PMID 10655484, 29550587].
- **H2 — Substrate = CDP-ME + ATP; product = CDP-ME2P via 2-OH phosphorylation.** Supported by direct NMR product identification [PMID 10655484] and structural work [PMID 20208151].
- **H3 — GHMP two-domain fold with an inter-domain ATP/CDP-ME cleft, functional monomer.** Supported [PMID 20208151, 29550587, 11751891].
- **H4 — Cytoplasmic localization in bacteria.** Supported by orthology and the contrasting plastid targeting of the plant orthologue [PMID 29893915].
- **H5 — Product feeds IPP/DMAPP → quinones, cell-wall carrier lipids, carotenoids; pathway essential.** Supported [PMID 10698701, 22450534, 29550587, 20208151].

**Refuted / set aside:**
- The crystallographic "dimer" as the biological unit was **refuted**; the functional enzyme is a monomer [PMID 20208151].
- No evidence supports a non-MEP or moonlighting role; IspE's specificity for CDP-ME argues against promiscuous activity.

---

## 7. Limitations and Future Directions

- **No organism-specific study:** All experimental evidence is from orthologues (*E. coli*, *Plasmodium*, plants); the *P. putida* KT2440 enzyme itself has not been individually characterized. Direct kinetic measurement (Km for CDP-ME/ATP, kcat) and gene-essentiality confirmation (e.g., transposon-insertion/conditional-knockout data) in KT2440 would strengthen the annotation.
- **Residue-level mechanism** is inferred from family homologues; an *E. coli*/*Pseudomonas* IspE ternary structure with substrate plus site-directed mutagenesis of the proposed catalytic aspartate would nail down the catalytic base.
- **PubMed search limitations:** The literature interface returned few hits for some highly specific queries; additional classic structural papers (e.g., the original *E. coli* IspE structure) likely exist beyond those retrieved here but are represented indirectly through PMID 20208151.

---

## 8. Key References
- Lüttgen H *et al.* (2000) *PNAS* — IspE/YchB phosphorylates the 2-OH of CDP-ME. **PMID 10655484**
- Kalinowska-Tłuścik J *et al.* (2010) — *E. coli* IspE crystal structures; monomeric functional unit. **PMID 20208151**
- Kadian K *et al.* (2018) — IspE as fourth MEP enzyme, GHMP domain, ATP/CDPME cleft, essentiality. **PMID 29550587**
- Liu *et al.* (2018) — IspF acts on CDP-ME2P, releasing CMP (defines downstream step). **PMID 29335298**
- Yang D *et al.* (2002) — GHMP kinase (mevalonate kinase) fold and catalytic Asp. **PMID 11751891**
- Huang J *et al.* (2016) — GHMP phosphoryl-transfer mechanism (catalytic Lys). **PMID 27676321**
- Charon L *et al.* (2000) — MEP intermediates incorporated into ubiquinone/menaquinone. **PMID 10698701**
- Kuzuyama T & Seto H (2012) — isoprenoid functions; IPP/DMAPP building blocks. **PMID 22450534**
- Hunter WN (2011) — non-mevalonate pathway: eight steps, cofactors/metals, drug target. **PMID 21619509**
- Chen H *et al.* (2018) — plant OsIspE targeted to chloroplast. **PMID 29893915**
- Ropponen H-K *et al.* (2023) — *E. coli* IspE inhibitors active vs *P. aeruginosa*/*A. baumannii*. **PMID 37718320**
- Walsh *et al.* (2026) / (2025) — IspE ATP-dependent phosphorylation; MEP pathway antibacterial target. **PMID 41695590, 41439264**


## Artifacts

- [OpenScientist final report](ispE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ispE-deep-research-openscientist_artifacts/final_report.pdf)