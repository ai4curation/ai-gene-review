# ndx-4 (Y37H9A.6, Q9U2M7) review notes

## Summary of evidence

- Asymmetrical Ap4A hydrolase (Nudix family), the worm counterpart of human NUDT2.
  [PMID:11738085 "It hydrolyses Ap4A with a K(m) of 7 microM and k(cat) of 27 s(-1) producing AMP and ATP as products."]
- Activity also present in adult worm extracts.
  [PMID:11738085 "Asymmetrically cleaving diadenosine 5',5\"'-P(1),P(4)-tetraphosphate (Ap4A) hydrolase activity has been detected in extracts of adult Caenorhabditis elegans"]
- Broad (di)adenosine polyphosphate substrate range (>=4 phosphates), not Ap3A; ATP is always a product.
  [PMID:11738085 "always generating ATP as one of the products"]
- Crystal structures (free, 2.0 A; binary complex, 1.8 A); monomer with Nudix fold.
  [PMID:11937063 "The structures reveal that the enzyme has the mixed alpha/beta fold of the Nudix family"]
- Mutagenesis: Glu56, Glu52, Glu103 catalytic; P1/P4 phosphate contacts sufficient for binding.
  [PMID:12475970 "interactions with the P(1)- and P(4)-phosphates are minimum and sufficient requirements for substrate binding"]
- Secondary in vitro PRPP pyrophosphatase activity using the same active site.
  [PMID:12370170 "Active site mutants of the Caenorhabditis elegans diadenosine tetraphosphate hydrolase had no activity, confirming that the same active site is responsible for nucleotide and PRPP hydrolysis."]

## Curation decisions

- AMP/ADP/ATP biosynthetic process: products of a catabolic reaction; marked over-annotated
  in favour of GO:0015967 diadenosine tetraphosphate catabolic process.
- Apoptotic process (TAS, PMID:11937063): the sentence is speculative ("potentially") background
  in a structure paper; removed.
- Ribose phosphate metabolic process: in vitro family screen only; authors did not consider
  PRPP significant for Ap4A hydrolases; over-annotated. PRPP pyrophosphatase MF kept as non-core.
- No cellular component annotations exist and no localization data were found; none proposed.

## Caveats

All four cached publications are abstract-only (`full_text_available: false`).

## Deep research status

The falcon run (with perplexity-lite fallback) failed on 2026-10-08: falcon timed out
after 600 s and perplexity was not configured. OpenScientist then succeeded
(`ndx-4-deep-research-openscientist.md`, ~19 min).

OpenScientist found no ndx-4 literature beyond the four GOA papers plus the
crystallisation report (PMID:11856844). Points it adds are orthologue-based only and do not
change any curation decision:

- Drosophila Apf (the fly Ap4A hydrolase) is predominantly nuclear [PMID:17344088, per
  deep research]; NDX-4 localisation is untested, so no CC annotation is proposed.
- Human NUDT2 degrades Ap4A in activated mast cells, affecting MITF/USF2 targets
  [PMID:18644867, per deep research]; a mammalian signalling context, not evidence for worm
  processes.
- It agrees that PRPP is a minor secondary substrate and that the apoptosis link is a
  hypothesis from the Ap3A/Ap4A-ratio model rather than an ndx-4 finding.

## 2026-10 update: 8-oxo-dGTP hydrolysis and in vivo data (three papers missing from the first pass)

A PubMed search (ndx-4, Y37H9A.6, MutT/Nudix + C. elegans) found three ndx-4 papers that the
first review and the OpenScientist deep-research run both missed: PMID:21111690 (Arczewska et
al., DNA Repair 2011, issue date; e-pub Dec 2010), PMID:24435662 (Sanada & Zhang-Akiyama,
Mutagenesis 2014) and PMID:24347047 (Chatterjee et al., Environ Mol Mutagen 2014).

### Arczewska et al. 2010/2011 (PMID:21111690), full text read from a PDF supplied by the curator

The paper is paywalled (Elsevier) and not in PMC, so its full text is not cached in
`publications/` (which holds only the abstract). The excerpts below are verbatim from the PDF,
with line-break hyphenation removed.

- Only NDX-4 among the cloned worm Nudix proteins (including NDX-2) hydrolysed 8-oxo-dGTP:
  "Of the remaining constructs, only extract from the clone overexpressing NDX-4 hydrolyzed 8-oxodGTP"
- Both 8-oxo-dGMP + PPi and 8-oxo-dGDP + Pi are formed:
  "NDX-4 possesses 8-oxodGTP phosphatase and pyrophosphohydrolase activities, producing both 8-oxodGDP and inorganic phosphate as well as 8-oxodGMP and pyrophosphate as products."
- Weak discrimination against unoxidised dNTPs:
  "Similarly to Arabidopsis thaliana AtNUDT1, NDX-4 does not show a strong preference for 8-oxodGTP and is able to hydrolyze unmodified dATP and dGTP with comparable efficiency."
