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
