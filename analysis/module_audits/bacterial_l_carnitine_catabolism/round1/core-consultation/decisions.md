# PR6182 round1 core and lifecycle consultation

The review's two redundancy findings are valid. The historical bcoG GO:0016747
proposal duplicates the existing GO:0043720 MODIFY replacement; the historical
bcoE-bcoF GO:0042413 proposal duplicates the existing GO:0009437 refinement.
Only their annotation-level `retired` flags are added. Their original source
payloads, ordered presence and NEW actions remain unchanged. The reasons identify
curator retirement for redundancy, not upstream GOA disappearance or withdrawal
of supported chemistry. The already-retired bcoG IMP proposal is unchanged.

PP_0303 now uses `proposed_molecular_function` with the exact existing name
`3-dehydrocarnitine:acetyl-CoA trimethylamine transferase activity`. Its existing
supporting evidence and proposed term are unchanged. Adding a generic MF NEW row
would be unnecessary here. The target BKACE511 screen and unresolved processed
KAH threshold still warrant UNDECIDED on GO:0043720. Neither screening signals nor
ortholog chemistry is converted into a demonstrated native KT2440 phenotype.

The optional NAD+ binding consistency finding is also valid: bcoE-bcoF changes
GO:0070403 from KEEP_AS_NON_CORE to ACCEPT. The full PMID30670548 Results section
"Smc01638 is a trifunctional enzyme (CDH thioesterase)" explicitly monitors NADH
formation and reports the NAD+ kinetic parameter in Table 1. NAD+ is the redox
cofactor, so binding is central to this supported chemistry even though the
catalytic reaction has a separate term. This is not an autonomous second reaction
or a new annotation. The frozen publication-linked UniProt kinetic statement
provides the row's precise quotation; the full primary was re-read independently.

GO:0045329 remains an existing MODIFY replacement and core process. The definition
in the frozen QuickGO response covers formation of carnitine. The primary directly
measures carnitinyl-CoA hydrolysis, and the reconstructed pathway supplies that
substrate. The added clause makes explicit that carnitine is a transient product
within GBB utilization, not a claim of mammalian BBOX-type hydroxylation.

Primary scope and exact 3D0a2→Rm2011→1021 protein bridges are unchanged. Intrinsic
sequence-matched enzyme chemistry is distinguished from strain-dependent GBB
utilization. No native strain 1021 growth, separate-domain necessity, substrate
channeling, or BcoG knockout is inferred. Existing genuine research/provider
artifacts were reused; no source was refreshed or invented.

Inputs consulted include the frozen primary full text at
`.cache/module-audit-logs/carnitine-20261107/rhime-consultation/primary-full.txt`,
the durable source analysis under `genes/RHIME/bcoE-bcoF/bcoE-bcoF-source-analysis/`,
the PSEPK consultation evidence and publisher-dataset mapping, and the current
schema (`retired` means retired or replaced; proposed core activities must match
a supported proposed_new_terms entry). Historical audit proofs are left intact.

There are 18 preserved rows in this scope, four historical NEW actions, and three
retired proposals after the change (one already retired, two newly retired). One
historical NEW remains active. No rows were added or removed. The reproducible
preservation checker also verifies all 63 protected source hashes captured by the
parent's published-head baseline. The parent owns overall panel counts and the
capacity checker's support for the exact proposed core activity.
