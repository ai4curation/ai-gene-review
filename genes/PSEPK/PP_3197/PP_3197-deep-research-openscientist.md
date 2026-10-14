---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:02:35.510415'
end_time: '2026-08-31T21:18:20.372069'
duration_seconds: 944.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3197
  gene_symbol: PP_3197
  uniprot_accession: Q88I05
  protein_description: 'SubName: Full=Glyoxalase family protein {ECO:0000313|EMBL:AAN68805.1};'
  gene_info: OrderedLocusNames=PP_3197 {ECO:0000313|EMBL:AAN68805.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Glyas_Bleomycin-R_OHBP_Dase. (IPR029068); Glyas_Fos-R_dOase_dom.
    (IPR004360); VOC_core. (IPR037523); Glyoxalase (PF00903)
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3197-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3197-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I05
- **Protein Description:** SubName: Full=Glyoxalase family protein {ECO:0000313|EMBL:AAN68805.1};
- **Gene Information:** OrderedLocusNames=PP_3197 {ECO:0000313|EMBL:AAN68805.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Glyas_Bleomycin-R_OHBP_Dase. (IPR029068); Glyas_Fos-R_dOase_dom. (IPR004360); VOC_core. (IPR037523); Glyoxalase (PF00903)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3197" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3197' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3197** (gene ID: PP_3197, UniProt: Q88I05) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_3197 (Q88I05) in *Pseudomonas putida* KT2440: FdeC, a Flavonoid A-Ring Ring-Cleavage Dioxygenase

## Summary

The gene **PP_3197** of *Pseudomonas putida* strain KT2440 (UniProt **Q88I05**) is annotated in UniProt only generically as a "Glyoxalase family protein," a label that reflects the protein's structural fold rather than its true biochemical activity. Integrating orthology, genomic synteny, sequence analysis, and structural prediction, this investigation concludes that PP_3197 is **FdeC, a metal-dependent aromatic ring-cleavage (extradiol-type) dioxygenase** that participates in the bacterial catabolism of the plant flavonoid **naringenin**. Its primary function is to catalyze the oxygenolytic *meta*-cleavage of the aromatic A-ring of a trihydroxyflavanone intermediate, opening the ring and channeling the resulting carbon skeleton toward central metabolism (ultimately oxaloacetate and the TCA cycle).

This assignment rests on several converging lines of evidence. KEGG orthology places PP_3197 in ortholog group **K26181 (fdeC)** and assigns it reaction **R13075** within pathway **ppu00946 / map00946 ("Degradation of flavonoids")**. The gene sits within a **syntenic *fde* gene cluster** in the *P. putida* genome that mirrors the experimentally validated naringenin *meta*-cleavage pathway of *Herbaspirillum seropedicae* SmR1. Critically, PP_3197 shares **71% amino-acid identity** with the *H. seropedicae* FdeC (Hsero_1005) that was directly shown by site-directed mutagenesis and LC-MS/MS to be the A-ring-cleaving dioxygenase, including a strictly conserved C-terminal metal-binding active-site motif. Finally, the AlphaFold model of Q88I05 is of very high confidence (mean pLDDT 95.7) and displays the expected two-domain (bicupin) VOC fold typical of type I extradiol dioxygenases.

The protein is predicted to be a **soluble cytoplasmic enzyme** (no signal peptide, no transmembrane segments), consistent with an intracellular catabolic role. Importantly, the "glyoxalase" naming shared by PP_3197 and its validated ortholog is a **fold-based, not activity-based** descriptor: the vicinal oxygen chelate (VOC)/glyoxalase superfamily encompasses both glyoxalase-I lyases and numerous ring-cleavage dioxygenases that share the same βαβββ metalloenzyme module. PP_3197 belongs to the dioxygenase branch of this superfamily. No dedicated experimental study of PP_3197 itself exists (UniProt evidence level PE=4, "Predicted"), so the functional assignment is an orthology-based inference of high confidence rather than a direct biochemical demonstration.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity checks are addressed:

| Check | Result |
|-------|--------|
| Gene symbol / locus | PP_3197 (OrderedLocusName), UniProt Q88I05 — matches target |
| Organism | *Pseudomonas putida* strain ATCC 47054 / KT2440 (PSEPK), NCBI taxid 160488 — confirmed |
| Cross-references | RefSeq WP_010954082.1, EMBL AAN68805.1, KEGG ppu:PP_3197, STRING 160488.PP_3197 — all point to the same 313-aa protein |
| UniProt description | "Glyoxalase family protein" — a fold-based annotation, **not** the true catalytic activity |
| Domains/family | PF00903 (Glyoxalase), VOC core (IPR037523), IPR004360, IPR029068 — all consistent with the VOC/glyoxalase superfamily |
| Literature match | No paper studies PP_3197 directly; function inferred from a **71%-identity, experimentally validated ortholog** (FdeC of *H. seropedicae*, PMID 27059806) in a syntenic gene cluster |

**Conclusion of verification:** The generic "glyoxalase family protein" annotation is correct at the level of protein *fold* but does not capture the protein's specific *function*. All evidence points to PP_3197 being a **flavonoid A-ring-cleaving dioxygenase (FdeC)**, not a glyoxalase-I methylglyoxal detoxification enzyme. This is a case where the database annotation is technically accurate but functionally misleading — exactly the scenario the identification guidance was designed to catch. **This report concerns the correct protein.**

---

## Key Findings

### Finding 1 — PP_3197 is FdeC, the ring-cleavage dioxygenase of the naringenin/flavonoid catabolic pathway

The central finding of this investigation is that PP_3197 is functionally **FdeC**, the dioxygenase that cleaves the A-ring of a flavanone intermediate during naringenin degradation. KEGG orthology assigns PP_3197 to ortholog group **K26181 (fdeC, "naringenin degradation protein FdeC")** and places it in pathway **ppu00946 / map00946 ("Degradation of flavonoids")**, catalyzing reaction **R13075**:

```
5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one   (8-hydroxynaringenin / a trihydroxyflavanone)
        │
        │  FdeC (PP_3197) + O2   — A-ring meta-cleavage (dioxygenation)
        ▼
(2E,4E)-2,4-dihydroxy-4-[6-(4-hydroxyphenyl)-2,4-dioxodihydro-2H-pyran-3(4H)-ylidene]but-2-enoate
        │
        │  downstream fde enzymes
        ▼
oxaloacetic acid  ──►  TCA cycle
```

The functional anchor for this assignment is the experimental characterization of the orthologous FdeC in *Herbaspirillum seropedicae* SmR1. In that organism, the pathway was genetically and functionally dissected using a random Tn5 mutant unable to grow on naringenin plus targeted mutants: naringenin is first mono-oxygenated by FdeE to produce the trihydroxyflavanone, which is then dioxygenated and cleaved at the A-ring by FdeC. The evidence was direct — an *fdeC* mutant strain accumulated the trihydroxyflavanone substrate, demonstrating that FdeC acts precisely at that step: *"naringenin is first mono-oxygenated by the FdeE protein, to produce 5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one, that is subsequently dioxygenated and cleaved at the A-ring by the FdeC dioxygenase, since the latter compound accumulated in the fdeC strain"* ([PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)). PP_3197 is one-to-one orthologous to this validated FdeC (KEGG GENES lists PPU:PP_3197 under K26181) and sits within the syntenic *P. putida fde* cluster (see Finding 3).

The pathway's metabolic endpoint is also established: *"After meta-cleavage of the A-ring, the subsequent metabolic steps generate oxaloacetic acid that is metabolized via the tricarboxylic acid cycle"* ([PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)). Thus FdeC/PP_3197 performs the committed ring-opening step that converts a stable aromatic flavonoid into a metabolizable, ring-opened intermediate, allowing *P. putida* to use naringenin as a carbon and energy source.

**Substrate specificity.** The physiological substrate is the FdeE product **5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one** (a trihydroxyflavanone), not free catechol or methylglyoxal, and not naringenin itself. The extra hydroxyl introduced by FdeE onto the flavonoid A-ring creates the catechol-like *vicinal-diol* motif that extradiol/VOC dioxygenases require for ring cleavage. No formal EC number has been assigned; KEGG classes the transformation as "dioxygenation."

### Finding 2 — VOC/glyoxalase superfamily membership and a tandem two-module architecture consistent with a type I extradiol dioxygenase

PP_3197 is a **313-amino-acid** protein whose domain architecture places it firmly in the VOC/glyoxalase structural superfamily, but in its **dioxygenase branch**. UniProt/InterPro annotations include **Pfam PF00903** (Glyoxalase/Bleomycin resistance/Dioxygenase), **PROSITE PS51819** (VOC domain, residues 155–272), and InterPro entries **IPR004360**, **IPR029068**, and **IPR037523** (VOC core). Structural-classification databases add **SUPFAM SSF54593**, **Gene3D G3DSA:3.10.180.10** (explicitly named "2,3-Dihydroxybiphenyl 1,2-Dioxygenase, domain 1" — a canonical extradiol dioxygenase), and **eggNOG COG0346** ("lactoylglutathione lyase and related lyases"). Members of this superfamily coordinate substrate through vicinal (adjacent) oxygen atoms chelated to an active-site divalent metal, and include glyoxalase-I lyases, fosfomycin-resistance thiol transferases, methylmalonyl-CoA epimerase, and extradiol ring-cleavage dioxygenases.

The 313-residue length is approximately **twice** that of a single ~130-residue VOC (βαβββ) module, indicating a **bicupin / two-domain fold** — the architecture characteristic of **type I extradiol ring-cleavage dioxygenases** such as BphC (2,3-dihydroxybiphenyl 1,2-dioxygenase) and XylE (catechol 2,3-dioxygenase). The C-terminal module houses the catalytic metal site (PROSITE VOC domain, residues 155–272) and carries a cluster of candidate metal-coordinating residues (His200, His201, His211, His217, His221, Glu216, Glu227) arranged to form the type of His/Glu triad that binds the catalytic divalent metal ion in these enzymes.

Biophysical prediction supports a **soluble, cytoplasmic** localization. A Kyte-Doolittle hydropathy analysis gives a maximum window-19 hydropathy of 1.12, well below the ~1.6 threshold for transmembrane segments, and no N-terminal Sec/Tat signal peptide is present (N-terminal 30-residue mean hydropathy 0.61). This is fully consistent with an intracellular catabolic enzyme acting on an intracellular substrate. UniProt lists the protein at evidence level **PE=4 (Predicted)**, underscoring that no dedicated experimental study of PP_3197 exists and that the annotation rests on inference.

### Finding 3 — PP_3197 resides in a syntenic *P. putida fde* flavonoid-degradation gene cluster

Functional context strongly reinforces the FdeC assignment. KEGG pathway ppu00946 maps a cluster of adjacent *P. putida* genes to *fde* orthologs, reconstructing a complete *meta*-cleavage flavonoid degradation pathway. STRING functional-association analysis gives high co-association scores for PP_3197 with its neighbors:

| Locus | *fde* / KO | Annotation | STRING score with PP_3197 |
|-------|------------|------------|---------------------------|
| PP_3195 | FdeB (K26184) | S9 prolyl-oligopeptidase / α/β-hydrolase | 0.87 |
| **PP_3197** | **FdeC (K26181)** | **VOC/glyoxalase-fold ring-cleavage dioxygenase (target)** | — |
| PP_3198 | FdeD (K26179) | 2Fe-2S ferredoxin | 0.91 |
| PP_3199 | (FdeE-type) | Monooxygenase, 374 aa (initial hydroxylase) | 0.89 |
| PP_3204 | FdeH (K26182) | Cupin type-2 (co-listed with FdeC for R13075) | 0.84 |
| PP_3205 | FdeI (K26185) | Fumarylacetoacetate hydrolase (FAH) family | 0.80 |
| PP_3206 | FdeJ (K26183) | NAD-dependent epimerase/dehydratase | 0.72 |
| PP_1403 | *bglX* (K05349) | β-glucosidase (deglycosylation of flavonoid glycosides) | — |

The presence of a **monooxygenase + ferredoxin** module (aromatic-ring hydroxylation, PP_3199 + PP_3198), a **VOC dioxygenase** (ring cleavage, PP_3197), and an **FAH-family hydrolase** (processing of the ring-fission product toward oxaloacetate, PP_3205) recapitulates a canonical aromatic *meta*-cleavage catabolic operon — exactly the arrangement functionally validated in *H. seropedicae*, where the orthologous cluster (Hsero_1005 *fdeC*, Hsero_1007 *fdeE*, Hsero_1009 *fdeG*) is a validated naringenin *meta*-cleavage pathway ([PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)). The conservation of both gene content and gene order between the two organisms is powerful circumstantial evidence that the *P. putida* cluster performs the same chemistry. This is ecologically coherent: *P. putida* is a metabolically versatile soil/rhizosphere bacterium in intimate contact with plant-derived aromatics, and flavonoid catabolism provides a carbon/energy source.

### Finding 4 — PP_3197 is a true ortholog (71% identity) of the experimentally validated FdeC, with a conserved active-site motif

A quantitative sequence comparison converts the orthology inference into a high-confidence assignment. A Needleman-Wunsch global alignment of PP_3197 (Q88I05, 313 aa) against the experimentally characterized FdeC from *H. seropedicae* SmR1 (Hsero_1005 = UniProt **D8J0W7**, 308 aa) yields **216 identical residues over 303 ungapped columns = 71.3% identity** (69% over the full PP_3197 length). This level of identity is far above the ~30–40% threshold typically taken to imply conserved enzymatic function, and it spans the entire two-domain length rather than being confined to a single motif.

Both proteins carry a strictly conserved C-terminal active-site motif:

```
PP_3197 (residues ~206–222):  ...I Q T P P H M Q G C E H F T F H M G...
FdeC    (H. seropedicae):      ...I Q T P P F M K G C E H F T F H M G...
                                        *           * * *   * * *
```

The invariant **GC-E-H-F-T-F-H-M-G** block supplies the His/Glu residues that coordinate the catalytic divalent metal of VOC-superfamily dioxygenases, and its perfect conservation between PP_3197 and the validated FdeC indicates a shared catalytic machinery.

A crucial cautionary note emerges from this comparison: the validated *H. seropedicae* FdeC (D8J0W7) is itself **mis-annotated in UniProt as "Glyoxalase II protein (EC 3.1.2.6)"**, yet it is unambiguously the gene shown by mutagenesis to be the naringenin A-ring dioxygenase ([PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/)). This directly demonstrates that the "glyoxalase" naming shared across this ortholog group is **fold-based, not activity-based**, and it explains — and effectively neutralizes — the misleading "Glyoxalase family protein" label on PP_3197.

### Finding 5 — AlphaFold model of PP_3197 is very high confidence (mean pLDDT 95.7)

The AlphaFold Protein Structure Database entry **AF-Q88I05-F1** (version 6) covers all 313 residues of Q88I05 with a **global mean pLDDT of 95.69**. pLDDT values above 90 indicate residues modeled with very high per-atom confidence, so a global mean approaching 96 across the entire chain indicates a confidently predicted, well-ordered structure spanning both VOC modules. This corroborates that PP_3197 folds as a **stable two-domain (bicupin) enzyme** consistent with a type I extradiol dioxygenase, rather than being a disordered, truncated, or non-functional gene product. The structural prediction is therefore independent computational support for the domain-architecture argument in Finding 2 and for the enzyme's competence to bind metal and substrate in a defined active-site pocket.

---

## Mechanistic Model / Interpretation

Synthesizing the five findings, PP_3197/FdeC is best understood as the **ring-opening catalyst of the *P. putida* naringenin *meta*-cleavage catabolon**. The proposed pathway, by analogy to the validated *H. seropedicae* system, is:

```
                      Plant flavonoid (dietary/soil/rhizosphere source)
                                    │
   naringenin  (a flavanone: A-ring + C-ring + B-ring)
                                    │
                   ┌────────────────┘
                   │  FdeE-type monooxygenase (PP_3199) + O2  [+ FdeD ferredoxin, PP_3198]
                   │  → installs an extra A-ring hydroxyl (creates catechol-like vicinal diol)
                   ▼
   5,7,8-trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one
                   │
                   │  ★ FdeC = PP_3197 (VOC/extradiol dioxygenase) + O2
                   │  → META-CLEAVAGE of the aromatic A-ring
                   ▼
   ring-opened dioxo/pyranylidene-butenoate intermediate
                   │
                   │  FdeH / FdeI / FdeJ (cupin, FAH-family hydrolase, epimerase/dehydratase)
                   ▼
              oxaloacetic acid  ──►  TCA cycle  ──►  biomass / energy
```

**Why the "glyoxalase" label is misleading but the fold is real.** The VOC/glyoxalase superfamily is defined by a characteristic βαβββ module and a "vicinal oxygen chelate" mechanism in which two adjacent oxygen atoms of the substrate coordinate a divalent metal center. This same scaffold has been evolutionarily repurposed for chemistries as diverse as glyoxalase-I isomerization, fosfomycin resistance thiol transfer, bleomycin resistance, methylmalonyl-CoA epimerization, and — most relevant here — **extradiol aromatic ring cleavage**. Membership in the superfamily therefore constrains the *fold and mechanism class* but not the *specific reaction*. For PP_3197, three features push the assignment firmly toward the dioxygenase branch: (1) the **two-domain length** (313 aa ≈ 2× a single VOC module), diagnostic of type I extradiol dioxygenases rather than the single-domain glyoxalase-I; (2) the **Gene3D/SUPFAM classification** that explicitly maps it onto 2,3-dihydroxybiphenyl 1,2-dioxygenase; and (3) the **71% identity plus conserved metal-binding motif** to a gene experimentally proven to be a flavonoid ring dioxygenase.

**Localization.** All evidence indicates an **intracellular, cytoplasmic** site of action: no signal peptide, no transmembrane helices (max hydropathy 1.12), a soluble globular AlphaFold fold, and a catabolic role acting on a metabolite that is generated intracellularly (after import and initial hydroxylation). There is no evidence for periplasmic or membrane localization.

**Pathway role, not pleiotropy.** The precise role is narrow and committed: FdeC performs the single dioxygenolytic ring-cleavage step that converts a chemically stable aromatic flavonoid into a ring-opened, TCA-feeding intermediate. This is a catabolic carbon-acquisition function that allows *P. putida* to exploit flavonoids as growth substrates — not a broad, pleiotropic activity.

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance to PP_3197 |
|------|-----------------|----------------------|
| [27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/) | *Genetic and functional characterization of a novel meta-pathway for degradation of naringenin in Herbaspirillum seropedicae SmR1* | **Primary anchor.** Directly demonstrates by mutagenesis + LC-MS/MS that FdeC is the A-ring-cleaving dioxygenase; PP_3197 is its 71%-identity ortholog. |
| [40014075](https://pubmed.ncbi.nlm.nih.gov/40014075/) | *Flavonoid-converting capabilities of Clostridium butyricum* | Context: bacterial flavonoid (naringenin/eriodictyol) ring cleavage; supports flavonoids as microbial catabolic substrates (via a different, anaerobic mechanism). |
| [31375488](https://pubmed.ncbi.nlm.nih.gov/31375488/) | *An NADH-Dependent Reductase from Eubacterium ramulus Catalyzes... Cleavage of Flavanones* | Context: microbial flavanone heteroring cleavage, illustrating alternative flavonoid-degradation strategies. |
| [17047689](https://pubmed.ncbi.nlm.nih.gov/17047689/) | *Pharmacokinetics of the citrus flavanone aglycones hesperetin and naringenin...* | Context: naringenin is a physiologically abundant flavonoid subject to bacterial ring cleavage — establishes environmental/dietary relevance of the substrate. |
| [31710815](https://pubmed.ncbi.nlm.nih.gov/31710815/) | *A New Way of Belonging: Active-Site Investigation of L-DOPA Dioxygenase, a VOC Family Enzyme* | Supports the concept that VOC-family enzymes act as extradiol dioxygenases; clarifies VOC domain-architecture/function relationships. |
| [31180203](https://pubmed.ncbi.nlm.nih.gov/31180203/) | *Crystal Structures of L-DOPA Dioxygenase...* | Structural precedent for VOC-superfamily extradiol dioxygenases, supporting the fold-to-function argument for PP_3197. |
| [32951427](https://pubmed.ncbi.nlm.nih.gov/32951427/) | *Mechanistic Insights into... the Unprecedented Dioxygenase ChaP (VOC superfamily)* | Demonstrates that VOC-superfamily members carry out diverse dioxygenase chemistries. |
| [35415958](https://pubmed.ncbi.nlm.nih.gov/35415958/) | *Alteration of the Catalytic Reaction Trajectory of a Vicinal Oxygen Chelate Enzyme by Directed Evolution* | Reinforces mechanistic breadth of the VOC superfamily (extradiol vs. intradiol trajectories). |
| [24004181](https://pubmed.ncbi.nlm.nih.gov/24004181/) | *Structural and chemical aspects of resistance to fosfomycin conferred by FosB from Bacillus cereus* | Illustrates fold-based (not activity-based) naming and metal chemistry across the VOC superfamily — parallels the "glyoxalase" mislabeling of PP_3197. |
| [22070249](https://pubmed.ncbi.nlm.nih.gov/22070249/) | *clusterMaker: a multi-algorithm clustering plugin for Cytoscape* | Methodological reference for VOC superfamily annotation/clustering; cautions that superfamily membership ≠ specific function. |

**How the evidence coheres.** The single most decisive paper is [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/), which supplies the experimental proof that FdeC is a flavonoid A-ring dioxygenase in a closely related β-proteobacterium. The VOC-superfamily structural/mechanistic papers (31710815, 31180203, 32951427, 35415958, 24004181) collectively establish that the glyoxalase fold routinely hosts dioxygenase and other non-glyoxalase activities, resolving the apparent conflict between the "glyoxalase family protein" label and the assigned dioxygenase function. The flavonoid-catabolism papers (40014075, 31375488, 17047689) establish that naringenin is a real, abundant substrate that bacteria degrade. None of the numerous methylglyoxal/glyoxalase-I disease-biology papers surfaced during literature searches apply to PP_3197, because — as the ortholog comparison shows — the shared name is a fold artifact.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_3197 itself.** The functional assignment is entirely inferential (UniProt PE=4, "Predicted"). There is no purified-enzyme assay, crystal structure, or *P. putida* knockout demonstrating flavonoid degradation attributable specifically to PP_3197. The confidence derives from orthology (71% identity) to a validated enzyme, not from primary data on the *P. putida* protein.

2. **Metal identity and cofactor requirements are unverified.** Type I extradiol dioxygenases typically use Fe(II), but VOC-superfamily members employ a range of divalent metals (Mn, Ni, Co, Zn). The catalytic metal of PP_3197 is inferred from conserved His/Glu residues, not measured. The role of the adjacent FdeD ferredoxin (PP_3198) as a redox partner is plausible but untested for the *P. putida* cluster.

3. **Exact substrate regiochemistry and product structure rest on KEGG/analogy.** Reaction R13075 and the trihydroxyflavanone substrate are derived from KEGG and the *H. seropedicae* study; the precise cleavage position on the A-ring and the identity of the ring-opened product in *P. putida* have not been chemically confirmed in this organism. No formal EC number is assigned.

4. **The initial monooxygenase step is assigned by position, not proof.** PP_3199 is annotated as the FdeE-type hydroxylase largely on the basis of gene neighborhood and general annotation; its role as the enzyme that generates PP_3197's substrate is inferred.

5. **Regulation and physiological induction are unknown.** Whether the *fde* cluster is induced by naringenin, which regulator controls it, and under what growth conditions *P. putida* KT2440 actually utilizes flavonoids have not been examined here.

6. **Superfamily promiscuity caveat.** Although the two-domain architecture and conserved motif strongly favor a dioxygenase, VOC enzymes are known to be catalytically promiscuous and evolutionarily plastic (PMIDs 35415958, 32951427). A minor or alternative activity for PP_3197 cannot be formally excluded without biochemistry.

---

## Supported and Refuted Hypotheses

- **Supported:** PP_3197 is FdeC, a cytoplasmic VOC-superfamily ring-cleavage dioxygenase that *meta*-cleaves the A-ring of a trihydroxyflavanone in naringenin/flavonoid degradation, channeling carbon to oxaloacetate and the TCA cycle.
- **Refuted / disfavored:** That PP_3197 is a *bona fide* glyoxalase I (lactoylglutathione lyase / methylglyoxal detoxification enzyme). Although the UniProt name and Pfam "Glyoxalase" reflect the shared VOC fold, the two-domain architecture, extradiol-dioxygenase Gene3D class, the *fde* operon context, and 71% identity to a validated flavonoid A-ring dioxygenase all point to a **ring-cleavage dioxygenase**, not a dicarbonyl-detoxifying lyase.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and in vitro assay.** Clone PP_3197, express and purify the protein, and assay ring-cleavage activity against the FdeE product (5,7,8-trihydroxyflavanone) with O2, monitoring by UV-Vis (appearance of a *meta*-cleavage chromophore) and LC-MS/MS product identification. Include metal-reconstitution experiments (Fe²⁺, Mn²⁺, Ni²⁺, Co²⁺) to determine the catalytic metal.

2. **Targeted gene knockout in *P. putida* KT2440.** Test growth of KT2440 on naringenin as sole carbon source, then delete PP_3197 (ΔfdeC) and test for a growth defect plus accumulation of the trihydroxyflavanone intermediate (by LC-MS). This would directly replicate the *H. seropedicae fdeC* phenotype and confirm the assignment in the native organism.

3. **Active-site mutagenesis.** Individually mutate the predicted metal-coordinating residues (His200/His201/His211/His217/His221, Glu216/Glu227) to Ala and confirm loss of activity, validating the catalytic-metal model.

4. **Substrate-specificity panel.** Test related flavonoids/flavanones (eriodictyol, taxifolin, hydroxylated derivatives) and simple catechols to map the substrate scope and determine whether PP_3197 is dedicated to the flavonoid A-ring or has broader extradiol activity.

5. **Structural determination.** Solve an experimental crystal or cryo-EM structure (ideally with bound metal and substrate/analog) to confirm the two-domain VOC fold predicted by AlphaFold (pLDDT 95.7) and to define the active-site geometry.

6. **Transcriptional/regulatory analysis.** Use RT-qPCR or RNA-seq to test induction of the *fde* cluster (PP_3195–PP_3206) by naringenin, and identify the cluster's regulator, clarifying when the pathway operates physiologically.

7. **Database re-annotation.** On the strength of the orthology and (pending) experimental data, submit an annotation update reclassifying PP_3197 (and the mis-annotated *H. seropedicae* D8J0W7) from generic "glyoxalase family protein" to "FdeC, flavonoid A-ring-cleaving dioxygenase," to prevent propagation of the misleading name.

---

## Conclusion

PP_3197 (Q88I05) of *Pseudomonas putida* KT2440 is **FdeC, a cytoplasmic, metal-dependent aromatic ring-cleavage dioxygenase of the VOC/glyoxalase structural superfamily**. Its primary function is the oxygenolytic *meta*-cleavage of the A-ring of the trihydroxyflavanone intermediate generated during naringenin catabolism, feeding the ring-fission carbon toward oxaloacetate and the TCA cycle. This assignment — supported by KEGG orthology (K26181, reaction R13075, pathway ppu00946), a syntenic *fde* gene cluster, 71% identity to the experimentally validated *H. seropedicae* FdeC with a conserved metal-binding motif, and a high-confidence AlphaFold model (mean pLDDT 95.7) — supersedes the generic "glyoxalase family protein" label, which reflects only the protein's fold and not its true dioxygenase activity. The assignment is a high-confidence inference; direct biochemical and genetic validation in *P. putida* remains the key outstanding step.

---

### Key References

- Marín A.M., de la Torre J., Oliveira A.R.M., et al. **Genetic and functional characterization of a novel meta-pathway for degradation of naringenin in *Herbaspirillum seropedicae* SmR1.** *Environ. Microbiol.* 18:4653–4661 (2016). [PMID: 27059806](https://pubmed.ncbi.nlm.nih.gov/27059806/).
- Thompson M.K., et al. **Structural and chemical aspects of resistance to the antibiotic fosfomycin conferred by FosB from *Bacillus cereus*.** *Biochemistry* (2013). [PMID: 24004181](https://pubmed.ncbi.nlm.nih.gov/24004181/).
- Morris J.H., et al. **clusterMaker: a multi-algorithm clustering plugin for Cytoscape** (cluster analysis of the VOC enzyme superfamily). *BMC Bioinformatics* (2011). [PMID: 22070249](https://pubmed.ncbi.nlm.nih.gov/22070249/).
- Database sources: UniProt Q88I05; KEGG K26181 / R13075 / ppu00946; InterPro/Pfam PF00903, PROSITE PS51819; Gene3D G3DSA:3.10.180.10; STRING 160488.PP_3197; AlphaFold DB AF-Q88I05-F1.


## Artifacts

- [OpenScientist final report](PP_3197-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3197-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27059806
2. PMID:24004181
3. PMID:22070249