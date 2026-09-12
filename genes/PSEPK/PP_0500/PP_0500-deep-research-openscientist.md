---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:41:50.083956'
end_time: '2026-07-16T12:04:42.044350'
duration_seconds: 4971.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0500
  gene_symbol: PP_0500
  uniprot_accession: Q88QJ2
  protein_description: 'RecName: Full=dTDP-4-dehydrorhamnose reductase {ECO:0000256|ARBA:ARBA00017099,
    ECO:0000256|RuleBase:RU364082}; EC=1.1.1.133 {ECO:0000256|ARBA:ARBA00012929, ECO:0000256|RuleBase:RU364082};'
  gene_info: OrderedLocusNames=PP_0500 {ECO:0000313|EMBL:AAN66128.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the dTDP-4-dehydrorhamnose reductase family.
  protein_domains: dTDP_dehydrorham_reduct. (IPR005913); NAD(P)-bd_dom_sf. (IPR036291);
    RmlD-like-bd. (IPR029903); RmlD_sub_bind (PF04321)
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
  path: PP_0500-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0500-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QJ2
- **Protein Description:** RecName: Full=dTDP-4-dehydrorhamnose reductase {ECO:0000256|ARBA:ARBA00017099, ECO:0000256|RuleBase:RU364082}; EC=1.1.1.133 {ECO:0000256|ARBA:ARBA00012929, ECO:0000256|RuleBase:RU364082};
- **Gene Information:** OrderedLocusNames=PP_0500 {ECO:0000313|EMBL:AAN66128.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the dTDP-4-dehydrorhamnose reductase family.
- **Key Domains:** dTDP_dehydrorham_reduct. (IPR005913); NAD(P)-bd_dom_sf. (IPR036291); RmlD-like-bd. (IPR029903); RmlD_sub_bind (PF04321)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0500" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0500' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0500** (gene ID: PP_0500, UniProt: Q88QJ2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0500 (Q88QJ2) — dTDP-4-dehydrorhamnose reductase (RmlD)

**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) — proteome code PSEPK
**UniProt:** Q88QJ2 · **Locus:** PP_0500 · **EC:** 1.1.1.133 · **Length:** 294 aa
**Family:** dTDP-4-dehydrorhamnose reductase (RmlD) family; short-chain dehydrogenase/reductase (SDR) superfamily
**Domains/signatures:** PF04321 (RmlD_sub_bind); IPR005913 (dTDP_dehydrorham_reduct); IPR029903 (RmlD-like-bd); IPR036291 (NAD(P)-bd domain superfamily)

---

## 1. Summary (answer to the research question)

PP_0500 encodes **RmlD, dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133)**, the enzyme that catalyzes the **fourth and final step of dTDP-L-rhamnose biosynthesis**. Using **NAD(P)H as the hydride donor and a Mg²⁺ cofactor**, RmlD reduces the C4 keto group of dTDP-4-keto-6-deoxy-L-mannose (dTDP-6-deoxy-L-*lyxo*-4-hexulose) to produce **dTDP-β-L-rhamnose**, the activated nucleotide-sugar donor used by rhamnosyltransferases to build rhamnose-containing cell-surface glycans. The enzyme is a **soluble, cytoplasmic, Mg²⁺-dependent homodimer** of the SDR superfamily. The gene identity is unambiguous and fully consistent with the provided UniProt annotation.

---

## 2. Gene/Protein Identity Verification

The requested verification steps are satisfied:

- **Symbol ↔ description match:** UniProt Q88QJ2 (PP_0500) is named "dTDP-4-dehydrorhamnose reductase," EC 1.1.1.133, with catalytic-activity, cofactor (Mg²⁺) and pathway ("dTDP-L-rhamnose biosynthesis") annotations that match the RmlD family description exactly.
- **Organism correct:** Entry belongs to *P. putida* KT2440 (taxid 160488).
- **Family/domains align with literature:** The Pfam/InterPro signatures (PF04321 RmlD_sub_bind; NAD(P)-binding domain) are the canonical RmlD signatures, and the enzymology matches the definitive *Salmonella* RmlD structural study (Blankenfeldt et al., 2002).
- **No conflicting gene of the same symbol was found.** "RmlD" is used consistently across bacteria for this single enzymatic activity; there is no ambiguity for this locus.

