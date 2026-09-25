# CDC25C (human, P30307) — curation notes

## Identity
M-phase inducer phosphatase 3 / dual-specificity phosphatase CDC25C, 473 aa, gene 5q31.2.
One of three human CDC25 paralogues (A/B/C). C-terminal rhodanese-like catalytic domain
(FT DOMAIN 321..428) with the HCX5R PTP loop; catalytic Cys is the active site (FT ACT_SITE 377).
Divergent, disordered N-terminal regulatory region carrying the phospho-sites.
[UniProt P30307; falcon deep research §1]

## Core biochemistry
Cysteine-dependent dual-specificity phosphatase; removes inhibitory phosphates from CDK1
(Cdc2) Thr14 and Tyr15, reversing WEE1/PKMYT1 and activating cyclin B–CDK1 at mitotic entry.
[PMID:8119945 "Human cdc25C protein, a specific tyrosine phosphatase that activates the p34cdc2 protein kinase at mitosis"]
[PMID:1828290 "We propose that the cdc25+ gene product directly activates the p34cdc2-cyclin B complex"]
Physiological preference is CDK1-pThr14/pTyr15–cyclin B; weak/absent on CDK2–cyclin A
(contrast CDC25A). [falcon §2.2; rudolph2001]
Human CDC25 rescues a fission-yeast cdc25ts mutant (functional orthology).
[PMID:2195549 "The human CDC25 gene rescues the defect of a fission yeast temperature-sensitive (ts) cdc25ts mutant that is unable to initiate mitosis"]

## Activation / positive feedback
Multisite phosphorylation by CDK1 (Thr48, Thr67, Ser122, Thr130, Ser168, Ser214) and PLK1
converts CDC25C from an interphase-inhibited to a mitotically active state (positive feedback).
[UniProt PTM; PMID:8119945 "only the phosphorylated form of cdc25 is highly effective in activating G2 cells into premature prophase"]
PLK1 docks on Cdc25C via its polo-box domain after Thr130 priming phosphorylation.
[PMID:17307877 "Plk1 recognizes this region of Cdc25C upon Thr-130 phosphorylation"; PMID:19597481 "the interaction between Plk1 PBD and its physiological binding target, phospho-Cdc25C"]
PLK3 phosphorylates Ser191 to promote nuclear translocation.
[PMID:14968113 "polo-like kinase 3 (Plk3) is able to phosphorylate Cdc25C primarily on S191"; "the S191D Cdc25C mutant leads to an enhanced accumulation of Cdc25C in the nucleus"]

## Inhibitory checkpoint regulation (Ser216 / 14-3-3)
CHEK1/CHEK2/MARK3(C-TAK1)/MAPK14 phosphorylate Ser216 (interphase, DNA-damage checkpoint),
creating a 14-3-3 binding site that sequesters CDC25C in the cytoplasm and impedes nuclear import.
[PMID:9543386 "Serine 216 phosphorylation mediates the binding of 14-3-3 protein to Cdc25C"]
[PMID:12941695 "Disruption of the Cdc25C-C-TAK1 interaction resulted in reduced 14-3-3-binding site phosphorylation and nuclear accumulation of Cdc25C in interphase cells"]
Specific isoform contacts: 14-3-3epsilon (F135 pocket) and 14-3-3gamma.
[PMID:19331823 "Cdc25C function is inhibited by complex formation with two 14-3-3 isoforms, 14-3-3epsilon and 14-3-3gamma"]
BRCA1 governs the checkpoint upstream, controlling Cdc25C expression/localization and 14-3-3.
[PMID:11836499 "the 14-3-3 family of proteins that sequesters phosphorylated Cdc25C and Cdc2/cyclin B kinase in the cytoplasm"]

## Localization
UniProt subcellular location: Nucleus. CDC25C is a nucleocytoplasmic shuttling protein,
predominantly cytoplasmic in interphase (CRM1 export + phospho-Ser216/14-3-3), nuclear at mitotic
onset. [falcon §4; PMID:14968113]. Nuclear speck IDA (GO_REF:0000052, HPA). The mitochondrial
intermembrane-space IEA (GO_REF:0000107, from mouse ortholog P48967) is an erroneous electronic
localization not supported by any CDC25C evidence — REMOVE.

## Interaction partners (GOA WITH mapping)
O14757=CHEK1; P27448=MARK3(C-TAK1); P63104=YWHAZ(14-3-3ζ); P62258=YWHAE(14-3-3ε);
P31946=YWHAB(14-3-3β); P53350=PLK1; P06493=CDK1(Cdc2); Q9Y250=LZTS1(Fez1); Q9H4B4=PLK3;
Q13526=PIN1. Generic GO:0005515 rows resolved: 14-3-3 partners → 14-3-3 protein binding
(GO:0071889); kinase partners (CHEK1, PLK1, CDK1) → protein kinase binding (GO:0019901);
MARK3 → protein serine/threonine kinase binding (GO:0120283). LZTS1 (a mitotic adapter that
protects Cdc25C from degradation, PMID:17349584) gives no informative CDC25C MF → REMOVE generic
protein binding without asserting the interaction is false.

## Necessity / paralogue redundancy
Cdc25c-null mice are viable with normal checkpoints; Cdc25b/Cdc25c double-null viable (females
sterile) — substantial compensation by CDC25A/B. Do not annotate CDC25C as solely required for
mitosis. [kiyokawa2008; falcon §5]

## Meiosis
GO:0110032 (positive regulation of G2/MI meiotic transition) is an IBA carried from the pombe/
family node — same Tyr15-dephosphorylation activity deployed in meiosis; genuine but non-core for
human somatic CDC25C → KEEP_AS_NON_CORE (mirrors SCHPO cdc25 exemplar).

## Splice isoforms
Five isoforms; Cdc25Cdm (isoform 5) reported in A431; variants alter N-terminal regulatory
phospho-sites but retain the catalytic domain. [PMID:11078813; PMID:11139144]
