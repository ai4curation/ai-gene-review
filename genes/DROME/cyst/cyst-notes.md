# Curation Notes: *Drosophila melanogaster* `cyst` (`UniProtKB:M9PBE1`, `FB:FBgn0032796`)

## 1. Gene Identity, Nomenclature & Phylogenetic Position
- **Gene symbol / FlyBase ID**: `cyst` (*cysts*; synonyms `CG10188`, `Dp114RhoGEF`; `FB:FBgn0032796`).
- **UniProtKB record**: `UniProtKB:M9PBE1` (`M9PBE1_DROME`, sequence version `1`, 1,334 aa; isoform B of CG10188). Alternative *Drosophila* UniProt entries for the same locus include `Q9VIV0` (1,288 aa) and `Q8MQR4`.
- **PANTHER 19.0 classification**: `PANTHER:PTHR13944:SF21` (*RHO GUANINE NUCLEOTIDE EXCHANGE FACTOR CYSTS*), representing the single-copy invertebrate/protostome ortholog of the four vertebrate Lbc-family RhoGEFs (`ARHGEF18`/p114RhoGEF in `SF23`, `ARHGEF2`/GEF-H1 in `SF20`, `ARHGEF28`/p190RhoGEF in `SF22`, and `AKAP13`/AKAP-Lbc in `SF18`) [PMID:31409654].
- **MOD description status**: `just mod-description-deep-research DROME cyst` (`ai-gene-review mod-description-deep-research DROME cyst`) queried Alliance `/api/gene/FB:FBgn0032796` and returned `no_curated: 1` (`FB:FBgn0032796 has no curated description` — FlyBase `FBgn0032796` has only an automated GO-derived synopsis and no hand-written `MOD_provided_gene_description` gene snapshot), so per `AGENTS.md` no `cyst-deep-research-flybase.md` file was fabricated.

## 2. Domain Architecture & Catalytic Residue Conservation (`M9PBE1`, `sv=1`, 1,334 aa)
- **N-terminal C1-like zinc finger**: `343-CDVC-346` (`Cys343` aligns with `Cys53` of human `ARHGEF2` `Q92974`, `site_ref: PANTHER:PTHR13944#c1_zn_finger_cys53`).
- **Dbl-homology (DH) catalytic domain**: residues `442-637` (`PROSITE:PRU00062`), preserving both family-wide catalytic anchor residues:
  - CR1 Switch-I-remodeling glutamate: `Glu449` (`444-QEVIFELIQTEM-455`; aligns with `Glu242` of `Q92974` and `Glu2001` of `Q12802`, `site_ref: PANTHER:PTHR13944#dh_cr1_catalytic_glu`).
  - CR3 Switch-II-stabilizing tyrosine: `Tyr590` (`585-QRLTKYPL-592`; aligns with `Tyr394` of `Q92974`, `Tyr2153` of `Q12802`, and `Tyr606` of `Q6ZSZ5`, `site_ref: PANTHER:PTHR13944#dh_cr3_catalytic_tyr`).
- **Pleckstrin-homology (PH) domain**: residues `668-799` (`PROSITE:PRU00145`), followed by C-terminal coiled-coil (`887-949`) and intrinsically disordered polarity-recruitment tail (`965-1334`).

## 3. Synthesized Biological Function from Primary Literature
1. **Apical polarity-coupled Rho1 activation at adherens junctions (`PMID:31409654`)**:
   - Maternal loss or knockdown of `cyst` (`CG10188`) causes embryonic epithelial collapse into hollow cuticle-lined vesicles/cysts phenocopying *crumbs* (*crb*) mutants [PMID:31409654].
   - Cysts is recruited to the apico-lateral membrane / adherens junction belt via interactions of its C-terminal region with the Crumbs complex and Bazooka/Par-3, where its DH/PH module activates Rho1 (and not Rac1/Cdc42) to stabilize junctional non-muscle myosin II and maintain adherens junction integrity during gastrulation [PMID:31409654].
2. **Cleavage furrow mechanosensing and de novo junction assembly during epithelial cytokinesis (`PMID:36917931`)**:
   - Systematic GFP-tagged RhoGEF/GAP imaging in *Drosophila* pupal notum epithelium showed Cysts localizing to the cleavage furrow rim during contractile ring ingression, where Cysts acts via Rho1 in the neighbor mechanosensing response to juxtapose daughter-cell membranes ahead of de novo adherens junction assembly (acting sequentially with Rac-directed RhoGEF4 at the midbody) [PMID:36917931].

## 4. Audit of Existing GOA Rows (10 rows) & Conservative `NEW` Additions (2 rows)
- **`GO:0005085` (`guanyl-nucleotide exchange factor activity`)** (`IBA`, `IDA` `PMID:36917931`, `IEA`, `ISS` from *Drosophila* paralog `FB:FBgn0023172` = `RhoGEF2`): All 4 rows `ACCEPT`. Note on the FlyBase `ISS` rows (`GO:0005085` and `GO:0035025` from `FB:FBgn0023172`): `FBgn0023172` is *Drosophila* `RhoGEF2` (`PDZ-RhoGEF` family `PTHR12858`), a paralogous Rho1-specific Dbl GEF rather than an ortholog, but both `GO:0005085` and `GO:0035025` are independently confirmed directly on `cyst` (`PMID:31409654`, `PMID:36917931`).
- **`GO:0007264`** (`IBA`) and **`GO:0035023`** (`IBA`): Both `MODIFY` -> `GO:0035025` (`positive regulation of Rho protein signal transduction`), already present on `cyst` and directly established in vivo (`PMID:31409654`, `PMID:36917931`).
- **`GO:0035025`** (`ISS`): `ACCEPT` (core process, directly supported on `cyst` by `PMID:31409654` and `PMID:36917931`).
- **`GO:0005737` (`cytoplasm`, `IEA`)**: `MODIFY` -> `GO:0005938` (`cell cortex`, cytoplasmic `part_of` descendant) alongside junctional/furrow membrane-proximal compartments `GO:0005912` (`adherens junction`) and `GO:0090688` (`cleavage furrow rim`).
- **`GO:0090688` (`cleavage furrow rim`, `IDA` `PMID:36917931`)**: `ACCEPT`.
- **`GO:1902408` (`mitotic cytokinesis, division site positioning`, `IEP` `PMID:36917931`)**: `MARK_AS_OVER_ANNOTATED` — in `PMID:36917931`, Cysts acts during late contractile ring ingression to mediate neighbor mechanosensing and daughter-daughter membrane juxtaposition for de novo junction formation, rather than positioning the mitotic division plane prior to furrow initiation (and `IEP` is an expression/localization code inappropriate for division-site positioning).
- **Proposed `NEW` annotations from uncurated founding paper `PMID:31409654` (full text cached)**:
  1. `GO:0005912` (`adherens junction`, `IDA`, `is_active_in`, `PMID:31409654`) — apico-lateral adherens junction belt where Cysts is recruited by Crumbs and Bazooka/Par3 to activate Rho1.
  2. `GO:0034332` (`adherens junction organization`, `IMP`, `involved_in`, `PMID:31409654`) — maternal/zygotic `cyst` loss disrupts adherens junction myosin II assembly and belt integrity, collapsing embryonic epithelia into cysts.
