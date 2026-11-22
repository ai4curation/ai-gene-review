# mgtE (PA0913, Q9I544) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 20)

No deep-research provider was available; literature collected by PubMed search
and the cached abstracts. The PseudoCAP-cited paper (PMID:24722909, Coffey et
al. 2014) is abstract-only here: there is no PMC copy and the publisher page
and the thesis repository could not be fetched.

### Identity and family

- UniProt Q9I544 (unreviewed), 482 aa, "Magnesium transporter MgtE" by
  RuleBase; SLC41A/MgtE family; N-terminal MgtE_N domain, two CBS domains,
  C-terminal MgtE transmembrane domain (Pfam PF01769, NCBIfam TIGR00400 mgtE);
  three predicted TM segments (393-415, 421-446, 458-481)
  [file:PSEAE/mgtE/mgtE-uniprot.txt].
- PANTHER PTHR43773:SF1. The PAINT node PTN000227060 is the family root (25
  leaves, 21 organisms) [file:PSEAE/mgtE/mgtE-bioinformatics/RESULTS.md].

### Function in P. aeruginosa

- Inner-membrane Mg2+ transporter and virulence modulator
  [PMID:24722909 "We previously found that the inner-membrane protein MgtE can
  function both as a magnesium transporter and a virulence modulator"].
- Transport and cytotoxicity regulation were both demonstrated, and
  Mg2+-binding sites in the connecting helix were required for coupling them
  [PMID:24722909 "We demonstrated both magnesium transport and
  cytotoxicity-regulating functions, and showed that magnesium-binding sites in
  the connecting helix region of MgtE are vital in coupling these two
  functions."]. The sites were identified from a homology model built on the
  T. thermophilus crystal structure [PMID:24722909 "Our in silico analysis
  demonstrated the structural similarity of P. aeruginosa MgtE to that of the
  crystal structure of MgtE in Thermus thermophilus."]. As far as the abstract
  shows, no direct Mg2+-binding assay was done.
- mgtE mutation raises T3SS transcription and cytotoxicity; transport-defective
  variants still complement the cytotoxicity phenotype [PMID:20028803
  "Furthermore, mgtE variants that were defective for magnesium transport could
  still complement the cytotoxicity effect."].
- Mechanism of T3SS inhibition: mgtE expression acts through GacAS to raise
  rsmY/rsmZ and inhibit exsA translation [PMID:28847924 "We now demonstrate
  that mgtE expression acts through the GacAS two-component system to activate
  rsmY and rsmZ transcription."]. This is regulatory output, probably indirect;
  no GO process for it is proposed here.
- mgtE is not essential and is induced by low Mg2+ [PMID:24722909
  "Furthermore, limiting magnesium environments stimulated mgtE transcriptional
  responses."].

### Family reference: T. thermophilus MgtE (Q5SMG8)

- Homodimer; Mg2+ in the pore at Asp432 and at cytosolic sensor sites
  [PMID:17700703 "A solvent-accessible pore nearly traverses the transmembrane
  domains, with one potential Mg2+ bound to the conserved Asp 432 within the
  pore."].
- Mg2+-selective channel gated by cytosolic Mg2+ [PMID:19798051 "Here, we
  showed that MgtE is a highly Mg(2+)-selective channel gated by Mg(2+)"].
- Mg2+-binding residues mapped onto PA0913: 8 of 15 positions identical
  (including pore Asp -> Asp466) and 2 conservative
  [file:PSEAE/mgtE/mgtE-bioinformatics/RESULTS.md].

### Annotation decisions (summary)

- GO:0015095 magnesium ion transmembrane transporter activity (IEA): ACCEPT, core.
- GO:1903830 magnesium ion transmembrane transport (IEA): ACCEPT, core.
- GO:0015693 magnesium ion transport (IBA, IEA, IMP): MODIFY to GO:1903830.
- GO:0000287 magnesium ion binding (IBA, IMP): KEEP_AS_NON_CORE; true by
  similarity to the Tth structure, but the IMP row is not binding evidence.
- GO:0008324, GO:0006812, GO:0098655: MODIFY to the Mg2+-specific terms.
- GO:0016020 membrane: MODIFY to GO:0005886; GO:0005886 (IEA): ACCEPT.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000227060 | GO:0015693 magnesium ion transport | 1 (sole) | 25 | GO:0015693, IMP, PMID:24722909 | SOUND | The abstract reports Mg2+ transport by P. aeruginosa MgtE, and transport-defective variants are described in PMID:20028803. A transporter's own process, not an indirect phenotype. Node placement issue: 6 of 22 resolved leaves (SCO5154, Rv1232c, CBO0203, TM_0892, A7T8Y4, VC_0300) lack the MgtE transmembrane domain (PF01769) yet inherit the IBA; NOT annotations are needed there. |
| PTN000227060 | GO:0000287 magnesium ion binding | 1 (sole) | 25 | GO:0000287, IMP, PMID:24722909 | INDIRECT-PHENOTYPE | A mutant phenotype cannot show ion binding. Coffey et al. mutated Mg2+ sites predicted from the Tth homology model and saw lost coupling of functions. The binding claim is true by similarity (Tth Q5SMG8 crystal structures; ligands conserved in PA0913), but this seed is not experimental binding evidence. Q5SMG8 is in PTHR43773:SF1 but not a tree leaf, so it cannot re-seed the node; the IBD rests only on this row. |

Term breadth: magnesium ion transport (and Mg2+ binding) at the eubacterial
family root suits the full-length MgtE transporters, which dominate the clade.
The six TM-less leaves are scattered losses (the Actinomycetales clade
PTN005181931, CBO0203, TM_0892, A7T8Y4, VC_0300) and need NOT rows rather
than a smaller node.
