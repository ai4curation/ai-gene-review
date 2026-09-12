---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T14:02:25.799209'
end_time: '2026-07-23T14:15:36.694815'
duration_seconds: 790.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murD
  gene_symbol: murD
  uniprot_accession: Q88N78
  protein_description: 'RecName: Full=UDP-N-acetylmuramoylalanine--D-glutamate ligase
    {ECO:0000255|HAMAP-Rule:MF_00639}; EC=6.3.2.9 {ECO:0000255|HAMAP-Rule:MF_00639};
    AltName: Full=D-glutamic acid-adding enzyme {ECO:0000255|HAMAP-Rule:MF_00639};
    AltName: Full=UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase {ECO:0000255|HAMAP-Rule:MF_00639};'
  gene_info: Name=murD {ECO:0000255|HAMAP-Rule:MF_00639}; OrderedLocusNames=PP_1335;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MurCDEF family. {ECO:0000255|HAMAP-
  protein_domains: Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf.
    (IPR036615); Mur_ligase_cen. (IPR013221); MurD. (IPR005762)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N78
- **Protein Description:** RecName: Full=UDP-N-acetylmuramoylalanine--D-glutamate ligase {ECO:0000255|HAMAP-Rule:MF_00639}; EC=6.3.2.9 {ECO:0000255|HAMAP-Rule:MF_00639}; AltName: Full=D-glutamic acid-adding enzyme {ECO:0000255|HAMAP-Rule:MF_00639}; AltName: Full=UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase {ECO:0000255|HAMAP-Rule:MF_00639};
- **Gene Information:** Name=murD {ECO:0000255|HAMAP-Rule:MF_00639}; OrderedLocusNames=PP_1335;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MurCDEF family. {ECO:0000255|HAMAP-
- **Key Domains:** Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf. (IPR036615); Mur_ligase_cen. (IPR013221); MurD. (IPR005762)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murD** (gene ID: murD, UniProt: Q88N78) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *murD* (Q88N78, PP_1335) in *Pseudomonas putida* KT2440

## Summary

The gene **murD** (UniProt accession **Q88N78**; ordered locus name **PP_1335**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes **MurD**, the enzyme **UDP-N-acetylmuramoyl-L-alanine—D-glutamate ligase** (EC 6.3.2.9), also named the **D-glutamic acid-adding enzyme** or **UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase**. MurD is an ATP-dependent, amide-bond-forming ligase belonging to the **MurCDEF (Mur ligase) family**. It catalyzes the second amino-acid-adding step in the cytoplasmic assembly of the peptidoglycan precursor, specifically the stereospecific addition of **D-glutamate** onto the growing UDP-MurNAc stem peptide. The gene identity was verified against the UniProt record: the gene symbol, organism, EC number, family membership (MurCDEF), and diagnostic InterPro domain signatures—the MurD-specific signature IPR005762 together with the Mur ligase central domain (IPR013221) and C-terminal domain (IPR004101)—are all mutually consistent, confirming that the correct protein is being described. The identity is unambiguous.

The reaction catalyzed is: **UDP-MurNAc-L-Ala + D-glutamate + ATP → UDP-MurNAc-L-Ala-D-Glu + ADP + Pi.** The best-characterized ortholog, *Escherichia coli* MurD, has been studied extensively by kinetics, crystallography, and computational chemistry and provides the mechanistic template for the *P. putida* enzyme. Catalysis proceeds by an **ordered mechanism**: the C-terminal carboxylate of UDP-MurNAc-L-Ala is first activated by phosphoryl transfer from ATP to form an **acyl-phosphate intermediate**, which is then attacked by the amino group of D-glutamate to give a **tetrahedral intermediate** that collapses to form the new amide bond and release inorganic phosphate. MurD is a **three-domain protein** that undergoes a large substrate-induced domain closure to bring the reactants into catalytically competent geometry.

Functionally, MurD operates in the **bacterial cytoplasm** as the second of four consecutive Mur ligases (MurC→MurD→MurE→MurF) that build the UDP-MurNAc-pentapeptide, the soluble precursor subsequently handed to the membrane enzymes MraY and MurG. This intracellular pathway is coordinated with the divisome and elongasome machineries that govern cell division and cell-wall elongation. Because peptidoglycan biosynthesis is essential and specific to bacteria—with no human homolog—MurD is a well-recognized and validated **target for antibacterial drug design**.

---

## Key Findings

### Finding 1 — MurD is the ATP-dependent D-glutamate-adding ligase (EC 6.3.2.9) of peptidoglycan biosynthesis

The primary function of the *murD* gene product is unambiguous. UniProt Q88N78 annotates the *P. putida* KT2440 gene *murD* (PP_1335) as **UDP-N-acetylmuramoylalanine—D-glutamate ligase, EC 6.3.2.9**, a member of the **MurCDEF family**, carrying the MurD-specific domain signature **IPR005762** and the Mur ligase central and C-terminal domains (**IPR013221**, **IPR004101**). These signatures are diagnostic of the Mur ligase fold; IPR005762 in particular identifies the enzyme specifically as MurD rather than one of its paralogs (MurC, MurE, MurF).

The biochemical reaction is defined by studies of characterized orthologs. A crystallographic study of MurD states directly that "*MurD catalyzes the addition of D-glutamic acid to UDP-MurNAc-L-Ala in the presence of ATP*" ([PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/)). A dedicated review of MurD enzymes reinforces the substrate specificity and cofactor requirement: "*MurD is responsible for the ATP-dependent addition of d-glutamic acid to UDP-MurNAc-l-Ala*" ([PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/)). The net transformation is:

```
UDP-MurNAc-L-Ala  +  D-glutamate  +  ATP
        │
        ▼   MurD (EC 6.3.2.9)
UDP-MurNAc-L-Ala-D-Glu  +  ADP  +  Pi
```

Two aspects of substrate specificity deserve emphasis. First, MurD is **stereospecific for the D-isomer of glutamate**—the acceptor amino acid is D-glutamic acid, a non-proteinogenic amino acid characteristic of the bacterial cell wall (the D-Glu is supplied *in vivo* by glutamate racemase, MurI). This stereospecificity is the basis of D-Glu-scaffold inhibitor design against MurD ([PMID: 23990043](https://pubmed.ncbi.nlm.nih.gov/23990043/)). Second, MurD acts only after MurC has added L-alanine; its acceptor substrate is the UDP-MurNAc-L-Ala product of the preceding step. This strict ordering gives the Mur ligase pathway its defined, sequential architecture.

### Finding 2 — MurD uses an ordered, ATP-driven mechanism through acyl-phosphate and tetrahedral intermediates

MurD's catalytic mechanism has been dissected in the *E. coli* ortholog and is shared across the Mur ligase family. The C-terminal (L-Ala) carboxylate of UDP-MurNAc-L-Ala is activated by phosphoryl transfer from the ATP γ-phosphate, generating a reactive **acyl-phosphate intermediate**. The amino group of the incoming D-glutamate then performs a nucleophilic attack on this activated carbonyl, forming a high-energy **tetrahedral intermediate**. Collapse of the tetrahedral intermediate expels inorganic phosphate and forms the amide (peptide) bond, while ATP is consumed to ADP + Pi.

The MurD review states this directly: the enzyme carries out "*the ATP-dependent addition of d-glutamic acid to UDP-MurNAc-l-Ala, a reaction which involves acyl-phosphate and tetrahedral intermediates*" ([PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/)). Direct experimental evidence for the acyl-phosphate intermediate comes from a comparative study of the *E. coli* MurC and MurD synthetases, which found that "*MurD, but not MurC, catalyses the synthesis of adenosine 5'-tetraphosphate from the acyl phosphate, thereby substantiating its existence*" ([PMID: 10403366](https://pubmed.ncbi.nlm.nih.gov/10403366/)). The ability of MurD to convert the acyl-phosphate into adenosine 5′-tetraphosphate is a chemical signature that could arise only if the acyl-phosphate is a genuine on-pathway species.

The full stepwise pathway has also been examined computationally. A hybrid quantum-mechanical/molecular-mechanical (QM/MM) replica-path study of *E. coli* MurD proposed "*a stepwise catalytic mechanism that commences with a formation of the acyl-phosphate intermediate, followed by a nucleophilic attack of D-glutamate that, through the formation of a tetrahedral reaction intermediate and subsequent phosphate dissociation, affords the final product*" ([PMID: 18704940](https://pubmed.ncbi.nlm.nih.gov/18704940/)). The convergence of kinetic, chemical-trapping, and computational evidence makes MurD's mechanism one of the best-understood among the Mur ligases. Kinetically, MurD follows an **ordered mechanism** (UDP-MurNAc-L-Ala binds first, then ATP, then D-Glu), with substrate binding driving active-site closure.

```
Step 1 (activation):   UDP-MurNAc-L-Ala-COO⁻  +  ATP
                            │
                            ▼
                       UDP-MurNAc-L-Ala-CO-OPO₃²⁻  (acyl-phosphate)  +  ADP

Step 2 (attack):       + D-Glu-NH₂  →  tetrahedral intermediate

Step 3 (collapse):     → UDP-MurNAc-L-Ala-D-Glu (amide bond)  +  Pi
```

### Finding 3 — MurD is a three-domain enzyme that closes around its substrates during catalysis

MurD is built from **three consecutive α/β domains**: (1) an N-terminal domain that binds the UDP-MurNAc moiety and adopts a Rossmann-like fold; (2) a central mononucleotide-binding domain that binds ATP; and (3) a C-terminal dinucleotide-binding domain. *E. coli* MurD was the first Mur ligase whose three-dimensional structure was solved, making it the structural prototype for the entire family: "*Escherichia coli MurD has been the first Mur ligase for which the tridimensional (3D) structure was solved*" ([PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/)).

A defining feature of MurD is a **large substrate-induced conformational change**. Binding of substrates drives closure of the active-site cleft, bringing the three domains together into a catalytically competent arrangement. Crystallographic analysis emphasizes that this closure is exquisitely sensitive: the study of domain movement "*reveals that minor structural modifications contribute to major overall conformation alterations*" ([PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/)). In other words, small local changes at the substrate-binding interface propagate into a large rigid-body domain rotation that opens or closes the enzyme.

The conserved fold organization is shared across the family. The crystal structure of *E. coli* MurF—the D-alanyl-D-alanine-adding enzyme that acts two steps downstream—shows the same modular architecture: "*its central and C-terminal domains exhibit similar mononucleotide and dinucleotide-binding folds*" ([PMID: 11090285](https://pubmed.ncbi.nlm.nih.gov/11090285/)). This homology across MurC/D/E/F supports the inference that the *P. putida* MurD adopts the same three-domain, closure-competent architecture, even though its own structure has not been experimentally solved. Notably, these domains correspond exactly to Q88N78's annotated InterPro domains (IPR013221 central; IPR004101 C-terminal; IPR036565 Mur-like catalytic superfamily; IPR005762 MurD-specific), so *P. putida* MurD is expected to share this substrate-clamping catalytic architecture.

### Finding 4 — MurD acts in the cytoplasm during the intracellular stage of peptidoglycan precursor assembly and is a validated antibacterial target

MurD carries out its function in the **bacterial cytosol**, at the intracellular stage of peptidoglycan biosynthesis. The Mur ligases collectively build the soluble nucleotide-sugar precursor before it is exported to the membrane. As described in a crystallographic review, "*Peptidoglycan precursors are synthesized in the bacterial cytosol by various enzymes including the ATP-hydrolyzing Mur ligases, which catalyze the stepwise addition of amino acids to a UDP-MurNAc precursor to yield UDP-MurNAc-pentapeptide*" ([PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/)).

MurD is the second of four Mur ligases in the assembly line:

```
MurA → MurB → MurC → [MurD] → MurE → MurF → (MraY → MurG → membrane/periplasm)
                │        │        │       │
             + L-Ala  + D-Glu  + m-DAP  + D-Ala-D-Ala
```

MurC adds L-alanine, **MurD adds D-glutamate**, MurE adds the diamino acid (meso-diaminopimelate in Gram-negative bacteria such as *P. putida*), and MurF adds the D-Ala-D-Ala dipeptide, yielding UDP-MurNAc-pentapeptide. This soluble product is then transferred by the membrane enzyme MraY to the lipid carrier (forming lipid I), and MurG adds GlcNAc (forming lipid II), which is flipped across the membrane for polymerization into mature peptidoglycan.

Beyond being a single enzymatic step, MurD and its fellow cytoplasmic biosynthesis proteins are integrated into higher-order cellular machineries. As reviewed in a study of protein-protein interactions in cell-wall biogenesis, these are "*proteins that are involved in multi-member complexes which are essential for cell division (the 'divisome') and/or cell wall elongation (the 'elongasome')*" ([PMID: 27136593](https://pubmed.ncbi.nlm.nih.gov/27136593/)). This coupling ensures that precursor supply is spatially and temporally matched to the sites of active wall synthesis.

Finally, the essentiality and bacterial specificity of MurD make it an attractive drug target. The MurD review concludes that "*MurD constitutes an attractive target for the design and synthesis of new antibacterial agents*" ([PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/)). Structure-based inhibitor design efforts, particularly around D-glutamate-mimetic scaffolds, have been pursued using MurD structural and dynamic data ([PMID: 23990043](https://pubmed.ncbi.nlm.nih.gov/23990043/)).

---

## Mechanistic Model / Interpretation

Integrating the four findings yields a coherent picture of MurD as a **cytoplasmic, ATP-dependent, stereospecific amide ligase** occupying a defined position in the linear peptidoglycan precursor pathway.

- **Where it acts:** MurD is a soluble cytoplasmic enzyme. It operates before any membrane-bound step, working on the nucleotide-sugar-peptide intermediate while it is still fully soluble in the cytosol.
- **What it does:** It ligates D-glutamate to the L-alanine terminus of UDP-MurNAc-L-Ala, forming a peptide bond and extending the stem peptide by one residue.
- **How it does it:** The reaction is powered by ATP hydrolysis, using the conserved Mur ligase chemistry of carboxylate activation (acyl-phosphate) followed by amine attack (tetrahedral intermediate) and product release. The enzyme's three-domain architecture acts as a molecular clamp that closes on the substrates, aligning the ATP γ-phosphate, the UDP-MurNAc-L-Ala carboxylate, and the D-glutamate amine.

The following table summarizes the enzyme's key properties:

| Property | Value / Description | Evidence |
|---|---|---|
| Gene / locus | *murD* / PP_1335 | UniProt Q88N78 |
| Protein | UDP-N-acetylmuramoyl-L-alanine—D-glutamate ligase | UniProt Q88N78 |
| EC number | 6.3.2.9 | UniProt; [PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/) |
| Family | MurCDEF (Mur ligases) | UniProt; IPR005762 |
| Reaction | UDP-MurNAc-L-Ala + D-Glu + ATP → UDP-MurNAc-L-Ala-D-Glu + ADP + Pi | [PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/) |
| Cofactor / energy | ATP (hydrolyzed to ADP + Pi) | [PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/) |
| Substrate specificity | Acceptor = UDP-MurNAc-L-Ala; amino donor = D-glutamate (D-stereospecific) | [PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/); [PMID: 23990043](https://pubmed.ncbi.nlm.nih.gov/23990043/) |
| Intermediates | Acyl-phosphate, tetrahedral | [PMID: 10403366](https://pubmed.ncbi.nlm.nih.gov/10403366/); [PMID: 18704940](https://pubmed.ncbi.nlm.nih.gov/18704940/) |
| Architecture | Three α/β domains (UDP-binding, ATP-binding, dinucleotide-binding) | [PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/) |
| Conformational behavior | Large substrate-induced domain closure | [PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/) |
| Localization | Cytoplasm (intracellular precursor stage) | [PMID: 27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/) |
| Cellular context | Divisome / elongasome coupling | [PMID: 27136593](https://pubmed.ncbi.nlm.nih.gov/27136593/) |
| Druggability | Validated antibacterial target; no human homolog | [PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/) |

**Basis for the *P. putida* annotation:** The functional assignment for the *P. putida* KT2440 enzyme rests primarily on **orthology and domain-signature inference**. UniProt classifies Q88N78 in the MurCDEF family with the MurD-specific InterPro signature (IPR005762), and the biochemically and structurally characterized *E. coli* MurD serves as the mechanistic reference. Given the very high conservation of the Mur ligase pathway across Gram-negative bacteria and the presence of the diagnostic MurD domain architecture, the assignment is robust. It should be noted, however, that the specific enzymatic and structural characterizations cited here were performed on the *E. coli* ortholog (and, for architecture, the MurF paralog) rather than on the *P. putida* protein itself.

---

## Evidence Base

| PMID | Title | Contribution to this report |
|---|---|---|
| [25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/) | *MurD enzymes: some recent developments.* | Authoritative review; establishes the reaction, ATP dependence, acyl-phosphate/tetrahedral intermediates, three-domain architecture (first Mur ligase structure), and drug-target status. |
| [27031227](https://pubmed.ncbi.nlm.nih.gov/27031227/) | *Crystallographic Study of Peptidoglycan Biosynthesis Enzyme MurD: Domain Movement Revisited.* | Confirms the exact reaction and substrate; documents cytosolic Mur-ligase assembly of UDP-MurNAc-pentapeptide; shows minor structural changes drive major domain-closure motions. |
| [10403366](https://pubmed.ncbi.nlm.nih.gov/10403366/) | *Formation of adenosine 5′-tetraphosphate from the acyl phosphate intermediate: a difference between the MurC and MurD synthetases of E. coli.* | Direct chemical evidence for the acyl-phosphate intermediate in MurD, distinguishing MurD from MurC. |
| [18704940](https://pubmed.ncbi.nlm.nih.gov/18704940/) | *MurD ligase from E. coli: Tetrahedral intermediate formation study by hybrid QM/MM replica path method.* | Computational support for the stepwise mechanism: acyl-phosphate → nucleophilic attack by D-Glu → tetrahedral intermediate → phosphate dissociation → product. |
| [11090285](https://pubmed.ncbi.nlm.nih.gov/11090285/) | *Crystal structure of E. coli MurF at 2.3 Å resolution.* | Shows the conserved mononucleotide/dinucleotide-binding fold organization shared across the Mur ligase family (supports inference for MurD architecture). |
| [27136593](https://pubmed.ncbi.nlm.nih.gov/27136593/) | *Structural Insights into Protein-Protein Interactions Involved in Bacterial Cell Wall Biogenesis.* | Places cytoplasmic peptidoglycan enzymes in the divisome/elongasome multi-protein complexes coordinating division and elongation. |
| [23990043](https://pubmed.ncbi.nlm.nih.gov/23990043/) | *Molecular dynamics simulation and linear interaction energy study of D-Glu-based inhibitors of the MurD ligase.* | Illustrates MurD as a validated antibacterial target and the D-Glu paradigm for inhibitor design; confirms MurD acts at the intracellular stage of peptidoglycan construction. |

Overall, the evidence base is internally consistent and mutually reinforcing. The primary functional claims (reaction, substrate specificity, cofactor, intermediates) are supported by multiple independent lines of evidence—kinetic, chemical-trapping, crystallographic, and computational—converging on the same mechanism. No cited source contradicts the annotation.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** All mechanistic, kinetic, and structural evidence cited derives from the *E. coli* ortholog (and, for architecture, the MurF paralog). The *P. putida* KT2440 MurD (Q88N78) has not, to the knowledge captured here, been purified, assayed, or crystallized. Its function is assigned by orthology and domain signature. While the Mur ligase pathway is highly conserved and the inference is strong, organism-specific kinetic parameters (Km, kcat), pH optima, and metal-ion requirements remain unmeasured for the *P. putida* enzyme.

2. **Diamino-acid context is inferred, not directly shown here.** *P. putida* is a Gram-negative bacterium expected to use meso-diaminopimelate at the MurE step; this places MurD's D-Glu product in a specific downstream context, but the exact stem-peptide composition of *P. putida* peptidoglycan was not independently verified in this investigation.

3. **Quantitative in-vivo data are absent.** Expression levels, essentiality confirmation by targeted knockout, and any regulation of *murD* (PP_1335) specifically in *P. putida* were not examined. Essentiality is inferred from the general essentiality of peptidoglycan biosynthesis.

4. **Protein-protein interaction specifics.** While the general divisome/elongasome coupling of Mur enzymes is documented, the specific interaction partners and complex stoichiometry for the *P. putida* MurD are not defined by the reviewed literature.

5. **Literature scope.** The investigation reviewed seven papers focused on the Mur ligase family; a broader survey (e.g., structural genomics entries, AlphaFold models, or *Pseudomonas*-specific cell-wall studies) could refine organism-specific details.

---

## Proposed Follow-up Experiments / Actions

1. **Structural modeling of the *P. putida* enzyme.** Retrieve or generate an AlphaFold model of Q88N78 and superpose it on the *E. coli* MurD crystal structure to confirm conservation of the three-domain architecture, the ATP-binding P-loop, and the D-Glu-binding pocket residues. This low-cost bioinformatic step would directly test the orthology-based inference.

2. **Active-site residue conservation analysis.** Perform a multiple sequence alignment of *P. putida* MurD against biochemically characterized MurD orthologs to verify conservation of catalytic residues (phosphate-binding loop, Mg²⁺-coordinating residues, D-Glu carboxylate-recognition residues), confirming mechanistic transferability.

3. **Recombinant expression and enzyme assay.** Clone PP_1335, express and purify the protein, and measure D-glutamate-adding activity (e.g., by ADP/Pi release or LC-MS detection of UDP-MurNAc-L-Ala-D-Glu) to obtain organism-specific kinetic constants and confirm D-stereospecificity.

4. **Essentiality confirmation.** Attempt a conditional knockout or CRISPRi knockdown of *murD* in *P. putida* KT2440 to confirm essentiality and characterize the morphological/lytic phenotype expected of peptidoglycan-precursor depletion.

5. **Peptidoglycan composition analysis.** Determine the muropeptide composition of *P. putida* cell wall by HPLC/MS to confirm the D-Glu at position 2 and the identity of the position-3 diamino acid, closing the loop on the downstream context of the MurD product.

6. **Inhibitor susceptibility.** Given MurD's status as an antibacterial target, test whether known D-Glu-based MurD inhibitors (cf. [PMID: 23990043](https://pubmed.ncbi.nlm.nih.gov/23990043/)) inhibit the *P. putida* enzyme, informing the breadth of the D-Glu inhibitor paradigm across Gram-negative species.

---

## Conclusion

The gene *murD* (Q88N78, PP_1335) of *Pseudomonas putida* KT2440 encodes **MurD, the ATP-dependent UDP-N-acetylmuramoyl-L-alanine:D-glutamate ligase (EC 6.3.2.9)**, a cytoplasmic three-domain enzyme of the MurCDEF family. It catalyzes the stereospecific addition of D-glutamate to UDP-MurNAc-L-Ala—the second amino-acid-adding step in the cytoplasmic assembly of the UDP-MurNAc-pentapeptide peptidoglycan precursor—via acyl-phosphate and tetrahedral intermediates, accompanied by a large substrate-induced domain closure. It functions in coordination with the divisome and elongasome machineries, and as an essential enzyme with no human homolog it is a validated antibacterial drug target. The assignment is strongly supported by domain-signature and orthology inference from the extensively characterized *E. coli* MurD, though direct experimental characterization of the *P. putida* enzyme itself remains an open task.


## Artifacts

- [OpenScientist final report](murD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27031227
2. PMID:25436755
3. PMID:23990043
4. PMID:10403366
5. PMID:18704940
6. PMID:11090285
7. PMID:27136593