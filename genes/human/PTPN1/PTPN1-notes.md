# PTPN1 review notes

Deep-research providers were unavailable in this checkout: the configured client
reported only `claude_code` as available, while the requested `falcon` and
`perplexity` providers were absent. This file records the manual synthesis used
for the PTPN1 review.

## Core function

- PTPN1/PTP1B is an ER-tail-anchored non-receptor protein tyrosine phosphatase.
  UniProt describes the protein as mediating dephosphorylation of EIF2AK3/PERK,
  regulating EFNA5-EPHA3 and MET signaling, and localizing to the cytoplasmic
  side of the ER membrane.
- Frangioni et al. 1992 established the topology of PTP1B: it is tightly
  associated with microsomal membranes and its phosphatase domain faces the
  cytoplasm [PMID:1739967, "phosphatase domain oriented towards the
  cytoplasm"]. This supports `GO:0098554 cytoplasmic side of endoplasmic
  reticulum membrane` and the ER/ER-membrane rows.
- Salmeen et al. 2000 and Wu et al. 2011 support PTP1B as a negative regulator
  of insulin receptor signaling: PTP1B dephosphorylates the insulin receptor
  kinase activation segment [PMID:11163213, "dephosphorylating the
  phosphotyrosine residues of the insulin receptor kinase"], and Nck helps
  recruit the mammalian Nck/PTP1B complex to the insulin receptor for signal
  attenuation [PMID:21707536, "attenuates insulin signalling by recruiting
  PTP61F/PTP1B to its substrate, the IR"].
- PTP1B contacts and dephosphorylates activated receptor tyrosine kinases as
  they pass ER-endosome or peripheral ER contacts. Wimmer-Kleikamp et al. 2011
  show that PTP1B governs EphA3 phosphorylation, direct EphA3/PTP1B contacts
  occur before ligand-stimulated receptor internalization and on endosomes, and
  PTP1B slows ephrin-induced EphA3 trafficking.
- Sangwan et al. 2008 and Reactome R-HSA-6807027 support dephosphorylation of
  MET by PTPN1/PTP1B and PTPN2/TCPTP. Reactome R-HSA-8849435 supports
  PTPN1-dependent dephosphorylation and inactivation of PTK6, and Reactome
  R-HSA-997311 records PTP1B interaction with and dephosphorylation of TYK2 in
  interferon signaling.
- Fuentes et al. 2012 show that PTP1B activity is needed for RTK trafficking
  along the endocytic pathway: loss of PTP1B delayed Met and EGFR degradation,
  blocked efficient traffic to early endosomes and perinuclear compartments, and
  identified NSF as a PTP1B substrate needed for receptor trafficking.
- Krishnan et al. 2011 show that ER-stress-induced H2S sulfhydrates the PTP1B
  catalytic cysteine and inhibits its ability to dephosphorylate PERK; the same
  paper establishes a direct enzyme-substrate interaction between PTP1B and
  pTyr619-PERK.
- Gu et al. 2004 show that mouse Ptpn1 is required for full IRE1-arm signaling
  after ER stress, including XBP1 splicing, JNK activation and EDEM induction
  [PMID:15465829, "The absence of PTP-1B caused impaired ER stress-induced
  IRE1 signaling"].

## Propagation and non-core rows

- PANTHER PTHR46047 has only three reviewed subfamilies: PTPN2/TC-PTP in SF1,
  PTPN1/PTP1B in SF2, and Drosophila Ptp61F in SF3. The PAINT root IBDs for
  non-membrane-spanning protein tyrosine phosphatase activity, protein kinase
  binding, cytoplasm and ERK regulation are biologically sound for both human
  paralogs. The PTPN1 branch separately has ER, early-endosome and negative
  PERK UPR IBDs.
- The PAINT IRD at PTN002917511 cleanly prevents the root nucleus IBD from
  propagating into the PTPN1-specific clade; PTPN1 is ER anchored and lacks the
  TC45-like nuclear isoform that characterizes PTPN2. The same PTN002917511 IRD
  for the broad JAK-STAT term is harder to read because human PTPN1 has
  receptor-specific TYK2/JAK2 curation in Reactome; this review leaves it as an
  unresolved PAINT loss rather than proposing a PAINT edit.
- The Ensembl/orthology tail on PTPN1 contains many rat or mouse phenotype and
  stimulus terms, including blood-pressure, heart-rate, cardiac-apoptosis,
  neuron-projection, VEGF, proteolysis, nutrient, insulin-stimulus, FGF,
  hypoxia, nitric-oxide, PI3K/AKT, angiotensin, smooth-muscle migration,
  nerve-growth-factor, postsynaptic and endothelial-apoptosis rows. These are
  downstream outcomes of mouse or rat physiology, not direct human PTPN1
  substrate dephosphorylation events.
- The mitochondrial matrix, mitochondrial crista and endosome lumen projections
  conflict with the established ER-membrane topology of full-length PTPN1. PTP1B
  reaches receptors on the cytoplasmic face of ER, plasma and endosomal
  membranes; it is not a soluble matrix, crista or luminal endosomal protein.
- High-throughput `RNA binding` and generic `protein-containing complex` rows
  record screen hits or proximity data but do not identify an RNA-binding or
  complex-membership function for PTPN1; the `cadherin binding` row is supported
  by direct N-cadherin binding evidence from Rhee et al. 2001 [PMID:11106648,
  "PTP1B interacts directly with the cytoplasmic domain of N-cadherin"].
- `GO:0005515 protein binding` is an uninformative umbrella term for the many
  PTPN1 substrate-trap and interactome rows. Those interactions are useful
  evidence for specific receptor, kinase and ephrin-receptor rows, but the bare
  protein-binding term itself should be removed by policy.
- PMID:18074158 argues against zinc as a cofactor: it states that PTP1B is not
  classified as a zinc enzyme and is instead strongly inhibited by Zn(II), so the
  zinc-binding row overstates inhibitory metal binding as a molecular function.
