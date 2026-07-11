# HSD11B1 (P28845) review notes

## Identity
- 11-beta-hydroxysteroid dehydrogenase type 1 (11beta-HSD1), a.k.a. cortisone reductase,
  corticosteroid 11-beta-dehydrogenase isozyme 1, SDR26C1, 7-oxosteroid reductase.
- 292 aa, short-chain dehydrogenase/reductase (SDR) family member.
- EC 1.1.1.146 (11beta-HSD) and EC 1.1.1.201 (7-oxosteroid / 7beta-HSD).

## Core biology (from UniProt P28845 + abstracts)
- NADP(H)-dependent enzyme; single-pass type II membrane protein of the ER membrane, with
  the catalytic C-terminal domain protruding into the ER lumen [PMID:10497248].
- Interconverts inactive cortisone <-> active cortisol (and 11-dehydrocorticosterone <->
  corticosterone). Bidirectional in vitro, but predominantly a REDUCTASE in vivo (cortisone
  -> cortisol), amplifying local glucocorticoid concentrations = "pre-receptor" glucocorticoid
  activation [UniProt FUNCTION; PMID:15152005 "pre-receptor function"].
- Directionality is set by NADPH supply: ER-lumenal hexose-6-phosphate dehydrogenase (H6PD)
  regenerates NADPH and drives HSD11B1 as an oxoreductase; the G6P transporter supplies H6PD
  substrate [UniProt ACTIVITY REGULATION; PMID:15280030 (Atanasov 2004), PMID:17593962].
- Broad substrate range beyond glucocorticoids: 7-oxo/7beta-hydroxy oxysterols
  (7-ketocholesterol -> 7beta-hydroxycholesterol), 7-oxo bile acids (7-oxolithocholate ->
  chenodeoxycholate/ursodeoxycholate), 7-oxo/7beta-hydroxy neurosteroids, 11-oxy C19 steroids.
- Highest expression in liver; also adipose, brain, eye (cornea/ciliary epithelium), gonad.
  Drug target for metabolic syndrome / type 2 diabetes / obesity because adipose 11beta-HSD1
  cortisol regeneration drives visceral adiposity [PMID:15513927 "In adipose tissue, excessive
  cortisol production through 11beta-HSD1 activity has been implicated in the pathogenesis of
  type II diabetes and obesity"].
- Homodimer (crystal structures show tetramerization motif at C-termini)
  [PMID:15513927, PMID:17919905, PMID:18069989, PMID:18485702, PMID:18553955, PMID:19217779].
- Disease: cortisone reductase deficiency 2 (CORTRD2, MIM:614662) — failure to regenerate
  cortisol from cortisone, ACTH-driven adrenal androgen excess [PMID:12858176].

## Curation reasoning for GOA lines
- MF 11beta-HSD (NADP+) activity GO:0070524 = CORE (IBA + multiple IDA). ACCEPT.
- MF cortisol dehydrogenase (NADP+) GO:0102196 (RHEA IEA, RHEA:68616 cortisone+NADPH=cortisol+NADP)
  captures the physiologically dominant reductase reaction; ACCEPT (more specific than parent).
- MF carbonyl reductase (NADPH) GO:0004090 (RHEA IEA) is a broad generic parent capturing the
  bile-acid/oxysterol 7-oxo reductions; not the informative core term but not wrong -> MARK_AS_OVER_ANNOTATED.
- MF 7beta-HSD (NADP+) GO:0047022 (EC 1.1.1.201 IEA) supported by oxysterol/bile-acid data
  (PMID:15095019, 14973125, 21453287). ACCEPT (secondary but real, EC-backed moonlighting activity).
- MF steroid binding GO:0005496 (IBA) — substrate binding, real but generic; KEEP_AS_NON_CORE.
- MF NADP binding GO:0050661 (6x IDA, all from crystal-structure/inhibitor papers with NADP in
  complex) — cofactor binding, real; KEEP_AS_NON_CORE (cofactor, not the informative core MF).
- MF protein homodimerization GO:0042803 (6x IDA) — homodimer confirmed by crystallography;
  ACCEPT (real quaternary structure), keep as non-core relative to catalysis.
- CC ER membrane GO:0005789 (IBA is_active_in, IEA SubCell, 2x Reactome TAS, IDA PMID:10497248)
  = CORE localization. ACCEPT.
- CC membrane GO:0016020 (HDA, NK-cell membrane proteome MS PMID:19946888) — generic parent of
  ER membrane, HTP proteomics; MARK_AS_OVER_ANNOTATED.
- BP steroid catabolic process GO:0006706 (IBA) — HSD11B1's core in-vivo action is reductive
  ACTIVATION not catabolism; the oxidative/oxysterol directions can be catabolic but the term
  is imprecise for the core role -> MODIFY to glucocorticoid metabolic process GO:0008211.

## core_functions choices
- MF: GO:0070524 11-beta-hydroxysteroid dehydrogenase (NADP+) activity.
- BP (directly_involved_in): GO:0008211 glucocorticoid metabolic process.
  (Note: GO:0034651 cortisol biosynthetic process is defined as de novo synthesis from
  cholesterol in the adrenal gland — HSD11B1 does pre-receptor regeneration, not de novo
  synthesis, so glucocorticoid metabolic process is the accurate BP.)
- CC (located_in): GO:0005789 endoplasmic reticulum membrane.

## Sources
- publications/PMID_*.md are all abstract-only (full_text_available: false).
- Deep research not available (falcon out of credits, HTTP 402). Grounded in UniProt + abstracts + GOA.
