---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T15:02:34.449475'
end_time: '2026-07-20T15:20:19.476730'
duration_seconds: 1065.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pqqF
  gene_symbol: pqqF
  uniprot_accession: Q88QV3
  protein_description: 'RecName: Full=Coenzyme PQQ synthesis protein F; EC=3.4.24.-;
    AltName: Full=Pyrroloquinoline quinone biosynthesis protein F;'
  gene_info: Name=pqqF; OrderedLocusNames=PP_0381;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase M16 family. .
  protein_domains: Metalloenz_LuxS/M16. (IPR011249); Pept_M16_N. (IPR011765); Pept_M16_Zn_BS.
    (IPR001431); Peptidase_M16. (IPR050626); PQQ_synth_PqqF. (IPR011844)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pqqF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pqqF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QV3
- **Protein Description:** RecName: Full=Coenzyme PQQ synthesis protein F; EC=3.4.24.-; AltName: Full=Pyrroloquinoline quinone biosynthesis protein F;
- **Gene Information:** Name=pqqF; OrderedLocusNames=PP_0381;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase M16 family. .
- **Key Domains:** Metalloenz_LuxS/M16. (IPR011249); Pept_M16_N. (IPR011765); Pept_M16_Zn_BS. (IPR001431); Peptidase_M16. (IPR050626); PQQ_synth_PqqF. (IPR011844)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pqqF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pqqF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pqqF** (gene ID: pqqF, UniProt: Q88QV3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PqqF (Coenzyme PQQ Synthesis Protein F) in *Pseudomonas putida* KT2440

**Gene:** *pqqF* (ordered locus **PP_0381**)
**UniProt:** [Q88QV3](https://www.uniprot.org/uniprotkb/Q88QV3)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK
**EC:** 3.4.24.- (metalloendopeptidase)
**Protein family:** Peptidase M16 (inverzincin / pitrilysin clan)

---

## Summary

**PqqF is a cytoplasmic, zinc-dependent M16-family metalloendopeptidase whose primary biological function is to act as the protease that liberates the direct amino-acid precursor of the redox cofactor pyrroloquinoline quinone (PQQ).** During PQQ biosynthesis, the small ribosomally synthesized precursor peptide **PqqA** is first modified by the radical-SAM enzyme PqqE, which forms a covalent carbon–carbon cross-link between a conserved glutamate and tyrosine. PqqF is the peptidase that then hydrolyzes the flanking peptide bonds to **excise the cross-linked Glu–Tyr unit**, releasing the substrate that is subsequently cyclized and oxidized (by PqqB and PqqC) into mature PQQ. In this sense PqqF is a peptide-processing enzyme in a **RiPP-like (ribosomally synthesized and post-translationally modified peptide) cofactor biosynthesis pathway**, not a classical degradative protease.

The enzyme carries the canonical M16 "inverzincin" active site — the inverted zinc-binding motif **HxxEH** (His49–Phe–Leu–Glu52–His53) together with a distal catalytic glutamate (Glu130) — placing it firmly in Pfam PF00675 / peptidase clan ME. It is a large (766-residue) bilobed protein and, in *P. putida* KT2440, is the first gene of the **pqqFABCDEG** operon. Genetic and biochemical evidence across multiple bacteria (*Klebsiella pneumoniae*, *Methylobacterium extorquens*, *Pseudomonas aeruginosa*, and an alpha-proteobacterium studied by the Klinman group) confirms that PqqF-type zinc proteases are required for PQQ production and are frequently interchangeable — the excision step can be supplied in *trans* by related M16/zinc proteases in organisms lacking a dedicated *pqqF*. In *P. putida* KT2440 specifically, *pqqF* expression tracks the amount of PQQ synthesized, implying a role in tuning cofactor output to growth conditions.

Localization and pathway context are well constrained. PqqF has **no signal peptide** and operates in the **cytoplasm**, where the entire PqqA-processing cascade takes place. The mature PQQ cofactor is subsequently exported to the **periplasm**, where it serves quinoprotein dehydrogenases — most prominently the membrane-bound, PQQ-dependent **glucose dehydrogenase (Gcd)** that oxidizes glucose to gluconic acid in the periplasmic space, a reaction central to *P. putida*'s direct-oxidation metabolism and phosphate-solubilizing lifestyle. Thus PqqF's precise contribution is upstream and cytoplasmic: it manufactures the peptide-derived precursor that ultimately becomes the extracytoplasmic cofactor.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and **passed**:

| Criterion | Expected (UniProt) | Found in literature/databases | Match |
|---|---|---|---|
| Gene symbol | *pqqF* | *pqqF* used consistently for the PQQ-biosynthesis protease | ✅ |
| Protein description | Coenzyme PQQ synthesis protein F, EC 3.4.24.- | M16 zinc protease excising PQQ precursor | ✅ |
| Organism | *P. putida* KT2440 (PSEPK) | *pqqFABCDEG* operon characterized in KT2440 | ✅ |
| Family/domains | Peptidase M16; HxxEH inverzincin motif | Pfam PF00675, PROSITE PS00143 INSULINASE, "family of zinc proteases" | ✅ |

The literature on *pqqF* is unambiguous and organism-consistent; there is **no** competing gene of a different function sharing the symbol. Research proceeded normally. It is worth noting, however, that the bulk of recent PubMed hits for "PQQ" concern the *pharmacology of the PQQ molecule itself* (anti-aging, Nrf2 signaling, oocyte quality, osteoarthritis, lupus) rather than the biosynthetic enzyme PqqF; these were correctly excluded as irrelevant to the enzyme's function.

---

## Key Findings

### Finding 1 — PqqF is an M16-family zinc metalloendopeptidase with a canonical inverzincin active site

UniProt Q88QV3 describes a **766-amino-acid** soluble protein annotated as EC 3.4.24.-, with the keyword set Metalloprotease / Zinc / Metal-binding / Hydrolase and the family assignment "Belongs to the peptidase M16 family." This is corroborated by an unusually consistent stack of domain signatures: InterPro **IPR011765** (Pept_M16_N), **IPR001431** (Pept_M16_Zn_BS — the zinc binding site), **IPR050626** (Peptidase_M16), **IPR011844** (PQQ_synth_PqqF), Pfam **PF00675** (Peptidase_M16), and PROSITE **PS00143** (INSULINASE).

Sequence analysis of Q88QV3 confirms the **M16 "inverzincin" zinc-binding motif HxxEH** at positions 49–53 (**H49**-F-L-**E52**-**H53**), together with the distal catalytic **Glu130**. UniProt annotates Glu52 as the catalytic proton acceptor and His49/His53/Glu130 as metal-binding/catalytic residues. The associated Gene Ontology terms are **GO:0004222** (metalloendopeptidase activity) and **GO:0008270** (zinc ion binding). The HxxEH arrangement is the hallmark of the M16 clan (which includes insulin-degrading enzyme and pitrilysin): the two histidines and the glutamate of the motif ligate the catalytic Zn²⁺, while the motif's downstream glutamate acts as the general base — an "inverted" version of the more familiar HExxH thermolysin motif, hence *inverzincin*.

**Interpretation:** PqqF is a bona-fide zinc endopeptidase, mechanistically equipped to hydrolyze internal peptide bonds. This structural identity is the foundation for its assigned role as the PQQ-precursor excision protease.

### Finding 2 — PqqF excises the cross-linked Glu–Tyr precursor from the PqqA peptide

UniProt's function annotation (by similarity) states that PqqF is "*required for coenzyme pyrroloquinoline quinone (PQQ) biosynthesis... a protease that cleaves peptide bonds in a small peptide (gene pqqA), providing the glutamate and tyrosine residues which are necessary for the synthesis of PQQ.*" The protein is placed in the pathway "cofactor biosynthesis; PQQ biosynthesis" (**GO:0018189**, PQQ biosynthetic process).

This annotation is supported by direct mechanistic work from the Klinman laboratory. Martins et al. (2019) identified "*a protease/peptidase required for the excision of an early, cross-linked di-amino acid precursor to pyrroloquinoline quinone*" ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)). The authoritative 2020 review by Zhu & Klinman places this activity among the mechanistically characterized PQQ enzymes, "*focusing on the mechanisms of PqqE, PqqF/G, and PqqB*" ([PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)).

