# groS manual review notes

- Deep research and FEBA fitness summaries were unavailable for this review; the synthesis below is based on the cached UniProtKB record and the cached publications cited by the seeded GOA rows.
- GroES/GroS is the heptameric co-chaperonin lid of the GroEL-GroES machine. GroEL binds unfolded proteins and ATP, whereas GroES binds GroEL's apical domains to cap the cis chamber and enable productive folding. The GroES folding, chaperone-binding, GroEL-GroES complex, and cytosolic localization rows are accepted.
- Every GO:0005515 row in the stub names GroEL as the interacting partner. Structural, cryo-EM, atomic-force, NMR, and single-molecule studies all assay the GroEL-GroES machine, so these rows are modified to GO:0051087 protein-folding chaperone binding rather than retained as generic protein binding.
- The IEA ATP-binding row is removed: GroES regulates ATP-dependent chaperonin cycling by capping GroEL, but the ATP/ADP nucleotide sites are in GroEL rings. The broad PAINT metal-ion-binding row is also removed; it was placed at the root of the GroES family from a single mycobacterial descendant and is not supported for E. coli GroES.
- Identical-protein-binding rows are kept as non-core because the GroES heptameric ring is essential architecture but not the terminal activity that the annotation should surface as the protein's core function.
- GroES is retained as a host factor for bacteriophage morphogenesis; that activity is real but contextual, so the phage virion-assembly process is non-core relative to the GroEL/GroES chaperonin cycle.


## 2026-11-07 UTC — comparative GroEL-system evidence audit

Retained real GroES folding-cofactor activity under current GO0044183 (binding protein or protein-containing complex to assist folding); core contributes to ATP-dependent folding without assigning autonomous GroES ATPase. Functional heptamerization is ACCEPT, not peripheral merely because it is structural. Cytoplasm refines to existing cytosol. ATP REMOVE is now grounded in PMID7867782 direct negative calorimetry/equilibrium experiments and nonspecific photolabel controls, while retaining the conflicting 1993 positive report. Metal binding is KEEP_AS_NON_CORE: ancestral PAINT support is corroborated by PMID12837792 E. coli GroES calcium-responsive oligomerization. Its 20 mM CaCl2 DLS measurement and proposed Glu53 site are not direct site occupancy, affinity or physiological calcium regulation. Earlier donor-count/missing-site rejection is superseded. Scoped primary excerpt records source and assay limits.

All original ordered annotation payloads, historical NEW actions and protected source/provider bytes were retained. No NEW rows were added. Existing provider research was used as a lead, with primary/curated evidence checked independently. A genuine default Falcon attempt failed with403 authentication; no provider report was fabricated. PAINT-loss check completed: no IRD/IKR found on the mapped target lineage.

Current actions: 16 ACCEPT, 2 KEEP_AS_NON_CORE, 17 MODIFY, 1 REMOVE. Status COMPLETE reflects completed adjudication, including explicit uncertainty, not proof of every tested proposition. Focused validation/render/history results and source preservation are recorded in the existing-member consultation proof.


## PR6164 review follow-up, 2026-11-07

Independently reconsidered review5809803940 using original PMID12198306, biochemical lower-oligomer evidence in PMID15327959, current GO definitions and full publisher PMID12837792 Methods/Table2. [Activity evidence](../../../analysis/module_audits/bacterial_groel_groes_chaperonin_folding/round1-activity-consultation/evidence.md) records the judgment. GroEL2 self-binding is refined to identical protein binding; its broad folding-chaperone row explicitly covers the non-ATP mode. E. coli GroES metal binding is marked over-annotated because DLS assembly effects and a proposed site do not establish direct target coordination, even with a valid ancestral source. This supersedes the earlier inference that the DLS response sufficiently justified KEEP_AS_NON_CORE. Neither high calcium alone nor short donor lists is used as a refutation. Original payloads and sources are preserved.
