# BST2 (tetherin/CD317) review notes

Deep research not run (providers unavailable); research from cached publications and UniProt.

- Antiviral tether: two membrane anchors (TM + GPI), disulfide-linked coiled-coil homodimer [PMID:20399176 "The restriction factor BST-2/tetherin contains two membrane anchors employed to retain some enveloped viruses, including HIV-1 tethered to the plasma membrane"]; directly tethers virions [PMID:19879838 "Tetherin inhibits HIV-1 release by directly tethering virions to cells"].
- Added NEW GO:0044790 suppression of viral release by host (BST2 performs the tethering work).
- MT1-MMP (MMP14) inhibitor [PMID:22065321 "binding to cellular MT1-MMP on its C-terminus and inhibiting its proteolytic activity"] -> metalloendopeptidase inhibitor activity ACCEPT.
- ILT7 ligand on pDC [PMID:19564354].
- Localization: PM, cell surface (ectodomain+GPI exposed), apical PM, lipid raft, TGN/Golgi; endosome/MVB (endocytosed virions) non-core. Surface-exposed restriction factor.
- RNA binding (HDA) over-annotated; protein binding removed; self-interaction -> homodimerization.

## 2026-11-13 ORGANELLES Golgi batch 1 (Golgi apparatus rows)

- Rows: GO:0005794 IDA GO_REF:0000052 (HPA) and IEA GO_REF:0000044 (SL-0132), both ACCEPT before. No Golgi sub-compartment rows.
- UniProt location: "Golgi apparatus, trans-Golgi network" (untagged in the main block; ECO:0000269 PubMed:26172439 in the microbial-infection block), with the note that BST2 shuttles between the cell membrane and the TGN. The IEA mapped this to the root (SL-0132), losing the TGN.
- Evidence for the TGN: [PMID:19244337 "Tetherin localized predominantly within cytoplasmic structures that corresponded at least in part to the TGN"] with TGN46 co-stain, native tetherin in HeLa (cells transfected with a Vpu-encoding provirus); [PMID:17940069 "these data indicate that CD317 is internalised and delivered back to the TGN by the sequential action of AP2 and AP1 adaptor complexes"] (abstract only; uninfected recycling); PMID:20419159 shows TGN46-positive accumulation only in Vpu-expressing cells (control cells: plasma membrane plus CD63 endosomes).
- Outcome: both GO:0005794 rows ACCEPT -> KEEP_AS_NON_CORE (real recycling location, but tethering and MT1-MMP inhibition act at the plasma membrane; Golgi is not in core_functions; consistent with endosome/MVB rows). NEW GO:0005802 trans-Golgi network (IC, PMID:19244337) added beside the root rows. The GO:0016020 HDA row was already MODIFY to plasma membrane; GO:0005802 is not a membrane term, so it is unchanged. Added PMID:17940069 and PMID:19244337 to references.
- Caveat: the TGN46 co-stain is in Vpu-transfected cells; the AP1-dependent return is the uninfected line.
