# ADP1 Lol panel consultation

The four ACIAD reviews are COMPLETE: Q6F8G3/lolA (ACIAD2937), Q6F8J1/lolB (ACIAD2902), A0ACM8PZZ0/lolC (ACIAD2641, functionally LolF), and Q9EYM2/lolD (ACIAD2640), all taxon 62977. All 16 seeded annotation payloads remain exact and ordered. Three independent molecular-function rows are added from target-specific PMID:42736309 evidence: LolA carrier activity and LolF/LolD contributions to lipoprotein release. No biological-process proposal, retirement, qualifier rewrite or guessed accession was introduced.

## Direct versus inferred coverage

PMID:42736309 was read in full. Native ADP1 chromosomal LolD tagging and purification, structural LolDF/LolA complexes, conditional silencing/complementation, ATPase-active-site controls, and detergent-purified BamE handover are kept distinct. LolA is the A. baylyi protein expressed in E. coli, not an E. coli donor inference. The direct single-cycle assay does not demonstrate a complete native outer-membrane delivery cycle, uniform kinetics for all lipoproteins, or delivery by ADP1 LolB.

LolB's terminal insertion role remains an ortholog inference supported by TIGR00548/IPR004565, signal/lipid features and the positive E. coli study PMID:9384574 (protected abstract-only cache). The target's ARBA-only prose is not independent support. Its protein-transport row is refined to lipoprotein transport, with the existing LolB insertion concept represented as an NTR core. No native LolB essentiality, depletion, localization experiment or target insertion assay is asserted. The module may therefore carry a matched ADP1 protein panel, but should not label every component or the full delivery route directly assayed.

## Identity, architecture and source corrections

Reproducible check_identity.py establishes that A0ACM8PZZ0 and active older Q9EYM3 have identical 411-residue sequences. All three source-deposited LolF entities match positions 1–410. The LolD deposited entities match Q9EYM2 positions 3–226. The 202-residue LolA entity matches Q6F8G3 positions 29–230, while the paper's methods name 29–231; this endpoint discrepancy is documented rather than silently repaired. All tested catalytic/coupling positions used in interpretation agree with the current native sequences. No sequence/version or source record was rewritten.

The direct architecture is a LolF membrane homodimer coupled to two LolD ATPase subunits. It does not require distinct LolC and LolE membrane paralogs. The gene folder and seeded symbol remain lolC because that is the verified genome record. PTHR30489:SF0 contains related membrane roles and cannot distinguish them by label alone. LolD is PTHR42798:SF2, not PTHR24220. LolA is PTHR35869:SF1; specific direct target evidence is stronger than any uncertain universal family carrier scope. LolB has no PANTHER assignment in its source record.

A structured UniProt WRONG_STATEMENT defect on Q9EYM2 records the specific CC:SUBUNIT claim that its partners are distinct LolC and LolE proteins. Native target structures contradict that architecture while confirming the LolD ATPase assignment. The original UniProt bytes are preserved; no upstream report was sent.

## Limits that the module and capacity checks must retain

* Only one LolA is observed bound to the LolDF dimer; two identical LolF protomers do not demonstrate two-carrier occupancy.
* The copurified endogenous lipoprotein-like substrate is not uniquely identified. Short-entity naming in the PDB must not be promoted to definitive native cargo identity. Defined BamE is a separate experimental substrate.
* Charge substitutions test BamE binding/extraction. Their results do not establish a universal exclusion of all clients carrying a positive residue at +3, or a universal sorting rule for every protein.
* Lnt repression/viability and structural accommodation support acyl-state tolerance as a mechanistic interpretation, not direct chemically defined transport measurements of every diacylated lipoprotein. The full paper distinguishes viable cells with envelope defects from wild-type physiology.
* LolD enables ATP hydrolysis; the intact LolDF assembly performs complete lipoprotein recognition/release. LolF and LolD contribute distinct coupled functions. The specific release GO term remains appropriate for the homodimeric architecture despite naming canonical LolCDE in its definition.

## Validation and acquisition

All four focused gene validations pass without warnings. Record-section backfill changes zero files and finds no unresolved quotes. Four renders and four scaffold-generated append-only histories are validated. Ruff passes for the identity and preservation checkers. The strict preservation checker verifies the original ordered payloads, exactly the three evidence-qualified new MF rows, zero new BP rows, 16 corruption-detection mutations, seven exact deposited entity matches, immutable source hashes, and the unchanged frozen PSEPK handoff.

All four genuine Falcon attempts returned exit 1 with HTTP 403 authentication failure. Exact logs are archived; no provider report was fabricated. PAINT-loss tools cannot resolve these target lineages because LolB lacks a family entry and the other targets are absent from cached trees. No absence-of-loss claim, source-count argument or unsupported PAINT-node adjudication is made. No full-corpus run, module/family/project edit, commit or push is included.
