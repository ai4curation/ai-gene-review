# BicD (Drosophila melanogaster, P16568) - curation notes

## 2026-09-27 session (claude-code)

Sources: UniProt P16568, GOA seed (39 rows), cached publications; Falcon deep research not yet available at time of writing.

### Biology summary
- BicD is a dimeric coiled-coil dynein activating adaptor [PMID:38264934 "In the dynein-dynactin-Bicaudal-D transport machinery, Bicaudal-D (BicD) links the cargo to the motor"].
- Egl + BicD are the minimal RNA-motor link; RNA licenses BicD to recruit dynein-dynactin [PMID:29944118 "A Bicaudal-D (BicD) adaptor protein and the RNA-binding protein Egalitarian (Egl) are sufficient for long-distance mRNA transport by the dynein motor and its accessory complex dynactin"; "The hairy RNA significantly increased the number of processive movements of dynein in the presence of dynactin and Egl/DmBicD"]. Drosophila BicD itself (DmBicD) was assayed, not only mouse BICD2.
- Autoinhibition relieved by cargo [PMID:32378283 "The dynein adaptor Drosophila Bicaudal D (BicD) is auto-inhibited and activates dynein motility only after cargo is bound"].
- Egl, not BicD, binds the RNA [PMID:19515976 "despite lacking a canonical RNA-binding motif, Egl directly recognizes active localization elements"] -> supports the NOT mRNA binding row.
- Cargo partners: Rab6/Rab2/Rab30/Rab39 GTP-dependent [PMID:25453831], Chc direct [PMID:20111007 "BicD binds Chc directly"].
- Synapse: kinetic role in SV recycling, not obligatory for endocytosis/exocytosis [PMID:20111007 "Collectively, these observations provide further evidence that there is not an obligatory requirement for BicD in endocytosis or exocytosis"].
- Photoreceptor nuclear migration [PMID:15582780 "Msn, like Bic-D, is required for the apical migration of differentiating R-cell precursor nuclei"] (abstract only); nervous system nuclear localization [PMID:10559989].
- Bristles, redundant with BicDR [PMID:38264934].

### Decisions
- protein binding x2 -> MODIFY to small GTPase binding (Rab6) and clathrin heavy chain binding (Chc).
- GO:0140312 cargo adaptor activity -> MODIFY to GO:0008093; 0140312 is defined as a vesicle-coat (clathrin/COPII) adaptor.
- GO:0048488 SV endocytosis -> MODIFY to GO:0036465 synaptic vesicle recycling (authors: not required for budding/uncoating).
- GO:0050658 RNA transport -> MODIFY to GO:0051028 mRNA transport.
- GO:0007312 oocyte nucleus migration (TAS, PMID:9642168 review on mRNA stability) -> UNDECIDED; same review also backs an egl TAS; only a tethering hypothesis found [PMID:10825285].
- Developmental outcomes (oocyte fate, egg chamber formation, oogenesis, chaeta development, MT polarization) -> KEEP_AS_NON_CORE.
- NEW: GO:0140660 cytoskeletal motor activator activity (IDA, PMID:29944118); GO:0007097 nuclear migration (IMP, PMID:15582780). Comparator: Dhc64C has nuclear migration (IBA); human BICD2 has both as NEW.

### Module relevance (nucleokinesis)
- Conserved: dynein adaptor + activator (GO:0008093/GO:0140660) as in BICD2; Rab6 Golgi cargo.
- Fly-specific emphasis: Egl-mediated mRNA cargo; the nuclear cargo link used by BICD2 (RANBP2, nesprin-2) is not established for fly BicD in R-cell nuclear migration.

### Publications added
PMID:29944118, PMID:19515976, PMID:32378283, PMID:15582780, PMID:10825285, PMID:8951073 (all PubMed-verified via eutils before fetch).
