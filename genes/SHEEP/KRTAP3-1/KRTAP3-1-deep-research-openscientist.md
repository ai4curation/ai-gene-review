---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:27:41.874731'
end_time: '2026-10-24T17:56:46.834384'
duration_seconds: 1744.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SHEEP
  gene_id: KRTAP3-1
  gene_symbol: KRTAP3-1
  uniprot_accession: P02446
  protein_description: 'RecName: Full=Keratin-associated protein 3-1; AltName: Full=Keratin,
    high sulfur matrix protein, IIIB2;'
  gene_info: Name=KRTAP3-1;
  organism_full: Ovis aries (Sheep).
  protein_family: Belongs to the KRTAP type 3 family. .
  protein_domains: Keratin_matx. (IPR007659); Keratin_matx (PF04579)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KRTAP3-1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KRTAP3-1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P02446
- **Protein Description:** RecName: Full=Keratin-associated protein 3-1; AltName: Full=Keratin, high sulfur matrix protein, IIIB2;
- **Gene Information:** Name=KRTAP3-1;
- **Organism (full):** Ovis aries (Sheep).
- **Protein Family:** Belongs to the KRTAP type 3 family. .
- **Key Domains:** Keratin_matx. (IPR007659); Keratin_matx (PF04579)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KRTAP3-1" matches the protein description above**
2. **Verify the organism is correct:** Ovis aries (Sheep).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KRTAP3-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KRTAP3-1** (gene ID: KRTAP3-1, UniProt: P02446) in SHEEP.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KRTAP3-1 (Keratin-Associated Protein 3-1) in Sheep — Functional Annotation Report

