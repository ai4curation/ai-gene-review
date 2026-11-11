# EGR2 evidence results

The saved-input replay resolves all four PAINT assertions in the 1,852-node PTHR23235 tree. The target leaf is PTN002545415, and its ungapped MSA sequence exactly matches the official 476-residue P11161 sequence. Three IBD assertions are at PTN004619861 and the nucleus assertion is at PTN009066117; both nodes lie on the target path. Literal full GAF fields and physical line numbers are retained in `results.json`. Target self-grounding and donor count are not treated as evidence failures.

The complete saved mouse Egr2 query contains 92 annotations. These include the real GO:0006611 source assertion from PMID:17938205, the KLF4-binding assertion from PMID:18396140 and SUMO E3/sumoylation assertions from PMID:21836637. A database join establishes the provenance of these claims; interpretation of the experiment and organism belongs to the source guide and annotation reasons.

All 11 current target IntAct records are retained. The PMID:14532282 HCFC1 record includes EGR2 residues 1–170 and HCFC1 residues 1–380/P134 among its feature fields. The reference ROGIDs match the current human parent sequences. These checks identify the curated database parents and regions; the primary Methods separately identify murine Krox20. HCFC1's official functional classification is transcription coactivator, WWP2's is ubiquitin E3 ligase, and mouse KLF4's is sequence-specific transcription factor. The classification is separate from the evidence that each pair associates.

All 12 imported Reactome assertions resolve through 17 saved API objects to human EGR2 entity R-HSA-977385, reference P11161, modeled residues 1–476. The protein's own compartment is nucleoplasm. Two events represent EGR2 expression output; these are not used to infer that EGR2 performs its own induction. The other paths retain their actual input, set-member or complex-component relationships. These models do not establish equivalent localization of both natural products or represent 12 independent localization experiments.

Current official term definitions and typed binding/export ancestors are included in the computed results. The public source guide provides the experimental distinctions needed to interpret these database records. Full numerical/identifier fields, URLs and input hashes are available in `results.json` and `input-manifest.json`.

## Reproduction checks

- The script derives identities, counts and paths from complete hashed inputs.
- The saved inputs and computed results are included; no network access is required.
- Normal and optimized Python executions agree, and altered input is rejected.
- This is a target-specific source reconstruction, not a predictive model. Generalization to another gene was not tested.
