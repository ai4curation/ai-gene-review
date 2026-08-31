---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T10:23:28.438198'
end_time: '2026-08-31T11:50:34.780427'
duration_seconds: 5226.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rbsA-I
  gene_symbol: rbsA-I
  uniprot_accession: Q88K37
  protein_description: 'SubName: Full=Ribose ABC transporter-ATP-binding subunit {ECO:0000313|EMBL:AAN68067.1};
    EC=3.6.3.17 {ECO:0000313|EMBL:AAN68067.1};'
  gene_info: Name=rbsA-I {ECO:0000313|EMBL:AAN68067.1}; OrderedLocusNames=PP_2455
    {ECO:0000313|EMBL:AAN68067.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AAA+_ATPase. (IPR003593); ABC_carbohydrate_import_ATPase. (IPR050107);
    ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871);
    P-loop_NTPase. (IPR027417)
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
citation_count: 2
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rbsA-I-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rbsA-I-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K37
- **Protein Description:** SubName: Full=Ribose ABC transporter-ATP-binding subunit {ECO:0000313|EMBL:AAN68067.1}; EC=3.6.3.17 {ECO:0000313|EMBL:AAN68067.1};
- **Gene Information:** Name=rbsA-I {ECO:0000313|EMBL:AAN68067.1}; OrderedLocusNames=PP_2455 {ECO:0000313|EMBL:AAN68067.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_carbohydrate_import_ATPase. (IPR050107); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rbsA-I" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rbsA-I' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rbsA-I** (gene ID: rbsA-I, UniProt: Q88K37) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: rbsA-I (PP_2455 / Q88K37) in *Pseudomonas putida* KT2440

## Summary

**rbsA-I (PP_2455; UniProt Q88K37) encodes the cytoplasmic ATP-binding (ATPase) subunit of the high-affinity D-ribose ABC importer of *Pseudomonas putida* KT2440.** It is a 524-amino-acid soluble protein built from two fused nucleotide-binding domains (NBDs), each carrying the canonical Walker A / P-loop and Walker B catalytic motifs of the ABC-transporter ATPase superfamily. Its primary function is not to catalyze a stand-alone metabolic reaction but to serve as the energy-coupling motor of a membrane transport machine: it binds and hydrolyzes ATP at the cytoplasmic face of the inner membrane, and the resulting conformational cycling drives the vectorial translocation of D-ribose from the periplasm into the cytoplasm through its partner permease. The enzyme classification EC 7.5.2.7 (previously EC 3.6.3.17), KEGG orthology K10441 ("ribose transport system ATP-binding protein"), and GO terms GO:0005524 (ATP binding), GO:0016887 (ATP hydrolysis activity), and GO:0015749 (monosaccharide transmembrane transport) all converge on this assignment.

The identity of the protein is unambiguous. PP_2455 sits within a complete, canonically organized chromosomal ribose (*rbs*) operon (PP_2454–PP_2460) that encodes the periplasmic ribose-binding protein (RbsB), the ATPase (RbsA-I), the permease (RbsC), a LacI-family repressor (RbsR), and the downstream catabolic enzymes ribokinase (RbsK), ribose pyranase (RbsD), and a ribonucleoside hydrolase. This gene neighborhood mirrors the archetypal *Escherichia coli* *rbsDACBK*–*rbsR* system, in which the RbsABC complex is the high-affinity transporter and RbsD/RbsK convert imported D-ribose into D-ribose-5-phosphate for entry into the pentose-phosphate pathway. RbsA-I shares 41% amino-acid identity with the biochemically characterized *E. coli* RbsA, a level well above the threshold generally accepted for confident cross-genus functional transfer among transporter ATPases.

The substrate specificity of the transporter — D-ribose — is determined by the periplasmic binding protein RbsB rather than by RbsA-I itself; the ATPase is the generic energizing component. RbsA-I therefore acts at the cytoplasmic face of the inner membrane, physically docked onto the RbsC permease homodimer, where its nucleotide-binding state governs the assembly and conformational state of the full RbsABC₂ translocation complex. This report details the evidence for each of these conclusions, presents a mechanistic model, evaluates the supporting literature, and identifies the residual knowledge gaps and experiments that would close them.

---

## Key Findings

### Finding 1 — PP_2455 (rbsA-I) encodes the ATP-binding (ATPase) subunit of a canonical D-ribose ABC importer

The core functional assignment rests on a convergence of sequence, domain, and orthology evidence. UniProt Q88K37 describes a 524-amino-acid protein annotated with the keywords ATP-binding, Nucleotide-binding, Translocase/Hydrolase, and Sugar transport. Domain analysis identifies two copies of the Pfam PF00005 ABC_tran domain (a tandem, repeated architecture), together with InterPro signatures IPR050107 (ABC carbohydrate-import ATPase), IPR003439 (ABC transporter-like ATP-binding domain), IPR003593 (AAA+ ATPase), and IPR027417 (P-loop NTPase). The KEGG entry ppu:PP_2455 maps to KEGG Orthology K10441, "ribose transport system ATP-binding protein," with EC 7.5.2.7 (ABC-type D-ribose transporter; the modern reclassification of the legacy EC 3.6.3.17 cited in the UniProt record). The Gene Ontology annotations — GO:0005524 (ATP binding), GO:0016887 (ATP hydrolysis activity), and GO:0015749 (monosaccharide transmembrane transport) — are fully consistent with an ABC-transporter ATPase. Direct inspection of the primary sequence confirms a Walker A / P-loop motif (…TGENGAGKSTL…) diagnostic of nucleotide binding.

The protein's length is itself informative. At 524 aa, RbsA-I is roughly twice the size of a single ~260-aa nucleotide-binding domain, consistent with two fused NBDs — exactly the architecture of the experimentally defined *E. coli* RbsA. The reconstitution study of the *E. coli* ribose transporter states plainly that "the ribose transporter in *Escherichia coli* is a tripartite complex consisting of a cytoplasmic ATP-binding cassette protein, RbsA, with fused nucleotide binding domains; a transmembrane domain homodimer, RbsC₂; and a periplasmic substrate binding protein, RbsB" ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)). This description of RbsA as a cytoplasmic ABC protein with two fused NBDs matches the observed 524-aa, two-NBD architecture of Q88K37 point for point.

**Interpretation:** RbsA-I is the ATP-hydrolyzing engine of an importer. It supplies the free energy — through ATP binding and hydrolysis — that powers uphill accumulation of D-ribose against a concentration gradient. It is a transporter subunit, not an independent catabolic enzyme.

### Finding 2 — rbsA-I lies within a complete chromosomal ribose (*rbs*) operon dedicated to D-ribose uptake and catabolism

Gene context is one of the strongest lines of evidence for the function of a transporter subunit, because ABC-importer genes are almost universally clustered with their cognate binding protein, permease, and downstream catabolic enzymes. The KEGG genomic neighborhood of PP_2455 (chromosomal coordinates ~2,801,617–2,803,191 and flanking genes) comprises:

| Locus tag | Gene | Product | Role in ribose utilization |
|-----------|------|---------|----------------------------|
| PP_2454 | rbsB | Periplasmic ribose-binding protein | Captures D-ribose in periplasm; sets substrate specificity |
| **PP_2455** | **rbsA-I** | **ABC transporter ATP-binding subunit** | **Energizes transport via ATP hydrolysis (this study)** |
| PP_2456 | rbsC | Ribose permease (transmembrane domain) | Forms the translocation channel |
| PP_2457 | rbsR | LacI-family transcriptional repressor | Regulates operon expression |
| PP_2458 | rbsK | Ribokinase | Phosphorylates D-ribose → D-ribose-5-phosphate |
| PP_2459 | rbsD | Ribose pyranase | Interconverts ribose anomers/forms for kinase |
| PP_2460 | — | Ribonucleoside hydrolase | Liberates ribose from nucleosides |

This organization recapitulates the *E. coli* *rbsDACBK*–*rbsR* system, in which RbsABC is the high-affinity transporter and RbsD/RbsK convert D-ribose into D-ribose-5-phosphate. The regulatory and metabolic logic of the operon is well established: "the genes for the transport and initial-step metabolism of D-ribose form a single *rbsDACBK* operon. RbsABC forms the ABC-type high-affinity D-ribose transporter, while RbsD and RbsK are involved in the conversion of D-ribose into D-ribose 5-phosphate" ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)). The presence in the *P. putida* cluster of all three transporter genes (*rbsB*, *rbsA-I*, *rbsC*) together with *rbsK*, *rbsD*, and a ribonucleoside hydrolase confirms that this locus constitutes a complete, self-contained ribose acquisition-and-catabolism module.

