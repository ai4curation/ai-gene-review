# Curatorial Notes for Zebrafish abhd10b (UniProtKB:E7F9Y7)

## Summary of Gene Product, Synteny & Resolution of Historical `tagln3b` Mislabeling

- **Protein**: Palmitoyl-protein thioesterase ABHD10, mitochondrial (`UniProtKB:E7F9Y7`, sequence version 1; 289 aa; `ZFIN:ZDB-GENE-041111-196`, `GeneID:492622`, chromosome 24; `PANTHER:PTHR16138:SF7`).
- **Resolution of Historical PANTHER 19.0 `tagln3b` Mis-mapping**:
  - In `.cache/panther/PTHR19.0_zebrafish`, leaf `E7F9Y7` in `PTHR16138:SF7` carried a stale ZFIN cross-reference (`ZFIN=ZDB-GENE-030131-4199`, `tagln3b`). Inspection of `E7F9Y7_DANRE` confirms that `E7F9Y7` is **not** transgelin-3b (true zebrafish `tagln3b` is the 199-aa calponin-homology actin-binding protein `UniProtKB:Q6P697`), but rather the genuine 289-aa alpha/beta-hydrolase **`abhd10b`** (`PF00561` residues 62-166, `IPR052382`, `ZFIN:ZDB-GENE-041111-196`) encoded adjacent to `tagln3b` on zebrafish chromosome 24—conserving the ancestral vertebrate `ABHD10`–`TAGLN3` synteny seen at human 3q13.2.
  - Because of that historical locus/RefSeq cross-link to `tagln3b`, `E7F9Y7-uniprot.txt` (`RN [1]`, via `RefSeq:NP_001373402.1`) still lists `PMID:26469318` (*"RFX transcription factors are essential for hearing in mice"*), a mouse hair-cell transcriptomics paper that does not study zebrafish `abhd10b`.
- **Catalytic Triad Conservation**:
  - `abhd10b` (`E7F9Y7`) is a teleost whole-genome duplication (`PMID:27189481`) co-ortholog of tetrapod `ABHD10` alongside `abhd10a` (`A0A0R4ILM1`), strictly conserving the alpha/beta-hydrolase charge-relay triad at **Ser136** (in the `GSSMG` nucleophilic elbow), **Asp233**, and **His263** (`PMID:22294686`, `PMID:31740833`).

## Literature Search for ND Policy Verification

- Systematic PubMed searches conducted on 2026-11-11 for `"abhd10b"`, `("abhd10" AND ("zebrafish" OR "Danio rerio"))`, `"ZDB-GENE-041111-196"`, `"im:7144007"`, and `"E7F9Y7"` returned 0 publications reporting experimental molecular function, biological process, or subcellular localization data on zebrafish `abhd10b`.

## Key Curation Decisions

- **`ND` Root Annotations (`GO:0003674` MF, `GO:0005575` CC, `GO:0008150` BP; `GO_REF:0000015`, assigned by `ZFIN`) -> `ACCEPT`**:
  - Per the ND Policy (`projects/NO_DATA.md`), all three ZFIN `ND` rows accurately reflect the complete absence of species-specific experimental literature on *Danio rerio* `abhd10b` (ortholog-derived `IBA` and electronic `IEA` rows do not render an `ND` stale):
    - `GO:0003674` (`molecular_function`, `ND`): `ACCEPT` with `nd_case: INFERABLE` (covered by accepted `IBA`/`IEA` rows for `GO:0008474`).
    - `GO:0005575` (`cellular_component`, `ND`): `ACCEPT` with `nd_case: INFERABLE` (covered by accepted `IBA`/`IEA` rows for `GO:0005739`).
    - `GO:0008150` (`biological_process`, `ND`): `ACCEPT` with `nd_case: TRUE_GAP`, paired with a `BIOLOGY` (`BP_DARK`) `knowledge_gaps` entry because no non-obsolete biological process annotation is supported in zebrafish and the physiological division of labor between teleost TGD paralogs `abhd10a` and `abhd10b` across redox homeostasis and gametogenesis is unknown.
- **`GO:0008474` (`palmitoyl-(protein) hydrolase activity`, `IBA` `PTN001043685` and `IEA` `GO_REF:0000120`)**: `ACCEPT` (with `propagation_review` and `residue_claims` confirming retention of `Ser136` aligned to `Q9NUJ1` `Ser152`).
- **`GO:0005739` (`mitochondrion`, `IBA` `PTN001043685` and `IEA` `GO_REF:0000044`)**: `ACCEPT` per the Root Organelle Policy (no `NEW` `GO:0005759` added because `E7F9Y7` lacks an annotated transit-peptide cleavage boundary and fish sub-organellar assays).
- **`GO:0004553` (`hydrolase activity, hydrolyzing O-glycosyl compounds`, `IBA` `PTN004490000`)**: `REMOVE` (`SOURCE_BAD` / `SOURCE_MISCITATION` from erroneous `GO:0004553` on human `Q9NUJ1` in `PMID:22294686`).
- **`GO:0098734` (`obsolete macromolecule depalmitoylation`, `IEA` `GO_REF:0000108`)**: `MODIFY` -> `GO:0008474`.
- **`GO:0102390` (`mycophenolic acid acyl-glucuronide esterase activity`, `IEA` `GO_REF:0000003` via `EC:3.1.1.93`)**: `MARK_AS_OVER_ANNOTATED` (automated projection of human hepatic drug-conjugate esterase activity onto a teleost paralog).
