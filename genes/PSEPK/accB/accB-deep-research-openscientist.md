---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T15:37:58.052471'
end_time: '2026-07-23T16:00:14.801052'
duration_seconds: 1336.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: accB
  gene_symbol: accB
  uniprot_accession: Q88QD5
  protein_description: 'RecName: Full=Biotin carboxyl carrier protein of acetyl-CoA
    carboxylase {ECO:0000256|ARBA:ARBA00017562, ECO:0000256|RuleBase:RU364072};'
  gene_info: Name=accB {ECO:0000313|EMBL:AAN66186.1}; OrderedLocusNames=PP_0559 {ECO:0000313|EMBL:AAN66186.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AcCoA_biotinCC. (IPR001249); Biotin_BS. (IPR001882); Biotin_Carboxyl_Carrier/Decarb.
    (IPR050709); Biotin_lipoyl. (IPR000089); Single_hybrid_motif. (IPR011053)
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
  path: accB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: accB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QD5
- **Protein Description:** RecName: Full=Biotin carboxyl carrier protein of acetyl-CoA carboxylase {ECO:0000256|ARBA:ARBA00017562, ECO:0000256|RuleBase:RU364072};
- **Gene Information:** Name=accB {ECO:0000313|EMBL:AAN66186.1}; OrderedLocusNames=PP_0559 {ECO:0000313|EMBL:AAN66186.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AcCoA_biotinCC. (IPR001249); Biotin_BS. (IPR001882); Biotin_Carboxyl_Carrier/Decarb. (IPR050709); Biotin_lipoyl. (IPR000089); Single_hybrid_motif. (IPR011053)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "accB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'accB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **accB** (gene ID: accB, UniProt: Q88QD5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **accB** (Q88QD5) — Biotin Carboxyl Carrier Protein of Acetyl-CoA Carboxylase in *Pseudomonas putida* KT2440

**Gene:** accB · **Ordered locus:** PP_0559 · **UniProt:** Q88QD5
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK
**Protein length:** 153 aa · **EC context:** subunit of acetyl-CoA carboxylase (EC 6.4.1.2 / 6.3.4.14)

---

## 1. Summary (Answer to the Research Question)

**accB encodes the biotin carboxyl carrier protein (BCCP), a non-catalytic but essential subunit of the multi-subunit bacterial acetyl-CoA carboxylase (ACC) complex.** ACC catalyzes the first committed and rate-limiting step of fatty acid biosynthesis — the ATP- and bicarbonate-dependent carboxylation of acetyl-CoA to malonyl-CoA. BCCP's specific molecular role is to serve as a **covalently biotinylated "swinging arm" carrier** that ferries an activated carboxyl (CO₂) group between the two spatially separated catalytic subunits of ACC: biotin carboxylase (AccC) and carboxyltransferase (AccA/AccD). The protein functions in the **cytoplasm** as part of the soluble ACC complex, is post-translationally biotinylated on a single conserved lysine by biotin protein ligase (BirA), and is encoded within an **accBC operon** whose transcription AccB itself autoregulates.

### Gene-identity verification (mandatory)
- The gene symbol **accB** consistently denotes the **BCCP subunit** across bacteria (*E. coli*, *Pseudomonas aeruginosa*, *Bacillus subtilis*, *Lactobacillus plantarum*) — this matches the UniProt protein description exactly [PMID 14594796; 7693652; 7592499; 11133475].
- Organism confirmed: KEGG entry **ppu:PP_0559** maps to *P. putida* KT2440; orthology group **eggNOG COG0511 (BCCP)**.
- Domain/family signatures align: **Pfam PF00364 (Biotin_lipoyl)**, **InterPro IPR000089 (Biotin/lipoyl attachment), IPR001882 (Biotin binding site), IPR011053 (single hybrid motif), IPR001249 (AcCoA_biotinCC)** — all diagnostic of BCCP.
- **No ambiguity.** (Note: the *plant* gene "accB" refers to the homologous BCCP subunit of the plastid heteromeric ACCase — same function, different organism. This report concerns the bacterial cytoplasmic enzyme.)

---

## 2. Molecular Function: What reaction, what role

### 2.1 The enzyme complex and the reaction
Bacterial ACC is a **multi-subunit enzyme** composed of four polypeptides encoded by *accA*, *accB*, *accC*, and *accD* [PMID 14594796]. It catalyzes:

> Acetyl-CoA + HCO₃⁻ + ATP → Malonyl-CoA + ADP + Pᵢ

This is "the first step of fatty acid biosynthesis, the synthesis of malonyl-CoA from acetyl-CoA using ATP and bicarbonate" [PMID 14594796], and is the first *committed* / rate-limiting step of the pathway [PMID 7678242]. The functional subunits are:
- **AccC** — biotin carboxylase (BC)
- **AccB** — biotin carboxyl carrier protein (**BCCP**) ← *this gene*
- **AccA + AccD** — the α and β subunits of carboxyltransferase (CT)

### 2.2 Precise role of BCCP — a mobile CO₂ carrier
BCCP is **not itself catalytic**; it is the **prosthetic-group carrier** that couples the two half-reactions occurring at physically distinct active sites:

1. **Half-reaction 1 (biotin carboxylation):** Holo-BCCP presents its biotin to the **biotin carboxylase (AccC)** active site, "which leads to the addition of the carboxylate group of bicarbonate to biotin" (ATP-dependent), forming **carboxy-biotin–BCCP** [PMID 10048324].
2. **Half-reaction 2 (carboxyl transfer):** The "carboxy-biotinylated form of BCCP interacts with transcarboxylase [carboxyltransferase] in the transfer of the carboxylate to acetyl-CoA to form malonyl-CoA" [PMID 10048324].

Between these steps, the biotinylated domain physically **swings** between the BC and CT active sites, mediated by a flexible linker (see §3). BCCP therefore acts as a **swinging-arm carrier of activated CO₂** — the defining mechanistic feature of all biotin-dependent carboxylases.

Substrate specificity of the overall enzyme is for **acetyl-CoA** (yielding malonyl-CoA); BCCP's own "substrate" is the **biotin cofactor / CO₂ group** it carries. (In some organisms the related carrier can also service propionyl-CoA carboxylation, but the canonical bacterial ACC/BCCP is dedicated to malonyl-CoA formation for fatty acid synthesis [PMID 14997352].)

---

## 3. Structure and Sequence Features (Q88QD5, evidence from sequence + homology)

Direct analysis of the Q88QD5 sequence (153 aa) reveals the canonical two-part BCCP architecture:

| Feature | Location (Q88QD5) | Evidence |
|---|---|---|
| **N-terminal region** | ~1–46 | Interaction/structural region; N-terminal segment mediates operon autoregulation in orthologs |
| **Ala/Pro-rich flexible linker ("hinge")** | ~48–73 (`…PAPMAAAPAAAPVAAAAPAAEATAAAPAL…`) | Low-complexity Ala/Pro linker that allows the biotinyl domain to swing between active sites |
| **C-terminal biotinyl/lipoyl domain** | **77–153** | UniProt Domain "Lipoyl-binding"; Pfam PF00364; a β-barrel single-hybrid-motif fold |
| **Conserved biotinylation motif (A)MKM** | **M118–K119–M120** | The strictly conserved Met-**Lys**-Met motif; **K119 is the biotinyl-lysine** (biocytin attachment site) |

The C-terminal domain adopts the well-characterized **biotinyl-domain fold** — a flattened β-barrel whose biotin-bearing lysine sits on a tight β-turn ("protruding thumb"/hairpin) at the tip of the domain, structurally homologous to the lipoyl domains of 2-oxoacid dehydrogenases (hence the shared IPR000089/IPR011053 and PF00364 signatures). NMR and crystallographic studies of the *E. coli* BCCP C-terminal domain show that biotinylation causes small, localized conformational changes in the biotin-binding region that help discriminate its three successive protein partners (BirA → BC → CT) [PMID 10048324]. This structural inference transfers to Q88QD5 given the high conservation of the biotinyl domain and the exact AMKM motif.

---

## 4. Post-translational Modification: Biotinylation

BCCP is synthesized as inactive **apo-protein** and activated by covalent attachment of biotin:

- **"Biotin protein ligase (BPL) catalyses the biotinylation of the biotin carboxyl carrier protein (BCCP) subunit of acetyl CoA carboxylase and this post-translational modification of a single lysine residue is exceptionally specific"** [PMID 12631286].
- Biotin is amide-linked to the ε-amino group of the target lysine (**K119** in *P. putida* BCCP), producing the biotinyl-lysine (biocytin) prosthetic swinging arm.
- The apo-form is the specific substrate of the biotin holoenzyme synthetase **BirA**; the resulting **holo-BCCP** then engages biotin carboxylase [PMID 10048324]. Addition of the biotin group itself modulates downstream partner recognition [PMID 12631286].

Because biotinylation is obligatory for ACC activity, the ligase step (BirA/BPL) is a validated **antibacterial drug target** [PMID 32268615; 28942842].

---

## 5. Subcellular Localization

BCCP functions in the **cytoplasm** as a component of the soluble, dissociable multi-subunit ACC complex (GO:0009317 "acetyl-CoA carboxylase complex"). Unlike the plant plastid heteromeric ACCase, the *P. putida* enzyme is not membrane-bound or organellar; its product malonyl-CoA is delivered to the cytoplasmic type-II fatty acid synthase (FAS-II) machinery. Notably, *Pseudomonas* species contain **more than one biotinylated protein** (at least three reported in *P. aeruginosa*), so BCCP is one of several biotin-dependent carriers in the cell but the one dedicated to ACC/fatty-acid synthesis [PMID 7693652].

---

## 6. Pathway Context and Regulation

### 6.1 Pathway
BCCP acts at the entry point of the **fatty acid biosynthesis pathway**: ACC-produced **malonyl-CoA** is the two-carbon donor for every elongation cycle of FAS-II, supplying membrane phospholipid acyl chains and, in *P. putida*, precursors for storage/valuable polyketides and other malonyl-CoA-derived products. GO annotation: **GO:0006633 fatty acid biosynthetic process**; **GO:0003989 acetyl-CoA carboxylase activity** (KEGG module for fatty acid biosynthesis initiation).

### 6.2 Operon organization
In *Pseudomonas*, **accB is co-transcribed with accC** in a two-gene **accBC operon**: "the *P. aeruginosa* accB (fabE) homolog, which encodes BCCP, is part of a 2-gene operon that includes accC (fabG), the structural gene for the biotin carboxylase subunit of ACC" [PMID 7693652]. The carboxyltransferase genes accA/accD lie elsewhere on the chromosome, as in *E. coli*.

### 6.3 Regulation
- **Autoregulation:** AccB is a transcriptional repressor of its own operon — "AccB functions to negatively regulate transcription of the accBC operon," and the N-terminal ~68 residues are sufficient for this repression [PMID 14594796]. This feedback balances BCCP:BC stoichiometry and couples ACC levels to demand.
- **Growth-rate control:** acc transcription correlates directly with cellular growth rate, matching malonyl-CoA/lipid supply to biosynthetic need [PMID 7678242].

### 6.4 Biotechnological relevance in *P. putida*
ACC is the malonyl-CoA-supplying bottleneck for engineering *P. putida* as a chassis: computer-assisted "optimization of the acetyl-CoA carboxylase complex through ribosome binding site engineering" contributed to a **5.8-fold** increase in polyketide (phloroglucinol) titer [PMID 40107409], underscoring that AccB/ACC dosage directly limits flux into malonyl-CoA-derived products.

---

## 7. Evidence Assessment

| Claim | Evidence type | Strength |
|---|---|---|
| accB = BCCP subunit of ACC | Sequence/orthology (COG0511, Pfam, InterPro) + cross-species genetics | Very strong |
| ACC makes malonyl-CoA (first FAS step) | Biochemistry, genetics (multiple bacteria) | Very strong |
| BCCP = swinging biotin carrier between BC and CT | Biochemistry + NMR/crystal structure (*E. coli*) | Strong (direct in ortholog; inferred for Q88QD5 by conservation) |
| Biotinylation on single Lys (K119) by BirA/BPL | Enzymology + sequence motif AMKM | Strong |
| accBC operon organization in *Pseudomonas* | Cloning/RNA blots (*P. aeruginosa*) | Strong (direct in *Pseudomonas*) |
| AccB autoregulates accBC | Genetics (*E. coli*) | Strong (ortholog) |
| Cytoplasmic localization / ACC complex | GO/subcellular annotation, enzyme biochemistry | Strong |

Most mechanistic and structural evidence derives from the highly conserved *E. coli* and *Pseudomonas aeruginosa* orthologs; direct experimental characterization of the *P. putida* KT2440 protein specifically is limited, but the sequence identity, exact conservation of the AMKM biotinylation motif (K119), and identical domain architecture make transfer of these conclusions robust.

---

## 8. Supported vs. Refuted Hypotheses

**Supported**
- H1: accB encodes BCCP, a subunit (not the catalytic core) of ACC. ✅
- H2: Its role is to carry biotin/CO₂ between the BC and CT active sites via a flexible linker. ✅
- H3: It is biotinylated on a single conserved lysine (K119) by BirA. ✅
- H4: It functions in the cytoplasm in fatty acid biosynthesis, supplying malonyl-CoA. ✅
- H5: accB is co-operonic with accC and autoregulates transcription. ✅

**Refuted / excluded**
- accB is *not* a catalytic carboxylase, transporter, or signaling molecule — it is a carrier/adapter subunit.
- It is *not* membrane-bound or organellar (contrast with plant plastid ACCase).

## 9. Limitations and Future Directions
- No *P. putida* KT2440-specific structure or in-vitro kinetics; conclusions rely on orthologs.
- The precise in-vivo biotinylation stoichiometry and identity of all *P. putida* biotinylated proteins are not directly characterized here.
- Future work: solve/predict the KT2440 BCCP–BC interaction, confirm K119 biotinylation by MS, and quantify AccB autoregulation in *P. putida*.

---

### Key References
- James & Cronan 2004, *J Biol Chem* — ACC subunits; AccB autoregulation of accBC (PMID 14594796)
- Yao, Soden, Summers & Beckett 1999, *Biochemistry* — BCCP functional cycle & biotinyl-domain structure/dynamics (PMID 10048324)
- Clarke et al. 2003 — BPL biotinylation of a single specific BCCP lysine (PMID 12631286)
- Best & Knauf 1993, *J Bacteriol* — *Pseudomonas* accBC operon; multiple biotinylated proteins (PMID 7693652)
- Li & Cronan 1993, *J Bacteriol* — growth-rate regulation of acc genes (PMID 7678242)
- Gu et al. 2011 — accB = BCCP assignment (PMID 21421413)
- Batianis et al. 2025 — ACC/malonyl-CoA engineering in *P. putida* (PMID 40107409)


## Artifacts

- [OpenScientist final report](accB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](accB-deep-research-openscientist_artifacts/final_report.pdf)