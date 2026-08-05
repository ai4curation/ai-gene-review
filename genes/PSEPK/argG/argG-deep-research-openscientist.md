---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T16:54:00.343108'
end_time: '2026-07-17T17:17:25.503237'
duration_seconds: 1405.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argG
  gene_symbol: argG
  uniprot_accession: P59604
  protein_description: 'RecName: Full=Argininosuccinate synthase {ECO:0000255|HAMAP-Rule:MF_00005};
    EC=6.3.4.5 {ECO:0000255|HAMAP-Rule:MF_00005}; AltName: Full=Citrulline--aspartate
    ligase {ECO:0000255|HAMAP-Rule:MF_00005};'
  gene_info: Name=argG {ECO:0000255|HAMAP-Rule:MF_00005}; OrderedLocusNames=PP_1088;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the argininosuccinate synthase family. Type 1
  protein_domains: Arginosuc_syn_C. (IPR048268); Arginosuc_syn_N. (IPR048267); Arginosuc_synth.
    (IPR001518); Arginosuc_synth_CS. (IPR018223); Arginosuc_synth_type_1_subfam. (IPR023434)
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
  path: argG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P59604
- **Protein Description:** RecName: Full=Argininosuccinate synthase {ECO:0000255|HAMAP-Rule:MF_00005}; EC=6.3.4.5 {ECO:0000255|HAMAP-Rule:MF_00005}; AltName: Full=Citrulline--aspartate ligase {ECO:0000255|HAMAP-Rule:MF_00005};
- **Gene Information:** Name=argG {ECO:0000255|HAMAP-Rule:MF_00005}; OrderedLocusNames=PP_1088;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the argininosuccinate synthase family. Type 1
- **Key Domains:** Arginosuc_syn_C. (IPR048268); Arginosuc_syn_N. (IPR048267); Arginosuc_synth. (IPR001518); Arginosuc_synth_CS. (IPR018223); Arginosuc_synth_type_1_subfam. (IPR023434)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argG** (gene ID: argG, UniProt: P59604) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *argG* (Argininosuccinate Synthase, UniProt P59604) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

The target is **unambiguous**. Every identifier in the UniProt record is internally consistent and matches the canonical, universally conserved bacterial gene name:

| Field | Value |
|-------|-------|
| Gene symbol | *argG* (OrderedLocusName **PP_1088**) |
| UniProt accession | **P59604** |
| Protein | Argininosuccinate synthase; **EC 6.3.4.5**; AltName: Citrulline–aspartate ligase |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) |
| Family | Argininosuccinate synthase family, **Type 1** |
| Domains | IPR048267 (Arginosuc_syn_N), IPR048268 (Arginosuc_syn_C), IPR001518, IPR018223 (conserved site), IPR023434 (type-1 subfamily) |

The symbol *argG* denotes argininosuccinate synthase in essentially all bacteria (E. coli, *Streptomyces*, *Neisseria*, cyanobacteria, *Thermotoga*), and the domain architecture and EC number all coincide. **There is no ambiguity and no risk of confusion with an unrelated gene.**

---

## 1. Summary (Answer to the Research Question)

**ArgG (PP_1088, P59604) is argininosuccinate synthase (EC 6.3.4.5), a cytoplasmic, ATP-dependent carbon–nitrogen ligase that catalyzes the penultimate, rate-limiting step of de novo L-arginine biosynthesis.** It condenses L-citrulline with L-aspartate at the expense of ATP to produce N-(L-arginino)succinate, AMP, and diphosphate (PPi). Its product is handed to argininosuccinate lyase (ArgH), which releases L-arginine and fumarate. In *P. putida* KT2440 the flux through ArgG sets intracellular arginine levels, which — under control of the master regulator ArgR — feed into c-di-GMP second-messenger signaling and biofilm/lifestyle decisions.

---

## 2. Primary Molecular Function and Reaction

ArgG catalyzes:

> **L-citrulline + L-aspartate + ATP → N-(L-argininosuccinate) + AMP + PPi**

