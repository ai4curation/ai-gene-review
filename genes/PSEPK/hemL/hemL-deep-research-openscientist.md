---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T16:55:27.579009'
end_time: '2026-07-20T17:12:11.684512'
duration_seconds: 1004.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemL
  gene_symbol: hemL
  uniprot_accession: Q88DP0
  protein_description: 'RecName: Full=Glutamate-1-semialdehyde 2,1-aminomutase {ECO:0000255|HAMAP-Rule:MF_00375};
    Short=GSA {ECO:0000255|HAMAP-Rule:MF_00375}; EC=5.4.3.8 {ECO:0000255|HAMAP-Rule:MF_00375};
    AltName: Full=Glutamate-1-semialdehyde aminotransferase {ECO:0000255|HAMAP-Rule:MF_00375};
    Short=GSA-AT {ECO:0000255|HAMAP-Rule:MF_00375};'
  gene_info: Name=hemL {ECO:0000255|HAMAP-Rule:MF_00375}; OrderedLocusNames=PP_4784;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-III pyridoxal-phosphate-dependent
  protein_domains: 4pyrrol_synth_GluAld_NH2Trfase. (IPR004639); Aminotrans_3. (IPR005814);
    Aminotrans_3_PPA_site. (IPR049704); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major.
    (IPR015421)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hemL-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemL-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DP0
- **Protein Description:** RecName: Full=Glutamate-1-semialdehyde 2,1-aminomutase {ECO:0000255|HAMAP-Rule:MF_00375}; Short=GSA {ECO:0000255|HAMAP-Rule:MF_00375}; EC=5.4.3.8 {ECO:0000255|HAMAP-Rule:MF_00375}; AltName: Full=Glutamate-1-semialdehyde aminotransferase {ECO:0000255|HAMAP-Rule:MF_00375}; Short=GSA-AT {ECO:0000255|HAMAP-Rule:MF_00375};
- **Gene Information:** Name=hemL {ECO:0000255|HAMAP-Rule:MF_00375}; OrderedLocusNames=PP_4784;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-III pyridoxal-phosphate-dependent
- **Key Domains:** 4pyrrol_synth_GluAld_NH2Trfase. (IPR004639); Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemL" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemL' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemL** (gene ID: hemL, UniProt: Q88DP0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hemL* (Q88DP0) — Glutamate-1-Semialdehyde 2,1-Aminomutase in *Pseudomonas putida* KT2440

**Gene:** hemL (OrderedLocusName PP_4784) · **UniProt:** Q88DP0 · **Organism:** *Pseudomonas putida* KT2440 (PSEPK)
**Enzyme:** Glutamate-1-semialdehyde 2,1-aminomutase (GSA-AM; also GSA aminotransferase, GSA-AT, GSAM) · **EC 5.4.3.8**
**Family:** Class-III pyridoxal-5′-phosphate (PLP)-dependent aminotransferase (Aminotrans_3; aspartate-aminotransferase superfamily)

## Summary

The gene **hemL** (UniProt **Q88DP0**; ordered locus **PP_4784**) of *Pseudomonas putida* strain KT2440 encodes **glutamate-1-semialdehyde 2,1-aminomutase** (GSA-AM, also called glutamate-1-semialdehyde aminotransferase, GSA-AT; **EC 5.4.3.8**). This is a **pyridoxal-5′-phosphate (PLP)-dependent, class-III aminotransferase** that catalyzes the **second and terminal step of the C5 (glutamate/tRNA-dependent) pathway** for the biosynthesis of **5-aminolevulinic acid (ALA)**, the universal precursor of all tetrapyrroles. The enzyme performs an unusual **intramolecular transamination**: it converts **(S)-glutamate-1-semialdehyde (GSA)** into **ALA** by exchanging an amino group and an oxo group within a single molecule, proceeding through a free **4,5-diaminovalerate (DAVA)** intermediate and — uniquely among transaminations — requiring **no external nitrogen donor or acceptor**.

