# SYNE3 (nesprin-3) curation notes

## 2026-09-27 — initial review (claude-code)

Sources: UniProt Q6ZMZ3, cached GOA-cited papers, additional primary papers fetched via PubMed
(PMID:17881500, 23761073, 25170155, 31822208), and `SYNE3-deep-research-falcon.md` (retrieval support only;
claims checked against primary papers).

### Biology
- Nesprin-3 is a ~110 kDa ONM KASH protein lacking the CH actin-binding domain of nesprin-1/-2; its N-terminus
  binds the plectin actin-binding domain [PMID:16330710 "We have now isolated a third member of the nesprin family
  that lacks an ABD and instead binds to the plakin family member plectin, which can associate with the
  intermediate filament (IF) system."].
- KASH-SUN binding retains it at the NE [PMID:17881500 "the last four amino acids of the nesprin-3alpha KASH domain
  are essential for its interaction with Sun1 and Sun2."]; KASH3 binds SUN1/SUN2 promiscuously [PMID:18396275];
  SUN2-KASH3 crystal structure [PMID:33058875].
- Human aortic endothelial cells: NE localization, knockdown -> elongation, loss of perinuclear plectin/vimentin,
  MTOC detachment, loss of flow-induced polarization [PMID:21937718 "We propose that nesprin-3 provides a scaffold
  for plectin perinuclear organization and that nesprin-3 contributes to the connection between the nucleus and the
  centrosome."].
- Mouse KO: required for perinuclear plectin/vimentin in Sertoli cells but fertile; not needed for 2D MEF migration
  [PMID:23761073 "Furthermore, nesprin-3 was not required for the polarization and migration of mouse embryonic
  fibroblasts."].
- 3D migration nuclear piston in human fibroblasts [PMID:25170155 "Thus, nesprin 3 is required for piston-like
  nuclear movements and pressurizing lobopodial protrusions."].
- Rat cardiomyocytes: desmin-nesprin-3 tether resists microtubule-driven nuclear infolding [PMID:31822208].
- F-actin co-sedimentation of an N-terminal SR fragment in vitro [PMID:22518138] — physiological relevance unclear;
  contrasts with [PMID:18827015 "nesprin-3 lacks an actin-binding domain (ABD) and is therefore unable to associate
  with actin directly"].

### Decisions
- GO:0140444 (anchor activity) = core MF; SUN-partner protein-binding rows MODIFY -> GO:0140444 (as in SUN1/SUN2).
- TOR1A and nesprin-1 protein-binding rows REMOVE (uninformative).
- GO:0034993 (meiotic) -> MODIFY to GO:0106094, consistent with SUN1/SUN2/SYNE1/SYNE2.
- GO:0007010 -> MODIFY to GO:0045104 (phenotype is IF-specific; actin/MT unaffected).
- GO:0090150 -> MODIFY to GO:0090435 protein localization to nuclear envelope (recruits vimentin/plectin to NE).
- Rough ER (IEA, by similarity) MARK_AS_OVER_ANNOTATED: ER pool reflects SUN-binding loss / overexpression.
- Actin filament binding (IMP, IBA) KEEP_AS_NON_CORE.
- No NEW annotations.

### For the LINC module
- MF GO:0140444; location GO:0005640; complex GO:0106094; cytoskeletal partner = plectin (plakin) -> intermediate
  filaments (keratin, vimentin, desmin); broadly expressed (endothelium, fibroblasts, keratinocytes, Sertoli cells,
  cardiomyocytes). Knockout mice have no gross phenotype.
