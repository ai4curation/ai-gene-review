---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T04:00:28.046675'
end_time: '2026-08-13T04:11:35.480717'
duration_seconds: 667.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ssuB
  gene_symbol: ssuB
  uniprot_accession: Q88R93
  protein_description: 'RecName: Full=Aliphatic sulfonates import ATP-binding protein
    SsuB {ECO:0000255|HAMAP-Rule:MF_01724}; EC=7.6.2.14 {ECO:0000255|HAMAP-Rule:MF_01724};'
  gene_info: Name=ssuB {ECO:0000255|HAMAP-Rule:MF_01724}; OrderedLocusNames=PP_0240;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC transporter superfamily. Aliphatic
  protein_domains: AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439);
    ABC_transporter-like_CS. (IPR017871); ABC_transporter_ATP-bind. (IPR050166); P-loop_NTPase.
    (IPR027417)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ssuB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ssuB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R93
- **Protein Description:** RecName: Full=Aliphatic sulfonates import ATP-binding protein SsuB {ECO:0000255|HAMAP-Rule:MF_01724}; EC=7.6.2.14 {ECO:0000255|HAMAP-Rule:MF_01724};
- **Gene Information:** Name=ssuB {ECO:0000255|HAMAP-Rule:MF_01724}; OrderedLocusNames=PP_0240;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC transporter superfamily. Aliphatic
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); ABC_transporter_ATP-bind. (IPR050166); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ssuB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ssuB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ssuB** (gene ID: ssuB, UniProt: Q88R93) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: SsuB (Q88R93, PP_0240) — Aliphatic Sulfonate Import ATP-Binding Protein of *Pseudomonas putida* KT2440

## Summary

**SsuB (UniProt Q88R93; locus PP_0240) is the cytoplasmic ATP-binding and ATP-hydrolyzing subunit — the "motor" nucleotide-binding domain (NBD) — of the SsuABC ABC-type importer that actively translocates aliphatic (organo-)sulfonates across the inner membrane of *Pseudomonas putida* KT2440.** Its single, well-defined molecular function is to bind and hydrolyze ATP (EC 7.6.2.14), converting chemical energy into the conformational cycling that drives substrate transport. SsuB does not itself recognize or bind the sulfonate substrate; that role belongs to the periplasmic solute-binding protein SsuA (PP_0237) and the integral-membrane permease SsuC (PP_0239). SsuB supplies the energy that couples these components together.

The physiological purpose of this transport system is **sulfur scavenging under sulfate starvation**. When *P. putida* is deprived of its preferred sulfur sources (inorganic sulfate and cysteine), it induces the *ssuEADCB(F)* operon to import and metabolize alternative organosulfur compounds — in particular aliphatic sulfonates such as methanesulfonate and other alkanesulfonates. Once imported by SsuABC, these compounds are desulfonated in the cytoplasm by the two-component FMNH₂-dependent monooxygenase system SsuD/SsuE, releasing sulfite for assimilation into cysteine and downstream sulfur-containing biomolecules. SsuB therefore sits at the entry point of this pathway, at the cytoplasmic face of the inner membrane.

Expression of the entire *ssu* system is tightly controlled: it is a member of the **sulfate-starvation-induced (SSI) stimulon** and is governed by the LysR-type master regulator **CysB**, being repressed in the presence of sulfate/cysteine and derepressed upon sulfur limitation. The functional assignment of SsuB rests on strong convergent evidence: (i) sequence analysis showing all canonical ABC-ATPase catalytic motifs; (ii) genetic studies in closely related *P. putida* strains (S-313 and DS1) demonstrating that disruption of the *ssu* operon abolishes growth on aliphatic sulfonates; (iii) mechanistic understanding of the ABC-importer family exemplified by the maltose transporter MalFGK₂; and (iv) HAMAP/UniProt curation assigning a defined 2:2:1 (SsuB:SsuC:SsuA) complex stoichiometry. Direct biochemical characterization of the KT2440 SsuB protein itself has not been reported, so its function is assigned by robust homology and operon-context inference rather than by protein-specific enzymology.

---

## Key Findings

### Finding 1 — SsuB is the ATP-hydrolyzing subunit of the SsuABC aliphatic sulfonate ABC importer

