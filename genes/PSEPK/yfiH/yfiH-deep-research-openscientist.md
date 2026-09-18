---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T08:36:06.965920'
end_time: '2026-08-13T08:50:48.876484'
duration_seconds: 881.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: yfiH
  gene_symbol: yfiH
  uniprot_accession: Q88Q72
  protein_description: 'RecName: Full=Purine nucleoside phosphorylase {ECO:0000256|RuleBase:RU361274};'
  gene_info: Name=yfiH {ECO:0000313|EMBL:AAN66249.1}; OrderedLocusNames=PP_0624 {ECO:0000313|EMBL:AAN66249.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the purine nucleoside phosphorylase YfiH/LACC1
  protein_domains: Cu_polyphenol_OxRdtase. (IPR003730); Cu_polyphenol_OxRdtase_sf.
    (IPR038371); Cytotoxic_necrot_fac-like_cat. (IPR011324); Cu-oxidase_4 (PF02578)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: yfiH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: yfiH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88Q72
- **Protein Description:** RecName: Full=Purine nucleoside phosphorylase {ECO:0000256|RuleBase:RU361274};
- **Gene Information:** Name=yfiH {ECO:0000313|EMBL:AAN66249.1}; OrderedLocusNames=PP_0624 {ECO:0000313|EMBL:AAN66249.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the purine nucleoside phosphorylase YfiH/LACC1
- **Key Domains:** Cu_polyphenol_OxRdtase. (IPR003730); Cu_polyphenol_OxRdtase_sf. (IPR038371); Cytotoxic_necrot_fac-like_cat. (IPR011324); Cu-oxidase_4 (PF02578)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "yfiH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'yfiH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **yfiH** (gene ID: yfiH, UniProt: Q88Q72) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *yfiH* (PP_0624, UniProt Q88Q72) in *Pseudomonas putida* KT2440

## Summary

The gene **yfiH** (ordered locus **PP_0624**; UniProt **Q88Q72**) of *Pseudomonas putida* KT2440 encodes a **246-amino-acid cytoplasmic enzyme of the YfiH/LACC1 family**. Despite a fold that historically caused it to be annotated as a "laccase-like" copper–polyphenol oxidase, the family is now understood to be a **multifunctional purine-metabolizing enzyme**. Its primary biochemical activity is **purine nucleoside phosphorylase (PNP, EC 2.4.2.1)**: it uses inorganic phosphate to cleave the N-glycosidic bond of purine (deoxy)ribonucleosides such as adenosine and inosine into the free base (adenine or hypoxanthine) plus α-D-ribose-1-phosphate. The same active site also carries **5'-methylthioadenosine phosphorylase (MTAP, EC 2.4.2.28)** and **adenosine deaminase (EC 3.5.4.4)** activities, placing YfiH at the crossroads of central purine salvage and methionine/MTA salvage in the cytoplasm.

Beyond its role in nucleotide metabolism, bacterial YfiH has a second, genetically well-documented physiological function: it acts as a **peptidoglycan (PG) stem-peptide editing / quality-control factor** (hence its alternative name **PgeF**, "peptidoglycan editing factor"). In *Escherichia coli*, loss of *yfiH* leads to misincorporation of L-serine or glycine in place of the canonical L-alanine at position 1 of the PG stem peptide, producing β-lactam hypersensitivity, morphological defects, reduced PG synthesis, and lethality in strains defective in PG recycling or remodelling. This editing function is conserved across the bacterial kingdom, as *yfiH* orthologs from Gram-positive genera complement an *E. coli* deletion.

It is important to state clearly that **PP_0624 itself has not been experimentally characterized**. Every functional statement in this report is an **inference from orthology** to the well-studied human LACC1/FAMIN protein and to *E. coli* YfiH/PgeF, combined with UniProt family/rule-based annotations. The gene symbol "yfiH" and the target organism (*P. putida* KT2440) are correctly matched to the UniProt record, and the family/domain signatures (Cu_polyphenol_OxRdtase, Cu-oxidase_4, Cytotoxic_necrot_fac-like_cat) align with the characterized YfiH/LACC1 family, so this report proceeds on a firm identification.

---

## Verification of Gene Identity

Before presenting findings, the mandated identity checks were completed:

| Check | Result |
|-------|--------|
| Gene symbol "yfiH" matches protein description | ✅ Yes — UniProt Q88Q72 lists Name=yfiH, family "purine nucleoside phosphorylase YfiH/LACC1" |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), KEGG `ppu:PP_0624` |
| Protein family/domains align with literature | ✅ Cu-oxidase_4 (PF02578) / Cu_polyphenol_OxRdtase (IPR003730) = the "laccase-fold" of the YfiH/LACC1 family |
| Literature is for the same gene, not a homonym | ✅ Bacterial YfiH/PgeF and human LACC1/FAMIN are true orthologs of PP_0624 |

The literature base is **not** ambiguous: bacterial *yfiH* (a.k.a. *pgeF*) and its eukaryotic ortholog LACC1/FAMIN belong to a single, well-defined protein family, and the functional inferences transfer cleanly to the *P. putida* protein. No study on a homonymous but unrelated gene was mistaken for the target.

---

## Key Findings

### Finding 1 — The YfiH/LACC1 family is a multifunctional purine nucleoside phosphorylase

The single most important reassignment of function for this family came from an unbiased LC-MS enzymatic screen of the human "orphan" protein **FAMIN** (encoded by **LACC1**), the eukaryotic ortholog of bacterial YfiH. The study demonstrated that FAMIN **phosphorolytically cleaves adenosine into adenine and ribose-1-phosphate**, the defining reaction of a purine nucleoside phosphorylase. Critically, the authors reported that FAMIN and its **prokaryotic orthologs** additionally possess **adenosine deaminase, purine nucleoside phosphorylase, and S-methyl-5'-thioadenosine phosphorylase activities** — thereby combining, in a single polypeptide, the activities of several namesake enzymes of central purine metabolism ([PMID: 31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/)).

This experimental result is the empirical anchor for the UniProt RuleBase assignment of Q88Q72 to the "purine nucleoside phosphorylase YfiH/LACC1" family. Because the *P. putida* protein is a direct prokaryotic ortholog, the same suite of catalytic capabilities is inferred for PP_0624. In physiological terms, this places YfiH in the **purine nucleotide cycle / purine salvage**, recovering free bases and ribose-1-phosphate from nucleosides for reuse.

> Supporting quote: *"We report that FAMIN phosphorolytically cleaves adenosine into adenine and ribose-1-phosphate."* — [PMID: 31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/)

### Finding 2 — Q88Q72 catalyzes coupled phosphorolysis/deamination reactions at a single metal (Zn) center

The UniProt entry for Q88Q72 (246 aa; KEGG `ppu:PP_0624`) annotates **three coupled catalytic activities** (rule/family-based, evidence code ECO:0000256):

| Activity | EC number | Reaction (Rhea) |
|----------|-----------|-----------------|
| Purine nucleoside phosphorylase | EC 2.4.2.1 | adenosine + Pᵢ → α-D-ribose-1-phosphate + adenine; inosine + Pᵢ → ribose-1-phosphate + hypoxanthine (Rhea 27642/27646) |
| 5'-Methylthioadenosine phosphorylase | EC 2.4.2.28 | MTA + Pᵢ → 5-methylthioribose-1-phosphate + adenine (Rhea 11852) |
| Adenosine deaminase | EC 3.5.4.4 | adenosine + H₂O → inosine + NH₄⁺ (Rhea 24408) |

UniProt keywords include **Metal-binding** and **Zinc**, indicating a **single catalytic metal ion**. This is significant: although the fold is a copper-polyphenol-oxidase ("laccase") fold and was historically presumed to bind copper, the functional metal annotated for this entry is a single Zn ion coordinating the phosphorolysis/deamination chemistry. The experimental demonstration that the family carries **adenosine deaminase, PNP, and MTAP activities** ([PMID: 31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/)) directly supports the three activities that UniProt assigns to Q88Q72.

Mechanistically, these three activities are metabolically complementary: adenosine deaminase converts adenosine → inosine, PNP then phosphorolyzes inosine → hypoxanthine + ribose-1-phosphate, and MTAP salvages the methionine-cycle byproduct 5'-methylthioadenosine. A single active site thus performs a small, self-contained module of purine and MTA salvage. The **substrate specificity** is centered on 6-aminopurine and 6-oxopurine ribonucleosides (adenosine, inosine) and the methionine-salvage intermediate MTA.

### Finding 3 — A "laccase/polyphenol-oxidase" fold repurposed for phosphorylase chemistry

The domain architecture of Q88Q72 — **Cu_polyphenol_OxRdtase (IPR003730)**, **Cu-oxidase_4 (PF02578)**, and **Cytotoxic_necrot_fac-like_cat (IPR011324)** — is the origin of the historical, and now known to be misleading, annotation of YfiH as a "**Laccase domain protein**" or putative polyphenol oxidase. Structural-genomics efforts solved several YfiH structures under this legacy interpretation (e.g., YfiH from *Shigella flexneri*, [PMID: 16498617](https://pubmed.ncbi.nlm.nih.gov/16498617/)), and database-driven proteomics work in *Campylobacter jejuni* still lists the annotation "**Laccase domain protein YfiH**" ([PMID: 34799308](https://pubmed.ncbi.nlm.nih.gov/34799308/)).

However, the direct enzymology from FAMIN ([PMID: 31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/)) reassigns the family's true catalytic activity to **purine nucleoside phosphorylase**, not a copper-dependent oxidase. This is a textbook example of **fold-function divergence**: a scaffold with structural similarity to copper oxidases has been evolutionarily repurposed for a completely different reaction chemistry, and it lacks the classical multi-copper centers of true laccases. The lesson for annotating PP_0624 is that the "laccase" or "polyphenol oxidase" labels that may still propagate through databases should be treated as **legacy fold-based artifacts**, not as evidence of oxidase function.

> Supporting quote: *"Laccase domain protein YfiH"* — [PMID: 34799308](https://pubmed.ncbi.nlm.nih.gov/34799308/) (illustrating the persistent legacy annotation)

### Finding 4 — Bacterial YfiH (PgeF) safeguards peptidoglycan peptide composition

The best-characterized *in vivo* function of a bacterial YfiH comes from *E. coli*, where genetic, biochemical, and mass-spectrometric analyses established YfiH (renamed **PgeF**) as a **peptidoglycan peptide-composition editing factor** ([PMID: 28612943](https://pubmed.ncbi.nlm.nih.gov/28612943/)). The authors identified YfiH via a β-lactam hypersensitive mutant and showed that a conserved ORF of unknown function contributes to the maintenance of PG peptide composition.

The specific editing defect is precise: in the **absence of yfiH**, cells **misincorporate the non-canonical amino acids L-serine or glycine in place of L-alanine at position 1** of the PG stem peptide. This aberrant PG causes a suite of phenotypes:

- **β-lactam hypersensitivity**
- **Lethality** in mutants defective in PG remodelling or recycling pathways
- **Altered cell morphology**
- **Reduced PG synthesis**

Crucially, the function is **conserved across bacteria**: *yfiH* orthologs from other Gram-positive genera complemented the *E. coli* deletion, indicating a conserved pathway across the bacterial kingdom. This cross-genus complementation is the strongest single justification for inferring an analogous PG-editing role for *P. putida* PP_0624. The structural basis for this peptidoglycan-editing activity was subsequently determined ([PMID: 35164571](https://pubmed.ncbi.nlm.nih.gov/35164571/)), and a conserved editing mechanism for the fidelity of bacterial cell-wall biosynthesis was further elaborated ([PMID: 40632566](https://pubmed.ncbi.nlm.nih.gov/40632566/)).

> Supporting quotes ([PMID: 28612943](https://pubmed.ncbi.nlm.nih.gov/28612943/)):
> - *"we find that a conserved open reading frame of unknown function, YfiH (renamed PgeF) contributes to the maintenance of peptide composition in E. coli"*
> - *"absence of yfiH results in incorporation of non-canonical amino acids, L-serine or glycine in place of L-alanine in PG sacculi leading to β-lactam - sensitivity, lethality in mutants defective in PG remodelling or recycling pathways, altered cell morphology and reduced PG synthesis"*
> - *"yfiH orthologs from other Gram-positive genera were able to compensate the absence of yfiH in E. coli indicating a conserved pathway in bacterial kingdom"*

### Finding 5 — *yfiH* is genomically linked to the division/cell-wall (dcw) locus but individually dispensable

In several actinobacteria and firmicutes, *yfiH* is positioned within or adjacent to the **division and cell-wall (dcw) gene cluster**, immediately downstream of the cell-division genes **ftsQ–ftsZ**. In *Streptomyces collinus*, the genes upstream of *ftsZ* are *ftsQ*, *murG*, and *ftsW*, and downstream lies *yfiH* ([PMID: 10679194](https://pubmed.ncbi.nlm.nih.gov/10679194/)). In *Brevibacterium lactofermentum*, YFIH sits downstream of *ftsQ*/*ftsZ* ([PMID: 11523774](https://pubmed.ncbi.nlm.nih.gov/11523774/)).

Functionally, disruption of *yfiH* (and neighboring ORFs) **did not impair growth or viability**, whereas *ftsQ* and *ftsZ* were essential. Thus *yfiH* is **individually dispensable** under standard laboratory conditions — consistent with a quality-control / editing role that becomes critical only under cell-wall stress or in genetic backgrounds compromised for PG recycling/remodelling (as seen in the *E. coli* work). The genomic linkage to the dcw locus reinforces a cell-envelope–associated physiological context for the protein.

> Supporting quotes:
> - *"Upstream of ftsZ are localized genes ftsQ, murG, and ftsW, and downstream is yfiH"* — [PMID: 10679194](https://pubmed.ncbi.nlm.nih.gov/10679194/)
> - *"The three ORFs (YFIH, ORF5 and ORF6) located downstream of the cell division genes ftsQ and ftsZ in Brevibacterium lactofermentum were disrupted by single homologous recombination events"* — [PMID: 11523774](https://pubmed.ncbi.nlm.nih.gov/11523774/)

---

## Mechanistic Model / Interpretation

YfiH (PP_0624) is best understood as a **dual-function, single-metal (Zn) cytoplasmic enzyme** that bridges purine/MTA salvage metabolism and cell-wall quality control. The two activities are not contradictory; both reflect a nucleophilic/phosphorolytic active site acting on distinct substrate classes (nucleosides vs. non-canonical residues in peptidoglycan precursors), and the family's history of misannotation as a laccase reflects fold similarity rather than true oxidase chemistry.

```
                        ┌───────────────────────────────────────────────┐
                        │   YfiH / PgeF (PP_0624, Q88Q72)                │
                        │   YfiH/LACC1 family · Cu-oxidase_4 "laccase"   │
                        │   fold · single catalytic Zn²⁺ · CYTOPLASM     │
                        └───────────────────────────────────────────────┘
                               │                            │
             ┌─────────────────┘                            └──────────────────┐
             ▼                                                                  ▼
   PURINE / MTA SALVAGE (biochemical)                        CELL-WALL QUALITY CONTROL (physiological)
   ─────────────────────────────────                        ────────────────────────────────────────
   adenosine ──ADA(3.5.4.4)──► inosine                       Edits PG stem peptide: prevents
   inosine ──PNP(2.4.2.1)──► hypoxanthine                    mis-incorporation of L-Ser / Gly
             + ribose-1-phosphate                            in place of L-Ala at position 1
   MTA ──MTAP(2.4.2.28)──► adenine                           │
             + 5-methylthioribose-1-P                        ▼
   → feeds base + sugar-phosphate back                       Loss ⇒ β-lactam sensitivity, altered
     into central purine metabolism                          morphology, ↓PG synthesis, lethality
                                                             in PG recycling/remodelling mutants
```

**Localization.** The enzyme functions in the **cytoplasm**. Purine/MTA salvage is a cytoplasmic process, and PG stem-peptide editing acts on precursors/recycling intermediates on the cytoplasmic side. The family lacks signal peptides or transmembrane segments, and there is no evidence for secretion. The genomic linkage to cytoplasmic/membrane-associated dcw genes such as *ftsZ*, *murG*, and *ftsW* is consistent with a cytoplasmic, cell-envelope–adjacent context.

**Pathway integration.** In its metabolic role, YfiH participates in the **purine nucleotide cycle** and **methionine/MTA salvage**, recovering free purine bases and (methylthio)ribose-1-phosphate for reuse — consolidating activities normally distributed across *deoD*-type PNP, *add*-type adenosine deaminase, and *mtnP*/MTAP enzymes. In its physiological role, it is a **fidelity/editing factor** in **peptidoglycan biosynthesis**, protecting the L-Ala-1 identity of the stem peptide and thereby preserving cell-wall crosslinking and β-lactam resistance thresholds.

**Reconciling the two roles.** The purine-phosphorylase and PG-editing activities were reported by different laboratories with different assays; both are supported by direct evidence in family members. They may reflect genuine moonlighting of a single active site, or a metabolic activity whose products/flux impinge on cell-wall precursor quality. For PP_0624 specifically, both functions are inferences from orthology, with the purine-phosphorylase activity being the assignment carried by UniProt for this accession.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|-------------------------------|
| [31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/) | *FAMIN Is a Multifunctional Purine Enzyme Enabling the Purine Nucleotide Cycle* | **Primary experimental anchor.** Direct LC-MS enzymology of the human LACC1/FAMIN ortholog demonstrates PNP activity (adenosine → adenine + ribose-1-P) plus adenosine deaminase and MTAP; explicitly states prokaryotic orthologs share these activities. Basis for Findings 1 and 2. |
| [28612943](https://pubmed.ncbi.nlm.nih.gov/28612943/) | *Identification of YfiH (PgeF) as a factor contributing to the maintenance of bacterial peptidoglycan composition* | **Primary in vivo function.** Genetic/MS evidence in *E. coli* for PG stem-peptide editing; defines the L-Ser/Gly-for-L-Ala defect, phenotypes, and cross-genus conservation. Basis for Finding 4. |
| [35164571](https://pubmed.ncbi.nlm.nih.gov/35164571/) | *Structural Basis for the Peptidoglycan-Editing Activity of YfiH* | Structural mechanism underpinning the PG-editing role; complements PMID 28612943. |
| [40632566](https://pubmed.ncbi.nlm.nih.gov/40632566/) | *A conserved editing mechanism for the fidelity of bacterial cell wall biosynthesis* | Extends the editing model to a conserved fidelity mechanism for cell-wall biosynthesis. |
| [16498617](https://pubmed.ncbi.nlm.nih.gov/16498617/) | *Crystal structure of hypothetical protein YfiH from Shigella flexneri at 2 Å* | Early structural-genomics structure; illustrates the "hypothetical/laccase-fold" era of annotation (Finding 3). |
| [34799308](https://pubmed.ncbi.nlm.nih.gov/34799308/) | *Comparative proteome-wide study … Campylobacter jejuni* | Documents the persistent legacy "Laccase domain protein YfiH" annotation (Finding 3). |
| [10679194](https://pubmed.ncbi.nlm.nih.gov/10679194/) | *Isolation and characterization of dcw cluster from Streptomyces collinus* | Documents genomic linkage of *yfiH* to *ftsQ–ftsZ*/*murG*/*ftsW* (Finding 5). |
| [11523774](https://pubmed.ncbi.nlm.nih.gov/11523774/) | *The cell division genes ftsQ and ftsZ, but not … YFIH, ORF5, ORF6, are essential …* | Confirms dcw synteny and that *yfiH* is dispensable, unlike *ftsQ/ftsZ* (Finding 5). |

**Convergence.** Two independent lines of primary evidence — enzymology (PMID 31978345) and bacterial genetics/mass spectrometry (PMID 28612943) — together define the two faces of YfiH function. The structural (PMID 16498617, 35164571) and comparative-genomic (PMID 10679194, 11523774, 34799308) papers provide corroborating context and explain the historical laccase misannotation.

---

## Supported vs. Refuted Hypotheses

**Supported by evidence:**
- YfiH/LACC1 family is a multifunctional **purine nucleoside phosphorylase** (PNP + MTAP + adenosine deaminase) — [PMID: 31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/); UniProt Q88Q72 catalytic annotations.
- Bacterial YfiH (PgeF) safeguards **peptidoglycan stem-peptide composition** — [PMID: 28612943](https://pubmed.ncbi.nlm.nih.gov/28612943/); [PMID: 35164571](https://pubmed.ncbi.nlm.nih.gov/35164571/); [PMID: 40632566](https://pubmed.ncbi.nlm.nih.gov/40632566/).
- Conserved **synteny with the dcw/ftsQZ cluster**; gene individually dispensable — [PMID: 10679194](https://pubmed.ncbi.nlm.nih.gov/10679194/), [PMID: 11523774](https://pubmed.ncbi.nlm.nih.gov/11523774/).

**Refuted / down-weighted:**
- YfiH as a functional **laccase / multicopper polyphenol oxidase**: this legacy annotation reflects the fold, not measured activity; the family lacks classical laccase copper centers and performs phosphorylase/deaminase chemistry instead — [PMID: 31978345](https://pubmed.ncbi.nlm.nih.gov/31978345/).

---

## Limitations and Knowledge Gaps

1. **No direct study of PP_0624.** All functional claims are **orthology-based inferences** from the human LACC1/FAMIN protein and *E. coli* YfiH/PgeF, plus UniProt rule-based annotation (ECO:0000256). The *P. putida* KT2440 protein has not been enzymatically assayed, structurally solved, or genetically dissected. Confidence rests on strong family conservation and cross-genus complementation.

2. **Metal identity nuance.** UniProt annotates a single **Zn**-binding site, but the fold is a copper-oxidase fold and older literature invoked copper. The precise metal used by the *P. putida* enzyme in vivo, and whether copper plays any role, remains unverified for this ortholog.

3. **Relative importance of the two functions in *P. putida*.** It is unknown whether PP_0624 primarily serves purine/MTA salvage, PG editing, or both. In *E. coli*, the PG-editing phenotype is conditional (revealed under β-lactam stress or in recycling/remodelling mutants), so the metabolic role could dominate under standard growth.

4. **Substrate specificity details.** Quantitative kinetics (kcat/Km) for adenosine vs. inosine vs. MTA, and any preference for ribo- vs. deoxyribonucleosides, have not been measured for the *P. putida* enzyme.

5. **Localization is inferred, not demonstrated.** Cytoplasmic localization is consistent with function and the absence of a signal peptide, but has not been experimentally confirmed for PP_0624.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology of PP_0624.** Express and purify Q88Q72 and assay PNP (adenosine, inosine), MTAP (MTA), and adenosine deaminase activities by LC-MS/coupled spectrophotometric assays; determine kcat/Km and metal dependence (Zn vs. Cu) via metal reconstitution.

2. **Peptidoglycan composition analysis of a *P. putida* Δ*PP_0624* mutant.** Construct a clean deletion and perform muropeptide analysis (HPLC/LC-MS of digested sacculi) to test for L-Ser/Gly misincorporation at stem-peptide position 1, mirroring the *E. coli* assay ([PMID: 28612943](https://pubmed.ncbi.nlm.nih.gov/28612943/)).

3. **β-lactam susceptibility and synthetic-lethality screen.** Test the Δ*PP_0624* mutant for β-lactam hypersensitivity and combine with mutations in *P. putida* PG recycling/remodelling genes to reproduce the conditional lethality seen in *E. coli*.

4. **Complementation test.** Ask whether *P. putida* PP_0624 rescues an *E. coli* Δ*yfiH* strain (and vice versa), directly testing functional orthology.

5. **Structural determination / AlphaFold analysis.** Solve or model the PP_0624 structure, confirm the single-metal active-site geometry, and compare with the *Shigella* YfiH ([PMID: 16498617](https://pubmed.ncbi.nlm.nih.gov/16498617/)) and the PG-editing structural model ([PMID: 35164571](https://pubmed.ncbi.nlm.nih.gov/35164571/)).

6. **Metabolomic phenotyping.** Compare purine-nucleoside and MTA pools between wild-type and Δ*PP_0624* *P. putida* to establish the in vivo contribution to purine/MTA salvage.

---

## Conclusion

*yfiH* / PP_0624 in *Pseudomonas putida* KT2440 encodes a cytoplasmic, single-metal (Zn) enzyme of the YfiH/LACC1 family. By orthology to experimentally characterized LACC1/FAMIN and *E. coli* YfiH/PgeF, its **primary catalytic function is purine nucleoside phosphorylase (EC 2.4.2.1)** — phosphorolysis of adenosine/inosine to the free base plus ribose-1-phosphate — with additional **MTAP (EC 2.4.2.28)** and **adenosine deaminase (EC 3.5.4.4)** activities at the same active site, serving cytoplasmic purine and MTA salvage. In parallel, bacterial YfiH acts as a **conserved peptidoglycan stem-peptide editing/quality-control factor (PgeF)** that prevents mis-incorporation of Ser/Gly for L-Ala at position 1 of the stem peptide, protecting cell-wall integrity and β-lactam resistance. Its historical "laccase/polyphenol oxidase" annotation reflects fold similarity, not true oxidase activity. All statements are inferences from orthology and UniProt family rules, as PP_0624 has not been directly studied.


## Artifacts

- [OpenScientist final report](yfiH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](yfiH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31978345
2. PMID:16498617
3. PMID:34799308
4. PMID:28612943
5. PMID:35164571
6. PMID:40632566
7. PMID:10679194
8. PMID:11523774