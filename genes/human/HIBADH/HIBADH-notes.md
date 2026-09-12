# HIBADH (P31937) — review notes

## Identity and core biology

HIBADH encodes **3-hydroxyisobutyrate dehydrogenase, mitochondrial** (EC 1.1.1.31),
336 aa precursor with an N-terminal mitochondrial transit peptide (residues 1–36),
mature chain 37–336.

- RecName and EC from UniProt: `RecName: Full=3-hydroxyisobutyrate dehydrogenase, mitochondrial; ... EC=1.1.1.31` [file:human/HIBADH/HIBADH-uniprot.txt].
- Catalytic activity: `Reaction=3-hydroxy-2-methylpropanoate + NAD(+) = 2-methyl-3-oxopropanoate + NADH + H(+)` with `EC=1.1.1.31`, `Evidence={ECO:0000269|PubMed:16466957}` [file:human/HIBADH/HIBADH-uniprot.txt]. 3-hydroxy-2-methylpropanoate = 3-hydroxyisobutyrate; 2-methyl-3-oxopropanoate = (2-)methylmalonate semialdehyde.
- Pathway: `Amino-acid degradation; L-valine degradation. {ECO:0000269|PubMed:16466957}` [file:human/HIBADH/HIBADH-uniprot.txt].
- Subcellular location: `Mitochondrion` [file:human/HIBADH/HIBADH-uniprot.txt]; transit peptide directs matrix import.
- Subunit: `Homodimer. {ECO:0000250}` [file:human/HIBADH/HIBADH-uniprot.txt]. (Reactome infers a tetramer from PDB 2GF2; UniProt states homodimer by similarity.)
- Family: `Belongs to the HIBADH-related family. 3-hydroxyisobutyrate dehydrogenase subfamily. {ECO:0000305}` [file:human/HIBADH/HIBADH-uniprot.txt].
- NAD binding is structurally established: multiple `BINDING ... /ligand="NAD(+)"` features from PDB 2GF2 (residues 40–68, 103–104, 108, 134, 284) [file:human/HIBADH/HIBADH-uniprot.txt]; PDB 2GF2/2I9P crystallized as apoprotein and in complex with NADH. DrugBank lists NADH as ligand. The enzyme uses **NAD(+)** as the physiological cofactor (Rhea:17681 uses NAD).

## Valine catabolism context

3-hydroxyisobutyrate → methylmalonate semialdehyde is a downstream step of L-valine
degradation. The product (methylmalonate semialdehyde) is handled next by ALDH6A1
(methylmalonate-semialdehyde dehydrogenase). Reactome places HIBADH in "Branched-chain
amino acid catabolism" (R-HSA-70895) and models the reaction both directions
(R-HSA-70885 forward beta-hydroxyisobutyrate + NAD+ → methylmalonyl semialdehyde + NADH;
R-HSA-508473 reverse), located in mitochondrial matrix [reactome/R-HSA-70885.md,
reactome/R-HSA-508473.md].

## Key primary reference — PMID:16466957 (Loupatty et al. 2006)

Abstract-only in cache (`full_text_available: false`). This is the functional
identification of the human enzyme:
- "By heterologous expression in Escherichia coli, we showed that the product of the HIBADH gene indeed displays 3-hydroxyisobutyrate dehydrogenase activity." [PMID:16466957]
- Assays used skin fibroblast homogenates (UniProt TISSUE SPECIFICITY "Detected in skin fibroblasts" cites this PMID).
- Notably, the paper concludes **HIBADH is NOT the causative gene in 3-hydroxyisobutyric aciduria** — no mutations found in patients; enzyme activity in patient fibroblasts was normal. So HIBADH deficiency is not established as the disease mechanism; the disease association is negative. This is a caveat for any disease annotation but does not affect the enzymatic MF/BP annotations, which the paper directly supports.
- UniProt cites this same PMID for CATALYTIC ACTIVITY and PATHWAY, so it is the anchor for GO:0008442 (MF) and GO:0006574 (BP) IDA annotations.

## Large-scale / screen references

- **PMID:32296183** (Luck et al. 2020, HuRI binary interactome, Y2H). Source of the ~40 GO:0005515 "protein binding" IPI annotations in GOA. HIBADH is a matrix metabolic enzyme; the IntAct partners in the UniProt INTERACTION block are overwhelmingly membrane / secretory-pathway proteins (ADAM33, AQP3, VAMP2/5, GOSR2, SEC22B, TFRC, TMEM* family, etc.) — these are typical high-throughput Y2H associations, not evidence of a physiological complex or an informative molecular function. Bare "protein binding" is uninformative per curation policy → MARK_AS_OVER_ANNOTATED (do not REMOVE an IPI).
- **PMID:34800366** (Morgenstern et al. 2021, high-confidence human mitochondrial proteome, Cell Metab, full text available). HTP mitochondrial localization evidence, consistent with UniProt "Mitochondrion" and matrix localization. Corroborates GO:0005739 (mitochondrion). HIBADH not found in a simple grep of the cached text (likely reported in a supplementary table); the localization claim is consistent with authoritative UniProt so ACCEPT as non-core corroboration.

## Annotation review summary

Core function (well supported): 3-hydroxyisobutyrate dehydrogenase activity (GO:0008442,
NAD+-dependent, EC 1.1.1.31) acting in L-valine catabolic process (GO:0006574) in the
mitochondrial matrix (GO:0005759). NAD binding (GO:0051287) supported structurally.

- GO:0008442 IDA (PMID:16466957) → ACCEPT (core MF).
- GO:0006574 IDA (PMID:16466957) → ACCEPT (core BP).
- GO:0008442 IBA / IEA → ACCEPT (redundant with IDA, consistent).
- GO:0006574 IBA / IEA → ACCEPT / consistent.
- GO:0005739 mitochondrion (IBA, IEA, HTP) → ACCEPT but non-core relative to the more specific matrix term; UniProt only says "Mitochondrion". The specific matrix localization (GO:0005759, Reactome TAS) is the better location.
- GO:0005759 mitochondrial matrix (TAS Reactome x2) → ACCEPT (core location).
- GO:0051287 NAD binding (IEA, InterPro) → ACCEPT; NAD(+) is the physiological cofactor (Rhea:17681), structurally bound (PDB 2GF2).
- GO:0050661 NADP binding (IEA, InterPro) → MARK_AS_OVER_ANNOTATED. Family/Rossmann InterPro signature (IPR006115 "6PGDH NADP-bd") generically maps to NADP binding, but HIBADH's physiological cofactor is NAD(+), not NADP. No evidence of NADP use; over-propagated from the 6-phosphogluconate-dehydrogenase-like fold. Keep (IEA, not experimental) but flag as over-annotation; a REMOVE could be argued but MARK_AS_OVER_ANNOTATED is the conservative choice.
- GO:0016491 oxidoreductase activity (IEA, InterPro) → MARK_AS_OVER_ANNOTATED. Correct but far too general; the specific GO:0008442 is annotated and preferred.
- GO:0005515 protein binding (IPI x~40, PMID:32296183) → MARK_AS_OVER_ANNOTATED (bare protein binding, uninformative; HuRI Y2H).

No REMOVE actions (policy: no REMOVE of experimental annotations or bare protein-binding IPI;
IEA over-annotations flagged rather than removed here since NADP/oxidoreductase are not
"clearly wrong" so much as over-general/family-propagated).
</content>
</invoke>
