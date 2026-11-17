# fadE review notes

## 2026-11-06: complete strain168 review

Pristine seed captured before edits in bacillus-review/fadE-baseline.json. Every original annotation payload is retained; no new GO rows were necessary. Official identity and frozen UniProt agree on strain168 and the historical locus synonym. All rows, including broad molecular functions and the FadA phenylacetate/localization uncertainties, were assessed.

Default Falcon was genuinely attempted and failed with HTTP403 authentication failure; this is manual research, with no fabricated provider report. Normal PAINT loss screening reported no IRD/IKR on this lineage. Current GO reaction definitions were checked through QuickGO.

FadE (YusJ) is a FAD-dependent acyl-CoA dehydrogenase contributing to fatty-acid beta-oxidation in Bacillus subtilis 168. Native genetic evidence links it to palmitate utilization and an ETF-dependent pathway; the exact electron-transfer partner of the isolated enzyme remains unresolved. Its expression is controlled by FadR.

PMID:17189250 cached abstract was preserved. Author-uploaded full text was inspected independently: palmitate genetics uses 168-derived pMUTIN strains and IPTG to induce downstream genes. It does not measure purified FadE-to-ETF chemistry or target chain-length kinetics. See shared BACSU/fadE/fadE-source-analysis/primary-scope.md. The 2011 FadB direct study is DOI10.1007/s13213-010-0121-5; its institutional PDF and short scoped evidence distinguish strain168 DNA from recombinant BL21 expression. No isolated FadN assay was found. Its hydratase domain is explicitly retained as an additional capability hypothesis rather than declared absent.

## 2026-11-06 — PR6136 native ETF inference

Accepted the ETF-linked activity as an inference from convergent yusJ/etfAB regulation and growth phenotypes plus protein identities. Direct purified-protein transfer is not a universal acceptance requirement. This does not assign a whole substrate range from palmitate growth or resolve the other bacterial relays.
