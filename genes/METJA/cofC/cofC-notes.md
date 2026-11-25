# cofC (MJ0887, Q58297) notes

## Literature search (2026-11-07)

Deep-research providers were unavailable for this session. Searches run:
WebSearch "Bashiri 2019 revised biosynthetic pathway cofactor F420
phosphoenolpyruvate CofC FbiD Methanocaldococcus"; WebSearch "Braga 2019
Paraburkholderia rhizoxinica CofC Methanocaldococcus jannaschii CofC
2-phospho-L-lactate 3-phospho-D-glycerate substrate specificity"; QuickGO
annotation API for Q58297 (to check for annotation extensions on the NOT row;
none present). Papers cached and read: PMID:18260642 (abstract only),
PMID:30952857 (full text), PMID:31469543 (abstract only), PMID:35038903
(full text).

## Biology

- MJ0887 was identified bioinformatically and shown to make LPPG from
  2-phospho-L-lactate (LP) and GTP [PMID:18260642 "the purified protein was
  found to catalyze the formation of lactyl-2-diphospho-5'-guanosine from LP
  and GTP"]. Kinetics: Vmax 3 umol/min/mg, Km(GTP) 56 uM, Km(LP) 36 uM
  [PMID:18260642]. Named CofC for the third step of F420 biosynthesis
  [PMID:18260642 "The MJ0887 gene product has been designated CofC to indicate
  its involvement in the third step of coenzyme F 420 biosynthesis."].
- UniProt (curated, ECO:0000269 PubMed:18260642): homodimer; also uses ATP,
  dGTP, ITP more weakly; no lactate kinase activity; thermostable.
- Bashiri et al. 2019 (Nat Commun) assayed Mj-CofC coupled to Mtb-FbiA (a
  non-cognate CofD) and saw no product from 2-PL, but did see dehydro-F420-0
  from PEP [PMID:30952857 "We then tested whether Mtb-FbiA and CofC from
  Methanocaldococcus jannaschii (Mj-CofC) could catalyze F420-0 formation under
  the same conditions, which again yielded no product"; "both Mtb-FbiD and CofC
  from Methanocaldococcus jannaschii (Mj-CofC) enzymes use PEP to produce
  dehydro-F420-0"]. They attributed the earlier 2-PL result to PEP/pyruvate
  kinase in the Grochowski assay [PMID:30952857 "this discrepancy is most likely
  due to the supplementation of the coupled CofC/CofD reaction in these studies
  with pyruvate kinase and 2 mM PEP"].
- Braga et al. 2019 (Lackner lab) found a CofC specificity switch to
  3-phospho-D-glycerate in Paraburkholderia [PMID:31469543 "a specificity
  switch in the guanylyltransferase CofC reprogrammed the pathway to start from
  3-phospho-d-glycerate"]; per Hasan 2022 that study also found 2-PL to be the
  best substrate of Mj-CofC (Braga full text not cached; claim taken from
  Hasan 2022).
- Hasan et al. 2022 (mBio) resolved the conflict: CofD/FbiA partner choice
  controls which CofC product is captured; Mtb-FbiA only takes EPPG, so the
  Bashiri assay missed 2-PL activation [PMID:35038903 "Since Mjan-CofC can
  accept PEP as a minor substrate when combined with its cognate CofD (22), the
  assay resulted exclusively in DF420-formation when combined with FbiA, thus
  erroneously suggesting that 2-PL was not accepted by CofC."; "reestablished
  2-PL as the most likely starting point of F420 biosynthesis in archaea"].

## The NOT row

GOA has, for GO:0043814 phospholactate guanylyltransferase activity, both a
positive IDA and a NOT|enables IDA, both assigned by UniProt on 2010-09-29 and
both citing PMID:18260642, with no extensions (QuickGO checked). A third,
positive IDA from MENGO (2013) cites the same paper. The NOT row predates
Bashiri 2019 (so it cannot reflect the PEP debate) and negates exactly the
activity the cited abstract reports. The same paper reports no lactate kinase
activity (UniProt FUNCTION), which is a plausible source of a mis-keyed negation,
but the intended term cannot be seen. Conclusion: positive and NOT rows cannot
both stand; the positive is supported by PMID:18260642 and re-established by
PMID:35038903; the NOT row is REMOVE with a source defect for UniProt (CHECK).
The later evidence that would superficially support a NOT (PMID:30952857) is
recorded as a DISPUTED finding superseded by PMID:35038903.

## GO terms

- No GO MF term exists for PEP guanylyltransferase (EC 2.7.7.105, RHEA:30519) or
  3-phospho-D-glycerate guanylyltransferase (EC 2.7.7.106, RHEA:63440); children
  of GO:0070568 checked in OLS. PEP activity is minor for Mj-CofC, so it is not a
  core function, but the NTR is proposed for FbiD-type enzymes.
- GO:0052645 F420-0 metabolic process has no biosynthetic child; it is the most
  specific BP available.