- **Enzyme class:** EC 6.3.4.5 — a **ligase** (class 6) forming a **carbon–nitrogen bond** with hydrolysis of ATP to **AMP + PPi** (an *adenylate-forming*, ATP-pyrophosphatase-type reaction, not a kinase/phosphotransfer reaction) [PMID 38478146].
- **Substrate specificity:** highly specific for **L-citrulline** (the ureido/amidino donor) and **L-aspartate** (the amino-group donor that becomes the guanidino nitrogen of arginine); **ATP** is the required nucleotide cofactor and phosphoryl/adenylyl donor [PMID 38478146; PMID 11809762].
- **Biological role:** ArgG is the **sole enzyme** performing this step; loss of *argG* renders cells **arginine auxotrophs** (demonstrated by complementation of E. coli ΔargG strains and by *argG* deletion auxotrophs in *Neisseria* and *Streptomyces*) [PMID 32179161; PMID 2517044; PMID 3598876].

### Catalytic mechanism (structural/mechanistic evidence)

The mechanism is established from crystal structures of the bacterial ortholog (E. coli argininosuccinate synthetase, same family and Type 1 subfamily as *P. putida* ArgG) solved with ATP and with ATP + citrulline at 2.0 Å [PMID 11809762]:

1. **Step 1 (adenylation):** the ureido group of citrulline attacks the α-phosphate of ATP, forming a reactive **citrulline-adenylate (citrulline-AMP) intermediate** and releasing PPi.
2. **Step 2 (substitution):** the α-amino group of aspartate displaces AMP, forming the C–N bond of argininosuccinate.

The structures reveal **two catalytically relevant ATP conformations** and **ATP-induced conformational changes** in the nucleotide-binding domain, consistent with substrate-driven domain closure that sequesters the labile adenylate intermediate [PMID 11809762]. The two-domain architecture (N-terminal nucleotide-binding domain, IPR048267; C-terminal synthetase domain, IPR048268) places ArgG in the **N-type ATP-pyrophosphatase / adenine-nucleotide α-hydrolase** superfamily.

A second, independent bacterial structure — argininosuccinate synthetase from *Thermus thermophilus* HB8, solved free, with ATP, and with AMP-PNP + arginine + succinate (1.95–2.3 Å) — is described as **"essentially the same as that of the *E. coli* argininosuccinate synthetase"** [PMID 11844799]. It confirms that the **small (N-terminal) domain adopts the "N-type" ATP-pyrophosphatase fold with a P-loop** that binds ATP phosphates, and that **ATP and the citrulline/aspartate-mimicking substrate analogues sit adjacently in the active site in a geometry favorable for catalysis**. This P-loop corresponds directly to the **SGGLDT motif at residues 12–17 of *P. putida* P59604**. (Of note, the *T. thermophilus* enzyme shows little conformational change on binding, versus more pronounced induced fit in *E. coli* — the degree of induced fit varies among orthologs while the conserved active-site architecture and mechanism do not.)

---

## 3. Subcellular Localization and Quaternary Structure

ArgG is a **soluble cytoplasmic enzyme** (UniProt/HAMAP-Rule MF_00005 subcellular location: **Cytoplasm**). It carries no signal peptide, no lipobox, and no transmembrane segments, consistent with a housekeeping biosynthetic enzyme acting on small, charged cytoplasmic metabolites (citrulline, aspartate, ATP). All characterized orthologs are cytosolic; the mammalian ortholog ASS1 is likewise cytosolic. Its function is carried out **inside the cell, in the cytoplasm**.

The functional unit is a **homotetramer** (UniProt SUBUNIT annotation for P59604), the canonical oligomeric state of bacterial Type-1 argininosuccinate synthetases.

### Direct sequence-level evidence for the target protein (P59604)

Rather than relying solely on ortholog inference, the target 405-residue sequence itself was inspected and shown to contain the family-diagnostic catalytic motifs:

