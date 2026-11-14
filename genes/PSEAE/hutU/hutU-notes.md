# hutU (PA5100, Q9HU83) review notes

## Sources and research (2026-11-05)

No deep-research provider was available; this is manual research. Sources read: the
UniProt record (Swiss-Prot, HAMAP MF_00577), the GOA file, cached PMID:4290562 (abstract
only; the MCP returned no PMC body), PMID:16475788 and the sibling hut reviews in
genes/PSEAE/hutH, hutI and hutF, whose notes record a full-text reading of PMID:4290562.

- HutU is urocanase (urocanate hydratase, EC 4.2.1.49), the NAD+-containing enzyme of
  step II of histidine degradation, converting trans-urocanate to 4-imidazolone-5-propanoate
  (UniProt CC:CATALYTIC ACTIVITY and CC:COFACTOR, HAMAP-Rule MF_00577).
- The first three pathway steps are HutH, HutU and HutI
  [PMID:16475788 "The first three steps for the degradation of histidine include the action of HutH, HutU, and HutI to convert L-histidine to N-formimino-L-glutamate."].
- Lessie and Neidhardt 1967 assay urocanase in P. aeruginosa and describe urocanase-deficient
  mutants [PMID:4290562 "Urocanase-deficient bacteria formed enzymes I and IV constitutively; presumably they accumulate enough urocanate from the breakdown of endogenous histidine to induce formation of the pathway."].
  The hutI and hutF notes record that the full text has
  these mutants (a copy supplied by the user was read): "Its mutants are a urocanase-deficient strain, a histidine auxotroph and
  regulatory mutants with altered repression" (genes/PSEAE/hutI/hutI-notes.md).
- The paper predates gene cloning, so the tie between the mutant and PA5100 is an
  inference. It is secure: a live UniProt query (2026-11-05, organism_id 208964 with family
  urocanase or Pfam PF01175) returns one protein, Q9HU83 hutU PA5100. The phenotype of the
  urocanase-deficient mutant (it still induces enzymes I and IV, so it is not a regulatory
  mutant) fits a structural-gene lesion.

## PseudoCAP IBA-seed assessment

Seeds of PTN002639709 (`.cache/paint/IBD.gaf`, column 8): GO:0016153 is seeded by
Q96N76 (human UROC1), Q9HU83 (this gene) and P25503 (B. subtilis HutU); GO:0006548 by
Q96N76 and Q9HU83. QuickGO (2026-11-05): UROC1 has GO:0016153 IDA and GO:0006548 IMP
(BHF-UCL, PMID:19304569); B. subtilis HutU has GO:0016153 EXP (UniProt, PMID:4990470).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002639709 | GO:0016153 urocanate hydratase activity | 3 | 50 (47 taxa) | GO:0016153 urocanate hydratase activity, IMP, PMID:4290562 (PseudoCAP) | SOUND | The paper assays urocanase and describes a urocanase-deficient mutant; PA5100 is the only urocanase-family protein in PAO1, so loss of the activity maps to this gene. The node term suits a conserved single-function urocanase family (HAMAP MF_00577, TIGR01228). Gene assignment is by inference (pre-cloning paper). | Human UROC1 (IDA), B. subtilis HutU (EXP) | Yes. No GO_CENTRAL defect. |
| PTN002639709 | GO:0006548 L-histidine catabolic process | 2 | 50 (47 taxa) | GO:0006548 L-histidine catabolic process, IMP, PMID:4290562 (PseudoCAP) | SOUND | Urocanase catalyses step II of histidine degradation, named as such in the abstract. | Human UROC1 (IMP, urocanic aciduria) | Yes. No GO_CENTRAL defect. |

Consistency with the sibling hut reviews: the same 1967 paper is SOUND for hutH (histidase
assayed directly) and UNVERIFIABLE/MISCITED for hutI and hutF (their steps are not studied).
HutU is in the hutH situation: step II is assayed and a urocanase mutant is described, so the
reference fits this gene. No hut nodes are shared (hutH PTN000796617/PTN000796665, hutI
PTN000505272, hutF PTN000138516, hutU PTN002639709).

## Annotation decisions

- GO:0016153 (IBA, IEA, IMP): ACCEPT; core activity.
- GO:0006548 (IBA, IEA, IMP): ACCEPT; HutU performs step II. As in the sibling reviews, the
  general histidine-catabolism term is kept (the urocanase step is shared by the
  formamide and formate branches).
- GO:0005737 cytoplasm (IEA): ACCEPT; soluble enzyme without signal peptide or TM segment.
