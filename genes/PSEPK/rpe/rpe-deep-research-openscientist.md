---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T09:11:25.393881'
end_time: '2026-07-15T09:24:12.431606'
duration_seconds: 767.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rpe
  gene_symbol: rpe
  uniprot_accession: Q88QS3
  protein_description: 'RecName: Full=Ribulose-phosphate 3-epimerase {ECO:0000256|ARBA:ARBA00013188,
    ECO:0000256|HAMAP-Rule:MF_02227}; EC=5.1.3.1 {ECO:0000256|ARBA:ARBA00013188, ECO:0000256|HAMAP-Rule:MF_02227};'
  gene_info: Name=rpe {ECO:0000256|HAMAP-Rule:MF_02227, ECO:0000313|EMBL:AAN66045.2};
    OrderedLocusNames=PP_0415 {ECO:0000313|EMBL:AAN66045.2};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ribulose-phosphate 3-epimerase family.
  protein_domains: Aldolase_TIM. (IPR013785); Ribul_P_3_epim. (IPR026019); Ribul_P_3_epim-like.
    (IPR000056); RibuloseP-bd_barrel. (IPR011060); Ribul_P_3_epim (PF00834)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rpe-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rpe-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QS3
- **Protein Description:** RecName: Full=Ribulose-phosphate 3-epimerase {ECO:0000256|ARBA:ARBA00013188, ECO:0000256|HAMAP-Rule:MF_02227}; EC=5.1.3.1 {ECO:0000256|ARBA:ARBA00013188, ECO:0000256|HAMAP-Rule:MF_02227};
- **Gene Information:** Name=rpe {ECO:0000256|HAMAP-Rule:MF_02227, ECO:0000313|EMBL:AAN66045.2}; OrderedLocusNames=PP_0415 {ECO:0000313|EMBL:AAN66045.2};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ribulose-phosphate 3-epimerase family.
- **Key Domains:** Aldolase_TIM. (IPR013785); Ribul_P_3_epim. (IPR026019); Ribul_P_3_epim-like. (IPR000056); RibuloseP-bd_barrel. (IPR011060); Ribul_P_3_epim (PF00834)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rpe" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rpe' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rpe** (gene ID: rpe, UniProt: Q88QS3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *rpe* (Q88QS3, PP_0415) — D-Ribulose-5-Phosphate 3-Epimerase in *Pseudomonas putida* KT2440

## Summary

The gene **rpe** (locus tag **PP_0415**; UniProt accession **Q88QS3**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / KT2440) encodes **D-ribulose-5-phosphate 3-epimerase** (EC 5.1.3.1), a soluble, cytoplasmic enzyme of the ribulose-phosphate 3-epimerase family. Its primary and, so far as the evidence indicates, sole biochemical function is to catalyze the **reversible C3 epimerization of D-ribulose-5-phosphate to D-xylulose-5-phosphate**, the central interconversion of the non-oxidative branch of the pentose phosphate pathway (PPP). Gene-symbol identity, protein family, EC number, catalytic residues, and organism all cross-validate: this is an authentic, correctly annotated Rpe enzyme, and the research below concerns the intended target rather than a same-symbol gene from a different organism.

Structurally, Q88QS3 is a small (~224 amino acids, ~24 kDa) **(β/α)₈ TIM-barrel** protein carrying the conserved catalytic and metal-binding architecture of the family. Direct inspection of the sequence confirms the two catalytic aspartates (Asp36, the proton acceptor, and Asp177, the proton donor) and a divalent-metal-coordinating sphere (His34, Asp36, His68, Asp177) that is diagnostic of the ribulose-phosphate 3-epimerase active site. Its conserved serine (Ser9) corresponds to a residue whose mutation nearly abolishes activity in the human orthologue. Catalysis proceeds through a **divalent-metal-dependent, cis-enediolate intermediate** mechanism, consistent with the structurally solved plant, rice, and human enzymes of the same family.

