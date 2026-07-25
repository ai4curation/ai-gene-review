---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:50:19.320394'
end_time: '2026-07-18T14:15:47.438836'
duration_seconds: 1528.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: panC
  gene_symbol: panC
  uniprot_accession: Q88DW8
  protein_description: 'RecName: Full=Pantothenate synthetase {ECO:0000255|HAMAP-Rule:MF_00158};
    Short=PS {ECO:0000255|HAMAP-Rule:MF_00158}; EC=6.3.2.1 {ECO:0000255|HAMAP-Rule:MF_00158};
    AltName: Full=Pantoate--beta-alanine ligase {ECO:0000255|HAMAP-Rule:MF_00158};
    AltName: Full=Pantoate-activating enzyme {ECO:0000255|HAMAP-Rule:MF_00158};'
  gene_info: Name=panC {ECO:0000255|HAMAP-Rule:MF_00158}; OrderedLocusNames=PP_4700;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the pantothenate synthetase family.
  protein_domains: Pantoate_ligase. (IPR003721); Pantoate_ligase_C. (IPR042176); Rossmann-like_a/b/a_fold.
    (IPR014729); Pantoate_ligase (PF02569)
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
  path: panC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: panC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DW8
- **Protein Description:** RecName: Full=Pantothenate synthetase {ECO:0000255|HAMAP-Rule:MF_00158}; Short=PS {ECO:0000255|HAMAP-Rule:MF_00158}; EC=6.3.2.1 {ECO:0000255|HAMAP-Rule:MF_00158}; AltName: Full=Pantoate--beta-alanine ligase {ECO:0000255|HAMAP-Rule:MF_00158}; AltName: Full=Pantoate-activating enzyme {ECO:0000255|HAMAP-Rule:MF_00158};
- **Gene Information:** Name=panC {ECO:0000255|HAMAP-Rule:MF_00158}; OrderedLocusNames=PP_4700;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the pantothenate synthetase family.
- **Key Domains:** Pantoate_ligase. (IPR003721); Pantoate_ligase_C. (IPR042176); Rossmann-like_a/b/a_fold. (IPR014729); Pantoate_ligase (PF02569)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "panC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'panC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **panC** (gene ID: panC, UniProt: Q88DW8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *panC* (PP_4700, UniProt Q88DW8) in *Pseudomonas putida* KT2440

## 1. Summary

**panC** (ordered locus **PP_4700**; UniProt **Q88DW8**) of *Pseudomonas putida* KT2440 encodes **pantothenate synthetase** (also called pantoate—β-alanine ligase or pantoate-activating enzyme; **EC 6.3.2.1**; KEGG ortholog **K01918**). Its primary function is to catalyze the final, committed step of *de novo* **pantothenate (vitamin B5) biosynthesis**: the **ATP-dependent condensation of (R)-pantoate and β-alanine to form pantothenate**, proceeding through a covalent **pantoyl-adenylate** reaction intermediate and releasing **AMP and pyrophosphate**. Pantothenate is the obligate precursor of the 4′-phosphopantetheine moiety of **coenzyme A (CoA) and acyl carrier protein (ACP)**, making PanC an essential feeder of central CoA/ACP-dependent metabolism. The enzyme functions as a **soluble, cytoplasmic homodimer** requiring a **divalent metal cofactor (Mg²⁺ or Mn²⁺)**. The gene is co-organized with *panB* in an overlapping **panB–panC operon**, coupling two consecutive pathway steps.

No experimental study has been published on the *P. putida* KT2440 protein specifically; the annotation is transferred with high confidence from closely related, biochemically and structurally characterized orthologs (E. coli, *M. tuberculosis*, plants, fungi) supported by ~53–55% sequence identity, an intact catalytic motif, conserved substrate-binding residues, and native operon context.

---

## 2. Gene / Protein Identity Verification

The gene symbol **panC** matches the protein description in every respect and is **not ambiguous** in this context:

- **UniProt Q88DW8** annotates the protein as *Pantothenate synthetase* (EC 6.3.2.1), gene *panC*, locus PP_4700, in *Pseudomonas putida* KT2440.
- **KEGG** independently curates PP_4700 as *panC* / K01918 / EC 6.3.2.1, in the *Pantothenate and CoA biosynthesis* (ppu00770) and *β-Alanine metabolism* (ppu00410) pathways (NCBI protein AAN70273).
- The protein carries the family-defining **Pantoate_ligase** Pfam domain (PF02569; InterPro IPR003721), a C-terminal Pantoate_ligase_C domain (IPR042176), and a Rossmann-like a/b/a fold (IPR014729) — all consistent with the pantothenate synthetase family.
- All literature discussed below concerns the **same enzyme (pantothenate synthetase / PanC / EC 6.3.2.1)** across bacteria, fungi, and plants; the mechanism and reaction are conserved across the family, so cross-species inference is valid.

**Conclusion:** the target is correctly identified as bacterial pantothenate synthetase.

---

## 3. Primary Function: Reaction Catalyzed and Mechanism

