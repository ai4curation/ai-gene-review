# CDC14 (Saccharomyces cerevisiae, UniProt Q00684) - curation notes

## Identity and biochemistry

- Cdc14/Oaf3/YFR028C, 551 aa, protein-tyrosine phosphatase superfamily, Cdc14 subfamily. Catalytic Cys283
  (phosphocysteine intermediate), Asp253 general acid/base; the C-terminal Asn/Ser-rich tail (375-551) is
  dispensable for activity and for the essential function [PMID:9295359 "This COOH-terminal segment is not
  required for activity, for oligomerization, or for the critical cell cycle function of Cdc14p."].
- Dual-specificity in vitro [PMID:9295359 "Recombinant Cdc14p was produced in bacteria, characterized, and
  shown to be a dual specificity protein phosphatase."], but every characterised physiological substrate is a
  CDK pSer-Pro site; pThr and pTyr are poor substrates (deep research, Kataria 2018 / DeMarco 2020 summaries:
  "Phosphothreonine is disfavored because its additional methyl group creates steric conflict in the active
  site."). This is why the EC 3.1.3.48-derived IEA GO:0004725 row was graded MODIFY -> GO:0008138
  (protein tyrosine/serine/threonine phosphatase activity) and the IBA GO:0004722 row is the core MF.
- Phosphatase activity is required for the essential function [PMID:9295359 "The catalytically inactive Cdc14p
  C283S/R289A mutant is not able to suppress the temperature sensitivity of a cdc14-1(ts) mutant nor replace
  the wild type gene in vivo"].
- In vivo substrate landscape: 835 Cdc14-dependent dephosphorylation sites on 455 candidate substrates,
  with Smc4 (condensin) and Bud3 validated [PMID:24319056 "Cdc14-mediated dephosphorylation of Smc4 and Bud3
  is essential for proper mitosis and cytokinesis, respectively."].

## Regulation by sequestration (RENT, FEAR, MEN)

- RENT = Net1 + Cdc14 + Sir2, nucleolar from G1 through anaphase; Net1 inhibits Cdc14; Tem1-dependent
  dispersal in late anaphase triggers mitotic exit [PMID:10219244 "In late anaphase, Cdc14 dissociates from
  RENT, disperses throughout the cell in a Tem1-dependent manner, and ultimately triggers mitotic exit."].
- Net1(1-600) is a direct competitive inhibitor, Ki 3 nM, measured with Swi5 and Sic1 as substrates
  [PMID:11274204]. PP2A-Cdc55 keeps Net1 underphosphorylated until separase downregulates it
  [PMID:16713564 "In metaphase, Cdc14 is kept inactive in the nucleolus by its inhibitor Net1."].
- Cdc5 (Polo) binds Cdc14 directly through its Polo-box domain and is required for release
  [PMID:18927509 "We find that Cdc5 physically associates with Cdc14, as well as with the FEAR network
  components Slk19 and Esp1."].
- Tof2 (Net1 paralog) binds Cdc14 directly; reported both as a nucleolar activator supporting rDNA
  segregation [PMID:18595708] and as a brake that retains a nucleolar pool after FEAR for later MEN release
  [PMID:18923139]. Both papers agree on direct binding; the functional interpretation differs.
- FEAR release is nuclear-confined and dispensable for timely mitotic exit but needed for timely rDNA
  segregation [PMID:26090959 "We find that Cdc14 is confined to the nucleus during early mitotic anaphase
  release, and during its meiosis I release."]. MEN drives export to the cytoplasm [PMID:26090959 "By late
  anaphase, Cdc14 had been efficiently exported to the cytoplasm (Fig 1C), indicating MEN activity."].
- Localisation: nucleolus (G1-metaphase), nucleus (FEAR), cytoplasm, SPBs (MEN-dependent; preferentially the
  bud/new SPB), bud neck in telophase [PMID:12062061 "We observed Cdc14-5GFP at the SPB in addition to the
  nucleolus."; PMID:36259662 "In telophase cells characterised by disassembled spindles, Cdc14 was localised
  at the bud SPB, nucleoli and bud neck (Type 3)."].

## Core function: mitotic exit

- Reverses Cdc28 phosphorylation of Cdh1, Sic1 and Swi5 (Visintin 1998, not cached; summarised in UniProt and
  the deep research: "Cdc14 is essential for late-anaphase-to-G1 progression in budding yeast."). Ordered
  dephosphorylation of CDK substrates is set by the phosphatase:kinase ratio [PMID:22078879].
- Graded core: GO:0007096 regulation of exit from mitosis (IBA, IEA, IMP), GO:0000278, GO:0004721/GO:0004722.

## Anaphase nuclear/nucleolar functions (graded non-core or MODIFY)

- rDNA segregation requires Cdc14 because of array length and Pol I hypertranscription [PMID:16769819];
  Cdc14 inhibits Pol I in anaphase, phosphatase-dependently, and this permits condensin loading
  [PMID:19158678 "The phosphatase activity of Cdc14 is required for RNA polymerase I (Pol I) inhibition in
  vitro and in vivo."]. GO:0007059 IMP row graded MODIFY -> GO:0000070 mitotic sister chromatid segregation.
- Interphase, TORC1-inactivation-induced rDNA condensation needs Cdc14, Rpd3, Hmo1, CLIP, cohibin but not
  condensin [PMID:35477092].
- Spindle: Fin1 is dephosphorylated by Cdc14 in anaphase and then stabilises the spindle
  [PMID:17173039 "In anaphase, when Clb5-Cdk1 is inactivated, Fin1 is dephosphorylated by the phosphatase
  Cdc14."]; Ase1 is another midzone substrate (UniProt).
- Top2: Cdc14 opposes Top2 phosphorylation and, with Cdc5, promotes catenane resolution
  [PMID:41533572 "Cdc5 promotes, whereas Cdc14 opposes, Top2 phosphorylation"]. The IGI (with CDC5) to
  GO:0071103 DNA conformation change is kept non-core: the conformation change is Top2's work, Cdc14 is a
  regulator.
- SPB duplication licensing: Cdc14 dephosphorylates C-Sfi1 [PMID:24954044].
- rDNA heterochromatin formation (NAS, PMID:12923057): the cited paper is about Net1/Sir2/Fob1; Cdc14 is a
  RENT subunit but the silencing work is Sir2's. Graded MARK_AS_OVER_ANNOTATED.

## Cytokinesis (graded core with mitotic exit)

- Cdk downregulation plus Cdc14 activation controls furrow ingression, membrane resolution and cell
  separation; nuclear-retained Cdc14-NLS cannot support cytokinesis; Inn1 dephosphorylation is required
  [PMID:25371407 "This confirms Inn1 as a Cdk target whose dephosphorylation by Cdc14 is crucial for
  successful cytokinesis."].
- Iqg1: Cdc14 binds and dephosphorylates CHD-flanking Cdk sites; iqg1-4A rescues actin ring failure of
  cdc14-1 [PMID:26085509 "Of importance, the iqg1-4A mutant rescued the inability of cdc14-1 cells to form
  actin rings."].
- Cbk1 (RAM network kinase) binds Cdc14 [PMID:17892321]; Gic1 binds Cdc14 directly but does not displace Net1
  [PMID:14734533 "Together, these results suggest that Gic1 does not promote mitotic exit by directly
  regulating Cdc14 localization."].

## Meiosis, autophagy, stress (graded non-core)

- Meiosis I spindle disassembly and two consecutive segregation phases need Cdc14/Slk19/Spo12
  [PMID:12737806].
- Meiotic anaphase I/II cytoplasmic Cdc14 dephosphorylates Atg13 to activate Atg1 and autophagy
  [PMID:35238874 "Cdc14 is activated in anaphase I and II, accompanying its subcellular relocation from the
  nucleolus to the cytoplasm, where it dephosphorylates Atg13 to stimulate Atg1 kinase activity and thus
  autophagy."]; after TORC1 inactivation Cdc14 is needed for Atg13 dephosphorylation and PAS formation
  [PMID:29694832]; SGD also records mitophagy from that paper (full text not cached; deferred to curator).
- NaCl response: cdc14-3 transcriptome defect overlaps the Hog1 program, Hog1 nuclear localisation aberrant,
  no direct Cdc14-Hog1 interaction [PMID:25411400 "Cdc14 is critical for coordinating distinct facets of
  the NaCl response"].

## Protein-binding (GO:0005515) IPI rows - policy applied

- 48 rows. Kinase partners (Cdc5, Cbk1, Snf1, Ste7, Cka1, Cka2, Mck1, Swe1, Chk1, Sak1, Bck1, Vhs1, Fmp48)
  -> MODIFY to GO:0019901 protein kinase binding; Clb3 -> GO:0030332 cyclin binding; Rsp5 -> GO:0031625
  ubiquitin protein ligase binding. Most kinase rows derive from the KPI AP-MS network
  [PMID:20489023 "the cell cycle phosphatase Cdc14 associated with multiple kinases"].
- Net1, Sir2, Tof2 (RENT / nucleolar anchor network), Sic1 and the Cdk substrates Ask1, Sli15, Orc6, Fin1
  (PMID:22078879), Hsp42 (two HTP surveys), Gic1, Boi1, Met14 (APS kinase, not a protein kinase) -> REMOVE
  as uninformative; complex membership is captured by GO:0030869 RENT complex, substrate relations belong on
  has_input. Removal does not claim the interactions are false.

## Open questions

- Which phosphoproteomic candidates are direct PxL-docked substrates vs. relay/indirect targets?
- Any physiological pTyr substrate? (None known; hence the GO:0004725 MODIFY.)
- Direct substrate mediating the osmotic-stress coordination.
