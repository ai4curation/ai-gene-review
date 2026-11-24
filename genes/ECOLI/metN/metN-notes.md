# metN (P30750) notes

## Literature search (2026-11-24)

- Sources: all GOA-cited papers (PMID:12169620, 12218041, 12819857, 18621668,
  22095702, 30352853, plus the interaction screens 15690043, 20173761, 22841565,
  24561554), all already cached by `just fetch-gene`. Full text available for
  PMID:18621668 and PMID:30352853; the others are abstract-only.
- UniProt also cites PMID:25678706 (MetNI ATPase kinetics, ADP inhibition); not
  cached, not needed for any row.
- No deep-research provider file was generated.

## Findings

- metD locus = metNIQ, encoding a DL-methionine ABC importer with MetN the ATPase,
  MetI the permease, MetQ the binding protein [PMID:12218041 "MetD is an ABC
  transporter with Abc the ATPase, YaeE the permease, and YaeC the likely substrate
  binding protein."].
- Transports L- and D-methionine but not other natural amino acids [PMID:12819857
  "transports both L- and D-methionine, but not other natural amino acids"].
- MetNI structure: two MetN (ATPase) + two MetI; MetN C2 regulatory domain binds
  methionine and inhibits ATPase (transinhibition) [PMID:18621668 "Methionine binds
  to the dimerized carboxyl-terminal domain and is shown to inhibit ATPase
  activity."]. E166Q Walker B mutant has little ATPase activity.
- MetNI has high-affinity L-Met transport and broad specificity incl. D-Met
  [PMID:30352853 "exhibits both high-affinity transport toward l-methionine and broad
  specificity toward methionine derivatives, including d-methionine"].

## Complex-activity reasoning (staged RHEA:29779 -> GO:0015191 broadMatch)

RHEA:29779 is the whole-transporter reaction. UniProt places it on MetN (HAMAP
MF_01719) because MetN hydrolyses the ATP, but MetN alone moves no methionine: MetI
forms the translocation pathway and MetQ delivers substrate. In GO terms MetN
*contributes_to* L-methionine transmembrane transporter activity of the MetNIQ
complex; its own enabled activity is ATP hydrolysis (GO:0016887).

The review ACCEPTs the GO:0015191 claim (IBA, IDA) as a statement about the MetNIQ
complex MetN belongs to, following the precedent of the RbsA, TauB and SsuB reviews,
and records contributes_to GO:0015191 in core_functions. Under the backing criterion
(ACCEPT of the staged term) this backs the row, but with the caveat that the backing
is a contributes_to backing: an RHEA transport reaction on an NBD subunit is a
complex activity, and the GOA rows' `enables` qualifier should strictly be
`contributes_to` (recorded as a CHECK source defect, not a reason to reject the term).
The staged term itself is correct as a broadMatch (no ABC-type L-methionine term
exists; GO:0033232 is D-methionine only).
