# nuoN (E. coli K-12, P0AFF0) notes

## 2026-10-23 review (Claude Code)

Deep-research providers are unavailable in this environment (no API keys), so the
literature was reviewed manually from cached `publications/PMID_*.md` files and the
UniProt record (most cached papers abstract-only; PMID:9495756 and PMID:18316732
full text).

- nuoN deletion abolishes complex I activity [PMID:12718520 "the gene for subunit N
  was disrupted by a 163 bp deletion in the chromosome, resulting in the loss of
  Complex I function, as measured by deamino-NADH oxidase activity"]; point mutants
  reduce proton translocation and show enhanced decylubiquinone inhibition
  [PMID:12718520 "These mutants also showed enhanced inhibition by decylubiquinone,
  indicating that subunit N interacts with quinones."]. No quinone-binding GO row
  exists for NuoN; not proposed (the effect may be indirect).
- Lys395 participates in proton translocation [PMID:23864658 "Our mutation study on
  NLys(395) suggests that this residue participates in the proton translocation."].
- GO:0050136 (non-electrogenic NADH:quinone oxidoreductase) REMOVED: contradicts the
  electrogenic NDH-1 [PMID:3122832 "an enzyme (NADH dh II) that reacts with NADH
  exclusively whose turnover does not lead to generation of a H+ electrochemical
  gradient"]; NDH-1 is the proton-pumping enzyme (GO:0008137, RHEA:29091).
- GO:0003954 -> GO:0008137; GO:0016020 -> GO:0005886; GO:0030964 -> GO:0045271.
- PANTHER: UniProt DR line gives PTHR22773 without subfamily; PANTHER 19.0 e_coli
  classification places P0AFF0 in PTHR22773:SF41 (NADH-UBIQUINONE OXIDOREDUCTASE
  CHAIN 2).
- Validation: `just validate ECOLI nuoN` zero warnings/errors.
