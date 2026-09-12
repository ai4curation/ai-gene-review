# GAD1 (Q99259) review notes

Deep research: falcon provider was OUT OF CREDITS (HTTP 402) at review time, so no
`GAD1-deep-research-falcon.md` was generated. This review is grounded in the UniProt
record (`GAD1-uniprot.txt`), the seeded GOA (`GAD1-goa.tsv`), and cached
`publications/PMID_*.md`.

## Identity / core biology

- GAD1 = glutamate decarboxylase 1, a.k.a. GAD67 / 67 kDa glutamic acid decarboxylase
  (UniProt DCE1_HUMAN, Q99259; HGNC:4092; chromosome 2q31).
- Pyridoxal-5'-phosphate (PLP)-dependent enzyme; EC 4.1.1.15; group II decarboxylase
  family. PLP is covalently bound at Lys405 (N6-(pyridoxal phosphate)lysine)
  [GAD1-uniprot.txt FT MOD_RES 405].
- Catalyzes L-glutamate -> 4-aminobutanoate (GABA) + CO2 (RHEA:17785)
  [GAD1-uniprot.txt CATALYTIC ACTIVITY].
- GAD67 is the **constitutively active** isoform responsible for basal GABA production;
  the paralog GAD2/GAD65 is the synaptic-vesicle-associated form that is transiently
  activated on demand [PMID:17384644 abstract: "GAD67 is constitutively active and is
  responsible for basal GABA production. In contrast, GAD65 ... is transiently
  activated"].
- Homodimer [GAD1-uniprot.txt SUBUNIT; PMID:17384644].
- Localization: cytosolic (neuronal). Note GOA cytoplasm (IBA) and Reactome CC terms
  (plasma membrane, clathrin-sculpted GABA transport vesicle membrane, vesicle
  membrane) describe pathway/vesicle-context localization rather than the enzyme's own
  soluble cytosolic activity; GAD67 lacks the N-terminal palmitoylation-based membrane
  anchoring that targets GAD65 to vesicles.

## Structure / mechanism references (cited in UniProt)

- PMID:17384644 (Fenalti 2007, Nat Struct Mol Biol): crystal structures of GAD67 &
  GAD65; GAD67 has a tethered catalytic loop covering the active site sustaining GABA
  production. Provides CATALYTIC ACTIVITY, COFACTOR (PLP), SUBUNIT (homodimer), FUNCTION.
  Source of IDA for glutamate decarboxylase activity, GABA shunt, identical protein binding.
- PMID:23126365 (Langendorf 2013): GAD auto-activation structure. Not in GOA/references
  list; not cited.
- PMID:10671565 (Chessler & Lernmark 2000): describes GAD25 (isoform 3), a
  catalytically **inactive** splice variant in non-neural tissue; establishes GAD67
  enzymatic activity and L-glutamate catabolic role. Note isoform 3 = enzymatically
  inactive; the IDA glutamate decarboxylase / L-glutamate catabolic annotations refer
  to full-length GAD67 (isoform 1).

## Disease

- Bi-allelic GAD1 variants -> developmental and epileptic encephalopathy 89 (DEE89,
  MIM:619124), autosomal recessive [PMID:32282878, cited in UniProt; not cached].
- Homozygous missense S12C associated with autosomal recessive spastic cerebral palsy
  [PMID:15571623, cited in UniProt; not cached]; note PMID:33634263 later attributes
  CPSQ1 to HPDL, so the cerebral-palsy attribution is caveated. Consistent with GAD1's
  role in supplying the major inhibitory neurotransmitter GABA.

## GOA annotation assessment summary

- MF glutamate decarboxylase activity (GO:0004351): CORE. Supported by IDA (PMID:17384644,
  PMID:10671565), IBA, and IEA(ARBA EC 4.1.1.15 / RHEA:17785). ACCEPT.
- MF pyridoxal phosphate binding (GO:0030170) IEA(InterPro): CORE cofactor. ACCEPT
  (PLP is the essential cofactor, Lys405 Schiff base).
- MF carbon-carbon lyase / carboxy-lyase (GO:0016830 / GO:0016831) IEA(InterPro):
  correct parents of glutamate decarboxylase activity but less informative; MARK_AS_OVER_ANNOTATED.
- BP GABA biosynthetic process (GO:0009449) IBA + IEA: CORE. ACCEPT.
- BP GABA shunt (GO:0006540) IDA/TAS/IEA: KEEP (metabolic-context process); the IDA
  (PMID:17384644) reflects the decarboxylation step feeding the shunt.
- BP L-glutamate catabolic process (GO:0006538) TAS(PMID:10671565): ACCEPT as broader
  correct process (glutamate is consumed).
- BP chemical synaptic transmission (GO:0007268) TAS: KEEP_AS_NON_CORE — downstream
  physiological role via GABA, not GAD1's own molecular action.
- CC cytoplasm (GO:0005737) IBA: ACCEPT (soluble/cytosolic enzyme).
- CC presynaptic active zone (GO:0048786) IBA: KEEP_AS_NON_CORE (mostly GAD65-context;
  GAD67 basal cytosolic, only partly synaptically localized).
- CC plasma membrane (GO:0005886) TAS Reactome, vesicle membrane (GO:0012506) NAS,
  clathrin-sculpted GABA transport vesicle membrane (GO:0061202) TAS: these are Reactome
  pathway-context / vesicle-membrane placements; GAD67 (unlike palmitoylated GAD65) is
  soluble cytosolic, so these overstate GAD67's own localization. MARK_AS_OVER_ANNOTATED.
- MF protein binding (GO:0005515) IPI x11: all from large-scale interactome / SH3-array /
  variant-interactome screens (PMID:16189514, 17474147, 21516116, 25416956, 26871637,
  31515488, 32296183) and one small-scale (PMID:10671565). Uninformative bare
  `protein binding`; per policy MARK_AS_OVER_ANNOTATED (not REMOVE).
- MF identical protein binding (GO:0042802) IDA (PMID:17384644): supports the homodimer;
  ACCEPT (structurally verified homodimer).
</content>
