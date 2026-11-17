# bktB (PP_3754, Q88GH0) notes

## 2026-11-11

Fetched with `just fetch-gene PSEPK Q88GH0 --alias bktB` for the
`ketone_body_oxidation` module, where BktB is the KT2440 reaction-capable
candidate for terminal acetoacetyl-CoA thiolysis.

No deep-research provider output was generated for this gene in this session;
no `-deep-research-*.md` file exists. A search of the local `publications/`
cache found no paper naming BktB, and no PP_3754-specific publication is
cited in GOA. The review therefore rests on the UniProt record's family
signatures (NCBIfam TIGR01930 and the BktB-specific NF006552, PROSITE PS00098 /
PS00099, PIRSR PIRSR000429 active-site residues) and on comparison with the
KT2440 sibling thiolase review `genes/PSEPK/pcaF`.

Decisions:

- GO:0003985 accepted as the core predicted activity (PROSITE-ProRule-backed
  EC 2.3.1.9 catalytic-activity line, TIGR01930).
- GO:0003988, GO:0016746, GO:0016747: TOO_GENERAL, entailed by GO:0003985
  (ancestry checked with the local GO sqlite via `runoak ancestors`), matching
  the pcaF-I treatment.
- GO:0033812 3-oxoadipyl-CoA thiolase: MARK_AS_OVER_ANNOTATED. Only an ARBA
  rule supports EC 2.3.1.174; the PcaF model TIGR02430 is absent and KT2440
  has a dedicated PcaF-I.

PANTHER: PTHR18919:SF107, the mixed subfamily already described in
`interpro/panther/PTHR18919/PTHR18919-review.yaml`.

The KT2440 fatty-acid beta-oxidation deep research
(`projects/P_PUTIDA/deep-research/PSEPK__fatty_acid_beta_oxidation__ppu00071-deep-research-openscientist.md`)
lists BktB among the EC 2.3.1.9 thiolases (with PP_2215, PP_3355, PP_0582 and
YqeF/PP_4636) that are not the degradative beta-oxidation thiolase, which is
consistent with leaving its in vivo role open.
