# fpr (Q9HYK7, PA3397) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 74)

No deep-research provider was available; these notes are my own reading of the Swiss-Prot record and the
cited paper PMID:17915950 (abstract only in the cache; no PMC full text).

## Identity

- PAO1 PA3397, Swiss-Prot Q9HYK7, 258 aa, ferredoxin--NADP reductase type 1 (plastid-type FNR fold:
  N-terminal FAD-binding FR-type domain, C-terminal NADP-binding domain). Monomer; structures 2QDX (FAD)
  and 3CRZ (FAD + NADP+). PANTHER PTHR47878:SF1.
- Upregulated under iron starvation (UniProt INDUCTION, PubMed:12207696).

## Literature

- Activity and HO partner: [PMID:17915950 "the fpr gene encodes a 258-residue NADPH-dependent ferredoxin
  reductase (pa-FPR) that utilizes FAD as a cofactor"]; [PMID:17915950 "In vitro reconstitution of pa-HO
  catalytic activity with the newly characterized proteins led to the surprising observation that pa-FPR
  efficiently supports the catalytic cycle of pa-HO, without the need of a ferredoxin."]; the ferredoxin
  route is slow [PMID:17915950 "electron transfer from pa-Bfd to pa-HO is sluggish"]; physiological framing
  [PMID:17915950 "Given that pa-HO functions to release iron from exogenous heme acquired under
  iron-starvation conditions, the use of a flavoenzyme rather than an iron-sulfur center-containing protein
  to support heme degradation is an efficient use of resources in the cell."].
- Other partners: Swiss-Prot curated FUNCTION (ECO:0000269, PubMed:19575528, 21574546): FPR also supplies
  electrons, via Bfd, to reduce and mobilise Fe(3+) from bacterioferritin BfrB. Not in GOA; not added here.

## Is FPR a participant in heme catabolism?

Applying the CLAUDE.md participation test ("which entity performs the step"): heme oxygenase (pa-HO,
HemO/PigA) catalyses the oxygenation of heme to biliverdin, Fe2+ and CO, but each of its turnover steps
consumes electrons that must be delivered by a reductase. GO's own definition of heme oxygenase activity
(GO:0004392) writes the reductase in as a co-substrate ("3 reduced [NADPH-hemoprotein reductase]"). FPR is
not the substrate of the process and is not merely required; it catalyses the NADPH-to-HO electron transfer
that the oxygenation steps depend on. This is the "cofactor activity" case that CLAUDE.md counts as doing
some of the work, so `involved_in heme catabolic process` is defensible for FPR in P. aeruginosa.

Comparator check (QuickGO, 2026-10-28): human, mouse and rat POR (P16435, P37040, P00388), the electron
donor of mammalian HO-1/HO-2, carry no annotation to GO:0042168 heme metabolic process or its descendants.
On the other hand, adrenodoxin reductase FDXR (P22570) is annotated to GO:0006694 steroid biosynthetic
process (IBA and TAS), so GO does annotate electron-donor reductases to the processes they serve. The
convention is inconsistent rather than prohibitive; I accept the FPR annotation, which rests on direct in
vitro reconstitution with the cognate HO, and note that in vivo dependence of heme-iron use on FPR has not
been shown.

The MF that describes the HO-partner role is reduction of a hemoprotein by NADPH (GO:0003958
NADPH-hemoprotein reductase activity), which the reconstitution supports and which GOA lacks. Added as NEW.

## The node PTN002500048

QuickGO (2026-10-28): 13 GO:0042167 IBA leaves: E. coli Fpr (P28861), Salmonella Fpr (Q8ZKP5), Yersinia
Fpr (A0A5P8YKR3), Shewanella Fpr (Q8EIT7), Xanthomonas Fpr (Q8PAR4), Neisseria meningitidis Fpr-1/Fpr-2
(Q7DDI7, Q9JYS7), Bradyrhizobium MvrA, blr3195, bll0100, P. aeruginosa PA4615 (Q9HVH6, the second FPR
paralog), Nematostella A7TBA2 (eukaryotic genome entry, probably a bacterial contaminant), and fpr itself.
E. coli Fpr is the flavodoxin/ferredoxin-NADP+ reductase of the SoxRS oxidative-stress regulon, and E. coli
K-12 and Salmonella have no canonical heme oxygenase, so heme catabolism is not a family property: it is
a partner-specific role demonstrated for one member. The reductase activity is the conserved feature; the
node term is too specific for the clade.

## Annotation decisions

- GO:0004324 ferredoxin-NADP+ reductase activity (EXP, IEA): ACCEPT, core MF.
- GO:0016491 oxidoreductase activity (IEA): MODIFY to GO:0004324.
- GO:0042167 heme catabolic process (IDA PseudoCAP; IBA): ACCEPT for fpr; GO_CENTRAL defect on node.
- NEW GO:0003958 NADPH-hemoprotein reductase activity (IDA, PMID:17915950).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002500048 | GO:0042167 heme catabolic process | 1 (sole) | 13 (9 taxa) | GO:0042167, IDA, PMID:17915950 (PseudoCAP) | OVER-SPECIFIC | For FPR the seed is sound: in vitro reconstitution shows FPR, without ferredoxin, drives the catalytic cycle of P. aeruginosa heme oxygenase, so FPR does part of the work (electron delivery, the cofactor case of the participation test), not mere necessity. But heme degradation is a partner-specific role, not a property of the FNR clade: the node includes E. coli and Salmonella Fpr (organisms without a canonical heme oxygenase; E. coli Fpr acts in the oxidative-stress response) and a eukaryotic contaminant entry. Withdraw the IBD; the reductase MF is the appropriate family-level term. |
