# DCAF12 (DDB1- and CUL4-associated factor 12) review notes

UniProt: **Q5T6F0** → **DCAF12**. PANTHER: PTHR19860. Taxon: 9606.

## Core function (standalone summary)

DCAF12 is the **substrate-recognition subunit (substrate receptor)** of a **CRL4
(DDB1-CUL4A/B-RBX1) E3 ubiquitin ligase** operating in the **DesCEND / C-end degron**
pathway. It recognises C-terminal acidic degrons — a **diglutamate** motif, and the
alternative **Glu-Leu** degron — and presents degron-bearing substrates (e.g. **MOV10**,
**MAGE-A3/A6**) to the ligase for ubiquitination and proteasomal degradation. Acts in
the nucleus and cytoplasm as part of the Cul4-RING complex.

## Key evidence (provenance)

- UniProt Q5T6F0 CC:FUNCTION: "Substrate-recognition component of a DCX
  (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via
  C-end degrons) pathway, which recognizes a C-degron located at the extreme C
  terminus"; "DCX(DCAF12) complex specifically recognizes proteins with a diglutamate";
  "Also directly recognizes the C-terminal glutamate-leucine (Glu-Leu) degron ... in
  proteins such as MOV10". CC:SUBUNIT: "Component of the DCX(DCAF12) E3 ubiquitin ligase
  complex, at least composed of CUL4 (CUL4A or CUL4B), DDB1, DCAF12 and RBX1."
- [PMID:34065512 abstract]: "Multisubunit cullin-RING ubiquitin ligase 4 (CRL4)-DCAF12
  recognizes the C-terminal degron containing acidic amino acid residues." (MOV10 in
  spermatogenesis.)
- [PMID:29779948 abstract]: "The Eukaryotic Proteome Is Shaped by E3 Ubiquitin Ligases
  Targeting C-Terminal Degrons." Establishes the C-end degron pathway and DCAF12.
- [PMID:31267705 abstract]: CRL4-DCAF12 controls MAGE-A3/6 degradation.

## Annotation landscape (GOA, 29 rows)

- Adaptor MF: GO:1990756 ubiquitin-like ligase-substrate adaptor activity (IDA x3) — core.
- Complex (part_of, core): GO:0080008 Cul4-RING E3 ubiquitin ligase complex;
  GO:0031464 Cul4A-RING; GO:0031465 Cul4B-RING.
- Core process: GO:0140627 ubiquitin-dependent protein catabolic process via the C-end
  degron rule pathway (IDA x3); GO:0016567 protein ubiquitination.
- protein binding (IPI): all three rows are to DDB1 (Q16531), i.e. docking into the CRL4
  complex -> REMOVE (complex membership captured by part_of).
- Downstream-of-substrate (KEEP_AS_NON_CORE): GO:0010506 regulation of autophagy
  (acts_upstream_of), GO:0042110 T cell activation, GO:0042127 proliferation,
  GO:0060964 regulation of miRNA-mediated gene silencing (via MOV10 degradation).
- Locations (ACCEPT): nucleus, cytoplasm, cytosol, centrosome.
