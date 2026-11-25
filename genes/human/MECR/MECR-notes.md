# MECR (human, UniProtKB:Q9BV79) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml`, where MECR is one of the
representatives of the mitochondrial (MECR/ETR1-type) NADPH enoyl reductase variant
of the enoyl-reduction step, beside yeast ETR1 and *S. pombe* etr1 (both already
reviewed in this repository).

## Core function

MECR is the mammalian orthologue of yeast Etr1/Mrf1' and catalyses the last of the
four reactions of each mitochondrial FAS II elongation cycle. The purified
recombinant enzyme reduces trans-2-enoyl thioesters of C6–C16 with NADPH, preferring
medium chains
[PMID:12654921 "Recombinant HsNrbf-1p reduces trans-2-enoyl-CoA to acyl-CoA with chain length from C6 to C16 in an NADPH-dependent manner with preference to medium chain length substrate."],
and it restores respiratory growth to the yeast reductase mutant, which places the
activity in the mitochondrial pathway rather than in any cytosolic process
[PMID:12654921 "Furthermore, expression of HsNRBF-1 in the ybr026cDelta yeast strain restored mitochondrial respiratory function allowing growth on glycerol."].
UniProt's curated FUNCTION records that the physiological carrier is ACP while CoA
thioesters are accepted in vitro
[file:human/MECR/MECR-uniprot.txt "Fatty acid chain elongation in mitochondria uses acyl carrier"],
which is why the ACP-specific term `GO:0141148` is accepted as the core molecular
function even though the assays used CoA esters. Core location is the mitochondrial
matrix, matching the ETR1 and etr1 reviews.

## Annotation decisions, and why they match the paralogs

- `GO:0006631` fatty acid metabolic process (IBA, IDA, IMP — three rows): all three
  `MODIFY` to `GO:0006633` fatty acid biosynthetic process. The term is true but spans
  catabolism, and the family's shared role is biosynthetic. The yeast ETR1 and
  *S. pombe* etr1 reviews use `TOO_GENERAL` for their `GO:0006631` rows — but those
  reviews **already carry a separate `GO:0006633` row** that entails the general term,
  which is what `TOO_GENERAL` requires. MECR has no `GO:0006633` row, so the correct
  action here is `MODIFY` with that term as the replacement; the outcome is the same
  claim about the biology. The IBA row's `propagation_review` records PAINT node
  PTN000190628 (PTHR43981) as `SUPPORTS_TRANSFER` with a `GRANULARITY_MISMATCH`: the
  inheritance is sound, only the term is one level too high. MECR itself appears in
  that node's seed list, which is expected and not circular.
- `GO:0016491` oxidoreductase activity (IEA from IPR020843): `MODIFY` to `GO:0141148`,
  exactly as the *S. pombe* etr1 review does for its equivalent row.
- `GO:0005739` mitochondrion — five rows (HTP, IBA, two IDA, IEA): all `ACCEPT`. Per
  the root-organelle policy the organelle term is informative and is not modified to a
  sub-compartment; the assays behind these rows (MitoCoP proteomics, GFP/MitoTracker
  colocalization, antibody imaging) cannot resolve matrix from membrane.
  `GO:0005759` mitochondrial matrix (TAS, Reactome) is the row that carries the
  sub-compartment and is accepted as the core location: MECR is soluble, carries a
  cleavable targeting peptide whose loss in cMECR abolishes import, and acts on a
  matrix ACP thioester. No new IC sub-compartment row was needed, since the matrix row
  already exists.
- `GO:0006879` intracellular iron ion homeostasis and `GO:0046513` ceramide
  biosynthetic process (both IMP, `acts_upstream_of`, PMID:37653044): both
  `KEEP_AS_NON_CORE`. The genetics are strong — fly *mecr* mutants and MECR patient
  fibroblasts accumulate iron
  [PMID:37653044 "Compared to the control cells, fibroblasts from both patients displayed an elevated level of iron"]
  and ceramide, and mitochondrial aconitase activity drops by more than half
  [PMID:37653044 "We find that the enzymatic activity of aconitase is significantly reduced in mecr mutants (>50%) (Fig. 8b) suggesting a defect in Fe-S cluster biogenesis."] —
  but MECR performs no step of either process: the chain runs through the acyl-ACP
  products that Fe-S cluster assembly needs, and ceramide rises downstream of iron. The
  `acts_upstream_of` qualifier states that indirectness correctly, so these rows are
  kept rather than removed, and are deliberately **not** promoted to `involved_in`.
  This is the "necessity is not participation" case from CLAUDE.md.

## The cytosolic isoform, and the NRBF-1 name

The `GO:0005634` nucleus and `GO:0005737` cytoplasm rows (IEA from UniProt's
subcellular-location vocabulary) are not errors and are not generic parents of the
mitochondrion rows: UniProt records them for **isoform 2 only** (Q9BV79-2, cMECR), a
splice variant whose N-terminal region lacks the mitochondrial targeting peptide
[PMID:25031892 "The protein generated from this splicing variant has an N-terminal region that does not contain the mitochondrial targeting signal peptide and thus is not localized in mitochondria."].
cMECR distributes through cytoplasm and nucleus and binds PPARα there
[PMID:25031892 "cMECR directly bound PPARα in the nucleus and increased PPARα-dependent luciferase activity in HeLa cells."].
That resolves the old puzzle behind the gene's alias "nuclear receptor binding
factor 1": the yeast-two-hybrid interaction with a nuclear transcription factor cannot
involve a matrix enzyme, but it can involve this variant. Both rows are therefore
`KEEP_AS_NON_CORE`, and a `functional_isoforms` entry (`MECR_CYTOSOLIC`,
`SPLICE_VARIANT`, mapped to Q9BV79-2) records the two locations as
`isoform_specific_terms` so they are not read as properties of the canonical enzyme.
Caveat recorded in the reference review: the variant was characterized in rat tissues
and in HeLa cells, and no catalytic role in mtFAS is claimed for it.

## Disease context (not annotated as process terms)

Recessive MECR mutations cause MEPAN syndrome, a childhood-onset dystonia with optic
atrophy
[PMID:27817865 "All affected individuals were found to harbor recessive mutations in MECR encoding the mitochondrial trans-2-enoyl-coenzyme A-reductase involved in human mtFAS."],
with reduced protein lipoylation and defective respiration in patient fibroblasts.
Lipoylation and respiration are downstream consequences of the missing acyl-ACP
products; lipoyl transfer is modelled in `modules/endogenous_protein_lipoylation.yaml`,
so no lipoylation or respiration process term is proposed here.

## Reference correction

The stub's machine-fetched title for PMID:34800366 did not match the cached
publication; the real paper is the MitoCoP mitochondrial-proteome study
(Morgenstern et al., Cell Metab 2021), which is the actual source of the HTP
mitochondrion row and is now cited as such.