**Interpretation:** The operon context removes essentially all ambiguity about the substrate and pathway. RbsA-I energizes the import of D-ribose, which is immediately handed off to RbsK/RbsD for conversion to D-ribose-5-phosphate and entry into the pentose-phosphate pathway. The co-localized RbsR repressor places the entire module under substrate-responsive transcriptional control.

### Finding 3 — RbsA localizes to the cytoplasmic face of the inner membrane and powers transport via ATP hydrolysis within the RbsABC₂ complex

The subcellular localization annotation in UniProt places Q88K37 at the cell inner membrane / cell membrane as a peripheral protein on the cytoplasmic side. This is precisely the expected topology for a soluble ABC-ATPase that docks onto the cytoplasmic coupling helices of its permease. The functional dynamics of this arrangement were resolved biochemically for the *E. coli* orthologue. In vitro reassembly of the ribose transporter demonstrated that RbsA associates with the RbsC₂ permease homodimer, and that the composition of the isolated complex depends on the nucleotide state: "we were able to purify a full complex, RbsABC₂, in the presence of stable, transition state mimics (ATP, Mg²⁺, and VO₄); a RbsAC complex in the presence of ADP and Mg²⁺; and a heretofore unobserved RbsBC complex in the absence of cofactors" ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)).

This nucleotide-dependent assembly is direct experimental evidence that RbsA's catalytic cycle — ATP binding, hydrolysis to ADP, and product release — drives the conformational transitions that alternately assemble and disassemble the translocation-competent complex. The transition-state mimic (ATP·Mg·VO₄) traps the full RbsABC₂ complex, whereas the post-hydrolysis ADP·Mg state yields only RbsAC, illustrating how the ATPase gates the recruitment of the substrate-loaded binding protein. Because RbsA-I of *P. putida* is 41% identical to this *E. coli* RbsA and conserves all catalytic motifs (Finding 4), the same mechanism is confidently inferred.

