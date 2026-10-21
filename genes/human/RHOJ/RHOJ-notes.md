# RHOJ (G3V4H1) review notes

## 2026-10-20 full re-review (independent of ProtNLM output)

This re-review replaces earlier notes that mixed annotation review with a review of
ProtNLM output. Those prediction assessments are not used as evidence here.

### Identity of the benchmark accession

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

### Gene-level biology (canonical Q9H4E5)

- Fast-exchanging, hydrolytically active GTPase [PMID:10967094 "In vitro, TCL shows rapid
  GDP/GTP exchange and displays higher GTP dissociation and hydolysis rates than TC10."].
- Localization depends on activation state (plasma membrane versus EEA1/Rab5 endosomes)
  [PMID:27660391].
- Endothelial-enriched and an ERG target. Required for lumen and tube formation
  [PMID:21628409; PMID:21148427 "RhoJ is endothelial-expressed in vivo, activated by vascular
  endothelial growth factor, localizes to focal adhesions..."].
- GTP-bound RHOJ binds the PlexinD1 cytoplasmic domain and integrates Sema3E and VEGF
  cues [PMID:32347571].

### Evolutionary grounding

- PAINT node PTN000632671 (Rho-family root, PTHR24072) carries IBD GTPase activity,
  GTP binding and plasma membrane. Q9H4E5 is among the seeds. The node supports these
  functions for the RHOJ lineage. The question for G3V4H1 is not lineage loss but product
  integrity.
- Closest characterised relative by phylogeny: mouse Rhoj (Q9ER71), the SF17 ortholog,
  characterised in endothelial knockout and retinal angiogenesis studies
  [PMID:32347571]. The repo has no mouse Rhoj review, and no review of human canonical
  Q9H4E5 as a separate accession (this folder is G3V4H1).

### Decisions

All three IEA MF rows (GTPase activity, G protein activity, GTP binding) are marked
MARK_AS_OVER_ANNOTATED. The terms are correct for RHOJ but not supported for an
NMD-transcript product that lacks half the G domain. They are not removed, because the
claims are true of the gene. core_functions is left empty because no function is
supported for this product.

### Family / modules

- interpro/panther/PTHR24072/PTHR24072-review.yaml lists G3V4H1 under "Benchmark members
  without resolved subfamily placement". This matches the PANTHER lookup (G3V4H1 is
  unmapped at subfamily level, while canonical RHOJ is SF17). The family review does not
  mention the NMD biotype.
- No module in modules/ includes RHOJ. RHOJ appears only in falcon deep-research artifacts
  for the FGFR, Fc-gamma receptor, death-receptor and Nodal modules, as incidental text.

### Deep research

The falcon report (RHOJ-deep-research-falcon.md) is gene-level and accurate on endothelial
biology. It correctly flags that the "Rab family" label is wrong. It does not analyse the
G3V4H1 product.
