# unc-83 (C. elegans) review notes

## Session 1 (2026-09-27, claude-code)

Context: KASH partner of UNC-84; reviewed for `modules/linc_complex.yaml` (KASH variants) and
`modules/nucleokinesis.yaml` (candidate C. elegans P-cell/hyp7 variant).

### Identity and family
- Q23064, W01A11.3; isoforms a/b/c differ at N-terminus (per deep research; UniProt entry lists no
  alternative products in the stub).
- UniProt carries no PANTHER family and no KASH InterPro/Pfam match (IPR012315/PF10541 absent);
  only UNC-83-specific Pfam domains (PF29142 UNC83_N, PF29152 middle bundle, PF29149 four bundle).
  The KASH peptide is short and divergent, lacking the conserved cysteine
  [file:worm/unc-83/unc-83-deep-research-falcon.md "The luminal KASH peptide is unusually short—approximately 18 residues—and lacks some features of longer canonical KASH domains, including the canonical cysteine used by some SUN–KASH pairs to form an intermolecular disulfide bond."].
  So UNC-83 is not a nesprin homolog beyond the KASH tail; no PANTHER id is asserted.

### Function (with provenance)
- KASH protein of the ONM, recruited by UNC-84 [PMID:16481402 "Caenorhabditis elegans UNC-83 was shown to localize to the outer nuclear membrane"].
- Binds UNC-84 SUN domain [PMID:11748140 "UNC-83 interacted with the SUN domain of UNC-84 in vitro"].
- Kinesin-1 cargo adaptor via KLC-2 [PMID:19605495 "UNC-83 interacts with and recruits KLC-2 to the nuclear envelope in a heterologous tissue culture system"].
- Dynein regulators: NUD-2/LIS-1 and BICD-1/EGAL-1/DLC-1 [PMID:20005871 "Instead, UNC-83 interacted with two dynein-regulating complexes; one consisting of BICD-1, EGAL-1, and DLC-1, and a second that includes NUD-2 and LIS-1."].
- Motor balance is cell-type specific: kinesin-1 major in hyp7 [PMID:20005871 "Kinesin-1 functions as the major force generator during nuclear migration"]; dynein major in P cells [PMID:27697906 "Finally, and in contrast to hyp7 nuclear migration, we found that cytoplasmic dynein was the primary motor for moving P-cell nuclei towards the minus ends of polarized microtubules."].

### Decisions
- protein binding: UNC-84 (x2) -> GO:0140444; KLC-2 -> GO:0019894 kinesin binding; DLC-1 -> GO:0045503;
  NUD-2, BICD-1 and the two WB-id rows (WBGene00011230 -> O45717 NUD-2, WBGene00016611 -> V6CJ04 BICD-1
  by UniProt text search) -> GO:0140444.
- GO:0034993 meiotic complex -> MODIFY GO:0106094.
- Phenotype-level rows handled as for unc-84 (Egl/Unc over-annotated; developmental rows non-core;
  1987 TAS regulation of cell migration over-annotated).

### Module implications
- UNC-83 is functionally analogous to the nesprin-2/nesprin-4 motor-recruiting KASH arm and to
  KASH5 (dynein recruitment), but is not homologous beyond the KASH tail. It recruits BICD-1 and
  NUD-2/LIS-1, the same dynein-regulator set (BICD2, NDE1/NDEL1, LIS1) used in mammalian
  nucleokinesis; this supports a C. elegans variant in `modules/nucleokinesis.yaml`.
- Unlike the module's neuronal model (dynein pulling toward the centrosome), hyp7 nuclei move
  toward plus ends with kinesin-1 as the main motor; P cells are dynein-dominant.
- UNC-83's KASH lacks the disulfide cysteine, which supports the module's note that the SUN-KASH disulfide
  is not universal.

### Deep research
- `unc-83-deep-research-falcon.md` read and used for retrieval support (KASH peptide features,
  cargo adaptor, P-cell dynein dominance). The isoform-specific kinesin regulation model
  (2025 preprint) is recorded as a suggested question only.
