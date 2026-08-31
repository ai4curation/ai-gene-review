# PP_0076 curation notes

## Evidence boundary

PP_0076 (Q88RQ3) is a 307-aa signal-peptide-bearing periplasmic binding protein
with choline/glycine-betaine transporter substrate-binding domains
[`PP_0076-uniprot.txt`, "FT   SIGNAL          1..20";
"InterPro; IPR017783; ABC_choline_sub-bd."]. It has no transmembrane helix and
therefore cannot independently provide transmembrane transporter activity.

The adjacent KT2440 `betC` region was implicated in choline-O-sulfate
utilization, but the available paper does not individually assay PP_0076 and
shows that intact choline-O-sulfate still accumulates when `betC` is deleted
[PMID:17116241, "This mutant still accumulated intact COS but failed to use
this compound as carbon or nitrogen source."]. The current partner PP_0075 is
an SLC26A/SulP-STAS protein rather than a canonical ABC permease plus
nucleotide-binding subunit.

## Curation position

- Retain periplasmic localization.
- Keep transport participation and exact choline binding unresolved pending
  direct substrate-binding or genetics for PP_0076.
- Reject a stand-alone transporter MF and an asserted ABC-complex membership;
  these conflict with the target architecture and current partner annotation.

## OpenScientist adjudication

The report retrieves useful ChoX/OpuAC-family context and explicitly notes the
lack of direct target characterization. It nevertheless constructs a complete
PP_0074/PP_0075/PP_0076 ABC importer by misidentifying PP_0074/Q88RQ5 as an ABC
ATPase. PP_0074 is shikimate dehydrogenase AroE, while PP_0075 is an
SLC26A/SulP-STAS protein. The definitive complex, partner, and choline-specific
conclusions are therefore not adopted.
