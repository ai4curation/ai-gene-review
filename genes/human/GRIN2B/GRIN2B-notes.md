# GRIN2B (GluN2B / NR2B, Q13224) — review notes

## Provider / workflow situation
- Falcon and Perplexity deep-research providers are not configured in this environment. Deep research
  was generated with OpenScientist:
  `genes/human/GRIN2B/GRIN2B-deep-research-openscientist.md`
  (`just deep-research-openscientist human GRIN2B`). Treated as a lead; claims checked against the
  cached publications and UniProt before use.
- `just paint-losses human GRIN2B` reports no IRD/IKR loss on this gene's lineage.
- Reviewed as the GluN2B partner of the merged GRIN1 review; kept consistent with GRIN1 and GRIN2A.

## Core biology
- GluN2B is one of four GluN2 subunits of NMDA receptors; GluN2 binds **glutamate**, GluN1 binds the
  co-agonist glycine/D-serine [PMID:12805203]. GluN2B-containing receptors have slow deactivation
  kinetics; GluN2B predominates in the immature forebrain and shifts to a smaller, largely
  extrasynaptic pool in the adult. UniProt records L-glutamate binding residues (514/519/690–691/732)
  and an N-terminal-domain Zn2+ site (127/284).
- The exceptionally long GluN2B C-terminal tail is a scaffolding hub: CaMKII docks on it [PMID:28130356];
  PSD-95/DLG-family PDZ scaffolds anchor the receptor; DAPK1 phosphorylates Ser1303 in excitotoxicity.
- Disease: de novo/inherited GRIN2B variants cause autosomal-dominant ID with/without seizures and
  developmental-and-epileptic encephalopathy; West-syndrome GoF variants [PMID:24272827 "Mutations
  p.Asn615Ile and p.Val618Gly cause a significantly reduced Mg(2+) block and higher Ca(2+) permeability,
  leading to a dramatically increased Ca(2+) influx"].

## Key review decisions
- Channel MF cluster (GO:0004972 etc.): ACCEPT. GO:0016595 glutamate binding (ISS) ACCEPT as core GluN2
  function. Generic MF terms MODIFY → GO:0004972; calcium channel → GO:0022849.
- **GO:0016594 glycine binding (IDA PMID:17047094) → REMOVE + source_defect (WRONG_TERM).** The
  glycine site is formed by GluN1/GluN3; GluN2 forms the glutamate site. PMID:17047094 assays only the
  NR1 and NR3 ligand-binding cores (NR1/NR3 receptors) and does not characterise a GluN2B glycine site,
  so the IDA glycine-binding annotation on Q13224 is a subunit/ligand mis-attribution. GluN2B's correct
  ligand-binding function (glutamate binding) is retained from the ISS row. This is a textbook,
  project-consensus ligand-selectivity fact (not hidden full-text), so REMOVE rather than UNDECIDED.
- **GO:0099507 presynaptic ligand-gated channel activity (IDA/IMP/NAS PMID:19666514) → KEEP_AS_NON_CORE +
  source_defect (WRONG_GENE_PRODUCT).** PMID:19666514 is explicitly about presynaptic **NR2A** receptors
  at cerebellar parallel fibres; the presynaptic high-pass-filter function it demonstrates is for GluN2A.
  Presynaptic NMDA receptors are a real minor pool, so kept non-core, but the citation is a likely
  subunit mis-attribution and is flagged.
- GO:0005515 protein binding (IPI, many incl. CaMKII, PSD-95/DLG) → REMOVE per policy; interactions real
  but uninformative.
- Ciliary rows from HPA immunofluorescence (GO:0005929 cilium, GO:0035869 transition zone, GO:0097542
  tip; all IDA GO_REF:0000052) → MARK_AS_OVER_ANNOTATED: ciliary localisation is unsupported by the
  established synaptic biology and most likely antibody cross-reactivity.
- ER membrane (Reactome assembly) → MARK_AS_OVER_ANNOTATED (transit, not residence).
- Endosome/lysosome/cytoplasm/cytoskeleton rows → KEEP_AS_NON_CORE (trafficking, C-tail, KIF17 transport).
- negative regulation of dendritic spine maintenance (GO:1902951, ISS; mouse IGI PMID:22820466 Aβ/Fyn
  context) → KEEP_AS_NON_CORE (context-dependent downstream GluN2B-tail signalling).
- Amyloid-beta binding / ethanol / brain development / learning & memory handled as for GRIN2A and GRIN1.

## Action totals
See the PR body. 150 annotation rows.

## 2026-11-15: full text of PMID:19666514

The requester supplied the full text of PMID:19666514 (Bidoret et al. 2009), which the cache holds as abstract
only. It is the paper behind the three SynGO rows for GO:0099507 (ligand-gated channel activity involved in
regulation of presynaptic membrane potential; IDA, IMP, NAS). The paper assigns the presynaptic NMDA receptor
role at rat cerebellar parallel fibres to NR2A: "NR2A- but not NR2B-containing NMDARs are required for LTD
induction" (the NR2B-selective antagonist Ro25-6981 did not prevent LTD; nanomolar zinc did). NR2B labelled
about 10% of parallel fibre boutons, against 23% for NR2A and 49% for NR1. The three rows changed from UNDECIDED
to REMOVE, and the SynGO query became a confirmed wrong-gene-product source defect (the evidence fits rat Grin2a).

## 2026-11-15: review round on PR #6368

- GO:0099505 (inter-ontology IEA from GO:0099507) is now REMOVE: it inherits the wrong-subunit defect of the three SynGO rows it is generated from.
- The SynGO source defects now request REPOINT to GRIN2A (UniProtKB:Q12879) rather than CHECK, since the full text was read.
- PDZ-scaffold IPI rows from PMID:11937501 are MODIFY to GO:0030165 PDZ domain binding; CaMKII alpha rows (PMID:19453375, PMID:28130356) are MODIFY to GO:0019901 protein kinase binding. A third core function records the C-tail scaffolding role.
- Location rows now quote the UniProt SUBCELLULAR LOCATION lines rather than the complex-membership sentence.
