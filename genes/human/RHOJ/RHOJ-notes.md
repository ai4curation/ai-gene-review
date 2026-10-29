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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: G3V4H1 (ProtNLM2 benchmark target, cohort MOD_EVOLUTION20). No ProtNLM2 file or prediction output was opened or used. New analysis: `RHOJ-bioinformatics/compare_sequences_rereview.py` -> `RESULTS-rereview.txt` / `RESULTS-rereview.md`, which fetch sequences and transcript models live from UniProt and Ensembl. The earlier `RESULTS.md` and its scripts are unchanged.

### Identity of the benchmark accession

- G3V4H1 is an **alternative gene model**, not the canonical RHOJ product and not one of the UniProt-described isoforms. It is 153 aa; canonical Q9H4E5 is 214 aa, and isoform 2 (Q9H4E5-2) lacks only residues 113-134 and keeps the canonical C-terminus.
- It is translated from ENST00000557447 (RHOJ-204), Ensembl biotype **nonsense_mediated_decay**. The CDS matches canonical RHOJ-201 to nt 305. RHOJ-204 then uses a shortened exon 3, skips exon 4 and splices into the canonical 3' UTR. The 50-residue proline-rich tail (104-153) is read from sequence just 3' of the canonical stop codon, and it is not a frameshifted read of canonical coding sequence.
- Retained: G1 P-loop (GDGAVGKT, 28), switch I (PTVFD, 52), switch II (DTAGQ, 75), effector region 50-58, N-terminal palmitoylation cysteines 3 and 11. Missing: the 121-129 distal loop needed for nucleotide loading [PMID:27660391 "Chimeras of TCL and TC10 revealed amino acids 121-129 of TCL contributed to the differences in nucleotide loading."], the G4 TQID (133), the G5 CSAL (175), the polybasic region and the CAAX box (CSII, 211).
- PE 1 on the TrEMBL record comes from PeptideAtlas. Peptides from shared residues 1-103 cannot tell this product apart from the canonical one, so the PE level is not evidence that G3V4H1 exists as a polypeptide.

### Evolutionary grounding

- PANTHER PTHR24072 (Rho family GTPase). The PANTHER 19 geneinfo service places canonical Q9H4E5 in PTHR24072:SF17 (RHO-RELATED GTP-BINDING PROTEIN RHOJ). G3V4H1 is unmapped there; it only matches the family HMM over residues 20-103 (InterPro API). GTPase activity, GTP binding and plasma membrane are IBD-placed at the family root, PTN000632671, and Q9H4E5 is among the donors. Because the function is ancestral to the whole family, it holds for the RHOJ gene. G3V4H1 itself receives no IBA; its three rows are InterPro/UniRule/EC-mapping IEAs triggered by the N-terminal half-domain.
- The family review (`interpro/panther/PTHR24072/PTHR24072-review.yaml`) already names G3V4H1 as an altered same-gene product and does not dispute subfamily placement. I found no disagreement.

### Decisions

All three IEAs (GTPase activity, G protein activity, GTP binding) changed from UNDECIDED to **MARK_AS_OVER_ANNOTATED**. They are true of the gene and of Q9H4E5 [PMID:10967094 "In vitro, TCL shows rapid GDP/GTP exchange and displays higher GTP dissociation and hydolysis rates than TC10."]. They are not supported for an NMD-transcript product that lacks the guanine-base motifs and half the fold. I did not use REMOVE, because no assay of this product exists and the claims are correct at gene level. The description was rewritten so that it gives the gene-level biology [PMID:21628409; PMID:30158707] and then the product-identity boundary. core_functions stays empty, since no function is established for this product. No NEW terms were proposed.

### Relative to review next

The canonical product of the same gene, Q9H4E5 (RHOJ_HUMAN, reviewed). `genes/human/RHOJ` is keyed to G3V4H1, and no review of Q9H4E5 exists in the repo, so the next folder would be `genes/human/RHOJ__Q9H4E5`. No module names RHOJ or Q9H4E5. These modules use PTHR24072 Rho-family descriptors and are context only: `modules/rho_gprotein_signaling.yaml`, `modules/ephrin_receptor_signaling.yaml`, `modules/chemokine_signaling.yaml`, `modules/phagocytic_engulfment.yaml`.

## 2026-10-29: function narrative rescored

The function narrative (`RHOJ-protnlm-function-review.md`) now scores "binds GTP" as NPI
(DOMAIN_ARCHITECTURE_MISMATCH) for G3V4H1. GTP binding is true of the gene, but guanine binding needs
the G4 (TQID) and G5 (CSAL) motifs, and G3V4H1 keeps only the P-loop, switch I and switch II before
diverging after residue 103. "Lacks intrinsic GTPase activity and is resistant to Rho-specific GAPs"
stays UNC. This supersedes the single UNC given under "Exact non-GO claims" above.
