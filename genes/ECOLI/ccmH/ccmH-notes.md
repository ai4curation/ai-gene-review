# ccmH (P0ABM9, b2194) notes

## Deep research status
- 2026-10-23: `just deep-research-falcon ECOLI ccmH` was attempted and failed with
  `Exception: Failed to authenticate`; no other provider credentials were available.
  Review based on cached publications and the UniProt record.

## Biology
- Domain architecture (UniProt P0ABM9): signal/N-terminal periplasmic CcmH/CycL/NrfF
  domain with RCPKC motif (residues ~43-46), two TM helices, C-terminal periplasmic TPR
  domain homologous to CcmI/CycH (fusion of CcmH and CcmI-like domains).
- Only the N-terminal CXXC domain is required in E. coli
  [PMID:9914305 "This confirmed that only the N-terminal domain containing a conserved CXXC motif is required in E. coli."]
- Null mutant lacks all c-type cytochromes
  [PMID:9914305 "A mutant in which the entire ccmH gene was deleted failed to synthesize both indigenous and foreign c-type cytochromes."]
- Thiol rescue of cysteine mutants; proposed reducing role
  [PMID:9914305 "We propose a model for the reaction sequence in which CcmH keeps the heme binding site of apocytochrome c in a reduced form for subsequent heme ligation."]
- CcmF-CcmH complex = heme lyase
  [PMID:11744735 "We propose that CcmFH forms a bacterial heme lyase complex for the transfer of heme from CcmE to apocytochrome c."]
  [PMID:19629033 "showing that CcmF, CcmH and haem all co-purify as a complex"]
- R. capsulatus ortholog: CcmH forms a mixed disulfide with apocytochrome c resolved by CcmG
  [PMID:28634234 "We conclude that CcmG confers efficiency, and CcmH ensures stereo-specificity during Ccm"]

## Curation decisions
- protein binding (IPI x2, CcmF): REMOVE per protein-binding policy; complex captured as
  contributes_to GO:0004408 in core function (complex-level activity, not assigned to CcmH alone).
- GO:0015035 (ISM): ACCEPT as subunit-level redox activity.
- GO:0017004 rows: MODIFY -> GO:0018063 cytochrome c-heme linkage (is_a descendant of GO:0017004).
- membrane (ARBA IEA): MODIFY -> plasma membrane.
- Fetched PMID:7635817 (UniProt RX) for context.


## 2026-11-06 system I comparative reassessment

Contributes thiol-disulfide substrate handling to the CcmF-associated heme-ligation machinery. The E. coli evidence is distinguished from heterologous ortholog assays and engineered expression constructs.

Specific reassessment: Contributes thiol-disulfide substrate handling to the CcmF-associated heme-ligation machinery. Net reductase chemistry and the exact cysteine-substrate relay remain unresolved for this protein.

PMID:9914305 mutant/thiol-rescue evidence supports redox involvement; PMID:24397552 supports synthase contribution in engineered E. coli CcmFGH-only. PMID:28634234 assigns direct reduction to R. capsulatus CcmG and stereospecific mixed-disulfide chemistry to CcmH, so a net CcmH reductase reaction remains unresolved.

Default Falcon was genuinely attempted and failed with HTTP403 authentication; no provider report was created. Manual literature assessment is recorded here. Original seed rows (including inherited NEW), raw UniProt/GOA, and existing provider files are preserved against original-members-baseline.json. Focused validation and helper history are recorded in the original-panel audit ledger.


## 2026-11-06: PR6121 round-2 location-evidence audit

Replaced chemistry-only support on location rows 7 and added matching locational evidence to location-bearing cores. The curated E. coli CcmH record assigns an integral inner-membrane topology, independently corroborated by the primary periplasmic-domain mapping. CcmFH synthesis activity alone would not establish this location. Annotation actions and every original non-review payload, including historical NEW rows, remain unchanged. Full prior reviews and source hashes were frozen before editing in the round2-location cache; the durable preservation proof records comparison to published head 044f9278bcea364ad66bccc221fdfc78132ba4eb.
