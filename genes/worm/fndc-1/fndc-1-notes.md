# fndc-1 (C. elegans) research notes

UniProt: **Q22252** (FNDC1_CAEEL) · WormBase: **WBGene00011528** / locus **T06D8.7** ·
mammalian ortholog: FUNDC1 · Family: FUN14 (Pfam PF04930, InterPro IPR007014).

> Naming note: the task/flagship project refers to this gene as "fundc-1" (after
> mammalian *FUNDC1*). The **official WormBase symbol is `fndc-1`** (used by UniProt with
> ECO:0000303|PubMed:31233739 and ECO:0000312|WormBase:T06D8.7). All work here uses the
> correct WormBase symbol `fndc-1`. The earlier project note ("no clear C. elegans
> ortholog in UniProt") reflects a symbol mismatch, not a missing gene — Q22252 is a
> reviewed Swiss-Prot entry.

## Protein / identity (established)

- 138-aa integral membrane protein with **two predicted TM helices** (residues 37–56,
  61–78; ECO:0000255) and UniProt subcellular location **"Mitochondrion outer membrane …
  Multi-pass membrane protein"** (ECO:0000305|PubMed:31233739). Small multi-pass OMM
  topology is the hallmark of the FUN14/FUNDC1 family.
- Sole informative domain: FUN14 (the FUNDC1 family fold). No enzymatic domain — this is
  an adaptor/receptor-type protein, not an enzyme.

## What is KNOWN in *C. elegans* (peer-reviewed, worm-established)

1. **Contributes to paternal-mitochondria elimination after fertilization.**
   - [PMID:31233739 "FNDC-1 is strongly expressed in sperm but not oocytes and contributes to paternal mitochondria elimination"]
   - [PMID:31233739 "loss of fndc-1 retards the rate of paternal mitochondria degradation, but not that of membranous organelles, a nematode specific membrane compartment whose fusion is required for sperm motility"]
   - Functional read-out that paternal mtDNA persists without fndc-1:
     [PMID:31233739 "Paternal mitochondrial DNA is normally undetectable in wildtype larva, but can be detected in the cross-progeny of fndc-1 mutant males"]
   - The authors frame this as the **first ubiquitin-independent mitophagy receptor** for
     sperm-mitochondria degradation:
     [PMID:31233739 "This is the first example of a ubiquitin-independent mitophagy receptor playing a role in the selective degradation of sperm mitochondria"]
   - fndc-1 is a **second, temporally distinct** route, redundant with an earlier
     ubiquitin-dependent (ubc-18/ubc-16 → proteasome/LGG-1) mechanism:
     [PMID:31153831 "If paternal mitochondria are not eliminated via this early process, they are eventually removed from the embryo in a process that depends on the mitophagy adaptor protein, fndc-1"]
     [PMID:31153831 "Thus, there are two redundant, but temporally distinct mechanisms that target paternal mitochondria for elimination in C. elegans"]
   - The phenotype is a **delay, not a block** (redundancy) → mild loss-of-function.

2. **Mediates hypoxia-reoxygenation (HR)-induced mitophagy in somatic tissue (body-wall muscle).**
   - Establishes the worm ortholog identity explicitly:
     [PMID:33416042 "Here, we provide evidence that FNDC-1 is the C. elegans ortholog of FUNDC1, and that its loss protects against injury in a worm model of HR"]
   - Protection on *loss* depends on the UPRmt transcription factor ATFS-1:
     [PMID:33416042 "This protection depends upon ATFS-1, a transcription factor that is central to the mitochondrial unfolded protein response (UPRmt)"]
   - FNDC-1 also has a role in non-hypoxic (basal) mitochondrial quality control:
     [PMID:33416042 "These data support a role for FNDC-1 in non-hypoxic MQC, and further suggest that these changes are prophylactic in relation to subsequent HR"]
   - (Quantitative HR-mitophagy data — mito-mKeima, mRuby3::FNDC-1 co-localization,
     proteinase-K OMM topology — are in the Lim 2021 full text, not the cached abstract.)

3. **Localization: mitochondrial outer membrane.**
   - UniProt curated from primary lit (PubMed:31233739); GOA carries IBA (GO_REF:0000033)
     and IEA (GO_REF:0000044, UniProt-SubCell) OMM annotations. TM topology + FUN14 family
     are consistent. Established.

## What is INFERRED from mammalian FUNDC1 (NOT directly shown in worm)

- **LC3-interacting region (LIR) motif and direct ATG8 binding.** Mammalian FUNDC1 uses a
  phospho-regulated LIR to bind LC3/GABARAP. In worm, **no LIR has been mapped/mutated and
  no direct FNDC-1–LGG-1/LGG-2 (ATG8) interaction has been demonstrated.** The
  "receptor/adaptor" molecular activity in worm rests on genetic loss-of-function +
  orthology, i.e. it is an **ISS-level** MF claim, not a direct assay.
- **Phospho/ubiquitin regulation** (SRC, CK2, ULK1, PGAM5, MARCH5 acting on the LIR in
  mammals) — none demonstrated for worm FNDC-1.
- **MAM enrichment / DRP-1 recruitment / oocyte-to-zygote-transition (MOZT) developmental
  mitophagy.** These appear only in **2025 preprints** (bioRxiv 2025.02.01.636045;
  Research Square rs.3.rs-6330979) — treated here as preliminary and deliberately kept out
  of the top-level `description` and out of any peer-reviewed annotation. Documented as an
  open/narrowing knowledge gap only.

## Existing GOA annotations (6) and disposition

| GO term | Aspect | Evidence | Ref | Action |
|---|---|---|---|---|
| GO:0000422 autophagy of mitochondrion | BP | IBA | GO_REF:0000033 | ACCEPT |
| GO:0005741 mitochondrial outer membrane | CC | IBA | GO_REF:0000033 | ACCEPT |
| GO:0005741 mitochondrial outer membrane | CC | IEA | GO_REF:0000044 | ACCEPT |
| GO:0006914 autophagy | BP | IEA | GO_REF:0000043 | ACCEPT (general parent; subsumed by mitophagy terms) |
| GO:0000423 mitophagy | BP | IMP | PMID:31153831 | ACCEPT |
| GO:0000423 mitophagy | BP | IMP | PMID:31233739 | ACCEPT |

Proposed NEW (not in GOA):
- **GO:0140580 mitochondrion autophagosome adaptor activity** — the missing MF term.
  Coded **ISS** (not IDA): the adaptor/bridging activity is inferred from mammalian FUNDC1
  orthology + worm genetic phenotype; direct LGG-1/LGG-2 binding is not shown in worm.
- **GO:0071456 cellular response to hypoxia** — IMP from Lim 2021 HR model
  (fndc-1 loss changes HR outcome). Worm-established.

## Knowledge gaps (see YAML `knowledge_gaps`)

1. Molecular adaptor mechanism / LIR + LGG-1/LGG-2 partner not experimentally established in worm.
2. Regulation of FNDC-1 (post-translational switches) uncharacterized in worm.
3. Physiological scope / pathway placement (vs PINK-1/PDR-1, DCT-1/NIX) unresolved; phenotype
   mild/context-restricted; some stresses (acute heat) remodel mitochondria independently of fndc-1.

Explicit field admission (deep-research synthesis, grep-verified in the falcon report):
"Direct phosphorylation/ubiquitination mapping and LIR validation for C. elegans FNDC-1
remain to be fully elucidated."

## Provenance / sources

- Cached abstracts (abstract-only, `full_text_available: false`):
  publications/PMID_31233739.md, PMID_31153831.md, PMID_33416042.md.
- Deep research: genes/worm/fndc-1/fndc-1-deep-research-falcon.md (Edison Scientific,
  real run, 27 citations). Review/preprint claims (Ganguly 2024; Choubey 2021; Liu 2020;
  Haeussler 2020; Thendral/Sherwood 2025 preprints) used only for context/inference, not
  for peer-reviewed annotation.
