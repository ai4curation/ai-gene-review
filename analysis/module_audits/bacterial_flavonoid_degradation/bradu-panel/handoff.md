# BRADU panel handoff

Seven COMPLETE USDA110 reviews; all eleven original rows remain in order with exact machine payloads. One new ISS molecular-function row (bll6427 GO0016702); no NEW biological-process rows. Fourteen raw UniProt/GOA files unchanged. Seven genuine Falcon requests failed403; no provider report was created. No existing publication was changed and no publication was acquired by this worker.

All seven focused gene validations, reference validations, history validations and renders passed. The two no-core advisories for bll6421/FdeJ and bll6423/FdeH are intentional: family/domain membership does not establish their molecular work. Record-section check is clean. Scripts pass Ruff; frozen-sequence comparison reproduced for all seven. Reference validator skips local-source snippets; those are checked by the local-source validation within normal gene validation.

Scientific boundaries: E supports NAD(P)H-dependent monooxygenase class, not naringenin/isoflavone specificity. D supports Rieske binding, not an obligatory E partner. C supports qualified FdeC-derived dioxygenase inference while glyoxalase-I substrate specificity remains unresolved; unlike HERSS glyoxalase-II, it is not a wrong-fold case. B supports broad hydrolysis; ester specificity unresolved and peptide/proteolysis claims over-annotated. I supports catalytic activity only. H/J have no assigned core. USDA110 related operon was explicitly uncharacterized in2013.

New family consideration: bll6427 Q89GB8 is officially PTHR21366:SF14 / GLYOXALASE DOMAIN-CONTAINING PROTEIN 5, distinct from the HERSS FdeC record lacking a PANTHER classification. No family files were changed.

Ownership released: seven BRADU directories, seven helper-generated histories, and this scoped audit directory only. No commits, staging, full-corpus run, module/project edits, or source refresh. history-markers.json preserves successful scaffold paths; do not blindly rerun helpers. Manifest files give the exact content and hashes.
