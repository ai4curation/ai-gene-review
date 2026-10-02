---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:33:22.110238'
end_time: '2026-08-31T19:45:26.713851'
duration_seconds: 724.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fliD
  gene_symbol: fliD
  uniprot_accession: Q88ES7
  protein_description: 'RecName: Full=Flagellar hook-associated protein 2 {ECO:0000256|RuleBase:RU362066};
    Short=HAP2 {ECO:0000256|RuleBase:RU362066}; AltName: Full=Flagellar cap protein
    {ECO:0000256|RuleBase:RU362066};'
  gene_info: Name=fliD {ECO:0000313|EMBL:AAN69954.1}; OrderedLocusNames=PP_4376 {ECO:0000313|EMBL:AAN69954.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the FliD family. {ECO:0000256|ARBA:ARBA00009764,
  protein_domains: Flagellin_hook_IN_motif. (IPR010810); FliD. (IPR040026); FliD_C.
    (IPR010809); FliD_N. (IPR003481); Flagellin_IN (PF07196)
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
  path: fliD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fliD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ES7
- **Protein Description:** RecName: Full=Flagellar hook-associated protein 2 {ECO:0000256|RuleBase:RU362066}; Short=HAP2 {ECO:0000256|RuleBase:RU362066}; AltName: Full=Flagellar cap protein {ECO:0000256|RuleBase:RU362066};
- **Gene Information:** Name=fliD {ECO:0000313|EMBL:AAN69954.1}; OrderedLocusNames=PP_4376 {ECO:0000313|EMBL:AAN69954.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the FliD family. {ECO:0000256|ARBA:ARBA00009764,
- **Key Domains:** Flagellin_hook_IN_motif. (IPR010810); FliD. (IPR040026); FliD_C. (IPR010809); FliD_N. (IPR003481); Flagellin_IN (PF07196)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fliD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fliD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fliD** (gene ID: fliD, UniProt: Q88ES7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FliD — Flagellar Hook-Associated Protein 2 (HAP2 / Flagellar Cap Protein)

**Gene:** `fliD` (OrderedLocusName **PP_4376**)
**UniProt:** Q88ES7
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)
**Protein family:** FliD family (InterPro: FliD IPR040026; FliD_N IPR003481; FliD_C IPR010809; Flagellin_hook_IN_motif IPR010810; Pfam Flagellin_IN PF07196)

---

## 1. Identity Verification (MANDATORY CHECK)

- **Gene symbol vs. protein description:** ✅ Consistent. The gene symbol `fliD` is the universally used symbol for the **flagellar cap protein / hook-associated protein 2 (HAP2)**, matching the UniProt RecName exactly.
- **Organism:** ✅ *P. putida* KT2440 is a monotrichous (single polar flagellum) soil Gammaproteobacterium. FliD is a canonical component of its flagellar apparatus.
- **Family/domains:** ✅ The FliD_N / FliD_C domains and the Flagellin_IN (PF07196) motif are the diagnostic domains of the FliD family and are consistent with all characterized FliD orthologs.
- **Literature match:** ✅ FliD is a deeply studied protein family (Salmonella, *E. coli*, *Serratia*, *Bdellovibrio*, *Pseudomonas*). A *P. putida* KT2440–specific study of the flagellar cluster confirms `fliD` as a member of this organism's flagellar regulon.

**Conclusion:** The target is correctly identified. Direct primary-literature characterization of *P. putida* KT2440 FliD protein itself is limited, so the functional annotation below is built from (i) the extensively characterized FliD/HAP2 family mechanism (transferable because FliD's cap function is conserved and cross-species-compatible), and (ii) *P. putida*-specific genetic/regulatory studies of its flagellar system.

---

## 2. Summary (Answer to the Research Question)

FliD is the **flagellar cap protein (HAP2)**, a non-enzymatic **structural/assembly protein** that forms an oligomeric, star-shaped cap plugged onto the **distal (growing) tip of the extracellular flagellar filament**. Its primary function is to **prevent the exported, unfolded flagellin (FliC) monomers from diffusing away** and to **template/catalyze their ordered folding and polymerization** into the helical filament — flagellar filaments cannot grow without it. FliD itself is delivered to this site by unfolding and translocation through the **flagellar type III secretion system (fT3SS)**, chaperoned by **FliT** and handed off at the **FlhA** export gate. In *P. putida* KT2440, `fliD` (PP_4376) is one gene of the 59-gene flagellar cluster, expressed under the **FleQ / σ^N (RpoN) / FliA** hierarchical cascade that couples motility to the c-di-GMP–controlled planktonic↔biofilm switch.

---

## 3. Primary Function: What FliD Does

### 3.1 Filament cap that enables flagellin polymerization
The bacterial flagellum is built from the base outward: basal body → hook → hook-filament junction (HAP1/FlgK, HAP3/FlgL) → helical filament (flagellin, FliC) → **cap (HAP2/FliD)** at the distal end. Flagellin subunits are exported unfolded through the ~2 nm hollow central channel of the growing structure and must be added at the far tip, tens of micrometres from the cell. FliD is the machine that makes this possible.

Definitive genetic evidence: a *Salmonella* `fliD` (HAP2) deletion produces flagella consisting only of **hook–HAP1–HAP3** and **excretes flagellin monomers into the medium** — i.e., without the cap the exported flagellin simply leaks out and no filament forms. Adding **purified HAP2/FliD back** to this filament-less mutant **stops the leakage and restores filament growth** (~30 nm/min ≈ one flagellin subunit per second), and this occurs **without HAP2 turnover**, showing FliD remains at the tip while catalyzing polymerization (Ikeda, Yamaguchi & Hotani, 1993, PMID 8407873). The cap thus "plays an essential role in filament growth in vivo by preventing flagellin monomers from leaking out without polymerization" (Maki et al., 1998, PMID 9545371).

**This is an assembly/foldase-like activity, not a classical enzymatic reaction — FliD has no catalyzed metabolic substrate. Its functional "substrate" is the flagellin (FliC) subunit, which it captures and inserts into the filament lattice.**

### 3.2 Structure and mechanism (inference from crystallography)
FliD is composed of three domains — **D1, D2, D3** — and self-oligomerizes into a species-specific "star plate":
- ***E. coli*** FliD forms a **hexamer** (six-pointed star; D2/D3 form the plate, D1 forms the "legs").
- ***Salmonella*** Typhimurium forms a **pentamer** (five-pointed star) (Song et al., 2017, PMID 28179186).
- ***Serratia marcescens*** and ***Bdellovibrio bacteriovorus*** form **tetramers** (Cho et al., 2017 PMID 28527888; Cho et al., 2019 PMID 31542231).

In vitro, *Salmonella* HAP2 forms a **bipolar decamer** (a pair of pentamers) whose assembly is strongly pH- and salt-dependent (Imada et al., 1998, PMID 9545379). Electron microscopy shows the cap is a pentamer with a thin plate exposed to solvent and the other half **plugged into the ~2×-wider hole at the distal filament end** (Maki et al., 1998, PMID 9545371).

The crystallographic data support a **"catalyzed elongation / positional-replacement" mechanism**: FliD's interdomain and intersubunit flexibility lets it "occupy a position in place of a nascent flagellin until the flagellin reaches the growing end of the filament, and then FliD moves aside to repeat the positional replacement" (Song et al., 2017, PMID 28179186). In effect FliD acts as a rotating, flexible placeholder that guides each arriving flagellin into its correct helical site while never letting the tip open to the outside.

The number of "legs" ideally matches the ~5-start helical symmetry of the filament; the oligomeric state is species-specific. For **PSEPK specifically, UniProt curation annotates Q88ES7 as a "Homopentamer"** (SUBUNIT), consistent with the pentameric caps of other polar/peritrichous Gammaproteobacteria such as *Salmonella*.

### 3.2a Organism-specific bioinformatic confirmation (Q88ES7)
Direct annotation of the PSEPK protein corroborates the family model:
- **452 residues, ~46.5 kDa.** Domain architecture: **FliD_N domain (res 11–107; Pfam PF02465)** and **FliD_C domain (res 211–433; Pfam PF07195)** separated by a **disordered polar linker (183–209)**, plus a **C-terminal coiled coil (389–416)**. The N-/C-terminal regions and coiled coil correspond to the α-helical D0/D1 "leg" that plugs into the filament lumen, while the central region forms the solvent-exposed D2/D3 plate.
- **Curated FUNCTION (UniProt):** *"Required for morphogenesis and for the elongation of the flagellar filament by facilitating polymerization of the flagellin monomers at the tip of growing filament. Forms a capping structure, which prevents flagellin subunits ... from leaking out without polymerization at the distal end."* — i.e., exactly the mechanism established experimentally in the family.
- **Curated SUBCELLULAR LOCATION:** *Secreted; Bacterial flagellum* (keywords: Bacterial flagellum, Cell projection, Secreted, Coiled coil).

### 3.2b Genomic context in P. putida KT2440
`fliD` (PP_4376) sits within a compact, functionally coherent gene module (confirmed by KEGG Orthology assignments):

| Locus | Gene | KO | Product |
|---|---|---|---|
| PP_4373 | **fleQ** | K10941 | σ^54-dependent flagellar **master regulator** |
| PP_4374 | **fliT** | K02423 | **FliD-specific** T3S secretion chaperone |
| PP_4375 | **fliS** | K02422 | flagellin (FliC)-specific secretion chaperone |
| **PP_4376** | **fliD** | **K02407** | **flagellar hook-associated protein 2 (cap)** — *this gene* |
| PP_4377 | flaG | — | putative flagellin FlaG |
| PP_4378 | flaA/fliC | K02406 | flagellin (filament structural protein) |

This module co-locates the flagellar master regulator (**FleQ**), **both** late-substrate T3S chaperones (**FliT** for the cap, **FliS** for flagellin), and the cap plus flagellin structural genes — a genetic basis for coordinated, stoichiometric export and assembly of the filament tip. Crucially, KO **K02407** independently confirms PP_4376/Q88ES7 as **HAP2/FliD**, and the presence of **fliT (PP_4374, K02423)** confirms — at the organism-specific level — that PSEPK possesses the dedicated FliD export chaperone described mechanistically in enteric bacteria (Section 4). PP_4376 is a member of the KEGG flagellar-assembly pathway (map ppu02040).

### 3.3 Conserved, family-defining but interchangeable role
Cross-species reconstitution shows a clean division of labour: flagellin **FliC determines the flagellar "family" and cannot be exchanged across families**, but **FliD "serves as the cap protein even in different families"** — *E. coli* and *P. aeruginosa* FliD both allow *Salmonella* FliC to polymerize. The authors conclude "FliC is essential for determining families, but FliD plays a subsidiary role in filament formation" (Inaba et al., 2013, PMID 23097231). This mechanistic interchangeability is why FliD family knowledge transfers reliably to the poorly-studied *P. putida* ortholog.

---

## 4. Localization: Where FliD Acts

- **Site of function:** the **distal tip of the flagellar filament**, i.e., **extracellular / cell-surface exposed**, at the very end of the growing organelle. The solvent-exposed plate faces outward; the D1 legs plug into the filament lumen (PMID 9545371).
- **Delivery route to that site:** FliD is synthesized in the cytoplasm, kept export-competent/partially unfolded, and **secreted through the flagellar type III secretion system** — the same hollow axial channel used by all axial flagellar proteins ("exported through the 25–30 Å flagellum central channel as partially unfolded monomers"; Fraser et al., 1999, PMID 10320579).
- **Chaperone / export gate:** Its **cognate T3S chaperone is FliT** — and PSEPK encodes a dedicated **fliT (PP_4374, KO K02423)** immediately upstream of *fliD* (Section 5.2), confirming this chaperone is present in *P. putida*. FliD "bind[s] to the FlhA cytoplasmic domain (FlhA-C) only in complex with [its] cognate chaperone" FliT; FliJ modulates FlhA-C to favour FliD/FliT loading, and after FliD is exported the empty FliT remains associated — providing a switch from stoichiometric FliD export to bulk flagellin export (Bange et al., 2010, PMID 20534509). FlgN/FliT are the substrate-specific chaperones for the hook-associated proteins (PMID 10320579).

So FliD is a **secreted, extracytoplasmic structural protein** whose mature functional location is the tip of the surface-exposed flagellum.

---

## 5. Pathway Context

### 5.1 In the flagellar assembly / motility pathway
FliD is a late (Class III–type) flagellar building block. Functionally it sits **downstream of the hook and the hook–filament junction (HAP1/FlgK, HAP3/FlgL) and is required before/for bulk flagellin (FliC) polymerization**. Without FliD there is no filament, hence **no functional flagellum and no swimming motility**. The biological process is therefore **flagellum-dependent cell motility and chemotaxis** (directed swimming toward nutrients/away from repellents), which for *P. putida* underlies environmental dispersal and the early stages of surface/root colonization.

### 5.2 *P. putida* KT2440–specific regulation
`fliD` (PP_4376) is embedded in a **single 59-gene flagellar cluster** organized into **11 operons / 22 promoters**. Its expression is governed by a **three-tier transcriptional cascade** in which **FleQ is the Class I master regulator** at the top, acting with the alternative sigma factors **σ^N (RpoN)** and **FliA (σ^28)** (Leal-Morales et al., 2022, PMID 34859548). This flagellar regulon is tightly integrated with the **planktonic-to-biofilm ("swim–attach") decision**: FleQ, the second messenger **c-di-GMP**, and the antagonist **FleN** co-regulate motility genes together with the large adhesin **LapA** and cellulose synthesis; high c-di-GMP suppresses motility and favours biofilm/adhesion (Jiménez-Fernández et al., 2016 PMID 27636892; Navarrete et al., 2019 PMID 30889223; Hueso-Gil et al., 2020 PMID 32519402). FliD's abundance is thus co-timed with the rest of the flagellar apparatus during the motile lifestyle.

### 5.3 Secondary / moonlighting roles
Because FliD is surface-exposed, in several bacteria it has documented accessory functions:
- **Adhesin / host colonization & immunogenicity:** in *Clostridioides difficile* the flagellar cap protein FliD is a surface adhesin that elicits host antibody responses (Péchiné et al., 2005, PMID 15673516).
- **Biofilm relevance:** in *P. aeruginosa*, FliD is implicated (by molecular docking with an antibacterial agent) as a target relevant to biofilm inhibition (He et al., 2022, PMID 35165818).

These are consistent with, but secondary to, FliD's primary assembly role. For *P. putida* specifically, an adhesin role has not been directly demonstrated and should be regarded as plausible-but-untested; note that in *P. putida* the dominant adhesin driving biofilm is LapA, and flagellar-structural mutations cause only modest biofilm defects (López-Sánchez et al., 2016, PMID 27190143).

---

## 6. Evidence Table

| Claim | Evidence type | Key reference(s) |
|---|---|---|
| FliD caps distal filament tip; prevents flagellin leakage; enables filament growth | Genetic + in-vitro reconstitution (Salmonella) | PMID 8407873, 9545371 |
| Cap is oligomeric star-plate; bipolar decamer/pentamer in vitro | Biochemistry + EM | PMID 9545379, 9545371 |
| Three-domain (D1/D2/D3) architecture; penta/hexa/tetrameric, species-specific; catalyzed-elongation model | X-ray crystallography | PMID 28179186, 28527888, 31542231 |
| FliD cap function is cross-species interchangeable ("subsidiary role") | Chimeric filament assembly | PMID 23097231 |
| Exported via flagellar T3SS; chaperone FliT; FlhA/FliJ export gate | Biochemistry + crystallography | PMID 20534509, 10320579 |
| *P. putida* fliD in 59-gene flagellar cluster; FleQ/σ^N/FliA cascade | Bioinformatics + in-vivo expression (KT2440) | PMID 34859548 |
| Flagellar regulon coupled to c-di-GMP / biofilm switch in *P. putida* | Genetics | PMID 27636892, 30889223, 32519402 |
| FliD can act as surface adhesin/immunogen (other species) | Serology / docking | PMID 15673516, 35165818 |
| **PSEPK-specific:** Q88ES7 = 452 aa, ~46.5 kDa, homopentamer, Secreted/flagellum; FliD_N (11–107) + FliD_C (211–433) + C-terminal coiled coil (389–416) | UniProt curation / domain annotation | UniProt Q88ES7 |
| **PSEPK-specific:** fliD (PP_4376, KO K02407=HAP2) lies in a FleQ(PP_4373)–fliT(PP_4374)–fliS(PP_4375)–fliD–flaG(PP_4377)–fliC(PP_4378) module; PSEPK encodes the FliD chaperone FliT | Genome/KO annotation (KEGG) | KEGG ppu:PP_4373–4378 |

---

## 7. Supported and Refuted Hypotheses

**Supported**
- H1: *P. putida* FliD is the flagellar cap protein that enables flagellin polymerization at the filament tip. **(Supported by conserved family mechanism + KT2440 cluster membership.)**
- H2: FliD is a secreted, extracellular structural protein acting at the flagellum distal tip, delivered by the fT3SS with chaperone FliT. **(Supported.)**
- H3: FliD function is non-enzymatic (assembly/foldase-like), with flagellin (FliC) as its functional partner "substrate." **(Supported.)**
- H4: In *P. putida*, fliD expression is under FleQ-headed, σ^N/FliA-dependent flagellar control tied to c-di-GMP signaling. **(Supported.)**

**Refuted / rejected**
- FliD is an enzyme with a small-molecule substrate or a transporter. **(Refuted — it is a structural cap; no catalytic/transport activity.)**
- FliD determines flagellar filament "family"/helical type. **(Refuted — that is FliC's role; FliD is interchangeable across families, PMID 23097231.)**

**Uncertain / organism-specific gaps**
- The oligomeric number of *P. putida* KT2440 FliD is **curated as a homopentamer** in UniProt (Q88ES7), but this has not been verified by an experimental PSEPK structure.
- A direct adhesin/biofilm role for *P. putida* FliD is plausible but unproven; LapA is the dominant *P. putida* adhesin.

---

## 8. Limitations and Future Directions
- No FliD structure or biochemical study exists specifically for *P. putida* KT2440; conclusions rely on family-level conservation (well justified by the demonstrated cross-species cap interchangeability).
- **Future work:** determine the oligomeric state of PSEPK FliD (crystallography/cryo-EM or AlphaFold-multimer); construct a KT2440 `fliD` knockout to confirm the non-motile, flagellin-leaking phenotype; test whether purified PSEPK FliD binds mucins/plant-root surfaces (potential adhesin role relevant to rhizosphere colonization); map its FliT chaperone interaction.

---

*Report generated from primary literature (PubMed) and UniProt/InterPro annotation. Primary characterization is drawn from FliD/HAP2 family studies with organism-specific regulatory context from P. putida KT2440.*


## Artifacts

- [OpenScientist final report](fliD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fliD-deep-research-openscientist_artifacts/final_report.pdf)