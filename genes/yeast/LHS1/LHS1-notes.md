# LHS1 review notes

## 2026-10-01 IBA/current-GOA refresh

`just fetch-gene yeast LHS1 --force` refreshed the UniProt and GOA sources from
the 2026 exports. The exact current GOA has 15 rows. One InterPro2GO row was new
in the seeded YAML:

- `GO:0005524` ATP binding, `IEA`, `GO_REF:0000002`,
  `InterPro:IPR013126` - accepted because PMID:19759005 directly showed ATP
  binding by Lhs1p.

Eight older exact source tuples are no longer live and are preserved as
`retired: true`:

- `GO:0000166` nucleotide binding, `IEA`, `GO_REF:0000043`
- `GO:0005524` ATP binding, `IEA`, `GO_REF:0000120`
- `GO:0016787` hydrolase activity, `IEA`, `GO_REF:0000043`
- `GO:0005515` protein binding, `IPI`, `PMID:19536198`
- `GO:0005515` protein binding, `IPI`, `PMID:23217712`
- three `GO:0051082` unfolded protein binding `IMP` rows from
  `PMID:10409721`, `PMID:8654361`, and `PMID:8887673`

The two IntAct `GO:0005515` rows were changed to `REMOVE`. The PMID:19536198
chaperone-interaction atlas explicitly cautions that its TAP-tag interactions
are indirect, not direct binary interactions. The PMID:23217712 row was an SSA1
interaction carried by UniProt/IntAct in the older source file, but the refreshed
UniProt record no longer has that interaction and the paper is about cytosolic
Ssa1 phosphorylation and Cln3 control rather than a specific ER Lhs1p activity.

## PAINT / IBA

PTHR45639 has two live IBA rows for LHS1:

- `GO:0000774` adenyl-nucleotide exchange factor activity is placed at
  `PANTHER:PTN002900795`, seeded by several descendants including
  `SGD:S000001556`. That SGD identifier is LHS1 itself; this is valid direct
  descendant evidence used for PAINT placement, not circular evidence.
- `GO:0034663` endoplasmic reticulum chaperone complex is placed at
  `PANTHER:PTN000452651`, the eukaryotic Grp170 node. The row is seeded by
  mouse Hyou1 but transfers cleanly to yeast Lhs1p, which is the Kar2/BiP-linked
  Grp170-family ER lumen chaperone.

Both rows were retained as core, with only the PTN nodes listed in
`propagation_review.source_entities`.

## Holdase molecular function

`GO:0051082` was the old generic unfolded-protein-binding term. It is no longer
exported for Lhs1p in current GOA, and it should not be converted into
`GO:0140662` ATP-dependent protein folding chaperone: PMID:19759005 separates
Lhs1p's nucleotide-dependent Kar2 NEF activity from a
nucleotide-independent holdase activity: "These results demonstrate that Lhs1p
can function as a nucleotide-independent holdase in vitro." PMID:10409721 also
supports direct client engagement by Cer1p/Lhs1p during pro-CPY handling:
"Together, this suggests that Cer1p has a chaperoning activity required for
proper refolding of denatured pro-CPY which is mediated by direct interaction
with the unfolded polypeptide."

The holdase core function now uses the missing proposed molecular function
`holdase chaperone activity`, with the three old `GO:0051082` rows retired and
modified to `NTR`.

## ERAD literature

The 2013 ENaC paper first connected Lhs1p/Grp170 to ERAD substrate selection:
"These data establish the first evidence that Lhs1/Grp170 chaperones can act as
mediators of ERAD substrate selection." [PMID:23645669]

The newer 2023 Biochemical Journal paper refined that model, showing that Lhs1
is needed for a subset of Hrd1-dependent, unglycosylated, two-pass membrane
substrates with orphaned or unassembled transmembrane domains: "Lhs1 is required
for a subset of ERAD substrates that also require the Hrd1 ubiquitin ligase."
[PMID:37702403]

I added a conservative `NEW` annotation to `GO:0036503` ERAD quality control
pathway. This passes the participation check: Lhs1p is the ER-lumen chaperone
helping choose and retrotranslocate a subset of misfolded membrane clients, not
the substrate being degraded. Kar2p, Jem1p, and Scj1p are useful comparators in
the same ER quality-control role and all carry ERAD annotations.
