# Caulobacter ImuABC consultation

Reviewed all 16 annotation rows across imuA, imuB and dnaE2, including four historical NEW proposals. Source payloads/order and all historical proposals are preserved; no rows were added, retired or deleted. Four action changes are recorded with full before/after evidence in `action-ledger.yaml`:

- imuA SOS response: KEEP_AS_NON_CORE to ACCEPT. Native effector genetics, beyond promoter induction alone, supports the core damage-response role.
- dnaE2 cytoplasm: KEEP_AS_NON_CORE to ACCEPT. Inferred evidence does not make the central functional location peripheral.
- dnaE2 DNA replication: MARK_AS_OVER_ANNOTATED to MODIFY toward the existing TLS proposal. Current GO places TLS under DNA damage tolerance, which is **part_of** DNA replication. This is not a pure is_a path, and the real relationship is archived and checked.
- dnaE2 3-prime-to-5-prime exonuclease: MARK_AS_OVER_ANNOTATED to UNDECIDED. The mycobacterial PHP-residue discussion has not been verified residue by residue in Caulobacter. Error-proneness alone does not establish proofreading loss.

The core Caulobacter evidence is the 2005 deletion/complementation, epistasis, expression and rpoB mutation-spectrum study, performed in NA1000, a CB15 derivative. The imuA and imuB mutations were in-frame deletions, whereas dnaE2 was disrupted by insertion/truncation. These data support a mutagenic tolerance pathway; they do not directly observe polymerase insertion opposite a defined lesion or a physically assembled Caulobacter complex.

Caulobacter ImuA still has no asserted molecular-function term. Its RecA-like/P-loop fold and genetic requirement do not establish DNA binding, ATP hydrolysis or the exact accessory step. PMID38591662 demonstrates ATPase and DNA binding for **Myxococcus** ImuA, and direct interaction with an ImuB construct. This now informs a target-specific knowledge gap rather than the outdated global assertion that no ImuA activity has been characterized. No function or residue state was copied from Myxococcus.

The historical ImuB adaptor proposal remains explicitly inferential: target-specific ImuB-branch placement and native genetic cooperation are combined with mycobacterial and Myxococcus interaction evidence. Exact Caulobacter partners, stoichiometry, oligomeric state, clamp-binding motif and polymerase-inactive catalytic configuration have not been independently mapped. No DNA binding is transferred from a Myxococcus ImuB truncation.

DNA-repair explanations were corrected: current GO:0006281 includes bypass, so the old equation of repair with lesion excision was misleading. Specific TLS refinements remain, with no false is_a relationship asserted. The broad DnaE2 polymerase quote now contains catalytic reaction text rather than only a Rhea identifier. Full-text-unavailable metadata is explicit for the abstract-only PMID18083815 evidence; other cited papers were inspected in cached full text.

The three genuine Falcon requests failed with HTTP403 authentication. No provider report was fabricated. This panel has no IBA rows, so no PAINT lineage assertion is introduced. ImuA lacks a PANTHER assignment in the frozen record; this is a selector/phylogeny gap, not a reason to guess the Pseudomonas family. The new 2026 polymerase survey DOI10.1093/nar/gkag133 was flagged to the parent for family review, without changing families here.

Three focused validations pass with zero curation warnings. Three renders/content checks and three generated history checks pass. Standard record-section backfill added one field without unmatched/ambiguous quotes. The preservation checker is Ruff-clean and verifies the scientific boundaries above against exact GO responses, all original payloads and ten protected sources (six raw files and four publications).

Reproduce with `uv run python analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/caulobacter-consultation/verify.py`. Exact handoff hashes are in `.cache/module-audit-logs/imuabc-20261107/caulobacter-consultation/handoff.json`. Module, project, family and shared source files were not edited; no commit, push or full validation was performed.
