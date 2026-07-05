# MCO14 (YHL018W / P38744) review notes

## Identity (verified)

- **Standard name:** MCO14 (SGD). Name description at SGD: "Mitochondrial Class One protein of 14 kDa".
  The `MCO` prefix = "Mitochondrial Class One" protein, a naming series introduced by Morgenstern et al.
  2017 for high-confidence mitochondrial proteins of previously unknown function
  [PMID:28658629, "The mitochondrial class 1 protein of 10 kDa (Mco10)..."]. MCO14 was named in the same
  study; the trailing number encodes the ~kDa mass (Mco14 ≈ 14 kDa).
- **Systematic name:** YHL018W (chromosome VIII). **SGDID:** S000001010. **UniProt:** P38744 (PHS_YEAST),
  120 aa, 14 kDa, "Evidence at protein level" (PE1).
- **UniProt RecName:** "**Putative** pterin-4-alpha-carbinolamine dehydratase" (EC 4.2.1.96); AltNames
  "4-alpha-hydroxy-tetrahydropterin dehydratase", "Pterin carbinolamine dehydratase (PCD)". The word
  *Putative* is important: the enzymatic activity is a **family-based inference**, not measured in yeast.
- Verified via SGD REST (`/backend/locus/MCO14`): gene_name MCO14, uniprot_id P38744, feature YHL018W,
  qualifier "Verified" ORF.

## Domain / family (inline analysis of MCO14-uniprot.txt)

- Belongs to the **pterin-4-alpha-carbinolamine dehydratase (PCD/DCoH) family** (UniProt SIMILARITY,
  ECO:0000305). Domain hits in the UniProt record:
  - Pfam **PF01329** (Pterin_4a)
  - InterPro **IPR001533** (Pterin dehydratase), **IPR036428** (PCD superfamily)
  - CDD **cd00488** (PCD_DCoH)
  - PANTHER **PTHR12599** / **PTHR12599:SF0** (PTERIN-4-ALPHA-CARBINOLAMINE DEHYDRATASE)
  - Gene3D 3.30.1360.20 "Transcriptional coactivator/pterin dehydratase"; SUPFAM SSF55248 PCD-like.
- **Catalytic-motif conservation (inline sequence analysis).** MCO14 sequence
  `...VSMRSHLWG​HHPLIH...` contains the diagnostic PCD catalytic **HHP** motif. Aligning to human PCBD1
  (P61457), whose UniProt BINDING sites are residues 61-63 (`DHH`, containing the catalytic His pair) and
  78-81, the human catalytic motif `DHHPEW` aligns to MCO14 `GHHPLIH` — the **His-His-Pro core is
  conserved**, and the upstream `TRV` (human `TRVAL` / yeast `TRVSM`) is conserved. So MCO14 **retains the
  PCD catalytic signature** and is a plausible (not obviously defunct) dehydratase — but note this is a
  distant homolog (~30% local identity around the catalytic window), and no direct enzyme assay exists for
  the yeast protein.
- CDD/Gene3D also flag the shared fold with the **DCoH transcriptional-coactivator (dimerization cofactor
  of HNF1)** moonlighting activity known for the vertebrate paralogs. There is no evidence for a
  transcription-factor partner in yeast (yeast has no HNF1 ortholog), so that moonlighting role is not
  expected here.

## Localization (KNOWN)

- **Mitochondrion.** GOA: GO:0005739 mitochondrion, HDA, assigned by SGD from the genome-wide GFP
  localization dataset [PMID:14562095, Huh et al. 2003] (per-ORF localization is in that study's
  supplement; the cached entry is abstract-only).
- Independently confirmed by the high-confidence mitochondrial proteome study [PMID:28658629,
  Morgenstern et al. 2017], which included Mco14 among high-confidence mitochondrial proteins and studied
  its import/complex formation. In their blue-native + import assays, complex formation was
  membrane-potential (Δψ)-dependent: "*the precursor proteins were translocated into or across the inner
  membrane to form a complex (shown here for Dpa10, Mco14, Dpi29, and Dpi34)*" — indicating an
  inner-membrane/matrix-facing location rather than the outer membrane/IMS. Blue-native analysis also
  showed Mco14 forms "*distinct high-molecular-weight complexes*".