**Gene:** KRTAP3-1 · **UniProt:** [P02446](https://www.uniprot.org/uniprotkb/P02446) · **Organism:** *Ovis aries* (Sheep)
**Protein family:** KRTAP type 3 (high-sulfur / high-cysteine class) · **Domain:** Keratin_matx (Pfam [PF04579](https://www.ebi.ac.uk/interpro/entry/pfam/PF04579/); InterPro IPR007659)
**Classical names:** wool high-sulfur matrix protein IIIB2; SCMKB-IIIB2; SCMK-B2C

---

## Summary

Sheep **KRTAP3-1** encodes the classical wool **high-sulfur matrix protein IIIB2** (also historically designated SCMKB-IIIB2 / SCMK-B2C), a small, cysteine-rich **structural protein**, not an enzyme, transporter, receptor, or signaling molecule. The mature protein is 98 amino acids long and extraordinarily rich in cysteine (16.3%, 16 of 98 residues), proline (13.3%), threonine (10.2%), and serine (9.2%) — the hallmark compositional signature of the high-sulfur (HS) keratin-associated protein (KAP/KRTAP) class. It was one of the earliest wool proteins to be purified and directly protein-sequenced from reduced merino wool, and it belongs to the KRTAP type 3 family defined by the Keratin_matx domain.

The **primary function** of KRTAP3-1 is to serve as a **disulfide cross-linking component of the interfilamentous matrix** of the wool-fibre cortex. In terminally differentiating cortical trichocytes of the anagen wool follicle, keratin intermediate filaments (KIFs, the α-keratin microfibrils) become embedded in a dense matrix of keratin-associated proteins. KRTAP3-1 uses its abundant cysteine residues — many arranged as CC doublets and C-x-C / C-x-x-C motifs within internal sequence repeats — to form extensive intra- and inter-molecular disulfide (cystine) bonds that cross-link adjacent keratin filaments, bundle them into macrofibrils, and rigidify the fibre. This covalent cross-linking is the molecular basis of wool's mechanical strength, hardness, insolubility, and resistance to chemical and microbial degradation.

KRTAP3-1 carries out its role **intracellularly, within the keratinizing cortical cells of the wool fibre**, where it is deposited during cortical keratinization with a bias toward the **paracortex**. Its biological context is trichocyte terminal differentiation and wool-fibre formation, not any metabolic or signal-transduction pathway. At the genome level it is a small, single-ORF gene residing in a tandem high-sulfur KAP cluster on sheep chromosome 11, and it belongs to a gene family shaped by **concerted evolution and frequent gene conversion**. Variation within the high-sulfur KAP class, including the KAP3 proteins, is a major contributor to breed- and individual-level variation in wool fibre traits, making these genes candidate markers for wool quality.

---

## Gene / Protein Identity Verification

Before presenting findings, the mandatory identity checks were completed and all align:

| Verification item | Result |
|---|---|
| Gene symbol matches protein description | ✅ KRTAP3-1 = "Keratin-associated protein 3-1 / Keratin, high sulfur matrix protein, IIIB2" |
| Organism correct | ✅ *Ovis aries* (Sheep) — protein directly sequenced from merino wool |
| Protein family/domain aligns with literature | ✅ KRTAP type 3, high-sulfur class; Keratin_matx domain (PF04579 / IPR007659) consistent with wool matrix KAP literature |
| Risk of same-symbol confusion in another organism | Low — the directly-sequenced ovine wool protein (SCMKB-IIIB2 / B2C) is unambiguously this entry |

The literature located is specific and consistent with this protein; no mis-identification with a different same-symbol gene occurred. The amino-acid composition independently computed from P02446 matches the published high-sulfur wool protein signature, reinforcing the identification.

---

## Key Findings

### F001 — KRTAP3-1 is a high-sulfur keratin-associated matrix protein of sheep wool

KRTAP3-1 is the gene for the classical wool high-sulfur protein historically known as **IIIB2 / SCMKB-IIIB2**, one of the best-characterised members of the high-sulfur wool protein fraction. UniProt entry P02446 records a 98-residue protein that was **directly protein-sequenced** from the reduced and carboxymethylated high-sulfur fraction of merino wool — first as SCMKB-IIIB2 (1969) and subsequently as SCMK-B2C by Elleman (*Biochem J*, 1972). This places KRTAP3-1 among the earliest wool proteins to have its primary structure fully determined, well before the genomic era.

The amino-acid composition computed directly from the P02446 sequence confirms the diagnostic high-sulfur signature: **cysteine 16.3% (16/98)**, **proline 13.3%**, **threonine 10.2%**, and **serine 9.2%**. This cysteine/proline-rich composition is the defining chemical fingerprint of the high-sulfur (HS) KAP class, distinguishing it from the high-glycine-tyrosine (HGT) class of matrix proteins. The protein belongs to the KRTAP type 3 family (Pfam PF04579 "Keratin_matx"; InterPro IPR007659), and the UniProt keywords ("Direct protein sequencing", "Keratin", "Repeat") summarise its experimental provenance and internal repeat architecture.

> *"The amino acid sequence of a protein from the reduced and carboxymethylated high-sulphur fraction of wool has been determined."* — Elleman, [PMID: 4678578](https://pubmed.ncbi.nlm.nih.gov/4678578/)

### F002 — Primary function: disulfide cross-linking of keratin intermediate filaments in the wool cortex matrix

The **primary function** of KRTAP3-1 is structural and covalent: it cross-links keratin intermediate filaments via disulfide bonds. In the wool cortex, the α-keratin intermediate filaments (KIFs/microfibrils) are embedded in an **interfilamentous matrix** built from keratin-associated proteins. These KAPs are essential for forming a rigid, degradation-resistant wool shaft, achieved through extensive disulfide cross-linking between their cysteine residues and those of the wool keratins. UniProt's FUNCTION and SUBUNIT annotations for P02446 state exactly this: the protein participates in the matrix that cross-links KIFs and "interacts with wool keratins."

Two authoritative reviews make the mechanism explicit. Wu & Irwin (2018) state that **"KRTAPs form the interfilamentous matrix between intermediate filament bundles through extensive disulfide bond cross-linking with the numerous cysteine residues in hair keratins"** ([PMID: 29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/)). Fraser & Parry (2018) describe how KAPs "infiltrate the space between the IF" and have especially important roles "in the organisation of the IF into macrofibrils… and in linking IF to one another, either directly or indirectly, with a resultant increase in durability and resistance to degradation by microorganisms," with their conformations "stabilized predominantly by intramolecular disulfide bonds" ([PMID: 29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/)).

Thus KRTAP3-1 is best understood as a **molecular "disulfide glue"**: its multivalent cysteines form cystine bridges that tie neighbouring keratin filaments together and lock the matrix into a cohesive, hardened composite. There is no catalytic reaction, no transported substrate, and no ligand-receptor signaling role — the function is purely structural cross-linking.

### F003 — Localization: interfilamentous matrix of wool cortical cells; follicle/anagen-specific expression

KRTAP3-1 performs its function **intracellularly, within the cortical cells of the wool fibre**, as a fixed component of the interfilamentous matrix. UniProt lists tissue specificity as "Wool" and the GO cellular component "keratin filament" (GO:0045095). Flanagan, Plowman & Bryson (2002) state directly that **"High sulphur proteins (HSPs) form part of the matrix surrounding the intermediate filaments in the cortical cells of the wool fibre"** ([PMID: 12362341](https://pubmed.ncbi.nlm.nih.gov/12362341/)), which localises the high-sulfur KAP class (including KAP3) to the matrix around KIFs in cortical cells.

Expression is **developmentally restricted to the actively growing (anagen) wool follicle**. Rufaut et al. (1999) showed that the paralogue KRTAP3.2 is expressed in wool follicles and is down-regulated in telogen relative to anagen, with in situ localisation to cells that are absent in telogen; they concluded that **"KRTAP3.2 and Dsg1 both play structural roles in hair follicles"** ([PMID: 10594723](https://pubmed.ncbi.nlm.nih.gov/10594723/)). This confirms that the KRTAP3 family consists of follicle-expressed, anagen-associated structural proteins deposited during active fibre synthesis. Once the cortical cell keratinizes and dies, the deposited KRTAP3-1 becomes a permanent, insoluble structural component of the mature fibre.

### F004 — Member of a gene class that evolved by concerted evolution and gene conversion

KRTAP3-1 belongs to the **high-sulfur (high-cysteine) KRTAP class**, part of a large mammalian gene family of roughly 100–180 genes split into high/ultrahigh-cysteine (HS/UHS) and high-glycine-tyrosine (HGT) subfamilies. The evolutionary mode of the high-cysteine class is distinctive. Wu, Irwin & Zhang (2008) found that **"Genes in many subfamilies of the high/ultrahigh cysteine KRTAP genes have evolved by concerted evolution with frequent gene conversion events, yielding a higher GC base content for these gene sequences"** ([PMID: 18721477](https://pubmed.ncbi.nlm.nih.gov/18721477/)).

A broad comparative-genomics study across 22 genomes by Khan et al. (2014) reinforced this, reporting that **"the high cysteine (HS) subfamily experienced strong concerted evolution, high rates of gene conversion/recombination and high GC content"**, and that species with more hair and of higher complexity tended to have more KRTAP genes ([PMID: 25208914](https://pubmed.ncbi.nlm.nih.gov/25208914/)). These tandemly clustered genes thus homogenize within a genome through recombination/gene conversion, a pattern tightly linked to the evolution of mammalian hair. This evolutionary mode is directly relevant to interpreting KRTAP3-1's sequence: the internal repeats and high cysteine content are maintained and diversified by these recombinational mechanisms rather than by simple point-mutation divergence.

### F005 — KRTAP3-family variation contributes to wool fibre trait variation (candidate marker genes)

Because the high-sulfur matrix proteins set the cross-link density of the fibre, variation among them is a major driver of **breed- and individual-level differences in wool**. Flanagan et al. (2002), using 2D proteomics, found that between- and within-breed wool variation is concentrated in the high-sulfur proteins: **"most of the observed variation occurred among the HSPs, along with some minor variation among the high glycine-tyrosine proteins,"** with breed-specific HSP patterns distinguishing Merino, Romney, and Corriedale ([PMID: 12362341](https://pubmed.ncbi.nlm.nih.gov/12362341/)).

A recent authoritative review by Zhou, Bai, Li, Wang & Hickford (2025) frames the wool keratin and keratin-associated protein genes — their spatiotemporal expression patterns, and **"genetic polymorphism that may influence fibre characteristics"** — as central to understanding wool fibre trait variation and to marker-assisted selection for wool improvement ([PMID: 41096386](https://pubmed.ncbi.nlm.nih.gov/41096386/)). Together with the anagen-regulated follicular expression of KRTAP3.2 ([PMID: 10594723](https://pubmed.ncbi.nlm.nih.gov/10594723/)), this positions KRTAP3-family genes, including KRTAP3-1, as candidate genes for wool quality traits such as fibre diameter and crimp.

### F006 — Structural features: cysteine as CC doublets / CxxC motifs and internal repeats enabling multivalent cross-linking

The architecture of the protein explains how it functions as a cross-linker. Computed from P02446 (98 aa), the 16 cysteines (16.3%) are distributed across the chain at positions 3, 4, 8, 9, 20, 26, 28, 31, 36, 47, 48, 55, 65, 90, 94, and 98 — including **CC doublets** (positions 3–4, 8–9, 47–48) and multiple **C-x-C / C-x-x-C motifs**. The protein is also rich in serine+threonine (19.4%) and proline (13.3%), contains no tryptophan, and carries only a slight net positive charge (~+2). This distribution provides many spatially distributed thiols that can engage multiple disulfide partners — i.e., **multivalent cross-linking capacity**.

Elleman (1972), who directly sequenced the related wool B2 protein, documented an unusual repeat architecture: **"a ten-residue sequence occurs four times near the N-terminus and five times near the C-terminus with few changes. These regions contain much of the molecule's half-cystine,"** whereas between the two repeat blocks lies a ~19-residue region of mainly small residues devoid of cystine and proline ([PMID: 4678578](https://pubmed.ncbi.nlm.nih.gov/4678578/)). This gives a two-lobed, cysteine-dense/cysteine-poor/cysteine-dense organisation well suited to bridging filaments. Consistent with a flexible cross-linker, Fraser & Parry (2018) note that KAPs "adopt a variety of energetically-similar conformations stabilized predominantly by intramolecular disulfide bonds" ([PMID: 29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/)).

### F007 — Spatial deposition: high-sulfur KAPs enriched in the paracortex, deposited during cortical keratinization

Within the wool cortex, KRTAP3-1 is not uniformly distributed. The cortex comprises orthocortex, mesocortex, and paracortex cell types, which in fine Merino wool are **bilaterally segregated along the fibre crimp**. Plowman, Paton & Bryson (2007) reported that the paracortex has a higher cysteine concentration than the orthocortex, and that **"sulphur-rich proteins are initially expressed on the paracortical side of the fibre, with some becoming more uniformly spread… as the keratinization process progresses,"** whereas glycine/tyrosine-rich proteins are expressed initially on the orthocortical side ([PMID: 17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/)).

This positions the high-sulfur KAP class (which includes KAP3) **preferentially toward the paracortex** and temporally within the keratinizing cortical cell. Because the asymmetric (bilateral) distribution of ortho- and paracortex is mechanically linked to **wool crimp**, the paracortical deposition bias of high-sulfur KAPs provides a plausible structural link between KRTAP3-1-type proteins and fibre curvature/crimp.

### F008 — Genomic context: a small single-ORF gene in the ovine chromosome-11 KAP cluster

KRTAP3-1 is a **small, compact gene** encoding a short 98-aa protein (≈297-bp ORF), consistent with the typically intronless, single-exon architecture of KAP genes. The ovine high-sulfur KAP genes map to a **tandem cluster on sheep chromosome 11**. Wang et al. (2020), characterising the related ovine high-sulfur gene KAP2-1, found it as a 399-bp ORF **"which was clustered among nine previously identified keratin-associated protein genes on chromosome 11"** and expressed most highly in skin ([PMID: 32485962](https://pubmed.ncbi.nlm.nih.gov/32485962/)). This tandem clustering is exactly the genomic arrangement that enables the concerted evolution and gene conversion described in F004, and it situates KRTAP3-1 among its sibling high-sulfur KAP genes in the ovine genome.

---

## Mechanistic Model / Interpretation

KRTAP3-1 is a structural building block of the wool fibre. The following model integrates the eight findings into a coherent narrative spanning gene → protein → fibre.

**1. Where and when it is made.** KRTAP3-1 is transcribed specifically in the actively growing (anagen) wool follicle, within the terminally differentiating cortical trichocytes (F003). Its high-sulfur siblings are down-regulated in telogen, confirming anagen-restricted, developmentally timed synthesis.

**2. The protein it makes.** A 98-residue, cysteine-rich (16.3%) protein with internal 10-residue repeats concentrating cysteine near both termini and a cysteine-poor hinge between them (F001, F006). This gives a multivalent, flexible, disulfide-forming molecule.

**3. What it does.** As cortical cells keratinize, keratin intermediate filaments become embedded in a matrix of KAPs. KRTAP3-1 uses its many cysteines (CC doublets, CxxC motifs) to form intra- and inter-molecular cystine bonds, cross-linking adjacent keratin filaments, organising them into macrofibrils, and hardening the matrix (F002, F006).

**4. Where in the fibre.** Deposition is biased toward the paracortex and becomes a permanent feature of the dead, keratinized cortical cell; the ortho/paracortex asymmetry is linked to crimp (F007).

**5. Why it varies.** The gene sits in a tandem chromosome-11 cluster (F008) shaped by concerted evolution and gene conversion (F004); allelic/compositional variation among high-sulfur KAPs underlies breed-level wool differences and makes these candidate markers for fibre traits (F005).

```
   ANAGEN WOOL FOLLICLE → CORTICAL TRICHOCYTE (keratinizing)
   ────────────────────────────────────────────────────────
     KRTAP3-1 gene (chr 11 HS-KAP cluster, single ORF)
                         │ transcription (anagen-specific)
                         ▼
     98-aa Cys-rich protein  [C C ...repeat... C C | hinge | C C ...repeat... C]
                         │ many thiols (–SH)
                         ▼
   ┌──────── INTERFILAMENTOUS MATRIX of the wool cortex ────────┐
   │                                                            │
   │   KIF ===S–S=== KRTAP3-1 ===S–S=== KIF   (disulfide        │
   │    │                                   cross-linking)      │
   │   KIF ===S–S=== KRTAP3-1 ===S–S=== KIF                     │
   │                                                            │
   │   → bundles KIFs into MACROFIBRILS                         │
   │   → rigid, hard, insoluble, degradation-resistant fibre    │
   │   → paracortex-biased deposition → linked to crimp         │
   └────────────────────────────────────────────────────────────┘
```

**Functional classification summary:**

| Question posed | Answer for KRTAP3-1 |
|---|---|
| Enzyme? Reaction/substrate? | No — not catalytic |
| Transporter? Substrate? | No |
| Signaling molecule? Pathway role? | No |
| Structural protein? Role? | **Yes** — disulfide cross-linker of keratin intermediate filaments in the wool cortex matrix |
| Subcellular/organismal location of function | Intracellular; interfilamentous matrix of keratinized cortical cells; paracortex-biased |
| Pathway/biological process | Trichocyte terminal differentiation / wool-fibre keratinization (hair-shaft formation) |

---

## Evidence Base

| PMID | Paper (abbrev.) | How it supports the findings |
|---|---|---|
| [4678578](https://pubmed.ncbi.nlm.nih.gov/4678578/) | Elleman, *Amino acid sequence of SCMK-B2C from high-sulphur wool* | Direct protein sequencing; documents cysteine-rich internal 10-residue repeats (F001, F006) |
| [29797267](https://pubmed.ncbi.nlm.nih.gov/29797267/) | Wu & Irwin, *Evolution of Trichocyte KAPs* | Defines KRTAP disulfide cross-linking matrix function; concerted evolution (F002, F004) |
| [29797269](https://pubmed.ncbi.nlm.nih.gov/29797269/) | Fraser & Parry, *Trichocyte KAPs* | KAPs organise IFs into macrofibrils, link IFs, disulfide-stabilized conformation (F002, F006) |
| [12362341](https://pubmed.ncbi.nlm.nih.gov/12362341/) | Flanagan, Plowman & Bryson, *High sulphur proteins of wool* | Localises HSPs to matrix around IFs in cortical cells; HSP variation drives breed diversity (F003, F005) |
| [10594723](https://pubmed.ncbi.nlm.nih.gov/10594723/) | Rufaut et al., *Wool follicle growth cycle genes* | KRTAP3.2 is anagen-regulated, follicle-expressed, structural (F003, F005) |
| [18721477](https://pubmed.ncbi.nlm.nih.gov/18721477/) | Wu, Irwin & Zhang, *Molecular evolution of KAP family* | High/ultrahigh-cysteine KRTAPs evolve by concerted evolution + gene conversion (F004) |
| [25208914](https://pubmed.ncbi.nlm.nih.gov/25208914/) | Khan et al., *Mammalian KRTAP subgenomes* | HS subfamily: strong concerted evolution, gene conversion, high GC (F004) |
| [17697142](https://pubmed.ncbi.nlm.nih.gov/17697142/) | Plowman, Paton & Bryson, *Cortical cell proteins* | Sulphur-rich proteins expressed paracortical side during keratinization (F007) |
| [32485962](https://pubmed.ncbi.nlm.nih.gov/32485962/) | Wang et al., *Ovine KAP2-1 gene* | HS-KAP genes clustered on sheep chromosome 11 (F008) |
| [41096386](https://pubmed.ncbi.nlm.nih.gov/41096386/) | Zhou et al. 2025 review, *Wool…genetic insights* | Authoritative review linking KAP polymorphism to fibre traits (F005) |

Supporting/contextual literature also reviewed includes studies characterising other ovine KAP genes and their associations with wool traits (e.g., KRTAP28-1 [PMID: 30987059], KAP11-1 [PMID: 21400094], KAP22 family [PMID: 41096366], KAP19 family [PMID: 40725111], KAP20-1 [PMID: 39202420]), and classic keratin gene-organisation work (e.g., [PMID: 2417523], [PMID: 2458477], [PMID: 30599197]). These consistently depict KAPs as cysteine-rich structural matrix proteins and candidate wool-trait markers, corroborating the specific findings for KRTAP3-1.

**Nature of the evidence:** The core functional annotation rests on strong, convergent evidence — direct protein sequencing of the ovine protein itself (precise, primary), authoritative reviews of KAP structure/function, proteomic localisation studies, in situ follicular expression data, and comparative genomics. This is a rare case where a non-model-organism protein has both classical biochemical characterisation and modern genomic/evolutionary framing.

---

## Limitations and Knowledge Gaps

1. **No KRTAP3-1-specific functional perturbation.** There is no reported knockout, knockdown, or transgenic experiment isolating KRTAP3-1's individual contribution to fibre properties. Its function is inferred from (a) direct sequence/composition, (b) membership in a well-characterised structural class, and (c) studies of paralogues (e.g., KRTAP3.2) and the broader HS-KAP class. Functional redundancy among many KAP genes makes single-gene effects hard to isolate.

2. **Disulfide-bonding partners not mapped at residue resolution.** While cross-linking to keratins and other KAPs is established for the class, the specific keratin partners and exact cystine pairings of KRTAP3-1 have not been experimentally determined. The cross-linking model is mechanistically sound but not structurally resolved for this protein.

3. **Paracortex bias is class-level, not KRTAP3-1-specific.** The paracortical deposition and crimp linkage (F007) are demonstrated for sulphur-rich proteins collectively; direct spatial mapping of KRTAP3-1 itself within the ortho/para/mesocortex is lacking.

4. **Quantitative trait associations for KRTAP3-1.** Although HS-KAP variation drives wool diversity in general, published genotype–phenotype association studies for ovine KRTAP3-1 specifically (versus other KAPs) were not identified in this investigation; the trait-marker claim is by extension from the class.

5. **Post-translational modifications.** Related HS-KAPs can be phosphorylated (e.g., KAP11-1); whether KRTAP3-1's abundant Ser/Thr residues are phosphorylated and whether this affects assembly is unknown.

6. **3D structure.** No experimental 3D structure exists; KAPs are thought to be largely intrinsically flexible, adopting multiple disulfide-stabilized conformations, which complicates structural prediction.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted genotype–phenotype association.** Sequence ovine *KRTAP3-1* across breeds (e.g., Merino, Romney, Corriedale, Chinese breeds) and test SSCP/haplotype variants for association with fibre diameter, crimp, staple strength, and curvature — mirroring the approach used for other ovine KAP genes.

2. **Spatial proteomics / in situ localisation of KRTAP3-1.** Use isoform-specific antibodies or in situ hybridisation to map KRTAP3-1 within ortho-, meso-, and paracortex and along the keratinization gradient, testing the predicted paracortical bias directly.

3. **Disulfide cross-link mapping.** Apply redox proteomics (differential cysteine labelling + MS) to the wool cortex to identify KRTAP3-1's specific keratin and KAP disulfide partners and cystine pairings.

4. **Biophysical reconstitution.** Express recombinant KRTAP3-1 and assay its capacity to cross-link and bundle reconstituted keratin intermediate filaments in vitro, quantifying effects on matrix rigidity.

5. **Comparative/evolutionary analysis.** Characterise the KRTAP3-1 orthologue set and the chromosome-11 cluster across ruminants to quantify gene-conversion tracts and relate sequence homogenisation to fibre phenotypes.

6. **PTM characterisation.** Determine whether KRTAP3-1's Ser/Thr residues are phosphorylated in vivo and whether this modulates matrix assembly or cross-link density.

---

## Conclusion

Sheep **KRTAP3-1 (P02446)** is the classical wool high-sulfur matrix protein **IIIB2/SCMKB-B2**, a small (98-aa), cysteine-rich (16.3% Cys) **structural keratin-associated protein** of the high-sulfur KRTAP type 3 family. It is **not** an enzyme, transporter, or signaling molecule. Its primary function is to form part of the **interfilamentous matrix of the wool-fibre cortex**, cross-linking keratin intermediate filaments through extensive intra- and inter-molecular **disulfide (cystine) bonds** — organising them into macrofibrils and conferring the fibre's rigidity, hardness, and durability. It acts **intracellularly within terminally differentiating cortical trichocytes** of the anagen wool follicle, with a **paracortical deposition bias**, becoming a permanent component of the mature keratinized fibre. Its biological context is **trichocyte differentiation and wool-fibre keratinization**, and its genomic position in a tandem chromosome-11 KAP cluster, shaped by concerted evolution and gene conversion, underlies the variation that links high-sulfur KAPs to wool-fibre traits.


## Artifacts

- [OpenScientist final report](KRTAP3-1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KRTAP3-1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:4678578
2. PMID:29797267
3. PMID:29797269
4. PMID:12362341
5. PMID:10594723
6. PMID:18721477
7. PMID:25208914
8. PMID:41096386
9. PMID:17697142
10. PMID:32485962
11. PMID:30987059
12. PMID:21400094
13. PMID:41096366
14. PMID:40725111
15. PMID:39202420
16. PMID:2417523
17. PMID:2458477
18. PMID:30599197