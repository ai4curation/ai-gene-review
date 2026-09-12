---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:49:12.121833'
end_time: '2026-07-23T14:02:22.332944'
duration_seconds: 790.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murB
  gene_symbol: murB
  uniprot_accession: Q88LM5
  protein_description: 'RecName: Full=UDP-N-acetylenolpyruvoylglucosamine reductase
    {ECO:0000255|HAMAP-Rule:MF_00037}; EC=1.3.1.98 {ECO:0000255|HAMAP-Rule:MF_00037};
    AltName: Full=UDP-N-acetylmuramate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_00037};'
  gene_info: Name=murB {ECO:0000255|HAMAP-Rule:MF_00037}; OrderedLocusNames=PP_1904;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MurB family. {ECO:0000255|HAMAP-
  protein_domains: FAD-bd_PCMH. (IPR016166); FAD-bd_PCMH-like_sf. (IPR036318); FAD-bd_PCMH_sub1.
    (IPR016167); FAD-bd_PCMH_sub2. (IPR016169); MurB. (IPR003170)
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
  path: murB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LM5
- **Protein Description:** RecName: Full=UDP-N-acetylenolpyruvoylglucosamine reductase {ECO:0000255|HAMAP-Rule:MF_00037}; EC=1.3.1.98 {ECO:0000255|HAMAP-Rule:MF_00037}; AltName: Full=UDP-N-acetylmuramate dehydrogenase {ECO:0000255|HAMAP-Rule:MF_00037};
- **Gene Information:** Name=murB {ECO:0000255|HAMAP-Rule:MF_00037}; OrderedLocusNames=PP_1904;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MurB family. {ECO:0000255|HAMAP-
- **Key Domains:** FAD-bd_PCMH. (IPR016166); FAD-bd_PCMH-like_sf. (IPR036318); FAD-bd_PCMH_sub1. (IPR016167); FAD-bd_PCMH_sub2. (IPR016169); MurB. (IPR003170)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murB** (gene ID: murB, UniProt: Q88LM5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MurB (Q88LM5, PP_1904) — *Pseudomonas putida* KT2440

## 1. Summary / Answer

**MurB (UniProt Q88LM5; gene *murB*; ordered locus PP_1904) of *Pseudomonas putida* KT2440 is UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98; also called UDP-N-acetylmuramate dehydrogenase).** It is a cytoplasmic, monomeric FAD-dependent flavoenzyme that catalyzes the second committed step of the cytoplasmic phase of peptidoglycan (cell-wall) biosynthesis: the NADPH-dependent reduction of the enolpyruvyl group of UDP-N-acetylglucosamine-enolpyruvate (the product of MurA) to yield UDP-N-acetylmuramic acid (UDP-MurNAc), the essential precursor that MurC–MurF subsequently convert into UDP-MurNAc-pentapeptide. The enzyme is essential for viability and is a validated antibacterial drug target.

### Gene-identity verification
The gene symbol **murB** matches the UniProt protein description (UDP-N-acetylenolpyruvoylglucosamine reductase, EC 1.3.1.98, MurB family), the organism (*Pseudomonas putida* KT2440), and the domain architecture (FAD-bd_PCMH cofactor-binding fold; MurB signature IPR003170). The literature retrieved is unambiguously for this enzyme family. No mechanistic study exists on the *P. putida* KT2440 protein itself; however, the enzyme is one of the most thoroughly characterized in bacterial cell-wall biology, and — importantly — a high-resolution crystal structure exists for the ortholog from the same genus, *Pseudomonas aeruginosa* MurB (PMID 23805286), providing a strong basis for direct inference. Function is therefore assigned by (i) unambiguous family/domain membership and (ii) homology to biochemically and structurally characterized MurB enzymes, most closely the *Pseudomonas* ortholog.

---

## 2. Primary Function: the reaction catalyzed

MurB catalyzes:

> **UDP-N-acetyl-3-O-(1-carboxyvinyl)-D-glucosamine (enolpyruvyl-UDP-GlcNAc) + NADPH + H⁺ → UDP-N-acetylmuramate (UDP-MurNAc) + NADP⁺**

This is the reductive conversion of an enol ether to the D-lactyl ether that defines N-acetylmuramic acid. In the Mur pathway, MurA first transfers phosphoenolpyruvate onto UDP-GlcNAc to make the enolpyruvyl adduct; **MurB then reduces that enolpyruvyl group**, completing formation of UDP-MurNAc (Benson et al., PMID 8448160; Benson, Walsh & Hogle, PMID 8805513).

**Substrate specificity.** The physiological substrates are highly specific: the sugar-nucleotide **enolpyruvyl-UDP-GlcNAc** as the reducible substrate and **NADPH** (not NADH) as the hydride donor. The enzyme contains one tightly, stoichiometrically bound **FAD** cofactor that is reduced and re-oxidized during each catalytic cycle (PMID 8448160). The *E. coli* enzyme is a 38-kDa monomer purified to homogeneity with catalytically competent FAD (PMID 8448160).

---

## 3. Catalytic Mechanism (flavin-mediated, two half-reactions)

MurB is a classic example of a flavoenzyme running a **ping-pong (two-half-reaction) mechanism** at a single active site:

1. **Reductive half-reaction (NADPH → FAD).** A hydride is transferred from NADPH — specifically the **4-pro-S hydrogen** — to enzyme-bound FAD, generating FADH₂ (Benson et al., PMID 8448160). In the *P. aeruginosa* ternary complex, the NADP⁺ nicotinamide ring stacks against the **si face of the FAD isoalloxazine**, an unusual geometry for hydride transfer (Chen et al., PMID 23805286).

2. **Oxidative half-reaction (FADH₂ → enolpyruvyl substrate).** FADH₂ reduces the enolpyruvyl group: a **hydride is delivered to the β-methyl** of the incipient 3-O-lactyl moiety while a **proton from solvent adds to the α-carbon**, producing the D-lactyl ether of UDP-MurNAc (PMID 8448160). **Ser229 is the catalytic proton donor** for this step — the S229A mutant suffers an ~10⁷-fold kinetic defect in the second half-reaction (Benson, Walsh & Hogle, PMID 9020778).

**Single shared active site.** After NADP⁺ departs, the sugar-nucleotide binds the *same* pocket used by the nicotinamide. In *P. aeruginosa* MurB, both substrates share a binding site located between two lobes of substrate-binding **domain III**, with the nicotinamide and enolpyruvyl moieties strikingly superimposable and both poised for hydride exchange with FAD; a **potassium ion** in the active site aids substrate orientation, and channel flexibility lets the non-reactive parts of the two substrates adopt different conformations (PMID 23805286).

**Conformational gating.** Substrate binding drives a large motion of **domain 3 (residues ~219–319)** that closes the substrate channel over the ligand; the Tyr190/Tyr254 stacking pair is disrupted, and Tyr190 swings over to hydrogen-bond the α-phosphate of the sugar-nucleotide (Benson, Walsh & Hogle, PMID 8805513). NMR confirmed that NADP⁺ binding induces chemical-shift changes across both the sugar-nucleotide and FAD pockets (Constantine et al., PMID 9150408).

**Conserved catalytic residues.** Site-directed mutagenesis in *S. aureus* MurB defined distinct roles: **Arg213** maintains the FAD electronic state, **Arg176** binds the enolpyruvyl-UDP-GlcNAc substrate, and **His259** contacts both the sugar-nucleotide and NADP⁺ (Nishida et al., PMID 16236703). These residues are expected to be conserved in the *P. putida* ortholog.

---

## 4. Subcellular Localization

MurB functions in the **cytoplasm**. Peptidoglycan biosynthesis is compartmentalized across cytoplasm, inner membrane, and periplasm; the **cytoplasmic phase forms the soluble nucleotide precursors** through the Mur enzymes, converting UDP-GlcNAc into UDP-MurNAc-pentapeptide (Amera et al., PMID 42128180). MurB is explicitly described as catalyzing "an essential cytoplasmic step in the synthesis of peptidoglycan" (Shapiro et al., PMID 22068704). It is a soluble, monomeric protein with no membrane-spanning segments (consistent with the FAD-bd_PCMH soluble fold), acting on freely diffusible sugar-nucleotide substrates before the pathway moves to the membrane (MraY/MurG produce lipid I/II).

---

## 5. Pathway Context and Biological Process

MurB occupies a fixed, non-redundant position in the linear **Mur (peptidoglycan precursor) pathway**:

```
UDP-GlcNAc
   │  MurA (enolpyruvyl transfer from PEP)
   ▼
enolpyruvyl-UDP-GlcNAc
   │  MurB  ◄── NADPH + FAD   (THIS ENZYME, EC 1.3.1.98)
   ▼
UDP-MurNAc
   │  MurC (add L-Ala)
   ▼
UDP-MurNAc-L-Ala → (MurD, MurE, MurF) → UDP-MurNAc-pentapeptide
   │  MraY / MurG (membrane) → Lipid I / Lipid II
   ▼
peptidoglycan (periplasm)
```

MurB's product UDP-MurNAc is the demonstrated substrate for the next enzyme MurC (UDP-MurNAc:L-alanine ligase), as shown by coupled enzymatic synthesis using MurA (MurZ) + MurB to make UDP-MurNAc that then supports the MurC ligase reaction (Raymond et al., PMID 14659546; see also MurC structure/function, Seo et al., PMID 33950018). The broader biological process is **biosynthesis of the murein sacculus**, required for cell growth, elongation, division, and osmotic protection (Dhar et al., PMID 29185941).

---

## 6. Essentiality and Physiological Importance

- **Genetic essentiality.** In *Bacillus subtilis*, *murB* lies in the **dcw ("division and cell wall") cluster** immediately upstream of *divIB*; attempts to inactivate it were unsuccessful, and growth rate, morphology, and antibiotic resistance depend on the MurB expression level (Real & Henriques, PMID 16484183).
- **Conditional-lethal genetics.** In *Staphylococcus aureus*, temperature-sensitive *murB* point mutants **halt peptidoglycan synthesis** at the restrictive temperature with reduced reductase activity, confirming *murB* is essential for growth; five of six causal mutations map to substrate-binding domain 3 (Matsuo et al., PMID 12757953; Nishida et al., PMID 16236703).
- **Drug-target validation.** Because interrupting this step is lethal and the enzyme has no human counterpart, MurB is an actively pursued antibacterial target: multiple inhibitor classes (4-thiazolidinones, 3,5-dioxopyrazolidines/pyrazolidine-3,5-diones, tetrazoles) inhibit MurB and reduce peptidoglycan synthesis and bacterial growth (Yang et al., PMID 16436710; Gilbert et al., PMID 17004716; Hrast et al., PMID 29363274), and dedicated high-throughput assays have been developed (Shapiro et al., PMID 22068704).

For *P. putida* (an environmental, non-pathogenic soil bacterium and biotechnology chassis), MurB performs the same housekeeping role in building and maintaining the Gram-negative cell wall; its essentiality is inferred from the universal conservation and demonstrated essentiality of MurB across bacteria.

---

## 7. Evidence Basis and Confidence

| Claim | Evidence type | Confidence |
|-------|---------------|-----------|
| Reaction catalyzed (enolpyruvyl-UDP-GlcNAc → UDP-MurNAc; NADPH-dependent) | Direct biochemistry (E. coli), family/domain annotation | High |
| FAD cofactor, monomer, 4-pro-S NADPH hydride | Direct biochemistry (PMID 8448160) | High |
| Ping-pong, single-site mechanism; NADP⁺/FAD geometry | X-ray structures incl. **same-genus P. aeruginosa** (PMID 23805286) | High |
| Ser229 proton donor; Arg/His/Tyr active-site network | Mutagenesis + structure (PMID 9020778, 16236703, 8805513) | High for family; inferred for PP_1904 |
| Cytoplasmic localization | Pathway/biochemical consensus (PMID 22068704, 42128180) | High |
| Pathway position (MurA→MurB→MurC) | Coupled enzymatic reconstitution (PMID 14659546) | High |
| Essentiality | Genetics in B. subtilis/S. aureus (PMID 16484183, 12757953) | High for bacteria; inferred for P. putida |

**Key inference note:** All mechanistic/structural data derive from orthologs (E. coli, S. aureus, T. caldophilus, and — closest — P. aeruginosa). Given >universal conservation of MurB catalytic residues and the availability of a *Pseudomonas* structure, transfer of annotation to *P. putida* PP_1904 is well supported.

---

## 8. Supported vs. Refuted Hypotheses

**Supported:**
- MurB (Q88LM5) is the FAD-dependent UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98). ✔
- It uses NADPH and a two-half-reaction flavin mechanism at a single active site. ✔
- It functions in the cytoplasm, upstream of MurC. ✔
- It is essential and a validated antibacterial target. ✔

**Refuted / excluded:**
- Not a membrane transporter, structural/adapter protein, or signaling molecule — it is a soluble metabolic oxidoreductase. ✔
- Does not use NADH preferentially (NADPH-specific). ✔
- Gene-symbol ambiguity: **not applicable** — literature is abundant and specific to this exact enzyme family; no conflicting "murB" gene in other organisms was encountered.

---

## 9. Limitations and Future Directions

- **No direct study of PP_1904** exists; function is assigned by homology (strongly supported by the *P. aeruginosa* structure). A recombinant enzyme assay or complementation of an *E. coli murB(Ts)* strain with PP_1904 would give direct confirmation.
- Kinetic parameters (kcat, Km for enolpyruvyl-UDP-GlcNAc and NADPH) specific to *P. putida* are unknown.
- Whether *P. putida* MurB participates in any species-specific protein–protein interactions with divisome/elongasome components (as reviewed generally in PMID 27136593) has not been examined.
- Potential *P. putida*-specific roles in stress/solvent tolerance (a hallmark of this organism) via cell-wall remodeling remain unexplored.

---

## References (PMIDs)
8448160 (Benson et al. 1993, mechanism); 8805513 (Benson, Walsh & Hogle 1996, substrate-free structure); 9020778 (Benson, Walsh & Hogle 1997, S229A); 9150408 (Constantine et al. 1997, NMR); 23805286 (Chen et al. 2013, *P. aeruginosa* MurB structure); 16236703 (Nishida et al. 2006, S. aureus active-site residues); 12757953 (Matsuo et al. 2003, S. aureus Ts mutants); 16484183 (Real & Henriques 2006, B. subtilis dcw/essentiality); 14659546 (Raymond et al. 2003, MurA+MurB→UDP-MurNAc→MurC); 33950018 (Seo et al. 2021, MurC); 22068704 (Shapiro et al. 2012, cytoplasmic/essential, assay); 29363274 (Hrast et al. 2018, inhibitors); 16436710 (Yang et al. 2006, inhibitors + E. coli structure); 17004716 (Gilbert et al. 2006, inhibitors); 42128180 (Amera et al. 2026, Mur enzyme review); 29185941 (Dhar et al. 2018, E. coli/P. aeruginosa cell-wall review); 12492849 (El Zoeiby et al. 2003, Mur enzyme review); 16934839 (Smith 2006, Mur ligases); 27136593 (Laddomada et al. 2016, cell-wall protein complexes).


## Artifacts

- [OpenScientist final report](murB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murB-deep-research-openscientist_artifacts/final_report.pdf)