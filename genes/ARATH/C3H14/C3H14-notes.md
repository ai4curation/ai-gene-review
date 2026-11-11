# C3H14 (AT1G66810; UniProt Q9C9N3) review notes

## 2026-10-23 session

### Deep research
`just deep-research-falcon ARATH C3H14 --fallback perplexity-lite` failed in this
environment: `ERROR - Provider 'falcon' not available. Available: openscientist`, and
the perplexity fallback failed the same way. No `-deep-research-*.md` file was
generated. Literature was assembled manually from PubMed searches
(`(C3H14 OR AtC3H14 OR At1g66810) AND Arabidopsis`, 11 hits), the cached
publications, and the Wiley Scholar Gateway (full-text passages of Wiley papers).

### Source access
| PMID | Paper | Cache | Other access this session |
|---|---|---|---|
| 19674407 | Ko 2009 Plant J, MYB46 network | abstract | one Wiley passage (Figure 6/7 discussion) |
| 22271306 | Kim 2012 PMB, M46RE motif | abstract | none |
| 25228083 | Kim 2014 Plant J, AtC3H14 RNA binding (GOA source for 4 TAIR rows) | abstract | Wiley Scholar Gateway passages 0-12 of 16 (Summary, Introduction, all Results, Discussion, part of Methods) |
| 25732536 | Chai 2015 JXB, C3H14/C3H15 redundancy | abstract | none |
| 28650476 | CrY2H-seq 2017 Nat Methods (IntAct source) | full text | |
| 32279333 | Wang 2020 PCE, Botrytis/WRKY33 | abstract | one Wiley passage (Introduction) |
| 35736512 | Wang 2022 Plant Physiol, MPK4-C3H14 | full text | |
| 36430765 | Wang 2022 IJMS, review | full text | |
| 39276674 | Andres-Borderia 2024 PPB, metal homeostasis (mainly C3H15) | abstract | |
| 41758611 | Xue 2026 Plant Cell, meiotic RNA clearance | abstract | |
| 42711403 | Chen 2026 Nat Plants, meiocyte identity | abstract | |
| 42844995 | Gao 2026 Plant J, IAMH2 3'UTR | full text | |
| 19897605 | Pomeranz 2010 Plant Physiol, AtTZF1 localization (includes At1g66810-GFP) | full text | |

Europe PMC reports none of the abstract-only papers as open access.

### Protein
310 aa; two CCCH zinc fingers at 232-260 and 270-298 [UniProt Q9C9N3 FT ZN_FING];
InterPro IPR045877 ZFP36-like; PANTHER PTHR12547:SF161. Kim 2014 notes that AtC3H14
and AtC3H15 are the only Arabidopsis CCCH proteins with the TTP-type 18-aa
inter-finger spacing, plus an N-terminal leucine-rich NES and a conserved "LS"
motif [PMID:25228083 full text via Wiley, Introduction/Results].

### Molecular function evidence
- **RNA binding, 3'UTR/ARE**: [PMID:25228083 "RNA electrophoretic mobility shift
  assays (RNA-EMSA) were used to confirm the RIP results and demonstrate that the TZF
  domain of AtC3H14 is required for the target RNA binding."]. Full text (Wiley):
  in vivo RIP (DEX-inducible AtC3H14-GFP, formaldehyde cross-linked seedlings)
  enriched At1g23850, At3g22600, At3g57510 (ADPG1), At4g19370 (DUF1218); RNA-EMSA
  used 3'UTR fragments of ADPG1 and DUF1218 "containing the ARE motif"; TZF
  deletions abolished binding.
- **Poly(U) 3'UTR binding with repression**: [PMID:42844995 "the RNA-binding proteins
  C3H14/C3H15 directly bind this poly(U)-rich region to posttranscriptionally
  downregulate IAMH2 mRNA levels"]. Full text: RNA-EMSA with MBP-C3H14; dual-LUC with
  a 35S-LUC-IAMH2 3'UTR reporter, where co-expressing C3H14 "further and significantly
  repressed reporter expression"; IAMH2 mRNA elevated in c3h14 c3h15; iamh2 is
  epistatic for low-light hypocotyl length.
- **mRNA decay machinery**: [PMID:42711403 "C3H14/C3H15 interacts with
  processing-body proteins and the CCR4-NOT deadenylase complex, and is required for
  eliminating unwanted transcripts."] (abstract only; I cannot tell which assays,
  or whether C3H14 or C3H15 was the bait). [PMID:41758611] shows C3H15-DCP1 in
  P-bodies; the abstract does not state this for C3H14.