| Motif | Residues | Role |
|-------|----------|------|
| **S-G-G-L-D-T** (context `VLAYSGGLDTSVI`) | 12–17 | Glycine-rich, P-loop-like **ATP α-phosphate–binding** motif of the argininosuccinate synthase fold |
| **SHGAT** | 116 | Conserved synthase active-site segment |
| **GKGN** | 121 | Conserved substrate/nucleotide-binding segment |
| **GGTIML** | 280 | Conserved C-terminal synthetase-domain motif |

The intact SGGLDT nucleotide-binding motif is fully consistent with the adenylate-forming (ATP → AMP + PPi) chemistry, and confirms PP_1088 possesses the complete conserved catalytic machinery of the family. UniProt catalytic annotation for this exact protein (Rhea:10932): **L-citrulline + L-aspartate + ATP = 2-(Nω-L-arginino)succinate + AMP + diphosphate + H⁺**; pathway assignment: **L-arginine from L-ornithine and carbamoyl phosphate, step 2 of 3**.

---

## 4. Pathway Context

ArgG occupies the **penultimate step** of the arginine biosynthetic pathway:

```
Glutamate → ... → N-acetylornithine → Ornithine
Ornithine + carbamoyl-P → Citrulline           (ArgF / ArgI, ornithine transcarbamylase)
Citrulline + Aspartate + ATP → Argininosuccinate  (ArgG  ← THIS ENZYME)
Argininosuccinate → L-Arginine + Fumarate        (ArgH, argininosuccinate lyase)
```

Key pathway features [PMID 38478146; PMID 12730174]:

- **Rate-limiting node:** ArgG is repeatedly identified as the **rate-limiting enzyme** of arginine biosynthesis across taxa (cyanobacteria, mammals), making it the principal flux-controlling and feedback-sensitive step.
- **Nitrogen/carbon linkage:** aspartate is the nitrogen donor and its carbon skeleton is released downstream as **fumarate** (by ArgH), coupling arginine synthesis to the aspartate–fumarate shuttle and, indirectly, the TCA cycle.
- **Regulation:** in bacteria *argG* belongs to the **arginine regulon** controlled by the repressor **ArgR** (with L-arginine as corepressor). In E. coli, *argG* additionally responds to global carbon signaling (activated by the cAMP–CAP complex) [PMID 12730174].

### Genomic organization

In *P. putida* KT2440, *argG* (**PP_1088**, chromosome position 1,246,970–1,248,187, forward strand; 1,218 bp / 405 aa; KEGG orthology **K01940**, module **M00844** "ornithine → arginine") is **monocistronic/isolated**. Its neighbors are functionally unrelated and mostly on the opposite strand — *pyrC* (dihydroorotase, PP_1086), an OmpA-family outer-membrane protein (PP_1087), a conserved hypothetical protein (PP_1089), and a *bvgA*-like regulator (PP_1090). Thus, unlike the clustered *argGHCJBD* operons of some bacteria (e.g., *Thermotoga*), the *Pseudomonas* arginine-biosynthesis genes are **dispersed across the chromosome**, each independently regulated within the ArgR arginine regulon — the same monocistronic, independently regulated arrangement seen for *argG* in *E. coli* [PMID 12730174].

### *P. putida* KT2440–specific integration

In *P. putida* KT2440 (a plant-root–colonizing biocontrol/biotech organism), **ArgR is the master regulator of arginine biosynthesis and transport** [PMID 35254100]. Because both **de novo arginine biosynthesis (requiring ArgG) and arginine uptake modulate intracellular c-di-GMP** and the associated motile-to-sessile (biofilm) phenotypes [PMID 35254100], the biosynthetic flux set by ArgG indirectly participates in **second-messenger signaling and lifestyle control**. Arginine acts as a **metabolic signal** in this organism, with responses amplified in ArgR mutants [PMID 38429473]. These are downstream, pathway-level consequences of ArgG's output rather than direct catalytic roles of the enzyme itself.