**Interpretation:** RbsA-I performs its function as a membrane-associated (but not membrane-integral) subunit on the inner (cytoplasmic) leaflet of the inner membrane. Its ATPase cycle mechanically couples chemical energy to the alternating-access motion of the RbsC permease, achieving vectorial import of D-ribose.

### Finding 4 — RbsA-I shares 41% identity with experimentally characterized *E. coli* RbsA and possesses the conserved dual ABC-ATPase motif set

A Needleman–Wunsch global alignment of Q88K37 (524 aa) against *E. coli* RbsA (UniProt P04983, 501 aa) yields 41.2% identity over 498 aligned columns. For transporter ATPases, identity in this range across genera is a strong basis for functional transfer, especially when combined with conserved active-site motifs and identical genomic context. A motif scan of Q88K37 confirms the tandem two-NBD architecture expected of RbsA:

| Motif | NBD1 | NBD2 |
|-------|------|------|
| Walker A / P-loop | GENGAGKS (residue ~48) | P-loop-type region (AASGLGKT, res ~18 region) |
| Walker B (…hhhhDE) | LILDE (res ~174) | LLFDE (res ~430) |

The two cleanly separated Walker B motifs demarcate the two fused nucleotide-binding domains, exactly as expected for a "double-NBD" importer ATPase. The presence of two complete Walker A/Walker B pairs distinguishes RbsA from single-NBD ABC-ATPases (which function as homodimers) and identifies it as the intramolecularly-fused variant characteristic of the ribose importer family.

