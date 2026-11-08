# Source-record defects for GO_CENTRAL

3 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766131
- **Subject:** UniProtKB:Q9HTI7
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

The IBD for GO:0005275 amine transmembrane transporter activity at PTN000766131 (PTHR47737, ProW/ChoW-type permeases, about 13 leaf IBAs) is seeded by P. aeruginosa PA5377/CbcW (Q9HTI7, PseudoCAP IDA, PMID:19919675) and E. coli ProW (P14176). Both transport quaternary ammonium compounds (choline, glycine betaine, carnitine, proline betaine), which GO classifies under GO:0015651 and GO:0015418, not under amine transmembrane transporter activity. Please repoint the IBD to GO:0015418 (or GO:0015651). Because the node members are permease subunits, consider contributes_to.

## 2. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766131
- **Subject:** UniProtKB:Q9HTI7
- **Field:** GO_ID
- **Change:** check GO:0015226 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

The IBD for GO:0015226 carnitine transmembrane transporter activity at PTN000766131 (PTHR47737, about 13 leaf IBAs) rests only on P. aeruginosa PA5377/CbcW (Q9HTI7). In PMID:19919675, carnitine transport by CbcWV requires the separately encoded SBP CaiX (PA5388). The 98-100% identical P. syringae DC3000 Cbc core does not transport carnitine because DC3000 lacks caiX, and E. coli ProW, a co-seed of other IBDs at this node, is not a carnitine transporter. Substrate specificity is therefore not a property of the permease clade. Please remove this IBD, or replace it with GO:0015418 ABC-type quaternary ammonium compound transporting activity (contributes_to).

## 3. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** PANTHER:PTN000766131
- **Subject:** UniProtKB:Q9HTI7
- **Field:** GO_ID
- **Change:** check GO:1902603 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

The IBD for GO:1902603 carnitine transmembrane transport at PTN000766131 (PTHR47737, about 13 leaf IBAs) rests only on P. aeruginosa PA5377/CbcW (Q9HTI7, PseudoCAP IDA, PMID:21478341). Carnitine uptake by Cbc requires the separately encoded SBP CaiX (PMID:19919675). The 98-100% identical P. syringae DC3000 Cbc core does not transport carnitine, and E. coli ProW, in the same node, is a glycine betaine/proline betaine permease. Carnitine transport is therefore not a clade-wide property of these permeases. Please consider removing the IBD (keeping GO:0031460 and GO:0015871 if desired).
