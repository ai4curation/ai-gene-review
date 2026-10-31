# Akap5 (rat, P24587) - manual literature synthesis

No deep-research API was available for this review. This synthesis was written by hand
from the cached publications in `publications/` and the UniProt record
(`Akap5-uniprot.txt`). Quotes are verbatim from those sources.

## Identity

- Rat Akap5 = AKAP150 (P150), the rodent ortholog of human AKAP79 (P24588) and mouse
  Akap5 (D3YVF0). 714 aa; the rodent protein is longer than human AKAP79 because of a
  central array of 28 eight-residue repeats (V-G-Q-A-E-E-A-T) (UniProt FT REGION 305..597).
- Cloned from a rat brain expression library with RII-beta as a probe: "cDNA inserts
  (800 and 1100 base pairs) subcloned into expression plasmids directed the production of
  partial P150 polypeptides in Escherichia coli that bind RII-B" [PMID:2538452].
- Domain architecture (UniProt): N-terminal polybasic targeting region (1..164,
  "Essential to the intracellular anchoring function"), AKAP CaM-binding motif (74..94,
  PROSITE PS51893), RII-binding amphipathic helix (675..696), C-terminal NFATC2 tether
  (697..714), palmitoylation at Cys36/Cys123 (by similarity). InterPro IPR042375 (AKAP5),
  IPR001573 (AKAP WSK motif); PANTHER PTHR15182:SF0.

## Core activity: a multivalent anchoring scaffold

- Binds PKA RII and calcineurin (PP2B) and PKC; "Each enzyme is inhibited when bound to
  the anchoring protein" (UniProt CC SUBUNIT).
- PP2B and PKA co-IP with AKAP150 from rat myometrial plasma membranes: "Both PKA and
  PP2B coimmunoprecipitated with an antibody against the 150-kDa AKAP found in rat
  myometrial plasma membranes" [PMID:10598575].
- Recruitment to glutamate receptors via MAGUKs: "glutamate receptors and PKA are
  recruited into a macromolecular signaling complex through direct interaction between
  the MAGUK proteins, PSD-95 and SAP97, and AKAP79/150. The SH3 and GK regions of the
  MAGUKs mediate binding to the AKAP" [PMID:10939335].
- Membrane/actin targeting: the N-terminal basic domain "also binds F-actin in a
  calmodulin- and PKC-regulated" manner [PMID:12177200]; "AKAP79/150 postsynaptic
  targeting requires three N-terminal basic domains that bind F-actin and acidic
  phospholipids" and it interacts with cadherins [PMID:15930126].
- Context-dependent enzyme use: "AKAP79/150 coordinates different enzyme combinations to
  modulate the activity of two distinct neuronal ion channels: AMPA-type glutamate
  receptors and M-type potassium channels" [PMID:16460836].

## Adenylyl cyclase 8 (key paper PMID:20410303, full text read)

- GST pull-down screen: "Our initial screen using GST pull-down assays identified AKAP79
  and its rodent orthologue AKAP150 as candidate binding partners for AC8."
- Binding maps to AC8 residues 1-77: "interaction between either AKAP79 or AKAP150 and
  AC8 occurred within the first 77 amino acids of the N terminus of AC8".
- Endogenous complex in mouse MIN6 cells: "Using the AKAP150-specific antibody to
  immunoprecipitate endogenous AKAP150 from MIN6 cell lysates, we could demonstrate the
  interaction with endogenously expressed AC8".
- Function: knockdown of AKAP150 in MIN6 "produced a marked potentiation of cAMP
  production"; overexpression in rat hippocampal neurons "significantly delayed the
  Ca2+-dependent rise in AC activity"; "AKAP79/150 dampens Ca2+-dependent AC8 activity as
  a consequence of its interaction with the enzyme".
- Caveat in the paper itself: in HEK293 cells AKAP150-HA overexpression "had opposing
  effects on Ca2+-stimulated AC8 activity compared with AKAP79-HA, resulting in enhanced
  cAMP production during CCE"; authors attribute this to a non-native context ("Both
  AKAP79 and AKAP150 behaved similarly when studied in their native environments").
  Neuronal knockdown was "difficult to interpret".
- Follow-up: AKAP79 recruits PKA, which phosphorylates AC8 Ser-112 to slow cAMP
  production: "AKAP79-targeted PKA reduced the on-rate of cAMP production in wild-type but
  not non-phosphorylatable mutants of AC8" [PMID:22976297].

## Synaptic roles (mostly rat hippocampal neurons)

- Localization: "AKAP150 was close to asymmetric synapses" and not at inhibitory
  synapses [PMID:15951119]; NMDA receptor activation causes "persistent redistribution
  of AKAP79/150 and PKA-RII, but not PP2B/CaN, from postsynaptic membranes to the
  cytoplasm" [PMID:16510716].
- AMPAR endocytosis/LTD: "expression of a mutant AKAP150 that does not bind calcineurin
  inhibited this NMDAR-triggered trafficking event" [PMID:19169250].
- Spines: "RNA interference knockdown of AKAP150 decreased dendritic spine area only in
  mature neurons" [PMID:19535604].
- GABA-A receptors: AKAP150 "directly binds to the receptor beta1 and beta3" subunits
  [PMID:12595241]; but in vivo it is not at inhibitory synapses [PMID:15951119].

## Ion channel / calcineurin-NFAT signaling

- CaV1.2: "CaV1.2 interacts directly with AKAP79/150, which binds both PKA and the
  Ca2+/calmodulin-activated phosphatase calcineurin (CaN)"; "activation of the
  transcription factor NFATc4 via local Ca2+ influx through L-type channels requires
  AKAP79/150" [PMID:17640527].
- "RNAi-mediated depletion of endogenous AKAP150, the rat orthologue of human AKAP79,
  eliminates NFAT activation in neurons" [PMID:22343722].
- TRPV1: knockdown "led to a significant reduction in PKA phosphorylation of TRPV1 in
  cultured TG neurons" [PMID:18381233]; "If binding is prevented, then sensitization by
  both bradykinin and PGE(2) is abrogated" [PMID:18701070]. Both indicate AKAP150
  promotes (not inhibits) TRPV1 activity.
- BK channels: "a BKCa–β2AR–AKAP150 complex exists in native tissue" [PMID:15141163].

## Receptor partners

- beta2-AR (rat brain co-IP) [PMID:15141163]; beta2AR/GluR1/PSD95/PKA/AKAP150 complex
  [PMID:20395454]; beta1-AR ternary complex with AKAP79 and PKA [PMID:16940053].

## Expression-only studies (IEP)

- Exercise-trained adipocytes [PMID:12150937], electroconvulsive shock [PMID:14732469],
  pregnancy myometrium [PMID:12135903], developmental increase in cultured neurons
  [PMID:19535604]. These report expression changes only.

## Negative search results

- None of the cached Akap5 publications reports a role for AKAP150 in oocyte meiotic maturation.
