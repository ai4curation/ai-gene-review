---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:21:52.119778'
end_time: '2026-07-23T13:36:32.737259'
duration_seconds: 880.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hmgA
  gene_symbol: hmgA
  uniprot_accession: Q88E47
  protein_description: 'RecName: Full=Homogentisate 1,2-dioxygenase {ECO:0000255|HAMAP-Rule:MF_00334};
    Short=HGDO {ECO:0000255|HAMAP-Rule:MF_00334}; EC=1.13.11.5 {ECO:0000255|HAMAP-Rule:MF_00334};
    AltName: Full=Homogentisate oxygenase {ECO:0000255|HAMAP-Rule:MF_00334}; AltName:
    Full=Homogentisic acid oxidase {ECO:0000255|HAMAP-Rule:MF_00334}; AltName: Full=Homogentisicase
    {ECO:0000255|HAMAP-Rule:MF_00334};'
  gene_info: Name=hmgA {ECO:0000255|HAMAP-Rule:MF_00334}; OrderedLocusNames=PP_4621;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the homogentisate dioxygenase family.
  protein_domains: HgmA_C. (IPR046451); HgmA_N. (IPR046452); Homogentis_dOase. (IPR005708);
    Homogentis_dOase_bac. (IPR022950); RmlC-like_jellyroll. (IPR014710)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: hmgA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hmgA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E47
- **Protein Description:** RecName: Full=Homogentisate 1,2-dioxygenase {ECO:0000255|HAMAP-Rule:MF_00334}; Short=HGDO {ECO:0000255|HAMAP-Rule:MF_00334}; EC=1.13.11.5 {ECO:0000255|HAMAP-Rule:MF_00334}; AltName: Full=Homogentisate oxygenase {ECO:0000255|HAMAP-Rule:MF_00334}; AltName: Full=Homogentisic acid oxidase {ECO:0000255|HAMAP-Rule:MF_00334}; AltName: Full=Homogentisicase {ECO:0000255|HAMAP-Rule:MF_00334};
- **Gene Information:** Name=hmgA {ECO:0000255|HAMAP-Rule:MF_00334}; OrderedLocusNames=PP_4621;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the homogentisate dioxygenase family.
- **Key Domains:** HgmA_C. (IPR046451); HgmA_N. (IPR046452); Homogentis_dOase. (IPR005708); Homogentis_dOase_bac. (IPR022950); RmlC-like_jellyroll. (IPR014710)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hmgA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hmgA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hmgA** (gene ID: hmgA, UniProt: Q88E47) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hmgA* (Homogentisate 1,2-Dioxygenase, Q88E47) in *Pseudomonas putida* KT2440

## 0. Identity verification (performed before research)

The target was confirmed to be the correct protein before any literature was interpreted:

- **UniProt:** Q88E47 = **HGD_PSEPK** (reviewed).
- **Gene / locus:** `hmgA` / `PP_4621`.
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950).
- **Length / mass:** 433 aa, ~48 kDa.
- **EC 1.13.11.5**, homogentisate dioxygenase family (Pfam/InterPro HgmA_N + HgmA_C; RmlC‑like jelly‑roll / cupin‑type core, IPR014710).
- **Decisive check:** UniProt Q88E47 cross‑references PDB entries **3ZDS, 4AQ2, 4AQ6**, which are the structures reported in **Jeoung et al., 2013 (PMID 23858455)**. The iron‑ligand residues annotated for Q88E47 (His331, Glu337, His367), the substrate‑binding Tyr346, and the catalytic His288 match that paper's numbering exactly. **Therefore the 2013 Dobbek‑group structural/mechanistic study is of this exact protein, not a homolog** — giving direct experimental evidence for the target.

No ambiguity: the gene symbol, organism, family, and domains all align with a well‑characterized enzyme.

---

## 1. Summary (answer to the research question)

**HmgA is homogentisate 1,2‑dioxygenase (EC 1.13.11.5)**, a cytoplasmic, mononuclear **non‑heme Fe(II)** ring‑cleaving oxygenase. It catalyzes the committed, central step of the **homogentisate pathway** by using molecular O₂ to oxidatively cleave the aromatic ring of **homogentisate (2,5‑dihydroxyphenylacetate)**, producing **4‑maleylacetoacetate**. This reaction channels carbon derived from **L‑phenylalanine and L‑tyrosine** (and 3‑hydroxyphenylacetate) into central metabolism, ultimately yielding **fumarate + acetoacetate**. It acts inside the cell (soluble cytoplasmic enzyme) and its expression is induced by its own substrate homogentisate and repressed by the IclR‑type regulator HmgR.

