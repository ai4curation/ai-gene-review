---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:24:15.696217'
end_time: '2026-07-18T16:37:27.451377'
duration_seconds: 791.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dxr
  gene_symbol: dxr
  uniprot_accession: Q88MH4
  protein_description: 'RecName: Full=1-deoxy-D-xylulose 5-phosphate reductoisomerase
    {ECO:0000255|HAMAP-Rule:MF_00183}; Short=DXP reductoisomerase {ECO:0000255|HAMAP-Rule:MF_00183};
    EC=1.1.1.267 {ECO:0000255|HAMAP-Rule:MF_00183}; AltName: Full=1-deoxyxylulose-5-phosphate
    reductoisomerase {ECO:0000255|HAMAP-Rule:MF_00183}; AltName: Full=2-C-methyl-D-erythritol
    4-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00183};'
  gene_info: Name=dxr {ECO:0000255|HAMAP-Rule:MF_00183}; OrderedLocusNames=PP_1597;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the DXR family. {ECO:0000255|HAMAP-
  protein_domains: DXP_reductoisomerase. (IPR003821); DXP_reductoisomerase_C. (IPR013644);
    DXP_reductoisomerase_N. (IPR013512); DXPR_C. (IPR026877); DXPR_C_sf. (IPR036169)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dxr-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dxr-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MH4
- **Protein Description:** RecName: Full=1-deoxy-D-xylulose 5-phosphate reductoisomerase {ECO:0000255|HAMAP-Rule:MF_00183}; Short=DXP reductoisomerase {ECO:0000255|HAMAP-Rule:MF_00183}; EC=1.1.1.267 {ECO:0000255|HAMAP-Rule:MF_00183}; AltName: Full=1-deoxyxylulose-5-phosphate reductoisomerase {ECO:0000255|HAMAP-Rule:MF_00183}; AltName: Full=2-C-methyl-D-erythritol 4-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_00183};
- **Gene Information:** Name=dxr {ECO:0000255|HAMAP-Rule:MF_00183}; OrderedLocusNames=PP_1597;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the DXR family. {ECO:0000255|HAMAP-
- **Key Domains:** DXP_reductoisomerase. (IPR003821); DXP_reductoisomerase_C. (IPR013644); DXP_reductoisomerase_N. (IPR013512); DXPR_C. (IPR026877); DXPR_C_sf. (IPR036169)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dxr" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dxr' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dxr** (gene ID: dxr, UniProt: Q88MH4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dxr* (PP_1597, UniProt Q88MH4) in *Pseudomonas putida* KT2440

**Target:** UniProt **Q88MH4** · Gene **dxr** · Ordered locus **PP_1597**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**Enzyme:** 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXR / IspC; AltName "2-C-methyl-D-erythritol 4-phosphate synthase"), **EC 1.1.1.267**

---

## Summary

The gene **dxr** (ordered locus name **PP_1597**; UniProt accession **Q88MH4**) of *Pseudomonas putida* strain KT2440 encodes **1-deoxy-D-xylulose 5-phosphate reductoisomerase** (**DXR**, also known as **IspC**; **EC 1.1.1.267**). This is a soluble, cytoplasmic, NADPH- and divalent-metal-dependent oxidoreductase that catalyzes the **first committed and flux-controlling step** of the **2-C-methyl-D-erythritol 4-phosphate (MEP) pathway** — also called the non-mevalonate or DOXP pathway — of isoprenoid precursor biosynthesis. The enzyme converts **1-deoxy-D-xylulose 5-phosphate (DXP)** into **2-C-methyl-D-erythritol 4-phosphate (MEP)** through a coupled two-step reaction: an intramolecular retro-aldol/aldol rearrangement of DXP to the intermediate 2-C-methyl-D-erythrose 4-phosphate, followed by an NADPH-dependent reduction to MEP.

The gene assignment is unambiguous. The UniProt description, EC number, DXR protein-family membership (InterPro IPR003821), and the diagnostic N-terminal, catalytic, and C-terminal DXR domains (IPR013512, IPR013644, IPR026877, IPR036169) all converge on a single, thoroughly characterized enzyme. The founding biochemical characterization of DXR and multiple crystal structures of orthologous DXR enzymes provide a detailed, self-consistent mechanistic picture that applies directly to the *P. putida* ortholog. Crucially, a study performed **directly in *P. putida* KT2440** confirms that this organism relies exclusively on the MEP pathway (it has no native mevalonate pathway) and explicitly names **dxr** as an active, endogenous, flux-controlling MEP-pathway gene.

