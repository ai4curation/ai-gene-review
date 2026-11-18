# Ta0893 (UniProt Q9HJS1) - Thermoplasma acidophilum DSM 1728

## 2026-11-18 review notes

### Literature search

No deep-research provider was available. PubMed (NCBI E-utilities) queries:
`Thermoplasma[tiab] AND mevalonate[tiab]` (11 hits), `"bisphosphate decarboxylase"[tiab] AND
mevalonate[tiab]` (0 hits; the enzyme name is not in titles/abstracts in that form),
`PTO1356 OR Ta0893 OR SSO2989 OR HVO_1412` (no hit for Ta0893). Europe PMC search returned 34 hits
for `Picrophilus AND (mevalonate OR isobutene)` before it began returning HTTP 503; that list
contained PMID:35690147 and PMID:28004831.

Papers on Ta0893 itself: PMID:28004831 (identification; full text). PMID:35690147 is on the
P. torridus ortholog (PTO0478, Q6L1T9). Upstream enzymes: PMID:24914732, PMID:24755225.

### Reaction

- Mevalonate 3,5-bisphosphate decarboxylase (MBD; EC 4.1.1.110; RHEA:56500):
  (R)-3,5-bisphosphomevalonate + H+ = isopentenyl phosphate + CO2 + phosphate. No ATP.
  [PMID:28004831 "Here we report the identification of MBD from T. acidophilum, which produces IP
  through the ATP independent decarboxylation of mevalonate 3,5-bisphosphate"]
  [PMID:28004831 "Indeed, unlike all other mevalonate pathway decarboxylases, MBD does not require
  ATP."]
- Evidence on Ta0893: MBD activity in T. acidophilum crude lysate; anion exchange then native
  PAGE; MS of active gel fragments found Ta0893 among 7 proteins; recombinant Ta0893 formed
  inclusion bodies but was active when N-terminally truncated by 30 residues or co-expressed with
  GroES/GroEL; activity co-elutes at ~89 kDa in recombinant and native material (homodimer);
  product confirmed as isopentenyl phosphate by coupling to IP kinase.
  [PMID:28004831 "The finding that MBD activity in E. coli is dependent on Ta0893 expression and
  correlates with the same molecular weight as activity in T. acidophilum lysate, strongly
  suggests that Ta0893 is the missing MBD."]
- Kinetics and specificity were measured on the P. torridus ortholog (kcat ~7 s-1, optimum
  70 C and pH ~5), which is specific for the 3,5-bisphosphate.
  [PMID:28004831 "torridus MBD showed clear specificity for mevalonate 3,5-bisphosphate and no
  detectable decarboxylase activity on mevalonate, mevalonate 3-phosphate, mevalonate 5-phosphate
  or mevalonate 5-pyrophosphate"]
- Active site: keeps the Asp/Lys/Arg decarboxylation triad, lacks the ATP-binding residues
  [PMID:28004831 "retention of the invariant Asp/Lys/Arg catalytic triad required for
  decarboxylation, however MBDs are unique in that they are missing both nearly invariant ATP
  binding residues"]. In the P. torridus structure the conserved Asp309 is essential and the
  former ATP site holds a fatty-acid-like ligand; GGPP activates the enzyme (PMID:35690147).

### Evolution and family

- Proposed origin: a dual-function PMD split into a 3-kinase (M3K) and a dedicated decarboxylase
  (MBD) under low internal pH [PMID:28004831 "One lost its decarboxylase function to become a
  mevalonate 3-kinase, and the second lost its kinase function to become a dedicated
  decarboxylase (MBD)."]. Thermoplasmatales MBDs are sister to Lokiarchaeia PMDs (PMID:38674651).
- Dellas et al. 2013 (PMID:24327557) had grouped the Thermoplasmata MDD-annotated proteins with
  the MPD-like haloarchaeal/Chloroflexi enzymes; in fact the Thermoplasmatales homologs are M3K
  (Ta1305) and MBD (Ta0893), neither of which is an MPD.
- InterPro: IPR005935 (Mev_decarb) plus IPR053464 (MVD_Decarboxylase); NCBIfam NF040847
  mev_decarb. PANTHER PTHR10977:SF3 by HMM; not a leaf of the PANTHER 19 tree, and no tree leaf
  shares its UniRef50 cluster (`../../HALVD/mvaD/mvaD-bioinformatics/RESULTS.md`). No IBA reaches
  Ta0893.
- T. acidophilum also has an uncharacterised PTHR10977 member, Ta0461 (Q9HKY2, 384 aa), not
  reviewed here.

### Annotation decisions

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0016831 carboxy-lyase activity | IEA (IPR005935) | ACCEPT | most specific existing GO MF; NTR proposed |
| GO:0008299 isoprenoid biosynthetic process | IEA (IPR005935) | ACCEPT | broad, correct |
| GO:0019287 IPP biosynthesis, mevalonate pathway | IEA (UniPathway) | ACCEPT | core BP |
| NTR mevalonate 3,5-bisphosphate decarboxylase activity | - | proposed_new_terms | EC 4.1.1.110 / RHEA:56500 |

GO:0004163 or GO:0090710 must not be applied to Ta0893: both are ATP-dependent reactions on a
different substrate.
