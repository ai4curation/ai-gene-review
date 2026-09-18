# RHOJ (G3V4H1): evidence and exact-input prediction review

The full-length RHOJ/TCL protein is an active, rapidly exchanging GTPase, contrary to a generic GTPase-deficient Rho-family description. However, G3V4H1 is a substantially altered short product, so its activity cannot be decided from the full-length result in either direction.

## Input identity and functional boundary

G3V4H1 and Q9H4E5 share HGNC:688. The first 103 residues match exactly; the remainder is highly divergent. The reference guanine-binding residue 136 is not aligned to the target, reference binding residue 177 is not conserved, and the terminal lipidation region is absent from the conserved segment. Retaining the P-loop and switch-region segment alone does not establish a functional G-domain.

## Biological evidence

- [PMID:10967094 — Characterization of TCL, a new GTPase of the rho family related to TC10 andCcdc42.](https://pubmed.ncbi.nlm.nih.gov/10967094/): Full-length human TCL/RHOJ has intrinsic GTP hydrolysis activity, distinguishing it from GTPase-deficient Rho-family proteins.

> In vitro, TCL shows rapid GDP/GTP
> exchange and displays higher GTP dissociation and hydolysis rates than TC10.

- [PMID:27660391 — TCL/RhoJ Plasma Membrane Localization and Nucleotide Exchange Is Coordinately Regulated by Amino Acids within the N Terminus and a Distal Loop Region.](https://pubmed.ncbi.nlm.nih.gov/27660391/): Human RHOJ nucleotide exchange and membrane localization depend on sequence regions including a distal loop; this supports caution for an altered C-terminal product.

> Chimeras of TCL and TC10
> revealed amino acids 121-129 of TCL contributed to the differences in nucleotide
> loading.

## Exact non-GO claims

The complete emitted record is preserved in [RHOJ-protnlm-source.json](RHOJ-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Cell division control protein 42 homolog

LSP (CS 2) if “homolog” is read as a broad relationship: RHOJ is demonstrably Cdc42-related. The name is less informative than RHOJ/TCL and must not be read as identifying the CDC42 paralog or guaranteeing an intact Cdc42-like enzyme. [PMID:10967094](https://pubmed.ncbi.nlm.nih.gov/10967094/).

### Function

> Binds GTP but lacks intrinsic GTPase activity and is resistant to Rho-specific GTPase-activating proteins

UNC (CS 1) for the selected G3V4H1 product. The “lacks intrinsic GTPase activity” description is contradicted for full-length RHOJ by direct hydrolysis measurements, but the target has a divergent, incomplete G-domain. The conjunction “binds GTP but lacks hydrolysis and resists GAPs” requires binding, hydrolysis and GAP assays of this exact product; a truncation alone does not establish an atypical GTPase mechanism. [PMID:10967094](https://pubmed.ncbi.nlm.nih.gov/10967094/); [sequence mapping](RHOJ-bioinformatics/RESULTS.md).

### Location

> Membrane

UNC (CS 1). The selected product does not retain the reference C-terminal membrane-targeting region, and RHOJ membrane association is sensitive to sequence-dependent nucleotide loading. Partner-mediated membrane association remains possible, so no exclusively cytosolic alternative is asserted. [PMID:27660391](https://pubmed.ncbi.nlm.nih.gov/27660391/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

PTHR24072 establishes Rho-family ancestry but includes paralogs with different nucleotide cycling properties. The experimentally characterized RHOJ branch is catalytically active. The selected altered product creates an additional product-integrity boundary beyond family membership.

## Evidence limits

The original RHOJ paper is abstract-only in the cache; the 2016 mechanistic study has full text. Neither tests G3V4H1. A confident pseudoenzyme designation would conflate a potentially incomplete product with a stable, evolved GTPase-deficient signaling protein.

Exact sequence mapping: [RHOJ-bioinformatics/RESULTS.md](RHOJ-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Research integration

The genuine Falcon report is retained. Its gene-level synthesis is interpreted through the exact product sequence and the primary sources above; the truncation boundary and paralog distinctions are assessed independently.
