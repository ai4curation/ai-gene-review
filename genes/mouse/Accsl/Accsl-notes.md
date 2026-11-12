# Curatorial Notes for Mouse `Accsl` (`UniProtKB:Q3UX83`)

## 1. Identity, Synteny, and Isoforms
- **Gene symbol / IDs**: `Accsl` (synonym `Gm1967`; `MGI:3584519`, `NCBIGene:381411`, `ENSMUSG00000075023`), encoded on mouse chromosome 2 tandemly adjacent to `Accs` (`MGI:1919717`), conserving the eutherian `ACCS`–`ACCSL` locus architecture [PMID:39876065].
- **UniProtKB**: `Q3UX83` (`1A1L2_MOUSE`, sequence version 1, 580 aa), assigned to **`PANTHER:PTHR43795:SF1`** (*INACTIVE 1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 2-RELATED*).
- **Isoforms**:
  - `Q3UX83-1`: Canonical 580-residue polypeptide containing an extended disordered N-terminal tail (residues 1..43) followed by the fold-type I aminotransferase-like domain.
  - `Q3UX83-2` (`VSP_033860`): 528-residue splice variant missing N-terminal residues 1..52 while retaining the complete fold-type I domain.

## 2. Literature Search Log (Supporting `ND` Curation)
- Targeted PubMed and Europe PMC searches for `("Accsl" OR "Gm1967" OR "Q3UX83" OR "Q3TQ30" OR "MGI:3584519" OR "381411") AND ("mouse" OR "Mus musculus" OR "murine" OR "zygote")`:
  - Zero experimental publications assay purified mouse `Accsl` cofactor binding, enzymatic activity, subcellular localization, or loss-of-function phenotypes (`GO:0005575` `ND` is verified as `TRUE_GAP`).
  - Only FANTOM3/genome sequencing (`PMID:16141072`, `PMID:19468303`) and comparative phylogenetic/sequence analyses in Gao et al. 2025 (`PMID:39876065`, Figures 1b and 2) cover non-human mammalian `ACCSL` orthologs.

## 3. Active-Site Residue Comparison (`Q3UX83` sv 1 vs Human `Q96QU6` sv 1 & `Q4AC99` sv 3)
- `Tyr226` / `Trp229` (`Q96QU6` `Tyr132` / `Trp135`): **Retained**.
- `Asp380` (`Q96QU6` `Asp286`): **Retained** — canonical fold-type I pyridinium-stabilizing aspartate.
- `Lys417` (`Q96QU6` `Lys323`): **Retained** (`FT MOD_RES 417` by similarity) — putative Schiff-base lysine.
- `Tyr445` (`Q96QU6` `Arg351`; `Q4AC99` `Tyr423`): **Lost** (`R -> Y`) — shares the eutherian `SF1` arginine-to-tyrosine substitution at the partner-monomer pocket position whose surrogate mutation (`R351Y`) in human `ACCS` reduces C-beta-S lyase activity ~40-fold (`PMID:39876065`).
- `Arg551` (`Q96QU6` `Arg457`; `Q4AC99` `Cys529`): **Retained** (`R`) — unlike reference human `ACCSL` (`Cys529`), mouse `Accsl` preserves the canonical substrate alpha-carboxylate-anchoring arginine (`Arg551`), directly confirming Gao et al. 2025 (`PMID:39876065`, `"Interestingly, this arginine-to-cysteine substitution is unique to hACCSL, as the arginine residue is conserved in other non-human ACCSL orthologues (Figure 2)."`).

## 4. Annotation Decisions
- `GO:0005575` (`ND`, `GO_REF:0000015`): `ACCEPT` (`nd_case: TRUE_GAP`), paired with `[BIOLOGY]` `WHOLLY_DARK` knowledge gap.
- `GO:0006520` (`IBA`, `PTN002887088`) & `GO:0008483` (`IBA`, `PTN002887088`): `REMOVE` — stale propagations from retired plant aminotransferase PAINT node `PTN002887088`; current PAINT places an explicit `IKR` loss gate at the `SF1` ancestral node `PTN000202914`.
- `GO:0030170` (`IEA`, `InterPro:IPR004839`): `MARK_AS_OVER_ANNOTATED` — although `Q3UX83` retains `Lys417`, `Asp380`, and `Arg551`, it carries the clade-defining `SF1` `Tyr445` active-site substitution (plus `Ser295` at `hACCS` `His201`), is flagged in UniProt `CC:CAUTION` as probably catalytically inactive, and has never been tested for PLP binding in any mammal.
