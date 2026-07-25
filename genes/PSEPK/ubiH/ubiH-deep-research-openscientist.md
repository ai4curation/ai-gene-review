---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:46.488014'
end_time: '2026-07-18T19:18:35.532422'
duration_seconds: 5089.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiH
  gene_symbol: ubiH
  uniprot_accession: Q88CI2
  protein_description: 'SubName: Full=2-octaprenyl-6-methoxyphenyl hydroxylase {ECO:0000313|EMBL:AAN70764.1};'
  gene_info: Name=ubiH {ECO:0000313|EMBL:AAN70764.1}; OrderedLocusNames=PP_5199 {ECO:0000313|EMBL:AAN70764.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiH/COQ6 family.
  protein_domains: FAD-bd. (IPR002938); FAD/NAD-bd_sf. (IPR036188); UbiH. (IPR011295);
    UbiH/COQ6. (IPR010971); UbiH/COQ6_monooxygenase. (IPR051205)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CI2
- **Protein Description:** SubName: Full=2-octaprenyl-6-methoxyphenyl hydroxylase {ECO:0000313|EMBL:AAN70764.1};
- **Gene Information:** Name=ubiH {ECO:0000313|EMBL:AAN70764.1}; OrderedLocusNames=PP_5199 {ECO:0000313|EMBL:AAN70764.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiH/COQ6 family.
- **Key Domains:** FAD-bd. (IPR002938); FAD/NAD-bd_sf. (IPR036188); UbiH. (IPR011295); UbiH/COQ6. (IPR010971); UbiH/COQ6_monooxygenase. (IPR051205)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiH** (gene ID: ubiH, UniProt: Q88CI2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: UbiH (Q88CI2 / PP_5199) in *Pseudomonas putida* KT2440

## Summary

**UbiH (UniProt Q88CI2; locus PP_5199) of *Pseudomonas putida* KT2440 is a flavin (FAD)-dependent, NAD(P)H- and O₂-consuming aromatic-ring monooxygenase that performs one of the three oxygenative hydroxylation steps in the biosynthesis of coenzyme Q (ubiquinone).** Its primary reaction is the *para* (C4) hydroxylation of the lipophilic quinone precursor, converting **2-polyprenyl-6-methoxyphenol → 2-polyprenyl-6-methoxy-1,4-benzoquinol**. Because *P. putida* synthesizes ubiquinone-9 (Q9), the physiological substrate carries a nonaprenyl tail rather than the octaprenyl tail found in *E. coli* (Q8) — hence the historical name "2-octaprenyl-6-methoxyphenyl hydroxylase." The enzyme uses a non-covalently bound FAD cofactor, molecular O₂, and NAD(P)H as reductant.

The functional assignment is secure. The gene is annotated as *ubiH* in UniProt, KEGG (ppu:PP_5199, orthology K03185, EC 1.14.13.-), and InterPro, the protein belongs to the UbiH/COQ6 monooxygenase family, and the *P. putida* protein is a genuine ortholog (51% amino-acid identity) of the biochemically characterized *E. coli* UbiH. The enzyme adopts the canonical **p-hydroxybenzoate hydroxylase (PHBH) fold** of single-component "class A" flavoprotein aromatic hydroxylases; its N-terminal region contains the diagnostic FAD/NAD(P)-binding Rossmann dinucleotide motif (GxGxxG, present as **GGGLVG** at residues 10–15 of Q88CI2).

Localization and pathway context: most ubiquinone-biosynthesis steps occur in the **bacterial cytosol**, where the Ubi enzymes assemble into a soluble multiprotein complex — the "Ubi metabolon" — that relies on lipid-binding accessory proteins (UbiJ/UbiK) to sequester the extremely hydrophobic polyprenyl-tailed intermediates. UbiH therefore acts as a soluble/peripheral cytoplasmic enzyme carrying out its chemistry on a membrane-partitioned lipid substrate at the cytoplasmic face of the inner membrane. Its product feeds forward toward mature coenzyme Q, the lipophilic electron/proton carrier of the aerobic respiratory chain. Consistent with a purely aerobic role, *ubiH*-type mutants are blocked in the O₂-dependent hydroxylation branch but can still make ubiquinone anaerobically via O₂-independent alternative hydroxylases.

---

## Key Findings

### Finding 1 — UbiH is the C4 (*para*) aromatic-ring hydroxylase of ubiquinone biosynthesis

UniProt Q88CI2 is annotated as "2-octaprenyl-6-methoxyphenyl hydroxylase," gene *ubiH*, in *P. putida* KT2440, and belongs to the UbiH/COQ6 family (InterPro IPR011295 "UbiH"; IPR010971 "UbiH/COQ6"). The functional assignment rests on the well-characterized *E. coli* ortholog. In *E. coli*, three of the ubiquinone-pathway reactions are hydroxylations that introduce hydroxyl groups at contiguous positions of the benzene nucleus, catalyzed by three flavin monooxygenases; **UbiH performs the C-4 (*para*) hydroxylation** ([PMID: 10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/)). The biosynthesis of ubiquinone requires exactly three hydroxylation reactions on contiguous positions of an aromatic ring ([PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)).

The specific transformation is **2-polyprenyl-6-methoxyphenol → 2-polyprenyl-6-methoxy-1,4-benzoquinol**: introduction of the *para* hydroxyl converts the mono-phenol into a 1,4-dihydroxy (hydroquinone) ring. In *E. coli* the substrate is the octaprenyl homolog; in *P. putida*, which produces Q9, the substrate carries a nonaprenyl tail. Substrate specificity is defined by (i) the methoxy/prenyl-substituted phenolic ring recognized in the active site and (ii) the long polyisoprenoid tail, which is accommodated and sequestered by the pathway's lipid-binding accessory proteins rather than fully buried in the monooxygenase. This answers the central "what reaction is catalyzed" question: an FAD-dependent, regioselective *para*-hydroxylation of a polyprenylated methoxyphenol intermediate.

> *"Three of these reactions involve hydroxylations resulting in the introduction of hydroxyl groups at positions C-6, C-4, and C-5 of the benzene nucleus of Q. The genes encoding the enzymes responsible for these hydroxylations, ubiB, ubiH, and ubiF"* — [PMID: 10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/)
>
> *"The biosynthesis of UQ requires three hydroxylation reactions on contiguous positions of an aromatic ring."* — [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)

### Finding 2 — UbiH is an FAD-dependent (class A) monooxygenase of the PHBH structural family, using O₂ and NAD(P)H

Q88CI2 carries FAD-binding domains (InterPro IPR002938 "FAD-bd"; IPR036188 "FAD/NAD(P)-binding superfamily") and is a member of the UbiH/COQ6 monooxygenase family (IPR051205). The structural template is established: the related Q-biosynthesis monooxygenase **UbiI was crystallized and shown to share the canonical FAD-dependent p-hydroxybenzoate hydroxylase (PHBH) fold**, with a flavin-binding pocket essential for activity — the first structural characterization of a monooxygenase in Q biosynthesis ([PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)).

Mechanistically, such enzymes reduce the bound FAD with NAD(P)H, react the reduced flavin with molecular O₂ to form a **C4a-(hydro)peroxyflavin** intermediate, and use this reactive oxygen species for electrophilic aromatic hydroxylation — explaining the enzyme's strict **oxygen dependence**. One atom of O₂ is incorporated into the product hydroxyl; the other is reduced to water. This aerobic dependence is demonstrated genetically: mutants blocked in any of the three aerobic hydroxylation reactions (*ubiB*, *ubiH*, or *ubiF*) can still synthesize ubiquinone anaerobically, because O₂-independent alternative hydroxylases substitute for them under anoxic conditions ([PMID: 365223](https://pubmed.ncbi.nlm.nih.gov/365223/)). This places UbiH firmly in the O₂-dependent (aerobic) branch and identifies its co-substrates as molecular oxygen and NAD(P)H.

> *"This structure shares many features with the canonical FAD-dependent para-hydroxybenzoate hydroxylase and represents the first structural characterization of a monooxygenase involved in Q biosynthesis."* — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)
>
> *"mutants blocked in either of the three hydroxylation reactions of the aerobic pathway (ubiB, ubiH, or ubiF) are each able to synthesize ubiquinone 8 anaerobically"* — [PMID: 365223](https://pubmed.ncbi.nlm.nih.gov/365223/)

### Finding 3 — Sequence-level evidence: Q88CI2 carries the N-terminal FAD-binding dinucleotide motif of class A flavoprotein hydroxylases

The UniProt Q88CI2 sequence (399 aa; header confirms "2-octaprenyl-6-methoxyphenyl hydroxylase … GN=ubiH … *Pseudomonas putida* KT2440") begins **MSRVNLAIIGGGLVGASLALALQAGA…**, containing the canonical FAD/NAD(P)-binding Rossmann dinucleotide-binding motif **GxGxxG** (present as **GGGLVG** at residues 10–15). This βαβ fingerprint is the ADP-of-FAD binding signature shared by the PHBH family of single-component FAD-dependent aromatic monooxygenases. It is fully consistent with the InterPro annotations IPR002938 (FAD-binding), IPR036188 (FAD/NAD(P)-binding superfamily), IPR011295 (UbiH), IPR010971 (UbiH/COQ6), and IPR051205 (UbiH/COQ6 monooxygenase). The direct presence of this motif in the target sequence provides independent, bioinformatic corroboration of the cofactor requirement inferred from family membership.

### Finding 4 — Q88CI2 is a bona fide ortholog of biochemically characterized *E. coli* UbiH (51% identity)

A global (Needleman–Wunsch) alignment of the full-length target Q88CI2 (399 aa) against *E. coli* UBIH_ECOLI (P25534, 392 aa, "2-octaprenyl-6-methoxyphenol hydroxylase") gives **185/362 = 51.1% amino-acid identity** over the aligned length. The same target aligns to the family paralog UbiI (P25535, "2-octaprenylphenol hydroxylase") at only **165/364 = 45.3% identity**.

| Comparison | Identity | Aligned length | Interpretation |
|---|---|---|---|
| Q88CI2 vs *E. coli* **UbiH** (P25534) | **51.1%** | 362 aa | True ortholog — direct functional transfer justified |
| Q88CI2 vs *E. coli* **UbiI** (P25535) | 45.3% | 364 aa | Paralog — same family, different regioselectivity |

The higher similarity to UbiH than to the paralogous ring-hydroxylase UbiI, combined with >50% full-length identity (well above the ~25–30% "twilight zone" of ambiguous homology), indicates **true orthology rather than mere family membership**. This is the strongest single piece of evidence permitting direct transfer of the experimentally established *E. coli* UbiH function (C4 *para*-hydroxylation) to the *P. putida* protein.

### Finding 5 — Conservation is uniform across FAD-binding and substrate-binding regions, supporting conserved substrate specificity

Regional identity from the global pairwise alignment of Q88CI2 vs *E. coli* UbiH (P25534):

| Region | Approx. residues | Role in PHBH-family enzymes | Identity |
|---|---|---|---|
| N-terminal third | ~1–133 | FAD dinucleotide binding | 50.4% |
| Middle third | ~134–266 | Core / linker | 49.2% |
| C-terminal third | ~267–399 | Aromatic-substrate pocket / dimerization | **53.8%** |

Conservation is thus **not restricted to the cofactor-binding module** but is in fact slightly *higher* in the C-terminal region that, in PHBH-family monooxygenases, forms the aromatic-substrate binding pocket. Because the substrate-recognition machinery is retained at least as strongly as the cofactor machinery, the *P. putida* enzyme is predicted to have the **same substrate specificity and regioselectivity** as *E. coli* UbiH — the C4 hydroxylation of 2-polyprenyl-6-methoxyphenol, not merely generic hydroxylase chemistry. The diagnostic N-terminal GxGxxG (GGGLVG) FAD motif is present as expected.

### Finding 6 — UbiH acts in the cytosolic Ubi metabolon on a membrane-embedded lipophilic substrate

Most steps of ubiquinone biosynthesis take place in the **bacterial cytosol**, where the Ubi enzymes assemble into a soluble multiprotein complex — the "Ubi metabolon." This assembly requires the accessory proteins **UbiJ** (bearing an SCP2 lipid-binding domain) and **UbiK** to sequester the polyprenyl-tailed intermediates, which are otherwise too hydrophobic to remain in solution ([PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/); [PMID: 38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/)). UbiH is therefore a **soluble/peripheral cytoplasmic enzyme** (not an integral membrane protein) that carries out its chemistry on a membrane-partitioned lipid substrate at the **cytoplasmic face of the inner membrane** within this complex.

In flux terms, UbiH functions as a downstream-pulling step: in *Rhodobacter sphaeroides*, co-overexpression of UbiH relieved accumulation of an upstream intermediate and increased CoQ10 yield, demonstrating that UbiH activity pulls metabolic flux toward downstream CoQ intermediates ([PMID: 25817210](https://pubmed.ncbi.nlm.nih.gov/25817210/)). This answers the "where does the gene product act" question: it is a soluble, cytosolic enzyme operating on a membrane-partitioned lipid at the inner-membrane interface as part of a defined biosynthetic complex, and its end product, coenzyme Q, is the central lipophilic electron/proton carrier of the aerobic respiratory chain.

> *"Most steps of UQ biosynthesis take place in the cytosol of..."* — [PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/)
>
> *"UbiH was then co-overexpressed to pull the metabolic flux towards downstream..."* — [PMID: 25817210](https://pubmed.ncbi.nlm.nih.gov/25817210/)

### Finding 7 — KEGG confirms the assignment and places PP_5199 in a complete *P. putida* ubiquinone pathway

The KEGG entry for **ppu:PP_5199** assigns ORTHOLOGY **K03185** "2-octaprenyl-6-methoxyphenol hydroxylase [EC:1.14.13.-]"; PATHWAY **ppu00130** (Ubiquinone and other terpenoid-quinone biosynthesis); MODULE **ppu_M00117** (Ubiquinone biosynthesis, prokaryotes: chorismate + polyprenyl-PP ⇒ ubiquinol); and MOTIF Pfam **FAD_binding_3 (PF01494)** — the PHBH-family FAD-binding domain. The EC class **1.14.13.-** denotes an NAD(P)H- and O₂-dependent monooxygenase, consistent with the mechanism in Finding 2.

Genomic-neighborhood analysis (POSITION complement 5930870..5932069) shows PP_5199 (*ubiH*) flanked by **PP_5197** (K18800/*ubiV*, "oxidoreductase involved in anaerobic synthesis of ubiquinone") and PP_5198 (a small conserved protein of unknown function), with *pepP* (PP_5200) beyond. This adjacency of the aerobic UbiH to the O₂-independent (anaerobic) hydroxylase *ubiV* mirrors the two-branch aerobic/anaerobic ring-hydroxylation system. Importantly, *P. putida* also encodes a **complete Ubi pathway** elsewhere in the genome: *ubiA* (PP_5318), *ubiD/ubiX* (PP_5213/PP_5317), *ubiE* (PP_5011), *ubiC* (PP_5013), plus additional UbiF-type monooxygenases (PP_0427, PP_0548). The presence of a full, functional Ubi gene set confirms that PP_5199 is a committed, non-redundant step in an active coenzyme-Q biosynthetic route, not an orphan gene.

---

## Mechanistic Model / Interpretation

### Position of UbiH in the ubiquinone biosynthetic pathway

Ubiquinone biosynthesis in proteobacteria proceeds from **chorismate** (via 4-hydroxybenzoate, 4-HB) and a **polyprenyl-diphosphate** tail (nonaprenyl-PP in *P. putida*). The aromatic ring is prenylated (UbiA), decarboxylated (UbiD/UbiX), and then subjected to alternating **hydroxylation** (Ubi monooxygenases) and **O-/C-methylation** (UbiG/UbiE) steps that decorate the ring into the final ubiquinone quinone head group. UbiH performs the **C4 (*para*) hydroxylation**, one of the three contiguous ring hydroxylations:

```
Chorismate ──> 4-hydroxybenzoate (4-HB)
                     │  UbiA (prenylation, adds C45 nonaprenyl tail)
                     ▼
        3-nonaprenyl-4-hydroxybenzoate
                     │  UbiD / UbiX (decarboxylation)
                     ▼
             2-nonaprenylphenol
                     │  UbiI-type (ring hydroxylation, O2)
                     ▼
        2-nonaprenyl-6-hydroxyphenol
                     │  UbiG (O-methylation)
                     ▼
        2-nonaprenyl-6-methoxyphenol   ◄── UbiH SUBSTRATE
                     │  ****  UbiH  ****  (C4 / para hydroxylation; O2 + NAD(P)H; FAD)
                     ▼
   2-nonaprenyl-6-methoxy-1,4-benzoquinol   ◄── UbiH PRODUCT
                     │  UbiE (C-methylation)
                     ▼
                     │  UbiF-type (ring hydroxylation, O2)  +  UbiG (O-methylation)
                     ▼
              Ubiquinol-9 (reduced Q9)  ⇌  Ubiquinone-9 (Q9)
```

*(Intermediate order follows the E. coli paradigm; the P. putida homologs carry a nonaprenyl rather than octaprenyl tail because the organism makes Q9. Regioselectivity nomenclature (C1/C4/C5/C6) varies between older and revised models, but the transformation mono-phenol → 1,4-benzoquinol is unambiguous.)*

### Catalytic cycle (class A flavoprotein monooxygenase / PHBH paradigm)

```
   NAD(P)H ──► reduces bound FAD ──► FADH⁻
                                       │
                                       │ + O2
                                       ▼
                            C4a-(hydro)peroxyflavin
                                       │  electrophilic aromatic
                                       │  hydroxylation at ring C4
                                       ▼
     product-OH  +  C4a-hydroxyflavin ──► dehydration ──► oxidized FAD + H2O
```

### Localization and supramolecular organization

```
        CYTOPLASM
   ┌───────────────────────────────────────────────┐
   │   Ubi metabolon (soluble multiprotein complex) │
   │   UbiE UbiF UbiG UbiH UbiI ...                  │
   │        │      + UbiJ (SCP2 lipid carrier)       │
   │        │      + UbiK                            │
   │        ▼                                        │
   │   UbiH acts on lipid substrate held by UbiJ    │
   └────────┼───────────────────────────────────────┘
    ~~~~~~~~▼~~~~~~~ cytoplasmic face ~~~~~~~~~~~~~~~~
   ████████████ INNER MEMBRANE ████████████████████
        (polyprenyl-tailed intermediate partitions here;
         mature Q9 becomes the respiratory-chain quinone)
```

### Summary annotation table

| Attribute | Assignment | Confidence |
|---|---|---|
| **Primary function** | FAD-dependent aromatic *para* (C4) monooxygenase | High |
| **Reaction** | 2-nonaprenyl-6-methoxyphenol → 2-nonaprenyl-6-methoxy-1,4-benzoquinol | High |
| **Co-substrates / cofactor** | O₂, NAD(P)H; non-covalent FAD | High |
| **EC number** | 1.14.13.- | High (KEGG K03185) |
| **Pathway** | Ubiquinone (coenzyme Q9) biosynthesis, aerobic branch | High |
| **Localization** | Cytosol / cytoplasmic face of inner membrane (Ubi metabolon) | Medium–High |
| **Substrate specificity** | Polyprenyl-methoxyphenol; conserved with *E. coli* UbiH | Medium–High (inferred from orthology) |
| **Structural fold** | p-hydroxybenzoate hydroxylase (PHBH) fold | High (by homology) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/) | *Ubiquinone biosynthesis in E. coli: identification of ubiF* | Assigns UbiH to the C-4 (*para*) aromatic-ring hydroxylation; names the three ring hydroxylases of the Q pathway (Finding 1). |
| [27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/) | *Evolution of Ubiquinone Biosynthesis…* | Establishes that UQ biosynthesis needs three hydroxylations on contiguous ring positions; frames family regioselectivity (Findings 1, 5). |
| [23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/) | *ubiI, a new gene in E. coli CoQ biosynthesis…* | First crystal structure of a Q-pathway monooxygenase (UbiI); shows the PHBH FAD-dependent fold shared by UbiH-family enzymes (Finding 2). |
| [365223](https://pubmed.ncbi.nlm.nih.gov/365223/) | *Alternative hydroxylases for aerobic/anaerobic UQ biosynthesis* | Demonstrates UbiH functions in the O₂-dependent aerobic branch; anaerobic alternatives replace it without O₂ (Finding 2). |
| [36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/) | *Functional Role of UbiJ–UbiK…* | Localizes the Ubi enzymes to the cytosol and defines the soluble Ubi metabolon requiring lipid-binding accessory proteins (Finding 6). |
| [38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/) | *Structural Reconstruction of the Ubi complex* | Supports the metabolon model and sequestration of hydrophobic intermediates (Finding 6). |
| [25817210](https://pubmed.ncbi.nlm.nih.gov/25817210/) | *Metabolic bottlenecks for CoQ10 in R. sphaeroides* | Shows UbiH overexpression pulls flux toward downstream CoQ intermediates, confirming its on-pathway position (Finding 6). |
| [7032590](https://pubmed.ncbi.nlm.nih.gov/7032590/) | *Respiratory mutant of E. coli with reduced aminoglycoside uptake* | Illustrates the respiratory consequences of defective ubiquinone ring modification (physiological context). |

Supplementary database evidence (KEGG, UniProt, InterPro, Pfam) underpins Findings 3, 4, 5, and 7: the KEGG ortholog assignment K03185/EC 1.14.13.-, the InterPro/Pfam FAD-binding and UbiH/COQ6 domain annotations, the presence of the GGGLVG FAD motif in the target sequence, and the 51% ortholog-level identity to *E. coli* UbiH derived from pairwise global alignment.

---

## Supported and Refuted Hypotheses

**Supported**

- **H1** — UbiH is an enzyme (monooxygenase), not a transporter/structural protein — *supported* (family, domains, sequence motif, biochemical literature).
- **H2** — UbiH catalyzes a specific aromatic C4/*para* hydroxylation in Q biosynthesis — *supported* ([PMID: 10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/); [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)).
- **H3** — UbiH is FAD-dependent, O₂- and NAD(P)H-utilizing, PHBH-fold — *supported* ([PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/); sequence Rossmann motif; anaerobic bypass in [PMID: 365223](https://pubmed.ncbi.nlm.nih.gov/365223/)).
- **H4** — UbiH functions in the cytosol/Ubi metabolon on a lipid substrate — *supported* ([PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/); [PMID: 38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/)).

**Refuted / ruled out**

- UbiH is **not** an oxygen-independent enzyme — anaerobic Q synthesis proceeds via distinct alternative hydroxylases ([PMID: 365223](https://pubmed.ncbi.nlm.nih.gov/365223/)).
- UbiH is **not** an integral inner-membrane transporter or a menaquinone-pathway enzyme; it is a cytosolic flavoprotein specific to the ubiquinone ring-modification steps.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* protein.** The functional assignment for Q88CI2 rests on orthology transfer (51% identity to *E. coli* UbiH) and domain/family membership rather than on purified-enzyme assays of PP_5199 itself. No published kinetic constants (Km, kcat), substrate-range data, or in-vitro reconstitution exist specifically for the *P. putida* enzyme.

2. **No experimental structure.** The PHBH-fold assignment is inferred from the UbiI crystal structure and sequence homology; there is no experimental 3D structure of Q88CI2 confirming the flavin pocket and substrate channel.

3. **Substrate tail length inferred, not measured.** The nonaprenyl (Q9) substrate is inferred from *P. putida*'s known quinone content; the exact intermediate handled by PP_5199 has not been directly identified in this strain.

4. **Regioselectivity edge cases.** The UbiH/UbiF/UbiI family shows documented plasticity in regioselectivity across proteobacteria ([PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)). While the high C-terminal conservation argues for a conserved C4 specificity, cross-complementation has not been demonstrated for the *P. putida* protein specifically. Regioselectivity nomenclature (C1/C4 conventions) also varies between older and revised models.

5. **Localization details.** The cytosolic/metabolon localization is established for *E. coli*; whether *P. putida* assembles an identical UbiJ/UbiK-dependent complex is assumed by homology, not directly shown. *P. putida* UbiK/UbiJ orthology was not separately verified.

6. **Genomic-context nuance.** PP_5199 lies adjacent to *ubiV* (anaerobic UQ synthesis) rather than in an operon with the canonical aerobic *ubi* genes, which are dispersed across the genome. The regulatory logic of this arrangement was not explored.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic complementation.** Test whether cloned *P. putida* PP_5199 restores ubiquinone synthesis and aerobic respiratory growth in an *E. coli ΔubiH* mutant (succinate-oxidation / growth-on-nonfermentable-carbon phenotype). This would directly confirm functional equivalence.

2. **In-vitro enzymology.** Heterologously express and purify Q88CI2, reconstitute with FAD, and assay *para*-hydroxylation of a synthetic 2-prenyl-6-methoxyphenol analog in the presence of O₂ and NAD(P)H. Measure Km/kcat and confirm C4 regioselectivity by MS/NMR of the product.

3. **Structural determination or high-confidence modeling.** Obtain an AlphaFold model (or crystal structure) of Q88CI2, verify the PHBH fold, dock the polyprenyl-methoxyphenol substrate, and identify active-site residues; compare with the UbiI structure ([PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)).

4. **Knockout phenotyping in *P. putida* KT2440.** Delete PP_5199 and quantify ubiquinone-9 levels, accumulation of the expected upstream intermediate (2-nonaprenyl-6-methoxyphenol), and aerobic vs. anaerobic respiratory competence.

5. **Metabolon verification.** Test for co-assembly of PP_5199 with *P. putida* UbiJ/UbiK orthologs (co-purification / crosslinking) to confirm the cytosolic-metabolon localization model in this organism.

6. **Regioselectivity mapping.** Given family plasticity, perform structure-guided mutagenesis of the C-terminal substrate-pocket residues to test whether specificity/regioselectivity can be switched, informing the evolutionary framework of [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/).

---

## Gene-Identity Verification Statement

The gene symbol **ubiH** matches the UniProt protein description ("2-octaprenyl-6-methoxyphenyl hydroxylase"), the organism (*Pseudomonas putida* KT2440), the locus (PP_5199), the family (UbiH/COQ6), and the FAD-binding domain architecture. These are consistent across UniProt, KEGG (ppu:PP_5199, K03185), and the sequence header. The literature retrieved concerns the same UbiH/coenzyme-Q system across proteobacteria; **no evidence of an unrelated same-symbol gene was found.** Function was transferred to the *P. putida* protein on the basis of demonstrated orthology (51% identity to biochemically characterized *E. coli* UbiH), not merely a shared symbol. The annotation is therefore made on the correct protein and is judged secure.

### Cited References

- Kwon, Kotsakis & Meganathan (2000) *J Bacteriol.* — [PMID: 10802164](https://pubmed.ncbi.nlm.nih.gov/10802164/)
- Pelosi et al. (2016) *mBio.* — [PMID: 27822549](https://pubmed.ncbi.nlm.nih.gov/27822549/)
- Hajj Chehade et al. (2013) *J Biol Chem.* — [PMID: 23709220](https://pubmed.ncbi.nlm.nih.gov/23709220/)
- Alexander & Young (1978) *J Bacteriol.* — [PMID: 365223](https://pubmed.ncbi.nlm.nih.gov/365223/)
- Lu et al. (2015) *Metab Eng.* — [PMID: 25817210](https://pubmed.ncbi.nlm.nih.gov/25817210/)
- Launay et al. (2022) — [PMID: 36142227](https://pubmed.ncbi.nlm.nih.gov/36142227/); Launay et al. (2024) — [PMID: 38710096](https://pubmed.ncbi.nlm.nih.gov/38710096/)
- Muir, Hanwell & Wallace (1981) — [PMID: 7032590](https://pubmed.ncbi.nlm.nih.gov/7032590/)


## Artifacts

- [OpenScientist final report](ubiH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10802164
2. PMID:27822549
3. PMID:23709220
4. PMID:36142227
5. PMID:38710096
6. PMID:25817210
7. PMID:7032590