**Interpretation:** PqqF's precise reaction is the **hydrolytic excision of the PqqE-generated cross-linked Glu–Tyr unit** from the PqqA peptide backbone. Its substrate specificity is therefore narrow and pathway-dedicated: it recognizes the modified ribosomal peptide PqqA (or a PqqA-derived fragment) rather than acting as a general protein-degrading protease. This is a peptide-maturation step in a RiPP-like cofactor pathway.

### Finding 3 — In *P. putida* KT2440, *pqqF* leads the *pqqFABCDEG* cluster and its expression tracks PQQ output

An & Moe (2016) characterized the operon in the target organism itself: "*The pqq gene cluster (pqqFABCDEG) encodes at least two independent transcripts, and expression of the pqqF gene appears to be under the control of an independent promoter*," and critically, "*the levels of expression of the pqqF and pqqB genes mirror the levels of PQQ synthesized, suggesting that one or both of these genes may serve to modulate PQQ levels according to the growth conditions*" ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). The ordered locus **PP_0381** (*pqqF*) sits at the start of the cluster.

The functional requirement of *pqqF* for PQQ production is demonstrated genetically in the close relative *P. aeruginosa*: "*The putative pqqF gene of P. aeruginosa was shown to be essential for PQQ biosynthesis. A pqqF::Km(r) mutant did not grow aerobically on ethanol, because of its inability to produce PQQ*" ([PMID: 19902179](https://pubmed.ncbi.nlm.nih.gov/19902179/)).

**Interpretation:** *pqqF* is not only physically embedded in the PQQ operon of *P. putida* but is transcriptionally coupled to the flux of PQQ production, consistent with a rate-relevant, possibly regulatory, position at the head of the pathway. Loss of the orthologous gene abolishes PQQ synthesis, confirming it is functionally required (in Pseudomonads) rather than a redundant accessory.

### Finding 4 — PqqF acts in the cytoplasm; PQQ is later exported to the periplasm

Sequence analysis of the Q88QV3 N-terminus (MPDAIRQLTLANGLQLTLRH...) shows **no Sec/Tat signal peptide** — there is no N-terminal hydrophobic signal core, and UniProt provides no secretion annotation, classifying PqqF as a soluble metalloprotease. The other PQQ biosynthetic enzymes (PqqB–PqqE) are likewise cytoplasmic RiPP-processing enzymes that act on the ribosomally made PqqA peptide. The entire precursor-processing cascade therefore takes place in the **cytoplasm**.

The mature cofactor, by contrast, functions **extracytoplasmically**. Reviews and the An & Moe study describe PQQ as the coenzyme of the periplasmic/membrane-bound glucose dehydrogenase (Gcd). Two independent sources confirm the periplasmic location of PQQ-dependent chemistry: "*certain bacteria utilize membrane-bound dehydrogenases to oxidize glucose to gluconic acid (GA) in the periplasmic space*" with "PQQ-dependent" dehydrogenases ([PMID: 41494861](https://pubmed.ncbi.nlm.nih.gov/41494861/)), and "*strong organic acids produced in the periplasm via the direct oxidation pathway*" ([PMID: 12686144](https://pubmed.ncbi.nlm.nih.gov/12686144/)).

**Interpretation:** PqqF carries out its function in the cytoplasm (precursor manufacture), spatially separated from where the end-product acts (periplasm). This distinction is important for the annotation: the *enzyme's* localization is cytoplasmic even though the *pathway's output* is periplasmic.

### Finding 5 — PqqF is likely the catalytic subunit of a PqqF/PqqG two-component protease

The *P. putida* KT2440 cluster is *pqqFABCDEG* — it encodes both *pqqF* and a paralog *pqqG* ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). Martins et al. "*isolated and characterized a two-component heterodimer protein*" that supplies the protease/peptidase activity required for PQQ-precursor excision ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)), and the 2020 Klinman review names the activity "**PqqF/G**" ([PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)).

The domain architecture of Q88QV3 fits a bilobed M16 (pitrilysin/inverzincin) fold: an N-terminal catalytic lobe carrying the HxxEH49-53 motif plus Glu130, followed by C-terminal M16-type lobes. Structurally, M16 enzymes commonly function as two-domain "clamshells" that enclose the peptide substrate; a PqqF/PqqG heterodimer would reconstitute an analogous substrate-enclosing architecture. The AlphaFold DB model for Q88QV3 is of very high confidence (global pLDDT ≈ 91.75), consistent with a well-folded, ordered two-lobed protein.

**Interpretation:** PqqF is best understood as the **catalytic (Zn-bearing) component** of a two-component heterodimeric M16 protease, working together with PqqG to achieve precursor excision. This resolves an older ambiguity in which PqqF alone was assumed to be the whole enzyme.

### Finding 6 — PqqF belongs to a conserved, functionally interchangeable family of zinc proteases

Cross-species genetics establishes both the conservation and the interchangeability of PqqF-type proteases. Springer et al. (1996) reported that "*PqqE belongs to an endopeptidase family, including PqqF of Klebsiella pneumoniae*," and that *M. extorquens* AM1 *pqqE* complemented a *K. pneumoniae pqqF* mutant ([PMID: 8606199](https://pubmed.ncbi.nlm.nih.gov/8606199/)). Turlin et al. (1996) found that an *E. coli* chromosomal fragment complements *pqqE* and *pqqF* mutants of *Methylobacterium organophilum*; its ORF106 product "*shows homology with the pqqF gene product of K. pneumoniae, and seems to belong to a family of zinc proteases*" ([PMID: 9116051](https://pubmed.ncbi.nlm.nih.gov/9116051/)).

Consistent with this, many minimal *pqq* clusters (e.g., *pqqABCDE*) lack a dedicated *pqqF*, and the excision step can be provided in *trans* by other zinc proteases. In *Gluconobacter oxydans* 621H, a PQQ-deficient mutant mapped to a *tldD*-like peptidase gene, and the authors concluded *tldD* "*is involved in PQQ biosynthesis, possibly with a similar function to that of the pqqF genes found in other PQQ-synthesizing bacteria*" ([PMID: 16936032](https://pubmed.ncbi.nlm.nih.gov/16936032/)).

**Interpretation:** The excision protease role is evolutionarily conserved but not strictly gene-specific — it is a **modular zinc-protease function** that different bacteria have recruited from related M16/peptidase families. In *P. putida*, this function is carried by the dedicated *pqqF* (with *pqqG*).

### Finding 7 — The substrate PqqA in *P. putida* is a 23-residue peptide with conserved Glu15 and Tyr19

UniProt Q88QV4 (*pqqA*, *P. putida* KT2440) is a **23-amino-acid peptide** with sequence **MWTKPAYTDLRIGFEVTMYFANR**, containing the conserved **Glu (E15)** and **Tyr (Y19)**. PQQ is constructed from the cross-linked Glu + Tyr of PqqA: PqqE forms the Glu–Tyr C–C bond, and PqqF excises the cross-linked unit ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/); [PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)). The ~23-residue length is well within the short-peptide substrate preference typical of M16/pitrilysin peptidases, which favor peptides over folded proteins.

**Interpretation:** This defines the exact molecular substrate of PqqF in the target organism — a specific, short, cross-linked ribosomal peptide — and explains why an M16 clan enzyme (which handles short peptides in an enclosed active-site chamber) is the appropriate catalyst.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, well-supported model of PqqF as a peptide-maturation protease in PQQ cofactor biogenesis:

```
              CYTOPLASM (where PqqF works)
  ┌───────────────────────────────────────────────────────────┐
  │  pqqA gene ──► PqqA peptide (23 aa, ...E15...Y19...)        │
  │                        │                                    │
  │            PqqD (chaperone/presenter)                       │
  │                        │                                    │
  │            PqqE (radical-SAM) forms Glu–Tyr C–C cross-link  │
  │                        │                                    │
  │   ┌───────────────────────────────────────────────┐        │
  │   │  PqqF  (M16 Zn protease; HxxEH + Glu130)       │        │
  │   │  + PqqG  →  two-component heterodimer          │◄── this│
  │   │  EXCISES the cross-linked Glu–Tyr unit         │  report│
  │   └───────────────────────────────────────────────┘        │
  │                        │                                    │
  │            PqqB, PqqC  (cyclization + oxidation)            │
  │                        ▼                                    │
  │                    MATURE PQQ                               │
  └───────────────────────────────┬───────────────────────────┘
                                   │  export
                                   ▼
              PERIPLASM (where PQQ acts)
  ┌───────────────────────────────────────────────────────────┐
  │  PQQ-dependent glucose dehydrogenase (Gcd), quinoprotein   │
  │  alcohol/aldehyde dehydrogenases                           │
  │  glucose ──► gluconic acid (direct oxidation pathway)      │
  └───────────────────────────────────────────────────────────┘
```

**Catalytic logic.** PqqF is a Zn²⁺ metalloendopeptidase of the inverzincin (M16) clan. Its HxxEH motif (His49/Glu52/His53) plus Glu130 coordinate the catalytic zinc and polarize a water molecule for nucleophilic attack on the scissile peptide bond. In the PQQ pathway, the bonds to be cleaved flank the already-cross-linked Glu15–Tyr19 pair of PqqA, so hydrolysis **releases the di-amino-acid PQQ precursor** for downstream cyclization and oxidation.

**Enzyme vs. product localization.** A key nuance for annotation is that PqqF's site of action (cytoplasm) differs from the site of action of the pathway's end-product (periplasm). PqqF itself never reaches the periplasm; it is a soluble cytoplasmic protease. The value it creates — the PQQ precursor — becomes the cofactor that, once exported, powers periplasmic direct-oxidation metabolism (glucose → gluconic acid), which underlies *P. putida*'s phosphate-solubilizing, plant-growth-promoting phenotype.

**Quaternary organization.** The most current picture (Klinman group) is that the excision activity resides in a **PqqF/PqqG heterodimer**, with PqqF supplying the catalytic zinc center. This is consistent with the general M16 tendency to form two-lobed, substrate-enclosing architectures and with the presence of both *pqqF* and *pqqG* in the *P. putida* operon.

**Regulatory placement.** Because *pqqF* heads the operon under an independent promoter and its transcript level mirrors PQQ output, PqqF sits at a regulatorily meaningful node — its abundance may help set the ceiling on PQQ production according to carbon source and growth conditions.

| Feature | Assignment | Confidence | Basis |
|---|---|---|---|
| Molecular function | Zn²⁺ M16 metalloendopeptidase (EC 3.4.24.-) | High | Domains, motif, UniProt |
| Specific reaction | Excision of cross-linked Glu–Tyr from PqqA | High (by similarity + mechanistic studies) | PMID 31427437, 32731194 |
| Substrate | PqqA peptide (23 aa; E15/Y19) | High | UniProt Q88QV4; pathway logic |
| Quaternary state | Catalytic subunit of PqqF/PqqG heterodimer | Moderate–High | PMID 31427437, 27287323 |
| Localization (enzyme) | Cytoplasm (no signal peptide) | High | Sequence analysis |
| Localization (product action) | Periplasm | High | PMID 41494861, 12686144 |
| Pathway | PQQ cofactor biosynthesis | High | GO:0018189; operon context |
| Requirement for PQQ | Essential in *Pseudomonas* | High (ortholog) | PMID 19902179 |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Supports / Challenges |
|---|---|---|---|
| [31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/) | *A two-component protease…* | Identifies protease excising the cross-linked di-amino-acid PQQ precursor; a two-component heterodimer | **Supports** F2, F5, F7 (core mechanistic evidence) |
| [32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/) | *Biogenesis of the peptide-derived redox cofactor PQQ* | Authoritative review; names "PqqF/G" among characterized enzymes | **Supports** F2, F5, F7 |
| [27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/) | *Regulation of PQQ-dependent glucose dehydrogenase in P. putida KT2440* | Operon *pqqFABCDEG*; *pqqF* independent promoter; expression mirrors PQQ output | **Supports** F3, F5 (target-organism evidence) |
| [19902179](https://pubmed.ncbi.nlm.nih.gov/19902179/) | *PQQ biosynthetic operons in P. aeruginosa* | *pqqF* essential for PQQ; mutant cannot grow on ethanol | **Supports** F3 (functional requirement) |
| [8606199](https://pubmed.ncbi.nlm.nih.gov/8606199/) | *pqqE and pqqF in M. extorquens AM1* | Places PqqF in a conserved endopeptidase family; cross-complementation | **Supports** F6 |
| [9116051](https://pubmed.ncbi.nlm.nih.gov/9116051/) | *E. coli fragment complements pqqE/pqqF mutants* | PqqF homolog is a zinc protease; heterologous complementation | **Supports** F1, F6 |
| [16936032](https://pubmed.ncbi.nlm.nih.gov/16936032/) | *PQQ genes in G. oxydans 621H* | *tldD* peptidase substitutes for *pqqF* function | **Supports** F6 (interchangeability) |
| [41494861](https://pubmed.ncbi.nlm.nih.gov/41494861/) | *Bacterial glucose oxidation pathways* | PQQ-dependent dehydrogenases act in periplasm | **Supports** F4 (product localization) |
| [12686144](https://pubmed.ncbi.nlm.nih.gov/12686144/) | *Direct oxidation pathway / PQQ in E. coli* | Direct-oxidation acids produced in periplasm | **Supports** F4 |

**Databases:** UniProt Q88QV3 (protein), Q88QV4 (PqqA substrate); InterPro/Pfam/PROSITE domain signatures; AlphaFold DB model (pLDDT ≈ 91.75). Database annotations for PqqF's specific function are marked "by similarity," so they were treated as supporting rather than primary evidence and cross-checked against the experimental literature above.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* KT2440 enzyme.** The specific catalytic assignment for Q88QV3 rests on database annotation "by similarity" plus mechanistic work performed in *other* organisms (notably an alpha-proteobacterium in the Klinman studies and *Klebsiella/Methylobacterium* genetics). No purified-enzyme kinetic characterization of PP_0381 itself was located.

2. **PqqF vs. PqqG division of labor is not fully resolved.** While the excision activity is now attributed to a two-component PqqF/PqqG heterodimer, the exact catalytic contribution of each subunit — and whether PqqF alone retains partial activity — has not been dissected for the *P. putida* proteins.

3. **Exact cleavage sites unmapped.** The precise scissile bonds flanking Glu15–Tyr19 in *P. putida* PqqA, and any ordered/processive cleavage, have not been experimentally mapped for this organism.

4. **Structure is predicted, not experimental.** The bilobed M16 fold and high pLDDT come from AlphaFold; there is no experimental crystal/cryo-EM structure of the *P. putida* PqqF (or PqqF/PqqG complex) with substrate.

5. **Regulatory mechanism is correlative.** The observation that *pqqF* transcript level mirrors PQQ output is correlational; the upstream signals and transcription factors controlling the *pqqF* promoter in KT2440 are not defined.

6. **Redundancy in *P. putida* untested.** Whether a *tldD*-like or other host M16 protease can back up PqqF in *P. putida* (as *tldD* does in *G. oxydans*) has not been tested; the *P. aeruginosa* result suggests *pqqF* is essential, but this was not verified in KT2440.

---

## Proposed Follow-up Experiments / Actions

1. **In-vitro reconstitution.** Purify recombinant *P. putida* PqqF and PqqG, reconstitute the excision reaction on synthetic PqqE-cross-linked PqqA peptide, and confirm zinc-dependent cleavage by LC-MS. Determine kcat/Km and metal dependence (EDTA inhibition, Zn²⁺/Co²⁺ substitution).

2. **Active-site mutagenesis.** Mutate His49, Glu52, His53, and Glu130 (HxxEH + distal Glu) to Ala/Gln and test loss of protease activity and loss of PQQ production in vivo — directly validating the inverzincin mechanism for this enzyme.

3. **Cleavage-site mapping.** Use tandem MS / Edman sequencing on reaction products to define the exact peptide bonds hydrolyzed around Glu15–Tyr19 of *P. putida* PqqA.

4. **Genetic requirement in KT2440.** Construct a clean *pqqF* deletion in *P. putida* KT2440 and assay PQQ production, growth on glucose via the direct-oxidation (gluconate) pathway, and phosphate solubilization; complement with *pqqF* and with *pqqG* alone to test sufficiency.

5. **Complex characterization.** Determine the stoichiometry and structure of the PqqF/PqqG complex (SEC-MALS, cryo-EM), ideally with trapped substrate, to establish the substrate-enclosing architecture.

6. **Promoter/regulation dissection.** Map the independent *pqqF* promoter, identify regulators, and test whether *pqqF* dosage limits PQQ flux under different carbon sources.

7. **Redundancy test.** Screen the KT2440 genome for M16/*tldD*-like proteases and test whether any can substitute for PqqF, clarifying whether the excision step is uniquely PqqF-dependent in this organism.

---

## Conclusion

PqqF (PP_0381, Q88QV3) in *Pseudomonas putida* KT2440 is a **cytoplasmic, zinc-dependent M16-family (inverzincin) metalloendopeptidase** that functions as the **precursor-excision protease of pyrroloquinoline quinone (PQQ) biosynthesis**. Its primary catalytic act is hydrolyzing the ribosomal peptide **PqqA** to release the PqqE-generated **cross-linked Glu–Tyr** unit, the direct precursor of PQQ — most likely operating as the catalytic subunit of a **PqqF/PqqG two-component protease** encoded at the head of the *pqqFABCDEG* operon. The enzyme works in the cytoplasm; the PQQ cofactor it helps make is exported to the periplasm to serve quinoprotein dehydrogenases (notably glucose dehydrogenase) that drive direct-oxidation metabolism. The assignment is strongly supported by conserved domain architecture and by genetics and mechanistic studies across multiple bacteria, though direct biochemical characterization of the *P. putida* enzyme itself remains an open experimental target.


## Artifacts

- [OpenScientist final report](pqqF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pqqF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31427437
2. PMID:32731194
3. PMID:27287323
4. PMID:19902179
5. PMID:41494861
6. PMID:12686144
7. PMID:8606199
8. PMID:9116051
9. PMID:16936032