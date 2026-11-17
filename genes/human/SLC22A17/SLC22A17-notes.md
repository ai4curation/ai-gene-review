# SLC22A17 (BOCT / 24p3R / NgalR; UniProt Q8WUG5) — curation notes

## Summary / identity

SLC22A17 is misleadingly named: although it is classified in the SLC22 /
major-facilitator-superfamily "organic cation transporter" family (TC 2.A.1.19),
its established biological function is **not** that of a classic small-molecule
transmembrane transporter. It is the **cell-surface endocytic receptor for
lipocalin-2** (LCN2 / NGAL / 24p3), also called 24p3R, NgalR, BOCT (brain-type
organic cation transporter) and Lipocalin-2 receptor. The "transporter" name is a
family/fold-based label, not a demonstrated activity.

UniProt names (Q8WUG5): RecName "Solute carrier family 22 member 17"; AltNames
"24p3 receptor (24p3R)", "Brain-type organic cation transporter", "Lipocalin-2
receptor", "Neutrophil gelatinase-associated lipocalin receptor (NgalR)"; gene
synonyms BOCT, BOIT. 649 AA, multi-pass membrane protein (11 predicted TM helices,
MFS fold). Brain/choroid-plexus/pituitary enriched (HPA).

## Core function: lipocalin-2 endocytic receptor controlling cellular iron

UniProt CC:FUNCTION (ECO:0000250, By similarity): "Cell surface receptor for LCN2
(24p3) that plays a key role in iron homeostasis and transport. Able to bind
iron-bound LCN2 (holo-24p3), followed by internalization of holo-24p3 and release
of iron, thereby increasing intracellular iron concentration and leading to
inhibition of apoptosis. Also binds iron-free LCN2 (apo-24p3), followed by
internalization of apo-24p3 and its association with an intracellular siderophore,
leading to iron chelation and iron transfer to the extracellular medium, thereby
reducing intracellular iron concentration and resulting in apoptosis."
[UniProtKB:Q8WUG5 CC:FUNCTION].

So the gene product itself performs: (i) binding of the LCN2 ligand/cargo at the
cell surface (a specific **cargo/ligand receptor** molecular function, not bare
protein binding, and not transmembrane signal transduction); (ii)
**receptor-mediated endocytosis** of holo- or apo-LCN2; and (iii) consequent
**endocytic iron import** (holo-LCN2) or iron export (apo-LCN2), which sets the
intracellular iron level and thereby regulates apoptosis. The downstream
iron-homeostasis / apoptosis outcomes are the physiological consequences of the
receptor+endocytosis activity.

The mechanism is defined in mouse (24p3 / 24p3R): Devireddy et al. 2005, Cell
123:1293-1305 (PMID:16377569) showed a cell-surface receptor for 24p3 that
selectively mediates apoptosis and iron uptake; this is the basis of the UniProt
"By similarity" transfer and of the Reactome model. (PMID:16377569 not cached;
title/role per UniProt reference block.)

Reactome R-HSA-5671707 "Fe3+ dissociates from SLC22A17:LCN2:2,5DHBA":
"The iron-bound form of LCN2 (holo-LCN2) is internalised following binding to the
solute carrier family 22 member 17 (SLC22A17) receptor, leading to release of iron
which increases intracellular iron concentration and subsequent inhibition of
apoptosis. This step is inferred from experiments using the highly homologous 24p3
mouse lipocalin and 24p3R mouse cell surface receptor (Devireddy et al. 2005)."
[Reactome:R-HSA-5671707].

## Human-specific evidence (PMID:17253959, cached full text)

Fang et al. 2007, Biochem J 403:297-303 (PMID:17253959) cloned human NgalR
isoforms and a novel splice variant NgalR-3, and gave the direct human cell
evidence underpinning the IDA localization annotations:
- Localization: "Staining with an anti-HA or an anti-Myc antibody revealed a mainly
  cell membrane localization and a partial cytoplasm localization for the NgalR-3
  and NGAL protein" [PMID:17253959] — cell-surface plus internal (internalized)
  pool, consistent with an endocytic receptor.
- Interaction with the ligand: "a physical interaction between NGAL and NgalR-3
  could occur in mammalian cells" [PMID:17253959] (co-IP; co-localization).
