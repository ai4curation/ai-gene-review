# norpA (P13217, PIPA_DROME) - manual literature synthesis

No deep-research API was available for this review. This synthesis was compiled by hand
from the cached publications in `publications/` and from PubMed searches. Every claim
carries its source.

## Identity and domain architecture

- norpA (no receptor potential A) encodes a 1095-residue phosphoinositide-specific
  phospholipase C of the beta class (PLCbeta). [PMID:2457447 "The putative norpA protein is
  composed of 1095 amino acid residues and has extensive sequence similarity to a PLC amino
  acid sequence from bovine brain."]
- UniProt and InterPro place it in the PLC-beta family (IPR016280), PANTHER subfamily
  PTHR10336:SF36 (PLC beta-4 like). The protein has a PH domain, EF-hand pair, the catalytic
  PI-PLC X-box (319-469) and Y-box (550-666), a C2 domain (666-794) and the PLCbeta
  C-terminal region. [file:DROME/norpA/norpA-uniprot.txt]
- Two isoforms are produced by alternative splicing (A/B and C/D). [file:DROME/norpA/norpA-uniprot.txt]

## Enzymatic activity: PIP2-specific phospholipase C

- Severe norpA mutants have no photoreceptor potential and lack eye PLC activity.
  [PMID:2457447 "Severe norpA mutations in Drosophila eliminate the photoreceptor potential
  and render the fly completely blind."]
- Head-membrane PLC activity against PIP2 and PI is reduced in visual mutants and the enzyme
  is membrane associated. [PMID:3129419 "The enzyme was concluded to be membrane-associated"]
- Light stimulates PIP2-PLC in head membranes; activation needs rhodopsin photoconversion and
  is reduced in norpA mutants; a G protein (with Gbeta-e) couples rhodopsin to NorpA.
  [PMID:7759511 "PLC activation depends on the photoconversion of rhodopsin to metarhodopsin
  and is reduced in norpAEE5 PLC and ninaEP332 rhodopsin mutants."]
- Products: IP3 and DAG. [PMID:11707492 "hydrolysis of phosphatidyl inositol 4,5-bisphosphate
  (PIP(2)) by phospholipase C generates inositol 1,4,5-trisphosphate (InsP(3)) and diacyl
  glycerol (DAG)"]
- Analysis of 47 norpA alleles identified catalytic X/Y residues; specific PLC activity sets
  photoreceptor sensitivity; catalysis and response termination are separable.
  [PMID:15140198 "(ii) the catalytic activity and response termination are separable
  functions of PLC"]

## GTPase-activating (GAP) activity toward Gq-alpha

- NORPA acts as a GAP for the visual Gq alpha, needed for rapid response termination.
  [PMID:10806481 "show that PLC functions as a GTPase-activating protein (GAP)"]
- A catalytically dead NORPA with wild-type GAP activity rescues the slow termination phenotype.
  [PMID:18184564 "the slow termination resulting from expressing low levels of wild-type NORPA
  was suppressed by addition of normal amounts of an altered NORPA, which had wild-type GAP
  activity, but no PLC activity."]

## Signalplex and localization

- NORPA is concentrated in the rhabdomere, close to but not inside the microvillar membrane.
  [PMID:1662208 "specifically localized within the rhabdomeres, preferentially adjacent to,
  but not within, the rhabdomeric membranes"]
- NORPA binds the PDZ scaffold INAD through PDZ1 (C-terminal tail) and PDZ5 (an internal
  region). Mutants lacking these sites are mislocalized and phototransduction is defective.
  [PMID:9545241 "We report that INAD directly binds to NORPA via two terminally positioned PDZ1
  and PDZ5 domains."]
- Crystal structure of INAD PDZ1 with the NorpA C-terminal peptide (disulfide "dock-and-lock").
  [PMID:11500369] UniProt cautions that the disulfide is an artifact of the synthetic peptide.
- The INAD complex is the unit of signalling for single-photon responses. [PMID:9796815]
- NORPA is a core signalplex member with TRP, INAC (PKC) and INAD. [PMID:16301334]
- PLC immunoreactivity is also found in photoreceptor axons in the lamina, and norpA
  hypomorphs have less depolarization-induced synaptic vesicle exocytosis there.
  [PMID:22952921 "These results show that PLC, PKC, TRP and TRPL are present in photoreceptor
  axons."; "Depolarization-induced exocytosis was markedly reduced in norpA mutant, suggesting
  a role of PLC in neurotransmitter release."]
- Regulation of abundance: the SOCS-box protein STOPS keeps NORPA levels up. [PMID:18184564]

## Physiological roles

1. Phototransduction (core). Rhodopsin -> Gq -> NORPA -> PIP2 hydrolysis -> TRP/TRPL opening.
   [PMID:18184564 "In fly photoreceptor cells, the PLCbeta encoded by norpA is critical for
   activation of TRP channels."]
2. Retinal degeneration. norpA mutants degenerate in light because stable rhodopsin-arrestin
   complexes are endocytosed. [PMID:16301334; PMID:16835270] Developmental PCD pathways (rpr,
   hid, grim, caspases) are largely dispensable. [PMID:14724249 "These results establish that
   the pathways responsible for PCD in development do not play a major role in adult retinal
   degeneration caused by norpA."]
3. Circadian entrainment. NORPA-dependent eye phototransduction is one light-input route to
   the clock, alongside CRY and the H-B eyelet. [PMID:9845370; PMID:22306971; PMID:28840790]
   Rh7 signalling in LNvs does not need NORPA. [PMID:28489826] NORPA also contributes to
   temperature entrainment. [PMID:16085487]
4. Thermosensation and chemosensation. In larval thermotaxis, rhodopsin -> Gq -> PLC -> TRPA1.
   [PMID:21393546] In gustatory neurons, the same PLC is needed for TRPA1-dependent avoidance
   of aristolochic acid. [PMID:20404155]
5. Gut immunity. Galphaq-PLCbeta-IP3-Ca2+ drives DUOX ROS production against gut microbes.
   [PMID:19289084] It acts downstream of Hh and Cad99C signalling endosomes after uracil
   sensing. [PMID:25639794]
6. Renal (Malpighian tubule) signalling. norpA is needed for CAP2b- and leucokinin-stimulated
   IP3/Ca2+ signalling and diuresis. [PMID:12547945]

## Reviews

PMID:10611962 (Montell 1999), PMID:11707492 (Hardie 2001), PMID:8570597 (Zuker 1996),
PMID:12765677 (Harteneck 2003), PMID:22283804 (Shortridge 2012, norpA history).