- **DNA binding / transcription**: [PMID:35736512] ChIP-qPCR and EMSA show C3H14
  binding CHRE-containing fragments (GGGACA/GGGAGA) of the NIMIN1 and NIMIN2
  promoters; NIMIN1/2 expression is up in OE and down in c3h14c3h15. Ko 2009
  (protoplast transactivation of eight secondary-wall genes) and Kim 2014 (GAL4-BD
  fusion autoactivation in yeast) are weaker evidence.

### Localization
- Cytoplasmic foci: [PMID:19897605 "the two closest hTTP homologs, At1g66810 and
  At1g68200, were also localized in cytoplasmic foci"] (35S-GFP in protoplasts,
  Fig. 3B).
- Cytoplasm and nucleus by fractionation: [PMID:35736512 "both phosphorylated and
  dephosphorylated forms of C3H14 protein were detected in the cytoplasm, but only the
  dephosphorylated form was detected in the nucleus"].

### Biological process evidence
- **Secondary wall**: loss of function (double mutant) gives thinner walls;
  overexpression gives thicker walls and ectopic walls [PMID:25732536 abstract]. In
  Kim 2014 every growth and wall phenotype is from 35S overexpression. Full text
  (Wiley): "35S::AtC3H14 plants had early and aberrant phloem fiber development"
  (Figure 7 is titled "Enhanced phloem fiber formation"), and the
  AtC3H14-RNAi/atc3h15-1 lines "did not show any phenotypic alterations". So the
  TAIR IMP row "negative regulation of secondary cell wall biogenesis" (GO:1901347)
  from PMID:25228083 has the wrong sign: the same paper reports enhanced phloem
  fiber formation on overexpression. GO:1901348 positive regulation of secondary
  cell wall biogenesis fits both papers.
- **Cell elongation**: overexpression only in Kim 2014 (dwarf, shorter pith, vessel
  and fiber cells; stamen elongation defect causing sterility). Gao 2026 adds
  loss-of-function support in low-light hypocotyls (via IAMH2). The double mutant
  has larger leaves [PMID:32279333 Introduction, Wiley passage]. GO:0051511 is
  reasonable but rests partly on overexpression.
- **Immunity**: negative regulator of PTI/SAR against Pst DC3000; c3h14c3h15 shows
  enhanced resistance and SAR [PMID:35736512]. Positive regulator of defense against
  Botrytis via WRKY33 [PMID:32279333 abstract].
- **Male meiosis / anther**: [PMID:42711403], [PMID:41758611] (double mutant
  meiotic arrest at pachytene, RNA clearance failure), [PMID:25732536] (few pollen
  grains in double mutant).
- **Metal homeostasis**: [PMID:39276674] attributes the effect to C3H15, not C3H14.

### GO-term checks (OLS4, 2026-10-23)
GO:0003730 mRNA 3'-UTR binding; GO:0035925 mRNA 3'-UTR AU-rich region binding;
GO:0008266 poly(U) RNA binding; GO:0061158 3'-UTR-mediated mRNA destabilization;
GO:0000932 P-body; GO:0005737 cytoplasm; GO:1901348 positive regulation of secondary
cell wall biogenesis; GO:1900425 negative regulation of defense response to bacterium;
GO:0010113 negative regulation of systemic acquired resistance; GO:0050832 defense
response to fungus; GO:0000976 transcription cis-regulatory region binding. None
obsolete.

### Papers a curator with access could supply
25732536 (JXB 2015), 41758611 (Plant Cell 2026), 42711403 (Nat Plants 2026),
32279333 (PCE 2020), 19674407 (Plant J 2009), and 25228083 (the cache is
abstract-only, so full-text quotes cannot be validated).

## 2026-10-23 session 2: curator-supplied full texts

The curator uploaded PDFs of PMID:25228083 (Kim 2014, accepted manuscript),
PMID:25732536 (Chai 2015, JXB) and PMID:41758611 (Xue 2026, Plant Cell). These are
publisher copies under copyright, so they were **not** committed to `publications/`.
Quotes from them are recorded as `supporting_text_fulltext` (not validated against the
cache) with `full_text_unavailable: true`.

### Kim 2014 (PMID:25228083)
- Results heading: "Overexpression of AtC3H14 results in cell elongation defect and
  ectopic secondary wall formation."
- Figure 7 ("Enhanced phloem fiber formation in 35S::AtC3H14 plants") was viewed. TBO
  sections show precocious stem phloem fibers and many extra lignified phloem fibers in
  roots. The TAIR GO:1901347 (negative regulation of secondary cell wall biogenesis)
  sign error is therefore CONFIRMED; the correct term is GO:1901348.
- RNA-EMSA: "RNA-EMSA using AtC3H14-GST and in vitro transcribed ADPG1 and DUF1218 RNA
  fragments of 3'-UTR containing the ARE motif".

### Chai 2015 (PMID:25732536)
- "Both C3H14 and C3H15 were observed to localize to the nucleus and cytoplasmic foci in
  the same cells" (35S:GFP-C3H14 in tobacco epidermis).
- "Both proteins bound poly(rU), single-stranded DNA, and double-stranded DNA, but not
  poly(rC) at 0.1 M NaCl". This contradicts Kim 2014, which reports binding to poly(C)
  and poly(G) as well; salt conditions differ (0.1 M vs 250/500 mM NaCl).
- In yeast, GAL4-BD fusions of full-length C3H14 and its N-terminal 237 residues
  transactivate; the TZF domain alone does not.
- c3h14 c3h15 stems: "a significant reduction in secondary wall thickness of fibres or
  vessels"; "the cellulose, xylose, and lignin contents were visibly decreased". The
  double mutant "is taller than the wild type". Single mutants resemble wild type.
- Alleles: c3h14 GABI_239E11; c3h15-1 SALK_045897; c3h15-2 SALK_065040.

### Xue 2026 (PMID:41758611)
- ProC3H14::C3H14-VENUS in MMCs: weaker than C3H15-VENUS "but showed a similar
  pattern" (diffuse cytoplasm and nucleus, plus variable-sized cytoplasmic foci).
- DCP1 colocalization (~80% of DCP1 foci), BiFC, pull-down, FRET-FLIM and FRAP were all
  done with **C3H15 only**.
- RNA affinity purification used C3H15 protein: 2,480 targets, "C3H15 primarily binds to
  the coding region of mRNA (96%)". C3H14 was not tested. The abstract's "they bind
  highly expressed mRNAs" therefore rests on C3H15 data.
- c3h14/15 double mutant: RNA accumulates in MMC nuclei and cytoplasm at stage 5,
  meiosis arrests at pachytene, R-loops and gammaH2AX increase. C3H15-VENUS complements.
- Consequence for the review: P-body remains unproposed for C3H14. The GO:0061158 NEW
  row rests on C3H14's own 3'-UTR data (PMID:25228083, PMID:42844995) plus genetic
  requirement in meiocytes.

### Still not accessible
PMID:42711403 (Nat Plants 2026), PMID:32279333 (PCE 2020), PMID:19674407 (Plant J 2009).

## 2026-10-23 session 3: PR review follow-up (PR 5344)

- "Chai et al., 2022", which PMID:35736512 cites (with Chai 2015) for C3H14/15
  recognition of G-rich CHRE elements, is PMID:35139225 (Chai et al. 2022 Plant Physiol,
  "The CCCH zinc finger protein C3H15 negatively regulates cell elongation by inhibiting
  brassinosteroid signaling"). Its abstract describes C3H15, not C3H14: "The
  dephosphorylated C3H15 protein accumulates in the nucleus, where C3H15 regulates
  transcription via G-rich elements (typically GGGAGA)". It was not added to the review's
  references because it has no C3H14-specific data. It is the origin of the CHRE motif
  used in PMID:35736512 and is relevant to the paralog question about how a TZF protein
  discriminates DNA from RNA targets.
- Added NEW GO:0010113 negative regulation of systemic acquired resistance (IMP,
  PMID:35736512). It is a sibling of GO:1900425 under GO:0031348 (checked in the OLS4
  hierarchy).
- Expanded the reason for not using GO:0035925, and hedged the description's statement
  of the promoter-binding role.
- TAIR curator decision (2026-10-23, this session): the sign of the TAIR IMP row
  GO:1901347 (PMID:25228083) is wrong. The correction for TAIR is to re-point it to
  GO:2000652 regulation of secondary cell wall biogenesis, with the relation
  acts_upstream_of_or_within_positive_effect (RO:0004032), rather than to GO:1901348.
  Recorded as two source_defects (GO_ID and Qualifier) on that row. The review's own
  proposed replacement stays GO:1901348, because review replacement terms carry no
  relation. The suggested question asking whether to re-point the row was removed as
  answered. Checked in OLS4: GO:2000652 is the parent of GO:1901347 and GO:1901348.
