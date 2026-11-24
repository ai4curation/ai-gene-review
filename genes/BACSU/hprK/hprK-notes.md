# hprK (O34483) notes

## Literature search (2026-11-24)

- PubMed queries: `HPr kinase/phosphorylase Bacillus subtilis pyrophosphate` (5 hits:
  PMID:12779331, 12359880, 16717408 [G. stearothermophilus], 17878158 [L. casei
  structure], 12359875 [L. casei/B. subtilis HPr complex structure]) and
  `hprK Bacillus subtilis catabolite repression kinase Reizer` (PMID:12055300).
- Swiss-Prot reference list checked; B. subtilis primary papers cached with
  `just fetch-pmid`: PMID:9570401, 12009882, 12055300, 12359880, 12411438, 12779331
  (all abstract-only in cache). PMID:25278935 (GOA protein-binding source) already cached.
- No deep-research provider file was generated.

## Findings

- HPrK/P (PtsK) of B. subtilis is a novel-family Ser/Thr protein kinase that
  phosphorylates HPr; allosterically activated by FBP, inhibited by Pi; ptsK mutant
  loses catabolite repression [PMID:9570401 "In contrast to wild-type B. subtilis, the
  ptsK mutant is insensitive to transcriptional regulation by catabolite repression."].
- Dephosphorylation of P-Ser-HPr is a phosphorolysis producing PPi, not hydrolysis;
  reversible [PMID:12359880 "We demonstrate here that P-Ser-HPr dephosphorylation
  leads to the formation of HPr and pyrophosphate."].
- B. subtilis HprK/P has three activities (ATP-kinase, PPi-kinase, phosphorylase), all
  mediated by the P-loop [PMID:12779331 "participate in the three enzymatic activities
  of HprK/Ps (ATP-kinase, PP(i)-kinase, and phosphorylase)"].
- Divalent cations essential for both activities; hexamer at physiological pH; also
  acts on Crh [PMID:12411438, PMID:12009882].
- Kinase+phosphatase-dead mutant abolishes CCR [PMID:12055300 "Carbon catabolite
  repression was abolished in a B. subtilis strain expressing a mutant form of HPrK/P
  deficient in kinase and phosphatase activities."].

## Staged RHEA rows

- RHEA:46604 ([HPr]-O-phospho-L-serine + phosphate + H+ = [HPr]-L-serine + PPi) ->
  broadMatch GO:0016776 phosphotransferase activity, phosphate group as acceptor.
  Chemistry: Pi attacks the phosphoserine phosphoryl, forming PPi; no water is
  consumed, so this is a phosphoryl transfer to phosphate (EC 2.7.4.-), and GO:0016776
  is the right class. There is no GOA row for it on O34483; this review adds it as NEW
  (IDA, PMID:12779331 / PMID:12359880). This backs the staged row.
- RHEA:46600 (ATP kinase) maps to GO:0106310 via GOA's existing Rhea2GO row (accepted).
- RHEA:48580, 60648, 60652, 60700, 60704 are NOT HPrK reactions: 48580 is the PpsR
  [PEP synthase]-phosphate phosphorylase; 60648/60652/60700/60704 are sphingomyelinase
  D / lysophospholipase D cyclic-phosphate-forming reactions.

## Annotation problems

- GO:0000155 / GO:0000160 (phosphorelay sensor kinase / phosphorelay signal
  transduction) from InterPro2GO on the HPrK/P family signatures are wrong: those terms
  describe two-component His-Asp phosphorelays. HPrK/P is a P-loop Ser kinase /
  phosphorylase; the historical description of it as the "sensor in a multicomponent
  phosphorelay" (PMID:9570401) uses phosphorelay loosely.
