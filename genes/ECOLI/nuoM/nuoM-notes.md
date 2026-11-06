# nuoM (E. coli K-12, P0AFE8) notes

## 2026-10-23 review (Claude Code)

Deep-research providers are unavailable in this environment (no API keys), so the
literature was reviewed manually from cached `publications/PMID_*.md` files and the
UniProt record. Most cached papers are abstract-only; full text was available for
PMID:9495756, PMID:18316732 and PMID:23417064.

- NuoM is a 14-TM antiporter-like membrane-arm subunit (ND4 homologue)
  [PMID:21822288 "The fold of the homologous antiporter-like subunits L, M and N is
  novel"; "Each repeat includes a discontinuous transmembrane helix and forms half of
  a channel across the membrane."].
- Conserved NuoM residues are required for coupled activity [PMID:18590697 "The
  quinone reductase activity was practically lost in K234A, K234R and E144A"].
- NuoL/M/N likely pump by a common mechanism [PMID:23864658 "It seems likely that
  NuoL, NuoM, and NuoN pump protons by a similar mechanism."]; turnover cryo-EM
  proposes protons exit only via NuoL [PMID:36104567 "This mechanism explains why
  protons exit exclusively from the NuoL subunit"]. Open question recorded.
- Ubiquinone binding (IBA + IDA PMID:12730198): azido-Q labelled NuoM
  [PMID:12730198 "subunit NuoM was heavily labeled, suggesting that this protein houses
  the Q-binding site"], but structures put the quinone site at Nqo4/6/8 and "there are
  no cofactors in the membrane" [PMID:23417064]. Marked MARK_AS_OVER_ANNOTATED on
  both rows (not removed: the labelling result itself stands).
- GO:0003954 rows MODIFY -> GO:0008137 (descendant already carried);
  GO:0016020 -> GO:0005886; GO:0030964 -> GO:0045271. Aerobic respiration kept as
  non-core context. Note nuoM insertion alleles in PMID:9495756 were polar on nuoN.
- Validation: `just validate ECOLI nuoM` zero warnings/errors (run with
  `env -u UV_NATIVE_TLS` to suppress an environment-only uv deprecation warning).
