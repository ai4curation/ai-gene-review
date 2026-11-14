# gal7 (SPBPB2B2.10c, UniProt Q9HDU5) notes

## Identity
- UniProt: Galactose-1-phosphate uridylyltransferase, EC 2.7.7.12 by similarity to human GALT (P09148); GalT type 1 family; Zn2+ cofactor and homodimer by similarity [UniProt:Q9HDU5].

## Evidence
- Genetic: in uge1 gal10 double mutants, galactose rescues galactosylation and UDP-galactose; deleting gal7 abolishes the rescue [PMID:19942659 "Disruption of gal7(+), encoding galactose-1-phosphate uridylyltransferase, in the uge1Deltagal10Delta strain reversed suppression of the galactosylation defect and reduced levels of UDP-galactose"; "is converted into UDP-galactose via galactose 1-phosphate by Gal7p"].
- Galactose growth requires derepression of the gal cluster [PMID:21075050].

## Location
- HTP YFP: cytosol and nucleus [PMID:16823372]. Nuclear signal is probably diffusion of a small soluble fusion; no nuclear function known.

## GO-CAM
- 6796b94c00002484: gal7 enables GO:0008108 (IMP PMID:19942659 + IBA), cytosol, part_of GO:0033499. Consistent.

## 2026-11-12 audit (to COMPLETE)
- No deep-research provider file was available; none was generated. Literature check: cached abstracts PMID:19942659, PMID:21075050, PMID:16823372; web search found no further gal7-specific primary paper.
- PAINT: PTHR11943 has an IRD, NOT GO:0033499 at PTN008530881 (Schizosaccharomyces, 20260828), blocking the Leloir IBD from PTN000235304; not yet reflected in the cached GOA file (`just paint-losses SCHPO gal7`). Read as contradicted: wild-type silencing of the subtelomeric gal cluster is a regulatory state, and gal7 functions when expressed [PMID:19942659 "is converted into UDP-galactose via galactose 1-phosphate by Gal7p"]; [PMID:21075050 "these transformants grew on galactose medium"]. GO:0033499 rows kept ACCEPT; question raised in suggested_questions. The family-level assessment is handled in the PTHR11943 family review.
- Corrected the EXP GO:0033499 summary: the gal7delta::ura4+ result in PMID:21075050 is a silencing reporter (5-FOA growth), not a galactose-growth requirement test.