Functionally, Rpe operates in the **cytoplasm** within the non-oxidative PPP. In *P. putida* KT2440 — an organism that lacks a functional Embden–Meyerhof–Parnas (EMP) glycolysis and catabolizes glucose principally through the Entner–Doudoroff route — the non-oxidative PPP reactions are embedded in the cyclic **EDEMP** metabolic architecture that recycles triose phosphates back to hexose phosphates and biases the cell toward NADPH overproduction. In this network, Rpe supplies the ribulose-5-P ⇌ xylulose-5-P interconversion required to route carbon between pentose phosphates and the rest of central metabolism, thereby underpinning the supply of biosynthetic precursors (ribose-5-P for nucleotides, erythrose-4-P for aromatic amino acids) and supporting the redox homeostasis that gives this bacterium its notable oxidative-stress tolerance. KEGG assigns PP_0415 to orthology **K01783** and the enzyme is the **single-copy, non-redundant** Rpe in the KT2440 genome.

---

## Gene/Protein Identity Verification

Before presenting the functional findings, the mandatory identity checks were completed and all four align:

| Verification step | Result |
|---|---|
| Gene symbol "rpe" matches protein description | ✅ Yes — *rpe* is the standard symbol for ribulose-phosphate 3-epimerase |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (PSEPK); locus PP_0415 |
| Protein family/domains align with literature | ✅ Aldolase_TIM (IPR013785), Ribul_P_3_epim (PF00834 / IPR026019), RibuloseP-bd_barrel (IPR011060) — all consistent with an authentic Rpe TIM-barrel |
| No conflicting same-symbol gene | ✅ Literature retrieved concerns bona fide ribulose-phosphate 3-epimerases; no ambiguity identified |

The symbol "rpe" is unambiguous here: it is used consistently across bacteria, plants, and humans for the same EC 5.1.3.1 activity, and the *P. putida* protein shares 75.9% identity with the experimentally validated *Escherichia coli* Rpe. This report therefore proceeds with full confidence in the target identity.

---

## Key Findings

### F001 — Rpe catalyzes the reversible interconversion of D-ribulose-5-phosphate and D-xylulose-5-phosphate (EC 5.1.3.1)

The primary function of Q88QS3 is to catalyze the **reversible epimerization at C3 of D-ribulose-5-phosphate to yield D-xylulose-5-phosphate**, the defining reaction of the ribulose-phosphate 3-epimerase family and EC number 5.1.3.1. This assignment rests on the enzyme's family membership (UniProt/HAMAP rule **MF_02227**) and is reinforced by biochemical and structural characterization of orthologues across the tree of life. The rice, potato-chloroplast, and human RPE enzymes have all been characterized as catalyzing precisely this reversible interconversion, and the general statement of the reaction is well established in the literature: *"Ribulose-5-phosphate 3-epimerase (EC 5.1.3.1) catalyzes the interconversion of ribulose-5-phosphate and xylulose-5-phosphate in the Calvin cycle and in the oxidative pentose phosphate pathway"* ([PMID: 10191144](https://pubmed.ncbi.nlm.nih.gov/10191144/)), and *"catalyzing the reversible conversion of D-ribulose 5-phosphate to D-xylulose 5-phosphate"* ([PMID: 20923965](https://pubmed.ncbi.nlm.nih.gov/20923965/)).

