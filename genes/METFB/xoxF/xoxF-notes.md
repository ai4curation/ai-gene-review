# xoxF (I0JWN7), Methylacidiphilum fumariolicum SolV — notes

## 2026-11-21: initial review

Trigger: de Bary et al. 2026, Nat Commun 17:11837 (PMID:43058125), "Lanthanide-dependent
methanotroph thrives on radioactive promethium". The cached publication is abstract-only;
the full text was read from a PDF the user supplied (not cached in `publications/`).

### Literature search

No deep-research provider file was generated for this gene. Manual search instead:
PubMed query `Methylacidiphilum fumariolicum lanthanide` (2026-11-21) returned 18 PMIDs,
all cached: 43058125, 40626421, 38269599, 37074219, 34544276, 32913059, 32631865,
32369635, 32060650, 30954577, 30908783, 30308436, 30020281, 29524328, 29453257,
28488399, 25421364, 24034209. 32913059 (hydroxylamine oxidoreductases) and 34544276
(XoxF1 of *Methylacidimicrobium thermophilum* AP8) are not about this protein.

### Key findings

- SolV growth is strictly lanthanide-dependent and its MDH is a XoxF ortholog carrying a
  lanthanide cofactor in a homodimer [PMID:24034209 "lanthanides were essential as
  cofactor in a homodimeric MDH"]. Crystal structure with Ce(3+) and PQQ (PDB 4MAE).
- SolV has no gene for Ca-MDH [PMID:30020281 "strain SolV is strictly dependent on Ln, as
  it does not possess the gene for Ca-MDH"]. So the IEA `calcium ion binding` row
  (InterPro2GO from IPR017512, the MxaF/XoxF family signature) is wrong for this protein.
- Eu-grown SolV gives an Eu-containing MDH; structure PDB 6FKW, lower catalytic efficiency
  [PMID:29524328 "ICP-MS showed 70 % incorporation of Eu in the enzyme"].
- Activity across La to Lu: only the early lanthanides (La to Gd) give high activity
  [PMID:30020281 "only the earlier lanthanides (La-Gd) promote high MDH activity"].
- Am(3+) and Cm(3+) support growth without lanthanides [PMID:37074219].
- Pm-147 supports growth as the sole lanthanide; recombinant apo-XoxF (residues 1–34,
  the signal peptide, removed) reconstituted with Pm-147 and PQQ has activity between the
  Nd and Sm forms [PMID:43058125 "Reconstituted methanol dehydrogenase of the type
  XoxF-MDH displays Pm-dependent activity precisely between the neodymium and samarium
  variants"].
- Physiological electron acceptor is the XoxG–XoxJ fusion cytochrome cGJ [PMID:30954577
  "XoxGJ functions as the direct electron acceptor of its corresponding XoxF-type MDH and
  can sustain methanol turnover"]. This supports GO:0052933 alcohol dehydrogenase
  (cytochrome c(L)) activity by direct assay, not just by Rhea mapping.
- In vitro substrate range includes C2–C6 primary alcohols (UniProt CC FUNCTION, from
  PMID:24034209); methanol Km 0.8 µM.
- Location: signal peptide 1–34 and periplasm (UniProt, curator inference); no TM segment,
  so the IEA `membrane` row is an over-propagated family mapping.

### Decisions

- Kept: periplasmic space, methanol catabolic process, GO:0052933 (IEA row, now also backed by the PMID:30954577 cytochrome cGJ assay; a separate NEW IDA row is not allowed because the term is already in GOA), GO:0016614.
- Removed: calcium ion binding (lanthanide, not Ca), membrane (soluble periplasmic).
- `oxidoreductase activity` (ARBA): TOO_GENERAL, entailed by GO:0052933.
- New: metal ion binding IDA (lanthanide; GO has no
  lanthanide term, re-used the `lanthanide ion binding` proposal from METEA/xoxF1),
  PQQ binding IDA (PMID:24034209 structure).
