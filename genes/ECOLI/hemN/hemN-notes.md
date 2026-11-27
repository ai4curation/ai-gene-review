# hemN (P32131, E. coli K-12) notes

Deep research was unavailable for this gene (falcon returns 403 and asta returned nothing
useful in RADICAL_SAM Phase 1), so these notes are built from cached papers, PubMed and UniProt.

## Function
- Oxygen-independent coproporphyrinogen III dehydrogenase (CgdH; EC 1.3.98.3, RHEA:15425).
  [PMID:12114526 "A newly established anaerobic enzyme assay was used to demonstrate for the first time in vitro coproporphyrinogen-III oxidase activity for recombinant purified HemN"]
- Needs SAM, NAD(P)H and cytoplasmic components; monomer. The cluster cysteines are Cys62/66/69, and the GGGTP SAM motif (Gly111/113) is essential.
  [PMID:12114526 "The enzyme requires S-adenosyl-l-methionine (SAM), NAD(P)H, and additional cytoplasmatic components for catalysis"]
- First crystal structure of a radical SAM enzyme, at 2.07 A (PDB 1OLT), with two SAMs.
  [PMID:14633981 "HemN, strikingly, binds a second SAM immediately adjacent to the first"]
- Two SAM are cleaved per protoporphyrinogen IX, and SAM2 is needed for catalysis.
  [PMID:15967800 "Two molecules of AdoMet were cleaved during one catalytic cycle for the formation of one molecule of protoporphyrinogen IX"]
- SAM2 acts as a radical relay through a methylene radical. [PMID:37101575 "the second SAM was shown to act as a radical relay"]
- Allylic substrate radical. [PMID:16606627 "this coproporphyrinogenyl radical is allylic and encompasses carbon atoms 3', 3, and 4"]
- HemF is the O2-dependent isoenzyme. [PMID:12975365 "two structurally unrelated enzymes, one oxygen-dependent (HemF) and one oxygen-independent (HemN)"]

## GO term checks (QuickGO, 2026-10-19)
- GO:0004109 coproporphyrinogen oxidase activity is defined with O2 as oxidant (the HemF reaction).
- GO:0051989 coproporphyrinogen dehydrogenase activity = coproporphyrinogen III + 2 SAM -> protoporphyrinogen IX + 2 CO2 + 2 Met + 2 dAdo. This is HemN's reaction.
- GO:0006782 protoporphyrinogen IX biosynthetic process is OBSOLETE, so the process row is refined to GO:0006785 heme B biosynthetic process (as in genes/PSEPK/hemN).

## PAINT
- PTN000358281 (whole HemN/HemW node): cytoplasm, 4Fe-4S binding, porphyrin biosynthesis.
- PTN000358335 (HemN clade, taxon:2): GO:0051989. The curator kept the MF off HemW, but the BP sits on the deeper node (see genes/ECOLI/hemW).

## Decisions
- MODIFY GO:0003824 and GO:0004109 to GO:0051989. MODIFY GO:0051536 to GO:0051539. MODIFY GO:0006779 (IBA, IEA) to GO:0006785.
- ACCEPT the cytoplasm rows (3), GO:0051539 (2) and GO:0051989 (3).
- NEW GO:1904047 SAM binding (IDA, PMID:14633981).
- Inconsistency: genes/PSEPK/hemN marks GO:0051536, GO:0051539 and GO:0046872 KEEP_AS_NON_CORE. That predates the RADICAL_SAM treatment rule (MODIFY / ACCEPT / MODIFY).
