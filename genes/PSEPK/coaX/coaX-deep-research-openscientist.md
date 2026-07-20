---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:08:11.943121'
end_time: '2026-07-18T13:22:57.245431'
duration_seconds: 885.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: coaX
  gene_symbol: coaX
  uniprot_accession: Q88QQ0
  protein_description: 'RecName: Full=Type III pantothenate kinase {ECO:0000255|HAMAP-Rule:MF_01274};
    EC=2.7.1.33 {ECO:0000255|HAMAP-Rule:MF_01274}; AltName: Full=PanK-III {ECO:0000255|HAMAP-Rule:MF_01274};
    AltName: Full=Pantothenic acid kinase {ECO:0000255|HAMAP-Rule:MF_01274};'
  gene_info: Name=coaX {ECO:0000255|HAMAP-Rule:MF_01274}; OrderedLocusNames=PP_0438;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the type III pantothenate kinase family.
  protein_domains: ATPase_NBD. (IPR043129); Type_III_PanK. (IPR004619); Pan_kinase
    (PF03309)
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
  path: coaX-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: coaX-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QQ0
- **Protein Description:** RecName: Full=Type III pantothenate kinase {ECO:0000255|HAMAP-Rule:MF_01274}; EC=2.7.1.33 {ECO:0000255|HAMAP-Rule:MF_01274}; AltName: Full=PanK-III {ECO:0000255|HAMAP-Rule:MF_01274}; AltName: Full=Pantothenic acid kinase {ECO:0000255|HAMAP-Rule:MF_01274};
- **Gene Information:** Name=coaX {ECO:0000255|HAMAP-Rule:MF_01274}; OrderedLocusNames=PP_0438;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the type III pantothenate kinase family.
- **Key Domains:** ATPase_NBD. (IPR043129); Type_III_PanK. (IPR004619); Pan_kinase (PF03309)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "coaX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'coaX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **coaX** (gene ID: coaX, UniProt: Q88QQ0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *coaX* (Q88QQ0) — Type III Pantothenate Kinase, *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

The target is confirmed and **unambiguous**. A direct 2026 query of UniProtKB for pantothenate kinases (EC 2.7.1.33) in *Pseudomonas putida* KT2440 (taxid 160488) returns exactly **one** entry: **coaX / PP_0438 / Q88QQ0**, "Type III pantothenate kinase (PanK-III)." The gene symbol, EC number, organism, protein family (type III pantothenate kinase), and domain complement (ATPase_NBD IPR043129; Type_III_PanK IPR004619; Pfam PF03309 Pan_kinase) all match the literature for the CoaX/PanK-III family. No conflicting gene with the same symbol was encountered. All claims below apply to this specific protein.

---

## 1. Summary (Answer to the Research Question)

*coaX* (PP_0438, UniProt Q88QQ0) encodes a **type III pantothenate kinase (PanK-III/CoaX; EC 2.7.1.33)**, the enzyme that catalyzes the **first and committed step of coenzyme A (CoA) biosynthesis**: phosphorylation of the vitamin **(R)-pantothenate** using **ATP** to yield **(R)-4′-phosphopantothenate + ADP** (Rhea:16373). It is a soluble **cytoplasmic**, **homodimeric** enzyme that requires a **monovalent cation (K⁺ or NH₄⁺)** for activity and belongs to the **ASKHA (acetate/sugar kinase–Hsp70–actin) structural superfamily**. Unlike the *E. coli*-type PanK-I, PanK-III is **not feedback-inhibited by CoA**, has an **unusually high Km for ATP**, and **cannot use pantothenamide analogues** as substrates. Because *coaX* is the **sole pantothenate kinase gene** in *P. putida* KT2440, it is the non-redundant gatekeeper of the CoA pool and is expected to be **essential**.

---

## 2. Primary Function: Reaction and Substrate Specificity

**Reaction catalyzed (EC 2.7.1.33, Rhea:16373):**

> (R)-pantothenate + ATP → (R)-4′-phosphopantothenate + ADP + H⁺

This is **step 1 of the universal 5-step CoA biosynthetic pathway** ("CoA from (R)-pantothenate: step 1/5") and is the first committed, generally rate-controlling reaction of the pathway (UniProt Q88QQ0, HAMAP-Rule MF_01274; Yang et al. 2006, PMID 16855243; Yang et al. 2008, PMID 18186650).

**Substrate specificity.** The phosphoacceptor is the primary hydroxyl of **pantothenate (vitamin B5)**; the phosphate donor is **Mg-ATP**. Biophysical characterization of a Gram-negative PanK-III homolog (*Acinetobacter baumannii*) found **strong pantothenate affinity (Kd ≈ 1.2 × 10⁻⁸ M)** and only **moderate ATP affinity (Kd ≈ 3.7 × 10⁻³ M)** (Singla et al. 2021, PMID 32798368) — consistent with the family-wide signature of an **unusually high Km for ATP** (Yang et al. 2008, PMID 18186650).

