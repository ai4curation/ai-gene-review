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
this compound as carbon or nitrogen source."]. The adjacent partner PP_0075 is
an SLC26A/SulP-STAS protein rather than a canonical ABC permease plus
nucleotide-binding subunit. A syntenic Pseudomonas BetD homolog is nevertheless
described by in-silico analysis as a "substrate-binding ABC transporter protein"
[PMID:21369825]. Because orphan periplasmic binding proteins can use transporter
components encoded elsewhere, ABC-complex membership cannot currently be
confirmed or excluded.

## Curation position

- Retain periplasmic localization.
- Keep transport participation and exact choline binding unresolved pending
  direct substrate-binding or genetics for PP_0076.
- Reject a stand-alone transporter MF, but leave ABC-complex membership
  undecided pending identification of a cognate permease and ATPase.

## OpenScientist adjudication

The report retrieves useful ChoX/OpuAC-family context and explicitly notes the
lack of direct target characterization. It nevertheless constructs a complete
PP_0074/PP_0075/PP_0076 ABC importer by misidentifying PP_0074/Q88RQ5 as an ABC
ATPase. PP_0074 is shikimate dehydrogenase AroE, while PP_0075 is an
SLC26A/SulP-STAS protein. The definitive complex, partner, and choline-specific
conclusions are therefore not adopted.

## 2026-11-02 completion (choline-O-sulfate module curation)

The three UNDECIDED rows were resolved on biological grounds (all are InterPro2GO
IEA rows; there is no target-specific literature to wait for):

- GO:0033265 choline binding -> MODIFY to GO:0050997 quaternary ammonium group
  binding. The OpuAC (PF04069) domain supports a quaternary-ammonium ligand class but
  not choline specifically; the locus is induced by choline sulfate in Pseudomonas sp.
  ATCC19151 [PMID:21369825 "BetR activates betC and betR transcription in the presence
  of choline sulfate"], so choline-O-sulfate is an equally plausible ligand.
- GO:0015871 choline transport -> MODIFY to GO:0015697 quaternary ammonium group
  transport, for the same reason.
- GO:0043190 ABC transporter complex -> MARK_AS_OVER_ANNOTATED: no ABC permease or
  ATPase is encoded at the locus and none has been paired with PP_0076.

Core function now uses GO:0050997 (binding) with transport processes. Status set to
COMPLETE.
