# LITAFD notes

## 2026-10-04 Tier 3 over-annotation audit (claude-code)

### Identity and existence
- UniProt A0A1B0GVX0 (LITAD_HUMAN), Swiss-Prot reviewed, 72 aa, **PE3 (inferred from
  homology)**. No CAUTION lines. Family: CDIP1/LITAF family; PANTHER PTHR23292:SF27
  "LITAF DOMAIN-CONTAINING PROTEIN". The whole chain is the LITAF domain (1-71, PROSITE
  PS51837); UniProt maps Zn ligands C7, C10, C59, C62 (ProRule) and a membrane-binding
  amphipathic helix 22-45 (by similarity to Q99732).
- HGNC (REST, fetched 2026-10-04): HGNC:53927, "LITAF domain containing",
  locus_type **gene with protein product**, 16p13.2, Entrez 101929989,
  ENSG00000283516. MANE Select transcript ENST00000636296.2 / NM_001395433.1; CCDS92105.
- HPA: tissue enriched (testis); Bgee top expression in male germ line stem cells.
- Ensembl REST homology: one-to-one orthologues in mouse (ENSMUSG00000107252) and cow,
  plus orthologues in many mammals and teleosts. Conserved vertebrate gene.
- No proteomics cross-reference (no PeptideAtlas/MassIVE/ProteomicsDB DR lines).
- Literature: PubMed `LITAFD[tiab]` returns only PMID:34696794 (equine vitiligo GWAS,
  horse locus, not functional). No functional study of human LITAFD exists.

### Sequence check vs LITAF (bioinformatics, LITAFD-bioinformatics/RESULTS.md)
- LITAFD aligns to LITAF 90-161 (46.5% identity) and CDIP1 136-207 (36.6%).
- Both CXXC knuckles intact (CPYC at 7, CPVC at 59); all four Zn ligands of LITAF
  (C96/C99/C148/C151) and CDIP1 map onto LITAFD C7/C10/C59/C62.
- LITAF amphipathic helix 111-134 aligns gap-free to LITAFD 22-45; GALTWL motif
  identical; hydropathy of the core window equal to LITAF/CDIP1.
- LITAFD lacks the entire N-terminal proline-rich region of LITAF.

### What the parent family does
- LITAF is a zinc-binding monotopic membrane protein: [PMID:27582497 "Recombinant LITAF
  contains 1 mol/mol zinc, while mutation of predicted zinc-binding residues disrupts
  LITAF membrane association."] and [PMID:27582497 "we conclude that LITAF is a monotopic
  membrane protein whose membrane integration is stabilised by a zinc finger"].
- Topology is conserved: [PMID:27582497 "The related human protein, CDIP1 (cell death
  involved p53 target 1), displays identical membrane topology, suggesting that this mode
  of membrane integration is conserved in LITAF family proteins."]
- Compartments: [PMID:27582497 "Endogenous LITAF localised partially to EEA1-positive
  early endosomes and more extensively to LAMP1-positive late endosomes/lysosomes
  (Figure 2A)."]; CDIP1 [PMID:27582497 "epitope-tagged CDIP1 localised predominantly to
  CD63-positive late endosomes as well as to LAMP1-positive compartments"].

### Annotation decisions (6 GOA rows)
- GO:0008270 zinc ion binding (IBA, PTN000591207; LITAF has IDA from PMID:27582497):
  ACCEPT. Residues retained; this is the domain-level property.
- GO:0016020 membrane (IEA, SubCell): ACCEPT. Membrane-insertion region conserved.
- GO:0098560 / GO:0098574 cytoplasmic side of late endosome / lysosomal membrane (IBA,
  PTN008386299; CDIP1 has IDA from PMID:27582497): KEEP_AS_NON_CORE. Defensible because the
  domain that carries the membrane topology is intact, but untested for LITAFD, which is
  testis-enriched and has no N-terminal region.
- GO:0005634 nucleus (IBA, PTN008386299): MARK_AS_OVER_ANNOTATED. Nuclear localisation of
  LITAF is tied to its proposed transcription-factor role and sits uneasily with a
  monotopic membrane protein; LITAFD has no sequence outside the membrane domain.
- GO:0001817 regulation of cytokine production (IBA, PTN000591246, donor mouse Litaf
  MGI:1929512): MARK_AS_OVER_ANNOTATED. Donor biology is LPS/TNF macrophage context;
  LITAFD is testis-enriched with no functional data.

### Propagation route
All IBA rows come from PANTHER PTHR23292 nodes (PTN000591207 for zinc, PTN008386299
for locations and nucleus, PTN000591246 for cytokine regulation). LITAFD sits inside the
family and keeps the domain, so the domain-intrinsic terms (zinc, membrane) transfer
soundly. The problem terms (nucleus, cytokine production) are LITAF-specific claims that
were placed at deep nodes.
