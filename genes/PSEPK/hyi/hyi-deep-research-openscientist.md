---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T17:12:03.393661'
end_time: '2026-07-15T17:53:15.682877'
duration_seconds: 2472.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hyi
  gene_symbol: hyi
  uniprot_accession: Q88F02
  protein_description: 'SubName: Full=Hydroxypyruvate isomerase {ECO:0000313|EMBL:AAN69878.1};
    EC=5.3.1.22 {ECO:0000313|EMBL:AAN69878.1};'
  gene_info: Name=hyi {ECO:0000313|EMBL:AAN69878.1}; OrderedLocusNames=PP_4298 {ECO:0000313|EMBL:AAN69878.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the hyi family. .
  protein_domains: HPT_OtnI_isomerases. (IPR053398); Hydroxypyruvate_isomerase. (IPR017643);
    HyI-like. (IPR026040); Sugar_Epim/Isomerase. (IPR050417); Xyl_isomerase-like_sf.
    (IPR036237)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hyi-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hyi-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F02
- **Protein Description:** SubName: Full=Hydroxypyruvate isomerase {ECO:0000313|EMBL:AAN69878.1}; EC=5.3.1.22 {ECO:0000313|EMBL:AAN69878.1};
- **Gene Information:** Name=hyi {ECO:0000313|EMBL:AAN69878.1}; OrderedLocusNames=PP_4298 {ECO:0000313|EMBL:AAN69878.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the hyi family. .
- **Key Domains:** HPT_OtnI_isomerases. (IPR053398); Hydroxypyruvate_isomerase. (IPR017643); HyI-like. (IPR026040); Sugar_Epim/Isomerase. (IPR050417); Xyl_isomerase-like_sf. (IPR036237)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hyi" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hyi' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hyi** (gene ID: hyi, UniProt: Q88F02) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hyi* (PP_4298, UniProt Q88F02) in *Pseudomonas putida* KT2440

## Gene/Protein Identity (verified)

- **UniProt:** Q88F02 (Q88F02_PSEPK), 260 aa, ~29 kDa
- **Gene:** *hyi*; OrderedLocusName **PP_4298**; GenBank AAN69878
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950)
- **Annotated function:** Hydroxypyruvate isomerase, **EC 5.3.1.22** (KEGG ortholog **K01816**)
- **Family/fold:** *hyi* family; xylose-isomerase-like (β/α)₈ TIM-barrel (InterPro IPR017643 Hydroxypyruvate_isomerase, IPR026040 HyI-like, IPR036237 Xyl_isomerase-like_sf, IPR050417 Sugar_Epim/Isomerase; Pfam PF01261; PIRSF006241; TIGR03234 "OH-pyruv-isom"; eggNOG COG3622)

**Identity check passed.** The gene symbol *hyi*, the EC number, the KEGG ortholog, the protein family/domains, and the genomic context are all mutually consistent for hydroxypyruvate isomerase in *P. putida* KT2440. The characterized reference enzyme (E. coli Hyi, P30147) is a true ortholog (64% identity), not a same-symbol gene from an unrelated family. There is **no gene-identity ambiguity** for this target. The one important caveat, discussed throughout, is that the specific activity has been proven only for the ortholog — the P. putida protein itself is annotated at evidence level **PE3 (inferred from homology)**.

---

## Summary

The gene **hyi** (ordered locus **PP_4298**, UniProt **Q88F02**) of *Pseudomonas putida* strain KT2440 encodes **hydroxypyruvate isomerase (EC 5.3.1.22)**, a cytoplasmic, cofactor-independent enzyme that catalyzes the reversible interconversion of **hydroxypyruvate** and **tartronate semialdehyde (2-hydroxy-3-oxopropanoate)**. The protein is a ~29 kDa, 260-residue soluble enzyme adopting a **(β/α)₈ TIM-barrel fold of the xylose-isomerase-like superfamily**, and it uses two active-site glutamate residues (**Glu143 and Glu240**) as a proton-shuttle to carry out an aldose–ketose isomerization without any metal or nucleotide cofactor. This assignment is a high-confidence homology-based inference: PP_4298 shares **64.1% amino-acid identity** with the biochemically characterized *Escherichia coli* ortholog Hyi (P30147), which was purified and directly shown to "exclusively" catalyze this isomerization.

The biological role of *hyi* is defined by its genomic context. PP_4298 is the **single-copy** hydroxypyruvate isomerase in the KT2440 genome and sits within a compact, entirely same-strand (forward) gene cluster — **gcl (PP_4297) → hyi (PP_4298) → glxR (PP_4299) → glxK (PP_4300)** — that encodes the complete **glycerate pathway** of glyoxylate assimilation. In this pathway, two molecules of glyoxylate are condensed by glyoxylate carboligase (Gcl) into tartronate semialdehyde, which is reduced by tartronate semialdehyde reductase (GlxR) to D-glycerate and then phosphorylated by glycerate 2-kinase (GlxK) to 2-phosphoglycerate, an intermediate of central carbon metabolism. Hyi acts at/near the tartronate-semialdehyde branch point, providing an isomerase activity that links the glyoxylate-derived C3 pool to the hydroxypyruvate pool. The glyoxylate substrate of this pathway is generated in *P. putida* from multiple upstream sources, including the oxidation of ethylene glycol and glycolate, and the catabolism of purines via uric acid and allantoin.

Four independent evidence layers converge on the hydroxypyruvate isomerase assignment: **biochemical** (the proven E. coli ortholog), **evolutionary/sequence** (64% identity, conserved catalytic glutamates, single-copy gene), **genomic** (embedding in the glycerate operon), and **structural** (a very high-confidence AlphaFold TIM-barrel model with a two-glutamate, arginine-anchored pocket sized for a C3 acid). The main knowledge gap is that this activity has **not been directly assayed for the P. putida protein itself**, and the enclosing superfamily is functionally promiscuous. Nevertheless, the combination of high identity to a proven enzyme and the glycerate-operon context makes hydroxypyruvate isomerase by far the best-supported annotation.

---

## Key Findings

### Finding 1 — *hyi* encodes hydroxypyruvate isomerase (EC 5.3.1.22)

PP_4298 is annotated as **hydroxypyruvate isomerase (EC 5.3.1.22)**, an enzyme that catalyzes the reversible isomerization between **hydroxypyruvate** (a 3-carbon keto-acid) and **tartronate semialdehyde** (its aldehyde isomer). The gene is assigned to KEGG ortholog **K01816** and to the PIRSF006241 / TIGR03234 (OH-pyruv-isom) hydroxypyruvate isomerase family.

The biochemical foundation for this assignment comes from the *E. coli* ortholog. Ashiuchi & Misono purified the product of the *E. coli hyi* gene (orf b0508, also called *gip*) and showed that "**It exclusively catalyzed the isomerization between hydroxypyruvate and tartronate semialdehyde. The apparent K(m) value for hydroxypyruvate was 12.5 mM**" ([PMID: 10561547](https://pubmed.ncbi.nlm.nih.gov/10561547/)). The enzyme required **no cofactor**, and the same study established its quaternary structure: "**The enzyme had a molecular mass of 58 kDa and was composed of two identical subunits**" — i.e., a homodimer of ~29 kDa subunits ([PMID: 10561547](https://pubmed.ncbi.nlm.nih.gov/10561547/)). Because the P. putida protein is 260 residues (~29 kDa) and highly identical to this enzyme, it is inferred to be a homodimeric, cofactor-free hydroxypyruvate isomerase with the same substrate specificity.

### Finding 2 — Sequence homology: 64% identity to the characterized E. coli enzyme; catalytic residues Glu143/Glu240

A global Needleman–Wunsch pairwise alignment of PP_4298 (Q88F02, 260 aa) against the biochemically characterized *E. coli* Hyi (UniProt P30147, *hyi/gip/*b0508, 258 aa) gives **157/245 = 64.1% amino-acid identity** over the aligned region. This is far above the ~40% threshold generally regarded as sufficient for confident intra-family functional transfer, so the specific reaction and substrate specificity established for the E. coli enzyme ([PMID: 10561547](https://pubmed.ncbi.nlm.nih.gov/10561547/)) can be transferred to PP_4298 with high confidence.

The two UniProt-annotated proton donor/acceptor residues in PP_4298 are **Glu143 and Glu240** (both glutamate; sequence contexts RLVME**143**MINTR and WVGAE**240**YKPLT), and both align to conserved glutamate positions in the E. coli enzyme. This corrects an earlier note in the investigation that had mislabeled these residues as histidines. A pair of glutamate carboxylates acting as a general acid/base proton shuttle is the expected catalytic machinery for a cofactor-free aldose–ketose isomerization.

### Finding 3 — *hyi* is the single-copy hydroxypyruvate isomerase in a tightly linked glycerate operon

KEGG ortholog mapping for K01816 in *P. putida* KT2440 returns **exactly one gene: PP_4298** — there is no paralog redundancy. The genomic neighborhood is a compact, entirely same-strand (forward) gene cluster encoding the complete glyoxylate-assimilating glycerate pathway:

| Locus | Gene | Coordinates (bp) | Intergenic gap | Function | EC / KO |
|-------|------|------------------|----------------|----------|---------|
| PP_4295 | — | upstream | — | TetR/AcrR-family transcriptional regulator | K09017 |
| PP_4297 | *gcl* | 4,886,942–4,888,717 | — | Glyoxylate carboligase (2 glyoxylate → tartronate semialdehyde + CO₂) | 4.1.1.47 / K01608 |
| **PP_4298** | ***hyi*** | 4,888,772–4,889,554 | 55 bp | **Hydroxypyruvate isomerase** | **5.3.1.22 / K01816** |
| PP_4299 | *glxR* | 4,889,707–4,890,600 | 153 bp | Tartronate semialdehyde reductase (→ D-glycerate) | 1.1.1.60 / K00042 |
| PP_4300 | *glxK* | 4,890,839–4,892,113 | 239 bp | Glycerate 2-kinase (→ 2-phosphoglycerate) | 2.7.1.165 / K11529 |
| PP_4301 | *pykA* | 4,892,110–4,893,525 | contiguous | Pyruvate kinase | 2.7.1.40 / K00873 |
| PP_4302 | — | downstream | — | Urea transporter | — |

The small intergenic gaps (55–239 bp) and shared forward orientation are consistent with a **single operon / transcriptional unit**. This physical clustering is a strong functional-genomic argument: genes co-transcribed in an operon typically act in the same pathway — here, unambiguously the glycerate pathway. The downstream urea transporter (PP_4302) is notable because urea is a purine-degradation byproduct, tying the locus to purine catabolism.

The reaction of the adjacent *gcl* gene defines the shared pathway intermediate: "**Glyoxylate carboligase (Gcl) (EC 4.1.1.47) of Escherichia coli catalyzes the condensation of two molecules of glyoxylate to give tartronic semialdehyde, a key intermediate in glyoxylate catabolism**" ([PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)). Tartronate semialdehyde is precisely the isomer that *hyi* interconverts with hydroxypyruvate, tying the two adjacent enzymes to a common metabolite pool.

### Finding 4 — Physiological context: the glycerate pathway assimilates glyoxylate from multiple upstream sources

The *hyi*-containing pathway feeds glyoxylate — derived from several catabolic routes — into central metabolism. Two independent lines of evidence define these upstream sources:

1. **Ethylene glycol / glycolate oxidation.** In laboratory evolution of KT2440 for growth on ethylene glycol, "**Genomic analysis of these mutants revealed a central role of the transcriptional regulator GclR, which represses the glyoxylate carboligase pathway as part of a larger metabolic context of purine and allantoin metabolism**" ([PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)). Ethylene glycol is oxidized via glycolaldehyde and glycolate to glyoxylate; de-repression of the *gcl* (glycerate) pathway — including *hyi* — is required to assimilate that glyoxylate.

2. **Purine / allantoin catabolism.** In fluorescent pseudomonads, "**Fluorescent pseudomonads catabolize purines via uric acid and allantoin, a pathway whose end-product is glyoxylate**" ([PMID: 41369682](https://pubmed.ncbi.nlm.nih.gov/41369682/)), feeding an allantoin-inducible glyoxylate-utilization pathway.

Thus the glycerate pathway is a **convergent hub** that assimilates glyoxylate from at least two distinct catabolic contexts, channeling it toward 2-phosphoglycerate. The regulatory control by GclR indicates the pathway — and *hyi* within it — is expressed conditionally rather than constitutively.

### Finding 5 — Localization: a cytoplasmic, soluble enzyme

Q88F02 is a **260-aa, ~29 kDa soluble protein with no signal peptide** and no transmembrane segments, indicating a **cytoplasmic** location. This is consistent with a metabolic isomerase acting on soluble small-molecule intermediates of central carbon metabolism, and with its homodimeric E. coli ortholog, which was purified as a soluble cytosolic enzyme. Tellingly, when the *gcl*+*hyi* module has been transplanted into plants for photorespiratory engineering, an added peroxisomal transit peptide was required precisely because the native bacterial enzyme is cytosolic ([PMID: 22104170](https://pubmed.ncbi.nlm.nih.gov/22104170/)). All reactions of the glycerate pathway occur in the cytoplasm.

### Finding 6 — Structural confirmation: a high-confidence TIM-barrel with a two-glutamate, arginine-anchored pocket

The AlphaFold DB model of Q88F02 (**AF-Q88F02-F1, v6**) is of very high quality: **mean pLDDT 97.2**, with 96.5% of residues at pLDDT ≥90 and only 1.2% below 70. The two catalytic residues are modeled with near-maximal confidence (Glu143 at pLDDT 98.9; Glu240 at pLDDT 98.7). The structure adopts the classic **(β/α)₈ TIM-barrel** fold of the xylose-isomerase-like superfamily (Gene3D 3.20.20.150; SCOP SSF51658; Pfam PF01261; eggNOG COG3622).

Crucially, the model places the two glutamate carboxylates **5.7 Å apart on the same (C-terminal) face of the barrel**, flanking a single compact pocket — exactly the geometry expected for a two-base proton shuttle acting on a small substrate. Residues within 8 Å of the catalytic carboxylates include **Arg211, Arg71**, Asn7, Ser9, Glu33, Asn60, Asn103, Gln176, Asp178, His181, His202, Gln204, and Tyr241. The presence of two arginines creates a positively charged anchor well suited to bind the carboxylate group of a **small 3-carbon keto/hydroxy-acid** such as hydroxypyruvate or tartronate semialdehyde. The polar, compact character of the pocket is inconsistent with large or hydrophobic substrates and reinforces the C3-acid specificity. Because the characterized ortholog is cofactor-independent, any metal-ligand-like residues lining the pocket most likely serve substrate binding and general acid/base catalysis rather than metal coordination.

### Finding 7 — Consolidated conclusion: four converging evidence layers

The hydroxypyruvate isomerase assignment for PP_4298 rests on four independent lines of evidence that all point in the same direction:

1. **Biochemical** — the 64%-identical E. coli ortholog Hyi (P30147) exclusively isomerizes hydroxypyruvate ⇌ tartronate semialdehyde, cofactor-free, Km 12.5 mM ([PMID: 10561547](https://pubmed.ncbi.nlm.nih.gov/10561547/)).
2. **Evolutionary/sequence** — 64.1% identity, conserved catalytic Glu143/Glu240, single-copy K01816 gene.
3. **Genomic** — embedded in a compact, same-strand *gcl–hyi–glxR–glxK* operon (the glycerate pathway).
4. **Structural** — a high-confidence AlphaFold TIM-barrel (mean pLDDT 97.2) with the two catalytic glutamates 5.7 Å apart and an Arg-anchored polar pocket sized for a C3 keto/hydroxy-acid.

The alternative oxo-tetronate isomerase activity (flagged by NCBIfam HMM NF043033 within the promiscuous Sugar_Epim/Isomerase superfamily, IPR050417) is disfavored by both the high identity to a proven Hyi and the glycerate-operon context, since oxo-tetronate isomerases occur in separate tetronate/threonate-degradation clusters rather than glycerate operons.

---

## Mechanistic Model / Interpretation

### The reaction catalyzed by Hyi

Hydroxypyruvate isomerase catalyzes a reversible **aldose–ketose (keto–aldehyde) isomerization** between two C3 acids:

```
   Hydroxypyruvate                          Tartronate semialdehyde
   (3-hydroxy-2-oxopropanoate)              (2-hydroxy-3-oxopropanoate)

        COO⁻                                      COO⁻
         |                                         |
        C=O            <====  Hyi  ====>          HC-OH
         |              (EC 5.3.1.22)              |
        CH2-OH                                     CHO
```

The reaction proceeds without any cofactor via a **two-glutamate proton shuttle** (Glu143 and Glu240): one glutamate abstracts a proton to form a *cis*-enediol(ate) intermediate, and the other re-protonates on the opposite face, shifting the carbonyl between C2 and C3. The arginine pair (Arg71/Arg211) anchors the substrate's carboxylate and stabilizes the developing negative charge on the enediolate. This is the canonical chemistry of the xylose-isomerase-like TIM-barrel superfamily, adapted here to a small C3 keto/hydroxy-acid substrate.

### Position in the glycerate (glyoxylate assimilation) pathway

The four co-transcribed enzymes convert glyoxylate to a central-metabolism intermediate:

```
                          Gcl (PP_4297)          Hyi (PP_4298)
   2 × Glyoxylate  ───────────────────────▶  Tartronate  ⇌  Hydroxypyruvate
   (C2)              condensation (−CO2)      semialdehyde     (C3 isomer)
                                                   │
                                                   │ GlxR (PP_4299)
                                                   │ NAD(P)H reduction
                                                   ▼
                                              D-Glycerate
                                                   │
                                                   │ GlxK (PP_4300)
                                                   │ ATP phosphorylation
                                                   ▼
                                             2-Phosphoglycerate ──▶ central carbon metabolism
                                                                    (glycolysis / gluconeogenesis)
```

The upstream glyoxylate pool is fed by several catabolic routes:

```
   Ethylene glycol ──▶ glycolaldehyde ──▶ glycolate ──▶ glyoxylate ┐
                                                                    ├─▶ glycerate pathway (gcl–hyi–glxR–glxK)
   Purines ──▶ uric acid ──▶ allantoin ──▶ ... ──▶ glyoxylate ──────┘
```

### Interpreting the role of Hyi within the pathway

In the strict glycerate pathway of glyoxylate assimilation, the committed carbon-flux route is Gcl → GlxR → GlxK (tartronate semialdehyde is reduced directly to glycerate). The precise physiological role of the isomerase step is best understood as **metabolic balancing between the tartronate-semialdehyde and hydroxypyruvate pools**. Hydroxypyruvate is a metabolite shared with serine/glycerate metabolism, so Hyi provides a reversible bridge that allows carbon to move between the glyoxylate-derived tartronate-semialdehyde pool and the hydroxypyruvate pool depending on flux demands — an accessory/buffering role rather than a mandatory flux step. The tight operon linkage of *hyi* with *gcl*, *glxR*, and *glxK*, and its shared substrate (tartronate semialdehyde), indicate the cell co-regulates the isomerase with the core glycerate enzymes, implying its activity is needed precisely when glyoxylate assimilation is active. The conditional regulation by the repressor GclR ([PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)) means the whole module — including *hyi* — is switched on when glyoxylate-generating substrates (ethylene glycol, glycolate, allantoin/purines) are available.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|--------------------|------------------------------|
| [10561547](https://pubmed.ncbi.nlm.nih.gov/10561547/) | *Biochemical evidence that E. coli hyi (b0508, gip) encodes hydroxypyruvate isomerase* | **Primary biochemical anchor.** Purified E. coli Hyi "exclusively catalyzed the isomerization between hydroxypyruvate and tartronate semialdehyde" (Km 12.5 mM, cofactor-free, 58 kDa homodimer). PP_4298 is 64% identical to this enzyme, so the reaction and substrate specificity transfer directly. |
| [8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/) | *Molecular cloning... E. coli glyoxylate carboligase* | Defines the reaction of the adjacent operon gene *gcl* (EC 4.1.1.47): condensation of two glyoxylate molecules to tartronic semialdehyde, "a key intermediate in glyoxylate catabolism" — the metabolite *hyi* acts upon. |
| [31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/) | *Laboratory evolution... ethylene glycol metabolism by P. putida KT2440* | Shows the *hyi*-containing glyoxylate carboligase pathway is repressed by GclR and must be de-repressed for growth on ethylene glycol, establishing physiological regulation and a glyoxylate source in KT2440. |
| [41369682](https://pubmed.ncbi.nlm.nih.gov/41369682/) | *An allantoin-inducible glyoxylate utilization pathway* | Identifies purine/allantoin catabolism (via uric acid) as a physiological source of the glyoxylate assimilated by the glycerate pathway in pseudomonads. |
| [22104170](https://pubmed.ncbi.nlm.nih.gov/22104170/) | *An engineered pathway for glyoxylate metabolism in tobacco (gcl + hyi to peroxisomes)* | Demonstrates the *gcl*+*hyi* module functioning together in a heterologous system; the requirement for an added organelle-targeting peptide confirms the native bacterial enzyme is cytosolic. |
| [38354877](https://pubmed.ncbi.nlm.nih.gov/38354877/) | *Interrogating L-fuconate dehydratase with tartronate and 3-hydroxypyruvate* | Corroborates that hydroxypyruvate and tartronate are recognized as small-acid substrates/probes by related superfamily active sites, consistent with the C3-acid specificity inferred for Hyi. |

Additional papers in the corpus — photorespiratory-bypass engineering in Arabidopsis, rice, cucumber, and tobacco ([PMID: 17435746](https://pubmed.ncbi.nlm.nih.gov/17435746/), [PMID: 33075506](https://pubmed.ncbi.nlm.nih.gov/33075506/), [PMID: 34895540](https://pubmed.ncbi.nlm.nih.gov/34895540/), [PMID: 31191593](https://pubmed.ncbi.nlm.nih.gov/31191593/)) — repeatedly deploy the bacterial glycolate/glyoxylate catabolic pathway (glycolate dehydrogenase, glyoxylate carboligase, tartronic semialdehyde reductase, and in some cases *hyi*) to reroute carbon, reinforcing the pathway membership and co-functionality of *hyi* with *gcl*, *glxR*, and *glxK*. Several human-focused proteomics/metabolomics papers ([PMID: 40108892](https://pubmed.ncbi.nlm.nih.gov/40108892/), [PMID: 35509884](https://pubmed.ncbi.nlm.nih.gov/35509884/)) mention a human "hydroxypyruvate isomerase (HYI)" as a biomarker; these concern a **different organism's ortholog** and are **not** used to support claims about the P. putida enzyme, though they confirm the family name and reaction identity across taxa.

---

## Supported vs. Refuted Hypotheses

- **Supported:** *hyi* (PP_4298) is a hydroxypyruvate ⇌ tartronate-semialdehyde isomerase (EC 5.3.1.22); it is embedded in and co-regulated with the glyoxylate carboligase (glycerate) pathway; it acts in the **cytoplasm** within glyoxylate/dicarboxylate metabolism (KEGG ppu00630); it is single-copy and cofactor-independent; its catalytic machinery is a two-glutamate (Glu143/Glu240) proton shuttle.
- **Not supported / ruled out:** No evidence for a membrane, secreted, transport, structural, or signaling role; no metal/nucleotide cofactor dependence is indicated for the characterized ortholog; no paralog redundancy exists in the KT2440 genome.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical assay of the P. putida protein.** The activity, kinetics, and substrate specificity are all inferred from the 64%-identical E. coli ortholog; UniProt lists Q88F02 at evidence level **PE3 (inferred from homology)**. The P. putida enzyme has not itself been purified and assayed, so its Km, kcat, cofactor independence, and quaternary structure are predicted, not measured.

2. **Superfamily promiscuity.** The xylose-isomerase-like / Sugar_Epim/Isomerase superfamily (IPR050417) is functionally promiscuous. The same protein is flagged by an oxo-tetronate isomerase HMM (NCBIfam NF043033), so an alternative or secondary activity on a four-carbon oxo-acid cannot be formally excluded without direct assays.

3. **Precise physiological necessity is inferred, not demonstrated.** In the canonical glycerate pathway the committed steps are Gcl and GlxR; the exact metabolic advantage conferred by the Hyi isomerization step in *P. putida* has not been experimentally dissected, and no *hyi* single-gene knockout phenotype in KT2440 is documented in the reviewed corpus.

4. **Regulation details.** While GclR-mediated repression of the pathway is established, the specific promoter architecture, the exact extent of co-transcription of *hyi* with *gcl/glxR/glxK*, and the role of the upstream TetR/AcrR regulator (PP_4295) have not been experimentally mapped for this locus.

5. **Structural inference is model-based.** The active-site geometry comes from an AlphaFold model, not an experimental crystal structure of Q88F02; no ligand-bound structure exists to confirm the binding mode.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay.** Heterologously express and purify PP_4298 (His-tagged) and measure hydroxypyruvate ⇌ tartronate semialdehyde isomerase activity (e.g., coupled spectrophotometric or CD-based assay analogous to [PMID: 38354877](https://pubmed.ncbi.nlm.nih.gov/38354877/)), determining Km, kcat, cofactor requirement, and pH optimum. This would upgrade the annotation from PE3 (homology) to PE1 (protein-level evidence).

2. **Substrate-specificity screen.** Test the purified enzyme against a panel of small keto/hydroxy/oxo acids (hydroxypyruvate, tartronate semialdehyde, and candidate oxo-tetronate substrates) to determine whether the enzyme is a dedicated hydroxypyruvate isomerase or exhibits the promiscuity suggested by the NF043033 HMM.

3. **Site-directed mutagenesis** of Glu143 and Glu240 (E→Q or E→A) to confirm the two-glutamate proton-shuttle mechanism predicted from the AlphaFold model; assay Arg71/Arg211 mutants to test the carboxylate-anchoring hypothesis.

4. **Genetic knockout and growth phenotyping.** Construct a clean *hyi* deletion in KT2440 and test growth on ethylene glycol, glycolate, allantoin, and glyoxylate, comparing to *gcl/glxR/glxK* knockouts, to define the physiological necessity of the isomerase step.

5. **Operon/transcription mapping.** Use RT-PCR or RNA-seq (± inducing substrates) and reporter fusions to confirm co-transcription of *gcl–hyi–glxR–glxK* as a single operon and to map GclR- and PP_4295-dependent regulation.

6. **Experimental structure.** Solve a crystal or cryo-EM structure of Q88F02, ideally with substrate/product or a transition-state analog bound, to validate the Glu143/Glu240 catalytic geometry and the C3-acid binding pocket.

---

### Key References

- Ashiuchi M, Misono H. *Biochemical evidence that E. coli hyi (orf b0508, gip) gene encodes hydroxypyruvate isomerase.* 1999. [PMID: 10561547](https://pubmed.ncbi.nlm.nih.gov/10561547/).
- Chang YY, Wang AY, Cronan JE. *Molecular cloning, DNA sequencing, and biochemical analyses of E. coli glyoxylate carboligase.* 1993. [PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/).
- Li WJ et al. *Laboratory evolution reveals the metabolic and regulatory basis of ethylene glycol metabolism by Pseudomonas putida KT2440.* 2019. [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/).
- Parkhill et al. *An allantoin-inducible glyoxylate utilization pathway in fluorescent Pseudomonas.* 2025. [PMID: 41369682](https://pubmed.ncbi.nlm.nih.gov/41369682/).
- Carvalho JFC et al. *An engineered pathway for glyoxylate metabolism in tobacco (gcl + hyi to peroxisomes).* 2011. [PMID: 22104170](https://pubmed.ncbi.nlm.nih.gov/22104170/).
- Databases: UniProt Q88F02; KEGG ppu:PP_4298 (K01816); AlphaFold DB AF-Q88F02-F1; InterPro/Pfam/TIGRFAM as cited.

*Report generated from a 5-iteration autonomous investigation integrating UniProt/InterPro/KEGG annotations, pairwise sequence alignment against the characterized E. coli ortholog, genomic-neighborhood analysis, an AlphaFold structural model, and 21 literature references.*


## Artifacts

- [OpenScientist final report](hyi-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hyi-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10561547
2. PMID:8440684
3. PMID:31166064
4. PMID:41369682
5. PMID:22104170
6. PMID:17435746
7. PMID:33075506
8. PMID:34895540
9. PMID:31191593
10. PMID:40108892
11. PMID:35509884
12. PMID:38354877