SsuB is a 270-amino-acid protein encoded by locus PP_0240 in *P. putida* KT2440 and annotated as the ABC-transporter ATP-binding protein of the *ssu* (sulfonate utilization) system, carrying EC number 7.6.2.14 (ABC-type aliphatic-sulfonate transporter, ATP-hydrolyzing). Sequence analysis confirms a single canonical nucleotide-binding domain (the ABC domain spanning approximately residues 17–238) that contains every diagnostic motif of a functional ABC ATPase:

| Motif | Sequence | Approx. residues | Function |
|---|---|---|---|
| Walker A / P-loop | GRSGCGKS | 49–56 | ATP phosphate binding (annotated ATP-binding site) |
| ABC signature (C-loop) | LSGGQ | ~138 | Hallmark of the ABC transporter family; couples the two NBDs |
| Walker B | LLLLDE | ~158 | Coordinates Mg²⁺ and activates the catalytic water for ATP hydrolysis |
| Switch region | VTHD (His) | ~172 | γ-phosphate sensing; conformational switch |

The presence of an intact Walker A, ABC signature, Walker B, and switch histidine is definitive for a catalytically active ABC ATPase. Within the *ssuEADCB(F)* operon, the division of labor is clear: **ssuC** encodes the integral-membrane permease that forms the translocation channel; **ssuA** encodes the periplasmic (solute-binding) protein that captures the sulfonate substrate; and **ssuB** provides the two cytoplasmic ATPase subunits that energize the transport cycle.