- Kinetics (Table 1, transcribed; Ap4A values are cited from PMID:11738085):

  | Substrate | Km (uM) | kcat (s-1) | kcat/Km (s-1 M-1) |
  |---|---|---|---|
  | Ap4A | 7 | 27 | 3.9 x 10^6 |
  | 8-oxo-dGTP | 98.6 +/- 29.6 | 0.58 +/- 0.14 | 5.9 x 10^3 |
  | dGTP | 182.0 +/- 23.7 | 0.53 +/- 0.06 | 2.9 x 10^3 |
  | 2-oxo-dATP | 384.6 +/- 67.1 | 0.51 +/- 0.44 | 1.3 x 10^3 |
  | dATP | 114.3 +/- 5.3 | 0.37 +/- 0.03 | 3.3 x 10^3 |

  So Ap4A is hydrolysed about 660-fold more efficiently than 8-oxo-dGTP, and 8-oxo-dGTP is
  preferred over dGTP only about 2-fold.
- Complementation: "Hence, NDX-4 is a functional homologue of E. coli MutT."
- Worm extracts, with worms grown on mutT-deficient E. coli and extracts ultrafiltered to exclude
  bacterial MutT and nonspecific phosphatases:
  "The 8-oxodGTPase activity was significantly decreased in crude extracts from the ndx-4 mutant, with 1.28 ± 0.14 pmol 8-oxodGTP hydrolyzed per min/μg protein compared to 2.26 ± 0.08 pmol/min/μg protein in wild type C. elegans"
  The residual activity in the mutant "predominantly generated 8-oxodGDP" and its source is unknown.
- Genomic 8-oxo-dG: section heading "8-oxodG levels in DNA are not increased in the ndx-4 mutant".

### Sanada & Zhang-Akiyama 2014 (PMID:24435662), PMC full text (cached)

Table I (transcribed from the PMC article; 20 uM substrate, NDX-1 0.73 uM, NDX-2 5 uM,
NDX-4 1.51 uM, 37 C, 30 min; "-" means <5% hydrolysis):

| Substrate | NDX-1 | NDX-2 | NDX-4 |
|---|---|---|---|
| dGDP | - | 66.4% | - |
| dGTP | - | - | 24.0% |
| 8-oxo-dGDP | 62.7% | 54.4% | - |
| 8-oxo-dGTP | - | - | 59.5% |
| GDP | - | 5.40% | - |
| GTP | - | - | 33.7% |
| 8-oxo-GDP | 63.2% | 25.2% | - |
| 8-oxo-GTP | 10.5% | - | 34.3% |

- NDX-4 acts only on triphosphates. 8-oxo-GTP and GTP are hydrolysed equally (34.3% vs 33.7%),
  and the product from 8-oxo-GTP is 8-oxo-GDP. That matches the GO:0008413 definition
  (8-oxo-GTP + H2O = 8-oxo-GDP + phosphate), but with no discrimination against GTP it is not
  proposed as an annotation; it is raised as a suggested question instead.
- ndx-4(ok1003) adults are more sensitive to menadione bisulphite, and ndx-1/ndx-2 double RNAi
  makes this worse: [PMID:24435662 "Double knockdown of ndx-1 and ndx-2 in ndx-4 mutants resulted in significantly lower survival, suggesting that NDX-1, NDX-2 and NDX-4 co-ordinately participate in sanitisation of the nucleotide pool."]

### Chatterjee et al. 2014 (PMID:24347047), abstract only

Silver-nanoparticle exposure changes NDX-4 expression and 8-oxo-GTPase activity and the survival
of ndx-4(ok1003); loss of pmk-1 makes this worse. Abstract only; the full text was not obtained,
so it is cited as corroboration only.

### Curation decisions from this update

- NEW MF GO:0035539 8-oxo-7,8-dihydrodeoxyguanosine triphosphate pyrophosphatase activity
  (IDA, PMID:21111690). The definition (8-oxo-dGTP -> 8-oxo-dGMP + PPi) matches one of the two
  measured product pairs, and activity is measurable and partly ndx-4-dependent in worm
  extracts. It is non-core: catalytic efficiency is about 660-fold below Ap4A, and
  discrimination against dGTP is about 2-fold.
- No process term is proposed. "Nucleotide-pool sanitisation" rests on survival under oxidative
  stress and mutT complementation in E. coli. Those show that the activity can matter, not
  what NDX-4 does in the worm, and 8-oxo-dG in DNA is not raised in the mutant.
- The description no longer says that no in vivo phenotype has been reported.
- The Bailey 2002 phrase "dinucleoside tetraphosphate, but not triphosphate" refers to
  dinucleoside triphosphates (Ap3A), not mononucleoside triphosphates such as dGTP; the
  reference finding wording was corrected.

### OpenScientist hypothesis run (2026-10-09)

`ndx-4-hypotheses/ndx-4-8oxo-dgtp-sanitiser/openscientist.md`. Verdict: "Partially
supported — with the specific 'MutT-type sanitiser' framing over-annotated." Checked against
primary data:

- Agreed: the base pocket is adenine-stacking. Recomputed from PDB 1KTG coordinates: the
  nearest atoms to the bound AMP base are Tyr121 CG 3.34 A (C6), Tyr76 CZ 3.36 A (N7) and His31
  CD2 3.59 A (C8).
- Agreed: NDX-4 is a NUDT2-type enzyme, not a MutT/MTH1 orthologue.
- Rejected: its reading of PMID:11937063 as evidence against triphosphate substrates (see above).
- Rejected: its lead to add GO:0006281 DNA repair; nucleotide-pool hydrolysis is not DNA repair,
  and the support is necessity-type evidence.
- It said kinetics were missing; Arczewska Table 1 supplies them (the run did not read that paper's full text).
