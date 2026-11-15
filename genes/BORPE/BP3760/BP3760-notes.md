# BORPE BP3760 annotation review

2026-11-07. Complete manual review of 2 seeded rows; source payload/order/qualifiers preserved. No NEW rows were added, including for zero-row proteins. Core functions independently synthesize the supported biology.

BP3760 is an MlaA-family lipoprotein of Bordetella pertussis. It is predicted to act at the outer membrane, helping transfer misplaced phospholipids to the periplasmic MlaC carrier for return through the Mla system. Its MlaA domain and lipoprotein signal support this role, while the cognate porin partner and target-specific transfer kinetics remain unresolved.

PMID36518166 identifies BP3757–BP3761 as the MlaF/E/D/A/C locus in the Tohama I reference. The native experiments used B213, a streptomycin-resistant Tohama I derivative identified in Supplementary TableS1; complete experimental B213 protein sequences were not independently compared. Only MlaF was directly perturbed in this operon, and the clearest surface-PE defect involves combined mlaF/pldA loss. The source therefore supports a lineage-qualified Mla pathway, not five separate target assays or a measured native transport direction.

The standard E. coli MlaFEDB composition is not imported into Bordetella: PMID36518166 found no identifiable MlaB homolog. In particular, the automatic MlaFEDB stoichiometry in BP3758 UniProt is not target-specific support.

Contributes the outer-membrane lipid extraction/loading interface of the Mla pathway. Specific MlaA architecture, a lipidated signal-peptide cleavage product and the cognate Mla locus support this role; the exact Bordetella porin partner and native direction were not measured.

Sources and identity proof: `analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/new-member-consultation/evidence.md`, frozen `preflight/identity-proof.json`, current immutable UniProt record and the cited primary full texts. Official GO definitions were checked in `go-terms.json`.

A genuine `just deep-research BORPE BP3760 --provider falcon` attempt failed with403 authentication/access error. The exact failed attempt is archived in this consultation; no provider report was invented. Manual review proceeded from primary evidence.

PAINT-losses was run. Bordetella targets are absent from the cached reference trees, so the report cannot establish absence of ancestral loss; no imaginary target placement or loss node is asserted. PAO1 Ttg2D reports no applicable loss. Two first attempts raced the shared IBD download and were rerun sequentially after completion, with both attempts retained. TreeGrafter row nodes identify source ancestry, not donor-count or self-citation defects.

No universal essentiality, exact native stoichiometry, antibiotic transport or assay-derived native directional flux is inferred from growth/permeability phenotypes. See core descriptions for measured binding versus inferred transfer.


## PR6198 evidence follow-up (2026-11-07)

Replaced generic summaries and downgraded method-only GO_REF relevance; added exact target feature/signature quotations without changing source rows, actions or evidence tiers. Corrected all four PG/PE cargo quotations to the actual E. coli MlaA-assisted MlaC loading sentence; target localization/participation remains inferred from specific architecture and locus, not directly assayed. The earlier no-NEW tally is historical, not a policy barring evidence-supported additions. Prior receipts and provider attempts remain unchanged; the additive consultation records the new decisions.