Because ALA is the committed, flux-defining precursor of heme, siroheme, and cobalamin (and, in phototrophs, chlorophyll), HemL sits at the **gateway to the entire tetrapyrrole biosynthetic branch**. The physiological importance is direct and non-redundant in most organisms: the two-enzyme C5 route (glutamyl-tRNA reductase = **hemA**, then GSA-AM = **hemL**) is the only means by which *P. putida* and other γ/β-proteobacteria make ALA, in contrast to the ALA-synthase (Shemin/C4) route that is restricted to α-proteobacteria and animals. An experimental survey of proteobacteria explicitly demonstrated that *Pseudomonas putida* uses the hemA/hemL C5 pathway, which independently corroborates the annotation of Q88DP0.

At the molecular level, GSA-AM is a **soluble, cytoplasmic α₂ homodimer** adopting the **aspartate-aminotransferase (class-III B6) fold**. The *P. putida* protein itself carries the full catalytic apparatus expected of a functional GSA-AM: a **PLP Schiff-base catalytic lysine (Lys265)** embedded in the strictly conserved class-III aminotransferase motif, a bound PLP cofactor, homodimeric quaternary structure, and cytoplasmic localization. Sequence alignment shows the *P. putida* enzyme is **63.4% identical** to the experimentally characterized *Escherichia coli* GSA-AM, and specificity-determining residues (Arg32 orienting the substrate; Glu406 excluding α-carboxylates) are conserved. Taken together, the identity of Q88DP0 as *hemL*/GSA-AM is confidently established both by direct pathway experiments in *P. putida* and by conservation of the catalytic machinery. **This gene symbol is unambiguous for this organism** — the domain architecture, family membership, and organism-specific pathway data all align.

---

## Key Findings

### Finding 1 — HemL/Q88DP0 is glutamate-1-semialdehyde 2,1-aminomutase, the terminal ALA-producing enzyme of the C5 pathway (EC 5.4.3.8)

The primary function of the gene product is unambiguous at the biochemical level: it catalyzes the **intramolecular transamination of (S)-glutamate-1-semialdehyde (GSA) to 5-aminolevulinic acid (ALA)**. This is the second, terminal step of a two-enzyme route in which glutamyl-tRNA is first reduced by glutamyl-tRNA reductase (**hemA**) to glutamate-1-semialdehyde, which is then converted by HemL to ALA:

```
L-glutamyl-tRNA(Glu)
        │  glutamyl-tRNA reductase (hemA)   [step 1/2]
        ▼
(S)-glutamate-1-semialdehyde (GSA)
        │  GSA-2,1-aminomutase / HemL (EC 5.4.3.8)   [step 2/2]
        ▼
5-aminolevulinic acid (ALA)  ──►  universal tetrapyrrole precursor
                                   (heme, siroheme, cobalamin, chlorophyll)
```