Functionally, DXR sits at the head of the pathway that supplies **isopentenyl diphosphate (IPP)** and **dimethylallyl diphosphate (DMAPP)** — the universal five-carbon building blocks of all isoprenoids. In *P. putida*, these precursors feed the biosynthesis of respiratory quinones (ubiquinone), carotenoids, and the essential polyprenol lipid carrier undecaprenyl phosphate (bactoprenol) required for cell-envelope assembly. Because the MEP pathway is essential in most eubacteria and apicomplexan parasites but entirely absent in humans and animals, DXR is a clinically and agriculturally validated drug target — the specific molecular target of the antibiotic/antimalarial/herbicide **fosmidomycin**.

---

## Key Findings

### Finding 1 — DXR catalyzes the NADPH-dependent conversion of DXP to MEP (EC 1.1.1.267)

Enzyme identity is established directly by the UniProt record (Q88MH4: 1-deoxy-D-xylulose 5-phosphate reductoisomerase, EC 1.1.1.267, gene *dxr* / PP_1597) and by membership in the DXR family (IPR003821). The founding biochemical work by Takahashi and colleagues characterized the purified recombinant enzyme and demonstrated the reaction unambiguously: *"The purified recombinant yaeM gene product was overexpressed in E. coli and found to catalyze the formation of 2-C-methyl-D-erythritol 4-phosphate from 1-deoxy-D-xylulose 5-phosphate in the presence of NADPH. Replacement of NADPH with NADH decreased the reaction rate to about 1% of the original rate. The enzyme required Mn2+, Co2+, or Mg2+ as well"* ([PMID: 9707569](https://pubmed.ncbi.nlm.nih.gov/9707569/)).

Three specificity points emerge. First, the reaction is **cofactor-specific for NADPH** — NADH supports only ~1% of the maximal rate, a ~100-fold preference. Second, the enzyme has an **absolute requirement for a divalent metal cation** (Mn²⁺, Co²⁺, or Mg²⁺), which coordinates the substrate and stabilizes the reaction intermediate. Third, the reaction is a genuine **reductoisomerase** activity — an isomerization coupled to a reduction — not a simple hydride transfer. A more recent review reaffirms the assignment: *"The 1-deoxy-d-xylulose-5-phosphate reductoisomerase (DXR; EC1.1.1.267), an NADPH-dependent reductase, plays a pivotal role in the methylerythritol 4-phosphate pathway (MEP), in the conversion of 1-deoxy-d-xylulose-5-phosphate (DXP) into MEP"* ([PMID: 33927975](https://pubmed.ncbi.nlm.nih.gov/33927975/)). DXR is the **second enzyme** and the **first committed step** of the MEP pathway: DXP synthase (the first enzyme) also feeds thiamine and pyridoxal biosynthesis, whereas DXR irreversibly commits carbon to isoprenoids.

### Finding 2 — DXR functions in the cytoplasm within the essential bacterial MEP pathway and is the target of fosmidomycin

The MEP pathway is **essential and phylogenetically restricted**. As summarized by Eisenreich and colleagues, *"The pathway is essential in plants, many eubacteria and apicomplexan parasites, but not in archaea and animals"* ([PMID: 15197467](https://pubmed.ncbi.nlm.nih.gov/15197467/)). *Pseudomonas putida* is a Gram-negative gammaproteobacterium and falls squarely within the eubacteria that depend on this pathway.

DXR is the specific molecular target of the natural-product inhibitor **fosmidomycin**: *"1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXR) has been shown to be the target enzyme of fosmidomycin, an antimalarial, antibacterial and herbicidal compound"* ([PMID: 15567415](https://pubmed.ncbi.nlm.nih.gov/15567415/)). Lichtenthaler's review pinpoints the step: *"The herbicide fosmidomycin specifically blocks the second enzyme, the DOXP reductoisomerase"* ([PMID: 11171208](https://pubmed.ncbi.nlm.nih.gov/11171208/)). Fosmidomycin acts as a slow, tight-binding competitive inhibitor that mimics the substrate and chelates the active-site metal.

Regarding **subcellular localization**: in bacteria such as *P. putida*, DXR is a **soluble cytoplasmic enzyme**. The plastid/chloroplast localization reported for plant DXR orthologs is a plant-specific feature arising from N-terminal transit peptides that are absent in bacterial DXR. The enzyme therefore carries out its function in the bacterial cytosol, where its substrate DXP and cofactor NADPH are generated by central carbon metabolism.

### Finding 3 — *dxr* is an essential gene supplying IPP/DMAPP building blocks for downstream isoprenoids

Genetic evidence establishes essentiality. Disruption studies in *E. coli* show that *"the ability of E. coli extracts to stimulate gamma delta T cell proliferation is abrogated when genes coding for essential enzymes of the MEP pathway, dxr or gcpE, are disrupted or deleted from the bacterial genome"* ([PMID: 11238603](https://pubmed.ncbi.nlm.nih.gov/11238603/)). The abolished activity reflects loss of the phosphoantigen HMBPP, a downstream MEP-pathway metabolite, demonstrating that flux through DXR is required for the pathway to reach its end products.

Mechanistically, the reaction proceeds in two coupled steps: *"which is proposed to be formed from 1-deoxy-D-xylulose 5-phosphate via intramolecular rearrangement followed by reduction process"* ([PMID: 9707569](https://pubmed.ncbi.nlm.nih.gov/9707569/)). DXP first undergoes an intramolecular (retro-aldol/aldol) rearrangement to 2-C-methyl-D-erythrose 4-phosphate, which is then reduced by NADPH to MEP. MEP is subsequently processed by the remaining MEP-pathway enzymes (IspD, IspE, IspF, IspG/GcpE, IspH/LytB) to yield IPP and DMAPP, the universal C5 precursors of all isoprenoids — including respiratory quinones (ubiquinone), carotenoids, and the essential polyprenol carrier undecaprenyl phosphate (bactoprenol) used in peptidoglycan and O-antigen assembly.

### Finding 4 — DXR catalyzes a coupled rearrangement + NADPH-dependent reduction and has no human ortholog

An authoritative medicinal-chemistry review crystallizes the enzyme's function and therapeutic value. DXR *"is a key enzyme of the pathway that catalyzes the rearrangement and nicotinamide adenine dinucleotide phosphate (NADPH)-dependent reduction of 1-deoxy-D-xylulose 5-phosphate (DXP) to MEP"* ([PMID: 17430177](https://pubmed.ncbi.nlm.nih.gov/17430177/)). The same review establishes target selectivity: *"there are no functional equivalents to DXR in humans, making it an attractive target for therapeutic intervention"* ([PMID: 17430177](https://pubmed.ncbi.nlm.nih.gov/17430177/)).

Structural studies illuminate the catalytic cycle. The *E. coli* DXR–NADPH–fosmidomycin ternary crystal structure showed that *"The structure reveals a considerable conformational rearrangement upon fosmidomycin binding and provides insights into the slow, tight binding inhibition mode of the inhibitor"* ([PMID: 15567415](https://pubmed.ncbi.nlm.nih.gov/15567415/)). This closure of an active-site loop upon ligand binding is a hallmark of induced fit, in which the enzyme organizes around the substrate and the catalytic metal to enable the coupled isomerization/reduction.

### Finding 5 — In *P. putida* KT2440, *dxr* is an endogenous MEP-pathway gene supplying isoprenoid precursors from pyruvate + G3P

This is the most direct evidence for the target organism. Hernández-Arranz and colleagues studied *P. putida* KT2440 and reported: *"In P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway, whereas other bacteria synthesize the same precursors from acetyl-CoA using the unrelated mevalonate (MVA) pathway"* ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)). They further named *dxr* explicitly as an endogenous MEP gene: *"we compared lycopene production in cells expressing the Myxococcus xanthus MVA pathway genes or endogenous MEP pathway genes (dxs, dxr, idi)"* ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)).

By engineering these endogenous genes, the authors achieved up to a **50-fold increase in lycopene** production, demonstrating that flux through DXR (together with DXS and IDI) governs isoprenoid precursor availability in this strain. This confirms three things about *P. putida* KT2440: (i) it uses the MEP pathway exclusively and lacks a native mevalonate pathway; (ii) **dxr (PP_1597)** is an active, endogenous, and flux-controlling component of that pathway; and (iii) the pathway begins from the central-metabolism intermediates **pyruvate and glyceraldehyde 3-phosphate (G3P)**.

### Finding 6 — DXR is a homodimeric, three-domain enzyme with conserved catalytic acidic residues and a gating loop

Two independent crystal structures of *E. coli* DXR (the closest well-characterized ortholog to *P. putida* Q88MH4, sharing the same DXR family and domain architecture) define the enzyme's fold. Reuter and colleagues reported: *"Each monomer displays a V-like shape and is composed of an amino-terminal dinucleotide binding domain, a connective domain, and a carboxyl-terminal four-helix bundle domain. The connective domain is responsible for dimerization and harbors most of the active site"* ([PMID: 11741911](https://pubmed.ncbi.nlm.nih.gov/11741911/)). The enzyme is a **homodimer**, and each protomer has three domains: an N-terminal Rossmann-like NADPH-binding domain, a central catalytic/connective domain, and a C-terminal helical domain.

The same study identified the catalytic residues that coordinate the essential divalent metal: *"The strictly conserved acidic residues Asp(150), Glu(152), Glu(231), and Glu(234) are clustered at the putative active site and are probably involved in the binding of divalent cations mandatory for enzyme activity"* ([PMID: 11741911](https://pubmed.ncbi.nlm.nih.gov/11741911/)). A highly flexible loop (residues ~186–216) was implicated in induced fit upon substrate binding. Yajima and colleagues, solving the NADPH complex, independently noted *"the presence of an extra domain, which is absent from other NADPH-dependent oxidoreductases"* and that *"A flexible loop covering the substrate binding site plays an important role in the enzymatic reaction and the determination of substrate specificity"* ([PMID: 11872159](https://pubmed.ncbi.nlm.nih.gov/11872159/)). This structural picture maps directly onto the InterPro domain assignment for Q88MH4 (IPR013512 N-terminal NADPH-binding; catalytic middle; IPR013644/IPR026877/IPR036169 C-terminal), confirming that the *P. putida* enzyme adopts the same architecture.

---

## Mechanistic Model / Interpretation

### The catalyzed reaction

DXR performs a two-step, single-active-site conversion:

```
   DXP (1-deoxy-D-xylulose 5-phosphate)
        |
        |  Step 1: intramolecular retro-aldol / aldol
        |          rearrangement (isomerase activity)
        |          requires divalent metal (Mn2+/Co2+/Mg2+)
        v
   2-C-methyl-D-erythrose 4-phosphate   (bound intermediate)
        |
        |  Step 2: NADPH-dependent reduction (reductase activity)
        |          hydride transfer from NADPH; NADH ~100x slower
        v
   MEP (2-C-methyl-D-erythritol 4-phosphate)
```

The "reductoisomerase" name reflects that a single enzyme couples an **isomerization** (skeletal rearrangement of the carbon backbone from a straight-chain to a branched-chain sugar phosphate) with a **reduction** (NADPH-driven). The divalent metal cation, held by the conserved acidic residues (Asp150, Glu152, Glu231, Glu234 in *E. coli* numbering), is essential for both steps — it polarizes the substrate carbonyl and stabilizes the developing negative charge during rearrangement.

### Position in the MEP pathway and downstream fate in *P. putida*

```
 Pyruvate + Glyceraldehyde-3-phosphate (G3P)   [central carbon metabolism]
        |
        |  DXS (Dxs, 1-deoxy-D-xylulose-5-phosphate synthase)
        v
       DXP  ───────────────► (also feeds thiamine / PLP biosynthesis)
        |
        |  ***DXR / IspC (PP_1597, Q88MH4)***  ← THIS ENZYME
        |  NADPH + divalent metal; first committed step
        v
       MEP
        |
        |  IspD → IspE → IspF → IspG(GcpE) → IspH(LytB)
        v
   IPP  ⇌  DMAPP     (universal C5 isoprenoid building blocks)
        |
        +──► Ubiquinone (respiratory electron transport)
        +──► Carotenoids / lycopene
        +──► Undecaprenyl phosphate (bactoprenol; cell-envelope assembly)
        +──► Other prenylated metabolites
```

DXR occupies the **first committed step**: DXS-produced DXP can be diverted to thiamine and pyridoxal cofactor synthesis, but once DXR converts DXP to MEP, carbon is irreversibly committed to the isoprenoid pathway. This positioning, combined with the demonstrated 50-fold flux control in *P. putida* engineering experiments ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)), makes DXR a key control point.

### Localization and physiological role

| Property | Assignment | Basis |
|---|---|---|
| Reaction | DXP → MEP (EC 1.1.1.267) | [PMID: 9707569](https://pubmed.ncbi.nlm.nih.gov/9707569/) |
| Cofactor | NADPH (strong preference over NADH) | [PMID: 9707569](https://pubmed.ncbi.nlm.nih.gov/9707569/) |
| Metal | Mn²⁺ / Co²⁺ / Mg²⁺ (mandatory) | [PMID: 9707569](https://pubmed.ncbi.nlm.nih.gov/9707569/), [PMID: 11741911](https://pubmed.ncbi.nlm.nih.gov/11741911/) |
| Oligomeric state | Homodimer | [PMID: 11741911](https://pubmed.ncbi.nlm.nih.gov/11741911/) |
| Domains | N-terminal NADPH-binding; central catalytic; C-terminal helical | [PMID: 11741911](https://pubmed.ncbi.nlm.nih.gov/11741911/), [PMID: 11872159](https://pubmed.ncbi.nlm.nih.gov/11872159/) |
| Localization | Bacterial cytoplasm (soluble) | Inference; plastid targeting is plant-specific |
| Pathway | MEP / non-mevalonate isoprenoid pathway (committed step) | [PMID: 15197467](https://pubmed.ncbi.nlm.nih.gov/15197467/) |
| Essentiality | Essential | [PMID: 11238603](https://pubmed.ncbi.nlm.nih.gov/11238603/) |
| Human ortholog | None | [PMID: 17430177](https://pubmed.ncbi.nlm.nih.gov/17430177/) |
| Inhibitor | Fosmidomycin (slow, tight-binding) | [PMID: 15567415](https://pubmed.ncbi.nlm.nih.gov/15567415/) |

---

## Evidence Base

| PMID | Paper (abbreviated) | How it supports the annotation |
|---|---|---|
| [9707569](https://pubmed.ncbi.nlm.nih.gov/9707569/) | Takahashi et al., 1998 — founding DXR characterization | Purified enzyme converts DXP→MEP; NADPH-specific (NADH ~1%); requires Mn²⁺/Co²⁺/Mg²⁺; two-step rearrangement-then-reduction mechanism |
| [33927975](https://pubmed.ncbi.nlm.nih.gov/33927975/) | In silico characterization/expression of DXR | Confirms EC 1.1.1.267, NADPH dependence, DXP→MEP conversion in the MEP pathway |
| [15197467](https://pubmed.ncbi.nlm.nih.gov/15197467/) | Eisenreich et al., 2004 — non-mevalonate pathway review | Establishes MEP-pathway essentiality in eubacteria and absence in animals |
| [15567415](https://pubmed.ncbi.nlm.nih.gov/15567415/) | Mac Sweeney et al., 2005 — DXR·NADPH·fosmidomycin structure | Identifies DXR as fosmidomycin target; conformational closure; slow tight-binding inhibition |
| [11171208](https://pubmed.ncbi.nlm.nih.gov/11171208/) | Lichtenthaler, 2000 — enzymes/genes/inhibitors review | Confirms DXR is the second pathway enzyme and specific fosmidomycin target |
| [11238603](https://pubmed.ncbi.nlm.nih.gov/11238603/) | Altincicek et al., 2001 — γδ T-cell activation | Genetic evidence that *dxr* is essential; disruption abolishes downstream metabolite production |
| [17430177](https://pubmed.ncbi.nlm.nih.gov/17430177/) | Singh et al., 2007 — DXR inhibition review | Coupled rearrangement + NADPH reduction; no human functional equivalent |
| [31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) | Hernández-Arranz et al., 2019 — *P. putida* engineering | Direct target-organism evidence: P. putida uses MEP pathway from pyruvate + G3P; *dxr* endogenous, flux-controlling |
| [11741911](https://pubmed.ncbi.nlm.nih.gov/11741911/) | Reuter et al., 2002 — DXR crystal structure | Homodimeric three-domain fold; conserved catalytic acidic residues coordinating divalent metal; flexible loop |
| [11872159](https://pubmed.ncbi.nlm.nih.gov/11872159/) | Yajima et al., 2002 — DXR·cofactor structure | Unique extra domain; flexible loop governs catalysis and substrate specificity |

The evidence base is highly consistent. All ten primary references converge on a single, well-defined enzyme, and there is **no conflicting literature** suggesting an alternative function for the *dxr* gene product. The one important caveat is that the detailed biochemical and structural data derive from orthologs (chiefly *E. coli*, plus reviews spanning *Plasmodium*, *Mycobacterium*, and plants) rather than from the *P. putida* protein itself. However, the target-organism study ([PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)) ties the annotation directly to *P. putida* KT2440, and strict conservation of the DXR family, catalytic residues, and domain architecture makes cross-species inference robust.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* Q88MH4 protein.** Kinetic parameters (kcat, Km for DXP and NADPH), metal preference, and inhibitor sensitivity have not been measured for this specific ortholog. The functional assignment relies on strong orthology to biochemically characterized DXR enzymes (primarily *E. coli*) plus the target-organism engineering study.

2. **No experimentally solved structure of the *P. putida* enzyme.** The three-domain, homodimeric architecture and catalytic-residue identities are inferred from *E. coli* structures and the InterPro/HAMAP domain assignments, not from a *P. putida* crystal or cryo-EM structure. An AlphaFold model could be validated but has not been analyzed here.

3. **Essentiality inferred, not directly demonstrated in *P. putida*.** The essentiality evidence is from *E. coli* gene-disruption studies. Because *P. putida* KT2440 relies exclusively on the MEP pathway (confirmed in [PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)), *dxr* is expected to be essential, but a targeted knockout/conditional-depletion experiment in KT2440 has not been reported here.

4. **Localization is inferred.** Cytoplasmic localization follows from the absence of signal/transit peptides and the soluble nature of bacterial DXR, but has not been experimentally confirmed for PP_1597 (e.g., by fractionation or fluorescent tagging).

5. **Regulation and operon context unexplored.** How *dxr* transcription/translation is regulated in *P. putida*, its genomic/operon context, and any post-translational control remain outside the scope of the current evidence.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme kinetics.** Clone and purify PP_1597, and measure steady-state kinetics for DXP and NADPH plus divalent-metal preference (Mn²⁺ vs Mg²⁺ vs Co²⁺). This confirms the reaction and quantifies substrate specificity directly for the *P. putida* enzyme.

2. **Fosmidomycin sensitivity assay.** Test whether purified PP_1597 is inhibited by fosmidomycin (IC50, slow/tight-binding behavior), and whether *P. putida* KT2440 growth is fosmidomycin-sensitive and rescuable by MEP/isoprenoid precursor supplementation — establishing on-target inhibition.

3. **Conditional knockout / depletion in KT2440.** Construct a conditional *dxr* mutant (inducible promoter or CRISPRi) to demonstrate essentiality directly and characterize the terminal phenotype (loss of quinones, carotenoids, undecaprenyl phosphate).

4. **Structural determination or AlphaFold validation.** Solve the *P. putida* DXR structure, or validate an AlphaFold2 model (pLDDT/PAE), confirming the homodimeric three-domain fold, the metal-binding acidic cluster, and the gating loop.

5. **Metabolic flux analysis.** Quantify how *dxr* overexpression or repression shifts MEP-pathway flux and downstream isoprenoid titers in KT2440, building on the reported 50-fold lycopene improvement, to formally position DXR as a flux-controlling node.

6. **Subcellular localization confirmation.** Use cell fractionation or a fluorescent fusion to verify cytoplasmic localization of PP_1597.

---

## Conclusion

The gene *dxr* / PP_1597 (UniProt Q88MH4) of *Pseudomonas putida* KT2440 encodes **1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXR/IspC, EC 1.1.1.267)**, a cytoplasmic, homodimeric, NADPH- and divalent-metal-dependent enzyme that catalyzes the first committed step of the essential MEP (non-mevalonate) isoprenoid pathway — the coupled rearrangement and reduction of DXP to MEP. Its product feeds IPP/DMAPP biosynthesis, supplying the universal precursors for quinones, carotenoids, and the undecaprenyl-phosphate lipid carrier in *P. putida*. The assignment is well-supported, internally consistent across biochemical, structural, genetic, and target-organism metabolic-engineering studies, and free of ambiguity. Because DXR has no human counterpart, it is a validated selective target of the antibiotic/antimalarial/herbicide fosmidomycin.


## Artifacts

- [OpenScientist final report](dxr-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dxr-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9707569
2. PMID:33927975
3. PMID:15197467
4. PMID:15567415
5. PMID:11171208
6. PMID:11238603
7. PMID:17430177
8. PMID:31500633
9. PMID:11741911
10. PMID:11872159