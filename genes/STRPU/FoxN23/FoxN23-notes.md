# FoxN2/3 (Strongylocentrotus purpuratus, UniProt Q2V887) - curation notes

## Identity

- UniProt Q2V887 (`Q2V887_STRPU`, unreviewed/TrEMBL, 197 aa, flagged as a
  Fragment with a non-terminal C-terminus) is the S. purpuratus FoxN2/3 cDNA
  deposited by the Davidson lab (EMBL DQ286744 / ABB89482.1, `GN Name=FoxN2/3`).
  Its single RX line is PMID:17081512, the genome-wide Forkhead survey of Tu,
  Brown, Davidson & Oliveri (2006) that defined the 22 S. purpuratus fox genes.
  NCBI GeneID 590815 (`LOC590815`, "forkhead transcription factor N2/3", alias
  FoxN2/3; checked via NCBI gene esummary, 2026-10-04) is the same locus.
- The automated RecName "Forkhead box protein N3" and the ARBA function note
  ("Acts as a transcriptional repressor. May be involved in DNA damage-inducible
  cell cycle arrests") are family-level transfers from vertebrate FOXN3/CHES1 and
  are not sea urchin data. The sea urchin gene is equally related to vertebrate
  FOXN2 and FOXN3, hence the community symbol `FoxN2/3` (also written `foxN2/3`,
  `foxn2/3`, `Sp-FoxN2/3`). The FoxN subfamily has only two sea urchin members:
  [PMID:21303847 "22 fox genes were identified from the Strongylocentrotus
  purpuratus genome by searching for the conserved forkhead motif, and two
  members of the foxN subfamily were found: foxN1/4 and foxN2/3"]. Because the
  accession is the Davidson-lab FoxN2/3 clone itself, the identity between the
  accession and the GRN gene is not in doubt (confidence: high).
- Domain content: a single Fork-head DNA-binding domain (PROSITE PS50039, residues
  86-173; CDD cd20059 FH_FOXN3; InterPro IPR047119 "FOXN2/3-like"). PANTHER
  PTHR13962:SF22, whose official label (from `interpro/panther/panther.obo`) is
  "FORKHEAD BOX PROTEIN N3-LIKE PROTEIN" (family PTHR13962 "FORKHEAD BOX PROTEIN
  N3-LIKE PROTEIN-RELATED").
- Tu et al. 2006 is abstract-only in the cache; the abstract describes the
  survey, not foxN2/3 specifically: [PMID:17081512 "All but one of the S.
  purpuratus fox genes (SpfoxQ1) are expressed during embryogenesis, most in a
  very specific temporal and spatial manner."].

## Organism caveat for the functional literature

- The only functional (perturbation) studies of foxN2/3 are from the McClay lab
  and were done in **Lytechinus variegatus**, not S. purpuratus:
  [PMID:21303847 "In this study, foxN2/3 was cloned from Lytechinus variegatus
  and its regulation and function were investigated."] and
  [PMID:24598159 "To observe regulatory control of EMT directly, we used the sea
  urchin Lytechinus variegatus"]. The authors explicitly matched the Lytechinus
  expression pattern to the published S. purpuratus pattern: [PMID:21303847
  "variegatus foxN2/3 was similar to that previously reported for S. purpuratus
  ( Tu et al., 2006 ), and with time the expression sites changed dynamically."].
  The two species are both camarodont euechinoids with essentially the same PMC
  GRN architecture, so the data are used here as the primary functional evidence
  for the S. purpuratus orthologue, but every functional annotation derived from
  them is flagged as inferred across species.
- S. purpuratus-specific data are expression-level only: the Davidson-lab
  nCounter time course measured foxn2/3 transcript prevalence through
  mid-gastrula [PMID:20398801 "(Fig. 2: alx1, dach, e2a, erg, foxn2/3, myc,
  otxb1/2, soxc)"], and Materna & Davidson note that in S. purpuratus foxN2/3
  is first skeletogenic and then switches to NSM: [PMID:23261933 "though
  initially expressed in the skeletogenic lineage the zinc finger gene z48 as
  well as the transcription factor foxN2/3, not further considered here, turn
  on in NSM prior to gastrulation (Materna et al., 2006; Tu et al., 2006)"].
- Note: the brief listed Oliveri, Tu & Davidson 2008 (PMID:18413610) and Rafiq
  et al. 2014 (PMID:24496631) as placing foxN2/3 in the PMC GRN. The cached
  text of PMID:18413610 does not name foxN2/3 anywhere (it covers foxb and
  foxo), and the cached abstract of PMID:24496631 does not name it either, so
  neither is cited in the review YAML. Shashikant & Ettensohn (2018) do
  attribute the beta-catenin/Pmar1 dependence of foxN2/3 to Oliveri 2008 (see
  below), so the data are probably in that paper's supplementary material.

## Expression (where and when)

- Transient expression in the large-micromere / primary mesenchyme cell (PMC)
  lineage, then NSM, then endoderm: [PMID:21303847 "Expression of foxN2/3 mRNA
  begins in micromeres at the hatched blastula stage and then is lost from
  micromeres at the mesenchyme blastula stage. foxN2/3 expression then shifts
  to the non-skeletogenic mesoderm and, later, to the endoderm."]. Double FISH
  with tbr (PMC) and gcm (NSM) confirmed the lineage assignments: [PMID:21303847
  "At the hatched blastula stage, foxN2/3 was expressed in the precursors of
  PMCs as the expression sites of foxN2/3 and tbr were coincident"] and
  [PMID:21303847 "At the early mesenchyme blastula stage, as the PMCs ingressed
  they continued to express tbr but eliminated foxN2/3"].
- Listed among the regulatory genes expressed selectively in the PMC lineage in
  the 2018 synthesis of the S. purpuratus skeletogenic GRN: [PMID:30264451
  "These include alx4, dri, erg, fos, jun, foxB, foxN2/3, foxO, hex, mitf,
  nfkbil1L, nk7, nurr1, smad1/5/8, smad2/3, tbr, tel, and tgif"].
- Later gut expression (Lytechinus; reported as not previously described in
  S. purpuratus): "foxN2/3 mRNA was expressed in the endoderm from the early
  gastrula stage and remained in the mid- and hindgut area through the late
  gastrula stage".
- The brief's mention of oral-ectoderm expression is not supported by anything
  in the cached literature; the documented later domains are NSM and endoderm.

## Place in the GRN: inputs

- Downstream of beta-catenin and the Pmar1/HesC double-negative gate:
  [PMID:21303847 "When we overexpressed pmar1 by mRNA injection, foxN2/3
  expression was indeed induced in most of the cells"]; [PMID:30264451
  "overexpression of pmar1 or a form of cadherin that interferes with
  β-catenin function have shown that erg, foxN2/3, hex, tel, and tgif are all
  downstream of β-catenin and pmar1 (Oliveri et al., 2008; see also Rho and
  McClay, 2011, with respect to foxN2/3)"].
- Immediate upstream regulators in micromeres are Ets1 and Tbr, not Alx1:
  [PMID:21303847 "Here, we show that Pmar1, Ets1 and Tbr are necessary for
  activation of foxN2/3 in micromeres."]; [PMID:21303847 "Expression of
  dominant-negative Ets1 blocked foxN2/3 expression in the micromeres"];
  [PMID:21303847 "Embryos injected with tbr morpholinos failed to express
  foxN2/3 in micromeres"]; [PMID:21303847 "loss of Alx1 did not prevent foxN2/3
  expression in the precursors of PMCs, indicating that Alx1 expression does
  not occur upstream of foxN2/3 activation"]. Tbr is necessary but not
  sufficient (AND logic): [PMID:21303847 "This implies that Tbr is not
  sufficient to induce expression of foxN2/3 on its own, and requires other
  PMC-specific transcription factor(s) in an AND logic function (Tbr AND
  another TF)."]. The brief's statement that foxN2/3 lies downstream of alx1 is
  therefore not correct for the micromere phase; it lies downstream of
  ets1/tbr.
- The later NSM/endoderm phase is independent of the micromere phase, of
  Delta/Notch and of the Blimp1 torus subcircuit: [PMID:21303847 "the later
  expression of foxN2/3 requires an independent mechanism that is not dependent
  on earlier foxN2/3 expression in micromeres, nor from the micromere-released
  signals, including activation of Delta in the NSM."]; the authors infer
  [PMID:21303847 "foxN2/3 has at least one PMC-specific cis-regulatory module
  that is regulated by Ets1 and/or Tbr, and as Tbr is only expressed by
  micromeres, this module is not required for the later endomesodermal foxN2/3
  expression."]. No cis-regulatory module has actually been isolated.
- No autoregulation: foxN2/3 transcription is unchanged in foxN2/3 morphants
  ("QPCR results also showed that the expression level of foxN2/3 was not
  significantly changed by foxN2/3 MASOs").

## Place in the GRN: outputs and loss-of-function phenotype

- Two non-overlapping translation-blocking morpholinos with 5'UTR-RFP
  specificity controls and mRNA rescue: [PMID:21303847 "Thus, the morpholinos,
  by those tests, are efficient and specific for blockage of FoxN2/3
  translation."].
- Skeletogenic effector genes require FoxN2/3 early: [PMID:21303847 "Early
  expression of genes for the skeletal matrix is dependent on FoxN2/3, but only
  until the mesenchyme blastula stage as foxN2/3 mRNA disappears from PMCs at
  that time and we assume that the protein is not abnormally long-lived."];
  [PMID:21303847 "When we examined other skeletogenic genes by QPCR in FoxN2/3
  KD embryos, sm30 and sm50 expression levels were also strongly reduced,
  consistent with the hypothesis that many skeletogenic genes require FoxN2/3
  input"]; msp130 protein absent at 12 h. VEGFR is also a target:
  [PMID:21303847 "WMISH showed that the expression of VEGFR in the PMCs is
  absent in FoxN2/ 3 KD embryos whereas the control embryos showed VEGFR signal
  in the ingressed PMCs"]. All of these recover later, so FoxN2/3 is an early
  input, not a maintenance factor: [PMID:21303847 "Thus, although FoxN2/3 is
  part of the GRN that activates skeletogenic genes and the VEGFR , it is not
  likely to be involved in long-term maintenance of that expression."].
- Ingression (EMT): [PMID:21303847 "Knockdown of FoxN2/3 inhibits normal PMC
  ingression and foxN2/3 morphant PMCs do not organize in the blastocoel and
  fail to join the PMC syncytium."]. Saunders & McClay 2014 confirmed foxn2/3
  among the 13 PMC transcription factors required for EMT and found it has the
  strongest apical-constriction / de-adhesion defect: [PMID:24598159 "Three TFs
  highest in the GRN specified and activated EMT (alx1, ets1, tbr) and the 10
  TFs downstream of those (tel, erg, hex, tgif, snail, twist, foxn2/3, dri,
  foxb, foxo) were also required for EMT."]; [PMID:24598159 "Foxn2/3 was the
  only knockdown with a non-apically constricted shape significantly different
  from the mean shape for the duration of the time-course."].
- Cell-autonomous skeletal defect shown by micromere transplantation:
  [PMID:21303847 "PMCs originating from foxN2/3 MASO-injected micromeres
  remained in the blastocoel without contributing to the larval skeleton"];
  syncytium: [PMID:21303847 "knockdown of FoxN2/3 in PMCs resulted in a failure
  of these cells to be incorporated into the syncytium, explaining at least one
  of the reasons that the larval skeleton is malformed in FoxN2/3 KD embryos."].
- Non-autonomous: morphant PMCs fail to send the signal that normally
  suppresses NSM transfating: [PMID:21303847 "without FoxN2/3, the PMCs fail to
  repress the transfating of other mesodermal cells into the skeletogenic
  lineage."]. This is an indirect, signalling-mediated effect and is not
  annotated.
- Summary: [PMID:21303847 "Thus, FoxN2/3 is necessary for normal ingression,
  for expression of several skeletal matrix genes, for preventing transfating
  and for fusion of the PMC syncytium."]; [PMID:21303847 "our results suggest
  that FoxN2/3 is one of those inputs and a number of those inputs continue to
  be expressed after ingression."].

## Curation decisions

- Electronic rows: GO:0003700 (DNA-binding TF activity), GO:0006355, GO:0005634
  are consistent with a Forkhead TF whose knockdown abolishes early expression
  of a battery of PMC effector genes; accepted (nucleus and TF activity) or
  kept as non-core generic parent (GO:0006355). GO:0003677 is over-general
  (MODIFY to GO:0043565 which already exists as a separate row, which is
  accepted). The UniProt ARBA "transcriptional repressor" note is a vertebrate
  FOXN3 transfer; in the sea urchin the only direction shown is activation
  (loss of target expression), and direct binding to any target CRM has not
  been shown, so the sign-specific MF child is NOT proposed.
- NEW rows kept minimal because the functional data are Lytechinus-only:
  GO:0045944 positive regulation of transcription by RNA polymerase II (IMP;
  skeletal-matrix genes, msp130, VEGFR lost in morphants), GO:0010718 positive
  regulation of epithelial to mesenchymal transition (IMP; two independent
  studies), GO:0070169 positive regulation of biomineral tissue development
  (IMP; cell-autonomous failure of transplanted morphant PMCs to contribute to
  the skeleton, loss of sm30/sm50/msp130). Participation test: FoxN2/3 is the
  TF that drives these effector genes, so it does the regulatory work.
  Comparator: Alx1 and Ets1 reviews in this directory carry GO:0010718 and
  GO:0070169 for the same role.
- Not proposed: mesodermal cell fate specification (foxN2/3 is activated after
  the lineage is specified, and alx1/tbr are expressed normally in morphants,
  so it is a differentiation input, not a specification factor); NSM or
  endoderm roles (expression only, no perturbation of those phases); syncytium
  formation / cell fusion (no suitable term established for echinoderm PMC
  fusion, and the mechanism is unknown); regulation of VEGF signalling (VEGFR
  transcript loss is one of many downstream effector losses).
