# unc-29 (C. elegans; UniProt P48181) - manual literature synthesis

No deep-research API was available in this session. This file was written by hand from the
cached publications in `publications/` and PubMed metadata lookups. Every assertion carries
its provenance.

## Identity

- UNC-29 (T08G11.5, WBGene00006765) is a 493-aa non-alpha (beta-type) subunit of the
  Cys-loop ligand-gated ion channel superfamily (Pfam PF02931 ligand-binding domain,
  PF02932 transmembrane domain; four TM helices; signal peptide 1-26). UniProt: "Non-alpha
  subunit of nicotinic acetylcholine receptor (nAChR)" [UniProt P48181 CC FUNCTION,
  ECO:0000269|PubMed:15990870].
- Cloned as one of the levamisole resistance genes: "unc-38 encodes an alpha subunit while
  lev-1 and unc-29 encode non-alpha subunits" [PMID:9221782, abstract].

## Molecular function: subunit of the levamisole-sensitive AChR (L-AChR)

- Oocyte expression of UNC-29 with UNC-38 (and LEV-1) gives levamisole-induced currents
  blocked by nAChR antagonists [PMID:9221782 "Expression in Xenopus oocytes of combinations
  of these subunits that include the unc-38 alpha subunit results in levamisole-induced
  currents"].
- Full functional reconstitution requires five subunits (UNC-29, LEV-1, UNC-38, UNC-63,
  LEV-8) plus three ancillary proteins (RIC-3, UNC-50, UNC-74); "We demonstrate that 3
  alpha- and 2 non-alpha-subunits assemble into the same receptor" and "functional receptors
  were virtually eliminated when 1 or more of the 5 receptor subunits were omitted"
  [PMID:19020092]. The receptor is gated by acetylcholine and levamisole; nicotine is an
  allosteric inhibitor rather than an agonist [PMID:19020092 abstract].
- UNC-29 therefore contributes to, but does not on its own carry, acetylcholine-gated cation
  channel activity: it is a non-alpha subunit of a heteropentamer.
- In vivo purification: "Multiple peptides of each of the levamisole receptor subunits,
  UNC-29, UNC-38, UNC-63, LEV-8, and LEV-1, were identified in four different purifications"
  [PMID:15990870].

## Location

- Body-wall and head muscle and a subset of neurons ("An UNC-29-GFP fusion shows that UNC-29
  is expressed in body and head muscles" [PMID:9221782]; "both UNC-29 (ref. 20) and UNC-38
  ... are also expressed in a subset of neurons" [PMID:10461217]).
- Postsynaptic clusters at NMJs: "UNC-38∷3xMYC showed complete colocalization in the
  nervecord puncta with UNC-29∷GFP" and these puncta were "juxtaposed to, but did not
  overlap with, presynaptic synaptobrevin" [PMID:15990870].
- Cell-surface labelling in live worms: antibodies "specifically labelled synaptic regions on
  the cell surface of muscles and neurons" [PMID:16466809, abstract].
- Synaptic clustering depends on the extracellular scaffold LEV-10/LEV-9/OIG-4; "The L-AChR
  subunit UNC-29 and the LEV-10 protein were co-immunoprecipitated with GFP-OIG-4"
  [PMID:21252855]. ER maturation is enhanced by CRLD-1 ("UNC-29 expression was decreased by
  approximately 50% in crld-1(tm3993) mutants") [PMID:30407909].

## Physiological role

- Neuromuscular transmission: body-wall muscle levamisole response "was eliminated in
  mutants lacking either the unc-38 or unc-29 genes"; the L-AChR and a second, nicotine-
  sensitive AChR (ACR-16) both carry synaptic current: "we demonstrated that all three
  receptor types function at neuromuscular synapses" [PMID:10461217].
- Locomotion: unc-29 mutants are uncoordinated (Brenner screen) [PMID:4366476]; residual
  motility is due to ACR-16-containing N-AChR [PMID:10461217].
- Egg laying: unc-29 is "essential for the stimulation of egg laying by levamisole" but has
  "only subtle effects on egg-laying behavior in the absence of drug" [PMID:11290716].
- Male mating: in the backward command interneuron AVA, partially redundant AChRs containing
  ACR-18, UNC-29 and ACR-16 mediate PVY/PVX-induced reversal; AVA-specific unc-29(+) rescues
  the unc-29; acr-16 reversal defect [PMID:23577128].

## References whose cached text could not support the GOA row

- PMID:19028454 (SYN-1/AEX-1 defecation paper; full text cached): unc-29 is not named in the
  cached text, so the "regulation of muscle contraction" IMP row cannot be verified there.
- PMID:12657671 (EGL-21 CPE), PMID:12750328 (pharyngeal pumping) and PMID:23351035 (nicotine
  approach, acr-5/acr-15): abstract-only and none names unc-29 in the abstract.
