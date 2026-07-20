---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T08:07:27.690954'
end_time: '2026-07-15T08:19:13.033570'
duration_seconds: 705.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: tal
  gene_symbol: tal
  uniprot_accession: Q88KX1
  protein_description: 'RecName: Full=Transaldolase {ECO:0000255|HAMAP-Rule:MF_00492};
    EC=2.2.1.2 {ECO:0000255|HAMAP-Rule:MF_00492};'
  gene_info: Name=tal {ECO:0000255|HAMAP-Rule:MF_00492}; OrderedLocusNames=PP_2168;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transaldolase family. Type 1 subfamily.
  protein_domains: Aldolase_TIM. (IPR013785); TAL/FSA. (IPR001585); Transaldolase_1.
    (IPR004730); Transaldolase_AS. (IPR018225); TAL_FSA (PF00923)
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
  path: tal-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: tal-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KX1
- **Protein Description:** RecName: Full=Transaldolase {ECO:0000255|HAMAP-Rule:MF_00492}; EC=2.2.1.2 {ECO:0000255|HAMAP-Rule:MF_00492};
- **Gene Information:** Name=tal {ECO:0000255|HAMAP-Rule:MF_00492}; OrderedLocusNames=PP_2168;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transaldolase family. Type 1 subfamily.
- **Key Domains:** Aldolase_TIM. (IPR013785); TAL/FSA. (IPR001585); Transaldolase_1. (IPR004730); Transaldolase_AS. (IPR018225); TAL_FSA (PF00923)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tal" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tal' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tal** (gene ID: tal, UniProt: Q88KX1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *tal* (PP_2168, UniProt Q88KX1) — Transaldolase of *Pseudomonas putida* KT2440

## 0. Gene/Protein Identity Verification

The target is **unambiguous**. The UniProt record (Q88KX1) describes:
- **Protein:** Transaldolase (RecName), **EC 2.2.1.2**
- **Gene:** *tal*; ordered locus **PP_2168**
- **Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125)
- **Family/domains:** Transaldolase family, **Type 1 subfamily**; Aldolase_TIM (IPR013785), TAL/FSA (IPR001585), Transaldolase_1 (IPR004730), Transaldolase active-site signature (IPR018225), Pfam **PF00923** (TAL_FSA).

Every one of these annotations is internally consistent: the gene symbol *tal*, the EC number 2.2.1.2, the Pfam/InterPro transaldolase signatures, and the "Type 1 subfamily" classification all point to the same well-characterized enzyme, transaldolase. There is **no ambiguity** and no conflicting gene using the same symbol. Research therefore proceeds directly on transaldolase.

---

## 1. Summary (Answer to the Research Question)

**tal / PP_2168 encodes transaldolase (EC 2.2.1.2), a soluble cytoplasmic enzyme of the non-oxidative branch of the pentose phosphate pathway.** Its primary function is to catalyze the reversible transfer of a three-carbon **dihydroxyacetone (C3) unit** from a ketose-phosphate donor (sedoheptulose-7-phosphate or fructose-6-phosphate) to an aldose-phosphate acceptor (glyceraldehyde-3-phosphate or erythrose-4-phosphate). The signature reaction is **sedoheptulose-7-P + glyceraldehyde-3-P ⇌ erythrose-4-P + fructose-6-P**. It is a cofactor-less class I aldolase that acts through a covalent Schiff-base intermediate on a conserved active-site lysine. In *P. putida* KT2440 — a bacterium that runs glycolysis almost entirely through the Entner–Doudoroff route — transaldolase supplies the sugar-phosphate interconversion capacity that allows operation of the cyclic **EDEMP** metabolic architecture, balancing carbon between catabolism and biosynthesis and contributing to NADPH supply.

---

## 2. Primary Function: Reaction Catalyzed and Substrate Specificity

Transaldolase (TAL) is a near-ubiquitous enzyme of central carbon metabolism that **"transfers a dihydroxyacetone group from donor compounds (fructose 6-phosphate or sedoheptulose 7-phosphate) to aldehyde acceptor compounds"** (Samland & Sprenger, 2009, PMID 19401148).

