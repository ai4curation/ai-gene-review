# braG (PA1070, P21630) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P21630 --alias braG`; accession matches the
worklist. Reviewed Swiss-Prot entry (BRAG_PSEAE). No deep-research provider was
used; literature is the bra-operon papers already reviewed for braF and braD
(genes/PSEAE/braF, genes/PSEAE/braD). NCBI and Europe PMC search were unavailable.

### Literature

- BraG is the LivF-type ATPase, last gene of braCDEFG; BraF and BraG carry
  ATP-binding sequences and are membrane-associated
  [PMID:2120183 "both containing amino acid sequences typical of proteins with ATP-binding sites"];
  [PMID:2120183 "These proteins were found among cell membrane proteins"].
- Required for LIV-I [PMID:2120184 "confirming that the braD, braE, braF, and braG genes are required for the LIV-I transport system"].
- Reconstitution [PMID:1400443 "In this reconstituted system, leucine transport was completely dependent on the presence of all five Bra components and on ATP loaded internally to the proteoliposomes."];
  [PMID:1400443 "Alanine and threonine in addition to branched-chain amino acids were transported by the proteoliposomes"].
- Johnson et al. 2008 screen (PMID:18833300, full text): Table 2 lists PA1070
  with D-Alanine C +/- and L-Alanine C +/- (strain PAK, Mini-Tn5). braG is the
  last gene of the operon, so the insertion is not polar on the other bra genes.
  [PMID:18833300 "In this work, mutants for each of these genes were found to be defective in Alanine metabolism"].

### Decisions

- ACCEPT: ATP binding, ATP hydrolysis, plasma membrane (IEA), branched-chain
  amino acid transmembrane transporter activity (IBA contributes_to; IEA).
- TOO_GENERAL: L-amino acid transport (IBA, IEA), amino acid transmembrane
  transport, branched-chain amino acid transport, neutral amino acid transport,
  carboxylic acid transmembrane transport (all entailed by GO:1903801/GO:1904273).
- MODIFY: L-alanine transport (IMP) -> GO:1904273 L-alanine import across plasma membrane.
- UNDECIDED: D-alanine transmembrane transport (IMP), consistent with braF/braD.
- NEW: L-leucine import across plasma membrane (IDA PMID:1400443); ABC
  transporter complex, substrate-binding subunit-containing (IDA PMID:1400443).
- Counts: ACCEPT 5, TOO_GENERAL 6, MODIFY 1, UNDECIDED 1, NEW 2.

## PseudoCAP IBA-seed assessment

PTN000657089 is the LivF ATPase node (73 leaf IBAs, 25 taxa). It also carries an
E. coli LivF-seeded contributes_to GO:0015658 IBD. E. coli LivF (P22731) has IDA
annotations (EcoCyc, PMID:14702302) for L-leucine, L-isoleucine, L-valine and
branched-chain amino acid transport and transporter activity (QuickGO, 2026-11-05).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000657089 | GO:0015807 L-amino acid transport | 2 (P21630, P22731) | 73 (25 taxa) | GO:0015808 L-alanine transport, IMP, PMID:18833300 (PseudoCAP) | SOUND | The partial L-Ala growth defect is indirect on its own, but L-Ala import by BraCDEFG is shown in proteoliposomes (PMID:1400443), braG is required for LIV-I (PMID:2120184), and the insertion is not polar. The generic node term (an ancestor of the seed term) suits a LivF clade whose substrates are set by the partner binding proteins. | E. coli LivF (P22731), IDA L-leucine/isoleucine/valine transport (PMID:14702302) | Yes; E. coli LivF IDA annotations are descendants of the node term |

No `source_defects` were recorded. The D-alanine PseudoCAP IMP row is not a seed of
this node and is left UNDECIDED, as for braF and braD.