## Molecular function — what is known vs not

- **KNOWN (family inference):** PCD-family fold with conserved catalytic HHP motif → predicted
  4-alpha-hydroxytetrahydrobiopterin dehydratase (EC 4.2.1.96). This is the single most-supported
  functional hypothesis, but is IEA/IBA only and flagged "Putative" by UniProt.
- **NOT KNOWN:** No direct enzymatic assay of P38744; no measured substrate; no in-vivo function; no
  deletion phenotype (SGD phenotype_details returns 0 phenotypes); no genetic pathway placement. GOA has
  the ND (no-data) root annotations GO:0003674 and GO:0008150 recorded by SGD — an explicit statement
  that curators could not assign specific function/process from experiment.

## Biological process — the BH4 pathway is largely ABSENT in yeast (key reviewer point)

- The IEA BP annotation GO:0006729 "tetrahydrobiopterin biosynthetic process" (InterPro2GO, GO_REF:0000002)
  carries a **metazoan/bacterial pathway context that S. cerevisiae mostly lacks**:
  - Yeast has GTP cyclohydrolase I (**FOL2/GCH1**), but that enzyme feeds **folate** biosynthesis; the
    downstream **BH4-specific** enzymes 6-pyruvoyl-tetrahydropterin synthase (PTS/PTPS) and sepiapterin
    reductase (SPR) are **not present natively** — heterologous PTS and SPR must be introduced to make BH4
    in yeast (Germann et al. 2016, *Biotechnol J*, PMC5066760: "GCH1/Fol2 is natively present in wild-type
    S. cerevisiae, whereas heterologous PTS and SPR were introduced to enable BH4 production").
  - Yeast also lacks the aromatic amino acid hydroxylases (PAH/TH/TPH) whose reaction generates the
    4a-carbinolamine substrate that PCD/DCoH regenerates. PCD's canonical role is **regeneration/recycling**
    of BH4 during aromatic amino acid hydroxylation, not de novo BH4 *biosynthesis* — and neither the
    substrate-producing hydroxylases nor de novo BH4 synthesis operate natively in budding yeast.
  - Reactome maps P38744 to "Phenylalanine metabolism" (R-SCE-8964208) purely by family orthology; there
    is no evidence yeast runs Phe hydroxylation.
  → The BH4-biosynthesis BP is therefore an over-propagation in this organism (PATHWAY_CONTEXT_IGNORED).
  Marked MARK_AS_OVER_ANNOTATED (not a flat REMOVE: the term is family-appropriate; it is the yeast
  pathway context that is missing).

## Interactions / abundance

- Abundance: "*Present with 752 molecules/cell in log phase SD medium*" (UniProt MISCELLANEOUS, from
  PMID:14562106). SGD lists 97 physical/genetic interactions, essentially all high-throughput; no
  curated functional complex partner. BioGRID-ORCS: 0 hits in 10 CRISPR screens (non-essential, no strong
  fitness signal).

## Summary of KNOWN vs NOT-known (for knowledge_gaps)

- KNOWN: mitochondrial protein (dual proteomic evidence); ~14 kDa; PCD/DCoH fold with conserved catalytic
  HHP motif; imported in a Δψ-dependent manner and part of a high-MW complex; non-essential; moderate
  abundance.
- NOT KNOWN: the actual biochemical substrate and whether MCO14 is catalytically active in vivo; its
  physiological mitochondrial role/process; any deletion or conditional phenotype; whether the annotated
  BH4/pterin chemistry occurs at all in yeast mitochondria; its complex partners; any regulatory or
  moonlighting function.

## Provenance log
- SGD REST `/backend/locus/MCO14` and `/S000001010/phenotype_details`, `/interaction_details` (2026-07-05).
- UniProt P38744 (cached MCO14-uniprot.txt); human PCBD1 P61457 (rest.uniprot.org, for catalytic-residue
  comparison).
- PMID:28658629 (Morgenstern 2017, full text cached) — mitochondrial proteome, MCO naming, Mco14 import.
- PMID:14562095 (Huh 2003, abstract cached) — GFP localization source for the mitochondrion annotation.
- Germann et al. 2016 (PMC5066760, WebFetch) — yeast lacks native PTS/SPR for BH4.
