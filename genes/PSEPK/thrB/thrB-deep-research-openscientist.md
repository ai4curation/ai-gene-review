---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T10:38:26.257611'
end_time: '2026-08-11T11:00:14.001079'
duration_seconds: 1307.74
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: thrB
  gene_symbol: thrB
  uniprot_accession: Q88RK8
  protein_description: 'RecName: Full=Homoserine kinase {ECO:0000256|HAMAP-Rule:MF_00301,
    ECO:0000256|NCBIfam:TIGR00938}; Short=HK {ECO:0000256|HAMAP-Rule:MF_00301}; Short=HSK
    {ECO:0000256|HAMAP-Rule:MF_00301}; EC=2.7.1.39 {ECO:0000256|HAMAP-Rule:MF_00301,
    ECO:0000256|NCBIfam:TIGR00938};'
  gene_info: Name=thrB {ECO:0000256|HAMAP-Rule:MF_00301, ECO:0000313|EMBL:AAN65755.1};
    OrderedLocusNames=PP_0121 {ECO:0000313|EMBL:AAN65755.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the pseudomonas-type ThrB family.
  protein_domains: Aminoglycoside_PTrfase. (IPR002575); Homoserine_kinase_II. (IPR005280);
    Kinase-like_dom_sf. (IPR011009); Pseudomonas-type_ThrB. (IPR050249); APH (PF01636)
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
  path: thrB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: thrB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RK8
- **Protein Description:** RecName: Full=Homoserine kinase {ECO:0000256|HAMAP-Rule:MF_00301, ECO:0000256|NCBIfam:TIGR00938}; Short=HK {ECO:0000256|HAMAP-Rule:MF_00301}; Short=HSK {ECO:0000256|HAMAP-Rule:MF_00301}; EC=2.7.1.39 {ECO:0000256|HAMAP-Rule:MF_00301, ECO:0000256|NCBIfam:TIGR00938};
- **Gene Information:** Name=thrB {ECO:0000256|HAMAP-Rule:MF_00301, ECO:0000313|EMBL:AAN65755.1}; OrderedLocusNames=PP_0121 {ECO:0000313|EMBL:AAN65755.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the pseudomonas-type ThrB family.
- **Key Domains:** Aminoglycoside_PTrfase. (IPR002575); Homoserine_kinase_II. (IPR005280); Kinase-like_dom_sf. (IPR011009); Pseudomonas-type_ThrB. (IPR050249); APH (PF01636)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "thrB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'thrB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **thrB** (gene ID: thrB, UniProt: Q88RK8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *thrB* (Homoserine Kinase, Q88RK8) in *Pseudomonas putida* KT2440

**Gene:** *thrB* · **Ordered locus:** PP_0121 · **UniProt:** Q88RK8 · **EC:** 2.7.1.39
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), abbreviated PSEPK

---

## Summary

**thrB (PP_0121; UniProt Q88RK8) of *Pseudomonas putida* KT2440 encodes homoserine kinase (HK/HSK; EC 2.7.1.39), a soluble cytoplasmic enzyme that catalyzes the ATP-dependent phosphorylation of L-homoserine to O-phospho-L-homoserine (OPHS), the fourth of five steps in the aspartate-derived L-threonine biosynthetic pathway.** The product, O-phospho-L-homoserine, is the committed substrate handed to threonine synthase (ThrC) for the final conversion to L-threonine. The enzyme is strictly specific for L-homoserine, consistent with the broader HSK enzyme class. This assignment is anchored in the UniProt/KEGG catalytic annotation (RHEA:13985; K02204 "homoserine kinase type II") and is supported by direct experimental work in the close relative *Pseudomonas aeruginosa*, where *thrB* was cloned, sequenced, and shown to encode homoserine kinase activity.

A distinctive feature of the Pseudomonas ThrB is that it is **not** a member of the canonical GHMP-kinase family that includes *Escherichia coli* ThrB. Instead, it belongs to a structurally distinct "type II" homoserine kinase family within the protein-kinase-like / aminoglycoside-phosphotransferase (APH) superfamily. This is reflected in its domain architecture (Pfam PF01636 "APH"; InterPro IPR005280 "Homoserine kinase II, prokaryotic type"; IPR011009 "Protein kinase-like domain superfamily"; family IPR050249 "Pseudomonas-type ThrB") and was established experimentally when the *P. aeruginosa* ThrB product was found to share no sequence similarity with other known ThrB proteins. Two structurally unrelated enzyme folds thus converge on the same phosphotransfer chemistry.

A second key biological feature is **functional redundancy**. In Pseudomonas, inactivation of *thrB* alone produces no detectable growth phenotype because a second, isozymic homoserine-kinase activity — encoded by *thrH* — can supply O-phospho-L-homoserine. Threonine auxotrophy is observed only when *thrB* and *thrH* are simultaneously disrupted. ThrH is additionally a bifunctional enzyme with in vivo phosphoserine phosphatase (SerB-like) activity. This redundancy explains why *thrB* behaves as a dispensable, conditionally essential gene in genome-wide screens of *P. putida* KT2440. The enzyme acts entirely in the cytoplasm; sequence analysis reveals no signal peptide and no transmembrane segments, consistent with threonine biosynthesis being a cytosolic process.

---

## Gene/Protein Identity Verification

The mandatory identity checks were completed and **all confirm the correct target**:

| Check | Result |
|---|---|
| Gene symbol matches protein description | ✅ *thrB* = homoserine kinase (EC 2.7.1.39), consistent with UniProt RecName |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (PSEPK); KEGG locus ppu:PP_0121 |
| Protein family/domains align with literature | ✅ APH/protein-kinase-like "type II" ThrB family (IPR050249, IPR005280, PF01636) |
| Literature matches this gene/function | ✅ Direct experimental characterization of Pseudomonas *thrB* as homoserine kinase [PMID: 1333566] |

The gene symbol *thrB* is unambiguous here: it denotes homoserine kinase across bacteria, and the Pseudomonas-specific literature (both *P. aeruginosa* and *P. putida*) is directly applicable. No conflicting gene with the same symbol was encountered.

---

## Key Findings

### F001 — ThrB is a homoserine kinase catalyzing step 4 of threonine biosynthesis

ThrB (Q88RK8, PP_0121) catalyzes the ATP-dependent phosphorylation of L-homoserine, producing O-phospho-L-homoserine, ADP, and a proton:

```
L-homoserine + ATP  →  O-phospho-L-homoserine + ADP + H⁺      (EC 2.7.1.39; RHEA:13985)
```

This is annotated in UniProt Q88RK8 as pathway step "L-threonine from L-aspartate: step 4 of 5," and the gene is catalogued in KEGG as ppu:PP_0121. The functional assignment is not merely computational: in the closely related organism *P. aeruginosa*, the *thrB* gene was physically cloned and sequenced and shown to encode homoserine kinase activity. The definitive statement from that work is that "*three genes from Pseudomonas aeruginosa involved in threonine biosynthesis, hom, thrB and thrC, encoding homoserine dehydrogenase (HDH), homoserine kinase (HK) and threonine synthase (TS), respectively, have been cloned and sequenced*" [PMID: 1333566]. Because the *P. putida* ThrB is the direct ortholog of the *P. aeruginosa* enzyme, this experimental evidence establishes the same gene/function for Q88RK8.

The reaction sits within the aspartate-derived amino acid pathway. Homoserine dehydrogenase (Hom) produces L-homoserine; ThrB phosphorylates it; and threonine synthase (ThrC) then completes threonine synthesis from the O-phospho-L-homoserine product.

### F002 — Pseudomonas ThrB is a structurally distinct "type II" homoserine kinase (APH/protein-kinase-like superfamily)

Unlike *E. coli* ThrB, which is a GHMP-family kinase, the Pseudomonas ThrB belongs to a completely separate structural lineage. The InterPro/Pfam annotation of Q88RK8 comprises Pfam **PF01636 (APH, aminoglycoside phosphotransferase)**, **IPR005280 "Homoserine kinase II (prokaryotic type)"**, **IPR011009 "Protein kinase-like domain superfamily"**, **IPR002575 "Aminoglycoside phosphotransferase"**, and family **IPR050249 "Pseudomonas-type ThrB."** These place the enzyme firmly in the protein-kinase-like (ePK/APH) fold rather than the GHMP fold.

The experimental basis for this distinction is decisive: the *P. aeruginosa* ThrB "*product of this gene does not share any similarity with other known ThrB proteins*" [PMID: 1333566]. This sequence-level orphan status is exactly what is expected for a "type II" homoserine kinase that reached the same catalytic outcome through convergent evolution. As a general principle for the enzymes of this pathway, "*although these kinases bind similar substrates and catalyze analogous phosphotransfer chemistry, they do not show high amino acid sequence homology*" [PMID: 14759741]. Two structurally unrelated enzyme families independently solved the problem of phosphorylating homoserine, each forming an enzyme–ATP–amino acid ternary complex to carry out the phosphotransfer.

| Feature | *E. coli* ThrB (type I) | Pseudomonas ThrB (type II; Q88RK8) |
|---|---|---|
| Structural fold | GHMP kinase | Protein-kinase-like / APH superfamily |
| Pfam / InterPro | GHMP domain | PF01636 (APH); IPR005280; IPR011009; IPR050249 |
| Sequence homology to the other type | None | None |
| KEGG orthology | K00872 (type I) | **K02204 (type II)** |
| Reaction catalyzed | L-homoserine + ATP → OPHS + ADP | Identical (EC 2.7.1.39) |

### F003 — thrB is functionally redundant with the isozyme ThrH; loss of thrB alone does not cause threonine auxotrophy

A hallmark of the Pseudomonas threonine pathway is redundancy at the homoserine-kinase step. In *P. aeruginosa*, "*no phenotype could be detected when the chromosomal thrB gene was inactivated by an insertion. Therefore the existence of isozymes for this activity is postulated*" [PMID: 1333566]. The postulated isozyme was subsequently identified as **ThrH**: "*in P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated*" [PMID: 10220164]. ThrH is a bifunctional enzyme that also carries in vivo phosphoserine phosphatase (SerB-like) activity, linking threonine and serine metabolism.

This redundancy is consistent with the behavior of *thrB* in *P. putida* KT2440. A genome-wide mini-Tn5 mutant screen for conditionally essential genes recovered threonine auxotrophs among the amino-acid-biosynthesis mutants under minimal-medium growth conditions [PMID: 20158506], demonstrating that the pathway as a whole is required for prototrophy, while single-gene redundancy at the HK step buffers loss of *thrB* individually. In practical terms, *thrB* is dispensable on its own but the combined HK activity (ThrB + ThrH) is essential for threonine synthesis in the absence of exogenous threonine.

### F004 — Substrate specificity: strictly L-homoserine; product feeds threonine (and, in some organisms, methionine)

Homoserine kinases are strictly specific for L-homoserine. Purified recombinant homoserine kinase "*specifically phosphorylates L-homoserine and displays kinetic properties similar to other HSKs*" [PMID: 25367138], and this substrate specificity is a defining property of the enzyme class that applies to ThrB. The product, O-phospho-L-homoserine, is a metabolic branch point: "*the availability of the carbon backbone O-phosphohomoserine (OPHS) is critical to methionine (met) and threonine (thr) synthesis. OPHS derives from homoserine and is formed by homoserine kinase (HSK)*" [PMID: 17624493]. In *P. putida*, the principal downstream fate is threonine synthesis via threonine synthase (ThrC); methionine in Pseudomonas is generated from *O*-succinyl-homoserine, so ThrB flux is directed toward threonine. The UniProt catalytic activity for Q88RK8 is consistent with this: L-homoserine + ATP = O-phospho-L-homoserine + ADP + H⁺.

### F005 — ThrB is a soluble cytoplasmic enzyme with an APH/protein-kinase-like catalytic domain bearing the conserved HxDxxxxN motif

Sequence analysis of the 316-amino-acid Q88RK8 protein indicates a soluble cytoplasmic localization: there is **no signal peptide** and **zero predicted transmembrane segments** (Kyte–Doolittle hydropathy, window 19, maximum 1.12 — well below the ~1.6 threshold for membrane helices). UniProt annotates a single "Aminoglycoside phosphotransferase" catalytic domain spanning residues **27–255**. The domain contains the conserved catalytic-loop motif **HxDxxxxN** ("HADLFRDN"; His189 / Asp191 / Asn196) that is characteristic of the protein-kinase-like/APH superfamily — the Asp of the HxD acts as the catalytic base and the Asn coordinates the divalent metal (Mg²⁺) that positions the ATP phosphates. Because threonine biosynthesis is a cytosolic process and no targeting/localization signal is present, ThrB carries out its reaction in the cytoplasm. No experimental subcellular-fractionation study specific to *P. putida* ThrB was located; the cytoplasmic assignment rests on strong bioinformatic inference plus the universal cytosolic character of this pathway.

### F006 — KEGG confirms type II homoserine kinase (K02204); thrB is a standalone locus, not co-transcribed with other thr genes

KEGG independently corroborates the type II assignment: ppu:PP_0121 has ORTHOLOGY **K02204 "homoserine kinase type II [EC:2.7.1.39]"** and maps to pathways **ppu00260 (glycine, serine and threonine metabolism)** and **ppu01230 (biosynthesis of amino acids)**. The listed Pfam motifs (APH, TCAD9, Choline_kinase) all belong to the protein-kinase-like/APH superfamily.

Genomically, *thrB* occupies complement(126140..127090), a 951-bp ORF (316 aa). Its flanking genes are **PP_0119 (Zur, zinc uptake regulator)**, **PP_0120 (zinc ABC transporter)**, **PP_0122 (exported protein of unknown function)**, and **PP_0123 (DNA polymerase I, polA)** — none of which belong to the threonine pathway. This indicates that *thrB* is an isolated, likely monocistronic locus that is physically separated from the other threonine genes (*hom*, *thrC*). This dispersed organization is characteristic of Pseudomonas threonine genes and contrasts with the classical *thrABC* operon of *E. coli*.

---

## Mechanistic Model / Interpretation

### Position in the pathway

ThrB catalyzes the fourth committed step of the aspartate → threonine pathway. The full route and ThrB's place within it:

```
                aspartokinase        ASADH            homoserine
                (LysC/ThrA)          (Asd)            dehydrogenase (Hom)
   L-aspartate ───────────► L-aspartyl-P ──► L-aspartate ──► L-homoserine
        (1)                    (2)          semialdehyde (3)      │
                                                                  │  ThrB / ThrH
                                                                  │  (homoserine kinase, EC 2.7.1.39)
                                                                  │  ATP → ADP
                                                                  ▼
                                                        O-phospho-L-homoserine  ─────┐
                                                                  │  threonine       │ (branch point)
                                                                  │  synthase (ThrC) │
                                                                  ▼                  ▼
                                                            L-threonine     (methionine synthesis
                                                              (step 5)       in plants/some microbes)
                                                                  │
                                                                  │  threonine dehydratase (IlvA)
                                                                  ▼
                                                            2-oxobutanoate → L-isoleucine
```

### The two defining features: convergent structure + isozymic redundancy

Two ideas unify the findings. First, **convergent enzyme evolution**: the Pseudomonas ThrB reaches the canonical homoserine-kinase reaction using an entirely different protein scaffold (protein-kinase-like/APH fold) from the GHMP-family ThrB of *E. coli*. The catalytic machinery (HxDxxxxN motif, Mg-ATP binding) mirrors that of eukaryotic protein kinases and aminoglycoside phosphotransferases rather than GHMP kinases, yet the net chemistry — transfer of the ATP γ-phosphate to the γ-hydroxyl of L-homoserine — is identical.

Second, **metabolic robustness through redundancy**: the HK step is guarded by two isozymes (ThrB and ThrH). Deleting either alone is silent; only the double mutant is auxotrophic. ThrH additionally moonlights as a phosphoserine phosphatase, tying the threonine and serine branches together. This redundancy makes *thrB* a "conditionally essential/dispensable" gene — important physiologically but individually deletable, exactly as observed in high-throughput *P. putida* essentiality screens.

Downstream, the threonine produced is itself the precursor of L-isoleucine (via IlvA-catalyzed conversion of threonine to 2-oxobutanoate), so ThrB indirectly supports both protein synthesis and branched-chain amino-acid biosynthesis.

| Property | Value / evidence |
|---|---|
| Reaction | L-homoserine + ATP → O-phospho-L-homoserine + ADP + H⁺ (EC 2.7.1.39, RHEA:13985) |
| Substrate specificity | Strictly L-homoserine; ATP phosphoryl donor |
| Product fate | Substrate for threonine synthase (ThrC); branch-point precursor for Met in some taxa |
| Cofactor | ATP, Mg²⁺ (via HxDxxxxN metal coordination) |
| Structural family | Type II HK; protein-kinase-like / APH superfamily (PF01636; IPR050249) |
| Catalytic domain | Residues 27–255; motif HADLFRDN (His189/Asp191/Asn196) |
| Localization | Cytoplasm (no signal peptide, 0 TM segments) |
| Redundancy | Isozyme ThrH; double mutant required for auxotrophy |
| Gene organization | Standalone monocistronic locus (PP_0121); not in a thr operon |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [PMID: 1333566](https://pubmed.ncbi.nlm.nih.gov/1333566/) | *Isolation, organization and expression of the Pseudomonas aeruginosa threonine genes* | Primary experimental cloning/sequencing showing Pseudomonas *thrB* encodes homoserine kinase; ThrB product unlike other ThrBs; single-mutant has no phenotype → isozymes postulated. Supports F001, F002, F003. |
| [PMID: 10220164](https://pubmed.ncbi.nlm.nih.gov/10220164/) | *ThrH, a homoserine kinase isozyme with in vivo phosphoserine phosphatase activity in P. aeruginosa* | Identifies ThrH as the redundant HK isozyme; double *thrB thrH* mutant required for threonine auxotrophy. Supports F003. |
| [PMID: 14759741](https://pubmed.ncbi.nlm.nih.gov/14759741/) | *Small molecule functional discrimination of the kinases required for microbial synthesis of threonine and isoleucine* | Establishes that homoserine kinases of distinct families converge on analogous phosphotransfer chemistry without sequence homology. Supports F002. |
| [PMID: 25367138](https://pubmed.ncbi.nlm.nih.gov/25367138/) | *Homoserine and QS acyl-homoserine lactones as alternative sources of threonine ... homoserine kinase in T. brucei* | Purified recombinant HSK specifically phosphorylates L-homoserine with typical HSK kinetics. Supports F004. |
| [PMID: 17624493](https://pubmed.ncbi.nlm.nih.gov/17624493/) | *Regulation of aspartate-derived amino acid homeostasis in potato by E. coli homoserine kinase* | Defines OPHS as the HSK product and branch-point precursor for Thr/Met. Supports F004. |
| [PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | *Identification of conditionally essential genes in P. putida KT2440* | Genome-wide screen recovers threonine auxotrophs; contextualizes *thrB* as part of a conditionally essential pathway. Supports F003. |
| [PMID: 15133108](https://pubmed.ncbi.nlm.nih.gov/15133108/) | *Homoserine/threonine intermediates as precursors for AVG in Streptomyces* | Independent confirmation that *thrB* disruption blocks HK activity, reinforcing the *thrB* = HK assignment and homoserine branch point. Supports F001, F004. |
| [PMID: 25301583](https://pubmed.ncbi.nlm.nih.gov/25301583/) | *Channelling L-isoleucine synthesis in C. glutamicum* | Documents threonine → isoleucine flux via IlvA, contextualizing the downstream role of ThrB's pathway. Contextual. |

Supporting/contextual literature also reviewed: fungal *thr1Δ* homoserine kinase mutants attenuated in virulence [PMID: 20305003] (illustrating HSK essentiality where redundancy is absent), *G. sulfurreducens* alternate isoleucine biosynthesis [PMID: 18245290], and multiple industrial threonine/isoleucine engineering studies that express *thrB* as part of *thrABC* modules [PMID: 32315761, PMID: 39383016], underscoring the pathway role of homoserine kinase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88RK8 itself.** The catalytic assignment for the *P. putida* protein rests on (i) UniProt/KEGG annotation, (ii) orthology to the experimentally characterized *P. aeruginosa* ThrB [PMID: 1333566], and (iii) general HSK enzymology [PMID: 25367138, PMID: 17624493]. No purified-enzyme kinetics (Km, kcat, metal dependence) have been reported specifically for PP_0121.

2. **No experimental structure.** The APH/protein-kinase-like fold and the HxDxxxxN catalytic motif are inferred from sequence/domain annotation. An experimental or AlphaFold structure would confirm the active-site architecture and the catalytic residues (His189/Asp191/Asn196).

3. **ThrH redundancy demonstrated in *P. aeruginosa*, not directly in *P. putida*.** The *thrB*/*thrH* redundancy is best documented in *P. aeruginosa* [PMID: 10220164]. While *P. putida* is expected to share this architecture, a *P. putida*-specific double-mutant experiment has not been cited here.

4. **Regulation is uncharacterized.** Whether *thrB* expression responds to threonine/isoleucine feedback, and how the standalone locus (flanked by zinc-homeostasis and *polA* genes) is transcriptionally controlled, remains unknown. The genomic neighborhood provides no operonic clue.

5. **Substrate specificity limits.** L-homoserine specificity is inferred from the HSK class rather than measured for this ortholog; possible activity toward homoserine analogs has not been tested.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzyme characterization.** Overexpress and purify PP_0121, and measure steady-state kinetics (Km for L-homoserine and ATP, kcat, Mg²⁺ dependence, pH optimum). Confirm strict L-homoserine specificity by testing D-homoserine, L-serine, and homoserine analogs.

2. **Structural determination.** Solve the crystal/cryo-EM structure (or validate an AlphaFold model) of ThrB±AMP-PNP±L-homoserine to confirm the protein-kinase-like fold and the roles of His189/Asp191/Asn196 in metal coordination and catalysis.

3. **Genetic redundancy test in *P. putida*.** Construct single (ΔPP_0121) and double (Δ*thrB* Δ*thrH*) mutants in KT2440 and assay threonine prototrophy on minimal medium to directly confirm the ThrB/ThrH redundancy in this organism.

4. **Site-directed mutagenesis.** Mutate the HxDxxxxN motif residues (e.g., D191A, N196A) and assess loss of kinase activity to validate the predicted catalytic mechanism.

5. **Regulatory/transcriptional mapping.** Use RNA-seq/reporter assays to determine whether *thrB* is monocistronic and whether its expression is modulated by threonine, isoleucine, or the neighboring zinc-homeostasis regulon.

6. **Metabolic flux/complementation.** Test whether *P. putida thrB* complements an *E. coli thrB* mutant, confirming functional interchangeability across the two structural HK families despite the absence of sequence homology.

---

## Supported and Refuted Hypotheses

**Supported:**
- ThrB is a homoserine kinase (EC 2.7.1.39) catalyzing L-homoserine → O-phospho-L-homoserine [UniProt; PMID: 1333566].
- The enzyme is L-homoserine/ATP specific and operates via an enzyme·ATP·substrate ternary complex [PMID: 25367138, 14759741].
- ThrB is a "type II" homoserine kinase of the protein-kinase-like/APH superfamily, evolutionarily distinct from GHMP ThrB [Pfam/InterPro; PMID: 1333566].
- ThrB is cytoplasmic (no signal peptide/TM; sequence analysis).
- ThrB is functionally redundant with ThrH in Pseudomonas [PMID: 1333566, 10220164].

**Refuted / not supported:**
- That single *thrB* deletion causes threonine auxotrophy in Pseudomonas (refuted; requires *thrB* + *thrH* double loss [PMID: 1333566, 10220164]).
- That Pseudomonas ThrB is homologous to the *E. coli* GHMP-family homoserine kinase (refuted by sequence non-similarity and APH domain assignment).


## Artifacts

- [OpenScientist final report](thrB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](thrB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:1333566
2. PMID:14759741
3. PMID:10220164
4. PMID:20158506
5. PMID:25367138
6. PMID:17624493
7. PMID:15133108
8. PMID:25301583
9. PMID:20305003
10. PMID:18245290
11. PMID:32315761
12. PMID:39383016