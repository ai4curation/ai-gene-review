# PA5082 (DguC, Q9HUA1) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUA1 --alias PA5082` (no gene symbol in
UniProt; locus tag used as folder name). Accession Q9HUA1 matches the worklist
(rank 325). Unreviewed TrEMBL entry, 299 aa, SignalP signal peptide 1-22.
Reviewed with PA1342 (AatJ, Q9I402), the other PseudoCAP seed of the same
node, and checked against genes/PSEAE/PA5085 (DguR, the activator of the
dguABC operon; same paper). No deep-research provider was used.

### Identity

- Periplasmic solute-binding protein, SBP_bac_3 family (Pfam PF00497);
  PANTHER PTHR30085:SF2 "GLUTAMATE_ASPARTATE IMPORT SOLUTE-BINDING PROTEIN"
  (same subfamily as AatJ). Encoded as dguC, the last gene of the
  D-Glu-inducible dguABC operon (PA5084 dguA, PA5083 dguB, PA5082 dguC).

### Literature

- He et al. 2014 (PMID:25082951; abstract only), the PseudoCAP seed paper:
  [PMID:25082951 "Whilst a lesion in dguC encoding a periplasmic solute binding
  protein only affected growth on D-Glu slightly, expression of the previously
  characterized AatJMQP transporter for acidic l-amino acid uptake was found
  inducible by D-Glu and essential for D-Glu utilization."]
  [PMID:25082951 "the divergent dguR-dguABC (D-Glu utilization) gene cluster was
  shown to participate in D-Glu and D-Gln catabolism and regulation"]
- No binding or uptake data for DguC were found; its ligand is inferred from the
  operon (D-Glu-specific induction, D-amino acid dehydrogenase DguA) and the
  mild growth phenotype.

Assessment: a dguC mutant with a slight growth defect on D-Glu is a weak,
indirect readout, but the abstract positively reports it for this gene, and a
periplasmic binding protein in a D-Glu-induced catabolic operon has no
plausible role in D-Glu utilisation other than substrate capture for transport.
The row is accepted as the gene's (weakly supported) core process. The AatJMQP
system is the main D-Glu route, so DguC is at most a secondary binding protein.

### Clade check

PTN004739212 (GO:0006865 amino acid transport; seeds Q9HUA1, Q9I402, E. coli
GltI P37902). The full clade analysis is in `genes/PSEAE/PA1342/PA1342-notes.md`
(recorded once there): an SBP_bac_3 amino acid binding protein clade grounded
by E. coli GltI (IDA L-glutamate transmembrane transport), so the IBD does not
depend on this seed.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004739212 | GO:0006865 amino acid transport | 3 | 31 (14 taxa) | GO:0042940 D-amino acid transport, IMP, PMID:25082951 (PseudoCAP) | SOUND | The abstract reports a dguC lesion that slightly impairs growth on D-Glu; weak, but for a periplasmic binding protein in the D-Glu-induced dgu operon it supports D-amino acid transport, and it amply supports the general node term. | PA1342 Q9I402 (same paper); E. coli GltI P37902 (IDA) | Yes, on E. coli GltI alone (see PA1342 notes). No GO_CENTRAL defect. |

Defects filed: none.

## Decisions summary

- ACCEPT: D-amino acid transport (IMP); outer membrane-bounded periplasmic
  space (IBA).
- TOO_GENERAL: amino acid transport (IBA; entailed by D-amino acid transport);
  periplasmic space (IEA).