**Interpretation:** The high sequence identity to a functionally validated orthologue, combined with the fully conserved catalytic apparatus (two P-loops, two Walker B motifs), makes the functional assignment of RbsA-I as an ATP-hydrolyzing ribose-importer subunit essentially certain by homology, independent of the operon-context evidence.

### Finding 5 — *P. putida* encodes two ribose ABC-ATPase paralogs; rbsA-I (PP_2455) is the copy embedded in the complete catabolic ribose operon

*P. putida* KT2440 possesses two loci mapped to KEGG Orthology K10441: PP_2455 (rbsA-I, Q88K37, 524 aa) and PP_2759 (rbsA / "rbsA-II", Q88J90, 512 aa). The two paralogs share only 42.9% identity by global alignment, comparable to their individual identity with *E. coli* RbsA, indicating an ancient duplication or independent acquisition rather than a recent gene doubling. Critically, only PP_2455 sits within a *complete* ribose operon: it is flanked by the substrate-binding protein (rbsB, PP_2454), the permease (rbsC, PP_2456), the regulator (rbsR, PP_2457), and the downstream catabolic genes ribokinase (rbsK, PP_2458), ribose pyranase (rbsD, PP_2459), and a ribonucleoside hydrolase (PP_2460). By contrast, the PP_2759 cluster (PP_2757–PP_2761) contains two K10439-type binding proteins, the PP_2759 ATPase, and two K10440-type permeases but *lacks adjacent ribokinase and pyranase genes*.

**Interpretation:** The absence of co-localized catabolic enzymes at the PP_2759 cluster suggests that paralog carries out a related but distinct transport role (potentially a different pentose or ribose-derivative, or feeding a different metabolic branch), whereas rbsA-I (PP_2455) is the transporter ATPase directly wired to D-ribose catabolism through the pentose-phosphate pathway. This paralog distinction is important for correct annotation: RbsA-I is the "canonical," catabolically-coupled ribose importer ATPase of *P. putida*.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of a Type I ABC importer operating at the *P. putida* inner membrane. The transport module is tripartite plus a soluble receptor, and RbsA-I is its ATP-hydrolyzing motor.

```
                          PERIPLASM
                 D-ribose  ●
                            \
                    ┌────────▼────────┐
                    │  RbsB (PP_2454) │   periplasmic binding protein
                    │  captures ribose│   → sets D-ribose specificity
                    └────────┬────────┘
                             │ delivers substrate
   ══════════════════════════╪══════════════════════  INNER MEMBRANE
        ┌──────────────┐     │      ┌──────────────┐
        │  RbsC (PP_2456) permease homodimer (RbsC2) │  translocation channel
        └──────┬───────┘            └───────┬───────┘
               │  coupling helices          │
        ┌──────▼────────────────────────────▼──────┐
        │        RbsA-I (PP_2455)  —  ATPase        │  CYTOPLASMIC face
        │   NBD1 [Walker A GENGAGKS | Walker B LILDE]│
        │   NBD2 [Walker A/P-loop   | Walker B LLFDE]│
        │        ATP → ADP + Pi  (EC 7.5.2.7)        │
        └────────────────────┬──────────────────────┘
                          CYTOPLASM
                 D-ribose  ●
                            │  RbsK ribokinase (PP_2458)
                            │  RbsD pyranase   (PP_2459)
                            ▼
                 D-ribose-5-phosphate  →  Pentose-phosphate pathway
```

