---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T10:23:28.438192'
end_time: '2026-08-31T10:34:05.810744'
duration_seconds: 637.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rbsB
  gene_symbol: rbsB
  uniprot_accession: Q88K38
  protein_description: 'SubName: Full=Ribose ABC transporter, periplasmic ribose-binding
    subunit {ECO:0000313|EMBL:AAN68066.1};'
  gene_info: Name=rbsB {ECO:0000313|EMBL:AAN68066.1}; OrderedLocusNames=PP_2454 {ECO:0000313|EMBL:AAN68066.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial solute-binding protein 2 family.
  protein_domains: Peripla_BP_I. (IPR028082); SBP_2_dom. (IPR025997); Peripla_BP_4
    (PF13407)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rbsB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rbsB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K38
- **Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding subunit {ECO:0000313|EMBL:AAN68066.1};
- **Gene Information:** Name=rbsB {ECO:0000313|EMBL:AAN68066.1}; OrderedLocusNames=PP_2454 {ECO:0000313|EMBL:AAN68066.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial solute-binding protein 2 family.
- **Key Domains:** Peripla_BP_I. (IPR028082); SBP_2_dom. (IPR025997); Peripla_BP_4 (PF13407)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rbsB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rbsB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rbsB** (gene ID: rbsB, UniProt: Q88K38) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RbsB (PP_2454, Q88K38): Periplasmic D-Ribose-Binding Protein of a High-Affinity ABC Importer in *Pseudomonas putida* KT2440

## Summary

**RbsB (gene *rbsB*, ordered locus PP_2454, UniProt Q88K38) is the periplasmic, non-catalytic substrate-binding protein (SBP) of a high-affinity D-ribose ATP-binding cassette (ABC) import system in *Pseudomonas putida* KT2440.** Its molecular job is to scavenge free D-ribose in the periplasmic space and, through a large ligand-induced "Venus-flytrap" hinge-bending closure, present the captured sugar to the cognate membrane permease (RbsC) so that the ATPase (RbsA) can power its translocation into the cytoplasm. RbsB itself catalyzes no chemical reaction — it is a receptor/adapter whose function is molecular recognition and delivery. This identity rests on three independent lines of evidence: (1) *rbsB* heads a complete, dedicated ribose operon encoding every component needed to import and catabolize D-ribose; (2) the protein is a clear ortholog (39.7% identity) of the structurally and biochemically characterized *E. coli* ribose-binding protein, with near-complete conservation of the ribose-contacting pocket residues; and (3) the operon is controlled by a dedicated ribose-responsive LacI-family repressor (RbsR), the classic regulatory signature of a sugar-specific catabolic import module.

Functionally, RbsB operates **in the periplasm**. It is synthesized with an N-terminal Sec signal peptide (residues 1–29) that is cleaved to yield the mature periplasmic chain (residues 30–319), a single bilobed periplasmic-binding-protein domain. Downstream of binding, imported D-ribose is phosphorylated to ribose-5-phosphate by ribokinase (RbsK, EC 2.7.1.15), feeding directly into the pentose-phosphate pathway. The operon also carries a D-ribose pyranase (RbsD, EC 5.4.99.62) that interconverts the pyranose and furanose ring forms of ribose, and a ribonucleoside hydrolase that can liberate free ribose from nucleosides.

The primary role is therefore **transport-associated substrate capture, not enzymatic catalysis**. In addition to its transport role, homologous ribose-binding proteins in *E. coli* double as the receptor for ribose chemotaxis, feeding ligand-bound protein to the Trg chemoreceptor. This secondary role is plausible for *P. putida* RbsB by orthology — and KEGG maps PP_2454 to the bacterial chemotaxis pathway — but it has not been experimentally demonstrated in *P. putida* and remains an inference. **Gene-identity verification: PASSED** — the symbol *rbsB*, organism, protein family (bacterial solute-binding protein 2), and domains (Peripla_BP_I / SBP_2 / PF13407) are all mutually consistent, and PP_2454 sits inside a complete, canonical *rbs* operon; there is no evidence of gene-symbol ambiguity.

---

## Key Findings

### Finding 1 — *rbsB* is the substrate-binding subunit of a complete, dedicated D-ribose ABC import operon

The genomic context of PP_2454 in *P. putida* KT2440 (KEGG genome `ppu`) reveals a canonical, contiguous *rbs* operon in which every functional element of a ribose import-and-catabolism module is present and adjacent:

| Locus | Gene | KEGG KO | Product | Function |
|-------|------|---------|---------|----------|
| PP_2454 | **rbsB** | K10439 | Ribose ABC transporter substrate-binding protein | Periplasmic D-ribose capture (**target of this report**) |
| PP_2455 | rbsA | K10441 | ABC transporter ATP-binding protein (EC 7.5.2.7) | ATP hydrolysis powering transport |
| PP_2456 | rbsC | K10440 | Membrane permease | Transmembrane translocation channel |
| PP_2457 | rbsR | K02529 | LacI-family transcriptional repressor | Ribose-responsive regulation |
| PP_2458 | rbsK | K00852 | Ribokinase (EC 2.7.1.15) | D-ribose → D-ribose-5-phosphate |
| PP_2459 | rbsD | K06726 | D-ribose pyranase (EC 5.4.99.62) | Pyranose/furanose interconversion |
| PP_2460 | — | — | Ribonucleoside hydrolase | Ribose release from nucleosides |

This is the textbook architecture of a bacterial pentose-import operon. The co-localization of a solute-binding protein, an ATPase, a permease, a dedicated repressor, and the downstream catabolic kinase is diagnostic: RbsB cannot be a stand-alone enzyme, because the operon supplies no active site to it and instead surrounds it with a transport apparatus and a phosphorylating enzyme. UniProt assigns Q88K38 to KEGG orthology **K10439, "ribose transport system substrate-binding protein,"** and to Pfam **PF13407 (Peripla_BP_4 / SBP_2 domain)** with InterPro signatures **IPR028082 (Periplasmic binding protein-like I)** and **IPR025997 (SBP_2)** — exactly the fold family used by periplasmic sugar receptors. The presence of ribokinase and D-ribose pyranase in the operon leaves no reasonable alternative substrate: the module is dedicated to D-ribose acquisition and catabolism. Collectively this establishes RbsB as the periplasmic recognition component of the RbsABC importer.

### Finding 2 — RbsB is a periplasmic "Venus-flytrap" receptor that binds D-ribose and delivers it to the permease

RbsB belongs to the periplasmic binding protein (PBP) superfamily, whose members all operate by the same physical principle: two α/β domains connected by a hinge close around the ligand like a Venus flytrap, and downstream partners (the ABC permease and, in some systems, the chemoreceptor) recognize only the closed, ligand-bound conformation.

Several features anchor this interpretation for Q88K38. First, the protein carries a cleaved N-terminal signal peptide (residues 1–29), producing a mature chain (residues 30–319) that resides in the **periplasm / cell envelope** — the correct compartment for a receptor that must intercept sugar after it crosses the outer membrane but before it reaches the inner-membrane transporter. Second, the mature protein consists essentially of a single periplasmic-binding-protein domain (≈ residues 35–299), consistent with the two-lobe SBP architecture.

The mechanistic paradigm comes from the *E. coli* ribose-binding protein (RBP), which is periplasmic and "binds to ribose and mediates transport and chemotaxis" ([PMID: 8878033](https://pubmed.ncbi.nlm.nih.gov/8878033/)). Structural studies of RBP and close homologs show that binding is coupled to a large open→closed hinge-bending domain motion. Elastic-network modelling of *E. coli* RBP identifies discrete hinge residues (Ser103, Gln235, Asp264) about which the two domains rotate, bend, and twist as rigid bodies, generating the closed ligand-bound state while the internal structure of each domain remains largely intact ([PMID: 23698778](https://pubmed.ncbi.nlm.nih.gov/23698778/)). The crystal structure of the *Thermotoga maritima* ribose-binding protein — 39% identical to *E. coli* RBP — confirms that polar ligand interactions and the global ligand-induced conformational change are conserved across large evolutionary distances, even when local side-chain rearrangements differ ([PMID: 19019243](https://pubmed.ncbi.nlm.nih.gov/19019243/)). The same hinge-closure mechanism, with variations in hinge residues, is documented for the related glucose/galactose-binding protein ([PMID: 17473016](https://pubmed.ncbi.nlm.nih.gov/17473016/)) and the D-allose-binding protein ([PMID: 11825912](https://pubmed.ncbi.nlm.nih.gov/11825912/)), demonstrating this is the universal operating mode for the receptor class. KEGG maps PP_2454 to both **ppu02010 (ABC transporters)** and **ppu02030 (bacterial chemotaxis)**, mirroring the dual transport/taxis role established for the *E. coli* ortholog.

### Finding 3 — RbsB is a clear ortholog of *E. coli* ribose-binding protein with a conserved D-ribose-binding pocket

A Needleman–Wunsch global alignment of Q88K38 (*P. putida*, 319 aa) against P02925 (*E. coli* RbsB, 296 aa) yields **115/290 identical positions = 39.7% identity** over the aligned length — comfortably within the orthology range and essentially identical to the *E. coli*/*T. maritima* RBP relationship (39%) that preserves full ribose-binding function. Critically, the residues that directly contact ribose in the *E. coli* structure are conserved in the *P. putida* protein:

| *E. coli* RBP residue | *P. putida* RbsB residue | Conserved? |
|-----------------------|--------------------------|-----------|
| Asn13 | Asn44 | ✔ |
| Phe15 | Phe46 | ✔ |
| Asp89 | Asp130 | ✔ |
| Arg90 | Leu131 | ✘ (substituted) |
| Arg141 | Arg183 | ✔ |
| Asn190 | Asn232 | ✔ |
| Asp215 | Asp258 | ✔ |
| Gln235 | Gln278 | ✔ |

Seven of eight ribose-contacting residues are conserved (the single exception being Arg90→Leu131). This degree of pocket conservation strongly supports **D-ribose as the physiological substrate** of *P. putida* RbsB — direct structural-bioinformatic evidence independent of the genomic-context argument. Both proteins share the SBP_2 (Peripla_BP) fold and carry an N-terminal Sec signal peptide directing periplasmic export. Because these pocket residues form the hydrogen-bonding network that reads out the specific stereochemistry of the ribose sugar, their conservation across a large evolutionary distance is far stronger evidence of substrate identity than overall sequence similarity alone. An AlphaFold model (AlphaFoldDB Q88K38) is expected to reproduce the bilobed PBP fold.

### Finding 4 — The operon is controlled by a dedicated ribose-responsive LacI-family repressor (RbsR)

Within the *rbs* operon, PP_2457 (*rbsR*) encodes a LacI-family transcriptional repressor (KEGG K02529). In characterized homologs, RbsR represses the ribose gene cluster and its DNA-binding activity is relieved by a ribose-derived effector, providing tight, substrate-inducible control of RbsB expression:

- In *Bifidobacterium breve* UCC2003, "the promoter upstream of rbsABCDK is negatively controlled by RbsR(His) binding to an 18 bp inverted repeat and that RbsR(His) binding activity is modulated by D-ribose" ([PMID: 21255330](https://pubmed.ncbi.nlm.nih.gov/21255330/)). The same study confirmed that the operon's ribokinase specifically phosphorylates D-ribose to ribose-5-phosphate (EC 2.7.1.15), cementing the pathway logic.
- In *Corynebacterium glutamicum* ATCC 13032, RbsR represses the *rbsRACBD* operon; deletion of *rbsR* increases operon mRNA, and the physiological effector is likely **ribose-5-phosphate** (or a derivative), since a ribokinase double mutant shows no derepression by ribose ([PMID: 19118356](https://pubmed.ncbi.nlm.nih.gov/19118356/)). Deletion of the structural genes *rbsACBD* abolished ribose uptake, directly linking this gene set to ribose transport.

The presence of a dedicated, co-transcribed RbsR repressor is a hallmark of a substrate-specific sugar-import module: RbsB is produced on demand when ribose (or its phosphorylated derivative) is available, as expected for a high-affinity scavenging receptor rather than a constitutively expressed housekeeping protein. This mirrors the broader *P. putida* KT2440 strategy of dedicated LacI/GntR-type transcription factors controlling clustered catabolic genes ([PMID: 39589324](https://pubmed.ncbi.nlm.nih.gov/39589324/)).

---

## Mechanistic Model / Interpretation

The four findings converge on a single, coherent mechanistic picture in which RbsB is the entry-point receptor of a linear import-then-catabolize pathway:

```
   PERIPLASM                            INNER MEMBRANE            CYTOPLASM
 ┌───────────────┐
 │  D-ribose     │
 │  (free sugar) │
 └──────┬────────┘
        │  capture (Venus-flytrap closure)
        ▼
 ┌───────────────┐        open→closed
 │   RbsB        │  ──────hinge motion──────►  delivers closed,
 │  (PP_2454)    │                              ligand-bound form
 │  periplasmic  │                                     │
 │  SBP          │                                     ▼
 └───────────────┘                        ┌────────────────────────┐
                                          │  RbsC permease (PP_2456)│
                                          │  channel in membrane    │
                                          └───────────┬────────────┘
                                                      │  ATP-driven translocation
                                          ┌───────────▼────────────┐
                                          │  RbsA ATPase (PP_2455)  │
                                          │  EC 7.5.2.7             │
                                          └───────────┬────────────┘
                                                      ▼
                                        D-ribose in cytoplasm
                                                      │
                              RbsD pyranase (PP_2459) │  ring interconversion
                              EC 5.4.99.62            ▼  (pyranose ⇌ furanose)
                                        RbsK ribokinase (PP_2458)
                                              EC 2.7.1.15
                                                      │
                                                      ▼
                                          D-ribose-5-phosphate
                                                      │
                                                      ▼
                                        PENTOSE-PHOSPHATE PATHWAY
                                        (nucleotide biosynthesis,
                                         NADPH, central metabolism)

  Regulation:  RbsR (PP_2457, LacI-family) represses the whole operon;
               ribose / ribose-5-phosphate relieves repression (induction).
```

**Step-by-step interpretation:**

1. **Recognition (periplasm).** Free D-ribose that has crossed the outer membrane is captured by RbsB. The two lobes of the SBP fold close around the sugar via a hinge-bending motion, forming a high-affinity, stereospecific complex. The conserved pocket residues (Asn44, Phe46, Asp130, Arg183, Asn232, Asp258, Gln278) hydrogen-bond and stack against the ribose ring, enforcing selectivity for ribose over other sugars.

2. **Delivery (inner membrane).** Only the closed, ligand-loaded conformation of RbsB is recognized by the RbsC permease. This conformational proofreading ensures the transporter fires only when cargo is present.

3. **Translocation (across the inner membrane).** RbsC provides the transmembrane pathway; RbsA hydrolyzes ATP (EC 7.5.2.7) to power import of D-ribose into the cytoplasm.

4. **Catabolic commitment (cytoplasm).** RbsD (D-ribose pyranase, EC 5.4.99.62) equilibrates the ring forms of ribose to supply the substrate configuration preferred by the kinase. RbsK (ribokinase, EC 2.7.1.15) then phosphorylates D-ribose to D-ribose-5-phosphate, which is simultaneously a metabolic trap (preventing efflux) and the entry metabolite for the pentose-phosphate pathway, nucleotide biosynthesis, and NADPH generation. In *P. putida*, which relies on the Entner–Doudoroff pathway rather than glycolysis for hexose catabolism, ribose-5-phosphate provides biosynthetic precursors and, through PPP interconversions, carbon/energy.

5. **Regulation (transcription).** The LacI-family repressor RbsR keeps the operon off in the absence of ribose. When ribose (or ribose-5-phosphate) accumulates, it binds RbsR, relieving repression and inducing synthesis of the whole module — including RbsB.

Within this model, **RbsB's precise role is molecular recognition and hand-off**: it is the affinity-determining, specificity-conferring receptor that converts the presence of extracellular ribose into a productive transport event. It performs no chemistry itself; its "output" is a conformational signal (the closed state) that licenses transport. The location of its function is unambiguously the **periplasm/cell envelope**. Its pathway membership is **carbohydrate (pentose) uptake and catabolism feeding the pentose-phosphate pathway**, with a plausible but unconfirmed secondary role in **ribose chemotaxis**.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|---------------------|------------------------------|
| [8878033](https://pubmed.ncbi.nlm.nih.gov/8878033/) | *Genetically probing the regions of ribose-binding protein involved in permease interaction* | Establishes the *E. coli* RBP paradigm: periplasmic, "binds to ribose and mediates transport and chemotaxis"; identifies distinct surface regions for permease vs. chemoreceptor interaction. Anchors the dual transport/taxis role and receptor-adapter function (F002). |
| [23698778](https://pubmed.ncbi.nlm.nih.gov/23698778/) | *Analysis of conformational motions ... for E. coli ribose-binding protein (elastic network models)* | Defines the open→closed hinge-bending mechanism and hinge residues (Ser103, Gln235, Asp264); domains move as rigid bodies. Mechanistic basis for the Venus-flytrap model (F002). |
| [19019243](https://pubmed.ncbi.nlm.nih.gov/19019243/) | *Ligand-induced conformational changes in a thermophilic ribose-binding protein* | *T. maritima* RBP is 39% identical to *E. coli* RBP yet conserves polar ligand interactions and global conformational change — validating conservation of ribose binding at ~40% identity, precisely the *P. putida*/*E. coli* relationship (F002, F003). |
| [17473016](https://pubmed.ncbi.nlm.nih.gov/17473016/) | *Conformational changes of glucose/galactose-binding protein ...* | Independent PBP-superfamily example confirming hinge-bending closure mediates ligand binding, transport, and signaling; hinge residues vary between family members (F002). |
| [11825912](https://pubmed.ncbi.nlm.nih.gov/11825912/) | *Hinge-bending motion of D-allose-binding protein from E. coli* | Closely related receptor; open and closed structures show torsional hinge changes with intact domains, and explicitly contrasts with ribose-binding protein's pattern — reinforces the family mechanism (F002). |
| [19118356](https://pubmed.ncbi.nlm.nih.gov/19118356/) | *Characterization of the LacI-type repressor RbsR ... in C. glutamicum* | Deletion of *rbsACBD* abolishes ribose uptake (transport function); RbsR represses the *rbs* operon and is derepressed via ribose-5-phosphate. Supports F001 (transport operon) and F004 (RbsR regulation, effector identity). |
| [21255330](https://pubmed.ncbi.nlm.nih.gov/21255330/) | *Ribose utilization by ... Bifidobacterium breve UCC2003* | *rbsACBDK* cluster essential for ribose utilization; RbsR binds an 18-bp inverted repeat and is modulated by D-ribose; RbsK is a D-ribose-specific ribokinase (EC 2.7.1.15). Supports F001, F004, and the downstream phosphorylation step. |
| [39589324](https://pubmed.ncbi.nlm.nih.gov/39589324/) | *GnuR represses glucose and gluconate catabolism in P. putida KT2440* | *P. putida* KT2440 regulatory context: clustered catabolic genes controlled by dedicated LacI/GntR-type TFs, and Entner–Doudoroff-centric metabolism — consistent with the RbsR-controlled *rbs* cluster architecture (F004, background). |
| [36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/) | *Glucose-6-phosphate dehydrogenase ZwfA in Pseudomonas* | Background on *Pseudomonas* central carbon metabolism (Entner–Doudoroff and oxidative pentose-phosphate pathways), the downstream destination of imported ribose-derived ribose-5-phosphate (mechanistic context). |

**Overall weight of evidence.** The identity of RbsB as a periplasmic D-ribose-binding transport protein is supported by convergent structural, evolutionary, genomic, and regulatory evidence. The *direct* experimental characterization comes from orthologs (*E. coli*, *T. maritima*, *B. breve*, *C. glutamicum*), while the *P. putida*-specific evidence is bioinformatic/comparative (operon structure, sequence orthology, pocket conservation, domain assignment). No evidence contradicts the ribose-binding assignment.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on *P. putida* Q88K38.** There is no published purification, binding assay (e.g., ITC/fluorescence Kd for D-ribose), or crystal structure of the *P. putida* protein specifically. Substrate identity is inferred from orthology and pocket conservation, not measured directly in this organism.

2. **One binding-pocket residue is not conserved.** The *E. coli* Arg90 is replaced by Leu131 in *P. putida* RbsB. In *E. coli*, Arg90 participates in ribose coordination; its substitution could subtly alter affinity or specificity. Whether *P. putida* RbsB retains identical ribose affinity, or has shifted specificity (e.g., toward a ribose analog or related pentose), is untested.

3. **The chemotaxis role is inferred, not demonstrated.** KEGG maps PP_2454 to the chemotaxis pathway and the *E. coli* ortholog serves the Trg chemoreceptor, but *P. putida* KT2440 has a different chemoreceptor repertoire, and no ribose-taxis phenotype linked to RbsB has been reported. Treat the secondary signaling role as a hypothesis.

4. **RbsR effector and operator not mapped in *P. putida*.** The physiological inducer (D-ribose vs. ribose-5-phosphate) and the operator sequence for PP_2457 RbsR are inferred from *C. glutamicum*/*B. breve* homologs, not experimentally defined in KT2440.

5. **Physiological relevance of ribose to *P. putida* growth is unquantified.** It is unknown how strongly KT2440 relies on ribose as a carbon source, whether the *rbs* operon is induced under laboratory or environmental conditions, or whether the ribonucleoside hydrolase (PP_2460) supplies ribose from nucleoside salvage as the primary in vivo substrate source.

6. **Signal-peptide and localization boundaries are predicted.** The signal peptide (1–29) and mature-chain boundaries derive from UniProt sequence-based prediction; periplasmic localization, while highly likely, has not been experimentally confirmed for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Direct binding measurement.** Overexpress and purify mature RbsB (residues 30–319, His-tagged) and measure D-ribose affinity by isothermal titration calorimetry or intrinsic/extrinsic fluorescence. Include a panel of related sugars (D-arabinose, D-xylose, D-ribose-5-phosphate, D-allose, D-glucose) to define specificity and test whether the Arg90→Leu131 substitution has shifted selectivity.

2. **Structure determination.** Solve the crystal or cryo-EM structure of RbsB in apo and ribose-bound states to confirm the two-lobe SBP fold, verify the hinge-bending closure, and directly visualize the ribose-contact residues (Asn44, Phe46, Asp130, Arg183, Asn232, Asp258, Gln278). AlphaFold modelling plus docking would be a rapid first pass.

3. **Genetic transport phenotype.** Construct a clean *rbsB* (PP_2454) deletion in KT2440 and assay growth on D-ribose as sole carbon source and labeled-ribose uptake rates, with complementation. Compare against Δ*rbsA*/Δ*rbsC* to confirm the SBP is essential for high-affinity uptake.

4. **Regulation.** Map the RbsR (PP_2457) operator by EMSA/DNase footprinting on the *rbsB* promoter, determine the effector (ribose vs. ribose-5-phosphate) using ribokinase-mutant backgrounds, and quantify operon induction by RT-qPCR/RNA-seq during growth on ribose vs. glucose.

5. **Chemotaxis test.** Perform capillary or plate chemotaxis assays with D-ribose gradients in wild-type vs. Δ*rbsB* KT2440 to determine whether RbsB contributes to ribose taxis, and identify the candidate chemoreceptor partner.

6. **Substrate source in vivo.** Test whether the co-operonic ribonucleoside hydrolase (PP_2460) supplies ribose from nucleosides by comparing growth/uptake on ribose vs. ribonucleosides in relevant mutants, clarifying the ecological/physiological role of the module.

---

*Conclusion.* All available evidence — operon architecture, ortholog-level sequence identity with conserved binding-pocket residues, SBP_2/Peripla_BP domain assignment, periplasmic localization signal, and dedicated RbsR regulation — identifies RbsB (PP_2454, Q88K38) as the periplasmic D-ribose-binding receptor of the RbsABC high-affinity ABC importer in *Pseudomonas putida* KT2440. It is a non-catalytic substrate-recognition/adapter protein that captures D-ribose in the periplasm and delivers it to the membrane permease for ATP-driven import into a ribokinase-terminated catabolic pathway feeding the pentose-phosphate pathway, with a plausible but experimentally unconfirmed secondary role in ribose chemotaxis.


## Artifacts

- [OpenScientist final report](rbsB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rbsB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8878033
2. PMID:23698778
3. PMID:19019243
4. PMID:17473016
5. PMID:11825912
6. PMID:21255330
7. PMID:19118356
8. PMID:39589324