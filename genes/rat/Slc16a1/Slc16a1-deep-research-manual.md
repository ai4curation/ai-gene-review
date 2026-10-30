# Slc16a1 (rat MCT1, P53987) - manual literature synthesis

No deep-research provider API keys were available in this session, so this
synthesis was written by hand from the cached publications in `publications/`
and PubMed searches. Every claim below gives its source.

## Identity and family

- Rat Slc16a1 encodes monocarboxylate transporter 1 (MCT1), 494 aa, 12 predicted
  transmembrane helices, cloned from rat small intestine
  [PMID:8526936 "predicted a protein of 494 amino acids with twelve potential transmembrane domains"].
- Member of the SLC16 / monocarboxylate porter family (TC 2.A.1.13) of the major
  facilitator superfamily (UniProt P53987 SIMILARITY; InterPro IPR004743 MCT,
  PANTHER PTHR11360:SF24).
- Of the 14 SLC16 members, only MCT1-4 are proton-linked monocarboxylate
  transporters [PMID:23506875 "Four (SLC16A1, SLC16A3, SLC16A7, and SLC16A8) encode monocarboxylate transporters (MCT1, MCT4, MCT2, and MCT3, respectively) catalysing the proton-linked transport of monocarboxylates such as l-lactate, pyruvate and ketone bodies across the plasma membrane"].

## Transport activity (direct assays on rat MCT1)

- Rat MCT1 cRNA in Xenopus oocytes increases lactate uptake
  [PMID:8526936 "When expressed in Xenopus laevis oocytes, the ratMCT1 cRNA caused a significant increase in the uptake of radiolabeled lactic acid."].
- Proton coupling: lactate causes intracellular acidification of MCT1-expressing
  oocytes; substrate range includes pyruvate, D,L-3-hydroxybutyrate,
  acetoacetate and branched-chain 2-oxoacids, but not di- or tricarboxylates
  [PMID:9639576 "Superfusion with lactate resulted in intracellular acidification of MCT1-expressing oocytes, but not in non-injected control oocytes."]
  [PMID:9639576 "MCT1 mediated the reversible transport of a wide variety of monocarboxylic acids including pyruvate, D,L-3-hydroxybutyrate, acetoacetate, alpha-oxoisohexanoate and alpha-oxoisovalerate, but not of dicarboxylic and tricarboxylic acids."]
- MCT1 accounts for astrocyte lactate transport (astrocyte-neuron lactate
  shuttle context) [PMID:9374487 "MCT1 can account for all characteristics of lactate transport in glial cells"].
- Antisense depletion of MCT1 in rat brain capillary endothelial cells abolishes
  saturable benzoic acid uptake (xenobiotic monocarboxylic acid)
  [PMID:10714609 "hybrid depletion of MCT1 in RBEC1 using an antisense oligonucleotide against rat MCT1 abolished the saturable transport of benzoic acid."].
- Turnover in rat erythrocytes (~12 s-1) and potent inhibition by AR-C155858
  binding an intracellular site in TM7-10 [PMID:19929853].

## Mechanism / residues

- Asp302-Arg306 (TM8) ion pair: needed for plasma membrane expression and
  catalysis [PMID:17127621 "No PM expression of R306E-MCT1 or D302R-MCT1 was observed but D302R/R306D-MCT1 reached the PM, as did R306K-MCT1. However, both were catalytically inactive"].
- Lys38 (TM1) essential for transport but not for surface expression
  [PMID:19473976 "K38Q-MCT1 and K38R-MCT1 were inactive when expressed at the plasma membrane of Xenopus laevis oocytes"].
  The proposed cycle has Lys38 accept a proton before lactate binds, with
  passage via Asp302/Arg306 [PMID:19473976 "Our model suggests a translocation cycle in which Lys(38) accepts a proton before binding lactate."].

## Ancillary proteins (basigin/embigin)

- MCT1 needs basigin (CD147) or embigin for plasma membrane expression and
  activity [PMID:11719518 "The monocarboxylate (lactate) transporters MCT1 and MCT4 require the membrane-spanning glycoprotein CD147 for their correct plasma membrane expression and function."].
- FRET shows MCT1-CD147 proximity in situ; no FRET between MCT1 molecules
  [PMID:11719518 "No FRET was observed between MCT1-YFP and MCT-CFP in any combination."].
- DIDS cross-links MCT1 to embigin in rat erythrocytes [PMID:19473976].
- The ~85 kDa "MCT1 dimer" seen on blots is attributed by the authors to
  detergent aggregation, not a physiological homodimer
  [PMID:19473976 "It should be noted that this is distinct from the MCT1 dimer that is observed at ∼85 kDa. Such dimers occur even in the absence of DIDS, and we have shown previously that this occurs as a result of aggregation of MCT1 in detergent (16)."].

## Localisation

- Plasma membrane (all expression studies above).
- Basolateral membrane of rat jejunal enterocytes
  [PMID:10564700 "suggest that MCT1 is a major route for lactate efflux across the basolateral membrane of rat jejunum"].
- Luminal (apical-equivalent) surface of rat brain microvessel endothelium
  [PMID:18619525 abstract; in vivo biotinylation].

## Physiology (mostly mouse; for context, not for NEW process terms)

- Mct1+/- mice resist diet-induced obesity; null is embryonic lethal
  [PMID:24367518 "MCT1 (+/-) mice displayed resistance to development of diet-induced obesity"].
- Succinate efflux from reperfused ischaemic heart requires MCT1 and is favoured
  by acidification (protonated monocarboxylate form of succinate)
  [PMID:32766828 "Succinate release upon reperfusion of the ischaemic heart is mediated by MCT1 and is facilitated by the acidification of the myocardium during ischaemia."].
  This contrasts with neutral-pH oocyte data showing no dicarboxylate transport
  [PMID:9639576], consistent with transport of the monoprotonated species only.
