# RAB3IP curation notes

## 2026-10-03 — initial review (primary cilium life cycle module, stage 2 ciliary vesicle/membrane)

Human RAB3IP (Rabin8) = UniProt Q96QF0. 68 GOA annotations seeded; all reviewed.

### Deep research status

First falcon run (600 s timeout; perplexity fallback unavailable) did not complete; re-run with `--timeout 2400`
(outcome at end of file). Review based on cached primary literature.

### Biology

- Rab8-specific GEF [PMID:12221131 "stimulated nucleotide exchange on Rab8 but not on Rab3A and Rab5"; PMID:20937701
  "Sec2 domain proteins Rabin3/Rabin8 and Rabin3-like/GRAB are specific GEFs for Rab8A and Rab8B and have no activity
  toward Rab10"].
- Rab11 effector; Rab11-GTP stimulates GEF activity [PMID:20308558 "Rab11, in its GTP-bound form, interacts with Rabin8
  and kinetically stimulates the guanine nucleotide-exchange activity of Rabin8 toward Rab8"; PMID:26258637 "the
  C-terminal domain of Rabin8 adopts a previously undescribed fold that interacts with Rab11 at an unusual
  effector-binding site"].
- Preciliary trafficking to the centrosome [PMID:21273506 "Rab8-dependent ciliary assembly is initiated by the
  relocalization of Rabin8 to Rab11-positive vesicles that are transported to the centrosome"; "the transport protein
  particle (TRAPP) II complex associates with the Rabin8 NH(2)-terminal domain"; PMID:31467083 "We find that C7orf43
  directly binds to Rabin8 and that C7orf43 knockdown diminishes Rabin8 preciliary centrosome accumulation"].
- NDR2 phosphorylation switch [PMID:23435566 "NDR2 phosphorylates Rabin8 at Ser-272 and defects in this phosphorylation
  impair preciliary membrane assembly and ciliogenesis"; "Rabin8 binds to and colocalizes with GTP-bound Rab11 and
  phosphatidylserine (PS) on pericentrosomal vesicles"].
- BBSome contact [PMID:17574030 "This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which
  localizes to the basal body and contacts the BBSome"].
- GEF activity determines Rab8 membrane targeting [PMID:23382462 "Specific mistargeting of Rabex-5/DrrA/Rabin8 to
  mitochondria led to catalytic recruitment of Rab5A/Rab1A/Rab8A in a time-dependent manner that required the catalytic
  activity of the GEF"].
- Timing relative to ciliary vesicle (CV) formation [PMID:25686250 "only after ciliary vesicle assembly is Rab8
  activated for ciliary growth"].
- Non-ciliary: cortical actin, lamellipodia, polarized traffic [PMID:12221131].
- Nuclear only on SSX2 co-expression [PMID:12007189 "the RAB3IP protein is normally localized in the cytoplasm";
  "coexpression of both RAB3IP and SSX2 led to colocalization of both proteins in the nucleus"].

### Key decisions

- GEF activity (6 rows): ACCEPT, core MF (GO:0017112 Rab GEF was merged into GO:0005085; verified via OLS).
- Protein binding: RAB8A and RAB3A rows MODIFY -> GO:0031267 small GTPase binding; others REMOVE (TRAPPII subunits,
  TRAPPC14, SSX2, RAB3IL1, DCDC5, HuRI and SARS-CoV-2 hits).
- GO:1905349 ciliary transition zone assembly (Reactome TAS R-HSA-5620912): MARK_AS_OVER_ANNOTATED. This row is the
  mechanical replacement for obsoleted GO:0097711 (see projects/CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md; Reactome has
  revised the entry). RAB3IP activates RAB8A for ciliary membrane growth; TZ assembly is executed by TZ proteins.
- Protein targeting to membrane (IDA): ACCEPT (GEF catalysis targets Rab8).
- Nucleus/nucleoplasm (incl. HPA IDA): KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role

- HPA: **Centrosome (Supported)**; main location "Nucleoplasm". GOA HPA rows: nucleoplasm, centrosome and cytosol IDA
  (GO_REF:0000052).
- Module role: RAB8 GEF in ciliary vesicle formation / ciliary membrane supply (stage 2). The centrosome call fits the
  literature (Rabin8 accumulates at the mother centriole on Rab11/TRAPPII vesicles). No ciliary-compartment call is
  expected for a cytosolic GEF.
- Nuance against the module wording: Lu et al. 2015 show that ciliary vesicle *formation* from distal appendage vesicles
  is EHD1/EHD3-dependent and that Rab8 is activated only after the CV forms. RAB3IP therefore belongs to the
  "ciliary membrane supply/extension" part of stage 2 rather than CV formation per se. core_functions state this
  explicitly (GEF activity; cilium assembly; centrosome/vesicle). No NEW GO:1905556 (ciliary vesicle assembly)
  annotation is proposed.

## Deep research outcome

The re-run `just deep-research-falcon human RAB3IP --timeout 2400` succeeded and produced
`RAB3IP-deep-research-falcon.md` (2026-10-03). I read it after drafting the review. Its summary agrees with the
cached primary literature used here and changes none of the curation decisions. The review's supporting quotes come
from the cached publications, not from the deep-research file.
