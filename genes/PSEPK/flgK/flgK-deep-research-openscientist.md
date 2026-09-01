---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T01:28:07.570248'
end_time: '2026-08-11T01:44:33.986662'
duration_seconds: 986.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: flgK
  gene_symbol: flgK
  uniprot_accession: Q88ES2
  protein_description: 'RecName: Full=Flagellar hook-associated protein 1 {ECO:0000256|ARBA:ARBA00016244};'
  gene_info: Name=flgK {ECO:0000313|EMBL:AAN69959.1}; OrderedLocusNames=PP_4381 {ECO:0000313|EMBL:AAN69959.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the flagella basal body rod proteins family.
  protein_domains: Flag_bb_rod_N. (IPR001444); Flagellar_basal_body_rod_CS. (IPR019776);
    Flg_bb/hook_C_dom. (IPR010930); FlgK. (IPR002371); FlgK_D2-like. (IPR049119)
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: flgK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: flgK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ES2
- **Protein Description:** RecName: Full=Flagellar hook-associated protein 1 {ECO:0000256|ARBA:ARBA00016244};
- **Gene Information:** Name=flgK {ECO:0000313|EMBL:AAN69959.1}; OrderedLocusNames=PP_4381 {ECO:0000313|EMBL:AAN69959.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the flagella basal body rod proteins family.
- **Key Domains:** Flag_bb_rod_N. (IPR001444); Flagellar_basal_body_rod_CS. (IPR019776); Flg_bb/hook_C_dom. (IPR010930); FlgK. (IPR002371); FlgK_D2-like. (IPR049119)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "flgK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'flgK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **flgK** (gene ID: flgK, UniProt: Q88ES2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **flgK** (Q88ES2, PP_4381) in *Pseudomonas putida* KT2440

## Summary

**flgK** (UniProt **Q88ES2**; ordered locus **PP_4381**) of *Pseudomonas putida* strain KT2440 encodes **Flagellar Hook-Associated Protein 1 (HAP1)**, a **non-enzymatic structural adapter protein** of the bacterial flagellum. FlgK is not an enzyme, transporter, or diffusible signaling molecule — it is a self-assembling axial building block. Its primary function is to form the **proximal half of the hook–filament junction**: the short, specialized zone that mechanically connects the flexible, curved flagellar **hook** (built from FlgE) to the long, rigid, helical **filament** (built from flagellin/FliC). Working in an obligate partnership with **FlgL (HAP3, PP_4380, Q88ES3)**, FlgK bridges the mismatch in curvature and mechanical stiffness between hook and filament, and provides the assembly platform onto which the FliD (HAP2) filament cap and the flagellin subunits are subsequently added. Without FlgK, cells complete the hook but fail to build a filament and are therefore non-motile.

FlgK carries out its function **extracytoplasmically, at the distal growing tip of the nascent flagellum**, outside the cell body. It reaches that location by a dedicated route: it is exported in an **unfolded state through the ~2 nm central channel of the flagellum by the flagellar type III secretion system (fT3SS)**, escorted by the cytoplasmic export chaperone **FlgN**, and it polymerizes at the tip only after the hook has reached its mature length. Its export and assembly are temporally gated — FlgK, FlgL, FliD, and FliC are secreted efficiently only after hook completion, reflecting the substrate-specificity switch of the export apparatus. Structurally, FlgK belongs to the flagellar axial-protein superfamily: it shares the flagellin-like architecture of a large elongated α-helical bundle core (the D0/D1 coiled-coil domains that form the tube wall) decorated with smaller, species-variable outer β-domains (D2-like lobes).

In *P. putida* KT2440 specifically, *flgK* sits within a single **59-gene flagellar cluster** organized into 11 operons and governed by a **three-tier transcriptional cascade topped by the master regulator FleQ**, feeding through σ⁵⁴ (RpoN) and the flagellar sigma factor σ²⁸ (FliA). As a hook–filament junction gene, *flgK* is expressed in the **late (class 3, σ²⁸/FliA-dependent)** tier, co-regulated with the filament and cap genes. In the KT2440 genome it lies immediately adjacent to its junction partner *flgL* (PP_4380) and downstream of the rod-associated muramidase *flgJ* (PP_4382), placing it squarely in the basal-body/hook-filament assembly gene set. The flagellum that FlgK completes drives *P. putida*'s **swimming motility, surface adhesion, and biofilm/rhizosphere colonization**, and the whole system is integrated with c-di-GMP signaling that toggles the bacterium between motile and sessile (adhesive/biofilm) lifestyles.

---

## Gene / Protein Identity Verification

| Field | Value |
|---|---|
| UniProt accession | Q88ES2 |
| Ordered locus | PP_4381 |
| Gene symbol | *flgK* |
| Protein name | Flagellar hook-associated protein 1 (HAP1) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Length / mass | 680 aa / ~69.6 kDa |
| Family | Flagella basal-body rod protein family (FlgK / HAP1) |
| Domains | IPR001444 (Flag_bb_rod_N); IPR019776 (Flagellar_basal_body_rod_CS); IPR010930 (Flg_bb/hook_C_dom); IPR002371 (FlgK); IPR049119 (FlgK_D2-like) |

All mandatory verification checkpoints are satisfied: (1) the symbol *flgK* matches the UniProt description "Flagellar hook-associated protein 1"; (2) the organism is confirmed as *P. putida* KT2440 via locus PP_4381 and its native gene neighborhood (Finding F009); (3) the domain set aligns exactly with the FlgK family and the experimentally solved FlgK fold; and (4) no competing gene with the same symbol confounded the search. **The identification is high-confidence.**

---

## Key Findings

### F001 — FlgK is Hook-Associated Protein 1 (HAP1), the first hook–filament junction protein

The identity of *flgK* as the gene encoding **HAP1** is established through classical genetics and structural studies in the enteric model *Salmonella*. Three hook-associated proteins cap and extend the flagellar structure: **HAP1 = FlgK**, **HAP3 = FlgL**, and **HAP2 = FliD**. All three are essential for building a functional filament. In a *flgK* (HAP1) mutant, cells cannot assemble a filament; moreover, when hook protein (FlgE) is overproduced in a *flgK* background, cells produce **abnormally long hooks** — direct evidence that FlgK normally caps and terminates the hook, defining where the hook ends and the junction begins ([PMID: 10482524](https://pubmed.ncbi.nlm.nih.gov/10482524/)). FlgK also belongs to the set of hook-associated proteins whose presence is genetically coupled to flagellin gene expression, underscoring its position as a checkpoint late in assembly ([PMID: 1848842](https://pubmed.ncbi.nlm.nih.gov/1848842/)). Because Q88ES2 (PP_4381) carries the diagnostic **FlgK family signature (IPR002371)** and the full flagellar rod/hook domain architecture, this role transfers directly to the *P. putida* KT2440 protein.

> *"In a flgK (HAP1, first hook-filament junction protein) mutant or a flgL (HAP3, second hook-filament junction protein) mutant, the overproduction of FlgE also resulted in longer than normal hooks."* ([PMID: 10482524](https://pubmed.ncbi.nlm.nih.gov/10482524/))

### F002 — FlgK replaces the FlgD hook-cap at the hook tip and is required for filament nucleation

FlgK's assembly role is best understood as a **cap-replacement event**. During hook morphogenesis, the transient scaffolding protein **FlgD** caps the distal, growing end of the hook and is required for hook polymerization; immunoelectron microscopy localizes FlgD to the distal hook end. Once the hook reaches its mature length, the FlgD cap is discarded and **FlgK is added to the hook tip as the first junction protein** ([PMID: 8157595](https://pubmed.ncbi.nlm.nih.gov/8157595/)). The obligatory nature of this hand-off is demonstrated by FlgE Dc-domain deletion mutants: these mutants still build hooks and still export FlgK, FlgL, and FliC, yet they fail to make a filament — precisely because the **FlgD-to-FlgK replacement at the hook tip is blocked** ([PMID: 27493542](https://pubmed.ncbi.nlm.nih.gov/27493542/)). This shows that FlgK docking at the hook tip is the committed, non-bypassable step that nucleates filament construction.

> *"these deletions inhibited the replacement of the FlgD hook cap by FlgK at the hook tip, thereby abolishing filament formation"* ([PMID: 27493542](https://pubmed.ncbi.nlm.nih.gov/27493542/))
>
> *"the hook, having reached its mature length, has the first of the hook-filament junction proteins, FlgK, added to its tip"* ([PMID: 8157595](https://pubmed.ncbi.nlm.nih.gov/8157595/))

### F003 — FlgK has a flagellin-like elongated α-helical bundle fold with accessory β-domains

The only crystal structure of a FlgK protein — from the pathogen *Burkholderia pseudomallei*, solved at **1.8 Å** — reveals a **multidomain fold**: a large, elongated α-helical bundle core with **two small β-domains protruding** from it. This architecture is structurally homologous to flagellin, the filament subunit. The authors generalize that flagellar hook-associated proteins share a **conserved elongated α-helical bundle scaffold** (equivalent to flagellin's D0/D1 coiled-coil domains, which build the tube wall) coupled to a **variable number of smaller outer domains** ([PMID: 25645451](https://pubmed.ncbi.nlm.nih.gov/25645451/)). This directly matches the domain annotation of Q88ES2 — Flag_bb_rod_N (IPR001444), Flg_bb/hook_C_dom (IPR010930), FlgK (IPR002371), and FlgK_D2-like (IPR049119) — confirming that the *P. putida* protein possesses the same conserved axial scaffold plus outer D2-like lobes.

> *"reveals a multidomain fold, comprising two small β-domains protruding from a large elongated α-helical bundle core. The evident structural similarity to flagellin ... suggests that ... flagellar hook-associated proteins are likely to show a conserved, elongated α-helical bundle scaffold coupled to a variable number of smaller domains."* ([PMID: 25645451](https://pubmed.ncbi.nlm.nih.gov/25645451/))

### F004 — FlgK is a late-class flagellar T3SS export substrate chaperoned by FlgN

FlgK does not fold and travel through the periplasm like a Sec substrate. Instead, it is **secreted in an unfolded state through the flagellum's ~2–3 nm central channel by the flagellar type III secretion system** and folds only upon reaching the growing distal tip. Its export is **temporally ordered**: FlgK, FlgL, FliD, and FliC are exported efficiently **only after hook assembly is complete**, because the export apparatus undergoes a substrate-specificity switch once the hook reaches mature length ([PMID: 10478459](https://pubmed.ncbi.nlm.nih.gov/10478459/)). Efficient FlgK export additionally requires the dedicated cytoplasmic chaperone **FlgN**, which binds specifically to the hook-associated proteins FlgK and FlgL ([PMID: 10320579](https://pubmed.ncbi.nlm.nih.gov/10320579/)). Loss of FlgN specifically reduces FlgK and FlgL export and causes premature leakage of unpolymerized flagellin, showing that FlgN-mediated FlgK delivery must precede and enable ordered filament polymerization ([PMID: 10320579](https://pubmed.ncbi.nlm.nih.gov/10320579/)).

> *"the FlgK, FlgL, FliD, and FliC proteins are exported efficiently only after completion of hook assembly"* ([PMID: 10478459](https://pubmed.ncbi.nlm.nih.gov/10478459/))
>
> *"FlgN binds to the flagellar hook-associated proteins (HAPs) FlgK and FlgL"* … *"export of FlgK and FlgL was specifically reduced, with concomitant increased release of unpolymerized flagellin"* ([PMID: 10320579](https://pubmed.ncbi.nlm.nih.gov/10320579/))

### F005 — *flgK* is a late (σ²⁸/FliA-dependent, class 3) flagellar gene; the flagellar system drives *P. putida* motility, adhesion, and biofilm

Transcriptionally, *flgK* sits at the **late tier** of the flagellar hierarchy. In *Salmonella*, the *flgK* promoter region contains **only a class 3 promoter**, dependent on the flagellum-specific sigma factor **FliA (σ²⁸)**, whereas earlier genes carry class 2 promoters ([PMID: 7770032](https://pubmed.ncbi.nlm.nih.gov/7770032/)). This places *flgK* among the last-expressed structural genes, co-regulated with filament and cap genes. The physiological importance of this late regulon in the target organism is demonstrated directly in *P. putida* KT2440: a non-polar **fliA mutant is non-motile**, shows **decreased binding to corn seeds and abiotic surfaces**, and forms **~3-fold less biofilm** ([PMID: 23766109](https://pubmed.ncbi.nlm.nih.gov/23766109/)). Since FlgK is an essential structural component of the FliA-dependent flagellar apparatus, these organism-level phenotypes — swimming motility, surface attachment, and colonization — are the biological processes to which FlgK contributes.

> *"the promoter region of fliD contains both class 2 and class 3 promoters, while that of flgK contains only a class 3 promoter"* ([PMID: 7770032](https://pubmed.ncbi.nlm.nih.gov/7770032/))
>
> *"The mutant strain was nonmotile and exhibited decreased capacity to bind to corn seeds"* … *"its ability to form biofilms decreased by almost threefold"* ([PMID: 23766109](https://pubmed.ncbi.nlm.nih.gov/23766109/))

### F006 — Q88ES2 sequence architecture (680 aa) confirms a secreted flagellin-like axial adapter

UniProt **Q88ES2** is a **680-residue, ~69.6 kDa** protein. Its domain layout mirrors the FlgK family template:

| Region (approx. residues) | Feature | InterPro |
|---|---|---|
| 7–34 | N-terminal flagellar basal-body rod domain (D0) | IPR001444 (Flag_bb_rod_N) |
| 93–323 | Central FlgK helical domain (with predicted coiled coil at 162–189) | IPR002371 (FlgK) |
| 338–419 | FlgK D2-like outer domain | IPR049119 (FlgK_D2-like) |
| ~420–640 | Large intervening outer region (species-variable D2/D3 lobes) | — |
| 640–678 | C-terminal flagellar basal-body/hook domain (D0/D1) | IPR010930 (Flg_bb/hook_C_dom) |

The extreme N-terminus (**MSSLISIGLSGLSASQAALSVTSNNIANAATSG…**) is the conserved amphipathic α-helical signature of flagellar axial proteins, and there is **no cleavable signal peptide** — consistent with fT3SS export rather than Sec secretion. UniProt keywords and subcellular-localization annotations are **"Secreted," "Bacterial flagellum," "Cell projection," and "Coiled coil."** Notably, *P. putida* FlgK is **~120 residues larger than enteric FlgK (~547–560 aa)**, a size difference attributable to the expanded surface-exposed outer domains — the very "variable number of smaller domains" predicted by the *Burkholderia* structure ([PMID: 25645451](https://pubmed.ncbi.nlm.nih.gov/25645451/)).

### F007 — In KT2440, *flgK* lies in a 59-gene flagellar cluster governed by a FleQ → σ⁵⁴/σ²⁸ three-tier cascade

The *P. putida* genome contains a **single flagellar cluster of 59 genes** organized into **11 operons with 22 characterized promoters**. Flagellar/chemotaxis synthesis is controlled by a **three-tier transcriptional cascade** in which the master regulator **fleQ is the Class I gene at the top** ([PMID: 34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/)). Upstream regulatory/export-gate genes (*flhA-flhF-fleN-fliA*) form a σ⁵⁴ (RpoN)-dependent operon activated by FleQ and repressed by FleN, while FliA (σ²⁸) drives late gene expression. Critically, this regulatory network is integrated with the second messenger **c-di-GMP**: FleN, together with FleQ and c-di-GMP, differentially regulates *lapA* (a large adhesin) and the *bcs* cellulose-synthase operon ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/)). As a hook–filament junction gene, *flgK* belongs to the late (σ²⁸/FliA-dependent, class 3) tier of this cascade, meaning its expression is coupled — via the same regulators — to the motile-versus-sessile lifestyle decision.

> *"A single region of the Pseudomonas putida genome, designated the flagellar cluster, includes 59 genes potentially involved in the biogenesis and function of the flagellar system."* … *"regulated by a three-tier cascade in which fleQ is a Class I gene, standing at the top of the transcriptional hierarchy"* ([PMID: 34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/))
>
> *"FleN, along with FleQ and the second messenger c-di-GMP differentially regulated transcription of lapA and the bcs operon, encoding a large adhesion protein and cellulose synthase"* ([PMID: 30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/))

### F008 — FlgK (HAP1) with FlgL (HAP3) forms the mechanical hook–filament junction zone completing axial assembly

The flagellar axial structure (rods, hook, hook-associated proteins, cap, filament) shares a **common subunit-arrangement architecture**, but each segment has **distinct mechanical properties tuned to its function** — the rod is a rigid straight cylinder while the hook is a flexible curved tube ([PMID: 31284631](https://pubmed.ncbi.nlm.nih.gov/31284631/)). Within this framework, HAP1 (FlgK) and HAP3 (FlgL) **connect the filament to the hook and are required for the last stage of flagellar assembly** ([PMID: 9168617](https://pubmed.ncbi.nlm.nih.gov/9168617/)). FlgK is added first (proximal, on the hook side) and FlgL second (distal, on the filament side); together they bridge the curvature and stiffness mismatch between the flexible hook (which functions as a universal joint) and the rigid, propeller-like filament, and they provide the platform onto which the FliD (HAP2) cap and flagellin subunits assemble. The two proteins are typically encoded together in a conserved **flgK operon**; in *Borrelia burgdorferi*, for example, the *flgK* operon comprises *flbF*, *flgK* (HAP1), *flgL* (HAP3), and *orfX* ([PMID: 9168617](https://pubmed.ncbi.nlm.nih.gov/9168617/)).

> *"the hook-associated proteins HAP1 and HAP3 connect the flagellar filament to the hook and are required for the last stage of flagellar assembly"* … *"The flgK operon consists of flbF (function unknown), flgK (encoding HAP1), flgL (encoding HAP3) and orfX"* ([PMID: 9168617](https://pubmed.ncbi.nlm.nih.gov/9168617/))
>
> *"They share a common basic architecture of subunit arrangement, but each part shows quite distinct mechanical properties to achieve its specific function."* ([PMID: 31284631](https://pubmed.ncbi.nlm.nih.gov/31284631/))

### F009 — The KT2440 genome confirms *flgK* (PP_4381) is adjacent to its junction partner *flgL* (PP_4380)

A direct query of the *P. putida* KT2440 genome/UniProt confirms the conserved hook–filament-junction gene neighborhood in the actual target organism:

| Locus | Gene | Product | UniProt | Length |
|---|---|---|---|---|
| PP_4382 | *flgJ* | Peptidoglycan hydrolase / rod-associated muramidase FlgJ | Q88ES1 | 384 aa |
| **PP_4381** | ***flgK*** | **Flagellar hook-associated protein 1 (HAP1)** | **Q88ES2** | **680 aa** |
| PP_4380 | *flgL* | Flagellar hook-associated protein FlgL (HAP3) | Q88ES3 | 521 aa |

FlgK's immediate downstream neighbor is its **obligate junction partner FlgL**, mirroring the conserved *flgK–flgL* operon organization documented across bacteria, while its upstream neighbor is the rod-associated muramidase **FlgJ**. This genomic context firmly places *flgK* within the basal-body/hook-filament assembly gene set in KT2440 itself, corroborating the functional assignment inferred from homology.

---

## Mechanistic Model / Interpretation

FlgK is best understood by tracing the flagellum from the cell body outward. The flagellum is built inside-out, subunit by subunit, with each axial protein exported through the central channel and added at the distal tip under a growing cap. FlgK occupies the transition point between two mechanically opposite structures.

```
   CELL EXTERIOR (distal, growing tip)
        │
   ┌────▼─────────────────────────────┐
   │  FILAMENT  (FliC / flagellin)     │  rigid, helical propeller
   │  + FliD (HAP2) cap at very tip    │
   └────▲─────────────────────────────┘
        │  ← FlgL (HAP3, PP_4380)  ── distal junction subunit
   ═════╪═════  HOOK–FILAMENT JUNCTION
        │  ← FlgK (HAP1, PP_4381)  ── PROXIMAL junction subunit  ★
   ┌────▼─────────────────────────────┐
   │  HOOK  (FlgE)                     │  flexible, curved universal joint
   └────▲─────────────────────────────┘
        │
   ┌────▼─────────────────────────────┐
   │  DISTAL + PROXIMAL RODS           │  rigid drive shaft
   │  (FlgJ muramidase clears PG, PP_4382)
   └────▲─────────────────────────────┘
        │
   ═════╪═════  OUTER MEMBRANE / PERIPLASM / INNER MEMBRANE
        │
   [ BASAL BODY + MS-ring + C-ring + fT3SS export apparatus ]
        │
   FlgK monomer (unfolded) ── chaperoned by FlgN ── threaded through
   the ~2 nm central channel  ─────────────────────────────────────►
   CELL INTERIOR (cytoplasm)
```

**Assembly logic.** The hook (FlgE) polymerizes under a transient FlgD cap until it reaches its genetically programmed mature length (~55 nm in *Salmonella*). At that point the export apparatus switches substrate specificity, the FlgD cap is jettisoned, and **FlgK — the first junction protein — docks onto the hook tip** (F002, F004). FlgK's proximal D0/D1 helical domains splice seamlessly into the 11-protofilament axial lattice shared by all axial proteins, while its expanded outer D2-like domains sit on the exterior surface (F003, F006). FlgL then adds on top of FlgK, and together the two form a short adapter zone that reconciles the **flexible, curved hook** with the **rigid, straight, helically wound filament** (F008). This junction is not merely a passive spacer: it transmits torque from the motor-driven rod/hook into the filament propeller while accommodating the dramatic change in mechanical properties (F001, F008). FlgK/FlgL also establish the correct surface lattice onto which the FliD (HAP2) cap can sit and chaperone flagellin folding at the tip.

**Why FlgK is non-enzymatic and where it acts.** FlgK has no catalytic residues, no substrate-binding pocket, and no transporter fold — it is a self-polymerizing structural subunit. Its "substrate," in the loosest sense, is itself and its neighbors: it recognizes the hook tip below and templates FlgL above. It performs its function entirely **outside the cell**, incorporated into the extracellular flagellar axial structure at its growing distal end (F006 subcellular localization: "Secreted," "Bacterial flagellum," "Cell projection").

**Regulatory and lifestyle integration in KT2440.** Expression of *flgK* is confined to the late, σ²⁸/FliA-dependent tier of a FleQ-topped, σ⁵⁴-relayed cascade (F005, F007). This ensures FlgK protein appears only when the basal body and hook are already built — a just-in-time logic that prevents wasteful or premature production of junction subunits. Because the same regulators (FleQ, FleN) also respond to **c-di-GMP** and control adhesin (*lapA*) and cellulose (*bcs*) genes, flagellar biogenesis — including *flgK* — is reciprocally coordinated with the switch to a sessile, biofilm lifestyle (F007). The functional payoff of a completed flagellum is demonstrated by the *fliA* mutant phenotype: loss of the late regulon abolishes motility and markedly reduces seed/surface binding and biofilm formation (F005). Thus FlgK, though a single structural rivet, is indispensable for the *P. putida* behaviors of swimming, root/surface colonization, and biofilm initiation.

---

## Evidence Base

| PMID | Title (abbreviated) | Organism | How it supports the annotation |
|---|---|---|---|
| [10482524](https://pubmed.ncbi.nlm.nih.gov/10482524/) | Hook subunit concentration & length control | *Salmonella* | Defines FlgK as HAP1, first junction protein; *flgK* mutants + FlgE overproduction give long hooks (F001) |
| [8157595](https://pubmed.ncbi.nlm.nih.gov/8157595/) | FlgD scaffolding protein for hook assembly | *Salmonella* | FlgK is added to hook tip after FlgD cap is discarded (F002) |
| [27493542](https://pubmed.ncbi.nlm.nih.gov/27493542/) | Role of FlgE Dc domain | *Salmonella* | FlgD→FlgK cap replacement at hook tip is obligatory for filament formation (F002) |
| [10478459](https://pubmed.ncbi.nlm.nih.gov/10478459/) | Substrate-specificity switching of export apparatus | *Salmonella* | FlgK exported only after hook completion; late fT3SS substrate (F004) |
| [10320579](https://pubmed.ncbi.nlm.nih.gov/10320579/) | FlgN/FliT chaperones | *Salmonella* | FlgN binds and is required for FlgK export (F004) |
| [25645451](https://pubmed.ncbi.nlm.nih.gov/25645451/) | Crystal structure of FlgK | *Burkholderia pseudomallei* | 1.8 Å structure: flagellin-like α-helical bundle + outer β-domains (F003, F006) |
| [7770032](https://pubmed.ncbi.nlm.nih.gov/7770032/) | Transcription of *flgK*/*fliD* operons | *Salmonella* | *flgK* has only a class 3 (σ²⁸/FliA) promoter — late gene (F005) |
| [23766109](https://pubmed.ncbi.nlm.nih.gov/23766109/) | *fliA* mutant characterization | *P. putida* KT2440 | Late flagellar regulon required for motility, adhesion, biofilm (F005) |
| [34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/) | *P. putida* flagellar system organization | *P. putida* | 59-gene cluster; FleQ-topped three-tier cascade containing *flgK* (F007) |
| [30889223](https://pubmed.ncbi.nlm.nih.gov/30889223/) | *flhF*/*fleN* regulation | *P. putida* | FleN + FleQ + c-di-GMP link flagellar regulators to adhesion/biofilm (F007) |
| [31284631](https://pubmed.ncbi.nlm.nih.gov/31284631/) | Architecture of distal rod and hook | (axial structure) | Axial proteins share a lattice but have distinct mechanical properties (F008) |
| [9168617](https://pubmed.ncbi.nlm.nih.gov/9168617/) | *flgK* motility operon | *Borrelia burgdorferi* | HAP1+HAP3 connect filament to hook; conserved *flgK*–*flgL* operon (F008) |
| [1848842](https://pubmed.ncbi.nlm.nih.gov/1848842/) | Coupling flagellin synthesis to assembly | *Salmonella* | Groups *flgK* with HAPs essential for assembly (F001) |

**Supporting / contextual literature.** Additional papers reinforce the model: *Caulobacter* hook-gene organization confirms FlgK/HAP1 assignment by sequence similarity ([PMID: 11405627](https://pubmed.ncbi.nlm.nih.gov/11405627/)); FliK/FlhB studies show *flhB*–*flgK* double mutants give polyhooks, linking FlgK to hook-length control ([PMID: 8071222](https://pubmed.ncbi.nlm.nih.gov/8071222/)); solution-interaction studies of monomeric axial proteins illuminate HAP heterodimer polarity and the suppression of self-assembly in the cytoplasm ([PMID: 12054831](https://pubmed.ncbi.nlm.nih.gov/12054831/)); *Vibrio parahaemolyticus* polar-flagellum genetics show HAP genes under σ²⁸ control with distinct sheathed-filament phenotypes ([PMID: 7883718](https://pubmed.ncbi.nlm.nih.gov/7883718/)); FlgK is an immunodominant, epitope-mapped antigen in *Salmonella* ([PMID: 29914677](https://pubmed.ncbi.nlm.nih.gov/29914677/)); and *flgK* loss reduces outer-membrane-vesicle production in *E. coli*, a downstream consequence of impaired flagellation ([PMID: 24134841](https://pubmed.ncbi.nlm.nih.gov/24134841/)).

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of Q88ES2 itself.** The functional assignment rests on strong homology to characterized FlgK proteins in *Salmonella*, *Burkholderia*, *Caulobacter*, *Borrelia*, and *Vibrio*, plus the KT2440 genomic context and the KT2440 *fliA*-mutant phenotype. There is no published *P. putida flgK* knockout, no purified-protein biochemistry, and no *P. putida*-specific structure. The mechanistic model is inferred, not directly demonstrated, for PP_4381.

2. **Structure is from a homolog.** The 1.8 Å crystal structure is of *B. pseudomallei* FlgK ([PMID: 25645451](https://pubmed.ncbi.nlm.nih.gov/25645451/)). *P. putida* FlgK is ~120 residues larger, with expanded outer domains (~res 420–640) that are unassigned to a single Pfam. The fold and surface features of these species-specific lobes remain unmodeled; whether they contribute additional functions (e.g., surface interactions, sheath contacts, rhizosphere recognition) is unknown.

3. **Stoichiometry and exact junction geometry uncharacterized in *P. putida*.** The number of FlgK subunits in the junction and their precise contacts with FlgE (hook) below and FlgL above have not been resolved for a *Pseudomonas* flagellum.

4. **Regulatory tier assigned by orthology.** The class 3 / σ²⁸-FliA assignment of *flgK* is anchored in *Salmonella* promoter mapping ([PMID: 7770032](https://pubmed.ncbi.nlm.nih.gov/7770032/)) and the KT2440 cascade architecture ([PMID: 34859548](https://pubmed.ncbi.nlm.nih.gov/34859548/)); the exact *flgK* promoter and its FliA dependence in KT2440 have not been individually mapped in the primary literature reviewed here.

5. **Polar vs. peritrichous context.** Much mechanistic detail derives from peritrichous enterics. *P. putida* is polarly flagellated (multi-trichous polar tuft), and polar-flagellum systems (cf. *Vibrio*, [PMID: 7883718](https://pubmed.ncbi.nlm.nih.gov/7883718/)) can show distinct HAP phenotypes; subtle *Pseudomonas*-specific features may not be captured by the enteric paradigm.

---

## Proposed Follow-up Experiments / Actions

1. **Construct a clean, non-polar *flgK* (PP_4381) deletion in KT2440** and assay swimming/swarming motility, filament presence by electron microscopy, and biofilm/seed-attachment. Prediction: a filament-less, non-motile, adhesion-deficient phenotype, with hooks still present (and possibly elongated). Complement in *trans* to confirm specificity.

2. **Cryo-EM of the *P. putida* hook–filament junction.** Purify intact flagella and resolve the FlgK/FlgL junction to define subunit stoichiometry, the FlgE→FlgK→FlgL→FliC lattice transition, and the disposition of the expanded *Pseudomonas*-specific outer domains.

3. **Map the *flgK* promoter in KT2440** by primer extension / 5′-RACE and RNA-seq in *fliA*, *fleQ*, and *fleN* backgrounds to experimentally confirm class 3 (σ²⁸) control and quantify c-di-GMP responsiveness.

4. **Test the FlgN–FlgK chaperone interaction in *P. putida*** (bacterial two-hybrid or pull-down; *flgN* deletion) to verify that the enteric export-chaperone logic operates in KT2440 and to check for leakage of unpolymerized flagellin.

5. **Structural/functional dissection of the outer domains (res ~420–640).** Delete or swap the expanded D2/D3-like region and test filament assembly, motility, and any surface/rhizosphere-colonization phenotypes to determine whether these lobes are purely structural or carry accessory functions.

6. **AlphaFold modeling + comparison** of full-length Q88ES2 against the *Burkholderia* FlgK structure to generate a testable model of the *Pseudomonas*-specific lobes, guiding the mutagenesis in item 5.

---

*Report prepared from 9 confirmed findings across 5 investigation iterations and 19 reviewed papers. The functional annotation of flgK (Q88ES2, PP_4381) as Flagellar Hook-Associated Protein 1 is assigned with high confidence based on convergent evidence from protein-family signatures, a homolog crystal structure, extensive comparative genetics, native genomic context in KT2440, and the motility/adhesion phenotype of the KT2440 late-flagellar regulon.*


## Artifacts

- [OpenScientist final report](flgK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](flgK-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10482524
2. PMID:1848842
3. PMID:8157595
4. PMID:27493542
5. PMID:25645451
6. PMID:10478459
7. PMID:10320579
8. PMID:7770032
9. PMID:23766109
10. PMID:34859548
11. PMID:30889223
12. PMID:31284631
13. PMID:9168617
14. PMID:11405627
15. PMID:8071222
16. PMID:12054831
17. PMID:7883718
18. PMID:29914677
19. PMID:24134841