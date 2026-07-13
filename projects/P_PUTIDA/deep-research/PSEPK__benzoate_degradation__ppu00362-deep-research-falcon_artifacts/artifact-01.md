| Module Step | Expected Enzyme/Activity | Gene(s) in KT2440 | Status | Notes |
|---|---|---|---|---|
| Benzoate hydroxylation | Benzoate 1,2-dioxygenase | benA/benB/benC (PP_3161-PP_3163) | COVERED | Direct experimental and genomic evidence for ben cluster in KT2440 (pqac-00000000, pqac-00000003, pqac-00000029) |
| cis-diol dehydrogenation | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase | benD (PP_3164) | COVERED | Direct experimental and genomic evidence for benzoate cis-diol to catechol conversion (pqac-00000003, pqac-00000005) |
| Catechol ortho-cleavage | Catechol 1,2-dioxygenase | catA-I (PP_3713), catA-II (PP_3166) | COVERED | Two paralogs; catA-II is embedded in the ben cluster, supporting benzoate-derived catechol processing (pqac-00000000, pqac-00000003, pqac-00000027) |
| Muconate cycloisomerization | Muconate cycloisomerase | catB (PP_3715) | COVERED | Direct evidence for catechol-branch ortho-cleavage enzyme (pqac-00000034, pqac-00000035) |
| Muconolactone isomerization | Muconolactone delta-isomerase | catC (PP_3714) | COVERED | Direct evidence for catechol branch lower-pathway step (pqac-00000000, pqac-00000035) |
| 4-hydroxybenzoate hydroxylation | 4-hydroxybenzoate 3-monooxygenase | pobA (PP_3537) | COVERED | Direct evidence for protocatechuate-entry branch; pob cluster mapped in KT2440 (pqac-00000001, pqac-00000008, pqac-00000029) |
| Protocatechuate 3,4-dioxygenase | Protocatechuate 3,4-dioxygenase | pcaG/pcaH (PP_4655/PP_4656) | COVERED | Direct evidence for ring-cleavage step of the protocatechuate branch (pqac-00000009, pqac-00000026) |
| 3-carboxy-cis,cis-muconate cycloisomerization | 3-carboxy-cis,cis-muconate cycloisomerase | pcaB (PP_1379) | COVERED | Direct evidence from pca cluster annotation and pathway mapping (pqac-00000001, pqac-00000008, pqac-00000009) |
| 4-carboxymuconolactone decarboxylation | 4-carboxymuconolactone decarboxylase | pcaC (PP_1381) | COVERED | Direct evidence from pca cluster annotation and pathway mapping (pqac-00000001, pqac-00000009) |
| 3-oxoadipate enol-lactone hydrolysis | 3-oxoadipate enol-lactonase | pcaD (PP_1380) | COVERED | Direct evidence for shared lower-pathway step after branch convergence (pqac-00000001, pqac-00000009, pqac-00000036) |
| 3-oxoadipate CoA transfer | 3-oxoadipate CoA-transferase | pcaI/pcaJ (PP_3951/PP_3952) | COVERED | Direct evidence for terminal beta-ketoadipate CoA activation step (pqac-00000009, pqac-00000033) |
| Beta-ketoadipyl-CoA thiolysis | Beta-ketoadipyl-CoA thiolase | pcaF-I (PP_1377) | COVERED | Canonical terminal thiolase of the beta-ketoadipate pathway despite other thiolase paralogs elsewhere in genome (pqac-00000009, pqac-00000033, pqac-00000034) |
| Gallate dioxygenation | Gallate dioxygenase | galA (present in genome; not in candidate list) | CANDIDATE_UNCERTAIN | galA is supported by recent KT2440 gallate studies, but it is absent from the supplied candidate list; gallate is a side branch, not core benzoate entry (pqac-00000014, pqac-00000015, pqac-00000016) |
| 4-oxalomesaconate tautomerization | 4-oxalomesaconate tautomerase | galD (PP_2513) | COVERED | Covered for the gallate branch specifically, not required for strict benzoate-to-catechol module satisfiability (pqac-00000014, pqac-00000015) |
| OMA hydration | 4-oxalomesaconate hydratase | galB (PP_2515) | COVERED | Covered for the gallate branch specifically (pqac-00000014, pqac-00000015) |
| CHA aldol cleavage | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase | galC (PP_2514) | COVERED | Covered for the gallate branch specifically (pqac-00000014, pqac-00000015) |
| Ferredoxin electron transfer | Generic 2Fe-2S ferredoxin | fdx (PP_0847) | CANDIDATE_UNCERTAIN | Generic ferredoxin; no direct evidence that this locus is the dedicated benzoate dioxygenase electron-transfer partner in KT2440 (pqac-00000025, pqac-00000029) |
| Cytochrome P450 node | Cytochrome P450 | PP_1950 | NOT_EXPECTED | No direct evidence for a role in core benzoate/beta-ketoadipate degradation in KT2440; likely KEGG neighborhood/over-map carryover (pqac-00000025) |


*Table: This table summarizes step-by-step satisfiability of KEGG ppu00362 in Pseudomonas putida KT2440, distinguishing core covered steps from side-branch and uncertain assignments. It is useful for manual pathway curation and deciding which candidate genes truly satisfy the benzoate/beta-ketoadipate module.*