# NCU11362 evidence notes

NCU11362 is a METTL16-family RNA N6-adenosine methyltransferase inferred to modify U6 snRNA using S-adenosylmethionine. The conserved U6 modification promotes accurate pre-mRNA splice-site recognition. Nuclear RNA modification is strongly supported by fungal ortholog experiments; a distinct Neurospora mRNA methylation repertoire is unresolved.

## Identity and provenance

The exact current accession is A7UX10; NCU11362 is retained as the current locus identifier. No independently established formal gene-symbol replacement was found. Original claims are preserved in NCU11362-protnlm-source.json from the live API snapshot retrieved 2026-09-09T03:00:51.831347+00:00. The current sequence is not proven to be the prediction-time input, and placeholder API dates do not establish release or training membership.

## Primary evidence and justified transfer

- [PMID:40841561] "The N6-methyladenosine (m6A) modification in U6 snRNA, catalyzed by METTL16
using S-adenosylmethionine (SAM) as the methyl donor, is required for efficient
and accurate pre-mRNA splicing."
- [PMID:34050143] "We found that a subset of introns was retained in mRNAs, indicating a splicing defect caused by loss of m6A in U6 snRNA."

The specific domain/family observation used is `DR   InterPro; IPR010286; METTL16/RlmF.`. Family membership and characterized relatives establish the inference; ARBA or AI-generated names are not independent functional evidence. PAINT is a curator-reviewed ancestral assertion, not donor-count evidence.

## Unresolved assertions

- mRNA m(6)A methyltransferase activity: The curated ancestral assertion predicts mRNA methylation, but METTL16 substrate repertoires differ among eukaryotes. The verified fungal experiments establish U6 methylation and consequent mRNA splicing, which do not by themselves show methyl-group transfer to mRNA. Neurospora mRNA substrate recognition or a resolved fungal-clade substrate analysis is needed to adjudicate this more specific activity.

Frozen UniProt JSON carried GO:0052907/GO:0070475 rRNA assertions, whereas the current QuickGO seed carries METTL16 U6 and mRNA-methylation assertions. The main review assesses the actual seeded rows. The broad external metabolic-process claim is evaluated through supported RNA methylation; bacterial 23S substrate specificity is not transferred to this eukaryotic METTL16. GO:0001510 was verified through QuickGO before adding it.

## Falcon report appraisal

The actual Falcon report was inspected. It recognizes the broad METTL16/RlmF domain but does not evaluate the specific PANTHER METTL16 subfamily or current PAINT U6 assertion and omits the 2021 and 2025 fission yeast experiments. Its warning against inferring a specific RNA substrate from the broad shared fold alone is appropriate. Here the stronger inference combines the specific METTL16 subfamily, the curator-defined PTN000333540 assertion, and experimentally characterized fungal U6 methylation (PMID:34050143; PMID:40841561). The current sequence contains the NPPF motif, visible in the unedited UniProt sequence record; this corroborates catalytic-family conservation without being treated as an enzyme assay. The formal RNA methylation proposal is explicitly ISS, not a Neurospora experiment. Mammalian MAT2A substrate specificity remains unresolved on this target.

Specific family excerpt: "DR   PANTHER; PTHR13393:SF0; RNA N6-ADENOSINE-METHYLTRANSFERASE METTL16; 1.".