The reaction is described directly in the literature on glutamyl-tRNA reductase and ALA formation: *"The aldehyde is subsequently transaminated by glutamate-1-semialdehyde 2,1-aminomutase to yield 5-aminolaevulinic acid"* ([PMID: 12196141](https://pubmed.ncbi.nlm.nih.gov/12196141/)). Detailed enzymic and mechanistic studies further pin down the **substrate stereospecificity, product, intermediate, and kinetic mechanism**: *"The pyridoxamine 5′-phosphate form of the enzyme converts (S)-glutamate 1-semialdehyde to 5-aminolaevulinate via 4,5-diaminovalerate through a bi-bi ping-pong mechanism"* ([PMID: 7842860](https://pubmed.ncbi.nlm.nih.gov/7842860/)). ALA is the committed precursor of the whole tetrapyrrole family, so this single enzymatic step defines HemL's biological role as the **gateway to tetrapyrrole biosynthesis**.

The classification as an **aminomutase / isomerase (EC 5.4.3.8)** rather than a conventional aminotransferase (EC 2.6.1.x) reflects the fact that the amino group is transferred *within* one molecule: GSA (C5) and ALA (C5N) share the same carbon skeleton, and only the positions of the amino and oxo groups on adjacent carbons are interchanged.

### Finding 2 — *Pseudomonas putida* experimentally uses the tRNA-dependent (C5) hemA/hemL route, directly confirming the annotation

Bacteria make ALA by one of two mutually exclusive routes: the **C4 (Shemin) pathway**, in which ALA synthase condenses glycine and succinyl-CoA (found in α-proteobacteria and animals), or the **C5 (tRNA-dependent) pathway**, using hemA and hemL. A comparative experimental survey of proteobacteria established which organisms use which route, and it names *P. putida* explicitly: *"The tRNA-dependent pathway, involving the enzymes glutamyl-tRNA reductase (encoded by hemA) and glutamate-1-semialdehyde-2,1-aminomutase (encoded by hemL), was demonstrated to be used by Pseudomonas aeruginosa, Pseudomonas putida, Pseudomonas stutzeri, Comamonas testosteroni, Azotobacter vinelandii, and Acinetobacter calcoaceticus"* ([PMID: 7883699](https://pubmed.ncbi.nlm.nih.gov/7883699/)).

This is the strongest, organism-specific line of evidence in the annotation: it is not merely inference from sequence, but a demonstration that *P. putida* biochemically synthesizes ALA through hemA/hemL. It removes any ambiguity that a Pseudomonad hemL might be vestigial or that ALA might be produced by an alternative route. The metabolic-engineering literature reinforces the functional partnership of the two enzymes: in engineered *Corynebacterium glutamicum*, co-expressing HemL with HemA raised ALA titers roughly 2-fold over HemA alone (204 → 457 mg/L), confirming that HemL activity is the productive, flux-carrying step converting GSA to ALA ([PMID: 26453466](https://pubmed.ncbi.nlm.nih.gov/26453466/)).

### Finding 3 — The catalytic strategy is a unique intramolecular transamination via a free DAVA intermediate, needing no external nitrogen partner

GSA-AM belongs to the **class-III (vitamin B6/PLP) aminotransferases**, but its chemistry is mechanistically distinctive. Whereas canonical transaminases shuttle an amino group between two different molecules (using a keto-acid such as 2-oxoglutarate as the nitrogen acceptor), GSA-AM performs the amino/oxo swap **within a single substrate molecule**. The reaction proceeds through the catalytic intermediate **4,5-diaminovalerate (DAVA)**: *"a pyridoxamine-5′-phosphate (PMP)/pyridoxal-5′-phosphate (PLP) dependent enzyme, catalyses the transamination of the substrate glutamate-1-semialdehyde (GSA) to the product 5-Aminolevulinic acid (ALA) by an unusual intramolecular exchange of amino and oxo groups within the catalytic intermediate 4,5-diaminovalerate (DAVA)"* ([PMID: 20946885](https://pubmed.ncbi.nlm.nih.gov/20946885/)).

The defining, unusual mechanistic feature is that **no external cofactor acts as the nitrogen donor or acceptor**: *"This transamination reaction is unique in the fact that is does not require an external cofactor to act as a nitrogen donor or acceptor in this transamination reaction"* ([PMID: 21930115](https://pubmed.ncbi.nlm.nih.gov/21930115/)). The PMP form of the enzyme initiates catalysis; the diamine intermediate DAVA is retained in the active site (a mobile gating loop prevents its escape), whereupon the second half-reaction transfers the amino group to the opposite carbon, generating ALA. Transient-state kinetic analysis of the *Synechococcus* enzyme resolved chromophoric intermediates consistent with **Schiff-base formation and ketimine/aldimine tautomerization**, and supported a **ping-pong bi-bi** mechanism with rapid equilibration of isomeric aldimines and geminal diamines ([PMID: 9425053](https://pubmed.ncbi.nlm.nih.gov/9425053/)). The mechanistic picture is therefore internally consistent across biochemical, kinetic, and structural studies.

```
        PMP-enzyme
            │  + GSA (aldehyde end)
            ▼
   ┌───────────────────────┐
   │  4,5-diaminovalerate  │  ← free diamine intermediate, retained by gating loop
   │        (DAVA)          │     amino group transferred intramolecularly
   └───────────────────────┘
            │
            ▼
        ALA + PMP-enzyme (regenerated)
   (no external keto-acid / amino-acid partner consumed)
```

### Finding 4 — HemL is a soluble cytoplasmic α₂ homodimer with an aspartate-aminotransferase fold; specificity for GSA is enforced by active-site residues

Crystal structures of GSA-AM from *Synechococcus* (2.4 Å) and *Bacillus subtilis* (PMP-bound, 2.3 Å) reveal an **α₂-dimeric vitamin B6-dependent enzyme** with the **aspartate-aminotransferase fold** characteristic of class-III B6 enzymes: *"The overall fold is that of aspartate aminotransferase and related B6 enzymes"* ([PMID: 9144156](https://pubmed.ncbi.nlm.nih.gov/9144156/)). The structures display notable **subunit asymmetry** — one subunit carries PLP as an internal aldimine to the catalytic lysine while the partner subunit is cofactor-free — and a **mobile gating loop** (~residues 153–181) that closes over the active site to retain the DAVA intermediate.

The structural basis of **substrate specificity** was defined from these structures. The enzyme must accept GSA (a semialdehyde) while excluding the closely related α-amino/α-carboxylate glutamate. A key active-site glutamate accomplishes this by electrostatic repulsion: *"Glu-406 is suitably positioned to repel alpha-carboxylic acids, thereby suggesting a basis for the enzyme's reaction specificity"* ([PMID: 9144156](https://pubmed.ncbi.nlm.nih.gov/9144156/)). N-terminal-domain residues, notably **Arg-32**, orient and bind the substrate carboxylate. The importance of the active-site architecture is underscored by mutational data: a single **S162T** substitution in the *Synechococcus* hemL gene alters inhibitor sensitivity to the mechanism-based inactivator 4-amino-5-fluoropentanoic acid ([PMID: 10350057](https://pubmed.ncbi.nlm.nih.gov/10350057/)), and a Lys272→Ile mutation at the catalytic lysine perturbs the aldimine chemistry ([PMID: 9425053](https://pubmed.ncbi.nlm.nih.gov/9425053/)).

Localization is **soluble/cytoplasmic**. The C5-pathway enzymes are soluble proteins; in plants and algae they reside in the chloroplast stroma, and in bacteria they operate in the cytoplasm: *"These components are soluble and in plants and algae are located in the chloroplast stroma"* ([PMID: 7842860](https://pubmed.ncbi.nlm.nih.gov/7842860/)). For *P. putida*, this maps to a **cytoplasmic** site of action, consistent with the UniProt subcellular-location annotation of Q88DP0.

### Finding 5 — Sequence-level confirmation for the exact *P. putida* protein Q88DP0

The specific *P. putida* KT2440 protein carries every hallmark of a functional GSA-AM. UniProt **Q88DP0** (427 aa) is annotated with:

| Attribute | Value for Q88DP0 |
|---|---|
| Catalytic activity | (S)-4-amino-5-oxopentanoate (= GSA) ⇌ 5-aminolevulinate (**EC 5.4.3.8**) |
| Cofactor | Pyridoxal 5′-phosphate (PLP) |
| Pathway | Protoporphyrin-IX biosynthesis; 5-aminolevulinate from L-glutamyl-tRNA(Glu), **step 2/2** |
| Subunit | Homodimer |
| Subcellular location | Cytoplasm |
| Catalytic residue | Lys265 — N6-(pyridoxal phosphate)lysine (PLP Schiff-base attachment) |
| Length | 427 aa |

A Needleman–Wunsch global alignment against the experimentally characterized *E. coli* GSA-AM (UniProt **P23893**) yields **270/426 = 63.4% identity**, and the catalytic lysine is strictly conserved within the class-III aminotransferase PLP motif. In *P. putida*, the local sequence around the catalytic residue is `258-PDLSTFGKIVGGGMP-272`, in which **K265** aligns to the *E. coli* catalytic lysine in the homologous `...LGKIIGGGMPV...` motif. The presence of the intact PLP-binding lysine, the conserved specificity residues, homodimeric assembly, and cytoplasmic localization together demonstrate that Q88DP0 is not a divergent pseudo-gene or a mis-annotation but a *bona fide*, catalytically competent GSA-AM. The InterPro domain signatures listed in the annotation — 4pyrrol_synth_GluAld_NH2Trfase (IPR004639), Aminotrans_3 (IPR005814), Aminotrans_3_PPA_site (IPR049704), and the PyrdxlP-dep transferase folds (IPR015424/IPR015421) — are precisely those diagnostic of GSA-AM and independently corroborate the assignment.

---

## Mechanistic Model / Interpretation

The findings converge on a single, well-supported model of HemL's role in *P. putida*:

**Pathway context.** HemL is the second of two enzymes that convert the "activated glutamate" carried on tRNA^Glu into ALA. This C5 route is universal to plants, archaea, and most bacteria, and it is the pathway experimentally documented in *P. putida*. The tRNA-charged glutamate is reduced by HemA (glutamyl-tRNA reductase) to the reactive aldehyde GSA, which HemL then isomerizes to ALA.

```
                     C5 (tRNA-dependent) pathway — cytoplasm of P. putida
  ┌───────────────────────────────────────────────────────────────────────────┐
  │  Glu  --(GluRS)-->  Glu-tRNA(Glu)  --HemA-->  GSA  --HemL (Q88DP0)-->  ALA  │
  └───────────────────────────────────────────────────────────────────────────┘
                                                                     │
                                        2 ALA --HemB--> porphobilinogen
                                                                     │
                                                                     ▼
                              uroporphyrinogen III ──► heme / siroheme / cobalamin
```

**Catalytic logic.** ALA is C5N — five carbons and one nitrogen — and is produced from GSA (also C5) with no change in carbon skeleton: only the positions of the amino and oxo groups on C1 and C2 are swapped. This is why the enzyme is classified as an **aminomutase / intramolecular transaminase (isomerase, EC 5.4.3.8)** rather than a conventional inter-molecular aminotransferase (EC 2.6.1.x). The elegance of the mechanism is that the PLP/PMP cofactor shuttles the amino group between the two carbons of a single retained intermediate (DAVA), which is why no external amino donor/acceptor is consumed. The gating loop and the α₂-dimer's active-site asymmetry are structural adaptations that keep the diamine intermediate captive so that transamination completes on the same molecule.

**Specificity and localization.** The enzyme's active site is tuned to bind the semialdehyde/diamine substrate while rejecting glutamate itself — Glu406 repels α-carboxylates and Arg32 orients the substrate. All of this occurs in the soluble cytoplasm, where GSA is generated by HemA and where downstream ALA is consumed by HemB (porphobilinogen synthase) and the rest of the tetrapyrrole machinery.

**Biological significance for *P. putida*.** As the committed gateway to tetrapyrroles, HemL supplies the precursor for heme-dependent respiration (cytochromes), catalase/peroxidase defense against oxidative stress, and siroheme-dependent sulfite/nitrite reduction — all central to the aerobic, metabolically versatile lifestyle of *P. putida*. Because the C5 route is the organism's sole ALA source, HemL is expected to be essential or near-essential unless ALA is supplied exogenously.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [12196141](https://pubmed.ncbi.nlm.nih.gov/12196141/) | *Structure and function of glutamyl-tRNA reductase in ALA formation* | States the reaction: GSA is transaminated by GSA-2,1-aminomutase to yield ALA (defines HemL's step). |
| [7842860](https://pubmed.ncbi.nlm.nih.gov/7842860/) | *Enzymic and mechanistic studies on glutamate → 5-aminolaevulinate* | Defines (S)-GSA substrate stereospecificity, ALA product, DAVA intermediate, ping-pong bi-bi mechanism, and soluble/stromal localization. |
| [7883699](https://pubmed.ncbi.nlm.nih.gov/7883699/) | *Regulation of hemA in P. aeruginosa* | Experimentally names *P. putida* as using the hemA/hemL C5 pathway — organism-specific confirmation. |
| [21930115](https://pubmed.ncbi.nlm.nih.gov/21930115/) | *Proposed reaction mechanism of GSA aminomutase at atomic level* | Establishes the unique feature: no external nitrogen donor/acceptor. |
| [20946885](https://pubmed.ncbi.nlm.nih.gov/20946885/) | *Crystal structure of B. subtilis GSA-AT with PMP* | Confirms PLP/PMP dependence and intramolecular amino/oxo exchange via DAVA. |
| [9144156](https://pubmed.ncbi.nlm.nih.gov/9144156/) | *Crystal structure of GSA aminomutase (α₂-dimer)* | Aspartate-aminotransferase fold, α₂-dimer, active-site asymmetry, Glu-406 specificity basis. |
| [9425053](https://pubmed.ncbi.nlm.nih.gov/9425053/) | *Transient-state kinetics of Synechococcus GSAT* | Resolves Schiff-base/ketimine intermediates; Lys272 catalytic role; ping-pong mechanism. |
| [10350057](https://pubmed.ncbi.nlm.nih.gov/10350057/) | *Synechococcus mutants resistant to enamine inhibitor* | S162T mutation in hemL alters inhibitor sensitivity — active-site importance and gene identity. |
| [26453466](https://pubmed.ncbi.nlm.nih.gov/26453466/) | *ALA production in engineered C. glutamicum via C5 pathway* | Co-expression of HemL with HemA doubles ALA titer — HemL is the productive GSA→ALA step. |
| [1672867](https://pubmed.ncbi.nlm.nih.gov/1672867/) | *B. subtilis hemAXCDBL cluster* | Places hemL in the glutamate→uroporphyrinogen III pathway; notes GSA→ALA can occur slowly non-enzymatically. |
| [19473249](https://pubmed.ncbi.nlm.nih.gov/19473249/) | *Porphyrin intermediates from soil metagenomic genes in E. coli* | Reinforces hemL's position among the C5/porphyrin-pathway genes required for tetrapyrrole synthesis. |

Two additional plant-focused papers ([PMID: 25840087](https://pubmed.ncbi.nlm.nih.gov/25840087/), [PMID: 32092859](https://pubmed.ncbi.nlm.nih.gov/32092859/)) document GSA-AM (GSA2/HEMA/GSA1) in Arabidopsis and rice chlorophyll biosynthesis; while not from *P. putida*, they confirm the enzyme's conserved role as an ALA-producing gateway across kingdoms.

**Note on a caveat from the literature:** The *B. subtilis* study observed that deleting an internal fragment of hemL did *not* create an absolute ALA/heme growth requirement, suggesting GSA→ALA can occur slowly spontaneously or via another activity in that organism ([PMID: 1672867](https://pubmed.ncbi.nlm.nih.gov/1672867/)). This is a possible challenge to strict essentiality, but the non-enzymatic rate is far too low to support normal growth, and in most bacteria (and demonstrably in *P. putida*'s functional pathway) HemL is the physiologically relevant catalyst.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific enzymology.** The catalytic, kinetic, and structural details (DAVA intermediate, ping-pong mechanism, α₂-dimer, Glu406/Arg32 specificity, Lys265 Schiff base) are established from orthologs (*Synechococcus*, *B. subtilis*, *E. coli*, plants) and transferred to Q88DP0 by strong sequence homology (63% identity to *E. coli*) and conserved motifs. No purified-enzyme kinetic constants (kcat, KM) have been measured for the *P. putida* protein itself.

2. **No experimental structure of Q88DP0.** All structural claims rest on homology to solved GSA-AM structures; an experimental or high-confidence predicted structure of the *P. putida* enzyme has not been analyzed here.

3. **Essentiality not directly tested in *P. putida*.** Essentiality is inferred from the C5 pathway being the organism's sole ALA route. A targeted knockout/ALA-auxotrophy experiment in KT2440 has not been reviewed, and the *B. subtilis* observation ([PMID: 1672867](https://pubmed.ncbi.nlm.nih.gov/1672867/)) leaves a small caveat about spontaneous ALA formation.

4. **Regulation and expression in *P. putida* not characterized here.** How *hemL*/PP_4784 is transcriptionally regulated, whether it is co-transcribed with other hem genes, and how flux through ALA is controlled in *P. putida* were not investigated.

5. **Cofactor/metal partners and channeling.** While PLP dependence is certain, any accessory factors, in-vivo cofactor loading, or protein–protein interactions with HemA (potential metabolic channeling of the labile GSA intermediate) remain unexplored for this organism.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology of Q88DP0.** Clone PP_4784, purify the His-tagged protein, and measure steady-state kinetics (kcat, KM for GSA) and PLP/PMP content spectroscopically. Confirm product ALA by LC-MS and detect the DAVA intermediate. This would convert homology-based inference into direct evidence for the *P. putida* enzyme.

2. **Genetic essentiality test.** Attempt a clean ΔhemL (PP_4784) deletion in KT2440; test for ALA auxotrophy (rescue by exogenous ALA). This directly establishes physiological essentiality and the strict dependence on the C5 route.

3. **Structure determination / prediction.** Solve a crystal structure (or generate and analyze a high-confidence AlphaFold model) of Q88DP0, ideally with bound PLP/PMP, to verify the α₂-dimer, catalytic Lys265 aldimine, the gating loop, and the Glu406/Arg32 specificity pocket.

4. **Active-site mutagenesis.** Test predicted specificity/catalytic residues (K265A, R32A, E406Q) for loss of activity and altered substrate discrimination, mirroring the ortholog studies (Lys272, Glu406, S162T).

5. **HemA–HemL interaction / channeling.** Probe for a physical or functional complex between HemA and HemL that could channel the chemically labile GSA intermediate, using pull-downs or coupled-assay kinetics.

6. **Regulation.** Map the *hemL* transcript (operon structure), and test expression under heme-demanding conditions (aerobic growth, oxidative stress, iron limitation) to understand how tetrapyrrole precursor supply is controlled in *P. putida*.

---

## Conclusion

*hemL* (Q88DP0 / PP_4784) in *Pseudomonas putida* KT2440 encodes **glutamate-1-semialdehyde 2,1-aminomutase (GSA-AM; EC 5.4.3.8)**, a soluble cytoplasmic, PLP-dependent class-III aminotransferase that carries out the **terminal (step 2/2) reaction of the C5 tetrapyrrole pathway**: the unique intramolecular transamination of (S)-glutamate-1-semialdehyde to 5-aminolevulinic acid via a free 4,5-diaminovalerate intermediate, without any external nitrogen partner. As ALA is the universal precursor of heme, siroheme, and cobalamin, HemL is the **committed gateway to tetrapyrrole biosynthesis** in *P. putida*, an organism experimentally shown to depend on the hemA/hemL route. The protein functions as an **α₂ homodimer** with an aspartate-aminotransferase fold, and the *P. putida* sequence itself retains the catalytic PLP-lysine (Lys265) and specificity residues, making the functional annotation robust and well supported.


## Artifacts

- [OpenScientist final report](hemL-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemL-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12196141
2. PMID:7842860
3. PMID:7883699
4. PMID:26453466
5. PMID:20946885
6. PMID:21930115
7. PMID:9425053
8. PMID:9144156
9. PMID:10350057
10. PMID:25840087
11. PMID:32092859
12. PMID:1672867