# PRKCQ (Q04759, human) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PRKCQ was selected as the closest experimentally characterised relative of a
XENTR benchmark protein (A0A8J1IYX6) that sits at the base of the PKC/PKN clade in
PANTHER PTHR24351 with no subfamily assigned. That relationship is paralogous
(family level), so this review documents PRKCQ in its own right and is explicit about
which activities are experimentally established for the human protein. No ProtNLM2
output was opened or used.

### Deep research

`just deep-research-falcon human PRKCQ --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" and the perplexity fallback returned HTTP 401
(insufficient quota). No deep-research file exists. The review is built from the cached
publications (the 18 GOA-cited PMIDs plus five added papers: PMID:16356855,
PMID:36040231, PMID:10746729, PMID:16252004, PMID:14988727), the UniProt record and
the cached Reactome entries.

### Evolutionary placement

- PANTHER: PTHR24351 (RIBOSOMAL PROTEIN S6 KINASE), the large AGC family that also
  holds AKT, SGK, PKA, PKN and the PKC isoforms. InterPro places PRKCQ in the
  PKC-delta-like novel PKC group (IPR014376 Prot_kin_PKC_delta) and the PKC-theta
  family (IPR027264, IPR034668).
- The two IBA rows (GO:0004674, GO:0035556) both come from PTN000683254, a deep node
  seeded by plant, yeast, fly, worm and mammalian AGC kinases
  (`interpro/panther/PTHR24351/PTHR24351-paint.tsv`). The PAINT curators did not place
  diacylglycerol-dependent kinase activity at that node; DAG dependence is a property
  of the C1-domain-containing PKC subgroup, not of the family.
- The closest paralog is PRKCD (PKC-delta); PMID:21964608 reports 62% identity
  between them and shows that PKC-delta cannot substitute for PKC-theta's V3-domain
  functions (CD28/Lck binding, recruitment to the immunological synapse).
  Anything specific to the V3 PxxP motif is PKC-theta-specific and must not be
  transferred to other novel PKCs or to the XENTR target.

### Experimentally established for the human protein (or human cells)

- Kinase activity and its regulation: purified PKC-theta is inhibited by the PRKCH
  uORF2 peptide uPEP2 (PMID:34593629, in vitro kinase assays). Englerin A activates
  purified PKC-theta in vitro, competing with phorbol-ester binding (PMID:23352416).
  Thr-219 autophosphorylation is needed for membrane recruitment but not catalytic
  activity (PMID:16252004, Jurkat and primary T cells).
- Direct substrates shown in vitro: CARD11/CARMA1 linker serines (PMID:16356855,
  PMID:16356856), CCDC88A/GIV Ser1689 (PMID:23509302), HSF1 (PMID:23352416), LRRK1
  CORB-domain residues (PMID:36040231), IRS1 Ser1101 (PMID:15364919), SPAK/STK39 Ser311
  (PMID:14988727), PRKCZ (PMID:17588663) and BAD (PMID:11342610).
- TCR signalling: CARMA1 phosphorylation is needed for TCR-induced NF-kB activation
  (PMID:16356856). PKC-zeta/iota act downstream of PKC-theta in Jurkat cells
  (PMID:17588663). SPAK carries the AP-1 branch (PMID:14988727).
- Localisation: recruited to the immunological synapse/cSMAC through the V3 PxxP motif
  binding the Lck SH3 domain, which bridges it to CD28 (PMID:21964608; mostly mouse
  primary T cells and Jurkat). In resting T cells it is cytoplasmic (UniProt).
- Survival: protects T cells from Fas-induced apoptosis via BAD phosphorylation
  (PMID:11342610) and Bcl-xL induction (PMID:16709830; knockdown in Jurkat and
  Prkcq-/- mouse cells).

### Established mainly in mouse

- Mouse knockout: TCR-induced NF-kB activation is absent from mature Prkcq-/- T cells,
  while thymocyte development is normal and TNF/IL-1 NF-kB signalling is intact
  (PMID:10746729).
- Th2/Th17 responses, IL-4/IL-17 production and platelet roles come from mouse
  knockout work. Here they arrive only as ISS/IEA from mouse Q02111, a 1:1 ortholog
  with a sound transfer basis. They are downstream outcomes of the kinase's role in
  TCR signalling, so they are kept as non-core.

### Decisions worth flagging

- Bare protein-binding rows: removed per policy, except the Lck row
  (PMID:21964608), which was modified to SH3 domain binding (GO:0017124). The paper
  maps the interaction to the PKC-theta V3 PxxP motif binding the Lck SH3 domain.
- Kinase activity: the general rows (protein kinase / Ser-Thr kinase / DAG-dependent
  kinase) were modified to GO:0004699 (DAG-dependent, calcium-independent), which is
  experimentally supported. Protein serine kinase activity (GO:0106310) is not an
  ancestor of GO:0004699 (checked with OLS hierarchicalAncestors), so its EXP rows are
  accepted.
- Cell chemotaxis IMP (PMID:24008408): the abstract is about PKC-delta, but the full
  text (PMC3797592, checked by web fetch) states "HCECs transfected with siRNA
  directed against PKC isoforms delta and theta showed a complete inhibition of
  migration". Kept as non-core (corneal epithelium).
- Telomere maintenance IMP (PMID:21531765): from a kinome RNAi screen whose abstract
  does not name PRKCQ. Marked UNDECIDED.
- Axon guidance (Reactome TAS): no PKC-theta-specific evidence in neurons was found
  in the cached Reactome text. Marked as over-annotation.
- NEW: T cell receptor signaling pathway (GO:0050852). PKC-theta does the work of a
  step in the pathway (it phosphorylates the CARD11 linker, which triggers CBM
  assembly), so this is participation, not just requirement.
