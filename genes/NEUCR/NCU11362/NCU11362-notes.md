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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence: UniProt record, GOA seed, PAINT/IBA WITH/FROM, cached papers PMID:34050143 (S. pombe Mtl16 knockout, U6 m6A37, intron retention), PMID:40841561 (S. pombe METTL16 structures), PMID:29051200 (human METTL16 U6 A43 and MAT2A), and a new alignment `NCU11362-bioinformatics/RESULTS-rereview.md` (script `compare_mettl16_rereview.py`, `uv run --script`).

Identity: A7UX10 is the full-length 541-aa product of NCU11362, not a fragment or isoform. It covers 99.5% of S. pombe Mtl16 (O42662, 385 aa; 39.7% identity) including the C-terminal region, and carries an extra ~79-residue disordered N-terminal extension. A single NPPF catalytic motif (282-285) maps onto Mtl16 NPPF155 and human NPPF184.

Evolutionary grounding: UniProt places A7UX10 in PANTHER PTHR13393:SF0, the same subfamily as S. pombe Mtl16 and human METTL16; all GOA IBA rows come from PAINT node PTN000333540 (eukaryotic METTL16). The family review `interpro/panther/PTHR13393/PTHR13393-review.yaml` notes that SF0 also holds RlmF and PsiM members, so SF0 alone does not license substrate transfer; the METTL16-specific PTN node plus the full-length alignment does. No disagreement with the family review on subfamily placement.

Decisions:
- GO:0120048 U6 snRNA m6A methyltransferase (IBA): ACCEPT, core. Donors include S. pombe Mtl16 (experimental) and human METTL16.
- GO:0000398 mRNA splicing via spliceosome (IBA, Mtl16 donor): ACCEPT. U6 m6A pairs with the 5' splice site; loss causes intron retention.
- GO:0005634 nucleus (IBA): ACCEPT.
- GO:0008168 methyltransferase activity (IEA): MODIFY to GO:0120048.
- GO:0001734 mRNA m6A methyltransferase (IBA, animal donors only): changed from MARK_AS_OVER_ANNOTATED (uncommitted draft) to UNDECIDED. PAINT put the activity at the eukaryotic node; S. pombe lacks mRNA m6A, but S. pombe is a different subphylum and there are no Neurospora data, so a loss in the target cannot be asserted.
- GO:0010608 post-transcriptional regulation of gene expression (IBA, animal donors): UNDECIDED for the same reason (the animal MAT2A/sams regulatory deployment has not been tested in Neurospora).

Relative to review next: S. pombe Mtl16 (SPAC27D7.08c, O42662), same PANTHER subfamily and PAINT node, the closest experimentally characterised ortholog; no review exists in the repo (human METTL16 Q86W50 is also unreviewed). Modules: none contain METTL16; `modules/dmel_m6a_methyltransferase_complex.yaml` explicitly places Mettl16 outside its boundary.