**What PanK-III does NOT do.** PanK-III is **resistant to feedback inhibition by CoA and its thioesters**, and is **unable to phosphorylate N-alkylpantothenamide analogues** — so it does not convert those antimetabolites into toxic CoA analogues in vivo (Yang et al. 2008, PMID 18186650). These properties sharply distinguish it from the *E. coli* CoaA (type I) enzyme, in which CoA feedback inhibition is the principal regulatory valve of the pathway (Yang et al. 2006, PMID 16855243).

---

## 3. Cofactor and Catalytic Mechanism

- **Monovalent-cation dependence.** CoA/UniProt annotation specifies a required **monovalent cation, either NH₄⁺ or K⁺** (UniProt Q88QQ0, HAMAP-Rule MF_01274). This K⁺/NH₄⁺ activation is a defining biochemical hallmark of PanK-III that distinguishes it from PanK-I and PanK-II.
- **Fold and superfamily.** The first PanK-III crystal structure (*Thermotoga maritima*, 2.0 Å) established that type III PanKs adopt the **ASKHA (acetate and sugar kinase/Hsp70/actin) fold** and retain the superfamily's conserved active-site motifs (Yang et al. 2006, PMID 16855243). This is consistent with the ATPase nucleotide-binding-domain annotation (IPR043129) for Q88QQ0.
- **Catalytic residues.** Mutagenesis of **three highly conserved active-site aspartates** identified them as **critical for catalysis** and explained the enzyme's lack of CoA feedback inhibition (Yang et al. 2006, PMID 16855243). In Q88QQ0 the annotated catalytic active site is **residue Asp102**, with a P-loop/nucleotide-binding motif (residues 6–13) and additional substrate/metal-binding residues (93, 100–103, 122, 125, 181) (UniProt Q88QQ0).
- **Substrate-bound structures.** Binary complexes with **pantothenate** (substrate) and **phosphopantothenate** (product), and a **ternary complex with pantothenate + ADP**, together with isothermal titration calorimetry, defined the substrate-binding mode and thermodynamics of PanK-III catalysis (Yang et al. 2008, PMID 18186650).

---

## 4. Quaternary Structure and Subcellular Localization

- **Quaternary structure:** **homodimer** (UniProt Q88QQ0, HAMAP-Rule MF_01274). The mature protein is 249 aa.
- **Localization:** **cytoplasm** (GO:0005737; UniProt-SubCell). CoA biosynthesis is a soluble cytosolic process, and the enzyme acts on intracellular pantothenate and Mg-ATP. There are no signal peptides or membrane-spanning features; the enzyme carries out its function in the bacterial cytosol.

---

## 5. Pathway Context and Biological Process

CoaX initiates the conserved five-step conversion of pantothenate to CoA:

1. **Pantothenate → 4′-phosphopantothenate** (pantothenate kinase, **CoaX/PanK-III** — this enzyme)
2. 4′-phosphopantothenate + cysteine → 4′-phosphopantothenoylcysteine (PPC synthetase, CoaB)
3. → 4′-phosphopantetheine (PPC decarboxylase, CoaC)
4. → dephospho-CoA (phosphopantetheine adenylyltransferase, CoaD/PPAT)
5. → CoA (dephospho-CoA kinase, CoaE)

CoA and its 4′-phosphopantetheine moiety are indispensable cofactors for acyl-group transfer across central metabolism — fatty-acid synthesis/oxidation, the TCA cycle, and hundreds of acyl-CoA-dependent reactions — and CoA additionally serves as a **low-molecular-weight thiol in bacterial redox/antioxidant defence** (Gout 2019, PMID 30783014). By setting flux into this pathway, CoaX governs the supply of the cell's CoA pool. Notably, because PanK-III is CoA-insensitive, the **feedback regulation of the CoA pool in PanK-III organisms is exerted at downstream steps** (e.g., phosphopantetheine adenylyltransferase/PPAT, which is product-inhibited by CoA), rather than at the kinase step (Miller et al. 2007, PMID 17873050).

---

### Genomic context (P. putida KT2440)

