---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T06:45:02.395479'
end_time: '2026-08-11T07:50:16.239392'
duration_seconds: 3913.84
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murI
  gene_symbol: murI
  uniprot_accession: Q88PW2
  protein_description: 'RecName: Full=Glutamate racemase {ECO:0000255|HAMAP-Rule:MF_00258};
    EC=5.1.1.3 {ECO:0000255|HAMAP-Rule:MF_00258};'
  gene_info: Name=murI {ECO:0000255|HAMAP-Rule:MF_00258}; OrderedLocusNames=PP_0736;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the aspartate/glutamate racemases family.
  protein_domains: Asp/Glu/hydantoin_racemase. (IPR015942); Asp/Glu_race. (IPR001920);
    Asp/Glu_racemase_AS_1. (IPR018187); Asp/Glu_racemase_AS_2. (IPR033134); Glu_race.
    (IPR004391)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murI-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murI-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PW2
- **Protein Description:** RecName: Full=Glutamate racemase {ECO:0000255|HAMAP-Rule:MF_00258}; EC=5.1.1.3 {ECO:0000255|HAMAP-Rule:MF_00258};
- **Gene Information:** Name=murI {ECO:0000255|HAMAP-Rule:MF_00258}; OrderedLocusNames=PP_0736;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the aspartate/glutamate racemases family.
- **Key Domains:** Asp/Glu/hydantoin_racemase. (IPR015942); Asp/Glu_race. (IPR001920); Asp/Glu_racemase_AS_1. (IPR018187); Asp/Glu_racemase_AS_2. (IPR033134); Glu_race. (IPR004391)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murI** (gene ID: murI, UniProt: Q88PW2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *murI* (Glutamate Racemase) in *Pseudomonas putida* KT2440

**Gene:** murI (OrderedLocusName PP_0736)
**Protein:** Glutamate racemase (EC 5.1.1.3)
**UniProt:** Q88PW2
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), abbrev. PSEPK
**Protein family:** Aspartate/glutamate racemases family

---

## Summary

The gene **murI** (locus PP_0736; UniProt **Q88PW2**) of *Pseudomonas putida* KT2440 encodes **glutamate racemase**, a soluble, cytoplasmic, cofactor-independent isomerase classified under **EC 5.1.1.3**. Its identity is well supported: the UniProt annotation (HAMAP-Rule MF_00258) places it in the aspartate/glutamate racemases family bearing the diagnostic Asp/Glu-racemase domains (IPR004391, IPR001920, IPR018187, IPR033134), and the sequence itself retains both hallmark catalytic-cysteine motifs that define functional members of this family. The gene symbol *murI* is unambiguous here and matches the protein description; no evidence of gene-symbol confusion was encountered. Because the *P. putida* ortholog has not itself been the subject of dedicated enzymological studies, this report annotates it by rigorous homology to experimentally characterized glutamate racemases from *Aquifex pyrophilus*, *Escherichia coli*, *Lactobacillus plantarum*, *Thermus thermophilus*, and mycobacteria, combined with direct bioinformatic verification of the *P. putida* sequence.

The **primary function** is the reversible interconversion of **L-glutamate and D-glutamate** at the α-carbon. The enzyme is a homodimer, each monomer folded into two α/β domains that enclose the substrate in a deep pocket. Catalysis proceeds by a **metal-independent, "two-base" 1,1-proton-transfer mechanism**: two active-site cysteines act as a paired catalytic acid and base, one abstracting the α-proton from one enantiomer and the other re-protonating the planar carbanion/enolate intermediate from the opposite face. In the *P. putida* protein these two catalytic residues are conserved as **Cys75** (within the A‑C‑N‑T‑A motif) and **Cys186** (within the G‑C‑T‑H motif), exactly homologous to the established *E. coli* catalytic pair Cys92/Cys204 and the *Aquifex* pair Cys70/Cys178. The enzyme is highly substrate-specific, recognizing essentially only glutamate among amino acids, and racemizes the two enantiomers with comparable catalytic efficiency, consistent with a freely reversible reaction near equilibrium.