### Biotechnological relevance
Because ArgG is the essential, rate-limiting step, it is a favored **metabolic-engineering target**: temperature-sensitive ArgG variants have been used as tunable "metabolic valves" to switch E. coli between growth and **citrulline overproduction** (accumulating citrulline when ArgG is inactivated) [PMID 32179161].

---

## 5. Supported and Refuted Hypotheses

**Supported (high confidence):**
- H1: *argG*/P59604 is argininosuccinate synthase, EC 6.3.4.5 — **supported** (identifier consistency + universal ortholog literature).
- H2: Reaction = citrulline + aspartate + ATP → argininosuccinate + AMP + PPi — **supported** [PMID 38478146].
- H3: Mechanism proceeds through a citrulline-adenylate intermediate with ATP-induced conformational change — **supported by ortholog crystal structures** [PMID 11809762].
- H4: Penultimate, rate-limiting step of arginine biosynthesis, upstream of ArgH — **supported** [PMID 38478146].
- H5: Cytoplasmic localization — **supported** (sequence/family inference; no targeting signals).
- H6: In *P. putida*, ArgR-regulated arginine biosynthesis links to c-di-GMP/biofilm signaling — **supported** [PMID 35254100; PMID 38429473].
- H7: *argG* (PP_1088) is a monocistronic, independently ArgR-regulated locus (arg genes dispersed, not operonic) — **supported** (KEGG/GenBank genome context; mirrors *E. coli* [PMID 12730174]).
- H8: The catalytic core adopts the "N-type" ATP-pyrophosphatase P-loop fold, matching the SGGLDT motif (res 12–17) of P59604 — **supported by two independent ortholog structures** [PMID 11809762; PMID 11844799].

**Refuted / ruled out:**
- The gene is **not** ambiguous and does **not** correspond to an unrelated "argG"-symbol gene in another context; all evidence converges on argininosuccinate synthase.
- ArgG is **not** a transporter, structural protein, or a phosphotransfer (kinase) enzyme — it is an adenylate-forming ligase.

---

## 6. Evidence Types and Confidence

- **Direct structural/mechanistic evidence** (two independent bacterial ortholog crystal structures with substrates — *E. coli* and *T. thermophilus*, "essentially the same") — fold and mechanism [PMID 11809762; PMID 11844799].
- **Direct biochemical evidence** (purified ArgG kinetics, feedback inhibition) in cyanobacteria — reaction and rate-limiting status [PMID 38478146].
- **Genetic evidence** (auxotrophy, complementation, temperature-sensitive alleles) — essentiality and pathway position [PMID 32179161; PMID 2517044; PMID 3598876].
- **Organism-specific physiology/genetics** in *P. putida* KT2440 — regulation and signaling integration [PMID 35254100; PMID 38429473].
- **Bioinformatic/evolutionary inference** — HAMAP rule MF_00005, InterPro domains, family membership (Type 1) transfer the mechanism from characterized orthologs to PP_1088.

Confidence is **high**: the enzyme is one of the most highly conserved and well-characterized biosynthetic enzymes in biology, and the *P. putida* protein is a canonical Type-1 family member.

---

## 7. Limitations and Future Directions

- No crystal structure or in-vitro kinetic characterization of the *P. putida* KT2440 ArgG protein **itself** was found; the mechanism/specificity is inferred from orthologs (E. coli, cyanobacteria) sharing the same family and conserved active-site residues. Direct enzymology (Km for citrulline/aspartate/ATP, arginine feedback sensitivity) of PP_1088 would confirm the transfer.
- The precise contribution of ArgG flux (versus arginine uptake) to c-di-GMP pools in *P. putida* remains only partially resolved [PMID 35254100; PMID 37550221].
- Oligomeric state in *P. putida* (bacterial AS enzymes are typically homotetramers) was not directly verified for PP_1088.


## Artifacts

- [OpenScientist final report](argG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argG-deep-research-openscientist_artifacts/final_report.pdf)