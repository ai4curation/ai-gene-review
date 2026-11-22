# unc-84 (C. elegans) review notes

## Session 1 (2026-09-27, claude-code)

Context: reviewed as the C. elegans SUN member of `modules/linc_complex.yaml` and as a candidate
variant of `modules/nucleokinesis.yaml` (P-cell / hyp7 nuclear migration).

### Identity
- Q20745, UNC84_CAEEL, 1111 aa, isoforms a (long) and b (short). PANTHER PTHR12911:SF8
  ("KLAROID PROTEIN-RELATED", the subfamily containing Drosophila Koi), not SF2 (SUN1-like,
  which contains worm SUN-1). Type II INM protein: nucleoplasmic N-terminus (~59 kDa), TM at
  512-532, luminal C-terminus with SUN domain [PMID:21411627 "UNC-84 has the largest predicted
  nucleoplasmic (59 kDa) and lumenal (65 kDa) domains of any known endogenous INM protein"].

### Function (with provenance)
- Required for two developmental nuclear migrations (hyp7 precursors, P cells) and for nuclear
  anchorage in hyp7; alleles define separable migration and anchorage functions
  [PMID:10375507 "Both functions are required for nuclear and distal tip cell migrations, but only one is required for nuclear anchorage."].
- SUN domain binds UNC-83 KASH and recruits it to the ONM
  [PMID:11748140 "UNC-83 interacted with the SUN domain of UNC-84 in vitro"];
  [PMID:16481402 "At least two separable portions of the C-terminal half of UNC-84 were found to interact with the UNC-83 KASH domain"].
- UNC-83 then recruits dynein and kinesin-1 [PMID:27697906 "The LINC complex, consisting of the SUN protein UNC-84 and the KASH protein UNC-83, recruits dynein and kinesin-1 to the nuclear surface."].
- Nucleoplasmic domain binds LMN-1; P91S weakens binding and gives intermediate migration defect
  [PMID:25057012 "interacts with the nucleoplasmic domain of the SUN protein UNC-84"].
- Lamin-dependent NE localization; not required for centrosome-nucleus attachment
  [PMID:11907270 "UNC-84 is not required for centrosome attachment to the nucleus"].
- INM targeting uses redundant cNLS, INM-SM and SUN-NELS signals [PMID:21411627].
- Germline: UNC-84 SUN domain and ZYG-12 KASH peptide coelute; UNC-84 promotes cross-link repair,
  limits NHEJ, recruits FAN-1 [PMID:27956467 "UNC-84 interacts with the KASH protein ZYG-12 for DNA damage repair."].
- Egl/Unc phenotypes are secondary to P-cell death [PMID:27697906 "Failure of P-cell nuclear migration results in P-cell death and in turn, Egl (egg laying deficient) and Unc (uncoordinated) animals due to the lack of vulval cells and motor neurons, respectively"].

### Decisions
- protein binding (UNC-83) x2 -> MODIFY to GO:0140444 (consistent with human SUN1/SUN2).
- GO:0034993 meiotic complex (IBA, IPI) -> MODIFY to GO:0106094: UNC-84 complexes are somatic;
  worm meiotic telomere tethering uses SUN-1/ZYG-12.
- cytoskeleton (IEA from UniProt ECO:0000305 SubCell) -> REMOVE; INM protein with no cytoplasmic domain.
- locomotion, egg-laying -> MARK_AS_OVER_ANNOTATED (secondary to P-cell death).
- nervous system development, post-embryonic, vulval development -> KEEP_AS_NON_CORE.
- regulation of cell migration (TAS, 1987 review) -> MARK_AS_OVER_ANNOTATED.
- NEW GO:0051647 nucleus localization (anchorage), following fly Koi/Msp300/Klar and worm ANC-1 convention.

### Module implications
- UNC-84 is the canonical somatic SUN: KASH anchor (GO:0140444) + lamin binding (GO:0005521), as
  for human SUN1/SUN2. It partners with two KASH proteins that couple to different cytoskeletal
  systems (UNC-83: microtubule motors; ANC-1: actin/ER), the same "one SUN, several KASH" logic as
  the human module.
- Meiotic complex term is not appropriate for UNC-84; supports the module's GO:0106094 choice.
- The UNC-84/UNC-83 system is the best-characterised non-mammalian nucleokinesis variant (dynein
  primary in P cells, kinesin-1 primary in embryonic hyp7).

### Deep research
- Falcon deep research not present at time of review (checked); review built from UniProt and cached publications.

### Deep research (update, same session)
- `unc-84-deep-research-falcon.md` appeared during the session and was read. It agrees with the
  review: somatic SUN protein distinct from SUN-1; UNC-83 for movement, ANC-1 for anchorage
  [file:worm/unc-84/unc-84-deep-research-falcon.md "Thus, the same SUN protein supports two separable outputs by selecting different KASH partners: UNC-83 for movement and ANC-1 for anchorage."].
- Adds the C953A SUN-KASH disulfide-cysteine mutant, which impairs anchorage more than migration
  (Cain et al. 2018, not cached here; used only as retrieval support in core function 3).
- Treats the DNA-repair role as secondary, matching the decision not to add a DNA-repair term.
- Mentions body-wall muscle nuclear envelope spacing defects in unc-84 nulls (Cain et al. 2014, not cached).
