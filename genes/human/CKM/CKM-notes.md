# CKM (Creatine kinase M-type) — Gene Review Notes

UniProt: P06732 (KCRM_HUMAN). Gene: CKM (synonym CKMM). HGNC:1994. EC 2.7.3.2.
Located on chromosome 19q13. 381 aa cytosolic protein.

## Catalytic function and reaction

CKM is the muscle-type cytosolic creatine kinase. It reversibly catalyzes phosphoryl
transfer between ATP and creatine:

> creatine + ATP = N-phosphocreatine + ADP + H(+)  [Rhea:RHEA:17157, EC=2.7.3.2]
(UniProt CATALYTIC ACTIVITY, P06732)

UniProt FUNCTION: "Reversibly catalyzes the transfer of phosphate between ATP and various
phosphogens (e.g. creatine phosphate). Creatine kinase isoenzymes play a central role in
energy transduction in tissues with large, fluctuating energy demands, such as skeletal
muscle, heart, brain and spermatozoa." (P06732, by similarity to P00563).

The reaction is reversible; the physiological direction depends on local energy state.
In the cytosolic/myofibrillar limb of the phosphocreatine shuttle, CKM regenerates ATP
from phosphocreatine (PCr + ADP -> ATP + Cr) at sites of high ATPase activity, while
mitochondrial CK (CKMT) runs the reaction in the synthetic direction near the ATP source.
Membership of the ATP:guanido phosphotransferase family (UniProt SIMILARITY).

## Dimer composition (MM / MB)

UniProt SUBUNIT: "Dimer of identical or non-identical chains, which can be either B (brain
type) or M (muscle type). With MM being the major form in skeletal muscle and myocardium,
MB existing in myocardium, and BB existing in many tissues, especially brain." (P06732).

So CKM forms CK-MM homodimers (the dominant species in skeletal muscle and myocardium) and
CK-MB heterodimers with CKB (P12277, brain-type) in myocardium. The CKM/CKB interaction is
recorded in UniProt INTERACTION (P06732; P12277: CKB). CKM also interacts with mitochondrial
CK (CKMT1B, P12532), the ankyrin-repeat protein ASB9 (Q96DX5), and huntingtin (HTT, P42858).

## Localization: M-band / myofibrils and membranes

MM-CK is a bona fide cytosolic enzyme (UniProt SUBCELLULAR LOCATION: Cytoplasm) but a
functionally important pool is bound at the sarcomeric M-band, where it acts as a local
ATP regenerator coupled to the myosin ATPase.

[PMID:12972258 "MM-CK interacts in an isoform-specific manner with the M-band of sarcomeric
muscle, where it serves as an efficient intramyofibrillar ATP-regenerating system for the
actin-activated myosin ATPase located nearby on both sides of the M-band."]

[PMID:12972258 "A yeast two-hybrid screen led to the identification of MM-CK as a binding
partner of a central portion of myomesin (My7-8). An interaction was observed with domains
six to eight of the closely related M-protein but not with several other Ig-like domains,
including an M-band domain, of titin."]

[PMID:12972258 "the MM-CK-specific lysine residues (K8. K24, K104 and K115) are involved in
this interaction."] — these four M-specific N-terminal lysines mediate the M-band charge-clamp
binding (also covered by PMC2175123, Hornemann et al.).

Historical primary evidence for M-line CK as the receiving end of the shuttle: PMID:6143755
("Function of M-line-bound creatine kinase as intramyofibrillar ATP regenerator at the
receiving end of the phosphorylcreatine shuttle in muscle"). MM-CK is additionally found
associated with the sarcoplasmic reticulum and T-tubule membranes, where it supports local
ATP/ADP ratios for Ca2+ pumping (review/biochemical literature; not a CKM-specific cached PMID).

## Energy buffering / phosphocreatine shuttle

CK isoenzymes buffer cytosolic ATP and shuttle high-energy phosphate between mitochondria
(site of PCr synthesis by mitochondrial CK) and sites of ATP consumption (myofibrils,
sarcolemmal/SR ion pumps), where cytosolic CKM regenerates ATP. This temporal (buffering)
and spatial (shuttle) role is the core physiological function of the CK system in striated
muscle, heart, and other high-energy-demand tissues (UniProt FUNCTION; review literature).

## Tissue expression

Human Protein Atlas: "Group enriched (skeletal muscle, tongue)" (UniProt HPA line).
Bgee: expressed in skeletal muscle and many other tissues. CKM is the muscle-specific
isoform, highly expressed in skeletal muscle and cardiac muscle (myocardium). Its gene is
developmentally regulated and tissue-specific (PMID:2903158, "Developmental regulation and
tissue-specific expression of the human muscle creatine kinase gene"). The MCK enhancer/
promoter is a classic muscle-specific regulatory element.

## Disease / physiology

Serum CK-MM and CK-MB are classic clinical biomarkers: total CK and CK-MB rise after
myocardial infarction and CK-MM after skeletal-muscle injury (rhabdomyolysis, muscular
dystrophy). MIM:123310 (gene). A common CKM 3'-UTR polymorphism (NcoI) has been associated
with variation in exercise/endurance phenotypes in some studies. CKM is a drug-interaction
target (creatine, phosphocreatine in DrugBank). No classical Mendelian disease is firmly
attributed to CKM loss-of-function in humans; Ckm-knockout mice are viable but show altered
muscle energetics and burst-activity performance.

## Structure

Two-domain phosphagen kinase fold: N-terminal phosphagen kinase domain (res 11-98) and
C-terminal catalytic domain (res 125-367). ATP-binding residues annotated (128-132, 191,
236, 292, 320-325, 335). Crystal structures: 1I0E (3.5 Å human MM-CK), 7BF2 (peptide).

## GO review orientation

- Core MF: creatine kinase activity (GO:0004111) — strongly supported (catalytic activity,
  Rhea/EC mapping, ISS from P00563, TAS PMID:3778496, IBA). ACCEPT.
- Core BP: phosphocreatine biosynthetic process (GO:0046314) — the cytosolic enzyme
  catalyzes the reversible reaction whose "biosynthetic" labelled direction is PCr synthesis;
  appropriate, ACCEPT (the reverse direction is the ATP-regenerating physiological role).
- Core CC: cytosol (GO:0005829, TAS Reactome) / cytoplasm; M band (GO:0031430) supported by
  PMID:12972258 isoform-specific M-band binding.
- ATP binding (GO:0005524, KW IEA) — true, but a generic supporting MF; KEEP_AS_NON_CORE.
- Generic IEA parents (catalytic activity GO:0003824, kinase activity GO:0016301, transferase
  GO:0016772, phosphotransferase nitrogenous acceptor GO:0016775) — true but uninformative
  parents of creatine kinase activity; MARK_AS_OVER_ANNOTATED / generalizations subsumed by
  GO:0004111.
- extracellular region / extracellular space (GO:0005576 IBA & IEA) — CKM is a cytosolic
  enzyme; serum CK is leakage from damaged cells, not secretion. The IBA "is_active_in
  extracellular region" is an over-propagation. CKM is not active extracellularly. MARK_AS_
  OVER_ANNOTATED / REMOVE candidate (IBA/IEA, electronic, arguable on biological grounds).
- protein binding (GO:0005515, many IPI) — uninformative bare term; the informative ones
  (M-band myomesin/M-protein PMID:12972258; CKB; CKMT1B; ASB9; HTT) are captured by SUBUNIT/
  interaction. KEEP_AS_NON_CORE (avoid as core function per guidelines).
</content>