The literature on RmlD is authoritative and directly applicable, so research proceeded on the correct target.

---

## 3. Primary Function — Reaction Catalyzed and Substrate Specificity

**Reaction (UniProt Q88QJ2 catalytic activity; Rhea):**

> dTDP-β-L-rhamnose + NADP⁺  ⇌  dTDP-4-dehydro-β-L-rhamnose + NADPH + H⁺

In the biosynthetic (reductive) direction the enzyme converts **dTDP-4-keto-6-deoxy-L-mannose → dTDP-L-rhamnose**. UniProt summarizes the function as: *"Catalyzes the reduction of dTDP-6-deoxy-L-lyxo-4-hexulose to yield dTDP-L-rhamnose."*

**Mechanism (from the *Salmonella enterica* RmlD crystal structure; Blankenfeldt et al., EMBO J 2002, PMID 12057193):**
- *"RmlD … catalyzes the final step in the conversion of dTDP-D-glucose to dTDP-L-rhamnose in an NAD(P)H- and Mg²⁺-dependent reaction."*
- Catalysis proceeds by **hydride transfer from the nicotinamide ring of the cofactor to the C4′-carbonyl (keto) group of the substrate**, with the substrate *"activated through protonation by a conserved tyrosine"* — the classic SDR Ser/Tyr/Lys catalytic machinery, here with a proposed novel role for the catalytic Ser/Thr.
- NAD(P)H binds in a **solvent-exposed cleft, allowing facile cofactor exchange.**

**Cofactors:** NAD(P)H (the *S. enterica* enzyme binds both NADH and NADPH; the *P. putida* entry is annotated NADP-binding) and **one Mg²⁺ per monomer** (UniProt: "Binds 1 Mg(2+) ion per monomer").

**Substrate specificity:** RmlD is specific for the **dTDP-activated** 4-keto-6-deoxy-hexose intermediate of the rhamnose pathway; it is the committed reductase that fixes the L-*manno* (rhamnose) configuration at C4. It is highly substrate-specific for the nucleotide-sugar produced by the upstream epimerase RmlC.

---

## 4. Pathway Context — dTDP-L-rhamnose Biosynthesis (RmlABCD)

RmlD is the last of four enzymes of the conserved **RmlABCD** pathway that converts glucose-1-phosphate and dTTP into dTDP-L-rhamnose (reviewed in PMID 36014553; enzymology confirmed for reconstituted RmlABCD systems, e.g. PMID 34819927, PMID 42197457):

1. **RmlA** — glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24): Glc-1-P + dTTP → dTDP-D-glucose
2. **RmlB** — dTDP-D-glucose 4,6-dehydratase (EC 4.2.1.46): → dTDP-4-keto-6-deoxy-D-glucose
3. **RmlC** — dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13): → dTDP-4-keto-6-deoxy-L-mannose
4. **RmlD (PP_0500)** — dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133): → **dTDP-L-rhamnose**

**Pathway genes in *P. putida* KT2440.** The upstream enzymes are encoded in a separate genomic locus from *rmlD*:
- RmlA = **PP_1783** (Q88LZ3), RmlC = **PP_1782** (Q88LZ4), RmlB = **PP_1785** (Q88LZ1) — a small *rml* cluster around PP_1782–1785.
- RmlD = **PP_0500** (Q88QJ2), located separately.

This "split" arrangement (the RmlD reductase remote from the RmlABC core) is common in Gram-negative genomes and does not change the biochemistry: PP_0500 supplies the reductase activity that completes the pathway.

