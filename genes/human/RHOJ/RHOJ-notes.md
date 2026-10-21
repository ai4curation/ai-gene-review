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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20 full re-review (independent of ProtNLM output)

This re-review replaces earlier notes that mixed annotation review with a review of
ProtNLM output. Those prediction assessments are not used as evidence here.

#### Identity of the benchmark accession

- G3V4H1 (TrEMBL, 153 aa) is the translation of Ensembl ENST00000557447 (RHOJ-204).
  Ensembl annotates this transcript as `nonsense_mediated_decay`. It is not the canonical
  product. The canonical product is Q9H4E5 (Swiss-Prot, 214 aa), from ENST00000316754
  (RHOJ-201) [file:human/RHOJ/RHOJ-bioinformatics/RESULTS.md].
- Residues 1-103 are identical to Q9H4E5. Residues 104-153 are an unrelated tail that
  MobiDB-lite predicts to be disordered (124-153) and that is rich in Pro and His.
- The product keeps: the N-terminal extension, including the DEKK 17-20 determinant of
  nucleotide loading [PMID:27660391]; the N-terminal palmitoylation sites C3 and C11 of
  Q9H4E5; the G1 P-loop (28-35); switch I and the effector region (50-58); and the G3
  DTAGQE motif (75-80).
- The product lacks: the G4 (TQID, 133-136) and G5 (SAL, 176-178) guanine-base recognition
  motifs; the distal loop 121-129 that regulates nucleotide loading [PMID:27660391 "Chimeras
  of TCL and TC10 revealed amino acids 121–129 of TCL contributed to the differences in
  nucleotide loading."]; the polybasic region; and the CAAX box (C211 farnesylation).
- PANTHER v19 gene-info lookup places Q9H4E5 in PTHR24072:SF17 ("RHO-RELATED GTP-BINDING
  PROTEIN RHOJ"). G3V4H1 is unmapped there. InterPro places it in PTHR24072 at the family
  level only, on residues 20-103.
- The UniProt "Belongs to the small GTPase superfamily. Rab family" similarity line on
  G3V4H1 is a PROSITE-ProRule artefact. InterPro IPR003578 (Small_GTPase_Rho), PANTHER
  and the literature all place RHOJ in the Rho/Cdc42 subfamily.
- PE 1 on G3V4H1 comes from PeptideAtlas identifications. These may be peptides shared
  with the canonical product. No peptide unique to the tail is documented.

#### Gene-level biology (canonical Q9H4E5)

- Fast-exchanging, hydrolytically active GTPase [PMID:10967094 "In vitro, TCL shows rapid
  GDP/GTP exchange and displays higher GTP dissociation and hydolysis rates than TC10."].
- Localization depends on activation state (plasma membrane versus EEA1/Rab5 endosomes)
  [PMID:27660391].
- Endothelial-enriched and an ERG target. Required for lumen and tube formation
  [PMID:21628409; PMID:21148427 "RhoJ is endothelial-expressed in vivo, activated by vascular
  endothelial growth factor, localizes to focal adhesions..."].
- GTP-bound RHOJ binds the PlexinD1 cytoplasmic domain and integrates Sema3E and VEGF
  cues [PMID:32347571].

#### Evolutionary grounding

- PAINT node PTN000632671 (Rho-family root, PTHR24072) carries IBD GTPase activity,
  GTP binding and plasma membrane. Q9H4E5 is among the seeds. The node supports these
  functions for the RHOJ lineage. The question for G3V4H1 is not lineage loss but product
  integrity.
- Closest characterised relative by phylogeny: mouse Rhoj (Q9ER71), the SF17 ortholog,
  characterised in endothelial knockout and retinal angiogenesis studies
  [PMID:32347571]. The repo has no mouse Rhoj review, and no review of human canonical
  Q9H4E5 as a separate accession (this folder is G3V4H1).

#### Decisions

All three IEA MF rows (GTPase activity, G protein activity, GTP binding) are marked
MARK_AS_OVER_ANNOTATED. The terms are correct for RHOJ but not supported for an
NMD-transcript product that lacks half the G domain. They are not removed, because the
claims are true of the gene. core_functions is left empty because no function is
supported for this product.

#### Family / modules

- interpro/panther/PTHR24072/PTHR24072-review.yaml lists G3V4H1 under "Benchmark members
  without resolved subfamily placement". This matches the PANTHER lookup (G3V4H1 is
  unmapped at subfamily level, while canonical RHOJ is SF17). The family review does not
  mention the NMD biotype.
- No module in modules/ includes RHOJ. RHOJ appears only in falcon deep-research artifacts
  for the FGFR, Fc-gamma receptor, death-receptor and Nodal modules, as incidental text.

#### Deep research

The falcon report (RHOJ-deep-research-falcon.md) is gene-level and accurate on endothelial
biology. It correctly flags that the "Rab family" label is wrong. It does not analyse the
G3V4H1 product.