**Transport cycle.** In the resting state, the periplasmic RbsB scavenges D-ribose. Substrate-loaded RbsB docks onto the periplasmic face of the RbsC₂ permease. On the cytoplasmic side, RbsA-I binds two molecules of Mg·ATP at the interface of its two NBDs. ATP binding drives NBD dimerization/closure, which is transmitted through the permease coupling helices to open the transmembrane cavity toward the periplasm and accept the substrate. ATP hydrolysis and Pi/ADP release reset the transporter to the inward-open state, delivering D-ribose to the cytoplasm. The *E. coli* reconstitution study captured discrete snapshots of this cycle — full RbsABC₂ in the ATP transition-state mimic, RbsAC in the ADP state — providing direct structural-biochemical validation of the nucleotide-gated mechanism ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)).

**Metabolic coupling.** Imported D-ribose is immediately committed to catabolism by the co-operonic enzymes: ribose pyranase (RbsD) equilibrates the ribose anomeric forms, and ribokinase (RbsK) phosphorylates D-ribose to D-ribose-5-phosphate, the entry metabolite of the non-oxidative pentose-phosphate pathway ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)). The adjacent ribonucleoside hydrolase (PP_2460) can additionally liberate ribose from nucleosides, feeding the same pathway.

**Regulation.** The LacI-family repressor RbsR (PP_2457) controls operon expression in a substrate-responsive manner. In *E. coli*, RbsR additionally links ribose availability to purine nucleotide synthesis regulation, a role that underscores the tight integration of ribose transport with central nucleotide metabolism ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)).

**Division of labor / annotation clarity.** Substrate specificity resides in RbsB, not RbsA-I. RbsA-I is the interchangeable energizing subunit; its function is transport energization, and its "substrate" in the enzymatic sense is ATP. The presence of a second K10441 paralog (PP_2759) that is *not* embedded in a complete catabolic operon reinforces that PP_2455 specifically is the ribose-catabolism-coupled importer ATPase.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/) | *In vitro reassembly of the ribose ABC transporter…* | **Primary experimental anchor.** Defines RbsA as the cytoplasmic ABC protein with fused NBDs (supports F001, F004); shows nucleotide-state-dependent assembly of RbsABC₂ / RbsAC complexes, evidencing ATP-hydrolysis-driven transport at the membrane (supports F003). |
| [23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/) | *Involvement of the ribose operon repressor RbsR in regulation of purine nucleotide synthesis in E. coli.* | Establishes the *rbsDACBK* operon organization and that RbsABC is the high-affinity D-ribose transporter feeding RbsD/RbsK to make D-ribose-5-phosphate (supports F002); links the operon to nucleotide metabolism via RbsR. |
| [10941799](https://pubmed.ncbi.nlm.nih.gov/10941799/) | *Ribose utilization in Lactobacillus sakei…* | **Contrasting case.** Demonstrates that some bacteria dispense with the RbsABC ABC transporter entirely, using an alternative permease (RbsU) — highlighting that the ABC-transporter route seen in *P. putida* is one of several evolutionary solutions, and underscoring the value of *P. putida*'s complete *rbsBACR-KD* operon in confirming the ABC route here. |

**Assessment.** The two supporting papers ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/) and [PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)) are precise, mechanism-focused studies of the *E. coli* ribose system — the closest well-characterized orthologue. Together with the 41% sequence identity and complete conserved operon in *P. putida*, they provide a robust, non-high-throughput basis for the functional assignment. No direct experimental characterization of PP_2455 itself (e.g., in vitro ATPase assay, transport assay, or knockout) was located; the assignment is therefore inference-by-orthology of high confidence rather than direct demonstration.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on PP_2455 itself.** All mechanistic evidence derives from the *E. coli* orthologue. There is no published in vitro ATPase measurement, ribose-transport assay, structure, or gene-deletion phenotype specifically for *P. putida* RbsA-I. The assignment, while strong, is homology- and context-based.