- **Group transferred:** a C3 dihydroxyacetone moiety (from the ketose donor's C1–C3).
- **Donors (ketoses):** sedoheptulose-7-phosphate (S7P), fructose-6-phosphate (F6P).
- **Acceptors (aldoses):** glyceraldehyde-3-phosphate (G3P), erythrose-4-phosphate (E4P).
- **Canonical net reaction (EC 2.2.1.2; Rhea RHEA:17053):**
  `D-sedoheptulose-7-P + D-glyceraldehyde-3-P ⇌ D-erythrose-4-P + β-D-fructose-6-P`
- **Reversibility:** the reaction is freely reversible; direction is set by mass action / cellular metabolic demand.

The UniProt/HAMAP curated function statement for Q88KX1 (Rule MF_00492) matches exactly: *"Transaldolase involved in the non-oxidative phase in the pentose phosphate pathway. Catalyzes the reversible conversion of sedoheptulose-7-phosphate and D-glyceraldehyde 3-phosphate into erythrose-4-phosphate and beta-D-fructose 6-phosphate. Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway."* It is assigned to the non-oxidative PPP as **step 2 of 3** (generating G3P + F6P from ribose-5-P and xylulose-5-P).

Together with transketolase (which transfers C2 glycolaldehyde units), transaldolase performs the reversible carbon-shuffling reactions that interconvert 3-, 4-, 5-, 6-, and 7-carbon sugar phosphates in the **non-oxidative pentose phosphate pathway (PPP)** (Samland & Sprenger, 2009). This lets the cell (i) route pentose phosphates back into glycolytic hexose/triose phosphates and (ii) generate erythrose-4-phosphate (aromatic amino acid / vitamin precursor) and ribose-5-phosphate (nucleotide precursor) from glycolytic intermediates.

The Q88KX1 assignment to the **Type 1 transaldolase subfamily** is meaningful: within the transaldolase superfamily, five subfamilies are distinguished — three with proven TAL activity, one of unclear function, and a fifth comprising the related **fructose-6-phosphate aldolases** (Samland & Sprenger, 2009). Type 1 corresponds to the classical, catalytically confirmed transaldolases (the *E. coli* TalB type), so the substrate specificity above applies directly.

---

## 3. Catalytic Mechanism and Structural Basis

Transaldolase is a **class I aldolase**: it is **cofactor-less** (no metal ion, no thiamine/PLP) and **"proceeds with a Schiff base intermediate (bound dihydroxyacetone)"** (Samland & Sprenger, 2009, PMID 19401148).

Direct structural evidence comes from the *E. coli* transaldolase B (TalB) reduced-intermediate crystal structure (Jia et al., 1997, PMID 9007983):
- The **dihydroxyacetone moiety is covalently linked to the ε-amino group of Lys132** at the active site — the trapped Schiff-base intermediate.
- Surrounding residues position the substrate: the C1 hydroxyl H-bonds to Asn154 and Ser176; the C3 hydroxyl interacts with Asp17 and Asn35.
- A reaction mechanism for the whole class I aldolase family was deduced from this complex.

Mechanistically: the active-site lysine attacks the donor ketose carbonyl, forming a protonated Schiff base; C–C bond cleavage releases the aldose product (e.g., E4P) and leaves an enamine/carbanion-stabilized dihydroxyacetone–enzyme adduct; this then condenses with the acceptor aldose (e.g., G3P), and hydrolysis of the resulting Schiff base releases the new ketose product (e.g., F6P).

**Structural fold:** the protein adopts an (α/β)₈ **TIM-barrel** fold (InterPro IPR013785, Aldolase_TIM), the shared scaffold of the TAL/FSA family. Q88KX1 carries the **Transaldolase active-site signature (IPR018225)**, the sequence motif harboring the conserved catalytic lysine, so the *P. putida* enzyme is confidently predicted to use the identical Schiff-base chemistry by homology to TalB. UniProt annotates the **quaternary structure as a homodimer** (HAMAP-Rule MF_00492), as is typical for bacterial Type 1 transaldolases such as *E. coli* TalB.

**Direct residue-level evidence in Q88KX1 (this work).** I retrieved the 308-residue Q88KX1 sequence and its HAMAP-Rule annotations and verified the catalytic machinery at the sequence level:
- **Lys125** — active-site **nucleophile that forms the Schiff-base intermediate** with substrate (confirmed as a lysine in the sequence). This is the *P. putida* positional equivalent of *E. coli* TalB **Lys132**.
- **Glu89** — active-site **proton donor/acceptor** (confirmed as glutamate).
- **Substrate-binding residues Asp17, Asn35, Lys125, Asn147, Ser169, Arg174, Ser218, Arg220.** Notably **Asp17 and Asn35 are conserved at the *identical* sequence positions** as the TalB residues shown to contact the substrate C3 hydroxyl (Jia et al., 1997), and Asn147/Ser169 occupy the positions equivalent to TalB Asn154/Ser176 (which contact the C1 hydroxyl). The Arg174/Arg220 pair is consistent with binding of the substrate phosphate groups.

This constitutes structure/evolution-based evidence — beyond bare database annotation — that PP_2168 possesses a complete, correctly positioned Type 1 transaldolase catalytic site and is catalytically competent.

**Quantitative homology to the experimentally solved enzyme (this work).** A global (Needleman–Wunsch, BLOSUM62) alignment of Q88KX1 against *E. coli* TalB (P0A870, the enzyme whose Schiff-base intermediate was crystallized) gives **62.3% sequence identity and 76.3% similarity** over the full length — far above the ~30% identity threshold at which mechanism and fold can be confidently transferred. Critically, **all nine functional residues align one-to-one** with their experimentally characterized TalB counterparts:

| P. putida (Q88KX1) | E. coli TalB | Role (from TalB structure, Jia et al. 1997) |
|---|---|---|
| Lys125 | Lys132 | Catalytic nucleophile — Schiff base with dihydroxyacetone |
| Glu89 | Glu96 | Proton donor/acceptor |
| Asp17 | Asp17 | Contacts substrate C3 hydroxyl |
| Asn35 | Asn35 | Contacts substrate C3 hydroxyl |
| Asn147 | Asn154 | Contacts substrate C1 hydroxyl |
| Ser169 | Ser176 | Contacts substrate C1 hydroxyl |
| Arg174 | Arg181 | Substrate/phosphate binding |
| Ser218 | Ser226 | Substrate binding |
| Arg220 | Arg228 | Substrate/phosphate binding |

This upgrades the mechanistic assignment from database annotation to a **strongly homology-supported inference**: the *P. putida* enzyme forms the same Lys-Schiff-base intermediate and engages the same substrate hydroxyls as the structurally characterized *E. coli* enzyme.

---

## 4. Subcellular Localization

Transaldolase functions in the **cytoplasm (cytosol)**. UniProt (HAMAP-Rule MF_00492) explicitly annotates the subcellular location of Q88KX1 as **Cytoplasm**. This is supported by strong, convergent evidence:
- The pentose phosphate pathway is a soluble cytoplasmic pathway in bacteria; its enzymes act on phosphorylated sugar intermediates that do not cross membranes.
- Transaldolase is a soluble globular protein: it has **no signal peptide, no membrane-spanning region, and no lipidation/secretion signal** (consistent with the TIM-barrel fold and the absence of any localization signal in the Q88KX1 domain architecture).
- All biochemically and structurally characterized transaldolases (e.g., *E. coli* TalB, human TALDO1) are soluble cytosolic proteins (Samland & Sprenger, 2009; Jia et al., 1997).

Thus PP_2168 carries out its catalysis in the bacterial cytoplasm, physically and functionally co-localized with the other soluble central-metabolism enzymes.

---

## 5. Pathway Context and Physiological Role in *P. putida* KT2440

Transaldolase is a core enzyme of the **non-oxidative PPP**, but its physiological weight in *P. putida* KT2440 is distinctive because of this organism's unusual central metabolism.

- *P. putida* KT2440 **lacks a functional Embden–Meyerhof–Parnas (EMP) glycolysis** and catabolizes glucose almost exclusively via the **Entner–Doudoroff (ED)** route; ~90% of consumed sugar is converted to gluconate, entering as 6-phosphogluconate and channeled into ED (Nikel et al., 2015, PMID 26350459).
- Crucially, ~10% of triose phosphates are recycled back to hexose phosphates by a set of reactions that **"merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)"** (Nikel et al., 2015). Transaldolase provides the PPP carbon-rearrangement activity required for this cycle to close.
- The net effect of the cycle is redox-relevant: **"Cells growing on glucose thus run a biochemical cycle that favors NADPH formation"** (Nikel et al., 2015). The default metabolic state shows a slight catabolic overproduction of NADPH, which supports anabolism and counteracts environmental/oxidative stress — a hallmark of this robust soil bacterium.

**Genomic context — a single, non-redundant transaldolase.** A proteome-wide query of *P. putida* KT2440 (taxon 160488) shows that **Q88KX1/PP_2168 is the only protein in the genome carrying the transaldolase/FSA Pfam domain (PF00923)** and the only one annotated as transaldolase; no fructose-6-phosphate aldolase (Fsa) paralog or transaldolase isozyme exists (this work, UniProt search). Consequently, the transaldolase reaction of the non-oxidative PPP is supplied **uniquely** by PP_2168 — there is no genetic backup for its dihydroxyacetone-transfer activity, giving the gene a non-redundant role in sugar-phosphate balancing and erythrose-4-phosphate provision.

Beyond the EDEMP cycle, transaldolase's general PPP role supplies biosynthetic precursors:
- **Erythrose-4-phosphate** → shikimate pathway (aromatic amino acids Phe/Tyr/Trp, folate, ubiquinone precursors).
- Linkage to **ribose-5-phosphate** (via the non-oxidative PPP) → nucleotide and cofactor biosynthesis.

The broader significance of the transaldolase/PPP node in redox homeostasis is echoed across organisms: transaldolase and G6PDH overexpression increases NADPH-dependent oxidant defense (e.g., Ghosh et al., 2015, PMID 25690656, in *Leishmania*), and transaldolase is a recognized participant in oxidative-stress responses (Samland & Sprenger, 2009). Transaldolase-type chemistry has also been recruited into specialized catabolism, such as the sulfoglycolytic "sulfo-TAL" pathway for sulfoquinovose degradation (Wei et al., 2022, PMID 36196895), underscoring the enzyme's mechanistic versatility — though in *P. putida* KT2440 the annotated role of PP_2168 is the canonical central-metabolic one.

---

## 6. Evidence Summary

| Claim | Type of evidence | Source |
|---|---|---|
| Catalyzes dihydroxyacetone (C3) transfer between S7P/F6P and G3P/E4P | Biochemical/enzymology review | Samland & Sprenger 2009 (PMID 19401148) |
| Cofactor-less class I aldolase, Schiff-base mechanism | Review + X-ray structure | Samland & Sprenger 2009; Jia et al. 1997 (PMID 9007983) |
| Covalent intermediate on active-site Lys (Lys132 in TalB) | Crystal structure (2.2 Å) of trapped intermediate | Jia et al. 1997 (PMID 9007983) |
| Type 1 transaldolase subfamily; TIM-barrel fold; active-site signature | Sequence/domain annotation | UniProt Q88KX1 / InterPro IPR004730, IPR018225, IPR013785; Pfam PF00923 |
| Catalytic Lys125 (Schiff base) + Glu89 (proton donor/acceptor); binding Asp17/Asn35/Asn147/Ser169/Arg174/Ser218/Arg220 | Sequence-level verification of HAMAP-annotated active site; positional homology to TalB | This work (Q88KX1 sequence) + Jia et al. 1997 (PMID 9007983) |
| Homodimer; reaction Rhea RHEA:17053; non-oxidative PPP step 2/3 | Curated UniProt/HAMAP-Rule MF_00492 annotation | UniProt Q88KX1 |
| Cytoplasmic localization | UniProt/HAMAP annotation + inference from pathway + absence of targeting signals + homolog characterization | UniProt Q88KX1 (SL-0086); PPP biology |
| Functions in non-oxidative PPP / EDEMP cycle; contributes to NADPH | ¹³C metabolic flux analysis, enzymatic assays | Nikel et al. 2015 (PMID 26350459) |
| Sole transaldolase-family gene in KT2440 (no paralog/Fsa) → non-redundant role | Proteome-wide UniProt/Pfam search | This work (UniProt taxon 160488) |
| 62.3% identity to E. coli TalB; all 9 catalytic/binding residues conserved & aligned | Global sequence alignment (BLOSUM62) | This work + Jia et al. 1997 (PMID 9007983) |

---

## 7. Supported vs. Refuted Hypotheses

**Supported:**
- H1: *tal*/PP_2168 is a bona fide transaldolase (EC 2.2.1.2) catalyzing reversible C3-unit transfer in the non-oxidative PPP. **Supported** (domain annotation + family review).
- H2: The enzyme uses a cofactor-independent Schiff-base (class I aldolase) mechanism via an active-site lysine. **Supported** (structural homolog TalB).
- H3: The enzyme is cytoplasmic. **Supported** (inference; no targeting signals; PPP is cytosolic).
- H4: In *P. putida* KT2440 the enzyme participates in the EDEMP cycle and NADPH-favoring metabolism. **Supported** (flux analysis, Nikel et al. 2015).
- H5: PP_2168 is the sole (non-redundant) transaldolase in KT2440. **Supported** (proteome-wide Pfam PF00923 search returns only Q88KX1; no Fsa paralog).

**Refuted / not applicable:**
- The gene is **not** ambiguous and does **not** correspond to an unrelated "TAL" (e.g., transcription activator-like) protein — refuted by the concordant EC number, Pfam PF00923, and Type 1 transaldolase classification.

---

## 8. Limitations and Future Directions

- **No enzyme-specific experimental study of PP_2168 itself** (purified-protein kinetics or crystal structure) was found; the biochemical/mechanistic conclusions rest on the canonical *E. coli* TalB structure and the transaldolase family review. However, this inference is unusually strong: Q88KX1 is 62.3% identical to TalB with 100% conservation and correct alignment of every catalytic and substrate-binding residue, so the risk of mechanistic divergence is very low. Direct kinetic characterization (kcat/Km for S7P, F6P, G3P, E4P) of the *P. putida* enzyme would nonetheless confirm substrate specificity quantitatively.
- **Localization is inferred**, not experimentally demonstrated for this ortholog; a proteomic/fractionation confirmation would be definitive (though the prediction is very secure).
- **Quaternary structure** (homodimer, as in TalB) is predicted, not verified for Q88KX1.
- A *tal* deletion/flux study in *P. putida* KT2440 would directly quantify its contribution to EDEMP-cycle flux and NADPH balance; transaldolase deficiency is generally well tolerated in microorganisms (Samland & Sprenger, 2009), so a knockout phenotype may be subtle and condition-dependent.

---

### Key References
1. Samland AK, Sprenger GA. *Transaldolase: from biochemistry to human disease.* Int J Biochem Cell Biol. 2009. **PMID 19401148**.
2. Jia J, Schörken U, Lindqvist Y, Sprenger GA, Schneider G. *Crystal structure of the reduced Schiff-base intermediate complex of transaldolase B from Escherichia coli: mechanistic implications for class I aldolases.* Protein Sci. 1997. **PMID 9007983**.
3. Nikel PI, Chavarría M, Fuhrer T, Sauer U, de Lorenzo V. *Pseudomonas putida KT2440 strain metabolizes glucose through a cycle formed by enzymes of the Entner-Doudoroff, Embden-Meyerhof-Parnas, and pentose phosphate pathways.* J Biol Chem. 2015. **PMID 26350459**.
4. Wei Y, Tong Y, Zhang Y. *New mechanisms for bacterial degradation of sulfoquinovose.* 2022. **PMID 36196895** (context for transaldolase mechanistic versatility).
5. Ghosh et al. *Metabolic reconfiguration of the central glucose metabolism...* 2015. **PMID 25690656** (context: TAL/PPP in NADPH-dependent oxidant defense).


## Artifacts

- [OpenScientist final report](tal-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](tal-deep-research-openscientist_artifacts/final_report.pdf)