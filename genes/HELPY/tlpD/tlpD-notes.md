# tlpD / HP_0599 curation notes

## 2026-11-06 — chemotaxis taxon audit

Reviewed all three pristine GOA-derived rows for O25321 (H. pylori 26695). Accept chemotaxis IBA at PTN001280296; `just paint-losses HELPY tlpD` reports no applicable IRD/IKR. The family claim is supported by a real receptor mechanism, not judged by donor count. Refine signal transduction to the CheA-centered phosphorelay process. Refine membrane to its cytoplasmic side, reflecting real peripheral association without inventing transmembrane topology. Added signaling receptor activity, cytosol and cell pole, with explicit strain-transfer evidence. No new process claim is needed because chemotaxis and the refined phosphorelay process already cover the direct work.

Primary evidence and exact strain attribution are detailed in `tlpD-source-analysis/README.md`. PMID:31465435 was read in full: the reconstructed complex uses SS1 TlpD A0A1U9IUC7 and CheW plus G27 CheA, expressed in E. coli. G27 and PMSS1 provide native attraction assays. HOCl oxidation of C340 in the CZB domain inhibits receptor stimulation of CheA and leads to attraction. The reconstruction does not support direct pH, zinc, peroxide or superoxide sensing; those negatives do not exclude indirect stress responses in cells.

The SS1 accession has been retired from UniProt because it is not in a reference proteome, not because the protein is absent. Its linked UniParc sequence is preserved in the source analysis. Reproducible comparison finds 426/433 identical residues (98.383%) to O25321, with H315/C340/H368/H372 conserved. All seven substitutions and input hashes are recorded. This supports explicit ISS transfer, not an identical-sequence or exact-target assay claim.

PMID:18245281 and PMID:21725005 were fetched normally but remain abstract-only in the cache. The publisher full texts were inspected separately. The 2008 complementation uses KE26695-derived TlpD with a C-terminal V5 tag in N6; the 2011 sequence analysis explicitly identifies 26695 HP0599 as TlpD (also hylB/hlyB), while its zinc-binding proteins come from SS1/J99. The raw UniProt “Hemolysin secretion protein (HylB)” name is a source defect, recorded on the reference with the raw file unchanged. Its MCP/CZB domain membership remains useful evidence.

PMID:27002127 remains abstract-only after a normal forced fetch. Its abstract explicitly supports autonomous polar localization and partner-dependent membrane association; inability to retrieve full text is not used to reject those statements. PMID:41660828 is full-text peer-reviewed G27 localization evidence using tagged ectopic constructs. The discussion's AcxC/HP0599 locus mismatch is not used as evidence. PMID:41648481 is a J99 structure preprint and is contextual, not a new claim's sole support.

The full-text review PMID:38048436 reports the absence of the canonical CheR/CheB methylation adaptation pair in H. pylori. A methyl-accepting signal-domain label does not prove TlpD methylation. No specific direct metal-binding NEW was added merely to reproduce a domain label; the CZB chemistry is documented in the receptor mechanism. No target entry was found in gocams/index.tsv.

Normal Falcon attempt (`just deep-research HELPY tlpD --provider falcon`) failed HTTP403 authentication/access. No provider report was fabricated. Log: `.cache/module-audit-logs/chemotaxis-20261106/HELPY-tlpD-falcon.log`. All three original row payloads and two raw files remain intact; no inherited NEW rows existed. Status COMPLETE records completed decisions, with limits to exact strain and construct evidence explicit. Validation and preservation results are logged with the module audit.

## PR 6100 round 1 follow-up — 2026-11-06

Item 13: PMID:41648481 relevance is now MEDIUM because the J99 preprint provides comparative structural context, not decisive 26695 functional evidence. VERIFIED describes the checked source correspondence; preprint status does not by itself establish LOW_QUALITY. No annotation or core activity was added from this source.