This assignment is directly supported by the original identification of the operon in *P. putida* S-313, which described "*the ssuEADCBF operon, which contained genes for an ATP-binding cassette-type transporter (ssuABC), a two-component reduced flavin mononucleotide-dependent monooxygenase (ssuED)*" ([PMID: 10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/)). Work in *Corynebacterium glutamicum* independently confirmed the three-component architecture, noting that "*the clustered genes ssuC, ssuB, and ssuA, putatively encoding the components of an ABC-type transporter system, are required for the utilization of aliphatic sulfonates*" ([PMID: 16204527](https://pubmed.ncbi.nlm.nih.gov/16204527/)). The mechanistic role of the ATPase subunit is grounded in the broader ABC-transporter literature: "*ATP-binding cassette (ABC) transporters use the energy of ATP hydrolysis to transport a large diversity of molecules actively across biological membranes*" ([PMID: 31560984](https://pubmed.ncbi.nlm.nih.gov/31560984/)). In the maltose importer paradigm, this ATPase role is played by the MalK dimer — the structural and functional homolog of the SsuB dimer.

### Finding 2 — The SsuABC transporter imports aliphatic sulfonates as a sulfur source; the substrate is desulfonated intracellularly by the SsuD monooxygenase

The biological purpose of SsuABC-mediated transport is to deliver aliphatic sulfonates into the cytoplasm, where the sulfur atom is liberated for assimilation. Genetic evidence from *P. putida* S-313 is decisive: transposon insertions distributed across the *ssuEADCBF* operon — including the *ssuABC* transporter genes — abolished growth on a range of organosulfur compounds, and the pleiotropic phenotype was complemented by the intact operon. Specifically, these mutants "*were also deficient in growth with a variety of other organosulfur sources, including aromatic and aliphatic sulfate esters, methionine, and aliphatic sulfonates other than the natural sulfonates taurine and cysteate*" ([PMID: 10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/)). This establishes that an intact *ssu* operon — SsuB included — is required for utilization of aliphatic sulfonates and other organosulfur sources.

The transporter operates upstream of intracellular desulfonation. SsuD is an FMNH₂-dependent alkanesulfonate monooxygenase that cleaves the carbon–sulfur bond of the imported sulfonate, releasing sulfite; SsuE is the NAD(P)H-dependent FMN reductase that supplies reduced flavin to SsuD. In *P. putida* DS1, studies of dimethyl sulfide (DMS) catabolism demonstrated that "*Disruption of ssuD and SsuD enzymatic activity demonstrated that methanesulfonate is a metabolic intermediate of DMS and desulfonated by SsuD. Disruption of ssuC or ssuF also led to a DMS-utilization-defective phenotype*" ([PMID: 12835925](https://pubmed.ncbi.nlm.nih.gov/12835925/)). This places the SsuABC transporter (via the *ssuC* permease phenotype) directly in the pathway that imports methanesulfonate for SsuD-mediated desulfonation. The logical role of SsuB is to energize the import step that precedes this cytoplasmic C–S bond cleavage.

Notably, the *ssu* system handles *aliphatic* sulfonates that are not the "natural" sulfonates taurine and cysteate — the latter are transported and metabolized by a distinct taurine (*tau*) system. This substrate distinction is a defining feature of the aliphatic-sulfonate (*ssu*) pathway and is reflected in the HAMAP rule name for SsuB ("Aliphatic sulfonates import ATP-binding protein").

### Finding 3 — The *ssu* system is a sulfate-starvation-induced regulon controlled by the master regulator CysB

SsuB is not expressed constitutively; the entire *ssu* system is induced only when the cell is starved for its preferred sulfur sources. This regulatory logic was first established in *Escherichia coli*, where the *tauABCD* and *ssuEADCB* clusters "*are required for the utilization of taurine and alkanesulfonates as sulfur sources and are expressed only under conditions of sulfate or cysteine starvation*" ([PMID: 10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/)). The same principle applies in *P. putida*.

In *P. putida*, the sulfate-starvation response is governed by the LysR-type transcriptional regulator **CysB**, acting as the master regulator atop a hierarchical control system. Studies of the methylsulfur (*sfn*) regulon showed that "*CysB is a master regulator that controls the sulfate starvation response of the sfn operons, as is the case for the sulfonate utilization genes of Escherichia coli*" ([PMID: 18456803](https://pubmed.ncbi.nlm.nih.gov/18456803/)). CysB thus controls the sulfonate/organosulfur utilization genes — including the *ssu* operon — as part of the sulfate-starvation-induced (SSI) stimulon, while a secondary σ⁵⁴-dependent regulator SfnR governs the more specialized methylsulfur branch. Physiological studies of *P. putida* S-313 further demonstrated that the *ssu* locus is part of the SSI stimulon and that organosulfur utilization is repressed by sulfate/cysteine and derepressed upon sulfur limitation, with a defined hierarchy of preferred versus scavenged sulfur sources ([PMID: 8800815](https://pubmed.ncbi.nlm.nih.gov/8800815/)). This regulatory context is important for interpreting SsuB's function: it operates specifically as a sulfur-scavenging device, activated only when the cell must extract sulfur from organosulfonates.

### Finding 4 — KT2440-specific genomic evidence: *ssuB* (PP_0240) is the terminal ATPase gene of an intact *ssuEADCB* operon, with a curated 2:2:1 complex stoichiometry

Direct analysis of the *P. putida* KT2440 genome confirms that all cognate components of a functional sulfonate-utilization system are present and organized in a single operon (PP_0236–PP_0240):

| Locus | Gene | Product | KEGG ortholog | EC / notes |
|---|---|---|---|---|
| PP_0236 | *ssuE* | NAD(P)H-dependent FMN reductase | K00299 | Supplies FMNH₂ to SsuD |
| PP_0237 | *ssuA* | Sulfonate solute-binding protein | K15553 | Periplasmic; "transport of isethionate" |
| PP_0238 | *ssuD* | Alkanesulfonate monooxygenase | K04091 | EC 1.14.14.5; C–S bond cleavage |
| PP_0239 | *ssuC* | ABC transporter permease | K15554 | Integral inner-membrane channel |
| **PP_0240** | ***ssuB*** | **ABC transporter ATP-binding protein** | **K15555** | **EC 7.6.2.14; the NBD/ATPase** |

UniProt/HAMAP rule **MF_01724** curation states that SsuB is "*Part of the ABC transporter complex SsuABC involved in aliphatic sulfonates import. Responsible for energy coupling to the transport system,*" and specifies a complex stoichiometry of **two ATP-binding proteins (SsuB), two transmembrane proteins (SsuC), and one solute-binding protein (SsuA)** — i.e., an SsuB₂SsuC₂SsuA₁ assembly typical of type I ABC importers. The subcellular location is the **cell inner membrane, as a peripheral membrane protein** on the cytoplasmic face. The GO annotations reinforce this functional picture: alkanesulfonate transmembrane transport (GO:0042918), ATP binding (GO:0005524), and ATP hydrolysis (GO:0016887). Domain/family assignments (eggNOG COG1116; Pfam PF00005, ABC_tran) place SsuB firmly within the ABC-transporter ATPase superfamily.

---

## Mechanistic Model / Interpretation

SsuB functions as one of two identical ATPase subunits that form the cytoplasmic motor of a **type I ABC importer**. The transport cycle, inferred from the well-studied maltose importer (MalFGK₂-E) paradigm and applicable to SsuABC by homology, can be represented as follows:

```
        PERIPLASM
   ┌─────────────────────────────────────────────┐
   │   Aliphatic sulfonate (e.g. methanesulfonate)│
   │            │                                  │
   │            ▼                                  │
   │        [ SsuA ]  ← periplasmic binding protein│
   │            │  captures substrate, docks onto  │
   │            │  permease                         │
   ══════════════════════════════════════════════════  INNER MEMBRANE
   │        [ SsuC | SsuC ]  ← permease (channel)  │
   │            │        │                          │
   │        [ SsuB ]  [ SsuB ]  ← ATPase dimer (NBD)│
   │          ATP        ATP                        │
   │           └──hydrolysis──┘                     │
        CYTOPLASM   │
                    ▼
        Sulfonate released into cytoplasm
                    │
                    ▼
       [ SsuD + SsuE ]  → desulfonation (C–S cleavage)
                    │
                    ▼
              Sulfite (SO₃²⁻)
                    │
                    ▼
        Assimilation → cysteine → sulfur metabolism
```

**Step-by-step mechanism (by analogy to MalFGK₂-E):**

1. **Substrate capture.** The periplasmic binding protein SsuA scavenges an aliphatic sulfonate and docks onto the periplasmic face of the SsuC permease dimer.
2. **ATP binding closes the NBD dimer.** Two ATP molecules bind at the interface of the SsuB dimer, sandwiched between the Walker A/B motifs of one SsuB and the LSGGQ signature of the partner SsuB. ATP binding drives NBD dimer closure and pushes the transporter toward the outward-facing state.
3. **Substrate translocation.** Conformational coupling through SsuC opens a cytoplasm-facing cavity; the sulfonate is released into the cytoplasm.
4. **ATP hydrolysis resets the cycle.** SsuB hydrolyzes ATP (γ-phosphate cleavage sensed by the switch histidine); Pi and ADP release reopen the NBD dimer, returning the transporter to the inward-facing resting state.

The maltose-transporter studies illuminate why the ATPase (SsuB analog, MalK) depends on the other subunits for productive turnover. Basal ATPase activity of the isolated motor is low; it is stimulated by the binding protein and substrate. As shown for MalFGK₂: "*the basal ATPase activity of MalFGK2 is very low because the cleavage of ATP is rate-limiting … open-state MalE stabilizes MalFGK2 in the outward-facing conformation until maltose triggers return to the inward-facing state for substrate and Pi release*" ([PMID: 26338707](https://pubmed.ncbi.nlm.nih.gov/26338707/)). Reciprocal transmembrane signaling ensures ATP is not wasted in the absence of substrate: "*three functionally relevant conformations are found also in the periplasmic MalF-P2 loop, strictly dependent on cytoplasmic nucleotide binding and periplasmic docking of liganded MalE*" ([PMID: 19395376](https://pubmed.ncbi.nlm.nih.gov/19395376/)). By extension, SsuB's ATP hydrolysis is expected to be coupled to and stimulated by SsuA-delivered sulfonate, providing an energy-efficient, demand-driven import mechanism.

**Integration into sulfur metabolism.** SsuB sits at the membrane entry point of the sulfur-scavenging pathway. The imported sulfonate is desulfonated by SsuD (with reduced flavin from SsuE), releasing sulfite that feeds into the cysteine-biosynthetic sulfate-assimilation pathway. The whole module is switched on only when the cell is starved for sulfate/cysteine, under CysB control. Thus SsuB's role is best summarized as: **the ATP-driven motor that admits aliphatic sulfonates into the cytoplasm so their sulfur can be harvested during sulfate starvation.**

---

## Evidence Base

| PMID | Study | How it supports the annotation |
|---|---|---|
| [10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/) | *The ssu locus plays a key role in organosulfur metabolism in P. putida S-313* | Identifies the *ssuEADCBF* operon and *ssuABC* as an ABC transporter; shows operon disruption abolishes growth on aliphatic sulfonates and other organosulfur sources. **Primary genetic evidence.** |
| [12835925](https://pubmed.ncbi.nlm.nih.gov/12835925/) | *Genes essential for dimethyl sulfide utilization in P. putida DS1* | Shows *ssuC* permease disruption causes a sulfonate-utilization defect and that methanesulfonate is desulfonated by SsuD — placing SsuABC upstream of cytoplasmic desulfonation. **Primary genetic evidence.** |
| [16204527](https://pubmed.ncbi.nlm.nih.gov/16204527/) | *ssu/seu genes of C. glutamicum in sulfonate utilization* | Confirms *ssuA/B/C* form the three-component ABC transporter required for aliphatic sulfonate utilization. **Comparative genetic evidence.** |
| [10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) | *Deletion analysis of E. coli taurine and alkanesulfonate transport systems* | Establishes that *ssu* genes are induced only under sulfate/cysteine starvation and distinguishes *ssu* (alkanesulfonate) from *tau* (taurine) systems. **Regulatory/substrate-specificity evidence.** |
| [18456803](https://pubmed.ncbi.nlm.nih.gov/18456803/) | *CysB and SfnR hierarchical regulation in P. putida* | Identifies CysB as the master regulator of the sulfate-starvation response and sulfonate-utilization genes. **Regulatory evidence in the target organism.** |
| [8800815](https://pubmed.ncbi.nlm.nih.gov/8800815/) | *Sulfur assimilation and the SSI stimulon in P. putida S-313* | Places sulfonate utilization within the sulfate-starvation-induced stimulon and defines the sulfur-source hierarchy. **Physiological context.** |
| [31560984](https://pubmed.ncbi.nlm.nih.gov/31560984/) | *An integrated transport mechanism of the maltose ABC importer* | Provides the mechanistic ABC-importer paradigm: ATP hydrolysis energizes active transport. **Mechanistic model.** |
| [26338707](https://pubmed.ncbi.nlm.nih.gov/26338707/) | *Sequential action of MalE and maltose in MalFGK2* | Explains substrate-coupled stimulation of the NBD ATPase — directly relevant to how SsuB turnover is regulated. **Mechanistic model.** |
| [19395376](https://pubmed.ncbi.nlm.nih.gov/19395376/) | *Transmembrane signaling in MalFGK2-E* | Demonstrates reciprocal NBD–permease–binding-protein communication that gates ATP hydrolysis. **Mechanistic model.** |
| [23509285](https://pubmed.ncbi.nlm.nih.gov/23509285/) | *Conformational plasticity of the type I maltose ABC importer* | Details NBD open/closed cycling coupled to nucleotide and binding-protein states. **Mechanistic model.** |
| [28267156](https://pubmed.ncbi.nlm.nih.gov/28267156/) | *MBP stabilizes the partially closed MalFGK conformation* | Supports the binding-protein-driven conformational coupling of the NBD dimer. **Mechanistic model.** |
| [15661012](https://pubmed.ncbi.nlm.nih.gov/15661012/) | *SfnR regulates the sfnFG operon for dimethyl sulphone utilization* | Context for the broader methylsulfur/sulfate-starvation regulon in P. putida DS1. **Regulatory context.** |

**Note on evidence quality:** The functional assignment of SsuB rests on a combination of (i) direct genetic evidence in closely related *P. putida* strains (S-313, DS1) and in *C. glutamicum*, showing the *ssu* transporter is required for aliphatic sulfonate utilization; (ii) definitive sequence/motif analysis identifying SsuB as a catalytically competent ABC ATPase; (iii) HAMAP/UniProt curation (rule MF_01724) assigning the complex stoichiometry and subcellular location; and (iv) a well-characterized mechanistic paradigm (MalFGK₂) for the type I ABC importer family. No study has biochemically characterized the KT2440 SsuB protein in isolation, so the specific kinetic and structural properties of this exact protein are inferred rather than measured.

---

## Limitations and Knowledge Gaps

1. **No protein-specific biochemistry for KT2440 SsuB.** There is no published in vitro measurement of ATP hydrolysis rate, Km/kcat, Mg²⁺ dependence, or crystal/cryo-EM structure for the Q88R93 protein itself. Its catalytic function is assigned by homology and motif analysis, not by direct enzymology.

2. **Substrate specificity of the KT2440 system is inferred.** The precise spectrum of aliphatic sulfonates transported by the KT2440 SsuABC complex has not been directly measured. Substrate range is inferred from S-313 and DS1 genetic studies and from the SsuA binding-protein annotation (which references isethionate/alkanesulfonates). The defining exclusion of taurine and cysteate (handled by the *tau* system) is based on cross-species work.

3. **Complex assembly not verified experimentally in KT2440.** The 2:2:1 SsuB:SsuC:SsuA stoichiometry is a HAMAP-curated inference based on the type I ABC-importer paradigm, not a directly determined structure for this organism.

4. **Operon boundaries and the *ssuF* component.** The KT2440 operon is annotated as *ssuEADCB* (PP_0236–PP_0240); the *ssuF* gene seen in S-313 (implicated in DS1 phenotypes) may or may not be present/co-regulated in KT2440, which is a minor open question about accessory factors.

5. **Regulatory fine detail.** While CysB is established as the master regulator, the exact CysB-binding site(s), inducer identity (e.g., an O-acetylserine-type coinducer), and quantitative induction kinetics for the KT2440 *ssu* promoter have not been mapped in the target strain.

---

## Proposed Follow-up Experiments / Actions

1. **Biochemical characterization of recombinant SsuB.** Express and purify Q88R93, and measure basal and SsuC/SsuA-stimulated ATPase activity (Km, kcat for ATP; Mg²⁺ dependence). Confirm the predicted role of the switch histidine and Walker B glutamate via site-directed mutagenesis (e.g., E→Q catalytically dead mutant).

2. **Reconstitution of the SsuABC complex.** Co-express SsuB, SsuC, and SsuA, reconstitute into proteoliposomes, and demonstrate ATP-dependent, SsuA-mediated uptake of defined aliphatic sulfonates (e.g., methanesulfonate, ethanesulfonate) to directly verify substrate specificity and coupling.

3. **Structural determination.** Solve the cryo-EM structure of the SsuABC complex in apo, ATP-bound, and ADP states to confirm the 2:2:1 stoichiometry and the NBD open/closed cycle predicted from the MalFGK₂ paradigm.

4. **Targeted knockout in KT2440.** Construct a clean *ssuB* (PP_0240) deletion in KT2440 and test growth on a panel of aliphatic sulfonates vs. sulfate/cysteine controls; complement with the wild-type gene to confirm the phenotype is SsuB-specific rather than polar.

5. **Regulatory mapping.** Use ChIP or EMSA to define the CysB-binding site upstream of the KT2440 *ssuE* promoter, and RT-qPCR/RNA-seq under sulfate-replete vs. sulfate-starved conditions to quantify induction and confirm CysB dependence in the target strain.

6. **Substrate-profiling.** Perform growth-based and transport-based assays across a broad organosulfur panel to delineate the exact aliphatic-sulfonate substrate range of the KT2440 system and confirm the taurine/cysteate exclusion.

---

*Report prepared from a 3-iteration autonomous investigation. Functional assignment of SsuB (Q88R93) is well supported by convergent genetic, bioinformatic, regulatory, and mechanistic evidence, with the principal gap being the absence of direct biochemical/structural characterization of this specific protein.*


## Artifacts

- [OpenScientist final report](ssuB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ssuB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10781557
2. PMID:16204527
3. PMID:31560984
4. PMID:12835925
5. PMID:10781534
6. PMID:18456803
7. PMID:8800815
8. PMID:26338707
9. PMID:19395376