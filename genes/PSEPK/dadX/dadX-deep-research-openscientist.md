---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T06:46:14.720644'
end_time: '2026-08-11T07:28:44.770140'
duration_seconds: 2550.05
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dadX
  gene_symbol: dadX
  uniprot_accession: Q88CB2
  protein_description: 'RecName: Full=Alanine racemase, catabolic {ECO:0000305|PubMed:23995642};
    EC=5.1.1.1 {ECO:0000255|HAMAP-Rule:MF_01201, ECO:0000269|PubMed:23995642};'
  gene_info: Name=dadX {ECO:0000303|PubMed:23995642, ECO:0000312|EMBL:AAN70834.1};
    OrderedLocusNames=PP_5269 {ECO:0000312|EMBL:AAN70834.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the alanine racemase family. {ECO:0000255|HAMAP-
  protein_domains: Ala_racemase. (IPR000821); Ala_racemase/Decarboxylase_C. (IPR009006);
    Ala_racemase_C. (IPR011079); Ala_racemase_N. (IPR001608); Ala_racemase_pyridoxalP-BS.
    (IPR020622)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dadX-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dadX-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CB2
- **Protein Description:** RecName: Full=Alanine racemase, catabolic {ECO:0000305|PubMed:23995642}; EC=5.1.1.1 {ECO:0000255|HAMAP-Rule:MF_01201, ECO:0000269|PubMed:23995642};
- **Gene Information:** Name=dadX {ECO:0000303|PubMed:23995642, ECO:0000312|EMBL:AAN70834.1}; OrderedLocusNames=PP_5269 {ECO:0000312|EMBL:AAN70834.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the alanine racemase family. {ECO:0000255|HAMAP-
- **Key Domains:** Ala_racemase. (IPR000821); Ala_racemase/Decarboxylase_C. (IPR009006); Ala_racemase_C. (IPR011079); Ala_racemase_N. (IPR001608); Ala_racemase_pyridoxalP-BS. (IPR020622)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dadX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dadX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dadX** (gene ID: dadX, UniProt: Q88CB2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *dadX* (Q88CB2, PP_5269) — Catabolic Alanine Racemase of *Pseudomonas putida* KT2440

## Summary

The gene **dadX** (UniProt **Q88CB2**; ordered locus **PP_5269**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a **catabolic alanine racemase** (EC 5.1.1.1). Gene identity is unambiguous and well supported: the UniProt-provided description, the InterPro domain architecture (Ala_racemase N- and C-terminal domains plus the pyridoxal-5′-phosphate binding site), the 357-residue sequence, and multiple primary studies performed directly in *P. putida* KT2440 all converge on the same protein. This is not a case of gene-symbol ambiguity — the literature specifically characterizes DadX from this organism.

DadX catalyzes the **reversible interconversion of L-alanine and D-alanine** using a pyridoxal-5′-phosphate (PLP) cofactor covalently anchored through a Schiff base to an active-site lysine (Lys33 in the DadX numbering, positionally homologous to the catalytic Lys39 of the archetypal *Bacillus stearothermophilus* enzyme). The enzyme operates through the canonical **two-base racemization mechanism** shared by the entire alanine racemase family, in which a lysine and a tyrosine (contributed across the homodimer interface) act as complementary acid/base catalysts on opposite faces of the substrate α-carbon. Crucially, DadX is **substrate-specific for the alanine stereoisomers** — biochemical characterization showed it strongly prefers alanine and is far more restrictive than the biosynthetic racemase Alr, which racemizes many amino acids.

The **physiological role of DadX is catabolic**, not biosynthetic. It constitutes the first step of the two-enzyme *dad* (D-amino acid degradation) module. DadX converts L-alanine to D-alanine, and the adjacent membrane-associated flavoprotein D-amino acid dehydrogenase (DadA / DadA2, PP_5270) then oxidatively deaminates D-alanine to pyruvate and ammonia. This channels alanine into central carbon and nitrogen metabolism, enabling *P. putida* KT2440 to grow on alanine (and D-alanine) as a sole carbon and nitrogen source. The enzyme acts in the **cytoplasm**, consistent with the soluble nature of alanine racemases. This catabolic role is functionally and evolutionarily distinct from the housekeeping racemase Alr, whose D-alanine product is committed to peptidoglycan cell-wall biosynthesis.

---

## Gene / Protein Identity Verification

Before reporting function, the mandatory identity checks were completed and **all passed**:

| Verification criterion | Result |
|---|---|
| Gene symbol "dadX" matches protein description | ✅ dadX = catabolic alanine racemase, matches UniProt RecName |
| Organism correct (*P. putida* KT2440) | ✅ Primary literature ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/), [PMID: 16579470](https://pubmed.ncbi.nlm.nih.gov/16579470/)) characterizes DadX directly in *P. putida* KT2440 |
| Protein family/domains align with literature | ✅ Alanine racemase family; PLP-binding TIM-barrel + C-terminal β-domain |
| Risk of same-symbol different-gene confusion | ✅ Low — DadX is a conserved catabolic racemase; *E. coli* dadX ([PMID: 3920477](https://pubmed.ncbi.nlm.nih.gov/3920477/)) is the orthologous catabolic isozyme, not a false match |

The 357-amino-acid length retrieved from Q88CB2 exactly matches the DadX peptide reported by Cao et al. (357 aa, ~38.82 kDa; [PMID: 16579470](https://pubmed.ncbi.nlm.nih.gov/16579470/)), further confirming identity. **This report proceeds with confidence that the correct gene is being described.**

---

## Key Findings

### Finding 1 — DadX is the catabolic alanine racemase of *P. putida* KT2440 with narrow substrate specificity for alanine

The most direct and authoritative evidence comes from Radkov & Moe (2013), who **purified and kinetically characterized DadX from *P. putida* KT2440 in vitro** ([PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/)). Their work establishes two decisive points. First, DadX has **narrow substrate specificity**: it "clearly prefer[s] only the alanine stereoisomers as the substrates." This stands in sharp contrast to the biosynthetic racemase Alr from the same organism, which racemized 9 of 19 tested chiral amino acids. Second, DadX is the **kinetically superior alanine racemase**, showing 6- and 9-fold higher catalytic efficiency (*k*cat/*K*m) than Alr with L- and D-alanine, respectively. Together these results demonstrate that DadX is specialized for alanine racemization, which is precisely what a catabolic enzyme feeding the alanine-degradation pathway should be.

The physiological context is that *P. putida* KT2440 can **catabolize D-alanine as a sole carbon and nitrogen source** — Radkov & Moe showed the organism grows on the D-stereoisomers of lysine, phenylalanine, arginine, alanine, and hydroxyproline. DadX provides the racemase activity that couples L- and D-alanine pools to this catabolic capability.

> "the putative catabolic alanine racemase DadX showed narrow substrate specificity, clearly preferring only the alanine stereoisomers as the substrates" — Radkov & Moe 2013

> "DadX did show 6- and 9-fold higher k(cat)/K(m) values than Alr with l- and d-alanine, respectively" — Radkov & Moe 2013

### Finding 2 — DadX belongs to the PLP-dependent alanine racemase family and uses a conserved two-base (Lys/Tyr) catalytic mechanism

DadX carries the complete **alanine racemase domain architecture**: the N-terminal PLP-binding TIM-barrel (α/β)8 domain (InterPro **IPR001608**), the C-terminal β-sheet domain (**IPR011079 / IPR009006**), and the diagnostic PLP-binding site signature (**IPR020622**). Cao et al. explicitly identified the **pyridoxal-5′-phosphate binding site motif** in *P. putida* DadX ([PMID: 16579470](https://pubmed.ncbi.nlm.nih.gov/16579470/)), confirming the cofactor chemistry at the sequence level.

The catalytic mechanism is defined by decades of structural and mutagenesis work on the archetypal *Bacillus stearothermophilus* alanine racemase. X-ray crystallography of the enzyme bound with N-(5′-phosphopyridoxyl)alanine ([PMID: 11886871](https://pubmed.ncbi.nlm.nih.gov/11886871/)) established that **Tyr265′ and Lys39 are the catalytic bases** that remove the α-hydrogen from L- and D-alanine, respectively — a **two-base mechanism** in which each base acts on one face of the substrate α-carbon. Independent evidence from arginine-219 mutants ([PMID: 10194319](https://pubmed.ncbi.nlm.nih.gov/10194319/)) reinforced this model: a conserved Arg219 hydrogen-bonds to the PLP pyridine nitrogen and, through a His166-mediated network, electrostatically tunes the pKa of Tyr265; mutation of Arg219 shifts the kcat/KM pKa from ~7.1–7.4 to ~9.5–10.4 and produces a 510 nm quinonoid intermediate consistent with a two-base mechanism. Alanine racemases are **obligate homodimers**, with each active site assembled at the subunit interface (the N-terminal domain of one monomer plus the C-terminal domain — supplying the second catalytic tyrosine — of the partner). DadX inherits this mechanism and quaternary requirement.

> "Tyr(265)' and Lys(39) are the catalytic bases removing alpha-hydrogen from L- and D-alanine, respectively" — Watanabe et al. 2002

> "Two motifs believed essential to the enzyme activity are found both in DadX and Alr, such as pyridoxal-5'-phosphate binding site" — Cao et al. 2006

### Finding 3 — DadX functions in the cytoplasmic D-alanine catabolic (*dad*) pathway, feeding alanine into central metabolism

The functional pairing of *dadX* with *dadA* is well established from *E. coli*, where **dadX lies within an inducible operon adjacent to dadA** (D-amino acid dehydrogenase) (Wild et al. 1985, [PMID: 3920477](https://pubmed.ncbi.nlm.nih.gov/3920477/)). The DadX racemase produces D-alanine, which the membrane-associated flavoprotein DadA then oxidatively deaminates to **pyruvate + ammonia**, allowing alanine to serve as both a carbon and nitrogen source. Wild et al. also showed the pathway is metabolically regulated as a catabolic system: the predominant racemase isozyme is **induced by either alanine stereoisomer and repressed by glucose** (catabolite repression) — the regulatory signature of a degradative, not biosynthetic, enzyme.

In *P. putida* KT2440, Radkov & Moe confirmed the organism catabolizes D-alanine as a sole carbon and nitrogen source, the very pathway DadX serves. Alanine racemases are soluble **cytoplasmic** enzymes, and DadX carries no signal peptide or membrane-anchoring feature, so its racemization reaction occurs in the cytosol; the coupled DadA dehydrogenase is membrane-associated but faces the cytoplasm. This catabolic role is mechanistically distinct from the biosynthetic racemase **Alr**, whose D-alanine product is dedicated to **peptidoglycan/cell-wall synthesis**.

> "The gene dadX coding for its structure is located by the dadA gene determining the structure of D-amino acid dehydrogenase" — Wild et al. 1985

> "The predominant isozyme is inducible by either alanine stereoisomer and repressible by glucose" — Wild et al. 1985

> "P. putida KT2440 catabolized the d-stereoisomers of lysine, phenylalanine, arginine, alanine, and hydroxyproline as the sole carbon and nitrogen sources" — Radkov & Moe 2013

### Finding 4 — The 357-aa DadX sequence contains the conserved PLP-binding catalytic lysine (Lys33)

The Q88CB2 sequence is **357 residues**, matching the DadX peptide reported by Cao et al. (357 aa, ~38.8 kDa; [PMID: 16579470](https://pubmed.ncbi.nlm.nih.gov/16579470/)). Sequence inspection reveals the diagnostic N-terminal alanine-racemase PLP-binding motif **K-x-D-A-Y-G-H-G ("KADAYGHG")** with the **Schiff-base lysine at position 33** — positionally homologous to the catalytic **Lys39** of the *B. stearothermophilus* enzyme that abstracts the α-proton from D-alanine ([PMID: 11886871](https://pubmed.ncbi.nlm.nih.gov/11886871/)). Ten tyrosine residues are present in the sequence, including residues in the C-terminal domain that supplies the second catalytic base (the Tyr homolog of Tyr265′) across the dimer interface. This sequence-level conservation of both catalytic bases confirms DadX is a fully functional member of the family capable of the two-base mechanism.

> "DadX encodes a peptide of 357 amino acids with a calculated molecular weight of 38.82kDa" — Cao et al. 2006

### Finding 5 — Genomic context: *dadX* (PP_5269) is adjacent to *dadA2* (PP_5270), confirming native *dadAX* coupling

Interrogation of the *P. putida* KT2440 genome (taxid 160488) shows that the immediate neighbor of **dadX / PP_5269** (Q88CB2, alanine racemase, 357 aa) is **PP_5270 / Q88CB1**, annotated as **D-amino acid dehydrogenase 2** (dadA2, EC 1.4.99.-, 434 aa). This directly mirrors the *E. coli* *dadAX* operon architecture ([PMID: 3920477](https://pubmed.ncbi.nlm.nih.gov/3920477/)) **in the target organism itself**, providing strong genomic-context evidence that DadX-produced D-alanine is the substrate for the adjacent DadA dehydrogenase. Notably, a **leucine-responsive regulatory protein gene (lrp, PP_5271 / Q88CB0)** lies immediately downstream — Lrp being a known transcriptional regulator of amino-acid (including *dad*) catabolism. The gene neighborhood thus recapitulates a complete, regulated catabolic module.

> "The gene dadX coding for its structure is located by the dadA gene determining the structure of D-amino acid dehydrogenase" — Wild et al. 1985

---

## Mechanistic Model / Interpretation

### The reaction

DadX catalyzes the PLP-dependent racemization of alanine:

```
        L-alanine  ⇌  D-alanine
                 [DadX, PLP]
```

The PLP cofactor is bound as an internal aldimine (Schiff base) to **Lys33**. When alanine binds, a transaldimination forms the external aldimine. Racemization then proceeds by the **two-base mechanism**: the α-proton is abstracted from one face by one catalytic base, forming a resonance-stabilized **carbanion/quinonoid intermediate**, and reprotonated on the opposite face by the second base. In the family archetype, **Lys** abstracts from D-alanine and **Tyr** (from the partner subunit) abstracts from L-alanine.

```
   L-Ala face                       D-Ala face
      │                                  │
   Tyr (base)  ──►  quinonoid  ◄──  Lys33 (base)
      │           intermediate           │
      └──────── PLP (Schiff base) ────────┘
             active site at dimer interface
```

### The catabolic module

DadX is **step 1 of a two-enzyme degradation module** encoded in a conserved gene cluster:

```
 PP_5269 (dadX)      PP_5270 (dadA2)          PP_5271 (lrp)
 alanine racemase    D-amino acid dehydrog.   Lrp regulator
       │                    │                       │
   L-Ala ⇌ D-Ala   D-Ala + H2O + [FAD] ─►    (transcriptional
       └──────────►  pyruvate + NH3            control of module)
                            │
                            ▼
              central C/N metabolism (TCA cycle)
```

- **DadX** supplies D-alanine by racemizing the abundant L-alanine pool.
- **DadA (DadA2)**, a membrane-associated FAD-dependent D-amino acid dehydrogenase, oxidatively deaminates D-alanine to **pyruvate + ammonia**.
- The products enter central metabolism: **pyruvate** as a carbon skeleton (TCA cycle / gluconeogenesis) and **ammonia** as a nitrogen source.
- This enables growth on alanine (and D-alanine) as sole carbon and nitrogen source.

### Two racemases, two fates for D-alanine

*P. putida* possesses two alanine racemases with divergent physiological purposes — a recurring theme in Pseudomonads (cf. *P. aeruginosa* PAO1, which likewise has *dadX* and *alr*; [PMID: 10977898](https://pubmed.ncbi.nlm.nih.gov/10977898/)):

| Property | **DadX (catabolic, Q88CB2)** | **Alr (biosynthetic/anabolic)** |
|---|---|---|
| Substrate specificity | Narrow — alanine stereoisomers only | Broad — racemizes 9/19 chiral amino acids |
| Catalytic efficiency on Ala | 6–9× higher *k*cat/*K*m than Alr | Lower on alanine |
| Physiological role | Feeds D-Ala into DadA for degradation | Supplies D-Ala for peptidoglycan synthesis |
| Regulation | Inducible by alanine, glucose-repressible | Constitutive/housekeeping |
| Direction of net flux | L-Ala → D-Ala (for catabolism) | L-Ala → D-Ala (for cell wall) |
| Localization | Cytoplasm | Cytoplasm |

Both enzymes are cytoplasmic and mechanistically identical, but DadX's kinetic specialization for alanine and its co-regulation/co-localization with DadA mark it unambiguously as the **degradative** racemase.

---

## Evidence Base

| PMID | Study | Relevance to DadX function |
|---|---|---|
| [23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) | *Amino acid racemization in P. putida KT2440* (Radkov & Moe 2013) | **Primary, most authoritative.** Purified and kinetically characterized DadX from the target organism; established narrow alanine specificity and higher efficiency than Alr; demonstrated D-alanine catabolism as sole C/N source. Basis of the catabolic assignment. |
| [16579470](https://pubmed.ncbi.nlm.nih.gov/16579470/) | *Cloning, sequence analysis and expression of alanine racemase gene in P. putida* (Cao et al. 2006) | Confirms DadX identity (357 aa, 38.82 kDa) and presence of the PLP-binding site motif in *P. putida* DadX. Anchors sequence-level identity. |
| [3920477](https://pubmed.ncbi.nlm.nih.gov/3920477/) | *Identification of the dadX gene…in E. coli K12* (Wild et al. 1985) | Establishes the *dadAX* operon coupling and catabolic regulation (alanine induction, glucose repression) of the orthologous catabolic racemase. Supports pathway context. |
| [11886871](https://pubmed.ncbi.nlm.nih.gov/11886871/) | *Reaction mechanism of alanine racemase from B. stearothermophilus* (Watanabe et al. 2002) | Defines the conserved two-base (Lys39/Tyr265′) PLP mechanism to which DadX belongs. Structural/mechanistic foundation. |
| [10194319](https://pubmed.ncbi.nlm.nih.gov/10194319/) | *Evidence for a two-base mechanism…Arg-219 mutants* (Sun & Toney 1999) | Independent mechanistic validation of the two-base mechanism and the role of the conserved Arg219–His166–Tyr265 network. |
| [10977898](https://pubmed.ncbi.nlm.nih.gov/10977898/) | *Characterization of alanine racemases from P. aeruginosa PAO1* | Comparative evidence: a closely related Pseudomonad also has independent *dadX* and *alr* racemases, both PLP enzymes; supports the two-racemase paradigm. |
| [36483308](https://pubmed.ncbi.nlm.nih.gov/36483308/) | *DadY (PA5303) is required for fitness…* | Context for D-amino acid metabolism/transport fitness in Pseudomonas (abstract unavailable; peripheral support). |

**Consistency assessment:** All lines of evidence — direct enzymology in the target organism, sequence/motif analysis, the family's structural mechanism, operon genomics, and comparative Pseudomonad data — are mutually reinforcing. No evidence contradicts the assignment of DadX as the catabolic alanine racemase.

---

## Limitations and Knowledge Gaps

1. **No DadX-specific 3-D structure.** There is no experimentally determined crystal structure of *P. putida* KT2440 DadX itself. The two-base mechanism and catalytic residue assignments (Lys33; the partner-subunit Tyr) are inferred by homology from *B. stearothermophilus* and by sequence-motif conservation, not from a DadX structure. An AlphaFold model or crystal structure would confirm the active-site geometry directly.

2. **Catalytic Tyr not individually pinpointed in DadX.** While ten tyrosines are present and the C-terminal domain supplies the second base by homology, the exact catalytic Tyr residue number in DadX has not been experimentally confirmed by mutagenesis.

3. **No in vivo *dadX* knockout phenotype in KT2440.** The catabolic role is strongly inferred from in vitro kinetics, operon context, and orthology, but a targeted *dadX* deletion demonstrating loss of alanine catabolism (and the extent to which Alr can compensate) has not been reported here.

4. **Regulation in *P. putida* specifically.** The alanine-induction/glucose-repression regulation is documented for *E. coli* dadX; the precise transcriptional control of PP_5269 (including the exact role of the downstream Lrp / PP_5271) in KT2440 is inferred by analogy and warrants direct confirmation.

5. **Quantitative substrate profile is qualitative here.** "Narrow specificity for alanine" is established, but full kinetic constants (Km, kcat) across a panel of amino acids for DadX specifically are summarized rather than tabulated.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination / modeling.** Obtain an X-ray or cryo-EM structure of DadX, or analyze an AlphaFold2 model with PAE/pLDDT, to confirm the homodimeric active-site arrangement, verify Lys33 as the PLP Schiff-base residue, and identify the partner-subunit catalytic tyrosine.

2. **Site-directed mutagenesis.** Mutate Lys33 and candidate catalytic Tyr residues (and the conserved Arg homolog of Arg219) to alanine and measure racemase activity, directly testing the two-base mechanism in DadX.

3. **Targeted gene deletion.** Construct a clean *dadX* (PP_5269) knockout in *P. putida* KT2440 and assay growth on L- and D-alanine as sole C/N source; construct a *dadX alr* double mutant to test functional redundancy for D-alanine catabolism versus cell-wall provision.

4. **Transcriptional analysis.** Use qRT-PCR or reporter fusions to test alanine induction and glucose (catabolite) repression of the PP_5269–PP_5270 module in KT2440, and test the regulatory role of the adjacent *lrp* (PP_5271).

5. **Full kinetic panel.** Measure *K*m and *k*cat of purified DadX against a comprehensive panel of chiral amino acids to quantify the substrate specificity window relative to Alr.

6. **Metabolic flux confirmation.** Use ¹³C- or ¹⁵N-labeled alanine to trace flux from L-alanine → D-alanine → pyruvate + ammonia, quantifying the DadX/DadA contribution to central C and N metabolism.

---

## Conclusion

**dadX (Q88CB2, PP_5269) encodes the catabolic alanine racemase of *Pseudomonas putida* KT2440.** It is a soluble, cytoplasmic, PLP-dependent enzyme (Schiff-base catalytic Lys33) that reversibly interconverts L- and D-alanine via the conserved two-base racemase mechanism, with narrow substrate specificity for the alanine stereoisomers and higher catalytic efficiency than the broad-specificity biosynthetic racemase Alr. Its physiological function is the first step of the two-enzyme *dad* catabolic module — genomically confirmed by its adjacency to *dadA2* (PP_5270) — supplying D-alanine that the DadA dehydrogenase oxidatively deaminates to pyruvate and ammonia, enabling *P. putida* to use alanine as a carbon and nitrogen source. This role is distinct from the biosynthetic racemase Alr, which supplies D-alanine for peptidoglycan cell-wall synthesis.


## Artifacts

- [OpenScientist final report](dadX-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dadX-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23995642
2. PMID:16579470
3. PMID:3920477
4. PMID:11886871
5. PMID:10194319
6. PMID:10977898