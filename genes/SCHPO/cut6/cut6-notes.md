# cut6 (SPAC56E4.04c, UniProt P78820) notes

Fetch: `just fetch-gene SCHPO cut6` fetched the correct accession (ACAC_SCHPO, P78820, 2247 aa).

## Naming trap
- "cut6" = cell untimely torn 6 (a mitotic mutant class) but the gene is acetyl-CoA carboxylase, orthologue of S. cerevisiae ACC1.

## Evidence
- [PMID:8769419 "The cut6+ and lsd1+ genes are essential for viability and encode, respectively, acetyl CoA carboxylase and fatty acid synthetase, the key enzymes for fatty acid synthesis"].
- Mitotic phenotype: [PMID:8769419 "Two fission yeast temperature-sensitive mutants, cut6 and lsd1, show a defect in nuclear division"];
  [PMID:8769419 "A reduced level of fatty acid thus led to impaired separation of non-chromosomal nuclear components"].
- Domains/activities by similarity to S. cerevisiae ACC1 (Q00955) [UniProt:P78820]: BC, BCCP, CT; Mn2+, biotin cofactors.
- Cytoplasm/cytosol: ORFeome (PMID:16823372). Interaction with sad1 (two-hybrid, PMID:14655046; not in GOA).

## GO-CAM
- gomodel:678073a900002931 has TWO cut6 ACC activities: cytosol (678073a900004003, part_of GO:0006633) and
  mitochondrion (678073a900003027, part_of GO:2001295; location from the IBA PTN000429607 only).
  The module records only the cytosolic one.

## Differences from S. cerevisiae ACC1 review
- ACC1 review REMOVED the mitochondrion IBA because HFA1 is the mitochondrial ACC. S. pombe has no HFA1 counterpart,
  so here the same IBA is UNDECIDED (plausible dual targeting; no data).
- ACC1 core lists ER membrane (S. cerevisiae IDA); no S. pombe evidence, so cut6 core location is cytosol only.
- ACC1 core BP uses long-chain fatty acid biosynthetic process; here GO:0006633 (annotated) + GO:2001295.

## Decisions
- Core MF GO:0003989; BP GO:2001295 + GO:0006633; cytosol.
- mitotic nuclear membrane biogenesis (IMP): KEEP_AS_NON_CORE (downstream of lipid supply).
