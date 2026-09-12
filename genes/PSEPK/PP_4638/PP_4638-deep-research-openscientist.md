---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:53:19.768713'
end_time: '2026-07-20T19:25:45.110557'
duration_seconds: 1945.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4638
  gene_symbol: PP_4638
  uniprot_accession: Q88E30
  protein_description: 'RecName: Full=Methylenetetrahydrofolate reductase {ECO:0000256|RuleBase:RU003862};'
  gene_info: OrderedLocusNames=PP_4638 {ECO:0000313|EMBL:AAN70211.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the methylenetetrahydrofolate reductase family.
  protein_domains: DUF5981. (IPR022026); FAD-linked_oxidoreductase-like. (IPR029041);
    Mehydrof_redctse-like. (IPR003171); DUF5981 (PF12225); MTHFR (PF02219)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4638-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4638-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88E30
- **Protein Description:** RecName: Full=Methylenetetrahydrofolate reductase {ECO:0000256|RuleBase:RU003862};
- **Gene Information:** OrderedLocusNames=PP_4638 {ECO:0000313|EMBL:AAN70211.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the methylenetetrahydrofolate reductase family.
- **Key Domains:** DUF5981. (IPR022026); FAD-linked_oxidoreductase-like. (IPR029041); Mehydrof_redctse-like. (IPR003171); DUF5981 (PF12225); MTHFR (PF02219)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4638" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4638' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4638** (gene ID: PP_4638, UniProt: Q88E30) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_4638 (Q88E30), a Divergent Methylenetetrahydrofolate Reductase of *Pseudomonas putida* KT2440

## Summary

**PP_4638 (UniProt Q88E30) is a methylenetetrahydrofolate reductase (MTHFR; EC 1.5.1.54) of the soil bacterium *Pseudomonas putida* KT2440.** Its physiological function is to catalyze the FAD-dependent, NAD(P)H-linked reduction of 5,10-methylenetetrahydrofolate (5,10-CH₂-THF) to 5-methyltetrahydrofolate (5-methyl-THF). This is the committed, essentially irreversible step of folate one-carbon metabolism that channels one-carbon units toward the biosynthesis of methionine. The 5-methyl-THF produced is the direct methyl donor consumed by methionine synthase to remethylate homocysteine to methionine, which in turn feeds S-adenosylmethionine (SAM) synthesis — the universal methyl donor of the cell. The enzyme carries out its function in the cytoplasm as a soluble protein; it possesses no signal peptide, transmembrane segment, or export signal.

Beyond the core catalytic assignment, this investigation established that PP_4638 is not the organism's *canonical* MTHFR. *P. putida* KT2440 encodes exactly two MTHFR-family proteins, and PP_4638 is the **divergent, larger, two-domain paralog**. The genome's short canonical *metF* is a separate gene (PP_4977, 295 aa), while PP_4638 is a 495-aa protein composed of an N-terminal catalytic (β/α)₈ TIM-barrel fused to a **cysteine-rich C-terminal DUF5981 domain** (Pfam PF12225 / InterPro IPR022026) that is predicted to coordinate a metal or iron–sulfur ([Fe–S]) center. This architecture is reminiscent of non-canonical MTHFRs (the MetVF/Fe–S subfamily) that, in anaerobes, use reduced ferredoxin rather than NAD(P)H as their electron donor — raising the intriguing possibility that PP_4638 employs a distinct electron-transfer chemistry.

**An important caveat frames the entire report:** the functional assignment of PP_4638 rests on database annotation, protein-domain and fold analysis, sequence homology, and genomic-context/interaction-network inference. **No direct enzymatic or genetic characterization of PP_4638 itself has been published.** The gene is a well-defined but experimentally uncharacterized member of a well-understood enzyme family, and the confidence in its assignment derives from the strength of that family and fold conservation rather than from a dedicated study of this protein.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and passed. The evidence confirms that the gene symbol, organism, family, and domains are mutually consistent.

| Attribute | Value | Consistency check |
|-----------|-------|-------------------|
| UniProt accession | Q88E30 | — |
| Locus tag | PP_4638 | Matches EMBL AAN70211.1 |
| Organism | *Pseudomonas putida* KT2440 (taxon 160488) | Confirmed |
| Protein description | Methylenetetrahydrofolate reductase | Matches family assignment |
| Protein family | Methylenetetrahydrofolate reductase family | Confirmed by InterPro IPR003171/PF02219 |
| Catalytic domain | MTHFR (PF02219, cd00537), (β/α)₈ barrel | Confirmed |
| Accessory domain | DUF5981 (PF12225 / IPR022026) | Confirmed, cysteine-rich |
| KEGG ortholog | K00297, MTHFR (NADH) [EC:1.5.1.54] | Confirmed |

A note on the literature landscape: **the vast majority of PubMed hits for "MTHFR" concern the human enzyme and its clinical C677T/A1298C polymorphisms** (adenomyosis, pediatric thrombosis, hypothyroidism, colorectal-cancer chemotherapy response, etc.). These human-disease papers are *not* about PP_4638 and were correctly excluded from the functional inference for the bacterial protein. They are retained in the literature list only because they establish the general biochemistry of the MTHFR reaction (5,10-CH₂-THF → 5-methyl-THF, homocysteine remethylation), which is transferable in its chemistry. The bacterial/mechanistic papers (Thermus MTHFR structure, Clostridium ferredoxin-dependent MTHFR) are the relevant precedents for PP_4638.

---

## Key Findings

### Finding 1 — PP_4638 is a methylenetetrahydrofolate reductase (EC 1.5.1.54)

PP_4638 is assigned as a methylenetetrahydrofolate reductase that reduces 5,10-methylene-THF to 5-methyl-THF. The UniProt entry Q88E30 records the catalytic activity (ARBA00048628) as:

> (6S)-5-methyltetrahydrofolate + NAD⁺ ⇌ (6R)-5,10-methylenetetrahydrofolate + NADH + H⁺  (Rhea:19821; EC 1.5.1.54)

The physiologically relevant direction runs **right-to-left**, i.e., toward the *production* of 5-methyl-THF, consistent with the enzyme's role of feeding methyl groups into methionine biosynthesis. The cofactor is **FAD** (ChEBI:57692), the flavin prosthetic group that mediates hydride transfer between the nicotinamide and folate substrates. KEGG independently assigns the *P. putida* gene `ppu:PP_4638` to ortholog **K00297** ("methylenetetrahydrofolate reductase (NADH) [EC:1.5.1.54]") and maps it to pathway **ppu00670, "One carbon pool by folate."**

Structurally, InterPro places the catalytic domain in IPR003171 / PF02219 / cd00537 (MTHFR), with the classic **(β/α)₈ TIM-barrel fold** (Gene3D 3.20.20.220) belonging to the **FAD-linked oxidoreductase-like superfamily** (SSF51730). All of these annotations converge on a single, coherent enzymatic identity.

**Evidence class:** computational. The assignment comes from automated UniProt RuleBase/ARBA rules plus KEGG ortholog transfer. No direct enzymatic assay of PP_4638 exists.

### Finding 2 — PP_4638 is a divergent two-domain MTHFR paralog, distinct from the canonical *metF* (PP_4977)

A survey of the *P. putida* KT2440 proteome (UniProt taxonomy family query) shows the genome encodes **exactly two MTHFR-family proteins**:

| Protein | Locus | Length | Architecture | Role |
|---------|-------|--------|--------------|------|
| Q88D51 | PP_4977 (*metF*) | 295 aa | Catalytic barrel only | Canonical short MTHFR |
| Q88E30 | PP_4638 | 495 aa | Catalytic barrel + DUF5981 | Divergent two-domain paralog |

PP_4638 is ~200 residues longer than the canonical enzyme because of a **C-terminal DUF5981 domain** (IPR022026 / PF12225, "MTHFR C-terminal"). InterPro describes this domain as "a domain of unknown function, which contains 8 conserved cysteine residues that might form a metal binding site." Direct sequence inspection of PP_4638 confirms a C-terminal cysteine cluster — a **CDTCGRC motif (C392, C395, C398)**, a **CPETC motif (C407, C411)**, and additional cysteines at C420, C428, C435, and C460 — that is entirely absent from the canonical MetF.

Consistent with this distinct architecture, KEGG files PP_4638 not only under one-carbon folate metabolism but *additionally* under pathway ppu00720 ("Other carbon fixation pathways") and under energy-metabolism BRITE categories — filing that the standalone canonical *metF* does not receive. This differential annotation reinforces the interpretation that PP_4638 belongs to a mechanistically distinct MTHFR subclass.

### Finding 3 — PP_4638 functions in cytoplasmic folate one-carbon metabolism, supplying 5-methyl-THF for methionine biosynthesis

Two independent lines of contextual evidence localize PP_4638 firmly within the methionine-biosynthesis module of one-carbon metabolism.

**Genomic neighborhood.** PP_4638 (genome coordinates 5,261,828–5,263,315) lies immediately adjacent to **PP_4637** (complement 5,260,776–5,261,600), which is annotated **K00549 = 5-methyltetrahydropteroyltriglutamate–homocysteine methyltransferase (MetE-type, cobalamin-independent methionine synthase)**. This is precisely the downstream enzyme that *consumes* the 5-methyl-THF produced by MTHFR, transferring its methyl group to homocysteine to make methionine. The physical adjacency of the MTHFR and methionine-synthase genes is a strong functional-coupling signal.

**Interaction network.** STRING v11 lists the high-confidence functional partners of PP_4638 as the complete folate/methionine one-carbon module:

| Partner | Function | STRING score |
|---------|----------|--------------|
| *metH* | Cobalamin-dependent methionine synthase | 0.999 |
| *metF* | Methylenetetrahydrofolate reductase | 0.971 |
| *glyA-I/II* | Serine hydroxymethyltransferase (source of 5,10-CH₂-THF) | 0.934 |
| *folD-I/II* | Methylenetetrahydrofolate dehydrogenase/cyclohydrolase | 0.923 |
| *thyA* | Thymidylate synthase | 0.919 |
| *gcvT/gcvP* | Glycine cleavage system | 0.75–0.91 |
| *metE* | Cobalamin-independent methionine synthase | 0.718 |
| *metK* | SAM synthetase | 0.637 |

The network places PP_4638 at the junction between the folate pool (supplied by *glyA*, *folD*, and the glycine cleavage system) and the methionine/SAM output (*metH*, *metE*, *metK*).

**Localization.** UniProt lists no signal peptide and no subcellular annotation for Q88E30, and the sequence contains no export signal or transmembrane region. Combined with the fact that all characterized MTHFR-family enzymes are soluble cytoplasmic proteins, PP_4638 is confidently assigned to the **cytoplasm**, where the entire one-carbon/methionine module operates.

The clinical review [PMID: 42290938](https://pubmed.ncbi.nlm.nih.gov/42290938/) supports the general pathway context, noting the "central roles in one-carbon metabolism, DNA synthesis, and methylation" of folate/B12-dependent chemistry — the biochemical setting in which MTHFR-produced 5-methyl-THF operates.

### Finding 4 — PP_4638 retains a conserved FAD-binding catalytic barrel, while its Fe–S-like C-terminal domain evokes non-canonical electron donors

A pairwise global (Needleman–Wunsch) alignment of the PP_4638 N-terminal catalytic domain (residues 1–355) against *E. coli* MetF (P0AEZ1, 296 aa) yields **25.3% identity (75/296 residues)**, with a positive match to the CDD active-site model cd00537. This level of identity, together with the conserved active-site signature, indicates the **(β/α)₈ TIM-barrel fold and the FAD/folate-binding architecture are preserved** — i.e., PP_4638's catalytic machinery is genuinely competent.

This inference is anchored on the experimentally solved bacterial MTHFR structure from *Thermus thermophilus* HB8 ([PMID: 21858212](https://pubmed.ncbi.nlm.nih.gov/21858212/)), which showed that "the crystal structure of the holo-subunit was quite similar to the β(8)α(8) barrel of *E. coli* MTHFR" and that there is "one flavin adenine dinucleotide (FAD) prosthetic group bound per dimer." These features — the β₈α₈ barrel and one FAD per dimer — are exactly what PP_4638's InterPro FAD-linked oxidoreductase superfamily membership (SSF51730 / IPR029041) and its UniProt FAD cofactor annotation predict.

The **distinguishing feature** is the C-terminal cysteine-rich DUF5981 domain. In anaerobic bacteria, MTHFRs of the **MetVF / Fe–S subfamily** use reduced **ferredoxin** rather than NAD(P)H as their physiological electron donor. This has been documented for a heterodimeric reduced-ferredoxin-dependent MTHFR in the syngas-fermenting acetogen *Clostridium ljungdahlii* ([PMID: 34643446](https://pubmed.ncbi.nlm.nih.gov/34643446/)) and proposed as a general principle for MetVF-type enzymes in acetogenesis ([PMID: 34255221](https://pubmed.ncbi.nlm.nih.gov/34255221/)). These clades are defined by iron–sulfur/metal-binding modules **analogous to PP_4638's cysteine-rich C-terminal domain**. Whether PP_4638 in the aerobe *P. putida* actually uses ferredoxin, NAD(P)H, or another donor is an open — and biochemically testable — question raised by this structural analogy.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent model of PP_4638 as the folate-reducing node that gates one-carbon flux into methionine and SAM.

```
   Serine ─(glyA/SHMT)──►  5,10-CH2-THF   ◄── glycine cleavage (gcvTHP)
                                │
                                │  PP_4638  (MTHFR, EC 1.5.1.54)
                                │  FAD-dependent, NAD(P)H- (or Fd-?) linked
                                │  *** committed, ~irreversible step ***
                                ▼
                          5-methyl-THF
                                │
             ┌──────────────────┴──────────────────┐
             ▼                                      ▼
   MetH (B12-dependent)                   MetE / PP_4637 (B12-independent)
   methionine synthase                    methionine synthase
             │                                      │
             └──────────────────┬───────────────────┘
                                ▼
    Homocysteine  ─────────►  Methionine  ──(metK)──►  SAM
                                                        (universal methyl donor)
```

**Reaction catalyzed.** PP_4638 reduces the N5,N10-methylene bridge of 5,10-CH₂-THF to a methyl group, generating 5-methyl-THF. The chemistry proceeds through the enzyme's bound FAD, which shuttles a hydride from the reduced pyridine nucleotide (or, potentially, from reduced ferredoxin) to the folate substrate. Because 5-methyl-THF is metabolically "committed" — it can only be recovered to the folate pool by methionine synthase — this step exerts strong control over the partitioning of one-carbon units between methyl-group biogenesis and other folate-dependent processes (thymidylate synthesis via *thyA*, purine synthesis, formyl-methionine).

**Substrate specificity.** By family assignment, the substrate is 5,10-methylenetetrahydrofolate and the product is 5-methyltetrahydrofolate; the redox cosubstrate is a reduced nicotinamide (NADH per the KEGG "MTHFR (NADH)" assignment) with FAD as the intermediate carrier. The C-terminal Fe–S-like domain flags the possibility of an alternative or additional electron-input route.

**Localization.** The enzyme is cytoplasmic and soluble; it acts on the freely diffusible folate pool in the cytosol alongside its network partners.

**Pathway placement.** PP_4638 sits at the crossroads of (i) the folate one-carbon pool (KEGG ppu00670) fed by serine hydroxymethyltransferase and the glycine cleavage system, and (ii) the methionine/SAM output arm executed by MetH, MetE (including the adjacent PP_4637), and MetK. Its genomic adjacency to a methionine synthase gene and its near-perfect STRING linkage to *metH* (0.999) make the "supply the methyl donor for methionine biosynthesis" role the single most strongly supported functional statement about this protein.

**Why two MTHFRs?** The coexistence of a canonical short *metF* (PP_4977) and the divergent two-domain PP_4638 suggests functional specialization. One plausible model — consistent with the KEGG filing of PP_4638 under energy-metabolism categories and with the ferredoxin-linked MetVF precedent — is that PP_4638 couples folate reduction to a different redox input than the housekeeping NADH-linked *metF*, perhaps to balance one-carbon flux under particular redox or nutritional conditions. This remains hypothesis rather than established fact.

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance |
|------|-----------------|-----------|
| [21858212](https://pubmed.ncbi.nlm.nih.gov/21858212/) | *Crystal structure of MTHFR from Thermus thermophilus HB8* | Establishes the conserved bacterial β₈α₈ barrel with one FAD per dimer — the catalytic fold retained by PP_4638. **Supports Findings 1 & 4.** |
| [34643446](https://pubmed.ncbi.nlm.nih.gov/34643446/) | *Heterodimeric reduced-ferredoxin-dependent MTHFR from Clostridium ljungdahlii* | Documents a non-canonical, Fe–S/ferredoxin-linked MTHFR — the precedent for PP_4638's cysteine-rich C-terminal domain. **Supports Finding 4; raises the electron-donor hypothesis.** |
| [34255221](https://pubmed.ncbi.nlm.nih.gov/34255221/) | *Is reduced ferredoxin the physiological electron donor for MetVF-type MTHFRs?* | Frames the MetVF/Fe–S MTHFR subfamily hypothesis directly analogous to PP_4638's architecture. **Supports Finding 4.** |
| [26148714](https://pubmed.ncbi.nlm.nih.gov/26148714/) | *Energy conservation & electron bifurcation in C. autoethanogenum* | Context for ferredoxin/NADP-based redox in anaerobic MTHFR chemistry; notes MTHFR activity "only with artificial electron donors." **Background for Finding 4.** |
| [42290938](https://pubmed.ncbi.nlm.nih.gov/42290938/) | *Vitamins in preconception care* (review) | Confirms the central role of folate/B12 one-carbon metabolism and methylation — the pathway context of 5-methyl-THF. **Supports Finding 3.** |

**Human MTHFR clinical literature (context only, not evidence for PP_4638).** A large set of retrieved papers concern the human MTHFR C677T/A1298C polymorphisms and disease — adenomyosis ([PMID: 42445363](https://pubmed.ncbi.nlm.nih.gov/42445363/)), pediatric pneumonia-associated thrombosis ([PMID: 42413940](https://pubmed.ncbi.nlm.nih.gov/42413940/)), Isaac's syndrome ([PMID: 42396931](https://pubmed.ncbi.nlm.nih.gov/42396931/)), bladder-cancer methylation ([PMID: 42373686](https://pubmed.ncbi.nlm.nih.gov/42373686/)), colorectal-cancer chemotherapy response ([PMID: 42345176](https://pubmed.ncbi.nlm.nih.gov/42345176/)), subclinical hypothyroidism in pregnancy ([PMID: 42338702](https://pubmed.ncbi.nlm.nih.gov/42338702/)), and diabetic retinopathy ([PMID: 42290252](https://pubmed.ncbi.nlm.nih.gov/42290252/)). These establish that the MTHFR reaction (5,10-CH₂-THF → 5-methyl-THF) governs homocysteine remethylation and DNA methylation in humans — chemistry that is conserved in the bacterial enzyme — but they do **not** speak to PP_4638 specifically. They were deliberately kept separate from the functional inference to avoid conflating the human ortholog with the *P. putida* protein.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_4638 exists.** Every functional statement in this report is inferred from (i) automated database annotation (UniProt RuleBase/ARBA, KEGG ortholog transfer), (ii) domain/fold analysis, (iii) sequence homology (~25% identity to *E. coli* MetF), and (iv) genomic-context and interaction-network inference (STRING, gene adjacency). There is no published enzyme assay, kinetic measurement, or knockout phenotype for this specific protein.

2. **The physiological electron donor is unknown.** The presence of the cysteine-rich DUF5981/Fe–S-like domain makes it genuinely uncertain whether PP_4638 uses NAD(P)H (as the KEGG "MTHFR (NADH)" label implies) or a ferredoxin-type donor (as its architecture, by analogy to MetVF-type enzymes, might suggest). The two possibilities imply different roles in cellular redox balance.

3. **The functional division of labor between PP_4638 and PP_4977 (metF) is unresolved.** Why *P. putida* maintains two MTHFR paralogs, and under what conditions each is used, has not been experimentally established.

4. **Metal/[Fe–S] cofactor of the C-terminal domain is predicted, not demonstrated.** The eight-cysteine cluster "might form a metal binding site" per InterPro, but no spectroscopic or biochemical evidence confirms a bound metal or [Fe–S] cluster in PP_4638.

5. **Directionality and substrate glutamylation.** The precise in vivo directionality, folate polyglutamate preference, and any regulation (e.g., by SAM, as in mammalian MTHFR) have not been characterized for this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_4638, express it in *E. coli*, purify, and assay MTHFR activity spectrophotometrically (menadione-linked or physiological NAD(P)H/ferredoxin) to confirm catalysis of 5,10-CH₂-THF → 5-methyl-THF and to measure kinetic parameters.

2. **Electron-donor determination.** Directly test NADH vs. NADPH vs. reduced ferredoxin as electron donors to resolve whether PP_4638 is a canonical NAD(P)H-linked or a non-canonical ferredoxin-linked MTHFR. This is the single most informative experiment given the divergent architecture.

3. **Cofactor characterization.** Use UV-visible and EPR spectroscopy plus metal analysis (ICP-MS) on purified protein to test whether the C-terminal cysteine cluster binds an [Fe–S] cluster or other metal, and confirm FAD stoichiometry.

4. **Genetic phenotyping.** Construct single (ΔPP_4638, ΔPP_4977) and double knockouts and assay methionine auxotrophy / growth on minimal medium ± methionine to establish whether PP_4638 is required for methionine biosynthesis and how it partitions function with the canonical *metF*.

5. **Structural biology.** Determine the crystal or cryo-EM structure of PP_4638 to visualize the fusion of the catalytic barrel with the DUF5981 domain and to define the putative metal site — comparing against the *Thermus* MTHFR ([PMID: 21858212](https://pubmed.ncbi.nlm.nih.gov/21858212/)) and the *Clostridium* ferredoxin-dependent enzyme ([PMID: 34643446](https://pubmed.ncbi.nlm.nih.gov/34643446/)).

6. **Conditional expression profiling.** Measure PP_4638 vs. PP_4977 transcript/protein levels across growth conditions (aerobic/microaerobic, methionine-replete/-limited, varying carbon sources) to reveal the physiological niche of the divergent paralog.

---

*Prepared from a 3-iteration autonomous investigation: 4 confirmed findings, 12 papers reviewed. The functional assignment is high-confidence at the family/fold level but awaits direct experimental validation of PP_4638 specifically.*


## Artifacts

- [OpenScientist final report](PP_4638-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4638-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:42290938
2. PMID:21858212
3. PMID:34643446
4. PMID:34255221
5. PMID:42445363
6. PMID:42413940
7. PMID:42396931
8. PMID:42373686
9. PMID:42345176
10. PMID:42338702
11. PMID:42290252