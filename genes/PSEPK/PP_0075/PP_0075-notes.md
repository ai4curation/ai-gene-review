# PP_0075 curation notes

## Evidence boundary

PP_0075 (Q88RQ4) is a 521-aa multi-pass membrane protein annotated as a
choline-sulfate transporter. Its current architecture is SLC26A/SulP plus a
cytoplasmic STAS domain, not a canonical ABC permease/ATPase architecture
[`PP_0075-uniprot.txt`, "InterPro; IPR001902; SLC26A/SulP_fam.";
"InterPro; IPR002645; STAS_dom."].

The adjacent KT2440 `betC` locus was studied genetically. The paper describes
an adjacent putative ABC transporter, but the decisive phenotype is that a
`betC` mutant still accumulated intact choline-O-sulfate while failing to use
it as carbon or nitrogen. This establishes a role for BetC in utilization and
shows that uptake can occur independently of BetC; it does not directly assay
PP_0075 or establish PP_0075 as the sole choline-O-sulfate importer
[PMID:17116241, "This mutant still accumulated intact COS but failed to use
this compound as carbon or nitrogen source."].

## Curation position

- Retain the well-supported membrane location and generic transmembrane
  transport process.
- Treat choline-O-sulfate specificity as a pathway-level candidate assignment,
  not as an experimentally established gene-level function.
- Do not annotate PP_0075 as an ABC-transporter component.

## OpenScientist adjudication

The report correctly retrieves the SulP/SLC26-STAS architecture and the absence
of a direct transport assay. Its proposed sulfate cargo remains speculative.
Its assignment of intact choline-O-sulfate uptake to an unspecified ABC route
is also not established by the target or cached KT2440 evidence.
