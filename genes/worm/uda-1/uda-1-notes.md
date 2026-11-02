# uda-1 (Q9XU84, K08H10.4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: uda-1 is the experimentally characterised SF127 co-member of the fly NTPase
(O76268). This review is written for the worm gene in its own right; ProtNLM2 output
was not opened or used.

### Deep research

`just deep-research-falcon worm uda-1 --fallback perplexity-lite` failed for both
providers on 2026-10-21: falcon returned `403 Forbidden` at the Edison auth endpoint
(`Failed to authenticate`), and the perplexity-lite fallback returned
`401 insufficient_quota`. No deep-research file exists. The review is based on the
cached primary paper (abstract only), the curated UniProt record and PANTHER membership.

Europe PMC search for `"uda-1" OR K08H10.4` with elegans found no other paper that
characterises UDA-1 itself. APY-1 (PMID:18216284) is a separate worm UDP/GDPase from
a different family (Scan-1/CANT1 homolog), not a GDA1/CD39 paralog of uda-1.

### What is experimentally established in C. elegans (PMID:15102851, abstract only; Swiss-Prot curated text)

- Activity: UDA-1 is a cation-dependent UDP/GDPase: [PMID:15102851 "UDA-1, is a UDP/GDPase encoded by the gene uda-1"].
  UniProt (ECO:0000269 from PMID:15102851) says it "Hydrolyzes UDP and GDP but not any other nucleoside di-, mono- or triphosphates";
  Km 180 uM for UDP with 10 mM Ca2+; pH optimum 8.0 (UDP), 7.5 (GDP); Ca2+, Mg2+, Mn2+ cofactors.
  So, unlike fly NTPase (UDP = GDP = IDP, PMID:19467631), UniProt reports that IDP is not hydrolysed by UDA-1.
- Location/topology: when expressed in S. cerevisiae it "has a lumenal active site in vesicles displaying an
  intermediate density between those of the ER and GA" [PMID:15102851]. This is heterologous; no in-worm
  localisation. Single N-terminal signal-anchor (type II), large luminal domain (UniProt FT, ECO:0000255).
  N-glycosylated at Asn300 in vivo (glycoproteomics, PMID:12754521 / PMID:17761667 via UniProt), which
  is consistent with a luminal domain.
- Regulation: uda-1 transcript induced up to 3.5-fold by heat, tunicamycin and ethanol, ire-1-dependent
  [PMID:15102851 "Up-regulation of uda-1 did not occur in ire-1-deficient mutants"].
- Physiological role: only hypothesised. Authors propose UDP -> UMP hydrolysis relieves UGGT inhibition
  and supplies UMP for UDP-Glc antiport [PMID:15102851 "We hypothesize that up-regulation of uda-1 favors hydrolysis
  of the glucosyltransferase inhibitory product UDP to UMP"]. No loss-of-function data in the abstract.

### Evolutionary placement

- PANTHER PTHR11782:SF127 "NTPASE, ISOFORM F" (UniProt DR; PTHR11782 entries CSV). Fly NTPase O76268 is in
  the same subfamily (fly UniProt DR). Human/mouse ENTPD5 are SF35 and ENTPD6 are SF99.
- The IBA rows come from PTN008981015, whose donor set includes uda-1 itself, fly NTPase, mouse Entpd5,
  rat Entpd5/Entpd6 and human ENTPD5/ENTPD6. So the PAINT node sits above the split of SF127 from
  SF35/SF99 and the UDP/GDPase activity is placed as ancestral to the whole ENTPD5/6 + SF127 clade.
  The uda-1 own IDA is one of the donor evidences (expected, not circular).
- PAINT propagated "protein N-linked glycosylation" and "UDP catabolic process" from mouse Entpd5 alone.
  Mouse ENTPD5 evidence (PMID:21074248, abstract): "ENTPD5 hydrolyzes UDP to UMP to promote protein
  N-glycosylation and folding in ER". For uda-1 this remains inferred (worm data are only the authors'
  hypothesis plus UPR induction).

### Decisions

- UDP/GDP phosphatase (IDA + IBA): ACCEPT, core.
- NDP phosphatase (IEA, RHEA/EC): MODIFY to the two specific activities (the enzyme is not a general NDPase).
- hydrolase activity (InterPro IEA): TOO_GENERAL.
- UDP catabolic process (IBA): ACCEPT, the direct consequence of UDP -> UMP hydrolysis.
- UDP metabolic process / GDP metabolic process (IDA): MODIFY to UDP catabolic / GDP catabolic process.
- protein N-linked glycosylation (IBA): KEEP_AS_NON_CORE, inferred from mouse ENTPD5 via the PAINT node;
  not tested in worm. Flagged as inferred, not established.
- cytoplasm (IBA): MODIFY to endomembrane system (luminal enzyme; cytoplasm is technically inclusive
  but the protein is an endomembrane luminal enzyme).
- endomembrane system (IEA SubCell): ACCEPT (matches curated UniProt location).
- cytoplasmic vesicle membrane (IDA): ACCEPT, deferring to the WormBase curator, with the caveat that the
  data are from heterologous expression in yeast.
- No NEW terms. ER-stress induction of the transcript is regulation of uda-1, not participation of UDA-1
  in the stress response, so "response to ER stress" is not proposed.
