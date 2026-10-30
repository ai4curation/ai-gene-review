# Historical nitrate-reductase identity bridge

PMID:10852866 directly disrupted and complemented the assimilatory nitrate-reductase gene in Pseudomonas putida KT2442, a rifampicin-resistant derivative of KT2440. Its full primary text was normally recovered at `url:https://pmc.ncbi.nlm.nih.gov/articles/PMC101894/?report=xml`.

The historical paper calls the cloned gene nasB (2,175 bp) and deposits AF203789. The modern Q88M71 record encodes a 1,341-residue fusion. Names alone do not establish equivalence, so the deposited translations were compared against the immutable Q88M71 UniProt sequence.

AF203789 encodes 724 residues identical to Q88M71 residues 1–724.

AF240673, the downstream historical sirA record, encodes 521 residues. Excluding its initiating methionine, all 520 remaining residues match Q88M71 residues 822–1341 exactly. Its initiating methionine corresponds to valine at position 821 of Q88M71. These records do not establish the intervening 725–820 sequence or demonstrate that the historical assayed clone expressed the complete modern fusion.

This bridge directly grounds catalytic-region identity and the native nitrate-assimilation genetic interpretation. It does not turn the 724-residue clone into a full-length Q88M71 biochemical assay, erase the KT2442/KT2440 distinction, establish donor preference, or prove a monomeric assembly. The modern fusion architecture is independently supported by the target's molybdopterin, flavodoxin, FAD-binding, and NAD(P)-binding signatures. PMID:32111737 assayed other organisms, not this target.

## Reproduction and source provenance

Run `uv run python genes/PSEPK/PP_1703/PP_1703-source-analysis/check_historical_identity.py` from the repository root. The script parses the preserved original downloads and immutable target UniProt file with Biopython, asserts the exact matches, and emits `historical-identity.json`, including input hashes. It performs no network access and does not change the inputs.

Unmodified ENA downloads acquired on 2026-10-30 UTC:

- https://www.ebi.ac.uk/ena/browser/api/embl/AF203789
- https://www.ebi.ac.uk/ena/browser/api/embl/AF240673

The EMBL record gene names differ from the primary paper's naming; matching is by actual translation, not symbol inference. These source-analysis files are curator analysis, not generated-provider research.
