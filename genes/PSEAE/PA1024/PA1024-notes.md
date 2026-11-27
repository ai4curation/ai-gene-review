# PA1024 (Q9I4V0) notes

## Identity

- Locus PA1024, *Pseudomonas aeruginosa* PAO1; UniProt Q9I4V0 (NQRED_PSEAE, reviewed), 328 aa.
- Pfam PF03060 (NMO), InterPro IPR004136 (NMO), PANTHER PTHR32332:SF20; TIM barrel (Gene3D 3.20.20.70).
- Historically named "2-nitropropane dioxygenase" (the old name for nitronate monooxygenase, NMO).

## Literature

- Crystal structures with FMN and 2-nitropropane (PDB 2GJL, 2GJN) [PMID:16682407 "Here we report the first
  crystal structure of 2-nitropropane dioxygenase from Pseudomonas aeruginosa in two forms: a binary complex
  with FMN and a ternary complex with both FMN and 2-nitropropane."]. This paper assumed NMO activity from the
  annotation and named His152 as the catalytic base. Only the abstract is cached.
- Kinetic characterisation showed the purified enzyme has no NMO activity but is an NADH:quinone reductase
  [PMID:27502282 "Purified PA1024 did not exhibit nitronate monooxygenase activity; however, it displayed
  NADH:quinone reductase and a small NADH:oxidase activity."]; NADH is preferred to NADPH [PMID:27502282 "The
  enzyme preferred NADH to NADPH as a reducing substrate."]; it reduces many quinones by a Ping Pong Bi Bi
  mechanism [PMID:27502282 "PA1024 could reduce a broad spectrum of quinone substrates via a Ping Pong Bi Bi
  steady-state kinetic mechanism, generating the corresponding hydroquinones."]; it is not an azoreductase
  [PMID:27502282 "The enzyme was not able to reduce the azo dye methyl red"]. The authors define a new NQR class
  inside the NMO Pfam family, most of whose members are misannotated as NMO [PMID:27502282 "the vast majority
  of which are currently misannotated as nitronate monooxygenase"].
- Only the abstract of PMID:27502282 is available: PMC5076524 returned no full text through the PubMed MCP.
  The UniProt curated record (ECO:0000269, PubMed:27502282) gives the detail: KM values of 10-355 uM and kcat
  6-28 s-1 for eight naphtho- and benzoquinones, FMN cofactor (1 per subunit), and monomer (from the
  structure paper).
- UniProt CAUTION: the NMO activity reported by Ha et al. was "likely due to the non-enzymatic reaction of
  propyl-2-nitronate with oxygen".
- Physiological role: UniProt says only "May be required to maintain an appropriate [NAD(+)]/[NADH] ratio for
  the catabolism of fatty acids". This is speculative, and I propose no process term.

## Annotation decisions

- GO:0050136 NADH dehydrogenase (quinone) (non-electrogenic) activity (EXP, IEA RHEA/EC): ACCEPT, the core MF.
  The broad quinone range rules out the ubiquinone- or menaquinone-specific children (GO:0120555, GO:0103036).
  NADH is preferred over NADPH, so the NAD(P)H parent GO:0003955 is less accurate.
- GO:0016491 oxidoreductase activity (PseudoCAP IDA; IBA): true but uninformative. MODIFY to GO:0050136,
  which the gene already carries.
- GO:0018580 nitronate monooxygenase activity (IEA InterPro IPR004136): REMOVE. It is directly contradicted by
  the enzyme assays. The InterPro2GO mapping of IPR004136 to NMO is too broad, because the entry also covers
  the PA1024-type NQR class.
- NEW GO:0010181 FMN binding: FMN is bound in the crystal structures and is the cofactor of the kinetically
  characterised enzyme.

## PseudoCAP IBA-seed assessment

QuickGO (2026-10-28, withFrom=PTN002844975) returned 111 GO:0016491 IBA rows. The worklist reports 122 leaf
IBAs, so the counts differ slightly between releases. The leaves include PA1024 as the only PAO1 member,
plus plants (e.g. taxon 4432, 3635, 4565), fungi (227321, 5270), *Mycobacterium tuberculosis* (83332) and
other bacteria. The characterised true NMO of PAO1, PA4202 (Q9HWH9), takes its NMO IBA from a different node
(PTN001284536). PTN002844975 is therefore a broad cross-kingdom clade that does not contain the canonical
NMO.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002844975 | GO:0016491 oxidoreductase activity | 1 (sole) | 122 (69 taxa) | GO:0016491 oxidoreductase activity, IDA, PMID:27502282 (PseudoCAP); also GO:0050136 EXP, PMID:27502282 (UniProt) | SOUND | Purified PA1024 is shown to be an FMN-dependent NADH:quinone reductase, so the seed is direct biochemistry, not a phenotype. The generic node term is correct and is a suitably cautious choice for a clade spanning bacteria, fungi and plants: only one member has been characterised, and the family also contains true NMOs. Propagating the specific NQR activity would be poorly supported. For PA1024 itself, the generic term is redundant with GO:0050136. |

No PseudoCAP or GO_CENTRAL defect is recorded. The one upstream problem is the InterPro2GO NMO mapping.
