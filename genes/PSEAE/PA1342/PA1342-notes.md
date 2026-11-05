# PA1342 (AatJ, Q9I402) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I402 --alias PA1342` (no gene symbol in
UniProt; locus tag used as folder name, as for PA1340/PA1341). Accession Q9I402
matches the worklist (rank 326). Reviewed Swiss-Prot entry GASBP_PSEAE
(L-glutamate/L-aspartate-binding protein), 302 aa, signal peptide 1-23.
Reviewed with PA5082 (Q9HUA1), the other PseudoCAP seed of the same node, and
checked for consistency with the existing PA1340 and PA1341 reviews (permeases
of the same operon). No deep-research provider was used.

### Identity

- Periplasmic solute-binding protein, SBP_bac_3 family (Pfam PF00497); PANTHER
  PTHR30085:SF2 "GLUTAMATE_ASPARTATE IMPORT SOLUTE-BINDING PROTEIN". Binding
  protein of the PA1342-PA1339 AatJQMP ABC importer (orthologue of P. putida
  AatJ, E. coli GltI).

### Literature

- Fernandez et al. 2019 (PMID:31627455; full text cached): purified PA1342 by
  thermal shift and ITC. [PMID:31627455 "ITC studies revealed l-Glu and l-Asp
  binding with affinities of 1.4 and 20 µM, respectively. No binding was
  observed for other amino acids, including l-Gln and l-Asn, indicating that
  PA1342 is specific for l-Glu and l-Asp (Table 1)."] D-Glu is not among the
  ligands reported.
- He et al. 2014 (PMID:25082951; abstract only), the PseudoCAP seed paper:
  [PMID:25082951 "expression of the previously characterized AatJMQP
  transporter for acidic l-amino acid uptake was found inducible by D-Glu and
  essential for D-Glu utilization"]. The abstract does not say which aat gene
  was mutated. As for PA1340, I defer to the curator who read the full text.
- Singh and Rohm 2008 (PMID:18310026; abstract only), P. putida orthologue:
  [PMID:18310026 "The purified solute-binding protein AatJ exhibited high
  affinity towards Glu and Asp (K(d)=0.4 and 1.3 muM, respectively), while Gln
  and Asn as well as dicarboxylates (succinate and fumarate) were bound with
  much lower affinity."]
- Johnson et al. 2008 (PMID:18833300; full text cached): PA1339-PA1341 mutants
  defective for L-Glu use; PA1342 itself was not in that mutant set.

Assessment: AatJ is a Glu/Asp-specific binding protein (direct ITC), the
substrate-capture component of an L-Glu/L-Asp importer. Its D-Glu role is a
system-level genetic finding whose substrate basis is unclear (no D-Glu binding
reported), so D-amino acid transport is kept as non-core, matching PA1340.

### Clade check (cached PAINT IBD/leaf GAF; QuickGO 2026-11-05)

- PTN004739212 (GO:0006865 amino acid transport): 3 seeds, Q9I402 (this gene,
  PseudoCAP IMP GO:0042940 PMID:25082951), Q9HUA1 (PA5082/DguC, same paper)
  and E. coli GltI P37902. GltI has EcoCyc IDA for L-glutamate transmembrane
  transport (GO:0015813, PMID:1091635, PMID:236016) and IPI for glutamate and
  aspartate binding. 31 leaf IBAs in 14 taxa: GltI orthologues, GlnH
  glutamine-binding proteins (B. subtilis, Synechocystis, M. tuberculosis,
  Yersinia), cystine-binding and other SBP_bac_3 amino acid binding proteins
  (yhdW, sll/slr proteins, Bradyrhizobium bll/blr), and a few eukaryotic or
  actinobacterial SBP_bac_3 proteins (Thalassiosira, Ixodes, SCO2664 "sugar
  binding protein"). Amino acid transport is a suitably broad term for an
  SBP_bac_3 amino acid binding protein clade; SCO2664 is the only leaf whose
  name suggests another ligand class, too little to fault the node.
- The IBD stands on E. coli GltI alone, without either PAO1 seed.
- Node-level judgement for this node is recorded here (the gene with the most
  direct evidence, the ITC ligand profile); `genes/PSEAE/PA5082/PA5082-notes.md`
  points here.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004739212 | GO:0006865 amino acid transport | 3 | 31 (14 taxa) | GO:0042940 D-amino acid transport, IMP, PMID:25082951 (PseudoCAP) | SOUND | The abstract states that the AatJMQP transporter is essential for D-Glu utilisation; that supports the general node term for its binding protein, and AatJ independently binds L-Glu/L-Asp (ITC, PMID:31627455). Which aat gene was mutated is not in the abstract, so the D-Glu row is deferred to the curator and kept non-core. | PA5082 Q9HUA1 (same paper); E. coli GltI P37902 (IDA L-glutamate transport, IPI Glu/Asp binding) | Yes. E. coli GltI alone grounds amino acid transport for this SBP_bac_3 amino acid binding protein clade. No GO_CENTRAL defect. |

Defects filed: none.

## Decisions summary

- ACCEPT: outer membrane-bounded periplasmic space (IBA).
- MODIFY: amino acid transport (IBA) -> L-glutamate import across plasma
  membrane, L-aspartate import across plasma membrane.
- TOO_GENERAL: periplasmic space (IEA).
- KEEP_AS_NON_CORE: D-amino acid transport (IMP).
- NEW: glutamate binding and aspartate binding (IDA, PMID:31627455).