The **biological role** is to supply **D-glutamate**, an essential building block of the bacterial **peptidoglycan** stem peptide. D-glutamate produced by MurI is incorporated one step downstream by the MurD ligase onto the cytoplasmic precursor UDP-N-acetylmuramoyl-L-alanine, committing the cell to cell-wall assembly. Because D-glutamate cannot generally be obtained from other sources, glutamate racemase is **essential for viability** in numerous bacteria and is a validated antibacterial drug target. Its site of action is the **cytoplasm**, consistent with the absence of any signal peptide or transmembrane segment in Q88PW2. A lineage-specific secondary ("moonlighting") activity as a **DNA-gyrase inhibitor** is documented in some bacteria (notably *M. tuberculosis*), but this activity has **not** been demonstrated for the *P. putida* ortholog and should be regarded as unverified for this protein.

---

## Key Findings

### F001 — *murI* encodes a cofactor-independent glutamate racemase (EC 5.1.1.3)

Q88PW2 is annotated under the well-curated HAMAP rule MF_00258 as glutamate racemase, gene *murI* / PP_0736, within the aspartate/glutamate racemases family and carrying the Asp/Glu-racemase InterPro signatures (IPR004391, IPR001920). This annotation is grounded in decades of structural and mechanistic work on the enzyme family. The landmark 2.3 Å crystal structure of glutamate racemase (MurI) from *Aquifex pyrophilus* established that "**Glutamate racemase (MurI) is responsible for the synthesis of D-glutamate, an essential building block of the peptidoglycan layer in bacterial cell walls**" and that "**the enzyme forms a dimer and each monomer consists of two alpha/beta fold domains**," with a substrate analog (D-glutamine) bound in a deep interdomain pocket ([PMID: 10331867](https://pubmed.ncbi.nlm.nih.gov/10331867/)).

Critically, glutamate racemase belongs to the small class of **cofactor-independent racemases** — it requires neither pyridoxal-5′-phosphate nor a metal ion. The *Aquifex* study proposed "**a mechanism of metal cofactor-independent glutamate racemase in which two cysteine residues are involved in catalysis**" ([PMID: 10331867](https://pubmed.ncbi.nlm.nih.gov/10331867/)). Molecular-dynamics analysis of the enzyme refined this into a two-base mechanism in which the two cysteines act on opposite faces of the substrate: "**two cysteine residues serve as catalytic acid and base**" ([PMID: 15274623](https://pubmed.ncbi.nlm.nih.gov/15274623/)). Mechanistically, one cysteine thiolate deprotonates D-glutamate at the α-carbon, generating a planar carbanion/enolate stabilized by the surrounding pocket, and the second cysteine re-protonates it from the opposite face to give L-glutamate (and vice versa) — a classic 1,1-proton-transfer racemization.

### F002 — MurI supplies D-glutamate to peptidoglycan biosynthesis and is generally essential

The product of the reaction, **D-glutamate**, is a mandatory constituent of the peptidoglycan stem peptide. In the cytoplasmic phase of peptidoglycan synthesis, the second Mur ligase, MurD, consumes this D-glutamate: "**MurD (UDP-N-acetylmuramoyl-L-alanine:D-glutamate ligase) is the second enzyme in the series of Mur ligases, and it catalyzes the addition of D-glutamic acid (D-Glu) to the cytoplasmic intermediate UDP-N-acetylmuramoyl-L-alanine (UMA)**" ([PMID: 19007109](https://pubmed.ncbi.nlm.nih.gov/19007109/)). MurI therefore sits immediately upstream of MurD in a linear, committed pathway, and its D-Glu product becomes the second residue of the stem pentapeptide.

Because D-glutamate is otherwise unavailable, glutamate racemase is essential in many bacteria. "**The gene encoding glutamate racemase, murI has been shown to be essential for the growth of a number of bacterial species including Escherichia coli**" ([PMID: 25447907](https://pubmed.ncbi.nlm.nih.gov/25447907/)). The most decisive demonstration comes from *Mycobacterium smegmatis*, where "**The deletion of the murI gene in M. smegmatis could be achieved only in minimal medium supplemented with D-glutamate, demonstrating that MurI is essential for growth and that glutamate racemase is the only source of D-glutamate for peptidoglycan synthesis in M. smegmatis**" ([PMID: 25246478](https://pubmed.ncbi.nlm.nih.gov/25246478/)). This conditional-lethal / D-glutamate-rescue phenotype is the gold-standard genetic proof that MurI's physiological output is D-glutamate destined for the cell wall. By orthology — and given that *P. putida*, like *E. coli*, is a Gram-negative γ-proteobacterium with a standard peptidoglycan wall and no known D-amino-acid transaminase bypass — the *P. putida* MurI is expected to be the sole D-Glu source and essential, though this has not been individually tested in KT2440.

### F003 — High substrate specificity for glutamate; symmetric racemization of both enantiomers

Purified native glutamate racemase from *Lactobacillus plantarum* NC8 was shown to be strictly glutamate-specific and kinetically symmetric: "**Only D- and L-glutamic acid were recognised as substrates for the Murl with similar K(cat)/K(M) ratios of 3.6 s(-1)/mM for each enantiomer**" ([PMID: 23228473](https://pubmed.ncbi.nlm.nih.gov/23228473/)). The near-identical specificity constants for the L→D and D→L directions reflect the microscopic reversibility of a racemase operating near thermodynamic equilibrium (racemization has an equilibrium constant of ~1). Independently, the *Thermus thermophilus* enzyme (TTHA1643) was tested against a panel of amino acids: "**Among 21 amino acids tested, TTHA1643 showed highly specific activity toward Glu as the substrate**" ([PMID: 32474108](https://pubmed.ncbi.nlm.nih.gov/32474108/)). Together these establish that the enzyme discriminates sharply against other amino acids and processes both glutamate enantiomers comparably — a substrate profile expected to hold for the *P. putida* ortholog given its conserved active-site architecture. Structural/MD analyses attribute this discrimination to steering of the δ-carboxylate of glutamate by conserved Asp/Glu residues and coordination of the α-carboxylate/α-amino group by conserved Thr and Asn residues.

### F004 — Regulatory features and a lineage-specific moonlighting activity

A structural and biochemical survey of glutamate racemases from several pathogens described "**three distinct mechanisms of regulation for the family of glutamate racemases: allosteric activation by metabolic precursors, kinetic regulation through substrate inhibition, and D-glutamate recycling using a d-amino acid transaminase**" ([PMID: 17568739](https://pubmed.ncbi.nlm.nih.gov/17568739/)). Allosteric activation by UDP-MurNAc peptidoglycan precursors couples D-glutamate production to demand for cell-wall building blocks, an elegant feed-forward control of the committed cytoplasmic steps; a cryptic allosteric site in this family has also been exploited for species-selective inhibitors.

Separately, some glutamate racemases **moonlight**: "**MurI proteins from some bacteria have been shown to act as an inhibitor of DNA gyrase**" ([PMID: 18757813](https://pubmed.ncbi.nlm.nih.gov/18757813/)). In *M. tuberculosis*, racemization and gyrase inhibition are two independent activities of the same protein, and MurI overexpression conferred ciprofloxacin resistance in vivo. This is a lineage-specific property and is **not** established for *P. putida* MurI; it is included for completeness rather than as an annotation of Q88PW2.

### F005 — The *P. putida* ortholog conserves both catalytic cysteines (Cys75, Cys186)

Direct bioinformatic analysis of the Q88PW2 sequence (265 aa; predicted single-domain soluble protein with no signal peptide or transmembrane segment) confirmed that both catalytic cysteines are present in their diagnostic motifs. This is the strongest single line of evidence that PP_0736 is a catalytically competent racemase rather than a degenerate family member.

| | *P. putida* Q88PW2 | *E. coli* MurI | Motif / InterPro signature |
|---|---|---|---|
| 1st catalytic Cys | **Cys75** (`AMVLA`**`C`**`NTATV`) | Cys92 (`LAVVA`**`C`**`NTAST`) | A‑C‑N‑T‑A (IPR018187, AS_1) |
| 2nd catalytic Cys | **Cys186** (`TLILG`**`C`**`THYPF`) | Cys204 (`TVVLG`**`C`**`THFPL`) | G‑C‑T‑H (IPR033134, AS_2) |

The *E. coli* Cys92/Cys204 pair (equivalent to the *Aquifex* Cys70/Cys178 pair) is the established catalytic acid/base couple. The presence of both intact cysteines in the correct sequence context in Q88PW2 — supported by "**two cysteine residues serve as catalytic acid and base**" ([PMID: 15274623](https://pubmed.ncbi.nlm.nih.gov/15274623/)) and the *Aquifex* two-cysteine mechanism ([PMID: 10331867](https://pubmed.ncbi.nlm.nih.gov/10331867/)) — validates the racemase assignment for PP_0736 specifically, not merely for its family. The immediately flanking substrate-coordinating residues (the `C-N-T` of the ACNTA motif and the `C-T-H` of the second motif) are likewise conserved, and the absence of any signal/transmembrane segment confirms a soluble cytoplasmic enzyme.

---

## Mechanistic Model / Interpretation

### The reaction

```
                 Cys75 (base)          Cys186 (acid)
                     \                    /
   L-glutamate  <====================================>  D-glutamate
                 (planar carbanion / enolate intermediate
                  at the alpha-carbon; no cofactor, no metal)
```

Glutamate racemase catalyzes **L-glutamate ⇌ D-glutamate** (EC 5.1.1.3). The two active-site cysteines flank the substrate α-carbon on opposite faces. In the L→D direction, one cysteine thiolate abstracts the α-proton to form a planar, resonance-stabilized carbanion/enolate; the second cysteine then delivers a proton to the opposite face, inverting stereochemistry. The reverse direction uses the same residues with reversed roles. No pyridoxal phosphate and no metal ion participate — this is the defining feature of the cofactor-independent racemase mechanism.

### Placement in the peptidoglycan cytoplasmic pathway

```
   L-Glu
     |  MurI (glutamate racemase, PP_0736 / Q88PW2)   <-- THIS GENE
     v
   D-Glu
     |
     |  + UDP-MurNAc-L-Ala (UMA)
     v  MurD ligase (UDP-MurNAc-L-Ala:D-Glu ligase, EC 6.3.2.9)
   UDP-MurNAc-L-Ala-D-Glu
     |  MurE, MurF ...
     v
   UDP-MurNAc-pentapeptide  -->  Lipid I / Lipid II  -->  polymerized peptidoglycan
                                  (membrane / periplasm)
```

MurI operates entirely in the **cytoplasm**, at the head of the "Mur pathway," supplying the D-glutamate substrate for MurD. The downstream steps (lipid-linked intermediates, transglycosylation, transpeptidation) occur at and beyond the membrane, but MurI's own catalysis is soluble and cytoplasmic — consistent with the absence of any localization signal in Q88PW2.

### Comparative table of supporting orthologs

| Organism | Evidence type | Catalytic residues | Key result | PMID |
|---|---|---|---|---|
| *Aquifex pyrophilus* | X-ray structure (2.3 Å), mechanism | Cys70 / Cys178 | Homodimer, two α/β domains; cofactor-independent two-cysteine mechanism | [10331867](https://pubmed.ncbi.nlm.nih.gov/10331867/) |
| (general MD study) | Molecular dynamics | two Cys | Cysteines serve as catalytic acid and base; chiral recognition | [15274623](https://pubmed.ncbi.nlm.nih.gov/15274623/) |
| *Escherichia coli* | Genetics | Cys92 / Cys204 | *murI* essential | [25447907](https://pubmed.ncbi.nlm.nih.gov/25447907/) |
| *Mycobacterium smegmatis* | Gene knockout + rescue | — | ΔmurI viable only with D-Glu; MurI is sole D-Glu source | [25246478](https://pubmed.ncbi.nlm.nih.gov/25246478/) |
| *Lactobacillus plantarum* | Enzyme kinetics | — | Only D-/L-Glu are substrates; symmetric kcat/KM ≈ 3.6 s⁻¹/mM | [23228473](https://pubmed.ncbi.nlm.nih.gov/23228473/) |
| *Thermus thermophilus* | Enzyme assay | — | Highly specific for Glu among 21 amino acids | [32474108](https://pubmed.ncbi.nlm.nih.gov/32474108/) |
| *Mycobacterium tuberculosis* | Biochemistry | — | Moonlighting DNA-gyrase inhibition (independent of racemization) | [18757813](https://pubmed.ncbi.nlm.nih.gov/18757813/) |
| **Pseudomonas putida KT2440** | **Sequence/motif mapping (this work)** | **Cys75 / Cys186** | **Both catalytic cysteines conserved in A‑C‑N‑T‑A and G‑C‑T‑H motifs** | — |

### Synthesis

All lines of evidence converge on a single, high-confidence annotation. The UniProt/HAMAP identity, the InterPro domain architecture, and — most importantly — the direct observation that Q88PW2 retains both catalytic cysteines in their correct motif context together establish that PP_0736 encodes a functional, cofactor-independent glutamate racemase. Its biochemical role is to interconvert L- and D-glutamate; its physiological purpose is to provide D-glutamate for MurD-catalyzed assembly of the peptidoglycan stem peptide; and its subcellular location of action is the cytoplasm. This is the canonical, near-universally conserved role of MurI in bacteria, and *P. putida* KT2440 has no known deviation from it.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [10331867](https://pubmed.ncbi.nlm.nih.gov/10331867/) | *Structure and mechanism of glutamate racemase from Aquifex pyrophilus* | Defines the enzyme's function, homodimeric two-domain fold, and cofactor-independent two-cysteine mechanism |
| [15274623](https://pubmed.ncbi.nlm.nih.gov/15274623/) | *Multiple substrate binding states and chiral recognition in cofactor-independent glutamate racemase: an MD study* | Confirms the two cysteines act as catalytic acid/base; models chiral recognition |
| [25246478](https://pubmed.ncbi.nlm.nih.gov/25246478/) | *Investigation of the essentiality of glutamate racemase in M. smegmatis* | Genetic proof of essentiality and that MurI is the sole D-glutamate source |
| [25447907](https://pubmed.ncbi.nlm.nih.gov/25447907/) | *Revisiting the essentiality of glutamate racemase in M. tuberculosis* | Documents *murI* essentiality across species including *E. coli* |
| [19007109](https://pubmed.ncbi.nlm.nih.gov/19007109/) | *Novel naphthalene-N-sulfonyl-D-glutamic acid derivatives as inhibitors of MurD* | Establishes MurD as the downstream consumer of D-glutamate in the cytoplasm |
| [23228473](https://pubmed.ncbi.nlm.nih.gov/23228473/) | *Recombinant expression... native glutamate racemase from L. plantarum NC8* | Kinetic evidence of glutamate specificity and enantiomeric symmetry |
| [32474108](https://pubmed.ncbi.nlm.nih.gov/32474108/) | *Enzymatic properties... glutamate racemase from T. thermophilus* | Confirms strict specificity for glutamate over 20 other amino acids |
| [17568739](https://pubmed.ncbi.nlm.nih.gov/17568739/) | *Exploitation of structural and regulatory diversity in glutamate racemases* | Describes allosteric/substrate-inhibition regulation and D-Glu recycling |
| [18757813](https://pubmed.ncbi.nlm.nih.gov/18757813/) | *Moonlighting function of glutamate racemase from M. tuberculosis* | Documents lineage-specific DNA-gyrase inhibition, independent of racemization |

Supporting drug-discovery literature on the downstream MurD ligase — including high-throughput MurD assays and sulfonamide/transition-state inhibitors ([PMID: 21524830](https://pubmed.ncbi.nlm.nih.gov/21524830/), [PMID: 19403924](https://pubmed.ncbi.nlm.nih.gov/19403924/), [PMID: 17507028](https://pubmed.ncbi.nlm.nih.gov/17507028/)) and broader characterization of the Mur ligase cascade ([PMID: 23555903](https://pubmed.ncbi.nlm.nih.gov/23555903/), [PMID: 22102165](https://pubmed.ncbi.nlm.nih.gov/22102165/)) — corroborates the cytoplasmic peptidoglycan pathway context in which MurI operates, and underscores why the MurI→MurD node is an attractive antibacterial target.

**No conflicting evidence** was found. No literature was encountered for a different gene bearing the symbol *murI*; the symbol is standard and unambiguous for glutamate racemase.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of the *P. putida* KT2440 ortholog.** The functional annotation of Q88PW2 rests on (a) database/HAMAP annotation, (b) InterPro domain assignment, and (c) sequence-motif conservation of the two catalytic cysteines verified in this investigation. No purified-enzyme kinetics, crystal structure, or knockout phenotype exists specifically for PP_0736. The annotation is therefore high-confidence by homology but not experimentally proven in this organism.

2. **Essentiality in *P. putida* is inferred, not demonstrated.** Essentiality is established in *E. coli* and *M. smegmatis*, but not tested in KT2440. Some organisms possess a D-amino-acid transaminase route that can supply D-glutamate, potentially softening essentiality; whether *P. putida* has such a bypass was not determined here.

3. **Kinetic parameters are borrowed from orthologs.** The kcat/KM ≈ 3.6 s⁻¹/mM figure is from *L. plantarum*; *P. putida*-specific constants, KM for glutamate, and any substrate inhibition or allosteric activation by UDP-MurNAc precursors remain unmeasured.

4. **Moonlighting activity is unverified for this protein.** DNA-gyrase inhibition is documented in *M. tuberculosis* and some other bacteria but has not been tested in *P. putida*; it should not be assumed for Q88PW2.

5. **Structural inferences are model-based.** The homodimeric two-α/β-domain fold and cytoplasmic localization are inferred from family structures and the absence of targeting signals, not from an experimental *P. putida* structure.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Clone PP_0736, express and purify the protein, and measure racemase activity in both directions (L→D and D→L), determining KM, kcat, and kcat/KM for glutamate; confirm strict specificity against an amino-acid panel as done for *T. thermophilus*.

2. **Active-site mutagenesis.** Generate Cys75Ala and Cys186Ala (and the double mutant) and confirm loss of catalytic activity, directly validating the predicted catalytic acid/base pair in the *P. putida* enzyme.

3. **Genetic essentiality test.** Attempt a clean ΔPP_0736 deletion in KT2440 with and without D-glutamate supplementation; a D-glutamate–dependent rescue would replicate the definitive *M. smegmatis* result and prove essentiality / sole-source status.

4. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* MurI (± D-glutamate/D-glutamine or transition-state analog) to confirm the homodimeric two-domain fold and active-site geometry, and to enable structure-based inhibitor design.

5. **Regulation probing.** Test for allosteric activation by UDP-MurNAc peptidoglycan precursors and for substrate inhibition, to determine which of the family's regulatory modes operate in *P. putida*.

6. **Pathway/localization confirmation.** Verify cytoplasmic localization (e.g., fractionation or fluorescent fusion) and reconstitute the MurI→MurD coupling in vitro to confirm channeling of D-glutamate into UDP-MurNAc-L-Ala-D-Glu.

7. **Moonlighting assessment.** Test whether *P. putida* MurI inhibits DNA gyrase in vitro and whether overexpression alters fluoroquinolone susceptibility, to determine if the moonlighting activity extends to this species.

---

*Report generated from a 3-iteration autonomous investigation; 5 findings confirmed across 14 reviewed papers. The gene identity (murI = glutamate racemase, EC 5.1.1.3, Q88PW2, PP_0736) was verified and is unambiguous.*


## Artifacts

- [OpenScientist final report](murI-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murI-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10331867
2. PMID:15274623
3. PMID:19007109
4. PMID:25447907
5. PMID:25246478
6. PMID:23228473
7. PMID:32474108
8. PMID:17568739
9. PMID:18757813
10. PMID:21524830
11. PMID:19403924
12. PMID:17507028
13. PMID:23555903
14. PMID:22102165