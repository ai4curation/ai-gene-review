# IGO1 curation notes

## 2026-09-26 Initial review (P53897, YNL157W)

### Inputs

- `IGO1-uniprot.txt` (entry version 165), `IGO1-goa.tsv` (16 rows, 5 references),
  `IGO1-deep-research-falcon.md` (Edison/Falcon synthesis, 25 citations).
- Cached publications: PMID:20471941 (abstract only), PMID:23273919 (abstract
  only), PMID:23861665 (full text), PMID:14562095 (abstract only). Sarkar 2014
  (PLoS Genet), Talarek 2017 (eLife) and Hollenstein 2021 (EMBO Rep) are NOT
  cached; their content is taken from the Falcon report only and is used for
  context (description, core-function narrative), never as `supported_by` for an
  existing annotation. Superseded 2026-10-01: Talarek 2010, Sarkar 2014,
  Talarek 2017 and Hollenstein 2021 are now full-text cached.
- Comparators: human ENSA / ARPP19 / MASTL / PPP2R2A reviews (complete); yeast
  RIM15 review; `modules/g2_m_transition.yaml` (cites IGO1 as the budding-yeast
  endosulfine exemplar in the optional Greatwall-endosulfine part).

### Gene identity

Igo1 = "Initiation of G zero 1", endosulfine family (PF04667, PTHR10358:SF6),
168 aa, paralog Igo2 (YHR132W-A). Rim15 phosphorylates Ser64 in the conserved
YFDSGDY motif [PMID:20471941 "Rim15 coordinates transcription with
posttranscriptional mRNA protection by phosphorylating the paralogous Igo1 and
Igo2 proteins"]; UniProt: "Phosphorylated at Ser-64 by RIM15." Do not confuse
with S. pombe igo1 (SPAC10F6.16 / mug134), which is the subject of the 2024
Nature Communications translation/tRNA-modification paper (Falcon flags this).

### Holistic picture

1. **Core molecular function: phosphorylation-gated PP2A-Cdc55 inhibitor.**
   [PMID:23273919 "Rim15, analogous to the greatwall kinase in Xenopus,
   phosphorylates endosulfines to directly inhibit the Cdc55-protein phosphatase
   2A (PP2A(Cdc55))"]; independently [PMID:23861665 "addition of phosphorylated
   Igo1 to PP2ACdc55 complexes inhibited their activity in vitro in a
   dose-dependent manner"; "efficient interaction between Igo1 and PP2A requires
   Rim15-dependent phosphorylation of Igo1 on Ser64"; Pph21 and Cdc55 but not
   Rts1 co-IP with Igo1-Pk3]. Specificity for the Cdc55 holoenzyme is also
   genetic: cdc55 and pph21 deletion suppress igo1 igo2 / rim15 quiescence
   defects, rts1 deletion does not (Falcon report, from Bontron 2013).
2. **Core process: initiation of the G0 programme / quiescence entry**
   (GO:1903452). Downstream readouts: Gis1 kept phosphorylated and
   promoter-bound [PMID:23273919 "Inhibition of PP2A(Cdc55) preserves Gis1 in a
   phosphorylated state and consequently promotes its recruitment to and
   activation of transcription from promoters of specific nutrient-regulated
   genes"], Msn2/4- and Gis1-dependent gene expression, glycogen accumulation,
   chronological life span.
3. **mRNA protection branch** (GO:0048255, GO:1900152): Rim15-phosphorylated
   Igo proteins associate with Dhh1 and shelter newly made G0 transcripts from
   5'-3' decay [PMID:20471941 "This event, which stimulates Igo proteins to
   associate with the mRNA decapping activator Dhh1, shelters newly expressed
   mRNAs from degradation via the 5'-3' mRNA decay pathway"]. UniProt records
   interactions with RIM15, DHH1, PBP1, PBP4, LSM12. Caveats: (a) the 2013 PP2A
   mechanism could account for the effect indirectly; (b) Sarkar 2014 did not
   reproduce dhh1/ccr4 suppression in the SK1 background [PMID:24968058 "We
   also found that dhh1Δ and ccr4Δ did not suppress the G0 entry defect of
   igo1Δ igo2Δ cells"]. Kept as ACCEPT with caveats recorded;
   the curator read the full text and the finding is the paper's central claim.
4. **Mitotic role (Juanes 2013, full text).** Paradoxical: phospho-Igo1 is an
   inhibitor in vitro, but in vivo igo1 igo2 cells have LOWER PP2A-Cdc55
   activity, nuclear-retained Cdc55, elevated Swe1-dependent Cdk1-Y19
   phosphorylation and delayed mitotic entry/progression at 16 C and 38 C
   (not at 25 C); swe1 deletion or Cdc28-Y19F rescues [PMID:23861665
   "Surprisingly, deletion of IGO1 and IGO2 in yeast cells leads to a decrease
   in PP2A phosphatase activity, suggesting that endosulfines act also as
   positive regulators of PP2A in yeast"; "RIM15 and IGO1/2 promote, like
   PP2A(Cdc55), timely entry into mitosis under temperature-stress"]. Igo1-Cdc55
   binding peaks in late S/G2 while Ser64 phosphorylation is constant across
   the cycle. So in budding yeast, where PP2A-Cdc55 is pro-mitotic, the
   endosulfines support rather than oppose mitotic entry. NOTE: the task brief
   said Igo1 "contributes to mitotic entry/exit timing by restraining
   PP2A-Cdc55"; the paper says the opposite for the in vivo mitotic role, and
   the review follows the paper.
5. Other roles (Falcon only, not cached): START / cell-size homeostasis via
   Whi5 (Talarek 2017), sporulation and pre-meiotic autophagy (Sarkar 2014;
   ~3 % vs 65 % sporulation; S64A rescues poorly), hyperosmotic-stress
   phosphorylation response parallel to Hog1 (Hollenstein 2021; Igo1-S64
   phosphorylation up 7.3-fold within seconds). Mentioned in description and
   core-function narrative only.
6. Localisation: cytoplasm + nucleus (Huh 2003 GFP screen; SGD IDA nucleus from
   Talarek 2010), P-body pool during G0 initiation (SGD IDA from Talarek 2010).
   Falcon: nuclear concentration of the Rim15/Igo system under phosphate
   starvation, diauxic shift, TORC1 inhibition.

### Decisions on the 16 GOA rows

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0000932 P-body | IDA 20471941 | ACCEPT | abstract-only; Dhh1 association + UniProt partners; defer to curator |
| GO:0004864 | IBA | ACCEPT | family-root IBD; IGO1 in own WITH/FROM is expected |
| GO:0004865 | IDA 23273919 | ACCEPT | core MF |
| GO:0004865 | IDA 23861665 | ACCEPT | core MF, full text quoted |
| GO:0004865 | IMP 23273919 | ACCEPT | cdc55/pph21 epistasis |
| GO:0005634 nucleus | HDA 14562095 | ACCEPT | |
| GO:0005634 nucleus | IDA 20471941 | ACCEPT | |
| GO:0005737 cytoplasm | HDA 14562095 | ACCEPT | |
| GO:0005737 cytoplasm | IBA | ACCEPT | |
| GO:0048255 mRNA stabilization | IGI IGO2 | ACCEPT | caveats recorded |
| GO:1900152 (x2) | IGI CCR4/DHH1 + IGO2 | ACCEPT | mechanistic form of the above |
| GO:1901992 | IGI IGO2, 23861665 | KEEP_AS_NON_CORE | conditional (temperature stress), non-canonical mechanism; GO:0010971 noted as a defensible narrower term |
| GO:1903452 (x3) | IGI IGO2 / PPH21 / CDC55 | ACCEPT | core BP |

No REMOVE, MODIFY, UNDECIDED or NEW. The RIM15 review MODIFYed its own
GO:1901992 rows to GO:1903452; for IGO1 that would be wrong because the Juanes
2013 evidence is specifically about mitotic entry in cycling cells, not G0.

### NEW-term consideration (rejected)

The human ENSA review added GO:0010923 "negative regulation of phosphatase
activity" as NEW with ARPP19 as comparator. For yeast a QuickGO query for
GO:0010923 in taxa 559292 and 4896 returned zero annotations - neither IGO2 nor
S. pombe igo1 carries it; SGD/PomBase express the same biology as the MF
inhibitor term plus the quiescence BP. That is a MOD convention, not a gap, so
`proposed_new_terms: []`.

### Term ids verified via QuickGO (2026-09-26)

GO:0004864, GO:0004865, GO:0010923, GO:0051721, GO:0000086, GO:1903452,
GO:1901992, GO:0048255, GO:1900152, GO:0000932 all current (non-obsolete) with
the labels used; GO:0010971 = positive regulation of G2/M transition of mitotic
cell cycle (mentioned in a `reason` only, not asserted).

### Validation

`just validate yeast IGO1` -> Valid (no errors). All `supporting_text`
snippets were additionally checked as whitespace-normalised substrings of the
cached publications, the Falcon report and the UniProt record.

### Follow-ups

- Completed 2026-10-01: fetched full text for PMID:20471941 (PMC2919320) to
  verify the P-body/nucleus IDA rows and the dhh1/ccr4 IGI rows directly.
  PMID:23273919 remains abstract-only.
- Completed 2026-10-01: cached PMID:24968058 (Sarkar 2014), PMID:28600888
  (Talarek 2017) and PMID:34558777 (Hollenstein 2021) so the START,
  sporulation and osmostress roles can be cited as primary literature. The
  previously listed candidate PMIDs for Sarkar 2014 and Talarek 2017 were
  wrong; these are the PubMed-verified records for those papers.
- Completed 2026-10-01: added
  `history/genes/yeast/IGO1/2026-10-01T221113Z-codex-447b74.yaml` to record the
  IGO1 refresh.

## 2026-10-01 refresh

- Rebased from `origin/main` and reran `just fetch-gene yeast IGO1 --force`;
  the current GOA import still has the same 16 annotation rows reviewed on
  2026-09-26.
- Fetched current PAINT rows for `PTHR10358`. `PTN001309504` is the IBD node for
  both `GO:0004864` protein phosphatase inhibitor activity and `GO:0005737`
  cytoplasm; both IBA rows still point to this node, and IGO1 being present in
  its own `WITH/FROM` is target experimental grounding rather than circularity.
- Searched 2024-2026 papers for newer *S. cerevisiae* IGO1 work and found no
  newer direct budding-yeast IGO1 functional paper than Hollenstein et al. 2021.
  The 2024 *Nature Communications* `igo1` paper remains a fission-yeast study.
- Cached full text for PMID:24968058 (Sarkar et al. 2014), PMID:28600888
  (Talarek et al. 2017), and PMID:34558777 (Hollenstein et al. 2021), and
  upgraded PMID:20471941 to full text. The Sarkar and Talarek IDs listed as
  fetch candidates on 2026-09-26 were wrong; the IDs above are the
  PubMed-verified records for those papers.
- Updated `IGO1-ai-review.yaml` to cite Talarek et al. 2010 directly for P-body
  and nuclear/cytoplasmic localisation, and to replace Falcon-only START,
  gametogenesis and osmotic-stress context with cached primary citations.
