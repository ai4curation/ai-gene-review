---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T00:08:18.689726'
end_time: '2026-08-11T00:19:56.805226'
duration_seconds: 698.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: petA
  gene_symbol: petA
  uniprot_accession: Q88N95
  protein_description: 'RecName: Full=Ubiquinol-cytochrome c reductase iron-sulfur
    subunit {ECO:0000256|ARBA:ARBA00019816, ECO:0000256|RuleBase:RU004494}; EC=7.1.1.8
    {ECO:0000256|ARBA:ARBA00012951, ECO:0000256|RuleBase:RU004494};'
  gene_info: Name=petA {ECO:0000313|EMBL:AAN66941.1}; OrderedLocusNames=PP_1317 {ECO:0000313|EMBL:AAN66941.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the Rieske iron-sulfur protein family.
  protein_domains: Rieske_2Fe-2S. (IPR017941); Rieske_2Fe-2S_sf. (IPR036922); Rieske_Fe-S_prot.
    (IPR014349); Rieske_Fe-S_prot_C. (IPR005805); TAT_signal. (IPR006311)
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
  path: petA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: petA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N95
- **Protein Description:** RecName: Full=Ubiquinol-cytochrome c reductase iron-sulfur subunit {ECO:0000256|ARBA:ARBA00019816, ECO:0000256|RuleBase:RU004494}; EC=7.1.1.8 {ECO:0000256|ARBA:ARBA00012951, ECO:0000256|RuleBase:RU004494};
- **Gene Information:** Name=petA {ECO:0000313|EMBL:AAN66941.1}; OrderedLocusNames=PP_1317 {ECO:0000313|EMBL:AAN66941.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Rieske iron-sulfur protein family.
- **Key Domains:** Rieske_2Fe-2S. (IPR017941); Rieske_2Fe-2S_sf. (IPR036922); Rieske_Fe-S_prot. (IPR014349); Rieske_Fe-S_prot_C. (IPR005805); TAT_signal. (IPR006311)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "petA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'petA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **petA** (gene ID: petA, UniProt: Q88N95) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *petA* (Q88N95, PP_1317) in *Pseudomonas putida* KT2440

## 1. Summary — Answer to the Research Question

*petA* (locus **PP_1317**, UniProt **Q88N95**) encodes the **Rieske iron–sulfur protein (ISP)**, one of the three catalytic subunits of the respiratory **cytochrome *bc*₁ complex** (ubiquinol:cytochrome *c* oxidoreductase / Complex III; **EC 7.1.1.8**). Its defining function is to carry a **high-potential [2Fe-2S] "Rieske" cluster** that abstracts the first electron from **ubiquinol** at the enzyme's quinol-oxidation (Qo) site and passes it to **cytochrome *c*₁**, the electron-bifurcating step that drives the protonmotive **Q-cycle**. The reaction it enables is:

> QH₂ (ubiquinol) + 2 cytochrome *c* (oxidized) → Q (ubiquinone) + 2 cytochrome *c* (reduced) + 2 H⁺(periplasm)

The Rieske subunit performs its chemistry at the **periplasmic (positive) face of the cytoplasmic membrane**: it is a membrane-anchored protein whose cluster-bearing head domain sits in the periplasm, and it is delivered there **folded, with its metal cofactor pre-assembled, by the twin-arginine translocation (Tat) system**. In *P. putida* KT2440 the *bc*₁ complex is the central hub that oxidizes the ubiquinol pool and supplies reduced cytochrome *c* to the cytochrome-*c* terminal oxidases (cbb₃- and aa₃-type) of the branched aerobic respiratory chain, thereby contributing to protonmotive force and ATP synthesis.

**Identity verification:** The gene symbol *petA*, the annotated protein description ("Ubiquinol-cytochrome c reductase iron-sulfur subunit"), the Rieske iron-sulfur protein family assignment, and the InterPro domain set (Rieske_2Fe-2S, Rieske_Fe-S_prot_C, TAT_signal) are mutually consistent and match the primary literature on bacterial PetA proteins. This is the correct gene; no ambiguity was found.

---

## 2. Molecular Identity and Domain Architecture

| Feature | Value | Source |
|---|---|---|
| UniProt accession | Q88N95 | UniProt |
| Gene / locus | *petA* / PP_1317 | UniProt / EMBL AAN66941.1 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054) | UniProt |
| Enzyme classification | EC 7.1.1.8 (ubiquinol:cytochrome *c* reductase, translocase class) | UniProt |
| Family | Rieske iron-sulfur protein family | UniProt |
| Cofactor | [2Fe-2S] Rieske cluster, His₂Cys₂ ligation | Family/literature |
| Key domains | Rieske_2Fe-2S (IPR017941/IPR036922), Rieske_Fe-S_prot (IPR014349), Rieske_Fe-S_prot_C (IPR005805), **TAT_signal (IPR006311)** | InterPro |

The protein has the canonical three-part bacterial Rieske ISP architecture: (i) an **N-terminal Tat signal / membrane anchor**, (ii) a flexible hinge, and (iii) a **C-terminal soluble "head" domain** that folds around the [2Fe-2S] cluster.

**Direct sequence verification (this study).** Analysis of the actual 197-residue Q88N95 sequence confirms both hallmark features specific to PP_1317, not merely inferred by family transfer:
- **Twin-arginine (Tat) signal:** the N-terminus `MSNDGVNAG**RRR**FLVAA…` contains the twin(triple)-arginine motif at residues 10–12 followed by `FLV`, matching the (S/T)-**RR**-x-Φ-Φ Tat consensus.
- **Rieske [2Fe-2S] His₂Cys₂ ligand boxes:** Box I `**C124**-T-**H126**-L-G-C129` and Box II `C152-P-**C154**-**H155**`. Box I matches the **PROSITE PS00199 Rieske signature** (C-x-H-x-[GA]-C). The four cluster ligands are therefore **Cys124/His126** (to one Fe) and **Cys154/His155** (to the other Fe), with the conserved cluster-stabilizing **disulfide Cys129–Cys152** — the textbook high-potential *bc*₁/*b₆f* Rieske arrangement.
- **Redox-tuning serine:** a conserved **Ser157** (in the `H155-G-S157` motif just after Box II) occupies the position that, in *Rhodobacter sphaeroides* Rieske (Ser154), hydrogen-bonds to a cluster sulfur and raises the midpoint potential by ~140 mV [PMID 14567701]. Its presence predicts a **high, positive E_m** and firmly distinguishes PP_1317 from low-potential (~−150 mV) aromatic-oxygenase Rieske ferredoxins — an important discrimination in *Pseudomonas*, a genus rich in ring-hydroxylating Rieske oxygenases.

The bacterial *bc*₁ complex is encoded by the **petABC operon**, whose three subunits are the Rieske iron-sulfur protein (*petA*), the *b*-type cytochrome (*petB*), and the *c*₁-type cytochrome (*petC*) [PMID 15948965]. PetA is thus one component of a heteromeric, usually dimeric, membrane enzyme.

**Operon context in KT2440 (this study, via KEGG).** PP_1317 is the first gene of a compact three-gene *bc*₁ operon in the *P. putida* KT2440 genome:

| Locus | Product | KEGG Ortholog | Subunit |
|---|---|---|---|
| **PP_1317** | ubiquinol-cytochrome *c* reductase iron-sulfur subunit | K00411 (EC 7.1.1.8) | **petA — Rieske ISP** |
| PP_1318 | ubiquinol-cytochrome *c* reductase cytochrome *b* subunit | K00412 | petB — cytochrome *b* |
| PP_1319 | ubiquinol-cytochrome *c* reductase cytochrome *c*₁ subunit | K00413 | petC — cytochrome *c*₁ |

Flanking genes are unrelated (PP_1315/1316 = ribosomal proteins L13/S9; PP_1320 = stringent starvation protein A), so the three *pet* genes form the complete complex. There is a **single** *petA* locus in KT2440 (unlike organisms with duplicated Rieske genes), making PP_1317 the sole Rieske subunit of the complex.

---

## 3. Primary Function — The Catalyzed Reaction and Substrate Specificity

### 3.1 Role within Complex III
PetA is the **electron-input gatekeeper** of the *bc*₁ complex. Experimental studies in bacterial homologs identify it directly as "the Rieske Fe-S subunit of the ubiquinol-cytochrome c reductase" [PMID 23593508]. The overall enzyme "couples electron transfer from ubiquinol to cytochrome *c* with generation of proton motive force which fuels ATP synthesis" [PMID 21996020].

### 3.2 Substrate specificity
- **Electron donor / substrate:** **ubiquinol (QH₂)**, oxidized at the Qo (Qp) site located at the periplasmic side of cytochrome *b*.
- **Immediate electron acceptor:** the heme of **cytochrome *c*₁** (the *petC* product), which in turn reduces soluble/periplasmic **cytochrome *c***.
- The Rieske cluster's high, positive midpoint potential poises it to accept an electron from quinol and hand it "downhill" to cytochrome *c*₁.

### 3.3 The [2Fe-2S] cofactor and proton-coupled electron transfer (PCET)
The functional heart of PetA is its **[2Fe-2S] cluster with unique {His₂Cys₂} ligation**; the two histidine ligands "allow for coupling of electron and proton transfer (PCET) during quinol oxidation in respiratory and photosynthetic ET chains" [PMID 24506804]. Because the surface-exposed histidines both coordinate one iron and titrate protons, the cluster's reduction potential is **pH-dependent**, an effect "attributed to coupled deprotonation of the two histidine ligands" (apparent pKa ≈ 7.5 and 9.2 in the oxidized state) [PMID 14567701; DFT confirmation PMID 12072969]. High-potential *bc*₁-type Rieske proteins have midpoint potentials in the +150 to +350 mV range; a directly measured bacterial PetA value is **E_m ≈ +275 mV** [PMID 15948965].

### 3.4 Mechanistic consequence — the Q-cycle
By taking **one** electron (and effectively the associated proton) from ubiquinol, PetA forces the **bifurcation** of the two electrons of QH₂: one electron travels via the high-potential chain (Rieske → cyt *c*₁ → cyt *c*), while the second goes through the low-potential chain (cyt *b*_L → cyt *b*_H) to reduce quinone at the Qi site. This bifurcation is the essence of the protonmotive Q-cycle, releasing 2 H⁺ to the periplasm per QH₂ oxidized and doubling the charge separation efficiency of the complex. In many organisms the Rieske head domain physically **swivels** between the quinol site and cytochrome *c*₁ to shuttle the electron, making PetA a mobile catalytic element rather than a static wire.

---

## 4. Subcellular Localization and Topology

- **Location:** integral to the **cytoplasmic (inner) membrane**, with the catalytic [2Fe-2S] head domain exposed to the **periplasm** (the electropositive P-side). This is where it meets both ubiquinol (in the membrane) and cytochrome *c* (periplasmic).
- **Biogenesis / import route:** the [2Fe-2S] cluster is assembled in the **cytoplasm**, so PetA must be translocated **already folded and cofactor-loaded**. It therefore uses the **twin-arginine translocation (Tat) pathway**, consistent with its annotated TAT_signal domain. In *Legionella pneumophila*, "the Tat pathway is necessary for correct membrane insertion of PetA" [PMID 17188684]. In *Shewanella oneidensis*, mislocalization of PetA "predominantly accounts for the aerobic growth defect of Tat mutants," and importantly "the signal sequence in PetA appears to be resistant to cleavage after the protein is inserted into the cytoplasmic membrane" — i.e., the Tat signal is **retained as an N-terminal transmembrane anchor** [PMID 23593508].

This topology unifies the protein's function and localization: a single N-terminal membrane anchor tethers PetA in the inner membrane while its Tat-delivered, cluster-bearing head sits in the periplasm precisely where quinol oxidation and cytochrome *c* reduction occur.

---

## 5. Biochemical Pathway Context in *P. putida* KT2440

*P. putida* KT2440 has a **branched aerobic respiratory chain with several terminal oxidases** [PMID 16958757]. Electrons enter a common **ubiquinone/ubiquinol pool** from primary dehydrogenases (NADH dehydrogenase, succinate dehydrogenase, various substrate dehydrogenases). From that pool there are two competing routes to O₂:

1. **Quinol-oxidase branch** (bc₁-independent): the cytochrome *bo*₃/cyo quinol oxidase and the cyanide-insensitive oxidase (CIO) reduce O₂ directly from ubiquinol.
2. **Cytochrome-*c* branch** (bc₁-dependent): the **cytochrome *bc*₁ complex (PetABC)** oxidizes ubiquinol and reduces **cytochrome *c***, which then donates to the **cbb₃-1, cbb₃-2, and aa₃-type cytochrome *c* oxidases** [PMID 16958757].

**petA/bc₁ is the obligatory entry point of the cytochrome-*c* branch.** Reflecting this, cytochrome *c* reductase (the *bc*₁ complex) was identified as "a key enzyme involved in the extracellular electron transfer pathway" in *P. putida* toward transition-metal complexes [PMID 32678505]. The parallel quinol-oxidase branch provides partial redundancy, so loss of *bc*₁ is often not lethal under standard aerobic conditions — but *bc*₁ is required for cytochrome-*c*-linked respiration and for maximizing protonmotive-force/ATP yield, and it becomes important under conditions favoring the high-affinity cbb₃/aa₃ oxidases.

---

## 6. Evidence Basis

- **Sequence / domain inference (bioinformatic):** UniProt/InterPro assignment to the Rieske iron-sulfur protein family with Rieske_2Fe-2S and TAT_signal domains; membership in the petABC operon architecture [PMID 15948965]. **Direct analysis of the Q88N95 primary sequence (this study)** independently confirms the twin-arginine Tat motif (residues 10–12) and the His₂Cys₂ Rieske cluster-ligand boxes (Cys124/His126 + Cys154/His155; disulfide Cys129–Cys152).
- **Biophysical / structural:** {His₂Cys₂} [2Fe-2S] ligation and PCET behavior established by synthetic Rieske models [PMID 24506804] and by protein-film voltammetry / DFT on native Rieske proteins [PMID 14567701; PMID 12072969]; measured E_m ≈ +275 mV for bacterial PetA [PMID 15948965]; 2.7 Å X-ray structure of the dimeric bacterial *bc*₁ complex confirming ISP architecture and function [PMID 21996020].
- **Genetic / physiological (experimental):** Tat-dependence of PetA membrane insertion [PMID 17188684; PMID 23593508]; branched respiratory-chain organization and terminal-oxidase redundancy in *P. putida* KT2440 [PMID 16958757]; functional role of cytochrome *c* reductase in *P. putida* electron transfer [PMID 32678505]; functional interchangeability/essentiality of Rieske genes for *bc*₁ activity [PMID 15948965].

Note: the direct experimental studies above were performed largely in bacterial homologs (*Shewanella*, *Legionella*, *Rubrivivax*, *Paracoccus*, *Rhodobacter*, *Thermus*) rather than in *P. putida* itself; the annotation of PP_1317 rests on the very high conservation of the Rieske ISP family and the congruence of family, domains, operon context, and *P. putida*-specific respiratory-chain data.

---

## 7. Supported vs. Refuted Hypotheses

**Supported**
- H1: petA/PP_1317 is the Rieske [2Fe-2S] subunit of ubiquinol:cytochrome *c* reductase (Complex III). ✔
- H2: It functions via a His₂Cys₂ [2Fe-2S] cluster performing proton-coupled electron transfer from ubiquinol. ✔
- H3: It is membrane-anchored with a periplasm-facing head and is imported folded via the Tat pathway (uncleaved signal = anchor). ✔
- H4: In *P. putida* it feeds the cytochrome-*c* branch (cbb₃/aa₃ oxidases) of a branched aerobic respiratory chain. ✔

**Refuted / Excluded**
- The "petA/PetA" here is **not** a plant/cyanobacterial cytochrome *b₆f* apocytochrome *f* (also historically called *petA* in chloroplasts). The organism (*P. putida*, a heterotrophic proteobacterium) and the RecName "iron-sulfur subunit" exclude that interpretation; only the *bc*₁ Rieske assignment is consistent.
- petA is **not** an aromatic-ring-hydroxylating oxygenase Rieske ferredoxin (those are low-potential, cytoplasmic, ~ −150 mV) — the high-potential *bc*₁ family assignment, cytochrome *c* reductase EC number, KEGG ortholog K00411, petABC operon context, and the positive sequence markers (PROSITE PS00199 Box I, CPCH Box II, cluster-stabilizing disulfide, redox-tuning Ser157) all rule this out. This is a meaningful discrimination because *Pseudomonas* genomes encode many Rieske-domain oxygenases for aromatic-compound catabolism; PP_1317 is specifically the respiratory *bc*₁ Rieske subunit.

---

## 8. Limitations and Future Directions

- No *P. putida* KT2440-specific structural or knockout study of PP_1317 was found; conclusions are inferred from strong family conservation and homolog experiments.
- Direct measurement of the *P. putida* PetA midpoint potential, cluster EPR signature, and Tat-signal cleavage status would confirm the inferred parameters.
- A targeted *petA* deletion in KT2440, with respirometry across carbon sources and oxygen tensions, would quantify the physiological contribution of the cytochrome-*c* branch versus the redundant quinol oxidases.

---

### Key References
- PMID 23593508 — PetA identified as Rieske Fe-S subunit of ubiquinol-cytochrome c reductase; Tat mislocalization; uncleaved signal anchor.
- PMID 15948965 — petABC operon composition; measured Rieske E_m ≈ +275 mV; [2Fe-2S] insertion.
- PMID 24506804 — {His₂Cys₂} [2Fe-2S] ligation and proton-coupled electron transfer during quinol oxidation.
- PMID 14567701 / 12072969 — pH-dependent redox potential from His-ligand deprotonation.
- PMID 17188684 — Tat pathway required for correct PetA membrane insertion.
- PMID 21996020 — Bacterial *bc*₁ X-ray structure; couples ubiquinol→cyt *c* transfer to PMF/ATP.
- PMID 16958757 — *P. putida* KT2440 branched aerobic respiratory chain / terminal oxidases.
- PMID 32678505 — Cytochrome *c* reductase key in *P. putida* electron transfer.


## Artifacts

- [OpenScientist final report](petA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](petA-deep-research-openscientist_artifacts/final_report.pdf)