# MesD/MesX and MesB gene consultation

Three normally seeded reviews are COMPLETE: ACIAD/ACIAD3523 (MesD, Q6F6Z8), ACIAD/ACIAD3524 (MesX, Q6F6Z7), and DEHMC/cbdbA481 (MesB, A0A916P3S8). The original two ordered annotation payloads belong to MesD. MesX and MesB had zero-row seeds. `baseline.json` captures the root seed receipts before any edits and protects all six raw gene files plus four full publication caches.

## Decisions and evidence scope

MesD GO0003871 is MODIFY to GO0008172, preserving sulfur methyl transfer while removing the unsupported canonical folate-triglutamate donor. Exact ADP1 native genetics in PMID18319726/18840283 and the exact MesD identity/domain analysis in PMID33534785 support this interpretation. The catalytic zinc-binding row is ACCEPT as an explicitly inferred conserved feature; no native occupancy assay is claimed. The oxygen and MetF-independent complementation experiments used S. koreensis genes in E. coli, and are distinguished from native ADP1 genetics. The physiological donor is unresolved.

MesX remains a zero-row review. ADP1 deletion/rescue establishes necessity, while PMID:33534785 explicitly frames donor provision and oxidative chemistry as hypotheses. There is no demonstrated independent MF or stable-complex contribution to encode. Core functions are therefore omitted deliberately. No NEW process annotation is manufactured from necessity. Official raw identifiers IPR015004 and PF08908 establish MesX family membership; no PANTHER identifier is present. A module may represent the experimentally required partner context without asserting an invented molecular activity.

MesB gains one IDA NEW GO0008172 from the controlled purified assay in PMID32034217. The primary identifies cbdbA481/CAI82680 and 343 residues, matching current A0A916P3S8/CAI82680.1. The functional preparation was untagged recombinant enzyme, not the initial problematic tagged construct. Enzyme/substrate omission and crude-extract controls were negative; methionine formation was verified by LC-MS. Assays were anoxic and used free methylcobalamin. The folate-triglutamate reaction was negative with a canonical MetE positive control. Native AcsCD/CoFeSP transfer remains a hypothesis, and failed E. coli complementation is not converted into a denial of directly measured chemistry. No native complete-cycle flux is asserted.

Current QuickGO definitions, a methylcobalamin term search and all 12 direct GO0008172 children are archived. None supplies the measured methylcobalamin-to-homocysteine reaction; existing donor-specific children require other donors or acceptors. GO0008172 is an accurate genus, with exact chemistry retained in the core description and an ontology question. No redundant broad MF or process NEW is added.

## Source and validation limits

All four primary papers were read in full from genuine existing caches. Reference assessments distinguish direct target assays, native genetic phenotypes, comparative complementation, structural inference and explicit author hypotheses. All exact quoted findings and supporting evidence are checked against their sources by `check_preservation.py`, including publication titles. No cached publication, UniProt, GOA or provider file was rewritten.

All three genuine Falcon commands failed with HTTP 403 authentication/access errors. Exact logs are archived; no provider report was fabricated. Manual notes describe the fallback primary-source review.

Focused validation, standard record-section backfill, render and generated history checks pass. Three warnings are intentional: MesX has no established molecular core, and the two enzyme cores' methionine biosynthesis context has no duplicated process annotation. They are not resolved by inventing assertions. PAINT commands complete but cannot check these exact lineages: Q6F6Z8 is absent from the family tree, while MesX and current MesB records lack PANTHER identifiers. A tool footer saying no loss is not taken as a negative-loss finding when its own preceding message says the lineage was not checked.

`preservation.json` proves two source payloads/order/qualifiers/lifecycle unchanged, one new active MF proposal, no retired proposal and ten protected source files unchanged. It independently verifies all 81 files of the prior six-family frozen handoff. `recommended-psepk-zinc-followup.json` is a proposed additive correction for the previously released PSEPK review; that file has not been edited here.

The frozen handoff contains exact hashes of these three reviews, notes, HTML renders, generated histories and scoped consultation artifacts. It does not claim full-corpus validation or publication.
