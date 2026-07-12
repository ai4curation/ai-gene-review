---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:23:54.437427'
end_time: '2026-07-11T17:36:43.171185'
duration_seconds: 768.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: aceE
  gene_symbol: aceE
  uniprot_accession: Q88QZ5
  protein_description: 'RecName: Full=Pyruvate dehydrogenase E1 component {ECO:0000256|ARBA:ARBA00017172,
    ECO:0000256|PIRNR:PIRNR000156}; EC=1.2.4.1 {ECO:0000256|ARBA:ARBA00012281, ECO:0000256|PIRNR:PIRNR000156};'
  gene_info: Name=aceE {ECO:0000313|EMBL:AAN65970.1}; OrderedLocusNames=PP_0339 {ECO:0000313|EMBL:AAN65970.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: PDC_E1_N. (IPR035807); PDH/Transketolase. (IPR051157); PDH_E1.
    (IPR004660); PDH_E1_M. (IPR041621); THDP-binding. (IPR029061)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: aceE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: aceE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QZ5
- **Protein Description:** RecName: Full=Pyruvate dehydrogenase E1 component {ECO:0000256|ARBA:ARBA00017172, ECO:0000256|PIRNR:PIRNR000156}; EC=1.2.4.1 {ECO:0000256|ARBA:ARBA00012281, ECO:0000256|PIRNR:PIRNR000156};
- **Gene Information:** Name=aceE {ECO:0000313|EMBL:AAN65970.1}; OrderedLocusNames=PP_0339 {ECO:0000313|EMBL:AAN65970.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PDC_E1_N. (IPR035807); PDH/Transketolase. (IPR051157); PDH_E1. (IPR004660); PDH_E1_M. (IPR041621); THDP-binding. (IPR029061)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aceE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aceE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aceE** (gene ID: aceE, UniProt: Q88QZ5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *aceE* (Pyruvate Dehydrogenase E1 component) in *Pseudomonas putida* KT2440

**Target:** UniProt **Q88QZ5** | Gene **aceE** | Ordered locus **PP_0339**
**Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) — PSEPK
**EC:** 1.2.4.1 | **Cofactor:** Thiamine diphosphate (ThDP/TPP)

---

## 1. Summary (Answer to the Research Question)

*aceE* (PP_0339, Q88QZ5) encodes the **E1 component (pyruvate dehydrogenase, EC 1.2.4.1)** of the **pyruvate dehydrogenase multienzyme complex (PDHc)**. Its primary function is to catalyze the **first and rate-limiting step** of the complex: the **thiamine-diphosphate (ThDP)-dependent oxidative decarboxylation of pyruvate**, releasing CO₂ and generating a ThDP-bound C2α-hydroxyethylidene (enamine) intermediate, which E1 then uses to **reductively acetylate the lipoyl (lipoamide) prosthetic group of the E2 component**. Through the sequential action of E1→E2→E3 the complex converts **pyruvate + CoA + NAD⁺ → acetyl-CoA + CO₂ + NADH**, the "link reaction" connecting glycolysis to the citric acid cycle. In *P. putida*, whose glycolysis runs almost exclusively through the Entner–Doudoroff/EDEMP route, this reaction is the principal gateway feeding pyruvate-derived carbon into acetyl-CoA for the TCA cycle, energy metabolism, and biosynthesis. The enzyme functions as a **homodimeric peripheral subunit** that is **non-covalently tethered to the E2 structural core** of a large **soluble cytoplasmic** assembly.

---

## 2. Gene / Protein Identity Verification

| Attribute | Value | Consistency check |
|---|---|---|
| Gene symbol | *aceE* | Matches canonical name for PDH E1 in Gram-negative bacteria (as in *E. coli aceEF-lpd* operon) ✔ |
| Protein | Pyruvate dehydrogenase E1 component | Matches UniProt RecName ✔ |
| EC | 1.2.4.1 | Pyruvate dehydrogenase (acetyl-transferring), ThDP-dependent ✔ |
| Domains | PDC_E1_N (IPR035807), PDH_E1 (IPR004660), PDH_E1_M (IPR041621), THDP-binding (IPR029061), PDH/Transketolase (IPR051157) | All diagnostic of the ThDP-dependent 2-oxoacid dehydrogenase E1 family ✔ |
| Organism | *P. putida* KT2440 | ✔ |

**Verdict:** The gene symbol, protein description, EC number, and domain architecture are fully mutually consistent. This is an unambiguous, well-characterized enzyme family; annotation is confident. (Note: "aceE" is not ambiguous in bacteria — it is the standard designator for the PDH E1α/E1 subunit. Care is only needed not to conflate the bacterial single-chain E1 with the eukaryotic split E1α/E1β subunits PDHA1/PDHB.)

**Sequence-based orthology evidence (this work):** The UniProt sequence of Q88QZ5 is an **881-aa single polypeptide**. A global Needleman–Wunsch alignment against *E. coli* K-12 aceE (P0AFG8/ODP1_ECOLI, 887 aa) gives **61.9% amino-acid identity** (545/881 identical residues). This is far above the ~30% homology "twilight zone", establishing Q88QZ5 as a **confident ortholog** of the biochemically characterized *E. coli* E1p and justifying transfer of the *E. coli* mechanistic, kinetic, and structural data below. The single ~880-aa chain (vs. the split eukaryotic E1α ~360 aa + E1β ~330 aa) confirms the **gammaproteobacterial single-chain E1** architecture that functions as a homodimer. The conserved ThDP-binding **GDG** motif is present (~residue 224).

---

## 3. Primary Molecular Function — the Catalyzed Reaction

**Overall complex reaction (link reaction):**
> pyruvate + CoA-SH + NAD⁺ → acetyl-CoA + CO₂ + NADH + H⁺

**Step catalyzed specifically by E1 (aceE):**
1. **Substrate binding & decarboxylation.** Pyruvate binds at the ThDP cofactor. The thiazolium C2-ylide attacks the pyruvate carbonyl to form **2-(2-lactyl)-ThDP (LThDP)**, which is decarboxylated (loss of CO₂) to yield the resonance-stabilized **C2α-carbanion/enamine (2-α-hydroxyethylidene-ThDP)** intermediate.
2. **Reductive acetylation.** The enamine reduces and acetylates the **dithiolane of the lipoyl group** carried on E2's mobile lipoyl domain, transferring the acetyl (2-carbon) unit and regenerating ThDP.

**Substrate specificity:** E1 (aceE) is specific for **pyruvate** as the 2-oxo-acid substrate (2-oxoglutarate is handled by the paralogous OGDC E1o; branched-chain 2-oxoacids by BCKDH). Specificity is imposed by the ThDP-proximal substrate pocket characteristic of the PDH_E1 family. As a ThDP-dependent enzyme, E1 catalysis proceeds through covalent cofactor intermediates common to the ThDP superfamily (transketolase, 2-oxoacid dehydrogenases, decarboxylases).

**Ordered reaction sequence (E1's place in it):** "The reaction starts with a ThDP-dependent decarboxylation on E1 to an enamine/C2α carbanion, followed by oxidation and acetyl transfer to form S-acetyldihydrolipoamide E2, and then transfer of this acetyl group from the LD [lipoyl domain] to coenzyme A on the [E2 catalytic domain]. The dihydrolipoamide E2 is finally reoxidized by the E3 component" (Song & Jordan, 2012, PMID 22413895). In **Gram-negative bacteria** — the group that includes *P. putida* — the complex comprises **E1p (pyruvate dehydrogenase/decarboxylase), E2p (dihydrolipoyl acetyltransferase forming a 24-subunit core with multiple E1p/E3 binding sites and mobile lipoyl domains), and E3 (dihydrolipoyl dehydrogenase)**; the closely related *Azotobacter vinelandii* γ-proteobacterial complex is the best-characterized structurally (de Kok et al., 1998, PMID 9655933).

**Kinetic/mechanistic evidence:** In the closely homologous *E. coli* E1p (aceE), pre-steady-state kinetics show that **formation of the LThDP predecarboxylation intermediate is rate-limiting**, and that disorder→order transitions of active-site loops upon substrate binding gate covalent catalysis (Balakrishnan et al., 2012, PMID 23088422). E1 is the **first and rate-limiting** component of the whole complex (Chan et al., 2023, PMID 36723268). Radical/redox mechanisms and the coupling of decarboxylation to reductive acyl transfer in ThDP 2-oxoacid dehydrogenases are reviewed by Tittmann (2009, PMID 19476487).

**Cofactor-fold integrity (this work):** Sequence analysis of Q88QZ5 confirms an intact ThDP/Mg²⁺-binding signature — a **GDG** motif at residue 224 followed ~24 residues downstream by the conserved Asn (…M**GDG**E…IFVI**N**CN…), the diagnostic motif of the transketolase/2-oxoacid-dehydrogenase E1 ThDP-binding fold — indicating a **catalytically competent, non-degenerate** enzyme.

---

## 4. Pathway Context / Biological Process

- **Position in metabolism:** PDHc catalyzes the **irreversible link reaction** between glycolysis and the citric-acid cycle, converting the glycolytic end-product pyruvate into acetyl-CoA — a key substrate for the TCA cycle and fatty-acid synthesis (Bothe & Zdanowicz, 2026, PMID 40808219; Škerlová et al., 2021, PMID 34489474).
- ***P. putida*-specific context:** KT2440 **lacks a functional Embden–Meyerhof–Parnas pathway**; glucose is catabolized largely via periplasmic oxidation to gluconate and the **Entner–Doudoroff pathway**, with a cyclic **EDEMP** architecture that also boosts NADPH supply (Nikel et al., 2015, PMID 26350459). Regardless of upstream route, the **pyruvate → acetyl-CoA** conversion performed by aceE-containing PDHc is the dominant oxidative decarboxylation node feeding the TCA cycle in this obligate aerobe.
- **Downstream products:** Acetyl-CoA feeds the TCA cycle (energy/reducing equivalents), lipid/polyhydroxyalkanoate precursor supply, and biosynthesis; NADH feeds the respiratory chain.
- **Genomic/operon context (this work):** In *P. putida* KT2440, aceE (PP_0339) is immediately adjacent to **aceF (PP_0338, Q88QZ6)**, the **E2 acetyltransferase component of PDHc** (EC 2.3.1.12, dihydrolipoyllysine-residue acetyltransferase, 546 aa). This **aceEF gene cluster** mirrors the *E. coli aceEF-lpd* operon and provides organism-specific genomic evidence that PP_0339 is the E1 of a co-expressed, functional PDH complex whose cognate E2 core sits next to it. Flanking genes (PP_0337 c-di-GMP phosphodiesterase; PP_0340 *glnE*; PP_0341 *waaF*) are unrelated, and the shared E3 (dihydrolipoamide dehydrogenase, *lpd/lpdG*) is encoded elsewhere in the genome, as is typical.
- **Regulation (family-level inference):** In *E. coli* the *aceEF-lpd* operon is repressed by **PdhR**, a pyruvate-sensing transcriptional regulator; homologous pyruvate-responsive control is expected for the *P. putida* locus. (Direct experimental regulation data for PP_0339 were not retrieved here and are flagged as a knowledge gap.)

---

## 5. Structural Organization & Subcellular Localization

- **Quaternary structure:** PDHc is one of the largest known enzyme assemblies (~5–12 MDa). **E2 (dihydrolipoamide acetyltransferase) forms the structural core** (octahedral/cubic in most bacteria, icosahedral in others), and **E1 and E3 bind the core as peripheral subunits** (Bothe & Zdanowicz, 2026, PMID 40808219). Complex integrity is maintained by **non-covalent tethering of the peripheral E1 and E3 to E2 via the E2 peripheral-subunit-binding domain (PSBD)** (Arjunan et al., 2014, PMID 25210042).
- **Oligomeric state of E1:** In gammaproteobacteria (which includes *Pseudomonas*), E1p is a **homodimer** (Meinhold et al., 2024, PMID 38324697; Arjunan et al., 2014). Each aceE monomer contributes to a shared active-site environment for ThDP.
- **Substrate channeling:** E2's covalently attached, **swinging lipoyl domains** shuttle reaction intermediates between the E1, E2, and E3 active sites; cryo-EM of the native *E. coli* E2 core reveals how lipoyl domains dock at active sites (Škerlová et al., 2021, PMID 34489474).
- **Localization:** The complex is a **soluble cytoplasmic** assembly in bacteria (in eukaryotes it is mitochondrial). aceE therefore carries out its function in the **cytoplasm/cytosol** of *P. putida*.

---

## 6. Supported vs. Refuted Hypotheses

**Supported:**
- H1 — aceE is a ThDP-dependent pyruvate dehydrogenase E1 (EC 1.2.4.1) catalyzing the first, rate-limiting step of PDHc. **Supported** (domain architecture + homolog kinetics).
- H2 — Its physiological role is producing acetyl-CoA linking glycolysis (ED/EDEMP in *P. putida*) to the TCA cycle. **Supported.**
- H3 — aceE acts as a peripheral homodimer tethered to the cytoplasmic E2 core. **Supported** (structural literature).

**Refuted / excluded:**
- aceE is **not** an isolated soluble monomeric enzyme, and **not** a membrane transporter or structural protein — it is an enzymatic subunit of a large multienzyme complex.
- The bacterial *aceE* is a **single-chain E1**, distinct from the split eukaryotic E1α (PDHA1)/E1β architecture; literature on human PDHA1 describes the orthologous chemistry but a different subunit organization (excluded as a direct structural analogue).

---

## 7. Evidence Quality & Limitations

- **Strength:** The catalytic chemistry, cofactor, mechanism, and complex architecture are established by decades of precise biochemistry, kinetics, X-ray crystallography, and cryo-EM — largely on the near-identical *E. coli* E1p and on other bacterial/mammalian PDHc. Given very high sequence/domain conservation, transfer of this mechanism to *P. putida* PP_0339 is well justified.
- **Limitations / gaps specific to *P. putida* KT2440:**
  1. No *P. putida*-specific crystal/cryo-EM structure or steady-state kinetic constants (Km for pyruvate, kcat) for PP_0339 were retrieved — inference is by orthology.
  2. Transcriptional regulation of the *P. putida aceE* locus (PdhR-like control, growth-condition dependence) was not directly documented here.
  3. Quantitative flux through PDH vs. alternative pyruvate-consuming routes (e.g., pyruvate carboxylation, transhydrogenase-linked cycles) in KT2440 warrants organism-specific confirmation.
- **Future directions:** Determine PP_0339 kinetic parameters and the *P. putida* PDHc structure; test PdhR-type regulation; ¹³C-flux quantification of the pyruvate→acetyl-CoA node under industrially relevant carbon sources.

---

## 8. Key References
- Bothe & Zdanowicz (2026) *Structural diversity of pyruvate dehydrogenase complexes.* PMID 40808219
- Škerlová et al. (2021) *Structure of the native pyruvate dehydrogenase complex reveals the mechanism of substrate insertion.* PMID 34489474
- Arjunan et al. (2014) *Novel binding motif… E1p–E2p subcomplex from the E. coli PDH complex.* PMID 25210042
- Balakrishnan et al. (2012) *Pre-steady-state rate constants on the E. coli PDH complex… loop movement controls the rate-limiting step.* PMID 23088422
- Chan et al. (2023) *Furan-based inhibitors of pyruvate dehydrogenase (PDH E1 as TPP-dependent, rate-limiting).* PMID 36723268
- Tittmann (2009) *Reaction mechanisms of thiamin diphosphate enzymes: redox reactions.* PMID 19476487
- Meinhold et al. (2024) *Dimerization of a 5-kDa domain defines the architecture of the 5-MDa gammaproteobacterial PDH complex.* PMID 38324697
- Nikel et al. (2015) *P. putida KT2440 metabolizes glucose through an ED/EMP/PPP cycle (EDEMP).* PMID 26350459
- Wang et al. (2014) *Structure and function of the E2 catalytic domain in E. coli PDHc.* PMID 24742683
- Träger et al. (2026) *The Pyruvate Dehydrogenase Complex: A 90-Year-Old Enigma…* PMID 42334543
- Song & Jordan (2012) *Interchain acetyl transfer in the E2 component of bacterial pyruvate dehydrogenase… (defines the ordered E1→E2→E3 reaction).* PMID 22413895
- de Kok et al. (1998) *The pyruvate dehydrogenase multi-enzyme complex from Gram-negative bacteria.* PMID 9655933


## Artifacts

- [OpenScientist final report](aceE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](aceE-deep-research-openscientist_artifacts/final_report.pdf)