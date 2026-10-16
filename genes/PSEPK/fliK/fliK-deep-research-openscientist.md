---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:33:25.736988'
end_time: '2026-08-31T20:02:07.914001'
duration_seconds: 1722.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fliK
  gene_symbol: fliK
  uniprot_accession: Q88EU2
  protein_description: 'SubName: Full=Flagellar hook-length control protein FliK {ECO:0000313|EMBL:AAN69939.1};'
  gene_info: Name=fliK {ECO:0000313|EMBL:AAN69939.1}; OrderedLocusNames=PP_4361 {ECO:0000313|EMBL:AAN69939.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Flagellar_hook_control-like_C. (IPR021136); FliK. (IPR052563);
    FliK-like_C_sf. (IPR038610); Flg_hook (PF02120)
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
  path: fliK-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fliK-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EU2
- **Protein Description:** SubName: Full=Flagellar hook-length control protein FliK {ECO:0000313|EMBL:AAN69939.1};
- **Gene Information:** Name=fliK {ECO:0000313|EMBL:AAN69939.1}; OrderedLocusNames=PP_4361 {ECO:0000313|EMBL:AAN69939.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Flagellar_hook_control-like_C. (IPR021136); FliK. (IPR052563); FliK-like_C_sf. (IPR038610); Flg_hook (PF02120)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fliK" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fliK' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fliK** (gene ID: fliK, UniProt: Q88EU2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: FliK (Q88EU2, PP_4361) — Flagellar Hook-Length Control Protein of *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**fliK** (UniProt **Q88EU2**; ordered locus **PP_4361**) of *Pseudomonas putida* KT2440 encodes the **flagellar hook-length control protein FliK**, a **secreted "molecular ruler."** Its primary function is not enzymatic in the classical sense but **regulatory/adaptor**: during flagellar assembly it (i) **measures the length of the growing rod–hook structure**, and (ii) upon the hook reaching its mature length (~55 nm in the model organism *Salmonella*), **triggers a switch in the substrate specificity of the flagellar type III secretion system (fT3SS)** — from export of rod/hook subunits to export of filament subunits (flagellin). It carries out this role **at/within the flagellar export apparatus**, being **intermittently secreted through the nascent flagellar channel**, and functions within the **flagellar biogenesis pathway** by acting on the export gatekeeper **FlhB**.

Gene identity is confirmed: the gene symbol *fliK*, the protein description, the organism, and the InterPro/Pfam domain signatures (FliK family; T3S4/Flg_hook C-terminal domain) are all mutually consistent (see §2). Direct mechanistic experiments derive almost entirely from *Salmonella enterica* and *Escherichia coli*; the *P. putida* protein is characterized here **by orthology and domain architecture**, supported by evidence that KT2440 possesses a functional, hierarchically regulated flagellar system.

---

## 2. Gene/Protein Identity Verification

| Attribute | Value | Consistent? |
|---|---|---|
| Gene symbol | *fliK* | ✅ matches FliK family |
| UniProt | Q88EU2 | ✅ |
| Locus | PP_4361 | ✅ |
| Organism | *Pseudomonas putida* KT2440 | ✅ |
| Length | 421 aa | ✅ (typical FliK ~40 kDa; *Salmonella* 405 aa / 41.7 kDa, *E. coli* 39.2 kDa [PMID 8631687]) |
| Pfam | **PF02120** (Flg_hook) | ✅ FliK/T3S4 C-terminal domain |
| InterPro | **IPR052563** (FliK), **IPR021136** (Flagellar_hook_control-like_C), **IPR038610** (FliK-like C superfamily) | ✅ |
| Gene3D | 3.30.750.140 (C-terminal core fold) | ✅ |
| PANTHER | PTHR37533 "FLAGELLAR HOOK-LENGTH CONTROL PROTEIN" | ✅ |
| UniProt keywords | Flagellum, Cilium, Cell projection | ✅ |

**Sequence-composition corroboration.** The Q88EU2 sequence is markedly **Ala-rich (19.5%)** and **Gln-rich (10%)**, with a Gln stretch in the C-terminal region (…SRGQ**QQQQ**GQAQGSNL…) and abundant Pro (5.2%). This low-complexity, hydrophilic composition matches the described FliK architecture — an **intrinsically disordered N-terminal ruler region** followed by a **compact folded C-terminal domain** — and mirrors the historical observation that *Salmonella*/*E. coli* FliK are "fairly hydrophilic" with proline/glutamine-rich central and C-terminal regions [PMID 8631687].

**Conclusion:** This is an authentic FliK ortholog. The gene symbol is **not** ambiguous for this entry; the challenge is only that direct functional studies are in enteric model bacteria, not *P. putida* itself.

---

## 3. Primary Function

### 3.1 FliK is a secreted molecular ruler that sets hook length
FliK controls the length of the flagellar hook. In *Salmonella*, "the hook structure is controlled to a length of 55 nm by a molecular ruler protein, FliK" [PMID 28389943]; "FliK, a secreted molecular ruler, controls hook length" [PMID 21654632]. Systematic N-terminal insertion/deletion analysis demonstrated that hook length is **proportional to the molecular size of the ruler** — inserting Yersinia YscP fragments into FliK produced longer hooks in proportion to the added length — supporting a genuine **internal molecular-ruler** mechanism rather than subunit counting [PMID 17542929].

### 3.2 FliK triggers the export substrate-specificity switch
The second, coupled function is catalysis of the **rod/hook → filament secretion-specificity switch**. "Upon hook completion, FliK induces a secretion-specificity switch to filament-type substrate secretion" [PMID 21654632], "which allows secretion of filament-type substrates, such as flagellin" [PMID 28389943]. FliK is thus the **checkpoint-control protein** that senses hook completion and licenses the final (filament) stage of assembly [PMID 17456739]. Three proteins — **FliK, FlhB and FlhA** — jointly execute this switch, which is "the most important morphological checkpoint of the sequential flagellar assembly process" [PMID 29850796].

### 3.3 Two separable activities in two domains
FliK is bifunctional: "the N-terminal half (FliK(N)) determines length and the C-terminal half (FliK(C)) switches secretion from the hook protein to the filament protein" [PMID 21510958]. The N-terminal domain (FliK_N) is the flexible ruler; it binds the hook-capping protein **FlgD** (high affinity) and hook protein **FlgE** (low affinity), i.e., it interacts with the distal, growing tip during measurement [PMID 16630628]. The C-terminal domain (**FliK_C**) contains the conserved **T3S4 domain** (Type III Secretion Substrate-specificity Switch) — "a new protein domain… called T3S4," conserved across the FliK family and injectisome length regulators (e.g., YscP) [PMID 15773978]. This C-terminal region is the most conserved part of FliK and is essential for function (linker insertions abolish motility) [PMID 8631687].

---

## 4. Molecular Mechanism

### 4.1 The C-terminal domain acts on FlhB
The switch is executed by **FliK_C binding the cytoplasmic domain of FlhB** (FlhB_C), "the switchable secretion gate" [PMID 21510958]. FlhB undergoes **autocatalytic cleavage** at a conserved **NPTH** motif (residue N269 in *Salmonella*); cleavage is required for a functional switch [PMID 20586476]. NMR of FliK showed the protein is **largely unstructured** with a **compact FliK_C core domain** (two α-helices and a mixed β-sheet); a model places a FliK_C loop in contact with the cleaved NPTH of FlhB_C to trigger switching, contact that is sterically blocked when NPTH is uncleaved [PMID 21510958]. Quantitative interaction studies place the FliK–FlhB_C affinity in the **low-micromolar range (~1–10 µM)** with complex fast/slow kinetics and a post-binding conformational change [PMID 20586476; PMID 26244937]. Recent work adds that FliK-driven switching also requires **FlhA/FlhB conformational rearrangements** [PMID 31712281] and a **flexible linker** between FliK_N and FliK_C for productive export switching [PMID 31964971].

### 4.2 The "infrequent ruler" model — measurement during secretion
FliK is **not a static internal caliper**; it is **intermittently secreted during hook polymerization**, and "the probability of the specificity switch is an increasing function of hook length" [PMID 21654632]. Deletion variants that still measure hook length are secreted, showing "FliK directly measures rod-hook length **during the secretion process**"; overall "FliK acts as a molecular ruler that takes measurements of rod-hook length while being intermittently secreted during the assembly process of the hook-basal body complex" [PMID 20132451]. The infrequent-ruler model quantitatively fits experimental data and merodiploid short/long-ruler experiments (a short ruler dominates), and hook length is also modulated by hook **polymerization rate** ("molecular clock" contribution) [PMID 21654632; PMID 16630628; PMID 20132451]. The C-ring is **not** required for hook-length control, refuting the earlier "measuring cup" model [PMID 20132451].

### 4.3 Newest mechanistic refinement (2026)
The switch is now understood as **active de-repression**: FliK-dependent **ejection of two inhibitory components** — the cleaved C-terminal domain of FlhB and a component termed "Fluke" — "irreversibly triggers the transition to late substrate export," i.e., switching is driven by removal of inhibitors that actively hold the machine in the early state, rather than by passive sensing alone [PMID 42262106; PMID 41959102].

---

## 5. Subcellular Localization / Site of Function

- **UniProt localization keywords:** Flagellum, Cilium, Cell projection.
- FliK is a **cytoplasmic/export substrate** of the fT3SS. It performs its function **at and within the flagellar export apparatus and the nascent rod–hook channel**, being transiently threaded through the growing structure ("intermittently secreted"), with its N-terminus reaching the distal hook tip/cap (FlgD/FlgE contacts) and its C-terminus engaging FlhB_C at the cytoplasmic face of the export gate [PMID 20132451; PMID 16630628; PMID 21510958].
- It is therefore **not a stable structural component** of the mature flagellum; it acts transiently during assembly and is partly secreted to the cell exterior. *P. putida* KT2440 is monotrichously flagellated (single polar flagellum), so this activity occurs at the cell pole during flagellar biogenesis.

---

## 5b. Organism-Specific Evidence for the *P. putida* Protein (This Study)

Because no direct experiments on *P. putida* FliK exist, I generated two independent lines of organism-specific bioinformatic/structural evidence for Q88EU2 itself:

**(i) Genomic synteny — PP_4361 lies inside the flagellar structural/export cluster.** Mapping the loci flanking PP_4361 shows an unbroken flagellar gene neighborhood:

| Locus | Gene | Product |
|---|---|---|
| PP_4355 | *fliP* | Flagellar biosynthetic protein FliP (export apparatus) |
| PP_4356 | *fliO* | Flagellar export protein FliO |
| PP_4357 | *fliN* | Flagellar motor switch protein FliN (C-ring) |
| PP_4358 | *fliM* | Flagellar motor switch protein FliM (C-ring) |
| PP_4359 | *fliL* | Flagellar protein FliL |
| **PP_4361** | **_fliK_** | **Flagellar hook-length control protein FliK** |
| PP_4365 | *fliJ* | Flagellar FliJ protein (export chaperone escort) |
| PP_4366 | *fliI* | Flagellum-specific ATP synthase FliI |
| PP_4367 | *fliH* | Flagellar assembly protein FliH |

*fliK* sits directly among the fT3SS export apparatus (FliO/FliP), the motor/C-ring switch (FliM/FliN), and the export ATPase complex (FliH/FliI/FliJ) — i.e., the very machinery with which FliK functionally interacts — providing strong organism-specific support that PP_4361 is a genuine flagellar-assembly gene.

**(ii) AlphaFold structure prediction of Q88EU2 recapitulates the bipartite FliK architecture.** Analysis of the AlphaFold DB model (AF-Q88EU2, 421 residues) shows:
- **N-terminal region (1–270): mean pLDDT 50.1; 55% of residues pLDDT < 50** → predicted **intrinsically disordered** — consistent with the flexible "tape-measure" ruler (FliK_N).
- **C-terminal domain (271–383): mean pLDDT 78.2; 70% of residues pLDDT > 70** → a **confidently folded globular domain** — the **FliK_C / T3S4** switch module.
- **C-terminal tail (384–421): mean pLDDT 52.5** → disordered.

These predicted boundaries agree with independent annotations (Pfam PF02120: 291–374; CDD cd17470: 282–368; Gene3D 3.30.750.140: 271–383), and the InterPro *FliK family* signature (IPR052563) spans residues 22–421. This confirms that the *P. putida* protein — not merely its *Salmonella* ortholog — has the canonical disordered-ruler-plus-folded-T3S4 architecture that underlies the proposed mechanism.

---

## 6. Pathway Context

FliK operates within the **flagellar biogenesis / type III secretion pathway**, specifically at the **hook-completion checkpoint** that couples morphological progress to gene expression and export hierarchy:

- **Export partners:** FlhB (direct switch partner), FlhA, and the ATPase complex (FliI/FliH) coordinate hierarchical export [PMID 29850796; PMID 26244937].
- **Regulatory coupling:** The specificity switch also enables secretion of the anti-σ²⁸ factor **FlgM**, de-repressing σ²⁸ (FliA)-dependent late (filament/chemotaxis) genes — linking assembly state to transcription [PMID 25313396].
- **In *P. putida* KT2440:** the flagellar/chemotaxis regulon is intact and functional; *fliA* (σ²⁸) "is in a cluster with other genes involved in flagella biosynthesis and chemotaxis," and a *fliA* mutant is **nonmotile** with reduced adhesion and ~3-fold reduced biofilm formation [PMID 23766109]. FliK/PP_4361 functions upstream of/within this hierarchy to enable proper hook length and the transition to filament assembly.

---

## 6b. Evolutionary Note — Basis for Functional Transfer

FliK is one of the **most rapidly diverging flagellar proteins**. Even between the closely related enterobacteria *Salmonella* and *E. coli*, FliK shares only **50% overall identity**, with the C-terminal ~154 aa the most conserved part (71%) [PMID 8631687]. Consistent with this, a naive global alignment of *P. putida* FliK (Q88EU2) against *Salmonella* FliK (P26416) yields only **~28% identity across the C-terminal T3S4 domain and ~30% over the N-terminus** — low pairwise identity typical for this family across genera. Homology and functional assignment therefore rest **not on pairwise identity but on sensitive profile/HMM-based domain membership** (shared InterPro IPR052563, Pfam PF02120, CDD cd17470, PANTHER PTHR37533) and the shared bipartite fold reproduced by AlphaFold. The rapid divergence of the disordered N-terminal ruler is itself mechanistically sensible: for a length-encoding spacer, **overall length matters more than specific sequence**, so the ruler tolerates substitutions/indels as long as its effective length is preserved.

---

## 7. Supported and Refuted Hypotheses

**Supported**
- FliK is a secreted molecular ruler controlling hook length [PMID 21654632; 28389943; 17542929].
- Bifunctional two-domain architecture: N-terminal ruler + C-terminal T3S4 switch domain [PMID 21510958; 15773978].
- Switch executed via FliK_C–FlhB_C interaction requiring FlhB autocleavage [PMID 21510958; 20586476].
- Measurement occurs during intermittent secretion ("infrequent ruler") [PMID 20132451; 21654632].
- Q88EU2 is an authentic FliK ortholog by domain/family signatures and composition [UniProt; PMID 8631687].

**Refuted / superseded**
- "Measuring cup" / C-ring-based counting model — refuted; hook-length control persists without the C-ring [PMID 20132451].
- Pure subunit-counting (no ruler) — inconsistent with ruler-length-proportional hook lengths [PMID 17542929].
- Early skepticism that FliK is a ruler [PMID 8631687] — superseded by later quantitative ruler evidence.

---

## 8. Limitations and Future Directions

- **No *P. putida*-specific FliK study exists.** All mechanistic data derive from *Salmonella*/*E. coli*/*Yersinia*; the KT2440 assignment is by strong orthology, conserved domain architecture, and a functional flagellar regulon, not direct biochemistry.
- **Hook length set point in *P. putida* is not experimentally established** (the 55 nm value is *Salmonella*-specific); it may differ given the polar-flagellum lifestyle.
- **Future work:** *P. putida fliK* deletion/complementation and hook-length EM; test FliK–FlhB interaction and T3S4 function in KT2440; determine whether ruler length tuning alters polar-flagellum hook geometry, motility, adhesion, and biofilm phenotypes.

---

### Key references (PMIDs)
21654632, 28389943, 20132451, 17542929, 17456739, 16630628, 15773978, 8631687, 21510958, 20586476, 26244937, 31712281, 31964971, 29850796, 25313396, 42262106, 41959102, 23766109. UniProt Q88EU2; InterPro IPR052563/IPR021136/IPR038610; Pfam PF02120.


## Artifacts

- [OpenScientist final report](fliK-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fliK-deep-research-openscientist_artifacts/final_report.pdf)