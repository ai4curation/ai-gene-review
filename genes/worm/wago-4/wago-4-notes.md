# wago-4 (F58G1.1, O62275) — research notes

Curator research journal. Provenance is recorded inline as `[PMID:xxxx "verbatim quote"]`.
All quotes below were verified as verbatim substrings of the cached `publications/PMID_*.md`.

## Identity
- **Gene:** wago-4 / F58G1.1 / WBGene00010263. UniProt **O62275** (WAGO4_CAEEL, 965 aa).
- **Family:** Argonaute family, **WAGO (worm-specific Argonaute) subfamily**. Domains: PAZ (318–428) and Piwi (594–924) [from UniProt record].
- One of the ~27 C. elegans Argonautes; a *secondary* Argonaute of the WAGO clade.

## What is KNOWN (wago-4-specific, experimental)

### Small-RNA binding / molecular function
- WAGO-4 binds secondary **22G-RNAs** and their target mRNAs (not miRNAs):
  [PMID:29791857 "WAGO-4 binds to 22G-RNAs and their mRNA targets."]
- Its 22G-RNAs overlap the CSR-1 germline gene cohort and carry 3′ uridylation:
  [PMID:29791857 "WAGO-4-associated endogenous 22G-RNAs target the same cohort of germline genes as CSR-1 and contain untemplated addition of uracil at the 3' ends."]
- 22G-RNAs are RdRP-derived endo-siRNAs (~22 nt, 5′ G) — i.e. siRNAs, not miRNAs. So the
  correct MF is **siRNA binding (GO:0035197)**, and the IBA **miRNA binding (GO:0035198)** is a
  mischaracterization inherited from the pan-Argonaute tree.

### Catalytic (slicer) activity — likely ABSENT
- The downstream/secondary WAGO-clade Argonautes lack the catalytic residues for target cleavage:
  [PMID:17110334 "Interestingly, these AGO proteins lack key residues required for mRNA cleavage."]
- UniProt concurs (MISCELLANEOUS): "Members of the WAGO (worm-specific argonaute) subfamily
  lack conserved metal-binding residues found in other argonaute proteins and probably do not
  cleave target mRNAs directly." (ECO:0000303|PubMed:17110334).
- => The IBA **RNA endonuclease activity (GO:0004521)**, propagated from catalytically active
  Argonautes elsewhere in the family tree, is not warranted for WAGO-4. This is the crux of the
  "is it catalytically active?" question and remains formally unproven for WAGO-4 (see gaps).

### Biological process — RNAi inheritance / germline PTGS
- WAGO-4 is required for the inheritance (transgenerational maintenance) of RNAi:
  [PMID:29791857 "we identified a cytoplasmic Argonaute protein, WAGO-4, necessary for the inheritance of RNAi."]
  [PMID:29791857 "is required for the inheritance of exogenous RNAi targeting both germline- and soma-expressed genes."]
- Independent screen (Wan/Kennedy) reached the same conclusion:
  [PMID:29769721 "like ZNFX-1, WAGO-4 is required for RNAi inheritance."]
- Essential for germline RNAi (Sendoel):
  [PMID:30728462 "we additionally identified WAGO-4 as an essential Argonaute for germline-specific RNAi."]
- Dosage-sensitive positive regulator of silencing: WAGO-4 overexpression enhances RNAi:
  [PMID:30728462 "upregulation of WAGO-4 in mina-1 mutant animals causes hypersensitivity to exogenous RNAi."]
  (consistent with the general secondary-Argonaute behavior [PMID:17110334 "Overexpression of downstream AGOs enhances silencing, suggesting that these proteins are limiting for RNAi."])

### Partners / mechanism of transgenerational transport
- Physically and functionally partners with the helicase **ZNFX-1**:
  [PMID:29769721 "3xFLAG::WAGO-4 co-precipitates with HA::ZNFX-1, but not a HA tagged negative control protein HA::HRDE-1,"]
- WAGO-4 is required for ZNFX-1 to engage target mRNA:
  [PMID:29769721 "in wago-4 mutant animals, ZNFX-1 failed [to] interact with the oma-1 mRNA in response to oma-1 RNAi"]
  (verbatim string in text: "in wago-4 mutant animals, ZNFX-1 faile")
- Genetically/physically interacts with the KH-domain RBP **MINA-1**:
  [PMID:30728462 "WAGO-4 co-precipitated with MINA-1, suggesting a potential protein–protein interaction."]

### Localization (experimental)
- Cytoplasmic; germline perinuclear foci:
  [PMID:29791857 "accumulates at the perinuclear foci in the germline"]
- P-granule associated (transient component), adjacent to P granules:
  [PMID:30728462 "WAGO-4, like several other Argonautes including ALG-3, PRG-1, and CSR-1, is a transient component of P granules and localizes adjacent to P granules in germ cells."]
- With ZNFX-1, localizes to P granules in early germline blastomeres:
  [PMID:29769721 "in early P1-P3 germline blastomeres, ZNFX-1 and WAGO-4 localize to P granules."]
- Defines a distinct condensate, the **Z granule**, between P granules and Mutator foci:
  [PMID:29769721 "Here we show that the inheritance factors ZNFX-1 and WAGO-4 localize to a liquid-like condensate that we name the Z granule."]