Crucially for functional inference, genetic evidence in the closely related *E. coli* enzyme demonstrates that this activity is both essential and non-redundant: *"Disruption of the gene (rpe) causes loss of enzymatic activity and renders the rpe mutant unable to utilize single pentose sugars, indicating that rpe supplies the only ribulose-5-phosphate epimerase activity in E. coli"* ([PMID: 9729441](https://pubmed.ncbi.nlm.nih.gov/9729441/)). Because Q88QS3 is 76% identical to that enzyme (see F005), this experimentally validated function and phenotype can be transferred to the *P. putida* protein with high confidence.

### F002 — The sequence carries the conserved TIM-barrel catalytic and metal-binding residues of an authentic Rpe

Q88QS3 is a 224-residue, ~24 kDa protein whose InterPro domain content (Aldolase_TIM, Ribul_P_3_epim/PF00834, RibuloseP-bd_barrel) predicts a **(β/α)₈ TIM-barrel** fold — the canonical scaffold of the family. This prediction is directly consistent with structural work on the family: *"The subunit chain fold is a (beta alpha)8-barrel"* ([PMID: 10191144](https://pubmed.ncbi.nlm.nih.gov/10191144/)).

UniProt/HAMAP feature annotation, corroborated by direct inspection of the sequence, places the two catalytic aspartates at **Asp36** (proton acceptor) and **Asp177** (proton donor), and a divalent-metal-coordinating sphere composed of **His34, Asp36, His68, and Asp177** (two histidines plus two aspartates) — the arrangement diagnostic of the family's active site. A conserved **Ser9** corresponds to human RPE Ser10, whose mutation nearly abolishes activity. These residue assignments are anchored to human RPE structural work: *"Two aspartic acids are well positioned to carry out the proton transfers in an acid-base type of reaction mechanism. Interestingly, mutating Ser-10 to alanine almost abolished the enzymatic activity"* ([PMID: 20923965](https://pubmed.ncbi.nlm.nih.gov/20923965/)). The presence of the intact catalytic machinery confirms that PP_0415 is a catalytically competent epimerase, not a degenerate or pseudo-enzyme.

### F003 — Catalysis is divalent-metal-dependent and proceeds via a cis-enediolate intermediate

Members of the ribulose-phosphate 3-epimerase family require a buried divalent metal ion and stabilize a **cis-enediolate reaction intermediate**. Human RPE uses an octahedrally coordinated Fe²⁺: *"we show that human D-ribulose 5-phosphate 3-epimerase (hRPE) uses Fe(2+) for catalysis"* ([PMID: 20923965](https://pubmed.ncbi.nlm.nih.gov/20923965/)). The rice cytosolic enzyme uses a Zn²⁺ site at the active center, with a mechanism explicitly invoking a stabilized intermediate: *"Assuming that the bound zinc ion is an integral part of the enzyme, a reaction mechanism involving a well-stabilized cis-enediolate intermediate is suggested"* ([PMID: 12547196](https://pubmed.ncbi.nlm.nih.gov/12547196/)). The potato-chloroplast enzyme likewise stabilizes the intermediate: *"the negative charge of the putative cis-ene-diolate intermediate is stabilized"* ([PMID: 10191144](https://pubmed.ncbi.nlm.nih.gov/10191144/)).

Because the metal-ligand set (2 His + 2 Asp: His34/Asp36/His68/Asp177) is conserved in Q88QS3, the *P. putida* enzyme is expected to operate by the same metal-dependent, cis-enediolate mechanism. The precise physiological metal for the *P. putida* enzyme has not been experimentally determined, but the family precedent (Fe²⁺ in human, Zn²⁺ in rice) indicates a divalent transition-metal ion.

### F004 — Rpe functions in the cytoplasm within the non-oxidative PPP, embedded in the EDEMP cycle, supporting NADPH/redox homeostasis and precursor supply

*P. putida* KT2440 has an unusual central-carbon metabolism. It lacks a functional EMP glycolysis and catabolizes glucose mainly through the Entner–Doudoroff route. ¹³C-flux analysis shows that roughly 10% of triose phosphates are recycled back to hexose phosphates through a cyclic architecture that merges Entner–Doudoroff, (gluconeogenic) EMP, and pentose-phosphate reactions — the **EDEMP cycle**: *"This set of reactions merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)"* ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). The default state of this cycle biases the cell toward NADPH generation: *"Cells growing on glucose thus run a biochemical cycle that favors NADPH formation"* ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)).

Rpe, a soluble cytoplasmic enzyme, provides the ribulose-5-P ⇌ xylulose-5-P interconversion that the non-oxidative PPP reactions of this network require. The physiological relevance of this NADPH-generating capacity is underscored by the observation that, under sub-lethal oxidative challenge, the network is reconfigured to boost NADPH supply: *"metabolic network-wide routes for NADPH generation-the metabolic currency that fuels redox-stress quenching mechanisms-were inspected when P. putida KT2440 was challenged with a sub-lethal H"* ([PMID: 33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/)). Thus, in situ, Rpe sits at a control node that channels carbon between pentose phosphates and the rest of central metabolism, supplying ribose-5-P for nucleotide biosynthesis, erythrose-4-P for aromatic amino-acid biosynthesis, and supporting the redox balance that underlies this bacterium's stress tolerance.

### F005 — Q88QS3 is a close orthologue of *E. coli* Rpe (75.9% identity), justifying transfer of experimental evidence

A Needleman–Wunsch global alignment of Q88QS3 (224 aa) against *E. coli* K-12 Rpe (P0AG07, 225 aa) gives **170/224 identical positions = 75.9% amino-acid identity**, with near-identical chain length. Against human RPE (Q96AT9, 228 aa) the identity is 42.3%. This high identity to the *E. coli* enzyme — whose deletion removes all cellular ribulose-5-P epimerase activity and blocks pentose utilization — provides a strong basis for transferring the experimentally established function and phenotype to the *P. putida* protein: *"Disruption of the gene (rpe) causes loss of enzymatic activity and renders the rpe mutant unable to utilize single pentose sugars, indicating that rpe supplies the only ribulose-5-phosphate epimerase activity in E. coli"* ([PMID: 9729441](https://pubmed.ncbi.nlm.nih.gov/9729441/)). The moderate but clear identity to human RPE, whose Fe²⁺/two-Asp mechanism is structurally solved, further supports the mechanistic assignment for the conserved Asp36/Asp177 pair: *"Two aspartic acids are well positioned to carry out the proton transfers in an acid-base type of reaction mechanism"* ([PMID: 20923965](https://pubmed.ncbi.nlm.nih.gov/20923965/)).

| Comparison | Length | Identity to Q88QS3 | Transferable evidence |
|---|---|---|---|
| *E. coli* K-12 Rpe (P0AG07) | 225 aa | **75.9%** | Sole R5P epimerase; essential for pentose use (genetic) |
| Human RPE (Q96AT9) | 228 aa | 42.3% | Fe²⁺ cofactor; two-Asp acid–base mechanism (structural) |
| *P. putida* Rpe (Q88QS3) | 224 aa | — | Target protein |

### F006 — KEGG assigns PP_0415 to K01783 in the non-oxidative PPP module; the gene is not part of a conserved PPP operon

The KEGG database entry **ppu:PP_0415** carries SYMBOL *rpe* and ORTHOLOGY **K01783** (ribulose-phosphate 3-epimerase, EC 5.1.3.1). It maps to pathway maps ppu00030 (Pentose phosphate pathway), ppu00040 (Pentose and glucuronate interconversions), and ppu00710 (Carbon fixation/Calvin cycle map), and to modules **M00004** (Pentose phosphate cycle) and **M00007** (non-oxidative phase, fructose-6P ⇒ ribose-5P). This independently corroborates the EC assignment and the pathway placement derived from sequence and family evidence.

The genomic neighborhood indicates that *P. putida rpe* is **not** organized in a conserved PPP operon. Its flanking genes are functionally unrelated: PP_0413/PP_0414 are polyamine (spermidine/putrescine) ABC-transporter permeases, PP_0416 is a phosphoglycolate phosphatase (K01091), and PP_0417 is anthranilate synthase component I (K01657). Unlike *E. coli*, where *rpe* sits within the *dam*-containing operon, the *P. putida* gene is flanked by unrelated genes, consistent with **monocistronic/independent (housekeeping) expression**.

### F007 — *rpe*/PP_0415 is the sole ribulose-5-phosphate 3-epimerase gene in the KT2440 genome (no paralogs)

A genome-wide KEGG cross-reference confirms non-redundancy: querying all KT2440 genes linked to orthology K01783 returns exactly one hit (ppu:PP_0415), and querying all genes linked to EC 5.1.3.1 also returns exactly one hit (ppu:PP_0415). No second Rpe paralog — for example, a Calvin-cycle *cbbE*-type epimerase — is annotated in the genome. This mirrors the situation in *E. coli*, where the gene *"supplies the only ribulose-5-phosphate epimerase activity"* ([PMID: 9729441](https://pubmed.ncbi.nlm.nih.gov/9729441/)), implying that PP_0415 is likely the single genetic source of this essential metabolic activity in *P. putida* and therefore a potentially indispensable housekeeping gene.

---

## Mechanistic Model / Interpretation

### The reaction and its place in metabolism

Rpe catalyzes a single, reversible epimerization at the C3 position of a five-carbon sugar phosphate:

```
        Rpe (EC 5.1.3.1), divalent metal ion
   D-ribulose-5-phosphate  <===============>  D-xylulose-5-phosphate
                            cis-enediolate intermediate
```

This is one of the two "entry/exit" reactions of the **non-oxidative pentose phosphate pathway**, working alongside ribose-5-phosphate isomerase (RpiA/RpiB), transketolase (Tkt), and transaldolase (Tal). Ribulose-5-P is produced by the oxidative branch of the PPP (from 6-phosphogluconate via Gnd); Rpe converts part of that pool to xylulose-5-P, which — together with ribose-5-P — feeds transketolase/transaldolase reactions that interconvert C3–C7 sugar phosphates. The net effect is a flexible carbon-shuffling hub linking hexose/triose phosphates to pentose phosphates.

```
   Glucose-6-P
       │  (oxidative PPP, Zwf/Pgl/Gnd → NADPH)
       ▼
   Ribulose-5-P ──Rpe──► Xylulose-5-P ┐
       │ (Rpi)                        │  Tkt / Tal
       ▼                              ▼
   Ribose-5-P ──────────────► (C3–C7 sugar-P interconversion)
       │                              │
       ▼                              ▼
 nucleotides                Fructose-6-P / GAP
 (biosynthesis)             ↺ recycled in EDEMP cycle
```

### Why this matters specifically in *P. putida* KT2440

In most model bacteria the non-oxidative PPP is a "side" pathway. In *P. putida* KT2440, however, the absence of a working EMP glycolysis makes the PPP reactions part of the central **EDEMP cycle**, a recycling architecture that runs the gluconeogenic EMP enzymes in reverse and folds PPP reactions into a loop that regenerates NADPH ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). Rpe is one of the enzymes that make this loop chemically possible, because interconverting ribulose-5-P and xylulose-5-P is required to feed the transketolase/transaldolase reactions that shuttle carbon back to fructose-6-P and glyceraldehyde-3-P. The physiological payoff is a high NADPH-generating capacity that this soil bacterium can further ramp up under oxidative stress ([PMID: 33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/)), a trait central to its robustness as an industrial chassis.

### Localization

All lines of evidence place Rpe in the **cytoplasm**. It is a small, soluble globular TIM-barrel enzyme with no signal peptide, transmembrane segment, or targeting motif, and its substrates (phosphorylated sugars) and partner enzymes are cytoplasmic. This is the location where central carbon metabolism, including the PPP, operates in bacteria.

### Substrate specificity

The enzyme's specificity is **narrow**: it acts on the D-ribulose-5-P / D-xylulose-5-P pair. It should be distinguished from the mechanistically related but distinct TIM-barrel epimerases of the L-ascorbate utilization pathway — e.g., UlaE (L-xylulose-5-phosphate 3-epimerase), which shares the TIM-barrel fold and a metal-dependent epimerization mechanism but acts on a different substrate ([PMID: 18849419](https://pubmed.ncbi.nlm.nih.gov/18849419/)). The conserved active-site residues and 76% identity to *E. coli* Rpe indicate that PP_0415 is a canonical D-ribulose-5-P 3-epimerase rather than one of these specialized relatives.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [10191144](https://pubmed.ncbi.nlm.nih.gov/10191144/) | *Structure and mechanism of D-ribulose-5-P 3-epimerase from potato chloroplasts* | Defines the reaction and EC 5.1.3.1; establishes the (β/α)₈ TIM-barrel fold; documents cis-enediolate stabilization (F001, F002, F003) |
| [20923965](https://pubmed.ncbi.nlm.nih.gov/20923965/) | *Human RPE: structural and biochemical studies* | States the reversible reaction; Fe²⁺ cofactor; two-Asp acid–base mechanism; essential conserved Ser (F001, F002, F003, F005) |
| [12547196](https://pubmed.ncbi.nlm.nih.gov/12547196/) | *Cytosolic RPE from rice: structure and mechanism* | Zn²⁺ cofactor and cis-enediolate mechanism (F003) |
| [9729441](https://pubmed.ncbi.nlm.nih.gov/9729441/) | *Impaired growth of an E. coli rpe mutant* | Genetic proof that rpe is the sole R5P epimerase and required for pentose utilization; transferable phenotype (F001, F005, F007) |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 EDEMP cycle* | Defines the cyclic ED/EMP/PPP architecture and its NADPH bias, the pathway context of Rpe (F004) |
| [33432138](https://pubmed.ncbi.nlm.nih.gov/33432138/) | *Metabolic flux reconfiguration under oxidative stress in P. putida* | Shows PPP/NADPH network is reconfigured for redox-stress defense (F004) |
| [18849419](https://pubmed.ncbi.nlm.nih.gov/18849419/) | *UlaE (L-xylulose-5-P 3-epimerase) structure* | Distinguishes the narrow substrate specificity of Rpe from related TIM-barrel epimerases (interpretation) |

**Strength of evidence.** The functional assignment for Q88QS3 rests on a robust, convergent chain: (1) an authoritative family/EC assignment (HAMAP MF_02227, KEGG K01783); (2) direct sequence evidence for the intact catalytic machinery; (3) very high (76%) identity to a *genetically validated* bacterial orthologue; and (4) structurally solved mechanisms for multiple family members. The main gap is that no study has *directly* purified or assayed the *P. putida* PP_0415 protein itself — the functional claims are inferences (albeit strong ones) from orthology and family membership, not direct experimental characterization of this specific protein.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of PP_0415.** There is, to our knowledge, no published purification, kinetic assay (kcat/Km), or crystal structure of the *P. putida* KT2440 Rpe itself. All enzymatic claims are inferred from orthologues (chiefly *E. coli*, plus structural data from human, rice, and potato enzymes).

2. **Metal cofactor not experimentally identified for this protein.** Family members use Fe²⁺ (human) or Zn²⁺ (rice/plant). The specific physiological metal of the *P. putida* enzyme is inferred, not measured.

3. **Essentiality not directly tested in *P. putida*.** The single-copy, non-redundant status (F007) and the *E. coli* deletion phenotype (F005) strongly suggest that *rpe* is essential or important for pentose metabolism in KT2440, but a targeted knockout/growth study in this organism has not been reviewed here.

4. **Catalytic residue numbering rests on annotation + sequence inspection.** Asp36/Asp177 and the metal-binding His/Asp set are assigned from HAMAP features and alignment to characterized homologs, not from an experimental structure of Q88QS3.

5. **Regulation and expression are largely uncharacterized.** The gene appears monocistronic (F006), but its promoter, expression level, and any condition-dependent regulation (e.g., during oxidative stress or growth on pentoses) have not been directly established for this locus.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzymatic assay.** Clone PP_0415, purify the His-tagged protein, and measure ribulose-5-P ⇌ xylulose-5-P epimerase activity, determining kcat, Km, and the divalent-metal requirement (test Fe²⁺, Zn²⁺, Mn²⁺, Co²⁺) to confirm the inferred mechanism and cofactor.

2. **Gene deletion / complementation in KT2440.** Construct a clean Δ*rpe* mutant and test growth on glucose, gluconate, and pentose sugars; complement with the wild-type gene. This would directly establish essentiality and the metabolic role predicted from the *E. coli* orthologue.

3. **Site-directed mutagenesis of Asp36 and Asp177.** Mutate each catalytic aspartate (and Ser9) to alanine and assay residual activity to confirm the acid–base mechanism and the residue assignments transferred from human RPE.

4. **Structural determination.** Solve the crystal or cryo-EM structure of the *P. putida* enzyme (ideally with bound substrate/intermediate analog and metal) to verify the TIM-barrel fold, active-site geometry, and metal coordination.

5. **¹³C-flux analysis in Δ*rpe* / *rpe*-overexpression backgrounds.** Quantify how modulating Rpe activity perturbs the EDEMP cycle, NADPH yield, and oxidative-stress tolerance, directly linking this enzyme to the physiological phenotypes of interest.

6. **Expression profiling under oxidative stress.** Measure *rpe* transcript/protein levels during sub-lethal H₂O₂ challenge to test whether the enzyme is part of the NADPH-boosting reconfiguration observed for the broader network.

---

## Conclusion

*rpe* (Q88QS3, PP_0415) in *Pseudomonas putida* KT2440 encodes **D-ribulose-5-phosphate 3-epimerase (EC 5.1.3.1)**, a ~24 kDa cytoplasmic TIM-barrel enzyme that catalyzes the reversible C3 epimerization of D-ribulose-5-phosphate to D-xylulose-5-phosphate via a divalent-metal-dependent, cis-enediolate mechanism using two catalytic aspartates (Asp36/Asp177). It is the sole, non-redundant such epimerase in the genome and operates in the non-oxidative branch of the pentose phosphate pathway — embedded in this organism's cyclic EDEMP glucose-catabolism architecture — supplying sugar-phosphate precursors (ribose-5-P, erythrose-4-P) and supporting the NADPH/redox balance that underlies *P. putida*'s oxidative-stress tolerance. The functional assignment is strongly supported by family/EC annotation, conserved catalytic residues, 76% identity to the genetically validated *E. coli* enzyme, and structurally solved family mechanisms, though direct biochemical characterization of the *P. putida* protein itself remains to be performed.


## Artifacts

- [OpenScientist final report](rpe-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rpe-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10191144
2. PMID:20923965
3. PMID:9729441
4. PMID:12547196
5. PMID:26350459
6. PMID:33432138
7. PMID:18849419