---

## 2. Primary molecular function: the catalyzed reaction and substrate specificity

**Reaction:**
> homogentisate (2,5‑dihydroxyphenylacetate) + O₂ → 4‑maleylacetoacetate

HmgA is a **dioxygenase**: both atoms of O₂ are incorporated into the product as it opens the benzene ring between C1 and C2 of homogentisate. The enzyme is highly specific for homogentisate, a 1,2,4‑trisubstituted aromatic (a hydroquinone bearing an acetate side chain), which is the natural central intermediate of aromatic amino‑acid breakdown (PMID 23858455; PMID 15262943).

**Cofactor:** a single catalytic **Fe(II)** ion (non‑heme). The 1.70 Å resting‑state structure of the *P. putida* enzyme shows the iron in **octahedral coordination by two histidines (His331, His367), a bidentate carboxylate (Glu337), and two water molecules** — a variant of the classic 2‑His‑1‑carboxylate "facial triad" used by many Fe(II)/O₂ oxygenases (PMID 23858455).

**Mechanistic evidence (direct, on this protein):** Jeoung et al. trapped and crystallographically resolved **four consecutive states of the catalytic cycle** in the *P. putida* enzyme: the **substrate‑bound**, **superoxo:semiquinone‑**, **alkylperoxo‑**, and **product‑bound** intermediates. Homogentisate binds as a **monodentate** Fe ligand; its interaction with **Tyr346** triggers folding of a mobile loop that closes over the active site and excludes solvent, and substrate binding is enthalpy‑driven/entropically disfavored (anoxic ITC). This shows that, despite an unrelated fold, HmgA proceeds through the **same principal O₂‑activation intermediates as extradiol ring‑cleaving dioxygenases** (PMID 23858455).

**Residue function (mutagenesis on this protein, curated in UniProt from PMID 23858455):**
- **His288 (active‑site proton acceptor):** H288F reduces catalytic efficiency ~**75‑fold**.
- **Tyr346 (substrate anchor):** Y346F decreases homogentisate affinity **>60‑fold** and catalytic efficiency ~**20‑fold**.

**Quantum‑chemical support:** QM/MM (PMID 27119315) and hybrid‑DFT (PMID 16332080) studies of homogentisate dioxygenase reconstruct a mechanism of **peroxo‑intermediate formation → O–O bond cleavage (arene‑oxide radical) → ring scission**, with an active‑site glutamate stabilizing bridging species — consistent with the crystallographically observed alkylperoxo intermediate. These computational models rationalize the enzyme's product specificity.

---

## 3. Biological process and pathway context

HmgA is the **first (ring‑opening) enzyme of the "central" homogentisate catabolic pathway** in *P. putida* (PMID 15262943):

**Peripheral (upstream) reactions** feeding homogentisate:
- **PhhAB** — phenylalanine hydroxylase: L‑Phe → L‑Tyr
- **TyrB** — aminotransferase: L‑Tyr → 4‑hydroxyphenylpyruvate (4‑HPP)
- **Hpd** — 4‑HPP dioxygenase: 4‑HPP → **homogentisate**

**Central pathway (the hmgABC operon):**
1. **HmgA** (this protein): homogentisate → **4‑maleylacetoacetate**
2. **HmgC** — maleylacetoacetate isomerase: 4‑maleylacetoacetate → 4‑fumarylacetoacetate
3. **HmgB** — fumarylacetoacetate hydrolase: 4‑fumarylacetoacetate → **fumarate + acetoacetate**

The end products (fumarate, a TCA‑cycle intermediate, and acetoacetate) let *P. putida* use Phe/Tyr — and, via the same route, **3‑hydroxyphenylacetate** — as carbon and energy sources. An engineered cassette carrying *hmgABC*, *hpd* and *tyrB* confers tyrosine utilization on heterologous bacteria, demonstrating the pathway's sufficiency (PMID 15262943).

**Regulation:** The *hmgABC* genes form a **single transcriptional unit**. The divergently transcribed gene **hmgR** encodes an **IclR‑type repressor**; **homogentisate itself is the inducer**, relieving repression when substrate is present. HmgR was reported as the **first IclR‑type regulator shown to act as a repressor of an aromatic catabolic pathway**, protecting a 17‑bp palindrome/direct‑repeat region of the P*hmg* promoter (PMID 15262943).