- Germline-restricted expression (UniProt TISSUE SPECIFICITY): hermaphrodite germline and oocytes;
  not in soma.

### Heterochromatin / chromatin (redundant, indirect)
- In Gu 2012, wago-4 (F58G1.1, allele tm1019) was tested only as one member of the 6-gene "MAGO"
  secondary-Argonaute group required for dsRNA-triggered H3K9me3 chromatin modification:
  [PMID:22231482 "MAGO (ppw-1(tm914), sago-1(tm1195), sago-2(tm894), F58G1.1(tm1019), C06A1.4(tm887), and M03D4.6(tm1144)]"]
  [PMID:22231482 "The requirement of rde-1 and MAGO genes for dsRNA-triggered chromatin modification strongly suggests that secondary siRNAs may participate in a connection"]
  => This is a genetic-redundancy (group knockout) contribution; WAGO-4's own core role is
  cytoplasmic PTGS/inheritance, and heterochromatin formation is executed by the nuclear WAGOs
  (HRDE-1/NRDE-3). Keep the IGI (experimental) but as non-core.

## What is NOT known (knowledge gaps)
1. **Is WAGO-4 catalytically active?** It lacks the conserved catalytic/metal-binding residues and
   "probably" does not slice, but no biochemical assay directly tests WAGO-4 slicer activity; a
   non-catalytic, siRNA-guided mRNA-binding/silencing mechanism is inferred, not proven.
2. **Full target-mRNA repertoire and the silencing readout.** WAGO-4 22G-RNAs overlap the CSR-1
   cohort, yet CSR-1 and WAGO-4 have divergent (protective vs silencing/inheritance) outputs; how
   the same target space yields different outcomes, and the direct mRNA-level consequence of
   WAGO-4 binding (destabilization vs translational block vs licensing), is undefined.
3. **Mechanism of transgenerational transport.** WAGO-4 and ZNFX-1 mark a Z granule between P
   granules and Mutator foci, but how 22G-RNA/mRNA information is physically handed across the
   PZM assemblage and transmitted to progeny is a model, not a mechanism.

## Annotation-review plan (summary)
- GO:0035198 miRNA binding (IBA) → **MODIFY** to GO:0035197 siRNA binding (binds 22G-RNAs, not miRNAs).
- GO:0004521 RNA endonuclease activity (IBA) → **REMOVE** (WAGO subfamily lacks catalytic residues; over-propagated IBA).
- GO:0005634 nucleus (IBA) → **REMOVE** (WAGO-4 is a *cytoplasmic* Argonaute; no nuclear-action evidence; over-propagated IBA).
- GO:0003676 nucleic acid binding (IEA) / GO:0003723 RNA binding (IEA) → generic parents; KEEP_AS_NON_CORE.
- GO:0003727 single-stranded RNA binding (IBA) → ACCEPT (binds ss 22G guide + mRNA), non-core relative to siRNA binding.
- GO:0005737 cytoplasm (IBA/IEA/EXP), GO:0048471 perinuclear region (IEA), GO:0036464 cytoplasmic RNP granule (IBA) → ACCEPT; RNP granule refined to P granule in core_functions.
- GO:0016442 RISC complex (IBA) → ACCEPT.
- GO:0035194 regulatory ncRNA-mediated PTGS (IBA) → ACCEPT (core BP).
- GO:0060966 regulation of gene silencing by regulatory ncRNA (IMP, PMID:30728462) → ACCEPT (experimental).
- GO:0031048 regulatory ncRNA-mediated heterochromatin formation (IGI, PMID:22231482) → KEEP_AS_NON_CORE (redundant MAGO-group, indirect for a cytoplasmic Ago).

## Deep research provenance
Falcon deep research (`just deep-research-falcon worm wago-4 --fallback perplexity-lite`) was
launched but the Edison endpoint was congested (multiple concurrent gene jobs) and had not
returned a file at review time. This review is therefore built entirely on the cached primary
literature below plus the UniProt/GOA records; every claim is PMID-anchored and independently
verified against the cached full text/abstract. No `file:` deep-research quotes are used, so the
review is self-contained. (If a real falcon file lands later it can be added as a supplementary
reference; it is not required for any conclusion here.) No annotation required UNDECIDED — each
had sufficient primary-literature evidence.

## References used (all cached)
- PMID:29791857 Xu et al. 2018 Cell Rep — abstract-only cache; WAGO-4 = cytoplasmic Ago for RNAi inheritance; binds 22G-RNAs + mRNA targets.
- PMID:29769721 Wan et al. 2018 Nature — full text; Z granule, ZNFX-1 interaction, RNAi inheritance.
- PMID:30728462 Sendoel et al. 2019 Cell Death Differ — full text; MINA-1/WAGO-4 network; germline RNAi; P-granule.
- PMID:17110334 Yigit et al. 2006 Cell — abstract-only; WAGO clade lacks cleavage residues; secondary Argonautes act downstream.
- PMID:22231482 Gu et al. 2012 Nat Genet — full text; MAGO 6-gene group (incl. F58G1.1/wago-4) required for RNAi-triggered H3K9me3.
