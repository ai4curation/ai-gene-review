---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:08:37.024846'
end_time: '2026-07-20T15:19:16.627778'
duration_seconds: 639.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: nadA
  gene_symbol: nadA
  uniprot_accession: Q88NH8
  protein_description: 'RecName: Full=Quinolinate synthase {ECO:0000256|ARBA:ARBA00073059,
    ECO:0000256|HAMAP-Rule:MF_00567}; EC=2.5.1.72 {ECO:0000256|ARBA:ARBA00012669,
    ECO:0000256|HAMAP-Rule:MF_00567};'
  gene_info: Name=nadA {ECO:0000256|HAMAP-Rule:MF_00567, ECO:0000313|EMBL:AAN66855.1};
    OrderedLocusNames=PP_1231 {ECO:0000313|EMBL:AAN66855.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the quinolinate synthase family. Type 1
  protein_domains: NadA. (IPR003473); NadA_sf. (IPR036094); Quinolinate_synth_A_type1.
    (IPR023513); NadA (PF02445)
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
  path: nadA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NH8
- **Protein Description:** RecName: Full=Quinolinate synthase {ECO:0000256|ARBA:ARBA00073059, ECO:0000256|HAMAP-Rule:MF_00567}; EC=2.5.1.72 {ECO:0000256|ARBA:ARBA00012669, ECO:0000256|HAMAP-Rule:MF_00567};
- **Gene Information:** Name=nadA {ECO:0000256|HAMAP-Rule:MF_00567, ECO:0000313|EMBL:AAN66855.1}; OrderedLocusNames=PP_1231 {ECO:0000313|EMBL:AAN66855.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the quinolinate synthase family. Type 1
- **Key Domains:** NadA. (IPR003473); NadA_sf. (IPR036094); Quinolinate_synth_A_type1. (IPR023513); NadA (PF02445)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadA** (gene ID: nadA, UniProt: Q88NH8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: NadA — Quinolinate Synthase (Q88NH8)

**Gene:** *nadA* (OrderedLocusName PP_1231)
**Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / NCIMB 11950)
**UniProt:** Q88NH8 · **EC:** 2.5.1.72
**Family:** Quinolinate synthase family, Type 1 (Pfam PF02445 / NadA; InterPro IPR003473, IPR036094, IPR023513)

---

## 1. Summary (Answer to the Research Question)

NadA is **quinolinate synthase**, a cytoplasmic [4Fe-4S] cluster–dependent enzyme that catalyzes the committed step of *de novo* NAD biosynthesis: the condensation of **dihydroxyacetone phosphate (DHAP)** with **iminoaspartate (IA)** to form **quinolinic acid (QA)**, the universal pyridine-ring precursor of nicotinamide adenine dinucleotide (NAD). It functions in the soluble cytoplasm as the second enzyme of the bacterial NadB→NadA→NadC pathway, converting the product of L-aspartate oxidase (NadB) into a substrate for quinolinate phosphoribosyltransferase (NadC).

Gene-identity verification: the symbol *nadA*, the protein description (quinolinate synthase, EC 2.5.1.72), the "Type 1 quinolinate synthase" family, and the NadA/PF02445 domain architecture are all mutually consistent and match a large body of primary biochemical and structural literature on NadA orthologs. There is **no ambiguity** — this is a well-characterized enzyme, and the mechanistic conclusions below are drawn from studies on close orthologs (*E. coli*, *Thermotoga maritima*, *M. tuberculosis*, *Pyrococcus horikoshii*, *B. subtilis*) whose reaction chemistry and cofactor are conserved.

---

## 2. Primary Function: Reaction Catalyzed and Substrate Specificity

NadA catalyzes:

> **DHAP + iminoaspartate → quinolinic acid + 2 H₂O + Pᵢ**

Quinolinic acid is described as "a central intermediate in the biosynthesis of nicotinamide adenine dinucleotide (NAD)" and "the universal precursor" of the cofactor (PMID 18803397; PMID 34609124).

**Substrate specificity — the triose:** Biochemical work resolved a long-standing debate over whether DHAP or glyceraldehyde-3-phosphate (G-3P) is the true co-substrate. Reichmann, Couté & Ollagnier de Choudens (2015) demonstrated "that DHAP is the triose that condenses with IA to form QA," and that NadA's apparent capacity to use G-3P "is due to its previously unknown triose phosphate isomerase activity" (PMID 26455817). Thus **DHAP is the physiological triose substrate**, and NadA carries an intrinsic TIM-like isomerase activity that funnels G-3P into DHAP.

**Substrate specificity — the amino donor:** The second substrate, iminoaspartate, is not free in solution but is generated immediately upstream by L-aspartate oxidase (NadB): NadB "catalyzes the formation of iminoaspartate that is used by quinolinate synthase NadA in a condensation reaction with dihydroxyacetone phosphate to produce quinolinic acid" (PMID 41066930).

**Multistep chemistry within one active site:** The overall transformation is complex — "condensation of dihydroxyacetone phosphate (DHAP) and iminoaspartate (IA), which involves dephosphorylation, isomerization, cyclization, and two dehydration steps" (PMID 34609124). Crystallographic snapshots of *T. maritima* NadA trapped a condensation intermediate ("W"), a DHAP analogue, and the QA product, and showed directly that "condensation causes dephosphorylation" (PMID 27545412). NadA is therefore best described as a multifunctional dehydratase/cyclase that assembles the pyridine ring of QA.

---

## 3. Cofactor: A Catalytic [4Fe-4S] Cluster

NadA is an iron–sulfur enzyme. The *E. coli* protein was hypothesized to contain an Fe-S cluster "as early as 1991, because of its observed labile activity, especially in the presence of hyperbaric oxygen, and because its primary structure contained a CXXCXXC motif" (PMID 18803397); this was confirmed spectroscopically (Mössbauer/EPR). Saunders et al. (2008) showed that "[4Fe-4S] clusters are common cofactors throughout this class of enzymes" across *E. coli*, *M. tuberculosis* and *P. horikoshii* (PMID 18803397).

Crucially, the cluster carries "a unique noncysteinyl-ligated iron ion" (PMID 31390192). This fourth iron acts as a **Lewis-acid catalytic center**: rather than an electron-transfer role, it coordinates hydroxyl/carboxyl groups of the substrates and intermediate, activating them for the dehydration and cyclization steps. The requirement for this cluster explains the enzyme's characteristic oxygen sensitivity.

**Cofactor maturation:** The [4Fe-4S] cluster must be installed by dedicated sulfur-mobilization machinery. Jones et al. (2026) showed in *B. subtilis* that the cysteine sulfurtransferase NifS "is catalytically competent in promoting cluster assembly onto apo-NadA and that the rate of reactivation depends on the rate of sulfur mobilization," with apo-NadA reciprocally enhancing NifS turnover (PMID 41066930). In *P. putida*, an analogous cysteine-desulfurase/Suf/Isc system is expected to mature the cluster.

---

## 3b. Direct Sequence Evidence for the P. putida Enzyme (PP_1231)

To ground the annotation in the specific target protein rather than family membership alone, I analyzed the Q88NH8 sequence (352 aa) directly. A Needleman–Wunsch global alignment shows **P. putida NadA is 67.5% identical to E. coli NadA (P11458)** over its full length (233/345 aligned positions) — well within the range expected for direct orthologs with conserved function.

Critically, the **three catalytic [4Fe-4S]-ligating cysteines** identified in *E. coli* NadA are **conserved in identical local sequence contexts**, one contributed by each of the three homologous domains:

| Ligand | *E. coli* NadA | *P. putida* NadA (PP_1231) |
|--------|----------------|-----------------------------|
| 1 | Cys113 — `LQAE`**C**`SLDL` | Cys114 — `LEAT`**C**`SLDL` |
| 2 | Cys200 — `WQGA`**C**`IVHD` | Cys201 — `WDGA`**C**`IVHE` |
| 3 | Cys297 — `S`**C**`AHCPWMA` | Cys298 — `S`**C**`AHCPWMA` (locally identical) |

The third ligand sits within a conserved C-terminal `CRSCAHC` motif matching the CXXCXXC Fe-S signature noted for NadA (PMID 18803397). This perfect conservation of the domain-distributed cluster ligands confirms that PP_1231 adopts the canonical three-domain NadA fold and ligates its catalytic cluster identically to characterized orthologs — so the reaction chemistry, DHAP + iminoaspartate substrate specificity, and mechanism described above apply directly to the *P. putida* enzyme. *(Analysis performed in this study.)*

---

## 4. Structure and Active-Site Architecture

NadA folds into **three homologous domains** whose "convergence… defines a narrow active site that contains a catalytically essential [4Fe-4S] cluster" (PMID 34609124). Access to the buried cofactor is controlled by "a tunnel, which can be opened or closed depending on the nature (or absence) of the bound ligand" (PMID 34609124) — a gating mechanism for substrate entry and product release.

A notable mechanistic puzzle is that the characterized active site is too small to bind both DHAP and iminoaspartate at once. Basbous et al. (2021), combining mutagenesis, X-ray crystallography, functional assays and molecular dynamics, proposed a condensation mechanism involving "the transient formation of a second active site cavity to which one of the substrates can migrate before this reaction takes place" (PMID 34609124), elegantly resolving how two substrates are co-processed in a confined pocket.

---

## 5. Localization

NadA is a **soluble cytoplasmic enzyme**. It bears no signal peptide or membrane-spanning segments, and its substrates (DHAP from central carbon metabolism; iminoaspartate handed off from cytoplasmic NadB) and its oxygen-labile [4Fe-4S] cofactor are all consistent with function in the reducing intracellular environment. Its reaction is physically and kinetically coupled to the upstream flavoenzyme NadB, which supplies the unstable iminoaspartate intermediate directly (PMID 41066930).

---

## 6. Pathway Context and Biological Role

NadA is the second of three enzymes in the bacterial **de novo NAD biosynthesis pathway**:

1. **NadB** (L-aspartate oxidase): L-aspartate → iminoaspartate
2. **NadA** (quinolinate synthase): iminoaspartate + DHAP → **quinolinic acid**
3. **NadC** (quinolinate phosphoribosyltransferase): quinolinic acid + PRPP → nicotinate mononucleotide (NaMN)

NaMN is then adenylylated (NadD) and amidated (NadE) to yield NAD. This entire route is genomically intact in *P. putida* KT2440: a UniProt survey (taxid 160488) confirms all partners are encoded — **nadB** (Q88MZ2, L-aspartate oxidase), **nadA** (Q88NH8, this protein), **nadC** (Q88PR1, quinolinate phosphoribosyltransferase), **nadD** (Q88DL5) and **nadE** (Q88DF6) — so the organism can synthesize NAD de novo from L-aspartate, with NadA performing the committed ring-forming step *(analysis performed in this study)*. NadA thus performs the ring-forming step that commits carbon and nitrogen skeletons to the pyridine nucleotide pool. Because "most bacterial species cannot get NAD+ from their surroundings" and must synthesize the cofactor (PMID 38182101), the de novo enzymes are of interest as antibacterial targets. In *P. putida*, NAD homeostasis is additionally shaped by salvage routes and by an active nicotinate catabolism (nic) locus whose dysregulation "affected... NAD biosynthesis" in the related organism *Bordetella*, a system "highly similar to that characterized in *Pseudomonas putida* KT2440" (PMID 29485696).

---

## 7. Supported and Refuted Hypotheses

**Supported:**
- NadA is quinolinate synthase (EC 2.5.1.72) condensing DHAP + iminoaspartate → quinolinic acid (PMID 18803397, 26455817, 34609124).
- DHAP, not G-3P, is the true triose substrate; NadA has intrinsic triose-phosphate isomerase activity (PMID 26455817).
- NadA requires a catalytic [4Fe-4S] cluster with a unique non-Cys-ligated iron (PMID 18803397, 31390192).
- Reaction proceeds via dephosphorylation, isomerization, cyclization and two dehydrations within a three-domain, tunnel-gated active site (PMID 27545412, 34609124).
- Cluster maturation depends on cysteine-desulfurase machinery (PMID 41066930).

**Refuted / superseded:**
- Early reports (P. horikoshii structure) that NadA might lack an Fe-S cluster were superseded; the [4Fe-4S] cofactor is now recognized as conserved across the family (PMID 18803397).
- The hypothesis that G-3P is the direct condensation partner was refuted in favor of DHAP (PMID 26455817).

---

## 8. Limitations and Future Directions

- No study reported here characterizes the *P. putida* KT2440 NadA enzyme directly; conclusions are inferred from highly conserved orthologs and from domain/family assignment. Direct kinetic and structural characterization of PP_1231 would confirm strain-specific parameters.
- The precise identity of the *P. putida* Fe-S cluster–maturation partner(s) (Isc/Suf/IscS) for NadA remains to be established experimentally.
- Regulation of *nadA* expression in *P. putida* relative to salvage flux and the nicotinate degradation (nic) pathway warrants targeted study.

---

### Key References
- PMID 26455817 — Reichmann et al. (2015), *dual TIM/dehydration activity; DHAP is the substrate*.
- PMID 18803397 — Saunders et al. (2008), *[4Fe-4S] clusters common across NadA*.
- PMID 31390192 — Esakova et al. (2019), *unique non-Cys-ligated iron; reaction intermediate*.
- PMID 27545412 — Volbeda et al. (2016), *crystal structures of intermediate/product*.
- PMID 34609124 — Basbous et al. (2021), *three-domain fold, tunnel, transient second cavity*.
- PMID 41066930 — Jones et al. (2026), *NadB→NadA pathway; NifS cluster assembly*.
- PMID 29485696 — Brickman & Armstrong (2018), *P. putida KT2440 nic locus / NAD context*.


## Artifacts

- [OpenScientist final report](nadA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadA-deep-research-openscientist_artifacts/final_report.pdf)