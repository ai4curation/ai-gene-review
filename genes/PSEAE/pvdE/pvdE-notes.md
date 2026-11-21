# pvdE (PA2397, Q9I183) notes

No deep-research provider was available; the literature summary below was
compiled manually from PubMed searches ("PvdE pyoverdine" and pyoverdine
biosynthesis reviews) and the cached publications.

## Identity and architecture

- UniProtKB Q9I183 (unreviewed, PE 4), 549 aa, PAO1 locus PA2397.
- Full-length ABC exporter: six predicted TM helices and an ABC transmembrane
  type-1 domain (21-299) followed by an ABC transporter NBD (336-549) with a
  Walker A ATP-binding motif at 373-380 [file:PSEAE/pvdE/pvdE-uniprot.txt].
- NCBIfam TIGR01194 cyc_pep_trnsptr; InterPro IPR005898 "Cyclic peptide
  transporter SyrD/YojI" [file:PSEAE/pvdE/pvdE-uniprot.txt]. This family
  contains exporters of non-ribosomal / modified cyclic peptides (SyrD of
  P. syringae; YojI of E. coli, the microcin J25 exporter).
- PANTHER PTHR24221:SF654.

## Function

- pvdE is required for pyoverdine synthesis; the deduced protein is an ABC
  transporter, "the first example of the involvement of an ABC-type protein in
  siderophore synthesis" [PMID:8918232 "We report the characterisation of a
  fourth Pa gene, pvdE, which we show to be required for Pvd synthesis."].
- Pyoverdine maturation takes place in the periplasm; a pvdE mutant makes no
  PVDI and accumulates no periplasmic precursor (PVDIp), leading to the model
  that PvdE exports the cytoplasmic precursor peptide into the periplasm
  [PMID:19787431 "Mutation of the gene encoding the export ABC transporter PvdE
  prevented PVDI production and accumulation of PVDIp in the periplasm.";
  "a PVDI precursor peptide is synthesized in the cytoplasm and exported to the
  periplasm by PvdE"]. Full text not in cache (abstract only).
- The cytoplasmic precursor is acylated ferribactin (myristic or myristoleic
  chain), deacylated by PvdQ in the periplasm [PMID:22172280 "either a myristic
  or myristoleic chain that must be removed before PVDI is secreted into the
  extracellular medium"]. So the probable PvdE substrate is acylated
  ferribactin.
- Review (Ringel and Bruser 2018, full text): "The acylated ferribactin is most
  likely immediately translocated across the cytoplasmic membrane into the
  periplasm by the ABC transporter PvdE"; the best evidence is the PAO1
  interposon deletion with complementation; and importantly "A transport of
  acylated ferribactin by PvdE has not yet been demonstrated in vitro"
  [PMID:30386787].
- Secretion of mature pyoverdine to the medium is by a different system,
  PvdRT-OpmQ [PMID:23126435 "Secretion of pyoverdine involves a recently
  identified ATP-dependent efflux pump, PvdRT-OpmQ."]. PvdE is therefore an
  inner-membrane precursor exporter, not the siderophore secretion system.
- Phenotypes downstream of pyoverdine loss: a PAO1 delta-pvdE mutant is
  avirulent in a mouse keratitis model [PMID:30252682]; these are indirect
  pyoverdine-dependent effects and are not annotated.

## GO term considerations

- GO:0015440 ABC-type peptide transporter activity (EC 7.4.2.5; definition
  explicitly lists siderophores from Gram-negative bacteria among exported
  peptides) is the most specific MF supported by two lines: the mutant
  phenotype (no precursor peptide in periplasm) and family membership
  (TIGR01194/IPR005898 cyclic peptide exporters). It is an is_a descendant of
  GO:0140359 ABC-type transporter activity, GO:0042626 and GO:1904680.
- No "peptide transmembrane transport" BP exists; GO:0015833 peptide transport
  and GO:0055085 transmembrane transport are as precise as GO allows.
- GO:0180061 native siderophore export across plasma membrane is not
  appropriate: its definition ends in the extracellular region, and PvdE exports
  a precursor into the periplasm.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000656738 (PTHR24221) | GO:0042626 ATPase-coupled transmembrane transporter activity | 1 (sole seed) | 140 (74 taxa) | GO:0042626, IMP, PMID:19787431 (PseudoCAP) | SOUND | For PvdE itself the seed is sound: the pvdE mutant lacks the periplasmic pyoverdine precursor (consistent with loss of export) and the protein has the full TMD+NBD exporter architecture, so the broad transporter term is well justified (a more specific child, GO:0015440, is proposed). The IBD placement, however, is not sound: 126 of the 140 leaves are NBD-only soluble ATPases (EcfA/CbiO, ModF, FtsE, plant NAP/ABCI proteins) and only 6 have a membrane domain (file:PSEAE/pvdE/pvdE-bioinformatics/RESULTS.md). The node's other IBDs (ATP binding, ABC transporter complex) are NBD-level, so GO:0042626 'enables' was placed at a node defined by the NBD and over-propagates onto subunits that at most contribute to transport (and onto FtsE, part of the non-transporting FtsEX system). Recommend GO_Central move the IBD to the clade of TMD-NBD exporters containing PvdE/SyrD/YojI, or use contributes_to. |

Seed verdict: SOUND. Downstream IBD: over-propagated (placement too deep);
recorded as a GO_CENTRAL source defect (CHECK, PROBABLE) on the pvdE IBA row.
The IBA on pvdE itself is supported.

## Review decisions (summary)

- GO:0042626 (IMP, IBA), GO:0140359 (IEA), GO:1904680 (IEA): MODIFY to
  GO:0015440 ABC-type peptide transporter activity.
- GO:0002049 pyoverdine biosynthetic process (IMP PMID:8918232): ACCEPT.
- GO:0005524 ATP binding (IBA, IEA): ACCEPT; GO:0000166 nucleotide binding:
  MODIFY to ATP binding.
- GO:0016887 ATP hydrolysis activity: KEEP_AS_NON_CORE.
- GO:0005886 plasma membrane: ACCEPT; GO:0016020 membrane: MODIFY to plasma
  membrane.
- GO:0043190 ABC transporter complex (IBA, IEA): KEEP_AS_NON_CORE (no
  experimental evidence on oligomeric state; plausible homodimeric half
  transporter).
- GO:0015833 peptide transport, GO:0055085 transmembrane transport: ACCEPT.
