# ZDS1 review notes

## Identity and research provenance

- Canonical target: ZDS1/YMR273C, UniProt P50111. `HST1` is a legacy synonym of
  ZDS1 and caused the earlier directory collision with canonical sirtuin HST1
  (YOL068C/P53685).
- The existing Falcon report is correctly grounded on P50111/ZDS1, although its
  recorded request metadata still contains the former `gene_id: HST1` value.
- `just deep-research-openscientist yeast ZDS1` was attempted twice on
  2026-08-12. Both jobs resolved P50111/ZDS1 correctly but failed while polling
  the provider (first `ConnectTimeout`, then DNS `ConnectError`). No provider
  artifact was written or fabricated.

## Curation corrections

- PMID:10662670 directly studies ZDS1 deletion and reports redistribution of
  silencing among rDNA, a silent mating-type cassette, and telomeres. The
  experimental heterochromatin annotation is therefore retained as non-core;
  the initialized review's claim that the paper concerned a different protein
  was incorrect.
- PMID:18762578 directly reports that ectopic Zds1 down-regulates PP2A-Cdc55 and
  suggests that Zds1/Zds2 act as separase-regulated PP2A-Cdc55 inhibitors.
  Later spatial-localization work refines this mechanism but does not justify
  removing the experimental molecular-function annotations.
- Generic `protein binding` annotations were migrated from
  MARK_AS_OVER_ANNOTATED to REMOVE under the current GO:0005515 policy: the
  reported interactions are true, but the rows do not by themselves establish an
  evidence-backed, specific molecular function for Zds1.
- Coimmunoprecipitation with Cdc55 and Tpd3 demonstrates association with
  PP2A-Cdc55, not `part_of` membership in the heterotrimeric PP2A holoenzyme;
  no new GO:0000159 annotation is proposed.

## Core synthesis

Zds1 is a non-catalytic PP2A-Cdc55 adaptor/regulator. Its principal conserved
role is to establish the cytoplasmic and cortical pool of PP2A-Cdc55 and limit
nuclear Cdc55, thereby coordinating mitotic entry and exit. Cell-polarity,
cell-wall, mRNA-export, and chromatin-silencing phenotypes are retained where
experimentally supported but are secondary to this core mechanism; the broad
mRNA-transport parent is marked over-annotated because the more specific
nuclear-export term is already supported.

## 2026-09-29 IBA re-review

Re-checked the three ZDS1 IBA rows against `projects/IBA_REVIEW.md` and the
current `interpro/panther/PTHR28089/PTHR28089-paint.tsv` cache. The
`GO:0005737` cytoplasm, `GO:0010971` positive regulation of G2/M transition of
mitotic cell cycle, and `GO:0030010` establishment of cell polarity rows all
trace to `PANTHER:PTN001999034`, the fungal ancestral node for the Zds1/Zds2
family, and all are supported by direct budding-yeast ZDS1/ZDS2 seeds in PAINT.
The target's own experimental evidence is legitimate support for the ancestral
IBD placement rather than a circular source, so all three transfers were marked
`SUPPORTS_TRANSFER`; the polarity row remains `KEEP_AS_NON_CORE` because that
process is secondary to the core PP2A-Cdc55 adaptor/localization activity.

This pass also migrated the six `GO:0005515` protein binding rows from the old
`MARK_AS_OVER_ANNOTATED` convention to `REMOVE`. Those interactions still
support the mRNA-export and PP2A-Cdc55 regulatory annotations, but generic
protein binding does not add an informative standalone molecular function.

Searches for newer ZDS1/Zds1, Cdc55, PP2A and Rho1 literature did not find a
newer peer-reviewed paper that supersedes the cached 2011 Cdc55-localization
work, the 2016 Rho1-output paper summarized in the Falcon report, or the 2023
yeast interactome map already referenced in the review.

## 2026-10-10 PTHR28089 family pass: GOA refresh and molecular-function re-assessment

