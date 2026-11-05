# pvdR (PA2389, Q9I191) review notes

## Literature (no deep-research provider; own reading, 2026-11-05)

- Imperi et al. 2009 (full text read, PMC2787144) identify PA2389-PA2390-opmQ as a
  tripartite ABC exporter and rename the genes pvdR/pvdT
  [PMID:19906986 "we identified a tripartite ATP-binding cassette efflux transporter, here named PvdRT-OpmQ, which translocates PVD from the periplasmic space to the extracellular milieu"].
  All evidence is mutant phenotype with complementation
  [PMID:19906986 "Conversely, PA2389 , PA2390 , and opmQ mutants accumulated five- to sixfold higher amounts of PVD than wild-type PAO1, suggesting an involvement of these genes in PVD export."].
  No antibiotic resistance contribution
  [PMID:19906986 "the PvdRT-OpmQ efflux system does not provide any contribution to P. aeruginosa resistance to antibiotics belonging to the classes of tetracyclines, aminoglycosides, β-lactams and macrolides, and chloramphenicol"].
  Lower PVD yield of mutants attributed to reduced synthesis secondary to the export defect
  [PMID:19906986 "our preliminary results suggest that the lower PVD levels in their culture supernatants are a result of reduced PVD synthesis rather than of impaired secretion of de novo synthesized PVD"].
- Hannauer et al. 2010 (abstract): pump also secretes newly made PVD
  [PMID:21035449 "due to their inability to efficiently secrete into the media newly synthesized PVD"].
- Hannauer et al. 2012 (abstract): exports PVD-metal complexes
  [PMID:22187978 "the PvdRT-OpmQ efflux pump exports unwanted metals complexed with PVD from the bacterium"].
- Yeterian et al. 2010 (abstract): recycling
  [PMID:23766114 "prevented recycling of PVDI from the periplasm into the extracellular medium"].

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001253051 | GO:1990281 efflux pump complex | 2 | 87 (21 taxa) | GO:1990281, IDA PMID:19906986/21035449/22187978; IMP PMID:19906986/22187978/23766114 | SOUND | PvdR is the MFP of PvdRT-OpmQ; operon, architecture and identical mutant phenotypes support membership. The PMID:19906986 IDA code is wrong (full text: mutants only) -> PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE. | Salmonella MdtA Q8ZNQ3 (IDA PMID:24960027, AgBase) | Yes |
| PTN001253051 | GO:0015562 efflux transmembrane transporter activity | 2 | 86 (21 taxa) | GO:0015562, same six rows | SOUND | Pump exports PVD from the periplasm (mutant accumulation, complementation). Same IDA-code defect. contributes_to would be the more exact qualifier for an MFP, but GO practice uses enables. | MdtA Q8ZNQ3 (IDA PMID:24960027) | Yes |

Node term suits the clade (MdtA-like MFPs of tripartite pumps). No GO_CENTRAL defect.
OpmQ (PA2391) shares the operon but seeds a different node (PTN008411811); its
evidence-code defects are recorded in parallel in opmQ.

Other rows:
- GO:0002049 pyoverdine biosynthetic process IMP (PMID:12686626): INDIRECT-PHENOTYPE
  (not a seed). MODIFY to GO:0015891 siderophore transport; PSEUDOCAP WRONG_TERM,
  PROBABLE. Same call on opmQ. Contrast pvdD/pvdQ, enzymes for which the same term is
  correct.
- GO:1990195 macrolide transmembrane transporter complex and GO:1990961 xenobiotic
  detoxification (InterPro IPR030190 MacA alpha-hairpin): REMOVE; the full text
  excludes antibiotic export.
