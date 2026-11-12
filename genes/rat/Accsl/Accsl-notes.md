# Curatorial Notes for Rat `Accsl` (`UniProtKB:D3ZUW2`)

## 1. Identity, Gene Model, and Phylogeny
- **Gene symbol / IDs**: `Accsl` (`RGD:1596039`, `NCBIGene:690470`), encoded on rat chromosome 3 adjacent to paralog `Accs` (`RGD:1309314`), conserving the eutherian `ACCS`–`ACCSL` tandem duplication [PMID:39876065].
- **UniProtKB**: `D3ZUW2` (`D3ZUW2_RAT`, unreviewed TrEMBL entry, sequence version 1, 617 aa, `PE 4: Predicted`), assigned to **`PANTHER:PTHR43795:SF1`** (*INACTIVE 1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 2-RELATED*).
- **Sequence & domain note**: Contains an extended disordered N-terminus (residues 1..42), the fold-type I aminotransferase-like domain (`PF00155`, residues 195..562), and a short disordered C-terminal tail (residues 579..617). Note that Ensembl GRCr8 merged `ENSRNOT00000068585.3` (`D3ZUW2`, `Accsl`) and `ENSRNOT00000012214.9` (`A0A8J8YIP6`, `Accs`) under `ENSRNOG00000042533.3`, giving `D3ZUW2` the misleading Ensembl-derived `SubName: Full=1-aminocyclopropane-1-carboxylate synthase`.

## 2. Literature Search Log
- Targeted PubMed and Europe PMC searches for `("Accsl" OR "D3ZUW2" OR "RGD:1596039" OR "690470") AND ("rat" OR "Rattus norvegicus")`:
  - Zero experimental publications investigate rat `Accsl` biochemistry, cofactor binding, subcellular localization, or in vivo function.

## 3. Active-Site Residue Comparison (`D3ZUW2` sv 1 vs Human `Q96QU6` sv 1 & `Q4AC99` sv 3)
- `Tyr228` / `Trp231` (`Q96QU6` `Tyr132` / `Trp135`): **Retained**.
- `Asp382` (`Q96QU6` `Asp286`): **Retained** — canonical fold-type I pyridinium-stabilizing aspartate.
- `Lys419` (`Q96QU6` `Lys323`): **Retained** — putative Schiff-base lysine.
- `Tyr447` (`Q96QU6` `Arg351`; `Q4AC99` `Tyr423`; mouse `Q3UX83` `Tyr445`): **Lost** (`R -> Y`) — shares the clade-defining `SF1` tyrosine substitution at the partner-monomer pocket position whose surrogate mutation (`R351Y`) in human `ACCS` reduces C-beta-S lyase activity ~40-fold (`PMID:39876065`).
- `Arg553` (`Q96QU6` `Arg457`; `Q4AC99` `Cys529`; mouse `Q3UX83` `Arg551`): **Retained** (`R`) — like mouse `Accsl` and other non-human mammals, rat `Accsl` preserves the substrate alpha-carboxylate-anchoring arginine (`PMID:39876065` Figure 2).

## 4. Annotation Decisions
- `GO:0006520` (`IBA`, `PTN002887088`) & `GO:0008483` (`IBA`, `PTN002887088`): `REMOVE` — stale propagations from retired plant aminotransferase PAINT node `PTN002887088`; current PAINT blocks catalytic propagation into `SF1` via an explicit `IKR` loss gate at `PTN000202914`.
- `GO:0030170` (`IEA`, `InterPro:IPR004839`): `MARK_AS_OVER_ANNOTATED` — unverified InterPro2GO domain projection onto a predicted (`PE 4`) member of putative pseudoenzyme clade `PTHR43795:SF1` that substitutes `Tyr447` at the inter-subunit pocket and has never been assayed for PLP binding.
