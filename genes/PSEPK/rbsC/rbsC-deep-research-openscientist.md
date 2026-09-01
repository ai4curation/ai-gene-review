---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T10:23:28.438131'
end_time: '2026-08-31T11:46:00.575312'
duration_seconds: 4952.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rbsC
  gene_symbol: rbsC
  uniprot_accession: Q88K36
  protein_description: 'SubName: Full=D-ribose ABC transporter-permease subunit {ECO:0000313|EMBL:AAN68068.1};
    EC=3.6.3.17 {ECO:0000313|EMBL:AAN68068.1};'
  gene_info: Name=rbsC {ECO:0000313|EMBL:AAN68068.1}; OrderedLocusNames=PP_2456 {ECO:0000313|EMBL:AAN68068.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the binding-protein-dependent transport system
  protein_domains: ABC_transp_permease. (IPR001851); BPD_transp_2 (PF02653)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rbsC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rbsC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88K36
- **Protein Description:** SubName: Full=D-ribose ABC transporter-permease subunit {ECO:0000313|EMBL:AAN68068.1}; EC=3.6.3.17 {ECO:0000313|EMBL:AAN68068.1};
- **Gene Information:** Name=rbsC {ECO:0000313|EMBL:AAN68068.1}; OrderedLocusNames=PP_2456 {ECO:0000313|EMBL:AAN68068.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the binding-protein-dependent transport system
- **Key Domains:** ABC_transp_permease. (IPR001851); BPD_transp_2 (PF02653)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rbsC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rbsC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rbsC** (gene ID: rbsC, UniProt: Q88K36) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *rbsC* (PP_2456, UniProt Q88K36) in *Pseudomonas putida* KT2440

## Summary

**rbsC** (ordered locus **PP_2456**; UniProt **Q88K36**) of *Pseudomonas putida* KT2440 encodes the **integral inner-membrane permease subunit of the high-affinity D-ribose ATP-binding cassette (ABC) import system, RbsABC**. This assignment is supported by convergent lines of evidence: the UniProt/InterPro/Pfam annotation of Q88K36 as a binding-protein-dependent transport permease (domain BPD_transp_2, PF02653; IPR001851); its position within a complete, syntenic ribose (*rbs*) operon in the KT2440 genome; and clear sequence orthology (38% identity, 60% similarity) to the biochemically and genetically characterized *Escherichia coli* RbsC. RbsC itself has no catalytic (enzymatic) activity — despite the legacy EC number 3.6.3.17 carried on the UniProt record — because the ATP hydrolysis that powers transport is performed by the associated cytoplasmic ATPase RbsA. The historical EC 3.6.3.17 has been reclassified to EC 7.5.2.7 and assigned to the RbsA ATPase (PP_2455), not to the RbsC permease.

Functionally, RbsC forms the **transmembrane channel** through which D-ribose crosses the cytoplasmic (inner) membrane. In the well-studied *E. coli* paradigm, the transporter is a tripartite complex: a periplasmic **substrate-binding protein RbsB** captures D-ribose in the periplasm and delivers it to a **transmembrane RbsC homodimer (RbsC₂)**, while the cytoplasmic **RbsA** ATPase (with fused nucleotide-binding domains) hydrolyzes ATP to drive conformational cycling and substrate translocation into the cytoplasm. RbsC is a polytopic membrane protein (10 transmembrane helices in the definitive *E. coli* topology, with cytosolic N- and C-termini) belonging to the AraH/BtuC-like superfamily of ABC-importer membrane components. It engages the periplasmic binding protein symmetrically across the two halves of the homodimer.

Biologically, RbsC is the gateway of the ribose catabolic pathway. Once imported, D-ribose is converted by the ribose pyranase **RbsD** and the ribokinase **RbsK** into **D-ribose-5-phosphate**, which feeds the **pentose phosphate pathway** and nucleotide biosynthesis. In KT2440 the entire cassette — periplasmic binding protein (rbsB, PP_2454), ATPase (rbsA, PP_2455), permease (rbsC, PP_2456), LacI-family repressor (rbsR, PP_2457), ribokinase (rbsK, PP_2458), and pyranase (rbsD, PP_2459) — is genomically clustered, mirroring the operonic organization known from *E. coli* and confirming that PP_2456 functions as the ribose-import permease in this organism. Its site of action is the **cytoplasmic/inner membrane**, with its substrate-facing interactions occurring at the periplasmic and membrane-embedded surfaces.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and **passed**:

| Attribute | Target (UniProt Q88K36) | Confirmed in this study |
|---|---|---|
| Gene symbol | rbsC | ✔ Matches KEGG/PANTHER "ribose import permease RbsC" |
| Organism | *P. putida* KT2440 (PSEPK) | ✔ PP_2456 is a KT2440 ordered locus |
| Protein family | Binding-protein-dependent transport system permease | ✔ BPD_transp_2 (PF02653), IPR001851, COG1172 (AraH) |
| Function | D-ribose ABC transporter permease subunit | ✔ Ortholog of characterized *E. coli* RbsC (38% ID) |

The gene symbol, organism, protein family, and domain architecture are internally consistent, and the literature retrieved describes the correct molecular entity (the ribose ABC-importer permease). The functional knowledge transferred from *E. coli* is justified by quantitative orthology (see Finding F008). This is **not** a case of gene-symbol ambiguity.

---

## Key Findings

### F001 — RbsC is the integral inner-membrane permease of the high-affinity D-ribose ABC importer

UniProt Q88K36 annotates PP_2456/rbsC as a "D-ribose ABC transporter-permease subunit," and the protein belongs to the binding-protein-dependent transport system permease family, carrying the BPD_transp_2 domain (PF02653) and the ABC transporter permease signature (IPR001851). The canonical, experimentally characterized ortholog in *E. coli* defines the architecture in which RbsC operates: the ribose transporter is a **tripartite complex** consisting of a cytoplasmic ATP-binding cassette protein (RbsA, with fused nucleotide-binding domains), a transmembrane domain homodimer (RbsC₂), and a periplasmic substrate-binding protein (RbsB). Within this complex, **RbsC is the transmembrane (permease) component** and the substrate is **D-ribose**. As stated in the primary reassembly study, *"The ribose transporter in Escherichia coli is a tripartite complex consisting of a cytoplasmic ATP-binding cassette protein, RbsA, with fused nucleotide binding domains; a transmembrane domain homodimer, RbsC2; and a periplasmic substrate binding protein, RbsB"* ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)).

