# hsp104 review notes

## 2026-10-09 fungal PAINT-family review

- Reviewed `SCHPO/hsp104` as the fission-yeast member of the fungal cytosolic
  Hsp104 branch. PAINT places `GO:0005829`, `GO:0051087`, `GO:0042026`,
  `GO:0043335`, and `GO:0070370` on `PANTHER:PTN007521008`; those IBAs were
  accepted because the target lies in that cytosolic Hsp104 subtree rather than
  the mitochondrial Hsp78 subtree.

- Deep-research provider generation failed because `uvx` attempted to write its
  managed tool environment under read-only `~/.local/share/uv/tools`. No
  `hsp104-deep-research-*.md` provider file was hand-written. I used cached GOA
  publications plus a 2026-10-09 live newer-paper search instead.

- The key direct hsp104 paper shows that fission-yeast hsp104 is heat induced,
  required for thermotolerance, and a conserved disaggregase [PMID:19759825,
  "As its S. cerevisiae counterpart, Sp_hsp104(+) is heat-inducible and
  required for thermotolerance in S. pombe."].

- Coelho et al. used Hsp104-associated aggregates to follow stress damage in
  fission yeast [PMID:24035542, "Cell death correlated with the inheritance of
  Hsp104-associated protein aggregates."], and the later aggregate-fusion paper
  explicitly imaged Hsp104-associated aggregates in vivo [PMID:24936793, "by
  combining in vivo imaging of Hsp104-associated aggregates, a form of damage,
  with mathematical modeling"]. These support the direct aggregate and
  disaggregase rows.

- Oberti et al. support the Hsp104 response to misfolded proteins and
  nuclear/cytoplasmic deployment [PMID:25543137, "In the absence of Hsp104,
  Dicer accumulates in cytoplasmic inclusions and heterochromatin becomes
  unstable at elevated temperatures"].

- The `GO:0030163 protein catabolic process` row from the Sdj1-L169P paper was
  kept as non-core. Hsp104 is required for efficient degradation of that
  aggregate-prone substrate, but the direct Hsp104 role is disaggregation
  upstream of proteasomal clearance [PMID:26152728, "Hsp104 and Hsp70-type
  chaperones are required for efficient degradation of Sdj1-L169P."].

- The ORFeome `nuclear envelope` call and the `nucleolar peripheral inclusion
  body` row were left `UNDECIDED`. The former is abstract-only and does not
  expose the exact Hsp104 localization entry. The latter shows Hsp104-dependent
  NuR disaggregation [PMID:33176152, "NuRs disaggregate, and their components
  relocate to their functional environments in an Hsf1- and Hsp104-dependent
  manner"], but the abstract does not explicitly say that Hsp104 localizes at
  NuRs.