**Fate of the product.** dTDP-L-rhamnose is *"used by prokaryotic rhamnosyltransferases as the glycosyl donor for the synthesis of rhamnose-containing polysaccharides"* (PMID 34819927). In *Pseudomonas* and other Gram-negatives, L-rhamnose is a building block of the **lipopolysaccharide (LPS) O-antigen and core** and of other cell-surface/exo-polysaccharides; the RmlD product is therefore a metabolic feed-in point for **cell-envelope glycan assembly**.

---

## 5. Subcellular Localization

RmlD functions in the **cytoplasm**, as part of soluble nucleotide-sugar metabolism, upstream of the membrane-associated steps that assemble and export glycans:
- The 294-aa sequence contains **no signal peptide and no predicted transmembrane helices**, and UniProt annotates it as a soluble oxidoreductase (NADP ligand keyword) with no membrane/secretion localization — consistent with a cytosolic enzyme.
- Its substrates and products (dTDP-sugars, NAD(P)H, Mg²⁺) are cytoplasmic metabolites.
- Mechanistically the enzyme is a **homodimer with a Mg²⁺-containing dimer interface** (Blankenfeldt et al., 2002), i.e. it operates as a soluble oligomer rather than a membrane complex.

The downstream product is subsequently used at the inner membrane/periplasmic face by rhamnosyltransferases during glycan biosynthesis, but RmlD's own catalytic step is cytoplasmic.

---

## 6. Structure and Evolutionary Classification

- **Fold/superfamily:** RmlD belongs to the **short-chain dehydrogenase/reductase (SDR) superfamily** (Rossmann NAD(P)-binding fold; IPR036291) with a C-terminal RmlD substrate-binding domain (PF04321). It retains the SDR catalytic Ser/Tyr/Lys triad, with a conserved tyrosine acting as the catalytic acid.
- **Distinctive feature:** Unlike canonical SDRs, RmlD *"has a novel dimer interface that contains Mg²⁺"* and requires the metal for activity (PMID 12057193) — a defining biochemical hallmark of this family that separates it from ordinary NAD(P)-dependent reductases.
- **Evidence class for PP_0500:** The *P. putida* annotation is **inference by orthology / family rule** (UniProt automated rules ARBA/RuleBase RU364082) built on strong experimental characterization of RmlD orthologs (e.g., *Salmonella enterica* structure/mechanism; multiple reconstituted RmlABCD systems). The specific enzyme from strain KT2440 has not, to my knowledge, been individually crystallized or kinetically characterized, but sequence/domain conservation to characterized RmlD enzymes is unambiguous.
- **Independent sequence check (this study).** Global pairwise alignment of the 294-aa PP_0500 sequence to reviewed, experimentally characterized EC 1.1.1.133 enzymes gives **~29–31% identity**: *Salmonella* RmlD P26392 (the crystallized enzyme, PDB 1KBZ) **29.1%** (83/285); *M. tuberculosis* P9WH09 **31.0%**; *Streptomyces griseus* P29781 **31.2%**; *M. smegmatis* A0QTF8 **30.1%**. This "twilight-zone" identity is typical *within* the RmlD family across distant taxa. PP_0500 also carries the diagnostic **N-terminal glycine-rich Rossmann NAD(P)-binding motif** (…M**LLGGGNALGQ**…, a GxxGxxG-type loop; IPR036291) plus the RmlD substrate-binding domain (PF04321) — corroborating, by sequence and evolutionary inference, that PP_0500 is a genuine RmlD and not a mis-annotation.

---

## 7. Biological Importance and Significance