This is the primary functional assignment for the gene: **a substrate-translocation channel, not an enzyme.**

### F002 — RbsC works as a homodimer (RbsC₂) that symmetrically engages the periplasmic binding protein RbsB

Genetic suppressor analysis in *E. coli* mapped RbsC suppressors of transport-defective *rbsB* mutations to two regions of RbsC, each interacting with one lobe/domain of the ribose-binding protein. A tandem, head-to-tail dimeric *rbsC* construct was stable and functional for growth and ribose uptake, and the pattern of mutation–suppressor combinations was consistent with the periplasmic binding protein interacting **symmetrically with a homodimeric RbsC**. The authors concluded directly that *"the binding protein module interacts symmetrically with homodimeric RbsC"* ([PMID: 10428954](https://pubmed.ncbi.nlm.nih.gov/10428954/)). In vitro reassembly of the complex independently confirmed a transmembrane **RbsC₂** homodimer ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)). This dimeric, pseudo-two-fold-symmetric arrangement is the hallmark of ABC-importer transmembrane domains and explains how the single-lobe binding protein docks across the membrane channel to deliver its cargo.

### F003 — RbsC is a polytopic inner-membrane protein with 10 transmembrane helices and cytosolic termini (AraH/BtuC-like fold)

Cysteine-scanning combined with multiplex fluorescence labeling of 34 single-cysteine mutants established the definitive topology of *E. coli* RbsC: *"The results indicate that RbsC contains 10 transmembrane-spanning helices, with the N and C termini being in the cytosol"* ([PMID: 12923096](https://pubmed.ncbi.nlm.nih.gov/12923096/)). This topology matches the crystallized ABC-importer permease BtuC and situates RbsC firmly in the AraH superfamily of binding-protein-dependent (ABC) transporter membrane components ([PMID: 9922273](https://pubmed.ncbi.nlm.nih.gov/9922273/)). An earlier PhoA-fusion study had proposed a six-transmembrane model with cytoplasmic N- and C-termini ([PMID: 9922273](https://pubmed.ncbi.nlm.nih.gov/9922273/)); the later cysteine-scanning work refined the count to 10 TM helices while confirming the cytosolic disposition of both termini. The 10-TM model is the current consensus and is consistent with the AraH/BtuC-family fold and the Pfam BPD_transp_2 (PF02653) annotation of Q88K36.

### F004 — RbsC operates within the *rbsDACBK* operon, feeding imported ribose into the pentose phosphate pathway via ribokinase

In *E. coli*, the genes for transport and initial metabolism of D-ribose form a single operon: *"The genes for the transport and initial-step metabolism of d-ribose form a single rbsDACBK operon. RbsABC forms the ABC-type high-affinity d-ribose transporter, while RbsD and RbsK are involved in the conversion of d-ribose into d-ribose 5-phosphate"* ([PMID: 23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/)). RbsABC (with RbsC as the permease) imports ribose; the ribose pyranase **RbsD** interconverts ribose anomers and the ribokinase **RbsK** phosphorylates D-ribose to **D-ribose-5-phosphate**, which enters the **pentose phosphate pathway** and nucleotide biosynthesis. The operon is repressed by the LacI-family regulator **RbsR** in the absence of ribose. This places RbsC at the entry point of a defined biochemical pathway and links its transport function to central carbon and nucleotide metabolism.

### F005 — The RbsABC₂ transporter uses a hybrid ATP-driven import mechanism with unique features

In vitro reassembly of the *E. coli* ribose transporter, probing intersubunit interactions under varying ribose and nucleotide conditions, isolated distinct assembly states: a full **RbsABC₂** complex trapped as a transition-state mimic (ATP/Mg²⁺/vanadate), an **RbsAC** complex (ADP/Mg²⁺), and a novel nucleotide-free **RbsBC** complex; excess ribose destabilized the RbsB–RbsC association. From these observations the authors concluded that *"RbsABC2 shares functional traits with both type I and type II importers, as well as possessing unique features, and employs a distinct mechanism relative to other ABC transporters"* ([PMID: 25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/)). RbsC is the transmembrane channel at the center of these transitions, and the ribose-dependent destabilization of the RbsB–RbsC interface provides a mechanistic snapshot of how the periplasmic binding protein hands off substrate to the permease during the transport cycle.

### F006 — Organism-specific confirmation: PP_2456 lies within a complete, syntenic *rbs* operon in *P. putida* KT2440

KEGG annotations for the PP_2454–PP_2459 locus form a contiguous ribose transport/catabolism cluster in KT2440, directly confirming the assignment in the target organism rather than by inference alone:

| Locus | Gene | KEGG KO | Function | EC |
|---|---|---|---|---|
| PP_2454 | rbsB | K10439 | Ribose-binding periplasmic protein | — |
| PP_2455 | rbsA | K10441 | Ribose ABC transporter ATP-binding protein | 7.5.2.7 |
| **PP_2456** | **rbsC** | **K10440** | **D-ribose ABC transporter permease (target)** | — |
| PP_2457 | rbsR | K02529 | LacI-family transcriptional repressor | — |
| PP_2458 | rbsK | K00852 | Ribokinase | 2.7.1.15 |
| PP_2459 | rbsD | K06726 | D-ribose pyranase | 5.4.99.62 |

PP_2456 itself carries UniProt cross-references to eggNOG **COG1172** (AraH-family sugar ABC permease), PANTHER subfamily **PTHR32196:SF72 "RIBOSE IMPORT PERMEASE PROTEIN RBSC,"** Pfam **PF02653** (BPD_transp_2), and InterPro **IPR001851**. The presence of all six functional partners in a single genomic neighborhood provides strong organism-specific corroboration that PP_2456 is the ribose-import permease and that the entire ribose uptake-and-catabolism module is intact in KT2440.

### F007 — Sequence features of Q88K36 and the deprecated EC number

Q88K36 is a **331-residue** polytopic membrane protein with UniProt-predicted helical transmembrane segments (approximately residues 20–43, 63–79, 135–152, 172–193, 224–243, 255–274, and 281–300) and a single Pfam **BPD_transp_2 (PF02653)** domain, consistent with the AraH/COG1172 ABC-importer permease fold. The sequence is strongly hydrophobic, matching an integral-membrane transporter. Importantly, the legacy **EC 3.6.3.17** ("monosaccharide-transporting ATPase") on the UniProt record is a property of the *transporter complex's ATPase activity*, which has been reclassified to **EC 7.5.2.7** and assigned by KEGG to the RbsA ATPase (PP_2455). The RbsC permease **has no intrinsic ATPase or catalytic activity**; it provides the transmembrane conduit. Any statement that RbsC "catalyzes" ATP hydrolysis is a mis-attribution of the complex-level EC number to the permease subunit.

*Note:* the UniProt annotation lists 7 predicted TM helices for Q88K36, whereas the experimentally determined *E. coli* topology is 10 TM helices ([PMID: 12923096](https://pubmed.ncbi.nlm.nih.gov/12923096/)). This is a common discrepancy between automated prediction and experimental topology mapping; the experimental 10-TM model should be regarded as more authoritative for the family.

### F008 — Q88K36 is a clear ortholog of *E. coli* RbsC, validating knowledge transfer

A global Needleman–Wunsch alignment (BLOSUM62, gap penalty −6) of Q88K36 (331 aa) against the experimentally characterized *E. coli* K-12 RbsC (P0AGI1, 321 aa) gave **38.4% identity (121/315)** and **60.3% BLOSUM-positive similarity (190/315)** over 315 gap-free aligned columns, with near-equal lengths and minimal indels (alignment length 337). Both proteins occupy the same eggNOG orthologous group (AraH/COG1172) and share the Pfam BPD_transp_2 (PF02653) domain. This level of identity across the full length of a membrane transporter, together with shared operonic context and identical domain architecture, is well above the threshold at which function is confidently conserved. It licenses the transfer of the detailed *E. coli* mechanistic knowledge (Findings F001–F005) to the *P. putida* protein.

---

## Mechanistic Model / Interpretation

RbsC is the membrane-embedded translocation channel of a classical tripartite ABC importer. The transport cycle can be represented as follows:

```
              PERIPLASM
        D-ribose (free sugar)
               │
               ▼
        ┌──────────────┐        RbsB captures ribose,
        │    RbsB       │  ◄──── closes around it, and docks
        │ (binding      │        onto the RbsC dimer
        │  protein)     │
        └──────┬───────┘
               │ symmetric hand-off (F002)
   ════════════▼════════════   INNER (CYTOPLASMIC) MEMBRANE
        ┌──────────────┐
        │  RbsC  ‖ RbsC │  10 TM helices each; homodimer RbsC₂
        │  (permease   │  forms the substrate pathway (F001,F003)
        │   channel)   │
        └──────┬───────┘
               │ ATP binding/hydrolysis drives
               │ conformational switch (F005)
        ┌──────▼───────┐
        │    RbsA       │  cytoplasmic ATPase, fused NBDs
        │ (ATP → ADP+Pi)│  EC 7.5.2.7 (F001, F007)
        └──────┬───────┘
               ▼
              CYTOPLASM
        D-ribose  ──RbsD (pyranase)──►  ──RbsK (ribokinase)──►
        D-ribose-5-phosphate  ──►  Pentose Phosphate Pathway
                                     & nucleotide biosynthesis (F004)
```

**Localization of function.** RbsC carries out its function in the **cytoplasmic (inner) membrane**. Its N- and C-termini and the nucleotide-hydrolyzing partner RbsA are on the cytoplasmic face; the substrate is captured in the **periplasm** by RbsB and delivered to the periplasmic/membrane surface of RbsC. Thus RbsC bridges the periplasm and cytoplasm, physically defining the pathway across the membrane.

**Primary function (direct answer to the research question).** The primary function of RbsC is **transport, not catalysis**: it is the transmembrane permease that translocates **D-ribose** (the substrate; substrate specificity is for the pentose sugar D-ribose) from the periplasm into the cytoplasm, energized indirectly by ATP hydrolysis carried out by the partner ATPase RbsA. It has no independent enzymatic activity; the EC number on its record reflects the complex's ATPase and properly belongs to RbsA.

**Pathway role.** RbsC is the committed entry step of the ribose utilization pathway. By importing ribose, it supplies the substrate for RbsD/RbsK, which produce ribose-5-phosphate — a node feeding the non-oxidative pentose phosphate pathway and nucleotide (purine/pyrimidine) biosynthesis. In *E. coli* the pathway is controlled by the LacI-family repressor RbsR, and the syntenic KT2440 operon contains the same repressor (PP_2457), indicating conserved ribose-inducible regulation.

**Mechanistic nuance.** In vitro reassembly shows the transporter passes through discrete states (RbsBC nucleotide-free; RbsAC with ADP; RbsABC₂ transition-state) and that ribose destabilizes the RbsB–RbsC interface, consistent with a peristaltic hand-off in which substrate binding by RbsB and nucleotide state at RbsA together gate the RbsC channel. The authors describe this as a hybrid of type I and type II importer behavior with unique features — an important caveat that RbsC's mechanism is not a textbook carbon-copy of maltose (type I) or vitamin-B12 (type II) importers.

---

## Evidence Base

| PMID | Title (abridged) | How it supports the findings |
|---|---|---|
| [25533465](https://pubmed.ncbi.nlm.nih.gov/25533465/) | *In vitro reassembly of the ribose ABC transporter reveals a distinct set of transport complexes* | Defines the tripartite RbsA/RbsC₂/RbsB architecture, confirms the RbsC₂ homodimer, and characterizes the hybrid transport mechanism (F001, F002, F005). |
| [10428954](https://pubmed.ncbi.nlm.nih.gov/10428954/) | *Molecular interactions in ribose transport: the binding protein module symmetrically associates with the homodimeric membrane transporter* | Genetic/suppressor proof that RbsC is a homodimer engaging RbsB symmetrically (F002). |
| [12923096](https://pubmed.ncbi.nlm.nih.gov/12923096/) | *Topology of RbsC, the membrane component of the E. coli ribose transporter* | Cysteine-scanning establishes 10 TM helices with cytosolic N/C termini (F003). |
| [9922273](https://pubmed.ncbi.nlm.nih.gov/9922273/) | *Topology of RbsC ... belonging to the AraH superfamily* | Places RbsC in the AraH ABC-importer superfamily; earlier PhoA-fusion topology (F003). |
| [23651393](https://pubmed.ncbi.nlm.nih.gov/23651393/) | *Involvement of the ribose operon repressor RbsR in regulation of purine nucleotide synthesis in E. coli* | Establishes the *rbsDACBK* operon, RbsABC as the high-affinity transporter, RbsD/RbsK producing ribose-5-phosphate, and RbsR regulation (F004). |

Supporting database evidence (not primary literature) includes KEGG orthology assignments for the PP_2454–PP_2459 cluster, UniProt/InterPro/Pfam domain annotations for Q88K36, and the computed orthology alignment to *E. coli* P0AGI1 (F006, F007, F008).

**Consistency of the evidence.** All five primary papers concern the *E. coli* ribose transporter and consistently describe RbsC as the transmembrane permease of a tripartite ABC importer. There is no conflicting literature attributing a different function to RbsC. The only internal discrepancy is the predicted (7 TM, UniProt) versus experimental (10 TM, *E. coli*) transmembrane-helix count, which is a prediction-vs-experiment artifact rather than a functional disagreement.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization in *P. putida*.** All mechanistic, topological, and biochemical evidence comes from *E. coli* RbsC. The assignment for Q88K36 rests on strong orthology (38% identity, full-length, shared operon and domains) rather than on direct *P. putida* transport assays, structures, or knockouts. While the inference is robust, kinetic parameters (K_m, V_max), exact substrate specificity, and physiological role in *P. putida* have not been measured here.

2. **Substrate specificity assumed, not tested in KT2440.** The substrate is inferred to be D-ribose from orthology and operon context. Some sugar ABC permeases exhibit relaxed specificity; whether *P. putida* RbsC also transports ribose analogs (e.g., other pentoses) has not been examined.

3. **Transmembrane topology of the *P. putida* protein is predicted only.** The 10-TM model is experimentally established for *E. coli* RbsC; the KT2440 protein's topology is inferred by homology, and automated prediction returns a lower helix count (7).

4. **No 3-D structure.** No experimental structure of any RbsC (from either organism) was analyzed; the fold assignment (AraH/BtuC-like) is homology-based.

5. **Regulation not experimentally verified in KT2440.** RbsR-mediated ribose induction is documented in *E. coli*; presence of PP_2457 (rbsR) suggests conserved regulation, but this has not been confirmed experimentally for KT2440.

6. **Legacy EC annotation.** The UniProt record still lists EC 3.6.3.17 on RbsC, which can mislead automated pipelines into treating the permease as an ATPase/enzyme. This report explicitly corrects that: the catalytic (ATP-hydrolysis) activity resides in RbsA.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic validation in KT2440.** Construct a clean *rbsC* (PP_2456) deletion and assay growth on D-ribose as sole carbon source; complement in *trans* to confirm the permease is required for ribose utilization. Test the whole *rbs* operon (PP_2454–PP_2459) for polar effects.

2. **Substrate-uptake kinetics.** Measure ¹⁴C-D-ribose uptake in wild-type vs. Δ*rbsC* cells and in vesicles to quantify affinity (K_m) and confirm ATP dependence; screen candidate alternative pentoses to define specificity.

3. **Reconstitution/structure.** Purify the *P. putida* RbsABC complex (analogous to the *E. coli* reassembly work) and pursue cryo-EM to obtain a species-specific structure and confirm the RbsC₂ homodimer and 10-TM fold.

4. **Topology confirmation.** Perform cysteine-scanning or reporter-fusion topology mapping on *P. putida* RbsC to reconcile the predicted 7-TM vs. experimental 10-TM models.

5. **Regulation assays.** Test ribose-dependent induction of the operon and RbsR (PP_2457) binding to the operator to confirm conserved transcriptional control.

6. **Annotation correction.** Flag the deprecated EC 3.6.3.17 on the RbsC record; the ATPase activity (EC 7.5.2.7) should be attributed to RbsA (PP_2455), and RbsC should be annotated strictly as the transmembrane permease.

---

## Conclusion

RbsC (PP_2456, Q88K36) in *Pseudomonas putida* KT2440 is the **inner-membrane permease subunit of the high-affinity D-ribose ABC importer**. It is a polytopic AraH/BtuC-family transmembrane protein that functions as a homodimer (RbsC₂), forming the substrate-translocation channel; together with the periplasmic ribose-binding protein RbsB and the cytoplasmic ATPase RbsA, it imports **D-ribose** across the cytoplasmic membrane in an ATP-driven cycle. RbsC has no intrinsic catalytic activity — the ATP hydrolysis powering transport is performed by RbsA. Imported ribose is phosphorylated by ribokinase (RbsK) to ribose-5-phosphate, feeding the pentose phosphate pathway and nucleotide metabolism. The assignment is confirmed for KT2440 by a complete syntenic *rbs* operon and by robust orthology (38% identity) to the experimentally characterized *E. coli* RbsC.


## Artifacts

- [OpenScientist final report](rbsC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rbsC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25533465
2. PMID:10428954
3. PMID:12923096
4. PMID:9922273
5. PMID:23651393