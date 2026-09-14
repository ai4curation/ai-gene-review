---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T04:05:13.911756'
end_time: '2026-08-13T05:14:12.972630'
duration_seconds: 4139.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ptxD
  gene_symbol: ptxD
  uniprot_accession: Q88HI1
  protein_description: 'SubName: Full=Phosphonate dehydrogenase {ECO:0000313|EMBL:AAN68980.1};
    EC=1.20.1.1 {ECO:0000313|EMBL:AAN68980.1};'
  gene_info: Name=ptxD {ECO:0000313|EMBL:AAN68980.1}; OrderedLocusNames=PP_3376 {ECO:0000313|EMBL:AAN68980.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the D-isomer specific 2-hydroxyacid
  protein_domains: D-isomer_2-hydroxyacid_DH. (IPR050223); D-isomer_2_OHA_DH_cat_dom.
    (IPR006139); D-isomer_DH_CS. (IPR029753); D-isomer_DH_CS1. (IPR029752); D-isomer_DH_NAD-bd.
    (IPR006140)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ptxD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ptxD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HI1
- **Protein Description:** SubName: Full=Phosphonate dehydrogenase {ECO:0000313|EMBL:AAN68980.1}; EC=1.20.1.1 {ECO:0000313|EMBL:AAN68980.1};
- **Gene Information:** Name=ptxD {ECO:0000313|EMBL:AAN68980.1}; OrderedLocusNames=PP_3376 {ECO:0000313|EMBL:AAN68980.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the D-isomer specific 2-hydroxyacid
- **Key Domains:** D-isomer_2-hydroxyacid_DH. (IPR050223); D-isomer_2_OHA_DH_cat_dom. (IPR006139); D-isomer_DH_CS. (IPR029753); D-isomer_DH_CS1. (IPR029752); D-isomer_DH_NAD-bd. (IPR006140)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ptxD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ptxD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ptxD** (gene ID: ptxD, UniProt: Q88HI1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: ptxD (Q88HI1), Pseudomonas putida KT2440 (PP_3376)

## 1. Summary / Answer

**ptxD encodes phosphite dehydrogenase (PtxD), an NAD⁺-dependent oxidoreductase (systematic name NAD:phosphite oxidoreductase; EC 1.20.1.1).** Its primary function is the essentially irreversible two-electron oxidation of inorganic phosphite (HPO₃²⁻; phosphorus oxidation state +3) to orthophosphate (Pi; +5), coupled to the reduction of NAD⁺ to NADH:

> **phosphite + NAD⁺ + H₂O → phosphate + NADH + H⁺**

The enzyme is a soluble, cytoplasmic homodimer that is highly specific for phosphite and strongly prefers NAD⁺ over NADP⁺. Biologically it is the committed step that allows the cell to use the environmentally "exotic," reduced phosphorus compound **phosphite as a sole phosphorus source**, converting it into the orthophosphate that feeds normal cellular phosphate assimilation. It is encoded within a reduced-phosphorus (ptx/htx) gene cluster that also provides an ABC transporter for phosphite uptake.

### ⚠️ Identity note (verification outcome)
The target protein Q88HI1 is the *P. putida* KT2440 gene **PP_3376 / ptxD**, annotated as phosphite/"phosphonate" dehydrogenase (EC 1.20.1.1) by genome homology (EMBL AAN68980). The gene symbol *ptxD* is **not ambiguous** — it consistently denotes phosphite dehydrogenase across bacteria (no competing gene family uses this symbol). Verification result: dedicated literature searches for *P. putida* KT2440–specific phosphite oxidation / PP_3376 characterization returned **no direct studies**; all deep biochemical/structural evidence comes from the *P. stutzeri* WM88 ortholog and closely related homologs. The EC number (1.20.1.1), family (D-2-hydroxyacid dehydrogenase), and InterPro domain set of Q88HI1 are all fully consistent with phosphite dehydrogenase, so the annotation is transferred with high confidence by orthology. The deep experimental characterization in the literature was performed on the founding ortholog from *Pseudomonas stutzeri* WM88 (and closely related homologs). Direct, isolated biochemical study of the *P. putida* KT2440 protein itself was not found; its function is assigned by strong orthology, conserved domain architecture, and the demonstrated conservation of activity across divergent PtxD homologs. The UniProt "phosphonate dehydrogenase" wording is a database naming variant — the enzyme acts on **phosphite** (HPO₃²⁻), an inorganic reduced-phosphorus oxyanion, not on organophosphonates (C–P compounds).

---

## 2. Primary molecular function (the reaction and substrate specificity)

**Reaction catalyzed.** The founding ortholog stoichiometrically produces NADH and phosphate from NAD⁺ and phosphite, and **the reverse reaction is not observed**, i.e., oxidation is thermodynamically irreversible under physiological conditions (Costas, White & Metcalf 2001, PMID 11278981). Chemically, a P–H bond of phosphite is replaced by a P–OH bond; the hydride is transferred to NAD⁺ and the new oxygen is derived from water, so despite belonging to the 2-hydroxyacid dehydrogenase family the chemistry is a genuine phosphorus oxidation rather than hydroxyacid → ketoacid conversion.

**Substrate specificity.** PtxD is a dedicated phosphite oxidase: of numerous compounds tested, **none could substitute for phosphite**, and NADP⁺ substitutes only poorly for NAD⁺ (PMID 11278981). The phosphite analog **sulfite acts as a dead-end inhibitor**, consistent with a specific anion-binding pocket.

**Kinetics and mechanism.** High affinity for both substrates: Km(phosphite) = 53.1 µM, Km(NAD⁺) = 54.6 µM; Vmax = 12.2 µmol·min⁻¹·mg⁻¹; kcat = 440 min⁻¹. Initial-rate, product-inhibition and dead-end-inhibitor analyses indicate a **sequential ordered mechanism with NAD⁺ binding first and NADH released last** (PMID 11278981). Catalysis proceeds by **hydride transfer from phosphite to the nicotinamide C4 of NAD⁺**, and transition-state work shows that binding energy from the NAD⁺ ADP fragment is used to activate this hydride transfer (Hegazy & Richard 2025, PMID 41220039). The wild-type enzyme is NAD⁺-specific, but this preference rests on a few cofactor-pocket residues and has been **engineered to accept NADP⁺**, and to be highly thermostable, making PtxD a widely used NAD(P)H-regeneration biocatalyst (McLachlan, Johannes & Zhao 2008, PMID 17615560) — confirming genuine NAD(P)-dependent dehydrogenase chemistry.

---

## 3. Structure, family and catalytic residues

PtxD is a member of the **D-isomer–specific 2-hydroxyacid NAD-dependent dehydrogenase (DHDH) superfamily** — and is notably "**the only one to have an inorganic substrate**" (PMID 11278981). This matches the InterPro architecture of Q88HI1: a catalytic domain (IPR006139), an NAD-binding Rossmann domain (IPR006140), and the family conserved-site signatures (IPR029752/IPR029753; family IPR050223).

An X-ray crystal structure revealed **Arg301** in the active site as a PtxD-specific residue (conserved in PtxDs but not in other DHDHs). Mutagenesis showed it is critical for catalysis: R301A caused ~100-fold lower kcat and ~700-fold higher Km(phosphite), while the conservative R301K retained (even slightly higher) activity — implicating Arg301 in binding/orienting the anionic phosphite via electrostatics. Additional PtxD-specific active-site residues include **Trp134, Tyr139 and Ser295** (Hung et al. 2012, PMID 22564138). A conserved His/Asp catalytic dyad typical of the DHDH family serves as the general base. Importantly, divergent PtxD homologs sharing only 39–72% identity **all oxidize phosphite with similar kinetics**, providing strong support for transferring this functional annotation to the KT2440 ortholog.

---

## 4. Cellular localization

PtxD is a **soluble cytoplasmic enzyme**. It purifies as a soluble homodimer, carries no signal/membrane-sorting sequence, is NAD⁺-dependent (using the cytosolic cofactor pool), and its substrate phosphite is delivered to the cytoplasm by an upstream ABC transporter (htxBCD) (PMID 15640200). Its extensive heterologous use as a **cytosolic NAD(P)H-regeneration** enzyme in bacteria, algae and plants further confirms it functions intracellularly (PMID 27007496). No evidence supports periplasmic or membrane localization; the KT2440 localization is inferred from these conserved properties.

---

## 5. Pathway and physiological role

PtxD is the **committed, terminal oxidation step** in the assimilation of reduced phosphorus:

- In *P. stutzeri* WM88, all genes for oxidizing phosphite and hypophosphite lie on a single ~30-kb region; **hypophosphite is oxidized to phosphate via a phosphite intermediate**, and PtxD performs the phosphite → phosphate step (Metcalf & Wolfe 1998, PMID 9791102).
- The gene cluster couples PtxD to an **ABC-type transporter (htxBCD)** that imports phosphite/hypophosphite, plus (for hypophosphite users) the 2-oxoglutarate–dependent hypophosphite dioxygenase HtxA (Wilson & Metcalf 2005, PMID 15640200).
- The orthophosphate produced enters normal cellular phosphate metabolism (Pho regulon / central P assimilation). Because oxidation also yields NADH, the reaction can additionally supply reducing equivalents.
- Ecologically, phosphite-oxidizing bacteria are abundant in soils and sediments, and PtxD-type oxidation is a significant part of the environmental phosphorus cycle (White & Metcalf 2007, PMID 18035609; Stone & White 2012, PMID 22134432; Sakuma et al. 2025, PMID 41343678).

We focus on this precise assimilatory role rather than broad pleiotropic effects. For *P. putida* KT2440 specifically, PP_3376/ptxD is genome-annotated and predicted to enable phosphite utilization; a KT2440-specific growth/knockout phenotype was not located in the retrieved literature and remains an inference from orthology.

---

## 6. Supported vs. refuted hypotheses

**Supported**
- H1: ptxD encodes an NAD⁺-dependent phosphite dehydrogenase (EC 1.20.1.1) oxidizing phosphite→phosphate. ✔ (PMID 11278981)
- H2: Substrate specificity is strict for phosphite; NAD⁺ ≫ NADP⁺. ✔ (PMID 11278981)
- H3: Enzyme is a soluble cytoplasmic homodimer with an ordered NAD-first mechanism. ✔ (PMID 11278981)
- H4: Belongs to D-2-hydroxyacid dehydrogenase family; Arg301 is a key active-site residue. ✔ (PMID 11278981, 22564138)
- H5: Functions in reduced-P assimilation within a ptx/htx cluster with an ABC transporter. ✔ (PMID 9791102, 15640200)

**Refuted / not supported**
- "Phosphonate (C–P organophosphonate) dehydrogenase" as literal substrate — refuted; the enzyme acts on inorganic phosphite, and no organophosphonate substrate activity is described. The UniProt "phosphonate dehydrogenase" label is a naming variant.
- Reversible phosphite/phosphate interconversion — refuted (reverse reaction not observed).

---

## 7. Limitations and future directions

- The KT2440 protein Q88HI1 itself has not, to our knowledge, been purified and kinetically characterized; conclusions rest on strong orthology and demonstrated functional conservation among PtxD homologs.
- A KT2440-specific phenotype (growth on phosphite as sole P source; ΔptxD knockout) would directly confirm physiological function.
- Direct structural determination (or confident AlphaFold model with the Arg301/Trp134/Tyr139/Ser295 constellation) of the KT2440 protein would verify active-site conservation.

---

## Key references
- Costas, White & Metcalf 2001, *J Biol Chem* — purification & kinetics of PtxD (PMID 11278981)
- Hung et al. 2012, *Biochemistry* — X-ray structure, Arg301 (PMID 22564138)
- Metcalf & Wolfe 1998, *J Bacteriol* — genetics of phosphite/hypophosphite oxidation (PMID 9791102)
- Wilson & Metcalf 2005, *Appl Environ Microbiol* — ptx/htx cluster, ABC transporter, evolution (PMID 15640200)
- White & Metcalf 2007, *Annu Rev Microbiol* — review of reduced-P metabolism (PMID 18035609)
- Hegazy & Richard 2025 — hydride-transfer activation by NAD (PMID 41220039)
- Sakuma et al. 2025 — evolution/distribution of phosphite oxidases (PMID 41343678)


## Artifacts

- [OpenScientist final report](ptxD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ptxD-deep-research-openscientist_artifacts/final_report.pdf)