- Family label (not a demonstrated activity): "NgalR is a member of the organic
  cation transporter family." [PMID:17253959] — this is the classification, and the
  paper itself frames NgalR's role as NGAL binding / iron-delivery via the
  receptor, not as direct organic-cation transport.

This paper (abstract already on record; full text cached) is the source of
UniProt's "Cell membrane" and "Vacuole membrane" subcellular-location calls and of
the IDA plasma-membrane (GO:0005886) and organelle-membrane (GO:0031090)
annotations. The "Vacuole membrane" call overstates the data: the paper shows cell
membrane + cytoplasm (internalized receptor), i.e. an endosomal/endocytic-vesicle
compartment rather than a bona fide human vacuole.

## Regulation / disease context

- Expression activated by RUNX3; repressed by BCR-ABL via a RUNX1 switch (Ras
  pathway): Devireddy et al. 2005 (PMID:16377569, INDUCTION) and Sheng et al. 2009,
  EMBO J 28:866-876 (PMID:19229297, INDUCTION) — per UniProt reference block
  (neither cached).
- Brain enrichment; implicated in neuronal iron handling and neurodegeneration
  contexts; appears in the neurodegenerative-disease interactome screen of Haenig
  et al. 2020 (PMID:32814053), which is the source of the bare GO:0005515 IPI with
  P4HB (PDI). This high-throughput interactome hit is uninformative of function.

## Transporter-vs-receptor: handling of family-name over-propagations

The following GOA rows assert transmembrane transporter function purely from the
SLC22 / MFS family classification, with no gene-specific evidence that SLC22A17
transports a solute:
- GO:0022857 transmembrane transporter activity — IBA (PAINT across the SLC22/MFS
  tree), IEA (ARBA + InterPro MFS signatures IPR005828/IPR005829/IPR020846), and
  TAS (Reactome, which actually models SLC22A17 only as the LCN2 receptor).
- GO:0055085 transmembrane transport — IEA (InterPro).
SLC22A17 has demonstrably **diverged** from the transporter function of the family
into a lipocalin receptor; these are treated as MARK_AS_OVER_ANNOTATED (family
label, not evidence). The InterPro/ARBA transmembrane-transporter-activity IEA is
recorded as a source_defect (OVER_PROPAGATION from an MFS signature to a protein
whose characterized function is receptor-mediated endocytosis).

The generic GO:0016020 membrane IEA is TOO_GENERAL (the specific plasma-membrane
location is asserted from direct evidence elsewhere).

The ISS GO:0004888 transmembrane signaling receptor activity (from mouse Q9D9E0)
captures that the protein is a receptor, but "transmembrane signaling receptor
activity" implies signal transduction across the membrane, whereas the
characterized activity is ligand/cargo binding followed by endocytosis. MODIFY to
the more accurate cargo receptor activity (GO:0038024).

## GO term choices (verified live, non-obsolete, via QuickGO 2026-11)

- GO:0038024 cargo receptor activity (MF) — def: "Binding specifically to a
  substance (cargo) to deliver it to a transport vesicle." Fits a receptor that
  binds LCN2 and internalizes it by endocytosis; avoids bare GO:0005515.
- GO:0006898 receptor-mediated endocytosis (BP).
- GO:0140298 endocytic iron import into cell (BP) — def: "Uptake of iron into a
  cell via binding to an extracellular receptor, which is internalized by
  endocytosis." Exact fit for holo-LCN2 import.
- GO:0006879 intracellular iron ion homeostasis (BP).
- GO:0015891 siderophore transport (BP).
- GO:0005886 plasma membrane; GO:0030666 endocytic vesicle membrane (CC).

## Action summary

- ACCEPT (5): GO:0005886 plasma membrane x4 (IBA, IDA, IEA, TAS); GO:0006879 iron
  ion homeostasis (TAS).
- KEEP_AS_NON_CORE (2): GO:0015891 siderophore transport (ISS); GO:0031090
  organelle membrane (IDA, internalized receptor).
- MODIFY (1): GO:0004888 -> GO:0038024 cargo receptor activity.
- MARK_AS_OVER_ANNOTATED (5): GO:0005774 vacuolar membrane; GO:0022857 x3;
  GO:0055085 transmembrane transport.
- TOO_GENERAL (1): GO:0016020 membrane.
- REMOVE (1): GO:0005515 protein binding (bare, HT interactome; protein-binding
  policy).