Context: review of PANTHER PTHR28089 (ZDS1, ZDS2, S. pombe zds1). The PAINT node
PTN001999034 (Fungi) now also asserts GO:0004864 protein phosphatase inhibitor
activity (IBD dated 2026-03-20), seeded only by ZDS1 (SGD:S000004886).

GOA refresh housekeeping:
- Seven review rows no longer in GOA were removed: GO:0051028 and GO:0071555
  (IEA, GO_REF:0000043), and GO:0005515 IPI rows from PMID:16429126, 16554755,
  18762578, 19536198 and 37968396.
- Seven new GOA rows were resolved (IBA inhibitor, Gfd1 protein binding, DBP5
  mRNA-export IGI/IPI, ZDS2 G2/M IGI, CDC42 and ZDS2 polarity IGI).
- SGD ids were resolved via the SGD API: S000003158 = CDC55 (not separase, as
  the earlier IGI review text implied), S000004219 = CDC42, S000005572 = DBP5,
  S000004868 = GFD1, S000000039 = CDC24, S000004577 = ZDS2.

Molecular-function conclusion: protein phosphatase regulator activity
(GO:0019888) is the core MF, and the inhibitor rows (IBA/IMP/IGI) are MODIFY to it.
- Evidence for inhibition (context: mitotic exit, overexpression):
  [PMID:18762578 "The PP2ACdc55 phosphatase-specific activity decreased to about half of its initial value in response to Zds1 induction"];
  [PMID:18762578 "Our results suggest that these proteins may act as separase-regulated PP2A(Cdc55) inhibitors."]
- Evidence for activation/targeting (context: mitotic entry):
  [PMID:21119008 "Thus, Zds1/2 activate PP2ACdc55-dependent dephosphorylation of Mih1."];
  [PMID:21119008 "which suggests that they can play both positive and negative roles in the regulation of PP2ACdc55"];
  [PMID:21536748 "Zds1/Zds2 promote Cdc55-PP2A function for mitotic entry, whereas Zds1/Zds2 inhibit Cdc55-PP2A function during mitotic exit."]
- The Queralt lab itself retreated from the direct-inhibitor model:
  [PMID:22427694 "Therefore, it seems unlikely that Zds1p and Zds2p act as direct inhibitory components of the PP2ACdc55 complex."]
- Binding: [PMID:22427694 "Zds1p physically interacts with, and regulates the localization of, Cdc55p through the Zds_C motif."];
  Zds2 binds Cdc55 directly in vitro [PMID:20980617 "ZH4 is shown by protein affinity assays to be necessary and sufficient for interaction with Cdc55p"].
- Family scope: [PMID:24800822 "Zds1-family proteins are found only in fungi but not in higher eukaryotes."]
- I found no published Zds-derived peptide that inhibits PP2A-Cdc55 in vitro
  (PubMed search for (Zds1 OR Zds2) AND (Cdc55 OR PP2A) returned 12 papers, none
  with such an experiment). The only activity measurement is the immunopurified
  PP2A-Cdc55 assay after Zds1 overexpression in PMID:18762578.

NEW: GO:0031536 positive regulation of exit from mitosis (IMP, PMID:18762578).
Comparator check (QuickGO, taxon 559292): ESP1 (IMP/IGI), LTE1 (IMP), GLC7 (IGI)
and NUD1 carry GO:0031536, and CDC55 carries GO:0001100 negative regulation of
exit from mitosis. Zds1 is a regulator that does the regulatory work, acting
through PP2A-Cdc55 on Net1 phosphorylation
[PMID:18762578 "Zds1 and Zds2 are required downstream of separase to facilitate nucleolar Cdc14 release."].

Rim15/TORC1 links: no primary paper linking Zds1 to Rim15 was found. In that
module, the PP2A-Cdc55 inhibitors are the endosulfines Igo1/Igo2
[PMID:24800822 "Igo1/Igo2 can inhibit Cdc55 in early mitosis, but their contribution to Cdc55 regulation is relatively minor compared with the role of Zds1/Zds2"].
No Rim15-related annotation was proposed.