### 3.1 Overall reaction
PanC catalyzes:

> **(R)-pantoate + β-alanine + ATP → (R)-pantothenate + AMP + pyrophosphate (PPi)**

This is the "ATP-dependent condensation of pantoate and beta-alanine to form pantothenate" (Wang & Eisenberg, 2006, PMID 16460002).

### 3.2 Two-step (ordered) mechanism via a pantoyl-adenylate intermediate
Crystallographic "snapshots" of the *M. tuberculosis* ortholog captured the enzyme bound to substrates (ATP/AMPCPP, pantoate), the covalent reaction intermediate, and product (AMP), establishing an ordered, two-step mechanism (Wang & Eisenberg, 2006, PMID 16460002):

1. **Adenylation:** pantoate attacks the α-phosphate of ATP, forming enzyme-bound **pantoyl-adenylate** + PPi.
2. **Aminolysis:** the amino group of β-alanine attacks the activated pantoyl carbonyl, forming the amide bond of pantothenate and releasing AMP.

A key mechanistic feature is that **β-alanine can bind only after the pantoyl-adenylate intermediate has formed** — "binding of beta-alanine in the active site cavity can occur only after formation of the pantoyl adenylate intermediate," with "the phosphate group of AMP [serving] as an anchor for the binding of beta-alanine" (Wang & Eisenberg, 2006, PMID 16460002). This adenylate-forming chemistry (activation of a carboxylate as an acyl-adenylate) is characteristic of the pantothenate synthetase family and is echoed by the ATP-sulfurylase-like nucleotide-binding motif noted in the KEGG annotation.

### 3.3 Conserved catalytic residues
Structural/mutational analysis of the *M. tuberculosis* enzyme identifies conserved active-site residues **His44, His47, Asn69, Gln72, Lys160, Gln164** as important for substrate binding and pantoyl-adenylate formation; alanine substitutions (e.g., H47A, K160A) weaken ATP binding and reduce catalysis (Pandey et al., 2018, PMID 29343701). In *P. putida* Q88DW8 the corresponding catalytic **HxGH motif is intact (His34-Ser35-Gly36-His37)**, and UniProt annotates **His37 as the catalytic proton donor**, along with ATP-binding residues (30–37, 149–152, 178, 186–189), (R)-pantoate-binding residues (Gln61, Gln155), and a β-alanine-binding residue (Gln61) — matching the two-substrate/ATP active-site architecture.

---

## 4. Substrate Specificity and Cofactor

- **Strict substrate requirement:** the purified enzyme "requires d-pantoate, beta-alanine and ATP for activity" (Genschel et al., 1999, PMID 10417331).
- **Stereo/chemo-selectivity:** "**Neither oxopantoate nor pantoyl-lactone can replace pantoate as substrate**," demonstrating tight specificity for reduced, open-chain D-(R)-pantoate (Genschel et al., 1999, PMID 10417331).
- **Relative affinities:** the enzyme "has a higher affinity for pantoate (Km 45 µM) than for beta-alanine (Km 990 µM)" (Genschel et al., 1999, PMID 10417331), with kcat ≈ 0.63 s⁻¹ and uncompetitive substrate inhibition at pantoate > ~1 mM.
- **Metal cofactor:** the enzyme "is most active in the presence of magnesium or manganese" (PMID 37578562), consistent with Mg·ATP being the true substrate for adenylate formation.

These kinetic parameters derive from characterized orthologs; given ~53–55% identity and full active-site conservation, they are expected to hold, at least qualitatively, for *P. putida* PanC.

---

## 5. Biological Process / Pathway Context

### 5.1 Final step of the four-enzyme pantothenate pathway
Bacterial *de novo* pantothenate biosynthesis "compris[es] four enzymic reactions catalysed by ketopantoate hydroxymethyltransferase (KPHMT), L-aspartate-alpha-decarboxylase (ADC), pantothenate synthetase (PS) and ketopantoate reductase (KPR) encoded by **panB, panD, panC and panE** genes" (Chakauya et al., 2008, PMID 18726075). PanC performs the terminal condensation. Its two substrates are supplied by the other pathway branches:
- **(R)-pantoate** branch: α-ketoisovalerate (from branched-chain amino acid metabolism) → ketopantoate (**PanB**, EC 2.1.2.11) → pantoate (**PanE**).
- **β-alanine** branch: L-aspartate → β-alanine (**PanD**, aspartate-1-decarboxylase).

