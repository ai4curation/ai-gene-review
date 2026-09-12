# PGK1 (human) review notes

UniProtKB: P00558. X-linked (Xq21.1), ubiquitously expressed. 417 aa monomer.
PANTHER: PTHR11406:SF14 (PHOSPHOGLYCERATE KINASE 1). EC 2.7.2.3.

## Core function
Phosphoglycerate kinase 1 catalyses the first ATP-generating (substrate-level
phosphorylation) step of the glycolytic payoff phase: reversible transfer of a
phosphate between 1,3-bisphosphoglycerate + ADP and 3-phosphoglycerate + ATP.
UniProt CATALYTIC ACTIVITY: "(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl
phosphate + ADP" (RHEA:14801, EC 2.7.2.3). The reverse (right-to-left, RHEA:14803)
direction operates in gluconeogenesis. Requires Mg2+ (PMID:18463139).

- Core MF: GO:0004618 phosphoglycerate kinase activity (well supported by EXP/IMP/IBA/ISS/IEA).
- Core BP: GO:0006096 glycolytic process; GO:0006094 gluconeogenesis (reverse direction).
- Core CC: GO:0005829 cytosol.
- Nucleotide binding: ATP binding (GO:0005524), ADP binding (GO:0043531) are direct substrate
  binding for the reaction — accept as supporting/core.

Verbatim (PMID:26942675 full text): "Phosphoglycerate kinase 1 (PGK1), the first
ATP-generating enzyme in the glycolytic pathway, catalyzes the transfer of the high-energy
phosphate from the 1-position of 1,3-diphosphoglycerate (1,3-BPG) to ADP, which leads to
the generation of 3-phosphoglycerate (3-PG) and ATP".

## Moonlighting / non-core functions
- **Protein kinase (moonlighting).** Mitochondria-translocated PGK1 phosphorylates PDHK1
  (T338), activating it to inhibit the PDH complex; suppresses pyruvate->acetyl-CoA,
  promotes Warburg-effect glycolysis (PMID:26942675, IDA/EXP). UniProt lists EC 2.7.11.1
  and RHEA:17989 (protein Ser kinase). This is a context-specific (hypoxia/oncogenic,
  mitochondrial) moonlighting activity — KEEP_AS_NON_CORE. Terms: GO:0004674 protein
  ser/thr kinase, GO:0106310 protein serine kinase, GO:0160218 neg reg of pyruvate
  decarboxylation to acetyl-CoA, GO:0005759 mitochondrial matrix.
- **Secreted disulfide reductase / angiogenesis.** Secreted by tumour cells; reduces plasmin
  disulfides -> angiostatin release, inhibits angiogenesis (PMID:11130727, Nature 2000, IMP/IDA).
  Terms: GO:0047134 protein-disulfide reductase, GO:0005576 extracellular region,
  GO:0016525 neg reg angiogenesis, GO:0031639 plasminogen activation, GO:0071456 response to
  hypoxia. Non-core moonlighting.
- **Primer recognition protein / pol-alpha cofactor** (PMID:2324090) — noted in UniProt, not GOA.
- **Sperm motility** (PMID:26677959) — testis PGK; note PGK2 is the testis paralog.

## PPI / protein binding (bare GO:0005515)
Multiple IntAct/HT IPIs to GAPDH (P04406), PCNA (P12004), HDAC3 (O15379), PGK2 (P07205),
NEK7 (Q8TDX7), and 26942675 partners MAPK1/PIN1/PDHK1 (P28482/Q13526/Q15118). Per curation
policy, bare "protein binding" is uninformative -> MARK_AS_OVER_ANNOTATED (not REMOVE for
experimental IPIs). HDAC3 (26356530) deacetylates/activates PGK1 (regulatory).

## Localization (proteomics / HDA)
Extracellular exosome (multiple HDA PMIDs), membrane (HDA), membrane raft/detergent-resistant
fraction (PMID:25204797, PGK1 in DRM list). These reflect abundant cytosolic protein
co-purifying; KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED. Cytosol is the true core CC.

## Disease
PGK1 deficiency (PGK1D, MIM:300653): X-linked; hemolytic anemia, myopathy (exercise
intolerance / rhabdomyolysis), CNS/neurologic involvement, some parkinsonism.

## Wrong / to-remove
- GO:0004674 protein ser/thr kinase IEA via GO_REF:0000003 EC:2.7.11.1 — this generic
  EC->GO mapping is over-broad; the real activity is the specific moonlighting kinase; keep
  the experimental ones, mark the EC-mapping IEA as over-annotated (accept level too generic).
- GO:0005759 mitochondrial matrix IEA GO_REF:0000044 SubCell — same as experimental IDA;
  non-core (moonlighting-dependent import).
- GO:0044325 transmembrane transporter binding (Ensembl IEA GO_REF:0000107, from mouse) —
  weak orthology transfer, uninformative -> MARK_AS_OVER_ANNOTATED.