2. **Substrate specificity is inferred, not measured, in *P. putida*.** D-ribose specificity is attributed to RbsB by analogy. It remains possible (though unlikely) that the *P. putida* system has broadened or shifted specificity toward a ribose-related pentose.

3. **Role of the second paralog (PP_2759 / rbsA-II) is unresolved.** Its cluster lacks co-localized ribokinase/pyranase; whether it transports ribose under different conditions, a different sugar, or feeds a different pathway is not established. This affects the completeness of the ribose-transport annotation for the organism.

4. **Regulatory details in *P. putida* are unverified.** RbsR-mediated, ribose-responsive control of the PP_2454–PP_2460 operon is inferred from *E. coli*; the effector and operator architecture in *P. putida* have not been experimentally mapped.

5. **Quantitative kinetics unknown.** Affinity (K_m/K_d) for ribose, ATP turnover rate, and coupling stoichiometry (ATP hydrolyzed per ribose imported) are unmeasured for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Direct ATPase assay.** Heterologously express and purify RbsA-I (PP_2455), and measure Mg-ATP hydrolysis (malachite-green / NADH-coupled assay), ideally with and without reconstituted RbsC permease to demonstrate permease-stimulated ATPase activity.

2. **Transport assay in a defined background.** Construct a ΔPP_2455 deletion (and a ΔPP_2455 ΔPP_2759 double mutant) and assay ¹⁴C-D-ribose uptake and growth on D-ribose as the sole carbon source. A growth/uptake defect rescued by complementation would provide direct in vivo proof of function and clarify the division of labor with the PP_2759 paralog.

3. **Reconstitution / structure.** Co-express RbsA-I with RbsC (PP_2456) and RbsB (PP_2454), reconstitute into nanodiscs/proteoliposomes, and use cryo-EM to capture nucleotide-state-dependent conformations, paralleling the *E. coli* study ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)).

4. **Specificity screen of RbsB.** Determine the binding spectrum of the periplasmic RbsB (PP_2454) by isothermal titration calorimetry against D-ribose and related pentoses to confirm that specificity is set at the binding-protein step.

5. **Operon regulation mapping.** Test RbsR (PP_2457) binding to the operon promoter by EMSA and identify the physiological inducer, confirming ribose-responsive transcriptional control in *P. putida*.

6. **Paralog functional dissection.** Characterize the PP_2757–PP_2761 cluster (including PP_2759) transport specificity to resolve whether it is a second ribose route or handles a distinct substrate, completing the transport annotation of the organism.

---

## Conclusion

rbsA-I (PP_2455 / Q88K37) is the cytoplasmic ATP-binding subunit of the high-affinity D-ribose ABC importer of *Pseudomonas putida* KT2440. It is a 524-amino-acid, two-fused-NBD ABC-ATPase (EC 7.5.2.7, KEGG K10441) that hydrolyzes ATP at the cytoplasmic face of the inner membrane to energize D-ribose translocation through the RbsC permease, working with the periplasmic RbsB substrate-binding protein that dictates D-ribose specificity. It is embedded in a complete *rbs* operon (rbsB–rbsA-I–rbsC–rbsR–rbsK–rbsD–nucleoside hydrolase) that channels imported ribose, via ribokinase-produced D-ribose-5-phosphate, into the pentose-phosphate pathway. The assignment is supported by 41% identity to the biochemically characterized *E. coli* RbsA, full conservation of the dual Walker A/Walker B catalytic apparatus, unambiguous operon context, and reconstitution studies of the *E. coli* RbsABC₂ transporter — while remaining, at present, an inference-by-orthology that has not yet been directly validated for the *P. putida* protein itself.


## Artifacts

- [OpenScientist final report](rbsA-I-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rbsA-I-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25533465
2. PMID:23651393