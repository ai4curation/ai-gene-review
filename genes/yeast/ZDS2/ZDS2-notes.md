# ZDS2 review notes

## Identity

- ZDS2 / YML109W / MCS1, UniProt P54786 (942 aa), SGD:S000004577. Paralog of
  ZDS1 (P50111, SGD:S000004886); PANTHER PTHR28089 (PROTEIN ZDS1-RELATED).
- Fungus-specific family [PMID:24800822 "Zds1-family proteins are found only in fungi but not in higher eukaryotes."].
- No deep-research file was available when this review was written; a Falcon
  job was running in the background (2026-10-10). The review is based on cached
  primary literature.

## Molecular function

- Direct binding to Cdc55 through the C-terminal ZH4/Zds_C region
  [PMID:20980617 "ZH4 is shown by protein affinity assays to be necessary and sufficient for interaction with Cdc55p, a regulatory subunit of protein phosphatase 2A (PP2A)."];
  a recombinant GST-Zds2(731-942) vs MBP-Cdc55 binding assay was performed (methods of PMID:20980617).
- Complex with PP2A-Cdc55 throughout mitosis
  [PMID:18762578 "Again, coimmunoprecipitation demonstrated interaction of Zds2 with Cdc55 and Tpd3 in metaphase as well as during synchronous progression through anaphase and mitotic exit"];
  [PMID:21119008 "Zds1 and Zds2 form a tight stoichiometric complex with PP2A(Cdc55) and target its activity to Cdc25 but not to Wee1"].
- Sign of regulation depends on context: activation/targeting at mitotic entry,
  down-regulation at mitotic exit
  [PMID:21536748 "Zds1/Zds2 promote Cdc55-PP2A function for mitotic entry, whereas Zds1/Zds2 inhibit Cdc55-PP2A function during mitotic exit."];
  [PMID:22427694 "Therefore, it seems unlikely that Zds1p and Zds2p act as direct inhibitory components of the PP2ACdc55 complex."].
- Conclusion: GO:0019888 protein phosphatase regulator activity is the core MF.
  The IBA GO:0004864 (seeded only by ZDS1's overexpression IMP) is MODIFY to
  GO:0019888. No direct phosphatase-inhibition assay exists for Zds2.

## Processes

- G2/M: [PMID:20980617 "We also show that expression of ZDS1 or ZDS2 from a strong galactose-inducible promoter can induce mitosis even when the Swe1p-dependent G2/M checkpoint is activated"];
  [PMID:21536748 "Thus, the cytoplasmic localization of Cdc55 mediated by Zds1/Zds2 is required and sufficient for normal mitotic entry."]
- Mitotic exit / FEAR: zds2 single mutant has normal Cdc14 release timing, but
  the double mutant almost abolishes separase-induced release
  [PMID:18762578 "Cdc14 nucleolar release was almost completely abolished in zds1Δ zds2Δ cells."];
  ectopic Zds2 is sufficient
  [PMID:18762578 "We conclude that ectopic expression of either Zds1 or Zds2 in metaphase-arrested cells is sufficient to cause nucleolar release of Cdc14."].
  NEW GO:0031536 (IGI). Comparator: ESP1, LTE1 and GLC7 carry GO:0031536 in SGD.
- Polarity / Rho1: [PMID:8816439 "overexpression of either Zds1p or Zds2p decreases the level of Cdc42p activity"];
  [PMID:26728856 "Cdc55, and its cortical anchoring proteins Zds1/Zds2 as novel regulators of Rho1 signaling"]. Kept non-core.
- Silencing / life span (opposite to zds1):
  [PMID:10662670 "deletion of its paralog ZDS2 caused a decrease in rDNA silencing, a decrease in life span and an increase in Sir3p phosphorylation"]. Kept non-core.
- Bcy1 cytoplasmic retention at 37 C (not in GOA):
  [PMID:12704202 "Zds1 and Zds2 may play a role in this process, since these were found required to retain hyperphosphorylated Bcy1 in the cytoplasm at 37 degrees C."]

## Localization

- Cytoplasm and cortex, excluded from the nucleus [PMID:21536748 "First, the majority of Zds1/Zds2 is in the cytoplasm."].
- Bud cortex/tip [PMID:20980617 "On budding, Zds2-i-9x-myc concentrated at the bud cortex in 78% of small-budded, 90% of medium-budded, and 86% of large-budded cells"].
- Bud neck late in mitosis [PMID:21536748 "We also observed bud neck localization of Zds1-GFP and Zds2-GFP in late mitotic cells"].

## Protein binding rows

All four GO:0005515 IPI rows (Boi1 from PMID:10688190, PMID:11743162 and
PMID:19841731; Sla1 from PMID:19841731) come from high-throughput two-hybrid or
SH3-interactome screens. None supports a more specific Zds2 MF, so all four are
REMOVE.
