# MAP3K2 (MEKK2) curation notes

UniProt Q9Y2U5, 619 aa. N-terminal PB1 domain (PB1_MEKK2/3, IPR034879), C-terminal STE11-family
Ser/Thr kinase domain. Close paralog of MAP3K3/MEKK3 (kinase domains ~94% conserved)
[PMID:8621389 "The kinase domains encoded in the COOH-terminal moiety are 94% conserved"].

## Molecular function

- MAP3K that phosphorylates and activates MAP2Ks. Original cloning: immunoprecipitated MEKK2
  phosphorylated MEK1 and JNKK; overexpression activates ERK1/2 and JNK but not p38
  [PMID:8621389 "Immunoprecipitated MEKK 2 phosphorylated the MAP kinase kinases, MEK 1, and JNK kinase."].
- Best-established physiological substrate: MEK5 (MAP2K5), recruited through PB1-PB1 heterodimerization
  [PMID:12912994 "Deletion or mutation of the MEKK2 PB1 domain abolishes MEKK2-MEK5 complexes"],
  [PMID:11073940 "we have identified MEK5, the MAPK kinase in the big mitogen-activated protein kinase 1 (BMK1)/ERK5 pathway, as a binding partner for MEKK2"].
- Direct phosphorylation of MEK5 (Ser311/Thr315) and MKK6 (Ser207), with a kinase-dead D483N control,
  and a 2.4 A kinase-domain crystal structure showing an alphaG-centred dimerization surface needed for
  autophosphorylation, conserved with MEKK3 [PMID:41318559 "we find that MEKK2 efficiently phosphorylates MEK5, but that its inactivation by D483N mutation results in loss of MEK5 phosphorylation"].
- MKK7/JNK branch in mast cells: MEKK2 disruption inhibits FcepsilonRI-induced MKK7 activation
  [PMID:11274363 "MKK7 is activated in response to cross-linking of FcepsilonRI, and this activation is inhibited by MAP/ERK kinase (MEK) kinase 2 (MEKK2) gene disruption"].
  But in T cells Mekk2 loss does not block JNK (moderately enhances it) [PMID:12138187 "TCR-mediated c-Jun N-terminal kinase activation was not blocked but moderately enhanced in Mekk2(-/-) T cells"].
  So the JNK branch is context-dependent; not proposed as a NEW term.

## Biological process

- ERK5 cascade: MEKK2-MEK5-ERK5-MEF2C module in mast cells [PMID:14515274 "these data define an activation module, MEKK2-MEK5-ERK5-MEF2C in the transcriptional activation of c-Jun in mast cells"].
  Free PB1 domain of MEKK2/3 selectively blocks ERK5 but not p38/JNK [PMID:12912994].
- Hyperosmotic stress: MEKK2 mediates transient ERK activation, terminated by CHIP (STUB1)-dependent
  degradation [PMID:20588253].
- Hippo: MEKK2/3 phosphorylate LATS1/2 and YAP/TAZ downstream of TNF, serum, actin dynamics [PMID:33571521] (mostly
  combined MEKK2/3 perturbation; not proposed as NEW).
- Regulators: STK38 binds the catalytic domain and inhibits MEKK2 autophosphorylation [PMID:17906693];
  SMYD3 methylates MEKK2 (Lys260) [PMID:27066749]; 14-3-3 binds phospho-Thr283 (deep research; secondary
  source) ; NEDD4L ubiquitination (deep research, not cached).

## Localization

- Cytosolic at rest; translocates to nucleus on EGF [PMID:15075238 "their upstream activator MEKK2 is localized mainly in the cytosol of resting cells, and translocates into the nucleus upon EGF stimulation"].
- HPA IDA: cytosol + nucleoplasm (GO_REF:0000052).

## Annotation issues

- GO:0071260 cellular response to mechanical stimulus (IEP, PMID:19593445, UniProt 2010). The cached
  full text of PMID:19593445 (BAD in prostate cancer) contains no mention of MEKK2/MAP3K2 or of mechanical
  stimuli; the citation appears not to support the annotation. Left UNDECIDED rather than REMOVE because we
  cannot rule out supplementary data / identifier mix-up without the curator's source.
- GO:0004672 IDA from PMID:15001576 (TRAF7/MEKK3 paper): abstract only mentions MEKK3. Following the
  "do not overrule curators" rule: function is clearly correct for MEKK2, so ACCEPT.
- Protein binding IPIs: 14-3-3 partners (SFN, YWHAE) -> GO:0071889; MAP2K5 -> GO:0019901; STUB1 (CHIP E3)
  -> GO:0031625; SMYD3 (methyltransferase acting on MEKK2) -> REMOVE (no informative MF for being a
  substrate). Mirrors the MAP3K5 review.
- IDA intracellular signal transduction (PMID:14515274) -> MODIFY to GO:0070375 ERK5 cascade.
  ERK5 cascade is sparsely used in GO (7 annotations across human/mouse/rat in QuickGO, 2026-09), so its
  absence on MEKK2/3 is not a curatorial convention; MEKK2 catalyses the MEK5-phosphorylation step, so it
  participates (passes the participation test).

## Audit (second pass)

- Replaced deep-research (secondary) support for the 14-3-3 protein-binding MODIFYs with primary papers:
  [PMID:23963453 "We have found that MEKK2 is regulated through a phosphorylation-dependent association with 14-3-3"],
  [PMID:9452471 "14-3-3 proteins also interacted with MEKK1 and MEKK2, but not MEKK4."]. MEKK3 comparison now cites
  PMID:18308725 (pThr294) and PMID:16407301 (pSer526).
- Added reference_review to all references; tightened description (Ser519 autophosphorylation, Lad/RIBP, viable knockout
  [PMID:12138187 "Mekk2(-/-) mice are viable and fertile"]).
- Suggested question on MEKK2 vs MEKK3 dominance checked against PMID:11073940 abstract (kinase-inactive MEKK3, not
  MEKK2, blocked EGF/H2O2 ERK5 activation in Cos7/HEK293; reverse in D10 T cells).
