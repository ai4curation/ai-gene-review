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

## 2026-10-30 follow-up: why the modern single-CDS model is accepted

The historical fragments do not themselves cover the complete modern fusion, but their missing interval is not a gap in the modern KT2440 chromosome. The downloaded primary genomic interval **AE015451.2:1899450–1903475** is annotated as a single, uninterrupted PP_1703 CDS. Translation with the record's bacterial code (table 11) produces **1,341 amino acids followed by one terminal stop, with zero internal stops**, and matches both **AAN67324.2** and the immutable **Q88M71** sequence exactly. The genomic sequence therefore covers the historical split and the intervening segment positively; acceptance of the fusion does not rest only on a database protein name or analogy to NasN.

The exact comparison also exposes a real record difference: AF203789 ends with TGA at coding nucleotides 2173–2175, whereas the corresponding modern KT2440 triplet is GAT (Asp725), continuing the ORF. Two earlier nucleotide differences are synonymous, consistent with the exact first-724-residue protein match. These observations do **not** establish whether the terminal difference arose from strain variation, historical sequencing/annotation, or the cloned construct. KT2442 and KT2440 must remain distinguished. No conclusion that the historical missing interval disproves the fusion is justified.

The modern genomic continuity, exact full translation, and coherent catalytic/diflavin architecture support accepting the single-CDS model for the KT2440 target. A `gene_model_issues: SUSPECTED` flag is therefore not warranted solely by the two historical ORFs. This is a supported genomic model, not direct demonstration that the full-length polypeptide was purified or that every historical construct encoded it. Donor preference, enzyme kinetics, assembly, and full-length native expression remain separate experimental questions. The sequence revision is consistent with the target's 2016 AAN67324.2/UniProt sequence update and its PMID:26913973 genome-revisit citation; that paper's abstract does not itself constitute a PP_1703-specific junction assay.

The original genomic interval and GenPept response bytes are preserved beside `modern-source-provenance.json`. `check_modern_cds.py` accepts explicit input paths, selects the locus-tagged CDS, translates the actual nucleotide sequence, and calculates all comparisons in `modern-cds-proof.json`. Reproduce with `just --justfile genes/PSEPK/PP_1703/PP_1703-source-analysis/justfile modern`. These sequences support the model, not the mixed nitrate/sulfite function label in the protein record. See `RESULTS.md` for checks and limitations.
