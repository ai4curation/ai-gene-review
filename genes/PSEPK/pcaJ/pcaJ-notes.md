# pcaJ notes

- PcaJ is the partner subunit of the heteromeric PcaIJ
  beta-ketoadipate:succinyl-CoA transferase [PMID:1624453 "two proteins of sizes
  appropriate to encode the two nonidentical subunits of the enzyme were
  produced in Escherichia coli"]. The specific GO:0047569 term is retained, but
  the gene product contributes to the complex activity rather than independently
  enabling it.

- The source `enables` annotation for GO:0047569 is therefore reviewed as
  `MODIFY`, retaining the term while replacing its relation with
  `contributes_to`.

- The lower-pathway module starts at 3-oxoadipate and treats PcaIJ CoA transfer
  as the first reaction, followed by PcaF thiolysis.
