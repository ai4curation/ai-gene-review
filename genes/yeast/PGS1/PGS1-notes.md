# PGS1 (PEL1, YCL004W, P25578) notes

## Identity
- CDP-diacylglycerol--glycerol-3-phosphate 3-phosphatidyltransferase (PGP synthase), EC 2.7.8.5; PLD superfamily (HKD) [UniProt:P25578].

## Evidence
- PGS1 encodes the major PGP synthase; null lacks PGP synthase activity, PG and CL [PMID:9545322 "The pgs1 null mutant exhibited no detectable in vitro PG-P synthase activity and no detectable CL or phosphatidylglycerol (PG); significant CL synthase activity was still present."]
- Committed step of CL synthesis [PMID:9545322 "functions as the committed and rate-limiting step in the biosynthesis of cardiolipin (CL)"].
- Mitochondrial localization [PMID:9799363 "its fluorescent protein was localized to mitochondria"]; activity in inner membrane [PMID:3005242 "Phosphatidylserine decarboxylase and phosphatidylglycerolphosphate synthase were localized exclusively in the inner mitochondrial membrane"].

## Curation decisions
- Core: GO:0008444; CL and PG biosynthesis; mitochondrial inner membrane (not in GOA; GOA has only mitochondrion).
- Cytosol RCA removed (conflicts with mitochondrion RCA from PHOS-PWY). catalytic activity IEA -> MODIFY.