KEGG assigns PP_0438 to **KO K03525** (type III pantothenate kinase) within pathway **ppu00770 "Pantothenate and CoA biosynthesis,"** at genome positions **531,036–531,785 (forward strand)**. The gene is **not part of a dedicated CoA-biosynthesis operon**; instead its start codon **overlaps (~10 bp) the stop of the immediately upstream same-strand gene *birA*** (PP_0437, bifunctional biotin-[acetyl-CoA-carboxylase] ligase/biotin operon repressor), and its 3′ end overlaps PP_0439 (conserved hypothetical). This tight overlap suggests **probable co-transcription/translational coupling with *birA***, functionally linking two cofactor-supply systems that both feed acyl/lipid metabolism (CoA for acyl-group chemistry; biotinylation of acetyl-CoA carboxylase for fatty-acid synthesis). Immediately downstream lie highly expressed housekeeping genes (EF-Tu/*tuf*, *secE*, *nusG*), consistent with constitutive expression of an essential biosynthetic enzyme. No second (type I) *coaA* gene is present anywhere in the genome. *(Bioinformatic inference from gene neighborhood; the operon has not been experimentally mapped.)*

## 6. Essentiality, Distribution, and Druggability

- **Distribution:** PanK-III is **widely distributed across bacteria** and is the **only PanK in many species, including *Pseudomonas aeruginosa*, *Helicobacter pylori*, and *Bordetella pertussis*** (Yang et al. 2006, PMID 16855243).
- **Sole PanK in *P. putida*:** the UniProt inventory confirms *coaX*/PP_0438 is the **only** pantothenate kinase gene in *P. putida* KT2440, making it non-redundant.
- **Essentiality is context-dependent.** In *Mycobacterium tuberculosis*, which encodes **both** a type I *coaA* and a type III *coaX*, *coaA* could only be deleted with an extra gene copy while ***coaX* was dispensable** (no growth defect in vitro, in macrophages, or in mice) — CoaA is the essential PanK there; by contrast, **CoaX is essential in *Bacillus anthracis***, where it is the sole PanK (Awasthy et al. 2010, PMID 20576686). Applying this logic, *coaX* is **expected to be essential in *P. putida*** because it is the organism's only PanK.
- **Drug target:** PanK-III is an attractive **selective antibacterial target** — it is essential (in sole-PanK organisms) and **structurally divergent from human PanK (≈28% identity)** (Singla et al. 2021, PMID 32798368). The broader CoA pathway is a well-validated antimicrobial target space (Butman et al. 2020, PMID 33384970).

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- H1: *coaX* encodes a functional type III pantothenate kinase catalyzing pantothenate + ATP → 4′-phosphopantothenate + ADP. **Supported** (UniProt catalytic activity; family structural/enzymatic studies PMID 16855243, 18186650).
- H2: The enzyme is CoA-insensitive with high Km for ATP and cannot use pantothenamides. **Supported** (PMID 18186650; homolog kinetics PMID 32798368).
- H3: It adopts an ASKHA fold with catalytic aspartates; functions as a K⁺/NH₄⁺-dependent cytoplasmic homodimer. **Supported** (PMID 16855243; UniProt Q88QQ0).
- H4: *coaX* is the sole PanK and therefore essential in *P. putida*. **Supported by inference** (UniProt gene inventory + sole-PanK essentiality argument, PMID 20576686); not yet directly tested genetically in *P. putida*.

**Refuted / Qualified:**
- The blanket claim "coaX is always essential" is **refuted** — it is dispensable where a type I CoaA is co-encoded (M. tuberculosis, PMID 20576686). Essentiality depends on being the sole PanK.

---

## 8. Limitations and Future Directions

- **No *P. putida*-specific enzymology or knockout** was found in the literature; the functional assignment rests on (i) UniProt/HAMAP curation of Q88QQ0, (ii) strong structural/biochemical studies of PanK-III orthologs (*T. maritima*, *A. baumannii*), and (iii) the essentiality logic. Direct biochemical characterization and a conditional knockout of PP_0438 in *P. putida* KT2440 would confirm essentiality and native kinetic parameters.
- The **K⁺/NH₄⁺ cofactor** requirement for the *P. putida* enzyme is annotation-based (HAMAP-Rule MF_01274); species-specific verification would be valuable.
- Future work: solve/validate the *P. putida* CoaX structure (or AlphaFold model) to confirm Asp102 and the dimer interface, and evaluate CoaX-selective inhibitors as anti-Pseudomonad leads.

---

### Key References
- Yang K, Eyobo Y, Brand LA, et al. *J Bacteriol* 2006; **PMID 16855243** — first PanK-III crystal structure; ASKHA fold; catalytic aspartates; CoA-insensitive; sole PanK in *Pseudomonas*, *H. pylori*, *B. pertussis*.
- Yang K, Strauss E, Huerta C, Zhang H. *Biochemistry* 2008; **PMID 18186650** — substrate/product/ternary complex structures; high Km for ATP; CoA-resistant; no pantothenamide use.
- Awasthy D, et al. *Microbiology* 2010; **PMID 20576686** — coaA vs coaX essentiality in *M. tuberculosis*; CoaX essential in *B. anthracis*.
- Singla M, et al. 2021; **PMID 32798368** — *A. baumannii* PanK-III biophysics; substrate affinities; drug-target rationale; ~28% identity to human PanK.
- Miller JR, et al. *Biochemistry* 2007; **PMID 17873050** — PPAT as the CoA-feedback-regulated step.
- Gout I. 2019; **PMID 30783014** — CoA as protective thiol in bacterial antioxidant defence.
- Butman HS, et al. 2020; **PMID 33384970** — CoA biosynthesis as antibacterial target space.
- UniProtKB **Q88QQ0** (HAMAP-Rule MF_01274) — reaction, cofactor, pathway, homodimer, cytoplasm, catalytic/binding residues.


## Artifacts

- [OpenScientist final report](coaX-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](coaX-deep-research-openscientist_artifacts/final_report.pdf)