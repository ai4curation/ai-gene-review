# glnG (NtrC / NRI), E. coli K-12, P0AFB8 — curation notes

Provider deep research was NOT run for this gene (not available in this session); these notes are based on the cached
publications in `publications/` and the UniProt record `glnG-uniprot.txt`.

## Function
- Response regulator phosphorylated by NtrB on an aspartate; autodephosphorylates: [PMID:2848245 "NRII-phosphate transfers its phosphate reversibly to an aspartic residue of NRI. NRI-phosphate is hydrolyzed to NRI and inorganic phosphate in a divalent cation-requiring autocatalytic reaction."] (Asp54, UniProt MOD_RES).
- Sigma-54-dependent activator: [PMID:2574599 "In its phosphorylated form the effector activates the initiation of transcription at promoters specific of sigma 54, rather than the abundant sigma 70."]
- Enhancer-like binding sites acting at a distance: [PMID:2574599 "These sites can be moved more than 1000 base pairs upstream or downstream without losing their effectiveness."]
- ATPase activity of the central domain, activated by phosphorylation-driven oligomerization: [PMID:10074086 "The phosphorylation of the N-terminal receiver domain of NRI (NRI-N) brings about the oligomerization of NRI dimers, activating an ATPase activity and transcriptional activation activity of the central domain of NRI"]
- NRI-P activates transcription of nitrogen-regulated promoters: [PMID:2874557 "we propose that NRI-phosphate activates transcription from nitrogen-regulated promoters"]

## Curation decisions
- DNA binding / sequence-specific DNA binding (IEA) -> MODIFY to GO:0000987.
- Regulation of DNA-templated transcription -> MODIFY to GO:0045893; cytoplasm -> MODIFY to cytosol (IDA, accepted deferring to curator; abstract-only paper).
- ATP binding kept non-core; NEW GO:0016887 ATP hydrolysis activity (TAS, PMID:10074086).
- GO:0005515 rows -> REMOVE per protein-binding policy.
- Not captured from cached literature: NtrC autorepression of glnLp and the Nac cascade; no cached papers to support these, so no annotations proposed.
