# betC curation notes

## Evidence boundary

KT2440 BetC (Q88RQ2; PP_0077) is assigned EC 3.1.6.6 and the exact
choline-sulfatase family signature [`betC-uniprot.txt`, "EC=3.1.6.6";
"InterPro; IPR017785; Choline-sulfatase."]. The KT2440 genetic study found
that a `betC` mutant accumulated intact choline-O-sulfate but could not use it
as carbon or nitrogen, supporting a central role in utilization rather than
uptake or osmoprotection [PMID:17116241, "This mutant still accumulated intact
COS but failed to use this compound as carbon or nitrogen source."].

Direct ortholog evidence comes from Sinorhizobium meliloti BetC (UniProt
O69787): the gene encodes a choline sulfatase converting choline-O-sulfate, and
more slowly phosphorylcholine, to choline [PMID:9736747, "a new gene (betC) was
identified as encoding a choline sulfatase catalyzing the conversion of
choline-O-sulfate and, at a lower rate, phosphorylcholine, into choline."].

The same Sinorhizobium choline sulfatase was subsequently characterized as a
purified enzyme and by X-ray crystallography [PMID:29458126,
"Sinorhizobium meliloti choline sulfatase (SmCS) efficiently catalyzes the
hydrolysis of alkyl sulfate choline-O-sulfate"]. This provides a direct
structural and kinetic exemplar for the exact BetC family assignment.

PANTHER PTHR45953:SF1 is not used as an exact BetC selector because its official
label is `IDURONATE 2-SULFATASE` and its membership spans functionally distinct
sulfatases. InterPro IPR017785 and the characterized UniProt exemplar provide a
more defensible module selector.

## Curation position

- Accept exact choline-sulfatase activity as the core function.
- Retain sulfuric ester hydrolase activity as a valid but broad non-core parent.
- Retain cytoplasm only as non-core localization evidence.

## OpenScientist adjudication

The report correctly identifies Q88RQ2, the C52-A-P-S-R sulfatase motif, the
direct KT2440 `betC` phenotype, and the absence of purified target-protein
kinetics. Its claim that an adjacent ABC transporter imports choline-O-sulfate
is not adopted: PP_0075 has SLC26A/SulP-STAS architecture, no cognate local ABC
ATPase is established, and neither PP_0075 nor PP_0076 has a target-specific
transport assay.