- **Cell-envelope function.** L-Rhamnose contributes to LPS/cell-wall glycans; genetic loss of rmlD ablates cell-wall rhamnose. In *Streptococcus mutans*, *"loss of either rmlD or rgpG results in ablation of rhamnose content in the … cell wall,"* and rmlD deletion caused *"a severe growth defect … [and] elevated susceptibility … to acid and oxidative stress"* (PMID 31871035). This illustrates the pathway's contribution to envelope integrity, stress resistance and (in pathogens) virulence — though these specific phenotypes are from other species and are inferred, not demonstrated, for *P. putida*.
- **Antibacterial target.** Because *"[rhamnose-associated molecules] are present in bacteria but not mammals"* (PMID 36014553) and *"L-rhamnose biosynthesis is an antibacterial target"* (PMID 12057193), RmlD (with RmlA–C) is pursued as a selective antibacterial/anti-tuberculosis target (e.g., inhibitor/modeling studies, PMID 33547544).
- **Biotechnology.** RmlABCD systems, including the RmlD reductase, are used in one-pot enzymatic synthesis of dTDP-L-rhamnose for glycochemistry (PMID 34819927, PMID 42197457).

---

## 8. Supported vs. Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| PP_0500 is RmlD / dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) | **Supported** | UniProt catalytic activity + family signatures; matches characterized RmlD enzymology |
| Reaction = NAD(P)H/Mg²⁺-dependent reduction of dTDP-4-keto-6-deoxy-L-mannose → dTDP-L-rhamnose | **Supported** | UniProt; Blankenfeldt et al. 2002 (PMID 12057193) |
| Product dTDP-L-rhamnose is a rhamnosyl donor for surface glycans (LPS/O-antigen) | **Supported** | PMID 34819927; review PMID 36014553 |
| Enzyme is a cytoplasmic Mg²⁺-dependent homodimer (SDR superfamily) | **Supported** | PMID 12057193; UniProt cofactor note; no TM/signal in sequence |
| Full RmlABCD pathway present in KT2440 (RmlA/B/C at PP_1782–1785) | **Supported** | UniProt EC-based queries in taxid 160488 |
| KT2440-specific in vitro kinetics / structure of PP_0500 exist | **Refuted / not found** | No primary biochemical study of the KT2440 enzyme located |

---

## 9. Limitations and Future Directions

- Functional assignment of PP_0500 rests on **orthology and family rules**, not on direct biochemical or genetic characterization of the *P. putida* KT2440 enzyme; the reaction/mechanism details derive from orthologs (chiefly *S. enterica* RmlD).
- The precise glycan destination of dTDP-L-rhamnose in KT2440 (O-antigen vs. core vs. other exopolysaccharide) was not resolved from a strain-specific LPS-composition study; this is stated as the general Gram-negative role. Targeted literature searches for a KT2440-specific LPS/O-antigen sugar-composition analysis, and for a *PP_0500*-specific essentiality/transposon phenotype, returned **no primary strain-specific data** (though KT2440 is intensively studied as a biotechnology chassis, e.g. PMID 38975763). Rhamnose/O-antigen genes are generally dispensable for viability under laboratory conditions in pseudomonads, so *PP_0500* is expected to be non-essential in rich medium — but this is an inference, not a measured result for this locus.
- **Future work:** heterologous expression + kinetic assay of PP_0500; *rmlD* knockout in KT2440 to test LPS-rhamnose loss and phenotype; structural confirmation (crystal/AlphaFold) of the Mg²⁺ dimer interface; tracing which surface glycan(s) incorporate the rhamnose.

---

### Key references
- Blankenfeldt W. et al. (2002) *EMBO J* — RmlD (dTDP-6-deoxy-L-lyxo-4-hexulose reductase) structure and Mg²⁺-dependent mechanism. **PMID 12057193**
- Review: Rhamnose-Containing Compounds: Biosynthesis and Applications (2022). **PMID 36014553**
- One-pot RmlABCD synthesis of dTDP-L-rhamnose (2021). **PMID 34819927**
- RmlABCD from marine bacteria; dTDP-L-rhamnose synthesis (2026). **PMID 42197457**
- rmlD disruption in *S. mutans* — cell-wall rhamnose and fitness (2020). **PMID 31871035**
- RmlD *M. tuberculosis* modeling/inhibitors (2021). **PMID 33547544**
- UniProt Q88QJ2 (PP_0500), *P. putida* KT2440.


## Artifacts

- [OpenScientist final report](PP_0500-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0500-deep-research-openscientist_artifacts/final_report.pdf)