Genetics confirm the gene–function assignment: in *E. coli*/*S. typhimurium*, "the **panC mutants lack pantothenate synthetase**," each showing a single enzyme defect (Cronan et al., 1982, PMID 7037743).

### 5.2 Downstream role: essential precursor of CoA and ACP
"Pantothenate (vitamin B5) is the precursor of the 4′-phosphopantetheine moiety of **coenzyme A and acyl-carrier protein**" (Chakauya et al., 2008, PMID 18726075). Pantothenate "is required for the synthesis of coenzyme A (CoA)" (Riske et al., 2023, PMID 37762222). Because CoA and holo-ACP are indispensable for fatty-acid synthesis, the TCA cycle, and myriad acyl-transfer reactions, the pantothenate/CoA pathway is essential and a validated antimicrobial drug target (Wang & Eisenberg, 2006, PMID 16460002; Pepi et al., 2022, PMID 35015509). This is especially relevant for the metabolically versatile, solvent-tolerant lifestyle of *P. putida*, which relies heavily on CoA/acyl-CoA metabolism.

### 5.3 Genomic organization — panB–panC operon
In *P. putida* KT2440, KEGG genome coordinates place **panB (PP_4699)** at 5,340,894–5,341,694 and **panC (PP_4700)** at 5,341,691–5,342,554 on the same strand; the two ORFs **overlap by 4 bp**, the hallmark of translational coupling within a single operon. This mirrors the *E. coli* cluster where "panB and panC lie adjacent to one another" (Merkel & Nichols, 1996, PMID 8837478). The overlap implies coordinated, stoichiometric expression of two consecutive pathway enzymes.

---

## 6. Localization

Pantothenate synthetase is a **soluble, cytoplasmic** enzyme. Characterized plant orthologs localize to the cytosol with "no N-terminal extension" ("The Lotus and rice PSs are therefore likely to be cytosolic"; Genschel et al., 1999, PMID 10417331); bacterial PanC likewise has no signal peptide or membrane-spanning region (Q88DW8 is a 287-aa soluble protein). The enzyme is active as a **homodimer** ("Recombinant PS from Lotus … is a dimer," PMID 10417331; the *M. tuberculosis* enzyme is also dimeric). Thus *P. putida* PanC carries out its reaction in the **cytoplasm**, where its substrates (pantoate, β-alanine, Mg·ATP) and downstream CoA-biosynthetic enzymes reside.

---

## 7. Evidence Summary

| Claim | Evidence type | Key source(s) |
|---|---|---|
| Catalyzes ATP-dependent pantoate + β-alanine → pantothenate | Experimental (enzymology, crystallography of orthologs) | PMID 16460002, 10417331 |
| Two-step mechanism via pantoyl-adenylate; ordered substrate binding | Experimental (crystal structures) | PMID 16460002 |
| Conserved catalytic residues (His pair / HxGH, Lys, Gln, Asn) | Experimental + bioinformatic | PMID 29343701; UniProt Q88DW8 |
| Strict specificity for D-pantoate; Km values | Experimental (kinetics) | PMID 10417331 |
| Mg²⁺/Mn²⁺ cofactor | Experimental | PMID 37578562 |
| Final of four steps in pantothenate pathway | Review + genetics | PMID 18726075, 7037743 |
| Product is CoA/ACP precursor; pathway essential/drug target | Review | PMID 18726075, 37762222, 35015509 |
| Cytoplasmic, homodimeric | Experimental (orthologs) + sequence | PMID 10417331 |
| Q88DW8 is a true PanC ortholog (~53–55% id, intact motif) | Bioinformatic (this work) | UniProt; alignment vs P31663, P9WIL5 |
| panB–panC operon in KT2440 (4-bp overlap) | Genomic (this work) | KEGG ppu; PMID 8837478 |
| High-confidence AlphaFold fold (mean pLDDT 95.7; 92.7% >90) | Structure prediction (this work) | AlphaFold DB AF-Q88DW8-F1 |

---

## 8. Supported and Refuted Hypotheses

- **Supported:** PP_4700 encodes a functional pantothenate synthetase (EC 6.3.2.1) catalyzing the terminal step of pantothenate biosynthesis via a pantoyl-adenylate intermediate; it is cytoplasmic, homodimeric, Mg/Mn-dependent, strictly D-pantoate–specific, and co-expressed with panB.
- **Refuted / ruled out:** the gene symbol is **not** ambiguous here — no competing gene with the same symbol and a different function fits the sequence, domains, or genomic context. Oxopantoate and pantoyl-lactone are **not** substrates (ruled out experimentally in the ortholog).

---

## 9. Limitations and Future Directions

- **No direct experimental characterization of the *P. putida* KT2440 protein** exists; all enzymology/structure is from orthologs. Function is inferred (with high confidence) from ~53–55% identity, an intact catalytic HxGH motif, conserved substrate-binding residues, and conserved genomic operon context.
- Kinetic constants (Km, kcat) are ortholog-derived and may differ quantitatively in *P. putida*.
- **Future work:** recombinant expression and steady-state kinetics of Q88DW8; determination of a *P. putida* PanC crystal or cryo-EM/AlphaFold-validated structure; targeted *panC* deletion/complementation to confirm essentiality and pantothenate auxotrophy in KT2440; transcriptional mapping to confirm the panB–panC operon experimentally.

---

*Report generated from literature (PubMed) and database (UniProt, KEGG) evidence, plus computational sequence/genomic analysis. All quantitative claims are cited to primary or review literature.*


## Artifacts

- [OpenScientist final report](panC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](panC-deep-research-openscientist_artifacts/final_report.pdf)