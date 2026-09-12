# IDS (iduronate 2-sulfatase) — curation notes

UniProtKB: P22304 (IDS_HUMAN). HGNC:5389. EC 3.1.6.13. Gene on Xq28.

## Function (grounded)

IDS is a **lysosomal sulfatase** that catalyses one step in the stepwise exolytic
degradation of the glycosaminoglycans (GAGs) **heparan sulfate and dermatan sulfate**.
It **hydrolytically removes the 2-O-sulfate group from terminal (non-reducing end)
2-O-sulfo-α-L-iduronic acid (L-iduronate-2-sulfate) residues**, exposing iduronate for
the next enzyme in the pathway (IDUA, α-L-iduronidase).

- UniProt FUNCTION: "Lysosomal enzyme involved in the degradation pathway of dermatan
  sulfate and heparan sulfate" [file:human/IDS/IDS-uniprot.txt].
- CATALYTIC ACTIVITY (EC 3.1.6.13): "Hydrolysis of the 2-sulfate groups of the
  L-iduronate 2-sulfate units of dermatan sulfate, heparan sulfate and heparin"
  [file:human/IDS/IDS-uniprot.txt].
- Structure paper: "IDS belongs to the sulfatase family of enzymes and catalyses
  hydrolysis of the C2-sulfate ester bond at the non-reducing end of 2-O-sulfo-α-L-iduronic
  acid residues in dermatan sulfate and heparan sulfate" [PMID:28593992].
- cDNA paper: "Iduronate 2-sulfatase (IDS, EC 3.1.6.13) is required for the lysosomal
  degradation of heparan sulfate and dermatan sulfate" [PMID:2122463].

## Catalytic mechanism / formylglycine

Like all eukaryotic sulfatases, IDS requires the **Cα-formylglycine (FGly, 3-oxoalanine)**
catalytic residue at Cys84, generated post-translationally in the ER by the
formylglycine-generating enzyme (FGE / SUMF1) acting on the conserved CxPSR motif.
- "The catalytic residue C84 ... In all eukaryotic sulfatases, the thiol group of this
  residue is oxidized to Cα-formylglycine (FGly ...), an essential modification required
  for catalytic activity. This modification is performed by FGly-generating enzyme (FGE),
  which recognizes the highly conserved sequence motif CxPSR" [PMID:28593992].
- Crystal structure (PDB 5FQL, 2.3 Å) shows a **single Ca2+ ion per subunit** in the
  active site coordinating the FGly-sulfate and metal-binding aspartates
  (D45/D46/D334/H335) — basis of the GO:0005509 calcium ion binding IDA [PMID:28593992].

## Localization / processing

- Lysosome / lysosomal lumen. SUBCELLULAR LOCATION: "Lysosome" [file:human/IDS/IDS-uniprot.txt].
- Synthesized as a ~75-kDa ER precursor, proteolytically processed to a mature ~55-kDa form
  (42-kDa + 14-kDa chains that remain associated as the active 58-kDa intermediate)
  [PMID:28593992; file:human/IDS/IDS-uniprot.txt].
- N-glycosylated (8 sites); glycans and mannose-6-phosphate route govern lysosomal targeting.

## Disease

Deficiency causes **Mucopolysaccharidosis type II (Hunter syndrome; MIM 309900)**, an
X-linked lysosomal storage disease with accumulation of heparan and dermatan sulfate.
Enzyme replacement therapy = idursulfase (Elaprase). >500 IDS mutations known.

## SUMF2 interaction (PMID:15962010, the IPI on GO:0005515)

The IntAct IPI (GO:0005515 protein binding, with UniProtKB:Q8NBJ7 = SUMF2) derives from
Zito et al. 2005: SUMF2 "is able to stably associate with IDS and with SGSH alone or in a
complex with SUMF1" [PMID:15962010]. This is a regulatory ER interaction (SUMF2 modulates
SUMF1/FGE-mediated activation of sulphatases), not a core molecular function of IDS.
Per curation policy, bare `protein binding` IPI is marked MARK_AS_OVER_ANNOTATED (kept,
flagged as uninformative), not removed.

## GO annotation decisions (summary)

Core MF: **GO:0004423 iduronate-2-sulfatase activity** (exact GOA term; EC 3.1.6.13).
Core BP: heparan sulfate + dermatan sulfate catabolism — GO:0030200 (HS proteoglycan
catabolic), GO:0030209 (DS proteoglycan catabolic), parent GO:0006027 (GAG catabolic, IDA).
Core CC: GO:0005764 lysosome / GO:0043202 lysosomal lumen.

- GO:0004423 (IBA, IEA, EXP x2, IDA, TAS) — ACCEPT (all robust; core MF).
- GO:0005764 lysosome (IBA, IEA, IDA) — ACCEPT (core CC).
- GO:0043202 lysosomal lumen (IEA-ARBA, TAS x4 Reactome) — ACCEPT (core CC; more specific).
- GO:1901136 carbohydrate derivative catabolic process (IEA-ARBA) — ACCEPT but non-core
  (correct but very general; GO:0006027 is the informative form).
- GO:0006027 glycosaminoglycan catabolic process (IDA) — ACCEPT (core BP; supported by
  PMID:28593992 GAG degradation pathway).
- GO:0005509 calcium ion binding (IDA, PMID:28593992) — ACCEPT (structural cofactor;
  supports catalysis but not the "core function" descriptor; keep).
- GO:0005515 protein binding (IPI, PMID:15962010, SUMF2) — MARK_AS_OVER_ANNOTATED
  (uninformative bare protein binding).
</content>