**Physiological consequence of loss of function:** Blocking HmgA causes homogentisate to accumulate; homogentisate auto‑oxidizes and polymerizes into the brown pigment **pyomelanin** (ochronotic pigment). This is the bacterial counterpart of the human disease **alkaptonuria**, caused by deficiency of the orthologous HGD/HGO enzyme (PMID 9244427; and analogous plant HGO loss browns soybean seed, PMID 27660165) — a cross‑kingdom confirmation of the conserved committed‑step role.

---

## 4. Localization

HmgA is a **soluble cytoplasmic enzyme**. It has no signal peptide, no transmembrane segments, and no lipidation/secretion signals in Q88E47; its substrate (homogentisate) and downstream enzymes (HmgB, HmgC) are intracellular products of cytoplasmic amino‑acid catabolism. The crystallized protein is a soluble multimer (the crystallographic asymmetric unit of 3ZDS/4AQ2/4AQ6 contains 12 chains; HGDO enzymes assemble as homo‑oligomers, and the human ortholog is a hexamer arranged as a dimer of trimers). Thus HmgA carries out its function **in the cytoplasm**.

---

## 5. Structural fold

HmgA adopts a **cupin/RmlC‑like β‑jelly‑roll core** (InterPro IPR014710) that houses the mononuclear Fe(II) site, flanked by the family‑specific HgmA N‑ and C‑domains (IPR046452/IPR046451). This fold is distinct from both catechol‑cleaving intradiol and classic extradiol dioxygenases, yet supports an analogous Fe(II)/O₂ chemistry — an example of **convergent catalytic strategy** on divergent scaffolds (PMID 23858455).

---

## 6. Hypotheses: supported vs. refuted

**Supported**
- HmgA catalyzes homogentisate + O₂ → 4‑maleylacetoacetate (direct: trapped substrate‑ and product‑bound structures of this protein; PMID 23858455).
- Catalysis uses a mononuclear non‑heme Fe(II) center coordinated by His331/His367/Glu337 (direct crystallography + matching UniProt annotation).
- HmgA is the committed central step of Phe/Tyr catabolism via the *hmgABC* operon, regulated by HmgR/homogentisate (PMID 15262943).
- Enzyme is cytoplasmic (sequence features; substrate/pathway context).

**Refuted / ruled out**
- HmgA is **not** a heme enzyme, **not** a monooxygenase, and **not** membrane‑bound.
- Gene‑symbol ambiguity was ruled out: the "hmgA" and PDB evidence map unambiguously to Q88E47/PP_4621 (no mis‑identification with unrelated "HMG" genes such as HMG‑CoA reductase or HMGB chromatin proteins).

---

## 7. Limitations and future directions

- Kinetic parameters (kcap/Km) for the wild‑type *P. putida* enzyme are referenced through mutagenesis fold‑changes; a full steady‑state kinetic table for KT2440 HmgA would sharpen the substrate‑specificity claim.
- The precise biological oligomeric state (hexamer vs. other) of the *P. putida* enzyme should be confirmed by solution methods (SEC‑MALS).
- Whether HmgA has measurable activity toward homogentisate analogs (substrate‑specificity breadth) is not fully mapped experimentally.

---

## 8. Key references
- Jeoung, Bommer, Lin, Dobbek (2013) *PNAS* — crystal structures/intermediates of this enzyme. **PMID 23858455.** (PDB 3ZDS/4AQ2/4AQ6)
- Arias‑Barrau et al. (2004) *J. Bacteriol.* — homogentisate pathway & hmgABC/hmgR regulation in *P. putida*. **PMID 15262943.**
- Qi, Lu, Lai (2016) — QM/MM mechanism. **PMID 27119315.**
- Borowski, Georgiev, Siegbahn (2005) — DFT mechanism. **PMID 16332080.**
- Granadino et al. (1997) — human HGO gene / alkaptonuria (ortholog). **PMID 9244427.**
- Stacey et al. (2016) — plant HGO loss‑of‑function phenotype (ortholog). **PMID 27660165.**


## Artifacts

- [OpenScientist final report](hmgA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hmgA-deep-research-openscientist_artifacts/final_report.pdf)