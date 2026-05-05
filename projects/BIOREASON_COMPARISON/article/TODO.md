# Paper TODO

## SFT Prediction Reviews — Manual Review Required

The automated review script (`scripts/auto_review_sft_predictions.py`) was a mistake.
All SFT prediction assessments MUST be manually reviewed by reading the AIGR curated
review, GOA, and relevant publications. Automated comparison against GOA is not sufficient.

### Status
- 29 genes manually reviewed (335 predictions) — DONE, verified
- 155 genes auto-reviewed — MUST BE REDONE MANUALLY
- The auto-assessed files need to be reverted and reviewed properly

### Priority genes for manual review
Focus on genes where auto-review assigned COR or NPI, plus a representative sample
of CNN genes to verify the automated CNN calls are correct.
